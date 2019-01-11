---
expires: 2019-03-15
---
# Cryptography

## The base principles

* All data **must** employ adequate and proportionate cryptography to preserve confidentiality and integrity whether data is at-rest or in-transit.
* Existing cryptographic algorithms (and implementations thereof) should be used - at the highest possible abstraction level.

## In-transit

In-transit encryption techniques can both protect data during transit through cryptography but also help facilitate the establishing of identity of devices on one or more sides of the connection.

### Transport Layer Security (TLS)

The [National Cyber Security Centre (NCSC)](https://www.ncsc.gov.uk/) have published information on good TLS configurations [https://www.ncsc.gov.uk/guidance/tls-external-facing-services](https://www.ncsc.gov.uk/guidance/tls-external-facing-services).

In general, subject to document exceptions (such as end-user needs and required legacy backwards compatiability)

### Testing

Tools such as [Qualys SSL Server Test](https://www.ssllabs.com/ssltest/) and Check TLS services from [checktls.com](http://www.checktls.com/index.html) **must** be used where applicable to help identify most common issues and configuration problems.

While these tools are not a replacement for skilled testing, the outputs of these tools can help you identify inefficient or insecure configurations which should be considered for remediation.

Configurations should be periodically re-validated.

### Internet protocol security (IPsec)

NCSC have published information on good IPsec configurations [https://www.ncsc.gov.uk/guidance/using-ipsec-protect-data](https://www.ncsc.gov.uk/guidance/using-ipsec-protect-data).

## At-rest

At-rest encryption techniques can protect data while being stored and even during some processing. At-rest techniques usually protect against physical theft or attack methods.

### 3rd Party Storage

When using 3rd party services/storage from cloud providers such as Amazon Web Services (AWS) or Microsoft Azure for example, you must always enable encryption-at-rest by default. Ensuring unauthorised access to the encryption key is vital, therefore depending on the risks, the key management can either be managed by yourself or by the cloud provider. 

### Portable storage

Portable storage such as CDs, DVDs and USB sticks can be safely used to move data. As usual, data must be adequately protected based on the overall governance and information risk requirements.

While the following certifications are preferred, they may not be required based on the data and data methods being stored or transported.

* [FIPS 140-2 Level 3](https://en.wikipedia.org/wiki/FIPS_140-2)
* [NCSC CPA](https://www.ncsc.gov.uk/scheme/commercial-product-assurance-cpa)
* [NATO Restricted Level Certified](https://www.ia.nato.int/NIAPC/)

The MOJ prefers the use of network-based transfers compared to the use of portable storage (even if the portable storage is encrypted).

### Portable end-user devices

Portable end-user devices such as laptops, tablets and smart phones must utilised at-rest encryption to protect on-board data (and subsequent configured accounts) while the device is 'locked' or powered down.

The [NCSC End-user Device Security Collection](https://www.ncsc.gov.uk/guidance/end-user-device-security) discusses per-platform configuration advice.

Summarily, native at-rest encryption must be enabled with a suitable and proportional decryption code (typically, a password) and hardware-backed cryptography is preferred.

### Hashing

The published [MOJ Password Standard](https://github.com/ministryofjustice/itpolicycontent/blob/master/content/security/framework/password-standard.md) has a [section on hashing as part of password storage](https://github.com/ministryofjustice/itpolicycontent/blob/master/content/security/framework/password-standard.md#password-storage).