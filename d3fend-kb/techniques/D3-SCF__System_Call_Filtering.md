# D3-SCF: System Call Filtering

**Synonym(s):** System Call Control  
**Reference:** https://d3fend.mitre.org/technique/D3-SCF/  

## Definition
Controlling access to local computer system resources with kernel-level capabilities.

## Parent Class(es)
- Access Mediation

## Relationships
- **filters:** System Call
- **isolates:** Process
- **kb-reference:** Reference - Analysis of the Windows Vista Security Model - Symantec Corporation
- **kb-reference:** Reference - Architecture of transparent network security for application containers - Neuvector Inc
- **kb-reference:** Reference - Overview of the seccomp sandbox

## Knowledge Base Article
## How it works
System call filtering uses a mandatory access control paradigm (that is, a non-discretionary access control) system because the rules and polices that determine access is determined by a security control authority and not distributed to local users. Access determinations are based on designed access control polices and are not based on local resource owner determinations.

Access is typically granted by defining sets of subjects and sets of objects. Subjects are the entities requesting access and objects are the resources that subjects are trying to access. Rules and policies are defined that associate subjects and object permissions and access controls.

### Common implementations
#### Security label access control
A fine-grained form control is to apply security labels to individual resources, including processes, and the access control decisions are against a particular resource and a given user attempting to gain access. This type of control requires that the file system has built-in support for security labels.

Access controls are typically implemented through the use of label identifiers for every file system object. Identifier labels are applied to resources and users are assigned a similar access identifier. Users attempting to access a resource will result in the operating system performing an access control check. The access control check will compare the assigned user's credentials to that of the resource or object they are attempting to access.

A security context is associated with resources and is used to determine assess. Typical basic access control elements include users, roles and types and together they form a security context which is the basis for the security labels.

This type of access control is what is employed in SELinux [2]. This form of security kernel access control is considered the most flexible implementation, but it also is the most complex to deploy across the enterprise. Where multiple virtual machines (VM) are run together this type of access control is typically employed to ensure true isolation of processes and VMs.

#### File path level controls
A less fine-grained form of mandatory access control is to apply security labels that allow for access control at the file path level.  Access control is filesystem agnostic and no relabeling of resources is required. Pathname access control usually seems more natural for implementation and corresponding access audits.

This type of system call filtering is what is employed in AppArmor [3]. AppArmor was developed to provide a simpler alternative method with much less management overhead. A simple access policy is maintained that defines path resource access rules. Access control attributes are typically associated with programs instead of users.


## Considerations
Some implementations of security label-based control contain complex rules set that are hard to verify and complex to maintain over time.

Initial planning of access model and continuous monitoring of the available users, resources and object is necessary.

## Implementations

 * Linux C-Groups, and policy engines like SELinux and AppArmor
 * Windows Mandatory Integrity Control introduced in Windows Vista


### Citations
1. [SELinux](https://selinuxproject.org/)
2. [AppArmor](https://www.apparmor.net/)
