# Spam and Phishing Guide

**Parent topic:**[Email Security Guide](email-security-guide.md)

## Introduction

This guide outlines the technical implementations you, as technical users, should make to keep Ministry of Justice \(MoJ\) systems secure. This guide is a sub-page to the [Email Security Guide](email-security-guide.md).

## Common email threats

### Spam and phishing

To protect against spam and phishing attacks, the MoJ will make use of government services such as the National Cyber Security Centre's [Suspicious Email Reporting Service](mailto:report@phishing.gov.uk) and any other services that are appropriate.

### Spoofing attacks

Spoofing attacks may be mitigated by:

-   Implementing SPF, DKIM and DMARC e.g. sender information

    ```
    from
    ```

    ,

    ```
    reply-to
    ```

    ,

    ```
    return-path
    ```

    and even

    ```
    x-origin
    ```

    can be spoofed \(please refer to the [Email Authentication Guide](email-authentication-guide.md) for further guidance\).

-   Using secure email gateways.
-   Implementing access controls, such as [multi factor authentication\(MFA\)](multi-factor-authentication-mfa-guide.md), to avoid an attacker gaining access to credentials for an email account where they could legitimately spoof the sender's email address.

## Protecting a parked domain

DMARC must also be implemented on non-email sending domains as they can be easily be used for email spoofing and phishing.

-   Once parked domains are protected, they must be configured to automatically renew by default. If you are a domain owner you should aim to do the following to protect a parked domain:
    1.  Create a SPF record with no permitted senders so that no IP is authorised to send email for your parked domain.
    2.  Include a RUA address to which aggregate reports can be sent. These will provide you with visibility of potential abuse.
    3.  If you have an

        ```
        A
        ```

        record on your domain, but no

        ```
        MX
        ```

        records, you should create a null

        ```
        MX
        ```

        record to immediately fail any email to that domain.

-   Create a record of type

    ```
    MX
    ```

    , with a priority of 0 \(highest priority\).

    A null DKIM record isn't required, as email will be treated the same as if it had no record at all. However, recipients may treat a null DKIM record with extra caution, as it explicitly revokes any keys that may be cached.


Some interfaces may not allow you to implement all these steps but implement as many as possible.

### Compromised email systems

Compromised email systems are often used to deliver spam messages and conduct phishing. It is recommended that email systems are protected by [multi factor authentication](multi-factor-authentication-mfa-guide.md) where possible to mitigate this risk.

Such account takeovers should be reported as an incident in compliance with the [IT Incident Management Guide](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/incident-management-plan-and-process-guide/).

### Accidental disclosure

Not all security threats are intentional. Authorised users may accidentally send proprietary information via e-mail to unintended recipients. Where these incidents are reported incident managers should refer to the [IT Incident Management Guide](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/incident-management-plan-and-process-guide/) for further guidance.

### Man-in-the-Middle \(MITM\) attacks

MITM attacks can result in unauthorised access to email whilst in transit and are often used to gain access to sensitive information.

You can mitigate MITM attacks by:

-   Configuring Secure/Multipurpose Internet Mail Extensions to encrypt emails and provide unique digital certificates.
-   Implementing certificate based authentication for all end user machines and devices, for example printers with email services enabled.
-   Using TLS certificates which activate HTTPS protocol to provide a secure connection between the MoJ and third parties on webmail portals.
-   Using SMTPS \(encrypted by TLS\) rather than unencrypted SMTP.

## Mail Check

Mail Check is a NCSC cyber defence service that enables email administrators to improve and maintain the security of email domains by preventing spoofing attacks. All domains operated by, or on behalf of the MoJ, must be added to Mail Check, regardless of whether the domain is expected to send or receive emails. All future contracts and agreements with third party suppliers must make this a requirement.

Mail Check should only be used if the email domain name provided is publicly routable from the internet via Simple Mail Transfer Protocol \(SMTP\).

Digital and Technology users must contact the [NCSC Mail Check team](mailto:mailcheck@digital.ncsc.gov.uk) to have domains added to the MoJ's subscription of the Mail Check service.

## Email sandboxing

Sandboxing provides an additional layer of protection in which any email that contains URLs, attachments or suspicious senders can be securely checked for malicious content before they reach the network or mail server. If the email is found to be harmful it will not be delivered. Sandboxing is beneficial as it:

-   Mirrors the end user's computer and provides a secure space to interact with and analyse harmful communications.
-   Allows developers and technical architects to actively minimise the impact of a threat.

For further guidance on implementing sandboxing, including which products you should use, contact the Operational Security Team: [OperationalSecurityTeam@justice.gov.uk](mailto:OperationalSecurityTeam@justice.gov.uk).

## URL link rewriting

URL link rewriting is a technique used to detect malicious links in emails. Links in emails are actively scanned and rewritten to point to an Advanced Threat Protection gateway where the following checks occur:

-   Check the link to see if it is blacklisted by the MoJ or has been previously malicious.
-   If the link points to downloadable content, the content is scanned.

After the checks have completed, it will either allow the user to continue to the URL or block them from accessing it. Where the user has been blocked, URL rewriting should provide them with a message containing contact details to get help.

## Protecting against email security threats

To provide protection against email security threats, implement the following controls:

-   Implement anti-malware software. Refer to the [Malware Protection Guidance](malware-protection-guide-introduction.md) for more information.
-   Install only the minimal mail server services required. Eliminate known vulnerabilities through patches, configurations and upgrades. Refer to the Vulnerability Scanning and Patch Management Guide for more information.
-   Implement external email warning messages to insert text \(usually in the subject line\) into an email when it is identified as coming from outside of the MoJ[1](#fntarg_1).
-   Develop email security management plans to define best practices for employees.
-   Use SMTP alert policies to track malware activity and data loss incidents from anti-malware software.
-   Ensure there is no unnecessary detail on the MoJ website or webmail by considering what visitors need to know with the aim of reducing the threat of spear phishing.
-   Restrict auto-forwarding. Refer to the [Secure Email Transfer Guide](secure-email-transfer-guide.md) for more information.
-   Restrict delegate access. Refer to the [Email Security Guide](email-security-guide.md) for more information.

The [Email Authentication Guide](email-authentication-guide.md) provides further detail on the email authentication controls mentioned in this guide.

## Reporting spam or malicious emails

If you think your email service provision has been susceptible to spam or a virus, report it immediately to the Technology Service Desk as an IT security incident. Please refer to the [IT Incident Management Policy](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/it-incident-management-policy/) for further guidance.

## Incidents

**Note:** If you work for an agency or ALB, refer to your local incident reporting guidance.

Operational Security Team:

-   Email: [OperationalSecurityTeam@justice.gov.uk](mailto:OperationalSecurityTeam@justice.gov.uk)
-   Slack:

    ```
    #security
    ```


## Contact details

-   Contact the Cyber Assistance Team for specific advice on IT security: [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).
-   For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).
-   [To report an incident](reporting-an-incident.md).
-   Suppliers to the MoJ should first ask their usual MoJ points of contact.

[1](#fnsrc_1) An external email service is any service that is outside the ```
gov.uk
```

 domain.

