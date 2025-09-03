# Guidance on IT Health Checks

**Classification:** OFFICIAL **Scope:** All Ministry of Justice \(MoJ\) staff, contractors, and suppliers **Expires:** When rescinded or replaced, with annual review **Authors:** [Security Policy, Awareness, Culture, and Education team \(SPACE\)](mailto:SPACE@justice.gov.uk) **Authorised by:** MoJ Chief Information Security Officer **Date of publication:** 3 September 2025

## 1. Introduction

A definition and guidance for IT Health Checks \(ITHCs\) is available through [GOV.UK](https://www.gov.uk/government/publications/it-health-check-ithc-supporting-guidance/it-health-check-ithc-supporting-guidance). ITHCs provide independent assurance: 

1.  that internal systems have no significant weaknesses in their design, or interactions with other infrastructure or services that could allow one internal device, system, product, or service to impact on the security of another intentionally or unintentionally. 
2.  that external systems and services are protected from unauthorised access or change. 
3.  to the Cabinet Office, that services do not provide an unauthorised entry point into systems that consume Public Services Network \(PSN\) services. 

The MoJ approach to Secure by Design may involve penetration tests and/or vulnerability assessments at any stage of a service or product implementation \(including during Business as Usual\), and/or at an organisational level \(from individual agencies and business units up to MoJ-wide\). 

A definition and guidance on penetration testing is available through [GOV.UK](https://www.gov.uk/service-manual/technology/vulnerability-and-penetration-testing). Penetration tests and vulnerability assessments help to make sure services are secure. 

## 2. Scope

This guidance applies to all staff employed by the MoJ, its agencies and associated bodies, and to contractors and third-party suppliers who manage information on our behalf.

## 3. Guidance

### When should an ITHC be considered?

There are 3 primary scenarios when an ITHC might be undertaken:

1.  Introduction of new IT services 
2.  Changes to an existing IT baseline 
3.  To meet compliance requirements, such as PSN Code of Connection \(CoCo\)

#### Introduction of new IT services

Commissioning an ITHC at the design and build phase allows service owners to validate the service against the stated risk tolerance and position. The scope of the ITHC can be adjusted to test security and technical controls to target and verify their effectiveness. ITHC results can then be used as a baseline security position against which future changes can be internally risk assessed. An ITHC is a significant artifact for Secure by Design.

#### Changes to an existing baseline

When major changes are made to an existing service, a new ITHC is required to provide assurance of the new service configuration. Major changes may be either updates to part of a system or service with significant security responsibility, or changes to significant parts of the overall system that cumulatively change the security position.

If a change creates an increased risk of misconfiguration, an ITHC should be considered as part of the change process. If you are not sure whether an ITHC is required, contact your local security team for guidance or reach out to the central mailbox [security@justice.gov.uk](mailto:security@justice.gov.uk) or \#security on Slack.

### Before an ITHC

The scope of an ITHC can be broad, including a wide variety of internal and external tests. See the [NCSC guidance](https://www.gov.uk/government/publications/it-health-check-ithc-supporting-guidance/it-health-check-ithc-supporting-guidance) for a fuller breakdown of recommended internal and external tests. Consider the timeframe allocated for the ITHC and consider whether tests must be time-boxed or services sampled.

ITHCs are performed by highly trained specialists from a third-party service provider. ITHC specialists are trained to not actively exploit vulnerabilities in services or run service-impacting tests without permission. An ITHC should not be a risky activity, so running an ITHC on your production environment can be advantageous. Testing a production environment provides greater assurance that the service can withstand intrusion attempts and protect valuable data and systems.

However, if some tests are expected to cause issues, consider testing on a non-production environment. This should only be done if the non-production environment is a true representation of the production environment.

#### Vulnerability Scanning

Vulnerability scans of a service provide regular and consistent checks against known vulnerabilities, though they do not offer the broader assurance of an ITHC. Vulnerability scans should be run on a regular basis and should be completed before beginning an ITHC to avoid the ITHC report finding vulnerabilities that could have been detected and remediated earlier.

Click here for further information and [guidance about vulnerability scanning](https://security-guidance.service.justice.gov.uk/vulnerability-scanning-guide/#roles-and-responsibilities).

#### Logging and Monitoring

All MoJ services should have security logging and monitoring, with logs going to a central Security Operations Centre \(SOC\) for live monitoring and alerting. Subject to your agreement with any SOC, you may be required to inform them prior to any test taking place.

You may receive alerts related to the testing activity and if those alerts are actioned \(such as blocking an IP address\) you may risk impacting the ITHC. Not all ITHC tests will be highlighted as malicious, so some ITHC tests may go entirely unnoticed, however some specific tests should be reported on. Speak to your testers and/or local security team for further guidance on logging specific tests as they happen.

#### External or Cloud Platform Considerations

If the application or service you intend to test is hosted within a cloud platform service offering, such as Microsoft Azure and AWS \(Amazon Web Services\), there are Rules of Engagement that you should be aware of. Information can be found for the following: 

-   Microsoft Azure: [https://www.microsoft.com/en-us/msrc/pentest-rules-of-engagement](https://www.microsoft.com/en-us/msrc/pentest-rules-of-engagement)
-   AWS: [https://aws.amazon.com/security/penetration-testing/](https://aws.amazon.com/security/penetration-testing/)

The same is true if an application or service is hosted by any external third-party, for example: a service hosted on-premises by a supplier. Contact your MoJ cloud provider or external service provider for more details on specific rules of engagement for your platform. 

### Commissioning an ITHC

When commissioning an ITHC, use the process defined on the MoJ HQ Intranet.

## 4. Contact and Feedback

For any further questions or advice relating to security, or for any feedback or suggestions for improvement, contact [security@justice.gov.uk](mailto:security@justice.gov.uk).

