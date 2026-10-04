# CAPEC-27: Leveraging Race Conditions via Symbolic Links

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/27.html  

## Description
This attack leverages the use of symbolic links (Symlinks) in order to write to sensitive files. An attacker can create a Symlink link to a target file not otherwise accessible to them. When the privileged program tries to create a temporary file with the same name as the Symlink link, it will actually write to the target file pointed to by the attackers' Symlink link. If the attacker can insert malicious content in the temporary file they will be writing to the sensitive file by using the Symlink. The race occurs because the system checks if the temporary file exists, then creates the file. The attacker would typically create the Symlink during the interval between the check and the creation of the temporary file.

## Related Attack Patterns
- ChildOf: CAPEC-29

## Prerequisites
- The attacker is able to create Symlink links on the target host.
- Tainted data from the attacker is used and copied to temporary files.
- The target host does insecure temporary file creation.

## Skills Required
- [Medium] This attack is sophisticated because the attacker has to overcome a few challenges such as creating symlinks on the target host during a precise timing, inserting malicious data in the temporary file and have knowledge about the temporary files created (file name and function which creates them).

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Use safe libraries when creating temporary files. For instance the standard library function mkstemp can be used to safely create temporary files. For shell scripts, the system utility mktemp does the same thing.
- Access to the directories should be restricted as to prevent attackers from manipulating the files. Denying access to a file can prevent an attacker from replacing that file with a link to a sensitive file.
- Follow the principle of least privilege when assigning access rights to files.
- Ensure good compartmentalization in the system to provide protected areas that can be trusted.

## Related Weaknesses (CWE)
- CWE-367
- CWE-61
- CWE-662
- CWE-689
- CWE-667
