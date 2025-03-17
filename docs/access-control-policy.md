# Access Control Policy

This policy gives an overview of access control security principles and responsibilities within the Ministry of Justice \(MoJ\). It provides a summary of the policies and guides that apply to MoJ access management.

To help identify formal policy statements, each is prefixed with an identifier of the form: **POL.ACP.xxx**, where **xxx** is a unique ID number.

## Audience

This policy is aimed at:

<a name="technical-users"></a>

-   **Technical users**

    These are in-house MoJ Digital and Technology staff responsible for implementing controls throughout technical design, development, system integration, and operation. This includes DevOps, Software Developers, Technical Architects, and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI, and Knowledge \(EPICK\) Team.

<a name="service-providers"></a>

-   **Service Providers**

    Defined as any other MoJ business group, agency, contractor, IT supplier, and partner who in any way designs, develops or supplies services \(including processing, transmitting and storing data\), for or on behalf of the MoJ.

<a name="general-users"></a>

-   **General users**

    All other staff working for the MoJ.


"All MoJ users" refers to General users, Technical users, and Service Providers, as defined previously.

## Policy Sections

This policy aligns to industry standards and frameworks, and is divided into four security categories \(and subsections describing the controls\) addressing:

1.  Business Requirements of Access Controls.
2.  System and Application Access Controls.
3.  User Access Management.
4.  User Responsibilities.

## Best Practice Framework - IAAA

Identification, Authentication, Authorisation, and Accounting \(IAAA\) are the core principles of an Access Control Policy. The principles apply to all security categories described in this policy, as follows:

<a name="identification"></a>

-   **Identification**

    **POL.ACP.001:** The MoJ **shall** provide a unique ID that is assigned, named, and linked to a private account, for each user.

<a name="authentication"></a>

-   **Authentication**

    **POL.ACP.002:** To access MoJ systems, users **shall** authenticate themselves.

<a name="authorisation"></a>

-   **Authorisation**

    **POL.ACP.003:** Specifying access rights, privileges, and resources to users **shall** be granted in line with the principle of least privilege.

<a name="accounting"></a>

-   **Accounting**

    **POL.ACP.004:** Successful and unsuccessful attempts to access systems and user activities conducted while using systems **shall** be recorded in logs.


**Note:** If any of the controls within this policy cannot be applied, they are considered an exception to be assessed for inclusion within a risk register.

## Business Requirements of Access Control

The MoJ's business or strategic requirements limit access to MoJ information and information processing facilities, as described in the following subsections.

### Access Control Policy

**POL.ACP.005:** This access control policy **shall** be established and maintained, based on business and information security requirements, to inform associated standards and guidance, for all users.

**POL.ACP.006:** The policy **shall** also follow the additional principles of:

-   "Need-to-know".
-   Non-repudiation of user actions.
-   Least privilege.
-   User access management.

### Access to Networks and network services

This subsection aligns to the principle of least access, to protect a network and network services which are covered in other areas of this policy, specifically:

