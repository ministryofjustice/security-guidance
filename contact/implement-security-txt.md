---
category: Vulnerability Disclosure
expires: 2019-12-31
---
# Implementing security.txt

For production (live) domains where the MOJ is primarily responsible for cyber security the `/.well_known/security.txt` location **must** exist and redirect to the central `security.txt` file.

## security.txt

`/.well_known/security.txt` should HTTP 301 (permanent redirect) to `https://raw.githubusercontent.com/ministryofjustice/security-guidance/master/contact/vulnerability-disclosure-security.txt`

For example,
https://www.prisonvisits.service.gov.uk/.well_known/security.txt
should HTTP 301 to
https://raw.githubusercontent.com/ministryofjustice/security-guidance/master/contact/vulnerability-disclosure-security.txt

### /.well_known/

We use `/.well_known/` to house `security.txt` as [RFC5785](https://tools.ietf.org/html/rfc5785){:target="_blank"} defines a path prefix for "well-known locations", `/.well-known/`, in selected Uniform Resource Identifier (URI) schemes.