# The Chemical Gap Layer — Reproduction Package

**The Chemical Gap Layer: Locating the Arena of Matter Coupling and Decoupling**

- CN: [doi:10.5281/zenodo.22249369](https://doi.org/10.5281/zenodo.22249369)
- EN: [doi:10.5281/zenodo.22249374](https://doi.org/10.5281/zenodo.22249374)
- Preprint series: native-unknown / array line (see [vortex-QC/native-unknown-array](https://github.com/vortex-QC/native-unknown-array), Zenodo 22220040/22220164 v1.0, 22233498/22233508 v1.1)

## Contents

| Group | Files |
|---|---|
| Paper | chemical_gap_layer_v1.0_CN.md / _EN.md |
| Data (10) | data_ionization.json (NIST, 38 elements/270 levels) · data_bond_energy.json (21 bonds) · data_noble_gas.json · data_pubchem_ie1.json · data_electronegativity.json (95 elements) · data_sabatier_volcano.json (+volcano_points_v2) · data_marcus_bio_et.json (29 items) · data_et_chain.json (25 stations) · data_3d4s_config.json (10 elements × 8 levels) · ET链甜蜜点判读_v0.1_out.json |
| Scripts (4) | 分析框架_电离能驻留谱_v0.1.py · 分析框架_惰性饱和映射_v0.1.py · 分析框架_键能吸附根_v0.1.py · 分析框架_ET链甜蜜点_v0.1.py |
| Verification reports (5) | 数据考古报告_v0.1.md · 数据考古报告_Sabatier_v0.1.md · 数据考古报告_Marcus_bio_v0.1.md · 数据考古报告_ET链_v0.1.md · refs_v1.0_核验.md (9/9 verified, 5 corrections) |
| Raw archives (8) | nist_ie_z1_36.tsv (+Ti/V/Xe_Rn/Sc_Zn_v2) · pubchem_periodictable_raw.json · webbook_Cl2_diatomic.html |

## Provenance & discipline

- All data first-hand retrieved 2026-09-02 (NIST ASD ie.pl, PubChem periodic-table API, Crossref/PubMed/OpenAlex, Nobel lecture PDF). Zero values from training memory; every value carries a source URL and accessed date.
- Citation verification: 9/9 references verified; 5 pre-search citation errors corrected (3 misattributions, 2 unregistered DOIs) — trail in refs_v1.0_核验.md.
- Discriminant scripts re-run end-to-end: ionization jumps 8/8 shell boundaries (main group), inertness two-variable caliper, bond-energy tests A/B/C, ET-chain sweet-spot tiers (14/25 stations judgeable, 93% normal region).

## License

CC-BY 4.0 for text; scripts/data as deposited.
