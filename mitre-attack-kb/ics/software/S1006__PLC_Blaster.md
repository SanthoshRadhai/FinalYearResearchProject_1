# S1006: PLC-Blaster

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1006  
**Aliases:** PLC-Blaster  

## Description
[PLC-Blaster](https://attack.mitre.org/software/S1006) is a piece of proof-of-concept malware that runs on Siemens S7 PLCs. This worm locates other Siemens S7 PLCs on the network and attempts to infect them.  Once this worm has infected its target and attempted to infect other devices on the network, the worm can then run one of many modules. (Citation: Spenneberg, Ralf, Maik Brggemann, and Hendrik Schwartke March 2016) (Citation: Spenneberg, Ralf 2016)

## Techniques Used
- T0814: Denial of Service
- T0821: Modify Controller Tasking
- T0834: Native API
- T0835: Manipulate I/O Image
- T0843: Program Download
- T0846.001: Port Scan
- T0858: Change Operating Mode
- T0889: Modify Program
