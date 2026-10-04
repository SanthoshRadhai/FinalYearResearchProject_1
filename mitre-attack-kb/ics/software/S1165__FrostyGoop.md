# S1165: FrostyGoop

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1165  
**Aliases:** FrostyGoop, BUSTLEBERM  
**Platforms:** Control Server, Field Controller/RTU/PLC/IED  

## Description
[FrostyGoop](https://attack.mitre.org/software/S1165) is a Windows-based binary written in Golang that allows for interaction with industrial control system (ICS) equipment via Modbus TCP over port 502. [FrostyGoop](https://attack.mitre.org/software/S1165) allows for reading and writing data to holding registers on targeted devices, manipulating the operation of systems for malicious purposes. [FrostyGoop](https://attack.mitre.org/software/S1165) is associated with the [FrostyGoop Incident](https://attack.mitre.org/campaigns/C0041) in Ukraine.(Citation: Dragos FROSTYGOOP 2024)(Citation: Nozomi BUSTLEBERM 2024)

## Techniques Used
- T0801: Monitor Process State
- T0807: Command-Line Interface
- T0836: Modify Parameter
- T0869: Standard Application Layer Protocol
- T0885: Commonly Used Port
