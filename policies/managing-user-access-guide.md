---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](home-security-policies-guides.md)

# Managing User Access Guide

## Introduction

This guide provides information on the authentication methods which should be used to manage user access to systems and information in the MoJ. This is a sub-page to the Access Control Guide.

## Managing access to MoJ systems

The following methods can be used to manage access to the MoJ’s systems. They are in order of preference for their use, with 1 providing more secure management features than 4.

| | Method | Comment |
| --- | --- | --- |
| 1 | Application Program Interface (API) | Where possible, APIs should be used instead of Secure Shell (SSH) as APIs offer greater technical control over security systems without the need for parsing commands required by SSH. For AWS instances, it is recommended that you use AWS Session Manager. |
| 2 | Automated diagnostic data collection | It should be considered the exception for administrators to directly administer a server/node when there is automated diagnostic data collection. Diagnostic data collection allows the underlying technical data to be easily correlated and analysed. |
| 3 | Pre-defined, pre-audited | Authentication tools such as Amazon Identity Access Management (IAM) should be used to manage access when technically possible. The use of pre-defined tools for authentication can be designed to avoid human error and instruct pre-audited actions to be taken on an administrator’s behalf, thus reducing manual human interaction. |
| 4 | Secure Shell (SSH) | If you cannot use APIs, such as Session Manager for AWS, then SSH can be used with the following controls.
| | | Use of bastion or ‘jump’ boxes for access into systems is a useful technical security design that also helps ‘choke’ and control sessions. |
| | | The need to use SSH to interact with a server/node can be reduced through improved infrastructure and server design. For instance, the use of stateless cluster expansion/contraction and the automated diagnostic data capture can reduce the need to use SSH. |
| | | System Admins should only login to a server/node via SSH and execute commands with elevated privileges (typically, root) under exceptional circumstances.
| | | - SSH must be strictly controlled and environments should be segregated so that no single bastion or ‘jump’ SSH server can access both production and non-production accounts. |
| | | - Do not allow direct logging in as root through SSH, administrators must have a separate account that they regularly use and simply sudo to root when necessary. |
| | | - SSHs must be limited to users who need shell (by comparison to users who will use SSH as a port forwarding tunnel). |
| | | - Joiners/Movers/Leavers processes must be strictly enforced (optimally and preferably automated) on SSH servers as they are a critical and privileged access method. |
| | | - SSH should not be password-based, and should use individually created and purposed SSH key pairs. Private keys must not be shared or re-used. |

The Government Digital Service (GDS) recommends the use of the open authorisation standard ‘OAuth2’ as a means to authenticate users. See the GDS guide for more information.

Contact details

Contact the Cyber Assistance Team for advice – [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk)
