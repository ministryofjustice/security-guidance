---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](../..)

[spf]: https://www.gov.uk/government/publications/security-policy-framework

# IT Security Policy

## Introduction

This policy gives an overview of information security principles and responsibilities within the MoJ and provides a summary of the MoJ's related security policies and guides.

## Who is this for?

This guide is aimed at three audiences:

1. The in-house MoJ Digital and Technology staff who are responsible for implementing controls throughout technical design, development, system integration and operation. This includes DevOps, Software Developers, Technical Architects and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI and Knowledge (EPICK) Team.
2. Any other MoJ business group, agency, contractor, IT supplier and partner who in any way designs, develops or supplies services (including processing, transmitting and storing data) for, or on behalf of the MoJ.
3. General users working for the MoJ.

## Assets

This IT security policy applies to all premises, physical equipment, software and data owned or managed by the MoJ. This includes IT systems, whether developed by the MoJ or managed by IT service providers. It covers the use of IT equipment and the information processed on those IT systems, irrespective of location and provides direction and support to preserve the confidentiality, integrity and availability of MoJ resources.

## Approach

The MoJ is committed to protecting its staff, assets and data. These include personal data of those who interact with the Justice System, our staff and suppliers; other data we've been entrusted with, as well as ensuring the continued operation of our systems and processes. The MoJ will ensure information security controls are designed and implemented to protect MoJ data, IT Assets and reputation based around the following requirements:

- **Confidentiality**: knowing and ensuring information can only be accessed by those authorised to do so
- **Integrity**: knowing and ensuring the accuracy and completeness of data and that it has not been deliberately or inadvertently modified from a previous version
- **Availability**: knowing and ensuring that IT systems and data can always be accessed when required.

## Information security classification

The MoJ maintains an Information Security Policy, which aligns with the HM Government Security Classifications, to provide a framework for safeguarding data from risks including, but not limited to, unauthorised destruction, modification, disclosure, access, use and removal.

All MoJ Staff are responsible for ensuring data is:
- classified correctly as detailed in the [Information Classification, Handling and Security Guide](../information-classification-handling-and-security-guide/)
- distributed only in accordance with the statements of this policy and related guides
- protected by the appropriate security controls to ensure its confidentiality, integrity and availability.

Access to said classified information shall be controlled in accordance with the requirements set out within the MoJ [Access Control Guide](../access-control-guide/).

## Physical and personnel security

The Physical Security Policy defines how physical access to assets must be controlled within the MoJ to prevent unauthorised access, use, modification, loss or damage.

- All MoJ IT systems and services must be assessed against environmental risks (e.g. flood or fire) to maintain the asset's confidentiality, integrity and availability.
- The MoJ's IT Teams are not directly responsible for the physical security and environment of the MoJ sites.
- Physical security controls and the environment in which the MoJ IT systems operate form part of a system's overall risk landscape, and, therefore, all MoJ users must ensure they adhere to the security controls and requirements set out in this policy.

The MoJ shall include appropriate clauses in a contract with any supplier which will define the classified matter that is furnished, or which is to be developed, under said contract.  This will include any relevant personnel security controls such as security clearance.  Not all contracts will require such clauses but where they are required and failing the inclusion of this information in the contract, a separate Security Aspects Letter (SAL) must be issued to the contractor along with the contract document.

