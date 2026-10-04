# D3-FIM: File Integrity Monitoring

**Reference:** https://d3fend.mitre.org/technique/D3-FIM/  

## Definition
Detecting any suspicious changes to files in a computer system.

## Parent Class(es)
- Platform Monitoring

## Relationships
- **analyzes:** File
- **kb-reference:** Reference - File Integrity Monitoring in Microsoft Defender for Cloud - Microsoft
- **kb-reference:** Reference - Tripwire

## Knowledge Base Article
## How it Works
There are a number of tools in Windows and Unix that can monitor specific files in a system and generate alerts if any artifacts have been created, modified, or removed. They accomplish this by comparing the current artifacts to a previous snapshot.

Unix - Unix systems have a file integrity checker tool called tripwire. Tripwire first initializes a database that serves as a basis for comparison and can then scan the system to compare the state of the current file system against the initial baseline database. Additionally, users can define policies that specify potential violations.

Windows - In Microsoft Azure, file integrity monitoring can be enabled which can track file and registry key creation, removals, and modifications of specific files.

## Considerations
Files can change constantly due to the non-static nature of a computer system. File Integrity Monitoring works best when pointed at a narrow scope of critical files to limit the number of unnecessary files that may be modified over the course of normal use. The accuracy and precision of defined policies also affect the efficacy of this technique.
