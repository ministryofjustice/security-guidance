# Operational Response to Phishing

This guidance provides Ministry of Justice \(MoJ\) operational security teams and system administrators with process steps to follow, in response to a Phishing incident report.

## Principles

A user reporting a possible Phishing incident is probably very nervous. Be as supportive and sympathetic as you can.

Try to minimise the number of questions you ask the user. Asking lots of technical questions is daunting.

The single most important question to ask is:

-   Did you provide any passwords or access codes?

If the answer is `Yes`, then the incident *must* be escalated to an analyst so that the credentials can be expired, revoked, or reset, as necessary.

## Phishing Incident Checklist

The following checklist is indicative. Do not hesitate to adapt according to circumstances, but ensure that you have sought and obtained approval from a senior person before doing so.

|Task|Sub-task|Activity|Who does this|
|----|--------|--------|-------------|
|1.||Determine what team\(s\) are affected by the phishing incident. Notify them. Determine if there are any team-specific instructions, and follow them.|Operational security team|
|2.||Include all affected teams into the incident management 'war' room. Don't forget the communications team.|Incident manager|
|3.||Determine scope and impact of incident.|Incident manager, Operational security team|
||a.|What does the email look like \(subject, body, and sender\)?||
||b.|How many users received the phishing email?||
||c.|Which user groups are affected?||
||d.|How many users clicked the link/downloaded an attachment?||
|4.||If we know the URL of the link, immediately block it and action password resets for anybody that followed it.|Incident manager|
|5.||Does the link deliver malware? Unless the answer is *definitely* no, If yes or unsure, run anti-virus scans for all accounts that clicked the link.|Operational security team|
|6.||Identify required and recommended communications:|Communications, Incident manager, Operational security team|
||a.|Enforced password resets and anti-virus scans.||
||b.|End-user and business holding statements.||
|7.||Watch for additional users reporting that they clicked on the link.|Operational security team|
|8.||Monitor and report on progress of password resets and anti-virus scanning activities.|Incident manager, Operational security team|
|10.||Post-incident activities:|Incident manager, Operational security team|
||a.|Monitor affected user accounts.||
||b.|Refresh and promote anti-phishing awareness and training.||

