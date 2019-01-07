---
category: Data Destruction
expires: 2019-03-15
---
# Longform appendix

The current draft of the MOJ commodity longform data destruction appendix. The appendix is a dependancy of the longform clause itself.

`Highlighted` words indicate potential requirement for contextual change, requirement of definition and so on.

## Appendix

While all applicable and proportional steps must be defined by the context of the dataset(s) and/or system(s), the following standards or guidelines are expected to be followed and applied accordingly:

- National Cyber Security Centre (NCSC) guidance on end-user device reset procedures: <https://www.ncsc.gov.uk/guidance/end-user-device-guidance-factory-reset-and-reprovisioning>
- NCSC guidance on secure sanitisation of storage media: <https://www.ncsc.gov.uk/guidance/secure-sanitisation-storage-media>
- NCSC Cloud Security Principle 2: Asset Protection and Resilience (Data Destruction): <https://www.ncsc.gov.uk/guidance/cloud-security-principle-2-asset-protection-and-resilience#sanitisation>
- Payment Card Industry Data Security Standard (Data Destruction): <https://www.pcisecuritystandards.org>

Data Destruction must include, unless otherwise superseded by NCSC, PCI-DSS or `Authority` guidance, the revocation or otherwise destruction of decryption keys and/or mechanisms to render `Authority Data` inaccessible or otherwise void through the use of modern cryptography and/or a data overwriting methods consisting of at least 3 (three) complete overwrite passes of random data.