# Mail Check

## The service

The [Mail Check Service](https://www.ncsc.gov.uk/blog-post/helping-secure-public-sector-email-mail-check) from NCSC is part of the [Active Cyber Defence](https://www.ncsc.gov.uk/blog-post/active-cyber-defence-tackling-cyber-attacks-uk) suite of services.

The service helps public sector email administrators improve and maintain the security of their email domains by preventing spoof email.

Domains operated by, or on behalf of, the Ministry of Justice \(MoJ\) **must** be added to Mail Check under at least the central MoJ Mail Check account.

## When to use the service

Mail Check \(and the underlying DMARC and SPF configurations\) **must** be implemented regardless of whether the domain is expected to send or receive emails on a routine basis.

This is important to ensure domains that are not expected to send emails are still monitored for being spoofed, as they are still legitimate MoJ domains which attackers may attempt to exploit in order to attack users.

## How to use the service

### Requirements

The email domain name is required. It must be publicly contactable for SMTP from the general Internet.

DMARC \(which requires SPF and DKIM\) TXT records must be available for creation or iteration, as per the [GOV.UK DMARC configuration guide page](https://www.gov.uk/guidance/set-up-government-email-services-securely#create-and-iterate-dmarc-records).

MoJ is permitted to use the service for free as a central government organisation, but suppliers to MoJ currently are not.

### Get started

Contact the MoJ Cyber Security team to be added into MoJ's subscription of the service.

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

