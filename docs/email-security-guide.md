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

In this and the related guides outlined below, the intended audience will be referred to as “technical users”.

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
-   Ensure suspected or actual phishing emails are easily reported to the Technology Service Desk as email attachments. Do this by contacting your [appropriate service desk](#general-enquiries-including-theft-and-loss).
-   Ensure email services are appropriately authenticated. Refer to the [Email Authentication Guide](email-authentication-guide.md) for more information.
-   Enable opportunistic encryption of emails in transit. This means that wherever possible, encryption should be used to transfer information. Refer to the [Secure Email Transfer Guide](secure-email-transfer-guide.md) for further guidance.
-   Ensure that email configuration is secure and all necessary technical controls, including those set out in the [Malware Protection Guide](malware-protection-guide-introduction.md) are implemented and kept up to date.

Suppliers are permitted to use their own email services, if agreed in advance by the MoJ but, as a minimum, they must meet the security requirements in this guide and its related guides.

## Delegate access

There might be valid business reasons why an MoJ IT user might need to give another user access to their email account. These valid requirements include:

-   Reading, sending or deleting messages on their behalf.
-   Managing their calendar.

Where an email system permits delegation, ensure that:

-   By default, delegate access is not initially operating for an email account. In other words, when an email account is created, no-one has delegate access immediately.
-   Access cannot be delegated to people outside the MoJ.
-   When delegate access is enabled, it is for a limited period of time. In most email systems, cancellation of delegation cannot be scheduled; it requires a manual step. Therefore, as part of the process of enabling delegate access, there must be a reminder or alerting mechanism to review and cancel the delegation at an expiry date and time.
-   Mailbox owners can manage and revoke access themselves.
-   There is no 'federated' sharing. In other words, users in one email community cannot share calendar or other email information with recipients in other email communities. For example, it should not be possible for someone in a `securityteam@email.address` to delegate access to `developerteam@another.email.address`.
-   Auto-forwards to external email services are not possible. This includes preventing auto-forwards to personal email accounts.

**Note:** An external email service is any service that is outside the `gov.uk` domain.

For further details see the [Privileged Account Management Guide](privileged-account-management-guide.md).

## General enquiries, including theft and loss

Dom1/Quantum - Technology Service Desk:

-   Tel: 0800 917 5148

**Note:** The previous `itservicedesk@justice.gov.uk` email address is no longer being monitored.

Digital &amp; Technology - Digital Service Desk:

-   Email: [servicedesk@digital.justice.gov.uk](mailto:servicedesk@digital.justice.gov.uk)
-   Slack: `#digitalservicedesk`

HMPPS Information & security:

-   Email: [informationmgmtsecurity@justice.gov.uk](mailto:informationmgmtsecurity@justice.gov.uk)
-   Tel: 0203 334 0324

## Contact details

-   Contact the Cyber Assistance Team for specific advice on IT security: [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).
-   For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).
-   [To report an incident](reporting-an-incident.md).
-   Suppliers to the MoJ should first ask their usual MoJ points of contact.

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

