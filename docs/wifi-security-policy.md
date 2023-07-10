# Wifi security policy

## Introduction

This policy gives an overview of wireless networking \(wifi\) security principles and responsibilities within the Ministry of Justice \(MoJ\).

To help identify formal policy statements, each is prefixed with an identifier of the form: **POL.WIFI.xxx**, where **xxx** is a unique ID number.

## Audience

This policy is aimed at:

<a name="technical-users"></a>

-   **Technical users**

    These are in-house MoJ Digital and Technology staff who are responsible for implementing controls throughout technical design, development, system integration, and operation. This includes DevOps, Software Developers, Technical Architects, and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI, and Knowledge \(EPICK\) Team.

<a name="service-providers"></a>

-   **Service Providers**

    Any other MoJ business group, agency, contractor, IT supplier, and partner who in any way designs, develops or supplies services, including processing, transmitting,and storing data for, or on behalf of, the MoJ.

<a name="general-users"></a>

-   **General users**

    All other staff working for the MoJ.


"All MoJ users" refers to General users, Technical users, and Service Providers, as defined previously.

## Purpose

The purpose of this document is to define a set of security requirements for MoJ wifi networks, based on industry good practices and our local requirements.

**POL.WIFI.001:** Any exceptions to the policy **shall** be managed through the MoJ's security risk management process.

## Applicability

This policy applies to all MoJ owned or managed wifi networks provided for any purpose. It also applies to the use of third-party wifi networks by MoJ devices which handle **Official** information, for example staff end user computing devices.

## MoJ wifi networks

**POL.WIFI.002:** Each MoJ wifi network **shall** have a defined policy which is reviewed at least annually, that describes:

-   The purpose of the wifi network.

-   The intended users of the wifi network.

-   The Service Owner of the wifi network.

-   The access controls that are applied to ensure that only those intended users can connect to the wifi network.

-   User and administrator responsibilities for maintaining the security of the wifi network.

-   Who has authority to expand or alter the wifi network.

-   Logging and monitoring requirements and responsibilities for the wifi network.


## General security requirements

The following statements apply to all MoJ-provided wifi networks.

**POL.WIFI.003:** Wifi networks **shall not** be treated as extensions of trusted LANs or WANs.

**POL.WIFI.004:** Wifi networks **shall** be treated as untrusted bearers for the purposes of application security.

**POL.WIFI.005:** All products used in an MoJ wifi network **shall** support WPA2-Enterprise.

**POL.WIFI.006:** CCMP **shall** be used to protect the confidentiality and integrity of information transmitted over the wifi network.

**POL.WIFI.007:** Other wifi security modes \(such as WEP\) **shall not** be enabled.

**POL.WIFI.008:** All products used in MoJ wifi networks **shall** support certificate-based authentication.

**POL.WIFI.009:** On MoJ wireless networks, isolation between wifi clients **should** be enabled. Where there is no requirement for devices to communicate directly, isolation **shall** be enabled.

