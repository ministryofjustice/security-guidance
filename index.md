
# Cyber and Technical Security Guidance

## Summary

This site documents some of the security decisions that the
[Ministry of Justice (MoJ)](https://www.gov.uk/government/organisations/ministry-of-justice)
has made for the products we operate, and our relationships with suppliers.

[Technical guidance](https://ministryofjustice.github.io/technical-guidance/) covers technical decisions in the MoJ more widely.

## Background

*Government Functional Standard - GovS 007: Security* replaces the HMG Security Policy Framework (SPF) last published in May 2018. It also incorporates the *Minimum Cyber Security Standard (MCSS)* which defines the minimum security measures that departments implement with regards to protecting their information, technology and digital services to meet their SPF and National Cyber Security Strategy obligations.

Sections 6.12 Cyber security and 6.13 Technical security of the standard state:

> - The security of information and data is essential to good government and public confidence. To operate effectively, HMG needs to maintain the confidentiality, integrity and availability of its information, systems and infrastructure, and the services it provides. Any organisation that handles government information shall meet the standards expected of HM Government.
> - Technical security relates to the protection of security systems from compromise and/or external interference that may have occurred as a result of an attack.

## Taxonomy

MoJ has developed their cyber and technical security taxonomy as follows:

| Level 1 | Level 2 | Documents |
| --- | --- | --- |
| Cyber | Access Control | ... |
| | Asset Management | ... |
| | Cryptography | ... |
| | Operational Security | ... |
| Technical | Data and Information | ... |
| | Incident Management | ... |
| | Software Development | ... |

Documents have been developed and defined within this taxonomy, and are listed in the next section together with their suggested target audiences.

## Document List

| Level 1 | Level 2 | Documents | Target Audience |
| --- | --- | --- | --- |
| Cyber | Access Control | [Access Control Guide](https://github.com/ministryofjustice/security-guidance/blob/Local/policies/access-control-guide.md) | Technical Architect, DevOps, IT Service Manager, Software Developer |
| | | JML process | |
| | | [Managing User Access Guide](https://github.com/ministryofjustice/security-guidance/blob/Local/policies/managing-user-access-guide.md) |  |
| | | [Minimum User Clearance Levels Guide](https://github.com/ministryofjustice/security-guidance/blob/Local/policies/minimum-user-clearance-requirements-guide.md) | |
| | | [Multi-Factor Authentication](https://github.com/ministryofjustice/security-guidance/blob/Local/policies/multi-Factor-authentication-mfa-guide.md) | |
| | | [Multi-user Accounts and Public-Facing Service Accounts Guide](https://github.com/ministryofjustice/security-guidance/blob/Local/policies/multi-user-accounts-and-public-facing-service-accounts-guide.md) | |
| | | [Password Changes, Account Locks and Disabling Accounts Guide](https://github.com/ministryofjustice/security-guidance/blob/Local/policies/password-changes-account-locks-and-disabling-accounts-guide.md) | |
| | | [Password Creation and Authentication Guide](https://github.com/ministryofjustice/security-guidance/blob/Local/policies/password-creation-and-authentication-guide.md) | |
| | | [Password Management Guide](https://github.com/ministryofjustice/security-guidance/blob/Local/policies/password-management-guide.md) | |
| | | [Password Storage and Management Guide](https://github.com/ministryofjustice/security-guidance/blob/Local/policies/password-storage-and-management-guide.md) | |
| | | [Privileged Account Management Guide](https://github.com/ministryofjustice/security-guidance/blob/Local/policies/privileged-account-management-guide.md) | |
| | | [Privileged User Guide](https://github.com/ministryofjustice/security-guidance/blob/Local/policies/privileged-user-guide.md) | |
| | | [Privileged User Guide - Backups Removable Media and Incident Management Guide](https://github.com/ministryofjustice/security-guidance/blob/Local/policies/privileged-user-backups-removable-media-and-incident-management-guide.md) | |
| | | [Privileged User Guide - Configuration Patching and Change](https://github.com/ministryofjustice/security-guidance/blob/Local/policies/privileged-user-configuration-patching-and-change-management-guide.md) | |
| | | [Privileged User Guide - Logging Guide](https://github.com/ministryofjustice/security-guidance/blob/Local/policies/privileged-user-logging-and-protective-monitoring-guide.md) |
| | Asset Management | Accessing MoJ Systems from Abroad | |
| | | General User Video and Messaging Apps Guidance | |
| | | Patch Management Guide | |
| | | Remote Working | |
| | | Taking IT Equipment Abroad | |
| | | Vulnerability Scanning and Patch Management Guide | |
| | | Vulnerability Scanning Guide | |
| | Cryptography |
| | Operational Security | [Email Authentication Guide](./policies/email-authentication-guide/) | |
| | | [Email Security Policy](./policies/email-security-policy/) | MoJ Digital and Technology staff implementing controls throughout technical design, development, system integration and operation. Incident Managers. Any other party designing, developing or supplying services for the MoJ |
| | | [IT Security Policy](./policies/it-security-policy/) | As above |
| | | [Malware Protection Guide (Overview)](./policies/malware-protection-guide-introduction/) | As above |
| | | [Malware Protection Guide: Defensive Layer 1](./policies/malware-protection-guidance-defensive-layer-1) | |
| | | [Malware Protection Guide: Defensive Layer 2](./policies/malware-protection-guidance-defensive-layer-2) | |
| | | [Malware Protection Guide: Defensive Layer 3](./policies/malware-protection-guidance-defensive-layer-3) | |
| | | Secure Email Transfer Guide | |
| | | Spam and Phishing Guide | |
| | | Technical Controls Guide Introductory Page | |
| | | Technical Controls Guide - Layer 1 | |
| | | Technical Controls Guide - Layer 2 | |
| | | Technical Controls Guide - Layer 3 | |
| Technical | Principles | [Data Security & Privacy](./security_decisions/principles/data-security-and-privacy/) | |
| | | [IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER](./security_decisions/principles/identify-protect-detect-respond-recover/) | |
| | | [Maintained by Default](./security_decisions/principles/maintained-by-default/) | |
| | | [Secure by Default](./security_decisions/principles/secure-by-default/) | |
| | | [Security Log Collection](./security_decisions/principles/security-log-collection/) | |
| | | [Shared Responsibility Models](./security_decisions/principles/shared-responsibility-models/) | |
| | Data and Information | Information Security Policy | |
| | | Information Classification Handling and Security Guide | |
| | Incident Management |
| | Software Development |

## Other Guidance

### Intranet

There are other cyber and technical security guidance documents available to reference. A large number of these documents are available in the [IT and Computer Security](https://intranet.justice.gov.uk/guidance/security/it-computer-security/) repository on the MoJ Intranet, but these documents are currently being reviewed and progressively are being incorporated into the main [Security Guidance](https://ministryofjustice.github.io/security-guidance/#moj-security--guidance) repository as detailed above.

### GitHub Library

This library documents the security decisions that the MoJ has made for the products it operates, and its relationships with suppliers.

## References

![](https://github.com/ministryofjustice/security-guidance/blob/Local/images/GovS_007_Thumbnail.png) Government Functional Standard - GovS 007: Security

====


## Policies

{% assign policies = site.pages
  | where: "policy", true
  | group_by: "category" %}

{% for policy_group in policies %}
{% if policy_group.name != "" %}
### {{ policy_group.name }}
{% else %}
### General policies
{% endif %}

{% for policy in policy_group.items %}
- [{{ policy.title }}]({{ policy.url | relative_url }})
{% endfor %}
{% endfor %}

## Standards

{% assign standards = site.pages
  | where: "standard", true
  | group_by: "category" %}

{% for standard_group in standards %}
{% if standard_group.name != "" %}
### {{ standard_group.name }}
{% else %}
### General standards
{% endif %}

{% for standard in standard_group.items %}
- [{{ standard.title }}]({{ standard.url | relative_url }})
{% endfor %}
{% endfor %}

## Guides

{% assign guides = site.pages
  | where: "guide", true
  | group_by: "category" %}

{% for guide_group in guides %}
{% if guide_group.name != "" %}
### {{ guide_group.name }}
{% else %}
### General guides
{% endif %}

{% for guide in guide_group.items %}
- [{{ guide.title }}]({{ guide.url | relative_url }})
{% endfor %}
{% endfor %}

## Suppliers to MOJ

{% assign suppliers = site.pages
  | where: "supplier", true
  | group_by: "category" %}

{% for supplier_group in suppliers %}
{% if supplier_group.name != "" %}
### {{ supplier_group.name }}
{% else %}
### General notes to suppliers
{% endif %}

{% for supplier in supplier_group.items %}
- [{{ supplier.title }}]({{ supplier.url | relative_url }})
{% endfor %}
{% endfor %}

## Mythbusting

{% assign mythbustings = site.pages
  | where: "mythbusting", true
  | group_by: "category" %}

{% for myth_group in mythbustings %}
{% if myth_group.name != "" %}
### {{ myth_group.name }}
{% endif %}

{% for myth in myth_group.items %}
- [{{ myth.title }}]({{ myth.url | relative_url }})
{% endfor %}
{% endfor %}

## Technical Guidance

The [technical guidance](https://ministryofjustice.github.io/technical-guidance/) should be read together with this security-focused guidance.

## Getting in touch

{% assign contacts = site.pages
  | where: "contact", true
  | group_by: "category" %}

{% for contact_group in contacts %}
{% if contact_group.name != "" %}
### {{ contact_group.name }}
{% else %}
### General information
{% endif %}

{% for contact in contact_group.items %}
- [{{ contact.title }}]({{ contact.url | relative_url }})
{% endfor %}
{% endfor %}
