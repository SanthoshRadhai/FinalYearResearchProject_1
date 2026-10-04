# CWE-1298: Hardware Logic Contains Race Conditions

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1298.html  

## Description
A race condition in the hardware logic results in undermining security guarantees of the system.

## Extended Description
A race condition in logic circuits typically occurs when a logic gate gets inputs from signals that have traversed different paths while originating from the same source. Such inputs to the gate can change at slightly different times in response to a change in the source signal. This results in a timing error or a glitch (temporary or permanent) that causes the output to change to an unwanted state before settling back to the desired state. If such timing errors occur in access control logic or finite state machines that are implemented in security sensitive flows, an attacker might exploit them to circumvent existing protections.

## Related Weaknesses
- ChildOf: CWE-362

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism, Gain Privileges or Assume Identity, Alter Execution Logic

## Potential Mitigations
- [Architecture and Design] Adopting design practices that encourage designers to recognize and eliminate race conditions, such as Karnaugh maps, could result in the decrease in occurrences of race conditions.
- [Implementation] Logic redundancy can be implemented along security critical paths to prevent race conditions. To avoid metastability, it is a good practice in general to default to a secure state in which access is not given to untrusted agents.

## Demonstrative Examples (summary)
- The code below shows a 2x1 multiplexor using logic gates. Though the code shown below results in the minimum gate solution, it is disjoint and causes glitches.
- The example code is taken from the DMA (Direct Memory Access) module of the buggy OpenPiton SoC of HACK@DAC'21. The DMA contains a finite-state machine (FSM) for accessing the permissions using the physical memory protection (PMP) unit. PMP provides secure regions of physical memory against unauthorized access. It allows an operating system or a hypervisor to define a series of physical memory regions and then set permissions for those regions, such as read, write, and execute permissions. When a user tries to access a protected memory area (e.g., through DMA), PMP checks the access of a PMP address (e.g., pmpaddr_i) against its configuration (pmpcfg_i). If the access violates the defined permissions (e.g., CTRL_ABORT), the PMP can trigger a fault or an interrupt. This access check is implemented in the pmp parametrized module in the below code snippet. The below code assumes that the state of the pmpaddr_i and pmpcfg_i signals will not change during the different DMA states (i.e., CTRL_IDLE to CTRL_DONE) while processing a DMA request (via dma_ctrl_reg). The DMA state machine is implemented using a case statement (not shown in the code snippet).