**POL.WIFI.010:** MoJ wireless networks **should** use a DNS resolver that chains to the [Protective Domain Name Service \(PDNS\)](https://www.ncsc.gov.uk/information/pdns) service.

**POL.WIFI.011:** All MoJ wireless networking equipment **shall** be kept [patched and secure](vulnerability-scanning-and-patch-management-guide.md), whether connecting to MoJ wifi services or GovWifi.

**POL.WIFI.012:** All management of MoJ Wireless networking equipment **shall** be undertaken in compliance with the [Privileged User Access Guide](privileged-account-management-guide.md) and any relevant Security Operating Procedures \(SyOPS\).

## MoJ enterprise wifi networks

**Note:** MoJ enterprise wifi networks are those used solely for MoJ users and devices.

**POL.WIFI.013:** Pre-Shared Keys \(PSKs\) **may** be used for user or device authentication.

**POL.WIFI.014:** PSKs **shall** be unique per user or device.

**POL.WIFI.015:** PSKs **shall** only be implemented with prior agreement from the cyber security team

**POL.WIFI.016:** PSKs **shall** be changed at least once a year.

**POL.WIFI.017:** EAP-PSK **should** be used.

**POL.WIFI.018:** In higher-threat situations such as in a prison location where any unauthorised use of the Wireless network would constitute a security incident, mutually-authenticated authentication based on certificates **shall** be used.

**POL.WIFI.019:** EAP-TLS or EAP-TTLS **should** be used.

**POL.WIFI.020:** Where user or device groups have differing functions, PKI trust domains **should** be defined and used to maintain functional separation.

## MoJ special-purpose wifi networks

**POL.WIFI.021:** If MoJ devices, including IoT or legacy devices, cannot meet the general security policy requirements, or if there are non-security reasons for segregating traffic onto different SSIDs, then dedicated MoJ wifi networks **may** be created.

**POL.WIFI.022:** These dedicated networks **may** have reduced authentication controls, for example a shared PSK or a reduced ability to rotate PSKs due to form-factor limitations.

**POL.WIFI.023:** In such circumstances, special care **shall** be taken to ensure that the general network architecture and other security controls constrain network connectivity for clients. The constraints limit network connectivity to the minimum required for them to function properly.

**POL.WIFI.024:** Other mechanisms such as MAC filtering **should** be used to reduce the chance of misuse.

## MoJ guest wifi networks

Due to complexities and management effort involved in running wifi solutions, the MoJ preference is to utilise the cross-Government GovWifi service: [https://www.wifi.service.gov.uk/](https://www.wifi.service.gov.uk/).

This also has the benefit of being available across HMG Departments and Agencies. GovWifi has a level of pre-registration, monitoring and filtering in place to protect the users. However, GovWifi does not provide enterprise level security functions. GovWifi users are required to maintain their own security controls. For MoJ users of GovWifi connections, this means using the MoJ-provided VPN services when accessing protected MoJ services.

**POL.WIFI.025:** Any considerations for not using GovWifi in an MoJ guest wifi network **shall** be discussed and agreed beforehand with the cyber security team.

**POL.WIFI.026:** Where GovWifi cannot be used, or where an existing guest wifi service exists,the following **shall** be in place:

-   Regular rotation of the passphrase, with agreement from the [Security team](mailto:security@justice.gov.uk). Normally, this requires a fresh and unique passphrase each day.

-   Filtering and Monitoring for known 'bad-sites' and threats **shall** be in place at the network level.

-   Guests wishing to utilise the service **shall** first register for access, and can then be provided with the passphrase for that day.


## Logging and monitoring

**POL.WIFI.027:** Security monitoring for MoJ wireless networks **shall** be implemented, in accordance with the [MoJ security monitoring policy](logging-and-monitoring.md).

**POL.WIFI.028:** Security logging **shall** be enabled to record activity such as client access events, authentication successes and failures, client association history, and relevant information about devices and users attempting to connect to the wireless network.

**POL.WIFI.029:** In higher threat environments, security logging **should** also include identification of rogue access points, and logging of all attempted associations with the wifi network.

**POL.WIFI.030:** For MoJ guest wifi networks, but not including GovWifi, audit logs of sites accessed **shall** be retained for at least 6 months, including authentication details. This data is held to allow forensic analysis of data in the case of a security incident. No personal information except that required to conduct the analysis is logged or retained.

## Using third-party wifi

**POL.WIFI.031:** MoJ staff **shall** ensure they have permission from the network owner before using wifi that is not operated by the MoJ.

**POL.WIFI.032:** Staff **should** take [reasonable precautions](https://ico.org.uk/your-data-matters/online/wifi-security/) to check that their home wifi network is secure.

**POL.WIFI.033:** Staff **may** use work-provided mobile phones to 'tether' their MoJ-provided devices for connectivity.

**POL.WIFI.034:** Tethered connections **shall** be password protected using unique and complex passwords.

**POL.WIFI.035:** Tethering passwords for MoJ devices **shall not** be shared with non-MoJ users.

**POL.WIFI.036:** Public wifi networks or guest wifi provided at third-party sites **shall** only be used by devices which have suitable encryption for MoJ **Official** information. Here, 'suitable' means either an 'always-on full-take' VPN, or that provides appropriate application-level encryption for all services. This is currently \(October 2021\) limited to Dom1 and PTTP/MoJO laptops and mobile devices.

**POL.WIFI.037:** Staff travelling overseas **shall** follow the guidance on [Accessing MoJ IT systems from overseas](accessing-moj-it-systems-from-overseas.md) regarding the use of wifi or other networks.

## Enforcement

This policy is enforced by lower level policies, standards, procedures, and guidance.

Non-conformance with this policy could result in disciplinary action taken in accordance with the MoJ's disciplinary procedures. This could result in penalties up to and including dismissal. If an employee commits a criminal offence, they might also be prosecuted. In such cases, the department always cooperates with the relevant authorities, and provides appropriate evidence.

## Incidents

**Note:** If you work for an agency or ALB, refer to your local incident reporting guidance.

**Security Team**

-   Email: [security@justice.gov.uk](mailto:security@justice.gov.uk)
-   Slack: `#security`

## Contact details

For any further questions or advice relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

