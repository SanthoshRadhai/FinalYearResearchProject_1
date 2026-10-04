# CWE-1311: Improper Translation of Security Attributes by Fabric Bridge

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1311.html  

## Description
The bridge incorrectly translates security attributes from either trusted to untrusted or from untrusted to trusted when converting from one fabric protocol to another.

## Extended Description
A bridge allows IP blocks supporting different fabric protocols to be integrated into the system. Fabric end-points or interfaces usually have dedicated signals to transport security attributes. For example, HPROT signals in AHB, AxPROT signals in AXI, and MReqInfo and SRespInfo signals in OCP. The values on these signals are used to indicate the security attributes of the transaction. These include the immutable hardware identity of the controller initiating the transaction, privilege level, and type of transaction (e.g., read/write, cacheable/non-cacheable, posted/non-posted). A weakness can arise if the bridge IP block, which translates the signals from the protocol used in the IP block endpoint to the protocol used by the central bus, does not properly translate the security attributes. As a result, the identity of the initiator could be translated from untrusted to trusted or vice-versa. This could result in access-control bypass, privilege escalation, or denial of service.

## Related Weaknesses
- ChildOf: CWE-284

## Common Consequences
- Scope: Confidentiality, Integrity, Access Control; Impact: Modify Memory, Read Memory, Gain Privileges or Assume Identity, Bypass Protection Mechanism, Execute Unauthorized Code or Commands

## Potential Mitigations
- [Architecture and Design] The translation must map signals in such a way that untrusted agents cannot map to trusted agents or vice-versa.
- [Implementation] Ensure that the translation maps signals in such a way that untrusted agents cannot map to trusted agents or vice-versa.

## Demonstrative Examples (summary)
- The bridge interfaces between OCP and AHB end points. OCP uses MReqInfo signal to indicate security attributes, whereas AHB uses HPROT signal to indicate the security attributes. The width of MReqInfo can be customized as needed. In this example, MReqInfo is 5-bits wide and carries the privilege level of the OCP controller. The values 5'h11, 5'h10, 5'h0F, 5'h0D, 5'h0C, 5'h0B, 5'h09, 5'h08, 5'h04, and 5'h02 in MReqInfo indicate that the request is coming from a privileged state of the OCP bus controller. Values 5'h1F, 5'h0E, and 5'h00 indicate untrusted, privilege state. Though HPROT is a 5-bit signal, we only consider the lower, two bits in this example. HPROT values 2'b00 and 2'b10 are considered trusted, and 2'b01 and 2'b11 are considered untrusted. The OCP2AHB bridge is expected to translate trusted identities on the controller side to trusted identities on the responder side. Similarly, it is expected to translate untrusted identities on the controller side to untrusted identities on the responder side.
