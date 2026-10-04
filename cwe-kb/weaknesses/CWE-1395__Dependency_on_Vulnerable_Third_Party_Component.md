# CWE-1395: Dependency on Vulnerable Third-Party Component

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1395.html  

## Description
The product has a dependency on a third-party component that contains one or more known vulnerabilities.

## Extended Description
Many products are large enough or complex enough that part of their functionality uses libraries, modules, or other intellectual property developed by third parties who are not the product creator. For example, even an entire operating system might be from a third-party supplier in some hardware products. Whether open or closed source, these components may contain publicly known vulnerabilities or hidden functionality such as malware that could be exploited by adversaries to compromise the product.

## Related Weaknesses
- ChildOf: CWE-1357
- ChildOf: CWE-657

## Common Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Varies by Context — The consequences vary widely, depending on the vulnerabilities that exist in the component; how those vulnerabilities can be "reached" by adversaries, as the exploitation paths and attack surface will vary depending on how the component is used; and the criticality of the privilege levels and features for which the product relies on the component.

## Potential Mitigations
- [Requirements, Policy] In some industries such as healthcare [REF-1320] [REF-1322] or technologies such as the cloud [REF-1321], it might be unclear about who is responsible for applying patches for third-party vulnerabilities: the vendor, the operator/customer, or a separate service. Clarifying roles and responsibilities can be important to minimize confusion or unnecessary delay when third-party vulnerabilities are disclosed.
- [Requirements] Require a Bill of Materials for all components and sub-components of the product. For software, require a Software Bill of Materials (SBOM) [REF-1247] [REF-1311].
- [Architecture and Design, Implementation, Integration, Manufacturing] Maintain a Bill of Materials for all components and sub-components of the product. For software, maintain a Software Bill of Materials (SBOM). According to [REF-1247], "An SBOM is a formal, machine-readable inventory of software components and dependencies, information about those components, and their hierarchical relationships."
- [Operation, Patching and Maintenance] Actively monitor when a third-party component vendor announces vulnerability patches; fix the third-party component as soon as possible; and make it easy for operators/customers to obtain and apply the patch.
- [Operation, Patching and Maintenance] Continuously monitor changes in each of the product's components, especially when the changes indicate new vulnerabilities, end-of-life (EOL) plans, etc.

## Detection Methods
- [Automated Analysis] For software, use Software Composition Analysis (SCA) tools, which automatically analyze products to identify third-party dependencies. Often, SCA tools can be used to link with known vulnerabilities in the dependencies that they detect. There are commercial and open-source alternatives, such as OWASP Dependency-Check [REF-1312]. Many languages or frameworks have package managers with similar capabilities, such as npm audit for JavaScript, pip-audit for Python, govulncheck for Go, and many others. Dynamic methods can detect loading of third-party components.

## Demonstrative Examples (summary)
- The "SweynTooth" vulnerabilities in Bluetooth Low Energy (BLE) software development kits (SDK) were found to affect multiple Bluetooth System-on-Chip (SoC) manufacturers. These SoCs were used by many products such as medical devices, Smart Home devices, wearables, and other IoT devices. [REF-1314] [REF-1315]
- log4j, a Java-based logging framework, is used in a large number of products, with estimates in the range of 3 billion affected devices [REF-1317]. When the "log4shell" (CVE-2021-44228) vulnerability was initially announced, it was actively exploited for remote code execution, requiring urgent mitigation in many organizations. However, it was unclear how many products were affected, as Log4j would sometimes be part of a long sequence of transitive dependencies. [REF-1316]
