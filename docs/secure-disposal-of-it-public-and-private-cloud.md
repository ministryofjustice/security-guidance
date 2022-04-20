# Secure disposal of IT - public and private cloud

This document is the Ministry of Justice \(MoJ\) IT Disposal of Equipment Guidance covering:

-   Data sanitisation and deletion within a public or private cloud environment that a Service Provider hosts.

-   The decommissioning of Storage Area Network \([SAN](https://en.wikipedia.org/wiki/Storage_area_network)\) and Virtual Machine \([VM](https://en.wikipedia.org/wiki/Virtual_machine)\) based technology.


It is designed to ensure the confidentiality of MoJ data remains when a cloud service is decommissioned.

This information is part of the MoJ asset management policies and guidance on [media handling](cyber-and-technical-security-guidance.md#).

**Note:** For disposal of physical on-premise media and data, refer to the [Secure disposal of IT - physical and on-premise](secure-disposal-of-it-physical-and-on-premise.md) guidance.

**Parent topic:** [Secure disposal of IT equipment](secure-disposal-of-it-equipment.md)

**Related information**  


[Secure disposal of IT equipment](secure-disposal-of-it-equipment.md)

[Secure disposal of IT - physical and on-premise](secure-disposal-of-it-physical-and-on-premise.md)

[Secure disposal of IT - public and private cloud](secure-disposal-of-it-public-and-private-cloud.md)

[Technical Controls Policy](technical-controls-policy.md)

## MoJ cloud environments overview

The MoJ consumes several public \(shared cloud\) and private cloud platforms, operating over 900 different technology systems ranging from internal IT tools or solutions to case management solutions.

Public cloud service environments are delivered through the internet. They are shared across organisations using a "multi-tenant" model. For example, a service provider hosts a public environment that gives the MoJ and other customers a portion of the same physical server hardware to run their website or application.

Private cloud environments differ, as they are dedicated to a single tenant. They are intended to address concerns on data security. They may also offer greater control because resources are not shared with other tenants.

Public and private clouds both have different ways of ensuring compliance. Therefore, compliance should be evaluated using the government's [Cloud Security Principles](https://www.ncsc.gov.uk/collection/cloud-security/implementing-the-cloud-security-principles). In addition, these principles should be assessed against several other factors outlined in the government's technical guidance on [securing your cloud environment](https://www.gov.uk/service-manual/technology/securing-your-cloud-environment#finding-a-secure-cloud-provider).

## NCSC on sanitisation and disposal of cloud assets

MoJ asset owners or administrators **SHOULD** be confident that:

-   All data stored in a cloud service are erased when resources are moved or re-provisioned, when the resources are no longer required, or when the asset owner requests or carries out the erasure of the data.

-   Storage media that has held MoJ data is sanitised or securely destroyed at the end of its life.


**Note:** For more information on this approach, refer to NCSC guidance on the [sanitisation of cloud assets](https://www.ncsc.gov.uk/collection/cloud-security/implementing-the-cloud-security-principles/asset-protection-and-resilience#sanitisation).

### Equipment destruction

MoJ asset owners or administrators **SHALL** ensure that for all data stored in a cloud service:

-   All equipment containing MoJ data, credentials, or configuration information for the service is identified at the end of its life and before it is recycled.

-   Any components containing sensitive data are sanitised, removed, or destroyed.

-   Accounts or credentials specific to redundant equipment are revoked to reduce their value to an attacker.


**Note:** For more information on this approach, refer to NCSC guidance on [equipment disposal.](https://www.ncsc.gov.uk/collection/cloud-security/implementing-the-cloud-security-principles/asset-protection-and-resilience#disposal)

## Checklist for the sanitisation and disposal of cloud assets

Due to the possible lack of control of physical infrastructure, a checklist of questions to ask a cloud provider to establish a baseline for data sanitisation and deletion is provided.

|Reference|Action to help ensure sufficient data sanitisation and deletion with a cloud provider|
|---------|-------------------------------------------------------------------------------------|
|1.|A standardised process to be agreed including credible witnesses, describing how private/public cloud service providers store and handle hard disks for decommissioning until destruction. This **SHALL** be aligned to the following controls as outlined in ISO 27002: 8.3.1 - Management of removable media \(Control\) "Procedures **SHOULD** be implemented for the management of removable media in accordance with the classification scheme adopted by the organization." 11.2.7 - Secure Disposal or re-use of equipment \(Control\) "All items of equipment containing storage media **SHOULD** be verified to ensure that any sensitive data and licensed software has been removed or securely overwritten prior to disposal or re-use."|
|2.|Standardised procedures agreed between the MoJ and the Cloud Provider to establish a chain of custody including [crypto-shredding](https://en.wikipedia.org/wiki/Crypto-shredding) or an initial software erasure and then degaussing the disk and/or shred/incinerate/pulverise. This **SHALL** be aligned to the following control as outlined in ISO 27002: 8.3.2 - Disposal of media \(Control\) "Media **SHOULD** be disposed of securely when no longer required, using formal procedures."|
|3.|If required, the cloud provider agrees they **SHALL** [securely deliver in transit](secure-disposal-of-it-physical-and-on-premise.md#transporting-data-between-sites-securely) hard disks that contain MoJ data, which the MoJ **SHALL** destroy.|
|4.|Optionally, MoJ asset owners using the responses to checklists 1 to 3 can establish a data sanitisation strategy SLA aligned to [Data Security Lifecycle Management](https://downloads.cloudsecurityalliance.org/assets/research/security-guidance/security-guidance-v4-FINAL.pdf) standards, specifically sanitisation and destruction \(end of life\).|

**Note:** The Data Security Lifecycle Management concept is described in the Cloud Security Alliance's Security Guidance for Critical Areas of Focus in Cloud Computing v4.0 \([CCA CSM v4.0](https://downloads.cloudsecurityalliance.org/assets/research/security-guidance/security-guidance-v4-FINAL.pdf)\). Refer to section 5.1.2: The Data Security Lifecycle on page 62.

**Note:** To ensure that MoJ data in the cloud is sanitised sufficiently and that the devices or hard drives they are stored in meet data management security standards when destroyed, it might require specific clauses in the contract with the cloud provider.

**Note:** If the cloud provider has a mechanism for resilience or redundancy that duplicates MoJ data, this duplicated data **SHALL** also be sanitised or destroyed using the checklist provided. All duplicated data **SHALL** be sanitised at the same time. The MoJ destroys all decryption keys held in their possession to ensure this occurs. This makes all the duplicated cloud data unreadable. This method is called [crypto-shredding](https://en.wikipedia.org/wiki/Crypto-shredding).

When duplicates of data cannot be destroyed immediately, there **SHALL** be methods in place for protecting and controlling the data until data destruction is assured. This includes the supplier providing a formal [declaration](data-destruction-instruction-and-confirmation-letter.md#supplier-declaration) of destruction. If any destruction tasks are delayed, a confirmation date of final data destruction **SHALL** be provided.

## Data deletion - Verification for virtual devices and SAN allocations \(public cloud or on-prem\)

When working on an MoJ public cloud or on-premise virtual infrastructure, obtaining a decommissioning or destruction certificate cannot be carried out according to the method used for the MoJ's [on-premise physical servers and disk arrays](secure-disposal-of-it-physical-and-on-premise.md#data-destruction-verification) when they are wiped, blanked, destroyed, or overwritten. This is because these MoJ infrastructures might be needed to support other services or infrastructure still in use.

For example, a single on-premise physical server might host eight virtual servers providing various services. If three of these virtual servers are deleted, the other five need to continue to operate. Similarly, an on-premise firewall might have a virtual context or a subset of rules that need to be removed, but the physical equipment is still required to provide services to other devices.

A soft and hard decommissioning approach for MoJ on-prem virtual devices might also be required. A soft decommissioning involves switching off the resource, ensuring that it cannot restart on a scheduled basis. This means stopping all hosted service or application, powering down the resource, and setting any remaining firewall rules to block all traffic to or from the resource. Once this soft decommissioning is complete, a hard decommissioning can take place. Hard decommissioning involves deleting the configuration, images, and storage that the virtual devices used and returning the resources to a resource pool.

The process used for SAN or VM items destruction and decommissioning is described next.

![A picture showing a flow of tasks to dispose of equipment within cloud systems. Step 1 is to install recording software. Step 2 makes sure that an official witness can observe the operator terminal that will be used to dispose of the equipment. Recording starts. Step 3 is where an encryption key is prepared, then stored in a secure location. Step 4 describes the various operator processes, beginning with a review of the steps to follow. For each equipment object, a check is made whether it needs to be retained for policy reasons. If so, no further action is required for that object. If deletion of the object is required, this takes place through the operator terminal and is observed by the witness. Step 5 is where all applicable objects have been either deleted or marked for retention. The recording is finished. A copy of the recording is placed in the secure location. Step 6 is the last step. The witness affirms that all applicable objects have been addressed. A decommissioning certificate is issued. Copies of the witness affirmation and the decommissioning certificate are placed in the secure location.](images/cloud-disposal.png)

1.  Install a screen recording tool on the operator's terminal. In cases where it is impossible to install a recording tool on a device, screenshots showing before and after states are acceptable if agreed in advance.

2.  Ideally, have a witness sit next to the operator and start the screen recording tool. If this is not possible, the witness can view the screen recording after the decommissioning activity.

3.  Encryption keys for the solution **SHOULD** be archived for backup retention purposes, if necessary, onto a secure storage space.

4.  For each of the given technologies, the operator **SHOULD** create an initial listing of the resource, then run the decommissioning task, then finish by creating another listing to show that the change has occurred.

    1.  Depending on the process used to create or maintain backups, some jobs might need to be removed. However, backups **SHOULD NOT** be deleted without consulting the retention policy and confirming that deletion is compliant with policy. This check applies to all decommissioning steps.

    2.  The operator, if possible, formats the SAN areas used for the files and "zero's" them by overwriting all storage with binary 0 data. The operator then deletes the various SAN [LUNs](https://en.wikipedia.org/wiki/Logical_unit_number), Arrays, Volumes, and other storage units in the SAN. Each of the storage units is reallocated to free space. This is then verified with listings of the SAN structure.

    3.  Any virtual machines are permanently deleted in the virtual machine control panel. An attempt **SHOULD** be made to list and restart the machine; this should provide evidence that the virtual machine has been permanently removed.

    4.  Any firewall or other Security Enforcing Functionality \(SEF\) configurations **SHOULD** be removed from the live service.

    5.  Any switch configurations, such as IP addresses or subnet masks, **SHOULD** be removed.

5.  Screen recording is stopped.

6.  Witness signs the decommissioning certificate, and the screen recording is stored in a secure storage space.


**Note:** There are free versions of screen recorder tools that might be used. The tool **SHALL** be assessed, before use, by requesting an MoJ security team review using this [form](https://docs.google.com/forms/d/e/1FAIpQLSeEEBDS1HBF7meUk3SjgkqxbXBQlKAiBAezJIbKHnEjfNjBTg/viewform?gxids=7628). Refer to the MoJ guidance on [requesting that an app be approved for use](general-user-video-and-messaging-apps-guidance.md#requesting-that-an-app-be-approved-for-use). An alternative option would be to use Teams to record the decommissioning via screen share.

## Contact details

For any further questions or advice relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

