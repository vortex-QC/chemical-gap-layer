# 数据考古报告 · Sabatier 火山图（合成氨）v0.1

- 日期：2026-09-02（系统时间核验）
- 考古代理：数据考古代理（涡）
- 数据落盘：`papers/chemical_gap_layer/data_sabatier_volcano.json`
- 纪律：每个数值来自本次实际访问的来源原文；拿不到即标 **未核验**；记忆值不入正文，只进"待核验参考"。

---

## 一、成功/失败清单

### 成功（拿到可核验定量或定性数据）
| 项 | 状态 | 来源通道 |
|---|---|---|
| 3 个任务 DOI 全部证伪并找到正确 DOI | 成功 | doi.org 404 + Crossref + OpenAlex |
| 碳载金属系列 9 催化剂实验活性火山图（Ru/MoFe/Re/Co/Pt/Ir/Os/Rh/Ni）+ 峰位 95.0 kJ/mol | 成功（图级数据） | arXiv:1812.09531 PDF 全文 |
| Co、Mo fcc(111) N 吸附能 −0.56 / −2.51 eV/N | 成功 | arXiv:2104.07827 PDF 全文 |
| Ru(0001) 短桥位最优 N 吸附能 −1.27 eV/N | 成功 | arXiv:2104.07827 |
| Fe C7 位两 *N 合计 −2.4 eV、Ru B5 位两 *N −0.8 eV | 成功 | Nat. Commun. 2018 OA PDF + PMC 交叉核对 |
| Fe3/Al2O3 TOF = 1.4×10⁻² s⁻¹ site⁻¹（100 bar, 700 K） | 成功 | Nat. Commun. 2018 |
| Fe(111) 单晶 TOF = 9.7 s⁻¹（15 atm H2 + 5 atm N2） | 成功 | PMC11054198 转述 |
| 定性火山序 Mo>Fe>Co>Ni；强侧 Re/Mo/Fe、弱侧 Co/Ni；峰附近 Fe/Ru；CoMo 插值最优 | 成功 | OSTI 1770110 + PMC12112505 + Springer 氮化物综述 |
| Sabatier & Senderens 1902 原始引文（C.R. 134, 514-516 与 134, 689-691） | 成功（两条独立引文交叉） | RSC/Wiley/IOP 多源 |
| Sabatier 1911 Berichte 44, 1984（原理早期表述） | 引文核验成功，原文未核验 | arXiv:1812.09531 ref.4 |
| Evans–Polanyi ΔG‡ = β1 + β2·ΔG_R 与 β1/β2 含义 | 成功 | OGST 2016 综述全文 |
| Brønsted 方程 k = α1·(Ka)^α2 与 Brønsted 1928 Chem. Rev. DOI | 成功 | OGST + Crossref |

### 失败（明确标未核验）
| 项 | 失败原因 |
|---|---|
| Logadottir 2001 全文（逐金属 ΔE_N+TOF 精确配对） | ScienceDirect Cloudflare 挡板 |
| Vojvodic 2014 摘要与预测数值 | Elsevier 403、Unpaywall 无 OA 副本 |
| Bligaard 2004 / Cheng & Hu 2008 全文 | 无 OA；ACS Cloudflare 挡板 |
| Wikipedia 火山图条目 | 直连+代理均 SSL EOF/超时；DBpedia 空 |
| Jacobsen 2001 图中逐点 (ΔE_N, 相对活性) 数值 | 付费墙；只拿到定性插值逻辑 |

---

## 二、来源逐条（带 URL 与访问日期，均 2026-09-02）

