# Shared Responsibility Models

The Ministry of Justice \(MoJ\) by default will leverage shared responsibility models, particularly in commodity environments, in order to achieve efficiencies such as time, risk and cost.

The MoJ believes that it should focus on elements which are unique to its requirements rather than attempting to solve commodity requirements in a unique way.

h/t [https://aws.amazon.com/compliance/shared-responsibility-model/](https://aws.amazon.com/compliance/shared-responsibility-model/)

## Assessments

The MoJ conducts assessments \(including risk assessments\) where appropriate to ensure it understands the shared responsibility model, its obligations under the same and measure how third-parties are meeting their obligations.

### Inherited

The MoJ inherits controls which are fully controlled and managed by a third-party, such as physical and environmental controls in a data centre.

### Shared

MoJ has shared controls which is jointly responsible for with the third-party, for example:

-   Patch Management - AWS is responsible for patching and fixing flaws within the infrastructure, but customers are responsible for patching their guest OS and applications.

-   Configuration Management - AWS maintains the configuration of its infrastructure devices, but a customer is responsible for configuring their own guest operating systems, databases, and applications.

-   Awareness &amp; Training - AWS trains AWS employees, but a customer must train their own employees.


### MoJ specific

The MoJ is responsible for appropriate use within its partnership or 'tenancy' of a third-party supplier or product.

For example, in AWS, MoJ must correctly leverage native AWS functionality \(such as Security Groups\) to protect systems/data, and only the MoJ can implement these.

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

