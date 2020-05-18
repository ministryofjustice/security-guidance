---
expires: 2020-12-31
---
# Multi-factor Authentication (MFA) Guide

## Introduction

This Multi-Factor Authentication (MFA) guide explains how MFA can be used to ensure that users are only granted access to MoJ information once their identity is confirmed. This is a sub-page to the
Access Control Guide.

## MFA

Users should have their identity authenticated through the following methods:

* something they know (such as a password)
* something they have (such as a mobile phone or smart card), and/or
* something they are (biometric authentication such as a fingerprint).

MFA can be used as a possession-based factor for authentication (something I have). MFA is sometimes referred to as Two-Factor Authentication (2FA) if it involves a second form of authentication or 3/4/5 Factor Authentication if it includes additional authentication requirements. Different methods of secondary authentication identify users with varying degrees of accuracy. The list below identifies the MoJ’s preference for MFA methods, with 1 ranked the highest. These can be used for 2/3/4/5 Factor Authentication as required.

Note:

* MFA Type 1 may not be suitable for all systems so other methods of delivering MFA should be considered as these still provide additional protections beyond single sign on.
* MFA types 5 and 8 should only be used when no other MFA method is appropriate as these methods can be easily spoofed or circumvented.

| Preference | Type |
| --- | --- |
| 1. | Hardware-based (for example, Yubikeys) |
| 2. | Software-based (for example, Google Prompt on a mobile device) |
| 3. | Time-based One Time Password (TOTP)-based (the code is held by a dedicated app such as Google Authenticator on a mobile device) |
| 4. | TOTP-based (the code is held within a multi-purpose app, for example, a password manager app that also holds other factor information) |
| 5. | Certificate-based (a digital certificate used to authenticate a user) |
| 6. | Email-based (a one-time code/link sent to the registered on-file email address) |
| 7. | SMS-based (a one-time code sent via SMS) |
| 8. | Phone-call based (a phone call providing a one-time code or password)

The MoJ Password Guide provides more information on the use of MFA. See the Authentication guide for further information.

## Contact details

Contact the Cyber Assistance Team for advice – [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk)
