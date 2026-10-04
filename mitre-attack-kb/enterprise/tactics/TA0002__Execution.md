# TA0002: Execution

**Type:** Tactic  
**Reference:** https://attack.mitre.org/tactics/TA0002  

## Description
The adversary is trying to run malicious code.

Execution consists of techniques that result in adversary-controlled code running on a local or remote system. Techniques that run malicious code are often paired with techniques from all other tactics to achieve broader goals, like exploring a network or stealing data. For example, an adversary might use a remote access tool to run a PowerShell script that does Remote System Discovery.

## Techniques in This Tactic
- T1047: Windows Management Instrumentation
- T1053: Scheduled Task/Job
- T1053.002: At
- T1053.003: Cron
- T1053.005: Scheduled Task
- T1053.006: Systemd Timers
- T1053.007: Container Orchestration Job
- T1059: Command and Scripting Interpreter
- T1059.001: PowerShell
- T1059.002: AppleScript
- T1059.003: Windows Command Shell
- T1059.004: Unix Shell
- T1059.005: Visual Basic
- T1059.006: Python
- T1059.007: JavaScript
- T1059.008: Network Device CLI
- T1059.009: Cloud API
- T1059.010: AutoHotKey & AutoIT
- T1059.011: Lua
- T1059.012: Hypervisor CLI
- T1059.013: Container CLI/API
- T1072: Software Deployment Tools
- T1106: Native API
- T1127: Trusted Developer Utilities Proxy Execution
- T1127.001: MSBuild
- T1127.002: ClickOnce
- T1127.003: JamPlus
- T1129: Shared Modules
- T1197: BITS Jobs
- T1203: Exploitation for Client Execution
- T1204: User Execution
- T1204.001: Malicious Link
- T1204.002: Malicious File
- T1204.003: Malicious Image
- T1204.004: Malicious Copy and Paste
- T1204.005: Malicious Library
- T1559: Inter-Process Communication
- T1559.001: Component Object Model
- T1559.002: Dynamic Data Exchange
- T1559.003: XPC Services
- T1569: System Services
- T1569.001: Launchctl
- T1569.002: Service Execution
- T1569.003: Systemctl
- T1574: Hijack Execution Flow
- T1574.001: DLL
- T1574.004: Dylib Hijacking
- T1574.005: Executable Installer File Permissions Weakness
- T1574.006: Dynamic Linker Hijacking
- T1574.007: Path Interception by PATH Environment Variable
- T1574.008: Path Interception by Search Order Hijacking
- T1574.009: Path Interception by Unquoted Path
- T1574.010: Services File Permissions Weakness
- T1574.011: Services Registry Permissions Weakness
- T1574.012: COR_PROFILER
- T1574.013: KernelCallbackTable
- T1574.014: AppDomainManager
- T1609: Container Administration Command
- T1610: Deploy Container
- T1648: Serverless Execution
- T1651: Cloud Administration Command
- T1674: Input Injection
- T1675: ESXi Administration Command
- T1677: Poisoned Pipeline Execution
