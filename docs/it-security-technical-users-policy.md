# IT Security Technical Users Policy

**Parent topic:** [IT Security Policy \(Overview\)](it-security-policy-overview.md)

## Introduction

This policy provides more information on the actions expected of Technical and Service Provider users when using Ministry of Justice \(MoJ\) equipment and infrastructure. It is a sub-page to the [IT Security Policy Overview](it-security-policy-overview.md).

## Audience

This policy is aimed at:

<a name="technical-users"></a>

-   **Technical users**

    These are in-house MoJ Digital and Technology staff who are responsible for implementing controls throughout technical design, development, system integration, and operation. This includes DevOps, Software Developers, Technical Architects, and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI and Knowledge \(EPICK\) Team.

<a name="service-providers"></a>

-   **Service Providers**

    Defined as any other MoJ business group, agency, contractor, IT supplier and partner who in any way designs, develops or supplies services \(including processing, transmitting and storing data\) for, or on behalf of, the MoJ.


## Vulnerability scanning and patch management

The MoJ [Vulnerability Scanning and Patch Management Guide](vulnerability-scanning-and-patch-management-guide.md) outlines the requirements for maintaining up to date MoJ systems and equipment to protect them from security vulnerabilities.

The guide includes patching schedules for the different MoJ systems and equipment according to their risk levels. It sets out the vulnerability ratings used to understand the criticality of a system security vulnerability. The guide addresses the following areas:

-   Patching schedules and technical guides.
-   Scanning requirements for different MoJ systems.

## Technical controls

The MoJ [Technical Security Controls Guide](technical-security-controls-guide.md) ensures protection from unauthorised access or misuse of the MoJ IT systems, applications, and data stored within them.

The policy outlines the control design requirements that are needed to secure the MoJ network and IT assets in accordance with the three layers of defence. The policy addresses the following areas:

-   Enforcing access controls in support of the [Access Control Guide](access-control-guide.md).
-   Building adequate security for the MoJ network and network boundaries.
-   Creating secure software development and software configuration processes and designs.
-   Monitoring the MoJ network against malicious code and anomalous behaviour.

## Cryptography

Cryptography is a method of securing information and communication channels to allow only authorised recipients and personnel to view the information. The MoJ's IT systems **shall** use cryptographic technologies to provide secure connections to third party systems or to protect information "at rest" on user devices, including laptops and mobile devices.

However, where staff have procured key material or hardware through the United Kingdom Key Production Authority \(UKKPA\) or any other cryptographic items where National Cyber Security Centre \(NCSC\) dictate that national cryptographic policy applies, the NCSC dictate the policy. In this case, the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security) \(previously HMG IA Standard No. 4, Protective Security Controls for the Handling and Management of Cryptographic Items, IS4\) applies.

