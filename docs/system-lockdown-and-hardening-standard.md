# System Lockdown and Hardening Standard

This standard is designed to help protect IT systems by providing basic configuration details for how IT systems should be hardened to defend against malicious attack.

The describes mandatory requirements for security controls. To comply with the , the requires that IT systems and services are:

-   Locked-down: All unnecessary or non-essential services or capabilities are switched off, or restricted to the bare minimum of functionality.
-   Hardened: All system options and capabilities are configured for maximum possible resistance to attack or unauthorised use.

Specifics of the lockdown policy are covered in the [Technical Controls Policy](technical-controls-policy.md#lockdown-policy). This document provides more information about the implementation of the lockdown policy.

**Related information**  


[Technical Controls Policy](technical-controls-policy.md)

## Scope

This standard provides some high level guidance on IT system hardening. It applies to all IT systems.

**Note:** This standard is a generic standard, designed to provide high level direction. It does not replace platform- or system-specific hardening guidance, such as vendor advisory or best practice recommendations.

This standard be read in conjunction with the , the , and the .

## Demonstration of Compliance

The [NCSC GPG40 Information Assurance Maturity Model \(IAMM\)](https://www.ncsc.gov.uk/information/hmg-ia-maturity-model-iamm) provides useful guidance on the security levels expected for systems and services. All demonstrate compliance that meets or exceeds maturity Level 1, or equivalent.

## Generic hardening standard

This standard provides a generic set of hardening details, designed to guide IT system development and to supplement the [Technical Controls Policy](technical-controls-policy.md).

Those configuring IT systems consider additional sources of reference such as vendor-supplied platform-specific materials to ensure that specific systems, such as SQL server or UNIX-based servers, are built and configured to a secure standard. A selection of external reference sources can be found in this guidance.

Where this standard provides a generic set of hardening procedures, other material in the [security guidance](cyber-and-technical-security-guidance.md) provides vendor- and system-specific hardening guides which have been approved for use in IT systems.

The secure configuration of an IT system be examined during the assurance process. This might include an IT Health Check \(ITHC\), and a review of the system's build configuration.

Details provided in this standard address:

-   [General procedures](#general-procedures) which can be commonly applied to most IT systems.

-   [External devices](#external-devices).

-   [Account log-on](#account-log-on).

-   [Services, security and networking applications](#services-security-and-networking-applications).

-   [Server-specific](#server-specific) procedures which can be commonly applied to servers.


### General procedures

|Name|Description|
|----|-----------|
|BIOS Lockdown|Access to the BIOS be restricted to system administrators only.|
|Removal of unnecessary applications and services|All applications and system services which are not required be uninstalled or disabled.|
|Auto-run of data on remote media devices|Auto-run be disabled.|
|Screen lockout|Desktops and servers be configured to lock after 5 minutes of inactivity. Unlock be by password only.|
|Time and Date|The Time and Date setting be configured to central synchronisation servers, which themselves synchronise with the UK Government time server.|
|System Preferences|Users without system administration privileges have access to change the desktop background or screensaver setting, the date or time, network settings or internet browser settings, and system security settings or group policy settings. Users without system administration privileges have access to the system settings or utilities including the system registry or administrative equivalent, access to operating system directories and files, access to CMD or Command Line Prompt, access to terminal commands or tools, or access to local system utilities such as disk defragmenter and disk cleanup.|

#### External Devices

|Name|Description|
|----|-----------|
|Bluetooth|Bluetooth be disabled by default. If required due to business need, Bluetooth devices be set as 'discoverable'.|
|Webcam|The webcam lens be obstructed when not in use.|
|Infrared receiver|The IR receiver be disabled, ideally at the hardware level by physically disconnecting the component.|
|Sound input \(microphone\)|Sound input from a microphone be kept at zero level when not in use.|
|Media drives and external data ports, such as USB, FireWire, CD/DVD drive, and similar|All media drives and external data ports be disabled by default. Where there is a business justification to allow access, that access be audited and restricted to an individual user, for example when using an approved tool for an approved business purpose.|

#### Account Log-on

|Name|Description|
|----|-----------|
|Passwords|All passwords conform to the [password guidance](passwords.md).|
|Guest and 'null' accounts|Guest and 'null' accounts \(accounts with a blank username or password\) be disabled and removed where possible.|
|Fast User Switching|Fast User Switching be disabled.|
|Login failure logging|Failed logins be logged after the 1st failed attempt.|
|Automatic log in|Any automatic log in feature be disabled. This does not include Single Sign On functionality, where a user has already authenticated themselves to the system.|
|User list|During logon, the option to display a set of possible usernames, or the previous usernames that logged on successfully, be disabled.|
|Logon Banner|The standard login banner be displayed at login, both locally and remotely. The standard banner is provided in [Appendix A](#appendix-a-login-banner).|

#### Services, security, and networking applications

|Name|Description|
|----|-----------|
|Firewalls|An application firewall be installed. The firewall be configured to 'allow only essential services', log firewall activity, and operate in 'stealth mode' \(undiscoverable\).|
|Anonymous FTP|Anonymous FTP be disabled. Where there is a business requirement for file transfer between systems, FTP\(S\) or SFTP be used.|
|Simple Network Management Protocol \(SNMP\)|Where SNMP is required, version 2.0 or a more recent version be used.|
|Cisco Discovery Protocol \(CDP\)|CDP be disabled.|
|Telnet based administration interface|Telnet access be disabled.|
|SSH based administration interface|SSH access direct into an administrative account or service be disabled.|
|HTTP based administration interface|All web based administration interfaces which are accessible over a network \(in other words, not restricted to a localhost\) be encrypted for the entire session using SSL version 3, or TLS version 1.2, or higher.|
|Connection Timeouts|Idle connections be disconnected after a default period; normally less than 30 minutes.|
|ICMP Redirects|ICMP redirects be disabled.|
|Clear text authentication protocols|All plain-text authentication protocols be disabled and their functionality replaced with encrypted alternatives.|
|Initiating outbound connections|An system or service initiate a connection to a non- system or service, unless such outbound connections have been reviewed and approved as a standard part of their design. Firewall rules and other network configuration prevent unapproved outbound connections.|

#### Server specific

|Name|Description|
|----|-----------|
|Internet access from web browsers|External Internet access from web browsers on a server be disabled.|
|Example, test and temporary installation files.|All example, test and temporary installation files be deleted when no longer required.|
|File share access control|Server file shares be subject to access control restrictions.|

## External reference sources

The following external reference sources provide a good source of information on IT system hardening and secure system configuration.

### CPNI

CPNI provides general information on security IT systems including advice on how to build secure systems: [https://www.cpni.gov.uk/cyber-security](https://www.cpni.gov.uk/cyber-security).

### NIST

NIST is a US standards body and provide a wealth of information which can be used to build secure systems: [https://www.nist.gov/cybersecurity](https://www.nist.gov/cybersecurity).

### SANS

The SANS Institute provides a source of best practice advice for designing and configuring secure systems including Apple MAC OS and Linux based systems: [https://www.sans.org/reading\_room/](https://www.sans.org/reading_room/).

### Microsoft

Microsoft provides detailed information and configuration details covering the lockdown and hardening of Microsoft server and desktop products.

## Appendix A: Login banner

The standard login banner be displayed at login:

> THIS SYSTEM IS FOR AUTHORISED USERS ONLY.

> This is a private system; only use this system if you have specific authority to do so. Otherwise you are liable to prosecution under the Computer Misuse Act 1990. If you do not have the express permission of the operator or owner of this system, switch off or disconnect now to avoid prosecution.

