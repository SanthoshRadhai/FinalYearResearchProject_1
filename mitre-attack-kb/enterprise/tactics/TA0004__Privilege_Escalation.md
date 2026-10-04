# TA0004: Privilege Escalation

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0004  

## Description
The adversary is trying to gain higher-level permissions.

Privilege Escalation consists of techniques that adversaries use to gain higher-level permissions on a system or network. Adversaries can often enter and explore a network with unprivileged access but require elevated permissions to follow through on their objectives. Common approaches are to take advantage of system weaknesses, misconfigurations, and vulnerabilities. Examples of elevated access include: 

* SYSTEM/root level
* local administrator
* user account with admin-like access 
* user accounts with access to specific system or perform specific function

These techniques often overlap with Persistence techniques, as OS features that let an adversary persist can execute in an elevated context.

## Techniques in This Tactic
- T1037: Boot or Logon Initialization Scripts
- T1037.001: Logon Script (Windows)
- T1037.002: Login Hook
- T1037.003: Network Logon Script
- T1037.004: RC Scripts
- T1037.005: Startup Items
- T1053: Scheduled Task/Job
- T1053.002: At
- T1053.003: Cron
- T1053.005: Scheduled Task
- T1053.006: Systemd Timers
- T1053.007: Container Orchestration Job
- T1055: Process Injection
- T1055.001: Dynamic-link Library Injection
- T1055.002: Portable Executable Injection
- T1055.003: Thread Execution Hijacking
- T1055.004: Asynchronous Procedure Call
- T1055.005: Thread Local Storage
- T1055.008: Ptrace System Calls
- T1055.009: Proc Memory
- T1055.011: Extra Window Memory Injection
- T1055.012: Process Hollowing
- T1055.013: Process Doppelgänging
- T1055.014: VDSO Hijacking
- T1055.015: ListPlanting
- T1068: Exploitation for Privilege Escalation
- T1078: Valid Accounts
- T1078.001: Default Accounts
- T1078.002: Domain Accounts
- T1078.003: Local Accounts
- T1078.004: Cloud Accounts
- T1098: Account Manipulation
- T1098.001: Additional Cloud Credentials
- T1098.002: Additional Email Delegate Permissions
- T1098.003: Additional Cloud Roles
- T1098.004: SSH Authorized Keys
- T1098.005: Device Registration
- T1098.006: Additional Container Cluster Roles
- T1098.007: Additional Local or Domain Groups
- T1134: Access Token Manipulation
- T1134.001: Token Impersonation/Theft
- T1134.002: Create Process with Token
- T1134.003: Make and Impersonate Token
- T1134.004: Parent PID Spoofing
- T1134.005: SID-History Injection
- T1484: Domain or Tenant Policy Modification
- T1484.001: Group Policy Modification
- T1484.002: Trust Modification
- T1543: Create or Modify System Process
- T1543.001: Launch Agent
- T1543.002: Systemd Service
- T1543.003: Windows Service
- T1543.004: Launch Daemon
- T1543.005: Container Service
- T1546: Event Triggered Execution
- T1546.001: Change Default File Association
- T1546.002: Screensaver
- T1546.003: Windows Management Instrumentation Event Subscription
- T1546.004: Unix Shell Configuration Modification
- T1546.005: Trap
- T1546.006: LC_LOAD_DYLIB Addition
- T1546.007: Netsh Helper DLL
- T1546.008: Accessibility Features
- T1546.009: AppCert DLLs
- T1546.010: AppInit DLLs
- T1546.011: Application Shimming
- T1546.012: Image File Execution Options Injection
- T1546.013: PowerShell Profile
- T1546.014: Emond
- T1546.015: Component Object Model Hijacking
- T1546.016: Installer Packages
- T1546.017: Udev Rules
- T1546.018: Python Startup Hooks
- T1547: Boot or Logon Autostart Execution
- T1547.001: Registry Run Keys / Startup Folder
- T1547.002: Authentication Package
- T1547.003: Time Providers
- T1547.004: Winlogon Helper DLL
- T1547.005: Security Support Provider
- T1547.006: Kernel Modules and Extensions
- T1547.007: Re-opened Applications
- T1547.008: LSASS Driver
- T1547.009: Shortcut Modification
- T1547.010: Port Monitors
- T1547.012: Print Processors
- T1547.013: XDG Autostart Entries
- T1547.014: Active Setup
- T1547.015: Login Items
- T1548: Abuse Elevation Control Mechanism
- T1548.001: Setuid and Setgid
- T1548.002: Bypass User Account Control
- T1548.003: Sudo and Sudo Caching
- T1548.004: Elevated Execution with Prompt
- T1548.005: Temporary Elevated Cloud Access
- T1548.006: TCC Manipulation
- T1611: Escape to Host
