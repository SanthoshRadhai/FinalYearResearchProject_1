# T1622: Debugger Evasion


**ATT&CK ID:** T1622  
**Domain:** Mitre Attack  
**Tactic(s):** Stealth, Discovery  
**Platforms:** Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1622  

## Description
Adversaries may employ various means to detect and avoid debuggers. Debuggers are typically used by defenders to trace and/or analyze the execution of potential malware payloads.(Citation: ProcessHacker Github)

Debugger evasion may include changing behaviors based on the results of the checks for the presence of artifacts indicative of a debugged environment. Similar to [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497), if the adversary detects a debugger, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for debugger artifacts before dropping secondary or additional payloads.

Specific checks will vary based on the target and/or adversary. On Windows, this may involve [Native API](https://attack.mitre.org/techniques/T1106) function calls such as <code>IsDebuggerPresent()</code> and <code> NtQueryInformationProcess()</code>, or manually checking the <code>BeingDebugged</code> flag of the Process Environment Block (PEB). On Linux, this may involve querying `/proc/self/status` for the `TracerPID` field, which indicates whether or not the process is being traced by dynamic analysis tools.(Citation: Cado Security P2PInfect 2023)(Citation: Positive Technologies Hellhounds 2023) Other checks for debugging artifacts may also seek to enumerate hardware breakpoints, interrupt assembly opcodes, time checks, or measurements if exceptions are raised in the current process (assuming a present debugger would “swallow” or handle the potential error).(Citation: hasherezade debug)(Citation: AlKhaser Debug)(Citation: vxunderground debug)

Malware may also leverage Structured Exception Handling (SEH) to detect debuggers by throwing an exception and detecting whether the process is suspended. SEH handles both hardware and software expectations, providing control over the exceptions including support for debugging. If a debugger is present, the program’s control will be transferred to the debugger, and the execution of the code will be suspended. If the debugger is not present, control will be transferred to the SEH handler, which will automatically handle the exception and allow the program’s execution to continue.(Citation: Apriorit)

Adversaries may use the information learned from these debugger checks during automated discovery to shape follow-on behaviors. Debuggers can also be evaded by detaching the process or flooding debug logs with meaningless data via messages produced by looping [Native API](https://attack.mitre.org/techniques/T1106) function calls such as <code>OutputDebugStringW()</code>.(Citation: wardle evilquest partii)(Citation: Checkpoint Dridex Jan 2021)

## Known Threat Groups Using This Technique
- G0129: Mustang Panda

## Known Software Using This Technique
- S9027: ANELLDR
- S1087: AsyncRAT
- S1070: Black Basta
- S1039: Bumblebee
- S0694: DRATzarus
- S1111: DarkGate
- S1066: DarkTortilla
- S1160: Latrodectus
- S1202: LockBit 3.0
- S1213: Lumma Stealer
- S1060: Mafalda
- S1228: PUBLOAD
- S1145: Pikabot
- S0013: PlugX
- S9019: PureCrypter
- S0240: ROKRAT
- S1130: Raspberry Robin
- S9037: RustyWater
- S1018: Saint Bot
- S1200: StealBit
- S1183: StrelaStealer
- S1239: TONESHELL
- S0595: ThiefQuest
- S1207: XLoader
