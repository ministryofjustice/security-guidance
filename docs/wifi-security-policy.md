# Wifi security policy

## Introduction

This policy gives an overview of wireless networking \(wifi\) security principles and responsibilities within the Ministry of Justice \(MoJ\).

To help identify formal policy statements, each is prefixed with an identifier of the form: POLWIFIxxx, where xxx is a unique ID number.

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

`POLWIFI001:` Any exceptions to the policy **SHALL** be managed through the MoJ's security risk management process.

## Applicability

This policy applies to all MoJ owned or managed wifi networks provided for any purpose. It also applies to the use of third-party wifi networks by MoJ devices which handle `OFFICIAL` information, for example staff end user computing devices.

## MoJ wifi networks

`POLWIFI002:` Each MoJ wifi network **SHALL** have a defined policy which is reviewed at least annually, that describes:

-   The purpose of the wifi network.

-   The intended users of the wifi network.

-   The Service Owner of the wifi network.

-   The access controls that are applied to ensure that only those intended users can connect to the wifi network.

-   User and administrator responsibilities for maintaining the security of the wifi network.

-   Who has authority to expand or alter the wifi network.

-   Logging and monitoring requirements and responsibilities for the wifi network.


## General security requirements

The following statements apply to all MoJ-provided wifi networks.

`POLWIFI003:` Wifi networks **SHALL NOT** be treated as extensions of trusted LANs or WANs.

`POLWIFI004:` Wifi networks **SHALL** be treated as untrusted bearers for the purposes of application security.

`POLWIFI005:` All products used in an MoJ wifi network **SHALL** support WPA2-Enterprise.

`POLWIFI006:` CCMP **SHALL** be used to protect the confidentiality and integrity of information transmitted over the wifi network.

`POLWIFI007:` Other wifi security modes \(such as WEP\) **SHALL NOT** be enabled.

`POLWIFI008:` All products used in MoJ wifi networks **SHALL** support certificate-based authentication.

`POLWIFI009:` On MoJ wireless networks, isolation between wifi clients **SHOULD** be enabled. Where there is no requirement for devices to communicate directly, isolation **SHALL** be enabled.

