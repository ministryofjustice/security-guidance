# Privileged User Guide

<a name="[privileged-user-backups-removable-media-and-incident-management-guide](privileged-user-backups-removable-media-and-incident-management-guide.md)"></a>

-   **[Privileged User Backups, Removable Media and Incident Management Guide](privileged-user-backups-removable-media-and-incident-management-guide.md)**  

<a name="[privileged-user-configuration-patching-and-change-management-guide](privileged-user-configuration-patching-and-change-management-guide.md)"></a>

-   **[Privileged User Configuration, Patching and Change Management Guide](privileged-user-configuration-patching-and-change-management-guide.md)**  

<a name="[privileged-user-logging-and-protective-monitoring-guide](privileged-user-logging-and-protective-monitoring-guide.md)"></a>

-   **[Privileged User Logging and Protective Monitoring Guide](privileged-user-logging-and-protective-monitoring-guide.md)**  


## Introduction

This guide outlines the security procedures and advice that privileged users should follow when accessing the Ministry of Justice \(MoJ\) IT systems in a safe and secure manner. Privileged users are those who have elevated levels of system access in order to manage IT system components to meet MoJ IT service requirements. Privileged users might, for example, install software, configure and upgrade IT systems, input into the Service Management Tool for the systems they manage, and run day-to-day operations to satisfy continuity of service, recovery, security, and performance needs. This includes privileged users who manage Slack or Github repositories, users who have administrative access on their laptops, and users who setup and maintain platforms hosted in the Cloud.

Specific responsibilities of individual privileged users are likely to vary depending on the systems they manage. The system's Information Risk Assessment Report documents the security controls \([MoJ Information Assurance Framework Process](https://docs.google.com/document/d/1vQOlnD1Xixlw20p7OuO8nleV8qt0BfvVWvXkPQurZ3A/edit?usp=sharing)\). The [IRAR](https://docs.google.com/document/d/1MeJJtfHpwR1XM_okk3Pi4gW0bpcnLDdt5OXwddB7-Bk/edit?ts=5e25c004) should be completed as part of this process. For a comprehensive list of individual responsibilities, privileged users should refer to the system specific documentation.

This page is the first in a series of guides for privileged users within the MoJ; refer also to the related guides.

## Who is this for?

This guide is aimed at two audiences, both technical.

-   The in-house MoJ Digital and Technology staff who are responsible for implementing controls throughout technical design, development, system integration and operation. This includes DevOps, Software Developers, Technical Architects and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI and Knowledge \(EPICK\) Team.
-   Any other MoJ business groups, Agencies, contractors, IT suppliers and partners who in any way design, develop or supply services \(including processing, transmitting and storing data\) for, or on behalf of, the MoJ.

## Related guides

For further details about privileged user responsibilities, refer to the following guides.

-   The [Privileged Account Management Guide](privileged-account-management-guide.md) provides the guidelines to ensure that privileged accounts are securely managed. It is part of the [Access Control Guide](access-control-guide.md).
-   The [Logging and Protective Monitoring Guide](privileged-user-logging-and-protective-monitoring-guide.md) provides information about security procedures privileged users should implement to conduct logging activities.
-   The [Backups, Removable Media and Incident Management Guide](privileged-user-backups-removable-media-and-incident-management-guide.md) provides information that privileged users should follow to reduce the impact of a security incident, and understand how they should respond.
-   The [Configuration, Patching and Change Management Guide](privileged-user-configuration-patching-and-change-management-guide.md) provides privileged users with guidance to ensure that systems are configured securely, that change is managed correctly, and that systems are patched regularly.

## Management of privileged user accounts

Privileged user accounts have a high degree of risk associated with them due to the control that they give the privileged user, hence they must be treated with great care. To reduce the risk of a data breach on the MoJ systems, access rights must be managed in the following ways.

-   Privileged user accounts should only be created for users with a genuine business need, and only for the duration that the business need exists.
-   Privileged access must be limited and granted in line with the principle of least privilege necessary to fulfil the required function.
-   The privileged accounts should be strictly controlled, and their number kept to the absolute minimum per system or app.
-   Privileged user passwords must be created in line with the MoJ's [Password Guide](password-creation-and-authentication-guide.md).
-   The password for a privileged user account must not be re-used for another privileged user account or a normal user account.
-   Privileged user passwords must be deleted along with the account when a privileged user leaves the MoJ or changes role.
-   Multi Factor Authentication \(MFA\) must be used for privileged user accounts where possible. Refer to the [Password Guide](password-creation-and-authentication-guide.md) for further details.
-   Privileged user accounts must only be used when carrying out administrative tasks such as creating new user accounts or implementing software updates. At all other times a normal user account must be used, e.g. for tasks such as searching the internet and reading emails.
-   Privileged user accounts on depreciated systems must be reviewed quarterly by system owners for breach as aging systems frequently cannot be, or are not, patched leaving them vulnerable to take over.
-   Privileged users must not abuse the privileges they are given, such as circumventing controls put in place to protect the MoJ.

