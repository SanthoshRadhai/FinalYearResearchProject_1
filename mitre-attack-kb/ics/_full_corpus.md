# MITRE ATT&CK — ICS domain


---

# C0041: FrostyGoop Incident

**Type:** campaign  
**Reference:** https://attack.mitre.org/campaigns/C0041  
**Aliases:** FrostyGoop Incident  

## Description
[FrostyGoop Incident](https://attack.mitre.org/campaigns/C0041) took place in January 2024 against a municipal district heating company in Ukraine. Following initial access via likely exploitation of external facing services, [FrostyGoop](https://attack.mitre.org/software/S1165) was used to manipulate ENCO control systems via legitimate Modbus commands to impact the delivery of heating services to Ukrainian civilians.(Citation: Dragos FROSTYGOOP 2024)(Citation: Nozomi BUSTLEBERM 2024)


---

# C0030: Triton Safety Instrumented System Attack

**Type:** campaign  
**Reference:** https://attack.mitre.org/campaigns/C0030  
**Aliases:** Triton Safety Instrumented System Attack  

## Description
[Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030) was a campaign employed by [TEMP.Veles](https://attack.mitre.org/groups/G0088) which leveraged the [Triton](https://attack.mitre.org/software/S1009) malware framework against a petrochemical organization.(Citation: Triton-EENews-2017) The malware and techniques used within this campaign targeted specific Triconex [Safety Controller](https://attack.mitre.org/assets/A0010)s within the environment.(Citation: FireEye TRITON 2018) The incident was eventually discovered due to a safety trip that occurred as a result of an issue in the malware.(Citation: FireEye TRITON 2017)


---

# C0028: 2015 Ukraine Electric Power Attack

**Type:** campaign  
**Reference:** https://attack.mitre.org/campaigns/C0028  
**Aliases:** 2015 Ukraine Electric Power Attack  

## Description
[2015 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0028) was a [Sandworm Team](https://attack.mitre.org/groups/G0034) campaign during which they used [BlackEnergy](https://attack.mitre.org/software/S0089) (specifically BlackEnergy3) and [KillDisk](https://attack.mitre.org/software/S0607) to target and disrupt transmission and distribution substations within the Ukrainian power grid. This campaign was the first major public attack conducted against the Ukrainian power grid by Sandworm Team.


---

# C0020: Maroochy Water Breach

**Type:** campaign  
**Reference:** https://attack.mitre.org/campaigns/C0020  
**Aliases:** Maroochy Water Breach  

## Description
[Maroochy Water Breach](https://attack.mitre.org/campaigns/C0020) was an incident in 2000 where an adversary leveraged the local government’s wastewater control system and stolen engineering equipment to disrupt and eventually release 800,000 liters of raw sewage into the local community.(Citation: Marshall Abrams July 2008)


---

# C0031: Unitronics Defacement Campaign

**Type:** campaign  
**Reference:** https://attack.mitre.org/campaigns/C0031  
**Aliases:** Unitronics Defacement Campaign  

## Description
The [Unitronics Defacement Campaign](https://attack.mitre.org/campaigns/C0031) was a collection of intrusions across multiple sectors by the [CyberAv3ngers](https://attack.mitre.org/groups/G1027), where threat actors engaged in a seemingly opportunistic and global targeting and defacement of Unitronics Vision Series [Programmable Logic Controller (PLC)](https://attack.mitre.org/assets/A0003) with [Human-Machine Interface (HMI)](https://attack.mitre.org/assets/A0002). The sectors that these PLCs can be commonly found in are water and wastewater, energy, food and beverage manufacturing, and healthcare. The most notable feature of this attack was the defacement of the PLCs' HMIs.(Citation: CISA AA23-335A IRGC-Affiliated December 2023)(Citation: Frank Bajak and Marc Levy December 2023)


---

# C0063: 2025 Poland Wiper Attacks

**Type:** campaign  
**Reference:** https://attack.mitre.org/campaigns/C0063  
**Aliases:** 2025 Poland Wiper Attacks, 2025 Poland Wiper Campaign  

## Description
[2025 Poland Wiper Attacks](https://attack.mitre.org/campaigns/C0063) is a Russian state-sponsored campaign that conducted destructive cyberattacks against Polish energy infrastructure in December 2025. Targets included more than 30 wind and photovoltaic farms, a combined heat and power (CHP) plant, and a manufacturing sector company. The attacks on the distributed energy resources (DER) disrupted communications between affected facilities and the distribution system operator, but did not impact electricity generation or heat supply. Across the campaign, threat actors deployed two previously undocumented wiper tools, [DynoWiper](https://attack.mitre.org/software/S9038), a Windows-based wiper and [LazyWiper](https://attack.mitre.org/software/S9039), a PowerShell wiper, distributed via malicious Group Policy Objects. At the CHP plant, threat actors had maintained access since at least March 2025, using that foothold to obtain credentials and move laterally before attempting wiper deployment. Some reporting has assessed the activity to be consistent with Russian Federal Security Service (FSB) threat activity group [Dragonfly](https://attack.mitre.org/groups/G0035), also tracked as STATIC TUNDRA, while other reporting attributes the destructive wiper activities to the Russian General Staff Main Intelligence Directorate (GRU) threat activity group ELECTRUM, also tracked as [Sandworm Team](https://attack.mitre.org/groups/G0034).(Citation: CERT Polska)(Citation: Dragos ELECTRUM JAN 2026)(Citation: ESET DynoWiper JAN 2026)(Citation: ESET DynoWiper Update JAN 2026)


---

# C0025: 2016 Ukraine Electric Power Attack

**Type:** campaign  
**Reference:** https://attack.mitre.org/campaigns/C0025  
**Aliases:** 2016 Ukraine Electric Power Attack  

## Description
[2016 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0025) was a [Sandworm Team](https://attack.mitre.org/groups/G0034) campaign during which they used [Industroyer](https://attack.mitre.org/software/S0604) malware to target and disrupt distribution substations within the Ukrainian power grid. This campaign was the second major public attack conducted against Ukraine by [Sandworm Team](https://attack.mitre.org/groups/G0034).(Citation: ESET Industroyer)(Citation: Dragos Crashoverride 2018)


---

# C0034: 2022 Ukraine Electric Power Attack

**Type:** campaign  
**Reference:** https://attack.mitre.org/campaigns/C0034  
**Aliases:** 2022 Ukraine Electric Power Attack  

## Description
The [2022 Ukraine Electric Power Attack](https://attack.mitre.org/campaigns/C0034) was a [Sandworm Team](https://attack.mitre.org/groups/G0034) campaign that used a combination of GOGETTER, Neo-REGEORG, [CaddyWiper](https://attack.mitre.org/software/S0693), and living of the land (LotL) techniques to gain access to a Ukrainian electric utility to send unauthorized commands from their SCADA system.(Citation: Mandiant-Sandworm-Ukraine-2022)(Citation: Dragos-Sandworm-Ukraine-2022)


---

# M0948: Application Isolation and Sandboxing

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0948  

## Description
Restrict the execution of code to a virtual environment on or in-transit to an endpoint system.

## Techniques Mitigated
- T0817: Drive-by Compromise
- T0819: Exploit Public-Facing Application
- T0820: Exploitation for Evasion
- T0853: Scripting
- T0866: Exploitation of Remote Services
- T0890: Exploitation for Privilege Escalation


---

# M0937: Filter Network Traffic

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0937  

## Description
Use network appliances to filter ingress or egress traffic and perform protocol-based filtering. Configure software on endpoints to filter network traffic.   Perform inline allow/denylisting of network messages based on the application layer (OSI Layer 7) protocol, especially for automation protocols. Application allowlists are beneficial when there are well-defined communication sequences, types, rates, or patterns needed during expected system operations. Application denylists may be needed if all acceptable communication sequences cannot be defined, but instead a set of known malicious uses can be denied (e.g., excessive communication  attempts, shutdown messages, invalid commands).  Devices performing these functions are often referred to as deep-packet inspection (DPI) firewalls, context-aware firewalls, or firewalls blocking specific automation/SCADA protocol aware firewalls. (Citation: Centre for the Protection of National Infrastructure February 2005)

## Techniques Mitigated
- T0800: Activate Firmware Update Mode
- T0806: Brute Force I/O
- T0816: Device Restart/Shutdown
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0845: Program Upload
- T0848: Rogue Master
- T0859: Valid Accounts
- T0861: Point & Tag Identification
- T0868: Detect Operating Mode
- T0884: Connection Proxy
- T0886: Remote Services
- T1692: Unauthorized Message
- T1692.001: Command Message
- T1692.002: Reporting Message
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware


---

# M0921: Restrict Web-Based Content

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0921  

## Description
Restrict use of certain websites, block downloads/attachments, block Javascript, restrict browser extensions, etc.

## Techniques Mitigated
- T0817: Drive-by Compromise
- T0863: User Execution
- T0865: Spearphishing Attachment


---

# M0818: Validate Program Inputs

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0818  

## Description
Devices and programs designed to interact with control system parameters should validate the format and content of all user inputs and actions to ensure the values are within intended operational ranges. These values should be evaluated and further enforced through the program logic running on the field controller. If a problematic or invalid input is identified, the programs should either utilize a predetermined safe value or enter a known safe state, while also logging or alerting on the event.(Citation: PLCTop20 Mar 2023)

## Techniques Mitigated
- T0836: Modify Parameter
- T1692.001: Command Message


---

# M0930: Network Segmentation

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0930  

## Description
Architect sections of the network to isolate critical systems, functions, or resources. Use physical and logical segmentation to prevent access to potentially sensitive systems and information. Use a DMZ to contain any internet-facing services that should not be exposed from the internal network.  Restrict network access to only required systems and services. In addition, prevent systems from other networks or business functions (e.g., enterprise) from accessing critical process control systems. For example, in IEC 62443, systems within the same secure level should be grouped into a zone, and access to that zone is restricted by a conduit, or mechanism to restrict data flows between zones by segmenting the network. (Citation: IEC February 2019) (Citation: IEC August 2013)

## Techniques Mitigated
- T0800: Activate Firmware Update Mode
- T0802: Automated Collection
- T0806: Brute Force I/O
- T0816: Device Restart/Shutdown
- T0819: Exploit Public-Facing Application
- T0822: External Remote Services
- T0830: Adversary-in-the-Middle
- T0838: Modify Alarm Settings
- T0842: Network Sniffing
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0845: Program Upload
- T0846.001: Port Scan
- T0846.002: Broadcast Discovery
- T0846.003: Multicast Discovery
- T0848: Rogue Master
- T0858: Change Operating Mode
- T0861: Point & Tag Identification
- T0864: Transient Cyber Asset
- T0866: Exploitation of Remote Services
- T0868: Detect Operating Mode
- T0869: Standard Application Layer Protocol
- T0878: Alarm Suppression
- T0881: Service Stop
- T0883: Internet Accessible Device
- T0885: Commonly Used Port
- T0886: Remote Services
- T1692: Unauthorized Message
- T1692.001: Command Message
- T1692.002: Reporting Message
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware
- T1695: Block Communications
- T1695.001: Serial COM
- T1695.002: Ethernet
- T1695.003: Wi-Fi


---

# M0944: Restrict Library Loading

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0944  

## Description
Prevent abuse of library loading mechanisms in the operating system and software to load untrusted code by configuring appropriate library loading mechanisms and investigating potential vulnerable software.

## Techniques Mitigated
- T0874: Hooking


---

# M0915: Active Directory Configuration

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0915  

## Description
Configure Active Directory to prevent use of certain techniques; use security identifier (SID) Filtering, etc.

## Techniques Mitigated
- T0859: Valid Accounts


---

# M0931: Network Intrusion Prevention

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0931  

## Description
Use intrusion detection signatures to block traffic at network boundaries.  In industrial control environments, network intrusion prevention should be configured so it will not disrupt protocols and communications responsible for real-time functions related to control or safety.

## Techniques Mitigated
- T0830: Adversary-in-the-Middle
- T0846.001: Port Scan
- T0863: User Execution
- T0865: Spearphishing Attachment
- T0867: Lateral Tool Transfer
- T0869: Standard Application Layer Protocol
- T0884: Connection Proxy
- T0885: Commonly Used Port


---

# M0924: Restrict Registry Permissions

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0924  

## Description
Restrict the ability to modify certain hives or keys in the Windows Registry.

## Techniques Mitigated
- T0881: Service Stop


---

# M0803: Data Loss Prevention

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0803  

## Description
Data Loss Prevention (DLP) technologies can be used to help identify adversarial attempts to exfiltrate operational information, such as engineering plans, trade secrets, recipes, intellectual property, or process telemetry. DLP functionality may be built into other security products such as firewalls or standalone suites running on the network and host-based agents. DLP may be configured to prevent the transfer of information through corporate resources such as email, web, and physical media such as USB for host-based solutions.

## Techniques Mitigated
- T0882: Theft of Operational Information
- T0893: Data from Local System


---

# M0801: Access Management

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0801  

## Description
Access Management technologies can be used to enforce authorization polices and decisions, especially when existing field devices do not provide sufficient capabilities to support user identification and authentication. (Citation: McCarthy, J et al. July 2018) These technologies typically utilize an in-line network device or gateway system to prevent access to unauthenticated users, while also integrating with an authentication service to first verify user credentials. (Citation: Centre for the Protection of National Infrastructure November 2010)

## Techniques Mitigated
- T0800: Activate Firmware Update Mode
- T0816: Device Restart/Shutdown
- T0838: Modify Alarm Settings
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0845: Program Upload
- T0858: Change Operating Mode
- T0859: Valid Accounts
- T0861: Point & Tag Identification
- T0868: Detect Operating Mode
- T0871: Execution through API
- T0886: Remote Services
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware
- T1694: Insecure Credentials
- T1694.001: Default Credentials
- T1694.002: Hardcoded Credentials


---

# M0816: Mitigation Limited or Not Effective

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0816  

## Description
This type of attack technique cannot be easily mitigated with preventative controls since it is based on the abuse of system features.

## Techniques Mitigated
- T0801: Monitor Process State
- T0823: Graphical User Interface
- T0835: Manipulate I/O Image
- T0840: Network Connection Enumeration
- T0852: Screen Capture
- T0877: I/O Image


---

# M0950: Exploit Protection

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0950  

## Description
Use capabilities to detect and block conditions that may lead to or be indicative of a software exploit occurring.

## Techniques Mitigated
- T0817: Drive-by Compromise
- T0819: Exploit Public-Facing Application
- T0820: Exploitation for Evasion
- T0866: Exploitation of Remote Services
- T0890: Exploitation for Privilege Escalation


---

# M0935: Limit Access to Resource Over Network

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0935  

## Description
Prevent access to file shares, remote access to systems, unnecessary services. Mechanisms to limit access may include use of network concentrators, RDP gateways, etc.

## Techniques Mitigated
- T0822: External Remote Services


---

# M0938: Execution Prevention

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0938  

## Description
Block execution of code on a system through application control, and/or script blocking.

## Techniques Mitigated
- T0807: Command-Line Interface
- T0834: Native API
- T0849: Masquerading
- T0853: Scripting
- T0863: User Execution
- T0871: Execution through API
- T0894: System Binary Proxy Execution


---

# M0814: Static Network Configuration

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0814  

## Description
Configure hosts and devices to use static network configurations when possible, protocols that require dynamic discovery/addressing (e.g., ARP, DHCP, DNS) can be used to manipulate network message forwarding and enable various AiTM attacks. This mitigation may not always be usable due to limited device features or challenges introduced with different network configurations.

## Techniques Mitigated
- T0830: Adversary-in-the-Middle
- T0842: Network Sniffing
- T0846: Remote System Discovery
- T0846.001: Port Scan
- T0846.002: Broadcast Discovery
- T0846.003: Multicast Discovery
- T0878: Alarm Suppression
- T0888: Remote System Information Discovery
- T1691: Block Operational Technology Message
- T1691.001: Command Message
- T1691.002: Reporting Message


---

# M0927: Password Policies

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0927  

## Description
Set and enforce secure password policies for accounts.

## Techniques Mitigated
- T0822: External Remote Services
- T0859: Valid Accounts
- T0886: Remote Services
- T0892: Change Credential
- T1694.001: Default Credentials


---

# M0926: Privileged Account Management

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0926  

## Description
Manage the creation, modification, use, and permissions associated to privileged accounts, including SYSTEM and root.

## Techniques Mitigated
- T0809: Data Destruction
- T0811: Data from Information Repositories
- T0819: Exploit Public-Facing Application
- T0842: Network Sniffing
- T0859: Valid Accounts
- T0866: Exploitation of Remote Services


---

# M0804: Human User Authentication

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0804  

## Description
Require user authentication before allowing access to data or accepting commands to a device. While strong multi-factor authentication is preferable, it is not always feasible within ICS environments. Performing strong user authentication also requires additional security controls and processes which are often the target of related adversarial techniques (e.g., Valid Accounts, Default Credentials). Therefore, associated ATT&CK mitigations should be considered in addition to this, including [Multi-factor Authentication](https://attack.mitre.org/mitigations/M0932), [Account Use Policies](https://attack.mitre.org/mitigations/M0936), [Password Policies](https://attack.mitre.org/mitigations/M0927), [User Account Management](https://attack.mitre.org/mitigations/M0918), [Privileged Account Management](https://attack.mitre.org/mitigations/M0926), and [User Account Control](https://attack.mitre.org/mitigations/M1052).

## Techniques Mitigated
- T0800: Activate Firmware Update Mode
- T0816: Device Restart/Shutdown
- T0821: Modify Controller Tasking
- T0836: Modify Parameter
- T0838: Modify Alarm Settings
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0845: Program Upload
- T0858: Change Operating Mode
- T0861: Point & Tag Identification
- T0868: Detect Operating Mode
- T0871: Execution through API
- T0885: Commonly Used Port
- T0886: Remote Services
- T0889: Modify Program
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware


---

# M0920: SSL/TLS Inspection

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0920  

## Description
Break and inspect SSL/TLS sessions to look at encrypted web traffic for adversary activity.

## Techniques Mitigated
- T0884: Connection Proxy


---

# M0945: Code Signing

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0945  

## Description
Enforce binary and application integrity with digital signature verification to prevent untrusted code from executing.

## Techniques Mitigated
- T0821: Modify Controller Tasking
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0849: Masquerading
- T0851: Rootkit
- T0862: Supply Chain Compromise
- T0863: User Execution
- T0873: Project File Infection
- T0873.001: Siemens Project File Format
- T0889: Modify Program
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware


---

# M0813: Software Process and Device Authentication

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0813  

## Description
Require the authentication of devices and software processes where appropriate. Devices that connect remotely to other systems should require strong authentication to prevent spoofing of communications. Furthermore, software processes should also require authentication when accessing APIs.

## Techniques Mitigated
- T0800: Activate Firmware Update Mode
- T0806: Brute Force I/O
- T0816: Device Restart/Shutdown
- T0830: Adversary-in-the-Middle
- T0838: Modify Alarm Settings
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0845: Program Upload
- T0848: Rogue Master
- T0858: Change Operating Mode
- T0860: Wireless Compromise
- T0861: Point & Tag Identification
- T0868: Detect Operating Mode
- T0886: Remote Services
- T1692: Unauthorized Message
- T1692.001: Command Message
- T1692.002: Reporting Message
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware


---

# M0808: Encrypt Network Traffic

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0808  

## Description
Utilize strong cryptographic techniques and protocols to prevent eavesdropping on network communications.

## Techniques Mitigated
- T0842: Network Sniffing
- T0860: Wireless Compromise
- T0887: Wireless Sniffing
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware


---

# M0936: Account Use Policies

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0936  

## Description
Configure features related to account use like login attempt lockouts, specific login times, etc.

## Techniques Mitigated
- T0822: External Remote Services
- T0859: Valid Accounts


---

# M0913: Application Developer Guidance

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0913  

## Description
This mitigation describes any guidance or training given to developers of applications to avoid introducing security weaknesses that an adversary may be able to take advantage of.

## Techniques Mitigated
- T0859: Valid Accounts


---

# M0946: Boot Integrity

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0946  

## Description
Use secure methods to boot a system and verify the integrity of the operating system and loading mechanisms.

## Techniques Mitigated
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware


---

# M0805: Mechanical Protection Layers

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0805  

## Description
Utilize a layered protection design based on physical or mechanical protection systems to prevent damage to property, equipment, human safety, or the environment. Examples include interlocks, rupture disk, release values, etc. (Citation: A G Foord, W G Gulland, C R Howard, T Kellacher, W H Smith 2004)

## Techniques Mitigated
- T0879: Damage to Property
- T0880: Loss of Safety


---

# M0951: Update Software

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0951  

## Description
Perform regular software updates to mitigate exploitation risk. Software updates may need to be scheduled around operational down times.

## Techniques Mitigated
- T0817: Drive-by Compromise
- T0819: Exploit Public-Facing Application
- T0820: Exploitation for Evasion
- T0862: Supply Chain Compromise
- T0864: Transient Cyber Asset
- T0866: Exploitation of Remote Services
- T0890: Exploitation for Privilege Escalation
- T1693.001: System Firmware


---

# M0815: Watchdog Timers

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0815  

## Description
Utilize watchdog timers to ensure devices can quickly detect whether a system is unresponsive.

## Techniques Mitigated
- T0814: Denial of Service


---

# M0809: Operational Information Confidentiality

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0809  

## Description
Deploy mechanisms to protect the confidentiality of information related to operational processes, facility locations, device configurations, programs, or databases that may have information that can be used to infer organizational trade-secrets, recipes, and other intellectual property (IP).

## Techniques Mitigated
- T0882: Theft of Operational Information


---

# M0928: Operating System Configuration

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0928  

## Description
Make configuration changes related to the operating system or a common feature of the operating system that result in system hardening against techniques.

## Techniques Mitigated
- T0847: Replication Through Removable Media
- T0895: Autorun Image


---

# M0934: Limit Hardware Installation

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0934  

## Description
Block users or groups from installing or using unapproved hardware on systems, including USB devices.

## Techniques Mitigated
- T0847: Replication Through Removable Media


---

# M0941: Encrypt Sensitive Information

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0941  

## Description
Protect sensitive data-at-rest with strong encryption.

## Techniques Mitigated
- T0811: Data from Information Repositories
- T0864: Transient Cyber Asset
- T0873: Project File Infection
- T0873.001: Siemens Project File Format
- T0882: Theft of Operational Information
- T0893: Data from Local System
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware


---

# M0807: Network Allowlists

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0807  

## Description
Network allowlists can be implemented through either host-based files or system hosts files to specify what connections (e.g., IP address, MAC address, port, protocol) can be made from a device. Allowlist techniques that operate at the  application layer (e.g., DNP3, Modbus, HTTP) are addressed in [Filter Network Traffic](https://attack.mitre.org/mitigations/M0937) mitigation.

## Techniques Mitigated
- T0800: Activate Firmware Update Mode
- T0802: Automated Collection
- T0806: Brute Force I/O
- T0816: Device Restart/Shutdown
- T0838: Modify Alarm Settings
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0845: Program Upload
- T0848: Rogue Master
- T0858: Change Operating Mode
- T0861: Point & Tag Identification
- T0868: Detect Operating Mode
- T0869: Standard Application Layer Protocol
- T0878: Alarm Suppression
- T0879: Damage to Property
- T0884: Connection Proxy
- T0886: Remote Services
- T1691: Block Operational Technology Message
- T1691.001: Command Message
- T1691.002: Reporting Message
- T1692: Unauthorized Message
- T1692.001: Command Message
- T1692.002: Reporting Message
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware
- T1695: Block Communications
- T1695.001: Serial COM
- T1695.002: Ethernet
- T1695.003: Wi-Fi


---

# M0817: Supply Chain Management

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0817  

## Description
Implement a supply chain management program, including policies and procedures to ensure all devices and components originate from a trusted supplier and are tested to verify their integrity.

## Techniques Mitigated
- T0862: Supply Chain Compromise


---

# M0953: Data Backup

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0953  

## Description
Take and store data backups from end user systems and critical servers. Ensure backup and storage systems are hardened and kept separate from the corporate network to prevent compromise.   Maintain and exercise incident response plans  (Citation: Department of Homeland Security October 2009), including the management of  'gold-copy' back-up images and configurations for key systems to enable quick recovery and response from adversarial activities that impact control, view, or availability.

## Techniques Mitigated
- T0809: Data Destruction
- T0813: Denial of Control
- T0815: Denial of View
- T0826: Loss of Availability
- T0827: Loss of Control
- T0828: Loss of Productivity and Revenue
- T0829: Loss of View
- T0831: Manipulation of Control
- T0832: Manipulation of View
- T0892: Change Credential


---

# M0810: Out-of-Band Communications Channel

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0810  

## Description
Have alternative methods to support communication requirements during communication failures and data integrity attacks. (Citation: National Institute of Standards and Technology April 2013) (Citation: Defense Advanced Research Projects Agency)

## Techniques Mitigated
- T0813: Denial of Control
- T0815: Denial of View
- T0826: Loss of Availability
- T0827: Loss of Control
- T0829: Loss of View
- T0830: Adversary-in-the-Middle
- T0831: Manipulation of Control
- T0832: Manipulation of View
- T0878: Alarm Suppression
- T1691: Block Operational Technology Message
- T1691.001: Command Message
- T1691.002: Reporting Message
- T1695: Block Communications
- T1695.001: Serial COM
- T1695.002: Ethernet
- T1695.003: Wi-Fi


---

# M0947: Audit

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0947  

## Description
Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. Perform periodic integrity checks of the device to validate the correctness of the firmware, software, programs, and configurations. Integrity checks, which typically include cryptographic hashes or digital signatures, should be compared to those obtained at known valid states, especially after events like device reboots, program downloads, or program restarts.

## Techniques Mitigated
- T0811: Data from Information Repositories
- T0821: Modify Controller Tasking
- T0830: Adversary-in-the-Middle
- T0836: Modify Parameter
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0851: Rootkit
- T0859: Valid Accounts
- T0862: Supply Chain Compromise
- T0864: Transient Cyber Asset
- T0873: Project File Infection
- T0873.001: Siemens Project File Format
- T0874: Hooking
- T0889: Modify Program
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware


---

# M0802: Communication Authenticity

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0802  

## Description
When communicating over an untrusted network, utilize secure network protocols that both authenticate the message sender and can verify its integrity. This can be done either through message authentication codes (MACs) or digital signatures, to detect spoofed network messages and unauthorized connections.

## Techniques Mitigated
- T0800: Activate Firmware Update Mode
- T0816: Device Restart/Shutdown
- T0830: Adversary-in-the-Middle
- T0831: Manipulation of Control
- T0832: Manipulation of View
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0845: Program Upload
- T0848: Rogue Master
- T0858: Change Operating Mode
- T0860: Wireless Compromise
- T0861: Point & Tag Identification
- T0868: Detect Operating Mode
- T1692: Unauthorized Message
- T1692.001: Command Message
- T1692.002: Reporting Message
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware


---

# M0942: Disable or Remove Feature or Program

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0942  

## Description
Remove or deny access to unnecessary and potentially vulnerable software to prevent abuse by adversaries.

## Techniques Mitigated
- T0807: Command-Line Interface
- T0816: Device Restart/Shutdown
- T0822: External Remote Services
- T0830: Adversary-in-the-Middle
- T0847: Replication Through Removable Media
- T0853: Scripting
- T0866: Exploitation of Remote Services
- T0885: Commonly Used Port


---

# M0919: Threat Intelligence Program

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0919  

## Description
A threat intelligence program helps an organization generate their own threat intelligence information and track trends to inform defensive priorities to mitigate risk.

## Techniques Mitigated
- T0820: Exploitation for Evasion
- T0866: Exploitation of Remote Services
- T0890: Exploitation for Privilege Escalation


---

# M0812: Safety Instrumented Systems

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0812  

## Description
Utilize Safety Instrumented Systems (SIS) to provide an additional layer of protection to hazard scenarios that may cause property damage. A SIS will typically include sensors, logic solvers, and a final control element that can be used to automatically respond to an hazardous condition  (Citation: A G Foord, W G Gulland, C R Howard, T Kellacher, W H Smith 2004) . Ensure that all SISs are segmented from operational networks to prevent them from being targeted by additional adversarial behavior.

## Techniques Mitigated
- T0879: Damage to Property
- T0880: Loss of Safety


---

# M0917: User Training

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0917  

## Description
Train users to be aware of access or manipulation attempts by an adversary to reduce the risk of successful spearphishing, social engineering, and other techniques that involve user interaction.

## Techniques Mitigated
- T0811: Data from Information Repositories
- T0863: User Execution
- T0865: Spearphishing Attachment
- T0893: Data from Local System


---

# M0932: Multi-factor Authentication

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0932  

## Description
Use two or more pieces of evidence to authenticate to a system; such as username and password in addition to a token from a physical smart card or token generator.  Within industrial control environments assets such as low-level controllers, workstations, and HMIs have real-time operational control and safety requirements which may restrict the use of multi-factor.

## Techniques Mitigated
- T0822: External Remote Services
- T0842: Network Sniffing
- T0859: Valid Accounts


---

# M0916: Vulnerability Scanning

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0916  

## Description
Vulnerability scanning is used to find potentially exploitable software vulnerabilities to remediate them.

## Techniques Mitigated
- T0819: Exploit Public-Facing Application
- T0862: Supply Chain Compromise
- T0866: Exploitation of Remote Services


---

# M0800: Authorization Enforcement

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0800  

## Description
The device or system should restrict read, manipulate, or execute privileges to only authenticated users who require access based on approved security policies.  Role-based Access Control (RBAC) schemes can help reduce the overhead of assigning permissions to the large number of devices within an ICS. For example, IEC 62351 provides examples of roles used to support common system operations within the electric power sector  (Citation: International Electrotechnical Commission July 2020), while IEEE 1686 defines standard permissions for users of IEDs. (Citation: Institute of Electrical and Electronics Engineers January 2014)

## Techniques Mitigated
- T0800: Activate Firmware Update Mode
- T0816: Device Restart/Shutdown
- T0821: Modify Controller Tasking
- T0836: Modify Parameter
- T0838: Modify Alarm Settings
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0845: Program Upload
- T0858: Change Operating Mode
- T0861: Point & Tag Identification
- T0868: Detect Operating Mode
- T0871: Execution through API
- T0886: Remote Services
- T0889: Modify Program


---

# M0918: User Account Management

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0918  

## Description
Manage the creation, modification, use, and permissions associated to user accounts.

## Techniques Mitigated
- T0811: Data from Information Repositories
- T0822: External Remote Services
- T0838: Modify Alarm Settings
- T0859: Valid Accounts
- T0881: Service Stop
- T0886: Remote Services


---

# M0811: Redundancy of Service

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0811  

## Description
Redundancy could be provided for both critical ICS devices and services, such as back-up devices or hot-standbys.

## Techniques Mitigated
- T0813: Denial of Control
- T0815: Denial of View
- T0826: Loss of Availability
- T0827: Loss of Control
- T0829: Loss of View
- T0892: Change Credential


---

# M0922: Restrict File and Directory Permissions

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0922  

## Description
Restrict access by setting directory and file permissions that are not specific to users or privileged accounts.

## Techniques Mitigated
- T0809: Data Destruction
- T0811: Data from Information Repositories
- T0849: Masquerading
- T0872: Indicator Removal on Host
- T0873: Project File Infection
- T0873.001: Siemens Project File Format
- T0881: Service Stop
- T0882: Theft of Operational Information
- T0893: Data from Local System


---

# M0954: Software Configuration

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0954  

## Description
Implement configuration changes to software (other than the operating system) to mitigate security risks associated with how the software operates.


---

# M0949: Antivirus/Antimalware

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0949  

## Description
Use signatures or heuristics to detect malicious software.  Within industrial control environments, antivirus/antimalware installations should be limited to assets that are not involved in critical or real-time operations. To minimize the impact to system availability, all products should first be validated within a representative test environment before deployment to production systems. (Citation: NCCIC August 2018)

## Techniques Mitigated
- T0863: User Execution
- T0864: Transient Cyber Asset
- T0865: Spearphishing Attachment


---

# M0806: Minimize Wireless Signal Propagation

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0806  

## Description
Wireless signals frequently propagate outside of organizational boundaries, which provide opportunities for adversaries to monitor or gain unauthorized access to the wireless network. (Citation: CISA March 2010) To minimize this threat, organizations should implement measures to detect, understand, and reduce unnecessary RF propagation. (Citation: DHS  National Urban Security Technology Laboratory April 2019)

## Techniques Mitigated
- T0860: Wireless Compromise
- T0887: Wireless Sniffing


---

# G0082: APT38

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0082  
**Aliases:** APT38, NICKEL GLADSTONE, BeagleBoyz, Bluenoroff, Stardust Chollima, Sapphire Sleet, COPERNICIUM  

## Description
[APT38](https://attack.mitre.org/groups/G0082) is a North Korean state-sponsored threat group that specializes in financial cyber operations; it has been attributed to the Reconnaissance General Bureau.(Citation: CISA AA20-239A BeagleBoyz August 2020) Active since at least 2014, [APT38](https://attack.mitre.org/groups/G0082) has targeted banks, financial institutions, casinos, cryptocurrency exchanges, SWIFT system endpoints, and ATMs in at least 38 countries worldwide. Significant operations include the 2016 Bank of Bangladesh heist, during which [APT38](https://attack.mitre.org/groups/G0082) stole $81 million, as well as attacks against Bancomext (Citation: FireEye APT38 Oct 2018) and Banco de Chile (Citation: FireEye APT38 Oct 2018); some of their attacks have been destructive.(Citation: CISA AA20-239A BeagleBoyz August 2020)(Citation: FireEye APT38 Oct 2018)(Citation: DOJ North Korea Indictment Feb 2021)(Citation: Kaspersky Lazarus Under The Hood Blog 2017)

North Korean group definitions are known to have significant overlap, and some security researchers report all North Korean state-sponsored cyber activity under the name [Lazarus Group](https://attack.mitre.org/groups/G0032) instead of tracking clusters or subgroups.


---

# G1000: ALLANITE

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1000  
**Aliases:** ALLANITE, Palmetto Fusion  

## Description
[ALLANITE](https://attack.mitre.org/groups/G1000) is a suspected Russian cyber espionage group, that has primarily targeted the electric utility sector within the United States and United Kingdom. The group's tactics and techniques are reportedly similar to [Dragonfly](https://attack.mitre.org/groups/G0035), although [ALLANITE](https://attack.mitre.org/groups/G1000)s technical capabilities have not exhibited disruptive or destructive abilities. It has been suggested that the group maintains a presence in ICS for the purpose of gaining understanding of processes and to maintain persistence. (Citation: Dragos)

## Techniques Used
- T0817: Drive-by Compromise
- T0852: Screen Capture
- T0859: Valid Accounts
- T0865: Spearphishing Attachment


---

# G0035: Dragonfly

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0035  
**Aliases:** Dragonfly, TEMP.Isotope, DYMALLOY, Berserk Bear, TG-4192, Crouching Yeti, IRON LIBERTY, Energetic Bear, Ghost Blizzard, BROMINE  

## Description
[Dragonfly](https://attack.mitre.org/groups/G0035) is a cyber espionage group that has been attributed to Russia's Federal Security Service (FSB) Center 16.(Citation: DOJ Russia Targeting Critical Infrastructure March 2022)(Citation: UK GOV FSB Factsheet April 2022) Active since at least 2010, [Dragonfly](https://attack.mitre.org/groups/G0035) has targeted defense and aviation companies, government entities, companies related to industrial control systems, and critical infrastructure sectors worldwide through supply chain, spearphishing, and drive-by compromise attacks.(Citation: Symantec Dragonfly)(Citation: Secureworks IRON LIBERTY July 2019)(Citation: Symantec Dragonfly Sept 2017)(Citation: Fortune Dragonfly 2.0 Sept 2017)(Citation: Gigamon Berserk Bear October 2021)(Citation: CISA AA20-296A Berserk Bear December 2020)(Citation: Symantec Dragonfly 2.0 October 2017)

## Techniques Used
- T0817: Drive-by Compromise
- T0862: Supply Chain Compromise


---

# G0037: FIN6

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0037  
**Aliases:** FIN6, Magecart Group 6, ITG08, Skeleton Spider, TAAL, Camouflage Tempest  

## Description
[FIN6](https://attack.mitre.org/groups/G0037) is a cyber crime group that has stolen payment card data and sold it for profit on underground marketplaces. This group has aggressively targeted and compromised point of sale (PoS) systems in the hospitality and retail sectors.(Citation: FireEye FIN6 April 2016)(Citation: FireEye FIN6 Apr 2019)


---

# G0046: FIN7

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0046  
**Aliases:** FIN7, GOLD NIAGARA, ITG14, Carbon Spider, ELBRUS, Sangria Tempest  

## Description
[FIN7](https://attack.mitre.org/groups/G0046) is a financially-motivated threat group that has been active since 2013. [FIN7](https://attack.mitre.org/groups/G0046) has targeted the retail, restaurant, hospitality, software, consulting, financial services, medical equipment, cloud services, media, food and beverage, transportation, pharmaceutical, and utilities industries in the United States. A portion of [FIN7](https://attack.mitre.org/groups/G0046) was operated out of a front company called Combi Security and often used point-of-sale malware for targeting efforts. Since 2020, [FIN7](https://attack.mitre.org/groups/G0046) shifted operations to big game hunting (BGH), including use of [REvil](https://attack.mitre.org/software/S0496) ransomware and their own Ransomware-as-a-Service (RaaS), Darkside. FIN7 may be linked to the [Carbanak](https://attack.mitre.org/groups/G0008) Group, but multiple threat groups have been observed using [Carbanak](https://attack.mitre.org/software/S0030), leading these groups to be tracked separately.(Citation: FireEye FIN7 March 2017)(Citation: FireEye FIN7 April 2017)(Citation: FireEye CARBANAK June 2017)(Citation: FireEye FIN7 Aug 2018)(Citation: CrowdStrike Carbon Spider August 2021)(Citation: Mandiant FIN7 Apr 2022)(Citation: BiZone Lizar May 2021)


---

# G0034: Sandworm Team

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0034  
**Aliases:** Sandworm Team, ELECTRUM, Telebots, IRON VIKING, BlackEnergy (Group), Quedagh, Voodoo Bear, IRIDIUM, Seashell Blizzard, FROZENBARENTS, APT44  

## Description
[Sandworm Team](https://attack.mitre.org/groups/G0034) is a destructive threat group that has been attributed to Russia's General Staff Main Intelligence Directorate (GRU) Main Center for Special Technologies (GTsST) military unit 74455.(Citation: US District Court Indictment GRU Unit 74455 October 2020)(Citation: UK NCSC Olympic Attacks October 2020) This group has been active since at least 2009.(Citation: iSIGHT Sandworm 2014)(Citation: CrowdStrike VOODOO BEAR)(Citation: USDOJ Sandworm Feb 2020)(Citation: NCSC Sandworm Feb 2020)

In October 2020, the US indicted six GRU Unit 74455 officers associated with [Sandworm Team](https://attack.mitre.org/groups/G0034) for the following cyber operations: the 2015 and 2016 attacks against Ukrainian electrical companies and government organizations, the 2017 worldwide [NotPetya](https://attack.mitre.org/software/S0368) attack, targeting of the 2017 French presidential campaign, the 2018 [Olympic Destroyer](https://attack.mitre.org/software/S0365) attack against the Winter Olympic Games, the 2018 operation against the Organisation for the Prohibition of Chemical Weapons, and attacks against the country of Georgia in 2018 and 2019.(Citation: US District Court Indictment GRU Unit 74455 October 2020)(Citation: UK NCSC Olympic Attacks October 2020) Some of these were conducted with the assistance of GRU Unit 26165, which is also referred to as [APT28](https://attack.mitre.org/groups/G0007).(Citation: US District Court Indictment GRU Oct 2018)

## Techniques Used
- T0807: Command-Line Interface
- T0819: Exploit Public-Facing Application
- T0884: Connection Proxy


---

# G0049: OilRig

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0049  
**Aliases:** OilRig, COBALT GYPSY, IRN2, APT34, Helix Kitten, Evasive Serpens, Hazel Sandstorm, EUROPIUM, ITG13, Earth Simnavaz, Crambus, TA452  

## Description
[OilRig](https://attack.mitre.org/groups/G0049) is a suspected Iranian threat group that has targeted Middle Eastern and international victims since at least 2014. The group has targeted a variety of sectors, including financial, government, energy, chemical, and telecommunications. It appears the group carries out supply chain attacks, leveraging the trust relationship between organizations to attack their primary targets. The group works on behalf of the Iranian government based on infrastructure details that contain references to Iran, use of Iranian infrastructure, and targeting that aligns with nation-state interests.(Citation: FireEye APT34 Dec 2017)(Citation: Palo Alto OilRig April 2017)(Citation: ClearSky OilRig Jan 2017)(Citation: Palo Alto OilRig May 2016)(Citation: Palo Alto OilRig Oct 2016)(Citation: Unit42 OilRig Playbook 2023)(Citation: Unit 42 QUADAGENT July 2018)

## Techniques Used
- T0817: Drive-by Compromise
- T0853: Scripting
- T0859: Valid Accounts
- T0865: Spearphishing Attachment
- T0869: Standard Application Layer Protocol


---

# G0088: TEMP.Veles

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0088  
**Aliases:** TEMP.Veles, XENOTIME  

## Description
[TEMP.Veles](https://attack.mitre.org/groups/G0088) is a Russia-based threat group that has targeted critical infrastructure. The group has been observed utilizing [TRITON](https://attack.mitre.org/software/S0609), a malware framework designed to manipulate industrial safety systems.(Citation: FireEye TRITON 2019)(Citation: FireEye TEMP.Veles 2018)(Citation: FireEye TEMP.Veles JSON April 2019)

## Techniques Used
- T0817: Drive-by Compromise
- T0862: Supply Chain Compromise


---

# G1027: CyberAv3ngers

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1027  
**Aliases:** CyberAv3ngers, Soldiers of Soloman  

## Description
The [CyberAv3ngers](https://attack.mitre.org/groups/G1027) are a suspected Iranian Government Islamic Revolutionary Guard Corps (IRGC)-affiliated APT group. The [CyberAv3ngers](https://attack.mitre.org/groups/G1027) have been known to be active since at least 2020, with disputed and false claims of critical infrastructure compromises in Israel.(Citation: CISA AA23-335A IRGC-Affiliated December 2023)

In 2023, the [CyberAv3ngers](https://attack.mitre.org/groups/G1027) engaged in a global targeting and hacking of the Unitronics [Programmable Logic Controller (PLC)](https://attack.mitre.org/assets/A0003) with [Human-Machine Interface (HMI)](https://attack.mitre.org/assets/A0002). This PLC can be found in multiple sectors, including water and wastewater, energy, food and beverage manufacturing, and healthcare. The most notable feature of this attack was the defacement of the devices user interface.(Citation: CISA AA23-335A IRGC-Affiliated December 2023)


---

# G0115: GOLD SOUTHFIELD

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0115  
**Aliases:** GOLD SOUTHFIELD, Pinchy Spider  

## Description
[GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) is a financially motivated threat group active since at least 2018 that operates the [REvil](https://attack.mitre.org/software/S0496) Ransomware-as-a Service (RaaS). [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) provides backend infrastructure for affiliates recruited on underground forums to perpetrate high value deployments. By early 2020, [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) started capitalizing on the new trend of stealing data and further extorting the victim to pay for their data to not get publicly leaked.(Citation: Secureworks REvil September 2019)(Citation: Secureworks GandCrab and REvil September 2019)(Citation: Secureworks GOLD SOUTHFIELD)(Citation: CrowdStrike Evolution of Pinchy Spider July 2021)


---

# G0032: Lazarus Group

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0032  
**Aliases:** Lazarus Group, Labyrinth Chollima, HIDDEN COBRA, Guardians of Peace, ZINC, NICKEL ACADEMY, Diamond Sleet  

## Description
[Lazarus Group](https://attack.mitre.org/groups/G0032) is a North Korean state-sponsored cyber threat group attributed to the Reconnaissance General Bureau (RGB). (Citation: US-CERT HIDDEN COBRA June 2017) (Citation: Treasury North Korean Cyber Groups September 2019) [Lazarus Group](https://attack.mitre.org/groups/G0032) has been active since at least 2009 and is reportedly responsible for the November 2014 destructive wiper attack on Sony Pictures Entertainment, identified by Novetta as part of Operation Blockbuster. Malware used by [Lazarus Group](https://attack.mitre.org/groups/G0032) correlates to other reported campaigns, including Operation Flame, Operation 1Mission, Operation Troy, DarkSeoul, and Ten Days of Rain.(Citation: Novetta Blockbuster)

North Korea’s cyber operations have shown a consistent pattern of adaptation, forming and reorganizing units as national priorities shift. These units frequently share personnel, infrastructure, malware, and tradecraft, making it difficult to attribute specific operations with high confidence. Public reporting often uses “Lazarus Group” as an umbrella term for multiple North Korean cyber operators conducting espionage, destructive attacks, and financially motivated campaigns.(Citation: Mandiant DPRK Laz Org Breakdown 2022)(Citation: Mandiant DPRK Groups 2023)(Citation: JPCert Blog Laz Subgroups 2025)

## Techniques Used
- T0865: Spearphishing Attachment


---

# G0102: Wizard Spider

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0102  
**Aliases:** Wizard Spider, UNC1878, TEMP.MixMaster, Grim Spider, FIN12, GOLD BLACKBURN, ITG23, Periwinkle Tempest, DEV-0193, Pistachio Tempest, DEV-0237  

## Description
[Wizard Spider](https://attack.mitre.org/groups/G0102) is a Russia-based financially motivated threat group originally known for the creation and deployment of [TrickBot](https://attack.mitre.org/software/S0266) since at least 2016. [Wizard Spider](https://attack.mitre.org/groups/G0102) possesses a diverse arsenal of tools and has conducted ransomware campaigns against a variety of organizations, ranging from major corporations to hospitals.(Citation: CrowdStrike Ryuk January 2019)(Citation: DHS/CISA Ransomware Targeting Healthcare October 2020)(Citation: CrowdStrike Wizard Spider October 2020)


---

# G1001: HEXANE

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1001  
**Aliases:** HEXANE, Lyceum, Siamesekitten, Spirlin  

## Description
[HEXANE](https://attack.mitre.org/groups/G1001) is a cyber espionage threat group that has targeted oil & gas, telecommunications, aviation, and internet service provider organizations since at least 2017. Targeted companies have been located in the Middle East and Africa, including Israel, Saudi Arabia, Kuwait, Morocco, and Tunisia. [HEXANE](https://attack.mitre.org/groups/G1001)'s TTPs appear similar to [APT33](https://attack.mitre.org/groups/G0064) and [OilRig](https://attack.mitre.org/groups/G0049) but due to differences in victims and tools it is tracked as a separate entity.(Citation: Dragos Hexane)(Citation: Kaspersky Lyceum October 2021)(Citation: ClearSky Siamesekitten August 2021)(Citation: Accenture Lyceum Targets November 2021)


---

# G0064: APT33

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0064  
**Aliases:** APT33, HOLMIUM, Elfin, Peach Sandstorm  

## Description
[APT33](https://attack.mitre.org/groups/G0064) is a suspected Iranian threat group that has carried out operations since at least 2013. The group has targeted organizations across multiple industries in the United States, Saudi Arabia, and South Korea, with a particular interest in the aviation and energy sectors.(Citation: FireEye APT33 Sept 2017)(Citation: FireEye APT33 Webinar Sept 2017)

## Techniques Used
- T0852: Screen Capture
- T0853: Scripting
- T0865: Spearphishing Attachment


---

# S0605: EKANS

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0605  
**Aliases:** EKANS, SNAKEHOSE  
**Platforms:** Windows  

## Description
[EKANS](https://attack.mitre.org/software/S0605) is ransomware variant written in Golang that first appeared in mid-December 2019 and has been used against multiple sectors, including energy, healthcare, and automotive manufacturing, which in some cases resulted in significant operational disruptions. [EKANS](https://attack.mitre.org/software/S0605) has used a hard-coded kill-list of processes, including some associated with common ICS software platforms (e.g., GE Proficy, Honeywell HMIWeb, etc), similar to those defined in [MegaCortex](https://attack.mitre.org/software/S0576).(Citation: Dragos EKANS)(Citation: Palo Alto Unit 42 EKANS)

## Techniques Used
- T0828: Loss of Productivity and Revenue
- T0840: Network Connection Enumeration
- T0849: Masquerading
- T0881: Service Stop


---

# S0093: Backdoor.Oldrea

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0093  
**Aliases:** Backdoor.Oldrea, Havex  
**Platforms:** Windows  

## Description
[Backdoor.Oldrea](https://attack.mitre.org/software/S0093) is a modular backdoor that used by [Dragonfly](https://attack.mitre.org/groups/G0035) against energy companies since at least 2013. [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) was distributed via supply chain compromise, and included specialized modules to enumerate and map ICS-specific systems, processes, and protocols.(Citation: Symantec Dragonfly)(Citation: Gigamon Berserk Bear October 2021)(Citation: Symantec Dragonfly Sept 2017)

## Techniques Used
- T0802: Automated Collection
- T0814: Denial of Service
- T0846: Remote System Discovery
- T0861: Point & Tag Identification
- T0862: Supply Chain Compromise
- T0863: User Execution
- T0865: Spearphishing Attachment
- T0888: Remote System Information Discovery


---

# S0603: Stuxnet

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0603  
**Aliases:** Stuxnet, W32.Stuxnet  
**Platforms:** Windows  

## Description
[Stuxnet](https://attack.mitre.org/software/S0603) was the first publicly reported malware to specifically target industrial control systems devices. [Stuxnet](https://attack.mitre.org/software/S0603) is a large and complex malware that utilized multiple behaviors, including numerous zero-day vulnerabilities, a sophisticated Windows rootkit, and network infection routines.(Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)(Citation: CISA ICS Advisory ICSA-10-272-01)(Citation: ESET Stuxnet Under the Microscope)(Citation: Langer Stuxnet) [Stuxnet](https://attack.mitre.org/software/S0603) was discovered in 2010, with some components being used as early as November 2008.(Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

## Techniques Used
- T0801: Monitor Process State
- T0807: Command-Line Interface
- T0821: Modify Controller Tasking
- T0831: Manipulation of Control
- T0832: Manipulation of View
- T0834: Native API
- T0835: Manipulate I/O Image
- T0836: Modify Parameter
- T0842: Network Sniffing
- T0843: Program Download
- T0847: Replication Through Removable Media
- T0849: Masquerading
- T0851: Rootkit
- T0863: User Execution
- T0866: Exploitation of Remote Services
- T0867: Lateral Tool Transfer
- T0869: Standard Application Layer Protocol
- T0873.001: Siemens Project File Format
- T0874: Hooking
- T0877: I/O Image
- T0885: Commonly Used Port
- T0886: Remote Services
- T0888: Remote System Information Discovery
- T0889: Modify Program
- T1694.002: Hardcoded Credentials


---

# S0606: Bad Rabbit

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0606  
**Aliases:** Bad Rabbit, Win32/Diskcoder.D  
**Platforms:** Windows  

## Description
[Bad Rabbit](https://attack.mitre.org/software/S0606) is a self-propagating ransomware that affected the Ukrainian transportation sector in 2017. [Bad Rabbit](https://attack.mitre.org/software/S0606) has also targeted organizations and consumers in Russia. (Citation: Secure List Bad Rabbit)(Citation: ESET Bad Rabbit)(Citation: Dragos Apr 2019)

## Techniques Used
- T0817: Drive-by Compromise
- T0828: Loss of Productivity and Revenue
- T0863: User Execution
- T0866: Exploitation of Remote Services
- T0867: Lateral Tool Transfer


---

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


---

# S0089: BlackEnergy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0089  
**Aliases:** BlackEnergy, Black Energy  
**Platforms:** Windows  

## Description
[BlackEnergy](https://attack.mitre.org/software/S0089) is a malware toolkit that has been used by both criminal and APT actors. It dates back to at least 2007 and was originally designed to create botnets for use in conducting Distributed Denial of Service (DDoS) attacks, but its use has evolved to support various plug-ins. It is well known for being used during the confrontation between Georgia and Russia in 2008, as well as in targeting Ukrainian institutions. Variants include BlackEnergy 2 and BlackEnergy 3. (Citation: F-Secure BlackEnergy 2014)

## Techniques Used
- T0859: Valid Accounts
- T0865: Spearphishing Attachment
- T0869: Standard Application Layer Protocol


---

# S0368: NotPetya

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0368  
**Aliases:** NotPetya, ExPetr, Diskcoder.C, GoldenEye, Petrwrap, Nyetya  
**Platforms:** Windows  

## Description
[NotPetya](https://attack.mitre.org/software/S0368) is malware that was used by [Sandworm Team](https://attack.mitre.org/groups/G0034) in a worldwide attack starting on June 27, 2017. While [NotPetya](https://attack.mitre.org/software/S0368) appears as a form of ransomware, its main purpose was to destroy data and disk structures on compromised systems; the attackers never intended to make the encrypted data recoverable. As such, [NotPetya](https://attack.mitre.org/software/S0368) may be more appropriately thought of as a form of wiper malware. [NotPetya](https://attack.mitre.org/software/S0368) contains worm-like features to spread itself across a computer network using the SMBv1 exploits EternalBlue and EternalRomance.(Citation: Talos Nyetya June 2017)(Citation: US-CERT NotPetya 2017)(Citation: ESET Telebots June 2017)(Citation: US District Court Indictment GRU Unit 74455 October 2020)

## Techniques Used
- T0828: Loss of Productivity and Revenue
- T0866: Exploitation of Remote Services
- T0867: Lateral Tool Transfer


---

# S0608: Conficker

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0608  
**Aliases:** Conficker, Kido, Downadup  
**Platforms:** Windows  

## Description
[Conficker](https://attack.mitre.org/software/S0608) is a computer worm first detected in October 2008 that targeted Microsoft Windows using the MS08-067 Windows vulnerability to spread.(Citation: SANS Conficker) In 2016, a variant of [Conficker](https://attack.mitre.org/software/S0608) made its way on computers and removable disk drives belonging to a nuclear power plant.(Citation: Conficker Nuclear Power Plant)

## Techniques Used
- T0826: Loss of Availability
- T0828: Loss of Productivity and Revenue
- T0847: Replication Through Removable Media


---

# S0372: LockerGoga

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0372  
**Aliases:** LockerGoga  
**Platforms:** Windows  

## Description
[LockerGoga](https://attack.mitre.org/software/S0372) is ransomware that was first reported in January 2019, and has been tied to various attacks on European companies, including industrial and manufacturing firms.(Citation: Unit42 LockerGoga 2019)(Citation: CarbonBlack LockerGoga 2019)

## Techniques Used
- T0827: Loss of Control
- T0828: Loss of Productivity and Revenue
- T0829: Loss of View
- T1695.002: Ethernet
- T1695.003: Wi-Fi


---

# S1010: VPNFilter

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1010  
**Aliases:** VPNFilter  
**Platforms:** Network Devices, Linux  

## Description
[VPNFilter](https://attack.mitre.org/software/S1010) is a multi-stage, modular platform with versatile capabilities to support both intelligence-collection and destructive cyber attack operations. [VPNFilter](https://attack.mitre.org/software/S1010) modules such as its packet sniffer ('ps') can collect traffic that passes through an infected device, allowing the theft of website credentials and monitoring of Modbus SCADA protocols. (Citation: William Largent June 2018) (Citation: Carl Hurd March 2019) [VPNFilter](https://attack.mitre.org/software/S1010) was assessed to be replaced by [Sandworm Team](https://attack.mitre.org/groups/G0034) with [Cyclops Blink](https://attack.mitre.org/software/S0687) starting in 2019.(Citation: NCSC CISA Cyclops Blink Advisory February 2022)

## Techniques Used
- T0830: Adversary-in-the-Middle
- T0842: Network Sniffing


---

# S0038: Duqu

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0038  
**Aliases:** Duqu  
**Platforms:** Windows  

## Description
[Duqu](https://attack.mitre.org/software/S0038) is a malware platform that uses a modular approach to extend functionality after deployment within a target network. (Citation: Symantec W32.Duqu)

## Techniques Used
- T0811: Data from Information Repositories
- T0882: Theft of Operational Information
- T0893: Data from Local System


---

# S1072: Industroyer2

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1072  
**Aliases:** Industroyer2  
**Platforms:** Field Controller/RTU/PLC/IED, Engineering Workstation  

## Description
[Industroyer2](https://attack.mitre.org/software/S1072) is a compiled and static piece of malware that has the ability to communicate over the IEC-104 protocol. It is similar to the IEC-104 module found in [Industroyer](https://attack.mitre.org/software/S0604). Security researchers assess that [Industroyer2](https://attack.mitre.org/software/S1072) was designed to cause impact to high-voltage electrical substations. The initial [Industroyer2](https://attack.mitre.org/software/S1072) sample was compiled on 03/23/2022 and scheduled to execute on 04/08/2022, however it was discovered before deploying, resulting in no impact.(Citation: Industroyer2 Blackhat ESET)

## Techniques Used
- T0801: Monitor Process State
- T0802: Automated Collection
- T0806: Brute Force I/O
- T0836: Modify Parameter
- T0881: Service Stop
- T0888: Remote System Information Discovery
- T1692.001: Command Message


---

# S0366: WannaCry

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0366  
**Aliases:** WannaCry, WanaCry, WanaCrypt, WanaCrypt0r, WCry  
**Platforms:** Windows  

## Description
[WannaCry](https://attack.mitre.org/software/S0366) is ransomware that was first seen in a global attack during May 2017, which affected more than 150 countries. It contains worm-like features to spread itself across a computer network using the SMBv1 exploit EternalBlue.(Citation: LogRhythm WannaCry)(Citation: US-CERT WannaCry 2017)(Citation: Washington Post WannaCry 2017)(Citation: FireEye WannaCry 2017)

## Techniques Used
- T0866: Exploitation of Remote Services
- T0867: Lateral Tool Transfer


---

# S1009: Triton

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1009  
**Aliases:** Triton, TRISIS, HatMan  

## Description
[Triton](https://attack.mitre.org/software/S1009) is an attack framework built to interact with Triconex Safety Instrumented System (SIS) controllers.(Citation: Blake Johnson, Dan Caban, Marina Krotofil, Dan Scali, Nathan Brubaker, Christopher Glyer December 2017)(Citation: Dragos December 2017)(Citation: DHS CISA February 2019)(Citation: Schneider Electric January 2018)(Citation: Julian Gutmanis March 2019)(Citation: Schneider December 2018)(Citation: Jos Wetzels January 2018)

## Techniques Used
- T0820: Exploitation for Evasion
- T0821: Modify Controller Tasking
- T0834: Native API
- T0843: Program Download
- T0845: Program Upload
- T0846.002: Broadcast Discovery
- T0849: Masquerading
- T0853: Scripting
- T0858: Change Operating Mode
- T0868: Detect Operating Mode
- T0869: Standard Application Layer Protocol
- T0871: Execution through API
- T0872: Indicator Removal on Host
- T0874: Hooking
- T0880: Loss of Safety
- T0885: Commonly Used Port
- T0890: Exploitation for Privilege Escalation
- T1693.001: System Firmware


---

# S1157: Fuxnet

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1157  
**Aliases:** Fuxnet  
**Platforms:** Input/Output Server, Control Server  

## Description
[Fuxnet](https://attack.mitre.org/software/S1157) is malware designed to impact the industrial network infrastructure managing control system sensors for utility operations in Moscow. [Fuxnet](https://attack.mitre.org/software/S1157) is linked to an entity referred to as the Blackjack hacking group, which is assessed to be linked to Ukrainian intelligence services.(Citation: Claroty Fuxnet 2024)

## Techniques Used
- T0806: Brute Force I/O
- T0809: Data Destruction
- T0814: Denial of Service
- T0822: External Remote Services
- T0829: Loss of View
- T0883: Internet Accessible Device


---

# S0446: Ryuk

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0446  
**Aliases:** Ryuk  
**Platforms:** Windows  

## Description
[Ryuk](https://attack.mitre.org/software/S0446) is a ransomware designed to target enterprise environments that has been used in attacks since at least 2018. [Ryuk](https://attack.mitre.org/software/S0446) shares code similarities with Hermes ransomware.(Citation: CrowdStrike Ryuk January 2019)(Citation: FireEye Ryuk and Trickbot January 2019)(Citation: FireEye FIN6 Apr 2019)

## Techniques Used
- T0828: Loss of Productivity and Revenue


---

# S1000: ACAD/Medre.A

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1000  
**Aliases:** ACAD/Medre.A  

## Description
[ACAD/Medre.A](https://attack.mitre.org/software/S1000) is a worm that steals operational information. The worm collects AutoCAD files with drawings. [ACAD/Medre.A](https://attack.mitre.org/software/S1000) has the capability to be used for industrial espionage.(Citation: ESET)

## Techniques Used
- T0882: Theft of Operational Information
- T0893: Data from Local System


---

# S0496: REvil

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0496  
**Aliases:** REvil, Sodin, Sodinokibi  
**Platforms:** Windows  

## Description
[REvil](https://attack.mitre.org/software/S0496) is a ransomware family that has been linked to the [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) group and operated as ransomware-as-a-service (RaaS) since at least April 2019. [REvil](https://attack.mitre.org/software/S0496), which as been used against organizations in the manufacturing, transportation, and electric sectors, is highly configurable and shares code similarities with the GandCrab RaaS.(Citation: Secureworks REvil September 2019)(Citation: Intel 471 REvil March 2020)(Citation: Group IB Ransomware May 2020)

## Techniques Used
- T0828: Loss of Productivity and Revenue
- T0849: Masquerading
- T0853: Scripting
- T0863: User Execution
- T0869: Standard Application Layer Protocol
- T0881: Service Stop
- T0882: Theft of Operational Information
- T0886: Remote Services


---

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


---

# S1045: INCONTROLLER

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1045  
**Aliases:** INCONTROLLER, PIPEDREAM  
**Platforms:** Engineering Workstation, Field Controller/RTU/PLC/IED, Safety Instrumented System/Protection Relay, Windows  

## Description
[INCONTROLLER](https://attack.mitre.org/software/S1045) is custom malware that includes multiple modules tailored towards ICS devices and technologies, including Schneider Electric and Omron PLCs as well as OPC UA, Modbus, and CODESYS protocols. [INCONTROLLER](https://attack.mitre.org/software/S1045) has the ability to discover specific devices, download logic on the devices, and exploit platform-specific vulnerabilities. As of September 2022, some security researchers assessed [INCONTROLLER](https://attack.mitre.org/software/S1045) was developed by CHERNOVITE.(Citation: CISA-AA22-103A)(Citation: Brubaker-Incontroller)(Citation: Dragos-Pipedream)(Citation: Schneider-Incontroller)(Citation: Wylie-22)

## Techniques Used
- T0809: Data Destruction
- T0836: Modify Parameter
- T0842: Network Sniffing
- T0843: Program Download
- T0843.001: Download All
- T0845: Program Upload
- T0846: Remote System Discovery
- T0846.001: Port Scan
- T0846.003: Multicast Discovery
- T0858: Change Operating Mode
- T0859: Valid Accounts
- T0861: Point & Tag Identification
- T0867: Lateral Tool Transfer
- T0869: Standard Application Layer Protocol
- T0884: Connection Proxy
- T0886: Remote Services
- T0888: Remote System Information Discovery
- T0890: Exploitation for Privilege Escalation
- T1692.001: Command Message
- T1694.002: Hardcoded Credentials


---

# S0607: KillDisk

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0607  
**Aliases:** KillDisk, Win32/KillDisk.NBI, Win32/KillDisk.NBH, Win32/KillDisk.NBD, Win32/KillDisk.NBC, Win32/KillDisk.NBB  
**Platforms:** Linux, Windows  

## Description
[KillDisk](https://attack.mitre.org/software/S0607) is a disk-wiping tool designed to overwrite files with random data to render the OS unbootable. It was first observed as a component of [BlackEnergy](https://attack.mitre.org/software/S0089) malware during cyber attacks against Ukraine in 2015. [KillDisk](https://attack.mitre.org/software/S0607) has since evolved into stand-alone malware used by a variety of threat actors against additional targets in Europe and Latin America; in 2016 a ransomware component was also incorporated into some [KillDisk](https://attack.mitre.org/software/S0607) variants.(Citation: KillDisk Ransomware)(Citation: ESEST Black Energy Jan 2016)(Citation: Trend Micro KillDisk 1)(Citation: Trend Micro KillDisk 2)

## Techniques Used
- T0809: Data Destruction
- T0829: Loss of View
- T0872: Indicator Removal on Host
- T0881: Service Stop


---

# S0604: Industroyer

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0604  
**Aliases:** Industroyer, CRASHOVERRIDE, Win32/Industroyer  
**Platforms:** Windows  

## Description
[Industroyer](https://attack.mitre.org/software/S0604) is a sophisticated malware framework designed to cause an impact to the working processes of Industrial Control Systems (ICS), specifically components used in electrical substations.(Citation: ESET Industroyer) [Industroyer](https://attack.mitre.org/software/S0604) was used in the attacks on the Ukrainian power grid in December 2016.(Citation: Dragos Crashoverride 2017) This is the first publicly known malware specifically designed to target and impact operations in the electric grid.(Citation: Dragos Crashoverride 2018)

## Techniques Used
- T0800: Activate Firmware Update Mode
- T0801: Monitor Process State
- T0802: Automated Collection
- T0806: Brute Force I/O
- T0807: Command-Line Interface
- T0809: Data Destruction
- T0813: Denial of Control
- T0814: Denial of Service
- T0815: Denial of View
- T0816: Device Restart/Shutdown
- T0827: Loss of Control
- T0829: Loss of View
- T0831: Manipulation of Control
- T0832: Manipulation of View
- T0837: Loss of Protection
- T0840: Network Connection Enumeration
- T0846: Remote System Discovery
- T0846.001: Port Scan
- T0881: Service Stop
- T0884: Connection Proxy
- T0888: Remote System Information Discovery
- T1691.001: Command Message
- T1691.002: Reporting Message
- T1692.001: Command Message
- T1695.001: Serial COM


---

# S0143: Flame

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0143  
**Aliases:** Flame, Flamer, sKyWIper  
**Platforms:** Windows  

## Description
[Flame](https://attack.mitre.org/software/S0143) is a sophisticated toolkit that has been used to collect information since at least 2010, largely targeting Middle East countries. (Citation: Kaspersky Flame)

## Techniques Used
- T0882: Theft of Operational Information
- T0893: Data from Local System


---

# T0881: Service Stop


**ATT&CK ID:** T0881  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0881  

## Description
Adversaries may stop or disable services on a system to render those services unavailable to legitimate users. Stopping critical services can inhibit or stop response to an incident or aid in the adversary's overall objectives to cause damage to the environment. (Citation: Enterprise ATT&CK)  Services may not allow for modification of their data stores while running. Adversaries may stop services in order to conduct Data Destruction. (Citation: Enterprise ATT&CK)

## Mitigations
- M0918: User Account Management
- M0922: Restrict File and Directory Permissions
- M0924: Restrict Registry Permissions
- M0930: Network Segmentation

## Known Software Using This Technique
- S0605: EKANS
- S0604: Industroyer
- S1072: Industroyer2
- S0607: KillDisk
- S0496: REvil


---

# T0836: Modify Parameter


**ATT&CK ID:** T0836  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impair Process Control  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0836  

## Description
Adversaries may modify parameters used to instruct industrial control system devices. These devices operate via programs that dictate how and when to perform actions based on such parameters. Such parameters can determine the extent to which an action is performed and may specify additional options. For example, a program on a control system device dictating motor processes may take a parameter defining the total number of seconds to run that motor.      

An adversary can potentially modify these parameters to produce an outcome outside of what was intended by the operators. By modifying system and process critical parameters, the adversary may cause [Impact](https://attack.mitre.org/tactics/TA0105) to equipment and/or control processes. Modified parameters may be turned into dangerous, out-of-bounds, or unexpected values from typical operations. For example, specifying that a process run for more or less time than it should, or dictating an unusually high, low, or invalid value as a parameter.

## Mitigations
- M0800: Authorization Enforcement
- M0804: Human User Authentication
- M0818: Validate Program Inputs
- M0947: Audit

## Known Software Using This Technique
- S1165: FrostyGoop
- S1045: INCONTROLLER
- S1072: Industroyer2
- S0603: Stuxnet


---

# T0821: Modify Controller Tasking


**ATT&CK ID:** T0821  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Execution  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0821  

## Description
Adversaries may modify the tasking of a controller to allow for the execution of their own programs. This can allow an adversary to manipulate the execution flow and behavior of a controller. 

According to 61131-3, the association of a Task with a Program Organization Unit (POU) defines a task association. (Citation: IEC February 2013) An adversary may modify these associations or create new ones to manipulate the execution flow of a controller. Modification of controller tasking can be accomplished using a Program Download in addition to other types of program modification such as online edit and program append.

Tasks have properties, such as interval, frequency and priority to meet the requirements of program execution. Some controller vendors implement tasks with implicit, pre-defined properties whereas others allow for these properties to be formulated explicitly. An adversary may associate their program with tasks that have a higher priority or execute associated programs more frequently. For instance, to ensure cyclic execution of their program on a Siemens controller, an adversary may add their program to the task, Organization Block 1 (OB1).

## Mitigations
- M0800: Authorization Enforcement
- M0804: Human User Authentication
- M0945: Code Signing
- M0947: Audit

## Known Software Using This Technique
- S1006: PLC-Blaster
- S0603: Stuxnet
- S1009: Triton


---

# T0887: Wireless Sniffing


**ATT&CK ID:** T0887  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Discovery, Collection  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0887  

## Description
Adversaries may seek to capture radio frequency (RF) communication used for remote control and reporting in distributed environments. RF communication frequencies vary between 3 kHz to 300 GHz, although are commonly between 300 MHz to 6 GHz. (Citation: Candell, R., Hany, M., Lee, K. B., Liu,Y., Quimby, J., Remley, K. April 2018)  The wavelength and frequency of the signal affect how the signal propagates through open air, obstacles (e.g. walls and trees) and the type of radio required to capture them. These characteristics are often standardized in the protocol and hardware and may have an effect on how the signal is captured. Some examples of wireless protocols that may be found in cyber-physical environments are: WirelessHART, Zigbee, WIA-FA, and 700 MHz Public Safety Spectrum. 

Adversaries may capture RF communications by using specialized hardware, such as software defined radio (SDR), handheld radio, or a computer with radio demodulator tuned to the communication frequency. (Citation: Bastille April 2017) Information transmitted over a wireless medium may be captured in-transit whether the sniffing device is the intended destination or not. This technique may be particularly useful to an adversary when the communications are not encrypted. (Citation: Gallagher, S. April 2017) 

In the 2017 Dallas Siren incident, it is suspected that adversaries likely captured wireless command message broadcasts on a 700 MHz frequency during a regular test of the system. These messages were later replayed to trigger the alarm systems. (Citation: Gallagher, S. April 2017)

## Mitigations
- M0806: Minimize Wireless Signal Propagation
- M0808: Encrypt Network Traffic


---

# T0829: Loss of View


**ATT&CK ID:** T0829  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impact  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0829  

## Description
Adversaries may cause a sustained or permanent loss of view where the ICS equipment will require local, hands-on operator intervention; for instance, a restart or manual operation. By causing a sustained reporting or visibility loss, the adversary can effectively hide the present state of operations. This loss of view can occur without affecting the physical processes themselves. (Citation: Corero) (Citation: Michael J. Assante and Robert M. Lee) (Citation: Tyson Macaulay)

## Mitigations
- M0810: Out-of-Band Communications Channel
- M0811: Redundancy of Service
- M0953: Data Backup

## Known Software Using This Technique
- S1157: Fuxnet
- S0604: Industroyer
- S0607: KillDisk
- S0372: LockerGoga


---

# T1691.001: Command Message

**Parent technique:** T1691
**ATT&CK ID:** T1691.001  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Reference:** https://attack.mitre.org/techniques/T1691/001  

## Description
Adversaries may block a command message from reaching its intended target to prevent command execution. In OT networks, command messages are sent to provide instructions to control system devices. A blocked command message can inhibit response functions from correcting a disruption or unsafe condition.(Citation: Bonnie Zhu, Anthony Joseph, Shankar Sastry 2011)(Citation: Electricity Information Sharing and Analysis Center; SANS Industrial Control Systems March 2016)

## Mitigations
- M0807: Network Allowlists
- M0810: Out-of-Band Communications Channel
- M0814: Static Network Configuration

## Known Software Using This Technique
- S0604: Industroyer


---

# T0800: Activate Firmware Update Mode


**ATT&CK ID:** T0800  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0800  

## Description
Adversaries may activate firmware update mode on devices to prevent expected response functions from engaging in reaction to an emergency or process malfunction. For example, devices such as protection relays may have an operation mode designed for firmware installation. This mode may halt process monitoring and related functions to allow new firmware to be loaded. A device left in update mode may be placed in an inactive holding state if no firmware is provided to it. By entering and leaving a device in this mode, the adversary may deny its usual functionalities.

## Mitigations
- M0800: Authorization Enforcement
- M0801: Access Management
- M0802: Communication Authenticity
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic

## Known Software Using This Technique
- S0604: Industroyer


---

# T0831: Manipulation of Control


**ATT&CK ID:** T0831  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impact  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0831  

## Description
Adversaries may manipulate physical process control within the industrial environment. Methods of manipulating control can include changes to set point values, tags, or other parameters. Adversaries may manipulate control systems devices or possibly leverage their own, to communicate with and command physical control processes. The duration of manipulation may be temporary or longer sustained, depending on operator detection.   

Methods of Manipulation of Control include: 

* Man-in-the-middle  
* Spoof command message 
* Changing setpoints  

A Polish student used a remote controller device to interface with the Lodz city tram system in Poland. (Citation: John Bill May 2017) (Citation: Shelley Smith February 2008) (Citation: Bruce Schneier January 2008) Using this remote, the student was able to capture and replay legitimate tram signals. As a consequence, four trams were derailed and twelve people injured due to resulting emergency stops. (Citation: Shelley Smith February 2008) The track controlling commands issued may have also resulted in tram collisions, a further risk to those on board and nearby the areas of impact. (Citation: Bruce Schneier January 2008)

## Mitigations
- M0802: Communication Authenticity
- M0810: Out-of-Band Communications Channel
- M0953: Data Backup

## Known Software Using This Technique
- S0604: Industroyer
- S0603: Stuxnet


---

# T0814: Denial of Service


**ATT&CK ID:** T0814  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0814  

## Description
Adversaries may perform Denial-of-Service (DoS) attacks to disrupt expected device functionality. Examples of DoS attacks include overwhelming the target device with a high volume of requests in a short time period and sending the target device a request it does not know how to handle. Disrupting device state may temporarily render it unresponsive, possibly lasting until a reboot can occur. When placed in this state, devices may be unable to send and receive requests, and may not perform expected response functions in reaction to other events in the environment. 

Some ICS devices are particularly sensitive to DoS events, and may become unresponsive in reaction to even a simple ping sweep. Adversaries may also attempt to execute a Permanent Denial-of-Service (PDoS) against certain devices, such as in the case of the BrickerBot malware. (Citation: ICS-CERT April 2017) 

Adversaries may exploit a software vulnerability to cause a denial of service by taking advantage of a programming error in a program, service, or within the operating system software or kernel itself to execute adversary-controlled code. Vulnerabilities may exist in software that can be used to cause a denial of service condition. 

Adversaries may have prior knowledge about industrial protocols or control devices used in the environment through [Remote System Information Discovery](https://attack.mitre.org/techniques/T0888). There are examples of adversaries remotely causing a [Device Restart/Shutdown](https://attack.mitre.org/techniques/T0816) by exploiting a vulnerability that induces uncontrolled resource consumption. (Citation: ICS-CERT August 2018) (Citation: Common Weakness Enumeration January 2019) (Citation: MITRE March 2018)

## Mitigations
- M0815: Watchdog Timers

## Known Software Using This Technique
- S0093: Backdoor.Oldrea
- S1157: Fuxnet
- S0604: Industroyer
- S1006: PLC-Blaster


---

# T0894: System Binary Proxy Execution


**ATT&CK ID:** T0894  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Evasion  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0894  

## Description
Adversaries may bypass process and/or signature-based defenses by proxying execution of malicious content with signed, or otherwise trusted, binaries. Binaries used in this technique are often Microsoft-signed files, indicating that they have been either downloaded from Microsoft or are already native in the operating system. (Citation: LOLBAS Project) Binaries signed with trusted digital certificates can typically execute on Windows systems protected by digital signature validation. Several Microsoft signed binaries that are default on Windows installations can be used to proxy execution of other files or commands. Similarly, on Linux systems adversaries may abuse trusted binaries such as split to proxy execution of malicious commands. (Citation: split man page)(Citation: GTFO split)

Adversaries may abuse application binaries installed on a system for proxy execution of malicious code or domain-specific commands. These commands could be used to target local resources on the device or networked devices within the environment through defined APIs ([Execution through API](https://attack.mitre.org/techniques/T0871)) or application-specific programming languages (e.g., MicroSCADA SCIL). Application binaries may be signed by the developer or generally trusted by the operators, analysts, and monitoring tools accustomed to the environment. These applications may be developed and/or directly provided by the device vendor to enable configuration, management, and operation of their devices without many alternatives. 

Adversaries may seek to target these trusted application binaries to execute or send commands without the development of custom malware. For example, adversaries may target a SCADA server binary which has the existing ability to send commands to substation devices, such as through IEC 104 command messages. Proxy execution may still require the development of custom tools to hook into the application binary’s execution.

## Mitigations
- M0938: Execution Prevention


---

# T0807: Command-Line Interface


**ATT&CK ID:** T0807  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Execution  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0807  

## Description
Adversaries may utilize command-line interfaces (CLIs) to interact with systems and execute commands. CLIs provide a means of interacting with computer systems and are a common feature across many types of platforms and devices within control systems environments. (Citation: Enterprise ATT&CK January 2018) Adversaries may also use CLIs to install and run new software, including malicious tools that may be installed over the course of an operation.

CLIs are typically accessed locally, but can also be exposed via services, such as SSH, Telnet, and RDP.  Commands that are executed in the CLI execute with the current permissions level of the process running the terminal emulator, unless the command specifies a change in permissions context. Many controllers have CLI interfaces for management purposes.

## Mitigations
- M0938: Execution Prevention
- M0942: Disable or Remove Feature or Program

## Known Threat Groups Using This Technique
- G0034: Sandworm Team

## Known Software Using This Technique
- S1165: FrostyGoop
- S0604: Industroyer
- S0603: Stuxnet


---

# T0861: Point & Tag Identification


**ATT&CK ID:** T0861  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Collection  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0861  

## Description
Adversaries may collect point and tag values to gain a more comprehensive understanding of the process environment. Points may be values such as inputs, memory locations, outputs or other process specific variables. (Citation: Dennis L. Sloatman September 2016) Tags are the identifiers given to points for operator convenience. 

Collecting such tags provides valuable context to environmental points and enables an adversary to map inputs, outputs, and other values to their control processes. Understanding the points being collected may inform an adversary on which processes and values to keep track of over the course of an operation.

## Mitigations
- M0800: Authorization Enforcement
- M0801: Access Management
- M0802: Communication Authenticity
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic

## Known Software Using This Technique
- S0093: Backdoor.Oldrea
- S1045: INCONTROLLER


---

# T0816: Device Restart/Shutdown


**ATT&CK ID:** T0816  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0816  

## Description
Adversaries may forcibly restart or shutdown a device in an ICS environment to disrupt and potentially negatively impact physical processes. Methods of device restart and shutdown exist in some devices as built-in, standard functionalities. These functionalities can be executed using interactive device web interfaces, CLIs, and network protocol commands.

Unexpected restart or shutdown of control system devices may prevent expected response functions happening during critical states.

A device restart can also be a sign of malicious device modifications, as many updates require a shutdown in order to take effect.

## Mitigations
- M0800: Authorization Enforcement
- M0801: Access Management
- M0802: Communication Authenticity
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic
- M0942: Disable or Remove Feature or Program

## Known Software Using This Technique
- S0604: Industroyer


---

# T0863: User Execution


**ATT&CK ID:** T0863  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Execution  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0863  

## Description
Adversaries may rely on a targeted organizations user interaction for the execution of malicious code. User interaction may consist of installing applications, opening email attachments, or granting higher permissions to documents. 

Adversaries may embed malicious code or visual basic code into files such as Microsoft Word and Excel documents or software installers. (Citation: Booz Allen Hamilton) Execution of this code requires that the user enable scripting or write access within the document. Embedded code may not always be noticeable to the user especially in cases of trojanized software. (Citation: Daavid Hentunen, Antti Tikkanen June 2014) 

A Chinese spearphishing campaign running from December 9, 2011 through February 29, 2012 delivered malware through spearphishing attachments which required user action to achieve execution. (Citation: CISA AA21-201A Pipeline Intrusion July 2021)

## Mitigations
- M0917: User Training
- M0921: Restrict Web-Based Content
- M0931: Network Intrusion Prevention
- M0938: Execution Prevention
- M0945: Code Signing
- M0949: Antivirus/Antimalware

## Known Software Using This Technique
- S0093: Backdoor.Oldrea
- S0606: Bad Rabbit
- S0496: REvil
- S0603: Stuxnet


---

# T0860: Wireless Compromise


**ATT&CK ID:** T0860  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Initial Access  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0860  

## Description
Adversaries may perform wireless compromise as a method of gaining communications and unauthorized access to a wireless network. Access to a wireless network may be gained through the compromise of a wireless device. (Citation: Alexander Bolshev, Gleb Cherbov July 2014) (Citation: Alexander Bolshev March 2014) Adversaries may also utilize radios and other wireless communication devices on the same frequency as the wireless network. Wireless compromise can be done as an initial access vector from a remote distance. 

A Polish student used a modified TV remote controller to gain access to and control over the Lodz city tram system in Poland. (Citation: John Bill May 2017) (Citation: Shelley Smith February 2008) The remote controller device allowed the student to interface with the trams network to modify track settings and override operator control. The adversary may have accomplished this by aligning the controller to the frequency and amplitude of IR control protocol signals. (Citation: Bruce Schneier January 2008) The controller then enabled initial access to the network, allowing the capture and replay of tram signals. (Citation: John Bill May 2017)

## Mitigations
- M0802: Communication Authenticity
- M0806: Minimize Wireless Signal Propagation
- M0808: Encrypt Network Traffic
- M0813: Software Process and Device Authentication


---

# T0858: Change Operating Mode


**ATT&CK ID:** T0858  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Execution, Evasion  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0858  

## Description
Adversaries may change the operating mode of a controller to gain additional access to engineering functions such as Program Download.   Programmable controllers typically have several modes of operation that control the state of the user program and control access to the controllers API. Operating modes can be physically selected using a key switch on the face of the controller but may also be selected with calls to the controllers API. Operating modes and the mechanisms by which they are selected often vary by vendor and product line. Some commonly implemented operating modes are described below:  

* Program - This mode must be enabled before changes can be made to a devices program. This allows program uploads and downloads between the device and an engineering workstation. Often the PLCs logic Is halted, and all outputs may be forced off. (Citation: N.A. October 2017)  
* Run - Execution of the devices program occurs in this mode. Input and output (values, points, tags, elements, etc.) are monitored and used according to the programs logic. [Program Upload](https://attack.mitre.org/techniques/T0845) and [Program Download](https://attack.mitre.org/techniques/T0843) are disabled while in this mode. (Citation: Omron) (Citation: Machine Information Systems 2007)  (Citation: N.A. October 2017) (Citation: PLCgurus 2021)   
* Remote - Allows for remote changes to a PLCs operation mode. (Citation: PLCgurus 2021)    
* Stop - The PLC and program is stopped, while in this mode, outputs are forced off. (Citation: Machine Information Systems 2007)   
* Reset - Conditions on the PLC are reset to their original states. Warm resets may retain some memory while cold resets will reset all I/O and data registers. (Citation: Machine Information Systems 2007)   
* Test / Monitor mode - Similar to run mode, I/O is processed, although this mode allows for monitoring, force set, resets, and more generally tuning or debugging of the system. Often monitor mode may be used as a trial for initialization. (Citation: Omron)

## Mitigations
- M0800: Authorization Enforcement
- M0801: Access Management
- M0802: Communication Authenticity
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation

## Known Software Using This Technique
- S1045: INCONTROLLER
- S1006: PLC-Blaster
- S1009: Triton


---

# T0878: Alarm Suppression


**ATT&CK ID:** T0878  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0878  

## Description
Adversaries may target protection function alarms to prevent them from notifying operators of critical conditions. Alarm messages may be a part of an overall reporting system and of particular interest for adversaries. Disruption of the alarm system does not imply the disruption of the reporting system as a whole.

A Secura presentation on targeting OT notes a dual fold goal for adversaries attempting alarm suppression: prevent outgoing alarms from being raised and prevent incoming alarms from being responded to. (Citation: Jos Wetzels, Marina Krotofil 2019) The method of suppression may greatly depend on the type of alarm in question:  

* An alarm raised by a protocol message 
* An alarm signaled with I/O 
* An alarm bit set in a flag (and read) 

In ICS environments, the adversary may have to suppress or contend with multiple alarms and/or alarm propagation to achieve a specific goal to evade detection or prevent intended responses from occurring. (Citation: Jos Wetzels, Marina Krotofil 2019)  Methods of suppression may involve tampering or altering device displays and logs, modifying in memory code to fixed values, or even tampering with assembly level instruction code.

## Mitigations
- M0807: Network Allowlists
- M0810: Out-of-Band Communications Channel
- M0814: Static Network Configuration
- M0930: Network Segmentation


---

# T0868: Detect Operating Mode


**ATT&CK ID:** T0868  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Collection  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0868  

## Description
Adversaries may gather information about a PLCs or controllers current operating mode. Operating modes dictate what change or maintenance functions can be manipulated and are often controlled by a key switch on the PLC (e.g.,  run, prog [program], and remote). Knowledge of these states may be valuable to an adversary to determine if they are able to reprogram the PLC. Operating modes and the mechanisms by which they are selected often vary by vendor and product line. Some commonly implemented operating modes are described below:  

* Program - This mode must be enabled before changes can be made to a devices program. This allows program uploads and downloads between the device and an engineering workstation. Often the PLCs logic Is halted, and all outputs may be forced off. (Citation: N.A. October 2017)  
* Run - Execution of the devices program occurs in this mode. Input and output (values, points, tags, elements, etc.) are monitored and used according to the programs logic.[Program Upload](https://attack.mitre.org/techniques/T0845) and [Program Download](https://attack.mitre.org/techniques/T0843) are disabled while in this mode. (Citation: Omron) (Citation: Machine Information Systems 2007)  (Citation: N.A. October 2017) (Citation: PLCgurus 2021)   
* Remote - Allows for remote changes to a PLCs operation mode. (Citation: PLCgurus 2021)    
* Stop - The PLC and program is stopped, while in this mode, outputs are forced off. (Citation: Machine Information Systems 2007)   
* Reset - Conditions on the PLC are reset to their original states. Warm resets may retain some memory while cold resets will reset all I/O and data registers. (Citation: Machine Information Systems 2007)   
* Test / Monitor mode - Similar to run mode, I/O is processed, although this mode allows for monitoring, force set, resets, and more generally tuning or debugging of the system. Often monitor mode may be used as a trial for initialization. (Citation: Omron)

## Mitigations
- M0800: Authorization Enforcement
- M0801: Access Management
- M0802: Communication Authenticity
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic

## Known Software Using This Technique
- S1009: Triton


---

# T0837: Loss of Protection


**ATT&CK ID:** T0837  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impact  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0837  

## Description
Adversaries may compromise protective system functions designed to prevent the effects of faults and abnormal conditions. This can result in equipment damage, prolonged process disruptions and hazards to personnel. 

Many faults and abnormal conditions in process control happen too quickly for a human operator to react to. Speed is critical in correcting these conditions to limit serious impacts such as Loss of Control and Property Damage. 

Adversaries may target and disable protective system functions as a prerequisite to subsequent attack execution or to allow for future faults and abnormal conditions to go unchecked. Detection of a Loss of Protection by operators can result in the shutdown of a process due to strict policies regarding protection systems. This can cause a Loss of Productivity and Revenue and may meet the technical goals of adversaries seeking to cause process disruptions.

## Known Software Using This Technique
- S0604: Industroyer


---

# T0801: Monitor Process State


**ATT&CK ID:** T0801  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Collection  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0801  

## Description
Adversaries may gather information about the physical process state. This information may be used to gain more information about the process itself or used as a trigger for malicious actions. The sources of process state information may vary such as, OPC tags, historian data, specific PLC block information, or network traffic.

## Mitigations
- M0816: Mitigation Limited or Not Effective

## Known Software Using This Technique
- S1165: FrostyGoop
- S0604: Industroyer
- S1072: Industroyer2
- S0603: Stuxnet


---

# T0853: Scripting


**ATT&CK ID:** T0853  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Execution  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0853  

## Description
Adversaries may use scripting languages to execute arbitrary code in the form of a pre-written script or in the form of user-supplied code to an interpreter. Scripting languages are programming languages that differ from compiled languages, in that scripting languages use an interpreter, instead of a compiler. These interpreters read and compile part of the source code just before it is executed, as opposed to compilers, which compile each and every line of code to an executable file. Scripting allows software developers to run their code on any system where the interpreter exists. This way, they can distribute one package, instead of precompiling executables for many different systems. Scripting languages, such as Python, have their interpreters shipped as a default with many Linux distributions. 

In addition to being a useful tool for developers and administrators, scripting language interpreters may be abused by the adversary to execute code in the target environment. Due to the nature of scripting languages, this allows for weaponized code to be deployed to a target easily, and leaves open the possibility of on-the-fly scripting to perform a task.

## Mitigations
- M0938: Execution Prevention
- M0942: Disable or Remove Feature or Program
- M0948: Application Isolation and Sandboxing

## Known Threat Groups Using This Technique
- G0064: APT33
- G0049: OilRig

## Known Software Using This Technique
- S0496: REvil
- S1009: Triton


---

# T0888: Remote System Information Discovery


**ATT&CK ID:** T0888  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Discovery  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0888  

## Description
An adversary may attempt to get detailed information about remote systems and their peripherals, such as make/model, role, and configuration. Adversaries may use information from Remote System Information Discovery to aid in targeting and shaping follow-on behaviors. For example, the system's operational role and model information can dictate whether it is a relevant target for the adversary's operational objectives. In addition, the system's configuration may be used to scope subsequent technique usage. 

Requests for system information are typically implemented using automation and management protocols and are often automatically requested by vendor software during normal operation. This information may be used to tailor management actions, such as program download and system or module firmware. An adversary may leverage this same information by issuing calls directly to the system's API.

## Mitigations
- M0814: Static Network Configuration

## Known Software Using This Technique
- S0093: Backdoor.Oldrea
- S1045: INCONTROLLER
- S0604: Industroyer
- S1072: Industroyer2
- S0603: Stuxnet


---

# T0845: Program Upload


**ATT&CK ID:** T0845  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Collection  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0845  

## Description
Adversaries may attempt to upload a program from a PLC to gather information about an industrial process. Uploading a program may allow them to acquire and study the underlying logic. Methods of program upload include vendor software, which enables the user to upload and read a program running on a PLC. This software can be used to upload the target program to a workstation, jump box, or an interfacing device.

## Mitigations
- M0800: Authorization Enforcement
- M0801: Access Management
- M0802: Communication Authenticity
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic

## Known Software Using This Technique
- S1045: INCONTROLLER
- S1009: Triton


---

# T0819: Exploit Public-Facing Application


**ATT&CK ID:** T0819  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Initial Access  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0819  

## Description
Adversaries may leverage weaknesses to exploit internet-facing software for initial access into an industrial network. Internet-facing software may be user applications, underlying networking implementations, an assets operating system, weak defenses, etc. Targets of this technique may be intentionally exposed for the purpose of remote management and visibility.

An adversary may seek to target public-facing applications as they may provide direct access into an ICS environment or the ability to move into the ICS network. Publicly exposed applications may be found through online tools that scan the internet for open ports and services. Version numbers for the exposed application may provide adversaries an ability to target specific known vulnerabilities. Exposed control protocol or remote access ports found in Commonly Used Port may be of interest by adversaries.

## Mitigations
- M0916: Vulnerability Scanning
- M0926: Privileged Account Management
- M0930: Network Segmentation
- M0948: Application Isolation and Sandboxing
- M0950: Exploit Protection
- M0951: Update Software

## Known Threat Groups Using This Technique
- G0034: Sandworm Team


---

# T1691: Block Operational Technology Message


**ATT&CK ID:** T1691  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Reference:** https://attack.mitre.org/techniques/T1691  

## Description
Adversaries may block messages between systems and devices in an OT/ICS environment to disrupt processes. Messages typically fall into two categories: (1) reporting messages that contain telemetry data about the current state of systems, devices, and processes and (2) command messages that contain instructions to control systems, devices, and processes. Both types of messages are critical for the proper functioning of industrial control processes and failure of the messages to reach their intended destinations could inhibit response functions or create an unsafe condition that could have physical impacts.(Citation: Bonnie Zhu, Anthony Joseph, Shankar Sastry 2011)(Citation: Electricity Information Sharing and Analysis Center; SANS Industrial Control Systems March 2016)

Adversaries may block communications by either making modifications to software ([System Firmware](https://attack.mitre.org/techniques/T0857), [Module Firmware](https://attack.mitre.org/techniques/T0839), [Hooking](https://attack.mitre.org/techniques/T0874), and [Rootkit](https://attack.mitre.org/techniques/T0851)) and services ([Service Stop](https://attack.mitre.org/techniques/T0881), [Denial of Service](https://attack.mitre.org/techniques/T0814)) on systems and devices or by positioning themselves between systems and devices and intercepting and blocking the communications such as the case with an [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T0830) attack.

## Sub-techniques
- T1691.001: Command Message
- T1691.002: Reporting Message

## Mitigations
- M0807: Network Allowlists
- M0810: Out-of-Band Communications Channel
- M0814: Static Network Configuration


---

# T0811: Data from Information Repositories


**ATT&CK ID:** T0811  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Collection  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0811  

## Description
Adversaries may target and collect data from information repositories. This can include sensitive data such as specifications, schematics, or diagrams of control system layouts, devices, and processes. Examples of information repositories include reference databases in the process environment, as well as databases in the corporate network that might contain information about the ICS.(Citation: Cybersecurity & Infrastructure Security Agency March 2018)

Information collected from these systems may provide the adversary with a better understanding of the operational environment, vendors used, processes, or procedures of the ICS.

In a campaign between 2011 and 2013 against ONG organizations, Chinese state-sponsored actors searched document repositories for specific information such as, system manuals, remote terminal unit (RTU) sites, personnel lists, documents that included the string SCAD*, user credentials, and remote dial-up access information. (Citation: CISA AA21-201A Pipeline Intrusion July 2021)

## Mitigations
- M0917: User Training
- M0918: User Account Management
- M0922: Restrict File and Directory Permissions
- M0926: Privileged Account Management
- M0941: Encrypt Sensitive Information
- M0947: Audit

## Known Software Using This Technique
- S0038: Duqu


---

# T0864: Transient Cyber Asset


**ATT&CK ID:** T0864  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Initial Access  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0864  

## Description
Adversaries may target devices that are transient across ICS networks and external networks. Normally, transient assets are brought into an environment by authorized personnel and do not remain in that environment on a permanent basis. (Citation: North American Electric Reliability Corporation June 2021) Transient assets are commonly needed to support management functions and may be more common in systems where a remotely managed asset is not feasible, external connections for remote access do not exist, or 3rd party contractor/vendor access is required. 

Adversaries may take advantage of transient assets in different ways. For instance, adversaries may target a transient asset when it is connected to an external network and then leverage its trusted access in another environment to launch an attack. They may also take advantage of installed applications and libraries that are used by legitimate end-users to interact with control system devices. 

Transient assets, in some cases, may not be deployed with a secure configuration leading to weaknesses that could allow an adversary to propagate malicious executable code, e.g., the transient asset may be infected by malware and when connected to an ICS environment the malware propagates onto other systems.

## Mitigations
- M0930: Network Segmentation
- M0941: Encrypt Sensitive Information
- M0947: Audit
- M0949: Antivirus/Antimalware
- M0951: Update Software


---

# T0873.001: Siemens Project File Format

**Parent technique:** T0873
**ATT&CK ID:** T0873.001  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Persistence  
**Reference:** https://attack.mitre.org/techniques/T0873/001  

## Description
Adversaries may infect Siemens PLC project files (i.e., Step 7, WinCC, etc.) to achieve [Execution](https://attack.mitre.org/tactics/TA0104), [Persistence](https://attack.mitre.org/tactics/TA0110), and [Lateral Movement](https://attack.mitre.org/tactics/TA0109) objectives. Adversaries may modify an existing project file or bring their own project files into the environment.(Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

The ability for an adversary to deploy an infected project file relies on access to a workstation with Siemens PLC programming software installed on it from which a program download can be performed.

## Mitigations
- M0922: Restrict File and Directory Permissions
- M0941: Encrypt Sensitive Information
- M0945: Code Signing
- M0947: Audit

## Known Software Using This Technique
- S0603: Stuxnet


---

# T0835: Manipulate I/O Image


**ATT&CK ID:** T0835  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0835  

## Description
Adversaries may manipulate the I/O image of PLCs through various means to prevent them from functioning as expected. Methods of I/O image manipulation may include overriding the I/O table via direct memory manipulation or using the override function used for testing PLC programs. (Citation: Dr. Kelvin T. Erickson December 2010) During the scan cycle, a PLC reads the status of all inputs and stores them in an image table. (Citation: Nanjundaiah, Vaidyanath) The image table is the PLCs internal storage location where values of inputs/outputs for one scan are stored while it executes the user program. After the PLC has solved the entire logic program, it updates the output image table. The contents of this output image table are written to the corresponding output points in I/O Modules. 

One of the unique characteristics of PLCs is their ability to override the status of a physical discrete input or to override the logic driving a physical output coil and force the output to a desired status.

## Mitigations
- M0816: Mitigation Limited or Not Effective

## Known Software Using This Technique
- S1006: PLC-Blaster
- S0603: Stuxnet


---

# T0842: Network Sniffing


**ATT&CK ID:** T0842  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Discovery  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0842  

## Description
Network sniffing is the practice of using a network interface on a computer system to monitor or capture information (Citation: Enterprise ATT&CK January 2018) regardless of whether it is the specified destination for the information. 

An adversary may attempt to sniff the traffic to gain information about the target. This information can vary in the level of importance. Relatively unimportant information is general communications to and from machines.  Relatively important information would be login information. User credentials may be sent over an unencrypted protocol, such as Telnet, that can be captured and obtained through network packet analysis. 

In addition, ARP and Domain Name Service (DNS) poisoning can be used to capture credentials to websites, proxies, and internal systems by redirecting traffic to an adversary.

## Mitigations
- M0808: Encrypt Network Traffic
- M0814: Static Network Configuration
- M0926: Privileged Account Management
- M0930: Network Segmentation
- M0932: Multi-factor Authentication

## Known Software Using This Technique
- S1045: INCONTROLLER
- S0603: Stuxnet
- S1010: VPNFilter


---

# T0851: Rootkit


**ATT&CK ID:** T0851  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Evasion, Inhibit Response Function  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0851  

## Description
Adversaries may deploy rootkits to hide the presence of programs, files, network connections, services, drivers, and other system components. Rootkits are programs that hide the existence of malware by intercepting and modifying operating-system API calls that supply system information. Rootkits or rootkit-enabling functionality may reside at the user or kernel level in the operating system, or lower. (Citation: Enterprise ATT&CK January 2018)   

Firmware rootkits that affect the operating system yield nearly full control of the system. While firmware rootkits are normally developed for the main processing board, they can also be developed for the I/O that is attached to an asset. Compromise of this firmware allows the modification of all of the process variables and functions the module engages in. This may result in commands being disregarded and false information being fed to the main device. By tampering with device processes, an adversary may inhibit its expected response functions and possibly enable [Impact](https://attack.mitre.org/tactics/TA0105).

## Mitigations
- M0945: Code Signing
- M0947: Audit

## Known Software Using This Technique
- S0603: Stuxnet


---

# T0802: Automated Collection


**ATT&CK ID:** T0802  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Collection  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0802  

## Description
Adversaries may automate collection of industrial environment information using tools or scripts. This automated collection may leverage native control protocols and tools available in the control systems environment. For example, the OPC protocol may be used to enumerate and gather information. Access to a system or interface with these native protocols may allow collection and enumeration of other attached, communicating servers and devices.

## Mitigations
- M0807: Network Allowlists
- M0930: Network Segmentation

## Known Software Using This Technique
- S0093: Backdoor.Oldrea
- S0604: Industroyer
- S1072: Industroyer2


---

# T1694: Insecure Credentials


**ATT&CK ID:** T1694  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Persistence, Lateral Movement  
**Reference:** https://attack.mitre.org/techniques/T1694  

## Description
Adversaries may target insecure credentials as a means to persist on a system or device or move laterally from one system or device to another. Insecure credentials may appear as default credentials which are pre-configured credentials on a system, device, or software that are well-known in documentation or hard-coded credentials which are built into the system, device, or software that cannot be changed or not easily changed because of the impact on control processes.(Citation: NIST SP 800-82r3)(Citation: ICS-ALERT-13-164-01)(Citation: OT IceFall)
 Adversaries often times use insecure credentials to evade detection as they are typically forgotten about by system and device owners.

## Sub-techniques
- T1694.001: Default Credentials
- T1694.002: Hardcoded Credentials

## Mitigations
- M0801: Access Management


---

# T1692.001: Command Message

**Parent technique:** T1692
**ATT&CK ID:** T1692.001  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Evasion, Impair Process Control  
**Reference:** https://attack.mitre.org/techniques/T1692/001  

## Description
Adversaries may send unauthorized command messages to instruct control system assets to perform actions outside of their intended functionality, or without the logical preconditions to trigger their expected function. Command messages are used in ICS networks to give direct instructions to control systems devices. If an adversary can send an unauthorized command message to a control system, then it can instruct the control systems device to perform an action outside the normal bounds of the device's actions. An adversary could potentially instruct a control systems device to perform an action that will cause an [Impact](https://attack.mitre.org/tactics/TA0105).(Citation: Bonnie Zhu, Anthony Joseph, Shankar Sastry 2011)

In the Dallas Siren incident, adversaries were able to send command messages to activate tornado alarm systems across the city without an impending tornado or other disaster.(Citation: Zack Whittaker April 2017)(Citation: Benjamin Freed March 2019)

## Mitigations
- M0802: Communication Authenticity
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0818: Validate Program Inputs
- M0930: Network Segmentation
- M0937: Filter Network Traffic

## Known Software Using This Technique
- S1045: INCONTROLLER
- S0604: Industroyer
- S1072: Industroyer2


---

# T0809: Data Destruction


**ATT&CK ID:** T0809  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0809  

## Description
Adversaries may perform data destruction over the course of an operation. The adversary may drop or create malware, tools, or other non-native files on a target system to accomplish this, potentially leaving behind traces of malicious activities. Such non-native files and other data may be removed over the course of an intrusion to maintain a small footprint or as a standard part of the post-intrusion cleanup process. (Citation: Enterprise ATT&CK January 2018)

Data destruction may also be used to render operator interfaces unable to respond and to disrupt response functions from occurring as expected. An adversary may also destroy data backups that are vital to recovery after an incident.

Standard file deletion commands are available on most operating system and device interfaces to perform cleanup, but adversaries may use other tools as well. Two examples are Windows Sysinternals SDelete and Active@ Killdisk.

## Mitigations
- M0922: Restrict File and Directory Permissions
- M0926: Privileged Account Management
- M0953: Data Backup

## Known Software Using This Technique
- S1157: Fuxnet
- S1045: INCONTROLLER
- S0604: Industroyer
- S0607: KillDisk


---

# T0832: Manipulation of View


**ATT&CK ID:** T0832  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impact  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0832  

## Description
Adversaries may attempt to manipulate the information reported back to operators or controllers. This manipulation may be short term or sustained. During this time the process itself could be in a much different state than what is reported. (Citation: Corero) (Citation: Michael J. Assante and Robert M. Lee) (Citation: Tyson Macaulay) 

Operators may be fooled into doing something that is harmful to the system in a loss of view situation. With a manipulated view into the systems, operators may issue inappropriate control sequences that introduce faults or catastrophic failures into the system. Business analysis systems can also be provided with inaccurate data leading to bad management decisions.

## Mitigations
- M0802: Communication Authenticity
- M0810: Out-of-Band Communications Channel
- M0953: Data Backup

## Known Software Using This Technique
- S0604: Industroyer
- S0603: Stuxnet


---

# T1692.002: Reporting Message

**Parent technique:** T1692
**ATT&CK ID:** T1692.002  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Evasion, Impair Process Control  
**Reference:** https://attack.mitre.org/techniques/T1692/002  

## Description
Adversaries may spoof reporting messages in control system environments for evasion and to impair process control. In control systems, reporting messages contain telemetry data (e.g., I/O values) pertaining to the current state of equipment and the industrial process. Reporting messages are important for monitoring the normal operation of a system or identifying important events such as deviations from expected values.

If an adversary has the ability to Spoof Reporting Messages, they can impact the control system in many ways. The adversary can Spoof Reporting Messages that state that the process is operating normally, as a form of evasion. The adversary could also Spoof Reporting Messages to make the defenders and operators think that other errors are occurring in order to distract them from the actual source of a problem.(Citation: Bonnie Zhu, Anthony Joseph, Shankar Sastry 2011)

## Mitigations
- M0802: Communication Authenticity
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic


---

# T0872: Indicator Removal on Host


**ATT&CK ID:** T0872  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Evasion  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0872  

## Description
Adversaries may attempt to remove indicators of their presence on a system in an effort to cover their tracks. In cases where an adversary may feel detection is imminent, they may try to overwrite, delete, or cover up changes they have made to the device.

## Mitigations
- M0922: Restrict File and Directory Permissions

## Known Software Using This Technique
- S0607: KillDisk
- S1009: Triton


---

# T0877: I/O Image


**ATT&CK ID:** T0877  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Collection  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0877  

## Description
Adversaries may seek to capture process values related to the inputs and outputs of a PLC. During the scan cycle, a PLC reads the status of all inputs and stores them in an image table. (Citation: Nanjundaiah, Vaidyanath) The image table is the PLCs internal storage location where values of inputs/outputs for one scan are stored while it executes the user program. After the PLC has solved the entire logic program, it updates the output image table. The contents of this output image table are written to the corresponding output points in I/O Modules.

The Input and Output Image tables described above make up the I/O Image on a PLC. This image is used by the user program instead of directly interacting with physical I/O. (Citation: Spenneberg, Ralf 2016) 

Adversaries may collect the I/O Image state of a PLC by utilizing a devices [Native API](https://attack.mitre.org/techniques/T0834) to access the memory regions directly. The collection of the PLCs I/O state could be used to replace values or inform future stages of an attack.

## Mitigations
- M0816: Mitigation Limited or Not Effective

## Known Software Using This Technique
- S0603: Stuxnet


---

# T1695.001: Serial COM

**Parent technique:** T1695
**ATT&CK ID:** T1695.001  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Reference:** https://attack.mitre.org/techniques/T1695/001  

## Description
Adversaries may block access to serial COM to prevent instructions or configurations from reaching target devices. Serial Communication ports (COM) allow communication with control system devices. Devices can receive command and configuration messages over such serial COM. Devices also use serial COM to send command and reporting messages. Blocking device serial COM may also block command messages and block reporting messages.

A serial to Ethernet converter is often connected to a serial COM to facilitate communication between serial and Ethernet devices. One approach to blocking a serial COM would be to create and hold open a TCP session with the Ethernet side of the converter. A serial to Ethernet converter may have a few ports open to facilitate multiple communications. For example, if there are three serial COM available -- 1, 2 and 3 --, the converter might be listening on the corresponding ports 20001, 20002, and 20003. If a TCP/IP connection is opened with one of these ports and held open, then the port will be unavailable for use by another party. One way the adversary could achieve this would be to initiate a TCP session with the serial to Ethernet converter at 10.0.0.1 via Telnet on serial port 1 with the following command: telnet 10.0.0.1 20001.

## Mitigations
- M0807: Network Allowlists
- M0810: Out-of-Band Communications Channel
- M0930: Network Segmentation

## Known Software Using This Technique
- S0604: Industroyer


---

# T1694.001: Default Credentials

**Parent technique:** T1694
**ATT&CK ID:** T1694.001  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Persistence, Lateral Movement  
**Reference:** https://attack.mitre.org/techniques/T1694/001  

## Description
Adversaries may leverage manufacturer or supplier set default credentials on control system devices. These default credentials may have administrative permissions and may be necessary for initial configuration of the device. It is general best practice to change the passwords for these accounts as soon as possible, but some manufacturers may have devices that have passwords or usernames that cannot be changed.(Citation: Keith Stouffer May 2015)

Default credentials are normally documented in an instruction manual that is either packaged with the device, published online through official means, or published online through unofficial means. Adversaries may leverage default credentials that have not been properly modified or disabled.

## Mitigations
- M0801: Access Management
- M0927: Password Policies


---

# T0815: Denial of View


**ATT&CK ID:** T0815  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impact  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0815  

## Description
Adversaries may cause a denial of view in attempt to disrupt and prevent operator oversight on the status of an ICS environment. This may manifest itself as a temporary communication failure between a device and its control source, where the interface recovers and becomes available once the interference ceases. (Citation: Corero) (Citation: Michael J. Assante and Robert M. Lee) (Citation: Tyson Macaulay) 

An adversary may attempt to deny operator visibility by preventing them from receiving status and reporting messages. Denying this view may temporarily block and prevent operators from noticing a change in state or anomalous behavior. The environment's data and processes may still be operational, but functioning in an unintended or adversarial manner.

## Mitigations
- M0810: Out-of-Band Communications Channel
- M0811: Redundancy of Service
- M0953: Data Backup

## Known Software Using This Technique
- S0604: Industroyer


---

# T0843.003: Program Append

**Parent technique:** T0843
**ATT&CK ID:** T0843.003  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Lateral Movement  
**Reference:** https://attack.mitre.org/techniques/T0843/003  

## Description
Adversaries may execute a program append to a PLC to update parts of an existing program. It may or may not require stopping the PLC which may allow it to continue running during transfer and reconfiguration without interruption to process control. Adversaries may leverage this approach to minimize downtime and evade detection. 

The ability to perform a program append to the PLC typically relies on access to a workstation with the vendor-specific PLC programming software installed.

## Mitigations
- M0800: Authorization Enforcement
- M0801: Access Management
- M0802: Communication Authenticity
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic
- M0945: Code Signing
- M0947: Audit


---

# T0871: Execution through API


**ATT&CK ID:** T0871  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Execution  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0871  

## Description
Adversaries may attempt to leverage Application Program Interfaces (APIs) used for communication between control software and the hardware. Specific functionality is often coded into APIs which can be called by software to engage specific functions on a device or other software.

## Mitigations
- M0800: Authorization Enforcement
- M0801: Access Management
- M0804: Human User Authentication
- M0938: Execution Prevention

## Known Software Using This Technique
- S1009: Triton


---

# T0846.001: Port Scan

**Parent technique:** T0846
**ATT&CK ID:** T0846.001  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Discovery  
**Reference:** https://attack.mitre.org/techniques/T0846/001  

## Description
Adversaries may perform a port scan on a system, device, or network to identify live hosts, enumerate open ports and running services, identify operating systems, and map out the network.(Citation: NIST SP 800-82r3) The results of a port scan may inform adversary [Discovery](https://attack.mitre.org/tactics/TA0102), [Lateral Movement](https://attack.mitre.org/tactics/TA0109), and vulnerability exploitation decisions ([Exploitation for Evasion](https://attack.mitre.org/techniques/T0820), [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T0890), [Exploitation of Remote Services](https://attack.mitre.org/techniques/T0866)). 

Some common tools for executing a port scan include `nmap`, `netcat`, and the Advanced Port Scanner.

## Mitigations
- M0814: Static Network Configuration
- M0930: Network Segmentation
- M0931: Network Intrusion Prevention

## Known Software Using This Technique
- S1045: INCONTROLLER
- S0604: Industroyer
- S1006: PLC-Blaster


---

# T0862: Supply Chain Compromise


**ATT&CK ID:** T0862  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Initial Access  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0862  

## Description
Adversaries may perform supply chain compromise to gain control systems environment access by means of infected products, software, and workflows. Supply chain compromise is the manipulation of products, such as devices or software, or their delivery mechanisms before receipt by the end consumer. Adversary compromise of these products and mechanisms is done for the goal of data or system compromise, once infected products are introduced to the target environment. 

Supply chain compromise can occur at all stages of the supply chain, from manipulation of development tools and environments to manipulation of developed products and tools distribution mechanisms. This may involve the compromise and replacement of legitimate software and patches, such as on third party or vendor websites. Targeting of supply chain compromise can be done in attempts to infiltrate the environments of a specific audience. In control systems environments with assets in both the IT and OT networks, it is possible a supply chain compromise affecting the IT environment could enable further access to the OT environment.   

Counterfeit devices may be introduced to the global supply chain posing safety and cyber risks to asset owners and operators. These devices may not meet the safety, engineering and manufacturing requirements of regulatory bodies but may feature tagging indicating conformance with industry standards. Due to the lack of adherence to standards and overall lesser quality, the counterfeit products may pose a serious safety and operational risk. (Citation: Control Global May 2019) 

Yokogawa identified instances in which their customers received counterfeit differential pressure transmitters using the Yokogawa logo. The counterfeit transmitters were nearly indistinguishable with a semblance of functionality and interface that mimics the genuine product. (Citation: Control Global May 2019) 

F-Secure Labs analyzed the approach the adversary used to compromise victim systems with Havex. (Citation: Daavid Hentunen, Antti Tikkanen June 2014) The adversary planted trojanized software installers available on legitimate ICS/SCADA vendor websites. After being downloaded, this software infected the host computer with a Remote Access Trojan (RAT).

## Mitigations
- M0817: Supply Chain Management
- M0916: Vulnerability Scanning
- M0945: Code Signing
- M0947: Audit
- M0951: Update Software

## Known Threat Groups Using This Technique
- G0035: Dragonfly
- G0088: TEMP.Veles

## Known Software Using This Technique
- S0093: Backdoor.Oldrea


---

# T0880: Loss of Safety


**ATT&CK ID:** T0880  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impact  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0880  

## Description
Adversaries may compromise safety system functions designed to maintain safe operation of a process when unacceptable or dangerous conditions occur. Safety systems are often composed of the same elements as control systems but have the sole purpose of ensuring the process fails in a predetermined safe manner. 

Many unsafe conditions in process control happen too quickly for a human operator to react to. Speed is critical in correcting these conditions to limit serious impacts such as Loss of Control and Property Damage. 

Adversaries may target and disable safety system functions as a prerequisite to subsequent attack execution or to allow for future unsafe conditionals to go unchecked. Detection of a Loss of Safety by operators can result in the shutdown of a process due to strict policies regarding safety systems. This can cause a Loss of Productivity and Revenue and may meet the technical goals of adversaries seeking to cause process disruptions.

## Mitigations
- M0805: Mechanical Protection Layers
- M0812: Safety Instrumented Systems

## Known Software Using This Technique
- S1009: Triton


---

# T1695.002: Ethernet

**Parent technique:** T1695
**ATT&CK ID:** T1695.002  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Reference:** https://attack.mitre.org/techniques/T1695/002  

## Description
Adversaries may block access to Ethernet communications to prevent instructions or configurations messages from reaching target systems and devices. Ethernet connections allow for communications between IT and OT systems and devices. Blocking Ethernet communications may also block command and reporting messages.(Citation: Bonnie Zhu, Anthony Joseph, Shankar Sastry 2011)

An adversary may block Ethernet communications by disabling network interfaces, [Service Stop](https://attack.mitre.org/techniques/T0881), or conducting an [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T0830) attack and dropping the network traffic.

## Mitigations
- M0807: Network Allowlists
- M0810: Out-of-Band Communications Channel
- M0930: Network Segmentation

## Known Software Using This Technique
- S0372: LockerGoga


---

# T0828: Loss of Productivity and Revenue


**ATT&CK ID:** T0828  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impact  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0828  

## Description
Adversaries may cause loss of productivity and revenue through disruption and even damage to the availability and integrity of control system operations, devices, and related processes. This technique may manifest as a direct effect of an ICS-targeting attack or tangentially, due to an IT-targeting attack against non-segregated environments. 

In cases where these operations or services are brought to a halt, the loss of productivity may eventually present an impact for the end-users or consumers of products and services. The disrupted supply-chain may result in supply shortages and increased prices, among other consequences. 

A ransomware attack on an Australian beverage company resulted in the shutdown of some manufacturing sites, including precautionary halts to protect key systems. (Citation: Paganini, Pierluigi June 2020) The company announced the potential for temporary shortages of their products following the attack. (Citation: Paganini, Pierluigi June 2020) (Citation: Lion Corporation June 2020) 

In the 2021 Colonial Pipeline ransomware incident, the pipeline was unable to transport approximately 2.5 million barrels of fuel per day to the East Coast.  (Citation: Colonial Pipeline Company May 2021)

## Mitigations
- M0953: Data Backup

## Known Software Using This Technique
- S0606: Bad Rabbit
- S0608: Conficker
- S0605: EKANS
- S0372: LockerGoga
- S0368: NotPetya
- S0496: REvil
- S0446: Ryuk


---

# T0865: Spearphishing Attachment


**ATT&CK ID:** T0865  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Initial Access  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0865  

## Description
Adversaries may use a spearphishing attachment, a variant of spearphishing, as a form of a social engineering attack against specific targets. Spearphishing attachments are different from other forms of spearphishing in that they employ malware attached to an email. All forms of spearphishing are electronically delivered and target a specific individual, company, or industry. In this scenario, adversaries attach a file to the spearphishing email and usually rely upon [User Execution](https://attack.mitre.org/techniques/T0863) to gain execution and access. (Citation: Enterprise ATT&CK October 2019) 

A Chinese spearphishing campaign running from December 9, 2011 through February 29, 2012, targeted ONG organizations and their employees. The emails were constructed with a high level of sophistication to convince employees to open the malicious file attachments. (Citation: CISA AA21-201A Pipeline Intrusion July 2021)

## Mitigations
- M0917: User Training
- M0921: Restrict Web-Based Content
- M0931: Network Intrusion Prevention
- M0949: Antivirus/Antimalware

## Known Threat Groups Using This Technique
- G1000: ALLANITE
- G0064: APT33
- G0032: Lazarus Group
- G0049: OilRig

## Known Software Using This Technique
- S0093: Backdoor.Oldrea
- S0089: BlackEnergy


---

# T0846.003: Multicast Discovery

**Parent technique:** T0846
**ATT&CK ID:** T0846.003  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Discovery  
**Reference:** https://attack.mitre.org/techniques/T0846/003  

## Description
Adversaries may perform multicast discovery requests which is when one system or device sends messages to all systems and devices in a pre-defined group on a network (or subnet) and then waits for a response. If a response is received that means the system or device that responded is live and can communicate over that protocol.  Multicast discovery tends to be stealthier than broadcast discovery because every system or device on the network (or subnet) is not being messaged. 

One common OT protocol that has a multicast discovery mechanism is the Process Field Network (PROFINET) Discovery and Configuration Protocol (DCP) with its Identify All requests.(Citation: Cisco Active Discovery)

## Mitigations
- M0814: Static Network Configuration
- M0930: Network Segmentation

## Known Software Using This Technique
- S1045: INCONTROLLER


---

# T1693.001: System Firmware

**Parent technique:** T1693
**ATT&CK ID:** T1693.001  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Persistence, Inhibit Response Function, Impair Process Control  
**Reference:** https://attack.mitre.org/techniques/T1693/001  

## Description
System firmware on modern assets is often designed with an update feature. Older device firmware may be factory installed and require special reprograming equipment. When available, the firmware update feature enables vendors to remotely patch bugs and perform upgrades. Device firmware updates are often delegated to the user and may be done using a software update package. It may also be possible to perform this task over the network.

An adversary may exploit the firmware update feature on accessible devices to upload malicious or out-of-date firmware. Malicious modification of device firmware may provide an adversary with root access to a device, given firmware is one of the lowest programming abstraction layers.(Citation: Basnight, Zachry, et al.)

## Mitigations
- M0801: Access Management
- M0802: Communication Authenticity
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0808: Encrypt Network Traffic
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic
- M0941: Encrypt Sensitive Information
- M0945: Code Signing
- M0946: Boot Integrity
- M0947: Audit
- M0951: Update Software

## Known Software Using This Technique
- S1009: Triton


---

# T1694.002: Hardcoded Credentials

**Parent technique:** T1694
**ATT&CK ID:** T1694.002  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Persistence, Lateral Movement  
**Reference:** https://attack.mitre.org/techniques/T1694/002  

## Description
Adversaries may leverage credentials that are hardcoded in software or firmware to gain an unauthorized interactive user session to an asset. Examples credentials that may be hardcoded in an asset include:

* Username/Passwords
* Cryptographic keys/Certificates
* API tokens

Unlike [Default Credentials](https://attack.mitre.org/techniques/T0812), these credentials are built into the system in a way that they either cannot be changed by the asset owner, or may be infeasible to change because of the impact it would cause to the control system operation. These credentials may be reused across whole product lines or device models and are often not published or known to the owner and operators of the asset.(Citation: ICS-ALERT-13-164-01)(Citation: OT IceFall)

Adversaries may utilize these hardcoded credentials to move throughout the control system environment or provide reliable access for their tools to interact with industrial assets.

## Mitigations
- M0801: Access Management

## Known Software Using This Technique
- S1045: INCONTROLLER
- S0603: Stuxnet


---

# T1695.003: Wi-Fi

**Parent technique:** T1695
**ATT&CK ID:** T1695.003  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Reference:** https://attack.mitre.org/techniques/T1695/003  

## Description
Adversaries may block access to Wi-Fi communications to prevent messages from reaching target systems and devices. Wi-Fi connections allow for communications between IT and OT systems and devices. Blocking Wi-Fi communications may also block command and reporting messages.(Citation: Bonnie Zhu, Anthony Joseph, Shankar Sastry 2011)

An adversary may block Wi-Fi communications by disabling network interfaces, [Service Stop](https://attack.mitre.org/techniques/T0881), conducting an [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T0830) attack and dropping the network traffic, or by jamming the Wi-Fi signal.

## Mitigations
- M0807: Network Allowlists
- M0810: Out-of-Band Communications Channel
- M0930: Network Segmentation

## Known Software Using This Technique
- S0372: LockerGoga


---

# T1693.002: Module Firmware

**Parent technique:** T1693
**ATT&CK ID:** T1693.002  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Persistence, Inhibit Response Function, Impair Process Control  
**Reference:** https://attack.mitre.org/techniques/T1693/002  

## Description
Adversaries may install malicious or vulnerable firmware onto modular hardware devices. Control system devices often contain modular hardware devices. These devices may have their own set of firmware that is separate from the firmware of the main control system equipment.

This technique is similar to System Firmware, but is conducted on other system components that may not have the same capabilities or level of integrity checking. Although it results in a device re-image, malicious device firmware may provide persistent access to remaining devices.(Citation: Daniel Peck,  Dale Peterson January 2009)

An easy point of access for an adversary is the Ethernet card, which may have its own CPU, RAM, and operating system. The adversary may attack and likely exploit the computer on an Ethernet card. Exploitation of the Ethernet card computer may enable the adversary to accomplish additional attacks, such as the following:(Citation: Daniel Peck,  Dale Peterson January 2009)

* Delayed Attack - The adversary may stage an attack in advance and choose when to launch it, such as at a particularly damaging time.
* Brick the Ethernet Card - Malicious firmware may be programmed to result in an Ethernet card failure, requiring a factory return.
* Random Attack or Failure - The adversary may load malicious firmware onto multiple field devices. Execution of an attack and the time it occurs is generated by a pseudo-random number generator.
* A Field Device Worm - The adversary may choose to identify all field devices of the same model, with the end goal of performing a device-wide compromise.
* Attack Other Cards on the Field Device - Although it is not the most important module in a field device, the Ethernet card is most accessible to the adversary and malware. Compromise of the Ethernet card may provide a more direct route to compromising other modules, such as the CPU module.

## Mitigations
- M0801: Access Management
- M0802: Communication Authenticity
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0808: Encrypt Network Traffic
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic
- M0941: Encrypt Sensitive Information
- M0945: Code Signing
- M0946: Boot Integrity
- M0947: Audit


---

# T0843.001: Download All

**Parent technique:** T0843
**ATT&CK ID:** T0843.001  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Lateral Movement  
**Reference:** https://attack.mitre.org/techniques/T0843/001  

## Description
Adversaries may execute a full program download to a PLC to overwrite the entire PLC program and configuration to deploy a new project or make major changes. This typically requires stopping the PLC and adversely impacting control processes.

The ability to perform a full program download to the PLC typically relies on access to a workstation with the vendor-specific PLC programming software installed.

## Mitigations
- M0800: Authorization Enforcement
- M0801: Access Management
- M0802: Communication Authenticity
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic
- M0945: Code Signing
- M0947: Audit

## Known Software Using This Technique
- S1045: INCONTROLLER


---

# T0895: Autorun Image


**ATT&CK ID:** T0895  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Execution  
**Reference:** https://attack.mitre.org/techniques/T0895  

## Description
Adversaries may leverage AutoRun functionality or scripts to execute malicious code. Devices configured to enable AutoRun functionality or legacy operating systems may be susceptible to abuse of these features to run malicious code stored on various forms of removeable media (i.e., USB, Disk Images [.ISO]). Commonly, AutoRun or AutoPlay are disabled in many operating systems configurations to mitigate against this technique. If a device is configured to enable AutoRun or AutoPlay, adversaries may execute code on the device by mounting the removable media to the device, either through physical or virtual means. This may be especially relevant for virtual machine environments where disk images may be dynamically mapped to a guest system on a hypervisor.  

An example could include an adversary gaining access to a hypervisor through the management interface to modify a virtual machine’s hardware configuration. They could then deploy an iso image with a malicious AutoRun script to cause the virtual machine to automatically execute the code contained on the disk image. This would enable the execution of malicious code within a virtual machine without needing any prior remote access to that system.

## Mitigations
- M0928: Operating System Configuration


---

# T0817: Drive-by Compromise


**ATT&CK ID:** T0817  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Initial Access  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0817  

## Description
Adversaries may gain access to a system during a drive-by compromise, when a user visits a website as part of a regular browsing session. With this technique, the user's web browser is targeted and exploited simply by visiting the compromised website. 

The adversary may target a specific community, such as trusted third party suppliers or other industry specific groups, which often visit the target website. This kind of targeted attack relies on a common interest, and is known as a strategic web compromise or watering hole attack. 

The National Cyber Awareness System (NCAS) has issued a Technical Alert (TA) regarding Russian government cyber activity targeting critical infrastructure sectors. (Citation: Cybersecurity & Infrastructure Security Agency March 2018) Analysis by DHS and FBI has noted two distinct categories of victims in the Dragonfly campaign on the Western energy sector: staging and intended targets. The adversary targeted the less secure networks of staging targets, including trusted third-party suppliers and related peripheral organizations. Initial access to the intended targets used watering hole attacks to target process control, ICS, and critical infrastructure related trade publications and informational websites.

## Mitigations
- M0921: Restrict Web-Based Content
- M0948: Application Isolation and Sandboxing
- M0950: Exploit Protection
- M0951: Update Software

## Known Threat Groups Using This Technique
- G1000: ALLANITE
- G0035: Dragonfly
- G0049: OilRig
- G0088: TEMP.Veles

## Known Software Using This Technique
- S0606: Bad Rabbit


---

# T1691.002: Reporting Message

**Parent technique:** T1691
**ATT&CK ID:** T1691.002  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Reference:** https://attack.mitre.org/techniques/T1691/002  

## Description
Adversaries may block or prevent a reporting message from reaching its intended target. In control systems, reporting messages contain telemetry data (e.g., I/O values) pertaining to the current state of equipment and the industrial process. By blocking these reporting messages, an adversary can potentially hide their actions from an operator.

Blocking reporting messages in control systems that manage physical processes may contribute to system impact, causing inhibition of a response function. A control system may not be able to respond in a proper or timely manner to an event, such as a dangerous fault, if its corresponding reporting message is blocked.(Citation: Bonnie Zhu, Anthony Joseph, Shankar Sastry 2011)(Citation: Electricity Information Sharing and Analysis Center; SANS Industrial Control Systems March 2016)

## Mitigations
- M0807: Network Allowlists
- M0810: Out-of-Band Communications Channel
- M0814: Static Network Configuration

## Known Software Using This Technique
- S0604: Industroyer


---

# T1693: Modify Firmware


**ATT&CK ID:** T1693  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Persistence, Inhibit Response Function, Impair Process Control  
**Reference:** https://attack.mitre.org/techniques/T1693  

## Description
Firmware is low-level software embedded in hardware that enables systems and devices to function properly and is commonly found in ICS environments. Adversaries may modify firmware on a system or device by installing malicious or vulnerable versions that enable them to achieve objectives such as [Persistence](https://attack.mitre.org/tactics/TA0110), [Impair Process Control](https://attack.mitre.org/tactics/TA0106), and [Inhibit Response Function](https://attack.mitre.org/tactics/TA0107). 

Adversaries may modify system and device firmware by using the built-in firmware update functionality which may support local or remote installation. The malicious or vulnerable firmware may be delivered via [Replication Through Removable Media](https://attack.mitre.org/techniques/T0847), [Supply Chain Compromise](https://attack.mitre.org/techniques/T0862), or [Remote Services](https://attack.mitre.org/techniques/T0886). Once installed, the malicious or vulnerable firmware could be used to provide [Rootkit](https://attack.mitre.org/techniques/T0851) and [Hooking](https://attack.mitre.org/techniques/T0874) functionality, [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T0890), or [Denial of Service](https://attack.mitre.org/techniques/T0814).(Citation: Basnight, Zachry, et al.)

## Sub-techniques
- T1693.001: System Firmware
- T1693.002: Module Firmware

## Mitigations
- M0801: Access Management
- M0802: Communication Authenticity
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0808: Encrypt Network Traffic
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic
- M0941: Encrypt Sensitive Information
- M0945: Code Signing
- M0946: Boot Integrity
- M0947: Audit


---

# T0879: Damage to Property


**ATT&CK ID:** T0879  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impact  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0879  

## Description
Adversaries may cause damage and destruction of property to infrastructure, equipment, and the surrounding environment when attacking control systems. This technique may result in device and operational equipment breakdown, or represent tangential damage from other techniques used in an attack. Depending on the severity of physical damage and disruption caused to control processes and systems, this technique may result in [Loss of Safety](https://attack.mitre.org/techniques/T0880). Operations that result in [Loss of Control](https://attack.mitre.org/techniques/T0827) may also cause damage to property, which may be directly or indirectly motivated by an adversary seeking to cause impact in the form of [Loss of Productivity and Revenue](https://attack.mitre.org/techniques/T0828). 


The German Federal Office for Information Security (BSI) reported a targeted attack on a steel mill under an incidents affecting business section of its 2014 IT Security Report. (Citation: BSI State of IT Security 2014)  These targeted attacks affected industrial operations and resulted in breakdowns of control system components and even entire installations. As a result of these breakdowns, massive impact and damage resulted from the uncontrolled shutdown of a blast furnace. 

A Polish student used a remote controller device to interface with the Lodz city tram system in Poland. (Citation: John Bill May 2017) (Citation: Shelley Smith February 2008) (Citation: Bruce Schneier January 2008) Using this remote, the student was able to capture and replay legitimate tram signals. This resulted in damage to impacted trams, people, and the surrounding property. Reportedly, four trams were derailed and were forced to make emergency stops. (Citation: Shelley Smith February 2008) Commands issued by the student may have also resulted in tram collisions, causing harm to those on board and the environment outside. (Citation: Bruce Schneier January 2008)

## Mitigations
- M0805: Mechanical Protection Layers
- M0807: Network Allowlists
- M0812: Safety Instrumented Systems


---

# T0866: Exploitation of Remote Services


**ATT&CK ID:** T0866  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Initial Access, Lateral Movement  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0866  

## Description
Adversaries may exploit a software vulnerability to take advantage of a programming error in a program, service, or within the operating system software or kernel itself to enable remote service abuse. A common goal for post-compromise exploitation of remote services is for initial access into and lateral movement throughout the ICS environment to enable access to targeted systems. (Citation: Enterprise ATT&CK)

ICS asset owners and operators have been affected by ransomware (or disruptive malware masquerading as ransomware) migrating from enterprise IT to ICS environments: WannaCry, NotPetya, and BadRabbit. In each of these cases, self-propagating (wormable) malware initially infected IT networks, but through exploit (particularly the SMBv1-targeting MS17-010 vulnerability) spread to industrial networks, producing significant impacts. (Citation: Joe Slowik April 2019)

## Mitigations
- M0916: Vulnerability Scanning
- M0919: Threat Intelligence Program
- M0926: Privileged Account Management
- M0930: Network Segmentation
- M0942: Disable or Remove Feature or Program
- M0948: Application Isolation and Sandboxing
- M0950: Exploit Protection
- M0951: Update Software

## Known Software Using This Technique
- S0606: Bad Rabbit
- S0368: NotPetya
- S0603: Stuxnet
- S0366: WannaCry


---

# T0822: External Remote Services


**ATT&CK ID:** T0822  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Initial Access  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0822  

## Description
Adversaries may leverage external remote services as a point of initial access into your network. These services allow users to connect to internal network resources from external locations. Examples are VPNs, Citrix, and other access mechanisms. Remote service gateways often manage connections and credential authentication for these services. (Citation: Daniel Oakley, Travis Smith, Tripwire)

External remote services allow administration of a control system from outside the system. Often, vendors and internal engineering groups have access to external remote services to control system networks via the corporate network. In some cases, this access is enabled directly from the internet. While remote access enables ease of maintenance when a control system is in a remote area, compromise of remote access solutions is a liability. The adversary may use these services to gain access to and execute attacks against a control system network. Access to valid accounts is often a requirement. 

As they look for an entry point into the control system network, adversaries may begin searching for existing point-to-point VPN implementations at trusted third party networks or through remote support employee connections where split tunneling is enabled. (Citation: Electricity Information Sharing and Analysis Center; SANS Industrial Control Systems March 2016)

## Mitigations
- M0918: User Account Management
- M0927: Password Policies
- M0930: Network Segmentation
- M0932: Multi-factor Authentication
- M0935: Limit Access to Resource Over Network
- M0936: Account Use Policies
- M0942: Disable or Remove Feature or Program

## Known Software Using This Technique
- S1157: Fuxnet


---

# T0806: Brute Force I/O


**ATT&CK ID:** T0806  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impair Process Control  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0806  

## Description
Adversaries may repetitively or successively change I/O point values to perform an action. Brute Force I/O may be achieved by changing either a range of I/O point values or a single point value repeatedly to manipulate a process function. The adversary's goal and the information they have about the target environment will influence which of the options they choose. In the case of brute forcing a range of point values, the adversary may be able to achieve an impact without targeting a specific point. In the case where a single point is targeted, the adversary may be able to generate instability on the process function associated with that particular point. 

Adversaries may use Brute Force I/O to cause failures within various industrial processes. These failures could be the result of wear on equipment or damage to downstream equipment.

## Mitigations
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic

## Known Software Using This Technique
- S1157: Fuxnet
- S0604: Industroyer
- S1072: Industroyer2


---

# T0830: Adversary-in-the-Middle


**ATT&CK ID:** T0830  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Collection  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0830  

## Description
Adversaries with privileged network access may seek to modify network traffic in real time using adversary-in-the-middle (AiTM) attacks. (Citation: Gabriel Sanchez October 2017) This type of attack allows the adversary to intercept traffic to and/or from a particular device on the network. If a AiTM attack is established, then the adversary has the ability to block, log, modify, or inject traffic into the communication stream. There are several ways to accomplish this attack, but some of the most-common are Address Resolution Protocol (ARP) poisoning and the use of a proxy. (Citation: Bonnie Zhu, Anthony Joseph, Shankar Sastry 2011)  

An AiTM attack may allow an adversary to perform the following attacks:  
[Block Reporting Message](https://attack.mitre.org/techniques/T0804), [Spoof Reporting Message](https://attack.mitre.org/techniques/T0856), [Modify Parameter](https://attack.mitre.org/techniques/T0836), [Unauthorized Command Message](https://attack.mitre.org/techniques/T0855)

## Mitigations
- M0802: Communication Authenticity
- M0810: Out-of-Band Communications Channel
- M0813: Software Process and Device Authentication
- M0814: Static Network Configuration
- M0930: Network Segmentation
- M0931: Network Intrusion Prevention
- M0942: Disable or Remove Feature or Program
- M0947: Audit

## Known Software Using This Technique
- S1010: VPNFilter


---

# T0820: Exploitation for Evasion


**ATT&CK ID:** T0820  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Evasion  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0820  

## Description
Adversaries may exploit a software vulnerability to take advantage of a programming error in a program, service, or within the operating system software or kernel itself to evade detection. Vulnerabilities may exist in software that can be used to disable or circumvent security features.  

Adversaries may have prior knowledge through [Remote System Information Discovery](https://attack.mitre.org/techniques/T0888) about security features implemented on control devices. These device security features will likely be targeted directly for exploitation. There are examples of firmware RAM/ROM consistency checks on control devices being targeted by adversaries to enable the installation of malicious [System Firmware](https://attack.mitre.org/techniques/T0857).

## Mitigations
- M0919: Threat Intelligence Program
- M0948: Application Isolation and Sandboxing
- M0950: Exploit Protection
- M0951: Update Software

## Known Software Using This Technique
- S1009: Triton


---

# T0827: Loss of Control


**ATT&CK ID:** T0827  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impact  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0827  

## Description
Adversaries may seek to achieve a sustained loss of control or a runaway condition in which operators cannot issue any commands even if the malicious interference has subsided. (Citation: Corero) (Citation: Michael J. Assante and Robert M. Lee) (Citation: Tyson Macaulay)

The German Federal Office for Information Security (BSI) reported a targeted attack on a steel mill in its 2014 IT Security Report.(Citation: BSI State of IT Security 2014) These targeted attacks affected industrial operations and resulted in breakdowns of control system components and even entire installations. As a result of these breakdowns, massive impact resulted in damage and unsafe conditions from the uncontrolled shutdown of a blast furnace.

## Mitigations
- M0810: Out-of-Band Communications Channel
- M0811: Redundancy of Service
- M0953: Data Backup

## Known Software Using This Technique
- S0604: Industroyer
- S0372: LockerGoga


---

# T0874: Hooking


**ATT&CK ID:** T0874  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Execution, Privilege Escalation  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0874  

## Description
Adversaries may hook into application programming interface (API) functions used by processes to redirect calls for execution and privilege escalation means. Windows processes often leverage these API functions to perform tasks that require reusable system resources. Windows API functions are typically stored in dynamic-link libraries (DLLs) as exported functions. (Citation: Enterprise ATT&CK)

One type of hooking seen in ICS involves redirecting calls to these functions via import address table (IAT) hooking. IAT hooking uses modifications to a process IAT, where pointers to imported API functions are stored. (Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011)

## Mitigations
- M0944: Restrict Library Loading
- M0947: Audit

## Known Software Using This Technique
- S0603: Stuxnet
- S1009: Triton


---

# T0823: Graphical User Interface


**ATT&CK ID:** T0823  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Execution  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0823  

## Description
Adversaries may attempt to gain access to a machine via a Graphical User Interface (GUI) to enhance execution capabilities. Access to a GUI allows a user to interact with a computer in a more visual manner than a CLI. A GUI allows users to move a cursor and click on interface objects, with a mouse and keyboard as the main input devices, as opposed to just using the keyboard.

If physical access is not an option, then access might be possible via protocols such as VNC on Linux-based and Unix-based operating systems, and RDP on Windows operating systems. An adversary can use this access to execute programs and applications on the target machine.

## Mitigations
- M0816: Mitigation Limited or Not Effective


---

# T0848: Rogue Master


**ATT&CK ID:** T0848  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Initial Access  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0848  

## Description
Adversaries may setup a rogue master to leverage control server functions to communicate with outstations. A rogue master can be used to send legitimate control messages to other control system devices, affecting processes in unintended ways. It may also be used to disrupt network communications by capturing and receiving the network traffic meant for the actual master. Impersonating a master may also allow an adversary to avoid detection. 

In the case of the 2017 Dallas Siren incident, adversaries used a rogue master to send command messages to the 156 distributed sirens across the city, either through a single rogue transmitter with a strong signal, or using many distributed repeaters. (Citation: Bastille April 2017) (Citation: Zack Whittaker April 2017)

## Mitigations
- M0802: Communication Authenticity
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic


---

# T0834: Native API


**ATT&CK ID:** T0834  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Execution  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0834  

## Description
Adversaries may directly interact with the native OS application programming interface (API) to access system functions. Native APIs provide a controlled means of calling low-level OS services within the kernel, such as those involving hardware/devices, memory, and processes. (Citation: The MITRE Corporation May 2017) These native APIs are leveraged by the OS during system boot (when other system components are not yet initialized) as well as carrying out tasks and requests during routine operations. 

Functionality provided by native APIs are often also exposed to user-mode applications via interfaces and libraries. For example, functions such as memcpy and direct operations on memory registers can be used to modify user and system memory space.

## Mitigations
- M0938: Execution Prevention

## Known Software Using This Technique
- S1006: PLC-Blaster
- S0603: Stuxnet
- S1009: Triton


---

# T0826: Loss of Availability


**ATT&CK ID:** T0826  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impact  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0826  

## Description
Adversaries may attempt to disrupt essential components or systems to prevent owner and operator from delivering products or services. (Citation: Corero) (Citation: Michael J. Assante and Robert M. Lee) (Citation: Tyson Macaulay) 

Adversaries may leverage malware to delete or encrypt critical data on HMIs, workstations, or databases.

In the 2021 Colonial Pipeline ransomware incident, pipeline operations were temporally halted on May 7th and were not fully restarted until May 12th. (Citation: Colonial Pipeline Company May 2021)

## Mitigations
- M0810: Out-of-Band Communications Channel
- M0811: Redundancy of Service
- M0953: Data Backup

## Known Software Using This Technique
- S0608: Conficker


---

# T0882: Theft of Operational Information


**ATT&CK ID:** T0882  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impact  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0882  

## Description
Adversaries may steal operational information on a production environment as a direct mission outcome for personal gain or to inform future operations. This information may include design documents, schedules, rotational data, or similar artifacts that provide insight on operations.    In the Bowman Dam incident, adversaries probed systems for operational data. (Citation: Mark Thompson March 2016) (Citation: Danny Yadron December 2015)

## Mitigations
- M0803: Data Loss Prevention
- M0809: Operational Information Confidentiality
- M0922: Restrict File and Directory Permissions
- M0941: Encrypt Sensitive Information

## Known Software Using This Technique
- S1000: ACAD/Medre.A
- S0038: Duqu
- S0143: Flame
- S0496: REvil


---

# T0849: Masquerading


**ATT&CK ID:** T0849  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Evasion  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0849  

## Description
Adversaries may use masquerading to disguise a malicious application or executable as another file, to avoid operator and engineer suspicion. Possible disguises of these masquerading files can include commonly found programs, expected vendor executables and configuration files, and other commonplace application and naming conventions. By impersonating expected and vendor-relevant files and applications, operators and engineers may not notice the presence of the underlying malicious content and possibly end up running those masquerading as legitimate functions. 

Applications and other files commonly found on Windows systems or in engineering workstations have been impersonated before. This can be as simple as renaming a file to effectively disguise it in the ICS environment.

## Mitigations
- M0922: Restrict File and Directory Permissions
- M0938: Execution Prevention
- M0945: Code Signing

## Known Software Using This Technique
- S0605: EKANS
- S0496: REvil
- S0603: Stuxnet
- S1009: Triton


---

# T0843: Program Download


**ATT&CK ID:** T0843  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Lateral Movement  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0843  

## Description
Adversaries may perform a program download to transfer a user program to a controller. 

Variations of program download, such as online edit and program append, allow a controller to continue running during the transfer and reconfiguration process without interruption to process control. However, before starting a full program download (i.e., download all) a controller may need to go into a stop state. This can have negative consequences on the physical process, especially if the controller is not able to fulfill a time-sensitive action. Adversaries may choose to avoid a download all in favor of an online edit or program append to avoid disrupting the physical process. An adversary may need to use the technique Detect Operating Mode or Change Operating Mode to make sure the controller is in the proper mode to accept a program download.

The granularity of control to transfer a user program in whole or parts is dictated by the management protocol (e.g., S7CommPlus, TriStation) and underlying controller API. Thus, program download is a high-level term for the suite of vendor-specific API calls used to configure a controllers user program memory space.  

[Modify Controller Tasking](https://attack.mitre.org/techniques/T0821) and [Modify Program](https://attack.mitre.org/techniques/T0889) represent the configuration changes that are transferred to a controller via a program download.

## Sub-techniques
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append

## Mitigations
- M0800: Authorization Enforcement
- M0801: Access Management
- M0802: Communication Authenticity
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic
- M0945: Code Signing
- M0947: Audit

## Known Software Using This Technique
- S1045: INCONTROLLER
- S1006: PLC-Blaster
- S0603: Stuxnet
- S1009: Triton


---

# T0847: Replication Through Removable Media


**ATT&CK ID:** T0847  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Initial Access  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0847  

## Description
Adversaries may move onto systems, such as those separated from the enterprise network, by copying malware to removable media which is inserted into the control systems environment. The adversary may rely on unknowing trusted third parties, such as suppliers or contractors with access privileges, to introduce the removable media. This technique enables initial access to target devices that never connect to untrusted networks, but are physically accessible.     

Operators of the German nuclear power plant, Gundremmingen, discovered malware on a facility computer not connected to the internet. (Citation: Kernkraftwerk Gundremmingen April 2016) (Citation: Trend Micro April 2016) The malware included Conficker and W32.Ramnit, which were also found on eighteen removable disk drives in the facility. (Citation: Christoph Steitz, Eric Auchard April 2016) (Citation: Catalin Cimpanu April 2016) (Citation: Peter Dockrill April 2016) (Citation: Lee Mathews April 2016) (Citation: Sean Gallagher April 2016) (Citation: Dark Reading Staff April 2016) The plant has since checked for infection and cleaned up more than 1,000 computers. (Citation: BBC April 2016) An ESET researcher commented that internet disconnection does not guarantee system safety from infection or payload execution. (Citation: ESET April 2016)

## Mitigations
- M0928: Operating System Configuration
- M0934: Limit Hardware Installation
- M0942: Disable or Remove Feature or Program

## Known Software Using This Technique
- S0608: Conficker
- S0603: Stuxnet


---

# T0846.002: Broadcast Discovery

**Parent technique:** T0846
**ATT&CK ID:** T0846.002  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Discovery  
**Reference:** https://attack.mitre.org/techniques/T0846/002  

## Description
Adversaries may perform broadcast discovery requests to enumerate systems and devices on a network. Broadcast discovery works by one system or device sending messages to all systems and devices on a network (or subnet) and then waiting for a response. If a response is received that means the system or device that responded is live and can communicate over that protocol. Adversaries may leverage different protocols supported on the network for sending broadcast messages. 

Some common OT protocols that have broadcast discovery mechanisms are Building Automation and Control Network (BACNet) Who-Is requests, Common Industrial Protocol (CIP) List Identity User Datagram Protocol (UDP) broadcast requests, and Siemens S7 broadcast identification requests.(Citation: Broadcasting BACnet)(Citation: Cisco Active Discovery)

## Mitigations
- M0814: Static Network Configuration
- M0930: Network Segmentation

## Known Software Using This Technique
- S1009: Triton


---

# T0852: Screen Capture


**ATT&CK ID:** T0852  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Collection  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0852  

## Description
Adversaries may attempt to perform screen capture of devices in the control system environment. Screenshots may be taken of workstations, HMIs, or other devices that display environment-relevant process, device, reporting, alarm, or related data. These device displays may reveal information regarding the ICS process, layout, control, and related schematics. In particular, an HMI can provide a lot of important industrial process information. (Citation: ICS-CERT October 2017) Analysis of screen captures may provide the adversary with an understanding of intended operations and interactions between critical devices.

## Mitigations
- M0816: Mitigation Limited or Not Effective

## Known Threat Groups Using This Technique
- G1000: ALLANITE
- G0064: APT33


---

# T0859: Valid Accounts


**ATT&CK ID:** T0859  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Persistence, Lateral Movement  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0859  

## Description
Adversaries may steal the credentials of a specific user or service account using credential access techniques. In some cases, default credentials for control system devices may be publicly available. Compromised credentials may be used to bypass access controls placed on various resources on hosts and within the network, and may even be used for persistent access to remote systems. Compromised and default credentials may also grant an adversary increased privilege to specific systems and devices or access to restricted areas of the network. Adversaries may choose not to use malware or tools, in conjunction with the legitimate access those credentials provide, to make it harder to detect their presence or to control devices and send legitimate commands in an unintended way. 

Adversaries may also create accounts, sometimes using predefined account names and passwords, to provide a means of backup access for persistence. (Citation: Booz Allen Hamilton) 

The overlap of credentials and permissions across a network of systems is of concern because the adversary may be able to pivot across accounts and systems to reach a high level of access (i.e., domain or enterprise administrator)  and possibly between the enterprise and operational technology environments. Adversaries may be able to leverage valid credentials from one system to gain access to another system.

## Mitigations
- M0801: Access Management
- M0913: Application Developer Guidance
- M0915: Active Directory Configuration
- M0918: User Account Management
- M0926: Privileged Account Management
- M0927: Password Policies
- M0932: Multi-factor Authentication
- M0936: Account Use Policies
- M0937: Filter Network Traffic
- M0947: Audit

## Known Threat Groups Using This Technique
- G1000: ALLANITE
- G0049: OilRig

## Known Software Using This Technique
- S0089: BlackEnergy
- S1045: INCONTROLLER


---

# T0890: Exploitation for Privilege Escalation


**ATT&CK ID:** T0890  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Privilege Escalation  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0890  

## Description
Adversaries may exploit software vulnerabilities in an attempt to elevate privileges. Exploitation of a software vulnerability occurs when an adversary takes advantage of a programming error in a program, service, or within the operating system software or kernel itself to execute adversary-controlled code. Security constructs such as permission levels will often hinder access to information and use of certain techniques, so adversaries will likely need to perform privilege escalation to include use of software exploitation to circumvent those restrictions. (Citation: The MITRE Corporation) 

When initially gaining access to a system, an adversary may be operating within a lower privileged process which will prevent them from accessing certain resources on the system. Vulnerabilities may exist, usually in operating system components and software commonly running at higher permissions, that can be exploited to gain higher levels of access on the system. This could enable someone to move from unprivileged or user level permissions to SYSTEM or root permissions depending on the component that is vulnerable. This may be a necessary step for an adversary compromising an endpoint system that has been properly configured and limits other privilege escalation methods. (Citation: The MITRE Corporation)

## Mitigations
- M0919: Threat Intelligence Program
- M0948: Application Isolation and Sandboxing
- M0950: Exploit Protection
- M0951: Update Software

## Known Software Using This Technique
- S1045: INCONTROLLER
- S1009: Triton


---

# T0846: Remote System Discovery


**ATT&CK ID:** T0846  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Discovery  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0846  

## Description
Adversaries may attempt to get a listing of other systems by IP address, hostname, or other logical identifier on a network that may be used for subsequent Lateral Movement or Discovery techniques. Functionality could exist within adversary tools to enable this, but utilities available on the operating system or vendor software could also be used.(Citation: Enterprise ATT&CK January 2018)

## Sub-techniques
- T0846.001: Port Scan
- T0846.002: Broadcast Discovery
- T0846.003: Multicast Discovery

## Mitigations
- M0814: Static Network Configuration

## Known Software Using This Technique
- S0093: Backdoor.Oldrea
- S1045: INCONTROLLER
- S0604: Industroyer


---

# T0884: Connection Proxy


**ATT&CK ID:** T0884  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Command And Control  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0884  

## Description
Adversaries may use a connection proxy to direct network traffic between systems or act as an intermediary for network communications.

The definition of a proxy can also be expanded to encompass trust relationships between networks in peer-to-peer, mesh, or trusted connections between networks consisting of hosts or systems that regularly communicate with each other.

The network may be within a single organization or across multiple organizations with trust relationships. Adversaries could use these types of relationships to manage command and control communications, to reduce the number of simultaneous outbound network connections, to provide resiliency in the face of connection loss, or to ride over existing trusted communications paths between victims to avoid suspicion. (Citation: Enterprise ATT&CK January 2018)

## Mitigations
- M0807: Network Allowlists
- M0920: SSL/TLS Inspection
- M0931: Network Intrusion Prevention
- M0937: Filter Network Traffic

## Known Threat Groups Using This Technique
- G0034: Sandworm Team

## Known Software Using This Technique
- S1045: INCONTROLLER
- S0604: Industroyer


---

# T0843.002: Online Edit

**Parent technique:** T0843
**ATT&CK ID:** T0843.002  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Lateral Movement  
**Reference:** https://attack.mitre.org/techniques/T0843/002  

## Description
Adversaries may execute an online edit of a PLC to update parts of an existing program. It does not require stopping the PLC which allows it to continue running during transfer and reconfiguration without interruption to process control. Adversaries may leverage this approach to minimize downtime and evade detection. 

The ability to perform an online edit to the PLC typically relies on access to a workstation with the vendor-specific PLC programming software installed.

## Mitigations
- M0800: Authorization Enforcement
- M0801: Access Management
- M0802: Communication Authenticity
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic
- M0945: Code Signing
- M0947: Audit


---

# T0869: Standard Application Layer Protocol


**ATT&CK ID:** T0869  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Command And Control  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0869  

## Description
Adversaries may establish command and control capabilities over commonly used application layer protocols such as HTTP(S), OPC, RDP, telnet, DNP3, and modbus. These protocols may be used to disguise adversary actions as benign network traffic. Standard protocols may be seen on their associated port or in some cases over a non-standard port.  Adversaries may use these protocols to reach out of the network for command and control, or in some cases to other infected devices within the network.

## Mitigations
- M0807: Network Allowlists
- M0930: Network Segmentation
- M0931: Network Intrusion Prevention

## Known Threat Groups Using This Technique
- G0049: OilRig

## Known Software Using This Technique
- S0089: BlackEnergy
- S1165: FrostyGoop
- S1045: INCONTROLLER
- S0496: REvil
- S0603: Stuxnet
- S1009: Triton


---

# T1692: Unauthorized Message


**ATT&CK ID:** T1692  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Evasion, Impair Process Control  
**Reference:** https://attack.mitre.org/techniques/T1692  

## Description
Adversaries may send unauthorized messages to ICS systems and devices to evade defenses or manipulate processes. Unauthorized messages can be categorized as either reporting messages that contain telemetry data about the current state of systems, devices, and processes or as command messages which instruct systems and devices on how to operate. By injecting unauthorized messages, adversaries can make it appear as if everything is working correctly when it isn’t, trigger alarms to misdirect personnel or impact processes, and manipulate controls to disrupt processes.(Citation: Bonnie Zhu, Anthony Joseph, Shankar Sastry 2011)

Adversaries may send unauthorized messages in an ICS environment using software found within the environment (living-off-the-land, vendor-specific interfaces, etc.), custom tooling leveraging OT protocols and libraries, or by positioning themselves between systems and devices and injecting messages into the communications such as the case with an [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T0830) attack.

## Sub-techniques
- T1692.001: Command Message
- T1692.002: Reporting Message

## Mitigations
- M0802: Communication Authenticity
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic


---

# T0886: Remote Services


**ATT&CK ID:** T0886  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Initial Access, Lateral Movement  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0886  

## Description
Adversaries may leverage remote services to move between assets and network segments. These services are often used to allow operators to interact with systems remotely within the network, some examples are RDP, SMB, SSH, and other similar mechanisms. (Citation: Blake Johnson, Dan Caban, Marina Krotofil, Dan Scali, Nathan Brubaker, Christopher Glyer December 2017) (Citation: Dragos December 2017) (Citation: Joe Slowik April 2019) 

Remote services could be used to support remote access, data transmission, authentication, name resolution, and other remote functions. Further, remote services may be necessary to allow operators and administrators to configure systems within the network from their engineering or management workstations. An adversary may use this technique to access devices which may be dual-homed (Citation: Blake Johnson, Dan Caban, Marina Krotofil, Dan Scali, Nathan Brubaker, Christopher Glyer December 2017) to multiple network segments, and can be used for [Program Download](https://attack.mitre.org/techniques/T0843) or to execute attacks on control devices directly through [Valid Accounts](https://attack.mitre.org/techniques/T0859).

Specific remote services (RDP & VNC) may be a precursor to enable [Graphical User Interface](https://attack.mitre.org/techniques/T0823) execution on devices such as HMIs or engineering workstation software.

Based on incident data, CISA and FBI assessed that Chinese state-sponsored actors also compromised various authorized remote access channels, including systems designed to transfer data and/or allow access between corporate and ICS networks.  (Citation: CISA AA21-201A Pipeline Intrusion July 2021)

## Mitigations
- M0800: Authorization Enforcement
- M0801: Access Management
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0918: User Account Management
- M0927: Password Policies
- M0930: Network Segmentation
- M0937: Filter Network Traffic

## Known Software Using This Technique
- S1045: INCONTROLLER
- S0496: REvil
- S0603: Stuxnet


---

# T0813: Denial of Control


**ATT&CK ID:** T0813  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impact  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0813  

## Description
Adversaries may cause a denial of control to temporarily prevent operators and engineers from interacting with process controls. An adversary may attempt to deny process control access to cause a temporary loss of communication with the control device or to prevent operator adjustment of process controls. An affected process may still be operating during the period of control loss, but not necessarily in a desired state. (Citation: Corero) (Citation: Michael J. Assante and Robert M. Lee) (Citation: Tyson Macaulay)

In the 2017 Dallas Siren incident operators were unable to disable the false alarms from the Office of Emergency Management headquarters. (Citation: Mark Loveless April 2017)

## Mitigations
- M0810: Out-of-Band Communications Channel
- M0811: Redundancy of Service
- M0953: Data Backup

## Known Software Using This Technique
- S0604: Industroyer


---

# T0838: Modify Alarm Settings


**ATT&CK ID:** T0838  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0838  

## Description
Adversaries may modify alarm settings to prevent alerts that may inform operators of their presence or to prevent responses to dangerous and unintended scenarios. Reporting messages are a standard part of data acquisition in control systems. Reporting messages are used as a way to transmit system state information and acknowledgements that specific actions have occurred. These messages provide vital information for the management of a physical process, and keep operators, engineers, and administrators aware of the state of system devices and physical processes. 

If an adversary is able to change the reporting settings, certain events could be prevented from being reported. This type of modification can also prevent operators or devices from performing actions to keep the system in a safe state. If critical reporting messages cannot trigger these actions then a [Impact](https://attack.mitre.org/tactics/TA0105) could occur. 

In ICS environments, the adversary may have to use [Alarm Suppression](https://attack.mitre.org/techniques/T0878) or contend with multiple alarms and/or alarm propagation to achieve a specific goal to evade detection or prevent intended responses from occurring. (Citation: Jos Wetzels, Marina Krotofil 2019)  Methods of suppression often rely on modification of alarm settings, such as modifying in memory code to fixed values or tampering with assembly level instruction code.

## Mitigations
- M0800: Authorization Enforcement
- M0801: Access Management
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0918: User Account Management
- M0930: Network Segmentation


---

# T0885: Commonly Used Port


**ATT&CK ID:** T0885  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Command And Control  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0885  

## Description
Adversaries may communicate over a commonly used port to bypass firewalls or network detection systems and to blend in with normal network activity, to avoid more detailed inspection. They may use the protocol associated with the port, or a completely different protocol. They may use commonly open ports, such as the examples provided below. 
 
 * TCP:80 (HTTP) 
 * TCP:443 (HTTPS) 
 * TCP/UDP:53 (DNS) 
 * TCP:1024-4999 (OPC on XP/Win2k3) 
 * TCP:49152-65535 (OPC on Vista and later) 
 * TCP:23 (TELNET) 
 * UDP:161 (SNMP) 
 * TCP:502 (MODBUS) 
 * TCP:102 (S7comm/ISO-TSAP) 
 * TCP:20000 (DNP3) 
 * TCP:44818 (Ethernet/IP)

## Mitigations
- M0804: Human User Authentication
- M0930: Network Segmentation
- M0931: Network Intrusion Prevention
- M0942: Disable or Remove Feature or Program

## Known Software Using This Technique
- S1165: FrostyGoop
- S0603: Stuxnet
- S1009: Triton


---

# T0873: Project File Infection


**ATT&CK ID:** T0873  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Persistence  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0873  

## Description
Adversaries may attempt to infect project files with malicious code. These project files may consist of objects, program organization units, variables such as tags, documentation, and other configurations needed for PLC programs to function.(Citation: Beckhoff) Using built in functions of the engineering software, adversaries may be able to download an infected program to a PLC in the operating environment enabling further [Execution](https://attack.mitre.org/tactics/TA0104) and [Persistence](https://attack.mitre.org/tactics/TA0110) techniques.(Citation: PLCdev) 

Adversaries may export their own code into project files with conditions to execute at specific intervals.(Citation: Nicolas Falliere, Liam O Murchu, Eric Chien February 2011) Malicious programs allow adversaries control of all aspects of the process enabled by the PLC. Once the project file is downloaded to a PLC the workstation device may be disconnected with the infected project file still executing.(Citation: PLCdev)

## Sub-techniques
- T0873.001: Siemens Project File Format

## Mitigations
- M0922: Restrict File and Directory Permissions
- M0941: Encrypt Sensitive Information
- M0945: Code Signing
- M0947: Audit


---

# T0840: Network Connection Enumeration


**ATT&CK ID:** T0840  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Discovery  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0840  

## Description
Adversaries may perform network connection enumeration to discover information about device communication patterns. If an adversary can inspect the state of a network connection with tools, such as Netstat(Citation: Netstat), in conjunction with [System Firmware](https://attack.mitre.org/techniques/T0857), then they can determine the role of certain devices on the network  (Citation: MITRE). The adversary can also use [Network Sniffing](https://attack.mitre.org/techniques/T0842) to watch network traffic for details about the source, destination, protocol, and content.

## Mitigations
- M0816: Mitigation Limited or Not Effective

## Known Software Using This Technique
- S0605: EKANS
- S0604: Industroyer


---

# T0867: Lateral Tool Transfer


**ATT&CK ID:** T0867  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Lateral Movement  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0867  

## Description
Adversaries may transfer tools or other files from one system to another to stage adversary tools or other files over the course of an operation. (Citation: Enterprise ATT&CK) Copying of files may also be performed laterally between internal victim systems to support Lateral Movement with remote Execution using inherent file sharing protocols such as file sharing over SMB to connected network shares. (Citation: Enterprise ATT&CK)

In control systems environments, malware may use SMB and other file sharing protocols to move laterally through industrial networks.

## Mitigations
- M0931: Network Intrusion Prevention

## Known Software Using This Technique
- S0606: Bad Rabbit
- S1045: INCONTROLLER
- S0368: NotPetya
- S0603: Stuxnet
- S0366: WannaCry


---

# T0883: Internet Accessible Device


**ATT&CK ID:** T0883  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Initial Access  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0883  

## Description
Adversaries may gain access into industrial environments through systems exposed directly to the internet for remote access rather than through [External Remote Services](https://attack.mitre.org/techniques/T0822). Internet Accessible Devices are exposed to the internet unintentionally or intentionally without adequate protections. This may allow for adversaries to move directly into the control system network. Access onto these devices is accomplished without the use of exploits, these would be represented within the [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T0819) technique.

Adversaries may leverage built in functions for remote access which may not be protected or utilize minimal legacy protections that may be targeted. (Citation: NCCIC January 2014) These services may be discoverable through the use of online scanning tools. 

In the case of the Bowman dam incident, adversaries leveraged access to the dam control network through a cellular modem. Access to the device was protected by password authentication, although the application was vulnerable to brute forcing. (Citation: NCCIC January 2014) (Citation: Danny Yadron December 2015) (Citation: Mark Thompson March 2016)

In Trend Micros manufacturing deception operations adversaries were detected leveraging direct internet access to an ICS environment through the exposure of operational protocols such as Siemens S7, Omron FINS, and EtherNet/IP, in addition to misconfigured VNC access. (Citation: Stephen Hilt, Federico Maggi, Charles Perine, Lord Remorin, Martin Rsler, and Rainer Vosseler)

## Mitigations
- M0930: Network Segmentation

## Known Software Using This Technique
- S1157: Fuxnet


---

# T0893: Data from Local System


**ATT&CK ID:** T0893  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Collection  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0893  

## Description
Adversaries may target and collect data from local system sources, such as file systems, configuration files, or local databases. This can include sensitive data such as specifications, schematics, or diagrams of control system layouts, devices, and processes.

Adversaries may do this using [Command-Line Interface](https://attack.mitre.org/techniques/T0807) or [Scripting](https://attack.mitre.org/techniques/T0853) techniques to interact with the file system to gather information. Adversaries may also use [Automated Collection](https://attack.mitre.org/techniques/T0802) on the local system.

## Mitigations
- M0803: Data Loss Prevention
- M0917: User Training
- M0922: Restrict File and Directory Permissions
- M0941: Encrypt Sensitive Information

## Known Software Using This Technique
- S1000: ACAD/Medre.A
- S0038: Duqu
- S0143: Flame


---

# T0892: Change Credential


**ATT&CK ID:** T0892  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0892  

## Description
Adversaries may modify software and device credentials to prevent operator and responder access. Depending on the device, the modification or addition of this password could prevent any device configuration actions from being accomplished and may require a factory reset or replacement of hardware. These credentials are often built-in features provided by the device vendors as a means to restrict access to management interfaces.

An adversary with access to valid or hardcoded credentials could change the credential to prevent future authorized device access. Change Credential may be especially damaging when paired with other techniques such as Modify Program, Data Destruction, or Modify Controller Tasking. In these cases, a device’s configuration may be destroyed or include malicious actions for the process environment, which cannot not be removed through normal device configuration actions. 

Additionally, recovery of the device and original configuration may be difficult depending on the features provided by the device. In some cases, these passwords cannot be removed onsite and may require that the device be sent back to the vendor for additional recovery steps.


A chain of incidents occurred in Germany, where adversaries locked operators out of their building automation system (BAS) controllers by enabling a previously unset BCU key. (Citation: German BAS Lockout Dec 2021)

## Mitigations
- M0811: Redundancy of Service
- M0927: Password Policies
- M0953: Data Backup


---

# T1695: Block Communications


**ATT&CK ID:** T1695  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Reference:** https://attack.mitre.org/techniques/T1695  

## Description
Operational technology communications occur over serial COM, Ethernet, Wi-Fi, cellular (4G/5G), and satellite mediums. Adversaries may block communications to prevent reporting messages and command messages from reaching their intended target devices disrupting processes, operations, and causing cyber-physical impacts.(Citation: Bonnie Zhu, Anthony Joseph, Shankar Sastry 2011)  

Adversaries may block communications by either making modifications to software ([System Firmware](https://attack.mitre.org/techniques/T0857), [Module Firmware](https://attack.mitre.org/techniques/T0839), [Hooking](https://attack.mitre.org/techniques/T0874), and [Rootkit](https://attack.mitre.org/techniques/T0851)) and services ([Service Stop](https://attack.mitre.org/techniques/T0881), [Denial of Service](https://attack.mitre.org/techniques/T0814)) on systems and devices or by positioning themselves between systems and devices and intercepting and blocking the communications such as the case with an [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T0830) attack.

## Sub-techniques
- T1695.001: Serial COM
- T1695.002: Ethernet
- T1695.003: Wi-Fi

## Mitigations
- M0807: Network Allowlists
- M0810: Out-of-Band Communications Channel
- M0930: Network Segmentation


---

# T0889: Modify Program


**ATT&CK ID:** T0889  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Persistence  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0889  

## Description
Adversaries may modify or add a program on a controller to affect how it interacts with the physical process, peripheral devices and other hosts on the network. Modification to controller programs can be accomplished using a Program Download in addition to other types of program modification such as online edit and program append. 

Program modification encompasses the addition and modification of instructions and logic contained in Program Organization Units (POU)  (Citation: IEC February 2013) and similar programming elements found on controllers. This can include, for example, adding new functions to a controller, modifying the logic in existing functions and making new calls from one function to another. 

Some programs may allow an adversary to interact directly with the native API of the controller to take advantage of obscure features or vulnerabilities.

## Mitigations
- M0800: Authorization Enforcement
- M0804: Human User Authentication
- M0945: Code Signing
- M0947: Audit

## Known Software Using This Technique
- S1006: PLC-Blaster
- S0603: Stuxnet


---

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


---

# TA0111: Privilege Escalation

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0111  

## Description
The adversary is trying to gain higher-level permissions.

Privilege Escalation consists of techniques that adversaries use to gain higher-level permissions on a system or network. Adversaries can often enter and explore a network with unprivileged access but require elevated permissions to follow through on their objectives. Common approaches are to take advantage of system weaknesses, misconfigurations, and vulnerabilities.

## Techniques in This Tactic
- T0874: Hooking
- T0890: Exploitation for Privilege Escalation


---

# TA0109: Lateral Movement

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0109  

## Description
The adversary is trying to move through your ICS environment.

Lateral Movement consists of techniques that adversaries use to enter and control remote systems on a network. These techniques abuse default credentials, known accounts, and vulnerable services, and may also leverage dual-homed devices and systems that reside on both the IT and OT networks. The adversary uses these techniques to pivot to their next point in the environment, positioning themselves to where they want to be or think they should be. Following through on their primary objective often requires [Discovery](https://attack.mitre.org/tactics/TA0102) of the network and [Collection](https://attack.mitre.org/tactics/TA0100) to develop awareness of unique ICS devices and processes, in order to find their target and subsequently gain access to it. Reaching this objective often involves pivoting through multiple systems, devices, and accounts. Adversaries may install their own remote tools to accomplish Lateral Movement or leverage default tools, programs, and manufacturer set or other legitimate credentials native to the network, which may be stealthier.

## Techniques in This Tactic
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0859: Valid Accounts
- T0866: Exploitation of Remote Services
- T0867: Lateral Tool Transfer
- T0886: Remote Services
- T1694: Insecure Credentials
- T1694.001: Default Credentials
- T1694.002: Hardcoded Credentials


---

# TA0102: Discovery

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0102  

## Description
The adversary is locating information to assess and identify their targets in your environment.

Discovery consists of techniques that adversaries use to survey your ICS environment and gain knowledge about the internal network, control system devices, and how their processes interact. These techniques help adversaries observe the environment and determine next steps for target selection and Lateral Movement. They also allow adversaries to explore what they can control and gain insight on interactions between various control system processes. Discovery techniques are often an act of progression into the environment which enable the adversary to orient themselves before deciding how to act. Adversaries may use Discovery techniques that result in Collection, to help determine how available resources benefit their current objective. A combination of native device communications and functions, and custom tools are often used toward this post-compromise information-gathering objective.

## Techniques in This Tactic
- T0840: Network Connection Enumeration
- T0842: Network Sniffing
- T0846: Remote System Discovery
- T0846.001: Port Scan
- T0846.002: Broadcast Discovery
- T0846.003: Multicast Discovery
- T0887: Wireless Sniffing
- T0888: Remote System Information Discovery


---

# TA0108: Initial Access

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0108  

## Description
The adversary is trying to get into your ICS environment.

Initial Access consists of techniques that adversaries may use as entry vectors to gain an initial foothold within an ICS environment. These techniques include compromising operational technology assets, IT resources in the OT network, and external remote services and websites. They may also target third party entities and users with privileged access. In particular, these initial access footholds may include devices and communication mechanisms with access to and privileges in both the IT and OT environments. IT resources in the OT environment are also potentially vulnerable to the same attacks as enterprise IT systems. Trusted third parties of concern may include vendors, maintenance personnel, engineers, external integrators, and other outside entities involved in expected ICS operations. Vendor maintained assets may include physical devices, software, and operational equipment. Initial access techniques may also leverage outside devices, such as radios, controllers, or removable media, to remotely interfere with and possibly infect OT operations.

## Techniques in This Tactic
- T0817: Drive-by Compromise
- T0819: Exploit Public-Facing Application
- T0822: External Remote Services
- T0847: Replication Through Removable Media
- T0848: Rogue Master
- T0860: Wireless Compromise
- T0862: Supply Chain Compromise
- T0864: Transient Cyber Asset
- T0865: Spearphishing Attachment
- T0866: Exploitation of Remote Services
- T0883: Internet Accessible Device
- T0886: Remote Services


---

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


---

# TA0110: Persistence

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0110  

## Description
The adversary is trying to maintain their foothold in your ICS environment.

Persistence consists of techniques that adversaries use to maintain access to ICS systems and devices across restarts, changed credentials, and other interruptions that could cut off their access. Techniques used for persistence include any access, action, or configuration changes that allow them to secure their ongoing activity and keep their foothold on systems. This may include replacing or hijacking legitimate code, firmware, and other project files, or adding startup code and downloading programs onto devices.

## Techniques in This Tactic
- T0859: Valid Accounts
- T0873: Project File Infection
- T0873.001: Siemens Project File Format
- T0889: Modify Program
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware
- T1694: Insecure Credentials
- T1694.001: Default Credentials
- T1694.002: Hardcoded Credentials


---

# TA0104: Execution

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0104  

## Description
The adversary is trying to run code or manipulate system functions, parameters, and data in an unauthorized way.

Execution consists of techniques that result in adversary-controlled code running on a local or remote system, device, or other asset. This execution may also rely on unknowing end users or the manipulation of device operating modes to run. Adversaries may infect remote targets with programmed executables or malicious project files that operate according to specified behavior and may alter expected device behavior in subtle ways. Commands for execution may also be issued from command-line interfaces, APIs, GUIs, or other available interfaces. Techniques that run malicious code may also be paired with techniques from other tactics, particularly to aid network [Discovery](https://attack.mitre.org/tactics/TA0102) and [Collection](https://attack.mitre.org/tactics/TA0100), impact operations, and inhibit response functions.

## Techniques in This Tactic
- T0807: Command-Line Interface
- T0821: Modify Controller Tasking
- T0823: Graphical User Interface
- T0834: Native API
- T0853: Scripting
- T0858: Change Operating Mode
- T0863: User Execution
- T0871: Execution through API
- T0874: Hooking
- T0895: Autorun Image


---

# TA0101: Command and Control

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0101  

## Description
The adversary is trying to communicate with and control compromised systems, controllers, and platforms with access to your ICS environment.

Command and Control consists of techniques that adversaries use to communicate with and send commands to compromised systems, devices, controllers, and platforms with specialized applications used in ICS environments. Examples of these specialized communication devices include human machine interfaces (HMIs), data historians, SCADA servers, and engineering workstations (EWS). Adversaries often seek to use commonly available resources and mimic expected network traffic to avoid detection and suspicion. For instance, commonly used ports and protocols in ICS environments, and even expected IT resources, depending on the target network. Command and Control may be established to varying degrees of stealth, often depending on the victim’s network structure and defenses.

## Techniques in This Tactic
- T0869: Standard Application Layer Protocol
- T0884: Connection Proxy
- T0885: Commonly Used Port


---

# TA0100: Collection

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0100  

## Description
The adversary is trying to gather data of interest and domain knowledge on your ICS environment to inform their goal.

Collection consists of techniques adversaries use to gather domain knowledge and obtain contextual feedback in an ICS environment. This tactic is often performed as part of [Discovery](https://attack.mitre.org/tactics/TA0102), to compile data on control systems and targets of interest that may be used to follow through on the adversary’s objective. Examples of these techniques include observing operation states, capturing screenshots, identifying unique device roles, and gathering system and diagram schematics. Collection of this data can play a key role in planning, executing, and even revising an ICS-targeted attack. Methods of collection depend on the categories of data being targeted, which can include protocol specific, device specific, and process specific configurations and functionality. Information collected may pertain to a combination of system, supervisory, device, and network related data, which conceptually fall under high, medium, and low levels of plan operations. For example, information repositories on plant data at a high level or device specific programs at a low level. Sensitive floor plans, vendor device manuals, and other references may also be at risk and exposed on the internet or otherwise publicly accessible.

## Techniques in This Tactic
- T0801: Monitor Process State
- T0802: Automated Collection
- T0811: Data from Information Repositories
- T0830: Adversary-in-the-Middle
- T0845: Program Upload
- T0852: Screen Capture
- T0861: Point & Tag Identification
- T0868: Detect Operating Mode
- T0877: I/O Image
- T0887: Wireless Sniffing
- T0893: Data from Local System


---

# TA0103: Evasion

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0103  

## Description
The adversary is trying to avoid security defenses.

Evasion consists of techniques that adversaries use to avoid technical defenses throughout their campaign. Techniques used for evasion include removal of indicators of compromise, spoofing communications, and exploiting software vulnerabilities. Adversaries may also leverage and abuse trusted devices and processes to hide their activity, possibly by masquerading as master devices or native software. Methods of defense evasion for this purpose are often more passive in nature.

## Techniques in This Tactic
- T0820: Exploitation for Evasion
- T0849: Masquerading
- T0851: Rootkit
- T0858: Change Operating Mode
- T0872: Indicator Removal on Host
- T0894: System Binary Proxy Execution
- T1692: Unauthorized Message
- T1692.001: Command Message
- T1692.002: Reporting Message


---

# TA0106: Impair Process Control

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0106  

## Description
The adversary is trying to manipulate, disable, or damage physical control processes.

Impair Process Control consists of techniques that adversaries use to disrupt control logic and cause determinantal effects to processes being controlled in the target environment. Targets of interest may include active procedures or parameters that manipulate the physical environment. These techniques can also include prevention or manipulation of reporting elements and control logic. If an adversary has modified process functionality, then they may also obfuscate the results, which are often self-revealing in their impact on the outcome of a product or the environment. The direct physical control these techniques exert may also threaten the safety of operators and downstream users, which can prompt response mechanisms. Adversaries may follow up with or use [Inhibit Response Function](https://attack.mitre.org/tactics/TA0107) techniques in tandem, to assist with the successful abuse of control processes to result in [Impact](https://attack.mitre.org/tactics/TA0105).

## Techniques in This Tactic
- T0806: Brute Force I/O
- T0836: Modify Parameter
- T1692: Unauthorized Message
- T1692.001: Command Message
- T1692.002: Reporting Message
- T1693: Modify Firmware
- T1693.001: System Firmware
- T1693.002: Module Firmware
