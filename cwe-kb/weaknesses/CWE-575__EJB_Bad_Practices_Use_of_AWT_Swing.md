# CWE-575: EJB Bad Practices: Use of AWT Swing

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/575.html  

## Description
The product violates the Enterprise JavaBeans (EJB) specification by using AWT/Swing.

## Extended Description
The Enterprise JavaBeans specification requires that every bean provider follow a set of programming guidelines designed to ensure that the bean will be portable and behave consistently in any EJB container. In this case, the product violates the following EJB guideline: "An enterprise bean must not use the AWT functionality to attempt to output information to a display, or to input information from a keyboard." The specification justifies this requirement in the following way: "Most servers do not allow direct interaction between an application program and a keyboard/display attached to the server system."

## Related Weaknesses
- ChildOf: CWE-695

## Common Consequences
- Scope: Other; Impact: Quality Degradation

## Potential Mitigations
- [Architecture and Design] Do not use AWT/Swing when writing EJBs.

## Demonstrative Examples (summary)
- The following Java example is a simple converter class for converting US dollars to Yen. This converter class demonstrates the improper practice of using a stateless session Enterprise JavaBean that implements an AWT Component and AWT keyboard event listener to retrieve keyboard input from the user for the amount of the US dollars to convert to Yen.