`POLWIFI010:` MoJ wireless networks **SHOULD** use a DNS resolver that chains to the [Protective Domain Name Service \(PDNS\)](https://www.ncsc.gov.uk/information/pdns) service.

`POLWIFI011:` All MoJ wireless networking equipment **SHALL** be kept [patched and secure](vulnerability-scanning-and-patch-management-guide.md), whether connecting to MoJ wifi services or GovWifi.

`POLWIFI012:` All management of MoJ Wireless networking equipment **SHALL** be undertaken in compliance with the [Privileged User Access Guide](privileged-account-management-guide.md) and any relevant Security Operating Procedures \(SyOPS\).

## MoJ enterprise wifi networks

**Note:** MoJ enterprise wifi networks are those used solely for MoJ users and devices.

`POLWIFI013:` Pre-Shared Keys \(PSKs\) **MAY** be used for user or device authentication.

`POLWIFI014:` PSKs **SHALL** be unique per user or device.

`POLWIFI015:` PSKs **SHALL** only be implemented with prior agreement from the cyber security team

`POLWIFI016:` PSKs **SHALL** be changed at least once a year.

`POLWIFI017:` EAP-PSK **SHOULD** be used.

`POLWIFI018:` In higher-threat situations such as in a prison location where any unauthorised use of the Wireless network would constitute a security incident, mutually-authenticated authentication based on certificates **SHALL** be used.

`POLWIFI019:` EAP-TLS or EAP-TTLS **SHOULD** be used.

`POLWIFI020:` Where user or device groups have differing functions, PKI trust domains **SHOULD** be defined and used to maintain functional separation.

## MoJ special-purpose wifi networks

`POLWIFI021:` If MoJ devices, including IoT or legacy devices, cannot meet the general security policy requirements, or if there are non-security reasons for segregating traffic onto different SSIDs, then dedicated MoJ wifi networks **MAY** be created.

`POLWIFI022:` These dedicated networks **MAY** have reduced authentication controls, for example a shared PSK or a reduced ability to rotate PSKs due to form-factor limitations.

`POLWIFI023:` In such circumstances, special care **SHALL** be taken to ensure that the general network architecture and other security controls constrain network connectivity for clients. The constraints limit network connectivity to the minimum required for them to function properly.

`POLWIFI024:` Other mechanisms such as MAC filtering **SHOULD** be used to reduce the chance of misuse.

## MoJ guest wifi networks

Due to complexities and management effort involved in running wifi solutions, the MoJ preference is to utilise the cross-Government GovWifi service: [https://www.wifi.service.gov.uk/](https://www.wifi.service.gov.uk/).

This also has the benefit of being available across HMG Departments and Agencies. GovWifi has a level of pre-registration, monitoring and filtering in place to protect the users. However, GovWifi does not provide enterprise level security functions. GovWifi users are required to maintain their own security controls. For MoJ users of GovWifi connections, this means using the MoJ-provided VPN services when accessing protected MoJ services.

`POLWIFI025:` Any considerations for not using GovWifi in an MoJ guest WiFi network **SHALL** be discussed and agreed beforehand with the cyber security team.

`POLWIFI026:` Where GovWifi cannot be used, or where an existing guest wifi service exists,the following **SHALL** be in place:

-   Regular rotation of the passphrase, with agreement from the [Operational Security Team](mailto:OperationalSecurityTeam@justice.gov.uk). Normally, this requires a fresh and unique passphrase each day.

-   Filtering and Monitoring for known 'bad-sites' and threats **SHALL** be in place at the network level.

-   Guests wishing to utilise the service **SHALL** first register for access, and can then be provided with the passphrase for that day.


## Logging and monitoring

`POLWIFI027:` Security monitoring for MoJ wireless networks **SHALL** be implemented, in accordance with the [MoJ security monitoring policy](logging-and-monitoring.md).

`POLWIFI028:` Security logging **SHALL** be enabled to record activity such as client access events, authentication successes and failures, client association history, and relevant information about devices and users attempting to connect to the wireless network.

`POLWIFI029:` In higher threat environments, security logging **SHOULD** also include identification of rogue access points, and logging of all attempted associations with the wifi network.

`POLWIFI030:` For MoJ guest wifi networks, but not including GovWifi, audit logs of sites accessed **SHALL** be retained for at least 6 months, including authentication details. This data is held to allow forensic analysis of data in the case of a security incident. No personal information except that required to conduct the analysis is logged or retained.

## Using third-party wifi

`POLWIFI031:` MoJ staff **SHALL** ensure they have permission from the network owner before using wifi that is not operated by the MoJ.

`POLWIFI032:` Staff **SHOULD** take [reasonable precautions](https://ico.org.uk/your-data-matters/online/wifi-security/) to check that their home wifi network is secure.

`POLWIFI033:` Staff **MAY** use work-provided mobile phones to 'tether' their MoJ-provided devices for connectivity.

`POLWIFI034:` Tethered connections **SHALL** be password protected using unique and complex passwords.

`POLWIFI035:` Tethering passwords for MoJ devices **SHALL NOT** be shared with non-MoJ users.

`POLWIFI036:` Public wifi networks or guest wifi provided at third-party sites **SHALL** only be used by devices which have suitable encryption for MoJ `OFFICIAL` information. Here, 'suitable' means either an 'always-on full-take' VPN, or that provides appropriate application-level encryption for all services. This is currently \(October 2021\) limited to Dom1 and PTTP/MoJO laptops and mobile devices.

`POLWIFI037:` Staff travelling overseas **SHALL** follow the guidance on [Accessing MoJ IT systems from overseas](accessing-moj-it-systems-from-overseas.md) and [taking equipment overseas](general-advice-on-taking-equipment-overseas.md) regarding the use of wifi or other networks.

## Enforcement

This policy is enforced by lower level policies, standards, procedures, and guidance.

Non-conformance with this policy could result in disciplinary action taken in accordance with the MoJ's disciplinary procedures. This could result in penalties up to and including dismissal. If an employee commits a criminal offence, they might also be prosecuted. In such cases, the department always cooperates with the relevant authorities, and provides appropriate evidence.

## Incidents

**Note:** If you work for an agency or ALB, refer to your local incident reporting guidance.

**Operational Security Team**

-   Email: [OperationalSecurityTeam@justice.gov.uk](mailto:OperationalSecurityTeam@justice.gov.uk)
-   Slack: `#security`

## Contact details

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for cyber security advice, contact the Cyber Assistance Team: [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

