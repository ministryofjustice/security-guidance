# Supplier corporate IT

The Ministry of Justice \(MoJ\) does not by default prohibit the use of supplier organisation corporate IT for processing MoJ data. The expectation is that the supplier corporate IT environment is well designed, maintained, governed, and defended, in line with large scale commercial threat models.

Subject to the requirements described in this document, the MoJ does not require suppliers to create or maintain dedicated or segregated IT solutions for processing MoJ data classified at `OFFICIAL`.

For MoJ data classified at `OFFICIAL-SENSITIVE`, additional comprehensive security assurance is required. The assurance **SHALL** include controls and governance processes. The assurance **SHALL** be appropriate to the information sensitivity. Contact the [Cyber Assistance Team](mailto:CyberConsultancy@digital.justice.gov.uk) for assistance regarding acceptable security assurance for `OFFICIAL-SENSITIVE` MoJ data.

## Technical security

Supplier corporate IT systems are expected to maintain appropriate levels of technical security defences. These defences **SHALL** protect appropriately all types of MoJ data. This includes MoJ data processed or stored in any way by supplier corporate IT systems.

Examples of appropriate defences include, but are not limited to:

-   Use of current Transport Layer Security or IPSec for in-transit encryption.
-   Hashing and cryptography mechanisms for data stored at-rest.

The defences **SHALL** scale from individual data items in a database, up to entire storage facilities.

Supplier systems **SHALL** be proportionally resilient to malware. This might be achieved by ensuring segregation between systems, users, and data. Other industry standard best practices, such as email attachment scanning or filtering, might also be suitable.

### Email security

Supplier corporate email systems processing MoJ data **SHALL** align to the [UK government secure email policy](https://www.gov.uk/guidance/securing-government-email), thereby following widely accepted best practices.

Supplier corporate email systems are not required to integrate to the Public Services Network \(PSN\).

## Data Governance

### Data offshoring

Supplier's **MAY** process MoJ data, including Personal Data for which the MoJ is responsible, outside of the United Kingdom, subject to the maintenance of acceptable information controls and governance.

MoJ data **SHALL NOT** be processed within a legal framework that is incompatible with that of the United Kingdom.

#### Working overseas

Supplier staff are not prohibited from working overseas while processing `OFFICIAL` MoJ data, subject to implementing and maintaining acceptable information controls and governance. In particular, the controls and governance **SHALL** align and comply with MoJ policy on [remote working](remote-working.md) and [working overseas](accessing-moj-it-systems-from-overseas.md).

When working overseas, it might be necessary to limit access to information while the user travels. Alternatively, it might be appropriate to use secondary, temporary accounts, to avoid primary account compromise. Contact the [Cyber Assistance Team](mailto:CyberConsultancy@digital.justice.gov.uk) for assistance regarding acceptable security assurance when working overseas.

### Data backups

Supplier corporate IT systems **MAY** backup data for extended retention times. An example would be keeping archived or deleted emails for an additional few months. Backup systems **MAY** also exist in such a way that individual backup items cannot be individually deleted, but instead are subject to a system-wide backup rotation or retention schedule.

Suppliers **SHALL** discuss and agree these cases with the MoJ.

### Local end-user device data

The MoJ acknowledges that corporate users typically "download" files, for example from local email client caching to file downloads using a web browser. These files might remain within `Downloads` folders, until explicitly deleted by the user.

Suppliers **SHALL** include and address these types of data locations in data governance regimes.

## Contact details

For any further questions relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk), or for security advice, contact the Cyber Assistance Team [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

