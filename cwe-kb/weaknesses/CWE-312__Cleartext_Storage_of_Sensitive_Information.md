# CWE-312: Cleartext Storage of Sensitive Information

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/312.html  

## Description
The product stores sensitive information in cleartext within a resource that might be accessible to another control sphere.

## Related Weaknesses
- ChildOf: CWE-311
- ChildOf: CWE-311
- ChildOf: CWE-922

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — An attacker with access to the system could read sensitive information stored in cleartext (i.e., unencrypted). Even if the information is encoded in a way that is not human-readable, certain techniques could determine which encoding is being used, then decode the information.

## Potential Mitigations
- [Implementation, System Configuration, Operation] When storing data in the cloud (e.g., S3 buckets, Azure blobs, Google Cloud Storage, etc.), use the provider's controls to encrypt the data at rest. [REF-1297] [REF-1299] [REF-1301]
- [Implementation, System Configuration, Operation] In some systems/environments such as cloud, the use of "double encryption" (at both the software and hardware layer) might be required, and the developer might be solely responsible for both layers, instead of shared responsibility with the administrator of the broader system/environment.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code excerpt stores a plaintext user account ID in a browser cookie.
- This code writes a user's login information to a cookie so the user does not have to login again later.
- The following code attempts to establish a connection, read in a password, then store it to a buffer.
- The following examples show a portion of properties and configuration files for Java and ASP.NET applications. The files include username and password information but they are stored in cleartext.
- In 2022, the OT:ICEFALL study examined products by 10 different Operational Technology (OT) vendors. The researchers reported 56 vulnerabilities and said that the products were "insecure by design" [REF-1283]. If exploited, these vulnerabilities often allowed adversaries to change how the products operated, ranging from denial of service to changing the code that the products executed. Since these products were often used in industries such as power, electrical, water, and others, there could even be safety implications.
- In 2021, a web site operated by PeopleGIS stored data of US municipalities in Amazon Web Service (AWS) Simple Storage Service (S3) buckets.
- Consider the following PowerShell command examples for encryption scopes of Azure storage objects. In the first example, an encryption scope is set for the storage account.
