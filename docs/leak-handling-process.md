# Leak handling process

This document provides a high-level overview of the leak handling process for the Ministry of Justice \(MoJ\). It includes the roles, responsibilities, and major steps performed as part of leak handling.

It should be read in conjunction with the associated [leak handling policy](leak-handling-policy.md).

[MoJ Group Security](mailto:mojgroupsecurity@justice.gov.uk) owns the leak handling process. However, the [Investigations SOC team](mailto:MisuseInvestigationTeam@justice.gov.uk) provides tech support as required, for example performing searches. The analysis and reporting from these teams is an essential security management component in assessing and mitigating current and future leaks that affect MoJ data, systems, networks and solutions.

Send all leak questions or requests for help to [security@justice.gov.uk](mailto:security@justice.gov.uk). This applies to all leaks, suspected or otherwise. Your message is evaluated promptly and normally passed to [MoJ Group Security](mailto:mojgroupsecurity@justice.gov.uk). Depending on the circumstances, the [Investigations SOC team](mailto:MisuseInvestigationTeam@justice.gov.uk) might also provide direct advice on a case-by-case basis.

**Note:** Normally, the [MoJ incident management process](it-incident-management-policy.md) is followed at the start of a leak investigation.

**Note:** If a leak investigation indicates that physical examination of evidence is required, then [Investigations SOC team](mailto:MisuseInvestigationTeam@justice.gov.uk) involvement will involve a Team Lead as a minimum.

**Note:** An informal leak investigation takes place entirely within the MoJ. A formal leak investigation takes place with involvement from outside the MoJ, typically Cabinet Office.

**Related information**  


[Leak handling policy](leak-handling-policy.md)

## Audience

This process is aimed at all staff working for, or supplying services to, the MoJ. This includes General users, Technical users, contractors, third parties, and Service Providers.

## Roles and responsibilities

<a name="all-parties"></a>

-   **All parties**

    For each leak investigation, all parties agree on the scale, the scope, the expectations, and the limitations.

<a name="chief-information-security-officer-ciso"></a>

-   **Chief Information Security Officer \(CISO\)**

    Notifies and continues to update the MoJ Permanent Secretary regarding the incident. Obtains authorisation for a leak investigation if approved.

<a name="group-security"></a>

-   **Group Security**

    Following authorisation from the MoJ Permanent Secretary, Group Security:

    1.  Reviews the information available.
    2.  Defines the scope of the informal investigation \(internal to the MoJ\).
    3.  Provides the Cyber Security Team with the defined investigation scope and requests an electronic investigation if required.
    4.  Issues the leak questionnaire to those known to have had access to the leaked information.
    5.  Reviews all evidence gathered, and prepares the informal leak report.
<a name="ia-lead-case-manager-or-requestor"></a>

-   **IA Lead, Case Manager or Requestor**

    Addresses all investigation requirements. Provides governance sign-off. Communicates with the Investigations SOC team on case status, including case closure notification or retention date.

<a name="Shared-Security-team"></a>

-   **Shared Security team**

    Triages and formally logs incidents using ServiceNow. Works closely with all other security teams to resolve or escalate as required. The Shared Security team ensures that the Chief Security Officer is notified and informed of all suspected leak incidents.

<a name="Investigations-SOC-team"></a>

-   **Investigations SOC team**

    Has ownership of all data acquisition, preservation, analysis and reporting. This includes verification of sign-off. Provides regular feedback case review as needed. Tracks incidents using Service-Now and team internal tracker tools.


## Process steps

**Note:** These process steps apply to an informal leak investigation that is internal to the MoJ. If a formal leak investigation is required, it will be identified and initiated as part of the informal leak investigation process.

### Step 1: Identify leak

1.  A leak investigation is requested. The request might come from any of:

    -   CISO.
    -   Departmental office.
    -   Executive office.
    -   HMPPS.
    -   Ministerial office.
    -   MoJ agencies.
    -   Permanent Secretary.
    -   Senior Civil Servant \(SCS\).
    -   Other cross-government source.
2.  The request indicates that a leak investigation is required. The request is submitted to the Shared Security team: [security@justice.gov.uk](mailto:security@justice.gov.uk).

