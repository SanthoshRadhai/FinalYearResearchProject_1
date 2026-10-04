# D3-VI: Variable Initialization

**Reference:** https://d3fend.mitre.org/technique/D3-VI/  

## Definition
Setting variables to a known value before use.

## Parent Class(es)
- Source Code Hardening

## Relationships
- **hardens:** Subroutine
- **kb-reference:** Reference - Integer Initialization - GNU C Manual
- **kb-reference:** Reference - Variable Initialization - CWE-457

## Knowledge Base Article
## How it Works
Initializing variables upon declaration ensures that the variable has a known quantity before use.

## Considerations
* Default behavior when declaring variables varies by language.
* This is particularly important in programming languages that do not initialize variables to a default value upon declaration. In these instances, the value that a variable will contain after declaration is indeterminate which can cause issues. In fact, that value could be different each time the program is ran.
* Note: This resource should not be considered a definitive or exhaustive coding guideline.
