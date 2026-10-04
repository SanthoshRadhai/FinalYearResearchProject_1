# CWE-1434: Insecure Setting of Generative AI/ML Model Inference Parameters

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1434.html  

## Description
The product has a component that relies on a generative AI/ML model configured with inference parameters that produce an unacceptably high rate of erroneous or unexpected outputs.

## Extended Description
Generative AI/ML models, such as those used for text generation, image synthesis, and other creative tasks, rely on inference parameters that control model behavior, such as temperature, Top P, and Top K. These parameters affect the model's internal decision-making processes, learning rate, and probability distributions. Incorrect settings can lead to unusual behavior such as text "hallucinations," unrealistic images, or failure to converge during training. The impact of such misconfigurations can compromise the integrity of the application. If the results are used in security-critical operations or decisions, then this could violate the intended security policy, i.e., introduce a vulnerability.

## Related Weaknesses
- ChildOf: CWE-440
- ChildOf: CWE-665
- CanPrecede: CWE-684
- PeerOf: CWE-691

## Common Consequences
- Scope: Integrity, Other; Impact: Varies by Context, Unexpected State — The product can generate inaccurate, misleading, or nonsensical information.
- Scope: Other; Impact: Alter Execution Logic, Unexpected State, Varies by Context — If outputs are used in critical decision-making processes, errors could be propagated to other systems or components.

## Potential Mitigations
- [Implementation, System Configuration, Operation] Develop and adhere to robust parameter tuning processes that include extensive testing and validation.
- [Implementation, System Configuration, Operation] Implement feedback mechanisms to continuously assess and adjust model performance.
- [Documentation] Provide comprehensive documentation and guidelines for parameter settings to ensure consistent and accurate model behavior.

## Detection Methods
- [Automated Dynamic Analysis] Manipulate inference parameters and perform comparative evaluation to assess the impact of selected values. Build a suite of systems using targeted tools that detect problems such as prompt injection (CWE-1427) and other problems. Consider statistically measuring token distribution to see if it is consistent with expected results.
- [Manual Dynamic Analysis] Manipulate inference parameters and perform comparative evaluation to assess the impact of selected values. Build a suite of systems using targeted tools that detect problems such as prompt injection (CWE-1427) and other problems. Consider statistically measuring token distribution to see if it is consistent with expected results.

## Demonstrative Examples (summary)
- Assume the product offers an LLM-based AI coding assistant to help users to write code as part of an Integrated Development Environment (IDE). Assume the model has been trained on real-world code, and the model behaves normally under its default settings. Suppose there is a default temperature of 1, with a range of temperature values from 0 (most deterministic) to 2. Consider the following configuration.
