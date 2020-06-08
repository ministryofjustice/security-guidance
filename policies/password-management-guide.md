---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](home-security-policies-guides.md)

# Password Management Guide

## Introduction

This guide sets out the roles and requirements for setting and maintaining strong passwords across the MoJ’s systems. This page is the first in a series of guides for the management of MoJ passwords.

## Who is this for?

This guide is aimed at two audiences:

1. The in-house MoJ Digital and Technology staff who are responsible for implementing controls throughout technical design, development, system integration and operation. This includes DevOps, Software Developers, Technical Architects and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI and Knowledge [EPIC](https://peoplefinder.service.gov.uk/teams/epic) Team.

2. Any other MoJ business group, agency, contractor, IT supplier and partner who in any way designs, develops or supplies services (including processing, transmitting and storing data) for, or on behalf of the MoJ.



## Related guides

Further guidance around the management of passwords at the MoJ can be found in the guides below.

* _Password Creation and Authentication Guide_ – provides guidance to ensure you choose the correct passwords and authentication tools to protect information in line with its security classifications.  

* _Password Storage and Management Guide_ – provides guidance on storing and sharing passwords securely.

* _Password Changes, Account Locks and Disabling Accounts Guide_ – provides guidance about why you may need to change your password. It also addresses when and how you should change your password.

* _Multi-User Accounts and Public-Facing Service Accounts Guide_ – provides guidance on when you should use a multi-user account and how you should authenticate a service account.



## Roles and responsibilities

**All MoJ Digital and Technology users**

All MoJ Digital and Technology users must ensure that password creation, distribution and maintenance is done securely.

 ✔ Passwords must not ordinarily be shared. Refer to the Password Storage and Management Guide for exceptions and alternative solutions for sharing passwords.

 ✔ Passwords must be strong and complex as set out in the Password Creation and Authentication Guide’.

 ✔ Passwords must be changed upon indication of compromise.

 ✔ Passwords must be distributed securely. Refer to the Password Storage and Management Guide.

 ✔ Any system or information classified as SECRET or TOP SECRET must have additional access controls implemented as set out in the MoJ’s Access Control Guide. For any queries or decisions relating to SECRET or TOP SECRET systems or information, the [Cyber Assistance Team](mailto:CyberConsultancy@digital.justice.gov.uk) should be contacted.

 ✔ Additional authentication controls such as multi-factor authentication (MFA) must be enabled as required by specific systems. Further guidance can be found in the Password Creation and Authentication Guide and the Multi-user accounts and Public-Facing Service Accounts Guide.


**Software Developers, Technical Architects and Development Operations**

All application and software development within or on behalf of the MoJ must ensure the following password security requirements are adhered too.

 ✔ Multi-user accounts should be avoided, but if required please refer to the Multi-User Accounts and Public-Facing Service Accounts Guide for further guidance.

 ✔ Technical controls must be implemented to support requirements in the Password Creation and Authentication Guide.  

 ✔ Applications or software should support MFA and single sign-on (SSO) solutions leveraged by the MoJ.

 ✔ Passwords must not be stored in clear text or using encryption algorithms with known security weaknesses.

 ✔ Passwords must not be transmitted in clear text over networks.

 ✔ All applications or software must use HTTPS to require authentication.

 ✔ Applications or software must provide some form of role management, whereby an authorised user can take over the functions of another without having to know the other users’ password.

 ✔ Passwords and other secrets (SSH Keys, DevOps secrets, etc.) should not be embedded into applications. The use of key vaults, such AWS Secrets Manager, is strongly recommended.

**Suppliers and vendors**

Suppliers and vendors must ensure that their systems support the password requirements set by the MoJ.

 ✔ Supplier or vendor systems must be able to change, reset and revoke passwords. This must be possible using well-defined processes.

 ✔ Suppliers and vendors should consider implementing technical controls, such as locking accounts after repeated access attempts and blocking common password choices, to improve the effectiveness of password-enforcement and compliance.

 ✔ Senior Business Owners for Contracts should ensure that when contracts are signed, the supplier receives explicit guidance on password management and it is included in the associated Information Protection Plan (IPP).

**System Administrators**

System Administrators (SAs) must ensure that systems support the password requirements set by the MoJ. When provisioning and maintaining user accounts, SAs must:

 ✔ require a change of initial or first-time passwords

 ✔ verify a user’s identity before resetting a password

 ✔ implement automated notification of a password change or reset.

SAs must also ensure privileged accounts:

 ✔ are authorised only for a specified time  

 ✔ are managed and regularly reviewed for user access (access will be revoked when a user no longer needs it to prevent unauthorised access)

 ✔ use MFA for user authentication

 ✔ have activity logs for the purposes of review and monitoring.

## Contact details

For any further questions relating to security, please contact: [security@justice.gov.uk](mailto:security@justice.gov.uk)
