# D3-FMVV: File Metadata Value Verification

**Reference:** https://d3fend.mitre.org/technique/D3-FMVV/  

## Definition
The process of checking specific static values within a file, such as file signatures or magic numbers, to ensure they match the expected values defined by the file format specification.

## Parent Class(es)
- File Format Verification

## Relationships
- **analyzes:** File Footer Block
- **analyzes:** File Header Block
- **description:** ## How it works

File format specifications often define expected values for specific fields. A common example are file signatures, or magic numbers, which are used to quickly identify files. Another example is within the Compound Document Header of Microsoft Office files, the 29th and 30th byte identifies the byte order, specifically 0xFFFE for little-endian. This technique verifies that the file's static values match the values of the declared file format's specification.
- **kb-reference:** Reference - Carving Contiguous and Fragmented Files with Fast Object Validation
- **kb-reference:** Reference - Introductory Computer Forensics
