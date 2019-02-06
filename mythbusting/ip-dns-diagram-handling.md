---
expires: 2019-03-15
---
# IP addresses, DNS information & architecture documentation

## OFFICIAL-SENSITIVE? Not by default

The MOJ does **not** consider it's IP address, DNS or architectural information to be `SENSITIVE` (a handling caveat within the `OFFICIAL` information classification) *by default*.

In some contexts, this information may be considered sensitive (usually when combined with other information), for example, "Server X on IP address x.x.x.x has not been security patched for 5 years and there are known vulnerabilities which are unmitigated and thus could actively be exploited in this moment."

IP addresses of connecting clients (for example, the IP address of the computer of a general member of the public accessing a public MOJ digital service) *may* be Personal Data.

### RFC1918 addresses

[Private network IP addresses](https://en.wikipedia.org/wiki/Private_network) cannot be directly accessed from public networks so require multiple faults or compromises to be useful as part of an exploit.

### Information via email

IP addresses, DNS information & architecture documentation can generally be sent via email services that enforce adequate in-transit integrity/encryption without any additional security protections such as the use of ZIP files.
