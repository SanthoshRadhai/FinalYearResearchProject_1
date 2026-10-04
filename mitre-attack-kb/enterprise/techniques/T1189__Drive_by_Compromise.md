# T1189: Drive-by Compromise


**ATT&CK ID:** T1189  
**Domain:** Mitre Attack  
**Tactic(s):** Initial Access  
**Platforms:** Identity Provider, Linux, macOS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1189  

## Description
Adversaries may gain access to a system through a user visiting a website over the normal course of browsing. Multiple ways of delivering exploit code to a browser exist (i.e., [Drive-by Target](https://attack.mitre.org/techniques/T1608/004)), including:

* A legitimate website is compromised, allowing adversaries to inject malicious code
* Script files served to a legitimate website from a publicly writeable cloud storage bucket are modified by an adversary
* Malicious ads are paid for and served through legitimate ad providers (i.e., [Malvertising](https://attack.mitre.org/techniques/T1583/008))
* Built-in web application interfaces that allow user-controllable content are leveraged for the insertion of malicious scripts or iFrames (e.g., cross-site scripting)

Browser push notifications may also be abused by adversaries and leveraged for malicious code injection via [User Execution](https://attack.mitre.org/techniques/T1204). By clicking "allow" on browser push notifications, users may be granting a website permission to run JavaScript code on their browser.(Citation: Push notifications - viruspositive)(Citation: push notification -mcafee)(Citation: push notifications - malwarebytes)

Often the website used by an adversary is one visited by a specific community, such as government, a particular industry, or a particular region, where the goal is to compromise a specific user or set of users based on a shared interest. This kind of targeted campaign is often referred to a strategic web compromise or watering hole attack. There are several known examples of this occurring.(Citation: Shadowserver Strategic Web Compromise)

Typical drive-by compromise process:

1. A user visits a website that is used to host the adversary controlled content.
2. Scripts automatically execute, typically searching versions of the browser and plugins for a potentially vulnerable version. The user may be required to assist in this process by enabling scripting, notifications, or active website components and ignoring warning dialog boxes.
3. Upon finding a vulnerable version, exploit code is delivered to the browser.
4. If exploitation is successful, the adversary will gain code execution on the user's system unless other protections are in place. In some cases, a second visit to the website after the initial scan is required before exploit code is delivered.

Unlike [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190), the focus of this technique is to exploit software on a client endpoint upon visiting a website. This will commonly give an adversary access to systems on the internal network instead of external systems that may be in a DMZ.

## Mitigations
- M1017: User Training
- M1021: Restrict Web-Based Content
- M1048: Application Isolation and Sandboxing
- M1050: Exploit Protection
- M1051: Update Software

## Known Threat Groups Using This Technique
- G0073: APT19
- G0007: APT28
- G0050: APT32
- G0067: APT37
- G0082: APT38
- G0138: Andariel
- G0001: Axiom
- G0060: BRONZE BUTLER
- G1012: CURIUM
- G1034: Daggerfly
- G0070: Dark Caracal
- G0012: Darkhotel
- G0035: Dragonfly
- G1006: Earth Lusca
- G0066: Elderwood
- G0032: Lazarus Group
- G0077: Leafminer
- G0065: Leviathan
- G0095: Machete
- G0059: Magic Hound
- G1020: Mustard Tempest
- G0068: PLATINUM
- G0056: PROMETHIUM
- G0040: Patchwork
- G0048: RTM
- G0027: Threat Group-3390
- G0134: Transparent Tribe
- G0010: Turla
- G0124: Windigo
- G0112: Windshift
- G1035: Winter Vivern

## Known Software Using This Technique
- S0606: Bad Rabbit
- S0482: Bundlore
- S0531: Grandoreiro
- S0483: IcedID
- S0215: KARAE
- S0451: LoudMiner
- S0216: POORAIM
- S0496: REvil
- S1086: Snip3
- S1124: SocGholish
