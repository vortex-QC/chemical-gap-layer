#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分析框架_ET链甜蜜点_v0.1.py
化学间隙层 v0.2 检验：生物 ET 链逐站 Marcus 甜蜜点判读

数据源：data_et_chain.json（2026-09-02 数据考古落盘，全部数值带来源）
判读规则（-ΔG°/λ = r）：
  r < 0        uphill（上坡，前史——需要后续站回补能量）
  0 ≤ r < 0.8  normal（正常区：靠近活化带上升沿，"甜蜜点下沿"）
  0.8 ≤ r ≤ 1.25  activationless（活化顶：|−ΔG°−λ| 小，速率对驱动力最不敏感）
  r > 1.25     inverted（反转区：越放热越慢，用于抑制复合/短路）

λ 口径（双口径，明确标注）：
  口径A【站点实测/作者采用值】：站点有核验 λ 用之（RC 0.25-0.5；CI 0.5；bc1 1.0；CcO 0.7）
  口径B【链级 generic】：RC 初始电荷分离 0.25 eV（Nobel 讲稿核验）；
        呼吸链 0.7 eV（Moser/Dutton 2006 "we use a generic value of 0.7 eV" 核验）；
        呼吸链备用 1.0 eV（bc1 cytochrome 口径核验值）
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data_et_chain.json")
ACCESSED = "2026-09-02"

def classify(r):
    if r is None: return "no_data"
    if r < 0: return "uphill"
    if r < 0.8: return "normal"
    if r <= 1.25: return "activationless"
    return "inverted"

def region_from_dG(dG, lam):
    """dG: ΔG° (eV, 负=放热)。lam: λ (eV)。返回 (r, region)。"""
    if dG is None or lam in (None, 0): return None, "no_data"
    r = (-dG) / lam
    return r, classify(r)

def main():
    d = json.load(open(DATA, encoding="utf-8"))
    rows = []  # (chain, site, dG, lam_used, lam_caliber, r, region)

    # ---------- 链A：光合反应中心 ----------
    A = d["chain_A_photosynthetic_RC"]["sites"]
    LAM_RC_CALIB = 0.25  # Nobel 讲稿口径（verified）
    for s in A:
        name = s["site"]
        dG = s.get("dG_eV")
        dGv = dG.get("value") if isinstance(dG, dict) else None
        lam = s.get("lambda_eV")
        lamv = lam.get("value") if isinstance(lam, dict) else None
        # 口径A：站点 λ
        r, reg = region_from_dG(dGv, lamv)
        if r is not None:
            rows.append(("A_RC", name, dGv, lamv, "site_measured", r, reg))
            continue
        # 口径B：链级 0.25 eV（RC 初始电荷分离口径）
        r, reg = region_from_dG(dGv, LAM_RC_CALIB)
        if r is not None:
            rows.append(("A_RC", name, dGv, LAM_RC_CALIB, "RC_calib_0.25(Nobel)", r, reg))
        else:
            rows.append(("A_RC", name, None, None, "-", None, "no_dG_data"))

    # ---------- 链B：呼吸链 ----------
    B = d["chain_B_respiratory_chain"]
    lam_b_calib = 0.7   # Moser/Dutton generic（verified）
    for comp in ["complex_I", "complex_III_bc1", "complex_IV_cytC_oxidase"]:
        for s in B[comp]["sites"]:
            name = f"{comp}:{s['site']}"
            dG = s.get("dG_eV")
            dGv = dG.get("value") if isinstance(dG, dict) else None
            lam = s.get("lambda_eV")
            lamv = lam.get("value") if isinstance(lam, dict) else None
            r, reg = region_from_dG(dGv, lamv)
            if r is not None:
                rows.append((comp, name, dGv, lamv, "site_measured", r, reg))
                continue
            r, reg = region_from_dG(dGv, lam_b_calib)
            if r is not None:
                rows.append((comp, name, dGv, lam_b_calib, "resp_calib_0.7(Moser2006)", r, reg))
            else:
                rows.append((comp, name, None, None, "-", None, "no_dG_data"))

    # ---------- 输出 ----------
    print("=" * 108)
    print(f"{'链':10} {'站点':46} {'ΔG°(eV)':>9} {'λ(eV)':>6} {'口径':28} {'r=-ΔG°/λ':>9}  区域")
    print("-" * 108)
    counts = {}
    for chain, name, dGv, lam, cal, r, reg in rows:
        rstr = f"{r:9.2f}" if r is not None else "      ---"
        dg = f"{dGv:9.2f}" if dGv is not None else "      ---"
        print(f"{chain:10} {name:46} {dg} {lam if lam else 0:6.2f} {cal:28} {rstr}  {reg}")
        counts[reg] = counts.get(reg, 0) + 1
    print("-" * 108)
    total = sum(v for k, v in counts.items() if k not in ("no_dG_data", "no_data"))
    print(f"统计：可判读 {total} 站 → {counts}")
    if total:
        ok = counts.get("normal", 0) + counts.get("activationless", 0)
        print(f"正常区+活化顶占比：{ok}/{total} = {100*ok/total:.0f}%")
        print(f"反转区：{counts.get('inverted',0)} 站（预期=保护性通道：电荷复合/防短路）")
        print(f"上坡步：{counts.get('uphill',0)} 站（需门控/邻站回补）")
        print(f"缺 ΔG° 数据：{counts.get('no_dG_data',0)} 站（标 no_data，不进判读）")
    print()
    print("判读说明：")
    print("  1. r=-ΔG°/λ 中 ΔG° 为负（放热）时 r>0；uphill=ΔG°>0。")
    print("  2. 无站点 ΔG° 的站一律 no_data，不做甜蜜点宣称（去幻纪律）。")
    print("  3. λ 双口径：站点实测值优先；链级 generic（RC 0.25 / 呼吸链 0.7）标入口径列。")

    # 机器可读落盘
    out = {
        "meta": {"accessed": ACCESSED, "rule": "r=-dG/lambda; <0 uphill; 0-0.8 normal; 0.8-1.25 activationless; >1.25 inverted",
                 "lambda_calib": {"RC": "0.25 eV (Nobel lecture, verified)", "respiratory": "0.7 eV (Moser/Dutton 2006, verified)"}},
        "rows": [
            {"chain": c, "site": n, "dG_eV": g, "lambda_eV": l, "lambda_caliber": cal,
             "r": (round(r, 3) if r is not None else None), "region": reg}
            for c, n, g, l, cal, r, reg in rows
        ],
        "summary": counts
    }
    outp = os.path.join(HERE, "ET链甜蜜点判读_v0.1_out.json")
    with open(outp, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"\n机器可读结果已写：{outp}")

if __name__ == "__main__":
    main()
