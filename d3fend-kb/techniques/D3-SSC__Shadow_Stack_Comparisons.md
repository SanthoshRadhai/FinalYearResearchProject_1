# D3-SSC: Shadow Stack Comparisons

**Reference:** https://d3fend.mitre.org/technique/D3-SSC/  

## Definition
Comparing a call stack in system memory with a shadow call stack maintained by the processor to determine unauthorized shellcode activity.

## Parent Class(es)
- Process Analysis

## Relationships
- **analyzes:** Stack Frame
- **kb-reference:** Reference - Threat detection for return oriented programming - Crowdstrike Inc

## Knowledge Base Article
## How it works
This technique compares the call stack stored in system memory with the shadow call stack maintained in the cache memory of the processor.  Mismatches between the two are compared since a return oriented programming attack may only be able to control or spoof the call stack and not the shadow call stack. Mismatches are counted and if the number of mismatches exceeds a certain threshold it is an indication of unauthorized activity and a security response action is performed.

## Considerations
If the threshold for detecting a stack anomaly is low, it may not detect a return-oriented attack with just one gadget, such as a return-to-libc or return-to-plt attack.  Additionally, this technique may not detect JOP (Jump-oriented programming), as the return instruction is not executed.
