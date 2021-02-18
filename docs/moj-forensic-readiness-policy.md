# Ministry of Justice \(MoJ\) Forensic Readiness Policy

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

## About this document

This document is the MoJ IT Security – Forensic Readiness Policy. It provides the core set of IT security principles, expectations, roles and responsibilities for the capture and preservation of digital evidence.

### How to use this document

Each policy statement outlines a security requirement and where applicable, a reference is provided to further material. A unique identify is associated with each statement for easy reference. The format of each statement is illustrated below:

-   **POL.FRP.XXX**

    Policy statement text.


The policies outlined in this document form the baseline standard. Where exceptions are required, this is captured on a case by case basis in Tier 4, where approval is required from both the business group SIRO and MoJ ITSO.

## Forensics Readiness Policy

### Introduction

The aims of this policy are to:

-   Maximise the effectiveness of any digital incident investigation which may be required, normally as a result of a security incident;

-   Help protect MoJ information assets through the application of best practice in IT Forensics;

-   Minimise the cost and impact on the business of a forensic investigation;

-   Manage the risks associated with forensic investigations, and, the risks inherent in the incident\(s\) that occurred, necessitating the investigation.


IT forensics is the application of techniques to detect and react to types of security incidents that require the collection, storage, analysis and preparation of digital evidence that may be required in legal or disciplinary proceedings.

The use of IT forensics as a course of action is linked to decisions made during an IT security incident. As such, this policy is linked to, and should be read in conjunction with, the [IT Security - IT Incident Management Policy](it-incident-management-policy.md).

This policy outlines the requirements to collect, preserve and analyse data in a systematic, standardised and legally compliant fashion to ensure the admissibility of evidence in a legal case, dispute or disciplinary hearing relating to an incident.

-   **POL.FRP.001**

    Each IT system or IT domain **must have** \(or be explicitly covered by\) a Forensic Readiness Plan which implements this policy.


**Note:** In general, where an IT system \(or IT domain\) has an IT Security Incident Management Plan, there should be a corresponding Forensic Readiness Plan.

A template Forensic Readiness Plan is [available](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/forensic-readiness-guide/) with further guidance provided in [IT Security - Forensics Readiness Guide](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/forensic-readiness-guide/).

### Scope

This Policy applies to all users of MoJ IT systems; this includes contractors and third parties who have access to MoJ information assets or IT systems.

### Planning principles

#### Detection

Skilled perpetrators may attempt to cover up their unauthorised or malicious actions. An investigator, using IT forensic tools, can detect these actions and take suitable actions to limit the risk exposure from an incident.

-   **POL.FRP.002**

    The MoJ **must have** the capacity to conduct a forensic investigation \(as required\), whether it involves the use of internal or external capability and resource.


#### Deterrence

IT Security awareness training ensures staff are aware of the [IT Security Acceptable Use Policy](it-acceptable-use-policy.md) and that the MoJ has the right and ability to monitor all IT systems for conformance to this policy. This may deter staff from inappropriate, illegal or malicious actions. Additionally, external awareness of MoJ system monitoring capability may also deter unauthorised users from attempting to access or attack MoJ facilities and IT systems.

-   **POL.FRP.003**

    All users of an IT system **must be** made aware that their access is monitored and that as part of an investigation into a security incident, IT forensic techniques may be used to capture evidence.


#### Consistency

An IT Security Incident Management Plan documents a set of pre-planned procedures and methods for instigating and conducting an investigation. Part of this plan is concerned with the criteria for forensic monitoring and investigation. This is to ensure that all forensic investigations are conducted in a consistent, repeatable fashion.

-   **POL.FRP.004**

    Each IT security incident management plan **must outline** the criteria for initiating a forensic investigation.

-   **POL.FRP.005**

    A Forensic Readiness Plan **must contain** a defined set of procedures and methods for conducting a forensic investigation.


#### Business continuity

It is essential that the MoJ is able to resume or continue business operations after an IT security incident event. It is therefore important that a forensic investigation is conducted in a manner that supports the restoration of IT services. For example, a forensic investigation may involve the removal of hardware assets; steps should be taken to inform the relevant IT supplier to ensure replacement assets are installed.

-   **POL.FRP.006**

    The procedures and methods outlined in a Forensic Readiness Plan **must consider** the business continuity arrangements required to support the restoration of IT services.


#### Evidential ownership and responsibility

Digital evidence can be exceptionally fragile and must be handled extremely carefully to remain admissible. It is essential that at all stages of an incident's investigation, there is a clearly documented chain of custody for all evidential items, including a clear record of who was responsible for carrying out actions upon these evidential items.

-   **POL.FRP.007**

    For all stages of a forensic investigation, there **must be** a clearly documented chain of custody for all evidential items captured.

-   **POL.FRP.008**

    Each forensic investigation **must have** a named forensic investigation owner who is responsible for conducting the investigation and the integrity of any evidence captured.

