---
category: Security Log Collection
expires: 2020-03-01
---

# Hosting Platforms

We have developed a series of logging requirements for hosting platforms, such as virtualised and/or containered compute with associated supporting services such as database and queuing services at different maturity tiers in order to support defenisve cyber security, such as detecting breaches.

## Baseline Maturity Tier

### 1. User directory services
Log Collection Principle(s): 1, 2

User directory services must create and forward Authentication and Authorisation events from the directory service itself.

User directories within hosting environments can be rich and diverse, such technologies include:
* Active Directory (AD)
* Azure Active Directory
* OpenLDAP
* Amazon Web Services (Accounts and Incognito)
* Okta
* Auth0
* Github.com (acting as an identity provider)
* Google G-Suite (acting as an identity provider)
* Local user stores within operating systems

These event types must be logged and forward:
* a. account creation
* b. account lockout
* c. account reinstatement
* d. account authentication failures
* e. account authentication successes after 1 or more failures
* f. account password changes
* g. group membership addition / deletion (in particular, any group that gives admin access)
* h. group creation
* i. privilege modification for users (for example, role delegation through AWS IAM)
* k. multi-factor authentication state, such as:
⋅⋅1. enabled
⋅⋅2. disabled
⋅⋅3. reset/rotation
⋅⋅4. recovery method used

### 2. Bastion/Jump/Action-proxy services
Log Collection Principle(s): 1, 2, 6

Bastion/jump boxes that act as a management consolidation route and should be highly auditable therefore must create and forward security-related event data.

* a. SSH keypair generation/revocation, including:
⋅⋅1. public key
⋅⋅2. keypair ‘friendly name’ / identifier
* b. account login attempts
⋅⋅1. public key
⋅⋅2. username

### 3. Domain name service query logs
Log Collection Principle(s): 4

DNS query logs must be created and forwarded.

* a. client IP address
* b. query
* c. query response content including
⋅⋅1. returned record(s) or NXDOMAIN
⋅⋅2. authoritative nameserver
* d. query response code
* e. zone and/or view identifier (if local zone response and/or multiview)

This remains true for where nodes (for example, servers) may bypass internal DNS services.

### 4. Web proxy access logs
Log Collection Principle(s): 5

Where web traffic proxies exist, access logs should be created and forward and must, include the following variables.

* a. authenticated user name (if applicable)
* b. client identifiers:
⋅⋅1. IP address
⋅⋅2. reverse lookup client name (if applicable)
* c. HTTP method (for example, CONNECT GET)
* d. Where available, full destination/target URL or SNI value
* e. connection return status code (for example, 200 or 403)
* f. size of response

### 5. Hypervisor events
Log Collection Principle(s): 3, 6

Hypervisors manage virtualised compute resources and are entrusted to segregate the same. All instructions to hypervisors should be highly auditable.

* a. virtual machine creation (including templates)
⋅⋅1. identifier(s)
⋅⋅2. operating system image information
* b. virtual machine ‘power’ events
⋅⋅1. identifier(s)
⋅⋅2. ‘power’ on
⋅⋅3. ‘power’ off (including restart flag)
* c. virtual machine deletion
⋅⋅1. identifier(s)
* d. virtual machine resource modification events:
⋅⋅1. CPU addition/removal
⋅⋅2. RAM addition/removal
⋅⋅3. Networking additional/removal
⋅⋅4. Storage mount/dismount/resize

### 6. Orchestrator events
Log Collection Principle(s): 3, 6

Orchestrators such as Cloud Foundry and Kubernetes create and manage a variety of technology resources to facilitate an application environment.

* a. resource creation (including templates)
⋅⋅1. identifier(s)
⋅⋅2. resource type
⋅⋅3. operating system image information (if applicable)
* b. container ‘power’ events
⋅⋅1. identifier(s)
⋅⋅2. ‘power’ on
⋅⋅3. ‘power’ off (including restart flag)
* c. resource deletion
⋅⋅1. identifier(s)
* e. resource modification events:
⋅⋅1. identifier(s)

### 7. Allocation of IP address leases from DHCP services
Log Collection Principle(s): 3, 5

DHCP services must be configured to create and forward the following:

* a. successful client DHCP requests, including:
⋅⋅1. Requesting client MAC address
⋅⋅2. DHCP scope identifier
⋅⋅3. IP address leased
⋅⋅4. IP address lease duration

* b. unsuccessful client DHCP requests, including:
⋅⋅1. Requesting client MAC address
⋅⋅2. DHCP scope identifier (if applicable for unsuccessful request)

## Enhanced Maturity Tier

### 1. Firewall log data for denied network traffic
Log Collection Principle(s): 5

All firewall ‘DENY’ log data must be forwarded.

* a. client IP address
* b. firewall/router identifier
* c. request response code
* d. request content, including:
⋅⋅1. IP protocol (for example, ICMP)
⋅⋅2. destination/target port
⋅⋅3. destination/target IP address
⋅⋅4. destination/target hostname address (if reverse lookup performed)

### 2. Internal DNS namespace zone content
Log Collection Principle(s): 4

Internal domain name spaces must ultimate forward, in an [RFC5936 (DNS Zone Transfer Protocol (AXFR)](https://tools.ietf.org/html/rfc5936) compatible format including all information described in the RFC.

### 3. DHCP scopes (and the functional segmentation of each)
Log Collection Principle(s): 5

Machine-readable DHCP scope exports (and surrounding metadata/description of the purpose of each scope) must be created and forwarded.

### 4. Endpoint protection security logs
Log Collection Principle(s): 6

Security log data (as defined by the vendor) must be created and forwarded.

### 5. Security-related logs for all Windows-based end-user devices
Log Collection Principle(s): 6

Security-related logs, as defined by [NCSC’s Logging Made Easy template](https://github.com/ukncsc/), from all end-user devices operating a Microsoft Windows operating system must be created and forwarded.

### 6. Mobile device enrollment activity
Log Collection Principle(s): 1, 2, 3, 6

Where a mobile device management solution is used and end-user devices register/enrol and de-register/de-enrol with it, enrollment data should be created in and forwarded.

* a. enrolment or un-enrolment event type
* b. end-user device identifier(s), such as client IP address and/or MAC address and/or assigned DHCP name
* c. end-user account name (if applicable)

### 7. VPN concentrator activity data
Log Collection Principle(s): 3, 5

Where VPN services are in use, connection-related log data must be created and forwarded.

* a. success or unsuccess status
* b. user/certificate identifier
* c. client IP address
* d. concentrator identifier

### 8. Pipeline events
Log Collection Principle(s): 1, 2, 3, 6

Continuous integration and continuous deployment pipelines obey instructions to manage hosting environments and are a privileged position to oversee all tenant resources, they must be highly auditable to clarify activity and attribute the same.

* a. source identifier(s)
⋅⋅1. user(s)
⋅⋅2. repository
* b. activity events
⋅⋅1. resource creation
⋅⋅2. resource destruction
