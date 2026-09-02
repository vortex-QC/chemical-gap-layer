# 数据考古报告 · Marcus 反转区与生物电子转移 v0.1

- 签写：2026-09-02（系统时间 `date` 核验：2026年09月02日 12:20 CST 起作业，全部网络访问发生于当日）
- 作业代理：数据考古子代理（ZCode）
- 数据落盘：`papers/chemical_gap_layer/data_marcus_bio_et.json`（29 条，27 verified / 2 unverified）
- 用途：检验化学间隙层 v0.1 与 Marcus 反转区争议的兼容性

## 一、核验通道与方法

| 通道 | 用途 | 状态 |
|---|---|---|
| Crossref API | DOI/题目/作者/卷页/年份逐字核验 | 用上，19 次以上 |
| PubMed eutils（esearch/esummary/efetch） | 摘要全文逐字核验 | 用上，主要数值来源 |
| Europe PMC REST | 摘要/元数据核验 | 用上 |
| NCBI PMC efetch | 开放获取全文（β 数值、综述引文） | 用上 |
| Nobel 官网 PDF（经代理 127.0.0.1:7890） | Marcus 1993 讲稿全文（12 页，449 KB，pdftotext 解析） | 用上，最关键一手来源 |
| api.wikimedia.org（经代理） | Wikipedia Marcus_theory wikitext（41 KB） | 用上，仅二级脉络 |
| Semantic Scholar API | — | 429 限流，未用上 |
| en.wikipedia.org 直连/代理 REST | — | TLS 被切断，按预案改 api.wikimedia.org |

纪律：每个数值都有实际访问文本支撑；训练记忆值只进"待核验参考"字段并显式标注。

## 二、任务A：Marcus 反转区在生物体内的观测状态

### A1 原始预言（verified）
- Marcus 1956：J. Chem. Phys. 24, 966-978，DOI 10.1063/1.1742723（Crossref 逐字）。
- Marcus Nobel lecture：Angew. Chem. Int. Ed. 32, 1111-1121 (1993)，DOI 10.1002/anie.199311113。**注意：实际标题为 "Theory and Experiment"，不是任务书写的 "theory and practice"**（已勘误记录）。
- 反转区数学形式与图像：Nobel PDF 全文定位成功——Eq.(5b) 导出 ΔG‡=(λ+ΔG°)²/4λ 型抛物线依赖；原文 "Another prediction in the 1960 paper concerned what I termed there the inverted region"；图 8 "The Inverted Region Effect"。

### A2 化学体系首次观测（verified）
- Miller, Beitz, Huddleston, JACS 1984, 106, 5057-5068，DOI 10.1021/ja00330a004（任务书指向的文献，核验成立）。
- 但 Marcus 本人在讲稿中指认的"最佳实验证据"是：Miller, Calcaterra, Closs, JACS 1984, 106, 3047-3049，DOI 10.1021/ja00322a058（讲稿原句 "The best experimental evidence for the inverted region was provided in 1984 by Miller, Calcaterra and Closs, almost 25 years after it was predicted."）。**两篇 1984 都是首次观测的并列证据，任务书只记了前者，已补齐。**

