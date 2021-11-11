# Email blocking policy

This document outlines the policy for blocking emails, and deleting emails through administrative processes across email services across the Ministry of Justice \(MoJ\) estate. It specifically highlights the reasons for active inclusion on an email blocklist and removal from MoJ mailboxes.

To help identify formal policy statements, each is prefixed with an identifier of the form: `POLEBLxxx`, where `xxx` is a unique ID number.

**Parent topic:** [Email Security Guide](email-security-guide.md)

**Related information**  


[Acceptable use of Information Technology at work](acceptable-use.md)

[Data Security and Privacy](data-security-and-privacy.md)

[Email blocking process](email-blocklist-process.md)

[Malware Protection Guide - Overview](malware-protection-guide-introduction.md)

[Data Handling and Information Sharing Guide](data-handling-and-information-sharing-guide.md)

## Scope

This policy applies to all email domains and gateways managed by the MoJ, across all the applicable email services. Specifically, this policy applies to both email traffic inbound \(before it reaches the MoJ\), and outbound \(before it leaves the MoJ\).

## Blocklist definition

A blocklist is a real-time list, consisting of elements such as IP addresses, network ranges, domain names, email addresses, URLs, and other email characteristics. The common characteristic of the elements is that the sender is suspected of delivering spam.

The blocklist primary purpose is to prevent emails from entering or leaving the MoJ email services. Blocking emails is part of the overall cyber security strategy, providing defence-in-depth on MoJ managed email platforms.

Email types considered for blocking or removal include:

-   Malicious emails.

-   Phishing emails, including derivatives such as vishing, spearfishing, and whaling attacks.

-   Spoofed or impersonation emails.

-   Emails that cause disruption to the availability of an MoJ email service.

-   Other harmful or threatening emails.


## Blocking policy

`POLEBL001:` All email services used by the MoJ **SHALL** have the ability to add items to the blocklist. The MoJ [Operational Security Team](mailto:OperationalSecurityTeam@justice.gov.uk) **SHALL** have the appropriate permissions to update and review each MoJ email service blocklist.

`POLEBL002:` Any item added to an email service blocklist **SHOULD** be replicated across the different services in use across the MoJ estate.

`POLEBL003:` Blocklist items added are regularly reviewed to ensure the relevance of the block. Timeframes for reviews reflect the retention policies on the individual email services. Any changes that are made as a result of a review **SHALL** be completed and documented under change or incident management processes.

`POLEBL004:` When establishing the criteria for adding an item to the blocklist, the MoJ **SHOULD** go through an impact assessment to establish the impact of adding the specific item to the internal blocklist. If the impact might be substantial, for example causing widespread disruption, or where legitimate emails might be blocked, then the blocking object **SHOULD** be reconsidered or rescoped.

`POLEBL005:` As part the review process, or as a result of a user reported issue such as an incident reported through a user's local IT Team, a legitimate email might become blocked because it is now on a blocklist. This might be where the email address was added to the blocklist manually, or incorrectly flagged by automated tools in the email system. In this scenario, the MoJ **SHOULD** promptly unblock affected emails, and re-evaluate the blocking rule responsible, in line with this policy. This unblock **SHOULD** happen through the incident management process. All users are encouraged to speak with their Local IT team about concerns with email delivery, or email blocking.

`POLEBL006:` In the event that a legitimate email is blocked by an automatic vendor driven process, or included as an "indicator of compromise" through a threat intelligence product, the MoJ **MIGHT** request that the object be reviewed or reclassified.

`POLEBL007:` Before adding any object to the blocklist, or automatically removing it from an MoJ mailbox, impact analysis **SHALL** be carried out and documented through the MoJ change/incident management process.

## Deletion of existing emails in scope for blocking

`POLEBL008:` As part of the blocking procedure, the [Operational Security Team](mailto:OperationalSecurityTeam@justice.gov.uk) **SHOULD** have the ability to delete or purge emails across the estate which match the blocking criteria listed in the blocklist. This is an optional step, done at the discretion of the [Operational Security Team](mailto:OperationalSecurityTeam@justice.gov.uk).

