# Baseline for Azure Subscriptions

The Ministry of Justice \(MoJ\) has a 'lowest common denominator' approach to apply to the largest possible number of people for security-related promises, capabilities and configurations of MoJ Azure Subscriptions.

The baseline is not a holistic list of dos and don'ts, but a minimum line in the sand for what 'at least' **SHALL** be done.

This guidance is Version 1.3, September 16th 2021.

## The base principle

All MoJ Azure Subscriptions **SHALL** utilise a series of agreed configurations to enable and support good tenancy within Azure accounts, and a suitable cyber security posture.

### Anti-solutionising

This baseline discusses outcomes, not how the baseline is achieved or implemented.

The MoJ Cyber Security team strongly encourages the use of the highest abstraction level of services available from Azure to achieve these goals, and minimising the amount of custom code and configuration which needs to be developed \(and thereafter, maintained\) to satisfy each baseline.

## Initial Considerations

The type of hosting is the first consideration. AWS is the preferred Cloud Service Provider but we understand that Azure sometimes is a technical requirement.

Legacy applications **SHOULD** be hosted via the [Modernisation Platform](https://ministryofjustice.github.io/modernisation-platform/user-guide/cloud-platform-or-modernisation-platform.html#should-i-use-the-cloud-platform-or-the-modernisation-platform).

The requirement to use Azure **SHOULD** also include basing new services or subscriptions on existing or predefined settings and policies.

For [UK Government Services](https://docs.microsoft.com/en-us/azure/governance/blueprints/samples/ukofficial-uknhs), there are [Blueprints](https://portal.azure.com/#blade/Microsoft_Azure_Policy/BlueprintsMenuBlade/GetStarted) available to ensure compliance with meeting Standards and Policies. If these exist, they **CAN** be replicated and applied to new services or subscriptions.

## Security incidents

The CyberSecurity team **SHOULD** be added as a security contact for all Information or Cyber Security incidents. The contact details for raising Incidents need to be managed internally, for example using an Intranet page.

## Baseline

The following are the minimum requirements for usage of Azure.

### Identity and access management \(IAM\)

Utilise [Identity and access management \(IAM\)](https://azure.microsoft.com/en-gb/product-categories/identity/) to defend against malicious login attempts and safeguard credentials with risk-based access controls, identity protection tools and strong authentication options – without disrupting productivity and use IAM for Joiners, Movers and Leavers \(JML\) within Azure. Ensure Services / Subscriptions that legitimately exist are well protected.

|What **SHALL** be in place|Monitoring|Resolution or escalation if baseline is broken or violated|
|--------------------------|----------|----------------------------------------------------------|
|[Azure Active Directory](https://azure.microsoft.com/en-gb/services/active-directory/) is enabled on all accounts, in all used tenants or subscriptions, all of the time.|Alerts fire for new findings.|Findings are archived \(if intended\) or resolved \(if unintended\) within 7 days.|
|Azure user accounts have a defined and peer reviewed method for request or creation. Viable, authoritative and 'single source of truth' documentation exists to describe each Azure account and who should and should not have access based upon Role Based Access Control \(RBAC\). Idle Azure user accounts are suspended. MFA is always required and always enforced by policy. Root user account usage is considered abnormal. Passphrases or MFA seeds are cycled on every Azure root account.|Azure group account owners are alerted when new Azure accounts are created. Idle \(30 or more consecutive days of non-activity\) Azure user accounts issue suspension notices to Azure group account owners and target users. Where an account does not have MFA, the user and Azure group account owners are notified after 7 consecutive days. Any login or use of an Azure root account issues login alerts to the Azure group account owners.|Idle Azure user accounts are automatically suspended past threshold. Non-MFA Azure user accounts are automatically suspended past the threshold. Alerts fire when an Azure root user account is used but the credentials are not updated within 7 days of utilisation.|

For more information on MFA, see the [Multi-Factor Authentication guidance](multi-factor-authentication-mfa-guide.md).

### Advanced threat protection

Leverage Azure to identify and resolve vulnerabilities, assess threats efficiently, and ultimately focus on real threats.

|What **SHALL** be in place|Monitoring|Resolution or escalation if baseline is broken or violated|
|--------------------------|----------|----------------------------------------------------------|
|[Azure Security Center](https://azure.microsoft.com/en-gb/services/security-center/#overview) is enabled.|Security management system that strengthens the security posture of your data centers, and provides advanced threat protection across your Azure workloads in the cloud.|Protection is automatically re-enabled.|
|[Azure Defender](https://docs.microsoft.com/en-us/azure/security-center/azure-defender) is part of the Azure Security Center and **SHOULD** also be enabled.|Alerts fire when Defender for Identity is not enabled in an MoJ Azure account.|Protection is automatically re-enabled.|
|Enable Azure Bastion or Just in Time \(JIT\) for VM access for new services.|Requests are logged in Azure Activity Log, to monitor and audit access.|Protection is automatically re-enabled.|

### Firewall

Leverage Azure for protection of your web applications from common exploits and vulnerabilities.

|What **SHALL** be in place|Monitoring|Resolution or escalation if baseline is broken or violated|
|--------------------------|----------|----------------------------------------------------------|
|Web Application Firewall \([WAF](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview)\) is enabled.|Web applications are increasingly targeted by malicious attacks that exploit commonly known vulnerabilities. SQL injection and cross-site scripting are among the most common attacks.|Protection is automatically re-enabled.|
|[Azure Firewall](https://docs.microsoft.com/en-us/azure/firewall/overview) is a managed, cloud-based network security service that protects your Azure Virtual Network resources.|Centrally create, enforce, and log application and network connectivity policies across subscriptions and virtual networks.|Protection is automatically re-enabled.|

### Monitor

Leverage the Azure solution for collecting, analyzing, and acting on telemetry from your cloud and on-premises environments.

|What **SHALL** be in place|Monitoring|Resolution or escalation if baseline is broken or violated|
|--------------------------|----------|----------------------------------------------------------|
|[Monitor](https://azure.microsoft.com/en-gb/services/monitor/) is enabled within all subscriptions, all of the time.|Alerts fire when Monitor is not enabled in an MoJ Azure resource.|Monitor is automatically re-enabled.|

### Advisor

Leverage Azure's native configuration activity audit platform to capture what changes are being made to Azure configurations.

|What **SHALL** be in place|Monitoring|Resolution or escalation if baseline is broken or violated|
|--------------------------|----------|----------------------------------------------------------|
|[Advisor](https://azure.microsoft.com/en-gb/services/advisor/) is enabled within all accounts, all of the time.|Alerts fire when it identifies new and available recommendations.|Advisor is automatically scanning the estate for vulnerabilities and areas of concern. Monitor them and review. Security or high impact alerts should be remediated and escalated to senior management.|

### Regions

Do not use Non-UK Azure regions for strategic compliance and performance reasons.

|What **SHALL** be in place|Monitoring|Resolution or escalation if baseline is broken or violated|
|--------------------------|----------|----------------------------------------------------------|
|An Azure subscription **SHALL NOT** create resources outside of Azure UK regions.|Alerts fire when non-UK resources are created, to both the infrastructure teams and resource creator.|Non-UK resources are automatically and forcefully shut down after 12 hours.|

### Encryption

Leverage native Azure configuration options to make reasonable efforts to protect data.

|What **SHALL** be in place|Monitoring|Resolution or escalation if baseline is broken or violated|
|--------------------------|----------|----------------------------------------------------------|
|[Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) - protect and safeguard your data and meet your organizational security and compliance commitments.|Blob Storage without suitable encryption enabled are alerted to the resource creator and account owner.|After 7 days of non-action, alerts are sent to central hosting infrastructure teams, Head of Hosting, MoJ Cyber Security and MoJ Cyber Security.|
|Manage [Encryption](https://docs.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) for data storage.|Storage without suitable encryption enabled is alerted to the resource owner and account owner.|After 7 days of non-action, alerts are sent to central hosting infrastructure teams, Head of Hosting, MoJ Cyber Security and MoJ Cyber Security.|
|[Key Vault](https://azure.microsoft.com/en-gb/services/key-vault/) - Provides security solution and works with other services by providing a way to manage, create, and control encryption keys.|Azure Key vault triggers events when the status of a secret stored in the key vault has changed.|After 7 days of non-action, alerts are sent to central hosting infrastructure teams, Head of Hosting, MoJ Cyber Security and MoJ Cyber Security.|

### Public / 'World' Access

Ensure that public access to Azure data storage and compute is intentional, to avoid the 'leaky bucket' problem, and to aid attack surface minimisation.

|What **SHALL** be in place|Monitoring|Resolution or escalation if baseline is broken or violated|
|--------------------------|----------|----------------------------------------------------------|
|All Azure Data Storage objects should be not world \(public\) readable unless specifically intended to do so.|Data Storage objects are programmatically reviewed \(including 'open' ones\) against the source infrastructure-as-code, if there is a mismatch the resource creator and the Azure account owner are notified.|After 7 days of non-action, alerts are sent to central hosting infrastructure teams, Head of Hosting and MoJ Cyber Security. After 7 days, the Data Storage object permissions are forcefully and automatically changed to remove 'world' access.|
|Compute instances should not be directly accessible from public networks unless through specific intentional design and should be behind a firewall \(Azure based technology\). It **SHALL** be truly exceptional for common service ports \(for example, TCP80 or TCP443\) to be served directly from compute resources.|Compute instances are programmatically reviewed to ensure they are not internet-accessible unless explicitly designed and documented to be so. If there is a mismatch the resource creator and the Azure account owner are notified.|After 7 days of non-action, alerts are sent to central hosting infrastructure teams, Head of Hosting and MoJ Cyber Security. After 7 days, the relevant security groups are forcefully and automatically changed to remove 'world' access.|

## Implementation

[Infrastructure as Code](https://docs.microsoft.com/en-us/dotnet/architecture/cloud-native/infrastructure-as-code) \(IaC\) is the preferred method for initiating Services to encourage swift and predefined deployment.

|What **SHALL** be in place|Monitoring|Resolution or escalation if baseline is broken or violated|
|--------------------------|----------|----------------------------------------------------------|
|All Azure Services **SHALL** be defined in a IaC format.|Ensure IaC is maintained as reflects the current service.|7 days to correct and replace IaC data.|

## Tagging

Assigning tags to Azure resources is essential in creating a well-organised and transparent classification, and achieving significant cloud cost optimisation. When implemented, this practice can provide a consistent basis for applying policies across the organisation.

|What **SHALL** be in place|Monitoring|Resolution or escalation if baseline is broken or violated|
|--------------------------|----------|----------------------------------------------------------|
|All Azure Assets **SHALL** be [Tagged](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources?tabs=json).|Report created to show missing Tags for relaying to Service Owners|Best Practice to apply.|

## Contact details

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for security advice, contact the Cyber Assistance Team [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

