# 化学间隙层论文 · 参考文献发布级核验报告 v1.0

- 对象：`papers/化学间隙层_耦合解耦的场所定位_v1.0_CN.md` 参考文献表（9 条）
- 核验日期：2026-09-02（系统 `date` 输出）
- 核验通道：Crossref API（api.crossref.org/works/{doi}，主通道）、PubMed eutils（esearch/esummary/efetch）、arXiv abs 页（arxiv.org/abs/{id}）、Nobel 官网 PDF（HTTP 200）、OpenAlex（辅助）
- 汇总：**9/9 verified**（每条至少一条独立可核验路径）；共发现 **5 处引文错误需修正**（2 处 DOI 未注册 + 3 处张冠李戴/错题），详见修正明细。

---

## 一、修正后的完整参考文献表（9 条，可直接替换正文第七节）

1. Toulhoat H, Raybaud P. Prediction of optimal catalysts for a given chemical reaction. Catal Sci Technol. 2020;10:2069-2081. doi:10.1039/C9CY02196E.（arXiv:1812.09531 预印本版；实验火山图峰位 95.0±3 kJ/mol 引文，其 ref.28=Ozaki 1981、ref.29=Jacobsen 2001）
2. Saidi WA, Shadid W, Veser G. Optimization of high entropy alloy catalyst for ammonia decomposition and ammonia synthesis. J Phys Chem Lett. 2021;12:5185-5192. doi:10.1021/acs.jpclett.1c01242.（arXiv:2104.07827 预印本版；Co/Mo/Ru N 吸附能与 Ru optimum 位点）
3. Hoffman BM, Ratner MA. Gated electron transfer: when are observed rates controlled by conformational interconversion? J Am Chem Soc. 1987;109(21):6237-6243. doi:10.1021/ja00255a003
4. Marcus RA. Electron transfer reactions in chemistry. Theory and experiment. Rev Mod Phys. 1993;65(3):599-610. doi:10.1103/RevModPhys.65.599.（Nobel Lecture, 1992-12-08；Nobel 官网 PDF：https://www.nobelprize.org/uploads/2018/06/marcus-lecture.pdf ；含光合反应中心 λ~0.25 eV 与反转区功能要素表述）
5. Boussac A, Rappaport F, Brettel K, Sugiura M. Charge recombination in S_nTyrZ•Q_A^-• radical pairs in D1 protein variants of Photosystem II: long range electron transfer in the Marcus inverted region. J Phys Chem B. 2013;117(12):3308-3314. doi:10.1021/jp400337j. PMID 23448315.（−ΔG°≈1.2 eV 反转区证据，摘要原文 "−ΔG(0) ≈ 1.2 eV ... Marcus inverted region"）
6. Farver O, Hosseinzadeh P, Marshall NM, Wherland S, Lu Y, Pecht I. Long-range electron transfer in engineered azurins exhibits Marcus inverted region behavior. J Phys Chem Lett. 2015;6(1):100-105. doi:10.1021/jz5022685. PMID 26263097.（azurin 系列 protein-only/非衍生化蛋白反转区首证）
7. Moser CC, Farid TA, Chobot SE, Dutton PL. Electron tunneling chains of mitochondria. Biochim Biophys Acta. 2006;1757(9-10):1096-1109. doi:10.1016/j.bbabio.2006.04.015
8. Moser CC, Keske JM, Warncke K, Farid RS, Dutton PL. Nature of biological electron transfer. Nature. 1992;355(6363):796-802. doi:10.1038/355796a0（QA→QB 14 Å、10⁴-10⁵ s⁻¹）
9. Giangiacomo KM, Dutton PL. In photosynthetic reaction centers, the free energy difference for electron transfer between quinones bound at the primary and secondary quinone-binding sites governs the observed secondary site specificity. Proc Natl Acad Sci USA. 1989;86(8):2658-2662. doi:10.1073/pnas.86.8.2658. PMID 2649889.（QA−→QB 驱动力由蛋白调控的实验证据）

---

## 二、逐条核验状态