-   **POL.FRP.009**

    Any investigative action taken on an evidential item \(e.g. an analysis of a hard drive\) **must be** captured and recorded. This record **must include** details of the action taken and the person responsible for undertaking that action. Responsibility for the integrity of evidence resides with the Forensic Investigation Owner and MoJ Operational Security Team \(OST\). In addition, responsibility for any evidence captured, by or passed to an external forensic provider at the start of an investigation, resides with the MoJ and the Forensic Investigation Owner.

-   **POL.FRP.010**

    Admissibility of evidence in a court of law varies with the method of capture. Advice **must be** sought from the MoJ legal team and forensic investigation provider prior to capture if required.

-   **POL.FRP.011**

    Each Forensic Readiness Plan must include details of how any IT assets used or captured as part of a forensic investigation are securely disposed when they are no longer required. This must be in line with IT Security – IT Asset Disposal Guide \[IT Security – IT Asset Disposal Guide\].


#### Enforcement and escalation

Forensic investigations are closely related to MoJ IT security incident management processes. Clear, predefined roles and escalation points will assist in reducing the impact of an incident and allow the business to recover more quickly.

-   **POL.FRP.012**

    Each Forensic Readiness Plan **must have** an escalation path to raise issues identified as part of an investigation as required.


**Note:** The escalation path outlined in a Forensic Readiness Plan should align with the escalation path in the corresponding IT Security Incident Management Plan.

#### Legality

Consideration must be taken in account of the legal and regulatory constraints which apply to the MoJ, which may differ from region to region.

