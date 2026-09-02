# 数据考古报告 · 生物 ET 链逐站参数 v0.1

- 签写：2026-09-02（系统时间 `date` 核验：2026-09-02 12:57 CST 起作业，全部网络访问发生于当日）
- 作业代理：数据考古子代理（ZCode）
- 数据落盘：`papers/chemical_gap_layer/data_et_chain.json`（A 链 7 站 + B 链 18 站 + 链级注记 8 条）
- 判读脚本：`papers/chemical_gap_layer/分析框架_ET链甜蜜点_v0.1.py`（输出 `ET链甜蜜点判读_v0.1_out.json`）
- 用途：检验化学间隙层 v0.2"生物 ET 链 = 驻留深度甜蜜点级联"主张

## 一、核验通道与方法

| 通道 | 用途 | 状态 |
|---|---|---|
| Europe PMC REST（search/abstract） | 检索+摘要逐字核验 | 用上，主力 |
| NCBI PMC efetch（db=pmc XML） | 开放获取全文 | 用上，主力（PMC4230448/5511282/8433477/9720722/3535674 等） |
| pmc.ncbi.nlm.nih.gov 网页 HTML | XML 拿不到时的全文镜像 | 用上（Darwin/Moser 2006 论文，232 KB） |
| PubMed eutils（esearch/efetch abstract） | 摘要逐字核验 | 用上 |
| Nobel 官网 PDF（本地缓存 /tmp/marcus_dig/marcus_nobel.pdf，本会话再次引用） | Marcus 1993 讲稿原文 | 用上（λ 0.25 eV、3 ps、200 ps、1.1 eV 全出自此） |
| Crossref api.crossref.org | DOI 逐字核验（22 个 DOI 全过） | 用上 |
| Europe PMC fullTextXML 端点 | 全文 XML | **间歇性失败**（空响应/504/SSL EOF），见"失败通道" |

纪律：每个数值都有实际访问文本支撑（原文引句入 JSON）；训练记忆/任务书记忆值只进 `unverified_reference_values` 字段并显式标注；未核验数值 0 个混入核验字段。

## 二、任务A：光合反应中心（Rb. sphaeroides）逐站参数

### 已核验级联（速率链完整）

| 站点 | 时间常数 | 来源 |
|---|---|---|
| cyt c2 → P+ | τ≈1 μs（结合态）/100 μs（遭遇复合物） | Miyashita/Okamura/Onuchic PNAS 2005 摘要（PMID 15738426） |
| P* → P+BA− | 3–5 ps | PMC6023262（JPC Lett 2018）原句："the P* → P+BA−, P+BA− → P+HA−, and P+HA− → P+QA− ET steps occur with time constants of 3–5, 0.5–1, and ∼200 ps, respectively"；B*→P+BA− 通道 0.2–0.5 ps |
| P+BA− → P+HA− | 0.5–1 ps | 同上 |
| P+HA− → P+QA− | ∼200 ps | 同上 + Marcus 讲稿 "in 200 psec" |
| QA → QB | 10⁴–10⁵ s⁻¹（14 Å 隧穿，modest free energy） | Moser/Page/Dutton 2006（PMC1647310）原句 |
| 复合（P+HA−→P） | 高放能 ~1.1 eV，慢（反转区保护） | Marcus 讲稿原句 |

### 已核验能量/λ 参数

