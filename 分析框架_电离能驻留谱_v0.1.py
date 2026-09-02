#!/usr/bin/env python3
# 化学间隙层 v0.1 判别①：电离能谱=间隙驻留谱 全谱核对
# 判别逻辑：
#   核心预言：逐级电离能的【跳变点】= 壳层（驻留层）边界
#   体系内读法：壳层=间隙驻留深度分层；电离=从浅驻留位剥离；
#   跳变（比上一级大>2x）=剥离深度突增=穿越驻留层边界=进入下一壳层
# 判定标准（预注册）：
#   跳变定义：IE(n+1)/IE(n) >= 2.0
#   通过条件：全部跳变点与已知壳层构型边界一致（无假阳/漏检）
# 数据灌入口：data_ionization.json（考古代理落盘）
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

# 已知壳层边界（Z=1-36，构型中 n+l 或主层切换点）：跳变应发生在"剥完一个壳层"处
# 例如 Li(1s2 2s1): IE2/IE1 跳变（He 核→Li 核）；Na: IE2/IE1；Al: IE4/IE3（3p 剥完进 3s2）
EXPECTED = {
    "H": [], "He": [],
    "Li": [2], "Be": [3],   # Be: IE3/IE2 跳变（2s 剥完进 1s2）
    "B": [4],  "C": [5], "N": [6], "O": [7], "F": [8], "Ne": [9],
    "Na": [2], "Mg": [3], "Al": [4], "Si": [5], "P": [6], "S": [7], "Cl": [8], "Ar": [9],
    "K": [2], "Ca": [3],
    # 过渡金属跳变位置复杂（3d/4s 混层），标注为"复杂区"单独判读
}

def main():
    p = os.path.join(BASE, "data_ionization.json")
    if not os.path.exists(p):
        print("data_ionization.json 未落盘——考古代理未完成，框架就绪等待灌入")
        return
    D = json.load(open(p))
    print("=" * 72)
    print("判别①：逐级电离能跳变点 vs 壳层边界（预注册：ratio>=2.0 判跳变）")
    print("=" * 72)
    n_pass = n_fail = n_skip = 0
    for sym, e in sorted(D.items(), key=lambda kv: kv[1].get("Z", 0)):
        ies = e.get("ie_eV") or []
        ies = [x for x in ies if x]
        if len(ies) < 3:
            n_skip += 1
            continue
        jumps = [i+2 for i in range(len(ies)-1) if ies[i+1] / max(ies[i], 1e-9) >= 2.0]
        exp = EXPECTED.get(sym)
        if exp is None:
            n_skip += 1
            print(f"  {sym}(Z={e.get('Z')}) 复杂区：跳变@{jumps} 构型={ies[:4]}...")
            continue
        hit = set(jumps) == set(exp)
        if hit: n_pass += 1
        else: n_fail += 1
        print(f"  {sym}(Z={e.get('Z')}) {'✓' if hit else '✗'} 预期跳变@{exp} 实测@{jumps} IE前4级={[round(x,1) for x in ies[:4]]}")
    print(f"\n汇总：通过 {n_pass} / 失败 {n_fail} / 跳过 {n_skip}")

if __name__ == "__main__":
    main()
