# CWE-1339: Insufficient Precision or Accuracy of a Real Number

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1339.html  

## Description
The product processes a real number with an implementation in which the number's representation does not preserve required accuracy and precision in its fractional part, causing an incorrect result.

## Extended Description
When a security decision or calculation requires highly precise, accurate numbers such as financial calculations or prices, then small variations in the number could be exploited by an attacker. There are multiple ways to store the fractional part of a real number in a computer. In all of these cases, there is a limit to the accuracy of recording a fraction. If the fraction can be represented in a fixed number of digits (binary or decimal), there might not be enough digits assigned to represent the number. In other cases the number cannot be represented in a fixed number of digits due to repeating in decimal or binary notation (e.g. 0.333333...) or due to a transcendental number such as Π or √2. Rounding of numbers can lead to situations where the computer results do not adequately match the result of sufficiently accurate math.

## Related Weaknesses
- ChildOf: CWE-682
- PeerOf: CWE-190
- CanPrecede: CWE-834
- CanPrecede: CWE-119

## Common Consequences
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart — This weakness will generally lead to undefined results and therefore crashes. In some implementations the program will halt if the weakness causes an overflow during a calculation.
- Scope: Integrity; Impact: Execute Unauthorized Code or Commands — The results of the math are not as expected. This could cause issues where a value would not be properly calculated and provide an incorrect answer.
- Scope: Confidentiality, Availability, Access Control; Impact: Read Application Data, Modify Application Data — This weakness can sometimes trigger buffer overflows which can be used to execute arbitrary code. This is usually outside the scope of a product's implicit security policy.

## Potential Mitigations
- [Implementation, Patching and Maintenance] The developer or maintainer can move to a more accurate representation of real numbers. In extreme cases, the programmer can move to representations such as ratios of BigInts which can represent real numbers to extremely fine precision. The programmer can also use the concept of an Unum real. The memory and CPU tradeoffs of this change must be examined. Since floating point reals are used in many products and many locations, they are implemented in hardware and most format changes will cause the calculations to be moved into software resulting in slower products.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- Muller's Recurrence is a series that is supposed to converge to the number 5. When running this series with the following code, different implementations of real numbers fail at specific iterations:
- On February 25, 1991, during the eve of the Iraqi invasion of Saudi Arabia, a Scud missile fired from Iraqi positions hit a US Army barracks in Dhahran, Saudi Arabia. It miscalculated time and killed 28 people [REF-1190].
- Sleipner A, an offshore drilling platform in the North Sea, was incorrectly constructed with an underestimate of 50% of strength in a critical cluster of buoyancy cells needed for construction. This led to a leak in buoyancy cells during lowering, causing a seismic event of 3.0 on the Richter Scale and about $700M loss [REF-1281].
