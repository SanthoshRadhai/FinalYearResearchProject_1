# D3-UA: URL Analysis

**Reference:** https://d3fend.mitre.org/technique/D3-UA/  

## Definition
Determining if a URL is benign or malicious by analyzing the URL or its components.

## Parent Class(es)
- Identifier Analysis

## Relationships
- **analyzes:** URL
- **kb-reference:** Reference - Method and Apparatus for Detecting Malicious Websites - Endgame Inc
- **kb-reference:** Reference - Method and system for detecting restricted content associated with retrieved content - Sophos Ltd

## Knowledge Base Article
## How it works

URLs may contain components, for example:

 * scheme
 * userinfo
 * host name
 * port
 * path
 * query
 * fragment

These components are used as features in analysis algorithms.

Contextual information about a URL such as where it is embedded (ex. emails, files, network protocols), header, path, location, and origin information, as well as information about the content returned from the URL request, may be incorporated into an analytic for URL analysis. For example, if a URL indicates a .pdf file but an executable is actually returned, the combination of these two pieces of information indicates suspicious activity.

Additional techniques include:

* Extracting features of a URL such as domain name length, ratio of consecutive consonants, percentage of digits in a domain, and number of vowels. Values for each feature are combined to develop a score for the URL.
* Determining the probability of a character occurring in the URL given the preceding two characters. For example, for google.com, the probability of a 'g' occurring at the beginning of a word, the probability of an 'o' occurring after a "g, the probability of an o" occurring after a 'g' and "o, and so forth. A dictionary or a list of known good domains is used to determine probability. Probabilities are multiplied to develop a score for the URL.

URL analysis may trigger follow-on analytics such as **File Analysis**

## Considerations

* Volume of URLs being analyzed, combined with the speed at which they are analyzed
* Fidelity of analysis technique at detecting brand new URLs versus analyzing URLs of established domains
