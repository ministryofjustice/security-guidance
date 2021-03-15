---
Review: 2021-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](home-security-policies-guides.md)

# Privileged User - Backups, Removable Media and Incident Management Guide

## Introduction

This guide outlines the security procedures and advice for privileged users to reduce the impact of security incidents and improve the response to them. This guide is a sub-page to the [Privileged User Guide](privileged-user-guide.md).

## Removable media

Whether moving data to the Cloud or accepting data from third parties, removable media increases the risk of malware being introduced to systems and could result in the loss of critical or sensitive MoJ data. Privileged users play an important role in managing this risk and must follow the points below.

- Any data transferred from removable media to the MoJ systems should be scanned for malware before being uploaded to MoJ systems. One option is to adopt a sheep dip, a segregated system with anti-virus, which can be used to conduct these scans before data is introduced to the MoJ systems. This reduces, but does note eliminate, the risk that removable media is used as a threat vector for malware.  
- The origin of any removable media must be established to understand the risk it poses.
- If removable media is required for standard system operations, privileged users must ensure data is encrypted at rest and has suitable physical security controls in place. These include locking rooms where data is stored or using safes for storing removable media. See the [Information and Data Security Policy](information-and-data-security-policy.md) for further information.
- Removable media must not be used for a system's operation unless it is approved by the Senior Information Risk Officer (SIRO); advice should be sought from a risk advisor in the Cyber Assistance Team, contact details given below.

## System backups

Privileged users need to ensure that there are backups of system data in order to minimise the impact of incidents such as malware infection or data loss. Privileged users must:

- follow the IT system's data backup schedule to meet the required Recovery Point Objective.
- assign all backup media, whether physical or in the Cloud, a Protective Marking and provide appropriate protection based on that marking. Backup material must only be accessible to those who have a 'need-to-know', defined by the System Owner.
- ensure backups are kept off-site in a secure location.  In a Cloud environment, this would equate to a resilient data store, such as AWS Backup or Azure Backup services.
- where required, encryption types employed to prevent disclosure are outlined in the Information Risk Assessment Report (IRAR). Details of applicable encryption standards required are outlined in the [Technical Controls Guide](https://ministryofjustice.github.io/security-guidance/technical-security-controls-guide/#technical-security-controls-guide).

Guidance for system specific privileged users:
- where responsible for DOM1 systems, ensure backups are made to offsite locations such as to Dell EMC SANs in the MoJ off-site Ark and Ark-F data centres.
- where responsible for Quantum systems, ensure backups are made to the redundant data centre.
- where responsible for end user data, ensure data is not stored on or backed up to users' end devices but rather stored on OneDrive or Google Drive.

## Incident management & response

Privileged users play a front-line role in detecting and responding to incidents. To ensure that they are prepared to respond to any incidents, privileged users must follow the points below.

- If privileged users identify a suspected or known security breach through their regular system monitoring they must report it immediately to the System Manager, the Risk Advisor (part of the Cyber Assistance Team) and the MoJ's Technology Service Desk for any incidents involving technology. Incidents will then be escalated to the Operational Security Team (OST). For non-technology incidents, where security issues not related to IT have been identified, contact the MoJ Group Security Team, contact information given below. Security breaches can include personnel, hardware, software, communications, data and information or physical security breaches. See the [Incident Management Policy and Guide](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/incident-management-plan-and-process-guide/) for further details.
- Privileged users must know and be able to implement the incident management plans and processes required for their systems. For instance, within HMPPS, privileged users should know that the HMPPS Incident Management function operates within the HMPPS Infosec and Service Team and when they are to be contacted.
- Any system-specific incident management controls must align with the [MoJ's IT Disaster Recovery Policy](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/it-disaster-recovery-policy/) and the [Incident Management Policy and Guide](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/incident-management-plan-and-process-guide/).

## Contact details

- Contact the Technology Service Desk to report a suspected IT incident: Telephone: 0800 917 5148.
- Contact the MoJ Security Team for further advice and to report other security incidents: [Security@justice.gov.uk](mailto:Security@justice.gov.uk)
- Contact the MoJ Group Security Team to report non-technology incidents - [mailto:mojgroupsecurity@justice.gov.uk](mojgroupsecurity@justice.gov.uk)
