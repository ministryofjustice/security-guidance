---
Review: 2020-12-31
Owner: CISO
Target audience:
---

# Email Authentication Guide

## Introduction

This guide explains the security controls that must be implemented at the domain layer to verify sender’s domains and prevent spoofing attacks. This guide is a sub-page to the Email Security Guide.

## Mail Check

Mail Check is a NCSC cyber defence service that enables email administrators to improve and maintain the security of email domains by preventing spoofing attacks. All domains operated by, or on behalf of the MoJ, must be added to Mail Check, regardless of whether the domain is expected to send or receive emails. All future contracts and agreements with third party suppliers must make this a requirement.

Mail Check should only be used if the email domain name provided is publicly routable from the internet via Simple Mail Transfer Protocol (SMTP).

Digital and technology users must contact the [NCSC Mail Check team](mailto:mailcheck@digital.ncsc.gov.uk) to have domains added to the MoJ’s subscription of the Mail Check service.

## Email sandboxing

Sandboxing provides an additional layer of protection in which any email that contains URLs, attachments or suspicious senders can be securely checked for malicious content before they reach the network or mail server. If the email is found to be harmful it will not be delivered. Sandboxing is beneficial as it:

* mirrors the end user’s computer and provides a secure space to interact with and analyse harmful communications
* allows developers and technical architects to actively minimise the impact of a threat.

For further guidance on implementing sandboxing, including which products you should use, contact the [Operational Security Team](mailto:security@justice.gov.uk).

## URL link rewriting

URL link rewriting is a technique used to detect malicious links in emails. Links in emails are actively scanned and rewritten to point to an Advanced Threat Protection gateway where the following checks occur:

* check the link to see if it is blacklisted by the MoJ or has been previously malicious, and
* if the link points to downloadable content, the content is scanned.

After the checks have completed, it will either allow the user to continue to the URL or block them from accessing it. In the case that the user has been blocked, it should provide them with a message with contact details.

## Sender Policy Framework

Sender Policy Framework (SPF) enables organisations to publish a Domain Name System (DNS) record of all the domains and IP addresses which are trusted for sending and receiving email.

* SPF is verified by checking a specific TXT DNS entry in emails; emails will be flagged if they are not sent from the domains and IP addresses published in the DNS record.  

* The MoJ enforces SPF controls to help users spot spoofed or unknown email addresses by sending them directly to the spam folder, instead of to a user’s inbox.

When creating an **SPF record** in your public DNS, you must use all the IP addresses or address ranges from which you send an email. You can use both IPv4 and IPv6 addresses. A SPF record could look like the following:



1. An example of a basic SPF record to be added to an organisation's public DNS where it uses Google would look like this:

 <code>v=spf1 include:_spf.google.com ~all</code>_

2. This SPF record includes Google's IP ranges and a sending service with an IP address range:

 <code>v=spf1 include:_spf.google.com ip4:80.88.21.0/20 ~all</code>_

3. An example of a more complex record, with additional services and some dedicated IP addresses:

 * <code>v=spf1 include:spf.protection.outlook.com include:mail.zendesk.com ip6:2001:db8::/32 ip4:203.0.113.6 ~all</code>

 * <code>v=spf1 is a SPF record</code>

 * <code>include:</code> means email can only come from these sources

 * <code>~all</code> considers any other email as a soft fail

 * <code>–all</code> considers any other email as a hard fail (this should be used when a domain is getting forged into spam).

To correct SPF failures you should add the sending systems you use to your SPF record, either by IP address, or by reference to another SPF record. These examples are unique so you should ensure you add the domain or IP range of your email sending service and check with your supplier on ‘how to setup SPF records’.

## Domain Keys Identified Mail

Domain Keys Identified Mail (DKIM) enables automatic filtering or rejection of emails that fail DKIM verification.

* DKIM can verify a sender domain by looking up the sender's public key published in the DNS. You can then determine if an email has been tampered with during transit (e.g. during a Man-In-The-Middle attack).
* A valid digital signature provides assurance that the hashed content has not been modified since the signature was affixed to the email message.
* The MoJ enforces DKIM controls to help users identify communication tampering attacks, by sending them directly to the spam folder, instead of to a user’s Inbox.
* DKIM must be used across the MoJ, including by executive agencies and ALBs.


## Domain-based Message Authentication, Reporting and Conformance

Domain-based Message Authentication, Reporting and Conformance (DMARC) is an email authentication standard that must be used with SPF and DKIM to confirm sender’s email addresses and flag any emails that have been spoofed or otherwise tampered with.

By using DMARC:

* MoJ emails are more likely to reach the recipients' inboxes (suppliers, partners and public users), rather than getting filtered out as spam
* you will have full visibility of all the domains and IP addresses you’re using to send emails
* you will know if your mail senders are failing SPF, DKIM and DMARC authentication, and
* you will be able to detect any unauthorised use of your domain.

