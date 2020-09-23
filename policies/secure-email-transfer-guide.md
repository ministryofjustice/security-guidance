---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](home-security-policies-guides.md)

# Secure Email Transfer Guide

## Introduction

This guide instructs technical users of the services and encryption tools they should use to securely transfer information via email. You should ensure that email communication is sufficiently secured before transferring sensitive information, such as:

* `OFFICIAL-SENSITIVE` classified information such as personal data
* API and other application keys/credentials (including within containers)
* SSH Keys
* database and other system-to-system passwords
* private certificates for secure communication, transmitting and receiving of data (TLS, SSL etc.)
* private encryption keys, and
* RSA and other one-time password information.

## Transport Layer Security

Technical users should ensure that any service that is capable of sending and receiving email uses enforced TLS to encrypt messages.

* The MoJ should always use the latest version of TLS.
* TLS is required for sending to `gov.uk`.
* Any MoJ domains that do not support TLS must be documented in an exceptions list and an exception rule authorised by the DNS provider. Please refer to the [Email Authentication Guide](email-authentication-guide.md) for DNS provider contact details.
* Where mandatory TLS encryption is not suitable:
  * use certificates from Certificate Authorities, making sure they are always valid and use strong encryption, algorithms and key lengths, and
  * use Secure Multipurpose Internet Mail Extension (S/MIME) as it signs and encrypts email data before it is transmitted.
* If you operate an internet-facing email service, you must buy and manage appropriate TLS certificates from the [Digital Marketplace](https://www.digitalmarketplace.service.gov.uk/).

The [Information Classification Handling and Security Guide](information-classification-handling-and-security-guide.md) offers further advice on encrypting email communications. This includes protecting data at rest and data in transit.

For further guidance on TLS, please see the [Cryptography Standard](https://ministryofjustice.github.io/security-guidance/standards/cryptography/#cryptography).

## End-to-end encryption

End-to-end email encryption ensures only the sender and receiver can read email messages. Data is encrypted on the sender's system and only the intended recipient will be able to decrypt and read it. Microsoft provides end-to-end encryption for email communications; if you are using a different service provider you may want to implement transit encryption for your users with a third party app that provides end-to-end encryption. Please contact the Operational Security Team for further advice.

## Secure email transfer options

Technical users must select the most suitable system for their users and configure it appropriately.  This section provides the various options available.

| Secure Messaging Options | Examples |
|--- |---|
| Cloud Email Solutions (securing to the Government Secure Standard) | Office 365 (`@justice.gov.uk`) or Google G-Suite (`@digital.justice.gov.uk`) |
| Supplementary Email Solutions | CJSM |

## Cloud email solutions
These are cloud email solutions that are configured to the [government secure standard](https://www.gov.uk/guidance/securing-government-email), Technical Users should ensure that such systems provide assurance of compliance to this standard and confidence for the exchange of information.

## Google mail

Gmail uses Transport Layer Security (TLS) to automatically encrypt incoming and outgoing emails but this only works if the email providers of both the sender and the recipient always use TLS.
If required, S/MIME encryption can be enabled by contacting the Operational Security Team.

## Office 365

By default, all emails in Office 365 are sent using Opportunistic TLS. If a TLS connection cannot be established, the message will be sent in plain text using Simple Mail Transfer Protocol (SMTP). If TLS must always be applied, contact the Operational Security Team.  In this configuration, certificate verification is required whenever mail is sent from a third party to the MoJ.

Outlook supports two other encryption options:

1. S/MIME encryption - to use S/MIME encryption, the sender and recipient must have a mail application that supports the S/MIME standard - Outlook supports the S/MIME standard, and
2. Office 365 Message Encryption (Information Rights Management) - to use Office 365 Message Encryption, the sender must have Office 365 Message Encryption configured.

Microsoft currently provides additional tools to [secure information via email](https://www.microsoft.com/en-us/microsoft-365/blog/2018/04/05/defend-yourself-from-cybercrime-with-new-office-365-capabilities/).

If either of these additional encryption methods is required, please contact the [Operationalsecurityteam@justice.gov.uk](mailto:Operationalsecurityteam@justice.gov.uk).

## Criminal Justice Secure Mail

Criminal Justice Secure Mail (CJSM) provides a closed email service between Criminal Justice Agencies (CJAs) and Criminal Justice Practitioners (CJPs). CJSM must not be used from public or personal computers. CJSM should only be used for legitimate business purposes relating to the Criminal Justice System.

Examples of CJAs within the GSC are:

* Police
* Prison Service
* Court Service
* CPS
* Probation

Examples of agencies /CJPs outside the GSC are:

* Youth Offending Teams
* Victim Support
* Solicitors & Barristers.

CJSM offers two mechanisms for connection:

1. CJSM mailbox (webmail) - hosts a mailbox on behalf of the user.  A user accesses the mailbox via either a standard internet browser or a POP3 email client.
2. CJSM server connection (SMTP) - is deployed to act as an encryption proxy for any email traffic containing a destination address ending in `cjsm.net`. All CJSM servers require a certificate issued by Egress to be installed. Session keys are established for each transaction.

✔ All MoJ users can send or receive over CJSM by adding `.CJSM.net` to the end of their MoJ email address.

✔ CJSM may only be used to share information up to and including `OFFICIAL-SENSITIVE`.

✔ CJSM cannot be used with multi-client mail relay services like Mailgun, Mailchimp or AWS SES.

For further guidance contact the [CJSM Helpdesk](mailto:cjsm.helpdesk@egress.com) or further information is available at: [https://www.cjsm.justice.gov.uk/training/index.html](https://www.cjsm.justice.gov.uk/training/index.html).

## External emails

Technical users must ensure that all outgoing emails are automatically appended with a [disclaimer](https://intranet.justice.gov.uk/guidance/security/it-computer-security/ict-security-policy-framework/it-security-guidelines/).

## Auto-forward

Technical users should ensure auto-forwarding is used responsibly and in line with the MoJ's [Information Classification Handling and Security Guide](information-classification-handling-and-security-guide.md). As part of this responsibility they must:

* disable auto-forward to external domains, where this is required it should be controlled by creating custom RBAC roles
* advise users to only forward emails from an MoJ email address to an email address that provides the same or higher security standards
* not provide auto-forward capability when any MoJ standard, policy or guidance states that additional controls or protection must be implemented before sending an email.

## Contact details

* Contact the Cyber Assistance Team for advice on email security – [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk)
* Contact the Operational Security Team for further advice – [Operationalsecurityteam@justice.gov.uk](mailto:Operationalsecurityteam@justice.gov.uk)
