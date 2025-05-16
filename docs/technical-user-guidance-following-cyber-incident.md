# Technical User Guidance Following a Cyber Incident

## Introduction

A cyber incident can disrupt operations, compromise sensitive information, and expose vulnerabilities in an organisation's systems. Effective and cautious handling of cyber incidents is critical to minimise damage and prevent further exploitation.

During a live cybersecurity incident response, it is crucial for all staff to follow an Operational Security \(OPSEC\) approach to protect sensitive information and maintain the integrity of the response. Following OPSEC procedures enables us to to act in the best interest of the Ministry of Justice \(MoJ\) and ensures we demonstrate correct security behaviours.

## Do Not Probe Indicators of Compromise \(IoCs\)

IoCs may include, but are not limited to, suspicious IP addresses, domains, or files related to the attacker. Users **must** refrain from probing or interacting with IoCs. This includes active probing via pings, NSlookups of IoC IPs, domains or other URLs linked to the incident.

**Do not** engage with IoCs from any network, including MoJ infrastructure, your own personal infrastructure, or personal hosting. Direct engagement could alert the attacker, exacerbate the situation, or compromise additional systems. Leave the investigation to the relevant security team\(s\).

If you have already interacted with or probed any IoCs, immediately inform the relevant investigatory/security team\(s\) to avoid unnecessary efforts and misdirected alerts during the investigation.

## Testing Remedial Configuration

If testing controls or connections is necessary, please communicate your IP address, any usernames or roles, and the timeframe of actions you're conducting to relevant stakeholders involved in the investigation. This is to inform team members and the Security Operations Centre \(SOC\) of the potential for false positive alerts.

## Avoid Discussing the Incident Beyond Involved Teams

Information about the incident should only be shared with authorised personnel, such as the security team\(s\) and any professional third-parties onboarded as part of the investigation. You must not discuss details with colleagues, external parties, or on public platforms. Sensitive information could be inadvertently leaked, complicating the situation. If you need to share IP addresses in internal chat sessions obscure IP addresses to avoid accidental clicks or auto hyperlinking, using brackets can be useful, for example: `192[.]168[.]1[.]1`

## Do Not Erase Evidence

Deleting any files, logs, or email records can hinder the investigation and prevent the SOC team from identifying the attacker's methods. Even suspicious files, logs, and emails must be preserved. Deleting any evidence can compromise the integrity of the chain of custody, making it difficult to establish accountability or pursue legal action if necessary.

## Follow SOC Instructions for Updates

The SOC may request additional details or actions as they investigate. Be prepared to:

-   Provide any logs, screenshots, or records relevant to the incident.
-   Respond promptly and accurately to questions.
-   Follow instructions for securing devices and accounts.
-   Report and new information or findings.
-   Remain vigilant and avoid assumptions.

## Contact and Feedback

For any further questions or advice relating to security, or for any feedback or suggestions for improvement, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).

