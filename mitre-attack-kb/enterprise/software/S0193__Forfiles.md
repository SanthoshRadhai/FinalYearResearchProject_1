# S0193: Forfiles

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S0193  

## Description
[Forfiles](https://attack.mitre.org/software/S0193) is a Windows utility commonly used in batch jobs to execute commands on one or more selected files or directories (ex: list all directories in a drive, read the first line of all files created yesterday, etc.). Forfiles can be executed from either the command line, Run window, or batch files/scripts. (Citation: Microsoft Forfiles Aug 2016)

## Techniques Used
- T1005: Data from Local System
- T1083: File and Directory Discovery
- T1202: Indirect Command Execution
