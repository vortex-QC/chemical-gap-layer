#!/usr/bin/env python3
# 化学间隙层 v0.1 判别②：周期表惰性-饱和映射 预检框架
# 判别逻辑：稀有气体第一电离能排序 vs 壳层驻留饱和度（n+s^2 满壳层判定）——
# 预言：惰性排序 = 驻留饱和封闭度排序；第一电离能=最浅开放驻留位深度
# 数据灌入口：data_noble_gas.json / data_ionization.json（考古代理落盘后直接读）

import json, os, math, sys

BASE = os.path.dirname(os.path.abspath(__file__))

# 满壳层（闭壳层）判定：主族满壳 = ns2 np6（He: 1s2）
# 壳层驻留饱和度候选口径 S：闭壳层数 / 总壳层数（He=1/1, Ne=2/2, Ar=2/3, Kr=3/4, Xe=4/5, Rn=5/6）
#   —— Ar 电子构型 [Ne]3s2 3p6：填充到第3层，闭壳层2层 → S=2/3
NOBLE = [
    # symbol, Z, 填充最高主层 n, 闭壳层数 n_closed, 已知反应性等级(0=完全惰性..3=较活泼)
    ("He", 2, 1, 1, 0),
    ("Ne", 10, 2, 2, 0),
    ("Ar", 18, 3, 2, 0),
    ("Kr", 36, 4, 3, 1),   # KrF2 存在（低温）
    ("Xe", 54, 5, 4, 2),   # XeF2/F4/F6 + 氧化物
    ("Rn", 86, 6, 5, 2),   # 反应性推断>Xe（实验受限）
]

def load_ionization():
    p = os.path.join(BASE, "data_ionization.json")
    if os.path.exists(p):
        return json.load(open(p))
    return {}

def main():
    ion = load_ionization()
    print("=" * 72)
    print("判别②预检：惰性排序 vs 壳层驻留饱和度 S=n_closed/n_max")
    print("=" * 72)
    print(f"{'元素':<4}{'Z':<4}{'S饱和度':<10}{'IE1(eV)':<12}{'反应性等级':<10}{'S×IE1积':<10}")
    rows = []
    for sym, Z, nmax, nclose, react in NOBLE:
        S = nclose / nmax
        ie1 = None
        if ion and "elements" in str(type(ion)):
            pass
        if ion:
            e = ion.get(sym) or ion.get(str(Z))
            if e and "ie_eV" in e and e["ie_eV"]:
                ie1 = e["ie_eV"][0]
        rows.append((sym, Z, S, ie1, react))
        prod = (S * ie1) if ie1 else None
        print(f"{sym:<4}{Z:<4}{S:<10.3f}{str(ie1):<12}{react:<10}{str(prod):<10}")

    # 核心判别1：反应性随 S 递减（越接近全闭壳越惰性）
    print("\n判别1：S 饱和度高的元素应更惰性（反应性等级低）")
    for sym, Z, S, ie1, react in rows:
        print(f"  {sym}: S={S:.3f} 反应性={react} {'✓' if (S >= 0.9) == (react == 0) else '·'}")
    print("  注：Ar S=2/3 但完全惰性——本口径下 Ar 是关键反例（ns2np6 价壳层封闭")

    # 修正口径：饱和度应以【价壳层】为准（价壳封闭=惰性主判据）
    #   He 1s2 ✓ / Ne 2s2p6 ✓ / Ar 3s2p6 ✓ / Kr 4s2p6 ✓ / Xe 5s2p6 ✓ —— 全部价壳封闭！
    print("\n★修正判读：六元素价壳层全部封闭（ns2np6）——单纯'价壳封闭'不能区分 He/Ne/Ar")
    print("  与 Xe/Rn 的反应性差异 → 差异变量=驻留深度（IE1 递减：He 24.6 → Rn 10.7 eV）")
    print("  → 体系内读法：惰性=驻留饱和封闭，但【封闭强度】随主量子数 n 递减")
    print("    （外层间隙驻留离核远=浅=易被打开）——IE1=封闭强度的直接读数")
    print("  → 判别2：反应性阈值——IE1 低于某阈值（~12 eV? Xe=12.13 第一反应性元素）出现反应性")

    # 核心判别2：IE1 与反应性的对应（阈值候选）
    print("\n判别2：IE1 阈值候选（数据灌入后自动核）")
    for sym, Z, S, ie1, react in rows:
        if ie1:
            mark = "★反应性起点" if react > 0 else ""
            print(f"  {sym}: IE1={ie1} eV 反应性={react} {mark}")

    print("\n（数据考古落盘后重跑本脚本自动升级为全谱核对）")

if __name__ == "__main__":
    main()
