# S9012: TRAILBLAZE

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9012  
**Aliases:** TRAILBLAZE  
**Platforms:** Linux, Network Devices  

## Description
[TRAILBLAZE](https://attack.mitre.org/software/S9012) is an in-memory dropper used to deploy the passive backdoor [BRUSHFIRE](https://attack.mitre.org/software/S9011). First reported in March 2025, TRAILBLAZE has been observed in operations attributed to People's Republic of China (PRC) state-sponsored affiliated actors, including UNC5221 and SYLVANITE. (Citation: Dragos SYLVANITE MuddyWater Electrum March 2026)(Citation: Google UNC5221 Ivanti April 2025)(Citation: Picus Security UNC5221 Ivanti May 2025)

## Techniques Used
- T1055.012: Process Hollowing
- T1057: Process Discovery
- T1070.004: File Deletion
- T1106: Native API
