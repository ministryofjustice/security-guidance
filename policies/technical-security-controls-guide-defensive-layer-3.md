---
Review: 2020-12-31
Owner: CISO
Target audience:
---

# Technical Controls Guide: Defensive Layer 3

This guide is a sub-page to the Technical Controls Guide.

## Defensive layer 2: implementing monitoring and maintenance tools

The table below outlines key guidance notes for the security controls that should be implemented at Layer 3. These controls should be implemented **after** Layer 1 and Layer 2 have been successfully completed.


| Do |
|--- |
| ✔ Implement concurrent session control which is defined by:
| - account type (e.g. privileged and non-privileged users, domain, application)      
| - account role (e.g. system admins, critical domains/applications)
| - a combination of both. |
| ✔ Enforce session lock controls with pattern-hiding displays. For example:
| - patterns used with screen savers
| - photographic images     
| - solid colo\rs      
| - clock
| - battery life indicator. |
| ✔ Implement maintenance tools. For example:
| - hardware/software diagnostic test equipment      
| - hardware/software packet sniffers   
| - software tools to discover improper or unauthorised tool modification. |

The table below outlines the actions that should **not** be implemented when adopting Layer 3 security controls.

| Don't |
|---|
| ✖ Do not allow users to publish confidential information related to the MoJ on publicly available systems. To support this control, you should request the support of a third party to review the content on publicly accessible systems and remove any non-public information that is shared. |
| ✖ Do not allow unauthorised removal of maintenance equipment, for example, backup disks and power supplies. |
| ✖ Do not decommission maintenance equipment without appropriate security controls, for example:
| - verifying that there is no organisational information contained on the equipment     
| - sanitising the equipment
| - retaining the equipment within the facility. |

## Further Guidance

For further information please refer to:
* [Gov.uk Technology Code of Practice](https://www.gov.uk/government/publications/technology-code-of-practice/technology-code-of-practice)
* [NIST 800-53](https://nvd.nist.gov/800-53)
* [NCSC Advice and Guidance](https://www.ncsc.gov.uk/section/advice-guidance/all-topics)
