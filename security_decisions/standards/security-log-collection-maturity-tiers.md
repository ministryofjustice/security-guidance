---
category: Security Log Collection
expires: 2020-03-01
---

# Security Log Collection Maturity Tiers

MOJ systems and services must adequately create and retain event data as part of the [DETECT](https://ministryofjustice.github.io/security-guidance/principles/identify-protect-detect-respond-recover/#detect) portion of the [Cabinet Office's Minimum Cyber Security Standard (MCSS)](https://www.gov.uk/government/publications/the-minimum-cyber-security-standard).

Three tiers have been developed to reflect the breadth and complexity of collecting and forwarding log data.

These three tiers represent different levels of risk profile, and concern about a system.  All systems should be capable of meeting the baseline standard, but there are systems that are at greater likelihood of compromise due to factors such as age or public threats, or systems which would have a significantly elevated impact if compromised due to sensitivity or perceived value.  These systems should aim to be monitored to a higher standard.

Each tier is additive to the ones below it, so a system that operates at the Enhanced tier should also meet the requirements at the Baseline tier.

![](../../../images/Tiers.png)

## Baseline

The baseline is the generally minimum expected of event types that should be generated and forwarded for onward analysis from all of the MoJ systems and may also generally be met through the underlying platform(s) on which they are built.

This tier covers the broad spectrum of events that can reasonably be used to detect compromise and allow the defensive cyber team to respond appropriately before significant impact.

## Enhanced

Enhanced event types, in addition to the baseline event types, provide earlier notification of attempted compromise as well as gathering more information to detect stealthier attackers or significantly more capable attackers.

## Bespoke

Some systems are critical to the security, stability and statutory function of the MoJ and/or contain highly sensitive data. In these cases, systems must generate additional bespoke event types as agreed in context directly between the MOJ Cyber Security team and the associated product/service team, working in cohort to identify key nuance and contextual security monitoring requirements based on applicable threats and risks.
