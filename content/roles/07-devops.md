---
id: devops
order: 7
title: DevOps / SRE
short: DevOps / SRE
icon: devops
stack: Infrastructure · CI/CD · Observability · Incident Response · Reliability · Platform Engineering
---

## Lead
DevOps and SRE work has a peculiar relationship with AI disruption. The configuration layer, Terraform, Kubernetes manifests, CI pipeline definitions, alert rules, is being automated at remarkable speed. Meanwhile the human judgment that reliability engineering runs on grows more valuable as systems get more complex. Correctly configured infrastructure and a system that behaves well under failure are separated by a wide gap, and that gap is where AI runs out of road.

## Intro
The best SREs I know think of themselves as reliability owners: people accountable for what happens when things go wrong, carrying the context, the nerve, and the judgment to make the right call under pressure. That ownership is the part of the role AI can't displace, and it's worth far more than fluency with any particular config syntax.

## Layer 1 - Commodity: What AI now does for you
Writing Terraform and Pulumi infrastructure-as-code from a spec. Generating CI/CD pipeline configurations for standard toolchains (GitHub Actions, Jenkins, CircleCI). Creating Dockerfile templates and multi-stage build configurations. Writing Helm chart scaffolding for standard service deployments. Generating monitoring alert rules from SLO definitions. Writing runbook templates for common failure scenarios. Producing infrastructure cost analysis reports from billing exports. Generating Kubernetes resource manifests for standard workload types. Writing bash and Python automation scripts for common operational tasks. Creating network topology diagrams from infrastructure descriptions.

## Layer 2 - Leverage: How to work with AI effectively
Using AI to generate candidate alert threshold configurations and then calibrating them against your actual incident history, because generic thresholds produce either alert fatigue or missed signals, and only your incident history can tell you which way you're biased. Having AI produce infrastructure cost optimization suggestions (right-sizing, reserved instances, spot pricing) and then deciding which to act on based on the engineering effort, the risk, and the actual savings ... not the theoretical maximum. Using AI to generate runbook content while you add the "judgment call" sections: the cases where the standard procedure doesn't apply, the known failure modes that require off-script action, the context that only comes from having been on the incident before.

## Layer 3 - Irreplaceable: What no AI can own
Owning the blast radius. The ability to say, and be right, about what breaks, in what order, with what user impact, when a given service or dependency fails. This requires having built the system, lived through its failures, and internalized its failure modes in a way that no amount of reading documentation can replicate. Being the engineer who designed the fallback strategy that kept a 3am outage from becoming a 12-hour incident, who had thought through the failure scenario before it happened, not during. Incident ownership during a live event: the judgment calls made in real time, under pressure, with incomplete information, are irreducibly human.

## Pull Quote
Reliability is built in the quiet moments: the runbooks written before the incident, the chaos tests run when nothing's on fire, the postmortems that go after the systemic cause instead of the symptom. AI helps produce the artifacts. The engineer who decides what to write, what to test, and what to actually fix is the one who owns reliability.

## Real Talk
DevOps engineers who built their careers on configuring infrastructure will feel growing pressure as AI tooling takes over more of that configuration. Move toward reliability ownership: be the person accountable for what happens during incidents, not only for the config that hums along in normal operation. That means carrying a pager, owning postmortems, and accumulating the institutional knowledge that only comes from surviving real production failures. There's no shortcut around that experience.

## Roadmap
1. **Days 1–30: Build a blast radius map for your most critical service.** Document every dependency, every failure mode, and the cascade: if this service goes down for 30 seconds, what breaks? For five minutes? An hour? If this map doesn't exist, you've just identified the most dangerous gap in your system's operational knowledge. The process of building it will reveal at least one thing you didn't know ... and that's the point.
2. **Days 31–60: Own a postmortem end-to-end, including the systemic fix.** Write up what happened, then drive the "contributing factors" section all the way to the systemic issue underneath the immediate cause: the process gap, the monitoring blindspot, the design assumption. Then drive the fix at that level. A postmortem that ends at "we added a unit test" changes nothing; one that ends at "we changed how we think about X" is the kind of work that defines a reputation.
3. **Days 61–90: Define and publish your team's SLOs with business rationale.** Go past "99.9% availability" to the reasoning: why 99.9%, what the marginal cost of adding another nine actually buys, and how different a 15-minute degradation at 2pm Tuesday is from one at 2am Sunday. The engineer who connects reliability targets to business outcomes and gets both engineering and business stakeholders to sign off on them is doing work the org can't easily reassign.

## Trap
**Chasing cloud certifications as a primary career investment.** AWS Solutions Architect, GCP Professional Cloud Architect, Azure Expert all confirm you know a provider's API surface. None of them confirm you can make systems reliable under real production conditions. An engineer who has survived 20 real incidents and owns the postmortems is worth far more than one holding five certifications and no production scars. Get certified if the job requires it, and keep it in its lane: it's a checkbox, not expertise.

## Bonus
Build a "failure library" for your team: a structured, narrative catalog of every significant failure mode your systems have shown, with the context, the response, and the lesson, written as stories rather than bare incident tickets. When a new engineer joins, this library turns months of ramp-up into weeks. The person who builds it, maintains it, and owns it becomes the institutional memory the team can't easily do without.
