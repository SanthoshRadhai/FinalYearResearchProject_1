# D3-ER: Email Removal

**Synonym(s):** Email Deletion  
**Reference:** https://d3fend.mitre.org/technique/D3-ER/  

## Definition
The email removal technique deletes email files from system storage.

## Parent Class(es)
- File Eviction

## Relationships
- **deletes:** Email
- **kb-reference:** Reference - System and method for scanning remote services to locate stored objects with malware
- **may-access:** Mail Server

## Knowledge Base Article
## How it works

Email removal is a technique that can be used to prevent a user from executing malware or responding to phishing attempts. Security software or users themselves may detect malicious or suspicious email in a local or remote mail folder email and then employ this technique.

## Considerations

For email that needs to be removed, an infosec organization may choose to take additional follow-up actions (such as blocking the sources or notifying providers), rather than only relying on email deletion.

For the case where users detect likely suspicious email files, the organization should consider implementing a means for reporting these emails to their infosec organization.

Email files may propagate through many storage systems across an organization's systems over time, so early detection and blocking helps avoid residual, latent stores of malicious email content in the enterprise.
