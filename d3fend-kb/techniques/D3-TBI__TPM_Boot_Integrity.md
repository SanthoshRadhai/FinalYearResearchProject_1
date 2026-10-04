# D3-TBI: TPM Boot Integrity

**Synonym(s):** STRM, Static Root of Trust Measurement  
**Reference:** https://d3fend.mitre.org/technique/D3-TBI/  

## Definition
Assuring the integrity of a platform by demonstrating that the boot process starts from a trusted combination of hardware and software and continues until the operating system has fully booted and applications are running.  Sometimes called Static Root of Trust Measurement (STRM).

## Parent Class(es)
- Platform Hardening

## Relationships
- **kb-reference:** Reference - TCG Trusted Attestation Protocol Use Cases for TPM Families 1.2 and 2.0 and DICE
- **kb-reference:** Reference - TPM 2.0 Library Specification - Trusted Computing Group, Incorporated
- **kb-reference:** Reference - Trusted Attestation Protocol Use Cases

## Knowledge Base Article
## How it works
During the boot process, the BIOS boot block (which with this defense enabled, is the Core Root of Trust for Measurement) measures boot components (firmware, ROM). The TPM hashes those measurements and stores the hashes in Platform Configuration Registers (PCRs).  Upon a subsequent boot, these hashes are provided to a verifier which compares the stored measurements to the new boot measurements. Integrity of the boot components is assured if they match.

Attestation of the secure boot occurs when a verifying entity requests a Quote which is a concatenation of the requested PCR values, hashed and signed by the TPM's unique RSA key.  The TPM signature is trusted because the private key is stored securely in hardware and never leaves the TPM.

## Considerations

* The TPM does not perform the follow-on actions of acting on the PCR value information, it just provides the PCR stored information.
* The current version of TPM is 2.0.; most existing implementations use TPM 1.2.

## Citations
[1] [TPM 2.0 Library](https://trustedcomputinggroup.org/resource/tpm-library-specification/)
[2] [TCG Trusted Attestation Protocol (TAP) Use Cases for TPM Families 1.2 and 2.0 and DICE](https://trustedcomputinggroup.org/wp-content/uploads/TCG_TNC_TAP_Use_Cases_v1r0p35_published.pdf)