- **P+/P Em = 505 mV**（WT）；突变系列 410–765 mV（Venturoli 1998，PMID 9635776）。
- **cyt c2→P ΔG° = −160 meV（WT）**，突变体系 −65 至 −420 meV；Marcus 拟合 **λ = 500 meV**（Lin 1994，PMID 7947761）；同体系 Jortner/全谱拟合 λ = 0.96±0.07 eV（Venturoli 1998）——两口径并存，已标注。
- **P*→BPh 第一步驱动力 ~0.25 eV**（占 BChl₂* 激发能 1.38 eV 的一小部分）；**λ ~0.25 eV**；**复合通道 −ΔG° ~1.1 eV + 小 λ 0.25 eV → 反转区抑制复合**（Marcus Nobel 讲稿原文，三句全核）。
- **P+QA− 相对 P* 自由能 = −910±20 meV**（pH 8，天然泛醌；延迟荧光法，PMID 10866934）——三步前向 ET 总驱动力。
- **QA→QB 距离 14 Å**（Moser/Dutton 2006）；GluL212 质子化基团簇与初级半醌相互作用能 ~50 meV（同延迟荧光论文）。
- **RC 初始电荷分离 λ = 0.25–0.5 eV**、**QB 位点再氧化（耦合质子交换）λ = 1.1–1.5 eV**（Moser/Page/Dutton 2006 原句）。
- cyt c2→RC 跨水界面隧穿 **β = 1.1 Å⁻¹**（PMID 15738426）。
- B 支路（对称支路）：蓝光激发数百 fs 生成 B_B⁺H_B−、~15 ps 衰减，只做光保护不做输运（PMID 11705365）——级联"单边选择性"证据。

### 未核验（如实标注）

- BChl→Bphe、Bphe→QA 两步的单站 ΔG° 与 λ；P−B、B−H 边到边距离；QA/QB 单醌 Em（Bphe ≈−550 mV、QA≈−100 mV 等教科书值全部未核，入待核验参考）。
- P+H− 复合速率常数具体数值（PSII 类比值 −ΔG°≈1.2 eV/32 Å→k=3.4e−3 s⁻¹ 已在前次考古核验，Boussac 2013）。

## 三、任务B：呼吸链 Complex I-IV 逐站

### Complex I（FeS 间全部 6 跳 + FMN 起点 + Q 端，Table 1 完整）

来源：Hayashi & Stuchebrukhov JPCB 2011（PMC4230448，全文 Table 1）+ Sci Rep 2017（PMC5511282）。

| 跳 | ΔG° | C-to-C/G-to-G 距离 (Å) | k（干蛋白/含水） |
|---|---|---|---|
| N3→N1b | 0 eV | 14.0/11.0 | 1.3e3 / 2.9e6 s⁻¹ |
| N1b→N4 | 0 eV | 13.5/10.6 | 6.4e4 s⁻¹ |
| N4→N5 | 0 eV | 12.2/8.7 | 2.8e7 s⁻¹ |
| N5→N6a | 0 eV | 16.8/14.0（边到边 14.1） | 9.1 / 7.3e3 s⁻¹（最长跳=限速候选） |
| N6a→N6b | 0 eV | 12.1/9.3 | 2.8e6 s⁻¹ |
| N6b→N2 | −0.15 eV | 13.7/10.5 | 1.9e4 / 1.8e6 s⁻¹ |

- λ 口径：Hayashi 取 **0.5 eV**；Sci Rep 2017 记文献 generic **0.7–0.8 eV**，并主张用"有效重组能 λr"。
- 电位剖面："essentially flat"，N2 比其余高 ~100 meV；全链隧穿 ~200 μs（另有 ~90 μs 报道），周转 5 ms。
- 结构：7 簇 84 Å 链，簇间距最大 14 Å；N1a/N7 不在主链（Sazanov 2005 Science，PMID 16051796）。
- 光合 CI 实测电位（Nature Comm 2021，PMC8433477）：**N2 = −220±15 mV、N1 = −230±15 mV、N0 < −550 mV、PQ 池 +80 mV**；半醌距 N2 ~12 Å；N2 = 电子阱防反向产超氧。

### Complex III（bc1）——Rieske 门控证据链

来源：Millett/Havens/Rajagukguk/Durham BBA 2013 综述（PMC3535674，全文）。

