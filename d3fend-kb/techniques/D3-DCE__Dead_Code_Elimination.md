# D3-DCE: Dead Code Elimination

**Reference:** https://d3fend.mitre.org/technique/D3-DCE/  

## Definition
Removing unreachable or "dead code" from compiled source code.

## Parent Class(es)
- Application Hardening

## Relationships
- **kb-reference:** Reference - Dead code elimination

## Knowledge Base Article
## How it works

Dead code is code that is considered unreachable by normal program execution. Dead code can be created by adding code under a condition that never evaluates to true. Dead code should be removed since this type of code can produce unexpected results, if accidentally or maliciously forced to execute.

Dead code identification is typically performed by algorithms that implement program flows analysis looking for unreachable code. The dead code is eliminated by instructing compilers to remove the code through compiler flags, i.e., '-fdce' is used for Dead Code Elimination.

## Considerations

Code can also be deemed unreachable for certain run-time conditions. Different deployed systems and environments may contain some code that is unreachable for the given environment. This technique does not consider run-time conditions for unreachable code.
