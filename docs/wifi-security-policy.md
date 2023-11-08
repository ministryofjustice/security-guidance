# Wifi security policy

## Introduction

This policy gives an overview of wireless networking \(wifi\) security principles and responsibilities within the .

To help identify formal policy statements, each is prefixed with an identifier of the form: **POL.WIFI.xxx**, where **xxx** is a unique ID number.

## Audience

This policy is aimed at:

<a name="technical-users"></a>

-   **Technical users**

    These are in-house Digital and Technology staff who are responsible for implementing controls throughout technical design, development, system integration, and operation. This includes DevOps, Software Developers, Technical Architects, and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI, and Knowledge \(EPICK\) Team.

<a name="service-providers"></a>

-   **Service Providers**

    Any other business group, agency, contractor, IT supplier, and partner who in any way designs, develops or supplies services, including processing, transmitting,and storing data for, or on behalf of, the .

<a name="general-users"></a>

-   **General users**

    All other staff working for the .


"All users" refers to General users, Technical users, and Service Providers, as defined previously.

## Purpose

The purpose of this document is to define a set of security requirements for wifi networks, based on industry good practices and our local requirements.

**POL.WIFI.001:** Any exceptions to the policy be managed through the 's security risk management process.

## Applicability

This policy applies to all owned or managed wifi networks provided for any purpose. It also applies to the use of third-party wifi networks by devices which handle information, for example staff end user computing devices.

## wifi networks

**POL.WIFI.002:** Each wifi network have a defined policy which is reviewed at least annually, that describes:

-   The purpose of the wifi network.

-   The intended users of the wifi network.

-   The Service Owner of the wifi network.

-   The access controls that are applied to ensure that only those intended users can connect to the wifi network.

-   User and administrator responsibilities for maintaining the security of the wifi network.

-   Who has authority to expand or alter the wifi network.

-   Logging and monitoring requirements and responsibilities for the wifi network.


## General security requirements

The following statements apply to all -provided wifi networks.

**POL.WIFI.003:** Wifi networks be treated as extensions of trusted LANs or WANs.

**POL.WIFI.004:** Wifi networks be treated as untrusted bearers for the purposes of application security.

**POL.WIFI.005:** All products used in an wifi network support WPA2-Enterprise.

**POL.WIFI.006:** CCMP be used to protect the confidentiality and integrity of information transmitted over the wifi network.

**POL.WIFI.007:** Other wifi security modes \(such as WEP\) be enabled.

**POL.WIFI.008:** All products used in wifi networks support certificate-based authentication.

**POL.WIFI.009:** On wireless networks, isolation between wifi clients be enabled. Where there is no requirement for devices to communicate directly, isolation be enabled.

