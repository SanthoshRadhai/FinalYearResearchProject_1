# CAPEC-42: MIME Conversion

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/42.html  

## Description
An attacker exploits a weakness in the MIME conversion routine to cause a buffer overflow and gain control over the mail server machine. The MIME system is designed to allow various different information formats to be interpreted and sent via e-mail. Attack points exist when data are converted to MIME compatible format and back.

## Related Attack Patterns
- ChildOf: CAPEC-100

## Prerequisites
- The target system uses a mail server.
- Mail server vendor has not released a patch for the MIME conversion routine, the patch itself has a security hole or does not fix the original problem, or the patch has not been applied to the user's system.

## Skills Required
- [Low] It may be trivial to cause a DoS via this attack pattern
- [High] Causing arbitrary code to execute on the target system.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Stay up to date with third party vendor patches
- Disable the 7 to 8 bit conversion. This can be done by removing the F=9 flag from all Mailer specifications in the sendmail.cf file. For example, a sendmail.cf file with these changes applied should look similar to (depending on your system and configuration): Mlocal, P=/usr/libexec/mail.local, F=lsDFMAw5:/|@qrmn, S=10/30, R=20/40,T=DNS/RFC822/X-Unix,A=mail -d $u Mprog, P=/bin/sh, F=lsDFMoqeu, S=10/30, R=20/40,D=$z:/,T=X-Unix,A=sh -c $u This can be achieved for the "Mlocal" and "Mprog" Mailers by modifying the ".mc" file to include the following lines: define(`LOCAL_MAILER_FLAGS',ifdef(`LOCAL_MAILER_FLAGS',`translit(LOCAL_MAILER_FLAGS, `9')',`rmn')) define(`LOCAL_SHELL_FLAGS',ifdef(`LOCAL_SHELL_FLAGS',`translit(LOCAL_SHELL_FLAGS, `9')',`eu')) and then rebuilding the sendmail.cf file using m4(1). From "Exploiting Software", please see reference below.
- Use the sendmail restricted shell program (smrsh)
- Use mail.local

## Related Weaknesses (CWE)
- CWE-120
- CWE-119
- CWE-74
- CWE-20
