# D3-SMRA: Sender MTA Reputation Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-SMRA/  

## Definition
Characterizing the reputation of mail transfer agents (MTA) to determine the security risk in emails.

## Parent Class(es)
- Message Analysis

## Relationships
- **analyzes:** Email
- **kb-reference:** Reference - Systems and methods for detecting and/or handling targeted attacks in the email channel - Graphus Inc

## Knowledge Base Article
## How it works
The sender message transfer agent (MTA) trust rating can be considered an indicator of the level of security risk and/or a trust level associated with sender MTAs in an email header.

The features considered in determining the trust rating may include:

* Length of time MTA has interacted with the enterprise
* Number of sender domains sending emails from the MTA
* Number of recipients in the enterprise the MTA sends emails to
* Number of emails received from this MTA
* Number of email replies received from this MTA

For example, higher values for the length of time an MTA has interacted with the enterprise, or number of emails received from an MTA can result in a higher trust rating. The trust rating categorizes the sender MTA as unrated, neutral, trusted, suspicious, or malicious.

## Considerations
Legitimate emails from a sender MTA may receive a lower trust rating over time if the sender's domain gets spoofed and is used to send unauthorized emails.