**POL.WIFI.010:** wireless networks use a DNS resolver that chains to the [Protective Domain Name Service \(PDNS\)](https://www.ncsc.gov.uk/information/pdns) service.

**POL.WIFI.011:** All wireless networking equipment be kept [patched and secure](vulnerability-scanning-and-patch-management-guide.md), whether connecting to wifi services or GovWifi.

**POL.WIFI.012:** All management of Wireless networking equipment be undertaken in compliance with the [Privileged User Access Guide](privileged-account-management-guide.md) and any relevant Security Operating Procedures \(SyOPS\).

## enterprise wifi networks

**Note:** enterprise wifi networks are those used solely for users and devices.

**POL.WIFI.013:** Pre-Shared Keys \(PSKs\) be used for user or device authentication.

**POL.WIFI.014:** PSKs be unique per user or device.

**POL.WIFI.015:** PSKs only be implemented with prior agreement from the cyber security team

**POL.WIFI.016:** PSKs be changed at least once a year.

**POL.WIFI.017:** EAP-PSK be used.

**POL.WIFI.018:** In higher-threat situations such as in a prison location where any unauthorised use of the Wireless network would constitute a security incident, mutually-authenticated authentication based on certificates be used.

**POL.WIFI.019:** EAP-TLS or EAP-TTLS be used.

**POL.WIFI.020:** Where user or device groups have differing functions, PKI trust domains be defined and used to maintain functional separation.

## special-purpose wifi networks

**POL.WIFI.021:** If devices, including IoT or legacy devices, cannot meet the general security policy requirements, or if there are non-security reasons for segregating traffic onto different SSIDs, then dedicated wifi networks be created.

**POL.WIFI.022:** These dedicated networks have reduced authentication controls, for example a shared PSK or a reduced ability to rotate PSKs due to form-factor limitations.

**POL.WIFI.023:** In such circumstances, special care be taken to ensure that the general network architecture and other security controls constrain network connectivity for clients. The constraints limit network connectivity to the minimum required for them to function properly.

**POL.WIFI.024:** Other mechanisms such as MAC filtering be used to reduce the chance of misuse.

## guest wifi networks

Due to complexities and management effort involved in running wifi solutions, the preference is to utilise the cross-Government GovWifi service: [https://www.wifi.service.gov.uk/](https://www.wifi.service.gov.uk/).

This also has the benefit of being available across HMG Departments and Agencies. GovWifi has a level of pre-registration, monitoring and filtering in place to protect the users. However, GovWifi does not provide enterprise level security functions. GovWifi users are required to maintain their own security controls. For users of GovWifi connections, this means using the -provided VPN services when accessing protected services.

**POL.WIFI.025:** Any considerations for not using GovWifi in an guest wifi network be discussed and agreed beforehand with the cyber security team.

**POL.WIFI.026:** Where GovWifi cannot be used, or where an existing guest wifi service exists,the following be in place:

-   Regular rotation of the passphrase, with agreement from the . Normally, this requires a fresh and unique passphrase each day.

-   Filtering and Monitoring for known 'bad-sites' and threats be in place at the network level.

-   Guests wishing to utilise the service first register for access, and can then be provided with the passphrase for that day.


## Logging and monitoring

**POL.WIFI.027:** Security monitoring for wireless networks be implemented, in accordance with the [security monitoring policy](logging-and-monitoring.md).

**POL.WIFI.028:** Security logging be enabled to record activity such as client access events, authentication successes and failures, client association history, and relevant information about devices and users attempting to connect to the wireless network.

**POL.WIFI.029:** In higher threat environments, security logging also include identification of rogue access points, and logging of all attempted associations with the wifi network.

**POL.WIFI.030:** For guest wifi networks, but not including GovWifi, audit logs of sites accessed be retained for at least 6 months, including authentication details. This data is held to allow forensic analysis of data in the case of a security incident. No personal information except that required to conduct the analysis is logged or retained.

## Using third-party wifi

**POL.WIFI.031:** staff ensure they have permission from the network owner before using wifi that is not operated by the .

**POL.WIFI.032:** Staff take [reasonable precautions](https://ico.org.uk/your-data-matters/online/wifi-security/) to check that their home wifi network is secure.

**POL.WIFI.033:** Staff use work-provided mobile phones to 'tether' their -provided devices for connectivity.

**POL.WIFI.034:** Tethered connections be password protected using unique and complex passwords.

**POL.WIFI.035:** Tethering passwords for devices be shared with non- users.

**POL.WIFI.036:** Public wifi networks or guest wifi provided at third-party sites only be used by devices which have suitable encryption for information. Here, 'suitable' means either an 'always-on full-take' VPN, or that provides appropriate application-level encryption for all services. This is currently \(October 2021\) limited to Dom1 and PTTP/MoJO laptops and mobile devices.

**POL.WIFI.037:** Staff travelling overseas follow the guidance on accessing IT systems from overseas regarding the use of wifi or other networks.

## Enforcement

This policy is enforced by lower level policies, standards, procedures, and guidance.

Non-conformance with this policy could result in disciplinary action taken in accordance with the 's disciplinary procedures. This could result in penalties up to and including dismissal. If an employee commits a criminal offence, they might also be prosecuted. In such cases, the department always cooperates with the relevant authorities, and provides appropriate evidence.

