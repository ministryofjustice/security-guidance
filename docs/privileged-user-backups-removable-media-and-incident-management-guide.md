# Privileged User Backups, Removable Media and Incident Management Guide

**Parent topic:** [Privileged User Guide](privileged-user-guide.md)

## Introduction

This guide outlines the security procedures and advice for privileged users to reduce the impact of security incidents, and improve the response to them. This guide is a sub-page to the [Privileged User Guide](privileged-user-guide.md).

## Removable media

Whether moving data to the Cloud or accepting data from third parties, removable media increases the risk of malware being introduced to systems, and could result in the loss of critical or sensitive Ministry of Justice \(MoJ\) data. Privileged users play an important role in managing this risk, and must ensure that the following actions are undertaken by individuals using removable media.

-   Any data transferred from removable media to the MoJ systems should be scanned for malware before being uploaded to MoJ systems. One option is to adopt a "sheep dip". This is a segregated system with anti-virus and other security tools. It is used to conduct security scans before data is introduced to the MoJ systems. This reduces, but does not eliminate, the risk that removable media is used as a threat vector for malware.
-   The origin of any removable media must be established to understand the risk it poses.
-   If removable media is required for standard system operations, privileged users must ensure data is encrypted at rest, and has suitable physical security controls in place. These include locking rooms where data is stored or using safes for storing removable media.
-   Removable media must not be used for a system's operation unless it is approved by the Senior Information Risk Officer \(SIRO\). Advice should be sought from a risk advisor in the Cyber Assistance Team, using the [contact details](#incidents-and-contact-details).

## System backups

Privileged users need to ensure that there are backups of system data in order to minimise the impact of incidents, such as malware infection or data loss. Privileged users must:

-   Follow the IT system's data backup schedule to meet the required Recovery Point Objective.
-   Assign all backup media, whether physical or in the Cloud, a Protective Marking, and provide appropriate protection based on that marking. Backup material must only be accessible to those who have a "need-to-know", defined by the System Owner.
-   Ensure backups are kept off-site in a secure location. In a Cloud environment, this would equate to a resilient data store, such as AWS Backup or Azure Backup services.
-   Where required, encryption types employed to prevent disclosure are outlined in the Information Risk Assessment Report \(IRAR\). Details of applicable encryption standards required are outlined in the [Technical Controls Guide](technical-security-controls-guide.md).

Guidance for system specific privileged users:

-   Where responsible for DOM1 systems, ensure backups are made to offsite locations such as to Dell EMC SANs in the MoJ off-site Ark and Ark-F data centres.
-   Where responsible for Quantum systems, ensure backups are made to the redundant data centre.
-   Where responsible for end user data, ensure data is not stored on or backed up to users' end devices but rather stored on OneDrive or Google Drive.

## Incident management and response

Privileged users play a front-line role in detecting and responding to incidents. To ensure that they are prepared to respond to any incidents, privileged users should:

-   Know and be able to implement the incident management plans and processes required for their systems. For instance, within HMPPS, privileged users should know that the HMPPS Incident Management function operates within the HMPPS Infosec and Service Team, and when they are to be contacted.
-   Ensure that any system-specific incident management controls align with the [MoJ's IT Disaster Recovery Policy](it-disaster-recovery-policy.md) and the [Incident Management Policy and Guide](incident-management-plan-and-process-guide.md).

## General enquiries, including theft and loss

**Technology Service Desk** - including DOM1/Quantum, and Digital & Technology Digital Service Desk. Use one of the following two methods for contacting service desk:

-   Tel: 0800 917 5148
-   [MoJ Service Portal](https://mojprod.service-now.com/moj_sp)

**Note:** The previous `itservicedesk@justice.gov.uk` and `servicedesk@digital.justice.gov.uk` email addresses, and the Digital & Technology Digital Service Desk Slack channel \(`#digitalservicedesk`\), are no longer being monitored.

**HMPPS Information & security:**

-   Email: [informationmgmtsecurity@justice.gov.uk](mailto:informationmgmtsecurity@justice.gov.uk)
-   Tel: 0203 334 0324

## Incidents and contact details

**Note:** If you work for an agency or ALB, refer to your local incident reporting guidance.

For help with incidents, including theft and loss, contact:

-   **Technology Service Desk - including DOM1, Quantum, and the Digital & Technology Service Desk**

    Tel: 0800 917 5148

    **Note:** The previous `itservicedesk@justice.gov.uk` and `servicedesk@digital.justice.gov.uk` email addresses are no longer being monitored.

-   **HMPPS Information and security**
    -   Email: [informationmgmtsecurity@justice.gov.uk](mailto:informationmgmtsecurity@justice.gov.uk)
    -   Tel: 0203 334 0324

For non-technology incidents, contact the MoJ Group Security Team: [mojgroupsecurity@justice.gov.uk](mailto:mojgroupsecurity@justice.gov.uk)

Contact the Privacy Team for information on Data Protection Impact Assessments: [privacy@justice.gov.uk](mailto:privacy@justice.gov.uk)

If you are not sure who to contact, ask the Operational Security Team:

-   Email: [OperationalSecurityTeam@justice.gov.uk](mailto:OperationalSecurityTeam@justice.gov.uk)
-   Slack: `#security`

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for security advice, contact the Cyber Assistance Team [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

