---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](../..)

[spf]: https://www.gov.uk/government/publications/security-policy-framework

# IT Security Technical and Service Provider Users Guide

## Introduction

This guide provides more information on the actions expected of Technical and Service Provider users when using MoJ equipment and infrastructure. This guide is a sub-page to the [IT Security Policy](../it-security-policy/).

## Who is this for?

This guide is aimed at:

1. Technical users: these are in-house MoJ Digital and Technology staff who are responsible for implementing controls throughout technical design, development, system integration and operation. This includes DevOps, Software Developers, Technical Architects and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI and Knowledge (EPICK) Team.
2. Service Providers: defined as any other MoJ business group, agency, contractor, IT supplier and partner who in any way designs, develops or supplies services (including processing, transmitting and storing data) for, or on behalf of the MoJ.

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

### IT Security

For the MoJ [Information Assurance Framework Process](https://docs.google.com/document/d/1ni5bn9vXUj4JFKcoiEO8x31TFCE3AVWN-HxZcVzfNnc/edit?ts=5f10064a) to be effective, it must extend to organisations working on behalf of the MoJ or handling MoJ assets, such as contractors, offshore or nearshore managed service providers and suppliers of IT systems.

- Supplier service delivery must be regularly monitored, reviewed and audited.
- When the MoJ buys IT goods, services, systems or equipment, IT security implications must be considered.
- All MoJ IT suppliers who handle and store information on behalf of the MoJ must be assessed annually against the HMG [Security Policy Framework][spf] and the MoJ's IT Security Policy (this document).  Additional self-assessment requirements may be stipulated in the contract between the IT supplier and the MoJ. The MoJ's IT suppliers are responsible for carrying out these self-assessments and for submitting those assessments to the MoJ.  The MoJ is responsible for approving the assessments submitted by the supplier.
- Appropriate measures must be put in place for any supplier not meeting compliance requirements and the relevant MoJ teams must be notified and consulted.
- All MoJ suppliers and contractors must adhere to the GDPR and the Data Protection Act 2018.

Further advice can be found in the Information Classification, Handling and Security Guide.

### Physical and personnel Security

The MoJ shall include appropriate clauses in a contract with any supplier which will define the classified matter that is furnished, or which is to be developed, under said contract.  This will include any relevant personnel security controls such as security clearance.  Not all contracts will require such clauses but where they are required and failing the inclusion of this information in the contract, a separate Security Aspects Letter (SAL) must be issued to the contractor along with the contract document.

## Privileged users

The MoJ's [Privileged User Guide](../privileged-user-guide/) sets out the key responsibilities for administrator roles within the MoJ in order to protect systems, assets and applications from unauthorised access, use, modification or damage.

The guide sets out the security controls and processes required for the secure handling of MoJ assets and data stored and processed within them, such as the management of administrator accounts and the secure configuration and change management.

## Risk management

### Technical risk assessment and information assurance

The MoJ risk assessment and information assurance is defined in the [Information Assurance Framework Process](https://docs.google.com/document/d/1ni5bn9vXUj4JFKcoiEO8x31TFCE3AVWN-HxZcVzfNnc/edit?ts=5f10064a), which requires that all IT systems that manage or are connected to government information must be assessed to identify technical risks.

### Audit

A security audit is a systematic evaluation of the MoJ's IT security management system which is performed to maintain effective security policies and practices. These checks are subject to self or peer audit by operational line management, contract managers or MoJ HQ managers, as judged to be appropriate by the managers with responsibility for delivery.  For instance, checks on Information Asset Registers and Information Risk Registers should be carried out quarterly but other information assurance checks may be carried out less frequently or triggered by events such as contract renewals.  

Third party audits will be carried out by the [Government Internal Audit Agency](https://www.gov.uk/government/organisations/government-internal-audit-agency) (GIAA) to provide an external evaluation of policies and practices, for more information see contact information below.

When conducting an audit:

- documentary evidence must be made available to auditors upon request
- details provided should include the implementation of any technical security control in an IT system documentary evidence of changes must be reviewed
- the evaluation should cover all types of changes (including configuration changes) to IT systems and the IT security implications of those changes (this includes the case where no significant IT security impacts are identified)
- evidence of operating effectiveness for technical controls must be provided and the desired risk mitigation (as documented in the [Information Assurance Framework Process](https://docs.google.com/document/d/1ni5bn9vXUj4JFKcoiEO8x31TFCE3AVWN-HxZcVzfNnc/edit?ts=5f10064a))
- activities involving verification of operational systems should be carefully planned and agreed to minimise disruptions to business processes.˜

## Contact details

- Contact the Cyber Assistance Team for further advice - [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk)
- Contact the Technology Service Desk to report a suspected IT incident:<br/>Telephone: 0800 917 5148.
- Contact the MoJ Security Team to report other security incidents: [Security@justice.gov.uk](mailto:Security@justice.gov.uk)
- Contact the Operational Security Team for further advice: [Operationalsecurityteam@justice.gov.uk](mailto:operationalsecurityteam@justice.gov.uk)
- Contact the Government Internal Audit Agency for more information:
[correspondence@giaa.gov.uk](mailto:correspondence@giaa.gov.uk)
