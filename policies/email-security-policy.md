---
Expires: 2020-12-31
---


# Email Security Guide

## Introduction

This guide sets out the requirements for implementing and maintaining email security across the MoJ. This page is the first in a series of guides for implementing email security controls within the MoJ.

## Who is this for?     
This guide is aimed at two audiences:
1. The in-house MoJ Digital and Technology staff who are responsible for implementing controls throughout technical design, development, system integration and operation. This includes DevOps, Software Developers, Technical Architects and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI and Knowledge (EPICK) Team. 
2. Any other MoJ business group, agency, contractor, IT supplier and partner who in any way designs, develops or supplies services (including processing, transmitting and storing data) for, or on behalf of the MoJ.

## Related guides
Further guidance on email security at the MoJ can be found in the guides below. 

**Spam and Phishing Guide** – provides guidance on how you can protect against and report email security threats like phishing and spamming.

**Secure Email Transfer Guide** – provides guidance on the security tools you can use to securely transfer information via email. 

**Email Authentication Guide** – provides guidance on the authentication mechanisms that should be used at the domain layer to maintain security. 

## Roles and responsibilities  
All **technical users** are responsible for maintaining and using the MoJ’s email communications securely in line with the requirements set out in this guide. 
* Where possible automate checks of the sender's authenticity. 
* Ensure all email communications are protected according to the classification of the information held within them (see the Information Classification Handling and Security Guide for further information).
* Ensure all users of the email service are aware of the Acceptable Use Policy and operate it in accordance with it. 
* Encourage online working by default to limit the downloading of data to mobile devices. 
* Ensure suspected or actual phishing emails are easily reported to the Technology Service Desk as email attachments. 
* Keep your operating systems up to date to prevent susceptibility to viruses.
* Scan email attachments to detect viruses and other malware.
* Ensure email services are appropriately authenticated (Refer to Email Authentication Guide for more information)
* Ensure secure email messaging services and where necessary encryption tools are used to transfer information and system secrets (refer to the Secure Email Transfer Guide for further guidance). 
* Ensure that email configuration is secure and all necessary technical controls, including those set out in the Malware Protection Guide are implemented and kept up to date. 

**Suppliers** may use their own email services if agreed by the MoJ but, as a minimum, they must meet the security requirements in this guide and its related guides.

## Authorised access of users’ accounts
You must not access the email accounts of any other user unless you are authorised to do so as required by your role. Access is to be authorised on a case by case basis only, and will typically be aligned to the following circumstances: 

* during a criminal investigation by a law enforcement agency
* during an employee investigation relating to misconduct or a security incident, for example IT misuse
* upon the death or unexpected exit of an employee, for example for the retrieval of key information and closing down an account.  

Anyone required to undertake this task should read this guide in conjunction with the Privileged User Guide.
However, the MoJ does monitor Email services for security purposes.

## Delegate access 
MoJ IT users may want to give another user access to their email account. System administrators must ensure end users cannot provide another user with delegate access to their account; with the exception of a mailbox owner requiring a delegate user to:

* read, send or delete messages on their behalf
* manage their calendar.

To ensure secure delegation, system administrators must:

* enforce mailbox owners to limit delegate access to pre-defined periods of time 
* enable mailbox owners to manage and revoke access themselves
* prevent federated sharing
* prevent auto-forwards to external email services (including personal email accounts) or configure a remote domain
* prevent delegate access to unauthorised users (e.g. people outside the MoJ) by enforcing RBAC. 

For personal accounts the helpdesk can configure delegate access; administrators of group inboxes can also configure delegate access to those inboxes.

For further details see the Privileged User Guide. 

## Contact details

* Contact Cyber Assistance Team for advice on email security – [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk) 
* For any further questions relating to security, please contact: [security@justice.gov.uk](mailto:security@justice.gov.uk)
* Contact the Technology Service Desk to report suspected IT Security Incidents – [MOJ.Servicedesk.uk@CGI.com](mailto:MOJ.Servicedesk.uk@CGI.com) Telephone: 0800 917 5148.





















