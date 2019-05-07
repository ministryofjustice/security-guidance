---
expires: 2019-12-31
---
# Baseline for Amazon Web Services accounts

The MOJ has a 'lowest common denominator' for security-related promises, capabilities and configurations of MOJ Amazon Web Services (AWS) accounts.

The baseline is not a holistic list of dos and donts, but a _minimum_ line in the sand for what 'at least' **must** be done.

## The base principle

All MOJ AWS accounts **must** utilise a series of agreed configurations to enable and support good tenancy within AWS and a suitable cyber security posture.

### Anti-solutionising

This baseline discusses outcomes not _how_ the baseline will be achieved/implemented.

The MOJ Cyber Security team strongly encourage the use of the highest abstraction level of services available from AWS to achieve these goals, and minimising the amount of custom code and configuration which needs to be developed (and thereafter, maintained) to satisfy each baseline.

## Baseline

### GuardDuty

Leverage AWS’ commodity IDS solution to detect/protect from malicious or unauthorised behavior.

What must be in place | Monitoring | Resolution/Escalation if baseline is broken/violated
---|---|---|
* [GuardDuty](https://aws.amazon.com/guardduty/) is enabled on all accounts, in all regions, all of the time | * Alerts fire when GuardDuty is not enabled in a MOJ AWS account<br>* Alerts fire for at least HIGH and above (or some version of) GuardDuty matches | * GuardDuty is automatically re-enabled

### CloudTrail

Leverage AWS’ native activity audit platform (with adequate non-repudiation) to capture what AWS user (IAM etc) activity and changes are made within our AWS accounts

What must be in place | Monitoring | Resolution/Escalation if baseline is broken/violated
---|---|---|
* [CloudTrail](https://aws.amazon.com/cloudtrail/) is enabled within all accounts, all of the time<br>* CloudTrail logs are carbon copied to an AWS account controlled by Cyber Security | * Alerts fire when CloudTrail is not enabled in an MOJ AWS account | * CloudTrail is automatically re-enabled

### Config

Leverage AWS’ native AWS configuration activity audit platform to capture what changes are being made to AWS configurations.

What must be in place | Monitoring | Resolution/Escalation if baseline is broken/violated
---|---|---|
* [Config](https://aws.amazon.com/config/) is enabled within all accounts, all of the time<br>* Config logs are carbon copied to an AWS account controlled by CyberSecurity via CloudTrail | * Alerts fire when Config is not enabled in an MOJ AWS account | * Config is automatically re-enabled

### Tagging

[Tag](https://aws.amazon.com/answers/account-management/aws-tagging-strategies/) all of our AWS objects, so we know they have a purpose and are intentional with defined ownership.

We have our own [infrastructure ownership/tagging standards](https://ministryofjustice.github.io/technical-guidance/standards/documenting-infrastructure-owners/#documenting-owners-of-infrastructure).

What must be in place | Monitoring | Resolution/Escalation if baseline is broken/violated
---|---|---|
* All relevant AWS objects are tagged as per MOJ requirements | * Creating AWS user is notified automatically in increasing urgency when object is untagged<br>* AWS account owner (and increasing escalation) is automatically notified when objects remained untagged | * Untagged objects are forcefully and automatically shutdown/disabled or isolated after 7 consecutive days of not being tagged

### Regions

Do not use non-EU AWS [regions](https://docs.aws.amazon.com/general/latest/gr/rande.html) for strategic compliance and performance reasons.

What must be in place | Monitoring | Resolution/Escalation if baseline is broken/violated
---|---|---|
* No AWS account can create resources outside of AWS EU regions | * Alerts fire when non-EU resources are created to both the infrastructure teams and resource creator | * Non-EU resources are automatically and forcefully shut down after 12 hours

### Identity & Access Management

Enforce [Identity & Access Management](https://aws.amazon.com/iam/) and Joiners, Movers and Leavers (JML) within AWS. We also need to ensure accounts that legitimately exist are well protected.

What must be in place | Monitoring | Resolution/Escalation if baseline is broken/violated
---|---|---|
* AWS user accounts have a defined and peer reviewed method for request/creation<br>* Viable, authoritative and ‘single source of truth’ documentation exists to describe each AWS account and who should and should not have access (in terms of roles)<br>* Idle AWS user accounts are suspended<br>* MFA is required, always, enforced by policy<br>* Root user account usage is considered abnormal<br>* Passphrase and/or MFA seed cycled on every AWS root account use | * AWS group account owners are alerted when new AWS accounts are created<br>* Idle (30 or more consecutive days of non-activity) AWS user accounts issue suspension notices to AWS group account owners and target user<br>* Where an account does not have MFA, the user and AWS group account owners are notified after 7 consecutive days<br>* Any login or use of an AWS root account issues login alerts to the AWS group account owners | * Idle AWS user accounts are automatically suspended past threshold<br>* Non-MFA AWS user accounts are automatically suspended past threshold<br>* Alerts fire when an AWS root user account is used but the credentials are not updated within 7 days of utilisation

### Encryption

Leverage native AWS configuration options to make reasonable efforts to protect data.

What must be in place | Monitoring | Resolution/Escalation if baseline is broken/violated
---|---|---|
* All AWS objects supporting encryption must have it enabled | * S3 buckets without suitable SSE-* encryption enabled are alerted to resource creator and account owner | * After 7 days of non-action, alerts are sent to central hosting infrastructure teams, Head of Hosting and MOJ Cyber Security

### ‘World’ Access

Ensure that public access to AWS data storage and compute is intentional, to avoid the ‘leaky bucket’ problem, and to aid attack surface minimisation.

What must be in place | Monitoring | Resolution/Escalation if baseline is broken/violated
---|---|---|
* All AWS S3 objects should be not world (public) readable unless specifically intended to do so. | * S3 objects are programmatically reviewed (including ‘open’ ones) against the source infrastructure-as-code, if there is a mismatch the resource creator and AWS account owner notified | * After 7 days of non-action, alerts are sent to central hosting infrastructure teams, Head of Hosting and MOJ Cyber Security<br>* After 7 days, the S3 object permissions are forcefully and automatically changed to remove ‘world’ access
* Compute (for example, EC2 or ECS) instances should not be directly accessible from public networks unless through specific intentional design and should be behind CloudFront and/or applicable load balancing (preferring AWS LB technology).<br>It must be truly exceptional for common service ports (for example, TCP80 or TCP443) to be served directly from compute resources.| * Compute instances are programmatically reviewed to ensure they are not internet-accessible unless explicitly designed and documented to be so. If there is a mismatch the resource creator and AWS account owner notified | * After 7 days of non-action, alerts are sent to central hosting infrastructure teams, Head of Hosting and MOJ Cyber Security<br>* After 7 days, the relevant security groups are forcefully and automatically changed to remove ‘world’ access

### SecurityHub

[SecurityHub](https://aws.amazon.com/security-hub/) enabled where possible.

Over time we will be able to leverage this more, but in the immediate future this will enable us to do CIS-based scans.

What must be in place | Monitoring | Resolution/Escalation if baseline is broken/violated
---|---|---|
* SecurityHub  is enabled on all accounts, in all regions, all of the time | * Alerts fire when SecurityHub is not enabled in a MOJ AWS account | * SecurityHub is automatically re-enabled




## Implementation

Various [AWS account baseline templates](https://github.com/ministryofjustice/cloud-platform-infrastructure/tree/master/cloudformation/aws-account-baseline-templates) have been developed and published for use.
