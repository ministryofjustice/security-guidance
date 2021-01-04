# Before an incident

This part of the [Incident Response Plan](security-incident-management-plan.md) should be read by all those who might be part of a virtual [Incident Response Team](roles-and-responsibilities-for-handling-security-and-privacy-incidents.md), in advance of an actual incident.

Whilst every incident will be different, there are some key approaches we expect every Incident Response Team to be aware of and to follow.

**Parent topic:**[Security Incident Management Plan](security-incident-management-plan.md)

## What is an incident?

\(edit note: already covered?\)

## Useful templates

\(edit note: to do\)

## Joining incident calls

You've just joined an incident call, and you've never been on one before. You have no idea what's going on, or what you're supposed to be doing. This will help you through your first time on an incident call, and will provide a reference for future calls you may be a part of.

### First Steps

-   If you intend on participating on the incident call you should join both the call, and Slack.

-   Make sure you are in a quiet environment in order to participate on the call. Background noise should be kept to a minimum.

-   Keep your microphone muted until you have something to say.

-   Identify yourself when you join the call. State your name and the system you are the expert for.

-   Speak up and speak clearly.

-   Be direct and factual. Be clear about what you know versus what you suspect.

-   Keep conversations/discussions short and to the point.

-   Bring any concerns to the Incident Manager on the call.

-   Respect time constraints given by the Incident Manager.


### Clear communication

Use clear terminology, and avoid using acronyms or abbreviations during a call. Clear and accurate communication is more important than quick communication.

Do not invent new abbreviations, and always favor being explicit rather than implicit. It is better to make things clearer than to try and save time by abbreviating, only to have a misunderstanding because others didn't know the abbreviation.

Never be afraid to ask for something to be repeated if it wasn't clear - this saves time in the long run.

### The Incident Manager

The Incident Manager is the leader of the security incident response process, and is responsible for bringing the incident to resolution. They will announce themselves at the start of the call, and will generally be doing most of the talking.

-   Follow all instructions from the incident manager, without exception.

-   Do not perform any actions unless the incident manager has told you to do so.

-   The incident manager will typically poll for any strong objections before performing a large action. This is your time to raise any objections if you have them.

-   Once the incident manager has made a decision, that decision is final and should be followed, even if you disagreed during the poll.

-   Answer any questions the incident manager asks you in a clear and concise way.

-   Answering that you "don't know" something is perfectly acceptable. Do not try to guess.

-   The incident manager may ask you to investigate something and get back to them in X minutes. Make sure you are ready with an answer within that time.

-   Answering that you need more time is perfectly acceptable, but you need to give the incident manager an estimate of how much time.


## Things to avoid

There are some common anti-patterns for incident response that we try to avoid.

### Getting everyone on the call

It's important to maintain an effective span of control on any incident response. If you have more than 7 or 8 people directly reporting to the Incident Manager things can quickly get overwhelming.

### Everyone staying on the call

We believe in teamwork, not individual heroics. If someone is asked to join a call to investigate something, then once they're part is complete then we encourage people to leave if they're no longer required to help - not stick around 'just in case'.

### I need a status update on the status update

Seniors need to know what's going on and can often seem to want status updates every 5 minutes to keep them in the loop. The problem with this is that you'll spend the entire time providing status updates rather than resolving the incident.

We set out at the start of an incident how regularly we intend to provide updates, and do our utmost to stick to this cadence. If something happens that warrants an update, it is of course fine to share it, but our focus is on reducing the harm first and foremost.

### Assuming silence means no progress

It can be common to assume silence on an incident call means that nothing is being done, however this is rarely the case. When joining a call, be aware that a chatterless session can be acceptable and reasonable. Silence usually means everyone is working on fixing the problem rather than talking and providing updates.

The Incident Manager is the one who should be doing most of the talking on a call. They will typically fill silence with a status update if appropriate, but others within the virtual team need to know that silence on a call isn't a bad thing, and doesn't mean that progress has stopped. Making sure everyone is aware of this ahead of time will prevent awkward conversations during an incident call, which would be ultimately distracting from resolving the incident.

### Skipping the post-incident activities

It's tempting once an incident is resolved to not bother with the follow-up. Either you feel like the cause is well known, or you don't feel that it's worth it. Don't fall into this trap! It is always worthwhile. People were activiated to respond to an incident, which had a cost associated with it. We want to be sure that we understand why that happened, so we can avoid that cost in future.

Don't make the mistake of neglecting a post-mortem after an incident. Without a post-mortem we fail to recognise what we're doing right, where we could improve, and most importantly, how to avoid making the same exact mistakes next time around. A well-designed, blameless post-mortem allows teams to continuously learn, and serves as a way for us to iteratively improve our infrastructure and incident response plan.

Even if an incident turns out to be a false alarm it's often worth conducting ta post-morten to figure out whether we coud have avoided it.

### Trying to take on multiple roles

It can be really tempting as the Incident Manager to try and assume the role of Subject Matter Expert, particularly when the manager has specific knowledge of the systems involved from previous work. Wanting to solve the incident quickly, the Incident Manager will start to try and solve the problem. Sometimes you might get lucky and it will resolve the incident, but most of the time the immediately visible issue isn't necessarily the underlying cause of the incident. By the time that becomes apparent, you have an Incident Manager who is not paying attention to the other systems and is just focussed on the one problem in front of them. This effectively means there's no incident Manager, as they would be busy trying to fix the problem.

You cannot take on another role at the same time as being an Incident Manager. It can be a difficult to do this when you want to jump in as an SME, but you must resist the temptation to abandon the role of Incident Manager. If you really are the only person able to solve the problem, you should handover to another Incident Manager and then assume the role of SME. This ensures that the response process remains on track with a dedicated Incident Manager.

### Individual heroics

It can be tempting to try and solve every issue yourself if you're acting as a Subject Matter Expert. Every request that comes up, you want to jump on it and say you'll take care of it. You'll be the indispensable one who solves all the problems! As noble as the intent is, it rarely leads to an efficient outcome. You want to avoid as much multi-tasking as possible during an incident, and focus on one problem at a time. Don't try to solve everything yourself. If multiple requests are coming up for your area of expertise, delegate them to other experts, bringing in backup responders if required.

Likewise, if another SME has been assigned a task, don't do the task on their behalf without consulting with them first. While you are trying to help, it will end up hindering the response as you'll have two people working on the same issue, and they may be interfering with each other in unexpected ways.

