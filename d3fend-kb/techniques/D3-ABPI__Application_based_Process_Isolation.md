# D3-ABPI: Application-based Process Isolation

**Synonym(s):** Browser-based Process Isolation, Remote Browser Isolation, Sandbox  
**Reference:** https://d3fend.mitre.org/technique/D3-ABPI/  

## Definition
Application code which prevents its own subroutines from accessing intra-process / internal memory space.

## Parent Class(es)
- Execution Isolation

## Relationships
- **isolates:** Process
- **kb-reference:** Reference - Private application access with browser isolation
- **kb-reference:** Reference - Protecting web applications from untrusted endpoints using remote browser isolation
- **kb-reference:** Reference - Site Isolation Design Document
- **restricts:** Subroutine

## Knowledge Base Article
## How it works
Some applications implement logic to permit or deny a particular subroutine access to other data within the same application process. This is intended to prevent critical application process data from being tampered with.

### Application-based Process Isolation in web browsers.

Isolation in browsers usually is designed with the following architectural mindset:
* Sandboxes and web resources should not be allowed to access each other because compromise of one should not effect the other.
* The principle of least-privilege should be followed when browsing.
The following aspects help make browser-based process isolation possible:
* Same Origin Policy
* Separate tabs and iframes use their own DOMs (cross-site document object models always run as a different process)
* CORS ensures cross-site data is not delivered to a process unless the server allows it
* Cookie and local data storage is separated by domain/site
* Separate execution environments (threads)

## Considerations
- Using isolation in browsers does mitigate and protect by default some types of attacks (e.g. renderer attacks and access to the filesystem) but it depends on correct configuration of CORS, use of valid/appropriate certificates.
-  Application-based Process Isolation may increase memory footprint.
-  Application-based Process Isolation may decrease application performance.
