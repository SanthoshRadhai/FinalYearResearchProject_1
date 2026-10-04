# CWE-530: Exposure of Backup File to an Unauthorized Control Sphere

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/530.html  

## Description
A backup file is stored in a directory or archive that is made accessible to unauthorized actors.

## Extended Description
Often, older backup files are renamed with an extension such as .~bk to distinguish them from production files. The source code for old files that have been renamed in this manner and left in the webroot can often be retrieved. This renaming may have been performed automatically by the web server, or manually by the administrator.

## Related Weaknesses
- ChildOf: CWE-552

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — At a minimum, an attacker who retrieves this file would have all the information contained in it, whether that be database calls, the format of parameters accepted by the application, or simply information regarding the architectural structure of your site.

## Potential Mitigations
- [Policy] Recommendations include implementing a security policy within your organization that prohibits backing up web application source code in the webroot.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