### A3 生物体系观测状态（verified，6 正例 + 1 经典反例解释 + 1 负例 + 1 综述确认）
1. **工程化 azurin（protein-only 首次确认）**：Farver et al., J. Phys. Chem. Lett. 2015, 6, 100-105，DOI 10.1021/jz5022685："evidence of the inverted region in a 'protein-only' system has remained elusive. We herein provide such evidence in a series of nonderivatized proteins."
2. **PSII**：Boussac et al., J. Phys. Chem. B 2013, 117, 3308-3314，DOI 10.1021/jp400337j：S(n)TyrZ•QA-• 电荷复合在反转区，-ΔG°≈1.2 eV，~32 Å 单步隧穿。
3. **mini CuI 金属蛋白**：Hong et al., Angew. Chem. Int. Ed. 2006, 45, 6137-6140，DOI 10.1002/anie.200601517（标题即结论）。
4. **Zn-cyt c / cyt c 氧化酶**：Brzezinski et al., Biophys. Chem. 1995, 54, 191-197，DOI 10.1016/0301-4622(94)00128-7：驱动力 1.1 eV 使正向 ET 入反转区（故观测不到产物）。
5. **FMN 结合蛋白**：Nunthaboot et al., PCCP 2011, 13, 6085-6097，DOI 10.1039/c0cp02634d：主要正常区、部分反转区（理论拟合宣称，强度较弱）。
6. **flavodoxin 飞秒 ET**：He et al., Biochemistry 2013, 52, 9120-9128，DOI 10.1021/bi401137u：反转区内背 ET 势垒降低。
- 经典反例解释：**Marcus 本人在 Nobel 讲稿指出光合反应中心 λ~0.25 eV + 反转区效应是其在 ~1.1 eV 高放能下抑制电荷复合的功能要素**（1992 年已写明）。
- 负例背景：Tang et al., Biochemistry 1999, 38, 8794，DOI 10.1021/bi990346q（Rb. sphaeroides P+HA- 复合速率与 P/P+ 电位无关；标题+DOI 核验）。
- 综述确认：Biomolecules 2026, 16, 495（PMC 全文）："Single-molecule studies of Fe-S protein complexes reveal the Marcus inverted region, where current saturates or declines at high bias."

**一句话结论**：Marcus 反转区在生物/蛋白体系中并非"从未观测到"——1992 年起即有权威表述（光合反应中心 λ~0.25 eV 抑制效应），2013-2015 年起在 PSII 与非衍生化蛋白（azurin 系列）中获得直接实验确认；正确说法是**天然生理 ET 链的工作点被进化约束在正常区/激活区（中心距 ≤14 Å、电位精调），反转区只是很少被生理工作点触及，并非原则上不可达**。

## 三、任务B：β 因子谱（verified 为主）

| 条目 | β 值 | 来源 | 状态 |
|---|---|---|---|
| 蛋白质内经典 ET 典型带 | **1.0-1.4 Å⁻¹** | Biomolecules 2026, 16, 495 原句 "β ≈ 1.0–1.4 Å⁻¹"（PMC 全文）；一级底座 Moser et al. Nature 1992, 355, 796-802（DOI 10.1038/355796a0；"20 Å → 10^12 倍"反推 ≈1.38）+ Page/Dutton Nature 1999, 402, 47-52（DOI 10.1038/46972；14 Å 上限） | verified |
| Ru-azurin β-strand | **1.1 Å⁻¹**（理想 β 链理论 1.0） | Langen et al., Science 1995, 268, 1733-1735，DOI 10.1126/science.7792598，摘要原句 | verified |
| Ru-azurin 参数组 | β=1.1 Å⁻¹，H_AB0=186 cm⁻¹，d0=3 Å | PMC6004490（2018）全文引 (8,28)：Gray & Winkler PNAS 2005, 102, 3534（DOI 10.1073/pnas.0408029102）；Warren et al. JACS 2013, 135, 11151（DOI 10.1021/ja403734n） | verified |
| 机理分档确认 | 共价/氢键耦合 ≫ van der Waals 间隙 | Gray & Winkler PNAS 2005 摘要（Europe PMC 核验） | verified |
| hopping 对照谱 | 0.1-0.3 Å⁻¹（红氧还蛋白）、0.1-0.6（非红氧还）、0.1-0.2（大蛋白） | Biomolecules 2026, 16, 495 原句 | verified |
| 饱和烷烃链 | ~1.0 Å⁻¹ | 同上综述 | verified |
| **共价路径 β≈0.7 Å⁻¹** | — | **未找到含显式数字的开放获取文本**。候选：Winkler & Gray Chem. Rev. 1992, 92, 369-379（DOI 10.1021/cr00011a001，DOI 已核验，正文未取得）；Gray & Winkler QRB 2003, 36, 341-372（DOI 10.1017/s0033583503003913，摘要无数字） | **unverified（仅入待核验参考）** |

