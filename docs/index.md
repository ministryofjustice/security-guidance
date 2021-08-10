# Cyber and Technical Security Guidance

## Summary

This site documents some of the security decisions that the [Ministry of Justice \(MoJ\)](https://www.gov.uk/government/organisations/ministry-of-justice) has made for the products we operate, and our relationships with suppliers.

The MoJ [Technical Guidance](https://ministryofjustice.github.io/technical-guidance/) covers technical decisions in the MoJ more widely.

**Note:** This guidance is dated: 10 August 2021.

### Popular links

Popular links for all users:

-   [General Apps Guidance](general-user-video-and-messaging-apps-guidance.md)
-   [Minimum User Clearance Requirements Guide](minimum-user-clearance-requirements-guide.md)
-   [OFFICIAL, OFFICIAL-SENSITIVE](official-official-sensitive.md) classifications and handling
-   [Accessing MoJ IT Systems From overseas](accessing-moj-it-systems-from-overseas.md)
-   [Remote Working](remote-working.md)

### Offline content

For convenience, offline versions of this guidance are available.

|Audience|PDF format|EPUB format|
|--------|----------|-----------|
|All users. Does not include lots of technical detail.|[PDF](moj-guidance.pdf)|[EPUB](moj-guidance.epub)|
|Technical users. Includes lots of technical detail.|[PDF](moj-guidance-tech.pdf)|[EPUB](moj-guidance-tech.epub)|

The offline versions of this guidance are time-limited, and are not valid after 10 September 2021.

### Searching this content

The content of this site is searchable in two ways:

1.  By searching for the word or phrase on your preferred search engine, and specifying this site:

    ```
    site:https://ministryofjustice.github.io/security-guidance/
    ```

    For example, to search for information about passwords, you might use the following search expression:

    ```
    password site:https://ministryofjustice.github.io/security-guidance/
    ```

2.  By downloading one of the offline versions and using the inbuilt search capability of your offline reader.

### Getting in touch

-   [To report an incident](reporting-an-incident.md).
-   For general assistance on MoJ security matters, email [security@justice.gov.uk](mailto:security@justice.gov.uk).
-   For Cyber Security assistance or consulting, email [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk). More information about the Cyber Security Consultancy Team is [available](user-guide.md).
-   Suppliers to the MoJ should first communicate with their usual MoJ points of contact.

### Background

[Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security) replaces the [HMG Security Policy Framework \(SPF\)](https://www.gov.uk/government/publications/security-policy-framework), last published in May 2018. It also incorporates the [Minimum Cyber Security Standard \(MCSS\)](https://www.gov.uk/government/publications/the-minimum-cyber-security-standard) which defines the minimum security measures that departments implement with regards to protecting their information, technology and digital services to meet their SPF and National Cyber Security Strategy obligations.

![A diagram showing a hierarchy of the key components within the Government Functional Standard. It is in three sections. In the first section, at the top is a triangle labelled Principles. This stands on a block marked Content, which itself stands on a block marked Governance, showing that governance and content underpin the principles. The second section is called Security Life Cycle. It shows a flow from left to right. To the left of the section is a large arrow entitled Security Strategy and Planning. This arrow splits on the right hand side into two small arrows. The top small arrow is labelled Prevention and Detection. The bottom small arrow is labelled Security Incident Management. A small line arrow drops down from the top Prevention and Detection arrow to the bottom Security Incident Management arrow. To the right hand side of this section of the diagram, the Prevention and Detection and the Security Incident Management arrows converge into a final large arrow, entitled Review and Learn from Experience. A dotted line arrow, labelled Improvement, goes back from the Review and Learn arrow over to the beginning of this section of the diagram, linking to the Security Strategy and Planning arrow. Underneath these arrow diagrams is the third and final section. This is a summary text, called Security Practices. Many practices are listed using three columns in this section. The left column list includes: Critical Assets and Services, Risk Management, and Access to information. The middle column list includes: Capability, capacity and resources, Security culture, Security education and awareness, and Physical security. The right column list includes: Personnel security, Cyber security, and Technical security.](images/gov007overview.png)

Sections 6.9 Cyber security and 6.10 Technical security of the standard state:

-   > The security of information and data is essential to good government and public confidence. To operate effectively, HMG needs to maintain the confidentiality, integrity and availability of its information, systems and infrastructure, and the services it provides. Any organisation that handles government information shall meet the standards expected of HM Government.
-   > Technical security relates to the protection of security systems from compromise and/or external interference that may have occurred as a result of an attack.

## Information structure

The MoJ has developed our cyber and technical security taxonomy as follows:

|Level 1|Level 2|
|-------|-------|
|[Information security policies](#information-security-policies)|[Management direction for information security](#management-direction-for-information-security)|
|[Mobile devices and teleworking](#mobile-devices-and-teleworking)|[Mobile device policy](#mobile-device-policy)|
||[Teleworking](#teleworking)|
|[Human resource security](#human-resource-security)|[Prior to employment](#prior-to-employment)|
||[During employment](#during-employment)|
|[Asset management](#asset-management)|[Responsibility for assets](#responsibility-for-assets)|
||[Information classification](#information-classification)|
||[Media handling](#media-handling)|
|[Access control](#access-control)|[Business requirements of access control](#business-requirements-of-access-control)|
||[User access management](#user-access-management)|
||[User responsibilities](#user-responsibilities)|
||[System and application access control](#system-and-application-access-control)|
|[Cryptography](#cryptography)|[Cryptographic controls](#cryptographic-controls)|
|[Physical and environmental security](#physical-and-environmental-security)|[Secure areas](#secure-areas)|
||[Equipment](#equipment)|
|[Operations security](#operations-security)|[Operational procedures and responsibilities](#operational-procedures-and-responsibilities)|
||[Protection from malware](#protection-from-malware)|
||[Backup](#backup)|
||[Logging and monitoring](#logging-and-monitoring)|
||[Control of operational software](#control-of-operational-software)|
||[Technical vulnerability management](#technical-vulnerability-management)|
|[Communications security](#communications-security)|[Network security management](#network-security-management)|
||[Information transfer](#information-transfer)|
|[System acquisition, development and maintenance](#system-acquisition-development-and-maintenance)|[Security requirements of information systems](#security-requirements-of-information-systems)|
||[Security in development and support processes](#security-in-development-and-support-processes)|
||[Test data](#test-data)|
|[Supplier relationships](#supplier-relationships)|[Information security in supplier relationships](#information-security-in-supplier-relationships)|
||[Supplier service delivery management](#supplier-service-delivery-management)|
|[Information security incident management](#information-security-incident-management)|[Management of information security incidents and lost devices](#management-of-information-security-incidents-and-lost-devices)|
|[Information security aspects of business continuity management](#information-security-aspects-of-business-continuity-management)|[Information security continuity](#information-security-continuity)|
|[Compliance](#compliance)|[Compliance with legal and contractual requirements](#compliance-with-legal-and-contractual-requirements)|
||[Information security reviews](#information-security-reviews)|
|[Risk Assessment](#risk-assessment)|[Risk Assessment Process](#risk-assessment-process)|

The documents have been developed and defined within this taxonomy, and are listed in the next section, together with their suggested target audiences.

### Information security policies

#### Management direction for information security

|[Avoiding too much security](setecastronomy.md)|All users|
|[IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER](identify-protect-detect-respond-recover.md)|All users|
|[IT Security All Users Policy](it-security-all-users-policy.md)|All users \(Policy\)|
|[IT Security Policy \(Overview\)](it-security-policy-overview.md)|All users \(Policy\)|
|[IT Security Technical Users Policy](it-security-technical-users-policy.md)|Technical Architect, DevOps, IT Service Manager, Software Developer \(Policy\)|
|[Line Manager approval](line-manager-approval.md)|All users|
|[Shared Responsibility Models](shared-responsibility-models.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

### Mobile devices and teleworking

#### Mobile device policy

|[Mobile Device and Remote Working Policy](mobile-device-and-remote-working-policy.md)|All users \(Policy\)|
|[Remote Working](remote-working.md)|All users|

#### Teleworking

|[Accessing MoJ IT Systems From overseas](accessing-moj-it-systems-from-overseas.md)|All users|
|[General advice on taking equipment overseas](general-advice-on-taking-equipment-overseas.md)|All users|
|[Personal Devices](personal-devices.md)|All users|

### Human resource security

#### Prior to employment

|[Minimum User Clearance Levels Guide](minimum-user-clearance-requirements-guide.md)|All users|
|[National Security Vetting questions](national-security-vetting-questions.md)|All users|
|[National Security Vetting for External Candidates FAQ](national-security-vetting-for-external-candidates-faq.md)|All users|
|[Pre-employment screening](pre-employment-screening.md)|All users|
|[Pre-Employment Screening and Vetting of External Candidates - FAQs](pre-employment-screening-and-vetting-of-external-candidates-faqs.md)|All users|
|[Security clearance appeals policy](security-clearance-appeals-policy.md)|All users|

#### During employment

|[Ongoing Personnel Security](ongoing-personnel-security.md)|All users|
|[Personnel risk assessment](personnel-risk-assessment.md)|All users|
|[Reporting personal circumstance changes](reporting-personal-circumstance-changes.md)|All users|
|[Training and Education](training-and-education.md)|All users|
|[Voluntary drug testing policy](voluntary-drug-testing-policy.md)|All users|
|[Voluntary drug testing policy procedures](voluntary-drug-testing-policy-procedures.md)|All users|

#### Termination and change of employment

|[End or change of employment](end-or-change-of-employment.md)|All users|
|[Leavers with NSC and NSVCs](leavers-with-nsc-and-nscvs.md)|All users|

### Asset management

#### Responsibility for assets

|[Acceptable use](acceptable-use.md)|All users|
|[Acceptable use policy](acceptable-use-policy.md)|All users \(Policy\)|
|[Guidance on IT Accounts and Assets for Long Term Leave](long-term-leave.md)|All users|
|[IT Acceptable Use Policy](it-acceptable-use-policy.md)|All users \(Policy\)|
|[Protect Yourself Online](protect-yourself-online.md)|All users|
|[Web browsing security](web-browsing.md)|All users|

#### Information classification

|[Data Handling and Information Sharing Guide](data-handling-and-information-sharing-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Government Classification Scheme](government-classification-scheme.md)|All users|
|[Information Classification and Handling Guide](information-classification-handling-and-security-guide.md)|All users|
|[Information Classification and Handling Policy](information-classification-and-handling-policy.md)|All users \(Policy\)|
|[`OFFICIAL` and `OFFICIAL-SENSITIVE`](official-official-sensitive.md)|All users|
|[Secrets management](secrets-management.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

#### Media handling

|[Removable media](removable-media.md)|All users|
|[Secure disposal of IT equipment](secure-disposal-of-it-equipment.md)|All users|
|[Secure disposal of IT - physical and on-premise](secure-disposal-of-it-physical-and-on-premise.md)|All users|

### Access control

#### Business requirements of access control

|[Access Control Guide](access-control-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Access Control Policy](access-control-policy.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Enterprise Access Control Policy](enterprise-access-control-policy.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Privileged Account Management Guide](privileged-account-management-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

#### User access management

|[Authentication](authentication.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Management access](management-access.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Managing User Access Guide](managing-user-access-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Multi-Factor Authentication](multi-factor-authentication-mfa-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Privileged User Backups, Removable Media and Incident Management Guide](privileged-user-backups-removable-media-and-incident-management-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Privileged User Configuration, Patching and Change Management Guide](privileged-user-configuration-patching-and-change-management-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Privileged User Guide](privileged-user-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Privileged User Logging and Protective Monitoring Guide](privileged-user-logging-and-protective-monitoring-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

#### User responsibilities

|[Protecting Social Media Accounts](protecting-social-media-accounts.md)|All users|

#### System and application access control

|[Account management](account-management.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Authorisation](authorisation.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Multi-user accounts and Public-Facing Service Accounts Guide](multi-user-accounts-and-public-facing-service-accounts-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Password Creation and Authentication Guide](password-creation-and-authentication-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Password Management Guide](password-management-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Password Managers](password-managers.md)|All users|
|[Passwords](passwords.md)|All users|
|[Password Storage and Management Guide](password-storage-and-management-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Policies for Google Apps administrators](policies-for-google-apps-administrators.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Policies for MacBook Administrators](policies-for-macbook-administrators.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[System User and Application Administrators](system-users-and-application-administrators.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Using LastPass Enterprise](using-lastpass.md)|All users|

### Cryptography

#### Cryptographic controls

|[Automated certificate renewal](automated-certificate-renewal.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Cryptography](cryptography.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[HMG Cryptography Business Continuity Management Standard](hmg-cryptography-business-continuity-management-standard.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Public Key Infrastructure Policy](public-key-infrastructure-policy.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Use of HMG Cryptography Policy](use-of-hmg-cryptography-policy.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

### Physical and environmental security

#### Secure areas

|[Physical Security Policy](physical-security-policy.md)|All users|

#### Equipment

|[Clear Screen and Desk Policy](clear-screen-and-desk.md)|All users|
|[Equipment Reassignment Guide](equipment-reassignment-guide.md)|All users|
|[Laptops](laptops.md)|All users|
|[Locking and shutdown](locking-and-shutdown.md)|All users|
|[Policies for MacBook Users](policies-for-macbook-users.md)|All users|
|[System Lockdown and Hardening Standard](system-lockdown-and-hardening-standard.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

### Operations security

#### Operational procedures and responsibilities

|[Active Cyber Defence: Mail Check](mail-check.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Active Cyber Defence: Public Sector DNS](public-sector-dns.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Active Cyber Defence: Web Check](web-check.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Offshoring Guide](offshoring-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

#### Protection from malware

|[Malware Protection Guide \(Overview\)](malware-protection-guide-introduction.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Malware Protection Guide: Defensive Layer 1](malware-protection-guidance-defensive-layer-1.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Malware Protection Guide: Defensive Layer 2](malware-protection-guidance-defensive-layer-2.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Malware Protection Guide: Defensive Layer 3](malware-protection-guidance-defensive-layer-3.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Ransomware](ransomware.md)|All users|

#### Backup

|[System backup guidance](system-backup-guidance.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[System backup policy](system-backup-policy.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[System backup standard](system-backup-standard.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

#### Logging and monitoring

|[Accounting](accounting.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Commercial off-the-shelf applications](cots-applications.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Custom Applications](custom-applications.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Logging and monitoring](logging-and-monitoring.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Online identifiers in security logging and monitoring](online-identifiers.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Protective Monitoring](protective-monitoring.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Security Log Collection](security-log-collection.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Security Log Collection: Enterprise IT - Infrastructure](enterprise-it-infrastructure.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Security Log Collection: Enterprise IT - Mobile Devices](enterprise-it-mobile-devices.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Security Log Collection: Hosting Platforms](hosting-platforms.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Security Log Collection: Log entry metadata](log-entry-metadata.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Security Log Collection: Maturity Tiers](security-log-collection-maturity-tiers.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

#### Control of operational software

|[Guidance for using Open Internet Tools](guidance-for-using-open-internet-tools.md)|All users|

#### Technical vulnerability management

|[Patch management guide](patch-management-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Vulnerability Disclosure](vulnerability-disclosure-policy.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Vulnerability Disclosure: Implementing `security.txt`](implement-security-txt.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Vulnerability scanning and patch management guide](vulnerability-scanning-and-patch-management-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Vulnerability scanning guide](vulnerability-scanning-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

### Communications security

#### Network security management

|[Code of Connection Standard](code-of-connection-standard.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Defensive domain registrations](defensive-domain-registration.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Internet v. PSN](internet-v-psn.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[IP DNS Diagram Handling](ip-dns-diagram-handling.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Multiple Back-to-back Consecutive Firewalls](multiple-consecutive-back-to-back-firewalls.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Networks are just bearers](networks-bearers-not-trust.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

#### Information transfer

|[Bluetooth](bluetooth.md)|All users|
|[Criminal Justice Secure Mail \(CJSM\)](cjsm.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Data Sovereignty](data-sovereignty.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Email](email.md)|All users|
|[Email Authentication Guide](email-authentication-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Email Security Guide](email-security-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[General Apps Guidance](general-user-video-and-messaging-apps-guidance.md)|All users|
|[Secure Data Transfer Guide](secure-data-transfer-guide.md)|All users|
|[Secure Email Transfer Guide](secure-email-transfer-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Spam and Phishing Guide](spam-and-phishing-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Web browsing security policy profiles](web-browsing-security-policy-profiles.md)|All users \(Policy\)|

### System acquisition, development and maintenance

#### Security requirements of information systems

|[Technical Security Controls Guide](technical-security-controls-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Technical Security Controls Guide: Defensive Layer 1](technical-security-controls-guide-defensive-layer-1.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Technical Security Controls Guide: Defensive Layer 2](technical-security-controls-guide-defensive-layer-2.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

#### Security in development and support processes

|[Maintained by Default](maintained-by-default.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Secure by Default](secure-by-default.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Source Code Publishing](source-code-publishing.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[System Test Standard](system-test-standard.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

#### Test data

|[Using Live Data for Testing purposes](using-live-data-for-testing-purposes.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

### Supplier relationships

#### Information security in supplier relationships

|[Suppliers to MoJ: Assessing Suppliers](assessing-suppliers.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Suppliers to MoJ: Contracts](contracts.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Suppliers to MoJ: Security Aspect Letters](security-aspect-letters.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Suppliers to MoJ: Supplier Corporate IT](supplier-corporate-it.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

#### Supplier service delivery management

|[Baseline for Amazon Web Services accounts](baseline-aws-accounts.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

### Information security incident management

#### Management of information security incidents and lost devices

|[Forensic Principles](forensic-principles.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Forensic Readiness Guide](forensic-readiness-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Forensic Readiness Policy](forensic-readiness-policy.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Incident Management Plan and Process Guide](incident-management-plan-and-process-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[IT Incident Management Policy](it-incident-management-policy.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Lost devices or other IT security incidents](lost-devices-incidents.md)|All users|
|[Reporting an incident](reporting-an-incident.md)|All users|

### Information security aspects of business continuity management

#### Information security continuity

|[IT Disaster Recovery Plan and Process Guide](it-disaster-recovery-plan-and-process-guide.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[IT Disaster Recovery Policy](it-disaster-recovery-policy.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

### Compliance

#### Compliance with legal and contractual requirements

|[Data Destruction](data-destruction.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Data Destruction: Contract Clauses - Definitions](data-destruction-contract-clauses-definitions.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Data Destruction: Contract Clauses - Long Format](data-destruction-contract-clauses-long-format.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Data Destruction: Contract Clauses - Long Format \(Appendix\)](data-destruction-contract-clauses-long-format-appendix.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Data Destruction: Contract Clauses - Short Format](data-destruction-contract-clauses-short-format.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Data Destruction: Instruction and Confirmation Letter](data-destruction-instruction-and-confirmation-letter.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Data Security and Privacy](data-security-and-privacy.md)|All users|
|[Data Security & Privacy Lifecycle Expectations](data-security-and-privacy-lifecycle.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|
|[Data Security & Privacy Triage Standards](data-security-and-privacy-triage-standards.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

#### Information security reviews

|[Standards Assurance Tables](standards-assurance-tables.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

### Risk Assessment

#### Risk Management

|[Infrastructure and system accreditation](infrastructure-system-accreditation.md)|Technical Architect, DevOps, IT Service Manager, Software Developer|

#### Risk Assessment Process

|[Risk reviews](risk-reviews.md)|All users|

## Other Guidance

A glossary of some terms used in this guidance is available [here](glossary.md).

A more extensive list of acronyms is available [here](https://ministryofjustice.github.io/acronyms/).

### Technical Guidance

The MoJ [Technical Guidance](https://ministryofjustice.github.io/technical-guidance/) should be read together with this security-focused guidance.

The [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security) provides the base material for all security guidance in the MoJ.

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

