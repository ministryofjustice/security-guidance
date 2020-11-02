# Cyber and Technical Security Guidance

## Summary

This site documents some of the security decisions that the [Ministry of Justice \(MoJ\)](https://www.gov.uk/government/organisations/ministry-of-justice) has made for the products we operate, and our relationships with suppliers.

The MoJ [Technical Guidance](https://ministryofjustice.github.io/technical-guidance/) covers technical decisions in the MoJ more widely.

**Note:**

This guidance is dated: 2 November 2020.

For convenience, offline versions of this guidance are available.

|Audience|PDF format|EPUB format|
|--------|----------|-----------|
|All users. Does not include lots of technical detail.|[PDF](moj-guidance.pdf)|[EPUB](moj-guidance.epub)|
|Technical users. Includes lots of technical detail.|[PDF](moj-guidance-tech.pdf)|[EPUB](moj-guidance-tech.epub)|

The offline versions of this guidance are time-limited, and are not valid after 2 December 2020.

### Getting in touch

-   [To report an incident](reporting-an-incident.md).
-   For general assistance on MoJ security matters, email [security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk).
-   For Cyber Security assistance or consulting, email [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk). More information about the Cyber Security Consultancy Team is [available](user-guide.md).
-   Suppliers to the MoJ should first communicate with their usual MoJ points of contact.

### Background

The new [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security) sits at the top of other government security governance documents like the [HMG Security Policy Framework \(SPF\)](https://www.gov.uk/government/publications/security-policy-framework) and the [Minimum Cyber Security Standard \(MCSS\)](https://www.gov.uk/government/publications/the-minimum-cyber-security-standard). Together they define the minimum security measures that departments need to implement with regards to protecting their information, technology and digital services to meet their SPF and National Cyber Security Strategy obligations.

Sections 6.9 Cyber security and 6.10 Technical security of the standard state:

-   > The security of information and data is essential to good government and public confidence. To operate effectively, HMG needs to maintain the confidentiality, integrity and availability of its information, systems and infrastructure, and the services it provides. Any organisation that handles government information shall meet the standards expected of HM Government.
-   > Technical security relates to the protection of security systems from compromise and/or external interference that may have occurred as a result of an attack.

## Information taxonomy andstructure

The MoJ has developed their cyber and technical security taxonomy as follows:

|Level 1|Level 2|
|-------|-------|
|Cyber|Access Control|
||Asset Management|
||Cryptography|
||Operational Security|
|Technical|Principles|
||Data and information|
||System development|

The documents have been developed and defined within this taxonomy, and are listed in the next section, together with their suggested target audiences.

### Document List

|Level 1|Level 2|Documents|Target Audience|
|-------|-------|---------|---------------|
|Cyber|Access Control|||
|||[Access Control Guide](access-control-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Accessing MoJ IT Systems From Abroad](accessing-moj-it-systems-from-abroad.md)|All users|
|||[Authentication](authentication.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Authorisation](authorisation.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Managing User Access Guide](managing-user-access-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Minimum User Clearance Levels Guide](minimum-user-clearance-requirements-guide.md)|All users|
|||[Multi-Factor Authentication](multi-factor-authentication-mfa-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Personnel security clearances](personnel-security-clearances.md)|All users|
|||[Privileged Account Management Guide](privileged-account-management-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Protecting Social Media Accounts](protecting-social-media-accounts.md)|All users|
||Asset Management|||
|||[Accounting](accounting.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Bluetooth](bluetooth.md)|All users|
|||[General advice on taking equipment abroad](general-advice-on-taking-equipment-abroad.md)|All users|
|||[General Apps Guidance](general-user-video-and-messaging-apps-guidance.md)|All users|
|||[Guidance for using Open Internet Tools](guidance-for-using-open-internet-tools.md)|All users|
|||[Lost Laptop or other IT security incident](lost-laptophardware.md)|All users|
|||[Remote Working](remote-working.md)|All users|
|||[Security Guidance for Using a Personal Device](personal-devices.md)|All users|
||Cryptography|[Cryptography](cryptography.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
||Operational Security|[Malware Protection Guide \(Overview\)](malware-protection-guide-introduction.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Malware Protection Guide: Defensive Layer 1](malware-protection-guidance-defensive-layer-1.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Malware Protection Guide: Defensive Layer 2](malware-protection-guidance-defensive-layer-2.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Malware Protection Guide: Defensive Layer 3](malware-protection-guidance-defensive-layer-3.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Vulnerability Disclosure](vulnerability-disclosure-policy.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Vulnerability Disclosure: Implementing `security.txt`](implement-security-txt.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|Technical|Principles|||
|||[Criminal Justice Secure Mail \(CJSM\)](cjsm.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Data Sovereignty](data-sovereignty.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER](identify-protect-detect-respond-recover.md)|All users|
|||[Internet v. PSN](internet-v-psn.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[IP DNS Diagram Handling](ip-dns-diagram-handling.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Management access](management-access.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Multiple Back-to-back Consecutive Firewalls](multiple-consecutive-back-to-back-firewalls.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Networks are just bearers](networks-bearers-not-trust.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[`OFFICIAL` and `OFFICIAL-SENSITIVE`](official-official-sensitive.md)|All users|
|||[Secrets management](secrets-management.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Secure by Default](secure-by-default.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Shared Responsibility Models](shared-responsibility-models.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Standards Assurance Tables](standards-assurance-tables.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Technical Security Controls Guide](technical-security-controls-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Technical Security Controls Guide: Defensive Layer 1](technical-security-controls-guide-defensive-layer-1.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Technical Security Controls Guide: Defensive Layer 2](technical-security-controls-guide-defensive-layer-2.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
||Data and information|||
|||[Data Destruction](data-destruction.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Data Destruction: Contract Clauses - Definitions](data-destruction-contract-clauses-definitions.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Data Destruction: Contract Clauses - Long Format](data-destruction-contract-clauses-long-format.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Data Destruction: Contract Clauses - Long Format \(Appendix\)](data-destruction-contract-clauses-long-format-appendix.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Data Destruction: Contract Clauses - Short Format](data-destruction-contract-clauses-short-format.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Data Destruction: Instruction and Confirmation Letter](data-destruction-instruction-and-confirmation-letter.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Data Security and Privacy](data-security-and-privacy.md)|All users|
|||[Password Managers](password-managers.md)|All users|
|||[Suppliers to MoJ: Assessing Suppliers](assessing-suppliers.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Suppliers to MoJ: Contracts](contracts.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Suppliers to MoJ: Security Aspect Letters](security-aspect-letters.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Suppliers to MoJ: Supplier Corporate IT](supplier-corporate-it.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Using LastPass Enterprise](using-lastpass.md)|All users|
||System development|||
|||[Active Cyber Defence: Mail Check](mail-check.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Active Cyber Defence: Public Sector DNS](public-sector-dns.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Active Cyber Defence: Web Check](web-check.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Automated certificate renewal](automated-certificate-renewal.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Baseline for Amazon Web Services accounts](baseline-aws-accounts.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Commercial off-the-shelf applications](cots-applications.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Custom Applications](custom-applications.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Data Security & Privacy Lifecycle Expectations](data-security-and-privacy-lifecycle.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Data Security & Privacy Triage Standards](data-security-and-privacy-triage-standards.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Defensive domain registrations](defensive-domain-registration.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Maintained by Default](maintained-by-default.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Online identifiers in security logging & monitoring](online-identifiers.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Security Log Collection](security-log-collection.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Security Log Collection: Enterprise IT - Infrastructure](enterprise-it-infrastructure.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Security Log Collection: Enterprise IT - Mobile Devices](enterprise-it-mobile-devices.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Security Log Collection: Hosting Platforms](hosting-platforms.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Security Log Collection: Log entry metadata](log-entry-metadata.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Security Log Collection: Maturity Tiers](security-log-collection-maturity-tiers.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Using Live Data for Testing purposes](using-live-data-for-testing-purposes.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|||[Vulnerability scanning](vulnerability-scanning.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

## Other Guidance

### Intranet

There are other cyber and technical security guidance documents available to reference. A large number of these documents are available in the [IT and Computer Security](https://intranet.justice.gov.uk/guidance/security/it-computer-security/) repository on the MoJ Intranet, but these documents are currently being reviewed and progressively are being incorporated into this main [Security Guidance](cyber-and-technical-security-guidance.md) repository.

### Technical Guidance

The MoJ [Technical Guidance](https://ministryofjustice.github.io/technical-guidance/) should be read together with this security-focused guidance.

The [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security) provides the base material for all security guidance in the MoJ.

