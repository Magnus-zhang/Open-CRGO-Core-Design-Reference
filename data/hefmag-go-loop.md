# HEFMAG grain-oriented FeSi hysteresis loop at 50 Hz

[Download the CSV](hefmag-go-loop-1p7t-50hz.csv). It contains 4,000 consecutive samples from the reference loop with approximately 1.7 T peak magnetic polarization. The upstream study measured a grain-oriented FeSi electrical-steel sample using a 700-turn Epstein frame at 50 Hz, following IEC 60404-2. The research sample has no commercial grade designation in the source. Figure 2 labels the sheet 0.3 mm in the plot legend and 0.2 mm in its caption, so the thickness is unresolved. Treat the loop as a research example for this sample and test condition.

| CSV column | Quantity | Unit and origin |
| --- | --- | --- |
| `field_strength_a_per_m` | Applied field strength, H | A/m, unchanged measurement |
| `magnetic_polarization_t` | Magnetic polarization, J | T, unchanged measurement |
| `derived_flux_density_t` | Magnetic flux density, B | T, calculated from J + μ₀H |

The first two columns preserve every source number and its order in the middle block of `GO.dat`, lines 4002–8001. For this CSV, the upstream tab delimiter was changed to a comma and a header and the derived B column were added. The calculation uses μ₀ = 1.25663706 × 10⁻⁶ H/m and rounds B to eight decimal places for export. The digits written to the CSV do not establish measurement accuracy. No points were interpolated or smoothed. [CODATA value for μ₀](https://physics.nist.gov/cuu/pdf/all.pdf)

## Source and license

Adapted from Massimo Pasquale (2022), *EMPIR 19ENG06 HEFMAG hysteresis loops NO and GO dataset example*, version 1, Zenodo. Source archive `EMPIR 19ENG06 HEFMAG dataset loops NO and GO.zip`, file `GO.dat`, method documented in `dataset example loops NO and GO.pdf`. The CSV is provided under the source [Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/). [Original dataset and supporting PDF](https://doi.org/10.5281/zenodo.5910893)
