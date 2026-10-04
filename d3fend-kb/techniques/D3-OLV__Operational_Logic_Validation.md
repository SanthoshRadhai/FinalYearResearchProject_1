# D3-OLV: Operational Logic Validation

**Reference:** https://d3fend.mitre.org/technique/D3-OLV/  

## Definition
Validation of variable state in the context of the control logic of the operational application.

## Parent Class(es)
- Domain Logic Validation

## Relationships
- **kb-reference:** Reference - Secure PLC Coding Practices: Top 20 List
- **validates:** OT Control Function

## Knowledge Base Article
## How it works
Validates the type, value, and/or range of a variable taking into account the local operational logic and operational state.

For example, if a controller has a restricted range when in a specified state, this may crosscheck the value against the state in addition to a more general range validation.
