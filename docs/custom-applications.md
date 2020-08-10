# Custom Applications

We have developed a series of logging requirements for custom applications, such as digital services, applications materially customised that they can reasonably be considered bespoke/custom for the MOJ and line of business applications at different maturity tiers in order to support defensive cyber security, such as detecting breaches.

## Baseline Maturity Tier

### 1. User directory services

Log Collection Principle\(s\): 1, 2

User directory services, or interactions with them, must create and forward Authentication and Authorisation events.

User directories within application environments can be rich and diverse, such technologies include:

-   Active Directory \(AD\)

-   Azure Active Directory

-   OpenLDAP

-   Amazon Web Services \(Accounts and Incognito\)

-   Okta

-   Auth0

-   Github.com \(acting as an identity provider\)

-   Google G-Suite \(acting as an identity provider\)

-   Oracle identity stores

-   Local user stores within operating systems leveraged by tenant applications


These event types must be logged and forward:

-   a: account creation

-   b: account lockout

-   c: account reinstatement

-   d: account authentication failures

-   e: account authentication successes after 1 or more failures

-   f: account password changes

-   g: group membership addition / deletion \(in particular, any group that gives admin access\)

-   h: group creation

-   i: privilege modification for users \(for example, role delegation through AWS IAM\)

-   k: multi-factor authentication state, such as:

    -   1: enabled

    -   2: disabled

    -   3: reset/rotation

    -   4: recovery method used


### 2. Authenticated user activity events

Log Collection Principle\(s\): 6

Applications should create viable user activity audit information for authenticated users so it is reasonably possible to understand retrospectively which actions the user took or attempted.

-   a: user/group identifier\(s\)

-   b: action/query

-   c: response size

-   d: response time


### 3. Unauthenticated user activity events

Log Collection Principle\(s\): 6

Where unauthenticated users interact with applications \(for example, a digital service published and available on the general Internet\), associated audit information must be created.

-   a: end-client identifier\(s\)

-   b: query metadata

    -   1: destination identifier \(such as target hostname, TCP/UDP port and/or full URI\)

    -   2: query type \(for example, `HTTP GET` or `HTTP POST`\)

    -   3: query size

-   c: response size

-   d: response time


## Enhanced Maturity Tier

### 1. Pipeline events

Log Collection Principle\(s\): 1, 2, 3, 6

Continuous integration and continuous deployment pipelines obey instructions to manage applications and are a privileged position to oversee all associated resources, they must be highly auditable to clarify activity and attribute the same.

-   a: source identifier\(s\)

    -   1: user\(s\)

    -   2: repository

-   b: activity events

    -   1: resource creation

    -   2: resource destruction

    -   3: target environment


### 2. Data store events

Log Collection Principle\(s\): 6

Temporary data stores \(such as intermediate queues\) and permanent data store \(such as databases\) are key data locations and all interactions should be highly auditable.

-   a: data store identifier\(s\)

-   b: credential identifier\(s\)

-   c: query

-   d: query response size

-   e: query response time


