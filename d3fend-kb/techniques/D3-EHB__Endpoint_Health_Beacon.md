# D3-EHB: Endpoint Health Beacon

**Synonym(s):** Endpoint Health Telemetry  
**Reference:** https://d3fend.mitre.org/technique/D3-EHB/  

## Definition
Monitoring the security status of an endpoint by sending periodic messages with health status, where absence of a response may indicate that the endpoint has been compromised.

## Parent Class(es)
- Operating System Monitoring

## Relationships
- **kb-reference:** Reference - Intrusion detection using a heartbeat - Sophos Ltd
- **monitors:** Network Node

## Knowledge Base Article
## How it works
Endpoints are configured to periodically generate and transmit a secure heartbeat that is delivered on a configured schedule and provides endpoint status information. Status information can include software details (version, configuration, etc), endpoint identification (MAC, IP address, machine ID) or other hardware/software configuration information. Interruption of the heartbeat can signal that the endpoint has been compromised.

## Considerations
* Security of heartbeat messages to ensure message integrity
* Disappearance of the heartbeat could simply mean that the endpoint is powered off or intentionally disconnected from the network. Therefore other criteria may need to be used to accurately detect endpoint compromise.
* Attacker presence on the machine may leave the heartbeat intact.
* An attacker may determine the format of the heartbeat and continue to send it even after the machine is compromised.
