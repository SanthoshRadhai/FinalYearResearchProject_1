# CAPEC-229: Serialized Data Parameter Blowup

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/229.html  

## Description
This attack exploits certain serialized data parsers (e.g., XML, YAML, etc.) which manage data in an inefficient manner. The attacker crafts an serialized data file with multiple configuration parameters in the same dataset. In a vulnerable parser, this results in a denial of service condition where CPU resources are exhausted because of the parsing algorithm. The weakness being exploited is tied to parser implementation and not language specific.

## Related Attack Patterns
- ChildOf: CAPEC-231

## Prerequisites
- The server accepts input in the form of serialized data and is using a parser with a runtime longer than O(n) for the insertion of a new configuration parameter in the data container.(examples are .NET framework 1.0 and 1.1)

## Mitigations
- This attack may be mitigated completely by using a parser that is not using a vulnerable container.
- Mitigation may limit the number of configuration parameters per dataset.

## Related Weaknesses (CWE)
- CWE-770
