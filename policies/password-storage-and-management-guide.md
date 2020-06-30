---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](home-security-policies-guides.md)

# Password Storage and Management Guide

## Introduction

This guide sets out how passwords must be stored securely to prevent unauthorised access or compromise. The MoJ encourages the use of password managers to reduce the burden on users for maintaining password security. This guide is a sub-page to the [Password Management Guide](password-management-guide.md).

## Password storage

The MoJ leverages the one-way salting hashing technique to encrypt passwords for safe storage. The following steps can be followed to setup salting for any MoJ systems that do not support or allow for automatic salting:

1. Generate a salt using a cryptographically secure function within the MoJ encryption tool.

2. Ensure that the salt is at least 16 characters long and encode it to a safe character set, such as hexadecimal.

3. Combine the salt with the password using concatenation or hash-based message authentication code.

4. Hash the combined password and salt.

5. Store the salt and the password hash within the MoJ approved tools.

Passwords must be securely stored within MoJ approved storage tools. The following tools are approved for use:

✔ [Argon2](https://en.wikipedia.org/wiki/Argon2)

✔ [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2)

✔ [LastPass](https://ministryofjustice.github.io/security-guidance/guides/using-lastpass/#using-lastpass-enterprise)

Please contact the [Cyber Assistance Team](mailto:CyberConsultancy@digital.justice.gov.uk) for approval to use a different storage tool.

## Sharing passwords

Passwords should not normally be shared. Sharing of passwords should be avoided by delegating privileges to other accounts (e.g. access to a document or inbox).

Passwords can be shared for the following exceptions:

- for an encrypted document that has to be shared to make sense
- for generic admin accounts where passwords have to be shared (Privileged Access Management (PAM) should be used where possible for systems that are admin only).

If there is a strong business need for shared access to a resource, account or system, then access to the password should be monitored and continually reviewed. The password should be:

- governed by PAM and only be used by known and trusted users
- changed if a user is no longer allowed access
- shared using a password manager.

## Password managers

Password managers are software and application tools that store passwords in an encrypted form. Password managers allow you to keep track of multiple passwords and avoid weak passwords, but to keep passwords secure a strong password manager must:

- never store passwords in an unencrypted form
- apply strong encryption algorithms
- have network access for encrypted lists sorted in the cloud
- have a dedicated application as well as a web browser page for working with the password list
- have a tool to generate passwords of varying complexity
- have the ability to fill in login pages
- automatically prompt notifications for security updates
- protect against brute forcing of the master key (where master key is the password to gain entry to the key safe)
- impose password strength requirements on the master key, for further guidance on password strength, please see the Password Creation and Authentication Guide.

The MoJ authorises the use of the following password managers and password vaults:

| Password managers for personal or team use | Password Vaults |
|--- |---|
| Lastpass | Hashicorp Vault |
| 1Password | Kubernetes Secrets |
| | AWS Key Management |
| | Azure Key Vault |

Please contact the [Cyber Assistance Team](mailto:CyberConsultancy@digital.justice.gov.uk) for approval to use a different password manager or vault.
This guide has been written in alignment with [NCSC guidance](https://www.ncsc.gov.uk/collection/passwords/updating-your-approach).

## Contact details

For any further questions relating to security, please contact: [Security@justice.gov.uk](mailto:security@justice.gov.uk).

Contact the Cyber Assistance Team for further advice - [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk)
