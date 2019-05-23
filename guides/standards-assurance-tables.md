---
expires: 2019-09-01
---
# Standards Assurance Tables

The MOJ Cyber Security team have developed a 'Standards Assurance Table' (SAT) in the form of a Google Sheet template.

The SAT measures technology systems (and surrounding information governance) against the [UK Cabinet Office](https://www.gov.uk/government/organisations/cabinet-office) [Minimum Cyber Security Standard (MCSS)](https://www.gov.uk/government/publications/the-minimum-cyber-security-standard) and [UK National Cyber Security Centre (NCSC)](https://www.ncsc.gov.uk/) [Cloud Security Principles (CSPs)](https://www.ncsc.gov.uk/collection/cloud-security?curPage=/collection/cloud-security/implementing-the-cloud-security-principles).

For transparency and open-working purposes, a [redacted copy of the Standards Assurance Table](https://docs.google.com/spreadsheets/d/1oO9RAZQ6ETsN2iHZb5zcFM0HROliw18MBv89oF-BPeg/edit?usp=sharing) has been published. Please note, this is not the functional template used within the MOJ.

## SAT Template

The SAT itself is written to be self-explanitory to a cyber security professional that is already aware of the MCSS/CSP and has a familiarity with information risk management concepts.

- Black labelled sheets describe the SAT and how it should be used
- Blue labelled sheets are the sheets to be completed
- Yellow labelled sheets are automatically calculated reporting based on the blue labelled sheet data
- Green labelled sheets offer help/guidance on SAT components

## Key SAT concepts

The SATs have concepts of "Objectives", "Evidence", "Confidence", an overall "Delta" (which is the most pertinent output) and "Further Evidence Required", with supporting commentary.

The primary SAT purpose is to assess the system against the MCSS/CSP, determining how compliant (or non-compliant) the system is, based on a collation and review of evidence. Evidence is analysed to determine confidence that the evidence demonstrates the system meets (or does not meet) the standard, and the 'gap' (delta) between system posture according to said evidence and the standards.

### Objectives

The MCSS/CSPs have been distilled into 39 Objectives which the assessor (typically a cyber security professional) completing the SAT is measuring against.

The [categories used within the MCSS](https://ministryofjustice.github.io/security-guidance/principles/identify-protect-detect-respond-recover/#identify-protect-detect-respond-recover) have been discussed seperately.

Objectives are templated, so can be added to but not modified in-place.

### Evidence

To avoid assessments that are ultimately anecdotal, the SAT considers written evidence.

Evidence can come in the form of transcribed conversations, diagrams, documentation or an otherwise written conveyable information about a system. 

Evidence may not be related to the system itself but form a part, for example, where there is a wider document that is not system orientated that describes who relevant role holders currently are.

Evidence is 'Held', 'Partial', 'Not Held' or 'N/A' (where the Objective is not applicable to the system being assessed).

### Confidence

The assessor reviews the evidence and uses their professional opinion to indicate a Confidence Score.

The Confidence Score is based on a scale of 0 (no confidence at all) to 14 (high level of confidence), or 'N/A' (where the Objective is not applicable to the system being assessed).

### Delta

The Delta Rating is the resulting 'distance' between the assessed system posture against an Objective and the confidence of the same.

Mathematically, the results are N/A (where the Objective is not applicable to the system being assessed) or 0 to 14 (inc).

A wide delta (higher numerical value) conveys the Objective is not met. A narrow delta (lower numerical value) conveys the Objective is closer to being met.

The Delta Rating is automatically calculated as '14 minus Confidence Score'.

### Further Evidence Required

The assessor indicates what further evidence _types_ in their view are required based on the evidence they have thus far.

The [Further Evidence Required (Help) sheet](https://docs.google.com/spreadsheets/d/1oO9RAZQ6ETsN2iHZb5zcFM0HROliw18MBv89oF-BPeg/edit#gid=679100590) has a calculator which the assessor will use.

This data point was designed as unique numericals as this allows programmatic analysis in the future. This data point and how it is formed is currently under active review.

## Understanding the Objectives, gathering evidence for the assessor

Teams/individuals responsible for the design, creation, implementation, support and maintenance of systems should have viable written evidence (regardless of format) that should be made available to various teams on request, for example, security or to internal audit.

Using the [categories used within the MCSS](https://ministryofjustice.github.io/security-guidance/principles/identify-protect-detect-respond-recover/#identify-protect-detect-respond-recover) as sections some helpful thought questions and documentation expectations are discussed below.

### IDENTIFY

#### Possible documentation

- Team organisation charts
- Data Privacy Impact Assessments (DPIAs)
- Information risk management documentation (for example, RMADS)
- Information flow diagrams

#### Thought questions

- Who is responsible and/or accountable for the the system whether from an operational or budgetary perspective?
- Who is responsible and/or accountable for the information held inside the system?
- What security-focused work has been conducted on any suppliers and supplier systems to ensure they are safe for use/integration?
- Where is the system technically hosted?
- Where are the places where the system stores data?
- What are the consequences if the system is unavailable to users or data has been lost/corrupted?
- What happens for business continuity / disaster recovery if the system is unavailable or data has been lost/corrupted?

### PROTECT

#### Possible documentation

- Data Privacy Impact Assessments (DPIAs)
- Information risk management documentation (for example, RMADS)
- Information flow diagrams
- Technical/system architecture documentation
- Penetration test / IT Health Check reports and remedial documentation
- Risk registers

#### Thought questions

- How does the system ensure only authorised people can use the system?
- How are system users managed for joiners, movers and leavers?
- How is the system's underlying software kept up to date for security software patching?
- How does the system protect itself appropriately and proportionately from attackers?
- How do ensure the system can protect itself from attackers over time, so it is secure now but also will remain secure in the future?
- How often has technical security testing been conducted? Where within the system?
- How does the system stay up to date using modern encryption to keep data safe?
- Does the system use multi-factor authentication (MFA, also known as 2FA)?
- For people who have access to the system, do they have all the right clearances in place?

### DETECT

#### Possible documentation

- Information risk management documentation (for example, RMADS)
- Technical/system architecture documentation
- Penetration test / IT Health Check reports and remedial documentation
- Risk registers

#### Thought questions

- How does the system, and accompanying operational support teams, know/detect when the system is under attack?
- How is access to the system (both legitimate and illegitimate) logged so retrospective investigations can take place to determine 'who did what when'?

### RESPOND

#### Possible documentation

- Information risk management documentation (for example, RMADS)
- Technical/system architecture documentation
- Operational/support documentation

#### Thought questions

- What plans, processes or procedures are in place to respond to a detected cyber attack?
- How are these plans kept up to date and relevant?
- Does everyone who needs to know about these plans know about them?
- Has the plan been tested in the last 12 months?
- How are stakeholder communications handled during a security incident?
- How are external communications handled during a security incident for external parties, such as supervisory bodies, the NCSC or Cabinet Office?

### RECOVER

#### Possible documentation

- Operational/support documentation
- Retrospective session notes

#### Thought questions

- What happens for business continuity / disaster recovery if the system is unavailable or data has been lost/corrupted?
- Have these measures been tested in the last 12 months?