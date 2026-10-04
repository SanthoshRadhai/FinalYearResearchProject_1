# CWE-1269: Product Released in Non-Release Configuration

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1269.html  

## Description
The product released to market is released in pre-production or manufacturing configuration.

## Extended Description
Products in the pre-production or manufacturing stages are configured to have many debug hooks and debug capabilities, including but not limited to: Ability to override/bypass various cryptographic checks (including authentication, authorization, and integrity) Ability to read/write/modify/dump internal state (including registers and memory) Ability to change system configurations Ability to run hidden or private commands that are not allowed during production (as they expose IP). The above is by no means an exhaustive list, but it alludes to the greater capability and the greater state of vulnerability of a product during it's preproduction or manufacturing state. Complexity increases when multiple parties are involved in executing the tests before the final production version. For example, a chipmaker might fabricate a chip and run its own preproduction tests, following which the chip would be delivered to the Original Equipment Manufacturer (OEM), who would now run a second set of different preproduction tests on the same chip. Only after both of these sets of activities are complete, can the overall manufacturing phase be called "complete" and have the "Manufacturing Complete" fuse blown. However, if the OEM forgets to blow the Manufacturing Complete fuse, then the system remains in the manufacturing stage, rendering the system both exposed and vulnerable.

## Related Weaknesses
- ChildOf: CWE-693

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Access Control, Accountability, Authentication, Authorization, Non-Repudiation; Impact: Other

## Potential Mitigations
- [Implementation] Ensure that there exists a marker for denoting the Manufacturing Complete stage and that the Manufacturing Complete marker gets updated at the Manufacturing Complete stage (i.e., the Manufacturing Complete fuse gets blown).
- [Integration] Ensure that there exists a marker for denoting the Manufacturing Complete stage and that the Manufacturing Complete marker gets updated at the Manufacturing Complete stage (i.e., the Manufacturing Complete fuse gets blown).
- [Manufacturing] Ensure that there exists a marker for denoting the Manufacturing Complete stage and that the Manufacturing Complete marker gets updated at the Manufacturing Complete stage (i.e., the Manufacturing Complete fuse gets blown).

## Demonstrative Examples (summary)
- This example shows what happens when a preproduction system is made available for production.
