# D3-HD: Homoglyph Detection

**Reference:** https://d3fend.mitre.org/technique/D3-HD/  

## Definition
Comparing strings using a variety of techniques to determine if a deceptive or malicious string is being presented to a user.

## Parent Class(es)
- Identifier Analysis

## Relationships
- **analyzes:** Email
- **analyzes:** URL
- **kb-reference:** Reference - Computer-implemented methods and systems for identifying visually similar text character strings - Greathorn Inc
- **kb-reference:** Reference - System and method for detecting homoglyph attacks with a siamese convolutional neural network - Endgame Inc

## Knowledge Base Article
## How it works
A homoglyph, in this context, is a deceptive string or word which looks like a trusted word, but is composed of different characters, for example: goooogle.com versus google.com. This is commonly found in phishing and typo squatting attacks where a human exploiting through a social engineering campaign.

## Considerations
* In very large environments processing DNS queries can be computationally expensive due to the amount of traffic that is generated
* Legitimate companies and products use non-dictionary words in their names that could result in many false positives
