# D3-DNR: Decoy Network Resource

**Reference:** https://d3fend.mitre.org/technique/D3-DNR/  

## Definition
Deploying a network resource for the purposes of deceiving an adversary.

## Parent Class(es)
- Decoy Object

## Relationships
- **kb-reference:** Reference - Automatically generating network resource groups and assigning customized decoy policies thereto - Illusive Networks Ltd
- **kb-reference:** Reference - Deception-Based Responses to Security Attacks - Crowdstrike Inc
- **kb-reference:** Reference - Dynamic selection and generation of a virtual clone for detonation of suspicious content within a honey network - Palo Alto Networks Inc
- **kb-reference:** Reference - System and method for identifying the presence of malware using mini-traps set at network endpoints - Fidelis Cybersecurity Solutions Inc
- **spoofs:** Network Resource

## Knowledge Base Article
## How it works
Decoy network resources are deployed to web application servers, network file shares, or other network based sharing services.

A "honeypot" may serve a variety of decoy network resources.

## Considerations

* Developing a deployment and placement strategy for the decoy network resource.
* Personnel responsible for creation of decoy networks should consider the potential for resource exhaustion through denial of service attacks.

## Examples
* Honeypots are typically used to mimic a known system with fake vulnerabilities. This may attract attackers to the honeypot.
* Decoy accounts are also used to scan for attempted logins. The decoy accounts can provide security analysts with the attacker's potential intents and strategies.
* Tarpits are used to monitor unallocated IP space for unauthorized network activity.
