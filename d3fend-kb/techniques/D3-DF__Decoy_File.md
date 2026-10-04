# D3-DF: Decoy File

**Reference:** https://d3fend.mitre.org/technique/D3-DF/  

## Definition
A file created for the purposes of deceiving an adversary.

## Parent Class(es)
- Decoy Object

## Relationships
- **kb-reference:** Reference - Open source intelligence deceptions - Illusive Networks Ltd
- **kb-reference:** Reference - Supply chain cyber-deception - Cymmetria, Inc.
- **kb-reference:** Reference - System and a method for identifying the presence of malware and ransomware using mini-traps set at network endpoints - Fidelis Cybersecurity Solutions Inc
- **kb-reference:** Reference - System and methods thereof for preventing ransomware from encrypting data elements stored in a memory of a computer-based system - Palo Alto Networks Inc
- **spoofs:** File

## Knowledge Base Article
## How it works
The decoy file is made available as a local or network resource. Accesses to the file may be monitored. The files may be configurations, documents, executables, or other file types.


## Considerations
Properties of the file such as cryptographic checksums, file creation date, file modified date, file size, file owner etc may be modified to improve the credibility of the file.

## Example
* A CSV file with decoy user credentials is placed on a system. The system or network is then monitored to detect any accesses to the decoy files.
