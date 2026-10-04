# D3-DST: Decoy Session Token

**Reference:** https://d3fend.mitre.org/technique/D3-DST/  

## Definition
An authentication token created for the purposes of deceiving an adversary.

## Parent Class(es)
- Decoy Object

## Relationships
- **kb-reference:** Reference - Decoy and deceptive data object technology - Cymmetria Inc
- **spoofs:** Session Token

## Knowledge Base Article
## How it works
Usage of decoy session tokens may be monitored to track attacker behavior or otherwise control the beliefs of the attacker.

## Considerations
* Interaction and activity with the decoy session token must be constantly monitored and analyzed to detect unauthorized activity.
* Session tokens are typically short-lived and therefore the decoy must be continuously updated to provide the appearance of it being used in the production environment.
* Automated tools can assist with maintenance and updates by automatically adjusting the decoy session token and environment to mimic the production environment.
