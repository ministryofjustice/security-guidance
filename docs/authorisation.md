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

## IP addresses

The purpose of IP addresses in this context, are to help determine origin. Thus, grant trust and offer privileges as a result.  

IP addresses in and of themselves do not constitute authentication but may be considered a minor authentication *indicator* when combined with other authentication and authorisation techniques.

For example, traffic originating from a perceived known IP address/range does not automatically mean it is the perceived user\(s\) however it could be used as an indicator to *reduce* \(not eliminate\) how often [MFA](multi-factor-authentication-mfa-guide.md) is requested *within* an existing session.

Where applicable, maintain a single source of truth. Automatically apply confirmed changes when trying to identify the IP address ranges. There is an importance of advance change notification as well as the consequences if not up kept.  

### Implement defensive depth  

With less trust in IP addresses as a filtration method, the below is required to be carried out:  

log access/activity  

monitor access/activity  

actual authentication  

such as client certificates 

magic links 

usernames/password 

single/same sign-on 

multi-factor authentication 

build in defences against denial-of-service attacks, brute force attempts, and credential stuffing  

### External IP addresses  

External IP address access control lists are useful as part of a wider set of controls.  

Introducing external IP address ACLs can filter out tertiary noise. First, assure your use-cases are quite airtight and other defensive and AAA measures are in place. This will ensure protection from random port scans or brute force attempts.  

Two real life examples are:  

Reducing MFA prompts  

Depending on whether the corporate staff Wi-Fi is appropriately access controlled. As well as having a clear egress rang of IP addresses. To reduce the number of time MFA prompts, leverage the proximity probability of individuals/ devices.  


Making sessions longer  

Similarly to the above, you could allow sessions/tokens to last for 30 days instead of 7. If the session is only active from this predictably and ‘known’ location. 

This [medium article](https://medium.com/@joelgsamuel/ip-address-access-control-lists-are-not-as-great-as-you-think-they-are-4176b7d68f20) provides more details regarding IP address access control lists. 

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

