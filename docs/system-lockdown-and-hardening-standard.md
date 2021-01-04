# System Lockdown and Hardening Standard

## Legacy information

**Note:** This document is Legacy IA Policy. It is under review and likely to be withdrawn or substantially revised soon. Before using this content for a project, contact [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

**Note:** This document might refer to several organisations, information sources, or terms that have been replaced or updated, as follows:

-   CESG \(Communications-Electronics Security Group\), refer to the National Cyber Security Centre \(NCSC\), contact [security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk).
-   CINRAS \(Comsec Incident Notification Reporting and Alerting Scheme\), refer to the NCSC, contact [security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk).
-   ComSO \(Communications Security Officer\), contact the Chief Information Security Office \(CISO\) \([security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk)\).
-   `CONFIDENTIAL`, an older information classification marking, see [Information Classification and Handling Policy](information-classification-and-handling-policy.md).
-   CPNI \([Centre for the Protection of the National Infrastructure](https://www.cpni.gov.uk/)\), contact the CISO \([security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk)\).
-   DSO \(Departmental Security Officer\), contact the Senior Security Advisor \([security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk)\).
-   GPG6 \(Good Practice Guide 6: Outsourcing and Offshoring: Managing the Security Risks\), refer to the NCSC, contact [security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk).
-   IS1 \(HMG Infosec Standard 1 Technical Risk Assessment\), see the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   IS4 \(HMG Infosec Standard 4 Communications Security and Cryptography\), see the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   IS6 \(HMG Infosec Standard 6 Protecting Personal Data and Managing Information Risk\), see the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   ITSO \(Information Technology Security Officer\), contact the CISO \([security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk)\).
-   `RESTRICTED`, an older information classification marking, see [Information Classification and Handling Policy](information-classification-and-handling-policy.md).
-   SPF \([Security Policy Framework](https://www.gov.uk/government/publications/security-policy-framework)\), see the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security), contact [security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk).

## Overview

This standard is designed to help protect Ministry of Justice \(MoJ\) IT systems by providing basis configuration details for how IT systems should be hardened to defend against malicious attack.

[HMG Security Policy Framework](https://www.gov.uk/government/publications/security-policy-framework/hmg-security-policy-framework) mandatory requirement \(MR\) 9 concerns technical security controls. To comply with MR 7, the MoJ needs to ensure that it has:

> Lockdown policy to restrict unnecessary services;

The lockdown policy itself is covered in the IT Security – Technical Controls Policy whilst this document sets out the MoJ standard for its application.

### Scope

This standard provides some high level guidance on IT system hardening with which applied to all MoJ IT systems.

**Note:** This standard is a generic standard designed to provide high level direction. This standard does not replace the Government Assurance Pack \(GAP\) which must be considered for MS Windows based systems. The hardening of an IT system will be considered during the Accreditation process where the exact specification for the system will be considered and agreed. For further details on the Accreditation process see.

This standard must be read in conjunction with CESG GPG No.35 and the MoJ Security Architecture Framework.

### Demonstration of Compliance

The CESG Information Assurance Maturity Model \(IAMM\) sets out the minimum maturity level Government departments should attain. Providing secure IT systems captured as a basic requirement in Level 1 and the MoJ will need to demonstrate compliance against this requirement.

## Generic hardening standard

Table 1 below provides a generic set of hardening procedures designed to guide IT system development and supplement the [IT Security – Technical Controls Policy](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/technical-controls-policy/).

Those configuring MoJ IT systems must consider additional sources of reference such as the Government Assurance Pack \(GAP\) for MS Windows based systems; Microsoft TechNet and NIST to ensure that specific systems \(e.g. SQL server or a UNIX based server\) are built to a secure standard. A selection of external reference sources can be found below.

Where this standard provides a generic set of hardening procedures, The MoJ Security Architecture Framework provides a set of vendor and system specific hardening guides which have been approved for use in MoJ IT systems.

The secure configuration of an IT system will be examined during the Accreditation process for further details\). This may include an IT Health Check \(ITHC\) and a review of the system's build configuration.

Table 1 is split into 5 sections:

-   General – Procedures which can be commonly applied to most IT systems;

-   External devices;

-   Account log-on;

-   Services, security and networking applications;

-   Server specific – Procedures which can be commonly applied to servers.


### General

|Name|Description|
|BIOS Lockdown|Access to the BIOS must be restricted to system administrators only.|
|Removal of unnecessary applications and services|All applications and system services which are not required must be uninstalled or disabled.|
|Auto-run of data on remote media devices|Auto-run must be disabled.|
|Screen lockout|Desktops and servers must be configured to lock after 5 minutes of inactivity. Unlock must be by password only.|
|Time and Date|The Time and Date setting must be configured to central synchronisation servers which synchronises with the GSi time server.|
|System Preferences|Non-system administrative Users must not have access to change: -   The desktop background or screensaver setting;
-   The date or time;
-   Network settings or internet browser settings;
-   System security settings or group policy settings.

 Non-system administrative Users must not have access to the following system settings / utilities: -   The system registry;
-   Access to operating system directories and files;
-   Access to CMD / Command Line Prompt and local system utilities such as disk defragmenter and disk cleanup.

|

#### External Devices

|Name|Description|
|----|-----------|
|Bluetooth|Bluetooth must be disabled by default. If required due to business need, Bluetooth devices must be set to not be 'discoverable'.|
|Webcam|The webcam lens must be obstructed when not in use.|
|Infrared receiver|The IR receiver must be disabled, ideally at the hardware level \(by physically disconnecting the component\).|
|Sound input \(microphone\)|Sound input from a microphone must be kept at zero level when not in use.|
|Media drives and external data ports \(e.g. USB, FireWire, CD/DVD drive, ...\)|All media drives and external data ports must be disabled. Where there is a business justification to allow access, that access must be audited and restricted to an individual User \(for example using a technical control such as Lumension\).|

#### Account Log-on

|Name|Description|
|----|-----------|
|Passwords|All passwords must conform to the [password guidance](passwords.md).|
|Guest and 'null' accounts|Guest and 'null' accounts \(accounts with a blank username and password\) must be disabled and removed where possible.|
|Fast User Switching|Fast User Switching must be disabled.|
|Login failure logging|Failed logins must be logged after the 1st failed attempt.|
|Automatic log in|Any automatic log in feature must be disabled. This does not include Single Sign On functionality where a User has already authenticated themselves to the system.|
|User list|The option to display a set of usernames list or the previous logged in User's username at logon must be disabled.|
|Logon Banner|The standard MoJ login banner must be displayed at login, both locally and remotely, see [Appendix A](#appendix-a-login-banner).|

#### Services, security and networking applications

|Name|Description|
|Firewalls|An Application Firewall should be installed which: -   Must be configured to 'allow only essential services';
-   Must log Firewall activity;
-   Must operate in 'stealth mode' \(undiscoverable\).

|
|Anonymous FTP|Anonymous FTP must be disabled. Where there is a business requirement for FTP, FTP\(S\) or SFTP must be used.|
|Simple Network Management Protocol \(SNMP\)|Where SNMP is required, v2.0 must be used.|
|Cisco Discovery Protocol \(CDP\)|CDP must be disabled.|
|Telnet based administration interface|Telnet access must be disabled.|
|SSH based administration interface|SSH access must be disabled.|
|HTTP based administration interface|All web based administration interfaces which are accessible over a network \(in other words, not restricted to a localhost\) must be encrypted for the entire session using SSL version 3 or TLS version 1.0 or above.|
|Connection Timeouts|Idle connections must be dropped after a default period.|
|ICMP Redirects|ICMP redirects must be disabled.|
|Clear text authentication protocols|All plain-text authentication protocols must be disabled and their functionality replaced with encrypted alternatives.|

#### Server specific

|Name|Description|
|----|-----------|
|Internet access from web browsers|External Internet access from web browsers must be disabled.|
|Example, test and temporary installation files.|All example, test and temporary installation files must be deleted when no longer required.|
|File share access control|Server file shares must be subject to access control restrictions.|

## External reference sources

In addition to CESG GPG No.35, the following external reference sources provide a good source of information on IT system hardening and secure system configuration.

### CPNI

CPNI provides general information on security IT systems including advice on how to build secure systems: [https://www.cpni.gov.uk/cyber-security](https://www.cpni.gov.uk/cyber-security).

### NIST

NIST is a US standards body and provide a wealth of information which can be used to build secure systems: [https://www.nist.gov/cybersecurity](https://www.nist.gov/cybersecurity).

### SANS

The SANS Institute provides a source of best practice advice for designing and configuring secure systems including Apple MAC OS and Linux based systems: [https://www.sans.org/reading\_room/](https://www.sans.org/reading_room/).

### Microsoft

Microsoft provides detailed information and configuration details covering the lockdown and hardening of Microsoft server and desktop products.

## Appendix A – Login banner

The standard MoJ login banner must be displayed at login. A copy of the banner is as follows:

> THIS SYSTEM IS FOR AUTHORISED USERS ONLY.

> This is a private system; only use this system if you have specific authority to do so. Otherwise you are liable to prosecution under the Computer Misuse Act 1990. If you do not have the express permission of the operator or owner of this system, switch off now to avoid prosecution.

