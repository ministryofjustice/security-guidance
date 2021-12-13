# Technical Controls Policy

**Note:** This document might refer to several organisations, information sources, or terms that have been replaced or updated, as follows:

-   CESG \(Communications-Electronics Security Group\), refer to the National Cyber Security Centre \(NCSC\), contact [security@justice.gov.uk](mailto:security@justice.gov.uk).
-   CINRAS \(Comsec Incident Notification Reporting and Alerting Scheme\), refer to the NCSC, contact [security@justice.gov.uk](mailto:security@justice.gov.uk).
-   ComSO \(Communications Security Officer\), contact the Chief Information Security Officer \(CISO\) \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   `CONFIDENTIAL`, an older information classification marking, refer to [Information Classification and Handling Policy](information-classification-and-handling-policy.md).
-   CPNI \([Centre for the Protection of the National Infrastructure](https://www.cpni.gov.uk/)\), contact the CISO \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   DSO \(Departmental Security Officer\), contact the Senior Security Advisor \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   GPG6 \(Good Practice Guide 6: Outsourcing and Offshoring: Managing the Security Risks\), refer to the NCSC, contact [security@justice.gov.uk](mailto:security@justice.gov.uk).
-   IS1 \(HMG Infosec Standard 1 Technical Risk Assessment\), refer to the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   IS2 \(HMG Infosec Standard 2 Information Risk Management\), refer to the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   IS4 \(HMG Infosec Standard 4 Communications Security and Cryptography\), refer to the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   IS6 \(HMG Infosec Standard 6 Protecting Personal Data and Managing Information Risk\), refer to the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   ITSO \(Information Technology Security Officer\), contact the CISO \([security@justice.gov.uk](mailto:security@justice.gov.uk)\).
-   `RESTRICTED`, an older information classification marking, refer to [Information Classification and Handling Policy](information-classification-and-handling-policy.md).
-   SPF \([Security Policy Framework](https://www.gov.uk/government/publications/security-policy-framework)\), refer to the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security), contact [security@justice.gov.uk](mailto:security@justice.gov.uk).

To help identify formal policy statements, each is prefixed with an identifier of the form: `POL.TCP.xxx`, where xxx is a unique ID number.

**Related information**  


[System Backup Policy](system-backup-policy.md)

[Acceptable Use Policy](acceptable-use-policy.md)

[Access Control Policy](access-control-policy.md)

[Code of connection standard](code-of-connection-standard.md)

[Information Classification and Handling Policy](information-classification-and-handling-policy.md)

[IT Incident Management Policy](it-incident-management-policy.md)

[IT Security Policy \(Overview\)](it-security-policy-overview.md)

[Malware Protection Guide - Overview](malware-protection-guide-introduction.md)

[Offshoring Guide](offshoring-guide.md)

[Passwords](passwords.md)

[Patch Management Guide](patch-management-guide.md)

[Protective Monitoring Guide](protective-monitoring.md)

[Secure disposal of IT equipment](secure-disposal-of-it-equipment.md)

[Secure disposal of IT - physical and on-premise](secure-disposal-of-it-physical-and-on-premise.md)

[Secure disposal of IT - public and private cloud](secure-disposal-of-it-public-and-private-cloud.md)

[System Lockdown and Hardening Standard](system-lockdown-and-hardening-standard.md)

[System Test Standard](system-test-standard.md)

[Use of HMG Cryptography Policy](use-of-hmg-cryptography-policy.md)

## Approach to technical controls

The Ministry of Justice \(MoJ\) relies heavily upon IT systems to support service delivery in all MoJ business groups. This policy covers the technical security controls required for all IT systems.

This document outlines the minimum baseline standard for the application of technical security controls which applies to all IT systems. Each IT system is different and it is intended that IT systems will be assessed and a judgement made on the applicability of the technical controls outlined in this policy.

`POL.TCP.001`: All IT equipment and systems **SHALL** comply with this policy, which outlines the minimum baseline standard, when considering technical security controls. This includes where appropriate, the standards, guides and procedures which support this policy.

`POL.TCP.002`: All IT systems **SHALL** provide evidence that this policy has been considered and the appropriate technical controls selected.

`POL.TCP.003`: All IT systems **SHALL** have their security architecture documented. This can be within an existing system architecture document or where appropriate within the relevant section of risk management documentation.

## Overarching objectives

The objectives of this policy are:

-   To facilitate the consistent application of technical security controls across the MoJ where similar controls and configurations are applied in a similar manner to a common standard.

-   To support business continuity by promoting standard configuration which will make it easier to re-provision or re-build systems.

-   By providing a minimum baseline technical security requirement for all IT systems, the appropriateness of those controls can be reviewed centrally against future security developments and MoJ Information Assurance strategy.

-   Reduce the cost of implementing IT systems by ensuring security considerations are considered at the start of the development process shaping the requirements and providing input into system design.


## Technical controls lifecycle

The development and operation of an IT system follows a project lifecycle from initial design through to disposal where Information Security needs to be including and considered at every stage.

`POL.TCP.004`: The selection of technical security controls **SHALL** be based on a technical risk assessment. For systems covered under the accreditation process, this is an assessment conducted following HMG Information Assurance Standard No. 1 and 2.

`POL.TCP.005`: All IT systems **SHALL** have all selected technical security controls operationally active before use in a live environment. Any exceptions are at the discretion of the system Accreditor, IAO or SIRO.

`POL.TCP.006`: All IT systems **SHALL** be tested in a Non-Live Environment \(NLE\) prior to going into live operation. This includes the testing of any security controls and features.

`POL.TCP.007`: All IT systems **SHALL NOT** use live data in system testing. Any exceptions are at the discretion of the system Accreditor and approved by the business group SIRO.

`POL.TCP.008`: All IT systems **SHALL NOT** use live personal data in system testing. Any exceptions must be approved by the IAO or SIRO, this approval process is managed by the MoJ Data Access and Compliance Unit \(DACU\).

`POL.TCP.009`: All IT systems **SHALL** enforce separation between test environments and live operational environments.

`POL.TCP.010`: All IT systems **SHALL** be tested in line with the [System Test Standard](system-test-standard.md), this includes conducting a secure code review.

### Protection of system test data

IT System test environments generally do not implement all the security controls and operating procedures present in a live operational environment. As such it is important to consider what security controls are required to protect both the system source information \(for example source files and configuration data\) and any test data utilised.

`POL.TCP.011`: Where an IT system uses live test data or test data which attracts a HMG protective marking, the system test environment or NLE **SHALL** be accredited to process data at that protective marking.

## Assurance and Compliance

The [MoJ IT Security Policy](it-security-policy-overview.md) describes how the MoJ manages information security risk and the information assurance arrangements in place to ensure that any information security controls adopted are adequate and operating correctly.

### Compliance to HMG Information Assurance Standards

For IT systems operating in an HMG environment, general security standards are provided centrally from the National Cyber Security Centre \(NCSC\) to ensure that across HMG, a consistent approach is applied.

`POL.TCP.012`: All IT systems **SHALL** ensure that they comply with HMG Information Assurance standards. This includes the assessment of technical risk, selection of controls and their implementation. The primary reference is [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).

### Technical review of operational changes

`POL.TCP.013`: All IT systems **SHALL** have all operational changes reviewed and approved by MoJ IT IA prior to any system change. This is to ensure the risk profile of a system is not significantly altered by the change and that any required technical security controls have been considered.

**Note:** An Accreditor may decide that a particular system change requires a revision to that system's accreditation. This could involve updating the risk management documentation where appropriate.

## Physical Security of IT Assets Policy

The physical environment in which an IT system is used often influences the design decisions taken regarding which technical security controls are required to attain the desired risk mitigation.

`POL.TCP.014`: The physical location and environment an IT system will operate in **SHALL** be considered when selecting technical security controls. This includes any IT equipment used in a remote working environment.

`POL.TCP.015`: Where an IT system is provided under contract, that contract **SHALL** specify the responsibilities for equipment and IT Security at any service provider, MoJ, or other third party sites used.

`POL.TCP.016`: Where IT equipment for MoJ IT systems are located at a third party site, the security of these assets **SHALL** be documented and agreed with MoJ IT IA.

Physical security is the responsibility of MoJ Corporate security and business continuity branch where further information can be found at.

`POL.TCP.016.001`: Buildings and premises used to store and process HMG protectively marked information need to meet a specified HMG standard, this includes supplier premises. MoJ Corporate security and business continuity branch **SHALL** be consulted and can provide further advice.

An example of where IT Security controls are influenced by the physical environment is where a desktop terminal \(with access to sensitive information\) is located in an area where it can be overlooked by members of the public. Supplementary technical and procedural controls are required to balance the additional risk posed.

### Cabling security

All IT systems have some form of cabling, whether it is for power, network connectivity or connections to peripheral devices.

Cabling itself needs to be protected against potential threats such as the compromise of confidentiality due to physical access \(such as unattended network ports in a public area\) or loss of availability due to power cabling running through an area which is liable to flood.

`POL.TCP.017`: Any technical risk assessment **SHALL** examine the risks associated with cabling within an IT system.

`POL.TCP.018`: All IT systems **SHALL** consider the need to separate cable trunking where justified by the Business Impact Assessment \(BIA\) and risk assessment. Further advice can be sought from MoJ Corporate security and business continuity branch.

Network cabling in particular is prone to electronic interference or interception.

### Equipment maintenance

Maintenance of IT equipment can support Information Security by ensuring systems continue to meet their integrity and availability requirements but it can also introduce new security risks.

`POL.TCP.019`: Equipment **SHALL** be appropriately maintained to ensure continued availability and integrity.

`POL.TCP.020`: All IT systems **SHALL** provide documented evidence of a maintenance regime or support arrangements. This could be within risk management documentation or referenced support agreements or contracts.

`POL.TCP.021`: Any piece of IT equipment taken offsite for maintenance or repair which may contain protectively marked data or personal information **SHALL** be approved via an operational change request by MoJ IT IA. Pieces of IT equipment which fall into this category include \(but are not limited to\):

-   Magnetic Storage Media

-   Solid State Drives

-   Optical Media

-   Digital printers, copiers, and, multi-function devices

-   Networking Equipment

-   Personal Electronic Devices


`POL.TCP.022`: Any piece of IT equipment which has been taken offsite for maintenance or repair **SHALL** be assessed and tested before integration or installation back into a MoJ IT system. This activity must be approved via an operational change request by MoJ IT IA.

**Note:** One change request can be used to cover both the removal to an offsite location and its return.

`POL.TCP.023`: Where sanitisation of a piece of IT equipment is required prior to any maintenance or repair, this **SHALL** be completed according to HMG Information Assurance Standard No. 5.

`POL.TCP.024`: All IT systems **SHALL** maintain a log of maintenance activity noting any MoJ IT IA approvals where appropriate.

On some occasions, IT equipment may be decommissioned rather than repaired.

### TEMPEST

IT systems which process or handle protectively marked information can produce unintended emanations which can compromise the information being processed or be used as a covert channel to compromise the system as a whole. This activity, its investigation, testing and suppression, is collectively known as TEMPEST within HMG.

`POL.TCP.025`: Where a technical risk assessment has indicated that TEMPEST threats pose a risk to an IT system, TEMPEST controls must be considered. The application controls **SHALL** follow CESG Good Practice Guide No. 14.

## Identity and Access Management Policy

### Access Control

Access to IT systems must be controlled on the basis of business need and security requirements. Access control rules and rights for each user or group of users must be clearly stated in an access control statement \(within risk management documentation or other referenced security documentation\) and assessed through a Business Impact Assessment \(BIA\).

For end Users, this is presented through an IT system's Security Operating Procedures \(SyOPs\). Further details are provided in the [Acceptable Use Policy](acceptable-use-policy.md).

`POL.TCP.026`: All IT systems **SHALL** provide a secure access control mechanism which can be configured to restrict access to both system functionality and information assets processed or stored.

`POL.TCP.027`: All IT systems **SHALL** use the appropriate access control mechanism based on the method of access and risk assessment \(for example, remote access where two factor authentication is assessed to be appropriate\).

`POL.TCP.028`: Access to an IT system \(and functionality provided\) **SHALL** be provided on a 'need-to-know' \(least privilege\) basis. Any additional privileges **SHALL** only be granted through a valid business case signed-off by the business system owner or a senior manager.

`POL.TCP.029`: Any access control solution **SHALL** take into consideration the [Information Classification and Handling Policy](information-classification-and-handling-policy.md).

`POL.TCP.030`: All IT systems **SHALL** define and maintain an access control schema which aligns to the [MoJ IT Security Policy](it-security-policy-overview.md).

`POL.TCP.031`: All IT systems **SHALL** follow the [Access Control Policy](access-control-policy.md).

#### User Identity Management

Management of user identities on IT systems is important to ensure access to services and information is on a 'need-to-know' basis and end users actions can be monitored and correctly attributed.

`POL.TCP.032`: All IT systems **SHALL** have a process for managing User identities covering the full lifecycle \(from creation to removal\), this includes where a User changes role or business group. This must be in line with the [Access Control Policy](access-control-policy.md).

**Note:** The lifecycle for User identities needs to be mapped onto the MoJ HR processes for new joiners and leavers. Refer to the MoJ Intranet for more information.

#### User Registration

`POL.TCP.033`: All IT systems **SHALL** have or use a formal user registration and deregistration procedure to control the allocation and removal of access rights.

`POL.TCP.034`: Each User on an IT system **SHALL** have a unique User IDs which can be used to record their actions on that system. The use of group IDs will only be considered on a case by case basis by the system Accreditor \(for example, legacy systems which may not provide the functionality for unique User IDs\).

`POL.TCP.035`: A check **SHALL** be made to ensure a User is authorised to access an IT system before being granted their access credentials \(for example, from a system owner or MoJ senior manager\). This includes ensuring only the appropriate access required by that User is granted.

`POL.TCP.036`: Users **SHALL** be made aware of their access rights to an IT system.

`POL.TCP.037`: All IT systems **SHALL** maintain a formal record of all Users registered on that system.

`POL.TCP.038`: All IT systems **SHALL** have a process for periodically checking and removing redundant User IDs and accounts.

`POL.TCP.039`: All IT systems **SHALL** ensure that a redundant User ID is not recycled and issued to other User.

#### Privilege Management

Most IT systems provide access to a number of services and information assets. In general, a particular User does not need access to every service or information asset. As such, privileges and privilege management provides a mechanism to restrict user access and enforce principles such as 'need-to-know'.

`POL.TCP.040`: The privileges associated with each component of an IT system \(e.g. operating system, database and applications\) **SHALL** be categorised and grouped together into appropriate roles which can be assigned to individual Users.

`POL.TCP.041`: Privileges **SHALL** be allocated on a 'need-to-know' \(least privilege\) basis.

`POL.TCP.042`: Where appropriate, any allocation of privileges which allows a User to perform system administrative functions **SHALL** be assigned to a different User ID from the User ID used by that User for normal business functions.

`POL.TCP.043`: Segregation of duties **SHALL** be considered in the allocation of privileges.



#### User Password Management

`POL.TCP.044`: The requirement for an IT system to be protected by a password **SHALL** be derived from a technical risk assessment \(using HMG Information Assurance Standard No. 1 and 2 for systems undergoing the accreditation process\) and a Business Impact Assessment \(BIA\).

`POL.TCP.045`: The standard on password generation, composition and management is contained within the [Password guidance](passwords.md). All IT systems which use passwords for access control **SHALL** follow this standard.

`POL.TCP.046`: All supplier or vendor supplied passwords **SHALL** be changed before live operation.

`POL.TCP.047`: All IT systems **SHALL** have a process to change any passwords which have been compromised.

Though passwords are the primary method of User authentication, other technologies for User identification and authentication, such as biometrics and hardware tokens should be considered where appropriate.

#### Review of user rights

To maintain effective control over who has access to which information assets and services, access rights and privileges need to be regularly reviewed.

`POL.TCP.048`: All IT systems **SHALL** have and follow a process to review user access rights and privileges on a regular basis and the capability to change those rights, as required, in a timely manner.

`POL.TCP.049`: All IT systems **SHALL** have the capability to provide a report on all user access rights upon request.

## Network Security Policy

Network security is a combination of security controls, the architecture in which those controls are deployed and, the processes and procedures which direct their operation.

`POL.TCP.050`: The risk assessment for an IT system **SHALL** include an assessment of the threats and vulnerabilities to or from any IT network supported by or utilised by that system.

`POL.TCP.051`: All IT systems **SHALL** implement controls to ensure the Confidentiality, Integrity, Availability and Accountability of data in transit across any networks utilised. This includes ensuring correct network routing.

`POL.TCP.052`: All IT systems **SHALL** implement controls to protect any exposed services \(i.e. those made available for use across a network\) from unauthorised access. This includes remote access services.

`POL.TCP.053`: Based on a Business Impact Assessment \(BIA\) and technical risk assessment, where appropriate as directed by the Accreditor, an IT Heath Check **SHALL** be conducted on all MoJ IT systems. The type of check conducted must be inline with the segmentation model detailed in HMG Information Assurance Standard No. 1 and 2.

`POL.TCP.054`: All IT system **SHALL** follow the MoJ Enterprise Security Architecture Framework. This framework provides details on architectural patterns for secure system design and guidance on network segregation.

### Network access control

Much like User access control, network access controls seeks to control access to network services and systems. MoJ networks are generally shared networks, with some extending across organisational boundaries and outside of the MoJ itself.

`POL.TCP.055`: All IT systems **SHALL** implement appropriate authentication mechanisms for access to network devices \(e.g. servers, printers, network storage and routers\). This includes access to devices from an internal MoJ network.

`POL.TCP.056`: Where an IT system connects to an external network, network security controls **SHALL** be implemented to enforce separation between the two networks and restrict data flow and access between the two networks.

`POL.TCP.057`: The selection and application of network access controls **SHALL** follow the MoJ Enterprise Security Architecture Framework.

## Application Security Policy

The strategy for the comprehensive application of Information Security is often described as 'Defence in Depth'. This is to say, security controls should be appropriately considered at all levels of an IT system. It is therefore important to assess what security controls need to be applied at the application level.

`POL.TCP.058`: The risk assessment for an IT system **SHALL** include an assessment of the threats and vulnerabilities to any application supported by or utilised by that system.

`POL.TCP.059`: All software applications which form an IT system **SHALL** be patchable and supported.

`POL.TCP.060`: Commercial Off The Shelf \(COTS\) supplied software **SHALL** be maintainable with appropriate support arrangement/agreements in place based on an IT system's risk assessment.

`POL.TCP.061`: Where an application is developed for the MoJ \(i.e. is not COTS products\), a defined process for identifying and rectifying security issues **SHALL** be established.

`POL.TCP.062`: Where applicable, an application **SHALL** be within the scope of an IT system's IT Health Check \(ITHC\).

`POL.TCP.063`: All IT systems **SHALL** follow the MoJ Enterprise Security Architecture Framework. This framework provides details on standard security features and secure development practices which must be considered.

## Protective Monitoring Policy

All IT systems are monitored to detect non-conformance to policy and record auditable events providing evidence to help diagnose and investigate security incidents.

`POL.TCP.064`: All IT systems **SHALL** provide the capability to audit events whether initiated by a User or system process.

`POL.TCP.065`: All IT systems **SHALL** implement a set of audit points which are in accordance with the [Protective Monitoring Guide](protective-monitoring.md).

`POL.TCP.066`: All IT systems **SHALL** be included in a protective monitoring solution. The level of monitoring required must be determined using HMG Information Assurance Standard No. 1 and 2, and CESG Good Practice Guide No. 13.

`POL.TCP.067`: All audit logs **SHALL** be securely stored to protect the confidentiality of the data contained.

`POL.TCP.068`: All IT systems **SHALL** implement controls to protect the integrity of audit and accounting logs.

`POL.TCP.069`: All IT systems **SHALL** synchronise all IT devices with a consistent time source.

`POL.TCP.070`: All audit and accounting logs **SHALL** be retained in accordance with stated data retention period as expressed by Information Asset Owner \(IAO\) and recorded in the system risk management documentation \(refer to the [logging and monitoring](logging-and-monitoring.md#) information\).

`POL.TCP.071`: All IT systems **SHALL** follow the [Protective Monitoring Guide](protective-monitoring.md), where further guidance is provided.

### Interface with Operational Security

The [Operational Security Team](mailto:OperationalSecurityTeam@justice.gov.uk) \(OST\) at the MoJ is responsible for managing security incidents involving MoJ IT systems and information assets. As such, they are the primary consumer of any protective monitoring solution as it is a key feed of information and mechanism for raising security incidents.

`POL.TCP.072`: All protective monitoring solutions **SHALL** provide the capability to report security incident \(or the audit and log data which can be used to generate security incidents\) to the MoJ Operational Security team.

`POL.TCP.073`: All IT systems **SHALL** provide their audit logs to the MoJ Operational Security Team \(OST\) upon request.

Further information on IT incident management is available in [IT Incident Management Policy](it-incident-management-policy.md).

## Connection with 3rd Party Systems Policy

Working with other Government departments and establishing partnerships with other organisations is common practice at the MoJ.

In the context of this policy, the definition of a 3rd party system is any system which is not a MoJ internal network. Therefore, a 3rd party connection is a connection between a MoJ internal network or system and an external network or system for system-to-system data transfers. This includes other Government department using the GSi.

Where there is a business need for such third party access, a risk assessment needs to be carried out to determine the security implications and control requirements. Security controls must be agreed and defined in an agreement or contract with the third party before a connection is provided.

`POL.TCP.074`: All IT systems which connect to a 3rd party system or share information with any 3rd party **SHALL** include the following in the technical risk assessment:

-   Access to information assets by 3rd parties;

-   Compliance to applicable legal or regulatory requirements;

-   Security of network connection;

-   Business continuity.


`POL.TCP.075`: All IT systems which connect to or share information with a 3rd party system **SHALL** ensure a Code of Connection is drawn up, understood and signed by each connected parties Information Asset Owner \(IAO\). An Information Sharing Agreement is also required.

`POL.TCP.076`: Where 3rd party access involves other participants, for example subcontractors, this **SHALL** be brought to the attention of the system Accreditor for approval where any agreements made with the 3rd party will also be considered applicable to any further participants.

`POL.TCP.077`: Where an IT system is connected to a 3rd party for the purposes of offshoring, it **SHALL** comply with [Offshoring Guide](offshoring-guide.md).

`POL.TCP.078`: Any Codes of Connection **SHALL** comply with [Code of connection standard](code-of-connection-standard.md).

### Security of 3rd party access

When connecting to a 3rd party system, the security controls deployed on either side of the connection need to be considered and assessed.

`POL.TCP.079`: A process **SHALL** be defined for controlling and notifying transmission, despatch and receipt of data to/from a 3rd party.

`POL.TCP.080`: An agreed protective marking system **SHALL** be used for all data transfers. By default, this is the HMG protective marking system.

`POL.TCP.081`: All IT systems which connect to or share information with a 3rd party system **SHALL** ensure that adequate security controls are in place to:

-   Protect against virus or malware infiltration and malicious attack;

-   Provide adherence to [Acceptable Use Policy](acceptable-use-policy.md) and [Information Classification and Handling Policy](information-classification-and-handling-policy.md) where applicable.


`POL.TCP.082`: All connections **SHALL** meet the minimum technical standard detailed in the [Code of Connection Standard](code-of-connection-standard.md). Where HMG cryptographic material is required, additional policy requirements are detailed in the [Use of HMG Cryptography Policy](use-of-hmg-cryptography-policy.md).

## Secure storage and processing of Information Assets

The HMG protective marking system defines how information needs be labelled and handled. Further information on the marking system can be found in [Information Classification and Handling Policy](information-classification-and-handling-policy.md).

`POL.TCP.083`: All IT systems which handle HMG protectively marked or personal data **SHALL** be accredited to the assessed Business Impact Level \(BIL\) as captured in a Business Impact Assessment \(BIA\). Any exceptions are at the discretion of the system Accreditor.

`POL.TCP.084`: All Users of an IT system **SHALL** be aware of the protective marking which the system is operating at. Where it is not feasible to label each screen viewed by a user which contains protectively marked information, a message **SHALL** be displayed on successful log-on advising the user of the protective marking of the information held on that system.

`POL.TCP.085`: All electronic outputs from an IT system containing protectively marked information **SHALL** carry the appropriate protective marking. This includes MS Word documents, e-mails and system-to-system data transfers.

### Aggregation policy

`POL.TCP.086`: The risk assessment of an IT system **SHALL** consider the business impact should the aggregated sum of data held on system be compromised \(in terms of Confidentiality, Integrity and Availability\). This assessment must be made with reference to HMG Information Assurance Standard No. 6 and CESG Good Practice Guide No. 9.

### Personal Data

HMG outlines specific requirements on the protection of personal data as documented in HMG Information Assurance Standard No. 6. All Government departments need to follow these requirements to ensure personal data is correctly stored, processed and handled on MoJ IT systems.

`POL.TCP.087`: The definition of personal data is derived from HMG Information Assurance Standard No. 6. Any information assets in an IT system assessed as personal **SHALL** be labelled, as a minimum, `OFFICIAL-SENSITIVE`.

**Note:** Further details on the application of an HMG protective marking is provided in the [Information Classification and Handling Policy](information-classification-and-handling-policy.md).

## Use of Cryptographic Controls

HMG cryptographic material is used within MoJ IT systems mainly to secure communications with IT assets which are not directly connected to a MoJ network, for example remote access laptop. HMG maintains strict requirements and controls over the deployment and use of HMG cryptographic material which the MoJ has to follow.

`POL.TCP.088`: Any IT system which utilises HMG cryptographic material in any technical security controls \(e.g. VPN solution\) **SHALL** conform to the [Use of HMG Cryptography Policy](use-of-hmg-cryptography-policy.md).

## Secure System Build and Configuration Policy

### Capacity planning

IT system managers need to monitor their system and network usage so that they are able to provide an early warning of any potential capacity shortages, bottlenecks, or overcapacity.

`POL.TCP.089`: All IT systems **SHALL** consider capacity planning during system design and operation to ensure continued availability.

`POL.TCP.090`: Capacity planning **SHALL** take account of the need for current and future audit and logging requirements.

`POL.TCP.091`: All IT systems **SHALL** monitor system and network usage and provide the capability to detect potential capacity issues or bottlenecks.

`POL.TCP.092`: All IT systems **SHALL** report any potential capacity issues to Service Management preferably in advance of any immediate issues.

### Patching policy

Patches and Service Packs, in general, are updates to software or firmware to fix a bug or provide additional functionality. A security patch is a change typically applied to a software asset to correct a vulnerability which if exploited could compromise that asset and others on an IT system or wider network.

It is important to ensure IT systems are kept up to date with the latest security patches as any known vulnerability is highly likely to be exploited by a threat source.

`POL.TCP.093`: All IT systems, including operating systems and applications, **SHALL** be subject to a security vulnerability patching regime consistent with the level of criticality of the IT system to the business in accordance with the [Patch Management Guide](patch-management-guide.md).

`POL.TCP.094`: Security patches **SHALL** be applied in a timely manner according to their categorisation in accordance with the [Patch Management Guide](patch-management-guide.md).

`POL.TCP.095`: All IT systems **SHALL** have a Patch Management Plan. This plan must include a process for managing, testing and deploying security patches. Further details are available in the [Patch Management Guide](patch-management-guide.md).

The [Patch Management Guide](patch-management-guide.md) provides the MoJ baseline standard and template patch management plan. This standard provides details of patch categorisation \(based on the severity of the vulnerability and criticality of update\) and the expected timescales for applying a particular patch based on its categorisation.

### Lockdown policy

`POL.TCP.096`: All unnecessary or unused applications, services \(including system services\) and functionality **SHALL** be removed or disabled from all IT systems.

`POL.TCP.097`: Where applicable, Government Assurance Pack \(GAP\) **SHALL** be considered for MS Windows based systems.

`POL.TCP.098`: All IT desktop and server hardware **SHALL** be locked down to remove, prevent or limit access to non-business critical communication ports \(e.g. USB port\), removable media drives \(e.g. CD Drive\) and network communication interfaces \(e.g. infrared or Bluetooth\).

`POL.TCP.099`: All IT desktop and server hardware **SHALL** be built using a standard build, where possible, where the security of the build has been assessed and approved by MoJ IT IA.

`POL.TCP.100`: All IT systems **SHALL** be locked down in accordance with [System Lockdown and Hardening Standard](system-lockdown-and-hardening-standard.md). This standard describes general lockdown procedures supplemented by system specific procedures. For example, a set of specific procedures for MS Windows based application servers.

### Protection from malicious code

Preventative measures are required to detect and defend against the introduction of malicious code, and to protect against mobile code threats \(for example JavaScript or ActiveX code executing malicious code in a web browser\).

Software and information processing facilities are vulnerable to the introduction of malicious code, such as computer viruses, network worms, Trojan horses and logic bombs.

`POL.TCP.101`: All IT systems **SHALL** have an anti-virus client installed on each desktop and/or server configured to conduct regular anti-virus scans with real-time scanning activated.

`POL.TCP.102`: All anti-virus clients **SHALL** be updated with the latest virus definitions to a schedule outlined in the [Malware Protection Guide](malware-protection-guide-introduction.md). The default limit is within 4 hours of release by the anti-virus client vendor.

`POL.TCP.103`: All imports and exports to an IT system received from an external network or via removable media must be scanned for viruses and malware prior to being loaded on that system. This includes e-mails as well as system-to-system transfers.

`POL.TCP.104`: All IT systems **SHALL** have a procedure to report any virus or malware instances. As standards, this must be an alert to the User and to MoJ Operational Security \(OST\).

`POL.TCP.105`: All IT systems **SHALL** refer to the [Malware Protection Guide](malware-protection-guide-introduction.md) when selecting security controls to protect against malicious code and threats from mobile code.

**Note:** All malicious code instances must be recorded as an IT Security incident. Further details are provided in [IT Incident Management Policy](it-incident-management-policy.md).

#### Covert channels and Trojan code

A covert channel is where information can be exposed by an indirect or obscure method. Trojan code is designed to change the way an application or system operates in a way that it appears to be operating normally however it contains code which can perform unauthorised actions.

`POL.TCP.106`: All IT systems **SHALL** be analysed for potential covert channels which are either present in the system design or exposed through any of the applications hosted.

`POL.TCP.107`: Where a risk assessment indicates that Trojan code is a threat, all applications hosted by an IT system **SHALL** be tested for potential Trojan code.

Further details and guidance on the prevention of covert channels and Trojan code in application can be found in the MoJ Enterprise Security Architecture Framework.

### Data Backup

Data back-up arrangements for IT systems support the overall business continuity plans of the MoJ.

`POL.TCP.108`: All IT systems **SHALL** have back-up procedures to maintain the integrity and availability of all Information Assets held. This must align to the Recovery Point Objective which may be expressed in the Business Impact Assessment \(BIA\).

`POL.TCP.109`: All IT systems **SHALL** maintain a log of all back-ups taken.

`POL.TCP.110`: Back-up data **SHALL** be stored and handled in a manner appropriate to the protective marking of the Information Assets stored.

`POL.TCP.111`: All IT systems **SHALL** check all historic back-ups regularly to ensure that they can be relied upon. This includes the testing of back-up media such as tape or hard disks.

`POL.TCP.112`: All IT systems **SHALL** have a back-up restoration procedure which is tested regularly. Ideally, the testing takes place automatically.

`POL.TCP.113`: The retention period for historic back-ups **SHALL** align to the retention period of the Information Assets held.

`POL.TCP.114`: All IT systems **SHALL** conform to the [System Backup Policy](system-backup-policy.md).

## Electronic Messaging Policy

### Electronic mail \(E-Mail\)

E-mail presents a number of security challenges as it provides a channel for malware proliferation and for the exfiltration of sensitive information assets out of the MoJ either accidentally or maliciously.

**Note:** The following policy statements are applicable to IT systems which are either, an e-mail system, or, make use of e-mail services provides by another system.

`POL.TCP.115`: All e-mails sent or received external to an MoJ IT network **SHALL** be examined for potential viruses \(or malware\) and its content inspected for adherence to the [Acceptable Use Policy](acceptable-use-policy.md) and [Information Classification and Handling Policy](information-classification-and-handling-policy.md) where applicable.

`POL.TCP.116`: All IT systems which process e-mails must make provision to detect incorrect addressing or misdirection.

`POL.TCP.117`: All e-mail group distribution lists \(e.g. MoJ ZZ distribution lists\) **SHALL** be configured with a local address for internal distribution only. The use of an external address must be supported by a valid business case and is subject to approval by the MoJ ITSO.

Further details on the secure operating procedures applicable to the use of email are provided in the [Acceptable Use Policy](acceptable-use-policy.md).

## Configuration Management Policy

Configuration management is important to maintaining the operational security of live IT systems and ensuring any changes or disposal of assets is conducted in a secure manner.

`POL.TCP.118`: All IT system configurations **SHALL** be fully documented and version controlled.

`POL.TCP.119`: All IT systems **SHALL** maintain an asset inventory covering all hardware and software assets.

`POL.TCP.120`: All IT operational changes, system changes or upgrades **SHALL** be approved by MoJ IT IA prior to any change or upgrade taking place.

### IT Asset disposal policy

IT assets at their end of life can contain data, system design or configuration details can be used to compromise MoJ IT systems in addition to potentially compromising the Confidentiality of MoJ information assets held.

`POL.TCP.121`: All IT systems **SHALL** have an asset decommissioning and disposal procedure.

`POL.TCP.122`: All IT system **SHALL** seek approval from MoJ IT IA before any disposal or decommissioning activity takes place.

`POL.TCP.123`: Disposal of IT assets **SHALL** be in conformance to [Secure disposal of IT equipment guide](secure-disposal-of-it-equipment.md).

## Compliance with Legal Requirement

A number of pieces of legislation are relevant to Information Assurance \(IA\). To avoid breaches of any criminal and civil law all relevant statutory, regulatory and contractual requirements need to be considered when applying any technical security controls.

`POL.TCP.124`: All IT systems **SHALL** consider applicable legal and regulatory requirement when selecting, designing and operating any security controls. This consideration must be documented. This consideration must be document \(for example in a system design document and/or RMADS\).

Applicable pieces of legislation may include \(but is not limited to\):

-   The Computer Misuse Act, 1990

-   The Copyright, Designs and Patents Act 1988

-   The Data Protection Act 1998

-   The Official Secrets Act 1989

-   The Public Records Acts 1958 and 1967

-   Freedom of Information Act 2000

-   Human Rights Act 1998

-   Regulation of Investigatory Powers Act 2000

-   Civil Evidence Act 1968 and Police and Criminal Evidence Act

-   Wireless Telegraphy Act 1949

-   The Communication Act 2003


## Contact details

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for security advice, contact the Cyber Assistance Team [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

