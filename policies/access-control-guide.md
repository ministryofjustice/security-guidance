---
Review: 2020-12-31
Owner: CISO
Target audience: Technical Architects, DevOps, Service Owners, Software Developers
---

[Home > Cyber and Technical Security](../..)

# Access Control guide

## Introduction

This guide explains how the MoJ manages access to its IT systems so that users have access only to the material they need to see. This guide has sub-pages which provide in-depth Access Control guidance.

## Who is this for?

This guide is aimed at two audiences:

1.	The in-house MoJ Digital and Technology staff who are responsible for implementing controls throughout technical design, development, system integration and operation.
2.	Any other MoJ business group, agency, contractor, IT supplier and partner who in any way designs, develops or supplies services (including processing, transmitting and storing data) for, or on behalf of the MoJ.

## Related guides

Further guidance on how to manage user access can be found in the guides below.

- [Privileged Accounts](../privileged-account-management-guide/).
- [Management Access](../managing-user-access-guide/).
<!-- - Joiners, Movers, Leavers Process (currently in development). -->
- [Minimum User Clearance Requirements](../minimum-user-clearance-requirements-guide/).
- [Multi-Factor Authentication (MFA)](../multi-factor-authentication-mfa-guide/).

## Information security principles for access control

These are the Access Control principles you need to know.

- **The 'need-to-know' principle:** Restricting access to information based on a business requirement.
- **Non-repudiation of user actions:** Holding a user accountable for their actions on an IT system.
- **The 'least privilege' principle:** Assigning the least number of privileges required for users to fulfil their work, usually done through Discretionary Access Controls (DAC).
- **User Access Management:** Managing user access to systems and services through a formal user identity lifecycle process.

## Access control principles

Effective access control should be implemented by following these four principles.

<ol>
<li><b>Identification:</b> The MoJ should provide a single, unique ID assigned, named and linked to a private account for each user. For example, Lesley is issued a user account that only Lesley uses, and only Lesley can access. This is important so that logging information is accurate (see the <a href="#accounting">Accounting section below</a> for further information).</li>
<li><b>Authentication:</b> To access MoJ systems, users must authenticate themselves. They can do so using:
<ul><li>something they know (such as a password - the primary authentication method used at the MoJ)</li>
<li>something they have (such as a smart card)</li>
<li>something they are (biometric authentication such as a fingerprint, voice recognition, iris scan and others)</li></ul>
Systems holding sensitive information, or systems that are mission critical to the MoJ, must use Multi-Factor Authentication (MFA) to prove user identity. See the <a href="../multi-factor-authentication-mfa-guide/">Multi-Factor Authentication Guide</a> and <a href="../../standards/password-managers/">Password Management Guide</a> for further information. If you wish to use an additional method of authentication you should review the National Cyber Security Center's (NCSC) guidance and contact the Cyber Assistance Team (CAT). For information on authentication methods including OAuth, refer to the <A href="../managing-user-access-guide/">Managing User Access Guide</a>.</li>
<li><b>Authorisation:</b> Authorisation is the function of specifying access rights/privileges and resources to users, which should be granted in line with the principle of least privilege. Reducing access privileges reduces the "attack surface" of IT systems. This helps to prevent malware and hackers from moving laterally across the network if they compromise a user account.</li>
<li><a id="accounting"><b>Accounting:</b></a> Successful and unsuccessful attempts to access systems, and user activities conducted while using systems must be recorded in logs. Please see the <a href="../../standards/security-log-collection-maturity-tiers/">Security Log Collection Guide</a> for more information. This will help to attribute security events or suspicious activities to users who can be supported to improve their behaviours or held accountable for their actions.</li>
</ol>

Consider the following points when creating activity logs.

Logs should be:

- stored securely
- backed up, so that data are not lost if there is a system unavailability
- managed according to the sensitivity of the data they hold, for example personal information. Contact the Data Privacy Team for advice on protecting sensitive personal information - [privacy@justice.gov.uk](mailto:privacy@justice.gov.uk).
- stored for a minimum of 6 months

Logs should not be:

- retained for longer than 2 years unless otherwise stipulated. Retention rules may vary on a case by case basis so check with the Data Privacy Team, the Cyber Assistance team, and the MoJ Data Protection Officer if a Log involves personal information. See the [Accounting Guide](../../standards/accounting/) for further information.
- tampered with under any circumstances, for example through modification or removal.

See the [Security Log Collection Guide](../../standards/security-log-collection-maturity-tiers/) for more information.

## Segregation of duties

In some parts of the MoJ, segregation of duties is used to help to reduce the possibility that malicious activity takes place without detection.

You can segregate duties in various ways, including:

- implementing manual or automated Role Based Access Control (RBAC), to enforce user authorisation rights.
- regularly reviewing audit logs to check for suspicious activity
- ensuring strict control of software and data changes
- requiring that a user can perform only _one_ of the following roles:
  - identification of a requirement or change management request (Business function)
  - authorisation and approval of a change request (Governance function)
  - design and development (Architect or Developer function)
  - review, inspection, and approval (another Architect or Developer function)
  - implementation in production (System Administrator function)

## Contact details

Contact the Cyber Assistance Team for access control advice – [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk)
