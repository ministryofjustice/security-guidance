---
expires: 2019-03-15
---
# Secrets management

'Secrets' is defined here as a sensitive bit of information that should be kept private but with a technical system or user focus, such as, a password, OAuth token or 'private key' (SSH, certificate etc).

'Secrets' here is **not** referring to the `SECRET` classification.

## The base principle

All secrets **must** be adequately protected from a loss of confidentiality or integrity. Secrets, much like other confidential data, must be controlled so they can only be viewed or influenced by authorised parties.

## Application & infrastructure secrets

All secrets should be adequately protected and suitably stored.

Where possible, use infrastructure-based secrets management services such as [AWS Key Management Service](https://aws.amazon.com/kms/), [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-paramstore.html), [Microsoft Azure Key Vault](https://azure.microsoft.com/en-gb/services/key-vault/) or [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) on MOJ's Cloud Platforms.

It should be rare and exceptional to store secrets within code repositories, such as in Github.com, and where conducted must use [git-crypt](https://github.com/AGWA/git-crypt) to encrypt those secrets and control who has the ability to view (decrypt) those secrets.

Secrets must never be stored in plain-text, particularly in code repositories (even when the repository is set to a private mode).

Secrets for managing infrastructure must be issued as user authentication secrets, not a single shared secret.

## User authentication secrets

User authentication secrets such as SSH private keys or tokens must be generated for each purpose and kept private.

Unless by intended design, authentication secrets should never be shared or published.

SSH private keys should be password protected where practical to do so.