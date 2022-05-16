# Patch Management Guide

This guide explains the patching requirements for Ministry of Justice \(MoJ\) systems once a vulnerability has been identified.

The intent is to avoid compromise of MoJ systems because of vulnerabilities.

**Parent topic:** [Vulnerability Scanning and Patch Management Guide](vulnerability-scanning-and-patch-management-guide.md)

**Related information**  


[Technical Controls Policy](technical-controls-policy.md)

## Patching of MoJ systems and equipment

This guidance **SHALL** be followed for all systems and services developed or procured by the MoJ. It applies to all asset types including, but not limited to:

-   Internet facing websites and digital services.
-   End user client devices, such as Desktop PCs, laptops, tablets, and mobile phones.
-   Infrastructure devices, such as networking equipment, servers, and printers.
-   Applications.
-   Internet-of-Things \(IoT\) devices.

Patching is the application of a vendor-supplied security patch. It can also refer to other ways of achieving the same goal. Examples include:

-   Virtual patches.
-   Removal of vulnerable services or functionality.
-   Disabling and preventing access.

Patching might include recompiling applications to incorporate security updates. The updates might be in third party libraries or other code.

In general, there are three options for patching:

-   'Now': The problem is serious or urgent, and **SHALL** be mitigated as soon as possible. It is a priority to get this security mitigation deployed, the problem is being utilised in the wild, immediate action is required.
-   'Next': The problem is important but not urgent; mitigation can wait until the next scheduled patching cycle. This patch **SHALL** be picked up in the next regular patching cycle for affected systems, for example at their monthly or quarterly update.
-   'Never': The problem does not require mitigation in advance of changes introduced as part of normal system upgrades. This patch is not relevant or is too complex to deploy, for too little benefit, so **SHOULD** be applied at system rebuild time.

**Note:** The nature of the patching cycle depends on what is agreed during development, deployment, and subsequent maintenance of the system or service.

By default, all security updates require 'Next' scheduling. The urgency might be increased to 'Now' for security reasons. Conversely, there might be operational or development reasons for revising the urgency down to 'Never'. If agreement cannot be reached about the urgency, then the problem requires risk escalation.

In general, always apply patches as soon as possible. Where this guidance mentions a time limit, you **SHOULD** apply patches no later than the time given. Some important or sensitive systems might need more urgent patching. For example, a system might need you to apply 'critical' or 'high risk' patches within 2 days.

