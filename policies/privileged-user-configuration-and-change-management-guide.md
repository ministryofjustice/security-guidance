---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](home-security-policies-guides.md)

# Privileged User Configuration, Patching and Change Management Guide

## Introduction

This guide outlines the security procedures and controls privileged users should look to implement in order to ensure that systems are configured securely, change is managed correctly and systems are regularly patched. The goal is to provide guidance for both physical environments such as Dom1 and Quantum as well as the Cloud estates in AWS, Azure and Google Cloud.  This guide is a sub-page to the [Privileged User Guide](../privileged-user-guide).

## Secure configuration and change management

Privileged users must ensure that secure configuration and change management processes are followed so that any changes to system operating procedures are understood and support the MoJ's risk management and mitigation activities. Privileged users must implement the following controls.

- Approve and test all changes to IT Systems, in a non-live environment, before they are implemented on the live system.
- For digital products developed by the MoJ's in-house teams, development and hence testing should be conducted iteratively and changes captured.
- Maintain an audit log of configuration changes and ensure that changes do not affect the secure operation of the IT system.
- If you are working on an in-house developed product or service, configuration changes along with the approval workflow must be recorded in a Service Management Tool which for many teams is Jira or Trello.
- If you are working on a system provided by a Managed Service Provider (MSP) changes must be input into the Configuration Management Database (CMDB).  In some cases these CMDBs will be held by the MSP but with access rights to the MoJ or they can be provided through ServiceNow.
- If you are working on a system provided by an MSP do not implement changes that deviate from the standard build unless the corresponding Operational Change Request (OCR) has been approved by each approver in the Change Management workflow. Once all approvals are complete the change can be implemented. Further information can be found in the [Vulnerability Scanning and Patch Management Guide](vulnerability-scanning-and-patch-management-guide.md).
- Report any changes that affect the security posture or risk profile of a system to the Cyber Assistance Team, and specifically to the business area Risk Advisor before they are implemented.
- Ensure that operating systems are fully supported by the relevant platform vendor or a MoJ service team. If the system is not supported, consult with the system owner and the Cyber Assistance Team for advice. A lack of ongoing support may create security risks within the system and the wider MoJ networks.
- Privileged users must have the correct management authorisation to make changes to operational software, applications and programme libraries.
- Documentary evidence must be maintained to catalogue all changes (including configuration changes) to IT systems and the IT security implications of those changes (this includes the case where no significant IT security impacts are identified).

## Contact details

- Contact the Cyber Assistance Team for advice: [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk)
- Contact the Technology Service Desk to report a suspected incident: 0800 917 5148.