# M1060: Out-of-Band Communications Channel

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M1060  

## Description
Establish secure out-of-band communication channels to ensure the continuity of critical communications during security incidents, data integrity attacks, or in-network communication failures. Out-of-band communication refers to using an alternative, separate communication path that is not dependent on the potentially compromised primary network infrastructure. This method can include secure messaging apps, encrypted phone lines, satellite communications, or dedicated emergency communication systems. Leveraging these alternative channels reduces the risk of adversaries intercepting, disrupting, or tampering with sensitive communications and helps coordinate an effective incident response.(Citation: TrustedSec OOB Communications)(Citation: NIST Special Publication 800-53 Revision 5)

## Techniques Mitigated
- T1114: Email Collection
- T1114.001: Local Email Collection
- T1114.002: Remote Email Collection
- T1114.003: Email Forwarding Rule
- T1213: Data from Information Repositories
- T1213.005: Messaging Applications
- T1489: Service Stop
