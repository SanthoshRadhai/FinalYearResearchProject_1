# CWE-1426: Improper Validation of Generative AI Output

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1426.html  

## Description
The product invokes a generative AI/ML component whose behaviors and outputs cannot be directly controlled, but the product does not validate or insufficiently validates the outputs to ensure that they align with the intended security, content, or privacy policy.

## Related Weaknesses
- ChildOf: CWE-707

## Common Consequences
- Scope: Integrity; Impact: Execute Unauthorized Code or Commands, Varies by Context — In an agent-oriented setting, output could be used to cause unpredictable agent invocation, i.e., to control or influence agents that might be invoked from the output. The impact varies depending on the access that is granted to the tools, such as creating a database or writing files.

## Potential Mitigations
- [Architecture and Design] Since the output from a generative AI component (such as an LLM) cannot be trusted, ensure that it operates in an untrusted or non-privileged space.
- [Operation] Use "semantic comparators," which are mechanisms that provide semantic comparison to identify objects that might appear different but are semantically similar.
- [Operation] Use components that operate externally to the system to monitor the output and act as a moderator. These components are called different terms, such as supervisors or guardrails.
- [Build and Compilation] During model training, use an appropriate variety of good and bad examples to guide preferred outputs.

## Detection Methods
- [Dynamic Analysis with Manual Results Interpretation] Use known techniques for prompt injection and other attacks, and adjust the attacks to be more specific to the model or system.
- [Dynamic Analysis with Automated Results Interpretation] Use known techniques for prompt injection and other attacks, and adjust the attacks to be more specific to the model or system.
- [Architecture or Design Review] Review of the product design can be effective, but it works best in conjunction with dynamic analysis.
