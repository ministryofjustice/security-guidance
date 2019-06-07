---
expires: 2021-06-01
---
# Defensive domain registrations

The MOJ and associated organisations (Executive agencies, non-departmental public bodies and so on) main varying levels of 'online presence' using domain registrations that are often a cornerstone of the organisation's identity on the public internet, for example, as the email domain for contacting other government organisations, partners and members of the public.

Each MOJ organisation **must** identify a core set of internet domains it considers critical to it’s internet identity and defensively register a small number of overt variations (for example, `justice.gov.uk` may justify `justicegov.uk`, `justice.co.uk` and `justice.uk`) to protect itself, partners and members of the public from illegitimate parties pretending to be the organisation when they are not (this usually occurs as phishing emails).

## Limiting the permutations to register

Domain permutations for defensive registration should be limited to the organisation's core identity, as opposed to tertiary campaigns/identities, in order to keep costs and management overheads down.

Some domain registrars have programmes to detect malicious registrations of overtly government-associated domains through the use of misspellings and so on, so unless accompanied by strong justifications as to why misspellings must be covered, organisations should only defensively register `.uk` and `.co.uk` top-level domain variants and visual manipulations (for example, the removal of a dot from justice.gov.uk leads to justicegov.uk which would be a registerable domain that looks a lot like justice.gov.uk to the naked eye)

## Mandatory features for defensively registered domain

### Functional nameservers

The defensively registered domain must have a functional nameserver configuration.

### Sender Policy Framework (SPF)

An [SPF record](https://en.wikipedia.org/wiki/Sender_Policy_Framework) which uses strict indications to publish whether the domain is expected by the owner to send emails, or not.

Example:
`v=spf1 -all`

### DNS Certification Authority Authorization (CAA)

[DNS CAA](https://en.wikipedia.org/wiki/DNS_Certification_Authority_Authorization) record(s) to publish desired restrictions on whether certificate authorities should, or should not, accept requests to issue certificates for this domain.

The contents of the CAA record(s) are subject to change, pending whether the defensively registered domain will have an active web redirect on it or not (see below).

## Optional features for defensively registered domains

### Web redirects

A functional encrypted HTTPS TCP/443 redirect from any web domain query to the organisation's main domain identity, or (more preferably) the organisation's identity on GOV.UK.

An unencrypted HTTP TCP/80 redirect could also be added but encrypted HTTPS is preferred.

(Web redirects *must not* log, store, process or forward any unexpected data such as GET or POST queries.)

## MOJ Digital & Technology

MOJ organisations should contact [domains@digital.justice.gov.uk](mailto://domains@digital.justice.gov.uk) for assistance with defensive doman registrations.


