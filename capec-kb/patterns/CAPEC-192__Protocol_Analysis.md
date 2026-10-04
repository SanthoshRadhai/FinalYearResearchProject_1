# CAPEC-192: Protocol Analysis

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/192.html  

## Description
An adversary engages in activities to decipher and/or decode protocol information for a network or application communication protocol used for transmitting information between interconnected nodes or systems on a packet-switched data network. While this type of analysis involves the analysis of a networking protocol inherently, it does not require the presence of an actual or physical network.

## Prerequisites
- Access to a binary executable.
- The ability to observe and interact with a communication channel between communicating processes.

## Skills Required
- [High] Knowlegde of the Open Systems Interconnection model (OSI model), and famililarity with Wireshark or some other packet analyzer.

## Resources Required
- Depending on the type of analysis, a variety of tools might be required, such as static code and/or dynamic analysis tools. Alternatively, the effort might require debugging programs such as ollydbg, SoftICE, or disassemblers like IDA Pro. In some instances, packet sniffing or packet analyzing programs such as TCP dump or Wireshark are necessary. Lastly, specific protocol analysis might require tools such as PDB (Protocol Debug), or packet injection tools like pcap or Nemesis.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Related Weaknesses (CWE)
- CWE-326
