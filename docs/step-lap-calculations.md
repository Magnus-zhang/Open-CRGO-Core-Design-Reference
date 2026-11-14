# Step-lap core calculations

Use these equations for a first estimate of net grain-oriented electrical steel (GOES) area, steel mass and assembled-core loss. The worked example uses assumed inputs.

## Net steel area and mass

For a uniform rectangular stack, let `w` be the lamination width and `h` be the compressed stack height. For a stepped cross-section, use the sum of the gross packet areas. Deduct any cooling ducts or other macroscopic voids included in the gross dimensions before applying the stacking factor.

```text
A_gross = w × h or Σ(packet width × packet height)   [mm²]
A_net   = A_gross × k_s                              [mm²]
V_steel = A_net × 10⁻⁶ × L                           [m³]
m_steel = ρ × V_steel                                [kg]
```

`k_s` is the stacking factor as a fraction, `L` is the equivalent length of steel at the stated area in metres, and `ρ` is steel density in kg/m³. The single-length formula assumes a uniform section or an equivalent volume. For a multi-limb core or different section areas, sum the steel volumes of each non-overlapping section, or calculate steel volume from the lamination cut list. Count the steel in each joint once. The resulting mass covers the steel laminations. Add clamps, hardware and packaging separately for shipping mass. Use the agreed stacking factor and density for the material and measurement conditions. [IEC 60404-13, stacking factor and density measurement](https://webstore.iec.ch/en/publication/32477)

## Assembled-core loss

```text
P_material = m_steel × p_strip  [W]
P_core_est = K_b × P_material   [W]
K_b        = P_core_measured ÷ P_material
```

`p_strip` is the strip's specific total loss in W/kg at the stated peak induction or polarization, frequency and test method. Record the exact basis, including any conversion the applicable material specification requires. Where sections use different grades or operating conditions, use a mass-weighted sum of the section losses for the material-loss baseline. A building factor `K_b` transfers only where the core geometry, manufacturing process, excitation and loss basis are comparable. The assembled-core estimate covers the core. A complete transformer's measured no-load loss can include additional losses, such as winding losses from excitation current. [IEC 60404-2, Epstein frame](https://webstore.iec.ch/en/publication/2064) · [IEC 60404-3, single-sheet tester](https://webstore.iec.ch/en/publication/66641)

## Joint geometry and assembly

Step-lap joints stagger the lamination end positions through the stack. Record the number of steps, lap length and step offset as separate drawing inputs, along with laminations per packet, joint gap and cut angles. Keep rolling direction and packet sequence traceable. Burrs, damaged insulation, residual cutting stress, clamping and uneven gaps can change local flux and loss. For acceptance, use the approved drawing, material certificate and agreed core or transformer test. [JFE Steel joint-geometry experiment, US11495378B2](https://patents.google.com/patent/US11495378B2/en)

## Worked check

Assume `A_gross = 10,000 mm²`, `k_s = 0.96`, `L = 2.00 m`, and `ρ = 7,650 kg/m³`. Use an illustrative strip-loss input of `0.80 W/kg` at `1.70 T / 50 Hz` and a building factor of `1.10`.

| Quantity | Calculation | Result |
| --- | --- | --- |
| Net steel area | 10,000 × 0.96 | 9,600 mm² |
| Steel volume | 9,600 × 10⁻⁶ × 2.00 | 0.0192 m³ |
| Net steel mass | 0.0192 × 7,650 | 146.88 kg |
| Material-loss baseline | 146.88 × 0.80 | 117.504 W |
| Assembled-core loss estimate | 117.504 × 1.10 | 129.2544 W |

See the [calculation examples CSV](../data/core_design_examples.csv) for the inputs and results in machine-readable form.
