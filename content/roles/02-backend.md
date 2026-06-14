---
id: backend
order: 2
title: Backend Engineer
short: Backend
icon: backend
stack: APIs · Databases · Microservices · System Design · Performance · Reliability · Data Contracts
---

## Lead
Backend engineering is where the AI disruption gets interesting. The surface threat is real: AI writes CRUD endpoints, generates ORM models, scaffolds APIs, and produces migrations faster than any human. Go deeper into the distributed-systems decisions, the reliability contracts, the failure-mode engineering, and you hit work that depends on institutional context no model has been trained on, which is exactly where backend engineers become hard to replace.

## Intro
The backend engineers who thrive own the contracts between systems. They carry two years of design-decision context in their heads. They know why the retry strategy looks the way it does and exactly what happens to the downstream queue when someone changes it. Endpoint count is not the measure here; the measure is how much of the system's behavior you can predict and answer for.

## Layer 1 - Commodity: What AI now does for you
Writing CRUD endpoints in any framework. Generating ORM model definitions from schema descriptions. Writing SQL queries and stored procedures from natural language specs. Scaffolding REST and GraphQL APIs with standard patterns. Writing serializers, validators, and error handling boilerplate. Database migration scripts. Integration test skeletons and fixture setup. API documentation from code (Swagger/OpenAPI). Standard authentication middleware patterns. Rate limiting and pagination boilerplate. Docker and containerization configs for common service architectures.

## Layer 2 - Leverage: How to work with AI effectively
Generating several schema design options and using your knowledge of the real data access patterns to pick the right one. Having AI produce load-test scripts while you define the SLOs being tested and read what the results say about system health. Letting AI propose caching strategies, then validating them against your real traffic patterns, cache invalidation complexity, and consistency requirements. Running AI as a first-pass reviewer on your own PRs, which catches mistakes and sharpens your eye for what to look for. Having AI draft runbooks while you supply the sections that need real system context: the judgment calls, the known failure modes, the things that matter at 3am.

## Layer 3 - Irreplaceable: What no AI can own
Designing the service boundary that prevents a downstream provider failure from cascading into a full-system outage, the kind of decision that requires understanding six months of incident history and three different team's operational patterns. Knowing the data contract between your service and its 12 consumers, and knowing which of them will silently break when you change the response schema in a way that looks backwards-compatible but isn't. The architectural judgment to decide when to split a service and when the operational overhead isn't worth it. End-to-end reliability ownership, not just keeping the lights on, but understanding the system well enough to predict where the next failure will occur before it does.

## Pull Quote
At 3am, our downstream payment provider went dark with zero warning. Our retry logic was correct in isolation and catastrophic at scale: we hammered an already-degraded service with 40x its normal traffic. No AI had context on the contract we'd signed with that provider six months earlier or why we'd built the retry the way we did. I did, and that institutional memory was the only thing that let us make the right call in under ten minutes.

## Real Talk
The backend engineers I've watched get commoditized described their job as "building APIs." The ones thriving describe it as "owning the reliability of system X." Becoming the person who answers for a system at 3am is the single most powerful career move available to a backend engineer right now. AI will happily take the work off your plate; it can't take the accountability for the outcome, so make that accountability the thing you're known for.

## Roadmap
1. **Days 1–30: Draw the map.** Pick one service you own or are closest to. Draw its full dependency map, every downstream call, every queue, every external provider, every database. Mark the single points of failure. Identify what happens to each consumer if this service goes down for 30 seconds. Five minutes. An hour. You will almost certainly find at least two failure modes nobody has documented. Write them up.
2. **Days 31–60: Write an ADR for the most complex decision in your system.** An Architecture Decision Record: what decision was made, what alternatives were considered, why they were rejected, and what the trade-offs are. Force yourself to write the alternatives section ... the options you didn't choose. This is the irreplaceable context. When AI or a new team member looks at your codebase, they see the decision. Only the ADR explains the reasoning. Be the person who writes those.
3. **Days 61–90: Run a chaos exercise.** Kill a dependency in staging. Not randomly ... deliberately, with a hypothesis about what should happen. Write the postmortem even if nothing breaks. Did your alerts fire? Did the fallback work? Was the degradation graceful or catastrophic? Publish the postmortem to your team. The person who runs chaos exercises and owns the results is building the most defensible expertise in backend engineering right now.

## Trap
**Technology tourism, chasing the latest database or message queue.** Kafka vs. Pulsar vs. RabbitMQ. PostgreSQL vs. DynamoDB. Knowing a technology is cheap: it's documented, it's in every tutorial, and an AI can lay out the trade-offs in two paragraphs. Own the problem instead. The tool is interchangeable; your understanding of why *your specific system* breaks at *your specific scale*, and your judgment about how to fix it, is not.

## Bonus
Write a "failure resume" for your systems: every significant incident or near-miss, what caused it, and what you personally learned. Keep it for yourself, not for performance reviews. A deep library of failure patterns is one of the hardest things to hand to a model or a new hire, so every outage you survive and document compounds into expertise nobody can shortcut.
