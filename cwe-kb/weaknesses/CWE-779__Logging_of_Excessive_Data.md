# CWE-779: Logging of Excessive Data

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/779.html  

## Description
The product logs too much information, making log files hard to process and possibly hindering recovery efforts or forensic analysis after an attack.

## Extended Description
While logging is a good practice in general, and very high levels of logging are appropriate for debugging stages of development, too much logging in a production environment might hinder a system administrator's ability to detect anomalous conditions. This can provide cover for an attacker while attempting to penetrate a system, clutter the audit trail for forensic analysis, or make it more difficult to debug problems in a production environment.

## Related Weaknesses
- ChildOf: CWE-400

## Common Consequences
- Scope: Availability; Impact: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Other) — Log files can become so large that they consume excessive resources, such as disk and CPU, which can hinder the performance of the system.
- Scope: Non-Repudiation; Impact: Hide Activities — Logging too much information can make the log files of less use to forensics analysts and developers when trying to diagnose a problem or recover from an attack.
- Scope: Non-Repudiation; Impact: Hide Activities — If system administrators are unable to effectively process log files, attempted attacks may go undetected, possibly leading to eventual system compromise.

## Potential Mitigations
- [Architecture and Design] Suppress large numbers of duplicate log messages and replace them with periodic summaries. For example, syslog may include an entry that states "last message repeated X times" when recording repeated events.
- [Architecture and Design] Support a maximum size for the log file that can be controlled by the administrator. If the maximum size is reached, the admin should be notified. Also, consider reducing functionality of the product. This may result in a denial-of-service to legitimate product users, but it will prevent the product from adversely impacting the entire system.
- [Implementation] Adjust configurations appropriately when the product is transitioned from a debug state to production.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
