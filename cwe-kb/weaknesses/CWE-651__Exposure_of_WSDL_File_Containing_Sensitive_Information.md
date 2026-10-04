# CWE-651: Exposure of WSDL File Containing Sensitive Information

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/651.html  

## Description
The Web services architecture may require exposing a Web Service Definition Language (WSDL) file that contains information on the publicly accessible services and how callers of these services should interact with them (e.g. what parameters they expect and what types they return).

## Extended Description
An information exposure may occur if any of the following apply: The WSDL file is accessible to a wider audience than intended. The WSDL file contains information on the methods/services that should not be publicly accessible or information about deprecated methods. This problem is made more likely due to the WSDL often being automatically generated from the code. Information in the WSDL file helps guess names/locations of methods/resources that should not be publicly accessible.

## Related Weaknesses
- ChildOf: CWE-538

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — The attacker may find sensitive information located in the WSDL file.

## Potential Mitigations
- [Architecture and Design] Limit access to the WSDL file as much as possible. If services are provided only to a limited number of entities, it may be better to provide WSDL privately to each of these entities than to publish WSDL publicly.
- [Architecture and Design] Make sure that WSDL does not describe methods that should not be publicly accessible. Make sure to protect service methods that should not be publicly accessible with access controls.
- [Architecture and Design] Do not use method names in WSDL that might help an adversary guess names of private methods/resources used by the service.

## Demonstrative Examples (summary)
- The WSDL for a service providing information on the best price of a certain item exposes the following method: float getBestPrice(String ItemID) An attacker might guess that there is a method setBestPrice (String ItemID, float Price) that is available and invoke that method to try and change the best price of a given item to their advantage. The attack may succeed if the attacker correctly guesses the name of the method, the method does not have proper access controls around it and the service itself has the functionality to update the best price of the item.
