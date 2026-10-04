# D3-DUC: Decoy User Credential

**Reference:** https://d3fend.mitre.org/technique/D3-DUC/  

## Definition
A Credential created for the purpose of deceiving an adversary.

## Parent Class(es)
- Decoy Object

## Relationships
- **kb-reference:** Reference - Decoy and deceptive data object technology - Cymmetria Inc
- **kb-reference:** Reference - Decoy Network-Based Service for Deceiving Attackers - Amazon Technologies
- **kb-reference:** Reference - System and method for identifying the presence of malware using mini-traps set at network endpoints - Fidelis Cybersecurity Solutions Inc
- **spoofs:** Credential

## Knowledge Base Article
## How it works
A detection analytic is developed to determine when a user uses decoy credentials. Subsequent actions by that user may be monitored or controlled by the defender.

A credential may be:
 * Domain username and password
 * Local system username and password

## Considerations
* Decoy credentials should be integrated with a larger decoy environment to ensure that when decoy credentials are compromised, the credentials are used to interact with a decoy asset that is being monitored.
* Continuous maintenance and updates are needed to ensure the legitimacy of the larger decoy environment and specifically the assets that utilize the decoy credentials.
