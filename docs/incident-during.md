# During a security incident

This document forms part of the incident management plan. 

## Starting an incident
Anyone from across the MoJ can begin this incident process - whenever they believe a data incident is likely, is happening, or has happened. 

This process is not absolute - different circumstances will require the incident manager to take alterative steps depending on what has happened and what is going in - but provides a framework of steps that are likely to be needed. These are also not absolutely sequential - for example, notifying the regulators can and should occur in parallel to other steps; likewise with briefings to SIROs or other stakeholders. 

## What should I do?
- If it is possible for you, as the incident discoverer, to do so, take immediate action to stop any on-going data breach / attack that is in progress, and close off the route by which the attack / breach is being caused by. 
- Immediately start an incident by contacting the Security Team.
- If possible, stay available to discuss what you have done with the Incident Manager so they can understand the situation, the actions you've taken, and the circumstances surrounding the incident. 


## Initial Incident Triage
The on-call Incident Manager will perform an initial triage on a report from the incident discoverer. It is the Incident Manager's role to sound the alarm if they believe it warrants mobilisation of formal incident response. 

The initial purpose of the triage stage is to ascertain if the security event that has been detected warrants being treated as a security incident, or is a false positive.

All security events should be logged and triaged to support trend analysis and understanding the effectiveness of security countermeasures. False-positive security events can be closed following triage.

Where a security event warrants further investigation a security incident should be opened and the rest of this process be followed.

As part of triage, all security incidents must be assigned a severity and category. Depending on the severity of the incident an escalation may be required.

Useful points to consider when triaging a security incident are:
- Who reported or what led to the discovery of the event?
- Where (systems, networks, users) does the event affect?
- What are the consequences of the event?
- How was it discovered?
- What are the related, and potentially exposed, devices, systems or networks?
- Has the source(s) of the events been identified?

Some of these questions may not be answerable immediately; this should not delay making a decision about starting the incident response process. Remember, it is prefered that the process is started when it doesn't need to be, than not run when it is.

*Triage Checklist*
 - [ ] Log the incident
 - [ ] Record the source of the incident
 - [ ] Record details and what is known about the incident
 - [ ] Form a working hypothesis for the incident
 - [ ] Assign an incident severity
 - [ ] Assign an incident category
 - [ ] Escalate or notify (as required)
 - [ ] Mobilise virtual Incident Response Team based on type and severity of the incident
 
 
## Assembling the Team
If the on-call Incident Manager has decided to trigger the incident response process, they must now assemble the virtual team, and move to the *hot* phase of the incident.  

The secretariat immediately starts an incident log using the template provided.

The immediate priority for the Incident Manager is to brief the virtual team on what is already known from the Triage stage above, and identify the gaps in knowledge that need to be filled, and assumptions that need to be confirmed or refuted. 

The next priority is to ensure action is taken so that any on-going breach or attack has been closed down effectively.

### Observe
SMEs and Security Analysts are responsible for capturing and collating data that support the investigation of a security incident.

Data and logs should be sourced from all relevant tools and systems to the investigation and that will help to understand ‘what has, or is, happening?’

Observation may involve detailed technical analysis to take large volumes of data (obtained from raw log files, or captured disk images) and conduct forensics to pull out important data points.

#### Observe Checklist

 - [ ] Identify what data is required to support testing the hypothesis
 - [ ] Record the working hypothesis in the incident log
 - [ ] Confirm which assets and data sources are in scope
 - [ ] Gather direct observations (or request from suppliers)
 - [ ] Collate outside data (e.g. OSINT)

### Orient

The **Incident Manager** collates the data from the Observe stage and, with the Incident Team evaluates the scenario.

Contextual information, such as asset information, agency data, and external/open-source intelligence may be used to help understand the landscape. 

Observations need to be analysed to understand what they tell you about the situation and help prioritise the response. The analysis at this stage takes ‘data’ and turns it into ‘information.’ Important questions include, for example, ‘is this an active event still unfolding?’ or ‘is action needed immediately to prevent further consequences?’

The aim of this stage is to form a provable hypothesis: something that further observation or action can test. It is important to assert the objective facts rather than adopt subjective assumptions.

> “Never attribute to malice, that which is adequately explained by stupidity.” – Hanlon’s Razor

> “When you have eliminated the impossible, whatever remains, however improbable – must be the Truth.” – Sherlock Holmes

When forming and reviewing hypotheses the Analysis of Competing Hypothesis (ACH) method can be used to conduct a structured review of hypotheses, identifying which observations are consistent, inconsistent or not applicable. 

Once the hypothesis is formed then decisions that need to be made in order to take the next steps can be identified.

