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
