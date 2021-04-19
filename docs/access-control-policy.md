# Access Control Policy

## Introduction

This policy gives an overview of access control security principles and responsibilities within the Ministry of Justice \(MoJ\). It provides a summary of the MoJ's related access management policies and guides.

To help identify formal policy statements, each is prefixed with an identifier of the form: `POLACPxxx`, where xxx is a unique ID number.

## Audience

This policy is aimed at:

-   **Technical users**

    These are in-house MoJ Digital and Technology staff responsible for implementing controls throughout technical design, development, system integration, and operation. This includes DevOps, Software Developers, Technical Architects, and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI, and Knowledge \(EPICK\) Team.

-   **Service Providers**

    Defined as any other MoJ business group, agency, contractor, IT supplier, and partner who in any way designs, develops or supplies services \(including processing, transmitting and storing data\), for or on behalf of the MoJ.

-   **General users**

    All other staff working for the MoJ.


“All MoJ users” refers to General users, Technical users, and Service Providers, as defined above.

## Policy Sections

This policy aligns to industry standards and frameworks, and is divided into four security categories \(and subsections describing the controls\) addressing:

1.  Business Requirements of Access Controls.
2.  System and Application Access Controls.
3.  User Access Management.
4.  User Responsibilities.

## Best Practice Framework - IAAA

Identification, Authentication, Authorisation, and Accounting \(IAAA\) are the core principles of an Access Control Policy. The principles apply to all security categories described in this policy, as follows:

-   **Identification**

    `POLACP001:` The MoJ **MUST** provide a unique ID that is assigned, named, and linked to a private account, for each user.

-   **Authentication**

    `POLACP002:` To access MoJ systems, users **MUST** authenticate themselves.

-   **Authorisation**

    `POLACP003:` Specifying access rights, privileges, and resources to users **MUST** be granted in line with the principle of least privilege.

-   **Accounting**

    `POLACP004:` Successful and unsuccessful attempts to access systems and user activities conducted while using systems **MUST** be recorded in logs.


**Note:** If any of the controls within this policy cannot be applied, they are considered an exception to be assessed for inclusion within a risk register.

## Business Requirements of Access Control

The MoJ's business or strategic requirements limit access to MoJ information and information processing facilities, as described in the following subsections.

### Access Control Policy

`POLACP005:` This access control policy **MUST** be established and maintained, based on business and information security requirements, to inform associated standards and guidance, for all users.

`POLACP006:` The policy **MUST** also follow the additional principles of:

-   “Need-to-know”.
-   Non-repudiation of user actions.
-   Least privilege.
-   User access management.

### Access to Networks and network services

This subsection aligns to the principle of least access, to protect a network and network services which are covered in other areas of this policy, specifically:

