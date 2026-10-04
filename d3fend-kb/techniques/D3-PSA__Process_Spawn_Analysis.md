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
