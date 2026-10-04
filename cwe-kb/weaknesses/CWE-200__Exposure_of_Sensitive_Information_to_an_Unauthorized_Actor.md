# CWE-200: Exposure of Sensitive Information to an Unauthorized Actor

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/200.html  

## Description
The product exposes sensitive information to an actor that is not explicitly authorized to have access to that information.

## Extended Description
There are many different kinds of mistakes that introduce information exposures. The severity of the error can range widely, depending on the context in which the product operates, the type of sensitive information that is revealed, and the benefits it may provide to an attacker. Some kinds of sensitive information include: private, personal information, such as personal messages, financial data, health records, geographic location, or contact details system status and environment, such as the operating system and installed packages business secrets and intellectual property network status and configuration the product's own code or internal state metadata, e.g. logging of connections or message headers indirect information, such as a discrepancy between two internal operations that can be observed by an outsider Information might be sensitive to different parties, each of which may have their own expectations for whether the information should be protected. These parties include: the product's own users people or organizations whose information is created or used by the product, even if they are not direct product users the product's administrators, including the admins of the system(s) and/or networks on which the product operates the developer Information exposures can occur in different ways: the code explicitly inserts sensitive information into resources or messages that are intentionally made accessible to unauthorized actors, but should not contain the information - i.e., the information should have been "scrubbed" or "sanitized" a different weakness or mistake indirectly inserts the sensitive information into resources, such as a web script error revealing the full system path of the program. the code manages resources that intentionally contain sensitive information, but the resources are unintentionally made accessible to unauthorized actors. In this case, the information exposure is resultant - i.e., a different weakness enabled the access to the information in the first place. It is common practice to describe any loss of confidentiality as an "information exposure," but this can lead to overuse of CWE-200 in CWE mapping. From the CWE perspective, loss of confidentiality is a technical impact that can arise from dozens of different weaknesses, such as insecure file permissions or out-of-bounds read. CWE-200 and its lower-level descendants are intended to cover the mistakes that occur in behaviors that explicitly manage, store, transfer, or cleanse sensitive information.

## Related Weaknesses
- ChildOf: CWE-668

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data

## Potential Mitigations
- [Architecture and Design] Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.

## Detection Methods
- [Automated Static Analysis - Binary or Bytecode] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Bytecode Weakness Analysis - including disassembler + source code weakness analysis Inter-application Flow Analysis
- [Dynamic Analysis with Automated Results Interpretation] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Web Application Scanner Web Services Scanner Database Scanners
- [Dynamic Analysis with Manual Results Interpretation] According to SOAR [REF-1479], the following detection techniques may be useful: Cost effective for partial coverage: Fuzz Tester Framework-based Fuzzer Automated Monitored Execution Monitored Virtual Environment - run potentially malicious code in sandbox / wrapper / virtual machine, see if it does anything suspicious
- [Manual Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Manual Source Code Review (not inspections)
- [Automated Static Analysis - Source Code] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Context-configured Source Code Weakness Analyzer Cost effective for partial coverage: Source code Weakness Analyzer
- [Architecture or Design Review] According to SOAR [REF-1479], the following detection techniques may be useful: Highly cost effective: Formal Methods / Correct-By-Construction Cost effective for partial coverage: Attack Modeling Inspection (IEEE 1028 standard) (can apply to requirements, design, source code, etc.)

## Demonstrative Examples (summary)
- The following code checks validity of the supplied username and password and notifies the user of a successful or failed login.
- This code tries to open a database connection, and prints any exceptions that occur.
- In the example below, the method getUserBankAccount retrieves a bank account object from a database using the supplied username and account number to query the database. If an SQLException is raised when querying the database, an error message is created and output to a log file.
- This code stores location information about the current user:
- The following is an actual MySQL error statement:
- This code displays some information on a web page.
- The following program changes its behavior based on a debug flag.
- This code uses location to determine the user's current US State location.
