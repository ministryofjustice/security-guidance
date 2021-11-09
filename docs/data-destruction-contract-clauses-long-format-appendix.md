# Long format appendix

The current draft of the Ministry of Justice \(MoJ\) commodity long format data destruction appendix. The appendix is a dependency of the long format clause itself.

`Highlighted` words indicate potential requirement for contextual change, requirement of definition and so on.

## Appendix

The following standards and guidelines are the *minimum* basis for data decommissioning or destruction. Follow and apply them as appropriate. There might also be extra steps specific to a data set or system.

-   National Cyber Security Centre \(NCSC\) guidance on end-user device reset procedures: [https://www.ncsc.gov.uk/guidance/end-user-device-guidance-factory-reset-and-reprovisioning](https://www.ncsc.gov.uk/guidance/end-user-device-guidance-factory-reset-and-reprovisioning)

-   NCSC guidance on secure sanitisation of storage media: [https://www.ncsc.gov.uk/guidance/secure-sanitisation-storage-media](https://www.ncsc.gov.uk/guidance/secure-sanitisation-storage-media)

-   NCSC Cloud Security Principle 2: Asset Protection and Resilience \(Data Destruction\): [https://www.ncsc.gov.uk/guidance/cloud-security-principle-2-asset-protection-and-resilience\#sanitisation](https://www.ncsc.gov.uk/guidance/cloud-security-principle-2-asset-protection-and-resilience#sanitisation)

-   Payment Card Industry Data Security Standard \(Data Destruction\): [https://www.pcisecuritystandards.org](https://www.pcisecuritystandards.org)

-   DIN: [http://www.din-66399.com/index.php/en/securitylevels](http://www.din-66399.com/index.php/en/securitylevels)


Data Destruction for electronic/magnetic storage **must** include, unless otherwise superseded by NCSC, PCI-DSS or specific `Authority` guidance:

-   the revocation or otherwise destruction of decryption keys and/or mechanisms to render data inaccessible or otherwise void through the use of modern cryptography; AND/OR

-   data overwriting methods consisting of at least 3 \(three\) complete overwrite passes of random data.


Data Destruction for printed materials **must** include, unless otherwise superseded by NCSC or specific `Authority` guidance:

-   paper cross-shredding methods to satisfy at least the DIN 66399 Level 4 standard with a maximum cross cut particle surface area 160 \(one hundred and sixty\) millimetres squared with a maximum strip width of 6 \(six\) millimetres


The required outcome is to ensure that `Authority` data is inaccessible by any reasonable commercial and resourced means \(such as commercially available data recovery services\).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

