# MITRE D3FEND


---

# Harden (D3FEND Tactic)

**Reference:** https://d3fend.mitre.org/dao/artifact/d3f:Harden/  

## Definition
The harden tactic is used to increase the opportunity cost of computer network exploitation. Hardening differs from Detection in that it generally is conducted before a system is online and operational.

## Techniques Related to This Tactic (via 'enables' relationship)
- D3-AA: Agent Authentication
- D3-AH: Application Hardening
- D3-CH: Credential Hardening
- D3-MH: Message Hardening
- D3-PH: Platform Hardening
- D3-SCH: Source Code Hardening


---

# Detect (D3FEND Tactic)

**Reference:** https://d3fend.mitre.org/dao/artifact/d3f:Detect/  

## Definition
The detect tactic is used to identify adversary access to or unauthorized activity on computer networks.

## Techniques Related to This Tactic (via 'enables' relationship)
- D3-FA: File Analysis
- D3-ID: Identifier Analysis
- D3-MA: Message Analysis
- D3-NTA: Network Traffic Analysis
- D3-OSM: Operating System Monitoring
- D3-PA: Process Analysis
- D3-PHAM: Physical Access Monitoring
- D3-PM: Platform Monitoring
- D3-UBA: User Behavior Analysis


---

# Isolate (D3FEND Tactic)

**Reference:** https://d3fend.mitre.org/dao/artifact/d3f:Isolate/  

## Definition
The isolate tactic creates logical or physical barriers in a system which reduces opportunities for adversaries to create further accesses.

## Techniques Related to This Tactic (via 'enables' relationship)
- D3-AMED: Access Mediation
- D3-APA: Access Policy Administration
- D3-CF: Content Filtering
- D3-EI: Execution Isolation
- D3-NI: Network Isolation
- D3-OVAR: OT Variable Access Restriction


---

# Deceive (D3FEND Tactic)

**Reference:** https://d3fend.mitre.org/dao/artifact/d3f:Deceive/  

## Definition
The deceive tactic is used to advertise, entice, and allow potential attackers access to an observed or controlled environment.

## Techniques Related to This Tactic (via 'enables' relationship)
- D3-DE: Decoy Environment
- D3-DO: Decoy Object


---

# Evict (D3FEND Tactic)

**Reference:** https://d3fend.mitre.org/dao/artifact/d3f:Evict/  

## Definition
The eviction tactic is used to remove an adversary from a computer network.

## Techniques Related to This Tactic (via 'enables' relationship)
- D3-CE: Credential Eviction
- D3-OE: Object Eviction
- D3-PE: Process Eviction


---

# Restore (D3FEND Tactic)

**Reference:** https://d3fend.mitre.org/dao/artifact/d3f:Restore/  

## Definition
The restore tactic is used to return the system to a better state.

## Techniques Related to This Tactic (via 'enables' relationship)
- D3-RA: Restore Access
- D3-RO: Restore Object


---

# D3-ARMA: ARMA Model

**Synonym(s):** Autoregressive moving average model  
**Reference:** https://d3fend.mitre.org/technique/D3-ARMA/  

## Definition
Autoregressive-moving-average (ARMA) models provide a parsimonious description of a (weakly) stationary stochastic process in terms of two polynomials, one for the autoregression (AR) and the second for the moving average (MA).

## Parent Class(es)
- Time Series Analysis

## Knowledge Base Article
## References
Wikipedia. (n.d.). Autoregressive-moving-average model. [Link](https://en.wikipedia.org/wiki/Autoregressive%E2%80%93moving-average_model)


---

# D3-AMED: Access Mediation

**Synonym(s):** Access Control  
**Reference:** https://d3fend.mitre.org/technique/D3-AMED/  

## Definition
Access mediation is the process of granting or denying specific requests to: 1) obtain and use information and related information processing services; and 2) enter specific physical facilities (e.g., Federal buildings, military establishments, border crossing entrances). Access mediation decisions should enforce least privilege by granting access for scoped durations to prevent privilege creep and, where applicable, implement just-in-time (JIT) access. Denial decisions may prevent initial access or terminate access that has already been granted, ensuring continuous enforcement of security policies.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Isolate
- **kb-reference:** Reference - Committee on National Security Systems (CNSS) Glossary


---

# D3-AM: Access Modeling

**Reference:** https://d3fend.mitre.org/technique/D3-AM/  

## Definition
Access modeling captures and records the access permissions granted to identities (e.g., administrators, users, groups, systems) and optionally includes details on how these identities are stored, managed, and shared across systems.

## Parent Class(es)
- Operational Activity Mapping

## Relationships
- **kb-reference:** Reference - RFC 7642: System for Cross-domain Identity Management: Definitions, Overview, Concepts, and Requirements
- **maps:** Access Control Configuration
- **maps:** Digital Identity
- **maps:** User Account


---

# D3-APA: Access Policy Administration

**Synonym(s):** Access Control Administration  
**Reference:** https://d3fend.mitre.org/technique/D3-APA/  

## Definition
Access policy administration is the systematic process of defining, implementing, and managing access control policies that dictate user permissions to resources.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Isolate


---

# D3-AL: Account Locking

**Reference:** https://d3fend.mitre.org/technique/D3-AL/  

## Definition
The process of temporarily disabling user accounts on a system or domain.

## Parent Class(es)
- Credential Eviction

## Relationships
- **created:** 2020-08-05T00:00:00
- **disables:** User Account
- **kb-reference:** Reference - Account monitoring - Forescout Technologies
- **kb-reference:** Reference - Framework for notifying a directory service of authentication events processed outside the directory service - Oracle International Corp

## Knowledge Base Article
## How it works
Management servers with enterprise policies for account management provide the ability to enable and disable account for given rules. The rules may include specific periods of time (eg. weekend, plant shutdown, leave periods), specific user types or groups, or individual users.

## Considerations
* Local accounts caches vs centralized account management
* Single Sign-on
* Role based vs Attribute based systems

## Examples of account configuration stores
* Directory Services
* Active Directory
* RADIUS
* LDAP
* Oracle User Account Management
* JumpCloud


---

# D3-ACA: Active Certificate Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-ACA/  

## Definition
Actively collecting PKI certificates by connecting to the server and downloading its server certificates for analysis.

## Parent Class(es)
- Certificate Analysis

## Relationships
- **created:** 2020-08-05T00:00:00
- **kb-reference:** Reference - Securing Web Transactions

## Knowledge Base Article
## How it works
Analysis of server certificates using active methods to detect if certificates have been misconfigured or spoofed by using elements of the certificate, certificate authorities and signatures.

### Certificate validity analysis
This can be accomplished by verifying the digital signature on certificate.

### Certificate path analysis
The client's browser can perform path verification to ensure that the server's certificate contains a valid trust anchor.

### Certificate configuration analysis
Some browsers can be configured to implement the key-usage extensions contained certificates. This can help to prevent a certificate from being misused.

### Certificate revocation status analysis
Using either Certificate Revocation Lists (CRLs) or Online Certificate Status Protocol (OCSP) to determine the revocation status. OCSP Stapling, binding the status with the certificate, helps to mitigate potential delay in status verifications.

## Considerations
* Management of the PKI across the enterprise typically requires automation to maintain scalability and flexibility
* If the certificate authority, issuing the certificate, is compromised then all of the certificates issued by the CA are suspect
* There may be delays associated with updates to certificates
* Revoked certificates give the appearance of valid certificates until they are published to a trusted revocation service (OCSP or CRL)
* The revocation service (OCSP or CRL) may be down during our connection and a browser will need to make a decision will need to be made about trusting the connection


---

# D3-ALLM: Active Logical Link Mapping

**Reference:** https://d3fend.mitre.org/technique/D3-ALLM/  

## Definition
Active logical link mapping sends and receives network traffic as a means to map the whole data link layer, where the links represent logical data flows rather than physical connection

## Parent Class(es)
- Logical Link Mapping

## Relationships
- **kb-reference:** Reference - Identification of traceroute nodes and associated devices
- **kb-reference:** Reference - SNMP - Network Auto-Discovery
- **may-query:** Network Agent

## Knowledge Base Article
## How it works

Active logical link mapping establishes awareness of logical links in the network by sending data over the network to gather information about logical connections in the network.

Typically this will be achieved through network telemetry coordinated for network management and monitoring and will use a link layer discovery protocol such as LLDP and the information gathered and aggregated at higher levels using an application protocol such as SNMP.  The information may be polled by network management software or configured once and then pushed from network sensors (or agents.)

Another means of establishing network connectivity is by means of sending traffic through the use of a tool such as traceroute, to determine the logical paths through the network architecture.

## Considerations

* Best practice is to encrypt network monitoring data and require authentication for queries or admin/management functions.
* Push notifications reduce bandwidth necessary to capture and maintain information if reliable transport is used.
* Special consideration should be made before using of active scanning in OT networks and OT-safe options chosen where available.


---

# D3-APLM: Active Physical Link Mapping

**Synonym(s):** Active Physical Layer Mapping  
**Reference:** https://d3fend.mitre.org/technique/D3-APLM/  

## Definition
Active physical link mapping sends and receives network traffic as a means to map the physical layer.

## Parent Class(es)
- Physical Link Mapping

## Relationships
- **kb-reference:** Reference - Identification of traceroute nodes and associated devices
- **kb-reference:** Reference - Using spanning tree protocol (STP) to enhance layer-2 topology maps
- **may-query:** Network Agent


---

# D3-ANAA: Administrative Network Activity Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-ANAA/  

## Definition
Detection of unauthorized use of administrative network protocols by analyzing network activity against a baseline.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Intranet Administrative Network Traffic
- **created:** 2020-08-05T00:00:00
- **kb-reference:** Reference - Method and system for detecting suspicious administrative activity - Vectra Networks Inc
- **kb-reference:** Reference - CAR-2014-11-005: Remote Registry - MITRE
- **kb-reference:** Reference - CAR-2014-11-006: Windows Remote Management (WinRM) - MITRE

## Knowledge Base Article
## How it works
Network protocols such as RDP, IPMI, SSH, SNMP, VNC, MOSH, NX, TeamViewer, SPICE, PCoIP, and others are used by system administrators to remotely manage servers. Defenders monitor administrative network activity to determine if the use of remote protocols is malicious. Attackers can abuse administrative protocols and leverage them for initial access to various endpoints. For example, an attacker with valid credentials will remotely SSH or RDP into a server and attempt to blend in with existing traffic from system administrators. By monitoring the traffic activity, it is possible to detect when the protocols are behaving differently from a known baseline of system administration activity.

## Considerations
* Administrative traffic can be encrypted, making network protocol analysis a challenge
* False alarms can be mitigated by integration with inventory management systems


---

# D3-AA: Agent Authentication

**Reference:** https://d3fend.mitre.org/technique/D3-AA/  

## Definition
Agent authentication is the process of verifying the identities of agents to ensure they are authorized and trustworthy participants within a system.

## Parent Class(es)
- Defensive Technique

## Relationships
- **authenticates:** Agent
- **enables:** Harden
- **kb-reference:** Reference - NIST Special Publication 800-53 Revision 5 - Security and Privacy Controls for Information Systems and Organizations
- **strengthens:** User Account


---

# D3-ABPI: Application-based Process Isolation

**Synonym(s):** Browser-based Process Isolation, Remote Browser Isolation, Sandbox  
**Reference:** https://d3fend.mitre.org/technique/D3-ABPI/  

## Definition
Application code which prevents its own subroutines from accessing intra-process / internal memory space.

## Parent Class(es)
- Execution Isolation

## Relationships
- **isolates:** Process
- **kb-reference:** Reference - Private application access with browser isolation
- **kb-reference:** Reference - Protecting web applications from untrusted endpoints using remote browser isolation
- **kb-reference:** Reference - Site Isolation Design Document
- **restricts:** Subroutine

## Knowledge Base Article
## How it works
Some applications implement logic to permit or deny a particular subroutine access to other data within the same application process. This is intended to prevent critical application process data from being tampered with.

### Application-based Process Isolation in web browsers.

Isolation in browsers usually is designed with the following architectural mindset:
* Sandboxes and web resources should not be allowed to access each other because compromise of one should not effect the other.
* The principle of least-privilege should be followed when browsing.
The following aspects help make browser-based process isolation possible:
* Same Origin Policy
* Separate tabs and iframes use their own DOMs (cross-site document object models always run as a different process)
* CORS ensures cross-site data is not delivered to a process unless the server allows it
* Cookie and local data storage is separated by domain/site
* Separate execution environments (threads)

## Considerations
- Using isolation in browsers does mitigate and protect by default some types of attacks (e.g. renderer attacks and access to the filesystem) but it depends on correct configuration of CORS, use of valid/appropriate certificates.
-  Application-based Process Isolation may increase memory footprint.
-  Application-based Process Isolation may decrease application performance.


---

# D3-ACH: Application Configuration Hardening

**Reference:** https://d3fend.mitre.org/technique/D3-ACH/  

## Definition
Modifying an application's configuration to reduce its attack surface.

## Parent Class(es)
- Application Hardening

## Relationships
- **hardens:** Application Configuration
- **kb-reference:** Reference - Red Hat Enterprise Linux 8 Security Technical Implementation Guide
- **kb-reference:** Reference - Windows 10 STIG

## Knowledge Base Article
## How it works
Application configuration settings can be configured to limit the permissions on an application or disable certain vulnerable application features.

Hardening an application's configuration involves analyzing not only the application but also the environment in which the application is run in for potential vulnerabilities.


---

# D3-AEM: Application Exception Monitoring

**Synonym(s):** Application Failure Monitoring  
**Reference:** https://d3fend.mitre.org/technique/D3-AEM/  

## Definition
Monitoring the failures of system counters and timers.

## Parent Class(es)
- Application Performance Monitoring

## Relationships
- **kb-reference:** Reference - Secure PLC Coding Practices: Top 20 List
- **monitors:** Application Failure Count Variable
- **monitors:** Log

## Knowledge Base Article
## How it works
Monitoring timer and counter failures or exceedances can reveal issues with the program or platform, and is important for both safety and security. It may also help identify tampering or malicious activity affecting the device or the processes it controls.


---

# D3-AH: Application Hardening

**Synonym(s):** Process Hardening  
**Reference:** https://d3fend.mitre.org/technique/D3-AH/  

## Definition
Application Hardening makes an executable application more resilient to a class of exploits which either introduce new code or execute unwanted existing code. These techniques may be applied at compile-time or on an application binary.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Harden

## Knowledge Base Article
## Technique Overview

Exploits may, for example, rely on knowledge of addresses in a process's memory, they may alter memory contents, and they may cause a program to use instructions in a way that they were not intended.  By, for example, including code that dynamically changes the memory address of data or code on each run, introducing logic to validating the memory contents before certain potentially dangerous flows are executed, or monitoring a program for unusual sequence of instructions, this makes it harder for an attacker to craft a working exploit.


---

# D3-APM: Application Performance Monitoring

**Reference:** https://d3fend.mitre.org/technique/D3-APM/  

## Definition
Monitoring the count and duration of the application or program cycle.

## Parent Class(es)
- Platform Monitoring

## Relationships
- **kb-reference:** Reference - Secure PLC Coding Practices: Top 20 List
- **monitors:** Application Scan Time
- **monitors:** System Application Cycle Count

## Knowledge Base Article
## How it works
Keeping track of the controller cycle time by logging it, setting alarms, and correlating with other events. Changes to cycle time can be indicative of injecting new logic, deleting logic, or system failures.


---

# D3-APCA: Application Protocol Command Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-APCA/  

## Definition
Analyzing application protocol level remote commands to detect unauthorized activity.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **kb-reference:** Reference - Method and apparatus for detecting anomalies of an infrastructure in a network
- **kb-reference:** Reference - Protocol based detection of suspicious network traffic
- **monitors:** Network Traffic

## Knowledge Base Article
## How it works
This technique requires the ability to parse application layer protocols to understand the commands being sent to a remote service. Signature-based or statistical analysis may be employed to identify unauthorized commands being sent. These commands can be observed by monitoring network traffic or application logs.


---

# D3-AI: Asset Inventory

**Synonym(s):** Asset Discovery, Asset Inventorying  
**Reference:** https://d3fend.mitre.org/technique/D3-AI/  

## Definition
Asset inventorying identifies and records the organization's assets and enriches each inventory item with knowledge about their vulnerabilities.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Model


---

# D3-AVE: Asset Vulnerability Enumeration

**Reference:** https://d3fend.mitre.org/technique/D3-AVE/  

## Definition
Asset vulnerability enumeration enriches inventory items with knowledge identifying their vulnerabilities.

## Parent Class(es)
- Asset Inventory

## Relationships
- **evaluates:** Physical Artifact
- **evaluates:** Software
- **identifies:** Vulnerability
- **kb-reference:** Reference - Automated computer vulnerability resolution system
- **kb-reference:** Reference - Security vulnerability information aggregation
- **kb-reference:** Reference - System and method for vulnerability risk analysis


---

# D3-ANCI: Authentication Cache Invalidation

**Reference:** https://d3fend.mitre.org/technique/D3-ANCI/  

## Definition
Removing tokens or credentials from an authentication cache to prevent further user associated account accesses.

## Parent Class(es)
- Credential Eviction

## Relationships
- **deletes:** Credential
- **kb-reference:** Reference - Secure caching of server credentials - Dell Products LP
- **kb-reference:** Reference - System and method for providing an actively invalidated client-side network resource cache - IMVU

## Knowledge Base Article
## How it works
Applications can locally cache user authentication credentials for certain server connections. An application may attempt to use the cached credential for a connection. If the cached credentials exist then the user will not be typically prompted for new credentials.


## Considerations
Are these cached credentials only on the local host? Can they be persisted to the remote server?

## Examples
Windows Credential Management API


---

# D3-ANET: Authentication Event Thresholding

**Reference:** https://d3fend.mitre.org/technique/D3-ANET/  

## Definition
Collecting authentication events, creating a baseline user profile, and determining whether authentication events are consistent with the baseline profile.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **analyzes:** Authentication
- **created:** 2020-08-05T00:00:00
- **kb-reference:** Reference - Method and Apparatus for Network Fraud Detection and Remediation Through Analytics - Idaptive LLC
- **kb-reference:** Reference - CAR-2013-02-008: Simultaneous Logins on a Host - MITRE
- **kb-reference:** Reference - System, method, and computer program product for detecting and assessing security risks in a network - Exabeam Inc
- **kb-reference:** Reference - CAR-2013-02-012: User Logged in to Multiple Hosts - MITRE
- **kb-reference:** Reference - CAR-2013-10-001: User Login Activity Monitoring - MITRE

## Knowledge Base Article
## How it works
Authentication event data is collected (logon information such as device id, time of day, day of week, geo-location, etc.) to create an activity baseline. Then, a threshold is determined either through a manually specified configuration, or a statistical analysis of deviations in historical data. New authentication events are evaluated to determine if a threshold is exceeded. Thresholds can be static or dynamic.

### Actions
As a result of the analysis, actions taken could include:

* [Account Locking](/technique/d3f:AccountLocking)
* Raising an alert

### Example data sources
 * Directory server logs
 * VPN Server logs
 * IDAM Capability logs
 * NAC logs
 * Authentication client logs
 * Kerberos network traffic
 * LDAP network traffic

## Considerations

This technique covers statistical outliers. Though depending on the complexity or dimensionality of the data considered, outliers may not be obvious to a human analyst reviewing events in simplistic analytic views. If the malicious activity is not statistically different from benign activity, an alert threshold will not be met.


---

# D3-AZET: Authorization Event Thresholding

**Reference:** https://d3fend.mitre.org/technique/D3-AZET/  

## Definition
Collecting authorization events, creating a baseline user profile, and determining whether authorization events are consistent with the baseline profile.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **analyzes:** Authorization
- **created:** 2020-08-05T00:00:00
- **kb-reference:** Reference - Method and Apparatus for Network Fraud Detection and Remediation Through Analytics - Idaptive LLC
- **kb-reference:** Reference - CAR-2013-09-003: SMB Session Setups - MITRE
- **kb-reference:** Reference - System, method, and computer program product for detecting and assessing security risks in a network - Exabeam Inc
- **kb-reference:** Reference - CAR-2013-02-012: User Logged in to Multiple Hosts - MITRE

## Knowledge Base Article
## How it works

Authorization event data is collected to create a baseline user profile. Authorization events that deviate from the baseline and exceed a static or dynamic threshold are identified for further action. Authorization events can include successful and failed authorization attempts as well as events related to permissions including viewing, editing, deleting, creating files, databases etc.

## Considerations

Depending on the complexity of the data considered, outliers may not be obvious to a human analyst reviewing events in simplistic analytic views. If malicious activity is not statistically different from benign activity, an alert threshold will not be met.


---

# D3-BAN: Biometric Authentication

**Reference:** https://d3fend.mitre.org/technique/D3-BAN/  

## Definition
Using biological measures in order to authenticate a user.

## Parent Class(es)
- Agent Authentication

## Relationships
- **authenticates:** Person
- **kb-reference:** Reference - Tokenless biometric transaction authorization method and system
- **kb-reference:** Reference - http://www.biometric-solutions.com/keystroke-dynamics.html - biometric-solutions.com


---

# D3-BA: Bootloader Authentication

**Synonym(s):** Secure Boot  
**Reference:** https://d3fend.mitre.org/technique/D3-BA/  

## Definition
Cryptographically authenticating the bootloader software before system boot.

## Parent Class(es)
- Platform Hardening

## Relationships
- **authenticates:** Boot Loader
- **kb-reference:** Reference - UEFI Platform Initialization (PI) Specification


---

# D3-BDI: Broadcast Domain Isolation

**Synonym(s):** Network Segmentation  
**Reference:** https://d3fend.mitre.org/technique/D3-BDI/  

## Definition
Broadcast isolation restricts the number of computers a host can contact on their LAN.

## Parent Class(es)
- Network Isolation

## Relationships
- **filters:** Local Area Network Traffic
- **kb-reference:** Reference - Broadcast isolation and level 3 network switch - Hewlett Packard Enterprise Development LP
- **kb-reference:** Reference - Private virtual local area network isolation - Cisco Technology Inc

## Knowledge Base Article
## How it works
Software Defined Networking, or other network encapsulation technologies intercept host broadcast traffic then route it to a specified destination per a configured policy.

This can be implemented within hypervisors, networking hardware (WAPs, switches, routers), or virtual hardware.

## Considerations
This technique is highly dependent on network infrastructure and networking requirements.


---

# D3-BMA: Bus Message Authentication

**Reference:** https://d3fend.mitre.org/technique/D3-BMA/  

## Definition
Applies cryptographic primitives to individual bus frames to verify the sender's identity and ensure the integrity of the data payload.

## Parent Class(es)
- Message Authentication

## Relationships
- **authenticates:** Bus Message
- **kb-reference:** Reference - Controller area network message authentication - Ford Global Technologies LLC

## Knowledge Base Article
## How it works
Bus Message Authentication functions as a continuous validation layer that operates between the physical transmission of a signal and the application layer's processing of data. Every node on a bus network is provisioned with a cryptographic key and a synchronized 'freshness' state (such as a monotonic counter). When a node prepares to transmit, it generates a Message Authentication Code (MAC) which is created by hashing the message content, the sender's unique ID, and the current freshness value using its secret key. This MAC is then appended to the outgoing frame.

As messages circulate on the bus network, receiving nodes do not immediately trust the incoming data. Instead, a hardware controller intercepts the frame and performs a real-time parallel verification. The controller re-calculates the expected MAC based on its own copy of the key and the current network freshness state. If the received MAC matches the calculated one, the message is passed to the system for further action. If the MAC is missing, incorrect, or stale (indicating a replay of an older message), the hardware silently drops the frame or triggers a security alert.

## Considerations
* Bandwidth Overhead: Adding authentication tags (MACs) and freshness values reduces the effective data throughput; this requires a trade-off between the desired security level (tag length) and the available bus capacity.

* Real-Time Latency: Cryptographic processing must occur in hardware (e.g., via AES-NI, FPGA logic, or specialized ASICs) to meet the deterministic timing constraints of safety-critical systems.

* Key Management: A robust mechanism for secure key storage and lifecycle management (e.g., rotation and revocation) is required to ensure that a single compromised node does not jeopardize the entire network.

* Protocol Transparency: In legacy environments, authentication must often be implemented as a shim that remains compatible with existing protocol standards to avoid breaking legacy hardware.


---

# D3-BSE: Byte Sequence Emulation

**Synonym(s):** Shellcode Transmission Detection  
**Reference:** https://d3fend.mitre.org/technique/D3-BSE/  

## Definition
Analyzing sequences of bytes and determining if they likely represent malicious shellcode.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **kb-reference:** Reference - Network-Based Buffer Overflow Detection by Exploit Code Analysis - Information Security Research Centre
- **kb-reference:** Reference - Network-level polymorphic shellcode detection using emulation

## Knowledge Base Article
## How it works

Bytes are analyzed as if they are machine code instructions, and such instructions that are a common component of known shellcode are noted, such as stack pivots, reads from a Memory Address Table, and system calls for functions that disable protections or execute code.  For example, the x86 instruction `b0 0b: mov $11, %ax`, with no further alterations to the `%ax` register, followed by `cd 80: syscall` executes the system call `execve()` in the Linux kernel, which replaces the current process with another one specified -- this is a common action in shellcode, so this sequence would be flagged.

This technique detects shellcode despite whether or not it would cause a buffer overflow in the target binary.

If the sequence of bytes contains a sequence similar to that used in malicious shellcode, the entire byte sequence is flagged and a follow-on technique may be invoked.

## Considerations

### False Negatives
If the shellcode instructions are far apart, simple implementations might not detect the shellcode.

Due to the nature of assembly instructions not having a defined start or end, implementations which do not process all start sequences (for example, when they a find byte sequence of interest, continue scanning forwards from the end of it) might not detect the shellcode.

This technique might not detect more complex or obfuscated instructions.  For that purpose, Dynamic Analysis or Emulated File Analysis could assist by analyzing the actual instruction function.

This technique may not detect self-modifying code.  To make it harder for a process to modify itself, Process Segment Execution Prevention should be used, while noting its considerations.

This technique might not detect malicious shellcode which reuses instructions in the target binary for malicious effect, as memory references in the presumed assembly code are not dereferenced.  Dynamic Analysis and Emulated File Analysis, when set up properly to fork from the running target binary, might detect this.  Process Segment Execution Prevention combined with Segment Address Offset Randomization frequently makes introduction of shellcode through overwriting a saved return pointer more difficult.  Call stack depth analysis might detect excessive reuse of instructions in the target binary.  Shadow Stack Frames might detect that a stack frame's return address has changed and Stack Frame Canary Verification might detect that the stack frame's return address was overwritten.  Other heuristic methods might detect jump-oriented programming shellcode.

With inserting code directly, that it is not a buffer overflow, and just some place where code is executed either to a file or a write-what-where, the buffer overflow mitigations do not help.  Behavioral analysis could detect this, or proper access control could mitigate this.

### False Positives

