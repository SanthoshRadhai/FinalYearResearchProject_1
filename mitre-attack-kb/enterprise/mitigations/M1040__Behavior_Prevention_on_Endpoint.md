# M1040: Behavior Prevention on Endpoint

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1040  

## Description
Behavior Prevention on Endpoint refers to the use of technologies and strategies to detect and block potentially malicious activities by analyzing the behavior of processes, files, API calls, and other endpoint events. Rather than relying solely on known signatures, this approach leverages heuristics, machine learning, and real-time monitoring to identify anomalous patterns indicative of an attack. This mitigation can be implemented through the following measures:

Suspicious Process Behavior:

- Implementation: Use Endpoint Detection and Response (EDR) tools to monitor and block processes exhibiting unusual behavior, such as privilege escalation attempts.
- Use Case: An attacker uses a known vulnerability to spawn a privileged process from a user-level application. The endpoint tool detects the abnormal parent-child process relationship and blocks the action.

Unauthorized File Access:

- Implementation: Leverage Data Loss Prevention (DLP) or endpoint tools to block processes attempting to access sensitive files without proper authorization.
- Use Case: A process tries to read or modify a sensitive file located in a restricted directory, such as /etc/shadow on Linux or the SAM registry hive on Windows. The endpoint tool identifies this anomalous behavior and prevents it.

Abnormal API Calls:

- Implementation: Implement runtime analysis tools to monitor API calls and block those associated with malicious activities.
- Use Case: A process dynamically injects itself into another process to hijack its execution. The endpoint detects the abnormal use of APIs like `OpenProcess` and `WriteProcessMemory` and terminates the offending process.

Exploit Prevention:

- Implementation: Use behavioral exploit prevention tools to detect and block exploits attempting to gain unauthorized access.
- Use Case: A buffer overflow exploit is launched against a vulnerable application. The endpoint detects the anomalous memory write operation and halts the process.

## Techniques Mitigated
- T1003: OS Credential Dumping
- T1003.001: LSASS Memory
- T1006: Direct Volume Access
- T1027: Obfuscated Files or Information
- T1027.009: Embedded Payloads
- T1027.010: Command Obfuscation
- T1027.012: LNK Icon Smuggling
- T1027.013: Encrypted/Encoded File
- T1027.014: Polymorphic Code
- T1036: Masquerading
- T1036.008: Masquerade File Type
- T1047: Windows Management Instrumentation
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
- T1059: Command and Scripting Interpreter
- T1059.005: Visual Basic
- T1059.007: JavaScript
- T1091: Replication Through Removable Media
- T1106: Native API
- T1137: Office Application Startup
- T1137.001: Office Template Macros
- T1137.002: Office Test
- T1137.003: Outlook Forms
- T1137.004: Outlook Home Page
- T1137.005: Outlook Rules
- T1137.006: Add-ins
- T1204: User Execution
- T1204.002: Malicious File
- T1216.001: PubPrn
- T1486: Data Encrypted for Impact
- T1543: Create or Modify System Process
- T1543.003: Windows Service
- T1546.003: Windows Management Instrumentation Event Subscription
- T1559: Inter-Process Communication
- T1559.002: Dynamic Data Exchange
- T1564.014: Extended Attributes
- T1569: System Services
- T1569.002: Service Execution
- T1574: Hijack Execution Flow
- T1574.013: KernelCallbackTable
