# D3-PHDURA: Per Host Download-Upload Ratio Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-PHDURA/  

## Definition
Detecting anomalies that indicate malicious activity by comparing the amount of data downloaded versus data uploaded by a host.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** Network Traffic
- **kb-reference:** Reference - System for detecting threats using scenario-based tracking of internal and external network traffic - VECTRA NETWORKS Inc

## Knowledge Base Article
## How it works
Aggregate pull vs. push ratios from metadata are used to develop a baseline for a given host over a specific time period, e.g., over a three-hour period, one day, one week, etc. Anomalies identified over a threshold produce an alert.

## Considerations
Collection and analysis of large network packet captures requires large storage and intensive computing power. The time windows used to calculate the ratio may vary in implementations, this consideration should take into account a threat model and likely effects (impacts) delivered by an adversary.
