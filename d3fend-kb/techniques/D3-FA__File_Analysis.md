# D3-FA: File Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-FA/  

## Definition
File Analysis is an analytic process to determine a file's status. For example: virus, trojan, benign, malicious, trusted, unauthorized, sensitive, etc.

## Parent Class(es)
- Defensive Technique

## Relationships
- **analyzes:** File
- **enables:** Detect

## Knowledge Base Article
## Technique Overview
Some techniques use file signatures or file metadata to compare against historical collections of malware. Files may also be compared against a source of ground truth such as cryptographic signatures. Examining files for potential malware using pattern matching against file contents/file behavior. Binary code may be dissembled and analyzed for predictive malware behavior, such as API call signatures. Analysis might occur within a protected environment such as a sandbox or live system.
