---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](../..)

# Technical Controls Guide: Defensive Layer 3

This guide is a sub-page to the [Technical Controls Guide](../technical-security-controls-guide/).

## Defensive layer 2: implementing monitoring and maintenance tools

The table below outlines key guidance notes for the security controls that should be implemented at Layer 3. These controls should be implemented **after** Layer 1 and Layer 2 have been successfully completed.

<table>
<tr><th>Do</th></tr>
<tr><td>✔ Implement concurrent session control which is defined by:
<ul>
<li>account type (e.g. privileged and non-privileged users, domain, application)</li>
<li>account role (e.g. system admins, critical domains/applications)</li>
<li>a combination of both.</li></ul></td></tr>
<tr><td>✔ Enforce session lock controls with pattern-hiding displays. For example:
<ul>
<li>patterns used with screen savers</li>
<li>photographic images</li>
<li>solid colours</li>
<li>clock</li>
<li>battery life indicator.</li></ul></td></tr>
<tr><td>✔ Implement maintenance tools. For example:
<ul>
<li>hardware/software diagnostic test equipment</li>
<li>hardware/software packet sniffers</li>
<li>software tools to discover improper or unauthorised tool modification.</li></ul></td></tr>
</table>

The table below outlines the actions that should **not** be implemented when adopting Layer 3 security controls.

<table>
<tr><th>Don't</th></tr>
<tr><td>✖ Do not allow users to publish confidential information related to the MoJ on publicly available systems. To support this control, you should request the support of a third party to review the content on publicly accessible systems and remove any non-public information that is shared.</td></tr>
<tr><td>✖ Do not allow unauthorised removal of maintenance equipment, for example, backup disks and power supplies.</td></tr>
<tr><td>✖ Do not decommission maintenance equipment without appropriate security controls, for example:
<ul>
<li>verifying that there is no organisational information contained on the equipment</li>
<li>sanitising the equipment</li>
<li>retaining the equipment within the facility.</li></ul></td></tr>
</table>

## Further Guidance

For further information please refer to:
* [Gov.uk Technology Code of Practice](https://www.gov.uk/government/publications/technology-code-of-practice/technology-code-of-practice)
* [NIST 800-53](https://nvd.nist.gov/800-53)
* [NCSC Advice and Guidance](https://www.ncsc.gov.uk/section/advice-guidance/all-topics)
