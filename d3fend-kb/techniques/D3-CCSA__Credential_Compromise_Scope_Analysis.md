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
