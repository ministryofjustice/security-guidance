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

| Do |
|--- |
| ✔ Enforce access control through using multi-factor authentication, security attributes and enforcing the ‘need to know’ principle. Dual authorisation must also be used to conduct sensitive system changes. |
| ✔ Implement host-based protection for established boundaries. |
| ✔ Restrict and monitor remote access connections through the following controls:
| - Encryption
| - secure network protocols. |
| ✔ When protecting the MoJ wired and wireless networks, you must implement the following access control and security measures:
| - restricting a user’s ability to change wireless configurations     
| - preventing electromagnetic interference, for example through TEMPEST controls and strong encryption and authentication
| - reducing wireless detection potential     
| - conducting signal parameter identification      
| - implementing wireless intrusion detection tools
| - implementing wireless to wireline communications. |
| ✔ Synchronise timestamps with a primary and secondary authoritative time source. |
| ✔ Classify system connections and apply restrictions to external systems and public networks. |
| ✔ Test backup solutions at least every three months for data reliability and integrity. |
| ✔ Use backlisting/whitelisting tools for current and newly developed software. |
| ✔ Use encryption to protect information. Encryption mechanisms should include:
| - secure key management and storage   
| - PKI certificates and hardware tokens. |
| ✔ When using system component inventories ensure that they: |
| - are updated during installations and/or removals     
| - have automated location tracking      
| - have components assigned to systems
| - do not have component duplication. |
| ✔ To protect the network against malicious code, implement the following security controls:
| - vulnerability scanning tools
| - intrusion detection systems
| - non-signature based detection
| - software patching and updates
| - detect unauthorised commands
| - tools for real-time analysis
| - indicators of compromise detection. |
| ✔ When connecting to external networks and systems, establish and maintain a trust relationship and ensure secure processing, storage, service controls and locations. |
| ✔ Enable excess capacity or bandwidth above what is required for business as usual operations, and implement monitoring and detection tools for denial of service attempts. |
| ✔ Enforce both signature and non-signature based detection of malicious code or behaviour. |
| ✔ Where possible, ensure a redundant secondary system or other resilience controls are in place, which have alternative security mechanisms and communication protocols. |

The table below identifies what should not be done, and what activities should be limited, to improve baseline security controls.

| Don't |
|---|
| ✖ Do not allow systems to release information outside of established boundaries unless the following security controls are implemented:|
| - boundary security filters
| - domain authentication
| - logical separation of information flows
| - security attribute binding
| - one way flowing mechanisms
| - dynamic information flow control
| - detection of unsanctioned information
| - embedded data types
| - restriction of suspicious inbound and outbound traffic. |
| ✖ Do not allow general users to make configuration changes to software, firmware or hardware. Any exceptions, such as software updates, must be risk assessed and approved by IT and the Risk Advisory Team. |
| ✖ Do not allow users to install software. Instead, software installations should be approved and only users with privileged access should be permitted to conduct the installation. |
| ✖ Do not allow split tunnelling. |
| ✖ Do not allow inbound traffic to go through unauthenticated networks. Instead, use authenticated proxy servers. |
| ✖ Do not allow general users to execute code. Code must only be executed by authorised users (such as the IT team). Any exceptions must be risk-assessed and approved by IT and the Risk Advisory Team. |
| ✖ Do not allow the discovery of system components or devices on the network. |
| ✖ Do not enable boundary protection settings to allow different security domains to connect through the same subnet. |

## Defensive Layer 1: creating a baseline security - software development and system configuration

The table below outlines what should be in place to create secure software development and configuration environments within the MoJ.

| Do |
|--- |
| ✔ If you are developing new systems or applications, use a development lifecycle which enforces security by design. Examples include: |
| - code analysis and testing      
| - mapping integrity for version control      
| - trust distribution
| - software/firmware/hardware integrity verification.|
| ✔ Use baseline configuration templates for critical and non-critical assets. These need to include: |
| - automation support for accuracy/currency     
| - retention of previous configurations     
| - separate development and test environments     
| - cryptography management, and    
| - unauthorised change detection. |
| ✔ Enforce binary or machine executable code and implement time limits for process execution. |
| ✔ Verify the boot process and ensure the protection of boot hardware. |
| ✔ Enforce module coupling for software engineering. |
| ✔ Enforce application partitioning. |
| ✔ Take a ‘deny by default’ approach to boundary protection for both outbound as well as inbound. Example controls include: |
| - automated enforcement of protocol formats   
| - separate subnets for connecting to different security domains.|
| ✔ Enforce protocol formats. |

The table below outlines the actions that should not be undertaken in relation to software development and secure configuration.

| Don't |
|---|
| ✖ Do not allow access privileges to library and production/operation environments for unauthorised users. |
| ✖ Do not allow systems or applications to go live without testing them in a non-live environment. |
| ✖ Do not use live data, including personal data, in system or application testing. Exceptions must be approved by the group SIRO. |
| ✖ Do not implement off-the-shelf software without ensuring appropriate support and security arrangements/agreements are in place. |
