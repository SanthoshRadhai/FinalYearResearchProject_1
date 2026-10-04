# T1695: Block Communications


**ATT&CK ID:** T1695  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Reference:** https://attack.mitre.org/techniques/T1695  

## Description
Operational technology communications occur over serial COM, Ethernet, Wi-Fi, cellular (4G/5G), and satellite mediums. Adversaries may block communications to prevent reporting messages and command messages from reaching their intended target devices disrupting processes, operations, and causing cyber-physical impacts.(Citation: Bonnie Zhu, Anthony Joseph, Shankar Sastry 2011)  

Adversaries may block communications by either making modifications to software ([System Firmware](https://attack.mitre.org/techniques/T0857), [Module Firmware](https://attack.mitre.org/techniques/T0839), [Hooking](https://attack.mitre.org/techniques/T0874), and [Rootkit](https://attack.mitre.org/techniques/T0851)) and services ([Service Stop](https://attack.mitre.org/techniques/T0881), [Denial of Service](https://attack.mitre.org/techniques/T0814)) on systems and devices or by positioning themselves between systems and devices and intercepting and blocking the communications such as the case with an [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T0830) attack.

## Sub-techniques
- T1695.001: Serial COM
- T1695.002: Ethernet
- T1695.003: Wi-Fi

## Mitigations
- M0807: Network Allowlists
- M0810: Out-of-Band Communications Channel
- M0930: Network Segmentation
