# System Test Standard

**Related information**  


[Technical Controls Policy](technical-controls-policy.md)

## About this document

This document is the System Test Standard. It is designed to help protect IT systems by providing a common standard for system security testing.

## How to use this document

The purpose of this standard is to provide a process around the security testing of IT systems and outline what security issues should be considered at each stage of the process.

**Note:** This document focuses on the security aspects of system testing. It is not intended to provide comprehensive information on general system testing.

## Overview

### Introduction

The purpose of system testing is to ensure all the functional and non-functional requirements of the system are verified to be operating within specified bounds.

[HMG Security Policy Framework](https://www.gov.uk/government/publications/security-policy-framework/hmg-security-policy-framework) mandatory requirements 9 states that:

> Departments and Agencies must put in place an appropriate range of technical controls for all IT systems, proportionate to the value, importance and sensitivity of the information held and the requirements of any interconnected systems.

Policy statements on system testing are covered in the [IT Security Technical Users Policy](it-security-technical-users-policy.md). This document sets out the standard for system test implementation from a security perspective.

### Scope

This standard is concerned with the security testing of all IT systems including IT systems hosted by third party suppliers on behalf of the .

### Definitions

For the purposes of this standard, the following definitions apply:

<a name="system-testing"></a>

-   **System testing**

    Tests conducted against an application or IT system to ascertain whether that application or IT system has implemented the desired functional and non-functional requirements.

<a name="security-testing"></a>

-   **Security testing**

    The subset of system tests which concentrate on testing an application's or IT system's functional and non-functional security requirements.


### Demonstration of Compliance

The [CESG Information Assurance Maturity Model \(IAMM\)](https://www.ncsc.gov.uk/guidance/information-assurance-maturity-model-and-assessment-framework-gpg-40) sets out the minimum maturity level Government departments should attain. System testing is captured as a basic requirement in Level 1, which the will need to demonstrate compliance with in the IAMM return to Cabinet Office.

## Testing approach

This standard outlines at a high level the security testing which must be applied to all IT systems to ensure that security vulnerabilities are identified and risk managed appropriately. The aim is for this standard to feed into the overall test requirements and test plan for an IT system.

System testing, in particular system security testing, must be performed in support of the system assurance process to provide confidence that:

-   The implementation delivers the agreed security controls.
-   There are no unacceptable security vulnerabilities within the delivered solution.

The following three principles must be applied when putting together a test plan for an IT system:

1.  The rigour of the tests must be commensurate with the impact of a security failure.
2.  The tests may need to be repeated to provide assurance that subsequent changes to the system or service have not introduced new vulnerabilities.
3.  The testing services \(automated or otherwise\) used must generate security compliance/assurance evidence against known threats and current IT security policies. For example, penetration testing \(or ITHC\), ad-hoc scanning, secure code review, and software configuration assurance.

**Note:** It is policy that system testing be conducted in a live environment. System testing should combine tests conducted in a non-live system test environment with tests conducted in a live environment \(e.g. an IT Health Check\).

The rest of this document is split into four sections:

1.  [Guidelines](#guidelines): Sets out the basic security requirements for IT system testing and provides guidance on system test data.
2.  [Risk assessment and management](#risk-assessment-and-management): Outlines the link between system assurance and security testing.
3.  [Types of security tests](#types-of-security-tests): Provides an overview of the common types of security testing.
4.  [Pre-live security testing](#pre-live-security-testing): Outlines how security testing links in with the standard set of testing activities which are conducted during the development and deployment phases of an IT system.

### Guidelines

HMG IS 1 and 2 require that assurance evidence is provided covering an IT system's business systems design, implementation, and operation.

Security testing of an IT system to obtain the assurance evidence required can occur at various points throughout the system development and deployment lifecycle \(refer to [Table 1](#security-consideration)\). For example:

<a name="commercial-off-the-shelf-cots-product-assurance"></a>

-   **Commercial off the Shelf \(COTS\) product assurance**

    Test assurance obtained through the use of a security evaluated, either by CESG or via the Common Criteria scheme COTS product. This assurance can be obtained during the system design phase.

<a name="system-configuration-tests"></a>

-   **System configuration tests**

    Test assurance obtained before deployment and maintained thereafter in line with the system re-accreditation process. Further details on the Accreditation process can be found in the [Accreditation Framework](https://intranet.justice.gov.uk/documents/2015/04/accreditation-framework.pdf).


#### System test data

Data used for system testing usually involves test data which have similar characteristics as close as possible to operational data.

Data used for system testing **must not** contain any live data. The use of live data, and in particular live data containing personal information, is prohibited. However, as test data will tend to simulate live operations data, it is important that test data is protected to ensure details of the system design and operation are not compromised.

To protect system test data, the following principles should be followed:

-   The test manager must authorise the use of test data.
-   Test data should be erased from a testing environment immediately after the testing is complete or when no longer required.
-   The copying and use of test data should be logged to provide an audit trail.

In exceptional circumstances, the use of live system data might be permitted. Permission to use live data is by exception only. A valid business case must be approved by the IT Security Officer \(ITSO\), system assurer, and Information Asset Owner \(IAO\). Further information can be obtained from the Data Access and Compliance Unit \(DACU\) who maintain the policy on the use of live personal data.

**Note:** The risk associated with the use of live personal data for testing might require Senior Information Risk Owner \(SIRO\) approval. Refer to [this information](using-live-data-for-testing-purposes.md) for further details.

### Risk assessment and management

As expressed at the start of this section, the rigour of any security tests must be commensurate with the impact of a security failure. This means that a risk based approach must be taken when considering what types of security tests to execute.

The decision on what security tests to include in the overall system test plan must be based on the system IS1 risk assessment, and agreed with the system assurer. The following section \([Types of security tests](#types-of-security-tests)\) provides an overview of the types of security tests which must be considered. Further details on the assurance process can be found in the [Accreditation Framework](https://intranet.justice.gov.uk/documents/2015/04/accreditation-framework.pdf).

When a security test has been conducted, it is likely to highlight several risks and issues which need to be remediated and managed appropriately. This remediation is usually captured in a Risk Treatment Plan \(RTP\) which outlines what the issue or vulnerability identified is, the risk associated with it, and the planned risk mitigation. The RTP needs to be agreed with the system Accreditor prior to being implemented. Further details on this process can be found in the [Accreditation Framework](https://intranet.justice.gov.uk/documents/2015/04/accreditation-framework.pdf).

### Types of security tests

Security testing is discussed as part of the NCSC guidance on [Building a secure digital service](https://www.ncsc.gov.uk/collection/digital-service-security/digital-services-building-secure-digital-service).

This section provides an overview of the three most common types:

-   [System configuration tests](#system-configuration-tests).
-   [Vulnerability scanning](#vulnerability-scanning).
-   [Compliance scanning](#compliance-scanning).

#### System configuration tests

System configuration tests are first conducted prior to deployment and repeated periodically thereafter with the objective being to ensure that the system or system component does not contain any unacceptable vulnerabilities.

These tests may include:

-   Internally conducted tests \(e.g. by the system developer\) to provide informal assurance that there are no unacceptable vulnerabilities.
-   External and perhaps more rigorous tests to provide formal assurance, for example, a penetration test or social engineering test.

There any many different types of penetration test. For most IT systems, the most common conducted is an annual [IT Health Check \(ITHC\)](#it-health-check).

Internal tests may be performed more regularly to provide informal assurance that on-going changes have not introduced any new vulnerabilities to an IT system, and that existing security controls are operating correctly.

##### IT Health Check

An IT Health Check \(ITHC\) is the penetration test conducted as part of the NCSC specified and managed [CHECK scheme](https://www.ncsc.gov.uk/information/check-penetration-testing). It is intended to provide external assurance that an IT system's setup and configuration meets the desired HMG assurance level.

**Note:** Most systems connected to or other government networks or systems mandate an ITHC every 12 months.

#### Vulnerability scanning

A vulnerability scan is intended to scan a network \(and connected IT systems\), cataloguing the patch status of all software and system services, and alerting on those identified which are not up-to-date, based on databases of patches and vulnerabilities. These alerts provide an operational view of the technical vulnerabilities an IT system is exposed to, and the information required to assist an IT system manager in applying up-to-date patches.

This type of scanning is intended to provide regular internal assurance to the ITSO and assurer that operational security risks are being managed effectively.

#### Compliance scanning

Besides simply testing for the absence of correctly patched software, some vulnerability scanners can also test when an IT system's settings correspond to an established benchmark, for example, to the [password requirements](passwords.md), or a commercial security standard such as [PCI DSS](https://www.pcisecuritystandards.org/). The scanner operates by examining the security configuration settings of each IT system client \(through a client installed agent\) against one or more benchmarks \(e.g. PCI DSS or ISO 27001\), producing a compliance report as an output which can be supplied as assurance evidence.

### Pre-live security testing

During the development and deployment phases of an IT system, there are a number of standard testing activities which are conducted. Security testing is not a separate stream of activity. It must be integrated within the overall set of testing activities.

The [Secure code review](#secure-code-review) activity highlights the issues associated with secure code reviews, while the [Security consideration](#security-consideration) activity provides an overview of the security testing consideration which should be applied against each standard testing activity.

#### Secure code review

In principle, good software development practices and the application of a comprehensive code quality assurance regime should cover the basics of what is required to deliver a secure system. The NCSC provides guidance on [Building a secure digital service](https://www.ncsc.gov.uk/collection/digital-service-security/digital-services-building-secure-digital-service). It is recommended that those responsible for software development and system testing review the guidance, and ensure any development practices and system testing reflects the guidance provided.

**Note:** It is essential that the secure coding guidance provided to application developers and the secure code review regime is documented, and made available to the system assurer for review and approval.

#### Security consideration

Table 1 following provides a high level overview of the security testing which should be considered against each of the main testing activities typically conducted during the development and deployment phases of an IT system.

|Testing activity|Description|Security testing consideration|
|----------------|-----------|------------------------------|
|Unit, Module, or Package Testing|This is aimed at verifying that individual modules/packages comply with their design.|Refer to [Secure code review](#secure-code-review).|
|Component Testing|Units or Modules combined into components then tested. This is aimed at verifying that the individual components meet their design and specification requirements. Third party software may also be introduced at this point and tested.|Refer to [Secure code review](#secure-code-review). Functional testing and enhanced secure code review of security enforcing components.|
|Integration Testing|Involves combining system components together into a complete system release, then testing as a whole.|Functional testing of security enforcing components. Functional testing of the integration of components with security enforcing functions.|
|Acceptance Testing \(FAT and SAT\)|The set of tests to be run to demonstrate the suitability of the system to the client. These will typically be a subset of the tests used for system testing in the integration phase.|Testing of both functional and non-functional security requirements. Penetration test or ITHC \(refer to [System Configuration Tests](#system-configuration-tests)\). Vulnerability scan \(refer to [Vulnerability Scanning](#vulnerability-scanning)\). Compliance scan \(refer to [Compliance Scanning](#compliance-scanning)\).|

#### Testing failure

Should a failure occur in any of the security testing activities undertaken, an assessment must be made on what caused the failure and how serious it is. There may need to be discussions with the system assurer to inform them of any serious issues which might affect the assurance of the IT system.

#### Acceptance testing

As described in the last row of Table 1, some form of security testing must form part of the acceptance criteria for an IT System.

