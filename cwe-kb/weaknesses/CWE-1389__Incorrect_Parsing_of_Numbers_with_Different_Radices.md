# CWE-1389: Incorrect Parsing of Numbers with Different Radices

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1389.html  

## Description
The product parses numeric input assuming base 10 (decimal) values, but it does not account for inputs that use a different base number (radix).

## Extended Description
Frequently, a numeric input that begins with "0" is treated as octal, or "0x" causes it to be treated as hexadecimal, e.g. by the inet_addr() function. For example, "023" (octal) is 35 decimal, or "0x31" is 49 decimal. Other bases may be used as well. If the developer assumes decimal-only inputs, the code could produce incorrect numbers when the inputs are parsed using a different base. This can result in unexpected and/or dangerous behavior. For example, a "0127.0.0.1" IP address is parsed as octal due to the leading "0", whose numeric value would be the same as 87.0.0.1 (decimal), where the developer likely expected to use 127.0.0.1. The consequences vary depending on the surrounding code in which this weakness occurs, but they can include bypassing network-based access control using unexpected IP addresses or netmasks, or causing apparently-symbolic identifiers to be processed as if they are numbers. In web applications, this can enable bypassing of SSRF restrictions.

## Related Weaknesses
- ChildOf: CWE-704

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — An attacker may use an unexpected numerical base to access private application resources.
- Scope: Integrity; Impact: Bypass Protection Mechanism, Alter Execution Logic — An attacker may use an unexpected numerical base to bypass or manipulate access control mechanisms.

## Potential Mitigations
- [Implementation] If only decimal-based values are expected in the application, conditional checks should be created in a way that prevent octal or hexadecimal strings from being checked. This can be achieved by converting any numerical string to an explicit base-10 integer prior to the conditional check, to prevent octal or hex values from ever being checked against the condition.
- [Implementation] If various numerical bases do need to be supported, check for leading values indicating the non-decimal base you wish to support (such as 0x for hex) and convert the numeric strings to integers of the respective base. Reject any other alternative-base string that is not intentionally supported by the application.
- [Implementation] If regular expressions are used to validate IP addresses, ensure that they are bounded using ^ and $ to prevent base-prepended IP addresses from being matched.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The below demonstrative example uses an IP validator that splits up an IP address by octet, tests to ensure each octet can be casted into an integer, and then returns the original IP address if no exceptions are raised. This validated IP address is then tested using the "ping" command.
- This code uses a regular expression to validate an IP string prior to using it in a call to the "ping" command.
- Consider the following scenario, inspired by CWE team member Kelly Todd. Kelly wants to set up monitoring systems for his two cats, who pose very different threats. One cat, Night, tweets embarrassing or critical comments about his owner in ways that could cause reputational damage, so Night's blog needs to be monitored regularly. The other cat, Taki, likes to distract Kelly and his coworkers during business meetings with cute meows, so Kelly monitors Taki's location using a different web site. Suppose /etc/hosts provides the site info as follows:
