# IT Incident Management Policy

Incident management is the ability to react to security incidents in a controlled, pre-planned manner. Preparation and planning are key factors to successful information security management and all Ministry of Justice \(MoJ\) systems rely on Incident Management Plans for safe and secure operations.

The aim of this policy is to ensure best practice is followed by all IT systems when dealing with security incidents, in particular, those pertaining to data loss, in a timely and efficient manner.

**POL.IMP.001:**

Each MoJ Business Group **must have** an IT Security Incident Management Plan which aligns to this policy. This plan must be common to all IT systems within a particular business group.

A template plan and guidance on the construction of an IT Security Incident Management Plan is provided in [IT Security – Incident Management Plan and Process guide](incident-management-plan-and-process-guide.md).

**Related information**  


[Technical Controls Policy](technical-controls-policy.md)

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

## Scope

This policy is concerned with IT related security incidents outlining the roles and responsibilities, escalation path and criteria for escalation.

## Relationship with wider MoJ functions

An IT system is one element of a number of supporting elements which sustain MoJ business functions and delivery of services. The MoJ [Corporate Security and Business Continuity Branch](https://intranet.justice.gov.uk/guidance/security/) is responsible for overall MoJ Incident Management policy and plan. This policy is designed to sit within the overall MoJ incident management structure.

## Incident Management Process

An incident management process is a prepared course of actions that will be instigated upon the detection or report of a security incident. Incident management requires a variety of decisions to be made, drawing on the experience of a number of roles, depending on the nature of the incident.

The incident management process supports the making of informed decisions following a consistent approach designed to reduce the consequences of any incident.

### Definition of an Incident

For the purposes of this policy, an incident is defined as any event or action which results in an actual and/or potential compromise of a MoJ IT asset or MoJ Information Asset \(including personal data\).

Such events will result in the MoJ, individuals or IT systems and/or the information held on them being exposed, or potentially exposed, to illegitimate access. As a result, incidents have the potential to compromise MoJ business delivery, the Data Protection Act, as well as the confidentiality, integrity and availability of IT systems and the information held on them. This may, in turn cause harm, distress or other damage to individuals or organisations, and result in operational disruption or reputation damage to the MoJ.

#### Types of Incidents

IT Security related incidents include \(but are not limited to\):

-   Breaches of the [Acceptable Use Policy](acceptable-use-policy.md);
-   Detection of malicious code \(e.g. viruses and malware\);
-   Network attacks or Denial of Service \(DOS\) attacks;
-   Scanning and probing of a network \(where significant network resources are consumed\);
-   Inappropriate use of MoJ IT assets as defined in the [Acceptable Use Policy](acceptable-use-policy.md);
-   The discovery of a new network vulnerability or release of a patch or software update which is considered critical or an emergency;
-   The results of a penetration test on a live operational IT system that reveals critical vulnerabilities;
-   Unauthorised access to an IT system;
-   Accidental loss of personal or other information assets;
-   Deliberate release of personal or other information assets;
-   Compromise of integrity; or
-   Any alerts or suspicious activity report generated by an IT system that proves to be a real security alert.

### Incident Detection and Recording

Security Incidents may come to light from a variety of sources, including through protective monitoring solutions, reports filled by MoJ staff or breaches of the MoJ IT Security Policy detected by an IT system.

The [MoJ IT Security Policy](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/ict-security-policy/) defines the requirements for capturing and recording security events and monitoring them for suspected malicious activity or breaches of security.

This section of the policy is concerned with taking those security events and ensuring that if an event relates to an actual IT Security incident, this incident is appropriately recorded.

**POL.IMP.002:**

All IT Security incidents or suspected incidents **must be** reported to the MoJ [Security team](mailto:security@justice.gov.uk) within 60 minutes of detection.

**POL.IMP.003:**

For all incidents involving an IT Security incident, an IT Security Incident Report Form **must be** completed and submitted to the [Security team](mailto:security@justice.gov.uk) \([Reporting an incident or breach](https://intranet.justice.gov.uk/guidance/security/report-a-security-incident/) \). This is irrespective of the reporting route \(i.e. a User direct with [Security team](mailto:security@justice.gov.uk) or a user via the IT Service Desk\).

**POL.IMP.004:**

All IT Security incidents involving personal data \(or other information assets\) **must be** reported to the MoJ Data Access and Compliance Unit: [Data.access@justice.gov.uk](mailto:Data.access@justice.gov.uk).

The MoJ [Security team](mailto:security@justice.gov.uk) is responsible for maintaining a centralised database and view of all IT Security incidents across any MoJ IT system. This database contains information on:

-   Security incident reports;

-   An up to date status of all reported security incidents;

-   An up to date status of any actions taken with respect to a particular security incident.


This database and the effective reporting of security incidents which populate it are important in managing the MoJ's overall risk exposure. This is both in the short term, to identity any major deficiencies with an IT system which requires immediate remedial action and in the long term, to capture lessons learnt to improve Information Assurance maturity.

### Categorisation of incidents

Security incidents are categorised in order to assess their impact and required level of escalation. This is to ensure that the appropriate resources can be allocated and incident resolution is conducted in a timely manner.

The three categories are:

-   Low Impact \(refer [here](#low-impact-incident) \);

-   Medium Impact \(refer [here](#medium-impact-incident) \);

-   High Impact \(refer [here](#high-impact-incident) \).


**POL.IMP.005:**

All IT Security incidents **must be** categorised in accordance with this policy.

The nature of an incident may not be immediately obvious when it is first reported; further assessments of its categorisation need to be made as more information is gathered. For example, through conducting an investigation \(refer to Figure 2 which outlines this process flow\).

The following sub-sections provide an overview of the three categories with further guidance on its practical application provided in [IT Security – Incident Management Plan and Process Guide](incident-management-plan-and-process-guide.md).

#### Low impact incident

Low impact incidents would typically be minor internal infractions, such as, a low level breach in IT Security, or, a minor loss of an IT service \(e.g. due to a short loss of power\).

A low impact personal data incident would typically include an incident where no actually data had been lost but a weakness in an IT system which may have led to a potential loss is discovered where a relatively small amount of remedial action is required to address the vulnerability.

#### Medium impact incident

Examples of a medium level impact event include \(but are not limited to\):

-   Deliberate disregard for the MoJ [IT Security Policy](it-security-policy-overview.md) leading to minor breach in security or the potential of data loss;
-   Inappropriate use of MoJ IT assets as defined in [Acceptable Use Policy](acceptable-use-policy.md);
-   Loss of data or IT asset \(where the data or asset does not contain any personal data and is not protectively marked\);
-   Theft of data or IT asset \(where the data or asset is does not contain any personal data and is not protectively marked\);
-   Damage to any MoJ IT asset;
-   Connecting unauthorised equipment to an IT system \(where there is no intent or suspicion of malicious activity\);
-   Prolonged or permanent failure of an IT system;
-   Prolonged set of unsuccessfully attempts to scan an IT network or instigate a denial of service attack;
-   Any alert or reported suspicious activity on an IT system \(note this may need to be escalated to High Impact upon investigation\);
-   Compromise of integrity;
-   The recognition of a new critical security vulnerability in an IT system \(this may be the result of a penetration test\);
-   The release of a critical patch by an application or IT equipment vendor;
-   Localised report of malicious code \(e.g. the detection of a virus or malware of a desktop terminal\);
-   Serious case of equipment theft; or
-   The theft or loss of HMG cryptographic material.

#### High Impact Incident

IT Security incidents at this level require immediate escalation to the relevant MoJ Business Group Senior Information Risk Owner \(SIRO\) in addition to the [Security team](mailto:security@justice.gov.uk) and where applicable, the MoJ Data Access and Compliance Unit: [Data.access@justice.gov.uk](mailto:Data.access@justice.gov.uk).

Incident at this impact may warrant forensic investigation.

Examples of incidents at the level include \(but are not limited to\):

-   Evident of malicious activity, intent or espionage;

-   An incident which comes to the attention of local or national media;

-   Any successful network intrusion;

-   Widespread malicious code attacks \(e.g. a worm spreading across an IT system\);

-   The release of an emergency patch by an application or IT equipment vendor;

-   The theft or loss of personal or protectively marked data from an IT system.


#### Further escalation requirements

The decisions to escalate an incident irrespective of its impact up through the chain from ITSO, MoJ SIRO, DSO, and higher \(possible to Ministerial level\) may include the following factors:

-   Issues of national security;

-   If the incident has received local/national press coverage;

-   If the incident has caused harm to a member of staff or public;

-   There is high likelihood that the MoJ has suffered reputational damage or been brought into disrepute;

-   Where there is a HMG requirement to report to another Department or central management function \(e.g. GovCERT for network incidents or CINRAS for incidents involving HMG cryptographic material\);

-   Where there is a significant actual or possible loss of personal information where the Information Commissioner's Office and Cabinet Office need to be informed.


## Incident Management Stakeholders

This policy outlines the general incident management stakeholders and escalation path principles. Each MoJ business group implementation of this policy \(which is the creation and acceptance of an IT Security Incident Management Plan\) will need to consider how this is practically implemented, all the individual stakeholders involved \(including others such as IT suppliers\), and escalation path.

### All MoJ staff \(including contractors and agency staff\)

It is important that all MoJ staff are aware of what a security incident is and how to correctly report it.

**POL.IMP.006:**

All MoJ staff **must** report any concerns that the MoJ [IT Security Policy](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/ict-security-policy/) is not being followed to their line manager.

**POL.IMP.007:**

All MoJ staff **must** report any breach of the MoJ [IT Security Policy](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/ict-security-policy/) as an IT Security incident.

**POL.IMP.008:**

All MoJ staff must report any suspicious activity which indicates an IT Security incident has occurred.

**POL.IMP.009:**

All MoJ staff **must** report an IT Security incident either to the IT Service Desk or directly to the MoJ Operational Security Team using an IT Security Incident Report Form.

### MoJ Senior Managers

POL.IMP.010:

All MoJ Local Managers **must ensure** that all IT Security or personal data incidents or breaches are reported and taken seriously. These include facilitating any investigation and, where appropriate, pursue disciplinary action and/or legal proceedings.

### Senior Information Risk Owner \(SIRO\)

**POL.IMP.011:**

Each MoJ business group SIRO **must ensure** that each IT domain \(e.g. DISC or OMNI\) which fall under their remit has an IT Security Incident Management Plan which implements this policy. A template plan and guidance is available in [IT Security – Incident Management Plan and Process guide](incident-management-plan-and-process-guide.md).

**POL.IMP.012:**

All High impact IT Security incidents and any IT Security incident involving personal data **must be** reported to the SIRO immediately.

### Information Asset Owner \(IAO\)

The role of an IAO is to understand what information is held, how it's adapted, used, shared and removed from an IT system.

**POL.IMP.013:**

All IT Security incidents involving the loss, theft or compromise of an Information Asset **must be** reported to the asset's IAO.

### MoJ Security Team

The [Security team](mailto:security@justice.gov.uk) are responsible for:

-   Incident ownership, monitoring, tracking and communication

-   Sanction enhanced monitoring on IT systems where appropriate

-   Update the incident management database with details of all incidents, any investigation conducted and actions undertaken

-   Carry out analysis of security incidents as required

-   Initiating a forensic investigation and commissioning forensic analysis \(in accordance with the [Forensic Readiness Policy](forensic-readiness-policy.md) \)

-   Providing progress reports on specific incidents to relevant parties.


### IT Service Desk

The IT Service Desk plays a crucial role in ensuring security incidents are correctly reported and escalated to the [Security team](mailto:security@justice.gov.uk) in a timely manner. The majority of IT Security incident will be reported to the IT Service Desk first. Also, the IT Service Desk can help identify where a user reporting an issue is actually an IT Security incident. It is therefore important that the IT Service Desk recognise this and report it to the [Security team](mailto:security@justice.gov.uk).

**POL.IMP.014:**

Where the IT Service Desk receives a report of a security incident, this **must be** reported and escalated to the [Security team](mailto:security@justice.gov.uk) immediately.

### Escalation Path

As a rule, all IT Security incidents are reported to [Security team](mailto:security@justice.gov.uk). As depicted in Figure 2, [Security team](mailto:security@justice.gov.uk) then progress the incident according to its categorisation \(refer [here](#categorisation-of-incidents) \). Depending on the category and nature of the incident, this can involve escalating the incident to other stakeholders.

**POL.IMP.015:**

Each IT Security Incident Management Plan **must include** a pre-arranged escalation path where each stakeholder is named and aware of their role in the Incident Management Plan.

A generic escalation path is provided [here](#it-security-incident-escalation-path). This generic path is intended to provide a starting point where further guidance on tailoring and customisation is provided in the [IT Security – Incident Management Plan and Process Guide](incident-management-plan-and-process-guide.md).

## Investigation and Diagnosis capability

The MoJ [Security team](mailto:security@justice.gov.uk) is responsible for the investigation of all IT Security incidents. Where evidence gathering is required for possible disciplinary or legal proceedings, a forensic investigation may be required, further details are provided in the [Forensic Readiness Policy](forensic-readiness-policy.md).

In the course of investigation, the [Security team](mailto:security@justice.gov.uk) may:

-   Investigate incidents at the direction of the ITSO;

-   Proactively monitor suspected targets or IT systems to capture potential suspicious behaviour for analysis;

-   Undertake or oversee an investigation requested by an outside agency \(e.g. CESG\) where authorised by the ITSO;

-   Recover and securely store evidence where required;

-   Require a SIRO or Senior Manager to collect more information on an IT Security incident.


**POL.ITSEC.016:**

The MoJ [Security team](mailto:security@justice.gov.uk) **must maintain** files on any investigation undertaken.

**POL.ITSEC.017:**

Any diagnosis of an IT Security incident and the events surrounding it **must be** shared and reported to relevant stakeholders.

### Resolution, Recovery and Incident Closure

Based on the investigation of an IT Security incident, remedial action may be required to ensure appropriate incident resolution and the recovery of any IT services or information assets compromised as a result of the incident.

**POL.ITSEC.018:**

An IT system which has a significant compromise \(Medium or High impact, refer [here](#categorisation-of-incidents) \) **must be** reported to the system Accreditor and a review of that system's risk assessment and accreditation must be conducted.

**POL.ITSEC.019:**

All IT Security incidents for an IT system **must be** collated and provided to the system Accreditor during the re-accreditation process.

### Recovering from an IT Security incident

There may be occasions when it is appropriate to restore a system that has been attacked or compromised from its backup since it might be the only way to ensure system integrity.

Checks must be made to ensure the IT system being restored pre-dates the incident and does not contain any exploitable weaknesses, for example, ensure the IT system is fully patched before it is brought back into service.

**POL.ITSEC.020:**

The IT Security Incident Management Plan for an IT System or overarching IT Domain **must include** details on how that system or IT domain IT services are restored \(or recovered\) following an IT Security incident.

**Note** – The detail of how an IT system recovers from an incident event should be captured in that systems disaster recovery plan. Refer to the [IT Security – Disaster Recovery Policy](it-disaster-recovery-policy.md) for further information.

## Preventing re-occurrences

Once the cause of an IT Security incident has been identified, steps must be taken to reduce the risk of its reoccurrence, for example eradicate any computer viruses, block firewall ports, and install any missing system patches, as necessary.

### Learning points

When an IT Security incident has been resolved and closed, a management report needs to be prepared outlining the incident, the outcome of the investigation, actions taken, and recommendations about how to improve the business systems to reduce the likelihood of a reoccurrence.

Copies of the report must be sent to the ITSO who has a responsibility for forwarding the report onto any HMG central reporting functions, for example CESG, GovCertUK or CINRAS, as appropriate.

**POL.ITSEC.021:**

For each Medium and High impact \(refer [here](#categorisation-of-incidents) \) IT Security incident, a management report **must be** prepared covering:

-   A description of the incident;

-   The outcome of the incident investigation;

-   Actions raised \(or taken\) with associated action owners;

-   Any recommendations made.


## IT Security Incident Recording and Categorisation

![IT Security Incident Recording and Categorisation](images/incident-management-plan-and-process-guide-diagram-3.png)

## IT Security Incident Escalation Path

The following is a generic IT Security incident escalation path which provides a starting point for the creation of a tailored version in an IT Security Incident Management Plan. Further information is provided in the [IT Security – Incident Management Plan and Process Guide](incident-management-plan-and-process-guide.md).

![IT Security Incident Escalation Path](images/incident-management-plan-and-process-guide-diagram-4.png)

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

