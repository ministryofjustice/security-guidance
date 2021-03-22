# Privileged User Configuration, Patching and Change Management Guide

**Parent topic:**[Privileged User Guide](privileged-user-guide.md)

## Introduction

This guide outlines the security procedures and controls privileged users should look to implement in order to ensure that systems are configured securely, change is managed correctly. and systems are regularly patched. The goal is to provide guidance for both physical environments, such as Dom1 and Quantum, as well as the Cloud estates in AWS, Azure and Google Cloud. This guide is a sub-page to the [Privileged User Guide](privileged-user-guide.md).

## Secure configuration and change management

Privileged users must ensure that secure configuration and change management processes are followed so that any changes to system operating procedures are understood and support the Ministry of Justice \(MoJ\)'s risk management and mitigation activities. Privileged users must implement the following controls.

-   Approve and test all changes to IT Systems, in a non-live environment, before they are implemented on the live system.
-   For digital products developed by the MoJ's in-house teams, development and hence testing should be conducted iteratively, and changes captured.
-   Maintain an audit log of configuration changes, and ensure that changes do not affect the secure operation of the IT system.
-   If you are working on an in-house developed product or service, configuration changes along with the approval workflow must be recorded in a Service Management Tool, which for many teams is Jira or Trello.
-   If you are working on a system provided by a Managed Service Provider \(MSP\), changes must be input into the Configuration Management Database \(CMDB\). In some cases, these CMDBs will be held by the MSP, but with access rights to the MoJ, or they can be provided through ServiceNow.
-   If you are working on a system provided by an MSP, do not implement changes that deviate from the standard build unless the corresponding Operational Change Request \(OCR\) has been approved by each approver in the Change Management workflow. Once all approvals are complete, the change can be implemented. Further information can be found in the [Vulnerability Scanning and Patch Management Guide](vulnerability-scanning-and-patch-management-guide.md).
-   Report any changes that affect the security posture or risk profile of a system to the [Cyber Assistance Team](#contact-details), and specifically to the business area Risk Advisor before they are implemented.
-   Ensure that operating systems are fully supported by the relevant platform vendor or an MoJ service team. If the system is not supported, consult with the system owner and the [Cyber Assistance Team](#contact-details) for advice. A lack of ongoing support might create security risks within the system and the wider MoJ networks.
-   Privileged users must have the correct management authorisation to make changes to operational software, applications, and program libraries.
-   Documentary evidence must be maintained to catalogue all changes \(including configuration changes\) to IT systems, and the IT security implications of those changes. This includes the case where no significant IT security impacts are identified.

## Incidents

**Note:** If you work for an agency or ALB, refer to your local incident reporting guidance.

**Operational Security Team**

-   Email: [OperationalSecurityTeam@justice.gov.uk](mailto:OperationalSecurityTeam@justice.gov.uk)
-   Slack: `#security`

## General enquiries, including theft and loss

**Dom1/Quantum - Technology Service Desk**

-   Tel: 0800 917 5148

**Note:** The previous `itservicedesk@justice.gov.uk` email address is no longer being monitored.

**Digital & Technology - Digital Service Desk**

-   Email: [servicedesk@digital.justice.gov.uk](mailto:servicedesk@digital.justice.gov.uk)
-   Slack: `#digitalservicedesk`

**HMPPS Information & security:**

-   Email: [informationmgmtsecurity@justice.gov.uk](mailto:informationmgmtsecurity@justice.gov.uk)
-   Tel: 0203 334 0324

## Contact details

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for security advice, contact the Cyber Assistance Team [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

