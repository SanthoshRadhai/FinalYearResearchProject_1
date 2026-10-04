# T0836: Modify Parameter


**ATT&CK ID:** T0836  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impair Process Control  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0836  

## Description
Adversaries may modify parameters used to instruct industrial control system devices. These devices operate via programs that dictate how and when to perform actions based on such parameters. Such parameters can determine the extent to which an action is performed and may specify additional options. For example, a program on a control system device dictating motor processes may take a parameter defining the total number of seconds to run that motor.      

An adversary can potentially modify these parameters to produce an outcome outside of what was intended by the operators. By modifying system and process critical parameters, the adversary may cause [Impact](https://attack.mitre.org/tactics/TA0105) to equipment and/or control processes. Modified parameters may be turned into dangerous, out-of-bounds, or unexpected values from typical operations. For example, specifying that a process run for more or less time than it should, or dictating an unusually high, low, or invalid value as a parameter.

## Mitigations
- M0800: Authorization Enforcement
- M0804: Human User Authentication
- M0818: Validate Program Inputs
- M0947: Audit

## Known Software Using This Technique
- S1165: FrostyGoop
- S1045: INCONTROLLER
- S1072: Industroyer2
- S0603: Stuxnet
