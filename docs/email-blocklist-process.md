# Email blocking process

The Ministry of Justice \(MoJ\) manages a number of different mail platforms, including infrastructure in Google Workspace, as well as Microsoft Exchange \(on-premise\) and Microsoft Cloud platforms.

There are numerous reasons that email might be blocked. An email matching the criteria on a blocklist is only one reason.

If you have any concerns about email delivery, contact your email service provider or Infrastructure exchange team.

**Parent topic:** [Email Security Guide](email-security-guide.md)

**Related information**  


[Email blocking policy](email-blocklist-policy.md)

## Definitions

Within this guidance, 'email' might refer to individual user mailboxes, shared or group mailboxes, or distribution lists and mailing lists.

More specifically, a recipient or mailbox is any functional MoJ email account, for example [security@justice.gov.uk](mailto:security@justice.gov.uk).

Throughout this guidance, references to malicious emails include the following specific threats:

-   Emails which contain malware.

-   Phishing emails.

-   Spoofed or impersonal emails.

-   Harmful emails.

-   General spam emails.


There are a number of different email threats that exist in information technology. Each threat varies in complexity, and the impact it might have on the MoJ and its employees.

-   **Spam**

    Spam emails, also called junk emails, involve the sending of nearly identical messages to numerous recipients. They are high volume, unsolicited messages.

-   **Malicious or malware**

    These emails are specifically designed to damage operational systems or disrupt business operations. While the email itself may not be malicious, it might contain URLs or file attachments which are malicious.

-   **Phishing**

    This is an email-based attempt to acquire sensitive information such as credentials including IDs and passwords for malicious purposes. Phishing emails typically masquerade as a trustworthy person supposedly taking part in electronic communications.

-   **Spoofed or impersonation emails**

    These emails are from a forged sender address. At first glance, the email seems to be from a respected or reputable email sender, or an individual you know or trust.

-   **Harmful emails**

    These are emails that are not necessarily classified as malicious, but might cause distress or harm to users. Examples include threatening emails, or Denial of Service \(DoS\) attacks.


## Email blocklist

The purpose of any email blocklist is to prevent malicious emails entering or leaving the MoJ email infrastructure.

A blocklist consists of some or all of the following elements:

-   IP address.
-   Network range.
-   Domain name.
-   Email address.
-   URL.
-   Other email characteristics.

Each element helps identify more precisely where the sender is suspected of delivering malicious emails.

Throughout this document, any item on the email blocklist is referred to as a 'blocklist object'.

Each individual mail platform has its own set of objects that can be added to the blocklist. These obects vary from product to product.

**Note:** Users **SHOULD NOT** interact with any unsolicited or unwanted emails. Instead, follow email spam handling processes. For more information on this, contact your local IT Service Desk.

All email platforms in use by the MoJ **SHALL** have the ability to add items to the blocklist. The MoJ security team **SHALL** have appropriate permissions to update and review items on this list.

### Internal blocklist

There are two specific types of blocklists:

-   Individual mailbox blocklist.

-   Global blocklist.


Each mail platform that the MoJ manages has its own internal blocklist. Any object added to an internal blocklist is blocked from reaching mailboxes or recipients in that mail platform. Where possible, when a specific object is added to an internal blocklist in one platform, it **SHOULD** be replicated to other email environments.

The criteria for adding items to the internal blocklist are outlined in this policy.

**Note:** Individual mailboxes might have their own internal blocklist. This is a preferred route for requests to add domains to the global blocklist. Owners of individual mailboxes are responsible for managing their own individual mailbox blocklists.

If a user has multiple email addresses spanning different email platforms, then it's the users responsibility to keep their personal blocklists synchronized between the platforms.

### External blockList

The MoJ Security team use a number of commercial products which provide estate-wide or 'global' blocking, rather than individual blocking.

By default, external email blocklists are applied at the global level, meaning that they are applied to all mailboxes in an email environment.

## Auditing

All emails that are received into the MoJ email platforms **SHOULD** have AntiVirus scanning in place. The scanning includes automatic detection, classification, and actioning of suspicious emails.

Be aware that email filtering and blocking can not be 100% effective. This means any suspicious or unsolicited emails **SHOULD** always be treated with caution. Similarly, an e-mail might be incorrectly marked as infected or "spam". This might result in some emails being blocked unnecessarily.

## Freedom of Information \(FOI\) requests

