# Passwords

This article provides guidance on passwords within the Ministry of Justice MoJ. It helps you protect MoJ IT systems by telling you about choosing and using passwords. Whenever you see the word system here, it applies to:

-   Hardware, such as laptops, PCs, servers, mobile devices, and any IT equipment.
-   Software, such as the Operating System, or applications installed on hardware, or mobile device applications apps.
-   Services, such as remote databases or cloud-based tools like [Slack](https://slack.com/).

This password guidance is for all users.

<a id="best-practices-for-everyone"></a>
## Best practices for everyone

The MoJ password guidance follows [NCSC guidance](https://www.ncsc.gov.uk/guidance/using-passwords-protect-your-data). The NCSC recommends a [simpler](https://www.ncsc.gov.uk/guidance/password-guidance-simplifying-your-approach) approach to passwords. Some agencies or bodies might have specific requirements or variations. Check your team Intranet or ask your Line Manager for more information.

Follow the [CyberAware advice](https://www.cyberaware.gov.uk/passwords) to generate your passwords. Always use a separate and unique password for each account or service.

The most important points to remember are that passwords should be:

-   At least 8 characters long.
-   No more than 128 characters long.
-   Not obvious.
-   Not a dictionary word. A combination of dictionary words might be suitable, such as `CorrectHorseBatteryStaple`.
-   Unique for each account or service.

If a system or another person provides you with a password, change it before doing any MoJ work on that system. Examples of 'single-use' passwords include:

-   Your own account on a work-provided laptop.
-   A shared account for accessing a data analytics service.
-   All supplier or vendor supplied accounts.

You must change a password whenever:

-   There has been a security incident involving your account or password. For example, someone guessed your password, or you used it on another account.
-   There was a security incident with the service that you access using the password. For example, if someone broke into the system that provides the service you use.
-   Your line manager or other authorised person tells you to do so.

When required to change a password, you must do so as soon as possible. If you don't change the password soon enough, you might be locked out of your account automatically. The following table shows the maximum time allowed:

|Type of system|Maximum time to change a password|
|--------------|---------------------------------|
|Single-user systems, such as laptops|1 week|
|All other systems|1 day|

<a id="password-expiry"></a>
## Password expiry

You don't have to change a password because it is old. The reason is that time-expiry of passwords is an [...outdated and ineffective practice](https://www.ncsc.gov.uk/blog-post/your-password-expiry-policy-may-have-reached-its-expiry-date).

Some current or legacy systems don't allow passwords that follow MoJ guidance. For example, some mobile devices, laptop hard drive encryption tools, or older computers might not be able to support a mix of character types. For such systems, choose passwords that are as close as possible to MoJ guidance.

<a id="password-managers"></a>
## Password managers

Use a password manager to help you keep track of your passwords.

These are tools that help you create, use, and manage your passwords. A useful overview is available [here](https://www.ncsc.gov.uk/blog-post/what-does-ncsc-think-password-managers).

As passwords become more complex, and you need to look after more of them, it becomes increasingly necessary to use a password manager. For example, development teams in MoJ Digital & Technology use [LastPass](https://intranet.justice.gov.uk/guidance/security/it-computer-security/user-access/passwords/password-managers/using-lastpass-enterprise/).

You still need to remember one password. This is the password that gets you into the manager application. Once you have access, the application works like a simple database, storing all the passwords associated with your various accounts and services. Some managers have extra features, such as password generators. Some managers can even automatically fill-in username and password fields for you when during log in.

The password manager database is often stored in the cloud so that you can use it anywhere. The database is encrypted, so only you can open it. That's why your single password key is so important. Without it, you can never get access to the password database again.

Using a password manager for your MoJ account and service details is recommended.

You can find additional useful information about password manager tools [here](https://intranet.justice.gov.uk/guidance/security/it-computer-security/user-access/passwords/password-managers/).

<a id="default-passwords"></a>
## Default passwords

Change all default passwords when a new, modified, or replacement system arrives. Complete the changes before making the system available for any MoJ work.

<a id="password-access-attempts"></a>
## Password access attempts

If a password is ever entered incorrectly, a count starts. After at most 10 ten consecutive failed attempts at using the correct password, access to the account or system is locked. A successful use of the password resets the count to zero again.

<a id="password-reset"></a>
## Password reset

If a password lock occurs, a reset is necessary. This requires action by the system administrator or the MoJ Service Desk. The process should be like issuing the password for the first time. Other account details are not changed during the reset. This helps avoid losing any work. Checks ensure that an attacker cannot use the password reset process.

<a id="blocking-bad-passwords"></a>
## Blocking bad passwords

You should not try and use [obvious passwords](https://en.wikipedia.org/wiki/List_of_the_most_common_passwords). Attempts to do so will be blocked.

<a id="single-use-passwords"></a>
## Single-use passwords

Some passwords are 'one time' or single-use. Administrators and developers use these to grant access to a service for the first time. After using the password once, the user must immediately change the password.

Single-use passwords are time limited. If they are not used within a specific time after generation, they must become invalid.

The following table shows the valid lifetime of a single-use password:

|Type of system|Lifetime of a single-use password|
|--------------|---------------------------------|
|Single-user systems, such as laptops|1 week|
|All other systems|1 day|

<a id="contacts"></a>
## Contacts

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for security advice, contact the [Cyber Assistance Team](mailto:CyberConsultancy@digital.justice.gov.uk).

<a id="feedback"></a>
## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [IT policy content](mailto:itpolicycontent@digital.justice.gov.uk).