`POLEBL009:` Purging of existing emails which have been added to the blocklist **SHALL** be done under peer review. Peer review **SHOULD** be completed by an independent member of the team who is not involved directly in the analysis or investigation of the email. Peer review takes place only if there is a further threat of users interacting with the newly classified email.

`POLEBL010:` If deletion of emails takes place, then details of the criteria **SHOULD** be included as part of the documentation process recorded as part of change or incident management.

`POLEBL011:` Where appropriate, users are encouraged to delete for themselves any emails confirmed to be in scope for blocking or deletion. Deletion of emails by the [Operational Security Team](mailto:OperationalSecurityTeam@justice.gov.uk) **SHOULD** take place only where there is a significant number of users who received the newly classified email.

`POLEBL012:` Removing emails from recipient mailboxes is a viable alternative to adding emails to an email blocklist. This **SHOULD** be the preferred option to prevent users from interacting with emails considered for blocking or removal.

`POLEBL013:` Deletion of emails **SHOULD** be done in such a way that the email could be recovered if required. If this is not possible, the email **SHOULD** be moved to the users 'junk' folder rather than simply being deleted.

`POLEBL014:` Users **SHOULD** be made aware of the deletion of emails. However, this is not mandatory.

`POLEBL015:` The MoJ has no responsibility to delete emails from unmanaged MoJ mailboxes.

`POLEBL016:` Automatic deletion of emails for users **SHOULD** be done through automated processes. The [Operational Security Team](mailto:OperationalSecurityTeam@justice.gov.uk) **SHALL** minimise access to the mailbox from which unwanted emails are purged.

## Automated blocking tools

`POLEBL017:` MoJ email services **SHOULD** come with inbuilt vendor managed blocking facilities based on known Indicators of Compromise \(IOC's\) to prevent emails entering or leaving the MoJ email environments. This vendor managed list **CAN** either be done through general lists of IOCs, or heuristic scanning.

`POLEBL018:` The email service vendor **SHOULD** provide the MoJ with the ability to reclassify incorrectly classified emails. This reclassification process **SHOULD** be accessible to the MoJ Cyber Security team, as well as email administrators.

The Cyber Security Team encourages the integration with 3rd party threat intelligence feeds from trusted providers as part of the in-depth defence strategy.

## Blocking or deleting received emails

`POLEBL019:` Any MoJ user who receives an email suspected to be one of the [types described previously](#blocklist-definition) **CAN** request that the email be blocked, preventing future similar emails from being received. On receipt of this, the MoJ reviews the evidence and determines if addition to a blocklist is appropriate. Further actions taken follow the policy statements in this guidance.

`POLEBL020:` Addition of emails to the blocklist is completed by either the local email service management team, or by the [Operational Security Team](mailto:OperationalSecurityTeam@justice.gov.uk). If the former, then approval **SHALL** be obtained from the [Operational Security Team](mailto:OperationalSecurityTeam@justice.gov.uk).

`POLEBL021:` In the event that an email is causing widespread disruptions or impacting business, then the individual email administration team responsible for the email platforms **CAN** delete emails or place blocks on emails without prior approval. This **SHOULD** be done under change and incident management, with notifications sent to the [Operational Security Team](mailto:OperationalSecurityTeam@justice.gov.uk).

`POLEBL022:` The MoJ **SHALL** provide a way for users to request emails for review by the relevant teams.

## Preemptive blocking

`POLEBL023:` If MoJ security receives intelligence about a credible threat to the confidentiality, integrity, or availability of an MoJ managed email service, then those emails **SHOULD** be added to the blocklist. Before blocking according to this policy statement, the intelligence **SHOULD** go through an impact analysis.

`POLEBL024:` All blocks **SHOULD** remain in place until the threat is no longer a credible threat to the MoJ.

`POLEBL025:` Email from previously known or blocked items **MAY** be re-added to the list if there is credible information or grounds to do so.

## Automatic blocking of emails based on attachments

`POLEBL026:` The MoJ **SHOULD** be able to restrict the delivery or sending of emails with certain malicious file attachment types.

`POLEBL027:` A complete list of email attachments blocked **SHOULD** be kept and managed by the individual email administrators, and **SHOULD** be consistent across different email services in use across the MoJ estate.

## Contact details

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for security advice, contact the Cyber Assistance Team [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