| 跳 | ΔG° | 距离 | k |
|---|---|---|---|
| QH2(Qo)→2Fe2S | 未核到数值 | 未核到 | k3=1650 s⁻¹（Rs 色素载体；牛 250；P.d. 700）——**限速步** |
| Q•−→heme bL | 未核 | 未核 | k4 > 1e9 s⁻¹ |
| bL→bH | 未核 | 未核 | 半衰期 0.1 ms（Shinkarev 瞬态电场） |
| 2Fe2S→c1 | **−0.02 V（pH7）→ +0.115 V（pH10，His161 去质子化）** | **9.9 Å** | WT k2=8.0e4 s⁻¹（Rs，Ru 法）；牛 1.6e4；P.d. 1.07e4；**λ = 1.0 eV** |
| c1→cyt c | 未核 | 未核 | >1e4 s⁻¹；酵母 Ru 法 3900 s⁻¹ |

**关键发现（门控）**：ISP 突变使 2Fe2S Em 降 62/109/159 mV，按 Marcus（λ=1.0 eV）预测速率应升最多 17 倍，**实测 k2 完全不变**——2Fe2S→c1 被 ISP 结构域 57° 转动（构象门控）限速，不是真 ET 限速（综述原句 "rate-limited by the rotational dynamics of the iron-sulfur protein rather than true electron transfer"）。这是"甜蜜点级联外还叠着门控"的直接一级证据。

- bc1 可逆性/防短路（Moser/Dutton/Osyczka Nature 2004 摘要核验）：毫秒可逆性下半醌模型易短路；两保险——半醌构象门控或协同双电子化学——把短路 relegated 到秒级。
- b6f 对比（JPCB 2022，PMC9720722 全文）：b6f bp/bn Em = −80/−111 mV、bc1 bl/bh = −124/（−30/+120 双组分）mV；**b6f 跨膜 ET 出现上坡步**（高→低电位血红素）——"级联未必单调"的实测反例，供理论注意。

### Complex IV（CcO）——电位表+距离+速率三全（Moser/Page/Dutton 2006 Table 1/3）

- Em 表（verified）：CuA 0.24 V（Moody/Rich 1990）；haem a 0.26 V；a3 II/III 0.28（氧化态估 0.32）V；a3 III/IV 0.6 V；CuB 0.26 V；Tyr• 1.0 V。中心间静电互作 35–40 mV。
- O2 单电子偶溶液值 −0.33/0.94/0.305/2.33 V；催化位"拉平"至 0.81 V（100% 拉平假设）或 −0.27/0.93/0.33/2.25 V（5% 拉平）。
- 站点表：

| 跳 | ΔG° (eV) | 距离 (Å) | k 实测 | k 计算（λ=0.7, ρ 口径） |
|---|---|---|---|---|
| cyt c→CuA | 未核单值 | 未核 | τ≈1 μs（β=1.1 Å⁻¹） | — |
| CuA→a | −0.02 | 16.1 | 3.0e4 s⁻¹（Adelroth 1995） | 3.0e3（ρ=0.76）/8.7e4（ρ=0.87） |
| a→a3 | −0.02 | 7.0 | pre-2001: 3e5；post-2001: 7e8（Pilet 2004，1.2 ns） | 6.5e8–1.4e9 |
| CuA→a3（短路） | −0.04 | 18.9 | 4 s⁻¹（Kannt 1999） | 90/40/0.17/250 s⁻¹（λ 三口径） |
| a3/CuB→O2 | 微态依赖 | 簇内 a 6.9/Tyr 4.9 Å | O2 还原 30 μs | — |

- **λ 争议全程核验**：generic 0.7 eV（Moser 主张，与 53–60 meV 实测活化能自洽）；0.3 eV（Brzezinski 1996 温度拟合，Moser 判为经典 Marcus 误用核量子模式）；0.09 eV（Winkler 1995，Moser 称 unprecedented 需再检）；路径模型 0.44 eV。**同一站四个 λ 口径并存——λ 的口径纪律必要**。

