# D3-IRV: Integer Range Validation

**Reference:** https://d3fend.mitre.org/technique/D3-IRV/  

## Definition
Ensuring that an integer is within a valid range.

## Parent Class(es)
- Source Code Hardening

## Relationships
- **hardens:** Mathematical Function
- **kb-reference:** Reference - Integer Range Validation

## Knowledge Base Article
## How it Works
Integer Range Validation can be done by programmatically checking the value of an integer before or after an operation to determine if the resulting value will be valid.
Checking the value of an integer to ensure it is in a valid range helps prevent integer overflow, wraparound, and logical errors.

## Considerations
* A valid range can be defined by language, data-type, or logical constraints.
* Take extra care when doing operations on integers that will result in a value close to the bounds of a valid range.
* Note: This resource should not be considered a definitive or exhaustive coding guideline.
