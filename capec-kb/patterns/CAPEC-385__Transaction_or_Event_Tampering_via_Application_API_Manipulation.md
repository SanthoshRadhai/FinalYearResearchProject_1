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
