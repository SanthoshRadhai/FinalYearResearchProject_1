# D3-SBV: Service Binary Verification

**Reference:** https://d3fend.mitre.org/technique/D3-SBV/  

## Definition
Analyzing changes in service binary files by comparing to a source of truth.

## Parent Class(es)
- System File Analysis

## Relationships
- **kb-reference:** Reference - CAR-2014-02-001: Service Binary Modifications - MITRE
- **verifies:** Service Application

## Knowledge Base Article
## How it works
System service applications may originate from the operating system installation or third-party applications installed with administrative privileges. These services have an entry point of some executable file-- a binary or a script. Attackers sometimes modify these executables to launch their own code. Analyzing changes in these files may uncover unauthorized activity.

## Considerations
* These files change for legitimate reasons when the system or software updates.
* The source of truth must not be corrupted in order for this method to work.
