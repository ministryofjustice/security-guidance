# Cyber and Technical Security Guidance

## Summary

This site documents some of the security decisions that the
[Ministry of Justice (MoJ)](https://www.gov.uk/government/organisations/ministry-of-justice)
has made for the products we operate, and our relationships with suppliers.

The MoJ [Technical Guidance](https://ministryofjustice.github.io/technical-guidance/) covers technical decisions in the MoJ more widely.

### Background

*Government Functional Standard - GovS 007: Security* replaces the HMG Security Policy Framework (SPF) last published in May 2018. It also incorporates the *Minimum Cyber Security Standard (MCSS)* which defines the minimum security measures that departments implement with regards to protecting their information, technology and digital services to meet their SPF and National Cyber Security Strategy obligations.

Sections 6.12 Cyber security and 6.13 Technical security of the standard state:

> - The security of information and data is essential to good government and public confidence. To operate effectively, HMG needs to maintain the confidentiality, integrity and availability of its information, systems and infrastructure, and the services it provides. Any organisation that handles government information shall meet the standards expected of HM Government.
> - Technical security relates to the protection of security systems from compromise and/or external interference that may have occurred as a result of an attack.

## Taxonomy

MoJ has developed their cyber and technical security taxonomy as follows:

| Level 1 | Level 2 |
| --- | --- |
| Cyber | Access Control |
| | Asset Management |
| | Cryptography |
| | Operational Security |
| Technical | Principles |
| | Data and Information |
| | Incident Management |
| | Software Development |

Documents have been developed and defined within this taxonomy, and are listed in the next section together with their suggested target audiences.

### Document List

| Level 1 | Level 2 | Documents | Target Audience |
| --- | --- | --- | --- |
| Cyber | Access Control | [Access Control Guide](./policies/access-control-guide/) | Technical Architect, DevOps, IT Service Manager, Software Developer |
| | | [Managing User Access Guide](./policies/managing-user-access-guide/) | Technical Architect, DevOps, IT Service Manager, Software Developer |
| | | [Minimum User Clearance Levels Guide](./policies/minimum-user-clearance-requirements-guide/) | All users |
| | | [Multi-Factor Authentication](./policies/multi-factor-authentication-mfa-guide/) | Technical Architect, DevOps, IT Service Manager, Software Developer |
| | | [Privileged Account Management Guide](./policies/privileged-account-management-guide/) | Technical Architect, DevOps, IT Service Manager, Software Developer |
| | Asset Management | [General User Video and Messaging Apps Guidance](./policies/general-user-video-and-messaging-apps-guidance/) | All users |
| | | [Guidance for using Open Internet Tools](./policies/guidance-for-using-open-internet-tools/) | All users |
| | | [Security Guidance for Using a Personal Device](./policies/personal-devices/) | All users |
| | | [Remote Working](./policies/remote-working/) | All users |
| | Cryptography | [Cryptography](./standards/cryptography/) | Technical Architect, DevOps, IT Service Manager, Software Developer |
| | Operational Security | [Malware Protection Guide (Overview)](./standards/malware-protection-guide-introduction/) | Technical Architect, DevOps, IT Service Manager, Software Developer |
| | | [Malware Protection Guide: Defensive Layer 1](./standards/malware-protection-guidance-defensive-layer-1) | Technical Architect, DevOps, IT Service Manager, Software Developer |
| | | [Malware Protection Guide: Defensive Layer 2](./standards/malware-protection-guidance-defensive-layer-2) | Technical Architect, DevOps, IT Service Manager, Software Developer |
| | | [Malware Protection Guide: Defensive Layer 3](./standards/malware-protection-guidance-defensive-layer-3) | Technical Architect, DevOps, IT Service Manager, Software Developer |
| Technical | Principles | [Data Security & Privacy](./security_decisions/principles/data-security-and-privacy/) | All users |
| | | [IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER](./security_decisions/principles/identify-protect-detect-respond-recover/) | All users |
| | | [Maintained by Default](./security_decisions/principles/maintained-by-default/) | Technical Architect, DevOps, IT Service Manager, Software Developer |
| | | [Secure by Default](./security_decisions/principles/secure-by-default/) | Technical Architect, DevOps, IT Service Manager, Software Developer |
| | | [Security Log Collection](./security_decisions/principles/security-log-collection/) | Technical Architect, DevOps, IT Service Manager, Software Developer |
| | | [Shared Responsibility Models](./security_decisions/principles/shared-responsibility-models/) | Technical Architect, DevOps, IT Service Manager, Software Developer |

<!--
| Cyber | Access Control | [Access Control Guide](./policies/access-control-guide/) | Technical Architect, DevOps, IT Service Manager, Software Developer |
| | | JML process | |
| | | [Managing User Access Guide](./policies/managing-user-access-guide/) | |
| | | [Minimum User Clearance Levels Guide](./policies/minimum-user-clearance-requirements-guide/)] | |
| | | [Multi-Factor Authentication](./policies/multi-Factor-authentication-mfa-guide/) | |
| | | [Multi-user Accounts and Public-Facing Service Accounts Guide](./policies/multi-user-accounts-and-public-facing-service-accounts-guide/) | |
| | | [Password Changes, Account Locks and Disabling Accounts Guide](./policies/password-changes-account-locks-and-disabling-accounts-guide/) | |
| | | [Password Creation and Authentication Guide](./policies/password-creation-and-authentication-guide/) | |
| | | [Password Management Guide](./policies/password-management-guide/) | |
| | | [Password Storage and Management Guide](./policies/password-storage-and-management-guide/) | |
| | | [Privileged Account Management Guide](./policies/privileged-account-management-guide/) | |
| | | [Privileged User Guide](./policies/privileged-user-guide/) | |
| | | [Privileged User Guide - Backups Removable Media and Incident Management Guide](./policies/privileged-user-backups-removable-media-and-incident-management-guide/) | |
| | | [Privileged User Guide - Configuration, Patching and Change Management](./policies/privileged-user-configuration-patching-and-change-management-guide/) | |
| | | [Privileged User Guide - Logging and Protective Monitoring Guide](./policies/privileged-user-logging-and-protective-monitoring-guide/) |
| | Asset Management | [Acceptable Use Policy](./policies/acceptable-use-policy/) | |
| | | [Accessing MoJ Systems from Abroad](./policies/taking-it-equipment-abroad-business-or-personal/) | |
| | | [Video and Voice Conferencing Best Practice](./policies/video-and-voice-conferencing-best-practice/) | |
| | | [Patch Management Guide](./policies/patch-management-guide/) | |
| | | [Taking IT Equipment Abroad](./policies/taking-it-equipment-abroad-guidance/) | |
| | | [Vulnerability Scanning and Patch Management Guide](./policies/vulnerability-scanning-and-patch-management-guide/) | |
| | | [Vulnerability Scanning Guide](./policies/vulnerability-scanning-guide/) | |
| | Cryptography |
| | Operational Security | [Email Authentication Guide](./policies/email-authentication-guide/) | |
| | | [Email Security Guide](./policies/email-security-guide/) | MoJ Digital and Technology staff implementing controls throughout technical design, development, system integration and operation. Incident Managers. Any other party designing, developing or supplying services for the MoJ |
| | | [IT Security Policy](./policies/it-security-policy/) | As above |
| | | [Secure Email Transfer Guide](./policies/secure-email.transfer-guide/) | |
| | | [Spam and Phishing Guide](./policies/spam-and-phishing-guide/) | |
| | | [Technical Controls Guide (Overview)](./policies/technical-security-controls-guide/) | |
| | | [Technical Controls Guide - Layer 1](./policies/technical-security-controls-guide-defensive-layer-1/) | |
| | | [Technical Controls Guide - Layer 2](./policies/technical-security-controls-guide-defensive-layer-2/) | |
| | | [Technical Controls Guide - Layer 3](./policies/technical-security-controls-guide-defensive-layer-3/) | |
| | [Data and Information | Information and Data Security Policy](./policies/information-and-data-security-policy/) | |
| | | [Information Classification Handling and Security Guide](./policies/information-classification-handling-and-security-guide/) | |
| | Incident Management |
| | Software Development |

-->

## Standards

### Authentication, Authorisation & Accounting

- [Accounting](./standards/accounting/)
- [Authentication](./standards/authentication/)
- [Authorisation](./standards/authorisation/)

### General standards

<!-- - [Anti-malware](./standards/anti-malware/) -->
- [Baseline for Amazon Web Services accounts](./standards/baseline-aws-accounts/)
- [Data Destruction](./standards/data-destruction/)
- [Data Security & Privacy](./standards/data-security-and-privacy)
- [Management access](./standards/management-access/)
- [Networks are just bearers](./standards/networks-bearers-not-trust/)
- [Password Managers](./standards/password-managers/)
- [Secrets management](./standards/secrets-management/)
- [Vulnerability scanning](./standards/vulnerability-scanning/)

### Security Log Collection

- [Commercial off-the-shelf applications](./standards/cots-applications/)
- [Custom Applications](./standards/custom-applications/)
- [Enterprise IT - Infrastructure](./standards/enterprise-it-infrastructure/)
- [Enterprise IT - Mobile Devices](./standards/enterprise-it-mobile-devices/)
- [Hosting Platforms](./standards/hosting-platforms/)
- [Log entry metadata](./standards/log-entry-metadata/)
- [Security Log Collection Maturity Tiers](./standards/security-log-collection-maturity-tiers/)

## Guides

### General guides

- [Automated certificate renewal](./guides/automated-certificate-renewal/)
- [Data Security & Privacy Lifecycle Expectations](./guides/data-security-and-privacy-lifecycle/)
- [Data Security & Privacy Triage Standards](./guides/data-security-and-privacy-triage-standards/)
- [Defensive domain registrations](./guides/defensive-domain-registration/)
- [Online identifiers in security logging & monitoring](./guides/online-indentifiers/)
- [Personnel security clearances](./guides/personnel-security-clearances/)
- [Standards Assurance Tables](./guides/standards-assurance-tables/)
- [Cyber Security Consultancy Team: asking for help](./guides/user-guide/)

### Active Cyber Defence

- [Mail Check](./guides/mail-check/)
- [Public Sector DNS](./guides/public-sector-dns/)
- [Web Check](./guides/web-check/)

### Product specific guides

- [Using LastPass Enterprise](./guides/using-lastpass/)

## Suppliers to MOJ

- [Assessing Suppliers](./security_decisions/suppliers/assessing-suppliers/)
- [Contracts](./security_decisions/suppliers/contracts/)
- Data Destruction
  - [Data Destruction Instruction and Confirmation Letter](./security_decisions/suppliers/data-destruction-instruction-and-confirmation-letter/)
  - [Data Destruction Contract Clauses - Definitions](./security_decisions/suppliers/data-destruction-contract-clauses-definitions/)
  - [Data Destruction Contract Clauses - Short Format](./security_decisions/suppliers/data-destruction-contract-clauses-short-format/)
  - [Data Destruction Contract Clauses - Long Format](./security_decisions/suppliers/data-destruction-contract-clauses-long-format/)
  - [Data Destruction Contract Clauses - Long Format (Appendix)](./security_decisions/suppliers/data-destruction-contract-clauses-long-format-appendix/)
- [Security Aspect Letters](./security_decisions/suppliers/security-aspect-letters/)
- [Supplier Corporate IT](./security_decisions/suppliers/supplier-corporate-it/)

## Mythbusting

- [Criminal Justice Secure Mail (CJSM)](./security_decisions/mythbusting/cjsm/)
- [Data Sovereignty](./security_decisions/mythbusting/data-sovereignty/)
- [Internet v. PSN](./security_decisions/mythbusting/internet-v-psn/)
- [IP DNS Diagram Handling](./security_decisions/mythbusting/ip-dns-diagram-handling/)
- [Multiple Back-to-back Consecutive Firewalls](./security_decisions/mythbusting/multiple-consecutive-back-to-back-firewalls/)
- [`OFFICIAL` and `OFFICIAL-SENSITIVE`](./security_decisions/mythbusting/official-official-sensitive/)

## Other Guidance

<!-- - Using GMail’s Confidential Mode(./policies/gmail-confidential-mode/) -->

### Intranet

There are other cyber and technical security guidance documents available to reference. A large number of these documents are available in the [IT and Computer Security](https://intranet.justice.gov.uk/guidance/security/it-computer-security/) repository on the MoJ Intranet, but these documents are currently being reviewed and progressively are being incorporated into this main [Security Guidance](.) repository.

### Technical Guidance

The MoJ [Technical Guidance](https://ministryofjustice.github.io/technical-guidance/) should be read together with this security-focused guidance.

<!-- ## References

![](https://github.com/ministryofjustice/security-guidance/blob/Local/images/GovS_007_Thumbnail.png) Government Functional Standard - GovS 007: Security -->

## Getting in touch

### Contact information

- [Email](./contact/email/)
- [Reporting an incident](./contact/reporting-an-incident/)

### Vulnerability Disclosure

- [Vulnerability Disclosure Policy](./contact/vulnerability-disclosure-policy)
- [Implementing `security.txt`](./contact/implement-security-txt)
