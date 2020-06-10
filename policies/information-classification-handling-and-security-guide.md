---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](../..)

# Information Classification, Handling and Security Guide

## Introduction

All MoJ employees interact with information and are responsible for its protection. Digital and Technology will need to consider information security in the process of designing, maintaining and securing the MoJ’s IT systems used to process information.

However, not all information warrants the strictest levels of protection. This is why information classification is so important to the MoJ – to ensure that the department can focus its security efforts on its most sensitive information. Information security must be proportionate to the security classification of the information and must be considered throughout the information lifecycle to maintain its confidentiality, integrity and availability.

## Classifying information

The three information security classifications the MoJ uses are OFFICIAL, SECRET and TOP SECRET and follow the [HMG Security Classifications Policy](https://www.gov.uk/government/publications/government-security-classifications).

Each information security classification has a minimum set of security measures associated with it that need to be applied. These security measures may change depending on the information lifecycle stage.

| Classification | Description |
|--- |---|
| **OFFICIAL** | All information related to routine business, operations and services. If this information is lost, stolen or published it could have damaging consequences but is not subject to a heightened threat profile. |
| **SECRET** | Very sensitive information that requires protection against highly sophisticated, well-resourced and determined threat actors. For example, where compromise could seriously damage military capabilities, international relations or the investigation of a serious crime. |
| **TOP SECRET** | Exceptionally sensitive information that directly supports (or threatens) the national security of the UK or its allies and requires extremely high assurance of protection from all threats. |

Securing the MoJ’s information must be done with a combination of information security measures:

| Type of Measure | Description |
|--- |---|
| **PERSONNEL** | Personnel should be aware of their security responsibilities and in turn acquire security clearances and undertake training to support the MoJ’s information security objectives. |
| **PHYSICAL** | Tangible measures that prevent unauthorised access to physical areas, systems or assets. |
| **TECHNICAL** | Hardware or software mechanisms that protect information and IT assets. |

It is important to understand that security classification is determined by the level of risk in case of loss or unauthorised access and not by the type of information.

It is the responsibility of the Data Owner to classify the data.

**Examples**

 - Most production data will be OFFICIAL information. Within this, some production data may be classified as SECRET information.
 - Most personal data will be OFFICIAL information. Within this, some personal data may be classified as SECRET information if it meets the risk threshold defined.

The table below sets out the definitions for each security classification as well as whether it is necessary to explicitly ‘mark’ a piece of information with its classification type.

| Classification | Definition | Marking |
|---|---|---|
| **OFFICIAL** | All information related to routine public sector business, operations and services. | |
| | Almost all personal information falls within the OFFICIAL classification. | |
| | OFFICIAL-SENSITIVE is not a separate security classification. It should be used to reinforce the ‘need to know’ principle, beyond the baseline for OFFICIAL.   | OFFICIAL data does not need to be marked except where Sensitive, and must be marked OFFICIAL-SENSITIVE |
| **SECRET** | Very sensitive information that requires protection against highly sophisticated, well-resourced and determined threat actors e.g. serious and organised crime. | Must be marked |
| **TOP SECRET** | Exceptionally sensitive information that directly supports (or threatens) the national security of the UK or its allies and requires extremely high assurance of protection from all threats. | Must be marked |

Additional information on how to manage information is described in the Information Asset Management Policy.

Information security classification may change throughout the information lifecycle, it is important to apply appropriate security classifications and continually evaluate them.

The consequences of not classifying information correctly are outlined below.

 - Applying too high a marking can inhibit business operations, such as collaboration, and lead to unnecessary and expensive protective controls being applied.
 - Applying too low a marking may result in inappropriate controls and may put sensitive assets at greater risk of compromise.
 - Incorrect disposal can lead to unauthorised access to information. Disposal of information should be done using approved processes, equipment or service providers. Refer to the [MoJ Data Destruction guide](../../security_decisions/standards/data-destruction/) to understand when the disposal should be witnessed/recorded.

### OFFICIAL AND OFFICIAL-SENSITIVE

All of the MoJ’s information is, at a minimum, OFFICIAL information. It is very likely that the information you are creating and using in your MoJ day-to-day job is OFFICIAL information.

**Examples**
 - routine emails you send to your colleagues
 - information posted on the intranet
 - supplier contracts
 - information and data you’d use to build a database – e.g. database secrets, record types, field types
 - in general, most production data, and
 - in general, most non-production data.

OFFICIAL means that the MoJ’s typical security measures are regarded as sufficient.

OFFICIAL-SENSITIVE “whilst not a formal classification”, should be used sparingly so that its effectiveness is not weakened (especially when you consider that OFFICIAL is already well-protected).

**When to use OFFICIAL-SENSITIVE**

When you wish to particularly remind users to be careful when handling information, beyond the expected for the baseline OFFICIAL classification.

### SECRET

The threshold for classifying information as SECRET information is very high. It is unlikely that you will encounter SECRET information in your day-to-day job.

**When to use SECRET**

SECRET information should not usually be handled unless you have sufficient and valid clearance. If you have gained access to information that you believe is SECRET, please contact the Cyber Assistance Team (CAT) immediately.

If a hacker gained unauthorised access to it, could it compromise the security or prosperity of the country?

The answer is most likely NO. In that case, you should consider using the OFFICIAL classification.

### TOP SECRET

If the threshold for classifying information as SECRET is very high, the threshold for classifying information as TOP SECRET is extremely high. It is very unlikely that you will encounter TOP SECRET information in your day-to-day job.

**When to use TOP SECRET:**

TOP SECRET information should not be handled unless you have sufficient and valid clearance. If you have gained access to information that you believe is TOP SECRET, please contact [CAT](mailto:CyberConsultancy@digital.justice.gov.uk) immediately.

If a hacker gained unauthorised access to this information, would it directly and immediately threaten the national security of the country?

The answer is most likely NO. In that case, you should consider using the OFFICIAL or SECRET classification as appropriate.

## Handling and securing information

The HMG Government Security Classifications Policy is the most comprehensive guide on the security measures necessary for each of the three security classifications, including measures related to the following:

 - personnel (administrative) security
 - physical security, and
 - technical (information security).

The following sections set out the minimum measures you need to consider when handling and securing information within the different levels of classification.

### Handling and securing OFFICIAL and OFFICIAL-SENSITIVE information

| Type | Measure | Example |
|---|---|---|
| **PERSONNEL** | Make sure all MoJ staff including contractors undergo baseline security clearance checks. | A contractor working with the MoJ Security Team must undergo a baseline background check (i.e. BPSS check) at minimum.  Refer to [Security Vetting Guidance](https://intranet.justice.gov.uk/guidance/hr/recruitment/security-vetting/). |
| **PHYSICAL** | Make sure that you lock your screen before you leave your desk. | |
| | When working in an unsecured area (e.g. you are working remotely), think about whether unauthorised people can eavesdrop on your conversations or look over your shoulder at your screen. | |
| | The MoJ have additional requirements when moving assets which can be found in the [HMG Government Security Classifications Policy](https://www.gov.uk/government/publications/government-security-classifications). | A software developer working from a flatshare should take calls in private and use a privacy screen. |
| | Transferring information from one location to another requires planning and preparation, this could include a risk assessment. More information on this is available in the [Government Security Classifications guidance](https://www.gov.uk/government/publications/government-security-classifications) and from your manager. |  A technical architect working on the requirements for a new HMCTS platform should lock their laptop before leaving their desk.
| **TECHNICAL** | Protect information at rest by using [Foundation Grade encryption](https://www.ncsc.gov.uk/information/foundation-grade-explained). | In the development of a new cloud-hosted solution, the following criteria should be considered: remote access connections and sessions are encrypted e.g. VPN; information stored at rest on end user devices and the cloud is encrypted; information in transit between the end user and the cloud service is encrypted e.g. payment services, and the cloud service used is a GCloud service. |
| | Foundation Grade encryption is also necessary when protecting information in transit. | When using any services over the PSN, make sure you fully read the agreements that you make with the service provider for details and definitions about the data you use or transfer using the service to ensure you understand the risks to compliance, integrity and availability |
| | [GCloud services](https://www.digitalmarketplace.service.gov.uk/g-cloud) can be used for OFFICIAL information. | |
| | You must not use removable media such as an USB memory stick unless it is necessary. When you have to use one, it must be MoJ issued, encrypted so that the effects of losing it are minimised and the data erased after use. | | |

**Different information security measures may be applicable throughout the information lifecycle; it is important to continually evaluate security classifications and corresponding measures. Please refer to the [HMG Government Security Classifications Policy](https://www.gov.uk/government/publications/government-security-classifications) for further guidance.**

### Handling and securing SECRET information

| Type | Measure | Example |
|--- |---|---|
| **PERSONNEL** | Make sure employees and contractors undergo Security Check (SC). | A contractor working with the MoJ Security Team must have at least SC before being allowed to access SECRET information. |
| **PHYSICAL** | Consider using multiple layers of security to protect SECRET information. SECRET information should be held on a secure computer network which is physically isolated from unsecured networks and the internet. | Imagine you are moving locations for a server used to host SECRET information. The encrypted server is secured in a locked and monitored room in 102 Petty France. You have now decided to move it to 10 South Colonnade. This should only be done after relevant parties (e.g. the data owner, line manager and system owner) have reviewed and accepted the risks associated with this transfer. The transfer should then be handled by two SC-cleared individuals, for example, employees of a specialised commercial courier company.  |
| | Transferring SECRET information from one location to another requires planning and preparation, including the completion of a risk assessment and the use of SC-cleared personnel. More information on this is available in the [Government Security Classifications guidance](https://www.gov.uk/government/publications/government-security-classifications) and from your manager. | |
| **TECHNICAL** | SECRET information at rest should be protected with Enhanced Grade encryption. The [CAPS Team](mailto:caps@ncsc.gov.uk) at the NCSC should be contacted in these circumstances. | In the development of a new cloud-hosted solution for SECRET information, you should consider the following: information stored at rest on the cloud is encrypted with Enhanced Grade encryption; information in transit between the end user; the cloud service is encrypted with Enhanced Grade encryption, and the cloud service used is accredited by the [CAPS Team](mailto:caps@ncsc.gov.uk) against the SECRET threat model with guidance from the [CAT Team](mailto:CyberConsultancy@digital.justice.gov.uk). |
| |Care should be taken to ensure that SECRET information in transit is only shared with defined recipient users through assured shared infrastructure or using Enhanced Grade encryption. | |
| | SECRET information should be processed on IT systems which have been assured against the SECRET threat model. Advice on what commercial IT systems meet this requirement is available from the Security Team | | |

**Different information security measures may be applicable throughout the information lifecycle; it is important to continually evaluate security classifications and corresponding measures. Please refer to the [HMG Government Security Classifications Policy](https://www.gov.uk/government/publications/government-security-classifications) for further guidance.**

### Handling and securing TOP SECRET information

| Type | Measure | Example |
|--- |---|---|
| **PERSONNEL** | Ensure employees and contractors undergo DV security clearance checks. | A contractor working with the MoJ Security Team should have at least DV clearance before being allowed to access TOP SECRET information. |
| **PHYSICAL** |  Handling and storing TOP SECRET information requires exceptional planning, monitoring and record-keeping. | Imagine you are moving locations for a server used to host TOP SECRET information. The encrypted server is secured in a locked and continuously monitored room in 102 Petty France. You have now decided to move it to 10 South Colonnade. This should only be done after you, your manager, and senior managers have reviewed and accepted the risks associated with this transfer. The transfer should then be handled by two DV-cleared individuals, for example, employees of a specialised commercial courier company. When it happens, local police may need to be informed and involved in providing an additional layer of security. |
| | Working remotely with TOP SECRET is not permitted due to the extreme sensitivity of the information. | |
| | Transferring TOP SECRET information from one location to another requires even greater planning and preparation than for SECRET information, including the completion of a risk assessment by senior management and the use of DV-cleared personnel. More information on this is available in the [Government Security Classifications guidance](https://www.gov.uk/government/publications/government-security-classifications) and from your manager. | |
| **TECHNICAL** | When physical security measures cannot be used, TOP SECRET information at rest should be protected with High Grade encryption. The [CAPS Team](mailto:caps@ncsc.gov.uk) at the NCSC should be contacted in these circumstances. | In the development of a new cloud-hosted solution for TOP SECRET information, you should contact the [CATS Team](mailto:CyberConsultancy@digital.justice.gov.uk). Information stored at rest on the cloud is encrypted with Enhanced Grade encryption; information in transit between the end user and the cloud service is encrypted with Enhanced Grade encryption and the cloud service used is accredited  by the [CAPS Team](mailto:caps@ncsc.gov.uk) against the SECRET threat model with guidance from the [CATS Team](mailto:CyberConsultancy@digital.justice.gov.uk).  |
| | Care should be taken to ensure that TOP SECRET information in transit is only shared with defined recipient users through accredited shared infrastructure or using High Grade encryption. | |
| | TOP SECRET information should be processed on IT systems which have been accredited against the TOP SECRET threat model. Advice on what commercial IT systems meet this requirement is available from the Security Team. | | |

**Different information security measures may be applicable throughout the information lifecycle; it is important to continually evaluate security classifications and corresponding measures. Please refer to the [HMG Government Security Classifications Policy](https://www.gov.uk/government/publications/government-security-classifications) for further guidance.**

For further information on statutory disclosures and transfer to national archives please refer to the [HMG Government Security Classifications Policy](https://www.gov.uk/government/publications/government-security-classifications).

## Contact details
For any further questions relating to security, please contact: [security@justice.gov.uk](mailto:security@justice.gov.uk)
Contact the Cyber Assistance Team for further advice: [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk)
