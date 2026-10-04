# D3-FCDC: File Content Decompression Checking

**Reference:** https://d3fend.mitre.org/technique/D3-FCDC/  

## Definition
Checking if compressed or encoded data sections can be successfully decompressed or decoded. Can follow with further analysis with semantic knowledge

## Parent Class(es)
- File Format Verification

## Relationships
- **analyzes:** File Content Block Data
- **kb-reference:** Reference - Carving Contiguous and Fragmented Files with Fast Object Validation
- **kb-reference:** Reference - Gathering Evidence: Model-Driven Software Engineering in Automated Digital Forensics

## Knowledge Base Article
## How it works

Some file formats such as JPEGs include encoded or compressed sections. This technique verifies that those expected sections are present and can be properly decoded according to the spec.
