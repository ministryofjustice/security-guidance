# Domain names and Domain Name System \(DNS\) security policy

## Introduction

This policy gives an overview of domain name registration and monitoring principles and responsibilities within the and summarises the 's related compliance policies and guides.

To help identify formal policy statements, each is prefixed with an identifier of the form: **POL.DOM.xxx**, where **xxx** is a unique ID number.

## Who is it for?

This policy is aimed at:

<a name="technical-users"></a>

-   **Technical users**

    These are in-house Digital and Technology staff responsible for implementing controls throughout technical design, development, system integration and operation. This includes DevOps, Software Developers, Technical Architects, Service Owners and the [EPICK](https://ministry-of-justice-acronyms.service.justice.gov.uk/) Team.

<a name="service-providers"></a>

-   **Service providers**

    Defined as any other business group, agency, contractor, IT supplier and partner who in any way designs, develops or supplies services \(including processing, transmitting and storing data\) for or on behalf of the .

<a name="general-users"></a>

-   **General users**

    All other staff working for the .


'All users' refers to General users, Technical users and Service Providers as defined previously.

## Policy sections

This policy aligns to industry standards and frameworks and is divided into two categories \(and subsections describing the controls\) addressing:

-   [Principles](#principles).

-   [Policy statements](#domain-name-registration-statements).


**Note:** If any of the controls within this policy cannot be applied, they are considered an exception to be assessed for inclusion within a risk register.

## Principles

Effective domain name registration encompasses the following five principles, which include:

-   **POL.DOM.001:** The secure domain name management aligning this to its [Cyber security guidance](https://security-guidance.service.justice.gov.uk/), specifically [multi-factor authentication](access-control-policy.md#user-registration-and-de-registration) \(MFA\), [least privilege](access-control-policy.md#access-control-policy-1) and [review of user access rights](access-control-policy.md#review-of-user-access-rights).

-   **POL.DOM.002:** The manage domain name portfolio growth, that is, their inherent value, before assessing their expiration.

-   **POL.DOM.003:** The ensure non-core or defensively registered domains point to relevant content.

-   **POL.DOM.004:** The ensure all "Technical users" and "Service Providers" are reminded of the processes for requesting new registrations, auto-renewal, and decommissioning domains.

-   **POL.DOM.005:** The apply domain name specific technologies such as \(list not exhaustive\):

    -   Domain Name System Security Extensions \([DNSSEC](https://www.ncsc.gov.uk/guidance/managing-public-domain-names#section_6)\), which protects against cache poisoning.

    -   Domain-based Message Authentication, Reporting and Conformance \([DMARC](https://www.ncsc.gov.uk/information/mailcheck)\), which protects against email spoofing.


## Domain name registration statements

This policy's statement elements are outlined as follows:

### Standards, guidance and technology

-   **POL.DOM.006:** To improve clarity and security hardening, all domain name registrations and usage adhere to the 's [domain naming standards](https://ministryofjustice.github.io/technical-guidance/documentation/standards/naming-domains.html#naming-domains.Guidance) and [system hardening standards](system-lockdown-and-hardening-standard.md#scope).

-   **POL.DOM.007:** This policy's related security guidance clearly describe why defensive domain registration is essential and why not doing it creates cyber risk.

-   **POL.DOM.008:** This policy's related guidance on [How to get, register or manage a domain name](https://technical-guidance.service.justice.gov.uk/documentation/standards/how-to-get-a-domain-name.html) clearly describes defensive domain names solutions.


### Domain Operations: Operations Engineering team

-   **POL.DOM.009:** The team manage the registration of all domain names, including defensive domain names.

-   **POL.DOM.010:** Departmental teams and ALBs be directed to the team to carry out domain registration on the user or department's behalf.

-   **POL.DOM.011:** All departments and ALBs ensure that they transfer ownership of non-GOV.UK domains to the team, with a list of transfers and registration managed by the team.


### Domain monitoring

-   **POL.DOM.012:** The Threat Vulnerability Management team \(TVM\) be responsible for identifying, detecting, reporting, and helping prioritise domain monitoring issues, including squatting or hijacking.

-   **POL.DOM.013:** The TVM team also be responsible for detecting and reporting on external domain name hijackings.

-   **POL.DOM.014:** The team and TVM team be responsible for resolving domain issues raised by the TVM team, domain owners and teams, by implementing any required changes.

-   **POL.DOM.015:** The follow when a domain is hijacked or used maliciously.

-   **POL.DOM.016:** departments, ALBs and third parties report domain variants and domains used within the but which are not owned by the . Refer to the [contact details](#contact-details).


**Note:** Contact the TVM team through the .

**Note:** Security contacts in the event of an incident are located on the [Intranet](https://intranet.justice.gov.uk/guidance/knowledge-information/protecting-information/information-assurance-roles/).

### Decommissioning domains

-   **POL.DOM.017:** Any decommissioned domain be transferred to the team. Contact them at on behalf of departmental teams or ALBs, and providing appropriate HTTP redirections to a suitable URL, for example, `301` or `302`.

-   **POL.DOM.018:** Domains registered pre-policy be moved to the team.

-   **POL.DOM.019:** The allow decommissioned domains to expire if there is no risk to the via "Domain Squatting" or "Phishing" attacks, or value in registering them defensively.

-   **POL.DOM.020:** Any decommissioned domains be added and managed in a risk register.


## Enforcement

-   **POL.DOM.021:** domains discovered that do not abide by the statements set out in this policy be treated as suspicious, reported to NCSC, and blocked automatically.

-   This policy is enforced by lower-level policies, standards, procedures and guidance.

-   Non-conformance with this policy could result in disciplinary action taken as per the department's disciplinary procedures. This could result in penalties up to and including dismissal. If an employee commits a criminal offence, they might also be prosecuted. In such cases, the department always cooperates with the relevant authorities and provides appropriate evidence.


## Contact details

organisations should contact for assistance with domain registrations, defensive domain registrations, transfers and operations.

