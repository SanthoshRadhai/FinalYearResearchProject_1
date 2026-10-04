# D3-IOPR: IO Port Restriction

**Reference:** https://d3fend.mitre.org/technique/D3-IOPR/  

## Definition
Limiting access to computer input/output (IO) ports to restrict unauthorized devices.

## Parent Class(es)
- Access Mediation

## Relationships
- **filters:** Input Device
- **filters:** Removable Media Device
- **isolates:** I/O Module
- **kb-reference:** Reference - Computer motherboard having peripheral security functions
- **kb-reference:** Reference - Method and system for controlling communication ports
- **kb-reference:** Reference - USB filter for hub malicious code prevention system

## Knowledge Base Article
## How It works

Software-based restriction uses agent software installed on a computer system. The agent software monitors all IO port system traffic. The agent software is configurable to limit the use of certain devices connected to IO ports. The restriction software can also be configured to limit the access to files and applications on external storage devices connected to IO ports.

Hardware-based restriction can also be employed to limit access to IO ports. For example, a hardware USB filter device that is placed between the host system and the external devices can filter IO port connections based on configurable rules. When new devices are connected to the USB filter the type of device is determined. Using an allow list a connection determination is made for the device.

Some implementations detect when a device is connected in order to authorize the connection against a list of approved devices, in some cases by device type. For example, if the device is determined to be a storage device, then the contained files and executables are examined to more accurately identify the device type.

Types of restrictions that may be applied:
- Device connection
- Device command filtering
- Device file system read or write restrictions

## Considerations
 * Agent software will need to be installed on host systems
 * Configurations for allow/deny for devices and files will need to be maintained
