# CAPEC-406: Dumpster Diving

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/406.html  

## Description
An adversary cases an establishment and searches through trash bins, dumpsters, or areas where company information may have been accidentally discarded for information items which may be useful to the dumpster diver. The devastating nature of the items and/or information found can be anything from medical records, resumes, personal photos and emails, bank statements, account details or information about software, tech support logs and so much more, including hardware devices. By collecting this information an adversary may be able to learn important facts about the person or organization that play a role in helping the adversary in their attack.

## Related Attack Patterns
- ChildOf: CAPEC-150
- CanPrecede: CAPEC-163
- CanPrecede: CAPEC-675

## Prerequisites
- An adversary must have physical access to the dumpster or downstream processing facility.

## Consequences
- Scope: Confidentiality; Impact: Other
