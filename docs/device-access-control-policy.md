# Device Access Control Policy

This policy gives an overview of device access control security principles and responsibilities within the Ministry of Justice \(MoJ\). It provides a summary of the policies and guides that apply to MoJ device access management.

To help identify formal policy statements, each is prefixed with an identifier of the form: `POLDACPxxx`, where xxx is a unique ID number.

**Note:** For the purposes of this policy, "network" or "networks" refers to MoJ protected networks.

**Parent topic:** [Access Control Policy](access-control-policy.md)

**Related information**  


[Enterprise Access Control Policy](enterprise-access-control-policy.md)

[User Access Control Policy](user-access-control-policy.md)

[Technical Controls Policy](technical-controls-policy.md)

## Audience

This policy is aimed at:

<a name="technical-users"></a>

-   **Technical users**

    These are in-house MoJ Digital and Technology staff responsible for implementing controls throughout technical design, development, system integration, and operation. This includes DevOps, Software Developers, Technical Architects, and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI, and Knowledge \(EPICK\) Team.

<a name="service-providers"></a>

-   **Service Providers**

    Defined as any other MoJ business group, agency, contractor, IT supplier, and partner who in any way designs, develops or supplies services \(including processing, transmitting and storing data\), for or on behalf of the MoJ.

<a name="general-users"></a>

-   **General users**

    All other staff working for the MoJ.


"All MoJ users" refers to General users, Technical users, and Service Providers, as defined previously.

## Policy Sections

This policy aligns to industry standards and frameworks, and is divided into three security categories \(and subsections describing the controls\) addressing:

1.  Business Requirements of Device Access Controls.
2.  Relevant Device Controls.
3.  Device Access Control Management.

## Best Practice Framework - IAAA

Identification, Authentication, Authorisation, and Accounting \(IAAA\) are the core principles of an Access Control Policy. The principles apply to all security categories described in this policy, as follows:

<a name="identification"></a>

-   **Identification**

    `POLDACP001:` Devices **SHALL** provide a unique ID that is presented on access to networks.

<a name="authentication"></a>

-   **Authentication**

    `POLDACP002:` To access MoJ networks, devices **SHALL** be authenticated.

<a name="authorisation"></a>

-   **Authorisation**

    `POLDACP003:` Specifying access rights to devices **SHALL** be in accordance with the [Device Access Provisioning](#device-access-provisioning) guidance.

<a name="accounting"></a>

-   **Accounting**

    `POLDACP004:` Successful and unsuccessful device attempts to access networks **SHALL** be recorded in logs.


**Note:** If any of the controls within this policy cannot be applied, they are considered an exception to be assessed for inclusion within a risk register.

## Business Requirements of Device Access Control

The MoJ's business or strategic requirements are to control, limit, and manage device access to MoJ networks as described in the following subsections.

### Device Access Control Policy

`POLDACP005:` This device access control policy **SHALL** be established and maintained, based on business and information security requirements, to inform associated standards, configurations, and guidance, for all devices.

`POLDACP006:` The policy **SHALL** also follow the additional principles of:

-   "Need-to-know".
-   Least privilege.
-   Device access control.

### Access to Protected Networks

This subsection aligns to the principle of least access, to protect a network which is covered in other areas of this policy, specifically:

-   Authorisation procedures for showing which device is allowed to access which network.
-   Management controls and procedures to prevent unauthorised access, and for the provision of real-time monitoring.

## Device Access Control

`POLDACP007:` The MoJ **SHALL** strive to prevent unauthorised access by devices to networks, as described in the following subsections.

### Authentication Procedures

`POLDACP008:` Where required by the access control policy, device access to networks **SHALL** be controlled by a secure device authentication procedure.

`POLDACP009:` Multiple devices **SHALL NOT** share the same authentication certificate.

### Credential Management System

`POLDACP010:` Device credentials **SHALL** expire after a period of time.

`POLDACP011:` The maximum allowable lifetime for a device certificate **SHALL** be defined.

`POLDACP012:` If credentials expire or are revoked, access **SHALL** be disallowed until new credentials are obtained.

**Note:** By exception, a device **MAY** be allowed to connect in order to renew credentials.

## Device Access Management

Device access management ensures authorised device access and prevents unauthorised access to networks. These are described in the following subsections.

### Device Registration and de-registration

`POLDACP013:` A formal device registration and de-registration process **SHALL** be implemented to enable device access.

### Device Access Provisioning

`POLDACP014:` A formal device access provisioning process **SHALL** be implemented to assign or revoke access rights for all devices to all networks.

Specifically, for the MoJ, this includes:

-   `POLDACP015:` All MoJ network access **SHALL** employ adequate authentication techniques to identify the connecting device with confidence, where that device requires access to MoJ networks. Refer to the [Authentication](authentication.md) guidance.
-   `POLDACP016:` Administrators **SHALL** maintain the device access service, with failure to manage successfully leading to potential compromise of the network.

    **Note:** Administrators consist of all those involved in the provision of the device, or network services and capabilities, including third parties contracted to the MoJ such as Service Providers.

-   `POLDACP017:` Administrators **SHALL** maintain an active list of all active and suspended devices, and maintain their access control to networks.
-   `POLDACP018:` Access provisioning **SHALL** be implemented, adjusted, and revoked as described in associated Device Provisioning Guides for each class of network subject to access control under this Policy.

### Management of Device Certificates

`POLDACP019:` The allocation of certificates **SHALL** be controlled through a formal management process.

### Removal or Adjustment of Device Access Rights

The removal or adjustment of device access rights is covered in this policy under [Device Access Provisioning](#device-access-provisioning).

## Enforcement

-   This policy is enforced by lower-level policies, standards, procedures, and guidance.
-   Non-conformance with this policy could result in disciplinary action per the department's disciplinary procedures. This could result in penalties up to and including dismissal. If an employee commits a criminal offence, they may also be prosecuted. In such cases, the department will always co-operate with the relevant authorities and provide appropriate evidence.

## Contact details

For any further questions or advice relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

