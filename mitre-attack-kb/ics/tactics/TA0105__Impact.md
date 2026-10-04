# TA0105: Impact

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0105  

## Description
The adversary is trying to manipulate, interrupt, or destroy your ICS systems, data, and their surrounding environment.

Impact consists of techniques that adversaries use to disrupt, compromise, destroy, and manipulate the integrity and availability of control system operations, processes, devices, and data. These techniques encompass the influence and effects resulting from adversarial efforts to attack the ICS environment or that tangentially impact it. Impact techniques can result in more instantaneous disruption to control processes and the operator, or may result in more long term damage or loss to the ICS environment and related operations. The adversary may leverage [Impair Process Control](https://attack.mitre.org/tactics/TA0106) techniques, which often manifest in more self-revealing impacts on operations, or [Impair Process Control](https://attack.mitre.org/tactics/TA0106) techniques to hinder safeguards and alarms in order to follow through with and provide cover for Impact. In some scenarios, control system processes can appear to function as expected, but may have been altered to benefit the adversary’s goal over the course of a longer duration. These techniques might be used by adversaries to follow through on their end goal or to provide cover for a confidentiality breach.

[Loss of Productivity and Revenue](https://attack.mitre.org/techniques/T0828), [Theft of Operational Information](https://attack.mitre.org/techniques/T0882), and [Damage to Property](https://attack.mitre.org/techniques/T0879) are meant to encompass some of the more granular goals of adversaries in targeted and untargeted attacks. These techniques in and of themselves are not necessarily detectable, but the associated adversary behavior can potentially be mitigated and/or detected.

## Techniques in This Tactic
- T0813: Denial of Control
- T0815: Denial of View
- T0826: Loss of Availability
- T0827: Loss of Control
- T0828: Loss of Productivity and Revenue
- T0829: Loss of View
- T0831: Manipulation of Control
- T0832: Manipulation of View
- T0837: Loss of Protection
- T0879: Damage to Property
- T0880: Loss of Safety
- T0882: Theft of Operational Information