3.  Proceed to [step 2](#step-2-is-it-a-leak).


### Step 2: Is it a leak?

1.  The Shared Security team evaluates the request.

2.  If the situation is indeed a leak, the request is sent to [MoJ Group Security](mailto:mojgroupsecurity@justice.gov.uk). Proceed to step [2.1](#step-21-require-informal-leak-investigation).

3.  If the situation is not a leak, or it is not clear whether the situation is a leak, the request is sent to the [Investigations SOC team](mailto:MisuseInvestigationTeam@justice.gov.uk). Proceed to step [2.2](#step-22-information-and-sign-off-check).


### Step 2.1: Require informal leak investigation

1.  Group Security reviews the request to determine if a leak investigation is required.

2.  If a leak investigation is needed, go to step [2.1.1](#step-211-produce-informal-investigation-report).

3.  If a leak investigation is not needed, the Shared Security team notifies the Requestor that a leak investigation is not required, based on the rationale provided by Group Security. The leak process ends. No further action is required.


### Step 2.1.1: Produce informal investigation report

1.  Group Security produces an informal investigation report with input from the Cyber Security Team. The report describes the findings and recommendations.

2.  The report is sent to the Requestor.

3.  Proceed to step [2.1.2](#step-212-receive-investigation-report).


### Step 2.1.2: Receive investigation report

1.  The Requestor receives the informal leak report.

2.  If the report is satisfactory, and no escalation is required or requested, the process ends. No further action is required.

3.  If the report is not satisfactory, or an escalation is required or requested, proceed to step [2.1.3](#step-213-escalate-leak-request).


### Step 2.1.3: Escalate leak request

1.  Group Security re-evaluates the leak request, in the light of the informal leak report.

2.  Group Security signs off the informal leak request.

3.  If an escalation is required or requested, Group Security begins the process of requesting formal leak investigation.

4.  Proceed to step [2.2](#step-22-information-and-sign-off-check) to continue and complete the informal leak investigation.


### Step 2.2: Information and sign off check

1.  The Investigations SOC Lead checks that the leak investigation request is complete with all required information and the required sign-off. This confirms the legitimacy of the investigation.

2.  If the request is incomplete or not signed off, the Investigations SOC Lead connects back to the Requestor to provide this information. The process returns to step [2.1.2](#step-212-receive-investigation-report).

3.  If the request is complete and signed off, go to step [2.2.1](#step-221-create-incident).


### Step 2.2.1: Create incident

1.  The Investigation SOC Lead assigns an Investigations SOC Analyst to the request.

2.  The Investigations SOC Analyst creates a ServiceNow 'placeholder' incident using the Technology Portal. In all cases, the title of the placeholder **SHALL** be "An investigation carried out by the SOC."

3.  Proceed to step [2.2.2](#step-222-collect-evidence).


**Note:** **Do not include any case details within the ServiceNow incident.** Use the ServiceNow incident number, plus any Requester case reference numbers or descriptions, for all correspondence, case notes or tracker updates.

### Step 2.2.2: Collect evidence

1.  The Investigations SOC Analyst starts the leak investigation, using tools appropriate to the platform, system, or location from which the data was leaked.

2.  Evidence is collected, secured and validated with checksums, following forensic best practices.

3.  Proceed to step [2.2.3](#step-223-process-evidence-and-produce-report).


**Note:** The Investigations SOC Analyst **SHALL** record all the steps taken for each request in OneNote. These contemporaneous notes **SHALL** include supporting data, such as photos, screenshots and images. In addition, each entry **SHALL** be supported by the Analyst's comments.

### Step 2.2.3: Process evidence and produce report

1.  The Investigations SOC Analyst processes or analyses the data as needed and produces a report.

2.  Proceed to step [2.2.4](#step-224-close-servicenow-incident).


### Step 2.2.4: Close ServiceNow incident

1.  The Investigations SOC Analyst confirms that the leak investigation request can be closed with the Requestor.

2.  When confirmation is received, the Investigations SOC Analyst provides the Requestor with a concluding report outlining the findings and recommendations established during step [2.1.2](#step-212-receive-investigation-report).

3.  The Investigations SOC Analyst updates and closes the ServiceNow Incident.

4.  Proceed to step [2.2.5](#step-225-update-tracker-and-onenote).


### Step 2.2.5: Update Tracker and OneNote

1.  The Investigations SOC Analyst updates the Tracker spreadsheet in Teams and the OneNote record.

2.  The process ends.


**Note:** Information **SHALL** be retained and recorded as set out in the MoJ information retention policy. Guidance on what to keep is [available](https://intranet.justice.gov.uk/guidance/knowledge-information/managing-information/keeping-deleting-disclosing-info/).

## Who to contact if a leak is suspected

Contact [security@justice.gov.uk](mailto:security@justice.gov.uk).

**Note:** To log a security incidents during UK working hours, you must report it using the process on the [Reporting a Security Incident](https://intranet.justice.gov.uk/guidance/security/report-a-security-incident/) page of the MoJ Intranet.

## Contact details

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for cyber security advice, contact the Cyber Assistance Team: [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