-   Authorisation procedures for showing who \(role-based\) is allowed to access what, and when. Refer to subsections [Information Access Restrictions](#information-access-restrictions) and [Management of Privileged Access Rights](#management-of-privileged-access-rights).
-   Management controls and procedures to prevent access and real-time monitoring. Refer to the categories called [System and Application Access Control](#system-and-application-access-control) and [User Access Management](#user-access-management), with monitoring covered in the subsections called [Password Management System](#password-management-system) and [Management of Privileged Access Rights](#management-of-privileged-access-rights).

## System and Application Access Control

**POL.ACP.007:** The MoJ **shall** strive to prevent unauthorised access to systems and applications, as described in the following subsections.

### Information Access Restrictions

**POL.ACP.008:** Access to information and application system functions **shall** be restricted by following access control policies and procedures.

**POL.ACP.009:** In particular, System Designers and Administrators **shall** use adequate authentication techniques to identify with confidence user access to their system or data, using the principle of "least privilege". Refer to the guidance on [Authorisation](authorisation.md) for more detail.

### Secure Log-on Procedures

**POL.ACP.010:** Where required by the access control policy, access to systems and applications **shall** be controlled by a secure log-on procedure, including the following points:

-   **POL.ACP.011:** Multi-user \(MU\) accounts **shall** be managed carefully using PAM or a Bastion server, to avoid accountability type security risks. Refer to the [Multi-user Accounts and Public-Facing Service Accounts](multi-user-accounts-and-public-facing-service-accounts-guide.md) guidance.
-   **POL.ACP.012:** Front-end users accessing the MoJ's public services **shall** authenticate via the GOV.UK Verify Service. Refer to the [User Facing Services](passwords.md) guidance.
-   **POL.ACP.013:** System Designers for internal systems **shall** use the MoJ's single sign-on \(SSO\) solution to authenticate via an Identity and Access system.
-   **POL.ACP.014:** Passwords **shall not** be stored or transmitted over the network in clear text, nor be protected with encryption that has known security weaknesses. Refer to the [Password Management Guide](password-management-guide.md).

### Password Management System

**POL.ACP.015:** The MoJ's password management systems **shall** be interactive, ensure quality passwords are used, and **shall** store and transmit passwords in a protected form, specifically:

-   **POL.ACP.016:** Systems **shall** support MoJ password requirements that are provisioned and maintained by System Administrators.
-   **POL.ACP.017:** System Administrators **shall** always have time-bound administrative sessions, which **shall** be protected using [Multi-Factor Authentication \(MFA\)](multi-factor-authentication-mfa-guide.md).

    **POL.ACP.018:** The system **shall** regularly monitor, review, and revoke these sessions when no longer required.

-   **POL.ACP.019:** Strong passwords, separate and unique for each account or service, **shall** be created and maintained by all users. Refer to the [Password Management Guide, Roles and Responsibilities section](password-management-guide.md), [Passwords](passwords.md) and [CyberAware advice](https://www.ncsc.gov.uk/cyberaware/home#action-2).
-   **POL.ACP.020:** Users **shall** change a password initially received by a system or support team before carrying out MoJ tasks. Refer to [Passwords](passwords.md).
-   **POL.ACP.021:** Password history and blocking of commonly guessed passwords **shall** be enabled in a system. Refer to the [Password Creation and Authentication Guide](password-creation-and-authentication-guide.md).
-   Regular password change is not required, as it is an [outdated and ineffective practice](https://www.ncsc.gov.uk/blog-post/your-password-expiry-policy-may-have-reached-its-expiry-date).
-   **POL.ACP.022:** Password managers or vaults used at the MoJ **shall** align to industry standards to securely store and transmit passwords in a protected form. Refer to [Password Managers](password-managers.md) and [Password Vaults and Managers](password-storage-and-management-guide.md).

**Note:** Contact the [Security team](#contact-details) if you have specialised needs when selecting or using a storage tool.

### Access Control to Program Source Code

-   **POL.ACP.023:** When coding in the open, MoJ Technical users and Service Providers **shall** follow coding best practices and keep code separate from configuration and data.

## User Access Management

User access management ensures authorised user access, and prevents unauthorised access to systems and services. These are described in the following subsections.

### User Registration and de-registration

**POL.ACP.024:** A formal user registration and de-registration process **shall** be implemented to enable the assignment of access rights, specifically:

-   **POL.ACP.025:** Multi-User \(MU\) or shared ID accounts **shall** only be used directly if there is no alternative. Refer to [Multi-user Accounts and Public-Facing Service Accounts](multi-user-accounts-and-public-facing-service-accounts-guide.md).
-   **POL.ACP.026:** The identity of the new user **shall** be confirmed. For all MoJ staff members, this is established as part of pre-employment screening and vetting using the Baseline Personnel Security Standard \(BPSS\), which is the joint responsibility of HR \(performed on their behalf by Shared Services Connected Ltd\), and a line manager. Refer to [Security Vetting](https://intranet.justice.gov.uk/guidance/hr/recruitment/security-vetting/) and the [BPSS](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/714002/HMG_Baseline_Personnel_Security_Standard_-_May_2018.pdf) information.
-   **POL.ACP.027:** The hiring line manager **shall** submit a ServiceNow [Order IT](https://mojprod.service-now.com/moj_sp?id=moj_sc_landing) role-based access request on behalf of the new user. For example, a list of Role-based access control \(RBAC\) groups or applications.
-   **POL.ACP.028:** The hiring manager's line manager \(or the budget holder\) **shall** authorise the application for user registration within ServiceNow [My Approvals](https://mojprod.service-now.com/moj_sp?id=moj_my_approvals). This confirms the user's identity, and hence access rights, are correct.
-   **POL.ACP.029:** Confirmation of the Clearance Level **shall** be initiated by a line manager, and carried out by [United Kingdom Security Vetting](https://www.gov.uk/government/organisations/united-kingdom-security-vetting/about) \(UKSV\) to recruit new staff \(civil servants, armed forces and temporary staff\), or staff changing their MoJ roles. Refer to [Clearance Levels](https://www.gov.uk/government/publications/united-kingdom-security-vetting-clearance-levels/national-security-vetting-clearance-levels).

**Note:** For Contractors or Agency staff, HR/SSCL do not seek assurance that the BPSS check has been completed; instead, the responsibility is with the line manager, via the receipt of the Baseline Personnel Security Verification Record Form, as described [here](https://intranet.justice.gov.uk/guidance/security/personnel-security-prior-to-employment/).

**POL.ACP.030:** De-registration of users **shall** be at the request of line managers and follow the JML process found [here](https://intranet.justice.gov.uk/guidance/hr/end-change-of-employment/). The following controls need to be adopted for leavers:

-   **POL.ACP.031:** Line Managers **shall** authorise account removal. The associated leaver's process can be found on the [HR intranet page](https://intranet.justice.gov.uk/guidance/hr/end-change-of-employment/).
-   **POL.ACP.032:** User accounts and their access rights **shall** be removed once an individual has left the organisation or no longer requires access to the system\(s\).
-   **POL.ACP.033:** Existing user accounts **shall** be reviewed every three months by the System Administrator to confirm those not used in the last three months, and then with MoJ HR to approve accounts for removal.
-   **POL.ACP.034:** Remote access authentication token usage **shall** be reviewed by the System Administrator every three months, and when a token is identified as unused in the last three months, the account disabled.
-   **POL.ACP.035:** Assigned User roles and privileges **shall** be reviewed every six to twelve months, and those no longer required removed.

For further information on user de-registration, refer to the [MoJ Enterprise Access Control Policy](enterprise-access-control-policy.md).

### User Access Provisioning

**POL.ACP.036:** A formal user access provisioning process **shall** be implemented to assign or revoke access rights for all users to all systems and services. Specifically for MoJ, this includes:

-   **POL.ACP.037:** The security clearance required by staff to access specific account types **shall** align to the [MoJ's UK security clearance levels](https://www.gov.uk/government/publications/united-kingdom-security-vetting-clearance-levels/national-security-vetting-clearance-levels), as per requirements such as [segregation of duties](https://security-guidance.service.justice.gov.uk/access-control-guide/#segregation-of-duties). Refer to minimum user clearance level guidance, by contacting [Security team](mailto:security@justice.gov.uk).
-   **POL.ACP.038:** MFA **shall** be used to ensure access to MoJ Information, and is only granted to users once their identity is confirmed. Refer to the [Multi-Factor Authentication](multi-factor-authentication-mfa-guide.md) guidance.
-   **POL.ACP.039:** All MoJ data access **shall** employ adequate authentication techniques to identify the system or user with confidence, where that system or user requires access to MoJ systems or data. Refer to the [Authentication](authentication.md) guidance.
-   **POL.ACP.040:** System Administrators **shall** maintain the MoJ's systems' security, with failure to comply compromising the organisational infrastructure.
-   **POL.ACP.041:** System Administrators **shall** maintain an active list of all active and suspended users, and maintain their access control to services or applications.
-   **POL.ACP.042:** System Administrators **shall**, on a minimum quarterly basis \(rotated with other Admins\), conduct an account audit to check:
    -   Any escalation of privileges from non-administrator to administrator.
    -   Any forwarding of email accounts.
    -   Any taking ownership of user accounts.
-   **POL.ACP.043:** A user leaving **shall** move their data to a shared folder if needed for retention. Refer to the [Account Deletion](https://mojprod.service-now.com/moj_sp?id=sc_cat_item&sys_id=c195e78edb73e7441b4ffc45ae9619f2) process.
-   **POL.ACP.044:** If anyone with an MoJ account leaves the organisation, system administrators **shall** retrieve the user's equipment and suspend the account.
-   **POL.ACP.045:** If a user leaving has not returned all MoJ assets, the line manager **shall** initially contact the IT Service Desk via [Live Chat](https://mojprod.service-now.com/moj_sp), or Telephone \(0800 917 5148\), and raise a security incident, with the following [form](https://intranet.justice.gov.uk/documents/2015/04/security-incident-report-form.xls) completed and emailed to [security@justice.gov.uk](mailto:security@justice.gov.uk). Refer to the [Leavers checklist for managers](https://intranet.justice.gov.uk/documents/2015/04/leavers-checklist-for-managers.docx) for more information.

**Note:** The previous points are covered by the [System Administrators](system-users-and-application-administrators.md) guidance.

### Management of Privileged Access Rights

**POL.ACP.046:** The allocation and use of privileged access rights **shall** be restricted and controlled using the MoJ's Access Control Policy. This includes:

-   **POL.ACP.047:** Users **shall** only use their system administrator account when elevated privileges are required.
-   **POL.ACP.048:** MFA **shall** be used with privileged accounts, including access to enterprise-level social media accounts.
-   **POL.ACP.049:** Default passwords **shall** be managed securely and safely by privileged account users, described in the [Password Manager](password-managers.md) guidance. Refer to the [Privileged Account Management](privileged-account-management-guide.md) guidance for more information.
-   **POL.ACP.050:** All users with ownership and use of privileged accounts **shall** have these secured, controlled, monitored, and audited by System Administrators every month using an industry-standard Privileged Access Management \(PAM\) tool. Refer to the [Privileged Account Management](privileged-account-management-guide.md) guidance for more information.

**Note:** Privileged access rights provide a Technical user or a Service Provider with an enhanced level of access to the MoJ's information systems, compared to a General user. This can include the authorisation to configure networks or systems, provision and configure accounts and cloud instances, and so on.

### Management of Secret Authentication Information of Users

**POL.ACP.051:** The allocation of secret authentication information, such as passwords or encryption keys, **shall** be controlled through formal management:

-   **POL.ACP.052:** User password management **shall** be configured, so a password is changed after the initial log-on and invalid if not used in a specified time. Refer to the [Passwords](passwords.md) guidance.
-   **POL.ACP.053:** System Administrators and systems **shall** never send passwords by email, as it is an unsecured channel.

    **POL.ACP.054:** Instead, users **shall** receive a time-limited password-reset link or code to their registered email address or phone number. Refer to the Government guidance "[Send a link to trigger password resets](https://design-system.service.gov.uk/patterns/passwords/)".


### Review of User Access Rights

**POL.ACP.055:** System Administrators **shall** review users' access rights at regular intervals:

-   The review of user access rights is covered in this policy under [User Access Provisioning](#user-access-provisioning).

### Removal or Adjustment of Access Rights

**POL.ACP.056:** All employees and external party user's access rights to information and information processing facilities **shall** be removed upon termination of their employment, contract or agreement, or adjusted when changing their role:

-   The removal or adjustment of user access rights is covered in this policy under [User Access Provisioning](#user-access-provisioning).

## User Responsibilities

Users are required to follow the MoJ's practices in the use of secret authentication. This is described in the following subsection.

### Use of secret authentication information

-   **POL.ACP.057:** All users **shall** follow the MoJ's password policy, as referenced in the [Password Management System](#password-management-system), and the associated tools referenced in the [Secure Log-on Procedures](#secure-log-on-procedures).

## Enforcement

-   This policy is enforced by lower-level policies, standards, procedures, and guidance.
-   Non-conformance with this policy could result in disciplinary action per the department's disciplinary procedures. This could result in penalties up to and including dismissal. If an employee commits a criminal offence, they may also be prosecuted. In such cases, the department will always co-operate with the relevant authorities and provide appropriate evidence.

## Incidents

**Note:** If you work for an agency or ALB, refer to your local incident reporting guidance.

**Security Team**

-   Email: [security@justice.gov.uk](mailto:security@justice.gov.uk)
-   Slack: `#security`

## Contact and Feedback

For any further questions or advice relating to security, or for any feedback or suggestions for improvement, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).

