# D3-CIA: Container Image Analysis

**Synonym(s):** Container Image Scanning  
**Reference:** https://d3fend.mitre.org/technique/D3-CIA/  

## Definition
Analyzing a Container Image with respect to a set of policies.

## Parent Class(es)
- Asset Vulnerability Enumeration

## Relationships
- **analyzes:** Container Image
- **kb-reference:** Reference - Container Image Analysis

## Knowledge Base Article
## How it works

Container images are standalone collections of the executable code and
content that are used to populate a container environment.
They are usually created by either building a container from scratch or by
building on top of an existing image pulled from a repository.

Throughout the container build workflow,
images should be scanned to identify:

- outdated libraries,
- known vulnerabilities,
- or misconfigurations, such as insecure ports or permissions.

Scanning should also provide the flexibility to disregard false positives
for vulnerability detection where knowledgeable
cybersecurity professionals have deemed alerts to be inaccurate.

One approach to implementing image scanning is to use an admission controller
to block deployments if the image does not comply with the organization's
security policies.

An admission controller is a Container Orchestration feature that can intercept and
process requests to the Container Orchestration API prior to persistence of the object,
but after the request is authenticated and authorized.
A webhook can be implemented to scan any image before it is deployed in the orchestrator.
This admission controller

## Considerations

* Image scanning is key to ensuring deployed containers are secure.
* Using trusted repositories to build containers is a critical part of the container build workflow.
* This technique does not necessarily prevent the build process to add insecure or unsecured
  files to the Image.
