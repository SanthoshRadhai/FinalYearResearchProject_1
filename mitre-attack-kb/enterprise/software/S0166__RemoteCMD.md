# S0166: RemoteCMD

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0166  
**Aliases:** RemoteCMD  
**Platforms:** Windows  

## Description
[RemoteCMD](https://attack.mitre.org/software/S0166) is a custom tool used by [APT3](https://attack.mitre.org/groups/G0022) to execute commands on a remote system similar to SysInternal's PSEXEC functionality. (Citation: Symantec Buckeye)

## Techniques Used
- T1053.005: Scheduled Task
- T1105: Ingress Tool Transfer
- T1569.002: Service Execution
