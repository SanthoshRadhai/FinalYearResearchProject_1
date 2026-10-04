# CWE-578: EJB Bad Practices: Use of Class Loader

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/578.html  

## Description
The product violates the Enterprise JavaBeans (EJB) specification by using the class loader.

## Extended Description
The Enterprise JavaBeans specification requires that every bean provider follow a set of programming guidelines designed to ensure that the bean will be portable and behave consistently in any EJB container. In this case, the product violates the following EJB guideline: "The enterprise bean must not attempt to create a class loader; obtain the current class loader; set the context class loader; set security manager; create a new security manager; stop the JVM; or change the input, output, and error streams." The specification justifies this requirement in the following way: "These functions are reserved for the EJB container. Allowing the enterprise bean to use these functions could compromise security and decrease the container's ability to properly manage the runtime environment."

## Related Weaknesses
- ChildOf: CWE-573

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Other; Impact: Execute Unauthorized Code or Commands, Varies by Context

## Potential Mitigations
- [Architecture and Design, Implementation] Do not use the Class Loader when writing EJBs.

## Demonstrative Examples (summary)
- The following Java example is a simple stateless Enterprise JavaBean that retrieves the interest rate for the number of points for a mortgage. The interest rates for various points are retrieved from an XML document on the local file system, and the EJB uses the Class Loader for the EJB class to obtain the XML document from the local file system as an input stream.
- An EJB is also restricted from creating a custom class loader and creating a class and instance of a class from the class loader, as shown in the following example.
