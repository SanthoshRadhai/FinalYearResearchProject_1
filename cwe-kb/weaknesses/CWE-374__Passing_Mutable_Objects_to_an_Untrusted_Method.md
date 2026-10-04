# CWE-374: Passing Mutable Objects to an Untrusted Method

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/374.html  

## Description
The product sends non-cloned mutable data as an argument to a method or function.

## Extended Description
The function or method that has been called can alter or delete the mutable data. This could violate assumptions that the calling function has made about its state. In situations where unknown code is called with references to mutable data, this external code could make changes to the data sent. If this data was not previously cloned, the modified data might not be valid in the context of execution.

## Related Weaknesses
- ChildOf: CWE-668

## Common Consequences
- Scope: Integrity; Impact: Modify Memory — Potentially data could be tampered with by another function which should not have been tampered with.

## Potential Mitigations
- [Implementation] Pass in data which should not be altered as constant or immutable.
- [Implementation] Clone all mutable data before passing it into an external function . This is the preferred mitigation. This way, regardless of what changes are made to the data, a valid copy is retained for use by the class.

## Demonstrative Examples (summary)
- The following example demonstrates the weakness.
- In the following Java example, the BookStore class manages the sale of books in a bookstore, this class includes the member objects for the bookstore inventory and sales database manager classes. The BookStore class includes a method for updating the sales database and inventory when a book is sold. This method retrieves a Book object from the bookstore inventory object using the supplied ISBN number for the book class, then calls a method for the sales object to update the sales information and then calls a method for the inventory object to update inventory for the BookStore.
