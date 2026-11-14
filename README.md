# Open CRGO Core Design Reference

An engineering reference for cold-rolled grain-oriented electrical steel (CRGO / GOES) and step-lap transformer cores, maintained by Chenfan Electric. Use it to check net steel area and mass, make a first estimate of core loss, and trace published strip-loss values back to the mill.

| File | What it contains |
| --- | --- |
| [Step-lap calculations](docs/step-lap-calculations.md) | Equations, units, joint inputs and a worked example |
| [Core design examples](data/core_design_examples.csv) | Three illustrative cases with inputs and computed results |
| [Mill loss reference](data/mill_loss_reference.csv) | Published Shougang 23SQGD085 and Baosteel B23R080 strip-loss values, with typical values and specification limits shown separately |
| [HEFMAG hysteresis loop](data/hefmag-go-loop-1p7t-50hz.csv) | 4,000 measured H and J samples at 50 Hz, with B calculated from J and H |
| [HEFMAG measurement and license](data/hefmag-go-loop.md) | Source, test conditions and CC BY 4.0 attribution |
| [Data notes](data/README.md) | Column definitions, test basis and original sources |

Recalculate the three examples with Python 3. No dependencies are required.

```sh
python3 scripts/verify_examples.py
```

A strip-loss value in W/kg is measured under stated magnetic and test conditions. A B–H curve describes a different property. Use the approved drawing, the coil certificate and the agreed test for production acceptance.

[Open the transformer core weight and loss calculator](https://chenfanelectric.com/tools/transformer-core-calculator/)

The [MIT license](LICENSE) covers the original documentation, illustrative examples and verification script. The adapted [HEFMAG CSV](data/hefmag-go-loop-1p7t-50hz.csv) is available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Cited publications and mill source documents retain their respective terms.