| # | 状态 | 核验内容 | 核验 URL |
|---|---|---|---|
| 1 | **verified（修正自"Toulhoat H. et al. arXiv:1812.09531"）** | arXiv 存在（2018-12-22 提交，v2 2022-01-19），题名 "Prediction of optimal catalysts for a given chemical reaction"，作者仅 2 人：Toulhoat Hervé, Raybaud Pascal（非"et al."）；正式发表版 Catal Sci Technol 2020;10:2069-2081。摘要确认 EMX 描述符 + ammonia synthesis 应用。"volcano plot 峰位 95.0±3 kJ/mol（EM-N）"表述见 arXiv PDF 图 4b（此前考古已核：`数据考古报告_Sabatier_v0.1.md` §4/正结果 1） | https://arxiv.org/abs/1812.09531 ; https://api.crossref.org/works/10.1039/c9cy02196e |
| 2 | **verified（补正式发表版）** | arXiv 存在，题名 "Optimization of High Entropy Alloy Catalyst for Ammonia Decomposition and Ammonia Synthesis"，作者 Saidi Wissam A., Shadid Waseem, Veser Götz（与原引一致）；正式发表版 J Phys Chem Lett 2021;12:5185-5192 | https://arxiv.org/abs/2104.07827 ; https://api.crossref.org/works/10.1021/acs.jpclett.1c01242 |
| 3 | **verified（修正自 10.1021/ja00254a059 张冠李戴）** | Crossref：10.1021/ja00255a003 = Hoffman Brian M., Ratner Mark A., "Gated electron transfer: when are observed rates controlled by conformational interconversion?", JACS 1987;109(21):6237-6243。原 DOI 10.1021/ja00254a059 实为 Traylor & Xu "A biomimetic model for catalase..." JACS 1987;109(20):6201-6202 | https://api.crossref.org/works/10.1021/ja00255a003 |
| 4 | **verified** | Crossref：10.1103/RevModPhys.65.599 = Marcus Rudolph A., "Electron transfer reactions in chemistry. Theory and experiment", Rev Mod Phys 1993;65:599-610。Nobel PDF 可达（HTTP 200） | https://api.crossref.org/works/10.1103/RevModPhys.65.599 ; https://www.nobelprize.org/uploads/2018/06/marcus-lecture.pdf |
| 5 | **verified（修正自 BBA Trp295 条目张冠李戴）** | PubMed PMID 23448315 = Boussac A, Rappaport F, Brettel K, Sugiura M, J Phys Chem B 2013;117(12):3308-3314, DOI 10.1021/jp400337j，题名即 "…long range electron transfer in the Marcus inverted region"，efetch 摘要原句 "−ΔG(0) ≈ 1.2 eV at room temperature for S1"——**正是"PSII −ΔG°≈1.2 eV 反转区"的出处**。作者顺序/名单与原引（Boussac, Sugiura, Lai TL, Rappaport）不符，Lai TL 不在作者列 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=23448315 ; https://api.crossref.org/works/10.1021/jp400337j |
| 6 | **verified（修正自 Faraday Discuss 2015;185:97-108 / C5FD00093B 三重错误）** | ① DOI 10.1039/C5FD00093B 未注册（Crossref 404）；② Faraday Discuss 185 卷（2015，人工光合作用专题）Crossref 全目录中 97-108 页无此文（C5FD00093A 是 Lemon & Nocera 量子点论文 249-266 页）；③ Farver/Pecht 在 Faraday Discussions 无论文。正确出处：J Phys Chem Lett 2015;6(1):100-105, doi:10.1021/jz5022685, PMID 26263097，作者 6 人（Farver O, Hosseinzadeh P, Marshall NM, Wherland S, Lu Y, Pecht I），题名 "Long-Range Electron Transfer in Engineered Azurins Exhibits Marcus Inverted Region Behavior"（与此前考古 `数据考古报告_Marcus_bio_v0.1.md` 记录一致，双源闭环） | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=26263097 ; https://api.crossref.org/works/10.1021/jz5022685 ; https://api.crossref.org/works/10.1039/C5FD00093A |
| 7 | **verified** | Crossref：10.1016/j.bbabio.2006.04.015 = Moser CC, Farid TA, Chobot SE, Dutton PL, "Electron tunneling chains of mitochondria", BBA-Bioenergetics 2006;1757(9-10):1096-1109。原引完全正确 | https://api.crossref.org/works/10.1016/j.bbabio.2006.04.015 |
| 8 | **verified（修正自 10.1038/358796a0 未注册）** | 10.1038/358796a0 Crossref 404（"Resource not found"）；正确 DOI 10.1038/355796a0 = Moser CC, Keske JM, Warncke K, Farid RS, Dutton PL, "Nature of biological electron transfer", Nature 1992;355(6363):796-802。错因：卷号 355 误写为 358 | https://api.crossref.org/works/10.1038/355796a0 |
| 9 | **verified（修正自 10.1021/bi00456a003 张冠李戴 + 错题）** | ① 原 DOI 10.1021/bi00456a003 实为 Shayiq & Avadhani 1990 Biochemistry 29(4):866-873（肝 P-450，完全无关）；② 原标题 "In natural and engineered reaction centers the energies of electron transfer from QA- to QB are regulated by the protein" 在 Crossref/PubMed 标题检索均无此文献；③ 正确著录：10.1073/pnas.86.8.2658 = Giangiacomo K M, Dutton P L, PNAS 1989;86(8):2658-2662, PMID 2649889，真实标题见上表（双源：Crossref + PubMed esummary 一致） | https://api.crossref.org/works/10.1073/pnas.86.8.2658 ; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=2649889 |

