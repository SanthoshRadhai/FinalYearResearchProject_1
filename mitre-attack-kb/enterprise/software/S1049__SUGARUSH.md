# S1049: SUGARUSH

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1049  
**Aliases:** SUGARUSH  
**Platforms:** Windows  

## Description
[SUGARUSH](https://attack.mitre.org/software/S1049) is a small custom backdoor that can establish a reverse shell over TCP to a hard coded C2 address. [SUGARUSH](https://attack.mitre.org/software/S1049) was first identified during analysis of UNC3890's [C0010](https://attack.mitre.org/campaigns/C0010) campaign targeting Israeli companies, which began in late 2020.(Citation: Mandiant UNC3890 Aug 2022)

## Techniques Used
- T1016.001: Internet Connection Discovery
- T1059.003: Windows Command Shell
- T1095: Non-Application Layer Protocol
- T1543.003: Windows Service
- T1571: Non-Standard Port
- T1680: Local Storage Discovery
