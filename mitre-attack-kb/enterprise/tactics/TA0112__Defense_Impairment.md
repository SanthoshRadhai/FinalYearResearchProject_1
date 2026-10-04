# TA0112: Defense Impairment

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0112  

## Description
The adversary is trying to break security mechanisms, pipelines, and tooling so defenders can’t see or trust what’s happening.

Defense Impairment consists of techniques that degrade, disable, or undermine the effectiveness and trustworthiness of security controls and monitoring mechanisms. These techniques are characterized by direct interference with defensive systems. The goal is to reduce defenders’ ability to detect, interpret, or respond to adversary activity.

## Techniques in This Tactic
- T1112: Modify Registry
- T1207: Rogue Domain Controller
- T1222: File and Directory Permissions Modification
- T1222.001: Windows Permissions
- T1222.002: Linux and Mac Permissions
- T1484: Domain or Tenant Policy Modification
- T1484.001: Group Policy Modification
- T1484.002: Trust Modification
- T1553: Subvert Trust Controls
- T1553.001: Gatekeeper Bypass
- T1553.002: Code Signing
- T1553.003: SIP and Trust Provider Hijacking
- T1553.004: Install Root Certificate
- T1553.005: Mark-of-the-Web Bypass
- T1553.006: Code Signing Policy Modification
- T1556: Modify Authentication Process
- T1556.001: Domain Controller Authentication
- T1556.002: Password Filter DLL
- T1556.003: Pluggable Authentication Modules
- T1556.004: Network Device Authentication
- T1556.005: Reversible Encryption
- T1556.006: Multi-Factor Authentication
- T1556.007: Hybrid Identity
- T1556.008: Network Provider DLL
- T1556.009: Conditional Access Policies
- T1578: Modify Cloud Compute Infrastructure
- T1578.001: Create Snapshot
- T1578.002: Create Cloud Instance
- T1578.003: Delete Cloud Instance
- T1578.004: Revert Cloud Instance
- T1578.005: Modify Cloud Compute Configurations
- T1599: Network Boundary Bridging
- T1599.001: Network Address Translation Traversal
- T1600: Weaken Encryption
- T1600.001: Reduce Key Space
- T1600.002: Disable Crypto Hardware
- T1601: Modify System Image
- T1601.001: Patch System Image
- T1601.002: Downgrade System Image
- T1647: Plist File Modification
- T1666: Modify Cloud Resource Hierarchy
- T1685: Disable or Modify Tools
- T1685.001: Disable or Modify Windows Event Log
- T1685.002: Disable or Modify Cloud Log
- T1685.003: Modify or Spoof Tool UI
- T1685.004: Disable or Modify Linux Audit System Log
- T1685.005: Clear Windows Event Logs
- T1685.006: Clear Linux or Mac System Logs
- T1686: Disable or Modify System Firewall
- T1686.001: Cloud Firewall
- T1686.002: Network Device Firewall
- T1686.003: Windows Host Firewall
- T1687: Exploitation for Defense Impairment
- T1688: Safe Mode Boot
- T1689: Downgrade Attack
- T1690: Prevent Command History Logging
