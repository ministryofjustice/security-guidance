---
Review: 2021-12-31
Owner: CISO
---

[Home > Cyber and Technical Security](../..)

# Operations Security Policy

## Introduction

This policy gives an overview of the operations security and responsibilities within the Ministry of Justice (MoJ) and provides a summary of the MoJ's related operations security policies and guides.

## Who is it for?

This policy is aimed at:
- **Technical users:** these are in-house MoJ Digital and Technology staff who are responsible for implementing controls throughout technical design, development, system integration and operation. This includes DevOps, Software Developers, Technical Architects and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI and Knowledge (EPICK) Team.
- **Service Providers:** defined as any other MoJ business group, agency, contractor, IT supplier and partner who in any way designs, develops or supplies services (including processing, transmitting and storing data) for, or on behalf of the MoJ.
- **General users:** all other staff working for the MoJ.

'All MoJ users' refers to General users, Technical users and Service Providers as defined above.

## Operational procedures and responsibilities

Ensure correct and secure operations of information processing facilities.

Offshoring
Infrastructure and system accreditation
Active Cyber Defence

### Documented operating procedures

Operating procedures must be documented and made available to all users who need them. Documented procedures must be prepared for operational activities associated with information processing and communication facilities, such as:

- computer start-up and close-down procedures
- backup
- equipment maintenance
- media handling
- computer room
- mail handling management and safety

Operating procedures and the documented procedures for system activities must be treated as formal documents and changes authorised by management. Where technically feasible, information systems should be managed consistently, using the same procedures, tools and utilities.

### Change management

Changes to the organisation, business processes, information processing facilities and systems that affect information security must be controlled.

Formal management responsibilities and procedures must be in place to ensure satisfactory control of all changes. When changes are made, an audit log containing all relevant information must be retained.

### Capacity management

The use of resources must be monitored, tuned and projections made of future capacity requirements to ensure the required system performance.

Capacity requirements must be identified, taking into account the business criticality of the concerned system. System tuning and monitoring must be applied to ensure and, where necessary, improve the availability and efficiency of systems.

Detective controls must be put in place to indicate problems in due time. Projections of future capacity requirements must take account of new business and system
requirements and current and projected trends in the MoJ’s information processing capabilities.

The capacity of the human resources, as well as offices and facilities must be addressed.

### Separation of development, testing and operational environments

Development, testing, and operational environments must be separated to reduce the risks of unauthorised access or changes to the operational environment.

The level of separation between operational, testing, and development environments that is necessary to prevent operational problems must be identified and implemented.

## Protection from malware

Ensure that information and information processing facilities are protected against malware.

Protection against malware must be based on malware detection and repair software, information security awareness and appropriate system access and change management controls.

### Controls against malware

Detection, prevention and recovery controls to protect against malware must be implemented, combined with appropriate user awareness.

Malware Protection
Spam and Phishing

## Backup

Protect against loss of data.

Backups Removable Media and Incident Management
System backup

### Information backup

Backup copies of information, software and system images must be taken and tested regularly in accordance with an agreed backup policy.

Adequate backup facilities must be provided to ensure that all essential information and software can be recovered following a disaster or media failure.

Operational procedures must monitor the execution of backups and address failures of scheduled backups to ensure completeness of backups.

Backup arrangements for individual systems and services must be regularly tested to ensure that they meet the requirements of business continuity plans.

## Control of operational software

Ensure the integrity of operational systems.

Using Open Internet Tools
Using 3rd Party Open Source Products

### Installation of software on operational systems

Procedures must be implemented to control the installation of software on operational systems.

## Logging and monitoring

Record events and generate evidence.

Logging
Protective Monitoring
Accounting
Commercial off-the-shelf applications
Custom Applications
Online identifiers in security logging & monitoring
Security Log Collection

### Event logging		

Event logs recording user activities, exceptions, faults and information security events must be produced, kept and regularly reviewed.

Event logs can contain sensitive data and personally identifiable information. Appropriate privacy protection measures must be taken.

