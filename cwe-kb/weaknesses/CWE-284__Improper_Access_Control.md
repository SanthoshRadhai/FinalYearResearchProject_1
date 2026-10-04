# CWE-284: Improper Access Control

**Abstraction:** Pillar  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/284.html  

## Description
The product does not restrict or incorrectly restricts access to a resource from an unauthorized actor.

## Extended Description
Access control involves the use of several protection mechanisms such as: Authentication (proving the identity of an actor) Authorization (ensuring that a given actor can access a resource), and Accountability (tracking of activities that were performed) When any mechanism is not applied or otherwise fails, attackers can compromise the security of the product by gaining privileges, reading sensitive information, executing commands, evading detection, etc. There are two distinct behaviors that can introduce access control weaknesses: Specification: incorrect privileges, permissions, ownership, etc. are explicitly specified for either the user or the resource (for example, setting a password file to be world-writable, or giving administrator capabilities to a guest user). This action could be performed by the program or the administrator. Enforcement: the mechanism contains errors that prevent it from properly enforcing the specified access control requirements (e.g., allowing the user to specify their own privileges, or allowing a syntactically-incorrect ACL to produce insecure settings). This problem occurs within the program itself, in that it does not actually enforce the intended security policy that the administrator specifies.

## Common Consequences
- Scope: Other; Impact: Varies by Context

## Potential Mitigations
- [Architecture and Design, Operation] Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software.
- [Architecture and Design] Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.

## Demonstrative Examples (summary)
- This code temporarily raises the program's privileges to allow creation of a new user folder.
- This function runs an arbitrary SQL query on a given database, returning the result of the query.
- In 2022, the OT:ICEFALL study examined products by 10 different Operational Technology (OT) vendors. The researchers reported 56 vulnerabilities and said that the products were "insecure by design" [REF-1283]. If exploited, these vulnerabilities often allowed adversaries to change how the products operated, ranging from denial of service to changing the code that the products executed. Since these products were often used in industries such as power, electrical, water, and others, there could even be safety implications.
