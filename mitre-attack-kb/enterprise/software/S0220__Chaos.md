# S0220: Chaos

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0220  
**Aliases:** Chaos  
**Platforms:** Linux  

## Description
[Chaos](https://attack.mitre.org/software/S0220) is Linux malware that compromises systems by brute force attacks against SSH services. Once installed, it provides a reverse shell to its controllers, triggered by unsolicited packets. (Citation: Chaos Stolen Backdoor)

## Techniques Used
- T1059.004: Unix Shell
- T1104: Multi-Stage Channels
- T1110: Brute Force
- T1205: Traffic Signaling
- T1573.001: Symmetric Cryptography
