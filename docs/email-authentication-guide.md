# Email Authentication Guide

This guide identifies the security controls that **shall** or **should** be implemented at the domain layer to verify sender's domains and mitigate spoofing attacks.

It is Ministry of Justice \(MoJ\) policy to follow and comply with [HMG Email Security policy](https://www.gov.uk/guidance/securing-government-email).

This means that the MoJ implements a number of controls for email systems:

-   [Sender Policy Framework](#sender-policy-framework)
-   [Domain Keys Identified Mail](#domain-keys-identified-mail)
-   [Domain-based Message Authentication, Reporting and Conformance](#domain-based-message-authentication-reporting-and-conformance)
-   [Mail Transfer Agent Strict Transport Security](#mail-transfer-agent-strict-transport-security)
-   [TLS Reporting](#tls-reporting)

**Related information**  


[Email Security Guide](email-security-guide.md)

## Sender Policy Framework

[Sender Policy Framework \(SPF\)](https://en.wikipedia.org/wiki/Sender_Policy_Framework) **should** be implemented for email domains. SPF enables organisations to publish a Domain Name System \(DNS\) record of all the domains and IP addresses which are trusted for sending and receiving email.

SPF is verified by checking a specific `TXT` DNS entry in emails. Emails are flagged if they are not sent from the domains and IP addresses published in the DNS record.

The MoJ enforces SPF controls to help users spot spoofed or unknown email addresses. Suspicious emails are sent directly to the "spam" folder, instead of to the user's inbox.

When creating an SPF record in the public DNS, use all the IP addresses or address ranges from which an email might be sent. You can use both IPv4 and IPv6 addresses. An SPF record might look like the following:

-   An example of a basic SPF record to be added to an organisation's public DNS, where it uses Google, might be:

    > `v=spf1 include:spf.google.com ~all`

-   An SPF record including Google's IP ranges and a sending service with an IP address range, might be:

    > `v=spf1 include:spf.google.com ip4:80.88.21.0/20 ~all`

-   An example of a more complex record, with additional services and some dedicated IP addresses, might be:

    > `v=spf1 include:spf.protection.outlook.com include:mail.zendesk.com ip6:2001:db8::/32 ip4:203.0.113.6 ~all`


In the previous examples, `v=spf1` is an SPF record, `include:` means email can only come from these sources, `~all` considers any other email as a soft fail, and `–all` considers any other email as a hard fail.

**Note:** A hard fail **should** be used when a domain is being forged by spam.

To correct SPF failures, add the sending systems you use to your SPF record. Do this using either the IP address or by reference to another SPF record. These previous examples are unique, so check the actual domain or IP range of the email sending service. Also check with the supplier on setting up SPF records.

## Domain Keys Identified Mail

[Domain Keys Identified Mail \(DKIM\)](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) **shall** be enabled for all MoJ email domains. DKIM enables automatic filtering or rejection of emails that fail DKIM verification.

-   DKIM can verify a sender domain by looking up the sender's public key published in the DNS. You can then determine if an email has been tampered with during transit, for example during a "Man-In-The-Middle" attack.
-   A valid digital signature provides assurance that the hashed content has not been modified since the signature was affixed to the email message.
-   The MoJ enforces DKIM controls to help users identify communication tampering attacks by sending the messages directly to the spam folder, instead of to the user Inbox.
-   DKIM **shall** be used across the MoJ, including by executive agencies and ALBs.

## Domain-based Message Authentication, Reporting and Conformance

[Domain-based Message Authentication, Reporting and Conformance \(DMARC\)](https://en.wikipedia.org/wiki/DMARC) is an email authentication standard that **shall** be used with SPF and DKIM to:

-   Confirm a sender's email addresses.
-   Flag any emails that have been spoofed or otherwise tampered with.

By using DMARC:

-   MoJ emails are more likely to reach the recipients' inboxes \(suppliers, partners and public users\), rather than getting filtered out as spam.
-   There is full visibility of all the domains and IP addresses used to send emails.
-   There are warnings if a mail sender fails SPF, DKIM, or DMARC authentication.
-   It is possible to detect any unauthorised use of the domain.

When developing a new service with email sending or receiving capability, a DMARC policy **shall** be published. The policy **shall** be set to the highest level:

> `'p=reject'`

This policy indicates that mailbox providers **shall** reject all emails that fail DMARC.

If the DMARC policy cannot be set to `'p=reject'`, publish a record using `'p=none'` to override the default DMARC policy. This means that the mailbox provider won't take any actions with emails that fail DMARC.

Publish a DMARC record to the DNS for the domain to tell the email receiver how to handle emails that fail DMARC authentication, and where to send DMARC reports.

|DMARC Profiles|Benefits|Risks|
|--------------|--------|-----|
|`p=none`|Allows you to review incoming email to determine legitimacy while implementing DMARC for the first time.|Easier for phishers and spammers to take advantage.|
|`P=quarantine`|Malicious email is filtered out. Recipients decide what they want to do with quarantined email.|Legitimate emails might be missed if incorrectly quarantined and filtered|
|`P=reject`|All malicious email is stopped. The intended recipient of malicious email is not aware of the email, as it won't be sent to a spam or quarantine folder.|Legitimate emails might fail authentication and be rejected without the recipient being aware.|

`DMARC TXT` records **shall** be available for [creation](https://www.dmarcanalyzer.com/how-to-create-a-dmarc-record/) or iteration across the MoJ. This is to comply with the GOV.UK DMARC configuration [guide page](https://www.gov.uk/government/publications/email-security-standards/domain-based-message-authentication-reporting-and-conformance-dmarc).

## Mail Transfer Agent Strict Transport Security

Mail Transfer Agent Strict Transport Security \(MTA-STS\) is a protocol which tells services that are sending email to your organisation that your domain supports Transport Layer Security \(TLS\) 1.2 or higher. This protocol makes email less vulnerable to middle-person attacks, and allows the receiving email service to enforce encryption, without the risk of delivery failing.

The MoJ **shall** implement and use MTA-STS for MoJ email systems.

To 'enable' MTA-STS, publish a text file containing the MoJ MTA-STS policy. Before sending an email to the MoJ, the sending email service checks the Domain Name System \(DNS\) record of the MoJ email service for an MTA-STS policy.

It is MoJ policy to follow HMG Email Security policy for MTA-STS. The MoJ **shall** deploy an MTA-STS policy with `enforce` mode specified.

For more information on UK Government configuration and use of MTA-STS, refer to the [published guidance](https://www.gov.uk/government/publications/email-security-standards/using-the-mail-transfer-agent-strict-transport-security-mta-sts-protocol-in-your-organisation).

## TLS Reporting

TLS Reporting \(TLS-RPT\) is a protocol that allows a domain to advertise a destination for sending email services to report the success or failure of encryption in transit.

The MoJ **shall** implement and use TLS-RPT for MoJ email systems.

To 'enable' TLS-RPT, publish a DNS record telling mail sender tools where to send TLS-RPT reports. A sending email service checks for the record, and if one exists it is used to send a report to the address provided.

For more information on UK Government configuration and use of TLS-RPT, refer to the [published guidance](https://www.gov.uk/government/publications/email-security-standards/using-tls-reporting-tls-rpt-in-your-organisation).

## Making changes to the domain name system

Changes **shall** be made to DNS records when implementing SPF, DKIM, DMARC, MTA-STS, and TLS-RPT controls. When requesting changes, specific information **shall** be included for each record. If given the option, set a short time to live \(TTL\) in DNS records to monitor changes quickly, and fix any issues.

### DKIM example

Record type: `TXT`

Host or record name: `selector.*domainkey*`

Put your selector, or the selector provided by your service provider, in place of selector in the host or record name.

Record value: `v=DKIM1; k=rsa; p=<your DKIM key>`

Paste your DKIM key from your key generator in place of `<your DKIM key>`.

Some providers might use a `CNAME` record instead of a `TXT` record. Follow the guidance from your provider.

GSI is no longer used, but the following addresses still route through to `@justice.gov.uk`. The following table shows the authorised users you can contact to request DNS changes:

|Record Type|Contact|
|-----------|-------|
|`*.gsi.gov.uk`, `*.gsx.gov.uk`, `*.gse.gov.uk`, `*.gcsx.gov.uk`, `*.x.gsi.gov.uk`|[Vodafone Contact GDS](https://emailassurance.zendesk.com/hc/en-us/requests/new?ticket_form_id=130185)|
|`*.gov.uk` or any other domains|Your registrar, DNS provider or Internal System Admin|
|`*.cjsm.net`|Egress via [Security team](mailto:security@justice.gov.uk)|

### DMARC example

Record type: `TXT`

Host or record name: `dmarc`

Record value: `v=DMARC1;p=none;fo=1;rua=mailto:<example dmarc email address>,mailto:dmarc@<yourdomain.gov.uk>`

Create the email address and put your domain in place of `<yourdomain.gov.uk>`.

### SPF example

Record type: `TXT` or `CNAME` \(check guidance for your service on which to use\).

Host or record name: `@` \(if required\)

Record value: `v=spf1 include:<your email server domain> ip4:<your email service IP> ~all`

Put your email server domains or email sending IP ranges in place of the `< >` sections. You do not need to include both. In many cases you might only need `include:`.

## DNS contact details

For DNS changes and associated advice, contact the Platforms and Architecture team: [domains@digital.justice.gov.uk](mailto:domains@digital.justice.gov.uk)

## Contact details

For any further questions or advice relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