**Note:** IS4 can be accessed by joining the [Cyber Security Information Sharing Partnership \(CISP\)](https://www.ncsc.gov.uk/section/keep-up-to-date/cisp) and joining the UKKPA-Crpy Key Policy and Incident Management Group.

The MoJ's Staff who use cryptography **shall** ensure they have the appropriate level of security clearance. This requires secret \(SC\) level clearance for managing cryptography.

The Chief Information Security Officer \(CISO\) is accountable to the Senior Information Risk Owner \(SIRO\) and Senior Security Advisor \(SSA\) for ensuring the MoJ's compliance with the minimum cryptography requirements.

## Software development

The MoJ ensures that all in house development, including development performed by third parties, is performed according to industry best practices and standards, as laid out in the Software Development Lifecycle Guide \(SDLC\).

All MoJ developers **shall** ensure they are aware of the importance of security when developing software and applications for MoJ use. The SDLC addresses the required methodology to be used in code development, and the security concerns that **shall** be accounted for during the development lifecycle.

## Security incident management

The MoJ's [Security Incident Management](it-security-incident-management-policy.md) covers the end-to-end incident lifecycle, and provides the guidance for the MoJ to respond effectively in the event of an IT Security Incident, which includes security incidents. Examples of topics covered are preparation for incidents, escalation and incident response, and recovery activities, including containment, resolution, and recovery.

The MoJ [IT Security Incident Response Plan and Process Guide](it-security-incident-response-plan-and-process-guide.md) provides additional detail to the policy, but also further guidance around Incident Response Team assembly and communication channels.

## Suppliers and procurement

### IT Security

For the MoJ Information Assurance Framework Process to be effective, it must extend to organisations working on behalf of the MoJ or handling MoJ assets, such as contractors, offshore or nearshore managed service providers, and suppliers of IT systems. Within the Framework, the Contract owner is responsible for ensuring that:

-   The supplier service delivery **shall** be regularly monitored, reviewed, and audited.
-   When the MoJ buys IT goods, services, systems, or equipment, IT security implications **shall** be considered.
-   All MoJ IT suppliers who handle and store information on behalf of the MoJ **shall** be assessed annually against the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security) \(previously HMG [Security Policy Framework](https://www.gov.uk/government/publications/security-policy-framework)\) and the MoJ's [IT Security Policy](it-security-policy-overview.md). Additional self-assessment requirements may be stipulated in the contract between the IT supplier and the MoJ. The MoJ's IT suppliers are responsible for carrying out these self-assessments, and for submitting those assessments to the MoJ. The MoJ is responsible for approving the assessments submitted by the supplier.
-   The appropriate measures **shall** be put in place for any supplier not meeting compliance requirements, and the relevant MoJ teams **shall** be notified and consulted.
-   All MoJ suppliers and contractors **shall** adhere to the GDPR and the Data Protection Act 2018.

Further advice can be found in the [Information Classification, Handling and Security Guide](information-classification-handling-and-security-guide.md).

### Physical and personnel Security

The Contract owner **shall** include appropriate clauses in a contract with any supplier which will define the classified matter that is furnished, or which is to be developed, under said contract. This will include any relevant personnel security controls such as security clearance. Not all contracts will require such clauses, but where they are required, and failing the inclusion of this information in the contract, a separate [Security Aspects Letter \(SAL\)](security-aspect-letters.md) is issued to the contractor along with the contract document.

## Privileged users

The MoJ's Privileged User Guide sets out the key responsibilities for administrator roles within the MoJ in order to protect systems, assets and applications from unauthorised access, use, modification, or damage.

The guide sets out the security controls and processes required for the secure handling of MoJ assets and data stored and processed within them, such as the management of administrator accounts and secure configuration and change management.

## Risk management

### Technical risk assessment and information assurance

The MoJ risk assessment and information assurance is defined in the Information Assurance Framework Process, which requires that all IT systems that manage or are connected to government information **shall** be assessed to identify technical risks.

### Audit

A security audit is a systematic evaluation of the MoJ's IT security management system. It is performed to maintain effective security policies and practices. These checks are subject to self or peer audit by operational line management, contract managers or MoJ HQ managers, as judged to be appropriate by the managers with responsibility for delivery. For instance, checks on Information Asset Registers and Information Risk Registers **should** be carried out quarterly, but other information assurance checks might be carried out less frequently, or triggered by events such as contract renewals.

Third party audits will be carried out by the [Government Internal Audit Agency](https://www.gov.uk/government/organisations/government-internal-audit-agency) \(GIAA\) to provide an external evaluation of policies and practices. For more information, contact the Government Internal Audit Agency: Government Internal Audit Agency via [Security team](mailto:security@justice.gov.uk)

When conducting an audit:

-   Documentary evidence **shall** be made available to auditors upon request.
-   Details provided **should** include the implementation of any technical security control in an IT system. Documentary evidence of changes **shall** be reviewed.
-   The evaluation **should** cover all types of changes, including configuration changes, to IT systems, and the IT security implications of those changes. This includes the case where no significant IT security impacts are identified.
-   Evidence of operating effectiveness for technical controls **shall** be provided, and the desired risk mitigation as documented in the Information Assurance Framework Process.
-   Activities involving verification of operational systems **should** be carefully planned and agreed to minimise disruptions to business processes.

## Incidents

**Note:** If you work for an agency or ALB, refer to your local incident reporting guidance.

**Security Team**

-   Email: [security@justice.gov.uk](mailto:security@justice.gov.uk)
-   Slack: `#security`

## Contact and Feedback

For any further questions or advice relating to security, or for any feedback or suggestions for improvement, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).

