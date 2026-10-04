# S1167: AcidPour

**Type:** malware  
**Reference:** https://attack.mitre.org/software/S1167  
**Aliases:** AcidPour  
**Platforms:** Linux  

## Description
[AcidPour](https://attack.mitre.org/software/S1167) is a variant of [AcidRain](https://attack.mitre.org/software/S1125) designed to impact a wider range of x86 architecture Linux devices. [AcidPour](https://attack.mitre.org/software/S1167) is an x86 ELF binary that expands on the targeted devices and locations in [AcidRain](https://attack.mitre.org/software/S1125) by including items such as Unsorted Block Image (UBI), Deice Mapper (DM), and various flash memory references. Based on this expanded targeting, [AcidPour](https://attack.mitre.org/software/S1167) can impact a variety of device types including IoT, networking, and ICS embedded device types.(Citation: SentinelOne AcidPour 2024) [AcidPour](https://attack.mitre.org/software/S1167) is a wiping payload associated with the [Sandworm Team](https://attack.mitre.org/groups/G0034) threat actor, and potentially linked to attacks against Ukrainian internet service providers (ISPs) in 2023.(Citation: CERT-UA TelecomAttack 2023)

## Techniques Used
- T1070.004: File Deletion
- T1082: System Information Discovery
- T1083: File and Directory Discovery
- T1120: Peripheral Device Discovery
- T1485: Data Destruction
- T1529: System Shutdown/Reboot
- T1561.001: Disk Content Wipe
