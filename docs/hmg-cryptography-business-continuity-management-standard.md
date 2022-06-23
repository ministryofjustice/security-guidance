# HMG Cryptography Business Continuity Management Standard

## Legacy information

**Note:** This document is Legacy IA Policy material. It is under review and likely to be withdrawn or substantially revised soon. Before using this content for a project, contact [security@justice.gov.uk](mailto:security@justice.gov.uk).

**Note:** This document might refer to several organisations, information sources, or terms that have been replaced or updated, as follows:

-   CESG \(Communications-Electronics Security Group\), refer to the National Cyber Security Centre \(NCSC\), contact [security@justice.gov.uk](mailto:security@justice.gov.uk).
-   CINRAS \(Comsec Incident Notification Reporting and Alerting Scheme\), refer to the NCSC, contact [security@justice.gov.uk](mailto:security@justice.gov.uk).
-   ComSO \(Communications Security Officer\), contact the Chief Information Security Officer \(CISO\) \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   **Confidential**, an older information classification marking, refer to [Information Classification and Handling Policy](information-classification-and-handling-policy.md).
-   CPNI \([Centre for the Protection of the National Infrastructure](https://www.cpni.gov.uk/)\), contact the CISO \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   DSO \(Departmental Security Officer\), contact the Senior Security Advisor \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   GPG6 \(Good Practice Guide 6: Outsourcing and Offshoring: Managing the Security Risks\), refer to the NCSC, contact [security@justice.gov.uk](mailto:security@justice.gov.uk).
-   IS1 \(HMG Infosec Standard 1 Technical Risk Assessment\), refer to the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   IS2 \(HMG Infosec Standard 2 Information Risk Management\), refer to the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   IS4 \(HMG Infosec Standard 4 Communications Security and Cryptography\), refer to the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   IS6 \(HMG Infosec Standard 6 Protecting Personal Data and Managing Information Risk\), refer to the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   ITSO \(Information Technology Security Officer\), contact the CISO \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   **Restricted**, an older information classification marking, refer to [Information Classification and Handling Policy](information-classification-and-handling-policy.md).
-   SPF \([Security Policy Framework](https://www.gov.uk/government/publications/security-policy-framework)\), refer to the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security), contact [security@justice.gov.uk](mailto:security@justice.gov.uk).

## Introduction

### Scope

This Business continuity plan is limited to all HMG cryptographic material procured by the Ministry of Justice \(MoJ\) Crypto Custodian for and on behalf of any part of the MoJ with the exception of BRENT encryption requirements.

### Who needs to read this document

This document is for the MoJ Crypto Custodian, the Alternate Crypto Custodian and any authorised signatories and or people who have access to the safes where encryption that is managed by the MoJ Crypto Custodian is stored.

### Background

All HMG encryption is procured from CESG which is the National Technical Authority for Information Assurance and is based in GCHQ. It is typically produced to support a [CESG Assisted Products Service \(CAPS\)](https://www.ncsc.gov.uk/information/products-cesg-assisted-products-service) product which means that it has gone through rigorous testing to give HMG assurance that it is secure. HMG Cryptography is produced under special circumstances to provide additional assurance and that process, distribution and storage of this material is protected and secure.

HMG has specific standards on the management of Crypto and other associated products called the HMG IS4, it is the policy of the MoJ to follow and comply with HMG IS4 and this document is intended to support and augment that standard.

## Encryption Media

### Types of encryption and how they are distributed

Key Variables are typically loaded onto Floppy discs, or CD.

#### Hard disc encryption

Products such as Becrypt, Eclypt and Bitlocker are procured and distributed to by suppliers through the MoJ Crypto Custodian and transferred to them to deploy and manage for the lifetime of the key variable which is determined by the CESG Security Operating Procedures \(SyOPs\).

#### Transmission encryption

Products such as XKryptor, Datacryptor and Ultra AEP are procured and managed by the MoJ Crypto Custodian and distributed to suppliers as and when necessary and returned to the MoJ Crypto Custodian for storage.

### Segregation and supersession

Key variables that are issued from CESG are typically issued with two editions. The first is for immediate deployment and the second is for emergency supersession. In the case of hard disc encryption the supplier holds the live edition and the MoJ Crypto Custodian holds any others. All supplier crypto deployment environments are not at the same site as the MoJ Crypto Custodian and this provides natural segregation of the editions.

Eclypt uses a lifetime key variable and does not have more than one edition, In the event of compromise, the usual CINRAS report and request to CESG for emergency replacement of the key variable will be required.

## Protection of Key Variables

All encryption is stored in a [CPNI \(Centre for the Protection of the National Infrastructure\)](https://www.cpni.gov.uk/) Class 4 safe which also has a certified 2 hour burning time. Protecting the safe is a fire suppressant sprinkler system.

Access to the safe is strictly limited to the MoJ Crypto Custodian and the Alternate Crypto Custodian. A copy of the master code for the safe is stored with the Departmental Security Officer. Only the DSO or ITSO are permitted to open the safe in the event of an emergency.

### Work ethic with key variables

The area that the MoJ Custodian works is open plan in an accredited IL3 environment. The DSO has further accredited the immediate area surrounding the MoJ Crypto Custodian in 5.31 of 102 Petty France for Crypto Management on the understanding that the personnel surrounding them are SC cleared and because there are desks immediately by the safe to allow a clear line of site from the Custodian's desk to the safe.

All key variables must be kept in the safe and only removed when specific action is required on a key variable.

## Emergency procedures for evacuation and invacuation

Applicable to anyone who has access to any of the safes:

1.  If the alarms sound return all encryption that is out and in use to the fireproof safe.

2.  **Lock and check** all safes are secure.

3.  Leave by the nearest exit in accordance with Fire Evacuation procedures.


## Post action to emergency evacuation and invacuation

If there has been any damage to any of the encryption stored at the MoJ:

-   Notify CESG immediately on: 01242 221491 extension 31950

    notifying them of the event and request an immediate record of holdings list.

-   A CINRAS report must be generated and issued to: cinras@cesg.gsi.gov.uk

    and a copy to the Security Team: [security@justice.gov.uk](mailto:security@justice.gov.uk)

-   A muster of all key variables and a check against the record of holding list undertaken and an order to CESG raised of any replacement key variables.
-   Upon receipt of a replacement key variable emergency plans to change the key variable of the associated product must begin.

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

