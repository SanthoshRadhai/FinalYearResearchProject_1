# M0800: Authorization Enforcement

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0800  

## Description
The device or system should restrict read, manipulate, or execute privileges to only authenticated users who require access based on approved security policies.  Role-based Access Control (RBAC) schemes can help reduce the overhead of assigning permissions to the large number of devices within an ICS. For example, IEC 62351 provides examples of roles used to support common system operations within the electric power sector  (Citation: International Electrotechnical Commission July 2020), while IEEE 1686 defines standard permissions for users of IEDs. (Citation: Institute of Electrical and Electronics Engineers January 2014)

## Techniques Mitigated
- T0800: Activate Firmware Update Mode
- T0816: Device Restart/Shutdown
- T0821: Modify Controller Tasking
- T0836: Modify Parameter
- T0838: Modify Alarm Settings
- T0843: Program Download
- T0843.001: Download All
- T0843.002: Online Edit
- T0843.003: Program Append
- T0845: Program Upload
- T0858: Change Operating Mode
- T0861: Point & Tag Identification
- T0868: Detect Operating Mode
- T0871: Execution through API
- T0886: Remote Services
- T0889: Modify Program
