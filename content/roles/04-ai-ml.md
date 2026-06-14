---
id: ai-ml
order: 4
title: AI / ML Engineer
short: AI / ML
icon: ai-ml
stack: Model Training · Fine-Tuning · Inference · MLOps · LLM Integration · Evaluation · Deployment
---

## Lead
The AI/ML engineer holds the most paradoxical position on this list: you build the tools automating everyone else's job while those same tools automate big chunks of your own. The parts going first are exactly the parts that got the heaviest tutorial coverage over the last five years, training loop boilerplate, standard fine-tuning pipelines, basic RAG setups, API integrations. If that's your whole day, read this one carefully.

## Intro
The parts nobody can hand to a model are the genuinely hard ones: knowing what to evaluate, designing evaluations that catch real failure modes, and making deployment calls in a domain where the outputs are probabilistic, the failures are silent, and the consequences stay invisible until they turn catastrophic.

## Layer 1 - Commodity: What AI now does for you
Fine-tuning pre-trained models on a labeled dataset (increasingly automated by platforms like Vertex AI, SageMaker Autopilot, and OpenAI fine-tuning APIs). Writing training loop boilerplate in PyTorch or JAX. Generating data augmentation pipelines for common data types. Writing standard inference serving code for common model architectures. Building prompt templates for straightforward tasks. Connecting LLM APIs with standard patterns. Writing model card documentation from a template. Creating basic RAG pipelines with off-the-shelf vector databases. Standard MLflow experiment tracking setup.

## Layer 2 - Leverage: How to work with AI effectively
Using AI to generate candidate evaluation metrics for a new task, brainstorming precision/recall/F1/BLEU/ROUGE variants, and then applying domain knowledge to decide which failure modes actually matter most for your use case. Having AI produce a first-pass dataset analysis (label distribution, quality issues, potential leakage) while you validate the findings against the known messiness of your data collection process. Using AI to generate adversarial test cases and edge-case prompts while you define the failure taxonomy, what categories of failure exist, which are acceptable, which are catastrophic. Letting AI write the benchmark evaluation harness while you specify exactly what it needs to measure and why.

## Layer 3 - Irreplaceable: What no AI can own
Owning the evaluation framework, because AI cannot self-assess at the depth and domain-specificity your use case requires. The judgment to say "this model is passing all our automated evals but I've seen three production failure patterns our evals don't capture, here's why and here's what we need to add." Knowing when to deploy, when to hold, and when to roll back, a decision that requires understanding the full context of your system, your users, your business constraints, and the model's failure modes simultaneously. Building the monitoring system that catches silent degradation before users do. The organizational courage to say "this model is not ready" when the pressure to ship is enormous.

## Pull Quote
The most dangerous AI systems are the ones that fail silently. The model returns a response, it looks plausible, and nobody notices until a downstream consequence shows up weeks later, hard to trace back. The engineer who builds evaluation infrastructure that catches those silent failures before users do is the most valuable person on any AI team.

## Real Talk
Most "AI engineers" right now are doing sophisticated prompt engineering and API integration. That work matters, and it's also becoming commodity fast. The ones who'll be hard to replace in 18 months own evaluation rigor: they design test suites that catch failure modes before production, and they know a model passing your evals is only as trustworthy as the evals themselves. Invest in evaluation. Almost nobody is doing it well, which is exactly why it pays.

## Roadmap
1. **Days 1–30: Audit one production model's failure modes.** Pick a model running in production. Find three failure modes your current evaluation suite does not catch. Write tests for them. (You'll almost certainly find them faster than you expect.) You're hunting for the gaps in your coverage, so document each gap as formally as the tests you write to close it.
2. **Days 31–60: Build a red team eval process.** Take one of your LLM integrations and run a structured red-teaming exercise: adversarial inputs, jailbreak attempts, prompt injection, edge cases that expose the model's real-world failure modes. Produce a failure taxonomy document, a classification of the types of failures that exist, with examples. This artifact is the most valuable thing you can produce for an AI team. Almost no teams have one.
3. **Days 61–90: Write the deployment decision framework.** For one model in your pipeline, write a formal document that answers: What metrics trigger a no-ship decision? What production metrics trigger a rollback? What does "good enough" look like, and why? Who makes the final call? This document forces the organizational conversation that most teams avoid. Being the person who drives that conversation, and produces the artifact, is an irreplaceable function.

## Trap
**Fine-tuning for the sake of fine-tuning.** Most teams pour effort into model training and starve evaluation. A smaller, thoroughly evaluated model your team understands and can monitor will beat a state-of-the-art model you can't explain to product and can't watch in production. For most teams the math runs the wrong way: every hour on fine-tuning is an hour not spent building the evals that are the actual moat. Own the evals.

## Bonus
Build a "model behavior changelog": a document tracking how your model's behavior shifts across versions, with concrete examples for each category of change. Most teams track performance metrics; almost none track behavioral changes at the example level. The day something breaks in production and you need to pinpoint when the behavior drifted, this artifact is what saves you hours of guessing.
