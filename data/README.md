# Data

## Core design examples

[core_design_examples.csv](core_design_examples.csv) holds three illustrative arithmetic cases for laminated transformer cores. The density, stacking factor, strip loss and building factor are assumed per case. Magnetic level and frequency describe the assumed strip-loss input. For a real design, take the loss input from the applicable material report at the intended excitation and frequency.

Each case models a uniform net cross-section along an equivalent path. The estimated mass covers steel only. The loss model uses a lumped building factor, with no separate calculation of step-lap joint loss.

| Output | Calculation |
| --- | --- |
| Net steel area, mm² | Gross area × stacking factor |
| Estimated steel mass, kg | Net area × 10⁻⁶ × equivalent path in metres × steel density in kg/m³ |
| Strip loss baseline, W | Unrounded estimated steel mass × assumed strip loss in W/kg |
| Estimated core loss, W | Unrounded strip loss baseline × assumed building factor |

The CSV rounds the mass and losses to four decimal places, using round-half-up. Run `python3 scripts/verify_examples.py` from the repository root to recompute the outputs.

## Published mill loss values

[mill_loss_reference.csv](mill_loss_reference.csv) transcribes a few reported steel-strip properties for exact grade designations. Typical values describe published examples. Maximum values are sourced separately from the applicable specification table. The blank 60 Hz maximum for 23SQGD085 reflects the coverage of the cited Shougang specification table.

The reported magnetic level is the value in the source loss columns. Confirm the test basis before comparing mills or setting an acceptance limit. The cited Shougang tables do not identify the test fixture. Baosteel Q/BQB 485–2023 specifies the GB/T 13789 single-sheet test and requires conversion of specific total loss to the Epstein-frame basis for Table 5 acceptance of this 0.23 mm domain-refined grade. Verify any delivery against the applicable specification and the coil’s material test certificate. [Shougang specifications](https://www.shougang.com.cn/u/cms/www/202412/2024122703.pdf#page=8) · [Shougang typical values](https://www.shougang.com.cn/u/cms/www/202412/2024122703.pdf#page=9) · [Baosteel Table 5](https://ecommerce.ibaosteel.com/baosteel/manufacturerStandard/pdf2023/BQB%20485-2023.pdf#page=12) · [Baosteel typical values](https://ecommerce.ibaosteel.com/baosteel/manufacturerStandard/pdf2023/BQB%20485-2023.pdf#page=27) · [Baosteel test basis](https://ecommerce.ibaosteel.com/baosteel/manufacturerStandard/pdf2023/BQB%20485-2023.pdf#page=10)

The published points cover loss at a fixed magnetic level and two frequencies. The underlying mill documents retain their own terms. The example script recalculates the illustrative cases only.