---

## 三、修正明细（原引文 → 修正后 → 修正依据）

1. **文献1**：`Toulhoat H. et al. … arXiv:1812.09531` → `Toulhoat H, Raybaud P. Catal Sci Technol 2020;10:2069-2081. doi:10.1039/C9CY02196E`（保留 arXiv 号注明）。依据：arXiv abs 页作者仅 2 人（非 et al.）；Crossref 给出正式发表版 DOI。
2. **文献2**：`arXiv:2104.07827`（无 DOI）→ 补正式发表版 `J Phys Chem Lett 2021;12:5185-5192. doi:10.1021/acs.jpclett.1c01242`。依据：Crossref bibliographic 检索命中，作者/题名一致。
3. **文献3**：DOI `10.1021/ja00254a059` → `10.1021/ja00255a003`；标题 "…when are electron transfer rates governed by conformational motion?" → "…when are observed rates controlled by conformational interconversion?"；页码 6237-6239 → 6237-6243。依据：原 DOI 实为 Traylor & Xu 过氧化氢酶模型论文（Crossref 直查）；Crossref bibliographic 检索 "Gated electron transfer" 命中正确 DOI。
4. **文献4**：页码 599 → 599-610（补全）；标题定稿为 Crossref 口径 "Electron transfer reactions in chemistry. Theory and experiment"。DOI 10.1103/RevModPhys.65.599 原引正确，Crossref 直查通过。
5. **文献5**：`Boussac A, Sugiura M, Lai TL, Rappaport F. Functional role of C-terminus Trp (Trp295) of D1 in the oxidation of QA- in PSII. Biochim Biophys Acta 2013`（期刊卷页悬空）→ `Boussac A, Rappaport F, Brettel K, Sugiura M. Charge recombination in S_nTyrZ•Q_A^-• radical pairs… J Phys Chem B 2013;117(12):3308-3314. doi:10.1021/jp400337j. PMID 23448315`。依据：PMID 23448315 题名/摘要直接含 "Marcus inverted region" 与 "−ΔG(0) ≈ 1.2 eV"，即"−ΔG°≈1.2 eV 反转区"的准确出处；原 BBA Trp295 条目经 PubMed 多路检索（Trp295/W295/C-terminus）无法定位，判定为预检索张冠李戴。此修正同时与此前考古记录（`数据考古报告_Marcus_bio_v0.1.md` A3-2）双源闭环。
6. **文献6**：`Farver O, Pecht I. … Faraday Discuss 2015;185:97-108. doi:10.1039/C5FD00093B` → `Farver O, Hosseinzadeh P, Marshall NM, Wherland S, Lu Y, Pecht I. Long-range electron transfer in engineered azurins exhibits Marcus inverted region behavior. J Phys Chem Lett 2015;6(1):100-105. doi:10.1021/jz5022685`。依据：原 DOI 未注册（404）；FD 185 全目录无此文；PubMed+Crossref 双源确认 JPCL 条目（题名/作者/卷页/DOI 一致）。
7. **文献7**：无修正（原引逐字段与 Crossref 一致）。
8. **文献8**：DOI `10.1038/358796a0` → `10.1038/355796a0`（卷号 355 误写 358，未注册 DOI）。依据：原 DOI Crossref 404；正确 DOI 直查命中，作者/卷页与原引一致。
9. **文献9**：DOI `10.1021/bi00456a003` → `10.1073/pnas.86.8.2658`；标题修正为真实标题（"In photosynthetic reaction centers, the free energy difference for electron transfer between quinones bound at the primary and secondary quinone-binding sites governs the observed secondary site specificity."）。依据：原 DOI 实为 Shayiq & Avadhani 1990（肝 P-450）论文；原引标题在 Crossref/PubMed 检索无命中；正确 DOI 由 Crossref 直查+PubMed PMID 2649889 双源确认。原引"准确 DOI 见复现包"悬置标注一并消除。

