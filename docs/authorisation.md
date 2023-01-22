# Authorisation

## The base principle

Any access to any data **must** employ adequate authentication techniques to identify the system or user to a suitable level of confidence for the system or data within.

## Least privilege principle

The principle of least privilege \(also known as the principle of least authority\) is effectively conferring only the minimum number of required privileges required in order to perform the required tasks.

This helps reduce the "attack surface" of the computer by eliminating unnecessary privileges.

Day to day examples include: not ordinarily using an 'administrator' login on an end-user device \(such as a laptop\), logging into a server as 'root' or a user being able to access all records within a database when they only need to access a subset for their work.

### Administrator definition

An administrator is much broader than a technical system administrator to a server, network or service \(such as 'domain admin' in Microsoft Active Directory\) but someone has who has higher levels of access or control than a required for day to day operation.

Examples include those with high privileges on a Ministry of Justice \(MoJ\) GitHub repository and credentials to the MoJ communications accounts \(such as social media\).

## AWS assume-role

Amazon Web Services \(AWS\) Identity and Access Management \(IAM\) has a `Role` function, which effectively allows explicitly permitted and explicitly denied activity \(within the AWS ecosystem\) to be defined on a per role-based.

This allows IAM accounts to be grouped based on role and purpose. This avoids individual IAM accounts being given permissions individually, which can often lead to over or under privilege configurations.

Where possible, IAM Roles should be used.

## Maintain IP address lists

Where applicable, maintain a single source of truth with meaningful labels to describe each IP address range.

The use of infrastructure as code to both store and apply IP address lists helps reduce errors, and aids with change management.

Where practical, periodically check the IP addresses with the team responsible for those IP addresses, to cater for upcoming changes in IP spacing or change of use or scope.

## Implement defensive depth

When you depend less on IP addresses as a filtration method, other activities become more important. These include:

-   Monitor accesses and activity.
-   Log accesses and activity.
-   Perform actual authentication, using techniques such as:
    -   Use of client certificates.
    -   'Magic' links.
    -   Usernames and passwords.
    -   Single or same sign-on.
    -   [Multi-factor authentication \(MFA\)](multi-factor-authentication-mfa-guide.md).
-   Including defences against denial-of-service attacks, brute force attempts, and credential stuffing.

## External IP addresses

External IP address access control lists are useful as part of a wider set of controls.

Introducing external IP address access control lists \(ACLs\) can filter out tertiary noise. Ensure that your use cases are rigorous, and that other defensive and authentication, authorisation, and accounting \(AAA\) measures are in place. This helps ensure protection from random port scans or brute force attempts.

Two real-life examples are:

-   Reducing MFA prompts. Do this by ensuring that corporate and staff wifi is appropriately access controlled. This includes having a clear egress range of IP addresses. It is important also to analyse and use the proximity probability of individuals and devices.
-   Make connection sessions longer. This is where you allow sessions and tokens to last for a longer period, such as 30 days instead of 7. These longer sessions are enabled only they take place from predictable and 'known' locations.

This [Medium article](https://medium.com/@joelgsamuel/ip-address-access-control-lists-are-not-as-great-as-you-think-they-are-4176b7d68f20) provides more details regarding IP address access control lists.

## Contact details

For any further questions or advice relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

