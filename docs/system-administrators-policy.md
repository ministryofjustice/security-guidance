# System administrators policy

This document is intended to help System Administrators use and access Ministry of Justice \(MoJ\) systems in a safe and secure manner.

To help identify formal policy statements, each is prefixed with an identifier of the form: `POLSYADxxx`, where xxx is a unique ID number.

## Overview

This policy applies to all system administrators working with MoJ systems.

All MoJ system administrators **SHALL** follow this policy.

System administrators **SHALL** also be compliant with the System Operating Procedures \(SyOps\) that apply for a given system they administer.

System Administrators **SHALL** read this document prior to using an MoJ system for the first time.

System Administrators **SHOULD** revisit this document every six \(6\) months or so, to remind themselves of the content. Audits will check that the policy is being followed.

System Administrators are responsible for maintaining the security of MoJ systems. Failure to comply with this policy or the system SyOPs could lead to compromise of the MoJ's infrastructure, or the services it uses or connects to. Failure to comply with this policy or corresponding SyOPs would be considered a breach of the [IT Security Policy](it-security-policy-overview.md).

For any security related information or help, [get in contact](#contact-details).

## Physical security and environmental controls

-   Routine physical checks of server room **SHALL** be performed to identify unknown equipment and evidence of tampering.
-   A hardware asset register **SHALL** be kept and maintained by the system administrator to assist in equipment monitoring.
-   Any evidence of tampering **SHALL** be immediately reported to the MoJ Operational Security Team \(OST\): [OperationalSecurityTeam@justice.gov.uk](mailto:OperationalSecurityTeam@justice.gov.uk).
-   System administrator **SHALL** ensure an appropriate environment to protect system hardware, for example through air conditioning or dust prevention sheets.
-   Access to a server room **SHALL** be logged and monitored.
-   If an electronic monitoring system is not in place \(such as key card entry\), then a manual log of sever room activity **SHALL** be taken.

## Identification and authentication

-   Accounts **SHALL** only be created when correct authorisation has been received.
-   Permissions granted to accounts **SHALL** be commensurate to the account's business role.
-   Accounts **SHOULD** be enabled only when there is confirmation that a user understands and will comply with the system SyOps.
-   Account usage **SHOULD** be reviewed on regular intervals.
-   If an account is dormant, the System Administrator **SHALL** investigate its status, and disable the account if appropriate.
-   When staff members leave the organisation or where the account is not required, the corresponding accounts **SHALL** be disabled.
-   Administrator level accounts **SHALL** only be used when carrying out administrative tasks.
-   For all non-administrative tasks, a normal \(non-privileged\) User account **SHALL** be used.

## Change management

-   All changes to an MoJ Systems **SHALL** be approved and tested prior to implementation on the live system \(e.g. in a Non-Live Environment\).
-   System Administrators **SHALL** maintain an audit log of configuration changes and ensure that changes do not affect the secure operation of the IT system.
-   Changes **SHALL NOT** be implemented unless the corresponding Operational Change Request \(OCR\) has been approved by [IT Security](#contact-details).
-   Any change which affect the security posture or risk profile of the system **SHALL** be [reported](#contact-details).

## Patch management

-   All system software **SHALL** be kept patched and up-to-date in accordance with the MoJ [Patch Management Guide](patch-management-guide.md).
-   If one exists, a security patch **SHALL** first be tested in the non-live test environment.
-   The system administrator **SHALL**:
    -   Verifying the origin and authenticity of the patch.
    -   Checking the patch and its source media for viruses or malware.
    -   Confirming the base environment required to apply the patch.
    -   Finding out if there are common problems with applying the new patch of software.
-   Un-patched system software **SHALL** be identified and reported to the MoJ OST: [OperationalSecurityTeam@justice.gov.uk](mailto:OperationalSecurityTeam@justice.gov.uk).
-   Problems discovered in patch testing **SHOULD** be documented and reported to the MoJ Chief Information Security Officer \(CISO\) and system owner.

## Audit and protective monitoring

-   Audit logs collected as part of the IT System's protective monitoring solution **SHALL** be monitored by the System Administrator.
-   General audit checking **SHALL** occur at regular intervals \(set by the system owner\).
-   All suspicious activity **SHALL** be monitored and investigated thoroughly.
-   System Administrators **SHALL** ensure that audit and compliance checks do not adversely affect the business operation of the IT System.
-   It is the System Administrator's **SHALL** protect audit logs in accordance with the Protective Marking of the system.

## Passwords

-   Administrator passwords **SHALL** be created in line with the MoJ [Password Management Guide](password-management-guide.md).
-   The password for an Administrator account **SHALL NOT** be re-used with another Administrator or Normal User account.

## Backups

-   System Administrators **SHALL** follow the IT System's back up schedule and procedures.
-   All back up media **SHALL** be assigned a Protective Marking and afforded appropriate protection based on that marking.
-   Back-up material **SHALL** only be accessible to those who have a need-to-know. Encryption might be required to maintain an acceptable level of system assurance.

## Incident management and response

-   Any incident involving a suspected or known security breach involving personnel, hardware, software, communications, document, or physical security **SHALL** be reported immediately to the System Administrator's System Manager, **AND** the MoJ Operational Security Team \(OST\): [OperationalSecurityTeam@justice.gov.uk](mailto:OperationalSecurityTeam@justice.gov.uk).
-   Any loss of IT equipment, MoJ or personal data **SHALL** be reported to:
    -   The System Administrator's line manager.
    -   The MoJ OST \([OperationalSecurityTeam@justice.gov.uk](mailto:OperationalSecurityTeam@justice.gov.uk)\).
    -   The Data Access and Compliance Unit \(DACU\): [Data.access@justice.gov.uk](mailto:Data.access@justice.gov.uk).
-   To ensure a quick response, all emails reporting a loss **SHALL** be marked “Urgent” **AND** have “Data Incident” in the title/subject heading.

## Contact details

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for security advice, contact the Cyber Assistance Team [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

