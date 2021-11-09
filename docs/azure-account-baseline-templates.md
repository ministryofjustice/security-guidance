# Azure Account Baseline Templates

The lowest acceptable common denominator to appeal to the largest possible number of people for security-related promises, capabilities and configurations of Ministry of Justice \(MoJ\) Azure accounts.

## Baseline

The baseline for Azure accounts is formally published as part of the Security Guidance from the MoJ Digital and Technology Security and Privacy team.

## Background

As an organisation expands its use of Azure services, there is often a conversation about the need to create multiple Azure subscriptions to ensure separation of business processes or for security, compliance, and billing. We tend to use separate Azure subscriptions for each business unit so that it can meet the different needs of the organisation. Although creating multiple subscriptions has simplified operational issues and provided benefits like security and resource isolation, a smaller blast radius, and simplified billing, it results in widely varying security posture across the subscriptions and there is the need to align all of these subscriptions to a baseline secure standard.

## Areas of Concern

[Azure Security Center](#azure-security-centre).

[Azure Identity Management \(PIM\)](#azure-identity-management-pim).

[Azure Defender](#azure-defender).

[Web Application Firewall](#web-application-firewall).

[Monitor](#monitor).

[Advisor](#advisor).

[Regions](#regions).

[Azure Storage Encryption](#azure-storage-encryption).

[Key Vault](#key-vault).

[Tagging](#tagging).

This section provides the definition of baseline controls and list of templates that cover the baseline and governance guardrails that can be implemented in new accounts.

### Azure Security Centre

Use Azure Security Centre to ensure workloads are secure and to strengthen the security posture of the Azure estate. With continuous assessment, newly delivered resources are assessed and scored based on recommendations against Azure Security Benchmark.

### Azure Identity Management \(PIM\)

Enabling PIM helps to mitigate the risk of excessive, unnecessary or misused access rights by allowing administrators to discover, restrict and monitor access to Azure Active Directory resources. Essentially, it means that any user with access to the MoJ data is only allowed access to certain files or services, assigned by the global and privileged role administrators.

Recommendations to improve overall Azure security posture by monitoring at a minimum include:

-   Block or secure risky user accounts.
-   Require users to register for [Multi-Factor Authentication \(MFA\)](multi-factor-authentication-mfa-guide.md).
-   Enable the use of Just-in-Time access, so that administrators can create privileged access for a specific time frame.

Refer also:

-   [Azure AD Privileged Identity Management](https://docs.microsoft.com/en-us/azure/active-directory/privileged-identity-management/pim-configure).
-   [Activate my Azure AD roles in PIM](https://docs.microsoft.com/en-us/azure/active-directory/privileged-identity-management/pim-how-to-activate-role).

### Azure Defender

By enabling Azure Defender and integrating with Azure Security Center, you get an additional layer of security with which you can protect workloads hosted in Azure. Defender provides protection from most advanced threats, such as brute force, remote desktop protocol \(RDP\) or SQL injection attacks.

Refer also:

-   [Enable Azure Defender](https://docs.microsoft.com/en-us/azure/security-center/security-center-wdatp?tabs=windows).
-   [Enable Defender for Key Vault](https://docs.microsoft.com/en-us/azure/security-center/defender-for-key-vault-introduction).
-   [Enable Defender for SQL](https://docs.microsoft.com/en-us/azure/azure-sql/database/azure-defender-for-sql).

### Web Application Firewall

Azure Web Application Firewall \(WAF\) on Azure Application Gateway is a cloud-native service that provides centralised protection to web applications from common cyber attacks. Azure WAF protects against crawlers and scanners, SQL and command injection, cross-site scripting, HTTP protocol violations, anomalies, and other common web attacks. A WAF can support configurable request size limits and custom rules, exclusion lists, and geo-filtration of traffic.

Refer also:

-   [Azure WAF deployment](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview).

### Monitor

Azure Monitor is the centralised console where you can create alerts around various resources in your subscription and also manage them. Alerting in Azure Monitor includes creating and managing alert rules, and creating and managing action groups.

Refer also:

-   [Create, view, and manage activity log alerts by using Azure Monitor](https://docs.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-activity-log).

### Advisor

Azure Advisor takes the guesswork out of optimising your Azure deployments. Specifically, providing highly-personalised recommendations and best practices which are both actionable and proactive. Azure Advisor helps you find ways to reduce costs related to Azure service subscriptions, improve the performance, security, and availability of resources that are in use.

Refer also:

-   [Azure Advisor](https://docs.microsoft.com/en-us/azure/advisor/advisor-overview).

### Regions

The MoJ does not use non-EU Azure regions, for strategic compliance and performance reasons. For more information on regions, refer to [Conditional Access : Block by region](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/howto-conditional-access-policy-location).

### Azure Storage Encryption

Azure Storage data encryption and decryption is transparently done using 256-bit AES. Azure Storage encryption is for all storage accounts, including both Resource Manager and classic storage accounts. This cannot be disabled, as the data is secured by default. All Azure Storage resources, such as blobs, disks, files, queues, and tables, including all object metadata, are also encrypted at rest.

Refer also:

-   [Azure Storage encryption for data at rest](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption).

### Key Vault

Azure Key Vault protects encryption keys and secrets stored in Azure. The material might be certificates, connection strings, and passwords. However, steps should be taken to maximise the security of your vaults and the data stored within them while storing sensitive data, including enabling Defender for Key Vault to safeguard your data.

Refer also:

-   [Best practices to use Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/general/best-practices).
-   [Defender for Key Vault](https://docs.microsoft.com/en-us/azure/security-center/defender-for-key-vault-introduction).

### Tagging

Assigning tags to Azure resources is essential in creating a well-organised and transparent classification, and achieving significant cloud cost optimisation. When implemented, this practice can provide a consistent basis for applying policies across the organisation.

Refer also:

-   [Assign policy definitions for tag compliance](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/tag-policies).

## Contact details

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for security advice, contact the Cyber Assistance Team [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

