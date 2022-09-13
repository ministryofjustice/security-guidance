# Password Creation and Authentication Guide

## Introduction

This guide sets out considerations for creating passwords and authenticating users for access to Ministry of Justice \(MoJ\) systems. This includes ensuring that there are appropriate authentication methods for information, accounts and systems. For more information, refer to the [Password Management Guide](password-management-guide.md).

This guide has been written to align with [NCSC guidance](https://www.ncsc.gov.uk/collection/passwords/updating-your-approach).

## Default passwords

All default passwords **shall** be changed before using any system. Default passwords **should not** be 'guessable'. This applies to all new, modified or replaced systems, applications and end-user devices or endpoints.

## Password length and complexity

Best practice for creating a strong password is to create a passphrase consisting of a string of words that is easy to remember. If using this approach, have a minimum of three words in the passphrase. Passwords **shall** be complex and difficult to guess. When selecting a password, ensure that:

-   It has a minimum of 8 characters for personal accounts.
-   It has a minimum of 15 characters for high value accounts, for example administrator accounts, password managers or service accounts.
-   It does not contain usernames or personal information, such as date of birth, address, phone number or family or pet names.
-   It is used alongside system monitoring tools such as last login attempt notifications, rather than enforcing regular password expiry.
-   You have alternative or additional authentication options, such as Single-Sign On \(SSO\) and Multi-Factor Authentication \(MFA\), depending on a system's security classification or where otherwise required.

Stronger passwords typically contain at least one instance of each of the following character types: upper case, lower case, numbers, and special characters. Special characters include: `@`, `&`, `$`, `%` or `^`. However, there is no specific obligation to include special characters for a password to be acceptable.

For more details about passwords for service accounts, refer to the [Passwords](passwords.md) guidance.

## Password history and block listing

The MoJ requires a password block list to help users create strong passwords. This is a list of commonly used passwords, which can be easily guessed or brute forced by threat actors, and so **shall not** be used. To understand trends in bad passwords and set up password block listing, refer to 'SecLists', found on [GitHub](https://github.com/danielmiessler/SecLists/tree/master/Passwords).

The MoJ requires password history management, to prevent an old password being reused. This prevents threat actors using previously compromised passwords in an attack, and helps to enforce MoJ strong password requirements.

## Multi-factor authentication

MFA provides an additional layer of security for login and access controls. Two-Factor Authentication \(2FA\), Time-based One-Time Password Algorithm \(TOTP\), and hardware and software tokens and biometric authentication are all forms of MFA that might be used within MoJ systems. The [Access Control Guide](access-control-guide.md) provides further information.

If a service supports MFA, it **shall** be enabled and used by default. An MFA prompt **shall** appear when attempting to access an **Official** system, where:

-   The system relies upon 'cloud' applications, cloud-based APIs, or other internet-connected services.
-   A new device is used to log on to the service.
-   A password change is being made for a privileged account.

Further guidance around the use of Multi-Factor Authentication can be found in the [Authentication](authentication.md) guide.

## Single-Sign On

MoJ SSO solutions include Office 365, and Digital and Technology G-Suite. SSO solutions **shall** be integrated within the MoJ application development and service delivery environment, to improve user experience by authenticating to systems using existing MoJ credentials. SSO **shall**:

-   Have a pre-defined identity source for users, such as Active Directory, Google Directory or LDAP. This means a developer or service provider must use an established MoJ SSO solution rather than creating a new one.
-   Normally be based on applications rather than groups of people. This means that SSO is to a specific application or service, rather than saying something like 'all administrators of the Widget application have SSO-managed access'. Instead, SSO must be enabled for the 'Widget' application. It can be based on groups of people or roles if these have been defined.

## Contact details

For any further questions or advice relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