When developing a new service with email sending or receiving capability, you must publish a DMARC policy and aim to set it to the highest level, called ‘p=reject’. This policy indicates you want mailbox providers to reject all emails that fail DMARC.

If you cannot set the DMARC policy to p=reject, you should publish a record using ‘p=none’ to override the default policy. This means that the mailbox provider won't take any actions with your emails that fail DMARC.

You must publish a DMARC record to the DNS for your domain to tell the email receiver how to handle emails that fail DMARC authentication and where to send DMARC reports.

| DMARC Profiles | Benefits | Risks |
|--- |---|---|
| p=none | Allows you to review incoming email to determine legitimacy while implementing DMARC for the first time. | Easier for phishers and spammers to take advantage. |
| P=quarantine | - Malicious email is filtered out. | Legitimate emails may be missed if incorrectly quarantined and filtered |
| | - Recipients can decide what they want to do with quarantined email. |  |
| P=reject | - All malicious email is stopped. | Legitimate emails may fail authentication and be rejected without the recipient being aware. |
| |  - The intended recipient of malicious email will not be aware of the email, as it won’t be sent to a spam or quarantine folder. | |

DMARC TXT records must be available for [creation](https://www.dmarcanalyzer.com/how-to-create-a-dmarc-record/) or iteration across the MoJ, as per the GOV.UK DMARC configuration [guide page](https://www.gov.uk/government/publications/email-security-standards/domain-based-message-authentication-reporting-and-conformance-dmarc).



## Protecting a parked domain

DMARC must also be implemented on non-email sending domains as they can be easily used for email spoofing and phishing.

* Once parked domains are protected, they must be configured to automatically renew by default.

If you are a domain owner you should aim to do the following to protect a parked domain:

1. Create a SPF record with no permitted senders so that no IP is authorised to send email for your parked domain.

2. Include a RUA address to which aggregate reports can be sent – these will provide you with visibility of potential abuse.

3. If you have an ‘A’ record on your domain, but no ‘MX’ records, you should create a null ‘MX’ record to immediately fail any email to that domain.

* Create a record of type MX, with a priority of 0 (highest priority).

4. A null DKIM record isn’t required, as email will be treated the same as if it had no record at all. However, recipients may treat a null DKIM record with extra caution, as it explicitly revokes any keys that may be cached.

Some interfaces may not allow you to implement all these steps but implement as many as possible.

## Making changes to the domain name system

Changes must be made to DNS records if you are implementing SPF, DKIM and DMARC controls. When requesting changes you must include specific information for each record. If given the option, set a short time to live (TTL) in DNS records so you can see changes quickly and fix issues.

**DMARC example**

Record type: TXT
Host or record name: <code>_dmarc</code>_

Record value: <code>v=DMARC1;p=none;fo=1;rua=mailto:dmarc-rua@dmarc.service.gov.uk,mailto:dmarc@<yourdomain.gov.uk></code>

Create the email address and put your domain in place of <code><yourdomain.gov.uk></code>.

**SPF example**

Record type: TXT or CNAME (check guidance for your service on which to use)

Host or record name: @ (if required)

Record value: <code>v=spf1 include:<your email server domain> ip4:<your email service IP> ~all</code>

Put your email server domains and/or email sending IP ranges in place of the <code><></code> sections. You do not need to include both - in many cases you may only need <code>‘include:’</code>.

**DKIM example**

Record type: TXT
Host or record name: <code>selector._domainkey</code>_

Put your selector, or the selector provider by your service provider, in place of selector in the host or record name.

Record value: <code>v=DKIM1; k=rsa; p=<your DKIM key></code>

Paste your DKIM key from your key generator in place of <code><your DKIM key></code>.

Some providers will use a CNAME record instead of a TXT record. Follow the guidance from your provider.

GSI is no longer used but the following addresses still route through to @justice.gov.uk. The table below shows the authorised users you can contact to request DNS changes:


| Record Type | Benefits |
|--- |---|
| *.gsi.gov.uk, *.gsx.gov.uk, *.gse.gov.uk, *.gcsx.gov.uk, *.x.gsi.gov.uk | [Vodafone Contact GDS](https://emailassurance.zendesk.com/hc/en-us/requests/new?ticket_form_id=130185) |
| *.gov.uk or any other domains | Your registrar, DNS provider or Internal System Admin |
| *cjsm.net | [Egress](mailto:cjsm.helpdesk@egress.com) |

You can contact the Platforms and Architecture team at [domains@digital.justice.gov.uk](mailto:domains@digital.justice.gov.uk) should you need advice about DNS changes.

## Contact details

* Contact Cyber Assistance Team for advice on email security: [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk)
* For any further questions relating to security, please contact: [security@justice.gov.uk](mailto:security@justice.gov.uk)
