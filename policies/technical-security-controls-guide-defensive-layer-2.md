---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](home-security-policies-guides.md)

# Technical Controls Guide: Defensive Layer 2

This guide is a sub-page to the Technical Controls Guide.

## Defensive layer 2: implementing monitoring capabilities

The table below identifies the security controls that should be implemented to mature existing Layer 1 controls and enable the capability of active monitoring of the MoJ network.


| Do |
|--- |
| ✔ Monitor login attempts and block access after 10 unsuccessful attempts. |
| ✔ Implement session timeouts and block accounts after a defined period of inactivity, for example, 5 minutes. |
| ✔ Implement a mobile device management solution to enable the wiping of mobile devices where access to the device has been lost or unauthorised access identified, for example, in the event of: |
| an identified data breach   
| an identified policy breach such as jailbreaking a device  
| a lost device, and/or
| the end of an employment contract, for example, for an employee, contractor or other staff. |
| ✔ Use automation tools for easy search and retrieval of information, for example, AI machine-based learning for keyword searching.
| ✔ Terminate network connections associated with communication sessions. For example the de-allocation of: |
| - associated TCP/IP address pairs, and
| - network assignments at the application level. |
| ✔ Control the development and use of mobile code, whether developed in-house or through acquisitions. |
| ✔ Implement spam protection tools, which have the capability to: |
| - monitor system entry and exit points such as mail servers, web servers, proxy servers, workstations and mobile devices     
| - incorporate signature-based detection
| - implement filters for continuous learning. |
| ✔ Use error handling techniques, such as pop-up messages, which provide information necessary for corrective actions without revealing data that can be exploited by threat actors. |


The table below sets out the guidance for what actions should **not** be undertaken when implementing Layer 2 security controls.

| Don't |
|---|
| ✖ You should not allow general users to make configuration changes to software, firmware and hardware.
| ✖ You should not allow connections between internal and external systems without carrying out security checks.
| ✖ You should not allow the use of open source software, including commercial off-the-shelf tools, unless approved by the MoJ. Contact the Cyber Assistance Team (CAT) for advice at [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk). |
| ✖ You should not allow general users to execute code on their mobile devices. Your devices should be able to: |
| - identify malicious code      
| - prevent downloading and execution      
| - prevent automatic execution, and      
| - allow execution only in secured and segregated environments. |
| ✖ You should not reveal error messages to anyone outside of the MoJ-defined personnel and roles.
