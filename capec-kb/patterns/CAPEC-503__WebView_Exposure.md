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
