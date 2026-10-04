# CWE-1284: Improper Validation of Specified Quantity in Input

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1284.html  

## Description
The product receives input that is expected to specify a quantity (such as size or length), but it does not validate or incorrectly validates that the quantity has the required properties.

## Extended Description
Specified quantities include size, length, frequency, price, rate, number of operations, time, and others. Code may rely on specified quantities to allocate resources, perform calculations, control iteration, etc.

## Related Weaknesses
- ChildOf: CWE-20
- ChildOf: CWE-20
- CanPrecede: CWE-789

## Common Consequences
- Scope: Other, Integrity, Availability; Impact: Varies by Context, DoS: Resource Consumption (CPU), Modify Memory, Read Memory — When the quantity is not properly validated, then attackers can specify malicious quantities to cause excessive resource allocation, trigger unexpected failures, enable buffer overflows, etc.

## Potential Mitigations
- [Implementation] Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This example demonstrates a shopping interaction in which the user is free to specify the quantity of items to be purchased and a total is calculated.
- This example asks the user for a height and width of an m X n game board with a maximum dimension of 100 squares.
- The following code is a workflow job written using YAML. The code attempts to download pull request artifacts, unzip from the artifact called pr.zip and extract the value of the file NR into a variable "pr_number" that will be used later in another job. It attempts to create a github workflow environment variable, writing to $GITHUB_ENV. The environment variable value is retrieved from an external resource.
- The following PHP code could be from a shopping cart application. It allows users to apply a discount to an item.
