# D3-FAPA: File Access Pattern Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-FAPA/  

## Definition
Analyzing the files accessed by a process to identify unauthorized activity.

## Parent Class(es)
- Process Analysis

## Relationships
- **analyzes:** Local Resource Access
- **kb-reference:** Reference - File-modifying malware detection - Crowdstrike Inc

## Knowledge Base Article
## How it works
File modifying malware such as wipers and ransomware are detected by identifying file access patterns that are associated with a malicious process. Examples of file access patterns include accessing a large number of files, accessing multiple file types, files being accessed located in multiple locations in a directory, and copying a file and encrypting the contents of that file into a copy.

## Considerations
Certain file access actions may not be statistically different from authorized activity.
