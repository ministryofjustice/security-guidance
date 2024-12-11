# Protective Monitoring Guide

**Related information**  


[Technical Controls Policy](technical-controls-policy.md)

## About this document

**Note:** This is Legacy IA Policy. It is under review and likely to be withdrawn or substantially revised soon. Please contact us before using this on a new project: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk)

This policy applies to all staff and contractors who work for the Ministry of Justice \(MoJ\).

This document is the MoJ IT Security – Protective Monitoring Guide. It is designed to help protect MoJ ICT systems by providing implementation guidance for a protective monitoring solution.

### How to use this document

The purpose of this document is to provide guidance on developing a protective monitoring schema for a MoJ ICT system. It must be read in conjunction with [CESG Good Practice Guide No.13 - Protective Monitoring for HMG ICT Systems](https://www.ncsc.gov.uk/guidance/protective-monitoring-hmg-ict-systems-gpg-13).

**Note:** This document is a supplement to [CESG Good Practice Guide No.13 - Protective Monitoring for HMG ICT Systems](https://www.ncsc.gov.uk/guidance/protective-monitoring-hmg-ict-systems-gpg-13), not a replacement.

## Overview

### Introduction

Protective Monitoring is a set of business processes, with essential support technology, that oversees how ICT systems are used and to assure user accountability for their use of ICT facilities. Protective monitoring places mechanisms for collecting ICT log information to provide an audit trail of defined security relevant events which can be used for reporting and alerting.

[HMG Security Policy Framework \(SPF\)](https://www.gov.uk/government/publications/security-policy-framework) Mandatory Requirement 9 states that:

> Departments and Agencies must put in place an appropriate range of technical controls for all ICT systems, proportionate to the value, importance and sensitivity of the information held and the requirements of any interconnected systems.

In order to meet that requirement, the SPF stipulates that ICT systems must:

> Put in place a proportionate risk based suite of technical policies and controls including: ... IV. Protective Monitoring;

Policy statements on protective monitoring are covered in [IT Security – Technical Controls Policy](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/technical-controls-policy/), while this document sets out the MoJ guidance for its implementation.

### Scope

This guide applies to all MoJ ICT systems including ICT systems hosted by third party suppliers on behalf of the MoJ.

### Demonstration of Compliance

The [CESG Information Assurance Maturity Model \(IAMM\)](https://www.ncsc.gov.uk/guidance/information-assurance-maturity-model-and-assessment-framework-gpg-40) sets out the minimum maturity level Government departments should attain. Protective monitoring is captured as a basic requirement in Level 1 of this model, which the MoJ will need to demonstrate compliance with in their IAMM return to the Cabinet Office.

## Basics of protective monitoring

### Accounting and Auditing

Protective monitoring as described in [CESG Good Practice Guide \(GPG\) No.13](https://www.ncsc.gov.uk/guidance/protective-monitoring-hmg-ict-systems-gpg-13) centres on the concepts of Account and Auditing.

Accounting is defined as 'the process of collecting and recording information about events', whilst Auditing is defined as 'the systematic, independent and documented process for obtaining audit evidence and evaluating it objectively to determine the extent to which audit criteria are fulfilled'.

An organisation can choose to account for almost every transaction that takes place on the system, but then audit almost none of them. When deciding on what approach to take with accounting and auditing it is necessary to first identify what types of information should be recorded then decide what information should be examined and how regularly that examination should be carried out.

### Accreditation and protective monitoring

The audit criteria and the decision on what information is collected and alerted upon must be derived from a risk assessment conducted against the ICT system. This decision making process for the selection of protective monitoring controls forms part of the Accreditation process where the resultant protective monitoring solution **must be** documented in the Risk Management and Accreditation Document Set \(RMADS\). This document provides guidance on the [selection of those controls](#minimum-control-objectives), the [key questions](#key-questions) to be applied to that selection and a [template for documenting it](#protective-monitoring-schema-template).

Further details on the Accreditation process can be found in the [Accreditation Framework](https://intranet.justice.gov.uk/documents/2015/04/accreditation-framework.pdf).

**Note:** The Accreditor will assess any protective monitoring solution against [CESG GPG No.13](https://www.ncsc.gov.uk/guidance/protective-monitoring-hmg-ict-systems-gpg-13), the policy statement in the [IT Security – Technical Controls Policy](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/technical-controls-policy/) and this guide.

### Accounting

The decision on how much information needs to be recorded in an accounting log requires a comprehensive assessment and must be consummate with the risks identified. Recording too much information can be as great a problem as recording too little. If too much information is recorded it can become extremely difficult to review and can cause performance and capacity problems for an ICT system. If too little information is recorded it may be impossible to investigate a security incident effectively.

A good method of analysing this problem is to have a structured approach whereby the different types of information which could be captured are analysed at the different levels of an ICT system \(e.g. network, system and application\), building a picture of the inter-relationships between the different accounting logs \(at those different levels\). For example, accounting may take place at the following levels:

-   Network accounting \(e.g. logs created by network components, such as firewalls or domain controller\);
-   System accounting \(e.g. logs created by individual host systems, such as Windows server security logs\);
-   Application accounting \(e.g. logs created by individual applications\).

The network/systems logs can be used to record the following security events:

-   All actions taken by the Administrators;
-   All actions taken whilst using the database administrators' accounts;
-   All updates to operating system files;
-   All workstation time-outs;
-   Any attempts to copy the password file;
-   All updates to the application software;
-   Use of the system out of normal hours.

The application logs tend to record almost all the actions that take place whilst an application is being used. These tend include:

-   All failed log-on attempts;
-   All successful log-ins;
-   All log-offs;
-   All updates to a record;
-   Each time a record is viewed.

### Auditing

The types of auditable event mainly fall into two categories.

Firstly, there are events which need to be checked on a regular basis because they could indicate that someone is actively trying to breach the security of the system. An example of this is unauthorised log-on attempts or copying of the password file.

Secondly, when a breach of security is detected \(or reported\), the work which was being conducted on the system at that time in order to identify:

-   How the breach of security occurred;
-   Who was responsible for the breach;
-   The amount of damage caused by the breach.

To support an investigation into a security incident, it is important to have a range of flexible reporting tools which allow the investigator to sort through the accounting information collected in a variety of different ways, and allows interconnections to be made between data derived from different sources.

**Note:** When considering what types of information which should be captured and what auditing should be implemented, it is important to ensure that the relevant IT Security Incident Management Plan is factored into the decision making process. This is to ensure that any protective monitoring solution supports the identification, alerting and investigation of security incidents. Further information can be found in the [IT Security Incident Response Plan and Process Guide](it-security-incident-response-plan-and-process-guide.md).

## Developing a protective monitoring schema

For the purposes of this guide, a protective monitoring schema sets out all the controls points which will be implemented in an ICT system.

### Development stages

The business process for protective monitoring is captured in Figure 1 of [CESG GPG No.13](https://www.ncsc.gov.uk/guidance/protective-monitoring-hmg-ict-systems-gpg-13). This section covers the stages which should be followed when developing a protective monitoring schema:

-   The key questions which must be applied which selecting protective monitoring control items;
-   The minimum protective monitoring requirement;
-   Selecting minimum control objectives;
-   Setting the minimum audit requirement;
-   Reporting and service validation.

### Key questions

The following key questions cover items which should be thought about when selecting protective monitoring controls:

-   What is being audited and monitored? In terms of:
    -   Usage scenarios - what users are allowed to do and which actions need to be accounted for;
    -   Exceptions and how they will be detected - what users are not allowed to do or what would constitute suspicious activity;
    -   The complexity in terms of the different types of connectivity to support these interactions \(e.g. air-gapped systems, electronic exchanges, remote access, wireless, Internet services, etc.\).
-   What information will be collected to support the accounting, audit and monitoring of these activities?
-   How the information gathered will be used \(including both a list of permitted purposes and a list of prohibited purposes\)?
-   Who will access the protective monitoring data and their associated responsibilities?
-   How the information will be protected, stored, retained and disposed of?
-   How notification of monitoring is achieved and how user consent is obtained, or otherwise?

### Minimum protective monitoring requirement

The minimum level of protective monitoring which need to be implemented is set out in [CESG GPG No.13](https://www.ncsc.gov.uk/guidance/protective-monitoring-hmg-ict-systems-gpg-13); Table 1 following reproduces part of GPG13 which sets the baseline requirement to achieve a minimum level of protective monitoring.

|Protective Monitoring Control|Objective|
|-----------------------------|---------|
|PMC1: Accurate time in logs.|To provide a means of providing accurate time in logs and synchronisation between system components with a view to facilitating collation of events between those components.|
|PMC2: Recording relating to business traffic crossing a boundary.|To provide reports, monitoring, recording and analysis of business traffic crossing a boundary with a view to ensuring traffic exchanges are authorised, conform to security policy, transport of malicious content is prevented and alerted, and that other forms of attack by manipulation of business traffic are detected or prevented.|
|PMC3: Recording relating to suspicious activity at a boundary.|To provide reports, monitoring, recording and analysis of network traffic crossing a boundary with a view to detecting suspect activity that would be indicative of the actions of an attacker attempting to breach an ICT system boundary or other deviation from normal business behaviour.|
|PMC4: Recording of workstation, server or device status.|To detect changes to device status and configuration. Changes may occur through accidental or deliberate acts by a user or by subversion of a device by malware \(e.g. installation of Trojan software or so called "rootkits"\). It will also record indications that are typical of the behaviour of such events \(including unexpected and repeated system restarts or addition of unidentified system processes\).|
|PMC5: Recording relating to suspicious internal network activity.|To monitor critical internal boundaries and resources within internal networks to detect suspicious activity that may indicate attacks either by internal users or by external attackers who have penetrated the internal network.|
|PMC6: Recording relating to network connections.|To monitor temporary connections to the network either made by remote access, virtual private networking, wireless or any other transient means of network connection.|
|PMC7: Recording of session activity by user and workstation.|To monitor user activity and access to ensure they can be made accountable for their actions and to detect unauthorised activity and access that is either suspicious or is in violation of security policy requirements.|
|PMC8: Recording of data backup status.|To provide a means by which previous known working states of information assets can be identified and recovered from in the event that either their integrity or availability is compromised.|
|PMC9: Alerting critical events.|To allow critical classes of events to be notified in as close to real-time as is achievable.|
|PMC10: Reporting on the status of the audit system.|To support means by which the integrity status of the collected accounting data can be verified.|
|PMC11: Production of sanitised and statistical management reports.|To provide management feedback on the performance of the Protective Monitoring system in regard of audit, detection and investigation of information security incidents.|
|PMC12: Providing a legal framework for Protective Monitoring activities.|To ensure that all monitoring and interception of communications is conducted lawfully and that accounting data collected by the system is treated as a sensitive information asset in its own right.|

Table 1 - Minimum audit requirements

#### Additional control objectives

**Note:** During the risk assessment process, additional control objectives may be identified for inclusion into the set derived from [CESG GPG No.13](https://www.ncsc.gov.uk/guidance/protective-monitoring-hmg-ict-systems-gpg-13). These additional control objectives must be recorded in the protective marking schema.

### Minimum control objectives

The minimum control objectives that are to be applied are in the [Protective monitoring schema template](#protective-monitoring-schema-template). These control objectives are provided as a template for the author of the protective marking schema to fill in, notes are provided and once completed can be used as part of the description of the protective monitoring solution presented to the system Accreditor in the RMADS.

Where a minimum control objective cannot be met \(for example, due to an implementation restriction or where the risk does not justify the control\) it must be recorded as an exception \(a template is provided [here](#exceptions) \).

**Note:** This is generic set of control objectives and the templates provided in section A.1 and A.2 are designed for the author of the protective marking schema to customising based on the guidance provided in this document, [CESG GPG No.13](https://www.ncsc.gov.uk/guidance/protective-monitoring-hmg-ict-systems-gpg-13), the ICT system and associated risk assessment.

#### Control objectives extensibility

It is important to ensure that there is a mechanism in place to review, update or extend the protective monitoring controls once an ICT system is in live operation. This will occur when an ICT system undergoes the re-accreditation process, further details of which can be found in the [Accreditation Framework](https://intranet.justice.gov.uk/documents/2015/04/accreditation-framework.pdf).

### Minimum audit requirements

The minimum audit requirement is specified in [CESG GPG No.13](https://www.ncsc.gov.uk/guidance/protective-monitoring-hmg-ict-systems-gpg-13) where the following provides the audit criteria which **must be** captured in the protective monitoring schema \(a template table is provided [here](#audit-regime) \):

-   The retention period of any protective monitoring data captured;
-   Details on when log checks are to be carried;
-   Details on when the protective monitoring system is to be manned;
-   Details on when the system is to be subject to compliance review;
-   Details on the reporting structure \(refer to [Reporting Structure](#reporting-structure) \), which should be specified in terms of a weekly, monthly or annual report.

### Baseline Control Set and implementation of controls objectives

Table 2 defines the minimum controls which **must be** implemented to achieve the baseline controls set out in [HMG IA Standard Numbers 1 &amp; 2 – Supplement: Technical Risk Assessment and Risk Treatment](https://www.ncsc.gov.uk/guidance/technical-risk-assessment-and-risk-treatment-is1-2-supplement).

|Control|Baseline Control|Notes|
|-------|----------------|-----|
|10.10.1 Audit logging|In accordance with SPF Departments must ensure that ICT systems are capable of producing records of user activity to support monitoring, incident response and investigations.|Routine user activity such as log-on and log-off, log-on failures, keyboard inactivity, password change, object permissions change, read/write access to objects, import/export, print, object save and deletion.|
|10.10.2 Monitoring system use|Departments must develop and implement procedures to monitor use of systems and services by users to support incident response and investigation activities.|Establish baseline activity within the environment and develop auditable events outside this baseline activity.|
|10.10.3 Protection of log information|Audit logs must be protected in accordance with their sensitivity or protective marking.|The BIL of log information captured must be documented in the ICT system's Business Impact Assessment \(BIA\).|
|10.10.4 Administrator and operator logs|ICT systems must be capable of generating audit logs for all system users including system administrators.|Log collection and storage.|
|10.10.5 Fault logging|Departments must log and review system faults at regular intervals.|System management activity.|
|10.10.6 Clock synchronisation|Departments must implement a reliable means to keep all server and device clocks of the ICT System in synchronisation.|Establish time server.|
|13.2.3 Collection of evidence|In accordance with [Security Policy Framework MR 9](https://intranet.justice.gov.uk/documents/2015/04/security-policy-framework.doc) Departments must have 'a forensic readiness policy that will maximise the ability to preserve and analyse data generated by an ICT system, that may be required for legal and management purposes'.|How is the integrity of the collected data assured? How is collected data stored to prevent unauthorised access?|
|15.3.1 Information system audit controls|Departments must implement plans and controls to ensure that audit and compliance checks do not adversely affect the business operation of an ICT system.|Minimum impact on services is required. Does this mean no degradation of service?|
|15.3.2 Protection of information system audit tools|System audit tools must be protected to prevent their use for unauthorised purposes.|Installed and controlled in a physically separate environment with protected network connectivity.|

Table 2 - Baseline controls to achieve protective monitoring

With Table 2 in mind [CESG GPG No.13](https://www.ncsc.gov.uk/guidance/protective-monitoring-hmg-ict-systems-gpg-13) outlines a number of options which should be consider when translating the identified control objectives into a protective monitoring solution which can be implemented in an ICT system.

The following provides the typical list of components which can be put together to deliver a protective monitoring solution:

-   Security Information and Event Management \(SIEM\) system, which includes:
    -   Log collection;
    -   Log analysers;
    -   Filtering, query and pattern matching tools;
    -   Reporting tools;
    -   Computer forensic tools;
    -   Network management system;
-   Intrusion Detection and Prevention System \(IDS/IPS\);
-   Network Intrusion Detection System \(NIDS\);
-   Host Intrusion Detection System \(HIDS\);
-   Wireless Intrusion Detection System \(WIDS\).

A template is provided [here](#accounting-items) to capture all the accounting items to be collected and where those items are collected.

### Reporting Structure

Protective monitoring is only effective if there is a clear and effective reporting structure is in place to ensure that any alerts generated by the protective monitoring solution are escalated to the relevant people.

**Note:** The protective monitoring solution must fit into the overall IT Security Incident Management plan; refer to the [IT Security Incident Response Plan and Process Guide](it-security-incident-response-plan-and-process-guide.md) for further details.

### Service Validation

Once the protective monitoring schema has been generated and approved by the system Accreditor, the next step in delivering an effective protective monitoring solution is ensuring that the service provided is working as planned and that it is effectively gathering the data. This part of the protective monitoring solution must be document and should contain the following:

-   Details on the initial operational capability and the start date;
-   A defined series of service review points, specifically identifying the review of the control sets and the validation of data gathered;
-   A defined criteria for spurious or unnecessary data that should be identified during the validation period and removed from the log reporting/alerting mechanism;
-   Details on the full operational capability and the start date. At the point the protective monitoring service is fully operational, no changes may be made to the service without the approval of the system Accreditor.

## Protective monitoring schema template

### Minimum control objective

This section of the template captures the implementation details and compliance evidence for each protective monitoring control \(PMC\) specified in [CESG GPG No.13](https://www.ncsc.gov.uk/guidance/protective-monitoring-hmg-ict-systems-gpg-13). A minimum control object for each PMC is entered and is intended to provide an initial starting position.

Minimum control objective for PMC 1

For PMC 1 the following is to be implemented:

|Detail|Notes/Statement of Compliance|
|Control| |
|Accurate time in logs.|\[Insert additional notes/test as required.\]|
|Control Description| |
|Provide a means of providing accurate time in logs and synchronisation between system components to facilitate collation of events between those components. The error margin for time accuracy is to be specified.|\[Use any of the following: Providing a master clock system component which is synchronised to an approved time source \(e.g. GSi time source\); Updating device clocks from the master clock using the Network Time Protocol \(NTP\); Record time in logs in a consistent format \(Universal Co-ordinated Time \(UTC\) is recommended\)\]|
|Objective| |
|Provide a centralised, single time reference for all components that are subject to monitoring.|Any of the previous mechanisms may be used and an existing clock source within the support environment should be used where possible.|
|Risk Level| |
|VERY LOW/LOW/MEDIUM|\[Insert Risk level\]|
|Service Description|Report|Alert|Proposed control/implementation|
|\[Insert controls to be applied and any additional controls identified as part of analysis.\]|\[Insert R to denote report\]|\[Insert A to denote alert\]|\[Insert additional notes/test as required.\]|

Minimum control objective for PMC 2

For PMC 2 the following is to be implemented:

|Detail|Notes/Statement of Compliance|
|Control| |
|Recording of business traffic crossing a boundary.|\[Insert additional notes/test as required.\]|
|Control Description| |
|Provide reports, monitoring, recording and analysis of business traffic crossing a boundary with a view to ensuring traffic exchanges are authorised, conform to security policy, transport of malicious content is prevented and alerted, and that other forms of attack by manipulation of business traffic are detected or prevented.|\[Insert additional notes/test as required.\]|
|Objective| |
|Ensure only authorised traffic is passed into and out of the PM environment.|\[Insert additional notes/test as required.\]|
|Risk Level| |
|VERY LOW/LOW/MEDIUM|Insert Risk level|
|Service Description|Report|Alert|Proposed control/implementation|
|\[Insert controls to be applied and any additional controls identified as part of analysis.\]|\[Insert R to denote report\]|\[Insert A to denote alert\]|\[Insert additional notes/test as required.\]|

Minimum control objective for PMC 3

For PMC 3 the following is to be implemented:

|Detail|Notes/Statement of Compliance|
|Control| |
|Recording relating to suspicious activity at the boundary.|\[Insert additional notes/test as required.\]|
|Control Description| |
|Provide reports, monitoring, recording and analysis of network activity at the boundary with a view to detecting suspect activity that would be indicative of the actions of an attacker attempting to breach the system boundary or other deviation from normal business behaviour.|\[Insert additional notes/test as required.\]|
|Objective| |
|Identify potential or actual attempts to access the ICT System environment by an unauthorised individual who is external to the environment|\[Insert additional notes/test as required.\]|
|Risk Level| |
|VERY LOW/LOW/MEDIUM|*\[Insert Risk level\]*|
|Service Description|Report|Alert|Proposed control/implementation|
|\[Insert controls to be applied and any additional controls identified as part of analysis.\]|\[Insert R to denote report\]|\[Insert A to denote alert\]|\[Insert additional notes/test as required.\]|

Minimum control objective for PMC 4

For PMC 4 the following is to be implemented:

|Detail|Notes/Statement of Compliance|
|Control| |
|Recording on internal workstation, server or device status.|\[Insert additional notes/test as required.\]|
|Control Description| |
|Detect changes to device status and configuration.|\[Insert additional notes/test as required.\]|
|Objective| |
|Identify and report authorised and unauthorised changes to the configuration of devices in the environment.|\[Insert additional notes/test as required.\]|
|Risk Level| |
|VERY LOW/LOW/MEDIUM|*Insert Risk level*|
|Service Description|Report|Alert|Proposed control/implementation|
|\[Insert controls to be applied and any additional controls identified as part of analysis.\]|\[Insert R to denote report\]|\[Insert A to denote alert\]|\[Insert additional notes/test as required.\]|

Minimum control objective for PMC 5

For PMC 5 the following is to be implemented:

|Detail|Notes/Statement of Compliance|
|Control| |
|Recording relating to suspicious internal network activity.|\[Insert additional notes/test as required.\]|
|Control Description| |
|Monitor critical internal boundaries and resources within internal networks to detect suspicious activity that may indicate attacks either by internal users or by external attackers who have penetrated to the internal network.|\[Insert additional notes/test as required.\]|
|Objective| |
|Identify internal and external attacks on the environment network.|\[Insert additional notes/test as required.\]|
|Risk Level| |
|VERY LOW/LOW/MEDIUM|*Insert Risk level*|
|Service Description|Report|Alert|Proposed control/implementation|
|\[Insert controls to be applied and any additional controls identified as part of analysis.\]|\[Insert R to denote report\]|\[Insert A to denote alert\]|\[Insert additional notes/test as required.\]|

Minimum control objective for PMC 6

For PMC 6 the following is to be implemented:

|Detail|Notes/Statement of Compliance|
|Control| |
|Recording relating to network connections.|\[Insert additional notes/test as required.\]|
|Control Description| |
|Monitor temporary connections to the network either made by remote access, virtual private networking, wireless or any other transient means of network connection.|\[Insert additional notes/test as required.\]|
|Objective| |
|Identify, monitor and audit temporary connections to the environment.|\[Insert additional notes/test as required.\]|
|Risk Level| |
|VERY LOW/LOW/MEDIUM|*Insert Risk level*|
|Service Description|Report|Alert|Proposed control/implementation|
|\[Insert controls to be applied and any additional controls identified as part of analysis.\]|\[Insert R to denote report\]|\[Insert A to denote alert\]|\[Insert additional notes/test as required.\]|

Minimum control objective for PMC 7

For PMC 7 the following is to be implemented:

|Detail|Notes/Statement of Compliance|
|Control| |
|Recording on session activity by user and workstation.|\[Insert additional notes/test as required.\]|
|Control Description| |
|Monitor user activity and access to ensure they can be made accountable for their actions.|\[Insert additional notes/test as required.\]|
|Objective| |
|Detect unauthorised activity and access that is either suspicious or is in violation of security policy.|\[Insert additional notes/test as required.\]|
|Risk Level| |
|VERY LOW/LOW/MEDIUM|*Insert Risk level*|
|Service Description|Report|Alert|Proposed control/implementation|
|\[Insert controls to be applied and any additional controls identified as part of analysis.\]|\[Insert R to denote report\]|\[Insert A to denote alert\]|\[Insert additional notes/test as required.\]|

Minimum control objective for PMC 8

For PMC 8 the following is to be implemented:

|Detail|Notes/Statement of Compliance|
|Control| |
|Recording on data backup status.|\[Insert additional notes/test as required.\]|
|Control Description| |
|Provide for a previously known working state of information assets to be identified and recovered.|\[Insert additional notes/test as required.\]|
|Objective| |
|Implement and audit backup and recovery procedures.|\[Insert additional notes/test as required.\]|
|Risk Level| |
|VERY LOW/LOW/MEDIUM|*Insert Risk level*|
|Service Description|Report|Alert|Proposed control/implementation|
|\[Insert controls to be applied and any additional controls identified as part of analysis.\]|\[Insert R to denote report\]|\[Insert A to denote alert\]|\[Insert additional notes/test as required.\]|

Minimum control objective for PMC 9

For PMC 9 the following is to be implemented:

|Detail|Notes/Statement of Compliance|
|Control| |
|Reporting on the status of the audit system.|\[Insert additional notes/test as required.\]|
|Control Description| |
|Event reporting.|\[Insert additional notes/test as required.\]|
|Objective| |
|Provide a mechanism for reporting in near real-time.|\[Insert additional notes/test as required.\]|
|Risk Level| |
|VERY LOW/LOW/MEDIUM|*Insert Risk level*|
|Service Description|Report|Alert|Proposed control/implementation|
|\[Insert controls to be applied and any additional controls identified as part of analysis.\]|\[Insert R to denote report\]|\[Insert A to denote alert\]|\[Insert additional notes/test as required.\]|

Minimum control objective for PMC 10

For PMC 10 the following is to be implemented:

|Detail|Notes/Statement of Compliance|
|Control| |
|Alerting critical events.|\[Insert additional notes/test as required.\]|
|Control Description| |
|Maintain status of the protective monitoring system and its collected accounting data.|\[Insert additional notes/test as required.\]|
|Objective| |
|Ensure the integrity and proper management of the protective monitoring system.|\[Insert additional notes/test as required.\]|
|Risk Level| |
|VERY LOW/LOW/MEDIUM|*Insert Risk level*|
|Service Description|Report|Alert|Proposed control/implementation|
|\[Insert controls to be applied and any additional controls identified as part of analysis.\]|\[Insert R to denote report\]|\[Insert A to denote alert\]|\[Insert additional notes/test as required.\]|

Minimum control objective for PMC 11

For PMC 11 the following is to be implemented:

|Detail|Notes/Statement of Compliance|
|Control| |
|Alerting critical events.|\[Insert additional notes/test as required.\]|
|Control Description| |
|Maintain status of the protective monitoring system and its collected accounting data.|\[Insert additional notes/test as required.\]|
|Objective| |
|Ensure the integrity and proper management of the protective monitoring system.|\[Insert additional notes/test as required.\]|
|Risk Level| |
|VERY LOW/LOW/MEDIUM|*Insert Risk level*|
|Service Description|Report|Alert|Proposed control/implementation|
|\[Insert controls to be applied and any additional controls identified as part of analysis.\]|\[Insert R to denote report\]|\[Insert A to denote alert\]|\[Insert additional notes/test as required.\]|

Minimum control objective for PMC 12

For PMC 12 the following is to be implemented:

|Detail|Notes/Statement of Compliance|
|Control| |
|Providing a legal framework for Protective Monitoring activities.|\[Insert additional notes/test as required.\]|
|Control Description| |
|Ensure that all monitoring and interception of communications is conducted lawfully and that accounting data collected by the system is treated as a sensitive information asset in its own right.|\[Insert additional notes/test as required.\]|
|Objective| |
|Maintain legal and statutory obligations.|\[Insert additional notes/test as required.\]|
|Risk Level| |
|VERY LOW/LOW/MEDIUM|*Insert Risk level*|
|Service Description|Report|Alert|Proposed control/implementation|
|\[Insert controls to be applied and any additional controls identified as part of analysis.\]|\[Insert R to denote report\]|\[Insert A to denote alert\]|\[Insert additional notes/test as required.\]|

### Exceptions

The exceptions to the minimum baseline requirements [must be recorded](#minimum-control-objectives), based on the following template table.

|Serial|Protective Monitoring Control|Control Detail|Reason for non-compliance|
|\[Insert details of those controls that will not be implemented as a result of reviewing the protective monitoring controls for each of the defined levels to show which controls either cannot be implemented for technical reasons, or as a result of a risk management decision. Delete this row on completion of table.\]|
| | | | |
| | | | |

### Audit regime

The audit regime which forms part of the protective marking solution [must be recorded](#minimum-audit-requirements) based on the following template table:

|Risk Level|Log Retention Period|Log Checks|Console Manning|Compliance Review Period|Report Production|
| | | | | | |

### Accounting items

The following table provides a template to capture [all the accounting items to be collected](#baseline-control-set-and-implementation-of-controls-objectives) in an ICT system, its source and alerting details.

|PMC|\#|Cat|Ref|Recordable events|Include in report|Alert on event|Method|Notes in Environment PM policy|Accounting items \(defined in GPG13\)|Sources and notes|Logging application requirement|Tags|Predicate|Specific Events: Audit|Specific Events: Errors &amp; Warnings|Specific Events: Protocol errors|
| | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | |

## Contact and Feedback

For any further questions or advice relating to security, or for any feedback or suggestions for improvement, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).

