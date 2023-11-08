# Online identifiers in security logging and monitoring

**Parent topic:** [Logging and monitoring](logging-and-monitoring.md)

**Related information**  


[Logging and monitoring](logging-and-monitoring.md)

## Overview

It can sometimes be counter-intuitive to think of IP addresses, cookies, and log data as personal data. However there are good reasons why it is important fort he during design, implementation, and operation of online services. Put simply, it is easiest for the to assume that any information captured and processed through public-facing services might contain personal information, and to protect this information accordingly.

## What are online identifiers?

Online identifiers are anything that could be used to track someone as they interact with online services. This can include, for example:

-   IP addresses.
-   Cookies that the or authorised 3rd parties set on devices.
-   Information placed into local storage on devices.
-   Usernames or other IDs associated with services.
-   Third-party authentication tokens.

Online identifiers could also include metadata captured about a device interacting with services if this information is sufficiently different to allow devices to be reliably identified.

## Why are online identifiers treated as personal data?

If there is any way to tie an online identifier to an individual, then that identifier needs to be treated as though it is personal data.

The way this mapping might be achieved is unimportant.

It could be because the user later provides personal data to the as part of using a service, and in doing so provides a link between all of the activities that their IP or session cookie has done with their identity.

There might also be a legal route available to the to determine the identity behind an identifier. For example, by making a lawful request to an ISP to uncover the person associated with a dynamic IP address at a particular time.

For more information on this, refer to the Information Commissioner's Office \(ICO\) [key definitions](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/key-definitions/), and "[Recital 30](https://www.privacy-regulation.eu/en/recital-30-GDPR.htm)" from the [Article 29 Working Group](https://en.wikipedia.org/wiki/Article_29_Data_Protection_Working_Party). There is also an informative article [here](https://www.fieldfisher.com/en/services/privacy-security-and-information/privacy-security-and-information-law-blog/can-a-dynamic-ip-address-constitute-personal-data).

## What does this mean for services?

It is important to think carefully about:

-   What metadata is captured during a user's interaction with services.
-   How long information is retained.
-   Who has access to the information.

privacy notices on services must be clear about the information captured as part of a user's interaction. This includes "anonymous" interactions, such as simple browsing information about the services. Metadata like this must be included in the scope of privacy impact assessments for services.

**Note:** Theoretically, privacy notices are only mandatory for externally-facing services. They are not required for internal services. However, it is undoubtedly good practice - and highly recommended - to apply the same approach, for consistency.

