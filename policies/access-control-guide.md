[Home > Cyber and Technical Security](home-security-policies-guides.md)

---
Review: 2020-12-31
Owner: CISO
Target audience: Technical Architect, DevOps, IT Service Manager, Software Developer
---

# Access Control guide

## Introduction

This guide explains how the MoJ manages access to its IT systems so that users have access only to the material they need to see. This guide has sub-pages which provide in-depth Access Control guidance.

## Who is this for?

This guide is aimed at two audiences:

1.	The in-house MoJ Digital and Technology staff who are responsible for implementing controls throughout technical design, development, system integration and operation. This includes DevOps, Software Developers, Technical Architects and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI and Knowledge (EPICK) Team.
2.	Any other MoJ business group, agency, contractor, IT supplier and partner who in any way designs, develops or supplies services (including processing, transmitting and storing data) for, or on behalf of the MoJ.

## Related guides

Further guidance on how to manage user access can be found in the guides below.

- [Privileged Accounts](privileged-account-management-guide.md).
- [Management Access](managing-user-access-guide.md).
- Joiners, Movers, Leavers Process.
- [Minimum User Clearance Requirements](minimum-user-clearance-requirements-guide.md).
- [Multi-Factor Authentication (MFA)](multi-Factor-authentication-mfa-guide.md).

## Information security principles for access control

These are the Access Control principles you need to know.

- **The ‘need-to-know’ principle:** Restricting access to information based on a business requirement.
- **Non-repudiation of user actions:** Holding a user accountable for their actions on an IT system.
- **The ‘least privilege’ principle:** Assigning the least number of privileges required for users to fulfil their work, usually done through Discretionary Access Controls (DAC).
- **User Access Management:** Managing user access to systems and services through a formal user identity lifecycle process.

## Access control principles

Effective access control should be implemented by following these four principles.
1. **Identification:** The MoJ should provide a single, unique ID assigned, named and linked to a private account for each user. For example, Joe Bloggs is issued a user account that only Joe uses and only Joe can access. This is important so that logging information is accurate (see Accounting section below for further information).

2. **Authentication:** To access MoJ systems, users must authenticate themselves. They can do so using:

- something they know (such as a password - the primary authentication method used at the MoJ),
- something they have (such as a smart card), and/or
- something they are (biometric authentication such as a fingerprint, voice recognition, iris scan and others).

Systems holding sensitive information or systems that are mission critical to the MoJ must use Multi-Factor Authentication (MFA) to prove user identity. See the Multi-Factor Authentication Guide and Password Management Guide for further information. If you wish to use a federated identity, you should review the National Cyber Security Center’s (NCSC) guidance and contact the Cyber Assistance Team. For information on authentication methods including OAuth, refer to the Managing User Access guide.

3. **Authorisation:** Authorisation is the function of specifying access rights/privileges and resources to users, which should be granted in line with the principle of least privilege. Reducing access privileges reduces the “attack surface” of IT systems. This helps to prevent malware and hackers from moving laterally across the network if they compromise a user account.

4. **Accounting:** Successful and unsuccessful attempts to access systems, and user activities conducted while using systems must be recorded in logs. Please see the Security Log Collection Guide for more information. This will help to attribute security events or suspicious activities to users who can be supported to improve their behaviours or held accountable for their actions.

Consider the following when creating activity logs:

- Logs should be stored securely.
- Logs should be backed up so that they are not lost if there is a system unavailability.
- Logs can include sensitive data (such as personal information) and should be managed accordingly. Contact the Data Privacy Team for advice on protecting sensitive personal information - [privacy@justice.gov.uk](mailto:privacy@justice.gov.uk).
- Log files should be stored for a minimum of 6 months.
- Log data should not be retained for longer than 2 years unless otherwise stipulated. Retention rules may vary on a case by case basis so should be checked with the Data Privacy Team, the Cyber Assistance team, and the MoJ Data Protection Officer if it involves personal information. See the Accounting Guide for further information.
- Log files should not be tampered with, for example through modification or removal, under any circumstance.

See the Security Log Collection guide for more information.

## Segregation of duties

In certain areas of the business, such as transactions, segregation of duties is encouraged to help to reduce the risk that malicious activity takes place without detection.

This can be implemented by conducting the following activities:

- implement manual or automated Role Based Access Control (RBAC) to enforce user authorisation rights.
- regularly review audit logs to check for suspicious activity, and
- ensure strict control of software and data changes require that each user can perform only one of the following roles:
- identification of a requirement or change management request (Business function)
- authorisation and approval of a change request (Governance function)
- design and development (Architect or Developer function)
- review, inspection, and approval (another Architect or Developer function), and
- implementation in production (System Administrator function)

## Contact details

Contact the Cyber Assistance Team for access control advice – [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk)
