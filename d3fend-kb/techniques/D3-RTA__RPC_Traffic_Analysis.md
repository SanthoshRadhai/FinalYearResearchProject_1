# D3-RTA: RPC Traffic Analysis

**Synonym(s):** RPC Protocol Analysis  
**Reference:** https://d3fend.mitre.org/technique/D3-RTA/  

## Definition
Monitoring the activity of remote procedure calls in communication traffic to establish standard protocol operations and potential attacker activities.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** RPC Network Traffic
- **kb-reference:** Reference - CAR-2014-05-001: RPC Activity - MITRE
- **kb-reference:** Reference - CAR-2014-11-007: Remote Windows Management Instrumentation (WMI) over RPC - MITRE
- **kb-reference:** Reference - CAR-2016-03-002: Create Remote Process via WMIC - MITRE
- **kb-reference:** Reference - RPC call interception - Crowdstrike Inc
- **kb-reference:** Reference - CAR-2014-03-005: Remotely Launched Executables via Services - MITRE
- **kb-reference:** Reference - CAR-2014-12-001: Remotely Launched Executables via WMI - MITRE
- **kb-reference:** Reference - CAR-2015-04-002: Remotely Scheduled Tasks via Schtasks - MITRE
- **kb-reference:** Reference - CAR-2014-03-001: SMB Write Request - NamedPipes - MITRE

## Knowledge Base Article
## How it works
A remote procedure call (RPC) enables one computer to execute a specific function on another computer, as if it were a local application process. There are numerous RPC specifications and implementations. RPC capabilities can be abused by attackers in order to achieve a variety of tactical objectives including execution, persistence, initial access, and more. RPC proxies may be used to collect and store RPC traffic. RPCs can occur over network sockets or named pipes.

Analytics look for unauthorized behavior such as:

* Processes being launched or scheduled remotely
* System configurations being changed remotely
* Unauthorized file read activity

Example RPC Protocols:

* DCE/RPC
* CORBA
* Open Network Computing Remote Procedure Call
* D-Bus
* XML-RPC
* JSON-RPC
* SOAP
* Apache Thrift

## Considerations
* RPC is widely used in enterprise environments, and significant data filtering may be required in large environments to enable analytic processing.
* RPC traffic may occur over a pipe, or within a host over loopback interface, thus making network collection difficult.
