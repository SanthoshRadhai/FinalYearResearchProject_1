# CWE-640: Weak Password Recovery Mechanism for Forgotten Password

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/640.html  

## Description
The product contains a mechanism for users to recover or change their passwords without knowing the original password, but the mechanism is weak.

## Extended Description
It is common for an application to have a mechanism that provides a means for a user to gain access to their account in the event they forget their password. Very often the password recovery mechanism is weak, which has the effect of making it more likely that it would be possible for a person other than the legitimate system user to gain access to that user's account. Weak password recovery schemes completely undermine a strong password authentication scheme. This weakness may be that the security question is too easy to guess or find an answer to (e.g. because the question is too common, or the answers can be found using social media). Or there might be an implementation weakness in the password recovery mechanism code that may for instance trick the system into e-mailing the new password to an e-mail account other than that of the user. There might be no throttling done on the rate of password resets so that a legitimate user can be denied service by an attacker if an attacker tries to recover their password in a rapid succession. The system may send the original password to the user rather than generating a new temporary password. In summary, password recovery functionality, if not carefully designed and implemented can often become the system's weakest link that can be misused in a way that would allow an attacker to gain unauthorized access to the system.

## Related Weaknesses
- ChildOf: CWE-1390
- ChildOf: CWE-287

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity — An attacker could gain unauthorized access to the system by retrieving legitimate user's authentication credentials.
- Scope: Availability; Impact: DoS: Resource Consumption (Other) — An attacker could deny service to legitimate system users by launching a brute force attack on the password recovery mechanism using user ids of legitimate users.
- Scope: Integrity, Other; Impact: Other — The system's security functionality is turned against the system by the attacker.

## Potential Mitigations
- [Architecture and Design] Make sure that all input supplied by the user to the password recovery mechanism is thoroughly filtered and validated.
- [Architecture and Design] Do not use standard weak security questions and use several security questions.
- [Architecture and Design] Make sure that there is throttling on the number of incorrect answers to a security question. Disable the password recovery functionality after a certain (small) number of incorrect guesses.
- [Architecture and Design] Require that the user properly answers the security question prior to resetting their password and sending the new password to the e-mail address of record.
- [Architecture and Design] Never allow the user to control what e-mail address the new password will be sent to in the password recovery mechanism.
- [Architecture and Design] Assign a new temporary password rather than revealing the original password.

## Demonstrative Examples (summary)
- A famous example of this type of weakness being exploited is the eBay attack. eBay always displays the user id of the highest bidder. In the final minutes of the auction, one of the bidders could try to log in as the highest bidder three times. After three incorrect log in attempts, eBay password throttling would kick in and lock out the highest bidder's account for some time. An attacker could then make their own bid and their victim would not have a chance to place the counter bid because they would be locked out. Thus an attacker could win the auction.
