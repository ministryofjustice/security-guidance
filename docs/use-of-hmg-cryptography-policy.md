# Use of HMG Cryptography Policy

## Legacy information

**Note:** This document is Legacy IA Policy material. It is under review and likely to be withdrawn or substantially revised soon. Before using this content for a project, contact [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

**Note:** This document might refer to several organisations, information sources, or terms that have been replaced or updated, as follows:

-   CESG \(Communications-Electronics Security Group\), refer to the National Cyber Security Centre \(NCSC\), contact [security@justice.gov.uk](mailto:security@justice.gov.uk).
-   CINRAS \(Comsec Incident Notification Reporting and Alerting Scheme\), refer to the NCSC, contact [security@justice.gov.uk](mailto:security@justice.gov.uk).
-   ComSO \(Communications Security Officer\), contact the Chief Information Security Officer \(CISO\) \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   `CONFIDENTIAL`, an older information classification marking, see [Information Classification and Handling Policy](information-classification-and-handling-policy.md).
-   CPNI \([Centre for the Protection of the National Infrastructure](https://www.cpni.gov.uk/)\), contact the CISO \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   DSO \(Departmental Security Officer\), contact the Senior Security Advisor \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   GPG6 \(Good Practice Guide 6: Outsourcing and Offshoring: Managing the Security Risks\), refer to the NCSC, contact [security@justice.gov.uk](mailto:security@justice.gov.uk).
-   IS1 \(HMG Infosec Standard 1 Technical Risk Assessment\), see the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   IS2 \(HMG Infosec Standard 2 Information Risk Management\), see the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   IS4 \(HMG Infosec Standard 4 Communications Security and Cryptography\), see the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   IS6 \(HMG Infosec Standard 6 Protecting Personal Data and Managing Information Risk\), see the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   ITSO \(Information Technology Security Officer\), contact the CISO \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   `RESTRICTED`, an older information classification marking, see [Information Classification and Handling Policy](information-classification-and-handling-policy.md).
-   SPF \([Security Policy Framework](https://www.gov.uk/government/publications/security-policy-framework)\), see the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security), contact [security@justice.gov.uk](mailto:security@justice.gov.uk).

## About this document

This document is the Ministry of Justice \(MoJ\) IT Security – Use of HMG Cryptography Policy. It provides the core set of principles, expectations, roles and responsibilities for using HMG cryptographic material.

### How to use this document

Each policy statement outlines a security requirement and where applicable, a reference is provided to further material. A unique identifier is associated with each statement for easy reference. The format of each statement is illustrated below:

-   **POL.CRYPTO.XXX**

    Policy statement text.


The policies outlined in this document form the baseline standard. However this policy is not a replacement for HMG Information Assurance Standard No. 4 - Management of Cryptographic Systems \[Ref, 2\]. HMG IAS4 remains the primary reference source where this policy provides a supplement to it.

## Use of HMG Cryptography Policy

### Introduction

-   **POL.CRYPTO.001**

    It is the policy of the MoJ to follow the policy of HMG Information Assurance Standard 4. This document endorses and augments that policy. Where the local policy contained herein, if different to HMG Policy, the local policy overrides HMG policy and must be adhered to.


### Scope

This policy is concerned with the use of HMG cryptographic material used on any MoJ IT system and/or where HMG cryptographic material is obtained through the MoJ.

### Purpose

MoJ uses a wide range of cryptography products or various classifications and is serviced by several suppliers. This policy is intended to supplement the HMG IAS4 \[Ref, 2\] and assist suppliers to procure encryption from CESG and manage its life cycle.

### Audience

Anyone who wants to obtain encryption from CESG and everyone who is, or needs to be, CRYPTO or ACCSEC authorised \(see glossary\) to handle Key Variables \(KV\) or hardware.

In accordance with HMG IAS4 \[Ref, 2\] encryption is only provided for fully accredited systems. There are long lead times to obtain encryption products from CESG \(which fluctuate between 8-12 weeks and are always subject to change\). It is recognised that there needs to be some flexibility in the process to order encryption and this guide helps meet that requirement.

### Definitions

-   **Trusted Hand**

    An individual who is at least BPSS cleared and recognised as a member of staff of a supplier.


### Communication

-   **POL.CRYPTO.002**

    The use of secure email **must be** used a primary method of communication for all and any communications from suppliers in respect of cryptography to the MoJ Crypto Custodian, Communications Security Officer \(COMSO\) and IT Security Officer \(ITSO\) regardless of whether the protective marking is UNCLASSIFIED or NOT PROTECTIVELY MARKED and up to RESTRICTED.


Acceptable secure e-mail methods are GSi, xGSi and CJSM accounts. All queries towards CESG must be forwarded to the MoJ Crypto Custodian and/or COMSO. CESG must not be contacted direct.

### New requirements for encryption and/or hardware

As soon as the need for encryption is identified the system Accreditor, the COMSO must be informed by the Project Manager and agreement sought for the need for the hardware, software and encryption from CESG.

The process requires that an applicant is appointed and that applicant is responsible for ensuring that the product is suitable for the requirement and it is their responsibility to familiarise themselves with the CESG Security Operating Procedures \(SyOPs\) for that product. The applicant can delegate this element to someone else but that person must be identified to the other parties of this approval process.

-   **POL.CRYPTO.003**

    The Project Manager **must appoint** an applicant. Exceptionally, the applicant can be the Project Manager. The applicant **must contact** the vendor of the encryption product and obtain the latest version of the CESG macro enabled word application form to complete.


This form must be completed by the applicant with a full explanation of the requirement and attached with, if appropriate, a diagram \(e.g. MS Visio diagram\) which explains the solution and this must be sent to the COMSO, Accreditor and MoJ Crypto Custodian for approval with the application form.

**Note:** The applicant is responsible for ensuring that the product is suitable and meets the desired business requirement.

If the solution requiring encryption has not yet been Accredited \(at the time the application is being drafted\), or if the current RMADS need to be updated to accommodate this requirement, a timetable must be set out for the delivery of draft RMADS and SyOPs, this **must be** attached to the application form.

The COMSO and Accreditor must both approve and notify the MoJ Crypto Custodian in order for the form to be sent to CESG for processing.

If any of the conditions above have not been met the form cannot be processed and this may cause delays.

Further processing is required by the MoJ Crypto Custodian and upon dispatch to CESG the MoJ Crypto Custodian will give the applicant a reference number \(hereafter referred to as the IAB account number\) which must be referred to in any future communications regarding the requirement.

### Increase in a community \(usage of Crypto\)

When it is necessary to increase the number of licences, changes to hardware or otherwise change how Crypto used, the applicant must obtain the latest form from the vendor and send the form to the Accreditor and COMSO for approval. The applicant must refer to the CESG X reference which can be found in the documentation that the supplier holds.

-   **POL.CRYPTO.004**

    The applicant **must determine** whether or not a change to the RMADS or SyOPs are necessary and confirm this on application. If changes are required it must be declared how and when this will happen.

-   **POL.CRYPTO.005**

    The Accreditor and COMSO **must** both agree and approve the change and advise the MoJ Crypto Custodian.


The MoJ Crypto Custodian will forward the approved form to CESG for processing and any notifications from CESG will be advised by the MoJ Crypto Custodian to the applicant.

### Authority to Operate Certificate

The MoJ Crypto Custodian and the Vendor will be advised by CESG of the Authority to operate and this will be forwarded to the applicant by the MoJ Crypto Custodian, with this certificate the applicant can purchase the relevant hardware or licences from the vendor.

It is the responsibility of the applicant to raise any relevant purchase orders though the MoJ purchase order system or progress the financial procurement for the product through other channels.

### CRYPTO and ACCSEC authorisation

If there is a requirement to store Key Variables locally, the supplier must appoint a Local Crypto Custodian \(LCC\) and Local Alternate Crypto Custodian \(LACC\). Both must attend the CESG training course for Crypto Custodians and be sponsored by the MoJ Crypto Custodian.

Any subject who handles Key Variables for the MoJ must be SC cleared and CRYPTO or ACCSEC authorised initially by the MoJ Crypto Custodian. The subject must provide the details on the Crypto Authorisation form through secure channels and provide the contact details of the vetting office which approved their clearance.

-   **POL.CRYPTO.006**

    Every 12 months the LCC and LACC **must re-authorise** each other and check that their clearances are still valid and this must be evidenced and recorded with the authorisation form for audit purposes.


If the LCC or LACC CRYPTO or ACCSEC authorises anyone else locally, there are responsible for checking the security clearances and maintaining and renewing the authorisation or de-authorisation process and keeping records available for inspection and audit by the MoJ Crypto Custodian or Authority.

### Delivery of Key Variables

When Key Variables arrives and has been checked and recorded by the MoJ Crypto Custodian an email will be sent to the applicant to inform them that their Key Variables has arrived.

### Key Variables distribution

All Key Variables is stored and managed centrally by the MoJ with some exceptions such as hard disk encryption which suppliers need to store locally.

There are special arrangements for the local storage of Key Variables which must be agreed with the COMSO.

-   **POL.CRYPTO.007**

    Key Variables **must not** be deployed unless the encryption solution is accredited or the timetable has been set out and agreed on its delivery, draft RMADS and final SyOPs must be made available to the MoJ Crypto Custodian.

-   **POL.CRYPTO.008**

    The applicant **must agree** with the MoJ Crypto Custodian how the Key Variables is to be deployed, or provide the details of the person who will manage this if it is not the applicant. Generally speaking the Key Variables is retained at MoJ HQ and issued out for a short period of time in order to encrypt the system and then returned to MoJ HQ for storage.


Key Variables distribution as follows \(in order of preference\);

1.  Collected from and returned to MoJ HQ by a CRYPTO or ACCSEC authorised person and transported in a secure lockable container \(such as a lockable briefcase or a CPNI approved transportation container\).

2.  Collected and returned by trusted hand for transportation in a secure lockable container to a CRYPTO or ACCSEC authorised person in tamper evident packaging using the usual Government Protective Marking Scheme \(GPMS\).

3.  Dispatched from and returned by a reputable courier who guarantees delivery within 24 hours and provides a tracking service \(not Royal Mail\). The Key Variables must be sealed within tamper evident packaging and appropriately protected. Suppliers must take full responsibility for this process and arrange for courier to collect and return.


### Key Variables Management

-   **POL.CRYPTO.009**

    The management of Key Variables **must be** in accordance with HMG IAS4 Supplement 7 \[Ref, 3\].


### Key Variables Destruction

-   **POL.CRYPTO.010**

    Suppliers **must not** under any circumstances destroy Key Variables. All Key Variables must be returned to the MoJ Crypto Custodian for destruction.


### Business continuity

-   **POL.CRYPTO.011**

    The MoJ Crypto Custodian, the Alternate Crypto Custodian and any authorised signatories and or people who have access to the safes where cryptographic material that is managed by the MoJ Crypto Custodian is stored must conform to the IT Security Policy - HMG Cryptography Business Continuity Management Standard \[Ref, 4\].


### Annual Audit of Crypto

Every 12 months the COMSO will inspect the arrangements for sites locally storing Key Variables. A date will be agreed with the COMSO to inspect the premises, audit the paperwork and check the crypto stock.

## References

|ID|Title|Version / Issue|
|--|-----|---------------|
|1|IT Security Policy|V1-00|
|2|HMG IS4 - Management of Cryptographic Systems|Issue 5.1, Apr 2011|
|3|HMG IS4 - Supplement No.7 - Accounting of Cryptographic Items|Issue 1.0, Apr 2011|
|4|IT Security Policy - HMG Cryptography Business Continuity Management Standard|V0-01|

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

