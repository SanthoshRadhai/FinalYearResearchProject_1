# CAPEC-138: Reflection Injection

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/138.html  

## Description
An adversary supplies a value to the target application which is then used by reflection methods to identify a class, method, or field. For example, in the Java programming language the reflection libraries permit an application to inspect, load, and invoke classes and their components by name. If an adversary can control the input into these methods including the name of the class/method/field or the parameters passed to methods, they can cause the targeted application to invoke incorrect methods, read random fields, or even to load and utilize malicious classes that the adversary created. This can lead to the application revealing sensitive information, returning incorrect results, or even having the adversary take control of the targeted application.

## Related Attack Patterns
- ChildOf: CAPEC-137

## Prerequisites
- The target application must utilize reflection libraries and allow users to directly control the parameters to these methods. If the adversary can host classes where the target can invoke them, more powerful variants of this attack are possible.
- The target application must accept a string as user input, fail to sanitize characters that have a special meaning in the parameter encoding, and insert the user-supplied string in an encoding which is then processed.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Related Weaknesses (CWE)
- CWE-470
