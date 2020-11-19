# Secure Email Transfer Guide

**Parent topic:**[Email Security Guide](email-security-guide.md)

## Introduction

This guide instructs technical users of the services and encryption tools they should use to securely transfer information via email. This guide is a sub-page to the [Email Security Guide](email-security-guide.md).

You should ensure that email communication is sufficiently secured before transferring sensitive information, such as:

-   `OFFICIAL-SENSITIVE` classified information such as personal data.
-   API and other application keys/credentials \(including within containers\).
-   SSH Keys.
-   Database and other system-to-system passwords.
-   Private certificates for secure communication, transmitting and receiving of data \(TLS, SSL etc.\)
-   Private encryption keys.
-   RSA and other one-time password information.

## Transport Layer Security

Technical users should ensure that any service that is capable of sending and receiving email uses enforced TLS to encrypt messages:

-   The Ministry of Justice \(MoJ\) should always use the latest version of TLS.
-   TLS is required for sending to `gov.uk`.
-   Any MoJ domains that do not support TLS must be documented in an exceptions list and an exception rule authorised by the DNS provider. Refer to the [Email Authentication Guide](email-authentication-guide.md) for DNS provider contact details.
-   Where mandatory TLS encryption is not suitable:
    -   Use certificates from Certificate Authorities, making sure they are always valid and use strong encryption, algorithms and key lengths.
    -   Use Secure Multipurpose Internet Mail Extension \(S/MIME\) as it signs and encrypts email data before it is transmitted.
-   If you operate an internet-facing email service, you must buy and manage appropriate TLS certificates from the [Digital Marketplace](https://www.digitalmarketplace.service.gov.uk/).

The Information Classification Handling and Security Guide offers further advice on encrypting email communications. This includes protecting data at rest and data in transit.

For further guidance on TLS, please see the [Cryptography](cryptography.md) guidance.

## End-to-end encryption

End-to-end email encryption ensures only the sender and receiver can read email messages. Data is encrypted on the sender's system and only the intended recipient will be able to decrypt and read it. Microsoft provides end-to-end encryption for email communications; if you are using a different service provider you may want to implement transit encryption for your users with a third party app that provides end-to-end encryption. Contact the Operational Security Team for further advice: [OperationalSecurityTeam@justice.gov.uk](mailto:OperationalSecurityTeam@justice.gov.uk).

## Secure email transfer options

Technical users must select the most suitable system for their users and configure it appropriately. This section provides the various options available.

|Secure Messaging Options|Examples|
|------------------------|--------|
|Cloud Email Solutions \(securing to the Government Secure Standard\)|Office 365 \(`@justice.gov.uk`\) or Google Workspace \(`@digital.justice.gov.uk`\)|
|Supplementary Email Solutions|CJSM|

## Cloud email solutions

These are cloud email solutions that are configured to the [government secure standard](https://www.gov.uk/guidance/securing-government-email). Technical Users should ensure that such systems provide assurance of compliance to this standard and confidence for the exchange of information.

## Google mail

Google mail provided as part of Google Workspace uses Transport Layer Security \(TLS\) to automatically encrypt incoming and outgoing emails, but this only works if the email providers of both the sender and the recipient always use TLS. If required, S/MIME encryption can be enabled by contacting the Operational Security Team: [OperationalSecurityTeam@justice.gov.uk](mailto:OperationalSecurityTeam@justice.gov.uk).

## Office 365

By default, all emails in Office 365 are sent using Opportunistic TLS. If a TLS connection cannot be established, the message will be sent in plain text using Simple Mail Transfer Protocol \(SMTP\). If TLS must always be applied, contact the Operational Security Team: [OperationalSecurityTeam@justice.gov.uk](mailto:OperationalSecurityTeam@justice.gov.uk). In this configuration, certificate verification is required whenever mail is sent from a third party to the MoJ.

Outlook \(the email client within Office 365\) supports two other encryption options:

1.  S/MIME encryption - to use S/MIME encryption, the sender and recipient must have a mail application that supports the S/MIME standard. Outlook supports the S/MIME standard.
2.  Office 365 Message Encryption \(Information Rights Management\) - to use Office 365 Message Encryption, the sender must have Office 365 Message Encryption configured.

Microsoft currently provides additional tools to [secure information via email](https://www.microsoft.com/en-us/microsoft-365/blog/2018/04/05/defend-yourself-from-cybercrime-with-new-office-365-capabilities/).

If either of these additional encryption methods is required, please contact the Operational Security Team: [OperationalSecurityTeam@justice.gov.uk](mailto:OperationalSecurityTeam@justice.gov.uk).

## Criminal Justice Secure Mail

[Criminal Justice Secure Mail \(CJSM\)](cjsm.md) provides a closed email service between Criminal Justice Agencies \(CJAs\) and Criminal Justice Practitioners \(CJPs\). CJSM must not be used from public or personal computers. CJSM should only be used for legitimate business purposes relating to the Criminal Justice System.

Examples of CJAs within the GSC are:

-   Police.
-   Prison Service.
-   Court Service.
-   CPS.
-   Probation Service.

Examples of agencies and CJPs outside the GSC are:

-   Youth Offending Teams.
-   Victim Support.
-   Solicitors and Barristers.

CJSM offers two mechanisms for connection:

1.  CJSM mailbox \(webmail\) hosts a mailbox on behalf of the user. A user accesses the mailbox via either a standard internet browser or a POP3 email client.
2.  CJSM server connection \(SMTP\) is deployed to act as an encryption proxy for any email traffic containing a destination address ending in `cjsm.net`. All CJSM servers require a certificate issued by Egress to be installed. Session keys are established for each transaction.

✔ All MoJ users can send or receive over CJSM by adding `.CJSM.net` to the end of their MoJ email address.

✔ CJSM may only be used to share information up to and including `OFFICIAL-SENSITIVE`.

✔ CJSM cannot be used with multi-client mail relay services like Mailgun, Mailchimp or AWS SES.

For further guidance contact the [CJSM Helpdesk](mailto:cjsm.helpdesk@egress.com). Further information is available at: [https://www.cjsm.justice.gov.uk/training/index.html](https://www.cjsm.justice.gov.uk/training/index.html).

## External emails

Technical users must ensure that all outgoing emails are automatically appended with a [disclaimer](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/it-security-guidelines/).

## Auto-forward

Technical users should ensure auto-forwarding is used responsibly and in line with the MoJ's Information Classification Handling and Security Guide. As part of this responsibility they must:

-   Disable auto-forward to external domains. Where this is required it should be controlled by creating custom RBAC roles.
-   Advise users to only forward emails from an MoJ email address to an email address that provides the same or higher security standards.
-   Not provide auto-forward capability when any MoJ standard, policy or guidance states that additional controls or protection must be implemented before sending an email.

## Contact details

-   Contact the Cyber Assistance Team for specific advice on IT security: [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).
-   For any further questions relating to security, contact: [security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk).
-   [To report an incident](reporting-an-incident.md).
-   Suppliers to the MoJ should first ask their usual MoJ points of contact.

