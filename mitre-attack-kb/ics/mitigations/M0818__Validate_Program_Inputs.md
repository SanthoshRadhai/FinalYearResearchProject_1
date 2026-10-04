# M0818: Validate Program Inputs

**Type:** course-of-action  
**Reference:** https://attack.mitre.org/mitigations/M0818  

## Description
Devices and programs designed to interact with control system parameters should validate the format and content of all user inputs and actions to ensure the values are within intended operational ranges. These values should be evaluated and further enforced through the program logic running on the field controller. If a problematic or invalid input is identified, the programs should either utilize a predetermined safe value or enter a known safe state, while also logging or alerting on the event.(Citation: PLCTop20 Mar 2023)

## Techniques Mitigated
- T0836: Modify Parameter
- T1692.001: Command Message
