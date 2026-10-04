# CWE-576: EJB Bad Practices: Use of Java I/O

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/576.html  

## Description
The product violates the Enterprise JavaBeans (EJB) specification by using the java.io package.

## Extended Description
The Enterprise JavaBeans specification requires that every bean provider follow a set of programming guidelines designed to ensure that the bean will be portable and behave consistently in any EJB container. In this case, the product violates the following EJB guideline: "An enterprise bean must not use the java.io package to attempt to access files and directories in the file system." The specification justifies this requirement in the following way: "The file system APIs are not well-suited for business components to access data. Business components should use a resource manager API, such as JDBC, to store data."

## Related Weaknesses
- ChildOf: CWE-695

## Common Consequences
- Scope: Other; Impact: Quality Degradation

## Potential Mitigations
- [Implementation] Do not use Java I/O when writing EJBs.

## Demonstrative Examples (summary)
- The following Java example is a simple stateless Enterprise JavaBean that retrieves the interest rate for the number of points for a mortgage. In this example, the interest rates for various points are retrieved from an XML document on the local file system, and the EJB uses the Java I/O API to retrieve the XML document from the local file system.
