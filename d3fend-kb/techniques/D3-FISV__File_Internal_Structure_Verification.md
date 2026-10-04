# D3-FISV: File Internal Structure Verification

**Reference:** https://d3fend.mitre.org/technique/D3-FISV/  

## Definition
The process of checking specific static values within a file, such as file signatures or magic numbers, to ensure they match the expected values defined by the file format specification.

## Parent Class(es)
- File Format Verification

## Relationships
- **analyzes:** File Content Block
- **kb-reference:** Reference - Carving Contiguous and Fragmented Files with Fast Object Validation
- **kb-reference:** Reference - Gathering Evidence: Model-Driven Software Engineering in Automated Digital Forensics

## Knowledge Base Article
## How it works

File format specifications often define expected values for specific fields. A common example are file signatures, or magic numbers, which are used to quickly identify files. Another example is within the Compound Document Header of Microsoft Office files, the 29th and 30th byte identifies the byte order, specifically 0xFFFE for little-endian. This technique verifies that the file's static values match the values of the declared file format's specification.
