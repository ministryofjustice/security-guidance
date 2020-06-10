---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](../..))

# Privileged User Backups, Removable Media and Incident Management Guide

## Introduction

This guide outlines the security procedures and advice for privileged users to reduce the impact of security incidents and improve the response to them. This guide is a sub-page to the [Privileged User Guide](../privileged-user-guide/).

## Removable media

Removable media increases the risk of malware being introduced to systems and could result in the loss of critical/sensitive MoJ data. Privileged users play an important role in managing this risk and must follow the points below.

- Any data transferred from removable media to the MoJ systems should be scanned for malware before being uploaded to MoJ systems. One option is to adopt a sheep dip, a segregated terminal with anti-virus, which can be used to conduct these scans before data is introduced to the MoJ systems. This reduces the risk that removable media is used as a threat vector for malware.
- The origin of any removable media must be established to understand the risk it poses.
- If removable media is required for standard system operations, privileged users must ensure data is encrypted at rest and has suitable physical security controls in place. These include locking rooms where data is stored or using safes for storing removable media. See the [Information and Data Security Policy](../information-and-data-security-policy/) for further information.
- Removable media must not be used for a system operation unless it is approved by the Senior Information Risk Officer (SIRO); advice should be sought from the Risk Advisor Team.

## System backups

Privileged users need to ensure that there are frequent backups of system data in order to minimise the impact of incidents such as malware infection or data loss. Privileged users must:

- follow the IT system's data backup schedule to meet the required Recovery Point Objective
- ensure that DOM1 backups are made to Dell EMC SAN in the MoJ off-site Ark and Ark-F data centres.
- ensure that Quantum backups are made to the redundant data centre
- ensure user data is backed up to OneDrive in line with Microsoft's Service Level Agreement
- assign all backup media a Protective Marking and provide appropriate protection based on that marking. Backup material must only be accessible to those who have a 'need-to-know', defined by the System Owner.
- ensure that backups are encrypted to prevent disclosure. Encryption types employed are outlined in the IRAR. Details of applicable encryption standards required are outlined in the Technical Controls Guide.
- ensure backups are kept off-site in a secure location.

## Incident management & response

Privileged users play a front-line role in detecting and responding to incidents. To ensure that they are prepared to respond to any incidents, privileged users must follow the points below.

- If privileged users identify a suspected or known security breach through their regular system monitoring they must report it immediately to the System Manager, the Risk Advisor and the MoJ's Technology Service Desk for any incidents involving technology. Incidents will then be escalated to the Operational Security Team (OST). For non-technology incidents contact the MoJ Security Team at [mojgroupsecurity@justice.gov.uk](mailto:mojgroupsecurity@justice.gov.uk). Security breaches can include personnel, hardware, software, communications, data and information or physical security breaches. See the Incident Management Policy and Guide for further details.
- Privileged users must know and be able to implement the incident management plans and processes required for their systems. For instance, within HMPPS, privileged users should know that the HMPPS Incident Management function operates within the HMPPS Infosec and Service Team and when they are to be contacted.
- Any system-specific incident management controls must align with the [MoJ's IT Disaster Recovery Policy](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/it-disaster-recovery-policy/) and the Incident Management Policy and Guide.

## Contact details

 - Contact the Cyber Assistance Team for advice: [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk)

 - Contact the Technology Service Desk to report a suspected incident: 0800 917 5148.

 - Contact the MoJ Security Team to report non-technology incidents - [mailto:mojgroupsecurity@justice.gov.uk](mojgroupsecurity@justice.gov.uk)
