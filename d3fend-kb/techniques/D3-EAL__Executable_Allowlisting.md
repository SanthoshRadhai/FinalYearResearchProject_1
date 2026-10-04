# D3-EAL: Executable Allowlisting

**Synonym(s):** File Signature Authentication  
**Reference:** https://d3fend.mitre.org/technique/D3-EAL/  

## Definition
Using a digital signature to authenticate a file before opening.

## Parent Class(es)
- Execution Isolation

## Relationships
- **blocks:** Executable File
- **filters:** Create Process
- **kb-reference:** Reference - Computing apparatus with automatic integrity reference generation and maintenance - Tripwire, Inc.
- **kb-reference:** Reference - Enhancing Network Security By Preventing User-Initiated Malware Execution - MITRE

## Knowledge Base Article
## How it works

This technique is generic and there are numerous ways to compute and authenticate digital signatures.
A digital certificate is generated from a private/public key pair issued by a certificate authority (CA). A hash of the file is encrypted using the private key. When the file is downloaded by another user, the user's system uses the public key to decrypt the hash and a new hash is created of the downloaded file. The hash decrypted by the public key is compared to the new hash and if there is a mismatch, further techniques, such as file deletion, file quarantine, or **Executable Blacklisting** may be invoked.

This technique may be invoked when deciding whether to load or execute a file.

## Considerations

Organizations which download or create high volumes of software make management complex, in particular engineering or scientific organizations.
