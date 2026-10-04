# CAPEC-579: Replace Winlogon Helper DLL

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/579.html  

## Description
Winlogon is a part of Windows that performs logon actions. In Windows systems prior to Windows Vista, a registry key can be modified that causes Winlogon to load a DLL on startup. Adversaries may take advantage of this feature to load adversarial code at startup.

## Related Attack Patterns
- ChildOf: CAPEC-542

## Mitigations
- Changes to registry entries in "HKLM\Software\Microsoft\Windows NT\Winlogon\Notify" that do not correlate with known software, patch cycles, etc are suspicious. New DLLs written to System32 which do not correlate with known good software or patching may be suspicious.

## Related Weaknesses (CWE)
- CWE-15
