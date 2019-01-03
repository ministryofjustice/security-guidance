---
category: Shared Responsibility Models
expires: 2019-07-01
---

# Shared Responsibility Models

The MOJ by default will leverage shared responsibility models, particularly in commodity environments, in order to achieve efficiencies such as time, risk and cost.

The MOJ believe that it should focus on elements which are unique to its requirements rather than attempting to solve commodity requirements in a unique way.

h/t [https://aws.amazon.com/compliance/shared-responsibility-model/](https://aws.amazon.com/compliance/shared-responsibility-model/)

## Assessments

The MOJ conduct assessments (including risk assessments) where appropriate to ensure it understands the shared responsibility model, it's obligations under the same and measure how third-parties are meeting their obligations.

### Inherited

The MOJ inherits controls which are fully controlled and managed by a third-party, such as physical and environmental controls in a data centre.

### Shared

MOJ has shared controls which is jointly responsible for with the third-party, for example:

* Patch Management – AWS is responsible for patching and fixing flaws within the infrastructure, but customers are responsible for patching their guest OS and applications.
* Configuration Management – AWS maintains the configuration of its infrastructure devices, but a customer is responsible for configuring their own guest operating systems, databases, and applications.
* Awareness & Training - AWS trains AWS employees, but a customer must train their own employees.

### MOJ specific

The MOJ is responsible for appropriate use within it's partnership or 'tenancy' of a third-party supplier or product.

For example, in AWS, MOJ must correctly leverage natively AWS functionality (such as Security Groups) to protect systems/data, and only the MOJ can implement these.