Byte sequences containing code that is never used as machine code are still analyzed and flagged for anomalies, and [eventually](http://mathforum.org/library/drmath/view/55871.html), it is likely that an attack sequence will arise from the sheer volume of bytes transmitted.


---

# D3-CBAN: Certificate-based Authentication

**Reference:** https://d3fend.mitre.org/technique/D3-CBAN/  

## Definition
Requiring a digital certificate in order to authenticate a user.

## Parent Class(es)
- Agent Authentication

## Relationships
- **kb-reference:** Reference - Federal Public Key Infrastructure 101
- **reads:** Certificate

## Knowledge Base Article
## How it works

Certificate-based authentication is a security mechanism that uses digital certificates to verify the identity of a user, device, or server before granting access to a network or system. This method relies on a pair of cryptographic keys: a public key and a private key.

## Considerations

* Private Key Protection: Ensure that private keys are securely stored and protected against unauthorized access.
* Certificate Revocation: Implement a robust process for revoking certificates if they are compromised or no longer needed.
* Man-in-the Middle Attacks: Use mutual authentication to mitigate the risk of these attacks.


---

# D3-CA: Certificate Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-CA/  

## Definition
Analyzing Public Key Infrastructure certificates to detect if they have been misconfigured or spoofed using both network traffic, certificate fields and third-party logs.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Certificate File
- **kb-reference:** Reference - Securing Web Transactions

## Knowledge Base Article
## How it works
Certificate Analysis ensures that the data elements of the certificate are current and anchored in a known trust model. Certificate authorities, revocation lists, and third-party secure logs are used in the analysis. Analysis includes detection of server impersonation, phishing domains, and forged certificates.

TLS certificates are designed to expire to ensure that the cryptographic keys are forced to be changed on a regular basis. The certificates in the trust path also expire and can cause a break in the trust chain. This means that even if a server certificate is updated correctly, intermediate certificates can expire and the trust chain is not maintained. This can cause services to become unavailable.


---

# D3-CP: Certificate Pinning

**Reference:** https://d3fend.mitre.org/technique/D3-CP/  

## Definition
Persisting either a server's X.509 certificate or their public key and comparing that to server's presented identity to allow for greater client confidence in the remote server's identity for SSL connections.

## Parent Class(es)
- Credential Hardening

## Relationships
- **authenticates:** Public Key
- **hardens:** Certificate
- **kb-reference:** Reference - Certificate and Public Key Pinning
- **kb-reference:** Reference - End-to-end certificate pinning
- **kb-reference:** Reference - Public Key Pinning Extension for HTTP

## Knowledge Base Article
## How it works
Pinning allows for a trusted copy of a certificate or public key to be associated with a server and thus reducing the likelihood of frequently visited sites being subjected to man-in-the-middle attacks. Certificates or public keys can be pinned after a trusted connection has been established or the pinning can be preloaded in an application, which is the preferred method for mobile applications.

Pinning can take the form of certificate pinning or public key pinning.

## Forms of Pinning
* Certificate Pinning (CP) allows for the client to verify the X.509 certificate with a preloaded certificate. Typically, this is involves storing a hash of the certificate and using the stored hash for comparison to the hash of the certificate submitted during the SSL handshake.

* Public Key Pinning (PKP) requires the extraction of a public key from server's certificate. The stored public key is compared to the server's presented public key. A public key is expected to rotate less frequently than an X.509 certificate and is generally favored over certificate pinning.

An extension of PKP is Subject Public Key Information Pinning (SPKI) includes public key pinning plus additional information for SSL connections. The additional information can include preferred algorithms.

## Considerations

* With pinned certificates whenever a server updates its certificate, the pinned certificates will also need to be updated
* With pinned public keys the extracted key may be subject to key refresh policies but much less frequently
* Servers can become unavailable if pinned objects are set and not updated with the rotated identities. This may require a pinning strategy to be developed.
* The application of this technique within web browser applications has been [deprecated](https://developer.mozilla.org/en-US/docs/Web/HTTP/Public_Key_Pinning) by  popular web browser developers. They now favor certificate analysis via public certificate transparency logs, and the EXPECT-CT HTTP header.


---

# D3-CERO: Certificate Rotation

**Reference:** https://d3fend.mitre.org/technique/D3-CERO/  

## Definition
Certificate rotation involves replacing digital certificates and their private keys to maintain cryptographic integrity and trust, mitigating key compromise risks and ensuring continuous secure communications.

## Parent Class(es)
- Credential Rotation

## Relationships
- **kb-reference:** Reference - Password and Key Rotation - SSH
- **regenerates:** Certificate

## Knowledge Base Article
## How it works

Certificate rotation should be performed when:
- Any certificate expires.
- A new CA authority is substituted for the old, thus requiring a replacement root certificate.
- New or modified constraints need to be imposed on one or more certificates.
- A security breach has occurred.

Considerations:
- Managing certificate rotation across an enterprise can be complex. Automated solutions, sold by multiple vendors, should be considered to manage this complexity.


---

# D3-CDP: Change Default Password

**Reference:** https://d3fend.mitre.org/technique/D3-CDP/  

## Definition
Changing the default password means replacing the factory-set credentials with a strong, unique password before the device is deployed, preventing unauthorized access.

## Parent Class(es)
- Strong Password Policy

## Relationships
- **hardens:** OT Controller
- **kb-reference:** Reference - CISA CPG Checklist
- **kb-reference:** Reference - NIST SP 800-82R3 Guide to Operational Technology (OT) Security, Section 6.2.1.4.5 Password Authentication
- **kb-reference:** Reference - MITRE ATT&CK - Password Policies
- **strengthens:** Password
- **strengthens:** User Account

## Knowledge Base Article
## How it works
Change the default password as soon as a new device is received. The default credentials are normally documented in an instruction manual that is either packaged with the device, published online through official means, or published online through unofficial means.

## Considerations
* These should be changed before a device is brought online so that an adversary cannot take advantage of these default credentials.
* Strong and complex passwords are preferred if the technology allows.


---

# D3-CSPP: Client-server Payload Profiling

**Reference:** https://d3fend.mitre.org/technique/D3-CSPP/  

## Definition
Comparing client-server request and response payloads to a baseline profile to identify outliers.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Network Traffic
- **kb-reference:** Reference - Method and system for detecting malicious payloads - Vectra Networks Inc

## Knowledge Base Article
## How it works
Profiling request and response payloads across multiple clients to a single server to develop a baseline of their characteristics. May take into account request/response sizes, entropy, frequency, and rhythm. Finally, identify outliers as they may indicate a malicious payload delivery and subsequent server exploitation.


## Considerations
* Collecting metrics to establish a profile can be challenging since user behavior can change easily.
* Employees may work different hours or inconsistent schedules which will cause false positives.
* Collection of network activity to generate metrics is a computationally intensive process.
* Users may log into different workstations which may cause false positives.


---

# D3-CI: Configuration Inventory

**Reference:** https://d3fend.mitre.org/technique/D3-CI/  

## Definition
Configuration inventory identifies and records the configuration of software and hardware and their components throughout the organization.

## Parent Class(es)
- Asset Inventory

## Relationships
- **inventories:** Configuration Resource
- **kb-reference:** Reference - Web-Based Enterprise Management
- **kb-reference:** Reference - Windows Management Infrastructure (MI)
- **kb-reference:** Reference - Windows Management Instrumentation (WMI)

## Knowledge Base Article
## How it works

The organization retrieves configuration information through means of SNMP (MIB records), WBEM (CIM records), other protocols, or custom scripts and captures that information in a repository, typically known as a Configuration Management Database (CMDB)."


---

# D3-CHN: Connected Honeynet

**Reference:** https://d3fend.mitre.org/technique/D3-CHN/  

## Definition
A decoy service, system, or environment, that is connected to the enterprise network, and simulates or emulates certain functionality to the network, without exposing full access to a production system.

## Parent Class(es)
- Decoy Environment

## Relationships
- **kb-reference:** Reference - Modification of a Server to Mimic a Deception Mechanism - Acalvio Technologies Inc
- **spoofs:** Local Area Network

## Knowledge Base Article
## How it works
Decoy honeypots are deployed within the enterprise environment that emulate certain services or portions of an OS to attract attackers.

## Considerations
A connected honeynet provides a tradeoff between emulating certain functionality but not being as sophisticated as an integrated honeynet. The connected honeynet may not provide enough functionality to detect new attack patterns or zero day exploits but could provide enough functionality for specific known vulnerabilities.


---

# D3-CAA: Connection Attempt Analysis

**Synonym(s):** Network Scan Detection  
**Reference:** https://d3fend.mitre.org/technique/D3-CAA/  

## Definition
Analyzing failed connections in a network to detect unauthorized activity.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Intranet Network Traffic
- **kb-reference:** Reference - Detecting network reconnaissance by tracking intranet dark-net communications - VECTRA NETWORKS Inc

## Knowledge Base Article
## How it works
Connection Attempt Analysis in multiple ways.

### Monitoring traffic to unallocated IP space
One approach looks for failed connection attempts against unallocated IP space. First, network traffic is captured to map out the network to identify network assets as well as unallocated IP space. The map is then used to determine if connection attempts are being made to the unallocated IP space.

### Monitoring for sequentially transmitted traffic
Another approach passively inspects network traffic with application protocol analyzers observing network activity characteristics such as volume of packets sent/ received, TCP session attributes, and connection information between hosts (start time, source/destination host, services, etc.). Then using pattern matching to identify traffic which appears to be probing for network hosts.

## Considerations

* Implementations that rely on analysis of unallocated IP address space increase in their complexity with network size and decentralized network infrastructure.
* Inventory of unallocated IP space should be continuously updated to mitigate the risk of false positives.
* IPv6 also introduces challenges including IPv6 traffic bypassing IPv4 specific protection systems (ex. firewalls and IDS) and complexity in managing both IPv6 and IPv4 addresses.


---

# D3-CIA: Container Image Analysis

**Synonym(s):** Container Image Scanning  
**Reference:** https://d3fend.mitre.org/technique/D3-CIA/  

## Definition
Analyzing a Container Image with respect to a set of policies.

## Parent Class(es)
- Asset Vulnerability Enumeration

## Relationships
- **analyzes:** Container Image
- **kb-reference:** Reference - Container Image Analysis

## Knowledge Base Article
## How it works

Container images are standalone collections of the executable code and
content that are used to populate a container environment.
They are usually created by either building a container from scratch or by
building on top of an existing image pulled from a repository.

Throughout the container build workflow,
images should be scanned to identify:

- outdated libraries,
- known vulnerabilities,
- or misconfigurations, such as insecure ports or permissions.

Scanning should also provide the flexibility to disregard false positives
for vulnerability detection where knowledgeable
cybersecurity professionals have deemed alerts to be inaccurate.

One approach to implementing image scanning is to use an admission controller
to block deployments if the image does not comply with the organization's
security policies.

An admission controller is a Container Orchestration feature that can intercept and
process requests to the Container Orchestration API prior to persistence of the object,
but after the request is authenticated and authorized.
A webhook can be implemented to scan any image before it is deployed in the orchestrator.
This admission controller

## Considerations

* Image scanning is key to ensuring deployed containers are secure.
* Using trusted repositories to build containers is a critical part of the container build workflow.
* This technique does not necessarily prevent the build process to add insecure or unsecured
  files to the Image.


---

# D3-CNE: Content Excision

**Reference:** https://d3fend.mitre.org/technique/D3-CNE/  

## Definition
Removing specific, potentially malicious, parts of content

## Parent Class(es)
- Content Modification

## Relationships
- **kb-reference:** Reference - Method For Content Disarm and Reconstruction - OPSWAT Inc

## Knowledge Base Article
## How it works

If malicious or unnecessary elements is discovered within the content, or if a specific embedded portion does not comply with policy, it may be removed to ensure safety.


---

# D3-CF: Content Filtering

**Reference:** https://d3fend.mitre.org/technique/D3-CF/  

## Definition
Content Filtering techniques aid in the process of analyzing an input file for malicious or erroneous content and outputting a sanitized version.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Isolate
- **enforces:** Content Policy
- **filters:** File
- **kb-reference:** Reference - Method For Content Disarm and Reconstruction - OPSWAT Inc


---

# D3-CFC: Content Format Conversion

**Reference:** https://d3fend.mitre.org/technique/D3-CFC/  

## Definition
Content format conversion is mechanical transformation from one format to another which may be normalization or specifically flattening.

## Parent Class(es)
- Content Modification

## Relationships
- **kb-reference:** Reference - Method For Content Disarm and Reconstruction - OPSWAT Inc

## Knowledge Base Article
## How it works

This technique may enhance security by transforming files into safer or normalized formats.


---

# D3-CM: Content Modification

**Reference:** https://d3fend.mitre.org/technique/D3-CM/  

## Definition
Modify content that does not comply with policy.

## Parent Class(es)
- Content Filtering

## Relationships
- **filters:** Digital Media
- **filters:** File Content Block
- **filters:** File Metadata
- **kb-reference:** Reference - Method For Content Disarm and Reconstruction - OPSWAT Inc
- **modifies:** File

## Knowledge Base Article
## How it works

When content is found to not comply with it's content policy, it may be transformed to a safer state by modifying it.


---

# D3-CQ: Content Quarantine

**Reference:** https://d3fend.mitre.org/technique/D3-CQ/  

## Definition
Transfer content that does not comply with policy to a quarantine zone.

## Parent Class(es)
- Content Filtering

## Relationships
- **kb-reference:** Reference - Method For Content Disarm and Reconstruction - OPSWAT Inc
- **quarantines:** Database Record
- **quarantines:** File

## Knowledge Base Article
## How it works

Quarantining serves as a protective measure to isolate potentially harmful files or elements until they can be safely analyzed or processed.


---

# D3-CNR: Content Rebuild

**Synonym(s):** Content Reconstruction  
**Reference:** https://d3fend.mitre.org/technique/D3-CNR/  

## Definition
Rebuild the file according to the spec so any unreferenced components or objects are removed.

## Parent Class(es)
- Content Modification

## Relationships
- **kb-reference:** Reference - Method For Content Disarm and Reconstruction - OPSWAT Inc

## Knowledge Base Article
## How it works

If inputted content is divided up into components for further scrutiny, the components may be combined back afterwards in a safer state.


---

# D3-CNS: Content Substitution

**Reference:** https://d3fend.mitre.org/technique/D3-CNS/  

## Definition
Modifies specific digital content information by replacing it with something else.

## Parent Class(es)
- Content Modification

## Relationships
- **kb-reference:** Reference - Method For Content Disarm and Reconstruction - OPSWAT Inc

## Knowledge Base Article
## How it works

If malicious or unnecessary elements is discovered within the content, or if a specific embedded portion does not comply with policy, it may be replaced with alternatives to ensure safety.


---

# D3-CV: Content Validation

**Reference:** https://d3fend.mitre.org/technique/D3-CV/  

## Definition
Verify and validate contents complies with policy

## Parent Class(es)
- Content Filtering

## Relationships
- **kb-reference:** Reference - File Security Using File Format Validation - OPSWAT Inc

## Knowledge Base Article
## How it works

To ensure that content is safe, it's composition must be validated according to its content policy.


---

# D3-CFI: Control Flow Integrity

**Reference:** https://d3fend.mitre.org/technique/D3-CFI/  

## Definition
Enforcing legal control flow transfers during application process execution.

## Parent Class(es)
- Application Hardening

## Relationships
- **enforces:** Control Flow Policy
- **kb-reference:** Reference - Control Enforcement Technology (CET) - Intel Corporation
- **kb-reference:** Reference - Clang/LLVM - Control Flow Integrity (CFI)
- **kb-reference:** Reference - Control Flow Guard (CFG) - Microsoft
- **monitors:** Call Stack
- **monitors:** Shadow Stack
- **validates:** Control Flow Graph
- **validates:** Memory Address

## Knowledge Base Article
## How it works

Control flow integrity (CFI) restricts the destinations of control flow transfer instructions---particularly indirect function branches such as indirect function calls, jumps, and returns---such that execution can only proceed along paths determined to be valid at compile-time or load-time.

CFI is typically implemented by instrumenting a program during compilation or binary rewriting. A control flow graph is constructed that defines the legitimate targets for each indirect control flow transfer. At runtime, before an indirect branch is taken, a check is performed to ensure that the target address is a member of the allowed target set. If the check fails, a defensive response such as process termination or exception handling is triggered.

Implementations vary in granularity and enforcement mechanism:
- Compiler-based CFI inserts runtime checks that validate indirect call targets against type or signature-based constraints.
- Operating system–assisted CFI maintains a bitmap or table of valid indirect call targets and verifies them at runtime before allowing execution to continue.
- Hardware-assisted CFI enforces control flow integrity using architectural features such as shadow stacks and specific CPU instructions.

By preventing execution from jumping to attacker-controlled or unintended code locations, CFI mitigates a wide range of exploitation techniques, including return-oriented programming (ROP), jump-oriented programming (JOP), and function pointer overwrite attacks.

## Considerations

While control flow integrity significantly raises the bar for control flow hijacking attacks, several considerations affect its effectiveness:
- Granularity trade-offs: coarse-grained CFI allows larger target sets and may permit some unintended control flow paths, while fine-grained CFI offers stronger guarantees at the cost of performance and complexity.
- Performance overhead: runtime checks or hardware enforcement may introduce execution overhead, particularly in applications with frequent indirect branches.
- Compatibility limitations: some legacy code patterns, dynamic code generation, or just-in-time (JIT) compilation workflows may require special handling or reduced CFI enforcement.
- Data-only attacks: CFI does not prevent attacks that manipulate program behavior without altering control flow, such as logic corruption or data-oriented programming.
- Bypass techniques: if an attacker can redirect execution to a valid but unintended target within the allowed control flow graph, exploitation may still be possible.

CFI is most effective when combined with complementary defenses such as stack canaries, memory safety checks, address space layout randomization (ASLR), and hardware-backed memory protections.


---

# D3-CCSA: Credential Compromise Scope Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-CCSA/  

## Definition
Determining which credentials may have been compromised by analyzing the user logon history of a particular system.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **analyzes:** Credential
- **kb-reference:** Reference - CAR-2015-07-001: All Logins Since Last Boot - MITRE
- **kb-reference:** Reference - Systems and methods for detecting credential theft - Symantec Corp

## Knowledge Base Article
## How it works

#### Memory
Credentials may be stored in memory for a variety of reasons; on Windows, they may be stored in lsass.exe.  Once a credential dumper like mimikatz runs and dumps the memory of lsass.exe, the credentials of every account logged on since boot are potentially compromised.
When such an event occurs, this analytic will give the forensic context to identify compromised users. Those users could potentially be used in later events for additional logons.


#### Hard disk
Operating System may cache a certain number of credentials onto the hard disk to use as a source of truth if it cannot contact the credential server.  In many versions of Microsoft Windows, the 10 most recent are cached by default; this setting can be changed in the Microsoft Management Console's Local Security Policy: ```Computer Configuration -> Windows Settings -> Local Policy -> Security Options -> Interactive Logon: Number of previous logons to cache -> 0```  Here we are not concerned with the alteration of the credentials but the fact that they might be read.  If the attacker has physical access to the machine they are unlikely to be stopped from reading files on the filesystem.
"In the event that the domain controller is unavailable Windows will check the last password hashes that has been cached in order to authenticate the user with the system. These password hashes are cached in the following registry setting:
HKEY_LOCAL_MACHINE\SECURITY\Cache
Mimikatz can retrieve these hashes if the following command is executed:
lsadump::cache" [1]

The Registry Hive, HKEY_LOCAL_MACHINE\SAM, which is stored in the supporting files %systemroot%\System32\Config\{Sam,sam.log,sam.sav}, contains the SAM file.

DC: This is stored in %systemroot%\ntds\ntds.dit. (https://www.ultimatewindowssecurity.com/blog/default.aspx?d=10/2017)

Sometimes memory, which contains credentials, could get on the hard disk. Like with hiberfil.sys in Windows.  Equivalent on Linux


In Linux, an attacker could read the /etc/shadow file.

Reading from /proc directory: mimipenguin, many others.

## Considerations
Effective implementation requires identifying any location that could end up containing credentials, and detecting an method of potential access to a source of credential data.

1. https://medium.com/blue-team/preventing-mimikatz-attacks-ed283e7ebdd5


---

# D3-CE: Credential Eviction

**Reference:** https://d3fend.mitre.org/technique/D3-CE/  

## Definition
Credential Eviction techniques disable or remove compromised credentials from a computer network.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Evict
- **kb-reference:** Reference - Account monitoring - Forescout Technologies


---

# D3-CH: Credential Hardening

**Reference:** https://d3fend.mitre.org/technique/D3-CH/  

## Definition
Credential Hardening techniques modify system or network properties in order to protect system or network/domain credentials.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Harden
- **hardens:** Credential


---

# D3-CR: Credential Revocation

**Reference:** https://d3fend.mitre.org/technique/D3-CR/  

## Definition
Deleting a set of credentials permanently to prevent them from being used to authenticate.

## Parent Class(es)
- Credential Eviction

## Relationships
- **deletes:** Credential
- **kb-reference:** Reference - Revoke a previously issued verifiable credential - Microsoft

## Knowledge Base Article
## How it works

Management servers with enterprise policies for account management provide the ability remove permissions, accounts, or credentials. Compromised credentials should be revoked to prevent further malicious activity.


---

# D3-CRO: Credential Rotation

**Reference:** https://d3fend.mitre.org/technique/D3-CRO/  

## Definition
Credential rotation is a security procedure in which authentication credentials, such as passwords, API keys, or certificates, are regularly changed or replaced to minimize the risk of unauthorized access.

## Parent Class(es)
- Credential Hardening

## Relationships
- **kb-reference:** Reference - Eviction Guidance for Networks Affected by the SolarWinds and Active Directory/M365 Compromise - CISA
- **kb-reference:** Reference - Password and Key Rotation - SSH
- **regenerates:** Credential

## Knowledge Base Article
## How it works

Credentials can be systematically changed at predetermined intervals or based on specific events.  Credentials such as user passwords may be rotated manually, but it is increasingly common to use an automated system to manage rotation of enterprise passwords, certificates and keys.

## Considerations

- Rotation of credentials must be managed carefully to avoid inadvertent service interruption
- Management servers with enterprise policies for account management provide the ability to change or reset passwords for accounts. Some organizations rotate credentials periodically to limit the risk of stolen credentials.
- When responding to an incident, severity of compromise should be considered to determine what credentials to what accounts should be regenerated
- If proactively rotating credentials periodically, several factors should be considered to determine the frequency. Also introduces some risk including promoting the creation of weak passwords and poor storage practices for employees and presents challenges in proper tracking.


---

# D3-CS: Credential Scrubbing

**Reference:** https://d3fend.mitre.org/technique/D3-CS/  

## Definition
The systematic removal of hard-coded credentials from source code to prevent accidental exposure and unauthorized access.

## Parent Class(es)
- Source Code Hardening

## Relationships
- **hardens:** Subroutine
- **kb-reference:** Secrets Management Cheat Sheet

## Knowledge Base Article
## How it Works
Credential Scrubbing involves identifying and eliminating hard-coded credentials such as usernames, passwords, API keys, and tokens from source code repositories. These credentials should be managed securely using environment variables, secret management tools, or secure vaults where they can be safely accessed when needed.

## Considerations
* Developers should conduct regular audits of source code to ensure credentials are not hard-coded.
* Exposed credentials found in version control history must be disabled and replaced promptly.
* Adopt role-based access controls and credential rotation policies to minimize security risks.


---

# D3-CTS: Credential Transmission Scoping

**Synonym(s):** Phishing Resistant Authentication  
**Reference:** https://d3fend.mitre.org/technique/D3-CTS/  

## Definition
Limiting the transmission of a credential to a scoped set of relying parties.

## Parent Class(es)
- Access Mediation

## Relationships
- **isolates:** Credential
- **kb-reference:** Reference - Web Authentication: An API for accessing Public Key Credentials
Level 2


---

# D3-DNSAL: DNS Allowlisting

**Synonym(s):** DNS Whitelisting  
**Reference:** https://d3fend.mitre.org/technique/D3-DNSAL/  

## Definition
Permitting only approved domains and their subdomains to be resolved.

## Parent Class(es)
- Network Isolation

## Relationships
- **blocks:** Outbound Internet DNS Lookup Traffic
- **kb-reference:** Reference - DNS Whitelist (DNSWL) Email Authentication Method Extension


---

# D3-DNSCE: DNS Cache Eviction

**Synonym(s):** Flush DNS Cache  
**Reference:** https://d3fend.mitre.org/technique/D3-DNSCE/  

## Definition
Flushing DNS to clear any IP addresses or other DNS records from the cache.

## Parent Class(es)
- Object Eviction

## Relationships
- **deletes:** DNS Record
- **kb-reference:** Reference - Eviction Guidance for Networks Affected by the SolarWinds and Active Directory/M365 Compromise - CISA

## Knowledge Base Article
# How it works

Flushing the DNS Cache will clear the IP addresses of websites you have visited recently. This can help remediate DNS Cache Poisoning attacks, which is a type of cyber attack where corrupted DNS data is inserted into the cache, causing redirects to malicious websites.

On windows, the DNS cache can be wiped by issuing the command `ipconfig /flushdns`.


---

# D3-DNSDL: DNS Denylisting

**Synonym(s):** DNS Blacklisting  
**Reference:** https://d3fend.mitre.org/technique/D3-DNSDL/  

## Definition
Blocking DNS Network Traffic based on criteria such as IP address, domain name, or DNS query type.

## Parent Class(es)
- Network Isolation

## Relationships
- **blocks:** DNS Network Traffic
- **kb-reference:** Reference - Use DNS Policy for Applying Filters on DNS Queries

## Knowledge Base Article
## How it works
Rules are implemented that filter DNS queries using criteria such as:
- Client subnet
- Type of network protocol used in query
- Fully qualified domain name (FQDN) of record in the query
- DNS Server IP address that received the DNS request
- Type of DNS record being queried
- Time of day the query is received
- Size of the response

For example, a DNS policy can be created for blocking DNS queries for FQDNs that have been identified as unauthorized.

## Considerations
- Implementation considerations for DNS filtering policies to avoid over-blocking or under-blocking domains.
- Continuous maintenance of unauthorized domain lists is needed to keep up to date with possible site content changes.
- File sharing or content delivery networks may require other filtering techniques that are more fine-grained (URL blocking).
- Access to malicious websites or other network resources directly by IP instead of by DNS record, or after alteration of local DNS hosts file, may not result in DNS network traffic.


---

# D3-DNSTA: DNS Traffic Analysis

**Synonym(s):** Domain Name Analysis  
**Reference:** https://d3fend.mitre.org/technique/D3-DNSTA/  

## Definition
Analysis of domain name metadata, including name and DNS records, to determine whether the domain is likely to resolve to an undesirable host.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Outbound Internet DNS Lookup Traffic
- **kb-reference:** Reference - Domain age registration alert - Inc Rapid7 Inc RAPID7 Inc
- **kb-reference:** Reference - Heuristic botnet detection - Palo Alto Networks Inc
- **kb-reference:** Reference - Method and system for detecting algorithm-generated domains - VECTRA NETWORKS Inc
- **kb-reference:** Reference - Predicting Domain Generation Algorithms with Long Short-Term Memory Networks
- **kb-reference:** Reference - Sinkholing bad network domains by registering the bad network domains on the internet - Palo Alto Networks Inc
- **may-contain:** DNS Lookup

## Knowledge Base Article
## How it works
This technique can be accomplished in a number of ways.

* One example analytic determines whether or not a domain name was generated with an algorithm. Domain generation algorithms (DGAs) are sometimes used to create a domain name automatically  that will resolve to C2 infrastructure, without directly coding the domains in question into the malicious code.
* Another method analyzes information about domains that have been visited, including whether a domain name is longer than a common length,  if a dynamic DNS domain was visited, if a fast-flux domain was visited, and if a recently created domain was visited. These factors are used to develop a score and if that score is over a certain threshold, an alert is generated.
* Collected malware samples can be executed in a virtual environment to identify network domains that are connected to during execution. The network domains are then generated into signatures to identity bad domains for other hosts.

This technique does not check for content hosted at the domain.

## Considerations

* DNS produces a large amount of traffic which can be resource-intensive to analyze in real time.
* If a server is compromised, for example, as part of a watering hole attack, but the DNS information pointing to that server is not altered, this technique would not catch such an incident.


---

# D3-DEM: Data Exchange Mapping

**Synonym(s):** Data Flow Mapping, Information Exchange Mapping  
**Reference:** https://d3fend.mitre.org/technique/D3-DEM/  

## Definition
Data exchange mapping identifies and models the organization's intended design for the flows of the data types, formats, and volumes between systems at the application layer.

## Parent Class(es)
- System Mapping

## Relationships
- **kb-reference:** Reference - Catia UAF Plugin
- **kb-reference:** Reference - Tivoli Application Dependency Discovery Manager 7.3.0 - Dependencies between resources
- **kb-reference:** Reference - Unified Architecture Framework (UAF)
- **maps:** Data Dependency


---

# D3-DI: Data Inventory

**Synonym(s):** Data Discovery, Data Inventorying  
**Reference:** https://d3fend.mitre.org/technique/D3-DI/  

## Definition
Data inventorying identifies and records the schemas, formats, volumes, and locations of data stored and used on the organization's architecture.

## Parent Class(es)
- Asset Inventory

## Relationships
- **inventories:** Database
- **inventories:** Document File
- **kb-reference:** Reference - Data processing and scanning systems for generating and populating a data inventory


---

# D3-DQSA: Database Query String Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-DQSA/  

## Definition
Analyzing database queries to detect [SQL Injection](https://capec.mitre.org/data/definitions/66.html).

## Parent Class(es)
- Process Analysis

## Relationships
- **analyzes:** Database Query
- **kb-reference:** Reference - System and method for internet security - Cylance Inc

## Knowledge Base Article
## How it works

Some implementations use software hooks to intercept function calls related to database query operations. Other implementations might intercept or collect network traffic. The database query string is then extracted and analyzed with various methods, for example:
* Detecting specific administrative SQL commands
* Anomalous sequences of commands when compared to a statistical baseline.
* Anomalous commands for a given user role.

## Considerations

Some capabilities sanitize queries before permitting them to be transmitted to the database. This incurs risks such altering data in an undesired way or breaking application functionality.


---

# D3-DCE: Dead Code Elimination

**Reference:** https://d3fend.mitre.org/technique/D3-DCE/  

## Definition
Removing unreachable or "dead code" from compiled source code.

## Parent Class(es)
- Application Hardening

## Relationships
- **kb-reference:** Reference - Dead code elimination

## Knowledge Base Article
## How it works

Dead code is code that is considered unreachable by normal program execution. Dead code can be created by adding code under a condition that never evaluates to true. Dead code should be removed since this type of code can produce unexpected results, if accidentally or maliciously forced to execute.

Dead code identification is typically performed by algorithms that implement program flows analysis looking for unreachable code. The dead code is eliminated by instructing compilers to remove the code through compiler flags, i.e., '-fdce' is used for Dead Code Elimination.

## Considerations

Code can also be deemed unreachable for certain run-time conditions. Different deployed systems and environments may contain some code that is unreachable for the given environment. This technique does not consider run-time conditions for unreachable code.


---

# D3-DE: Decoy Environment

**Synonym(s):** Honeypot  
**Reference:** https://d3fend.mitre.org/technique/D3-DE/  

## Definition
A Decoy Environment comprises hosts and networks for the purposes of deceiving an attacker.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Deceive
- **manages:** Decoy Artifact

## Knowledge Base Article
## Technique Overview

Systems in a decoy environment are typically configured so that some detectable means of communication does not have any legitimate business purpose.  Any communication via these means should be logged and analyzed to find potential indicators of compromise for a possible past or future attack against other systems.


---

# D3-DF: Decoy File

**Reference:** https://d3fend.mitre.org/technique/D3-DF/  

## Definition
A file created for the purposes of deceiving an adversary.

## Parent Class(es)
- Decoy Object

## Relationships
- **kb-reference:** Reference - Open source intelligence deceptions - Illusive Networks Ltd
- **kb-reference:** Reference - Supply chain cyber-deception - Cymmetria, Inc.
- **kb-reference:** Reference - System and a method for identifying the presence of malware and ransomware using mini-traps set at network endpoints - Fidelis Cybersecurity Solutions Inc
- **kb-reference:** Reference - System and methods thereof for preventing ransomware from encrypting data elements stored in a memory of a computer-based system - Palo Alto Networks Inc
- **spoofs:** File

## Knowledge Base Article
## How it works
The decoy file is made available as a local or network resource. Accesses to the file may be monitored. The files may be configurations, documents, executables, or other file types.


## Considerations
Properties of the file such as cryptographic checksums, file creation date, file modified date, file size, file owner etc may be modified to improve the credibility of the file.

## Example
* A CSV file with decoy user credentials is placed on a system. The system or network is then monitored to detect any accesses to the decoy files.


---

# D3-DNR: Decoy Network Resource

**Reference:** https://d3fend.mitre.org/technique/D3-DNR/  

## Definition
Deploying a network resource for the purposes of deceiving an adversary.

## Parent Class(es)
- Decoy Object

## Relationships
- **kb-reference:** Reference - Automatically generating network resource groups and assigning customized decoy policies thereto - Illusive Networks Ltd
- **kb-reference:** Reference - Deception-Based Responses to Security Attacks - Crowdstrike Inc
- **kb-reference:** Reference - Dynamic selection and generation of a virtual clone for detonation of suspicious content within a honey network - Palo Alto Networks Inc
- **kb-reference:** Reference - System and method for identifying the presence of malware using mini-traps set at network endpoints - Fidelis Cybersecurity Solutions Inc
- **spoofs:** Network Resource

## Knowledge Base Article
## How it works
Decoy network resources are deployed to web application servers, network file shares, or other network based sharing services.

A "honeypot" may serve a variety of decoy network resources.

## Considerations

* Developing a deployment and placement strategy for the decoy network resource.
* Personnel responsible for creation of decoy networks should consider the potential for resource exhaustion through denial of service attacks.

## Examples
* Honeypots are typically used to mimic a known system with fake vulnerabilities. This may attract attackers to the honeypot.
* Decoy accounts are also used to scan for attempted logins. The decoy accounts can provide security analysts with the attacker's potential intents and strategies.
* Tarpits are used to monitor unallocated IP space for unauthorized network activity.


---

# D3-DO: Decoy Object

**Synonym(s):** Lure  
**Reference:** https://d3fend.mitre.org/technique/D3-DO/  

## Definition
A Decoy Object is created and deployed for the purposes of deceiving attackers.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Deceive

## Knowledge Base Article
## Technique Overview
Decoy objects are typically configured with detectable means of communication but do not have any legitimate business purpose. Any communication via or to these objects should be logged and analyzed to find potential indicators of compromise for a possible past or future attack against other systems.


---

# D3-DP: Decoy Persona

**Reference:** https://d3fend.mitre.org/technique/D3-DP/  

## Definition
Establishing a fake online identity to misdirect, deceive, and or interact with adversaries.

## Parent Class(es)
- Decoy Object

## Relationships
- **kb-reference:** Reference - Decoy and deceptive data object technology - Cymmetria, Inc.
- **kb-reference:** Reference - Decoy Personas for Safeguarding Online Identity Using Deception - MITRE
- **spoofs:** User

## Knowledge Base Article
## How it works
A false online identity is created for the purposes of interacting with adversaries in a direct or indirect manner. This includes the associated email addresses, social media accounts, and other online communication profiles.

## Considerations
* Include phone numbers and online social profiles as well as automatically or manually responding to contact made to the persona to improve realism.
* Continuous updating and managing the decoy personas and online activity streams to ensure personas do not become stale and outdated.


---

# D3-DPR: Decoy Public Release

**Reference:** https://d3fend.mitre.org/technique/D3-DPR/  

## Definition
Issuing publicly released media to deceive adversaries.

## Parent Class(es)
- Decoy Object

## Relationships
- **kb-reference:** Reference - Mock attack cybersecurity training system and methods - WOMBAT SECURITY TECHNOLOGIES Inc

## Knowledge Base Article
## How it works
Publicly released media includes press release, videos, or other marketing collateral. The media may include URLs, points of contact, or other identifiers to entice interaction from adversaries.

## Considerations
* Information used in decoy public released media must contain enough realism to deceive and provide interaction from adversaries.
* Continuous development, creation, and distribution of media and identifiers are needed to ensure adversary interaction continues over time.
* Decoy public releases could be placed on platforms with different degrees of ownership, including entirely enterprise-owned infrastructure, IaaS, and SaaS (including social applications). Platforms that are not entirely enterprise-owned may be more likely to gather information


---

# D3-DST: Decoy Session Token

**Reference:** https://d3fend.mitre.org/technique/D3-DST/  

## Definition
An authentication token created for the purposes of deceiving an adversary.

## Parent Class(es)
- Decoy Object

## Relationships
- **kb-reference:** Reference - Decoy and deceptive data object technology - Cymmetria Inc
- **spoofs:** Session Token

## Knowledge Base Article
## How it works
Usage of decoy session tokens may be monitored to track attacker behavior or otherwise control the beliefs of the attacker.

## Considerations
* Interaction and activity with the decoy session token must be constantly monitored and analyzed to detect unauthorized activity.
* Session tokens are typically short-lived and therefore the decoy must be continuously updated to provide the appearance of it being used in the production environment.
* Automated tools can assist with maintenance and updates by automatically adjusting the decoy session token and environment to mimic the production environment.


---

# D3-DUC: Decoy User Credential

**Reference:** https://d3fend.mitre.org/technique/D3-DUC/  

## Definition
A Credential created for the purpose of deceiving an adversary.

## Parent Class(es)
- Decoy Object

## Relationships
- **kb-reference:** Reference - Decoy and deceptive data object technology - Cymmetria Inc
- **kb-reference:** Reference - Decoy Network-Based Service for Deceiving Attackers - Amazon Technologies
- **kb-reference:** Reference - System and method for identifying the presence of malware using mini-traps set at network endpoints - Fidelis Cybersecurity Solutions Inc
- **spoofs:** Credential

## Knowledge Base Article
## How it works
A detection analytic is developed to determine when a user uses decoy credentials. Subsequent actions by that user may be monitored or controlled by the defender.

A credential may be:
 * Domain username and password
 * Local system username and password

## Considerations
* Decoy credentials should be integrated with a larger decoy environment to ensure that when decoy credentials are compromised, the credentials are used to interact with a decoy asset that is being monitored.
* Continuous maintenance and updates are needed to ensure the legitimacy of the larger decoy environment and specifically the assets that utilize the decoy credentials.


---

# D3-DPLM: Direct Physical Link Mapping

**Synonym(s):** Manual Physical Link Mapping  
**Reference:** https://d3fend.mitre.org/technique/D3-DPLM/  

## Definition
Direct physical link mapping creates a physical link map by direct observation and recording of the physical network links.

## Parent Class(es)
- Physical Link Mapping

## Relationships
- **kb-reference:** Reference - Network Mapping

## Knowledge Base Article
## How it works

Direct Physical Link Mapping involves a manual process where a network engineer or administrator physically observes and documents the physical connections within the network infrastructure.

## Considerations

* Constructing and maintaining physical topologies for extensive networks can be challenging and time-consuming using manual methods. Therefore, where feasible, automated methods like active physical link mapping should be considered as a partial or complete solution for physical link mapping processes.

* In scenarios where active physical link mapping is not an option, physical inspection of networks is necessary to accomplish physical link mapping. This is due to the lack of reliable techniques to accurately map physical links solely through passive network traffic monitoring.


---

# D3-DNL: Directional Network Link

**Reference:** https://d3fend.mitre.org/technique/D3-DNL/  

## Definition
Enforce one-way network communication by preventing two-way communication.

## Parent Class(es)
- Network Isolation

## Relationships
- **kb-reference:** Reference - Secure one-way data transfer using communication interface circuitry
- **restricts:** Physical Link
- **uses:** Physical Data Diode

## Knowledge Base Article
## How it works
Using a device such as a data diode, or otherwise enforcing unidirectional (one-way) network communication / data transfer, to physically prevent signals from traveling in the reverse direction.

Unidirectional network link enforcement is a security measure used to separate control and safety systems in operational technology (OT) environments. By employing physical data diodes, this approach ensures one-way communication, allowing information from safety systems to be viewed without permitting any modification or interference, thereby protecting the integrity of the safety system.


---

# D3-DRA: Disable Remote Access

**Reference:** https://d3fend.mitre.org/technique/D3-DRA/  

## Definition
Limiting access to a computing device which is not required through or from a non-organization-controlled network.

## Parent Class(es)
- Application Configuration Hardening

## Relationships
- **configures:** Application Configuration

## Knowledge Base Article
## How It Works
There are several different methods of achieving remote access restriction. This could include: time-based controls, just-in-time authorization, and deny-by-default controls.

This can be done on a Windows machine by unchecking an "allow remote assistance" or checking the "don't allow remote connections" boxes; creating firewall rules to block remote access protocols; uninstalling remote access software; disabling Wi-Fi, Ethernet, Bluetooth, or other connection methods enabling remote access.

One way to achieve remote access restrictions in OT is by programming logic in the OT Controller to give the Operator authorizing abilities which ensures local control is maintained. In this situation, a remote access modem would be powered on/off using a discrete output from an I/O module of the OT controller.


---

# D3-DENCR: Disk Encryption

**Reference:** https://d3fend.mitre.org/technique/D3-DENCR/  

## Definition
Encrypting a hard disk partition to prevent cleartext access to a file system.

## Parent Class(es)
- Platform Hardening

## Relationships
- **encrypts:** Storage
- **kb-reference:** Reference - LUKS1 On-Disk Format SpecificationVersion 1.2.3


---

# D3-DKE: Disk Erasure

**Reference:** https://d3fend.mitre.org/technique/D3-DKE/  

## Definition
Disk Erasure is the process of securely deleting all data on a disk to ensure that it cannot be recovered by any means.

## Parent Class(es)
- Disk Formatting

## Relationships
- **erases:** Secondary Storage
- **kb-reference:** Reference - Remembrance of data passed: A study of disk sanitization practices

## Knowledge Base Article
### How it works

Disk Erasure involves overwriting the existing data with random or specific patterns multiple times. Disk erasure is crucial for data sanitization, ensuring that sensitive information is completely removed from storage devices before they are repurposed, disposed of, or transferred to another party.


---

# D3-DKF: Disk Formatting

**Reference:** https://d3fend.mitre.org/technique/D3-DKF/  

## Definition
Disk Formatting is the process of preparing a data storage device, such as a hard drive, solid-state drive, or USB flash drive, for initial use.

## Parent Class(es)
- Object Eviction

## Relationships
- **kb-reference:** Reference - Remembrance of data passed: A study of disk sanitization practices
- **modifies:** Secondary Storage

## Knowledge Base Article
### How it works

This process involves setting up an empty file system on the disk, which includes creating a directory structure and initializing metadata structures. In cybersecurity, disk formatting can be used to remove all existing data on a disk, making it a clean slate for new data storage or to prevent unauthorized access to previously stored data.


---

# D3-DKP: Disk Partitioning

**Reference:** https://d3fend.mitre.org/technique/D3-DKP/  

## Definition
Disk Partitioning is the process of dividing a disk into multiple distinct sections, known as partitions.

## Parent Class(es)
- Disk Formatting

## Relationships
- **creates:** Partition Table
- **kb-reference:** Reference - Remembrance of data passed: A study of disk sanitization practices

## Knowledge Base Article
### How it works

Each partition can be managed separately and can have its own file system. Disk partitioning can be used to segregate sensitive data from less critical data, improve system performance, and enhance data management and recovery processes. It can also help in isolating different operating systems or environments on the same physical disk.


---

# D3-DAM: Domain Account Monitoring

**Reference:** https://d3fend.mitre.org/technique/D3-DAM/  

## Definition
Monitoring the existence of or changes to Domain User Accounts.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **kb-reference:** Reference - Audit User Account Management
- **monitors:** Domain User Account


---

# D3-DLV: Domain Logic Validation

**Reference:** https://d3fend.mitre.org/technique/D3-DLV/  

## Definition
Validation of variable state in the context of the domain application.

## Parent Class(es)
- Source Code Hardening

## Relationships
- **kb-reference:** Reference - Secure PLC Coding Practices: Top 20 List
- **validates:** Subroutine

## Knowledge Base Article
## How it works
Validates the type, value, and/or range of an variable taking into context the current application in the business domain.


---

# D3-DNRA: Domain Name Reputation Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-DNRA/  

## Definition
Analyzing the reputation of a domain name.

## Parent Class(es)
- Identifier Reputation Analysis

## Relationships
- **analyzes:** Domain Name
- **kb-reference:** Reference - Database for receiving, storing and compiling information about email messages
- **kb-reference:** Reference - Finding phishing sites


---

# D3-DRT: Domain Registration Takedown

**Reference:** https://d3fend.mitre.org/technique/D3-DRT/  

## Definition
The process of performing a takedown of the attacker's domain registration infrastructure.

## Parent Class(es)
- Object Eviction

## Relationships
- **deletes:** Domain Registration
- **kb-reference:** Reference - Understanding the Domain Registration Behavior of Spammers

## Knowledge Base Article
## How it works

Most nameserver hosts and domain name registrars comply with internationally recognised standards and supply their services based on terms and conditions that provide users and organisations protection from abuse and trademark infringement. Performing a WHOIS query on the attacker's domain will provide a contact that can be notified in the case of abuse. Formal takedown processes should be initiated to suspend or disable the normal function of the domain name.

## Considerations

- Takedown notifications should clearly demonstrate (with evidence) that the nameserver or registrars Terms and Conditions have been breached.
- Takedown processes are notoriously slow and sometimes unsuccessful.
- Many government organisations will have takedown processes that should also be followed. They may use this for intelligence to assist other organisations suffering an attack.
- Top level domain registrars will have takedown processes that can be followed, as an escalation path, when the nameserver host and/or registrar have not responded or complied timeously or inline with the TLD expectations.

## Examples of Domain Registration Abuse

Attackers will create infrastructure from which to carry out their operations and this may include registering domain names to be used in the various attacks. Known misuse cases include:

- Registering domain names that are similar to the victim's. This is known as typosquatting or URL hijacking. Legitimate looking mails or URLs could be sent using this domain in phishing campaigns.
- Registering domain names that are used in C2 beacons.


---

# D3-DTP: Domain Trust Policy

**Reference:** https://d3fend.mitre.org/technique/D3-DTP/  

## Definition
Restricting inter-domain trust by modifying domain configuration.

## Parent Class(es)
- Access Policy Administration

## Relationships
- **kb-reference:** Reference - How trust relationships work for resource forests in Azure Active Directory Domain Services
- **restricts:** Directory Service
- **restricts:** Domain Account


---

# D3-DLIC: Driver Load Integrity Checking

**Reference:** https://d3fend.mitre.org/technique/D3-DLIC/  

## Definition
Ensuring the integrity of drivers loaded during initialization of the operating system.

## Parent Class(es)
- Platform Hardening

## Relationships
- **authenticates:** Hardware Driver
- **kb-reference:** Reference - Integrity assurance through early loading in the boot phase - Crowdstrike Inc
- **kb-reference:** Reference - Protected computing environment - Microsoft Technology Licensing LLC

## Knowledge Base Article
## How it works
This technique can be accomplished in a number of ways:

* A kernel level security agent installed on a host machine ensures that the driver associated with the agent is first in the initialization order. A dependent DLL associated with the driver is configured to be processed before other dependent DLLs and executes a number of operations to ensure the driver associated with the security agent is initialized first.

* Kernel components can be signed by a certificate obtained by a third party to verify the source of the component and whether it has been modified. When signed, the component will include a signature block implemented as a hash value of the component header and can also include a certificate chain. The signature and certificate data are typically added before the kernel component is distributed to the public.


## Considerations

* The private keys to sign certificates as reputable companies have been stolen in the past -- in cases such as where certificates from Adobe, Realtek, and JMicron have been used to sign malicious executables. (Source: https://resources.infosecinstitute.com/cybercrime-exploits-digital-certificates/#gref)

* Trusted Root Certificate Authorities have been compromised, yielding the ability to use the compromised keys to generate certificates with an arbitrary company name.

* It may not be difficult for an attacker to start an organization which can obtain a signed certificate.

* A root certificate authority (CA) whose certificate is trusted in the verification logic could generate incorrect certificates, if they are lax or have ulterior motives.


---

# D3-DA: Dynamic Analysis

**Synonym(s):** Malware Detonation, Malware Sandbox  
**Reference:** https://d3fend.mitre.org/technique/D3-DA/  

## Definition
Executing or opening a file in a synthetic "sandbox" environment to determine if the file is a malicious program or if the file exploits another program such as a document reader.

## Parent Class(es)
- File Analysis

## Relationships
- **analyzes:** Document File
- **analyzes:** Executable File
- **kb-reference:** Reference - Malware analysis system - Palo Alto Networks Inc
- **kb-reference:** Reference - Use of an application controller to monitor and control software file and application environments - Sophos Ltd

## Knowledge Base Article
## How it works
Analyzing the interaction of a piece of code with a system while the code is being executed in a controlled environment such as a sandbox, virtual machine, or simulator. This exposes the natural behavior of the piece of code without requiring the code to be disassembled.

## Considerations
 * Malware often detects a fake environment, then changes its behavior accordingly. For example, it could detect that the system clock is being sped up in an effort to get it to execute commands that it would normally only execute at a later time, or that the hardware manufacturer of the machine is a virtualization provider.
 * Malware can attempt to determine if it is being debugged, and change its behavior accordingly.
 * For maximum fidelity, the simulated and real environments should be as similar as possible because the malware could perform differently in different environments.
 * Sometimes the malware behavior is triggered only under certain conditions (on a specific system date, after a certain time, or after it is sent a specific command) and can't be detected through a short execution in a virtual environment.

## Implementations
* Cuckoo Sandbox


---

# D3-EMH: Electromagnetic Radiation Hardening

**Synonym(s):** EM Hardening  
**Reference:** https://d3fend.mitre.org/technique/D3-EMH/  

## Definition
The application of physical and material-level design measures to electronic systems, components, or facilities to reduce their susceptibility to damage or disruption from electromagnetic threats.

## Parent Class(es)
- Radiation Hardening

## Relationships
- **kb-reference:** Reference - System and method for providing certifiable electromagnetic pulse and rfi protection through mass-produced shielded containers and rooms - Instant Access Networks LLC

## Knowledge Base Article
## How it works
EM hardening operates on the principle of controlling the coupling path between an electromagnetic threat and the sensitive electronics it could affect. At the most fundamental level, this involves creating barriers that reflect, absorb, or redirect unwanted electromagnetic energy before it can induce damaging or disruptive currents in protected circuitry. The physical mechanisms exploited include the Faraday cage effect (conductive enclosures that attenuate external fields), skin-depth shielding (where conductive materials dissipate high-frequency fields before they penetrate), and transient suppression components (such as surge protectors and ferrite chokes) that clamp induced voltages at I/O interfaces.

For threats at higher energy levels or involving ionizing radiation, such as nuclear EMP (NEMP) or space radiation, hardening extends beyond shielding to encompass radiation-tolerant component selection, redundant circuit architectures, and layout practices that minimize antenna-like structures susceptible to field coupling. The approach is inherently defense-in-depth: no single measure provides complete protection, so hardened systems typically layer multiple techniques across the facility, chassis, board, and component levels.

## Considerations
* Threat scope must be defined early: design choices differ significantly between defending against ambient RFI, conducted EMI on power lines, intentional jamming, HEMP (High-Altitude EMP), or ionizing radiation in space or nuclear environments.
* Hardening can conflict with thermal management: fully sealed enclosures that maximize shielding often restrict airflow, requiring careful thermal design trade-offs.
* Testing and certification are mandatory for assurance: claimed shielding effectiveness must be validated through standardized testing (e.g., IEEE 299, MIL-STD-461) rather than inferred from design alone.
* Maintenance can degrade hardening: field modifications, connector re-terminations, or enclosure repairs can inadvertently introduce shielding gaps, necessitating re-verification procedures.


---

# D3-ELM: Electronic Lock Monitoring

**Synonym(s):** Door Lock Monitoring, Lock State Monitoring  
**Reference:** https://d3fend.mitre.org/technique/D3-ELM/  

## Definition
Monitoring electronic lock and door hardware states and access events (e.g., locked/unlocked, access granted/denied, door forced/held, tamper) to detect and respond to unauthorized entry.

## Parent Class(es)
- Physical Access Monitoring

## Relationships
- **kb-reference:** Reference - FIPS 201-3
- **kb-reference:** Reference - NIST SP 800-116 Rev. 1
- **kb-reference:** Reference - NIST Special Publication 800-53 Revision 5 - Security and Privacy Controls for Information Systems and Organizations
- **kb-reference:** Reference - SIA OSDP v2.2
- **monitors:** Electronic Combination Lock

## Knowledge Base Article
## How it works

Electronic lock monitoring collects status and events from door controllers, readers (badge/PIV, keypad), and door hardware (door position switch, request-to-exit, bolt/latch, tamper). The physical access control system (PACS) logs access decisions, correlates door-held/forced conditions, and generates alarms for response. Secure, supervised reader links, such as Open Supervised Device Protocol (OSDP), help detect wiring faults and reduce credential interception. Integration with video systems can pop relevant camera views on lock-related alarms.

## Considerations

* Use encrypted, supervised reader-to-controller protocols to protect credentials and detect wiring faults.
* Harden door controllers and isolate the PACS network to limit the attack surface.
* Configure fail-safe or fail-secure behavior and emergency release to meet life-safety requirements.
* Tune alarms for door-held, door-forced, and invalid retries to reduce noise while catching misuse.
* Supervise inputs, provide backup power, and regularly test door, bolt, and tamper sensors to ensure reliability.


---

# D3-EF: Email Filtering

**Reference:** https://d3fend.mitre.org/technique/D3-EF/  

## Definition
Filtering incoming email traffic based on specific criteria.

## Parent Class(es)
- Inbound Traffic Filtering

## Relationships
- **filters:** Email
- **kb-reference:** Reference - System and method for providing anonymous remailing and filtering of electronic mail - Nokia

## Knowledge Base Article
## How it works

Mail filters can be implemented to scan inbound email messages at the initial SMTP connection stage to detect and reject email containing spam and malware.

This technique is distinct from d3f:EmailDeletion because it prevents an email from reaching an user's inbox. This technique can also be used for outbound email traffic.

## Considerations
* The effectiveness of mail filters depend on the completeness of the filter policies


---

# D3-ER: Email Removal

**Synonym(s):** Email Deletion  
**Reference:** https://d3fend.mitre.org/technique/D3-ER/  

## Definition
The email removal technique deletes email files from system storage.

## Parent Class(es)
- File Eviction

## Relationships
- **deletes:** Email
- **kb-reference:** Reference - System and method for scanning remote services to locate stored objects with malware
- **may-access:** Mail Server

## Knowledge Base Article
## How it works

Email removal is a technique that can be used to prevent a user from executing malware or responding to phishing attempts. Security software or users themselves may detect malicious or suspicious email in a local or remote mail folder email and then employ this technique.

## Considerations

For email that needs to be removed, an infosec organization may choose to take additional follow-up actions (such as blocking the sources or notifying providers), rather than only relying on email deletion.

For the case where users detect likely suspicious email files, the organization should consider implementing a means for reporting these emails to their infosec organization.

Email files may propagate through many storage systems across an organization's systems over time, so early detection and blocking helps avoid residual, latent stores of malicious email content in the enterprise.


---

# D3-EFA: Emulated File Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-EFA/  

## Definition
Emulating instructions in a file looking for specific patterns.

## Parent Class(es)
- File Analysis

## Relationships
- **analyzes:** Document File
- **analyzes:** Executable File
- **kb-reference:** Reference - Network-level polymorphic shellcode detection using emulation


---

# D3-ET: Encrypted Tunnels

**Reference:** https://d3fend.mitre.org/technique/D3-ET/  

## Definition
Encrypted encapsulation of routable network traffic.

## Parent Class(es)
- Network Isolation

## Relationships
- **isolates:** Intranet Network
- **kb-reference:** Reference - Security Architecture for the Internet Protocol


---

# D3-EBWSAM: Endpoint-based Web Server Access Mediation

**Reference:** https://d3fend.mitre.org/technique/D3-EBWSAM/  

## Definition
Endpoint-based web server access mediation regulates web server access directly from user endpoints by implementing mechanisms such as client-side certificates and endpoint security software to authenticate devices and ensure compliant access.

## Parent Class(es)
- Web Session Access Mediation

## Relationships
- **kb-reference:** Reference - Special Publication 800-41 Revision 1 Guidelines on Firewalls and Firewall Policy

## Knowledge Base Article
## How it works

Endpoint-based Web Server Access Mediation focuses on managing access to web servers directly from user devices. This involves implementing security measures like client certificates or endpoint security software to ensure that only authorized devices can initiate sessions with web servers. Examples include direct access to internal web applications from company laptops.


---

# D3-EHB: Endpoint Health Beacon

**Synonym(s):** Endpoint Health Telemetry  
**Reference:** https://d3fend.mitre.org/technique/D3-EHB/  

## Definition
Monitoring the security status of an endpoint by sending periodic messages with health status, where absence of a response may indicate that the endpoint has been compromised.

## Parent Class(es)
- Operating System Monitoring

## Relationships
- **kb-reference:** Reference - Intrusion detection using a heartbeat - Sophos Ltd
- **monitors:** Network Node

## Knowledge Base Article
## How it works
Endpoints are configured to periodically generate and transmit a secure heartbeat that is delivered on a configured schedule and provides endpoint status information. Status information can include software details (version, configuration, etc), endpoint identification (MAC, IP address, machine ID) or other hardware/software configuration information. Interruption of the heartbeat can signal that the endpoint has been compromised.

## Considerations
* Security of heartbeat messages to ensure message integrity
* Disappearance of the heartbeat could simply mean that the endpoint is powered off or intentionally disconnected from the network. Therefore other criteria may need to be used to accurately detect endpoint compromise.
* Attacker presence on the machine may leave the heartbeat intact.
* An attacker may determine the format of the heartbeat and continue to send it even after the machine is compromised.


---

# D3-EHPV: Exception Handler Pointer Validation

**Synonym(s):** Exception Handler Validation  
**Reference:** https://d3fend.mitre.org/technique/D3-EHPV/  

## Definition
Validates that a referenced exception handler pointer is a valid exception handler.

## Parent Class(es)
- Application Hardening

## Relationships
- **kb-reference:** Reference - /SAFESEH (Image has Safe Exception Handlers) - Microsoft Docs
- **validates:** Pointer

## Knowledge Base Article
## How It Works
When a process encounters an exception, it calls an exception handler to deal with the exception.  The method by which this exception handler is determined varies by the operating system.  The exception handler is called, even if it is the default exception handler to terminate the program and display a message that the program stopped working.  In the case that no valid exception handler is found, the program would fail to proceed as normal and could be programmed to terminate.

In Windows, the address of the exception registration record is stored at the very start of the Thread Information Block; the GS register points to this structure.

The exception registration record contains two pointers: a pointer to the next exception registration record should this handler fail to handle the exception, and a pointer to the handler.

A buffer overflow can overwrite the saved return pointer with an invalid location to execute memory; this often triggers the exception handler chain, which could also be corrupted by the buffer overflow.  Although Process Exception Handler Validation does not make sure that the exception handler pointer or the code at the exception handler was unaltered, or that the exception handler code is secure, this technique does ensure that the pointer is at least an exception handler that could be called by the program.

With Process Exception Handler Validation, before the handler is called, it checks the exception handler against a source of valid exception handlers.  If the requested handler is not in this list, other techniques such as those in Process Eviction might be invoked, such as Process Termination to end the current process, or Executable Blacklisting to blacklist the potentially vulnerable or malfunctioning executable.

### Runtime valid exception handler source generation
The source of valid exception handlers could be generated at runtime, with the risk of the information that is used to determine the validity of exception handlers being compromised.

### Compile-time
The source of valid exception handlers could also be generated at compile time or as a binary patch.  Given the source code, it would be rather straightforward to find the exceptions, as they are pointed in the catch statement of a try-catch clause and the compiler must already generate the code to call exceptions from this.

## Considerations
If the program file can be altered by the attacker, then the security could be bypassed by replacing it with any desired program, without even bypassing SEH.

If the attacker was already able to overwrite the code for a valid exception handler via other functionality in the program, this defense would not prevent arbitrary code execution.
If an exception handler recognized as valid is vulnerable, it would be executed anyway.

SafeSEH might be applied only to some executable files or modules, allowing an attacker to call any piece of code as an exception handler in the unprotected modules.


---

# D3-EAL: Executable Allowlisting

**Synonym(s):** File Signature Authentication  
**Reference:** https://d3fend.mitre.org/technique/D3-EAL/  

## Definition
Using a digital signature to authenticate a file before opening.

## Parent Class(es)
- Execution Isolation

## Relationships
- **blocks:** Executable File
- **filters:** Create Process
- **kb-reference:** Reference - Computing apparatus with automatic integrity reference generation and maintenance - Tripwire, Inc.
- **kb-reference:** Reference - Enhancing Network Security By Preventing User-Initiated Malware Execution - MITRE

## Knowledge Base Article
## How it works

This technique is generic and there are numerous ways to compute and authenticate digital signatures.
A digital certificate is generated from a private/public key pair issued by a certificate authority (CA). A hash of the file is encrypted using the private key. When the file is downloaded by another user, the user's system uses the public key to decrypt the hash and a new hash is created of the downloaded file. The hash decrypted by the public key is compared to the new hash and if there is a mismatch, further techniques, such as file deletion, file quarantine, or **Executable Blacklisting** may be invoked.

This technique may be invoked when deciding whether to load or execute a file.

## Considerations

Organizations which download or create high volumes of software make management complex, in particular engineering or scientific organizations.


---

# D3-EDL: Executable Denylisting

**Synonym(s):** Executable Blacklisting  
**Reference:** https://d3fend.mitre.org/technique/D3-EDL/  

## Definition
Blocking the execution of files on a host in accordance with defined application policy rules.

## Parent Class(es)
- Execution Isolation

## Relationships
- **blocks:** Executable File
- **filters:** Create Process
- **kb-reference:** Reference - Content extractor and analysis system - Bit 9 Inc, Carbon Black Inc
- **kb-reference:** Reference - Method and apparatus for increasing the speed at which computer viruses are detected - McAfee LLC

## Knowledge Base Article
## How it works

#### Criteria

A policy-enforcing application can register an application for denylisting based on conditions including the following:

* File attributes
    * file name
    * file path
    * file hash
    * file publisher, as obtained from the digital signature
    * permissions of the file
* File malware scan (eg. Windows SmartScreen)
* User-File combination

This may be done to prevent execution of applications which are:

* an old version with known vulnerabilities
* without a valid license, which could cause legal issues
* in a directory that is accessible to low-privileged users, that could be accessed by a malware dropper
* known trojan horse programs
* too open in their permissions, possibly set to run as a user other than the originator or allowing execution when they should not be
* a match to the hash of other known malware
* are detected as undesirable based on a file scan runtime behavior

System administrators will customize the rules for the given environment.

#### Backend

The policy-enforcing program may work by running in kernel mode, and [intercepting] [system calls which execute a process].

## Considerations

* If denylisting is done by filename, filepath, or hash, these mechanisms may be a worthy first line of defense and detection, but could still be evaded by an attacker.
* Continuous management is needed to keep the denylist up to date, whether it is based on hash, publisher, behavior, or any other digital artifact.
* Although denylists based on attributes such as file path and virus scan could defend against some threats which they have not been explicitly coded to block, denylists may not provide protection from new, unknown, or zero day attacks.


## Examples
On a Windows machine the Windows Defender Application Control (WDAC) policy enforcement is run in the kernel and allows for restricting applications.


---

# D3-EI: Execution Isolation

**Reference:** https://d3fend.mitre.org/technique/D3-EI/  

## Definition
Execution Isolation techniques prevent application processes from accessing non-essential system resources, such as memory, devices, or files.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Isolate


---

# D3-FAPA: File Access Pattern Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-FAPA/  

## Definition
Analyzing the files accessed by a process to identify unauthorized activity.

## Parent Class(es)
- Process Analysis

## Relationships
- **analyzes:** Local Resource Access
- **kb-reference:** Reference - File-modifying malware detection - Crowdstrike Inc

## Knowledge Base Article
## How it works
File modifying malware such as wipers and ransomware are detected by identifying file access patterns that are associated with a malicious process. Examples of file access patterns include accessing a large number of files, accessing multiple file types, files being accessed located in multiple locations in a directory, and copying a file and encrypting the contents of that file into a copy.

## Considerations
Certain file access actions may not be statistically different from authorized activity.


---

# D3-FA: File Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-FA/  

## Definition
File Analysis is an analytic process to determine a file's status. For example: virus, trojan, benign, malicious, trusted, unauthorized, sensitive, etc.

## Parent Class(es)
- Defensive Technique

## Relationships
- **analyzes:** File
- **enables:** Detect

## Knowledge Base Article
## Technique Overview
Some techniques use file signatures or file metadata to compare against historical collections of malware. Files may also be compared against a source of ground truth such as cryptographic signatures. Examining files for potential malware using pattern matching against file contents/file behavior. Binary code may be dissembled and analyzed for predictive malware behavior, such as API call signatures. Analysis might occur within a protected environment such as a sandbox or live system.


---

# D3-FC: File Carving

**Reference:** https://d3fend.mitre.org/technique/D3-FC/  

## Definition
Identifying and extracting files from network application protocols through the use of network stream reassembly software.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** File Transfer Network Traffic
- **kb-reference:** Reference - Computer Worm Defense System and Method - FireEye Inc

## Knowledge Base Article
## How it works
Protocol stream reassembly software recreates a directional byte stream by analyzing captured network packets. Once the stream is reassembled pattern matching is applied to determine if it contains a file of interest. Files of interest range from executable, archive, or document file formats. Once the file is captured, it is then processed with standard File Analysis Techniques. Example network protocols include HTTP, SMTP, FTP, HTTP/2, and TLS/HTTP/Dropbox.

## Considerations
- This is an error prone process due to the intricacies of network protocols and network packet capture.  For example reassembly may be done in real-time or streaming fashion, or packets may be written to disk, then bulk processed.  The packets may arrive out of order, with fragmentation, duplicates, or re-transmissions.  The reassembly software must compensate for the imperfect packet stream in order to recreate the well formed file which was transmitted.
- File type identification can be a difficult process which can be exploited by adversaries.


---

# D3-FCOA: File Content Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-FCOA/  

## Definition
Employing a pattern matching algorithm to statically analyze the content of files.

## Parent Class(es)
- File Analysis

## Relationships
- **kb-reference:** Reference - Cyber vaccine and predictive-malware-defense methods and systems

## Knowledge Base Article
## How it works
Analyzing a piece of code without it being executed in a sandbox, virtual machine, or simulator. Patterns or signatures in the file can indicate whati kind of software it is, including whether it is malware.


---

# D3-FCDC: File Content Decompression Checking

**Reference:** https://d3fend.mitre.org/technique/D3-FCDC/  

## Definition
Checking if compressed or encoded data sections can be successfully decompressed or decoded. Can follow with further analysis with semantic knowledge

## Parent Class(es)
- File Format Verification

## Relationships
- **analyzes:** File Content Block Data
- **kb-reference:** Reference - Carving Contiguous and Fragmented Files with Fast Object Validation
- **kb-reference:** Reference - Gathering Evidence: Model-Driven Software Engineering in Automated Digital Forensics

## Knowledge Base Article
## How it works

Some file formats such as JPEGs include encoded or compressed sections. This technique verifies that those expected sections are present and can be properly decoded according to the spec.


---

# D3-FCR: File Content Rules

**Synonym(s):** File Content Signatures, File Signatures  
**Reference:** https://d3fend.mitre.org/technique/D3-FCR/  

## Definition
Employing a pattern matching rule language to analyze the content of files.

## Parent Class(es)
- File Content Analysis

## Relationships
- **kb-reference:** Reference - Computational modeling and classification of data streams - Crowdstrike Inc
- **kb-reference:** Reference - Detecting script-based malware - Crowdstrike Inc
- **kb-reference:** Reference - Distributed meta-information query in a network - Bit 9 Inc
- **kb-reference:** Reference - System and methods thereof for logical identification of malicious threats across a plurality of end-point devices (epd) communicatively connected by a network - Palo Alto Networks IncCyber Secdo Ltd

## Knowledge Base Article
## How it works
Rules, often called signatures, are used for both generic and targeted malware detection. The rules are usually expressed in a domain specific language (DSL), then deployed to software that scans files for matches. The rules are developed and broadly distributed by commercial vendors, or they are developed and deployed by enterprise security teams to address highly targeted or custom malware. Conceptually, there are public and private rule sets. Both leverage the same technology, but they are intended to detect different types of cyber adversaries.

## Considerations
* Patterns expressed in the DSLs range in their complexity. Some scanning engines support file parsing and normalization for high fidelity matching, others support only simple regular expression matching against raw file data. Engineers must make a trade-off in terms of:
     * The fidelity of the matching capabilities in order to balance high recall with avoiding false positives,
     * The computational load for scanning, and
     * The resilience of the engine to deal with adversarial content presented in different forms-- content which in some cases is designed to exploit or defeat the scanning engines.
 * Signature libraries can become large over time and impact scanning performance.
 * Some vendors who sell signatures have to delete old signatures over time.
 * Simple signatures against raw content cannot match against encoded, encrypted, or sufficiently obfuscated content.

## Implementations
 * YARA
 * ClamAV


---

# D3-FCA: File Creation Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-FCA/  

## Definition
Analyzing the properties of file create system call invocations.

## Parent Class(es)
- System Call Analysis

## Relationships
- **analyzes:** Create File
- **kb-reference:** Reference - CAR-2020-09-001: Scheduled Task - FileAccess - MITRE
- **kb-reference:** Reference - CAR-2019-07-002: Lsass Process Dump via Procdump - MITRE


---

# D3-FE: File Encryption

**Reference:** https://d3fend.mitre.org/technique/D3-FE/  

## Definition
Encrypting a file using a cryptographic key.

## Parent Class(es)
- Platform Hardening

## Relationships
- **encrypts:** File
- **kb-reference:** Reference -  File Encryption 101: Safeguarding Your Sensitive Data
- **kb-reference:** Reference - Guide to Storage Encryption Technologies for End User Devices
- **kb-reference:** Reference - Security Considerations for Exchanging Files Over the Internet

## Knowledge Base Article
## How it Works
Files are encrypted using either a single key for both encryption and decryption or separate keys. Single key encryption is symmetric encryption and using two key distinct keys is asymmetric encryption.

### Symmetric Cryptography
Symmetric encryption uses the same cryptographic key for both the encryption and decryption a file. Managing keys at scale sometimes uses asymmetric key exchange. Protocols such as RSA or Diffie-Hellman can be used to share the symmetric cryptographic key with the others.

### Asymmetric Cryptography
Asymmetric encryption is typically accomplished using public and private key certificates based on the X.509 standard. Files are encrypted using the public key and decrypted using their private key. Asymmetric encryption is typically slower than symmetric encryption and not widely used for large file encryption, but is popular for key wrapping, key exchanges, and digital signatures.

## Considerations
- Continuous monitoring must be carried out to ensure private keys are not compromised and the certificate authority (CA) is trusted.
- Transfer of private keys between multiple devices must be performed securely.


---

# D3-FEV: File Eviction

**Reference:** https://d3fend.mitre.org/technique/D3-FEV/  

## Definition
File eviction techniques delete files from system storage.

## Parent Class(es)
- Object Eviction

## Relationships
- **deletes:** File
- **kb-reference:** Reference - How Does Antivirus Quarantine Work? - Safety Detectives

## Knowledge Base Article
## How it works

Adversaries may place files or programs into a computer's file system to perform malicious actions. As part of the eviction process, these files and programs should be removed to prevent further compromise or reinfection. Examples of malicious types of files are malware which is directly harmful and content files with the intent to deceive users (e.g., phishing.)

On Windows systems, antivirus (AV) software should be used to safely and permanently remove malicious files. AV software may first quarantine a suspected malicious file, which is the process of moving a file from its original location to a new location and makes changes so that it cannot be executed. Users can then verify that the file is not benign and then permanently delete it.

## Considerations

When it is determined that a file should be removed for security purposes, the organization--or systems implementing an organization's policies--may determine that the file should not simply be deleted from the enterprise's mission systems, but be quarantined to a secure system by an approved mechanism, so as to allow follow-up investigation by security staff.

On Windows systems, deleting a file in File Explorer does not permanently delete a file - it sends it to the Recycle Bin instead. The Recycle Bin must be emptied, or alternative steps must be performed to remove files completely. Even then, in some cases the data may persist in disk, so data shredder tools may be needed to completely wipe a file. Thus, AV tools are recommended.


---

# D3-FFV: File Format Verification

**Reference:** https://d3fend.mitre.org/technique/D3-FFV/  

## Definition
Verifying that a file conforms to its expected format specifications

## Parent Class(es)
- Content Validation

## Relationships
- **analyzes:** File Section
- **kb-reference:** Reference - File Security Using File Format Validation - OPSWAT Inc


---

# D3-FHRA: File Hash Reputation Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-FHRA/  

## Definition
Analyzing the reputation of a file hash.

## Parent Class(es)
- Identifier Reputation Analysis

## Relationships
- **analyzes:** File Hash
- **kb-reference:** Reference - Reputation of an entity associated with a content item


---

# D3-FH: File Hashing

**Reference:** https://d3fend.mitre.org/technique/D3-FH/  

## Definition
Employing file hash comparisons to detect known malware.

## Parent Class(es)
- File Analysis

## Relationships
- **kb-reference:** Reference - Munin

## Knowledge Base Article
## How it works
This technique requires a list of hashes to compare a file against.

## Considerations
Performance on large files or very large numbers of files.


---

# D3-FIM: File Integrity Monitoring

**Reference:** https://d3fend.mitre.org/technique/D3-FIM/  

## Definition
Detecting any suspicious changes to files in a computer system.

## Parent Class(es)
- Platform Monitoring

## Relationships
- **analyzes:** File
- **kb-reference:** Reference - File Integrity Monitoring in Microsoft Defender for Cloud - Microsoft
- **kb-reference:** Reference - Tripwire

## Knowledge Base Article
## How it Works
There are a number of tools in Windows and Unix that can monitor specific files in a system and generate alerts if any artifacts have been created, modified, or removed. They accomplish this by comparing the current artifacts to a previous snapshot.

Unix - Unix systems have a file integrity checker tool called tripwire. Tripwire first initializes a database that serves as a basis for comparison and can then scan the system to compare the state of the current file system against the initial baseline database. Additionally, users can define policies that specify potential violations.

Windows - In Microsoft Azure, file integrity monitoring can be enabled which can track file and registry key creation, removals, and modifications of specific files.

## Considerations
Files can change constantly due to the non-static nature of a computer system. File Integrity Monitoring works best when pointed at a narrow scope of critical files to limit the number of unnecessary files that may be modified over the course of normal use. The accuracy and precision of defined policies also affect the efficacy of this technique.


---

# D3-FISV: File Internal Structure Verification

**Reference:** https://d3fend.mitre.org/technique/D3-FISV/  

## Definition
The process of checking specific static values within a file, such as file signatures or magic numbers, to ensure they match the expected values defined by the file format specification.

## Parent Class(es)
- File Format Verification

## Relationships
- **analyzes:** File Content Block
- **kb-reference:** Reference - Carving Contiguous and Fragmented Files with Fast Object Validation
- **kb-reference:** Reference - Gathering Evidence: Model-Driven Software Engineering in Automated Digital Forensics

## Knowledge Base Article
## How it works

File format specifications often define expected values for specific fields. A common example are file signatures, or magic numbers, which are used to quickly identify files. Another example is within the Compound Document Header of Microsoft Office files, the 29th and 30th byte identifies the byte order, specifically 0xFFFE for little-endian. This technique verifies that the file's static values match the values of the declared file format's specification.


---

# D3-FMBV: File Magic Byte Verification

**Reference:** https://d3fend.mitre.org/technique/D3-FMBV/  

## Definition
Utilizing the magic number to verify the file

## Parent Class(es)
- File Metadata Value Verification

## Relationships
- **analyzes:** File Magic Bytes
- **kb-reference:** Reference - Carving Contiguous and Fragmented Files with Fast Object Validation
- **kb-reference:** Reference - Gathering Evidence: Model-Driven Software Engineering in Automated Digital Forensics

## Knowledge Base Article
## How it works

Many file formats use magic numbers to identify a file format or protocol. Verifying that the magic number matches the expected value of its declared format is a simple way of verifying the file format.


---

# D3-FMCV: File Metadata Consistency Validation

**Reference:** https://d3fend.mitre.org/technique/D3-FMCV/  

## Definition
The process of validating the consistency between a file's metadata and its actual content, ensuring that elements like declared lengths, pointers, and checksums accurately describe the file's content.

## Parent Class(es)
- File Format Verification

## Relationships
- **analyzes:** File Content Block Data
- **analyzes:** File Metadata
- **kb-reference:** Reference - Gathering Evidence: Model-Driven Software Engineering in Automated Digital Forensics

## Knowledge Base Article
## How it works

This technique involves validating the consistency between a file's metadata and its actual content. It checks elements like declared lengths, pointers, and checksums to ensure they accurately describe the file's content. For instance, if a header specifies a content block of 50 bytes, this should be verified, and CRC values should be recalculated and compared.


---

# D3-FMVV: File Metadata Value Verification

**Reference:** https://d3fend.mitre.org/technique/D3-FMVV/  

## Definition
The process of checking specific static values within a file, such as file signatures or magic numbers, to ensure they match the expected values defined by the file format specification.

## Parent Class(es)
- File Format Verification

## Relationships
- **analyzes:** File Footer Block
- **analyzes:** File Header Block
- **description:** ## How it works

File format specifications often define expected values for specific fields. A common example are file signatures, or magic numbers, which are used to quickly identify files. Another example is within the Compound Document Header of Microsoft Office files, the 29th and 30th byte identifies the byte order, specifically 0xFFFE for little-endian. This technique verifies that the file's static values match the values of the declared file format's specification.
- **kb-reference:** Reference - Carving Contiguous and Fragmented Files with Fast Object Validation
- **kb-reference:** Reference - Introductory Computer Forensics


---

# D3-FBA: Firmware Behavior Analysis

**Synonym(s):** Firmware Timing Analysis  
**Reference:** https://d3fend.mitre.org/technique/D3-FBA/  

## Definition
Analyzing the behavior of embedded code in firmware and looking for anomalous behavior and suspicious activity.

## Parent Class(es)
- Platform Monitoring

## Relationships
- **analyzes:** Firmware
- **kb-reference:** Reference - Firmware Behavior Analysis ConFirm
- **kb-reference:** Reference - Firmware Behavior Analysis VIPER

## Knowledge Base Article
## How it works
Firmware behavior analysis provides protections by ensuring that installed firmware has not been tampered with or modified. Firmware analysis applies to mutable firmware and immutable read-only memory (ROMs).

Firmware in deployed network devices is typically not analyzed and monitored for vulnerabilities and thus is subject to potential attacks. This technique makes use of known and measured behavioral attributes, including timing attributes, of analyzed firmware on deployed devices.

A behavioral method that employs known timing measurements may use the timing results from a challenge and response protocol to detect the presence of malware in embedded firmware. Firmware device timing measurements are made, specific to the installed device, and are used in the verifying function.

The original firmware image is modified by injecting a monitoring software component into the embedded firmware code. The injected software components will allow for a software root of trust, the challenge and response protocol, to be implement in the firmware.

A challenge-response is issued and includes a nonce so that replays are not allowed. The firmware will calculate a checksum over all of memory, including the nonce, and return the result. The verification system will compare the computed checksum and the time it took for the computation of the checksum to determine if the firmware has been modified.

## Considerations
* The firmware code will need to be modified to include the behavioral monitoring functionality.
* This technique is sensitive to the device the embedded firmware is hosted on and it is expected that the devices and firmware will need to be profiled and analyzed to determine timing estimation.
* This technique is not expected to be one hundred percent correct as you would expect in a hardware root of trust solution and may require some tuning.


---

# D3-FEMC: Firmware Embedded Monitoring Code

**Reference:** https://d3fend.mitre.org/technique/D3-FEMC/  

## Definition
Monitoring code is injected into firmware for integrity monitoring of firmware and firmware data.

## Parent Class(es)
- Platform Monitoring

## Relationships
- **analyzes:** Firmware
- **kb-reference:** Reference - Firmware Embedded Monitoring Code Red Balloon
- **kb-reference:** Reference - Firmware Embedded Monitoring Code Symbiotes

## Knowledge Base Article
## How it works
Firmware in deployed network devices is typically not monitored for malicious changes. This technique provides a method to embed a software security component into the deployed firmware which provides a near real-time monitoring hook. The exception handling code, in the firmware, is typically used to expose any detected vulnerabilities.

The injected software components provide a feature similar to intrusion detection systems for the firmware by detecting unauthorized modifications of the embedded firmware. The integrity of static code and firmware data are monitored continuously in the hosted devices. Comparisons are made to monitored elements like firmware memory addresses and data segments. Memory pages are scanned and if a modification is detected the software component may lock the page. This will protect subsequent attempted modifications to the firmware. The software component may utilize the exception handling code and thus be able to disclose the exact address of the modified memory.

The injected software components are inserted during the firmware imaging process. The injected software is assumed to have knowledge of both the embedded code and the current execution state of the host program. The injected software will monitor and alert, in near real-time, on potential suspicious activity. The injected code is run alongside of the embedded code in the host. The injected software operates as an independent entity and is not dependent on the host software.

Finally, this technique may implement other countermeasure techniques as part of their analytical processes. These should be identified by referencing other countermeasure techniques directly as necessary.

## Considerations
* The firmware code will need to be modified and re-hosted on the device.
* Exposing monitoring hooks to the injected code may introduce additional risk.


---

# D3-FV: Firmware Verification

**Reference:** https://d3fend.mitre.org/technique/D3-FV/  

## Definition
Cryptographically verifying firmware integrity.

## Parent Class(es)
- Platform Monitoring

## Relationships
- **kb-reference:** Reference - Firmware Verification Eclypsium
- **kb-reference:** Reference - Firmware Verification Trapezoid
- **kb-reference:** Reference - Platform Firmware Resiliency Guidelines - NIST
- **verifies:** Firmware

## Knowledge Base Article
## How it works
Cryptographic hash values are computed for system and peripheral firmware. The hash values are compared against precomputed hash values for the identified firmware. A hash value mismatch may indicate that the firmware may have been tampered with or updated with a non-current release indicating a misconfiguration for the system.

## Considerations
* Requires cryptographically computed hash values of firmware
* Requires storage of precomputed firmware hash values


---

# D3-FRDDL: Forward Resolution Domain Denylisting

**Synonym(s):** Forward Resolution Domain Blacklisting  
**Reference:** https://d3fend.mitre.org/technique/D3-FRDDL/  

## Definition
Blocking a lookup based on the query's domain name value.

## Parent Class(es)
- DNS Denylisting

## Relationships
- **blocks:** Outbound Internet DNS Lookup Traffic
- **kb-reference:** Reference - Use DNS Policy for Applying Filters on DNS Queries

## Knowledge Base Article
## How it works

Policies are created that filter DNS queries using fully qualified domain name (FQDN) of record in the query. A DNS policy can be created for blocking DNS queries from FQDNs that have been identified as unauthorized.

## Considerations

Continuous maintenance of unauthorized domain lists is needed to keep up to date as updates occur.


---

# D3-FRIDL: Forward Resolution IP Denylisting

**Synonym(s):** Forward Resolution IP Blacklisting  
**Reference:** https://d3fend.mitre.org/technique/D3-FRIDL/  

## Definition
Blocking a DNS lookup's answer's IP address value.

## Parent Class(es)
- DNS Denylisting

## Relationships
- **blocks:** Inbound Internet DNS Response Traffic
- **kb-reference:** Reference - Use DNS Policy for Applying Filters on DNS Queries

## Knowledge Base Article
## How it works

This technique prevents a client from learning IP addresses deemed to be potentially malicious, which would have been delivered via forward resolution responses.

Responses to forward resolution requests (that is, requests where a domain is sent and IP(s) are returned) are collected, and the IP address(es) included as a response are examined. If the IP address(es) are in a range included in the blacklist, then the response is dropped and not forwarded to the client.

The DNS lookup can be blocked by either dropping the network traffic with an inline device, or modifying the value of the response sent by the DNS server. To transparently prevent client applications from hanging on a request, it is common practice to replace malicious values with addresses in the range 127.0.0.0/8 or the address of a honeypot maintained by the network administrators.

## Considerations

* This technique does not prevent the client from contacting the blacklisted IP, only from learning about this IP address via a nameserver lookup request.
* DNS Response traffic can be transmitted over many different protocols, which presents a challenge to implementing methods to extract all DNS answer IP address value(s).
  * DNS has historically used UDP port 53, with TCP port 53 instead used for responses over 512 bytes or after a lack of response over UDP.
  * Usage of new protocols to provide confidentiality for DNS traffic, such as DoH (DNS over HTTPS) and DoT (DNS over TLS), complicates collection of the IP address(es) in DNS responses. These protocols have often been enabled in browser settings transparently after a browser update, with DNS requests proxied over one of these cryptographic protocols through a specified host.
* This technique must be implemented logically between the application that receives the response and the server which sent the response.
  * DNS responses sent in an encrypted manner, such as those using DoH or DoT, will require interception of the TLS connections in order to determine the IP address(es) in the response.
* Replacing the response is not effective in the case that the nameserver uses a technique to provide integrity of its responses, such as DNSSEC for DNS responses.


---

# D3-HBPI: Hardware-based Process Isolation

**Synonym(s):** Virtualization  
**Reference:** https://d3fend.mitre.org/technique/D3-HBPI/  

## Definition
Preventing one process from writing to the memory space of another process through hardware based address manager implementations.

## Parent Class(es)
- Execution Isolation

## Relationships
- **isolates:** Process
- **kb-reference:** Reference - Approaches for securing an internet endpoint using fine-grained operating system virtualization - Bromium, Inc.
- **kb-reference:** Reference - Isolation of applications within a virtual machine - Bromium, Inc.
- **kb-reference:** Reference - Virtualized process isolation - Advanced Micro Devices Inc
- **restricts:** Create Process

## Knowledge Base Article
## How it works
Process isolation, in this context, is address space separation controlled by a security function that limits the communication between processes so that one process cannot directly modify the executing code of another process. For example with virtual address space:

* Process A address space is different from process B address space, which prevents process A from writing to process B

Hardware process isolation is commonly implemented through Direct Memory Access (DMA) which collaborates with a Memory Management Unit (MMU), or Input-Output Memory Management Unit (IOMMU). These hardware controls are deployed directly on processors to aid hosts or enclaves in process isolation.

* DMA - Direct memory access allows memory access to occur independently of the program currently run by the microprocessor. DMA allows for I/O devices to directly read from and write to memory, or it can be used to efficiently copy blocks of memory. During DMA transfers, the microprocessor can execute an unrelated program.
* MMU - A memory management unit acts as an access control and is responsible for performing the translation of virtual memory addresses to physical memory addresses. The MMU allocates each process its own virtual memory space.
* IOMMU - An input-output memory management unit is used to allocate each I/O device its own virtual address space to the underlying physical addresses. IOMMU allows devices that do not support long memory addresses to address the entire memory space.

## Considerations
* Private hosts may be vulnerable to DMA attack if they have a PCI or PCI Express port that connects attached devices directly to physical address space.

## Implementations:
 * Intel Virtualization Technology for Directed I/O (Intel VT-d)
 * Firecracker


---

# D3-HBWP: Hardware-based Write Protection

**Reference:** https://d3fend.mitre.org/technique/D3-HBWP/  

## Definition
Physical methods of preventing data from being written to computer storage.

## Parent Class(es)
- Platform Hardening

## Relationships
- **hardens:** Secondary Storage
- **kb-reference:** Reference - What is Hardware Write Protect?


---

# D3-HCI: Hardware Component Inventory

**Synonym(s):** Hardware Component Discovery, Hardware Component Inventorying  
**Reference:** https://d3fend.mitre.org/technique/D3-HCI/  

## Definition
Hardware component inventorying identifies and records the hardware items in the organization's architecture.

## Parent Class(es)
- Asset Inventory

## Relationships
- **inventories:** Hardware Device
- **kb-reference:** Reference - Advanced device matching system

## Knowledge Base Article
## How it works
Administrators collect information on hardware devices such as peripherals, NICs, processors, and memory devices that are components of the computers in their architecture using a variety of administrative and management tools that query for this information.  In some cases, where such queries are not supported or provide specific information of interest, an administrator may also collect this information through remote administration tools and system commands, either manually or using scripts.

## Considerations
* Scanning and probing techniques using mapping tools can result in side effects to information technology (IT) and operational technology (OT) systems.
* An adversary conducting network enumeration may engage in activities that parallel normal hardware inventorying activities, but would require escalating to admin privileges for most of the operations requiting administrative tools

## Examples
* Bus discovery
   * Admin-scripted PCI Bus inventory using ssh and pciutils
* Application-layer discovery
   * Simple Network Management Protocol (SNMP) collects MIB information
   * Web-based Enterprise Management (WBEM) collects CIM information
      * Windows Management Instrumentation (WMI)
      * Windows Management Infrastructure (MI)


---

# D3-HDDL: Hierarchical Domain Denylisting

**Synonym(s):** Hierarchical Domain Blacklisting  
**Reference:** https://d3fend.mitre.org/technique/D3-HDDL/  

## Definition
Blocking the resolution of any subdomain of a specified domain name.

## Parent Class(es)
- Forward Resolution Domain Denylisting

## Relationships
- **kb-reference:** Reference - Use DNS Policy for Applying Filters on DNS Queries

## Knowledge Base Article
## How it works
This technique is used to block DNS queries from related domains and subdomains that are unauthorized.

Hierarchical domain blacklisting considers the blacklisting of second level domains and additional sub-domains and specific hosts for a given query value. A denylist is maintained that contains DNS names and corresponding subdomains, including wildcards, that should be blocked for a given lookup.

## Considerations
* The denylist of domain names will have to be maintained and will need to be kept up to date
* Other domains that resolve to the domain of interest for blocking (CNAME, etc).
* Denylists should have identified maintenance cycles to ensure lists are not stale.


---

# D3-HDL: Homoglyph Denylisting

**Synonym(s):** Homoglyph Blacklisting  
**Reference:** https://d3fend.mitre.org/technique/D3-HDL/  

## Definition
Blocking DNS queries that are deceptively similar to legitimate domain names.

## Parent Class(es)
- Forward Resolution Domain Denylisting

## Relationships
- **kb-reference:** Reference - Detection of Malicious IDNHomoglyph Domains

## Knowledge Base Article
## How it works

Homoglyph domain blacklisting considers the domain and subdomain structure of a lookup and compares the named components to blacklisted named components. The blacklisted named components are typically crafted modifications of known good domains, e.g., gooogle.com versus google.com. The blacklisted domains typically resemble trusted domains, but have been altered slightly to deceive users.

The blacklisted named components also include consideration for fonts or Unicode characters that can make certain characters appear very similar (zero vs capital O and the letter l vs the number one). The blacklisted domains under certain fonts will appear to be a trusted domain.

## Considerations
* Maintaining the currency of the list can be a challenge especially with newly registered domain entries.
* Blacklists should have identified maintenance cycles to ensure lists are not stale.


---

# D3-HD: Homoglyph Detection

**Reference:** https://d3fend.mitre.org/technique/D3-HD/  

## Definition
Comparing strings using a variety of techniques to determine if a deceptive or malicious string is being presented to a user.

## Parent Class(es)
- Identifier Analysis

## Relationships
- **analyzes:** Email
- **analyzes:** URL
- **kb-reference:** Reference - Computer-implemented methods and systems for identifying visually similar text character strings - Greathorn Inc
- **kb-reference:** Reference - System and method for detecting homoglyph attacks with a siamese convolutional neural network - Endgame Inc

## Knowledge Base Article
## How it works
A homoglyph, in this context, is a deceptive string or word which looks like a trusted word, but is composed of different characters, for example: goooogle.com versus google.com. This is commonly found in phishing and typo squatting attacks where a human exploiting through a social engineering campaign.

## Considerations
* In very large environments processing DNS queries can be computationally expensive due to the amount of traffic that is generated
* Legitimate companies and products use non-dictionary words in their names that could result in many false positives


---

# D3-HR: Host Reboot

**Reference:** https://d3fend.mitre.org/technique/D3-HR/  

## Definition
Initiating a host's reboot sequence to terminate all running processes.

## Parent Class(es)
- Host Shutdown

## Relationships
- **kb-reference:** Reference - Near-Memory & In-Memory Detection of Fileless Malware
- **terminates:** Process

## Knowledge Base Article
## How It Works

Host reboot can either be initiated in the physical presence of the device using the power functions or remotely using the provided user interface or an installed EDR agent (with the available function). This process may allow for the removal of specific types of malware, such as fileless malware, and can also prevent further damage, for example, if the system is part of a botnet.

## Considerations

- If the attacker has achieved persistence techniques, this technique may not be effective
- Compromised systems may not respond to remote commands to shutdown or reboot, requiring physical intervention.
- Shutting down a system will usually result in the memory losing its state which can be useful in forensic activities so this should be considered when deciding to shutdown.
- Shutting down or rebooting systems may disrupt access to computer resources for legitimate users.


---

# D3-HS: Host Shutdown

**Reference:** https://d3fend.mitre.org/technique/D3-HS/  

## Definition
Initiating a host's shutdown sequence to terminate all running processes.

## Parent Class(es)
- Process Eviction

## Relationships
- **kb-reference:** Reference - Near-Memory & In-Memory Detection of Fileless Malware
- **terminates:** Process

## Knowledge Base Article
## How It Works

Host shutdown can either be initiated in the physical presence of the device using the power functions or remotely using the provided user interface or an installed EDR agent (with the available function). This process may allow for the removal of specific types of malware, such as fileless malware, and can also prevent further damage, for example, if the system is part of a botnet.

## Considerations

- If the attacker has achieved persistence techniques, this technique may not be effective
- Compromised systems may not respond to remote commands to shutdown or reboot, requiring physical intervention.
- Shutting down a system will usually result in the memory losing its state which can be useful in forensic activities so this should be considered when deciding to shutdown.
- Shutting down systems may disrupt access to computer resources for legitimate users.


---

# D3-IOPR: IO Port Restriction

**Reference:** https://d3fend.mitre.org/technique/D3-IOPR/  

## Definition
Limiting access to computer input/output (IO) ports to restrict unauthorized devices.

## Parent Class(es)
- Access Mediation

## Relationships
- **filters:** Input Device
- **filters:** Removable Media Device
- **isolates:** I/O Module
- **kb-reference:** Reference - Computer motherboard having peripheral security functions
- **kb-reference:** Reference - Method and system for controlling communication ports
- **kb-reference:** Reference - USB filter for hub malicious code prevention system

## Knowledge Base Article
## How It works

Software-based restriction uses agent software installed on a computer system. The agent software monitors all IO port system traffic. The agent software is configurable to limit the use of certain devices connected to IO ports. The restriction software can also be configured to limit the access to files and applications on external storage devices connected to IO ports.

Hardware-based restriction can also be employed to limit access to IO ports. For example, a hardware USB filter device that is placed between the host system and the external devices can filter IO port connections based on configurable rules. When new devices are connected to the USB filter the type of device is determined. Using an allow list a connection determination is made for the device.

Some implementations detect when a device is connected in order to authorize the connection against a list of approved devices, in some cases by device type. For example, if the device is determined to be a storage device, then the contained files and executables are examined to more accurately identify the device type.

Types of restrictions that may be applied:
- Device connection
- Device command filtering
- Device file system read or write restrictions

## Considerations
 * Agent software will need to be installed on host systems
 * Configurations for allow/deny for devices and files will need to be maintained


---

# D3-IPCTA: IPC Traffic Analysis

**Synonym(s):** IPC Analysis  
**Reference:** https://d3fend.mitre.org/technique/D3-IPCTA/  

## Definition
Analyzing standard inter process communication (IPC) protocols to detect deviations from normal protocol activity.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Intranet IPC Network Traffic
- **kb-reference:** Reference - CAR-2015-04-001: Remotely Scheduled Tasks via AT - MITRE
- **kb-reference:** Reference - CAR-2013-05-005: SMB Copy and Execution - MITRE
- **kb-reference:** Reference - CAR-2013-01-003: SMB Events Monitoring - MITRE
- **kb-reference:** Reference - CAR-2013-09-003: SMB Session Setups - MITRE
- **kb-reference:** Reference - CAR-2014-03-001: SMB Write Request - NamedPipes - MITRE
- **kb-reference:** Reference - CAR-2013-05-003: SMB Write Request - MITRE
- **kb-reference:** Reference - Security System with Methodology for Interprocess Communication Control - Check Point Software Tech Inc

## Knowledge Base Article
## How it works
Inter process communication enables applications or threads to share data. This can involve one or more computers. Monitoring IPC in your environment can reveal abnormal or malicious activity.
IPC can occur within a single computer or between multiple computers remotely through network protocols. Thus there are multiple ways to collect and monitor these exchanges between processes. A network protocol analyzer may monitor and parse SMB network traffic to record system activity. A host based monitoring agent may monitor IPC activity contained within a single host to look for deviations from standard usages.

### Examples
 * SMB
 * Zeromq
 * Java RMI API

## Considerations
* IPC can generate substantial amounts of data, and it may not be feasible to collect all of it.
* IPC may occur over loopback interfaces or direct memory access granted by the operating system.


---

# D3-IPRA: IP Reputation Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-IPRA/  

## Definition
Analyzing the reputation of an IP address.

## Parent Class(es)
- Identifier Reputation Analysis

## Relationships
- **analyzes:** IP Address
- **kb-reference:** Reference - Database for receiving, storing and compiling information about email messages
- **kb-reference:** Reference - Finding phishing sites


---

# D3-IAA: Identifier Activity Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-IAA/  

## Definition
Taking known malicious identifiers and determining if they are present in a system.

## Parent Class(es)
- Identifier Analysis

## Relationships
- **analyzes:** Identifier
- **kb-reference:** Reference - The Pyramid of Pain - David Bianco

## Knowledge Base Article
## How it works

Identifier activity analysis is the process of taking identifiers--typically known malicious identifiers--and determining the artifacts that have interacted with those identifiers.

There are many open and closed source repositories of identifiers that represent indicators of compromise. For example, VirusTotal contains hash signatures of malware and IP Addresses used by threat actors. Defenders can search for these indicators of compromise their own systems to gain context on activity around an identifier.

## Considerations

Indicator activity analysis is a good way to gain high precision analysis, but adversaries can modify their own signatures such as hashes quickly to evade detection. This is related to David Bianco’s Pyramid of Pain - Indicators on the lower level (hash values, IP addresses domain names) are easy for adversaries to change.

Identifier activity data of interest for analysis with the identifier might include, but is not limited to:

* network traffic activity where the identifier was used to identify communicating entities or referred to in the communication
* process activity referencing the identifier, especially for resource access
* file activity referencing the identifier
* registry settings referencing the identifier


---

# D3-ID: Identifier Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-ID/  

## Definition
Analyzing identifier artifacts such as IP address, domain names, or URL(I)s.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Detect


---

# D3-IRA: Identifier Reputation Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-IRA/  

## Definition
Analyzing the reputation of an identifier.

## Parent Class(es)
- Identifier Analysis

## Relationships
- **kb-reference:** Reference - Finding phishing sites


---

# D3-ISVA: Inbound Session Volume Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-ISVA/  

## Definition
Analyzing inbound network session or connection attempt volume.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Inbound Internet Network Traffic
- **kb-reference:** Reference - Detecting DDoS Attack Using Snort
- **kb-reference:** Reference - Identifying a denial-of-service attack in a cloud-based proxy service - Cloudfare Inc.
- **kb-reference:** Reference - Method and system for UDP flood attack detection - Riorey LLC
- **kb-reference:** Reference - Protecting against distributed denial of service attacks - Cisco Technology Inc.
- **kb-reference:** Reference - Protecting against distributed network flood attacks - Juniper Networks Inc.

## Knowledge Base Article
## How it works
Network appliances are configured to alert on certain packets that typically are involved in DoS attacks. Typical packets include ICMP packets and SYN requests that are commonly used to flood networks. A sampling period is used to define a time window in which collected counts of the identified packets can be measured. If the collected number of packets exceeds a predefined limit then an alert is generated.

## Considerations
Scalability as volume of attacks increase; single servers may not have the memory and storage resources to handle high volumes of network traffic.


---

# D3-ITF: Inbound Traffic Filtering

**Reference:** https://d3fend.mitre.org/technique/D3-ITF/  

## Definition
Restricting network traffic originating from untrusted networks destined towards a private host or enclave.

## Parent Class(es)
- Network Traffic Filtering

## Relationships
- **filters:** Inbound Network Traffic
- **kb-reference:** Reference - Active firewall system and methodology - McAfee LLC
- **kb-reference:** Reference - Automatically generating rules for connection security - Microsoft
- **kb-reference:** Reference - FWTK - Firewall Toolkit
- **kb-reference:** Reference - Firewall for interent access - Secure Computing LLC
- **kb-reference:** Reference - Firewall for processing a connectionless network packet - National Security Agency
- **kb-reference:** Reference - Firewall for processing connection-oriented and connectionless datagrams over a connection-oriented network - National Security Agency
- **kb-reference:** Reference - Firewalls that filter based upon protocol commands - Intel Corp
- **kb-reference:** Reference - Method for controlling computer network security - Checkpoint Software Technologies Ltd
- **kb-reference:** Reference - Network firewall with proxy - Secure Computing LLC

## Knowledge Base Article
## How it works
Inbound Traffic, in this context, is network traffic originating from an untrusted network towards a private host or enclave.
For example:

* An untrusted network host connecting to a internal commercial portal, shopping.example.com
* An external mail server connecting to an internal mail server, mail.example.com

Filtering policies are developed by administrators to meet business requirements and limit connectivity. These policies are implemented on edge devices such as firewalls, routers, and intrusion prevention systems. Examples of filters:

* Blocking incoming traffic from spoofed internally facing IP addresses
* Blocking specific ports and services from establishing connections
* Limiting specific IP ranges from connecting to the network
* Dynamic inbound filtering (Hole punching, STUN, NAT-T)

## Considerations
* Business requirements typically drive the development of filtering rulesets
* Protocols using non-standard ports may circumvent filtering technology, which does not detect application protocol based on traffic content

## Implementations
* OpenWRT (Embedded)
* Netfilter (Linux)
* Windows Firewall
* pf(BSD)


---

# D3-IBCA: Indirect Branch Call Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-IBCA/  

## Definition
Analyzing vendor specific branch call recording in order to detect ROP style attacks.

## Parent Class(es)
- Process Analysis

## Relationships
- **kb-reference:** Reference - Indirect Branching Calls

## Knowledge Base Article
## How it works

This technique is used to detect an attacker attempting to exploit and execute code on a target system's call stack using return-oriented programming (ROP). Modern processors that have the ability to maintain a list of the branching calls, e.g., Intel's Last Branch Recording (LBR), can be used to track and analyze indirect branching calls that are indicative of malicious activity.

In order to reduce the number of indirect branch calls to analyze to a manageable set it is assumed that malicious ROP activity will involve the use of system calls.  The technique observes indirect branch calls that are part of paths that lead to system calls, all others are ignored. Branching calls chained together is often referred to as gadgets and gadgets are often used in ROP attacks. Indirect branch calls that involve a transfer from user-space to kernel-space are of interest for this technique.

Identification of potential ROP exploit execution includes:

- Inspecting the LBR when a system function call is made

  - The LBR is configured to return only instruction of interest (ret, indirect jmp, indirect calls)


- Behavior is analyzed for
  - Ret instructions that appear to target areas not preceded by the call sites
  - Sequences of small code fragments that appear to be chained through the indirect branching calls (gadgets)


- Of interest are returns that appear to not render control back after calls
  - Typical ret-call are paired
  - gadgets will appear to have ret followed by instruction of next instruction of the following gadget


## Considerations

* May be operating system dependent since specific system calls are used to scope branching behavior
* Processors need to support access to a Last Branch Recording list feature
* The size of the LBR stack can limit the expected size of the analyzed execution stack
* If processor does not support LBR then overhead costs for the analysis can be significant


---

# D3-IDA: Input Device Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-IDA/  

## Definition
Operating system level mechanisms to prevent abusive input device exploitation.

## Parent Class(es)
- Operating System Monitoring

## Relationships
- **analyzes:** Input Device
- **kb-reference:** Reference - Continuous authentication by analysis of keyboard typing characteristics - Bradford Univ., UK
- **kb-reference:** Reference - http://www.biometric-solutions.com/keystroke-dynamics.html - biometric-solutions.com

## Knowledge Base Article
## How it works

Input Device Hardening techniques filter certain commands, or disable related operating system functionality.

### Analytics

All of these values can be analyzed and compared to a baseline:

* Amount of input
* Duration of a single input
* Durations between inputs
* Value of input

Context can also include:

* User which is logged in, to include attributes such as physical location of the user
* Date and time
* System which is processing the input
* Source device of input, to include its properties (eg. manufacturer), configuration (eg. keyboard layout) and behavioral attributes of this device (eg. first use)
* Source system of input (local or remote system)
* Other hardware devices attached to the system


### Actions

Actions can include:

* Disabling the source device
* Sending an alert
* Locking the current session (eg. system screen lock, or returning to an authentication screen in a web app) and requiring one or more methods of authentication to continue
* Administratively disabling credentials for the account or the entire account -- the technique *Account Locking*


### Examples
A malicious input device sends many keystrokes with approximately the same delay between each.  This does not match the normal cadence of input, and the device is disabled.

Input to type the session user's name takes abnormally longer for each keystroke.  The system is locked to the password prompt screen.

A system receives key press events from two different devices -- one device sends keystrokes after the other has been idle for a long time.

A system receives physical input in a user session, while that user has sent input from a device located out of the country in the past hour.

Network traffic is suddenly routed through a new external device, and nearly the same volume of network traffic is subsequently sent out the previously existing interface.  The new external device is disabled, and an alert is raised to investigate the network configuration for a potential compromise.


## Considerations

Given some example of legitimate behavioral input patterns, attackers could mimic those input patterns, a technique which has been used in popular culture in the creation of Deepfake videos and [This Person Does Not Exist](https://thispersondoesnotexist.com).


---

# D3-IRV: Integer Range Validation

**Reference:** https://d3fend.mitre.org/technique/D3-IRV/  

## Definition
Ensuring that an integer is within a valid range.

## Parent Class(es)
- Source Code Hardening

## Relationships
- **hardens:** Mathematical Function
- **kb-reference:** Reference - Integer Range Validation

## Knowledge Base Article
## How it Works
Integer Range Validation can be done by programmatically checking the value of an integer before or after an operation to determine if the resulting value will be valid.
Checking the value of an integer to ensure it is in a valid range helps prevent integer overflow, wraparound, and logical errors.

## Considerations
* A valid range can be defined by language, data-type, or logical constraints.
* Take extra care when doing operations on integers that will result in a value close to the bounds of a valid range.
* Note: This resource should not be considered a definitive or exhaustive coding guideline.


---

# D3-IHN: Integrated Honeynet

**Reference:** https://d3fend.mitre.org/technique/D3-IHN/  

## Definition
The practice of setting decoys in a production environment to entice interaction from attackers.

## Parent Class(es)
- Decoy Environment

## Relationships
- **kb-reference:** Reference - Synchronizing a honey network configuration to reflect a target network environment - Palo Alto Networks Inc
- **spoofs:** Intranet Network

## Knowledge Base Article
## How it works
Integrated honeynets use full production environments connected to the enterprise network, that utilize computing resources or software that attract attackers, and allow full interaction and access that provides a complete view of an attack.

## Considerations
An attacker with control of a system on an Integrated Honeynet could:
* try to attack other connected hosts on the network, its IP range of internal hosts not properly configured to react to connections from machines on the integrated honeynet, or position behind the firewall.
* exploit its position by eavesdropping on network traffic
If an attacker manages to stop the processes used to log an attack without setting off any alarms. [1]

1. Honeypots for Windows, Roger Grimes, 2005


---

# D3-JFAPA: Job Function Access Pattern Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-JFAPA/  

## Definition
Detecting anomalies in user access patterns by comparing user access activity to behavioral profiles that categorize users by role such as job title, function, department.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **analyzes:** Authorization
- **kb-reference:** Reference - Anomaly Detection Using Adaptive Behavioral Profiles - Securonix Inc

## Knowledge Base Article
## How it works
Peer group analysis identifies functionally similar groups of actors (users or resources) based on categorizations such as job title, organizational hierarchy, or other attribute that indicates similarity of job function. Current user access activity is then compared to the appropriate peer group behavior profile to identify anomalies.

## Considerations
Potential for false positives from anomalies that are not associated with malicious activity.


---

# D3-KBPI: Kernel-based Process Isolation

**Reference:** https://d3fend.mitre.org/technique/D3-KBPI/  

## Definition
Using kernel-level capabilities to isolate processes.

## Parent Class(es)
- Execution Isolation

## Relationships
- **isolates:** Process
- **kb-reference:** Reference - Overview of the seccomp sandbox


---

# D3-LAMED: LAN Access Mediation

**Reference:** https://d3fend.mitre.org/technique/D3-LAMED/  

## Definition
LAN access mediation encompasses the application of strict access control policies, systematic verification of devices, and authentication mechanisms to govern connectivity to a Local Area Network.

## Parent Class(es)
- Network Access Mediation

## Relationships
- **isolates:** Local Area Network
- **kb-reference:** Reference - What is Network Access Control?

## Knowledge Base Article
## How it works

LAN Access Mediation is a network security approach that manages and controls access to a Local Area Network by using key components such as Access Control Lists (ACLs) to specify which devices are allowed or denied access, Port Security to restrict device connections to specific switch ports, RADIUS for determining the level of access or specific resources available to users or devices, and 802.1X for enforcing device authentication before granting network access. This comprehensive strategy ensures that only authorized devices and users can connect to the network, enhancing overall security.


---

# D3-LAM: Local Account Monitoring

**Reference:** https://d3fend.mitre.org/technique/D3-LAM/  

## Definition
Analyzing local user accounts to detect unauthorized activity.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **analyzes:** Local User Account
- **kb-reference:** Reference - Audit User Account Management
- **kb-reference:** Reference - CAR-2016-04-004: Successful Local Account Login
- **kb-reference:** Reference - OS Query Windows User Collection Code


---

# D3-LFAM: Local File Access Mediation

**Synonym(s):** Local File Access Control  
**Reference:** https://d3fend.mitre.org/technique/D3-LFAM/  

## Definition
Local file access mediation is the process of an operating system granting or denying a specific access request to a local file.

## Parent Class(es)
- System Call Filtering

## Relationships
- **filters:** Open File
- **kb-reference:** Reference - File and Folder Permissions


---

# D3-LFP: Local File Permissions

**Reference:** https://d3fend.mitre.org/technique/D3-LFP/  

## Definition
Local file permissions is the systematic process of defining, implementing, and managing access control policies that dictate user permissions for accessing files on a local system through the configuration of operating system functionality.

## Parent Class(es)
- Access Policy Administration

## Relationships
- **kb-reference:** Reference - File and Folder Permissions
- **restricts:** Directory
- **restricts:** File


---

# D3-LLM: Logical Link Mapping

**Reference:** https://d3fend.mitre.org/technique/D3-LLM/  

## Definition
Logical link mapping creates a model of existing or previous node-to-node connections using network-layer data or metadata.

## Parent Class(es)
- Network Mapping

## Relationships
- **kb-reference:** Reference - Libre NMS - Network Map Extension
- **maps:** Logical Link
- **maps:** Network
- **maps:** Network Node


---

# D3-MBSV: Memory Block Start Validation

**Reference:** https://d3fend.mitre.org/technique/D3-MBSV/  

## Definition
Ensuring that a pointer accurately references the beginning of a designated memory block.

## Parent Class(es)
- Pointer Validation

## Relationships
- **hardens:** Memory Free Function
- **kb-reference:** Reference - Memory Block Start Validation - GNU C Manual

## Knowledge Base Article
## How it Works
Ensure that a pointer is referencing the beginning of the intended block before using.

## Considerations
Be careful with pointer arithmetic.


---

# D3-MBT: Memory Boundary Tracking

**Reference:** https://d3fend.mitre.org/technique/D3-MBT/  

## Definition
Analyzing a call stack for return addresses which point to unexpected  memory locations.

## Parent Class(es)
- Operating System Monitoring

## Relationships
- **analyzes:** Process Code Segment
- **kb-reference:** Reference - Inferential exploit attempt detection - Crowdstrike Inc

## Knowledge Base Article
## How it works
This technique monitors for indicators of whether a return address is outside memory previously allocated for an object (i.e. function, module, process, or thread). If so, code that the return address points to is treated as malicious code.

## Considerations
Kernel malware can manipulate memory contents, for example modifying pointers to hide processes, and thereby impact the accuracy of memory allocation information used to perform the analysis.


---

# D3-MA: Message Analysis

**Synonym(s):** Electronic Message Analysis, Email Or Messaging Analysis  
**Reference:** https://d3fend.mitre.org/technique/D3-MA/  

## Definition
Analyzing email or instant message content to detect unauthorized activity.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Detect

## Knowledge Base Article
## Technique Overview

Email and messaging are frequently used to deliver malicious content to targets. These enterprise capabilities are used to deliver software exploits or social engineering tricks. If the recipient of a message trusts the sender, attackers can avoid escalating suspicion.

Emails and messages are also complex data structures. They contain files and links, and complex data encodings which vary region to region. Thus the defensive techniques used to analyze emails and messages are highly varied ranging from deep content analysis and execution to social network graph-style analytics to analyze trust or risk.


---

# D3-MAN: Message Authentication

**Reference:** https://d3fend.mitre.org/technique/D3-MAN/  

## Definition
Authenticating the sender of a message and ensuring message integrity.

## Parent Class(es)
- Message Hardening

## Relationships
- **authenticates:** Digital Message
- **kb-reference:** Reference - RFC 6376: DomainKeys Identified Mail (DKIM) Signatures - IETF
- **kb-reference:** Reference - Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 3.1

## Knowledge Base Article
## How it works

### Digital Signature
Digital signatures are used to verifying a message is from the expected sender. In email, Secure/Multipurpose Internet Mail Extensions (S/MIME) protocol is typically used to digitally sign messages. A hash value of the sender's message is created and encrypted with the sender's private key to create a digital signature. The message and the digital signature are sent to the recipient where the sender's public key is used to decrypt the digital signature and compute the hash of the message. The computed hash is compared with the hash from the received message, and any difference in the hash values signify the message did not originate from the sender and has been alerted in transit.

### Message Authentication Code (MAC)
MAC is a fixed size string that is appended to a message to provide message authentication and integrity. The sender MAC signing algorithm takes as input a secret symmetric key shared between sender and recipient and the message to calculate a short tag that is appended to the message. The recipient receives the message with the appended tag, and a MAC verification algorithm is run using the symmetric key to verify the message came from the stated sender and ensure the message has not been tampered with.

## Considerations
- Public keys associated with digital signatures should be verified by a Certification Authority (CA) to prevent impersonation. The CA verifies the owner of a public key and puts the sender's identity and public key into a certificate that is signed by the CA.
- Digital signatures provide non-repudiation where a third party can verify the authenticity of the message using the sender's digital certificate signed by the CA.
- Symmetric keys must be exchanged securely via a private channel and management of new symmetric keys are needed for each pair of participants wishing to exchange messages.


---

# D3-MENCR: Message Encryption

**Reference:** https://d3fend.mitre.org/technique/D3-MENCR/  

## Definition
Encrypting a message body using a cryptographic key.

## Parent Class(es)
- Message Hardening

## Relationships
- **encrypts:** Digital Message
- **kb-reference:** Reference - Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 3.1

## Knowledge Base Article
## How it works

### Asymmetric Cryptography
Asymmetric encryption is typically accomplished using public and private key certificates based on the X.509 standard. The sender encrypts messages using the recipient's public key and the receipt decrypts the message using their private key. Standards that can be used to implement user message encryption include S/MIME (Secure/Multipurpose Internet Mail Extensions) and PGP.

### Symmetric Cryptography
Symmetric encryption uses the same cryptographic key by both the sender and receiver to encrypt and decrypt a message. Asymmetric key exchange protocols such as Diffie-Hellman can be used to share the cryptographic key with the recipient. For synchronous or low-latency environments (like a message bus), a pre-shared or dynamically derived symmetric key is typically used to minimize computational overhead.

## Considerations
- Separate configuration settings to enable message encryption are often needed for each messenger client (e.g. webmail, desktop client, mobile).
- Continuous monitoring to ensure private keys are not compromised and the certificate authority (CA) is trusted.
- Secure transfer of private keys between multiple devices.
- Encryption adds latency and increases CPU utilization; while negligible for user-to-user messages, it can be a critical factor for real-time bus systems.


---

# D3-MH: Message Hardening

**Reference:** https://d3fend.mitre.org/technique/D3-MH/  

## Definition
The application of security controls to user-to-user and system-to-system communications so messages remain confidential, unaltered, and verifiable while resisting injection, replay, and tampering.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Harden


---

# D3-MSM: Motion Sensor Monitoring

**Synonym(s):** Motion Alarm Monitoring, Motion Detector Monitoring  
**Reference:** https://d3fend.mitre.org/technique/D3-MSM/  

## Definition
Monitoring events from motion detectors (e.g., passive IR, microwave, dual-technology) to detect presence or movement within protected areas.

## Parent Class(es)
- Physical Access Monitoring

## Relationships
- **kb-reference:** Reference - NIST Special Publication 800-53 Revision 5 - Security and Privacy Controls for Information Systems and Organizations
- **kb-reference:** Reference - Wikipedia: Motion detector
- **kb-reference:** Reference - Wikipedia: Passive infrared sensor
- **monitors:** Motion Detector

## Knowledge Base Article
## How it works

Motion sensors generate events when movement is detected within their coverage pattern. Alarm panels or PACS correlate motion with arming schedules, door openings, and other sensors; video systems can use motion to trigger recording or bookmarks. Cross-zoning and sensitivity/pulse-count settings are commonly adjusted to balance detection and false-alarm rates.

## Considerations

* Place sensors at appropriate height and angle with clear line of sight, avoiding obstructions or reflective surfaces that can cause missed or false detections.
* Reduce false alarms by tuning sensitivity and pulse-count, using cross-zoning when needed, and accounting for HVAC airflow or rapid thermal changes.
* Monitor tamper and supervision signals; for wireless devices, verify periodic check-ins and battery levels; perform regular walk tests to validate coverage.
* Integrate motion events with cameras and with door position switches and other sensors in the protected area to provide context and faster verification; use motion to trigger recording or bookmarks.


---

# D3-MFA: Multi-factor Authentication

**Reference:** https://d3fend.mitre.org/technique/D3-MFA/  

## Definition
Requiring proof of two or more pieces of evidence in order to authenticate a user.

## Parent Class(es)
- Agent Authentication

## Relationships
- **kb-reference:** Reference - Method and apparatus for utilizing a token for resource access - Rsa Security Inc.
- **uses:** Credential

## Knowledge Base Article
## How it works
When logging into an account users present two or more credentials that fall into different categories: something you know (password or PIN), something you have (smart card or phone), or something you are (fingerprint).

## Considerations
MFA configuration steps may vary across accounts and in some cases left up to users to activate and implement.


---

# D3-NAM: Network Access Mediation

**Synonym(s):** Network Access Control  
**Reference:** https://d3fend.mitre.org/technique/D3-NAM/  

## Definition
Network access mediation is the control method for authorizing access to a system by a user (or a process acting on behalf of a user) communicating through a network, including a local area network, a wide area network, and the Internet.

## Parent Class(es)
- Access Mediation

## Relationships
- **isolates:** Network
- **kb-reference:** Reference - What is Network Access Control?

## Knowledge Base Article
## How it works

Network Access Mediation is a crucial process in telecommunications and IT networks that involves controlling access to network resources. It acts as an intermediary layer between network access requests and the actual network resources, ensuring that only authorized users and devices can access the network.


---

# D3-NI: Network Isolation

**Reference:** https://d3fend.mitre.org/technique/D3-NI/  

## Definition
Network Isolation techniques prevent network hosts from accessing non-essential system network resources.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Isolate


---

# D3-NM: Network Mapping

**Reference:** https://d3fend.mitre.org/technique/D3-NM/  

## Definition
Network mapping encompasses the techniques to identify and model the physical layer, network layer, and data exchange layers of the organization's network and their physical location, and determine allowed pathways through that network.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Model


---

# D3-NNI: Network Node Inventory

**Synonym(s):** System Discovery, System Inventorying  
**Reference:** https://d3fend.mitre.org/technique/D3-NNI/  

## Definition
Network node inventorying identifies and records all the network nodes (hosts, routers, switches, firewalls, etc.) in the organization's architecture.

## Parent Class(es)
- Asset Inventory

## Relationships
- **inventories:** Network Node
- **kb-reference:** Reference - IEEE Standard for Local and Metropolitan Area Networks - Station and Media Access Control Connectivity Discovery
- **kb-reference:** Reference - Qualys Network Passive Sensor Getting Started Guide
- **kb-reference:** Reference - An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks
- **kb-reference:** Reference - Web-Based Enterprise Management
- **kb-reference:** Reference - Windows Management Infrastructure (MI)
- **kb-reference:** Reference - Windows Management Instrumentation (WMI)

## Knowledge Base Article
## How it works
Administrators collect information on network nodes in their architecture using a variety of administrative and management tools that query network devices and nodes for information.  In some cases, where such queries are not supported or provide specific information of interest, an administrator may also collect this information through network enumeration methods to include host discovery and scanning for active ports and services.

## Considerations
* Scanning and probing techniques using mapping tools can result in side effects to information technology (IT) and operational technology (OT) systems.
* An adversary conducting network enumeration may engage in activities that parallel normal network node inventorying activities, but would require escalating to admin privileges for most of the operations requiting administrative tools

## Examples
* Link-layer discovery
   * Link-layer Discovery Protocol (LLDP)
   * Cisco Discovery Protocol (CDP)
* Application-layer discovery
   * Simple Network Management Protocol (SNMP) collects MIB information
   * Web-based Enterprise Management (WBEM) collects CIM information
      * Windows Management Instrumentation (WMI)
      * Windows Management Infrastructure (MI)


---

# D3-NRAM: Network Resource Access Mediation

**Synonym(s):** Remote Access Control  
**Reference:** https://d3fend.mitre.org/technique/D3-NRAM/  

## Definition
Control of access to organizational systems and services by users or processes over a network.

## Parent Class(es)
- Access Mediation

## Relationships
- **isolates:** Network Resource
- **kb-reference:** Reference - NIST Special Publication 800-53 Revision 5 - Security and Privacy Controls for Information Systems and Organizations

## Knowledge Base Article
## How it works

Network Resource Access Control involves managing and regulating access to resources within an organization's network. This includes ensuring that only authorized users or processes can access specific systems or data, often through authentication and authorization mechanisms. Examples include accessing internal databases, file servers, or application services.


---

# D3-NTA: Network Traffic Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-NTA/  

## Definition
Analyzing intercepted or summarized computer network traffic to detect unauthorized activity.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Detect


---

# D3-NTCD: Network Traffic Community Deviation

**Reference:** https://d3fend.mitre.org/technique/D3-NTCD/  

## Definition
Establishing baseline communities of network hosts and identifying statistically divergent inter-community communication.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Network Traffic
- **kb-reference:** Reference - System for implementing threat detection using daily network traffic community outliers - VECTRA NETWORKS Inc

## Knowledge Base Article
## How it works
Hosts/users within a computer network are analyzed to identify communities of hosts which frequently communicate. Future communications between communities that don't usually communicate can then be detected.  For example, if a community of hosts that communicate in support of a company's finance division suddenly starts to access the code server usually accessed only by engineers, this may indicate unauthorized activity.

## Considerations
* Potential for false positives in very dynamic network environments.
* Attackers that move low and slow may not differentiate their behavior enough to trigger an alert.


---

# D3-NTF: Network Traffic Filtering

**Reference:** https://d3fend.mitre.org/technique/D3-NTF/  

## Definition
Restricting network traffic originating from any location.

## Parent Class(es)
- Network Isolation

## Relationships
- **filters:** Network Traffic
- **filters:** OT Protocol Message
- **filters:** Remote Command
- **kb-reference:** Reference - Active firewall system and methodology - McAfee LLC
- **kb-reference:** Reference - Automatically generating rules for connection security - Microsoft
- **kb-reference:** Reference - FWTK - Firewall Toolkit
- **kb-reference:** Reference - Firewall for interent access - Secure Computing LLC
- **kb-reference:** Reference - Firewall for processing a connectionless network packet - National Security Agency
- **kb-reference:** Reference - Firewall for processing connection-oriented and connectionless datagrams over a connection-oriented network - National Security Agency
- **kb-reference:** Reference - Firewalls that filter based upon protocol commands - Intel Corp
- **kb-reference:** Reference - Method for controlling computer network security - Checkpoint Software Technologies Ltd
- **kb-reference:** Reference - Network firewall with proxy - Secure Computing LLC


---

# D3-NTPM: Network Traffic Policy Mapping

**Synonym(s):** DLP Policy Mapping, Firewall Mapping, IPS Policy Mapping, Web Security Gateway Policy Mapping  
**Reference:** https://d3fend.mitre.org/technique/D3-NTPM/  

## Definition
Network traffic policy mapping identifies and models the allowed pathways of data at the network, transport, and/or application levels.

## Parent Class(es)
- Network Mapping

## Relationships
- **kb-reference:** Reference - Cisco ASR 9000 Series Aggregation Services Routers - Access List Commands
- **maps:** Access Control Configuration
- **queries:** Network Agent


---

# D3-NTSA: Network Traffic Signature Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-NTSA/  

## Definition
Analyzing network traffic and compares it to known signatures

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Network Traffic
- **kb-reference:** Reference - System and method for strategic anti-malware monitoring - Tenable

## Knowledge Base Article
## How it works

Network signature analysis relies on predefined patterns, or signatures, to identify malicious network activity. These signatures typically match against specific byte sequences, packet header information, or protocol anomalies indicative of known threats.

The process works as follows:

* Packet Capture: Network traffic is captured on an interface or port, resulting in a stream of raw packets.
* Preprocessing: The captured packets are preprocessed, cleaning and normalizing the data for efficient analysis.
* Signature Matching: Each packet is compared against a database of signatures using dedicated engines.

## Considerations

### False Negatives

Network signature analysis is susceptible to generating false negatives. These occur when malicious activity evades detection due to limitations in the signature-based approach. Here are some common causes:

* Evolving threats: Attackers frequently modify their tactics, rendering existing signatures ineffective against new variants.
* Obfuscation: Attackers may disguise malicious content using encryption, encoding, or other techniques to bypass signature detection.
* Limited visibility: Signatures rely on specific patterns. If crucial information is encrypted or hidden, the signature might miss the threat.
* Zero-day attacks: By definition, new and unknown attacks lack corresponding signatures, allowing them to pass undetected.

### False Positives

Network signature analysis is susceptible to generating false positives. These occur when the signature analysis triggers an alert for benign traffic. Common causes include:

* Overly broad signatures: Rules designed to be too general might match harmless activities, generating false alarms.
* Network misconfigurations: Improperly configured devices or legitimate network activity can mimic malicious patterns, triggering false positives.
* Data errors: Corrupted or incomplete network data can lead to misinterpretations and false alerts.


---

# D3-NVA: Network Vulnerability Assessment

**Reference:** https://d3fend.mitre.org/technique/D3-NVA/  

## Definition
Network vulnerability assessment relates all the vulnerabilities of a network's components in the context of their configuration and interdependencies and can also include assessing risk emerging from the network's design as a whole, not just the sum of individual network node or network segment vulnerabilities.

## Parent Class(es)
- Network Mapping

## Relationships
- **evaluates:** Network
- **identifies:** Vulnerability
- **kb-reference:** Reference - Reachability graph-based safe remediations for security of on-premise and cloud computing environments


---

# D3-NPC: Null Pointer Checking

**Synonym(s):** Nil Pointer Checking  
**Reference:** https://d3fend.mitre.org/technique/D3-NPC/  

## Definition
Checking if a pointer is NULL.

## Parent Class(es)
- Pointer Validation

## Relationships
- **hardens:** Memory Free Function
- **hardens:** Pointer Dereferencing Function
- **kb-reference:** Reference - Null Pointer Checking - SEI
- **kb-reference:** Reference - Null Pointer Dereferencing - CWE-476
- **kb-reference:** Reference - Pointer Validation Function - SEI

## Knowledge Base Article

## How it Works
Programmatically checking if a pointer is NULL before use.

## Considerations
* Pointers should be checked prior to use after they have, or may have been modified.
* Note that it may vary by circumstance whether the caller, or callee is responsible for checking if a pointer is NULL.
* Note: This resource should not be considered a definitive or exhaustive coding guideline.


---

# D3-OVAR: OT Variable Access Restriction

**Synonym(s):** OT Variable Access Policy  
**Reference:** https://d3fend.mitre.org/technique/D3-OVAR/  

## Definition
Assign read/write access controls on designated registers or data tags to prevent unauthorized writes.

## Parent Class(es)
- Access Mediation

## Relationships
- **enables:** Isolate
- **kb-reference:** Reference - PLX3x Series Multi-Protocol Gateways
- **kb-reference:** Reference - S7-1200 Programmable controller
- **kb-reference:** Reference - Secure PLC Coding Practices: Top 20 List
- **limits:** OT Logic Variable
- **restricts:** OT Write Command

## Knowledge Base Article
 ## How it works

Many OT Controllers and OT Communication Modules enable Read-Only or Read/Write access on a per-tag basis.

As an example, when configuring OT process tags which can be accessed using the Modbus protocol, configure the tag to a Modbus Input Register to leverage the protocol's registry ranges, restricting the ability of external sources to modify data.

In Siemens, each data block (DB) tag can be configured as "data block write-protected in the device."


---

# D3-OE: Object Eviction

**Reference:** https://d3fend.mitre.org/technique/D3-OE/  

## Definition
Terminate or remove an object from a host machine. This is the broadest class for object eviction.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Evict


---

# D3-OTP: One-time Password

**Synonym(s):** OTP  
**Reference:** https://d3fend.mitre.org/technique/D3-OTP/  

## Definition
A one-time password is valid for only one user authentication.

## Parent Class(es)
- Password Rotation

## Relationships
- **kb-reference:** Reference - Digital Identity Guidelines 800-63-3
- **kb-reference:** Reference - RFC 2289 - A One-Time Password System
- **use-limits:** Password

## Knowledge Base Article
## How it works

When a user initiates authentication, they are asked for a one-time password, often in addition to other credentials such as a traditional password or smart card. The one-time password may be from a list provided in advance, sent via a channel such as SMS or HTTPS to an app, or a generated token.

In the case of a physical token which generates one-time passwords incrementally based on time elapsed, that token device need not be connected to the internet. In different implementations, an administrator of the system, or a user with additional verification, can adjust for clock skew between the token and the verification system as needed.

## Considerations

### Compromise of delivery channel
- SIM Swapping
- Secure token visual compromise
- Insecure delivery channel

### Compromise of delivery device
Physical loss of One-time Password device.

### Compromise of long-term backup codes
These are often provided in the form of a downloadable document with a regular name, which can be searched for in the case that the user forgets where they put them.  This digital file or printed document could be stolen.
Additionally, after the code file is printed, it could be recovered from the system printer spool unless the spooler cache is cleared.


---

# D3-OMM: Operating Mode Monitoring

**Reference:** https://d3fend.mitre.org/technique/D3-OMM/  

## Definition
Detects operating modes such as Program, Run, Remote, or Stop.

## Parent Class(es)
- Platform Monitoring

## Relationships
- **kb-reference:** Reference - Value of PLC Key Switch Monitoring to Keep Critical Systems More Secure
- **kb-reference:** Reference - TRITON Malware Remains Threat to Global Critical Infrastructure Industrial Control Systems (ICS)
- **monitors:** OT Controller Operating Mode

## Knowledge Base Article
## How it works
Many OT Controllers have key switches to change the controller into various modes of operation. These modes of operation can include Program, Run, Remote, or Stop.

The key switch position is often available as a system diagnostic function block of the programming logic.

## Considerations
* It is advised to configure a key switch alarm such that an operator is alerted when the controller is put into a programming mode, as this could indicate unintentional or malicious changes to operational code.


---

# D3-OPR: Operating Mode Restriction

**Reference:** https://d3fend.mitre.org/technique/D3-OPR/  

## Definition
Restricting unauthorized changes to the operating mode prevents devices from switching into inappropriate or vulnerable states during normal use.

## Parent Class(es)
- Access Mediation

## Relationships
- **kb-reference:** Reference - MITRE ATT&CK - Authorization Enforcement
- **kb-reference:** Reference - TRITON Malware Remains Threat to Global Critical Infrastructure Industrial Control Systems (ICS)
- **restricts:** OT Controller Operating Mode

## Knowledge Base Article
## How it works
Many OT Controllers use key switches to change the controller into different modes of operation. These modes of operation can include Program, Run, Remote, or Stop.

The key switch should be left in the appropriate key switch position, e.g., run or remote during normal operations.

Implement a key management procedure to include removing the physical key from the key switch when not in use.


---

# D3-OSM: Operating System Monitoring

**Reference:** https://d3fend.mitre.org/technique/D3-OSM/  

## Definition
The operating system software, for D3FEND's purposes, includes the kernel and its process management functions, hardware drivers, initialization or boot logic. It also includes and other key system daemons and their configuration. The monitoring or analysis of these components for unauthorized activity constitute **Operating System Monitoring**.

## Parent Class(es)
- Platform Monitoring

## Relationships
- **enables:** Detect
- **kb-reference:** Reference - Host intrusion prevention system using software and user behavior analysis - Sophos Ltd
- **kb-reference:** Reference - CAR-2016-04-002: User Activity from Clearing Event Logs - MITRE

## Knowledge Base Article
## Technique Overview

"An operating system (OS) is system software that manages computer hardware and software resources and provides common services for computer programs." [1]

Operating System Monitoring Techniques have varied implementations including built-in kernel modules, third-party privileged system daemons, or even standard systems administration tools included with an operating system.

1. http://dbpedia.org/resource/Operating_system


---

# D3-OAM: Operational Activity Mapping

**Synonym(s):** Mission Mapping  
**Reference:** https://d3fend.mitre.org/technique/D3-OAM/  

## Definition
Operational activity mapping identifies activities of the organization and the organization's suborganizations, groups, roles, and individuals that carry out the activities and then establishes the dependencies of the activities on the systems and people that perform those activities.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Model
- **kb-reference:** Reference - Catia UAF Plugin


---

# D3-ODM: Operational Dependency Mapping

**Reference:** https://d3fend.mitre.org/technique/D3-ODM/  

## Definition
Operational dependency mapping identifies and models the dependencies of the organization's activities on each other and on the organization's performers (people, systems, and services.)  This may include modeling the higher- and lower-level activities of an organization forming a hierarchy, or layering, of the dependencies in an organization's activities.

## Parent Class(es)
- Operational Activity Mapping

## Relationships
- **kb-reference:** Reference - Catia UAF Plugin
- **kb-reference:** Reference - Cyber Command System (CYCS)
- **kb-reference:** Reference - Dagger Fact Sheet
- **kb-reference:** Reference - Dagger: Modeling and visualization for mission impact situational awareness
- **kb-reference:** Reference - Mission Dependency Modeling for Cyber Situational Awareness
- **kb-reference:** Reference - Unified Architecture Framework (UAF)
- **maps:** Dependency
- **maps:** Operational Activity Plan


---

# D3-OLV: Operational Logic Validation

**Reference:** https://d3fend.mitre.org/technique/D3-OLV/  

## Definition
Validation of variable state in the context of the control logic of the operational application.

## Parent Class(es)
- Domain Logic Validation

## Relationships
- **kb-reference:** Reference - Secure PLC Coding Practices: Top 20 List
- **validates:** OT Control Function

## Knowledge Base Article
## How it works
Validates the type, value, and/or range of a variable taking into account the local operational logic and operational state.

For example, if a controller has a restricted range when in a specified state, this may crosscheck the value against the state in addition to a more general range validation.


---

# D3-OPM: Operational Process Monitoring

**Synonym(s):** Supervisory Control Monitoring  
**Reference:** https://d3fend.mitre.org/technique/D3-OPM/  

## Definition
Monitoring physical parameters and operator actions related to an operational environment.

## Parent Class(es)
- Platform Monitoring

## Relationships
- **kb-reference:** Reference - NIST SP 800-82R3 Guide to Operational Technology (OT) Security, Section 6.2.1.4.5 Password Authentication
- **monitors:** Event Log
- **uses:** OT Process Data Historian

## Knowledge Base Article
## How it works

While some Operational Technology systems are designed to operate without human intervention, most systems are designed with the ability to monitor and modify the physical process with user input.

This technique detects adversarial risks to operational processes by observing physical events and operator actions and analyzing event logs.

Key steps in operational process security monitoring are:

1. Read logs generated by controllers, and HMIs, through DAU's and DA agents;

2. Produce digital event records;

3. Display the aggregated data to a device such as an HMI or process historian, and write those records to event logs and/or to the OT process data historian for traceability and incident reconstruction.

4. Monitor the process and detect incidents or indicators of tampering such as:
- malfunctions
- unauthorized commands,
- unsafe setpoint changes,
- alarm suppression, and
- anomalous mode transitions;


---

# D3-ORA: Operational Risk Assessment

**Synonym(s):** Mission Risk Assessment  
**Reference:** https://d3fend.mitre.org/technique/D3-ORA/  

## Definition
Operational risk assessment identifies and models the vulnerabilities of, and risks to, an organization's activities individually and as a whole.

## Parent Class(es)
- Operational Activity Mapping

## Relationships
- **evaluates:** Organization
- **identifies:** Vulnerability
- **kb-reference:** Reference - MGT516: Managing Security Vulnerabilities: Enterprise and Cloud
- **kb-reference:** Reference - NIST RMF Quick Start Guide - Assess Step - Frequently Asked Questions (FAQ)
- **kb-reference:** Reference - NIST Special Publication 800-160 Volume 1 - System Security Engineering
- **kb-reference:** Reference - NIST Special Publication 800-37 Revision 2 - Risk Management Framework for Information Systems and Organizations
- **kb-reference:** Reference - NIST Special Publication 800-53A Revision 5 - Assessing Security and Privacy Controls in Information Systems and Organizations
- **kb-reference:** Reference - NISTIR 8011 Volume 1 - Automation Support for Security Control Assessments


---

# D3-OM: Organization Mapping

**Reference:** https://d3fend.mitre.org/technique/D3-OM/  

## Definition
Organization mapping identifies and models the people, roles, and groups with an organization and the relations between them.

## Parent Class(es)
- Operational Activity Mapping

## Relationships
- **kb-reference:** Reference - Catia UAF Plugin
- **kb-reference:** Reference - Organizational Management in SAP ERP HCM
- **kb-reference:** Reference - Unified Architecture Framework (UAF)
- **maps:** Dependency
- **maps:** Organization
- **maps:** Person
- **may-map:** Operational Activity Plan


---

# D3-OTF: Outbound Traffic Filtering

**Reference:** https://d3fend.mitre.org/technique/D3-OTF/  

## Definition
Restricting network traffic originating from a private host or enclave destined towards untrusted networks.

## Parent Class(es)
- Network Traffic Filtering

## Relationships
- **filters:** Outbound Network Traffic
- **kb-reference:** Reference - Automatically generating rules for connection security - Microsoft

## Knowledge Base Article
## How it works

Outbound traffic, in this context, is network traffic originating from a private host or enclave destined towards untrusted networks.
For example:

* An enterprise desktop intranet user connecting to www.example.com
* An internal mail server connecting to an external mail server, mail.example.com

Filtering is commonly implemented as firewall rulesets to limit outbound traffic permitted to egress a host or network. Firewalls are deployed either directly on hosts through kernel level software implementations or installed in-line directly on network links. There are benefits and disadvantages to each approach.

There are various strategies for developing filtering rulesets:

* Block everything by default
* Limit destination hosts
* Limit destination transport or application protocols
* Restrict content outbound (Ex. strings formatted as social security numbers, or proprietary data)

## Considerations
* Dynamic IP assignment creates challenges for Outbound Traffic Filtering because users are not necessarily associated with the same IP address. This can be addressed by linking IP address management information with the filtering logic.
* Connections using non-standard transport layer ports may circumvent outbound traffic filtering technology which does not detect application protocol based on traffic content.
* Business requirements typically drive the development of filtering rule sets.

## Implementations
- iptables (Linux)
- Windows Firewall
- pf (BSD)


---

# D3-PCA: Passive Certificate Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-PCA/  

## Definition
Collecting host certificates from network traffic or other passive sources like a certificate transparency log and analyzing them for unauthorized activity.

## Parent Class(es)
- Certificate Analysis

## Relationships
- **kb-reference:** Reference - Certificate Transparency
- **kb-reference:** Reference - StreamingPhish

## Knowledge Base Article
## How it works
Certificates are analyzed outside of a TLS server connection using third-party secure update logs, domain name analysis and analytics.

### Secure update certificate logs
* Certificate Logs
The key enabling feature is a secure service that maintains record logs of certificate activities. The logs allow users to only append certificates and never to delete or modify the log entries. The logs use Merkle Tree Hashes to ensure they have not been tampered with. The logging service also allows for public auditing by any user.

The logging service, upon receipt of a certificate to log, will respond with a signed certificate timestamp (SCT). The SCT guarantees the certificate will be added to the log within the time specified. The SCT must be present with the certificate during a TLS handshake.

* Certificate Monitoring
Certificate monitoring, of the logs, is typically done by the CA and they watch for suspicious certificate logging and unusual certificates or extensions or permissions. Monitors are also responsible for verifying the logs are accurate and public.

* Certificate Auditors
Log integrity is verified by log auditors. Auditors make use of log proofs are used to validate the cryptographic hashes (Merkle Trees) that the log employs are consistent. In order to ensure consistency throughout multiple monitors and auditors, sharing a common logging service, gossip protocol is employed.

### Phishing domain name analysis
* A curated corpus of known benign domains and phishing domain names is used as training text for machine learning. Through the use of feature set extraction, vectors labels are created with scoring to indicated if they are considered benign or phishing domains.

* A stream of new or updated SSL certificates with fully qualified domain names (FQDN) is analyzed against the feature vectors and a predictive model determines a score for the domains. The scoring considers distance measures such as Levenshtein distance to help in determining the final label score. Supervised learning is also employed using the curated domains of benign and phishing domains.

* Subdomain phishing analysis, prepending a trusted domain to a phishing domain, and regular expression comparisons  are also used in the label scoring model. A tunable measure is used to determine the threshold for alerting. This measure helps to balance between precision and recall measures.

## Considerations
* Some entity will need to run the logging service and a trusted entity is preferred.
* Certificate Authorities will likely need to monitor the logging service for consistency.
* Certificate revocation is unchanged and remains outside of Certificate Transparency, but certificates needing to be revoked are visible.
* Technique dependent of reliable feed of new and updated certificates
* Some certificate authorities allow for certificates to be registered with wildcards in the FQDN and thus will fail some of the subdomain scoring
* Phishing HTTP domains will not be discovered


---

# D3-PLLM: Passive Logical Link Mapping

**Synonym(s):** Passive Logical Layer Mapping  
**Reference:** https://d3fend.mitre.org/technique/D3-PLLM/  

## Definition
Passive logical link mapping only listens to network traffic as a means to map the whole data link layer, where the links represent logical data flows rather than physical connections.

## Parent Class(es)
- Logical Link Mapping

## Relationships
- **kb-reference:** Reference - Tenable Passive Network Monitoring


---

# D3-PWA: Password Authentication

**Reference:** https://d3fend.mitre.org/technique/D3-PWA/  

## Definition
Password authentication is a security mechanism used to verify the identity of a user or entity attempting to access a system or resource by requiring the input of a secret string of characters, known as a password, that is associated with the user or entity.

## Parent Class(es)
- Agent Authentication

## Relationships
- **kb-reference:** Reference - NIST Special Publication 800-53 Revision 5 - Security and Privacy Controls for Information Systems and Organizations
- **uses:** Password


---

# D3-PR: Password Rotation

**Reference:** https://d3fend.mitre.org/technique/D3-PR/  

## Definition
Password rotation is a security policy that mandates the periodic change of user account passwords to mitigate the risk of unauthorized access due to compromised credentials.

## Parent Class(es)
- Credential Rotation

## Relationships
- **kb-reference:** Reference - Password and Key Rotation - SSH
- **regenerates:** Password

## Knowledge Base Article
## How it works

Users may be requested to change their passwords on a regular schedule. Management servers with enterprise policies for account management provide the ability to change or reset passwords for accounts.

## Considerations

Requiring users to change their passwords frequently can result in insecure password practices by the user. The latest update of NIST SP 800-63B, Digital Identity Guidelines, recommends requiring password reset only when a known compromise has occurred, or every 365 days, rather than every 60 or 90 days.


---

# D3-PHDURA: Per Host Download-Upload Ratio Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-PHDURA/  

## Definition
Detecting anomalies that indicate malicious activity by comparing the amount of data downloaded versus data uploaded by a host.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Network Traffic
- **kb-reference:** Reference - System for detecting threats using scenario-based tracking of internal and external network traffic - VECTRA NETWORKS Inc

## Knowledge Base Article
## How it works
Aggregate pull vs. push ratios from metadata are used to develop a baseline for a given host over a specific time period, e.g., over a three-hour period, one day, one week, etc. Anomalies identified over a threshold produce an alert.

## Considerations
Collection and analysis of large network packet captures requires large storage and intensive computing power. The time windows used to calculate the ratio may vary in implementations, this consideration should take into account a threat model and likely effects (impacts) delivered by an adversary.


---

# D3-PFV: Peripheral Firmware Verification

**Reference:** https://d3fend.mitre.org/technique/D3-PFV/  

## Definition
Cryptographically verifying peripheral firmware integrity.

## Parent Class(es)
- Firmware Verification

## Relationships
- **kb-reference:** Reference - Firmware Verification Eclypsium
- **kb-reference:** Reference - Firmware Verification Trapezoid
- **verifies:** Peripheral Firmware

## Knowledge Base Article
# How it works
Peripheral firmware is collected and  analyzed on a host either periodically or on demand. This information may be collected for future comparisons.

Changes in firmware hash values may indicate that the firmware has been tampered with or that firmware images are not maintained to current baselined versions, or even known vulnerable versions are deployed.

## Considerations
* Trust baselines will need to be generated for specific devices
* Changes to trusted configurations will need to be managed across the enterprise


---

# D3-PAM: Physical Access Mediation

**Synonym(s):** Physical Access Control  
**Reference:** https://d3fend.mitre.org/technique/D3-PAM/  

## Definition
Physical access mediation is the process of granting or denying specific requests to enter specific physical facilities (e.g., Federal buildings, military establishments, border crossing entrances.)

## Parent Class(es)
- Access Mediation

## Relationships
- **isolates:** Physical Artifact
- **kb-reference:** Reference - Committee on National Security Systems (CNSS) Glossary
- **mediates-access-to:** Physical Artifact


---

# D3-PHAM: Physical Access Monitoring

**Reference:** https://d3fend.mitre.org/technique/D3-PHAM/  

## Definition
Monitoring the physical access of a specified environment through detection, recording, reviewing, and logging of who/what enters and exists areas.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Detect
- **kb-reference:** Reference - NIST Special Publication 800-53 Revision 5: Security and Privacy Controls for Information Systems and Organizations


---

# D3-PEH: Physical Enclosure Hardening

**Reference:** https://d3fend.mitre.org/technique/D3-PEH/  

## Definition
Physical changes to a computer enclosure which reduce the ability for agents or the environment to affect the contained computer system.

## Parent Class(es)
- Platform Hardening

## Relationships
- **hardens:** Computer Enclosure
- **kb-reference:** Reference - REGULATORY GUIDE 5.12 GENERAL USE OF LOCKS IN THE PROTECTION AND CONTROL OF: FACILITIES, RADIOACTIVE MATERIALS, CLASSIFIED INFORMATION, CLASSIFIED MATTER, AND SAFEGUARDS INFORMATION
- **kb-reference:** Reference - NIST SP 800-82R3 Guide to Operational Technology (OT) Security, Section 6.2.1.4.5 Password Authentication

## Knowledge Base Article
## How it works

System designers or operators make physical changes to a computer enclosure which reduce the ability for agents or the environment to affect the contained computer system. These additions to the enclosure may be of various materials to reduce the effects of heat, gases, vibration, or agent access.

## Considerations

* Use asset inventory tools to track physical equipment and monitor both people and devices for access control.
* Consider relevant regulations to ensure enclosures are in compliance.

* Properly hardened enclosures should be installed and maintained to ensure they are operable and free of tampering. Access to these enclosures is controlled through physical barriers, such as locks and bolts, and may include tamper-evident hardware.

* Records should be maintained concerning maintenance performed, access, and any possible tampering marks or associated incidents.


---

# D3-PLM: Physical Link Mapping

**Synonym(s):** Layer 1 Mapping  
**Reference:** https://d3fend.mitre.org/technique/D3-PLM/  

## Definition
Physical link mapping identifies and models the link connectivity of the network devices within a physical network.

## Parent Class(es)
- Network Mapping

## Relationships
- **kb-reference:** Reference - Libre NMS - Network Map Extension
- **maps:** Network Node
- **maps:** Physical Link


---

# D3-EPL: Physical Locking

**Reference:** https://d3fend.mitre.org/technique/D3-EPL/  

## Definition
Employ a mechanical locking device for securing moveable portions of physical barriers (e.g., doors, gates, drawers) in a secured position.

## Parent Class(es)
- Physical Access Mediation

## Relationships
- **kb-reference:** Reference - REGULATORY GUIDE 5.12 GENERAL USE OF LOCKS IN THE PROTECTION AND CONTROL OF: FACILITIES, RADIOACTIVE MATERIALS, CLASSIFIED INFORMATION, CLASSIFIED MATTER, AND SAFEGUARDS INFORMATION
- **kb-reference:** Reference - NIST SP 800-82R3 Guide to Operational Technology (OT) Security, Section 6.2.1.4.5 Password Authentication
- **mediates-access-to:** Computer Enclosure

## Knowledge Base Article
## How it works

A physical mechanism which has a associated credential which when entered enables the lock bolt to operate, i.e. open or close.

## Considerations

* Consider that locks for specified materials should adhere to relevant regulations.

* Lock equipment cabinets when not needed for operation or safety; set OT asset keys of devices (e.g., PLCs and safety systems) to the “RUN” position unless otherwise specified.

* Locks and all associated hardware should be properly installed, operable, and free of substantive indications of tampering.

* Records should be maintained concerning maintenance performed, access, and any possible tampering marks or associated incidents.

* For locks operated by a physical key, a key management system should be implemented to manage and secure physical keys.

* Key locks should provide a high degree of resistance to opening by force and tampering techniques.


---

# D3-PH: Platform Hardening

**Synonym(s):** Endpoint Hardening, System Hardening  
**Reference:** https://d3fend.mitre.org/technique/D3-PH/  

## Definition
Hardening components of a Platform with the intention of making them more difficult to exploit.

Platforms includes components such as:
* BIOS UEFI Subsystems
* Hardware security devices such as Trusted Platform Modules
* Boot process logic or code
* Kernel software components

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Harden


---

# D3-PM: Platform Monitoring

**Reference:** https://d3fend.mitre.org/technique/D3-PM/  

## Definition
Monitoring platform components such as operating systems software, hardware devices, or firmware.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Detect

## Knowledge Base Article
Platform monitoring consists of the analysis and monitoring of system level devices and low-level components, including hardware devices, to detect unauthorized modifications or suspicious activity.

Monitored platform components includes system files and embedded devices such as:

 * Kernel software modules
 * Boot process code and load logic
 * Operating system components and device files
 * System libraries and dynamically loaded files
 * Hardware device drivers
 * Embedded firmware devices


---

# D3-PUM: Platform Uptime Monitoring

**Reference:** https://d3fend.mitre.org/technique/D3-PUM/  

## Definition
Monitor the amount of time since the last power cycle or restart.

## Parent Class(es)
- Platform Monitoring

## Relationships
- **kb-reference:** Reference - Secure PLC Coding Practices: Top 20 List
- **monitors:** Platform Uptime

## Knowledge Base Article
## How it works
Monitoring the time since the last power cycle or restart alerts operators to unexpected restarts and their frequency. This can indicate potential issues or malicious activity, and provides valuable information for forensic investigations.

## Considerations
The source of the variable may be mutable depending on the platform, and the provenance of the value.


---

# D3-PAN: Pointer Authentication

**Reference:** https://d3fend.mitre.org/technique/D3-PAN/  

## Definition
Comparing the cryptographic hash or derivative of a pointer's value to an expected value.

## Parent Class(es)
- Application Hardening

## Relationships
- **authenticates:** Pointer
- **kb-reference:** Reference - Pointer Authentication on ARMv8.3
- **kb-reference:** Reference - Pointer Authentication Project Zero

## Knowledge Base Article
## How It Works

Pointer Authentication (frequently referred to as PAC, although the technique is properly Pointer Authentication) is a security feature to provide protection against attackers with memory read/write access.  A Pointer Authentication Code (PAC) is a cryptographic hash or derivative computed on the value of a pointer and some additional context information which can then provide a cryptographically strong guarantee about the likelihood that a pointer has been tampered with by an attacker.

Although pointers are 64 bits, most systems have a substantially smaller virtual address space, leaving unused bits in pointers that can store the value of the PAC, this can be done to reduce memory space requirements. One implementation is in ARMv8.3-A.  A PAC is computed over the 64-bit pointer value and a 64-bit context value.  Instructions are introduced to deal with pointers: one category to compute and insert the PAC into a pointer, another category to verify the pointer and invalidate the pointer if the PAC does not check, and a third category to remove the pointer and restore the original value without verifying.

The ARM standard specifies a cryptographic algorithm called QARMA-64 (designed by Qualcomm) to compute the signature, although this algorithm is not required.  The architecture provides for five secret 128-bit Pointer Authentication keys: two for instruction pointers, two for data pointers, and a general key for signing larger blocks of data.

## Considerations

In the ARM implementation, the mechanisms above for manipulating PACS are provided, but it is up to the code developer to manage the keys for the cryptographic algorithm.


A known potential limitation of PACs concerns signing gadgets. Under certain circumstances PACs can be bypassed by forcing the system to run a signing gadget which will allow the signing of arbitrary pointers to occur.


---

# D3-PV: Pointer Validation

**Reference:** https://d3fend.mitre.org/technique/D3-PV/  

## Definition
Ensuring that a pointer variable has the required properties for use.

## Parent Class(es)
- Source Code Hardening

## Relationships
- **kb-reference:** Reference - Pointer Validation Function - SEI


---

# D3-PA: Process Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-PA/  

## Definition
Process Analysis consists of observing a running application process and analyzing it to watch for certain behaviors or conditions which may indicate adversary activity. Analysis can occur inside of the process or through a third-party monitoring application. Examples include monitoring system and privileged calls, monitoring process initiation chains, and memory boundary allocations.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Detect


---

# D3-PCSV: Process Code Segment Verification

**Reference:** https://d3fend.mitre.org/technique/D3-PCSV/  

## Definition
Comparing the "text" or "code" memory segments to a source of truth.

## Parent Class(es)
- Process Analysis

## Relationships
- **kb-reference:** Reference - Anti-tamper system with self-adjusting guards - ARXAN TECHNOLOGIES Inc
- **kb-reference:** Reference - Guards for application in software tamperproofing - Purdue Research Foundation
- **kb-reference:** Reference - System and method for detecting malware injected into memory of a computing device - Endgame Inc
- **kb-reference:** Reference - System and method for validating in-memory integrity of executable files to identify malicious activity - Endgame Inc
- **kb-reference:** Reference - Tamper proof mutating software - ARXAN TECHNOLOGIES Inc
- **kb-reference:** Reference - Threat detection through the accumulated detection of threat characteristics - Sophos Ltd
- **verifies:** Process Code Segment

## Knowledge Base Article
## How it works
A process code segment is an executable portion of computer memory allocated to a particular process. Process Code Segment Verification implements verification to compare a process code segment to some expected value.

### Verification logic
Verification can occur during application startup, or continuously during execution. The logic which verifies the process code may be separate in a third-party process, embedded in the application itself at compile time, or dynamically linked at runtime.

### System of record
Examples of systems of record:

 * On-disk application binary files or checksums
 * Remotely stored binary data or checksums
 * Embedded binary data or checksums

### Post Verification Actions
If the verification function determines a process code segment may have been altered, a capability may invoke Eviction techniques  as **Process Termination** to end the current process, or **Executable Blacklisting** to prevent the executable from launching in the future.

## Considerations

### False positives

False positives commonly occur in the case that the layout of code in the process segment is legitimately modified:

*  Operating system features or third-party security software may modify the layout of process code, for example in the defensive technique **Segment Address Offset Randomization**, or in the case that a module is rebased.  In both of these cases, the alteration occurs before the code is fully loaded into memory, and it would be possible to avoid the false positive by securely feeding this constant offset and any relocation data into the verification logic.

* Process code segments may be written to modify themselves or other process code segments; however, this goes against widely-accepted current practices in software development.

### False negatives

False negatives can occur via alteration of the verification logic or source of truth, or insufficient verification logic.

* Verification techniques which are executed only locally may be defeated by altering the local verification logic.

* Verification that is run only on a recurring basis could be evaded if the malicious alteration is completed before verification is run.

* Verification that requests an operation to be performed on a subset of the code segment could be evaded by performing that operation on a copy of the relevant bytes of the code segment.

* Verification based on a system of record that can be altered may fail if that system of record is modifiable by a malicious user.


---

# D3-PE: Process Eviction

**Reference:** https://d3fend.mitre.org/technique/D3-PE/  

## Definition
Process eviction techniques terminate or remove running process.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Evict
- **kb-reference:** Reference - Malware detection using local computational models - Crowdstrike Inc


---

# D3-PLA: Process Lineage Analysis

**Synonym(s):** Process Tree Analysis  
**Reference:** https://d3fend.mitre.org/technique/D3-PLA/  

## Definition
Identification of suspicious processes executing on an end-point device by examining the ancestry and siblings of a process, and the associated metadata of each node on the tree, such as process execution, duration, and order relative to siblings and ancestors.

## Parent Class(es)
- Process Spawn Analysis

## Relationships
- **analyzes:** Process
- **analyzes:** Process Tree
- **kb-reference:** Reference - CAR-2020-11-002: Local Network Sniffing - MITRE
- **kb-reference:** Reference - CAR-2020-11-004: Processes Started From Irregular Parent - MITRE
- **kb-reference:** Reference - CAR-2021-02-002: Get System Elevation - MITRE
- **kb-reference:** Reference - CAR-2021-05-003: BCDEdit Failure Recovery Modification - MITRE
- **kb-reference:** Reference - CAR-2014-11-008: Command Launched from WinLogon - MITRE
- **kb-reference:** Reference - CAR-2014-11-003: Debuggers for Accessibility Applications - MITRE
- **kb-reference:** Reference - CAR-2019-04-002: Generic Regsvr32 - MITRE
- **kb-reference:** Reference - CAR-2014-11-002: Outlier Parents of Cmd - MITRE
- **kb-reference:** Reference - CAR-2013-02-003: Processes Spawning cmd.exe - MITRE
- **kb-reference:** Reference - CAR-2013-04-002: Quick execution of a series of suspicious commands - MITRE
- **kb-reference:** Reference - CAR-2013-03-001: Reg.exe called from Command Shell - MITRE
- **kb-reference:** Reference - CAR-2014-12-001: Remotely Launched Executables via WMI - MITRE
- **kb-reference:** Reference - CAR-2013-09-005: Service Outlier Executables - MITRE
- **kb-reference:** Reference - CAR-2014-07-001: Service Search Path Interception - MITRE
- **kb-reference:** Reference - CAR-2014-05-002: Services launching Cmd - MITRE
- **kb-reference:** Reference - System and methods thereof for causality identification and attributions determination of processes in a network - Palo Alto Networks IncCyber Secdo Ltd
- **kb-reference:** Reference - System and methods thereof for identification of suspicious system processes - Palo Alto Networks Inc
- **kb-reference:** Reference - CAR-2019-04-001: UAC Bypass - MITRE

## Knowledge Base Article
## How it works
Process tree analysis techniques gather information on how a process was initiated to determine if a process is malicious. For example, if a process was not initiated from boot or not initiated by another process, that process is identified as suspicious. Also, if a new process was started before a process initiated by the device (ex. during boot) and that new process was not initiated by a user (which can be determined by examining process parameters such as type of process, its creator, source, etc.) the process is identified as suspicious.

For example, Microsoft Word may block execution of any subprocess that is not in an approved path.

## Considerations
* Attackers may spoof the parent PID (https://attack.mitre.org/techniques/T1502/), rendering such after-the-fact analysis on process lineage ineffective.
* Processes may hide from various means of detection; an example on Linux is where a rootkit might remove key files for the process from its directory in /proc.
* Zombie processes.


---

# D3-PSEP: Process Segment Execution Prevention

**Synonym(s):** Execute Disable, No Execute  
**Reference:** https://d3fend.mitre.org/technique/D3-PSEP/  

## Definition
Preventing execution of any address in a memory region other than the code segment.

## Parent Class(es)
- Application Hardening

## Relationships
- **kb-reference:** Reference - Mitigate threats by using Windows 10 security features: Data Execution Prevention - Microsoft
- **kb-reference:** Reference - What is NX/XD feature?
- **neutralizes:** Process Segment

## Knowledge Base Article
## How it works

During execution of a process, the instruction pointer register should only point to addresses in a code segment (also called the .text segment), as this is the sole segment which should contain program code.

When this technique detects an attempt to execute something that has been designated as non-executable, other techniques such as those in **Process Eviction** might be invoked, such as **Process Termination** to end the current process, or **Executable Blacklisting** to blacklist the potentially vulnerable or malfunctioning executable.

### Software-based implementations
The software-based implementation in Windows XP SP2 might not check that every time the instruction pointer is changed, and does not check on each jump or return.  Before calling an exception handler, Windows XP SP2 software-enforced DEP checks whether the exception handler is located in a memory region marked as executable.  If the program was also built with SafeSEH, this implementation also checks before changing control to the exception handler whether it is a registered exception handler in the program's file on disk.

### Hardware-based implementations
The NX (No Execute) or XD (Execute Disable) bit on the processor specifies whether a certain part of memory is executable.  Early implementations set this bit by the memory segment, while modern implementations which are built on the flat memory model often store this bit in each entry of the page table, to control execution by the page.


## Considerations

Non-hardware process data segment execution prevention is more susceptible to being able to be turned off for a page of memory.

Different implementations of this defense have been in place since the 1980s, but implementation stalled when larger 16-bit programs began stuffing code in the segments usually reserved for data. Many modern programs follow the best practice of separation of code and data, are able to run under this defense.

ROP or ret2libc/return-to-function attacks could bypass this defense, as although they may pass attacker-controlled data or stack frames to a function, they abuse functions that are legitimately located in the .text segment (code segment) of the program.  For those, more advanced defenses such as a table of valid jump addresses, function call analysis, or return depth analysis could be used.


---

# D3-PSMD: Process Self-Modification Detection

**Reference:** https://d3fend.mitre.org/technique/D3-PSMD/  

## Definition
Detects processes that modify, change, or replace their own code at runtime.

## Parent Class(es)
- Process Analysis

## Relationships
- **analyzes:** Process
- **kb-reference:** Reference - System and Method for Process Hollowing Detection - Carbon Black Inc

## Knowledge Base Article
## How it Works
A security agent installed on the host machine intercepts API calls between a process and operating system. Intercepted API calls are then compared against attack signatures/patterns to identify API calls that modify executable memory or modify the entry point address of a suspended child process. Attack patterns include:

* Executable code of a suspended child process removed from memory by one or more API calls.
* New executable code injected and / or loaded into memory of a suspended child process by one or more API calls.
* Executable code modified by one or more API calls.
* Next instruction pointer value in memory modified by one or more API calls.

## Considerations
Comparing loaded code segments of processes with what is expected to have been loaded from a file can result in false positives, due to legitimate uses of self-modification for decrypting or uncompressing code segments.


---

# D3-PSA: Process Spawn Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-PSA/  

## Definition
Analyzing spawn arguments or attributes of a process to detect processes that are unauthorized.

## Parent Class(es)
- Process Analysis

## Relationships
- **analyzes:** Create Process
- **analyzes:** Process
- **kb-reference:** Reference - CAR-2019-08-002: Active Directory Dumping via NTDSUtil - MITRE
- **kb-reference:** Reference - CAR-2020-04-001: Shadow Copy Deletion - MITRE
- **kb-reference:** Reference - CAR-2020-05-003: Rare LolBAS Command Lines - MITRE
- **kb-reference:** Reference - CAR-2020-08-001: NTFS Alternate Data Stream Execution - System Utilities - MITRE
- **kb-reference:** Reference - CAR-2020-09-003: Indicator Blocking - Driver Unloaded - MITRE
- **kb-reference:** Reference - CAR-2020-09-004: Credentials in Files & Registry - MITRE
- **kb-reference:** Reference - CAR-2020-11-001: Boot or Logon Initialization Scripts - MITRE
- **kb-reference:** Reference - CAR-2020-11-003: DLL Injection with Mavinject - MITRE
- **kb-reference:** Reference - CAR-2020-11-005: Clear Powershell Console Command History - MITRE
- **kb-reference:** Reference - CAR-2020-11-006: Local Permission Group Discovery - MITRE
- **kb-reference:** Reference - CAR-2020-11-007: Network Share Connection Removal - MITRE
- **kb-reference:** Reference - CAR-2020-11-008: MSBuild and msxsl - MITRE
- **kb-reference:** Reference - CAR-2020-11-009: Compiled HTML Access - MITRE
- **kb-reference:** Reference - CAR-2021-01-002: Unusually Long Command Line Strings - MITRE
- **kb-reference:** Reference - CAR-2021-01-003: Clearing Windows Logs with Wevtutil - MITRE
- **kb-reference:** Reference - CAR-2021-01-004: Unusual Child Process for Spoolsv.Exe or Connhost.Exe - MITRE
- **kb-reference:** Reference - CAR-2021-01-006: Unusual Child Process spawned using DDE exploit - MITRE
- **kb-reference:** Reference - CAR-2021-01-007: Detecting Tampering of Windows Defender Command Prompt - MITRE
- **kb-reference:** Reference - CAR-2021-01-008: Disable UAC - MITRE
- **kb-reference:** Reference - CAR-2021-01-009: Detecting Shadow Copy Deletion via Vssadmin.exe - MITRE
- **kb-reference:** Reference - CAR-2021-02-001: Webshell-Indicative Process Tree - MITRE
- **kb-reference:** Reference - CAR-2021-04-001: Common Windows Process Masquerading - MITRE
- **kb-reference:** Reference - CAR-2021-05-001: Attempt To Add Certificate To Untrusted Store - MITRE
- **kb-reference:** Reference - CAR-2021-05-002: Batch File Write to System32 - MITRE
- **kb-reference:** Reference - CAR-2021-05-003: BCDEdit Failure Recovery Modification - MITRE
- **kb-reference:** Reference - CAR-2021-05-004: BITS Job Persistence - MITRE
- **kb-reference:** Reference - CAR-2021-05-005: BITSAdmin Download File - MITRE
- **kb-reference:** Reference - CAR-2021-05-006: CertUtil Download With URLCache and Split Arguments - MITRE
- **kb-reference:** Reference - CAR-2021-05-007: CertUtil Download With VerifyCtl and Split Arguments - MITRE
- **kb-reference:** Reference - CAR-2021-05-008: Certutil exe certificate extraction - MITRE
- **kb-reference:** Reference - CAR-2021-05-009: CertUtil With Decode Argument - MITRE
- **kb-reference:** Reference - CAR-2021-05-010: Create local admin accounts using net exe - MITRE
- **kb-reference:** Reference - CAR-2013-07-005: Command Line Usage of Archiving Software - MITRE
- **kb-reference:** Reference - CAR-2016-03-002: Create Remote Process via WMIC - MITRE
- **kb-reference:** Reference - CAR-2019-04-004: Credential Dumping via Mimikatz - MITRE
- **kb-reference:** Reference - CAR-2016-03-001: Host Discovery Commands - MITRE
- **kb-reference:** Reference - CAR-2019-07-002: Lsass Process Dump via Procdump - MITRE
- **kb-reference:** Reference - CAR-2014-04-003: Powershell Execution - MITRE
- **kb-reference:** Reference - CAR-2014-03-006: RunDLL32.exe monitoring - MITRE
- **kb-reference:** Reference - CAR-2019-04-003: Squiblydoo - MITRE
- **kb-reference:** Reference - CAR-2013-07-001: Suspicious Arguments - MITRE
- **kb-reference:** Reference - CAR-2013-05-002: Suspicious Run Locations - MITRE

## Knowledge Base Article
## How it works
Process attributes are established when an operating system spawns a new process. These attributes are analyzed to look for the presence or absence of specific values or patterns.

Some attributes of interest are:
 - user
 - process name
 - image path
 - security content

## Considerations

 - Attackers can spoof the parent process identifier (PPID), which could bypass this defense to allow execution of a malicious process from an arbitrary parent process.
 - Attackers could have legitimately compromised any of the process properties, such as the user, to make the execution appear legitimate.
 - Location: If the full image path is not checked, there could be a conflict with an executable that appears earlier due to resolution involving the system environment path/classpath variable.
 - Parsing issues: If the raw command from a shell is analyzed, rather than the actual function call, it is important to identify the actual command  being run from its arguments.  In Windows, services with unquoted file paths containing spaces will try to use the first token as the executable and the rest as arguments -- and shift tokens to the executable until a valid one is found.
 - Some [operating systems](/dao/artifact/d3f:OperatingSystem) can spawn processes without forking.


---

# D3-PS: Process Suspension

**Reference:** https://d3fend.mitre.org/technique/D3-PS/  

## Definition
Suspending a running process on a computer system.

## Parent Class(es)
- Process Eviction

## Relationships
- **kb-reference:** Reference - PsSuspend - Microsoft
- **suspends:** Process

## Knowledge Base Article
## How it works

A running process might be suspended to mitigate its immediate effects if it is exhibiting anomalous, unauthorized, or malicious behavior. Defenders may choose to suspend rather than terminate to analyze the process first and resume the process if deemed benign.

### System-provided functions

#### Windows tools
In Windows, the `PsSuspend` command line utility from the SysInternals Suite provides functionality to suspend processes on a local or remote system.


---

# D3-PT: Process Termination

**Reference:** https://d3fend.mitre.org/technique/D3-PT/  

## Definition
Terminating a running application process on a computer system.

## Parent Class(es)
- Process Eviction

## Relationships
- **kb-reference:** Reference - Instant process termination tool to recover control of an information handling system - Dell Products LP
- **kb-reference:** Reference - Malware detection using local computational models - Crowdstrike Inc
- **terminates:** Process

## Knowledge Base Article
## How it works

Processes are managed by the operating system kernel.  Different operating system kernels manage the creation and termination of processes in a different manner, and expose this functionality via the kernel API.

A running process might be terminated to mitigate its immediate effects if it is exhibiting anomalous, unauthorized, or malicious behavior; such as after detecting anomalous behavior via <a href="https://d3fend.mitre.org/technique/d3f:AdministrativeNetworkActivityAnalysis" rdf:about="https://d3fend.mitre.org/ontologies/d3fend.owl#AdministrativeNetworkActivityAnalysis">Administrative Network Activity Analysis</a>, after a failed check from <a href="https://d3fend.mitre.org/technique/d3f:StackFrameCanaryVerification" rdf:about="https://d3fend.mitre.org/ontologies/d3fend.owl#StackFrameCanaryValidation">Stack Frame Canary Validation</a>, or after <a href="https://d3fend.mitre.org/technique/d3f:SystemCallAnalysis" rdf:about="https://d3fend.mitre.org/ontologies/d3fend.owl#SystemCallAnalysis">System Call Analysis</a> finds an attempt to execute an unauthorized system call.

### Proprietary technology
Security software might use proprietary technology to terminate processes, instead of the system-provided functions.    Further research may provide specific detail on such methods used.

### System-provided functions

#### Windows tools
In Windows, `ExitProcess()` is used to send a signal to a process to request it to exit, and `TerminateProcess()` is used to force a process to exit.

The `taskkill` executable available in the cmd shell is used to kill a process, with the `/F` switch forcing termination as with `TerminateProcess()`.  In PowerShell, `Stop-Process` is used, which is aliased by default to `spps` and `kill`.  Processes started in the Windows Subsystem for Linux (WSL) environment may be terminated there with the `kill` command.

In some cases, existing drivers can also be leveraged to kill processes.

#### Unix/Linux tools
In Unix-like systems, all process termination requests are handled using signals.  The `kill` function takes the Process ID and signal to send, and is accessible with the `kill` command.  Some shells have a `kill` builtin function which is separate than the `kill` binary, which can also kill background jobs in the shell and additionally perform the function faster, and can run from an existing instance of the shell if the process table is full.  The signal SIGTERM specifies that the process to terminate may invoke a handler that it has defined instead of terminating, and the signal SIGKILL forces immediate termination.

The related command `xkill` terminates the connection of a program to the X window server, after which the user process may decide to terminate itself; however, termination is not guaranteed as the process, which could be on the same or different host, could then run in a terminal or reconnect to a different X server on any host.  Emacs is such a program that would not terminate itself after its connection to the X server is terminated.

## Considerations

### Persistence Mechanisms
Terminating a malicious process is not enough to stop an adversary that has already gained persistence in the host via any initial access mechanism, including through that process or another access mechanism.

### Terminating Multiple Processes
On most operating systems, process termination operations typically occur independently of each other, without functionality provided to atomically terminate multiple processes.  If there are multiple malicious processes which can make system calls to spawn other processes once one of them is closed, user session termination or system restart might be required.

### Process Access Permissions
Users must have permissions to kill the process.  On Unix-like systems, either root or the process user can kill the process.  On Windows systems, process permissions are managed separately via process security tokens.

### Process Resource Handles

#### Terminating Processes with Open Resource Handles

Processes may have open resource handles, which could leave those resources in an undesired state if the process is forced to terminate.  As such, most operating systems provide a means to send a signal to a process to inform it to gracefully terminate, and on most of these operating systems, it is the typical first step used to terminate a process.

#### Signal Traps
As the process may have open resource handles, commonly-used methods of process termination involve sending a signal to the process to terminate.
On Windows, the `ExitProcess()` function is used for this purpose.  Process instructions, as well as a third-party DLL can also cause the process to exit.
On Linux, the process is sent a signal on the occurrence of various events: when it loses the console, `SIGHUP`; when termination is requested, `SIGTERM`.  The processor then redirects execution to the function registered to handle the signal.

Therefore, sending a signal to the process to ask it to terminate may not always work.

##### Avoiding Signal Traps

On Unix-like systems, sending the `SIGKILL` signal for a process does not send a message to the process or invoke an implementation-defined handler; instead, it immediately does not allow the process to execute any further processor instructions.   On Windows `TerminateProcess()` instead of `ExitProcess()` performs the equivalent.

#### Hang on System Call Execution

Even still, as the operating system kernel manages the processes, kernel code may block process signals, including those which cannot be trapped, and does in certain circumstances.  Signals are blocked and queued for the duration of the system call when interrupting the system call would result in a kernel invariant being violated, such as when an action results in a malformed data structure; this blocking is common for filesystem requests.  Such system calls can hang when a filesystem has gone offline, leading to a long-term uninterruptible sleep, represented in POSIX command `ps` output as D state.
Any malicious system calls or system call handlers are issues of a much larger problem (a kernel-level rootkit) and the system should be redeployed entirely or restored from a backup known to be prior to compromise, and other systems accessible directly and indirectly from that one should also be examined.

A process that is truly hung in a system call may prevent the system from shutting down and leave it in an unresponsive state; a hard power off is required.

To speed up the action of terminating a process in uninterruptible sleep, the process resource accesses (handles) could be analyzed.

On Linux, [`sync` followed by `echo 3 > /proc/sys/vm/drop_caches`](https://www.kernel.org/doc/Documentation/sysctl/vm.txt) is a safe way to free up some inactive resource handles.


#### Kernel Processes and Threads
The kernel may not allow kernel processes, which are created via methods other than user-space processes, to be terminated.

#### Other Code using the Process

Terminating a shared library can lead to unexpected errors; such shared libraries have their own mechanisms for termination.

On Windows, a DLL is unloaded when the reference count of the library reaches 0.

#### Zombie process

After a process has been terminated, it may still take up an entry in the operating system process table until another event occurs.

##### Windows
In Windows, a process object is deleted when the last handle to the process is closed.

##### Linux
In Linux, a process is removed from the process table when it is reaped by its parent process.  If the parent terminates, historically the parent has been changed to pid 1; however, in the Linux kernel 3.4 and above, processes can set a different process as the subreaper using the `prctl()` system call.

Zombie processes and hung processes could be resolved with a restart of the system.

#### System restart
Finally a system restart might be required to kill a process.
Systems which are only accessible via a remote in-band connection may become inaccessible if a process termination operation that is necessary for reboot does not complete.

### Subsystems
Processes that are started in a subsystem might not be fully terminated if they are terminated using the command for that subsystem.  For example, in the Windows Subsystem for Linux (WSL), processes started and terminated via WSL calls such as with the `kill` command in Bash may still have an entry in the Windows process table.


---

# D3-PMAD: Protocol Metadata Anomaly Detection

**Reference:** https://d3fend.mitre.org/technique/D3-PMAD/  

## Definition
Collecting network communication protocol metadata and identifying statistical outliers.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Network Traffic
- **kb-reference:** Reference - Method and system for detecting threats using metadata vectors - VECTRA NETWORKS Inc
- **kb-reference:** Reference - Method and system for detecting threats using passive cluster mapping - Vectra Networks Inc
- **kb-reference:** Reference - System for implementing threat detection using daily network traffic community outliers - VECTRA NETWORKS Inc

## Knowledge Base Article
## How it works
Network protocol metadata is first collected and processed in real-time or post-facto. Metadata may include packet header information or information about a session (ex. time between requests/responses). Metadata is then grouped based on shared characteristics and those groups are compared to each other. If particular metadata differs significantly from other data, an alert is generated, identifying the network event as anomalous. Anomalous activity may indicate unauthorized activity.

## Considerations
Metadata collection on enterprises can yield large data sets. Storage, indexing, querying, and aging should be considered prior to implementation.


---

# D3-PSM: Proximity Sensor Monitoring

**Synonym(s):** Proximity Reader Monitoring, RFID Reader Monitoring  
**Reference:** https://d3fend.mitre.org/technique/D3-PSM/  

## Definition
Monitoring events from proximity sensors that indicate a credential or tagged asset is within the sensor’s read range or a defined zone. Common enabling technologies include RFID, Bluetooth Low Energy (BLE), and Ultra-Wideband (UWB).

## Parent Class(es)
- Physical Access Monitoring

## Relationships
- **kb-reference:** Reference - FIPS 201-3
- **kb-reference:** Reference - NIST SP 800-116 Rev. 1
- **kb-reference:** Reference - Wikipedia: Proximity card
- **kb-reference:** Reference - Wikipedia: RFID
- **monitors:** Proximity Sensor

## Knowledge Base Article
## How it works

Proximity readers and sensors detect credentials or tagged assets within their read field, then report presence and, when applicable, authenticate to a controller for access decisions. Systems may use RSSI, dwell time, or time-of-flight to enforce zones and policies such as anti-passback. Secure, authenticated communication between readers and controllers helps prevent cloning and replay attacks.

## Considerations

 * Place readers and align antennas to achieve consistent read ranges; account for materials like metal and liquids that can detune signals.
* Use cryptographic credentials with mutual authentication and encrypted, supervised reader links to mitigate cloning and relay attacks.
* Protect privacy by minimizing collected data, limiting retention, and restricting access to proximity logs.
* Calibrate detection thresholds and zone boundaries; re-test after layout changes or equipment moves.
* Monitor reader and tag health, including battery status for BLE and UWB tags and supervision signals for wired and wireless devices.


---

# D3-PBWSAM: Proxy-based Web Server Access Mediation

**Reference:** https://d3fend.mitre.org/technique/D3-PBWSAM/  

## Definition
Proxy-based web server access mediation focuses on the regulation of web server access through intermediary proxy servers.

## Parent Class(es)
- Web Session Access Mediation

## Relationships
- **kb-reference:** Reference - Special Publication 800-41 Revision 1 Guidelines on Firewalls and Firewall Policy

## Knowledge Base Article
## How it works

Proxy-based Web Server Access Mediation involves controlling access to web servers via proxy servers, which act as intermediaries between users and web resources. This approach can enhance security by anonymizing user requests, filtering content, and enforcing access policies. Examples include using corporate proxies to access external websites or services.


---

# D3-RFS: RF Shielding

**Reference:** https://d3fend.mitre.org/technique/D3-RFS/  

## Definition
Adding physical barriers to a platform to prevent undesired radio interference.

## Parent Class(es)
- Electromagnetic Radiation Hardening

## Relationships
- **kb-reference:** Reference - Privacy and security systems and methods of use
- **kb-reference:** Reference - Technical Specifications for Construction and Management of Sensitive Compartmented Information Facilities


---

# D3-RTA: RPC Traffic Analysis

**Synonym(s):** RPC Protocol Analysis  
**Reference:** https://d3fend.mitre.org/technique/D3-RTA/  

## Definition
Monitoring the activity of remote procedure calls in communication traffic to establish standard protocol operations and potential attacker activities.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** RPC Network Traffic
- **kb-reference:** Reference - CAR-2014-05-001: RPC Activity - MITRE
- **kb-reference:** Reference - CAR-2014-11-007: Remote Windows Management Instrumentation (WMI) over RPC - MITRE
- **kb-reference:** Reference - CAR-2016-03-002: Create Remote Process via WMIC - MITRE
- **kb-reference:** Reference - RPC call interception - Crowdstrike Inc
- **kb-reference:** Reference - CAR-2014-03-005: Remotely Launched Executables via Services - MITRE
- **kb-reference:** Reference - CAR-2014-12-001: Remotely Launched Executables via WMI - MITRE
- **kb-reference:** Reference - CAR-2015-04-002: Remotely Scheduled Tasks via Schtasks - MITRE
- **kb-reference:** Reference - CAR-2014-03-001: SMB Write Request - NamedPipes - MITRE

## Knowledge Base Article
## How it works
A remote procedure call (RPC) enables one computer to execute a specific function on another computer, as if it were a local application process. There are numerous RPC specifications and implementations. RPC capabilities can be abused by attackers in order to achieve a variety of tactical objectives including execution, persistence, initial access, and more. RPC proxies may be used to collect and store RPC traffic. RPCs can occur over network sockets or named pipes.

Analytics look for unauthorized behavior such as:

* Processes being launched or scheduled remotely
* System configurations being changed remotely
* Unauthorized file read activity

Example RPC Protocols:

* DCE/RPC
* CORBA
* Open Network Computing Remote Procedure Call
* D-Bus
* XML-RPC
* JSON-RPC
* SOAP
* Apache Thrift

## Considerations
* RPC is widely used in enterprise environments, and significant data filtering may be required in large environments to enable analytic processing.
* RPC traffic may occur over a pipe, or within a host over loopback interface, thus making network collection difficult.


---

# D3-RH: Radiation Hardening

**Reference:** https://d3fend.mitre.org/technique/D3-RH/  

## Definition
Radiation hardening is the process of making electronic components and circuits resistant to damage or malfunction caused by high levels of ionizing radiation.

## Parent Class(es)
- Platform Hardening

## Relationships
- **hardens:** Hardware Device
- **kb-reference:** Reference - A Radiation-Hardened SAR ADC with Delay-Based Dual Feedback Flip-Flops for Sensor Readout Systems
- **kb-reference:** Reference - Diagnosis of Faults Induced by Radiation and Circuit-Level Design Mitigation Techniques: Experience from VCO and High-Speed Driver CMOS ICs Case Studies
- **kb-reference:** Reference - Method of making thin atomic (Z) grade shields - NASA

## Knowledge Base Article
## How it works

There are three core radiation hardening methodologies:

1. Radiation Hardening by Process (RHBP): modifying the physical fabrication of a semiconductor (e.g., using SOI - Silicon on Insulator), offering the highest intrinsic protection. Usually the most expensive option as it requires a specialized semiconductor fabrication plant.
2. Radiation Hardening by Design (RHBD): modifying circuit topology and physical layout using techniques such as Triple Modular Redundancy (TMR). A more cost-effective option, with the constraint of potentially increasing chip area and power.
3. Radiation Hardening by Shielding (RHBS): using physical materials (e.g., aluminum or tantalum) to block ionizing particles. Simple to implement, with the constraint of increasing size and weight.


---

# D3-RN: Reference Nullification

**Reference:** https://d3fend.mitre.org/technique/D3-RN/  

## Definition
Invalidating all pointers that reference a specific memory block, ensuring that the block cannot be accessed or modified after deallocation.

## Parent Class(es)
- Source Code Hardening

## Relationships
- **hardens:** Memory Free Function
- **kb-reference:** Reference - Reference Nullification

## Knowledge Base Article
## How it Works
Nullifying references to memory blocks makes those blocks no longer accessible. This is critical to prevent use-after-free errors.

## Considerations
* If a memory block is freed, all other references to that block should be nullified.
* This is particularly relevant when manually managing memory.
* Note: This resource should not be considered a definitive or exhaustive coding guideline.


---

# D3-RKD: Registry Key Deletion

**Reference:** https://d3fend.mitre.org/technique/D3-RKD/  

## Definition
Delete a registry key.

## Parent Class(es)
- Object Eviction

## Relationships
- **deletes:** Windows Registry Key
- **kb-reference:** Reference - Cybersecurity Incident and Vulnerability Response Playbooks


---

# D3-RIC: Reissue Credential

**Reference:** https://d3fend.mitre.org/technique/D3-RIC/  

## Definition
Issue a new credential to a user which supersedes their old credential.

## Parent Class(es)
- Restore Access

## Relationships
- **kb-reference:** Reference - Cybersecurity Incident and Vulnerability Response Playbooks
- **restores:** Credential


---

# D3-RPA: Relay Pattern Analysis

**Synonym(s):** Relay Network Detection  
**Reference:** https://d3fend.mitre.org/technique/D3-RPA/  

## Definition
The detection of an internal host relaying traffic between the internal network and the external network.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Outbound Internet Network Traffic
- **kb-reference:** Reference - Malicious relay detection on networks - VECTRA NETWORKS Inc

## Knowledge Base Article
## How it works
A relay may use a variety of proxying, forwarding, or routing technologies to bridge a protected network with an external network. A defensive analytic to detect a relay network may compare the network sessions among multiple hosts. Hosts which have nearly similar network statistics may be part of a relay network. The statistics may include number of bytes sent to and from, time of session initiation, packet size, or packet arrival time data.

## Considerations

Complex intranet VPNs or routing encapsulation may affect the detection analytics.  In addition, unwanted packets might not be forwarded, and additional packets may be added at the relay, further complicating detection.


---

# D3-RFAM: Remote File Access Mediation

**Synonym(s):** File Share Access Mediation  
**Reference:** https://d3fend.mitre.org/technique/D3-RFAM/  

## Definition
Remote file access mediation is the process of managing and securing access to file systems over a network to ensure that only authorized users or processes can interact with remote files.

## Parent Class(es)
- Network Resource Access Mediation

## Relationships
- **isolates:** File
- **kb-reference:** Reference - NIST Special Publication 800-53 Revision 5 - Security and Privacy Controls for Information Systems and Organizations

## Knowledge Base Article
## How it works

Remote File Access Mediation focuses on controlling how users or processes access file systems from remote locations. This involves ensuring secure connections, often through protocols like SFTP or SMB, and enforcing permissions to prevent unauthorized access or data breaches. Examples of enforcement areas include accessing shared drives or cloud storage from remote offices or home networks.


---

# D3-RFUM: Remote Firmware Update Monitoring

**Reference:** https://d3fend.mitre.org/technique/D3-RFUM/  

## Definition
Monitoring of remote firmware update commands to identify unauthorized software installations.

## Parent Class(es)
- Application Protocol Command Analysis

## Relationships
- **detects:** OT Device Firmware Command
- **kb-reference:** Reference - Method for detecting anomalies in time series data produced by devices of an infrastructure in a network
- **monitors:** OT Network Traffic

## Knowledge Base Article
## How it works
By deploying sensors within the OT environment to passively monitor network traffic, tools can leverage deep packet inspection to identify protocol-specific commands and generate logs of relevant firmware activity. Additionally, these tools may incorporate behavioral and signature-based analysis to enhance detection and alerting capabilities.


---

# D3-RTSD: Remote Terminal Session Detection

**Reference:** https://d3fend.mitre.org/technique/D3-RTSD/  

## Definition
Detection of an unauthorized remote live terminal console session by examining network traffic to a network host.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Network Traffic
- **kb-reference:** Reference - Method and system for detecting external control of compromised hosts - VECTRA NETWORKS Inc
- **kb-reference:** Reference - CAR-2013-07-002: RDP Connection Detection - MITRE
- **kb-reference:** Reference - CAR-2016-04-005: Remote Desktop Logon - MITRE

## Knowledge Base Article
## How it works
An external attacker takes remote control of a host inside a company or organization's network and manually directs offensive techniques. Nonstandard terminal sessions and abnormal behaviors are analyzed in this technique. Abnormal behavior detection includes analysis of user input patterns in the real-time session, keyboard output and packet inspection.

### Network Traffic Inspection
Network traffic from internal hosts is the main concern and focus for the traffic inspection. The network traffic is collected into inspection groups. The groups of traffic are assembled into distinct pair flows (outbound/inbound) and the pair flows are further divided into sessions. Only sessions originated inside of the network are considered for the inspection. Traffic inspection includes analysis to determine if a human is involved in the session exchanges. Time-based statistics are captured for each session being analyzed by the detection engine.

### Algorithm Analysis Description
Analysis algorithms look for patterns in the network traffic captured from the session data.  A detection engine groups the session traffic data, between the hosts, into rapid exchange instances. Analysis of rapid exchange traffic patterns can lead to the discovery of abnormal behavior which is indicative of a compromised internal host. The analysis algorithms look for patterns in the traffic which correlate to known activity (e.g., relay attacks, bot activity, bitcoin mining). Some metrics used during inspection include the following.

* Number of rapid-exchange instances
* Time interval between packets
* Fixed cadence of traffic
* Rhythm and direction of the initiation of instances
* Volume of data flowing from internal to external controlling host
* Data transfer characteristics
* Variability in length of silent periods

## Considerations
* Full packet capture is required which can be process intensive to analyze
* Attackers that move low and slow may blend in with existing traffic resulting in false negatives


---

# D3-RAPA: Resource Access Pattern Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-RAPA/  

## Definition
Analyzing the resources accessed by a user to identify unauthorized activity.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **analyzes:** Authentication
- **analyzes:** Authorization
- **kb-reference:** Reference - Host intrusion prevention system using software and user behavior analysis - Sophos Ltd
- **kb-reference:** Reference - Method and Apparatus for Network Fraud Detection and Remediation Through Analytics - Idaptive LLC
- **kb-reference:** Reference - Modeling user access to computer resources - Daedalus Group LLC (formerly IBM)
- **kb-reference:** Reference - System, method, and computer program product for detecting and assessing security risks in a network - Exabeam Inc
- **kb-reference:** Reference - System and method thereof for identifying and responding to security incidents based on preemptive forensics - Palo Alto Networks Inc

## Knowledge Base Article
## How it works
This technique analyzes a user's resource accesses by comparing the user's recent activity against a baseline activity model. Major differences between the current activity and the baseline model might indicate unauthorized activity if they are severe enough.


## Considerations
* Potential for false positives from anomalies that are not associated with malicious activity.
* Attackers that move low and slow may not differentiate their resource access activity behavior enough to trigger an alert.


---

# D3-RA: Restore Access

**Reference:** https://d3fend.mitre.org/technique/D3-RA/  

## Definition
Restoring an entity's access to resources.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Restore
- **kb-reference:** Reference - Cybersecurity Incident and Vulnerability Response Playbooks


---

# D3-RC: Restore Configuration

**Reference:** https://d3fend.mitre.org/technique/D3-RC/  

## Definition
Restoring an software configuration.

## Parent Class(es)
- Restore Object

## Relationships
- **kb-reference:** Reference - Cybersecurity Incident and Vulnerability Response Playbooks
- **restores:** Configuration Resource


---

# D3-RD: Restore Database

**Reference:** https://d3fend.mitre.org/technique/D3-RD/  

## Definition
Restoring the data in a database.

## Parent Class(es)
- Restore Object

## Relationships
- **kb-reference:** Reference - Cybersecurity Incident and Vulnerability Response Playbooks
- **restores:** Database


---

# D3-RDI: Restore Disk Image

**Reference:** https://d3fend.mitre.org/technique/D3-RDI/  

## Definition
Restoring a previously captured disk image a hard drive.

## Parent Class(es)
- Restore Object

## Relationships
- **kb-reference:** Reference - Cybersecurity Incident and Vulnerability Response Playbooks


---

# D3-RE: Restore Email

**Reference:** https://d3fend.mitre.org/technique/D3-RE/  

## Definition
Restoring an email for an entity to access.

## Parent Class(es)
- Restore File

## Relationships
- **kb-reference:** Reference - Cybersecurity Incident and Vulnerability Response Playbooks
- **restores:** Email


---

# D3-RF: Restore File

**Reference:** https://d3fend.mitre.org/technique/D3-RF/  

## Definition
Restoring a file for an entity to access.

## Parent Class(es)
- Restore Object

## Relationships
- **kb-reference:** Reference - Cybersecurity Incident and Vulnerability Response Playbooks
- **restores:** File


---

# D3-RNA: Restore Network Access

**Reference:** https://d3fend.mitre.org/technique/D3-RNA/  

## Definition
Restoring a entity's access to a computer network.

## Parent Class(es)
- Restore Access

## Relationships
- **kb-reference:** Reference - Cybersecurity Incident and Vulnerability Response Playbooks
- **restores:** Host


---

# D3-RO: Restore Object

**Reference:** https://d3fend.mitre.org/technique/D3-RO/  

## Definition
Restoring an object for an entity to access. This is the broadest class for object restoral.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Restore


---

# D3-RS: Restore Software

**Reference:** https://d3fend.mitre.org/technique/D3-RS/  

## Definition
Restoring software to a host.

## Parent Class(es)
- Restore Object

## Relationships
- **kb-reference:** Reference - Cybersecurity Incident and Vulnerability Response Playbooks
- **restores:** Software


---

# D3-RUAA: Restore User Account Access

**Reference:** https://d3fend.mitre.org/technique/D3-RUAA/  

## Definition
Restoring a user account's access to resources.

## Parent Class(es)
- Restore Access

## Relationships
- **kb-reference:** Reference - Cybersecurity Incident and Vulnerability Response Playbooks
- **restores:** User Account


---

# D3-RRID: Reverse Resolution IP Denylisting

**Synonym(s):** Reverse Resolution IP Blacklisting  
**Reference:** https://d3fend.mitre.org/technique/D3-RRID/  

## Definition
Blocking a reverse lookup based on the query's IP address value.

## Parent Class(es)
- DNS Denylisting

## Relationships
- **blocks:** Outbound Internet DNS Lookup Traffic
- **kb-reference:** Reference - Use DNS Policy for Applying Filters on DNS Queries

## Knowledge Base Article
## How it works
This technique prevents a client from learning domains deemed to be potentially malicious, which would have been delivered via reverse resolution responses over the DNS protocol.

Queries for reverse resolution requests (that is, requests where IP(s) are sent and a domain is returned) are collected, and the IP address(es) included in the query are examined. If the IP address(es) are in a range included in the blacklist, then the query is dropped.

## Considerations
- The blacklist will have to be maintained and will need to be kept up to date with identified maintenance cycles to ensure lists are not stale.
- DNS query traffic can be transmitted over many different protocols, which presents a challenge to implementing methods to extract all DNS query IP address value(s).
  - DNS has historically used UDP port 53, with TCP port 53 instead used for responses over 512 bytes or after a lack of response over UDP.
  - Usage of new protocols to provide confidentiality for DNS traffic, such as DoH (DNS over HTTPS) and DoT (DNS over TLS), complicates collection of the IP address(es) in DNS queries. These protocols have often been enabled in browser settings transparently after a browser update, with DNS queries proxied over one of these cryptographic protocols through a specified host.


---

# D3-RAM: Routing Access Mediation

**Reference:** https://d3fend.mitre.org/technique/D3-RAM/  

## Definition
Routing access mediation is a network security approach that manages and controls access at the network layer using VPNs, tunneling protocols, firewall rules, and traffic inspection to ensure secure and efficient data routing.

## Parent Class(es)
- Network Access Mediation

## Relationships
- **isolates:** Network
- **kb-reference:** Reference - What is Network Access Control?

## Knowledge Base Article
## How it works

Routing Access Mediation is a network security strategy focused on managing and controlling access at the network layer. It includes the use of VPNs for secure remote access, tunneling protocols for encapsulating data, firewall rules for filtering traffic, and advanced inspection techniques like Cisco's Context-Based Access Control (CBAC) to monitor and regulate data flow. This approach ensures secure and efficient routing of data across networks, protecting against unauthorized access and enhancing overall network security.


---

# D3-SJA: Scheduled Job Analysis

**Synonym(s):** Scheduled Job Execution  
**Reference:** https://d3fend.mitre.org/technique/D3-SJA/  

## Definition
Analysis of source files, processes, destination files, or destination servers associated with a scheduled job to detect unauthorized use of job scheduling.

## Parent Class(es)
- Operating System Monitoring

## Relationships
- **analyzes:** Job Schedule
- **kb-reference:** Reference - CAR-2013-05-004: Execution with AT - MITRE
- **kb-reference:** Reference - CAR-2013-08-001: Execution with schtasks - MITRE
- **kb-reference:** Reference - Preventing execution of task scheduled malware - McAfee LLC

## Knowledge Base Article
## How it works
Scheduled job execution can be utilized by adversaries for the purpose of persistence, conducting remote execution, or gaining privileges. Details of a scheduled job such as associated source files, processes, destination files, or destination servers are first identified and analyzed and then compared against an anti-malware signature database, whitelist, or reputation server. For example, a file associated with a scheduled job to be executed at a specified time or a remote server that is accessed as part of a scheduled task is compared against an anti-malware signature database, whitelist, or reputation server, and if a match is found, execution is denied and an alert is generated.

In addition to traditional scheduled jobs, triggers can be set to execute a specific command after detecting a specific event in the system, such as with WMI Event Subscriptions in Windows.

## Considerations
Jobs can be scheduled in many different and sometimes creative ways through operating system capabilities.


---

# D3-SEA: Script Execution Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-SEA/  

## Definition
Analyzing the execution of a script to detect unauthorized user activity.

## Parent Class(es)
- Process Analysis

## Relationships
- **analyzes:** Script Application Process
- **kb-reference:** Reference - Detecting script-based malware - Crowdstrike Inc

## Knowledge Base Article
## How it works
Software installed on the host system hooks into a scripting engine to intercept commands before they are executed and block commands if they are determined to be harmful. Pattern matching is used to identify unauthorized commands or in the case of script files, a hash of the file is compared against hashes of known unauthorized script files.

## Considerations
List of known unauthorized script files or regular expression patterns must be kept up to date to ensure detection of new threats.


---

# D3-SAOR: Segment Address Offset Randomization

**Synonym(s):** ASLR, Address Space Layout Randomization  
**Reference:** https://d3fend.mitre.org/technique/D3-SAOR/  

## Definition
Randomizing the base (start) address of one or more segments of memory during the initialization of a process.

## Parent Class(es)
- Application Hardening

## Relationships
- **kb-reference:** Reference - /DYNAMICBASE (Use address space layout randomization) - Microsoft Docs
- **kb-reference:** Reference - How ASLR protects Linux systems from buffer overflow attacks - Network World
- **obfuscates:** Process Segment

## Knowledge Base Article
## How it works

Many application exploits rely on an attacker specifying a location in memory, which points to data or code used by the attacker.  If the addresses are changed each time the program is run, then it becomes more difficult for the attacker to determine the location that will contain the code they wish to run.

Imported modules may be similarly realigned if their default memory addresses conflict with other modules, in a process known as "rebasing."  Just as not all code is built for participation in ASLR, not all modules can be rebased; instead, modules must indicate whether they implement support for rebasing.  Such information to relocate the executable is typically stored in the ".reloc" segment -- each of the addresses pointed to in this segment has its address increased by the amount of the offset.
(An alternative method for relocation would be to add an amount to a global variable each time -- leading to less overhead in the module load, but more for each access.  Still another implementation could instead contain code to deference each changeable memory location on the fly, so that each of the references do not need to be updated.


## Considerations

As the offset for each segment is constant, it is possible to guess at the value of the address given the address of another variable.  Alternatively, memory pointers may be kept around, which contain the address of another variable.
Another bypass technique is known as an "egg hunt," whereby the attacker searches for a rather unique piece of the data or code in memory to determine its likely address.

The program needs to store these addresses for the functions somewhere.  In Linux, the PLT contains a "trampoline" to these addresses.  If an attacker desires to jump to the start of an existing function, they can jump directly to the trampoline anyway, and may have the opportunity to provide their own stack frame to the function with a write to the stack. If they overwrite a saved stack pointer which is loaded back into memory, or execute a function, that changes the address of a stack pointer.

If an attacker wants to inject some data into the program, for example as a parameter to a known function that is not under ASLR or a pointer to a trampoline function in the PLT, then they can repeat the data until they exceed the range of ASLR coverage, which on 32-bit systems is accomplishable in a few seconds with a heap spray.  Microsoft's EMET and Windows 10 Exploit Guard can pre-allocate particular addresses that are commonly used in heap sprays.  However, in many products, there does not seem to be nearly a complete coverage of such addresses, which only need to be executable and in the range of the heap; 0x0c0c0c0c is such an address that is commonly used for the x86 processor architecture, as when executed it only performs a numeric operation to a register four times.


---

# D3-SMRA: Sender MTA Reputation Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-SMRA/  

## Definition
Characterizing the reputation of mail transfer agents (MTA) to determine the security risk in emails.

## Parent Class(es)
- Message Analysis

## Relationships
- **analyzes:** Email
- **kb-reference:** Reference - Systems and methods for detecting and/or handling targeted attacks in the email channel - Graphus Inc

## Knowledge Base Article
## How it works
The sender message transfer agent (MTA) trust rating can be considered an indicator of the level of security risk and/or a trust level associated with sender MTAs in an email header.

The features considered in determining the trust rating may include:

* Length of time MTA has interacted with the enterprise
* Number of sender domains sending emails from the MTA
* Number of recipients in the enterprise the MTA sends emails to
* Number of emails received from this MTA
* Number of email replies received from this MTA

For example, higher values for the length of time an MTA has interacted with the enterprise, or number of emails received from an MTA can result in a higher trust rating. The trust rating categorizes the sender MTA as unrated, neutral, trusted, suspicious, or malicious.

## Considerations
Legitimate emails from a sender MTA may receive a lower trust rating over time if the sender's domain gets spoofed and is used to send unauthorized emails.


---

# D3-SRA: Sender Reputation Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-SRA/  

## Definition
Ascertaining sender reputation based on information associated with a message (e.g. email/instant messaging).

## Parent Class(es)
- Message Analysis

## Relationships
- **analyzes:** Email
- **kb-reference:** Reference - Systems and methods for detecting and/or handling targeted attacks in the email channel - Graphus Inc

## Knowledge Base Article
## How it works

Sender trust rating can be considered an indicator of the level of security risk and/or a trust level associated with a sender. The features considered in determining the trust rating include:

* Length of time sender has sent emails to the enterprise
* Number of recipients in the enterprise the sender interacts with
* Sender vs. enterprise originated message ratio
* Sender messages opened vs. not-opened ratio
* Number of emails received from this sender
* Number of emails replied to this sender
* Number of emails from this sender not opened
* Number of emails from this sender not opened that contain an attachment
* Number of emails from this sender not opened that contain a URL
* Number of emails sent to this sender
* Number of email replies received from this sender.

Higher values for the number of recipients the sender has interacted with or the number of emails received from the sender, for example, results in a higher trust rating. The trust rating can categorize the sender as unrated, neutral, trusted, suspicious, or malicious.

## Considerations
Legitimate emails from a sender may receive a lower trust rating over time if the sender's domain gets spoofed and is used to send unauthorized emails.


---

# D3-SBV: Service Binary Verification

**Reference:** https://d3fend.mitre.org/technique/D3-SBV/  

## Definition
Analyzing changes in service binary files by comparing to a source of truth.

## Parent Class(es)
- System File Analysis

## Relationships
- **kb-reference:** Reference - CAR-2014-02-001: Service Binary Modifications - MITRE
- **verifies:** Service Application

## Knowledge Base Article
## How it works
System service applications may originate from the operating system installation or third-party applications installed with administrative privileges. These services have an entry point of some executable file-- a binary or a script. Attackers sometimes modify these executables to launch their own code. Analyzing changes in these files may uncover unauthorized activity.

## Considerations
* These files change for legitimate reasons when the system or software updates.
* The source of truth must not be corrupted in order for this method to work.


---

# D3-SVCDM: Service Dependency Mapping

**Synonym(s):** Distributed Tracing  
**Reference:** https://d3fend.mitre.org/technique/D3-SVCDM/  

## Definition
Service dependency mapping determines the services on which each given service relies.

## Parent Class(es)
- System Mapping

## Relationships
- **kb-reference:** Reference - Catia UAF Plugin
- **kb-reference:** Reference - Tivoli Application Dependency Discovery Manager 7.3.0 - Dependencies between resources
- **kb-reference:** Reference - Unified Architecture Framework (UAF)
- **maps:** Service Dependency

## Knowledge Base Article
## How it works
The organization collects and models architectural information about the services and consumers of services and maps the dependencies between the services.

## Considerations
* Architectural design artifacts and SMEs may need to be consulted to determine if dependencies are intended or otherwise essential.
* Service dependencies for critical systems--those supporting critical organizational activities--should be prioritized for supply chain risk analysis.
* Service dependencies in cloud or microservice architectures may be discovered using distributed tracing capabilities


---

# D3-SDA: Session Duration Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-SDA/  

## Definition
Analyzing the duration of user sessions in order to detect unauthorized  activity.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **analyzes:** Authentication
- **analyzes:** Authorization
- **kb-reference:** Reference - Method and Apparatus for Network Fraud Detection and Remediation Through Analytics - Idaptive LLC
- **kb-reference:** Reference - System, method, and computer program product for detecting and assessing security risks in a network - Exabeam Inc

## Knowledge Base Article
## How it works
Detecting unauthorized user sessions by comparing the duration of a user logon session with a baseline behavior model. The behavior model comprises historical user session duration times.  Abnormalities between session duration and the behavior model may indicate suspicious activity.

## Considerations
* Potential for false positives from anomalies that are not associated with malicious activity.
* Attackers may not differentiate their session duration enough to trigger an alert.


---

# D3-ST: Session Termination

**Reference:** https://d3fend.mitre.org/technique/D3-ST/  

## Definition
Forcefully end all active sessions associated with compromised accounts or devices.

## Parent Class(es)
- Process Eviction

## Relationships
- **deletes:** Session
- **kb-reference:** Reference - NIST Special Publication 800-53A Revision 5 - Assessing Security and Privacy Controls in Information Systems and Organizations

## Knowledge Base Article
Defined in NIST 800-53 as AC-12.


---

# D3-SSC: Shadow Stack Comparisons

**Reference:** https://d3fend.mitre.org/technique/D3-SSC/  

## Definition
Comparing a call stack in system memory with a shadow call stack maintained by the processor to determine unauthorized shellcode activity.

## Parent Class(es)
- Process Analysis

## Relationships
- **analyzes:** Stack Frame
- **kb-reference:** Reference - Threat detection for return oriented programming - Crowdstrike Inc

## Knowledge Base Article
## How it works
This technique compares the call stack stored in system memory with the shadow call stack maintained in the cache memory of the processor.  Mismatches between the two are compared since a return oriented programming attack may only be able to control or spoof the call stack and not the shadow call stack. Mismatches are counted and if the number of mismatches exceeds a certain threshold it is an indication of unauthorized activity and a security response action is performed.

## Considerations
If the threshold for detecting a stack anomaly is low, it may not detect a return-oriented attack with just one gadget, such as a return-to-libc or return-to-plt attack.  Additionally, this technique may not detect JOP (Jump-oriented programming), as the return instruction is not executed.


---

# D3-SWI: Software Inventory

**Synonym(s):** Software Discovery, Software Inventorying  
**Reference:** https://d3fend.mitre.org/technique/D3-SWI/  

## Definition
Software inventorying identifies and records the software items in the organization's architecture.

## Parent Class(es)
- Asset Inventory

## Relationships
- **inventories:** Software
- **kb-reference:** Reference - Web-Based Enterprise Management
- **kb-reference:** Reference - Windows Management Infrastructure (MI)
- **kb-reference:** Reference - Windows Management Instrumentation (WMI)

## Knowledge Base Article
## How it works
Administrators collect information on software items in their architecture using a variety of administrative and management tools that query network nodes for information.  In limited cases, where such queries are not supported or provide specific information of interest, an administrator may also collect this information through network enumeration methods to determine services responding on network nodes.

## Considerations
* Scanning and probing techniques using mapping tools can result in side effects to information technology (IT) and operational technology (OT) systems.
* An adversary conducting network enumeration may engage in activities that parallel normal software inventorying activities, but would require escalating to admin privileges for most of the operations requiting administrative tools.

## Examples

Application-layer discovery:

* Simple Network Management Protocol (SNMP) collects MIB information
* Web-based Enterprise Management (WBEM) collects CIM information
   * Windows Management Instrumentation (WMI)
   * Windows Management Infrastructure (MI)


---

# D3-SU: Software Update

**Reference:** https://d3fend.mitre.org/technique/D3-SU/  

## Definition
Replacing old software on a computer system component.

## Parent Class(es)
- Platform Hardening

## Relationships
- **kb-reference:** Reference - Method and system for providing software updates to local machines
- **updates:** Software


---

# D3-SCH: Source Code Hardening

**Reference:** https://d3fend.mitre.org/technique/D3-SCH/  

## Definition
Hardening source code with the intention of making it more difficult to exploit and less error prone.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Harden


---

# D3-SFCV: Stack Frame Canary Validation

**Reference:** https://d3fend.mitre.org/technique/D3-SFCV/  

## Definition
Comparing a value stored in a stack frame with a known good value in order to prevent or detect a memory segment overwrite.

## Parent Class(es)
- Application Hardening

## Relationships
- **kb-reference:** Reference - /GS (Buffer Security Check) - Microsoft Docs
- **kb-reference:** Reference - Security Technologies: Stack Smashing Protection (StackGuard) - Red Hat
- **validates:** Stack Frame

## Knowledge Base Article
## How it works

This defense must be applied at compile-time, or via a patch to the program binary.  Stack Frame Canary Verification inserts instructions at the prologue and epilogue of desired functions.  In the prologue, a canary value, typically with the same size as the register size, is stored in the system of record and on the stack.  Typically, the canary is loaded to where it has a memory address just below that of the saved instruction pointer and base pointer.  In the epilogue, the canary value stored on the stack and, is compared to the canary value in the system of record.  If the values are different, other techniques such as those in Process Eviction might be invoked, such as Process Termination to end the current process, or Executable Blacklisting to blacklist the potentially vulnerable or malfunctioning executable.

Stack Frame Canary Verification is commonly used to detect potential tampering of a saved register value on the stack before it has been restored.  Examples of registers with values commonly saved to the stack include the instruction pointer and the base pointer.

The canary should be stored between where the start of a buffer overrun is likely, and the data to protect, in cases where the buffer size increases it will overwrite the data to be protected.

On most processor architectures, including x86, x64, and ARM, a "push" operation to store data to the stack grows the stack towards a lower memory address.  As in these architectures, saved register values are stored to the stack at a point in time just before space is made for the local function variables, the saved register values have a higher address than that of the local function variables.  Values at increasing indexes of a buffer are written to increasing memory addresses; therefore, an overwrite in the local variable buffer could overwrite saved register values, and a stack canary between these two would be useful in detecting an overwrite.

On some other processor architectures such as the B5000, the stack grows towards increasing memory addresses, and some architectures, such as System Z and RCA1802A, stack direction can be chosen.  If the stack grows towards increasing memory addresses, while this architecture inherently provides more protection against a saved register being overwritten, other data including local function variables might be overwritten.


## Considerations

There are several ways that the protection provided by a canary could be rendered ineffective.

### Performing a malicious action before the canary is checked

If the attacker alters the memory in such a way that it performs a malicious action before the epilogue is called, then this protection will not be effective.  This includes altering the logic of the program by altering the values of local variables stored on the function stack, or by causing an exception and exploiting the exception mechanism such as the SEH (Structured Exception Handling) mechanism on Windows.

### Determining the canary value

Determining the canary value is possible through reading memory either for the code used to check the canary, or from the stored canary value itself in a stack frame.

### Changing the canary value

A vulnerability such as a write-what-where condition that allows one to write data after the canary in the stack, would allow control of the value of the saved instruction pointer without needing to know the canary value.


---

# D3-SHN: Standalone Honeynet

**Reference:** https://d3fend.mitre.org/technique/D3-SHN/  

## Definition
An environment created for the purpose of attracting attackers and eliciting their behaviors that is not connected to any production enterprise systems.

## Parent Class(es)
- Decoy Environment

## Relationships
- **kb-reference:** Reference - Dynamic selection and generation of a virtual clone for detonation of suspicious content within a honey network - Palo Alto Networks Inc
- **spoofs:** Intranet Network

## Knowledge Base Article
## How it works
A standalone honeynet does not directly interact with the real enterprise environment. It may be located near or in some portion of the enterprise address space, but it does not interact with enterprise resources.

## Considerations
A standalone honeynet is a lower risk to deploy compared to connected or integrated honeynets due to its isolation from the enterprise network. However, this comes at cost in loss of fidelity and realism. Significant extra effort must be made in order to make the environment look realistic.


---

# D3-SPP: Strong Password Policy

**Reference:** https://d3fend.mitre.org/technique/D3-SPP/  

## Definition
Modifying system configuration to increase password strength.

## Parent Class(es)
- Credential Hardening

## Relationships
- **kb-reference:** Reference - Digital Identity Guidelines 800-63-3
- **kb-reference:** Reference - Testing Metrics for Password Creation Policies by Attacking Large Sets of Revealed Passwords
- **strengthens:** Password

## Knowledge Base Article
## How it works
Password strength guidelines include increasing password length, permitting passwords that contain ASCII or Unicode characters, and requiring systems to screen new passwords against lists of commonly used or compromised passwords.
## Considerations
Extremely complex password requirements may lead users to saving passwords in text files or picking obvious passwords that meet the policy.


---

# D3-SCA: System Call Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-SCA/  

## Definition
Analyzing system calls to determine whether a process is exhibiting unauthorized behavior.

## Parent Class(es)
- Process Analysis

## Relationships
- **analyzes:** System Call
- **kb-reference:** Reference - CAR-2020-05-001: MiniDump of LSASS - MITRE
- **kb-reference:** Reference - CAR-2021-05-011: Create Remote Thread into LSASS - MITRE
- **kb-reference:** Reference - CAR-2019-08-001: Credential Dumping via Windows Task Manager - MITRE
- **kb-reference:** Reference - CAR-2013-10-002: DLL Injection via Load Library - MITRE
- **kb-reference:** Reference - Deterministic method for detecting and blocking of exploits on interpreted code - K2 Cyber Security Inc
- **kb-reference:** Reference - Hardware-assisted system and method for detecting and analyzing system calls made to an operting system kernel - Endgame Inc
- **kb-reference:** Reference - Malware detection in event loops - Crowdstrike Inc
- **kb-reference:** Reference - Post sandbox methods and systems for detecting and blocking zero-day exploits via api call validation - K2 Cyber Security Inc

## Knowledge Base Article
## How it works

System calls are APIs between a user application and the operating system [1].

By analyzing a process's use of these APIs, it is, in some cases, possible to ascertain whether a program is exhibiting unauthorized behavior, including trying to escalate its privileges.

### Gathering System Calls
A common method to capture system calls is to use kernel APIs to hook [2] a process's system call invocations.

The Linux system call `ptrace` tracks other system calls in a process and allows their alteration; this is made use of by GDB.  `strace` utilizes `ptrace` and will print to stdout each system call invoked. Other applications record this data in local or remote databases.

The log entry for each system call, which may reference additional information such as the date and time, and the process tree for the process which made the system call, is relayed, in real time or post-facto, to an analysis module which consults a catalog or model to determine whether the distribution matches a known-good or known-bad pattern.


### Analysis

System calls are analyzed with a variety of methods. Some analytics look for specific sequences of instructions, others may apply statistical methods to identify abnormal behavior. Sequences of instructions can be abstracted into conceptually higher order user activities, for example:

* An attacker executes many system calls in a short period of time, with several sequences which could be used to escalate privileges.
* Getting the contents from a URL, writing to a new file, and then executing the same file.
* A ransomware program which either uses a loop or creates many threads to: read a specified file, encrypt its contents, create an output file with a similar name to the original file, and delete the unencrypted original.

## Considerations

* Duplicative or extraneous system calls may be added to malware to defeat analytics.
* Malware could replace API hooking instructions to allow system calls to be made without being monitored.
* A model built from a training set of system calls and related data may not be updated fast enough to detect new threats.


[1] [Syscalls](http://man7.org/linux/man-pages/man2/syscalls.2.html)

[2] [Hooking](http://dbpedia.org/resource/Hooking)


---

# D3-SCF: System Call Filtering

**Synonym(s):** System Call Control  
**Reference:** https://d3fend.mitre.org/technique/D3-SCF/  

## Definition
Controlling access to local computer system resources with kernel-level capabilities.

## Parent Class(es)
- Access Mediation

## Relationships
- **filters:** System Call
- **isolates:** Process
- **kb-reference:** Reference - Analysis of the Windows Vista Security Model - Symantec Corporation
- **kb-reference:** Reference - Architecture of transparent network security for application containers - Neuvector Inc
- **kb-reference:** Reference - Overview of the seccomp sandbox

## Knowledge Base Article
## How it works
System call filtering uses a mandatory access control paradigm (that is, a non-discretionary access control) system because the rules and polices that determine access is determined by a security control authority and not distributed to local users. Access determinations are based on designed access control polices and are not based on local resource owner determinations.

Access is typically granted by defining sets of subjects and sets of objects. Subjects are the entities requesting access and objects are the resources that subjects are trying to access. Rules and policies are defined that associate subjects and object permissions and access controls.

### Common implementations
#### Security label access control
A fine-grained form control is to apply security labels to individual resources, including processes, and the access control decisions are against a particular resource and a given user attempting to gain access. This type of control requires that the file system has built-in support for security labels.

Access controls are typically implemented through the use of label identifiers for every file system object. Identifier labels are applied to resources and users are assigned a similar access identifier. Users attempting to access a resource will result in the operating system performing an access control check. The access control check will compare the assigned user's credentials to that of the resource or object they are attempting to access.

A security context is associated with resources and is used to determine assess. Typical basic access control elements include users, roles and types and together they form a security context which is the basis for the security labels.

This type of access control is what is employed in SELinux [2]. This form of security kernel access control is considered the most flexible implementation, but it also is the most complex to deploy across the enterprise. Where multiple virtual machines (VM) are run together this type of access control is typically employed to ensure true isolation of processes and VMs.

#### File path level controls
A less fine-grained form of mandatory access control is to apply security labels that allow for access control at the file path level.  Access control is filesystem agnostic and no relabeling of resources is required. Pathname access control usually seems more natural for implementation and corresponding access audits.

This type of system call filtering is what is employed in AppArmor [3]. AppArmor was developed to provide a simpler alternative method with much less management overhead. A simple access policy is maintained that defines path resource access rules. Access control attributes are typically associated with programs instead of users.


## Considerations
Some implementations of security label-based control contain complex rules set that are hard to verify and complex to maintain over time.

Initial planning of access model and continuous monitoring of the available users, resources and object is necessary.

## Implementations

 * Linux C-Groups, and policy engines like SELinux and AppArmor
 * Windows Mandatory Integrity Control introduced in Windows Vista


### Citations
1. [SELinux](https://selinuxproject.org/)
2. [AppArmor](https://www.apparmor.net/)


---

# D3-SCP: System Configuration Permissions

**Reference:** https://d3fend.mitre.org/technique/D3-SCP/  

## Definition
Restricting system configuration modifications to a specific user or group of users.

## Parent Class(es)
- Platform Hardening

## Relationships
- **kb-reference:** Reference - How to change registry values or permissions from a command line or a script
- **restricts:** System Configuration Database


---

# D3-SDM: System Daemon Monitoring

**Reference:** https://d3fend.mitre.org/technique/D3-SDM/  

## Definition
Tracking changes to the state or configuration of critical system level processes.

## Parent Class(es)
- Operating System Monitoring

## Relationships
- **kb-reference:** Reference - Host intrusion prevention system using software and user behavior analysis - Sophos Ltd
- **kb-reference:** Reference - Method using kernel mode assistance for the detection and removal of threats which are actively preventing detection and removal from a running system - Symantec Corporation
- **kb-reference:** Reference - CAR-2016-04-003: User Activity from Stopping Windows Defensive Services - MITRE
- **monitors:** Operating System Process

## Knowledge Base Article
## How it works
Attackers may manipulate system settings or services to disable system logging or monitoring of security tools and events. Firewall and antivirus services are popular targets for attackers. Disabling system logs will also allow an attacker's actions to go unnoticed. Analysis of logs, registries, and process monitoring help defenders locate signs of tampering. Two possible approaches are to monitor hardened system services or to monitor registry updates for modifications to security settings.


---

# D3-SYSDM: System Dependency Mapping

**Reference:** https://d3fend.mitre.org/technique/D3-SYSDM/  

## Definition
System dependency mapping identifies and models the dependencies of system components on each other to carry out their function.

## Parent Class(es)
- System Mapping

## Relationships
- **kb-reference:** Reference - Catia UAF Plugin
- **kb-reference:** Reference - Software vulnerability graph database
- **kb-reference:** Reference - Tivoli Application Dependency Discovery Manager 7.3.0 - Dependencies between resources
- **kb-reference:** Reference - Unified Architecture Framework (UAF)
- **maps:** System Dependency

## Knowledge Base Article
## How it works
The organization collects and models architectural information about the software, hardware, and products and maps the dependencies between systems, including each system's internal components and dependencies.

## Considerations
* Data exchanges identified in the network mapping efforts usually indicate such dependencies, but may not be part of the intended design.
* Architectural design artifacts and SMEs may need to be consulted to determine if dependencies are intended or otherwise essential.
* System dependency mapping can identify internal dependencies of standard and pre-built systems that should be incorporated into a complete system dependency model.
* System dependencies for critical systems--those supporting critical organizational activities--should be prioritized for supply chain risk analysis.
* System dependencies should identify the integral components of a given named system and their structure to form a system.
* System dependencies with a given system may be fixed by a particular product's configuration, and leveraging external knowledge bases about dependencies available (e.g., from package managers) is essential.


---

# D3-SFA: System File Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-SFA/  

## Definition
Monitoring system files such as authentication databases, configuration files, system logs, and system executables for modification or tampering.

## Parent Class(es)
- Operating System Monitoring

## Relationships
- **analyzes:** Operating System File
- **kb-reference:** Reference - CAR-2019-07-001: Access Permission Modification - MITRE
- **kb-reference:** Reference - CAR-2013-01-002: Autorun Differences - MITRE
- **kb-reference:** Reference - CAR-2016-04-002: User Activity from Clearing Event Logs - MITRE

## Knowledge Base Article
## How it works
This technique ensures the integrity of system owned file resources. System files can impact the behavior below the user level.


## Considerations
* Need to manage the size of log file analysis.
* False positives are a concern with this technique and filtering will need to be given additional thought.
* A baseline or snapshot of file checksums should be established for future comparison.


---

# D3-SFV: System Firmware Verification

**Reference:** https://d3fend.mitre.org/technique/D3-SFV/  

## Definition
Cryptographically verifying installed system firmware integrity.

## Parent Class(es)
- Firmware Verification

## Relationships
- **kb-reference:** Reference - Firmware Verification Eclypsium
- **kb-reference:** Reference - Platform Firmware Resiliency Guidelines - NIST
- **verifies:** System Firmware

## Knowledge Base Article
## How it works
Cryptographic hash values are computed for system firmware. The hash values are compared against precomputed firmware hash values to determine if the firmware has been tampered with.

When system firmware verification fails a set of predefined responses is typically invoked. The responses may direct the system to disable some devices or operations.

## Considerations
* Requires the use of system provided security modules
* Secure hash values will need to be computed for firmware


---

# D3-SICA: System Init Config Analysis

**Synonym(s):** Autorun Analysis, Startup Analysis  
**Reference:** https://d3fend.mitre.org/technique/D3-SICA/  

## Definition
Analysis of any system process startup configuration.

## Parent Class(es)
- Operating System Monitoring

## Relationships
- **analyzes:** System Init Configuration
- **kb-reference:** Reference - CAR-2013-01-002: Autorun Differences - MITRE
- **kb-reference:** Reference - CAR-2020-09-005: AppInit DLLs - MITRE
- **kb-reference:** Reference - CAR-2020-11-001: Boot or Logon Initialization Scripts - MITRE


---

# D3-SYSM: System Mapping

**Reference:** https://d3fend.mitre.org/technique/D3-SYSM/  

## Definition
System mapping encompasses the techniques to identify the organization's systems, how they are configured and decomposed into subsystems and components, how they are dependent on one another, and where they are physically located.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Model


---

# D3-SYSVA: System Vulnerability Assessment

**Reference:** https://d3fend.mitre.org/technique/D3-SYSVA/  

## Definition
System vulnerability assessment relates all the vulnerabilities of a system's components in the context of their configuration and internal dependencies and can also include assessing risk emerging from the system's design as a whole, not just the sum of individual component vulnerabilities.

## Parent Class(es)
- System Mapping

## Relationships
- **evaluates:** Digital System
- **identifies:** Vulnerability
- **kb-reference:** Reference - Software vulnerability graph database


---

# D3-TBI: TPM Boot Integrity

**Synonym(s):** STRM, Static Root of Trust Measurement  
**Reference:** https://d3fend.mitre.org/technique/D3-TBI/  

## Definition
Assuring the integrity of a platform by demonstrating that the boot process starts from a trusted combination of hardware and software and continues until the operating system has fully booted and applications are running.  Sometimes called Static Root of Trust Measurement (STRM).

## Parent Class(es)
- Platform Hardening

## Relationships
- **kb-reference:** Reference - TCG Trusted Attestation Protocol Use Cases for TPM Families 1.2 and 2.0 and DICE
- **kb-reference:** Reference - TPM 2.0 Library Specification - Trusted Computing Group, Incorporated
- **kb-reference:** Reference - Trusted Attestation Protocol Use Cases

## Knowledge Base Article
## How it works
During the boot process, the BIOS boot block (which with this defense enabled, is the Core Root of Trust for Measurement) measures boot components (firmware, ROM). The TPM hashes those measurements and stores the hashes in Platform Configuration Registers (PCRs).  Upon a subsequent boot, these hashes are provided to a verifier which compares the stored measurements to the new boot measurements. Integrity of the boot components is assured if they match.

Attestation of the secure boot occurs when a verifying entity requests a Quote which is a concatenation of the requested PCR values, hashed and signed by the TPM's unique RSA key.  The TPM signature is trusted because the private key is stored securely in hardware and never leaves the TPM.

## Considerations

* The TPM does not perform the follow-on actions of acting on the PCR value information, it just provides the PCR stored information.
* The current version of TPM is 2.0.; most existing implementations use TPM 1.2.

## Citations
[1] [TPM 2.0 Library](https://trustedcomputinggroup.org/resource/tpm-library-specification/)
[2] [TCG Trusted Attestation Protocol (TAP) Use Cases for TPM Families 1.2 and 2.0 and DICE](https://trustedcomputinggroup.org/wp-content/uploads/TCG_TNC_TAP_Use_Cases_v1r0p35_published.pdf)


---

# D3-TBA: Token-based Authentication

**Reference:** https://d3fend.mitre.org/technique/D3-TBA/  

## Definition
Token-based authentication is an authentication protocol where users verify their identity in exchange for a unique access token. Users can then access the website, application, or resource for the life of the token without having to re-enter their credentials.

## Parent Class(es)
- Agent Authentication

## Relationships
- **kb-reference:** Reference - Identity Providers: What is Token Based Authentication
- **uses:** Access Token

## Knowledge Base Article
## How it works

Token-based authentication starts with a user logging into a system, device or application, typically using a password or a security question. An authorization server validates that initial authentication and then issues an access token, which is a small piece of data that lets a client application make a secure call or signal to an API server. Once this initial token-based authentication protocol is completed, the token works like a stamped ticket: The user can continue to seamlessly access the relevant resources, without re-authenticating, for the duration of the token lifecycle. That lifecycle ends when the user logs out or quits an app — and can also be triggered by a set time-out protocol.

## Considerations:

While token-based authentication is undoubtedly a major step above traditional password-based authentication, the token is still considered a “bearer token” — that is, access is granted to whomever holds the token.


---

# D3-TB: Token Binding

**Reference:** https://d3fend.mitre.org/technique/D3-TB/  

## Definition
Token binding is a security mechanism used to enhance the protection of tokens, such as cookies or OAuth tokens, by binding them to a specific connection.

## Parent Class(es)
- Credential Hardening

## Relationships
- **kb-reference:** Reference - The Token Binding Protocol Version 1.0
- **strengthens:** Access Token

## Knowledge Base Article
## How it works

When issuing a security token to a client that supports Token Binding, a server includes the client's Token Binding ID (or its cryptographic hash) in the token. Later on, when a client presents a security token containing a Token Binding ID, the server verifies that the ID in the token matches the ID of the Token Binding established with the client. In the case of a mismatch, the server rejects the token.

## Considerations

- While industry participation in the standards process is widespread, browser support remains limited.
- In practice, token-binding implementations are tied to Transport Security Layer (TLS).


---

# D3-TAAN: Transfer Agent Authentication

**Reference:** https://d3fend.mitre.org/technique/D3-TAAN/  

## Definition
Validating that server components of a messaging infrastructure are authorized to send a particular message.

## Parent Class(es)
- Message Hardening

## Relationships
- **kb-reference:** Reference - RFC 6376: DomainKeys Identified Mail (DKIM) Signatures - IETF
- **kb-reference:** Reference - RFC 7208: Sender Policy Framework (SPF) for Authorizing Use of Domains in Email - IETF
- **kb-reference:** Reference - RFC 7489: Domain-based Message Authentication, Reporting, and Conformance (DMARC) - IETF

## Knowledge Base Article
## How it works
Transfer Agent Authentication can be accomplished in different ways for depending on the protocol. In Email, Sender Policy Framework (SPF), Domain Key Identified Email (DKIM) or Domain-based Message Authentication Reporting and Conformance (DMARC) are used to validate sender domain ownership.

### SPF
SPF protocol allows for mail domain owners to specify the mail servers they use when sending email. SPF requires the use of SPF records published in the Domain Name System (DNS). The records record the authorized IPs for email senders. SPF uses the return-path address for domain IP identification. Email that is forwarded may cause the return-path validation problems.
### DKIM
DKIM also uses a record entry in DNS for authentication but does not rely on the simple return-path for validation. A signature header is added to email and encryption is used for security. This adds an additional layer of complexity and requires that DKIM servers be configured identified cryptographic signatures. The additional complexity results in a validation process that can survive complex routing of emails.

### DMARC
DMARC is an email policy and authentication protocol that seeks to ensure that the "From" field of emails is not spoofed. DMARC makes use of both SPF records and DKIM published key validation. DMARC also has a decision policy framework, contained in a DMARC record, for handling of rejected email. The DMARC framework also updates DMARC domains with authentication statues for allowed senders of that domain.

## Considerations
- Additional work is required to ensure that all SPF, DKIM and DMARC records are current and up to date.
- Maintenance of DKIM signing keys is needed.
- Using SPF without DKIM and DMARC verifies the Return-Path domain however does not prevent spoofing of the displayed From: address.
- Parts of an email that are not signed or verified by email authentication methods, such as the message body or the header To: and Subject: fields, can be altered or modified.
- Email message authentication does not replace the need to do email content analysis since executables, attachments, or links or other parts of the email beyond the sender domain are not verified.


---

# D3-TL: Trusted Library

**Reference:** https://d3fend.mitre.org/technique/D3-TL/  

## Definition
A trusted library is a collection of pre-verified and secure code modules or components that are used within software applications to perform specific functions. These libraries are considered reliable and have been vetted for security vulnerabilities, ensuring they do not introduce risks into the application.

## Parent Class(es)
- Source Code Hardening

## Relationships
- **hardens:** Subroutine
- **kb-reference:** Reference - Leverage Security Frameworks and Libraries - OWASP

## Knowledge Base Article
## How it Works
Using a trusted library can reduce the chances of introducing errors compared to writing code from scratch.



## Considerations

Note: This resource should not be considered a definitive or exhaustive coding guideline.


---

# D3-UA: URL Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-UA/  

## Definition
Determining if a URL is benign or malicious by analyzing the URL or its components.

## Parent Class(es)
- Identifier Analysis

## Relationships
- **analyzes:** URL
- **kb-reference:** Reference - Method and Apparatus for Detecting Malicious Websites - Endgame Inc
- **kb-reference:** Reference - Method and system for detecting restricted content associated with retrieved content - Sophos Ltd

## Knowledge Base Article
## How it works

URLs may contain components, for example:

 * scheme
 * userinfo
 * host name
 * port
 * path
 * query
 * fragment

These components are used as features in analysis algorithms.

Contextual information about a URL such as where it is embedded (ex. emails, files, network protocols), header, path, location, and origin information, as well as information about the content returned from the URL request, may be incorporated into an analytic for URL analysis. For example, if a URL indicates a .pdf file but an executable is actually returned, the combination of these two pieces of information indicates suspicious activity.

Additional techniques include:

* Extracting features of a URL such as domain name length, ratio of consecutive consonants, percentage of digits in a domain, and number of vowels. Values for each feature are combined to develop a score for the URL.
* Determining the probability of a character occurring in the URL given the preceding two characters. For example, for google.com, the probability of a 'g' occurring at the beginning of a word, the probability of an 'o' occurring after a "g, the probability of an o" occurring after a 'g' and "o, and so forth. A dictionary or a list of known good domains is used to determine probability. Probabilities are multiplied to develop a score for the URL.

URL analysis may trigger follow-on analytics such as **File Analysis**

## Considerations

* Volume of URLs being analyzed, combined with the speed at which they are analyzed
* Fidelity of analysis technique at detecting brand new URLs versus analyzing URLs of established domains


---

# D3-URA: URL Reputation Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-URA/  

## Definition
Analyzing the reputation of a URL.

## Parent Class(es)
- Identifier Reputation Analysis

## Relationships
- **analyzes:** URL
- **kb-reference:** Reference - Finding phishing sites


---

# D3-ULA: Unlock Account

**Reference:** https://d3fend.mitre.org/technique/D3-ULA/  

## Definition
Restoring a user account's access to resources by unlocking a locked User Account.

## Parent Class(es)
- Restore User Account Access

## Relationships
- **kb-reference:** Reference - Cybersecurity Incident and Vulnerability Response Playbooks
- **restores:** User Account


---

# D3-UAP: User Account Permissions

**Reference:** https://d3fend.mitre.org/technique/D3-UAP/  

## Definition
Restricting a user account's access to resources.

## Parent Class(es)
- Access Policy Administration

## Relationships
- **kb-reference:** Reference - Configure User Access Control and Permissions
- **restricts:** User Account


---

# D3-UBA: User Behavior Analysis

**Synonym(s):** Credential Monitoring, UBA  
**Reference:** https://d3fend.mitre.org/technique/D3-UBA/  

## Definition
User behavior analytics ("UBA") as defined by Gartner, is a cybersecurity process about detection of insider threats, targeted attacks, and financial fraud. UBA solutions look at patterns of human behavior, and then apply algorithms and statistical analysis to detect meaningful anomalies from those patterns-anomalies that indicate potential threats.' Instead of tracking devices or security events, UBA tracks a system's users. Big data platforms are increasing UBA functionality by allowing them to analyze petabytes worth of data to detect insider threats and advanced persistent threats.

## Parent Class(es)
- Defensive Technique

## Relationships
- **enables:** Detect

## Knowledge Base Article
## Technique Overview

Some techniques monitor patterns of human behavior and then apply algorithms and to identify patterns such as repeated login attempts from a single IP address or large file downloads, or abnormal accesses.

Other techniques may have explicit or rigid definitions of "bad behavior" which are then matched against instances in a computer network environment.


---

# D3-UDTA: User Data Transfer Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-UDTA/  

## Definition
Analyzing the amount of data transferred by a user.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **analyzes:** Resource Access
- **kb-reference:** Reference - System and method thereof for identifying and responding to security incidents based on preemptive forensics - Palo Alto Networks Inc
- **kb-reference:** Reference - System for implementing threat detection using threat and risk assessment of asset-actor interactions - VECTRA NETWORKS Inc

## Knowledge Base Article
## How it works
Unusual data transfer activity may indicate unauthorized activity. Data transfers can be analyzed by collecting network traffic or application logs.

## Considerations
* There is a potential for false positives from anomalies that are not associated with unauthorized activity.
* Attackers that move low and slow may not differentiate their data transfer behavior enough for an alert to trigger.


---

# D3-UGLPA: User Geolocation Logon Pattern Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-UGLPA/  

## Definition
Monitoring geolocation data of user logon attempts and comparing it to a baseline user behavior profile to identify anomalies in logon location.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **analyzes:** Network Traffic
- **kb-reference:** Reference - Method and Apparatus for Network Fraud Detection and Remediation Through Analytics - Idaptive LLC
- **kb-reference:** Reference - System, method, and computer program product for detecting and assessing security risks in a network - Exabeam Inc

## Knowledge Base Article
## How it works
Geolocation data for each user logon attempt is collected and used to create a baseline user behavior profile. Current geolocation logon data is then compared against the user behavior profile. Logon activity that deviates from normal patterns and can help in identifying situations that may be indicative of a remote attacker using stolen credentials. For example:

* logons from locations that are different from where a user usually logs in
* logons from a location in which an enterprise has no users located
* logon that is not physically possible given the elapsed time since a logon from another location.

## Considerations
* Potential for false positives from logon anomalies that are not associated with malicious activity.
* Attackers may not differentiate their logon behavior enough to trigger an alert.


---

# D3-UGPH: User Group Permissions

**Synonym(s):** Role Based Access Controls  
**Reference:** https://d3fend.mitre.org/technique/D3-UGPH/  

## Definition
Access control where access is determined based on attributes associated with users and the objects being accessed.

## Parent Class(es)
- Access Policy Administration

## Relationships
- **kb-reference:** Reference - NIST SP 800-82R3 Guide to Operational Technology (OT) Security, Section 6.2.1.4.5 Password Authentication
- **restricts:** User Group

## Knowledge Base Article
## How it works

Access is determined based on the attributes associated with subjects (requesters) and the objects being accessed. Each object and subject has a set of associated attributes, such as location, time of creation, and access rights. Access to an object is authorized or denied depending on whether the required.


---

# D3-USICA: User Session Init Config Analysis

**Synonym(s):** User Startup Config Analysis  
**Reference:** https://d3fend.mitre.org/technique/D3-USICA/  

## Definition
Analyzing modifications to user session config files such as .bashrc or .bash_profile.

## Parent Class(es)
- Operating System Monitoring

## Relationships
- **analyzes:** User Init Configuration File
- **kb-reference:** Reference - CAR-2020-09-002:  Component Object Model Hijacking - MITRE
- **kb-reference:** Reference - CAR-2020-11-011: Registry Edit from Screensaver
- **kb-reference:** Reference - Identification and extraction of key forensics indicators of compromise using subject-specific filesystem views
- **kb-reference:** Reference - Registry Key Security and Access Rights


---

# D3-VI: Variable Initialization

**Reference:** https://d3fend.mitre.org/technique/D3-VI/  

## Definition
Setting variables to a known value before use.

## Parent Class(es)
- Source Code Hardening

## Relationships
- **hardens:** Subroutine
- **kb-reference:** Reference - Integer Initialization - GNU C Manual
- **kb-reference:** Reference - Variable Initialization - CWE-457

## Knowledge Base Article
## How it Works
Initializing variables upon declaration ensures that the variable has a known quantity before use.

## Considerations
* Default behavior when declaring variables varies by language.
* This is particularly important in programming languages that do not initialize variables to a default value upon declaration. In these instances, the value that a variable will contain after declaration is indeterminate which can cause issues. In fact, that value could be different each time the program is ran.
* Note: This resource should not be considered a definitive or exhaustive coding guideline.


---

# D3-VTV: Variable Type Validation

**Reference:** https://d3fend.mitre.org/technique/D3-VTV/  

## Definition
Ensuring that a variable has the correct type.

## Parent Class(es)
- Source Code Hardening

## Relationships
- **hardens:** Pointer Dereferencing Function
- **kb-reference:** Reference - Type Systems

## Knowledge Base Article
## How it Works
A developer should consider how the variable will be used throughout the program and choose the correct variable type.
A developer should programmatically check if a variable has the correct (expected) type before using that variable.

## Considerations
* The result of an operation on an unexpected variable type will vary based on the language.
* Note: This resource should not be considered a definitive or exhaustive coding guideline.


---

# D3-VS: Video Surveillance

**Synonym(s):** CCTV Surveillance, Video Monitoring  
**Reference:** https://d3fend.mitre.org/technique/D3-VS/  

## Definition
Monitoring of physical areas via camera video feeds to deter, detect, and investigate unauthorized access and related security events.

## Parent Class(es)
- Physical Access Monitoring

## Relationships
- **kb-reference:** Reference - DHS CCTV Technology Handbook
- **kb-reference:** Reference - NIST Special Publication 800-53 Revision 5 - Security and Privacy Controls for Information Systems and Organizations
- **kb-reference:** Reference - ONVIF Profile S
- **monitors:** Digital Camera

## Knowledge Base Article
## How it works

Video surveillance uses digital cameras that stream to a video management system (VMS) or network video recorder (NVR) for live monitoring, recording, and retrieval. Recording can be continuous or event-driven using analytics (motion in regions of interest, line crossing) or external triggers (access denials, sensor alarms). Time synchronization aligns video with other logs, while health monitoring detects camera outages and tamper. Secure export workflows preserve integrity for investigations.

## Considerations

* Plan camera placement and coverage to avoid occlusions and handle challenging lighting; select lenses and mounting to capture entry points and critical areas.
* Size storage and bandwidth for the intended retention period by choosing appropriate resolution, frame rate, and compression, and monitor capacity over time.
* Secure cameras and management systems with unique credentials, timely firmware updates, encrypted transport, and network segmentation to limit exposure.
* Address privacy and legal obligations with visible notice, role-based access to footage, and retention policies aligned with regulations and organizational policy.
* Monitor system health and build resilience with tamper and heartbeat alerts, recorder failover where needed, and accurate time synchronization for correlation.


---

# D3-WSAM: Web Session Access Mediation

**Reference:** https://d3fend.mitre.org/technique/D3-WSAM/  

## Definition
Web session access mediation secures user sessions in web applications by employing robust authentication and integrity validation, along with adaptive threat mitigation techniques, to ensure that access to web resources is authorized and protected from session-related attacks.

## Parent Class(es)
- Network Resource Access Mediation

## Relationships
- **isolates:** Service Application Process
- **kb-reference:** Reference - Special Publication 800-41 Revision 1 Guidelines on Firewalls and Firewall Policy

## Knowledge Base Article
## How it works

Web Session Access Mediation involves managing user access to web applications and services, ensuring secure and authorized sessions. This includes authenticating users, maintaining session integrity, and protecting against threats like session hijacking. Examples include accessing corporate intranets, SaaS applications, or online portals.


---

# D3-WSAA: Web Session Activity Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-WSAA/  

## Definition
Monitoring changes in user web session behavior by comparing current web session activity to a baseline behavior profile or a catalog of predetermined malicious behavior.

## Parent Class(es)
- User Behavior Analysis

## Relationships
- **analyzes:** Web Resource Access
- **kb-reference:** Reference - Host intrusion prevention system using software and user behavior analysis - Sophos Ltd
- **kb-reference:** Reference - System and Method for Detection of a Change in Behavior in the Use of a Website Through Vector Velocity Analysis - Silver Tail Systems
- **kb-reference:** Reference - System and Method for Network Security Including Detection of Attacks Through Partner Websites - EMC IP Holding Co LLC
- **kb-reference:** Reference - System and method thereof for identifying and responding to security incidents based on preemptive forensics - Palo Alto Networks Inc

## Knowledge Base Article
## How it works
User web session data is collected over a period of time to create a user behavior profile. Data collected includes clicks made on a website, average time between clicks, filling out web forms, order in which pages are viewed, and downloading files. Current user web session behavior is then compared against the use behavior profile to identify anomalies and a likelihood that the current user web session is malicious. Current user web session behavior can also be compared to predetermined known malicious behavior profiles that are developed through analysis of malware in run time at a threat research facility.

## Considerations
* Potential for false positives from anomalies that are not associated with malicious activity.
* Attackers may not differentiate their web session activity enough to trigger an alert.