Where possible, system administrators must not have permission to erase or de-activate logs of their own activities.

### Protection of log information

Logging facilities and log information must be protected against tampering and unauthorised access.

Some audit logs may be required to be archived as part of the record retention policy or because of requirements to collect and retain evidence.

### Administrator and operator logs

System administrator and system operator activities must be logged and the logs protected and regularly reviewed.

Privileged user account holders may be able to manipulate the logs on information processing facilities under their direct control, therefore it is necessary to protect and review the logs to maintain accountability for the privileged users.

An intrusion detection system managed outside of the control of system and network administrators can be used to monitor system and network administration activities for compliance.

### Clock synchronisation

The clocks of all relevant information processing systems within the MoJ or security domain must be synchronised to a single reference time source.

External and internal requirements for time representation, synchronisation and accuracy must be documented. Such requirements can be legal, regulatory, contractual requirements, standards compliance or requirements for internal monitoring. A standard reference time for use within the MoJ should be defined.

The MoJ's approach to obtaining a reference time from external source(s) and how to synchronise internal clocks reliably must be documented and implemented.

## Control of operational software

Ensure the integrity of operational systems.

### Installation of software on operational systems

Procedures must be implemented to control the installation of software on operational systems. Vendor supplied software used in operational systems should be maintained at a level supported by the supplier. Over time, software vendors will cease to support older versions of software. The MoJ must consider the risks of relying on unsupported software.

Any decision to upgrade to a new release must take into account the business requirements for the change and the security of the release, e.g. the introduction of new information security functionality or the number and severity of information security problems affecting this version. Software patches must be applied when they can help to remove or reduce information security weaknesses.

Physical or logical access must only be given to suppliers for support purposes when necessary and with management approval. The supplier’s activities must be monitored.

Computer software may rely on externally supplied software and modules, which must be monitored and controlled to avoid unauthorised changes, which could introduce security weaknesses.

## Technical vulnerability management

Prevent exploitation of technical vulnerabilities.

### Management of technical vulnerabilities

Information about technical vulnerabilities of information systems being used must be obtained in a timely fashion, the MoJ's exposure to such vulnerabilities evaluated and appropriate measures taken to address the associated risk.

A current and complete inventory of assets is a prerequisite for effective technical vulnerability management. Specific information needed to support technical vulnerability management includes the software vendor, version numbers, current state of deployment (e.g. what software is installed on what systems) and the person(s) within the MoJ responsible for the software.

Appropriate and timely action must be taken in response to the identification of potential technical vulnerabilities.

Technical vulnerability management can be viewed as a sub-function of change management and as such can take advantage of the change management processes and procedures.

### Restrictions on software installation

Rules governing the installation of software by users must be established and implemented.

The MoJ must define and enforce strict policy on which types of software users may install. The principle of least privilege should be applied. If granted certain privileges, users may have the ability to install software. The MoJ must identify what types of software installations are permitted (e.g. updates and security patches to existing software) and what types of installations are prohibited (e.g. software that is only for personal use and software whose pedigree with regard to being
potentially malicious is unknown or suspect). These privileges must be granted having regard to the roles of the users concerned.

Vulnerability Scanning
Patch Management
Configuration Patching and Change
Vulnerability Disclosure

## Information systems audit considerations

Minimise the impact of audit activities on operational systems.

### Information systems audit controls

Audit requirements and activities involving verification of operational systems must be carefully planned and agreed to minimise disruptions to business processes.

## Enforcement

This policy is enforced by lower level policies, standards, procedures and guidance.
Non-conformance with this policy could result in disciplinary action taken in accordance with the department’s Disciplinary procedures. This could result in penalties up to and including dismissal. If an employee commits a criminal offence, s/he may also be prosecuted. In such cases, the department will always cooperate with the relevant authorities, and provide appropriate evidence.

## Contact details

- Contact the Technology Service Desk to report a suspected IT incident: Telephone: 0800 917 5148.
- Contact the MoJ Security Team for further advice and to report other security incidents: [security@justice.gov.uk](mailto:security@justice.gov.uk)
