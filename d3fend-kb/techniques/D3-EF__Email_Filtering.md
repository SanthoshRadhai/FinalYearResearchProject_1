# D3-EF: Email Filtering

**Reference:** https://d3fend.mitre.org/technique/D3-EF/  

## Definition
Filtering incoming email traffic based on specific criteria.

## Parent Class(es)
- Inbound Traffic Filtering

## Relationships
- **filters:** Email
- **kb-reference:** Reference - System and method for providing anonymous remailing and filtering of electronic mail - Nokia

## Knowledge Base Article
## How it works

Mail filters can be implemented to scan inbound email messages at the initial SMTP connection stage to detect and reject email containing spam and malware.

This technique is distinct from d3f:EmailDeletion because it prevents an email from reaching an user's inbox. This technique can also be used for outbound email traffic.

## Considerations
* The effectiveness of mail filters depend on the completeness of the filter policies
