# D3-FMCV: File Metadata Consistency Validation

**Reference:** https://d3fend.mitre.org/technique/D3-FMCV/  

## Definition
The process of validating the consistency between a file's metadata and its actual content, ensuring that elements like declared lengths, pointers, and checksums accurately describe the file's content.

## Parent Class(es)
- File Format Verification

## Relationships
- **analyzes:** File Content Block Data
- **analyzes:** File Metadata
- **kb-reference:** Reference - Gathering Evidence: Model-Driven Software Engineering in Automated Digital Forensics

## Knowledge Base Article
## How it works

This technique involves validating the consistency between a file's metadata and its actual content. It checks elements like declared lengths, pointers, and checksums to ensure they accurately describe the file's content. For instance, if a header specifies a content block of 50 bytes, this should be verified, and CRC values should be recalculated and compared.
