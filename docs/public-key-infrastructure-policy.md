# Public Key Infrastructure Policy

## Legacy information

**Note:** This document is Legacy IA Policy. It is under review and likely to be withdrawn or substantially revised soon. Before using this content for a project, contact [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

**Note:** This document might refer to several organisations, information sources, or terms that have been replaced or updated, as follows:

-   CESG \(Communications-Electronics Security Group\), refer to the National Cyber Security Centre \(NCSC\), contact [security@justice.gov.uk](mailto:security@justice.gov.uk).
-   CINRAS \(Comsec Incident Notification Reporting and Alerting Scheme\), refer to the NCSC, contact [security@justice.gov.uk](mailto:security@justice.gov.uk).
-   ComSO \(Communications Security Officer\), contact the Chief Information Security Office \(CISO\) \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   `CONFIDENTIAL`, an older information classification marking, see [Information Classification and Handling Policy](information-classification-and-handling-policy.md).
-   CPNI \([Centre for the Protection of the National Infrastructure](https://www.cpni.gov.uk/)\), contact the CISO \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   DSO \(Departmental Security Officer\), contact the Senior Security Advisor \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   GPG6 \(Good Practice Guide 6: Outsourcing and Offshoring: Managing the Security Risks\), refer to the NCSC, contact [security@justice.gov.uk](mailto:security@justice.gov.uk).
-   IS1 \(HMG Infosec Standard 1 Technical Risk Assessment\), see the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   IS4 \(HMG Infosec Standard 4 Communications Security and Cryptography\), see the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   IS6 \(HMG Infosec Standard 6 Protecting Personal Data and Managing Information Risk\), see the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   ITSO \(Information Technology Security Officer\), contact the CISO \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   `RESTRICTED`, an older information classification marking, see [Information Classification and Handling Policy](information-classification-and-handling-policy.md).
-   SPF \([Security Policy Framework](https://www.gov.uk/government/publications/security-policy-framework)\), see the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security), contact [security@justice.gov.uk](mailto:security@justice.gov.uk).

## Introduction

### Scope

Within the Ministry of Justice \(MoJ\), there are a number of requirements for Public Key Infrastructure \(PKI\) services to support confidentiality, integrity and authentication. This document defines the mandatory policy requirements for PKI use.

The policy contained in this document refers specifically to PKI Services used for the following functions:

-   PSN Wide Area Network VPN cryptography

-   Server-side certificates for:

    -   Internet applications

    -   Intranet applications

    -   PSN/GSI applications

-   User and Device Certificates for Network Access Control using 802.1x EAP/TLS

-   User certificates for digital signature functions


For PKI Services in respect of other functions, including RAS VPNs, contact the appropriate system Accreditor or MoJ Crypto Custodian.

### Out of Scope

Any information or component, which operates at SECRET or TOP SECRET \(e.g. Private Keys with a classification above OFFICIAL-SENSITIVE\) fall outside of the scope of this policy

Certificates used for authentication of users or organisations used in token or PKI based authentications systems other than 802.1x are out of scope.

### Defined Terms

|Term|Definition|
|Public Key Infrastructure \(PKI\)|A set of hardware, software, people, policies, and procedures needed to create, manage, distribute, use, store, validate and revoke digital certificates.|
|Certificate Authority \(CA\)|An entity that issues digital certificates. Certificate Authorities are hierarchical, with subordinate CAs being authorised to issue certificates by a trusted, top level, "Root" CA.|
|Registration Authority \(RA\)|An entity that validates the identities of actors in a PKI, and processes certificate signing requests and certificate revocation requests on behalf of authorised actors sending these to the CA for processing.|
|Validation authority \(VA\)|A service that authenticates and validates the certificates of a PKI. The VA provides a public key directory and also enables access to certificate revocation information either by providing CRLs or using the OCSP protocol.|
|Certificate Policy \(CP\)|A document that states the different actors of a public key infrastructure \(PKI\), specifying their roles and their duties. Its content and structure is described in [IETF RFC3647](https://tools.ietf.org/html/rfc3647) \[Ref.16\]. This is often a legal document forming part of a contract.|
|Certificate Practice Statement \(CPS\)|A document from a Certificate Authority which describes their practice for issuing and managing public key certificates in line with the root CA Certificate Policy. . Its content and structure is described in [IETF RFC3647](https://tools.ietf.org/html/rfc3647).|
|Certificate Revocation List \(CRL\)|A signed list of certificates \(or more specifically, a list of serial numbers for certificates\) that have been revoked before they expire, and therefore, entities presenting those \(revoked\) certificates should no longer be trusted. CRL is described in [IETF RFC5280](https://tools.ietf.org/html/rfc5280).|
|Online Certificate Status Protocol \(OCSP\)|An Internet protocol used for obtaining the revocation status of an X.509 digital certificate. It is described in [IETF RFC 6960](https://tools.ietf.org/html/rfc6960)|
|Trust Anchor|An authoritative entity for which trust is presumed and not derived. Root CAs must be Trust Anchors.|
|Certificate Signing Request \(CSR\)|A message sent from an applicant to a certificate authority in order to apply for a digital identity certificate. Normally complies with PKCS \#10 as defined in [IETF RFC 2986](https://tools.ietf.org/html/rfc2986)|
|Certificate Revocation Request \(CRR\)|A message sent from the registered owner of a digital certificate to a certificate authority in order to revoke a compromised digital certificate. Normally complies with PKCS \#10 as defined in [IETF RFC 2986](https://tools.ietf.org/html/rfc2986).|
|Key|A piece of information that determines the functional output of a cryptographic algorithm or cipher.|
|Public Key Cryptography|A class of cryptographic algorithms which requires two separate keys, one of which is kept private \(secret\) and one of which is made public usually embedded in a certificate.|
|Private Key \(PrK\)|A secret key used to decrypt or digitally sign information.|
|Public Key \(PuK\)|A non-sensitive key that is used to encrypt information or validate digital signatures.|
|PKI Services|The services provided in the delivery of Public Key Infrastructure. PKI Services includes those provided either as a root or subordinate Certificate Authority, Registration Authority, and Validation Authority. The usage of digital certificates for cryptography or digital signatures within applications and other IT systems is not considered a PKI Service, but those systems would consume PKI Services.

|
|PKI Customer|An entity \(a user or organisation\) that is authorised to access the PKI Services for the purposes of signing or revoking digital certificates. Some PKI customers may also provide delegated PKI Services.|

## General PKI Policy

### Overview

This section describes the common PKI policy that applies regardless of the type of PKI service in question. It covers the following subsections:

-   Governance Structure

-   Technical Architecture

-   Operational Policy

-   Process Requirements


### Governance Structure

#### Roles and Responsibilities

-   Senior Information Risk Owner \(SIRO\) – Responsible for all risks to do with the PKI Services. Final point of escalation for incidents.

-   Departmental Security Officer \(DSO\) – Responsible for the operational governance of the PKI Services and the report line for the ComSO.

-   Communication Security Officer \(ComSO\) – Responsible for day to day management of the PKI Services, relationship management with CESG and UKKPA \(GCHQ's UK key production authority\), mustering and other formal processes. First point of escalation for incidents and managing initial incident response.

-   Crypto Custodians – Responsible for day to day operation of the PKI services, including the distribution of keys from the UKKPA. Where keymat is provided from the UKKPA they shall be formally trained and authorised Crypto Custodians. For other services they should be formally trained. Note that the Authority's Crypto Custodian may delegate key management responsibilities to Supplier Crypto Custodians.

-   IT Security Officer \(ITSO\) – Responsible for operational IT security management.

-   Administrators – Responsible for configuration, maintenance and support of the PKI services

-   Auditors – Internal and external auditors including UKKPA and MoJ Information Assurance who ensure that the PKI Services are running within specification and comply with legal and regulatory requirements, HMG Policy and MoJ Policy.


#### Incident Response

1.  There shall be an Incident Response and Escalation process in place.

2.  The incident response process shall cover procedures for:


-   Impact minimisation

-   Escalation

-   CRL issue

-   Digital Forensics

-   BC / DR


1.  The escalation shall be from the person discovering the incident to the local Crypto Custodian, then the MoJ Cypto Custodian, then ComSO, then DSO then SIRO. Escalation to CINRAS and other external bodies shall only be performed by the ComSO, DSO or SIRO.


#### User Registration

1.  Any individual who requires access to the IT Systems providing PKI Services shall be subject to stringent background checks shall be vetted to at least Security Check \(SC\) before any access to the system is permitted.

2.  **Important:** Interim access pending security clearance must not be allowed under any circumstances. The impact of allowing such access in the event that the individual is not subsequently cleared would be to revoke and reissue all certificates signed by the PKI Services.

3.  When clearance is confirmed and identity is validated by MoJ, the user shall be enrolled in the services required and shall be issued with the relevant credentials for access.

4.  Users shall be removed from the systems and their credentials revoked as soon as they leave the role related to the PKI Services. The relevant HR Processes must be reviewed, and updated if necessary, to account for this policy.


#### Authentication

1.  All Users of the PKI Services shall be authenticated beyond reasonable doubt for the purposes of legal admissibility of evidence in accordance with BS 10008. Password strength, complexity and expiry rules must comply with [MoJ Password requirements](passwords.md).

2.  Access to Root CA Services must be subject to multi-factor authentication and subject to two-man rule.

3.  Access to specific signing functions shall be subject to specific authentication and access control policies including two man rule.


#### Accounting

1.  Auditing and accounting of all PKI functions must be carried out in accordance with HMG Good Practice Guide 13. The integrity and confidentiality of accounting logs must maintained to British Standard BS 10008 as appropriate for legal admissibility of evidence, in the event that disputes need to be heard in a court of law.

2.  Internal audit by authorised auditors shall take place at least every quarter

3.  Where PKI Services are subordinate to external services, e.g. UKKPA or PSNA, then the audit and accounting regime must comply with the policies of the relevant authority.

4.  Audit reports shall be provided to the DSO and SIRO quarterly.


#### Compliance

1.  The PKI Services shall at all times comply with Legal and Regulatory requirements including \(but not limited to\):


-   Data Protection Act \(1998 and 2003\)

-   Official Secrets Act \(1989\)

-   Cryptography Export Regulations

-   Regulation of Investigatory Powers Act \(2002\) \(RIPA\) Part 3

-   Export Controls Act \(2002\)

-   Electronic Communications Act 2000

-   SI 2002/318 The Electronic Signatures Regulations 2002


1.  The PKI Services shall at all times comply with HMG Policy including:


-   Security Policy Framework

-   HMG IA Standard 4

-   HMG IA Standard 5


1.  The PKI Services shall at all times comply with any Code of Connection, Memorandum of Understanding or other connection criteria that applies to the environment in which the services are deployed. These shall include as a minimum:


-   PSN Code of Connection

-   GSI Code of Connection \(while GSI connections remain\)


### Technical Architecture

#### Technical Design Considerations

The design of PKI systems must ensure:

-   Resilience

    -   Redundancy

    -   Business Continuity

    -   Disaster Recovery

-   Accessibility

    -   Availability of Registration; Enrolment; and Validation services

-   Security

    -   Confidentiality of system assets \(hardware, operating systems, and software\)

    -   Confidentiality of PKI assets \(private keys, authentication credentials etc\)

    -   Integrity of PKI assets

    -   Availability of PKI services

    -   Confidentiality, Integrity and Availability of information assets that are protected by PKI assets

-   Assurance

    -   System and Product Assurance: Products should be assured to a formal evaluation recognised by the Authority and appropriate to the sensitivity of the material being processed. For cryptographic material this is normally CESG Assisted Products Scheme \(CAPS\) or CESG Product Assurance \(CPA\). Other assurances, such as FIPS 140-2 \(Level 2 or better\) may be permitted in some cases and, in exceptional circumstances, other forms of assurance may be considered. Where system assurance is required, at the discretion of the Accreditor, then a formalised process will be necessary, e.g. Bespoke Assurance by a CESG approved company. In some cases, again at the discretion of the Accreditor, an IT Health Check may be scoped to provide the necessary assurance.

    -   Service Assurance: The security aspects of the service e.g. forensic readiness, auditing, accounting, processes and procedures will be assured through the formal process of accreditation.


### Operational Policies

#### General Operational Policy

1.  The MoJ Crypto Custodian must be informed of any IT system deployed in support of PKI Services including:


-   Certificate Authority devices and software

-   Key generating devices

-   Random number generating devices used to create entropy for cryptographic components

-   Removable media used to transport Certificates and Signing Requests

-   Certificate Revocation List services, including OCSP responders


1.  The MoJ Crypto Custodian reserves the right to audit equipment and processes used in the delivery of PKI Services. The MoJ Crypto Custodian requires that all cryptographic components are managed and processed in accordance with HMG Standard IAS4.

2.  Any remedial action required by the MoJ Crypto Custodian, to meet the requirements of HMG IAS4. must be agreed and implemented within reasonable timescales set by the MoJ Crypto Custodian. "Reasonable timescales" means with sufficient time for the supplier to assess the remediation impact, acquire materials for compliance, test the remediation, and to schedule and deploy the remediation on the production equipment with minimum disruption to MoJ business.

3.  The Crypto Custodian may require key escrow of private keys for lawful purposes. The Crypto Custodian will specify the means by which key material may be exported, stored and transported.


Key escrow may be used for encryption keys but shall under no circumstances be used for signing keys, especially those for use with digital signatures.

#### Trust Anchor Operational Policy

1.  Root CAs for services shared with other parties must be appropriate for the other parties. Trust Anchors for PKI used to deliver services to external parties may be provided by external authorities, e.g. commercial roots, PSN or UKKPA.

2.  Root CAs must be off-line to prevent direct attack against the top level trust anchor. Root CAs shall have appropriate controls, as agreed with the Crypto Custodian and reviewed every six months, to protect the signing functions when in operation.

3.  The Trust Anchor or root Certificate Authority for all FITS services shall be one of the following, as applicable for the specific use case\(s\) for each FITS service:


-   Provided by UKKPA where required; or

-   Provided as a standalone/offline capability as the default for most FITS services; or

-   Provided by a suitable Commercial CA, as agreed with the Authority, where appropriate for external-facing services.


1.  The Trust Anchor shall only be used for signing Sub-CA or Issuing CA certificates and related CRLs.

2.  Assurance of the Trust Anchor CA shall be appropriate to the data assets protected by the digital certificates, as agreed with the Crypto Custodian and Accreditor. For OFFICIAL and OFFICIAL-SENSITIVE material, recognised assurances are stated below:


-   CAPS Baseline

-   CPA Foundation

-   FIPS140-2 \(Level 2\)

-   Other assurance \(permitted in exceptional circumstances when other assurances are not available, and must be supported by a business case, agreed with Accreditor, and signed off by the IAO or SIRO\)


#### Registration Authority Operational Policy

1.  The Registration Authority \(RA\) shall identify, validate and authorise PKI Customers, i.e. organisations that are permitted to make certificate signing requests of the PKI Service. The RA shall also identify, validate and authorise nominated representatives of the PKI Customer, i.e. individuals who are authorised to represent the PKI Customer in respect of the PKI Services. Authorisation will be dependent upon a mutual agreement between the Authority and the PKI Customer specifying the conditions for registration. This may be in the form of a Memo of Understanding or a formal contract.

2.  Subordinate Registration Authorities, i.e. those that register entities at a lower level in the trust authority than the root, must comply with any obligations set by the root authority, including the right of the root authority to audit compliance.

3.  Identity validation shall comply, where possible, with HMG Good Practice Guide 45 \(Identity Proofing and Verification of an Individual\) and Good Practice Guide 46 \(Organisational Identity\).

4.  A Registration Authority shall register each authorised organisation requesting certificates for subordinate CAs. On registration, the Registration Authority shall ensure that the registered party is provided with the Certificate Policy of the required service. The registered party shall provide a Certificate Practice Statement in response.

5.  The PKI Customer shall at all times have at least two nominated representatives registered with the RA that can act on behalf of the Customer and are authorised to submit CSRs, CRRs and perform other formal tasks.

6.  The PKI Customer must notify the RA when any of their nominated representatives are no longer authorised to access the services. Individuals will become unauthorised if their security clearance is expired or revoked, if their employment is terminated, if they are under investigation for malpractice, or if they no longer work on the MoJ account.

7.  The RA must notify the appropriate Crypto Custodian for potential escalation in respect of the incidents specified at para 2.4.3.6 or any other relevant security incident.

8.  Certificates issued to PKI Customers must be revoked when the business relationship is ended. It may be permitted to transfer ownership of certificates in some cases where responsibility is transferred to another party, e.g. contract novation, but each case must be individually agreed with the MoJ Crypto Custodian.

9.  Auditing and accounting of RA functions must be carried out in accordance with HMG Good Practice Guide 13. The integrity and confidentiality of accounting logs must maintained to British Standard BS 10008 as appropriate for legal admissibility of evidence, in the event that disputes need to be heard in a court of law.

10. For online submission of CSR and CRR the RA shall use two-factor authentication to authenticate and authorise enrolled users.

11. The CSR/CRR form shall have fields for all mandatory information and attachment of a public key in PKCS\#10 format.

12. The CSR/CRR shall be approved by one person \(e.g. ComSO\) and actioned by another \(e.g. Crypto Custodian\), except in cases where this process is automated. For automated process, e.g. automated generation of device certificates for EUCS client devices, the MoJ Crypto Custodian and ComSo must approve the automation process.

13. The CA shall distribute certificates in PKCS \#7 format to the requestor and VA as appropriate.


#### Certificate Authority Operational Policy

1.  This section is applicable to root and subordinate CAs. For policy that is specific to Trust Anchor CAs, see [here](#general-operational-policy).

2.  Any CA shall be patched against all known vulnerabilities for which a vendor-published patch is available, in accordance with the Authority's patching policy. The operating system supporting the CA must be less than five \(5\) years old and must have three \(3\) or more years of vendor support remaining \(5/3 rule\).

3.  Assurance of CA shall be appropriate to the data assets protected by the digital certificates, as agreed with the Crypto Custodian and Accreditor. For OFFICIAL and OFFICIAL-SENSITIVE material, assurance preferences are stated below:


-   CAPS Baseline

-   CPA Foundation

-   FIPS140-2 \(Level 2\)

-   Other assurance \(permitted in exceptional circumstances when other assurances are not available, and must be supported by a business case, agreed with Accreditor, and signed off by the IAO or SIRO\)


1.  Any CA connected to a network shall be protected from unauthorised access by a security Gateway that minimises the exposure of the CA to attack.

2.  Auditing and accounting of RA functions must be carried out in accordance with HMG Good Practice Guide 13. The integrity and confidentiality of accounting logs must maintained to British Standard BS 10008 as appropriate for legal admissibility of evidence, in the event that disputes need to be heard in a court of law.

3.  The CA shall be operated in accordance with HMG IS4.


#### Validation Authority Operational Policy

1.  Any VA shall provide authorised access to Certificates and the CRL for the associated CA. This should be automated as far as possible with a Public Key Directory \(PKD\).

2.  The VA shall ensure that the Certificates and CRL are properly signed and authentic before they are published.

3.  The VA shall operate a certificate repository that is visible to all authorised users.

4.  Auditing and accounting of VA functions must be carried out in accordance with HMG Good Practice Guide 13. The integrity and confidentiality of accounting logs must maintained to British Standard BS 10008 as appropriate for legal admissibility of evidence, in the event that disputes need to be heard in a court of law.


#### Audit, Accounting and Mustering Policy

1.  All requests \(CSR/CRR\) shall be logged: on receipt; on processing, on certificate/CRL issue and on destruction

2.  All access to the systems and use of credentials including failures shall be logged

3.  All keymat sub-classified as ACCSEC or CRYPTO shall be mustered quarterly, and in accordance with the individual keymat procedures

4.  Audit and accounting logs shall be managed in accordance with BS 10008


#### Change Control Policy

1.  All software shall be patched with the latest security patches. Such patches shall be regression tested before implementation on the live system.

2.  All software version updates and hardware changes, including configuration changes shall be approved by the ComSO and implemented by the Administrator.

3.  All patches and other minor changes shall be approved by a Crypto Custodian or ComSO and implemented via the change control process.

4.  All changes to a trust anchor or standalone/offline root CA shall also be witnessed and signed off by any two of: Crypto Custodians, ComSO, DSO.


#### Physical Security Policy

1.  The PKI Services shall be located in an HMG Government building or Supplier building with appropriate physical controls for OFFICIAL-SENSITIVE information, as assessed by the Authority's DSO or delegated representative.

2.  PKI Services are critical to the security of the information they protect, and therefore should not be housed in open or shared areas. The PKI Services shall be in a room or cage or locked cabinet that has strictly controlled access to named individuals. The strength of the physical controls will depend on the sensitivity of the specific service.

3.  The Trust Anchors and any standalone/offline Root CAs shall be kept in a safe or security cabinet protected by a CPNI Class 2 lock or equivalent when not in use. Only the ComSO and DSO, and their delegated representatives, shall know the combination. The ComSO and DSO shall not have credentials to operate the CA devices.

4.  The combination code must be changed at least annually, and immediately on permanent departure of any personnel who know the code.


#### Personnel Security Policy

1.  The DSO, ComSO, Crypto Custodians, Administrator\(s\), and individuals holding other key PKI roles shall have been subjected to BPSS checking and shall maintain a current and valid SC clearance as a minimum. Evidence of clearance will be maintained in an up-to-date register in a format agreed with the MoJ and made available to the MoJ.

2.  The Crypto Custodians shall have formal training from CESG or MoD on key management and PKI operation.

3.  No other person shall have access to the PKI infrastructure without prior written permission of the DSO.


### Process Requirements

#### Required Processes

1.  The following formal processes shall be written and implemented:
    -   Registration and de-registration of an organisation
    -   Registration and de-registration of an authorised user of the PKI Services
        -   Including identification according to GPG45 and GPG46
        -   Audit trail of identification, role allocation and access rights
    -   Registration of a nominated individual by a registered organisation by the RA
    -   Enrolment
    -   Certificate Expiration and Renewal
    -   Management of requests \(CSR/CRR\) by the RA
    -   Trust Anchor and root CA operation including signing functions
    -   Incident Response, escalation, digital forensics and aftercare
2.  Other processes should also be formalised and documented

#### Required Standards for each function

1.  Certificates shall comply with ITU-T Recommendation X.509 and RFC 5280 unless required for a specific application in which case written approval from the SIRO will be required

2.  CRLs shall comply with X.509 Version 2 and RFC 5280.

3.  All key material management and PKI operations shall be performed in accordance with all relevant HMG standards.


#### Certificate Policy requirements

1.  The CP shall be written by the supplier providing the issuing Certificate Authority in line with RFC3647, Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework

2.  The PKI service shall not re-sign any public key into a certificate. All public keys shall be new and unique.

3.  There shall be a CP for each certificate hierarchy where the scope \(including user base\), use or liability model is different


#### Certification Practices Statement requirements

1.  The CPS shall be written by the supplier providing the issuing Certificate Authority in line with RFC3647, Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework.

2.  There shall be a CPS for each signing certificate.


## References

The following are FITS PKI Policy specific references used within this document.

|Ref:|Title & Location|
|1|HMG Security Policy Framework \(SPF\) v11.0 Nov 2013 [https://www.gov.uk/government/publications/security-policy-framework](https://www.gov.uk/government/publications/security-policy-framework)|
|2|CESG Cryptographic Standards – Cryptographic Mechanisms, Algorithms & Protocols v1.0 July 2010|
|3|CESG Good Practice Guide 13 - Protective Monitoring for HMG ICT Systems v1.7 – Oct 2012|
|4|HMG IA Standard No.4 - Management of Cryptographic Systems v5.3 – Oct 2013|
|5|HMG IA Standard No.4 - Supplement 1 - Roles and Responsibilities v3.0 - Apr 2013|
|6|HMG IA Standard No.4 - Supplement 2 - Concepts and Terminology of Cryptography v1.0 - Apr 2011|
|7|HMG IA Standard No.4 - Supplement 4 - Labelling of Cryptographic Items v2.0 – Nov 2012|
|8|HMG IA Standard No.4 - Supplement 5 - Account Management v1.0 - Apr 2011|
|9|HMG IA Standard No.4 - Supplement 6 - Personnel & Physical Security of Crypto Items v3.0 - Nov 2012|
|10|HMG IA Standard No.4 - Supplement 7 - Accounting of Cryptographic Items v1.0 - Apr 2011|
|11|HMG IA Standard No.4 - Supplement 8 - Movement of Cryptographic Items v1.0 - Apr 2011|
|12|HMG IA Standard No.4 - Supplement 9 - Destruction & Disposal of Cryptographic Items v2.0 - Apr 2012|
|13|HMG IA Standard No.4 - Supplement 10 – Compliance v2.0 – Oct 2013|
|14|HMG IA Standard No.4 - Supplement 11 - Incident Reporting for Cryptographic Items v2.0 - Apr 2012|
|15|HMG IA Standard No.4 - Supplement 13 - Assurance Standards v4.0 – Oct 2013|
|16|RFC 3647 - Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework [http://datatracker.ietf.org/doc/rfc3647/](http://datatracker.ietf.org/doc/rfc3647/)|
|17|RFC 5280 - Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List \(CRL\) Profile [http://datatracker.ietf.org/doc/rfc5280/](http://datatracker.ietf.org/doc/rfc5280/)|
|18|RFC 6960 - Internet X.509 Public Key Infrastructure Online Certificate Status Protocol – OCSP [http://datatracker.ietf.org/doc/rfc6960/](http://datatracker.ietf.org/doc/rfc6960/)|
|19|[https://shop.bsigroup.com/SearchResults/?q=BIP%200008](https://shop.bsigroup.com/SearchResults/?q=BIP%200008)-   BIP 0008-1:2008 Evidential weight and legal admissibility of information stored electronically. Code of Practice for the implementation of BS 10008
-   BIP 0008-2:2008 Evidential weight and legal admissibility of information transferred electronically. Code of practice for the implementation of BS 10008
-   BIP 0008-3:2008 Evidential weight and legal admissibility of linking electronic identity to documents. Code of practice for the implementation of BS 10008

|
|20|CESG Good Practice Guide 45 - Identity Proofing and Verification of an Individual v2.3 – July 2014|
|21|CESG Good Practice Guide 46 – Organisational Identity v1.0 – Oct 2013|
|22|HMG IA Standard No. 5 – Secure Sanitisation – v4.0 – April 2011|
|23|ITU-T Recommendation X.509 – Public-key and Attribute certificate frameworks \[10/2012\) [http://www.itu.int/ITU-T/recommendations/rec.aspx?rec=11735](http://www.itu.int/ITU-T/recommendations/rec.aspx?rec=11735)|
|24|[RFC 2986 - Certification Request Syntax Specification – November 2000](http://datatracker.ietf.org/doc/rfc2986/)|

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

