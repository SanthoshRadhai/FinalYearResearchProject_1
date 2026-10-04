# CWE-577: EJB Bad Practices: Use of Sockets

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/577.html  

## Description
The product violates the Enterprise JavaBeans (EJB) specification by using sockets.

## Extended Description
The Enterprise JavaBeans specification requires that every bean provider follow a set of programming guidelines designed to ensure that the bean will be portable and behave consistently in any EJB container. In this case, the product violates the following EJB guideline: "An enterprise bean must not attempt to listen on a socket, accept connections on a socket, or use a socket for multicast." The specification justifies this requirement in the following way: "The EJB architecture allows an enterprise bean instance to be a network socket client, but it does not allow it to be a network server. Allowing the instance to become a network server would conflict with the basic function of the enterprise bean-- to serve the EJB clients."

## Related Weaknesses
- ChildOf: CWE-573

## Common Consequences
- Scope: Other; Impact: Quality Degradation

## Potential Mitigations
- [Architecture and Design, Implementation] Do not use Sockets when writing EJBs.

## Demonstrative Examples (summary)
- The following Java example is a simple stateless Enterprise JavaBean that retrieves stock symbols and stock values. The Enterprise JavaBean creates a socket and listens for and accepts connections from clients on the socket.
