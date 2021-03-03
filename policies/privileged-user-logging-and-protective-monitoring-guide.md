---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](home-security-policies-guides.md)

# Privileged User Logging and Protective Monitoring Guide

## Introduction

This guide outlines the security procedures and advice that privileged users must consider when undertaking logging activities. Maintaining and monitoring system logs will help to ensure that suspicious activity on the MoJ's systems is detected early. This guide is a sub-page to the [Privileged User Guide](privileged-user-guide.md).

## Maintenance of system logs and protective monitoring

Privileged users are responsible for maintaining system logs (syslogs) for the systems they administer. Privileged user log management responsibilities include the following:

- Implementing logging and monitoring on the systems they manage.
- Performing regular maintenance of the logs and logging to ensure that configurations are correct.
- Reconfiguring system logging as needed based on the MoJ's policy or guidance changes, technology changes, emerging threats or other business needs.
- Implementing automated real-time log analysis where possible.
- Reviewing results from automated real-time analysis quarterly to ensure its relevance.
- Where real-time log analysis has not been implemented, then manual log analysis must be performed at least weekly.
- Working closely with the Operational Security Team (OST) to define requirements and ensure that when possible, automated log analysis and alerting is integrated with the MoJ's Security Operations Centre (SOC) which provides the MoJ's central monitoring function.
- Establishing the baseline activities for systems they are responsible for. This is essential to ensure that monitoring systems are able to detect when there is unusual activity.
- Ensuring that systems are synchronised to the centralised MoJ timing source to enable effective malware detection.
- Ensuring that audits and compliance checks of IT systems do not adversely affect business operations.
- Documenting and reporting anomalies in log settings, configurations, and processes to the OST and the Cyber Assistance Team (contact details below).
- Managing long-term storage of system log data, monitoring log rotation, and the archival and deletion of log data.
- Any suspicious activity must be reported to the Technology Service Desk (contact details below) who may escalate it to the OST.  See further details in the IT Incident Management Policy and Guide.

## Protection of log data

To ensure that there is an audit trail for log data, privileged users must:

- protect the information held within system audit logs in accordance with its Information Classification (refer to the [Information Classification Handling and Security Guide](information-classification-handling-and-security-guide.md) for further guidance on classifying information)
- establish log archival processes while filtering out entries that do not need to be archived to ensure log availability
- ensure that systems are designed with access controls to prevent privileged users from erasing or deactivating activity logs of their own activities, without the additional approval of the product or service manager
- review the activity logs of other privileged users on a monthly basis to ensure that privileged users remain impartial.

## Contact details

- Contact the Technology Service Desk to report a suspected incident: 0800 917 5148.
- Contact the MoJ Security Team for further advice and to report other security incidents: [Security@justice.gov.uk](mailto:Security@justice.gov.uk)
