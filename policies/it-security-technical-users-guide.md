---
Review: 2021-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](../..)

[spf]: https://www.gov.uk/government/publications/security-policy-framework

# IT Security Technical Users Policy

## Introduction

This policy provides more information on the actions expected of Technical and Service Provider users when using MoJ equipment and infrastructure. It is a sub-page to the [IT Security Policy](https://github.com/ministryofjustice/security-guidance/blob/Local/policies/it-security-policy.md).

## Who is this for?

This policy is aimed at:

1. **Technical users**: these are in-house MoJ Digital and Technology staff who are responsible for implementing controls throughout technical design, development, system integration and operation. This includes DevOps, Software Developers, Technical Architects and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI and Knowledge (EPICK) Team.
2. **Service Providers**: defined as any other MoJ business group, agency, contractor, IT supplier and partner who in any way designs, develops or supplies services (including processing, transmitting and storing data) for, or on behalf of the MoJ.

## Vulnerability scanning and patch management

The MoJ [Vulnerability Scanning and Patch Management Guide](https://ministryofjustice.github.io/security-guidance/vulnerability-scanning-and-patch-management-guide/#vulnerability-scanning-and-patch-management-guide) outlines the requirements for maintaining up to date MoJ systems and equipment to protect them from security vulnerabilities.

The guide includes patching schedules for the different MoJ systems and equipment according to their risk levels and sets out the vulnerability ratings used to understand the criticality of a system security vulnerability. The guide addresses the following areas:

- patching schedules and technical guides
- scanning requirements for different MoJ systems.

## Technical controls

The MoJ [Technical Controls Guide](https://ministryofjustice.github.io/security-guidance/technical-security-controls-guide/#technical-security-controls-guide) ensures protection from unauthorised access or misuse of the MoJ IT systems, applications and data stored within them.

The policy outlines the control design requirements that are needed to secure the MoJ network and IT assets in accordance with the three layers of defence. The policy addresses following areas:

- enforcing access controls in support of the [Access Control Guide](https://ministryofjustice.github.io/security-guidance/access-control-guide/#access-control-guide)
- building adequate security for the MoJ network and network boundaries
- creating secure software development and software configuration processes and designs
- monitoring the MoJ network against malicious code and anomalous behaviour.

## Cryptography

Cryptography is a method of securing information and communication channels to allow only authorised recipients and personnel to view the information. The MoJ's IT systems must use cryptographic technologies to provide secure connections to third party systems or protect information at rest on user devices (e.g. laptops and mobiles).

However, where staff have procured key material and/or hardware through the  United Kingdom Key Production Authority (UKKPA) or any other cryptographic items where National Cyber Security Centre (NCSC) dictate that national cryptographic policy applies, the NCSC dictate the policy and the HMG IA Standard No. 4, Protective Security Controls for the Handling and Management of Cryptographic Items (IS4) applies.

> Note: IS4 can be accessed by joining CiSP and joining the UKKPA-Crpy Key Policy and Incident Management Group.

The MoJ's Staff who use cryptography must ensure they have the appropriate level of security clearance. This requires secret (SC) level clearance for managing cryptography.

The Chief Information Security Officer (CISO) is accountable to the Senior Information Risk Owner (SIRO) and Senior Security Advisor (SSA) for ensuring the MoJ's compliance with the minimum HMG - Comsec and cryptography requirements and developing, implementing and maintaining organisational communications.

## Software development

The MoJ ensures that all in house development, including development performed by third parties, is performed according to industry best practices and standards, as laid out in the Software Development Lifecycle Guide (SDLC).

All MoJ developers must ensure they are aware of the importance of security when developing software and applications for MoJ use. The SDLC addresses the required methodology to be used in code development and the security concerns that need to be accounted for during the development lifecycle.

## Security incident management

The MoJ's [IT Incident Management Policy](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/it-incident-management-policy/) covers the end-to-end incident lifecycle and provides the guidance for the MoJ to respond effectively in the event of an IT Security Incident which includes security incidents.  Examples of topics covered are preparation for incidents, escalation and incident response and recovery (containment, resolution and recovery).

The MoJ [IT Incident Management Guide](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/incident-management-plan-and-process-guide/) provides additional detail to the policy but also further guidance around Incident Response Team assembly and communication channels.

## Suppliers and procurement

### IT Security

For the MoJ [Information Assurance Framework Process](https://docs.google.com/document/d/1ni5bn9vXUj4JFKcoiEO8x31TFCE3AVWN-HxZcVzfNnc/edit?ts=5f10064a) to be effective, it must extend to organisations working on behalf of the MoJ or handling MoJ assets, such as contractors, offshore or nearshore managed service providers and suppliers of IT systems.  From this document, the Contract owner is responsible for ensuring that:

- the supplier service delivery must be regularly monitored, reviewed and audited.
- when the MoJ buys IT goods, services, systems or equipment, IT security implications must be considered.
- all MoJ IT suppliers who handle and store information on behalf of the MoJ must be assessed annually against the HMG [Security Policy Framework][spf] and the MoJ's IT Security Policy.  Additional self-assessment requirements may be stipulated in the contract between the IT supplier and the MoJ. The MoJ's IT suppliers are responsible for carrying out these self-assessments and for submitting those assessments to the MoJ.  The MoJ is responsible for approving the assessments submitted by the supplier.
- the appropriate measures must be put in place for any supplier not meeting compliance requirements and the relevant MoJ teams must be notified and consulted.
- all MoJ suppliers and contractors adhere to the GDPR and the Data Protection Act 2018.

Further advice can be found in the Information Classification, Handling and Security Guide.

### Physical and personnel Security

The Contract owner shall include appropriate clauses in a contract with any supplier which will define the classified matter that is furnished, or which is to be developed, under said contract.  This will include any relevant personnel security controls such as security clearance.  Not all contracts will require such clauses but where they are required and failing the inclusion of this information in the contract, a separate Security Aspects Letter (SAL) is issued to the contractor along with the contract document.

## Privileged users

The MoJ's [Privileged User Guide](https://github.com/ministryofjustice/security-guidance/blob/Local/policies/privileged-user-guide.md) sets out the key responsibilities for administrator roles within the MoJ in order to protect systems, assets and applications from unauthorised access, use, modification or damage.

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

- Contact the Technology Service Desk to report a suspected IT incident:<br/>Telephone: 0800 917 5148.
- Contact the MoJ Security Team to report other security incidents: [Security@justice.gov.uk](mailto:Security@justice.gov.uk)
- Contact the Government Internal Audit Agency for more information: [correspondence@giaa.gov.uk](mailto:correspondence@giaa.gov.uk)
