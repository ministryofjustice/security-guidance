---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](home-security-policies-guides.md)

# Technical Security Controls Guide: Defensive Layer 1

This guide is a sub-page to the [Technical Controls Guide](technical-security-controls-guide.md).

## Defensive layer 1: creating a baseline security environment - general

This table displays the security controls that should be implemented to create a baseline security environment.

<table>
<tr><th>Do</th></tr>
<tr><td>✔ Enforce access control through using multi-factor authentication, security attributes and enforcing the 'need to know' principle. Dual authorisation must also be used to conduct sensitive system changes.</td></tr>
<tr><td>✔ Implement host-based protection for established boundaries.</td></tr>
<tr><td>✔ Restrict and monitor remote access connections through the following controls:
<ul>
<li>Encryption</li>
<li>Secure network protocols.</li></ul></td></tr>
<tr><td>✔ When protecting the MoJ wired and wireless networks, you must implement the following access control and security measures:
<ul>
<li>restricting a user's ability to change wireless configurations</li>
<li>preventing electromagnetic interference, for example through TEMPEST controls and strong encryption and authentication</li>
<li>reducing wireless detection potential</li>
<li>conducting signal parameter identification</li>
<li>implementing wireless intrusion detection tools</li>
<li>implementing wireless to wireline communications.</li></ul></td></tr>
<tr><td>✔ Synchronise timestamps with a primary and secondary authoritative time source.</td></tr>
<tr><td>✔ Classify system connections and apply restrictions to external systems and public networks.</td></tr>
<tr><td>✔ Test backup solutions at least every three months for data reliability and integrity.</td></tr>
<tr><td>✔ Use deny-listing/allow-listing tools for current and newly developed software.</td></tr>
<tr><td>✔ Use encryption to protect information. Encryption mechanisms should include:
<ul>
<li>secure key management and storage</li>
<li>PKI certificates and hardware tokens.</li></ul></td></tr>
<tr><td>✔ When using system component inventories ensure that they:
<ul>
<li>are updated during installations and/or removals</li>
<li>have automated location tracking</li>
<li>have components assigned to systems</li>
<li>do not have component duplication.</li></ul></td></tr>
<tr><td>✔ To protect the network against malicious code, implement the following security controls:
<ul>
<li>vulnerability scanning tools</li>
<li>intrusion detection systems</li>
<li>non-signature based detection</li>
<li>software patching and updates</li>
<li>detect unauthorised commands</li>
<li>tools for real-time analysis</li>
<li>indicators of compromise detection.</li></ul></td></tr>
<tr><td>✔ When connecting to external networks and systems, establish and maintain a trust relationship and ensure secure processing, storage, service controls and locations.</td></tr>
<tr><td>✔ Enable excess capacity or bandwidth above what is required for business as usual operations, and implement monitoring and detection tools for denial of service attempts.</td></tr>
<tr><td>✔ Enforce both signature and non-signature based detection of malicious code or behaviour.</td></tr>
<tr><td>✔ Where possible, ensure a redundant secondary system or other resilience controls are in place, which have alternative security mechanisms and communication protocols.</td></tr>
</table>

The table below identifies what should not be done, and what activities should be limited, to improve baseline security controls.

<table>
<tr><th>Don't</th></tr>
<tr><td>✖ Do not allow systems to release information outside of established boundaries unless the following security controls are implemented:
<ul>
<li>boundary security filters</li>
<li>domain authentication</li>
<li>logical separation of information flows</li>
<li>security attribute binding</li>
<li>one way flowing mechanisms</li>
<li>dynamic information flow control</li>
<li>detection of unsanctioned information</li>
<li>embedded data types</li>
<li>restriction of suspicious inbound and outbound traffic.</li></ul></td></tr>
<tr><td>✖ Do not allow general users to make configuration changes to software, firmware or hardware. Any exceptions, such as software updates, must be risk assessed and approved by IT and the Risk Advisory Team.</td></tr>
<tr><td>✖ Do not allow users to install software. Instead, software installations should be approved and only users with privileged access should be permitted to conduct the installation.</td></tr>
<tr><td>✖ Do not allow split tunnelling.</td></tr>
<tr><td>✖ Do not allow inbound traffic to go through unauthenticated networks. Instead, use authenticated proxy servers.</td></tr>
<tr><td>✖ Do not allow general users to execute code. Code must only be executed by authorised users (such as the IT team). Any exceptions must be risk-assessed and approved by IT and the Risk Advisory Team.</td></tr>
<tr><td>✖ Do not allow the discovery of system components or devices on the network.</td></tr>
<tr><td>✖ Do not enable boundary protection settings to allow different security domains to connect through the same subnet.</td></tr>
</table>

## Defensive Layer 1: creating a baseline security - software development and system configuration

The table below outlines what should be in place to create secure software development and configuration environments within the MoJ.

<table>
<tr><th>Do</th></tr>
<tr><td>✔ If you are developing new systems or applications, use a development lifecycle which enforces security by design. Examples include:
<ul>
<li>code analysis and testing</li>
<li>mapping integrity for version control</li>
<li>trust distribution</li>
<li>software/firmware/hardware integrity verification.</li></ul></td></tr>
<tr><td>✔ Use baseline configuration templates for critical and non-critical assets. These need to include:
<ul>
<li>automation support for accuracy/currency</li>
<li>retention of previous configurations</li>
<li>separate development and test environments</li>
<li>cryptography management, and</li>
<li>unauthorised change detection.</li></ul></td></tr>
<tr><td>✔ Enforce binary or machine executable code and implement time limits for process execution.</td></tr>
<tr><td>✔ Verify the boot process and ensure the protection of boot hardware.</td></tr>
<tr><td>✔ Enforce module coupling for software engineering.</td></tr>
<tr><td>✔ Enforce application partitioning.</td></tr>
<tr><td>✔ Take a 'deny by default' approach to boundary protection for both outbound as well as inbound. Example controls include:
<ul>
<li>automated enforcement of protocol formats</li>
<li>separate subnets for connecting to different security domains.</li></ul></td></tr>
<tr><td>✔ Enforce protocol formats.</td></tr>
</table>

The table below outlines the actions that should not be undertaken in relation to software development and secure configuration.

| Don't |
|---|
| ✖ Do not allow access privileges to library and production/operation environments for unauthorised users. |
| ✖ Do not allow systems or applications to go live without testing them in a non-live environment. |
| ✖ Do not use live data, including personal data, in system or application testing. Exceptions must be approved by the group SIRO. |
| ✖ Do not implement off-the-shelf software without ensuring appropriate support and security arrangements/agreements are in place. |
