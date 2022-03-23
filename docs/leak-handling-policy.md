# Leak handling policy

This document describes the leak handling policy for the Ministry of Justice \(MoJ\).

To help identify formal policy statements, each is prefixed with an identifier of the form: POLLEAKxxx, where xxx is a unique ID number.

Information on following the policy may be found in the associated [leak handling process](leak-handling-process.md).

**Related information**  


[Leak handling process](leak-handling-process.md)

## Audience

This policy is aimed at all other staff working for or supplying services to the MoJ. This includes General users, Technical users, contractors, third parties, and Service Providers.

## Purpose

The purpose of this document is to define the requirements and policy for handling leaks associated with or affecting the MoJ.

`POLLEAK001:` Any exceptions to the policy **SHALL** be managed through the MoJ's security risk management process.

## Applicability

This policy applies to all MoJ owned or managed services or information provided or used for any business purpose.

## Enforcement

This policy is enforced by lower-level policies, standards, procedures, and guidance.

Non-conformance with this policy could result in disciplinary action taken in accordance with the MoJ's disciplinary procedures. This could result in penalties up to and including dismissal. If an employee commits a criminal offence, they might also be prosecuted. In such cases, the department always cooperates with the relevant authorities and provides appropriate evidence.

## Definition

A leak is an unauthorised disclosure of information into the public domain by an official.

A useful test is to consider whether the person or system receiving the information is authorised to do so. Do they have a "need to know for business purposes"? If there is no authorisation or need to know, then the disclosure is probably a leak.

A leak often takes place, but not always, with the intention of furthering the private interests of the person leaking the information, or of others. Such leaks are considered to be malicious.

Leaks can also be accidental or unintentional, for example, as a result of security vulnerabilities or someone leaving a document uncollected in a printer.

A leak is different to a data breach, although there are some similarities. The distinction is that in a data breach, specific data is sought to answer a malicious objective. An attack is planned and targeted at obtaining the corresponding data. Specific tools or techniques are deployed and used to gain access to the data. These tools or techniques can be detected by security tooling and processes.

By contrast, a leak is less controlled or targeted. It typically takes place using existing business tools or processes, making it harder to detect.

## Information classification

The amount of data or information being leaked can vary, from entire documents or reports, down to single sentences or diagrams.

`POLLEAK002:` This policy **SHALL** apply to all leaks, regardless of the quantity of data or information involved.

It is important to take into account the [information classification](information-classification-handling-and-security-guide.md) of the data, information, service or system.

`POLLEAK003:` A leak situation **CAN NOT** apply to any data or information containing only `OFFICIAL` material that does not have a handling caveat such as `OFFICIAL-SENSITIVE`.

`POLLEAK004:` A leak situation **CAN** apply to any data or information containing `OFFICIAL` material that does have a handling caveat such as `OFFICIAL-SENSITIVE`.

`POLLEAK005:` A leak situation **CAN** apply to any data or information containing `SECRET` or `TOP SECRET` material.

`POLLEAK006:` A leak situation **MIGHT** apply to the access rights for a system where data or information is located. For example, if a URL link of an `OFFICIAL` document that is located on an `OFFICIAL-SENSITIVE` system or above is sent to a user or third party, but they do not have access rights to the system to open it, it is a leak of the system but not the content.

**Note:** Consider the case of someone who has the correct access rights to both some information and the system hosting the information. They then print a copy of the information and gives it to another user or a third party. In this case, it is not considered a leak of the system because the initial access to the information was by someone who was authorised to access both the information and the system hosting the information. However, the disclosure of the information to the other user or the third party might be an information leak, depending on whether the recipients of the information were authorised to receive the information.

### Classifying draft information

Work in progress activities, or draft information, might also be the subject of a leak.

`POLLEAK007:` Draft content **SHALL** be labelled correctly to confirm the security classification or the security handling requirements that apply to it.

For example, someone might be unsure of a draft document's security classification. It might be prudent to classify the draft as `OFFICIAL-SENSITIVE` or higher until the document is approved and a final classification determined.

## Other applicable policy

`POLLEAK008:` To minimise the possibility of a leak occurring, all users **SHALL** comply with MoJ policy, in particular, the [acceptable use policy](acceptable-use-policy.md), user access management as part of the [access control policy](access-control-policy.md), and the [information classification, handling and security guide](information-classification-handling-and-security-guide.md).

## Harm that leaks cause

Examples of harm caused by leaks include:

-   Reputational damage, undermining trust and good government.
-   Adverse effects on UK Government policies, or relationships with other countries.
-   Financial problems involving market-sensitive information that is critical to the UK economy.

## Accidental leaks

A lack of due diligence in an environment **MIGHT** lead to sensitive MoJ information being Overseen, Overheard, or Overshared.

An example would be the publication of sensitive information to an unintended audience by clicking "reply all" on an email, or having the "email auto-forward" capability active on your account.

## Malicious leaks

Malicious leaks are intentional. They are planned. They are deliberate. They will often bypass controls and mechanisms intended to prevent accidental leaks.

Examples of malicious leaks would include:

-   Someone within the MoJ shares confidential MoJ information through the web, using email, or using mobile data storage devices such as optical media, USB keys, and laptops.
-   Deliberately sending confidential information to any unauthorised audience, by knowingly including that audience in an email reply, or setting up the "email auto-forward" capability on your account to include that audience.

## Consequences

Any civil servant found to have perpetrated a leak could face disciplinary proceedings, with consequences up to and including dismissal. In addition, in extreme cases where an offence has been committed under the [Official Secrets Act 1989](https://www.legislation.gov.uk/ukpga/1989/6/contents), there might be a police investigation that could result in a criminal conviction.

This leak handling policy complements the [MoJ Conduct Policy](https://intranet.justice.gov.uk/documents/2015/04/conduct-policy.pdf), which states:

> You will not release official information unless you are authorised to do so. If you release official information without authority, your manager may take action under the disciplinary procedure.

This leak handling guidance is based upon:

-   The [Civil Service Code of Conduct](https://www.gov.uk/government/publications/civil-service-code/the-civil-service-code), which sets out values for all civil servants.
-   Rules that affect civil servants, such as confidentiality and appropriate behaviour.
-   Conduct that meets the MoJ organisational values.

## Incidents

**Note:** If you work for an agency or ALB, refer to your local incident reporting guidance.

**Operational Security Team**

-   Email: [OperationalSecurityTeam@justice.gov.uk](mailto:OperationalSecurityTeam@justice.gov.uk)
-   Slack: `#security`

## Contact details

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for cyber security advice, contact the Cyber Assistance Team: [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

