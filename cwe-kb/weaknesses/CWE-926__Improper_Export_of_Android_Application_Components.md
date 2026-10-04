# CWE-926: Improper Export of Android Application Components

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/926.html  

## Description
The Android application exports a component for use by other applications, but does not properly restrict which applications can launch the component or access the data it contains.

## Extended Description
The attacks and consequences of improperly exporting a component may depend on the exported component: If access to an exported Activity is not restricted, any application will be able to launch the activity. This may allow a malicious application to gain access to sensitive information, modify the internal state of the application, or trick a user into interacting with the victim application while believing they are still interacting with the malicious application. If access to an exported Service is not restricted, any application may start and bind to the Service. Depending on the exposed functionality, this may allow a malicious application to perform unauthorized actions, gain access to sensitive information, or corrupt the internal state of the application. If access to a Content Provider is not restricted to only the expected applications, then malicious applications might be able to access the sensitive data. Note that in Android before 4.2, the Content Provider is automatically exported unless it has been explicitly declared as NOT exported.

## Related Weaknesses
- ChildOf: CWE-285

## Common Consequences
- Scope: Availability, Integrity; Impact: Unexpected State, DoS: Crash, Exit, or Restart, DoS: Instability, Varies by Context — Other applications, possibly untrusted, can launch the Activity.
- Scope: Availability, Integrity; Impact: Unexpected State, Gain Privileges or Assume Identity, DoS: Crash, Exit, or Restart, DoS: Instability, Varies by Context — Other applications, possibly untrusted, can bind to the Service.
- Scope: Confidentiality, Integrity; Impact: Read Application Data, Modify Application Data — Other applications, possibly untrusted, can read or modify the data that is offered by the Content Provider.

## Potential Mitigations
- [Build and Compilation] If they do not need to be shared by other applications, explicitly mark components with android:exported="false" in the application manifest.
- [Build and Compilation] If you only intend to use exported components between related apps under your control, use android:protectionLevel="signature" in the xml manifest to restrict access to applications signed by you.
- [Build and Compilation, Architecture and Design] Limit Content Provider permissions (read/write) as appropriate.
- [Build and Compilation, Architecture and Design] Limit Content Provider permissions (read/write) as appropriate.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This application is exporting an activity and a service in its manifest.xml:
- This application has created a content provider to enable custom search suggestions within the application:
