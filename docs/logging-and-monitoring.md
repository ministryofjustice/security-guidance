# Logging and monitoring

The monitors the use of services, by recording \(logging\) event information.

This is permitted under data protection legislation, to help defend services against cyber security attacks, and misuse \(such as fraud\). General Data Protection Regulation \(GDPR\) [Recital 49](https://www.privacy-regulation.eu/en/recital-49-GDPR.htm) notes that the processing of personal data \(to the extent that is strictly necessary and proportionate\) to ensure the security of a system which forms the underlying lawful basis for why the processes this type of data for this purpose.

This is why the can log and monitor external interactions with its services, looking for evidence of cyber security attacks. It also allows the to act to protect those services. For example, the can block an IP address associated with known malware, or which is trying to perform a denial of service attack.

At the same time, the is careful not to "over-retain" log information, or to share it with those who do not need to access it, without lawful justification. The must always act in a proportionate way with this data.

The Chief Information Security Officer \(CISO\) is ultimately responsible for all logging and monitoring systems which have been implemented for cyber security purposes. This means that the CISO is also the Information Asset Owner for all logging and monitoring data.

<a name="[online-identifiers-in-security-logging-and-monitoring](online-identifiers.md)"></a>

-   **[Online identifiers in security logging and monitoring](online-identifiers.md)**  


**Related information**  


[Online identifiers in security logging and monitoring](online-identifiers.md)

[Privileged User Logging and Protective Monitoring Guide](privileged-user-logging-and-protective-monitoring-guide.md)

[Security Log Collection](security-log-collection.md)

## Log retention

A distinction is drawn between web-facing services \(available to anyone on the public Internet\) and internal-facing services \(available only to people who are authenticated by an or Government means of identification, for example an email address or login ID\).

Application logs be kept for the same period as those for other services. The reason is that they might contain relevant information if evidence of an intrusion is found.

### Logs for external services

Logs for all services that can be accessed from the public Web be kept for a minimum of 90 days.

### Logs for internal services

Logs for all services that are accessed using an or Government identity or login be kept for a minimum of 13 months.

### Maximum retention period

Logs be retained for longer than 2 years without specific approval from the CISO. However, aggregate data from logging systems, such as the number of particular types of events or the total numbers of visits to sites, be retained indefinitely, so long as care is taken to remove potentially unique or personally identifying information from the retained information set.

### Variations and exceptions

These requirements are defined and required by legislation, regulation such as the Law Enforcement Directive, or certification compliance such as [PCI-DSS](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard). Variations or exceptions be created without the specific documented permission of the CISO

## Protecting log files and log data

Default permissions must be set on logging and monitoring systems such that only ops staff for that service, and the 's Security team \(\), have access to the data in them. All access to the raw logging and monitoring data must also be logged.

Bulk exporting from such logging systems is prohibited by default. Where analysis is required using sensitive logs, it must be performed "in-situ". Bulk exporting should be prevented by default, using technical or other access controls where possible. If a bulk extract from a logging system is required, for example, into a more complex analytical system or as part of a wider migration, this requires the prior approval of the CISO.

