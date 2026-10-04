# MITRE CAPEC (Common Attack Pattern Enumeration and Classification)


---

# CAPEC-1: Accessing Functionality Not Properly Constrained by ACLs

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/1.html  

## Description
In applications, particularly web applications, access to functionality is mitigated by an authorization framework. This framework maps Access Control Lists (ACLs) to elements of the application's functionality; particularly URL's for web apps. In the case that the administrator failed to specify an ACL for a particular element, an attacker may be able to access it with impunity. An attacker with the ability to access functionality not properly constrained by ACLs can obtain sensitive information and possibly compromise the entire application. Such an attacker can access resources that must be available only to users at a higher privilege level, can access management sections of the application, or can run queries for data that they otherwise not supposed to.

## Related Attack Patterns
- ChildOf: CAPEC-122
- CanPrecede: CAPEC-17

## Prerequisites
- The application must be navigable in a manner that associates elements (subsections) of the application with ACLs.
- The various resources, or individual URLs, must be somehow discoverable by the attacker
- The administrator must have forgotten to associate an ACL or has associated an inappropriately permissive ACL with a particular navigable resource.

## Skills Required
- [Low] In order to discover unrestricted resources, the attacker does not need special tools or skills. They only have to observe the resources or access mechanisms invoked as each action is performed and then try and access those access mechanisms directly.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- In a J2EE setting, administrators can associate a role that is impossible for the authenticator to grant users, such as "NoAccess", with all Servlets to which access is guarded by a limited number of servlets visible to, and accessible by, the user. Having done so, any direct access to those protected Servlets will be prohibited by the web container. In a more general setting, the administrator must mark every resource besides the ones supposed to be exposed to the user as accessible by a role impossible for the user to assume. The default security setting must be to deny access and then grant access only to those resources intended by business logic.

## Related Weaknesses (CWE)
- CWE-276
- CWE-285
- CWE-434
- CWE-693
- CWE-732
- CWE-1191
- CWE-1193
- CWE-1220
- CWE-1297
- CWE-1311
- CWE-1314
- CWE-1315
- CWE-1318
- CWE-1320
- CWE-1321
- CWE-1327


---

# CAPEC-10: Buffer Overflow via Environment Variables

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/10.html  

## Description
This attack pattern involves causing a buffer overflow through manipulation of environment variables. Once the adversary finds that they can modify an environment variable, they may try to overflow associated buffers. This attack leverages implicit trust often placed in environment variables.

## Related Attack Patterns
- ChildOf: CAPEC-100

## Prerequisites
- The application uses environment variables.
- An environment variable exposed to the user is vulnerable to a buffer overflow.
- The vulnerable environment variable uses untrusted data.
- Tainted data used in the environment variables is not properly validated. For instance boundary checking is not done before copying the input data to a buffer.

## Skills Required
- [Low] An attacker can simply overflow a buffer by inserting a long string into an attacker-modifiable injection vector. The result can be a DoS.
- [High] Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Do not expose environment variable to the user.
- Do not use untrusted data in your environment variables.
- Use a language or compiler that performs automatic bounds checking
- There are tools such as Sharefuzz [REF-2] which is an environment variable fuzzer for Unix that support loading a shared library. You can use Sharefuzz to determine if you are exposing an environment variable vulnerable to buffer overflow.

## Related Weaknesses (CWE)
- CWE-120
- CWE-302
- CWE-118
- CWE-119
- CWE-74
- CWE-99
- CWE-20
- CWE-680
- CWE-733
- CWE-697


---

# CAPEC-100: Overflow Buffers

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/100.html  

## Description
Buffer Overflow attacks target improper or missing bounds checking on buffer operations, typically triggered by input injected by an adversary. As a consequence, an adversary is able to write past the boundaries of allocated buffer regions in memory, causing a program crash or potentially redirection of execution as per the adversaries' choice.

## Related Attack Patterns
- ChildOf: CAPEC-123

## Prerequisites
- Targeted software performs buffer operations.
- Targeted software inadequately performs bounds-checking on buffer operations.
- Adversary has the capability to influence the input to buffer operations.

## Skills Required
- [Low] In most cases, overflowing a buffer does not require advanced skills beyond the ability to notice an overflow and stuff an input variable with content.
- [High] In cases of directed overflows, where the motive is to divert the flow of the program or application as per the adversaries' bidding, high level skills are required. This may involve detailed knowledge of the target system architecture and kernel.

## Resources Required
- None: No specialized resources are required to execute this type of attack. Detecting and exploiting a buffer overflow does not require any resources beyond knowledge of and access to the target system.

## Consequences
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Use a language or compiler that performs automatic bounds checking.
- Use secure functions not vulnerable to buffer overflow.
- If you have to use dangerous functions, make sure that you do boundary checking.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Use OS-level preventative functionality. Not a complete solution.
- Utilize static source code analysis tools to identify potential buffer overflow weaknesses in the software.

## Related Weaknesses (CWE)
- CWE-120
- CWE-119
- CWE-131
- CWE-129
- CWE-805
- CWE-680


---

# CAPEC-101: Server Side Include (SSI) Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/101.html  

## Description
An attacker can use Server Side Include (SSI) Injection to send code to a web application that then gets executed by the web server. Doing so enables the attacker to achieve similar results to Cross Site Scripting, viz., arbitrary code execution and information disclosure, albeit on a more limited scale, since the SSI directives are nowhere near as powerful as a full-fledged scripting language. Nonetheless, the attacker can conveniently gain access to sensitive files, such as password files, and execute shell commands.

## Related Attack Patterns
- ChildOf: CAPEC-253
- CanPrecede: CAPEC-600

## Prerequisites
- A web server that supports server side includes and has them enabled
- User controllable input that can carry include directives to the web server

## Skills Required
- [Medium] The attacker needs to be aware of SSI technology, determine the nature of injection and be able to craft input that results in the SSI directives being executed.

## Resources Required
- None: No specialized resources are required to execute this type of attack. Determining whether the server supports SSI does not require special tools, and nor does injecting directives that get executed. Spidering tools can make the task of finding and following links easier.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Set the OPTIONS IncludesNOEXEC in the global access.conf file or local .htaccess (Apache) file to deny SSI execution in directories that do not need them
- All user controllable input must be appropriately sanitized before use in the application. This includes omitting, or encoding, certain characters or strings that have the potential of being interpreted as part of an SSI directive
- Server Side Includes must be enabled only if there is a strong business reason to do so. Every additional component enabled on the web server increases the attack surface as well as administrative overhead

## Related Weaknesses (CWE)
- CWE-97
- CWE-74
- CWE-20


---

# CAPEC-102: Session Sidejacking

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/102.html  

## Description
Session sidejacking takes advantage of an unencrypted communication channel between a victim and target system. The attacker sniffs traffic on a network looking for session tokens in unencrypted traffic. Once a session token is captured, the attacker performs malicious actions by using the stolen token with the targeted application to impersonate the victim. This attack is a specific method of session hijacking, which is exploiting a valid session token to gain unauthorized access to a target system or information. Other methods to perform a session hijacking are session fixation, cross-site scripting, or compromising a user or server machine and stealing the session token.

## Related Attack Patterns
- ChildOf: CAPEC-593

## Prerequisites
- An attacker and the victim are both using the same WiFi network.
- The victim has an active session with a target system.
- The victim is not using a secure channel to communicate with the target system (e.g. SSL, VPN, etc.)
- The victim initiated communication with a target system that requires transfer of the session token or the target application uses AJAX and thereby periodically "rings home" asynchronously using the session token

## Skills Required
- [Low] Easy to use tools exist to automate this attack.

## Resources Required
- A packet sniffing tool, such as wireshark, can be used to capture session information.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Make sure that HTTPS is used to communicate with the target system. Alternatively, use VPN if possible. It is important to ensure that all communication between the client and the server happens via an encrypted secure channel.
- Modify the session token with each transmission and protect it with cryptography. Add the idea of request sequencing that gives the server an ability to detect replay attacks.

## Related Weaknesses (CWE)
- CWE-294
- CWE-522
- CWE-523
- CWE-319
- CWE-614


---

# CAPEC-103: Clickjacking

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/103.html  

## Description
An adversary tricks a victim into unknowingly initiating some action in one system while interacting with the UI from a seemingly completely different, usually an adversary controlled or intended, system.

## Related Attack Patterns
- ChildOf: CAPEC-173

## Prerequisites
- The victim is communicating with the target application via a web based UI and not a thick client
- The victim's browser security policies allow at least one of the following JavaScript, Flash, iFrames, ActiveX, or CSS.
- The victim uses a modern browser that supports UI elements like clickable buttons (i.e. not using an old text only browser)
- The victim has an active session with the target system.
- The target system's interaction window is open in the victim's browser and supports the ability for initiating sensitive actions on behalf of the user in the target system

## Skills Required
- [High] Crafting the proper malicious site and luring the victim to this site are not trivial tasks.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- If using the Firefox browser, use the NoScript plug-in that will help forbid iFrames.
- Turn off JavaScript, Flash and disable CSS.
- When maintaining an authenticated session with a privileged target system, do not use the same browser to navigate to unfamiliar sites to perform other activities. Finish working with the target system and logout first before proceeding to other tasks.

## Related Weaknesses (CWE)
- CWE-1021


---

# CAPEC-104: Cross Zone Scripting

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/104.html  

## Description
An attacker is able to cause a victim to load content into their web-browser that bypasses security zone controls and gain access to increased privileges to execute scripting code or other web objects such as unsigned ActiveX controls or applets. This is a privilege elevation attack targeted at zone-based web-browser security.

## Related Attack Patterns
- ChildOf: CAPEC-233

## Prerequisites
- The target must be using a zone-aware browser.

## Skills Required
- [Medium] Ability to craft malicious scripts or find them elsewhere and ability to identify functionality that is running web controls in the local zone and to find an injection vector into that functionality

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Disable script execution.
- Ensure that sufficient input validation is performed for any potentially untrusted data before it is used in any privileged context or zone
- Limit the flow of untrusted data into the privileged areas of the system that run in the higher trust zone
- Limit the sites that are being added to the local machine zone and restrict the privileges of the code running in that zone to the bare minimum
- Ensure proper HTML output encoding before writing user supplied data to the page

## Related Weaknesses (CWE)
- CWE-250
- CWE-638
- CWE-285
- CWE-116
- CWE-20


---

# CAPEC-105: HTTP Request Splitting

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/105.html  

## Description
An adversary abuses the flexibility and discrepancies in the parsing and interpretation of HTTP Request messages by different intermediary HTTP agents (e.g., load balancer, reverse proxy, web caching proxies, application firewalls, etc.) to split a single HTTP request into multiple unauthorized and malicious HTTP requests to a back-end HTTP agent (e.g., web server). See CanPrecede relationships for possible consequences.

## Related Attack Patterns
- ChildOf: CAPEC-220
- PeerOf: CAPEC-34
- CanPrecede: CAPEC-115
- CanPrecede: CAPEC-141
- CanPrecede: CAPEC-63
- CanPrecede: CAPEC-593
- CanPrecede: CAPEC-148
- CanPrecede: CAPEC-154

## Prerequisites
- An additional intermediary HTTP agent such as an application firewall or a web caching proxy between the adversary and the second agent such as a web server, that sends multiple HTTP messages over same network connection.
- Differences in the way the two HTTP agents parse and interpret HTTP requests and its headers.
- HTTP headers capable of being user-manipulated.
- HTTP agents running on HTTP/1.0 or HTTP/1.1 that allow for Keep Alive mode, Pipelined queries, and Chunked queries and responses.

## Skills Required
- [Medium] Detailed knowledge on HTTP protocol: request and response messages structure and usage of specific headers.
- [Medium] Detailed knowledge on how specific HTTP agents receive, send, process, interpret, and parse a variety of HTTP messages and headers.
- [Medium] Possess knowledge on the exact details in the discrepancies between several targeted HTTP agents in path of an HTTP message in parsing its message structure and individual headers.

## Resources Required
- Tools capable of crafting malicious HTTP messages and monitoring HTTP messages responses.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Design: evaluate HTTP agents prior to deployment for parsing/interpretation discrepancies.
- Configuration: front-end HTTP agents notice ambiguous requests.
- Configuration: back-end HTTP agents reject ambiguous requests and close the network connection.
- Configuration: Disable reuse of back-end connections.
- Configuration: Use HTTP/2 for back-end connections.
- Configuration: Use the same web server software for front-end and back-end server.
- Implementation: Utilize a Web Application Firewall (WAF) that has built-in mitigation to detect abnormal requests/responses.
- Configuration: Install latest vendor security patches available for both intermediary and back-end HTTP infrastructure (i.e. proxies and web servers)
- Configuration: Ensure that HTTP infrastructure in the chain or network path utilize a strict uniform parsing process.
- Implementation: Utilize intermediary HTTP infrastructure capable of filtering and/or sanitizing user-input.

## Related Weaknesses (CWE)
- CWE-74
- CWE-113
- CWE-138
- CWE-436


---

# CAPEC-106: DEPRECATED: XSS through Log Files

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/106.html  

## Description
This attack pattern has been deprecated as it referes to an existing chain relationship between "CAPEC-93 : Log Injection-Tampering-Forging" and "CAPEC-63 : Cross-Site Scripting". Please refer to these CAPECs going forward.


---

# CAPEC-107: Cross Site Tracing

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/107.html  

## Description
Cross Site Tracing (XST) enables an adversary to steal the victim's session cookie and possibly other authentication credentials transmitted in the header of the HTTP request when the victim's browser communicates to a destination system's web server.

## Related Attack Patterns
- ChildOf: CAPEC-593

## Prerequisites
- HTTP TRACE is enabled on the web server
- The destination system is susceptible to XSS or an adversary can leverage some other weakness to bypass the same origin policy
- Scripting is enabled in the client's browser
- HTTP is used as the communication protocol between the server and the client

## Skills Required
- [Medium] Understanding of the HTTP protocol and an ability to craft a malicious script

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Administrators should disable support for HTTP TRACE at the destination's web server. Vendors should disable TRACE by default.
- Patch web browser against known security origin policy bypass exploits.

## Related Weaknesses (CWE)
- CWE-693
- CWE-648


---

# CAPEC-108: Command Line Execution through SQL Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/108.html  

## Description
An attacker uses standard SQL injection methods to inject data into the command line for execution. This could be done directly through misuse of directives such as MSSQL_xp_cmdshell or indirectly through injection of data into the database that would be interpreted as shell commands. Sometime later, an unscrupulous backend application (or could be part of the functionality of the same application) fetches the injected data stored in the database and uses this data as command line arguments without performing proper validation. The malicious data escapes that data plane by spawning new commands to be executed on the host.

## Related Attack Patterns
- ChildOf: CAPEC-66

## Prerequisites
- The application does not properly validate data before storing in the database
- Backend application implicitly trusts the data stored in the database
- Malicious data is used on the backend as a command line argument

## Skills Required
- [High] The attacker most likely has to be familiar with the internal functionality of the system to launch this attack. Without that knowledge, there are not many feedback mechanisms to give an attacker the indication of how to perform command injection or whether the attack is succeeding.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Disable MSSQL xp_cmdshell directive on the database
- Properly validate the data (syntactically and semantically) before writing it to the database.
- Do not implicitly trust the data stored in the database. Re-validate it prior to usage to make sure that it is safe to use in a given context (e.g. as a command line argument).

## Related Weaknesses (CWE)
- CWE-89
- CWE-74
- CWE-20
- CWE-78
- CWE-114


---

# CAPEC-109: Object Relational Mapping Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/109.html  

## Description
An attacker leverages a weakness present in the database access layer code generated with an Object Relational Mapping (ORM) tool or a weakness in the way that a developer used a persistence framework to inject their own SQL commands to be executed against the underlying database. The attack here is similar to plain SQL injection, except that the application does not use JDBC to directly talk to the database, but instead it uses a data access layer generated by an ORM tool or framework (e.g. Hibernate). While most of the time code generated by an ORM tool contains safe access methods that are immune to SQL injection, sometimes either due to some weakness in the generated code or due to the fact that the developer failed to use the generated access methods properly, SQL injection is still possible.

## Related Attack Patterns
- ChildOf: CAPEC-66

## Prerequisites
- An application uses data access layer generated by an ORM tool or framework
- An application uses user supplied data in queries executed against the database
- The separation between data plane and control plane is not ensured, through either developer error or an underlying weakness in the data access layer code generation framework

## Skills Required
- [Medium] Knowledge of general SQL injection techniques and subtleties of the ORM framework is needed

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Remember to understand how to use the data access methods generated by the ORM tool / framework properly in a way that would leverage the built-in security mechanisms of the framework
- Ensure to keep up to date with security relevant updates to the persistence framework used within your application.

## Related Weaknesses (CWE)
- CWE-20
- CWE-89
- CWE-564


---

# CAPEC-11: Cause Web Server Misclassification

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/11.html  

## Description
An attack of this type exploits a Web server's decision to take action based on filename or file extension. Because different file types are handled by different server processes, misclassification may force the Web server to take unexpected action, or expected actions in an unexpected sequence. This may cause the server to exhaust resources, supply debug or system data to the attacker, or bind an attacker to a remote process.

## Related Attack Patterns
- ChildOf: CAPEC-635

## Prerequisites
- Web server software must rely on file name or file extension for processing.
- The attacker must be able to make HTTP requests to the web server.

## Skills Required
- [Low] To modify file name or file extension
- [Medium] To use misclassification to force the Web server to disclose configuration information, source, or binary data

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Implementation: Server routines should be determined by content not determined by filename or file extension.

## Related Weaknesses (CWE)
- CWE-430


---

# CAPEC-110: SQL Injection through SOAP Parameter Tampering

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/110.html  

## Description
An attacker modifies the parameters of the SOAP message that is sent from the service consumer to the service provider to initiate a SQL injection attack. On the service provider side, the SOAP message is parsed and parameters are not properly validated before being used to access a database in a way that does not use parameter binding, thus enabling the attacker to control the structure of the executed SQL query. This pattern describes a SQL injection attack with the delivery mechanism being a SOAP message.

## Related Attack Patterns
- ChildOf: CAPEC-66
- CanPrecede: CAPEC-108

## Prerequisites
- SOAP messages are used as a communication mechanism in the system
- SOAP parameters are not properly validated at the service provider
- The service provider does not properly utilize parameter binding when building SQL queries

## Skills Required
- [Medium] If the attacker is able to gain good understanding of the system's database schema
- [High] If the attacker has to perform Blind SQL Injection

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Properly validate and sanitize/reject user input at the service provider.
- Ensure that prepared statements or other mechanism that enables parameter binding is used when accessing the database in a way that would prevent the attackers' supplied data from controlling the structure of the executed query.
- At the database level, ensure that the database user used by the application in a particular context has the minimum needed privileges to the database that are needed to perform the operation. When possible, run queries against pre-generated views rather than the tables directly.

## Related Weaknesses (CWE)
- CWE-89
- CWE-20


---

# CAPEC-111: JSON Hijacking (aka JavaScript Hijacking)

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/111.html  

## Description
An attacker targets a system that uses JavaScript Object Notation (JSON) as a transport mechanism between the client and the server (common in Web 2.0 systems using AJAX) to steal possibly confidential information transmitted from the server back to the client inside the JSON object by taking advantage of the loophole in the browser's Same Origin Policy that does not prohibit JavaScript from one website to be included and executed in the context of another website.

## Related Attack Patterns
- ChildOf: CAPEC-212

## Prerequisites
- JSON is used as a transport mechanism between the client and the server
- The target server cannot differentiate real requests from forged requests
- The JSON object returned from the server can be accessed by the attackers' malicious code via a script tag

## Skills Required
- [Medium] Once this attack pattern is developed and understood, creating an exploit is not very complex.The attacker needs to have knowledge of the URLs that need to be accessed on the target system to request the JSON objects.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Ensure that server side code can differentiate between legitimate requests and forged requests. The solution is similar to protection against Cross Site Request Forger (CSRF), which is to use a hard to guess random nonce (that is unique to the victim's session with the server) that the attacker has no way of knowing (at least in the absence of other weaknesses). Each request from the client to the server should contain this nonce and the server should reject all requests that do not contain the nonce.
- On the client side, the system's design could make it difficult to get access to the JSON object content via the script tag. Since the JSON object is never assigned locally to a variable, it cannot be readily modified by the attacker before being used by a script tag. For instance, if while(1) was added to the beginning of the JavaScript returned by the server, trying to access it with a script tag would result in an infinite loop. On the other hand, legitimate client side code can remove the while(1) statement after which the JavaScript can be evaluated. A similar result can be achieved by surrounding the returned JavaScript with comment tags, or using other similar techniques (e.g. wrapping the JavaScript with HTML tags).
- Make the URLs in the system used to retrieve JSON objects unpredictable and unique for each user session.
- Ensure that to the extent possible, no sensitive data is passed from the server to the client via JSON objects. JavaScript was never intended to play that role, hence the same origin policy does not adequate address this scenario.

## Related Weaknesses (CWE)
- CWE-345
- CWE-346
- CWE-352


---

# CAPEC-112: Brute Force

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/112.html  

## Description
In this attack, some asset (information, functionality, identity, etc.) is protected by a finite secret value. The attacker attempts to gain access to this asset by using trial-and-error to exhaustively explore all the possible secret values in the hope of finding the secret (or a value that is functionally equivalent) that will unlock the asset.

## Prerequisites
- The attacker must be able to determine when they have successfully guessed the secret. As such, one-time pads are immune to this type of attack since there is no way to determine when a guess is correct.

## Skills Required
- [Low] The attack simply requires basic scripting ability to automate the exploration of the search space. More sophisticated attackers may be able to use more advanced methods to reduce the search space and increase the speed with which the secret is located.

## Resources Required
- None: No specialized resources are required to execute this type of attack. Ultimately, the speed with which an attacker discovers a secret is directly proportional to the computational resources the attacker has at their disposal. This attack method is resource expensive: having large amounts of computational power do not guarantee timely success, but having only minimal resources makes the problem intractable against all but the weakest secret selection procedures.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Select a provably large secret space for selection of the secret. Provably large means that the procedure by which the secret is selected does not have artifacts that significantly reduce the size of the total secret space.
- Use a secret space that is well known and with no known patterns that may reduce functional size.
- Do not provide the means for an attacker to determine success independently. This forces the attacker to check their guesses against an external authority, which can slow the attack and warn the defender. This mitigation may not be possible if testing material must appear externally, such as with a transmitted cryptotext.

## Related Weaknesses (CWE)
- CWE-330
- CWE-326
- CWE-521


---

# CAPEC-113: Interface Manipulation

**Abstraction:** Meta  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/113.html  

## Description
An adversary manipulates the use or processing of an interface (e.g. Application Programming Interface (API) or System-on-Chip (SoC)) resulting in an adverse impact upon the security of the system implementing the interface. This can allow the adversary to bypass access control and/or execute functionality not intended by the interface implementation, possibly compromising the system which integrates the interface. Interface manipulation can take on a number of forms including forcing the unexpected use of an interface or the use of an interface in an unintended way.

## Prerequisites
- The target system must expose interface functionality in a manner that can be discovered and manipulated by an adversary. This may require reverse engineering the interface or decrypting/de-obfuscating client-server exchanges.

## Resources Required
- The requirements vary depending upon the nature of the interface. For example, application-layer APIs related to the processing of the HTTP protocol may require one or more of the following: an Adversary-In-The-Middle (CAPEC-94) proxy, a web browser, or a programming/scripting language.

## Related Weaknesses (CWE)
- CWE-1192


---

# CAPEC-114: Authentication Abuse

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/114.html  

## Description
An attacker obtains unauthorized access to an application, service or device either through knowledge of the inherent weaknesses of an authentication mechanism, or by exploiting a flaw in the authentication scheme's implementation. In such an attack an authentication mechanism is functioning but a carefully controlled sequence of events causes the mechanism to grant access to the attacker.

## Prerequisites
- An authentication mechanism or subsystem implementing some form of authentication such as passwords, digest authentication, security certificates, etc. which is flawed in some way.

## Resources Required
- A client application, command-line access to a binary, or scripting language capable of interacting with the authentication mechanism.

## Related Weaknesses (CWE)
- CWE-287
- CWE-1244


---

# CAPEC-115: Authentication Bypass

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/115.html  

## Description
An attacker gains access to application, service, or device with the privileges of an authorized or privileged user by evading or circumventing an authentication mechanism. The attacker is therefore able to access protected data without authentication ever having taken place.

## Prerequisites
- An authentication mechanism or subsystem implementing some form of authentication such as passwords, digest authentication, security certificates, etc.

## Resources Required
- A client application, such as a web browser, or a scripting language capable of interacting with the target.

## Related Weaknesses (CWE)
- CWE-287


---

# CAPEC-116: Excavation

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/116.html  

## Description
An adversary actively probes the target in a manner that is designed to solicit information that could be leveraged for malicious purposes.

## Related Attack Patterns
- CanPrecede: CAPEC-163

## Prerequisites
- An adversary requires some way of interacting with the system.

## Resources Required
- A tool, such as an Adversary in the Middle (CAPEC-94) Proxy or a fuzzer, that is capable of generating and injecting custom inputs to be used in the attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Minimize error/response output to only what is necessary for functional use or corrective language.
- Remove potentially sensitive information that is not necessary for the application's functionality.

## Related Weaknesses (CWE)
- CWE-200
- CWE-1243


---

# CAPEC-117: Interception

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/117.html  

## Description
An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as other types of data streams (e.g. radio). The adversary can attempt to initiate the establishment of a data stream or passively observe the communications as they unfold. In all variants of this attack, the adversary is not the intended recipient of the data stream. In contrast to other means of gathering information (e.g., targeting data leaks), the adversary must actively position themself so as to observe explicit data channels (e.g. network traffic) and read the content. However, this attack differs from a Adversary-In-the-Middle (CAPEC-94) attack, as the adversary does not alter the content of the communications nor forward data to the intended recipient.

## Prerequisites
- The target must transmit data over a medium that is accessible to the adversary.

## Resources Required
- The adversary must have the necessary technology to intercept information passing between the nodes of a network. For TCP/IP, the capability to run tcpdump, ethereal, etc. can be useful. Depending upon the data being targeted the technological requirements will change.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.

## Related Weaknesses (CWE)
- CWE-319


---

# CAPEC-12: Choosing Message Identifier

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/12.html  

## Description
This pattern of attack is defined by the selection of messages distributed via multicast or public information channels that are intended for another client by determining the parameter value assigned to that client. This attack allows the adversary to gain access to potentially privileged information, and to possibly perpetrate other attacks through the distribution means by impersonation. If the channel/message being manipulated is an input rather than output mechanism for the system, (such as a command bus), this style of attack could be used to change the adversary's identifier to more a privileged one.

## Related Attack Patterns
- PeerOf: CAPEC-21
- ChildOf: CAPEC-216

## Prerequisites
- Information and client-sensitive (and client-specific) data must be present through a distribution channel available to all users.
- Distribution means must code (through channel, message identifiers, or convention) message destination in a manner visible within the distribution means itself (such as a control channel) or in the messages themselves.

## Skills Required
- [Low] All the adversary needs to discover is the format of the messages on the channel/distribution means and the particular identifier used within the messages.

## Resources Required
- The adversary needs the ability to control source code or application configuration responsible for selecting which message/channel id is absorbed from the public distribution means.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Associate some ACL (in the form of a token) with an authenticated user which they provide middleware. The middleware uses this token as part of its channel/message selection for that client, or part of a discerning authorization decision for privileged channels/messages. The purpose is to architect the system in a way that associates proper authentication/authorization with each channel/message.
- Re-architect system input/output channels as appropriate to distribute self-protecting data. That is, encrypt (or otherwise protect) channels/messages so that only authorized readers can see them.

## Related Weaknesses (CWE)
- CWE-201
- CWE-306


---

# CAPEC-120: Double Encoding

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/120.html  

## Description
The adversary utilizes a repeating of the encoding process for a set of characters (that is, character encoding a character encoding of a character) to obfuscate the payload of a particular request. This may allow the adversary to bypass filters that attempt to detect illegal characters or strings, such as those that might be used in traversal or injection attacks. Filters may be able to catch illegal encoded strings, but may not catch doubly encoded strings. For example, a dot (.), often used in path traversal attacks and therefore often blocked by filters, could be URL encoded as %2E. However, many filters recognize this encoding and would still block the request. In a double encoding, the % in the above URL encoding would be encoded again as %25, resulting in %252E which some filters might not catch, but which could still be interpreted as a dot (.) by interpreters on the target.

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- The target's filters must fail to detect that a character has been doubly encoded but its interpreting engine must still be able to convert a doubly encoded character to an un-encoded character.
- The application accepts and decodes URL string request.
- The application performs insufficient filtering/canonicalization on the URLs.

## Resources Required
- Tools that automate encoding of data can assist the adversary in generating encoded strings.

## Mitigations
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system. Test your decoding process against malicious input.
- Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding.
- When client input is required from web-based forms, avoid using the "GET" method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the "POST method whenever possible.
- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.
- Refer to the RFCs to safely decode URL.
- Regular expression can be used to match safe URL patterns. However, that may discard valid URL requests if the regular expression is too restrictive.
- There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx).

## Related Weaknesses (CWE)
- CWE-173
- CWE-172
- CWE-177
- CWE-181
- CWE-183
- CWE-184
- CWE-74
- CWE-20
- CWE-697
- CWE-692


---

# CAPEC-121: Exploit Non-Production Interfaces

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/121.html  

## Description
An adversary exploits a sample, demonstration, test, or debug interface that is unintentionally enabled on a production system, with the goal of gleaning information or leveraging functionality that would otherwise be unavailable.

## Related Attack Patterns
- ChildOf: CAPEC-113

## Prerequisites
- The target must have configured non-production interfaces and failed to secure or remove them when brought into a production environment.

## Skills Required
- [High] Exploiting non-production interfaces requires significant skill and knowledge about the potential non-production interfaces left enabled in production.

## Resources Required
- For some interfaces, the adversary will need that appropriate client application or hardware that interfaces with the interface. Other non-production interfaces can be executed using simple tools, such as web browsers or console windows. In some cases, an adversary may need to be able to authenticate to the target before it can access the vulnerable interface.

## Consequences
- Scope: Confidentiality, Access Control, Authentication; Impact: Gain Privileges, Bypass Protection Mechanism
- Scope: Confidentiality, Access Control, Authorization; Impact: Read Data, Execute Unauthorized Commands
- Scope: Access Control, Integrity; Impact: Modify Data, Alter Execution Logic

## Mitigations
- Ensure that production systems do not contain non-production interfaces and that these interfaces are only used in development environments.

## Related Weaknesses (CWE)
- CWE-489
- CWE-1209
- CWE-1259
- CWE-1267
- CWE-1270
- CWE-1294
- CWE-1295
- CWE-1296
- CWE-1302
- CWE-1313


---

# CAPEC-122: Privilege Abuse

**Abstraction:** Meta  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/122.html  

## Description
An adversary is able to exploit features of the target that should be reserved for privileged users or administrators but are exposed to use by lower or non-privileged accounts. Access to sensitive information and functionality must be controlled to ensure that only authorized users are able to access these resources.

## Related Attack Patterns
- CanPrecede: CAPEC-664

## Prerequisites
- The target must have misconfigured their access control mechanisms such that sensitive information, which should only be accessible to more trusted users, remains accessible to less trusted users.
- The adversary must have access to the target, albeit with an account that is less privileged than would be appropriate for the targeted resources.

## Skills Required
- [Low] Adversary can leverage privileged features they already have access to without additional effort or skill. Adversary is only required to have access to an account with improper priveleges.

## Resources Required
- None: No specialized resources are required to execute this type of attack. The ability to access the target is required.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Authorization; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Configure account privileges such privileged/administrator functionality is not exposed to non-privileged/lower accounts.

## Related Weaknesses (CWE)
- CWE-269
- CWE-732
- CWE-1317


---

# CAPEC-123: Buffer Manipulation

**Abstraction:** Meta  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/123.html  

## Description
An adversary manipulates an application's interaction with a buffer in an attempt to read or modify data they shouldn't have access to. Buffer attacks are distinguished in that it is the buffer space itself that is the target of the attack rather than any code responsible for interpreting the content of the buffer. In virtually all buffer attacks the content that is placed in the buffer is immaterial. Instead, most buffer attacks involve retrieving or providing more input than can be stored in the allocated buffer, resulting in the reading or overwriting of other unintended program memory.

## Prerequisites
- The adversary must identify a programmatic means for interacting with a buffer, such as vulnerable C code, and be able to provide input to this interaction.

## Consequences
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality; Impact: Execute Unauthorized Commands, Modify Data, Read Data

## Mitigations
- To help protect an application from buffer manipulation attacks, a number of potential mitigations can be leveraged. Before starting the development of the application, consider using a code language (e.g., Java) or compiler that limits the ability of developers to act beyond the bounds of a buffer. If the chosen language is susceptible to buffer related issues (e.g., C) then consider using secure functions instead of those vulnerable to buffer manipulations. If a potentially dangerous function must be used, make sure that proper boundary checking is performed. Additionally, there are often a number of compiler-based mechanisms (e.g., StackGuard, ProPolice and the Microsoft Visual Studio /GS flag) that can help identify and protect against potential buffer issues. Finally, there may be operating system level preventative functionality that can be applied.

## Related Weaknesses (CWE)
- CWE-119


---

# CAPEC-124: Shared Resource Manipulation

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/124.html  

## Description
An adversary exploits a resource shared between multiple applications, an application pool or hardware pin multiplexing to affect behavior. Resources may be shared between multiple applications or between multiple threads of a single application. Resource sharing is usually accomplished through mutual access to a single memory location or multiplexed hardware pins. If an adversary can manipulate this shared resource (usually by co-opting one of the applications or threads) the other applications or threads using the shared resource will often continue to trust the validity of the compromised shared resource and use it in their calculations. This can result in invalid trust assumptions, corruption of additional data through the normal operations of the other users of the shared resource, or even cause a crash or compromise of the sharing applications.

## Prerequisites
- The target applications, threads or functions must share resources between themselves.
- The adversary must be able to manipulate some piece of the shared resource either directly or indirectly and the other users of the data must accept the changed data as valid. Usually this requires that the adversary be able to compromise one of the sharing applications or threads in order to manipulate the shared data.

## Resources Required
- None: The attacker does not need any specialized resources to execute this type of attack.

## Related Weaknesses (CWE)
- CWE-1189
- CWE-1331


---

# CAPEC-125: Flooding

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/125.html  

## Description
An adversary consumes the resources of a target by rapidly engaging in a large number of interactions with the target. This type of attack generally exposes a weakness in rate limiting or flow. When successful this attack prevents legitimate users from accessing the service and can cause the target to crash. This attack differs from resource depletion through leaks or allocations in that the latter attacks do not rely on the volume of requests made to the target but instead focus on manipulation of the target's operations. The key factor in a flooding attack is the number of requests the adversary can make in a given period of time. The greater this number, the more likely an attack is to succeed against a given target.

## Prerequisites
- Any target that services requests is vulnerable to this attack on some level of scale.

## Resources Required
- A script or program capable of generating more requests than the target can handle, or a network or cluster of objects all capable of making simultaneous requests.

## Consequences
- Scope: Availability; Impact: Unreliable Execution, Resource Consumption

## Mitigations
- Ensure that protocols have specific limits of scale configured.
- Specify expectations for capabilities and dictate which behaviors are acceptable when resource allocation reaches limits.
- Uniformly throttle all requests in order to make it more difficult to consume resources more quickly than they can again be freed.

## Related Weaknesses (CWE)
- CWE-404
- CWE-770


---

# CAPEC-126: Path Traversal

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/126.html  

## Description
An adversary uses path manipulation methods to exploit insufficient input validation of a target to obtain access to data that should be not be retrievable by ordinary well-formed requests. A typical variety of this attack involves specifying a path to a desired file together with dot-dot-slash characters, resulting in the file access API or function traversing out of the intended directory structure and into the root file system. By replacing or modifying the expected path information the access function or API retrieves the file desired by the attacker. These attacks either involve the attacker providing a complete path to a targeted file or using control characters (e.g. path separators (/ or \) and/or dots (.)) to reach desired directories or files.

## Related Attack Patterns
- ChildOf: CAPEC-153
- CanPrecede: CAPEC-664

## Prerequisites
- The attacker must be able to control the path that is requested of the target.
- The target must fail to adequately sanitize incoming paths

## Skills Required
- [Low] Simple command line attacks or to inject the malicious payload in a web page.
- [Medium] Customizing attacks to bypass non trivial filters in the application.

## Resources Required
- The ability to manually manipulate path information either directly through a client application relative to the service or application or via a proxy application.

## Consequences
- Scope: Integrity, Confidentiality, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Design: Configure the access control correctly.
- Design: Enforce principle of least privilege.
- Design: Execute programs with constrained privileges, so parent process does not open up further vulnerabilities. Ensure that all directories, temporary directories and files, and memory are executing with limited privileges to protect against remote execution.
- Design: Input validation. Assume that user inputs are malicious. Utilize strict type, character, and encoding enforcement.
- Design: Proxy communication to host, so that communications are terminated at the proxy, sanitizing the requests before forwarding to server host.
- Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.
- Implementation: Host integrity monitoring for critical files, directories, and processes. The goal of host integrity monitoring is to be aware when a security issue has occurred so that incident response and other forensic activities can begin.
- Implementation: Perform input validation for all remote content, including remote and user-generated content.
- Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.
- Implementation: Use indirect references rather than actual file names.
- Implementation: Use possible permissions on file access when developing and deploying web applications.
- Implementation: Validate user input by only accepting known good. Ensure all content that is delivered to client is sanitized against an acceptable content specification -- using an allowlist approach.

## Related Weaknesses (CWE)
- CWE-22


---

# CAPEC-127: Directory Indexing

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/127.html  

## Description
An adversary crafts a request to a target that results in the target listing/indexing the content of a directory as output. One common method of triggering directory contents as output is to construct a request containing a path that terminates in a directory name rather than a file name since many applications are configured to provide a list of the directory's contents when such a request is received. An adversary can use this to explore the directory tree on a target as well as learn the names of files. This can often end up revealing test files, backup files, temporary files, hidden files, configuration files, user accounts, script contents, as well as naming conventions, all of which can be used by an attacker to mount additional attacks.

## Related Attack Patterns
- ChildOf: CAPEC-54

## Prerequisites
- The target must be misconfigured to return a list of a directory's content when it receives a request that ends in a directory name rather than a file name.
- The adversary must be able to control the path that is requested of the target.
- The administrator must have failed to properly configure an ACL or has associated an overly permissive ACL with a particular directory.
- The server version or patch level must not inherently prevent known directory listing attacks from working.

## Skills Required
- [Low] To issue the request to URL without given a specific file name
- [High] To bypass the access control of the directory of listings

## Resources Required
- Ability to send HTTP requests to a web application.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- 1. Using blank index.html: putting blank index.html simply prevent directory listings from displaying to site visitors.
- 2. Preventing with .htaccess in Apache web server: In .htaccess, write "Options-indexes".
- 3. Suppressing error messages: using error 403 "Forbidden" message exactly like error 404 "Not Found" message.

## Related Weaknesses (CWE)
- CWE-424
- CWE-425
- CWE-288
- CWE-285
- CWE-732
- CWE-276
- CWE-693


---

# CAPEC-128: Integer Attacks

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/128.html  

## Description
An attacker takes advantage of the structure of integer variables to cause these variables to assume values that are not expected by an application. For example, adding one to the largest positive integer in a signed integer variable results in a negative number. Negative numbers may be illegal in an application and the application may prevent an attacker from providing them directly, but the application may not consider that adding two positive numbers can create a negative number do to the structure of integer storage formats.

## Related Attack Patterns
- ChildOf: CAPEC-153

## Prerequisites
- The target application must have an integer variable for which only some of the possible integer values are expected by the application and where there are no checks on the value of the variable before use.
- The attacker must be able to manipulate the targeted integer variable such that normal operations result in non-standard values due to the storage structure of integers.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Related Weaknesses (CWE)
- CWE-682


---

# CAPEC-129: Pointer Manipulation

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/129.html  

## Description
This attack pattern involves an adversary manipulating a pointer within a target application resulting in the application accessing an unintended memory location. This can result in the crashing of the application or, for certain pointer values, access to data that would not normally be possible or the execution of arbitrary code. Since pointers are simply integer variables, Integer Attacks may often be used in Pointer Attacks.

## Prerequisites
- The target application must have a pointer variable that the attacker can influence to hold an arbitrary value.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Related Weaknesses (CWE)
- CWE-682
- CWE-822
- CWE-823


---

# CAPEC-13: Subverting Environment Variable Values

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/13.html  

## Description
The adversary directly or indirectly modifies environment variables used by or controlling the target software. The adversary's goal is to cause the target software to deviate from its expected operation in a manner that benefits the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-77
- CanPrecede: CAPEC-14
- PeerOf: CAPEC-10

## Prerequisites
- An environment variable is accessible to the user.
- An environment variable used by the application can be tainted with user supplied data.
- Input data used in an environment variable is not validated properly.
- The variables encapsulation is not done properly. For instance setting a variable as public in a class makes it visible and an adversary may attempt to manipulate that variable.

## Skills Required
- [Low] In a web based scenario, the client controls the data that it submitted to the server. So anybody can try to send malicious data and try to bypass the authentication mechanism.
- [High] Some more advanced attacks may require knowledge about protocols and probing technique which help controlling a variable. The malicious user may try to understand the authentication mechanism in order to defeat it.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality; Impact: Read Data
- Scope: Accountability; Impact: Hide Activities

## Mitigations
- Protect environment variables against unauthorized read and write access.
- Protect the configuration files which contain environment variables against illegitimate read and write access.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.
- Apply the least privilege principles. If a process has no legitimate reason to read an environment variable do not give that privilege.

## Related Weaknesses (CWE)
- CWE-353
- CWE-285
- CWE-302
- CWE-74
- CWE-15
- CWE-73
- CWE-20
- CWE-200


---

# CAPEC-130: Excessive Allocation

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/130.html  

## Description
An adversary causes the target to allocate excessive resources to servicing the attackers' request, thereby reducing the resources available for legitimate services and degrading or denying services. Usually, this attack focuses on memory allocation, but any finite resource on the target could be the attacked, including bandwidth, processing cycles, or other resources. This attack does not attempt to force this allocation through a large number of requests (that would be Resource Depletion through Flooding) but instead uses one or a small number of requests that are carefully formatted to force the target to allocate excessive resources to service this request(s). Often this attack takes advantage of a bug in the target to cause the target to allocate resources vastly beyond what would be needed for a normal request.

## Prerequisites
- The target must accept service requests from the attacker and the adversary must be able to control the resource allocation associated with this request to be in excess of the normal allocation. The latter is usually accomplished through the presence of a bug on the target that allows the adversary to manipulate variables used in the allocation.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Limit the amount of resources that are accessible to unprivileged users.
- Assume all input is malicious. Consider all potentially relevant properties when validating input.
- Consider uniformly throttling all requests in order to make it more difficult to consume resources more quickly than they can again be freed.
- Use resource-limiting settings, if possible.

## Related Weaknesses (CWE)
- CWE-404
- CWE-770
- CWE-1325


---

# CAPEC-131: Resource Leak Exposure

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/131.html  

## Description
An adversary utilizes a resource leak on the target to deplete the quantity of the resource available to service legitimate requests.

## Prerequisites
- The target must have a resource leak that the adversary can repeatedly trigger.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Availability; Impact: Unreliable Execution, Resource Consumption

## Mitigations
- If possible, leverage coding language(s) that do not allow this weakness to occur (e.g., Java, Ruby, and Python all perform automatic garbage collection that releases memory for objects that have been deallocated).
- Memory should always be allocated/freed using matching functions (e.g., malloc/free, new/delete, etc.)
- Implement best practices with respect to memory management, including the freeing of all allocated resources at all exit points and ensuring consistency with how and where memory is freed in a function.

## Related Weaknesses (CWE)
- CWE-404


---

# CAPEC-132: Symlink Attack

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/132.html  

## Description
An adversary positions a symbolic link in such a manner that the targeted user or application accesses the link's endpoint, assuming that it is accessing a file with the link's name.

## Related Attack Patterns
- ChildOf: CAPEC-159

## Prerequisites
- The targeted application must perform the desired activities on a file without checking whether the file is a symbolic link or not. The adversary must be able to predict the name of the file the target application is modifying and be able to create a new symbolic link where that file would appear.

## Skills Required
- [Low] To create symlinks
- [High] To identify the files and create the symlinks during the file operation time window

## Resources Required
- None: No specialized resources are required to execute this type of attack. The only requirement is the ability to create the necessary symbolic link.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Design: Check for the existence of files to be created, if in existence verify they are neither symlinks nor hard links before opening them.
- Implementation: Use randomly generated file names for temporary files. Give the files restrictive permissions.

## Related Weaknesses (CWE)
- CWE-59


---

# CAPEC-133: Try All Common Switches

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/133.html  

## Description
An attacker attempts to invoke all common switches and options in the target application for the purpose of discovering weaknesses in the target. For example, in some applications, adding a --debug switch causes debugging information to be displayed, which can sometimes reveal sensitive processing or configuration information to an attacker. This attack differs from other forms of API abuse in that the attacker is indiscriminately attempting to invoke options in the hope that one of them will work rather than specifically targeting a known option. Nonetheless, even if the attacker is familiar with the published options of a targeted application this attack method may still be fruitful as it might discover unpublicized functionality.

## Related Attack Patterns
- ChildOf: CAPEC-113

## Prerequisites
- The attacker must be able to control the options or switches sent to the target.

## Resources Required
- None: No specialized resources are required to execute this type of attack. The only requirement is the ability to send requests to the target.

## Mitigations
- Design: Minimize switch and option functionality to only that necessary for correct function of the command.
- Implementation: Remove all debug and testing options from production code.

## Related Weaknesses (CWE)
- CWE-912


---

# CAPEC-134: Email Injection

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/134.html  

## Description
An adversary manipulates the headers and content of an email message by injecting data via the use of delimiter characters native to the protocol.

## Related Attack Patterns
- ChildOf: CAPEC-137

## Prerequisites
- The target application must allow the user to send email to some recipient, to specify the content at least one header field in the message, and must fail to sanitize against the injection of command separators.
- The adversary must have the ability to access the target mail application.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Related Weaknesses (CWE)
- CWE-150


---

# CAPEC-135: Format String Injection

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/135.html  

## Description
An adversary includes formatting characters in a string input field on the target application. Most applications assume that users will provide static text and may respond unpredictably to the presence of formatting character. For example, in certain functions of the C programming languages such as printf, the formatting character %s will print the contents of a memory location expecting this location to identify a string and the formatting character %n prints the number of DWORD written in the memory. An adversary can use this to read or write to memory locations or files, or simply to manipulate the value of the resulting text in unexpected ways. Reading or writing memory may result in program crashes and writing memory could result in the execution of arbitrary code if the adversary can write to the program stack.

## Related Attack Patterns
- ChildOf: CAPEC-137

## Prerequisites
- The target application must accept a strings as user input, fail to sanitize string formatting characters in the user input, and process this string using functions that interpret string formatting characters.

## Skills Required
- [High] In order to discover format string vulnerabilities it takes only low skill, however, converting this discovery into a working exploit requires advanced knowledge on the part of the adversary.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Access Control; Impact: Gain Privileges
- Scope: Integrity; Impact: Execute Unauthorized Commands
- Scope: Access Control; Impact: Bypass Protection Mechanism

## Mitigations
- Limit the usage of formatting string functions.
- Strong input validation - All user-controllable input must be validated and filtered for illegal formatting characters.

## Related Weaknesses (CWE)
- CWE-134
- CWE-20
- CWE-74


---

# CAPEC-136: LDAP Injection

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/136.html  

## Description
An attacker manipulates or crafts an LDAP query for the purpose of undermining the security of the target. Some applications use user input to create LDAP queries that are processed by an LDAP server. For example, a user might provide their username during authentication and the username might be inserted in an LDAP query during the authentication process. An attacker could use this input to inject additional commands into an LDAP query that could disclose sensitive information. For example, entering a * in the aforementioned query might return information about all users on the system. This attack is very similar to an SQL injection attack in that it manipulates a query to gather additional information or coerce a particular return value.

## Related Attack Patterns
- ChildOf: CAPEC-248

## Prerequisites
- The target application must accept a string as user input, fail to sanitize characters that have a special meaning in LDAP queries in the user input, and insert the user-supplied string in an LDAP query which is then processed.

## Skills Required
- [Medium] The attacker needs to have knowledge of LDAP, especially its query syntax.

## Consequences
- Scope: Availability; Impact: Unreliable Execution
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as LDAP content.
- Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the LDAP or application.

## Related Weaknesses (CWE)
- CWE-77
- CWE-90
- CWE-20


---

# CAPEC-137: Parameter Injection

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/137.html  

## Description
An adversary manipulates the content of request parameters for the purpose of undermining the security of the target. Some parameter encodings use text characters as separators. For example, parameters in a HTTP GET message are encoded as name-value pairs separated by an ampersand (&). If an attacker can supply text strings that are used to fill in these parameters, then they can inject special characters used in the encoding scheme to add or modify parameters. For example, if user input is fed directly into an HTTP GET request and the user provides the value "myInput&new_param=myValue", then the input parameter is set to myInput, but a new parameter (new_param) is also added with a value of myValue. This can significantly change the meaning of the query that is processed by the server. Any encoding scheme where parameters are identified and separated by text characters is potentially vulnerable to this attack - the HTTP GET encoding used above is just one example.

## Prerequisites
- The target application must use a parameter encoding where separators and parameter identifiers are expressed in regular text.
- The target application must accept a string as user input, fail to sanitize characters that have a special meaning in the parameter encoding, and insert the user-supplied string in an encoding which is then processed.

## Resources Required
- None: No specialized resources are required to execute this type of attack. The only requirement is the ability to provide string input to the target.

## Consequences
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Implement an audit log written to a separate host. In the event of a compromise, the audit log may be able to provide evidence and details of the compromise.
- Treat all user input as untrusted data that must be validated before use.

## Related Weaknesses (CWE)
- CWE-88


---

# CAPEC-138: Reflection Injection

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/138.html  

## Description
An adversary supplies a value to the target application which is then used by reflection methods to identify a class, method, or field. For example, in the Java programming language the reflection libraries permit an application to inspect, load, and invoke classes and their components by name. If an adversary can control the input into these methods including the name of the class/method/field or the parameters passed to methods, they can cause the targeted application to invoke incorrect methods, read random fields, or even to load and utilize malicious classes that the adversary created. This can lead to the application revealing sensitive information, returning incorrect results, or even having the adversary take control of the targeted application.

## Related Attack Patterns
- ChildOf: CAPEC-137

## Prerequisites
- The target application must utilize reflection libraries and allow users to directly control the parameters to these methods. If the adversary can host classes where the target can invoke them, more powerful variants of this attack are possible.
- The target application must accept a string as user input, fail to sanitize characters that have a special meaning in the parameter encoding, and insert the user-supplied string in an encoding which is then processed.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Related Weaknesses (CWE)
- CWE-470


---

# CAPEC-139: Relative Path Traversal

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/139.html  

## Description
An attacker exploits a weakness in input validation on the target by supplying a specially constructed path utilizing dot and slash characters for the purpose of obtaining access to arbitrary files or resources. An attacker modifies a known path on the target in order to reach material that is not available through intended channels. These attacks normally involve adding additional path separators (/ or \) and/or dots (.), or encodings thereof, in various combinations in order to reach parent directories or entirely separate trees of the target's directory structure.

## Related Attack Patterns
- ChildOf: CAPEC-126

## Prerequisites
- The target application must accept a string as user input, fail to sanitize combinations of characters in the input that have a special meaning in the context of path navigation, and insert the user-supplied string into path navigation commands.

## Skills Required
- [Low] To inject the malicious payload in a web page
- [High] To bypass non trivial filters in the application

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Access Control; Impact: Bypass Protection Mechanism
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Design: Input validation. Assume that user inputs are malicious. Utilize strict type, character, and encoding enforcement
- Implementation: Perform input validation for all remote content, including remote and user-generated content.
- Implementation: Validate user input by only accepting known good. Ensure all content that is delivered to client is sanitized against an acceptable content specification -- using an allowlist approach.
- Implementation: Prefer working without user input when using file system calls
- Implementation: Use indirect references rather than actual file names.
- Implementation: Use possible permissions on file access when developing and deploying web applications.

## Related Weaknesses (CWE)
- CWE-23


---

# CAPEC-14: Client-side Injection-induced Buffer Overflow

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/14.html  

## Description
This type of attack exploits a buffer overflow vulnerability in targeted client software through injection of malicious content from a custom-built hostile service. This hostile service is created to deliver the correct content to the client software. For example, if the client-side application is a browser, the service will host a webpage that the browser loads.

## Related Attack Patterns
- ChildOf: CAPEC-100

## Prerequisites
- The targeted client software communicates with an external server.
- The targeted client software has a buffer overflow vulnerability.

## Skills Required
- [Low] To achieve a denial of service, an attacker can simply overflow a buffer by inserting a long string into an attacker-modifiable injection vector.
- [High] Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap requires a more in-depth knowledge and higher skill level.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- The client software should not install untrusted code from a non-authenticated server.
- The client software should have the latest patches and should be audited for vulnerabilities before being used to communicate with potentially hostile servers.
- Perform input validation for length of buffer inputs.
- Use a language or compiler that performs automatic bounds checking.
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Ensure all buffer uses are consistently bounds-checked.
- Use OS-level preventative functionality. Not a complete solution.

## Related Weaknesses (CWE)
- CWE-120
- CWE-353
- CWE-118
- CWE-119
- CWE-74
- CWE-20
- CWE-680
- CWE-697


---

# CAPEC-140: Bypassing of Intermediate Forms in Multiple-Form Sets

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/140.html  

## Description
Some web applications require users to submit information through an ordered sequence of web forms. This is often done if there is a very large amount of information being collected or if information on earlier forms is used to pre-populate fields or determine which additional information the application needs to collect. An attacker who knows the names of the various forms in the sequence may be able to explicitly type in the name of a later form and navigate to it without first going through the previous forms. This can result in incomplete collection of information, incorrect assumptions about the information submitted by the attacker, or other problems that can impair the functioning of the application.

## Related Attack Patterns
- ChildOf: CAPEC-74

## Prerequisites
- The target must collect information from the user in a series of forms where each form has its own URL that the attacker can anticipate and the application must fail to detect attempts to access intermediate forms without first filling out the previous forms.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Related Weaknesses (CWE)
- CWE-372


---

# CAPEC-141: Cache Poisoning

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/141.html  

## Description
An attacker exploits the functionality of cache technologies to cause specific data to be cached that aids the attackers' objectives. This describes any attack whereby an attacker places incorrect or harmful material in cache. The targeted cache can be an application's cache (e.g. a web browser cache) or a public cache (e.g. a DNS or ARP cache). Until the cache is refreshed, most applications or clients will treat the corrupted cache value as valid. This can lead to a wide range of exploits including redirecting web browsers towards sites that install malware and repeatedly incorrect calculations based on the incorrect value.

## Related Attack Patterns
- ChildOf: CAPEC-161

## Prerequisites
- The attacker must be able to modify the value stored in a cache to match a desired value.
- The targeted application must not be able to detect the illicit modification of the cache and must trust the cache value in its calculations.

## Skills Required
- [Medium] To overwrite/modify targeted cache

## Mitigations
- Configuration: Disable client side caching.
- Implementation: Listens for query replies on a network, and sends a notification via email when an entry changes.

## Related Weaknesses (CWE)
- CWE-348
- CWE-345
- CWE-349
- CWE-346


---

# CAPEC-142: DNS Cache Poisoning

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/142.html  

## Description
A domain name server translates a domain name (such as www.example.com) into an IP address that Internet hosts use to contact Internet resources. An adversary modifies a public DNS cache to cause certain names to resolve to incorrect addresses that the adversary specifies. The result is that client applications that rely upon the targeted cache for domain name resolution will be directed not to the actual address of the specified domain name but to some other address. Adversaries can use this to herd clients to sites that install malware on the victim's computer or to masquerade as part of a Pharming attack.

## Related Attack Patterns
- ChildOf: CAPEC-141
- CanPrecede: CAPEC-89

## Prerequisites
- A DNS cache must be vulnerable to some attack that allows the adversary to replace addresses in its lookup table.Client applications must trust the corrupted cashed values and utilize them for their domain name resolutions.

## Skills Required
- [Medium] To overwrite/modify targeted DNS cache

## Resources Required
- The adversary must have the resources to modify the targeted cache. In addition, in most cases the adversary will wish to host the sites to which users will be redirected, although in some cases redirecting to a third party site will accomplish the adversary's goals.

## Mitigations
- Configuration: Make sure your DNS servers have been updated to the latest versions
- Configuration: UNIX services like rlogin, rsh/rcp, xhost, and nfs are all susceptible to wrong information being held in a cache. Care should be taken with these services so they do not rely upon DNS caches that have been exposed to the Internet.
- Configuration: Disable client side DNS caching.

## Related Weaknesses (CWE)
- CWE-348
- CWE-345
- CWE-349
- CWE-346
- CWE-350


---

# CAPEC-143: Detect Unpublicized Web Pages

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/143.html  

## Description
An adversary searches a targeted web site for web pages that have not been publicized. In doing this, the adversary may be able to gain access to information that the targeted site did not intend to make public.

## Related Attack Patterns
- ChildOf: CAPEC-150

## Prerequisites
- The targeted web site must include pages within its published tree that are not connected to its tree of links. The sensitivity of the content of these pages determines the severity of this attack.

## Resources Required
- Spidering tools to explore the target web site are extremely useful in this attack especially when attacking large sites. Some tools might also be able to automatically construct common page locations from known paths.

## Related Weaknesses (CWE)
- CWE-425


---

# CAPEC-144: Detect Unpublicized Web Services

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/144.html  

## Description
An adversary searches a targeted web site for web services that have not been publicized. This attack can be especially dangerous since unpublished but available services may not have adequate security controls placed upon them given that an administrator may believe they are unreachable.

## Related Attack Patterns
- ChildOf: CAPEC-150

## Prerequisites
- The targeted web site must include unpublished services within its web tree. The nature of these services determines the severity of this attack.

## Resources Required
- Spidering tools to explore the target web site are extremely useful in this attack especially when attacking large sites. Some tools might also be able to automatically construct common service queries from known paths.

## Related Weaknesses (CWE)
- CWE-425


---

# CAPEC-145: Checksum Spoofing

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/145.html  

## Description
An adversary spoofs a checksum message for the purpose of making a payload appear to have a valid corresponding checksum. Checksums are used to verify message integrity. They consist of some value based on the value of the message they are protecting. Hash codes are a common checksum mechanism. Both the sender and recipient are able to compute the checksum based on the contents of the message. If the message contents change between the sender and recipient, the sender and recipient will compute different checksum values. Since the sender's checksum value is transmitted with the message, the recipient would know that a modification occurred. In checksum spoofing an adversary modifies the message body and then modifies the corresponding checksum so that the recipient's checksum calculation will match the checksum (created by the adversary) in the message. This would prevent the recipient from realizing that a change occurred.

## Related Attack Patterns
- ChildOf: CAPEC-148

## Prerequisites
- The adversary must be able to intercept a message from the sender (keeping the recipient from getting it), modify it, and send the modified message to the recipient.
- The sender and recipient must use a checksum to protect the integrity of their message and transmit this checksum in a manner where the adversary can intercept and modify it.
- The checksum value must be computable using information known to the adversary. A cryptographic checksum, which uses a key known only to the sender and recipient, would thwart this attack.

## Resources Required
- The adversary must have a utility that can intercept and modify messages between the sender and recipient.

## Related Weaknesses (CWE)
- CWE-354


---

# CAPEC-146: XML Schema Poisoning

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/146.html  

## Description
An adversary corrupts or modifies the content of XML schema information passed between a client and server for the purpose of undermining the security of the target. XML Schemas provide the structure and content definitions for XML documents. Schema poisoning is the ability to manipulate a schema either by replacing or modifying it to compromise the programs that process documents that use this schema.

## Related Attack Patterns
- ChildOf: CAPEC-271

## Prerequisites
- Some level of access to modify the target schema.
- The schema used by the target application must be improperly secured against unauthorized modification and manipulation.

## Resources Required
- Access to the schema and the knowledge and ability modify it. Ability to replace or redirect access to the modified schema.

## Consequences
- Scope: Availability; Impact: Unreliable Execution, Resource Consumption
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Design: Protect the schema against unauthorized modification.
- Implementation: For applications that use a known schema, use a local copy or a known good repository instead of the schema reference supplied in the XML document. Additionally, ensure that the proper permissions are set on local files to avoid unauthorized modification.
- Implementation: For applications that leverage remote schemas, use the HTTPS protocol to prevent modification of traffic in transit and to avoid unauthorized modification.

## Related Weaknesses (CWE)
- CWE-15
- CWE-472


---

# CAPEC-147: XML Ping of the Death

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/147.html  

## Description
An attacker initiates a resource depletion attack where a large number of small XML messages are delivered at a sufficiently rapid rate to cause a denial of service or crash of the target. Transactions such as repetitive SOAP transactions can deplete resources faster than a simple flooding attack because of the additional resources used by the SOAP protocol and the resources necessary to process SOAP messages. The transactions used are immaterial as long as they cause resource utilization on the target. In other words, this is a normal flooding attack augmented by using messages that will require extra processing on the target.

## Related Attack Patterns
- ChildOf: CAPEC-528

## Prerequisites
- The target must receive and process XML transactions.

## Skills Required
- [Low] To send small XML messages
- [High] To use distributed network to launch the attack

## Resources Required
- Transaction generator(s)/source(s) and ability to cause arrival of messages at the target with sufficient rapidity to overload target. Larger targets may be able to handle large volumes of requests so the attacker may require significant resources (such as a distributed network) to affect the target. However, the resources required of the attacker would be less than in the case of a simple flooding attack against the same target.

## Consequences
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Design: Build throttling mechanism into the resource allocation. Provide for a timeout mechanism for allocated resources whose transaction does not complete within a specified interval.
- Implementation: Provide for network flow control and traffic shaping to control access to the resources.

## Related Weaknesses (CWE)
- CWE-400
- CWE-770


---

# CAPEC-148: Content Spoofing

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/148.html  

## Description
An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to display the adversary's content instead of the owner's content. However, any content can be spoofed, including the content of email messages, file transfers, or the content of other network communication protocols. Content can be modified at the source (e.g. modifying the source file for a web page) or in transit (e.g. intercepting and modifying a message between the sender and recipient). Usually, the adversary will attempt to hide the fact that the content has been modified, but in some cases, such as with web site defacement, this is not necessary. Content Spoofing can lead to malware exposure, financial fraud (if the content governs financial transactions), privacy violations, and other unwanted outcomes.

## Prerequisites
- The target must provide content but fail to adequately protect it against modification.The adversary must have the means to alter data to which they are not authorized. If the content is to be modified in transit, the adversary must be able to intercept the targeted messages.

## Resources Required
- If the content is to be modified in transit, the adversary requires a tool capable of intercepting the target's communication and generating/creating custom packets to impact the communications. In some variants, the targeted content is altered so that all or some of it is redirected towards content published by the attacker (for example, images and frames in the target's web site might be modified to be loaded from a source controlled by the attacker). In these cases, the attacker requires the necessary resources to host the replacement content.

## Consequences
- Scope: Integrity; Impact: Modify Data

## Related Weaknesses (CWE)
- CWE-345


---

# CAPEC-149: Explore for Predictable Temporary File Names

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/149.html  

## Description
An attacker explores a target to identify the names and locations of predictable temporary files for the purpose of launching further attacks against the target. This involves analyzing naming conventions and storage locations of the temporary files created by a target application. If an attacker can predict the names of temporary files they can use this information to mount other attacks, such as information gathering and symlink attacks.

## Related Attack Patterns
- ChildOf: CAPEC-497
- CanPrecede: CAPEC-155

## Prerequisites
- The targeted application must create names for temporary files using a predictable procedure, e.g. using sequentially increasing numbers.
- The attacker must be able to see the names of the files the target is creating.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Related Weaknesses (CWE)
- CWE-377


---

# CAPEC-15: Command Delimiters

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/15.html  

## Description
An attack of this type exploits a programs' vulnerabilities that allows an attacker's commands to be concatenated onto a legitimate command with the intent of targeting other resources such as the file system or database. The system that uses a filter or denylist input validation, as opposed to allowlist validation is vulnerable to an attacker who predicts delimiters (or combinations of delimiters) not present in the filter or denylist. As with other injection attacks, the attacker uses the command delimiter payload as an entry point to tunnel through the application and activate additional attacks through SQL queries, shell commands, network scanning, and so on.

## Related Attack Patterns
- ChildOf: CAPEC-137

## Prerequisites
- Software's input validation or filtering must not detect and block presence of additional malicious command.

## Skills Required
- [Medium] The attacker has to identify injection vector, identify the specific commands, and optionally collect the output, i.e. from an interactive session.

## Resources Required
- Ability to communicate synchronously or asynchronously with server. Optionally, ability to capture output directly through synchronous communication or other method such as FTP.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Design: Perform allowlist validation against a positive specification for command length, type, and parameters.
- Design: Limit program privileges, so if commands circumvent program input validation or filter routines then commands do not running under a privileged account
- Implementation: Perform input validation for all remote content.
- Implementation: Use type conversions such as JDBC prepared statements.

## Related Weaknesses (CWE)
- CWE-146
- CWE-77
- CWE-184
- CWE-78
- CWE-185
- CWE-93
- CWE-140
- CWE-157
- CWE-138
- CWE-154
- CWE-697


---

# CAPEC-150: Collect Data from Common Resource Locations

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/150.html  

## Description
An adversary exploits well-known locations for resources for the purposes of undermining the security of the target. In many, if not most systems, files and resources are organized in a default tree structure. This can be useful for adversaries because they often know where to look for resources or files that are necessary for attacks. Even when the precise location of a targeted resource may not be known, naming conventions may indicate a small area of the target machine's file tree where the resources are typically located. For example, configuration files are normally stored in the /etc director on Unix systems. Adversaries can take advantage of this to commit other types of attacks.

## Related Attack Patterns
- ChildOf: CAPEC-116

## Prerequisites
- The targeted applications must either expect files to be located at a specific location or, if the location of the files can be configured by the user, the user either failed to move the files from the default location or placed them in a conventional location for files of the given type.

## Resources Required
- None: No specialized resources are required to execute this type of attack. In some cases, the attacker need not even have direct access to the locations on the target computer where the targeted resources reside.

## Related Weaknesses (CWE)
- CWE-552
- CWE-1239
- CWE-1258
- CWE-1266
- CWE-1272
- CWE-1323
- CWE-1330


---

# CAPEC-151: Identity Spoofing

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/151.html  

## Description
Identity Spoofing refers to the action of assuming (i.e., taking on) the identity of some other entity (human or non-human) and then using that identity to accomplish a goal. An adversary may craft messages that appear to come from a different principle or use stolen / spoofed authentication credentials.

## Prerequisites
- The identity associated with the message or resource must be removable or modifiable in an undetectable way.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality, Integrity, Authentication, Access Control; Impact: Gain Privileges

## Mitigations
- Employ robust authentication processes (e.g., multi-factor authentication).

## Related Weaknesses (CWE)
- CWE-287


---

# CAPEC-153: Input Data Manipulation

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/153.html  

## Description
An attacker exploits a weakness in input validation by controlling the format, structure, and composition of data to an input-processing interface. By supplying input of a non-standard or unexpected form an attacker can adversely impact the security of the target.

## Prerequisites
- The target must accept user data for processing and the manner in which this data is processed must depend on some aspect of the format or flags that the attacker can control.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Related Weaknesses (CWE)
- CWE-20


---

# CAPEC-154: Resource Location Spoofing

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/154.html  

## Description
An adversary deceives an application or user and convinces them to request a resource from an unintended location. By spoofing the location, the adversary can cause an alternate resource to be used, often one that the adversary controls and can be used to help them achieve their malicious goals.

## Prerequisites
- None. All applications rely on file paths and therefore, in theory, they or their resources could be affected by this type of attack.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Monitor network activity to detect any anomalous or unauthorized communication exchanges.

## Related Weaknesses (CWE)
- CWE-451


---

# CAPEC-155: Screen Temporary Files for Sensitive Information

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/155.html  

## Description
An adversary exploits the temporary, insecure storage of information by monitoring the content of files used to store temp data during an application's routine execution flow. Many applications use temporary files to accelerate processing or to provide records of state across multiple executions of the application. Sometimes, however, these temporary files may end up storing sensitive information. By screening an application's temporary files, an adversary might be able to discover such sensitive information. For example, web browsers often cache content to accelerate subsequent lookups. If the content contains sensitive information then the adversary could recover this from the web cache.

## Related Attack Patterns
- ChildOf: CAPEC-150

## Prerequisites
- The target application must utilize temporary files and must fail to adequately secure them against other parties reading them.

## Resources Required
- Because some application may have a large number of temporary files and/or these temporary files may be very large, an adversary may need tools that help them quickly search these files for sensitive information. If the adversary can simply copy the files to another location and if the speed of the search is not important, the adversary can still perform the attack without any special resources.

## Related Weaknesses (CWE)
- CWE-377


---

# CAPEC-157: Sniffing Attacks

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/157.html  

## Description
In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient. Sniffing Attacks are similar to Adversary-In-The-Middle attacks (CAPEC-94), but are entirely passive. AiTM attacks are predominantly active and often alter the content of the communications themselves.

## Related Attack Patterns
- ChildOf: CAPEC-117
- CanPrecede: CAPEC-652

## Prerequisites
- The target data stream must be transmitted on a medium to which the adversary has access.

## Resources Required
- The adversary must be able to intercept the transmissions containing the data of interest. Depending on the medium of transmission and the path the data takes between the sender and recipient, the adversary may require special equipment and/or require that this equipment be placed in specific locations (e.g., a network sniffing tool)

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Encrypt sensitive information when transmitted on insecure mediums to prevent interception.

## Related Weaknesses (CWE)
- CWE-311


---

# CAPEC-158: Sniffing Network Traffic

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/158.html  

## Description
In this attack pattern, the adversary monitors network traffic between nodes of a public or multicast network in an attempt to capture sensitive information at the protocol level. Network sniffing applications can reveal TCP/IP, DNS, Ethernet, and other low-level network communication information. The adversary takes a passive role in this attack pattern and simply observes and analyzes the traffic. The adversary may precipitate or indirectly influence the content of the observed transaction, but is never the intended recipient of the target information.

## Related Attack Patterns
- ChildOf: CAPEC-157

## Prerequisites
- The target must be communicating on a network protocol visible by a network sniffing application.
- The adversary must obtain a logical position on the network from intercepting target network traffic is possible. Depending on the network topology, traffic sniffing may be simple or challenging. If both the target sender and target recipient are members of a single subnet, the adversary must also be on that subnet in order to see their traffic communication.

## Skills Required
- [Low] Adversaries can obtain and set up open-source network sniffing tools easily.

## Resources Required
- A tool with the capability of presenting network communication traffic (e.g., Wireshark, tcpdump, Cain and Abel, etc.).

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Obfuscate network traffic through encryption to prevent its readability by network sniffers.
- Employ appropriate levels of segmentation to your network in accordance with best practices.

## Related Weaknesses (CWE)
- CWE-311


---

# CAPEC-159: Redirect Access to Libraries

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/159.html  

## Description
An adversary exploits a weakness in the way an application searches for external libraries to manipulate the execution flow to point to an adversary supplied library or code base. This pattern of attack allows the adversary to compromise the application or server via the execution of unauthorized code. An application typically makes calls to functions that are a part of libraries external to the application. These libraries may be part of the operating system or they may be third party libraries. If an adversary can redirect an application's attempts to access these libraries to other libraries that the adversary supplies, the adversary will be able to force the targeted application to execute arbitrary code. This is especially dangerous if the targeted application has enhanced privileges. Access can be redirected through a number of techniques, including the use of symbolic links, search path modification, and relative path manipulation.

## Related Attack Patterns
- ChildOf: CAPEC-154
- CanPrecede: CAPEC-185

## Prerequisites
- The target must utilize external libraries and must fail to verify the integrity of these libraries before using them.

## Skills Required
- [Low] To modify the entries in the configuration file pointing to malicious libraries
- [Medium] To force symlink and timing issues for redirecting access to libraries
- [High] To reverse engineering the libraries and inject malicious code into the libraries

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Implementation: Restrict the permission to modify the entries in the configuration file.
- Implementation: Check the integrity of the dynamically linked libraries before use them.
- Implementation: Use obfuscation and other techniques to prevent reverse engineering the libraries.

## Related Weaknesses (CWE)
- CWE-706


---

# CAPEC-16: Dictionary-based Password Attack

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/16.html  

## Description
An attacker tries each of the words in a dictionary as passwords to gain access to the system via some user's account. If the password chosen by the user was a word within the dictionary, this attack will be successful (in the absence of other mitigations). This is a specific instance of the password brute forcing attack pattern. Dictionary Attacks differ from similar attacks such as Password Spraying (CAPEC-565) and Credential Stuffing (CAPEC-600), since they leverage unknown username/password combinations and don't care about inducing account lockouts.

## Related Attack Patterns
- ChildOf: CAPEC-49
- CanPrecede: CAPEC-600
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-560
- CanPrecede: CAPEC-561
- CanPrecede: CAPEC-653

## Prerequisites
- The system uses one factor password based authentication.
- The system does not have a sound password policy that is being enforced.
- The system does not implement an effective password throttling mechanism.

## Skills Required
- [Low] A variety of password cracking tools and dictionaries are available to launch this type of an attack.

## Resources Required
- A machine with sufficient resources for the job (e.g. CPU, RAM, HD). Applicable dictionaries are required. Also a password cracking tool or a custom script that leverages the dictionary database to launch the attack.

## Consequences
- Scope: Confidentiality, Access Control, Authentication; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Create a strong password policy and ensure that your system enforces this policy.
- Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-2.
- Leverage multi-factor authentication for all authentication services.

## Related Weaknesses (CWE)
- CWE-521
- CWE-262
- CWE-263
- CWE-654
- CWE-307
- CWE-308
- CWE-309


---

# CAPEC-160: Exploit Script-Based APIs

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/160.html  

## Description
Some APIs support scripting instructions as arguments. Methods that take scripted instructions (or references to scripted instructions) can be very flexible and powerful. However, if an attacker can specify the script that serves as input to these methods they can gain access to a great deal of functionality. For example, HTML pages support <script> tags that allow scripting languages to be embedded in the page and then interpreted by the receiving web browser. If the content provider is malicious, these scripts can compromise the client application. Some applications may even execute the scripts under their own identity (rather than the identity of the user providing the script) which can allow attackers to perform activities that would otherwise be denied to them.

## Related Attack Patterns
- ChildOf: CAPEC-113

## Prerequisites
- The target application must include the use of APIs that execute scripts.
- The target application must allow the attacker to provide some or all of the arguments to one of these script interpretation methods and must fail to adequately filter these arguments for dangerous or unwanted script commands.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Related Weaknesses (CWE)
- CWE-346


---

# CAPEC-161: Infrastructure Manipulation

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/161.html  

## Description
An attacker exploits characteristics of the infrastructure of a network entity in order to perpetrate attacks or information gathering on network objects or effect a change in the ordinary information flow between network objects. Most often, this involves manipulation of the routing of network messages so, instead of arriving at their proper destination, they are directed towards an entity of the attackers' choosing, usually a server controlled by the attacker. The victim is often unaware that their messages are not being processed correctly. For example, a targeted client may believe they are connecting to their own bank but, in fact, be connecting to a Pharming site controlled by the attacker which then collects the user's login information in order to hijack the actual bank account.

## Related Attack Patterns
- CanPrecede: CAPEC-664

## Prerequisites
- The targeted client must access the site via infrastructure that the attacker has co-opted and must fail to adequately verify that the communication channel is operating correctly (e.g. by verifying that they are, in fact, connected to the site they intended.)

## Resources Required
- The attacker must be able to corrupt the infrastructure used by the client. For some variants of this attack, the attacker must be able to stand up their own services that mimic the services the targeted client intends to use.

## Related Weaknesses (CWE)
- CWE-923


---

# CAPEC-162: Manipulating Hidden Fields

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/162.html  

## Description
An adversary exploits a weakness in the server's trust of client-side processing by modifying data on the client-side, such as price information, and then submitting this data to the server, which processes the modified data. For example, eShoplifting is a data manipulation attack against an on-line merchant during a purchasing transaction. The manipulation of price, discount or quantity fields in the transaction message allows the adversary to acquire items at a lower cost than the merchant intended. The adversary performs a normal purchasing transaction but edits hidden fields within the HTML form response that store price or other information to give themselves a better deal. The merchant then uses the modified pricing information in calculating the cost of the selected items.

## Related Attack Patterns
- ChildOf: CAPEC-77

## Prerequisites
- The targeted site must contain hidden fields to be modified.
- The targeted site must not validate the hidden fields with backend processing.

## Resources Required
- The adversary must have the ability to modify hidden fields by editing the HTTP response to the server.

## Related Weaknesses (CWE)
- CWE-602


---

# CAPEC-163: Spear Phishing

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/163.html  

## Description
An adversary targets a specific user or group with a Phishing (CAPEC-98) attack tailored to a category of users in order to have maximum relevance and deceptive capability. Spear Phishing is an enhanced version of the Phishing attack targeted to a specific user or group. The quality of the targeted email is usually enhanced by appearing to come from a known or trusted entity. If the email account of some trusted entity has been compromised the message may be digitally signed. The message will contain information specific to the targeted users that will enhance the probability that they will follow the URL to the compromised site. For example, the message may indicate knowledge of the targets employment, residence, interests, or other information that suggests familiarity. As soon as the user follows the instructions in the message, the attack proceeds as a standard Phishing attack.

## Related Attack Patterns
- ChildOf: CAPEC-98

## Prerequisites
- None. Any user can be targeted by a Spear Phishing attack.

## Skills Required
- [Medium] Spear phishing attacks require specific knowledge of the victims being targeted, such as which bank is being used by the victims, or websites they commonly log into (Google, Facebook, etc).

## Resources Required
- An adversay must have the ability communicate their phishing scheme to the victims (via email, instance message, etc.), as well as a website or other platform for victims to enter personal information into.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Do not follow any links that you receive within your e-mails and certainly do not input any login credentials on the page that they take you too. Instead, call your Bank, PayPal, eBay, etc., and inquire about the problem. A safe practice would also be to type the URL of your bank in the browser directly and only then log in. Also, never reply to any e-mails that ask you to provide sensitive information of any kind.

## Related Weaknesses (CWE)
- CWE-451


---

# CAPEC-164: Mobile Phishing

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/164.html  

## Description
An adversary targets mobile phone users with a phishing attack for the purpose of soliciting account passwords or sensitive information from the user. Mobile Phishing is a variation of the Phishing social engineering technique where the attack is initiated via a text or SMS message, rather than email. The user is enticed to provide information or visit a compromised web site via this message. Apart from the manner in which the attack is initiated, the attack proceeds as a standard Phishing attack.

## Related Attack Patterns
- ChildOf: CAPEC-98

## Prerequisites
- An adversary needs mobile phone numbers to initiate contact with the victim.
- An adversary needs to correctly guess the entity with which the victim does business and impersonate it. Most of the time phishers just use the most popular banks/services and send out their "hooks" to many potential victims.
- An adversary needs to have a sufficiently compelling call to action to prompt the user to take action.
- The replicated website needs to look extremely similar to the original website and the URL used to get to that website needs to look like the real URL of the said business entity.

## Skills Required
- [Medium] Basic knowledge about websites: obtaining them, designing and implementing them, etc.

## Resources Required
- Either mobile phone or access to a web resource that allows text messages to be sent to mobile phones. Resources needed for regular Phishing attack.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Do not follow any links that you receive within text messages and do not input any login credentials on the page that they take you too. Instead, call your Bank, PayPal, eBay, etc., and inquire about the problem. Safe practices also include leveraging the entity's mobile application or directly typing the entity's URL in the browser and only then logging in. Never reply to any text messages that ask you to provide sensitive information of any kind.

## Related Weaknesses (CWE)
- CWE-451


---

# CAPEC-165: File Manipulation

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/165.html  

## Description
An attacker modifies file contents or attributes (such as extensions or names) of files in a manner to cause incorrect processing by an application. Attackers use this class of attacks to cause applications to enter unstable states, overwrite or expose sensitive information, and even execute arbitrary code with the application's privileges. This class of attacks differs from attacks on configuration information (even if file-based) in that file manipulation causes the file processing to result in non-standard behaviors, such as buffer overflows or use of the incorrect interpreter. Configuration attacks rely on the application interpreting files correctly in order to insert harmful configuration information. Likewise, resource location attacks rely on controlling an application's ability to locate files, whereas File Manipulation attacks do not require the application to look in a non-default location, although the two classes of attacks are often combined.

## Prerequisites
- The target must use the affected file without verifying its integrity.

## Resources Required
- None: No specialized resources are required to execute this type of attack. In some cases, tools can be used to better control the response of the targeted application to the modified file.


---

# CAPEC-166: Force the System to Reset Values

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/166.html  

## Description
An attacker forces the target into a previous state in order to leverage potential weaknesses in the target dependent upon a prior configuration or state-dependent factors. Even in cases where an attacker may not be able to directly control the configuration of the targeted application, they may be able to reset the configuration to a prior state since many applications implement reset functions.

## Related Attack Patterns
- ChildOf: CAPEC-161

## Prerequisites
- The targeted application must have a reset function that returns the configuration of the application to an earlier state.
- The reset functionality must be inadequately protected against use.

## Resources Required
- None: No specialized resources are required to execute this type of attack. In some cases, the attacker may need special client applications in order to execute the reset functionality.

## Related Weaknesses (CWE)
- CWE-306
- CWE-1221
- CWE-1232


---

# CAPEC-167: White Box Reverse Engineering

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/167.html  

## Description
An attacker discovers the structure, function, and composition of a type of computer software through white box analysis techniques. White box techniques involve methods which can be applied to a piece of software when an executable or some other compiled object can be directly subjected to analysis, revealing at least a portion of its machine instructions that can be observed upon execution.

## Related Attack Patterns
- ChildOf: CAPEC-188

## Prerequisites
- Direct access to the object or software.

## Resources Required
- Reverse engineering of software requires varying tools and methods that enable the decompiling of executable or other compiled objects.

## Related Weaknesses (CWE)
- CWE-1323


---

# CAPEC-168: Windows ::DATA Alternate Data Stream

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/168.html  

## Description
An attacker exploits the functionality of Microsoft NTFS Alternate Data Streams (ADS) to undermine system security. ADS allows multiple "files" to be stored in one directory entry referenced as filename:streamname. One or more alternate data streams may be stored in any file or directory. Normal Microsoft utilities do not show the presence of an ADS stream attached to a file. The additional space for the ADS is not recorded in the displayed file size. The additional space for ADS is accounted for in the used space on the volume. An ADS can be any type of file. ADS are copied by standard Microsoft utilities between NTFS volumes. ADS can be used by an attacker or intruder to hide tools, scripts, and data from detection by normal system utilities. Many anti-virus programs do not check for or scan ADS. Windows Vista does have a switch (-R) on the command line DIR command that will display alternate streams.

## Related Attack Patterns
- ChildOf: CAPEC-636

## Prerequisites
- The target must be running the Microsoft NTFS file system.

## Resources Required
- The attacker must have command line or programmatic access to the target's files system with write/read permissions.

## Mitigations
- Design: Use FAT file systems which do not support Alternate Data Streams.
- Implementation: Use Vista dir with the -R switch or utility to find Alternate Data Streams and take appropriate action with those discovered.
- Implementation: Use products that are Alternate Data Stream aware for virus scanning and system security operations.

## Related Weaknesses (CWE)
- CWE-212
- CWE-69


---

# CAPEC-169: Footprinting

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very Low  
**Reference:** https://capec.mitre.org/data/definitions/169.html  

## Description
An adversary engages in probing and exploration activities to identify constituents and properties of the target.

## Prerequisites
- An application must publicize identifiable information about the system or application through voluntary or involuntary means. Certain identification details of information systems are visible on communication networks (e.g., if an adversary uses a sniffer to inspect the traffic) due to their inherent structure and protocol standards. Any system or network that can be detected can be footprinted. However, some configuration choices may limit the useful information that can be collected during a footprinting attack.

## Skills Required
- [Low] The adversary knows how to send HTTP request, run the scan tool.

## Resources Required
- The adversary requires a variety of tools to collect information about the target. These include port/network scanners and tools to analyze responses from applications to determine version and configuration information. Footprinting a system adequately may also take a few days if the attacker wishes the footprinting attempt to go undetected.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Keep patches up to date by installing weekly or daily if possible.
- Shut down unnecessary services/ports.
- Change default passwords by choosing strong passwords.
- Curtail unexpected input.
- Encrypt and password-protect sensitive data.
- Avoid including information that has the potential to identify and compromise your organization's security such as access to business plans, formulas, and proprietary documents.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-17: Using Malicious Files

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/17.html  

## Description
An attack of this type exploits a system's configuration that allows an adversary to either directly access an executable file, for example through shell access; or in a possible worst case allows an adversary to upload a file and then execute it. Web servers, ftp servers, and message oriented middleware systems which have many integration points are particularly vulnerable, because both the programmers and the administrators must be in synch regarding the interfaces and the correct privileges for each interface.

## Related Attack Patterns
- ChildOf: CAPEC-122
- CanPrecede: CAPEC-233

## Prerequisites
- System's configuration must allow an attacker to directly access executable files or upload files to execute. This means that any access control system that is supposed to mediate communications between the subject and the object is set incorrectly or assumes a benign environment.

## Skills Required
- [Low] To identify and execute against an over-privileged system interface

## Resources Required
- Ability to communicate synchronously or asynchronously with server that publishes an over-privileged directory, program, or interface. Optionally, ability to capture output directly through synchronous communication or other method such as FTP.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Design: Enforce principle of least privilege
- Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.
- Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.

## Related Weaknesses (CWE)
- CWE-732
- CWE-285
- CWE-272
- CWE-59
- CWE-282
- CWE-270
- CWE-693


---

# CAPEC-170: Web Application Fingerprinting

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/170.html  

## Description
An attacker sends a series of probes to a web application in order to elicit version-dependent and type-dependent behavior that assists in identifying the target. An attacker could learn information such as software versions, error pages, and response headers, variations in implementations of the HTTP protocol, directory structures, and other similar information about the targeted service. This information can then be used by an attacker to formulate a targeted attack plan. While web application fingerprinting is not intended to be damaging (although certain activities, such as network scans, can sometimes cause disruptions to vulnerable applications inadvertently) it may often pave the way for more damaging attacks.

## Related Attack Patterns
- ChildOf: CAPEC-541

## Prerequisites
- Any web application can be fingerprinted. However, some configuration choices can limit the useful information an attacker may collect during a fingerprinting attack.

## Skills Required
- [Low] Attacker knows how to send HTTP request, SQL query to a web application.

## Resources Required
- While simple fingerprinting can be accomplished with only a web browser, for more thorough fingerprinting an attacker requires a variety of tools to collect information about the target. These tools might include protocol analyzers, web-site crawlers, and fuzzing tools. Footprinting a service adequately may also take a few days if the attacker wishes the footprinting attempt to go undetected.

## Consequences
- Scope: Confidentiality; Impact: Other

## Mitigations
- Implementation: Obfuscate server fields of HTTP response.
- Implementation: Hide inner ordering of HTTP response header.
- Implementation: Customizing HTTP error codes such as 404 or 500.
- Implementation: Hide URL file extension.
- Implementation: Hide HTTP response header software information filed.
- Implementation: Hide cookie's software information filed.
- Implementation: Appropriately deal with error messages.
- Implementation: Obfuscate database type in Database API's error message.

## Related Weaknesses (CWE)
- CWE-497


---

# CAPEC-171: DEPRECATED: Variable Manipulation

**Abstraction:** Meta  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/171.html  

## Description
This attack pattern has been deprecated as it is a duplicate of the existing attack pattern "CAPEC-77 : Manipulating User-Controlled Variables". Please refer to this other CAPEC going forward.


---

# CAPEC-173: Action Spoofing

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/173.html  

## Description
An adversary is able to disguise one action for another and therefore trick a user into initiating one type of action when they intend to initiate a different action. For example, a user might be led to believe that clicking a button will submit a query, but in fact it downloads software. Adversaries may perform this attack through social means, such as by simply convincing a victim to perform the action or relying on a user's natural inclination to do so, or through technical means, such as a clickjacking attack where a user sees one interface but is actually interacting with a second, invisible, interface.

## Prerequisites
- The adversary must convince the victim into performing the decoy action.
- The adversary must have the means to control a user's interface to present them with a decoy action as well as the actual malicious action. Simple versions of this attack can be performed using web pages requiring only that the adversary be able to host (or control) content that the user visits.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- Avoid interacting with suspicious sites or clicking suspicious links.
- An organization should provide regular, robust cybersecurity training to its employees.

## Related Weaknesses (CWE)
- CWE-451


---

# CAPEC-174: Flash Parameter Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/174.html  

## Description
An adversary takes advantage of improper data validation to inject malicious global parameters into a Flash file embedded within an HTML document. Flash files can leverage user-submitted data to configure the Flash document and access the embedding HTML document.

## Related Attack Patterns
- ChildOf: CAPEC-182
- CanAlsoBe: CAPEC-460
- CanPrecede: CAPEC-63
- CanPrecede: CAPEC-178

## Skills Required
- [Medium] The adversary need inject values into the global parameters to the Flash file and understand the parent HTML document DOM structure. The adversary needs to be smart enough to convince the victim to click on their crafted link.

## Resources Required
- The adversary must convince the victim to click their crafted link.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- User input must be sanitized according to context before reflected back to the user. The JavaScript function 'encodeURI' is not always sufficient for sanitizing input intended for global Flash parameters. Extreme caution should be taken when saving user input in Flash cookies. In such cases the Flash file itself will need to be fixed and recompiled, changing the name of the local shared objects (Flash cookies).

## Related Weaknesses (CWE)
- CWE-88


---

# CAPEC-175: Code Inclusion

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/175.html  

## Description
An adversary exploits a weakness on the target to force arbitrary code to be retrieved locally or from a remote location and executed. This differs from code injection in that code injection involves the direct inclusion of code while code inclusion involves the addition or replacement of a reference to a code file, which is subsequently loaded by the target and used as part of the code of some application.

## Prerequisites
- The target application must include external code/libraries that are executed when the application runs and the adversary must be able to influence the specific files that get included.
- The victim must run the targeted application, possibly using the crafted parameters that the adversary uses to identify the code to include.

## Resources Required
- The adversary may need the capability to host code modules if they wish their own code files to be included.

## Related Weaknesses (CWE)
- CWE-829


---

# CAPEC-176: Configuration/Environment Manipulation

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/176.html  

## Description
An attacker manipulates files or settings external to a target application which affect the behavior of that application. For example, many applications use external configuration files and libraries - modification of these entities or otherwise affecting the application's ability to use them would constitute a configuration/environment manipulation attack.

## Prerequisites
- The target application must consult external files or configuration controls to control its execution. All but the very simplest applications meet this requirement.

## Resources Required
- The attacker must have the access necessary to affect the files or other environment items the targeted application uses for its operations.

## Related Weaknesses (CWE)
- CWE-15
- CWE-1233
- CWE-1234
- CWE-1304
- CWE-1328


---

# CAPEC-177: Create files with the same name as files protected with a higher classification

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/177.html  

## Description
An attacker exploits file location algorithms in an operating system or application by creating a file with the same name as a protected or privileged file. The attacker could manipulate the system if the attacker-created file is trusted by the operating system or an application component that attempts to load the original file. Applications often load or include external files, such as libraries or configuration files. These files should be protected against malicious manipulation. However, if the application only uses the name of the file when locating it, an attacker may be able to create a file with the same name and place it in a directory that the application will search before the directory with the legitimate file is searched. Because the attackers' file is discovered first, it would be used by the target application. This attack can be extremely destructive if the referenced file is executable and/or is granted special privileges based solely on having a particular name.

## Related Attack Patterns
- ChildOf: CAPEC-17

## Prerequisites
- The target application must include external files. Most non-trivial applications meet this criterion.
- The target application does not verify that a located file is the one it was looking for through means other than the name. Many applications fail to perform checks of this type.
- The directories the target application searches to find the included file include directories writable by the attacker which are searched before the protected directory containing the actual files. It is much less common for applications to meet this criterion, but if an attacker can manipulate the application's search path (possibly by controlling environmental variables) then they can force this criterion to be met.

## Resources Required
- The attacker must have sufficient access to place an arbitrarily named file somewhere early in the application's search path.

## Related Weaknesses (CWE)
- CWE-706


---

# CAPEC-178: Cross-Site Flashing

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/178.html  

## Description
An attacker is able to trick the victim into executing a Flash document that passes commands or calls to a Flash player browser plugin, allowing the attacker to exploit native Flash functionality in the client browser. This attack pattern occurs where an attacker can provide a crafted link to a Flash document (SWF file) which, when followed, will cause additional malicious instructions to be executed. The attacker does not need to serve or control the Flash document. The attack takes advantage of the fact that Flash files can reference external URLs. If variables that serve as URLs that the Flash application references can be controlled through parameters, then by creating a link that includes values for those parameters, an attacker can cause arbitrary content to be referenced and possibly executed by the targeted Flash application.

## Related Attack Patterns
- ChildOf: CAPEC-182

## Prerequisites
- The targeted Flash application must reference external URLs and the locations thus referenced must be controllable through parameters. The Flash application must fail to sanitize such parameters against malicious manipulation. The victim must follow a crafted link created by the attacker.

## Skills Required
- [Medium] knowledge of Flash internals, parameters and remote referencing.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Implementation: Only allow known URL to be included as remote flash movies in a flash application
- Configuration: Properly configure the crossdomain.xml file to only include the known domains that should host remote flash movies.

## Related Weaknesses (CWE)
- CWE-601


---

# CAPEC-179: Calling Micro-Services Directly

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/179.html  

## Description
An attacker is able to discover and query Micro-services at a web location and thereby expose the Micro-services to further exploitation by gathering information about their implementation and function. Micro-services in web pages allow portions of a page to connect to the server and update content without needing to cause the entire page to update. This allows user activity to change portions of the page more quickly without causing disruptions elsewhere.

## Related Attack Patterns
- ChildOf: CAPEC-554

## Prerequisites
- The target site must use micro-services that interact with the server and one or more of these micro-services must be vulnerable to some other attack pattern.

## Resources Required
- The attacker usually needs to be able to invoke micro-services directly in order to control the parameters that are used in their attack. The attacker may require other resources depending on the nature of the flaw in the targeted micro-service.


---

# CAPEC-18: XSS Targeting Non-Script Elements

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/18.html  

## Description
This attack is a form of Cross-Site Scripting (XSS) where malicious scripts are embedded in elements that are not expected to host scripts such as image tags (<img>), comments in XML documents (< !-CDATA->), etc. These tags may not be subject to the same input validation, output validation, and other content filtering and checking routines, so this can create an opportunity for an adversary to tunnel through the application's elements and launch a XSS attack through other elements. As with all remote attacks, it is important to differentiate the ability to launch an attack (such as probing an internal network for unpatched servers) and the ability of the remote adversary to collect and interpret the output of said attack.

## Related Attack Patterns
- ChildOf: CAPEC-591
- ChildOf: CAPEC-592
- ChildOf: CAPEC-588

## Prerequisites
- The target client software must allow the execution of scripts generated by remote hosts.

## Skills Required
- [Low] To achieve a redirection and use of less trusted source, an adversary can simply edit content such as XML payload or HTML files that are sent to client machine.
- [High] Exploiting a client side vulnerability to inject malicious scripts into the browser's executable process.

## Resources Required
- Ability to include malicious script in document, e.g. HTML file, or XML document. Ability to deploy a custom hostile service for access by targeted clients. Ability to communicate synchronously or asynchronously with client machine

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- In addition to the traditional input fields, all other user controllable inputs, such as image tags within messages or the likes, must also be subjected to input validation. Such validation should ensure that content that can be potentially interpreted as script by the browser is appropriately filtered.
- All output displayed to clients must be properly escaped. Escaping ensures that the browser interprets special scripting characters literally and not as script to be executed.

## Related Weaknesses (CWE)
- CWE-80


---

# CAPEC-180: Exploiting Incorrectly Configured Access Control Security Levels

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/180.html  

## Description
An attacker exploits a weakness in the configuration of access controls and is able to bypass the intended protection that these measures guard against and thereby obtain unauthorized access to the system or network. Sensitive functionality should always be protected with access controls. However configuring all but the most trivial access control systems can be very complicated and there are many opportunities for mistakes. If an attacker can learn of incorrectly configured access security settings, they may be able to exploit this in an attack.

## Related Attack Patterns
- ChildOf: CAPEC-122
- CanPrecede: CAPEC-17

## Prerequisites
- The target must apply access controls, but incorrectly configure them. However, not all incorrect configurations can be exploited by an attacker. If the incorrect configuration applies too little security to some functionality, then the attacker may be able to exploit it if the access control would be the only thing preventing an attacker's access and it no longer does so. If the incorrect configuration applies too much security, it must prevent legitimate activity and the attacker must be able to force others to require this activity..

## Skills Required
- [Low] In order to discover unrestricted resources, the attacker does not need special tools or skills. They only have to observe the resources or access mechanisms invoked as each action is performed and then try and access those access mechanisms directly.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Authorization; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Design: Configure the access control correctly.

## Related Weaknesses (CWE)
- CWE-732
- CWE-1190
- CWE-1191
- CWE-1193
- CWE-1220
- CWE-1268
- CWE-1280
- CWE-1297
- CWE-1311
- CWE-1315
- CWE-1318
- CWE-1320
- CWE-1321


---

# CAPEC-181: Flash File Overlay

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/181.html  

## Description
An attacker creates a transparent overlay using flash in order to intercept user actions for the purpose of performing a clickjacking attack. In this technique, the Flash file provides a transparent overlay over HTML content. Because the Flash application is on top of the content, user actions, such as clicks, are caught by the Flash application rather than the underlying HTML. The action is then interpreted by the overlay to perform the actions the attacker wishes.

## Related Attack Patterns
- ChildOf: CAPEC-103

## Prerequisites
- The victim must be tricked into navigating to the attackers' decoy site and performing the actions on the decoy page.
- The victim's browser must support invisible Flash overlays.

## Resources Required
- The attacker must be able to force the Flash overlay over the decoy content.

## Related Weaknesses (CWE)
- CWE-1021


---

# CAPEC-182: Flash Injection

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/182.html  

## Description
An attacker tricks a victim to execute malicious flash content that executes commands or makes flash calls specified by the attacker. One example of this attack is cross-site flashing, an attacker controlled parameter to a reference call loads from content specified by the attacker.

## Related Attack Patterns
- ChildOf: CAPEC-137
- CanAlsoBe: CAPEC-248

## Prerequisites
- The target must be capable of running Flash applications. In some cases, the victim must follow an attacker-supplied link.

## Skills Required
- [Medium] The attacker needs to have knowledge of Flash, especially how to insert content the executes commands.

## Resources Required
- None: No specialized resources are required to execute this type of attack. The attacker may need to be able to serve the injected Flash content.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Implementation: remove sensitive information such as user name and password in the SWF file.
- Implementation: use validation on both client and server side.
- Implementation: remove debug information.
- Implementation: use SSL when loading external data
- Implementation: use crossdomain.xml file to allow the application domain to load stuff or the SWF file called by other domain.

## Related Weaknesses (CWE)
- CWE-20
- CWE-184
- CWE-697


---

# CAPEC-183: IMAP/SMTP Command Injection

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/183.html  

## Description
An adversary exploits weaknesses in input validation on web-mail servers to execute commands on the IMAP/SMTP server. Web-mail servers often sit between the Internet and the IMAP or SMTP mail server. User requests are received by the web-mail servers which then query the back-end mail server for the requested information and return this response to the user. In an IMAP/SMTP command injection attack, mail-server commands are embedded in parts of the request sent to the web-mail server. If the web-mail server fails to adequately sanitize these requests, these commands are then sent to the back-end mail server when it is queried by the web-mail server, where the commands are then executed. This attack can be especially dangerous since administrators may assume that the back-end server is protected against direct Internet access and therefore may not secure it adequately against the execution of malicious commands.

## Related Attack Patterns
- ChildOf: CAPEC-248

## Prerequisites
- The target environment must consist of a web-mail server that the attacker can query and a back-end mail server. The back-end mail server need not be directly accessible to the attacker.
- The web-mail server must fail to adequately sanitize fields received from users and passed on to the back-end mail server.
- The back-end mail server must not be adequately secured against receiving malicious commands from the web-mail server.

## Resources Required
- None: No specialized resources are required to execute this type of attack. However, in most cases, the attacker will need to be a recognized user of the web-mail server.

## Related Weaknesses (CWE)
- CWE-77


---

# CAPEC-184: Software Integrity Attack

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/184.html  

## Description
An attacker initiates a series of events designed to cause a user, program, server, or device to perform actions which undermine the integrity of software code, device data structures, or device firmware, achieving the modification of the target's integrity to achieve an insecure state.

## Skills Required
- [Medium] Manual or user-assisted attacks require deceptive mechanisms to trick the user into clicking a link or downloading and installing software. Automated update attacks require the attacker to host a payload and then trigger the installation of the payload code.

## Resources Required
- Software Integrity Attacks are usually a late stage focus of attack activity which depends upon the success of a chain of prior events. The resources required to perform the attack vary with respect to the overall attack strategy, existing countermeasures which must be bypassed, and the success of early phase attack vectors.

## Related Weaknesses (CWE)
- CWE-494


---

# CAPEC-185: Malicious Software Download

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/185.html  

## Description
An attacker uses deceptive methods to cause a user or an automated process to download and install dangerous code that originates from an attacker controlled source. There are several variations to this strategy of attack.

## Related Attack Patterns
- ChildOf: CAPEC-184
- CanPrecede: CAPEC-662

## Related Weaknesses (CWE)
- CWE-494


---

# CAPEC-186: Malicious Software Update

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/186.html  

## Description
An adversary uses deceptive methods to cause a user or an automated process to download and install dangerous code believed to be a valid update that originates from an adversary controlled source.

## Related Attack Patterns
- ChildOf: CAPEC-184
- CanFollow: CAPEC-98

## Skills Required
- [High] This attack requires advanced cyber capabilities

## Resources Required
- Manual or user-assisted attacks require deceptive mechanisms to trick the user into clicking a link or downloading and installing software. Automated update attacks require the adversary to host a payload and then trigger the installation of the payload code.

## Consequences
- Scope: Access Control, Availability, Confidentiality; Impact: Execute Unauthorized Commands

## Mitigations
- Validate software updates before installing.

## Related Weaknesses (CWE)
- CWE-494


---

# CAPEC-187: Malicious Automated Software Update via Redirection

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/187.html  

## Description
An attacker exploits two layers of weaknesses in server or client software for automated update mechanisms to undermine the integrity of the target code-base. The first weakness involves a failure to properly authenticate a server as a source of update or patch content. This type of weakness typically results from authentication mechanisms which can be defeated, allowing a hostile server to satisfy the criteria that establish a trust relationship. The second weakness is a systemic failure to validate the identity and integrity of code downloaded from a remote location, hence the inability to distinguish malicious code from a legitimate update.

## Related Attack Patterns
- ChildOf: CAPEC-186

## Consequences
- Scope: Access Control, Availability, Confidentiality; Impact: Execute Unauthorized Commands

## Related Weaknesses (CWE)
- CWE-494


---

# CAPEC-188: Reverse Engineering

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/188.html  

## Description
An adversary discovers the structure, function, and composition of an object, resource, or system by using a variety of analysis techniques to effectively determine how the analyzed entity was constructed or operates. The goal of reverse engineering is often to duplicate the function, or a part of the function, of an object in order to duplicate or "back engineer" some aspect of its functioning. Reverse engineering techniques can be applied to mechanical objects, electronic devices, or software, although the methodology and techniques involved in each type of analysis differ widely.

## Prerequisites
- Access to targeted system, resources, and information.

## Skills Required
- [High] Understanding of low level programming languages or technologies can be very helpful. For example, when reverse engineering a binary file, an understanding of assembly languages can help to determine the purpose and inner-workings of the code. Another example is reverse engineering an application that relies on networking. Here, an understanding networking protocols can provide insight into application details.

## Resources Required
- The technical resources necessary to engage in reverse engineering differ in accordance with the type of object, resource, or system being analyzed.

## Mitigations
- Employ code obfuscation techniques to prevent the adversary from reverse engineering the targeted entity.

## Related Weaknesses (CWE)
- CWE-1278


---

# CAPEC-189: Black Box Reverse Engineering

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/189.html  

## Description
An adversary discovers the structure, function, and composition of a type of computer software through black box analysis techniques. 'Black Box' methods involve interacting with the software indirectly, in the absence of direct access to the executable object. Such analysis typically involves interacting with the software at the boundaries of where the software interfaces with a larger execution environment, such as input-output vectors, libraries, or APIs. Black Box Reverse Engineering also refers to gathering physical side effects of a hardware device, such as electromagnetic radiation or sounds.

## Related Attack Patterns
- ChildOf: CAPEC-188

## Resources Required
- Black box methods require (at minimum) the ability to interact with the functional boundaries where the software communicates with a larger processing environment, such as inter-process communication on a host operating system, or via networking protocols.

## Related Weaknesses (CWE)
- CWE-203
- CWE-1255
- CWE-1300


---

# CAPEC-19: Embedding Scripts within Scripts

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/19.html  

## Description
An adversary leverages the capability to execute their own script by embedding it within other scripts that the target software is likely to execute due to programs' vulnerabilities that are brought on by allowing remote hosts to execute scripts.

## Related Attack Patterns
- ChildOf: CAPEC-242

## Prerequisites
- Target software must be able to execute scripts, and also grant the adversary privilege to write/upload scripts.

## Skills Required
- [Low] To load malicious script into open, e.g. world writable directory
- [Medium] Executing remote scripts on host and collecting output

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Use browser technologies that do not allow client side scripting.
- Utilize strict type, character, and encoding enforcement.
- Server side developers should not proxy content via XHR or other means. If a HTTP proxy for remote content is setup on the server side, the client's browser has no way of discerning where the data is originating from.
- Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Perform input validation for all remote content.
- Perform output validation for all remote content.
- Disable scripting languages such as JavaScript in browser
- Session tokens for specific host
- Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.
- Privileges are constrained, if a script is loaded, ensure system runs in chroot jail or other limited authority mode

## Related Weaknesses (CWE)
- CWE-284


---

# CAPEC-190: Reverse Engineer an Executable to Expose Assumed Hidden Functionality

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/190.html  

## Description
An attacker analyzes a binary file or executable for the purpose of discovering the structure, function, and possibly source-code of the file by using a variety of analysis techniques to effectively determine how the software functions and operates. This type of analysis is also referred to as Reverse Code Engineering, as techniques exist for extracting source code from an executable. Several techniques are often employed for this purpose, both black box and white box. The use of computer bus analyzers and packet sniffers allows the binary to be studied at a level of interactions with its computing environment, such as a host OS, inter-process communication, and/or network communication. This type of analysis falls into the 'black box' category because it involves behavioral analysis of the software without reference to source code, object code, or protocol specifications.

## Related Attack Patterns
- ChildOf: CAPEC-167

## Resources Required
- Access to the target file such that it can be analyzed with the appropriate tools. A range of tools suitable for analyzing an executable or its operations

## Related Weaknesses (CWE)
- CWE-912


---

# CAPEC-191: Read Sensitive Constants Within an Executable

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/191.html  

## Description
An adversary engages in activities to discover any sensitive constants present within the compiled code of an executable. These constants may include literal ASCII strings within the file itself, or possibly strings hard-coded into particular routines that can be revealed by code refactoring methods including static and dynamic analysis.

## Related Attack Patterns
- ChildOf: CAPEC-167

## Prerequisites
- Access to a binary or executable such that it can be analyzed by various utilities.

## Resources Required
- Binary analysis programs such as 'strings' or 'grep', or hex editors.

## Related Weaknesses (CWE)
- CWE-798


---

# CAPEC-192: Protocol Analysis

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/192.html  

## Description
An adversary engages in activities to decipher and/or decode protocol information for a network or application communication protocol used for transmitting information between interconnected nodes or systems on a packet-switched data network. While this type of analysis involves the analysis of a networking protocol inherently, it does not require the presence of an actual or physical network.

## Prerequisites
- Access to a binary executable.
- The ability to observe and interact with a communication channel between communicating processes.

## Skills Required
- [High] Knowlegde of the Open Systems Interconnection model (OSI model), and famililarity with Wireshark or some other packet analyzer.

## Resources Required
- Depending on the type of analysis, a variety of tools might be required, such as static code and/or dynamic analysis tools. Alternatively, the effort might require debugging programs such as ollydbg, SoftICE, or disassemblers like IDA Pro. In some instances, packet sniffing or packet analyzing programs such as TCP dump or Wireshark are necessary. Lastly, specific protocol analysis might require tools such as PDB (Protocol Debug), or packet injection tools like pcap or Nemesis.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Related Weaknesses (CWE)
- CWE-326


---

# CAPEC-193: PHP Remote File Inclusion

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/193.html  

## Description
In this pattern the adversary is able to load and execute arbitrary code remotely available from the application. This is usually accomplished through an insecurely configured PHP runtime environment and an improperly sanitized "include" or "require" call, which the user can then control to point to any web-accessible file. This allows adversaries to hijack the targeted application and force it to execute their own instructions.

## Related Attack Patterns
- ChildOf: CAPEC-253

## Prerequisites
- Target application server must allow remote files to be included in the "require", "include", etc. PHP directives
- The adversary must have the ability to make HTTP requests to the target web application.

## Skills Required
- [Low] To inject the malicious payload in a web page
- [Medium] To bypass filters in the application

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Implementation: Perform input validation for all remote content, including remote and user-generated content
- Implementation: Only allow known files to be included (allowlist)
- Implementation: Make use of indirect references passed in URL parameters instead of file names
- Configuration: Ensure that remote scripts cannot be include in the "include" or "require" PHP directives

## Related Weaknesses (CWE)
- CWE-98
- CWE-80


---

# CAPEC-194: Fake the Source of Data

**Abstraction:** Standard  
**Status:** Stable  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/194.html  

## Description
An adversary takes advantage of improper authentication to provide data or services under a falsified identity. The purpose of using the falsified identity may be to prevent traceability of the provided data or to assume the rights granted to another individual. One of the simplest forms of this attack would be the creation of an email message with a modified "From" field in order to appear that the message was sent from someone other than the actual sender. The root of the attack (in this case the email system) fails to properly authenticate the source and this results in the reader incorrectly performing the instructed action. Results of the attack vary depending on the details of the attack, but common results include privilege escalation, obfuscation of other attacks, and data corruption/manipulation.

## Related Attack Patterns
- ChildOf: CAPEC-151
- CanPrecede: CAPEC-657
- CanPrecede: CAPEC-667

## Prerequisites
- This attack is only applicable when a vulnerable entity associates data or services with an identity. Without such an association, there would be no reason to fake the source.

## Resources Required
- Resources required vary depending on the nature of the attack. Possible tools needed by an attacker could include tools to create custom network packets, specific client software, and tools to capture network traffic. Many variants of this attack require no attacker resources, however.

## Consequences
- Scope: Integrity; Impact: Alter Execution Logic
- Scope: Integrity; Impact: Gain Privileges
- Scope: Integrity; Impact: Hide Activities

## Related Weaknesses (CWE)
- CWE-287


---

# CAPEC-195: Principal Spoof

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/195.html  

## Description
A Principal Spoof is a form of Identity Spoofing where an adversary pretends to be some other person in an interaction. This is often accomplished by crafting a message (either written, verbal, or visual) that appears to come from a person other than the adversary. Phishing and Pharming attacks often attempt to do this so that their attempts to gather sensitive information appear to come from a legitimate source. A Principal Spoof does not use stolen or spoofed authentication credentials, instead relying on the appearance and content of the message to reflect identity.

## Related Attack Patterns
- ChildOf: CAPEC-151

## Prerequisites
- The target must associate data or activities with a person's identity and the adversary must be able to modify this identity without detection.

## Resources Required
- None: No specialized resources are required to execute this type of attack.


---

# CAPEC-196: Session Credential Falsification through Forging

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/196.html  

## Description
An attacker creates a false but functional session credential in order to gain or usurp access to a service. Session credentials allow users to identify themselves to a service after an initial authentication without needing to resend the authentication information (usually a username and password) with every message. If an attacker is able to forge valid session credentials they may be able to bypass authentication or piggy-back off some other authenticated user's session. This attack differs from Reuse of Session IDs and Session Sidejacking attacks in that in the latter attacks an attacker uses a previous or existing credential without modification while, in a forging attack, the attacker must create their own credential, although it may be based on previously observed credentials.

## Related Attack Patterns
- CanPrecede: CAPEC-384
- CanPrecede: CAPEC-61
- ChildOf: CAPEC-21

## Prerequisites
- The targeted application must use session credentials to identify legitimate users. Session identifiers that remains unchanged when the privilege levels change. Predictable session identifiers.

## Skills Required
- [Medium] Forge the session credential and reply the request.

## Resources Required
- Attackers may require tools to craft messages containing their forged credentials, and ability to send HTTP request to a web application.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Implementation: Use session IDs that are difficult to guess or brute-force: One way for the attackers to obtain valid session IDs is by brute-forcing or guessing them. By choosing session identifiers that are sufficiently random, brute-forcing or guessing becomes very difficult.
- Implementation: Regenerate and destroy session identifiers when there is a change in the level of privilege: This ensures that even though a potential victim may have followed a link with a fixated identifier, a new one is issued when the level of privilege changes.

## Related Weaknesses (CWE)
- CWE-384
- CWE-664


---

# CAPEC-197: Exponential Data Expansion

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/197.html  

## Description
An adversary submits data to a target application which contains nested exponential data expansion to produce excessively large output. Many data format languages allow the definition of macro-like structures that can be used to simplify the creation of complex structures. However, this capability can be abused to create excessive demands on a processor's CPU and memory. A small number of nested expansions can result in an exponential growth in demands on memory.

## Related Attack Patterns
- ChildOf: CAPEC-230

## Prerequisites
- This type of attack requires that the target must receive input but either fail to provide an upper limit for entity expansion or provide a limit that is so large that it does not preclude significant resource consumption.

## Skills Required
- [Low] Ability to craft nested data expansion messages.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Availability; Impact: Unreliable Execution, Resource Consumption

## Mitigations
- Design: Use libraries and templates that minimize unfiltered input. Use methods that limit entity expansion and throw exceptions on attempted entity expansion.
- Implementation: For XML based data - disable altogether the use of inline DTD schemas when parsing XML objects. If a DTD must be used, normalize, filter and use an allowlist and parse with methods and routines that will detect entity expansion from untrusted sources.

## Related Weaknesses (CWE)
- CWE-770
- CWE-776


---

# CAPEC-198: XSS Targeting Error Pages

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/198.html  

## Description
An adversary distributes a link (or possibly some other query structure) with a request to a third party web server that is malformed and also contains a block of exploit code in order to have the exploit become live code in the resulting error page.

## Related Attack Patterns
- ChildOf: CAPEC-591
- ChildOf: CAPEC-592
- ChildOf: CAPEC-588

## Prerequisites
- A third party web server which fails to adequately sanitize messages sent in error pages.
- The victim must be made to execute a query crafted by the adversary which results in the infected error report.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Mitigations
- Design: Use libraries and templates that minimize unfiltered input.
- Implementation: Normalize, filter and use an allowlist for any input that will be used in error messages.
- Implementation: The victim should configure the browser to minimize active content from untrusted sources.

## Related Weaknesses (CWE)
- CWE-81


---

# CAPEC-199: XSS Using Alternate Syntax

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/199.html  

## Description
An adversary uses alternate forms of keywords or commands that result in the same action as the primary form but which may not be caught by filters. For example, many keywords are processed in a case insensitive manner. If the site's web filtering algorithm does not convert all tags into a consistent case before the comparison with forbidden keywords it is possible to bypass filters (e.g., incomplete black lists) by using an alternate case structure. For example, the "script" tag using the alternate forms of "Script" or "ScRiPt" may bypass filters where "script" is the only form tested. Other variants using different syntax representations are also possible as well as using pollution meta-characters or entities that are eventually ignored by the rendering engine. The attack can result in the execution of otherwise prohibited functionality.

## Related Attack Patterns
- ChildOf: CAPEC-591
- ChildOf: CAPEC-592
- ChildOf: CAPEC-588

## Prerequisites
- Target client software must allow scripting such as JavaScript.

## Skills Required
- [Low] To inject the malicious payload in a web page
- [High] To bypass non trivial filters in the application

## Resources Required
- Ability to send HTTP request to a web application.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Design: Use browser technologies that do not allow client side scripting.
- Design: Utilize strict type, character, and encoding enforcement
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Ensure all content coming from the client is using the same encoding; if not, the server-side application must canonicalize the data before applying any filtering.
- Implementation: Perform input validation for all remote content, including remote and user-generated content
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser
- Implementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.

## Related Weaknesses (CWE)
- CWE-87


---

# CAPEC-2: Inducing Account Lockout

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/2.html  

## Description
An attacker leverages the security functionality of the system aimed at thwarting potential attacks to launch a denial of service attack against a legitimate system user. Many systems, for instance, implement a password throttling mechanism that locks an account after a certain number of incorrect log in attempts. An attacker can leverage this throttling mechanism to lock a legitimate user out of their own account. The weakness that is being leveraged by an attacker is the very security feature that has been put in place to counteract attacks.

## Related Attack Patterns
- ChildOf: CAPEC-212

## Prerequisites
- The system has a lockout mechanism.
- An attacker must be able to reproduce behavior that would result in an account being locked.

## Skills Required
- [Low] No programming skills or computer knowledge is needed. An attacker can easily use this attack pattern following the Execution Flow above.

## Resources Required
- Computer with access to the login portion of the target system

## Consequences
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Implement intelligent password throttling mechanisms such as those which take IP address into account, in addition to the login name.
- When implementing security features, consider how they can be misused and made to turn on themselves.

## Related Weaknesses (CWE)
- CWE-645


---

# CAPEC-20: Encryption Brute Forcing

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/20.html  

## Description
An attacker, armed with the cipher text and the encryption algorithm used, performs an exhaustive (brute force) search on the key space to determine the key that decrypts the cipher text to obtain the plaintext.

## Related Attack Patterns
- ChildOf: CAPEC-112
- CanPrecede: CAPEC-668

## Prerequisites
- Ciphertext is known.
- Encryption algorithm and key size are known.

## Skills Required
- [Low] Brute forcing encryption does not require much skill.

## Resources Required
- A powerful enough computer for the job with sufficient CPU, RAM and HD. Exact requirements will depend on the size of the brute force job and the time requirement for completion. Some brute forcing jobs may require grid or distributed computing (e.g. DES Challenge). On average, for a binary key of size N, 2^(N/2) trials will be needed to find the key that would decrypt the ciphertext to obtain the original plaintext. Obviously as N gets large the brute force approach becomes infeasible.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Use commonly accepted algorithms and recommended key sizes. The key size used will depend on how important it is to keep the data confidential and for how long.
- In theory a brute force attack performing an exhaustive key space search will always succeed, so the goal is to have computational security. Moore's law needs to be taken into account that suggests that computing resources double every eighteen months.

## Related Weaknesses (CWE)
- CWE-326
- CWE-327
- CWE-693
- CWE-1204


---

# CAPEC-200: Removal of filters: Input filters, output filters, data masking

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/200.html  

## Description
An attacker removes or disables filtering mechanisms on the target application. Input filters prevent invalid data from being sent to an application (for example, overly large inputs that might cause a buffer overflow or other malformed inputs that may not be correctly handled by an application). Input filters might also be designed to constrained executable content.

## Related Attack Patterns
- ChildOf: CAPEC-207

## Prerequisites
- The target application must utilize some sort of filtering mechanism (input, output, or data masking).

## Resources Required
- None: No specialized resources are required to execute this type of attack.


---

# CAPEC-201: Serialized Data External Linking

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/201.html  

## Description
An adversary creates a serialized data file (e.g. XML, YAML, etc...) that contains an external data reference. Because serialized data parsers may not validate documents with external references, there may be no checks on the nature of the reference in the external data. This can allow an adversary to open arbitrary files or connections, which may further lead to the adversary gaining access to information on the system that they would normally be unable to obtain.

## Related Attack Patterns
- ChildOf: CAPEC-122
- ChildOf: CAPEC-278

## Prerequisites
- The target must follow external data references without validating the validity of the reference target.

## Skills Required
- [Low] To send serialized data messages with maliciously crafted schema.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Configure the serialized data processor to only retrieve external entities from trusted sources.

## Related Weaknesses (CWE)
- CWE-829


---

# CAPEC-202: Create Malicious Client

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/202.html  

## Description
An adversary creates a client application to interface with a target service where the client violates assumptions the service makes about clients. Services that have designated client applications (as opposed to services that use general client applications, such as IMAP or POP mail servers which can interact with any IMAP or POP client) may assume that the client will follow specific procedures.

## Related Attack Patterns
- ChildOf: CAPEC-22

## Prerequisites
- The targeted service must make assumptions about the behavior of the client application that interacts with it, which can be abused by an adversary.

## Resources Required
- The adversary must be able to reverse engineer a client of the targeted service. However, the adversary does not need to reverse engineer all client functionality - they only need to recreate enough of the functionality to access the desired server functionality.

## Related Weaknesses (CWE)
- CWE-602


---

# CAPEC-203: Manipulate Registry Information

**Abstraction:** Standard  
**Status:** Stable  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/203.html  

## Description
An adversary exploits a weakness in authorization in order to modify content within a registry (e.g., Windows Registry, Mac plist, application registry). Editing registry information can permit the adversary to hide configuration information or remove indicators of compromise to cover up activity. Many applications utilize registries to store configuration and service information. As such, modification of registry information can affect individual services (affecting billing, authorization, or even allowing for identity spoofing) or the overall configuration of a targeted application. For example, both Java RMI and SOAP use registries to track available services. Changing registry values is sometimes a preliminary step towards completing another attack pattern, but given the long term usage of many registry values, manipulation of registry information could be its own end.

## Related Attack Patterns
- ChildOf: CAPEC-176

## Prerequisites
- The targeted application must rely on values stored in a registry.
- The adversary must have a means of elevating permissions in order to access and modify registry content through either administrator privileges (e.g., credentialed access), or a remote access tool capable of editing a registry through an API.

## Skills Required
- [High] The adversary requires privileged credentials or the development/acquiring of a tailored remote access tool.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Mitigations
- Ensure proper permissions are set for Registry hives to prevent users from modifying keys.
- Employ a robust and layered defensive posture in order to prevent unauthorized users on your system.
- Employ robust identification and audit/blocking using an allowlist of applications on your system. Unnecessary applications, utilities, and configurations will have a presence in the system registry that can be leveraged by an adversary through this attack pattern.

## Related Weaknesses (CWE)
- CWE-15


---

# CAPEC-204: Lifting Sensitive Data Embedded in Cache

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/204.html  

## Description
An adversary examines a target application's cache, or a browser cache, for sensitive information. Many applications that communicate with remote entities or which perform intensive calculations utilize caches to improve efficiency. However, if the application computes or receives sensitive information and the cache is not appropriately protected, an attacker can browse the cache and retrieve this information. This can result in the disclosure of sensitive information.

## Related Attack Patterns
- ChildOf: CAPEC-167
- CanPrecede: CAPEC-560

## Prerequisites
- The target application must store sensitive information in a cache.
- The cache must be inadequately protected against attacker access.

## Resources Required
- The attacker must be able to reach the target application's cache. This may require prior access to the machine on which the target application runs. If the cache is encrypted, the attacker would need sufficient computational resources to crack the encryption. With strong encryption schemes, doing this could be intractable, but weaker encryption schemes could allow an attacker with sufficient resources to read the file.

## Related Weaknesses (CWE)
- CWE-524
- CWE-311
- CWE-1239
- CWE-1258


---

# CAPEC-205: DEPRECATED: Lifting credential(s)/key material embedded in client distributions (thick or thin)

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/205.html  

## Description
This attack pattern has been deprecated as it is a duplicate of CAPEC-37 : Retrieve Embedded Sensitive Data. Please refer to this other pattern going forward.


---

# CAPEC-206: Signing Malicious Code

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/206.html  

## Description
The adversary extracts credentials used for code signing from a production environment and then uses these credentials to sign malicious content with the developer's key. Many developers use signing keys to sign code or hashes of code. When users or applications verify the signatures are accurate they are led to believe that the code came from the owner of the signing key and that the code has not been modified since the signature was applied. If the adversary has extracted the signing credentials then they can use those credentials to sign their own code bundles. Users or tools that verify the signatures attached to the code will likely assume the code came from the legitimate developer and install or run the code, effectively allowing the adversary to execute arbitrary code on the victim's computer. This differs from CAPEC-673, because the adversary is performing the code signing.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- The targeted developer must use a signing key to sign code bundles. (Note that not doing this is not a defense - it only means that the adversary does not need to steal the signing key before forging code bundles in the developer's name.)

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Mitigations
- Ensure digital certificates are protected and inaccessible by unauthorized uses.
- If a digital certificate has been compromised it should be revoked and regenerated.
- Even if a piece of software has a valid and trusted digital signature, it should be assessed for any weaknesses and vulnerabilities.

## Related Weaknesses (CWE)
- CWE-732


---

# CAPEC-207: Removing Important Client Functionality

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/207.html  

## Description
An adversary removes or disables functionality on the client that the server assumes to be present and trustworthy.

## Related Attack Patterns
- ChildOf: CAPEC-22

## Prerequisites
- The targeted server must assume the client performs important actions to protect the server or the server functionality. For example, the server may assume the client filters outbound traffic or that the client performs all price calculations correctly. Moreover, the server must fail to detect when these assumptions are violated by a client.

## Skills Required
- [High] To reverse engineer the client-side code to disable/remove the functionality on the client that the server relies on.
- [Low] The adversary installs a web tool that allows scripts or the DOM model of web-based applications to be modified before they are executed in a browser. GreaseMonkey and Firebug are two examples of such tools.

## Resources Required
- The adversary must have access to a client and be able to modify the client behavior, often through reverse engineering. If the server is assuming specific client functionality, this usually means the server only recognizes a specific client application, rather than a broad class of client applications. Reverse engineering tools would likely be necessary.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Design: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side.
- Design: Ship client-side application with integrity checks (code signing) when possible.
- Design: Use obfuscation and other techniques to prevent reverse engineering the client code.

## Related Weaknesses (CWE)
- CWE-602


---

# CAPEC-208: Removing/short-circuiting 'Purse' logic: removing/mutating 'cash' decrements

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/208.html  

## Description
An attacker removes or modifies the logic on a client associated with monetary calculations resulting in incorrect information being sent to the server. A server may rely on a client to correctly compute monetary information. For example, a server might supply a price for an item and then rely on the client to correctly compute the total cost of a purchase given the number of items the user is buying. If the attacker can remove or modify the logic that controls these calculations, they can return incorrect values to the server. The attacker can use this to make purchases for a fraction of the legitimate cost or otherwise avoid correct billing for activities.

## Related Attack Patterns
- ChildOf: CAPEC-207

## Prerequisites
- The targeted server must rely on the client to correctly perform monetary calculations and must fail to detect errors in these calculations.

## Resources Required
- The attacker must have access to the client for the targeted service (this step is trivial for most web-based services). The attacker must also be able to reverse engineer the client in order to locate and modify the client's purse logic. Reverse engineering tools would be necessary for this.

## Related Weaknesses (CWE)
- CWE-602


---

# CAPEC-209: XSS Using MIME Type Mismatch

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/209.html  

## Description
An adversary creates a file with scripting content but where the specified MIME type of the file is such that scripting is not expected. The adversary tricks the victim into accessing a URL that responds with the script file. Some browsers will detect that the specified MIME type of the file does not match the actual type of its content and will automatically switch to using an interpreter for the real content type. If the browser does not invoke script filters before doing this, the adversary's script may run on the target unsanitized, possibly revealing the victim's cookies or executing arbitrary script in their browser.

## Related Attack Patterns
- ChildOf: CAPEC-592

## Prerequisites
- The victim must follow a crafted link that references a scripting file that is mis-typed as a non-executable file.
- The victim's browser must detect the true type of a mis-labeled scripting file and invoke the appropriate script interpreter without first performing filtering on the content.

## Resources Required
- The adversary must have the ability to source the file of the incorrect MIME type containing a script.

## Related Weaknesses (CWE)
- CWE-79
- CWE-20
- CWE-646


---

# CAPEC-21: Exploitation of Trusted Identifiers

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/21.html  

## Description
An adversary guesses, obtains, or "rides" a trusted identifier (e.g. session ID, resource ID, cookie, etc.) to perform authorized actions under the guise of an authenticated user or service.

## Prerequisites
- Server software must rely on weak identifier proof and/or verification schemes.
- Identifiers must have long lifetimes and potential for reusability.
- Server software must allow concurrent sessions to exist.

## Skills Required
- [Low] To achieve a direct connection with the weak or non-existent server session access control, and pose as an authorized user

## Resources Required
- Ability to deploy software on network.
- Ability to communicate synchronously or asynchronously with server.

## Consequences
- Scope: Confidentiality, Access Control, Authentication; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Design: utilize strong federated identity such as SAML to encrypt and sign identity tokens in transit.
- Implementation: Use industry standards session key generation mechanisms that utilize high amount of entropy to generate the session key. Many standard web and application servers will perform this task on your behalf.
- Implementation: If the identifier is used for authentication, such as in the so-called single sign on use cases, then ensure that it is protected at the same level of assurance as authentication tokens.
- Implementation: If the web or application server supports it, then encrypting and/or signing the identifier (such as cookie) can protect the ID if intercepted.
- Design: Use strong session identifiers that are protected in transit and at rest.
- Implementation: Utilize a session timeout for all sessions, for example 20 minutes. If the user does not explicitly logout, the server terminates their session after this period of inactivity. If the user logs back in then a new session key is generated.
- Implementation: Verify authenticity of all identifiers at runtime.

## Related Weaknesses (CWE)
- CWE-290
- CWE-302
- CWE-346
- CWE-539
- CWE-6
- CWE-384
- CWE-664
- CWE-602
- CWE-642


---

# CAPEC-211: DEPRECATED: Leveraging web tools (e.g. Mozilla's GreaseMonkey, Firebug) to change application behavior

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/211.html  

## Description
This attack pattern has been deprecated as it was deemed not to be a legitimate attack pattern.


---

# CAPEC-212: Functionality Misuse

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/212.html  

## Description
An adversary leverages a legitimate capability of an application in such a way as to achieve a negative technical impact. The system functionality is not altered or modified but used in a way that was not intended. This is often accomplished through the overuse of a specific functionality or by leveraging functionality with design flaws that enables the adversary to gain access to unauthorized, sensitive data.

## Prerequisites
- The adversary has the capability to interact with the application directly.The target system does not adequately implement safeguards to prevent misuse of authorized actions/processes.

## Skills Required
- [Low] General computer knowledge about how applications are launched, how they interact with input/output, and how they are configured.

## Consequences
- Scope: Confidentiality; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- Perform comprehensive threat modeling, a process of identifying, evaluating, and mitigating potential threats to the application. This effort can help reveal potentially obscure application functionality that can be manipulated for malicious purposes.
- When implementing security features, consider how they can be misused and compromised.

## Related Weaknesses (CWE)
- CWE-1242
- CWE-1246
- CWE-1281


---

# CAPEC-213: DEPRECATED: Directory Traversal

**Abstraction:** Standard  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/213.html  

## Description
This attack pattern has been deprecated as it is a duplicate of the existing attack pattern "CAPEC-126 : Path Traversal". Please refer to this other CAPEC going forward.


---

# CAPEC-214: DEPRECATED: Fuzzing for garnering J2EE/.NET-based stack traces, for application mapping

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/214.html  

## Description
This attack pattern has been deprecated as it was merged into "CAPEC-215 : Fuzzing for application mapping". Please refer to this other CAPEC going forward.


---

# CAPEC-215: Fuzzing for application mapping

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/215.html  

## Description
An attacker sends random, malformed, or otherwise unexpected messages to a target application and observes the application's log or error messages returned. The attacker does not initially know how a target will respond to individual messages but by attempting a large number of message variants they may find a variant that trigger's desired behavior. In this attack, the purpose of the fuzzing is to observe the application's log and error messages, although fuzzing a target can also sometimes cause the target to enter an unstable state, causing a crash.

## Related Attack Patterns
- ChildOf: CAPEC-54
- ChildOf: CAPEC-28

## Prerequisites
- The target application must fail to sanitize incoming messages adequately before processing.

## Skills Required
- [Medium] Although fuzzing parameters is not difficult, and often possible with automated fuzzing tools, interpreting the error conditions and modifying the parameters so as to move further in the process of mapping the application requires detailed knowledge of target platform, the languages and packages used as well as software design.

## Resources Required
- Fuzzing tools, which automatically generate and send message variants, are necessary for this attack. The attacker must have sufficient access to send messages to the target. The attacker must also have the ability to observe the target application's log and/or error messages in order to collect information about the target.

## Consequences
- Scope: Confidentiality; Impact: Other

## Mitigations
- Design: Construct a 'code book' for error messages. When using a code book, application error messages aren't generated in string or stack trace form, but are catalogued and replaced with a unique (often integer-based) value 'coding' for the error. Such a technique will require helpdesk and hosting personnel to use a 'code book' or similar mapping to decode application errors/logs in order to respond to them normally.
- Design: wrap application functionality (preferably through the underlying framework) in an output encoding scheme that obscures or cleanses error messages to prevent such attacks. Such a technique is often used in conjunction with the above 'code book' suggestion.
- Implementation: Obfuscate server fields of HTTP response.
- Implementation: Hide inner ordering of HTTP response header.
- Implementation: Customizing HTTP error codes such as 404 or 500.
- Implementation: Hide HTTP response header software information filed.
- Implementation: Hide cookie's software information filed.
- Implementation: Obfuscate database type in Database API's error message.

## Related Weaknesses (CWE)
- CWE-209
- CWE-532


---

# CAPEC-216: Communication Channel Manipulation

**Abstraction:** Meta  
**Status:** Stable  
**Reference:** https://capec.mitre.org/data/definitions/216.html  

## Description
An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise.

## Related Attack Patterns
- CanPrecede: CAPEC-94

## Prerequisites
- The target application must leverage an open communications channel.
- The channel on which the target communicates must be vulnerable to interception (e.g., adversary in the middle attack - CAPEC-94).

## Resources Required
- A tool that is capable of viewing network traffic and generating custom inputs to be used in the attack.

## Consequences
- Scope: Integrity; Impact: Read Data, Modify Data, Other
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Encrypt all sensitive communications using properly-configured cryptography.
- Design the communication system such that it associates proper authentication/authorization with each channel/message.

## Related Weaknesses (CWE)
- CWE-306


---

# CAPEC-217: Exploiting Incorrectly Configured SSL/TLS

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Reference:** https://capec.mitre.org/data/definitions/217.html  

## Description
An adversary takes advantage of incorrectly configured SSL/TLS communications that enables access to data intended to be encrypted. The adversary may also use this type of attack to inject commands or other traffic into the encrypted stream to cause compromise of either the client or server.

## Related Attack Patterns
- ChildOf: CAPEC-216

## Prerequisites
- Access to the client/server stream.

## Skills Required
- [High] The adversary needs real-time access to network traffic in such a manner that the adversary can grab needed information from the SSL stream, possibly influence the decided-upon encryption method and options, and perform automated analysis to decipher encrypted material recovered. Tools exist to automate part of the tasks, but to successfully use these tools in an attack scenario requires detailed understanding of the underlying principles.

## Resources Required
- The adversary needs the ability to sniff traffic, and optionally be able to route said traffic to a system where the sniffing of traffic can take place, and act upon the recovered traffic in real time.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Do not use SSL, as all SSL versions have been broken and should not be used. If TLS is not an option for the client or server, consider setting timeouts on SSL sessions to extremely low values to lessen the potential impact.
- Only use TLS version 1.2+, as versions 1.0 and 1.1 are insecure.
- Configure TLS to use secure algorithms. The current recommendation is to use ECDH, ECDSA, AES256-GCM, and SHA384 for the most security.

## Related Weaknesses (CWE)
- CWE-201


---

# CAPEC-218: Spoofing of UDDI/ebXML Messages

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/218.html  

## Description
An attacker spoofs a UDDI, ebXML, or similar message in order to impersonate a service provider in an e-business transaction. UDDI, ebXML, and similar standards are used to identify businesses in e-business transactions. Among other things, they identify a particular participant, WSDL information for SOAP transactions, and supported communication protocols, including security protocols. By spoofing one of these messages an attacker could impersonate a legitimate business in a transaction or could manipulate the protocols used between a client and business. This could result in disclosure of sensitive information, loss of message integrity, or even financial fraud.

## Related Attack Patterns
- ChildOf: CAPEC-148

## Prerequisites
- The targeted business's UDDI or ebXML information must be served from a location that the attacker can spoof or compromise or the attacker must be able to intercept and modify unsecured UDDI/ebXML messages in transit.

## Resources Required
- The attacker must be able to force the target user to accept their spoofed UDDI or ebXML message as opposed to the a message associated with a legitimate company. Depending on the follow-on for the attack, the attacker may also need to serve its own web services.

## Mitigations
- Implementation: Clients should only trust UDDI, ebXML, or similar messages that are verifiably signed by a trusted party.

## Related Weaknesses (CWE)
- CWE-345


---

# CAPEC-219: XML Routing Detour Attacks

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/219.html  

## Description
An attacker subverts an intermediate system used to process XML content and forces the intermediate to modify and/or re-route the processing of the content. XML Routing Detour Attacks are Adversary in the Middle type attacks (CAPEC-94). The attacker compromises or inserts an intermediate system in the processing of the XML message. For example, WS-Routing can be used to specify a series of nodes or intermediaries through which content is passed. If any of the intermediate nodes in this route are compromised by an attacker they could be used for a routing detour attack. From the compromised system the attacker is able to route the XML process to other nodes of their choice and modify the responses so that the normal chain of processing is unaware of the interception. This system can forward the message to an outside entity and hide the forwarding and processing from the legitimate processing systems by altering the header information.

## Related Attack Patterns
- ChildOf: CAPEC-94

## Prerequisites
- The targeted system must have multiple stages processing of XML content.

## Skills Required
- [Low] To inject a bogus node in the XML routing table

## Resources Required
- The attacker must be able to insert or compromise a system into the processing path for the transaction.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Design: Specify maximum number intermediate nodes for the request and require SSL connections with mutual authentication.
- Implementation: Use SSL for connections between all parties with mutual authentication.

## Related Weaknesses (CWE)
- CWE-441
- CWE-610


---

# CAPEC-22: Exploiting Trust in Client

**Abstraction:** Meta  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/22.html  

## Description
An attack of this type exploits vulnerabilities in client/server communication channel authentication and data integrity. It leverages the implicit trust a server places in the client, or more importantly, that which the server believes is the client. An attacker executes this type of attack by communicating directly with the server where the server believes it is communicating only with a valid client. There are numerous variations of this type of attack.

## Prerequisites
- Server software must rely on client side formatted and validated values, and not reinforce these checks on the server side.

## Skills Required
- [Medium] The attacker must have fairly detailed knowledge of the syntax and semantics of client/server communications protocols and grammars

## Resources Required
- Ability to communicate synchronously or asynchronously with server

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Design: Ensure that client process and/or message is authenticated so that anonymous communications and/or messages are not accepted by the system.
- Design: Do not rely on client validation or encoding for security purposes.
- Design: Utilize digital signatures to increase authentication assurance.
- Design: Utilize two factor authentication to increase authentication assurance.
- Implementation: Perform input validation for all remote content.

## Related Weaknesses (CWE)
- CWE-290
- CWE-287
- CWE-20
- CWE-200
- CWE-693


---

# CAPEC-220: Client-Server Protocol Manipulation

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/220.html  

## Description
An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions.

## Related Attack Patterns
- ChildOf: CAPEC-272

## Prerequisites
- The client and/or server must utilize a protocol that has a weakness allowing manipulation of the interaction.

## Resources Required
- The adversary must be able to identify the weakness in the utilized protocol and exploit it. This may require a sniffing tool as well as packet creation abilities. The adversary will be aided if they can force the client and/or server to utilize a specific protocol known to contain exploitable weaknesses.

## Related Weaknesses (CWE)
- CWE-757


---

# CAPEC-221: Data Serialization External Entities Blowup

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/221.html  

## Description
This attack takes advantage of the entity replacement property of certain data serialization languages (e.g., XML, YAML, etc.) where the value of the replacement is a URI. A well-crafted file could have the entity refer to a URI that consumes a large amount of resources to create a denial of service condition. This can cause the system to either freeze, crash, or execute arbitrary code depending on the URI.

## Related Attack Patterns
- ChildOf: CAPEC-231
- ChildOf: CAPEC-278

## Prerequisites
- A server that has an implementation that accepts entities containing URI values.

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- This attack may be mitigated by tweaking the XML parser to not resolve external entities. If external entities are needed, then implement a custom XmlResolver that has a request timeout, data retrieval limit, and restrict resources it can retrieve locally.
- This attack may be mitigated by tweaking the serialized data parser to not resolve external entities. If external entities are needed, then implement a custom resolver that has a request timeout, data retrieval limit, and restrict resources it can retrieve locally.

## Related Weaknesses (CWE)
- CWE-611


---

# CAPEC-222: iFrame Overlay

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/222.html  

## Description
In an iFrame overlay attack the victim is tricked into unknowingly initiating some action in one system while interacting with the UI from seemingly completely different system.

## Related Attack Patterns
- ChildOf: CAPEC-103

## Prerequisites
- The victim is communicating with the target application via a web based UI and not a thick client. The victim's browser security policies allow iFrames. The victim uses a modern browser that supports UI elements like clickable buttons (i.e. not using an old text only browser). The victim has an active session with the target system. The target system's interaction window is open in the victim's browser and supports the ability for initiating sensitive actions on behalf of the user in the target system.

## Skills Required
- [High] Crafting the proper malicious site and luring the victim to this site is not a trivial task.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Configuration: Disable iFrames in the Web browser.
- Operation: When maintaining an authenticated session with a privileged target system, do not use the same browser to navigate to unfamiliar sites to perform other activities. Finish working with the target system and logout first before proceeding to other tasks.
- Operation: If using the Firefox browser, use the NoScript plug-in that will help forbid iFrames.

## Related Weaknesses (CWE)
- CWE-1021


---

# CAPEC-224: Fingerprinting

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very Low  
**Reference:** https://capec.mitre.org/data/definitions/224.html  

## Description
An adversary compares output from a target system to known indicators that uniquely identify specific details about the target. Most commonly, fingerprinting is done to determine operating system and application versions. Fingerprinting can be done passively as well as actively. Fingerprinting by itself is not usually detrimental to the target. However, the information gathered through fingerprinting often enables an adversary to discover existing weaknesses in the target.

## Prerequisites
- A means by which to interact with the target system directly.

## Skills Required
- [Medium] Some fingerprinting activity requires very specific knowledge of how different operating systems respond to various TCP/IP requests. Application fingerprinting can be as easy as envoking the application with the correct command line argument, or mouse clicking in the appropriate place on the screen.

## Resources Required
- If on a network, the adversary needs a tool capable of viewing network communications at the packet level and with header information, like Mitmproxy, Wireshark, or Fiddler.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- While some information is shared by systems automatically based on standards and protocols, remove potentially sensitive information that is not necessary for the application's functionality as much as possible.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-226: Session Credential Falsification through Manipulation

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/226.html  

## Description
An attacker manipulates an existing credential in order to gain access to a target application. Session credentials allow users to identify themselves to a service after an initial authentication without needing to resend the authentication information (usually a username and password) with every message. An attacker may be able to manipulate a credential sniffed from an existing connection in order to gain access to a target server.

## Related Attack Patterns
- ChildOf: CAPEC-196

## Prerequisites
- The targeted application must use session credentials to identify legitimate users.

## Resources Required
- An attacker will need tools to sniff existing credentials (possibly their own) in order to retrieve a base credential for modification. They will need to understand how the components of the credential affect server behavior and how to manipulate this behavior by changing the credential. Finally, they will need tools to allow them to craft and transmit a modified credential.

## Related Weaknesses (CWE)
- CWE-565
- CWE-472


---

# CAPEC-227: Sustained Client Engagement

**Abstraction:** Meta  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/227.html  

## Description
An adversary attempts to deny legitimate users access to a resource by continually engaging a specific resource in an attempt to keep the resource tied up as long as possible. The adversary's primary goal is not to crash or flood the target, which would alert defenders; rather it is to repeatedly perform actions or abuse algorithmic flaws such that a given resource is tied up and not available to a legitimate user. By carefully crafting a requests that keep the resource engaged through what is seemingly benign requests, legitimate users are limited or completely denied access to the resource.

## Prerequisites
- This pattern of attack requires a temporal aspect to the servicing of a given request. Success can be achieved if the adversary can make requests that collectively take more time to complete than legitimate user requests within the same time frame.

## Resources Required
- To successfully execute this pattern of attack, a script or program is often required that is capable of continually engaging the target and maintaining sustained usage of a specific resource. Depending on the configuration of the target, it may or may not be necessary to involve a network or cluster of objects all capable of making parallel requests.

## Mitigations
- Potential mitigations include requiring a unique login for each resource request, constraining local unprivileged access by disallowing simultaneous engagements of the resource, or limiting access to the resource to one access per IP address. In such scenarios, the adversary would have to increase engagements either by launching multiple sessions manually or programmatically to counter such defenses.

## Related Weaknesses (CWE)
- CWE-400


---

# CAPEC-228: DTD Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/228.html  

## Description
An attacker injects malicious content into an application's DTD in an attempt to produce a negative technical impact. DTDs are used to describe how XML documents are processed. Certain malformed DTDs (for example, those with excessive entity expansion as described in CAPEC 197) can cause the XML parsers that process the DTDs to consume excessive resources resulting in resource depletion.

## Related Attack Patterns
- ChildOf: CAPEC-250
- CanPrecede: CAPEC-197
- CanPrecede: CAPEC-491

## Prerequisites
- The target must be running an XML based application that leverages DTDs.

## Mitigations
- Design: Sanitize incoming DTDs to prevent excessive expansion or other actions that could result in impacts like resource depletion.
- Implementation: Disallow the inclusion of DTDs as part of incoming messages.
- Implementation: Use XML parsing tools that protect against DTD attacks.

## Related Weaknesses (CWE)
- CWE-829


---

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


---

# CAPEC-23: File Content Injection

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/23.html  

## Description
An adversary poisons files with a malicious payload (targeting the file systems accessible by the target software), which may be passed through by standard channels such as via email, and standard web content like PDF and multimedia files. The adversary exploits known vulnerabilities or handling routines in the target processes, in order to exploit the host's trust in executing remote content, including binary files.

## Related Attack Patterns
- ChildOf: CAPEC-242
- CanAlsoBe: CAPEC-165

## Prerequisites
- The target software must consume files.
- The adversary must have access to modify files that the target software will consume.

## Skills Required
- [Medium] How to poison a file with malicious payload that will exploit a vulnerability when the file is opened. The adversary must also know how to place the file onto a system where it will be opened by an unsuspecting party, or force the file to be opened.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Design: Enforce principle of least privilege
- Design: Validate all input for content including files. Ensure that if files and remote content must be accepted that once accepted, they are placed in a sandbox type location so that lower assurance clients cannot write up to higher assurance processes (like Web server processes for example)
- Design: Execute programs with constrained privileges, so parent process does not open up further vulnerabilities. Ensure that all directories, temporary directories and files, and memory are executing with limited privileges to protect against remote execution.
- Design: Proxy communication to host, so that communications are terminated at the proxy, sanitizing the requests before forwarding to server host.
- Implementation: Virus scanning on host
- Implementation: Host integrity monitoring for critical files, directories, and processes. The goal of host integrity monitoring is to be aware when a security issue has occurred so that incident response and other forensic activities can begin.

## Related Weaknesses (CWE)
- CWE-20


---

# CAPEC-230: Serialized Data with Nested Payloads

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/230.html  

## Description
Applications often need to transform data in and out of a data format (e.g., XML and YAML) by using a parser. It may be possible for an adversary to inject data that may have an adverse effect on the parser when it is being processed. Many data format languages allow the definition of macro-like structures that can be used to simplify the creation of complex structures. By nesting these structures, causing the data to be repeatedly substituted, an adversary can cause the parser to consume more resources while processing, causing excessive memory consumption and CPU utilization.

## Related Attack Patterns
- ChildOf: CAPEC-130

## Prerequisites
- An application's user-controllable data is expressed in a language that supports subsitution.
- An application does not perform sufficient validation to ensure that user-controllable data is not malicious.

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Carefully validate and sanitize all user-controllable data prior to passing it to the data parser routine. Ensure that the resultant data is safe to pass to the data parser.
- Perform validation on canonical data.
- Pick a robust implementation of the data parser.

## Related Weaknesses (CWE)
- CWE-112
- CWE-20
- CWE-674
- CWE-770


---

# CAPEC-231: Oversized Serialized Data Payloads

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/231.html  

## Description
An adversary injects oversized serialized data payloads into a parser during data processing to produce adverse effects upon the parser such as exhausting system resources and arbitrary code execution.

## Related Attack Patterns
- ChildOf: CAPEC-130

## Prerequisites
- An application uses an parser for serialized data to perform transformation on user-controllable data.
- An application does not perform sufficient validation to ensure that user-controllable data is safe for a data parser.

## Skills Required
- [Low] Denial of service
- [High] Arbitrary code execution

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Carefully validate and sanitize all user-controllable serialized data prior to passing it to the parser routine. Ensure that the resultant data is safe to pass to the parser.
- Perform validation on canonical data.
- Pick a robust implementation of the serialized data parser.
- Validate data against a valid schema or DTD prior to parsing.

## Related Weaknesses (CWE)
- CWE-112
- CWE-20
- CWE-674
- CWE-770


---

# CAPEC-233: Privilege Escalation

**Abstraction:** Meta  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/233.html  

## Description
An adversary exploits a weakness enabling them to elevate their privilege and perform an action that they are not supposed to be authorized to perform.

## Related Weaknesses (CWE)
- CWE-269
- CWE-1264
- CWE-1311


---

# CAPEC-234: Hijacking a privileged process

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/234.html  

## Description
An adversary gains control of a process that is assigned elevated privileges in order to execute arbitrary code with those privileges. Some processes are assigned elevated privileges on an operating system, usually through association with a particular user, group, or role. If an attacker can hijack this process, they will be able to assume its level of privilege in order to execute their own code.

## Related Attack Patterns
- ChildOf: CAPEC-233
- CanFollow: CAPEC-242
- CanFollow: CAPEC-175
- CanFollow: CAPEC-100

## Prerequisites
- The targeted process or operating system must contain a bug that allows attackers to hijack the targeted process.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Related Weaknesses (CWE)
- CWE-732
- CWE-648


---

# CAPEC-235: DEPRECATED: Implementing a callback to system routine (old AWT Queue)

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/235.html  

## Description
This attack pattern has been deprecated. Please refer to CAPEC:30 - Hijacking a Privileged Thread of Execution.


---

# CAPEC-236: DEPRECATED: Catching exception throw/signal from privileged block

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/236.html  

## Description
This attack pattern has been deprecated as it did not have enough distinction from CAPEC-30 : Hijacking a Privileged Thread of Execution. Please refer to CAPEC-30 moving forward.


---

# CAPEC-237: Escaping a Sandbox by Calling Code in Another Language

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/237.html  

## Description
The attacker may submit malicious code of another language to obtain access to privileges that were not intentionally exposed by the sandbox, thus escaping the sandbox. For instance, Java code cannot perform unsafe operations, such as modifying arbitrary memory locations, due to restrictions placed on it by the Byte code Verifier and the JVM. If allowed, Java code can call directly into native C code, which may perform unsafe operations, such as call system calls and modify arbitrary memory locations on their behalf. To provide isolation, Java does not grant untrusted code with unmediated access to native C code. Instead, the sandboxed code is typically allowed to call some subset of the pre-existing native code that is part of standard libraries.

## Related Attack Patterns
- ChildOf: CAPEC-480

## Skills Required
- [High] The attacker must have a good knowledge of the platform specific mechanisms of signing and verifying code. Most code signing and verification schemes are based on use of cryptography, the attacker needs to have an understand of these cryptographic operations in good detail.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges

## Mitigations
- Assurance: Sanitize the code of the standard libraries to make sure there is no security weaknesses in them.
- Design: Use obfuscation and other techniques to prevent reverse engineering the standard libraries.
- Assurance: Use static analysis tool to do code review and dynamic tool to do penetration test on the standard library.
- Configuration: Get latest updates for the computer.

## Related Weaknesses (CWE)
- CWE-693


---

# CAPEC-238: DEPRECATED: Using URL/codebase / G.A.C. (code source) to convince sandbox of privilege

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/238.html  

## Description
This attack pattern has been deprecated as it did not appear to be a valid attack pattern.


---

# CAPEC-239: DEPRECATED: Subversion of Authorization Checks: Cache Filtering, Programmatic Security, etc.

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/239.html  

## Description
This attack pattern has been deprecated as it did not contain any content and did not serve any useful purpose. Please refer to "CAPEC-207: removing Important Client Functionality" going forward.


---

# CAPEC-24: Filter Failure through Buffer Overflow

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/24.html  

## Description
In this attack, the idea is to cause an active filter to fail by causing an oversized transaction. An attacker may try to feed overly long input strings to the program in an attempt to overwhelm the filter (by causing a buffer overflow) and hoping that the filter does not fail securely (i.e. the user input is let into the system unfiltered).

## Related Attack Patterns
- ChildOf: CAPEC-100

## Prerequisites
- Ability to control the length of data passed to an active filter.

## Skills Required
- [Low] An attacker can simply overflow a buffer by inserting a long string into an attacker-modifiable injection vector. The result can be a DoS.
- [High] Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Make sure that ANY failure occurring in the filtering or input validation routine is properly handled and that offending input is NOT allowed to go through. Basically make sure that the vault is closed when failure occurs.
- Pre-design: Use a language or compiler that performs automatic bounds checking.
- Pre-design through Build: Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Operational: Use OS-level preventative functionality. Not a complete solution.
- Design: Use an abstraction library to abstract away risky APIs. Not a complete solution.

## Related Weaknesses (CWE)
- CWE-120
- CWE-119
- CWE-118
- CWE-74
- CWE-20
- CWE-680
- CWE-733
- CWE-697


---

# CAPEC-240: Resource Injection

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/240.html  

## Description
An adversary exploits weaknesses in input validation by manipulating resource identifiers enabling the unintended modification or specification of a resource.

## Prerequisites
- The target application allows the user to both specify the identifier used to access a system resource. Through this permission, the user gains the capability to perform actions on that resource (e.g., overwrite the file)

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Ensure all input content that is delivered to client is sanitized against an acceptable content specification.
- Perform input validation for all content.
- Enforce regular patching of software.

## Related Weaknesses (CWE)
- CWE-99


---

# CAPEC-241: DEPRECATED: Code Injection

**Abstraction:** Meta  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/241.html  

## Description
This attack pattern has been deprecated as it is a duplicate of the existing attack pattern "CAPEC-242 : Code Injection". Please refer to this other CAPEC going forward.


---

# CAPEC-242: Code Injection

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/242.html  

## Description
An adversary exploits a weakness in input validation on the target to inject new code into that which is currently executing. This differs from code inclusion in that code inclusion involves the addition or replacement of a reference to a code file, which is subsequently loaded by the target and used as part of the code of some application.

## Prerequisites
- The target software does not validate user-controlled input such that the execution of a process may be altered by sending code in through legitimate data channels, using no other mechanism.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- Utilize strict type, character, and encoding enforcement
- Ensure all input content that is delivered to client is sanitized against an acceptable content specification.
- Perform input validation for all content.
- Enforce regular patching of software.

## Related Weaknesses (CWE)
- CWE-94


---

# CAPEC-243: XSS Targeting HTML Attributes

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/243.html  

## Description
An adversary inserts commands to perform cross-site scripting (XSS) actions in HTML attributes. Many filters do not adequately sanitize attributes against the presence of potentially dangerous commands even if they adequately sanitize tags. For example, dangerous expressions could be inserted into a style attribute in an anchor tag, resulting in the execution of malicious code when the resulting page is rendered. If a victim is tricked into viewing the rendered page the attack proceeds like a normal XSS attack, possibly resulting in the loss of sensitive cookies or other malicious activities.

## Related Attack Patterns
- ChildOf: CAPEC-591
- ChildOf: CAPEC-592
- ChildOf: CAPEC-588

## Prerequisites
- The target application must fail to adequately sanitize HTML attributes against the presence of dangerous commands.

## Resources Required
- The adversary must trick the victim into following a crafted link to a vulnerable server or view a web post where the dangerous commands are executed.

## Mitigations
- Design: Use libraries and templates that minimize unfiltered input.
- Implementation: Normalize, filter and use an allowlist for all input including that which is not expected to have any scripting content.
- Implementation: The victim should configure the browser to minimize active content from untrusted sources.

## Related Weaknesses (CWE)
- CWE-83


---

# CAPEC-244: XSS Targeting URI Placeholders

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/244.html  

## Description
An attack of this type exploits the ability of most browsers to interpret "data", "javascript" or other URI schemes as client-side executable content placeholders. This attack consists of passing a malicious URI in an anchor tag HREF attribute or any other similar attributes in other HTML tags. Such malicious URI contains, for example, a base64 encoded HTML content with an embedded cross-site scripting payload. The attack is executed when the browser interprets the malicious content i.e., for example, when the victim clicks on the malicious link.

## Related Attack Patterns
- ChildOf: CAPEC-591
- ChildOf: CAPEC-592
- ChildOf: CAPEC-588

## Prerequisites
- Target client software must allow scripting such as JavaScript and allows executable content delivered using a data URI scheme.

## Skills Required
- [Medium] To inject the malicious payload in a web page

## Resources Required
- Ability to send HTTP request to a web application

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Design: Use browser technologies that do not allow client side scripting.
- Design: Utilize strict type, character, and encoding enforcement.
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Ensure all content coming from the client is using the same encoding; if not, the server-side application must canonicalize the data before applying any filtering.
- Implementation: Perform input validation for all remote content, including remote and user-generated content
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser
- Implementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.

## Related Weaknesses (CWE)
- CWE-83


---

# CAPEC-245: XSS Using Doubled Characters

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/245.html  

## Description
The adversary bypasses input validation by using doubled characters in order to perform a cross-site scripting attack. Some filters fail to recognize dangerous sequences if they are preceded by repeated characters. For example, by doubling the < before a script command, (<<script or %3C%3script using URI encoding) the filters of some web applications may fail to recognize the presence of a script tag. If the targeted server is vulnerable to this type of bypass, the adversary can create a crafted URL or other trap to cause a victim to view a page on the targeted server where the malicious content is executed, as per a normal XSS attack.

## Related Attack Patterns
- ChildOf: CAPEC-591
- ChildOf: CAPEC-592
- ChildOf: CAPEC-588

## Prerequisites
- The targeted web application does not fully normalize input before checking for prohibited syntax. In particular, it must fail to recognize prohibited methods preceded by certain sequences of repeated characters.

## Resources Required
- The adversary must trick the victim into following a crafted link to a vulnerable server or view a web post where the dangerous commands are executed.

## Mitigations
- Design: Use libraries and templates that minimize unfiltered input.
- Implementation: Normalize, filter and sanitize all user supplied fields.
- Implementation: The victim should configure the browser to minimize active content from untrusted sources.

## Related Weaknesses (CWE)
- CWE-85


---

# CAPEC-246: DEPRECATED: XSS Using Flash

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/246.html  

## Description
This pattern has been deprecated as it is covered by a chaining relationship between CAPEC-174: Flash Parameter Injection and CAPEC-591: Stored XSS. Please refer to these CAPECs going forward.


---

# CAPEC-247: XSS Using Invalid Characters

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/247.html  

## Description
An adversary inserts invalid characters in identifiers to bypass application filtering of input. Filters may not scan beyond invalid characters but during later stages of processing content that follows these invalid characters may still be processed. This allows the adversary to sneak prohibited commands past filters and perform normally prohibited operations. Invalid characters may include null, carriage return, line feed or tab in an identifier. Successful bypassing of the filter can result in a XSS attack, resulting in the disclosure of web cookies or possibly other results.

## Related Attack Patterns
- ChildOf: CAPEC-591
- ChildOf: CAPEC-592
- ChildOf: CAPEC-588

## Prerequisites
- The target must fail to remove invalid characters from input and fail to adequately scan beyond these characters.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Mitigations
- Design: Use libraries and templates that minimize unfiltered input.
- Implementation: Normalize, filter and use an allowlist for any input that will be included in any subsequent web pages or back end operations.
- Implementation: The victim should configure the browser to minimize active content from untrusted sources.

## Related Weaknesses (CWE)
- CWE-86


---

# CAPEC-248: Command Injection

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/248.html  

## Description
An adversary looking to execute a command of their choosing, injects new items into an existing command thus modifying interpretation away from what was intended. Commands in this context are often standalone strings that are interpreted by a downstream component and cause specific responses. This type of attack is possible when untrusted values are used to build these command strings. Weaknesses in input validation or command construction can enable the attack and lead to successful exploitation.

## Prerequisites
- The target application must accept input from the user and then use this input in the construction of commands to be executed. In virtually all cases, this is some form of string input that is concatenated to a constant string defined by the application to form the full command to be executed.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- All user-controllable input should be validated and filtered for potentially unwanted characters. Using an allowlist for input is desired, but if use of a denylist approach is necessary, then focusing on command related terms and delimiters is necessary.
- Input should be encoded prior to use in commands to make sure command related characters are not treated as part of the command. For example, quotation characters may need to be encoded so that the application does not treat the quotation as a delimiter.
- Input should be parameterized, or restricted to data sections of a command, thus removing the chance that the input will be treated as part of the command itself.

## Related Weaknesses (CWE)
- CWE-77


---

# CAPEC-249: DEPRECATED: Linux Terminal Injection

**Abstraction:** Standard  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/249.html  

## Description
This attack pattern has been deprecated as it is covered by "CAPEC-40 : Manipulating Writeable Terminal Devices". Please refer to this CAPEC going forward.


---

# CAPEC-25: Forced Deadlock

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/25.html  

## Description
The adversary triggers and exploits a deadlock condition in the target software to cause a denial of service. A deadlock can occur when two or more competing actions are waiting for each other to finish, and thus neither ever does. Deadlock conditions can be difficult to detect.

## Prerequisites
- The target host has a deadlock condition. There are four conditions for a deadlock to occur, known as the Coffman conditions. [REF-101]
- The target host exposes an API to the user.

## Skills Required
- [Medium] This type of attack may be sophisticated and require knowledge about the system's resources and APIs.

## Consequences
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Use known algorithm to avoid deadlock condition (for instance non-blocking synchronization algorithms).
- For competing actions, use well-known libraries which implement synchronization.

## Related Weaknesses (CWE)
- CWE-412
- CWE-567
- CWE-662
- CWE-667
- CWE-833
- CWE-1322


---

# CAPEC-250: XML Injection

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Reference:** https://capec.mitre.org/data/definitions/250.html  

## Description
An attacker utilizes crafted XML user-controllable input to probe, attack, and inject data into the XML database, using techniques similar to SQL injection. The user-controllable input can allow for unauthorized viewing of data, bypassing authentication or the front-end application for direct XML database access, and possibly altering database information.

## Related Attack Patterns
- ChildOf: CAPEC-248

## Prerequisites
- XML queries used to process user input and retrieve information stored in XML documents
- User-controllable input not properly sanitized

## Skills Required
- [Low] An attacker must have knowledge of XML syntax and constructs in order to successfully leverage XML Injection

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as content that can be interpreted in the context of an XML data or a query.
- Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the database or application.

## Related Weaknesses (CWE)
- CWE-91
- CWE-74
- CWE-20
- CWE-707


---

# CAPEC-251: Local Code Inclusion

**Abstraction:** Standard  
**Status:** Stable  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/251.html  

## Description
The attacker forces an application to load arbitrary code files from the local machine. The attacker could use this to try to load old versions of library files that have known vulnerabilities, to load files that the attacker placed on the local machine during a prior attack, or to otherwise change the functionality of the targeted application in unexpected ways.

## Related Attack Patterns
- ChildOf: CAPEC-175

## Prerequisites
- The targeted application must have a bug that allows an adversary to control which code file is loaded at some juncture.
- Some variants of this attack may require that old versions of some code files be present and in predictable locations.

## Resources Required
- The adversary needs to have enough access to the target application to control the identity of a locally included file. The attacker may also need to be able to upload arbitrary code files to the target machine, although any location for these files may be acceptable.

## Consequences
- Scope: Integrity; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Implementation: Avoid passing user input to filesystem or framework API. If necessary to do so, implement a specific, allowlist approach.

## Related Weaknesses (CWE)
- CWE-829


---

# CAPEC-252: PHP Local File Inclusion

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/252.html  

## Description
The attacker loads and executes an arbitrary local PHP file on a target machine. The attacker could use this to try to load old versions of PHP files that have known vulnerabilities, to load PHP files that the attacker placed on the local machine during a prior attack, or to otherwise change the functionality of the targeted application in unexpected ways.

## Related Attack Patterns
- ChildOf: CAPEC-251

## Prerequisites
- The targeted PHP application must have a bug that allows an attacker to control which code file is loaded at some juncture.

## Resources Required
- The attacker needs to have enough access to the target application to control the identity of a locally included PHP file.

## Related Weaknesses (CWE)
- CWE-829


---

# CAPEC-253: Remote Code Inclusion

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/253.html  

## Description
The attacker forces an application to load arbitrary code files from a remote location. The attacker could use this to try to load old versions of library files that have known vulnerabilities, to load malicious files that the attacker placed on the remote machine, or to otherwise change the functionality of the targeted application in unexpected ways.

## Related Attack Patterns
- ChildOf: CAPEC-175
- CanPrecede: CAPEC-664

## Prerequisites
- Target application server must allow remote files to be included.The malicious file must be placed on the remote machine previously.

## Mitigations
- Minimize attacks by input validation and sanitization of any user data that will be used by the target application to locate a remote file to be included.

## Related Weaknesses (CWE)
- CWE-829


---

# CAPEC-254: DEPRECATED: DTD Injection in a SOAP Message

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/254.html  

## Description
This pattern has been deprecated as it was determined to be an unnecessary layer of abstraction. Please refer to the pattern CAPEC-228 : DTD Injection going forward.


---

# CAPEC-256: SOAP Array Overflow

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/256.html  

## Description
An attacker sends a SOAP request with an array whose actual length exceeds the length indicated in the request. If the server processing the transmission naively trusts the specified size, then an attacker can intentionally understate the size of the array, possibly resulting in a buffer overflow if the server attempts to read the entire data set into the memory it allocated for a smaller array.

## Related Attack Patterns
- ChildOf: CAPEC-100

## Prerequisites
- The targeted SOAP server must trust that the array size as stated in messages it receives is correct, but read through the entire content of the message regardless of the stated size of the array.

## Resources Required
- The attacker must be able to craft malformed SOAP messages, specifically, messages with arrays where the stated array size understates the actual size of the array in the message.

## Mitigations
- If the server either verifies the correctness of the stated array size or if the server stops processing an array once the stated number of elements have been read, regardless of the actual array size, then this attack will fail. The former detects the malformed SOAP message while the latter ensures that the server does not attempt to load more data than was allocated for.

## Related Weaknesses (CWE)
- CWE-805


---

# CAPEC-257: DEPRECATED: Abuse of Transaction Data Structure

**Abstraction:** Meta  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/257.html  

## Description
This attack pattern has been deprecated as it was deemed not to be a legitimate attack pattern.


---

# CAPEC-258: DEPRECATED: Passively Sniffing and Capturing Application Code Bound for an Authorized Client During Dynamic Update

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/258.html  

## Description
This attack pattern has been deprecated as it is a duplicate of the existing attack pattern "CAPEC-65 : Sniff Application Code". Please refer to this other CAPEC going forward.


---

# CAPEC-259: DEPRECATED: Passively Sniffing and Capturing Application Code Bound for an Authorized Client During Patching

**Abstraction:** Standard  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/259.html  

## Description
This attack pattern has been deprecated as it is a duplicate of the existing attack pattern "CAPEC-65 : Sniff Application Code". Please refer to this other CAPEC going forward.


---

# CAPEC-26: Leveraging Race Conditions

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/26.html  

## Description
The adversary targets a race condition occurring when multiple processes access and manipulate the same resource concurrently, and the outcome of the execution depends on the particular order in which the access takes place. The adversary can leverage a race condition by "running the race", modifying the resource and modifying the normal execution flow. For instance, a race condition can occur while accessing a file: the adversary can trick the system by replacing the original file with their version and cause the system to read the malicious file.

## Prerequisites
- A resource is accessed/modified concurrently by multiple processes such that a race condition exists.
- The adversary has the ability to modify the resource.

## Skills Required
- [Medium] Being able to "run the race" requires basic knowledge of concurrent processing including synchonization techniques.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Use safe libraries to access resources such as files.
- Be aware that improper use of access function calls such as chown(), tempfile(), chmod(), etc. can cause a race condition.
- Use synchronization to control the flow of execution.
- Use static analysis tools to find race conditions.
- Pay attention to concurrency problems related to the access of resources.

## Related Weaknesses (CWE)
- CWE-368
- CWE-363
- CWE-366
- CWE-370
- CWE-362
- CWE-662
- CWE-689
- CWE-667
- CWE-665
- CWE-1223
- CWE-1254
- CWE-1298


---

# CAPEC-260: DEPRECATED: Passively Sniffing and Capturing Application Code Bound for an Authorized Client During Initial Distribution

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/260.html  

## Description
This attack pattern has been deprecated as it is a duplicate of the existing attack pattern "CAPEC-65 : Sniff Application Code". Please refer to this other CAPEC going forward.


---

# CAPEC-261: Fuzzing for garnering other adjacent user/sensitive data

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/261.html  

## Description
An adversary who is authorized to send queries to a target sends variants of expected queries in the hope that these modified queries might return information (directly or indirectly through error logs) beyond what the expected set of queries should provide.

## Related Attack Patterns
- ChildOf: CAPEC-54

## Prerequisites
- The server must assume that the queries it receives follow specific templates and/or have fields or attributes that follow specific procedures. The server must process queries that it receives without adequately checking or sanitizing queries to ensure they follow these templates.

## Resources Required
- The attacker must have sufficient privileges to send queries to the targeted server. A normal client might limit the nature of these queries, so the attacker must either have a modified client or their own application which allows them to modify the expected queries.

## Related Weaknesses (CWE)
- CWE-20


---

# CAPEC-263: Force Use of Corrupted Files

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/263.html  

## Description
This describes an attack where an application is forced to use a file that an attacker has corrupted. The result is often a denial of service caused by the application being unable to process the corrupted file, but other results, including the disabling of filters or access controls (if the application fails in an unsafe way rather than failing by locking down) or buffer overflows are possible.

## Related Attack Patterns
- ChildOf: CAPEC-17

## Prerequisites
- The targeted application must utilize a configuration file that an attacker is able to corrupt. In some cases, the attacker must be able to force the (re-)reading of the corrupted file if the file is normally only consulted at startup.
- The severity of the attack hinges on how the application responds to the corrupted file. If the application detects the corruption and locks down, this may result in the denial of services provided by the application. If the application fails to detect the corruption, the result could be a more severe denial of service (crash or hang) or even an exploitable buffer overflow. If the application detects the corruption but fails in an unsafe way, this attack could result in the continuation of services but without certain security structures, such as filters or access controls. For example, if the corrupted file configures filters, an unsafe response from an application could result in simply disabling the filtering mechanisms due to the lack of usable configuration data.

## Resources Required
- This varies depending on the resources necessary to corrupt the configuration file and the resources needed to force the application to re-read it (if any).

## Related Weaknesses (CWE)
- CWE-829


---

# CAPEC-264: DEPRECATED: Environment Variable Manipulation

**Abstraction:** Meta  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/264.html  

## Description
This attack pattern has been deprecated as it is a duplicate of the existing attack pattern "CAPEC-13 : Subverting Environment Variable Values". Please refer to this other CAPEC going forward.


---

# CAPEC-265: DEPRECATED: Global variable manipulation

**Abstraction:** Meta  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/265.html  

## Description
This attack pattern has been deprecated as it is a duplicate of the existing attack pattern "CAPEC-77 : Manipulating User-Controlled Variables". Please refer to this other CAPEC going forward.


---

# CAPEC-266: DEPRECATED: Manipulate Canonicalization

**Abstraction:** Meta  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/266.html  

## Description
This attack pattern has been deprecated.


---

# CAPEC-267: Leverage Alternate Encoding

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/267.html  

## Description
An adversary leverages the possibility to encode potentially harmful input or content used by applications such that the applications are ineffective at validating this encoding standard.

## Related Attack Patterns
- ChildOf: CAPEC-153

## Prerequisites
- The application's decoder accepts and interprets encoded characters. Data canonicalization, input filtering and validating is not done properly leaving the door open to harmful characters for the target host.

## Skills Required
- [Low] An adversary can inject different representation of a filtered character in a different encoding.
- [Medium] An adversary may craft subtle encoding of input data by using the knowledge that they have gathered about the target host.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism
- Scope: Availability; Impact: Unreliable Execution, Resource Consumption

## Mitigations
- Assume all input might use an improper representation. Use canonicalized data inside the application; all data must be converted into the representation used inside the application (UTF-8, UTF-16, etc.)
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system. Test your decoding process against malicious input.

## Related Weaknesses (CWE)
- CWE-173
- CWE-172
- CWE-180
- CWE-181
- CWE-73
- CWE-74
- CWE-20
- CWE-697
- CWE-692


---

# CAPEC-268: Audit Log Manipulation

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/268.html  

## Description
The attacker injects, manipulates, deletes, or forges malicious log entries into the log file, in an attempt to mislead an audit of the log file or cover tracks of an attack. Due to either insufficient access controls of the log files or the logging mechanism, the attacker is able to perform such actions.

## Related Attack Patterns
- ChildOf: CAPEC-161

## Prerequisites
- The target host is logging the action and data of the user.
- The target host insufficiently protects access to the logs or logging mechanisms.

## Resources Required
- The attacker must understand how the logging mechanism works. Optionally, the attacker must know the location and the format of individual entries of the log files.

## Related Weaknesses (CWE)
- CWE-117


---

# CAPEC-269: DEPRECATED: Registry Manipulation

**Abstraction:** Meta  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/269.html  

## Description
This pattern has been deprecated as it was determined to be a duplicate of another pattern. Please refer to the pattern CAPEC-203 : Manipulate Application Registry Values going forward.


---

# CAPEC-27: Leveraging Race Conditions via Symbolic Links

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/27.html  

## Description
This attack leverages the use of symbolic links (Symlinks) in order to write to sensitive files. An attacker can create a Symlink link to a target file not otherwise accessible to them. When the privileged program tries to create a temporary file with the same name as the Symlink link, it will actually write to the target file pointed to by the attackers' Symlink link. If the attacker can insert malicious content in the temporary file they will be writing to the sensitive file by using the Symlink. The race occurs because the system checks if the temporary file exists, then creates the file. The attacker would typically create the Symlink during the interval between the check and the creation of the temporary file.

## Related Attack Patterns
- ChildOf: CAPEC-29

## Prerequisites
- The attacker is able to create Symlink links on the target host.
- Tainted data from the attacker is used and copied to temporary files.
- The target host does insecure temporary file creation.

## Skills Required
- [Medium] This attack is sophisticated because the attacker has to overcome a few challenges such as creating symlinks on the target host during a precise timing, inserting malicious data in the temporary file and have knowledge about the temporary files created (file name and function which creates them).

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Use safe libraries when creating temporary files. For instance the standard library function mkstemp can be used to safely create temporary files. For shell scripts, the system utility mktemp does the same thing.
- Access to the directories should be restricted as to prevent attackers from manipulating the files. Denying access to a file can prevent an attacker from replacing that file with a link to a sensitive file.
- Follow the principle of least privilege when assigning access rights to files.
- Ensure good compartmentalization in the system to provide protected areas that can be trusted.

## Related Weaknesses (CWE)
- CWE-367
- CWE-61
- CWE-662
- CWE-689
- CWE-667


---

# CAPEC-270: Modification of Registry Run Keys

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/270.html  

## Description
An adversary adds a new entry to the "run keys" in the Windows registry so that an application of their choosing is executed when a user logs in. In this way, the adversary can get their executable to operate and run on the target system with the authorized user's level of permissions. This attack is a good way for an adversary to run persistent spyware on a user's machine, such as a keylogger.

## Related Attack Patterns
- ChildOf: CAPEC-203
- CanPrecede: CAPEC-568
- CanPrecede: CAPEC-529
- CanPrecede: CAPEC-646
- CanFollow: CAPEC-555

## Prerequisites
- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.

## Consequences
- Scope: Integrity; Impact: Modify Data, Gain Privileges

## Mitigations
- Identify programs that may be used to acquire process information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.

## Related Weaknesses (CWE)
- CWE-15


---

# CAPEC-271: Schema Poisoning

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/271.html  

## Description
An adversary corrupts or modifies the content of a schema for the purpose of undermining the security of the target. Schemas provide the structure and content definitions for resources used by an application. By replacing or modifying a schema, the adversary can affect how the application handles or interprets a resource, often leading to possible denial of service, entering into an unexpected state, or recording incomplete data.

## Related Attack Patterns
- ChildOf: CAPEC-176
- CanFollow: CAPEC-94

## Prerequisites
- Some level of access to modify the target schema.
- The schema used by the target application must be improperly secured against unauthorized modification and manipulation.

## Resources Required
- Access to the schema and the knowledge and ability modify it. Ability to replace or redirect access to the modified schema.

## Consequences
- Scope: Availability; Impact: Unreliable Execution, Resource Consumption
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Design: Protect the schema against unauthorized modification.
- Implementation: For applications that use a known schema, use a local copy or a known good repository instead of the schema reference supplied in the schema document.
- Implementation: For applications that leverage remote schemas, use the HTTPS protocol to prevent modification of traffic in transit and to avoid unauthorized modification.

## Related Weaknesses (CWE)
- CWE-15


---

# CAPEC-272: Protocol Manipulation

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/272.html  

## Description
An adversary subverts a communications protocol to perform an attack. This type of attack can allow an adversary to impersonate others, discover sensitive information, control the outcome of a session, or perform other attacks. This type of attack targets invalid assumptions that may be inherent in implementers of the protocol, incorrect implementations of the protocol, or vulnerabilities in the protocol itself.

## Prerequisites
- The protocol or implementations thereof must contain bugs that an adversary can exploit.

## Resources Required
- In some variants of this attack the adversary must be able to intercept communications using the protocol. This means they need to be able to receive the communications from one participant and prevent the other participant from receiving these communications.


---

# CAPEC-273: HTTP Response Smuggling

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/273.html  

## Description
An adversary manipulates and injects malicious content in the form of secret unauthorized HTTP responses, into a single HTTP response from a vulnerable or compromised back-end HTTP agent (e.g., server). See CanPrecede relationships for possible consequences.

## Related Attack Patterns
- ChildOf: CAPEC-220
- PeerOf: CAPEC-33
- CanPrecede: CAPEC-115
- CanPrecede: CAPEC-141
- CanPrecede: CAPEC-63
- CanPrecede: CAPEC-593
- CanPrecede: CAPEC-148
- CanPrecede: CAPEC-154

## Prerequisites
- A vulnerable or compromised server or domain/site capable of allowing adversary to insert/inject malicious content that will appear in the server's response to target HTTP agents (e.g., proxies and users' web browsers).
- Differences in the way the two HTTP agents parse and interpret HTTP responses and its headers.
- HTTP agents running on HTTP/1.1 that allow for Keep Alive mode, Pipelined queries, and Chunked queries and responses.

## Skills Required
- [Medium] Detailed knowledge on HTTP protocol: request and response messages structure and usage of specific headers.
- [Medium] Detailed knowledge on how specific HTTP agents receive, send, process, interpret, and parse a variety of HTTP messages and headers.
- [Medium] Possess knowledge on the exact details in the discrepancies between several targeted HTTP agents in path of an HTTP message in parsing its message structure and individual headers.

## Resources Required
- Tools capable of monitoring HTTP messages, and crafting malicious HTTP messages and/or injecting malicious content into HTTP messages.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Design: evaluate HTTP agents prior to deployment for parsing/interpretation discrepancies.
- Configuration: front-end HTTP agents notice ambiguous requests.
- Configuration: back-end HTTP agents reject ambiguous requests and close the network connection.
- Configuration: Disable reuse of back-end connections.
- Configuration: Use HTTP/2 for back-end connections.
- Configuration: Use the same web server software for front-end and back-end server.
- Implementation: Utilize a Web Application Firewall (WAF) that has built-in mitigation to detect abnormal requests/responses.
- Configuration: Prioritize Transfer-Encoding header over Content-Length, whenever an HTTP message contains both.
- Configuration: Disallow HTTP messages with both Transfer-Encoding and Content-Length or Double Content-Length Headers.
- Configuration: Disallow Malformed/Invalid Transfer-Encoding Headers used in obfuscation, such as: Headers with no space before the value “chunked” Headers with extra spaces Headers beginning with trailing characters Headers providing a value “chunk” instead of “chunked” (the server normalizes this as chunked encoding) Headers with multiple spaces before the value “chunked” Headers with quoted values (whether single or double quotations) Headers with CRLF characters before the value “chunked” Values with invalid characters
- Configuration: Install latest vendor security patches available for both intermediary and back-end HTTP infrastructure (i.e. proxies and web servers)
- Configuration: Ensure that HTTP infrastructure in the chain or network path utilize a strict uniform parsing process.
- Implementation: Utilize intermediary HTTP infrastructure capable of filtering and/or sanitizing user-input.

## Related Weaknesses (CWE)
- CWE-74
- CWE-436
- CWE-444


---

# CAPEC-274: HTTP Verb Tampering

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/274.html  

## Description
An attacker modifies the HTTP Verb (e.g. GET, PUT, TRACE, etc.) in order to bypass access restrictions. Some web environments allow administrators to restrict access based on the HTTP Verb used with requests. However, attackers can often provide a different HTTP Verb, or even provide a random string as a verb in order to bypass these protections. This allows the attacker to access data that should otherwise be protected.

## Related Attack Patterns
- ChildOf: CAPEC-220

## Prerequisites
- The targeted system must attempt to filter access based on the HTTP verb used in requests.

## Resources Required
- The attacker requires a tool that allows them to manually control the HTTP verb used to send messages to the targeted server.

## Mitigations
- Design: Ensure that only legitimate HTTP verbs are allowed.
- Design: Do not use HTTP verbs as factors in access decisions.

## Related Weaknesses (CWE)
- CWE-302
- CWE-654


---

# CAPEC-275: DNS Rebinding

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/275.html  

## Description
An adversary serves content whose IP address is resolved by a DNS server that the adversary controls. After initial contact by a web browser (or similar client), the adversary changes the IP address to which its name resolves, to an address within the target organization that is not publicly accessible. This allows the web browser to examine this internal address on behalf of the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-194

## Prerequisites
- The target browser must access content server from the adversary controlled DNS name. Web advertisements are often used for this purpose. The target browser must honor the TTL value returned by the adversary and re-resolve the adversary's DNS name after initial contact.

## Skills Required
- [Medium] Setup DNS server and the adversary's web server. Write a malicious script to allow the victim to connect to the web server.

## Resources Required
- The adversary must serve some web content that a victim accesses initially. This content must include executable content that queries the adversary's DNS name (to provide the second DNS resolution) and then performs the follow-on attack against the internal system. The adversary also requires a customized DNS server that serves an IP address for their registered DNS name, but which resolves subsequent requests by a single client to addresses internal to that client's network.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Design: IP Pinning causes browsers to record the IP address to which a given name resolves and continue using this address regardless of the TTL set in the DNS response. Unfortunately, this is incompatible with the design of some legitimate sites.
- Implementation: Reject HTTP request with a malicious Host header.
- Implementation: Employ DNS resolvers that prevent external names from resolving to internal addresses.

## Related Weaknesses (CWE)
- CWE-350


---

# CAPEC-276: Inter-component Protocol Manipulation

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/276.html  

## Description
Inter-component protocols are used to communicate between different software and hardware modules within a single computer. Common examples are: interrupt signals and data pipes. Subverting the protocol can allow an adversary to impersonate others, discover sensitive information, control the outcome of a session, or perform other attacks. This type of attack targets invalid assumptions that may be inherent in implementers of the protocol, incorrect implementations of the protocol, or vulnerabilities in the protocol itself.

## Related Attack Patterns
- ChildOf: CAPEC-272

## Related Weaknesses (CWE)
- CWE-707


---

# CAPEC-277: Data Interchange Protocol Manipulation

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/277.html  

## Description
Data Interchange Protocols are used to transmit structured data between entities. These protocols are often specific to a particular domain (B2B: purchase orders, invoices, transport logistics and waybills, medical records). They are often, but not always, XML-based. Subverting the protocol can allow an adversary to impersonate others, discover sensitive information, control the outcome of a session, or perform other attacks. This type of attack targets invalid assumptions that may be inherent in implementers of the protocol, incorrect implementations of the protocol, or vulnerabilities in the protocol itself.

## Related Attack Patterns
- ChildOf: CAPEC-272

## Related Weaknesses (CWE)
- CWE-707


---

# CAPEC-278: Web Services Protocol Manipulation

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/278.html  

## Description
An adversary manipulates a web service related protocol to cause a web application or service to react differently than intended. This can either be performed through the manipulation of call parameters to include unexpected values, or by changing the called function to one that should normally be restricted or limited. By leveraging this pattern of attack, the adversary is able to gain access to data or resources normally restricted, or to cause the application or service to crash.

## Related Attack Patterns
- ChildOf: CAPEC-272

## Prerequisites
- The targeted application or service must rely on web service protocols in such a way that malicious manipulation of them can alter functionality.

## Resources Required
- The attacker must be able to manipulate the communications to the targeted application or service.

## Mitigations
- Design: Range, size and value and consistency verification for any arguments supplied to applications and services from external sources and devise appropriate error response.
- Design: Ensure that function calls that should not be called by an unprivileged user are not accessible to them.

## Related Weaknesses (CWE)
- CWE-707


---

# CAPEC-279: SOAP Manipulation

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/279.html  

## Description
Simple Object Access Protocol (SOAP) is used as a communication protocol between a client and server to invoke web services on the server. It is an XML-based protocol, and therefore suffers from many of the same shortcomings as other XML-based protocols. Adversaries can make use of these shortcomings and manipulate the content of SOAP paramters, leading to undesirable behavior on the server and allowing the adversary to carry out a number of further attacks.

## Related Attack Patterns
- ChildOf: CAPEC-278
- CanPrecede: CAPEC-110
- CanPrecede: CAPEC-228

## Prerequisites
- An application uses SOAP-based web service api.
- An application does not perform sufficient input validation to ensure that user-controllable data is safe for an XML parser.
- The targeted server either fails to verify that data in SOAP messages conforms to the appropriate XML schema, or it fails to correctly handle the complete range of data allowed by the schema.

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Related Weaknesses (CWE)
- CWE-707


---

# CAPEC-28: Fuzzing

**Abstraction:** Meta  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/28.html  

## Description
In this attack pattern, the adversary leverages fuzzing to try to identify weaknesses in the system. Fuzzing is a software security and functionality testing method that feeds randomly constructed input to the system and looks for an indication that a failure in response to that input has occurred. Fuzzing treats the system as a black box and is totally free from any preconceptions or assumptions about the system. Fuzzing can help an attacker discover certain assumptions made about user input in the system. Fuzzing gives an attacker a quick way of potentially uncovering some of these assumptions despite not necessarily knowing anything about the internals of the system. These assumptions can then be turned against the system by specially crafting user input that may allow an attacker to achieve their goals.

## Skills Required
- [Low] There is a wide variety of fuzzing tools available.

## Resources Required
- Fuzzing tools.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Alter Execution Logic

## Mitigations
- Test to ensure that the software behaves as per specification and that there are no unintended side effects. Ensure that no assumptions about the validity of data are made.
- Use fuzz testing during the software QA process to uncover any surprises, uncover any assumptions or unexpected behavior.

## Related Weaknesses (CWE)
- CWE-74
- CWE-20


---

# CAPEC-280: DEPRECATED: SOAP Parameter Tampering

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/280.html  

## Description
This attack pattern has been deprecated as its contents have been included in CAPEC-279 : SOAP Manipulation. Please refer to this other pattern going forward.


---

# CAPEC-285: ICMP Echo Request Ping

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/285.html  

## Description
An adversary sends out an ICMP Type 8 Echo Request, commonly known as a 'Ping', in order to determine if a target system is responsive. If the request is not blocked by a firewall or ACL, the target host will respond with an ICMP Type 0 Echo Reply datagram. This type of exchange is usually referred to as a 'Ping' due to the Ping utility present in almost all operating systems. Ping, as commonly implemented, allows a user to test for alive hosts, measure round-trip time, and measure the percentage of packet loss.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- The ability to send an ICMP type 8 query (Echo Request) to a remote target and receive an ICMP type 0 message (ICMP Echo Reply) in response. Any firewalls or access control lists between the sender and receiver must allow ICMP Type 8 and ICMP Type 0 messages in order for a ping operation to succeed.

## Skills Required
- [Low] The adversary needs to know certain linux commands for this type of attack.

## Resources Required
- Scanners or utilities that provide the ability to send custom ICMP queries.

## Consequences
- Scope: Confidentiality; Impact: Other

## Mitigations
- Consider configuring firewall rules to block ICMP Echo requests and prevent replies. If not practical, monitor and consider action when a system has fast and a repeated pattern of requests that move incrementally through port numbers.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-287: TCP SYN Scan

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/287.html  

## Description
An adversary uses a SYN scan to determine the status of ports on the remote target. SYN scanning is the most common type of port scanning that is used because of its many advantages and few drawbacks. As a result, novice attackers tend to overly rely on the SYN scan while performing system reconnaissance. As a scanning method, the primary advantages of SYN scanning are its universality and speed.

## Related Attack Patterns
- ChildOf: CAPEC-300

## Prerequisites
- This scan type is not possible with some operating systems (Windows XP SP 2). On Linux and Unix systems it requires root privileges to use raw sockets.

## Resources Required
- The ability to send TCP SYN segments to a host during network reconnaissance via the use of a network mapper or scanner, or via raw socket programming in a scripting language. Packet injection tools are also useful for this purpose. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-288: DEPRECATED: ICMP Echo Request Ping

**Abstraction:** Meta  
**Status:** Deprecated  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/288.html  

## Description
This attack pattern has been deprecated as it is a duplicate of the existing attack pattern "CAPEC-285". Please refer to this other CAPEC going forward.


---

# CAPEC-289: DEPRECATED: Infrastructure-based footprinting

**Abstraction:** Meta  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/289.html  

## Description
This attack pattern has been deprecated as it was determined to be an unnecessary layer of abstraction. Please refer to the meta level pattern CAPEC-169 : going forward, or to any of its children patterns.


---

# CAPEC-29: Leveraging Time-of-Check and Time-of-Use (TOCTOU) Race Conditions

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/29.html  

## Description
This attack targets a race condition occurring between the time of check (state) for a resource and the time of use of a resource. A typical example is file access. The adversary can leverage a file access race condition by "running the race", meaning that they would modify the resource between the first time the target program accesses the file and the time the target program uses the file. During that period of time, the adversary could replace or modify the file, causing the application to behave unexpectedly.

## Related Attack Patterns
- ChildOf: CAPEC-26

## Prerequisites
- A resource is access/modified concurrently by multiple processes.
- The adversary is able to modify resource.
- A race condition exists while accessing a resource.

## Skills Required
- [Medium] This attack can get sophisticated since the attack has to occur within a short interval of time.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Alter Execution Logic
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Use safe libraries to access resources such as files.
- Be aware that improper use of access function calls such as chown(), tempfile(), chmod(), etc. can cause a race condition.
- Use synchronization to control the flow of execution.
- Use static analysis tools to find race conditions.
- Pay attention to concurrency problems related to the access of resources.

## Related Weaknesses (CWE)
- CWE-367
- CWE-368
- CWE-366
- CWE-370
- CWE-362
- CWE-662
- CWE-691
- CWE-663
- CWE-665


---

# CAPEC-290: Enumerate Mail Exchange (MX) Records

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/290.html  

## Description
An adversary enumerates the MX records for a given via a DNS query. This type of information gathering returns the names of mail servers on the network. Mail servers are often not exposed to the Internet but are located within the DMZ of a network protected by a firewall. A side effect of this configuration is that enumerating the MX records for an organization my reveal the IP address of the firewall or possibly other internal systems. Attackers often resort to MX record enumeration when a DNS Zone Transfer is not possible.

## Related Attack Patterns
- ChildOf: CAPEC-309

## Prerequisites
- The adversary requires access to a DNS server that will return the MX records for a network.

## Resources Required
- A command-line utility or other application capable of sending requests to the DNS server is necessary.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-291: DNS Zone Transfers

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/291.html  

## Description
An attacker exploits a DNS misconfiguration that permits a ZONE transfer. Some external DNS servers will return a list of IP address and valid hostnames. Under certain conditions, it may even be possible to obtain Zone data about the organization's internal network. When successful the attacker learns valuable information about the topology of the target organization, including information about particular servers, their role within the IT structure, and possibly information about the operating systems running upon the network. This is configuration dependent behavior so it may also be required to search out multiple DNS servers while attempting to find one with ZONE transfers allowed.

## Related Attack Patterns
- ChildOf: CAPEC-309

## Prerequisites
- Access to a DNS server that allows Zone transfers.

## Resources Required
- A client application capable of interacting with the DNS server or a command-line utility or web application that automates DNS interactions.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-292: Host Discovery

**Abstraction:** Standard  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/292.html  

## Description
An adversary sends a probe to an IP address to determine if the host is alive. Host discovery is one of the earliest phases of network reconnaissance. The adversary usually starts with a range of IP addresses belonging to a target network and uses various methods to determine if a host is present at that IP address. Host discovery is usually referred to as 'Ping' scanning using a sonar analogy. The goal is to send a packet through to the IP address and solicit a response from the host. As such, a 'ping' can be virtually any crafted packet whatsoever, provided the adversary can identify a functional host based on its response. An attack of this nature is usually carried out with a 'ping sweep,' where a particular kind of ping is sent to a range of IP addresses.

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary requires logical access to the target network in order to carry out host discovery.

## Resources Required
- The resources required will differ based upon the type of host discovery being performed. Usually a network scanning tool or scanning script is required due to the volume of requests that must be generated.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-293: Traceroute Route Enumeration

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/293.html  

## Description
An adversary uses a traceroute utility to map out the route which data flows through the network in route to a target destination. Tracerouting can allow the adversary to construct a working topology of systems and routers by listing the systems through which data passes through on their way to the targeted machine. This attack can return varied results depending upon the type of traceroute that is performed. Traceroute works by sending packets to a target while incrementing the Time-to-Live field in the packet header. As the packet traverses each hop along its way to the destination, its TTL expires generating an ICMP diagnostic message that identifies where the packet expired. Traditional techniques for tracerouting involved the use of ICMP and UDP, but as more firewalls began to filter ingress ICMP, methods of traceroute using TCP were developed.

## Related Attack Patterns
- ChildOf: CAPEC-309

## Prerequisites
- A network capable of routing the attackers' packets to the destination network.

## Resources Required
- A command line version of traceroute or similar tool that performs route enumeration.

## Consequences
- Scope: Confidentiality; Impact: Other

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-294: ICMP Address Mask Request

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/294.html  

## Description
An adversary sends an ICMP Type 17 Address Mask Request to gather information about a target's networking configuration. ICMP Address Mask Requests are defined by RFC-950, "Internet Standard Subnetting Procedure." An Address Mask Request is an ICMP type 17 message that triggers a remote system to respond with a list of its related subnets, as well as its default gateway and broadcast address via an ICMP type 18 Address Mask Reply datagram. Gathering this type of information helps the adversary plan router-based attacks as well as denial-of-service attacks against the broadcast address.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- The ability to send an ICMP type 17 query (Address Mask Request) to a remote target and receive an ICMP type 18 message (ICMP Address Mask Reply) in response. Generally, modern operating systems will ignore ICMP type 17 messages, however, routers will commonly respond to this request.

## Resources Required
- The ability to send custom ICMP queries. This can be accomplished via the use of various scanners or utilities.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-295: Timestamp Request

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/295.html  

## Description
This pattern of attack leverages standard requests to learn the exact time associated with a target system. An adversary may be able to use the timestamp returned from the target to attack time-based security algorithms, such as random number generators, or time-based authentication mechanisms.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- The ability to send a timestamp request to a remote target and receive a response.

## Resources Required
- Scanners or utilities that provide the ability to send custom ICMP queries.

## Consequences
- Scope: Confidentiality; Impact: Other

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-296: ICMP Information Request

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/296.html  

## Description
An adversary sends an ICMP Information Request to a host to determine if it will respond to this deprecated mechanism. ICMP Information Requests are a deprecated message type. Information Requests were originally used for diskless machines to automatically obtain their network configuration, but this message type has been superseded by more robust protocol implementations like DHCP.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- The ability to send an ICMP Type 15 Information Request and receive an ICMP Type 16 Information Reply in response.

## Skills Required
- [Low] The adversary needs to know certain linux commands for this type of attack.

## Resources Required
- Scanners or utilities that provide the ability to send custom ICMP queries.

## Consequences
- Scope: Confidentiality; Impact: Other

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-297: TCP ACK Ping

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/297.html  

## Description
An adversary sends a TCP segment with the ACK flag set to a remote host for the purpose of determining if the host is alive. This is one of several TCP 'ping' types. The RFC 793 expected behavior for a service is to respond with a RST 'reset' packet to any unsolicited ACK segment that is not part of an existing connection. So by sending an ACK segment to a port, the adversary can identify that the host is alive by looking for a RST packet. Typically, a remote server will respond with a RST regardless of whether a port is open or closed. In this way, TCP ACK pings cannot discover the state of a remote port because the behavior is the same in either case. The firewall will look up the ACK packet in its state-table and discard the segment because it does not correspond to any active connection. A TCP ACK Ping can be used to discover if a host is alive via RST response packets sent from the host.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- The ability to send an ACK packet to a remote host and identify the response. Creating the ACK packet without building a full connection requires the use of raw sockets. As a result, it is not possible to send a TCP ACK ping from some systems (Windows XP SP 2) without the use of third-party packet drivers like Winpcap. On other systems (BSD, Linux) administrative privileges are required in order to write to the raw socket.
- The target must employ a stateless firewall that lacks a rule set that rejects unsolicited ACK packets.
- The adversary requires the ability to craft custom TCP ACK segments for use during network reconnaissance. Sending an ACK ping requires the ability to access "raw sockets" in order to create the packets with direct access to the packet header.

## Resources Required
- ACK scanning can be performed via the use of a port scanner or by raw socket manipulation using a scripting or programming language. Packet injection tools are also useful for this purpose. Depending upon the technique used it may also be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Mitigations
- Leverage stateful firewalls that allow for the rejection of a packet that is not part of an existing connection.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-298: UDP Ping

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/298.html  

## Description
An adversary sends a UDP datagram to the remote host to determine if the host is alive. If a UDP datagram is sent to an open UDP port there is very often no response, so a typical strategy for using a UDP ping is to send the datagram to a random high port on the target. The goal is to solicit an 'ICMP port unreachable' message from the target, indicating that the host is alive. UDP pings are useful because some firewalls are not configured to block UDP datagrams sent to strange or typically unused ports, like ports in the 65K range. Additionally, while some firewalls may filter incoming ICMP, weaknesses in firewall rule-sets may allow certain types of ICMP (host unreachable, port unreachable) which are useful for UDP ping attempts.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- The adversary requires the ability to send a UDP datagram to a remote host and receive a response.
- The adversary requires the ability to craft custom UDP Packets for use during network reconnaissance.
- The target's firewall must not be configured to block egress ICMP messages.

## Resources Required
- UDP pings can be performed via the use of a port scanner or by raw socket manipulation using a scripting or programming language. Packet injection tools are also useful for this purpose. Depending upon the technique used it may also be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Mitigations
- Configure your firewall to block egress ICMP messages.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-299: TCP SYN Ping

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/299.html  

## Description
An adversary uses TCP SYN packets as a means towards host discovery. Typical RFC 793 behavior specifies that when a TCP port is open, a host must respond to an incoming SYN "synchronize" packet by completing stage two of the 'three-way handshake' - by sending an SYN/ACK in response. When a port is closed, RFC 793 behavior is to respond with a RST "reset" packet. This behavior can be used to 'ping' a target to see if it is alive by sending a TCP SYN packet to a port and then looking for a RST or an ACK packet in response.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- The ability to send a TCP SYN packet to a remote target. Depending upon the operating system, the ability to craft SYN packets may require elevated privileges.

## Skills Required
- [Low] The adversary needs to know how to craft and send protocol commands from the command line or within a tool.

## Resources Required
- SYN pings can be performed via the use of a port scanner or by raw socket manipulation using a scripting or programming language. Packet injection tools are also useful for this purpose. Depending upon the technique used it may also be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-3: Using Leading 'Ghost' Character Sequences to Bypass Input Filters

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/3.html  

## Description
Some APIs will strip certain leading characters from a string of parameters. An adversary can intentionally introduce leading "ghost" characters (extra characters that don't affect the validity of the request at the API layer) that enable the input to pass the filters and therefore process the adversary's input. This occurs when the targeted API will accept input data in several syntactic forms and interpret it in the equivalent semantic way, while the filter does not take into account the full spectrum of the syntactic forms acceptable to the targeted API.

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- The targeted API must ignore the leading ghost characters that are used to get past the filters for the semantics to be the same.

## Skills Required
- [Medium] The ability to make an API request, and knowledge of "ghost" characters that will not be filtered by any input validation. These "ghost" characters must be known to not affect the way in which the request will be interpreted.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Use an allowlist rather than a denylist input validation.
- Canonicalize all data prior to validation.
- Take an iterative approach to input validation (defense in depth).

## Related Weaknesses (CWE)
- CWE-173
- CWE-41
- CWE-172
- CWE-179
- CWE-180
- CWE-181
- CWE-183
- CWE-184
- CWE-20
- CWE-74
- CWE-697
- CWE-707


---

# CAPEC-30: Hijacking a Privileged Thread of Execution

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/30.html  

## Description
An adversary hijacks a privileged thread of execution by injecting malicious code into a running process. By using a privleged thread to do their bidding, adversaries can evade process-based detection that would stop an attack that creates a new process. This can lead to an adversary gaining access to the process's memory and can also enable elevated privileges. The most common way to perform this attack is by suspending an existing thread and manipulating its memory.

## Related Attack Patterns
- ChildOf: CAPEC-233

## Prerequisites
- The application in question employs a threaded model of execution with the threads operating at, or having the ability to switch to, a higher privilege level than normal users
- In order to feasibly execute this class of attacks, the adversary must have the ability to hijack a privileged thread. This ability includes, but is not limited to, modifying environment variables that affect the process the thread belongs to, or calling native OS calls that can suspend and alter process memory. This does not preclude network-based attacks, but makes them conceptually more difficult to identify and execute.

## Skills Required
- [High] Hijacking a thread involves knowledge of how processes and threads function on the target platform, the design of the target application as well as the ability to identify the primitives to be used or manipulated to hijack the thread.

## Resources Required
- None: No specialized resources are required to execute this type of attack. The adversary needs to be able to latch onto a privileged thread. The adversary does, however, need to be able to program, compile, and link to the victim binaries being executed so that it will turn control of a privileged thread over to the adversary's malicious code. This is the case even if the adversary conducts the attack remotely.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Application Architects must be careful to design callback, signal, and similar asynchronous constructs such that they shed excess privilege prior to handing control to user-written (thus untrusted) code.
- Application Architects must be careful to design privileged code blocks such that upon return (successful, failed, or unpredicted) that privilege is shed prior to leaving the block/scope.

## Related Weaknesses (CWE)
- CWE-270


---

# CAPEC-300: Port Scanning

**Abstraction:** Standard  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/300.html  

## Description
An adversary uses a combination of techniques to determine the state of the ports on a remote target. Any service or application available for TCP or UDP networking will have a port open for communications over the network.

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary requires logical access to the target's network in order to carry out this type of attack.

## Resources Required
- The adversary requires a network mapping/scanning tool, or must conduct socket programming on the command line. Packet injection tools are also useful for this purpose. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-301: TCP Connect Scan

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/301.html  

## Description
An adversary uses full TCP connection attempts to determine if a port is open on the target system. The scanning process involves completing a 'three-way handshake' with a remote port, and reports the port as closed if the full handshake cannot be established. An advantage of TCP connect scanning is that it works against any TCP/IP stack.

## Related Attack Patterns
- ChildOf: CAPEC-300

## Prerequisites
- The adversary requires logical access to the target network. The TCP connect Scan requires the ability to connect to an available port and complete a 'three-way-handshake' This scanning technique does not require any special privileges in order to perform. This type of scan works against all TCP/IP stack implementations.

## Resources Required
- The adversary can leverage a network mapper or scanner, or perform this attack via routine socket programming in a scripting language. Packet injection tools are also useful for this purpose. Depending upon the method used it may be necessary to sniff the network to see the response.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Employ a robust network defense posture that includes an IDS/IPS system.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-302: TCP FIN Scan

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/302.html  

## Description
An adversary uses a TCP FIN scan to determine if ports are closed on the target machine. This scan type is accomplished by sending TCP segments with the FIN bit set in the packet header. The RFC 793 expected behavior is that any TCP segment with an out-of-state Flag sent to an open port is discarded, whereas segments with out-of-state flags sent to closed ports should be handled with a RST in response. This behavior should allow the adversary to scan for closed ports by sending certain types of rule-breaking packets (out of sync or disallowed by the TCB) and detect closed ports via RST packets.

## Related Attack Patterns
- ChildOf: CAPEC-300

## Prerequisites
- FIN scanning requires the use of raw sockets, and thus cannot be performed from some Windows systems (Windows XP SP 2, for example). On Unix and Linux, raw socket manipulations require root privileges.

## Resources Required
- This attack pattern requires the ability to send TCP FIN segments to a host during network reconnaissance. This can be achieved via the use of a network mapper or scanner, or via raw socket programming in a scripting language. Packet injection tools are also useful for this purpose. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Mitigations
- FIN scans are detected via heuristic (non-signature) based algorithms, much in the same way as other scan types are detected. An IDS/IPS system with heuristic algorithms is required to detect them.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-303: TCP Xmas Scan

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/303.html  

## Description
An adversary uses a TCP XMAS scan to determine if ports are closed on the target machine. This scan type is accomplished by sending TCP segments with all possible flags set in the packet header, generating packets that are illegal based on RFC 793. The RFC 793 expected behavior is that any TCP segment with an out-of-state Flag sent to an open port is discarded, whereas segments with out-of-state flags sent to closed ports should be handled with a RST in response. This behavior should allow an attacker to scan for closed ports by sending certain types of rule-breaking packets (out of sync or disallowed by the TCB) and detect closed ports via RST packets.

## Related Attack Patterns
- ChildOf: CAPEC-300

## Prerequisites
- The adversary needs logical access to the target network. XMAS scanning requires the use of raw sockets, and thus cannot be performed from some Windows systems (Windows XP SP 2, for example). On Unix and Linux, raw socket manipulations require root privileges.

## Resources Required
- This attack can be carried out with a network mapper or scanner, or via raw socket programming in a scripting language. Packet injection tools are also useful for this purpose. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Employ a robust network defensive posture that includes a managed IDS/IPS.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-304: TCP Null Scan

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/304.html  

## Description
An adversary uses a TCP NULL scan to determine if ports are closed on the target machine. This scan type is accomplished by sending TCP segments with no flags in the packet header, generating packets that are illegal based on RFC 793. The RFC 793 expected behavior is that any TCP segment with an out-of-state Flag sent to an open port is discarded, whereas segments with out-of-state flags sent to closed ports should be handled with a RST in response. This behavior should allow an attacker to scan for closed ports by sending certain types of rule-breaking packets (out of sync or disallowed by the TCB) and detect closed ports via RST packets.

## Related Attack Patterns
- ChildOf: CAPEC-300

## Prerequisites
- The adversary requires logical access to the target network. NULL scanning requires the use of raw sockets, and thus cannot be performed from some Windows systems (Windows XP SP 2, for example). On Unix and Linux, raw socket manipulations require root privileges.

## Resources Required
- This attack can be carried out via a network mapper/scanner, or via raw socket programming in a scripting language. Packet injection tools are also useful for this purpose. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Mitigations
- Employ a robust network defensive posture that includes a managed IDS/IPS.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-305: TCP ACK Scan

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/305.html  

## Description
An adversary uses TCP ACK segments to gather information about firewall or ACL configuration. The purpose of this type of scan is to discover information about filter configurations rather than port state. This type of scanning is rarely useful alone, but when combined with SYN scanning, gives a more complete picture of the type of firewall rules that are present.

## Related Attack Patterns
- ChildOf: CAPEC-300

## Prerequisites
- The adversary requires logical access to the target network. ACK scanning requires the use of raw sockets, and thus cannot be performed from some Windows systems (Windows XP SP 2, for example). On Unix and Linux, raw socket manipulations require root privileges.

## Resources Required
- This attack can be achieved via the use of a network mapper or scanner, or via raw socket programming in a scripting language. Packet injection tools are also useful for this purpose. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-306: TCP Window Scan

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/306.html  

## Description
An adversary engages in TCP Window scanning to analyze port status and operating system type. TCP Window scanning uses the ACK scanning method but examine the TCP Window Size field of response RST packets to make certain inferences. While TCP Window Scans are fast and relatively stealthy, they work against fewer TCP stack implementations than any other type of scan. Some operating systems return a positive TCP window size when a RST packet is sent from an open port, and a negative value when the RST originates from a closed port. TCP Window scanning is one of the most complex scan types, and its results are difficult to interpret. Window scanning alone rarely yields useful information, but when combined with other types of scanning is more useful. It is a generally more reliable means of making inference about operating system versions than port status.

## Related Attack Patterns
- ChildOf: CAPEC-300

## Prerequisites
- TCP Window scanning requires the use of raw sockets, and thus cannot be performed from some Windows systems (Windows XP SP 2, for example). On Unix and Linux, raw socket manipulations require root privileges.

## Resources Required
- The ability to send TCP segments with a custom window size to a host during network reconnaissance. This can be achieved via the use of a network mapper or scanner, or via raw socket programming in a scripting language. Packet injection tools are also useful for this purpose. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-307: TCP RPC Scan

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/307.html  

## Description
An adversary scans for RPC services listing on a Unix/Linux host.

## Related Attack Patterns
- ChildOf: CAPEC-300

## Prerequisites
- RPC scanning requires no special privileges when it is performed via a native system utility.

## Resources Required
- The ability to craft custom RPC datagrams for use during network reconnaissance via native OS utilities or a port scanning tool. By tailoring the bytes injected one can scan for specific RPC-registered services. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Mitigations
- Typically, an IDS/IPS system is very effective against this type of attack.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-308: UDP Scan

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/308.html  

## Description
An adversary engages in UDP scanning to gather information about UDP port status on the target system. UDP scanning methods involve sending a UDP datagram to the target port and looking for evidence that the port is closed. Open UDP ports usually do not respond to UDP datagrams as there is no stateful mechanism within the protocol that requires building or establishing a session. Responses to UDP datagrams are therefore application specific and cannot be relied upon as a method of detecting an open port. UDP scanning relies heavily upon ICMP diagnostic messages in order to determine the status of a remote port.

## Related Attack Patterns
- ChildOf: CAPEC-300

## Prerequisites
- The ability to send UDP datagrams to a host and receive ICMP error messages from that host. In cases where particular types of ICMP messaging is disallowed, the reliability of UDP scanning drops off sharply.

## Resources Required
- The ability to craft custom UDP Packets for use during network reconnaissance. This can be accomplished via the use of a port scanner, or via socket manipulation in a programming or scripting language. Packet injection tools are also useful. It is also necessary to trap ICMP diagnostic messages during this process. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Mitigations
- Firewalls or ACLs which block egress ICMP error types effectively prevent UDP scans from returning any useful information.
- UDP scanning is complicated by rate limiting mechanisms governing ICMP error messages.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-309: Network Topology Mapping

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/309.html  

## Description
An adversary engages in scanning activities to map network nodes, hosts, devices, and routes. Adversaries usually perform this type of network reconnaissance during the early stages of attack against an external network. Many types of scanning utilities are typically employed, including ICMP tools, network mappers, port scanners, and route testing utilities such as traceroute.

## Related Attack Patterns
- ChildOf: CAPEC-169
- CanPrecede: CAPEC-664

## Prerequisites
- None

## Resources Required
- Probing requires the ability to interactively send and receive data from a target, whereas passive listening requires a sufficient understanding of the protocol to analyze a preexisting channel of communication.

## Consequences
- Scope: Confidentiality; Impact: Other

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-31: Accessing/Intercepting/Modifying HTTP Cookies

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/31.html  

## Description
This attack relies on the use of HTTP Cookies to store credentials, state information and other critical data on client systems. There are several different forms of this attack. The first form of this attack involves accessing HTTP Cookies to mine for potentially sensitive data contained therein. The second form involves intercepting this data as it is transmitted from client to server. This intercepted information is then used by the adversary to impersonate the remote user/session. The third form is when the cookie's content is modified by the adversary before it is sent back to the server. Here the adversary seeks to convince the target server to operate on this falsified information.

## Related Attack Patterns
- ChildOf: CAPEC-39
- ChildOf: CAPEC-157

## Prerequisites
- Target server software must be a HTTP daemon that relies on cookies.
- The cookies must contain sensitive information.
- The adversary must be able to make HTTP requests to the server, and the cookie must be contained in the reply.

## Skills Required
- [Low] To overwrite session cookie data, and submit targeted attacks via HTTP
- [High] Exploiting a remote buffer overflow generated by attack

## Resources Required
- A utility that allows for the viewing and modification of cookies. Many modern web browsers support this behavior.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Design: Use input validation for cookies
- Design: Generate and validate MAC for cookies
- Implementation: Use SSL/TLS to protect cookie in transit
- Implementation: Ensure the web server implements all relevant security patches, many exploitable buffer overflows are fixed in patches issued for the software.

## Related Weaknesses (CWE)
- CWE-565
- CWE-302
- CWE-311
- CWE-113
- CWE-539
- CWE-20
- CWE-315
- CWE-384
- CWE-472
- CWE-602
- CWE-642


---

# CAPEC-310: Scanning for Vulnerable Software

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/310.html  

## Description
An attacker engages in scanning activity to find vulnerable software versions or types, such as operating system versions or network services. Vulnerable or exploitable network configurations, such as improperly firewalled systems, or misconfigured systems in the DMZ or external network, provide windows of opportunity for an attacker. Common types of vulnerable software include unpatched operating systems or services (e.g FTP, Telnet, SMTP, SNMP) running on open ports that the attacker has identified. Attackers usually begin probing for vulnerable software once the external network has been port scanned and potential targets have been revealed.

## Related Attack Patterns
- ChildOf: CAPEC-541

## Prerequisites
- Access to the network on which the targeted system resides.
- Software tools used to probe systems over a range of ports and protocols.

## Skills Required
- [Medium] To probe a system remotely without detection requires careful planning and patience.

## Resources Required
- Probing requires the ability to interactively send and receive data from a target, whereas passive listening requires a sufficient understanding of the protocol to analyze a preexisting channel of communication.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-311: DEPRECATED: OS Fingerprinting

**Abstraction:** Standard  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/311.html  

## Description
This pattern has been deprecated as it was determined to be an unnecessary layer of abstraction. Please refer to the standard level patterns CAPEC-312 : Active OS Fingerprinting or CAPEC-313 : Passive OS Fingerprinting going forward, or to any of the detailed patterns that are children of them.


---

# CAPEC-312: Active OS Fingerprinting

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/312.html  

## Description
An adversary engages in activity to detect the operating system or firmware version of a remote target by interrogating a device, server, or platform with a probe designed to solicit behavior that will reveal information about the operating systems or firmware in the environment. Operating System detection is possible because implementations of common protocols (Such as IP or TCP) differ in distinct ways. While the implementation differences are not sufficient to 'break' compatibility with the protocol the differences are detectable because the target will respond in unique ways to specific probing activity that breaks the semantic or logical rules of packet construction for a protocol. Different operating systems will have a unique response to the anomalous input, providing the basis to fingerprint the OS behavior. This type of OS fingerprinting can distinguish between operating system types and versions.

## Related Attack Patterns
- ChildOf: CAPEC-224

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- Any type of active probing that involves non-standard packet headers requires the use of raw sockets, which is not available on particular operating systems (Microsoft Windows XP SP 2, for example). Raw socket manipulation on Unix/Linux requires root privileges. A tool capable of sending and receiving packets from a remote system.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-313: Passive OS Fingerprinting

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/313.html  

## Description
An adversary engages in activity to detect the version or type of OS software in a an environment by passively monitoring communication between devices, nodes, or applications. Passive techniques for operating system detection send no actual probes to a target, but monitor network or client-server communication between nodes in order to identify operating systems based on observed behavior as compared to a database of known signatures or values. While passive OS fingerprinting is not usually as reliable as active methods, it is generally better able to evade detection.

## Related Attack Patterns
- ChildOf: CAPEC-224

## Prerequisites
- The ability to monitor network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- Any tool capable of monitoring network communications, like a packet sniffer (e.g., Wireshark)

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-314: DEPRECATED: IP Fingerprinting Probes

**Abstraction:** Standard  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/314.html  

## Description
This pattern has been deprecated as it was determined to be an unnecessary layer of abstraction. Please refer to the standard level pattern CAPEC-312 : Active OS Fingerprinting going forward, or to any of the detailed patterns that children of CAPEC-312.


---

# CAPEC-315: DEPRECATED: TCP/IP Fingerprinting Probes

**Abstraction:** Standard  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/315.html  

## Description
This pattern has been deprecated as it was determined to be an unnecessary layer of abstraction. Please refer to the standard level pattern CAPEC-312 : Active OS Fingerprinting going forward, or to any of the detailed patterns that are children of CAPEC-312.


---

# CAPEC-316: DEPRECATED: ICMP Fingerprinting Probes

**Abstraction:** Standard  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/316.html  

## Description
This pattern has been deprecated as it was determined to be an unnecessary layer of abstraction. Please refer to the standard level pattern CAPEC-312 : Active OS Fingerprinting going forward, or to any of the detailed patterns that are children of CAPEC-312.


---

# CAPEC-317: IP ID Sequencing Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/317.html  

## Description
This OS fingerprinting probe analyzes the IP 'ID' field sequence number generation algorithm of a remote host. Operating systems generate IP 'ID' numbers differently, allowing an attacker to identify the operating system of the host by examining how is assigns ID numbers when generating response packets. RFC 791 does not specify how ID numbers are chosen or their ranges, so ID sequence generation differs from implementation to implementation. There are two kinds of IP 'ID' sequence number analysis - IP 'ID' Sequencing: analyzing the IP 'ID' sequence generation algorithm for one protocol used by a host and Shared IP 'ID' Sequencing: analyzing the packet ordering via IP 'ID' values spanning multiple protocols, such as between ICMP and TCP.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-318: IP 'ID' Echoed Byte-Order Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/318.html  

## Description
This OS fingerprinting probe tests to determine if the remote host echoes back the IP 'ID' value from the probe packet. An attacker sends a UDP datagram with an arbitrary IP 'ID' value to a closed port on the remote host to observe the manner in which this bit is echoed back in the ICMP error message. The identification field (ID) is typically utilized for reassembling a fragmented packet. Some operating systems or router firmware reverse the bit order of the ID field when echoing the IP Header portion of the original datagram within an ICMP error message.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-319: IP (DF) 'Don't Fragment Bit' Echoing Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/319.html  

## Description
This OS fingerprinting probe tests to determine if the remote host echoes back the IP 'DF' (Don't Fragment) bit in a response packet. An attacker sends a UDP datagram with the DF bit set to a closed port on the remote host to observe whether the 'DF' bit is set in the response packet. Some operating systems will echo the bit in the ICMP error message while others will zero out the bit in the response packet.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-32: XSS Through HTTP Query Strings

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/32.html  

## Description
An adversary embeds malicious script code in the parameters of an HTTP query string and convinces a victim to submit the HTTP request that contains the query string to a vulnerable web application. The web application then procedes to use the values parameters without properly validation them first and generates the HTML code that will be executed by the victim's browser.

## Related Attack Patterns
- ChildOf: CAPEC-591
- ChildOf: CAPEC-588
- ChildOf: CAPEC-592

## Prerequisites
- Target client software must allow scripting such as JavaScript. Server software must allow display of remote generated HTML without sufficient input or output validation.

## Skills Required
- [Low] To place malicious payload on server via HTTP
- [High] Exploiting any information gathered by HTTP Query on script host

## Resources Required
- Ability to send HTTP post to scripting host and collect output

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Design: Use browser technologies that do not allow client side scripting.
- Design: Utilize strict type, character, and encoding enforcement
- Design: Server side developers should not proxy content via XHR or other means, if a http proxy for remote content is setup on the server side, the client's browser has no way of discerning where the data is originating from.
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Perform input validation for all remote content, including remote and user-generated content
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser
- Implementation: Session tokens for specific host
- Implementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.
- Implementation: Privileges are constrained, if a script is loaded, ensure system runs in chroot jail or other limited authority mode

## Related Weaknesses (CWE)
- CWE-80


---

# CAPEC-320: TCP Timestamp Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/320.html  

## Description
This OS fingerprinting probe examines the remote server's implementation of TCP timestamps. Not all operating systems implement timestamps within the TCP header, but when timestamps are used then this provides the attacker with a means to guess the operating system of the target. The attacker begins by probing any active TCP service in order to get response which contains a TCP timestamp. Different Operating systems update the timestamp value using different intervals. This type of analysis is most accurate when multiple timestamp responses are received and then analyzed. TCP timestamps can be found in the TCP Options field of the TCP header.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.The target OS must support the TCP timestamp option in order to obtain a fingerprint.

## Resources Required
- Any type of active probing that involves non-standard packet headers requires the use of raw sockets, which is not available on particular operating systems (Microsoft Windows XP SP 2, for example). Raw socket manipulation on Unix/Linux requires root privileges. A tool capable of sending and receiving packets from a remote system.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-321: TCP Sequence Number Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/321.html  

## Description
This OS fingerprinting probe tests the target system's assignment of TCP sequence numbers. One common way to test TCP Sequence Number generation is to send a probe packet to an open port on the target and then compare the how the Sequence Number generated by the target relates to the Acknowledgement Number in the probe packet. Different operating systems assign Sequence Numbers differently, so a fingerprint of the operating system can be obtained by categorizing the relationship between the acknowledgement number and sequence number as follows: 1) the Sequence Number generated by the target is Zero, 2) the Sequence Number generated by the target is the same as the acknowledgement number in the probe, 3) the Sequence Number generated by the target is the acknowledgement number plus one, or 4) the Sequence Number is any other non-zero number.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- A tool capable of sending and receiving packets from a remote system.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-322: TCP (ISN) Greatest Common Divisor Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/322.html  

## Description
This OS fingerprinting probe sends a number of TCP SYN packets to an open port of a remote machine. The Initial Sequence Number (ISN) in each of the SYN/ACK response packets is analyzed to determine the smallest number that the target host uses when incrementing sequence numbers. This information can be useful for identifying an operating system because particular operating systems and versions increment sequence numbers using different values. The result of the analysis is then compared against a database of OS behaviors to determine the OS type and/or version.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- A tool capable of sending and receiving packets from a remote system.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-323: TCP (ISN) Counter Rate Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/323.html  

## Description
This OS detection probe measures the average rate of initial sequence number increments during a period of time. Sequence numbers are incremented using a time-based algorithm and are susceptible to a timing analysis that can determine the number of increments per unit time. The result of this analysis is then compared against a database of operating systems and versions to determine likely operation system matches.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- Any type of active probing that involves non-standard packet headers requires the use of raw sockets, which is not available on particular operating systems (Microsoft Windows XP SP 2, for example). Raw socket manipulation on Unix/Linux requires root privileges. A tool capable of sending and receiving packets from a remote system.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-324: TCP (ISN) Sequence Predictability Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/324.html  

## Description
This type of operating system probe attempts to determine an estimate for how predictable the sequence number generation algorithm is for a remote host. Statistical techniques, such as standard deviation, can be used to determine how predictable the sequence number generation is for a system. This result can then be compared to a database of operating system behaviors to determine a likely match for operating system and version.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- A tool capable of sending and receiving packets from a remote system.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-325: TCP Congestion Control Flag (ECN) Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/325.html  

## Description
This OS fingerprinting probe checks to see if the remote host supports explicit congestion notification (ECN) messaging. ECN messaging was designed to allow routers to notify a remote host when signal congestion problems are occurring. Explicit Congestion Notification messaging is defined by RFC 3168. Different operating systems and versions may or may not implement ECN notifications, or may respond uniquely to particular ECN flag types.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- A tool capable of sending and receiving packets from a remote system.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-326: TCP Initial Window Size Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/326.html  

## Description
This OS fingerprinting probe checks the initial TCP Window size. TCP stacks limit the range of sequence numbers allowable within a session to maintain the "connected" state within TCP protocol logic. The initial window size specifies a range of acceptable sequence numbers that will qualify as a response to an ACK packet within a session. Various operating systems use different Initial window sizes. The initial window size can be sampled by establishing an ordinary TCP connection.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- A tool capable of sending and receiving packets from a remote system.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-327: TCP Options Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/327.html  

## Description
This OS fingerprinting probe analyzes the type and order of any TCP header options present within a response segment. Most operating systems use unique ordering and different option sets when options are present. RFC 793 does not specify a required order when options are present, so different implementations use unique ways of ordering or structuring TCP options. TCP options can be generated by ordinary TCP traffic.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- A tool capable of sending and receiving packets from a remote system.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-328: TCP 'RST' Flag Checksum Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/328.html  

## Description
This OS fingerprinting probe performs a checksum on any ASCII data contained within the data portion or a RST packet. Some operating systems will report a human-readable text message in the payload of a 'RST' (reset) packet when specific types of connection errors occur. RFC 1122 allows text payloads within reset packets but not all operating systems or routers implement this functionality.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- A tool capable of sending and receiving packets from a remote system.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-329: ICMP Error Message Quoting Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/329.html  

## Description
An adversary uses a technique to generate an ICMP Error message (Port Unreachable, Destination Unreachable, Redirect, Source Quench, Time Exceeded, Parameter Problem) from a target and then analyze the amount of data returned or "Quoted" from the originating request that generated the ICMP error message.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- A tool capable of sending/receiving UDP datagram packets from a remote system to a closed port and receive an ICMP Error Message Type 3, "Port Unreachable..

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-33: HTTP Request Smuggling

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/33.html  

## Description
An adversary abuses the flexibility and discrepancies in the parsing and interpretation of HTTP Request messages using various HTTP headers, request-line and body parameters as well as message sizes (denoted by the end of message signaled by a given HTTP header) by different intermediary HTTP agents (e.g., load balancer, reverse proxy, web caching proxies, application firewalls, etc.) to secretly send unauthorized and malicious HTTP requests to a back-end HTTP agent (e.g., web server). See CanPrecede relationships for possible consequences.

## Related Attack Patterns
- ChildOf: CAPEC-220
- PeerOf: CAPEC-273
- CanPrecede: CAPEC-115
- CanPrecede: CAPEC-141
- CanPrecede: CAPEC-63
- CanPrecede: CAPEC-593
- CanPrecede: CAPEC-148
- CanPrecede: CAPEC-154

## Prerequisites
- An additional intermediary HTTP agent such as an application firewall or a web caching proxy between the adversary and the second agent such as a web server, that sends multiple HTTP messages over same network connection.
- Differences in the way the two HTTP agents parse and interpret HTTP requests and its headers.
- HTTP agents running on HTTP/1.1 that allow for Keep Alive mode, Pipelined queries, and Chunked queries and responses.

## Skills Required
- [Medium] Detailed knowledge on HTTP protocol: request and response messages structure and usage of specific headers.
- [Medium] Detailed knowledge on how specific HTTP agents receive, send, process, interpret, and parse a variety of HTTP messages and headers.
- [Medium] Possess knowledge on the exact details in the discrepancies between several targeted HTTP agents in path of an HTTP message in parsing its message structure and individual headers.

## Resources Required
- Tools capable of crafting malicious HTTP messages and monitoring HTTP message responses.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Design: evaluate HTTP agents prior to deployment for parsing/interpretation discrepancies.
- Configuration: front-end HTTP agents notice ambiguous requests.
- Configuration: back-end HTTP agents reject ambiguous requests and close the network connection.
- Configuration: Disable reuse of back-end connections.
- Configuration: Use HTTP/2 for back-end connections.
- Configuration: Use the same web server software for front-end and back-end server.
- Implementation: Utilize a Web Application Firewall (WAF) that has built-in mitigation to detect abnormal requests/responses.
- Configuration: Prioritize Transfer-Encoding header over Content-Length, whenever an HTTP message contains both.
- Configuration: Disallow HTTP messages with both Transfer-Encoding and Content-Length or Double Content-Length Headers.
- Configuration: Disallow Malformed/Invalid Transfer-Encoding Headers used in obfuscation, such as: Headers with no space before the value “chunked” Headers with extra spaces Headers beginning with trailing characters Headers providing a value “chunk” instead of “chunked” (the server normalizes this as chunked encoding) Headers with multiple spaces before the value “chunked” Headers with quoted values (whether single or double quotations) Headers with CRLF characters before the value “chunked” Values with invalid characters
- Configuration: Install latest vendor security patches available for both intermediary and back-end HTTP infrastructure (i.e. proxies and web servers)
- Configuration: Ensure that HTTP infrastructure in the chain or network path utilize a strict uniform parsing process.
- Implementation: Utilize intermediary HTTP infrastructure capable of filtering and/or sanitizing user-input.

## Related Weaknesses (CWE)
- CWE-444


---

# CAPEC-330: ICMP Error Message Echoing Integrity Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/330.html  

## Description
An adversary uses a technique to generate an ICMP Error message (Port Unreachable, Destination Unreachable, Redirect, Source Quench, Time Exceeded, Parameter Problem) from a target and then analyze the integrity of data returned or "Quoted" from the originating request that generated the error message.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- A tool capable of sending/receiving UDP datagram packets from a remote system to a closed port and receive an ICMP Error Message Type 3, "Port Unreachable..

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-331: ICMP IP Total Length Field Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/331.html  

## Description
An adversary sends a UDP packet to a closed port on the target machine to solicit an IP Header's total length field value within the echoed 'Port Unreachable" error message. This type of behavior is useful for building a signature-base of operating system responses, particularly when error messages contain other types of information that is useful identifying specific operating system responses.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Prerequisites
- The ability to monitor and interact with network communications. Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- A tool capable of sending/receiving UDP datagram packets from a remote system to a closed port and receive an ICMP Error Message Type 3, "Port Unreachable."

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-204


---

# CAPEC-332: ICMP IP 'ID' Field Error Message Probe

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/332.html  

## Description
An adversary sends a UDP datagram having an assigned value to its internet identification field (ID) to a closed port on a target to observe the manner in which this bit is echoed back in the ICMP error message. This allows the attacker to construct a fingerprint of specific OS behaviors.

## Related Attack Patterns
- ChildOf: CAPEC-312

## Prerequisites
- The ability to monitor and interact with network communications. Access to at least one host, and the privileges to interface with the network interface card.

## Resources Required
- A tool capable of sending/receiving UDP datagram packets from a remote system to a closed port and receive an ICMP Error Message Type 3, "Port Unreachable."

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Related Weaknesses (CWE)
- CWE-204


---

# CAPEC-34: HTTP Response Splitting

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/34.html  

## Description
An adversary manipulates and injects malicious content, in the form of secret unauthorized HTTP responses, into a single HTTP response from a vulnerable or compromised back-end HTTP agent (e.g., web server) or into an already spoofed HTTP response from an adversary controlled domain/site. See CanPrecede relationships for possible consequences.

## Related Attack Patterns
- ChildOf: CAPEC-220
- PeerOf: CAPEC-105
- CanPrecede: CAPEC-115
- CanPrecede: CAPEC-141
- CanPrecede: CAPEC-63
- CanPrecede: CAPEC-593
- CanPrecede: CAPEC-148
- CanPrecede: CAPEC-154

## Prerequisites
- A vulnerable or compromised server or domain/site capable of allowing adversary to insert/inject malicious content that will appear in the server's response to target HTTP agents (e.g., proxies and users' web browsers).
- Differences in the way the two HTTP agents parse and interpret HTTP requests and its headers.
- HTTP headers capable of being user-manipulated.
- HTTP agents running on HTTP/1.0 or HTTP/1.1 that allow for Keep Alive mode, Pipelined queries, and Chunked queries and responses.

## Skills Required
- [Medium] Detailed knowledge on HTTP protocol: request and response messages structure and usage of specific headers.
- [Medium] Detailed knowledge on how specific HTTP agents receive, send, process, interpret, and parse a variety of HTTP messages and headers.
- [Medium] Possess knowledge on the exact details in the discrepancies between several targeted HTTP agents in path of an HTTP message in parsing its message structure and individual headers.

## Resources Required
- Tools capable of monitoring HTTP messages, and crafting malicious HTTP messages and/or injecting malicious content into HTTP messages.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Design: evaluate HTTP agents prior to deployment for parsing/interpretation discrepancies.
- Configuration: front-end HTTP agents notice ambiguous requests.
- Configuration: back-end HTTP agents reject ambiguous requests and close the network connection.
- Configuration: Disable reuse of back-end connections.
- Configuration: Use HTTP/2 for back-end connections.
- Configuration: Use the same web server software for front-end and back-end server.
- Implementation: Utilize a Web Application Firewall (WAF) that has built-in mitigation to detect abnormal requests/responses.
- Configuration: Install latest vendor security patches available for both intermediary and back-end HTTP infrastructure (i.e. proxies and web servers)
- Configuration: Ensure that HTTP infrastructure in the chain or network path utilize a strict uniform parsing process.
- Implementation: Utilize intermediary HTTP infrastructure capable of filtering and/or sanitizing user-input.

## Related Weaknesses (CWE)
- CWE-74
- CWE-113
- CWE-138
- CWE-436


---

# CAPEC-35: Leverage Executable Code in Non-Executable Files

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/35.html  

## Description
An attack of this type exploits a system's trust in configuration and resource files. When the executable loads the resource (such as an image file or configuration file) the attacker has modified the file to either execute malicious code directly or manipulate the target process (e.g. application server) to execute based on the malicious configuration parameters. Since systems are increasingly interrelated mashing up resources from local and remote sources the possibility of this attack occurring is high.

## Related Attack Patterns
- ChildOf: CAPEC-636
- PeerOf: CAPEC-23
- PeerOf: CAPEC-75

## Prerequisites
- The attacker must have the ability to modify non-executable files consumed by the target software.

## Skills Required
- [Low] To identify and execute against an over-privileged system interface

## Resources Required
- Ability to communicate synchronously or asynchronously with server that publishes an over-privileged directory, program, or interface. Optionally, ability to capture output directly through synchronous communication or other method such as FTP.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Design: Enforce principle of least privilege
- Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.
- Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.
- Implementation: Implement host integrity monitoring to detect any unwanted altering of configuration files.
- Implementation: Ensure that files that are not required to execute, such as configuration files, are not over-privileged, i.e. not allowed to execute.

## Related Weaknesses (CWE)
- CWE-94
- CWE-96
- CWE-95
- CWE-97
- CWE-272
- CWE-59
- CWE-282
- CWE-270


---

# CAPEC-36: Using Unpublished Interfaces or Functionality

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/36.html  

## Description
An adversary searches for and invokes interfaces or functionality that the target system designers did not intend to be publicly available. If interfaces fail to authenticate requests, the attacker may be able to invoke functionality they are not authorized for.

## Related Attack Patterns
- ChildOf: CAPEC-113

## Prerequisites
- The architecture under attack must publish or otherwise make available services that clients can attach to, either in an unauthenticated fashion, or having obtained an authentication token elsewhere. The service need not be 'discoverable', but in the event it isn't it must have some way of being discovered by an attacker. This might include listening on a well-known port. Ultimately, the likelihood of exploit depends on discoverability of the vulnerable service.

## Skills Required
- [Low] A number of web service digging tools are available for free that help discover exposed web services and their interfaces. In the event that a web service is not listed, the attacker does not need to know much more in addition to the format of web service messages that they can sniff/monitor for.

## Resources Required
- None: No specialized resources are required to execute this type of attack. Web service digging tools may be helpful.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Authenticating both services and their discovery, and protecting that authentication mechanism simply fixes the bulk of this problem. Protecting the authentication involves the standard means, including: 1) protecting the channel over which authentication occurs, 2) preventing the theft, forgery, or prediction of authentication credentials or the resultant tokens, or 3) subversion of password reset and the like.

## Related Weaknesses (CWE)
- CWE-306
- CWE-693
- CWE-695
- CWE-1242


---

# CAPEC-37: Retrieve Embedded Sensitive Data

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/37.html  

## Description
An attacker examines a target system to find sensitive data that has been embedded within it. This information can reveal confidential contents, such as account numbers or individual keys/credentials that can be used as an intermediate step in a larger attack.

## Related Attack Patterns
- ChildOf: CAPEC-167

## Prerequisites
- In order to feasibly execute this type of attack, some valuable data must be present in client software.
- Additionally, this information must be unprotected, or protected in a flawed fashion, or through a mechanism that fails to resist reverse engineering, statistical, or other attack.

## Skills Required
- [Medium] The attacker must possess knowledge of client code structure as well as ability to reverse-engineer or decompile it or probe it in other ways. This knowledge is specific to the technology and language used for the client distribution

## Resources Required
- The attacker must possess access to the system or code being exploited. Such access, for this set of attacks, will likely be physical. The attacker will make use of reverse engineering technologies, perhaps for data or to extract functionality from the binary. Such tool use may be as simple as "Strings" or a hex editor. Removing functionality may require the use of only a hex editor, or may require aspects of the toolchain used to construct the application: for instance the Adobe Flash development environment. Attacks of this nature do not require network access or undue CPU, memory, or other hardware-based resources.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Related Weaknesses (CWE)
- CWE-226
- CWE-311
- CWE-525
- CWE-312
- CWE-314
- CWE-315
- CWE-318
- CWE-1239
- CWE-1258
- CWE-1266
- CWE-1272
- CWE-1278
- CWE-1301
- CWE-1330


---

# CAPEC-38: Leveraging/Manipulating Configuration File Search Paths

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/38.html  

## Description
This pattern of attack sees an adversary load a malicious resource into a program's standard path so that when a known command is executed then the system instead executes the malicious component. The adversary can either modify the search path a program uses, like a PATH variable or classpath, or they can manipulate resources on the path to point to their malicious components. J2EE applications and other component based applications that are built from multiple binaries can have very long list of dependencies to execute. If one of these libraries and/or references is controllable by the attacker then application controls can be circumvented by the attacker.

## Related Attack Patterns
- ChildOf: CAPEC-159

## Prerequisites
- The attacker must be able to write to redirect search paths on the victim host.

## Skills Required
- [Low] To identify and execute against an over-privileged system interface

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Design: Enforce principle of least privilege
- Design: Ensure that the program's compound parts, including all system dependencies, classpath, path, and so on, are secured to the same or higher level assurance as the program
- Implementation: Host integrity monitoring

## Related Weaknesses (CWE)
- CWE-426
- CWE-427


---

# CAPEC-383: Harvesting Information via API Event Monitoring

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/383.html  

## Description
An adversary hosts an event within an application framework and then monitors the data exchanged during the course of the event for the purpose of harvesting any important data leaked during the transactions. One example could be harvesting lists of usernames or userIDs for the purpose of sending spam messages to those users. One example of this type of attack involves the adversary creating an event within the sub-application. Assume the adversary hosts a "virtual sale" of rare items. As other users enter the event, the attacker records via AiTM (CAPEC-94) proxy the user_ids and usernames of everyone who attends. The adversary would then be able to spam those users within the application using an automated script.

## Related Attack Patterns
- ChildOf: CAPEC-407
- CanPrecede: CAPEC-94

## Prerequisites
- The target software is utilizing application framework APIs

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Leverage encryption techniques during information transactions so as to protect them from attack patterns of this kind.

## Related Weaknesses (CWE)
- CWE-311
- CWE-319
- CWE-419
- CWE-602


---

# CAPEC-384: Application API Message Manipulation via Man-in-the-Middle

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/384.html  

## Description
An attacker manipulates either egress or ingress data from a client within an application framework in order to change the content of messages. Performing this attack can allow the attacker to gain unauthorized privileges within the application, or conduct attacks such as phishing, deceptive strategies to spread malware, or traditional web-application attacks. The techniques require use of specialized software that allow the attacker to perform adversary-in-the-middle (CAPEC-94) communications between the web browser and the remote system. Despite the use of AiTH software, the attack is actually directed at the server, as the client is one node in a series of content brokers that pass information along to the application framework. Additionally, it is not true "Adversary-in-the-Middle" attack at the network layer, but an application-layer attack the root cause of which is the master applications trust in the integrity of code supplied by the client.

## Related Attack Patterns
- ChildOf: CAPEC-94

## Prerequisites
- Targeted software is utilizing application framework APIs

## Resources Required
- A software program that allows a user to man-in-the-middle communications between the client and server, such as a man-in-the-middle proxy.

## Related Weaknesses (CWE)
- CWE-471
- CWE-345
- CWE-346
- CWE-602
- CWE-311


---

# CAPEC-385: Transaction or Event Tampering via Application API Manipulation

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/385.html  

## Description
An attacker hosts or joins an event or transaction within an application framework in order to change the content of messages or items that are being exchanged. Performing this attack allows the attacker to manipulate content in such a way as to produce messages or content that look authentic but may contain deceptive links, substitute one item or another, spoof an existing item and conduct a false exchange, or otherwise change the amounts or identity of what is being exchanged. The techniques require use of specialized software that allow the attacker to man-in-the-middle communications between the web browser and the remote system in order to change the content of various application elements. Often, items exchanged in game can be monetized via sales for coin, virtual dollars, etc. The purpose of the attack is for the attack to scam the victim by trapping the data packets involved the exchange and altering the integrity of the transfer process.

## Related Attack Patterns
- ChildOf: CAPEC-384

## Prerequisites
- Targeted software is utilizing application framework APIs

## Resources Required
- A software program that allows the use of adversary-in-the-middle communications (CAPEC-94) between the client and server, such as a man-in-the-middle proxy.

## Related Weaknesses (CWE)
- CWE-471
- CWE-345
- CWE-346
- CWE-602
- CWE-311


---

# CAPEC-386: Application API Navigation Remapping

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/386.html  

## Description
An attacker manipulates either egress or ingress data from a client within an application framework in order to change the destination and/or content of links/buttons displayed to a user within API messages. Performing this attack allows the attacker to manipulate content in such a way as to produce messages or content that looks authentic but contains links/buttons that point to an attacker controlled destination. Some applications make navigation remapping more difficult to detect because the actual HREF values of images, profile elements, and links/buttons are masked. One example would be to place an image in a user's photo gallery that when clicked upon redirected the user to an off-site location. Also, traditional web vulnerabilities (such as CSRF) can be constructed with remapped buttons or links. In some cases navigation remapping can be used for Phishing attacks or even means to artificially boost the page view, user site reputation, or click-fraud.

## Related Attack Patterns
- ChildOf: CAPEC-94

## Prerequisites
- Targeted software is utilizing application framework APIs

## Resources Required
- A software program that allows the use of adversary-in-the-middle (CAPEC-94) communications between the client and server, such as a man-in-the-middle proxy.

## Related Weaknesses (CWE)
- CWE-471
- CWE-345
- CWE-346
- CWE-602
- CWE-311


---

# CAPEC-387: Navigation Remapping To Propagate Malicious Content

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/387.html  

## Description
An adversary manipulates either egress or ingress data from a client within an application framework in order to change the content of messages and thereby circumvent the expected application logic.

## Related Attack Patterns
- ChildOf: CAPEC-386

## Prerequisites
- Targeted software is utilizing application framework APIs

## Resources Required
- A software program that allows the use of adversary-in-the-middle communications between the client and server, such as a man-in-the-middle proxy.

## Related Weaknesses (CWE)
- CWE-471
- CWE-345
- CWE-346
- CWE-602
- CWE-311


---

# CAPEC-388: Application API Button Hijacking

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/388.html  

## Description
An attacker manipulates either egress or ingress data from a client within an application framework in order to change the destination and/or content of buttons displayed to a user within API messages. Performing this attack allows the attacker to manipulate content in such a way as to produce messages or content that looks authentic but contains buttons that point to an attacker controlled destination.

## Related Attack Patterns
- ChildOf: CAPEC-386

## Prerequisites
- Targeted software is utilizing application framework APIs

## Resources Required
- A software program that allows the use of adversary-in-the-middle (CAPEC-94) communications between the client and server, such as a adversary-in-the-middle (CAPEC-94) proxy.

## Related Weaknesses (CWE)
- CWE-471
- CWE-345
- CWE-346
- CWE-602
- CWE-311


---

# CAPEC-389: Content Spoofing Via Application API Manipulation

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/389.html  

## Description
An attacker manipulates either egress or ingress data from a client within an application framework in order to change the content of messages. Performing this attack allows the attacker to manipulate content in such a way as to produce messages or content that look authentic but may contain deceptive links, spam-like content, or links to the attackers' code. In general, content-spoofing within an application API can be employed to stage many different types of attacks varied based on the attackers' intent. The techniques require use of specialized software that allow the attacker to use adversary-in-the-middle (CAPEC-94) communications between the web browser and the remote system.

## Related Attack Patterns
- ChildOf: CAPEC-384

## Prerequisites
- Targeted software is utilizing application framework APIs

## Resources Required
- A software program that allows the use of adversary-in-the-middle communications between the client and server, such as an adversary-in-the-middle proxy.

## Related Weaknesses (CWE)
- CWE-353


---

# CAPEC-39: Manipulating Opaque Client-based Data Tokens

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/39.html  

## Description
In circumstances where an application holds important data client-side in tokens (cookies, URLs, data files, and so forth) that data can be manipulated. If client or server-side application components reinterpret that data as authentication tokens or data (such as store item pricing or wallet information) then even opaquely manipulating that data may bear fruit for an Attacker. In this pattern an attacker undermines the assumption that client side tokens have been adequately protected from tampering through use of encryption or obfuscation.

## Related Attack Patterns
- ChildOf: CAPEC-22

## Prerequisites
- An attacker already has some access to the system or can steal the client based data tokens from another user who has access to the system.
- For an Attacker to viably execute this attack, some data (later interpreted by the application) must be held client-side in a way that can be manipulated without detection. This means that the data or tokens are not CRCd as part of their value or through a separate meta-data store elsewhere.

## Skills Required
- [Medium] If the client site token is obfuscated.
- [High] If the client site token is encrypted.

## Resources Required
- The Attacker needs no special hardware-based resources in order to conduct this attack. Software plugins, such as Tamper Data for Firefox, may help in manipulating URL- or cookie-based data.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- One solution to this problem is to protect encrypted data with a CRC of some sort. If knowing who last manipulated the data is important, then using a cryptographic "message authentication code" (or hMAC) is prescribed. However, this guidance is not a panacea. In particular, any value created by (and therefore encrypted by) the client, which itself is a "malicious" value, all the protective cryptography in the world can't make the value 'correct' again. Put simply, if the client has control over the whole process of generating and encoding the value, then simply protecting its integrity doesn't help.
- Make sure to protect client side authentication tokens for confidentiality (encryption) and integrity (signed hash)
- Make sure that all session tokens use a good source of randomness
- Perform validation on the server side to make sure that client side data tokens are consistent with what is expected.

## Related Weaknesses (CWE)
- CWE-353
- CWE-285
- CWE-302
- CWE-472
- CWE-565
- CWE-315
- CWE-539
- CWE-384
- CWE-233


---

# CAPEC-390: Bypassing Physical Security

**Abstraction:** Meta  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/390.html  

## Description
Facilities often used layered models for physical security such as traditional locks, Electronic-based card entry systems, coupled with physical alarms. Hardware security mechanisms range from the use of computer case and cable locks as well as RFID tags for tracking computer assets. This layered approach makes it difficult for random physical security breaches to go unnoticed, but is less effective at stopping deliberate and carefully planned break-ins. Avoiding detection begins with evading building security and surveillance and methods for bypassing the electronic or physical locks which secure entry points.


---

# CAPEC-391: Bypassing Physical Locks

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/391.html  

## Description
An attacker uses techniques and methods to bypass physical security measures of a building or facility. Physical locks may range from traditional lock and key mechanisms, cable locks used to secure laptops or servers, locks on server cases, or other such devices. Techniques such as lock bumping, lock forcing via snap guns, or lock picking can be employed to bypass those locks and gain access to the facilities or devices they protect, although stealth, evidence of tampering, and the integrity of the lock following an attack, are considerations that may determine the method employed. Physical locks are limited by the complexity of the locking mechanism. While some locks may offer protections such as shock resistant foam to prevent bumping or lock forcing methods, many commonly employed locks offer no such countermeasures.

## Related Attack Patterns
- ChildOf: CAPEC-390


---

# CAPEC-392: Lock Bumping

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/392.html  

## Description
An attacker uses a bump key to force a lock on a building or facility and gain entry. Lock Bumping is the use of a special type of key that can be tapped or bumped to cause the pins within the lock to fall into temporary alignment, allowing the lock to be opened. Lock bumping allows an attacker to open a lock without having the correct key. A standard lock is secured by a set of internal pins that prevent the device from turning. Spring loaded driver pins push down on the key pins. When the correct key is inserted, the ridges on the key push the key pins up and against the driver pins, causing correct alignment which allows the lock cylinder to rotate. A bump key is a specially constructed key that exploits this design. When the bump key is struck or firmly tapped, its teeth transfer the force of the tap into the key pins, causing the lock to momentarily shift into proper alignment for the mechanism to be opened.

## Related Attack Patterns
- ChildOf: CAPEC-391


---

# CAPEC-393: Lock Picking

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/393.html  

## Description
An attacker uses lock picking tools and techniques to bypass the locks on a building or facility. Lock picking is the use of a special set of tools to manipulate the pins within a lock. Different sets of tools are required for each type of lock. Lock picking attacks have the advantage of being non-invasive in that if performed correctly the lock will not be damaged. A standard lock pin-and-tumbler lock is secured by a set of internal pins that prevent the tumbler device from turning. Spring loaded driver pins push down on the key pins preventing rotation so that the bolt remains in a locked position.. When the correct key is inserted, the ridges on the key push the key pins up and against the driver pins, causing correct alignment which allows the lock cylinder to rotate. Most common locks, such as domestic locks in the US, can be picked using a standard 2 tools (i.e. a torsion wrench and a hook pick).

## Related Attack Patterns
- ChildOf: CAPEC-391


---

# CAPEC-394: Using a Snap Gun Lock to Force a Lock

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/394.html  

## Description
An attacker uses a Snap Gun, also known as a Pick Gun, to force the lock on a building or facility. A Pick Gun is a special type of lock picking instrument that works on similar principles as lock bumping. A snap gun is a hand-held device with an attached metal pick. The metal pick strikes the pins within the lock, transferring motion from the key pins to the driver pins and forcing the lock into momentary alignment. A standard lock is secured by a set of internal pins that prevent the device from turning. Spring loaded driver pins push down on the key pins. When the correct key is inserted, the ridges on the key push the key pins up and against the driver pins, causing correct alignment which allows the lock cylinder to rotate. A Snap Gun exploits this design by using a metal pin to strike all of the key pins at once, forcing the driver pins to shift into an unlocked position. Unlike bump keys or lock picks, a Snap Gun may damage the lock more easily, leaving evidence that the lock has been tampered with.

## Related Attack Patterns
- ChildOf: CAPEC-391


---

# CAPEC-395: Bypassing Electronic Locks and Access Controls

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/395.html  

## Description
An attacker exploits security assumptions to bypass electronic locks or other forms of access controls. Most attacks against electronic access controls follow similar methods but utilize different tools. Some electronic locks utilize magnetic strip cards, others employ RFID tags embedded within a card or badge, or may involve more sophisticated protections such as voice-print, thumb-print, or retinal biometrics. Magnetic Strip and RFID technologies are the most widespread because they are cost effective to deploy and more easily integrated with other electronic security measures. These technologies share common weaknesses that an attacker can exploit to gain access to a facility protected by the mechanisms via copying legitimate cards or badges, or generating new cards using reverse-engineered algorithms.

## Related Attack Patterns
- ChildOf: CAPEC-390


---

# CAPEC-396: DEPRECATED: Bypassing Card or Badge-Based Systems

**Abstraction:** Standard  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/396.html  

## Description
This attack pattern has been deprecated as it a generalization of CAPEC-397: Cloning Magnetic Strip Cards, CAPEC-398: Magnetic Strip Card Brute Force Attacks, CAPEC-399: Cloning RFID Cards or Chips and CAPEC-400: RFID Chip Deactivation or Destruction. Please refer to these CAPECs going forward.


---

# CAPEC-397: Cloning Magnetic Strip Cards

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/397.html  

## Description
An attacker duplicates the data on a Magnetic strip card (i.e. 'swipe card' or 'magstripe') to gain unauthorized access to a physical location or a person's private information. Magstripe cards encode data on a band of iron-based magnetic particles arrayed in a stripe along a rectangular card. Most magstripe card data formats conform to ISO standards 7810, 7811, 7813, 8583, and 4909. The primary advantage of magstripe technology is ease of encoding and portability, but this also renders magnetic strip cards susceptible to unauthorized duplication. If magstripe cards are used for access control, all an attacker need do is obtain a valid card long enough to make a copy of the card and then return the card to its location (i.e. a co-worker's desk). Magstripe reader/writers are widely available as well as software for analyzing data encoded on the cards. By swiping a valid card, it becomes trivial to make any number of duplicates that function as the original.

## Related Attack Patterns
- ChildOf: CAPEC-395


---

# CAPEC-398: Magnetic Strip Card Brute Force Attacks

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/398.html  

## Description
An adversary analyzes the data on two or more magnetic strip cards and is able to generate new cards containing valid sequences that allow unauthorized access and/or impersonation of individuals.

## Related Attack Patterns
- ChildOf: CAPEC-395

## Prerequisites
- The ability to calculate a card checksum and write out a valid checksum value. Some cards are protected by a checksum calculation, therefore it is necessary to determine what algorithm is being used to calculate the checksum and to employ that algorithm to calculate and write a new valid checksum for the card being created.


---

# CAPEC-399: Cloning RFID Cards or Chips

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/399.html  

## Description
An attacker analyzes data returned by an RFID chip and uses this information to duplicate a RFID signal that responds identically to the target chip. In some cases RFID chips are used for building access control, employee identification, or as markers on products being delivered along a supply chain. Some organizations also embed RFID tags inside computer assets to trigger alarms if they are removed from particular rooms, zones, or buildings. Similar to Magnetic strip cards, RFID cards are susceptible to duplication (cloning) and reuse.

## Related Attack Patterns
- ChildOf: CAPEC-395


---

# CAPEC-4: Using Alternative IP Address Encodings

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/4.html  

## Description
This attack relies on the adversary using unexpected formats for representing IP addresses. Networked applications may expect network location information in a specific format, such as fully qualified domains names (FQDNs), URL, IP address, or IP Address ranges. If the location information is not validated against a variety of different possible encodings and formats, the adversary can use an alternate format to bypass application access control.

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- The target software must fail to anticipate all of the possible valid encodings of an IP/web address.
- The adversary must have the ability to communicate with the server.

## Skills Required
- [Low] The adversary has only to try IP address format combinations.

## Resources Required
- The adversary needs to have knowledge of an alternative IP address encoding that bypasses the access control policy of an application. Alternatively, the adversary can simply try to brute-force various encoding possibilities.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Design: Default deny access control policies
- Design: Input validation routines should check and enforce both input data types and content against a positive specification. In regards to IP addresses, this should include the authorized manner for the application to represent IP addresses and not accept user specified IP addresses and IP address formats (such as ranges)
- Implementation: Perform input validation for all remote content.

## Related Weaknesses (CWE)
- CWE-291
- CWE-173


---

# CAPEC-40: Manipulating Writeable Terminal Devices

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/40.html  

## Description
This attack exploits terminal devices that allow themselves to be written to by other users. The attacker sends command strings to the target terminal device hoping that the target user will hit enter and thereby execute the malicious command with their privileges. The attacker can send the results (such as copying /etc/passwd) to a known directory and collect once the attack has succeeded.

## Related Attack Patterns
- ChildOf: CAPEC-248

## Prerequisites
- User terminals must have a permissive access control such as world writeable that allows normal users to control data on other user's terminals.

## Skills Required
- [Low] Ability to discover permissions on terminal devices. Of course, brute force can also be used.

## Resources Required
- Access to a terminal on the target network

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Design: Ensure that terminals are only writeable by named owner user and/or administrator
- Design: Enforce principle of least privilege

## Related Weaknesses (CWE)
- CWE-77


---

# CAPEC-400: RFID Chip Deactivation or Destruction

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/400.html  

## Description
An attacker uses methods to deactivate a passive RFID tag for the purpose of rendering the tag, badge, card, or object containing the tag unresponsive. RFID tags are used primarily for access control, inventory, or anti-theft devices. The purpose of attacking the RFID chip is to disable or damage the chip without causing damage to the object housing it.

## Related Attack Patterns
- ChildOf: CAPEC-395


---

# CAPEC-401: Physically Hacking Hardware

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/401.html  

## Description
An adversary exploits a weakness in access control to gain access to currently installed hardware and precedes to implement changes or secretly replace a hardware component which undermines the system's integrity for the purpose of carrying out an attack.

## Related Attack Patterns
- ChildOf: CAPEC-440

## Related Weaknesses (CWE)
- CWE-1263


---

# CAPEC-402: Bypassing ATA Password Security

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/402.html  

## Description
An adversary exploits a weakness in ATA security on a drive to gain access to the information the drive contains without supplying the proper credentials. ATA Security is often employed to protect hard disk information from unauthorized access. The mechanism requires the user to type in a password before the BIOS is allowed access to drive contents. Some implementations of ATA security will accept the ATA command to update the password without the user having authenticated with the BIOS. This occurs because the security mechanism assumes the user has first authenticated via the BIOS prior to sending commands to the drive. Various methods exist for exploiting this flaw, the most common being installing the ATA protected drive into a system lacking ATA security features (a.k.a. hot swapping). Once the drive is installed into the new system the BIOS can be used to reset the drive password.

## Related Attack Patterns
- ChildOf: CAPEC-401

## Prerequisites
- Access to the system containing the ATA Drive so that the drive can be physically removed from the system.

## Mitigations
- Avoid using ATA password security when possible.
- Use full disk encryption to protect the entire contents of the drive or sensitive partitions on the drive.
- Leverage third-party utilities that interface with self-encrypting drives (SEDs) to provide authentication, while relying on the SED itself for data encryption.

## Related Weaknesses (CWE)
- CWE-285


---

# CAPEC-404: DEPRECATED: Social Information Gathering Attacks

**Abstraction:** Meta  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/404.html  

## Description
This attack pattern has been deprecated as it was deemed not to be a legitimate attack pattern. Please refer to CAPEC-118 : Collect and Analyze Information.


---

# CAPEC-405: DEPRECATED: Social Information Gathering via Research

**Abstraction:** Meta  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/405.html  

## Description
This attack pattern has been deprecated as it was deemed not to be a legitimate attack pattern. Please refer to CAPEC-118 : Collect and Analyze Information.


---

# CAPEC-406: Dumpster Diving

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/406.html  

## Description
An adversary cases an establishment and searches through trash bins, dumpsters, or areas where company information may have been accidentally discarded for information items which may be useful to the dumpster diver. The devastating nature of the items and/or information found can be anything from medical records, resumes, personal photos and emails, bank statements, account details or information about software, tech support logs and so much more, including hardware devices. By collecting this information an adversary may be able to learn important facts about the person or organization that play a role in helping the adversary in their attack.

## Related Attack Patterns
- ChildOf: CAPEC-150
- CanPrecede: CAPEC-163
- CanPrecede: CAPEC-675

## Prerequisites
- An adversary must have physical access to the dumpster or downstream processing facility.

## Consequences
- Scope: Confidentiality; Impact: Other


---

# CAPEC-407: Pretexting

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/407.html  

## Description
An adversary engages in pretexting behavior to solicit information from target persons, or manipulate the target into performing some action that serves the adversary's interests. During a pretexting attack, the adversary creates an invented scenario, assuming an identity or role to persuade a targeted victim to release information or perform some action. It is more than just creating a lie; in some cases it can be creating a whole new identity and then using that identity to manipulate the receipt of information.

## Related Attack Patterns
- ChildOf: CAPEC-416
- ChildOf: CAPEC-410
- CanPrecede: CAPEC-163

## Prerequisites
- The adversary must have the means and knowledge of how to communicate with the target in some manner.The adversary must have knowledge of the pretext that would influence the actions of the specific target.

## Skills Required
- [Low] The adversary requires strong inter-personal and communication skills.

## Consequences
- Scope: Confidentiality; Impact: Other

## Mitigations
- An organization should provide regular, robust cybersecurity training to its employees to prevent successful social engineering attacks.


---

# CAPEC-408: DEPRECATED: Information Gathering from Traditional Sources

**Abstraction:** Meta  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/408.html  

## Description
This attack pattern has been deprecated as it was deemed not to be a legitimate attack pattern. Please refer to CAPEC-118 : Collect and Analyze Information.


---

# CAPEC-409: DEPRECATED: Information Gathering from Non-Traditional Sources

**Abstraction:** Meta  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/409.html  

## Description
This attack pattern has been deprecated as it was deemed not to be a legitimate attack pattern. Please refer to CAPEC-118 : Collect and Analyze Information.


---

# CAPEC-41: Using Meta-characters in E-mail Headers to Inject Malicious Payloads

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/41.html  

## Description
This type of attack involves an attacker leveraging meta-characters in email headers to inject improper behavior into email programs. Email software has become increasingly sophisticated and feature-rich. In addition, email applications are ubiquitous and connected directly to the Web making them ideal targets to launch and propagate attacks. As the user demand for new functionality in email applications grows, they become more like browsers with complex rendering and plug in routines. As more email functionality is included and abstracted from the user, this creates opportunities for attackers. Virtually all email applications do not list email header information by default, however the email header contains valuable attacker vectors for the attacker to exploit particularly if the behavior of the email client application is known. Meta-characters are hidden from the user, but can contain scripts, enumerations, probes, and other attacks against the user's system.

## Related Attack Patterns
- ChildOf: CAPEC-242
- ChildOf: CAPEC-134

## Prerequisites
- This attack targets most widely deployed feature rich email applications, including web based email programs.

## Skills Required
- [Low] To distribute email

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Design: Perform validation on email header data
- Implementation: Implement email filtering solutions on mail server or on MTA, relay server.
- Implementation: Mail servers that perform strict validation may catch these attacks, because metacharacters are not allowed in many header variables such as dns names

## Related Weaknesses (CWE)
- CWE-150
- CWE-88
- CWE-697


---

# CAPEC-410: Information Elicitation

**Abstraction:** Meta  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/410.html  

## Description
An adversary engages an individual using any combination of social engineering methods for the purpose of extracting information. Accurate contextual and environmental queues, such as knowing important information about the target company or individual can greatly increase the success of the attack and the quality of information gathered. Authentic mimicry combined with detailed knowledge increases the success of elicitation attacks.


---

# CAPEC-411: DEPRECATED: Pretexting

**Abstraction:** Meta  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/411.html  

## Description
This attack pattern has been deprecated as it is a duplicate of the existing attack pattern "CAPEC-407 : Social Information Gathering via Pretexting". Please refer to this other CAPEC going forward.


---

# CAPEC-412: Pretexting via Customer Service

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/412.html  

## Description
An adversary engages in pretexting behavior, assuming the role of someone who works for Customer Service, to solicit information from target persons, or manipulate the target into performing an action that serves the adversary's interests. One example of a scenario such as this would be to call an individual, articulate your false affiliation with a credit card company, and then attempt to get the individual to verify their credit card number.

## Related Attack Patterns
- ChildOf: CAPEC-407


---

# CAPEC-413: Pretexting via Tech Support

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/413.html  

## Description
An adversary engages in pretexting behavior, assuming the role of a tech support worker, to solicit information from target persons, or manipulate the target into performing an action that serves the adversary's interests. An adversary who uses social engineering to impersonate a tech support worker can have devastating effects on a network. This is an effective attack vector, because it can give an adversary physical access to network computers. It only takes a matter of seconds for someone to compromise a computer with physical access. One of the best technological tools at the disposal of a social engineer, posing as a technical support person, is a USB thumb drive. These are small, easy to conceal, and can be loaded with different payloads depending on what task needs to be done. However, this form of attack does not require physical access as it can also be effectively carried out via phone or email.

## Related Attack Patterns
- ChildOf: CAPEC-407


---

# CAPEC-414: Pretexting via Delivery Person

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/414.html  

## Description
An adversary engages in pretexting behavior, assuming the role of a delivery person, to solicit information from target persons, or manipulate the target into performing an action that serves the adversary's interests. Impersonating a delivery person is an effective attack and an easy attack since not much acting is involved. Usually the hardest part is looking the part and having all of the proper credentials, papers and "deliveries" in order to be able to pull it off.

## Related Attack Patterns
- ChildOf: CAPEC-407


---

# CAPEC-415: Pretexting via Phone

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/415.html  

## Description
An adversary engages in pretexting behavior, assuming some sort of trusted role, and contacting the targeted individual or organization via phone to solicit information from target persons, or manipulate the target into performing an action that serves the adversary's interests. This is the most common social engineering attack. Some of the most commonly effective approaches are to impersonate a fellow employee, impersonate a computer technician or to target help desk personnel.

## Related Attack Patterns
- ChildOf: CAPEC-407


---

# CAPEC-416: Manipulate Human Behavior

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/416.html  

## Description
An adversary exploits inherent human psychological predisposition to influence a targeted individual or group to solicit information or manipulate the target into performing an action that serves the adversary's interests. Many interpersonal social engineering techniques do not involve outright deception, although they can; many are subtle ways of manipulating a target to remove barriers, make the target feel comfortable, and produce an exchange in which the target is either more likely to share information directly, or let key information slip out unintentionally. A skilled adversary uses these techniques when appropriate to produce the desired outcome. Manipulation techniques vary from the overt, such as pretending to be a supervisor to a help desk, to the subtle, such as making the target feel comfortable with the adversary's speech and thought patterns.

## Prerequisites
- The adversary must have the means and knowledge of how to communicate with the target in some manner.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- An organization should provide regular, robust cybersecurity training to its employees to prevent successful social engineering attacks.


---

# CAPEC-417: Influence Perception

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/417.html  

## Description
The adversary uses social engineering to exploit the target's perception of the relationship between the adversary and themselves. This goal is to persuade the target to unknowingly perform an action or divulge information that is advantageous to the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-416

## Prerequisites
- The adversary must have the means and knowledge of how to communicate with the target in some manner.

## Skills Required
- [Low] The adversary requires strong inter-personal and communication skills.

## Resources Required
- There are no necessary resources required for this attack.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- An organization should provide regular, robust cybersecurity training to its employees to prevent social engineering attacks.


---

# CAPEC-418: Influence Perception of Reciprocation

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/418.html  

## Description
An adversary uses a social engineering techniques to produce a sense of obligation in the target to perform a certain action or concede some sensitive or key piece of information. Obligation has to do with actions one feels they need to take due to some sort of social, legal, or moral requirement, duty, contract, or promise. There are various techniques for fostering a sense of obligation to reciprocate or concede during ordinary modes of communication. One method is to compliment the target, and follow up the compliment with a question. If performed correctly the target may volunteer a key piece of information, sometimes involuntarily.

## Related Attack Patterns
- ChildOf: CAPEC-417

## Prerequisites
- The adversary must have the means and knowledge of how to communicate with the target in some manner.

## Skills Required
- [Low] The adversary requires strong inter-personal and communication skills.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- An organization should provide regular, robust cybersecurity training to its employees to prevent social engineering attacks.


---

# CAPEC-419: DEPRECATED: Target Influence via Perception of Concession

**Abstraction:** Meta  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/419.html  

## Description
This attack pattern has been deprecated as it was deemed not to be a legitimate pattern.


---

# CAPEC-42: MIME Conversion

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/42.html  

## Description
An attacker exploits a weakness in the MIME conversion routine to cause a buffer overflow and gain control over the mail server machine. The MIME system is designed to allow various different information formats to be interpreted and sent via e-mail. Attack points exist when data are converted to MIME compatible format and back.

## Related Attack Patterns
- ChildOf: CAPEC-100

## Prerequisites
- The target system uses a mail server.
- Mail server vendor has not released a patch for the MIME conversion routine, the patch itself has a security hole or does not fix the original problem, or the patch has not been applied to the user's system.

## Skills Required
- [Low] It may be trivial to cause a DoS via this attack pattern
- [High] Causing arbitrary code to execute on the target system.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Stay up to date with third party vendor patches
- Disable the 7 to 8 bit conversion. This can be done by removing the F=9 flag from all Mailer specifications in the sendmail.cf file. For example, a sendmail.cf file with these changes applied should look similar to (depending on your system and configuration): Mlocal, P=/usr/libexec/mail.local, F=lsDFMAw5:/|@qrmn, S=10/30, R=20/40,T=DNS/RFC822/X-Unix,A=mail -d $u Mprog, P=/bin/sh, F=lsDFMoqeu, S=10/30, R=20/40,D=$z:/,T=X-Unix,A=sh -c $u This can be achieved for the "Mlocal" and "Mprog" Mailers by modifying the ".mc" file to include the following lines: define(`LOCAL_MAILER_FLAGS',ifdef(`LOCAL_MAILER_FLAGS',`translit(LOCAL_MAILER_FLAGS, `9')',`rmn')) define(`LOCAL_SHELL_FLAGS',ifdef(`LOCAL_SHELL_FLAGS',`translit(LOCAL_SHELL_FLAGS, `9')',`eu')) and then rebuilding the sendmail.cf file using m4(1). From "Exploiting Software", please see reference below.
- Use the sendmail restricted shell program (smrsh)
- Use mail.local

## Related Weaknesses (CWE)
- CWE-120
- CWE-119
- CWE-74
- CWE-20


---

# CAPEC-420: Influence Perception of Scarcity

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/420.html  

## Description
The adversary leverages a perception of scarcity to persuade the target to perform an action or divulge information that is advantageous to the adversary. By conveying a perception of scarcity, or a situation of limited supply, the adversary aims to create a sense of urgency in the context of a target's decision-making process.

## Related Attack Patterns
- ChildOf: CAPEC-417

## Prerequisites
- The adversary must have the means and knowledge of how to communicate with the target in some manner.

## Skills Required
- [Low] The adversary requires strong inter-personal and communication skills.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- An organization should provide regular, robust cybersecurity training to its employees to prevent social engineering attacks.


---

# CAPEC-421: Influence Perception of Authority

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/421.html  

## Description
An adversary uses a social engineering technique to convey a sense of authority that motivates the target to reveal specific information or take specific action. There are various techniques for producing a sense of authority during ordinary modes of communication. One common method is impersonation. By impersonating someone with a position of power within an organization, an adversary may motivate the target individual to reveal some piece of sensitive information or perform an action that benefits the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-417

## Prerequisites
- The adversary must have the means and knowledge of how to communicate with the target in some manner.

## Skills Required
- [Low] The adversary requires strong inter-personal and communication skills.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- An organization should provide regular, robust cybersecurity training to its employees to prevent social engineering attacks.


---

# CAPEC-422: Influence Perception of Commitment and Consistency

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/422.html  

## Description
An adversary uses social engineering to convince the target to do minor tasks as opposed to larger actions. After complying with a request, individuals are more likely to agree to subsequent requests that are similar in type and required effort.

## Related Attack Patterns
- ChildOf: CAPEC-417

## Prerequisites
- The adversary must have the means and knowledge of how to communicate with the target in some manner.

## Skills Required
- [Low] The adversary requires strong inter-personal and communication skills.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- An organization should provide regular, robust cybersecurity training to its employees to prevent social engineering attacks.
- Individuals should avoid complying with suspicious requests.


---

# CAPEC-423: Influence Perception of Liking

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/423.html  

## Description
The adversary influences the target's actions by building a relationship where the target has a liking to the adversary. People are more likely to be influenced by people of whom they are fond, so the adversary attempts to ingratiate themself with the target via actions, appearance, or a combination thereof.

## Related Attack Patterns
- ChildOf: CAPEC-417

## Prerequisites
- The adversary must have the means and knowledge of how to communicate with the target in some manner.The adversary must have knowledge of the types of things that the target likes.

## Skills Required
- [Low] The adversary requires strong inter-personal and communication skills.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- An organization should provide regular, robust cybersecurity training to its employees to prevent social engineering attacks.


---

# CAPEC-424: Influence Perception of Consensus or Social Proof

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/424.html  

## Description
The adversary influences the target's actions by leveraging the inherent human nature to assume behavior of others is appropriate. In situations of uncertainty, people tend to behave in ways they see others behaving. The adversary convinces the target of adopting behavior or actions that is advantageous to the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-417

## Prerequisites
- The adversary must have the means and knowledge of how to communicate with the target in some manner.

## Skills Required
- [Low] The adversary requires strong inter-personal and communication skills.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- An organization should provide regular, robust cybersecurity training to its employees to prevent social engineering attacks.


---

# CAPEC-425: Target Influence via Framing

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/425.html  

## Description
An adversary uses framing techniques to contextualize a conversation so that the target is more likely to be influenced by the adversary's point of view. Framing is information and experiences in life that alter the way we react to decisions we must make. This type of persuasive technique exploits the way people are conditioned to perceive data and its significance, while avoiding negative or avoidance responses from the target. Rather than a specific technique framing is a methodology of conversation that slowly encourages the target to adopt to the adversary's perspective. One technique of framing is to avoid the use of the word "No" and to contextualize responses in a manner that is positive. When performed skillfully the target is much more likely to volunteer information or perform actions favorable to the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-416

## Prerequisites
- The adversary must have the means and knowledge of how to communicate with the target in some manner.

## Skills Required
- [Low] The adversary requires strong inter-personal and communication skills.

## Consequences
- Scope: Confidentiality; Impact: Other

## Mitigations
- An organization should provide regular, robust cybersecurity training to its employees to prevent social engineering attacks.
- Avoid sharing unnecessary information during interactions beyond what is absolutely required for effective communication.


---

# CAPEC-426: Influence via Incentives

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/426.html  

## Description
The adversary incites a behavior from the target by manipulating something of influence. This is commonly associated with financial, social, or ideological incentivization. Examples include monetary fraud, peer pressure, and preying on the target's morals or ethics. The most effective incentive against one target might not be as effective against another, therefore the adversary must gather information about the target's vulnerability to particular incentives.

## Related Attack Patterns
- ChildOf: CAPEC-416

## Prerequisites
- The adversary must have the means and knowledge of how to communicate with the target in some manner.The adversary must have knowledge of the incentives that would influence the actions of the specific target.

## Skills Required
- [Low] The adversary requires strong inter-personal and communication skills.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- An organization should provide regular, robust cybersecurity training to its employees to prevent social engineering attacks.


---

# CAPEC-427: Influence via Psychological Principles

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/427.html  

## Description
The adversary shapes the target's actions or behavior by focusing on the ways human interact and learn, leveraging such elements as cognitive and social psychology. In a variety of ways, a target can be influenced to behave or perform an action through capitalizing on what scholarship and research has learned about how and why humans react to specific scenarios and cues.

## Related Attack Patterns
- ChildOf: CAPEC-416

## Prerequisites
- The adversary must have the means and knowledge of how to communicate with the target in some manner.

## Skills Required
- [Low] The adversary requires strong inter-personal and communication skills.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- An organization should provide regular, robust cybersecurity training to its employees to prevent social engineering attacks.


---

# CAPEC-428: Influence via Modes of Thinking

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/428.html  

## Description
The adversary tailors their communication to the language and thought patterns of the target thereby weakening barriers or reluctance to communication. This method is a way of building rapport with a target by matching their speech patterns and the primary ways or dominant senses with which they make abstractions. This technique can be used to make the target more receptive to sharing information because the adversary has adapted their communication forms to match those of the target. When skillfully employed, the target is likely to be unaware that they are being manipulated.

## Related Attack Patterns
- ChildOf: CAPEC-427


---

# CAPEC-429: Target Influence via Eye Cues

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/429.html  

## Description
The adversary gains information via non-verbal means from the target through eye movements.

## Related Attack Patterns
- ChildOf: CAPEC-427


---

# CAPEC-43: Exploiting Multiple Input Interpretation Layers

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/43.html  

## Description
An attacker supplies the target software with input data that contains sequences of special characters designed to bypass input validation logic. This exploit relies on the target making multiples passes over the input data and processing a "layer" of special characters with each pass. In this manner, the attacker can disguise input that would otherwise be rejected as invalid by concealing it with layers of special/escape characters that are stripped off by subsequent processing steps. The goal is to first discover cases where the input validation layer executes before one or more parsing layers. That is, user input may go through the following logic in an application: <parser1> --> <input validator> --> <parser2>. In such cases, the attacker will need to provide input that will pass through the input validator, but after passing through parser2, will be converted into something that the input validator was supposed to stop.

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- User input is used to construct a command to be executed on the target system or as part of the file name.
- Multiple parser passes are performed on the data supplied by the user.

## Skills Required
- [Medium] Knowledge of various escaping schemes, such as URL escape encoding and XML escape characters.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- An iterative approach to input validation may be required to ensure that no dangerous characters are present. It may be necessary to implement redundant checking across different input validation layers. Ensure that invalid data is rejected as soon as possible and do not continue to work with it.
- Make sure to perform input validation on canonicalized data (i.e. data that is data in its most standard form). This will help avoid tricky encodings getting past the filters.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist would not be permitted to enter into the system.

## Related Weaknesses (CWE)
- CWE-179
- CWE-181
- CWE-184
- CWE-183
- CWE-77
- CWE-78
- CWE-74
- CWE-20
- CWE-697
- CWE-707


---

# CAPEC-430: DEPRECATED:  Target Influence via Micro-Expressions

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/430.html  

## Description
This attack pattern has been deprecated.


---

# CAPEC-431: DEPRECATED:  Target Influence via Neuro-Linguistic Programming (NLP)

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/431.html  

## Description
This attack pattern has been deprecated.


---

# CAPEC-432: DEPRECATED:  Target Influence via Voice in NLP

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/432.html  

## Description
This attack pattern has been deprecated.


---

# CAPEC-433: Target Influence via The Human Buffer Overflow

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/433.html  

## Description
An attacker utilizes a technique to insinuate commands to the subconscious mind of the target via communication patterns. The human buffer overflow methodology does not rely on over-stimulating the mind of the target, but rather embedding messages within communication that the mind of the listener assembles at a subconscious level. The human buffer-overflow method is similar to subconscious programming to the extent that messages are embedded within the message.

## Related Attack Patterns
- ChildOf: CAPEC-427


---

# CAPEC-434: Target Influence via Interview and Interrogation

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/434.html  

## Related Attack Patterns
- ChildOf: CAPEC-427


---

# CAPEC-435: Target Influence via Instant Rapport

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/435.html  

## Related Attack Patterns
- ChildOf: CAPEC-427


---

# CAPEC-438: Modification During Manufacture

**Abstraction:** Meta  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/438.html  

## Description
An attacker modifies a technology, product, or component during a stage in its manufacture for the purpose of carrying out an attack against some entity involved in the supply chain lifecycle. There are an almost limitless number of ways an attacker can modify a technology when they are involved in its manufacture, as the attacker has potential inroads to the software composition, hardware design and assembly, firmware, or basic design mechanics. Additionally, manufacturing of key components is often outsourced with the final product assembled by the primary manufacturer. The greatest risk, however, is deliberate manipulation of design specifications to produce malicious hardware or devices. There are billions of transistors in a single integrated circuit and studies have shown that fewer than 10 transistors are required to create malicious functionality.


---

# CAPEC-439: Manipulation During Distribution

**Abstraction:** Meta  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/439.html  

## Description
An attacker undermines the integrity of a product, software, or technology at some stage of the distribution channel. The core threat of modification or manipulation during distribution arise from the many stages of distribution, as a product may traverse multiple suppliers and integrators as the final asset is delivered. Components and services provided from a manufacturer to a supplier may be tampered with during integration or packaging.

## Related Weaknesses (CWE)
- CWE-1269


---

# CAPEC-44: Overflow Binary Resource File

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/44.html  

## Description
An attack of this type exploits a buffer overflow vulnerability in the handling of binary resources. Binary resources may include music files like MP3, image files like JPEG files, and any other binary file. These attacks may pass unnoticed to the client machine through normal usage of files, such as a browser loading a seemingly innocent JPEG file. This can allow the adversary access to the execution stack and execute arbitrary code in the target process.

## Related Attack Patterns
- ChildOf: CAPEC-100
- ChildOf: CAPEC-23

## Prerequisites
- Target software processes binary resource files.
- Target software contains a buffer overflow vulnerability reachable through input from a user-controllable binary resource file.

## Skills Required
- [Medium] To modify file, deceive client into downloading, locate and exploit remote stack or heap vulnerability

## Consequences
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Perform appropriate bounds checking on all buffers.
- Design: Enforce principle of least privilege
- Design: Static code analysis
- Implementation: Execute program in less trusted process space environment, do not allow lower integrity processes to write to higher integrity processes
- Implementation: Keep software patched to ensure that known vulnerabilities are not available for adversaries to target on host.

## Related Weaknesses (CWE)
- CWE-120
- CWE-119
- CWE-697


---

# CAPEC-440: Hardware Integrity Attack

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/440.html  

## Description
An adversary exploits a weakness in the system maintenance process and causes a change to be made to a technology, product, component, or sub-component or a new one installed during its deployed use at the victim location for the purpose of carrying out an attack.

## Prerequisites
- Influence over the deployed system at a victim location.

## Consequences
- Scope: Integrity; Impact: Execute Unauthorized Commands


---

# CAPEC-441: Malicious Logic Insertion

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/441.html  

## Description
An adversary installs or adds malicious logic (also known as malware) into a seemingly benign component of a fielded system. This logic is often hidden from the user of the system and works behind the scenes to achieve negative impacts. With the proliferation of mass digital storage and inexpensive multimedia devices, Bluetooth and 802.11 support, new attack vectors for spreading malware are emerging for things we once thought of as innocuous greeting cards, picture frames, or digital projectors. This pattern of attack focuses on systems already fielded and used in operation as opposed to systems and their components that are still under development and part of the supply chain.

## Prerequisites
- Access to the component currently deployed at a victim location.

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Related Weaknesses (CWE)
- CWE-284


---

# CAPEC-442: Infected Software

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/442.html  

## Description
An adversary adds malicious logic, often in the form of a computer virus, to otherwise benign software. This logic is often hidden from the user of the software and works behind the scenes to achieve negative impacts. Many times, the malicious logic is inserted into empty space between legitimate code, and is then called when the software is executed. This pattern of attack focuses on software already fielded and used in operation as opposed to software that is still under development and part of the supply chain.

## Related Attack Patterns
- ChildOf: CAPEC-441

## Prerequisites
- Access to the software currently deployed at a victim location. This access is often obtained by leveraging another attack pattern to gain permissions that the adversary wouldn't normally have.

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Leverage anti-virus products to detect and quarantine software with known virus.

## Related Weaknesses (CWE)
- CWE-506


---

# CAPEC-443: Malicious Logic Inserted Into Product by Authorized Developer

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/443.html  

## Description
An adversary uses their privileged position within an authorized development organization to inject malicious logic into a codebase or product.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- Access to the product during the initial or continuous development.

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Assess software and hardware during development and prior to deployment to ensure that it functions as intended and without any malicious functionality. This includes both initial development, as well as updates propagated to the product after deployment.


---

# CAPEC-444: Development Alteration

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/444.html  

## Description
An adversary modifies a technology, product, or component during its development to acheive a negative impact once the system is deployed. The goal of the adversary is to modify the system in such a way that the negative impact can be leveraged when the system is later deployed. Development alteration attacks may include attacks that insert malicious logic into the system's software, modify or replace hardware components, and other attacks which negatively impact the system during development. These attacks generally require insider access to modify source code or to tamper with hardware components. The product is then delivered to the user where the negative impact can be leveraged at a later time.

## Related Attack Patterns
- ChildOf: CAPEC-438

## Prerequisites
- Access to the system during the development phase to alter and/or modify software and hardware components. This access is often obtained via insider access or by leveraging another attack pattern to gain permissions that the adversary wouldn't normally have.

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Availability; Impact: Unreliable Execution
- Scope: Integrity; Impact: Alter Execution Logic

## Mitigations
- Assess software and software components during development and prior to deployment to ensure that they function as intended and without any malicious functionality.


---

# CAPEC-445: Malicious Logic Insertion into Product Software via Configuration Management Manipulation

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/445.html  

## Description
An adversary exploits a configuration management system so that malicious logic is inserted into a software products build, update or deployed environment. If an adversary can control the elements included in a product's configuration management for build they can potentially replace, modify or insert code files containing malicious logic. If an adversary can control elements of a product's ongoing operational configuration management baseline they can potentially force clients receiving updates from the system to install insecure software when receiving updates from the server.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- Access to the configuration management system during deployment or currently deployed at a victim location. This access is often obtained via insider access or by leveraging another attack pattern to gain permissions that the adversary wouldn't normally have.

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Assess software during development and prior to deployment to ensure that it functions as intended and without any malicious functionality.
- Leverage anti-virus products to detect and quarantine software with known virus.


---

# CAPEC-446: Malicious Logic Insertion into Product via Inclusion of Third-Party Component

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/446.html  

## Description
An adversary conducts supply chain attacks by the inclusion of insecure third-party components into a technology, product, or code-base, possibly packaging a malicious driver or component along with the product before shipping it to the consumer or acquirer.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- Access to the product during the initial or continuous development. This access is often obtained via insider access to include the third-party component after deployment.

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Assess software and hardware during development and prior to deployment to ensure that it functions as intended and without any malicious functionality. This includes both initial development, as well as updates propagated to the product after deployment.
- Don't assume popular third-party components are free from malware or vulnerabilities. For software, assess for malicious functionality via update/commit reviews or automated static/dynamic analysis prior to including the component within the application and deploying in a production environment.


---

# CAPEC-447: Design Alteration

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/447.html  

## Description
An adversary modifies the design of a technology, product, or component to acheive a negative impact once the system is deployed. In this type of attack, the goal of the adversary is to modify the design of the system, prior to development starting, in such a way that the negative impact can be leveraged when the system is later deployed. Design alteration attacks differ from development alteration attacks in that design alteration attacks take place prior to development and which then may or may not be developed by the adverary. Design alteration attacks include modifying system designs to degrade system performance, cause unexpected states or errors, and general design changes that may lead to additional vulnerabilities. These attacks generally require insider access to modify design documents, but they may also be spoofed via web communications. The product is then developed and delivered to the user where the negative impact can be leveraged at a later time.

## Related Attack Patterns
- ChildOf: CAPEC-438

## Prerequisites
- Access to system design documentation prior to the development phase. This access is often obtained via insider access or by leveraging another attack pattern to gain permissions that the adversary wouldn't normally have.
- Ability to forge web communications to deliver modified design documentation.

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Availability; Impact: Unreliable Execution
- Scope: Integrity; Impact: Alter Execution Logic

## Mitigations
- Assess design documentation prior to development to ensure that they function as intended and without any malicious functionality.
- Ensure that design documentation is saved in a secure location and has proper access controls set in place to avoid unnecessary modification.


---

# CAPEC-448: Embed Virus into DLL

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/448.html  

## Description
An adversary tampers with a DLL and embeds a computer virus into gaps between legitimate machine instructions. These gaps may be the result of compiler optimizations that pad memory blocks for performance gains. The embedded virus then attempts to infect any machine which interfaces with the product, and possibly steal private data or eavesdrop.

## Related Attack Patterns
- ChildOf: CAPEC-442

## Prerequisites
- Access to the software currently deployed at a victim location. This access is often obtained by leveraging another attack pattern to gain permissions that the adversary wouldn't normally have.

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Leverage anti-virus products to detect and quarantine software with known virus.

## Related Weaknesses (CWE)
- CWE-506


---

# CAPEC-449: DEPRECATED: Malware Propagation via USB Stick

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/449.html  

## Description
This attack pattern has been deprecated as it is a duplicate of CAPEC-448 : Malware Infection into Product Software. Please refer to this other pattern going forward.


---

# CAPEC-45: Buffer Overflow via Symbolic Links

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/45.html  

## Description
This type of attack leverages the use of symbolic links to cause buffer overflows. An adversary can try to create or manipulate a symbolic link file such that its contents result in out of bounds data. When the target software processes the symbolic link file, it could potentially overflow internal buffers with insufficient bounds checking.

## Related Attack Patterns
- ChildOf: CAPEC-100

## Prerequisites
- The adversary can create symbolic link on the target host.
- The target host does not perform correct boundary checking while consuming data from a resources.

## Skills Required
- [Low] An adversary can simply overflow a buffer by inserting a long string into an adversary-modifiable injection vector. The result can be a DoS.
- [High] Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Pay attention to the fact that the resource you read from can be a replaced by a Symbolic link. You can do a Symlink check before reading the file and decide that this is not a legitimate way of accessing the resource.
- Because Symlink can be modified by an adversary, make sure that the ones you read are located in protected directories.
- Pay attention to the resource pointed to by your symlink links (See attack pattern named "Forced Symlink race"), they can be replaced by malicious resources.
- Always check the size of the input data before copying to a buffer.
- Use a language or compiler that performs automatic bounds checking.
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Use OS-level preventative functionality. Not a complete solution.

## Related Weaknesses (CWE)
- CWE-120
- CWE-285
- CWE-302
- CWE-118
- CWE-119
- CWE-74
- CWE-20
- CWE-680
- CWE-697


---

# CAPEC-450: DEPRECATED: Malware Propagation via USB U3 Autorun

**Abstraction:** Standard  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/450.html  

## Description
This attack pattern has been deprecated as it is a duplicate of CAPEC-448 : Embed Virus into DLL. Please refer to this other pattern going forward.


---

# CAPEC-451: DEPRECATED: Malware Propagation via Infected Peripheral Device

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/451.html  

## Description
This attack pattern has been deprecated as it is a duplicate of CAPEC-448 : Malware Infection into Product Software. Please refer to this other pattern going forward.


---

# CAPEC-452: Infected Hardware

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/452.html  

## Description
An adversary inserts malicious logic into hardware, typically in the form of a computer virus or rootkit. This logic is often hidden from the user of the hardware and works behind the scenes to achieve negative impacts. This pattern of attack focuses on hardware already fielded and used in operation as opposed to hardware that is still under development and part of the supply chain.

## Related Attack Patterns
- ChildOf: CAPEC-441

## Prerequisites
- Access to the hardware currently deployed at a victim location.

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands


---

# CAPEC-453: DEPRECATED: Malicious Logic Insertion via Counterfeit Hardware

**Abstraction:** Standard  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/453.html  

## Description
This attack pattern has been deprecated as it is a duplicate of CAPEC-452 : Malicious Logic Insertion into Product Hardware. Please refer to this other pattern going forward.


---

# CAPEC-454: DEPRECATED: Modification of Existing Components with Counterfeit Hardware

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/454.html  

## Description
This attack pattern has been deprecated as it is a duplicate of CAPEC-452 : Malicious Logic Insertion into Product Hardware. Please refer to this other pattern going forward.


---

# CAPEC-455: DEPRECATED: Malicious Logic Insertion via Inclusion of Counterfeit Hardware Components

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/455.html  

## Description
This attack pattern has been deprecated as it is a duplicate of CAPEC-457 : Malicious Logic Insertion into Product Hardware. Please refer to this other pattern going forward.


---

# CAPEC-456: Infected Memory

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/456.html  

## Description
An adversary inserts malicious logic into memory enabling them to achieve a negative impact. This logic is often hidden from the user of the system and works behind the scenes to achieve negative impacts. This pattern of attack focuses on systems already fielded and used in operation as opposed to systems that are still under development and part of the supply chain.

## Related Attack Patterns
- ChildOf: CAPEC-441

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Leverage anti-virus products to detect stop operations with known virus.

## Related Weaknesses (CWE)
- CWE-1257
- CWE-1260
- CWE-1274
- CWE-1312
- CWE-1316


---

# CAPEC-457: USB Memory Attacks

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/457.html  

## Description
An adversary loads malicious code onto a USB memory stick in order to infect any system which the device is plugged in to. USB drives present a significant security risk for business and government agencies. Given the ability to integrate wireless functionality into a USB stick, it is possible to design malware that not only steals confidential data, but sniffs the network, or monitor keystrokes, and then exfiltrates the stolen data off-site via a Wireless connection. Also, viruses can be transmitted via the USB interface without the specific use of a memory stick. The attacks from USB devices are often of such sophistication that experts conclude they are not the work of single individuals, but suggest state sponsorship. These attacks can be performed by an adversary with direct access to a target system or can be executed via means such as USB Drop Attacks.

## Related Attack Patterns
- ChildOf: CAPEC-456
- CanPrecede: CAPEC-529

## Prerequisites
- Some level of physical access to the device being attacked.
- Information pertaining to the target organization on how to best execute a USB Drop Attack.

## Mitigations
- Ensure that proper, physical system access is regulated to prevent an adversary from physically connecting a malicious USB device themself.
- Use anti-virus and anti-malware tools which can prevent malware from executing if it finds its way onto a target system. Additionally, make sure these tools are regularly updated to contain up-to-date virus and malware signatures.
- Do not connect untrusted USB devices to systems connected on an organizational network. Additionally, use an isolated testing machine to validate untrusted devices and confirm malware does not exist.

## Related Weaknesses (CWE)
- CWE-1299


---

# CAPEC-458: Flash Memory Attacks

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/458.html  

## Description
An adversary inserts malicious logic into a product or technology via flashing the on-board memory with a code-base that contains malicious logic. Various attacks exist against the integrity of flash memory, the most direct being rootkits coded into the BIOS or chipset of a device.

## Related Attack Patterns
- ChildOf: CAPEC-456

## Related Weaknesses (CWE)
- CWE-1282


---

# CAPEC-459: Creating a Rogue Certification Authority Certificate

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/459.html  

## Description
An adversary exploits a weakness resulting from using a hashing algorithm with weak collision resistance to generate certificate signing requests (CSR) that contain collision blocks in their "to be signed" parts. The adversary submits one CSR to be signed by a trusted certificate authority then uses the signed blob to make a second certificate appear signed by said certificate authority. Due to the hash collision, both certificates, though different, hash to the same value and so the signed blob works just as well in the second certificate. The net effect is that the adversary's second X.509 certificate, which the Certification Authority has never seen, is now signed and validated by that Certification Authority.

## Related Attack Patterns
- ChildOf: CAPEC-473

## Prerequisites
- Certification Authority is using a hash function with insufficient collision resistance to generate the certificate hash to be signed

## Skills Required
- [High] Understanding of how to force a hash collision in X.509 certificates
- [High] An attacker must be able to craft two X.509 certificates that produce the same hash value
- [Medium] Knowledge needed to set up a certification authority

## Resources Required
- Knowledge of a certificate authority that uses hashing algorithms with poor collision resistance
- A valid certificate request and a malicious certificate request with identical hash values

## Consequences
- Scope: Access Control, Authentication; Impact: Gain Privileges

## Mitigations
- Certification Authorities need to stop using deprecated or cryptographically insecure hashing algorithms to hash the certificates that they are about to sign. Instead they should be using stronger hashing functions such as SHA-256 or SHA-512.

## Related Weaknesses (CWE)
- CWE-327
- CWE-295
- CWE-290


---

# CAPEC-46: Overflow Variables and Tags

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/46.html  

## Description
This type of attack leverages the use of tags or variables from a formatted configuration data to cause buffer overflow. The adversary crafts a malicious HTML page or configuration file that includes oversized strings, thus causing an overflow.

## Related Attack Patterns
- ChildOf: CAPEC-100
- PeerOf: CAPEC-8
- PeerOf: CAPEC-10

## Prerequisites
- The target program consumes user-controllable data in the form of tags or variables.
- The target program does not perform sufficient boundary checking.

## Skills Required
- [Low] An adversary can simply overflow a buffer by inserting a long string into an adversary-modifiable injection vector. The result can be a DoS.
- [High] Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Use a language or compiler that performs automatic bounds checking.
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Use OS-level preventative functionality. Not a complete solution.
- Do not trust input data from user. Validate all user input.

## Related Weaknesses (CWE)
- CWE-120
- CWE-118
- CWE-119
- CWE-74
- CWE-20
- CWE-680
- CWE-733
- CWE-697


---

# CAPEC-460: HTTP Parameter Pollution (HPP)

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/460.html  

## Description
An adversary adds duplicate HTTP GET/POST parameters by injecting query string delimiters. Via HPP it may be possible to override existing hardcoded HTTP parameters, modify the application behaviors, access and, potentially exploit, uncontrollable variables, and bypass input validation checkpoints and WAF rules.

## Related Attack Patterns
- ChildOf: CAPEC-15
- CanPrecede: CAPEC-676

## Prerequisites
- HTTP protocol is used with some GET/POST parameters passed

## Resources Required
- Any tool that enables intercepting and tampering with HTTP requests

## Mitigations
- Configuration: If using a Web Application Firewall (WAF), filters should be carefully configured to detect abnormal HTTP requests
- Design: Perform URL encoding
- Implementation: Use strict regular expressions in URL rewriting
- Implementation: Beware of multiple occurrences of a parameter in a Query String

## Related Weaknesses (CWE)
- CWE-88
- CWE-147
- CWE-235


---

# CAPEC-461: Web Services API Signature Forgery Leveraging Hash Function Extension Weakness

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/461.html  

## Description
An adversary utilizes a hash function extension/padding weakness, to modify the parameters passed to the web service requesting authentication by generating their own call in order to generate a legitimate signature hash (as described in the notes), without knowledge of the secret token sometimes provided by the web service.

## Related Attack Patterns
- ChildOf: CAPEC-115

## Prerequisites
- Web services check the signature of the API calls
- Authentication tokens / secrets are shared between the server and the legitimate client
- The API call signature is generated by concatenating the parameter list with the shared secret and hashing the result.
- An iterative hash function like MD5 and SHA1 is used.
- An attacker is able to intercept or in some other way gain access to the information passed between the legitimate client and the server in order to retrieve the hash value and length of the original message.
- The communication channel between the client and the server is not secured via channel security such as TLS

## Skills Required
- [Medium] Medium level of cryptography knowledge, specifically how iterative hash functions work. This is needed to select proper padding.

## Resources Required
- Access to a function to produce a hash (e.g., MD5, SHA1) Tools that allow the attacker to intercept a message between the client and the server, specifically the hash that is the signature and the length of the original message concatenated with the secret bytes

## Mitigations
- Design: Use a secure message authentication code (MAC) function such as an HMAC-SHA1

## Related Weaknesses (CWE)
- CWE-328
- CWE-290


---

# CAPEC-462: Cross-Domain Search Timing

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/462.html  

## Description
An attacker initiates cross domain HTTP / GET requests and times the server responses. The timing of these responses may leak important information on what is happening on the server. Browser's same origin policy prevents the attacker from directly reading the server responses (in the absence of any other weaknesses), but does not prevent the attacker from timing the responses to requests that the attacker issued cross domain.

## Related Attack Patterns
- ChildOf: CAPEC-54

## Prerequisites
- Ability to issue GET / POST requests cross domainJava Script is enabled in the victim's browserThe victim has an active session with the site from which the attacker would like to receive informationThe victim's site does not protect search functionality with cross site request forgery (CSRF) protection

## Skills Required
- [Low] Some knowledge of Java Script

## Resources Required
- Ability to issue GET / POST requests cross domain

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Design: The victim's site could protect all potentially sensitive functionality (e.g. search functions) with cross site request forgery (CSRF) protection and not perform any work on behalf of forged requests
- Design: The browser's security model could be fixed to not leak timing information for cross domain requests

## Related Weaknesses (CWE)
- CWE-385
- CWE-352
- CWE-208


---

# CAPEC-463: Padding Oracle Crypto Attack

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/463.html  

## Description
An adversary is able to efficiently decrypt data without knowing the decryption key if a target system leaks data on whether or not a padding error happened while decrypting the ciphertext. A target system that leaks this type of information becomes the padding oracle and an adversary is able to make use of that oracle to efficiently decrypt data without knowing the decryption key by issuing on average 128*b calls to the padding oracle (where b is the number of bytes in the ciphertext block). In addition to performing decryption, an adversary is also able to produce valid ciphertexts (i.e., perform encryption) by using the padding oracle, all without knowing the encryption key.

## Related Attack Patterns
- ChildOf: CAPEC-97

## Prerequisites
- The decryption routine does not properly authenticate the message / does not verify its integrity prior to performing the decryption operation
- The target system leaks data (in some way) on whether a padding error has occurred when attempting to decrypt the ciphertext.
- The padding oracle remains available for enough time / for as many requests as needed for the adversary to decrypt the ciphertext.

## Resources Required
- Ability to detect instances where a target system is vulnerable to an oracle padding attack Sufficient cryptography knowledge and tools needed to take advantage of the presence of the padding oracle to perform decryption / encryption of data without a key

## Mitigations
- Design: Use a message authentication code (MAC) or another mechanism to perform verification of message authenticity / integrity prior to decryption
- Implementation: Do not leak information back to the user as to any cryptography (e.g., padding) encountered during decryption.

## Related Weaknesses (CWE)
- CWE-209
- CWE-514
- CWE-649
- CWE-347
- CWE-354
- CWE-696


---

# CAPEC-464: Evercookie

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/464.html  

## Description
An attacker creates a very persistent cookie that stays present even after the user thinks it has been removed. The cookie is stored on the victim's machine in over ten places. When the victim clears the cookie cache via traditional means inside the browser, that operation removes the cookie from certain places but not others. The malicious code then replicates the cookie from all of the places where it was not deleted to all of the possible storage locations once again. So the victim again has the cookie in all of the original storage locations. In other words, failure to delete the cookie in even one location will result in the cookie's resurrection everywhere. The evercookie will also persist across different browsers because certain stores (e.g., Local Shared Objects) are shared between different browsers.

## Related Attack Patterns
- ChildOf: CAPEC-554

## Prerequisites
- The victim's browser is not configured to reject all cookiesThe victim visits a website that serves the attackers' evercookie

## Resources Required
- Evercookie source code

## Mitigations
- Design: Browser's design needs to be changed to limit where cookies can be stored on the client side and provide an option to clear these cookies in all places, as well as another option to stop these cookies from being written in the first place.
- Design: Safari browser's private browsing mode is currently effective against evercookies.

## Related Weaknesses (CWE)
- CWE-359


---

# CAPEC-465: Transparent Proxy Abuse

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/465.html  

## Description
A transparent proxy serves as an intermediate between the client and the internet at large. It intercepts all requests originating from the client and forwards them to the correct location. The proxy also intercepts all responses to the client and forwards these to the client. All of this is done in a manner transparent to the client.

## Related Attack Patterns
- ChildOf: CAPEC-554

## Prerequisites
- Transparent proxy is usedVulnerable configuration of network topology involving the transparent proxy (e.g., no NAT happening between the client and the proxy)Execution of malicious Flash or Applet in the victim's browser

## Skills Required
- [Medium] Creating malicious Flash or Applet to open a cross-domain socket connection to a remote system

## Mitigations
- Design: Ensure that the transparent proxy uses an actual network layer IP address for routing requests. On the transparent proxy, disable the use of routing based on address information in the HTTP host header.
- Configuration: Disable in the browser the execution of Java Script, Flash, SilverLight, etc.

## Related Weaknesses (CWE)
- CWE-441


---

# CAPEC-466: Leveraging Active Adversary in the Middle Attacks to Bypass Same Origin Policy

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/466.html  

## Description
An attacker leverages an adversary in the middle attack (CAPEC-94) in order to bypass the same origin policy protection in the victim's browser. This active adversary in the middle attack could be launched, for instance, when the victim is connected to a public WIFI hot spot. An attacker is able to intercept requests and responses between the victim's browser and some non-sensitive website that does not use TLS.

## Related Attack Patterns
- ChildOf: CAPEC-94

## Prerequisites
- The victim and the attacker are both in an environment where an active adversary in the middle attack is possible (e.g., public WIFI hot spot)The victim visits at least one website that does not use TLS / SSL

## Skills Required
- [Low] Ability to intercept and modify requests / responses
- [Medium] Ability to create iFrame and JavaScript code that would initiate unauthorized requests to sensitive sites from the victim's browser
- [Medium] Solid understanding of the HTTP protocol

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Design: Tunnel communications through a secure proxy
- Design: Trust level separation for privileged / non privileged interactions (e.g., two different browsers, two different users, two different operating systems, two different virtual machines)

## Related Weaknesses (CWE)
- CWE-300


---

# CAPEC-467: Cross Site Identification

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/467.html  

## Description
An attacker harvests identifying information about a victim via an active session that the victim's browser has with a social networking site. A victim may have the social networking site open in one tab or perhaps is simply using the "remember me" feature to keep their session with the social networking site active. An attacker induces a payload to execute in the victim's browser that transparently to the victim initiates a request to the social networking site (e.g., via available social network site APIs) to retrieve identifying information about a victim. While some of this information may be public, the attacker is able to harvest this information in context and may use it for further attacks on the user (e.g., spear phishing).

## Related Attack Patterns
- ChildOf: CAPEC-62

## Prerequisites
- The victim has an active session with the social networking site.

## Skills Required
- [High] An attacker should be able to create a payload and deliver it to the victim's browser.
- [Medium] An attacker needs to know how to interact with various social networking sites (e.g., via available APIs) to request information and how to send the harvested data back to the attacker.

## Mitigations
- Usage: Users should always explicitly log out from the social networking sites when done using them.
- Usage: Users should not open other tabs in the browser when using a social networking site.

## Related Weaknesses (CWE)
- CWE-352
- CWE-359


---

# CAPEC-468: Generic Cross-Browser Cross-Domain Theft

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/468.html  

## Description
An attacker makes use of Cascading Style Sheets (CSS) injection to steal data cross domain from the victim's browser. The attack works by abusing the standards relating to loading of CSS: 1. Send cookies on any load of CSS (including cross-domain) 2. When parsing returned CSS ignore all data that does not make sense before a valid CSS descriptor is found by the CSS parser.

## Related Attack Patterns
- ChildOf: CAPEC-242

## Prerequisites
- No new lines can be present in the injected CSS stringProper HTML or URL escaping of the " and ' characters is not presentThe attacker has control of two injection points: pre-string and post-string

## Skills Required
- [High] Ability to craft a CSS injection

## Resources Required
- Attacker controlled site/page to render a page referencing the injected CSS string

## Mitigations
- Design: Prior to performing CSS parsing, require the CSS to start with well-formed CSS when it is a cross-domain load and the MIME type is broken. This is a browser level fix.
- Implementation: Perform proper HTML encoding and URL escaping

## Related Weaknesses (CWE)
- CWE-707
- CWE-149
- CWE-177
- CWE-838


---

# CAPEC-469: HTTP DoS

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/469.html  

## Description
An attacker performs flooding at the HTTP level to bring down only a particular web application rather than anything listening on a TCP/IP connection. This denial of service attack requires substantially fewer packets to be sent which makes DoS harder to detect. This is an equivalent of SYN flood in HTTP. The idea is to keep the HTTP session alive indefinitely and then repeat that hundreds of times. This attack targets resource depletion weaknesses in web server software. The web server will wait to attacker's responses on the initiated HTTP sessions while the connection threads are being exhausted.

## Related Attack Patterns
- ChildOf: CAPEC-227

## Prerequisites
- HTTP protocol is usedWeb server used is vulnerable to denial of service via HTTP flooding

## Resources Required
- Ability to issues hundreds of HTTP requests

## Mitigations
- Configuration: Configure web server software to limit the waiting period on opened HTTP sessions
- Design: Use load balancing mechanisms

## Related Weaknesses (CWE)
- CWE-770
- CWE-772


---

# CAPEC-47: Buffer Overflow via Parameter Expansion

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/47.html  

## Description
In this attack, the target software is given input that the adversary knows will be modified and expanded in size during processing. This attack relies on the target software failing to anticipate that the expanded data may exceed some internal limit, thereby creating a buffer overflow.

## Related Attack Patterns
- ChildOf: CAPEC-100

## Prerequisites
- The program expands one of the parameters passed to a function with input controlled by the user, but a later function making use of the expanded parameter erroneously considers the original, not the expanded size of the parameter.
- The expanded parameter is used in the context where buffer overflow may become possible due to the incorrect understanding of the parameter size (i.e. thinking that it is smaller than it really is).

## Skills Required
- [High] Finding this particular buffer overflow may not be trivial. Also, stack and especially heap based buffer overflows require a lot of knowledge if the intended goal is arbitrary code execution. Not only that the adversary needs to write the shell code to accomplish their goals, but the adversary also needs to find a way to get the program execution to jump to the planted shell code. There also needs to be sufficient room for the payload. So not every buffer overflow will be exploitable, even by a skilled adversary.

## Resources Required
- Access to the program source or binary. If the program is only available in binary then a disassembler and other reverse engineering tools will be helpful.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Availability; Impact: Unreliable Execution
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Ensure that when parameter expansion happens in the code that the assumptions used to determine the resulting size of the parameter are accurate and that the new size of the parameter is visible to the whole system

## Related Weaknesses (CWE)
- CWE-120
- CWE-119
- CWE-118
- CWE-130
- CWE-131
- CWE-74
- CWE-20
- CWE-680
- CWE-697


---

# CAPEC-470: Expanding Control over the Operating System from the Database

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/470.html  

## Description
An attacker is able to leverage access gained to the database to read / write data to the file system, compromise the operating system, create a tunnel for accessing the host machine, and use this access to potentially attack other machines on the same network as the database machine. Traditionally SQL injections attacks are viewed as a way to gain unauthorized read access to the data stored in the database, modify the data in the database, delete the data, etc. However, almost every data base management system (DBMS) system includes facilities that if compromised allow an attacker complete access to the file system, operating system, and full access to the host running the database. The attacker can then use this privileged access to launch subsequent attacks. These facilities include dropping into a command shell, creating user defined functions that can call system level libraries present on the host machine, stored procedures, etc.

## Related Attack Patterns
- ChildOf: CAPEC-66

## Prerequisites
- A vulnerable DBMS is usedA SQL injection exists that gives an attacker access to the database or an attacker has access to the DBMS via other means

## Skills Required
- [High] Low level knowledge of the various facilities available in different DBMS systems for interacting with the file system and operating system

## Mitigations
- Design: Follow the defensive programming practices needed to protect an application accessing the database from SQL injection
- Configuration: Ensure that the DBMS is patched with the latest security patches
- Design: Ensure that the DBMS login used by the application has the lowest possible level of privileges in the DBMS
- Design: Ensure that DBMS runs with the lowest possible level of privileges on the host machine and that it runs as a separate user
- Usage: Do not use the DBMS machine for anything else other than the database
- Usage: Do not place any trust in the database host on the internal network. Authenticate and validate all network activity originating from the database host.
- Usage: Use an intrusion detection system to monitor network connections and logs on the database host.
- Implementation: Remove / disable all unneeded / unused functions of the DBMS system that may allow an attacker to elevate privileges if compromised

## Related Weaknesses (CWE)
- CWE-250
- CWE-89


---

# CAPEC-471: Search Order Hijacking

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/471.html  

## Description
An adversary exploits a weakness in an application's specification of external libraries to exploit the functionality of the loader where the process loading the library searches first in the same directory in which the process binary resides and then in other directories. Exploitation of this preferential search order can allow an attacker to make the loading process load the adversary's rogue library rather than the legitimate library. This attack can be leveraged with many different libraries and with many different loading processes. No forensic trails are left in the system's registry or file system that an incorrect library had been loaded.

## Related Attack Patterns
- ChildOf: CAPEC-159

## Prerequisites
- Attacker has a mechanism to place its malicious libraries in the needed location on the file system.

## Skills Required
- [Medium] Ability to create a malicious library.

## Mitigations
- Design: Fix the Windows loading process to eliminate the preferential search order by looking for DLLs in the precise location where they are expected
- Design: Sign system DLLs so that unauthorized DLLs can be detected.

## Related Weaknesses (CWE)
- CWE-427


---

# CAPEC-472: Browser Fingerprinting

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/472.html  

## Description
An attacker carefully crafts small snippets of Java Script to efficiently detect the type of browser the potential victim is using. Many web-based attacks need prior knowledge of the web browser including the version of browser to ensure successful exploitation of a vulnerability. Having this knowledge allows an attacker to target the victim with attacks that specifically exploit known or zero day weaknesses in the type and version of the browser used by the victim. Automating this process via Java Script as a part of the same delivery system used to exploit the browser is considered more efficient as the attacker can supply a browser fingerprinting method and integrate it with exploit code, all contained in Java Script and in response to the same web page request by the browser.

## Related Attack Patterns
- ChildOf: CAPEC-541

## Prerequisites
- Victim's browser visits a website that contains attacker's Java ScriptJava Script is not disabled in the victim's browser

## Mitigations
- Configuration: Disable Java Script in the browser

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-473: Signature Spoof

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/473.html  

## Description
An attacker generates a message or datablock that causes the recipient to believe that the message or datablock was generated and cryptographically signed by an authoritative or reputable source, misleading a victim or victim operating system into performing malicious actions.

## Related Attack Patterns
- ChildOf: CAPEC-151

## Prerequisites
- The victim or victim system is dependent upon a cryptographic signature-based verification system for validation of one or more security events or actions.
- The validation can be bypassed via an attacker-provided signature that makes it appear that the legitimate authoritative or reputable source provided the signature.

## Skills Required
- [High] Technical understanding of how signature verification algorithms work with data and applications

## Consequences
- Scope: Access Control, Authentication; Impact: Gain Privileges

## Related Weaknesses (CWE)
- CWE-20
- CWE-327
- CWE-290


---

# CAPEC-474: Signature Spoofing by Key Theft

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/474.html  

## Description
An attacker obtains an authoritative or reputable signer's private signature key by theft and then uses this key to forge signatures from the original signer to mislead a victim into performing actions that benefit the attacker.

## Related Attack Patterns
- ChildOf: CAPEC-473

## Prerequisites
- An authoritative or reputable signer is storing their private signature key with insufficient protection.

## Skills Required
- [Low] Knowledge of common location methods and access methods to sensitive data
- [High] Ability to compromise systems containing sensitive data

## Mitigations
- Restrict access to private keys from non-supervisory accounts
- Restrict access to administrative personnel and processes only
- Ensure all remote methods are secured
- Ensure all services are patched and up to date

## Related Weaknesses (CWE)
- CWE-522


---

# CAPEC-475: Signature Spoofing by Improper Validation

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/475.html  

## Description
An adversary exploits a cryptographic weakness in the signature verification algorithm implementation to generate a valid signature without knowing the key.

## Related Attack Patterns
- ChildOf: CAPEC-473
- CanPrecede: CAPEC-542

## Prerequisites
- Recipient is using a weak cryptographic signature verification algorithm or a weak implementation of a cryptographic signature verification algorithm, or the configuration of the recipient's application accepts the use of keys generated using cryptographically weak signature verification algorithms.

## Skills Required
- [High] Cryptanalysis of signature verification algorithm
- [High] Reverse engineering and cryptanalysis of signature verification algorithm implementation

## Mitigations
- Use programs and products that contain cryptographic elements that have been thoroughly tested for flaws in the signature verification routines.

## Related Weaknesses (CWE)
- CWE-347
- CWE-327
- CWE-295


---

# CAPEC-476: Signature Spoofing by Misrepresentation

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/476.html  

## Description
An attacker exploits a weakness in the parsing or display code of the recipient software to generate a data blob containing a supposedly valid signature, but the signer's identity is falsely represented, which can lead to the attacker manipulating the recipient software or its victim user to perform compromising actions.

## Related Attack Patterns
- ChildOf: CAPEC-473

## Prerequisites
- Recipient is using signature verification software that does not clearly indicate potential homographs in the signer identity.Recipient is using signature verification software that contains a parsing vulnerability, or allows control characters in the signer identity field, such that a signature is mistakenly displayed as valid and from a known or authoritative signer.

## Skills Required
- [High] Attacker needs to understand the layout and composition of data blobs used by the target application.
- [High] To discover a specific vulnerability, attacker needs to reverse engineer signature parsing, signature verification and signer representation code.
- [High] Attacker may be required to create malformed data blobs and know how to insert them in a location that the recipient will visit.

## Mitigations
- Ensure the application is using parsing and data display techniques that will accurately display control characters, international symbols and markings, and ultimately recognize potential homograph attacks.

## Related Weaknesses (CWE)
- CWE-290


---

# CAPEC-477: Signature Spoofing by Mixing Signed and Unsigned Content

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/477.html  

## Description
An attacker exploits the underlying complexity of a data structure that allows for both signed and unsigned content, to cause unsigned data to be processed as though it were signed data.

## Related Attack Patterns
- ChildOf: CAPEC-473

## Prerequisites
- Signer and recipient are using complex data storage structures that allow for a mix between signed and unsigned data
- Recipient is using signature verification software that does not maintain separation between signed and unsigned data once the signature has been verified.

## Skills Required
- [High] The attacker may need to continuously monitor a stream of signed data, waiting for an exploitable message to appear.
- [High] Attacker must be able to create malformed data blobs and know how to insert them in a location that the recipient will visit.

## Mitigations
- Ensure the application is fully patched and does not allow the processing of unsigned data as if it is signed data.

## Related Weaknesses (CWE)
- CWE-693
- CWE-311
- CWE-319


---

# CAPEC-478: Modification of Windows Service Configuration

**Abstraction:** Detailed  
**Status:** Usable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/478.html  

## Description
An adversary exploits a weakness in access control to modify the execution parameters of a Windows service. The goal of this attack is to execute a malicious binary in place of an existing service.

## Related Attack Patterns
- ChildOf: CAPEC-203

## Prerequisites
- The adversary must have the capability to write to the Windows Registry on the targeted system.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Execute Unauthorized Commands

## Mitigations
- Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation.

## Related Weaknesses (CWE)
- CWE-284


---

# CAPEC-479: Malicious Root Certificate

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/479.html  

## Description
An adversary exploits a weakness in authorization and installs a new root certificate on a compromised system. Certificates are commonly used for establishing secure TLS/SSL communications within a web browser. When a user attempts to browse a website that presents a certificate that is not trusted an error message will be displayed to warn the user of the security risk. Depending on the security settings, the browser may not allow the user to establish a connection to the website. Adversaries have used this technique to avoid security warnings prompting users when compromised systems connect over HTTPS to adversary controlled web servers that spoof legitimate websites in order to collect login credentials.

## Related Attack Patterns
- ChildOf: CAPEC-473

## Prerequisites
- The adversary must have the ability to create a new root certificate.

## Related Weaknesses (CWE)
- CWE-284


---

# CAPEC-48: Passing Local Filenames to Functions That Expect a URL

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/48.html  

## Description
This attack relies on client side code to access local files and resources instead of URLs. When the client browser is expecting a URL string, but instead receives a request for a local file, that execution is likely to occur in the browser process space with the browser's authority to local files. The attacker can send the results of this request to the local files out to a site that they control. This attack may be used to steal sensitive authentication data (either local or remote), or to gain system profile information to launch further attacks.

## Related Attack Patterns
- ChildOf: CAPEC-212

## Prerequisites
- The victim's software must not differentiate between the location and type of reference passed the client software, e.g. browser

## Skills Required
- [Medium] Attacker identifies known local files to exploit

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Ensure all configuration files and resource are either removed or protected when promoting code into production.
- Design: Use browser technologies that do not allow client side scripting.
- Implementation: Perform input validation for all remote content.
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser

## Related Weaknesses (CWE)
- CWE-241
- CWE-706


---

# CAPEC-480: Escaping Virtualization

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/480.html  

## Description
An adversary gains access to an application, service, or device with the privileges of an authorized or privileged user by escaping the confines of a virtualized environment. The adversary is then able to access resources or execute unauthorized code within the host environment, generally with the privileges of the user running the virtualized process. Successfully executing an attack of this type is often the first step in executing more complex attacks.

## Related Attack Patterns
- ChildOf: CAPEC-115

## Consequences
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges

## Mitigations
- Ensure virtualization software is current and up-to-date.
- Abide by the least privilege principle to avoid assigning users more privileges than necessary.

## Related Weaknesses (CWE)
- CWE-693


---

# CAPEC-481: Contradictory Destinations in Traffic Routing Schemes

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/481.html  

## Description
Adversaries can provide contradictory destinations when sending messages. Traffic is routed in networks using the domain names in various headers available at different levels of the OSI model. In a Content Delivery Network (CDN) multiple domains might be available, and if there are contradictory domain names provided it is possible to route traffic to an inappropriate destination. The technique, called Domain Fronting, involves using different domain names in the SNI field of the TLS header and the Host field of the HTTP header. An alternative technique, called Domainless Fronting, is similar, but the SNI field is left blank.

## Related Attack Patterns
- ChildOf: CAPEC-161

## Prerequisites
- An adversary must be aware that their message will be routed using a CDN, and that both of the contradictory domains are served from that CDN.
- If the purpose of the Domain Fronting is to hide redirected C2 traffic, the C2 server must have been created in the CDN.

## Skills Required
- [Medium] The adversary must have some knowledge of how messages are routed.

## Consequences
- Scope: Confidentiality; Impact: Read Data, Modify Data

## Mitigations
- Monitor connections, checking headers in traffic for contradictory domain names, or empty domain names.

## Related Weaknesses (CWE)
- CWE-923


---

# CAPEC-482: TCP Flood

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/482.html  

## Description
An adversary may execute a flooding attack using the TCP protocol with the intent to deny legitimate users access to a service. These attacks exploit the weakness within the TCP protocol where there is some state information for the connection the server needs to maintain. This often involves the use of TCP SYN messages.

## Related Attack Patterns
- ChildOf: CAPEC-125

## Prerequisites
- This type of an attack requires the ability to generate a large amount of TCP traffic to send to the target port of a functioning server.

## Mitigations
- To mitigate this type of an attack, an organization can monitor incoming packets and look for patterns in the TCP traffic to determine if the network is under an attack. The potential target may implement a rate limit on TCP SYN messages which would provide limited capabilities while under attack.

## Related Weaknesses (CWE)
- CWE-770


---

# CAPEC-484: DEPRECATED: XML Client-Side Attack

**Abstraction:** Standard  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/484.html  

## Description
This attack pattern has been deprecated as it a generalization of CAPEC-230: XML Nested Payloads and CAPEC-231: XML Oversized Payloads. Please refer to these CAPECs going forward.


---

# CAPEC-485: Signature Spoofing by Key Recreation

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/485.html  

## Description
An attacker obtains an authoritative or reputable signer's private signature key by exploiting a cryptographic weakness in the signature algorithm or pseudorandom number generation and then uses this key to forge signatures from the original signer to mislead a victim into performing actions that benefit the attacker.

## Related Attack Patterns
- ChildOf: CAPEC-473

## Prerequisites
- An authoritative signer is using a weak method of random number generation or weak signing software that causes key leakage or permits key inference.
- An authoritative signer is using a signature algorithm with a direct weakness or with poorly chosen parameters that enable the key to be recovered using signatures from that signer.

## Skills Required
- [High] Cryptanalysis of signature generation algorithm
- [High] Reverse engineering and cryptanalysis of signature generation algorithm implementation and random number generation
- [High] Ability to create malformed data blobs and know how to present them directly or indirectly to a victim.

## Mitigations
- Ensure cryptographic elements have been sufficiently tested for weaknesses.

## Related Weaknesses (CWE)
- CWE-330


---

# CAPEC-486: UDP Flood

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/486.html  

## Description
An adversary may execute a flooding attack using the UDP protocol with the intent to deny legitimate users access to a service by consuming the available network bandwidth. Additionally, firewalls often open a port for each UDP connection destined for a service with an open UDP port, meaning the firewalls in essence save the connection state thus the high packet nature of a UDP flood can also overwhelm resources allocated to the firewall. UDP attacks can also target services like DNS or VoIP which utilize these protocols. Additionally, due to the session-less nature of the UDP protocol, the source of a packet is easily spoofed making it difficult to find the source of the attack.

## Related Attack Patterns
- ChildOf: CAPEC-125

## Prerequisites
- This type of an attack requires the ability to generate a large amount of UDP traffic to send to the desired port of a target service using UDP.

## Mitigations
- To mitigate this type of an attack, modern firewalls drop UDP traffic destined for closed ports, and unsolicited UDP reply packets. A variety of other countermeasures such as universal reverse path forwarding and remote triggered black holing(RFC3704) along with modifications to BGP like black hole routing and sinkhole routing(RFC3882) help mitigate the spoofed source IP nature of these attacks.

## Related Weaknesses (CWE)
- CWE-770


---

# CAPEC-487: ICMP Flood

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/487.html  

## Description
An adversary may execute a flooding attack using the ICMP protocol with the intent to deny legitimate users access to a service by consuming the available network bandwidth. A typical attack involves a victim server receiving ICMP packets at a high rate from a wide range of source addresses. Additionally, due to the session-less nature of the ICMP protocol, the source of a packet is easily spoofed making it difficult to find the source of the attack.

## Related Attack Patterns
- ChildOf: CAPEC-125

## Prerequisites
- This type of an attack requires the ability to generate a large amount of ICMP traffic to send to the target server.

## Mitigations
- To mitigate this type of an attack, an organization can enable ingress filtering. Additionally modifications to BGP like black hole routing and sinkhole routing(RFC3882) help mitigate the spoofed source IP nature of these attacks.

## Related Weaknesses (CWE)
- CWE-770


---

# CAPEC-488: HTTP Flood

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/488.html  

## Description
An adversary may execute a flooding attack using the HTTP protocol with the intent to deny legitimate users access to a service by consuming resources at the application layer such as web services and their infrastructure. These attacks use legitimate session-based HTTP GET requests designed to consume large amounts of a server's resources. Since these are legitimate sessions this attack is very difficult to detect.

## Related Attack Patterns
- ChildOf: CAPEC-125

## Prerequisites
- This type of an attack requires the ability to generate a large amount of HTTP traffic to send to a target server.

## Mitigations
- Design: Use a Web Application Firewall (WAF) to help filter out malicious traffic. This can be setup with rules to block IP addresses found in IP reputation databases, which contains lists of known bad IP addresses. Analysts should also monitor when the traffic flow becomes abnormally large, and be able to add on-the-fly rules to block malicious traffic. Special care should be taken to ensure low false positive rates in block rules and functionality should be implemented to allow a legitimate user to resume sending traffic if they have been blocked.
- Hire a third party provider to implement a Web Application Firewall (WAF) for your application. Third party providers have dedicated resources and expertise that could allow them to update rules and prevent HTTP Floods very quickly.
- Design: Use a load balancer such as nginx to prevent small scale HTTP Floods by dispersing traffic between a group of servers.
- Implementation: Make a requesting machine solve some kind of challenge before allowing them to send an HTTP request. This could be a captcha or something similar that works to deter bots.

## Related Weaknesses (CWE)
- CWE-770


---

# CAPEC-489: SSL Flood

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/489.html  

## Description
An adversary may execute a flooding attack using the SSL protocol with the intent to deny legitimate users access to a service by consuming all the available resources on the server side. These attacks take advantage of the asymmetric relationship between the processing power used by the client and the processing power used by the server to create a secure connection. In this manner the attacker can make a large number of HTTPS requests on a low provisioned machine to tie up a disproportionately large number of resources on the server. The clients then continue to keep renegotiating the SSL connection. When multiplied by a large number of attacking machines, this attack can result in a crash or loss of service to legitimate users.

## Related Attack Patterns
- ChildOf: CAPEC-125

## Prerequisites
- This type of an attack requires the ability to generate a large amount of SSL traffic to send a target server.

## Mitigations
- To mitigate this type of an attack, an organization can create rule based filters to silently drop connections if too many are attempted in a certain time period.

## Related Weaknesses (CWE)
- CWE-770


---

# CAPEC-49: Password Brute Forcing

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/49.html  

## Description
An adversary tries every possible value for a password until they succeed. A brute force attack, if feasible computationally, will always be successful because it will essentially go through all possible passwords given the alphabet used (lower case letters, upper case letters, numbers, symbols, etc.) and the maximum length of the password.

## Related Attack Patterns
- ChildOf: CAPEC-112
- CanPrecede: CAPEC-600
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-560
- CanPrecede: CAPEC-561
- CanPrecede: CAPEC-653

## Prerequisites
- An adversary needs to know a username to target.
- The system uses password based authentication as the one factor authentication mechanism.
- An application does not have a password throttling mechanism in place. A good password throttling mechanism will make it almost impossible computationally to brute force a password as it may either lock out the user after a certain number of incorrect attempts or introduce time out periods. Both of these would make a brute force attack impractical.

## Skills Required
- [Low] A brute force attack is very straightforward. A variety of password cracking tools are widely available.

## Resources Required
- A powerful enough computer for the job with sufficient CPU, RAM and HD. Exact requirements will depend on the size of the brute force job and the time requirement for completion. Some brute forcing jobs may require grid or distributed computing (e.g. DES Challenge).

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Implement a password throttling mechanism. This mechanism should take into account both the IP address and the log in name of the user.
- Put together a strong password policy and make sure that all user created passwords comply with it. Alternatively automatically generate strong passwords for users.
- Passwords need to be recycled to prevent aging, that is every once in a while a new password must be chosen.

## Related Weaknesses (CWE)
- CWE-521
- CWE-262
- CWE-263
- CWE-257
- CWE-654
- CWE-307
- CWE-308
- CWE-309


---

# CAPEC-490: Amplification

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/490.html  

## Description
An adversary may execute an amplification where the size of a response is far greater than that of the request that generates it. The goal of this attack is to use a relatively few resources to create a large amount of traffic against a target server. To execute this attack, an adversary send a request to a 3rd party service, spoofing the source address to be that of the target server. The larger response that is generated by the 3rd party service is then sent to the target server. By sending a large number of initial requests, the adversary can generate a tremendous amount of traffic directed at the target. The greater the discrepancy in size between the initial request and the final payload delivered to the target increased the effectiveness of this attack.

## Related Attack Patterns
- ChildOf: CAPEC-125

## Prerequisites
- This type of an attack requires the existence of a 3rd party service that generates a response that is significantly larger than the request that triggers it.

## Mitigations
- To mitigate this type of an attack, an organization can attempt to identify the 3rd party services being used in an active attack and blocking them until the attack ends. This can be accomplished by filtering traffic for suspicious message patterns such as a spike in traffic where each response contains the same large block of data. Care should be taken to prevent false positive rates so legitimate traffic isn't blocked.

## Related Weaknesses (CWE)
- CWE-770


---

# CAPEC-491: Quadratic Data Expansion

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/491.html  

## Description
An adversary exploits macro-like substitution to cause a denial of service situation due to excessive memory being allocated to fully expand the data. The result of this denial of service could cause the application to freeze or crash. This involves defining a very large entity and using it multiple times in a single entity substitution. CAPEC-197 is a similar attack pattern, but it is easier to discover and defend against. This attack pattern does not perform multi-level substitution and therefore does not obviously appear to consume extensive resources.

## Related Attack Patterns
- ChildOf: CAPEC-230

## Prerequisites
- This type of attack requires a server that accepts serialization data which supports substitution and parses the data.

## Consequences
- Scope: Availability; Impact: Unreliable Execution, Resource Consumption

## Mitigations
- Design: Use libraries and templates that minimize unfiltered input. Use methods that limit entity expansion and throw exceptions on attempted entity expansion.
- Implementation: For XML based data - disable altogether the use of inline DTD schemas when parsing XML objects. If a DTD must be used, normalize, filter and use an allowlist and parse with methods and routines that will detect entity expansion from untrusted sources.

## Related Weaknesses (CWE)
- CWE-770


---

# CAPEC-492: Regular Expression Exponential Blowup

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/492.html  

## Description
An adversary may execute an attack on a program that uses a poor Regular Expression(Regex) implementation by choosing input that results in an extreme situation for the Regex. A typical extreme situation operates at exponential time compared to the input size. This is due to most implementations using a Nondeterministic Finite Automaton(NFA) state machine to be built by the Regex algorithm since NFA allows backtracking and thus more complex regular expressions.

## Related Attack Patterns
- ChildOf: CAPEC-130

## Prerequisites
- This type of an attack requires the ability to identify hosts running a poorly implemented Regex, and the ability to send crafted input to exploit the regular expression.

## Mitigations
- Test custom written Regex with fuzzing to determine if the Regex is a poor one. Add timeouts to processes that handle the Regex logic. If an evil Regex is found rewrite it as a good Regex.

## Related Weaknesses (CWE)
- CWE-400
- CWE-1333


---

# CAPEC-493: SOAP Array Blowup

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/493.html  

## Description
An adversary may execute an attack on a web service that uses SOAP messages in communication. By sending a very large SOAP array declaration to the web service, the attacker forces the web service to allocate space for the array elements before they are parsed by the XML parser. The attacker message is typically small in size containing a large array declaration of say 1,000,000 elements and a couple of array elements. This attack targets exhaustion of the memory resources of the web service.

## Related Attack Patterns
- ChildOf: CAPEC-130

## Prerequisites
- This type of an attack requires the attacker to know the endpoint of the web service, and be able to reach the endpoint with a malicious SOAP message.

## Mitigations
- Enforce strict schema validation. The schema should enforce a maximum number of array elements. If the number of maximum array elements can't be limited another validation method should be used. One such method could be comparing the declared number of items in the array with the existing number of elements of the array. If these numbers don't match drop the SOAP packet at the web service layer.

## Related Weaknesses (CWE)
- CWE-770


---

# CAPEC-494: TCP Fragmentation

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/494.html  

## Description
An adversary may execute a TCP Fragmentation attack against a target with the intention of avoiding filtering rules of network controls, by attempting to fragment the TCP packet such that the headers flag field is pushed into the second fragment which typically is not filtered.

## Related Attack Patterns
- ChildOf: CAPEC-130

## Prerequisites
- This type of an attack requires the target system to be running a vulnerable implementation of IP, and the adversary needs to ability to send TCP packets of arbitrary size with crafted data.

## Mitigations
- This attack may be mitigated by enforcing rules at the router following the guidance of RFC1858. The essential part of the guidance is creating the following rule "IF FO=1 and PROTOCOL=TCP then DROP PACKET" as this mitigated both tiny fragment and overlapping fragment attacks in IPv4. In IPv6 overlapping(RFC5722) additional steps may be required such as deep packet inspection. The delayed fragments may be mitigated by enforcing a timeout on the transmission to receive all packets by a certain time since the first packet is received. According to RFC2460 IPv6 implementations should enforce a rule to discard all fragments if the fragments are not ALL received within 60 seconds of the FIRST arriving fragment.

## Related Weaknesses (CWE)
- CWE-770
- CWE-404


---

# CAPEC-495: UDP Fragmentation

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/495.html  

## Description
An attacker may execute a UDP Fragmentation attack against a target server in an attempt to consume resources such as bandwidth and CPU. IP fragmentation occurs when an IP datagram is larger than the MTU of the route the datagram has to traverse. Typically the attacker will use large UDP packets over 1500 bytes of data which forces fragmentation as ethernet MTU is 1500 bytes. This attack is a variation on a typical UDP flood but it enables more network bandwidth to be consumed with fewer packets. Additionally it has the potential to consume server CPU resources and fill memory buffers associated with the processing and reassembling of fragmented packets.

## Related Attack Patterns
- ChildOf: CAPEC-130

## Prerequisites
- This type of an attack requires the attacker to be able to generate fragmented IP traffic containing crafted data.

## Mitigations
- This attack may be mitigated by changing default cache sizes to be larger at the OS level. Additionally rules can be enforced to prune the cache with shorter timeouts for packet reassembly as the cache nears capacity.

## Related Weaknesses (CWE)
- CWE-770
- CWE-404


---

# CAPEC-496: ICMP Fragmentation

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/496.html  

## Description
An attacker may execute a ICMP Fragmentation attack against a target with the intention of consuming resources or causing a crash. The attacker crafts a large number of identical fragmented IP packets containing a portion of a fragmented ICMP message. The attacker these sends these messages to a target host which causes the host to become non-responsive. Another vector may be sending a fragmented ICMP message to a target host with incorrect sizes in the header which causes the host to hang.

## Related Attack Patterns
- ChildOf: CAPEC-130

## Prerequisites
- This type of an attack requires the target system to be running a vulnerable implementation of IP, and the attacker needs to ability to send arbitrary sized ICMP packets to the target.

## Mitigations
- This attack may be mitigated through egress filtering based on ICMP payload so a network is a "good neighbor" to other networks. Bad IP implementations become patched, so using the proper version of a browser or OS is recommended.

## Related Weaknesses (CWE)
- CWE-770
- CWE-404


---

# CAPEC-497: File Discovery

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very Low  
**Reference:** https://capec.mitre.org/data/definitions/497.html  

## Description
An adversary engages in probing and exploration activities to determine if common key files exists. Such files often contain configuration and security parameters of the targeted application, system or network. Using this knowledge may often pave the way for more damaging attacks.

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary must know the location of these common key files.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Leverage file protection mechanisms to render these files accessible only to authorized parties.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-498: Probe iOS Screenshots

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/498.html  

## Description
An adversary examines screenshot images created by iOS in an attempt to obtain sensitive information. This attack targets temporary screenshots created by the underlying OS while the application remains open in the background.

## Related Attack Patterns
- ChildOf: CAPEC-545

## Prerequisites
- This type of an attack requires physical access to a device to either excavate the image files (potentially by leveraging a Jailbreak) or view the screenshots through the multitasking switcher (by double tapping the home button on the device).

## Mitigations
- To mitigate this type of an attack, an application that may display sensitive information should clear the screen contents before a screenshot is taken. This can be accomplished by setting the key window's hidden property to YES. This code to hide the contents should be placed in both the applicationWillResignActive() and applicationDidEnterBackground() methods.

## Related Weaknesses (CWE)
- CWE-359


---

# CAPEC-499: Android Intent Intercept

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/499.html  

## Description
An adversary, through a previously installed malicious application, intercepts messages from a trusted Android-based application in an attempt to achieve a variety of different objectives including denial of service, information disclosure, and data injection. An implicit intent sent from a trusted application can be received by any application that has declared an appropriate intent filter. If the intent is not protected by a permission that the malicious application lacks, then the attacker can gain access to the data contained within the intent. Further, the intent can be either blocked from reaching the intended destination, or modified and potentially forwarded along.

## Related Attack Patterns
- ChildOf: CAPEC-117

## Prerequisites
- An adversary must be able install a purpose built malicious application onto the Android device and convince the user to execute it. The malicious application is used to intercept implicit intents.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- To mitigate this type of an attack, explicit intents should be used whenever sensitive data is being sent. An explicit intent is delivered to a specific application as declared within the intent, whereas the Android operating system determines who receives an implicit intent which could potentially be a malicious application. If an implicit intent must be used, then it should be assumed that the intent will be received by an unknown application and any response should be treated accordingly. Implicit intents should never be used for inter-application communication.

## Related Weaknesses (CWE)
- CWE-925


---

# CAPEC-5: Blue Boxing

**Abstraction:** Detailed  
**Status:** Obsolete  
**Likelihood of Attack:** Medium  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/5.html  

## Description
This type of attack against older telephone switches and trunks has been around for decades. A tone is sent by an adversary to impersonate a supervisor signal which has the effect of rerouting or usurping command of the line. While the US infrastructure proper may not contain widespread vulnerabilities to this type of attack, many companies are connected globally through call centers and business process outsourcing. These international systems may be operated in countries which have not upgraded Telco infrastructure and so are vulnerable to Blue boxing. Blue boxing is a result of failure on the part of the system to enforce strong authorization for administrative functions. While the infrastructure is different than standard current applications like web applications, there are historical lessons to be learned to upgrade the access control for administrative functions. This attack pattern is included in CAPEC for historical purposes.

## Related Attack Patterns
- ChildOf: CAPEC-220

## Prerequisites
- System must use weak authentication mechanisms for administrative functions.

## Skills Required
- [Low] Given a vulnerable phone system, the attackers' technical vector relies on attacks that are well documented in cracker 'zines and have been around for decades.

## Resources Required
- CCITT-5 or other vulnerable lines, with the ability to send tones such as combined 2,400 Hz and 2,600 Hz tones to the switch

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Implementation: Upgrade phone lines. Note this may be prohibitively expensive
- Use strong access control such as two factor access control for administrative access to the switch

## Related Weaknesses (CWE)
- CWE-285


---

# CAPEC-50: Password Recovery Exploitation

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/50.html  

## Description
An attacker may take advantage of the application feature to help users recover their forgotten passwords in order to gain access into the system with the same privileges as the original user. Generally password recovery schemes tend to be weak and insecure.

## Related Attack Patterns
- ChildOf: CAPEC-212
- CanPrecede: CAPEC-600
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-560
- CanPrecede: CAPEC-561
- CanPrecede: CAPEC-653

## Prerequisites
- The system allows users to recover their passwords and gain access back into the system.
- Password recovery mechanism has been designed or implemented insecurely.
- Password recovery mechanism relies only on something the user knows and not something the user has.
- No third party intervention is required to use the password recovery mechanism.

## Skills Required
- [Low] Brute force attack
- [Medium] Social engineering and more sophisticated technical attacks.

## Resources Required
- For a brute force attack one would need a machine with sufficient CPU, RAM and HD.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Use multiple security questions (e.g. have three and make the user answer two of them correctly). Let the user select their own security questions or provide them with choices of questions that are not generic.
- E-mail the temporary password to the registered e-mail address of the user rather than letting the user reset the password online.
- Ensure that your password recovery functionality is not vulnerable to an injection style attack.

## Related Weaknesses (CWE)
- CWE-522
- CWE-640


---

# CAPEC-500: WebView Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/500.html  

## Description
An adversary, through a previously installed malicious application, injects code into the context of a web page displayed by a WebView component. Through the injected code, an adversary is able to manipulate the DOM tree and cookies of the page, expose sensitive information, and can launch attacks against the web application from within the web page.

## Related Attack Patterns
- ChildOf: CAPEC-253

## Prerequisites
- An adversary must be able install a purpose built malicious application onto the device and convince the user to execute it. The malicious application is designed to target a specific web application and is used to load the target web pages via the WebView component. For example, an adversary may develop an application that interacts with Facebook via WebView and adds a new feature that a user desires. The user would install this 3rd party app instead of the Facebook app.

## Mitigations
- The only known mitigation to this type of attack is to keep the malicious application off the system. There is nothing that can be done to the target application to protect itself from a malicious application that has been installed and executed.

## Related Weaknesses (CWE)
- CWE-749
- CWE-940


---

# CAPEC-501: Android Activity Hijack

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/501.html  

## Description
An adversary intercepts an implicit intent sent to launch a Android-based trusted activity and instead launches a counterfeit activity in its place. The malicious activity is then used to mimic the trusted activity's user interface and prompt the target to enter sensitive data as if they were interacting with the trusted activity.

## Related Attack Patterns
- ChildOf: CAPEC-499
- ChildOf: CAPEC-173

## Prerequisites
- The adversary must have previously installed the malicious application onto the Android device that will run in place of the trusted activity.

## Skills Required
- [High] The adversary must typically overcome network and host defenses in order to place malware on the system.

## Resources Required
- Malware capable of acting on the adversary's objectives.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- To mitigate this type of an attack, explicit intents should be used whenever sensitive data is being sent. An 'explicit intent' is delivered to a specific application as declared within the intent, whereas an 'implicit intent' is directed to an application as defined by the Android operating system. If an implicit intent must be used, then it should be assumed that the intent will be received by an unknown application and any response should be treated accordingly (i.e., with appropriate security controls).
- Never use implicit intents for inter-application communication.

## Related Weaknesses (CWE)
- CWE-923


---

# CAPEC-502: Intent Spoof

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/502.html  

## Description
An adversary, through a previously installed malicious application, issues an intent directed toward a specific trusted application's component in an attempt to achieve a variety of different objectives including modification of data, information disclosure, and data injection. Components that have been unintentionally exported and made public are subject to this type of an attack. If the component trusts the intent's action without verififcation, then the target application performs the functionality at the adversary's request, helping the adversary achieve the desired negative technical impact.

## Related Attack Patterns
- ChildOf: CAPEC-148

## Prerequisites
- An adversary must be able install a purpose built malicious application onto the Android device and convince the user to execute it. The malicious application will be used to issue spoofed intents.

## Mitigations
- To limit one's exposure to this type of attack, developers should avoid exporting components unless the component is specifically designed to handle requests from untrusted applications. Developers should be aware that declaring an intent filter will automatically export the component, exposing it to public access. Critical, state-changing actions should not be placed in exported components. If a single component handles both inter- and intra-application requests, the developer should consider dividing that component into separate components. If a component must be exported (e.g., to receive system broadcasts), then the component should dynamically check the caller's identity prior to performing any operations. Requiring Signature or SignatureOrSystem permissions is an effective way of limiting a component's exposure to a set of trusted applications. Finally, the return values of exported components can also leak private data, so developers should check the caller's identity prior to returning sensitive values.

## Related Weaknesses (CWE)
- CWE-284


---

# CAPEC-503: WebView Exposure

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/503.html  

## Description
An adversary, through a malicious web page, accesses application specific functionality by leveraging interfaces registered through WebView's addJavascriptInterface API. Once an interface is registered to WebView through addJavascriptInterface, it becomes global and all pages loaded in the WebView can call this interface.

## Related Attack Patterns
- ChildOf: CAPEC-122

## Prerequisites
- This type of an attack requires the adversary to convince the user to load the malicious web page inside the target application. Once loaded, the malicious web page will have the same permissions as the target application and will have access to all registered interfaces. Both the permission and the interface must be in place for the functionality to be exposed.

## Mitigations
- To mitigate this type of an attack, an application should limit permissions to only those required and should verify the origin of all web content it loads.

## Related Weaknesses (CWE)
- CWE-284


---

# CAPEC-504: Task Impersonation

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/504.html  

## Description
An adversary, through a previously installed malicious application, impersonates an expected or routine task in an attempt to steal sensitive information or leverage a user's privileges.

## Related Attack Patterns
- ChildOf: CAPEC-173

## Prerequisites
- The adversary must already have access to the target system via some means.
- A legitimate task must exist that an adversary can impersonate to glean credentials.
- The user's privileges allow them to execute certain tasks with elevated privileges.

## Skills Required
- [Low] Once an adversary has gained access to the target system, impersonating a task is trivial.

## Resources Required
- Malware or some other means to initially comprise the target system.
- Additional malware to impersonate a legitimate task.

## Consequences
- Scope: Access Control, Authentication; Impact: Gain Privileges

## Mitigations
- The only known mitigation to this attack is to avoid installing the malicious application on the device. However, to impersonate a running task the malicious application does need the GET_TASKS permission to be able to query the task list, and being suspicious of applications with that permission can help.

## Related Weaknesses (CWE)
- CWE-1021


---

# CAPEC-505: Scheme Squatting

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/505.html  

## Description
An adversary, through a previously installed malicious application, registers for a URL scheme intended for a target application that has not been installed. Thereafter, messages intended for the target application are handled by the malicious application. Upon receiving a message, the malicious application displays a screen that mimics the target application, thereby convincing the user to enter sensitive information. This type of attack is most often used to obtain sensitive information (e.g., credentials) from the user as they think that they are interacting with the intended target application.

## Related Attack Patterns
- ChildOf: CAPEC-616

## Mitigations
- The only known mitigation to this attack is to avoid installing the malicious application on the device. Applications usually have to declare the schemes they wish to register, so detecting this during a review is feasible.


---

# CAPEC-506: Tapjacking

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/506.html  

## Description
An adversary, through a previously installed malicious application, displays an interface that misleads the user and convinces them to tap on an attacker desired location on the screen. This is often accomplished by overlaying one screen on top of another while giving the appearance of a single interface. There are two main techniques used to accomplish this. The first is to leverage transparent properties that allow taps on the screen to pass through the visible application to an application running in the background. The second is to strategically place a small object (e.g., a button or text field) on top of the visible screen and make it appear to be a part of the underlying application. In both cases, the user is convinced to tap on the screen but does not realize the application that they are interacting with.

## Related Attack Patterns
- ChildOf: CAPEC-173

## Prerequisites
- This pattern of attack requires the ability to execute a malicious application on the user's device. This malicious application is used to present the interface to the user and make the attack possible.

## Related Weaknesses (CWE)
- CWE-1021


---

# CAPEC-507: Physical Theft

**Abstraction:** Meta  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/507.html  

## Description
An adversary gains physical access to a system or device through theft of the item. Possession of a system or device enables a number of unique attacks to be executed and often provides the adversary with an extended timeframe for which to perform an attack. Most protections put in place to secure sensitive information can be defeated when an adversary has physical access and enough time.

## Prerequisites
- This type of attack requires the existence of a physical target that an adversary believes hosts something of value.

## Mitigations
- To mitigate this type of attack, physical security techniques such as locks doors, alarms, and monitoring of targets should be implemented.


---

# CAPEC-508: Shoulder Surfing

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/508.html  

## Description
In a shoulder surfing attack, an adversary observes an unaware individual's keystrokes, screen content, or conversations with the goal of obtaining sensitive information. One motive for this attack is to obtain sensitive information about the target for financial, personal, political, or other gains. From an insider threat perspective, an additional motive could be to obtain system/application credentials or cryptographic keys. Shoulder surfing attacks are accomplished by observing the content "over the victim's shoulder", as implied by the name of this attack.

## Related Attack Patterns
- ChildOf: CAPEC-651
- CanPrecede: CAPEC-560

## Prerequisites
- The adversary typically requires physical proximity to the target's environment, in order to observe their screen or conversation. This may not be the case if the adversary is able to record the target and obtain sensitive information upon review of the recording.

## Skills Required
- [Low] In most cases, an adversary can simply observe and retain the desired information.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Be mindful of your surroundings when discussing or viewing sensitive information in public areas.
- Pertaining to insider threats, ensure that sensitive information is not displayed to nor discussed around individuals without need-to-know access to said information.

## Related Weaknesses (CWE)
- CWE-200
- CWE-359


---

# CAPEC-509: Kerberoasting

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/509.html  

## Description
Through the exploitation of how service accounts leverage Kerberos authentication with Service Principal Names (SPNs), the adversary obtains and subsequently cracks the hashed credentials of a service account target to exploit its privileges. The Kerberos authentication protocol centers around a ticketing system which is used to request/grant access to services and to then access the requested services. As an authenticated user, the adversary may request Active Directory and obtain a service ticket with portions encrypted via RC4 with the private key of the authenticated account. By extracting the local ticket and saving it disk, the adversary can brute force the hashed value to reveal the target account credentials.

## Related Attack Patterns
- ChildOf: CAPEC-652
- CanPrecede: CAPEC-151

## Prerequisites
- The adversary requires access as an authenticated user on the system. This attack pattern relates to elevating privileges.
- The adversary requires use of a third-party credential harvesting tool (e.g., Mimikatz).
- The adversary requires a brute force tool.

## Consequences
- Scope: Confidentiality; Impact: Gain Privileges

## Mitigations
- Monitor system and domain logs for abnormal access.
- Employ a robust password policy for service accounts. Passwords should be of adequate length and complexity, and they should expire after a period of time.
- Employ the principle of least privilege: limit service accounts privileges to what is required for functionality and no more.
- Enable AES Kerberos encryption (or another stronger encryption algorithm), rather than RC4, where possible.

## Related Weaknesses (CWE)
- CWE-522
- CWE-308
- CWE-309
- CWE-294
- CWE-263
- CWE-262
- CWE-521


---

# CAPEC-51: Poison Web Service Registry

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/51.html  

## Description
SOA and Web Services often use a registry to perform look up, get schema information, and metadata about services. A poisoned registry can redirect (think phishing for servers) the service requester to a malicious service provider, provide incorrect information in schema or metadata, and delete information about service provider interfaces.

## Related Attack Patterns
- ChildOf: CAPEC-203

## Prerequisites
- The attacker must be able to write to resources or redirect access to the service registry.

## Skills Required
- [Low] To identify and execute against an over-privileged system interface

## Resources Required
- Capability to directly or indirectly modify registry resources

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Design: Enforce principle of least privilege
- Design: Harden registry server and file access permissions
- Implementation: Implement communications to and from the registry using secure protocols

## Related Weaknesses (CWE)
- CWE-285
- CWE-74
- CWE-693


---

# CAPEC-510: SaaS User Request Forgery

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/510.html  

## Description
An adversary, through a previously installed malicious application, performs malicious actions against a third-party Software as a Service (SaaS) application (also known as a cloud based application) by leveraging the persistent and implicit trust placed on a trusted user's session. This attack is executed after a trusted user is authenticated into a cloud service, "piggy-backing" on the authenticated session, and exploiting the fact that the cloud service believes it is only interacting with the trusted user. If successful, the actions embedded in the malicious application will be processed and accepted by the targeted SaaS application and executed at the trusted user's privilege level.

## Related Attack Patterns
- ChildOf: CAPEC-21

## Prerequisites
- An adversary must be able install a purpose built malicious application onto the trusted user's system and convince the user to execute it while authenticated to the SaaS application.

## Skills Required
- [Medium] This attack pattern often requires the technical ability to modify a malicious software package (e.g. Zeus) to spider a targeted site and a way to trick a user into a malicious software download.

## Mitigations
- To limit one's exposure to this type of attack, tunnel communications through a secure proxy service.
- Detection of this type of attack can be done through heuristic analysis of behavioral anomalies (a la credit card fraud detection) which can be used to identify inhuman behavioral patterns. (e.g., spidering)

## Related Weaknesses (CWE)
- CWE-346


---

# CAPEC-511: Infiltration of Software Development Environment

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/511.html  

## Description
An attacker uses common delivery mechanisms such as email attachments or removable media to infiltrate the IDE (Integrated Development Environment) of a victim manufacturer with the intent of implanting malware allowing for attack control of the victim IDE environment. The attack then uses this access to exfiltrate sensitive data or information, manipulate said data or information, and conceal these actions. This will allow and aid the attack to meet the goal of future compromise of a recipient of the victim's manufactured product further down in the supply chain.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- The victim must use email or removable media from systems running the IDE (or systems adjacent to the IDE systems).
- The victim must have a system running exploitable applications and/or a vulnerable configuration to allow for initial infiltration.
- The attacker must have working knowledge of some if not all of the components involved in the IDE system as well as the infrastructure.

## Skills Required
- [Medium] Intelligence about the manufacturer's operating environment and infrastructure.
- [High] Ability to develop, deploy, and maintain a stealth malicious backdoor program remotely in what is essentially a hostile environment.
- [High] Development skills to construct malicious attachments that can be used to exploit vulnerabilities in typical desktop applications or system configurations. The malicious attachments should be crafted well enough to bypass typical defensive systems (IDS, anti-virus, etc)

## Mitigations
- Avoid the common delivery mechanisms of adversaries, such as email attachments, which could introduce the malware.


---

# CAPEC-516: Hardware Component Substitution During Baselining

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/516.html  

## Description
An adversary with access to system components during allocated baseline development can substitute a maliciously altered hardware component for a baseline component during the product development and research phases. This can lead to adjustments and calibrations being made in the product so that when the final product, now containing the modified component, is deployed it will not perform as designed and be advantageous to the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- The adversary will need either physical access or be able to supply malicious hardware components to the product development facility.

## Skills Required
- [Medium] Intelligence data on victim's purchasing habits.
- [High] Resources to maliciously construct/alter hardware components used for testing by the supplier.
- [High] Resources to physically infiltrate supplier.

## Mitigations
- Hardware attacks are often difficult to detect, as inserted components can be difficult to identify or remain dormant for an extended period of time.
- Acquire hardware and hardware components from trusted vendors. Additionally, determine where vendors purchase components or if any components are created/acquired via subcontractors to determine where supply chain risks may exist.


---

# CAPEC-517: Documentation Alteration to Circumvent Dial-down

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/517.html  

## Description
An attacker with access to a manufacturer's documentation, which include descriptions of advanced technology and/or specific components' criticality, alters the documents to circumvent dial-down functionality requirements. This alteration would change the interpretation of implementation and manufacturing techniques, allowing for advanced technologies to remain in place even though these technologies might be restricted to certain customers, such as nations on the terrorist watch list, giving the attacker on the receiving end of a shipped product access to an advanced technology that might otherwise be restricted.

## Related Attack Patterns
- ChildOf: CAPEC-447

## Prerequisites
- Advanced knowledge of internal software and hardware components within manufacturer's development environment.
- Access to the manufacturer's documentation.

## Skills Required
- [High] Ability to read, interpret, and subsequently alter manufacturer's documentation to prevent dial-down capabilities.
- [High] Ability to stealthly gain access via remote compromise or physical access to the manufacturer's documentation.

## Mitigations
- Digitize documents and cryptographically sign them to verify authenticity.
- Password protect documents and make them read-only for unauthorized users.
- Avoid emailing important documents and configurations.
- Ensure deleted files are actually deleted.
- Maintain backups of the document for recovery and verification.


---

# CAPEC-518: Documentation Alteration to Produce Under-performing Systems

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/518.html  

## Description
An attacker with access to a manufacturer's documentation alters the descriptions of system capabilities with the intent of causing errors in derived system requirements, impacting the overall effectiveness and capability of the system, allowing an attacker to take advantage of the introduced system capability flaw once the system is deployed.

## Related Attack Patterns
- ChildOf: CAPEC-447

## Prerequisites
- Advanced knowledge of software and hardware capabilities of a manufacturer's product.
- Access to the manufacturer's documentation.

## Skills Required
- [High] Ability to read, interpret, and subsequently alter manufacturer's documentation to misrepresent system capabilities.
- [High] Ability to stealthly gain access via remote compromise or physical access to the manufacturer's documentation.

## Mitigations
- Digitize documents and cryptographically sign them to verify authenticity.
- Password protect documents and make them read-only for unauthorized users.
- Avoid emailing important documents and configurations.
- Ensure deleted files are actually deleted.
- Maintain backups of the document for recovery and verification.
- Separate need-to-know information from system configuration information depending on the user.


---

# CAPEC-519: Documentation Alteration to Cause Errors in System Design

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/519.html  

## Description
An attacker with access to a manufacturer's documentation containing requirements allocation and software design processes maliciously alters the documentation in order to cause errors in system design. This allows the attacker to take advantage of a weakness in a deployed system of the manufacturer for malicious purposes.

## Related Attack Patterns
- ChildOf: CAPEC-447

## Prerequisites
- Advanced knowledge of software capabilities of a manufacturer's product.
- Access to the manufacturer's documentation.

## Skills Required
- [High] Ability to read, interpret, and subsequently alter manufacturer's documentation to cause errors in system design.
- [High] Ability to stealthly gain access via remote compromise or physical access to the manufacturer's documentation.

## Mitigations
- Digitize documents and cryptographically sign them to verify authenticity.
- Password protect documents and make them read-only for unauthorized users.
- Avoid emailing important documents and configurations.
- Ensure deleted files are actually deleted.
- Maintain multiple instances of the document across different privileged users for recovery and verification.


---

# CAPEC-52: Embedding NULL Bytes

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/52.html  

## Description
An adversary embeds one or more null bytes in input to the target software. This attack relies on the usage of a null-valued byte as a string terminator in many environments. The goal is for certain components of the target software to stop processing the input when it encounters the null byte(s).

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- The program does not properly handle postfix NULL terminators

## Skills Required
- [Medium] Directory traversal
- [High] Execution of arbitrary code

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Properly handle the NULL characters supplied as part of user input prior to doing anything with the data.

## Related Weaknesses (CWE)
- CWE-158
- CWE-172
- CWE-173
- CWE-74
- CWE-20
- CWE-697
- CWE-707


---

# CAPEC-520: Counterfeit Hardware Component Inserted During Product Assembly

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/520.html  

## Description
An adversary with either direct access to the product assembly process or to the supply of subcomponents used in the product assembly process introduces counterfeit hardware components into product assembly. The assembly containing the counterfeit components results in a system specifically designed for malicious purposes.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- The adversary will need either physical access or be able to supply malicious hardware components to the product development facility.

## Skills Required
- [High] Resources to maliciously construct components used by the manufacturer.
- [High] Resources to physically infiltrate manufacturer or manufacturer's supplier.

## Mitigations
- Hardware attacks are often difficult to detect, as inserted components can be difficult to identify or remain dormant for an extended period of time.
- Acquire hardware and hardware components from trusted vendors. Additionally, determine where vendors purchase components or if any components are created/acquired via subcontractors to determine where supply chain risks may exist.


---

# CAPEC-521: Hardware Design Specifications Are Altered

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/521.html  

## Description
An attacker with access to a manufacturer's hardware manufacturing process documentation alters the design specifications, which introduces flaws advantageous to the attacker once the system is deployed.

## Related Attack Patterns
- ChildOf: CAPEC-447

## Prerequisites
- Advanced knowledge of hardware capabilities of a manufacturer's product.
- Access to the manufacturer's documentation.

## Skills Required
- [High] Ability to read, interpret, and subsequently alter manufacturer's documentation to cause errors in design specifications.
- [High] Ability to stealthly gain access via remote compromise or physical access to the manufacturer's documentation.

## Mitigations
- Digitize documents and cryptographically sign them to verify authenticity.
- Password protect documents and make them read-only for unauthorized users.
- Avoid emailing important documents and configurations.
- Ensure deleted files are actually deleted.
- Maintain backups of the document for recovery and verification.
- Separate need-to-know information from system configuration information depending on the user.


---

# CAPEC-522: Malicious Hardware Component Replacement

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/522.html  

## Description
An adversary replaces legitimate hardware in the system with faulty counterfeit or tampered hardware in the supply chain distribution channel, with purpose of causing malicious disruption or allowing for additional compromise when the system is deployed.

## Related Attack Patterns
- ChildOf: CAPEC-439

## Prerequisites
- Physical access to the system after it has left the manufacturer but before it is deployed at the victim location.

## Skills Required
- [High] Advanced knowledge of the design of the system.
- [High] Hardware creation and manufacture of replacement components.

## Mitigations
- Ensure that all contractors and sub-suppliers use trusted means of shipping (e.g., bonded/cleared/vetted and insured couriers) to ensure that components, once purchased, are not subject to compromise during their delivery.
- Prevent or detect tampering with critical hardware or firmware components while in transit through use of state-of-the-art anti-tamper devices.
- Use tamper-resistant and tamper-evident packaging when shipping critical components (e.g., plastic coating for circuit boards, tamper tape, paint, sensors, and/or seals for cases and containers) and inspect received system components for evidence of tampering.


---

# CAPEC-523: Malicious Software Implanted

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/523.html  

## Description
An attacker implants malicious software into the system in the supply chain distribution channel, with purpose of causing malicious disruption or allowing for additional compromise when the system is deployed.

## Related Attack Patterns
- ChildOf: CAPEC-439

## Prerequisites
- Physical access to the system after it has left the manufacturer but before it is deployed at the victim location.

## Skills Required
- [High] Advanced knowledge of the design of the system and it's operating system components and subcomponents.
- [High] Malicious software creation.

## Mitigations
- Deploy strong code integrity policies to allow only authorized apps to run.
- Use endpoint detection and response solutions that can automaticalkly detect and remediate suspicious activities.
- Maintain a highly secure build and update infrastructure by immediately applying security patches for OS and software, implementing mandatory integrity controls to ensure only trusted tools run, and requiring multi-factor authentication for admins.
- Require SSL for update channels and implement certificate transparency based verification.
- Sign everything, including configuration files, XML files and packages.
- Develop an incident response process, disclose supply chain incidents and notify customers with accurate and timely information.


---

# CAPEC-524: Rogue Integration Procedures

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/524.html  

## Description
An attacker alters or establishes rogue processes in an integration facility in order to insert maliciously altered components into the system. The attacker would then supply the malicious components. This would allow for malicious disruption or additional compromise when the system is deployed.

## Related Attack Patterns
- ChildOf: CAPEC-439

## Prerequisites
- Physical access to an integration facility that prepares the system before it is deployed at the victim location.

## Skills Required
- [High] Advanced knowledge of the design of the system.
- [High] Hardware creation and manufacture of replacement components.

## Mitigations
- Deploy strong code integrity policies to allow only authorized apps to run.
- Use endpoint detection and response solutions that can automaticalkly detect and remediate suspicious activities.
- Maintain a highly secure build and update infrastructure by immediately applying security patches for OS and software, implementing mandatory integrity controls to ensure only trusted tools run, and requiring multi-factor authentication for admins.
- Require SSL for update channels and implement certificate transparency based verification.
- Sign everything, including configuration files, XML files and packages.
- Develop an incident response process, disclose supply chain incidents and notify customers with accurate and timely information.
- Maintain strong physical system access controls and monitor networks and physical facilities for insider threats.


---

# CAPEC-528: XML Flood

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/528.html  

## Description
An adversary may execute a flooding attack using XML messages with the intent to deny legitimate users access to a web service. These attacks are accomplished by sending a large number of XML based requests and letting the service attempt to parse each one. In many cases this type of an attack will result in a XML Denial of Service (XDoS) due to an application becoming unstable, freezing, or crashing.

## Related Attack Patterns
- ChildOf: CAPEC-125

## Prerequisites
- The target must receive and process XML transactions.
- An adverssary must possess the ability to generate a large amount of XML based messages to send to the target service.

## Skills Required
- [Low] Denial of service

## Consequences
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Design: Build throttling mechanism into the resource allocation. Provide for a timeout mechanism for allocated resources whose transaction does not complete within a specified interval.
- Implementation: Provide for network flow control and traffic shaping to control access to the resources.

## Related Weaknesses (CWE)
- CWE-770


---

# CAPEC-529: Malware-Directed Internal Reconnaissance

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/529.html  

## Description
Adversary uses malware or a similarly controlled application installed inside an organizational perimeter to gather information about the composition, configuration, and security mechanisms of a targeted application, system or network.

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary must have internal, logical access to the target network and system.

## Skills Required
- [Medium] The adversary must be able to obtain or develop, as well as place malicious software inside the target network/system.

## Resources Required
- The adversary requires a variety of tools to collect information about the target. These include port/network scanners and tools to analyze responses from applications to determine version and configuration information. Footprinting a system adequately may also take a few days if the attacker wishes the footprinting attempt to go undetected.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Keep patches up to date by installing weekly or daily if possible.
- Identify programs that may be used to acquire peripheral information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.


---

# CAPEC-53: Postfix, Null Terminate, and Backslash

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/53.html  

## Description
If a string is passed through a filter of some kind, then a terminal NULL may not be valid. Using alternate representation of NULL allows an adversary to embed the NULL mid-string while postfixing the proper data so that the filter is avoided. One example is a filter that looks for a trailing slash character. If a string insertion is possible, but the slash must exist, an alternate encoding of NULL in mid-string may be used.

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- Null terminators are not properly handled by the filter.

## Skills Required
- [Medium] An adversary needs to understand alternate encodings, what the filter looks for and the data format acceptable to the target API

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Properly handle Null characters. Make sure canonicalization is properly applied. Do not pass Null characters to the underlying APIs.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.

## Related Weaknesses (CWE)
- CWE-158
- CWE-172
- CWE-173
- CWE-74
- CWE-20
- CWE-697
- CWE-707


---

# CAPEC-530: Provide Counterfeit Component

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/530.html  

## Description
An attacker provides a counterfeit component during the procurement process of a lower-tier component supplier to a sub-system developer or integrator, which is then built into the system being upgraded or repaired by the victim, allowing the attacker to cause disruption or additional compromise.

## Related Attack Patterns
- ChildOf: CAPEC-531

## Prerequisites
- Advanced knowledge about the target system and sub-components.

## Skills Required
- [High] Able to develop and manufacture malicious system components that resemble legitimate name-brand components.

## Mitigations
- There are various methods to detect if the component is a counterfeit. See section II of [REF-703] for many techniques.


---

# CAPEC-531: Hardware Component Substitution

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/531.html  

## Description
An attacker substitutes out a tested and approved hardware component for a maliciously-altered hardware component. This type of attack is carried out directly on the system, enabling the attacker to then cause disruption or additional compromise.

## Related Attack Patterns
- ChildOf: CAPEC-534

## Prerequisites
- Physical access to the system or the integration facility where hardware components are kept.

## Skills Required
- [High] Able to develop and manufacture malicious system components that perform the same functions and processes as their non-malicious counterparts.


---

# CAPEC-532: Altered Installed BIOS

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/532.html  

## Description
An attacker with access to download and update system software sends a maliciously altered BIOS to the victim or victim supplier/integrator, which when installed allows for future exploitation.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- Advanced knowledge about the installed target system design.
- Advanced knowledge about the download and update installation processes.
- Access to the download and update system(s) used to deliver BIOS images.

## Skills Required
- [High] Able to develop a malicious BIOS image with the original functionality as a normal BIOS image, but with added functionality that allows for later compromise and/or disruption.

## Mitigations
- Deploy strong code integrity policies to allow only authorized apps to run.
- Use endpoint detection and response solutions that can automaticalkly detect and remediate suspicious activities.
- Maintain a highly secure build and update infrastructure by immediately applying security patches for OS and software, implementing mandatory integrity controls to ensure only trusted tools run, and requiring multi-factor authentication for admins.
- Require SSL for update channels and implement certificate transparency based verification.
- Sign update packages and BIOS patches.
- Use hardware security modules/trusted platform modules to verify authenticity using hardware-based cryptography.


---

# CAPEC-533: Malicious Manual Software Update

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/533.html  

## Description
An attacker introduces malicious code to the victim's system by altering the payload of a software update, allowing for additional compromise or site disruption at the victim location. These manual, or user-assisted attacks, vary from requiring the user to download and run an executable, to as streamlined as tricking the user to click a URL. Attacks which aim at penetrating a specific network infrastructure often rely upon secondary attack methods to achieve the desired impact. Spamming, for example, is a common method employed as an secondary attack vector. Thus the attacker has in their arsenal a choice of initial attack vectors ranging from traditional SMTP/POP/IMAP spamming and its varieties, to web-application mechanisms which commonly implement both chat and rich HTML messaging within the user interface.

## Related Attack Patterns
- ChildOf: CAPEC-186

## Prerequisites
- Advanced knowledge about the download and update installation processes.
- Advanced knowledge about the deployed system and its various software subcomponents and processes.

## Skills Required
- [High] Able to develop malicious code that can be used on the victim's system while maintaining normal functionality.

## Mitigations
- Only accept software updates from an official source.

## Related Weaknesses (CWE)
- CWE-494


---

# CAPEC-534: Malicious Hardware Update

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/534.html  

## Description
An adversary introduces malicious hardware during an update or replacement procedure, allowing for additional compromise or site disruption at the victim location. After deployment, it is not uncommon for upgrades and replacements to occur involving hardware and various replaceable parts. These upgrades and replacements are intended to correct defects, provide additional features, and to replace broken or worn-out parts. However, by forcing or tricking the replacement of a good component with a defective or corrupted component, an adversary can leverage known defects to obtain a desired malicious impact.

## Related Attack Patterns
- ChildOf: CAPEC-440

## Skills Required
- [High] Able to develop and manufacture malicious hardware components that perform the same functions and processes as their non-malicious counterparts.


---

# CAPEC-535: Malicious Gray Market Hardware

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/535.html  

## Description
An attacker maliciously alters hardware components that will be sold on the gray market, allowing for victim disruption and compromise when the victim needs replacement hardware components for systems where the parts are no longer in regular supply from original suppliers, or where the hardware components from the attacker seems to be a great benefit from a cost perspective.

## Related Attack Patterns
- ChildOf: CAPEC-531

## Prerequisites
- Physical access to a gray market reseller's hardware components supply, or the ability to appear as a gray market reseller to the victim's buyer.

## Skills Required
- [High] Able to develop and manufacture malicious hardware components that perform the same functions and processes as their non-malicious counterparts.

## Mitigations
- Purchase only from authorized resellers.
- Validate serial numbers from multiple sources


---

# CAPEC-536: Data Injected During Configuration

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/536.html  

## Description
An attacker with access to data files and processes on a victim's system injects malicious data into critical operational data during configuration or recalibration, causing the victim's system to perform in a suboptimal manner that benefits the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-176

## Prerequisites
- The attacker must have previously compromised the victim's systems or have physical access to the victim's systems.
- Advanced knowledge of software and hardware capabilities of a manufacturer's product.

## Skills Required
- [High] Ability to generate and inject false data into operational data into a system with the intent of causing the victim to alter the configuration of the system.

## Mitigations
- Ensure that proper access control is implemented on all systems to prevent unauthorized access to system files and processes.

## Related Weaknesses (CWE)
- CWE-284


---

# CAPEC-537: Infiltration of Hardware Development Environment

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/537.html  

## Description
An adversary, leveraging the ability to manipulate components of primary support systems and tools within the development and production environments, inserts malicious software within the hardware and/or firmware development environment. The infiltration purpose is to alter developed hardware components in a system destined for deployment at the victim's organization, for the purpose of disruption or further compromise.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- The victim must use email or removable media from systems running the IDE (or systems adjacent to the IDE systems).
- The victim must have a system running exploitable applications and/or a vulnerable configuration to allow for initial infiltration.
- The adversary must have working knowledge of some if not all of the components involved in the IDE system as well as the infrastructure.

## Skills Required
- [Medium] Intelligence about the manufacturer's operating environment and infrastructure.
- [High] Ability to develop, deploy, and maintain a stealth malicious backdoor program remotely in what is essentially a hostile environment.
- [High] Development skills to construct malicious attachments that can be used to exploit vulnerabilities in typical desktop applications or system configurations. The malicious attachments should be crafted well enough to bypass typical defensive systems (IDS, anti-virus, etc)

## Mitigations
- Verify software downloads and updates to ensure they have not been modified be adversaries
- Leverage antivirus tools to detect known malware
- Do not download software from untrusted sources
- Educate designers, developers, engineers, etc. on social engineering attacks to avoid downloading malicious software via attacks such as phishing attacks


---

# CAPEC-538: Open-Source Library Manipulation

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/538.html  

## Description
Adversaries implant malicious code in open source software (OSS) libraries to have it widely distributed, as OSS is commonly downloaded by developers and other users to incorporate into software development projects. The adversary can have a particular system in mind to target, or the implantation can be the first stage of follow-on attacks on many systems.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- Access to the open source code base being used by the manufacturer in a system being developed or currently deployed at a victim location.

## Skills Required
- [High] Advanced knowledge about the inclusion and specific usage of an open source code project within system being targeted for infiltration.

## Related Weaknesses (CWE)
- CWE-494
- CWE-829


---

# CAPEC-539: ASIC With Malicious Functionality

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/539.html  

## Description
An attacker with access to the development environment process of an application-specific integrated circuit (ASIC) for a victim system being developed or maintained after initial deployment can insert malicious functionality into the system for the purpose of disruption or further compromise.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- The attacker must have working knowledge of some if not all of the components involved in the target system as well as the infrastructure and development environment of the manufacturer.
- Advanced knowledge about the ASIC installed within the target system.

## Skills Required
- [High] Able to develop and manufacture malicious subroutines for an ASIC environment without degradation of existing functions and processes.


---

# CAPEC-54: Query System for Information

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/54.html  

## Description
An adversary, aware of an application's location (and possibly authorized to use the application), probes an application's structure and evaluates its robustness by submitting requests and examining responses. Often, this is accomplished by sending variants of expected queries in the hope that these modified queries might return information beyond what the expected set of queries would provide.

## Related Attack Patterns
- ChildOf: CAPEC-116

## Prerequisites
- This class of attacks does not strictly require authorized access to the application. As Attackers use this attack process to classify, map, and identify vulnerable aspects of an application, it simply requires hypotheses to be verified, interaction with the application, and time to conduct trial-and-error activities.

## Skills Required
- [Medium] Although fuzzing parameters is not difficult, and often possible with automated fuzzers, interpreting the error conditions and modifying the parameters so as to move further in the process of mapping the application requires detailed knowledge of target platform, the languages and packages used as well as software design.

## Resources Required
- The Attacker needs the ability to probe application functionality and provide it erroneous directives or data without triggering intrusion detection schemes or making enough of an impact on application logging that steps are taken against the adversary. The Attack does not need special hardware, software, skills, or access.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Application designers can construct a 'code book' for error messages. When using a code book, application error messages aren't generated in string or stack trace form, but are cataloged and replaced with a unique (often integer-based) value 'coding' for the error. Such a technique will require helpdesk and hosting personnel to use a 'code book' or similar mapping to decode application errors/logs in order to respond to them normally.
- Application designers can wrap application functionality (preferably through the underlying framework) in an output encoding scheme that obscures or cleanses error messages to prevent such attacks. Such a technique is often used in conjunction with the above 'code book' suggestion.

## Related Weaknesses (CWE)
- CWE-209


---

# CAPEC-540: Overread Buffers

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/540.html  

## Description
An adversary attacks a target by providing input that causes an application to read beyond the boundary of a defined buffer. This typically occurs when a value influencing where to start or stop reading is set to reflect positions outside of the valid memory location of the buffer. This type of attack may result in exposure of sensitive information, a system crash, or arbitrary code execution.

## Related Attack Patterns
- ChildOf: CAPEC-123

## Prerequisites
- For this type of attack to be successful, a few prerequisites must be met. First, the targeted software must be written in a language that enables fine grained buffer control. (e.g., c, c++) Second, the targeted software must actually perform buffer operations and inadequately perform bounds-checking on those buffer operations. Finally, the adversary must have the capability to influence the input that guides these buffer operations.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Unreliable Execution

## Related Weaknesses (CWE)
- CWE-125


---

# CAPEC-541: Application Fingerprinting

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/541.html  

## Description
An adversary engages in fingerprinting activities to determine the type or version of an application installed on a remote target.

## Related Attack Patterns
- ChildOf: CAPEC-224

## Prerequisites
- None

## Related Weaknesses (CWE)
- CWE-204
- CWE-205
- CWE-208


---

# CAPEC-542: Targeted Malware

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/542.html  

## Description
An adversary develops targeted malware that takes advantage of a known vulnerability in an organizational information technology environment. The malware crafted for these attacks is based specifically on information gathered about the technology environment. Successfully executing the malware enables an adversary to achieve a wide variety of negative technical impacts.

## Related Attack Patterns
- ChildOf: CAPEC-549
- CanPrecede: CAPEC-662


---

# CAPEC-543: Counterfeit Websites

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/543.html  

## Description
Adversary creates duplicates of legitimate websites. When users visit a counterfeit site, the site can gather information or upload malware.

## Related Attack Patterns
- ChildOf: CAPEC-194
- CanPrecede: CAPEC-89

## Prerequisites
- None


---

# CAPEC-544: Counterfeit Organizations

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/544.html  

## Description
An adversary creates a false front organizations with the appearance of a legitimate supplier in the critical life cycle path that then injects corrupted/malicious information system components into the organizational supply chain.

## Related Attack Patterns
- ChildOf: CAPEC-194

## Prerequisites
- None


---

# CAPEC-545: Pull Data from System Resources

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/545.html  

## Description
An adversary who is authorized or has the ability to search known system resources, does so with the intention of gathering useful information. System resources include files, memory, and other aspects of the target system. In this pattern of attack, the adversary does not necessarily know what they are going to find when they start pulling data. This is different than CAPEC-150 where the adversary knows what they are looking for due to the common location.

## Related Attack Patterns
- ChildOf: CAPEC-116

## Related Weaknesses (CWE)
- CWE-1239
- CWE-1243
- CWE-1258
- CWE-1266
- CWE-1272
- CWE-1278
- CWE-1323
- CWE-1258
- CWE-1330


---

# CAPEC-546: Incomplete Data Deletion in a Multi-Tenant Environment

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/546.html  

## Description
An adversary obtains unauthorized information due to insecure or incomplete data deletion in a multi-tenant environment. If a cloud provider fails to completely delete storage and data from former cloud tenants' systems/resources, once these resources are allocated to new, potentially malicious tenants, the latter can probe the provided resources for sensitive information still there.

## Related Attack Patterns
- ChildOf: CAPEC-545

## Prerequisites
- The cloud provider must not assuredly delete part or all of the sensitive data for which they are responsible.The adversary must have the ability to interact with the system.

## Skills Required
- [Low] The adversary requires the ability to traverse directory structure.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Cloud providers should completely delete data to render it irrecoverable and inaccessible from any layer and component of infrastructure resources.
- Deletion of data should be completed promptly when requested.

## Related Weaknesses (CWE)
- CWE-284
- CWE-1266
- CWE-1272


---

# CAPEC-547: Physical Destruction of Device or Component

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/547.html  

## Description
An adversary conducts a physical attack a device or component, destroying it such that it no longer functions as intended.

## Related Attack Patterns
- ChildOf: CAPEC-607


---

# CAPEC-548: Contaminate Resource

**Abstraction:** Meta  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/548.html  

## Description
An adversary contaminates organizational information systems (including devices and networks) by causing them to handle information of a classification/sensitivity for which they have not been authorized. When this happens, the contaminated information system, device, or network must be brought offline to investigate and mitigate the data spill, which denies availability of the system until the investigation is complete.

## Related Attack Patterns
- CanPrecede: CAPEC-607

## Prerequisites
- The adversary needs to have real or fake classified/sensitive information to place on a system

## Skills Required
- [Low] Knowledge of classification levels of systems
- [High] The ability to obtain a classified document or information
- [Low] The ability to fake a classified document

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Properly safeguard classified/sensitive data. This includes training cleared individuals to ensure they are handling and disposing of this data properly, as well as ensuring systems only handle information of the classification level they are designed for.
- Design systems with redundancy in mind. This could mean creating backing servers that could be switched over to in the event that a server has to be taken down for investigation.
- Have a planned and efficient response plan to limit the amount of time a system is offline while the contamination is investigated.


---

# CAPEC-549: Local Execution of Code

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/549.html  

## Description
An adversary installs and executes malicious code on the target system in an effort to achieve a negative technical impact. Examples include rootkits, ransomware, spyware, adware, and others.

## Prerequisites
- Knowledge of the target system's vulnerabilities that can be capitalized on with malicious code.The adversary must be able to place the malicious code on the target system.

## Resources Required
- The means by which the adversary intends to place the malicious code on the system dictates the tools required. For example, suppose the adversary wishes to leverage social engineering and convince a legitimate user to open a malicious file attached to a seemingly legitimate email. In this case, the adversary might require a tool capable of wrapping malicious code into an innocuous filetype (e.g., PDF, .doc, etc.)

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Integrity, Availability; Impact: Other

## Mitigations
- Employ robust cybersecurity training for all employees.
- Implement system antivirus software that scans all attachments before opening them.
- Regularly patch all software.
- Execute all suspicious files in a sandbox environment.

## Related Weaknesses (CWE)
- CWE-829


---

# CAPEC-55: Rainbow Table Password Cracking

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/55.html  

## Description
An attacker gets access to the database table where hashes of passwords are stored. They then use a rainbow table of pre-computed hash chains to attempt to look up the original password. Once the original password corresponding to the hash is obtained, the attacker uses the original password to gain access to the system.

## Related Attack Patterns
- ChildOf: CAPEC-49
- CanPrecede: CAPEC-600
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-560
- CanPrecede: CAPEC-561
- CanPrecede: CAPEC-653

## Prerequisites
- Hash of the original password is available to the attacker. For a better chance of success, an attacker should have more than one hash of the original password, and ideally the whole table.
- Salt was not used to create the hash of the original password. Otherwise the rainbow tables have to be re-computed, which is very expensive and will make the attack effectively infeasible (especially if salt was added in iterations).
- The system uses one factor password based authentication.

## Skills Required
- [Low] A variety of password cracking tools are available that can leverage a rainbow table. The more difficult part is to obtain the password hash(es) in the first place.

## Resources Required
- Rainbow table of password hash chains with the right algorithm used. A password cracking tool that leverages this rainbow table will also be required. Hash(es) of the password is required.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Use salt when computing password hashes. That is, concatenate the salt (random bits) with the original password prior to hashing it.

## Related Weaknesses (CWE)
- CWE-261
- CWE-521
- CWE-262
- CWE-263
- CWE-654
- CWE-916
- CWE-308
- CWE-309


---

# CAPEC-550: Install New Service

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/550.html  

## Description
When an operating system starts, it also starts programs called services or daemons. Adversaries may install a new service which will be executed at startup (on a Windows system, by modifying the registry). The service name may be disguised by using a name from a related operating system or benign software. Services are usually run with elevated privileges.

## Related Attack Patterns
- ChildOf: CAPEC-542

## Mitigations
- Limit privileges of user accounts so new service creation can only be performed by authorized administrators.

## Related Weaknesses (CWE)
- CWE-284


---

# CAPEC-551: Modify Existing Service

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/551.html  

## Description
When an operating system starts, it also starts programs called services or daemons. Modifying existing services may break existing services or may enable services that are disabled/not commonly used.

## Related Attack Patterns
- ChildOf: CAPEC-542

## Mitigations
- Limit privileges of user accounts so service changes can only be performed by authorized administrators. Also monitor any service changes that may occur inadvertently.

## Related Weaknesses (CWE)
- CWE-284
- CWE-522


---

# CAPEC-552: Install Rootkit 

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/552.html  

## Description
An adversary exploits a weakness in authentication to install malware that alters the functionality and information provide by targeted operating system API calls. Often referred to as rootkits, it is often used to hide the presence of programs, files, network connections, services, drivers, and other system components.

## Related Attack Patterns
- ChildOf: CAPEC-542

## Mitigations
- Prevent adversary access to privileged accounts necessary to install rootkits.

## Related Weaknesses (CWE)
- CWE-284


---

# CAPEC-554: Functionality Bypass

**Abstraction:** Meta  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/554.html  

## Description
An adversary attacks a system by bypassing some or all functionality intended to protect it. Often, a system user will think that protection is in place, but the functionality behind those protections has been disabled by the adversary.

## Related Weaknesses (CWE)
- CWE-424
- CWE-1299


---

# CAPEC-555: Remote Services with Stolen Credentials

**Abstraction:** Standard  
**Status:** Stable  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/555.html  

## Description
This pattern of attack involves an adversary that uses stolen credentials to leverage remote services such as RDP, telnet, SSH, and VNC to log into a system. Once access is gained, any number of malicious activities could be performed.

## Related Attack Patterns
- ChildOf: CAPEC-560
- CanPrecede: CAPEC-151

## Mitigations
- Disable RDP, telnet, SSH and enable firewall rules to block such traffic. Limit users and accounts that have remote interactive login access. Remove the Local Administrators group from the list of groups allowed to login through RDP. Limit remote user permissions. Use remote desktop gateways and multifactor authentication for remote logins.

## Related Weaknesses (CWE)
- CWE-522
- CWE-308
- CWE-309
- CWE-294
- CWE-263
- CWE-262
- CWE-521


---

# CAPEC-556: Replace File Extension Handlers

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/556.html  

## Description
When a file is opened, its file handler is checked to determine which program opens the file. File handlers are configuration properties of many operating systems. Applications can modify the file handler for a given file extension to call an arbitrary program when a file with the given extension is opened.

## Related Attack Patterns
- ChildOf: CAPEC-542

## Mitigations
- Inspect registry for changes. Limit privileges of user accounts so changes to default file handlers can only be performed by authorized administrators.

## Related Weaknesses (CWE)
- CWE-284


---

# CAPEC-557: DEPRECATED: Schedule Software To Run

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/557.html  

## Description
This CAPEC has been deprecated because it is not directly related to a weakness, social engineering, supply chains, or a physical-based attack.


---

# CAPEC-558: Replace Trusted Executable

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/558.html  

## Description
An adversary exploits weaknesses in privilege management or access control to replace a trusted executable with a malicious version and enable the execution of malware when that trusted executable is called.

## Related Attack Patterns
- ChildOf: CAPEC-542

## Related Weaknesses (CWE)
- CWE-284


---

# CAPEC-559: Orbital Jamming

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/559.html  

## Description
In this attack pattern, the adversary sends disruptive signals at a target satellite using a rogue uplink station to disrupt the intended transmission. Those within the satellite's footprint are prevented from reaching the satellite's targeted or neighboring channels. The satellite's footprint size depends upon its position in the sky; higher orbital satellites cover multiple continents.

## Related Attack Patterns
- ChildOf: CAPEC-601

## Prerequisites
- This attack requires the knowledge of the satellite's coordinates for targeting.

## Resources Required
- A satellite uplink station.

## Consequences
- Scope: Availability; Impact: Other


---

# CAPEC-56: DEPRECATED: Removing/short-circuiting 'guard logic'

**Abstraction:** Standard  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/56.html  

## Description
This attack pattern has been deprecated as it is a duplicate of CAPEC-207 : Removing Important Client Functionality. Please refer to this other pattern going forward.


---

# CAPEC-560: Use of Known Domain Credentials

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/560.html  

## Description
An adversary guesses or obtains (i.e. steals or purchases) legitimate credentials (e.g. userID/password) to achieve authentication and to perform authorized actions under the guise of an authenticated user or service.

## Related Attack Patterns
- CanPrecede: CAPEC-151

## Prerequisites
- The system/application uses one factor password based authentication, SSO, and/or cloud-based authentication.
- The system/application does not have a sound password policy that is being enforced.
- The system/application does not implement an effective password throttling mechanism.
- The adversary possesses a list of known user accounts and corresponding passwords that may exist on the target.

## Skills Required
- [Low] Once an adversary obtains a known credential, leveraging it is trivial.

## Resources Required
- A list of known credentials.
- A custom script that leverages the credential list to launch an attack.

## Consequences
- Scope: Confidentiality, Access Control, Authentication; Impact: Gain Privileges
- Scope: Confidentiality, Authorization; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Leverage multi-factor authentication for all authentication services and prior to granting an entity access to the domain network.
- Create a strong password policy and ensure that your system enforces this policy.
- Ensure users are not reusing username/password combinations for multiple systems, applications, or services.
- Do not reuse local administrator account credentials across systems.
- Deny remote use of local admin credentials to log into domain systems.
- Do not allow accounts to be a local administrator on more than one system.
- Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-2.
- Monitor system and domain logs for abnormal credential access.

## Related Weaknesses (CWE)
- CWE-522
- CWE-307
- CWE-308
- CWE-309
- CWE-262
- CWE-263
- CWE-654
- CWE-1273


---

# CAPEC-561: Windows Admin Shares with Stolen Credentials

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/561.html  

## Description
An adversary guesses or obtains (i.e. steals or purchases) legitimate Windows administrator credentials (e.g. userID/password) to access Windows Admin Shares on a local machine or within a Windows domain.

## Related Attack Patterns
- ChildOf: CAPEC-653
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-165
- CanPrecede: CAPEC-549
- CanPrecede: CAPEC-545

## Prerequisites
- The system/application is connected to the Windows domain.
- The target administrative share allows remote use of local admin credentials to log into domain systems.
- The adversary possesses a list of known Windows administrator credentials that exist on the target domain.

## Skills Required
- [Low] Once an adversary obtains a known Windows credential, leveraging it is trivial.

## Resources Required
- A list of known Windows administrator credentials for the targeted domain.

## Consequences
- Scope: Confidentiality, Access Control, Authentication; Impact: Gain Privileges
- Scope: Confidentiality, Authorization; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Do not reuse local administrator account credentials across systems.
- Deny remote use of local admin credentials to log into domain systems.
- Do not allow accounts to be a local administrator on more than one system.

## Related Weaknesses (CWE)
- CWE-522
- CWE-308
- CWE-309
- CWE-294
- CWE-263
- CWE-262
- CWE-521


---

# CAPEC-562: Modify Shared File

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/562.html  

## Description
An adversary manipulates the files in a shared location by adding malicious programs, scripts, or exploit code to valid content. Once a user opens the shared content, the tainted content is executed.

## Related Attack Patterns
- ChildOf: CAPEC-17

## Mitigations
- Disallow shared content. Protect shared folders by minimizing users that have write access. Use utilities that mitigate exploitation like the Microsoft Enhanced Mitigation Experience Toolkit (EMET) to prevent exploits from being run.

## Related Weaknesses (CWE)
- CWE-284


---

# CAPEC-563: Add Malicious File to Shared Webroot

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/563.html  

## Description
An adversaries may add malicious content to a website through the open file share and then browse to that content with a web browser to cause the server to execute the content. The malicious content will typically run under the context and permissions of the web server process, often resulting in local system or administrative privileges depending on how the web server is configured.

## Related Attack Patterns
- ChildOf: CAPEC-17

## Mitigations
- Ensure proper permissions on directories that are accessible through a web server. Disallow remote access to the web root. Disable execution on directories within the web root. Ensure that permissions of the web server process are only what is required by not using built-in accounts and instead create specific accounts to limit unnecessary access or permissions overlap across multiple systems.

## Related Weaknesses (CWE)
- CWE-284


---

# CAPEC-564: Run Software at Logon

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/564.html  

## Description
Operating system allows logon scripts to be run whenever a specific user or users logon to a system. If adversaries can access these scripts, they may insert additional code into the logon script. This code can allow them to maintain persistence or move laterally within an enclave because it is executed every time the affected user or users logon to a computer. Modifying logon scripts can effectively bypass workstation and enclave firewalls. Depending on the access configuration of the logon scripts, either local credentials or a remote administrative account may be necessary.

## Related Attack Patterns
- ChildOf: CAPEC-542

## Mitigations
- Restrict write access to logon scripts to necessary administrators.

## Related Weaknesses (CWE)
- CWE-284


---

# CAPEC-565: Password Spraying

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/565.html  

## Description
In a Password Spraying attack, an adversary tries a small list (e.g. 3-5) of common or expected passwords, often matching the target's complexity policy, against a known list of user accounts to gain valid credentials. The adversary tries a particular password for each user account, before moving onto the next password in the list. This approach assists the adversary in remaining undetected by avoiding rapid or frequent account lockouts. The adversary may then reattempt the process with additional passwords, once enough time has passed to prevent inducing a lockout.

## Related Attack Patterns
- ChildOf: CAPEC-49
- CanPrecede: CAPEC-600
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-560
- CanPrecede: CAPEC-561
- CanPrecede: CAPEC-653

## Prerequisites
- The system/application uses one factor password based authentication.
- The system/application does not have a sound password policy that is being enforced.
- The system/application does not implement an effective password throttling mechanism.
- The adversary possesses a list of known user accounts on the target system/application.

## Skills Required
- [Low] A Password Spraying attack is very straightforward. A variety of password cracking tools are widely available.

## Resources Required
- A machine with sufficient resources for the job (e.g. CPU, RAM, HD).
- Applicable password lists.
- A password cracking tool or a custom script that leverages the password list to launch the attack.

## Consequences
- Scope: Confidentiality, Access Control, Authentication; Impact: Gain Privileges
- Scope: Confidentiality, Authorization; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Create a strong password policy and ensure that your system enforces this policy.
- Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-2.
- Leverage multi-factor authentication for all authentication services and prior to granting an entity access to the domain network.

## Related Weaknesses (CWE)
- CWE-521
- CWE-262
- CWE-263
- CWE-654
- CWE-307
- CWE-308
- CWE-309


---

# CAPEC-566: DEPRECATED: Dump Password Hashes

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/566.html  

## Description
This CAPEC has been deprecated because of is not directly related to a weakness, social engineering, supply chains, or a physical-based attack.


---

# CAPEC-567: DEPRECATED: Obtain Data via Utilities

**Abstraction:** Standard  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/567.html  

## Description
This CAPEC has been deprecated because it is not directly related to a weakness, social engineering, supply chains, or a physical-based attack.


---

# CAPEC-568: Capture Credentials via Keylogger

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/568.html  

## Description
An adversary deploys a keylogger in an effort to obtain credentials directly from a system's user. After capturing all the keystrokes made by a user, the adversary can analyze the data and determine which string are likely to be passwords or other credential related information.

## Related Attack Patterns
- ChildOf: CAPEC-569
- CanPrecede: CAPEC-600
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-560
- CanPrecede: CAPEC-561
- CanPrecede: CAPEC-653

## Prerequisites
- The ability to install the keylogger, either in person or remote.

## Mitigations
- Strong physical security can help reduce the ability of an adversary to install a keylogger.


---

# CAPEC-569: Collect Data as Provided by Users

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/569.html  

## Description
An attacker leverages a tool, device, or program to obtain specific information as provided by a user of the target system. This information is often needed by the attacker to launch a follow-on attack. This attack is different than Social Engineering as the adversary is not tricking or deceiving the user. Instead the adversary is putting a mechanism in place that captures the information that a user legitimately enters into a system. Deploying a keylogger, performing a UAC prompt, or wrapping the Windows default credential provider are all examples of such interactions.

## Related Attack Patterns
- ChildOf: CAPEC-116


---

# CAPEC-57: Utilizing REST's Trust in the System Resource to Obtain Sensitive Data

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/57.html  

## Description
This attack utilizes a REST(REpresentational State Transfer)-style applications' trust in the system resources and environment to obtain sensitive data once SSL is terminated.

## Related Attack Patterns
- ChildOf: CAPEC-157

## Prerequisites
- Opportunity to intercept must exist beyond the point where SSL is terminated.
- The adversary must be able to insert a listener actively (proxying the communication) or passively (sniffing the communication) in the client-server communication path.

## Skills Required
- [Low] To insert a network sniffer or other listener into the communication stream

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Implementation: Implement message level security such as HMAC in the HTTP communication
- Design: Utilize defense in depth, do not rely on a single security mechanism like SSL
- Design: Enforce principle of least privilege

## Related Weaknesses (CWE)
- CWE-300
- CWE-287
- CWE-693


---

# CAPEC-570: DEPRECATED: Signature-Based Avoidance

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/570.html  

## Description
This CAPEC has been deprecated because it is not directly related to a weakness, social engineering, supply chains, or a physical-based attack.


---

# CAPEC-571: Block Logging to Central Repository

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/571.html  

## Description
An adversary prevents host-generated logs being delivered to a central location in an attempt to hide indicators of compromise.

## Related Attack Patterns
- ChildOf: CAPEC-161


---

# CAPEC-572: Artificially Inflate File Sizes

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/572.html  

## Description
An adversary modifies file contents by adding data to files for several reasons. Many different attacks could “follow” this pattern resulting in numerous outcomes. Adding data to a file could also result in a Denial of Service condition for devices with limited storage capacity.

## Related Attack Patterns
- ChildOf: CAPEC-165

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Integrity; Impact: Modify Data


---

# CAPEC-573: Process Footprinting

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/573.html  

## Description
An adversary exploits functionality meant to identify information about the currently running processes on the target system to an authorized user. By knowing what processes are running on the target system, the adversary can learn about the target environment as a means towards further malicious behavior.

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Mitigations
- Identify programs that may be used to acquire process information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-574: Services Footprinting

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/574.html  

## Description
An adversary exploits functionality meant to identify information about the services on the target system to an authorized user. By knowing what services are registered on the target system, the adversary can learn about the target environment as a means towards further malicious behavior. Depending on the operating system, commands that can obtain services information include "sc" and "tasklist/svc" using Tasklist, and "net start" using Net.

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Mitigations
- Identify programs that may be used to acquire service information and block them by using a software restriction policy or tools that restrict program execution by uaing a process allowlist.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-575: Account Footprinting

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/575.html  

## Description
An adversary exploits functionality meant to identify information about the domain accounts and their permissions on the target system to an authorized user. By knowing what accounts are registered on the target system, the adversary can inform further and more targeted malicious behavior. Example Windows commands which can acquire this information are: "net user" and "dsquery".

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Mitigations
- Identify programs that may be used to acquire account information and block them by using a software restriction policy or tools that restrict program execution by uysing a process allowlist.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-576: Group Permission Footprinting

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/576.html  

## Description
An adversary exploits functionality meant to identify information about user groups and their permissions on the target system to an authorized user. By knowing what users/permissions are registered on the target system, the adversary can inform further and more targeted malicious behavior. An example Windows command which can list local groups is "net localgroup".

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Mitigations
- Identify programs (such as "net") that may be used to enumerate local group permissions and block them by using a software restriction Policy or tools that restrict program execution by using a process allowlist.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-577: Owner Footprinting

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/577.html  

## Description
An adversary exploits functionality meant to identify information about the primary users on the target system to an authorized user. They may do this, for example, by reviewing logins or file modification times. By knowing what owners use the target system, the adversary can inform further and more targeted malicious behavior. An example Windows command that may accomplish this is "dir /A ntuser.dat". Which will display the last modified time of a user's ntuser.dat file when run within the root folder of a user. This time is synonymous with the last time that user was logged in.

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.
- Administrator permissions are required to view the home folder of other users.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Mitigations
- Ensure that proper permissions on files and folders are enacted to limit accessibility.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-578: Disable Security Software

**Abstraction:** Standard  
**Status:** Usable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/578.html  

## Description
An adversary exploits a weakness in access control to disable security tools so that detection does not occur. This can take the form of killing processes, deleting registry keys so that tools do not start at run time, deleting log files, or other methods.

## Related Attack Patterns
- ChildOf: CAPEC-176

## Prerequisites
- The adversary must have the capability to interact with the configuration of the targeted system.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Availability; Impact: Hide Activities

## Mitigations
- Ensure proper permissions are in place to prevent adversaries from altering the execution status of security tools.

## Related Weaknesses (CWE)
- CWE-284


---

# CAPEC-579: Replace Winlogon Helper DLL

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/579.html  

## Description
Winlogon is a part of Windows that performs logon actions. In Windows systems prior to Windows Vista, a registry key can be modified that causes Winlogon to load a DLL on startup. Adversaries may take advantage of this feature to load adversarial code at startup.

## Related Attack Patterns
- ChildOf: CAPEC-542

## Mitigations
- Changes to registry entries in "HKLM\Software\Microsoft\Windows NT\Winlogon\Notify" that do not correlate with known software, patch cycles, etc are suspicious. New DLLs written to System32 which do not correlate with known good software or patching may be suspicious.

## Related Weaknesses (CWE)
- CWE-15


---

# CAPEC-58: Restful Privilege Elevation

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/58.html  

## Description
An adversary identifies a Rest HTTP (Get, Put, Delete) style permission method allowing them to perform various malicious actions upon server data due to lack of access control mechanisms implemented within the application service accepting HTTP messages.

## Related Attack Patterns
- ChildOf: CAPEC-1
- ChildOf: CAPEC-180

## Prerequisites
- The attacker needs to be able to identify HTTP Get URLs. The Get methods must be set to call applications that perform operations other than get such as update and delete.

## Skills Required
- [Low] It is relatively straightforward to identify an HTTP Get method that changes state on the server side and executes against an over-privileged system interface

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Design: Enforce principle of least privilege
- Implementation: Ensure that HTTP Get methods only retrieve state and do not alter state on the server side
- Implementation: Ensure that HTTP methods have proper ACLs based on what the functionality they expose

## Related Weaknesses (CWE)
- CWE-267
- CWE-269


---

# CAPEC-580: System Footprinting

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/580.html  

## Description
An adversary engages in active probing and exploration activities to determine security information about a remote target system. Often times adversaries will rely on remote applications that can be probed for system configurations.

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary must have logical access to the target network and system.

## Skills Required
- [Low] The adversary needs to know basic linux commands.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Keep patches up to date by installing weekly or daily if possible.
- Identify programs that may be used to acquire peripheral information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.

## Related Weaknesses (CWE)
- CWE-204
- CWE-205
- CWE-208


---

# CAPEC-581: Security Software Footprinting

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/581.html  

## Description
Adversaries may attempt to get a listing of security tools that are installed on the system and their configurations. This may include security related system features (such as a built-in firewall or anti-spyware) as well as third-party security software.

## Related Attack Patterns
- ChildOf: CAPEC-580

## Mitigations
- Identify programs that may be used to acquire security tool information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.


---

# CAPEC-582: Route Disabling

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/582.html  

## Description
An adversary disables the network route between two targets. The goal is to completely sever the communications channel between two entities. This is often the result of a major error or the use of an "Internet kill switch" by those in control of critical infrastructure. This attack pattern differs from most other obstruction patterns by targeting the route itself, as opposed to the data passed over the route.

## Related Attack Patterns
- ChildOf: CAPEC-607

## Prerequisites
- The adversary requires knowledge of and access to network route.

## Consequences
- Scope: Availability; Impact: Other


---

# CAPEC-583: Disabling Network Hardware

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/583.html  

## Description
In this attack pattern, an adversary physically disables networking hardware by powering it down or disconnecting critical equipment. Disabling or shutting off critical system resources prevents them from performing their service as intended, which can have direct and indirect consequences on other systems. This attack pattern is considerably less technical than the selective blocking used in most obstruction attacks.

## Related Attack Patterns
- ChildOf: CAPEC-582

## Prerequisites
- The adversary requires physical access to the targeted communications equipment (networking devices, cables, etc.), which may be spread over a wide area.

## Consequences
- Scope: Availability; Impact: Other

## Mitigations
- Ensure rigorous physical defensive measures to keep the adversary from accessing critical systems..


---

# CAPEC-584: BGP Route Disabling

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/584.html  

## Description
An adversary suppresses the Border Gateway Protocol (BGP) advertisement for a route so as to render the underlying network inaccessible. The BGP protocol helps traffic move throughout the Internet by selecting the most efficient route between Autonomous Systems (AS), or routing domains. BGP is the basis for interdomain routing infrastructure, providing connections between these ASs. By suppressing the intended AS routing advertisements and/or forcing less effective routes for traffic to ASs, the adversary can deny availability for the target network.

## Related Attack Patterns
- ChildOf: CAPEC-582

## Prerequisites
- The adversary must have control of a router that can modify, drop, or introduce spoofed BGP updates.The adversary can convince

## Resources Required
- BGP Router

## Consequences
- Scope: Availability; Impact: Other

## Mitigations
- Implement Ingress filters to check the validity of received routes. However, this relies on the accuracy of Internet Routing Registries (IRRs) databases which are often not well-maintained.
- Implement Secure BGP (S-BGP protocol), which improves authorization and authentication capabilities based on public-key cryptography.


---

# CAPEC-585: DNS Domain Seizure

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/585.html  

## Description
In this attack pattern, an adversary influences a target's web-hosting company to disable a target domain. The goal is to prevent access to the targeted service provided by that domain. It usually occurs as the result of civil or criminal legal interventions.

## Related Attack Patterns
- ChildOf: CAPEC-582

## Prerequisites
- This attack pattern requires that the adversary has cooperation from the registrar of the target domain.

## Consequences
- Scope: Availability; Impact: Other


---

# CAPEC-586: Object Injection

**Abstraction:** Meta  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/586.html  

## Description
An adversary attempts to exploit an application by injecting additional, malicious content during its processing of serialized objects. Developers leverage serialization in order to convert data or state into a static, binary format for saving to disk or transferring over a network. These objects are then deserialized when needed to recover the data/state. By injecting a malformed object into a vulnerable application, an adversary can potentially compromise the application by manipulating the deserialization process. This can result in a number of unwanted outcomes, including remote code execution.

## Prerequisites
- The target application must unserialize data before validation.

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Integrity; Impact: Modify Data
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Implementation: Validate object before deserialization process
- Design: Limit which types can be deserialized.
- Implementation: Avoid having unnecessary types or gadgets available that can be leveraged for malicious ends. Use an allowlist of acceptable classes.
- Implementation: Keep session state on the server, when possible.

## Related Weaknesses (CWE)
- CWE-502


---

# CAPEC-587: Cross Frame Scripting (XFS)

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/587.html  

## Description
This attack pattern combines malicious Javascript and a legitimate webpage loaded into a concealed iframe. The malicious Javascript is then able to interact with a legitimate webpage in a manner that is unknown to the user. This attack usually leverages some element of social engineering in that an attacker must convinces a user to visit a web page that the attacker controls.

## Related Attack Patterns
- ChildOf: CAPEC-103

## Prerequisites
- The user's browser must have vulnerabilities in its implementation of the same-origin policy. It allows certain data in a loaded page to originate from different servers/domains.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Avoid clicking on untrusted links.
- Employ techniques such as frame busting, which is a method by which developers aim to prevent their site being loaded within a frame.

## Related Weaknesses (CWE)
- CWE-1021


---

# CAPEC-588: DOM-Based XSS

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/588.html  

## Description
This type of attack is a form of Cross-Site Scripting (XSS) where a malicious script is inserted into the client-side HTML being parsed by a web browser. Content served by a vulnerable web application includes script code used to manipulate the Document Object Model (DOM). This script code either does not properly validate input, or does not perform proper output encoding, thus creating an opportunity for an adversary to inject a malicious script launch a XSS attack. A key distinction between other XSS attacks and DOM-based attacks is that in other XSS attacks, the malicious script runs when the vulnerable web page is initially loaded, while a DOM-based attack executes sometime after the page loads. Another distinction of DOM-based attacks is that in some cases, the malicious script is never sent to the vulnerable web server at all. An attack like this is guaranteed to bypass any server-side filtering attempts to protect users.

## Related Attack Patterns
- ChildOf: CAPEC-63

## Prerequisites
- An application that leverages a client-side web browser with scripting enabled.
- An application that manipulates the DOM via client-side scripting.
- An application that failS to adequately sanitize or encode untrusted input.

## Skills Required
- [Medium] Requires the ability to write scripts of some complexity and to inject it through user controlled fields in the system.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Authorization, Access Control; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Use browser technologies that do not allow client-side scripting.
- Utilize proper character encoding for all output produced within client-site scripts manipulating the DOM.
- Ensure that all user-supplied input is validated before use.

## Related Weaknesses (CWE)
- CWE-79
- CWE-20
- CWE-83


---

# CAPEC-589: DNS Blocking

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/589.html  

## Description
An adversary intercepts traffic and intentionally drops DNS requests based on content in the request. In this way, the adversary can deny the availability of specific services or content to the user even if the IP address is changed.

## Related Attack Patterns
- ChildOf: CAPEC-603

## Prerequisites
- This attack requires the ability to conduct deep packet inspection with an In-Path device that can drop the targeted traffic and/or connection.

## Consequences
- Scope: Availability; Impact: Other

## Mitigations
- Hard Coded Alternate DNS server in applications
- Avoid dependence on DNS
- Include "hosts file"/IP address in the application.
- Ensure best practices with respect to communications channel protections.
- Use a .onion domain with Tor support

## Related Weaknesses (CWE)
- CWE-300


---

# CAPEC-59: Session Credential Falsification through Prediction

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/59.html  

## Description
This attack targets predictable session ID in order to gain privileges. The attacker can predict the session ID used during a transaction to perform spoofing and session hijacking.

## Related Attack Patterns
- ChildOf: CAPEC-196

## Prerequisites
- The target host uses session IDs to keep track of the users.
- Session IDs are used to control access to resources.
- The session IDs used by the target host are predictable. For example, the session IDs are generated using predictable information (e.g., time).

## Skills Required
- [Low] There are tools to brute force session ID. Those tools require a low level of knowledge.
- [Medium] Predicting Session ID may require more computation work which uses advanced analysis such as statistical analysis.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Use a strong source of randomness to generate a session ID.
- Use adequate length session IDs
- Do not use information available to the user in order to generate session ID (e.g., time).
- Ideas for creating random numbers are offered by Eastlake [RFC1750]
- Encrypt the session ID if you expose it to the user. For instance session ID can be stored in a cookie in encrypted format.

## Related Weaknesses (CWE)
- CWE-290
- CWE-330
- CWE-331
- CWE-346
- CWE-488
- CWE-539
- CWE-200
- CWE-6
- CWE-285
- CWE-384
- CWE-693


---

# CAPEC-590: IP Address Blocking

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/590.html  

## Description
An adversary performing this type of attack drops packets destined for a target IP address. The aim is to prevent access to the service hosted at the target IP address.

## Related Attack Patterns
- ChildOf: CAPEC-603

## Prerequisites
- This attack requires the ability to conduct deep packet inspection with an In-Path device that can drop the targeted traffic and/or connection.

## Consequences
- Scope: Availability; Impact: Other

## Mitigations
- Have a large pool of backup IPs built into the application and support proxy capability in the application.

## Related Weaknesses (CWE)
- CWE-300


---

# CAPEC-591: Reflected XSS

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/591.html  

## Description
This type of attack is a form of Cross-Site Scripting (XSS) where a malicious script is "reflected" off a vulnerable web application and then executed by a victim's browser. The process starts with an adversary delivering a malicious script to a victim and convincing the victim to send the script to the vulnerable web application.

## Related Attack Patterns
- ChildOf: CAPEC-63

## Prerequisites
- An application that leverages a client-side web browser with scripting enabled.
- An application that fail to adequately sanitize or encode untrusted input.

## Skills Required
- [Medium] Requires the ability to write malicious scripts and embed them into HTTP requests.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Authorization, Access Control; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Use browser technologies that do not allow client-side scripting.
- Utilize strict type, character, and encoding enforcement.
- Ensure that all user-supplied input is validated before use.

## Related Weaknesses (CWE)
- CWE-79


---

# CAPEC-592: Stored XSS

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/592.html  

## Description
An adversary utilizes a form of Cross-site Scripting (XSS) where a malicious script is persistently "stored" within the data storage of a vulnerable web application as valid input.

## Related Attack Patterns
- ChildOf: CAPEC-63

## Prerequisites
- An application that leverages a client-side web browser with scripting enabled.
- An application that fails to adequately sanitize or encode untrusted input.
- An application that stores information provided by the user in data storage of some kind.

## Skills Required
- [Medium] Requires the ability to write scripts of varying complexity and to inject them through user controlled fields within the application.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Authorization, Access Control; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Use browser technologies that do not allow client-side scripting.
- Utilize strict type, character, and encoding enforcement.
- Ensure that all user-supplied input is validated before being stored.

## Related Weaknesses (CWE)
- CWE-79


---

# CAPEC-593: Session Hijacking

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/593.html  

## Description
This type of attack involves an adversary that exploits weaknesses in an application's use of sessions in performing authentication. The adversary is able to steal or manipulate an active session and use it to gain unathorized access to the application.

## Related Attack Patterns
- ChildOf: CAPEC-21

## Prerequisites
- An application that leverages sessions to perform authentication.

## Skills Required
- [Low] Exploiting a poorly protected identity token is a well understood attack with many helpful resources available.

## Resources Required
- The adversary must have the ability to communicate with the application over the network.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Gain Privileges

## Mitigations
- Properly encrypt and sign identity tokens in transit, and use industry standard session key generation mechanisms that utilize high amount of entropy to generate the session key. Many standard web and application servers will perform this task on your behalf. Utilize a session timeout for all sessions. If the user does not explicitly logout, terminate their session after this period of inactivity. If the user logs back in then a new session key should be generated.

## Related Weaknesses (CWE)
- CWE-287


---

# CAPEC-594: Traffic Injection

**Abstraction:** Meta  
**Status:** Stable  
**Reference:** https://capec.mitre.org/data/definitions/594.html  

## Description
An adversary injects traffic into the target's network connection. The adversary is therefore able to degrade or disrupt the connection, and potentially modify the content. This is not a flooding attack, as the adversary is not focusing on exhausting resources. Instead, the adversary is crafting a specific input to affect the system in a particular way.

## Prerequisites
- The target application must leverage an open communications channel.
- The channel on which the target communicates must be vulnerable to interception (e.g., adversary in the middle attack - CAPEC-94).

## Resources Required
- A tool, such as a MITM Proxy, that is capable of generating and injecting custom inputs to be used in the attack.

## Consequences
- Scope: Availability; Impact: Unreliable Execution
- Scope: Integrity; Impact: Other

## Related Weaknesses (CWE)
- CWE-940


---

# CAPEC-595: Connection Reset

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/595.html  

## Description
In this attack pattern, an adversary injects a connection reset packet to one or both ends of a target's connection. The attacker is therefore able to have the target and/or the destination server sever the connection without having to directly filter the traffic between them.

## Related Attack Patterns
- ChildOf: CAPEC-594

## Prerequisites
- This attack requires the ability to monitor the target's network connection.

## Related Weaknesses (CWE)
- CWE-940


---

# CAPEC-596: TCP RST Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/596.html  

## Description
An adversary injects one or more TCP RST packets to a target after the target has made a HTTP GET request. The goal of this attack is to have the target and/or destination web server terminate the TCP connection.

## Related Attack Patterns
- ChildOf: CAPEC-595

## Prerequisites
- An On/In Path Device

## Related Weaknesses (CWE)
- CWE-940


---

# CAPEC-597: Absolute Path Traversal

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/597.html  

## Description
An adversary with access to file system resources, either directly or via application logic, will use various file absolute paths and navigation mechanisms such as ".." to extend their range of access to inappropriate areas of the file system. The goal of the adversary is to access directories and files that are intended to be restricted from their access.

## Related Attack Patterns
- ChildOf: CAPEC-126

## Prerequisites
- The target must leverage and access an underlying file system.

## Skills Required
- [Low] Simple command line attacks.
- [Medium] Programming attacks.

## Resources Required
- The attacker must have access to an application interface or a direct shell that allows them to inject directory strings and monitor the results.

## Consequences
- Scope: Integrity, Confidentiality, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Design: Configure the access control correctly.
- Design: Enforce principle of least privilege.
- Design: Execute programs with constrained privileges, so parent process does not open up further vulnerabilities. Ensure that all directories, temporary directories and files, and memory are executing with limited privileges to protect against remote execution.
- Design: Input validation. Assume that user inputs are malicious. Utilize strict type, character, and encoding enforcement.
- Design: Proxy communication to host, so that communications are terminated at the proxy, sanitizing the requests before forwarding to server host.
- Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.
- Implementation: Host integrity monitoring for critical files, directories, and processes. The goal of host integrity monitoring is to be aware when a security issue has occurred so that incident response and other forensic activities can begin.
- Implementation: Perform input validation for all remote content, including remote and user-generated content.
- Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.
- Implementation: Use indirect references rather than actual file names.
- Implementation: Use possible permissions on file access when developing and deploying web applications.
- Implementation: Validate user input by only accepting known good. Ensure all content that is delivered to client is sanitized against an acceptable content specification using an allowlist approach.

## Related Weaknesses (CWE)
- CWE-36


---

# CAPEC-598: DNS Spoofing

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/598.html  

## Description
An adversary sends a malicious ("NXDOMAIN" ("No such domain") code, or DNS A record) response to a target's route request before a legitimate resolver can. This technique requires an On-path or In-path device that can monitor and respond to the target's DNS requests. This attack differs from BGP Tampering in that it directly responds to requests made by the target instead of polluting the routing the target's infrastructure uses.

## Related Attack Patterns
- ChildOf: CAPEC-194

## Prerequisites
- On/In Path Device

## Skills Required
- [Low] To distribute email

## Mitigations
- Design: Avoid dependence on DNS
- Design: Include "hosts file"/IP address in the application
- Implementation: Utilize a .onion domain with Tor support
- Implementation: DNSSEC
- Implementation: DNS-hold-open


---

# CAPEC-599: Terrestrial Jamming

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/599.html  

## Description
In this attack pattern, the adversary transmits disruptive signals in the direction of the target's consumer-level satellite dish (as opposed to the satellite itself). The transmission disruption occurs in a more targeted range. Portable terrestrial jammers have a range of 3-5 kilometers in urban areas and 20 kilometers in rural areas. This technique requires a terrestrial jammer that is more powerful than the frequencies sent from the satellite.

## Related Attack Patterns
- ChildOf: CAPEC-195

## Resources Required
- A terrestrial satellite jammer with a signal more powerful than that of the satellite attempting to communicate with the target. The adversary must know the location of the target satellite dish.

## Consequences
- Scope: Availability; Impact: Other


---

# CAPEC-6: Argument Injection

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/6.html  

## Description
An attacker changes the behavior or state of a targeted application through injecting data or command syntax through the targets use of non-validated and non-filtered arguments of exposed services or methods.

## Related Attack Patterns
- ChildOf: CAPEC-137

## Prerequisites
- Target software fails to strip all user-supplied input of any content that could cause the shell to perform unexpected actions.
- Software must allow for unvalidated or unfiltered input to be executed on operating system shell, and, optionally, the system configuration must allow for output to be sent back to client.

## Skills Required
- [Medium] The attacker has to identify injection vector, identify the operating system-specific commands, and optionally collect the output.

## Resources Required
- Ability to communicate synchronously or asynchronously with server. Optionally, ability to capture output directly through synchronous communication or other method such as FTP.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Design: Do not program input values directly on command shell, instead treat user input as guilty until proven innocent. Build a function that takes user input and converts it to applications specific types and values, stripping or filtering out all unauthorized commands and characters in the process.
- Design: Limit program privileges, so if metacharacters or other methods circumvent program input validation routines and shell access is attained then it is not running under a privileged account. chroot jails create a sandbox for the application to execute in, making it more difficult for an attacker to elevate privilege even in the case that a compromise has occurred.
- Implementation: Implement an audit log that is written to a separate host, in the event of a compromise the audit log may be able to provide evidence and details of the compromise.

## Related Weaknesses (CWE)
- CWE-74
- CWE-146
- CWE-184
- CWE-78
- CWE-185
- CWE-697


---

# CAPEC-60: Reusing Session IDs (aka Session Replay)

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/60.html  

## Description
This attack targets the reuse of valid session ID to spoof the target system in order to gain privileges. The attacker tries to reuse a stolen session ID used previously during a transaction to perform spoofing and session hijacking. Another name for this type of attack is Session Replay.

## Related Attack Patterns
- ChildOf: CAPEC-593

## Prerequisites
- The target host uses session IDs to keep track of the users.
- Session IDs are used to control access to resources.
- The session IDs used by the target host are not well protected from session theft.

## Skills Required
- [Low] If an attacker can steal a valid session ID, they can then try to be authenticated with that stolen session ID.
- [Medium] More sophisticated attack can be used to hijack a valid session from a user and spoof a legitimate user by reusing their valid session ID.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Always invalidate a session ID after the user logout.
- Setup a session time out for the session IDs.
- Protect the communication between the client and server. For instance it is best practice to use SSL to mitigate adversary in the middle attacks (CAPEC-94).
- Do not code send session ID with GET method, otherwise the session ID will be copied to the URL. In general avoid writing session IDs in the URLs. URLs can get logged in log files, which are vulnerable to an attacker.
- Encrypt the session data associated with the session ID.
- Use multifactor authentication.

## Related Weaknesses (CWE)
- CWE-294
- CWE-290
- CWE-346
- CWE-384
- CWE-488
- CWE-539
- CWE-200
- CWE-285
- CWE-664
- CWE-732


---

# CAPEC-600: Credential Stuffing

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/600.html  

## Description
An adversary tries known username/password combinations against different systems, applications, or services to gain additional authenticated access. Credential Stuffing attacks rely upon the fact that many users leverage the same username/password combination for multiple systems, applications, and services.

## Related Attack Patterns
- ChildOf: CAPEC-560
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-653

## Prerequisites
- The system/application uses one factor password based authentication, SSO, and/or cloud-based authentication.
- The system/application does not have a sound password policy that is being enforced.
- The system/application does not implement an effective password throttling mechanism.
- The adversary possesses a list of known user accounts and corresponding passwords that may exist on the target.

## Skills Required
- [Low] A Credential Stuffing attack is very straightforward.

## Resources Required
- A machine with sufficient resources for the job (e.g. CPU, RAM, HD).
- A known list of username/password combinations.
- A custom script that leverages the credential list to launch the attack.

## Consequences
- Scope: Confidentiality, Access Control, Authentication; Impact: Gain Privileges
- Scope: Confidentiality, Authorization; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Leverage multi-factor authentication for all authentication services and prior to granting an entity access to the domain network.
- Create a strong password policy and ensure that your system enforces this policy.
- Ensure users are not reusing username/password combinations for multiple systems, applications, or services.
- Do not reuse local administrator account credentials across systems.
- Deny remote use of local admin credentials to log into domain systems.
- Do not allow accounts to be a local administrator on more than one system.
- Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-2.
- Monitor system and domain logs for abnormal credential access.

## Related Weaknesses (CWE)
- CWE-522
- CWE-307
- CWE-308
- CWE-309
- CWE-262
- CWE-263
- CWE-654


---

# CAPEC-601: Jamming

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/601.html  

## Description
An adversary uses radio noise or signals in an attempt to disrupt communications. By intentionally overwhelming system resources with illegitimate traffic, service is denied to the legitimate traffic of authorized users.

## Related Attack Patterns
- ChildOf: CAPEC-607

## Consequences
- Scope: Availability; Impact: Other


---

# CAPEC-602: DEPRECATED: Degradation

**Abstraction:** Meta  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/602.html  

## Description
This attack pattern has been deprecated.


---

# CAPEC-603: Blockage

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/603.html  

## Description
An adversary blocks the delivery of an important system resource causing the system to fail or stop working.

## Related Attack Patterns
- ChildOf: CAPEC-607

## Prerequisites
- This attack pattern requires knowledge of where important system resources are logically located as well as how they operate.

## Consequences
- Scope: Availability; Impact: Other


---

# CAPEC-604: Wi-Fi Jamming

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/604.html  

## Description
In this attack scenario, the attacker actively transmits on the Wi-Fi channel to prevent users from transmitting or receiving data from the targeted Wi-Fi network. There are several known techniques to perform this attack – for example: the attacker may flood the Wi-Fi access point (e.g. the retransmission device) with deauthentication frames. Another method is to transmit high levels of noise on the RF band used by the Wi-Fi network.

## Related Attack Patterns
- ChildOf: CAPEC-601

## Prerequisites
- Lack of anti-jam features in 802.11
- Lack of authentication on deauthentication/disassociation packets on 802.11-based networks

## Skills Required
- [Low] This attack can be performed by low capability attackers with freely available tools. Commercial tools are also available that can target select networks or all WiFi networks within a range of several miles.

## Consequences
- Scope: Availability; Impact: Other
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Countermeasures have been proposed for both disassociation flooding and RF jamming, however these countermeasures are not standardized and would need to be supported on both the retransmission device and the handset in order to be effective. Commercial products are not currently available that support jamming countermeasures for Wi-Fi.


---

# CAPEC-605: Cellular Jamming

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/605.html  

## Description
In this attack scenario, the attacker actively transmits signals to overpower and disrupt the communication between a cellular user device and a cell tower. Several existing techniques are known in the open literature for this attack for 2G, 3G, and 4G LTE cellular technology. For example, some attacks target cell towers by overwhelming them with false status messages, while others introduce high levels of noise on signaling channels.

## Related Attack Patterns
- ChildOf: CAPEC-601

## Prerequisites
- Lack of anti-jam features in cellular technology (2G, 3G, 4G, LTE)

## Skills Required
- [Low] This attack can be performed by low capability attackers with commercially available tools.

## Consequences
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Mitigating this attack requires countermeasures employed on both the retransmission device as well as on the cell tower. Therefore, any system that relies on existing commercial cell towards will likely be vulnerable to this attack. By using a private cellular LTE network (i.e., a custom cell tower), jamming countermeasures could be developed and employed.


---

# CAPEC-606: Weakening of Cellular Encryption

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/606.html  

## Description
An attacker, with control of a Cellular Rogue Base Station or through cooperation with a Malicious Mobile Network Operator can force the mobile device (e.g., the retransmission device) to use no encryption (A5/0 mode) or to use easily breakable encryption (A5/1 or A5/2 mode).

## Related Attack Patterns
- ChildOf: CAPEC-620

## Prerequisites
- Cellular devices that allow negotiating security modes to facilitate backwards compatibility and roaming on legacy networks.

## Skills Required
- [Medium] Adversaries can purchase and implement rogue BTS stations at a cost effective rate, and can push a mobile device to downgrade to a non-secure cellular protocol like 2G over GSM or CDMA.

## Consequences
- Scope: Confidentiality; Impact: Other

## Mitigations
- Use of hardened baseband firmware on retransmission device to detect and prevent the use of weak cellular encryption.
- Monitor cellular RF interface to detect the usage of weaker-than-expected cellular encryption.

## Related Weaknesses (CWE)
- CWE-757


---

# CAPEC-607: Obstruction

**Abstraction:** Meta  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/607.html  

## Description
An attacker obstructs the interactions between system components. By interrupting or disabling these interactions, an adversary can often force the system into a degraded state or cause the system to stop working as intended. This can cause the system components to be unavailable until the obstruction mitigated.

## Consequences
- Scope: Availability; Impact: Resource Consumption


---

# CAPEC-608: Cryptanalysis of Cellular Encryption

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/608.html  

## Description
The use of cryptanalytic techniques to derive cryptographic keys or otherwise effectively defeat cellular encryption to reveal traffic content. Some cellular encryption algorithms such as A5/1 and A5/2 (specified for GSM use) are known to be vulnerable to such attacks and commercial tools are available to execute these attacks and decrypt mobile phone conversations in real-time. Newer encryption algorithms in use by UMTS and LTE are stronger and currently believed to be less vulnerable to these types of attacks. Note, however, that an attacker with a Cellular Rogue Base Station can force the use of weak cellular encryption even by newer mobile devices.

## Related Attack Patterns
- ChildOf: CAPEC-97

## Prerequisites
- None

## Skills Required
- [Medium] Adversaries can rent commercial supercomputer time globally to conduct cryptanalysis on encrypted data captured from mobile devices. Foreign governments have their own cryptanalysis technology and capabilities. Commercial cellular standards for encryption (GSM and CDMA) are also subject to adversary cryptanalysis.

## Consequences
- Scope: Confidentiality; Impact: Other

## Mitigations
- Use of hardened baseband firmware on retransmission device to detect and prevent the use of weak cellular encryption.
- Monitor cellular RF interface to detect the usage of weaker-than-expected cellular encryption.

## Related Weaknesses (CWE)
- CWE-327


---

# CAPEC-609: Cellular Traffic Intercept

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/609.html  

## Description
Cellular traffic for voice and data from mobile devices and retransmission devices can be intercepted via numerous methods. Malicious actors can deploy their own cellular tower equipment and intercept cellular traffic surreptitiously. Additionally, government agencies of adversaries and malicious actors can intercept cellular traffic via the telecommunications backbone over which mobile traffic is transmitted.

## Related Attack Patterns
- ChildOf: CAPEC-157

## Prerequisites
- None

## Skills Required
- [Medium] Adversaries can purchase hardware and software solutions, or create their own solutions, to capture/intercept cellular radio traffic. The cost of a basic Base Transceiver Station (BTS) to broadcast to local mobile cellular radios in mobile devices has dropped to very affordable costs. The ability of commercial cellular providers to monitor for "rogue" BTS stations is poor in many areas and it is assumed that "rogue" BTS stations exist in urban areas.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Encryption of all data packets emanating from the smartphone to a retransmission device via two encrypted tunnels with Suite B cryptography, all the way to the VPN gateway at the datacenter.

## Related Weaknesses (CWE)
- CWE-311


---

# CAPEC-61: Session Fixation

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/61.html  

## Description
The attacker induces a client to establish a session with the target software using a session identifier provided by the attacker. Once the user successfully authenticates to the target software, the attacker uses the (now privileged) session identifier in their own transactions. This attack leverages the fact that the target software either relies on client-generated session identifiers or maintains the same session identifiers after privilege elevation.

## Related Attack Patterns
- ChildOf: CAPEC-593

## Prerequisites
- Session identifiers that remain unchanged when the privilege levels change.
- Permissive session management mechanism that accepts random user-generated session identifiers
- Predictable session identifiers

## Skills Required
- [Low] Only basic skills are required to determine and fixate session identifiers in a user's browser. Subsequent attacks may require greater skill levels depending on the attackers' motives.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Use a strict session management mechanism that only accepts locally generated session identifiers: This prevents attackers from fixating session identifiers of their own choice.
- Regenerate and destroy session identifiers when there is a change in the level of privilege: This ensures that even though a potential victim may have followed a link with a fixated identifier, a new one is issued when the level of privilege changes.
- Use session identifiers that are difficult to guess or brute-force: One way for the attackers to obtain valid session identifiers is by brute-forcing or guessing them. By choosing session identifiers that are sufficiently random, brute-forcing or guessing becomes very difficult.

## Related Weaknesses (CWE)
- CWE-384
- CWE-664
- CWE-732


---

# CAPEC-610: Cellular Data Injection

**Abstraction:** Standard  
**Status:** Stable  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/610.html  

## Description
Adversaries inject data into mobile technology traffic (data flows or signaling data) to disrupt communications or conduct additional surveillance operations.

## Related Attack Patterns
- ChildOf: CAPEC-240

## Prerequisites
- None

## Skills Required
- [High] Often achieved by nation states in conjunction with commercial cellular providers to conduct cellular traffic intercept and possible traffic injection.

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Availability; Impact: Modify Data

## Mitigations
- Commercial defensive technology to detect and alert to any attempts to modify mobile technology data flows or to inject new data into existing data flows and signaling data.


---

# CAPEC-611: BitSquatting

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/611.html  

## Description
An adversary registers a domain name one bit different than a trusted domain. A BitSquatting attack leverages random errors in memory to direct Internet traffic to adversary-controlled destinations. BitSquatting requires no exploitation or complicated reverse engineering, and is operating system and architecture agnostic. Experimental observations show that BitSquatting popular websites could redirect non-trivial amounts of Internet traffic to a malicious entity.

## Related Attack Patterns
- ChildOf: CAPEC-616
- CanPrecede: CAPEC-89
- CanPrecede: CAPEC-543

## Prerequisites
- An adversary requires knowledge of popular or high traffic domains, that could be used to deceive potential targets.

## Skills Required
- [Low] Adversaries must be able to register DNS hostnames/URL’s.

## Consequences
- Scope: Other; Impact: Other

## Mitigations
- Authenticate all servers and perform redundant checks when using DNS hostnames.
- When possible, use error-correcting (ECC) memory in local devices as non-ECC memory is significantly more vulnerable to faults.


---

# CAPEC-612: WiFi MAC Address Tracking

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/612.html  

## Description
In this attack scenario, the attacker passively listens for WiFi messages and logs the associated Media Access Control (MAC) addresses. These addresses are intended to be unique to each wireless device (although they can be configured and changed by software). Once the attacker is able to associate a MAC address with a particular user or set of users (for example, when attending a public event), the attacker can then scan for that MAC address to track that user in the future.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- None

## Skills Required
- [Low] Open source and commercial software tools are available and several commercial advertising companies routinely set up tools to collect and monitor MAC addresses.

## Mitigations
- Automatic randomization of WiFi MAC addresses
- Frequent changing of handset and retransmission device

## Related Weaknesses (CWE)
- CWE-201
- CWE-300


---

# CAPEC-613: WiFi SSID Tracking

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/613.html  

## Description
In this attack scenario, the attacker passively listens for WiFi management frame messages containing the Service Set Identifier (SSID) for the WiFi network. These messages are frequently transmitted by WiFi access points (e.g., the retransmission device) as well as by clients that are accessing the network (e.g., the handset/mobile device). Once the attacker is able to associate an SSID with a particular user or set of users (for example, when attending a public event), the attacker can then scan for this SSID to track that user in the future.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- None

## Skills Required
- [Low] Open source and commercial software tools are available and open databases of known WiFi SSID addresses are available online.

## Mitigations
- Do not enable the feature of "Hidden SSIDs" (also known as "Network Cloaking") – this option disables the usual broadcasting of the SSID by the access point, but forces the mobile handset to send requests on all supported radio channels which contains the SSID. The result is that tracking of the mobile device becomes easier since it is transmitting the SSID more frequently.
- Frequently change the SSID to new and unrelated values

## Related Weaknesses (CWE)
- CWE-201
- CWE-300


---

# CAPEC-614: Rooting SIM Cards

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/614.html  

## Description
SIM cards are the de facto trust anchor of mobile devices worldwide. The cards protect the mobile identity of subscribers, associate devices with phone numbers, and increasingly store payment credentials, for example in NFC-enabled phones with mobile wallets. This attack leverages over-the-air (OTA) updates deployed via cryptographically-secured SMS messages to deliver executable code to the SIM. By cracking the DES key, an attacker can send properly signed binary SMS messages to a device, which are treated as Java applets and are executed on the SIM. These applets are allowed to send SMS, change voicemail numbers, and query the phone location, among many other predefined functions. These capabilities alone provide plenty of potential for abuse.

## Related Attack Patterns
- ChildOf: CAPEC-186

## Prerequisites
- A SIM card that relies on the DES cipher.

## Skills Required
- [Medium] This is a sophisticated attack, but detailed techniques are published in open literature.

## Consequences
- Scope: Confidentiality, Integrity; Impact: Execute Unauthorized Commands

## Mitigations
- Upgrade the SIM card to use the state-of-the-art AES or the somewhat outdated 3DES algorithm for OTA.

## Related Weaknesses (CWE)
- CWE-327


---

# CAPEC-615: Evil Twin Wi-Fi Attack

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/615.html  

## Description
Adversaries install Wi-Fi equipment that acts as a legitimate Wi-Fi network access point. When a device connects to this access point, Wi-Fi data traffic is intercepted, captured, and analyzed. This also allows the adversary to use "adversary-in-the-middle" (CAPEC-94) for all communications.

## Related Attack Patterns
- ChildOf: CAPEC-616

## Prerequisites
- None

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Commercial defensive technology that monitors for rogue Wi-Fi access points, adversary-in-the-middle attacks, and anomalous activity with the mobile device baseband radios.

## Related Weaknesses (CWE)
- CWE-300


---

# CAPEC-616: Establish Rogue Location

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/616.html  

## Description
An adversary provides a malicious version of a resource at a location that is similar to the expected location of a legitimate resource. After establishing the rogue location, the adversary waits for a victim to visit the location and access the malicious resource.

## Related Attack Patterns
- ChildOf: CAPEC-154
- CanPrecede: CAPEC-691

## Prerequisites
- A resource is expected to available to the user.

## Skills Required
- [Low] Adversaries can often purchase low-cost technology to implement rogue access points.

## Consequences
- Scope: Confidentiality, Integrity; Impact: Other

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-617: Cellular Rogue Base Station

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/617.html  

## Description
In this attack scenario, the attacker imitates a cellular base station with their own "rogue" base station equipment. Since cellular devices connect to whatever station has the strongest signal, the attacker can easily convince a targeted cellular device (e.g. the retransmission device) to talk to the rogue base station.

## Related Attack Patterns
- ChildOf: CAPEC-616

## Prerequisites
- None

## Skills Required
- [Low] This technique has been demonstrated by amateur hackers and commercial tools and open source projects are available to automate the attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Passively monitor cellular network connection for real-time threat detection and logging for manual review.


---

# CAPEC-618: Cellular Broadcast Message Request

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/618.html  

## Description
In this attack scenario, the attacker uses knowledge of the target’s mobile phone number (i.e., the number associated with the SIM used in the retransmission device) to cause the cellular network to send broadcast messages to alert the mobile device. Since the network knows which cell tower the target’s mobile device is attached to, the broadcast messages are only sent in the Location Area Code (LAC) where the target is currently located. By triggering the cellular broadcast message and then listening for the presence or absence of that message, an attacker could verify that the target is in (or not in) a given location.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Prerequisites
- The attacker must have knowledge of the target’s mobile phone number.

## Skills Required
- [Low] Open source and commercial tools are available for this attack.

## Consequences
- Scope: Other; Impact: Other

## Mitigations
- Frequent changing of mobile number.

## Related Weaknesses (CWE)
- CWE-201


---

# CAPEC-619: Signal Strength Tracking

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/619.html  

## Description
In this attack scenario, the attacker passively monitors the signal strength of the target’s cellular RF signal or WiFi RF signal and uses the strength of the signal (with directional antennas and/or from multiple listening points at once) to identify the source location of the signal. Obtaining the signal of the target can be accomplished through multiple techniques such as through Cellular Broadcast Message Request or through the use of IMSI Tracking or WiFi MAC Address Tracking.

## Related Attack Patterns
- ChildOf: CAPEC-292

## Skills Required
- [Low] Commercial tools are available.

## Related Weaknesses (CWE)
- CWE-201


---

# CAPEC-62: Cross Site Request Forgery

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/62.html  

## Description
An attacker crafts malicious web links and distributes them (via web pages, email, etc.), typically in a targeted manner, hoping to induce users to click on the link and execute the malicious action against some third-party application. If successful, the action embedded in the malicious link will be processed and accepted by the targeted application with the users' privilege level. This type of attack leverages the persistence and implicit trust placed in user session cookies by many web applications today. In such an architecture, once the user authenticates to an application and a session cookie is created on the user's system, all following transactions for that session are authenticated using that cookie including potential actions initiated by an attacker and simply "riding" the existing session cookie.

## Related Attack Patterns
- ChildOf: CAPEC-21

## Skills Required
- [Medium] The attacker needs to figure out the exact invocation of the targeted malicious action and then craft a link that performs the said action. Having the user click on such a link is often accomplished by sending an email or posting such a link to a bulletin board or the likes.

## Resources Required
- All the attacker needs is the exact representation of requests to be made to the application and to be able to get the malicious link across to a victim.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Use cryptographic tokens to associate a request with a specific action. The token can be regenerated at every request so that if a request with an invalid token is encountered, it can be reliably discarded. The token is considered invalid if it arrived with a request other than the action it was supposed to be associated with.
- Although less reliable, the use of the optional HTTP Referrer header can also be used to determine whether an incoming request was actually one that the user is authorized for, in the current context.
- Additionally, the user can also be prompted to confirm an action every time an action concerning potentially sensitive data is invoked. This way, even if the attacker manages to get the user to click on a malicious link and request the desired action, the user has a chance to recover by denying confirmation. This solution is also implicitly tied to using a second factor of authentication before performing such actions.
- In general, every request must be checked for the appropriate authentication token as well as authorization in the current session context.

## Related Weaknesses (CWE)
- CWE-352
- CWE-306
- CWE-664
- CWE-732
- CWE-1275


---

# CAPEC-620: Drop Encryption Level

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/620.html  

## Description
An attacker forces the encryption level to be lowered, thus enabling a successful attack against the encrypted data.

## Related Attack Patterns
- ChildOf: CAPEC-212

## Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism

## Related Weaknesses (CWE)
- CWE-757


---

# CAPEC-621: Analysis of Packet Timing and Sizes

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/621.html  

## Description
An attacker may intercept and log encrypted transmissions for the purpose of analyzing metadata such as packet timing and sizes. Although the actual data may be encrypted, this metadata may reveal valuable information to an attacker. Note that this attack is applicable to VOIP data as well as application data, especially for interactive apps that require precise timing and low-latency (e.g. thin-clients).

## Related Attack Patterns
- ChildOf: CAPEC-189

## Prerequisites
- Use of untrusted communication paths enables an attacker to intercept and log communications, including metadata such as packet timing and sizes.

## Skills Required
- [High] These attacks generally require sophisticated machine learning techniques and require traffic capture as a prerequisite.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Distort packet sizes and timing at VPN layer by adding padding to normalize packet sizes and timing delays to reduce information leakage via timing.

## Related Weaknesses (CWE)
- CWE-201


---

# CAPEC-622: Electromagnetic Side-Channel Attack

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/622.html  

## Description
In this attack scenario, the attacker passively monitors electromagnetic emanations that are produced by the targeted electronic device as an unintentional side-effect of its processing. From these emanations, the attacker derives information about the data that is being processed (e.g. the attacker can recover cryptographic keys by monitoring emanations associated with cryptographic processing). This style of attack requires proximal access to the device, however attacks have been demonstrated at public conferences that work at distances of up to 10-15 feet. There have not been any significant studies to determine the maximum practical distance for such attacks. Since the attack is passive, it is nearly impossible to detect and the targeted device will continue to operate as normal after a successful attack.

## Related Attack Patterns
- ChildOf: CAPEC-189

## Prerequisites
- Proximal access to the device.

## Skills Required
- [Medium] Sophisticated attack, but detailed techniques published in the open literature.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Utilize side-channel resistant implementations of all crypto algorithms.
- Strong physical security of all devices that contain secret key information. (even when devices are not in use)

## Related Weaknesses (CWE)
- CWE-201


---

# CAPEC-623: Compromising Emanations Attack

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/623.html  

## Description
Compromising Emanations (CE) are defined as unintentional signals which an attacker may intercept and analyze to disclose the information processed by the targeted equipment. Commercial mobile devices and retransmission devices have displays, buttons, microchips, and radios that emit mechanical emissions in the form of sound or vibrations. Capturing these emissions can help an adversary understand what the device is doing.

## Related Attack Patterns
- ChildOf: CAPEC-189

## Prerequisites
- Proximal access to the device.

## Skills Required
- [High] Sophisticated attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- None are known.

## Related Weaknesses (CWE)
- CWE-201


---

# CAPEC-624: Hardware Fault Injection

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/624.html  

## Description
The adversary uses disruptive signals or events, or alters the physical environment a device operates in, to cause faulty behavior in electronic devices. This can include electromagnetic pulses, laser pulses, clock glitches, ambient temperature extremes, and more. When performed in a controlled manner on devices performing cryptographic operations, this faulty behavior can be exploited to derive secret key information.

## Prerequisites
- Physical access to the system
- The adversary must be cognizant of where fault injection vulnerabilities exist in the system in order to leverage them for exploitation.

## Skills Required
- [High] Adversaries require non-trivial technical skills to create and implement fault injection attacks. Although this style of attack has become easier (commercial equipment and training classes are available to perform these attacks), they usual require significant setup and experimentation time during which physical access to the device is required.

## Resources Required
- The relevant sensors and tools to detect and analyze fault/side-channel data from a system. A tool capable of injecting fault/side-channel data into a system or application.

## Consequences
- Scope: Confidentiality; Impact: Read Data, Bypass Protection Mechanism, Hide Activities
- Scope: Integrity; Impact: Execute Unauthorized Commands

## Mitigations
- Implement robust physical security countermeasures and monitoring.

## Related Weaknesses (CWE)
- CWE-1247
- CWE-1248
- CWE-1256
- CWE-1319
- CWE-1332
- CWE-1334
- CWE-1338
- CWE-1351


---

# CAPEC-625: Mobile Device Fault Injection

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/625.html  

## Description
Fault injection attacks against mobile devices use disruptive signals or events (e.g. electromagnetic pulses, laser pulses, clock glitches, etc.) to cause faulty behavior. When performed in a controlled manner on devices performing cryptographic operations, this faulty behavior can be exploited to derive secret key information. Although this attack usually requires physical control of the mobile device, it is non-destructive, and the device can be used after the attack without any indication that secret keys were compromised.

## Related Attack Patterns
- ChildOf: CAPEC-624

## Skills Required
- [High] Adversaries require non-trivial technical skills to create and implement fault injection attacks on mobile devices. Although this style of attack has become easier (commercial equipment and training classes are available to perform these attacks), they usual require significant setup and experimentation time during which physical access to the device is required. This prerequisite makes the attack challenging to perform (assuming that physical security countermeasures and monitoring are in place).

## Consequences
- Scope: Confidentiality, Access Control; Impact: Read Data

## Mitigations
- Strong physical security of all devices that contain secret key information. (even when devices are not in use)
- Frequent changes to secret keys and certificates.

## Related Weaknesses (CWE)
- CWE-1247
- CWE-1248
- CWE-1256
- CWE-1319
- CWE-1332
- CWE-1334
- CWE-1338
- CWE-1351


---

# CAPEC-626: Smudge Attack

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/626.html  

## Description
Attacks that reveal the password/passcode pattern on a touchscreen device by detecting oil smudges left behind by the user’s fingers.

## Related Attack Patterns
- ChildOf: CAPEC-395

## Prerequisites
- The attacker must have physical access to the device.

## Skills Required
- [Medium] The attacker must know how to make use of these smudges.

## Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism

## Mitigations
- Strong physical security of the device.


---

# CAPEC-627: Counterfeit GPS Signals

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/627.html  

## Description
An adversary attempts to deceive a GPS receiver by broadcasting counterfeit GPS signals, structured to resemble a set of normal GPS signals. These spoofed signals may be structured in such a way as to cause the receiver to estimate its position to be somewhere other than where it actually is, or to be located where it is but at a different time, as determined by the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-148

## Prerequisites
- The target must be relying on valid GPS signal to perform critical operations.

## Skills Required
- [High] The ability to spoof GPS signals is not trival.

## Resources Required
- Ability to create spoofed GPS signals.

## Consequences
- Scope: Integrity; Impact: Modify Data


---

# CAPEC-628: Carry-Off GPS Attack

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/628.html  

## Description
A common form of a GPS spoofing attack, commonly termed a carry-off attack begins with an adversary broadcasting signals synchronized with the genuine signals observed by the target receiver. The power of the counterfeit signals is then gradually increased and drawn away from the genuine signals. Over time, the adversary can carry the target away from their intended destination and toward a location chosen by the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-627

## Prerequisites
- The target must be relying on valid GPS signal to perform critical operations.

## Skills Required
- [High] This attack requires advanced knoweldge in GPS technology.


---

# CAPEC-629: DEPRECATED: Unauthorized Use of Device Resources

**Abstraction:** Standard  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/629.html  

## Description
This attack pattern has been deprecated.


---

# CAPEC-63: Cross-Site Scripting (XSS)

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/63.html  

## Description
An adversary embeds malicious scripts in content that will be served to web browsers. The goal of the attack is for the target software, the client-side browser, to execute the script with the users' privilege level. An attack of this type exploits a programs' vulnerabilities that are brought on by allowing remote hosts to execute code and scripts. Web browsers, for example, have some simple security controls in place, but if a remote attacker is allowed to execute scripts (through injecting them in to user-generated content like bulletin boards) then these controls may be bypassed. Further, these attacks are very difficult for an end user to detect.

## Related Attack Patterns
- ChildOf: CAPEC-242
- CanPrecede: CAPEC-107

## Prerequisites
- Target client software must be a client that allows scripting communication from remote hosts, such as a JavaScript-enabled Web Browser.

## Skills Required
- [Low] To achieve a redirection and use of less trusted source, an attacker can simply place a script in bulletin board, blog, wiki, or other user-generated content site that are echoed back to other client machines.
- [High] Exploiting a client side vulnerability to inject malicious scripts into the browser's executable process.

## Resources Required
- Ability to deploy a custom hostile service for access by targeted clients. Ability to communicate synchronously or asynchronously with client machine.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Design: Use browser technologies that do not allow client side scripting.
- Design: Utilize strict type, character, and encoding enforcement
- Design: Server side developers should not proxy content via XHR or other means, if a http proxy for remote content is setup on the server side, the client's browser has no way of discerning where the data is originating from.
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Perform input validation for all remote content.
- Implementation: Perform output validation for all remote content.
- Implementation: Session tokens for specific host
- Implementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.

## Related Weaknesses (CWE)
- CWE-79
- CWE-20


---

# CAPEC-630: TypoSquatting

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/630.html  

## Description
An adversary registers a domain name with at least one character different than a trusted domain. A TypoSquatting attack takes advantage of instances where a user mistypes a URL (e.g. www.goggle.com) or not does visually verify a URL before clicking on it (e.g. phishing attack). As a result, the user is directed to an adversary-controlled destination. TypoSquatting does not require an attack against the trusted domain or complicated reverse engineering.

## Related Attack Patterns
- ChildOf: CAPEC-616
- CanPrecede: CAPEC-89
- CanPrecede: CAPEC-543

## Prerequisites
- An adversary requires knowledge of popular or high traffic domains, that could be used to deceive potential targets.

## Skills Required
- [Low] Adversaries must be able to register DNS hostnames/URL’s.

## Consequences
- Scope: Other; Impact: Other

## Mitigations
- Authenticate all servers and perform redundant checks when using DNS hostnames.
- Purchase potential TypoSquatted domains and forward to legitimate domain.


---

# CAPEC-631: SoundSquatting

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/631.html  

## Description
An adversary registers a domain name that sounds the same as a trusted domain, but has a different spelling. A SoundSquatting attack takes advantage of a user's confusion of the two words to direct Internet traffic to adversary-controlled destinations. SoundSquatting does not require an attack against the trusted domain or complicated reverse engineering.

## Related Attack Patterns
- ChildOf: CAPEC-616
- CanPrecede: CAPEC-89
- CanPrecede: CAPEC-543

## Prerequisites
- An adversary requires knowledge of popular or high traffic domains, that could be used to deceive potential targets.

## Skills Required
- [Low] Adversaries must be able to register DNS hostnames/URL’s.

## Consequences
- Scope: Other; Impact: Other

## Mitigations
- Authenticate all servers and perform redundant checks when using DNS hostnames.
- Purchase potential SoundSquatted domains and forward to legitimate domain.


---

# CAPEC-632: Homograph Attack via Homoglyphs

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/632.html  

## Description
An adversary registers a domain name containing a homoglyph, leading the registered domain to appear the same as a trusted domain. A homograph attack leverages the fact that different characters among various character sets look the same to the user. Homograph attacks must generally be combined with other attacks, such as phishing attacks, in order to direct Internet traffic to the adversary-controlled destinations.

## Related Attack Patterns
- ChildOf: CAPEC-616
- CanPrecede: CAPEC-89
- CanPrecede: CAPEC-543

## Prerequisites
- An adversary requires knowledge of popular or high traffic domains, that could be used to deceive potential targets.

## Skills Required
- [Low] Adversaries must be able to register DNS hostnames/URL’s.

## Consequences
- Scope: Other; Impact: Other

## Mitigations
- Authenticate all servers and perform redundant checks when using DNS hostnames.
- Utilize browsers that can warn users if URLs contain characters from different character sets.

## Related Weaknesses (CWE)
- CWE-1007


---

# CAPEC-633: Token Impersonation

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/633.html  

## Description
An adversary exploits a weakness in authentication to create an access token (or equivalent) that impersonates a different entity, and then associates a process/thread to that that impersonated token. This action causes a downstream user to make a decision or take action that is based on the assumed identity, and not the response that blocks the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-194

## Prerequisites
- This pattern of attack is only applicable when a downstream user leverages tokens to verify identity, and then takes action based on that identity.

## Consequences
- Scope: Integrity; Impact: Alter Execution Logic
- Scope: Integrity; Impact: Gain Privileges
- Scope: Integrity; Impact: Hide Activities

## Related Weaknesses (CWE)
- CWE-287
- CWE-1270


---

# CAPEC-634: Probe Audio and Video Peripherals

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/634.html  

## Description
The adversary exploits the target system's audio and video functionalities through malware or scheduled tasks. The goal is to capture sensitive information about the target for financial, personal, political, or other gains which is accomplished by collecting communication data between two parties via the use of peripheral devices (e.g. microphones and webcams) or applications with audio and video capabilities (e.g. Skype) on a system.

## Related Attack Patterns
- ChildOf: CAPEC-651
- ChildOf: CAPEC-545

## Prerequisites
- Knowledge of the target device's or application’s vulnerabilities that can be capitalized on with malicious code. The adversary must be able to place the malicious code on the target device.

## Skills Required
- [High] To deploy a hidden process or malware on the system to automatically collect audio and video data.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Prevent unknown code from executing on a system through the use of an allowlist policy.
- Patch installed applications as soon as new updates become available.

## Related Weaknesses (CWE)
- CWE-267


---

# CAPEC-635: Alternative Execution Due to Deceptive Filenames

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/635.html  

## Description
The extension of a file name is often used in various contexts to determine the application that is used to open and use it. If an attacker can cause an alternative application to be used, it may be able to execute malicious code, cause a denial of service or expose sensitive information.

## Related Attack Patterns
- ChildOf: CAPEC-165

## Prerequisites
- The use of the file must be controlled by the file extension.

## Mitigations
- Applications should insure that the content of the file is consistent with format it is expecting, and not depend solely on the file extension.

## Related Weaknesses (CWE)
- CWE-162


---

# CAPEC-636: Hiding Malicious Data or Code within Files

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/636.html  

## Description
Files on various operating systems can have a complex format which allows for the storage of other data, in addition to its contents. Often this is metadata about the file, such as a cached thumbnail for an image file. Unless utilities are invoked in a particular way, this data is not visible during the normal use of the file. It is possible for an attacker to store malicious data or code using these facilities, which would be difficult to discover.

## Related Attack Patterns
- ChildOf: CAPEC-165

## Prerequisites
- The operating system must support a file system that allows for alternate data storage for a file.

## Mitigations
- Many tools are available to search for the hidden data. Scan regularly for such data using one of these tools.

## Related Weaknesses (CWE)
- CWE-506


---

# CAPEC-637: Collect Data from Clipboard

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/637.html  

## Description
The adversary exploits an application that allows for the copying of sensitive data or information by collecting information copied to the clipboard. Data copied to the clipboard can be accessed by other applications, such as malware built to exfiltrate or log clipboard contents on a periodic basis. In this way, the adversary aims to garner information to which they are unauthorized.

## Related Attack Patterns
- ChildOf: CAPEC-150

## Prerequisites
- The adversary must have a means (i.e., a pre-installed tool or background process) by which to collect data from the clipboard and store it. That is, when the target copies data to the clipboard (e.g., to paste into another application), the adversary needs some means of capturing that data in a third location.

## Skills Required
- [High] To deploy a hidden process or malware on the system to automatically collect clipboard data.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- While copying and pasting of data with the clipboard is a legitimate and practical function, certain situations and context may require the disabling of this feature. Just as certain applications disable screenshot capability, applications that handle highly sensitive information should consider disabling copy and paste functionality.
- Employ a robust identification and audit/blocking via using an allowlist of applications on your system. Malware may contain the functionality associated with this attack pattern.

## Related Weaknesses (CWE)
- CWE-267


---

# CAPEC-638: Altered Component Firmware

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/638.html  

## Description
An adversary exploits systems features and/or improperly protected firmware of hardware components, such as Hard Disk Drives (HDD), with the goal of executing malicious code from within the component's Master Boot Record (MBR). Conducting this type of attack entails the adversary infecting the target with firmware altering malware, using known tools, and a payload. Once this malware is executed, the MBR is modified to include instructions to execute the payload at desired intervals and when the system is booted up. A successful attack will obtain persistence within the victim system even if the operating system is reinstalled and/or if the component is formatted or has its data erased.

## Related Attack Patterns
- ChildOf: CAPEC-452

## Prerequisites
- Advanced knowledge about the target component's firmware
- Advanced knowledge about Master Boot Records (MBR)
- Advanced knowledge about tools used to insert firmware altering malware.
- Advanced knowledge about component shipments to the target organization.

## Skills Required
- [High] Ability to access and reverse engineer hardware component firmware.
- [High] Ability to intercept components in transit.
- [Medium] Ability to create malicious payload to be executed from MBR.
- [Low] Ability to leverage known malware tools to infect target system and insert firmware altering malware/payload

## Resources Required
- Manufacturer source code for hardware components.
- Malware tools used to insert malware and payload onto target component.
- Either remote or physical access to the target component.

## Consequences
- Scope: Authentication, Authorization; Impact: Gain Privileges, Execute Unauthorized Commands, Bypass Protection Mechanism, Hide Activities
- Scope: Confidentiality, Access Control; Impact: Read Data, Modify Data

## Mitigations
- Leverage hardware components known to not be susceptible to these types of attacks.
- Implement hardware RAID infrastructure.


---

# CAPEC-639: Probe System Files

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/639.html  

## Description
An adversary obtains unauthorized information due to improperly protected files. If an application stores sensitive information in a file that is not protected by proper access control, then an adversary can access the file and search for sensitive information.

## Related Attack Patterns
- ChildOf: CAPEC-545

## Prerequisites
- An adversary has access to the file system of a system.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Verify that files have proper access controls set, and reduce the storage of sensitive information to only what is necessary.

## Related Weaknesses (CWE)
- CWE-552


---

# CAPEC-64: Using Slashes and URL Encoding Combined to Bypass Validation Logic

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/64.html  

## Description
This attack targets the encoding of the URL combined with the encoding of the slash characters. An attacker can take advantage of the multiple ways of encoding a URL and abuse the interpretation of the URL. A URL may contain special character that need special syntax handling in order to be interpreted. Special characters are represented using a percentage character followed by two digits representing the octet code of the original character (%HEX-CODE). For instance US-ASCII space character would be represented with %20. This is often referred as escaped ending or percent-encoding. Since the server decodes the URL from the requests, it may restrict the access to some URL paths by validating and filtering out the URL requests it received. An attacker will try to craft an URL with a sequence of special characters which once interpreted by the server will be equivalent to a forbidden URL. It can be difficult to protect against this attack since the URL can contain other format of encoding such as UTF-8 encoding, Unicode-encoding, etc.

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- The application accepts and decodes URL string request.
- The application performs insufficient filtering/canonicalization on the URLs.

## Skills Required
- [Low] An attacker can try special characters in the URL and bypass the URL validation.
- [Medium] The attacker may write a script to defeat the input filtering mechanism.

## Consequences
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system. Test your decoding process against malicious input.
- Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding.
- When client input is required from web-based forms, avoid using the "GET" method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the "POST method whenever possible.
- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.
- Refer to the RFCs to safely decode URL.
- Regular expression can be used to match safe URL patterns. However, that may discard valid URL requests if the regular expression is too restrictive.
- There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx).

## Related Weaknesses (CWE)
- CWE-177
- CWE-173
- CWE-172
- CWE-73
- CWE-22
- CWE-74
- CWE-20
- CWE-697
- CWE-707


---

# CAPEC-640: Inclusion of Code in Existing Process

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/640.html  

## Description
The adversary takes advantage of a bug in an application failing to verify the integrity of the running process to execute arbitrary code in the address space of a separate live process. The adversary could use running code in the context of another process to try to access process's memory, system/network resources, etc. The goal of this attack is to evade detection defenses and escalate privileges by masking the malicious code under an existing legitimate process. Examples of approaches include but not limited to: dynamic-link library (DLL) injection, portable executable injection, thread execution hijacking, ptrace system calls, VDSO hijacking, function hooking, reflective code loading, and more.

## Related Attack Patterns
- ChildOf: CAPEC-251

## Prerequisites
- The targeted application fails to verify the integrity of the running process that allows an adversary to execute arbitrary code.

## Skills Required
- [High] Knowledge of how to load malicious code into the memory space of a running process, as well as the ability to have the running process execute this code. For example, with DLL injection, the adversary must know how to load a DLL into the memory space of another running process, and cause this process to execute the code inside of the DLL.

## Consequences
- Scope: Integrity, Confidentiality; Impact: Execute Unauthorized Commands, Read Data

## Mitigations
- Prevent unknown or malicious software from loading through using an allowlist policy.
- Properly restrict the location of the software being used.
- Leverage security kernel modules providing advanced access control and process restrictions like SELinux.
- Monitor API calls like CreateRemoteThread, SuspendThread/SetThreadContext/ResumeThread, QueueUserAPC, and similar for Windows.
- Monitor API calls like ptrace system call, use of LD_PRELOAD environment variable, dlfcn dynamic linking API calls, and similar for Linux.
- Monitor API calls like SetWindowsHookEx and SetWinEventHook which install hook procedures for Windows.
- Monitor processes and command-line arguments for unknown behavior related to code injection.

## Related Weaknesses (CWE)
- CWE-114
- CWE-829


---

# CAPEC-641: DLL Side-Loading

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/641.html  

## Description
An adversary places a malicious version of a Dynamic-Link Library (DLL) in the Windows Side-by-Side (WinSxS) directory to trick the operating system into loading this malicious DLL instead of a legitimate DLL. Programs specify the location of the DLLs to load via the use of WinSxS manifests or DLL redirection and if they aren't used then Windows searches in a predefined set of directories to locate the file. If the applications improperly specify a required DLL or WinSxS manifests aren't explicit about the characteristics of the DLL to be loaded, they can be vulnerable to side-loading.

## Related Attack Patterns
- ChildOf: CAPEC-159

## Prerequisites
- The target must fail to verify the integrity of the DLL before using them.

## Skills Required
- [High] Trick the operating system in loading a malicious DLL instead of a legitimate DLL.

## Consequences
- Scope: Integrity; Impact: Execute Unauthorized Commands, Bypass Protection Mechanism

## Mitigations
- Prevent unknown DLLs from loading through using an allowlist policy.
- Patch installed applications as soon as new updates become available.
- Properly restrict the location of the software being used.
- Use of sxstrace.exe on Windows as well as manual inspection of the manifests.
- Require code signing and avoid using relative paths for resources.

## Related Weaknesses (CWE)
- CWE-706


---

# CAPEC-642: Replace Binaries

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/642.html  

## Description
Adversaries know that certain binaries will be regularly executed as part of normal processing. If these binaries are not protected with the appropriate file system permissions, it could be possible to replace them with malware. This malware might be executed at higher system permission levels. A variation of this pattern is to discover self-extracting installation packages that unpack binaries to directories with weak file permissions which it does not clean up appropriately. These binaries can be replaced by malware, which can then be executed.

## Related Attack Patterns
- ChildOf: CAPEC-17

## Prerequisites
- The attacker must be able to place the malicious binary on the target machine.

## Mitigations
- Insure that binaries commonly used by the system have the correct file permissions. Set operating system policies that restrict privilege elevation of non-Administrators. Use auditing tools to observe changes to system services.

## Related Weaknesses (CWE)
- CWE-732


---

# CAPEC-643: Identify Shared Files/Directories on System

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/643.html  

## Description
An adversary discovers connections between systems by exploiting the target system's standard practice of revealing them in searchable, common areas. Through the identification of shared folders/drives between systems, the adversary may further their goals of locating and collecting sensitive information/files, or map potential routes for lateral movement within the network.

## Related Attack Patterns
- ChildOf: CAPEC-309
- CanPrecede: CAPEC-561
- CanPrecede: CAPEC-545
- CanPrecede: CAPEC-165

## Prerequisites
- The adversary must have obtained logical access to the system by some means (e.g., via obtained credentials or planting malware on the system).

## Skills Required
- [Low] Once the adversary has logical access (which can potentially require high knowledge and skill level), the adversary needs only the capability and facility to navigate the system through the OS graphical user interface or the command line. The adversary, or their malware, can simply employ a set of commands that search for shared drives on the system (e.g., net view \\remote system or net share).

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Identify unnecessary system utilities or potentially malicious software that may contain functionality to identify network share information, and audit and/or block them by using allowlist tools.

## Related Weaknesses (CWE)
- CWE-267
- CWE-200


---

# CAPEC-644: Use of Captured Hashes (Pass The Hash)

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/644.html  

## Description
An adversary obtains (i.e. steals or purchases) legitimate Windows domain credential hash values to access systems within the domain that leverage the Lan Man (LM) and/or NT Lan Man (NTLM) authentication protocols.

## Related Attack Patterns
- ChildOf: CAPEC-653
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-165
- CanPrecede: CAPEC-549
- CanPrecede: CAPEC-545

## Prerequisites
- The system/application is connected to the Windows domain.
- The system/application leverages the Lan Man (LM) and/or NT Lan Man (NTLM) authentication protocols.
- The adversary possesses known Windows credential hash value pairs that exist on the target domain.

## Skills Required
- [Low] Once an adversary obtains a known Windows credential hash value pair, leveraging it is trivial.

## Resources Required
- A list of known Window credential hash value pairs for the targeted domain.

## Consequences
- Scope: Confidentiality, Access Control, Authentication; Impact: Gain Privileges
- Scope: Confidentiality, Authorization; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Prevent the use of Lan Man and NT Lan Man authentication on severs and apply patch KB2871997 to Windows 7 and higher systems.
- Leverage multi-factor authentication for all authentication services and prior to granting an entity access to the domain network.
- Monitor system and domain logs for abnormal credential access.
- Create a strong password policy and ensure that your system enforces this policy.
- Leverage system penetration testing and other defense in depth methods to determine vulnerable systems within a domain.

## Related Weaknesses (CWE)
- CWE-522
- CWE-836
- CWE-308
- CWE-294
- CWE-308


---

# CAPEC-645: Use of Captured Tickets (Pass The Ticket)

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/645.html  

## Description
An adversary uses stolen Kerberos tickets to access systems/resources that leverage the Kerberos authentication protocol. The Kerberos authentication protocol centers around a ticketing system which is used to request/grant access to services and to then access the requested services. An adversary can obtain any one of these tickets (e.g. Service Ticket, Ticket Granting Ticket, Silver Ticket, or Golden Ticket) to authenticate to a system/resource without needing the account's credentials. Depending on the ticket obtained, the adversary may be able to access a particular resource or generate TGTs for any account within an Active Directory Domain.

## Related Attack Patterns
- ChildOf: CAPEC-652
- CanPrecede: CAPEC-151

## Prerequisites
- The adversary needs physical access to the victim system.
- The use of a third-party credential harvesting tool.

## Skills Required
- [Low] Determine if Kerberos authentication is used on the server.
- [High] The adversary uses a third-party tool to obtain the necessary tickets to execute the attack.

## Consequences
- Scope: Integrity; Impact: Gain Privileges

## Mitigations
- Reset the built-in KRBTGT account password twice to invalidate the existence of any current Golden Tickets and any tickets derived from them.
- Monitor system and domain logs for abnormal access.

## Related Weaknesses (CWE)
- CWE-522
- CWE-294
- CWE-308


---

# CAPEC-646: Peripheral Footprinting

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/646.html  

## Description
Adversaries may attempt to obtain information about attached peripheral devices and components connected to a computer system. Examples may include discovering the presence of iOS devices by searching for backups, analyzing the Windows registry to determine what USB devices have been connected, or infecting a victim system with malware to report when a USB device has been connected. This may allow the adversary to gain additional insight about the system or network environment, which may be useful in constructing further attacks.

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary needs either physical or remote access to the victim system.

## Skills Required
- [Medium] The adversary needs to be able to infect the victim system in a manner that gives them remote access.
- [Medium] If analyzing the Windows registry, the adversary must understand the registry structure to know where to look for devices.

## Mitigations
- Identify programs that may be used to acquire peripheral information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-647: Collect Data from Registries

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/647.html  

## Description
An adversary exploits a weakness in authorization to gather system-specific data and sensitive information within a registry (e.g., Windows Registry, Mac plist). These contain information about the system configuration, software, operating system, and security. The adversary can leverage information gathered in order to carry out further attacks.

## Related Attack Patterns
- ChildOf: CAPEC-150

## Prerequisites
- The adversary must have obtained logical access to the system by some means (e.g., via obtained credentials or planting malware on the system).
- The adversary must have capability to navigate the operating system to peruse the registry.

## Skills Required
- [Low] Once the adversary has logical access (which can potentially require high knowledge and skill level), the adversary needs only the capability and facility to navigate the system through the OS graphical user interface or the command line.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Employ a robust and layered defensive posture in order to prevent unauthorized users on your system.
- Employ robust identification and audit/blocking via using an allowlist of applications on your system. Unnecessary applications, utilities, and configurations will have a presence in the system registry that can be leveraged by an adversary through this attack pattern.

## Related Weaknesses (CWE)
- CWE-285


---

# CAPEC-648: Collect Data from Screen Capture

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/648.html  

## Description
An adversary gathers sensitive information by exploiting the system's screen capture functionality. Through screenshots, the adversary aims to see what happens on the screen over the course of an operation. The adversary can leverage information gathered in order to carry out further attacks.

## Related Attack Patterns
- ChildOf: CAPEC-150

## Prerequisites
- The adversary must have obtained logical access to the system by some means (e.g., via obtained credentials or planting malware on the system).

## Skills Required
- [Low] Once the adversary has logical access (which can potentially require high knowledge and skill level), the adversary needs only to leverage the relevant command for screen capture.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Identify potentially malicious software that may have functionality to acquire screen captures, and audit and/or block it by using allowlist tools.
- While screen capture is a legitimate and practical function, certain situations and context may require the disabling of this feature.

## Related Weaknesses (CWE)
- CWE-267


---

# CAPEC-649: Adding a Space to a File Extension

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/649.html  

## Description
An adversary adds a space character to the end of a file extension and takes advantage of an application that does not properly neutralize trailing special elements in file names. This extra space, which can be difficult for a user to notice, affects which default application is used to operate on the file and can be leveraged by the adversary to control execution.

## Related Attack Patterns
- ChildOf: CAPEC-635

## Prerequisites
- The use of the file must be controlled by the file extension.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- File extensions should be checked to see if non-visible characters are being included.

## Related Weaknesses (CWE)
- CWE-46


---

# CAPEC-65: Sniff Application Code

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/65.html  

## Description
An adversary passively sniffs network communications and captures application code bound for an authorized client. Once obtained, they can use it as-is, or through reverse-engineering glean sensitive information or exploit the trust relationship between the client and server. Such code may belong to a dynamic update to the client, a patch being applied to a client component or any such interaction where the client is authorized to communicate with the server.

## Related Attack Patterns
- ChildOf: CAPEC-157
- CanPrecede: CAPEC-37

## Prerequisites
- The attacker must have the ability to place themself in the communication path between the client and server.
- The targeted application must receive some application code from the server; for example, dynamic updates, patches, applets or scripts.
- The attacker must be able to employ a sniffer on the network without being detected.

## Skills Required
- [Medium] The attacker needs to setup a sniffer for a sufficient period of time so as to capture meaningful quantities of code. The presence of the sniffer should not be detected on the network. Also if the attacker plans to employ an adversary-in-the-middle attack (CAPEC-94), the client or server must not realize this. Finally, the attacker needs to regenerate source code from binary code if the need be.

## Resources Required
- The Attacker needs the ability to capture communications between the client being updated and the server providing the update. In the case that encryption obscures client/server communication the attacker will either need to lift key material from the client.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Design: Encrypt all communication between the client and server.
- Implementation: Use SSL, SSH, SCP.
- Operation: Use "ifconfig/ipconfig" or other tools to detect the sniffer installed in the network.

## Related Weaknesses (CWE)
- CWE-319
- CWE-311
- CWE-318
- CWE-693


---

# CAPEC-650: Upload a Web Shell to a Web Server

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/650.html  

## Description
By exploiting insufficient permissions, it is possible to upload a web shell to a web server in such a way that it can be executed remotely. This shell can have various capabilities, thereby acting as a "gateway" to the underlying web server. The shell might execute at the higher permission level of the web server, providing the ability the execute malicious code at elevated levels.

## Related Attack Patterns
- ChildOf: CAPEC-17

## Prerequisites
- The web server is susceptible to one of the various web application exploits that allows for uploading a shell file.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Make sure your web server is up-to-date with all patches to protect against known vulnerabilities.
- Ensure that the file permissions in directories on the web server from which files can be execute is set to the "least privilege" settings, and that those directories contents is controlled by an allowlist.

## Related Weaknesses (CWE)
- CWE-287
- CWE-553


---

# CAPEC-651: Eavesdropping

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/651.html  

## Description
An adversary intercepts a form of communication (e.g. text, audio, video) by way of software (e.g., microphone and audio recording application), hardware (e.g., recording equipment), or physical means (e.g., physical proximity). The goal of eavesdropping is typically to gain unauthorized access to sensitive information about the target for financial, personal, political, or other gains. Eavesdropping is different from a sniffing attack as it does not take place on a network-based communication channel (e.g., IP traffic). Instead, it entails listening in on the raw audio source of a conversation between two or more parties.

## Related Attack Patterns
- ChildOf: CAPEC-117

## Prerequisites
- The adversary typically requires physical proximity to the target's environment, whether for physical eavesdropping or for placing recording equipment. This is not always the case for software-based eavesdropping, if the adversary has the capability to install malware on the target system that can activate a microphone and record audio digitally.

## Resources Required
- For logical eavesdropping, some equipment may be necessary (e.g., microphone, tape recorder, etc.). For physical eavesdropping, only proximity is required.

## Consequences
- Scope: Confidentiality; Impact: Other

## Mitigations
- Be mindful of your surroundings when discussing sensitive information in public areas.
- Implement proper software restriction policies to only allow authorized software on your environment. Use of anti-virus and other security monitoring and detecting tools can aid in this too. Closely monitor installed software for unusual behavior or activity, and implement patches as soon as they become available.
- If possible, physically disable the microphone on your machine if it is not needed.

## Related Weaknesses (CWE)
- CWE-200


---

# CAPEC-652: Use of Known Kerberos Credentials

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/652.html  

## Description
An adversary obtains (i.e. steals or purchases) legitimate Kerberos credentials (e.g. Kerberos service account userID/password or Kerberos Tickets) with the goal of achieving authenticated access to additional systems, applications, or services within the domain.

## Related Attack Patterns
- ChildOf: CAPEC-560
- CanPrecede: CAPEC-151

## Prerequisites
- The system/application leverages Kerberos authentication.
- The system/application uses one factor password-based authentication, SSO, and/or cloud-based authentication for Kerberos service accounts.
- The system/application does not have a sound password policy that is being enforced for Kerberos service accounts.
- The system/application does not implement an effective password throttling mechanism for authenticating to Kerberos service accounts.
- The targeted network allows for network sniffing attacks to succeed.

## Skills Required
- [Low] Once an adversary obtains a known Kerberos credential, leveraging it is trivial.

## Resources Required
- A valid Kerberos ticket or a known Kerberos service account credential.

## Consequences
- Scope: Confidentiality, Access Control, Authentication; Impact: Gain Privileges
- Scope: Confidentiality, Authorization; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Create a strong password policy and ensure that your system enforces this policy for Kerberos service accounts.
- Ensure Kerberos service accounts are not reusing username/password combinations for multiple systems, applications, or services.
- Do not reuse Kerberos service account credentials across systems.
- Deny remote use of Kerberos service account credentials to log into domain systems.
- Do not allow Kerberos service accounts to be a local administrator on more than one system.
- Enable at least AES Kerberos encryption for tickets.
- Monitor system and domain logs for abnormal credential access.

## Related Weaknesses (CWE)
- CWE-522
- CWE-307
- CWE-308
- CWE-309
- CWE-262
- CWE-263
- CWE-654
- CWE-294
- CWE-836


---

# CAPEC-653: Use of Known Operating System Credentials

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/653.html  

## Description
An adversary guesses or obtains (i.e. steals or purchases) legitimate operating system credentials (e.g. userID/password) to achieve authentication and to perform authorized actions on the system, under the guise of an authenticated user or service. This applies to any Operating System.

## Related Attack Patterns
- ChildOf: CAPEC-560
- CanPrecede: CAPEC-151

## Prerequisites
- The system/application uses one factor password-based authentication, SSO, and/or cloud-based authentication.
- The system/application does not have a sound password policy that is being enforced.
- The system/application does not implement an effective password throttling mechanism.
- The adversary possesses a list of known user accounts and corresponding passwords that may exist on the target.

## Skills Required
- [Low] Once an adversary obtains a known credential, leveraging it is trivial.

## Resources Required
- A list of known credentials for the targeted domain.
- A custom script that leverages a credential list to launch an attack.

## Consequences
- Scope: Confidentiality, Access Control, Authentication; Impact: Gain Privileges
- Scope: Confidentiality, Authorization; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Leverage multi-factor authentication for all authentication services and prior to granting an entity access to the network.
- Create a strong password policy and ensure that your system enforces this policy.
- Ensure users are not reusing username/password combinations for multiple systems, applications, or services.
- Do not reuse local administrator account credentials across systems.
- Deny remote use of local admin credentials to log into domain systems.
- Do not allow accounts to be a local administrator on more than one system.
- Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-2.
- Monitor system and domain logs for abnormal credential access.

## Related Weaknesses (CWE)
- CWE-522
- CWE-307
- CWE-308
- CWE-309
- CWE-262
- CWE-263
- CWE-654


---

# CAPEC-654: Credential Prompt Impersonation

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/654.html  

## Description
An adversary, through a previously installed malicious application, impersonates a credential prompt in an attempt to steal a user's credentials.

## Related Attack Patterns
- ChildOf: CAPEC-504

## Prerequisites
- The adversary must already have access to the target system via some means.
- A legitimate task must exist that an adversary can impersonate to glean credentials.

## Skills Required
- [Low] Once an adversary has gained access to the target system, impersonating a credential prompt is not difficult.

## Resources Required
- Malware or some other means to initially comprise the target system.
- Additional malware to impersonate a legitimate credential prompt.

## Consequences
- Scope: Access Control, Authentication; Impact: Gain Privileges

## Mitigations
- The only known mitigation to this attack is to avoid installing the malicious application on the device. However, to impersonate a running task the malicious application does need the GET_TASKS permission to be able to query the task list, and being suspicious of applications with that permission can help.

## Related Weaknesses (CWE)
- CWE-1021


---

# CAPEC-655: Avoid Security Tool Identification by Adding Data

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/655.html  

## Description
An adversary adds data to a file to increase the file size beyond what security tools are capable of handling in an attempt to mask their actions. In addition to this, adding data to a file also changes the file's hash, frustrating security tools that look for known bad files by their hash.

## Related Attack Patterns
- ChildOf: CAPEC-572

## Consequences
- Scope: Accountability; Impact: Hide Activities, Bypass Protection Mechanism
- Scope: Integrity; Impact: Modify Data


---

# CAPEC-656: Voice Phishing

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/656.html  

## Description
An adversary targets users with a phishing attack for the purpose of soliciting account passwords or sensitive information from the user. Voice Phishing is a variation of the Phishing social engineering technique where the attack is initiated via a voice call, rather than email. The user is enticed to provide sensitive information by the adversary, who masquerades as a legitimate employee of the alleged organization. Voice Phishing attacks deviate from standard Phishing attacks, in that a user doesn't typically interact with a compromised website to provide sensitive information and instead provides this information verbally. Voice Phishing attacks can also be initiated by either the adversary in the form of a "cold call" or by the victim if calling an illegitimate telephone number.

## Related Attack Patterns
- ChildOf: CAPEC-98

## Prerequisites
- An adversary needs phone numbers to initiate contact with the victim, in addition to a legitimate-looking telephone number to call the victim from.
- An adversary needs to correctly guess the entity with which the victim does business and impersonate it. Most of the time phishers just use the most popular banks/services and send out their "hooks" to many potential victims.
- An adversary needs to have a sufficiently compelling call to action to prompt the user to take action.
- If passively conducting this attack via a spoofed website, replicated website needs to look extremely similar to the original website and the URL used to get to that website needs to look like the real URL of the said business entity.

## Skills Required
- [Medium] Basic knowledge about websites: obtaining them, designing and implementing them, etc.

## Resources Required
- Legitimate-looking telephone number(s) to initiate calls with victims

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Do not accept calls from unknown numbers or from numbers that may be flagged as spam. Also, do not call numbers that appear on-screen after being unexpectedly redirected to potentially malicious websites. In either case, do not provide sensitive information over voice calls that are not legitimately initiated. Instead, call your Bank, PayPal, eBay, etc., via the number on their public-facing website and inquire about the problem.


---

# CAPEC-657: Malicious Automated Software Update via Spoofing

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/657.html  

## Description
An attackers uses identify or content spoofing to trick a client into performing an automated software update from a malicious source. A malicious automated software update that leverages spoofing can include content or identity spoofing as well as protocol spoofing. Content or identity spoofing attacks can trigger updates in software by embedding scripted mechanisms within a malicious web page, which masquerades as a legitimate update source. Scripting mechanisms communicate with software components and trigger updates from locations specified by the attackers' server. The result is the client believing there is a legitimate software update available but instead downloading a malicious update from the attacker.

## Related Attack Patterns
- ChildOf: CAPEC-186

## Consequences
- Scope: Access Control, Availability, Confidentiality; Impact: Execute Unauthorized Commands

## Related Weaknesses (CWE)
- CWE-494


---

# CAPEC-66: SQL Injection

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/66.html  

## Description
This attack exploits target software that constructs SQL statements based on user input. An attacker crafts input strings so that when the target software constructs SQL statements based on the input, the resulting SQL statement performs actions other than those the application intended. SQL Injection results from failure of the application to appropriately validate input.

## Related Attack Patterns
- ChildOf: CAPEC-248

## Prerequisites
- SQL queries used by the application to store, retrieve or modify data.
- User-controllable input that is not properly validated by the application as part of SQL queries.

## Skills Required
- [Low] It is fairly simple for someone with basic SQL knowledge to perform SQL injection, in general. In certain instances, however, specific knowledge of the database employed may be required.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as SQL content. Keywords such as UNION, SELECT or INSERT must be filtered in addition to characters such as a single-quote(') or SQL-comments (--) based on the context in which they appear.
- Use of parameterized queries or stored procedures - Parameterization causes the input to be restricted to certain domains, such as strings or integers, and any input outside such domains is considered invalid and the query fails. Note that SQL Injection is possible even in the presence of stored procedures if the eventual query is constructed dynamically.
- Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the database or application.

## Related Weaknesses (CWE)
- CWE-89
- CWE-1286


---

# CAPEC-660: Root/Jailbreak Detection Evasion via Hooking

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/660.html  

## Description
An adversary forces a non-restricted mobile application to load arbitrary code or code files, via Hooking, with the goal of evading Root/Jailbreak detection. Mobile device users often Root/Jailbreak their devices in order to gain administrative control over the mobile operating system and/or to install third-party mobile applications that are not provided by authorized application stores (e.g. Google Play Store and Apple App Store). Adversaries may further leverage these capabilities to escalate privileges or bypass access control on legitimate applications. Although many mobile applications check if a mobile device is Rooted/Jailbroken prior to authorized use of the application, adversaries may be able to "hook" code in order to circumvent these checks. Successfully evading Root/Jailbreak detection allows an adversary to execute administrative commands, obtain confidential data, impersonate legitimate users of the application, and more.

## Related Attack Patterns
- ChildOf: CAPEC-251

## Prerequisites
- The targeted application must be non-restricted to allow code hooking.

## Skills Required
- [High] Knowledge about Root/Jailbreak detection and evasion techniques.
- [Medium] Knowledge about code hooking.

## Resources Required
- The adversary must have a Rooted/Jailbroken mobile device.
- The adversary needs to have enough access to the target application to control the included code or file.

## Consequences
- Scope: Integrity, Authorization; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Access Control; Impact: Read Data

## Mitigations
- Ensure mobile applications are signed appropriately to avoid code inclusion via hooking.
- Inspect the application's memory for suspicious artifacts, such as shared objects/JARs or dylibs, after other Root/Jailbreak detection methods.
- Inspect the application's stack trace for suspicious method calls.
- Allow legitimate native methods, and check for non-allowed native methods during Root/Jailbreak detection methods.
- For iOS applications, ensure application methods do not originate from outside of Apple's SDK.

## Related Weaknesses (CWE)
- CWE-829


---

# CAPEC-661: Root/Jailbreak Detection Evasion via Debugging

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/661.html  

## Description
An adversary inserts a debugger into the program entry point of a mobile application to modify the application binary, with the goal of evading Root/Jailbreak detection. Mobile device users often Root/Jailbreak their devices in order to gain administrative control over the mobile operating system and/or to install third-party mobile applications that are not provided by authorized application stores (e.g. Google Play Store and Apple App Store). Rooting/Jailbreaking a mobile device also provides users with access to system debuggers and disassemblers, which can be leveraged to exploit applications by dumping the application's memory at runtime in order to remove or bypass signature verification methods. This further allows the adversary to evade Root/Jailbreak detection mechanisms, which can result in execution of administrative commands, obtaining confidential data, impersonating legitimate users of the application, and more.

## Related Attack Patterns
- ChildOf: CAPEC-121
- CanPrecede: CAPEC-68
- CanPrecede: CAPEC-660

## Prerequisites
- A debugger must be able to be inserted into the targeted application.

## Skills Required
- [High] Knowledge about Root/Jailbreak detection and evasion techniques.
- [Medium] Knowledge about runtime debugging.

## Resources Required
- The adversary must have a Rooted/Jailbroken mobile device with debugging capabilities.

## Consequences
- Scope: Integrity, Authorization; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Access Control; Impact: Read Data

## Mitigations
- Instantiate checks within the application code that ensures debuggers are not attached.

## Related Weaknesses (CWE)
- CWE-489


---

# CAPEC-662: Adversary in the Browser (AiTB)

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/662.html  

## Description
An adversary exploits security vulnerabilities or inherent functionalities of a web browser, in order to manipulate traffic between two endpoints.

## Related Attack Patterns
- ChildOf: CAPEC-94

## Prerequisites
- The adversary must install or convince a user to install a Trojan.
- There are two components communicating with each other.
- An attacker is able to identify the nature and mechanism of communication between the two target components.
- Strong mutual authentication is not used between the two target components yielding opportunity for adversarial interposition.
- For browser pivoting, the SeDebugPrivilege and a high-integrity process must both exist to execute this attack.

## Skills Required
- [Medium] Tricking the victim into installing the Trojan is often the most difficult aspect of this attack. Afterwards, the remainder of this attack is fairly trivial.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Ensure software and applications are only downloaded from legitimate and reputable sources, in addition to conducting integrity checks on the downloaded component.
- Leverage anti-malware tools, which can detect Trojan Horse malware.
- Use strong, out-of-band mutual authentication to always fully authenticate both ends of any communications channel.
- Limit user permissions to prevent browser pivoting.
- Ensure browser sessions are regularly terminated and when their effective lifetime ends.

## Related Weaknesses (CWE)
- CWE-300
- CWE-494


---

# CAPEC-663: Exploitation of Transient Instruction Execution

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/663.html  

## Description
An adversary exploits a hardware design flaw in a CPU implementation of transient instruction execution to expose sensitive data and bypass/subvert access control over restricted resources. Typically, the adversary conducts a covert channel attack to target non-discarded microarchitectural changes caused by transient executions such as speculative execution, branch prediction, instruction pipelining, and/or out-of-order execution. The transient execution results in a series of instructions (gadgets) which construct covert channel and access/transfer the secret data.

## Related Attack Patterns
- ChildOf: CAPEC-74
- ChildOf: CAPEC-184
- CanPrecede: CAPEC-141
- PeerOf: CAPEC-212
- PeerOf: CAPEC-124
- PeerOf: CAPEC-180

## Prerequisites
- The adversary needs at least user execution access to a system and a maliciously crafted program/application/process with unprivileged code to misuse transient instruction set execution of the CPU.

## Skills Required
- [High] Detailed knowledge on how various CPU architectures and microcode perform transient execution for various low-level assembly language code instructions/operations.
- [High] Detailed knowledge on compiled binaries and operating system shared libraries of instruction sequences, and layout of application and OS/Kernel address spaces for data leakage.

## Resources Required
- C2C mechanism or direct access to victim system, capable of dropping malicious program and collecting covert channel attack data.
- Malicious program capable of triggering execution of transient instructions or vulnerable instruction sequences of victim program and performing a covert channel attack to gather data from victim process memory space. Ultimately, the speed with which an attacker discovers a secret is directly proportional to the computational resources of the victim machine.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Access Control; Impact: Bypass Protection Mechanism
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Implementation: DAWG (Dynamically Allocated Way Guard) - processor cache properly divided between different programs/processes that don't share resources
- Implementation: KPTI (Kernel Page-Table Isolation) to completely separate user-space and kernel space page tables
- Configuration: Architectural Design of Microcode to limit abuse of speculative execution and out-of-order execution
- Configuration: Disable SharedArrayBuffer for Web Browsers
- Configuration: Disable Copy-on-Write between Cloud VMs
- Configuration: Privilege Checks on Cache Flush Instructions
- Implementation: Non-inclusive Cache Memories to prevent Flush+Reload Attacks

## Related Weaknesses (CWE)
- CWE-1037
- CWE-1303
- CWE-1264


---

# CAPEC-664: Server Side Request Forgery

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/664.html  

## Description
An adversary exploits improper input validation by submitting maliciously crafted input to a target application running on a server, with the goal of forcing the server to make a request either to itself, to web services running in the server’s internal network, or to external third parties. If successful, the adversary’s request will be made with the server’s privilege level, bypassing its authentication controls. This ultimately allows the adversary to access sensitive data, execute commands on the server’s network, and make external requests with the stolen identity of the server. Server Side Request Forgery attacks differ from Cross Site Request Forgery attacks in that they target the server itself, whereas CSRF attacks exploit an insecure user authentication mechanism to perform unauthorized actions on the user's behalf.

## Related Attack Patterns
- ChildOf: CAPEC-115

## Prerequisites
- Server must be running a web application that processes HTTP requests.

## Skills Required
- [Medium] The adversary will have to detect the vulnerability through an intermediary service or specify maliciously crafted URLs and analyze the server response.
- [High] The adversary will be required to access internal resources, extract information, or leverage the services running on the server to perform unauthorized actions such as traversing the local network or routing a reflected TCP DDoS through them.

## Resources Required
- [None] No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity, Confidentiality, Availability; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Handling incoming requests securely is the first line of action to mitigate this vulnerability. This can be done through URL validation.
- Further down the process flow, examining the response and verifying that it is as expected before sending would be another way to secure the server.
- Allowlist the DNS name or IP address of every service the web application is required to access is another effective security measure. This ensures the server cannot make external requests to arbitrary services.
- Requiring authentication for local services adds another layer of security between the adversary and internal services running on the server. By enforcing local authentication, an adversary will not gain access to all internal services only with access to the server.
- Enforce the usage of relevant URL schemas. By limiting requests be made only through HTTP or HTTPS, for example, attacks made through insecure schemas such as file://, ftp://, etc. can be prevented.

## Related Weaknesses (CWE)
- CWE-918
- CWE-20


---

# CAPEC-665: Exploitation of Thunderbolt Protection Flaws

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/665.html  

## Description
An adversary leverages a firmware weakness within the Thunderbolt protocol, on a computing device to manipulate Thunderbolt controller firmware in order to exploit vulnerabilities in the implementation of authorization and verification schemes within Thunderbolt protection mechanisms. Upon gaining physical access to a target device, the adversary conducts high-level firmware manipulation of the victim Thunderbolt controller SPI (Serial Peripheral Interface) flash, through the use of a SPI Programing device and an external Thunderbolt device, typically as the target device is booting up. If successful, this allows the adversary to modify memory, subvert authentication mechanisms, spoof identities and content, and extract data and memory from the target device. Currently 7 major vulnerabilities exist within Thunderbolt protocol with 9 attack vectors as noted in the Execution Flow.

## Related Attack Patterns
- ChildOf: CAPEC-276
- CanFollow: CAPEC-390
- PeerOf: CAPEC-458
- PeerOf: CAPEC-148
- PeerOf: CAPEC-151

## Prerequisites
- The adversary needs at least a few minutes of physical access to a system with an open Thunderbolt port, version 3 or lower, and an external thunderbolt device controlled by the adversary with maliciously crafted software and firmware, via an SPI Programming device, to exploit weaknesses in security protections.

## Skills Required
- [High] Detailed knowledge on various system motherboards, PCI Express Domain, SPI, and Thunderbolt Protocol in order to interface with internal system components via external devices.
- [High] Detailed knowledge on OS/Kernel memory address space, Direct Memory Access (DMA) mapping, Input-Output Memory Management Units (IOMMUs), and vendor memory protections for data leakage.
- [High] Detailed knowledge on scripting and SPI programming in order to configure and modify Thunderbolt controller firmware and software configurations.

## Resources Required
- SPI Programming device capable of modifying/configuring or replacing the firmware of Thunderbolt device stored on SPI Flash of target Thunderbolt controller, as well as modification/spoofing of adversary-controlled Thunderbolt controller.
- Precrafted scripts/tools capable of implementing the modification and replacement of Thunderbolt Firmware.
- Thunderbolt-enabled computing device capable of interfacing with target Thunderbolt device and extracting/dumping data and memory contents of target device.

## Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Implementation: Kernel Direct Memory Access Protection
- Configuration: Enable UEFI option USB Passthrough mode - Thunderbolt 3 system port operates as USB 3.1 Type C interface
- Configuration: Enable UEFI option DisplayPort mode - Thunderbolt 3 system port operates as video-only DP interface
- Configuration: Enable UEFI option Mixed USB/DisplayPort mode - Thunderbolt 3 system port operates as USB 3.1 Type C interface with support for DP mode
- Configuration: Set Security Level to SL3 for Thunderbolt 2 system port
- Configuration: Disable PCIe tunneling to set Security Level to SL3
- Configuration: Disable Boot Camp upon MacOS systems

## Related Weaknesses (CWE)
- CWE-345
- CWE-353
- CWE-288
- CWE-1188
- CWE-862


---

# CAPEC-666: BlueSmacking

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/666.html  

## Description
An adversary uses Bluetooth flooding to transfer large packets to Bluetooth enabled devices over the L2CAP protocol with the goal of creating a DoS. This attack must be carried out within close proximity to a Bluetooth enabled device.

## Related Attack Patterns
- ChildOf: CAPEC-125

## Prerequisites
- The system/application has Bluetooth enabled.

## Skills Required
- [Low] An adversary only needs a Linux machine along with a Bluetooth adapter, which is extremely common.

## Consequences
- Scope: Availability; Impact: Unreliable Execution, Resource Consumption

## Mitigations
- Disable Bluetooth when not being used.
- When using Bluetooth, set it to hidden or non-discoverable mode.

## Related Weaknesses (CWE)
- CWE-404


---

# CAPEC-667: Bluetooth Impersonation AttackS (BIAS)

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/667.html  

## Description
An adversary disguises the MAC address of their Bluetooth enabled device to one for which there exists an active and trusted connection and authenticates successfully. The adversary can then perform malicious actions on the target Bluetooth device depending on the target’s capabilities.

## Related Attack Patterns
- ChildOf: CAPEC-616

## Prerequisites
- Knowledge of a target device's list of trusted connections.

## Skills Required
- [Low] Adversaries must be capable of using command line Linux tools.
- [Low] Adversaries must be in close proximity to Bluetooth devices.

## Consequences
- Scope: Integrity; Impact: (unspecified)
- Scope: Confidentiality; Impact: (unspecified)

## Mitigations
- Disable Bluetooth in public places.
- Verify incoming Bluetooth connections; do not automatically trust.
- Change default PIN passwords and always use one when connecting.

## Related Weaknesses (CWE)
- CWE-290


---

# CAPEC-668: Key Negotiation of Bluetooth Attack (KNOB)

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/668.html  

## Description
An adversary can exploit a flaw in Bluetooth key negotiation allowing them to decrypt information sent between two devices communicating via Bluetooth. The adversary uses an Adversary in the Middle setup to modify packets sent between the two devices during the authentication process, specifically the entropy bits. Knowledge of the number of entropy bits will allow the attacker to easily decrypt information passing over the line of communication.

## Related Attack Patterns
- ChildOf: CAPEC-115
- CanPrecede: CAPEC-148

## Prerequisites
- Person in the Middle network setup.

## Skills Required
- [Medium] Ability to modify packets.

## Resources Required
- Bluetooth adapter, packet capturing capabilities.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Newer Bluetooth firmwares ensure that the KNOB is not negotaited in plaintext. Update your device.

## Related Weaknesses (CWE)
- CWE-425
- CWE-285
- CWE-693


---

# CAPEC-669: Alteration of a Software Update

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/669.html  

## Description
An adversary with access to an organization’s software update infrastructure inserts malware into the content of an outgoing update to fielded systems where a wide range of malicious effects are possible. With the same level of access, the adversary can alter a software update to perform specific malicious acts including granting the adversary control over the software’s normal functionality.

## Related Attack Patterns
- ChildOf: CAPEC-184
- CanPrecede: CAPEC-673

## Prerequisites
- An adversary would need to have penetrated an organization’s software update infrastructure including gaining access to components supporting the configuration management of software versions and updates related to the software maintenance of customer systems.

## Skills Required
- [High] Skills required include the ability to infiltrate the organization’s software update infrastructure either from the Internet or from within the organization, including subcontractors, and be able to change software being delivered to customer/user systems in an undetected manner.

## Consequences
- Scope: Access Control; Impact: Gain Privileges
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Have a Software Assurance Plan that includes maintaining strict configuration management control of source code, object code and software development, build and distribution tools; manual code reviews and static code analysis for developmental software; and tracking of all storage and movement of code.
- Require elevated privileges for distribution of software and software updates.


---

# CAPEC-67: String Format Overflow in syslog()

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/67.html  

## Description
This attack targets applications and software that uses the syslog() function insecurely. If an application does not explicitely use a format string parameter in a call to syslog(), user input can be placed in the format string parameter leading to a format string injection attack. Adversaries can then inject malicious format string commands into the function call leading to a buffer overflow. There are many reported software vulnerabilities with the root cause being a misuse of the syslog() function.

## Related Attack Patterns
- ChildOf: CAPEC-100
- ChildOf: CAPEC-135

## Prerequisites
- The Syslog function is used without specifying a format string argument, allowing user input to be placed direct into the function call as a format string.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data

## Mitigations
- The code should be reviewed for misuse of the Syslog function call. Manual or automated code review can be used. The reviewer needs to ensure that all format string functions are passed a static string which cannot be controlled by the user and that the proper number of arguments are always sent to that function as well. If at all possible, do not use the %n operator in format strings. The following code shows a correct usage of Syslog(): syslog(LOG_ERR, "%s", cmdBuf); The following code shows a vulnerable usage of Syslog(): syslog(LOG_ERR, cmdBuf); // the buffer cmdBuff is taking user supplied data.

## Related Weaknesses (CWE)
- CWE-120
- CWE-134
- CWE-74
- CWE-20
- CWE-680
- CWE-697


---

# CAPEC-670: Software Development Tools Maliciously Altered

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/670.html  

## Description
An adversary with the ability to alter tools used in a development environment causes software to be developed with maliciously modified tools. Such tools include requirements management and database tools, software design tools, configuration management tools, compilers, system build tools, and software performance testing and load testing tools. The adversary then carries out malicious acts once the software is deployed including malware infection of other systems to support further compromises.

## Related Attack Patterns
- ChildOf: CAPEC-444
- CanPrecede: CAPEC-669

## Prerequisites
- An adversary would need to have access to a targeted developer’s development environment and in particular to tools used to design, create, test and manage software, where the adversary could ensure malicious code is included in software packages built through alteration or substitution of tools in the environment used in the development of software.

## Skills Required
- [High] Ability to leverage common delivery mechanisms (e.g., email attachments, removable media) to infiltrate a development environment to gain access to software development tools for the purpose of malware insertion into an existing tool or replacement of an existing tool with a maliciously altered copy.

## Consequences
- Scope: Integrity; Impact: Execute Unauthorized Commands
- Scope: Access Control; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Modify Data, Read Data

## Mitigations
- Have a security concept of operations (CONOPS) for the development environment that includes: Maintaining strict security administration and configuration management of requirements management and database tools, software design tools, configuration management tools, compilers, system build tools, and software performance testing and load testing tools.
- Avoid giving elevated privileges to developers.


---

# CAPEC-671: Requirements for ASIC Functionality Maliciously Altered

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/671.html  

## Description
An adversary with access to functional requirements for an application specific integrated circuit (ASIC), a chip designed/customized for a singular particular use, maliciously alters requirements derived from originating capability needs. In the chip manufacturing process, requirements drive the chip design which, when the chip is fully manufactured, could result in an ASIC which may not meet the user’s needs, contain malicious functionality, or exhibit other anomalous behaviors thereby affecting the intended use of the ASIC.

## Related Attack Patterns
- ChildOf: CAPEC-447

## Prerequisites
- An adversary would need to have access to a foundry’s or chip maker’s requirements management system that stores customer requirements for ASICs, requirements upon which the design of the ASIC is based.

## Skills Required
- [High] An adversary would need experience in designing chips based on functional requirements in order to manipulate requirements in such a way that deviations would not be detected in subsequent stages of ASIC manufacture and where intended malicious functionality would be available to the adversary once integrated into a system and fielded.

## Consequences
- Scope: Integrity; Impact: Alter Execution Logic

## Mitigations
- Utilize DMEA’s (Defense Microelectronics Activity) Trusted Foundry Program members for acquisition of microelectronic components.
- Ensure that each supplier performing hardware development implements comprehensive, security-focused configuration management including for hardware requirements and design.
- Require that provenance of COTS microelectronic components be known whenever procured.
- Conduct detailed vendor assessment before acquiring COTS hardware.


---

# CAPEC-672: Malicious Code Implanted During Chip Programming

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/672.html  

## Description
During the programming step of chip manufacture, an adversary with access and necessary technical skills maliciously alters a chip’s intended program logic to produce an effect intended by the adversary when the fully manufactured chip is deployed and in operational use. Intended effects can include the ability of the adversary to remotely control a host system to carry out malicious acts.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- An adversary would need to have access to a foundry’s or chip maker’s development/production environment where programs for specific chips are developed, managed and uploaded into targeted chips prior to distribution or sale.

## Skills Required
- [Medium] An adversary needs to be skilled in microprogramming, manipulation of configuration management systems, and in the operation of tools used for the uploading of programs into chips during manufacture. Uploading can be for individual chips or performed on a large scale basis.

## Consequences
- Scope: Integrity; Impact: Alter Execution Logic

## Mitigations
- Utilize DMEA’s (Defense Microelectronics Activity) Trusted Foundry Program members for acquisition of microelectronic components.
- Ensure that each supplier performing hardware development implements comprehensive, security-focused configuration management of microcode and microcode generating tools and software.
- Require that provenance of COTS microelectronic components be known whenever procured.
- Conduct detailed vendor assessment before acquiring COTS hardware.


---

# CAPEC-673: Developer Signing Maliciously Altered Software

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/673.html  

## Description
Software produced by a reputable developer is clandestinely infected with malicious code and then digitally signed by the unsuspecting developer, where the software has been altered via a compromised software development or build process prior to being signed. The receiver or user of the software has no reason to believe that it is anything but legitimate and proceeds to deploy it to organizational systems. This attack differs from CAPEC-206, since the developer is inadvertently signing malicious code they believe to be legitimate and which they are unware of any malicious modifications.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- An adversary would need to have access to a targeted developer’s software development environment, including to their software build processes, where the adversary could ensure code maliciously tainted prior to a build process is included in software packages built.

## Skills Required
- [High] The adversary must have the skills to infiltrate a developer’s software development/build environment and to implant malicious code in developmental software code, a build server, or a software repository containing dependency code, which would be referenced to be included during the software build process.

## Consequences
- Scope: Integrity, Confidentiality; Impact: Read Data, Modify Data
- Scope: Access Control, Authorization; Impact: Gain Privileges, Execute Unauthorized Commands

## Mitigations
- Have a security concept of operations (CONOPS) for the IDE that includes: Protecting the IDE via logical isolation using firewall and DMZ technologies/architectures; Maintaining strict security administration and configuration management of configuration management tools, developmental software and dependency code repositories, compilers, and system build tools.
- Employ intrusion detection and malware detection capabilities on IDE systems where feasible.


---

# CAPEC-674: Design for FPGA Maliciously Altered

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/674.html  

## Description
An adversary alters the functionality of a field-programmable gate array (FPGA) by causing an FPGA configuration memory chip reload in order to introduce a malicious function that could result in the FPGA performing or enabling malicious functions on a host system. Prior to the memory chip reload, the adversary alters the program for the FPGA by adding a function to impact system operation.

## Related Attack Patterns
- ChildOf: CAPEC-447

## Prerequisites
- An adversary would need to have access to FPGA programming/configuration-related systems in a chip maker’s development environment where FPGAs can be initially configured prior to delivery to a customer or have access to such systems in a customer facility where end-user FPGA configuration/reconfiguration can be performed.

## Skills Required
- [High] An adversary would need to be skilled in FPGA programming in order to create/manipulate configurations in such a way that when loaded into an FPGA, the end user would be able to observe through testing all user-defined required functions but would be unaware of any additional functions the adversary may have introduced.

## Consequences
- Scope: Integrity; Impact: Alter Execution Logic

## Mitigations
- Utilize DMEA’s (Defense Microelectronics Activity) Trusted Foundry Program members for acquisition of microelectronic components.
- Ensure that each supplier performing hardware development implements comprehensive, security-focused configuration management including for FPGA programming and program uploads to FPGA chips.
- Require that provenance of COTS microelectronic components be known whenever procured.
- Conduct detailed vendor assessment before acquiring COTS hardware.


---

# CAPEC-675: Retrieve Data from Decommissioned Devices

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/675.html  

## Description
An adversary obtains decommissioned, recycled, or discarded systems and devices that can include an organization’s intellectual property, employee data, and other types of controlled information. Systems and devices that have reached the end of their lifecycles may be subject to recycle or disposal where they can be exposed to adversarial attempts to retrieve information from internal memory chips and storage devices that are part of the system.

## Related Attack Patterns
- ChildOf: CAPEC-116
- CanPrecede: CAPEC-37

## Prerequisites
- An adversary needs to have access to electronic data processing equipment being recycled or disposed of (e.g., laptops, servers) at a collection location and the ability to take control of it for the purpose of exploiting its content.

## Skills Required
- [High] An adversary may need the ability to mount printed circuit boards and target individual chips for exploitation.
- [Medium] An adversary needs the technical skills required to extract solid state drives, hard disk drives, and other storage media to host on a compatible system or harness to gain access to digital content.

## Consequences
- Scope: Accountability; Impact: Bypass Protection Mechanism

## Mitigations
- Backup device data before erasure to retain intellectual property and inside knowledge.
- Overwrite data on device rather than deleting. Deleted data can still be recovered, even if the device trash can is emptied. Rewriting data removes any trace of the old data. Performing multiple overwrites followed by a zeroing of the device (overwriting with all zeros) is good practice.
- Use a secure erase software.
- Physically destroy the device if it is not intended to be reused. Using a specialized service to disintegrate, burn, melt or pulverize the device can be effective, but if those services are inaccessible, drilling nails or holes, or smashing the device with a hammer can be effective. Do not burn, microwave, or pour acid on a hard drive.
- Physically destroy memory and SIM cards for mobile devices not intended to be reused.
- Ensure that the user account has been terminated or switched to a new device before destroying.

## Related Weaknesses (CWE)
- CWE-1266


---

# CAPEC-676: NoSQL Injection

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/676.html  

## Description
An adversary targets software that constructs NoSQL statements based on user input or with parameters vulnerable to operator replacement in order to achieve a variety of technical impacts such as escalating privileges, bypassing authentication, and/or executing code.

## Related Attack Patterns
- ChildOf: CAPEC-248

## Prerequisites
- Awareness of the technology stack being leveraged by the target application.
- NoSQL queries used by the application to store, retrieve, or modify data.
- User-controllable input that is not properly validated by the application as part of NoSQL queries.
- Target potentially susceptible to operator replacement attacks.

## Skills Required
- [Low] For keyword and JavaScript injection attacks, it is fairly simple for someone with basic NoSQL knowledge to perform NoSQL injection, once the target's technology stack has been determined.
- [Medium] For operator replacement attacks, the adversary must also have knowledge of HTTP Parameter Pollution attacks and how to conduct them.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as relevant NoSQL and JavaScript content. NoSQL-specific keywords, such as $ne, $eq or $gt for MongoDB, must be filtered in addition to characters such as a single-quote(') or semicolons (;) based on the context in which they appear. Validation should also extend to expected types.
- If possible, leverage safe APIs (e.g., PyMongo and Flask-PyMongo for Python and MongoDB) for queries as opposed to building queries from strings.
- Ensure the most recent version of a NoSQL database and it's corresponding API are used by the application.
- Use of custom error pages - Adversaries can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the database or application.
- Exercise the principle of Least Privilege with regards to application accounts to minimize damage if a NoSQL injection attack is successful.
- If using MongoDB, disable server-side JavaScript execution and leverage a sanitization module such as "mongo-sanitize".
- If using PHP with MongoDB, ensure all special query operators (starting with $) use single quotes to prevent operator replacement attacks.
- Additional mitigations will depend on the NoSQL database, API, and programming language leveraged by the application.

## Related Weaknesses (CWE)
- CWE-943
- CWE-1286


---

# CAPEC-677: Server Motherboard Compromise

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/677.html  

## Description
Malware is inserted in a server motherboard (e.g., in the flash memory) in order to alter server functionality from that intended. The development environment or hardware/software support activity environment is susceptible to an adversary inserting malicious software into hardware components during development or update.

## Related Attack Patterns
- ChildOf: CAPEC-534

## Prerequisites
- An adversary with access to hardware/software processes and tools within the development or hardware/software support environment can insert malicious software into hardware components during development or update/maintenance.

## Consequences
- Scope: Integrity; Impact: Execute Unauthorized Commands

## Mitigations
- Purchase IT systems, components and parts from government approved vendors whenever possible.
- Establish diversity among suppliers.
- Conduct rigorous threat assessments of suppliers.
- Require that Bills of Material (BoM) for critical parts and components be certified.
- Utilize contract language requiring contractors and subcontractors to flow down to subcontractors and suppliers SCRM and SCRA (Supply Chain Risk Assessment) requirements.
- Establish trusted supplier networks.


---

# CAPEC-678: System Build Data Maliciously Altered

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/678.html  

## Description
During the system build process, the system is deliberately misconfigured by the alteration of the build data. Access to system configuration data files and build processes is susceptible to deliberate misconfiguration of the system.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- An adversary has access to the data files and processes used for executing system configuration and performing the build.

## Consequences
- Scope: Integrity; Impact: Execute Unauthorized Commands
- Scope: Access Control; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Modify Data, Read Data

## Mitigations
- Implement configuration management security practices that protect the integrity of software and associated data.
- Monitor and control access to the configuration management system.
- Harden centralized repositories against attack.
- Establish acceptance criteria for configuration management check-in to assure integrity.
- Plan for and audit the security of configuration management administration processes.
- Maintain configuration control over operational systems.


---

# CAPEC-679: Exploitation of Improperly Configured or Implemented Memory Protections

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/679.html  

## Description
An adversary takes advantage of missing or incorrectly configured access control within memory to read/write data or inject malicious code into said memory.

## Related Attack Patterns
- ChildOf: CAPEC-1
- ChildOf: CAPEC-180

## Prerequisites
- Access to the hardware being leveraged.

## Skills Required
- [Medium] Ability to craft malicious code to inject into the memory region.
- [High] Intricate knowledge of memory structures.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Ensure that protected and unprotected memory ranges are isolated and do not overlap.
- If memory regions must overlap, leverage memory priority schemes if memory regions can overlap.
- Ensure that original and mirrored memory regions apply the same protections.
- Ensure immutable code or data is programmed into ROM or write-once memory.

## Related Weaknesses (CWE)
- CWE-1222
- CWE-1252
- CWE-1257
- CWE-1260
- CWE-1274
- CWE-1282
- CWE-1312
- CWE-1316
- CWE-1326


---

# CAPEC-68: Subvert Code-signing Facilities

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/68.html  

## Description
Many languages use code signing facilities to vouch for code's identity and to thus tie code to its assigned privileges within an environment. Subverting this mechanism can be instrumental in an attacker escalating privilege. Any means of subverting the way that a virtual machine enforces code signing classifies for this style of attack.

## Related Attack Patterns
- ChildOf: CAPEC-233

## Prerequisites
- A framework-based language that supports code signing (such as, and most commonly, Java or .NET)
- Deployed code that has been signed by its authoring vendor, or a partner.
- The attacker will, for most circumstances, also need to be able to place code in the victim container. This does not necessarily mean that they will have to subvert host-level security, except when explicitly indicated.

## Skills Required
- [High] Subverting code signing is not a trivial activity. Most code signing and verification schemes are based on use of cryptography and the attacker needs to have an understanding of these cryptographic operations in good detail. Additionally the attacker also needs to be aware of the way memory is assigned and accessed by the container since, often, the only way to subvert code signing would be to patch the code in memory. Finally, a knowledge of the platform specific mechanisms of signing and verifying code is a must.

## Resources Required
- The Attacker needs no special resources beyond the listed prerequisites in order to conduct this style of attack.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- A given code signing scheme may be fallible due to improper use of cryptography. Developers must never roll out their own cryptography, nor should existing primitives be modified or ignored.
- If an attacker cannot attack the scheme directly, they might try to alter the environment that affects the signing and verification processes. A possible mitigation is to avoid reliance on flags or environment variables that are user-controllable.

## Related Weaknesses (CWE)
- CWE-325
- CWE-328
- CWE-1326


---

# CAPEC-680: Exploitation of Improperly Controlled Registers

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/680.html  

## Description
An adversary exploits missing or incorrectly configured access control within registers to read/write data that is not meant to be obtained or modified by a user.

## Related Attack Patterns
- ChildOf: CAPEC-1
- ChildOf: CAPEC-180

## Prerequisites
- Awareness of the hardware being leveraged.
- Access to the hardware being leveraged.

## Skills Required
- [High] Intricate knowledge of registers.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Design proper access control policies for hardware register access from software and ensure these policies are implemented in accordance with the specified design.
- Ensure security lock bit protections are reviewed for design inconsistencies and common weaknesses.
- Test security lock programming flow in both pre-silicon and post-silicon environments.
- Leverage automated tools to test that values are not reprogrammable and that write-once fields lock on writing zeros.
- Ensure that measurement data is stored in registers that are read-only or otherwise have access controls that prevent modification by an untrusted agent.

## Related Weaknesses (CWE)
- CWE-1224
- CWE-1231
- CWE-1233
- CWE-1262
- CWE-1283


---

# CAPEC-681: Exploitation of Improperly Controlled Hardware Security Identifiers

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/681.html  

## Description
An adversary takes advantage of missing or incorrectly configured security identifiers (e.g., tokens), which are used for access control within a System-on-Chip (SoC), to read/write data or execute a given action.

## Related Attack Patterns
- ChildOf: CAPEC-1
- ChildOf: CAPEC-180

## Prerequisites
- Awareness of the hardware being leveraged.
- Access to the hardware being leveraged.

## Skills Required
- [Medium] Ability to execute actions within the SoC.
- [High] Intricate knowledge of the identifiers being utilized.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Review generation of security identifiers for design inconsistencies and common weaknesses.
- Review security identifier decoders for design inconsistencies and common weaknesses.
- Test security identifier definition, access, and programming flow in both pre-silicon and post-silicon environments.

## Related Weaknesses (CWE)
- CWE-1259
- CWE-1267
- CWE-1270
- CWE-1294
- CWE-1302


---

# CAPEC-682: Exploitation of Firmware or ROM Code with Unpatchable Vulnerabilities

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/682.html  

## Description
An adversary may exploit vulnerable code (i.e., firmware or ROM) that is unpatchable. Unpatchable devices exist due to manufacturers intentionally or inadvertently designing devices incapable of updating their software. Additionally, with updatable devices, the manufacturer may decide not to support the device and stop making updates to their software.

## Related Attack Patterns
- ChildOf: CAPEC-212

## Prerequisites
- Awareness of the hardware being leveraged.
- Access to the hardware being leveraged, either physically or remotely.

## Skills Required
- [Medium] Knowledge of various wireless protocols to enable remote access to vulnerable devices
- [High] Ability to identify physical entry points such as debug interfaces if the device is not being accessed remotely

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Design systems and products with the ability to patch firmware or ROM code after deployment to fix vulnerabilities.
- Make use of OTA (Over-the-air) updates so that firmware can be patched remotely either through manual or automatic means

## Related Weaknesses (CWE)
- CWE-1277
- CWE-1310


---

# CAPEC-69: Target Programs with Elevated Privileges

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/69.html  

## Description
This attack targets programs running with elevated privileges. The adversary tries to leverage a vulnerability in the running program and get arbitrary code to execute with elevated privileges.

## Related Attack Patterns
- ChildOf: CAPEC-233
- CanPrecede: CAPEC-8
- CanPrecede: CAPEC-9
- CanPrecede: CAPEC-10
- CanPrecede: CAPEC-67

## Prerequisites
- The targeted program runs with elevated OS privileges.
- The targeted program accepts input data from the user or from another program.
- The targeted program is giving away information about itself. Before performing such attack, an eventual attacker may need to gather information about the services running on the host target. The more the host target is verbose about the services that are running (version number of application, etc.) the more information can be gather by an attacker.
- This attack often requires communicating with the host target services directly. For instance Telnet may be enough to communicate with the host target.

## Skills Required
- [Low] An attacker can use a tool to scan and automatically launch an attack against known issues. A tool can also repeat a sequence of instructions and try to brute force the service on the host target, an example of that would be the flooding technique.
- [Medium] More advanced attack may require knowledge of the protocol spoken by the host service.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Apply the principle of least privilege.
- Validate all untrusted data.
- Apply the latest patches.
- Scan your services and disable the ones which are not needed and are exposed unnecessarily. Exposing programs increases the attack surface. Only expose the services which are needed and have security mechanisms such as authentication built around them.
- Avoid revealing information about your system (e.g., version of the program) to anonymous users.
- Make sure that your program or service fail safely. What happen if the communication protocol is interrupted suddenly? What happen if a parameter is missing? Does your system have resistance and resilience to attack? Fail safely when a resource exhaustion occurs.
- If possible use a sandbox model which limits the actions that programs can take. A sandbox restricts a program to a set of privileges and commands that make it difficult or impossible for the program to cause any damage.
- Check your program for buffer overflow and format String vulnerabilities which can lead to execution of malicious code.
- Monitor traffic and resource usage and pay attention if resource exhaustion occurs.
- Protect your log file from unauthorized modification and log forging.

## Related Weaknesses (CWE)
- CWE-250
- CWE-15


---

# CAPEC-690: Metadata Spoofing

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/690.html  

## Description
An adversary alters the metadata of a resource (e.g., file, directory, repository, etc.) to present a malicious resource as legitimate/credible.

## Prerequisites
- Identification of a resource whose metadata is to be spoofed

## Skills Required
- [Medium] Ability to spoof a variety of metadata to convince victims the source is trusted

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Accountability; Impact: Hide Activities
- Scope: Access Control, Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Validate metadata of resources such as authors, timestamps, and statistics.
- Confirm the pedigree of open source packages and ensure the code being downloaded does not originate from another source.
- Even if the metadata is properly checked and a user believes it to be legitimate, there may still be a chance that they've been duped. Therefore, leverage automated testing techniques to determine where malicious areas of the code may exist.


---

# CAPEC-691: Spoof Open-Source Software Metadata

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/691.html  

## Description
An adversary spoofs open-source software metadata in an attempt to masquerade malicious software as popular, maintained, and trusted.

## Related Attack Patterns
- ChildOf: CAPEC-690
- CanPrecede: CAPEC-184
- CanPrecede: CAPEC-444
- PeerOf: CAPEC-630

## Prerequisites
- Identification of a popular open-source component whose metadata is to be spoofed.

## Skills Required
- [Medium] Ability to spoof a variety of software metadata to convince victims the source is trusted.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Accountability; Impact: Hide Activities
- Scope: Access Control, Authorization; Impact: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges

## Mitigations
- Before downloading open-source software, perform precursory metadata checks to determine the author(s), frequency of updates, when the software was last updated, and if the software is widely leveraged.
- Within package managers, look for conflicting or non-unique repository references to determine if multiple packages share the same repository reference.
- Reference vulnerability databases to determine if the software contains known vulnerabilities.
- Only download open-source software from reputable hosting sites or package managers.
- Only download open-source software that has been adequately signed by the developer(s). For repository commits/tags, look for the "Verified" status and for developers leveraging "Vigilant Mode" (GitHub) or similar modes.
- After downloading open-source software, ensure integrity values have not changed.
- Before executing or incorporating the software, leverage automated testing techniques (e.g., static and dynamic analysis) to determine if the software behaves maliciously.

## Related Weaknesses (CWE)
- CWE-494


---

# CAPEC-692: Spoof Version Control System Commit Metadata

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/692.html  

## Description
An adversary spoofs metadata pertaining to a Version Control System (VCS) (e.g., Git) repository's commits to deceive users into believing that the maliciously provided software is frequently maintained and originates from a trusted source.

## Related Attack Patterns
- ChildOf: CAPEC-691

## Prerequisites
- Identification of a popular open-source repository whose metadata is to be spoofed.

## Skills Required
- [Medium] Ability to spoof a variety of repository metadata to convince victims the source is trusted.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Accountability; Impact: Hide Activities
- Scope: Access Control, Authorization; Impact: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges

## Mitigations
- Before downloading open-source software, perform precursory metadata checks to determine the author(s), frequency of updates, when the software was last updated, and if the software is widely leveraged.
- Reference vulnerability databases to determine if the software contains known vulnerabilities.
- Only download open-source software from reputable hosting sites or package managers.
- Only download open-source software that has been adequately signed by the developer(s). For repository commits/tags, look for the "Verified" status and for developers leveraging "Vigilant Mode" (GitHub) or similar modes.
- After downloading open-source software, ensure integrity values have not changed.
- Before executing or incorporating the software, leverage automated testing techniques (e.g., static and dynamic analysis) to determine if the software behaves maliciously.

## Related Weaknesses (CWE)
- CWE-494


---

# CAPEC-693: StarJacking

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/693.html  

## Description
An adversary spoofs software popularity metadata to deceive users into believing that a maliciously provided package is widely used and originates from a trusted source.

## Related Attack Patterns
- ChildOf: CAPEC-691

## Prerequisites
- Identification of a popular open-source package whose popularity metadata is to be used for the malicious package.

## Skills Required
- [Low] Ability to provide a package to a package manager and associate a popular package's source code repository URL.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Accountability; Impact: Hide Activities
- Scope: Access Control, Authorization; Impact: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges

## Mitigations
- Before downloading open-source packages, perform precursory metadata checks to determine the author(s), frequency of updates, when the software was last updated, and if the software is widely leveraged.
- Look for conflicting or non-unique repository references to determine if multiple packages share the same repository reference.
- Reference vulnerability databases to determine if the software contains known vulnerabilities.
- Only download open-source packages from reputable package managers.
- After downloading open-source packages, ensure integrity values have not changed.
- Before executing or incorporating the package, leverage automated testing techniques (e.g., static and dynamic analysis) to determine if the software behaves maliciously.

## Related Weaknesses (CWE)
- CWE-494


---

# CAPEC-694: System Location Discovery

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very Low  
**Reference:** https://capec.mitre.org/data/definitions/694.html  

## Description
An adversary collects information about the target system in an attempt to identify the system's geographical location. Information gathered could include keyboard layout, system language, and timezone. This information may benefit an adversary in confirming the desired target and/or tailoring further attacks.

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary must have some level of access to the system and have a basic understanding of the operating system in order to query the appropriate sources for relevant information.

## Skills Required
- [Low] The adversary must know how to query various system sources of information respective of the system's operating system to obtain the relevant information.

## Resources Required
- The adversary requires access to the target's operating system tools to query relevant system information. On windows, registry queries can be conducted with powershell, wmi, or regedit. On Linux or macOS, queries can be performed with through a shell.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- To reduce the amount of information gathered, one could disable various geolocation features of the operating system not required for system operation.

## Related Weaknesses (CWE)
- CWE-497


---

# CAPEC-695: Repo Jacking

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/695.html  

## Description
An adversary takes advantage of the redirect property of directly linked Version Control System (VCS) repositories to trick users into incorporating malicious code into their applications.

## Related Attack Patterns
- ChildOf: CAPEC-616

## Prerequisites
- Identification of a popular repository that may be directly referenced in numerous software applications
- A repository owner/maintainer who has recently changed their username or deleted their account

## Skills Required
- [Low] Ability to create an account on a VCS hosting site and recreate an existing directory structure.
- [Low] Ability to create malware that can exploit various software applications.

## Consequences
- Scope: Integrity; Impact: Read Data, Modify Data
- Scope: Access Control, Authorization; Impact: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges

## Mitigations
- Leverage dedicated package managers instead of directly linking to VCS repositories.
- Utilize version pinning and lock files to prevent use of maliciously modified repositories.
- Implement "vendoring" (i.e., including third-party dependencies locally) and leverage automated testing techniques (e.g., static analysis) to determine if the software behaves maliciously.
- Leverage automated tools, such as Checkmarx's "ChainJacking" tool, to determine susceptibility to Repo Jacking attacks.

## Related Weaknesses (CWE)
- CWE-494
- CWE-829


---

# CAPEC-696: Load Value Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/696.html  

## Description
An adversary exploits a hardware design flaw in a CPU implementation of transient instruction execution in which a faulting or assisted load instruction transiently forwards adversary-controlled data from microarchitectural buffers. By inducing a page fault or microcode assist during victim execution, an adversary can force legitimate victim execution to operate on the adversary-controlled data which is stored in the microarchitectural buffers. The adversary can then use existing code gadgets and side channel analysis to discover victim secrets that have not yet been flushed from microarchitectural state or hijack the system control flow.

## Related Attack Patterns
- ChildOf: CAPEC-663

## Prerequisites
- The adversary needs at least user execution access to a system and a maliciously crafted program/application/process with unprivileged code to misuse transient instruction set execution of the CPU.
- The CPU incorrectly transiently forwards values from microarchitectural buffers after faulting or assisted loads
- The adversary needs the ability to induce page faults or microcode assists on the target system.
- Code gadgets exist that allow the adversary to hijack transient execution and encode secrets into the microarchitectural state.

## Skills Required
- [High] Detailed knowledge on how various CPU architectures and microcode perform transient execution for various low-level assembly language code instructions/operations.
- [High] Detailed knowledge on compiled binaries and operating system shared libraries of instruction sequences, and layout of application and OS/Kernel address spaces for data leakage.
- [High] The ability to provoke faulting or assisted loads in legitimate execution.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Access Control; Impact: Bypass Protection Mechanism
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Do not allow the forwarding of data resulting from a faulting or assisted instruction. Some current mitigations claim to zero out the forwarded data, but this mitigation still does not suffice.
- Insert explicit “lfence” speculation barriers in software before potentially faulting or assisted loads. This halts transient execution until all previous instructions have been executed and ensures that the architecturally correct value is forwarded.

## Related Weaknesses (CWE)
- CWE-1342


---

# CAPEC-697: DHCP Spoofing

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/697.html  

## Description
An adversary masquerades as a legitimate Dynamic Host Configuration Protocol (DHCP) server by spoofing DHCP traffic, with the goal of redirecting network traffic or denying service to DHCP.

## Related Attack Patterns
- ChildOf: CAPEC-194
- CanPrecede: CAPEC-158
- CanPrecede: CAPEC-94

## Prerequisites
- The adversary must have access to a machine within the target LAN which can send DHCP offers to the target.

## Skills Required
- [Medium] The adversary must identify potential targets for DHCP Spoofing and craft network configurations to obtain the desired results.

## Resources Required
- The adversary requires access to a machine within the target LAN on a network which does not secure its DHCP traffic through MAC-Forced Forwarding, port security, etc.

## Consequences
- Scope: Confidentiality, Access Control; Impact: Read Data
- Scope: Integrity, Access Control; Impact: Modify Data, Execute Unauthorized Commands
- Scope: Availability; Impact: Resource Consumption

## Mitigations
- Design: MAC-Forced Forwarding
- Implementation: Port Security and DHCP snooping
- Implementation: Network-based Intrusion Detection Systems

## Related Weaknesses (CWE)
- CWE-923


---

# CAPEC-698: Install Malicious Extension

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/698.html  

## Description
An adversary directly installs or tricks a user into installing a malicious extension into existing trusted software, with the goal of achieving a variety of negative technical impacts.

## Related Attack Patterns
- ChildOf: CAPEC-542

## Prerequisites
- The adversary must craft malware based on the type of software and system(s) they intend to exploit.
- If the adversary intends to install the malicious extension themself, they must first compromise the target machine via some other means.

## Skills Required
- [Medium] Ability to create malicious extensions that can exploit specific software applications and systems.
- [Medium] Optional: Ability to exploit target system(s) via other means in order to gain entry.

## Consequences
- Scope: Confidentiality, Access Control; Impact: Read Data
- Scope: Integrity, Access Control; Impact: Modify Data
- Scope: Authorization, Access Control; Impact: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges

## Mitigations
- Only install extensions/plugins from official/verifiable sources.
- Confirm extensions/plugins are legitimate and not malware masquerading as a legitimate extension/plugin.
- Ensure the underlying software leveraging the extension/plugin (including operating systems) is up-to-date.
- Implement an extension/plugin allow list, based on the given security policy.
- If applicable, confirm extensions/plugins are properly signed by the official developers.
- For web browsers, close sessions when finished to prevent malicious extensions/plugins from executing the the background.

## Related Weaknesses (CWE)
- CWE-507
- CWE-829


---

# CAPEC-699: Eavesdropping on a Monitor

**Abstraction:** Meta  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/699.html  

## Description
An Adversary can eavesdrop on the content of an external monitor through the air without modifying any cable or installing software, just capturing this signal emitted by the cable or video port, with this the attacker will be able to impact the confidentiality of the data without being detected by traditional security tools

## Related Attack Patterns
- ChildOf: CAPEC-651

## Prerequisites
- Victim should use an external monitor device
- Physical access to the target location and devices

## Skills Required
- [Medium] Knowledge of how to use the SDR and related software: With this knowledge, the adversary will find the correct frequency where the signal is being leaked
- [Low] Understanding of computing hardware, to identify the video cable and video ports

## Resources Required
- SDR device set with the correspondent antenna
- Computer with SDR Software

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Enhance: Increase the number of electromagnetic shield layers in the display ports and cables to contain or reduce the intensity of the leaked signal.
- Implement: Use a protocol that encrypts the video signal; in case the signal is intercepted the signal is protected by the encryption.
- Design: Lock away the video cables, making it difficult for the attacker to access the cables and place the antenna near them (If the distance condition between the antenna and display port/cable is not satisfied, the attack will not be possible).
- Implement: Use wireless technologies to connect to external display devices.

## Related Weaknesses (CWE)
- CWE-1300


---

# CAPEC-7: Blind SQL Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/7.html  

## Description
Blind SQL Injection results from an insufficient mitigation for SQL Injection. Although suppressing database error messages are considered best practice, the suppression alone is not sufficient to prevent SQL Injection. Blind SQL Injection is a form of SQL Injection that overcomes the lack of error messages. Without the error messages that facilitate SQL Injection, the adversary constructs input strings that probe the target through simple Boolean SQL expressions. The adversary can determine if the syntax and structure of the injection was successful based on whether the query was executed or not. Applied iteratively, the adversary determines how and where the target is vulnerable to SQL Injection.

## Related Attack Patterns
- ChildOf: CAPEC-66

## Prerequisites
- SQL queries used by the application to store, retrieve or modify data.
- User-controllable input that is not properly validated by the application as part of SQL queries.

## Skills Required
- [Medium] Determining the database type and version, as well as the right number and type of parameters to the query being injected in the absence of error messages requires greater skill than reverse-engineering database error messages.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Security by Obscurity is not a solution to preventing SQL Injection. Rather than suppress error messages and exceptions, the application must handle them gracefully, returning either a custom error page or redirecting the user to a default page, without revealing any information about the database or the application internals.
- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as SQL content. Keywords such as UNION, SELECT or INSERT must be filtered in addition to characters such as a single-quote(') or SQL-comments (--) based on the context in which they appear.

## Related Weaknesses (CWE)
- CWE-89
- CWE-209
- CWE-74
- CWE-20
- CWE-697
- CWE-707


---

# CAPEC-70: Try Common or Default Usernames and Passwords

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/70.html  

## Description
An adversary may try certain common or default usernames and passwords to gain access into the system and perform unauthorized actions. An adversary may try an intelligent brute force using empty passwords, known vendor default credentials, as well as a dictionary of common usernames and passwords. Many vendor products come preconfigured with default (and thus well-known) usernames and passwords that should be deleted prior to usage in a production environment. It is a common mistake to forget to remove these default login credentials. Another problem is that users would pick very simple (common) passwords (e.g. "secret" or "password") that make it easier for the attacker to gain access to the system compared to using a brute force attack or even a dictionary attack using a full dictionary.

## Related Attack Patterns
- ChildOf: CAPEC-49
- CanPrecede: CAPEC-600
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-560
- CanPrecede: CAPEC-561
- CanPrecede: CAPEC-653

## Prerequisites
- The system uses one factor password based authentication.The adversary has the means to interact with the system.

## Skills Required
- [Low] An adversary just needs to gain access to common default usernames/passwords specific to the technologies used by the system. Additionally, a brute force attack leveraging common passwords can be easily realized if the user name is known.

## Resources Required
- Technology or vendor specific list of default usernames and passwords.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Delete all default account credentials that may be put in by the product vendor.
- Implement a password throttling mechanism. This mechanism should take into account both the IP address and the log in name of the user.
- Put together a strong password policy and make sure that all user created passwords comply with it. Alternatively automatically generate strong passwords for users.
- Passwords need to be recycled to prevent aging, that is every once in a while a new password must be chosen.

## Related Weaknesses (CWE)
- CWE-521
- CWE-262
- CWE-263
- CWE-798
- CWE-654
- CWE-308
- CWE-309


---

# CAPEC-700: Network Boundary Bridging

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/700.html  

## Description
An adversary which has gained elevated access to network boundary devices may use these devices to create a channel to bridge trusted and untrusted networks. Boundary devices do not necessarily have to be on the network’s edge, but rather must serve to segment portions of the target network the adversary wishes to cross into.

## Related Attack Patterns
- ChildOf: CAPEC-161
- CanFollow: CAPEC-70
- CanFollow: CAPEC-560

## Prerequisites
- The adversary must have control of a network boundary device.

## Skills Required
- [Medium] The adversary must understand how to manage the target network device to create or edit policies which will bridge networks.

## Resources Required
- The adversary requires either high privileges or full control of a boundary device on a target network.

## Consequences
- Scope: Confidentiality, Access Control; Impact: Read Data, Bypass Protection Mechanism
- Scope: Integrity, Authorization; Impact: Alter Execution Logic, Hide Activities

## Mitigations
- Design: Ensure network devices are storing credentials in encrypted stores
- Design: Follow the principle of least privilege and restrict administrative duties to as few accounts as possible. Ensure these privileged accounts are secured with strong credentials which do not overlap with other network devices.
- Configuration: When possible, configure network boundary devices to use MFA.
- Configuration: Change the default configuration for network devices to harden their security profiles. Default configurations are often enabled with insecure features to allow ease of installation and management. However, these configurations can be easily discovered and exploited by adversaries.
- Implementation: Perform integrity checks on audit logs for network device management and review them to identify abnormalities in configurations.
- Implementation: Prevent network boundary devices from being physically accessed by unauthorized personnel to prevent tampering.


---

# CAPEC-701: Browser in the Middle (BiTM)

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/701.html  

## Description
An adversary exploits the inherent functionalities of a web browser, in order to establish an unnoticed remote desktop connection in the victim's browser to the adversary's system. The adversary must deploy a web client with a remote desktop session that the victim can access.

## Related Attack Patterns
- ChildOf: CAPEC-94
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-148
- CanFollow: CAPEC-98

## Prerequisites
- The adversary must create a convincing web client to establish the connection. The victim then needs to be lured onto the adversary's webpage. In addition, the victim's machine must not use local authentication APIs, a hardware token, or a Trusted Platform Module (TPM) to authenticate.

## Resources Required
- A web application with a client is needed to enable the victim's browser to establish a remote desktop connection to the system of the adversary.

## Consequences
- Scope: Confidentiality, Access Control, Authentication; Impact: Gain Privileges
- Scope: Confidentiality, Authorization; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Implementation: Use strong, mutual authentication to fully authenticate with both ends of any communications channel

## Related Weaknesses (CWE)
- CWE-294
- CWE-345


---

# CAPEC-702: Exploiting Incorrect Chaining or Granularity of Hardware Debug Components

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/702.html  

## Description
An adversary exploits incorrect chaining or granularity of hardware debug components in order to gain unauthorized access to debug functionality on a chip. This happens when authorization is not checked on a per function basis and is assumed for a chain or group of debug functionality.

## Related Attack Patterns
- ChildOf: CAPEC-180

## Prerequisites
- Hardware device has an exposed debug interface

## Skills Required
- [Medium] Ability to identify physical debug interfaces on a device
- [Medium] Ability to operate devices to scan and connect to an exposed debug interface

## Resources Required
- A device to scan a TAP or JTAG interface, such as a JTAGulator
- A device to communicate on a TAP or JTAG interface, such as a BusPirate

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data
- Scope: Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Implement: Ensure that debug components are properly chained, and their granularity is maintained at different authorization levels
- Perform Post-silicon validation tests at various authorization levels to ensure that debug components are only accessible to authorized users

## Related Weaknesses (CWE)
- CWE-1296


---

# CAPEC-71: Using Unicode Encoding to Bypass Validation Logic

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/71.html  

## Description
An attacker may provide a Unicode string to a system component that is not Unicode aware and use that to circumvent the filter or cause the classifying mechanism to fail to properly understanding the request. That may allow the attacker to slip malicious data past the content filter and/or possibly cause the application to route the request incorrectly.

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- Filtering is performed on data that has not be properly canonicalized.

## Skills Required
- [Medium] An attacker needs to understand Unicode encodings and have an idea (or be able to find out) what system components may not be Unicode aware.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Ensure that the system is Unicode aware and can properly process Unicode data. Do not make an assumption that data will be in ASCII.
- Ensure that filtering or input validation is applied to canonical data.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.

## Related Weaknesses (CWE)
- CWE-176
- CWE-179
- CWE-180
- CWE-173
- CWE-172
- CWE-184
- CWE-183
- CWE-74
- CWE-20
- CWE-697
- CWE-692


---

# CAPEC-72: URL Encoding

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/72.html  

## Description
This attack targets the encoding of the URL. An adversary can take advantage of the multiple way of encoding an URL and abuse the interpretation of the URL.

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- The application should accepts and decodes URL input.
- The application performs insufficient filtering/canonicalization on the URLs.

## Skills Required
- [Low] An adversary can try special characters in the URL and bypass the URL validation.
- [Medium] The adversary may write a script to defeat the input filtering mechanism.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Refer to the RFCs to safely decode URL.
- Regular expression can be used to match safe URL patterns. However, that may discard valid URL requests if the regular expression is too restrictive.
- There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx).
- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system. Test your decoding process against malicious input.
- Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding. (See related guideline section)
- When client input is required from web-based forms, avoid using the "GET" method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the "POST method whenever possible.

## Related Weaknesses (CWE)
- CWE-173
- CWE-177
- CWE-172
- CWE-73
- CWE-74
- CWE-20


---

# CAPEC-73: User-Controlled Filename

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/73.html  

## Description
An attack of this type involves an adversary inserting malicious characters (such as a XSS redirection) into a filename, directly or indirectly that is then used by the target software to generate HTML text or other potentially executable content. Many websites rely on user-generated content and dynamically build resources like files, filenames, and URL links directly from user supplied data. In this attack pattern, the attacker uploads code that can execute in the client browser and/or redirect the client browser to a site that the attacker owns. All XSS attack payload variants can be used to pass and exploit these vulnerabilities.

## Related Attack Patterns
- ChildOf: CAPEC-165
- CanPrecede: CAPEC-592

## Prerequisites
- The victim must trust the name and locale of user controlled filenames.

## Skills Required
- [Low] To achieve a redirection and use of less trusted source, an attacker can simply edit data that the host uses to build the filename
- [Medium] Deploying a malicious "look-a-like" site (such as a site masquerading as a bank or online auction site) that the user enters their authentication data into.
- [High] Exploiting a client side vulnerability to inject malicious scripts into the browser's executable process.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Availability; Impact: Alter Execution Logic
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Design: Use browser technologies that do not allow client side scripting.
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Perform input validation for all remote content.
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser
- Implementation: Scan dynamically generated content against validation specification

## Related Weaknesses (CWE)
- CWE-20
- CWE-184
- CWE-96
- CWE-348
- CWE-116
- CWE-350
- CWE-86
- CWE-697


---

# CAPEC-74: Manipulating State

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/74.html  

## Description
The adversary modifies state information maintained by the target software or causes a state transition in hardware. If successful, the target will use this tainted state and execute in an unintended manner. State management is an important function within a software application. User state maintained by the application can include usernames, payment information, browsing history as well as application-specific contents such as items in a shopping cart. Manipulating user state can be employed by an adversary to elevate privilege, conduct fraudulent transactions or otherwise modify the flow of the application to derive certain benefits. If there is a hardware logic error in a finite state machine, the adversary can use this to put the system in an undefined state which could cause a denial of service or exposure of secure data.

## Prerequisites
- User state is maintained at least in some way in user-controllable locations, such as cookies or URL parameters.
- There is a faulty finite state machine in the hardware logic that can be exploited.

## Skills Required
- [Medium] The adversary needs to have knowledge of state management as employed by the target application, and also the ability to manipulate the state in a meaningful way.

## Resources Required
- The adversary needs a data tampering tool capable of generating and creating custom inputs to aid in the attack, like Fiddler, Wireshark, or a similar in-browser plugin (e.g., Tamper Data for Firefox).

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Do not rely solely on user-controllable locations, such as cookies or URL parameters, to maintain user state.
- Avoid sensitive information, such as usernames or authentication and authorization information, in user-controllable locations.
- Sensitive information that is part of the user state must be appropriately protected to ensure confidentiality and integrity at each request.
- All possible states must be handled by hardware finite state machines.

## Related Weaknesses (CWE)
- CWE-372
- CWE-315
- CWE-353
- CWE-693
- CWE-1245
- CWE-1253
- CWE-1265
- CWE-1271


---

# CAPEC-75: Manipulating Writeable Configuration Files

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/75.html  

## Description
Generally these are manually edited files that are not in the preview of the system administrators, any ability on the attackers' behalf to modify these files, for example in a CVS repository, gives unauthorized access directly to the application, the same as authorized users.

## Related Attack Patterns
- ChildOf: CAPEC-176

## Prerequisites
- Configuration files must be modifiable by the attacker

## Skills Required
- [Medium] To identify vulnerable configuration files, and understand how to manipulate servers and erase forensic evidence

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Design: Enforce principle of least privilege
- Design: Backup copies of all configuration files
- Implementation: Integrity monitoring for configuration files
- Implementation: Enforce audit logging on code and configuration promotion procedures.
- Implementation: Load configuration from separate process and memory space, for example a separate physical device like a CD

## Related Weaknesses (CWE)
- CWE-349
- CWE-99
- CWE-77
- CWE-346
- CWE-353
- CWE-354


---

# CAPEC-76: Manipulating Web Input to File System Calls

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/76.html  

## Description
An attacker manipulates inputs to the target software which the target software passes to file system calls in the OS. The goal is to gain access to, and perhaps modify, areas of the file system that the target software did not intend to be accessible.

## Related Attack Patterns
- ChildOf: CAPEC-126

## Prerequisites
- Program must allow for user controlled variables to be applied directly to the filesystem

## Skills Required
- [Low] To identify file system entry point and execute against an over-privileged system interface

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Design: Enforce principle of least privilege.
- Design: Ensure all input is validated, and does not contain file system commands
- Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.
- Design: For interactive user applications, consider if direct file system interface is necessary, instead consider having the application proxy communication.
- Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.

## Related Weaknesses (CWE)
- CWE-23
- CWE-22
- CWE-73
- CWE-77
- CWE-346
- CWE-348
- CWE-285
- CWE-272
- CWE-59
- CWE-74
- CWE-15


---

# CAPEC-77: Manipulating User-Controlled Variables

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/77.html  

## Description
This attack targets user controlled variables (DEBUG=1, PHP Globals, and So Forth). An adversary can override variables leveraging user-supplied, untrusted query variables directly used on the application server without any data sanitization. In extreme cases, the adversary can change variables controlling the business logic of the application. For instance, in languages like PHP, a number of poorly set default configurations may allow the user to override variables.

## Related Attack Patterns
- ChildOf: CAPEC-22

## Prerequisites
- A variable consumed by the application server is exposed to the client.
- A variable consumed by the application server can be overwritten by the user.
- The application server trusts user supplied data to compute business logic.
- The application server does not perform proper input validation.

## Skills Required
- [Low] The malicious user can easily try some well-known global variables and find one which matches.
- [Medium] The adversary can use automated tools to probe for variables that they can control.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Do not allow override of global variables and do Not Trust Global Variables. If the register_globals option is enabled, PHP will create global variables for each GET, POST, and cookie variable included in the HTTP request. This means that a malicious user may be able to set variables unexpectedly. For instance make sure that the server setting for PHP does not expose global variables.
- A software system should be reluctant to trust variables that have been initialized outside of its trust boundary. Ensure adequate checking is performed when relying on input from outside a trust boundary.
- Separate the presentation layer and the business logic layer. Variables at the business logic layer should not be exposed at the presentation layer. This is to prevent computation of business logic from user controlled input data.
- Use encapsulation when declaring your variables. This is to lower the exposure of your variables.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should be rejected by the program.

## Related Weaknesses (CWE)
- CWE-15
- CWE-94
- CWE-96
- CWE-285
- CWE-302
- CWE-473
- CWE-1321


---

# CAPEC-78: Using Escaped Slashes in Alternate Encoding

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/78.html  

## Description
This attack targets the use of the backslash in alternate encoding. An adversary can provide a backslash as a leading character and causes a parser to believe that the next character is special. This is called an escape. By using that trick, the adversary tries to exploit alternate ways to encode the same character which leads to filter problems and opens avenues to attack.

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- The application accepts the backlash character as escape character.
- The application server does incomplete input data decoding, filtering and validation.

## Skills Required
- [Low] The adversary can naively try backslash character and discover that the target host uses it as escape character.
- [Medium] The adversary may need deep understanding of the host target in order to exploit the vulnerability. The adversary may also use automated tools to probe for this vulnerability.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Verify that the user-supplied data does not use backslash character to escape malicious characters.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.
- Be aware of the threat of alternative method of data encoding.
- Regular expressions can be used to filter out backslash. Make sure you decode before filtering and validating the untrusted input data.
- In the case of path traversals, use the principle of least privilege when determining access rights to file systems. Do not allow users to access directories/files that they should not access.
- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.
- Avoid making decisions based on names of resources (e.g. files) if those resources can have alternate names.

## Related Weaknesses (CWE)
- CWE-180
- CWE-181
- CWE-173
- CWE-172
- CWE-73
- CWE-22
- CWE-74
- CWE-20
- CWE-697
- CWE-707


---

# CAPEC-79: Using Slashes in Alternate Encoding

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/79.html  

## Description
This attack targets the encoding of the Slash characters. An adversary would try to exploit common filtering problems related to the use of the slashes characters to gain access to resources on the target host. Directory-driven systems, such as file systems and databases, typically use the slash character to indicate traversal between directories or other container components. For murky historical reasons, PCs (and, as a result, Microsoft OSs) choose to use a backslash, whereas the UNIX world typically makes use of the forward slash. The schizophrenic result is that many MS-based systems are required to understand both forms of the slash. This gives the adversary many opportunities to discover and abuse a number of common filtering problems. The goal of this pattern is to discover server software that only applies filters to one version, but not the other.

## Related Attack Patterns
- ChildOf: CAPEC-267

## Prerequisites
- The application server accepts paths to locate resources.
- The application server does insufficient input data validation on the resource path requested by the user.
- The access right to resources are not set properly.

## Skills Required
- [Low] An adversary can try variation of the slashes characters.
- [Medium] An adversary can use more sophisticated tool or script to scan a website and find a path filtering problem.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process. Refer to the RFCs to safely decode URL.
- When client input is required from web-based forms, avoid using the "GET" method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the "POST method whenever possible.
- There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx)
- Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding. (See related guideline section)
- Test your path decoding process against malicious input.
- In the case of path traversals, use the principle of least privilege when determining access rights to file systems. Do not allow users to access directories/files that they should not access.
- Assume all input is malicious. Create an allowlist that defines all valid input to the application based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.

## Related Weaknesses (CWE)
- CWE-173
- CWE-180
- CWE-181
- CWE-20
- CWE-74
- CWE-73
- CWE-22
- CWE-185
- CWE-200
- CWE-697
- CWE-707


---

# CAPEC-8: Buffer Overflow in an API Call

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/8.html  

## Description
This attack targets libraries or shared code modules which are vulnerable to buffer overflow attacks. An adversary who has knowledge of known vulnerable libraries or shared code can easily target software that makes use of these libraries. All clients that make use of the code library thus become vulnerable by association. This has a very broad effect on security across a system, usually affecting more than one software process.

## Related Attack Patterns
- ChildOf: CAPEC-100

## Prerequisites
- The target host exposes an API to the user.
- One or more API functions exposed by the target host has a buffer overflow vulnerability.

## Skills Required
- [Low] An adversary can simply overflow a buffer by inserting a long string into an adversary-modifiable injection vector. The result can be a DoS.
- [High] Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Use a language or compiler that performs automatic bounds checking.
- Use secure functions not vulnerable to buffer overflow.
- If you have to use dangerous functions, make sure that you do boundary checking.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Use OS-level preventative functionality. Not a complete solution.

## Related Weaknesses (CWE)
- CWE-120
- CWE-119
- CWE-118
- CWE-74
- CWE-20
- CWE-680
- CWE-733
- CWE-697


---

# CAPEC-80: Using UTF-8 Encoding to Bypass Validation Logic

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/80.html  

## Description
This attack is a specific variation on leveraging alternate encodings to bypass validation logic. This attack leverages the possibility to encode potentially harmful input in UTF-8 and submit it to applications not expecting or effective at validating this encoding standard making input filtering difficult. UTF-8 (8-bit UCS/Unicode Transformation Format) is a variable-length character encoding for Unicode. Legal UTF-8 characters are one to four bytes long. However, early version of the UTF-8 specification got some entries wrong (in some cases it permitted overlong characters). UTF-8 encoders are supposed to use the "shortest possible" encoding, but naive decoders may accept encodings that are longer than necessary. According to the RFC 3629, a particularly subtle form of this attack can be carried out against a parser which performs security-critical validity checks against the UTF-8 encoded form of its input, but interprets certain illegal octet sequences as characters.

## Related Attack Patterns
- PeerOf: CAPEC-64
- PeerOf: CAPEC-71
- ChildOf: CAPEC-267

## Prerequisites
- The application's UTF-8 decoder accepts and interprets illegal UTF-8 characters or non-shortest format of UTF-8 encoding.
- Input filtering and validating is not done properly leaving the door open to harmful characters for the target host.

## Skills Required
- [Low] An attacker can inject different representation of a filtered character in UTF-8 format.
- [Medium] An attacker may craft subtle encoding of input data by using the knowledge that they have gathered about the target host.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- The Unicode Consortium recognized multiple representations to be a problem and has revised the Unicode Standard to make multiple representations of the same code point with UTF-8 illegal. The UTF-8 Corrigendum lists the newly restricted UTF-8 range (See references). Many current applications may not have been revised to follow this rule. Verify that your application conform to the latest UTF-8 encoding specification. Pay extra attention to the filtering of illegal characters.
- The exact response required from an UTF-8 decoder on invalid input is not uniformly defined by the standards. In general, there are several ways a UTF-8 decoder might behave in the event of an invalid byte sequence: 1. Insert a replacement character (e.g. '?', ''). 2. Ignore the bytes. 3. Interpret the bytes according to a different character encoding (often the ISO-8859-1 character map). 4. Not notice and decode as if the bytes were some similar bit of UTF-8. 5. Stop decoding and report an error (possibly giving the caller the option to continue). It is possible for a decoder to behave in different ways for different types of invalid input. RFC 3629 only requires that UTF-8 decoders must not decode "overlong sequences" (where a character is encoded in more bytes than needed but still adheres to the forms above). The Unicode Standard requires a Unicode-compliant decoder to "...treat any ill-formed code unit sequence as an error condition. This guarantees that it will neither interpret nor emit an ill-formed code unit sequence." Overlong forms are one of the most troublesome types of UTF-8 data. The current RFC says they must not be decoded but older specifications for UTF-8 only gave a warning and many simpler decoders will happily decode them. Overlong forms have been used to bypass security validations in high profile products including Microsoft's IIS web server. Therefore, great care must be taken to avoid security issues if validation is performed before conversion from UTF-8, and it is generally much simpler to handle overlong forms before any input validation is done. To maintain security in the case of invalid input, there are two options. The first is to decode the UTF-8 before doing any input validation checks. The second is to use a decoder that, in the event of invalid input, returns either an error or text that the application considers to be harmless. Another possibility is to avoid conversion out of UTF-8 altogether but this relies on any other software that the data is passed to safely handling the invalid data. Another consideration is error recovery. To guarantee correct recovery after corrupt or lost bytes, decoders must be able to recognize the difference between lead and trail bytes, rather than just assuming that bytes will be of the type allowed in their position.
- For security reasons, a UTF-8 decoder must not accept UTF-8 sequences that are longer than necessary to encode a character. If you use a parser to decode the UTF-8 encoding, make sure that parser filter the invalid UTF-8 characters (invalid forms or overlong forms).
- Look for overlong UTF-8 sequences starting with malicious pattern. You can also use a UTF-8 decoder stress test to test your UTF-8 parser (See Markus Kuhn's UTF-8 and Unicode FAQ in reference section)
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system. Test your decoding process against malicious input.

## Related Weaknesses (CWE)
- CWE-173
- CWE-172
- CWE-180
- CWE-181
- CWE-73
- CWE-74
- CWE-20
- CWE-697
- CWE-692


---

# CAPEC-81: Web Server Logs Tampering

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/81.html  

## Description
Web Logs Tampering attacks involve an attacker injecting, deleting or otherwise tampering with the contents of web logs typically for the purposes of masking other malicious behavior. Additionally, writing malicious data to log files may target jobs, filters, reports, and other agents that process the logs in an asynchronous attack pattern. This pattern of attack is similar to "Log Injection-Tampering-Forging" except that in this case, the attack is targeting the logs of the web server and not the application.

## Related Attack Patterns
- ChildOf: CAPEC-268

## Prerequisites
- Target server software must be a HTTP server that performs web logging.

## Skills Required
- [Low] To input faked entries into Web logs

## Resources Required
- Ability to send specially formatted HTTP request to web server

## Consequences
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Design: Use input validation before writing to web log
- Design: Validate all log data before it is output

## Related Weaknesses (CWE)
- CWE-117
- CWE-93
- CWE-75
- CWE-221
- CWE-96
- CWE-20
- CWE-150
- CWE-276
- CWE-279
- CWE-116


---

# CAPEC-82: DEPRECATED: Violating Implicit Assumptions Regarding XML Content (aka XML Denial of Service (XDoS))

**Abstraction:** Standard  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/82.html  

## Description
This attack pattern has been deprecated as it a generalization of CAPEC-230: XML Nested Payloads, CAPEC-231: XML Oversized Payloads, and CAPEC-147: XML Ping of Death. Please refer to these CAPECs going forward.


---

# CAPEC-83: XPath Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/83.html  

## Description
An attacker can craft special user-controllable input consisting of XPath expressions to inject the XML database and bypass authentication or glean information that they normally would not be able to. XPath Injection enables an attacker to talk directly to the XML database, thus bypassing the application completely. XPath Injection results from the failure of an application to properly sanitize input used as part of dynamic XPath expressions used to query an XML database.

## Related Attack Patterns
- ChildOf: CAPEC-250

## Prerequisites
- XPath queries used to retrieve information stored in XML documents
- User-controllable input not properly sanitized before being used as part of XPath queries

## Skills Required
- [Low] XPath Injection shares the same basic premises with SQL Injection. An attacker must have knowledge of XPath syntax and constructs in order to successfully leverage XPath Injection

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as content that can be interpreted in the context of an XPath expression. Characters such as a single-quote(') or operators such as or (|), and (&) and such should be filtered if the application does not expect them in the context in which they appear. If such content cannot be filtered, it must at least be properly escaped to avoid them being interpreted as part of XPath expressions.
- Use of parameterized XPath queries - Parameterization causes the input to be restricted to certain domains, such as strings or integers, and any input outside such domains is considered invalid and the query fails.
- Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the database or application.

## Related Weaknesses (CWE)
- CWE-91
- CWE-74
- CWE-20
- CWE-707


---

# CAPEC-84: XQuery Injection

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/84.html  

## Description
This attack utilizes XQuery to probe and attack server systems; in a similar manner that SQL Injection allows an attacker to exploit SQL calls to RDBMS, XQuery Injection uses improperly validated data that is passed to XQuery commands to traverse and execute commands that the XQuery routines have access to. XQuery injection can be used to enumerate elements on the victim's environment, inject commands to the local host, or execute queries to remote files and data sources.

## Related Attack Patterns
- ChildOf: CAPEC-250

## Prerequisites
- The XQL must execute unvalidated data

## Skills Required
- [Low] Basic understanding of XQuery

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Design: Perform input allowlist validation on all XML input
- Implementation: Run xml parsing and query infrastructure with minimal privileges so that an attacker is limited in their ability to probe other system resources from XQL.

## Related Weaknesses (CWE)
- CWE-74
- CWE-707


---

# CAPEC-85: AJAX Footprinting

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/85.html  

## Description
This attack utilizes the frequent client-server roundtrips in Ajax conversation to scan a system. While Ajax does not open up new vulnerabilities per se, it does optimize them from an attacker point of view. A common first step for an attacker is to footprint the target environment to understand what attacks will work. Since footprinting relies on enumeration, the conversational pattern of rapid, multiple requests and responses that are typical in Ajax applications enable an attacker to look for many vulnerabilities, well-known ports, network locations and so on. The knowledge gained through Ajax fingerprinting can be used to support other attacks, such as XSS.

## Related Attack Patterns
- ChildOf: CAPEC-580
- CanPrecede: CAPEC-63

## Prerequisites
- The user must allow JavaScript to execute in their browser

## Skills Required
- [Medium] To land and launch a script on victim's machine with appropriate footprinting logic for enumerating services and vulnerabilities in JavaScript

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Design: Use browser technologies that do not allow client side scripting.
- Implementation: Perform input validation for all remote content.

## Related Weaknesses (CWE)
- CWE-79
- CWE-113
- CWE-348
- CWE-96
- CWE-20
- CWE-116
- CWE-184
- CWE-86
- CWE-692


---

# CAPEC-86: XSS Through HTTP Headers

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/86.html  

## Description
An adversary exploits web applications that generate web content, such as links in a HTML page, based on unvalidated or improperly validated data submitted by other actors. XSS in HTTP Headers attacks target the HTTP headers which are hidden from most users and may not be validated by web applications.

## Related Attack Patterns
- ChildOf: CAPEC-591
- ChildOf: CAPEC-588
- ChildOf: CAPEC-592

## Prerequisites
- Target software must be a client that allows scripting communication from remote hosts.

## Skills Required
- [Low] To achieve a redirection and use of less trusted source, an adversary can simply edit HTTP Headers that are sent to client machine.
- [High] Exploiting a client side vulnerability to inject malicious scripts into the browser's executable process.

## Resources Required
- The adversary must have the ability to deploy a custom hostile service for access by targeted clients and the abbility to communicate synchronously or asynchronously with client machine. The adversary must also control a remote site of some sort to redirect client and data to.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Design: Use browser technologies that do not allow client side scripting.
- Design: Utilize strict type, character, and encoding enforcement
- Design: Server side developers should not proxy content via XHR or other means, if a http proxy for remote content is setup on the server side, the client's browser has no way of discerning where the data is originating from.
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Perform input validation for all remote content.
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser
- Implementation: Session tokens for specific host
- Implementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.

## Related Weaknesses (CWE)
- CWE-80


---

# CAPEC-87: Forceful Browsing

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/87.html  

## Description
An attacker employs forceful browsing (direct URL entry) to access portions of a website that are otherwise unreachable. Usually, a front controller or similar design pattern is employed to protect access to portions of a web application. Forceful browsing enables an attacker to access information, perform privileged operations and otherwise reach sections of the web application that have been improperly protected.

## Related Attack Patterns
- ChildOf: CAPEC-115

## Prerequisites
- The forcibly browseable pages or accessible resources must be discoverable and improperly protected.

## Skills Required
- [Low] Forcibly browseable pages can be discovered by using a number of automated tools. Doing the same manually is tedious but by no means difficult.

## Resources Required
- None: No specialized resources are required to execute this type of attack. A directory listing is helpful, but not a requirement.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Authenticate request to every resource. In addition, every page or resource must ensure that the request it is handling has been made in an authorized context.
- Forceful browsing can also be made difficult to a large extent by not hard-coding names of application pages or resources. This way, the attacker cannot figure out, from the application alone, the resources available from the present context.

## Related Weaknesses (CWE)
- CWE-425
- CWE-285
- CWE-693


---

# CAPEC-88: OS Command Injection

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/88.html  

## Description
In this type of an attack, an adversary injects operating system commands into existing application functions. An application that uses untrusted input to build command strings is vulnerable. An adversary can leverage OS command injection in an application to elevate privileges, execute arbitrary commands and compromise the underlying operating system.

## Related Attack Patterns
- ChildOf: CAPEC-248

## Prerequisites
- User controllable input used as part of commands to the underlying operating system.

## Skills Required
- [High] The attacker needs to have knowledge of not only the application to exploit but also the exact nature of commands that pertain to the target operating system. This may involve, though not always, knowledge of specific assembly commands for the platform.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges, Bypass Protection Mechanism
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Use language APIs rather than relying on passing data to the operating system shell or command line. Doing so ensures that the available protection mechanisms in the language are intact and applicable.
- Filter all incoming data to escape or remove characters or strings that can be potentially misinterpreted as operating system or shell commands
- All application processes should be run with the minimal privileges required. Also, processes must shed privileges as soon as they no longer require them.

## Related Weaknesses (CWE)
- CWE-78
- CWE-88
- CWE-20
- CWE-697


---

# CAPEC-89: Pharming

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/89.html  

## Description
A pharming attack occurs when the victim is fooled into entering sensitive data into supposedly trusted locations, such as an online bank site or a trading platform. An attacker can impersonate these supposedly trusted sites and have the victim be directed to their site rather than the originally intended one. Pharming does not require script injection or clicking on malicious links for the attack to succeed.

## Related Attack Patterns
- ChildOf: CAPEC-151

## Prerequisites
- Vulnerable DNS software or improperly protected hosts file or router that can be poisoned
- A website that handles sensitive information but does not use a secure connection and a certificate that is valid is also prone to pharming

## Skills Required
- [Medium] The attacker needs to be able to poison the resolver - DNS entries or local hosts file or router entry pointing to a trusted DNS server - in order to successfully carry out a pharming attack. Setting up a fake website, identical to the targeted one, does not require special skills.

## Resources Required
- None: No specialized resources are required to execute this type of attack. Having knowledge of the way the target site has been structured, in order to create a fake version, is required. Poisoning the resolver requires knowledge of a vulnerability that can be exploited.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- All sensitive information must be handled over a secure connection.
- Known vulnerabilities in DNS or router software or in operating systems must be patched as soon as a fix has been released and tested.
- End users must ensure that they provide sensitive information only to websites that they trust, over a secure connection with a valid certificate issued by a well-known certificate authority.

## Related Weaknesses (CWE)
- CWE-346
- CWE-350


---

# CAPEC-9: Buffer Overflow in Local Command-Line Utilities

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/9.html  

## Description
This attack targets command-line utilities available in a number of shells. An adversary can leverage a vulnerability found in a command-line utility to escalate privilege to root.

## Related Attack Patterns
- ChildOf: CAPEC-100

## Prerequisites
- The target host exposes a command-line utility to the user.
- The command-line utility exposed by the target host has a buffer overflow vulnerability that can be exploited.

## Skills Required
- [Low] An adversary can simply overflow a buffer by inserting a long string into an adversary-modifiable injection vector. The result can be a DoS.
- [High] Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Carefully review the service's implementation before making it available to user. For instance you can use manual or automated code review to uncover vulnerabilities such as buffer overflow.
- Use a language or compiler that performs automatic bounds checking.
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Operational: Use OS-level preventative functionality. Not a complete solution.
- Apply the latest patches to your user exposed services. This may not be a complete solution, especially against a zero day attack.
- Do not unnecessarily expose services.

## Related Weaknesses (CWE)
- CWE-120
- CWE-118
- CWE-119
- CWE-74
- CWE-20
- CWE-680
- CWE-733
- CWE-697


---

# CAPEC-90: Reflection Attack in Authentication Protocol

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/90.html  

## Description
An adversary can abuse an authentication protocol susceptible to reflection attack in order to defeat it. Doing so allows the adversary illegitimate access to the target system, without possessing the requisite credentials. Reflection attacks are of great concern to authentication protocols that rely on a challenge-handshake or similar mechanism. An adversary can impersonate a legitimate user and can gain illegitimate access to the system by successfully mounting a reflection attack during authentication.

## Related Attack Patterns
- ChildOf: CAPEC-272
- ChildOf: CAPEC-114

## Prerequisites
- The attacker must have direct access to the target server in order to successfully mount a reflection attack. An intermediate entity, such as a router or proxy, that handles these exchanges on behalf of the attacker inhibits the attackers' ability to attack the authentication protocol.

## Skills Required
- [Medium] The attacker needs to have knowledge of observing the protocol exchange and managing the required connections in order to issue and respond to challenges

## Resources Required
- All that the attacker requires is a means to observe and understand the protocol exchanges in order to reflect the challenges appropriately.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges, Bypass Protection Mechanism
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- The server must initiate the handshake by issuing the challenge. This ensures that the client has to respond before the exchange can move any further
- The use of HMAC to hash the response from the server can also be used to thwart reflection. The server responds by returning its own challenge as well as hashing the client's challenge, its own challenge and the pre-shared secret. Requiring the client to respond with the HMAC of the two challenges ensures that only the possessor of a valid pre-shared secret can successfully hash in the two values.
- Introducing a random nonce with each new connection ensures that the attacker cannot employ two connections to attack the authentication protocol

## Related Weaknesses (CWE)
- CWE-301
- CWE-303


---

# CAPEC-91: DEPRECATED: XSS in IMG Tags

**Abstraction:** Detailed  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/91.html  

## Description
This attack pattern has been deprecated as it is contained in the existing attack pattern "CAPEC-18 : XSS Targeting Non-Script Elements". Please refer to this other CAPEC going forward.


---

# CAPEC-92: Forced Integer Overflow

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/92.html  

## Description
This attack forces an integer variable to go out of range. The integer variable is often used as an offset such as size of memory allocation or similarly. The attacker would typically control the value of such variable and try to get it out of range. For instance the integer in question is incremented past the maximum possible value, it may wrap to become a very small, or negative number, therefore providing a very incorrect value which can lead to unexpected behavior. At worst the attacker can execute arbitrary code.

## Related Attack Patterns
- ChildOf: CAPEC-128

## Prerequisites
- The attacker can manipulate the value of an integer variable utilized by the target host.
- The target host does not do proper range checking on the variable before utilizing it.
- When the integer variable is incremented or decremented to an out of range value, it gets a very different value (e.g. very small or negative number)

## Skills Required
- [Low] An attacker can simply overflow an integer by inserting an out of range value.
- [High] Exploiting a buffer overflow by injecting malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Use a language or compiler that performs automatic bounds checking.
- Carefully review the service's implementation before making it available to user. For instance you can use manual or automated code review to uncover vulnerabilities such as integer overflow.
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Always do bound checking before consuming user input data.

## Related Weaknesses (CWE)
- CWE-190
- CWE-128
- CWE-120
- CWE-122
- CWE-196
- CWE-680
- CWE-697


---

# CAPEC-93: Log Injection-Tampering-Forging

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/93.html  

## Description
This attack targets the log files of the target host. The attacker injects, manipulates or forges malicious log entries in the log file, allowing them to mislead a log audit, cover traces of attack, or perform other malicious actions. The target host is not properly controlling log access. As a result tainted data is resulting in the log files leading to a failure in accountability, non-repudiation and incident forensics capability.

## Related Attack Patterns
- ChildOf: CAPEC-268
- CanPrecede: CAPEC-592

## Prerequisites
- The target host is logging the action and data of the user.
- The target host insufficiently protects access to the logs or logging mechanisms.

## Skills Required
- [Low] This attack can be as simple as adding extra characters to the logged data (e.g. username). Adding entries is typically easier than removing entries.
- [Medium] A more sophisticated attack can try to defeat the input validation mechanism.

## Consequences
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Carefully control access to physical log files.
- Do not allow tainted data to be written in the log file without prior input validation. An allowlist may be used to properly validate the data.
- Use synchronization to control the flow of execution.
- Use static analysis tools to identify log forging vulnerabilities.
- Avoid viewing logs with tools that may interpret control characters in the file, such as command-line shells.

## Related Weaknesses (CWE)
- CWE-117
- CWE-75
- CWE-150


---

# CAPEC-94: Adversary in the Middle (AiTM)

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/94.html  

## Description
An adversary targets the communication between two components (typically client and server), in order to alter or obtain data from transactions. A general approach entails the adversary placing themself within the communication channel between the two components.

## Related Attack Patterns
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-668

## Prerequisites
- There are two components communicating with each other.
- An attacker is able to identify the nature and mechanism of communication between the two target components.
- An attacker can eavesdrop on the communication between the target components.
- Strong mutual authentication is not used between the two target components yielding opportunity for attacker interposition.
- The communication occurs in clear (not encrypted) or with insufficient and spoofable encryption.

## Skills Required
- [Medium] This attack can get sophisticated since the attack may use cryptography.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Ensure Public Keys are signed by a Certificate Authority
- Encrypt communications using cryptography (e.g., SSL/TLS)
- Use Strong mutual authentication to always fully authenticate both ends of any communications channel.
- Exchange public keys using a secure channel

## Related Weaknesses (CWE)
- CWE-300
- CWE-290
- CWE-593
- CWE-287
- CWE-294


---

# CAPEC-95: WSDL Scanning

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/95.html  

## Description
This attack targets the WSDL interface made available by a web service. The attacker may scan the WSDL interface to reveal sensitive information about invocation patterns, underlying technology implementations and associated vulnerabilities. This type of probing is carried out to perform more serious attacks (e.g. parameter tampering, malicious content injection, command injection, etc.). WSDL files provide detailed information about the services ports and bindings available to consumers. For instance, the attacker can submit special characters or malicious content to the Web service and can cause a denial of service condition or illegal access to database records. In addition, the attacker may try to guess other private methods by using the information provided in the WSDL files.

## Related Attack Patterns
- ChildOf: CAPEC-54

## Prerequisites
- A client program connecting to a web service can read the WSDL to determine what functions are available on the server.
- The target host exposes vulnerable functions within its WSDL interface.

## Skills Required
- [Low] This attack can be as simple as reading WSDL and starting sending invalid request.
- [Medium] This attack can be used to perform more sophisticated attacks (SQL injection, etc.)

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- It is important to protect WSDL file or provide limited access to it.
- Review the functions exposed by the WSDL interface (especially if you have used a tool to generate it). Make sure that none of them is vulnerable to injection.
- Ensure the WSDL does not expose functions and APIs that were not intended to be exposed.
- Pay attention to the function naming convention (within the WSDL interface). Easy to guess function name may be an entry point for attack.
- Validate the received messages against the WSDL Schema. Incomplete solution.

## Related Weaknesses (CWE)
- CWE-538


---

# CAPEC-96: Block Access to Libraries

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/96.html  

## Description
An application typically makes calls to functions that are a part of libraries external to the application. These libraries may be part of the operating system or they may be third party libraries. It is possible that the application does not handle situations properly where access to these libraries has been blocked. Depending on the error handling within the application, blocked access to libraries may leave the system in an insecure state that could be leveraged by an attacker.

## Related Attack Patterns
- ChildOf: CAPEC-603

## Prerequisites
- An application requires access to external libraries.
- An attacker has the privileges to block application access to external libraries.

## Skills Required
- [Low] Knowledge of how to block access to libraries, as well as knowledge of how to leverage the resulting state of the application based on the failed call.

## Consequences
- Scope: Availability; Impact: Alter Execution Logic
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism

## Mitigations
- Ensure that application handles situations where access to APIs in external libraries is not available securely. If the application cannot continue its execution safely it should fail in a consistent and secure fashion.

## Related Weaknesses (CWE)
- CWE-589


---

# CAPEC-97: Cryptanalysis

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/97.html  

## Description
Cryptanalysis is a process of finding weaknesses in cryptographic algorithms and using these weaknesses to decipher the ciphertext without knowing the secret key (instance deduction). Sometimes the weakness is not in the cryptographic algorithm itself, but rather in how it is applied that makes cryptanalysis successful. An attacker may have other goals as well, such as: Total Break (finding the secret key), Global Deduction (finding a functionally equivalent algorithm for encryption and decryption that does not require knowledge of the secret key), Information Deduction (gaining some information about plaintexts or ciphertexts that was not previously known) and Distinguishing Algorithm (the attacker has the ability to distinguish the output of the encryption (ciphertext) from a random permutation of bits).

## Related Attack Patterns
- ChildOf: CAPEC-192
- CanPrecede: CAPEC-20

## Prerequisites
- The target software utilizes some sort of cryptographic algorithm.
- An underlying weaknesses exists either in the cryptographic algorithm used or in the way that it was applied to a particular chunk of plaintext.
- The encryption algorithm is known to the attacker.
- An attacker has access to the ciphertext.

## Skills Required
- [High] Cryptanalysis generally requires a very significant level of understanding of mathematics and computation.

## Resources Required
- Computing resource requirements will vary based on the complexity of a given cryptanalysis technique. Access to the encryption/decryption routines of the algorithm is also required.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Use proven cryptographic algorithms with recommended key sizes.
- Ensure that the algorithms are used properly. That means: 1. Not rolling out your own crypto; Use proven algorithms and implementations. 2. Choosing initialization vectors with sufficiently random numbers 3. Generating key material using good sources of randomness and avoiding known weak keys 4. Using proven protocols and their implementations. 5. Picking the most appropriate cryptographic algorithm for your usage context and data

## Related Weaknesses (CWE)
- CWE-327
- CWE-1204
- CWE-1240
- CWE-1241
- CWE-1279


---

# CAPEC-98: Phishing

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/98.html  

## Description
Phishing is a social engineering technique where an attacker masquerades as a legitimate entity with which the victim might do business in order to prompt the user to reveal some confidential information (very frequently authentication credentials) that can later be used by an attacker. Phishing is essentially a form of information gathering or "fishing" for information.

## Related Attack Patterns
- ChildOf: CAPEC-151
- CanPrecede: CAPEC-89
- CanPrecede: CAPEC-543
- CanPrecede: CAPEC-611
- CanPrecede: CAPEC-630
- CanPrecede: CAPEC-631
- CanPrecede: CAPEC-632

## Prerequisites
- An attacker needs to have a way to initiate contact with the victim. Typically that will happen through e-mail.
- An attacker needs to correctly guess the entity with which the victim does business and impersonate it. Most of the time phishers just use the most popular banks/services and send out their "hooks" to many potential victims.
- An attacker needs to have a sufficiently compelling call to action to prompt the user to take action.
- The replicated website needs to look extremely similar to the original website and the URL used to get to that website needs to look like the real URL of the said business entity.

## Skills Required
- [Medium] Basic knowledge about websites: obtaining them, designing and implementing them, etc.

## Resources Required
- Some web development tools to put up a fake website.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Do not follow any links that you receive within your e-mails and certainly do not input any login credentials on the page that they take you too. Instead, call your Bank, PayPal, eBay, etc., and inquire about the problem. A safe practice would also be to type the URL of your bank in the browser directly and only then log in. Also, never reply to any e-mails that ask you to provide sensitive information of any kind.

## Related Weaknesses (CWE)
- CWE-451


---

# CAPEC-99: DEPRECATED: XML Parser Attack

**Abstraction:** Standard  
**Status:** Deprecated  
**Reference:** https://capec.mitre.org/data/definitions/99.html  

## Description
This attack pattern has been deprecated as it a generalization of CAPEC-230: XML Nested Payloads and CAPEC-231: XML Oversized Payloads. Please refer to these CAPECs going forward.