[BS 10008](https://www.bsigroup.com/en-GB/bs-10008-electronic-information-management/) is the British Standard regarding legal admissibility of evidence. This standard provides the foundation for the capture of evidential data \(including capture from IT systems\).

-   **POL.FRP.013**

    All investigations **must be** conducted in line with MoJ IT Security Policies, specifically [IT Security - Acceptable Use Policy](it-acceptable-use-policy.md).

-   **POL.FRP.014**

    The capture of evidence during a forensic investigation **must be** in accordance to [BS 10008](https://www.bsigroup.com/en-GB/bs-10008-electronic-information-management/).

-   **POL.FRP.015**

    All IT systems **must consider**, in their design, the need to capture evidence in an evidential way following [BS 10008](https://www.bsigroup.com/en-GB/bs-10008-electronic-information-management/).


**Note:** Guidance on evidential capture in accordance to [BS 10008](https://www.bsigroup.com/en-GB/bs-10008-electronic-information-management/) is provided in [IT Security - Forensics Readiness Guide](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/forensic-readiness-guide/).

## The need for IT Forensics

### Business risks that require digital evidence collection

It is necessary, as part of incident management, to have the ability to collect and analyse data held on a variety of electronic devices or storage media that may be used as evidence in some future investigation.

### The decision to conduct a forensic investigation

Other than as required by the MoJ's obligations under UK law, all decisions to forensically monitor or investigate a potential security incident must be justified by a risk analysis relating to the need to obtain forensically sound evidence, followed by a cost benefit analysis of how much the required evidence will cost to collect, and what benefit it provides.

-   **POL.FRP.016**

    Unless required by UK law or requested by UK law enforcement, a cost benefit analysis **must be** undertaken before a forensic investigation is launched.


All investigations will either be:

-   Proactive forensic monitoring - As part of an identified MoJ security control, where the appropriateness, legality and costs have been assessed and accepted by the relevant business unit or risk owner.

-   A reactive investigation - Where a suspicious incident has been identified \(or reported\). These investigations require the appropriateness, legality, effects of business disruption, cost and availability of key resources to be considered before the investigation is started.


Forensic investigations are only to be carried out under the following circumstances:

-   Risk Management of a system has revealed a particularly sensitive/vulnerable area which needs to be proactively monitored. Any discovered security incidents would then be escalated through the IT security incident management process.

-   A business function has issued a request to gather forensic investigation evidence directly to the MoJ Defensive Security Operations Team \(DSOT\). Results of such an investigation will be handed back to the requesting business function. Any request will be processed through the appropriate incident management process and escalated to the ITSO, DSO or SIRO as required.

-   An investigation is requested as part of the IT security incident management process. Results of the investigation will be reported back through the incident management process, but other subsidiary processes may also be invoked. Further details available in the [IT Security – Forensic Readiness Guide](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/forensic-readiness-guide/).

-   A forensic investigation is requested by the DSO as part of a leak investigation. Results of an investigation under these circumstances will be reported back to the DSO, who will report to the Permanent Secretary. Further information is available from the [Corporate Security and Business Continuity Branch](https://intranet.justice.gov.uk/guidance/security/).


-   **POL.FRP.017**

    Each Forensic Readiness Plan **must include**, in the criteria for conducting an investigation:

    -   An assessment of the risk management benefits;
    -   The investigation has been authorised by the ITSO, DSO or business group SIRO;
    -   The consideration of a forensic investigation is in line with the corresponding IT security incident management plan process.
-   **POL.FRP.018**

    Where a forensic investigation has been requested in response to a leak investigation. This investigation **must be** requested by the DSO where the DSO is responsible for that investigation.

    **Note:** This may fall outside of the IT security incident management process.


## Capability to collect evidence

### MoJ forensic principles

The following forensic principles are based on [ACPO guidelines](https://www.app.college.police.uk/app-content/investigations/linked-reference-material/):

-   Preservation of Evidence - The forensic investigation process needs to preserve the integrity of the original evidence by providing sufficient security, legal advice and procedural measures to ensure that evidential requirements are met. Any processes applied to copies of evidence must be repeatable and achieve the same results.

-   Aptitude for the task - Any task in a forensic investigation will need to be conducted by a person who is suitably trained and competent to carry out that task.

-   Documented Methodology – All investigations need to follow a documented methodology, as outlined in a Forensic Readiness Plan, with an audit trail of all processes applied to collect evidence. A chain of evidence will need to be created and preserved to demonstrate where evidence has been stored and under whose responsibility from capture until presentation. This allows other investigators to repeat those processes to obtain the same results as required.

-   Conformance - Investigations need to be conducted in a manner which is inline with MoJ policies \(this includes all MoJ corporate policies, not just IT Security policies\).


-   **POL.FRP.019**

    Each forensic investigation **must be** guided by the following principles \(further detail is provided in section 4.1\):

    -   Preservation of Evidence;
    -   Aptitude for the task \(i.e. ability and skill to conduct a forensic investigation\);
    -   Documented Methodology \(as outlined in a Forensic Readiness Plan\);
    -   Conformance to MoJ policies.

### Evidence collection and storage

Collection and management of evidence is the responsibility of the Forensic Investigation Owner for any particular investigation. This may involve the use of an external organisation to conduct the investigation, from the point of capture until presentation back to the MoJ. At all stages of an investigation, all evidential items collected from MoJ sites or IT systems need to be managed according to the applicable Forensic Readiness Plan.

-   **POL.FRP.020**

    Each Forensic Readiness Plan **must include** a process for the collection and storage of digital evidence \(including provision for where this task is conducted by an external organisation\).


### Internal reporting and communication

For all incidents it is necessary to consider the internal reporting and communication requirements, both from the perspective of informing senior management that an incident is ongoing, and also the danger that such a communication might pre-warn any investigation target that remedial and investigative activity is in hand. Roles where reporting and regular communication should be considered include:

-   Senior Management;

-   SIRO;

-   Corporate IA team;

-   HR \(where staff related matters are relevant\);

-   Internal Audit;

-   MoJ legal team;

-   MoJ Data Access and Compliance Unit \(DACU\) – where an incident involves personal data.


-   **POL.FRP.021**

    Each Forensic Readiness Plan **must include** the reporting structure and escalation path which outlines the roles involved and what communications is passed. This must be consistent with reporting structure in the corresponding IT Security Incident Management Plan.

-   **POL.FRP.022**

    Each Forensic Readiness Plan must name a single point of contact that is responsible to co-ordinating any stakeholders involved in a forensic investigation they may be the Forensic Investigation Owner.


### External reporting and escalation

For major incidents it is necessary to consider escalating the forensic investigation process to external bodies, including:

-   Other Government Agencies \(if common assets are affected, or if there are consequential effects\);

-   Law Enforcement;

-   CESG, including GovCertUK and CINRAS;

-   Cabinet Office \(as part of the annual returns required by the SPF\);

-   MoJ legal advisors.


Responsibility for escalation normally resides with the Information Asset Owner \(IAO\) who may also be in charge of the incident investigation. Where responsibility for an investigation has been escalated to the DSO or SIRO, further escalation responsibility will also reside with them.

The impact upon any relevant ongoing operational activity has to be considered before external reporting and escalation is invoked. The forensic investigation process needs to allow for the chain of evidence to be passed to outside agencies \(e.g. a law enforcement agency\).

-   **POL.FRP.023**

    Each Forensic Readiness Plan **must include** details of any external \(non MoJ\) entities which form part of the reporting structure and escalation path.


## References

|ID|Title|Version / Issue|
|--|-----|---------------|
|1|IT Security - Technical Controls Policy|V1-00|
|2|IT Security - Acceptable Use Policy|V1-00|
|3|IT Security - Information Classification and Handling Policy|V1-00|
|4|IT Security - IT Incident Management Policy|V1-00|
|5|HMG Security Policy Framework|Version 8, April 2012|
|6|MoJ Accreditation Framework|V0-01|
|7|BS 10008:2008 - Evidential weight and legal admissibility of electronic information|November, 2008|
|8|Corporate Security and Business Continuity Branch|n/a|
|9|Good Practice Guide for Computer-Based Electronic Evidence – Published by ACPO.|Version 4, 2008|
|10|IT Security - Forensics Readiness Guide|V0-01|
|11|IT Security – IT Asset Disposal Guide|V0-01|

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

