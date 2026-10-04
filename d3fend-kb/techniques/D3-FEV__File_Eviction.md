# D3-FEV: File Eviction

**Reference:** https://d3fend.mitre.org/technique/D3-FEV/  

## Definition
File eviction techniques delete files from system storage.

## Parent Class(es)
- Object Eviction

## Relationships
- **deletes:** File
- **kb-reference:** Reference - How Does Antivirus Quarantine Work? - Safety Detectives

## Knowledge Base Article
## How it works

Adversaries may place files or programs into a computer's file system to perform malicious actions. As part of the eviction process, these files and programs should be removed to prevent further compromise or reinfection. Examples of malicious types of files are malware which is directly harmful and content files with the intent to deceive users (e.g., phishing.)

On Windows systems, antivirus (AV) software should be used to safely and permanently remove malicious files. AV software may first quarantine a suspected malicious file, which is the process of moving a file from its original location to a new location and makes changes so that it cannot be executed. Users can then verify that the file is not benign and then permanently delete it.

## Considerations

When it is determined that a file should be removed for security purposes, the organization--or systems implementing an organization's policies--may determine that the file should not simply be deleted from the enterprise's mission systems, but be quarantined to a secure system by an approved mechanism, so as to allow follow-up investigation by security staff.

On Windows systems, deleting a file in File Explorer does not permanently delete a file - it sends it to the Recycle Bin instead. The Recycle Bin must be emptied, or alternative steps must be performed to remove files completely. Even then, in some cases the data may persist in disk, so data shredder tools may be needed to completely wipe a file. Thus, AV tools are recommended.