### "能量浪费站"问题的学术答案（任务B-3）

1. **CI 电位平坦 ≠ 浪费**：Sci Rep 2017 原句"very little downhill reaction free energy"——设计目的是保能+稳健，不是放热；FeS 族可调范围 650 meV 提供调谐空间。
2. **N1a（off-pathway 簇）**：Hirst 组（BJ 2013，PMID 23980528）操纵 N1a 电位 ±0.16 V，证明其不影响黄素 ROS 生成，推断功能是组装/稳定——不是热力学浪费站。
3. **主链外簇 N1a/N7 + 末端高电位 N2 电子阱**：N2 最正电位防反向电子流经还原黄素产超氧（Nature Comm 2021）——高电位差站的功能是防浪费（防短路/防 ROS）。
4. **电子分岔普适解**（PNAS 2020，PMID 32801212）："energy-wasting short-circuiting reactions that have large driving forces" 由"陡自由能坡+电子占据阻塞（occupancy blockade）"绝缘——大驱动力站被结构性地排除在速率路径外，不靠微观速率常数精细调谐。
5. **CcO 短路站**：CuA→a3 直连（−0.04 eV, 18.9 Å）实测仅 4 s⁻¹，且论文明说"often considered a physiological short circuit"、需要额外位垒压到 3% 产率以下。

**小结**：文献中"明显放热过大的站"确实存在，但全部位于非速率路径（短路通道/复合通道），学术界用"距离+位垒+占据阻塞+构象门控"四件套解释其无害化；速率主链上的站要么近零驱动（CI 全链、bc1 2Fe2S→c1、CcO CuA→a），要么驱动被调在 λ 量级（RC 初始分离）。**没有发现任何文献把主链速率站设计成反转区或大幅放热浪费。**

## 四、任务C：甜蜜点判读（脚本实跑结果）

判读规则 r = −ΔG°/λ：<0 uphill；0–0.8 normal；0.8–1.25 activationless；>1.25 inverted。λ 双口径（站点实测优先，链级 generic RC 0.25/呼吸链 0.7 标注）。

```
可判读 14 站：
  normal          12 站（85.7%）——CI 全部 7 跳（r=0.00–0.30）、bc1 2Fe2S→c1（r=0.02）、
                  CcO CuA→a / a→a3 / CuA→a3 短路（r=0.03–0.06）、RC cyt c2→P（r=0.32）
  activationless   1 站（ 7.1%）——RC P*→BChl 首步（r=1.00，−0.25 eV/0.25 eV）
  inverted         1 站（ 7.1%）——RC P+H− 电荷复合（r=4.40，−1.1 eV/0.25 eV，保护通道）
  no_dG_data      11 站（不计入）——ΔG° 未核验，不判读
正常区+活化顶占比：13/14 = 93%
上坡步：0 站（判读集内；b6f 上坡步在链级注记中，实测存在于光合 b6f 跨膜步）
```

**对化学间隙层 v0.2 的判读结论**：
1. 主链速率站压倒性落在正常区（r≈0–0.3 为主）——即"活化带上升沿、驱动力 ≪ λ"的**欠驱动甜蜜点**，不是教科书"−ΔG°≈λ 顶点"。这与文献"驱动力小→可逆性高→能量保存"的设计陈述（Moser/Dutton 2006 "substrate-to-substrate ΔG values are often very small... driving forces are also constrained to be small"）自洽。
2. 唯一 activationless 站恰是 RC 第一步（P*→BChl，进化压力最大处——要抢在荧光/无辐射弛豫之前完成），唯一 inverted 站是保护性复合通道。级联结构 = 正常区运输 + 顶点起步 + 反转区刹车。
3. "级联=甜蜜点"主张成立的准确形式：**主链站全部 r≤0.8（无过冲），起步站 r≈1，废热站 r≫1**——分档严格对应功能（输运/抢时/防复合），这是驻留深度级联的文献级证据形态。
4. 门控叠加：bc1 2Fe2S→c1 与 CcO a→a3 的观测速率由构象/质子门控而非 Marcus 速率决定——与前次考古（gated ET 文献链）衔接，级联是"Marcus 正常区 + 门控限速"的双层结构。

