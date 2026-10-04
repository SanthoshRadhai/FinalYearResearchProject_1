# CWE-356: Product UI does not Warn User of Unsafe Actions

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/356.html  

## Description
The product's user interface does not warn the user before undertaking an unsafe action on behalf of that user. This makes it easier for attackers to trick users into inflicting damage to their system.

## Extended Description
Product systems should warn users that a potentially dangerous action may occur if the user proceeds. For example, if the user downloads a file from an unknown source and attempts to execute the file on their machine, then the application's GUI can indicate that the file is unsafe.

## Related Weaknesses
- ChildOf: CWE-221

## Common Consequences
- Scope: Non-Repudiation; Impact: Hide Activities