1. **doi.org 解析**：`10.1016/j.jcat.2003.12.029` → 404；`10.1021/ja0709630` → 404；`10.1016/j.cplett.2014.07.057` → 解析到 Dhahri et al. BaZrO3 光致发光论文（Crossref 确认）。**任务三个入口 DOI 全错**。
2. **Crossref API**：`api.crossref.org/works`（bibliographic 检索）→ Bligaard 2004 真实 DOI `10.1016/j.jcat.2004.02.034`（J. Catal. 224, 206-217）；Vojvodic 2014 真实 DOI `10.1016/j.cplett.2014.03.003`（CPL 598, 108-112）；Jacobsen 论文真实 DOI `10.1021/ja010963d`（JACS 2001, 123, 8404-8405，**合成氨**而非 CO methanation，**2001** 而非 2007）。
3. **OpenAlex**：`api.openalex.org/works/doi:10.1021/ja010963d` → ACS 页面文本头，确认卷期页、被引 620；`doi:10.1006/jcat.2000.3087` → Logadottir 2001 J. Catal. 197, 229-231，被引 723。
4. **arXiv:1812.09531**（`arxiv.org/pdf/1812.09531`）→ Figure 4b 碳载金属合成氨实验火山图：金属 Ru/MoFe/Re/Co/Pt/Ir/Os/Rh/Ni，TOF 轴 1E-3 至 1E+2 mol NH3/mol M/s，峰位 **95.0 kJ/mol（EM-N 描述符）**；ref.28=Ozaki 1981、ref.29=Jacobsen 2001；ref.4=Sabatier, Ber. Dtsch. Chem. Ges. 1911, 44, 1984。
5. **arXiv:2104.07827**（Saidi et al.）→ "nitrogen adsorption energies on Co and Mo fcc (111) are -0.56 and -2.51 eV/N"；Ru(0001) 短桥位 −1.27 eV/N "agrees with previous results"。
6. **Liu et al. Nat. Commun. 2018, 9, 1610**（`nature.com/articles/s41467-018-03795-8.pdf` + PMC5913218 双源一致）→ Fe C7 两 *N −2.4 eV；Ru B5 两 *N −0.8 eV、*N2 解离 TS 0.4 eV；Fe C7 解离 TS −0.10 eV；Fe3 TOF 1.4×10⁻² s⁻¹ site⁻¹（100 bar, 700 K）"comparable to that on the Ru B5 site"；ref.14/15/16 确认 Medford 2015、Bligaard 2004、Dahl 2001 引文。
7. **OSTI 1770110**（`osti.gov/servlets/purl/1770110`）→ "From the volcano curve, the relative affinity ... Mo > Fe > Co > Ni"；三元氮化物活性为 γ-Mo2N 的 2.6-4 倍、Cs 促进后提 30 倍；ref.29=Medford 2015（Sabatier 原理出处链）、ref.35=Skúlason 2012、ref.38=Dahl 2001、ref.39=Jacobsen 2001。
8. **PMC12112505**（Catalysts 综述）→ 火山图/BEP 教科书表述；"Near the volcano peak, metals like Fe, and Ru ... with CoMo emerging as the most effective catalyst"；Ru/MgO N2 吸附 −1.95 eV 等。
9. **Hargreaves 氮化物综述**（`link.springer.com/content/pdf/10.1007/s13203-014-0049-y.pdf`）→ Fig.1 即 Jacobsen 2001 计算火山图（400°C, 50 bar, H2/N2=3/1 含 5% NH3 条件下 TOF 对 N 吸附能）："Calculated turnover frequencies for ammonia synthesis as a function of the adsorption energy of nitrogen ... Copyright (2001) American Chemical Society"——**注意：这确认 Jacobsen 2001 图的坐标就是 (N 吸附能, 计算 TOF)**。
10. **Sabatier 1902**：C.R. Hebd. Seances Acad. Sci. **134, 514-516**（RSC d0cy01254h 与 IOP 10.1088/1749-4699/2/1/015006 双源一致）；**134, 689-691**（Wiley cite.202200201 与 RSC 26/1/122 双源一致）。
11. **BEP/LFER**：OGST 2016 综述（`ogst.ifpenergiesnouvelles.fr/.../ogst150117.html`）→ Evans & Polanyi (1935,1936,1938) ΔG‡ = β1 + β2·ΔG_R，β1/β2 含义原文；Brønsted (1924, 1928) k = α1·(Ka)^α2；Brønsted 1928 "Acid and Basic Catalysis." Chem. Rev.（DOI 10.1021/cr60019a001，Crossref 核验题名/期刊/年份）。

## 三、数据规模

