# D3-DQSA: Database Query String Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-DQSA/  

## Definition
Analyzing database queries to detect [SQL Injection](https://capec.mitre.org/data/definitions/66.html).

## Parent Class(es)
- Process Analysis

## Relationships
- **analyzes:** Database Query
- **kb-reference:** Reference - System and method for internet security - Cylance Inc

## Knowledge Base Article
## How it works

Some implementations use software hooks to intercept function calls related to database query operations. Other implementations might intercept or collect network traffic. The database query string is then extracted and analyzed with various methods, for example:
* Detecting specific administrative SQL commands
* Anomalous sequences of commands when compared to a statistical baseline.
* Anomalous commands for a given user role.

## Considerations

Some capabilities sanitize queries before permitting them to be transmitted to the database. This incurs risks such altering data in an undesired way or breaking application functionality.
