---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](home-security-policies-guides.md)

# Password Creation and Authentication Guide

## Introduction

This guide sets out considerations for creating passwords and authenticating users for access to MoJ systems. This includes ensuring that there are appropriate authentication methods for information, accounts and systems. This guide is a sub-page to the [Password Management Guide](password-management-guide.md).

## Default passwords

All default passwords must be changed before using any system. This includes all new, modified or replaced systems, applications and end user devices/endpoints.


## Password length and complexity

To create a strong passphrase you should pick a string of words that is easy for you to remember. Passwords must be complex and difficult to guess. When selecting a password ensure:

- it is a passphrase with a minimum of 12 characters for personal accounts
- it is a passphrase with a minimum of 15 characters for high value accounts e.g. administrator accounts, password managers or service accounts
- it has at least one of the following character types: upper case, lower case, numbers and special characters, such `@`, `&`, `$`, `%` or `^`
- it does not contain usernames or personal information, such as date of birth, address, phone number or family/pet names
- it is used alongside system monitoring tools (e.g. last login attempt notification), rather than enforcing regular password expiry
- you have alternative authentication options, such as Single-Sign On (SSO) and Multi-Factor Authentication (MFA) depending on a system's security classification or where otherwise required.

## Password history and allow listing

The MoJ must enforce a password allow list to help users create strong passwords. This is a list of commonly used passwords which can be easily guessed or brute forced by threat actors. To understand trends in bad passwords and set up password allow listing, refer to SecLists found on [GitHub](https://github.com/danielmiessler/SecLists/tree/master/Passwords).

The MoJ should implement password history management, to prevent an old password being reused. This prevents threat actors using previously compromised passwords in an attack and helps to enforce the MoJ's strong password requirements.

## Multi-factor authentication and single-sign on

MFA provides an additional layer of security for login and access controls. Two-Factor Authentication (2FA); Time-based One-Time Password Algorithm (TOTP); hardware and software tokens and biometric authentication are all forms of MFA approved for use within MoJ. The [Access Control Guidance](access-control-guide.md) provides further information.

If a service provides MFA it should be used by default. MFA must be used for all `OFFICIAL` systems when:

- they rely upon cloud or provide internet-connected services
- logging on to a service using a new device
- changing a password
- for a privileged account.

All systems classified as `SECRET` or `TOP SECRET` require MFA.

Further guidance around the use of Multi-Factor Authentication can be found on [here](https://ministryofjustice.github.io/security-guidance/standards/authentication/#authentication).

MoJ's SSO solutions include Office 365 and Digital and Technology G-Suite. SSO solutions must be integrated within the MoJ's Identity Provider to improve user experience by authenticating to systems using existing MoJ credentials. SSO must:

 - be used for a defined and approved list of specific accounts and systems

 - have a pre-defined identity source for users, such as Active Directory, Google Directory or LDAP

 - usually be based on applications rather than groups of people. It can be based on groups of people or roles if these have been defined

 - not be used for privilege accounts or systems classified as `SECRET` or `TOP SECRET`.

This guide has been written in alignment with [NCSC guidance](https://www.ncsc.gov.uk/collection/passwords/updating-your-approach).

## Contact details

For any further questions relating to security, please contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).