## 五、可疑值与口径冲突清单

1. **cyt c2→P λ 双值**：0.5 eV（Lin 1994 Marcus 拟合）vs 0.96±0.07 eV（Venturoli 1998 Jortner 全局拟合）——同体系近 2 倍差，两口径均已核验，判读用 Lin 值（r=0.32）；若用 0.96 则 r=0.17，区域不变。
2. **CcO CuA→a λ 四口径**（0.09/0.3/0.44/0.7 eV）：Moser 2006 论文内部就有专节批评低温拟合口径；判读用 generic 0.7。r 对 λ 弱敏感（ΔG° 仅 −0.02 eV，r≤0.06 恒 normal）。
3. **bc1 bl/bh Em 教科书值与 2022 实测张力**：9 K 光谱+滴定给 bl=−124 mV（vs 教科书 ~+90）；引用必须带方法学标签（入待核验参考）。
4. **CI λ 0.5 vs 0.7–0.8 vs "无通用 λ"**：判读取站点采用值 0.5；ΔG°=0 或 −0.15 下区域结论不随 λ 变。
5. **弛豫控制口径**（Langevin 2001，λ_eff 70–100 meV）与经典 λ 口径不同，已隔离标注，不混入判读。
6. 任务书预设值 NADH −320 mV / Q 池 +90 mV / Rieske +280–310 / c1 +220 / cyt c +230–250 / bL +90 / bH +50：**全部未核验**（只有 PS-CI 口径 N2 −220/PQ +80 与 CcO 全表核到），在 JSON `unverified_reference_values` 中逐条列出，禁止入理论正文当核验值。

## 六、失败通道

- Europe PMC fullTextXML 端点间歇失败（空响应/504/SSL EOF）：PMC2984193（PNAS 2010 CI 隧穿）、PMC1647310 XML 多次重试失败；前者改用姊妹篇 JPCB 2011（PMC4230448，Table 1 完整取得），后者改走 PMC 网页 HTML 成功。
- royalsocietypublishing.org 被 Cloudflare 盾拦（"Just a moment..."）；改 PMC 镜像。
- NCBI pmc/utils/oa/oa.fcgi 404（端点迁移）；NCBI efetch 对非 OA 文章只回元数据。
- Europe PMC FT 全文多词组合查询频繁 0 hits/超时，需 5–6 次退避重试（已封装重试脚本）。
- PubMed 相关性检索对 RC 逐站 Em 组合查询噪声大，站级电位（Bphe/QA/QB 单值）最终未在开放获取文本核到——如需可补通道：图书馆版 Moser/Dutton 2003 "Length, time, and energy scales"（Elsevier，非 OA）与 Allen/Williams 1995 Annu Rev（非 OA）。

## 七、数据完整度自评

- 任务A：速率链 4/4 站核验（+cyt c2 前置与复合通道）；ΔG° 3/6 站核验（首步 0.25、总 0.91、复合 1.1）；λ 3 口径核验；距离 1/5（QA→QB 14 Å）。完整度：速率级联 100%，能量级联 ~50%。
- 任务B：CI 8/9 站全参数（Table 1 完整）；bc1 5/5 站速率 + 2 站 ΔG°/距离/λ；CcO 6 站电位表+3 站 ΔG°/距离/速率；"浪费站"问题 5 条机制性答案全核验。完整度：电位级联 CI+CcO 完整，bc1 站级 Em 未核（Rieske +280–310 未核验），NADH/Q 池线粒体口径未核。
- 任务C：14 站判读，正常区+活化顶 93%，反转 1 站（保护通道），与理论预期结构一致；11 站 no_data 不做宣称。
