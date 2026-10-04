# S0169: RawPOS

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0169  
**Aliases:** RawPOS, FIENDCRY, DUEBREW, DRIFTWOOD  
**Platforms:** Windows  

## Description
[RawPOS](https://attack.mitre.org/software/S0169) is a point-of-sale (POS) malware family that searches for cardholder data on victims. It has been in use since at least 2008. (Citation: Kroll RawPOS Jan 2017) (Citation: TrendMicro RawPOS April 2015) (Citation: Visa RawPOS March 2015) FireEye divides RawPOS into three components: FIENDCRY, DUEBREW, and DRIFTWOOD. (Citation: Mandiant FIN5 GrrCON Oct 2016) (Citation: DarkReading FireEye FIN5 Oct 2015)

## Techniques Used
- T1005: Data from Local System
- T1036.004: Masquerade Task or Service
- T1074.001: Local Data Staging
- T1543.003: Windows Service
- T1560.003: Archive via Custom Method
