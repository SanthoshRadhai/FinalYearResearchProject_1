# T1197: BITS Jobs


**ATT&CK ID:** T1197  
**Domain:** Mitre Attack  
**Tactic(s):** Stealth, Persistence, Execution  
**Platforms:** Windows  
**Reference:** https://attack.mitre.org/techniques/T1197  

## Description
Adversaries may abuse BITS jobs to persistently execute code and perform various background tasks. Windows Background Intelligent Transfer Service (BITS) is a low-bandwidth, asynchronous file transfer mechanism exposed through [Component Object Model](https://attack.mitre.org/techniques/T1559/001) (COM).(Citation: Microsoft COM)(Citation: Microsoft BITS) BITS is commonly used by updaters, messengers, and other applications preferred to operate in the background (using available idle bandwidth) without interrupting other networked applications. File transfer tasks are implemented as BITS jobs, which contain a queue of one or more file operations.

The interface to create and manage BITS jobs is accessible through [PowerShell](https://attack.mitre.org/techniques/T1059/001) and the [BITSAdmin](https://attack.mitre.org/software/S0190) tool.(Citation: Microsoft BITS)(Citation: Microsoft BITSAdmin)

Adversaries may abuse BITS to download (e.g. [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)), execute, and even clean up after running malicious code (e.g. [Indicator Removal](https://attack.mitre.org/techniques/T1070)). BITS tasks are self-contained in the BITS job database, without new files or registry modifications, and often permitted by host firewalls.(Citation: CTU BITS Malware June 2016)(Citation: Mondok Windows PiggyBack BITS May 2007)(Citation: Symantec BITS May 2007) BITS enabled execution may also enable persistence by creating long-standing jobs (the default maximum lifetime is 90 days and extendable) or invoking an arbitrary program when a job completes or errors (including after system reboots).(Citation: PaloAlto UBoatRAT Nov 2017)(Citation: CTU BITS Malware June 2016)

BITS upload functionalities can also be used to perform [Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048).(Citation: CTU BITS Malware June 2016)

## Mitigations
- M1018: User Account Management
- M1028: Operating System Configuration
- M1037: Filter Network Traffic

## Known Threat Groups Using This Technique
- G0087: APT39
- G0096: APT41
- G0065: Leviathan
- G0040: Patchwork
- G0102: Wizard Spider

## Known Software Using This Technique
- S0190: BITSAdmin
- S0534: Bazar
- S0154: Cobalt Strike
- S0554: Egregor
- S0201: JPIN
- S0652: MarkiRAT
- S0654: ProLock
- S0333: UBoatRAT
