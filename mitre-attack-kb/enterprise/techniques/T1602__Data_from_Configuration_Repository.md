# T1602: Data from Configuration Repository


**ATT&CK ID:** T1602  
**Domain:** Mitre Attack  
**Tactic(s):** Collection  
**Platforms:** Network Devices  
**Reference:** https://attack.mitre.org/techniques/T1602  

## Description
Adversaries may collect data related to managed devices from configuration repositories. Configuration repositories are used by management systems in order to configure, manage, and control data on remote systems. Configuration repositories may also facilitate remote access and administration of devices.

Adversaries may target these repositories in order to collect large quantities of sensitive system administration data. Data from configuration repositories may be exposed by various protocols and software and can store a wide variety of data, much of which may align with adversary Discovery objectives.(Citation: US-CERT-TA18-106A)(Citation: US-CERT TA17-156A SNMP Abuse 2017)

## Sub-techniques
- T1602.001: SNMP (MIB Dump)
- T1602.002: Network Device Configuration Dump

## Mitigations
- M1030: Network Segmentation
- M1031: Network Intrusion Prevention
- M1037: Filter Network Traffic
- M1041: Encrypt Sensitive Information
- M1051: Update Software
- M1054: Software Configuration
