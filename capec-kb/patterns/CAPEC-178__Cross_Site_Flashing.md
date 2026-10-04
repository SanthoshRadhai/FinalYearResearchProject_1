# CAPEC-178: Cross-Site Flashing

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/178.html  

## Description
An attacker is able to trick the victim into executing a Flash document that passes commands or calls to a Flash player browser plugin, allowing the attacker to exploit native Flash functionality in the client browser. This attack pattern occurs where an attacker can provide a crafted link to a Flash document (SWF file) which, when followed, will cause additional malicious instructions to be executed. The attacker does not need to serve or control the Flash document. The attack takes advantage of the fact that Flash files can reference external URLs. If variables that serve as URLs that the Flash application references can be controlled through parameters, then by creating a link that includes values for those parameters, an attacker can cause arbitrary content to be referenced and possibly executed by the targeted Flash application.

## Related Attack Patterns
- ChildOf: CAPEC-182

## Prerequisites
- The targeted Flash application must reference external URLs and the locations thus referenced must be controllable through parameters. The Flash application must fail to sanitize such parameters against malicious manipulation. The victim must follow a crafted link created by the attacker.

## Skills Required
- [Medium] knowledge of Flash internals, parameters and remote referencing.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Implementation: Only allow known URL to be included as remote flash movies in a flash application
- Configuration: Properly configure the crossdomain.xml file to only include the known domains that should host remote flash movies.

## Related Weaknesses (CWE)
- CWE-601
