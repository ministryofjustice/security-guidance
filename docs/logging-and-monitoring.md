# Logging and monitoring

-   **[Online identifiers in security logging and monitoring](online-identifiers.md)**  


**Related information**  


[Security Log Collection](security-log-collection.md)

[Privileged User Logging and Protective Monitoring Guide](privileged-user-logging-and-protective-monitoring-guide.md)

## Overview

The Ministry of Justice \(MoJ\) monitors the use of services, by recording \(logging\) event information.

This is permitted under data protection legislation, to help defend MoJ services against cyber security attacks, and misuse \(such as fraud\). General Data Protection Regulation \(GDPR\) [Recital 49](https://www.privacy-regulation.eu/en/recital-49-GDPR.htm) notes that the processing of personal data \(to the extent that is strictly necessary and proportionate\) to ensure the security of a system which forms the underlying lawful basis for why the MoJ processes this type of data for this purpose.

This is why the MoJ can log and monitor external interactions with its services, looking for evidence of cyber security attacks. It also allows the MoJ to act to protect those services. For example, the MoJ can block an IP address associated with known malware, or which is trying to perform a denial of service attack.

At the same time, the MoJ is careful not to “over-retain” log information, or to share it with those who do not need to see it, without lawful justification. The MoJ must always act in a proportionate way with this data.

The MoJ Chief Information Security Office \(CISO\) is ultimately responsible for all logging and monitoring systems which have been implemented for cyber security purposes. This means that the CISO is also the Information Asset Owner for all logging and monitoring data.

## Log retention

By default, the MoJ retains raw logs in direct relation to security logging and monitoring purposes for at least 90 days, and for a maximum of 2 years.

The variation in between is as defined and required by legislation, regulation \(such as the Law Enforcement Directive\) or certification compliance \(such as [PCI-DSS](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)\). Retention for periods longer than 2 years requires MoJ CISO approval.

Logs for web-facing services should normally be kept for 90 days.

Logs for internal-only services should normally be kept for 13 months.

Aggregate data from logging systems, such as the number of particular types of events, the total numbers of visits to sites, and so on, can be retained indefinitely, so long as care has been taken to remove potentially unique or identifying information from the retained information set.

## Protecting log files and log data

Default permissions must be set on logging and monitoring systems such that only ops staff for that service, and the MoJ's security operations team \([OperationalSecurityTeam@justice.gov.uk](mailto:OperationalSecurityTeam@justice.gov.uk)\), have access to the data in them. All access to the raw logging and monitoring data must also be logged.

Bulk exporting from such logging systems is prohibited by default. Where analysis is required using sensitive logs, it must be performed “in-situ”. Bulk exporting should be prevented by default, using technical or other access controls where possible. If a bulk extract from a logging system is required, for example, into a more complex analytical system or as part of a wider migration, this requires the prior approval of the MoJ CISO.

## Contact details

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for security advice, contact the Cyber Assistance Team [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

