# Secure Email Transfer Guide

This guide provides technical users with information about the services and encryption tools for transferring information securely using email. Ensure that email communication is sufficiently secured before transferring sensitive information. Examples of sensitive information include:

-   **Official-Sensitive** classified information such as personal data.
-   API and other application keys or credentials, including within containers.
-   SSH keys.
-   Database and other system-to-system passwords.
-   Private certificates for secure communication, transmitting, or receiving data using protocols such as TLS or SSL.
-   Private encryption keys.
-   RSA and other single-use password information.

**Related information**  


[Email Security Guide](email-security-guide.md)

## Transport Layer Security

Ensure that any service capable of sending and receiving email uses enforced TLS to encrypt messages:

-   The Ministry of Justice \(MoJ\) **should** always use the latest version of TLS.
-   TLS **shall** always be used when sending to `gov.uk` domains.
-   Any MoJ domains that do not support TLS **shall** be documented in an exceptions list, and an exception rule authorised by the DNS provider. Refer to the [Email Authentication Guide](email-authentication-guide.md) for DNS provider contact details.
-   Where mandatory TLS encryption is not suitable:
    -   Use certificates from Certificate Authorities, making sure they are always valid and use strong encryption, algorithms, and key lengths.
    -   Use [Secure Multipurpose Internet Mail Extension \(S/MIME\)](https://en.wikipedia.org/wiki/S/MIME), as it signs and encrypts email data before it is transmitted.
-   If you operate an internet-facing email service, you **shall** buy and manage appropriate TLS certificates from the [Digital Marketplace](https://www.digitalmarketplace.service.gov.uk/).

The [Information Classification Handling and Security Guide](information-classification-handling-and-security-guide.md) offers further advice on encrypting email communications. This includes protecting data at rest, and data in transit.

For further guidance on TLS, refer to the [Cryptography](cryptography.md) guidance.

## End-to-end encryption

End-to-end email encryption ensures that only the sender and intended receiver can read email messages. Data is encrypted on the sender's system. Only the intended recipient is able to decrypt and read it. Many but not all email tools support end-to-end encryption for email communications. You might need to implement transit encryption for your users with a third party app that provides end-to-end encryption. Contact the [Security team](mailto:security@justice.gov.uk) for advice.

## Secure email transfer options

Select the most suitable system for service users, and configure it appropriately. This section provides guidance on the various options available.

**Note:** Remember that only MoJ email systems may be used for business purposes. Personal email accounts **shall not** be used for business purposes.

|Secure Messaging Options|Examples|
|------------------------|--------|
|Cloud Email Solutions \(securing to the Government Secure Standard\)|Microsoft Office 365 \(`@justice.gov.uk`\) or Google Workspace \(`@digital.justice.gov.uk`\)|
|Supplementary Email Solutions|CJSM|

## Cloud email solutions

These are tools that are configured to the [Government secure standard](https://www.gov.uk/guidance/securing-government-email). When evaluating a tool, ensure that it provides assurance of compliance to the Government standard, and provides confidence for the secure exchange of information.

## Google mail

Google mail is part of the Google Workspace service. It uses Transport Layer Security \(TLS\) to encrypt incoming and outgoing emails automatically. However, the email providers of both the sender and the recipient must always use TLS, otherwise the email transfer cannot be assured as secure. If required, S/MIME encryption might be suitable. To get help with this, contact the [Security team](mailto:security@justice.gov.uk).

## Office 365

By default, all emails in Office 365 are sent using Opportunistic TLS. If a TLS connection cannot be established, the message is sent in plain text using Simple Mail Transfer Protocol \(SMTP\). If TLS must be applied, contact the [Security team](mailto:security@justice.gov.uk) for help. In this configuration, certificate verification is required whenever mail is sent from a third party to the MoJ.

Outlook supports two other encryption options:

-   S/MIME encryption: to use S/MIME encryption, the sender and recipient must have a mail application that supports the S/MIME standard. Outlook supports the S/MIME standard.
-   Office 365 Message Encryption \(Information Rights Management\): to use Office 365 Message Encryption, the sender must have Office 365 Message Encryption configured.

Microsoft currently provides additional tools to [secure information via email](https://www.microsoft.com/en-us/microsoft-365/blog/2018/04/05/defend-yourself-from-cybercrime-with-new-office-365-capabilities/).

If either of these additional encryption methods is required, please contact the [Security team](mailto:security@justice.gov.uk).

## Criminal Justice Secure Mail

Criminal Justice Secure Mail \(CJSM\) provides a closed email service between Criminal Justice Agencies \(CJAs\), and Criminal Justice Practitioners \(CJPs\). CJSM **shall not** be used from public or personal computers. CJSM **should** be used only for legitimate business purposes relating to the Criminal Justice System.

Examples of CJAs within the GSC are:

-   Police
-   Prison Service
-   Court Service
-   CPS
-   Probation

Examples of agencies or CJPs outside the GSC are:

-   Youth Offending Teams
-   Victim Support
-   Solicitors and Barristers.

The CJSM offers two mechanisms for connection:

-   A CJSM mailbox \(webmail\) hosts a mailbox on behalf of the user. A user accesses the mailbox using either a standard internet browser, or a POP3 email client.
-   A CJSM server connection \(SMTP\) is deployed to act as an encryption proxy for any email traffic containing a destination address ending in `cjsm.net`. All CJSM servers require a certificate to be installed. The certificate is issued by Egress. Session keys are established for each transaction.

All MoJ users can send or receive over CJSM by adding `.CJSM.net` to the end of their MoJ email address.

CJSM **shall** only be used to share information up to and including **Official-Sensitive**.

CJSM **shall not** be used with multi-client mail relay services such as Mailgun, Mailchimp, or AWS SES.

For further guidance contact the [CJSM Helpdesk](mailto:cjsm.helpdesk@egress.com). Alternatively, further information is available at: [https://www.cjsm.justice.gov.uk/training/index.html](https://www.cjsm.justice.gov.uk/training/index.html).

## External emails

Ensure that all outgoing emails are automatically appended with a disclaimer.

If you are exchanging email with an outside organisation with which the **shall not** could be bound contractually, the following text must be appended:

> I am not authorised to bind the Ministry of Justice contractually, nor to make representations or other statements which may bind the Ministry of Justice in any way via electronic means.

## Auto-forward

Ensure that auto-forwarding is used responsibly, and in line with the MoJ's [Information Classification Handling and Security Guide](information-classification-handling-and-security-guide.md). In particular:

-   Disable auto-forward to external domains. If auto-forwarding to an external domain is required, it **should** be controlled by creating custom Role Based Access Control \(RBAC\) roles.
-   Advise users to only forward emails from an MoJ email address to an email address that provides the same or higher security standards.
-   Do not provide auto-forward capability when any MoJ standard, policy, or guidance states that additional controls or protection **shall** be implemented before sending an email.

## Contact details

For any further questions or advice relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

