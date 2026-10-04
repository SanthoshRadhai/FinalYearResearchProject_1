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
