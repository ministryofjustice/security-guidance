---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](../..)

# Technical Controls Guide: Defensive Layer 2

This guide is a sub-page to the [Technical Controls Guide](../technical-security-controls-guide/).

## Defensive layer 2: implementing monitoring capabilities

The table below identifies the security controls that should be implemented to mature existing Layer 1 controls and enable the capability of active monitoring of the MoJ network.

<table>
<tr><th>Do</th></tr>
<tr><td>✔ Monitor login attempts and block access after 10 unsuccessful attempts.</td></tr>
<tr><td>✔ Implement session timeouts and block accounts after a defined period of inactivity, for example, 5 minutes.</td></tr>
<tr><td>✔ Implement a mobile device management solution to enable the wiping of mobile devices where access to the device has been lost or unauthorised access identified, for example, in the event of:
<ul>
<li>an identified data breach</li>
<li>an identified policy breach such as jailbreaking a device</li>
<li>a lost device, and/or</li>
<li>the end of an employment contract, for example, for an employee, contractor or other staff.</li></ul></td></tr>
<tr><td>✔ Use automation tools for easy search and retrieval of information, for example, AI machine-based learning for keyword searching.</td></tr>
<tr><td>✔ Terminate network connections associated with communication sessions. For example the de-allocation of:
<ul>
<li>associated TCP/IP address pairs, and</li>
<li>network assignments at the application level.</li></ul></td></tr>
<tr><td>✔ Control the development and use of mobile code, whether developed in-house or through acquisitions.</td></tr>
<tr><td>✔ Implement spam protection tools, which have the capability to:
<ul>
<li>monitor system entry and exit points such as mail servers, web servers, proxy servers, workstations and mobile devices</li>
<li>incorporate signature-based detection</li>
<li>implement filters for continuous learning.</li></ul></td></tr>
<tr><td>✔ Use error handling techniques, such as pop-up messages, which provide information necessary for corrective actions without revealing data that can be exploited by threat actors.</td></tr>
</table>

The table below sets out the guidance for what actions should **not** be undertaken when implementing Layer 2 security controls.

<table>
<tr><th>Don't</th></tr>
<tr><td>✖ You should not allow general users to make configuration changes to software, firmware and hardware.</td></tr>
<tr><td>✖ You should not allow connections between internal and external systems without carrying out security checks.</td></tr>
<tr><td>✖ You should not allow the use of open source software, including commercial off-the-shelf tools, unless approved by the MoJ. Contact the Cyber Assistance Team (CAT) for advice at <a href="mailto:CyberConsultancy@digital.justice.gov.uk">CyberConsultancy@digital.justice.gov.uk</a>.</td></tr>
<tr><td>✖ You should not allow general users to execute code on their mobile devices. Your devices should be able to:
<ul>
<li>identify malicious code</li>
<li>prevent downloading and execution</li>
<li>prevent automatic execution, and</li>
<li>allow execution only in secured and segregated environments.</li></ul></td></tr>
<tr><td>✖ You should not reveal error messages to anyone outside of the MoJ-defined personnel and roles.</td></tr>
</table>
