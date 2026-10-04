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
