# Security Log Collection Maturity Tiers

Ministry of Justice \(MoJ\) systems and services must adequately create and retain event data as part of the [DETECT](identify-protect-detect-respond-recover.md) portion of the [Cabinet Office's Minimum Cyber Security Standard \(MCSS\)](https://www.gov.uk/government/publications/the-minimum-cyber-security-standard).

Three tiers have been developed to reflect the breadth and complexity of collecting and forwarding log data.

These three tiers represent different levels of risk profile, and concern about a system. All systems should be capable of meeting the baseline standard.

Some systems are at greater likelihood of compromise. This is due to factors such as age or public threats. Other systems would have a higher impact if compromised. This is due to the systems being sensitive or having distinctive perceived value. Such systems should be monitored to a higher standard.

The extent to which a security log collection process implements the monitoring requirement indicates the logging maturity.

Each level of monitoring - or 'tier' - has characteristics that are 'in addition' to lower level tiers. For example, a system operating at the Enhanced tier should also meet the requirements of the Baseline tier.

![A diagram showing a large triangle, base at the bottom, split into three levels. The top level has the heading 'Bespoke'. It contains two items: Customised logging, and Dynamic event responses. The middle level has the heading 'Enhanced'. It contains three items: Notification of events, Active analysis, and Automation of manual processes. The bottom and largest level has the heading 'Baseline'. It contains four items: System logs, Authorisation logs, Failure logs, and Security functions.](images/tiers.png)

## Baseline

The baseline tier is the generally minimum expected for event types. It includes data that should be generated, recorded, and forwarded for onward analysis. It applies to all of the MoJ systems. In most cases, this requirement may be met through the underlying platform\(s\) on which the systems are built.

This tier covers the broad spectrum of events that can reasonably be used to detect compromise. It allows the defensive cyber team to respond appropriately before significant impact.

## Enhanced

The enhanced tier, in conjunction with the baseline event types, provides earlier notification of attempted compromise. It enables gathering of more information to detect stealthier or more capable attackers.

## Bespoke

The bespoke tier concerns systems that are critical to the security, stability and statutory function of the MoJ, or that contain highly sensitive data. In this tier, systems must generate additional bespoke \(customised\) event types. These event types are typically agreed in context between the MoJ Cyber Security team and the associated product or service team. The objective is produce logging that reliably identifies and captures key nuance and contextual security monitoring data, based on applicable threats and risks.

## Contact details

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for cyber security advice, contact the Cyber Assistance Team: [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

