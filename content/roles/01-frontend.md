---
id: frontend
order: 1
title: Frontend Engineer
short: Frontend
icon: frontend
stack: React · Vue · CSS · Design Systems · Web Performance · Accessibility · Browser APIs
---

## Lead
Frontend is the most visibly disrupted role in the AI era. v0, Cursor, Copilot, and Figma AI now turn a one-line description into a functional React component. If most of your week is boilerplate UI code, you're in the danger zone: the specific version of the job you're doing is being commoditized faster than any other role on this list, even though frontend itself isn't going anywhere.

## Intro
The counterintuitive part: demand for *great* frontend engineers has never been higher. An AI-generated UI and a UI built with real taste, deep accessibility understanding, and performance engineering are separated by an enormous gap, and that gap is visible to anyone who uses the product. The market is splitting into disposable UI factories on one end and frontend architects on the other, with the middle ground shrinking fast.

## Layer 1 - Commodity: What AI now does for you
Writing boilerplate React and Vue components from a description. Generating CSS from Figma specs or visual references. Creating form validation logic with error states. Writing unit tests for pure functions and utility helpers. Producing responsive layouts from wireframes. Converting design mocks to working code. Basic accessibility fixes like ARIA labels and focus management. Generating Storybook stories for existing components. Writing documentation from code. Creating animation CSS from reference descriptions. Scaffolding new pages with routing.

## Layer 2 - Leverage: How to work with AI effectively
Reviewing AI-generated components for the accessibility gaps it routinely misses: screen reader compatibility, keyboard navigation flows, color contrast edge cases. Feeding AI your design system's constraints so it produces brand-consistent output instead of generic boilerplate. Running AI performance audits across a codebase and deciding which recommendations are worth shipping for your actual user profile. Generating 10 layout variations in the time it used to take to sketch 2, then applying taste to pick and refine. Having AI write test cases for your logic while you validate the edge cases it gets wrong.

## Layer 3 - Irreplaceable: What no AI can own
Owning the design system that defines how the entire product looks and feels, and making the hard judgment calls about when to break the rules and when to enforce them. Understanding the full performance budget of a 500M-user app: which CSS property triggers a layout reflow, which JavaScript execution blocks the main thread, which font-loading strategy kills LCP by 200ms. The taste to look at a generated component and say "this is technically correct and accessible and on-brand, but it still feels wrong, and here's why." Knowing which browser quirks will bite you in Safari on iOS 16, which the AI has never debugged at 2am before a launch.

## Pull Quote
Every AI-generated component has the same tell: it's correct and it has no opinion. Great UI carries opinions in every spacing decision, every interaction pattern, every micro-animation. Taste is the skill underneath all of that, and there's no prompt that produces it for you.

## Real Talk
Junior frontend developers who spend their careers writing components they could have described in a prompt to v0 will find it hard to compete in 18 months. The path forward is depth. Own the system: know why every design choice works, not just that it does. Build the performance intuition that only comes from debugging real production incidents on a high-traffic app, the kind of intuition that tells you a 200ms LCP regression came from a font-loading change before you've even opened the profiler.

## Roadmap
1. **Days 1–30: Audit your commodity work and automate it.** Track every component you build in a week and tag each one: could AI have generated this from a description? Set up Cursor or GitHub Copilot and delegate the tasks that pass that test. Aim to reclaim 6–8 hours a week. Skip the abstract "learn AI" goal and point the tools at your specific, current problem.
2. **Days 31–60: Claim a piece of the design system.** Volunteer to own one significant chunk of it: a component library, a token architecture, a theming system. Then document the reasoning behind every decision: why this spacing scale, why this color ramp, why this interaction pattern. The components are just code that AI can regenerate. The documented reasoning is the artifact that makes you the owner.
3. **Days 61–90: Run a performance audit on something nobody owns.** Pick a slow product surface with no performance owner. Run a Core Web Vitals analysis, fix two or three issues, and write a postmortem-style document on what you found, why it happened, and what it cost users in real numbers. Ship the learning publicly: your team, your engineering blog, LinkedIn. Whoever owns performance becomes the person the org can't easily replace.

## Trap
**Learning yet another JavaScript framework.** Svelte, Astro, Qwik, Solid, whatever this month's favourite is. Framework knowledge is cheap: documented, promptable, learnable in a week. The durable skill is evaluating a framework against a real production context and owning the migration at scale. The valuable engineer is the one who can say whether a 40-engineer org can actually absorb a React-to-Solid move given its existing component library, and who then leads that migration, not the one who has skimmed the docs for all four.

## Bonus
Find one accessibility issue in your product that affects real users: keyboard users, screen reader users, people with motor impairments. Fix it, then write up why it existed and how you found it. Accessibility is one of the last areas where AI still routinely ships incorrect output, so an engineer with real accessibility instincts stays in perpetual demand.
