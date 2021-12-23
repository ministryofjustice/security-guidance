# Privileged User Logging and Protective Monitoring Guide

**Parent topic:** [Privileged User Guide](privileged-user-guide.md)

**Related information**  


[Logging and monitoring](logging-and-monitoring.md)

## Introduction

This guide outlines the security procedures and advice that privileged users must consider when undertaking logging activities. Maintaining and monitoring system logs will help to ensure that any suspicious activity on the Ministry of Justice \(MoJ\)'s systems is detected early. This guide is a sub-page to the [Privileged User Guide](privileged-user-guide.md).

## Maintenance of system logs and protective monitoring

Privileged users are responsible for maintaining system logs \(syslogs\) for the systems they administer. Privileged user log management responsibilities include the following:

-   Implementing logging and monitoring on the systems they manage.
-   Performing regular maintenance of the logs and logging to ensure that configurations are correct.
-   Reconfiguring system logging as needed based on the MoJ's policy or guidance changes, technology changes, emerging threats or other business needs.
-   Implementing automated real-time log analysis where possible.
-   Reviewing results from automated real-time analysis quarterly to ensure its relevance.
-   Where real-time log analysis has not been implemented, then manual log analysis must be performed at least weekly.
-   Working closely with the Operational Security Team \(OST\) to define requirements and ensure that when possible, automated log analysis and alerting is integrated with the MoJ's Security Operations Centre \(SOC\) which provides the MoJ's central monitoring function.
-   Establishing the baseline activities for systems they are responsible for. This is essential to ensure that monitoring systems are able to detect when there is unusual activity.
-   Ensuring that systems are synchronised to the centralised MoJ timing source, to enable effective malware detection.
-   Ensuring that audits and compliance checks of IT systems do not adversely affect business operations.
-   Documenting and reporting anomalies in log settings, configurations, and processes to the OST \([contact details](#incidents-and-contact-details)\) and the Cyber Assistance Team \([contact details](#incidents-and-contact-details)\).
-   Managing long-term storage of system log data, monitoring log rotation, and the archival and deletion of log data.
-   Any suspicious activity must be [reported](#incidents-and-contact-details). Refer to the details in the [IT Incident Management Policy](it-incident-management-policy.md).

## Protection of log data

To ensure that there is an audit trail for log data, privileged users must:

-   Protect the information held within system audit logs in accordance with its Information Classification. Refer to the [Information Classification Handling and Security Guide](information-classification-handling-and-security-guide.md) for further guidance on classifying information.
-   Establish log archival processes while filtering out entries that do not need to be archived to ensure log availability.
-   Ensure that systems are designed with access controls, to prevent privileged users from erasing or deactivating activity logs of their own activities, without the additional approval of the product or service manager.
-   Review the activity logs of other privileged users on a monthly basis, to ensure that privileged users remain impartial.

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

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for cyber security advice, contact the Cyber Assistance Team [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

