# Cyber and Technical Security Guidance

## Summary

This site documents some of the security decisions that the [Ministry of Justice \(MoJ\)](https://www.gov.uk/government/organisations/ministry-of-justice) has made for the products we operate, and our relationships with suppliers.

The MoJ [Technical Guidance](https://ministryofjustice.github.io/technical-guidance/) covers technical decisions in the MoJ more widely.

### Background

*[Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security)* replaces the HMG Security Policy Framework \(SPF\) last published in May 2018. It also incorporates the *Minimum Cyber Security Standard \(MCSS\)* which defines the minimum security measures that departments implement with regards to protecting their information, technology and digital services to meet their SPF and National Cyber Security Strategy obligations.

Sections 6.12 Cyber security and 6.13 Technical security of the standard state:

-   > The security of information and data is essential to good government and public confidence. To operate effectively, HMG needs to maintain the confidentiality, integrity and availability of its information, systems and infrastructure, and the services it provides. Any organisation that handles government information shall meet the standards expected of HM Government.

-   > Technical security relates to the protection of security systems from compromise and/or external interference that may have occurred as a result of an attack.


## Taxonomy

MoJ has developed their cyber and technical security taxonomy as follows:

|Level 1|Level 2|
|-------|-------|
|Cyber|Access Control|
||Asset Management|
||Cryptography|
||Operational Security|
|Technical|Principles|
||Data and Information|
||Incident Management|
||Software Development|

Documents have been developed and defined within this taxonomy, and are listed in the next section together with their suggested target audiences.

### Document List

|Level 1|Level 2|Documents|Target Audience|
|-------|-------|---------|---------------|
|Cyber|Access Control|[Access Control Guide](access-control-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Managing User Access Guide](managing-user-access-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Minimum User Clearance Levels Guide](minimum-user-clearance-requirements-guide.md)|All users|
|||[Multi-Factor Authentication](multi-factor-authentication-mfa-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Privileged Account Management Guide](privileged-account-management-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
||Asset Management|[General User Video and Messaging Apps Guidance](general-user-video-and-messaging-apps-guidance.md)|All users|
|||[Guidance for using Open Internet Tools](guidance-for-using-open-internet-tools.md)|All users|
|||[Security Guidance for Using a Personal Device](personal-devices.md)|All users|
|||[Remote Working](remote-working.md)|All users|
||Cryptography|[Cryptography](cryptography.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
||Operational Security|[Malware Protection Guide \(Overview\)](malware-protection-guide-introduction.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Malware Protection Guide: Defensive Layer 1](malware-protection-guidance-defensive-layer-1.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Malware Protection Guide: Defensive Layer 2](malware-protection-guidance-defensive-layer-2.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Malware Protection Guide: Defensive Layer 3](malware-protection-guidance-defensive-layer-3.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|Technical|Principles|[Data Security and Privacy](data-security-and-privacy.md)|All users|
|||[IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER](identify-protect-detect-respond-recover.md)|All users|
|||[Maintained by Default](maintained-by-default.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Secure by Default](secure-by-default.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Security Log Collection](security-log-collection.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Shared Responsibility Models](shared-responsibility-models.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

## Standards

### Authentication, Authorisation & Accounting

-   [Accounting](accounting.md)

-   [Authentication](authentication.md)

-   [Authorisation](authorisation.md)


### General standards

-   [Baseline for Amazon Web Services accounts](baseline-aws-accounts.md)

-   [Data Destruction](data-destruction.md)

-   [Data Security & Privacy](data-security-and-privacy.md)

-   [Management access](management-access.md)

-   [Networks are just bearers](networks-bearers-not-trust.md)

-   [Password Managers](password-managers.md)

-   [Secrets management](secrets-management.md)

-   [Vulnerability scanning](vulnerability-scanning.md)


### Security Log Collection

-   [Commercial off-the-shelf applications](cots-applications.md)

-   [Custom Applications](custom-applications.md)

-   [Enterprise IT - Infrastructure](enterprise-it-infrastructure.md)

-   [Enterprise IT - Mobile Devices](enterprise-it-mobile-devices.md)

-   [Hosting Platforms](hosting-platforms.md)

-   [Log entry metadata](log-entry-metadata.md)

-   [Security Log Collection Maturity Tiers](security-log-collection-maturity-tiers.md)


## Guides

### General guides

-   [Automated certificate renewal](automated-certificate-renewal.md)

-   [Data Security & Privacy Lifecycle Expectations](data-security-and-privacy-lifecycle.md)

-   [Data Security & Privacy Triage Standards](data-security-and-privacy-triage-standards.md)

-   [Defensive domain registrations](defensive-domain-registration.md)

-   [Online identifiers in security logging & monitoring](online-indentifiers.md)

-   [Personnel security clearances](personnel-security-clearances.md)

-   [Standards Assurance Tables](standards-assurance-tables.md)

-   [Cyber Security Consultancy Team: asking for help](user-guide.md)


### Active Cyber Defence

-   [Mail Check](mail-check.md)

-   [Public Sector DNS](public-sector-dns.md)

-   [Web Check](web-check.md)


### Product specific guides

-   [Using LastPass Enterprise](using-lastpass.md)


## Suppliers to MOJ

-   [Assessing Suppliers](assessing-suppliers.md)

-   [Contracts](contracts.md)

-   Data Destruction

    -   [Data Destruction Instruction and Confirmation Letter](data-destruction-instruction-and-confirmation-letter.md)

    -   [Data Destruction Contract Clauses - Definitions](data-destruction-contract-clauses-definitions.md)

    -   [Data Destruction Contract Clauses - Short Format](data-destruction-contract-clauses-short-format.md)

    -   [Data Destruction Contract Clauses - Long Format](data-destruction-contract-clauses-long-format.md)

    -   [Data Destruction Contract Clauses - Long Format \(Appendix\)](data-destruction-contract-clauses-long-format-appendix.md)

-   [Security Aspect Letters](security-aspect-letters.md)

-   [Supplier Corporate IT](supplier-corporate-it.md)


## Mythbusting

-   [Criminal Justice Secure Mail \(CJSM\)](cjsm.md)

-   [Data Sovereignty](data-sovereignty.md)

-   [Internet v. PSN](internet-v-psn.md)

-   [IP DNS Diagram Handling](ip-dns-diagram-handling.md)

-   [Multiple Back-to-back Consecutive Firewalls](multiple-consecutive-back-to-back-firewalls.md)

-   [`OFFICIAL` and `OFFICIAL-SENSITIVE`](official-official-sensitive.md)


## Other Guidance

### Intranet

There are other cyber and technical security guidance documents available to reference. A large number of these documents are available in the [IT and Computer Security](https://intranet.justice.gov.uk/guidance/security/it-computer-security/) repository on the MoJ Intranet, but these documents are currently being reviewed and progressively are being incorporated into this main [Security Guidance](cyber-and-technical-security-guidance.md) repository.

### Technical Guidance

The MoJ [Technical Guidance](https://ministryofjustice.github.io/technical-guidance/) should be read together with this security-focused guidance.

[Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security)

## Getting in touch

### Contact information

-   [Email](email.md)

-   [Reporting an incident](reporting-an-incident.md)


### Vulnerability Disclosure

-   [Vulnerability Disclosure Policy](vulnerability-disclosure-policy.md)

-   [Implementing `security.txt`](implement-security-txt.md)


