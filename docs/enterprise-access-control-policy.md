# Enterprise Access Control Policy

All Ministry of Justice \(MoJ\) staff \(including contractors and agency staff\) are entitled to be granted access to the information which is required for their work, subject to their level of clearance and employment status.

Access control mechanisms provide the ability for MoJ IT systems to control the levels of access granted to an individual User or defined groups of individual Users. This section outlines the process for managing User access to MoJ IT systems starting from when a User is initially registered through to the revocation of access rights and removal of their User account.

## Legacy information

**Note:** This document is Legacy IA Policy material. It is under review and likely to be withdrawn or substantially revised soon. Before using this content for a project, contact [security@justice.gov.uk](mailto:security@justice.gov.uk).

**Note:** This document might refer to several organisations, information sources, or terms that have been replaced or updated, as follows:

-   CESG \(Communications-Electronics Security Group\), refer to the National Cyber Security Centre \(NCSC\), contact [security@justice.gov.uk](mailto:security@justice.gov.uk).
-   CINRAS \(Comsec Incident Notification Reporting and Alerting Scheme\), refer to the NCSC, contact [security@justice.gov.uk](mailto:security@justice.gov.uk).
-   ComSO \(Communications Security Officer\), contact the Chief Information Security Officer \(CISO\) \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   **Confidential**, an older information classification marking, refer to [Information Classification and Handling Policy](information-classification-and-handling-policy.md).
-   CPNI \([Centre for the Protection of the National Infrastructure](https://www.cpni.gov.uk/)\), contact the CISO \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   DSO \(Departmental Security Officer\), contact the Chief Security Officer \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   GPG6 \(Good Practice Guide 6: Outsourcing and Offshoring: Managing the Security Risks\), refer to the NCSC, contact [security@justice.gov.uk](mailto:security@justice.gov.uk).
-   IS1 \(HMG Infosec Standard 1 Technical Risk Assessment\), refer to the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   IS2 \(HMG Infosec Standard 2 Information Risk Management\), refer to the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   IS4 \(HMG Infosec Standard 4 Communications Security and Cryptography\), refer to the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   IS6 \(HMG Infosec Standard 6 Protecting Personal Data and Managing Information Risk\), refer to the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   ITSO \(Information Technology Security Officer\), contact the CISO \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   **Restricted**, an older information classification marking, refer to [Information Classification and Handling Policy](information-classification-and-handling-policy.md).
-   SPF \([Security Policy Framework](https://www.gov.uk/government/publications/security-policy-framework)\), refer to the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security), contact [security@justice.gov.uk](mailto:security@justice.gov.uk).

## User and Information Access management

Access control is primarily about enforcing three information security principles:

-   The *'need-to-know'* principle – restricting access to information based on a business requirement.

-   *Non-repudiation* of User actions –holding a User accountable for their actions on an IT system.

-   The *'least privilege'* principle – assigning the least number of privileges required to fulfil their work.


At a high level, access control in MoJ is based on Role Based Access Control \(RBAC\). Each user is assigned a role \(or set of roles\) and access to a piece of information is granted on a per role basis. In general, information will either be subject to RBAC or classified as open access \(for example, a HR policy document made available on the MoJ intranet\).

Information made available on an open access basis \(i.e. not subject to any RBAC restrictions\) must be treated as an exception to general access control rules. It is important to ensure any information made available in this way has been validated by the Information Asset Owner \(IAO\) to ensure that the information does not have 'need-to-know' constraints that impede it's sharing beyond a defined RBAC group \(refer [here](#it-system-owner-information-asset-owner-responsibilities)for further details on the role of the IAO\).

## Management of User access control

The following diagram depicts the 4 stage management lifecycle for managing user access control.

![A diagram of the 4 stage management lifecycle for managing user access control. A the top is a box with the label "User registration". An arrow descends from the bottom of the box, and enters the top of a second box, located in the middle of the diagram, which has the label "Review of user access rights". An arrow descends from the bottom of the second box, and enter the top of a third box, located at the bottom of the diagram, which has the label "Account removal". Returning to the second box in the middle of the diagram, there is an arrow leaving the right hand side of the box and connecting into the left hand side of a fourth box, located on the right hand side of the diagram. This third box has the label "Amend user access rights". An arrow leaves the left hand side of the fourth box, and connects back into the right hand side of the second box, forming a loop between the second and fourth boxes.](images/enterprise-access-control-policy.png)

The rest of this section describes each of the 4 stages and outlines what activities are required.

**Note:** This lifecycle aligns with the MoJ HR processes for new joiners \(see: [https://intranet.justice.gov.uk/guidance/hr/induction/](https://intranet.justice.gov.uk/guidance/hr/induction/) \) and leavers \(see: [https://intranet.justice.gov.uk/guidance/hr/end-change-of-employment/](https://intranet.justice.gov.uk/guidance/hr/end-change-of-employment/) \).

### User registration and account creation

The following activities must be undertaken for each new User registration:

-   The identity of the new User must be confirmed – for an MoJ member of staff this is confirmed by MoJ HR;

-   The access rights required must be supplied \(for example, the list of RBAC groups and/or applications\);

-   Confirmation of clearance level \(refer [here](#minimum-user-clearance-requirements) for further details\);

-   The application for User registration must be authorised by a MoJ senior manager.

    **Note:** This authorisation is used as confirmation of the Users identity and the access rights requested are correct.


In general, individuals who are MoJ staff \(including contractors and agency staff\) will be provisioned with a User account and a number of roles applicable to the nature of their work so that they can access the relevant MoJ IT systems, application and information. Temporary use of a MoJ IT system may be permitted where a specific business need exists \(e.g. to allow an external trainer to train MoJ staff in a new application\) subject to clearance checks and a Non-Disclosure Agreement \(NDA\). A MoJ senior manager must assume total responsibility for the actions undertaken by that temporary User while they are using a MoJ IT system using a temporary account.

#### Minimum user clearance requirements

Most MoJ IT systems operate at IL3 where information with a protective marking of REST\* can be processed. As these systems process HMG protectively marked data, Users must attain a certain clearance level before they can be granted access rights, the exact level depends on the type of access rights required and job role.

For the purposes of this standard, access rights have been broken down into three User account types. Table 1 provide a description for each type and the minimum clearance required.

|User account type|Description|Minimum Clearance Required|
|-----------------|-----------|--------------------------|
|Normal User|Include all Users with entry-level access; includes read/write and read-only Users.|BPSS|
|Application Administrator / Privileged User|Typically an application system manager, i.e. those with the rights to create/remove user accounts, and provide internal support.|BPSS|
|Systems Administrator|A systems administrator does not necessarily have a 'need-to-know' over any of the business information held on the systems they support however they do have administrative privileges which allows them to view data held on those systems and change their configuration.|SC|

**Note:** The clearance level indicated in Table 1 is separate to the clearance level required for a particular job role and sets the minimum requirement for access to a MoJ IT system. Most job roles at the MoJ require an individual to attain BPSS however; some job roles require an individual to have a higher clearance such as SC or DV.

## Privilege management and review of user access rights

In order to ensure that privileges are assigned on a least privileges basis, the following information must be supplied when requesting a new User account or additional privileges:

-   A statement of the access required, for example, a path to a folder or functionality within an application;

-   The name/identity of the User requiring access and their associated User account identify \(where the request relates to an existing User account\);

-   Business justification; and

-   Approval from a MoJ senior manager.


### Review of user access rights

Access rights must be reviewed on a regular basis and may need to be updated as a result of any change in job role, security clearance, or employment status. The review schedule is captured in Table 2.

The following sub-sections outline the key roles involved in the review process and highlights further consideration which should be undertaken when granting privileges for access to knowledge repositories or remote access connectivity.

#### IT System owner / Information Asset Owner responsibilities

An IT System Owner or Information Asset Owner \(IAO\) is responsible for managing access control rules for their particular system.

The actual review and implementation of any access control changes may be performed by MoJ service management along with the relevant IT service provider on their behalf however they may be required to verify access rights in order to assist a scheduled review audit of User accounts and permissions.

#### IT service provider responsibilities

MoJ IT service providers operate as access control custodians \(as they retain top-level administration rights\) acting on the direction of an IT system manager, IAO's and MoJ senior managers.

The IT service provider will only amend access rights based on either an automatic joiners / leavers notification or from requests made from an authorised individual \(as described at the start of [this section](#privilege-management-and-review-of-user-access-rights) \). In performing these activities on behalf of the MoJ, the IT service provider has the responsibility to:

-   Retain a record of all authorised users \(granted accounts\);

-   Retain a record of all access approvals and changes.

-   Retain a record of all users granted administrative privileges on any network, system, or application under their administration.


#### Granting system administrator privileges

Systems administrators by their very nature have privileged access to MoJ IT systems, it is important that the use of system administrative accounts is kept to a minimum, as such:

-   Systems administrators must be provisioned with two system accounts, one operates as a normal user, the other as a systems administrator.

-   A systems administrator must ensure that they use their normal account as their main working account and only use the elevated privileges of their systems administrator account when required.

-   Further details can be found in [IT Security SyOPs - System Administrators](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/system-administrators/).


Non-IT service provider Users are not normally permitted to hold system administrative privileges. Exceptions may be granted where there is a legitimate business justification endorsed by a MoJ senior manager or Senior Civil Servant \(SCS\). Further advice must be sort from the MoJ ITSO.

#### Access to knowledge repositories

Knowledge repositories such as TRIM, are intended to host generally accessible information \(but still internal to the MoJ\), however certain categories of personnel may not be entitled to access these repositories \(or subsets of information held within them\) if they are deemed to contain any information that has a specific or implied access control restriction \(e.g. based on clearance level or job role\).

The relevant IAO is required to ensure that all information is suitable for sharing without access controls or alternatively shall restrict access to authorised personnel with an appropriate need-to-know.

#### Remote access

Remote access to a MoJ IT system requires the use of an authentication token \(such as an RSA token\) in addition to the standard network logon. Each token is unique to a particular individual and must only be issued to those Users who have a business need to access MoJ IT systems remotely, for example, home workers.

## Account removal

An individual's User account and any associated access rights must be removed once that individual has either left the organisation or no longer requires access to the IT system \(or application\) that the account was created for.

It is the responsibility of the line manager to request account removal. The leavers process can be found on the HR intranet page \(see: [https://intranet.justice.gov.uk/guidance/hr/end-change-of-employment/](https://intranet.justice.gov.uk/guidance/hr/end-change-of-employment/) \). As part of the HR process, the line manager must inform all relevant IT service providers when a member of staff leaves the organisation and as such instruct them to deactivate and remove their user account. The leavers guidance linked previously gives detail on how to contact IT service providers.

## Review of User privileges and accounts schedule

Table 2 outlines the review schedule which must be applied to all MoJ IT systems. All User privileges and accounts must be audited in accordance with this schedule, Table 2 states the review activity required with an associated frequency.

**Note:** It is anticipated that most MoJ IT system will be able to comply with this schedule, however it is recognised that this may not be feasible on some. Any deviation from this schedule must be approved by the system Accreditor and MoJ ITSO \(for example a copy of Table 2 with revised schedule can be placed within the relevant system RMADS\).

|Activity|Description|Schedule|
|--------|-----------|--------|
|**Review existing user accounts**|Review all the user \(and system user\) accounts and identify accounts which have not been used in the last 3 months.The list of identified accounts must be reviewed with MoJ HR to identify which accounts can be removed \(as the User has left the MoJ\) or require deactivation \(as the User is on long term leave\).|Every 3 months|
|**Review of user access / authentication tokens**|Review the usages of remote access authentication tokens \(e.g. RSA token\) and identify accounts where a token has not been used in the last 3 months. These token must be disabled.|Every 3 months|
|**Review of user account privileges**|Review the roles and privileges assigned to a User and remove any which are no longer required.|Every 6-12 months \(exact review period to be agreed with the system Accreditor and MoJ ITSO\)|

