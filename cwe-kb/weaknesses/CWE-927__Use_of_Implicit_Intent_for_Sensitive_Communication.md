# CWE-927: Use of Implicit Intent for Sensitive Communication

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/927.html  

## Description
The Android application uses an implicit intent for transmitting sensitive data to other applications.

## Extended Description
Since an implicit intent does not specify a particular application to receive the data, any application can process the intent by using an Intent Filter for that intent. This can allow untrusted applications to obtain sensitive data. There are two variations on the standard broadcast intent, ordered and sticky. Ordered broadcast intents are delivered to a series of registered receivers in order of priority as declared by the Receivers. A malicious receiver can give itself a high priority and cause a denial of service by stopping the broadcast from propagating further down the chain. There is also the possibility of malicious data modification, as a receiver may also alter the data within the Intent before passing it on to the next receiver. The downstream components have no way of asserting that the data has not been altered earlier in the chain. Sticky broadcast intents remain accessible after the initial broadcast. An old sticky intent will be broadcast again to any new receivers that register for it in the future, greatly increasing the chances of information exposure over time. Also, sticky broadcasts cannot be protected by permissions that may apply to other kinds of intents. In addition, any broadcast intent may include a URI that references data that the receiving component does not normally have the privileges to access. The sender of the intent can include special privileges that grant the receiver read or write access to the specific URI included in the intent. A malicious receiver that intercepts this intent will also gain those privileges and be able to read or write the resource at the specified URI.

## Related Weaknesses
- ChildOf: CWE-285
- ChildOf: CWE-668

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — Other applications, possibly untrusted, can read the data that is offered through the Intent.
- Scope: Integrity; Impact: Varies by Context — The application may handle responses from untrusted applications on the device, which could cause it to perform unexpected or unauthorized actions.

## Potential Mitigations
- [Implementation] If the application only requires communication with its own components, then the destination is always known, and an explicit intent could be used.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This application wants to create a user account in several trusted applications using one broadcast intent:
- This application interfaces with a web service that requires a separate user login. It creates a sticky intent, so that future trusted applications that also use the web service will know who the current user is:
- This application is sending an ordered broadcast, asking other applications to open a URL:
- This application sends a special intent with a flag that allows the receiving application to read a data file for backup purposes.
