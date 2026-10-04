# D3-RH: Radiation Hardening

**Reference:** https://d3fend.mitre.org/technique/D3-RH/  

## Definition
Radiation hardening is the process of making electronic components and circuits resistant to damage or malfunction caused by high levels of ionizing radiation.

## Parent Class(es)
- Platform Hardening

## Relationships
- **hardens:** Hardware Device
- **kb-reference:** Reference - A Radiation-Hardened SAR ADC with Delay-Based Dual Feedback Flip-Flops for Sensor Readout Systems
- **kb-reference:** Reference - Diagnosis of Faults Induced by Radiation and Circuit-Level Design Mitigation Techniques: Experience from VCO and High-Speed Driver CMOS ICs Case Studies
- **kb-reference:** Reference - Method of making thin atomic (Z) grade shields - NASA

## Knowledge Base Article
## How it works

There are three core radiation hardening methodologies:

1. Radiation Hardening by Process (RHBP): modifying the physical fabrication of a semiconductor (e.g., using SOI - Silicon on Insulator), offering the highest intrinsic protection. Usually the most expensive option as it requires a specialized semiconductor fabrication plant.
2. Radiation Hardening by Design (RHBD): modifying circuit topology and physical layout using techniques such as Triple Modular Redundancy (TMR). A more cost-effective option, with the constraint of potentially increasing chip area and power.
3. Radiation Hardening by Shielding (RHBS): using physical materials (e.g., aluminum or tantalum) to block ionizing particles. Simple to implement, with the constraint of increasing size and weight.