-   Authorisation procedures for showing who \(role-based\) is allowed to access what, and when. See subsections [Information Access Restrictions](#information-access-restrictions) and [Management of Privileged Access Rights](#management-of-privileged-access-rights).
-   Management controls and procedures to prevent access and real-time monitoring. See the categories called [System and Application Access Control](#system-and-application-access-control) and [User Access Management](#user-access-management), with monitoring covered in the subsections called [Password Management System](#password-management-system) and [Management of Privileged Access Rights](#management-of-privileged-access-rights).

## System and Application Access Control

`POLACP007:` The MoJ **MUST** strive to prevent unauthorised access to systems and applications, as described in the following subsections.

### Information Access Restrictions

`POLACP008:` Access to information and application system functions **MUST** be restricted by following access control policies and procedures.

`POLACP009:` In particular, System Designers and Administrators **MUST** use adequate authentication techniques to identify with confidence user access to their system or data, using the principle of “least privilege”. See the guidance on [Authorisation](Authorisationauthorisation.dita) for more detail.

### Secure Log-on Procedures

`POLACP010:` Where required by the access control policy, access to systems and applications **MUST** be controlled by a secure log-on procedure, including the following points:

-   `POLACP011:` Multi-user \(MU\) accounts **MUST** be managed carefully using PAM or a Bastion server, to avoid accountability type security risks. See the [Multi-user Accounts and Public-Facing Service Accounts](multi-user-accounts-and-public-facing-service-accounts-guide.md) guidance.
-   `POLACP012:` Front-end users accessing the MoJ's public services **MUST** authenticate via the GOV.UK Verify Service. See the [User Facing Services](passwords.md#) guidance.
-   `POLACP013:` System Designers for internal systems **MUST** use the MoJ's single sign-on \(SSO\) solution to authenticate via an Identity and Access system.
-   `POLACP014:` Passwords **MUST NOT** be stored or transmitted over the network in clear text, nor be protected with encryption that has known security weaknesses. See the [Password Management Guide](password-management-guide.md#).

### Password Management System

`POLACP015:` The MoJ's password management systems **MUST** be interactive, ensure quality passwords are used, and **MUST** store and transmit passwords in a protected form, specifically:

-   `POLACP016:` Systems **MUST** support MoJ password requirements that are provisioned and maintained by System Administrators.
-   `POLACP017:` System Administrators **MUST** always have time-bound administrative sessions, which **MUST** be protected using [Multi-Factor Authentication \(MFA\)](multi-factor-authentication-mfa-guide.md).

    `POLACP018:` The system **MUST** regularly monitor, review, and revoke these sessions when no longer required.

-   `POLACP019:` Strong passwords, separate and unique for each account or service, **MUST** be created and maintained by all users. See the [Password Management Guide Roles and Responsibilities section](password-management-guide.md#), [Passwords](passwords.md#) and [CyberAware advice](https://www.ncsc.gov.uk/cyberaware/home#action-2).
-   `POLACP020:` Users **MUST** change a password initially received by a system or support team before carrying out MoJ tasks. See [Passwords](passwords.md#).
-   `POLACP021:` Password history and blocking of commonly guessed passwords **MUST** be enabled in a system. See the [Password Creation and Authentication Guide](password-creation-and-authentication-guide.md#).
-   Regular password change is not required, as it is an [outdated and ineffective practice](https://www.ncsc.gov.uk/blog-post/your-password-expiry-policy-may-have-reached-its-expiry-date).
-   `POLACP022:` Password managers or vaults used at the MoJ **MUST** align to industry standards to securely store and transmit passwords in a protected form. See [Password Managers](password-managers.md) and [Password Vaults and Managers](password-storage-and-management-guide.md#).

**Note:** Contact the [Cyber Assistance Team](#contact-details) if you have specialised needs when selecting or using a storage tool.

### Access Control to Program Source Code

-   `POLACP023:` When coding in the open, MoJ Technical users and Service Providers **MUST** follow coding best practices and keep code separate from configuration and data.

## User Access Management

User access management ensures authorised user access, and prevents unauthorised access to systems and services. These are described in the following subsections.

### User Registration and de-registration

`POLACP024:` A formal user registration and de-registration process **MUST** be implemented to enable the assignment of access rights, specifically:

-   `POLACP025:` Multi-User \(MU\) or shared ID accounts **MUST** only be used directly if there is no alternative. See [Multi-user Accounts and Public-Facing Service Accounts](multi-user-accounts-and-public-facing-service-accounts-guide.md).
-   `POLACP026:` The identity of the new user **MUST** be confirmed. For all MoJ staff members, this is established as part of pre-employment screening and vetting using the Baseline Personnel Security Standard \(BPSS\), which is the joint responsibility of HR \(performed on their behalf by Shared Services Connected Ltd\), and a line manager. See [Security Vetting](https://intranet.justice.gov.uk/guidance/hr/recruitment/security-vetting/) and the [BPSS](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/714002/HMG_Baseline_Personnel_Security_Standard_-_May_2018.pdf) information.
-   `POLACP027:` The hiring line manager **MUST** submit a [ServiceNow Order](https://mojprod.service-now.com/moj_sp?id=moj_sc_landing) IT role-based access request on behalf of the new user. For example, a list of Role-based access control \(RBAC\) groups or applications.
-   `POLACP028:` The hiring manager's line manager \(or the budget holder\) **MUST** authorise the application for user registration within ServiceNow [My Approvals](https://mojprod.service-now.com/moj_sp?id=moj_my_approvals). This confirms the user's identity, and hence access rights, are correct.
-   `POLACP029:` Confirmation of the Clearance Level **MUST** be initiated by a line manager, and carried out by [United Kingdom Security Vetting](https://en.wikipedia.org/w/index.php?title=United_Kingdom_Security_Vetting&action=edit&redlink=1) \(UKSV\) to recruit new staff \(civil servants, armed forces and temporary staff\), or staff changing their MoJ roles. See [Clearance Levels](https://www.gov.uk/government/publications/united-kingdom-security-vetting-clearance-levels/national-security-vetting-clearance-levels).

**Note:** For Contractors or Agency staff, HR/SSCL do not seek assurance that the BPSS check has been completed; instead, the responsibility is with the line manager, via the receipt of the Baseline Personnel Security Verification Record Form, as described [here](https://intranet.justice.gov.uk/guidance/security/personnel-security-prior-to-employment/).

`POLACP030:` De-registration of users **MUST** be at the request of line managers and follow the JML process found [here](https://intranet.justice.gov.uk/guidance/hr/end-change-of-employment/). The following controls need to be adopted for leavers:

-   `POLACP031:` Line Managers **MUST** authorise account removal. The associated leaver's process can be found on the [HR intranet page](https://intranet.justice.gov.uk/guidance/hr/end-change-of-employment/).
-   `POLACP032:` User accounts and their access rights **MUST** be removed once an individual has left the organisation or no longer requires access to the system\(s\).
-   `POLACP033:` Existing user accounts **MUST** be reviewed every three months by the System Administrator to confirm those not used in the last three months, and then with MoJ HR to approve accounts for removal.
-   `POLACP034:` Remote access authentication token usage **MUST** be reviewed by the System Administrator every three months, and when a token is identified as unused in the last three months, the account disabled.
-   `POLACP035:` Assigned User roles and privileges **MUST** be reviewed every six to twelve months, and those no longer required removed.

For further information on user de-registration, see the [MoJ Enterprise Access Control Policy](enterprise-access-control-policy.md).

### User Access Provisioning

`POLACP036:` A formal user access provisioning process **MUST** be implemented to assign or revoke access rights for all users to all systems and services. Specifically for MoJ, this includes:

-   `POLACP037:` The security clearance required by staff to access specific account types **MUST** align to the [MoJ's UK security clearance levels](https://www.gov.uk/government/publications/united-kingdom-security-vetting-clearance-levels/national-security-vetting-clearance-levels), as per requirements such as [segregation of duties](https://ministryofjustice.github.io/security-guidance/access-control-guide/#segregation-of-duties). See [Minimum User Clearance Levels](minimum-user-clearance-requirements-guide.md) guidance.
-   `POLACP038:` MFA **MUST** be used to ensure access to MoJ Information, and is only granted to users once their identity is confirmed. See the [Multi-Factor Authentication](multi-factor-authentication-mfa-guide.md) guidance.
-   `POLACP039:` All MoJ data access **MUST** employ adequate authentication techniques to identify the system or user with confidence, where that system or user requires access to MoJ systems or data. See the [Authentication](authentication.md) guidance.
-   `POLACP040:` System Administrators **MUST** maintain the MoJ's systems' security, with failure to comply compromising the organisational infrastructure.
-   `POLACP041:` System Administrators **MUST** maintain an active list of all active and suspended users, and maintain their access control to services or applications.
-   `POLACP042:` System Administrators **MUST**, on a minimum quarterly basis \(rotated with other Admins\), conduct an account audit to check:
    -   Any escalation of privileges from non-administrator to administrator.
    -   Any forwarding of email accounts.
    -   Any taking ownership of user accounts.
-   `POLACP043:` A user leaving **MUST** move their data to a shared folder if needed for retention. See the [Account Deletion](https://mojprod.service-now.com/moj_sp?id=sc_cat_item&sys_id=c195e78edb73e7441b4ffc45ae9619f2) process.
-   `POLACP044:` If anyone with an MoJ account leaves the organisation, system administrators **MUST** retrieve the user's equipment and suspend the account.
-   `POLACP045:` If a user leaving has not returned all MoJ assets, the line manager **MUST** initially contact the IT Service Desk via [Live Chat](https://mojprod.service-now.com/moj_sp), or Telephone \(0800 917 5148\), and raise a security incident, with the following [form](https://intranet.justice.gov.uk/documents/2015/04/security-incident-report-form.xls) completed and emailed to [security@justice.gov.uk](mailto:security@justice.gov.uk). See the [Leavers checklist for managers](https://intranet.justice.gov.uk/documents/2015/04/leavers-checklist-for-managers.docx) for more information.

**Note:** The above points are covered by the [System Administrators](system-users-and-application-administrators.md) guidance.

### Management of Privileged Access Rights

`POLACP046:` The allocation and use of privileged access rights **MUST** be restricted and controlled using the MoJ's Access Control Policy. This includes:

-   `POLACP047:` Users **MUST** only use their system administrator account when elevated privileges are required.
-   `POLACP048:` MFA **MUST** be used with privileged accounts, including access to enterprise-level social media accounts.
-   `POLACP049:` Default passwords **MUST** be managed securely and safely by privileged account users, described in the [Password Manager](password-managers.md) guidance. See the [Privileged Account Management](privileged-account-management-guide.md) guidance for more information.
-   `POLACP050:` All users with ownership and use of privileged accounts **MUST** have these secured, controlled, monitored, and audited by System Administrators every month using an industry-standard Privileged Access Management \(PAM\) tool. See the [Privileged Account Management](privileged-account-management-guide.md) guidance for more information.

**Note:** Privileged access rights provide a Technical user or a Service Provider with an enhanced level of access to the MoJ's information systems, compared to a General user. This can include the authorisation to configure networks or systems, provision and configure accounts and cloud instances, and so on.

### Management of Secret Authentication Information of Users

`POLACP051:` The allocation of secret authentication information, such as passwords or encryption keys, **MUST** be controlled through formal management:

-   `POLACP052:` User password management **MUST** be configured, so a password is changed after the initial log-on and invalid if not used in a specified time. See the [Passwords](passwords.md#) guidance.
-   `POLACP053:` System Administrators and systems **MUST** never send passwords by email, as it is an unsecured channel.

    `POLACP054:` Instead, users **MUST** receive a time-limited password-reset link or code to their registered email address or phone number. See the Government guidance “[Send a link to trigger password resets](https://design-system.service.gov.uk/patterns/passwords/)”.


### Review of User Access Rights

`POLACP055:` System Administrators **MUST** review users' access rights at regular intervals:

-   The review of user access rights is covered in this policy under [User Access Provisioning](#user-access-provisioning).

### Removal or Adjustment of Access Rights

`POLACP056:` All employees and external party user's access rights to information and information processing facilities **MUST** be removed upon termination of their employment, contract or agreement, or adjusted when changing their role:

-   The removal or adjustment of user access rights is covered in this policy under [User Access Provisioning](#user-access-provisioning).

## User Responsibilities

Users are required to follow the MoJ's practices in the use of secret authentication. This is described in the following subsections.

### Use of secret authentication information

-   `POLACP057:` All users **MUST** follow the MoJ's password policy, as referenced in the [Password Management System](#password-management-system), and the associated tools referenced in the [Secure Log-on Procedures](#secure-log-on-procedures).

## Enforcement

-   This policy is enforced by lower-level policies, standards, procedures, and guidance.
-   Non-conformance with this policy could result in disciplinary action per the department's disciplinary procedures. This could result in penalties up to and including dismissal. If an employee commits a criminal offence, they may also be prosecuted. In such cases, the department will always cooperate with the relevant authorities and provide appropriate evidence.

## Incidents

**Note:** If you work for an agency or ALB, refer to your local incident reporting guidance.

**Operational Security Team**

-   Email: [OperationalSecurityTeam@justice.gov.uk](mailto:OperationalSecurityTeam@justice.gov.uk)
-   Slack: `#security`

## Contact details

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for security advice, contact the Cyber Assistance Team [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

