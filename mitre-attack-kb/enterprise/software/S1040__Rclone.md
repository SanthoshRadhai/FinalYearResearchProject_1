# S1040: Rclone

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S1040  
**Aliases:** Rclone  
**Platforms:** Linux, Windows, macOS  

## Description
[Rclone](https://attack.mitre.org/software/S1040) is a command line program for syncing files with cloud storage services such as Dropbox, Google Drive, Amazon S3, and MEGA. [Rclone](https://attack.mitre.org/software/S1040) has been used in a number of ransomware campaigns, including those associated with the [Conti](https://attack.mitre.org/software/S0575) and DarkSide Ransomware-as-a-Service operations.(Citation: Rclone)(Citation: Rclone Wars)(Citation: Detecting Rclone)(Citation: DarkSide Ransomware Gang)(Citation: DFIR Conti Bazar Nov 2021)

## Techniques Used
- T1030: Data Transfer Size Limits
- T1048.002: Exfiltration Over Asymmetric Encrypted Non-C2 Protocol
- T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol
- T1083: File and Directory Discovery
- T1560.001: Archive via Utility
- T1567.002: Exfiltration to Cloud Storage
