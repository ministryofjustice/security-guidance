# Automated certificate renewal

Where technically suitable, all new Ministry of Justice \(MOJ\) domains **must** use automated certificate techniques and services, such as [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) \(most preferred\) or [LetsEncrypt](https://letsencrypt.org/) \(uses [ACME](https://en.wikipedia.org/wiki/Automated_Certificate_Management_Environment)\)

Over time, existing MOJ domains **must** also be considered for migration to automated certificate provisioning and management techniques \(preferably on their next certificate renewal cycle in advance of expiry\) in order to reduce the consequences and management overheads of manual certificate renewal.

The MOJ acknowledges that not all systems support automated certificate management but leveraging such technology where possible reduces management overheads, the costs of such overheads and the consequences of unexpected certificate expiry.

## Manual certificate requests

Where automated certificate renewal is not possible, new certificates **must** be acquired through the MOJ Certificates team.

To request a manually issued certificate, complete the [certificate request form](https://docs.google.com/document/d/14XbWoudZd-t4-J3mDBcrAeafAbqxwvdkV-u3Zf8eLOs/edit?usp=sharing) and send it, with a [Certificate Signing Request \(CSR\)](https://docs.gandi.net/en/ssl/common_operations/csr.html#generate-csr) \(and an authority email approval if not an MOJ employee e.g. 3rd party supplier\), to [certificates@digital.justice.gov.uk](mailto:certificates@digital.justice.gov.uk).

