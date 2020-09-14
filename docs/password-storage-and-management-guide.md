# Password Storage and Management Guide

## Introduction

This guide sets out how passwords must be stored securely to prevent unauthorised access or compromise. The Ministry of Justice \(MoJ\) encourages the use of password managers to reduce the burden on users for maintaining password security. For more information, see the [Password Management Guide](password-management-guide.md).

This guide has been written in alignment with [NCSC guidance](https://www.ncsc.gov.uk/collection/passwords/updating-your-approach).

## Password storage

The MoJ leverages the one-way salting hashing technique to encrypt passwords for safe storage. The following steps can be followed to setup salting for any MoJ systems that do not support or allow for automatic salting:

1.  Generate a salt using a cryptographically secure function within the MoJ encryption tool.
2.  Ensure that the salt is at least 16 characters long and encode it to a safe character set, such as hexadecimal.
3.  Combine the salt with the password using concatenation or hash-based message authentication code.
4.  Hash the combined password and salt.
5.  Store the salt and the password hash within the MoJ approved tools.

Passwords must be securely stored within MoJ approved storage tools. The following tools are approved for use:

-   [Argon2](https://en.wikipedia.org/wiki/Argon2).
-   [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2).
-   [LastPass](using-lastpass.md)

Contact the Cyber Assistance Team [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk) if you want to use a different storage tool.

## Sharing passwords

Passwords should not normally be shared. Sharing of passwords should be avoided by delegating privileges to other accounts, for example to provide access to a document or inbox.

Passwords can be shared for the following exceptions:

-   For an encrypted document that has to be shared to make sense.
-   For generic administration accounts where passwords have to be shared. [Privileged Access Management \(PAM\)](privileged-account-management-guide.md) should be used where possible for systems that are administration only.

If there is a strong business need for shared access to a resource, account or system, then access to the password should be monitored and continually reviewed. The password must be:

-   Governed by PAM, and only be used by known and trusted users.
-   Changed if a user is no longer allowed access.
-   Shared using a password manager.

## Password managers

Password managers are software and application tools that store passwords in an encrypted form. Password managers allow you to keep track of multiple passwords and avoid weak passwords. To keep passwords secure, a strong password manager must:

-   Never store passwords in an unencrypted form.
-   Apply strong encryption algorithms.
-   Have network access for encrypted lists sorted in the cloud.
-   Have a dedicated application as well as a web browser page for working with the password list.
-   Have a tool to generate passwords of varying complexity.
-   Have the ability to fill in login pages.
-   Automatically prompt notifications for security updates.
-   Protect against brute forcing of the primary key, where the primary key is the password to gain entry to the key safe.
-   Impose password strength requirements on the primary key.

The MoJ recognises the use of the following password managers and password vaults:

|Password managers for personal or team use|Password Vaults|
|------------------------------------------|---------------|
|Lastpass|Hashicorp Vault|
|1Password|Kubernetes Secrets|
||AWS Key Management|
||Azure Key Vault|

For further guidance on password strength, see the [Password Creation and Authentication Guide](password-creation-and-authentication-guide.md). Contact the Cyber Assistance Team [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk) if you want to use a different password manager or vault.

## Contact details

For any further questions relating to security, contact: [security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk), or for security advice, contact the Cyber Assistance Team [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

