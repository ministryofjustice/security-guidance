# Email Security Guide

-   **[Email Authentication Guide](email-authentication-guide.md)**  

-   **[Secure Email Transfer Guide](secure-email-transfer-guide.md)**  

-   **[Spam and Phishing Guide](spam-and-phishing-guide.md)**  


## Introduction

This guide sets out the requirements for implementing and maintaining email security across the Ministry of Justice \(MoJ\).

## Who is this for?

This guide is aimed at two audiences:

-   The in-house MoJ Digital and Technology staff who are responsible for implementing controls throughout technical design, development, system integration, and operation. This includes DevOps, Software Developers, Technical Architects, and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI, and Knowledge \(EPICK\) Team.
-   Any other MoJ business group, agency, contractor, IT supplier, or partner who in any way designs, develops, or supplies services \(including processing, transmitting, and storing data\) for, or on behalf of, the MoJ.

These audiences are referred to as "technical users".

## Roles and responsibilities

All technical users are responsible for maintaining and using the MoJ's email communications securely, in line with the requirements set out in this guide. In particular:

-   Where possible, automate checks of the sender's authenticity by implementing the controls in the [Email Authentication Guide](email-authentication-guide.md).
-   Ensure all email communications are protected according to the classification of the information held within them. There is more information in the the [Information Classification Handling and Security Guide](information-classification-handling-and-security-guide.md).
-   Discourage people from downloading data to mobile devices. Instead, encourage and enable the use of cloud services such as Office 365.
-   Make it easy for people to send suspected or actual phishing emails to the IT Service Desk, so that the emails can be handled safely.
-   Keep operating systems up-to-date, to prevent susceptibility to viruses.
-   Scan email attachments to detect viruses and other malware.
-   Ensure email services are appropriately authenticated. Refer to the [Email Authentication Guide](email-authentication-guide.md) for more information.
-   Ensure secure email messaging services, and, where necessary, encryption tools, are used to transfer sensitive information and system secrets. Refer to the [Secure Email Transfer Guide](secure-email-transfer-guide.md) for further information.
-   Ensure that email configuration is secure, and that all necessary technical controls, including those set out in the [Malware Protection Guide](malware-protection-guide-introduction.md), are implemented and kept up to date.

**Note:** Suppliers **MAY** use their own email services if agreed by the MoJ but, as a minimum, they must meet the MoJ security requirements.

## Authorised access to user accounts

By default, users **SHALL NOT** access the email accounts of any other users, unless they are authorised to do so as required by their role. Access is authorised on a case-by-case basis only, and is normally aligned to the following circumstances:

-   During a criminal investigation by a law enforcement agency.
-   During an employee investigation relating to misconduct or a security incident, for example IT misuse.
-   Upon the death or unexpected exit of an employee, for example to enable retrieval of business information or closing down an account.

Anyone required to enable or carry out authorised access to a user account should follow the guidance in the [Privileged User Guide](privileged-user-guide.md).

## Monitoring

The MoJ does monitor Email services for security purposes.

## Delegate access

Ensure that standard end users do not by default have the permissions necessary to provide another user with delegate access to their account. There will, however, be occasions when an MoJ IT user might need to give another user access to their email account.

Examples would be where a mailbox owner has a legitimate requirement for another user to:

-   Read, send, or delete messages on their behalf.
-   Manage their calendar.

In this situation, the user **SHALL** first seek permission from their line manager. When permission is granted, technical users **SHALL** ensure secure delegation by:

-   Enforcing mailbox owners to limit delegate access to pre-defined periods of time.
-   Enabling mailbox owners to manage and revoke access themselves.
-   Prevent federated sharing, where users in one organisation can share free or busy calendar information with recipients in other organisations.
-   Preventing auto-forwards to external email services, including personal email accounts.
-   Preventing delegate access to unauthorised users, such as people outside the MoJ\), by enforcing Role Based Access Control \(RBAC\).
-   Implementing [Access Control Policy](access-control-policy.md), in particular regarding access to email as a result of forwarding or delegation.

For individual accounts, the IT Service Desk can configure delegate access. Administrators of group inboxes can also configure delegate access to those inboxes.

For further details, refer to the [Privileged User Guide](privileged-user-guide.md).

## Contact details

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for security advice, contact the Cyber Assistance Team [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

