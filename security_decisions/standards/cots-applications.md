---
category: Security Log Collection
expires: 2020-03-01
---

# Commercial off-the-shelf applications

We have developed a series of logging requirements for Commercial off-the-shelf (COTS) applications, such as Software-as-a-Service (SaaS) solutions or where applications are not so customised that they can reasonably be considered bespoke/custom for the MOJ.

## Baseline Maturity Tier

### 1. User directory services
Log Collection Principle(s): 1, 2

User directory services, or interactions with them, must create and forward Authentication and Authorisation events.

User directories within application environments can be rich and diverse, such technologies include:
* Active Directory (AD)
* Azure Active Directory
* OpenLDAP
* Amazon Web Services (Accounts and Incognito)
* Okta
* Auth0
* Github.com (acting as an identity provider)
* Google G-Suite (acting as an identity provider)
* Oracle identity stores
* Local user stores within operating systems leveraged by tenant applications

These event types must be logged and forward:
* a: account creation
* b: account lockout
* c: account reinstatement
* d: account authentication failures
* e: account authentication successes after 1 or more failures
* f: account password changes
* g: group membership addition / deletion (in particular, any group that gives admin access)
* h: group creation
* i: privilege modification for users (for example, role delegation through AWS IAM)
* k: multi-factor authentication state, such as:
    * 1: enabled
    * 2: disabled
    * 3: reset/rotation
    * 4: recovery method used

### 2. Authenticated user activity events
Log Collection Principle(s): 6

Applications should create viable user activity audit information for authenticated users to reasonably identify which authenticated user took which action.

* a: user/group identifier(s)
* b: action/query
* c: response size
* d: response time

## Enhanced Maturity Tier

### 1. Data store events
Log Collection Principle(s): 6

Temporary data stores (such as intermediate queues) and permanent data store (such as databases) are key data locations and all interactions should be highly auditable.

* a: data store identifier(s)
* b: credential identifier(s)
* c: query
* d: query response size
* e: query response time

### 2. Unauthenticated user activity events
Log Collection Principle(s): 6

Where unauthenticated users interact with applications (for example, a MOJ G-Suite document available on the general Internet through relaxed access controls), associated audit information must be created.

* a: end-client identifier(s)
* b: query metadata
    * 1: destination identifier (such as target hostname, TCP/UDP port and/or full URI)
    * 2: query type (for example, HTTP GET or HTTP POST)
    * 3: query size
* c: response size
* d: response time
