# Multi-Factor Authentication \(MFA\) Guide

**Related information**  


[Access Control guide](access-control-guide.md)

## Introduction

This Multi-Factor Authentication \(MFA\) guide explains how MFA is used to ensure that users are only granted access to Ministry of Justice \(MoJ\) information once their identity is confirmed. This is a sub-page to the [Access Control Guide](access-control-guide.md).

## MFA

Users **SHOULD** have their identity authenticated through one or more of the following methods:

-   Something they know, such as a password.

-   Something they have, such as a mobile phone or smart card.

-   Something they are, using biometric authentication such as a fingerprint.


MFA can be used as a possession-based factor for authentication, by checking for something 'you have'. MFA is sometimes referred to as Two-Factor Authentication \(2FA\) if it involves a second form of authentication. MFA is referred to as 3, 4, or 5 Factor Authentication if it includes additional authentication requirements. Different methods of additional authentication identify users with varying degrees of accuracy. Care **SHOULD** be taken to ensure true MFA. For example, password and security questions are both dependent on 'something the user knows' and therefore are just one factor of authentication.

The following list identifies the MoJ's preference for MFA methods, with 1 ranked the highest, and 8 the least desirable. These methods can be used for 2, 3, 4, or 5 Factor Authentication as required.

**Note:**

-   MFA Type 1 might not be suitable for all systems. In that case, other methods of delivering MFA **SHOULD** be considered to enable additional protection beyond single sign on.
-   MFA types 5 and 8 **SHOULD** only be used when no other MFA method is appropriate. The reason is that these methods are more easily spoofed or circumvented.

|Preference|Type|
|----------|----|
|1.|Hardware-based. For example, a Yubikey or similar TPM enabled device is presented during the authentication process.|
|2.|Software-based. For example, a [Google Prompt](https://support.google.com/accounts/answer/6361026?co=GENIE.Platform%3DAndroid&hl=en) is presented on a registered mobile device.|
|3.|Time-based One Time Password \(TOTP\)-based. The code is held by a dedicated app, such as Google Authenticator, on a mobile device.|
|4.|[TOTP](https://en.wikipedia.org/wiki/Time-based_One-time_Password_algorithm)-based. The code is held within a multi-purpose app, for example a password manager app that also holds other authentication information.|
|5.|Certificate-based. A digital certificate is used to authenticate a user.|
|6.|Email-based. A one-time code or link is sent to the user's registered on-file email address.|
|7.|SMS-based. A one-time code is sent to the user through an SMS message.|
|8.|Phone-call based. An automated phone call is made to the user's registered on-file phone number, to provide a one-time code or password.|

**Note:** When sending a one-time code to a mobile device, for example an SMS or phone call, the connection **SHALL** only be to a single user account. In other words, only telephone numbers allocated to a single individual **MAY** be used. Sending a one-time code to a shared device or shared number is not permitted.

The [MoJ Password Guide](passwords.md) provides more information on the use of MFA.

## Contact details

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for security advice, contact the Cyber Assistance Team [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

