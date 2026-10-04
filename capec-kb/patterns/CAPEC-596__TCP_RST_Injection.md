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
