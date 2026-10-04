# CWE-478: Missing Default Case in Multiple Condition Expression

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/478.html  

## Description
The code does not have a default case in an expression with multiple conditions, such as a switch statement.

## Extended Description
If a multiple-condition expression (such as a switch in C) omits the default case but does not consider or handle all possible values that could occur, then this might lead to complex logical errors and resultant weaknesses. Because of this, further decisions are made based on poor information, and cascading failure results. This cascading failure may result in any number of security issues, and constitutes a significant failure in the system.

## Related Weaknesses
- ChildOf: CWE-1023

## Common Consequences
- Scope: Integrity; Impact: Varies by Context, Alter Execution Logic — Depending on the logical circumstances involved, any consequences may result: e.g., issues of confidentiality, authentication, authorization, availability, integrity, accountability, or non-repudiation.

## Potential Mitigations
- [Implementation] Ensure that there are no cases unaccounted for when adjusting program flow or values based on the value of a given variable. In the case of switch style statements, the very simple act of creating a default case can, if done correctly, mitigate this situation. Often however, the default case is used simply to represent an assumed option, as opposed to working as a check for invalid input. This is poor practice and in some cases is as bad as omitting a default case entirely.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following does not properly check the return code in the case where the security_check function returns a -1 value when an error occurs. If an attacker can supply data that will invoke an error, the attacker can bypass the security check:
- In the following Java example the method getInterestRate retrieves the interest rate for the number of points for a mortgage. The number of points is provided within the input parameter and a switch statement will set the interest rate value to be returned based on the number of points.
- In the following Python example the match-case statements (available in Python version 3.10 and later) perform actions based on the result of the process_data() function. The expected return is either 0 or 1. However, if an unexpected result (e.g., -1 or 2) is obtained then no actions will be taken potentially leading to an unexpected program state.
- In the following JavaScript example the switch-case statements (available in JavaScript version 1.2 and later) are used to process a given step based on the result of a calcuation involving two inputs. The expected return is either 1, 2, or 3. However, if an unexpected result (e.g., 4) is obtained then no action will be taken potentially leading to an unexpected program state.
- The Finite State Machine (FSM) shown in the "bad" code snippet below assigns the output ("out") based on the value of state, which is determined based on the user provided input ("user_input").
