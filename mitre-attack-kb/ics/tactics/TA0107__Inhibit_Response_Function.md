# TA0107: Inhibit Response Function

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0107  

## Description
The adversary is trying to prevent your safety, protection, quality assurance, and operator intervention functions from responding to a failure, hazard, or unsafe state.

Inhibit Response Function consists of techniques that adversaries use to hinder the safeguards put in place for processes and products. This may involve the inhibition of safety, protection, quality assurance, or operator intervention functions to disrupt safeguards that aim to prevent the loss of life, destruction of equipment, and disruption of production. These techniques aim to actively deter and prevent expected alarms and responses that arise due to statuses in the ICS environment. Adversaries may modify or update system logic, or even outright prevent responses with a denial-of-service. They may result in the prevention, destruction, manipulation, or modification of programs, logic, devices, and communications. As prevention functions are generally dormant, reporting and processing functions can appear fine, but may have been altered to prevent failure responses in dangerous scenarios. Unlike [Evasion](https://attack.mitre.org/tactics/TA0103), Inhibit Response Function techniques may be more intrusive, such as actively preventing responses to a known dangerous scenario. Adversaries may use these techniques to follow through with or provide cover for [Impact](https://attack.mitre.org/tactics/TA0105) techniques.

## Techniques in This Tactic
- T0800: Activate Firmware Update Mode
- T0809: Data Destruction
- T0814: Denial of Service
- T0816: Device Restart/Shutdown
- T0835: Manipulate I/O Image
- T0838: Modify Alarm Settings
- T0851: Rootkit
- T0878: Alarm Suppression
- T0881: Service Stop
- T0892: Change Credential
- T1691: Block Operational Technology Message
- T1691.001: Command Message
- T1691.002: Reporting Message
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware
- T1695: Block Communications
- T1695.001: Serial COM
- T1695.002: Ethernet
- T1695.003: Wi-Fi