Where patching or other mitigation is required, it **SHALL** be applied in compliance with the [Patching Schedule](#patching-schedule) in this guide.

Operating systems and applications installed on systems **SHALL** be:

-   Licensed and supported.
-   Removed from devices when no longer licensed or supported.
-   Patched as soon as possible.
-   Patched within no more than 14 days of an update being released, where the fix is for a 'critical' or 'high risk' vulnerability.

To ensure that patches are implemented on systems, you **SHALL** either:

-   Enable and use any vendor-provided automatic patch deployment mechanisms for the system.
-   If automatic patch deployment is not available, apply patches manually according to the schedule outlined in this guide.

If a system or service, or a component it depends on, can no longer be licensed or supported, it **SHOULD** be reviewed within the timescale of the vulnerability scanning lifecycle, to determine what action to take. If the required license or support cannot be obtained, the system or service **SHOULD** be replaced by an alternative, or removed. If the system or service cannot be removed, then the issue **SHOULD** be raised through the patching exemptions process outlined in the [Patching Exemptions section](#patching-exemptions) in this guide.

In summary:

-   It **SHALL** be possible to patch or mitigate an MoJ system or service. A clear, documented process **SHALL** exist explaining how to patch or mitigate.
-   Wherever possible, patching **SHOULD** be automated, or at least have minimum possible dependency on manual intervention.
-   If a patch is not available, or cannot be deployed, then a suitable risk mitigation might be acceptable.
-   Patching or mitigating a system or service might impact or be affected by other systemic components. These **SHALL** be identified and addressed as part of the patch or mitigation process.

## MoJ Digital services

For systems or services developed by the MoJ, it **SHALL** be possible to patch or mitigate in order to address any vulnerabilities. To ensure this is possible:

-   The Beta development stage **SHALL** include a mechanism or process for a new or updated service to track and apply patches.
-   Sufficient logs **SHALL** be available from the new or updated service, so that security problems can be tracked from identification through to rectification.
-   The patching process **SHALL** also describe how to triage and action any problems.

## Patching Schedule

The following Patching Schedule defines the indicative severity ratings and consequent timescales. All vulnerabilities **SHALL** be remediated or patched in line with this schedule. By agreement and formal approval, alternative timescales for system patching, on a case-by-case basis, can be operated.

**Note:** The default is for patches to be applied as soon as possible. You should not normally delay patching because of concerns about possible issues with the patches themselves.

Patches and updates for security related devices **SHALL** be treated as High Risk \(3\) at least, and implemented in accordance with this rating. For more details on risk ratings, refer to the [vulnerability risk ratings](vulnerability-scanning-guide.md#vulnerability-risk-ratings) information.

All 'zero-day' issues and problems should be treated as 'Critical' by default.

For ratings of High Risk \(3\) or Critical \(4\), the Risk Advisor team \([contact through email](#contact-details)\) **SHALL** evaluate the probability and impact, and use this to guide a 'tolerance' period, at the end of which a patch **SHALL** be applied.

Where the rating is Medium \(2\) or lower, the patch can be deferred to the next scheduled maintenance or patching activity.

This schedule outline is considered a baseline. Some systems or services might require different patching schedules. These different schedules **SHALL** be identified in the system's Information Risk Assessment Report \(IRAR\).

An IRAR is normally completed by Security Architects and Risk Assessors, in conversation with the system architects, designers and developers. The IRAR document **SHALL** also be agreed with the Business Continuity Team. For more information regarding IRARs, and how to create and maintain them, contact the [Security team](mailto:security@justice.gov.uk).

The number of days for a patch indicates the timescale within which patching **SHALL** be started, and **SHOULD** be finished. For example, patching an End User Client Device to mitigate a 'Critical' vulnerability **SHALL** be started no more than 1-2 days after the fix is available, and **SHOULD** be finished no more than 1-2 days after the fix is available

**Note:** The 'number of days' measure is a simple calendar count, and reflects the support nature of the system or service. For example, if the system or service is expected to be available 24x7, as evidenced by a 24x7 support contract, then the count of workdays would be one day for each 24x7 period of time.

|Rating \(Severity\)|Infrastructure Devices; Server Applications; Digital Services|End User Client Devices|Web Check Reporting|
|-------------------|-------------------------------------------------------------|-----------------------|-------------------|
|Critical \(4\)|1-2 days after vulnerability alert released.|3-4 days after vulnerability alert released.|**Urgent:** Serious configuration problems that you **SHOULD** fix without delay and no later than 1-2 days after the vulnerability alert is released.|
|High Risk \(3\)|3-7 days after vulnerability alert released.|14 days after vulnerability alert released.|**Advisory:** Configuration problems that leave the site vulnerable. Patches **SHOULD** be implemented no later than 14 days after the vulnerability alert is released.|
|Medium \(2\)|28 days after vulnerability alert released.|28 days after vulnerability alert released.|**Informational:** Configurations that you could optimise, or information that you may find useful.|
|Low \(1\)|Next scheduled system upgrade \(not to exceed 90 days\).|Next scheduled system upgrade \(not to exceed 90 days\).|**N/A**|
|Positive \(0\)|N/A|N/A|**Positive:** Site configurations that conform to best practices.|

Any rollback requests require two activities:

-   Review and approval by the system or service risk owner, as the rollback will put the system or service back into an unpatched \(unmitigated\) state.
-   Invocation of and compliance with the normal change management process for the system or service.

## Patch management processes

There are two patching and change management approaches in the MoJ.

### Infrastructure and services provided by a Managed Service Provider \(MSP\)

Where services and infrastructure are provided by MSPs, the vendor is normally responsible for developing and implementing patches to identified vulnerabilities. Patches or a workaround **SHALL** be provided by vendors to ensure the MoJ is able to meet the schedule for implementing patches.

If this is not possible, vendors **SHALL** provide a firm statement that the patch or workaround cannot be made available within the timescale mandated for addressing the vulnerability. The vulnerability alert **SHALL** then be escalated to the Risk Advisor team \([contact through email](#contact-details)\) for help with acceptance, transfer, mitigation or avoidance.

Any patches to be deployed **SHALL** go through the normal change management and approval process, and the changes recorded in the Service Management Tool.

### Services and applications developed by MoJ in-house project teams

Where services and applications are developed by MoJ in-house project teams, patching and change management is addressed on a project-by-project basis. Changes are identified through awareness channels and scanning activities. These identify operational and security issues. A change management ticket **SHALL** be created, detailing the change required. The project manager follows the change management process to determine how and when to implement the change, based on the security risk rating.

The patch review and approval is normally managed within the project team. If assistance is required, contact the [Security Team](#contact-details).

If changes are urgent because a major security risk has been identified, the product, system, or service owner should ask a competent developer to investigate, and if possible create and implement a patch quickly. If the issue is more complex, Technical Architects, Security Architects and the [Security Team](#contact-details) might need to assist in the development of appropriate remediation plans.

Patches **SHALL** be implemented according to the schedule in this guide. If this is not possible, the project team **SHALL** provide an indication that the patch or workaround cannot be implemented within the timescale mandated for addressing the vulnerability. This delay **SHALL** be escalated to the Risk Advisor team \([contact through email](#contact-details)\) for help with acceptance, transfer, mitigation or avoidance.

## Removal of equipment

If a system or service vulnerability cannot be patched or mitigated, it might be necessary to remove that system or service.

Before the removal of any system or service, a fresh Business Impact Assessment **SHALL** be conducted and the business process owner consulted. The removal of a system or service is likely to come under the emergency and major change process.

## Patching exemptions

In exceptional cases where patching of systems is not possible, other mitigations \(such as logical separation\) **SHALL** be identified and evaluated for efficacy prior to enablement. The circumstances **SHALL** be discussed with the affected Information Asset Owners \(IAO\) and System Owners. If the IAOs agree with the deviation, System Owners **SHALL** request formal approval by the Senior Information Risk Owner \(SIRO\) for the exemption. Approval **SHALL** be sought and obtained within a comparable timescale to applying a patch. If a critical patch cannot be applied, the approval to be exempt **SHALL** be obtained within the same number of days allowed for applying a critical patch.

## Contact details

Contact the Security Team for advice on risk, scanning and patching, to report a vulnerability alert, or to add a URL to the MoJ Web Check system: [security@justice.gov.uk](mailto:security@justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

