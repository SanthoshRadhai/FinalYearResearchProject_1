# T1575: Native API


**ATT&CK ID:** T1575  
**Domain:** Mitre Mobile Attack  
**Tactic(s):** Defense Evasion, Execution  
**Platforms:** Android  
**Reference:** https://attack.mitre.org/techniques/T1575  

## Description
Adversaries may use Android’s Native Development Kit (NDK) to write native functions that can achieve execution of binaries or functions. Like system calls on a traditional desktop operating system, native code achieves execution on a lower level than normal Android SDK calls.

The NDK allows developers to write native code in C or C++ that is compiled directly to machine code, avoiding all intermediate languages and steps in compilation that higher level languages, like Java, typically have. The Java Native Interface (JNI) is the component that allows Java functions in the Android app to call functions in a native library.(Citation: Google NDK Getting Started)

Adversaries may also choose to use native functions to execute malicious code since native actions are typically much more difficult to analyze than standard, non-native behaviors.(Citation: MITRE App Vetting Effectiveness)

## Known Software Using This Technique
- S0540: Asacub
- S0432: Bread
- S0555: CHEMISTGAMES
- S0529: CarbonSteal
- S1083: Chameleon
- S9005: DocSwap
- S1231: GodFather
- S0544: HenBox
- S1185: LightSpy
- S0545: TERRACOTTA
