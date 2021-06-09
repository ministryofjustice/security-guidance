# Spam and Phishing Guide

**Parent topic:** [Email Security Guide](email-security-guide.md)

## Introduction

This guide outlines the technical implementations that technical users should make to keep Ministry of Justice \(MoJ\) systems secure.

## Common email threats

### Spam and phishing

To protect against spam and phishing attacks, the MoJ makes use of Government services such as National Cyber Security Centre's [Suspicious Email Reporting Service](mailto:report@phishing.gov.uk) and any other services that are appropriate.

### Spoofing attacks

To mitigate spoofing attacks, use techniques such as:

-   Implementing [Sender Policy Framework \(SPF\)](https://en.wikipedia.org/wiki/Sender_Policy_Framework), [Domain Keys Identified Mail \(DKIM\)](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail), and [Domain-based Message Authentication, Reporting and Conformance \(DMARC\)](https://en.wikipedia.org/wiki/DMARC). Any sender information details such as `from`, `reply-to`, `return-path`, or even `x-origin` can be spoofed. For further guidance refer to the [Email Authentication Guide](email-authentication-guide.md).
-   Using secure email gateways.
-   Implementing access controls, such as [Multi-Factor Authentication \(MFA\)](multi-factor-authentication-mfa-guide.md), to avoid an attacker gaining access to credentials for an email account where they could plausibly spoof the sender's email address.

## Protecting a parked domain

DMARC **SHALL** also be implemented on non-email sending domains. This is because the domains might be used for email spoofing and phishing.

Once parked domains are protected, configure them to renew automatically by default.

If you are a domain owner, to protect a parked domain follow these steps:

1.  Create an SPF record with no permitted senders. This means that no IP address is authorised to send email for the parked domain.
2.  Include an `RUA` address. Aggregate reports can be sent to this address. The reports provide visibility of potential abuse.
3.  If you have an `A` record on your domain, but no `MX` records, create a “null” `MX` record that immediately fails any email to the parked domain. Give the `MX` record the highest priority \(`0`\).

A “null” DKIM record is not required. This is because email will be treated the same as if it had no record at all. However, recipients might treat a “null” DKIM record with extra caution, as it explicitly revokes any keys that might be cached.

Some interfaces might not allow you to implement all these steps. Implement as many as possible.

## Compromised email systems

Compromised email systems are often used to deliver spam messages and conduct phishing campaigns. Protect email systems by using [MFA](multi-factor-authentication-mfa-guide.md) where possible, to mitigate the risk.

Report any account takeovers or email compromise [as an incident](reporting-an-incident.md).

Following a report, incident managers should refer to the [Incident Management Plan and Process Guide](incident-management-plan-and-process-guide.md) for further guidance.

## Accidental disclosure

Not all security threats are intentional. Authorised users might accidentally send proprietary information to unintended recipients using email. Report these [as an incident](reporting-an-incident.md).

Following a report, incident managers should refer to the [Incident Management Plan and Process Guide](incident-management-plan-and-process-guide.md) for further guidance.

## Man-in-the-Middle attacks

Man-in-the-Middle \(MITM\) attacks might result in unauthorised access to email whilst the message is in transit. These attacks are used to gain access to sensitive information.

Mitigate MITM attacks by:

-   Configuring [Secure Multipurpose Internet Mail Extension \(S/MIME\)](https://en.wikipedia.org/wiki/S/MIME) to encrypt emails and provide unique digital certificates.
-   Implementing certificate based authentication for all end user machines and devices, for example printers with email services enabled.
-   Using TLS certificates which use the HTTPS protocol to provide a secure connection between the MoJ and third parties when using webmail portals.
-   Using SMTPS \(SMTP encrypted with TLS\) rather than unencrypted SMTP.

## Mail Check

[Mail Check](https://www.ncsc.gov.uk/information/web-check) is an NCSC cyber defence service. It enables email administrators to improve and maintain the security of email domains by preventing spoofing attacks. All domains operated by, or on behalf of, the MoJ, **SHALL** be added to Mail Check, regardless of whether the domain is expected to send or receive emails. All future contracts and agreements with third party suppliers **SHALL** make this a requirement.

Mail Check **SHOULD** be used only if the email domain name provided is publicly routable from the Internet using the Simple Mail Transfer Protocol \(SMTP\).

To add domains to the MoJ's Mail Check service subscription, contact the [NCSC Mail Check team](mailto:mailcheck@digital.ncsc.gov.uk).

## Email sandboxing

Sandboxing provides an additional layer of protection. Any email that contains URLs, attachments, or suspicious senders can be securely checked for malicious content before they reach the network or mail server. If the email is found to be harmful, it is not delivered. Sandboxing is beneficial, because it:

-   Mirrors the end user's computer, and provides a secure space to interact with and analyse potentially harmful communications.
-   Allows developers and technical architects to be proactive in minimising the impact of a threat.

For further guidance on implementing sandboxing, including which products you might use, contact the [Operational Security Team](mailto:OperationalSecurityTeam@justice.gov.uk).

## URL link rewriting

URL link rewriting is a technique used to detect malicious links in emails. Links in emails are actively scanned. They are then rewritten to point to an Advanced Threat Protection gateway, where two checks occur:

1.  Determine if the link is denylisted by the MoJ or has been previously identified as malicious.
2.  Scan downloadable content available at the link address.

After the checks have completed, the user continues to the URL or is blocked from access, depending on the results of the checks. If access is blocked, URL rewriting is used to provide an explanation and contact details for additional help.

## Protecting against email security threats

To provide protection against email security threats, implement the following controls:

-   Implement anti-malware software. Refer to the [Malware Protection Guidance](malware-protection-guide-introduction.md) for more information.
-   Install only the minimal mail server services required. Eliminate known vulnerabilities through patches, configuration, and upgrades. Refer to the [Vulnerability Scanning and Patch Management Guide](vulnerability-scanning-and-patch-management-guide.md) for more information.
-   Implement external email warning messages to insert text \(usually in the subject line\) into an email when it is identified as coming from outside of the MoJ.
-   Develop email security management plans to define best practices for employees.
-   Use SMTP alert policies to track malware activity and data loss incidents from anti-malware software.
-   Ensure there is no unnecessary detail on the MoJ website or webmail, by considering what visitors need to know with the aim of reducing the threat of spear phishing.
-   Restrict auto-forwarding. Refer to the [Secure Email Transfer Guide](secure-email-transfer-guide.md) for more information.
-   Restrict delegate access. Refer to the [Email Security Guide](email-security-guide.md) for more information.

**Note:** An external email service is any service that is outside the `gov.uk` domain.

The [Email Authentication Guide](email-authentication-guide.md) provides further detail on the email authentication controls mentioned in this guide.

## Reporting spam or malicious emails

If you think your email service provision has been susceptible to spam or a virus, report it immediately to the Technology Service Desk as an IT security incident. Please refer to the [IT Incident Management Policy](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/it-incident-management-policy/) for further guidance.

## Incidents

**Note:** If you work for an agency or ALB, refer to your local incident reporting guidance.

**Operational Security Team**

-   Email: [OperationalSecurityTeam@justice.gov.uk](mailto:OperationalSecurityTeam@justice.gov.uk)
-   Slack: `#security`

## Contact details

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for security advice, contact the Cyber Assistance Team [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

