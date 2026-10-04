# D3-MBSV: Memory Block Start Validation

**Reference:** https://d3fend.mitre.org/technique/D3-MBSV/  

## Definition
Ensuring that a pointer accurately references the beginning of a designated memory block.

## Parent Class(es)
- Pointer Validation

## Relationships
- **hardens:** Memory Free Function
- **kb-reference:** Reference - Memory Block Start Validation - GNU C Manual

## Knowledge Base Article
## How it Works
Ensure that a pointer is referencing the beginning of the intended block before using.

## Considerations
Be careful with pointer arithmetic.
