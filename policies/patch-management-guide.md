---
Review: 2020-12-31
Owner: CISO
Target audience:
---

# Patch Management Guide

## Introduction
This guide explains the patching requirements for the MoJ’s systems once a vulnerability has been identified. This guide is a sub-page to the Vulnerability Scanning and Patch Management Guide.

Patching of MoJ systems and equipment

The patching guide must be followed for all asset types including, but not limited to:

* internet facing websites
* end user client devices
* infrastructure devices
* digital services, and
* applications.

## Internet facing websites

If you are developing or running any websites or services that are publically accessible through the open internet, you must patch any vulnerabilities and common configuration errors identified
either through the MoJ’s Web Check Account (see the Vulnerability Scanning Guide for details) or by any other means. You need to ensure that any vulnerabilities identified are remediated according to Service Level Agreements (SLAs) in this guide below.

## End user clients

If you run an end user client, you must ensure that the operating system and any applications installed on the end user client are licensed and supported. To ensure that patches are implemented, you must either:

1. enable and use any vendor provided automatic patch deployment mechanisms for the device, or
2. if automatic patch deployment is not available, apply patches manually according to the SLAs outlined in this guide.

## Infrastructure devices

All infrastructure devices must be licensed and supported. Any infrastructure devices that are no longer licensed or whose vendors do not provide ongoing support, should be reviewed in line with the MoJ patch management processes outlined below, and where possible removed. If devices cannot be removed then the issue should be raised through the patching exemptions process outlined in the Patching Exemptions section in this guide.

## Digital services

If you are developing a new digital service, you are responsible for ensuring that appropriate patches are developed and applied to the service. You must comply with the following requirements.

* To enter the Beta development stage, a new or updated service must be able to track and apply patches. See the Software Development Lifecycle Guide for further details.
* Sufficient logs must be provided by the new or updated service so that security problems can be tracked from identification through to rectification.
* The patching process must also describe how to triage and action any problems. Please see the Software Development Lifecycle Guide for further details.

Applications

If you develop or run applications hosted on MoJ servers, external servers or cloud platforms, you must ensure they are scanned and patched according to the SLAs in this guide. Applications include both traditional applications (tools) and services.

* Applications that are no longer licensed or whose vendors do not provide ongoing support should be reviewed and possibly removed. Please see the Patching Exemptions section below for further information.

Applications should be access-controlled to help prevent exploitation of any vulnerabilities. The level of access control must be matched to the level of risk to the service provided. For example, a
finance server might have stronger access control than an email server. See the Access Control Guide for further information.

## Patching schedule Service Level Agreement

The following Patching Schedule SLA defines the indicative severity ratings and consequent timescales. All vulnerabilities must be remediated/patched in line with this SLA. By agreement and formal approval, alternative timescales for a system patching, on a case-by-case basis, can be operated.

* It is recommended that patches are not applied immediately in order to allow for the identification of any issues with patches, so a 3 day testing period should be used.
* Where the rating is Medium (2) or lower, the patch can be deferred to the next scheduled maintenance/patching activity.
* For ratings of High Risk (3) or Critical (4), the Risk Advisor Team must evaluate the probability and impact, and use this to guide a 'tolerance' period, at the end of which a patch must be applied.
* Patches and updates for security related devices must be treated as High Risk and implemented in accordance with this rating.
* This is considered a baseline and some systems may require different patching schedules which will be identified in the system’s Information Risk Assessment Report (IRAR).

### Patching SLA

| Rating (Severity) | Infrastructure Devices; Server Applications; Digital Services | End User Client Devices | Web Check Reporting |
| --- | --- | --- | --- |
|Critical (4) | 3-7 days after vulnerability alert released | 14 days after vulnerability alert released | Urgent: Serious configuration problems that you should fix without delay and no later than 28 days after the vulnerability alert is released. |
| High Risk (3) | 3-7 days after vulnerability alert released | 14 days after vulnerability alert released | Advisory: Configuration problems that leave the site vulnerable. Patches should be implemented no later than 28 days after the vulnerability alert is released. |
| Medium (2) | 28 days after vulnerability alert released | 28 days after vulnerability alert released | Informational: Configurations that you could optimise, or information that you may find useful. |
| Low (1) | Next scheduled system upgrade (not to exceed 90 days) | Next scheduled system upgrade (not to exceed 90 days) | N/A |
| Positive (0) | N/A | N/A | Positive: Site configurations that conform to best practices. |

## Patch management processes

There are two patching and change management approaches in the MoJ:

1. Infrastructure and services provided by a Managed Service Provider (MSP)

Where services and infrastructure are provided by MSPs, the vendor is normally responsible for developing and implementing patches to identified vulnerabilities. Patches or a workaround must be provided by vendors to ensure the MoJ is able to meet the SLAs for implementing patches. If this is not possible, vendors must provide an indication that the patch/workaround cannot be made available within the timescale mandated for addressing the vulnerability. This must be escalated to the Risk Advisor team for acceptance, transfer, mitigation or avoidance.

Any patches to be deployed must go through the approval process, outlined in the diagram below, and the changes recorded in the Service Management Tool.

GRAPHIC

2. Services and applications developed by MoJ in-house project teams

Where services and applications are developed by the MoJ in-house project teams, patching and change management is managed on a project by project basis. Changes are identified through research and scanning which identifies operating and security issues. A ticket will be created detailing the change required and the project manager will determine how and when to implement the change based on the security risk rating. The patch review and approval is undertaken within the project team.

If changes are urgent because a major security risk has been identified, the product, system, or service owner will ask a developer to investigate and if possible create and implement a patch quickly. If the issue is more complex, Technical Architects, Security Architects and the Cyber Assistance Team may need to assist in the development of appropriate remediation plans.

Patches must be implemented according to the SLAs in this guide. If this is not possible, the project team must provide an indication that the patch/workaround cannot be implemented within the timescale mandated for addressing the vulnerability. This must be escalated to the Risk Advisor Team for acceptance, transfer, mitigation or avoidance.

## Removal of equipment

The removal of any IT equipment or software, must be managed as part of the MoJ’s change process outlined above in the Patch Management Process section. Before the removal of any IT equipment, a Business Impact Assessment must be conducted and the business process owner consulted. The removal of IT equipment may fall under the emergency and major change process.

## Patching exemptions

In exceptional cases where patching of systems is not possible, other mitigations (such as logical separation) must be identified and evaluated for efficacy prior to enablement. The circumstances
must be discussed with the affected Information Asset Owners (IAO) and System Owners. If the IAOs agree with the deviation, System Owners must request formal approval by the Senior Information Risk Owner (SIRO) for the exemption. Approval must be sought and obtained within a comparable timescale to applying a patch. If a critical patch cannot be applied, the approval to be exempt must be obtained within the same number of days allowed for applying a critical patch.

## Contact details

Contact the Cyber the Assistance Team for advice on scanning and patching – [CyberConsultancy@digital.justice.gov.uk](CyberConsultancy@digital.justice.gov.uk)

Contact the Operational Security Team to be added to the MoJ Web Check account – [Operationalsecurityteam@justice.gov.uk](Operationalsecurityteam@justice.gov.uk)