For further information on managing privileged user accounts refer to the [Privileged User Configuration, Patching and Change Management Guide](privileged-user-configuration-patching-and-change-management-guide.md).

## Resource monitoring

Privileged users are responsible for monitoring their systems to ensure that the system is operating effectively and providing the intended functionality. Privileged users should:

-   Define each system's Key Performance Indicators \(KPIs\), which can be used to ensure the systems are operating effectively.
-   Monitor and analyse data from the systems in order to observe malicious behaviour, and to minimise, or to prevent, system outages or slowdowns, examples being:
    -   For MoJ managed infrastructure:
        -   CPU usage.
        -   Disk usage.
        -   Memory consumption.
    -   For Cloud solutions:
        -   Access requests.
        -   Database monitoring.
        -   Monitoring storage resources and processes that are provisioned to virtual machines, services, databases, and applications.
        -   Virtual network monitoring.
-   Identify the root cause of excessive resource use and rectifying the issue when possible. If an issue cannot be rectified quickly, it should be reported to the system owner.
-   Notify the MoJ IT Service Desk if there is a suspected incident \(refer to the [contact details](#incidents-and-contact-details)\).

## Identification and authentication

Privileged users are responsible for managing user access to systems to enable effective access control to the MoJ's data and information. To support effective access controls, privileged users must:

-   Only create user accounts once authorisation has been received from that user's line manager.
-   Only grant permissions that are in line with the user's business role within the MoJ.
-   Review user account usage every 90 days. If an account is dormant, the privileged user must investigate its status and suspend the account if appropriate. Refer to the [Access Control Guide](access-control-guide.md) for details.
-   Disable all user and privileged user accounts when staff members leave the MoJ, or where the account is not required due to a change of role. Privileged users will be automatically notified by HR when access changes or revocations are required.
-   Retain a record of all authorised users, approvals, and changes of access rights and privileges for any network, system or application, for which privileged users are responsible.

## Mobile and home working

When working remotely, it is important that privileged users operate securely by:

-   Ensuring that they are not overlooked when working on administrative tasks.
-   Ensuring that they use the MoJ's Virtual private Network \(VPN\) to connect with MoJ systems when using Privileged user login details.
-   Using only MoJ issued equipment to connect to the MoJ estate, and to carry out MoJ business.

Access to the VPN requires 2 Factor Authentication \(2FA\). The [IT Security Policy](it-security-policy-overview.md) and [Remote Working](remote-working.md) guidance documents contain further information about Remote Working.

## Incidents and contact details

**Note:** If you work for an agency or ALB, refer to your local incident reporting guidance.

For help with incidents, including theft and loss, contact one of the following:

**Technology Service Desk** - including DOM1/Quantum, and Digital & Technology Digital Service Desk. Use one of the following two methods for contacting service desk:

-   Tel: 0800 917 5148
-   [MoJ Service Portal and Live Chat](https://mojprod.service-now.com/moj_sp)

**Note:** The previous `itservicedesk@justice.gov.uk` and `servicedesk@digital.justice.gov.uk` email addresses, and the Digital & Technology Digital Service Desk Slack channel \(`#digitalservicedesk`\), are no longer being monitored.

**HMPPS Information & security:**

-   Email: [informationmgmtsecurity@justice.gov.uk](mailto:informationmgmtsecurity@justice.gov.uk)
-   Tel: 0203 334 0324

For non-technology incidents, contact the MoJ Group Security Team: [mojgroupsecurity@justice.gov.uk](mailto:mojgroupsecurity@justice.gov.uk)

Contact the Data Protection Team for information on Data Protection Impact Assessments: [DataProtection@justice.gov.uk](mailto:DataProtection@justice.gov.uk)

If you are not sure who to contact, ask the Security Team:

-   Email: [security@justice.gov.uk](mailto:security@justice.gov.uk)
-   Slack: `#security`

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