#### Orient Checklist

 - [ ] Analyse the data to inform the understanding of what has, and is, going on
 - [ ] Describe any new hypotheses that explain the causes of the event
 - [ ] Combine observed data to understand the context
 - [ ] Test the observations against the proposed hypothesis (consistent, inconsistent, n/a)
 - [ ] Secretariate records results in incident log
 - [ ] Identify the activities, and decision points, required to progress the incident

### Decide

The **Incident Manager** with appropriate delegated authority, makes the required decisions based upon the context established in the previous stage. The **Incident Manager** explains the decisions and justifications for the course of action, which are recorded by the **Secretariat**.

Decisions should, where possible, be small in nature to preserve agility when dealing with evolving situations and so that the effects of any actions can be observed and actions pivoted if required.

#### Decide Checklist

 - [ ] Convene ‘heartbeat’ call
 - [ ] Report the known-facts from observations and orientation of the incident in plain English, wherever possible, e.g.:
 - [ ] What happened?
 - [ ] What does this mean for us?
 - [ ] What have we done?
 - [ ] What are we doing next?
 - [ ] Confirm the severity and categorisation of the incident are still appropriate
 - [ ] Discuss each decision point
 - [ ] Record the outcome in the incident log
 - [ ] Agree on the timeframe for the next decision point

### Act

SMEs, with support from others in the team, act on the decisions made in the previous stage to further the investigation or remedy of the situation.

It is important that actions be logged so that any cause/effect can be tracked and any ‘red herring’ subsequent security events discounted from the hypothesis.

During the ‘act’ stage teams will try to contain the threat and eradicate any actors that have infiltrated our environments.

Where action may have a side effect on authorised user behaviour it is important that they are informed to help minimise further disruption.

Actions may include:

 - Isolation of systems (can include critical systems, virtual machines, websites)
 - Reset of credentials and ability to block or lockdown remote access
 - Blocking in/outbound traffic and emails
 - Removing malicious files (clean or rebuild machines, clean user profiles, using AV, or deploying scripts)
 - Resetting domain admin and service accounts, and estate wide resets
 - Remotely isolate or quarantine machines or parts of the network
 - Remotely block or remove malicious files and/or processes
 - Block or alert on specific patterns (e.g. traffic patterns)
 - Monitoring of network and host activity to confirm actions have been successful
 - Moving suspicious VMs to quarantined virtual networks
 - Taking snapshots of block storage

The success or failure of every action should always be ascertained, especially before moving to recovery. The results form a data point when circling back to the ‘observe’ stage.

#### Act Checklist

 - [ ] Plan the activities required to achieve the objective
 - [ ] Communicate the plan with affected stakeholders
 - [ ] Record details of the actions taken and the results achieved
 - [ ] Communicate progress to the Incident Manager

### Recover

The **Incident Manager** is recommending a ‘green light’ to affected areas to resume business as usual activities once the SMEs confirm that the relevant systems have returned to a clean and fit state.

Once the security incident is believed to have been contained and consequences understood the primary goal becomes a return to ‘business as usual.’

Depending on the severity and scale of the incident this may be a brief set of checks, or a far more involved process.

For malware or system compromise events that may involve returning systems to a ‘clean’ and ‘known good’ state. This may involve applying further risk mitigations or security countermeasures to prevent or reduce the frequency that similar events occur in the future, such as configuration changes or applying security patches to harden the security posture.

All recovery efforts should be closely monitored so that you can respond quickly in the event of recurrence and confidently ‘sign-off’ systems back to live operations. You may need to return to the 'orientate' stage, and loop around. This is the Incident Manager's decision.

The team will also contact regulator(s) and other third parties (such as NCSC, Cabinet Office, Law Enforcement) as required, and ensure internal stakeholders, such as relevant SIRO(s), SCS, Ministers are briefed on the issue as appropriate.

Wider internal comms regarding the incident, as required, in conjunction with employee relations if there is a staff impact, will need to be undertaken in the 'act' phase. External comms with affected organisations (either as victims of, or vector for, attack) or individuals may also be required.


#### Recover Checklist

 - [ ] Confirm that the events are believed to have been successfully contained
 - [ ] Plan activities required in order to restore affected systems and assets to BAU state
 - [ ] Request any backups needed (NB: data-only backups, rather than snapshots, reduce the risk of reintroducing threats)
 - [ ] Communicate recovery plan to stakeholders
 - [ ] Implement recovery plan
 - [ ] Review systems to confirm operating as expected / ‘clean state’
 - [ ] Make a return to BAU operations recommendation to Senior Management
 - [ ] Communications with regulators, third parties, and internal stakeholders
 - [ ] Wider internal comms regarding the incident as necessary
 - [ ] Close the incident disband the Virtual IR Team


This concludes the 'hot' phase of the incident. 
