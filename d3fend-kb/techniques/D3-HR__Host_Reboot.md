# D3-HR: Host Reboot

**Reference:** https://d3fend.mitre.org/technique/D3-HR/  

## Definition
Initiating a host's reboot sequence to terminate all running processes.

## Parent Class(es)
- Host Shutdown

## Relationships
- **kb-reference:** Reference - Near-Memory & In-Memory Detection of Fileless Malware
- **terminates:** Process

## Knowledge Base Article
## How It Works

Host reboot can either be initiated in the physical presence of the device using the power functions or remotely using the provided user interface or an installed EDR agent (with the available function). This process may allow for the removal of specific types of malware, such as fileless malware, and can also prevent further damage, for example, if the system is part of a botnet.

## Considerations

- If the attacker has achieved persistence techniques, this technique may not be effective
- Compromised systems may not respond to remote commands to shutdown or reboot, requiring physical intervention.
- Shutting down a system will usually result in the memory losing its state which can be useful in forensic activities so this should be considered when deciding to shutdown.
- Shutting down or rebooting systems may disrupt access to computer resources for legitimate users.
