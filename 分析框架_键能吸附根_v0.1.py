#!/usr/bin/env python3
# 化学间隙层 v0.1 判别③：键能-吸附根定量对照
# 判别逻辑（质量双根语言）：键能=吸附根的分子级显化（场强驻留深度）
#   检验A：同族键能梯度（C-F>C-Cl>C-Br>C-I）= 驻留深度梯度（电负性=间隙抢占能力）
#   检验B：键级系列 N-N/N=N/N≡N 的超线性 vs C-C 系列近线性——
#         N≡N 945 kJ/mol = 深驻留（禁闭同构）；N-N 163 = 独对斥力压浅驻留
#   检验C：F-F 反常弱（159 < Cl-Cl 243）——独对驻留位挤占
# 数据灌入口：data_bond_energy.json

import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

def load():
    p = os.path.join(BASE, "data_bond_energy.json")
    if os.path.exists(p):
        return json.load(open(p))
    return {}

def main():
    D = load()
    if not D:
        print("data_bond_energy.json 未落盘（考古代理未完成）——先输出框架说明")
        return

    def E(b):
        v = D.get(b, {})
        return v.get("energy_kJ_mol")

    print("=" * 72)
    print("判别③：键能-吸附根定量对照")
    print("=" * 72)

    # 检验A：卤化氢/碳卤同族梯度
    print("\n检验A：同族梯度=驻留深度梯度（电负性递减→键能递减）")
    for fam in (["H-F", "H-Cl", "H-Br", "H-I"], ["C-F", "C-Cl", "C-Br", "C-I"]):
        vals = [(b, E(b)) for b in fam]
        ok = all(v is not None for _, v in vals)
        seq = [v for _, v in vals if v]
        mono = all(seq[i] > seq[i+1] for i in range(len(seq)-1)) if ok else None
        print(f"  {fam}: {'单调递减✓' if mono else ('非单调✗' if ok else '数据缺失')} {vals}")

    # 检验B：键级系列超线性
    print("\n检验B：键级系列——N 系超线性（深驻留）vs C 系近线性")
    for series, name in ((["N-N", "N=N", "N≡N"], "N系列"), (["C-C", "C=C", "C≡C"], "C系列")):
        vals = [E(b) for b in series]
        if all(vals):
            r12, r23 = vals[1]/vals[0], vals[2]/vals[1]
            print(f"  {name}: {vals}  单→双 {r12:.2f}x, 双→三 {r23:.2f}x  "
                  f"{'超线性' if vals[2]/vals[0] > 2.5 else '近线性'}")
            if name == "N系列" and vals[0] and vals[2]:
                print(f"    N≡N/N-N = {vals[2]/vals[0]:.2f}x（C系列 {E('C≡C')/E('C-C'):.2f}x 对照）")

    # 检验C：F-F 反常
    print("\n检验C：F-F 反常弱（独对驻留挤占）")
    ff, clcl = E("F-F"), E("Cl-Cl")
    if ff and clcl:
        print(f"  F-F={ff} < Cl-Cl={clcl} kJ/mol：{'✓反常成立' if ff < clcl else '✗'}"
              f"——周期表唯一 F2 弱于 Cl2 的同族；体系内读法=F 独对驻留位挤占使单键驻留浅化，"
              f"而 F-C 键反而最强（共享驻留增益>挤占代价）")

if __name__ == "__main__":
    main()
