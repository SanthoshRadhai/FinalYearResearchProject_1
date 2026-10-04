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
