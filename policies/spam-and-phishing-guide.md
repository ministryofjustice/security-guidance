---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](../..)

[eag]: ../email-authentication-guide/

# Spam and Phishing Guide

## Introduction

This guide explains the different types of email attacks that can threaten MoJ security and the technical implementations you should make to keep MoJ systems secure. This guide is a sub-page to the Email Security Guide.

## Common email threats

### Spam and phishing

Phishing emails are often formatted to look like legitimate emails in an attempt to deceive the recipient into completing an urgent action. The intended result of phishing emails is to impact the recipients' data or IT system's confidentiality, integrity or availability for monetary gain, typically using malware or impersonation tactics.

To protect against such attacks, the MoJ will make use of government services such as The National Cyber Security Centre's [Suspicious Email Reporting Service](mailto:report@phishing.gov.uk) and any other services that are appropriate.

### Spoofing attacks

Spoofing attacks are designed to mislead the recipient into trusting that a malicious email is delivered from a legitimate source. This may include altering names and email addresses; and disguising the true origin of websites, IP addresses and Domain Name System servers. For example, a legitimate sender could be _`example.com`_ but an illegitimate sender might email from _`exemple.com`_.

You can prevent spoofing attacks by:

* implementing SPF, DKIM and DMARC e.g. sender information `from`, `reply-to`, `return-path` and even `x-origin` can be spoofed (please refer to the [Email Authentication Guide][eag] for further guidance)
* using secure email gateways
* implementing access controls, such as multi factor authentication (MFA) , to avoid an attacker gaining access to credentials for an email account where they could legitimately spoof the sender's email address.

### Man-in-the-Middle (MITM) attacks

MITM attacks occur when threat actors intercept communications between two parties, for example using enforced TLS on your mail system does not guarantee TLS is truly enforced end to end, as there may be a break in encryption resulting in data being vulnerable to compromise. MITM attacks can result in unauthorised access to email accounts and are often used to gain sensitive information.

Compromised email systems are often used to deliver spam messages and conduct phishing.

Not all security threats are intentional. Authorised users may accidentally send proprietary information via e-mail to unintended recipients – where these incidents are reported incident managers should refer to the [IT Incident Management Guide](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/incident-management-plan-and-process-guide/) for further guidance.

You can prevent MITM attacks by:

* configuring Secure/Multipurpose Internet Mail Extensions to encrypt emails and provide unique digital certificates
* implementing certificate based authentication for all end user machines and devices (e.g. printers with email services enabled)
* using TLS certificates which activate HTTPS protocol to provide a secure connection between the MoJ and third parties on webmail portals
* using SMTPS (encrypted by TLS) rather than unencrypted SMTP.

## Protecting against email security threats

You can protect against email security threats by implementing the additional controls outlined below.

✔ Install the minimal mail server services required and eliminate known vulnerabilities through patches, configurations and upgrades. Refer to the [Vulnerability Scanning and Patch Management Guide](../vulnerability-scanning-and-patch-management-guide/) for more information.

✔ Implement anti-malware software where not already implemented. Refer to the [Malware Protection Guidance](../malware-protection-guide-introduction/) for more information.

✔ Implement URL Link Rewriting e.g. to check bit/ly links - adding the `+` symbol at the end of bit/ly links will direct you to the location without opening the link.

✔ Develop email security management plans to define best practices for employees.

✔ Use SMTP alert policies to track malware activity and data loss incidents.

✔ Use email filtering services and implement email sandboxing. Refer to the [Email Authentication Guide][eag] for further detail.

✔ Ensure there is no unnecessary detail on the MoJ website or webmail by considering what visitors need to know with the aim of reducing the threat of spear phishing.

✔ Restrict auto-forwarding. Please refer to the [Secure Email Transfer Guide](../secure-email-transfer-guide/) for more information.

✔ Restrict delegate access. Please refer to the [Email Security Guide](../email-security-policy/) for more information.

The [Email Authentication Guide][eag] provides further detail on the technical controls mentioned in this guide.

## Reporting spam or malicious emails

If you think your email service provision has been susceptible to spam or a virus, report it immediately to the Technology Service Desk as an IT security incident. Please refer to the [IT Incident Management Policy](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/it-incident-management-policy/) for further guidance.


## Contact details

* Contact the Technology Service Desk to report suspected IT Security Incidents:<br/>Telephone: 0800 917 5148.
* Contact Cyber Assistance Team for advice on email security – [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk)
* Contact the Operational Security Team for further advice – [Operationalsecurityteam@justice.gov.uk](mailto:Operationalsecurityteam@justice.gov.uk).
