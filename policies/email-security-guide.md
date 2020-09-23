---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](home-security-policies-guides.md)

# Email Security Guide

## Introduction

This guide sets out the requirements for implementing and maintaining email security across the MoJ. This page is the first in a series of guides for implementing email security controls within the MoJ.

## Who is this for?

This guide is aimed at two audiences:

1. The in-house MoJ Digital and Technology staff who are responsible for implementing controls throughout technical design, development, system integration and operation. This includes DevOps, Software Developers, Technical Architects and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI and Knowledge (EPICK) Team.
2. Any other MoJ business group, agency, contractor, IT supplier and partner who in any way designs, develops or supplies services (including processing, transmitting and storing data) for, or on behalf of the MoJ.

In this and the related guides outlined below, this audience will be referred to as "technical users".

## Related guides

Further guidance on email security at the MoJ can be found in the guides below.

* [Spam and Phishing Guide](spam-and-phishing-guide.md) - provides guidance on how you can protect against and report email security threats like phishing and spamming.
* [Secure Email Transfer Guide](secure-email-transfer-guide.md) - provides guidance on the security tools you can use to securely transfer information via email.
* [Email Authentication Guide](email-authentication-guide.md) - provides guidance on the authentication mechanisms that should be used at the domain layer to maintain security.

## Roles and responsibilities

All **technical users** are responsible for maintaining and using the MoJ's email communications securely in line with the requirements set out in this guide.

* Where possible automate checks of the sender's authenticity by implementing the controls in the [Email Authentication Guide](email-authentication-guide.md).
* Ensure all email communications are protected according to the classification of the information held within them (see the [Information Classification Handling and Security Guide](information-classification-handling-and-security-guide.md) for further information).
* Depreciate the downloading of data to mobile devices by promoting the use cloud services such as O365.
* Ensure suspected or actual phishing emails are easily reported to the Technology Service Desk as email attachments.
* Keep your operating systems up to date to prevent susceptibility to viruses.
* Scan email attachments to detect viruses and other malware.
* Ensure email services are appropriately authenticated (Refer to the [Email Authentication Guide](email-authentication-guide.md) for more information)
* Ensure secure email messaging services and, where necessary, encryption tools are used to transfer sensitive information and system secrets (refer to the [Secure Email Transfer Guide](secure-email-transfer-guide.md) for further guidance).
* Ensure that email configuration is secure and all necessary technical controls, including those set out in the [Malware Protection Guide](malware-protection-guide-introduction.md) are implemented and kept up to date.

**Suppliers** may use their own email services if agreed by the MoJ but, as a minimum, they must meet the security requirements in this guide and its related guides.

## Authorised access of users' accounts

By default, users must not access the email accounts of any other users unless they are authorised to do so as required by their role. Access is to be authorised on a case by case basis only, and will typically be aligned to the following circumstances:

* during a criminal investigation by a law enforcement agency
* during an employee investigation relating to misconduct or a security incident, for example IT misuse
* upon the death or unexpected exit of an employee, for example for the retrieval of key information and closing down an account.

Anyone required to undertake this task should read this guide in conjunction with the [Privileged User Guide](privileged-user-guide.md).

## Monitoring

For clarity and transparency, the MoJ does monitor Email services for security purposes.

## Delegate access

Technical users must ensure end users do not have the privileges required provide another user with delegate access to their account.  However, MoJ IT users may need to give another user access to their email account. If a mailbox owner has a legitimate requirement for another user to:  

* read, send or delete messages on their behalf, or
* manage their calendar

the user must seek permission from their line manager.  Where permission is granted and to ensure secure delegation, technical users must:

* enforce mailbox owners to limit delegate access to pre-defined periods of time
* enable mailbox owners to manage and revoke access themselves
* prevent federated sharing, this is where users in one Exchange organisation can share free/busy calendar information with recipients in other Exchange organisations
* prevent auto-forwards to external email services (including personal email accounts)
* prevent delegate access to unauthorised users (e.g. people outside the MoJ) by enforcing RBAC.

For personal accounts the helpdesk can configure delegate access; administrators of group inboxes can also configure delegate access to those inboxes.

For further details see the [Privileged User Guide](privileged-user-guide.md).

## Contact details

* Contact Cyber Assistance Team for advice on email security: [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk)
* For any further questions relating to security, please contact: [security@justice.gov.uk](mailto:security@justice.gov.uk)
* Contact the Technology Service Desk to report suspected IT Security Incidents: [MOJ.Servicedesk.uk@CGI.com](mailto:MOJ.Servicedesk.uk@CGI.com) Telephone: 0800 917 5148.
