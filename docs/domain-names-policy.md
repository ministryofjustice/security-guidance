# Domain names and Domain Name System \(DNS\) security policy

## Introduction

This policy gives an overview of domain name registration and monitoring principles and responsibilities within the Ministry of Justice \(MoJ\) and summarises the MoJ's related compliance policies and guides.

To help identify formal policy statements, each is prefixed with an identifier of the form: `POLDOMxxx`, where `xxx` is a unique ID number.

## Who is it for?

This policy is aimed at:

<a name="technical-users"></a>

-   **Technical users**

    These are in-house MoJ Digital and Technology staff responsible for implementing controls throughout technical design, development, system integration and operation. This includes DevOps, Software Developers, Technical Architects, Service Owners and the [EPICK](https://ministry-of-justice-acronyms.service.justice.gov.uk/) Team.

<a name="service-providers"></a>

-   **Service providers**

    Defined as any other MoJ business group, agency, contractor, IT supplier and partner who in any way designs, develops or supplies services \(including processing, transmitting and storing data\) for or on behalf of the MoJ.

<a name="general-users"></a>

-   **General users**

    All other staff working for the MoJ.


'All MoJ users' refers to General users, Technical users and Service Providers as defined previously.

## Policy sections

This policy aligns to industry standards and frameworks and is divided into two categories \(and subsections describing the controls\) addressing:

-   [Principles](#principles).

-   [Policy statements](#domain-name-registration-statements).


**Note:** If any of the controls within this policy cannot be applied, they are considered an exception to be assessed for inclusion within a risk register.

## Principles

Effective domain name registration encompasses the following five principles, which include:

-   `POLDOM001:` The MoJ **SHALL** secure domain name management aligning this to its [Cyber security guidance](https://security-guidance.service.justice.gov.uk/), specifically [multi-factor authentication](access-control-policy.md#) \(MFA\), [least privilege](access-control-policy.md#) and [review of user access rights](access-control-policy.md#).

-   `POLDOM002:` The MoJ **SHALL** manage domain name portfolio growth, that is, their inherent value, before assessing their expiration.

-   `POLDOM003:` The MoJ **SHALL** ensure non-core or defensively registered domains point to relevant content.

-   `POLDOM004:` The MoJ **SHALL** ensure all MoJ "Technical users" and "Service Providers" are reminded of the processes for requesting new registrations, auto-renewal, and decommissioning domains.

-   `POLDOM005:` The MoJ **SHALL** apply domain name specific technologies such as \(list not exhaustive\):

    -   Domain Name System Security Extensions \([DNSSEC](https://www.ncsc.gov.uk/guidance/managing-public-domain-names#section_6)\), which protects against cache poisoning.

    -   Domain-based Message Authentication, Reporting and Conformance \([DMARC](https://www.ncsc.gov.uk/information/mailcheck)\), which protects against email spoofing.


## Domain name registration statements

This policy's statement elements are outlined as follows:

### Standards, guidance and technology

-   `POLDOM006:` To improve clarity and security hardening, all MoJ domain name registrations and usage **SHALL** adhere to the MoJ's [domain naming standards](https://ministryofjustice.github.io/technical-guidance/documentation/standards/naming-domains.html#naming-domains.Guidance) and [system hardening standards](system-lockdown-and-hardening-standard.md#).

-   `POLDOM007:` This policy's related security guidance **SHALL** clearly describe why defensive domain registration is essential and why not doing it creates cyber risk.

-   `POLDOM008:` This policy's related guidance on [How to get, register or manage a domain name](https://technical-guidance.service.justice.gov.uk/documentation/standards/how-to-get-a-domain-name.html) clearly describes defensive domain names solutions.


### Domain Operations: Operations Engineering team

-   `POLDOM009:` The MoJ [Operations Engineering](https://operations-engineering.service.justice.gov.uk/) team **SHALL** manage the registration of all domain names, including defensive domain names.

-   `POLDOM010:` Departmental teams and ALBs **SHALL** be directed to the [Operations Engineering](https://operations-engineering.service.justice.gov.uk/) team to carry out domain registration on the user or department's behalf.

-   `POLDOM011:` All departments and ALBs **SHALL** ensure that they transfer ownership of non-GOV.UK domains to the MoJ [Operations Engineering](https://operations-engineering.service.justice.gov.uk/) team, with a list of transfers and registration managed by the MoJ [Operations Engineering](https://operations-engineering.service.justice.gov.uk/) team.


### Domain monitoring

-   `POLDOM012:` The Threat Vulnerability Management team \(TVM\) **SHALL** be responsible for identifying, detecting, reporting, and helping prioritise domain monitoring issues, including squatting or hijacking.

-   `POLDOM013:` The TVM team **SHALL** also be responsible for detecting and reporting on external domain name hijackings.

-   `POLDOM014:` The [Operations Engineering](https://operations-engineering.service.justice.gov.uk/) team and TVM team **SHALL** be responsible for resolving domain issues raised by the TVM team, domain owners and teams, by implementing any required changes.

-   `POLDOM015:` The MoJ **SHALL** follow when a domain is hijacked or used maliciously.

-   `POLDOM016:` MoJ departments, ALBs and third parties **SHALL** report domain variants and domains used within the MoJ but which are not owned by the MoJ. Refer to the [contact details](#contact-details).


**Note:** Contact the TVM team through the [Security team](mailto:security@justice.gov.uk).

**Note:** Security contacts in the event of an incident are located on the [MoJ Intranet](https://intranet.justice.gov.uk/guidance/knowledge-information/protecting-information/information-assurance-roles/).

### Decommissioning domains

-   `POLDOM017:` Any decommissioned domain **SHALL** be transferred to the MoJ [Operations Engineering](https://operations-engineering.service.justice.gov.uk/) team. Contact them at [domains@digital.justice.gov.uk](mailto:domains@digital.justice.gov.uk) on behalf of departmental teams or ALBs, and providing appropriate HTTP redirections to a suitable URL, for example, `301` or `302`.

-   `POLDOM018:` Domains registered pre-policy **SHALL** be moved to the [Operations Engineering](https://operations-engineering.service.justice.gov.uk/) team.

-   `POLDOM019:` The MoJ **SHALL** allow decommissioned domains to expire if there is no risk to the MoJ via "Domain Squatting" or "Phishing" attacks, or value in registering them defensively.

-   `POLDOM020:` Any decommissioned domains **SHALL** be added and managed in a risk register.


## Enforcement

-   `POLDOM021:` MoJ domains discovered that do not abide by the statements set out in this policy **SHOULD** be treated as suspicious, reported to NCSC, and blocked automatically.

-   This policy is enforced by lower-level policies, standards, procedures and guidance.

-   Non-conformance with this policy could result in disciplinary action taken as per the department's disciplinary procedures. This could result in penalties up to and including dismissal. If an employee commits a criminal offence, they might also be prosecuted. In such cases, the department always cooperates with the relevant authorities and provides appropriate evidence.


## Contact details

MoJ organisations should contact [domains@digital.justice.gov.uk](mailto:domains@digital.justice.gov.uk) for assistance with domain registrations, defensive domain registrations, transfers and operations.

## Incidents and contact details

**Note:** If you work for an agency or ALB, refer to your local incident reporting guidance.

For help with incidents, including theft and loss, contact one of the following:

**Technology Service Desk** - including DOM1/Quantum, and Digital & Technology Digital Service Desk. Use one of the following two methods for contacting service desk:

-   Tel: 0800 917 5148
-   [MoJ Service Portal and Live Chat](https://mojprod.service-now.com/moj_sp)

**Note:** The previous `itservicedesk@justice.gov.uk` and `servicedesk@digital.justice.gov.uk` email addresses, and the Digital & Technology Digital Service Desk Slack channel \(`#digitalservicedesk`\), are no longer being monitored.

**HMPPS Information & security:**

-   Email: [informationmgmtsecurity@justice.gov.uk](mailto:informationmgmtsecurity@justice.gov.uk)
-   Tel: 0203 334 0324

For non-technology incidents, contact the MoJ Group Security Team: [mojgroupsecurity@justice.gov.uk](mailto:mojgroupsecurity@justice.gov.uk)

Contact the Data Protection Team for information on Data Protection Impact Assessments: [DataProtection@justice.gov.uk](mailto:DataProtection@justice.gov.uk)

If you are not sure who to contact, ask the Security Team:

-   Email: [security@justice.gov.uk](mailto:security@justice.gov.uk)
-   Slack: `#security`

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