- Unless otherwise formally agreed by the MoJ, all MoJ staff, including agency staff and contractors who have access to MOJ data, require [BPSS](https://www.gov.uk/government/publications/government-baseline-personnel-security-standard).
- [National Security Vetting](https://www.gov.uk/guidance/security-vetting-and-clearance#applicant) should only be applied for where it is necessary, proportionate and adds real value.
- The MoJ does not have a standing requirement for system administrators or application developers to maintain Security Check (SC).

Further information is available from [MoJ Group Security](mailto:mojgroupsecurity@justice.gov.uk) and [CPNI Guidance](https://www.cpni.gov.uk/physical-security).

## Identity and access control

The MoJ [Access Control Guide](../access-control-guide/) ensures that information and IT assets can be accessed by only authorised personnel and that each individual is accountable for their actions.

The guide outlines the controls and processes designed to limit access based on a 'need to know' basis and according to defined roles and responsibilities.

The MoJ [Access Control Guide](../access-control-guide/) addresses access control principles such as identification, authentication, authorisation and accounting.  

## Password management

The MoJ [Password Management Guide](../password-management-guide/) sets out the requirements for strong password implementation and management to help prevent unauthorised access to MoJ systems.  Examples include
password creation and authentication and password storage and management.

## Email security

The MoJ [Email Security Guide](../email-security-guide/) specifies the controls and processes required to protect the MoJ's email systems from unauthorised access or misuse, that may compromise the confidentiality, integrity and/or availability of the information stored and shared within them.

The guide outlines the various security levels required to transfer information from the MoJ's email servers to organisations outside the MoJ and other government departments. It covers topics such as the threats to email security (phishing) and secure email transfer.

## Remote working and portable devices

The MoJ has in place a [Remote Working Standard](../remote-working/) which sets out the requirements for safely accessing and using the MoJ's systems and applications when working remotely, for example, from home, another government office or whilst travelling.

Mobile computing is the use of portable equipment such as mobile phone, laptop or tablet and supports remote working. Mobile computing equipment provided by the MoJ must be used in line with the [Acceptable Use Policy](../acceptable-use-policy/).

Any request to take MoJ IT equipment abroad must follow the guidance provided in the [Acceptable Use Policy](../acceptable-use-policy/) and the Travelling Abroad Policy.

## Malware protection

The MoJ [Malware Protection Guide](../malware-protection-guide-introduction/) specifies the controls and processes required to protect all systems against malware. Malware may enter the MoJ by employee email through the internet, mobile computers and removable media devices.

The MoJ [Malware Protection Guide](../malware-protection-guide-introduction/) addresses the following relevant domains:

- implementation controls to stop malware entering MoJ devices and systems
- preventing malicious code from executing on MoJ devices and systems
- mitigating the impact of malware when entering MoJ devices and systems.

## Vulnerability scanning and patch management

The MoJ [Vulnerability Scanning and Patch Management Guide](../vulnerability-scanning-and-patch-management-guide/) outlines the requirements for maintaining up to date MoJ systems and equipment to protect them from security vulnerabilities.

The guide includes patching schedules for the different MoJ systems and equipment according to their risk levels and sets out the vulnerability ratings used to understand the criticality of a system security vulnerability. The guide addresses the following areas:

- patching schedules and technical guides
- scanning requirements for different MoJ systems.

## Technical controls

The MoJ [Technical Controls Guide](../technical-security-controls-guide/) ensures protection from unauthorised access or misuse of the MoJ IT systems, applications and data stored within them.

The guide outlines the control design requirements that are needed to secure the MoJ network and IT assets in accordance with the three layers of defence. The guide addresses following areas:

- enforcing access controls in support of the [Access Control Guide](../access-control-guide/)
- building adequate security for the MoJ network and network boundaries
- creating secure software development and software configuration processes and designs
- monitoring the MoJ network against malicious code and anomalous behaviour.

## Cryptography

Cryptography is a method of securing information and communication channels to allow only authorised recipients and personnel to view the information. The MoJ's IT systems may use cryptographic technologies to provide secure connections to third party systems or protect information at rest on user devices (e.g. laptops and mobiles). Any staff member responsible for the use of cryptographic controls on an IT system must ensure that **all IT systems which require cryptographic controls must align with the HMG IA Standard No. 4 (IS4)**.

The MoJ's Staff who use cryptography must ensure they have the appropriate level of security clearance and that they are adhering to the following requirements:

- use of HMG cryptographic material or products must align with the HMG IA Standard No. 4 (IS4), and
- the Chief Information Security Officer (CISO) is accountable to the SIRO and SSA for ensuring the MoJ's compliance with the minimum HMG  - Comsec and cryptography requirements and developing, implementing and maintaining organisational communications.


## Software development

The MoJ ensures that all in house development, including development performed by third parties, is performed according to industry best practices and standards, as laid out in the Software Development Lifecycle Guide.

All MoJ developers must ensure they are aware of the importance of security when developing software and applications for MoJ use. The Software Development Lifecycle Policy addresses the required methodology to be used in code development and the security concerns that need to be accounted for during the development lifecycle.

## Security incident management

The MoJ's [IT Incident Management Policy](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/it-incident-management-policy/) covers the end-to-end incident lifecycle and provides the guidance for the MoJ to respond effectively in the event of an IT Security Incident which includes security incidents.  Examples of topics covered are preparation for incidents, escalation and incident response and recovery (containment, resolution and recovery).

The MoJ [IT Incident Management Guide](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/incident-management-plan-and-process-guide/) provides additional detail to the policy but also further guidance around Incident Response Team assembly and communication channels.

## Suppliers and procurement

For the MoJ [Information Assurance Framework Process](https://docs.google.com/document/d/1ni5bn9vXUj4JFKcoiEO8x31TFCE3AVWN-HxZcVzfNnc/edit?ts=5f10064a) to be effective, it must extend to organisations working on behalf of the MoJ or handling MoJ assets, such as contractors, offshore or nearshore managed service providers and suppliers of IT systems.

- Supplier service delivery must be regularly monitored, reviewed and audited.
- When the MoJ buys IT goods, services, systems or equipment, IT security implications must be considered.
- All MoJ IT suppliers who handle and store information on behalf of the MoJ must be assessed annually against the HMG [Security Policy Framework][spf] and the MoJ's IT Security Policy (this document).  Additional self-assessment requirements may be stipulated in the contract between the IT supplier and the MoJ. The MoJ's IT suppliers are responsible for carrying out these self-assessments and for submitting those assessments to the MoJ.  The MoJ is responsible for approving the assessments submitted by the supplier.
- Appropriate measures must be put in place for any supplier not meeting compliance requirements and the relevant MoJ teams must be notified and consulted.
- All MoJ suppliers and contractors must adhere to the GDPR and the Data Protection Act 2018.

Further advice can be found in the Information Classification, Handling and Security Guide.


## Privileged users

The MoJ's [Privileged User Guide](../privileged-user-guide/) sets out the key responsibilities for administrator roles within the MoJ in order to protect systems, assets and applications from unauthorised access, use, modification or damage.

The guide sets out the security controls and processes required for the secure handling of MoJ assets and data stored and processed within them, such as the management of administrator accounts and the secure configuration and change management.

## Roles and responsibilities

All MoJ users are responsible for ensuring the confidentiality, integrity and availability of data within the MoJ. This includes all MoJ data and assets, and these responsibilities extend to all subpages and guidance referenced in this policy.

All MoJ users are required to comply with the roles and responsibilities outlined in the MoJ [Information Assurance Framework Process](https://docs.google.com/document/d/1ni5bn9vXUj4JFKcoiEO8x31TFCE3AVWN-HxZcVzfNnc/edit?ts=5f10064a).

Specific roles and responsibilities are described within each sub-page. All MoJ users must comply with these roles and responsibilities and understand these as being a part of their ultimate responsibility for information security within the MoJ.

For the purpose of this Information Security Policy, the following roles are described, as they will be referred to as holding specific responsibilities in the implementation and monitoring of different provisions of the policy.

| Role | Responsibility | Which includes... |
|--- |---|---|
| **Senior Information Risk Owners (SIROs)** | The MoJ SIRO is responsible for the overall MoJ information risk policy and guidance, and ensures it continues to provide appropriate risk appetite and a suitable risk framework | Implementing and managing information risk management in their respective business groups|
| | | Regularly reviewing the application of policy and guidance to ensure it remains appropriate to their business objectives and risk environment |
| | | Authorising any exceptions and deviations from the IT Security Policy with consideration of the impact any changes might have to other users. |
| **Delegated Agency SIROs** |  | |
| **Information Asset Owners (IAO)** | IAOs, also known as IA Leads, must be satisfied that all required technical, personnel, physical and procedural security controls are in place and followed. IAOs are responsible for ensuring the management and security of their information asset over the whole asset lifecycle | Logging and monitoring |
| | | Reviewing access permissions |
| | | Understanding and addressing risks associated to their information assets |
| | | Ensuring secure disposal of information no longer required|
| **System Owners** | System Owners are responsible for managing access control rules for their particular system. | Verifying access rights in order to assist a scheduled review audit of User accounts and permissions.|
| **Contract Owners** | | |

## Risk management

### Technical risk assessment and information assurance

The MoJ risk assessment and information assurance is defined in the [Information Assurance Framework Process](https://docs.google.com/document/d/1ni5bn9vXUj4JFKcoiEO8x31TFCE3AVWN-HxZcVzfNnc/edit?ts=5f10064a), which requires that all IT systems that manage or are connected to government information must be assessed to identify technical risks.

### Audit

A security audit is a systematic evaluation of the MoJ's IT security management system which is performed to maintain effective security policies and practices. These checks may be subject to self or peer audit by operational line management, contract managers or HQ managers, as judged to be appropriate by the managers with responsibility for delivery.  For instance, checks on Information Asset Registers and Information Risk Registers should be carried out quarterly but other information assurance checks may be carried out less frequently  or triggered by events such as contract renewals.

When conducting an audit:

- documentary evidence must be made available to auditors upon request
- details provided should include the implementation of any technical security control in an IT system documentary evidence of changes must be reviewed
- the evaluation should cover all types of changes (including configuration changes) to IT systems and the IT security implications of those changes (this includes the case where no significant IT security impacts are identified)
- evidence of operating effectiveness for technical controls must be provided and the desired risk mitigation (as documented in the [Information Assurance Framework Process](https://docs.google.com/document/d/1ni5bn9vXUj4JFKcoiEO8x31TFCE3AVWN-HxZcVzfNnc/edit?ts=5f10064a))
- activities involving verification of operational systems should be carefully planned and agreed to minimise disruptions to business processes.

## Contact details

- Contact the Cyber Assistance Team for further advice - [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk)
- Contact the Technology Service Desk to report a suspected IT incident:<br/>Telephone: 0800 917 5148.
- Contact the MoJ Security Team to report other security incidents: [Security@justice.gov.uk](mailto:Security@justice.gov.uk)
- Contact the Operational Security Team for further advice: [Operationalsecurityteam@justice.gov.uk](mailto:operationalsecurityteam@justice.gov.uk)
