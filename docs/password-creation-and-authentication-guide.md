# Password Creation and Authentication Guide

## Introduction

This guide sets out considerations for creating passwords and authenticating users for access to Ministry of Justice \(MoJ\) systems. This includes ensuring that there are appropriate authentication methods for information, accounts and systems. For more information, see the [Password Management Guide](password-management-guide.md).

This guide has been written in alignment with [NCSC guidance](https://www.ncsc.gov.uk/collection/passwords/updating-your-approach).

## Default passwords

All default passwords must be changed before using any system. This includes all new, modified or replaced systems, applications and end-user devices or endpoints.

## Password length and complexity

To create a strong passphrase, you should pick a string of words that is easy for you to remember. Passwords must be complex and difficult to guess. When selecting a password ensure that:

-   It is a passphrase with a minimum of 12 characters for personal accounts.
-   It is a passphrase with a minimum of 15 characters for high value accounts, for example administrator accounts, password managers or service accounts.
-   It has at least one instance of each of the following character types: upper case, lower case, numbers and special characters, such `@`, `&`, `$`, `%` or `^`.
-   It does not contain usernames or personal information, such as date of birth, address, phone number or family or pet names.
-   It is used alongside system monitoring tools such as last login attempt notifications, rather than enforcing regular password expiry.
-   You have alternative authentication options, such as Single-Sign On \(SSO\) and Multi-Factor Authentication \(MFA\), depending on a system's security classification or where otherwise required.

## Password history and allow listing

The MoJ requires a password allow list to help users create strong passwords. This is a list of commonly used passwords, which can be easily guessed or brute forced by threat actors, and so must not be used. To understand trends in bad passwords and set up password allow listing, refer to 'SecLists', found on [GitHub](https://github.com/danielmiessler/SecLists/tree/master/Passwords).

The MoJ requires password history management, to prevent an old password being reused. This prevents threat actors using previously compromised passwords in an attack, and helps to enforce MoJ strong password requirements.

## Multi-factor authentication and single-sign on

MFA provides an additional layer of security for login and access controls. Two-Factor Authentication \(2FA\), Time-based One-Time Password Algorithm \(TOTP\), and hardware and software tokens and biometric authentication are all forms of MFA that might be used within MoJ systems. The [Access Control Guide](access-control-guide.md) provides further information.

If a service provides MFA, it should be used by default. MFA must be used for all `OFFICIAL` systems when:

-   They rely upon 'cloud' or other internet-connected services.
-   Logging on to a service using a new device.
-   Changing a password for a privileged account.

All systems classified as `SECRET` or `TOP SECRET` require MFA.

Further guidance around the use of Multi-Factor Authentication can be found in the [Authentication](authentication.md) guide.

MoJ SSO solutions include Office 365, and Digital and Technology G-Suite. SSO solutions must be integrated within the MoJ Identity Provider environment, to improve user experience by authenticating to systems using existing MoJ credentials. SSO must:

-   Be used for a defined and approved list of specific accounts and systems.
-   Have a pre-defined identity source for users, such as Active Directory, Google Directory or LDAP.
-   Normally be based on applications rather than groups of people. It can be based on groups of people or roles if these have been defined.
-   Not be used for privilege accounts, or for systems classified as `SECRET` or `TOP SECRET`.

## Contact details

For any further questions relating to security, contact: [security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk).

