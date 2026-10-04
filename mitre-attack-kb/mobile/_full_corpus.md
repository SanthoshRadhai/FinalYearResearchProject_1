# MITRE ATT&CK — MOBILE domain


---

# C0016: Operation Dust Storm

**Type:** campaign  
**Reference:** https://attack.mitre.org/campaigns/C0016  
**Aliases:** Operation Dust Storm  

## Description
[Operation Dust Storm](https://attack.mitre.org/campaigns/C0016) was a long-standing persistent cyber espionage campaign that targeted multiple industries in Japan, South Korea, the United States, Europe, and several Southeast Asian countries. By 2015, the [Operation Dust Storm](https://attack.mitre.org/campaigns/C0016) threat actors shifted from government and defense-related intelligence targets to Japanese companies or Japanese subdivisions of larger foreign organizations supporting Japan's critical infrastructure, including electricity generation, oil and natural gas, finance, transportation, and construction.(Citation: Cylance Dust Storm)

[Operation Dust Storm](https://attack.mitre.org/campaigns/C0016) threat actors also began to use Android backdoors in their operations by 2015, with all identified victims at the time residing in Japan or South Korea.(Citation: Cylance Dust Storm)


---

# C0033: C0033

**Type:** campaign  
**Reference:** https://attack.mitre.org/campaigns/C0033  
**Aliases:** C0033  

## Description
[C0033](https://attack.mitre.org/campaigns/C0033) was a [PROMETHIUM](https://attack.mitre.org/groups/G0056) campaign during which they used [StrongPity](https://attack.mitre.org/software/S0491) to target Android users. [C0033](https://attack.mitre.org/campaigns/C0033) was the first publicly documented mobile campaign for [PROMETHIUM](https://attack.mitre.org/groups/G0056), who previously used Windows-based techniques.(Citation: welivesec_strongpity)


---

# C0054: Operation Triangulation

**Type:** campaign  
**Reference:** https://attack.mitre.org/campaigns/C0054  
**Aliases:** Operation Triangulation  

## Description
[Operation Triangulation](https://attack.mitre.org/campaigns/C0054) is a mobile campaign targeting iOS devices.(Citation: SecureList OpTriangulation 01Jun2023) The unidentified actors used zero-click exploits in iMessage attachments to gain [Initial Access](https://attack.mitre.org/tactics/TA0027), then executed exploits and validators, such as [Binary Validator](https://attack.mitre.org/software/S1215) before finally executing the [TriangleDB](https://attack.mitre.org/software/S1216) implant.


---

# M1006: Use Recent OS Version

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1006  

## Description
New mobile operating system versions bring not only patches against discovered vulnerabilities but also often bring security architecture improvements that provide resilience against potential vulnerabilities or weaknesses that have not yet been discovered. They may also bring improvements that block use of observed adversary techniques.

## Techniques Mitigated
- T1407: Download New Code at Runtime
- T1409: Stored Application Data
- T1414: Clipboard Data
- T1417: Input Capture
- T1417.002: GUI Input Capture
- T1418: Software Discovery
- T1418.001: Security Software Discovery
- T1420: File and Directory Discovery
- T1422: System Network Configuration Discovery
- T1422.002: Wi-Fi Discovery
- T1424: Process Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1458: Replication Through Removable Media
- T1512: Video Capture
- T1577: Compromise Application Executable
- T1624: Event Triggered Execution
- T1624.001: Broadcast Receivers
- T1626.001: Device Administrator Permissions
- T1627: Execution Guardrails
- T1627.001: Geofencing
- T1628.001: Suppress Application Icon
- T1629.001: Prevent Application Removal
- T1629.002: Device Lockout
- T1632: Subvert Trust Controls
- T1632.001: Code Signing Policy Modification
- T1635: Steal Application Access Token
- T1635.001: URI Hijacking
- T1636: Protected User Data
- T1636.005: Accounts
- T1638: Adversary-in-the-Middle
- T1641: Data Manipulation
- T1641.001: Transmitted Data Manipulation
- T1642: Endpoint Denial of Service
- T1661: Application Versioning


---

# M1013: Application Developer Guidance

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1013  

## Description
Application Developer Guidance focuses on providing developers with the knowledge, tools, and best practices needed to write secure code, reduce vulnerabilities, and implement secure design principles. By integrating security throughout the software development lifecycle (SDLC), this mitigation aims to prevent the introduction of exploitable weaknesses in applications, systems, and APIs. This mitigation can be implemented through the following measures:
 
Preventing SQL Injection (Secure Coding Practice):

- Implementation: Train developers to use parameterized queries or prepared statements instead of directly embedding user input into SQL queries.
- Use Case: A web application accepts user input to search a database. By sanitizing and validating user inputs, developers can prevent attackers from injecting malicious SQL commands.

Cross-Site Scripting (XSS) Mitigation:

- Implementation: Require developers to implement output encoding for all user-generated content displayed on a web page.
- Use Case: An e-commerce site allows users to leave product reviews. Properly encoding and escaping user inputs prevents malicious scripts from being executed in other users’ browsers.

Secure API Design:

- Implementation: Train developers to authenticate all API endpoints and avoid exposing sensitive information in API responses.
- Use Case: A mobile banking application uses APIs for account management. By enforcing token-based authentication for every API call, developers reduce the risk of unauthorized access.

Static Code Analysis in the Build Pipeline:

- Implementation: Incorporate tools into CI/CD pipelines to automatically scan for vulnerabilities during the build process.
- Use Case: A fintech company integrates static analysis tools to detect hardcoded credentials in their source code before deployment.

Threat Modeling in the Design Phase:

- Implementation: Use frameworks like STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) to assess threats during application design.
- Use Case: Before launching a customer portal, a SaaS company identifies potential abuse cases, such as session hijacking, and designs mitigations like secure session management.

**Tools for Implementation**:

- Static Code Analysis Tools: Use tools that can scan for known vulnerabilities in source code.
- Dynamic Application Security Testing (DAST): Use tools like Burp Suite or OWASP ZAP to simulate runtime attacks and identify vulnerabilities.
- Secure Frameworks: Recommend secure-by-default frameworks (e.g., Django for Python, Spring Security for Java) that enforce security best practices.

## Techniques Mitigated
- T1474: Supply Chain Compromise
- T1474.001: Compromise Software Dependencies and Development Tools
- T1513: Screen Capture
- T1517: Access Notifications
- T1626: Abuse Elevation Control Mechanism
- T1635: Steal Application Access Token
- T1635.001: URI Hijacking


---

# M1012: Enterprise Policy

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1012  

## Description
An enterprise mobility management (EMM), also known as mobile device management (MDM), system can be used to provision policies to mobile devices to control aspects of their allowed behavior.

## Techniques Mitigated
- T1417: Input Capture
- T1417.001: Keylogging
- T1417.002: GUI Input Capture
- T1428: Exploitation of Remote Services
- T1430: Location Tracking
- T1430.001: Remote Device Management Services
- T1451: SIM Card Swap
- T1458: Replication Through Removable Media
- T1461: Lockscreen Bypass
- T1513: Screen Capture
- T1516: Input Injection
- T1517: Access Notifications
- T1521.003: SSL Pinning
- T1629: Impair Defenses
- T1629.001: Prevent Application Removal
- T1632: Subvert Trust Controls
- T1632.001: Code Signing Policy Modification
- T1661: Application Versioning
- T1663: Remote Access Software


---

# M1011: User Guidance

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1011  

## Description
Describes any guidance or training given to users to set particular configuration settings or avoid specific potentially risky behaviors.

## Techniques Mitigated
- T1417: Input Capture
- T1417.001: Keylogging
- T1418: Software Discovery
- T1418.001: Security Software Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1430.001: Remote Device Management Services
- T1451: SIM Card Swap
- T1453: Abuse Accessibility Features
- T1458: Replication Through Removable Media
- T1513: Screen Capture
- T1516: Input Injection
- T1517: Access Notifications
- T1521.003: SSL Pinning
- T1541: Foreground Persistence
- T1582: SMS Control
- T1616: Call Control
- T1626.001: Device Administrator Permissions
- T1627: Execution Guardrails
- T1627.001: Geofencing
- T1628.001: Suppress Application Icon
- T1629: Impair Defenses
- T1629.001: Prevent Application Removal
- T1629.003: Disable or Modify Tools
- T1630: Indicator Removal on Host
- T1630.001: Uninstall Malicious Application
- T1630.002: File Deletion
- T1632: Subvert Trust Controls
- T1632.001: Code Signing Policy Modification
- T1635: Steal Application Access Token
- T1635.001: URI Hijacking
- T1636: Protected User Data
- T1636.001: Calendar Entries
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1636.005: Accounts
- T1640: Account Access Removal
- T1642: Endpoint Denial of Service
- T1643: Generate Traffic from Victim
- T1644: Out of Band Data
- T1655: Masquerading
- T1655.001: Match Legitimate Name or Location
- T1658: Exploitation for Client Execution
- T1660: Phishing
- T1662: Data Destruction
- T1663: Remote Access Software
- T1670: Virtualization Solution
- T1676: Linked Devices


---

# M1059: Do Not Mitigate

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1059  

## Description
This category is to associate techniques that mitigation might increase risk of compromise and therefore mitigation is not recommended.

## Techniques Mitigated
- T1628.003: Conceal Multimedia Files


---

# M1058: Antivirus/Antimalware

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1058  

## Description
Mobile security products, such as Mobile Threat Defense (MTD), offer various device-based mitigations against certain behaviors.

## Techniques Mitigated
- T1660: Phishing
- T1664: Exploitation for Initial Access


---

# M1004: System Partition Integrity

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1004  

## Description
Ensure that Android devices being used include and enable the Verified Boot capability, which cryptographically ensures the integrity of the system partition.

## Techniques Mitigated
- T1398: Boot or Logon Initialization Scripts
- T1474.003: Compromise Software Supply Chain
- T1625: Hijack Execution Flow
- T1625.001: System Runtime API Hijacking
- T1629: Impair Defenses
- T1629.003: Disable or Modify Tools
- T1645: Compromise Client Software Binary


---

# M1009: Encrypt Network Traffic

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1009  

## Description
Application developers should encrypt all of their application network traffic using the Transport Layer Security (TLS) protocol to ensure protection of sensitive data and deter network-based attacks. If desired, application developers could perform message-based encryption of data before passing it for TLS encryption.

iOS's App Transport Security feature can be used to help ensure that all application network traffic is appropriately protected. Apple intends to mandate use of App Transport Security  (Citation: TechCrunch-ATS) for all apps in the Apple App Store unless appropriate justification is given.

Android's Network Security Configuration feature similarly can be used by app developers to help ensure that all of their application network traffic is appropriately protected  (Citation: Android-NetworkSecurityConfig).

Use of Virtual Private Network (VPN) tunnels, e.g. using the IPsec protocol, can help mitigate some types of network attacks as well.

## Techniques Mitigated
- T1422.001: Internet Connection Discovery
- T1638: Adversary-in-the-Middle


---

# M1003: Lock Bootloader

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1003  

## Description
On devices that provide the capability to unlock the bootloader (hence allowing any operating system code to be flashed onto the device), perform periodic checks to ensure that the bootloader is locked.

## Techniques Mitigated
- T1398: Boot or Logon Initialization Scripts
- T1458: Replication Through Removable Media
- T1645: Compromise Client Software Binary


---

# M1001: Security Updates

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1001  

## Description
Install security updates in response to discovered vulnerabilities.

Purchase devices with a vendor and/or mobile carrier commitment to provide security updates in a prompt manner for a set period of time.

Decommission devices that will no longer receive security updates.

Limit or block access to enterprise resources from devices that have not installed recent security updates.

On Android devices, access can be controlled based on each device's security patch level. On iOS devices, access can be controlled based on the iOS version.

## Techniques Mitigated
- T1398: Boot or Logon Initialization Scripts
- T1404: Exploitation for Privilege Escalation
- T1456: Drive-By Compromise
- T1458: Replication Through Removable Media
- T1461: Lockscreen Bypass
- T1474: Supply Chain Compromise
- T1474.002: Compromise Hardware Supply Chain
- T1474.003: Compromise Software Supply Chain
- T1577: Compromise Application Executable
- T1629: Impair Defenses
- T1629.003: Disable or Modify Tools
- T1630: Indicator Removal on Host
- T1630.001: Uninstall Malicious Application
- T1634: Credentials from Password Store
- T1634.001: Keychain
- T1645: Compromise Client Software Binary
- T1658: Exploitation for Client Execution
- T1664: Exploitation for Initial Access


---

# M1010: Deploy Compromised Device Detection Method

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1010  

## Description
A variety of methods exist that can be used to enable enterprises to identify compromised (e.g. rooted/jailbroken) devices, whether using security mechanisms built directly into the device, third-party mobile security applications, enterprise mobility management (EMM)/mobile device management (MDM) capabilities, or other methods. Some methods may be trivial to evade while others may be more sophisticated.

## Techniques Mitigated
- T1404: Exploitation for Privilege Escalation
- T1617: Hooking
- T1623: Command and Scripting Interpreter
- T1623.001: Unix Shell
- T1628.002: User Evasion
- T1629: Impair Defenses
- T1629.003: Disable or Modify Tools
- T1634: Credentials from Password Store
- T1634.001: Keychain


---

# M1014: Interconnection Filtering

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1014  

## Description
In order to mitigate Signaling System 7 (SS7) exploitation, the Communications, Security, Reliability, and Interoperability Council (CSRIC) describes filtering interconnections between network operators to block inappropriate requests (Citation: CSRIC5-WG10-FinalReport).

## Techniques Mitigated
- T1430: Location Tracking
- T1430.002: Impersonate SS7 Nodes


---

# M1002: Attestation

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1002  

## Description
Enable remote attestation capabilities when available (such as Android SafetyNet or Samsung Knox TIMA Attestation) and prohibit devices that fail the attestation from accessing enterprise resources.

## Techniques Mitigated
- T1398: Boot or Logon Initialization Scripts
- T1404: Exploitation for Privilege Escalation
- T1424: Process Discovery
- T1617: Hooking
- T1623: Command and Scripting Interpreter
- T1623.001: Unix Shell
- T1625: Hijack Execution Flow
- T1625.001: System Runtime API Hijacking
- T1630: Indicator Removal on Host
- T1630.001: Uninstall Malicious Application
- T1634: Credentials from Password Store
- T1634.001: Keychain
- T1645: Compromise Client Software Binary


---

# G0097: Bouncing Golf

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0097  
**Aliases:** Bouncing Golf  

## Description
[Bouncing Golf](https://attack.mitre.org/groups/G0097) is a cyberespionage campaign targeting Middle Eastern countries.(Citation: Trend Micro Bouncing Golf 2019)

## Techniques Used
- T1655.001: Match Legitimate Name or Location


---

# G0094: Kimsuky

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0094  
**Aliases:** Kimsuky, Black Banshee, Velvet Chollima, Emerald Sleet, THALLIUM, APT43, TA427, Springtail, Earth Kumiho, PatheticSlug  

## Description
[Kimsuky](https://attack.mitre.org/groups/G0094) is a Democratic People's Republic of Korea (DPRK)-based cyber espionage group that has been active since at least 2012. The group initially targeted South Korean government agencies, think tanks, and subject-matter experts in various fields. Its operations expanded to include the United Nations and organizations in the government, education, business services, and manufacturing sectors across the United States, Japan, Russia, and Europe. [Kimsuky](https://attack.mitre.org/groups/G0094) has focused collection on foreign policy and national security issues tied to the Korean Peninsula, nuclear policy, and sanctions. [Kimsuky](https://attack.mitre.org/groups/G0094) operations have overlapped with those of other North Korean state-sponsored cyber espionage actors as a result of ad hoc collaborations or other limited resource sharing.(Citation: EST Kimsuky April 2019)(Citation: Cybereason Kimsuky November 2020)(Citation: Malwarebytes Kimsuky June 2021)(Citation: CISA AA20-301A Kimsuky)(Citation: Mandiant APT43 March 2024)(Citation: Proofpoint TA427 April 2024) 

[Kimsuky](https://attack.mitre.org/groups/G0094) was assessed to be responsible for the 2014 Korea Hydro & Nuclear Power Co. compromise; other notable campaigns include Operation STOLEN PENCIL (2018), Operation Kabar Cobra (2019), and Operation Smoke Screen (2019).(Citation: Netscout Stolen Pencil Dec 2018)(Citation: EST Kimsuky SmokeScreen April 2019)(Citation: AhnLab Kimsuky Kabar Cobra Feb 2019) In 2023, [Kimsuky](https://attack.mitre.org/groups/G0094) was observed using commercial large language models (LLMs) to assist with vulnerability research, scripting, social engineering and reconnaissance.(Citation: MSFT-AI)

DPRK threat actor cluster boundaries overlap in open source reporting, with some security researchers consolidating all attributed North Korean state-sponsored cyber activity under [Lazarus Group](https://attack.mitre.org/groups/G0032), rather than tracking operationally distinct subgroups.

## Techniques Used
- T1660: Phishing


---

# G0040: Patchwork

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0040  
**Aliases:** Patchwork, Hangover Group, Dropping Elephant, Chinastrats, MONSOON, Operation Hangover  

## Description
[Patchwork](https://attack.mitre.org/groups/G0040) is a cyber espionage group that was first observed in December 2015. While the group has not been definitively attributed, circumstantial evidence suggests the group may be a pro-Indian or Indian entity. [Patchwork](https://attack.mitre.org/groups/G0040) has been seen targeting industries related to diplomatic and government agencies. Much of the code used by this group was copied and pasted from online forums. [Patchwork](https://attack.mitre.org/groups/G0040) was also seen operating spearphishing campaigns targeting U.S. think tank groups in March and April of 2018.(Citation: Cymmetria Patchwork) (Citation: Symantec Patchwork)(Citation: TrendMicro Patchwork Dec 2017)(Citation: Volexity Patchwork June 2018)


---

# G0096: APT41

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0096  
**Aliases:** APT41, Wicked Panda, Brass Typhoon, BARIUM  

## Description
[APT41](https://attack.mitre.org/groups/G0096) is a threat group that researchers have assessed as Chinese state-sponsored espionage group that also conducts financially-motivated operations. Active since at least 2012, [APT41](https://attack.mitre.org/groups/G0096) has been observed targeting various industries, including but not limited to healthcare, telecom, technology, finance, education, retail and video game industries in 14 countries.(Citation: apt41_mandiant) Notable behaviors include using a wide range of malware and tools to complete mission objectives. [APT41](https://attack.mitre.org/groups/G0096) overlaps at least partially with public reporting on groups including BARIUM and [Winnti Group](https://attack.mitre.org/groups/G0044).(Citation: FireEye APT41 Aug 2019)(Citation: Group IB APT 41 June 2021)


---

# G1029: UNC788

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1029  
**Aliases:** UNC788  

## Description
[UNC788](https://attack.mitre.org/groups/G1029) is a group of hackers from Iran that has targeted people in the Middle East.(Citation: Meta Adversarial Threat Report 2022)

## Techniques Used
- T1660: Phishing


---

# G0069: MuddyWater

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0069  
**Aliases:** MuddyWater, Earth Vetala, MERCURY, Static Kitten, Seedworm, TEMP.Zagros, Mango Sandstorm, TA450, MuddyKrill  

## Description
[MuddyWater](https://attack.mitre.org/groups/G0069) is a cyber espionage group assessed to be a subordinate element within Iran's Ministry of Intelligence and Security (MOIS).(Citation: CYBERCOM Iranian Intel Cyber January 2022) Since at least 2017, [MuddyWater](https://attack.mitre.org/groups/G0069) has targeted a range of government and private organizations across sectors, including telecommunications, local government, finance, defense, and oil and natural gas organizations, in the Middle East (specifically the UAE and Saudi Arabia), Asia, Africa, Europe, and North America. [MuddyWater](https://attack.mitre.org/groups/G0069) has reused domains dating back to October 2025, and has a preference for NameCheap and Hosterdaddy Private Limited (AS136557). In late 2025 and early 2026, [MuddyWater](https://attack.mitre.org/groups/G0069) used commercial satellite internet (i.e., Starlink) for command and control (C2) communication. (Citation: FalconFeeds_Iran_Mar2026)(Citation: Huntio_IranInfra_Mar2026)(Citation: Unit 42 MuddyWater Nov 2017)(Citation: Symantec MuddyWater Dec 2018)(Citation: ClearSky MuddyWater Nov 2018)(Citation: ClearSky MuddyWater June 2019)(Citation: Reaqta MuddyWater November 2017)(Citation: DHS CISA AA22-055A MuddyWater February 2022)(Citation: Talos MuddyWater Jan 2022)(Citation: NaumaanProofpoint_GlobalClickFix_April2025)(Citation: ESET_MuddyWater_Dec2025)(Citation: SymantecCarbonBlack_Seedworm_Mar2026)


---

# G0034: Sandworm Team

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0034  
**Aliases:** Sandworm Team, ELECTRUM, Telebots, IRON VIKING, BlackEnergy (Group), Quedagh, Voodoo Bear, IRIDIUM, Seashell Blizzard, FROZENBARENTS, APT44  

## Description
[Sandworm Team](https://attack.mitre.org/groups/G0034) is a destructive threat group that has been attributed to Russia's General Staff Main Intelligence Directorate (GRU) Main Center for Special Technologies (GTsST) military unit 74455.(Citation: US District Court Indictment GRU Unit 74455 October 2020)(Citation: UK NCSC Olympic Attacks October 2020) This group has been active since at least 2009.(Citation: iSIGHT Sandworm 2014)(Citation: CrowdStrike VOODOO BEAR)(Citation: USDOJ Sandworm Feb 2020)(Citation: NCSC Sandworm Feb 2020)

In October 2020, the US indicted six GRU Unit 74455 officers associated with [Sandworm Team](https://attack.mitre.org/groups/G0034) for the following cyber operations: the 2015 and 2016 attacks against Ukrainian electrical companies and government organizations, the 2017 worldwide [NotPetya](https://attack.mitre.org/software/S0368) attack, targeting of the 2017 French presidential campaign, the 2018 [Olympic Destroyer](https://attack.mitre.org/software/S0365) attack against the Winter Olympic Games, the 2018 operation against the Organisation for the Prohibition of Chemical Weapons, and attacks against the country of Georgia in 2018 and 2019.(Citation: US District Court Indictment GRU Unit 74455 October 2020)(Citation: UK NCSC Olympic Attacks October 2020) Some of these were conducted with the assistance of GRU Unit 26165, which is also referred to as [APT28](https://attack.mitre.org/groups/G0007).(Citation: US District Court Indictment GRU Oct 2018)

## Techniques Used
- T1409: Stored Application Data
- T1660: Phishing
- T1676: Linked Devices


---

# G1015: Scattered Spider

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1015  
**Aliases:** Scattered Spider, Roasted 0ktapus, Octo Tempest, Storm-0875, UNC3944  

## Description
[Scattered Spider](https://attack.mitre.org/groups/G1015) is a native English-speaking cybercriminal group active since at least 2022. (Citation: CrowdStrike Scattered Spider Profile) (Citation: MSTIC Octo Tempest Operations October 2023) The group initially targeted customer relationship management (CRM) providers, business process outsourcing (BPO) firms, and telecommunications and technology companies before expanding in 2023 to gaming, hospitality, retail, managed service provider (MSP), manufacturing, and financial sectors. (Citation: MSTIC Octo Tempest Operations October 2023)
[Scattered Spider](https://attack.mitre.org/groups/G1015) relies heavily on social engineering, including impersonating IT and help-desk staff, to gain initial access, bypass multi-factor authentication (MFA), and compromise enterprise networks. The group has adapted its tooling to evade endpoint detection and response (EDR) defenses and used ransomware for financial gain. (Citation: CISA Scattered Spider Advisory November 2023) (Citation: CrowdStrike Scattered Spider BYOVD January 2023) (Citation: Crowdstrike TELCO BPO Campaign December 2022)
[Scattered Spider](https://attack.mitre.org/groups/G1015) had expanded into hybrid cloud and identity environments, using help-desk impersonation and MFA bypass to obtain administrator access in Okta, AWS, and Office 365. (Citation: Mandiant UNC3944 May 2025)

## Techniques Used
- T1451: SIM Card Swap
- T1660: Phishing


---

# G0142: Confucius

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0142  
**Aliases:** Confucius, Confucius APT  

## Description
[Confucius](https://attack.mitre.org/groups/G0142) is a cyber espionage group that has primarily targeted military personnel, high-profile personalities, business persons, and government organizations in South Asia since at least 2013. Security researchers have noted similarities between [Confucius](https://attack.mitre.org/groups/G0142) and [Patchwork](https://attack.mitre.org/groups/G0040), particularly in their respective custom malware code and targets.(Citation: TrendMicro Confucius APT Feb 2018)(Citation: TrendMicro Confucius APT Aug 2021)(Citation: Uptycs Confucius APT Jan 2021)


---

# G1019: MoustachedBouncer

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1019  
**Aliases:** MoustachedBouncer  

## Description
[MoustachedBouncer](https://attack.mitre.org/groups/G1019) is a cyberespionage group that has been active since at least 2014 targeting foreign embassies in Belarus.(Citation: MoustachedBouncer ESET August 2023)

## Techniques Used
- T1655.001: Match Legitimate Name or Location


---

# G1002: BITTER

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1002  
**Aliases:** BITTER, T-APT-17  

## Description
[BITTER](https://attack.mitre.org/groups/G1002) is a suspected South Asian cyber espionage threat group that has been active since at least 2013. [BITTER](https://attack.mitre.org/groups/G1002) has targeted government, energy, and engineering organizations in Pakistan, China, Bangladesh, and Saudi Arabia.(Citation: Cisco Talos Bitter Bangladesh May 2022)(Citation: Forcepoint BITTER Pakistan Oct 2016)

## Techniques Used
- T1660: Phishing


---

# G1028: APT-C-23

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1028  
**Aliases:** APT-C-23, Mantis, Arid Viper, Desert Falcon, TAG-63, Grey Karkadann, Big Bang APT, Two-tailed Scorpion  

## Description
[APT-C-23](https://attack.mitre.org/groups/G1028) is a threat group that has been active since at least 2014.(Citation: symantec_mantis) [APT-C-23](https://attack.mitre.org/groups/G1028) has primarily focused its operations on the Middle East, including Israeli military assets. [APT-C-23](https://attack.mitre.org/groups/G1028) has developed mobile spyware targeting Android and iOS devices since 2017.(Citation: welivesecurity_apt-c-23)

## Techniques Used
- T1422: System Network Configuration Discovery
- T1655.001: Match Legitimate Name or Location
- T1660: Phishing


---

# G0070: Dark Caracal

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0070  
**Aliases:** Dark Caracal  

## Description
[Dark Caracal](https://attack.mitre.org/groups/G0070) is threat group that has been attributed to the Lebanese General Directorate of General Security (GDGS) and has operated since at least 2012. (Citation: Lookout Dark Caracal Jan 2018)

## Techniques Used
- T1437.001: Web Protocols


---

# G1033: Star Blizzard

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1033  
**Aliases:** Star Blizzard, SEABORGIUM, Callisto Group, TA446, COLDRIVER  

## Description
[Star Blizzard](https://attack.mitre.org/groups/G1033) is a cyber espionage and influence group originating in Russia that has been active since at least 2019. [Star Blizzard](https://attack.mitre.org/groups/G1033) campaigns align closely with Russian state interests and have included persistent phishing and credential theft against academic, defense, government, NGO, and think tank organizations in NATO countries, particularly the US and the UK.(Citation: Microsoft Star Blizzard August 2022)(Citation: CISA Star Blizzard Advisory December 2023)(Citation: StarBlizzard)(Citation: Google TAG COLDRIVER January 2024)

## Techniques Used
- T1676: Linked Devices


---

# G0112: Windshift

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0112  
**Aliases:** Windshift, Bahamut  

## Description
[Windshift](https://attack.mitre.org/groups/G0112) is a threat group that has been active since at least 2017, targeting specific individuals for surveillance in government departments and critical infrastructure across the Middle East.(Citation: SANS Windshift August 2018)(Citation: objective-see windtail1 dec 2018)(Citation: objective-see windtail2 jan 2019)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1407: Download New Code at Runtime
- T1417.001: Keylogging
- T1420: File and Directory Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1512: Video Capture
- T1521.001: Symmetric Cryptography
- T1533: Data from Local System
- T1627.001: Geofencing
- T1628.003: Conceal Multimedia Files
- T1632.001: Code Signing Policy Modification
- T1633.001: System Checks
- T1636.003: Contact List
- T1636.004: SMS Messages


---

# G0007: APT28

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0007  
**Aliases:** APT28, IRON TWILIGHT, SNAKEMACKEREL, Swallowtail, Group 74, Sednit, Sofacy, Pawn Storm, Fancy Bear, STRONTIUM, Tsar Team, Threat Group-4127, TG-4127, Forest Blizzard, FROZENLAKE, GruesomeLarch  

## Description
[APT28](https://attack.mitre.org/groups/G0007) is a threat group that has been attributed to Russia's General Staff Main Intelligence Directorate (GRU) 85th Main Special Service Center (GTsSS) military unit 26165.(Citation: NSA/FBI Drovorub August 2020)(Citation: Cybersecurity Advisory GRU Brute Force Campaign July 2021) This group has been active since at least 2004.(Citation: DOJ GRU Indictment Jul 2018)(Citation: Ars Technica GRU indictment Jul 2018)(Citation: Crowdstrike DNC June 2016)(Citation: FireEye APT28)(Citation: SecureWorks TG-4127)(Citation: FireEye APT28 January 2017)(Citation: GRIZZLY STEPPE JAR)(Citation: Sofacy DealersChoice)(Citation: Palo Alto Sofacy 06-2018)(Citation: Symantec APT28 Oct 2018)(Citation: ESET Zebrocy May 2019)

[APT28](https://attack.mitre.org/groups/G0007) reportedly compromised the Hillary Clinton campaign, the Democratic National Committee, and the Democratic Congressional Campaign Committee in 2016 in an attempt to interfere with the U.S. presidential election.(Citation: Crowdstrike DNC June 2016) In 2018, the US indicted five GRU Unit 26165 officers associated with [APT28](https://attack.mitre.org/groups/G0007) for cyber operations (including close-access operations) conducted between 2014 and 2018 against the World Anti-Doping Agency (WADA), the US Anti-Doping Agency, a US nuclear facility, the Organization for the Prohibition of Chemical Weapons (OPCW), the Spiez Swiss Chemicals Laboratory, and other organizations.(Citation: US District Court Indictment GRU Oct 2018) Some of these were conducted with the assistance of GRU Unit 74455, which is also referred to as [Sandworm Team](https://attack.mitre.org/groups/G0034).


---

# G1006: Earth Lusca

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1006  
**Aliases:** Earth Lusca, TAG-22, Charcoal Typhoon, CHROMIUM, ControlX  

## Description
[Earth Lusca](https://attack.mitre.org/groups/G1006) is a suspected China-based cyber espionage group that has been active since at least April 2019. [Earth Lusca](https://attack.mitre.org/groups/G1006) has targeted organizations in Australia, China, Hong Kong, Mongolia, Nepal, the Philippines, Taiwan, Thailand, Vietnam, the United Arab Emirates, Nigeria, Germany, France, and the United States. Targets included government institutions, news media outlets, gambling companies, educational institutions, COVID-19 research organizations, telecommunications companies, religious movements banned in China, and cryptocurrency trading platforms; security researchers assess some [Earth Lusca](https://attack.mitre.org/groups/G1006) operations may be financially motivated.(Citation: TrendMicro EarthLusca 2022)

[Earth Lusca](https://attack.mitre.org/groups/G1006) has used malware commonly used by other Chinese threat groups, including [APT41](https://attack.mitre.org/groups/G0096) and the [Winnti Group](https://attack.mitre.org/groups/G0044) cluster, however security researchers assess [Earth Lusca](https://attack.mitre.org/groups/G1006)'s techniques and infrastructure are separate.(Citation: TrendMicro EarthLusca 2022)


---

# G1004: LAPSUS$

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G1004  
**Aliases:** LAPSUS$, DEV-0537, Strawberry Tempest  

## Description
[LAPSUS$](https://attack.mitre.org/groups/G1004) is cyber criminal threat group that has been active since at least mid-2021. [LAPSUS$](https://attack.mitre.org/groups/G1004) specializes in large-scale social engineering and extortion operations, including destructive attacks without the use of ransomware. The group has targeted organizations globally, including in the government, manufacturing, higher education, energy, healthcare, technology, telecommunications, and media sectors.(Citation: BBC LAPSUS Apr 2022)(Citation: MSTIC DEV-0537 Mar 2022)(Citation: UNIT 42 LAPSUS Mar 2022)

## Techniques Used
- T1451: SIM Card Swap


---

# G0056: PROMETHIUM

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0056  
**Aliases:** PROMETHIUM, StrongPity  

## Description
[PROMETHIUM](https://attack.mitre.org/groups/G0056) is an activity group focused on espionage that has been active since at least 2012. The group has conducted operations globally with a heavy emphasis on Turkish targets. [PROMETHIUM](https://attack.mitre.org/groups/G0056) has demonstrated similarity to another activity group called [NEODYMIUM](https://attack.mitre.org/groups/G0055) due to overlapping victim and campaign characteristics.(Citation: Microsoft NEODYMIUM Dec 2016)(Citation: Microsoft SIR Vol 21)(Citation: Talos Promethium June 2020)


---

# G0090: WIRTE

**Type:** intrusion-set  
**Reference:** https://attack.mitre.org/groups/G0090  
**Aliases:** WIRTE, Ashen Lepus  

## Description
[WIRTE](https://attack.mitre.org/groups/G0090) is a cyberespionage actor, believed to be a subgroup of the Hamas-affiliated Gaza Cybergang, that has been active since at least August 2018. [WIRTE](https://attack.mitre.org/groups/G0090) has targeted diplomatic, financial, military, legal, and technology organizations across the Middle East, North Africa, and in Europe to gather intelligence. [WIRTE](https://attack.mitre.org/groups/G0090) has remained persistently active despite the ongoing Israel-Hamas conflict and has expanded their operations to include wiper malware attacks against Israeli targets.(Citation: Lab52 WIRTE Apr 2019)(Citation: Kaspersky WIRTE November 2021)(Citation: Check Point Wirte NOV 2024)(Citation: Palo Alto Ashen Lepus DEC 2025)


---

# S0529: CarbonSteal

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0529  
**Aliases:** CarbonSteal  
**Platforms:** Android  

## Description
[CarbonSteal](https://attack.mitre.org/software/S0529) is one of a family of four surveillanceware tools that share a common C2 infrastructure. [CarbonSteal](https://attack.mitre.org/software/S0529) primarily deals with audio surveillance. (Citation: Lookout Uyghur Campaign)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1407: Download New Code at Runtime
- T1409: Stored Application Data
- T1418: Software Discovery
- T1420: File and Directory Discovery
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1521.002: Asymmetric Cryptography
- T1575: Native API
- T1616: Call Control
- T1630.002: File Deletion
- T1636.004: SMS Messages
- T1644: Out of Band Data
- T1655.001: Match Legitimate Name or Location


---

# S0480: Cerberus

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0480  
**Aliases:** Cerberus  
**Platforms:** Android  

## Description
[Cerberus](https://attack.mitre.org/software/S0480) is a banking trojan whose usage can be rented on underground forums and marketplaces. Prior to being available to rent, the authors of [Cerberus](https://attack.mitre.org/software/S0480) claim was used in private operations for two years.(Citation: Threat Fabric Cerberus)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1407: Download New Code at Runtime
- T1417.001: Keylogging
- T1417.002: GUI Input Capture
- T1418: Software Discovery
- T1426: System Information Discovery
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1509: Non-Standard Port
- T1516: Input Injection
- T1582: SMS Control
- T1628.001: Suppress Application Icon
- T1629.003: Disable or Modify Tools
- T1630.001: Uninstall Malicious Application
- T1633.001: System Checks
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location


---

# S0320: DroidJack

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0320  
**Aliases:** DroidJack  
**Platforms:** Android  

## Description
[DroidJack](https://attack.mitre.org/software/S0320) is an Android remote access tool that has been observed posing as legitimate applications including the Super Mario Run and Pokemon GO games. (Citation: Zscaler-SuperMarioRun) (Citation: Proofpoint-Droidjack)

## Techniques Used
- T1429: Audio Capture
- T1512: Video Capture
- T1636.002: Call Log
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location


---

# S0411: Rotexy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0411  
**Aliases:** Rotexy  
**Platforms:** Android  

## Description
[Rotexy](https://attack.mitre.org/software/S0411) is an Android banking malware that has evolved over several years. It was originally an SMS spyware Trojan first spotted in October 2014, and since then has evolved to contain more features, including ransomware functionality.(Citation: securelist rotexy 2018)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1417.002: GUI Input Capture
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1424: Process Discovery
- T1426: System Information Discovery
- T1437.001: Web Protocols
- T1521.001: Symmetric Cryptography
- T1582: SMS Control
- T1628.001: Suppress Application Icon
- T1629.002: Device Lockout
- T1633.001: System Checks
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1637.001: Domain Generation Algorithms
- T1644: Out of Band Data


---

# S0328: Stealth Mango

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0328  
**Aliases:** Stealth Mango  
**Platforms:** Android  

## Description
[Stealth Mango](https://attack.mitre.org/software/S0328) is Android malware that has reportedly been used to successfully compromise the mobile devices of government officials, members of the military, medical professionals, and civilians. The iOS malware known as [Tangelo](https://attack.mitre.org/software/S0329) is believed to be from the same developer. (Citation: Lookout-StealthMango)

## Techniques Used
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1456: Drive-By Compromise
- T1474.003: Compromise Software Supply Chain
- T1512: Video Capture
- T1533: Data from Local System
- T1582: SMS Control
- T1636.001: Calendar Entries
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1644: Out of Band Data


---

# S0319: Allwinner

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0319  

## Description
[Allwinner](https://attack.mitre.org/software/S0319) is a company that supplies processors used in Android tablets and other devices. A Linux kernel distributed by [Allwinner](https://attack.mitre.org/software/S0319) for use on these devices reportedly contained a backdoor. (Citation: HackerNews-Allwinner)

## Techniques Used
- T1474.003: Compromise Software Supply Chain


---

# S0551: GoldenEagle

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0551  
**Aliases:** GoldenEagle  

## Description
[GoldenEagle](https://attack.mitre.org/software/S0551) is a piece of Android malware that has been used in targeting of Uyghurs, Muslims, Tibetans, individuals in Turkey, and individuals in China. Samples have been found as early as 2012.(Citation: Lookout Uyghur Campaign)

## Techniques Used
- T1407: Download New Code at Runtime
- T1409: Stored Application Data
- T1418: Software Discovery
- T1420: File and Directory Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1512: Video Capture
- T1513: Screen Capture
- T1533: Data from Local System
- T1582: SMS Control
- T1632.001: Code Signing Policy Modification
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1646: Exfiltration Over C2 Channel
- T1655.001: Match Legitimate Name or Location


---

# S1103: FlixOnline

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1103  
**Aliases:** FlixOnline  
**Platforms:** Android  

## Description
[FlixOnline](https://attack.mitre.org/software/S1103) is an Android malware, first detected in early 2021, believed to target users of WhatsApp. [FlixOnline](https://attack.mitre.org/software/S1103) primarily spreads via automatic replies to a device’s incoming WhatsApp messages.(Citation: checkpoint_flixonline_0421)

## Techniques Used
- T1409: Stored Application Data
- T1417.002: GUI Input Capture
- T1517: Access Notifications
- T1624.001: Broadcast Receivers
- T1628.001: Suppress Application Icon
- T1643: Generate Traffic from Victim


---

# S0432: Bread

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0432  
**Aliases:** Bread, Joker  
**Platforms:** Android  

## Description
[Bread](https://attack.mitre.org/software/S0432) was a large-scale billing fraud malware family known for employing many different cloaking and obfuscation techniques in an attempt to continuously evade Google Play Store’s malware detection. 1,700 unique Bread apps were detected and removed from the Google Play Store before being downloaded by users.(Citation: Google Bread)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1406.002: Software Packing
- T1407: Download New Code at Runtime
- T1422: System Network Configuration Discovery
- T1437.001: Web Protocols
- T1517: Access Notifications
- T1575: Native API
- T1636.004: SMS Messages
- T1643: Generate Traffic from Victim


---

# S1216: TriangleDB

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1216  
**Aliases:** TriangleDB  
**Platforms:** iOS  

## Description
[TriangleDB](https://attack.mitre.org/software/S1216) is an Objective-C written implant deployed after [Binary Validator](https://attack.mitre.org/software/S1215) and after root privileges are obtained during [Operation Triangulation](https://attack.mitre.org/campaigns/C0054)’s infection chain. Upon execution, [TriangleDB](https://attack.mitre.org/software/S1216) communicates with the C2 server, relaying information about the victim device.(Citation: SecureList OpTriangulation 21Jun2023)

## Techniques Used
- T1418: Software Discovery
- T1420: File and Directory Discovery
- T1422: System Network Configuration Discovery
- T1424: Process Discovery
- T1430: Location Tracking
- T1521.001: Symmetric Cryptography
- T1521.002: Asymmetric Cryptography
- T1533: Data from Local System
- T1544: Ingress Tool Transfer
- T1630.002: File Deletion
- T1634.001: Keychain
- T1644: Out of Band Data


---

# S1077: Hornbill

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1077  
**Aliases:** Hornbill  
**Platforms:** Android  

## Description
[Hornbill](https://attack.mitre.org/software/S1077) is one of two mobile malware families known to be used by the APT [Confucius](https://attack.mitre.org/groups/G0142). Analysis suggests that [Hornbill](https://attack.mitre.org/software/S1077) was first active in early 2018. While [Hornbill](https://attack.mitre.org/software/S1077) and [Sunbird](https://attack.mitre.org/software/S1082) overlap in core capabilities, [Hornbill](https://attack.mitre.org/software/S1077) has tools and behaviors suggesting more passive reconnaissance.(Citation: lookout_hornbill_sunbird_0221)

## Techniques Used
- T1409: Stored Application Data
- T1418: Software Discovery
- T1420: File and Directory Discovery
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1422.002: Wi-Fi Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1512: Video Capture
- T1513: Screen Capture
- T1517: Access Notifications
- T1533: Data from Local System
- T1626.001: Device Administrator Permissions
- T1628.002: User Evasion
- T1630.002: File Deletion
- T1636.002: Call Log
- T1636.003: Contact List
- T1646: Exfiltration Over C2 Channel
- T1655.001: Match Legitimate Name or Location


---

# S0325: Judy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0325  

## Description
[Judy](https://attack.mitre.org/software/S0325) is auto-clicking adware that was distributed through multiple apps in the Google Play Store. (Citation: CheckPoint-Judy)

## Techniques Used
- T1407: Download New Code at Runtime
- T1643: Generate Traffic from Victim


---

# S0285: OldBoot

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0285  

## Description
[OldBoot](https://attack.mitre.org/software/S0285) is an Android malware family. (Citation: HackerNews-OldBoot)

## Techniques Used
- T1398: Boot or Logon Initialization Scripts


---

# S0290: Gooligan

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0290  
**Aliases:** Gooligan, Ghost Push  
**Platforms:** Android  

## Description
[Gooligan](https://attack.mitre.org/software/S0290) is a malware family that runs privilege escalation exploits on Android devices and then uses its escalated privileges to steal authentication tokens that can be used to access data from many Google applications. [Gooligan](https://attack.mitre.org/software/S0290) has been described as part of the Ghost Push Android malware family. (Citation: Gooligan Citation) (Citation: Ludwig-GhostPush) (Citation: Lookout-Gooligan)

## Techniques Used
- T1404: Exploitation for Privilege Escalation
- T1533: Data from Local System
- T1643: Generate Traffic from Victim


---

# S0305: SpyNote RAT

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0305  
**Aliases:** SpyNote RAT  
**Platforms:** Android  

## Description
[SpyNote RAT](https://attack.mitre.org/software/S0305) (Remote Access Trojan) is a family of malicious Android apps. The [SpyNote RAT](https://attack.mitre.org/software/S0305) builder tool can be used to develop malicious apps with the malware's functionality. (Citation: Zscaler-SpyNote)

## Techniques Used
- T1429: Audio Capture
- T1430: Location Tracking
- T1533: Data from Local System
- T1624.001: Broadcast Receivers
- T1636.003: Contact List
- T1636.004: SMS Messages


---

# S0427: TrickMo

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0427  
**Aliases:** TrickMo  
**Platforms:** Android  

## Description
[TrickMo](https://attack.mitre.org/software/S0427) a 2FA bypass mobile banking trojan, most likely being distributed by [TrickBot](https://attack.mitre.org/software/S0266). [TrickMo](https://attack.mitre.org/software/S0427) has been primarily targeting users located in Germany.(Citation: SecurityIntelligence TrickMo)

[TrickMo](https://attack.mitre.org/software/S0427) is designed to steal transaction authorization numbers (TANs), which are typically used as one-time passwords.(Citation: SecurityIntelligence TrickMo)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1422.002: Wi-Fi Discovery
- T1426: System Information Discovery
- T1437.001: Web Protocols
- T1513: Screen Capture
- T1516: Input Injection
- T1533: Data from Local System
- T1582: SMS Control
- T1624.001: Broadcast Receivers
- T1629.002: Device Lockout
- T1630.001: Uninstall Malicious Application
- T1633.001: System Checks
- T1636.004: SMS Messages
- T1644: Out of Band Data


---

# S0463: INSOMNIA

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0463  
**Aliases:** INSOMNIA  
**Platforms:** iOS  

## Description
[INSOMNIA](https://attack.mitre.org/software/S0463) is spyware that has been used by the group Evil Eye.(Citation: Volexity Insomnia)

## Techniques Used
- T1404: Exploitation for Privilege Escalation
- T1406: Obfuscated Files or Information
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1422.002: Wi-Fi Discovery
- T1426: System Information Discovery
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1456: Drive-By Compromise
- T1509: Non-Standard Port
- T1533: Data from Local System
- T1631.001: Ptrace System Calls
- T1634.001: Keychain
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages


---

# S0420: Dvmap

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0420  
**Aliases:** Dvmap  
**Platforms:** Android  

## Description
[Dvmap](https://attack.mitre.org/software/S0420) is rooting malware that injects malicious code into system runtime libraries. It is credited with being the first malware that performs this type of code injection.(Citation: SecureList DVMap June 2017)

## Techniques Used
- T1404: Exploitation for Privilege Escalation
- T1406: Obfuscated Files or Information
- T1407: Download New Code at Runtime
- T1426: System Information Discovery
- T1625.001: System Runtime API Hijacking
- T1629.003: Disable or Modify Tools
- T1632.001: Code Signing Policy Modification


---

# S0494: Zen

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0494  
**Aliases:** Zen  
**Platforms:** Android  

## Description
[Zen](https://attack.mitre.org/software/S0494) is Android malware that was first seen in 2013.(Citation: Google Security Zen)

## Techniques Used
- T1404: Exploitation for Privilege Escalation
- T1406: Obfuscated Files or Information
- T1407: Download New Code at Runtime
- T1516: Input Injection
- T1625.001: System Runtime API Hijacking
- T1629.003: Disable or Modify Tools
- T1631.001: Ptrace System Calls
- T1643: Generate Traffic from Victim


---

# S0299: NotCompatible

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0299  

## Description
[NotCompatible](https://attack.mitre.org/software/S0299) is an Android malware family that was used between at least 2014 and 2016. It has multiple variants that have become more sophisticated over time. (Citation: Lookout-NotCompatible)

## Techniques Used
- T1428: Exploitation of Remote Services


---

# S1095: AhRat

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1095  
**Aliases:** AhRat  
**Platforms:** Android  

## Description
[AhRat](https://attack.mitre.org/software/S1095) is an Android remote access tool based on the open-source AhMyth remote access tool. [AhRat](https://attack.mitre.org/software/S1095) initially spread in August 2022 on the Google Play Store via an update containing malicious code to the previously benign application, “iRecorder – Screen Recorder,” which itself was released in September 2021.(Citation: welivesecurity_ahrat_0523)

## Techniques Used
- T1398: Boot or Logon Initialization Scripts
- T1406: Obfuscated Files or Information
- T1420: File and Directory Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1513: Screen Capture
- T1521: Encrypted Channel
- T1533: Data from Local System
- T1582: SMS Control
- T1624.001: Broadcast Receivers
- T1636.002: Call Log
- T1636.003: Contact List
- T1646: Exfiltration Over C2 Channel


---

# S0318: XLoader for Android

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0318  
**Aliases:** XLoader for Android  
**Platforms:** Android  

## Description
[XLoader for Android](https://attack.mitre.org/software/S0318) is a malicious Android app first observed targeting Japan, Korea, China, Taiwan, and Hong Kong in 2018. It has more recently been observed targeting South Korean users as a pornography application.(Citation: TrendMicro-XLoader-FakeSpy)(Citation: TrendMicro-XLoader) It is tracked separately from the [XLoader for iOS](https://attack.mitre.org/software/S0490).

## Techniques Used
- T1406: Obfuscated Files or Information
- T1422: System Network Configuration Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1481.001: Dead Drop Resolver
- T1626.001: Device Administrator Permissions
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location


---

# S0306: Trojan-SMS.AndroidOS.FakeInst.a

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0306  

## Description
[Trojan-SMS.AndroidOS.FakeInst.a](https://attack.mitre.org/software/S0306) is Android malware. (Citation: Kaspersky-MobileMalware)

## Techniques Used
- T1437.001: Web Protocols


---

# S0490: XLoader for iOS

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0490  
**Aliases:** XLoader for iOS  
**Platforms:** iOS  

## Description
[XLoader for iOS](https://attack.mitre.org/software/S0490) is a malicious iOS application that is capable of gathering system information.(Citation: TrendMicro-XLoader-FakeSpy) It is tracked separately from the [XLoader for Android](https://attack.mitre.org/software/S0318).

## Techniques Used
- T1422: System Network Configuration Discovery
- T1426: System Information Discovery
- T1632.001: Code Signing Policy Modification
- T1646: Exfiltration Over C2 Channel


---

# S1061: AbstractEmu

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1061  
**Aliases:** AbstractEmu  
**Platforms:** Android  

## Description
[AbstractEmu](https://attack.mitre.org/software/S1061) is mobile malware that was first seen in Google Play and other third-party stores in October 2021. It was discovered in 19 Android applications, of which at least 7 abused known Android exploits for obtaining root permissions. [AbstractEmu](https://attack.mitre.org/software/S1061) was observed primarily impacting users in the United States, however victims are believed to be across a total of 17 countries.(Citation: lookout_abstractemu_1021)

## Techniques Used
- T1404: Exploitation for Privilege Escalation
- T1406: Obfuscated Files or Information
- T1407: Download New Code at Runtime
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1512: Video Capture
- T1517: Access Notifications
- T1533: Data from Local System
- T1544: Ingress Tool Transfer
- T1623.001: Unix Shell
- T1626.001: Device Administrator Permissions
- T1629.003: Disable or Modify Tools
- T1633: Virtualization/Sandbox Evasion
- T1633.001: System Checks
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1646: Exfiltration Over C2 Channel


---

# S1083: Chameleon

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1083  
**Aliases:** Chameleon  
**Platforms:** Android  

## Description
[Chameleon](https://attack.mitre.org/software/S1083) is an Android banking trojan that can leverage Android’s Accessibility Services to perform malicious activities. Believed to have been first active in January 2023, [Chameleon](https://attack.mitre.org/software/S1083) has been observed targeting users in Australia and Poland by masquerading as official applications. A new variant of [Chameleon](https://attack.mitre.org/software/S1083) has expanded its targets to include Android users in the United Kingdom and Italy.(Citation: cyble_chameleon_0423)(Citation: ThreatFabric_Chameleon_Dec2023)

## Techniques Used
- T1407: Download New Code at Runtime
- T1417.001: Keylogging
- T1417.002: GUI Input Capture
- T1418: Software Discovery
- T1426: System Information Discovery
- T1430: Location Tracking
- T1437: Application Layer Protocol
- T1437.001: Web Protocols
- T1453: Abuse Accessibility Features
- T1461: Lockscreen Bypass
- T1509: Non-Standard Port
- T1513: Screen Capture
- T1517: Access Notifications
- T1533: Data from Local System
- T1544: Ingress Tool Transfer
- T1575: Native API
- T1603: Scheduled Task/Job
- T1616: Call Control
- T1629.001: Prevent Application Removal
- T1629.003: Disable or Modify Tools
- T1630: Indicator Removal on Host
- T1633.001: System Checks
- T1636.004: SMS Messages
- T1646: Exfiltration Over C2 Channel
- T1655.001: Match Legitimate Name or Location
- T1660: Phishing


---

# S0405: Exodus

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0405  
**Aliases:** Exodus, Exodus One, Exodus Two  
**Platforms:** Android  

## Description
[Exodus](https://attack.mitre.org/software/S0405) is Android spyware deployed in two distinct stages named Exodus One (dropper) and Exodus Two (payload).(Citation: SWB Exodus March 2019)

## Techniques Used
- T1404: Exploitation for Privilege Escalation
- T1407: Download New Code at Runtime
- T1409: Stored Application Data
- T1418: Software Discovery
- T1421: System Network Connections Discovery
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1509: Non-Standard Port
- T1512: Video Capture
- T1513: Screen Capture
- T1532: Archive Collected Data
- T1533: Data from Local System
- T1636.001: Calendar Entries
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages


---

# S0301: Dendroid

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0301  
**Aliases:** Dendroid  
**Platforms:** Android  

## Description
[Dendroid](https://attack.mitre.org/software/S0301) is an Android remote access tool (RAT) primarily targeting Western countries. The RAT was available for purchase for $300 and came bundled with a utility to inject the RAT into legitimate applications.(Citation: Lookout-Dendroid)

## Techniques Used
- T1417.002: GUI Input Capture
- T1429: Audio Capture
- T1512: Video Capture
- T1533: Data from Local System
- T1582: SMS Control
- T1633.001: System Checks
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location


---

# S0312: WireLurker

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0312  

## Description
[WireLurker](https://attack.mitre.org/software/S0312) is a family of macOS malware that targets iOS devices connected over USB. (Citation: PaloAlto-WireLurker)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1458: Replication Through Removable Media


---

# S0505: Desert Scorpion

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0505  
**Aliases:** Desert Scorpion  
**Platforms:** Android  

## Description
[Desert Scorpion](https://attack.mitre.org/software/S0505) is surveillanceware that has targeted the Middle East, specifically individuals located in Palestine. [Desert Scorpion](https://attack.mitre.org/software/S0505) is suspected to have been operated by the threat actor [APT-C-23](https://attack.mitre.org/groups/G1028).(Citation: Lookout Desert Scorpion) 

There are multiple close variants of [Desert Scorpion](https://attack.mitre.org/software/S0505), such as VAMP(Citation: Unit42 VAMP 2017), GnatSpy(Citation: Trendmicro GnatSpy 2017), [FrozenCell](https://attack.mitre.org/software/S0577) and [SpyC23](https://attack.mitre.org/software/S1195), which add some additional functionality but are not significantly different from the original malware.

## Techniques Used
- T1407: Download New Code at Runtime
- T1409: Stored Application Data
- T1418: Software Discovery
- T1420: File and Directory Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1512: Video Capture
- T1532: Archive Collected Data
- T1533: Data from Local System
- T1582: SMS Control
- T1628.001: Suppress Application Icon
- T1630.002: File Deletion
- T1632.001: Code Signing Policy Modification
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1644: Out of Band Data


---

# S0289: Pegasus for iOS

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0289  
**Aliases:** Pegasus for iOS  
**Platforms:** iOS  

## Description
[Pegasus for iOS](https://attack.mitre.org/software/S0289) is the iOS version of malware that has reportedly been linked to the NSO Group. It has been advertised and sold to target high-value victims.(Citation: Lookout-Pegasus)(Citation: PegasusCitizenLab) The Android version is tracked separately under [Pegasus for Android](https://attack.mitre.org/software/S0316).

## Techniques Used
- T1404: Exploitation for Privilege Escalation
- T1409: Stored Application Data
- T1421: System Network Connections Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1456: Drive-By Compromise
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1644: Out of Band Data
- T1645: Compromise Client Software Binary
- T1658: Exploitation for Client Execution
- T1660: Phishing
- T1664: Exploitation for Initial Access


---

# S0329: Tangelo

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0329  
**Aliases:** Tangelo  
**Platforms:** iOS  

## Description
[Tangelo](https://attack.mitre.org/software/S0329) is iOS malware that is believed to be from the same developers as the [Stealth Mango](https://attack.mitre.org/software/S0328) Android malware. It is not a mobile application, but rather a Debian package that can only run on jailbroken iOS devices. (Citation: Lookout-StealthMango)

## Techniques Used
- T1409: Stored Application Data
- T1422: System Network Configuration Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1533: Data from Local System
- T1636.002: Call Log
- T1636.004: SMS Messages


---

# S0295: RCSAndroid

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0295  
**Aliases:** RCSAndroid  
**Platforms:** Android  

## Description
[RCSAndroid](https://attack.mitre.org/software/S0295) is Android malware. (Citation: TrendMicro-RCSAndroid)

## Techniques Used
- T1407: Download New Code at Runtime
- T1409: Stored Application Data
- T1414: Clipboard Data
- T1429: Audio Capture
- T1430: Location Tracking
- T1512: Video Capture
- T1533: Data from Local System
- T1636.004: SMS Messages
- T1644: Out of Band Data


---

# S0425: Corona Updates

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0425  
**Aliases:** Corona Updates, Wabi Music, Concipit1248  
**Platforms:** Android  

## Description
[Corona Updates](https://attack.mitre.org/software/S0425) is Android spyware that took advantage of the Coronavirus pandemic. The campaign distributing this spyware is tracked as Project Spy. Multiple variants of this spyware have been discovered to have been hosted on the Google Play Store.(Citation: TrendMicro Coronavirus Updates)

## Techniques Used
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1422.002: Wi-Fi Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1512: Video Capture
- T1517: Access Notifications
- T1533: Data from Local System
- T1582: SMS Control
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1639.001: Exfiltration Over Unencrypted Non-C2 Protocol


---

# S0327: Skygofree

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0327  
**Aliases:** Skygofree  
**Platforms:** Android  

## Description
[Skygofree](https://attack.mitre.org/software/S0327) is Android spyware that is believed to have been developed in 2014 and used through at least 2017. (Citation: Kaspersky-Skygofree)

## Techniques Used
- T1404: Exploitation for Privilege Escalation
- T1407: Download New Code at Runtime
- T1409: Stored Application Data
- T1429: Audio Capture
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1512: Video Capture
- T1644: Out of Band Data


---

# S0288: KeyRaider

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0288  

## Description
[KeyRaider](https://attack.mitre.org/software/S0288) is malware that steals Apple account credentials and other data from jailbroken iOS devices. It also has ransomware functionality. (Citation: Xiao-KeyRaider)

## Techniques Used
- T1426: System Information Discovery
- T1638: Adversary-in-the-Middle


---

# S0287: ZergHelper

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0287  

## Description
[ZergHelper](https://attack.mitre.org/software/S0287) is iOS riskware that was unique due to its apparent evasion of Apple's App Store review process. No malicious functionality was identified in the app, but it presents security risks. (Citation: Xiao-ZergHelper)

## Techniques Used
- T1407: Download New Code at Runtime


---

# S1225: CherryBlos

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1225  
**Aliases:** CherryBlos  
**Platforms:** Android  

## Description
[CherryBlos](https://attack.mitre.org/software/S1225) is an Android malware that steals credentials and redirects cryptocurrency to adversary-controlled wallets. [CherryBlos](https://attack.mitre.org/software/S1225) was labelled Robot 999 in its first appearance in April 2023; since then, various aliases have been used, including GPTalk, Happy Miner, and SynthNet. The threat actors behind [CherryBlos](https://attack.mitre.org/software/S1225) uploaded the malware to different Google Play regions, such as Malaysia, Vietnam, Indonesia, Philippines, Uganda, and Mexico.(Citation: TrendMicro_CherryBlos_July2023)

## Techniques Used
- T1406.002: Software Packing
- T1417: Input Capture
- T1418: Software Discovery
- T1420: File and Directory Discovery
- T1424: Process Discovery
- T1437.001: Web Protocols
- T1453: Abuse Accessibility Features
- T1541: Foreground Persistence
- T1544: Ingress Tool Transfer
- T1629: Impair Defenses
- T1646: Exfiltration Over C2 Channel
- T1655: Masquerading
- T1660: Phishing


---

# S0550: DoubleAgent

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0550  
**Aliases:** DoubleAgent  
**Platforms:** Android  

## Description
[DoubleAgent](https://attack.mitre.org/software/S0550) is a family of RAT malware dating back to 2013, known to target groups with contentious relationships with the Chinese government.(Citation: Lookout Uyghur Campaign)

## Techniques Used
- T1404: Exploitation for Privilege Escalation
- T1406: Obfuscated Files or Information
- T1407: Download New Code at Runtime
- T1409: Stored Application Data
- T1418: Software Discovery
- T1420: File and Directory Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1437: Application Layer Protocol
- T1533: Data from Local System
- T1623.001: Unix Shell
- T1628.001: Suppress Application Icon
- T1630.002: File Deletion
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1645: Compromise Client Software Binary
- T1655.001: Match Legitimate Name or Location


---

# S9005: DocSwap

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9005  
**Aliases:** DocSwap  
**Platforms:** Android  

## Description
[DocSwap](https://attack.mitre.org/software/S9005) is an Android malware first identified in 2025, and attributed to [Kimsuky](https://attack.mitre.org/groups/G0094). [DocSwap](https://attack.mitre.org/software/S9005)’s name is a combination of its Korean name “문서열람 인증 앱” (Document Viewing Authentication App) and a phishing page masquerading as CoinSwap at the C2 address. Based on [DocSwap](https://attack.mitre.org/software/S9005)’s name and Korean-language strings, [DocSwap](https://attack.mitre.org/software/S9005) potentially targets mobile device users in South Korea. Several variants of [DocSwap](https://attack.mitre.org/software/S9005) exist; one of the latest samples indicates that the adversary added a native decryption function that decrypts an internal APK.(Citation: EnkiWhiteHat_KimsukyDOCSWAP_Dec2025)(Citation: S2W_DocSwap_Mar2025)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1417.001: Keylogging
- T1418: Software Discovery
- T1420: File and Directory Discovery
- T1422: System Network Configuration Discovery
- T1422.002: Wi-Fi Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1453: Abuse Accessibility Features
- T1512: Video Capture
- T1533: Data from Local System
- T1541: Foreground Persistence
- T1544: Ingress Tool Transfer
- T1575: Native API
- T1616: Call Control
- T1624.001: Broadcast Receivers
- T1627: Execution Guardrails
- T1630.002: File Deletion
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1636.005: Accounts
- T1646: Exfiltration Over C2 Channel
- T1655.001: Match Legitimate Name or Location
- T1660: Phishing


---

# S0302: Twitoor

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0302  
**Aliases:** Twitoor  
**Platforms:** Android  

## Description
[Twitoor](https://attack.mitre.org/software/S0302) is a dropper application capable of receiving commands from social media.(Citation: ESET-Twitoor)

## Techniques Used
- T1481.003: One-Way Communication
- T1521: Encrypted Channel
- T1628.001: Suppress Application Icon


---

# S1080: Fakecalls

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1080  
**Aliases:** Fakecalls  
**Platforms:** Android  

## Description
[Fakecalls](https://attack.mitre.org/software/S1080) is an Android trojan, first detected in January 2021, that masquerades as South Korean banking apps. It has capabilities to intercept calls to banking institutions and even maintain realistic dialogues with the victim using pre-recorded audio snippets.(Citation: kaspersky_fakecalls_0422)

## Techniques Used
- T1429: Audio Capture
- T1430: Location Tracking
- T1512: Video Capture
- T1533: Data from Local System
- T1616: Call Control
- T1630.002: File Deletion
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1646: Exfiltration Over C2 Channel
- T1655.001: Match Legitimate Name or Location


---

# S1062: S.O.V.A.

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1062  
**Aliases:** S.O.V.A.  
**Platforms:** Android  

## Description
[S.O.V.A.](https://attack.mitre.org/software/S1062) is an Android banking trojan that was first identified in August 2021 and has subsequently been found in a variety of applications, including banking, cryptocurrency wallet/exchange, and shopping apps. [S.O.V.A.](https://attack.mitre.org/software/S1062), which is Russian for "owl", contains features not commonly found in Android malware, such as session cookie theft.(Citation: threatfabric_sova_0921)(Citation: cleafy_sova_1122)

## Techniques Used
- T1406.002: Software Packing
- T1409: Stored Application Data
- T1417.001: Keylogging
- T1417.002: GUI Input Capture
- T1418: Software Discovery
- T1426: System Information Discovery
- T1437.001: Web Protocols
- T1464: Network Denial of Service
- T1471: Data Encrypted for Impact
- T1513: Screen Capture
- T1516: Input Injection
- T1517: Access Notifications
- T1582: SMS Control
- T1628.001: Suppress Application Icon
- T1629.001: Prevent Application Removal
- T1630.001: Uninstall Malicious Application
- T1636.004: SMS Messages
- T1638: Adversary-in-the-Middle
- T1641.001: Transmitted Data Manipulation


---

# S0310: ANDROIDOS_ANSERVER.A

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0310  
**Aliases:** ANDROIDOS_ANSERVER.A  
**Platforms:** Android  

## Description
[ANDROIDOS_ANSERVER.A](https://attack.mitre.org/software/S0310) is Android malware that is unique because it uses encrypted content within a blog site for command and control. (Citation: TrendMicro-Anserver)

## Techniques Used
- T1422: System Network Configuration Discovery
- T1426: System Information Discovery
- T1481.001: Dead Drop Resolver


---

# S9030: SameCoin

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9030  
**Aliases:** SameCoin  
**Platforms:** Windows, Android  

## Description
[SameCoin](https://attack.mitre.org/software/S9030) is a multi-platform wiper with Windows and Android versions that has been used by [WIRTE](https://attack.mitre.org/groups/G0090) to target entities in the Middle East including in Israel.(Citation: Check Point Wirte NOV 2024)

## Techniques Used
- T1420: File and Directory Discovery
- T1662: Data Destruction


---

# S0315: DualToy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0315  

## Description
[DualToy](https://attack.mitre.org/software/S0315) is Windows malware that installs malicious applications onto Android and iOS devices connected over USB. (Citation: PaloAlto-DualToy)

## Techniques Used
- T1422: System Network Configuration Discovery
- T1458: Replication Through Removable Media


---

# S0485: Mandrake

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0485  
**Aliases:** Mandrake, oxide, briar, ricinus, darkmatter  
**Platforms:** Android  

## Description
[Mandrake](https://attack.mitre.org/software/S0485) is a sophisticated Android espionage platform that has been active in the wild since at least 2016. [Mandrake](https://attack.mitre.org/software/S0485) is very actively maintained, with sophisticated features and attacks that are executed with surgical precision.

[Mandrake](https://attack.mitre.org/software/S0485) has gone undetected for several years by providing legitimate, ad-free applications with social media and real reviews to back the apps. The malware is only activated when the operators issue a specific command.(Citation: Bitdefender Mandrake)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1407: Download New Code at Runtime
- T1409: Stored Application Data
- T1417.002: GUI Input Capture
- T1418: Software Discovery
- T1426: System Information Discovery
- T1430: Location Tracking
- T1481.002: Bidirectional Communication
- T1509: Non-Standard Port
- T1513: Screen Capture
- T1516: Input Injection
- T1517: Access Notifications
- T1541: Foreground Persistence
- T1544: Ingress Tool Transfer
- T1582: SMS Control
- T1628.001: Suppress Application Icon
- T1629.001: Prevent Application Removal
- T1629.003: Disable or Modify Tools
- T1630.002: File Deletion
- T1632.001: Code Signing Policy Modification
- T1633.001: System Checks
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1637.001: Domain Generation Algorithms
- T1655.001: Match Legitimate Name or Location


---

# S1128: HilalRAT

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1128  
**Aliases:** HilalRAT  
**Platforms:** Android  

## Description
[HilalRAT](https://attack.mitre.org/software/S1128) is a remote access-capable Android malware, developed and used by [UNC788](https://attack.mitre.org/groups/G1029).(Citation: Meta Adversarial Threat Report 2022)   [HilalRAT](https://attack.mitre.org/software/S1128) is capable of collecting data, such as device location, call logs, etc., and is capable of executing actions, such as activating a device's camera and microphone.(Citation: Meta Adversarial Threat Report 2022)

## Techniques Used
- T1409: Stored Application Data
- T1429: Audio Capture
- T1430: Location Tracking
- T1512: Video Capture
- T1636.003: Contact List
- T1636.004: SMS Messages


---

# S0314: X-Agent for Android

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0314  

## Description
[X-Agent for Android](https://attack.mitre.org/software/S0314) is Android malware that was placed in a repackaged version of a Ukrainian artillery targeting application. The malware reportedly retrieved general location data on where the victim device was used, and therefore could likely indicate the potential location of Ukrainian artillery. (Citation: CrowdStrike-Android) Is it tracked separately from the [CHOPSTICK](https://attack.mitre.org/software/S0023).

## Techniques Used
- T1430: Location Tracking
- T1655.001: Match Legitimate Name or Location


---

# S0479: DEFENSOR ID

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0479  
**Aliases:** DEFENSOR ID  
**Platforms:** Android  

## Description
[DEFENSOR ID](https://attack.mitre.org/software/S0479) is a banking trojan capable of clearing a victim’s bank account or cryptocurrency wallet and taking over email or social media accounts. [DEFENSOR ID](https://attack.mitre.org/software/S0479) performs the majority of its malicious functionality by abusing Android’s accessibility service.(Citation: ESET DEFENSOR ID)

## Techniques Used
- T1418: Software Discovery
- T1437.001: Web Protocols
- T1513: Screen Capture
- T1516: Input Injection
- T1624.001: Broadcast Receivers


---

# S1094: BRATA

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1094  
**Aliases:** BRATA  
**Platforms:** Android  

## Description
[BRATA](https://attack.mitre.org/software/S1094) (Brazilian Remote Access Tool, Android), is an evolving Android malware strain, detected in late 2018 and again in late 2021. Originating in Brazil, [BRATA](https://attack.mitre.org/software/S1094) was later also found in the UK, Poland, Italy, Spain, and USA, where it is believed to have targeted financial institutions such as banks. There are currently three known variants of [BRATA](https://attack.mitre.org/software/S1094).(Citation: securelist_brata_0819)(Citation: cleafy_brata_0122)(Citation: mcafee_brata_0421)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1406.002: Software Packing
- T1407: Download New Code at Runtime
- T1417.001: Keylogging
- T1417.002: GUI Input Capture
- T1418.001: Security Software Discovery
- T1426: System Information Discovery
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1461: Lockscreen Bypass
- T1513: Screen Capture
- T1516: Input Injection
- T1532: Archive Collected Data
- T1533: Data from Local System
- T1616: Call Control
- T1627.001: Geofencing
- T1628.002: User Evasion
- T1629.003: Disable or Modify Tools
- T1630.001: Uninstall Malicious Application
- T1633.001: System Checks
- T1641.001: Transmitted Data Manipulation
- T1646: Exfiltration Over C2 Channel
- T1655.001: Match Legitimate Name or Location
- T1660: Phishing
- T1662: Data Destruction
- T1663: Remote Access Software
- T1664: Exploitation for Initial Access


---

# S1185: LightSpy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1185  
**Aliases:** LightSpy  
**Platforms:** Android, Windows, iOS, macOS  

## Description
First observed in 2018, LightSpy is a modular malware family that initially targeted iOS devices in Southern Asia before expanding to Android and macOS platforms. It consists of a downloader, a main executable that manages network communications, and functionality-specific modules, typically implemented as `.dylib` files (iOS, macOS) or `.apk` files (Android). LightSpy can collect VoIP call recordings, SMS messages, and credential stores, which are then exfiltrated to a command and control (C2) server.(Citation: MelikovBlackBerry LightSpy 2024)

## Techniques Used
- T1398: Boot or Logon Initialization Scripts
- T1404: Exploitation for Privilege Escalation
- T1406: Obfuscated Files or Information
- T1409: Stored Application Data
- T1418: Software Discovery
- T1421: System Network Connections Discovery
- T1422: System Network Configuration Discovery
- T1422.002: Wi-Fi Discovery
- T1423: Network Service Scanning
- T1424: Process Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1456: Drive-By Compromise
- T1509: Non-Standard Port
- T1512: Video Capture
- T1513: Screen Capture
- T1532: Archive Collected Data
- T1533: Data from Local System
- T1544: Ingress Tool Transfer
- T1575: Native API
- T1582: SMS Control
- T1623: Command and Scripting Interpreter
- T1631: Process Injection
- T1634.001: Keychain
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1642: Endpoint Denial of Service
- T1646: Exfiltration Over C2 Channel
- T1655: Masquerading
- T1658: Exploitation for Client Execution
- T1660: Phishing
- T1662: Data Destruction


---

# S0303: MazarBOT

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0303  

## Description
[MazarBOT](https://attack.mitre.org/software/S0303) is Android malware that was distributed via SMS in Denmark in 2016. (Citation: Tripwire-MazarBOT)

## Techniques Used
- T1636.004: SMS Messages
- T1643: Generate Traffic from Victim


---

# S0423: Ginp

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0423  
**Aliases:** Ginp  
**Platforms:** Android  

## Description
[Ginp](https://attack.mitre.org/software/S0423) is an Android banking trojan that has been used to target Spanish banks. Some of the code was taken directly from [Anubis](https://attack.mitre.org/software/S0422).(Citation: ThreatFabric Ginp)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1417.002: GUI Input Capture
- T1418: Software Discovery
- T1513: Screen Capture
- T1516: Input Injection
- T1533: Data from Local System
- T1582: SMS Control
- T1628.001: Suppress Application Icon
- T1633.001: System Checks
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location


---

# S0321: HummingWhale

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0321  

## Description
[HummingWhale](https://attack.mitre.org/software/S0321) is an Android malware family that performs ad fraud. (Citation: ArsTechnica-HummingWhale)

## Techniques Used
- T1643: Generate Traffic from Victim


---

# S0507: eSurv

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0507  
**Aliases:** eSurv  
**Platforms:** Android, iOS  

## Description
[eSurv](https://attack.mitre.org/software/S0507) is mobile surveillanceware designed for the lawful intercept market that was developed over the course of many years.(Citation: Lookout eSurv)

## Techniques Used
- T1407: Download New Code at Runtime
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1521.002: Asymmetric Cryptography
- T1521.003: SSL Pinning
- T1533: Data from Local System
- T1627.001: Geofencing
- T1636.003: Contact List
- T1646: Exfiltration Over C2 Channel


---

# S1069: TangleBot

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1069  
**Aliases:** TangleBot  
**Platforms:** Android  

## Description
[TangleBot](https://attack.mitre.org/software/S1069) is SMS malware that was initially observed in September 2021, primarily targeting mobile users in the United States and Canada. [TangleBot](https://attack.mitre.org/software/S1069) has used SMS text message lures about COVID-19 regulations and vaccines to trick mobile users into downloading the malware, similar to [FluBot](https://attack.mitre.org/software/S1067) Android malware campaigns.(Citation: cloudmark_tanglebot_0921)

## Techniques Used
- T1417.002: GUI Input Capture
- T1418: Software Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1512: Video Capture
- T1513: Screen Capture
- T1533: Data from Local System
- T1582: SMS Control
- T1616: Call Control
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages


---

# S0407: Monokle

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0407  
**Aliases:** Monokle  
**Platforms:** Android  

## Description
[Monokle](https://attack.mitre.org/software/S0407) is targeted, sophisticated mobile surveillanceware. It is developed for Android, but there are some code artifacts that suggests an iOS version may be in development.(Citation: Lookout-Monokle)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1417.001: Keylogging
- T1418: Software Discovery
- T1421: System Network Connections Discovery
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1422.002: Wi-Fi Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1512: Video Capture
- T1513: Screen Capture
- T1533: Data from Local System
- T1544: Ingress Tool Transfer
- T1616: Call Control
- T1617: Hooking
- T1630.002: File Deletion
- T1636.001: Calendar Entries
- T1636.002: Call Log
- T1636.003: Contact List
- T1638: Adversary-in-the-Middle
- T1640: Account Access Removal
- T1644: Out of Band Data
- T1645: Compromise Client Software Binary


---

# S1241: RatMilad

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1241  
**Aliases:** RatMilad  
**Platforms:** Android  

## Description
[RatMilad](https://attack.mitre.org/software/S1241) is an Android remote access tool (RAT) with spyware functionality that has been used to target enterprise mobile devices in the Middle East since at least 2021. Variants of [RatMilad](https://attack.mitre.org/software/S1241) have been disguised as VPN applications and a fake app named NumRent. Upon installation, [RatMilad](https://attack.mitre.org/software/S1241) employs multiple [Collection](https://attack.mitre.org/tactics/TA0035) techniques to collect sensitive information before uploading the collected data to its command and control (C2) server. (Citation: ZimperiumGupta_RatMilad_Oct2022)

## Techniques Used
- T1407: Download New Code at Runtime
- T1414: Clipboard Data
- T1418: Software Discovery
- T1420: File and Directory Discovery
- T1422: System Network Configuration Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1512: Video Capture
- T1533: Data from Local System
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1636.005: Accounts
- T1646: Exfiltration Over C2 Channel
- T1660: Phishing
- T1662: Data Destruction


---

# S1243: DCHSpy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1243  
**Aliases:** DCHSpy  
**Platforms:** Android  

## Description
[DCHSpy](https://attack.mitre.org/software/S1243) is an Android spyware likely used by [MuddyWater](https://attack.mitre.org/groups/G0069). [DCHSpy](https://attack.mitre.org/software/S1243) uses political decoys and masquerades as legitimate applications, such as VPNs and banking applications, to trick victims into downloading the malware. Once downloaded, [DCHSpy](https://attack.mitre.org/software/S1243) collects information from the device and exfiltrates the data to the command and control (C2) server.(Citation: Lookout_DCHSpy_July2025)

## Techniques Used
- T1409: Stored Application Data
- T1429: Audio Capture
- T1430: Location Tracking
- T1437: Application Layer Protocol
- T1512: Video Capture
- T1532: Archive Collected Data
- T1533: Data from Local System
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1636.005: Accounts
- T1655.001: Match Legitimate Name or Location


---

# S0539: Red Alert 2.0

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0539  
**Aliases:** Red Alert 2.0  
**Platforms:** Android  

## Description
[Red Alert 2.0](https://attack.mitre.org/software/S0539) is a banking trojan that masquerades as a VPN client.(Citation: Sophos Red Alert 2.0)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1407: Download New Code at Runtime
- T1417.002: GUI Input Capture
- T1418: Software Discovery
- T1437.001: Web Protocols
- T1481.001: Dead Drop Resolver
- T1509: Non-Standard Port
- T1582: SMS Control
- T1626.001: Device Administrator Permissions
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location


---

# S0418: ViceLeaker

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0418  
**Aliases:** ViceLeaker, Triout  
**Platforms:** Android  

## Description
[ViceLeaker](https://attack.mitre.org/software/S0418) is a spyware framework, capable of extensive surveillance and data exfiltration operations, primarily targeting devices belonging to Israeli citizens.(Citation: SecureList - ViceLeaker 2019)(Citation: Bitdefender - Triout 2018)

## Techniques Used
- T1418: Software Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1512: Video Capture
- T1533: Data from Local System
- T1544: Ingress Tool Transfer
- T1628.001: Suppress Application Icon
- T1630.002: File Deletion
- T1636.002: Call Log
- T1636.004: SMS Messages
- T1646: Exfiltration Over C2 Channel
- T1655.001: Match Legitimate Name or Location


---

# S9006: VajraSpy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9006  
**Aliases:** VajraSpy  
**Platforms:** Android  

## Description
[VajraSpy](https://attack.mitre.org/software/S9006) is Android malware distributed via trojanized messaging and news applications. It has been used to target individuals in Pakistan and India since at least 2021 and has been delivered through the Google Play Store, malicious domains, and other uncontrolled distribution channels. [VajraSpy](https://attack.mitre.org/software/S9006) is attributed with high confidence to [Patchwork](https://attack.mitre.org/groups/G0040) which has used the malware to conduct targeted espionage, primarily against devices in Pakistan.(Citation: ESET_VajraSpy_Feb2024)(Citation: ArcticWolf_DroppingElephant_July2025)(Citation: K7Dhanalakshmi_VajraSpy_April2022)

## Techniques Used
- T1409: Stored Application Data
- T1417.001: Keylogging
- T1418: Software Discovery
- T1420: File and Directory Discovery
- T1422.002: Wi-Fi Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1453: Abuse Accessibility Features
- T1461: Lockscreen Bypass
- T1481.002: Bidirectional Communication
- T1512: Video Capture
- T1517: Access Notifications
- T1533: Data from Local System
- T1616: Call Control
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1636.005: Accounts
- T1639.001: Exfiltration Over Unencrypted Non-C2 Protocol
- T1646: Exfiltration Over C2 Channel
- T1655: Masquerading
- T1660: Phishing


---

# S1093: FlyTrap

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1093  
**Aliases:** FlyTrap  
**Platforms:** Android  

## Description
[FlyTrap](https://attack.mitre.org/software/S1093) is an Android trojan, first detected in March 2021, that uses social engineering tactics to compromise Facebook accounts. [FlyTrap](https://attack.mitre.org/software/S1093) was initially detected through infected apps on the Google Play store, and is believed to have impacted over 10,000 victims across at least 140 countries.(Citation: Trend Micro FlyTrap)

## Techniques Used
- T1409: Stored Application Data
- T1417.002: GUI Input Capture
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1646: Exfiltration Over C2 Channel


---

# S0509: FakeSpy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0509  
**Aliases:** FakeSpy  
**Platforms:** Android  

## Description
[FakeSpy](https://attack.mitre.org/software/S0509) is Android spyware that has been operated by the Chinese threat actor behind the Roaming Mantis campaigns.(Citation: Cybereason FakeSpy)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1409: Stored Application Data
- T1418: Software Discovery
- T1421: System Network Connections Discovery
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1426: System Information Discovery
- T1437.001: Web Protocols
- T1582: SMS Control
- T1624.001: Broadcast Receivers
- T1628.001: Suppress Application Icon
- T1633.001: System Checks
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location


---

# S0324: SpyDealer

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0324  
**Aliases:** SpyDealer  
**Platforms:** Android  

## Description
[SpyDealer](https://attack.mitre.org/software/S0324) is Android malware that exfiltrates sensitive data from Android devices. (Citation: PaloAlto-SpyDealer)

## Techniques Used
- T1404: Exploitation for Privilege Escalation
- T1407: Download New Code at Runtime
- T1409: Stored Application Data
- T1422: System Network Configuration Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1512: Video Capture
- T1513: Screen Capture
- T1624.001: Broadcast Receivers
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1644: Out of Band Data
- T1645: Compromise Client Software Binary


---

# S0426: Concipit1248

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0426  
**Aliases:** Concipit1248, Corona Updates  
**Platforms:** iOS  

## Description
[Concipit1248](https://attack.mitre.org/software/S0426) is iOS spyware that was discovered using the same name as the developer of the Android spyware [Corona Updates](https://attack.mitre.org/software/S0425). Further investigation revealed that the two pieces of software contained the same C2 URL and similar functionality.(Citation: TrendMicro Coronavirus Updates)

## Techniques Used
- T1437.001: Web Protocols
- T1512: Video Capture
- T1533: Data from Local System


---

# S0313: RuMMS

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0313  

## Description
[RuMMS](https://attack.mitre.org/software/S0313) is an Android malware family. (Citation: FireEye-RuMMS)

## Techniques Used
- T1422: System Network Configuration Discovery
- T1426: System Information Discovery
- T1437.001: Web Protocols
- T1636.004: SMS Messages


---

# S0316: Pegasus for Android

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0316  
**Aliases:** Pegasus for Android, Chrysaor  
**Platforms:** Android  

## Description
[Pegasus for Android](https://attack.mitre.org/software/S0316) is the Android version of malware that has reportedly been linked to the NSO Group. (Citation: Lookout-PegasusAndroid) (Citation: Google-Chrysaor) The iOS version is tracked separately under [Pegasus for iOS](https://attack.mitre.org/software/S0289).

## Techniques Used
- T1404: Exploitation for Privilege Escalation
- T1409: Stored Application Data
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1422.002: Wi-Fi Discovery
- T1429: Audio Capture
- T1512: Video Capture
- T1624.001: Broadcast Receivers
- T1636.001: Calendar Entries
- T1636.002: Call Log
- T1636.003: Contact List
- T1644: Out of Band Data
- T1645: Compromise Client Software Binary


---

# S1195: SpyC23

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1195  
**Aliases:** SpyC23  
**Platforms:** Android  

## Description
[SpyC23](https://attack.mitre.org/software/S1195) is a mobile malware that has been used by [APT-C-23](https://attack.mitre.org/groups/G1028) since at least 2017. [SpyC23](https://attack.mitre.org/software/S1195) has been observed primarily targeting Android devices in the Middle East.(Citation: welivesecurity_apt-c-23) 

There are multiple close variants of [SpyC23](https://attack.mitre.org/software/S1195), such as VAMP(Citation: Unit42 VAMP 2017), GnatSpy(Citation: Trendmicro GnatSpy 2017), [Desert Scorpion](https://attack.mitre.org/software/S0505) and [FrozenCell](https://attack.mitre.org/software/S0577), which add some additional functionality but are not significantly different from the original malware.

## Techniques Used
- T1406: Obfuscated Files or Information
- T1429: Audio Capture
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1512: Video Capture
- T1513: Screen Capture
- T1517: Access Notifications
- T1533: Data from Local System
- T1544: Ingress Tool Transfer
- T1582: SMS Control
- T1616: Call Control
- T1624.001: Broadcast Receivers
- T1628.001: Suppress Application Icon
- T1628.002: User Evasion
- T1629.003: Disable or Modify Tools
- T1633: Virtualization/Sandbox Evasion
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1644: Out of Band Data
- T1655.001: Match Legitimate Name or Location


---

# S0577: FrozenCell

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0577  
**Aliases:** FrozenCell  
**Platforms:** Android  

## Description
[FrozenCell](https://attack.mitre.org/software/S0577) is the mobile component of a family of surveillanceware, with a corresponding desktop component known as KasperAgent and [Micropsia](https://attack.mitre.org/software/S0339).(Citation: Lookout FrozenCell) 

There are multiple close variants of [FrozenCell](https://attack.mitre.org/software/S0577), such as VAMP(Citation: Unit42 VAMP 2017), GnatSpy(Citation: Trendmicro GnatSpy 2017), [Desert Scorpion](https://attack.mitre.org/software/S0505) and [SpyC23](https://attack.mitre.org/software/S1195), which add some additional functionality but are not significantly different from the original malware.

## Techniques Used
- T1407: Download New Code at Runtime
- T1409: Stored Application Data
- T1420: File and Directory Discovery
- T1422: System Network Configuration Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1532: Archive Collected Data
- T1533: Data from Local System
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location


---

# S0524: AndroidOS/MalLocker.B

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0524  
**Aliases:** AndroidOS/MalLocker.B  
**Platforms:** Android  

## Description
[AndroidOS/MalLocker.B](https://attack.mitre.org/software/S0524) is a variant of a ransomware family targeting Android devices. It prevents the user from interacting with the UI by displaying a screen containing a ransom note over all other windows. (Citation: Microsoft MalLockerB)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1624.001: Broadcast Receivers
- T1629.002: Device Lockout
- T1655.001: Match Legitimate Name or Location


---

# S1055: SharkBot

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1055  
**Aliases:** SharkBot  
**Platforms:** Android  

## Description
[SharkBot](https://attack.mitre.org/software/S1055) is a banking malware, first discovered in October 2021, that tries to initiate money transfers directly from compromised devices by abusing Accessibility Services.(Citation: nccgroup_sharkbot_0322)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1407: Download New Code at Runtime
- T1417.001: Keylogging
- T1417.002: GUI Input Capture
- T1424: Process Discovery
- T1437.001: Web Protocols
- T1516: Input Injection
- T1517: Access Notifications
- T1521.001: Symmetric Cryptography
- T1521.002: Asymmetric Cryptography
- T1544: Ingress Tool Transfer
- T1582: SMS Control
- T1630.001: Uninstall Malicious Application
- T1636.004: SMS Messages
- T1637.001: Domain Generation Algorithms
- T1644: Out of Band Data
- T1646: Exfiltration Over C2 Channel
- T1661: Application Versioning


---

# S0326: RedDrop

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0326  
**Aliases:** RedDrop  
**Platforms:** Android  

## Description
[RedDrop](https://attack.mitre.org/software/S0326) is an Android malware family that exfiltrates sensitive data from devices. (Citation: Wandera-RedDrop)

## Techniques Used
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1422.002: Wi-Fi Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1437.001: Web Protocols
- T1544: Ingress Tool Transfer
- T1643: Generate Traffic from Victim
- T1646: Exfiltration Over C2 Channel


---

# S0555: CHEMISTGAMES

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0555  
**Aliases:** CHEMISTGAMES  
**Platforms:** Android  

## Description
[CHEMISTGAMES](https://attack.mitre.org/software/S0555) is a modular backdoor that has been deployed by [Sandworm Team](https://attack.mitre.org/groups/G0034).(Citation: CYBERWARCON CHEMISTGAMES)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1407: Download New Code at Runtime
- T1426: System Information Discovery
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1474.003: Compromise Software Supply Chain
- T1521.002: Asymmetric Cryptography
- T1533: Data from Local System
- T1575: Native API
- T1623.001: Unix Shell
- T1655.001: Match Legitimate Name or Location


---

# S0311: YiSpecter

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0311  
**Aliases:** YiSpecter  
**Platforms:** Android, iOS  

## Description
[YiSpecter](https://attack.mitre.org/software/S0311) is a family of iOS and Android malware, first detected in November 2014, targeting users in mainland China and Taiwan. [YiSpecter](https://attack.mitre.org/software/S0311) abuses private APIs in iOS to infect both jailbroken and non-jailbroken devices.(Citation: paloalto_yispecter_1015)

## Techniques Used
- T1407: Download New Code at Runtime
- T1409: Stored Application Data
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1424: Process Discovery
- T1426: System Information Discovery
- T1437.001: Web Protocols
- T1456: Drive-By Compromise
- T1577: Compromise Application Executable
- T1625: Hijack Execution Flow
- T1628.001: Suppress Application Icon
- T1632.001: Code Signing Policy Modification


---

# S0307: Trojan-SMS.AndroidOS.Agent.ao

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0307  

## Description
[Trojan-SMS.AndroidOS.Agent.ao](https://attack.mitre.org/software/S0307) is Android malware. (Citation: Kaspersky-MobileMalware)

## Techniques Used
- T1437.001: Web Protocols


---

# S1079: BOULDSPY

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1079  
**Aliases:** BOULDSPY  
**Platforms:** Android  

## Description
[BOULDSPY](https://attack.mitre.org/software/S1079) is an Android malware, detected in early 2023, with surveillance and remote-control capabilities. Analysis of exfiltrated C2 data suggests that [BOULDSPY](https://attack.mitre.org/software/S1079) primarily targeted minority groups in Iran.(Citation: lookout_bouldspy_0423)

## Techniques Used
- T1398: Boot or Logon Initialization Scripts
- T1407: Download New Code at Runtime
- T1409: Stored Application Data
- T1414: Clipboard Data
- T1417.001: Keylogging
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1422.002: Wi-Fi Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1512: Video Capture
- T1513: Screen Capture
- T1532: Archive Collected Data
- T1533: Data from Local System
- T1577: Compromise Application Executable
- T1624: Event Triggered Execution
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1644: Out of Band Data
- T1646: Exfiltration Over C2 Channel
- T1655.001: Match Legitimate Name or Location


---

# S0422: Anubis

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0422  
**Aliases:** Anubis  
**Platforms:** Android  

## Description
[Anubis](https://attack.mitre.org/software/S0422) is Android malware that was originally used for cyber espionage, and has been retooled as a banking trojan.(Citation: Cofense Anubis)

## Techniques Used
- T1407: Download New Code at Runtime
- T1417.001: Keylogging
- T1417.002: GUI Input Capture
- T1418: Software Discovery
- T1424: Process Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1453: Abuse Accessibility Features
- T1471: Data Encrypted for Impact
- T1481.001: Dead Drop Resolver
- T1513: Screen Capture
- T1532: Archive Collected Data
- T1533: Data from Local System
- T1582: SMS Control
- T1616: Call Control
- T1629.001: Prevent Application Removal
- T1629.003: Disable or Modify Tools
- T1633.001: System Checks
- T1636.003: Contact List
- T1655.001: Match Legitimate Name or Location


---

# S0292: AndroRAT

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0292  
**Aliases:** AndroRAT  
**Platforms:** Android  

## Description
[AndroRAT](https://attack.mitre.org/software/S0292) is an open-source remote access tool for Android devices. [AndroRAT](https://attack.mitre.org/software/S0292) is capable of collecting data, such as device location, call logs, etc., and is capable of executing actions, such as sending SMS messages and taking pictures.(Citation: Lookout-EnterpriseApps)(Citation: github_androrat)(Citation: Forcepoint BITTER Pakistan Oct 2016) It is originally available through the `The404Hacking` Github repository.(Citation: github_androrat)

## Techniques Used
- T1422: System Network Configuration Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1512: Video Capture
- T1582: SMS Control
- T1616: Call Control
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location


---

# S0182: FinFisher

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0182  
**Aliases:** FinFisher, FinSpy  
**Platforms:** Windows, Android  

## Description
[FinFisher](https://attack.mitre.org/software/S0182) is a government-grade commercial surveillance spyware reportedly sold exclusively to government agencies for use in targeted and lawful criminal investigations. It is heavily obfuscated and uses multiple anti-analysis techniques. It has other variants including [Wingbird](https://attack.mitre.org/software/S0176). (Citation: FinFisher Citation) (Citation: Microsoft SIR Vol 21) (Citation: FireEye FinSpy Sept 2017) (Citation: Securelist BlackOasis Oct 2017) (Citation: Microsoft FinFisher March 2018)

## Techniques Used
- T1404: Exploitation for Privilege Escalation
- T1429: Audio Capture
- T1430: Location Tracking
- T1636.002: Call Log
- T1636.004: SMS Messages


---

# S0440: Agent Smith

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0440  
**Aliases:** Agent Smith  
**Platforms:** Android  

## Description
[Agent Smith](https://attack.mitre.org/software/S0440) is mobile malware that generates financial gain by replacing legitimate applications on devices with malicious versions that include fraudulent ads. As of July 2019 [Agent Smith](https://attack.mitre.org/software/S0440) had infected around 25 million devices, primarily targeting India though effects had been observed in other Asian countries as well as Saudi Arabia, the United Kingdom, and the United States.(Citation: CheckPoint Agent Smith)

## Techniques Used
- T1404: Exploitation for Privilege Escalation
- T1406.001: Steganography
- T1418: Software Discovery
- T1424: Process Discovery
- T1577: Compromise Application Executable
- T1628.001: Suppress Application Icon
- T1630.002: File Deletion
- T1643: Generate Traffic from Victim
- T1655.001: Match Legitimate Name or Location


---

# S0540: Asacub

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0540  
**Aliases:** Asacub, Trojan-SMS.AndroidOS.Smaps  
**Platforms:** Android  

## Description
[Asacub](https://attack.mitre.org/software/S0540) is a banking trojan that attempts to steal money from victims’ bank accounts. It attempts to do this by initiating a wire transfer via SMS message from compromised devices.(Citation: Securelist Asacub)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1426: System Information Discovery
- T1437.001: Web Protocols
- T1532: Archive Collected Data
- T1575: Native API
- T1582: SMS Control
- T1626.001: Device Administrator Permissions
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location


---

# S0536: GPlayed

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0536  
**Aliases:** GPlayed  
**Platforms:** Android  

## Description
[GPlayed](https://attack.mitre.org/software/S0536) is an Android trojan with a broad range of capabilities.(Citation: Talos GPlayed)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1407: Download New Code at Runtime
- T1417.002: GUI Input Capture
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1426: System Information Discovery
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1533: Data from Local System
- T1582: SMS Control
- T1603: Scheduled Task/Job
- T1624.001: Broadcast Receivers
- T1626.001: Device Administrator Permissions
- T1630.002: File Deletion
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1642: Endpoint Denial of Service
- T1655.001: Match Legitimate Name or Location


---

# S0478: EventBot

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0478  
**Aliases:** EventBot  
**Platforms:** Android  

## Description
[EventBot](https://attack.mitre.org/software/S0478) is an Android banking trojan and information stealer that abuses Android’s accessibility service to steal data from various applications.(Citation: Cybereason EventBot) [EventBot](https://attack.mitre.org/software/S0478) was designed to target over 200 different banking and financial applications, the majority of which are European bank and cryptocurrency exchange applications.(Citation: Cybereason EventBot)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1407: Download New Code at Runtime
- T1417.001: Keylogging
- T1417.002: GUI Input Capture
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1426: System Information Discovery
- T1437.001: Web Protocols
- T1513: Screen Capture
- T1521.001: Symmetric Cryptography
- T1624.001: Broadcast Receivers
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location


---

# S0544: HenBox

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0544  
**Aliases:** HenBox  
**Platforms:** Android  

## Description
[HenBox](https://attack.mitre.org/software/S0544) is Android malware that attempts to only execute on Xiaomi devices running the MIUI operating system. [HenBox](https://attack.mitre.org/software/S0544) has primarily been used to target Uyghurs, a minority Turkic ethnic group.(Citation: Palo Alto HenBox)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1407: Download New Code at Runtime
- T1418: Software Discovery
- T1424: Process Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1512: Video Capture
- T1533: Data from Local System
- T1575: Native API
- T1623.001: Unix Shell
- T1624.001: Broadcast Receivers
- T1633.001: System Checks
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location


---

# S1215: Binary Validator

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1215  
**Aliases:** Binary Validator  
**Platforms:** iOS  

## Description
[Binary Validator](https://attack.mitre.org/software/S1215) is a Mach-O binary file used during [Operation Triangulation](https://attack.mitre.org/campaigns/C0054).(Citation: SecureList OpTriangulation 23Oct2023) [Binary Validator](https://attack.mitre.org/software/S1215) first collects information about the device, such as the device's phone number and a list of installed applications, before the deployment of the [TriangleDB](https://attack.mitre.org/software/S1216) implant.  After the actions are completed and the data is collected, [Binary Validator](https://attack.mitre.org/software/S1215) encrypts and sends the data to the C2 server, and in turn, the C2 server sends the [TriangleDB](https://attack.mitre.org/software/S1216) implant.

## Techniques Used
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1424: Process Discovery
- T1533: Data from Local System
- T1627: Execution Guardrails
- T1630.002: File Deletion
- T1646: Exfiltration Over C2 Channel


---

# S1231: GodFather

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1231  
**Aliases:** GodFather  
**Platforms:** Android  

## Description
[GodFather](https://attack.mitre.org/software/S1231) is an Android banking malware that uses virtualization to mimic legitimate applications and abuses accessibility services and other permissions to evade detection and exfiltrate sensitive data. First identified in 2020, [GodFather](https://attack.mitre.org/software/S1231) targets nearly 500 banking applications, cryptocurrency wallets, and exchanges worldwide; however, its virtualization-based attacks have primarily focused on several Turkish financial institutions. This capability enables threat actors to steal banking credentials and other sensitive account information. (Citation: ZimperiumOrtegaPratapagiri_GodFather_Jun2025)(Citation: MerkleScience_Godfather_April2023)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1417: Input Capture
- T1417.001: Keylogging
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1437.001: Web Protocols
- T1453: Abuse Accessibility Features
- T1516: Input Injection
- T1544: Ingress Tool Transfer
- T1575: Native API
- T1582: SMS Control
- T1603: Scheduled Task/Job
- T1616: Call Control
- T1617: Hooking
- T1624: Event Triggered Execution
- T1629: Impair Defenses
- T1629.001: Prevent Application Removal
- T1630: Indicator Removal on Host
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1646: Exfiltration Over C2 Channel
- T1655.001: Match Legitimate Name or Location
- T1660: Phishing
- T1670: Virtualization Solution


---

# S0403: Riltok

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0403  
**Aliases:** Riltok  
**Platforms:** Android  

## Description
[Riltok](https://attack.mitre.org/software/S0403) is banking malware that uses phishing popups to collect user credentials.(Citation: Kaspersky Riltok June 2019)

## Techniques Used
- T1417.002: GUI Input Capture
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1426: System Information Discovery
- T1437.001: Web Protocols
- T1516: Input Injection
- T1636.003: Contact List
- T1636.004: SMS Messages


---

# S0421: GolfSpy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0421  
**Aliases:** GolfSpy  
**Platforms:** Android  

## Description
[GolfSpy](https://attack.mitre.org/software/S0421) is Android spyware deployed by the group [Bouncing Golf](https://attack.mitre.org/groups/G0097).(Citation: Trend Micro Bouncing Golf 2019)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1414: Clipboard Data
- T1418: Software Discovery
- T1424: Process Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1512: Video Capture
- T1513: Screen Capture
- T1532: Archive Collected Data
- T1533: Data from Local System
- T1624.001: Broadcast Receivers
- T1630.002: File Deletion
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1646: Exfiltration Over C2 Channel


---

# S0399: Pallas

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0399  
**Aliases:** Pallas  
**Platforms:** Android  

## Description
[Pallas](https://attack.mitre.org/software/S0399) is mobile surveillanceware that was custom-developed by [Dark Caracal](https://attack.mitre.org/groups/G0070).(Citation: Lookout Dark Caracal Jan 2018)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1409: Stored Application Data
- T1417.002: GUI Input Capture
- T1418: Software Discovery
- T1421: System Network Connections Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1512: Video Capture
- T1630.002: File Deletion
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1646: Exfiltration Over C2 Channel


---

# S0602: Circles

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0602  
**Aliases:** Circles  

## Description
[Circles](https://attack.mitre.org/software/S0602) reportedly takes advantage of Signaling System 7 (SS7) weaknesses, the protocol suite used to route phone calls, to both track the location of mobile devices and intercept voice calls and SMS messages. It can be connected to a telecommunications company’s infrastructure or purchased as a cloud service. Circles has reportedly been linked to the NSO Group.(Citation: CitizenLab Circles)

## Techniques Used
- T1430.002: Impersonate SS7 Nodes


---

# S0558: Tiktok Pro

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0558  
**Aliases:** Tiktok Pro  
**Platforms:** Android  

## Description
[Tiktok Pro](https://attack.mitre.org/software/S0558) is spyware that has been masquerading as the TikTok application.(Citation: Zscaler TikTok Spyware)

## Techniques Used
- T1417.002: GUI Input Capture
- T1418: Software Discovery
- T1420: File and Directory Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1512: Video Capture
- T1513: Screen Capture
- T1533: Data from Local System
- T1541: Foreground Persistence
- T1582: SMS Control
- T1603: Scheduled Task/Job
- T1623.001: Unix Shell
- T1624.001: Broadcast Receivers
- T1628.001: Suppress Application Icon
- T1630.002: File Deletion
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location


---

# S0291: PJApps

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0291  

## Description
[PJApps](https://attack.mitre.org/software/S0291) is an Android malware family. (Citation: Lookout-EnterpriseApps)

## Techniques Used
- T1422: System Network Configuration Discovery
- T1430: Location Tracking
- T1643: Generate Traffic from Victim


---

# S0294: ShiftyBug

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0294  

## Description
[ShiftyBug](https://attack.mitre.org/software/S0294) is an auto-rooting adware family of malware for Android. The family is very similar to the other Android families known as Shedun, Shuanet, Kemoge, though it is not believed all the families were created by the same group. (Citation: Lookout-Adware)

## Techniques Used
- T1404: Exploitation for Privilege Escalation
- T1645: Compromise Client Software Binary


---

# S0322: HummingBad

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0322  
**Aliases:** HummingBad  

## Description
[HummingBad](https://attack.mitre.org/software/S0322) is a family of Android malware that generates fraudulent advertising revenue and has the ability to obtain root access on older, vulnerable versions of Android. (Citation: ArsTechnica-HummingBad)

## Techniques Used
- T1404: Exploitation for Privilege Escalation
- T1643: Generate Traffic from Victim


---

# S0522: Exobot

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0522  
**Aliases:** Exobot  
**Platforms:** Android  

## Description
[Exobot](https://attack.mitre.org/software/S0522) is Android banking malware, primarily targeting financial institutions in Germany, Austria, and France.(Citation: Threat Fabric Exobot)

## Techniques Used
- T1417.001: Keylogging
- T1417.002: GUI Input Capture
- T1418.001: Security Software Discovery
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1426: System Information Discovery
- T1437.001: Web Protocols
- T1582: SMS Control
- T1604: Proxy Through Victim
- T1624.001: Broadcast Receivers
- T1626.001: Device Administrator Permissions
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1642: Endpoint Denial of Service
- T1655.001: Match Legitimate Name or Location


---

# S0286: OBAD

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0286  

## Description
OBAD is an Android malware family. (Citation: TrendMicro-Obad)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1629.001: Prevent Application Removal


---

# S1208: FjordPhantom

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1208  
**Aliases:** FjordPhantom  
**Platforms:** Android  

## Description
[FjordPhantom](https://attack.mitre.org/software/S1208) is a malicious Android application first discovered in September 2024 with targets in Southeast Asia, specifically Indonesia, Thailand, and Vietnam. [FjordPhantom](https://attack.mitre.org/software/S1208) was distributed through email and messaging applications. Once installed, the application launches a virtualization solution to steal important information, such as bank accounts, and to manipulate the user interface. The malicious activity from the virtualization solution runs alongside legitimate banking applications.(Citation: Promon FjordPhantom Oct2024)

## Techniques Used
- T1617: Hooking
- T1631: Process Injection
- T1655: Masquerading
- T1660: Phishing
- T1670: Virtualization Solution


---

# S0304: Android/Chuli.A

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0304  
**Aliases:** Android/Chuli.A  
**Platforms:** Android  

## Description
[Android/Chuli.A](https://attack.mitre.org/software/S0304) is Android malware that was delivered to activist groups via a spearphishing email with an attachment. (Citation: Kaspersky-WUC)

## Techniques Used
- T1426: System Information Discovery
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1644: Out of Band Data


---

# S0323: Charger

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0323  
**Aliases:** Charger  
**Platforms:** Android  

## Description
[Charger](https://attack.mitre.org/software/S0323) is Android malware that steals steals contacts and SMS messages from the user's device. It can also lock the device and demand ransom payment if it receives admin permissions. (Citation: CheckPoint-Charger)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1430: Location Tracking
- T1636.003: Contact List
- T1642: Endpoint Denial of Service


---

# S1054: Drinik

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1054  
**Aliases:** Drinik  
**Platforms:** Android  

## Description
[Drinik](https://attack.mitre.org/software/S1054) is an evolving Android banking trojan that was observed targeting customers of around 27 banks in India in August 2021. Initially seen as an SMS stealer in 2016, [Drinik](https://attack.mitre.org/software/S1054) resurfaced as a banking trojan with more advanced capabilities included in subsequent versions between September 2021 and August 2022.(Citation: cyble_drinik_1022)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1417.001: Keylogging
- T1417.002: GUI Input Capture
- T1437: Application Layer Protocol
- T1513: Screen Capture
- T1533: Data from Local System
- T1541: Foreground Persistence
- T1582: SMS Control
- T1616: Call Control
- T1628.001: Suppress Application Icon
- T1629.003: Disable or Modify Tools
- T1636.002: Call Log
- T1636.004: SMS Messages
- T1646: Exfiltration Over C2 Channel


---

# S0308: Trojan-SMS.AndroidOS.OpFake.a

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0308  

## Description
[Trojan-SMS.AndroidOS.OpFake.a](https://attack.mitre.org/software/S0308) is Android malware. (Citation: Kaspersky-MobileMalware)

## Techniques Used
- T1437.001: Web Protocols


---

# S0297: XcodeGhost

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0297  

## Description
[XcodeGhost](https://attack.mitre.org/software/S0297) is iOS malware that infected at least 39 iOS apps in 2015 and potentially affected millions of users. (Citation: PaloAlto-XcodeGhost1) (Citation: PaloAlto-XcodeGhost)

## Techniques Used
- T1414: Clipboard Data
- T1417.002: GUI Input Capture
- T1474.001: Compromise Software Dependencies and Development Tools


---

# S0549: SilkBean

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0549  
**Aliases:** SilkBean  
**Platforms:** Android  

## Description
[SilkBean](https://attack.mitre.org/software/S0549) is a piece of Android surveillanceware containing comprehensive remote access tool (RAT) functionality that has been used in targeting of the Uyghur ethnic group.(Citation: Lookout Uyghur Campaign)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1407: Download New Code at Runtime
- T1420: File and Directory Discovery
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1512: Video Capture
- T1521.002: Asymmetric Cryptography
- T1533: Data from Local System
- T1582: SMS Control
- T1630.002: File Deletion
- T1632.001: Code Signing Policy Modification
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location


---

# S0489: WolfRAT

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0489  
**Aliases:** WolfRAT  
**Platforms:** Android  

## Description
[WolfRAT](https://attack.mitre.org/software/S0489) is malware based on a leaked version of [Dendroid](https://attack.mitre.org/software/S0301) that has primarily targeted Thai users. [WolfRAT](https://attack.mitre.org/software/S0489) has most likely been operated by the now defunct organization Wolf Research.(Citation: Talos-WolfRAT)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1407: Download New Code at Runtime
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1424: Process Discovery
- T1429: Audio Capture
- T1512: Video Capture
- T1513: Screen Capture
- T1517: Access Notifications
- T1533: Data from Local System
- T1582: SMS Control
- T1630.002: File Deletion
- T1633.001: System Checks
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location


---

# S0655: BusyGasper

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0655  
**Aliases:** BusyGasper  
**Platforms:** Android  

## Description
[BusyGasper](https://attack.mitre.org/software/S0655) is Android spyware that has been in use since May 2016. There have been less than 10 victims, all who appear to be located in Russia, that were all infected via physical access to the device.(Citation: SecureList BusyGasper)

## Techniques Used
- T1407: Download New Code at Runtime
- T1409: Stored Application Data
- T1417.001: Keylogging
- T1429: Audio Capture
- T1430: Location Tracking
- T1481.002: Bidirectional Communication
- T1512: Video Capture
- T1513: Screen Capture
- T1533: Data from Local System
- T1582: SMS Control
- T1616: Call Control
- T1623.001: Unix Shell
- T1628.001: Suppress Application Icon
- T1628.002: User Evasion
- T1636.004: SMS Messages
- T1639.001: Exfiltration Over Unencrypted Non-C2 Protocol
- T1644: Out of Band Data
- T1645: Compromise Client Software Binary


---

# S0293: BrainTest

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0293  

## Description
[BrainTest](https://attack.mitre.org/software/S0293) is a family of Android malware. (Citation: CheckPoint-BrainTest) (Citation: Lookout-BrainTest)

## Techniques Used
- T1404: Exploitation for Privilege Escalation
- T1406: Obfuscated Files or Information
- T1407: Download New Code at Runtime
- T1643: Generate Traffic from Victim
- T1645: Compromise Client Software Binary


---

# S0545: TERRACOTTA

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0545  
**Aliases:** TERRACOTTA  
**Platforms:** Android  

## Description
[TERRACOTTA](https://attack.mitre.org/software/S0545) is an ad fraud botnet that has been capable of generating over 2 billion fraudulent requests per week.(Citation: WhiteOps TERRACOTTA)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1407: Download New Code at Runtime
- T1417.002: GUI Input Capture
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1481.002: Bidirectional Communication
- T1516: Input Injection
- T1541: Foreground Persistence
- T1575: Native API
- T1582: SMS Control
- T1603: Scheduled Task/Job
- T1624.001: Broadcast Receivers
- T1633.001: System Checks
- T1643: Generate Traffic from Victim


---

# S1092: Escobar

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1092  
**Aliases:** Escobar  
**Platforms:** Android  

## Description
[Escobar](https://attack.mitre.org/software/S1092) is an Android banking trojan, first detected in March 2021, believed to be a new variant of AbereBot.(Citation: Bleeipng Computer Escobar)

## Techniques Used
- T1409: Stored Application Data
- T1417.001: Keylogging
- T1417.002: GUI Input Capture
- T1420: File and Directory Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1461: Lockscreen Bypass
- T1512: Video Capture
- T1517: Access Notifications
- T1533: Data from Local System
- T1582: SMS Control
- T1616: Call Control
- T1630.001: Uninstall Malicious Application
- T1636.002: Call Log
- T1636.004: SMS Messages
- T1663: Remote Access Software


---

# S9004: Crocodilus

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S9004  
**Aliases:** Crocodilus  
**Platforms:** Android  

## Description
[Crocodilus](https://attack.mitre.org/software/S9004) is an Android banking Trojan that was discovered in March 2025. [Crocodilus](https://attack.mitre.org/software/S9004) targeted users worldwide, including Turkey, Poland, Argentina, Brazil, Spain, the United States, Indonesia and India. [Crocodilus](https://attack.mitre.org/software/S9004) has been customized based on the target location. For example, [Crocodilus](https://attack.mitre.org/software/S9004) mimicked major Turkish and Spanish banks for users in Turkey and Spain, while users in Poland saw Facebook advertisements that promoted [Crocodilus](https://attack.mitre.org/software/S9004) to claim bonus points.(Citation: ThreatFabric_Crocodilus_March2025)(Citation: ThreatFabric_Crocodilus_June2025)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1406.002: Software Packing
- T1407: Download New Code at Runtime
- T1417.001: Keylogging
- T1417.002: GUI Input Capture
- T1418: Software Discovery
- T1437.001: Web Protocols
- T1453: Abuse Accessibility Features
- T1512: Video Capture
- T1513: Screen Capture
- T1516: Input Injection
- T1582: SMS Control
- T1616: Call Control
- T1626.001: Device Administrator Permissions
- T1628.002: User Evasion
- T1629.001: Prevent Application Removal
- T1630.001: Uninstall Malicious Application
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1646: Exfiltration Over C2 Channel
- T1655: Masquerading


---

# S1214: Android/SpyAgent

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1214  
**Aliases:** Android/SpyAgent  
**Platforms:** Android  

## Description
[Android/SpyAgent](https://attack.mitre.org/software/S1214) is a variant of spyware in the MoqHao phishing campaign primarily targeting Korean and Japanese users.(Citation: McAfee MoqHao 2019) Fake security applications were used to target Japanese users, while fake police applications were used to target Korean users. Both fake applications have common C2 commands and share the same crash report key on a cloud service.(Citation: McAfee MoqHao 2019)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1422: System Network Configuration Discovery
- T1481: Web Service
- T1481.001: Dead Drop Resolver
- T1616: Call Control
- T1629.003: Disable or Modify Tools
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location


---

# S0424: Triada

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0424  
**Aliases:** Triada  
**Platforms:** Android  

## Description
[Triada](https://attack.mitre.org/software/S0424) was first reported in 2016 as a second stage malware. Later versions in 2019 appeared with new techniques and as an initial downloader of other Trojan apps.(Citation: Kaspersky Triada March 2016)

## Techniques Used
- T1407: Download New Code at Runtime
- T1418: Software Discovery
- T1474.003: Compromise Software Supply Chain
- T1532: Archive Collected Data
- T1631.001: Ptrace System Calls
- T1636.004: SMS Messages
- T1643: Generate Traffic from Victim
- T1646: Exfiltration Over C2 Channel


---

# S0535: Golden Cup

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0535  
**Aliases:** Golden Cup  
**Platforms:** Android  

## Description
[Golden Cup](https://attack.mitre.org/software/S0535) is Android spyware that has been used to target World Cup fans.(Citation: Symantec GoldenCup)

## Techniques Used
- T1407: Download New Code at Runtime
- T1418: Software Discovery
- T1420: File and Directory Discovery
- T1422: System Network Configuration Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1437.001: Web Protocols
- T1512: Video Capture
- T1532: Archive Collected Data
- T1533: Data from Local System
- T1636.003: Contact List
- T1636.004: SMS Messages


---

# S1067: FluBot

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1067  
**Aliases:** FluBot  
**Platforms:** Android  

## Description
[FluBot](https://attack.mitre.org/software/S1067) is a multi-purpose mobile banking malware that was first observed in Spain in late 2020. It primarily spread through European countries using a variety of SMS phishing messages in multiple languages.(Citation: proofpoint_flubot_0421)(Citation: bitdefender_flubot_0524) An international law enforcement operation of 11 countries eventually disrupted the spread of [FluBot](https://attack.mitre.org/software/S1067).(Citation: Europol FluBot Jun2022)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1409: Stored Application Data
- T1417.002: GUI Input Capture
- T1437.001: Web Protocols
- T1453: Abuse Accessibility Features
- T1517: Access Notifications
- T1521.002: Asymmetric Cryptography
- T1582: SMS Control
- T1604: Proxy Through Victim
- T1628.002: User Evasion
- T1629.001: Prevent Application Removal
- T1629.003: Disable or Modify Tools
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1637.001: Domain Generation Algorithms
- T1646: Exfiltration Over C2 Channel
- T1660: Phishing


---

# S0506: ViperRAT

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0506  
**Aliases:** ViperRAT  
**Platforms:** Android  

## Description
[ViperRAT](https://attack.mitre.org/software/S0506) is sophisticated surveillanceware that has been in operation since at least 2015 and was used to target the Israeli Defense Force.(Citation: Lookout ViperRAT)

## Techniques Used
- T1407: Download New Code at Runtime
- T1421: System Network Connections Discovery
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1512: Video Capture
- T1533: Data from Local System
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location


---

# S0309: Adups

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0309  

## Description
[Adups](https://attack.mitre.org/software/S0309) is software that was pre-installed onto Android devices, including those made by BLU Products. The software was reportedly designed to help a Chinese phone manufacturer monitor user behavior, transferring sensitive data to a Chinese server. (Citation: NYTimes-BackDoor) (Citation: BankInfoSecurity-BackDoor)

## Techniques Used
- T1430: Location Tracking
- T1474.003: Compromise Software Supply Chain
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages


---

# S0419: SimBad

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0419  
**Aliases:** SimBad  
**Platforms:** Android  

## Description
[SimBad](https://attack.mitre.org/software/S0419) was a strain of adware on the Google Play Store, distributed through the RXDroider Software Development Kit. The name "SimBad" was derived from the fact that most of the infected applications were simulator games. The adware was controlled using an instance of the open source framework Parse Server.(Citation: CheckPoint SimBad 2019)

## Techniques Used
- T1624.001: Broadcast Receivers
- T1628.001: Suppress Application Icon
- T1643: Generate Traffic from Victim
- T1655.001: Match Legitimate Name or Location


---

# S0525: Android/AdDisplay.Ashas

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0525  
**Aliases:** Android/AdDisplay.Ashas  
**Platforms:** Android  

## Description
[Android/AdDisplay.Ashas](https://attack.mitre.org/software/S0525) is a variant of adware that has been distributed through multiple apps in the Google Play Store. (Citation: WeLiveSecurity AdDisplayAshas)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1418: Software Discovery
- T1426: System Information Discovery
- T1437.001: Web Protocols
- T1624.001: Broadcast Receivers
- T1628.001: Suppress Application Icon
- T1633.001: System Checks
- T1643: Generate Traffic from Victim
- T1655.001: Match Legitimate Name or Location


---

# S1126: Phenakite

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1126  
**Aliases:** Phenakite  
**Platforms:** iOS  

## Description
[Phenakite](https://attack.mitre.org/software/S1126) is a mobile malware that is used by [APT-C-23](https://attack.mitre.org/groups/G1028) to target iOS devices. According to several reports, [Phenakite](https://attack.mitre.org/software/S1126) was developed to fill a tooling gap and to target those who owned iPhones instead of Windows desktops or Android phones.(Citation: sentinelone_israel_hamas_war)(Citation: fb_arid_viper)

## Techniques Used
- T1404: Exploitation for Privilege Escalation
- T1417: Input Capture
- T1426: System Information Discovery
- T1429: Audio Capture
- T1512: Video Capture
- T1533: Data from Local System
- T1544: Ingress Tool Transfer
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1655.001: Match Legitimate Name or Location


---

# S1056: TianySpy

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1056  
**Aliases:** TianySpy  
**Platforms:** Android, iOS  

## Description
[TianySpy](https://attack.mitre.org/software/S1056) is a mobile malware primarily spread by SMS phishing between September 30 and October 12, 2021. [TianySpy](https://attack.mitre.org/software/S1056) is believed to have targeted credentials associated with membership websites of major Japanese telecommunication services.(Citation: trendmicro_tianyspy_0122)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1417.002: GUI Input Capture
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1422.002: Wi-Fi Discovery
- T1426: System Information Discovery
- T1623: Command and Scripting Interpreter
- T1632.001: Code Signing Policy Modification
- T1639: Exfiltration Over Alternative Protocol


---

# S1082: Sunbird

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1082  
**Aliases:** Sunbird  
**Platforms:** Android  

## Description
[Sunbird](https://attack.mitre.org/software/S1082) is one of two mobile malware families known to be used by the APT [Confucius](https://attack.mitre.org/groups/G0142).  Analysis suggests that [Sunbird](https://attack.mitre.org/software/S1082) was first active in early 2017. While [Sunbird](https://attack.mitre.org/software/S1082) and [Hornbill](https://attack.mitre.org/software/S1077) overlap in core capabilities, [Sunbird](https://attack.mitre.org/software/S1082) has a more extensive set of malicious features.(Citation: lookout_hornbill_sunbird_0221)

## Techniques Used
- T1409: Stored Application Data
- T1418: Software Discovery
- T1422: System Network Configuration Discovery
- T1426: System Information Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1512: Video Capture
- T1513: Screen Capture
- T1532: Archive Collected Data
- T1533: Data from Local System
- T1544: Ingress Tool Transfer
- T1623.001: Unix Shell
- T1626.001: Device Administrator Permissions
- T1636.001: Calendar Entries
- T1636.002: Call Log
- T1636.003: Contact List
- T1646: Exfiltration Over C2 Channel


---

# S0300: DressCode

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0300  

## Description
[DressCode](https://attack.mitre.org/software/S0300) is an Android malware family. (Citation: TrendMicro-DressCode)

## Techniques Used
- T1428: Exploitation of Remote Services


---

# S0406: Gustuff

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S0406  
**Aliases:** Gustuff  
**Platforms:** Android  

## Description
[Gustuff](https://attack.mitre.org/software/S0406) is mobile malware designed to steal users' banking and virtual currency credentials.(Citation: Talos Gustuff Apr 2019)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1406.002: Software Packing
- T1417.001: Keylogging
- T1417.002: GUI Input Capture
- T1418.001: Security Software Discovery
- T1422: System Network Configuration Discovery
- T1426: System Information Discovery
- T1437.001: Web Protocols
- T1516: Input Injection
- T1533: Data from Local System
- T1628.001: Suppress Application Icon
- T1629.001: Prevent Application Removal
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1644: Out of Band Data


---

# S0408: FlexiSpy

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S0408  
**Aliases:** FlexiSpy  
**Platforms:** Android  

## Description
[FlexiSpy](https://attack.mitre.org/software/S0408) is sophisticated surveillanceware for iOS and Android. Publicly-available, comprehensive analysis has only been found for the Android version.(Citation: FortiGuard-FlexiSpy)(Citation: CyberMerchants-FlexiSpy)

[FlexiSpy](https://attack.mitre.org/software/S0408) markets itself as a parental control and employee monitoring application.(Citation: FlexiSpy-Website)

## Techniques Used
- T1406: Obfuscated Files or Information
- T1409: Stored Application Data
- T1417.001: Keylogging
- T1418: Software Discovery
- T1421: System Network Connections Discovery
- T1429: Audio Capture
- T1430: Location Tracking
- T1509: Non-Standard Port
- T1512: Video Capture
- T1513: Screen Capture
- T1533: Data from Local System
- T1624.001: Broadcast Receivers
- T1625.001: System Runtime API Hijacking
- T1628.001: Suppress Application Icon
- T1630.002: File Deletion
- T1636.001: Calendar Entries
- T1636.003: Contact List
- T1636.004: SMS Messages


---

# S0298: Xbot

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S0298  

## Description
[Xbot](https://attack.mitre.org/software/S0298) is an Android malware family that was observed in 2016 primarily targeting Android users in Russia and Australia. (Citation: PaloAlto-Xbot)

## Techniques Used
- T1417.002: GUI Input Capture
- T1471: Data Encrypted for Impact
- T1636.004: SMS Messages
- T1642: Endpoint Denial of Service


---

# T1603: Scheduled Task/Job


**ATT&CK ID:** T1603  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Execution, Persistence  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1603  

## Description
Adversaries may abuse task scheduling functionality to facilitate initial or recurring execution of malicious code. On Android and iOS, APIs and libraries exist to facilitate scheduling tasks to execute at a specified date, time, or interval.

On Android, the `WorkManager` API allows asynchronous tasks to be scheduled with the system. `WorkManager` was introduced to unify task scheduling on Android, using `JobScheduler`, `GcmNetworkManager`, and `AlarmManager` internally. `WorkManager` offers a lot of flexibility for scheduling, including periodically, one time, or constraint-based (e.g. only when the device is charging).(Citation: Android WorkManager)

On iOS, the `NSBackgroundActivityScheduler` API allows asynchronous tasks to be scheduled with the system. The tasks can be scheduled to be repeating or non-repeating, however, the system chooses when the tasks will be executed. The app can choose the interval for repeating tasks, or the delay between scheduling and execution for one-time tasks.(Citation: Apple NSBackgroundActivityScheduler)

## Known Software Using This Technique
- S1083: Chameleon
- S0536: GPlayed
- S1231: GodFather
- S0545: TERRACOTTA
- S0558: Tiktok Pro


---

# T1638: Adversary-in-the-Middle


**ATT&CK ID:** T1638  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1638  

## Description
Adversaries may attempt to position themselves between two or more networked devices to support follow-on behaviors such as [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1565/002) or [Endpoint Denial of Service](https://attack.mitre.org/techniques/T1642).  

 

[Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1638) can be achieved through several mechanisms. For example, a malicious application may register itself as a VPN client, effectively redirecting device traffic to adversary-owned resources. Registering as a VPN client requires user consent on both Android and iOS; additionally, a special entitlement granted by Apple is needed for iOS devices. Alternatively, a malicious application with escalation privileges may utilize those privileges to gain access to network traffic.   


 Specific to Android devices, adversary-in-the-disk is a type of AiTM attack where adversaries monitor and manipulate data that is exchanged between applications and external storage.(Citation: mitd_kaspersky)(Citation: mitd_checkpoint)(Citation: mitd_checkpoint_research) To accomplish this, a malicious application firsts requests for access to multimedia files on the device (`READ_EXTERNAL STORAGE` and `WRITE_EXTERNAL_STORAGE`), then the application reads data on the device and/or writes malware to the device. Though the request for access is common, when used maliciously, adversaries may access files and other sensitive data due to abusing the permission. Multiple applications were shown to be vulnerable against this attack; however, scrutiny of permissions and input validations may mitigate this attack.    

Outside of a mobile device, adversaries may be able to capture traffic by employing a rogue base station or Wi-Fi access point. These devices will allow adversaries to capture network traffic after it has left the device, while it is flowing to its destination. On a local network, enterprise techniques could be used, such as [ARP Cache Poisoning](https://attack.mitre.org/techniques/T1557/002) or [DHCP Spoofing](https://attack.mitre.org/techniques/T1557/003).  

 

If applications properly encrypt their network traffic, sensitive data may not be accessible to adversaries, depending on the point of capture. For example, properly implementing Apple’s Application Transport Security (ATS) and Android’s Network Security Configuration (NSC) may prevent sensitive data leaks.(Citation: NSC_Android)

## Mitigations
- M1006: Use Recent OS Version
- M1009: Encrypt Network Traffic

## Known Software Using This Technique
- S0288: KeyRaider
- S0407: Monokle
- S1062: S.O.V.A.


---

# T1626: Abuse Elevation Control Mechanism


**ATT&CK ID:** T1626  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Privilege Escalation  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1626  

## Description
Adversaries may circumvent mechanisms designed to control elevated privileges to gain higher-level permissions. Most modern systems contain native elevation control mechanisms that are intended to limit privileges that a user can gain on a machine. Authorization has to be granted to specific users in order to perform tasks that are designated as higher risk. An adversary can use several methods to take advantage of built-in control mechanisms in order to escalate privileges on a system.

## Sub-techniques
- T1626.001: Device Administrator Permissions

## Mitigations
- M1013: Application Developer Guidance


---

# T1663: Remote Access Software


**ATT&CK ID:** T1663  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1663  

## Description
Adversaries may use legitimate remote access software, such as `VNC`, `TeamViewer`, `AirDroid`, `AirMirror`, etc., to establish an interactive command and control channel to target mobile devices.  

Remote access applications may be installed and used post-compromise as an alternate communication channel for redundant access or as a way to establish an interactive remote session with the target device. They may also be used as a component of malware to establish a reverse connection to an adversary-controlled system or service. Installation of remote access tools may also include persistence.

## Mitigations
- M1011: User Guidance
- M1012: Enterprise Policy

## Known Software Using This Technique
- S1094: BRATA
- S1092: Escobar


---

# T1630.001: Uninstall Malicious Application

**Parent technique:** T1630
**ATT&CK ID:** T1630.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1630/001  

## Description
Adversaries may include functionality in malware that uninstalls the malicious application from the device. This can be achieved by: 
 
* Abusing device owner permissions to perform silent uninstallation using device owner API calls. 
* Abusing root permissions to delete files from the filesystem. 
* Abusing the accessibility service. This requires sending an intent to the system to request uninstallation, and then abusing the accessibility service to click the proper places on the screen to confirm uninstallation.

## Mitigations
- M1001: Security Updates
- M1002: Attestation
- M1011: User Guidance

## Known Software Using This Technique
- S1094: BRATA
- S0480: Cerberus
- S9004: Crocodilus
- S1092: Escobar
- S1062: S.O.V.A.
- S1055: SharkBot
- S0427: TrickMo


---

# T1630: Indicator Removal on Host


**ATT&CK ID:** T1630  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** iOS, Android  
**Reference:** https://attack.mitre.org/techniques/T1630  

## Description
Adversaries may delete, alter, or hide generated artifacts on a device, including files, jailbreak status, or the malicious application itself. These actions may interfere with event collection, reporting, or other notifications used to detect intrusion activity. This may compromise the integrity of mobile security solutions by causing notable events or information to go unreported.

## Sub-techniques
- T1630.001: Uninstall Malicious Application
- T1630.002: File Deletion
- T1630.003: Disguise Root/Jailbreak Indicators

## Mitigations
- M1001: Security Updates
- M1002: Attestation
- M1011: User Guidance

## Known Software Using This Technique
- S1083: Chameleon
- S1231: GodFather


---

# T1474: Supply Chain Compromise


**ATT&CK ID:** T1474  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Initial Access  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1474  

## Description
Adversaries may manipulate products or product delivery mechanisms prior to receipt by a final consumer for the purpose of data or system compromise.

Supply chain compromise can take place at any stage of the supply chain including:

* Manipulation of development tools
* Manipulation of a development environment
* Manipulation of source code repositories (public or private)
* Manipulation of source code in open-source dependencies
* Manipulation of software update/distribution mechanisms
* Compromised/infected system images
* Replacement of legitimate software with modified versions
* Sales of modified/counterfeit products to legitimate distributors
* Shipment interdiction

While supply chain compromise can impact any component of hardware or software, attackers looking to gain execution have often focused on malicious additions to legitimate software in software distribution or update channels. Targeting may be specific to a desired victim set or malicious software may be distributed to a broad set of consumers but only move on to additional tactics on specific victims.  Popular open source projects that are used as dependencies in many applications may also be targeted as a means to add malicious code to users of the dependency, specifically with the widespread usage of third-party advertising libraries.(Citation: Grace-Advertisement)(Citation: NowSecure-RemoteCode)

## Sub-techniques
- T1474.001: Compromise Software Dependencies and Development Tools
- T1474.002: Compromise Hardware Supply Chain
- T1474.003: Compromise Software Supply Chain

## Mitigations
- M1001: Security Updates
- M1013: Application Developer Guidance


---

# T1430.002: Impersonate SS7 Nodes

**Parent technique:** T1430
**ATT&CK ID:** T1430.002  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection, Discovery  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1430/002  

## Description
Adversaries may exploit the lack of authentication in signaling system network nodes to track the location of mobile devices by impersonating a node.(Citation: Engel-SS7)(Citation: Engel-SS7-2008)(Citation: 3GPP-Security)(Citation: Positive-SS7)(Citation: CSRIC5-WG10-FinalReport) 

 

By providing the victim’s MSISDN (phone number) and impersonating network internal nodes to query subscriber information from other nodes, adversaries may use data collected from each hop to eventually determine the device’s geographical cell area or nearest cell tower.(Citation: Engel-SS7)

## Mitigations
- M1014: Interconnection Filtering

## Known Software Using This Technique
- S0602: Circles


---

# T1655.001: Match Legitimate Name or Location

**Parent technique:** T1655
**ATT&CK ID:** T1655.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1655/001  

## Description
Adversaries may match or approximate the name or location of legitimate files or resources when naming/placing them. This is done for the sake of evading defenses and observation. This may be done by giving artifacts the name and icon of a legitimate, trusted application (i.e., Settings), or using a package name that matches legitimate, trusted applications (i.e., `com.google.android.gm`). 

Adversaries may also use the same icon of the file or application they are trying to mimic.

## Mitigations
- M1011: User Guidance

## Known Threat Groups Using This Technique
- G1028: APT-C-23
- G0097: Bouncing Golf
- G1019: MoustachedBouncer

## Known Software Using This Technique
- S0440: Agent Smith
- S0292: AndroRAT
- S0525: Android/AdDisplay.Ashas
- S1214: Android/SpyAgent
- S0524: AndroidOS/MalLocker.B
- S0422: Anubis
- S0540: Asacub
- S1079: BOULDSPY
- S1094: BRATA
- S0555: CHEMISTGAMES
- S0529: CarbonSteal
- S0480: Cerberus
- S1083: Chameleon
- S1243: DCHSpy
- S0301: Dendroid
- S9005: DocSwap
- S0550: DoubleAgent
- S0320: DroidJack
- S0478: EventBot
- S0522: Exobot
- S0509: FakeSpy
- S1080: Fakecalls
- S0577: FrozenCell
- S0536: GPlayed
- S0423: Ginp
- S1231: GodFather
- S0551: GoldenEagle
- S0544: HenBox
- S1077: Hornbill
- S0485: Mandrake
- S1126: Phenakite
- S0539: Red Alert 2.0
- S0549: SilkBean
- S0419: SimBad
- S1195: SpyC23
- S0558: Tiktok Pro
- S0418: ViceLeaker
- S0506: ViperRAT
- S0489: WolfRAT
- S0314: X-Agent for Android
- S0318: XLoader for Android


---

# T1636: Protected User Data


**ATT&CK ID:** T1636  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1636  

## Description
Adversaries may utilize standard operating system APIs to collect data from permission-backed data stores on a device, such as the calendar or contact list. These permissions need to be declared ahead of time. On Android, they must be included in the application’s manifest. On iOS, they must be included in the application’s `Info.plist` file.  

 

In almost all cases, the user is required to grant access to the data store that the application is trying to access. In recent OS versions, vendors have introduced additional privacy controls for users, such as the ability to grant permission to an application only while the application is being actively used by the user. 

 

If the device has been jailbroken or rooted, an adversary may be able to access [Protected User Data](https://attack.mitre.org/techniques/T1636) without the user’s knowledge or approval.

## Sub-techniques
- T1636.001: Calendar Entries
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1636.005: Accounts

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance


---

# T1521.002: Asymmetric Cryptography

**Parent technique:** T1521
**ATT&CK ID:** T1521.002  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1521/002  

## Description
Adversaries may employ a known asymmetric encryption algorithm to conceal command and control traffic, rather than relying on any inherent protections provided by a communication protocol. Asymmetric cryptography, also known as public key cryptography, uses a keypair per party: one public that can be freely distributed, and one private that should not be distributed. Due to how asymmetric algorithms work, the sender encrypts data with the receiver’s public key and the receiver decrypts the data with their private key. This ensures that only the intended recipient can read the encrypted data. Common public key encryption algorithms include RSA, ElGamal, and ECDSA.

For efficiency, many protocols (including SSL/TLS) use symmetric cryptography once a connection is established, but use asymmetric cryptography to establish or transmit a key. As such, these protocols are classified as [Asymmetric Cryptography](https://attack.mitre.org/techniques/T1521/002).

## Known Software Using This Technique
- S0555: CHEMISTGAMES
- S0529: CarbonSteal
- S1067: FluBot
- S1055: SharkBot
- S0549: SilkBean
- S1216: TriangleDB
- S0507: eSurv


---

# T1418: Software Discovery


**ATT&CK ID:** T1418  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Discovery  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1418  

## Description
Adversaries may attempt to get a listing of applications that are installed on a device. Adversaries may use the information from [Software Discovery](https://attack.mitre.org/techniques/T1418) during automated discovery to shape follow-on behaviors, including whether or not to fully infect the target and/or attempts specific actions. 

 

Adversaries may attempt to enumerate applications for a variety of reasons, such as figuring out what security measures are present or to identify the presence of target applications.

## Sub-techniques
- T1418.001: Security Software Discovery

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance

## Known Software Using This Technique
- S1061: AbstractEmu
- S0440: Agent Smith
- S0525: Android/AdDisplay.Ashas
- S0422: Anubis
- S1079: BOULDSPY
- S1215: Binary Validator
- S0529: CarbonSteal
- S0480: Cerberus
- S1083: Chameleon
- S1225: CherryBlos
- S9004: Crocodilus
- S0479: DEFENSOR ID
- S0505: Desert Scorpion
- S9005: DocSwap
- S0550: DoubleAgent
- S0478: EventBot
- S0405: Exodus
- S0509: FakeSpy
- S0408: FlexiSpy
- S0536: GPlayed
- S0423: Ginp
- S1231: GodFather
- S0535: Golden Cup
- S0551: GoldenEagle
- S0421: GolfSpy
- S0544: HenBox
- S1077: Hornbill
- S0463: INSOMNIA
- S1185: LightSpy
- S0485: Mandrake
- S0407: Monokle
- S0399: Pallas
- S0316: Pegasus for Android
- S1241: RatMilad
- S0539: Red Alert 2.0
- S0403: Riltok
- S0411: Rotexy
- S1062: S.O.V.A.
- S0328: Stealth Mango
- S1082: Sunbird
- S0545: TERRACOTTA
- S1069: TangleBot
- S0558: Tiktok Pro
- S0424: Triada
- S1216: TriangleDB
- S0427: TrickMo
- S9006: VajraSpy
- S0418: ViceLeaker
- S0489: WolfRAT
- S0311: YiSpecter


---

# T1424: Process Discovery


**ATT&CK ID:** T1424  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Discovery  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1424  

## Description
Adversaries may attempt to get information about running processes on a device. Information obtained could be used to gain an understanding of common software/applications running on devices within a network. Adversaries may use the information from [Process Discovery](https://attack.mitre.org/techniques/T1424) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions. 

 

Recent Android security enhancements have made it more difficult to obtain a list of running processes. On Android 7 and later, there is no way for an application to obtain the process list without abusing elevated privileges. This is due to the Android kernel utilizing the `hidepid` mount feature. Prior to Android 7, applications could utilize the `ps` command or examine the `/proc` directory on the device.(Citation: Android-SELinuxChanges) 

 

In iOS, applications have previously been able to use the `sysctl` command to obtain a list of running processes. This functionality has been removed in later iOS versions.

## Mitigations
- M1002: Attestation
- M1006: Use Recent OS Version

## Known Software Using This Technique
- S0440: Agent Smith
- S0422: Anubis
- S1215: Binary Validator
- S1225: CherryBlos
- S0421: GolfSpy
- S0544: HenBox
- S1185: LightSpy
- S0411: Rotexy
- S1055: SharkBot
- S1216: TriangleDB
- S0489: WolfRAT
- S0311: YiSpecter


---

# T1636.002: Call Log

**Parent technique:** T1636
**ATT&CK ID:** T1636.002  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1636/002  

## Description
Adversaries may utilize standard operating system APIs to gather call log data. On Android, this can be accomplished using the Call Log Content Provider. iOS provides no standard API to access the call log. 

 

If the device has been jailbroken or rooted, an adversary may be able to access the [Call Log](https://attack.mitre.org/techniques/T1636/002) without the user’s knowledge or approval.

## Mitigations
- M1011: User Guidance

## Known Software Using This Technique
- S1061: AbstractEmu
- S0309: Adups
- S1095: AhRat
- S0292: AndroRAT
- S0304: Android/Chuli.A
- S1079: BOULDSPY
- S0425: Corona Updates
- S1243: DCHSpy
- S9005: DocSwap
- S0550: DoubleAgent
- S1054: Drinik
- S0320: DroidJack
- S1092: Escobar
- S0405: Exodus
- S1080: Fakecalls
- S0182: FinFisher
- S0551: GoldenEagle
- S0421: GolfSpy
- S0544: HenBox
- S1077: Hornbill
- S0463: INSOMNIA
- S1185: LightSpy
- S0407: Monokle
- S0399: Pallas
- S0316: Pegasus for Android
- S0289: Pegasus for iOS
- S1241: RatMilad
- S0539: Red Alert 2.0
- S0549: SilkBean
- S1195: SpyC23
- S0324: SpyDealer
- S0328: Stealth Mango
- S1082: Sunbird
- S0329: Tangelo
- S1069: TangleBot
- S0558: Tiktok Pro
- S9006: VajraSpy
- S0418: ViceLeaker
- S0506: ViperRAT
- S0489: WolfRAT


---

# T1418.001: Security Software Discovery

**Parent technique:** T1418
**ATT&CK ID:** T1418.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Discovery  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1418/001  

## Description
Adversaries may attempt to get a listing of security applications and configurations that are installed on a device. This may include things such as mobile security products. Adversaries may use the information from [Security Software Discovery](https://attack.mitre.org/techniques/T1418/001) during automated discovery to shape follow-on behaviors, including whether or not to fully infect the target and/or attempt specific actions.

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance

## Known Software Using This Technique
- S1094: BRATA
- S0522: Exobot
- S0406: Gustuff


---

# T1631.001: Ptrace System Calls

**Parent technique:** T1631
**ATT&CK ID:** T1631.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion, Privilege Escalation  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1631/001  

## Description
Adversaries may inject malicious code into processes via ptrace (process trace) system calls in order to evade process-based defenses as well as possibly elevate privileges. Ptrace system call injection is a method of executing arbitrary code in the address space of a separate live process.  

Ptrace system call injection involves attaching to and modifying a running process. The ptrace system call enables a debugging process to observe and control another process (and each individual thread), including changing memory and register values.(Citation: PTRACE man) Ptrace system call injection is commonly performed by writing arbitrary code into a running process (e.g., by using `malloc`) then invoking that memory with `PTRACE_SETREGS` to set the register containing the next instruction to execute. Ptrace system call injection can also be done with `PTRACE_POKETEXT`/`PTRACE_POKEDATA`, which copy data to a specific address in the target process's memory (e.g., the current address of the next instruction).(Citation: PTRACE man)(Citation: Medium Ptrace JUL 2018)  

Ptrace system call injection may not be possible when targeting processes with high-privileges, and on some systems those that are non-child processes.(Citation: BH Linux Inject)  

Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via ptrace system call injection may also evade detection from security products since the execution is masked under a legitimate process.

## Known Software Using This Technique
- S0463: INSOMNIA
- S0424: Triada
- S0494: Zen


---

# T1629: Impair Defenses


**ATT&CK ID:** T1629  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1629  

## Description
Adversaries may maliciously modify components of a victim environment in order to hinder or disable defensive mechanisms. This not only involves impairing preventative defenses, such as anti-virus, but also detection capabilities that defenders can use to audit activity and identify malicious behavior. This may span both native defenses as well as supplemental capabilities installed by users or mobile endpoint administrators.

## Sub-techniques
- T1629.001: Prevent Application Removal
- T1629.002: Device Lockout
- T1629.003: Disable or Modify Tools

## Mitigations
- M1001: Security Updates
- M1004: System Partition Integrity
- M1010: Deploy Compromised Device Detection Method
- M1011: User Guidance
- M1012: Enterprise Policy

## Known Software Using This Technique
- S1225: CherryBlos
- S1231: GodFather


---

# T1453: Abuse Accessibility Features


**ATT&CK ID:** T1453  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection, Credential Access  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1453  

## Description
Adversaries may abuse accessibility features in Android devices to steal sensitive data and to spread malware to other devices. Accessibility features in Android are designed to assist users with disabilities, performing a variety of tasks, such as using Action Blocks to control lightbulbs, and changing the device’s user interface, such as changing the font size and adjusting contract or colors.(Citation: Google_AndroidAcsOverview) 

One example of how adversaries abuse accessibility features is overlaying an HTML object mimicking a legitimate login screen. The user types their credentials in the overlay HTML object, which is then sent to the adversaries.(Citation: SahinSRLabs_FluBot_Dec2021)  

Another example is a malicious accessibility feature acting as a keylogger. The keylogger monitors changes on the EditText fields and sends it to the adversaries.(Citation: SahinSRLabs_FluBot_Dec2021) This method of attack is also described in [Keylogging](https://attack.mitre.org/techniques/T1417/001); whereas [Abuse Accessibility Features](https://attack.mitre.org/techniques/T1453) captures the overall abuse of accessibility features.

## Mitigations
- M1011: User Guidance

## Known Software Using This Technique
- S0422: Anubis
- S1083: Chameleon
- S1225: CherryBlos
- S9004: Crocodilus
- S9005: DocSwap
- S1067: FluBot
- S1231: GodFather
- S9006: VajraSpy


---

# T1428: Exploitation of Remote Services


**ATT&CK ID:** T1428  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Lateral Movement  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1428  

## Description
Adversaries may exploit remote services of enterprise servers, workstations, or other resources to gain unauthorized access to internal systems once inside of a network. Adversaries may exploit remote services by taking advantage of a mobile device’s access to an internal enterprise network through local connectivity or through a Virtual Private Network (VPN). Exploitation of a software vulnerability occurs when an adversary takes advantage of a programming error in a program, service, or within the operating system software or kernel itself to execute adversary-controlled code. A common goal for post-compromise exploitation of remote services is for lateral movement to enable access to a remote system. 

An adversary may need to determine if the remote system is in a vulnerable state, which may be done through [Network Service Scanning](https://attack.mitre.org/techniques/T1423) or other Discovery methods. These look for common, vulnerable software that may be deployed in the network, the lack of certain patches that may indicate vulnerabilities, or security software that may be used to detect or contain remote exploitation. Servers are likely a high value target for lateral movement exploitation, but endpoint systems may also be at risk if they provide an advantage or access to additional resources.

Depending on the permissions level of the vulnerable remote service, an adversary may achieve [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1404) as a result of lateral movement exploitation as well.

## Mitigations
- M1012: Enterprise Policy

## Known Software Using This Technique
- S0300: DressCode
- S0299: NotCompatible


---

# T1437.001: Web Protocols

**Parent technique:** T1437
**ATT&CK ID:** T1437.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1437/001  

## Description
Adversaries may communicate using application layer protocols associated with web protocols traffic to avoid detection/network filtering by blending in with existing traffic. Commands to remote mobile devices, and often the results of those commands, will be embedded within the protocol traffic between the mobile client and server. 

Web protocols such as HTTP and HTTPS are used for web traffic as well as well as notification services native to mobile messaging services such as Google Cloud Messaging (GCM) and newly, Firebase Cloud Messaging (FCM), (GCM/FCM: two-way communication) and Apple Push Notification Service (APNS; one-way server-to-device).  Such notification services leverage HTTP/S via the respective API and are commonly abused on Android and iOS respectively in order blend in with routine device traffic making it difficult for enterprises to inspect.

## Known Threat Groups Using This Technique
- G0070: Dark Caracal

## Known Software Using This Technique
- S1061: AbstractEmu
- S1095: AhRat
- S0525: Android/AdDisplay.Ashas
- S0304: Android/Chuli.A
- S0540: Asacub
- S1079: BOULDSPY
- S1094: BRATA
- S0432: Bread
- S0555: CHEMISTGAMES
- S0480: Cerberus
- S1083: Chameleon
- S1225: CherryBlos
- S0426: Concipit1248
- S0425: Corona Updates
- S9004: Crocodilus
- S0479: DEFENSOR ID
- S9005: DocSwap
- S0478: EventBot
- S0522: Exobot
- S0405: Exodus
- S0509: FakeSpy
- S1067: FluBot
- S1093: FlyTrap
- S0536: GPlayed
- S1231: GodFather
- S0535: Golden Cup
- S0551: GoldenEagle
- S0406: Gustuff
- S1077: Hornbill
- S0463: INSOMNIA
- S1185: LightSpy
- S1241: RatMilad
- S0539: Red Alert 2.0
- S0326: RedDrop
- S0403: Riltok
- S0411: Rotexy
- S0313: RuMMS
- S1062: S.O.V.A.
- S1055: SharkBot
- S0549: SilkBean
- S0327: Skygofree
- S1195: SpyC23
- S0427: TrickMo
- S0307: Trojan-SMS.AndroidOS.Agent.ao
- S0306: Trojan-SMS.AndroidOS.FakeInst.a
- S0308: Trojan-SMS.AndroidOS.OpFake.a
- S0418: ViceLeaker
- S0311: YiSpecter


---

# T1635: Steal Application Access Token


**ATT&CK ID:** T1635  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Credential Access  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1635  

## Description
Adversaries can steal user application access tokens as a means of acquiring credentials to access remote systems and resources. This can occur through social engineering or URI hijacking and typically requires user action to grant access, such as through a system “Open With” dialogue.  

Application access tokens are used to make authorized API requests on behalf of a user and are commonly used as a way to access resources in cloud-based applications and software-as-a-service (SaaS).(Citation: Auth0 - Why You Should Always Use Access Tokens to Secure APIs Sept 2019) OAuth is one commonly implemented framework used to issue tokens to users for access to systems. An application desiring access to cloud-based services or protected APIs can gain entry through OAuth 2.0 using a variety of authorization protocols. An example of a commonly-used sequence is Microsoft's Authorization Code Grant flow.(Citation: Microsoft Identity Platform Protocols May 2019)(Citation: Microsoft - OAuth Code Authorization flow - June 2019) An OAuth access token enables a third-party application to interact with resources containing user data in the ways requested without requiring user credentials.

## Sub-techniques
- T1635.001: URI Hijacking

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance
- M1013: Application Developer Guidance


---

# T1628.002: User Evasion

**Parent technique:** T1628
**ATT&CK ID:** T1628.002  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1628/002  

## Description
Adversaries may attempt to avoid detection by hiding malicious behavior from the user. By doing this, an adversary’s modifications would most likely remain installed on the device for longer, allowing the adversary to continue to operate on that device. 

While there are many ways this can be accomplished, one method is by using the device’s sensors. By utilizing the various motion sensors on a device, such as accelerometer or gyroscope, an application could detect that the device is being interacted with. That way, the application could continue to run while the device is not in use but cease operating while the user is using the device, hiding anything that would indicate malicious activity was ongoing. Accessing the sensors in this way does not require any permissions from the user, so it would be completely transparent.

## Mitigations
- M1010: Deploy Compromised Device Detection Method

## Known Software Using This Technique
- S1094: BRATA
- S0655: BusyGasper
- S9004: Crocodilus
- S1067: FluBot
- S1077: Hornbill
- S1195: SpyC23


---

# T1633: Virtualization/Sandbox Evasion


**ATT&CK ID:** T1633  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1633  

## Description
Adversaries may employ various means to detect and avoid virtualization and analysis environments. This may include changing behaviors after checking for the presence of artifacts indicative of a virtual machine environment (VME) or sandbox. If the adversary detects a VME, they may alter their malware’s behavior to disengage from the victim or conceal the core functions of the payload. They may also search for VME artifacts before dropping further payloads. Adversaries may use the information learned from [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1633) during automated discovery to shape follow-on behaviors. 

Adversaries may use several methods to accomplish [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1633) such as checking for system artifacts associated with analysis or virtualization. Adversaries may also check for legitimate user activity to help determine if it is in an analysis environment.

## Sub-techniques
- T1633.001: System Checks

## Known Software Using This Technique
- S1061: AbstractEmu
- S1195: SpyC23


---

# T1661: Application Versioning


**ATT&CK ID:** T1661  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Initial Access, Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1661  

## Description
An adversary may push an update to a previously benign application to add malicious code. This can be accomplished by pushing an initially benign, functional application to a trusted application store, such as the Google Play Store or the Apple App Store. This allows the adversary to establish a trusted userbase that may grant permissions to the application prior to the introduction of malicious code. Then, an application update could be pushed to introduce malicious code.(Citation: android_app_breaking_bad)

This technique could also be accomplished by compromising a developer’s account. This would allow an adversary to take advantage of an existing userbase without having to establish the userbase themselves.

## Mitigations
- M1006: Use Recent OS Version
- M1012: Enterprise Policy

## Known Software Using This Technique
- S1055: SharkBot


---

# T1623: Command and Scripting Interpreter


**ATT&CK ID:** T1623  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Execution  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1623  

## Description
Adversaries may abuse command and script interpreters to execute commands, scripts, or binaries. These interfaces and languages provide ways of interacting with computer systems and are a common feature across many different platforms. Most systems come with some built-in command-line interface and scripting capabilities, for example, Android is a UNIX-like OS and includes a basic [Unix Shell](https://attack.mitre.org/techniques/T1623/001) that can be accessed via the Android Debug Bridge (ADB) or Java’s `Runtime` package.

Adversaries may abuse these technologies in various ways as a means of executing arbitrary commands. Commands and scripts can be embedded in [Initial Access](https://attack.mitre.org/tactics/TA0027) payloads delivered to victims as lure documents or as secondary payloads downloaded from an existing C2. Adversaries may also execute commands through interactive terminals/shells.

## Sub-techniques
- T1623.001: Unix Shell

## Mitigations
- M1002: Attestation
- M1010: Deploy Compromised Device Detection Method

## Known Software Using This Technique
- S1185: LightSpy
- S1056: TianySpy


---

# T1629.003: Disable or Modify Tools

**Parent technique:** T1629
**ATT&CK ID:** T1629.003  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1629/003  

## Description
Adversaries may disable security tools to avoid potential detection of their tools and activities. This can take the form of disabling security software, modifying SELinux configuration, or other methods to interfere with security tools scanning or reporting information. This is typically done by abusing device administrator permissions or using system exploits to gain root access to the device to modify protected system files.

## Mitigations
- M1001: Security Updates
- M1004: System Partition Integrity
- M1010: Deploy Compromised Device Detection Method
- M1011: User Guidance

## Known Software Using This Technique
- S1061: AbstractEmu
- S1214: Android/SpyAgent
- S0422: Anubis
- S1094: BRATA
- S0480: Cerberus
- S1083: Chameleon
- S1054: Drinik
- S0420: Dvmap
- S1067: FluBot
- S0485: Mandrake
- S1195: SpyC23
- S0494: Zen


---

# T1544: Ingress Tool Transfer


**ATT&CK ID:** T1544  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1544  

## Description
Adversaries may transfer tools or other files from an external system onto a compromised device to facilitate follow-on actions. Files may be copied from an external adversary-controlled system through the command and control channel  or through alternate protocols with another tool such as FTP.

## Known Software Using This Technique
- S1061: AbstractEmu
- S1083: Chameleon
- S1225: CherryBlos
- S9005: DocSwap
- S1231: GodFather
- S1185: LightSpy
- S0485: Mandrake
- S0407: Monokle
- S1126: Phenakite
- S0326: RedDrop
- S1055: SharkBot
- S1195: SpyC23
- S1082: Sunbird
- S1216: TriangleDB
- S0418: ViceLeaker


---

# T1637: Dynamic Resolution


**ATT&CK ID:** T1637  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1637  

## Description
Adversaries may dynamically establish connections to command and control infrastructure to evade common detections and remediations. This may be achieved by using malware that shares a common algorithm with the infrastructure the adversary uses to receive the malware's communications. This algorithm can be used to dynamically adjust parameters such as the domain name, IP address, or port number the malware uses for command and control.

## Sub-techniques
- T1637.001: Domain Generation Algorithms


---

# T1423: Network Service Scanning


**ATT&CK ID:** T1423  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Discovery  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1423  

## Description
Adversaries may attempt to get a listing of services running on remote hosts, including those that may be vulnerable to remote software exploitation. Methods to acquire this information include port scans and vulnerability scans from the mobile device. This technique may take advantage of the mobile device's access to an internal enterprise network either through local connectivity or through a Virtual Private Network (VPN).

## Known Software Using This Technique
- S1185: LightSpy


---

# T1646: Exfiltration Over C2 Channel


**ATT&CK ID:** T1646  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Exfiltration  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1646  

## Description
Adversaries may steal data by exfiltrating it over an existing command and control channel. Stolen data is encoded into the normal communications channel using the same protocol as command and control communications.

## Known Software Using This Technique
- S1061: AbstractEmu
- S1095: AhRat
- S1079: BOULDSPY
- S1094: BRATA
- S1215: Binary Validator
- S1083: Chameleon
- S1225: CherryBlos
- S9004: Crocodilus
- S9005: DocSwap
- S1054: Drinik
- S1080: Fakecalls
- S1067: FluBot
- S1093: FlyTrap
- S1231: GodFather
- S0551: GoldenEagle
- S0421: GolfSpy
- S1077: Hornbill
- S1185: LightSpy
- S0399: Pallas
- S1241: RatMilad
- S0326: RedDrop
- S1055: SharkBot
- S1082: Sunbird
- S0424: Triada
- S9006: VajraSpy
- S0418: ViceLeaker
- S0490: XLoader for iOS
- S0507: eSurv


---

# T1636.005: Accounts

**Parent technique:** T1636
**ATT&CK ID:** T1636.005  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1636/005  

## Description
Adversaries may utilize standard operating system APIs to gather account data. On Android, this can be accomplished by using the AccountManager API. For example, adversaries may use the `getAccounts()` method to list all accounts.(Citation: Android_AccountManager_Feb2025) On iOS, this can be accomplished by using the Keychain services.  

If the device has been jailbroken or rooted, adversaries may be able to access [Accounts](https://attack.mitre.org/techniques/T1636/005) without the users’ knowledge or approval.

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance

## Known Software Using This Technique
- S1243: DCHSpy
- S9005: DocSwap
- S1241: RatMilad
- S9006: VajraSpy


---

# T1404: Exploitation for Privilege Escalation


**ATT&CK ID:** T1404  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Privilege Escalation  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1404  

## Description
Adversaries may exploit software vulnerabilities in order to elevate privileges. Exploitation of a software vulnerability occurs when an adversary takes advantage of a programming error in an application, service, within the operating system software, or kernel itself to execute adversary-controlled code. Security constructions, such as permission levels, will often hinder access to information and use of certain techniques. Adversaries will likely need to perform privilege escalation to include use of software exploitation to circumvent those restrictions. 

When initially gaining access to a device, an adversary may be operating within a lower privileged process which will prevent them from accessing certain resources on the system. Vulnerabilities may exist, usually in operating system components and applications running at higher permissions, that can be exploited to gain higher levels of access on the system. This could enable someone to move from unprivileged or user- level permission to root permissions depending on the component that is vulnerable.

## Mitigations
- M1001: Security Updates
- M1002: Attestation
- M1010: Deploy Compromised Device Detection Method

## Known Software Using This Technique
- S1061: AbstractEmu
- S0440: Agent Smith
- S0293: BrainTest
- S0550: DoubleAgent
- S0420: Dvmap
- S0405: Exodus
- S0182: FinFisher
- S0290: Gooligan
- S0322: HummingBad
- S0463: INSOMNIA
- S1185: LightSpy
- S0316: Pegasus for Android
- S0289: Pegasus for iOS
- S1126: Phenakite
- S0294: ShiftyBug
- S0327: Skygofree
- S0324: SpyDealer
- S0494: Zen


---

# T1616: Call Control


**ATT&CK ID:** T1616  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection, Impact, Command And Control  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1616  

## Description
Adversaries may make, forward, or block phone calls without user authorization. This could be used for adversary goals such as audio surveillance, blocking or forwarding calls from the device owner, or C2 communication.

Several permissions may be used to programmatically control phone calls, including:

* `ANSWER_PHONE_CALLS` - Allows the application to answer incoming phone calls(Citation: Android Permissions)
* `CALL_PHONE` - Allows the application to initiate a phone call without going through the Dialer interface(Citation: Android Permissions)
* `PROCESS_OUTGOING_CALLS` - Allows the application to see the number being dialed during an outgoing call with the option to redirect the call to a different number or abort the call altogether(Citation: Android Permissions)
* `MANAGE_OWN_CALLS` - Allows a calling application which manages its own calls through the self-managed `ConnectionService` APIs(Citation: Android Permissions)
* `BIND_TELECOM_CONNECTION_SERVICE` - Required permission when using a `ConnectionService`(Citation: Android Permissions)
* `WRITE_CALL_LOG` - Allows an application to write to the device call log, potentially to hide malicious phone calls(Citation: Android Permissions)

When granted some of these permissions, an application can make a phone call without opening the dialer first. However, if an application desires to simply redirect the user to the dialer with a phone number filled in, it can launch an Intent using `Intent.ACTION_DIAL`, which requires no specific permissions. This then requires the user to explicitly initiate the call or use some form of [Input Injection](https://attack.mitre.org/techniques/T1516) to programmatically initiate it.

## Mitigations
- M1011: User Guidance

## Known Software Using This Technique
- S0292: AndroRAT
- S1214: Android/SpyAgent
- S0422: Anubis
- S1094: BRATA
- S0655: BusyGasper
- S0529: CarbonSteal
- S1083: Chameleon
- S9004: Crocodilus
- S9005: DocSwap
- S1054: Drinik
- S1092: Escobar
- S1080: Fakecalls
- S1231: GodFather
- S0407: Monokle
- S1195: SpyC23
- S1069: TangleBot
- S9006: VajraSpy


---

# T1639.001: Exfiltration Over Unencrypted Non-C2 Protocol

**Parent technique:** T1639
**ATT&CK ID:** T1639.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Exfiltration  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1639/001  

## Description
Adversaries may steal data by exfiltrating it over an un-encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server.

Adversaries may opt to obfuscate this data, without the use of encryption, within network protocols that are natively unencrypted (such as HTTP, FTP, or DNS). Adversaries may employ custom or publicly available encoding/compression algorithms (such as base64) or embed data within protocol headers and fields.

## Known Software Using This Technique
- S0655: BusyGasper
- S0425: Corona Updates
- S9006: VajraSpy


---

# T1624.001: Broadcast Receivers

**Parent technique:** T1624
**ATT&CK ID:** T1624.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Persistence  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1624/001  

## Description
Adversaries may establish persistence using system mechanisms that trigger execution based on specific events. Mobile operating systems have means to subscribe to events such as receiving an SMS message, device boot completion, or other device activities. 

An intent is a message passed between Android applications or system components. Applications can register to receive broadcast intents at runtime, which are system-wide intents delivered to each app when certain events happen on the device, such as network changes or the user unlocking the screen. Malicious applications can then trigger certain actions within the app based on which broadcast intent was received. 

In addition to Android system intents, malicious applications can register for intents broadcasted by other applications. This allows the malware to respond based on actions in other applications. This behavior typically indicates a more intimate knowledge, or potentially the targeting of specific devices, users, or applications. 

In Android 8 (API level 26), broadcast intent behavior was changed, limiting the implicit intents that applications can register for in the manifest. In most cases, applications that register through the manifest will no longer receive the broadcasts. Now, applications must register context-specific broadcast receivers while the user is actively using the app.(Citation: Android Changes to System Broadcasts)

## Mitigations
- M1006: Use Recent OS Version

## Known Software Using This Technique
- S1095: AhRat
- S0525: Android/AdDisplay.Ashas
- S0524: AndroidOS/MalLocker.B
- S0479: DEFENSOR ID
- S9005: DocSwap
- S0478: EventBot
- S0522: Exobot
- S0509: FakeSpy
- S0408: FlexiSpy
- S1103: FlixOnline
- S0536: GPlayed
- S0421: GolfSpy
- S0544: HenBox
- S0316: Pegasus for Android
- S0419: SimBad
- S1195: SpyC23
- S0324: SpyDealer
- S0305: SpyNote RAT
- S0545: TERRACOTTA
- S0558: Tiktok Pro
- S0427: TrickMo


---

# T1517: Access Notifications


**ATT&CK ID:** T1517  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection, Credential Access  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1517  

## Description
Adversaries may collect data within notifications sent by the operating system or other applications. Notifications may contain sensitive data such as one-time authentication codes sent over SMS, email, or other mediums. In the case of Credential Access, adversaries may attempt to intercept one-time code sent to the device. Adversaries can also dismiss notifications to prevent the user from noticing that the notification has arrived and can trigger action buttons contained within notifications.(Citation: ESET 2FA Bypass)

## Mitigations
- M1011: User Guidance
- M1012: Enterprise Policy
- M1013: Application Developer Guidance

## Known Software Using This Technique
- S1061: AbstractEmu
- S0432: Bread
- S1083: Chameleon
- S0425: Corona Updates
- S1092: Escobar
- S1103: FlixOnline
- S1067: FluBot
- S1077: Hornbill
- S0485: Mandrake
- S1062: S.O.V.A.
- S1055: SharkBot
- S1195: SpyC23
- S9006: VajraSpy
- S0489: WolfRAT


---

# T1639: Exfiltration Over Alternative Protocol


**ATT&CK ID:** T1639  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Exfiltration  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1639  

## Description
Adversaries may steal data by exfiltrating it over a different protocol than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server. 

Alternate protocols include FTP, SMTP, HTTP/S, DNS, SMB, or any other network protocol not being used as the main command and control channel. Different protocol channels could also include Web services such as cloud storage. Adversaries may opt to also encrypt and/or obfuscate these alternate channels.

## Sub-techniques
- T1639.001: Exfiltration Over Unencrypted Non-C2 Protocol

## Known Software Using This Technique
- S1056: TianySpy


---

# T1422.001: Internet Connection Discovery

**Parent technique:** T1422
**ATT&CK ID:** T1422.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Discovery  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1422/001  

## Description
Adversaries may check for Internet connectivity on compromised systems. This may be performed during automated discovery and can be accomplished in numerous ways such as using `adb shell netstat` for Android.(Citation: adb_commands)

Adversaries may use the results and responses from these requests to determine if the mobile devices are capable of communicating with adversary-owned C2 servers before attempting to connect to them. The results may also be used to identify routes, redirectors, and proxy servers.

## Mitigations
- M1009: Encrypt Network Traffic

## Known Software Using This Technique
- S1061: AbstractEmu
- S0540: Asacub
- S1079: BOULDSPY
- S0529: CarbonSteal
- S0425: Corona Updates
- S0478: EventBot
- S0522: Exobot
- S0405: Exodus
- S0509: FakeSpy
- S1093: FlyTrap
- S1077: Hornbill
- S0463: INSOMNIA
- S0407: Monokle
- S0316: Pegasus for Android
- S0326: RedDrop
- S0545: TERRACOTTA
- S1056: TianySpy
- S0427: TrickMo
- S0506: ViperRAT


---

# T1398: Boot or Logon Initialization Scripts


**ATT&CK ID:** T1398  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Persistence  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1398  

## Description
Adversaries may use scripts automatically executed at boot or logon initialization to establish persistence. Initialization scripts are part of the underlying operating system and are not accessible to the user unless the device has been rooted or jailbroken.

## Mitigations
- M1001: Security Updates
- M1002: Attestation
- M1003: Lock Bootloader
- M1004: System Partition Integrity

## Known Software Using This Technique
- S1095: AhRat
- S1079: BOULDSPY
- S1185: LightSpy
- S0285: OldBoot


---

# T1627: Execution Guardrails


**ATT&CK ID:** T1627  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1627  

## Description
Adversaries may use execution guardrails to constrain execution or actions based on adversary supplied and environment specific conditions that are expected to be present on the target. Guardrails ensure that a payload only executes against an intended target and reduces collateral damage from an adversary’s campaign. Values an adversary can provide about a target system or environment to use as guardrails may include environment information such as location.(Citation: SWB Exodus March 2019)

Guardrails can be used to prevent exposure of capabilities in environments that are not intended to be compromised or operated within. This use of guardrails is distinct from typical [System Checks](https://attack.mitre.org/techniques/T1633/001). While use of [System Checks](https://attack.mitre.org/techniques/T1633/001) may involve checking for known sandbox values and continuing with execution only if there is no match, the use of guardrails will involve checking for an expected target-specific value and only continuing with execution if there is such a match.

## Sub-techniques
- T1627.001: Geofencing

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance

## Known Software Using This Technique
- S1215: Binary Validator
- S9005: DocSwap


---

# T1417.002: GUI Input Capture

**Parent technique:** T1417
**ATT&CK ID:** T1417.002  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Credential Access, Collection  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1417/002  

## Description
Adversaries may mimic common operating system GUI components to prompt users for sensitive information with a seemingly legitimate prompt. The operating system and installed applications often have legitimate needs to prompt the user for sensitive information such as account credentials, bank account information, or Personally Identifiable Information (PII). Compared to traditional PCs, the constrained display size of mobile devices may impair the ability to provide users with contextual information, making users more susceptible to this technique’s use.(Citation: Felt-PhishingOnMobileDevices)

There are several approaches adversaries may use to mimic this functionality. Adversaries may impersonate the identity of a legitimate application (e.g. use the same application name and/or icon) and, when installed on the device, may prompt the user for sensitive information.(Citation: eset-finance) Adversaries may also send fake device notifications to the user that may trigger the display of an input prompt when clicked.(Citation: Group IB Gustuff Mar 2019) 

Additionally, adversaries may display a prompt on top of a running, legitimate application to trick users into entering sensitive information into a malicious application rather than the legitimate application. Typically, adversaries need to know when the targeted application and the individual activity within the targeted application is running in the foreground to display the prompt at the proper time. Adversaries can abuse Android’s accessibility features to determine which application is currently in the foreground.(Citation: ThreatFabric Cerberus) Two known approaches to displaying a prompt include:

* Adversaries start a new activity on top of a running legitimate application.(Citation: Felt-PhishingOnMobileDevices)(Citation: Hassell-ExploitingAndroid) Android 10 places new restrictions on the ability for an application to start a new activity on top of another application, which may make it more difficult for adversaries to utilize this technique.(Citation: Android Background)
* Adversaries create an application overlay window on top of a running legitimate application. Applications must hold the `SYSTEM_ALERT_WINDOW` permission to create overlay windows. This permission is handled differently than typical Android permissions and, at least under certain conditions, is automatically granted to applications installed from the Google Play Store.(Citation: Cloak and Dagger)(Citation: NowSecure Android Overlay)(Citation: Skycure-Accessibility) The `SYSTEM_ALERT_WINDOW` permission and its associated ability to create application overlay windows are expected to be deprecated in a future release of Android in favor of a new API.(Citation: XDA Bubbles)

## Mitigations
- M1006: Use Recent OS Version
- M1012: Enterprise Policy

## Known Software Using This Technique
- S0422: Anubis
- S1094: BRATA
- S0480: Cerberus
- S1083: Chameleon
- S9004: Crocodilus
- S0301: Dendroid
- S1054: Drinik
- S1092: Escobar
- S0478: EventBot
- S0522: Exobot
- S1103: FlixOnline
- S1067: FluBot
- S1093: FlyTrap
- S0536: GPlayed
- S0423: Ginp
- S0406: Gustuff
- S0485: Mandrake
- S0399: Pallas
- S0539: Red Alert 2.0
- S0403: Riltok
- S0411: Rotexy
- S1062: S.O.V.A.
- S1055: SharkBot
- S0545: TERRACOTTA
- S1069: TangleBot
- S1056: TianySpy
- S0558: Tiktok Pro
- S0298: Xbot
- S0297: XcodeGhost


---

# T1645: Compromise Client Software Binary


**ATT&CK ID:** T1645  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Persistence  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1645  

## Description
Adversaries may modify system software binaries to establish persistent access to devices. System software binaries are used by the underlying operating system and users over adb or terminal emulators. 

Adversaries may make modifications to client software binaries to carry out malicious tasks when those binaries are executed. For example, malware may come with a pre-compiled malicious binary intended to overwrite the genuine one on the device. Since these binaries may be routinely executed by the system or user, the adversary can leverage this for persistent access to the device.

## Mitigations
- M1001: Security Updates
- M1002: Attestation
- M1003: Lock Bootloader
- M1004: System Partition Integrity

## Known Software Using This Technique
- S0293: BrainTest
- S0655: BusyGasper
- S0550: DoubleAgent
- S0407: Monokle
- S0316: Pegasus for Android
- S0289: Pegasus for iOS
- S0294: ShiftyBug
- S0324: SpyDealer


---

# T1406.002: Software Packing

**Parent technique:** T1406
**ATT&CK ID:** T1406.002  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1406/002  

## Description
Adversaries may perform software packing to conceal their code. Software packing is a method of compressing or encrypting an executable. Packing an executable changes the file signature in an attempt to avoid signature-based detection. Most decompression techniques decompress the executable code in memory. 

Utilities used to perform software packing are called packers. An example packer is FTT. A more comprehensive list of known packers is available, but adversaries may create their own packing techniques that do not leave the same artifacts as well-known packers to evade defenses.

## Known Software Using This Technique
- S1094: BRATA
- S0432: Bread
- S1225: CherryBlos
- S9004: Crocodilus
- S0406: Gustuff
- S1062: S.O.V.A.


---

# T1575: Native API


**ATT&CK ID:** T1575  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion, Execution  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1575  

## Description
Adversaries may use Android’s Native Development Kit (NDK) to write native functions that can achieve execution of binaries or functions. Like system calls on a traditional desktop operating system, native code achieves execution on a lower level than normal Android SDK calls.

The NDK allows developers to write native code in C or C++ that is compiled directly to machine code, avoiding all intermediate languages and steps in compilation that higher level languages, like Java, typically have. The Java Native Interface (JNI) is the component that allows Java functions in the Android app to call functions in a native library.(Citation: Google NDK Getting Started)

Adversaries may also choose to use native functions to execute malicious code since native actions are typically much more difficult to analyze than standard, non-native behaviors.(Citation: MITRE App Vetting Effectiveness)

## Known Software Using This Technique
- S0540: Asacub
- S0432: Bread
- S0555: CHEMISTGAMES
- S0529: CarbonSteal
- S1083: Chameleon
- S9005: DocSwap
- S1231: GodFather
- S0544: HenBox
- S1185: LightSpy
- S0545: TERRACOTTA


---

# T1658: Exploitation for Client Execution


**ATT&CK ID:** T1658  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Execution  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1658  

## Description
Adversaries may exploit software vulnerabilities in client applications to execute code. Vulnerabilities can exist in software due to insecure coding practices that can lead to unanticipated behavior. Adversaries may take advantage of certain vulnerabilities through targeted exploitation for the purpose of arbitrary code execution. Oftentimes the most valuable exploits to an offensive toolkit are those that can be used to obtain code execution on a remote system because they can be used to gain access to that system. Users will expect to see files related to the applications they commonly used to do work, so they are a useful target for exploit research and development because of their high utility. 

Adversaries may use device-based zero-click exploits for code execution. These exploits are powerful because there is no user interaction required for code execution. 

### SMS/iMessage Delivery  

SMS and iMessage in iOS are common targets through [Drive-By Compromise](https://attack.mitre.org/techniques/T1456), [Phishing](https://attack.mitre.org/techniques/T1660), etc. Adversaries may use embed malicious links, files, etc. in SMS messages or iMessages. Mobile devices may be compromised through one-click exploits, where the victim must interact with a text message, or zero-click exploits, where no user interaction is required. 

### AirDrop 

Unique to iOS, AirDrop is a network protocol that allows iOS users to transfer files between iOS devices. Before patches from Apple were released, on iOS 13.4 and earlier, adversaries may force the Apple Wireless Direct Link (AWDL) interface to activate, then exploit a buffer overflow to gain access to the device and run as root without interaction from the user.

## Mitigations
- M1001: Security Updates
- M1011: User Guidance

## Known Software Using This Technique
- S1185: LightSpy
- S0289: Pegasus for iOS


---

# T1604: Proxy Through Victim


**ATT&CK ID:** T1604  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1604  

## Description
Adversaries may use a compromised device as a proxy server to the Internet. By utilizing a proxy, adversaries hide the true IP address of their C2 server and associated infrastructure from the destination of the network traffic. This masquerades an adversary’s traffic as legitimate traffic originating from the compromised device, which can evade IP-based restrictions and alerts on certain services, such as bank accounts and social media websites.(Citation: Threat Fabric Exobot)

The most common type of proxy is a SOCKS proxy. It can typically be implemented using standard OS-level APIs and 3rd party libraries with no indication to the user. On Android, adversaries can use the `Proxy` API to programmatically establish a SOCKS proxy connection, or lower-level APIs to interact directly with raw sockets.

## Known Software Using This Technique
- S0522: Exobot
- S1067: FluBot


---

# T1541: Foreground Persistence


**ATT&CK ID:** T1541  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion, Persistence  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1541  

## Description
Adversaries may abuse Android's `startForeground()` API method to maintain continuous sensor access. Beginning in Android 9, idle applications running in the background no longer have access to device sensors, such as the camera, microphone, and gyroscope.(Citation: Android-SensorsOverview) Applications can retain sensor access by running in the foreground, using Android’s `startForeground()` API method. This informs the system that the user is actively interacting with the application, and it should not be killed. The only requirement to start a foreground service is showing a persistent notification to the user.(Citation: Android-ForegroundServices)

Malicious applications may abuse the `startForeground()` API method to continue running in the foreground, while presenting a notification to the user pretending to be a genuine application. This would allow unhindered access to the device’s sensors, assuming permission has been previously granted.(Citation: BlackHat Sutter Android Foreground 2019)

Malicious applications may also abuse the `startForeground()` API to inform the Android system that the user is actively interacting with the application, thus preventing it from being killed by the low memory killer.(Citation: TrendMicro-Yellow Camera)

## Mitigations
- M1011: User Guidance

## Known Software Using This Technique
- S1225: CherryBlos
- S9005: DocSwap
- S1054: Drinik
- S0485: Mandrake
- S0545: TERRACOTTA
- S0558: Tiktok Pro


---

# T1458: Replication Through Removable Media


**ATT&CK ID:** T1458  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Initial Access, Lateral Movement  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1458  

## Description
Adversaries may move onto devices by exploiting or copying malware to devices connected via USB. In the case of Lateral Movement, adversaries may utilize the physical connection of a device to a compromised or malicious charging station or PC to bypass application store requirements and install malicious applications directly.(Citation: Lau-Mactans) In the case of Initial Access, adversaries may attempt to exploit the device via the connection to gain access to data stored on the device.(Citation: Krebs-JuiceJacking) Examples of this include: 
 
* Exploiting insecure bootloaders in a Nexus 6 or 6P device over USB and gaining the ability to perform actions including intercepting phone calls, intercepting network traffic, and obtaining the device physical location.(Citation: IBM-NexusUSB) 
* Exploiting weakly-enforced security boundaries in Android devices such as the Google Pixel 2 over USB.(Citation: GoogleProjectZero-OATmeal) 
* Products from Cellebrite and Grayshift purportedly that can exploit some iOS devices using physical access to the data port to unlock the passcode.(Citation: Computerworld-iPhoneCracking)

## Mitigations
- M1001: Security Updates
- M1003: Lock Bootloader
- M1006: Use Recent OS Version
- M1011: User Guidance
- M1012: Enterprise Policy

## Known Software Using This Technique
- S0315: DualToy
- S0312: WireLurker


---

# T1429: Audio Capture


**ATT&CK ID:** T1429  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1429  

## Description
Adversaries may capture audio to collect information by leveraging standard operating system APIs of a mobile device. Examples of audio information adversaries may target include user conversations, surroundings, phone calls, or other sensitive information. 

 

Android and iOS, by default, require that applications request device microphone access from the user.  

 

On Android devices, applications must hold the `RECORD_AUDIO` permission to access the microphone or the `CAPTURE_AUDIO_OUTPUT` permission to access audio output. Because Android does not allow third-party applications to hold the `CAPTURE_AUDIO_OUTPUT` permission by default, only privileged applications, such as those distributed by Google or the device vendor, can access audio output.(Citation: Android Permissions) However, adversaries may be able to gain this access after successfully elevating their privileges. With the `CAPTURE_AUDIO_OUTPUT` permission, adversaries may pass the `MediaRecorder.AudioSource.VOICE_CALL` constant to `MediaRecorder.setAudioOutput`, allowing capture of both voice call uplink and downlink.(Citation: Manifest.permission) 

 

On iOS devices, applications must include the `NSMicrophoneUsageDescription` key in their `Info.plist` file to access the microphone.(Citation: Requesting Auth-Media Capture)

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S1061: AbstractEmu
- S1095: AhRat
- S0292: AndroRAT
- S0422: Anubis
- S1079: BOULDSPY
- S0655: BusyGasper
- S0529: CarbonSteal
- S0425: Corona Updates
- S1243: DCHSpy
- S0301: Dendroid
- S0505: Desert Scorpion
- S9005: DocSwap
- S0550: DoubleAgent
- S0320: DroidJack
- S1092: Escobar
- S0405: Exodus
- S1080: Fakecalls
- S0182: FinFisher
- S0408: FlexiSpy
- S0577: FrozenCell
- S1231: GodFather
- S0535: Golden Cup
- S0551: GoldenEagle
- S0421: GolfSpy
- S0544: HenBox
- S1128: HilalRAT
- S1077: Hornbill
- S1185: LightSpy
- S0407: Monokle
- S0399: Pallas
- S0316: Pegasus for Android
- S0289: Pegasus for iOS
- S1126: Phenakite
- S0295: RCSAndroid
- S1241: RatMilad
- S0326: RedDrop
- S0327: Skygofree
- S1195: SpyC23
- S0324: SpyDealer
- S0305: SpyNote RAT
- S0328: Stealth Mango
- S1082: Sunbird
- S0329: Tangelo
- S1069: TangleBot
- S0558: Tiktok Pro
- S9006: VajraSpy
- S0418: ViceLeaker
- S0506: ViperRAT
- S0489: WolfRAT
- S0318: XLoader for Android
- S0507: eSurv


---

# T1625: Hijack Execution Flow


**ATT&CK ID:** T1625  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Persistence  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1625  

## Description
Adversaries may execute their own malicious payloads by hijacking the way operating systems run applications. Hijacking execution flow can be for the purposes of persistence since this hijacked execution may reoccur over time. 

There are many ways an adversary may hijack the flow of execution. A primary way is by manipulating how the operating system locates programs to be executed. How the operating system locates libraries to be used by a program can also be intercepted. Locations where the operating system looks for programs or resources, such as file directories, could also be poisoned to include malicious payloads.

## Sub-techniques
- T1625.001: System Runtime API Hijacking

## Mitigations
- M1002: Attestation
- M1004: System Partition Integrity

## Known Software Using This Technique
- S0311: YiSpecter


---

# T1623.001: Unix Shell

**Parent technique:** T1623
**ATT&CK ID:** T1623.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Execution  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1623/001  

## Description
Adversaries may abuse Unix shell commands and scripts for execution. Unix shells are the underlying command prompts on Android and iOS devices. Unix shells can control every aspect of a system, with certain commands requiring elevated privileges that are only accessible if the device has been rooted or jailbroken. 

Unix shells also support scripts that enable sequential execution of commands as well as other typical programming operations such as conditionals and loops. Common uses of shell scripts include long or repetitive tasks, or the need to run the same set of commands on multiple systems. 

Adversaries may abuse Unix shells to execute various commands or payloads. Interactive shells may be accessed through command and control channels or during lateral movement such as with SSH. Adversaries may also leverage shell scripts to deliver and execute multiple commands on victims or as part of payloads used for persistence. 

If the device has been rooted or jailbroken, adversaries may locate and invoke a superuser binary to elevate their privileges and interact with the system as the root user. This dangerous level of permissions allows the adversary to run special commands and modify protected system files.

## Mitigations
- M1002: Attestation
- M1010: Deploy Compromised Device Detection Method

## Known Software Using This Technique
- S1061: AbstractEmu
- S0655: BusyGasper
- S0555: CHEMISTGAMES
- S0550: DoubleAgent
- S0544: HenBox
- S1082: Sunbird
- S0558: Tiktok Pro


---

# T1437: Application Layer Protocol


**ATT&CK ID:** T1437  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1437  

## Description
Adversaries may communicate using application layer protocols to avoid detection/network filtering by blending in with existing traffic. Commands to the mobile device, and often the results of those commands, will be embedded within the protocol traffic between the mobile device and server. 

Adversaries may utilize many different protocols, including those used for web browsing, transferring files, electronic mail, or DNS.

## Sub-techniques
- T1437.001: Web Protocols

## Known Software Using This Technique
- S1083: Chameleon
- S1243: DCHSpy
- S0550: DoubleAgent
- S1054: Drinik


---

# T1407: Download New Code at Runtime


**ATT&CK ID:** T1407  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1407  

## Description
Adversaries may download and execute dynamic code not included in the original application package after installation. This technique is primarily used to evade static analysis checks and pre-publication scans in official app stores. In some cases, more advanced dynamic or behavioral analysis techniques could detect this behavior. However, in conjunction with [Execution Guardrails](https://attack.mitre.org/techniques/T1627) techniques, detecting malicious code downloaded after installation could be difficult.

On Android, dynamic code could include native code, Dalvik code, or JavaScript code that utilizes Android WebView’s `JavascriptInterface` capability. 

On iOS, dynamic code could be downloaded and executed through 3rd party libraries such as JSPatch. (Citation: FireEye-JSPatch)

## Mitigations
- M1006: Use Recent OS Version

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S1061: AbstractEmu
- S0422: Anubis
- S1079: BOULDSPY
- S1094: BRATA
- S0293: BrainTest
- S0432: Bread
- S0655: BusyGasper
- S0555: CHEMISTGAMES
- S0529: CarbonSteal
- S0480: Cerberus
- S1083: Chameleon
- S9004: Crocodilus
- S0505: Desert Scorpion
- S0550: DoubleAgent
- S0420: Dvmap
- S0478: EventBot
- S0405: Exodus
- S0577: FrozenCell
- S0536: GPlayed
- S0535: Golden Cup
- S0551: GoldenEagle
- S0544: HenBox
- S0325: Judy
- S0485: Mandrake
- S0295: RCSAndroid
- S1241: RatMilad
- S0539: Red Alert 2.0
- S1055: SharkBot
- S0549: SilkBean
- S0327: Skygofree
- S0324: SpyDealer
- S0545: TERRACOTTA
- S0424: Triada
- S0506: ViperRAT
- S0489: WolfRAT
- S0311: YiSpecter
- S0494: Zen
- S0287: ZergHelper
- S0507: eSurv


---

# T1664: Exploitation for Initial Access


**ATT&CK ID:** T1664  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Initial Access  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1664  

## Description
Adversaries may exploit software vulnerabilities to gain initial access to a mobile device. 

This can be accomplished in a variety of ways. Vulnerabilities may be present in the applications, the services, the underlying operating system, or the kernel itself. Several well-known mobile device exploits exist, including FORCEDENTRY, StageFright, and BlueBorne. Furthermore, some exploits may be possible to exploit without any user interaction (i.e. zero-click exploits, see [Exploitation for Client Execution](https://attack.mitre.org/techniques/T1658)), making them particularly dangerous. Mobile operating system vendors are typically very quick to patch such critical bugs, ensuring only a small window where they can be exploited.

## Mitigations
- M1001: Security Updates
- M1058: Antivirus/Antimalware

## Known Software Using This Technique
- S1094: BRATA
- S0289: Pegasus for iOS


---

# T1633.001: System Checks

**Parent technique:** T1633
**ATT&CK ID:** T1633.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1633/001  

## Description
Adversaries may employ various system checks to detect and avoid virtualization and analysis environments. This may include changing behavior after checking for the presence of artifacts indicative of a virtual environment or sandbox. If the adversary detects a virtual environment, they may alter their malware’s behavior to disengage from the victim or conceal the core functions of the implant. They may also search for virtualization artifacts before dropping secondary or additional payloads. 

Checks could include generic system properties such as host/domain name and samples of network traffic. Adversaries may also check the network adapters addresses, CPU core count, and available memory/drive size. 

Hardware checks, such as the presence of motion sensors, could also be used to gather evidence that can be indicative a virtual environment. Adversaries may also query for specific readings from these devices.

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S1061: AbstractEmu
- S0525: Android/AdDisplay.Ashas
- S0422: Anubis
- S1094: BRATA
- S0480: Cerberus
- S1083: Chameleon
- S0301: Dendroid
- S0509: FakeSpy
- S0423: Ginp
- S0544: HenBox
- S0485: Mandrake
- S0411: Rotexy
- S0545: TERRACOTTA
- S0427: TrickMo
- S0489: WolfRAT


---

# T1409: Stored Application Data


**ATT&CK ID:** T1409  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1409  

## Description
Adversaries may try to access and collect application data resident on the device. Adversaries often target popular applications, such as Facebook, WeChat, and Gmail.(Citation: SWB Exodus March 2019) 

 

Due to mobile OS sandboxing, this technique is only possible in three scenarios: 

 

* An application stores files in unprotected external storage 
* An application stores files in its internal storage directory with insecure permissions (e.g. 777) 
* The adversary gains root permissions on the device

## Mitigations
- M1006: Use Recent OS Version

## Known Threat Groups Using This Technique
- G0034: Sandworm Team

## Known Software Using This Technique
- S1079: BOULDSPY
- S0655: BusyGasper
- S0529: CarbonSteal
- S1243: DCHSpy
- S0505: Desert Scorpion
- S0550: DoubleAgent
- S1092: Escobar
- S0405: Exodus
- S0509: FakeSpy
- S0408: FlexiSpy
- S1103: FlixOnline
- S1067: FluBot
- S1093: FlyTrap
- S0577: FrozenCell
- S0551: GoldenEagle
- S1128: HilalRAT
- S1077: Hornbill
- S1185: LightSpy
- S0485: Mandrake
- S0399: Pallas
- S0316: Pegasus for Android
- S0289: Pegasus for iOS
- S0295: RCSAndroid
- S1062: S.O.V.A.
- S0327: Skygofree
- S0324: SpyDealer
- S1082: Sunbird
- S0329: Tangelo
- S9006: VajraSpy
- S0311: YiSpecter


---

# T1513: Screen Capture


**ATT&CK ID:** T1513  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1513  

## Description
Adversaries may use screen capture to collect additional information about a target device, such as applications running in the foreground, user data, credentials, or other sensitive information. Applications running in the background can capture screenshots or videos of another application running in the foreground by using the Android `MediaProjectionManager` (generally requires the device user to grant consent).(Citation: Fortinet screencap July 2019)(Citation: Android ScreenCap1 2019) Background applications can also use Android accessibility services to capture screen contents being displayed by a foreground application.(Citation: Lookout-Monokle) An adversary with root access or Android Debug Bridge (adb) access could call the Android `screencap` or `screenrecord` commands.(Citation: Android ScreenCap2 2019)(Citation: Trend Micro ScreenCap July 2015)

## Mitigations
- M1011: User Guidance
- M1012: Enterprise Policy
- M1013: Application Developer Guidance

## Known Software Using This Technique
- S1095: AhRat
- S0422: Anubis
- S1079: BOULDSPY
- S1094: BRATA
- S0655: BusyGasper
- S1083: Chameleon
- S9004: Crocodilus
- S0479: DEFENSOR ID
- S1054: Drinik
- S0478: EventBot
- S0405: Exodus
- S0408: FlexiSpy
- S0423: Ginp
- S0551: GoldenEagle
- S0421: GolfSpy
- S1077: Hornbill
- S1185: LightSpy
- S0485: Mandrake
- S0407: Monokle
- S1062: S.O.V.A.
- S1195: SpyC23
- S0324: SpyDealer
- S1082: Sunbird
- S1069: TangleBot
- S0558: Tiktok Pro
- S0427: TrickMo
- S0489: WolfRAT


---

# T1641.001: Transmitted Data Manipulation

**Parent technique:** T1641
**ATT&CK ID:** T1641.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Impact  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1641/001  

## Description
Adversaries may alter data en route to storage or other systems in order to manipulate external outcomes or hide activity. By manipulating transmitted data, adversaries may attempt to affect a business process, organizational understanding, or decision making.

Manipulation may be possible over a network connection or between system processes where there is an opportunity to deploy a tool that will intercept and change information. The type of modification and the impact it will have depends on the target transmission mechanism as well as the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system, typically gained through a prolonged information gathering campaign, in order to have the desired impact.

One method to achieve [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1641/001) is by modifying the contents of the device clipboard. Malicious applications may monitor clipboard activity through the `ClipboardManager.OnPrimaryClipChangedListener` interface on Android to determine when clipboard contents have changed. Listening to clipboard activity, reading clipboard contents, and modifying clipboard contents requires no explicit application permissions and can be performed by applications running in the background. However, this behavior has changed with the release of Android 10.

Adversaries may use [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1641/001) to replace text prior to being pasted. For example, replacing a copied Bitcoin wallet address with a wallet address that is under adversarial control.

[Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1641/001) was seen within the Android/Clipper.C trojan. This sample was detected by ESET in an application distributed through the Google Play Store targeting cryptocurrency wallet numbers.(Citation: ESET Clipboard Modification February 2019)

## Mitigations
- M1006: Use Recent OS Version

## Known Software Using This Technique
- S1094: BRATA
- S1062: S.O.V.A.


---

# T1474.001: Compromise Software Dependencies and Development Tools

**Parent technique:** T1474
**ATT&CK ID:** T1474.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Initial Access  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1474/001  

## Description
Adversaries may manipulate products or product delivery mechanisms prior to receipt by a final consumer for the purpose of data or system compromise. Applications often depend on external software to function properly. Popular open source projects that are used as dependencies in many applications may be targeted as a means to add malicious code to users of the dependency.(Citation: Grace-Advertisement)

## Mitigations
- M1013: Application Developer Guidance

## Known Software Using This Technique
- S0297: XcodeGhost


---

# T1635.001: URI Hijacking

**Parent technique:** T1635
**ATT&CK ID:** T1635.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Credential Access  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1635/001  

## Description
Adversaries may register Uniform Resource Identifiers (URIs) to intercept sensitive data. 

Applications regularly register URIs with the operating system to act as a response handler for various actions, such as logging into an app using an external account via single sign-on. This allows redirections to that specific URI to be intercepted by the application. If an adversary were to register for a URI that was already in use by a genuine application, the adversary may be able to intercept data intended for the genuine application or perform a phishing attack against the genuine application. Intercepted data may include OAuth authorization codes or tokens that could be used by the adversary to gain access to protected resources.(Citation: Trend Micro iOS URL Hijacking)(Citation: IETF-PKCE)

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance
- M1013: Application Developer Guidance


---

# T1632: Subvert Trust Controls


**ATT&CK ID:** T1632  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1632  

## Description
Adversaries may undermine security controls that will either warn users of untrusted activity or prevent execution of untrusted applications. Operating systems and security products may contain mechanisms to identify programs or websites as possessing some level of trust. Examples of such features include: an app being allowed to run because it is signed by a valid code signing certificate; an OS prompt alerting the user that an app came from an untrusted source; or getting an indication that you are about to connect to an untrusted site. The method adversaries use will depend on the specific mechanism they seek to subvert.

## Sub-techniques
- T1632.001: Code Signing Policy Modification

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance
- M1012: Enterprise Policy


---

# T1634.001: Keychain

**Parent technique:** T1634
**ATT&CK ID:** T1634.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Credential Access  
**Platforms:** iOS  
**Reference:** https://attack.mitre.org/techniques/T1634/001  

## Description
Adversaries may collect keychain data from an iOS device to acquire credentials. Keychains are the built-in way for iOS to keep track of users' passwords and credentials for many services and features such as Wi-Fi passwords, websites, secure notes, certificates, private keys, and VPN credentials. 

On the device, the keychain database is stored outside of application sandboxes to prevent unauthorized access to the raw data. Standard iOS APIs allow applications access to their own keychain contained within the database. By utilizing a privilege escalation exploit or existing root access, adversaries can access the entire encrypted database.(Citation: Apple Keychain Services)(Citation: Elcomsoft Decrypt Keychain)

## Mitigations
- M1001: Security Updates
- M1002: Attestation
- M1010: Deploy Compromised Device Detection Method

## Known Software Using This Technique
- S0463: INSOMNIA
- S1185: LightSpy
- S1216: TriangleDB


---

# T1670: Virtualization Solution


**ATT&CK ID:** T1670  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1670  

## Description
Adversaries may carry out malicious operations using virtualization solutions to escape from Android sandboxes and to avoid detection. Android uses sandboxes to separate resources and code execution between applications and the operating system.(Citation: Android Application Sandbox) There are a few virtualization solutions available on Android, such as the Android Virtualization Framework (AVF).(Citation: Android AVF Overview)  

 

Through virtualization solutions, adversaries may execute malicious operations without user knowledge. For example, adversaries may mimic a legitimate banking application’s functionalities in a virtual environment, thanks to the virtualization solution, while malicious code captures credentials.

## Mitigations
- M1011: User Guidance

## Known Software Using This Technique
- S1208: FjordPhantom
- S1231: GodFather


---

# T1481.002: Bidirectional Communication

**Parent technique:** T1481
**ATT&CK ID:** T1481.002  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1481/002  

## Description
Adversaries may use an existing, legitimate external Web service channel as a means for sending commands to and receiving output from a compromised system. Compromised systems may leverage popular websites and social media to host command and control (C2) instructions. Those infected systems can then send the output from those commands back over that Web service channel. The return traffic may occur in a variety of ways, depending on the Web service being utilized. For example, the return traffic may take the form of the compromised system posting a comment on a forum, issuing a pull request to development project, updating a document hosted on a Web service, or by sending a Tweet. 

 

Popular websites and social media, acting as a mechanism for C2, may give a significant amount of cover. This is due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection.

## Known Software Using This Technique
- S0655: BusyGasper
- S0485: Mandrake
- S0545: TERRACOTTA
- S9006: VajraSpy


---

# T1509: Non-Standard Port


**ATT&CK ID:** T1509  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1509  

## Description
Adversaries may generate network traffic using a protocol and port pairing that are typically not associated. For example, HTTPS over port 8088 or port 587 as opposed to the traditional port 443. Adversaries may make changes to the standard port used by a protocol to bypass filtering or muddle analysis/parsing of network data.

## Known Software Using This Technique
- S0480: Cerberus
- S1083: Chameleon
- S0405: Exodus
- S0408: FlexiSpy
- S0463: INSOMNIA
- S1185: LightSpy
- S0485: Mandrake
- S0539: Red Alert 2.0


---

# T1474.003: Compromise Software Supply Chain

**Parent technique:** T1474
**ATT&CK ID:** T1474.003  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Initial Access  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1474/003  

## Description
Adversaries may manipulate application software prior to receipt by a final consumer for the purpose of data or system compromise. Supply chain compromise of software can take place in a number of ways, including manipulation of the application source code, manipulation of the update/distribution mechanism for that software, or replacing compiled releases with a modified version.

## Mitigations
- M1001: Security Updates
- M1004: System Partition Integrity

## Known Software Using This Technique
- S0309: Adups
- S0319: Allwinner
- S0555: CHEMISTGAMES
- S0328: Stealth Mango
- S0424: Triada


---

# T1481.001: Dead Drop Resolver

**Parent technique:** T1481
**ATT&CK ID:** T1481.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1481/001  

## Description
Adversaries may use an existing, legitimate external Web service to host information that points to additional command and control (C2) infrastructure. Adversaries may post content, known as a dead drop resolver, on Web services with embedded (and often obfuscated/encoded) domains or IP addresses. Once infected, victims will reach out to and be redirected by these resolvers. 

 

Popular websites and social media, acting as a mechanism for C2, may give a significant amount of cover. This is due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection. 

 

Use of a dead drop resolver may also protect back-end C2 infrastructure from discovery through malware binary analysis, or enable operational resiliency (since this infrastructure may be dynamically changed).

## Known Software Using This Technique
- S0310: ANDROIDOS_ANSERVER.A
- S1214: Android/SpyAgent
- S0422: Anubis
- S0539: Red Alert 2.0
- S0318: XLoader for Android


---

# T1430: Location Tracking


**ATT&CK ID:** T1430  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection, Discovery  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1430  

## Description
Adversaries may track a device’s physical location through use of standard operating system APIs via malicious or exploited applications on the compromised device. 

 

On Android, applications holding the `ACCESS_COAURSE_LOCATION` or `ACCESS_FINE_LOCATION` permissions provide access to the device’s physical location. On Android 10 and up, declaration of the `ACCESS_BACKGROUND_LOCATION` permission in an application’s manifest will allow applications to request location access even when the application is running in the background.(Citation: Android Request Location Permissions) Some adversaries have utilized integration of Baidu map services to retrieve geographical location once the location access permissions had been obtained.(Citation: PaloAlto-SpyDealer)(Citation: Palo Alto HenBox) 

 

On iOS, applications must include the `NSLocationWhenInUseUsageDescription`, `NSLocationAlwaysAndWhenInUseUsageDescription`, and/or `NSLocationAlwaysUsageDescription` keys in their `Info.plist` file depending on the extent of requested access to location information.(Citation: Apple Requesting Authorization for Location Services) On iOS 8.0 and up, applications call `requestWhenInUseAuthorization()` to request access to location information when the application is in use or `requestAlwaysAuthorization()` to request access to location information regardless of whether the application is in use. With elevated privileges, an adversary may be able to access location data without explicit user consent with the `com.apple.locationd.preauthorized` entitlement key.(Citation: Google Project Zero Insomnia)

## Sub-techniques
- T1430.001: Remote Device Management Services
- T1430.002: Impersonate SS7 Nodes

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance
- M1012: Enterprise Policy
- M1014: Interconnection Filtering

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S1061: AbstractEmu
- S0309: Adups
- S1095: AhRat
- S0292: AndroRAT
- S0304: Android/Chuli.A
- S0422: Anubis
- S1079: BOULDSPY
- S1094: BRATA
- S0655: BusyGasper
- S0555: CHEMISTGAMES
- S0529: CarbonSteal
- S0480: Cerberus
- S1083: Chameleon
- S0323: Charger
- S0425: Corona Updates
- S1243: DCHSpy
- S0505: Desert Scorpion
- S9005: DocSwap
- S1092: Escobar
- S0405: Exodus
- S1080: Fakecalls
- S0182: FinFisher
- S0408: FlexiSpy
- S1093: FlyTrap
- S0577: FrozenCell
- S0536: GPlayed
- S0535: Golden Cup
- S0551: GoldenEagle
- S0421: GolfSpy
- S0544: HenBox
- S1128: HilalRAT
- S1077: Hornbill
- S0463: INSOMNIA
- S1185: LightSpy
- S0485: Mandrake
- S0407: Monokle
- S0291: PJApps
- S0399: Pallas
- S0289: Pegasus for iOS
- S0295: RCSAndroid
- S1241: RatMilad
- S0549: SilkBean
- S0327: Skygofree
- S1195: SpyC23
- S0324: SpyDealer
- S0305: SpyNote RAT
- S0328: Stealth Mango
- S1082: Sunbird
- S0329: Tangelo
- S1069: TangleBot
- S0558: Tiktok Pro
- S1216: TriangleDB
- S9006: VajraSpy
- S0418: ViceLeaker
- S0506: ViperRAT
- S0314: X-Agent for Android
- S0507: eSurv


---

# T1626.001: Device Administrator Permissions

**Parent technique:** T1626
**ATT&CK ID:** T1626.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Privilege Escalation  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1626/001  

## Description
Adversaries may abuse Android’s device administration API to obtain a higher degree of control over the device. By abusing the API, adversaries can perform several nefarious actions, such as resetting the device’s password for [Endpoint Denial of Service](https://attack.mitre.org/techniques/T1642), factory resetting the device for [File Deletion](https://attack.mitre.org/techniques/T1630/002) and to delete any traces of the malware, disabling all the device’s cameras, or to make it more difficult to uninstall the app.

Device administrators must be approved by the user at runtime, with a system popup showing which actions have been requested by the app. In conjunction with other techniques, such as [Input Injection](https://attack.mitre.org/techniques/T1516), an app can programmatically grant itself administrator permissions without any user input.

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance

## Known Software Using This Technique
- S1061: AbstractEmu
- S0540: Asacub
- S9004: Crocodilus
- S0522: Exobot
- S0536: GPlayed
- S1077: Hornbill
- S0539: Red Alert 2.0
- S1082: Sunbird
- S0318: XLoader for Android


---

# T1430.001: Remote Device Management Services

**Parent technique:** T1430
**ATT&CK ID:** T1430.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection, Discovery  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1430/001  

## Description
An adversary may use access to cloud services (e.g. Google's Android Device Manager or Apple iCloud's Find my iPhone) or to an enterprise mobility management (EMM)/mobile device management (MDM) server console to track the location of mobile devices managed by the service.(Citation: Krebs-Location)

## Mitigations
- M1011: User Guidance
- M1012: Enterprise Policy


---

# T1662: Data Destruction


**ATT&CK ID:** T1662  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Impact  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1662  

## Description
Adversaries may destroy data and files on specific devices or in large numbers to interrupt availability to systems, services, and network resources. Data destruction is likely to render stored data irrecoverable by forensic techniques through overwriting files or data on local and remote drives.  

To achieve data destruction, adversaries may use the `pm uninstall` command to uninstall packages or the `rm` command to remove specific files. For example, adversaries may first use `pm uninstall` to uninstall non-system apps, and then use `rm (-f) <file(s)>` to delete specific files, further hiding malicious activity.(Citation: rootnik_rooting_tool)(Citation: abuse_native_linux_tools)

## Mitigations
- M1011: User Guidance

## Known Software Using This Technique
- S1094: BRATA
- S1185: LightSpy
- S1241: RatMilad
- S9030: SameCoin


---

# T1676: Linked Devices


**ATT&CK ID:** T1676  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection, Persistence  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1676  

## Description
Adversaries may abuse the “linked devices” feature on messaging applications, such as Signal and WhatsApp, to register the user’s account to an adversary-controlled device. By abusing the “linked devices” feature, adversaries may achieve and maintain persistence through the user’s account, may collect information, such as the user’s messages and contacts list, and may send future messages from the linked device.

Signal is a messaging application that uses the open-source Signal Protocol to encrypt messages and calls; similarly, WhatsApp is a messaging application that has end-to-end encryption and other security measures to protect messages and calls. Both applications have a “linked devices” feature that allows users to access their Signal and/or WhatsApp accounts from different devices, such as a Windows or Mac desktop, an iPad or an Android tablet.(Citation: WhatsApp_LinkDevice_NoDate)(Citation: Signal_LinkedDevices_NoDate)

Adversaries may use [Phishing](https://attack.mitre.org/techniques/T1660) techniques to trick the user into scanning a quick-response (QR) code, which is used to link the user’s Signal and/or WhatsApp account to an adversary-controlled device. For example, adversaries may masquerade QR codes as group invites, security alerts or as legitimate instructions for pairing linked devices. 
Upon scanning the QR code in Signal, users may click on the “Transfer Message History” option to sync the linked devices, which may allow adversaries to collect more information about the user. Upon scanning the QR code in WhatsApp, the user’s device will automatically send an end-to-end encrypted copy of recent message history to the adversary-controlled device.

## Mitigations
- M1011: User Guidance

## Known Threat Groups Using This Technique
- G0034: Sandworm Team
- G1033: Star Blizzard


---

# T1451: SIM Card Swap


**ATT&CK ID:** T1451  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Initial Access  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1451  

## Description
Adversaries may gain access to mobile devices through transfers or swaps from victims’ phone numbers to adversary-controlled SIM cards and mobile devices.(Citation: ATT SIM Swap Scams)(Citation: Verizon SIM Swapping) 

The typical process is as follows:  

1. Adversaries will first gather information about victims through [Phishing](https://attack.mitre.org/techniques/T1660), social engineering, data breaches, or other avenues. 
2. Adversaries will then impersonate victims as they contact mobile carriers to request for the SIM swaps. For example, adversaries would provide victims’ name and address to mobile carriers; once authenticated, adversaries would request for victims’ phone numbers to be transferred to adversary-controlled SIM cards.  
3. Once completed, victims will lose mobile data, such as text messages and phone calls, on their mobile devices. In turn, adversaries will receive mobile data that was intended for the victims.  

Adversaries may use the intercepted SMS messages to log into online accounts that use SMS-based authentication. Specifically, adversaries may use SMS-based authentication to log into banking and/or cryptocurrency accounts, then transfer funds to adversary-controlled wallets.

## Mitigations
- M1011: User Guidance
- M1012: Enterprise Policy

## Known Threat Groups Using This Technique
- G1004: LAPSUS$
- G1015: Scattered Spider


---

# T1417: Input Capture


**ATT&CK ID:** T1417  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection, Credential Access  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1417  

## Description
Adversaries may use methods of capturing user input to obtain credentials or collect information. During normal device usage, users often provide credentials to various locations, such as login pages/portals or system dialog boxes. Input capture mechanisms may be transparent to the user (e.g. [Keylogging](https://attack.mitre.org/techniques/T1417/001)) or rely on deceiving the user into providing input into what they believe to be a genuine application prompt (e.g. [GUI Input Capture](https://attack.mitre.org/techniques/T1417/002)).

## Sub-techniques
- T1417.001: Keylogging
- T1417.002: GUI Input Capture

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance
- M1012: Enterprise Policy

## Known Software Using This Technique
- S1225: CherryBlos
- S1231: GodFather
- S1126: Phenakite


---

# T1643: Generate Traffic from Victim


**ATT&CK ID:** T1643  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Impact  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1643  

## Description
Adversaries may generate outbound traffic from devices. This is typically performed to manipulate external outcomes, such as to achieve carrier billing fraud or to manipulate app store rankings or ratings. Outbound traffic is typically generated as SMS messages or general web traffic, but may take other forms as well.

If done via SMS messages, Android apps must hold the `SEND_SMS` permission. Additionally, sending an SMS message requires user consent if the recipient is a premium number. Applications cannot send SMS messages on iOS

## Mitigations
- M1011: User Guidance

## Known Software Using This Technique
- S0440: Agent Smith
- S0525: Android/AdDisplay.Ashas
- S0293: BrainTest
- S0432: Bread
- S1103: FlixOnline
- S0290: Gooligan
- S0322: HummingBad
- S0321: HummingWhale
- S0325: Judy
- S0303: MazarBOT
- S0291: PJApps
- S0326: RedDrop
- S0419: SimBad
- S0545: TERRACOTTA
- S0424: Triada
- S0494: Zen


---

# T1630.003: Disguise Root/Jailbreak Indicators

**Parent technique:** T1630
**ATT&CK ID:** T1630.003  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1630/003  

## Description
An adversary could use knowledge of the techniques used by security software to evade detection.(Citation: Brodie)(Citation: Tan) For example, some mobile security products perform compromised device detection by searching for particular artifacts such as an installed "su" binary, but that check could be evaded by naming the binary something else. Similarly, polymorphic code techniques could be used to evade signature-based detection.(Citation: Rastogi)


---

# T1636.001: Calendar Entries

**Parent technique:** T1636
**ATT&CK ID:** T1636.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1636/001  

## Description
Adversaries may utilize standard operating system APIs to gather calendar entry data. On Android, this can be accomplished using the Calendar Content Provider. On iOS, this can be accomplished using the `EventKit` framework. 

 

If the device has been jailbroken or rooted, an adversary may be able to access [Calendar Entries](https://attack.mitre.org/techniques/T1636/001) without the user’s knowledge or approval.

## Mitigations
- M1011: User Guidance

## Known Software Using This Technique
- S0405: Exodus
- S0408: FlexiSpy
- S0407: Monokle
- S0316: Pegasus for Android
- S0328: Stealth Mango
- S1082: Sunbird


---

# T1630.002: File Deletion

**Parent technique:** T1630
**ATT&CK ID:** T1630.002  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1630/002  

## Description
Adversaries may wipe a device or delete individual files in order to manipulate external outcomes or hide activity. An application must have administrator access to fully wipe the device, while individual files may not require special permissions to delete depending on their storage location.(Citation: Android DevicePolicyManager 2019) 

Stored data could include a variety of file formats, such as Office files, databases, stored emails, and custom file formats. The impact file deletion will have depends on the type of data as well as the goals and objectives of the adversary, but can include deleting update files to evade detection or deleting attacker-specified files for impact.

## Mitigations
- M1011: User Guidance

## Known Software Using This Technique
- S0440: Agent Smith
- S1215: Binary Validator
- S0529: CarbonSteal
- S0505: Desert Scorpion
- S9005: DocSwap
- S0550: DoubleAgent
- S1080: Fakecalls
- S0408: FlexiSpy
- S0536: GPlayed
- S0421: GolfSpy
- S1077: Hornbill
- S0485: Mandrake
- S0407: Monokle
- S0399: Pallas
- S0549: SilkBean
- S0558: Tiktok Pro
- S1216: TriangleDB
- S0418: ViceLeaker
- S0489: WolfRAT


---

# T1629.002: Device Lockout

**Parent technique:** T1629
**ATT&CK ID:** T1629.002  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1629/002  

## Description
An adversary may seek to inhibit user interaction by locking the legitimate user out of the device. This is typically accomplished by requesting device administrator permissions and then locking the screen using `DevicePolicyManager.lockNow()`. Other novel techniques for locking the user out of the device have been observed, such as showing a persistent overlay, using carefully crafted “call” notification screens, and locking HTML pages in the foreground. These techniques can be very difficult to get around, and typically require booting the device into safe mode to uninstall the malware.(Citation: Microsoft MalLockerB)(Citation: Talos GPlayed)(Citation: securelist rotexy 2018)

Prior to Android 7, device administrators were able to reset the device lock passcode to prevent the user from unlocking the device. The release of Android 7 introduced updates that only allow device or profile owners (e.g. MDMs) to reset the device’s passcode.(Citation: Android resetPassword)

## Mitigations
- M1006: Use Recent OS Version

## Known Software Using This Technique
- S0524: AndroidOS/MalLocker.B
- S0411: Rotexy
- S0427: TrickMo


---

# T1417.001: Keylogging

**Parent technique:** T1417
**ATT&CK ID:** T1417.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection, Credential Access  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1417/001  

## Description
Adversaries may log user keystrokes to intercept credentials or other information from the user as the user types them.

Some methods of keylogging include:

* Masquerading as a legitimate third-party keyboard to record user keystrokes.(Citation: Zeltser-Keyboard) On both Android and iOS, users must explicitly authorize the use of third-party keyboard apps. Users should be advised to use extreme caution before granting this authorization when it is requested.
* Abusing accessibility features. On Android, adversaries may abuse accessibility features to record keystrokes by registering an `AccessibilityService` class, overriding the `onAccessibilityEvent` method, and listening for the `AccessibilityEvent.TYPE_VIEW_TEXT_CHANGED` event type. The event object passed into the function will contain the data that the user typed. 
*Additional methods of keylogging may be possible if root access is available.

## Mitigations
- M1011: User Guidance
- M1012: Enterprise Policy

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S0422: Anubis
- S1079: BOULDSPY
- S1094: BRATA
- S0655: BusyGasper
- S0480: Cerberus
- S1083: Chameleon
- S9004: Crocodilus
- S9005: DocSwap
- S1054: Drinik
- S1092: Escobar
- S0478: EventBot
- S0522: Exobot
- S0408: FlexiSpy
- S1231: GodFather
- S0406: Gustuff
- S0407: Monokle
- S1062: S.O.V.A.
- S1055: SharkBot
- S9006: VajraSpy


---

# T1582: SMS Control


**ATT&CK ID:** T1582  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Impact  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1582  

## Description
Adversaries may delete, alter, or send SMS messages without user authorization. This could be used to hide C2 SMS messages, spread malware, or various external effects.

This can be accomplished by requesting the `RECEIVE_SMS` or `SEND_SMS` permissions depending on what the malware is attempting to do. If the app is set as the default SMS handler on the device, the `SMS_DELIVER` broadcast intent can be registered, which allows the app to write to the SMS content provider. The content provider directly modifies the messaging database on the device, which could allow malicious applications with this ability to insert, modify, or delete arbitrary messages on the device.(Citation: SMS KitKat)(Citation: Android SmsProvider)

## Mitigations
- M1011: User Guidance

## Known Software Using This Technique
- S1095: AhRat
- S0292: AndroRAT
- S0422: Anubis
- S0540: Asacub
- S0655: BusyGasper
- S0480: Cerberus
- S0425: Corona Updates
- S9004: Crocodilus
- S0301: Dendroid
- S0505: Desert Scorpion
- S1054: Drinik
- S1092: Escobar
- S0522: Exobot
- S0509: FakeSpy
- S1067: FluBot
- S0536: GPlayed
- S0423: Ginp
- S1231: GodFather
- S0551: GoldenEagle
- S1185: LightSpy
- S0485: Mandrake
- S0539: Red Alert 2.0
- S0411: Rotexy
- S1062: S.O.V.A.
- S1055: SharkBot
- S0549: SilkBean
- S1195: SpyC23
- S0328: Stealth Mango
- S0545: TERRACOTTA
- S1069: TangleBot
- S0558: Tiktok Pro
- S0427: TrickMo
- S0489: WolfRAT


---

# T1631: Process Injection


**ATT&CK ID:** T1631  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion, Privilege Escalation  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1631  

## Description
Adversaries may inject code into processes in order to evade process-based defenses or even elevate privileges. Process injection is a method of executing arbitrary code in the address space of a separate live process. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via process injection may also evade detection from security products since the execution is masked under a legitimate process. 

Both Android and iOS have no legitimate way to achieve process injection. The only way this is possible is by abusing existing root access or exploiting a vulnerability.

## Sub-techniques
- T1631.001: Ptrace System Calls

## Known Software Using This Technique
- S1208: FjordPhantom
- S1185: LightSpy


---

# T1521.001: Symmetric Cryptography

**Parent technique:** T1521
**ATT&CK ID:** T1521.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1521/001  

## Description
Adversaries may employ a known symmetric encryption algorithm to conceal command and control traffic, rather than relying on any inherent protections provided by a communication protocol. Symmetric encryption algorithms use the same key for plaintext encryption and ciphertext decryption. Common symmetric encryption algorithms include AES, Blowfish, and RC4.

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S0478: EventBot
- S0411: Rotexy
- S1055: SharkBot
- S1216: TriangleDB


---

# T1422.002: Wi-Fi Discovery

**Parent technique:** T1422
**ATT&CK ID:** T1422.002  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Discovery  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1422/002  

## Description
Adversaries may search for information about Wi-Fi networks, such as network names and passwords, on compromised systems. Adversaries may use Wi-Fi information as part of [Discovery](https://attack.mitre.org/tactics/TA0032) or [Credential Access](https://attack.mitre.org/tactics/TA0031) activity to support both ongoing and future campaigns.

## Mitigations
- M1006: Use Recent OS Version

## Known Software Using This Technique
- S1079: BOULDSPY
- S0425: Corona Updates
- S9005: DocSwap
- S1077: Hornbill
- S0463: INSOMNIA
- S1185: LightSpy
- S0407: Monokle
- S0316: Pegasus for Android
- S0326: RedDrop
- S1056: TianySpy
- S0427: TrickMo
- S9006: VajraSpy


---

# T1474.002: Compromise Hardware Supply Chain

**Parent technique:** T1474
**ATT&CK ID:** T1474.002  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Initial Access  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1474/002  

## Description
Adversaries may manipulate hardware components in products prior to receipt by a final consumer for the purpose of data or system compromise. By modifying hardware or firmware in the supply chain, adversaries can insert a backdoor into consumer networks that may be difficult to detect and give the adversary a high degree of control over the system.

## Mitigations
- M1001: Security Updates


---

# T1414: Clipboard Data


**ATT&CK ID:** T1414  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection, Credential Access  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1414  

## Description
Adversaries may abuse clipboard manager APIs to obtain sensitive information copied to the device clipboard. For example, passwords being copied and pasted from a password manager application could be captured by a malicious application installed on the device.(Citation: Fahl-Clipboard) 

 

On Android, applications can use the `ClipboardManager.OnPrimaryClipChangedListener()` API to register as a listener and monitor the clipboard for changes. However, starting in Android 10, this can only be used if the application is in the foreground, or is set as the device’s default input method editor (IME).(Citation: Github Capture Clipboard 2019)(Citation: Android 10 Privacy Changes) 

 

On iOS, this can be accomplished by accessing the `UIPasteboard.general.string` field. However, starting in iOS 14, upon accessing the clipboard, the user will be shown a system notification if the accessed text originated in a different application. For example, if the user copies the text of an iMessage from the Messages application, the notification will read “application_name has pasted from Messages” when the text was pasted in a different application.(Citation: UIPPasteboard)

## Mitigations
- M1006: Use Recent OS Version

## Known Software Using This Technique
- S1079: BOULDSPY
- S0421: GolfSpy
- S0295: RCSAndroid
- S1241: RatMilad
- S0297: XcodeGhost


---

# T1641: Data Manipulation


**ATT&CK ID:** T1641  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Impact  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1641  

## Description
Adversaries may insert, delete, or alter data in order to manipulate external outcomes or hide activity. By manipulating data, adversaries may attempt to affect a business process, organizational understanding, or decision making.

The type of modification and the impact it will have depends on the target application, process, and the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system, typically gained through a prolonged information gathering campaign, in order to have the desired impact.

## Sub-techniques
- T1641.001: Transmitted Data Manipulation

## Mitigations
- M1006: Use Recent OS Version


---

# T1636.004: SMS Messages

**Parent technique:** T1636
**ATT&CK ID:** T1636.004  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1636/004  

## Description
Adversaries may utilize standard operating system APIs to gather SMS messages. On Android, this can be accomplished using the SMS Content Provider. iOS provides no standard API to access SMS messages. 

If the device has been jailbroken or rooted, an adversary may be able to access [SMS Messages](https://attack.mitre.org/techniques/T1636/004) without the user’s knowledge or approval.

## Mitigations
- M1011: User Guidance

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S1061: AbstractEmu
- S0309: Adups
- S0292: AndroRAT
- S0304: Android/Chuli.A
- S1214: Android/SpyAgent
- S0540: Asacub
- S1079: BOULDSPY
- S0432: Bread
- S0655: BusyGasper
- S0529: CarbonSteal
- S0480: Cerberus
- S1083: Chameleon
- S0425: Corona Updates
- S9004: Crocodilus
- S1243: DCHSpy
- S0301: Dendroid
- S0505: Desert Scorpion
- S9005: DocSwap
- S0550: DoubleAgent
- S1054: Drinik
- S0320: DroidJack
- S1092: Escobar
- S0478: EventBot
- S0522: Exobot
- S0405: Exodus
- S0509: FakeSpy
- S1080: Fakecalls
- S0182: FinFisher
- S0408: FlexiSpy
- S1067: FluBot
- S0577: FrozenCell
- S0536: GPlayed
- S0423: Ginp
- S1231: GodFather
- S0535: Golden Cup
- S0551: GoldenEagle
- S0421: GolfSpy
- S0406: Gustuff
- S0544: HenBox
- S1128: HilalRAT
- S0463: INSOMNIA
- S1185: LightSpy
- S0485: Mandrake
- S0303: MazarBOT
- S0399: Pallas
- S0289: Pegasus for iOS
- S1126: Phenakite
- S0295: RCSAndroid
- S1241: RatMilad
- S0539: Red Alert 2.0
- S0403: Riltok
- S0411: Rotexy
- S0313: RuMMS
- S1062: S.O.V.A.
- S1055: SharkBot
- S0549: SilkBean
- S1195: SpyC23
- S0324: SpyDealer
- S0305: SpyNote RAT
- S0328: Stealth Mango
- S0329: Tangelo
- S1069: TangleBot
- S0558: Tiktok Pro
- S0424: Triada
- S0427: TrickMo
- S9006: VajraSpy
- S0418: ViceLeaker
- S0506: ViperRAT
- S0489: WolfRAT
- S0318: XLoader for Android
- S0298: Xbot


---

# T1481: Web Service


**ATT&CK ID:** T1481  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1481  

## Description
Adversaries may use an existing, legitimate external Web service as a means for relaying data to/from a compromised system. Popular websites and social media, acting as a mechanism for C2, may give a significant amount of cover. This is due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection. 

 

Use of Web services may also protect back-end C2 infrastructure from discovery through malware binary analysis, or enable operational resiliency (since this infrastructure may be dynamically changed).

## Sub-techniques
- T1481.001: Dead Drop Resolver
- T1481.002: Bidirectional Communication
- T1481.003: One-Way Communication

## Known Software Using This Technique
- S1214: Android/SpyAgent


---

# T1625.001: System Runtime API Hijacking

**Parent technique:** T1625
**ATT&CK ID:** T1625.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Persistence  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1625/001  

## Description
Adversaries may execute their own malicious payloads by hijacking the way an operating system runs applications. Hijacking execution flow can be for the purposes of persistence since this hijacked execution may reoccur at later points in time. 


On Android, adversaries may overwrite the standard OS API library with a malicious alternative to hook into core functions to achieve persistence. By doing this, the adversary’s code will be executed every time the overwritten API function is called by an app on the infected device.

## Mitigations
- M1002: Attestation
- M1004: System Partition Integrity

## Known Software Using This Technique
- S0420: Dvmap
- S0408: FlexiSpy
- S0494: Zen


---

# T1634: Credentials from Password Store


**ATT&CK ID:** T1634  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Credential Access  
**Platforms:** iOS  
**Reference:** https://attack.mitre.org/techniques/T1634  

## Description
Adversaries may search common password storage locations to obtain user credentials. Passwords can be stored in several places on a device, depending on the operating system or application holding the credentials. There are also specific applications that store passwords to make it easier for users to manage and maintain. Once credentials are obtained, they can be used to perform lateral movement and access restricted information.

## Sub-techniques
- T1634.001: Keychain

## Mitigations
- M1001: Security Updates
- M1002: Attestation
- M1010: Deploy Compromised Device Detection Method


---

# T1617: Hooking


**ATT&CK ID:** T1617  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1617  

## Description
Adversaries may utilize hooking to hide the presence of artifacts associated with their behaviors to evade detection. Hooking can be used to modify return values or data structures of system APIs and function calls. This process typically involves using 3rd party root frameworks, such as Xposed or Magisk, with either a system exploit or pre-existing root access. By including custom modules for root frameworks, adversaries can hook system APIs and alter the return value and/or system data structures to alter functionality/visibility of various aspects of the system.

## Mitigations
- M1002: Attestation
- M1010: Deploy Compromised Device Detection Method

## Known Software Using This Technique
- S1208: FjordPhantom
- S1231: GodFather
- S0407: Monokle


---

# T1420: File and Directory Discovery


**ATT&CK ID:** T1420  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Discovery  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1420  

## Description
Adversaries may enumerate files and directories or search in specific device locations for desired information within a filesystem. Adversaries may use the information from [File and Directory Discovery](https://attack.mitre.org/techniques/T1420) during automated discovery to shape follow-on behaviors, including deciding if the adversary should fully infect the target and/or attempt specific actions. 

On Android, Linux file permissions and SELinux policies typically stringently restrict what can be accessed by apps without taking advantage of a privilege escalation exploit. The contents of the external storage directory are generally visible, which could present concerns if sensitive data is inappropriately stored there. iOS's security architecture generally restricts the ability to perform any type of [File and Directory Discovery](https://attack.mitre.org/techniques/T1420) without use of escalated privileges.

## Mitigations
- M1006: Use Recent OS Version

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S1095: AhRat
- S0529: CarbonSteal
- S1225: CherryBlos
- S0505: Desert Scorpion
- S9005: DocSwap
- S0550: DoubleAgent
- S1092: Escobar
- S0577: FrozenCell
- S0535: Golden Cup
- S0551: GoldenEagle
- S1077: Hornbill
- S1241: RatMilad
- S9030: SameCoin
- S0549: SilkBean
- S0558: Tiktok Pro
- S1216: TriangleDB
- S9006: VajraSpy


---

# T1406: Obfuscated Files or Information


**ATT&CK ID:** T1406  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1406  

## Description
Adversaries may attempt to make a payload or file difficult to discover or analyze by encrypting, encoding, or otherwise obfuscating its contents on the device or in transit. This is common behavior that can be used across different platforms and the network to evade defenses. 
 
Payloads may be compressed, archived, or encrypted in order to avoid detection. These payloads may be used during Initial Access or later to mitigate detection. Portions of files can also be encoded to hide the plaintext strings that would otherwise help defenders with discovery. Payloads may also be split into separate, seemingly benign files that only reveal malicious functionality when reassembled.(Citation: Microsoft MalLockerB)

## Sub-techniques
- T1406.001: Steganography
- T1406.002: Software Packing

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S1061: AbstractEmu
- S1095: AhRat
- S0525: Android/AdDisplay.Ashas
- S1214: Android/SpyAgent
- S0524: AndroidOS/MalLocker.B
- S0540: Asacub
- S1094: BRATA
- S0293: BrainTest
- S0432: Bread
- S0555: CHEMISTGAMES
- S0529: CarbonSteal
- S0480: Cerberus
- S0323: Charger
- S9004: Crocodilus
- S9005: DocSwap
- S0550: DoubleAgent
- S1054: Drinik
- S0420: Dvmap
- S0478: EventBot
- S0509: FakeSpy
- S0408: FlexiSpy
- S1067: FluBot
- S0536: GPlayed
- S0423: Ginp
- S1231: GodFather
- S0421: GolfSpy
- S0406: Gustuff
- S0544: HenBox
- S0463: INSOMNIA
- S1185: LightSpy
- S0485: Mandrake
- S0407: Monokle
- S0286: OBAD
- S0399: Pallas
- S0539: Red Alert 2.0
- S0411: Rotexy
- S1055: SharkBot
- S0549: SilkBean
- S1195: SpyC23
- S0545: TERRACOTTA
- S1056: TianySpy
- S0427: TrickMo
- S0312: WireLurker
- S0489: WolfRAT
- S0318: XLoader for Android
- S0494: Zen


---

# T1516: Input Injection


**ATT&CK ID:** T1516  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion, Impact  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1516  

## Description
A malicious application can inject input to the user interface to mimic user interaction through the abuse of Android's accessibility APIs.

[Input Injection](https://attack.mitre.org/techniques/T1516) can be achieved using any of the following methods:

* Mimicking user clicks on the screen, for example to steal money from a user's PayPal account.(Citation: android-trojan-steals-paypal-2fa)
* Injecting global actions, such as `GLOBAL_ACTION_BACK` (programatically mimicking a physical back button press), to trigger actions on behalf of the user.(Citation: Talos Gustuff Apr 2019)
* Inserting input into text fields on behalf of the user. This method is used legitimately to auto-fill text fields by applications such as password managers.(Citation: bitwarden autofill logins)

## Mitigations
- M1011: User Guidance
- M1012: Enterprise Policy

## Known Software Using This Technique
- S1094: BRATA
- S0480: Cerberus
- S9004: Crocodilus
- S0479: DEFENSOR ID
- S0423: Ginp
- S1231: GodFather
- S0406: Gustuff
- S0485: Mandrake
- S0403: Riltok
- S1062: S.O.V.A.
- S1055: SharkBot
- S0545: TERRACOTTA
- S0427: TrickMo
- S0494: Zen


---

# T1464: Network Denial of Service


**ATT&CK ID:** T1464  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Impact  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1464  

## Description
Adversaries may perform Network Denial of Service (DoS) attacks to degrade or block the availability of targeted resources to users. Network DoS can be performed by exhausting the network bandwidth that services rely on, or by jamming the signal going to or coming from devices. 

A Network DoS will occur when an adversary is able to jam radio signals (e.g. Wi-Fi, cellular, GPS) around a device to prevent it from communicating. For example, to jam cellular signal, an adversary may use a handheld signal jammer, which jam devices within the jammer’s operational range.(Citation: NIST-SP800187) 

Usage of cellular jamming has been documented in several arrests reported in the news.(Citation: CNET-Celljammer)(Citation: NYTimes-Celljam)(Citation: Digitaltrends-Celljam)(Citation: Arstechnica-Celljam)

## Known Software Using This Technique
- S1062: S.O.V.A.


---

# T1577: Compromise Application Executable


**ATT&CK ID:** T1577  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Persistence  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1577  

## Description
Adversaries may modify applications installed on a device to establish persistent access to a victim. These malicious modifications can be used to make legitimate applications carry out adversary tasks when these applications are in use.

There are multiple ways an adversary can inject malicious code into applications. One method is by taking advantages of device vulnerabilities, the most well-known being Janus, an Android vulnerability that allows adversaries to add extra bytes to APK (application) and DEX (executable) files without affecting the file's signature. By being able to add arbitrary bytes to valid applications, attackers can seamlessly inject code into genuine executables without the user's knowledge.(Citation: Guardsquare Janus)

Adversaries may also rebuild applications to include malicious modifications. This can be achieved by decompiling the genuine application, merging it with the malicious code, and recompiling it.(Citation: CheckPoint Agent Smith)

Adversaries may also take action to conceal modifications to application executables and bypass user consent. These actions include altering modifications to appear as an update or exploiting vulnerabilities that allow activities of the malicious application to run inside a system application.(Citation: CheckPoint Agent Smith)

## Mitigations
- M1001: Security Updates
- M1006: Use Recent OS Version

## Known Software Using This Technique
- S0440: Agent Smith
- S1079: BOULDSPY
- S0311: YiSpecter


---

# T1624: Event Triggered Execution


**ATT&CK ID:** T1624  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Persistence  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1624  

## Description
Adversaries may establish persistence using system mechanisms that trigger execution based on specific events. Mobile operating systems have means to subscribe to events such as receiving an SMS message, device boot completion, or other device activities. 

Adversaries may abuse these mechanisms as a means of maintaining persistent access to a victim via automatically and repeatedly executing malicious code. After gaining access to a victim’s system, adversaries may create or modify event triggers to point to malicious content that will be executed whenever the event trigger is invoked.

## Sub-techniques
- T1624.001: Broadcast Receivers

## Mitigations
- M1006: Use Recent OS Version

## Known Software Using This Technique
- S1079: BOULDSPY
- S1231: GodFather


---

# T1422: System Network Configuration Discovery


**ATT&CK ID:** T1422  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Discovery  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1422  

## Description
Adversaries may look for details about the network configuration and settings, such as IP and/or MAC addresses, of devices they access or through information discovery of remote systems. 

Adversaries may use the information from [System Network Configuration Discovery](https://attack.mitre.org/techniques/T1422) during automated discovery to shape follow-on behaviors, including determining certain access within the target network and what actions to do next. 

On Android, details of onboard network interfaces are accessible to apps through the `java.net.NetworkInterface` class.(Citation: NetworkInterface) Previously, the Android `TelephonyManager` class could be used to gather telephony-related device identifiers, information such as the IMSI, IMEI, and phone number. However, starting with Android 10, only preloaded, carrier, the default SMS, or device and profile owner applications can access the telephony-related device identifiers.(Citation: TelephonyManager) 

 

On iOS, gathering network configuration information is not possible without root access. 

 

Adversaries may use the information from [System Network Configuration Discovery](https://attack.mitre.org/techniques/T1422) during automated discovery to shape follow-on behaviors, including determining certain access within the target network and what actions to do next.

## Sub-techniques
- T1422.001: Internet Connection Discovery
- T1422.002: Wi-Fi Discovery

## Mitigations
- M1006: Use Recent OS Version

## Known Threat Groups Using This Technique
- G1028: APT-C-23

## Known Software Using This Technique
- S0310: ANDROIDOS_ANSERVER.A
- S1061: AbstractEmu
- S0292: AndroRAT
- S1214: Android/SpyAgent
- S0540: Asacub
- S1079: BOULDSPY
- S1215: Binary Validator
- S0432: Bread
- S0529: CarbonSteal
- S0425: Corona Updates
- S9005: DocSwap
- S0315: DualToy
- S0478: EventBot
- S0522: Exobot
- S0405: Exodus
- S0509: FakeSpy
- S1093: FlyTrap
- S0577: FrozenCell
- S0536: GPlayed
- S1231: GodFather
- S0535: Golden Cup
- S0406: Gustuff
- S1077: Hornbill
- S0463: INSOMNIA
- S1185: LightSpy
- S0407: Monokle
- S0291: PJApps
- S0316: Pegasus for Android
- S1241: RatMilad
- S0326: RedDrop
- S0403: Riltok
- S0411: Rotexy
- S0313: RuMMS
- S0324: SpyDealer
- S0328: Stealth Mango
- S1082: Sunbird
- S0545: TERRACOTTA
- S0329: Tangelo
- S1056: TianySpy
- S1216: TriangleDB
- S0427: TrickMo
- S0506: ViperRAT
- S0489: WolfRAT
- S0318: XLoader for Android
- S0490: XLoader for iOS
- S0311: YiSpecter


---

# T1512: Video Capture


**ATT&CK ID:** T1512  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1512  

## Description
An adversary can leverage a device’s cameras to gather information by capturing video recordings. Images may also be captured, potentially in specified intervals, in lieu of video files.  

 

Malware or scripts may interact with the device cameras through an available API provided by the operating system. Video or image files may be written to disk and exfiltrated later. This technique differs from [Screen Capture](https://attack.mitre.org/techniques/T1513) due to use of the device’s cameras for video recording rather than capturing the victim’s screen. 

 

In Android, an application must hold the `android.permission.CAMERA` permission to access the cameras. In iOS, applications must include the `NSCameraUsageDescription` key in the `Info.plist` file. In both cases, the user must grant permission to the requesting application to use the camera. If the device has been rooted or jailbroken, an adversary may be able to access the camera without knowledge of the user.

## Mitigations
- M1006: Use Recent OS Version

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S1061: AbstractEmu
- S0292: AndroRAT
- S1079: BOULDSPY
- S0655: BusyGasper
- S0426: Concipit1248
- S0425: Corona Updates
- S9004: Crocodilus
- S1243: DCHSpy
- S0301: Dendroid
- S0505: Desert Scorpion
- S9005: DocSwap
- S0320: DroidJack
- S1092: Escobar
- S0405: Exodus
- S1080: Fakecalls
- S0408: FlexiSpy
- S0535: Golden Cup
- S0551: GoldenEagle
- S0421: GolfSpy
- S0544: HenBox
- S1128: HilalRAT
- S1077: Hornbill
- S1185: LightSpy
- S0407: Monokle
- S0399: Pallas
- S0316: Pegasus for Android
- S1126: Phenakite
- S0295: RCSAndroid
- S1241: RatMilad
- S0549: SilkBean
- S0327: Skygofree
- S1195: SpyC23
- S0324: SpyDealer
- S0328: Stealth Mango
- S1082: Sunbird
- S1069: TangleBot
- S0558: Tiktok Pro
- S9006: VajraSpy
- S0418: ViceLeaker
- S0506: ViperRAT
- S0489: WolfRAT


---

# T1481.003: One-Way Communication

**Parent technique:** T1481
**ATT&CK ID:** T1481.003  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1481/003  

## Description
Adversaries may use an existing, legitimate external Web service channel as a means for sending commands to a compromised system without receiving return output. Compromised systems may leverage popular websites and social media to host command and control (C2) instructions. Those infected systems may opt to send the output from those commands back over a different C2 channel, including to another distinct Web service. Alternatively, compromised systems may return no output at all in cases where adversaries want to send instructions to systems and do not want a response. 

 

Popular websites and social media, acting as a mechanism for C2, may give a significant amount of cover. This is due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection.

## Known Software Using This Technique
- S0302: Twitoor


---

# T1471: Data Encrypted for Impact


**ATT&CK ID:** T1471  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Impact  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1471  

## Description
An adversary may encrypt files stored on a mobile device to prevent the user from accessing them. This may be done in order to extract monetary compensation from a victim in exchange for decryption or a decryption key (ransomware) or to render data permanently inaccessible in cases where the key is not saved or transmitted.

## Known Software Using This Technique
- S0422: Anubis
- S1062: S.O.V.A.
- S0298: Xbot


---

# T1629.001: Prevent Application Removal

**Parent technique:** T1629
**ATT&CK ID:** T1629.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1629/001  

## Description
Adversaries may abuse the Android device administration API to prevent the user from uninstalling a target application. In earlier versions of Android, device administrator applications needed their administration capabilities explicitly deactivated by the user before the application could be uninstalled. This was later updated so the user could deactivate and uninstall the administrator application in one step.

Adversaries may also abuse the device accessibility APIs to prevent removal. This set of APIs allows the application to perform certain actions on behalf of the user and programmatically determine what is being shown on the screen. The malicious application could monitor the device screen for certain modals (e.g., the confirmation modal to uninstall an application) and inject screen input or a back button tap to close the modal. For example, Android's `performGlobalAction(int)` API could be utilized to prevent the user from removing the malicious application from the device after installation. If the user wants to uninstall the malicious application, two cases may occur, both preventing the user from removing the application.

* Case 1: If the integer argument passed to the API call is `2` or `GLOBAL_ACTION_HOME`, the malicious application may direct the user to the home screen from settings screen 

* Case 2: If the integer argument passed to the API call is `1` or `GLOBAL_ACTION_BACK`, the malicious application may emulate the back press event

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance
- M1012: Enterprise Policy

## Known Software Using This Technique
- S0422: Anubis
- S1083: Chameleon
- S9004: Crocodilus
- S1067: FluBot
- S1231: GodFather
- S0406: Gustuff
- S0485: Mandrake
- S0286: OBAD
- S1062: S.O.V.A.


---

# T1421: System Network Connections Discovery


**ATT&CK ID:** T1421  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Discovery  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1421  

## Description
Adversaries may attempt to get a listing of network connections to or from the compromised device they are currently accessing or from remote systems by querying for information over the network. 

 

This is typically accomplished by utilizing device APIs to collect information about nearby networks, such as Wi-Fi, Bluetooth, and cellular tower connections. On Android, this can be done by querying the respective APIs: 

 

* `WifiInfo` for information about the current Wi-Fi connection, as well as nearby Wi-Fi networks. Querying the `WiFiInfo` API requires the application to hold the `ACCESS_FINE_LOCATION` permission. 

* `BluetoothAdapter` for information about Bluetooth devices, which also requires the application to hold several permissions granted by the user at runtime. 

* For Android versions prior to Q, applications can use the `TelephonyManager.getNeighboringCellInfo()` method. For Q and later, applications can use the `TelephonyManager.getAllCellInfo()` method. Both methods require the application hold the `ACCESS_FINE_LOCATION` permission.

## Known Software Using This Technique
- S0405: Exodus
- S0509: FakeSpy
- S0408: FlexiSpy
- S1185: LightSpy
- S0407: Monokle
- S0399: Pallas
- S0289: Pegasus for iOS
- S0506: ViperRAT


---

# T1660: Phishing


**ATT&CK ID:** T1660  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Initial Access  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1660  

## Description
Adversaries may send malicious content to users in order to gain access to their mobile devices. All forms of phishing are electronically delivered social engineering. Adversaries can conduct both non-targeted phishing, such as in mass malware spam campaigns, as well as more targeted phishing tailored for a specific individual, company, or industry, known as “spearphishing.” Phishing often involves social engineering techniques, such as posing as a trusted source, as well as evasion techniques, such as removing or manipulating emails or metadata/headers from compromised accounts being abused to send messages.

Mobile phishing may take various forms. For example, adversaries may send emails containing malicious attachments or links, typically to deliver and then execute malicious code on victim devices. Phishing may also be conducted via third-party services, like social media platforms. Adversaries may also impersonate executives of organizations to persuade victims into performing some action on their behalf. For example, adversaries will often use social engineering techniques in text messages to trick the victims into acting quickly, which leads to adversaries obtaining credentials and other information. 

Mobile devices are a particularly attractive target for adversaries executing phishing campaigns.  Due to their smaller form factor than traditional desktop endpoints, users may not be able to notice minor differences between genuine and phishing websites. Further, mobile devices have additional sensors and radios that allow adversaries to execute phishing attempts over several different vectors, such as: 

- SMS messages: Adversaries may send SMS messages (known as “smishing”) from compromised devices to potential targets to convince the target to, for example, install malware, navigate to a specific website, or enable certain insecure configurations on their device.
- Quick Response (QR) Codes: Adversaries may use QR codes (known as “quishing”) to redirect users to a phishing website. For example, an adversary could replace a legitimate public QR Code with one that leads to a different destination, such as a phishing website. A malicious QR code could also be delivered via other means, such as SMS or email. In the latter case, an adversary could utilize a malicious QR code in an email to pivot from the user’s desktop computer to their mobile device.
- Phone Calls: Adversaries may call victims (known as "vishing") to persuade them to perform an action, such as providing login credentials or navigating to malicious websites. Common vishing targets include employees, especially executives of organizations, and help desks. This may also be used as a technique to perform the initial access on a mobile device, but then pivot to a desktop computer by having the victims perform actions on a desktop computer. With the rise of artificial intelligence (AI), adversaries may also use AI to clone a person’s voice, resulting in deepfake vishing. The cloned voice provides familiarity to the victims, increasing the likelihood of successful malicious actions performed by the victims. Additionally, adversaries may leave voicemails, which may use a real person’s voice or an AI-generated voice; these scams would urgently ask victims into calling back to perform an action, e.g. sending money or providing sensitive information and credentials.

## Mitigations
- M1011: User Guidance
- M1058: Antivirus/Antimalware

## Known Threat Groups Using This Technique
- G1028: APT-C-23
- G1002: BITTER
- G0094: Kimsuky
- G0034: Sandworm Team
- G1015: Scattered Spider
- G1029: UNC788

## Known Software Using This Technique
- S1094: BRATA
- S1083: Chameleon
- S1225: CherryBlos
- S9005: DocSwap
- S1208: FjordPhantom
- S1067: FluBot
- S1231: GodFather
- S1185: LightSpy
- S0289: Pegasus for iOS
- S1241: RatMilad
- S9006: VajraSpy


---

# T1521.003: SSL Pinning

**Parent technique:** T1521
**ATT&CK ID:** T1521.003  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1521/003  

## Description
Adversaries may use [SSL Pinning](https://attack.mitre.org/techniques/T1521/003)  to protect the C2 traffic from being intercepted and analyzed.

[SSL Pinning](https://attack.mitre.org/techniques/T1521/003)  is a technique commonly utilized by legitimate websites to ensure that encrypted communications are only allowed with a pre-defined certificate. If another certificate is presented, it could indicate device compromise, traffic interception, or another upstream issue. While benign usages are common, it is also possible for adversaries to abuse this technology to protect malicious C2 traffic.

In normal, not pinned SSL validation, when a client connects to a server using HTTPS, it typically checks whether the server’s SSL/TLS certificate is signed by a trusted Certificate Authority (CA) in the device’s trust store. If the certificate is valid and signed by a trusted CA, the connection is established. However, with [SSL Pinning](https://attack.mitre.org/techniques/T1521/003) , the client is configured to trust a specific SSL/TLS certificate or public key, rather than relying on the device’s trust store. This means that even if the server’s certificate is signed by a trusted CA, the client will only establish the connection of the certificate or key is pinned.

There are two types of [SSL Pinning](https://attack.mitre.org/techniques/T1521/003) :

1.	Certificate Pinning: The client stores a copy of the server’s certificate and compares it with the certificate received during the SSL handshake. If the certificates match, then the client proceeds with the connection. This approach also works with self-signed certificates.

2.	Public Key Pinning: Instead of pinning the entire certificate, the client pins just the public key extracted from the certificate. This is often more flexible, as it allows the server to renew its certificate without having to update the pinned certificate or breaking the SSL connection.

## Mitigations
- M1011: User Guidance
- M1012: Enterprise Policy

## Known Software Using This Technique
- S0507: eSurv


---

# T1461: Lockscreen Bypass


**ATT&CK ID:** T1461  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Initial Access  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1461  

## Description
An adversary with physical access to a mobile device may seek to bypass the device’s lockscreen. Several methods exist to accomplish this, including:

* Biometric spoofing: If biometric authentication is used, an adversary could attempt to spoof a mobile device’s biometric authentication mechanism. Both iOS and Android partly mitigate this attack by requiring the device’s passcode rather than biometrics to unlock the device after every device restart, and after a set or random amount of time.(Citation: SRLabs-Fingerprint)(Citation: TheSun-FaceID)
* Unlock code bypass: An adversary could attempt to brute-force or otherwise guess the lockscreen passcode (typically a PIN or password), including physically observing (“shoulder surfing”) the device owner’s use of the lockscreen passcode. Mobile OS vendors partly mitigate this by implementing incremental backoff timers after a set number of failed unlock attempts, as well as a configurable full device wipe after several failed unlock attempts.
* Vulnerability exploit: Techniques have been periodically demonstrated that exploit mobile devices to bypass the lockscreen. The vulnerabilities are generally patched by the device or OS vendor once disclosed.(Citation: Wired-AndroidBypass)(Citation: Kaspersky-iOSBypass)

## Mitigations
- M1001: Security Updates
- M1012: Enterprise Policy

## Known Software Using This Technique
- S1094: BRATA
- S1083: Chameleon
- S1092: Escobar
- S9006: VajraSpy


---

# T1636.003: Contact List

**Parent technique:** T1636
**ATT&CK ID:** T1636.003  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1636/003  

## Description
Adversaries may utilize standard operating system APIs to gather contact list data. On Android, this can be accomplished using the Contacts Content Provider. On iOS, this can be accomplished using the `Contacts` framework. 

 

If the device has been jailbroken or rooted, an adversary may be able to access the [Contact List](https://attack.mitre.org/techniques/T1636/003) without the user’s knowledge or approval.

## Mitigations
- M1011: User Guidance

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S1061: AbstractEmu
- S0309: Adups
- S1095: AhRat
- S0292: AndroRAT
- S0304: Android/Chuli.A
- S0422: Anubis
- S0540: Asacub
- S1079: BOULDSPY
- S0480: Cerberus
- S0323: Charger
- S0425: Corona Updates
- S9004: Crocodilus
- S1243: DCHSpy
- S0505: Desert Scorpion
- S9005: DocSwap
- S0550: DoubleAgent
- S0522: Exobot
- S0405: Exodus
- S0509: FakeSpy
- S1080: Fakecalls
- S0408: FlexiSpy
- S1067: FluBot
- S0536: GPlayed
- S0423: Ginp
- S1231: GodFather
- S0535: Golden Cup
- S0551: GoldenEagle
- S0421: GolfSpy
- S0406: Gustuff
- S0544: HenBox
- S1128: HilalRAT
- S1077: Hornbill
- S0463: INSOMNIA
- S1185: LightSpy
- S0485: Mandrake
- S0407: Monokle
- S0399: Pallas
- S0316: Pegasus for Android
- S0289: Pegasus for iOS
- S1126: Phenakite
- S1241: RatMilad
- S0539: Red Alert 2.0
- S0403: Riltok
- S0411: Rotexy
- S0549: SilkBean
- S1195: SpyC23
- S0324: SpyDealer
- S0305: SpyNote RAT
- S0328: Stealth Mango
- S1082: Sunbird
- S1069: TangleBot
- S0558: Tiktok Pro
- S9006: VajraSpy
- S0506: ViperRAT
- S0489: WolfRAT
- S0507: eSurv


---

# T1533: Data from Local System


**ATT&CK ID:** T1533  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1533  

## Description
Adversaries may search local system sources, such as file systems or local databases, to find files of interest and sensitive data prior to exfiltration.  

 

Access to local system data, which includes information stored by the operating system, often requires escalated privileges. Examples of local system data include authentication tokens, the device keyboard cache, Wi-Fi passwords, and photos. On Android, adversaries may also attempt to access files from external storage which may require additional storage-related permissions.

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S1061: AbstractEmu
- S1095: AhRat
- S0422: Anubis
- S1079: BOULDSPY
- S1094: BRATA
- S1215: Binary Validator
- S0655: BusyGasper
- S0555: CHEMISTGAMES
- S1083: Chameleon
- S0426: Concipit1248
- S0425: Corona Updates
- S1243: DCHSpy
- S0301: Dendroid
- S0505: Desert Scorpion
- S9005: DocSwap
- S0550: DoubleAgent
- S1054: Drinik
- S1092: Escobar
- S0405: Exodus
- S1080: Fakecalls
- S0408: FlexiSpy
- S0577: FrozenCell
- S0536: GPlayed
- S0423: Ginp
- S0535: Golden Cup
- S0551: GoldenEagle
- S0421: GolfSpy
- S0290: Gooligan
- S0406: Gustuff
- S0544: HenBox
- S1077: Hornbill
- S0463: INSOMNIA
- S1185: LightSpy
- S0407: Monokle
- S1126: Phenakite
- S0295: RCSAndroid
- S1241: RatMilad
- S0549: SilkBean
- S1195: SpyC23
- S0305: SpyNote RAT
- S0328: Stealth Mango
- S1082: Sunbird
- S0329: Tangelo
- S1069: TangleBot
- S0558: Tiktok Pro
- S1216: TriangleDB
- S0427: TrickMo
- S9006: VajraSpy
- S0418: ViceLeaker
- S0506: ViperRAT
- S0489: WolfRAT
- S0507: eSurv


---

# T1640: Account Access Removal


**ATT&CK ID:** T1640  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Impact  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1640  

## Description
Adversaries may interrupt availability of system and network resources by inhibiting access to accounts utilized by legitimate users. Accounts may be deleted, locked, or manipulated (ex: credentials changed) to remove access to accounts.

## Mitigations
- M1011: User Guidance

## Known Software Using This Technique
- S0407: Monokle


---

# T1426: System Information Discovery


**ATT&CK ID:** T1426  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Discovery  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1426  

## Description
Adversaries may attempt to get detailed information about a device’s operating system and hardware, including versions, patches, and architecture. Adversaries may use the information from [System Information Discovery](https://attack.mitre.org/techniques/T1426) during automated discovery to shape follow-on behaviors, including whether or not to fully infects the target and/or attempts specific actions. 

 

On Android, much of this information is programmatically accessible to applications through the `android.os.Build` class. (Citation: Android-Build) iOS is much more restrictive with what information is visible to applications. Typically, applications will only be able to query the device model and which version of iOS it is running.

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S0310: ANDROIDOS_ANSERVER.A
- S1061: AbstractEmu
- S1095: AhRat
- S0525: Android/AdDisplay.Ashas
- S0304: Android/Chuli.A
- S0422: Anubis
- S0540: Asacub
- S1079: BOULDSPY
- S1094: BRATA
- S0555: CHEMISTGAMES
- S0529: CarbonSteal
- S0480: Cerberus
- S1083: Chameleon
- S0425: Corona Updates
- S0505: Desert Scorpion
- S9005: DocSwap
- S0550: DoubleAgent
- S0420: Dvmap
- S0478: EventBot
- S0522: Exobot
- S0509: FakeSpy
- S0577: FrozenCell
- S0536: GPlayed
- S1231: GodFather
- S0535: Golden Cup
- S0551: GoldenEagle
- S0421: GolfSpy
- S0406: Gustuff
- S0544: HenBox
- S1077: Hornbill
- S0463: INSOMNIA
- S0288: KeyRaider
- S1185: LightSpy
- S0485: Mandrake
- S0407: Monokle
- S0399: Pallas
- S0289: Pegasus for iOS
- S1126: Phenakite
- S1241: RatMilad
- S0326: RedDrop
- S0403: Riltok
- S0411: Rotexy
- S0313: RuMMS
- S1062: S.O.V.A.
- S1082: Sunbird
- S1056: TianySpy
- S0558: Tiktok Pro
- S0427: TrickMo
- S9006: VajraSpy
- S0418: ViceLeaker
- S0506: ViperRAT
- S0318: XLoader for Android
- S0490: XLoader for iOS
- S0311: YiSpecter
- S0507: eSurv


---

# T1532: Archive Collected Data


**ATT&CK ID:** T1532  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Collection  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1532  

## Description
Adversaries may compress and/or encrypt data that is collected prior to exfiltration. Compressing data can help to obfuscate its contents and minimize use of network resources. Encryption can be used to hide information that is being exfiltrated from detection or make exfiltration less conspicuous upon inspection by a defender. 

 

Both compression and encryption are done prior to exfiltration, and can be performed using a utility, programming library, or custom algorithm.

## Known Software Using This Technique
- S0422: Anubis
- S0540: Asacub
- S1079: BOULDSPY
- S1094: BRATA
- S1243: DCHSpy
- S0505: Desert Scorpion
- S0405: Exodus
- S0577: FrozenCell
- S0535: Golden Cup
- S0421: GolfSpy
- S1185: LightSpy
- S1082: Sunbird
- S0424: Triada


---

# T1627.001: Geofencing

**Parent technique:** T1627
**ATT&CK ID:** T1627.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1627/001  

## Description
Adversaries may use a device’s geographical location to limit certain malicious behaviors. For example, malware operators may limit the distribution of a second stage payload to certain geographic regions.(Citation: Lookout eSurv)

[Geofencing](https://attack.mitre.org/techniques/T1627/001) is accomplished by persuading the user to grant the application permission to access location services. The application can then collect, process, and exfiltrate the device’s location to perform location-based actions, such as ceasing malicious behavior or showing region-specific advertisements. 

One method to accomplish [Geofencing](https://attack.mitre.org/techniques/T1627/001) on Android is to use the built-in Geofencing API to automatically trigger certain behaviors when the device enters or exits a specified radius around a geographical location. Similar to  other [Geofencing](https://attack.mitre.org/techniques/T1627/001) methods, this requires that the user has granted the `ACCESS_FINE_LOCATION` and `ACCESS_BACKGROUND_LOCATION` permissions. The latter is only required if the application targets Android 10 (API level 29) or higher. However, Android 11 introduced additional permission controls that may restrict background location collection based on user permission choices at runtime. These additional controls include "Allow only while using the app", which will effectively prohibit background location collection.  

Similarly, on iOS, developers can use built-in APIs to setup and execute geofencing. Depending on the use case, the app will either need to call `requestWhenInUseAuthorization()` or `requestAlwaysAuthorization()`, depending on when access to the location services is required. Similar to Android, users also have the option to limit when the application can access the device’s location, including one-time use and only when the application is running in the foreground.  

[Geofencing](https://attack.mitre.org/techniques/T1627/001) can be used to prevent exposure of capabilities in environments that are not intended to be compromised or operated within. For example, location data could be used to limit malware spread and/or capabilities, which could also potentially evade application analysis environments (ex: malware analysis outside of the target geographic area). Other malicious usages could include showing language-specific input prompts and/or advertisements.

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S1094: BRATA
- S0507: eSurv


---

# T1628.003: Conceal Multimedia Files

**Parent technique:** T1628
**ATT&CK ID:** T1628.003  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1628/003  

## Description
Adversaries may attempt to hide multimedia files from the user. By doing so, adversaries may conceal captured files, such as pictures, videos and/or screenshots, then later exfiltrate those files.  

Specific to Android devices, if the `.nomedia` file is present in a folder, multimedia files in that folder will not be visible to the user in the Gallery application. Additionally, other applications are asked not to scan the folder with the `.nomedia` file, effectively making the folder appear invisible to the user.  

This technique is often used by stalkerware and spyware applications.

## Mitigations
- M1059: Do Not Mitigate

## Known Threat Groups Using This Technique
- G0112: Windshift


---

# T1642: Endpoint Denial of Service


**ATT&CK ID:** T1642  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Impact  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1642  

## Description
Adversaries may perform Endpoint Denial of Service (DoS) attacks to degrade or block the availability of services to users.

On Android versions prior to 7, apps can abuse Device Administrator access to reset the device lock passcode, preventing the user from unlocking the device. After Android 7, only device or profile owners (e.g. MDMs) can reset the device’s passcode.(Citation: Android resetPassword)

On iOS devices, this technique does not work because mobile device management servers can only remove the screen lock passcode; they cannot set a new passcode. However, on jailbroken devices, malware has been discovered that can lock the user out of the device.(Citation: Xiao-KeyRaider)

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance

## Known Software Using This Technique
- S0323: Charger
- S0522: Exobot
- S0536: GPlayed
- S1185: LightSpy
- S0298: Xbot


---

# T1644: Out of Band Data


**ATT&CK ID:** T1644  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1644  

## Description
Adversaries may communicate with compromised devices using out of band data streams. This could be done for a variety of reasons, including evading network traffic monitoring, as a backup method of command and control, or for data exfiltration if the device is not connected to any Internet-providing networks (i.e. cellular or Wi-Fi). Several out of band data streams exist, such as SMS messages, NFC, and Bluetooth. 

 

On Android, applications can read push notifications to capture content from SMS messages, or other out of band data streams. This requires that the user manually grant notification access to the application via the settings menu. However, the application could launch an Intent to take the user directly there. 

 

On iOS, there is no way to programmatically read push notifications.

## Mitigations
- M1011: User Guidance

## Known Software Using This Technique
- S0304: Android/Chuli.A
- S1079: BOULDSPY
- S0655: BusyGasper
- S0529: CarbonSteal
- S0505: Desert Scorpion
- S0406: Gustuff
- S0407: Monokle
- S0316: Pegasus for Android
- S0289: Pegasus for iOS
- S0295: RCSAndroid
- S0411: Rotexy
- S1055: SharkBot
- S0327: Skygofree
- S1195: SpyC23
- S0324: SpyDealer
- S0328: Stealth Mango
- S1216: TriangleDB
- S0427: TrickMo


---

# T1521: Encrypted Channel


**ATT&CK ID:** T1521  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1521  

## Description
Adversaries may explicitly employ a known encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Despite the use of a secure algorithm, these implementations may be vulnerable to reverse engineering if necessary secret keys are encoded and/or generated within malware samples/configuration files.

## Sub-techniques
- T1521.001: Symmetric Cryptography
- T1521.002: Asymmetric Cryptography
- T1521.003: SSL Pinning

## Known Software Using This Technique
- S1095: AhRat
- S0302: Twitoor


---

# T1628.001: Suppress Application Icon

**Parent technique:** T1628
**ATT&CK ID:** T1628.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1628/001  

## Description
A malicious application could suppress its icon from being displayed to the user in the application launcher. This hides the fact that it is installed, and can make it more difficult for the user to uninstall the application. Hiding the application's icon programmatically does not require any special permissions. 

This behavior has been seen in the BankBot/Spy Banker family of malware.(Citation: android-trojan-steals-paypal-2fa)(Citation: sunny-stolen-credentials)(Citation: bankbot-spybanker) 

Beginning in Android 10, changes were introduced to inhibit malicious applications’ ability to hide their icon. If an app is a system app, requests no permissions, or does not have a launcher activity, the application’s icon will be fully hidden. Further, if the device is fully managed or the application is in a work profile, the icon will be fully hidden. Otherwise, a synthesized activity is shown, which is a launcher icon that represents the app’s details page in the system settings. If the user clicks the synthesized activity in the launcher, they are taken to the application’s details page in the system settings.(Citation: Android 10 Limitations to Hiding App Icons)(Citation: LauncherApps getActivityList)

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance

## Known Software Using This Technique
- S0440: Agent Smith
- S0525: Android/AdDisplay.Ashas
- S0655: BusyGasper
- S0480: Cerberus
- S0505: Desert Scorpion
- S0550: DoubleAgent
- S1054: Drinik
- S0509: FakeSpy
- S0408: FlexiSpy
- S1103: FlixOnline
- S0423: Ginp
- S0406: Gustuff
- S0485: Mandrake
- S0411: Rotexy
- S1062: S.O.V.A.
- S0419: SimBad
- S1195: SpyC23
- S0558: Tiktok Pro
- S0302: Twitoor
- S0418: ViceLeaker
- S0311: YiSpecter


---

# T1655: Masquerading


**ATT&CK ID:** T1655  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1655  

## Description
Adversaries may attempt to manipulate features of their artifacts to make them appear legitimate or benign to users and/or security tools. Masquerading occurs when the name, location, or appearance of an object, legitimate or malicious, is manipulated or abused for the sake of evading defenses and observation. This may include manipulating file metadata, tricking users into misidentifying the file type, and giving legitimate task or service names.

Renaming abusable system utilities to evade security monitoring is also a form of [Masquerading](https://attack.mitre.org/techniques/T1655)

## Sub-techniques
- T1655.001: Match Legitimate Name or Location

## Mitigations
- M1011: User Guidance

## Known Software Using This Technique
- S1225: CherryBlos
- S9004: Crocodilus
- S1208: FjordPhantom
- S1185: LightSpy
- S9006: VajraSpy


---

# T1406.001: Steganography

**Parent technique:** T1406
**ATT&CK ID:** T1406.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1406/001  

## Description
Adversaries may use steganography techniques in order to prevent the detection of hidden information. Steganographic techniques can be used to hide data in digital media such as images, audio tracks, video clips, or text files.

## Known Software Using This Technique
- S0440: Agent Smith


---

# T1628: Hide Artifacts


**ATT&CK ID:** T1628  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1628  

## Description
Adversaries may attempt to hide artifacts associated with their behaviors to evade detection. Mobile operating systems have features and developer APIs to hide various artifacts, such as an application’s launcher icon. These APIs have legitimate usages, such as hiding an icon to avoid application drawer clutter when an application does not have a usable interface. Adversaries may abuse these features and APIs to hide artifacts from the user to evade detection.

## Sub-techniques
- T1628.001: Suppress Application Icon
- T1628.002: User Evasion
- T1628.003: Conceal Multimedia Files


---

# T1632.001: Code Signing Policy Modification

**Parent technique:** T1632
**ATT&CK ID:** T1632.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1632/001  

## Description
Adversaries may modify code signing policies to enable execution of applications signed with unofficial or unknown keys. Code signing provides a level of authenticity on an app from a developer, guaranteeing that the program has not been tampered with and comes from an official source. Security controls can include enforcement mechanisms to ensure that only valid, signed code can be run on a device. 

Mobile devices generally enable these security controls by default, such as preventing the installation of unknown applications on Android. Adversaries may modify these policies in a number of ways, including [Input Injection](https://attack.mitre.org/techniques/T1516) or malicious configuration profiles.

## Mitigations
- M1006: Use Recent OS Version
- M1011: User Guidance
- M1012: Enterprise Policy

## Known Threat Groups Using This Technique
- G0112: Windshift

## Known Software Using This Technique
- S0505: Desert Scorpion
- S0420: Dvmap
- S0551: GoldenEagle
- S0485: Mandrake
- S0549: SilkBean
- S1056: TianySpy
- S0490: XLoader for iOS
- S0311: YiSpecter


---

# T1637.001: Domain Generation Algorithms

**Parent technique:** T1637
**ATT&CK ID:** T1637.001  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Command And Control  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1637/001  

## Description
Adversaries may use [Domain Generation Algorithms](https://attack.mitre.org/techniques/T1637/001) (DGAs) to procedurally generate domain names for uses such as command and control communication   or malicious application distribution.(Citation: securelist rotexy 2018)

DGAs increase the difficulty for defenders to block, track, or take over the command and control channel, as there could potentially be thousands of domains that malware can check for instructions.

## Known Software Using This Technique
- S1067: FluBot
- S0485: Mandrake
- S0411: Rotexy
- S1055: SharkBot


---

# T1456: Drive-By Compromise


**ATT&CK ID:** T1456  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Initial Access  
**Platforms:** Android, iOS  
**Reference:** https://attack.mitre.org/techniques/T1456  

## Description
Adversaries may gain access to a system through a user visiting a website over the normal course of browsing. With this technique, the user's web browser is typically targeted for exploitation, but adversaries may also use compromised websites for non-exploitation behavior such as acquiring an [Application Access Token](https://attack.mitre.org/techniques/T1550/001).

Multiple ways of delivering exploit code to a browser exist, including:

* A legitimate website is compromised where adversaries have injected some form of malicious code such as JavaScript, iFrames, and cross-site scripting.
* Malicious ads are paid for and served through legitimate ad providers.
* Built-in web application interfaces are leveraged for the insertion of any other kind of object that can be used to display web content or contain a script that executes on the visiting client (e.g. forum posts, comments, and other user controllable web content).

Often the website used by an adversary is one visited by a specific community, such as government, a particular industry, or region, where the goal is to compromise a specific user or set of users based on a shared interest. This kind of targeted attack is referred to a strategic web compromise or watering hole attack. There are several known examples of this occurring.(Citation: Lookout-StealthMango)

Typical drive-by compromise process:

1. A user visits a website that is used to host the adversary controlled content.
2. Scripts automatically execute, typically searching versions of the browser and plugins for a potentially vulnerable version. 
    * The user may be required to assist in this process by enabling scripting or active website components and ignoring warning dialog boxes.
3. Upon finding a vulnerable version, exploit code is delivered to the browser.
4. If exploitation is successful, then it will give the adversary code execution on the user's system unless other protections are in place.
    * In some cases a second visit to the website after the initial scan is required before exploit code is delivered.

## Mitigations
- M1001: Security Updates

## Known Software Using This Technique
- S0463: INSOMNIA
- S1185: LightSpy
- S0289: Pegasus for iOS
- S0328: Stealth Mango
- S0311: YiSpecter


---

# TA0027: Initial Access

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0027  

## Description
The adversary is trying to get into your device.

The initial access tactic represents the vectors adversaries use to gain an initial foothold onto a mobile device.

## Techniques in This Tactic
- T1451: SIM Card Swap
- T1456: Drive-By Compromise
- T1458: Replication Through Removable Media
- T1461: Lockscreen Bypass
- T1474: Supply Chain Compromise
- T1474.001: Compromise Software Dependencies and Development Tools
- T1474.002: Compromise Hardware Supply Chain
- T1474.003: Compromise Software Supply Chain
- T1660: Phishing
- T1661: Application Versioning
- T1664: Exploitation for Initial Access


---

# TA0036: Exfiltration

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0036  

## Description
The adversary is trying to steal data.

Exfiltration refers to techniques and attributes that result or aid in the adversary removing files and information from the targeted mobile device.

In the mobile environment, mobile devices are frequently connected to networks outside enterprise control such as cellular networks or public Wi-Fi networks. Adversaries could attempt to evade detection by communicating on these networks, and potentially even by using non-Internet Protocol mechanisms such as Short Message Service (SMS). However, cellular networks often have data caps and/or extra data charges that could increase the potential for adversarial communication to be detected.

## Techniques in This Tactic
- T1639: Exfiltration Over Alternative Protocol
- T1639.001: Exfiltration Over Unencrypted Non-C2 Protocol
- T1646: Exfiltration Over C2 Channel


---

# TA0028: Persistence

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0028  

## Description
The adversary is trying to maintain their foothold.

Persistence is any access, action, or configuration change to a mobile device that gives an attacker a persistent presence on the device. Attackers often will need to maintain access to mobile devices through interruptions such as device reboots and potentially even factory data resets.

## Techniques in This Tactic
- T1398: Boot or Logon Initialization Scripts
- T1541: Foreground Persistence
- T1577: Compromise Application Executable
- T1603: Scheduled Task/Job
- T1624: Event Triggered Execution
- T1624.001: Broadcast Receivers
- T1625: Hijack Execution Flow
- T1625.001: System Runtime API Hijacking
- T1645: Compromise Client Software Binary
- T1676: Linked Devices


---

# TA0029: Privilege Escalation

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0029  

## Description
The adversary is trying to gain higher-level permissions.

Privilege escalation includes techniques that allow an attacker to obtain a higher level of permissions on the mobile device. Attackers may enter the mobile device with very limited privileges and may be required to take advantage of a device weakness to obtain higher privileges necessary to successfully carry out their mission objectives.

## Techniques in This Tactic
- T1404: Exploitation for Privilege Escalation
- T1626: Abuse Elevation Control Mechanism
- T1626.001: Device Administrator Permissions
- T1631: Process Injection
- T1631.001: Ptrace System Calls


---

# TA0037: Command and Control

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0037  

## Description
The adversary is trying to communicate with compromised devices to control them.

The command and control tactic represents how adversaries communicate with systems under their control within a target network. There are many ways an adversary can establish command and control with various levels of covertness, depending on system configuration and network topology. Due to the wide degree of variation available to the adversary at the network level, only the most common factors were used to describe the differences in command and control. There are still a great many specific techniques within the documented methods, largely due to how easy it is to define new protocols and use existing, legitimate protocols and network services for communication. 

The resulting breakdown should help convey the concept that detecting intrusion through command and control protocols without prior knowledge is a difficult proposition over the long term. Adversaries' main constraints in network-level defense avoidance are testing and deployment of tools to rapidly change their protocols, awareness of existing defensive technologies, and access to legitimate Web services that, when used appropriately, make their tools difficult to distinguish from benign traffic.

Additionally, in the mobile environment, mobile devices are frequently connected to networks outside enterprise control such as cellular networks or public Wi-Fi networks. Adversaries could attempt to evade detection by communicating on these networks, and potentially even by using non-Internet Protocol mechanisms such as Short Message Service (SMS). However, cellular networks often have data caps and/or extra data charges that could increase the potential for adversarial communication to be detected.

## Techniques in This Tactic
- T1437: Application Layer Protocol
- T1437.001: Web Protocols
- T1481: Web Service
- T1481.001: Dead Drop Resolver
- T1481.002: Bidirectional Communication
- T1481.003: One-Way Communication
- T1509: Non-Standard Port
- T1521: Encrypted Channel
- T1521.001: Symmetric Cryptography
- T1521.002: Asymmetric Cryptography
- T1521.003: SSL Pinning
- T1544: Ingress Tool Transfer
- T1616: Call Control
- T1637: Dynamic Resolution
- T1637.001: Domain Generation Algorithms
- T1644: Out of Band Data
- T1663: Remote Access Software


---

# TA0041: Execution

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0041  

## Description
The adversary is trying to run malicious code.

Execution consists of techniques that result in adversary-controlled code running on a mobile device. Techniques that run malicious code are often paired with techniques from all other tactics to achieve broader goals, like exploring a network or stealing data.

## Techniques in This Tactic
- T1575: Native API
- T1603: Scheduled Task/Job
- T1623: Command and Scripting Interpreter
- T1623.001: Unix Shell
- T1658: Exploitation for Client Execution


---

# TA0034: Impact

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0034  

## Description
The adversary is trying to manipulate, interrupt, or destroy your devices and data.

The impact tactic consists of techniques used by the adversary to execute his or her mission objectives but that do not cleanly fit into another category such as Collection. Mission objectives vary based on each adversary's goals, but examples include toll fraud, destruction of device data, or locking the user out of his or her device until a ransom is paid.

## Techniques in This Tactic
- T1464: Network Denial of Service
- T1471: Data Encrypted for Impact
- T1516: Input Injection
- T1582: SMS Control
- T1616: Call Control
- T1640: Account Access Removal
- T1641: Data Manipulation
- T1641.001: Transmitted Data Manipulation
- T1642: Endpoint Denial of Service
- T1643: Generate Traffic from Victim
- T1662: Data Destruction


---

# TA0031: Credential Access

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0031  

## Description
The adversary is trying to steal account names, passwords, or other secrets that enable access to resources.

Credential access represents techniques that can be used by adversaries to obtain access to or control over passwords, tokens, cryptographic keys, or other values that could be used by an adversary to gain unauthorized access to resources. Credential access allows the adversary to assume the identity of an account, with all of that account's permissions on the system and network, and makes it harder for defenders to detect the adversary. With sufficient access within a network, an adversary can create accounts for later use within the environment.

## Techniques in This Tactic
- T1414: Clipboard Data
- T1417: Input Capture
- T1417.001: Keylogging
- T1417.002: GUI Input Capture
- T1453: Abuse Accessibility Features
- T1517: Access Notifications
- T1634: Credentials from Password Store
- T1634.001: Keychain
- T1635: Steal Application Access Token
- T1635.001: URI Hijacking


---

# TA0035: Collection

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0035  

## Description
The adversary is trying to gather data of interest to their goal.

Collection consists of techniques used to identify and gather information, such as sensitive files, from a target network prior to exfiltration. This category also covers locations on a system or network where the adversary may look for information to exfiltrate.

## Techniques in This Tactic
- T1409: Stored Application Data
- T1414: Clipboard Data
- T1417: Input Capture
- T1417.001: Keylogging
- T1417.002: GUI Input Capture
- T1429: Audio Capture
- T1430: Location Tracking
- T1430.001: Remote Device Management Services
- T1430.002: Impersonate SS7 Nodes
- T1453: Abuse Accessibility Features
- T1512: Video Capture
- T1513: Screen Capture
- T1517: Access Notifications
- T1532: Archive Collected Data
- T1533: Data from Local System
- T1616: Call Control
- T1636: Protected User Data
- T1636.001: Calendar Entries
- T1636.002: Call Log
- T1636.003: Contact List
- T1636.004: SMS Messages
- T1636.005: Accounts
- T1638: Adversary-in-the-Middle
- T1676: Linked Devices


---

# TA0033: Lateral Movement

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0033  

## Description
The adversary is trying to move through your environment.

Lateral movement consists of techniques that enable an adversary to access and control remote systems on a network and could, but does not necessarily, include execution of tools on remote systems. The lateral movement techniques could allow an adversary to gather information from a system without needing additional tools, such as a remote access tool.

## Techniques in This Tactic
- T1428: Exploitation of Remote Services
- T1458: Replication Through Removable Media


---

# TA0030: Defense Evasion

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0030  

## Description
The adversary is trying to avoid being detected.

Defense evasion consists of techniques an adversary may use to evade detection or avoid other defenses. Sometimes these actions are the same as or variations of techniques in other categories that have the added benefit of subverting a particular defense or mitigation. Defense evasion may be considered a set of attributes the adversary applies to all other phases of the operation.

## Techniques in This Tactic
- T1406: Obfuscated Files or Information
- T1406.001: Steganography
- T1406.002: Software Packing
- T1407: Download New Code at Runtime
- T1516: Input Injection
- T1541: Foreground Persistence
- T1575: Native API
- T1604: Proxy Through Victim
- T1617: Hooking
- T1627: Execution Guardrails
- T1627.001: Geofencing
- T1628: Hide Artifacts
- T1628.001: Suppress Application Icon
- T1628.002: User Evasion
- T1628.003: Conceal Multimedia Files
- T1629: Impair Defenses
- T1629.001: Prevent Application Removal
- T1629.002: Device Lockout
- T1629.003: Disable or Modify Tools
- T1630: Indicator Removal on Host
- T1630.001: Uninstall Malicious Application
- T1630.002: File Deletion
- T1630.003: Disguise Root/Jailbreak Indicators
- T1631: Process Injection
- T1631.001: Ptrace System Calls
- T1632: Subvert Trust Controls
- T1632.001: Code Signing Policy Modification
- T1633: Virtualization/Sandbox Evasion
- T1633.001: System Checks
- T1655: Masquerading
- T1655.001: Match Legitimate Name or Location
- T1661: Application Versioning
- T1670: Virtualization Solution


---

# TA0032: Discovery

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0032  

## Description
The adversary is trying to figure out your environment.

Discovery consists of techniques that allow the adversary to gain knowledge about the characteristics of the mobile device and potentially other networked systems. When adversaries gain access to a new system, they must orient themselves to what they now have control of and what benefits operating from that system give to their current objective or overall goals during the intrusion. The operating system may provide capabilities that aid in this post-compromise information-gathering phase.

## Techniques in This Tactic
- T1418: Software Discovery
- T1418.001: Security Software Discovery
- T1420: File and Directory Discovery
- T1421: System Network Connections Discovery
- T1422: System Network Configuration Discovery
- T1422.001: Internet Connection Discovery
- T1422.002: Wi-Fi Discovery
- T1423: Network Service Scanning
- T1424: Process Discovery
- T1426: System Information Discovery
- T1430: Location Tracking
- T1430.001: Remote Device Management Services
- T1430.002: Impersonate SS7 Nodes
