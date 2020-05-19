---
Expires: 2020-12-31
---

# Privileged User Guide

## Introduction

This guide outlines the security procedures and advice that privileged users should follow to access the MoJ’s IT systems in a safe and secure manner. Privileged users are those who have elevated levels of system access in order to manage IT system components to meet MoJ IT service requirements. Privileged users may install software, configure and upgrade IT systems, input into the Service Management Tool for the systems they manage and run day-to-day operations to satisfy continuity of service, recovery, security and performance needs.

Specific responsibilities of individual privileged users are likely to vary depending on the systems they manage. The system’s Information Risk Assessment Report (IRAR) will document the security controls, some of which the system’s privileged users will run. For a comprehensive list of individual responsibilities, privileged users should refer to the system specific documentation. This page is the first in a series of guides for privileged users within the MoJ.

## Who is this for?

This guide is aimed at two audiences:

1. The in-house MoJ Digital and Technology staff who are responsible for implementing controls throughout technical design, development, system integration and operation. This includes DevOps, Software Developers, Technical Architects and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI and Knowledge (EPICK) Team.

2. Any other MoJ business groups, Agencies, contractors, IT suppliers and partners who in any way design, develop or supply services (including processing, transmitting and storing data) for, or on behalf of the MoJ.

## Related guides
For further details about privileged user responsibilities, see the guides below.

_Logging Guide_: provides information about security procedures privileged users should implement to conduct logging activities.

_Backups, Removable Media and Incident Management Guide_: provides information that privileged users should follow to reduce the impact of and respond to a security incident.

_Configuration, Patching and Change Management Guide_: provides privileged users with guidance to ensure that systems are configured securely, change is managed correctly and systems are patched regularly.


## Management of privileged user accounts

Privileged user accounts have a high degree of risk associated with them due to the control that they give the privileged user, hence they must be treated with great care. To reduce the risk of a data breach on the MoJ systems, access rights must be managed in the following ways.

 - Privileged user accounts should only be created for users with a genuine business need and only for the duration that the business need exists.

 - They should be strictly controlled and their number kept to the absolute minimum per system or app.

 - Privileged user passwords must be created in line with the MoJ’s Password Guide.

 - The password for a privileged user account must not be re-used for another privileged user account or a normal user account.

 - Privileged access must be limited and granted on a ‘need to know’ basis for a specified period.

 - Multi Factor Authentication (MFA) must be used as an additional layer of authentication  for privileged user accounts. See the Password Guide for further details. 

 - Privileged user passwords must be deleted along with the account when a privileged user leaves the MoJ or changes role. 

 - Privileged user accounts must only be used when carrying out administrative tasks such as creating new user accounts or implementing software updates. At all other times a normal user account must be used, e.g. for tasks such as searching the internet and reading emails. 

For further information on managing privileged user accounts see the Configuration, Patching and Change Management Guide.


## Resource monitoring

Where privileged users are responsible for monitoring system resources to ensure that the system is operating effectively and providing their intended function, defined system Key Performance Indicators (KPIs) should be used to monitor systems and ensure they are operating effectively. Privileged users should do this by:

 - monitoring and analysing data from each of the following categories in order to minimise, or prevent, system outages or slowdowns:

  * CPU usage

  * memory consumption

  * input/output operations

  * network usage

  * disk usage

  * system down time

 - identifying the root cause of excessive resource use and rectifying the issue when possible - if an issue cannot be rectified quickly, it should be reported to the system owner

 - notifying the MoJ’s Technology Service Desk if there is a suspected incident (see below for contact details).


## Identification and authentication

Privileged users are responsible for managing user access to systems to enable effective access control to the MoJ’s data and information. To support effective access controls, privileged users must follow the points below. 

 - Only create user accounts once authorisation has been received from that user’s line manager.

 - Only grant permissions that are in line with the user’s business role within the MoJ.

 - Review user account usage every 90 days. If an account is dormant, the privileged user must investigate its status and suspend the account if appropriate. See the Access Control Guide  for details. 

 - Disable all user & privileged user accounts when staff members leave the MoJ or where the account is not required due to a change of role. Privileged users will be automatically notified by HR when access changes or revocations are required. 

 - Retain a record of all authorised users, approvals and changes of access rights and privileges for any network, system or application for which privileged users are responsible. 


## Mobile and home working

When working remotely, it is important that privileged users operate securely by:

 - not conducting administrative tasks (such as creating new user credentials) on untrusted public Wi-Fi networks

 - ensuring that they are not overlooked when working on administrative tasks

 - ensuring that they use the MoJ’s Virtual private Network (VPN) to connect with MoJ systems when using Privileged user login details. 

Access to the VPN requires 2 Factor Authentication (2FA). The IT Security Policy and Remote Working Guidance contain further information about Remote Working. 


## Contact details

 - Contact the Cyber Assistance Team for advice – [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk)

 - Contact the Technology Service Desk to report a suspected incident – 0800 917 5148.




























