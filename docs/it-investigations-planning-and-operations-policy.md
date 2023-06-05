# IT Investigations - Planning and Operations Policy

## How to use this policy

This policy is for technical users. Technical users include:

-   Technical architects
-   DevOps specialists
-   IT service managers
-   Software developers

This policy is part of a set of Ministry of Justice \(MoJ\) policies and supporting guides that cover various aspects of incident and disaster management and response.

The policies are:

-   [IT Incident Management Policy](it-incident-management-policy.md)
-   [IT Disaster Recovery Policy](it-disaster-recovery-policy.md)
-   IT Investigations - Planning and Operations Policy

The supporting guides are:

-   [IT Security Incident Response Plan and Process Guide](it-security-incident-response-plan-and-process-guide.md)
-   [IT Disaster Recovery Plan and Process Guide](it-disaster-recovery-plan-and-process-guide.md)

### Policy Statements

This policy refers to Policy Statements, POL.POP.001 to POL.POP.015.

**POL.POP.XXX** indicates the specific policy statement to be adhered to.

### IT Forensics

IT forensics is the collection, storage, analysis and preparation of digital evidence that might be required in legal or disciplinary proceedings,

Data used in a forensic investigation **shall** be collected, preserved and analysed using systemic, standardised and legally compliant methods.

This will ensure that data gathered is admissible as evidence in a legal case, dispute or disciplinary hearing relating to an IT security incident.

There are two types of forensic investigation:

-   proactive forensic monitoring - as part of an indentified MoJ security control
-   reactive investigation - where a suspicious incident has been identified or reported

A forensics investigation **should** be carried out:

-   if an area needs proactive monitoring to enable forensic investigation
-   if a business function makes a request via incident management escalation channels, to gather forensic evidence.
-   if an investigation is requested as part of the IT security incident management process
-   if requested as part of a leak investigation.

<a name="__pol.pop.001__"></a>

-   **__POL.POP.001__**

    Each MoJ IT system or IT domain **shall** be covered by a Forensic Readiness Plan.

<a name="__pol.pop.002__"></a>

-   **__POL.POP.002__**

    Each Forensic Readiness Plan **shall** include:

    -   an assessment of the risk management benefits
    -   authorisation from the IT Security Team and Senior Information Risk Officer \(SIRO\)
    -   a corresponding IT security incident management plan
    Risk management benefits include risk assessments and cost-benefit-analysis, which will determine if an investigation is viable from a risk and cost perspective.

<a name="__pol.pop.003__"></a>

-   **__POL.POP.003__**

    Forensic investigations in support of leak investigations **shall** be requested by the individual responsible for the leak investigation.


### Integrity of Digital Evidence

<a name="__pol.pop.004__"></a>

-   **__POL.POP.004__**

    Each forensic investigation **shall** be guided by the principles set out by the [ACPO guidelines](https://library.college.police.uk/docs/acpo/digital-evidence-2012.pdf) issued by the National Police Chiefs' Council \(NPCC\).


The integrity of data, which **might** subsequently relied upon in court, **shall** be maintained throughout the forensic investigation process.

Any person accessing data as part of an investigation **shall** be competent to do so and able to justify the relevance and implications of their actions.

Each investigation **shall** be documented clearly and leave an audit trail that will enable a third-party to examine each process and replicate the findings,

The person leading the investigation is responsible for ensuring that all methods used are carried out in accordance with the law.

Investigations **shall** be conducted in line with MoJ policies.

### Evidence Collection and Storage

Security teams **should** be able to monitor systems to detect and respond to potential security incidents. If an incident needs to be investigated further, forensic tools **may** be used to assess and gather evidence.

The Forensic Investigation Owner \(FIO\) is responsible for the collection and management of digital evidence.

An external organisation **may** conduct the investigation on behalf of the MoJ.

Each item of evidence collected **shall** be managed according to the relevant Forensic Readiness Plan.

<a name="__pol.pop.005__"></a>

-   **__POL.POP.005__**

    Each Forensic Readiness Plan **shall** include a process for the collection and storage of digital evidence, to include provision for where this task is conducted by an external organisation.

<a name="__pol.pop.006__"></a>

-   **__POL.POP.006__**

    All users of an MoJ IT system **shall** be made aware that their access is monitored, and that IT forensic techniques **may** be used to capture evidence as part of an investigation into an IT security incident.

<a name="__pol.pop.007__"></a>

-   **__POL.POP.007__**

    A Forensic Readiness Plan **shall** contain clearly defined procedures and methods for conducting a forensic investigation. The MoJ **shall** be able to resume business operations following an IT security incident. Any forensic investigation **shall** be conducted in a manner that enables the restoration of MoJ IT services.

<a name="__pol.pop.008__"></a>

-   **__POL.POP.008__**

    A Forensic Readiness Plan **shall** consider business continuity arrangements to ensure that essential functions are able to be restored. Digital evidence **shall** be handled carefully in order for it to remain admissible.

<a name="__pol.pop.009__"></a>

-   **__POL.POP.009__**

    Each forensic investigation **shall** have a clearly documented chain of custody for all digital evidence.

<a name="__pol.pop.010__"></a>

-   **__POL.POP.010__**

    The MoJ Security Team is responsible for the integrity of digital evidence. Each forensic investigation **shall** have a named FIO who is responsible for the investigation and management of digital evidence.

<a name="__pol.pop.011__"></a>

-   **__POL.POP.011__**

    Any investigative action taken on a piece of evidence **shall** be captured and recorded. This record **shall** include details of the action taken and the person responsible for undertaking that action.

<a name="__pol.pop.012__"></a>

-   **__POL.POP.012__**

    Admissibility of evidence in a court of law depends on how the evidence was captured. Before capturing any evidence, advice **shall** be sought from the MoJ legal team and forensic investigation provider.

<a name="__pol.pop.013__"></a>

-   **__POL.POP.013__**

    Each Forensic Readiness Plan **shall** include details of how to securely dispose of evidence when it is no longer required. This **shall** conform with [Secure disposal of IT equipment](secure-disposal-of-it-equipment.md).


### Legal Requirements

Investigations of electronically stored information within the MoJ **shall** conform to the latest legal and regulatory guidelines.

BS 10008:2022 provides information on the collection of electronically stored information as evidence.

<a name="__pol.pop.014__"></a>

-   **__POL.POP.014__**

    During each forensic investigation, methods used to capture digital evidence **shall** be in accordance with [BS 10008:2022](https://www.bsigroup.com/en-GB/bs-10008-electronic-information-management/).


### Reporting and Communication

Each IT Security Incident Management Plan contains a communication plan and an escalation plan that **shall** be followed when responding to an IT Security incident.

The [IT Incident Management Plan and Process Guide](incident-management-plan-and-process-guide.md) gives more information.

For major incidents it might be necessary to consider escalating the forensic investigation process to an external body. This might be:

-   Law Enforcement
-   National Cyber Security Centre \(NCSC\)
-   Cabinet Office
-   MoJ legal advisors
-   Other Government Agencies as required

<a name="__pol.pop.015__"></a>

-   **__POL.POP.015__**

    Each Forensic Readiness Plan **shall** include the reporting structure and escalation path for internal and external teams and the individual responsible for managing the incident. This **shall** be consistent with the corresponding [IT Security Incident Management Plan](incident-management-plan-and-process-guide.md). The forensic investigation process **shall** enable the chain of evidence to be passed to outside agencies, if required.


### Legacy information

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

### Contact details

For any further questions or advice relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).

### Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

