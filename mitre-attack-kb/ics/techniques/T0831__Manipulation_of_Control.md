# T0831: Manipulation of Control


**ATT&CK ID:** T0831  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Impact  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0831  

## Description
Adversaries may manipulate physical process control within the industrial environment. Methods of manipulating control can include changes to set point values, tags, or other parameters. Adversaries may manipulate control systems devices or possibly leverage their own, to communicate with and command physical control processes. The duration of manipulation may be temporary or longer sustained, depending on operator detection.   

Methods of Manipulation of Control include: 

* Man-in-the-middle  
* Spoof command message 
* Changing setpoints  

A Polish student used a remote controller device to interface with the Lodz city tram system in Poland. (Citation: John Bill May 2017) (Citation: Shelley Smith February 2008) (Citation: Bruce Schneier January 2008) Using this remote, the student was able to capture and replay legitimate tram signals. As a consequence, four trams were derailed and twelve people injured due to resulting emergency stops. (Citation: Shelley Smith February 2008) The track controlling commands issued may have also resulted in tram collisions, a further risk to those on board and nearby the areas of impact. (Citation: Bruce Schneier January 2008)

## Mitigations
- M0802: Communication Authenticity
- M0810: Out-of-Band Communications Channel
- M0953: Data Backup

## Known Software Using This Technique
- S0604: Industroyer
- S0603: Stuxnet
