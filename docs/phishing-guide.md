# Phishing Guide

This guide provides information explaining that 'phishing' is, how it happens, and what you can do to protect yourself and keep Ministry of Justice \(MoJ\) systems secure.

There is also information on [what to do if you think you have been phished](#what-to-do-if-you-are-phished).

## What is a phish?

Phishing attacks are when [threat actors](glossary.md#threat-actor) pretend to be legitimate parties. They do this to steal money, credentials, or sensitive information. There are a variety of phishing attacks that you might come across. Some are more sophisticated or targeted than others. Phishes use emotional states to create a sense of urgency. This urgency makes users want to do the actions requested. The combination of urgency and emotional manipulation leaves users feeling panicked and worried, or filled with a sense of euphoria. By heightening emotion and attaching a tight deadline, the threat actors are more able to convince users to do what they have requested.

Most phishes are emails, but they can also use other technology, such as SMS texts or telephone calls.

Threat actors might use phishes to request payments. They might ask you to click links and log in to an account or change a password. They might instruct you to buy items for them, or require you to provide some personal details before you can claim a supposed prize.

Threat actors utilise a variety of methods in phishes. They often take advantage of seasonal events to appear more legitimate. They use emotional and urgent triggers such as:

-   Telling you that your tax return is overdue.
-   Threatening to share access to your personal sensitive photos unless you pay.
-   A request to pay money to bail a family member out of jail.
-   Telling you 'good news' ,for example that you have won a big prize or are due a tax rebate.
-   Providing a final demand about a very overdue invoice that, if unpaid, will see you taken to court.
-   A 'last warning' about resetting your password, otherwise you will lose account access.

Any message that creates a sense of urgency or a heightened emotional state - positive or negative - should be treated with suspicion. Validate it before you take any action. Unexpected messages with attachments are also common. Never open the attachment until you have done an [out of band check](#out-of-band-checks).

## Common types of phish

There are many different types of phish. All of them can be spotted, but the more sophisticated the phishing attack, the harder it is to spot it. Out of band checks are the best way to stop a phishing attack. They use a second, different method of communication to validate the authenticity of the contact and the requested action.

### Email phishing

These are emails that request actions, such as clicking on links to change passwords or requesting money.

### SMS phishing \(smishing\)

These are text messages that ask you to click links to access services or to pay for things. They often take advantage of seasonal events to appear more legitimate. Examples include Christmas delivery phishing texts, texts around tax return time, and using news items like Covid to encourage payments or requests for personal information.

### Voice phishing \(vishing\)

These are phone calls that ask you for sensitive information, or payments, or to provide remote access to your devices. Threat actors commonly pretend to be from banks and other official organisations or technology companies such as Microsoft, or from jails requesting bail money.

### Spear phishing

These are targeted phishing attacks. Threat actors use [OSINT](glossary.md#open-source-intelligence-osint) to gather data about an individual. They can then create a custom phish specifically intended to be interesting for the target. The target is then more likely to respond to the phish. Examples include real names or work-related jargon. These are often very sophisticated phishes. The use of personal data makes the phish more likely to succeed.

### Whale phishing \(whaling\)

These are targeted at high level individuals such as CEOs and Director level and above staff. Whaling uses a variety of phishing methods to contact high profile targets, to steal large sums of money, or access high level credentials, intellectual property, and sensitive information.

### Business email compromise \(BEC\)

This type of phishing attack targets high level staff to steal money or reveal sensitive information. Threat actors pretend to be another high-level staff member by using their name or email address to seem legitimate. They often create a sense of urgency to convince junior staff to do the requested action. These emails often come from a compromised staff member's email account, so the email system doesn't block the sender.

### Watering hole attack

This is a very sophisticated supply chain attack. It uses research from an organisation's frequently used websites to identify a target. Targeted websites are then compromised and infected with malware. When users visit the websites, the malware is downloaded onto their systems. These attacks are sophisticated because the user is visiting an official and legitimate website. It is the website itself that has been compromised.

## Multi-factor authentication \(MFA\)

Multi-factor authentication \(MFA\) is an excellent way to reduce the risk of having your account compromised by a phishing attack. MFA provides an extra layer of defence for the account. If you have MFA set up, threat actors will be unable to access your account even if you accidentally reveal your credentials.

Never give MFA to codes to anyone. Companies, banks, government departments, and social media sites will never contact you and ask for your MFA code.

MFA also provides an early warning system for credential compromise. If you ever receive an MFA code for an account that you are not actively logging into, then someone other than you is trying to access the account. This means your credentials might have been compromised, so you should change your password as quickly as possible.

## Out of band checks

Out of band checks are an easy method to confirm the legitimacy of communications and requests. They can confirm the identity behind a message or request, and they can confirm the validity of the message or request itself. Social engineering techniques and phishing tactics take advantage of people who do not use out of band checks. By doing an out of band check, these sorts of attacks can be stopped very easily.

An out of band check is when an individual uses a different method of communication than the one the message came from. This method means that if one communication method is compromised, you quickly find out by using a different communication method to confirm validity. The likelihood of multiple communication methods for the same person or team being compromised is low.

**Example 1**: You receive an email request for an urgent review of an invoice, and immediate payment. The email comes from someone unexpected. You should find the official contact details of that person, and contact them using a phone call - but not email - to confirm that they did indeed send the original email. If they did send the email, you can proceed with the request. If they did not send the email, you can report the email as a phish, and also alert the owner of the email address that their email address might have been compromised.

**Example 2**: You receive a phone call from someone claiming to be your bank, or HMRC, or HMCTS. You hang up the call, and locate the official website for the company. You should be able to find multiple official contact details there. Use one of these to contact the place the caller claimed to be from. If, for example, the claim was that your bank was calling, you can call the direct number and speak to the switchboard about the reason for the initial call. They will forward you to the correct department. You can then confirm the validity of the original call, and so confirm whether the original caller was actually from your bank or not.

**Example 3**: Someone enters your place of work, and claims to have a meeting with a specific person. Unfortunately, there is no record of this on the expected visitor list. You can call or email the person within your place of work to confirm the visitor is legitimate. This check also works if tradespeople arrive unexpectedly, because you can contact both the relevant person within your place of work and also contact the company they claim to be from, using the company's official website contact details.

**Example 4**: You receive an email requesting that you reset your password immediately. The email contains a link to perform the password reset. You have not attempted to login to that account recently. You should use an internet search for the website or type the URL directly if you know exactly what it should be. When you attempt to login, the website will let you know if you need to reset your password. If not, you know someone else has attempted to gain access to your account. That would mean the password reset request was not legitimate, and most likely a phishing attempt hoping to get your username and password through the reset link in the original email. Similarly, if you get an [MFA request](glossary.md#multi-factor-authentication-mfa) unexpectedly, do not confirm it unless you were indeed attempting to access that account immediately before the request came through. If you get an MFA request, but had not been trying to connect using the account, you should change the account password as soon as possible, because it might have been compromised.

When doing an out of band check, be sure to pick a different method of communication to the one used to contact you originally. If someone emails you unexpectedly, perform an out of band check by making a phone call. If someone calls you, perform an out of band check by using the Internet. It is very unlikely that multiple communication channels have been compromised.

Be sure to get official contact details for companies only from their official websites. Never be afraid to hang up on someone and check their identity through another method, especially if they are asking for sensitive or personal information or credentials. Never be afraid to check the legitimacy of unusual email requests. by contacting the sender through a different communication channel.

Doing an out of band check lets you confirm that the messages come from the person they claim to be, and that the requests are valid. This helps prevent you or your company from losing money to fake invoices, from accidentally giving up sensitive information or credentials, and from having unauthorised individuals in your place of work. Doing an out of band check is fast and easy.

All members of your workplace should be happy to receive such a check. It shows that you take security seriously, and that you are helping to protect them as well as yourself.

## What to do if you are phished

**Don't panic.**

If you think you have been phished:

1.  Report it immediately.
2.  If your credentials were phished, highlight that in the report.
3.  Change the password for affected accounts as soon as possible.

MoJ firewalls and antivirus systems should catch the majority of malware before they can affect systems. By reporting the incident as quickly as possible, the security team will be alerted and on the lookout for any more sophisticated malware.

If your credentials have been phished, reporting it immediately and resetting your password quickly greatly reduces the risks.

Any phishing emails that get through the filters and into your inbox will be very sophisticated. This makes them much harder for you or anyone to spot. Never feel guilty or ashamed for being phished.

## Reporting phishes

If you think you have spotted a phish, report it as quickly as possible. If you think you have spotted a more targeted phish that claims to be from a vendor or another staff member then do an out of band check to determine if it is legitimate. If it is not, then please report the email as a phish.

You can forward on all spam and phishing text messages to 7726 for free. Reporting phishing attempts helps improve the filters that catch them before they get to your inbox. They also help protect other colleagues and the MoJ from being compromised, or having data or money stolen.

Reporting a phishing attempt is quick and easy. Simply forward the suspected phish to [security@justice.gov.uk](mailto:security@justice.gov.uk) with the subject line: 'suspected phish report'.

## Incidents

If you get phished, this must be reported as soon as possible, as an incident. The reason is that threat actors might have gained access to credentials, sensitive information, or have stolen money.

When a phish is reported, the security team can deal with the incident. Reports also provide useful information about the number of attempted phishes happening in the MoJ, and what sort they are. This in turn helps improve defences against phishing attempts.

## Contact details

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for cyber security advice, contact the Cyber Assistance Team: [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

