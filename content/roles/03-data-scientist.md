---
id: data-scientist
order: 3
title: Data Scientist
short: Data Science
icon: data-scientist
stack: ML Models · Statistical Analysis · Experimentation · Feature Engineering · Business Insights
---

## Lead
Data science is splitting in two. On one side sits the work that was always data processing with a statistics wrapper: automated reporting, basic predictive models, EDA on structured data. AI handles that with remarkable competence now. On the other side sits the genuinely hard part that always carried the value, deciding what to measure, defining what a meaningful result even is, turning a statistical finding into a business decision, and catching the moment the data starts lying to you.

## Intro
Here's the uncomfortable truth: plenty of people carrying the title "Data Scientist" have spent their whole careers in the commodity layer, valued for writing Python, running sklearn, and producing charts. The judgment about what to analyze and why was the actual job, and that's the version of the role now under enormous pressure.

## Layer 1 - Commodity: What AI now does for you
Exploratory data analysis on structured datasets ... producing summary statistics, correlation matrices, distribution plots. Feature engineering suggestions for tabular data. Running baseline models (sklearn, XGBoost, LightGBM) and producing comparison tables. Writing data cleaning and preprocessing pipelines from spec. Generating charts and visualizations from data. Drafting analysis reports and slide decks from findings. Writing statistical test boilerplate (t-tests, chi-squared, ANOVA). Building dashboards from a spec. Documentation for notebooks. Generating SQL for common aggregations and joins.

## Layer 2 - Leverage: How to work with AI effectively
Using AI to generate a full hypothesis tree for a business problem, brainstorming every possible explanation for an anomaly, and then applying domain knowledge to prioritize which three are worth actually testing. Having AI produce a first-cut feature set from a problem description while you validate each feature against the business logic the model doesn't know. Using AI to write experiment analysis code (sample size calculations, power analysis, significance testing) while you own the experimental design, what constitutes a meaningful effect, what the right control is, what confounds exist in your specific data. Letting AI generate multiple model architectures and then picking the one you can actually explain to the product team and defend when it fails.

## Layer 3 - Irreplaceable: What no AI can own
Defining what "good" looks like in your domain. A model with 92% accuracy on a fraud detection problem might be catastrophically wrong, only someone who understands the asymmetric cost of false negatives can set the evaluation bar correctly. Knowing when to stop an A/B test before statistical significance because the business context has changed in a way that makes the result irrelevant. The judgment to say "this result is statistically significant but it doesn't make business sense, here's what's actually going on in the data." Recognizing when a dataset is subtly broken in a way that produces plausible but wrong outputs. Translating a finding into a recommendation that gets a decision made.

## Pull Quote
The most valuable thing a data scientist produces is a decision, not a model. A 94%-accurate model that changes nothing the business does is worthless; a rough analysis that surfaces the right insight and flips a strategic call is the work people remember. AI can build the 94% model. The insight that actually moves the decision still comes from you.

## Real Talk
If your value as a data scientist lives entirely in writing pandas, running models, and producing charts, you're in the danger zone, because the market for that skillset is in structural decline. Get obsessively close to the business problems your data is meant to solve. Become the person consulted on what to measure before any data work begins. That seat, upstream of the analysis, is the one AI cannot take.

## Roadmap
1. **Days 1–30: Write a model card for a production model.** Pick one model your team runs in production. Write a one-page document covering: what it optimizes for, what it's sacrificing, where it fails, who should trust it for which decisions, and what would cause it to be wrong. That document almost certainly doesn't exist yet, and writing it makes you the person who actually understands the model, which is the person the org calls the moment it starts misbehaving.
2. **Days 31–60: Own an experiment end-to-end.** Don't just run the analysis. Own the entire lifecycle: write the business case for running the experiment, design it (what's the control, what's the treatment, what's the minimum detectable effect, how long does it need to run), conduct it, analyze it, and, most importantly, write the decision recommendation. Go past "users who saw variant B clicked more" to "we should ship variant B; here's the expected impact on Q3 revenue and the caveats that come with it."
3. **Days 61–90: Translate a finding into a meeting that gets a decision made.** Present a data insight to a non-technical stakeholder and leave with an actual decision in hand, not a follow-up and not a "we'll take this away." Turning data into organizational action is the scarcest and most valuable skill in data science right now, and it's the one almost nobody practices deliberately.

## Trap
**Chasing model benchmarks and Kaggle leaderboards.** A top Kaggle rank is impressive in one narrow context and close to useless in most others, because it optimizes metric performance on a clean, labeled dataset with a well-defined problem. Real data science is almost never that tidy. The durable skill is choosing which metric to optimize in the first place and recognizing when optimizing it causes harm the leaderboard can't show you, like a fraud model that minimizes overall error while quietly waving through the costliest false negatives.

## Bonus
Find one case in your organization where a business decision was made on data that was subtly wrong: wrong methodology, wrong metric, wrong interpretation. Document what happened, why the data led people astray, and what the right analysis would have produced. This kind of near-miss postmortem is the hallmark of senior data science judgment, and it doubles as a powerful portfolio piece.
