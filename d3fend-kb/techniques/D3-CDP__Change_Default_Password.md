# D3-CDP: Change Default Password

**Reference:** https://d3fend.mitre.org/technique/D3-CDP/  

## Definition
Changing the default password means replacing the factory-set credentials with a strong, unique password before the device is deployed, preventing unauthorized access.

## Parent Class(es)
- Strong Password Policy

## Relationships
- **hardens:** OT Controller
- **kb-reference:** Reference - CISA CPG Checklist
- **kb-reference:** Reference - NIST SP 800-82R3 Guide to Operational Technology (OT) Security, Section 6.2.1.4.5 Password Authentication
- **kb-reference:** Reference - MITRE ATT&CK - Password Policies
- **strengthens:** Password
- **strengthens:** User Account

## Knowledge Base Article
## How it works
Change the default password as soon as a new device is received. The default credentials are normally documented in an instruction manual that is either packaged with the device, published online through official means, or published online through unofficial means.

## Considerations
* These should be changed before a device is brought online so that an adversary cannot take advantage of these default credentials.
* Strong and complex passwords are preferred if the technology allows.
