# D3-DRA: Disable Remote Access

**Reference:** https://d3fend.mitre.org/technique/D3-DRA/  

## Definition
Limiting access to a computing device which is not required through or from a non-organization-controlled network.

## Parent Class(es)
- Application Configuration Hardening

## Relationships
- **configures:** Application Configuration

## Knowledge Base Article
## How It Works
There are several different methods of achieving remote access restriction. This could include: time-based controls, just-in-time authorization, and deny-by-default controls.

This can be done on a Windows machine by unchecking an "allow remote assistance" or checking the "don't allow remote connections" boxes; creating firewall rules to block remote access protocols; uninstalling remote access software; disabling Wi-Fi, Ethernet, Bluetooth, or other connection methods enabling remote access.

One way to achieve remote access restrictions in OT is by programming logic in the OT Controller to give the Operator authorizing abilities which ensures local control is maintained. In this situation, a remote access modem would be powered on/off using a discrete output from an I/O module of the OT controller.
