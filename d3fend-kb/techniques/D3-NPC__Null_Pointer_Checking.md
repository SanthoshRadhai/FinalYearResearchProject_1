# D3-NPC: Null Pointer Checking

**Synonym(s):** Nil Pointer Checking  
**Reference:** https://d3fend.mitre.org/technique/D3-NPC/  

## Definition
Checking if a pointer is NULL.

## Parent Class(es)
- Pointer Validation

## Relationships
- **hardens:** Memory Free Function
- **hardens:** Pointer Dereferencing Function
- **kb-reference:** Reference - Null Pointer Checking - SEI
- **kb-reference:** Reference - Null Pointer Dereferencing - CWE-476
- **kb-reference:** Reference - Pointer Validation Function - SEI

## Knowledge Base Article

## How it Works
Programmatically checking if a pointer is NULL before use.

## Considerations
* Pointers should be checked prior to use after they have, or may have been modified.
* Note that it may vary by circumstance whether the caller, or callee is responsible for checking if a pointer is NULL.
* Note: This resource should not be considered a definitive or exhaustive coding guideline.