- 定量配对：1 条图级火山序列（9 催化剂，逐点未核验）+ 5 条 DFT N 吸附能（Co/Mo/Ru(0001)/Fe C7/Ru B5）+ 3 条 TOF（Fe3、Fe(111)、碳载系列范围）。
- 定性火山序：4 条独立来源交叉。
- DOI 审计：3 条（全错，已纠错）。
- 原始文献考古：Sabatier 1902 两篇 + 1911 一篇 + Evans–Polanyi 1935-38 + Brønsted 1924/1928。
- 失败通道记录：10 条。

## 四、火山峰位置读数

1. **实验火山（碳载金属，EM-N 描述符）**：峰位 **95.0 ± 3 kJ/mol**（论文给出的不确定度约 3%），金属-氮键能坐标；峰附近金属 Ru、MoFe（图4b）。
2. **DFT 火山（N 吸附能描述符）**：峰位未直接核验到 Nørskov 组原始数值；旁证有——
   - Ru B5 位（"closest to the top of volcano curve"）：两 *N −0.8 eV 即 **≈ −0.4 eV/N**（Liu 2018）；
   - Ru(0001) 短桥位 **−1.27 eV/N** 被称为 "optimum nitrogen adsorption energy"（Saidi 2021，氨分解语境）；
   - Jacobsen 2001 的 CoMo 插值逻辑：Co（太弱）与 Mo（太强）之间，即介于 −0.56 与 −2.51 eV/N 之间。
   - 三个旁证跨度大（−0.4 ~ −1.27 eV/N），因位点/语境/参照不同，**不能取平均当峰位**；此为已知可疑点。
3. 降级说明：Logadottir 2001 的逐金属 (ΔE_N, TOF) 精确配对未拿到，最小定量集以"实验活性火山序列 + DFT 吸附能散点 + 定性火山序"降级满足。

## 五、可疑值清单

1. arXiv:1812.09531 图4b 的 "MoFe" 标签是单一双金属样品标签，非混合金属；逐点数值须回原文 ESI 核对（未核验）。
2. Ru B5 −0.4 eV/N 与 Ru(0001) −1.27 eV/N 差 0.87 eV，语境不同（微动力学拟合 vs 纯 DFT；台阶位 vs 台面），禁止混用。
3. 两套火山坐标不可互推：EM-N 键能（kJ/mol，键解离能口径）≠ ΔE_N 吸附能（eV，相对 N2 气相口径）；95 kJ/mol 峰位不能换算成 −0.99 eV。
4. Co3Mo3N 上 N2 吸附 +0.415 eV（吸热）属 MvK 机制语境，与金属面解离吸附不同。
5. 任务给的三个 DOI 全部错误（两个 404 未注册、一个张冠李戴）——提醒：后续引用这三个文献时一律使用本报告纠正后的 DOI。
6. Wikipedia 通道全灭，任务建议的 Wikipedia 数据源未能核验；其"速率对数 vs 吸附能"标准图数据未核验。

## 六、观测/推理分栏（去幻 v2.1）

- **观测**：本报告全部引号句为 PDF/页面原文摘录，URL+日期可回放。
- **推理**：Jacobsen 2001 图坐标为 (N 吸附能, 计算 TOF) 是从 Hargreaves 综述图注读出（观测），据此推其数据可作最小定量集的替代源（推理，需拿到原文确认）。
- **缸壁假设**：Sabatier 原理"峰在 −0.4~−1.27 eV/N 之间"的跨度是语境差异所致（假设，待 Logadottir 2001 原文检验）。

## 七、待核验参考（记忆值，不入正文数据）

- Nørskov 组 2001 年前后教科书火山图常引各金属 ΔE_N 序列：Mo ≈ −1.1 ~ −1.4、Fe ≈ −0.6 ~ −1.0（C7 更强）、Ru ≈ −0.4 ~ −0.6、Co ≈ −0.3 ~ −0.5、Ni ≈ −0.1 ~ −0.3 eV/N（凭训练记忆，**未核验**，仅供下次考古对照）。
- Logadottir 2001 结论（记忆）：TOF 对 ΔE_N 呈火山，Fe 附近最优，Ru/Co 次之（**未核验**）。