## 四、任务C：Marcus 前提检验（gated ET，verified）

- 定义文献：**Hoffman & Ratner, "Gated electron transfer: when are observed rates controlled by conformational interconversion?", JACS 1987, 109, 6237-6243**（DOI 10.1021/ja00255a003；勘误 1988, 110, 8267 亦核验）。标题本身就是答案：观测速率何时由构象互变控制——即 Marcus 速率常数只在门控态就绪后有定义。
- 实验链：Walker & Tollin（flavocytochrome b2, Biochemistry 1991, 30, 5546, DOI 10.1021/bi00236a030）；McLendon, Pardue, Bak（cyt c/cyt b2, JACS 1987, 109, 7540, DOI 10.1021/ja00258a054）；Zhou & Kostic（Zn-cyt c→PC, JACS 1992, 114, 3562, DOI 10.1021/ja00035a065；1993, 115, 10796, DOI 10.1021/ja00076a042）；Davidson 组系统化区分 true/gated/coupled ET（Acc. Chem. Res. 2008, PMID 18442271；Biochemistry 2002, PMID 12475211，摘要均核验）。
- 结论：**学术界正式承认 Marcus 描述的是"门控已打开后"的 ET 速率；门控之前的构象形成-消失是独立动力学**。这正是间隙层理论需要的缝隙：间隙跳跃图像中"间隙驻留的形成-消失"对应门控动力学，"驻留存在后的跃迁"对应 Marcus 动力学——两者分层，不冲突，且同构于化学键的间隙驻留重构。

## 五、可疑值清单

1. **共价路径 β≈0.7 Å⁻¹：未核验**（开放获取通道未获显式数字；不进理论正文）。
2. **McCleskey/Weller 门控文献：未核验**——Crossref 作者检索未返回 McCleskey 主作者的 gated ET 条目；任务书该记忆未获来源支持。门控链已由 Hoffman/Ratner 等完整支撑，不影响结论。
3. **任务书两处书目误差已勘误**：1993 Nobel lecture 标题应为 "Theory and Experiment"（非 "theory and practice"）；反转区首次观测应为 Miller 系 1984 两篇（JACS 106, 3047 Miller/Calcaterra/Closs 与 JACS 106, 5057 Miller/Beitz/Huddleston），任务书原引的第三作者名 Huddleston 对应后者。
4. Tang 1999 摘要在通道内被截断，仅以标题结论+DOI 入档（verified 但弱）。
5. Wikipedia "30 years until unequivocally verified in 1984" 为二级来源表述，与 Nobel 讲稿一致，但其中 "Gloss" 系讲稿印刷变体（实为 Closs），已标注。

## 六、成功/失败清单

成功（27 verified）：A1 三条、A2 三条、A3 九条、B 六条、C 五条+Davidson 组两条辅助。全部带 source_url 与 accessed=2026-09-02。
失败/未达（2 unverified）：共价 β 0.7 显式数字；McCleskey 门控条目。失败原因：两篇 ACS/剑桥期刊正文均非开放获取，本次未走 Sci-Hub 类通道（纪律边界）。

## 七、对化学间隙层理论的直接启示（供下一步）

- 反转区争议的准确表述修正后，间隙层理论不需要"解释反转区为何不存在"，而需要"解释为什么生理工作点不落在反转区、且为什么落点处门控（间隙形成-消失）常常是限速步"。
- gated ET 文献链是天然的盟友：Marcus 速率的适用前提（间隙/构象已就绪）与"间隙驻留的依次形成-消失"在同一条传力路径上分层。
- β 谱的隧穿（1.0-1.4）/hopping（0.1-0.3）分档为"间隙是否成为实驻留态"提供了可计算的分界判据。
