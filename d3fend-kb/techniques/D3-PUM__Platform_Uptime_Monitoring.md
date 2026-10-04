# D3-PUM: Platform Uptime Monitoring

**Reference:** https://d3fend.mitre.org/technique/D3-PUM/  

## Definition
Monitor the amount of time since the last power cycle or restart.

## Parent Class(es)
- Platform Monitoring

## Relationships
- **kb-reference:** Reference - Secure PLC Coding Practices: Top 20 List
- **monitors:** Platform Uptime

## Knowledge Base Article
## How it works
Monitoring the time since the last power cycle or restart alerts operators to unexpected restarts and their frequency. This can indicate potential issues or malicious activity, and provides valuable information for forensic investigations.

## Considerations
The source of the variable may be mutable depending on the platform, and the provenance of the value.
