---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](../..)

# Multi-user accounts and Public-Facing Service Accounts Guide

## Introduction

This guide sets out when multi-user accounts should be used, although this is discouraged and should be avoided if possible. The guide also explains how public-facing service accounts should be authenticated. This guide is a sub-page to the Password management Guide.

## Multi-user accounts

In this context, a multi-user account is where a single set of credentials is used by more than one person. This can be found on legacy systems where there is a dedicated administrator account. Multi-user accounts allow multiple users with individual logins and varying permissions to use the same account. Multi-user accounts need to be managed carefully using Privileged Access Management (PAM) or a Bastion server to avoid security risks associated with accountability. Multi-user accounts should only be used directly if there is no alternative.

The multi-user account checklist requires that you:

 ✔ Undertake a Business Impact Assessment before implementation of a multi-user account to understand risks posed to the MoJ. Contact the [Cyber Assistance Team](mailto:CyberConsultancy@digital.justice.gov.uk) for further guidance.

 ✔ Create a pre-defined and authorised list of users.

 ✔ Implement on the ‘need to know’ access principle on the PAM or if using a bastion host, see what options there are to enforce this principle.

 ✔ Regularly check for redundant user IDs and accounts on either the PAM or bastion hosts. These should then be blocked or removed.


## Public-facing services and service accounts

Technical users should ensure that front-end users who access the MoJ’s public-facing services or applications are authenticated through the GOV.UK Verify Service. When this is not possible (for example when an individual does not have a UK address), passwords must:

 - be different for each service used by the individual

 - be easy to use, for example, pasting passwords into web forms should be enabled

 - not be changed as a result of regular password expiry

 - use Two Factor Authentication (the [Password Creation and Authentication Guide](../password-creation-and-authentication-guide/) provides further advice)

 - be changed when required - e.g. after a system compromise is identified or if the limit of unsuccessful password attempts is reached and the account is locked

 - be reset using a one-time password.

Service accounts must be used for system and application authentication. Service accounts must use certificates for authentication, however if these cannot be used, then passwords are an acceptable alternative. The Password Creation and Authentication Guide provides further guidance on how you must create a strong and complex password.

This guide has been written in alignment with [NCSC guidance](https://www.ncsc.gov.uk/collection/passwords/updating-your-approach).

## Contact details

For any further questions relating to security, please contact: [security@justice.gov.uk](mailto:security@justice.gov.uk)

Contact the Cyber Assistance Team for further advice - [CyberConsultancy@digital.justice.gov.uk](CyberConsultancy@digital.justice.gov.uk).
