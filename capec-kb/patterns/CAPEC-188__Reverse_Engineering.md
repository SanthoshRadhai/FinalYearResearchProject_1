# CAPEC-188: Reverse Engineering

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/188.html  

## Description
An adversary discovers the structure, function, and composition of an object, resource, or system by using a variety of analysis techniques to effectively determine how the analyzed entity was constructed or operates. The goal of reverse engineering is often to duplicate the function, or a part of the function, of an object in order to duplicate or "back engineer" some aspect of its functioning. Reverse engineering techniques can be applied to mechanical objects, electronic devices, or software, although the methodology and techniques involved in each type of analysis differ widely.

## Prerequisites
- Access to targeted system, resources, and information.

## Skills Required
- [High] Understanding of low level programming languages or technologies can be very helpful. For example, when reverse engineering a binary file, an understanding of assembly languages can help to determine the purpose and inner-workings of the code. Another example is reverse engineering an application that relies on networking. Here, an understanding networking protocols can provide insight into application details.

## Resources Required
- The technical resources necessary to engage in reverse engineering differ in accordance with the type of object, resource, or system being analyzed.

## Mitigations
- Employ code obfuscation techniques to prevent the adversary from reverse engineering the targeted entity.

## Related Weaknesses (CWE)
- CWE-1278
