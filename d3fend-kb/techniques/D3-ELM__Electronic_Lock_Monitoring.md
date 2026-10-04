# D3-ELM: Electronic Lock Monitoring

**Synonym(s):** Door Lock Monitoring, Lock State Monitoring  
**Reference:** https://d3fend.mitre.org/technique/D3-ELM/  

## Definition
Monitoring electronic lock and door hardware states and access events (e.g., locked/unlocked, access granted/denied, door forced/held, tamper) to detect and respond to unauthorized entry.

## Parent Class(es)
- Physical Access Monitoring

## Relationships
- **kb-reference:** Reference - FIPS 201-3
- **kb-reference:** Reference - NIST SP 800-116 Rev. 1
- **kb-reference:** Reference - NIST Special Publication 800-53 Revision 5 - Security and Privacy Controls for Information Systems and Organizations
- **kb-reference:** Reference - SIA OSDP v2.2
- **monitors:** Electronic Combination Lock

## Knowledge Base Article
## How it works

Electronic lock monitoring collects status and events from door controllers, readers (badge/PIV, keypad), and door hardware (door position switch, request-to-exit, bolt/latch, tamper). The physical access control system (PACS) logs access decisions, correlates door-held/forced conditions, and generates alarms for response. Secure, supervised reader links, such as Open Supervised Device Protocol (OSDP), help detect wiring faults and reduce credential interception. Integration with video systems can pop relevant camera views on lock-related alarms.

## Considerations

* Use encrypted, supervised reader-to-controller protocols to protect credentials and detect wiring faults.
* Harden door controllers and isolate the PACS network to limit the attack surface.
* Configure fail-safe or fail-secure behavior and emergency release to meet life-safety requirements.
* Tune alarms for door-held, door-forced, and invalid retries to reduce noise while catching misuse.
* Supervise inputs, provide backup power, and regularly test door, bolt, and tamper sensors to ensure reliability.