---

## 四、需要在正文中同步修改的点

1. **第七节参考文献表整表替换**（用本报告第一节 9 条）。
2. **正文 5.2 节（114 行附近）**：文献 [6] 引用语境 "非衍生化蛋白 azurin [6] 已获直接证据"——与 JPCL 2015 摘要 "We herein provide such evidence in a series of nonderivatized proteins" 语义吻合，正文无需改写；但注意该文属 engineered azurin 系列，若追求精确可写 "工程化（非衍生化）azurin [6]"。
3. **正文 5.5 节（139 行附近）文献 [9]**："多数候选醌的 QA/QB 驱动力小到无法检测 [9]"——正确文献（PNAS 1989）的核心结论是 "QA/QB 间自由能差由蛋白调控、决定次级位点特异性"；"驱动力小到无法检测"是对该文的转述，建议发布前对照原文正文改写为与结论直连的表述（如 "QA−→QB 驱动力被蛋白调控、多数替换醌的驱动力差异决定位点特异性 [9]"），或标注为转述。
4. **文末"引文核验声明"改写**（165-175 行）：
   - 原句 "纠正了 4 处预检索引文错误（2 处 DOI 未注册、2 处张冠李戴）" → 改为 "纠正了 5 处预检索引文错误（2 处 DOI 未注册：文献 6/8；3 处张冠李戴：文献 3/5/9）"。
   - 原句 "个别未直接核验处（文献 5 准确卷期、文献 9 DOI 对应）已如实标注" → 删除，改为 "9 条全部经 Crossref/PubMed/arXiv 逐条直接核验（本次核验记录：`papers/chemical_gap_layer/refs_v1.0_核验.md`）"。
5. **文献 5 复现包悬置标注**（原第 170 行 "准确出处为 Boussac et al., J Phys Chem B / BBA 系（见复现包 data_et_chain.json…）"）→ 删除悬置，直接用定稿著录；`data_et_chain.json` 中 Boussac 条目如与定稿著录不符需同步更新。
6. **文献 9 复现包悬置标注**（原第 172 行 "准确 DOI 见复现包…"）→ 删除悬置，DOI 已定稿。

---

## 五、核验方法备注

- 主通道 Crossref API 直查 DOI 元数据（标题/作者/卷期页/年份），PubMed eutils esummary/efetch 交叉确认（文献 5/6/9），arXiv abs 页确认预印本存在性与作者（文献 1/2），Nobel PDF HEAD 200 确认可达（文献 4）。
- 网络备注：本机直连 export.arxiv.org 失败，经代理 127.0.0.1:7890 走 https://arxiv.org/abs/ 完成。
- 原始响应缓存于 /tmp：cr3_full.json、cr5b.json、cr6_full.json、cr7.json、cr8_full.json、cr9_full.json、pm5.json、pm6_sum.json、q9pm_sum.json、arx1_abs.html、arx2_abs.html 等。
