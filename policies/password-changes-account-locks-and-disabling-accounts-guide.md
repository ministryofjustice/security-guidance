---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](home-security-policies-guides.md)

# Password Changes, Account Locks and Disabling Accounts Guide

## Introduction

This guide sets out when passwords should be changed and when user accounts will be locked. This guide is a sub-page to the [Password Management Guide](../password-management-guide/).

## Password changes and account lockouts

When designing and developing systems for use within MoJ, password changes should be enforced when:

 ✔ a user has forgotten their password or is experiencing login issues

 ✔ there has been a security incident involving the account or password

 ✔ an authorised person, such as line manager or IT support, requests the change

 ✔ the system prompts you to change a password

 ✔ you suspect an account may have been compromised.

Password changes must be made within the timeframes specified in the table below:


| Type of System | Lifetime of a single-use password/change request|
|--- |---|
| Single-user systems, such as laptop | 1 week |
| All other systems | 1 day |

Account lockouts within the MoJ can happen for the following reasons:

1. **Failure to change passwords within the allocated time**. Systems must have a ‘change password’ function to recover the account or contact information for the Technology Service Desk.

2. **Unsuccessful connection attempts**. Allow between 5-10 login attempts before lockout.

3. **Forgotten passwords**. All MoJ systems must have a forgotten password link on the login page, which must enable the user to change the password on their own. Ensure this uses multi-factor authentication for user verification.

4. **Removed or disabled access**. Users may experience account lockouts due to inactivity, need to know permissions or change of employment status such as contract termination. Access to these accounts must only be re-enabled with line manager approval.

## Disabling accounts

All MoJ user accounts are access controlled according to the user's 'need to know' requirements and their employment status. Accounts should be disabled at contract termination and during long-term absences, such as maternity or long-term sickness leave. The MoJ disables user accounts in alignment with the Access Control Guide.

## Contact details

For any further questions relating to security, please contact: [security@justice.gov.uk](mailto:security@justice.gov.uk)