The MoJ is a public sector organisation. This means that any member of the public has the right to make an request for information about any item of public interest. General information about FOI is available on the [MoJ Intranet](https://intranet.justice.gov.uk/guidance/knowledge-information/providing-information-to-the-public/freedom-of-information/). Security-specific considerations are outlined in the [Data Handling and Information Sharing Guide](data-handling-and-information-sharing-guide.md).

The Security team applies vendor processes delisting an object or item from the external blocklist, where appropriate.

**Note:** The MoJ Security team cannot assist with troubleshooting generic email delivery issues.

### Requests to remove objects from a blocklist

If you have concerns about the use of a blocklist, you need to provide relevant information about the problem, such as:

-   Sending IP address.
-   Time and date, including timezone information.
-   Error messages, such as undeliverable mail notifications.

You might also be asked to provide other information to help determine the specific reason why the email has not been delivered. In response, the MoJ reviews internal and external blocklists, and determines if the email was indeed blocked by an object on the blocklist.

If you believe that you cannot access justice services due to a blocklist, then you can request that a review of blocklist by the MoJ.

Requests for review are assessed on an individual basis, working with the nformation disclosure team, to determine resolution steps.

## Impact assessment

Any blocklist object **SHOULD** be defined so as to not result in widespread email failures. For example, it would not be helpful to block the whole of `@gmail.com`. Each blocklist object **SHOULD** be examined, taking into account the characteristics of the specific blocklist, and relevant intelligence sources.

Senders that have an established history of clean or legitimate emails, but have recently been sending emails of concern, **SHOULD NOT** be added automatically or instantly to the blocklist. Instead, the sender **SHOULD** be 'quarantined' by the affected email system.

## Avoiding the use of blocklists

Requests are sometimes made to block individual senders based on repeat, vexatious, or otherwise undesirable content. Take care when determining whether the sender truly has malicious intent, or whether they are a simply a member of the public with a genuine grievance but lacking the skills to air their concerns more constructively. Consider the risk of 'denying access to the criminal justice system' to an individual. If in doubt, refer to the [Data Privacy Team](mailto:privacy@justice.gov.uk) or Chief Information Security Officer \(CISO\).

### Documentation for internal blocklists

Use the MoJ incident management and change management process to add emails to internal blocklists. This includes documenting expected impact, and other relevant information.

As part of the documentation steps, the assessment and justifications for blocking specific objects **SHOULD** be included. Ensure the information is brief but contains sufficient relevant information. The relevant information **SHOULD** include:

-   The specific items to be added to the internal blocklist.

-   The classification of the email, and justification for blocking.

-   Summary outcomes from the impact assessment.

-   Summary actions taken to triage and resolve the incident, before resorting to blocking.


One ticket might contain multiple different blocking objects.

If an item is blocked without a corresponding ticket and justification as described in this guidance, then that object **SHALL** be removed from the internal blocklist with immediate effect.

## Review of existing blocks

The MoJ **SHALL** review items manually added to the internal blocklist, on a regular basis, to determine if they are relevant or not. Regular means at least every quarter. Any item included in the list and which is considered irrelevant **SHOULD** be removed. An irrelevant item is one that blocks legitimate emails from entering the MoJ email system.

A review of internal blocklist **SHOULD** also be done frequently, in line with the time for which blocked email messages are kept. This ensures the MoJ is able to recover incorrectly-blocked emails, and avoid them being deleted automatically.

## Spam emails

The [ICO website](ICO websitehttps://ico.org.uk/) provides general information about spam, and gives advice about the steps to reduce spam.

A spam email does not necessarily require automatice and instant inclusion on the internal blocklist, although it might be included as part of the external blocklists, as highlighted in this policy.

## Blocklist listing policies

The MoJ email platforms **SHOULD** have the ability to deploy automatic blocking of traffic. This includes blocking the following email classifications:

-   Spam traffic.

-   Malware traffic.

-   Open proxy or open relays.

-   Shared cyber threat intelligence.

-   Spoofed domains.


## Reporting incidents to external companies

The MoJ reserves the right to forward any email suspected of being added to the blocklist to external organisations for verification.

Organisation that are trusted by the MoJ for this purpose include:

-   Google.

-   ICO

-   Microsoft.

-   Netcraft.

-   NCSC.


In such cases, after forwarding, the MoJ **CAN** delete email messages from affected mailboxes.

## Contact details

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for security advice, contact the Cyber Assistance Team [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

