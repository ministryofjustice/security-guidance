# Email Security Guide

-   **[Email Authentication Guide](email-authentication-guide.md)**  

-   **[Secure Email Transfer Guide](secure-email-transfer-guide.md)**  

-   **[Spam and Phishing Guide](spam-and-phishing-guide.md)**  


**Parent topic:**[Email security](email.md)

## Introduction

This guide sets out the requirements for implementing and maintaining email security across the Ministry of Justice \(MoJ\). This guidance is the first in a series of guides for implementing email security controls within the MoJ.

## Who is this for?

This guide is aimed at two audiences:

1.  The in-house MoJ Digital and Technology staff who are responsible for implementing controls throughout technical design, development, system integration and operation. This includes DevOps, Software Developers, Technical Architects and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI and Knowledge \(EPICK\) Team.
2.  Any other MoJ business group, agency, contractor, IT supplier and partner who in any way designs, develops or supplies services \(including processing, transmitting and storing data\) for, or on behalf of the MoJ.

In this and the related guides outlined below, this audience will be referred to as "technical users".

## Related guides

Further guidance on email security at the MoJ can be found in the following guides.

-   [Spam and Phishing Guide](spam-and-phishing-guide.md) - provides guidance on how you can protect against and report email security threats like phishing and spamming.

-   [Secure Email Transfer Guide](secure-email-transfer-guide.md) - provides guidance on the security tools you can use to securely transfer information via email.

-   [Email Authentication Guide](email-authentication-guide.md) - provides guidance on the authentication mechanisms that should be used at the domain layer to maintain security.


## Roles and responsibilities

All technical users are responsible for maintaining and using the MoJ's email communications securely in line with the requirements set out in this guide.

-   Where possible automate checks of the sender's authenticity by implementing the controls in the [Email Authentication Guide](email-authentication-guide.md).
-   Ensure all email communications are protected according to the classification of the information held within them. See the Information Classification Handling and Security Guide for further information.
-   Discourage downloading of data to mobile devices by promoting the use cloud services such as Office 365.
-   Ensure suspected or actual phishing emails are easily reported to the Technology Service Desk as email attachments.
-   Keep your operating systems up to date to prevent susceptibility to viruses.
-   Scan email attachments to detect viruses and other malware.
-   Ensure email services are appropriately authenticated. Refer to the [Email Authentication Guide](email-authentication-guide.md) for more information.
-   Ensure secure email messaging services and, where necessary, encryption tools are used to transfer sensitive information and system secrets. Refer to the [Secure Email Transfer Guide](secure-email-transfer-guide.md) for further guidance.
-   Ensure that email configuration is secure and all necessary technical controls, including those set out in the [Malware Protection Guide](malware-protection-guide-introduction.md) are implemented and kept up to date.

Suppliers are permitted to use their own email services, if agreed in advance by the MoJ but, as a minimum, they must meet the security requirements in this guide and its related guides.

## Authorised access of users' accounts

By default, users must not access the email accounts of any other users unless they are authorised to do so as required by their role. Access is to be authorised on a case by case basis only, and will typically be aligned to the following circumstances:

-   During a criminal investigation by a law enforcement agency.
-   During an employee investigation relating to misconduct or a security incident, for example IT misuse.
-   Upon the death or unexpected exit of an employee, for example for the retrieval of key information and closing down an account.

Anyone required to undertake this task should read this guide in conjunction with the [Privileged Account Management Guide](privileged-account-management-guide.md).

## Monitoring

To be clear, the MoJ *does* monitor Email services for security purposes.

## Delegate access

Technical users must ensure end users do not have the privileges required to provide another user with delegate access to their account. There might be valid business reasons why an MoJ IT user might need to give another user access to their email account. These valid requirements include:

-   Reading, sending or deleting messages on their behalf.
-   Managing their calendar.

In such cases, the user must seek permission from their line manager. Where permission is granted, and to ensure secure delegation, technical users must:

-   Enforce delegate access to pre-defined limited periods of time.
-   Enable mailbox owners to manage and revoke access themselves.
-   Prevent federated sharing, where users in one email community can share calendar or other email information with recipients in other email communities.
-   Prevent auto-forwards to external email services, including personal email accounts.
-   Prevent the possibility of delegating access to unauthorised users, for example to people outside the MoJ. Do this by enforcing RBAC.

For individual business accounts, the helpdesk can assist with configuring delegate access. Administrators of group inboxes can configure delegate access to those inboxes.

For further details see the [Privileged Account Management Guide](privileged-account-management-guide.md).

## Contact details

-   Contact the Cyber Assistance Team for specific advice on IT security: [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).
-   For any further questions relating to security, contact: [security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk).
-   [To report an incident](reporting-an-incident.md).
-   Suppliers to the MoJ should first ask their usual MoJ points of contact.

