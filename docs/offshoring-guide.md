# Offshoring Guide

## Legacy information

**Note:** This document is Legacy IA Policy. It is under review and likely to be withdrawn or substantially revised soon. Before using this content for a project, contact [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk).

**Note:** This document might refer to several organisations or information sources that have been replaced, as follows:

-   CESG \(Communications-Electronics Security Group\), refer to the National Cyber Security Centre \(NCSC\), contact [security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk).
-   CINRAS \(Comsec Incident Notification Reporting and Alerting Scheme\), refer to the NCSC, contact [security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk).
-   ComSO \(Communications Security Officer\), contact the Chief Information Security Office \(CISO\) \([security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk)\).
-   CPNI \([Centre for the Protection of the National Infrastructure](https://www.cpni.gov.uk/)\), contact the CISO \([security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk)\).
-   DSO \(Departmental Security Officer\), contact the Senior Security Advisor \([security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk)\).
-   GPG6 \(Good Practice Guide 6: Outsourcing and Offshoring: Managing the Security Risks\), refer to the NCSC, contact [security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk).
-   IS1 \(HMG Infosec Standard 1 Technical Risk Assessment\), see the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   IS4 \(HMG Infosec Standard 4 Communications Security and Cryptography\), see the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   IS6 \(HMG Infosec Standard 6 Protecting Personal Data and Managing Information Risk\), see the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security).
-   ITSO \(Information Technology Security Officer\), contact the CISO \([security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk)\).
-   SPF \([Security Policy Framework](https://www.gov.uk/government/publications/security-policy-framework)\), see the [Government Functional Standard - GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security), contact [security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk).

## Introduction

### Document Purpose

This document is the Ministry of Justice \(MoJ\) IT Information Assurance \(IA\) Policy and Guidance for offshoring of MoJ Information Systems, development, or other support services. The document states the IA requirements that must be complied with for offshore developments, and presents considerations to be taken into account when deciding whether to offshore an element of MoJ capability.

This document has not been developed in isolation. It draws heavily and intentionally on other guidance, particularly HMG Good Practice Guide \(GPG\) 6: Outsourcing & Offshoring: Managing the Security Risks. This document collates the high-level points from the CESG and CPNI guidance, and interprets these in the context of the MoJ.

The target audience for this document includes MoJ personnel with a requirement to make offshoring decisions; and MoJ suppliers who are considering, or currently engaged in, delivery of MoJ capabilities with an offshore element.

### Background

#### General

Some suppliers are keen to offshore elements of IT service delivery, due to a perception that this will reap strong financial benefits. Reasons often cited for offshoring decisions include: cost savings in wages and other business expenses relative to the domestic \(UK\) market; access to specific specialist technical skills; and access to a large labour pool to support peak loading or large-scale projects.

Offshoring is not, however, without its potential issues. Badly managed offshoring of a project can lead to over-runs in project costs and timescales which eclipse any anticipated benefits. In the worst cases, project over-spend, over-run and quality issues can lead to project failure. Also, there are a number of scenarios where offshoring would introduce unmanageable risks; and/or result in a direct breach of UK law; and/or result in unexpected financial exposure for the MoJ. These risks are not necessarily a blocker to offshoring, but must be balanced carefully against the anticipated benefits.

#### Quality, Cost and Time

Offshoring presents a range of ubiquitous project risks which must be considered. There can be a tendency to over-estimate the savings that can be made, and to underestimate the potential configuration management and integration issues. Much of the cost saving from offshore development comes from the labour-cost-differential between the UK and favoured offshore locations. High levels of inflation as those economies expand, often through development as offshore centres, can shrink or even overwhelm any predicted cost savings. This may make the supplier's position untenable. Cultural differences can also exaggerate normal project stress points that occur during integration and handover of outsourced elements. Customers and suppliers often fail to fully appreciate increased incidental costs, e.g. due to the additional testing overhead incurred. The long delivery chain can also become a difficulty to manage. In some less stable locations, risks due to war, civil uprising and the availability of Critical National Infrastructure also lead to unique business continuity issues.

#### Legal Risk

Offshore projects may also fall foul of more pedestrian but no less severe risks due to local laws at the offshore location. It is important to ask questions such as: to what extent are the contractual conditions legally binding for an offshore company in a proposed location; how difficult and expensive would it be to mount a legal challenge in the case of contract breach, and is this any less likely to be successful; and who would have priority over information and other assets in the event of a dispute. This is not just an issue which the MoJ will face when engaging an offshore supplier directly; it is also an issue that MoJ's suppliers will face, but may not be aware of, when subcontracting elements of delivery.

#### Risk to "UK PLC"

Many MoJ information systems handle HMG Protectively Marked and/or personal and sensitive personal data. These add a number of specific risks over-and-above the more usual project risks. Local data protection laws may not provide an appropriate level of legal protection, for the data or data subjects involved, against rogue individuals and criminal groups who misappropriate personal data. This may be more of a problem for countries outside of the European Economic Area \(EEA\), where the legal framework may not be familiar. Commercially sensitive information may be similarly at risk. Political instability may lead to facilities being over-run, which as well as having business continuity implications may also have severe consequences from potential disclosure of Protectively Marked information. Also, organised criminals are able to operate more actively and openly in some overseas jurisdictions. Such activity may be driven by political or economic advantage. It is not only the physical site but also application development that can present a risk to data. A vulnerability or backdoor, engineered into an application either maliciously or inadvertently, could be used to leak information over an extended period or even indefinitely without being identified. The [Open Web Application Security Project \(OWASP\)](http://www.owasp.org) presents a list of common vulnerabilities that occur due to careless programming and ineffectual testing. Deliberately engineered vulnerabilities and backdoors are considerably more difficult to identify and address.

#### Personnel Risks

Most people are reliable and honest. However, for work on systems which will handle sensitive Government information, a small number of unreliable or dishonest individuals can cause a disproportionate amount of harm. It is critical, therefore, to identify such high-risk individuals. Pre-employment screening is a critical element in helping to do this, along with aftercare to balance risks identified during screening, and monitor changes to an individual's status that may affect their reliability. Similarly, legal defences provide a complementary means to deter inappropriate behaviour.

### Scope

This document covers offshoring of MoJ business activities. Offshoring is defined here to include development or provision of services, from outside the UK or otherwise using non-UK resources, for domestic \(UK\) consumption.

The scope of offshoring is a broad one. This may involve, for example:

-   Development of applications, and/or provision of second-line and/or third-line support for these applications, from non-UK locations and/or by non-UK Nationals.
-   Follow-the-sun technical support for commercial products, so that suitable technical resources are available at times when domestic support would be unsociable.
-   Remote managed services for wholesale provision of MoJ capabilities from non-UK locations and/or by non-UK Nationals.
-   Other provision of support to the MoJ from non-UK locations and/or by non-UK Nationals.

The scenarios which are to be treated as offshoring are set out in the bulleted list below. This is not necessarily an exhaustive list; in case of uncertainty please contact MoJ IT IA for advice: [security@digital.justice.gov.uk](mailto:security@digital.justice.gov.uk).

-   **Captive centres**

    Refers to an office that forms part of a Government department but is physically located outside the UK.

-   **Far-shoring**

    Covers scenarios where development is to be transferred to locations outside of the EEA. Far-shoring may enable more cost-effective development than near-shoring, or may enable access to specific technical skills. However, far-shoring may require additional National Security and/or legislative considerations to be taken into account relative to near-shoring.

-   **Landed resources**

    Covers scenarios where resources from outside the UK are brought to the UK. This may be, for example, to provide: low-cost labour, specialised skill-sets, and/or support for peak loads. Use of landed resources makes it possible to obtain considerably more control over the working environment of non-UK Nationals on HMG programmes, and can enable a more robust screening and aftercare regime for personnel, traded off against increased development costs.

-   **Near-shoring**

    Covers scenarios where development is to be transferred to other countries within the European Economic Area \(EEA\), where legislation on key issues such as data protection, electronic communications and human rights is broadly aligned with UK legislation. It should be noted that although key legislation is broadly aligned across the EEA by a requirement to meet common EU Directives, the legislation that has been implemented by different EEC nations in order to comply with these directives has some important differences.

-   **Other**

    Any other activity using non-UK locations and/or non-UK Nationals to deliver elements of HMG capability.


### Exclusions from Scope

Exclusion 1: This document does not address UK or overseas legislation. The MoJ legal team, the MoJ Data Access and Compliance Unit \(DACU\), and the MoJ Data Protection EU and International Policy Teams must be consulted on legal issues. Contact [privacy@justice.gov.uk](mailto:privacy@justice.gov.uk) for assistance.

Exclusion 2: This document also does not address protection of individuals' personal data, except within the context of HMG Security Policy. The Data Access and Compliance Unit \(DACU\) must be consulted on personal data, the DPA, and related issues.

With the exception of Landed Resources, deployment to locations within the UK does not count as offshoring and is therefore beyond the scope of this document. It is noted, however, that there will be other geographical factors to be taken into account even within the UK. For example, there are special security arrangements for Northern Ireland, and different freedom of information legislation between England and Scotland. These differences should in no way be considered as a justification not to outsource to other UK locations, but would need to be addressed in the local controls deployed.

Outsourcing is beyond the scope of this document, except insofar as outsourcing arrangements are directly related to offshoring requirements \(e.g. contractual obligations to be included in supplier contracts and subcontracts\). Outsourcing is defined by HMG GPG6 as:

> a contractual relationship with an external vendor that is usually characterised by the transfer of assets, such as facilities, staff or hardware. It can include facilities management \(for data centres or networks\), application development and maintenance functions, end-user computing, or business process services.

### Document Overview

The remainder of this document is structured as follows:

-   The relevant [IA Constraints and Considerations](#ia-constraints-and-considerations) for offshoring.

-   A checklist of [assessment activities](#assessment-activities) at different points in the development lifecycle.


## IA Constraints and Considerations

### General

There are a number of specific IA Constraints which must be satisfied by any MoJ offshoring arrangements. There are also a number of key considerations that must be borne in mind in deciding whether to offshore a particular capability or service.

This section of the document sets out the general IA requirements and constraints that must be complied with when offshoring MoJ capabilities. This document is derived from some of the good but generic CESG and CPNI documentation on the subject, outlined in the [Further Reading](#further-reading) section. This guidance should not be used as a substitute for engagement with the MoJ Accreditor or with MoJ IT IA, who will be able to provide tailored guidance to support individual decisions; it is intended more as general guidance on MoJ policy, to support initial decision-making and project planning.

### Accountability

The development or management of a capability can be outsourced, however, ultimate accountability and responsibility for a capability remains with the end-customer for that capability: in this case the MoJ. The MoJ remains accountable for work performed by third parties on its behalf, whereas outsourcing and offshoring can make it difficult to directly identify and manage information risks and issues. Strong governance and clear lines of accountability and responsibility are required to address this.

[REQUIREMENT 1](#requirement-1-and-requirement-2): The MoJ remains ultimately responsible for the security and overall delivery of offshore application development and other services. All supplier and subcontractor contracts must ensure that the MoJ retains overall control over all security-relevant elements of the delivery. The enforceability of supplier and subcontractor contracts in overseas jurisdictions must be ratified by MoJ legal experts.

If a capability is delivered late, is substandard, fails completely or is compromised, then the MoJ will need to put measures into place to ensure business continuity while a remedial plan is developed and worked through, otherwise essential public services may not be deliverable in the interim. In some cases, the MoJ may find itself financially or legally liable for shortcomings in supplier subcontracts. Also, the MoJ rather than the supplier will almost certainly suffer the brunt of any bad publicity.

The core function of the MoJ is to deliver services for the general good, rather than commercial commodities. As such, the impact of failure is not quantifiable in purely financial terms. Failure or compromise of MoJ services cannot therefore be fully remedied through financial penalties in supplier contracts, although financial penalty clauses can nonetheless serve as a motivation for suppliers to deliver on time and to quality.

The responsibility of the MoJ for its own security and overall delivery is reinforced within the [HMG SPF](https://www.gov.uk/government/publications/security-policy-framework), at Paragraph 7, under Roles and Responsibilities:

> Accounting Officers \(e.g. Head of Department/Permanent Secretary\) have overall responsibility for ensuring that information risks are assessed and mitigated to an acceptable level. This responsibility must be supported by a Senior Information Risk Owner \(SIRO\) and the day-to-day duties may be delegated to the Departmental Security Officer \(DSO\), IT Security Officer \(ITSO\), Information Asset Owners \(IAOs\), supported by the Lead Accreditor.

[REQUIREMENT 2](#requirement-1-and-requirement-2): The MoJ SIRO remains accountable for information risks, including risks to Protectively Marked and personal data, in an offshore context. These risks must be documented and presented to the SIRO, and must be explicitly agreed to before any contract with an offshore element is accepted. In some cases, a submission to the Cabinet Office IA Delivery Group may be necessary. The MoJ Accreditor, MoJ IT IA, DACU and Legal experts must be engaged by the project team as soon as a potential offshoring requirement is identified, to enable identification of these information risks. Close engagement with these Special Interest Groups must be maintained for the delivery lifetime. This engagement must be formally set out in the delivery plan.

The MoJ will bear the main impact of any compromise of the Confidentiality, Integrity and/or Availability of public services that are delivered or managed on its behalf.

The ultimate decision on whether the IA risk of outsourcing is acceptable will therefore be made by the SIRO, as advised by the IAO and the MoJ Accreditor. [HMG security policy](https://www.gov.uk/government/publications/security-policy-framework) requires that the SIRO must personal approve all large-scale information-related outsourcing and offshoring decisions. The SIRO is also required to approve the offshoring of personal data sets and, in some cases, submit plans for scrutiny by the Cabinet Office IA Delivery Group. The MoJ Accreditor, MoJ IA function and SIRO must be involved as soon as a potential offshoring proposal is identified, so that a decision on whether the proposal presents an acceptable level of information risk can be made at the earliest opportunity. This limits the likelihood of nugatory work by the project team.

The requirement for early and ongoing engagement with the MoJ Accreditor and MoJ IA function is reinforced by HMG GPG6 :

> The risk assessment and treatment plan must be reviewed by the Accreditor and presented to the SIRO at each stage of the procurement process.

### Risk Assessment

Before any sensible dialogue can be had around whether or not offshoring is acceptable, the value of the assets to be offshored and the threats for the offshore location and/or personnel must be properly understood. Asset valuation and threat assessment must therefore be conducted as an upfront activity for any proposal, and will require early engagement with all interested parties. Risk assessment must be conducted as an initial activity, and regularly revisited as the project progresses. All threat assessment and risk assessment activities will need to be conducted in collaboration between the supplier as risk manager, and the MoJ as the owner of the threat and the risk.

[REQUIREMENT 3](#requirement-3): All MoJ assets and/or activities to be offshored must be identified, and a Threat Assessment for those assets/activities at the proposed offshore location carried out. This includes not only physical and software assets but also information and service assets. The value and business impact of compromise for each information asset must be determined against the [HMG Business Impact Table and MoJ Business Impact guidelines](https://www.ncsc.gov.uk/guidance/technical-risk-assessment-and-risk-treatment-is1-2-supplement); valuations must be agreed with the Information Asset Owner for each asset. A Privacy Impact Assessment \(PIA\) is also required, as discussed further in [REQUIREMENT 5](#requirement-4-and-requirement-5) below.

The set of assets to be offshored not only includes any specific capabilities to be developed or managed, but will also include any incidental assets which are required to support these activities. For example:

-   Development will require test data and schemas which may in themselves attract a Protective Marking or have other particular sensitivities.

-   Some development activities may be deemed to require real or anonymised data, rather than fully synthetic test data, to ensure the robustness of critical applications or to test revised applications against historical data from extant capabilities.

    Wherever it is considered that there may be a requirement to use real or anonymised data, rather than synthetic data, the MoJ "Policy on the use of live personal data for the testing of IT systems, processes or procedures" must be complied with. For more information, see [this guidance](using-live-data-for-testing-purposes.md).

-   Effective application development may require knowledge of real configuration information to support pre-integration-testing activities, or of broader MoJ network infrastructure designs in order to tailor and optimise development. Some of this information may attract a Protective Marking or have other particular sensitivities. The information shared with offshore developers should be minimised to the fullest extent that is possible.

-   Poor coding practices often result in sensitive information such as network configuration information, user and administrator credentials, and other sensitive details being hard-coded into applications. Support for development, for third-line support and application maintenance, and for upgrades to MoJ IT capabilities may therefore necessitate some unavoidable access to sensitive information for which there is no specific need-to-know by the development or maintenance team.


[REQUIREMENT 4](#requirement-4-and-requirement-5): Sensitive MoJ assets and/or activities should not be offshored to Countries where Special Security Regulations Apply, or to Countries in which there is a Substantial Security Threat to British Interests.

It is the policy of the MoJ that Protectively Marked or otherwise sensitive MoJ assets, and development or support activities relating to these assets, should not be offshored to Countries where Special Security Regulations Apply, or to Countries in which there is a Substantial Security Threat to British Interests. The MoJ ITSO can provide further details of these, on a need-to-know basis, in response to specific requests. It is the policy of the MoJ that activities involving Protectively Marked or otherwise sensitive MoJ information should not be offshored to these locations. In cases where there is an exceptionally compelling business case for offshoring to one of these locations, the MoJ ITSO must be consulted and will advise the business on suitability, weighing up all of the relevant factors and assessing the extent to which the proposed compensating controls mitigate the risk.

[REQUIREMENT 5](#requirement-4-and-requirement-5): MoJ assets and/or activities should not be offshored to countries where political stability, practical considerations and/or legal issues \(e.g. compliance with the DPA\) may result in a significantly-above-baseline risk to the confidentiality, integrity and/or availability of Protectively Marked or other sensitive data, or where there is not an adequate level of protection for the rights of data subjects in relation to their personal data.

Not all countries which have issues with political and/or economic instability are listed as CSSRA or Substantial Security Threat countries. There are several other countries that are not on the list which nonetheless present a high risk for offshore development and operations. These countries should be avoided on the general principle of avoiding development environments where the local threat is significantly above baseline. Also, as discussed above, the CSSRA and the list of Substantial Security Threat countries change from time to time. By not offshoring in unstable locations, the risk of outsourcing to a country that subsequently ends up on one of these lists is reduced.

In addition to the above, there are some politically stable locations where it is nonetheless difficult or impossible to meet other essential requirements for the handling of Protectively Marked or other sensitive data \(e.g. personal data\). Inability to assure the identity and history of personnel, and local legislation on disclosure of data \(for example, in response to local FoI or law enforcement obligations\), are common examples which can lead to issues with screening and with retaining control of information.

In addition to countries with political and/or economic issues, as discussed above, there may also be threats and risks as a result of other nations' legal systems. Legal constraints in some countries may:

-   Conflict with IA requirements under the HMG SPF and supporting guidance;

-   Conflict with requirements under the Data Protection Act \(DPA\) and/or other UK Law; and

-   Expose the MoJ to untenable legal liabilities in the event that something goes wrong.


A particular consideration for offshoring is DPA Principle 8: "Personal data shall not be transferred to a country or territory outside the European Economic Area unless that country or territory ensures an adequate level of protection for the rights and freedoms of data subjects in relation to the processing of personal data."

Legal advice must be engaged, separately to IA advice, to identify any potential legal issues in advance of making any offshoring decision.

[REQUIREMENT 6](#requirement-6): An information risk assessment for each offshore location must be conducted by the Offshoring Company or organisation. This risk assessment must be subject to review and acceptance by MoJ IA. This should include an IS1 Risk Assessment, an assessment against ISO27001 controls, and a "Delta Assessment" setting out any HMG requirements that may be unenforceable, any variations to HMG policy that may be required, and how it is proposed to address these Deltas. A Privacy Impact Assessment \(PIA\), taking into account local legal considerations at the offshore location, must also be conducted. The risks, and the costs of mitigating the risks, must be balanced against the benefits to be gained from outsourcing. A Risk Management Plan must be developed and maintained to identify the mitigations required to address offshoring risks and estimate the costs of implementing these mitigations.

An information risk assessment for the offshore location must be conducted. This must include an IS1 Risk Assessment in line with current HMG guidance. It must also include an assessment of physical, procedural, personnel and technical measures at the offshore location set against the ISO27001 requirements and highlighting the additional controls in place to address the concerns set out within HMG Good Practice Guide 6 for specific ISO27001 controls. It must also include a "Delta Assessment" setting out any HMG requirements that may be unenforceable, any variations to HMG policy that may be required, and how it is proposed to address these deltas.

The high-level information risk assessment is required at the proposal stage, prior to contract negotiations. This must be developed incrementally into a more detailed risk assessment as the project progresses. This risk assessment must take into account all assets to be offshored and the specific Threat Assessment for the offshore location and/or personnel. The risk assessment must meet the requirements of both HMG IS1 and HMG GPG6. The requirements of HMG IS6 relating to personal data can be more difficult to meet in an offshore context, so particular care must be taken to ensure that the PIA takes the offshore location into account and offshore elements of the contract are compliant with IS6.

A Risk Management Plan is essential to address the risks identified through offshoring. As well as providing evidence that the supplier has adequately considered these risks, this will also provide the basis for estimating the cost overhead of mitigating offshoring risks, enabling a more accurate assessment of whether offshoring truly represents value for money. For example, the cost of provisioning a suitably segregated technical environment to support offshore development work; combined with the cost of providing a suitably secure link to enable remote access for offshore workers; and the cost of sending out suitably trained personnel for regular inspections of an overseas site; may significantly erode any cost savings.

### Supplier Arrangements

[REQUIREMENT 7](#requirement-7): IA constraints and requirements for offshoring must be made clear to suppliers prior to contract award and explicitly set out in contractual arrangements with suppliers to the MoJ. These constraints and requirements must be flowed down to all subcontractors along the chain of supply. Conversely, Intellectual Property Rights must flow up contractually from the offshore supplier or suppliers to the MoJ.

IA requirements must be determined as an integral part of the initial requirements for any capability, and an assessment of competing solutions against IA requirements must be a critical part of supplier selection during the tender process. Offshoring is no exception to this. Offshoring constraints and requirements must be made clear to suppliers prior to contract award, so that there can be no ambiguity during costing for any solution to be delivered to the MoJ. There will almost certainly be additional time, effort and cost involved to implement the required physical controls, testing and decommissioning activities required to meet IA requirements in an offshore development environment.

Some suppliers with UK bases may wish to offshore and/or subcontract elements of their contracts with the MoJ. If elements of a contract have been offshored to a subcontractor working in one location, that subcontractor may themselves wish to offshore elements of their subcontract to a different offshore location. IA constraints and requirements must be applicable to all of those who are party to the contract. For example, an offshore organisation based in Country A, which provides second-line support for an MoJ application from Country A, might rely on teams from its offices in Country B to conduct development and third-line support activities. This would have an impact on the Threat Assessment and hence the risks to the capability.

The MoJ is responsible for all offshore activities that are being conducted on its behalf, and must retain oversight of these activities. This requirement must be enforced within supplier contracts, through robustly worded requirements for contractual flow-down of IA responsibilities through the supplier chain. The MoJ must be given both visibility and an over-riding right of approval or veto for subcontractor arrangements. A right of audit without warning must be maintained by the MoJ, including full access to all physical sites, logical capabilities, accounting logs, etc.

Ownership of all information assets, and all Intellectual Property Rights, developed as part of MoJ contracts must flow up to the MoJ. All MoJ information, including vestidual information, which is held on a supplier's physical assets, must be erased and/or disposed of to the satisfaction of MoJ IT IA during decommissioning. Again, legal limitations on the enforceability of contractual conditions in some locations must be taken into account and specialist legal advice will be required to ensure that all necessary contractual conditions are enforceable at offshore development locations.

The above issues with contractual flow-down of responsibilities and flow-up of ownership are best managed if the MoJ retains control of the subcontract chain. Ideally, wherever practicable, MoJ supplier contracts should only allow further subcontracts to be let with the explicit permission of the MoJ. This enables the cost and complexity of due-diligence checking and contractual enforcement, not just for offshoring considerations but also more generally, to be more effectually bounded and controlled.

[REQUIREMENT 8](#requirement-8): Suppliers must ensure that offshore development is conducted according to UK and other relevant IA standards and legislation.

The requirements of the HMG SPF must be adhered to for offshore development. This may require significant changes to local working practices in some cases. The requirements of other relevant British and International standards must also be adhered to. Most notably for IA considerations, this specifically includes [ISO27001 \(Information Security Management System\)](https://www.iso.org/standard/42103.html) and [ISO25999 \(Business Continuity\)](https://en.wikipedia.org/wiki/BS_25999). Offshore sites and processes must be demonstrably compliant with ISO27001, and must be subject to a combination of scheduled and snap audits to ensure this. In addition to all of the usual ISO27001 conditions, particular considerations for offshore development are set out within HMG GPG6. Any issues found during audit must be addressed over timescales that are agreeable to MoJ IT IA, with formal progress tracking of issues as they are addressed and resolved. Business Continuity can introduce particular issues in some offshore contexts, where events such as natural disasters, pandemics, criminal activity, acts of war, etc. may be sufficiently probable to merit more rigorous mitigations than for UK development. Factors such as staff turnover may also present particular issues in an offshore context, particularly where Landed Resources are used.

[REQUIREMENT 9](#requirement-9-and-requirement-10): The robustness of development and integration testing activities must be reconfirmed. Regular development and integration testing activities by the System Integrator are particularly essential for offshoring, where there will potentially be less visibility or direct control over the development environment. Additional code review must also be conducted to a level that is agreed by MoJ IT IA to be commensurate with the value of the information that will be handled by the live application, or otherwise accessible to the live application.

[REQUIREMENT 10](#requirement-9-and-requirement-10): Security Enforcing Functionality elements of MoJ applications must not be offshored. For other elements of application code which process, store and transmit sensitive MoJ information assets, an onshore security code review must be conducted. This should be to a level that is agreed by MoJ IT IA to be commensurate with the value of the information handled by the live application, or otherwise accessible to the live application. This is likely to include a combination of manual and automated testing, and should be supplemented by a more comprehensive ITHC scope where appropriate.

The basic principle of ensuring thorough testing during every stage of application development must be reinforced where elements of development and/or maintenance are to be offshored. Requirements for testing against internationally recognised standards \(e.g. the [OWASP standard for secure code development](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/migrated_content)\) must be secured in supplier contracts and flowed down to offshore and other subcontractors. A test data strategy must be agreed prior to contract award. A high-level test strategy must also be agreed prior to contract award, and should be developed and maintained as a living plan as the project evolves. There should be assurance that provision for testing is adequate to mitigate the Information Assurance and other System Integration risks identified.

Testing, including security testing, must be conducted at every stage of the development \(unit testing, integration testing, acceptance testing, etc\). The MoJ must retain executive control over the testing process, maintaining visibility of all test results and progress on remedial activities. This includes control by MoJ IT IA over security elements of testing. The MoJ must be contractually able to exert control over testing, through clauses to reject as substandard any delivery where test scopes are not agreed by the MoJ, where results are not fully disclosed or where remedial activities are deemed to be insufficient.

Some applications which are deemed to be relatively low value in themselves may be used to handle information with a significantly higher value, or may be able to easily access sensitive information \(for example, other information within the same business domain or information that is directly accessible from connections to servers in other business domains\). Additional code review must also be conducted as part of the development testing of these applications, with particular emphasis on Security Enforcing elements of the application. In some cases, the MoJ Accreditor and the IA Team may require the use of automated test tools and/or line-by-line code review for elements of the application to be conducted by UK Security Cleared personnel at onshore locations.

In some cases, the additional testing overhead required will outweigh the benefits gained by offshoring. This is most likely for particularly complex and/or sensitive applications. Back-doors and vulnerabilities become increasingly easy to engineer \(either deliberately or accidentally\) for complex applications, and increasingly difficult to identify. Based on experience, it is likely that suppliers will underestimate the true time and expense that would be necessary to test complex applications. It is important that supplier proposals are realistic about the benefits of any offshoring elements of the proposals, and have accommodated realistic costs for testing to address offshoring risks. Where test costs are not realistic, this does not represent a cost saving for the MoJ. If the supplier is not making an acceptable profit on a contract, then relationships between the supplier and the MoJ will undoubtedly deteriorate. The supplier is likely to try to recoup losses by streamlining test processes \(driving operational risk\); by reclaiming costs from elsewhere \(driving project cost\); or by delivering below expectations or not at all \(driving project risk\). Such unrealistic proposals should be either corrected or rejected during supplier selection and contract award.

### Use of Landed Resources

[REQUIREMENT 11](#requirement-11): Where landed resources are used to support project activities they must be vetted to a level appropriate for the value of the information assets and collateral assets that will potentially be available to them. Where it is not possible to meet some BPSS evidence requirements, suitable alternative evidence must be obtained and compensating controls such as technical lockdown, supervision and monitoring must be applied. If it is not possible to lock down the physical environment to the satisfaction of MoJ IT IA then landed resources must not be used. For higher levels of clearance such as SC, if a landed resource cannot achieve the required level of clearance or if there are prohibitive conditions on the individual's clearance, then that landed resource must not be used.

The most basic level of Government security checking, the [Baseline Personnel Security Standard \(BPSS\) check](https://www.gov.uk/government/publications/government-baseline-personnel-security-standard), is designed to provide an assessment of three key features of the individual to be vetted: their identity; their right to work; and the reliability, integrity and honesty of those individuals.

The BPSS requires that an individual's identity be confirmed, by matching some evidence of identity such as a passport or drivers licence, with evidence of address and activity in the community such as bills and bank statements. This provides a level of information that can be followed up for UK applicants if an individual raises any particular concerns. Further checks can be cheaply and easily conducted, to provide additional evidence that an individual with the asserted identity and address exists, and to confirm that the individual asserting that identity and address is not attempting identity theft. Where individuals originate from outside of the UK, and have not been in the UK for a suitably long period of time, it can be more difficult to obtain a suitably reliable history for those individuals \(long-term footprint\) to support effective screening. The Baseline Standard requires at least three years’ worth of previous employment history. From experience, it is considered that a commensurate length of time is also required to build up a suitably rich credit history and social footprint to enable reliable checks to be conducted.

Even confirming an individual's true identity may be problematic in some non-EU locations, where proofs of identity may be non-existent or considerably less reliable. It should also be noted that, for countries where record-keeping is managed locally rather than centrally, engagement at a local level to support checks can very quickly become prohibitively expensive for a moderately-sized workforce and/or where there is a high rate of staff turnover.

Personal and employers' references are used, partly to support confirmation of identity, and partly to enable checking of an individual's reliability, integrity and honesty. Criminal records declarations and supporting criminal records checks are also used as part of BPSS clearance. Criminal record checks for UK citizens are generally comprehensive and accurate. However, the accuracy of police and criminal records checks varies widely between different countries. The CPNI has compiled [information on such checks for a reasonably broad set of overseas jurisdictions](https://www.cpni.gov.uk/search?query=criminal%20record%20check%20overseas). The CPNI documentation also provides useful information on the reliability of identify checks overseas. A risk-balance decision by the SIRO is likely to be required on whether to accept the additional BPSS vetting risk for the offshore workforce.

To compensate for any shortcomings or uncertainty in vetting, landed resources brought to the UK are likely to require a heightened level of monitoring and supervision, as well as additional technical measures to limit and audit their physical and logical access to HMG information systems. HMG information systems to which landed resources have access must be locked down and supported by tight access controls over-and-above the usual HMG baseline.

Where higher levels of clearance such as SC are required it may not be possible for a specific landed resource to achieve the required level of clearance, or there may be prohibitive conditions on the individual's clearance. In those cases, the specific landed resource must not be used. For example, a non-UK National who has been within the UK for a sufficiently long period of time may be able to obtain an SC clearance. However, if a role requires handling of UK Eyes Only material, then the prohibitions on the SC clearance for that non-UK national would make them inappropriate to use for that role.

In exceptional circumstances, the use of landed resources from countries where Special Security Regulations Apply, or to countries in which there is a Substantial Security Threat to British Interests, depending on why that specific country is on the list. The MoJ ITSO should be consulted in such cases and will advise the business on suitability, weighing up all of the relevant factors and assessing the extent to which the proposed compensating controls mitigate the risk.

## Assessment Activities

Every offshoring decision must be made on a case-by-case basis, after balancing all of the facts of the situation. The project activities required to ensure this are set out below.

### REQUIREMENT 1 and REQUIREMENT 2

#### Project Scoping & Supplier Selection

MoJ Project Team:

-   Ensure that the MoJ SIRO, MoJ Accreditor, MoJ IT IA and MoJ Central IA are engaged from project conception.

-   Ensure that any contracts which may require personal data to be offshored outside of the EEA include suitable contractual clauses developed from reliable templates. For example, for personal data transferred outside of the EEA, the European Commission [approved model clauses](http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=OJ:L:2002:006:0052:0062:EN:PDF) as per Directive 95/46/EC of the European Parliament and of the Council, provides a useful template. The legal framework for managing the export of Protectively Marked information must be no less restrictive than this. Consider whether additional contractual clauses are required to mitigate risk and avoid legal problems arising from local laws and jurisdictional issues.

-   Ensure that offshoring elements of all Invitation To Tender \(ITT\) or other supplier requirements documentation are developed in consultation with MoJ Legal functions, DACU, and the MoJ Accreditor and MoJ IT IA. Ensure that these parties are key reviewers for all tender requirements.

-   On the advice of the Accreditor, DACU, MoJ IT IA, and MoJ Central IA, present and obtain approval for a SIRO Submission comprehensively setting out the risks and mitigations of any offshoring proposals.

-   Understand and advise the SIRO of any requirement that may exist for a submission to the Cabinet Office IA Delivery Group. Prepare any required submission on behalf of the SIRO, for approval.

-   Ensure that the operational assessment and investment appraisal of competing supplier proposals factors in the additional MoJ IT IA effort requirement to address offshore elements of the proposal, as per [Requirement 11](#requirement-11) below.

-   Reject any bids that do not meet IA, DACU or Legal requirements for offshoring.


MoJ Accreditor/IA:

-   Develop the elements of tender requirements which cover offshoring constraints and requirements.

-   Review outsourcing elements of supplier bids and other proposals.

-   Advise the MoJ Project Team on the suitability of offshoring proposals.


**Note:** MoJ IA includes both MoJ IT IA and the MoJ Central IA team. Both IA functions should be kept informed and engaged about offshoring proposals.

#### Contract Award

MoJ Project Team:

-   Ensure that offshoring requirements and constraints are worked up to a robust level of detail within the final supplier contract, and subject to a further round of review by the MoJ Accreditor and MoJ IT IA prior to acceptance and contract award.

-   Update any SIRO Submissions and submissions to the Cabinet Office IA Delivery Group to reflect the changes in the information risk between project scoping and contract award. Obtain acceptance for any changes from the SIRO prior to acceptance and contract award. Engage MoJ IT IA to advise and liaise with the SIRO.


MoJ Accreditor/IA:

-   Provide review support and remedial input to the MoJ Project Team.


#### Development

MoJ Project Team:

-   Use supplier audit as a mechanism to ensure that contractual requirements are being met. Where supplier indiscretions are found enforce remedial action.

-   Where remedial action is not implemented, or ineffectually implemented, invoke contractual penalty clauses.

-   Add and maintain any submissions to the SIRO and the Cabinet Office IA Delivery Group as necessary. Engage MoJ IT IA to advise and liaise with the SIRO.


MoJ Accreditor/IA:

-   Provide review support, remedial input and recommendations to the MoJ Project Team.


#### In-Service & Beyond

MoJ Service Management:

-   Use supplier audit as a mechanism to ensure that contractual requirements are being met. Where supplier indiscretions are found enforce remedial action.

-   Where remedial action is not implemented, or ineffectually implemented, invoke contractual penalty clauses.

-   Add and maintain any submissions to the SIRO and the Cabinet Office IA Delivery Group as necessary. Engage MoJ IT IA to advise and liaise with the SIRO.


MoJ Accreditor/IA:

-   Provide review support, remedial input and recommendations to the MoJ Project Team.


### REQUIREMENT 3

#### Project Scoping & Supplier Selection

Supplier:

-   Identify what hardware, software and information assets need to be offshored.

-   Set out asset valuations for the Confidentiality, Integrity and Availability of all assets. Core information assets must be valued according to the SAL and clarification sought for any ambiguities. Collateral information assets \(crypto, credentials, etc\) must be valued in line with MoJ and HMG guidance.

-   Asset valuations for all hardware and software assets must be clearly justified in the proposal documentation, and submitted to the MoJ Accreditor for review.


MoJ Project Team:

-   Ensure that supplier proposals include unambiguous asset valuations. Request clarification on any points of ambiguity. Ensure that the Information Asset Owner\(s\), the Accreditor and MoJ IT IA are engaged on an on-going basis.

-   Reject any proposals that do not meet with Requirement 3.


MoJ Accreditor/IA:

-   Ensure that a clear and detailed SAL is generated on a per-project basis, setting out the valuations for all information assets.

-   Review hardware, software and asset valuations on supplier proposals.


#### Contract Award

MoJ Project Team:

-   Ensure that the supplier contract includes an explicit requirement to develop and maintain hardware, software and information asset registers. The requirement should explicitly stipulate that registers be maintained in the MoJ standard format, or in an equivalent format which contains \(as a minimum\) all of the information in the MoJ standard format. Ensure that the supplier is supplied with a copy of this standard format in advance of contract award, so that they can take any additional overheads into account in their proposal.

-   Ensure that the supplier contract includes a right of audit, including no-notice audit, by the MoJ. The scope of audit must encompass hardware and software asset registers, all hardware and software assets, and all other elements related to the provision \(physical sites, personnel, etc.\)


MoJ Service Management:

-   Maintain a MoJ standard format for hardware and software asset registers.


#### Development

Supplier:

-   Develop and maintain hardware, software and information asset registers, covering all hardware, software and information assets. This must be developed in the MoJ standard format, or in an equivalent format which contains \(as a minimum\) all of the information in the MoJ standard format.


MoJ Project Team:

-   Maintain visibility of the hardware, software and information asset registers. Ensure that there is a regular joint \(supplier/MoJ\) activity to audit physical and software assets against these registers. Conduct irregular spot audits of assets against the registers. Ensure that remedial activity is time-lined, tracked and completed according to schedule by the supplier.


MoJ Accreditor/IA:

-   Advise physical and logical audit of assets, and remedial activity.


#### In-Service & Beyond

Supplier:

-   Ensure that the hardware, software and information asset registers are maintained as part of an ITIL service wrap for the delivered service. This must be maintained in the MoJ standard format, or in an equivalent format which contains \(as a minimum\) all of the information in the MoJ standard format.


MoJ Service Management:

-   Maintain visibility of the hardware, software and information asset registers. Ensure that there is a regular joint \(supplier/MoJ\) activity to audit physical and software assets against these registers. Conduct irregular spot audits of assets against the registers. Ensure that remedial activity is time-lined, tracked and completed according to schedule by the supplier.


MoJ Accreditor/IA:

-   Advise physical and logical audit of assets, and remedial activity.


### REQUIREMENT 4 and REQUIREMENT 5

#### Project Scoping & Supplier Selection

Supplier:

-   Ensure that any potential requirements to offshore any elements of service delivery are explicitly communicated with the MoJ as part of the tender response.


MoJ Project Team:

-   Ensure that suppliers are explicit about any proposals for offshoring any elements of the delivery when they develop their bids to supply a capability.

-   Ensure that the Accreditor, the IA Team, DACU and MoJ Legal advisors are aware of any potential requirements to offshore elements of the delivery.

-   Work with the Accreditor and MoJ IT IA to identify and resolve any potential IA issues for work at these offshore locations or involving personnel from these locations.

-   Work with DACU to identify and resolve any potential DPA issues for work at these offshore locations or involving personnel from these locations.

-   Obtain confirmation from MoJ Legal Advisors that work at these offshore locations or involving personnel from these locations will not cause any potential conflict with UK Law or leave the MoJ exposed to any additional legal liability.

-   Reject any proposals that do not meet with Requirement 4 or Requirement 5.


MoJ Accreditor/IA

-   Advise the project team on any potential offshoring problems and unacceptable offshoring proposals, and recommend mitigation options where necessary.


#### Contract Award

MoJ Project Team:

-   Ensure that the supplier contract explicitly prohibits offshoring except where locations and controls are explicitly set out within the contract.

-   Ensure that the contract prohibits offshoring to CSSRA and Substantial Security Threat countries, and any other identified problem countries, and that the contract contains flow-down provisions of all offshoring constraints for all subcontracts.

-   Ensure that the supplier contract includes a requirement to consult the MoJ before offshoring any elements of the delivery except where explicitly set out in the contract.

-   Ensure that the Accreditor and MoJ IT IA are critical reviewers for all supplier contracts with an offshoring requirement.


MoJ Accreditor/IA:

-   Advise the MoJ Project team on what countries are currently on the lists, and advise on exceptions on a case-by-case basis.

-   Review offshoring elements of supplier contracts.


#### Development

Supplier:

-   Ensure that any potential emerging requirement to offshore any elements of delivery are communicated immediately to the MoJ.


MoJ Project Team:

-   Deal with any emerging requirements on a case-by-case basis, through engagement with the Accreditor, the IA Team, DACU and MoJ Legal advisors, and Information Asset Owners.


#### In-Service & Beyond

Supplier:

-   Ensure that any potential emerging requirement to offshore any elements of delivery are communicated immediately to the MoJ.


MoJ Service Management:

-   Deal with any emerging requirements on a case-by-case basis, through engagement with the Accreditor, the IA Team, DACU and MoJ Legal advisors, and Information Asset Owners.


### REQUIREMENT 6

#### Project Scoping & Supplier Selection

Supplier:

-   Conduct an initial IS1 Risk Assessment, In line with the MoJ-provided threat assessment, which includes offshoring risks. This must include an HMG GPG6 compliance assessment, highlighting specific low-level risks due to any offshoring proposals, as part of the overall proposal to supply a capability.

-   Develop a specific Risk Management Plan to address offshoring threats and risks, detailing how these identified will be mitigated. The Risk Management Plan must provide an estimate of the costs required to implement the proposed mitigations, and any consequent issues that may arise.

-   Conduct a Privacy Impact Assessment \(PIA\) for the proposed solution, including an assessment of the PIA requirements covering the elements of information to be outsourced and documenting how the proposals meet these requirements.


MoJ Project Team:

-   Ensure that suppliers are aware of the requirement to include an IS1 Risk Assessment, HMG GPG6 compliance, and supporting low-level risk assessment.

-   Reject any proposals that do not contain a PIA, or which contain a PIA that is deemed by DACU, the MoJ Accreditor, or MoJ IT IA to be inadequate.

-   Reject any proposals that do not contain a risk assessment, or which contain a risk assessment that is deemed by the MoJ Accreditor and MoJ IT IA to be inadequate.

-   Reject any proposals where the mitigations proposed in the Risk Management Plan are deemed by the MoJ Accreditor and MoJ IT IA to be inadequate, or the costs of implementing those mitigations are deemed by the MoJ Security Architecture Team to be unrealistic.


MoJ Accreditor/IA

-   Develop bespoke threat assessments and advice for any proposed offshore locations and for use of non-UK personnel for development. Engage with the UK Security Authorities as necessary to support this.

-   Review Risk Assessment elements of supplier proposals.


#### Contract Award

MoJ Project Team:

-   Ensure that the supplier contract includes terms requiring the supplier to update the Risk Assessment and Risk Management Plan, including offshoring considerations, immediately following contract award and maintain this as a through-life activity. As a minimum, the supplier should be required to update the risk assessment \(and have this approved by the MoJ\) for any contract change and as part of the acceptance criteria for each distinct phase of the development.

-   Ensure that the Accreditor and MoJ IT IA are critical reviewers for all supplier contracts with an offshoring requirement.

-   Ensure that the outcomes of the PIA are folded into the supplier contract.

-   Ensure that the project budget includes a suitable level of contingency to accommodate any changes in offshoring costs due to change in Threat Assessment for the offshore environment.


MoJ Accreditor/IA:

-   Review offshoring elements of supplier contracts, including the terms and conditions surrounding risk assessment.


#### Development

Supplier:

-   Maintain the risk assessment, including offshoring considerations, in line with contractual requirements.

-   Ensure that offshoring arrangements do not break obligations arising from the PIA.

-   Maintain the Risk Management Plan, including offshoring considerations, in line with contractual requirements.


MoJ Project Team:

-   Ensure that suppliers meet their contractual obligations regarding risk assessment and PIA.


MoJ Accreditor/IA

-   Provide support for any required review of the supplier risk assessment, including offshoring considerations, in line with contractual requirements.


#### In-Service & Beyond

Supplier:

-   Maintain the risk assessment, including offshoring considerations, in line with contractual requirements.

-   Ensure that offshoring arrangements do not break obligations arising from the PIA.

-   Maintain the Risk Management Plan, including offshoring considerations, in line with contractual requirements.


MoJ Service Management:

-   Ensure that suppliers meet their contractual obligations regarding risk assessment and PIA.


MoJ Accreditor/IA

-   Provide support for any required review of the supplier risk assessment, including offshoring considerations, in line with contractual requirements.


### REQUIREMENT 7

#### Project Scoping & Supplier Selection

Supplier:

-   Identify any potential offshoring requirement as soon as possible in the tender process. Where proposals include an element of offshoring, it must be explicitly stated in the supplier’s response to the security requirements. This must explicitly state how security will be maintained in an offshore context \(including responses to User Security Requirements, System Security Requirements, etc.\)


MoJ Project Team:

-   Ensure that supplier proposals to deliver a capability are demonstrably compliant with offshoring security requirements.

-   Reject any proposals that the MoJ Accreditor and MoJ IT IA deem to either not address security requirements comprehensively enough or not give sufficient weighting to these requirements.


MoJ Accreditor/IA:

-   Engage with the MoJ Project Team and the supplier to support development and assessment of MoJ security requirements, including offshoring requirements, for the capability.


#### Contract Award

MoJ Project Team:

-   Ensure that the supplier contract specifically mandates compliance with all offshoring security requirements.

-   Ensure that the supplier contract mandates blanket flow-down of all contractual constraints and obligations to all of the suppliers’ suppliers, all of the way down the supply chain.

-   Ensure that the contract makes provision for routine and no-notice audit of supplier compliance with offshoring requirements, at any-and-all supplier locations and subcontractor locations that are relevant to the work.


MoJ Accreditor/IA

-   Support the MoJ Project Team in the development of contractual requirements around offshoring. Review contractual clauses relating to offshoring.


#### Development

Supplier:

-   Inform the MoJ upfront if any emerging requirements develop to offshore elements of the solution. Demonstrate how these requirements will be compliant with contractual obligations, and highlight and contractual obligations that would need to be relaxed in order for the proposal to work, balancing this against the potential benefit and considering a range of practicable options \(as determined through engagement with the MoJ Project Team, the MoJ Accreditor and MoJ IT IA. Work with MoJ to ensure that this can be managed in a secure way.


MoJ Project Team:

-   Retain engagement with the MoJ Accreditor and MoJ IT IA for all aspects of the project development relating to offshoring.


MoJ Accreditor/IA:

-   Provide support to the MoJ Project Team on offshoring, including direction for audit, remediation and emerging requirements as necessary.


#### In-Service & Beyond

Supplier:

-   Inform the MoJ upfront if any emerging requirements develop to offshore elements of the solution. Demonstrate how these requirements will be compliant with contractual obligations, and highlight and contractual obligations that would need to be relaxed in order for the proposal to work, balancing this against the potential benefit and considering a range of practicable options \(as determined through engagement with the MoJ Project Team, the MoJ Accreditor and MoJ IT IA. Work with MoJ to ensure that this can be managed in a secure way.


MoJ Service Management:

-   Retain engagement with the MoJ Accreditor and MoJ IT IA for all aspects of ongoing development \(e.g. third-line support\) relating to offshoring.


MoJ Accreditor/IA:

-   Provide support to the MoJ Project Team on offshoring, including direction for audit, remediation and emerging requirements as necessary.


### REQUIREMENT 8

#### Project Scoping & Supplier Selection

Supplier:

-   Ensure that proposals include an explicit assessment of compliance \(including any points of non-compliance\) of offshoring elements of proposals with relevant Legislation and Standards. This includes: the DPA and other relevant legislation; the HMG SPF and supporting documentation \(specifically, but not exclusively, HMG IS6, HMG GPG6 and the SPF MRs themselves\); relevant ISO standards \(most notably [ISO27001](https://www.iso.org/standard/42103.html) and [ISO25999](https://shop.bsigroup.com/en/ProductDetail/?pid=000000000030157563) \); Cabinet Office Guidance on IT Offshoring; and local MoJ IA Requirements.

-   Ensure that named CLAS Consultant resources are used on the supplier proposal to ensure that this proposal addresses all relevant HMG IA requirements and documentation \(including offshoring requirements\), and is compliant with these.


MoJ Project Team:

-   Ensure that MoJ IA Requirements are made available to suppliers, and that they are aware of their obligations to explicitly demonstrate compliance with offshore elements of their proposals against these.


MoJ Accreditor/IA:

-   Engage with the MoJ Project Team and Supplier security resource to review supplier bids for compliance with HMG IA requirements and documentation \(including offshoring requirements\).


#### Contract Award

MoJ Project Team:

-   Ensure explicit supplier compliance with all relevant identified legislation and standards \(as per the list set out in the previous column, plus any other relevant standards identified during the tender process\) are set out in the contract.

-   Ensure IA are engaged in the procurement process, and that IA concerns relating to offshoring elements of the contract are addressed to the satisfaction of the Accreditor prior to awarding the contract.


MoJ Procurement:

-   Support the MoJ Project Team in the development of contractual requirements around offshoring. Review contractual clauses relating to offshoring.

-   Ensure IA are engaged in the procurement process, and that IA concerns relating to offshoring elements of the contract are addressed to the satisfaction of the Accreditor prior to awarding the contract.


#### Development

All:

-   As per [Requirement 7](#requirement-7), above.


#### In-Service & Beyond

All:

-   As per [Requirement 7](#requirement-7), above.


### REQUIREMENT 9 and REQUIREMENT 10

#### Project Scoping & Supplier Selection

Supplier:

-   Ensure that the proposal includes provision for through-development testing, including security testing. Demonstrable compliance with the OWASP Testing Guide \([downloadable from the OWASP web-site](https://owasp.org/www-project-web-security-testing-guide/)\) is encouraged. The level of security testing required must be agreed with the Accreditor, and will need to be directly commensurate with the risk involved.


MoJ Project Team:

-   Ensure that suppliers are aware of the requirement for testing, including not only functional testing but also security testing. Reject any proposals that do not make provision for this.

-   Ensure that supplier proposals are realistic about the benefits of any offshoring elements of the proposals, and have accommodated realistic project costs and timescales for testing to address offshoring risks. Conduct an internal sanity check of supplier estimates for security and other testing. Reject any proposals where cost or time estimates are unrealistic.


MoJ Accreditor/IA:

-   Support assessment of functional and security testing proposals.


#### Contract Award

MoJ Project Team:

-   Ensure that the contract requires the supplier to test the solution against internationally recognised standards at all stages of the development \(unit testing, integration testing, acceptance testing, etc\). Suppliers must be contractually required to agree test scopes, including security test scopes, with the MoJ before the start of testing. The MoJ must be contractually entitled to visibility of all test results and progress on remedial activities to the MoJ. Ensure that the scope of testing in the contract includes security testing of the solution, at a level agreed with the Accreditor and the IA Team.

-   Ensure that the contract retains executive control over the test process by the MoJ, with the ability to reject substandard delivery, require remediation and enforce contractual penalty clauses.


MoJ Accreditor/IA:

-   Review offshoring elements of supplier contracts, including test arrangements. Provide input to the Project Team as required to support contractual terms for test, particularly security elements of testing.


#### Development

Supplier:

-   Maintain a regular forum with the MoJ Project Team to discuss progress against test requirements and milestones, exceptions and remedial planning.


MoJ Project Team:

-   Ensure that the Accreditor and MoJ IT IA are involved in test forum\(s\) during development. Proactively track progress of remedial action against test defects.


MoJ Accreditor/IA:

-   Support test review and remedial activities.


#### In-Service & Beyond

Supplier:

-   Maintain a regular forum with the MoJ Project Team to discuss progress against test requirements and milestones, exceptions and remedial planning.


MoJ Service Management:

-   Ensure that the Accreditor and MoJ IT IA are involved in test forum\(s\) during development. Proactively track progress of remedial action against test defects.


MoJ Accreditor/IA:

-   Support test review and remedial activities.


### REQUIREMENT 11

#### Project Scoping & Supplier Selection

Supplier:

-   Ensure that any proposal to use landed resources is clearly stated. Ensure that any associated costs and risks are identified.

-   Where landed resources are to be used, ensure that the proposal clearly sets out what information assets and collateral assets would be made available to those resources, how many landed resources are proposed, from where, what level of clearance would be required, and how clearance information requirements would be satisfied.

-   Where clearance is not possible to an equivalent level for a landed resource as for a UK resource, identify what the additional residual risks of this will be, how it is proposed to mitigate these risks. The proposal should identify any practical difficulties with these arrangements and how they will be overcome, as well as setting out the additional costs involved.


MoJ Project Team:

-   In liaison with the MoJ Accreditor and MoJ IT IA, ensure that proposals for using Landed Resources are realistic.

-   Ensure that the costs associated with the use of landed resources have been fully considered in the proposal.

-   Reject any unrealistic or un-costed proposals for use of Landed Resources.


MoJ Accreditor/IA

-   Support assessment of security risk and residual risk with supplier proposals to use landed resources.

-   Advise on the feasibility of using landed resources from high-threat countries if relevant.


#### Contract Award

Supplier:

-   Ensure that use of landed resources is in line with contractual requirements.


MoJ Project Team:

-   Ensure that the supplier contract includes provision to enforce suitable security controls surrounding landed resources, as agreed during supplier selection.

-   Ensure that the project budget includes a suitable level of contingency to accommodate any changes in offshoring costs due to change in Threat Assessment for landed resources.


MoJ Accreditor/IA:

-   Review offshoring elements of supplier contracts.


#### Development

Supplier:

-   Ensure that all landed resources are vetted to a level commensurate with the value of the information to be handled by that landed resource. Where it is not possible to effectively vet a landed resource to the required level, landed resources must not be used.

-   Inform the MoJ immediately if resource requirements change.


MoJ Project Team:

-   Ensure that the MoJ Accreditor and MoJ IT IA are kept fully informed of any change in supplier requirements, and that no change in Landed Resource requirements is agreed without the explicit approval of the IA Team.

-   Ensure that the supplier is kept fully informed of any change in Threat Assessment relating to landed resources and of the impact on project delivery.


MoJ Accreditor/IA

-   Ensure that the MoJ Project Team are made aware of any change in Threat Assessment relating to Landed Resources, and of how this will impact the project.


#### In-Service & Beyond

Supplier:

-   Ensure that all landed resources are vetted to a level commensurate with the value of the information to be handled by that landed resource. Where it is not possible to effectively vet a landed resource to the required level, landed resources must not be used.

-   Inform the MoJ immediately if resource requirements change.


MoJ Service Management:

-   Ensure that the MoJ Accreditor and MoJ IT IA are kept fully informed of any change in supplier requirements, and that no change in landed resource requirements is agreed without the explicit approval of the IA Team.

-   Ensure that the supplier is kept fully informed of any change in Threat Assessment relating to landed resources and of the impact on project delivery.


## Further Reading

|Title|Version / Issue|
|-----|---------------|
|[CPNI Personnel Security in Offshore Centres](https://www.cpni.gov.uk/system/files/documents/f4/75/personnel-security-in-offshore-centres-guidance.pdf)|04/2009|
|CPNI Good Practice Guide: Outsourcing: Security Governance Framework for IT Managed Service Provision|02/08/2006|
|CESG Good Practice Guide 16: Taking and Using Cryptographic Items Overseas|Issue 1.0, 08/2009|
|CESG Good Practice Guide 23: Assessing the Threat of Technical Attack Against IT Systems|Issue 1.0, 04/2010|

## Notes

[http://www.owasp.org](http://www.owasp.org)

Wherever it is considered that there may be a requirement to use real or anonymised data, rather than synthetic data, the MoJ "Policy on the use of live personal data for the testing of IT systems, processes or procedures" must be complied with. For more information, see [this guidance](using-live-data-for-testing-purposes.md).

A particular consideration for offshoring is DPA Principle 8: "Personal data shall not be transferred to a country or territory outside the European Economic Area unless that country or territory ensures an adequate level of protection for the rights and freedoms of data subjects in relation to the processing of personal data."

For example, an offshore organisation based in Country A, which provides second-line support for an MoJ application from Country A, might rely on teams from its offices in Country B to conduct development and third-line support activities. This would have an impact on the Threat Assessment and hence the risks to the capability.

The Baseline Standard requires at least three years’ worth of previous employment history. From experience, it is considered that a commensurate length of time is also required to build up a suitably rich credit history and social footprint to enable reliable checks to be conducted.

[http://www.cpni.gov.uk/advice/personnel-security1/overseas-criminal-record-checks/](http://www.cpni.gov.uk/advice/personnel-security1/overseas-criminal-record-checks/)

For example, for personal data transferred outside of the EEA the European Commission approved model clauses as per Directive 95/46/EC of the European Parliament and of the Council, provides a useful template. This can be found at [http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=OJ:L:2002:006:0052:0062:EN:PDF](http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=OJ:L:2002:006:0052:0062:EN:PDF). The legal framework for managing the export of Protectively Marked information must be no less restrictive than this.

MoJ IA includes both MoJ IT IA and the MoJ Central IA team. Both IA functions should be kept informed and engaged about offshoring proposals.

The additional costs for offshore proposals will include potentially significant additional costs for IA and Accreditor resources to support bid assessment, solution review, initial Accreditation, re-accreditation and through-life support. An increased requirement for IA engagement and design scrutiny will be inevitable, and would need to be determined by IA. Activities such as audit and remediation are likely to involve an increased time overhead and travel expenses \(e.g. for physical site visits to remote sites at overseas locations to conduct audits and follow-up remediation\). Other additional project and in-service assurance is almost certain to be necessary.

