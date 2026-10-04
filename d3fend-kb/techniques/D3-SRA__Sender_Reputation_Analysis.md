# D3-SRA: Sender Reputation Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-SRA/  

## Definition
Ascertaining sender reputation based on information associated with a message (e.g. email/instant messaging).

## Parent Class(es)
- Message Analysis

## Relationships
- **analyzes:** Email
- **kb-reference:** Reference - Systems and methods for detecting and/or handling targeted attacks in the email channel - Graphus Inc

## Knowledge Base Article
## How it works

Sender trust rating can be considered an indicator of the level of security risk and/or a trust level associated with a sender. The features considered in determining the trust rating include:

* Length of time sender has sent emails to the enterprise
* Number of recipients in the enterprise the sender interacts with
* Sender vs. enterprise originated message ratio
* Sender messages opened vs. not-opened ratio
* Number of emails received from this sender
* Number of emails replied to this sender
* Number of emails from this sender not opened
* Number of emails from this sender not opened that contain an attachment
* Number of emails from this sender not opened that contain a URL
* Number of emails sent to this sender
* Number of email replies received from this sender.

Higher values for the number of recipients the sender has interacted with or the number of emails received from the sender, for example, results in a higher trust rating. The trust rating can categorize the sender as unrated, neutral, trusted, suspicious, or malicious.

## Considerations
Legitimate emails from a sender may receive a lower trust rating over time if the sender's domain gets spoofed and is used to send unauthorized emails.
