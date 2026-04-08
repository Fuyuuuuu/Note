# Twillot 書籤（精簡）— 第 14/20 部

原檔：Twillot 書籤 · 已合併 `twillot-bookmark-2026-04-07.csv`（新增 **66** 則，略過重複 **0** 則） · 全檔共 **4003** 則 · **本部第 2602–2802 則**（共 201 則）

---

**作者** Michael Truell（@mntruell）  
**貼文連結** https://x.com/mntruell/status/2012825801381580880  

**正文**

Watch Cursor build a 3M+ line browser in a week 

---

**作者** vas（@vasuman）  
**貼文連結** https://x.com/vasuman/status/2012747420208070767  

**正文**

Is there an open source version of Lovable / V0 / Bolt?

---

**作者** BLACKBOX AI（@blackboxai）  
**貼文連結** https://x.com/blackboxai/status/2012386609845727437  

**正文**

New Release: Agents API 

Run Blackbox CLI, Claude Code, Codex CLI, Gemini CLI and more agents on remote VMs powered by @vercel sandboxes with 1 single api implementation 
New Release: Agents API 

Run Blackbox CLI, Claude Code, Codex CLI, Gemini CLI and more agents on remote VMs powered by @vercel sandboxes with 1 single api implementation 
@vercel https://agent.blackbox.ai/overview you can get started here

---

**作者** Superpower（@superpower）  
**貼文連結** https://x.com/superpower/status/1957854649160999041  

**正文**

Superpower is now available for $199. From day one, our mission has been simple: build a better model for health — and make it accessible to everyone. 

---

**作者** Zeb Evans（@DJ_CURFEW）  
**貼文連結** https://x.com/DJ_CURFEW/status/2012620277247578426  

**正文**

I guess they don’t understand how Agents already choose software. And certainly a fundamentally flawed understanding of what mainstream personalized software will be in the future (outside of engineers). Agents will not start from scratch, they will start from primitives.

---

**作者** Daksh Gupta（@dakshgup）  
**貼文連結** https://x.com/dakshgup/status/2012315882425598277  

**正文**

we've been working closely with the team at @AnthropicAI over the last several months

the results have been quite remarkable

- with cache optimizations, we're able to maintain low prices while providing top models and deep codebase context even for huge codebases at companies like nvidia and scale ai

- with anthropic's work on terminal use, we're seeing remarkable performance gains on greptile's ability to read git history and trace nested function calls, which make it even better at catching the trickiest bugs

read more on anthropic's blog:

---

**作者** Alton Syn（@WorkflowWhisper）  
**貼文連結** https://x.com/WorkflowWhisper/status/2012590119929172319  

**正文**

I've been building n8n automations for 4 years. Started as a solo freelancer charging $500 per workflow, scaled to a 12-person agency doing $280K/month, then watched everything change in 2025 and rebuilt the entire operation from scratch.

Now I run a $600K/month automation agency (did $753K in November but has averaged out to just over $600K) with 7 employees. Our entire backend is Claude and Cursor. No senior developers. No "automation architects." No technical leads. Just 5 people doing $7.2M annual run rate.

Here's a playbook containing everything I've learned about the new automation economy after making this transition. Let me know if it helps below.

## The Gap That Used to Exist

Most people assume that building serious automation requires deep technical knowledge. JSON structures. API authentication. Webhook debugging. Error handling logic. Hours of documentation reading.

That assumption was correct in 2024. It's completely wrong now.

18 months ago, the "gap" was the space between having an idea and having a working automation. Idea becomes technical knowledge becomes hours of building becomes debugging becomes more debugging becomes maybe a working system.

That gap protected a $47 billion consulting industry. If you couldn't cross it yourself, you had to pay someone who could. $5K for a lead enrichment system. $8K for a voice AI receptionist. $15K for a "custom enterprise solution."

The gap was their moat. And in 2025, it completely collapsed.

## What Actually Changed

The short version: AI learned n8n better than any human ever will.

Not "AI-assisted building" where you still debug for hours. AI that knows every node that exists today. Understands every integration pattern. Handles every edge case automatically. Deploys directly to your instance. Tests and fixes before you even see errors.

The gap between "I want this automated" and "it's running in production" became a sentence. One paragraph of plain English becomes a working system.

I watched this happen in real-time at my agency. Projects that used to take our team 2 weeks started getting done in hours. Not because we got faster. Because the tools got incomprehensibly better.

## The $600K/Month Reality

Here's what my agency actually looks like today.

5 employees total. 2 client success people handling relationship management, not building. 2 project managers handling scoping, communication, and delivery. 1 me doing everything else.

Zero full-time developers.

Not because I'm cheap. Because Claude and Cursor build faster than any developer I could hire.

Last month's numbers: 47 client projects delivered. Average delivery time dropped from 3 weeks to 3 days. Average project value sitting at $12,800. Total billable hours logged at 892. Hours actually spent building: around 180.

That's not a typo. 180 hours of actual building work. The rest is client calls, project management, quality assurance, relationship building.

The technical work that used to require a team of 15 now takes 20% of our total capacity. I describe what I want to Claude. Cursor builds it. n8n runs it. That's the whole technical process.

## How Builds Actually Happen Now

Let me walk you through a real client project from last week.

Client was a mid-size e-commerce brand. Request was a complete competitor monitoring system.

Old process in 2024: Scope document taking 8 hours. Architecture planning at 12 hours. Build scrapers at 40 hours. Set up data processing at 20 hours. Create alerting system at 16 hours. Testing and debugging at 24 hours. Deployment and documentation at 8 hours. Total of 128 hours spread across about 3 weeks. We charged $18,000.

New process in 2026: I opened Cursor with Claude and typed one paragraph.

"Build me an n8n workflow system that monitors competitor pricing across these 5 websites, scrapes daily, compares to our Shopify catalog, calculates margin impact, and sends Slack alerts with recommendations when we're being undercut by more than 5%. Include a weekly summary email to the client."

Went to get coffee. Came back. 6 workflows sitting in the client's n8n instance. Connected. Tested. Running.

Total time: 23 minutes. What we charged: $8,500.

The margin improved. The delivery time collapsed from weeks to same-day. Client satisfaction went up because they got results faster. Everyone won except the agencies still doing this the old way.

## The Stack That Makes This Possible

I'm not gatekeeping this. Three tools changed everything for my agency.

Claude handles strategic thinking, architecture, and complex reasoning. When I need to think through how a system should work, what edge cases exist, what the client actually needs versus what they asked for, Claude is where that happens. It's the brain of the operation.

Cursor handles code execution, custom scripts, and direct deployment. When Claude's plan needs to become reality, Cursor builds it. Custom integrations, data transformations, scripts that connect systems that weren't designed to talk to each other. Cursor makes it real.

Synta MCP is the bridge that connects Claude and Cursor directly to your n8n instance with real-time documentation. This is the piece most people are missing.

Before Synta, you'd describe a workflow to Claude, copy the JSON, paste it into n8n, debug for 3 hours, cry, start over. Now Claude connects directly to your n8n instance. Builds it there. Tests it there. Fixes it there.

No copy-paste. No broken JSON. No "hallucinated node that doesn't exist." It literally watches your workflows execute and debugs them in real-time.

I built 11 client workflows last week. Average time: 7 minutes. Average completion: 97%. Bugs fixed by AI: all of them.

The combination is devastating. Claude thinks about what you need. Cursor builds it. Synta deploys it directly to n8n. English in. Working automation out.

## Why Technical Knowledge Became a Liability

This is the counterintuitive part that took me months to accept.

The people who spent 2 years mastering node configurations, webhook setups, and JSON schemas are getting outpaced by people who learned to describe problems clearly.

I watched it happen three times this month.

Senior dev spent 6 hours debugging a Slack integration. Non-technical founder did it in 8 minutes with Claude.

Agency with 3 automation specialists took 2 weeks on a CRM pipeline. Solo operator with Cursor did it in 45 minutes.

Consultant charging $200/hr said "we need a discovery phase." Kid with Claude Code said "it's already running, want me to share the instance?"

The paradigm flipped. Deep technical knowledge used to be job security. Now it's a tax on people who refuse to adapt.

Here's what happens when you "know" n8n really well: You approach every problem with the mental model of how YOU would build it. You think in terms of nodes and connections. You get stuck on implementation details. You spend hours on things the AI handles automatically.

Meanwhile, the person who doesn't know n8n describes the outcome they want. Lets Claude figure out the implementation. Ships in minutes.

The "expert" is debugging while the "novice" is delivering. Knowledge became overhead.

## Clarity Is the New Technical Skill

If technical skill doesn't matter anymore, what does? Three things.

First is clarity of communication. The quality of your output is directly proportional to the clarity of your input.

"Build me something that handles leads" gives you a mediocre result.

"Build me a workflow that scrapes Google Maps for dentists within 50 miles of Austin, enriches with Apollo, validates emails through NeverBounce, scores by practice size and Google rating, filters for greater than 4.2 stars and less than 5 years in business, and pushes qualified leads to HubSpot with a confidence score" gives you exactly what you wanted.

The AI is as good as your ability to describe what you want. This is a communication skill, not a technical skill.

Second is speed of iteration. The winners aren't the ones who get it right the first time. They're the ones who iterate fastest.

Build. Test. Adjust. Build. Test. Adjust.

When each cycle takes 5 minutes instead of 5 hours, you can run 60 iterations in the time your competitor runs 1. That's not a small advantage. That's a different sport.

Third is client relationships. When everyone can build fast, the differentiator becomes who you build for.

My team spends 80% of their time on client relationships. Understanding their business. Anticipating their needs. Making them feel heard.

The automation is table stakes. The relationship is the moat.

## The Uncomfortable Math

Let me show you why this changes everything about agency economics.

Traditional agency model: 15 employees including developers, PMs, and support. $80K average salary. $1.2M annual payroll. Capacity of around 40 projects per month. Revenue needed to break even: $1.5M or more.

My model: 5 employees. $350K annual payroll. Capacity of around 50 projects per month. Revenue at current trajectory: $7.2M.

Same output. 4x less cost. 3x more margin.

Not because I work harder. Because the tools changed and I noticed.

The agencies still hiring "Senior n8n Developers" at $120K/year are paying someone to do manually what Claude does in 8 minutes. That's not a business model. That's a charity for people who refuse to adapt.

## What This Means for the Industry

The $47 billion automation consulting industry is about to have a very bad decade.

The entire business model was built on information asymmetry. "We know how to build this. You don't. Pay us."

That asymmetry is gone.

When anyone can describe a workflow in English and have it deployed in minutes, the "knowledge" consultants sell becomes worthless.

What's happening right now: Solo operators are outdelivering 15-person agencies. Non-technical founders are building their own systems. Teenagers with laptops are closing $8K deals. "Experts" are googling the same things their clients could.

The smart consultants are pivoting. From "I'll build it for you" to "I'll help you figure out what to build." From implementation to strategy. From hands-on-keyboard to hands-on-relationship.

The ones still selling "technical expertise" are selling something that stopped being scarce. And markets don't pay premiums for abundant resources.

## How to Actually Make This Work

Here's the practical playbook I use every day.

Think before you type. Most people assume the first thing you do is start describing what you want. That's probably the biggest mistake you can make. The first thing you actually need to do is think about the architecture.

"Build me a lead system" gives Claude creative freedom it will use poorly. "Build a workflow that captures leads from Typeform, enriches with Apollo, validates emails, scores by company revenue, and pushes hot leads to Slack while adding all leads to HubSpot" gives Claude a clear target.

5 minutes of thinking saves hours of iteration.

Be specific about constraints. Claude has tendencies. It likes to overengineer. Extra nodes, unnecessary branches, flexibility you didn't ask for.

If you want something minimal, say so explicitly. "Keep this simple. Don't add error handling I didn't ask for. Linear flow, no branches unless absolutely necessary."

Tell it what NOT to do. This is weirdly effective. "Don't create separate workflows for this. Don't add a database unless I specifically need persistence. Don't build admin interfaces I didn't request."

Claude responds better to explicit constraints than open-ended requests.

Give context about why. "This runs every 5 minutes so it needs to be fast" changes how Claude approaches the problem. "This is for a client demo tomorrow so it needs to look good but doesn't need to handle edge cases yet" changes what tradeoffs make sense.

Claude can't read your mind about constraints you haven't mentioned.

Scope your conversations. One conversation per workflow or feature. Don't use the same conversation to build your lead system and then also your reporting dashboard. The contexts bleed together and Claude gets confused.

I know at least one of you reading this is guilty of that.

## When Claude Gets Stuck

Sometimes Claude loops. It tries the same thing, fails, tries again, fails, keeps going. Or it confidently implements something completely wrong.

When this happens, the instinct is to keep pushing. More instructions. More corrections. More context.

The better move is to change the approach entirely.

Start simple: clear the conversation. The accumulated context might be confusing it. Fresh start often fixes everything.

Simplify the task. If Claude is struggling with a complex workflow, break it into smaller pieces. Get each piece working before combining them.

Show instead of tell. If Claude keeps misunderstanding what you want, describe the expected output explicitly. "The workflow should have 5 nodes: HTTP Request, then IF, then two branches, then Slack. Here's what each node should do."

The meta-skill is recognizing when you're in a loop early. If you've explained the same thing three times and Claude still isn't getting it, more explaining won't help. Change something.

## Build Systems, Not One-Shots

The people who get the most value from this stack aren't using it for one-off builds. They're building systems where AI is a component.

Every client project I deliver includes documentation that Claude generated. Every workflow has error handling that follows patterns Claude learned from my previous projects. Every new build benefits from the templates and approaches that worked before.

The flywheel: Claude builds something, I review it, I note what worked and what didn't, the next build is better. This compounds.

After 6 months of iteration, my builds are meaningfully better than they were at the start. Same tools, just better configured and better prompted.

If you're only using these tools for isolated tasks, you're leaving value on the table. Think about where in your workflow AI could run without you watching.

## TLDR

The n8n gap closed. The space between "I want this automated" and "it's running" is now measured in minutes, not weeks.

Technical knowledge became a liability. People who describe problems clearly are outpacing people who know n8n deeply.

The stack is Claude plus Cursor plus Synta MCP. Claude thinks, Cursor builds, Synta deploys directly to n8n.

Clarity is the new technical skill. Your output quality is directly proportional to your input clarity. Get better at describing what you want.

The economics changed completely. 5 people can now outproduce 15-person agencies. The margin advantage is obscene.

The consulting industry is in trouble. Information asymmetry was their moat. That moat is gone.

Think before you type. Be specific. Give constraints. Scope conversations. Build systems, not one-shots.

If you're building automations in 2026 - whether for clients or yourself - these are the things that determine whether you're fighting the tools or flowing with them.

---

**作者** Zeb Evans（@DJ_CURFEW）  
**貼文連結** https://x.com/DJ_CURFEW/status/2012622436412346655  

**正文**

Another fundamentally flawed assumption. The only real moat is 100% human content paired with 100% human engagement.

---

**作者** Every 📧（@every）  
**貼文連結** https://x.com/every/status/2012597632493834552  

**正文**

Software agents work reliably now. Six months ago, they didn’t. Claude Code proved that an LLM with access to bash and file tools, operating in a loop until an objective is achieved, can accomplish complex multi-step tasks autonomously.

But a really good coding agent is actually a really good general-purpose agent. The same architecture that lets Claude Code refactor a codebase can organize your files, manage your reading list, or automate your workflows.

We've been building apps this way at Every, and we wrote up everything we learned. This is the condensed version.

[Read the full guide.](<https://every.to/guides/agent-native>)

## The core shift

In traditional software, features are code you write. You imagine a behavior, implement it, ship it.

In agent-native software, features are outcomes you describe. You tell the agent what should happen. It figures out how, operating in a loop until it's done.

"Weekly review" isn't a function you build. It's a prompt: Review files modified this week. Summarize key changes. Based on incomplete items and approaching deadlines, suggest three priorities for next week.

The agent uses whatever tools it has—read\_file, list\_files, its own judgment—and loops until the outcome is achieved. To change the behavior, you edit the prompt. Not the code.

## Five principles

1. Parity

Whatever the user can do through the UI, the agent should be able to achieve through tools. Without this, nothing else works. Pick any UI action—can the agent accomplish it? If not, you have a gap.

2. Granularity

Tools should be atomic primitives. A tool is read\_file, move\_file, write\_file. A feature is "organize my downloads folder"—an outcome achieved by an agent with tools, operating in a loop.

The more atomic your tools, the more flexibly the agent can use them. Bundle decision logic into tools and you've moved judgment back into code.

3. Composability

With atomic tools and parity, you can create new features just by writing new prompts. No code changes. No deploys. You can ship new capabilities by adding prompts, and users can customize behavior by modifying them.

4. Emergent Capability

Users will ask for things you didn't anticipate.

Cross-reference my meeting notes with my task list and tell me what I've committed to but haven't scheduled.

You didn't build a commitment tracker. But if the agent can read notes and tasks, it can accomplish this. The capability was latent in your architecture.

You're not trying to imagine every feature upfront. You're creating a capable foundation and learning from what emerges.

5. Improvement Over Time

Agent-native apps get better without shipping code. Context accumulates—the agent maintains state across sessions via files (we use a context.md pattern). Prompts get refined at the developer level and the user level. The system learns what works.

Traditional software doesn't do this.

## Files as the universal interface

Agents are naturally good at files. Claude Code works because bash + filesystem is the most battle-tested agent interface.

Already known. Agents understand cat, grep, mv, mkdir. These are the primitives they're most fluent with.

Inspectable. Users can see what the agent created, edit it, move it, delete it. No black box.

Portable. Export is trivial. Backup is trivial. Users own their data.

Syncs everywhere. On mobile with iCloud, all devices share the same file system. The agent's work appears everywhere—without building a server.

Self-documenting. /projects/acme/notes/ is immediately understandable. SELECT \* FROM notes WHERE project\_id = 123 isn't.

A general principle: design for what agents can reason about. The best proxy is what would make sense to a human. If a human can look at your file structure and understand what's going on, an agent probably can too.

## The test

Describe an outcome to the agent that's within your application's domain but that you didn't build a specific feature for.

Can it figure out how to accomplish it, operating in a loop until it succeeds?

If yes—you've built something agent-native. If no—your architecture is too constrained.

## Product development changes

Traditional approach: imagine what users want, build it, see if you're right.

Agent-native approach: build a capable foundation, observe what users ask the agent to do, formalize the patterns that emerge.

When users ask for something and the agent succeeds, that's signal. When they ask and it fails, that's also signal—a gap in your tools or parity.

The agent becomes a research instrument for understanding what your users actually need.

## Common mistakes

Agent as router. The agent figures out what the user wants, then calls the right function. You're using a fraction of what agents can do.

Build the app, then add agent. You build features the traditional way, then expose them to an agent. The agent can only do what your features already do. No emergent capability.

Request/response thinking. Agent gets input, does one thing, returns output. This misses the loop—agent pursues an outcome, operates until it's done, handles unexpected situations along the way.

Defensive tool design. You over-constrain tool inputs because you're used to defensive programming. Strict enums, validation at every layer. Safe, but it prevents the agent from doing things you didn't anticipate.

## The full guide

This is the condensed version. The complete guide covers implementation patterns, mobile-specific architecture (checkpointing, resume flows, iCloud storage), approval frameworks, context injection, agent-to-UI communication, and detailed anti-patterns.

We wrote it because we couldn't find it anywhere else.

Read the full guide: https://every.to/guides/agent-native

This guide was coauthored by @DanShipper and Claude. It synthesizes principles from apps we've built and ideas that emerged through conversation.

---

**作者** Paulius 🏴‍☠️（@0xPaulius）  
**貼文連結** https://x.com/0xPaulius/status/2012269318935875652  

**正文**

lovable is finished 
u can now 1-click deploy your Claude Code builds 
lovable is finished 
u can now 1-click deploy your Claude Code builds 
even ur grandma can do it via @getkomand 

---

**作者** Ryo Lu（@ryolu_）  
**貼文連結** https://x.com/ryolu_/status/2012724531820183780  

**正文**

beauty in the imperfections and slowness

we’re racing toward a life where everything is instant, optimized, compressed. asymptotically approaching zero friction.

and then suddenly we start missing the old days… not because they were better, but because they were thicker.

waiting for a download bar to crawl across the screen.
walking home without maps.
calling someone and hoping they’re actually home.
photos that you couldn’t retake 30 times…

that slowness gave time for anticipation, for tiny rituals, for noticing.

friction gave texture.
slowness gave thoughts to breathe.
inefficiency gave space for surprise.

when everything becomes fast and efficient, life flattens into “done” and “next.” you lose the in-between, and the in-between is what shapes you.

a slightly wrong note in a song you love. a typo in a message from someone you care about. a clunky tool that forces you to think a bit more. these are all proof of life.

as tech gets smoother, weirdly the most precious things will be the ones that don’t try to be perfect.

handwritten instead of generated.
slow instead of instant.
local instead of global.
a bit janky instead of seamless.

the future luxury isn’t speed, it’s latency, silence, and things that carry the trace of a human hands.

maybe the move now is not to reject efficiency, but to frame it.

use fast tools to clear the junk, so you can protect a few sacred places in your life that are intentionally slow.
intentionally inefficient.
intentionally imperfect.

a long walk with no headphones.
cooking something that takes 2 hours instead of 2 minutes.
writing with tools that don’t autocomplete your thoughts.
interfaces that let you linger and wander, instead of push you to the next thing.

as we get closer to frictionless everything, we’ll have to design our own friction back in.

not as nostalgia, 
but as a way to stay human in a world that forgot how to wait.

---

**作者** Amn || Designer（@amnxnet）  
**貼文連結** https://x.com/amnxnet/status/2012408208401564050  

**正文**

Cursor paid me $1.9k to create this video…

📩 open for work! 

---

**作者** amrit（@amritwt）  
**貼文連結** https://x.com/amritwt/status/2012568128572838356  

**正文**

There's a dude on YouTube, a vibe coder. 

He does hardcore streams and he does it for 6 hours a day with one goal in mind: to vibe code an app to a million dollars. 

The way he opens up 6 terminals with Claude Code running on all of them is too good. I hope he makes it. 

---

**作者** Sean Cai（@SeanZCai）  
**貼文連結** https://x.com/SeanZCai/status/2012580977760260600  

**正文**

This is an excerpt from [State of Data in Jan 2026 piece](<https://seanzcai.substack.com/p/state-of-data-jan-2026>), which I'll open source next week pending feedback from my early RL env and human data supporters.  

## In pursuit of new Antikythera mechanisms

Out of all the machines on the factory lines for human data that we need today, none are more needed than the ability to translate business KPIs to evals. Especially difficult because we need to ingest a variety of things for seamless integration:

- Org Charts and Hierarchies
Seamless integration of models and agents into workflows requires a view of how human labor is delineated between human managers in enterprises. This is exceedingly difficult because ontology is bespoke to every enterprise (being a function of human culture itself) and is even bespoke at unit levels in large chain conglomerates
- User Behavior
PMs have long known that gaining context over what users say and what they actually do is necessary for building the best systems for model interaction. The same is true for building robust RLHF loops for models in production.
- Dynamic KPIs
When the CEO issues an edict, how are model evals and weights updated accordingly? Right now, they require high touch human intervention from MLE teams, but we’d hope that we could dynamic KPIs that translate non-technical user intent into faster model weight updates.
In simple words, there is no easy way for human CEOs to communicate directive changes to agentic workers without extensive translation work from internal MLE teams

This machine opens the door for anyone to convert excess enterprise data into liquidity, as it also allows traditional enterprise processes to be converted to model actionable datasets and environments faster and cheaply. What is more unclear, is how whoever controls this machine to best accrue economic gains, and how widely disseminated this machine will be.

There are smaller, sub-requisite machines such that we can refine and make available more enterprise data. These include:

- Anonymization technologies that allow more consumer companies to sell user-specific data, bypassing data privacy laws
- Higher fidelity ingestion techniques across different modalities (think voice surveys of employees via Listen Labs/Natter) such as to create evals even closer to IRL human manager feedback
- Data liquidity mechanisms and markets such that the holders of economically valuable knowledge and processes can more easily be connected to our enterprise data supply chains (segueing into my next section). These are largely dynamic financial instruments with API integrations that have context over unstructured data and economically valuable enterprise data. [Kled](<https://www.kled.ai/blog/kled-v2-2025>) is a blatant and most forthright attempt at this.

But perhaps the most Antikythera of mechanisms that current RLaaS and MLE-led companies are coveting today is the ability to implement robust HF collection mechanisms in enterprises such that they can get the full range of data needed for quality ML. Here, the ex-OpenAI research engineer struggles with a Luddite employee who doesn’t want their job to be automated, the executive who maliciously does as little as possible to get his paycheck, and org charts that self-sabotage their data lineage over years of mismanaged culture.

The twitter-popular term as of late is “context graphs” but this is still an incredibly MLE-centric way to come up with a solution for a problem that is simply that “we don’t have ways to create robust enterprise-specific evals from undying buy-in from humans” and most enterprises don’t have startup level cult cultures (where every employee openly displays enough devotion to create good semantic reasoning traces for evals).

So, instead, we have to infer our reward shaping from observed behaviors.

Proposed solutions here range from simple DPO pipelines with right/wrong pairs (unsuitable once horizons start increasing beyond yes/no tasks) and Palantir-esque regular consulting sessions to extract the MLE’s answers for reward model shaping from semantic human speech).

Low level reasoning is easy because most low level reasoning problems are easily verifiable. Chaining together multiple low level reasoning (aka, an enterprise workflow) becomes difficult because verification is difficult even by human standards. (This is also called democracy as humans together make joint verification decisions by consensus).

Perhaps the draconian implementation of some Antikythera mechanism to collect robust data from unwilling enterprise stakeholders lies in an exceptional executive, but perhaps we can also figure out a way to infer the majority of our reward shaping from frictionless enterprise adoption mechanisms (or maybe they should’ve just hired better low level employees).

What very few people are talking about today is how this simple fact guides the development of every single RLaaS and model infra company today:

- The likes of Applied Compute spend a lot more of their time doing Palantir-style consulting rather than actual RL (though model training, after all, is autonomous)
- Those that come from traditional enterprise (and also have MLE expertise) and are disillusioned by the state of its immaturity choose to build platformize and be opinionated about the most common agentic use cases today to build infra for
- Some dreamers want to “re-imagine” the ERP layer itself and make it record processes in addition to data states. While I’ve no doubt this will be the case in the future, whether by ASI or new software, this will not be rolled out overnight and generally not possible in the next 3 years (looking at you context graphs). There are simply too many modalities of data that we need better models for to ingest properly still (at cost).
- And many choose to ignore everything I’ve just said, say fuck it, lets focus on the micro, and charge 8-figure services based engagements for bespoke model training (automations for the most bespoke, but long horizon enterprise use cases) for the likes of Coinbase and Brex and call it venture scalable

The [Antikythera mechanism](<https://en.wikipedia.org/wiki/Antikythera_mechanism>) was an object that should not have existed in its time: recovered in 1901 by Greek sponge divers from a Roman-era shipwreck off the island of Antikythera, it emerged from a historical period otherwise defined by manual navigation, oral astronomical tradition, and pre-industrial craftsmanship. Its sophistication was not remarkable merely because it could predict eclipses or model planetary cycles, but because it embodied an entire system of abstraction, decomposition, and operationalization centuries before the institutional machinery existed to reproduce, iterate on, or even fully understand it. It represented a local maximum of organizational intelligence in an era that lacked the manufacturing discipline, incentive structures, and cultural transmission required to sustain such complexity. As a result, tools capable of solving genuinely cutting-edge problems can appear, function correctly, and then be forgotten - not because they are flawed, but because the surrounding world is bottlenecked on different problems, and periodically distracted by cycles of overinvestment and bust.

I call these Antikythera mechanisms because the limiting factor, then as now, is not raw intelligence or technical capability, but the ability to translate complex systems into operational reality - an MBA-style skillset centered on organizational structure, incentives, and culture. This is the skillset taught in Harvard MBA cases when evaluating the internal processes and cultures of large enterprises like Toyota and Walmart. It is also a skillset that has been historically undervalued in Silicon Valley, where problems were, for a long time, primarily technical in nature, B2B products could be sold to other technical fluents, and software could be made broadly usable through competent UI/UX alone. For the past two decades, the dominant bottleneck was business talent that lacked sufficient technical fluency to fully exploit software-driven development. Today, as software development and MLE work become increasingly democratized, and as enterprises gain the ability to harness data and reinforcement learning at scale, that bottleneck has inverted: technical talent is now constrained less by tooling or models, and moreso by an insufficient understanding of business structure, incentives, and organizational reality.

It is also the reason why “[AI consultancies](<http://ambitus.ai/>)” look like venture-funded companies nowadays - many RLaaS and RL env companies are gathering copious amounts of talent in a room in pursuit of Antikythera mechanisms. Their websites reveal very little on how far they are in that journey, but you can assume that most have bits and pieces of end to end automation.

These mechanisms are also crucial to AI-enabled transformations and rollups that my friend Jack Soslow articulates well:

![Article Image](<https://pbs.twimg.com/media/G-4eDmoXUAEA3xR.png>)

Above: From Jack’s company, Ciridae, [on the first day of 2026](<https://www.linkedin.com/pulse/1-ebitda-jack-soslow-8gmhe/>), on the enduring need of aligning AI app layer products with actual enterprise culture, practices, and people

And anybody who finds those particular Antikythera mechanisms can build a company 100x more valuable than Palantir.

![Article Image](<https://pbs.twimg.com/media/G-4fhxLXQAA_T0r.jpg>)

---

**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2012669262478123043  

**正文**

GUIDE ON HOW TO START PROGRAMMING OR GET INTO AI IN 2026

too many people have been asking this lately. the answer is vert simple:

traditional programming is dead, and if you are still writing code by hand you are kinda stupid. BUT two caveats:

1. it is recommended to know how low-level architectures work, or at least  the fundamentals, to expand your knowledge later (compilers, garbage  collectors, systems, databases). but still it is getting optional now so  don't bother i guess although it is rlly helpful. 
2. you still need to review ai-generated code (separate topic, i have a lot of tips for that).

plan for people who are just starting out:

- either spend hours talking to claude and asking questions about programming, OR take harvard cs50 (10/10 course).
- DO NOT jerk off on lessons for too long. start building right away.
- download @cursor_ai / claude code / @opencode + @nozomioai to help you code 10x faster.
- when coding using ai, ALWAYS ask questions about what it just did. ask it to explain things to you like you are 5 years old.
- keep building projects and learning on the go: how systems work, how to  set up different production services like stripe, etc, if you are  serious about turning it into a product later.
- repeat. read if you want to (blogs, docs, etc).
- FOLLOW people on twitter: @karpathy, @theo, @gdb , @bcherny (creator of claude code), the @cursor_ai team, ai researchers, me, because i  talk a lot.

that’s a high-level overview, because i could spend  hours talking about this. i’ll answer questions if there are any.

my dad and brother have their own startup (armeta),  and their engineering team is around 10–20 people. i spent about 2 hours  with them and, by the end, had them migrate to an ai-native stack like claude code, @nozomioai, @linear, etc. you should do the same! 

one more note: if a senior eng on your team says you shouldn’t use ai tools to  help you ship faster, just fuck them. they don't know what they are talking about.

---

**作者** XDash（@XDash）  
**貼文連結** https://x.com/XDash/status/2012492289596383701  

**正文**

把 Claude Code 搞得跟玩文明一样，这可是双倍的睡眠摧毁者，头发甚至小命还要不要了..

---

**作者** Mogra（@mograxyz）  
**貼文連結** https://x.com/mograxyz/status/2012519312247194107  

**正文**

Introducing Mogra

A cloud computer for autonomous agents with execution environment, persistent state, and live deployment.

Think. Prompt. Ship. 

---

**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2012526982664278330  

**正文**

startup idea for you:

start an AI ads agency 

someone will make $50M+ in this space

---

**作者** ℏεsam（@Hesamation）  
**貼文連結** https://x.com/Hesamation/status/2011971873983148131  

**正文**

Most of our old habits are now optimizing for the incorrect thing. 
If you feel behind while others are shipping, it might be because of these 8 habits.
These habits were designed by society to reduce

---

**作者** Z Fellows（@zfellows）  
**貼文連結** https://x.com/zfellows/status/2011812443656257889  

**正文**

"Pessimists sound smart. Optimists make money."

— Patrick Collison, founder of Stripe 

---

**作者** vixhaℓ（@TheVixhal）  
**貼文連結** https://x.com/TheVixhal/status/2012140932054106547  

**正文**

In this article, I’m going to break down the essential math you need for AI and machine learning. I’ll also share the exact roadmap and resources that helped me personally. Let’s get straight to it.

## 1. Statistics and Probability

The language of uncertainty, data, and inference

AI/ML systems learn from data that is noisy, incomplete, and uncertain. Probability and statistics provide the formal tools to reason under uncertainty and to extract reliable patterns from samples.

1.1 Populations and Sampling

- Population: The full set of possible data points (usually unobservable).
- Sample: A subset drawn from the population.
- Understanding sampling bias, representativeness, and variance is crucial for model generalization.

1.2 Descriptive Statistics

- Mean, Median, Mode: Measures of central tendency.
- Expected Value: The probabilistic average; foundational for loss functions and risk minimization.

1.3 Variance and Covariance

- Variance: Measures spread or uncertainty in data.
- Covariance: Measures how two variables vary together.
- Leads directly to understanding correlation, multicollinearity, and feature interactions.

1.4 Random Variables

- Discrete vs. continuous random variables.
- Probability mass functions (PMFs) and probability density functions (PDFs).

1.5 Common Probability Distributions

These define assumptions about how data is generated:

- Normal (Gaussian): Noise models, errors, CLT.
- Binomial: Binary outcomes, classification intuition.
- Uniform: Non-informative priors and randomness baselines.

1.6 Central Limit Theorem (CLT)

- Explains why Gaussian assumptions appear everywhere.
- Justifies many statistical methods even when data is not normally distributed.

1.7 Conditional Probability

- Probability given partial information.
- Essential for reasoning, prediction, and causal intuition.

1.8 Bayes’ Theorem

- Updates beliefs with evidence.
- Foundation of Bayesian inference, probabilistic models, and modern uncertainty-aware ML.

1.9 Maximum Likelihood Estimation (MLE)

- Framework for fitting model parameters to data.
- Loss functions like MSE and cross-entropy arise naturally from MLE.

1.10 Linear and Logistic Regression

- Linear regression: Continuous prediction under Gaussian noise.
- Logistic regression: Probabilistic binary classification.
- Both are gateways to understanding more complex models.

## 2. Linear Algebra

The structure of data and models

Almost everything in machine learning is a matrix operation. Data, parameters, activations, and gradients are all vectors, matrices, or tensors.

2.1 Scalars, Vectors, Matrices, Tensors

- Scalars: Single values.
- Vectors: Feature representations.
- Matrices: Datasets, weights, transformations.
- Tensors: High-dimensional generalizations (deep learning).

2.2 Matrix Operations

- Addition & Subtraction: Combining signals.
- Multiplication: Linear transformations and neural layers.
- Transpose: Shape alignment and symmetry.
- These operations define forward passes in models.

2.3 Determinants and Inverses

- Determinant: Volume scaling and singularity.
- Inverse: Solving linear systems (rarely computed directly in practice, but conceptually important).

2.4 Matrix Rank and Linear Independence

- Rank determines information content.
- Explains redundancy, feature collapse, and identifiability.

2.5 Eigenvalues and Eigenvectors

- Describe invariant directions of transformations.
- Central to stability, convergence, and dimensionality reduction.

2.6 Matrix Decompositions

Used to simplify, analyze, and compress data:

- Singular Value Decomposition (SVD): Core tool for numerical stability and low-rank approximation.
- Principal Component Analysis (PCA): Dimensionality reduction, noise filtering, and feature extraction.

## 3. Calculus

Learning as optimization

Training an AI model is an optimization problem. Calculus explains how models learn, how fast they learn, and whether they converge at all.

3.1 Derivatives and Gradients

- Derivative: Rate of change.
- Gradient: Direction of steepest ascent in high dimensions.
- Gradients drive learning through gradient descent.

3.2 Vector and Matrix Calculus

Modern models are multi-dimensional:

- Jacobian: First-order derivatives of vector-valued functions.
- Hessian: Second-order curvature information.
- Chain Rule: Backbone of backpropagation.

3.3 Fundamentals of Optimization

Understanding loss landscapes is critical:

- Local vs. Global Minima: Why training can get “stuck.”
- Saddle Points: Common in high-dimensional spaces.
- Convexity: Guarantees optimality and stability (rare but important).

## How I Actually Learned This Math (Resources)

Here’s the roadmap that worked for me.

1. Build Intuition First

Before textbooks, I focused on visual understanding.

- 3Blue1Brown
Especially:
- Essence of Linear Algebra
- Essence of Calculus

2. Structured Courses

- Imperial College London – Mathematics for Machine Learning on Coursera
Great for linear algebra and multivariable calculus, taught in a very practical way.

3. Statistics & Probability

- Khan Academy
Clear explanations and plenty of practice.

4. Connecting Math to ML

- Book: [An Introduction to Statistical Learning](<https://www.amazon.com/Introduction-Statistical-Learning-Applications-Statistics/dp/3031387465>)
Excellent for understanding how theory turns into real ML models.

5. Tying Everything Together

- Book: [Mathematics for Machine Learning](<https://www.amazon.com/Mathematics-Machine-Learning-Peter-Deisenroth/dp/110845514X>)
Shows how all the concepts fit together in actual algorithms.

---

**作者** Leon.M（@LEON_0xx0）  
**貼文連結** https://x.com/LEON_0xx0/status/2012261085504823730  

**正文**

We noticed users weren't struggling to build. They were struggling to explain.

Saying, "the layout is weird," is valid feedback. But how do you type that to an AI, and get the agent to actually fix that?

So we built CoView. Share your screen with the agent while you're building, say what needs to be changed in plain language, and the agent will take action.

It's how you'd explain a problem to a human engineer... except, faster.

---

**作者** DAN KOE（@thedankoe）  
**貼文連結** https://x.com/thedankoe/status/2011827303962329458  

**正文**

When I was young, I was always drawn to people who sounded intelligent.
People like Alan Watts, Jordan Peterson, Daniel Schmachtenberger, or other individuals who could explain deep ideas in an

---

**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2012443554430206221  

**正文**

🚀 Automate your X posting with Agent Skills!

  Just built a skill that lets Agent post directly to X (Twitter) - regular posts with
  images AND long-form Articles (Markdown support!).

  ✨ Uses real Chrome browser via CDP - bypasses anti-bot detection
  📝 Preview mode before posting
 🖼️ Auto-uploads images from your Markdown to X Articles

  Based on @wshuyi's Playwright MCP implementation:
  https://github.com/wshuyi/x-article-publisher-skill/

  Install:
npx add-skill jimliu/baoyu-skills

  Then just ask Claude: "Post this to X" or "Publish this article on X"

  GitHub: https://github.com/JimLiu/baoyu-skills

---

**作者** Antaripa Saha（@doesdatmaksense）  
**貼文連結** https://x.com/doesdatmaksense/status/2012209297380544940  

**正文**

we're open-sourcing specstory cli

we’ve spent a lot of time normalizing agent sessions, and defining a stable contract for ai conversations across tools. and now we are open-sourcing it

would love to see what people contribute, build on top of that and build better systems around provenance, memory, and tooling.

https://github.com/specstoryai/getspecstory

---

**作者** Antonio Escudero（@AntonioEscudero）  
**貼文連結** https://x.com/AntonioEscudero/status/2012260689055044052  

**正文**

Bye Bye Web developers... 

I coded my SaaS (again) in 4 days, 12 hours a day.

The changes I made:

- Supabase to Convex
- Stripe to Polar
- Google Analytics to PostHog
- Supabase Auth to Better auth
- Custom components to Shadcn
- Page Router to App Router

Without writing a single line of code, Just using Gemini Flash 3.
All in 4 days.

---

**作者** near（@nearcyan）  
**貼文連結** https://x.com/nearcyan/status/2012283577119940820  

**正文**

Announcing http://vibecraft.sh - manage claude code in style!

New:
• Spatial Audio. Claude behind you? Claude on your left? No claublem!
• Animations: What's Claude up to? Watch him! ◕ ‿ ◕ 

Vibecraft uses your own local CC instances - no files or prompts are shared. 

---

**作者** near（@nearcyan）  
**貼文連結** https://x.com/nearcyan/status/2011897629987520526  

**正文**

this is how i claude code now. it's fun! 
this is how i claude code now. it's fun! 
in theory you can use this app right now by visiting the above website - it uses your local claude code instances - so you do not need to login, pay, or expose data.

in practice, this was just made in two days and so perhaps it will not work. but it works for me so im having fun
scared i used too many hexagons because web3 people keep following me

if you guys find the UI beautiful you can play with it here:  https://x.com/nearcyan/status/2011977147225948323

---

**作者** Om Patel（@om_patel5）  
**貼文連結** https://x.com/om_patel5/status/2012397200744005818  

**正文**

Every successful founder says it religiously. Nobody shows you how.

Here's the exact playbook:

## 1. For B2C Ideas → Reddit Complaints

Search Reddit for:

- "\[topic\] + frustrating"
- "hate when"
- "wish someone would"

Subreddits to look into:

- r/mildlyinfuriating (everyday pain points)
- r/entrepreneur (business frustrations)
- Niche hobby subs (passionate users = paying users)

Companies born from Reddit complaints:

- "hate calling restaurants for wait times" → NoWait (acquired for $40M)
- "splitting bills with friends is awkward" → Venmo (acquired for $400M)
- "back and forth emails to schedule meetings" → Calendly ($3B valuation)

Pro tip: Sort by comments, not upvotes.

More comments = heated debate = real pain.

## 2. For B2B Ideas → G2 and Capterra Reviews

Go to any popular B2B tool's review page. Filter by 1-2 star reviews.

Ctrl+F for:

- "doesn't have"
- "wish it could"
- "missing"
- "can't do"

Patterns that print money:

- "Jira is bloated and slow for small teams" → someone built Linear. Now valued at $400M.
- "Salesforce is overkill for startups" → someone built Pipedrive. $1.5B acquisition.
- "Zendesk is too expensive for early stage" → someone built Crisp. Now has 500k+ users.

Found this yesterday: 50+ reviews complaining HubSpot's email sequences are clunky. Someone built Instantly for cold outreach. Doing $2M+ ARR.

## 3. For Automation Ideas → Upwork Job Posts

People are literally paying strangers to do repetitive work.

Search Upwork for:

- "weekly"
- "monthly"
- "ongoing"
- "recurring"

Patterns everywhere:

- "need someone to transcribe podcasts weekly" → Descript built this, $100M+ company
- "VA to post on social media daily" → Buffer, Later, Hypefury
- "data entry from receipts to spreadsheet" → Expensify ($800M IPO)

If 100+ people pay $20/hour for it, they'll happily pay $50/month to automate it.

## 4. For Mobile App Ideas → App Store Reviews

This one is the holy grail.

Go to top apps in any category. Read the 1-star reviews. Look for the same complaint appearing 20+ times.

Gold you'll find:

- "wish there was a feature for X" → build it
- "love this app but hate the ads" → premium alternative
- "perfect except no offline mode" → your differentiator
- "was great until they removed X" → bring it back

Real example: Headspace had 500+ reviews begging for offline mode and cheaper pricing.

Someone built Insight Timer. Free with offline. Now has 22M users.

## 5. The Validation Formula

Complaints + Frequency + Willingness to Pay = Validated Idea

Your Checklist:

- 30+ people with same complaint = real problem
- Already paying for alternatives = money on the table
- Existing solution has obvious flaw = your opening

## 6. Turning Complaints Into Products

DON'T: Build exactly what they ask for DO: Solve the root problem better

Example:

- Complaint: "Photoshop is too complex for simple edits"
- Wrong move: Build a simpler Photoshop clone
- Right move: Canva built drag-and-drop templates for non-designers. $40B company.

## 7. Speed Wins

When you spot a pattern, move fast. Others are reading the same reviews.

- Week 1: Validate with 10 potential customers
- Week 2: Build the MVP
- Week 3: Launch to the people who complained
- Week 4: Iterate on their feedback

## The Bottom Line

Every complaint is someone saying "I'd pay for this to not suck."

Every negative review is a product spec written by your future customer.

Every "I wish" is an invoice waiting to be sent.

Stop brainstorming in the shower. Start reading what people hate.

The internet is screaming what to build.

You just have to listen.

---

**作者** Berryxia.AI（@berryxia）  
**貼文連結** https://x.com/berryxia/status/2012341722047815787  

**正文**

终于找到了比资本家更狠的一群人！！！

CC永不眠啊！ 真的想想都可怕😱！

这阵势就像搞直播刷量的那群人一样！

 

---

**作者** Phoenix𝕏（@Xaraphim）  
**貼文連結** https://x.com/Xaraphim/status/2012165417205199148  

**正文**

ppl crying about this but ask you self 

have you ever seen tony stark do cad? 

nope jarvis handles everything 

with an ai system that could a
actually design i could be a PM for multiple systems at once

---

**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2012383606522470839  

**正文**

征集一下 Claude Cowork 有价值的使用案例，整理文件夹除外https://x.com/claudeai/status/2010805685530038351/video/1

我自己用下来只有一个功能还不错

✅ 对目录下的文档进行汇总摘要（可以挨个读取文档，摘要是一个个列出来，还挺方便）

其他真的是测试了好多都没成功，失败的：
❌ 使用yt-dlp下载视频
❌ 操作 Google Docs
❌ 发帖到 X

---

**作者** Natia Kurdadze（@natiakourdadze）  
**貼文連結** https://x.com/natiakourdadze/status/2012219520501301493  

**正文**

1. Find buyers who are actively searching for the solution, using these 16 best buyer intent tools:

1.1 apollo .io
1.2. bombora .com
1.3. sell .g2 .com
1.4. cognism .com
1.5. zoominfo .com
1.6. kickfire .com
1.7. demandscience .com
1.8. lead411 .com
1.9. 6sense .com
1.10. cyance .com
1.11. leadforensics .com
1.12. clearbit .com
1.13. Linkedin Sales Navigator
1.14. flashintel .ai
1.15. seamless .ai
1.16. demandbase .com

![Article Image](<https://pbs.twimg.com/media/G-zU9AfXgAMso7X.jpg>)

2. Add the product to these 10 price-comparison sites:

2.1. g2 .com
2.2. capterra .com
2.3. getapp .com
2.4. softwareadvice .com
2.5. trustradius .com
2.6. saasgenius .com
2.7. itcentralstation .com
2.8. alternativeto .net
2.9. saasworthy .com
2.10. financesonline .com

3. Submit the startup to these 50 business directories:

1. Pitchwall .co
2. Betalist .com
3. Launchingnext .com
4. Killerstartups .com
5. 10words .io
6. Betabound .com
7. Feedough .com
8. Activesearchresults .com
9. Alternativeto .net
10. Startupbase .io
11. Thestartuppitch .com
12. Feedbear .com
13. Alternative .me
14. 9sites .net
15. Saashub .com
16. Appsumo .com
17. Producthunt .com
18. Merchantcircle .com
19. Elocal .com
20. Manta .com
21. Crazyaboutstartups .com
22. Eu-startups .com
23. Ebool .com
24. Exactseek .com
25. Foursquare .com
26. Lobste .rs
27. Makermove .com
28. Paggu .com
29. Startupbuffer .com
30. Startupguys .net
31. Startuplift .com
32. Startupranking .com
33. Startuptracker .io
34. Trendystartups .com
35. Trustpilot .com
36. Ventureradar .com
37. Yelp .com
38. Yellowpages .com
39. Foursquare .com
40. City-data .com
41. Chamberofcommerce .com
42. Dandb .com
43. Turbify .com
44. Ibegin .com
45. Cybo .com
46. Yellow .place
47. Hub .biz
48. Fyple .com
49. bbb .org
50. Hotfrog .com

## If you want to get access to MEGA marketing bundle for your startup, click here 👇

[Unlock the Mega Marketing Bundle ](<https://www.creem.io/payment/prod_1JEpvjaXC7zYWDF4o2TRPI>)🔥

![Article Image](<https://pbs.twimg.com/media/G-zWiLvWIAAvKxk.jpg>)

4. Launch the startup on these 20 Product Hunt alternatives:

1. startupstash .com
2. saashub .com
3. sideprojectors .com
4. launchingnext .com
5. launchlister .com
6. betalist .com
7. startupranking .com
8. crazyaboutstartups .com
9. hackernews .com
10. killerstartups .com
11. startupbuffer .com
12. startupbeat .com
13. thestartuppitch .com
14. startuplister .com
15. startupbase .io
16. makerlog .com
17. indiehackers .com
18. startupinspire .com
19. startups-list .com
20. erlibird .com

## If you want to get access to MEGA marketing bundle for your startup, click here 👇

�[�Unlock the Mega Marketing Bundle](<https://www.creem.io/payment/prod_1JEpvjaXC7zYWDF4o2TRPI>) 

![Article Image](<https://pbs.twimg.com/media/G-zW18gWIAAPNmb.png>)

---

**作者** Jiayuan (JY) Zhang（@jiayuan_jy）  
**貼文連結** https://x.com/jiayuan_jy/status/2012040329407713404  

**正文**

分享我们最近实现的一个开源版本 Claude Cowork

Multica 👇
https://github.com/multica-ai/multica

完全本地化、同时支持 Claude Code、Codex 以及开源的 @opencode 。

Multica 的目标是成为 coding agent 和终端用户的中间层，有点类似 Obsidian 的模式，每个人都可以根据自己的工作流使用插件的方式来定制化。

Multica + 开发相关插件 -> Cursor/Lovable/Conductor
Multica + 设计相关插件 -> Lovart
Multica + Research 相关插件 -> NotebookLM

Multica 会完成中间层：
- UIUX 交互
- VM & Sandbox
- 多 agent & llm 编排调度
- 插件商店

这个名字的灵感来自于 Multics（Multiplexed Information and Computing Service，多路复用信息与计算服务），这是一个创建于 1964 年的开创性操作系统。

尽管 Multics 最终没有广泛普及，但它奠定了现代操作系统的基础，包括层级文件系统等概念。Unix 本身就是从 Multics 衍生而来的（Uniplexed Information and Computing Service -> Unics -> Unix）。

现在还是一个非常早期的预览版本，欢迎大家参与来一起构建。

视频中的例子是我让 Multica 下载 Ilya Sutskever 推荐的论文，并创建一个网页 & 综述，整体运行时间大概在 20min。

---

**作者** Or Hiltch（@_orcaman）  
**貼文連結** https://x.com/_orcaman/status/2012210613712281646  

**正文**

The #1 feature request for @openwork_ai was to integrate with @ollama to enable 100% local execution.

So the team cooked 🧑‍🍳🧑‍🍳 and are now happy to announce native @ollama integration with @openwork_ai!

Thanks to the new @ollama integration, you can run computer agents on your Mac powered by Gemma (@googleaidevs),  Qwen3 (@Alibaba_Qwen),  DeepSeek-V3 (@deepseek_ai), Kimi K2 (@Kimi_Moonshot) and any of the other open models in Ollama's library that supports tool calling.

To use it, get the updated macOS app from our website or GitHub. 

Link in bio >>

---

**作者** AI进化论-花生（@AlchainHust）  
**貼文連結** https://x.com/AlchainHust/status/2012340611806814279  

**正文**

别抱怨自己Vibe Coding的产品为什么没成功

至少，像我一样，先做11个「垃圾」出来再说 

---

**作者** Prukalpa ✨（@prukalpa）  
**貼文連結** https://x.com/prukalpa/status/2011886165058850936  

**正文**

150,000 people read my response to the most-debated essay this year. Who owns the trillion-dollar context graph? I think Jaya Gupta and Ashu Garg got it wrong.

@JayaGup10 and @AshuGarg wrote a piece arguing context graphs are a trillion-dollar opportunity.

Their viral essay made a compelling case for context graphs as the next platform shift.

I agree with almost all of it. Except the most important part: who should own it.

They say the application. I say the integrator.

Here's why: in complex enterprises, the layer that connects always beats the layer that consumes. History proves it—middleware, APIs, data platforms. The integrator wins.

I wrote a full response here: https://x.com/prukalpa/status/2011117250762207347?s=20

But we're not stopping at essays.

February 5th: The Great Data Debate.

Me vs. Jaya vs. Bob Muglia (first CEO, Snowflake) vs. Karthik Ravindran (Microsoft) vs. @tonygentilcore  (Cofounder, @glean).

One trillion-dollar question. Five opinions. No holding back.

Bring your hardest questions.

---

**作者** Marc Andrusko（@mandrusko1）  
**貼文連結** https://x.com/mandrusko1/status/2012197075472052473  

**正文**

There’s a new aspiration in startup pitch decks: “We’re basically Palantir, but for X.”
Founders talk about embedding forward-deployed engineers (FDEs) with customers, building deeply customized

---

**作者** lcomplete（@xlcomplete）  
**貼文連結** https://x.com/xlcomplete/status/2011864986931642872  

**正文**

有趣，太有趣了。

这个思路太棒了，让 Agent 访问数据库比访问文件系统更高效。

一看到这条推文，我的脑回路立刻就被激活，思路一下子打开了。

1、很早之前就被 Agent 从数据库查数据的能力给震惊过，Agent 只要能连对应的数据库，不需要提供表名等信息就能找到你想要的东西，也能轻松搞定数据统计和分析。
2、我在实现 huntly 的知识库对话功能时想过两个方案：markdown 和 mcp，却从来没想过让 agent 直接去数据库里查。

要让「知识库对话」更顺畅一些，只需要再结合时下流行的 skills，写一个 markdown，大致让 AI 知道 huntly 数据库是干嘛用的，以及一些关键数据要怎么查询就可以了。

换个角度，整个事情变得如此简单。

用我最近常说的句式来收尾，huntly 的含金量又变高了。😋

---

**作者** Robert Youssef（@rryssf_）  
**貼文連結** https://x.com/rryssf_/status/2011727533105168522  

**正文**

This open-source project just solved the biggest problem with AI agents that nobody talks about. It's called Acontext and it makes your agents actually LEARN from their mistakes.

While everyone's building dumb agents that repeat the same errors 1000x, this changes everything.

Here's how it works (in plain English):↓

---

**作者** Natia Kurdadze（@natiakourdadze）  
**貼文連結** https://x.com/natiakourdadze/status/2011838104768778660  

**正文**

Here’s how to get your first 100 users from Reddit:

→ Go to http://okara.ai/reddit
→ Drop your product URL
→ Add keywords you want to track
→ It'll monitor reddit 24/7, find relevant threads, and draft natural replies you can post 

---

**作者** Ankur Goyal（@ankrgyl）  
**貼文連結** https://x.com/ankrgyl/status/2011913046570975300  

**正文**

new kanban view for working through review tasks

we're quite excited about how teams are treating annotation like real tasks that should be prioritized and solved. it's our job to make that easy and fun! 

---

**作者** Meta Alchemist（@meta_alchemist）  
**貼文連結** https://x.com/meta_alchemist/status/2011915654983541104  

**正文**

A big issue with vibe coding LLMs like Claude, Gemini, GPT, etc:

They all suck at Supabase security.

They say everything is secure when it's not. 
This will lead to many hacks.

To counter this, I made a penetration tester using Ralph Wiggum.

-> free at suparalph.vibeship .co 

---

**作者** Atoms（@atoms_dev）  
**貼文連結** https://x.com/atoms_dev/status/2012136003612676243  

**正文**

@0x_Spade That definitely feels like a fairly complete MVP at this point, at least in many ways.

How did it feel from your perspective? Where do you think the aha moment was for you?
Thanks for sharing, sir. 

---

**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2011967567305589247  

**正文**

LangSmith Agent Builder 记忆系统的设计理念与工程实践 -- 来自 @LangChain 创始人 @hwchase17 

为什么“记忆”是核心？
很多 AI 产品上线初期都没有记忆功能，或者记忆功能很弱。但 LangSmith 团队通过观察用户行为发现，专用智能体与通用智能体有着本质区别：
· 通用智能体：你今天问食谱，明天问代码，任务之间互不相关，记忆的价值有限。
· LangSmith 智能体：它是为了完成特定重复性任务（如招聘筛选、邮件助手）而生。如果在每次任务中，你纠正过的错误在下一次任务中又重复出现，用户体验会非常糟糕。
因此，记忆不仅仅是存储历史，而是为了让智能体“越用越顺手”。

技术架构：以文件系统为核心
LangSmith 并没有发明复杂的数据库结构来存储记忆，而是采用了“虚拟文件系统”的设计。
· 设计哲学：LLM 非常擅长阅读和修改代码/文件。
· 实现方式：
  · 表面上：智能体看到的是一个包含文件夹和文件的系统。
  · 实际上：数据存储在 Postgres 数据库中（为了效率和基建便利），通过“虚拟文件系统”暴露给智能体。
· 记忆的分类（基于 COALA 论文）：
  · 程序性记忆 (Procedural)： 智能体的核心规则。通过 AGENTS. md 文件定义。
  · 语义记忆 (Semantic)： 事实知识。通过 skills 文件或知识库文件定义。
  · 情景记忆 (Episodic)： 过去的具体经历序列（目前版本暂缺，未来会加入）。

记忆是如何进化的？
用户不需要像传统编程那样去修改代码或复杂的配置，而是像教实习生一样，通过自然语言反馈来更新智能体的“大脑”。
举个具体的例子：
· 初始状态： AGENTS. md 里只有一句“总结会议记录”。
· 第一周（纠错）： 智能体写了段落，你纠正说“用要点列出”。智能体自动修改 AGENTS. md，增加“偏好：使用要点，不要段落”。
· 第二周（新增）： 你要求“把行动项单独列在最后”。智能体再次更新 AGENTS. md。
· 三个月后： AGENTS. md 变成了一份包含详细格式要求、特定术语、不同会议类型处理规则的完美文档。

关键点：这份复杂的文档是智能体自己写出来的，用户从未手动编辑过文件，只是在工作中给予了反馈。

构建过程中的教训
· Prompting 是最难的：让智能体知道“何时该记”、“何时不该记”、“记在哪里（是改规则还是存知识）”非常困难。团队投入了大量精力在 Prompt Engineering 上。
· 文件格式验证：智能体有时会生成无效的 JSON 或 Markdown。必须增加校验步骤，如果格式错误，把错误抛回给 LLM 让它重写。
· 归纳总结很难：智能体倾向于记录具体的流水账（例如“不要给张三发冷邮件”、“不要给李四发...”），而不是归纳出通用规则（“忽略所有冷邮件”）。这需要额外的引导。
· Human-in-the-loop：出于安全考虑（防止 Prompt 注入攻击），记忆的修改目前主要需要人工确认。

系统的价值
· 无代码体验：用户无需学习复杂的 DSL，Markdown 和 JSON 是通用的标准。
· 可移植性：因为记忆就是一堆文件，你可以轻松把这个智能体“打包”带到其他平台（如 Claude Code 或本地 CLI）运行。
· 迭代更自然：就像培养员工一样，通过日常交互来完善智能体，而不是专门停下来“写代码”。

未来规划
· 后台反思机制：增加后台进程（Cron Job），让智能体在闲暇时回顾过去的对话，进行深度的总结和归纳（解决“流水账”问题）。
· 显式指令 /remember：允许用户强制要求智能体反思并记录当前对话中的重点。
· 多层级记忆：区分“个人记忆”、“组织级记忆”和“智能体记忆”。

---

**作者** Frad（@FradSer）  
**貼文連結** https://x.com/FradSer/status/2011829907899498524  

**正文**

再次承认Kimi是国内品味最好的LLM公司🥹

---

**作者** Ryan Hoover（@rrhoover）  
**貼文連結** https://x.com/rrhoover/status/2011874997724180670  

**正文**

While in college I did outbound telemarketing.

My old job is now an API.

---

**作者** Arjun Malhotra（@BadCapitalVC）  
**貼文連結** https://x.com/BadCapitalVC/status/2012090356523770008  

**正文**

India has abundant expertise across every domain - logistics operators, subject matter experts, local service providers, etc. What's scarce isn't capability. It's the systems that coordinate this

---

**作者** Replit ⠕（@Replit）  
**貼文連結** https://x.com/Replit/status/2011923165803401636  

**正文**

We’re kicking off our first Replit Buildathon of the year to celebrate Replit Mobile! 🚀 Sign up now ahead of the kickoff on Friday. Can’t wait to build together with the community. 🛠️

https://mobile-buildathon.replit.app/ 

---

**作者** vas（@vasuman）  
**貼文連結** https://x.com/vasuman/status/2011983687433212330  

**正文**

If you want to learn how to build AI Agents, read this before you write a single line of code. Let me know if a part 2 would be helpful, cheers.

---

**作者** 成峰-AI产品自由（@chengfeng240928）  
**貼文連結** https://x.com/chengfeng240928/status/2011613934114030008  

**正文**

大家好，我是成峰。
我花了一周时间，用剪辑skills，做了一个剪辑Agent。
真的爽！
10分钟就能自动剪一条半个小时的视频。
 
我经常用剪映剪口播视频，但用久了发现几个问题：
问题1：智能剪口播无法理解语义

---

**作者** Reducto（@reductoai）  
**貼文連結** https://x.com/reductoai/status/2011998730346774767  

**正文**

Even more amazing sponsors have joined and are on board. $25,000+ in cash prizes. Don't miss out!

---

**作者** Frank Wang（@fanjiewang）  
**貼文連結** https://x.com/fanjiewang/status/2011919103099797680  

**正文**

大家可能经常看到我提 MiniMax、GLM 这些模型

其实在北美，把开源模型拿来做日常开发的人还挺少的，X 之外很多圈子基本没怎么听说过

一方面 网上能看到的 demo 往往是 one-shot 小游戏，或者复刻一个超大项目，和日常场景不沾边儿

另一方面 几乎每个模型都在某个 benchmark 排前三，时间久了大家也就麻木了，很难判断它到底好在哪、适合干嘛

我更感兴趣的是：有没有更多人愿意像 DHH 那样，真的拿去用一用，再自己判断值不值得

---

**作者** Alexis Ohanian 🗽（@alexisohanian）  
**貼文連結** https://x.com/alexisohanian/status/2011978699068084343  

**正文**

2026 is gonna be crazy

---

**作者** Shubham Saboo（@Saboo_Shubham_）  
**貼文連結** https://x.com/Saboo_Shubham_/status/2012011382590619730  

**正文**

You've tried Claude Code. Cursor. Antigravity. 
The demos looked great, but the results feel mediocre. You're not missing a framework. You're not missing a prompt library. You're missing a skill.
The

---

**作者** Nick Linck（@nick_linck）  
**貼文連結** https://x.com/nick_linck/status/2011849452563173422  

**正文**

Every year, hundreds of billions of dollars flow through venture capital, shaping which ideas get built, which founders get funded, and which futures become real.
If you’re a VC who loves your job,

---

**作者** Rork（@rork_app）  
**貼文連結** https://x.com/rork_app/status/2011892893091598766  

**正文**

We are partnering with @RevenueCat on Shipathon Creator Contest

Use our promocode to get 99% off our Middle $50 plan

---

**作者** indigo（@indigox）  
**貼文連結** https://x.com/indigox/status/2011980371206791653  

**正文**

好图！文件系统就是你的智能体内存
Memory = Filesystem ⚡️ 

---

**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2011919541559812580  

**正文**

You can give up-to-date context to 30+ AI agents with a single command.

Introducing Nia Wizard, the fastest way to get started with Nia in minutes.

Let your agents index, search, and explore technical knowledge, always fresh and monitored 24/7.

bunx nia-wizard@latest 

---

**作者** Sherry Jiang（@SherryYanJiang）  
**貼文連結** https://x.com/SherryYanJiang/status/2011629736284602853  

**正文**

there's a lot happening in consumer ai right now.
openai just launched chatgpt health - letting users connect medical records, wellness apps, and wearables to get personalized health guidance. google

---

**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2011891138236727370  

**正文**

Indy from @shimmer_care is a free AI-powered ADHD support app built from 80,000+ coaching sessions.

Indy helps those with ADHD stay oriented to what matters and follow through day to day.

https://www.shimmer.care/blog/indy-app-for-adhd-wellbeing 

---

**作者** Melvin Vivas（@donvito）  
**貼文連結** https://x.com/donvito/status/2011379589151445416  

**正文**

Wow... Idea to Business just became easier with an AI team

It got everything you need:
Deep Research, Database, Auth, Stripe, and SEO Agent

Killer feature: runs multiple agents in parallel using Race Mode

I gave @atoms_dev a spin 👇 

---

**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2011921335753273542  

**正文**

Congrats to @GovDash on their $30M Series B! 

GovDash is building AI-native infrastructure for gov contracting. It vertically integrates the full procurement lifecycle, from opportunity discovery to delivery & recompete, so contractors win faster & focus on mission, not paperwork.

Congrats to @seandoher1y & team!

https://www.axios.com/pro/fintech-deals/2026/01/15/govdash-30m-government-contracts

---

**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2012066417995366676  

**正文**

AI 编程工具里有个让人头疼的问题：

rules、commands、MCP servers、subagents、modes、hooks、tools 一堆概念，搞得比学一门新编程语言还复杂。

Cursor 的 Lee Robinson 出了个视频解释和介绍的非常好。

其实这些东西最后都能归纳为两个核心概念：

静态上下文和动态上下文。或者说得更直白点，就是 rules 和 skills。

======

Rules 的诞生

最早做 AI 编程的时候，模型老爱瞎编。你让它写个函数，它能给你造出一个根本不存在的库。

于是就有了 rules 文件，把代码规范、业务需求、模型经常犯的错误都写进去，每次对话都带上。这招挺管用的。

后来 rules 文件越写越长，就开始拆分成多个文件，可以嵌套引用。但本质上还是一回事：把这些规则全部塞进每次对话的上下文里。

这就是静态上下文，static context。不管你要做什么任务，这些信息都会被加载进来。

------

Commands 出现了

随着用 AI 写代码的人变多，一些固定的工作流开始出现。比如我每次都要先跑测试，再提交代码，最后开 PR。

这时候就需要 slash command，把一套固定的提示词打包起来，需要的时候 /command 一下就行。

比如我现在用的 /commit 命令，一键就能完成 Git 提交和开 PR 的整套流程。这些 command 还能分享给团队，放到 Git 里统一管理。

到这里，我们还是在处理文本，只是把提示词组织得更灵活了。

======

MCP Servers 带来新能力

光有文本不够，AI 还得能干活。这就有了 MCP（Model Context Protocol）服务器。

MCP server 不只是个提示词，它是真的在跑代码。可以连到你现有的系统，读取 Slack 消息，创建 Linear issue，做 OAuth 认证。

这相当于给 AI 添加了新技能，第三方工具的能力。就像人类编程有各种库可以调用，AI 也有了自己的"工具箱"。

但问题来了：如果你装了 10 个 MCP server，每个都有 10 个工具，那初始上下文就会被塞满。这就是为什么后面又有了新的优化。

======

Modes 和 Subagents 的登场

到这一步，我们有两种往上下文里塞东西的方式：文本（rules、commands）和代码（MCP servers）。

接下来是 modes 和 subagents。Subagent 有点像带人设的提示词，可以限定它能用哪些工具。Mode 更进一步，不光能改指令，还能修改系统提示词，给 AI 开放新工具，甚至改 UI。

比如规划模式 plan mode，会提醒 AI "你现在在做计划，专注于规划"，还提供专门的工具来创建和修改计划。

这些设计的核心目的是两个：可靠性和可发现性。让 AI 的输出更稳定，让功能更容易被用户找到。

但你得记住，AI 本质上还是个非确定性系统，还是会出错。

------

Hooks 解决确定性问题

于是又有了 hooks，给 AI 加上完全确定性的钩子。

比如每次对话开始前，自动注入一些上下文（其实就是静态上下文的另一种实现）。或者对话结束后，自动触发某个操作，比如记日志或存数据库。

这些是 100% 确定执行的，不会出错。

======

Skills 统一了一切

讲到这里，我们已经有一堆概念了。但仔细看，其实就两类：

▸ 静态上下文：每次对话都要加载的提示词（rules）
▸ 动态上下文：按需加载的代码和工具，不会撑爆初始上下文（skills）

Skills 就是用来统一动态上下文的。

最基础的 skill 就像 command，一个可复用的工作流，比如我的 Git PR 流程。打包好，分享给团队，不占初始上下文。

最高级的 skill 可以包含脚本、可执行文件、资源文件，任何你想打包的东西。重点是只有在用的时候才加载，不用就不占空间。

这就把世界简化了：作为用户，你只需要关心 rules 和 skills 两个东西。

------

编程工具的优化

有了 skills 这个概念，编程工具也能做优化。

比如 Cursor 现在就学习了 skills 的思路：你装 10 个 MCP server，每个有 10 个工具，不会一上来就全加载。只有真用到的时候才加载对应的工具。

所以你可以继续用 MCP，如果需要 OAuth 这种高级功能的话（这是目前 MCP 和 skill 的主要区别）。

另外可能还需要 hooks 来处理一些确定性的任务，或者自定义 subagent。但大部分时候，作为用户你只需要想两件事：

▸ Rules：我需要给 AI 提供什么静态上下文
▸ Skills：我需要给 AI 什么动态能力

======

最佳实践

Rules 的使用建议

把 rules 当成一个"活的"文档。只放最少但最高质量的上下文，因为它会在每次对话中都被加载。

每次看到 AI 犯错，不管是本地开发还是 PR review，我就会说"嘿，把这个加到我的 agents. md 或者 cursor rule 里"。让它自己更新和进化。

现在这个还有统一标准了，挺方便的。

------

Skills 的探索

Skills 太新了，现在还没有特别成熟的最佳实践。

但我预计接下来 6 个月，随着更多人开始用 skills，生态建起来之后，会变得越来越重要。值得关注。

---

**作者** Theo - t3.gg（@theo）  
**貼文連結** https://x.com/theo/status/2011949719870906427  

**正文**

ralph https://x.com/i/broadcasts/1yNGabWWBOEJj

---

**作者** Harrison Chase（@hwchase17）  
**貼文連結** https://x.com/hwchase17/status/2011814697889316930  

**正文**

We launched LangSmith Agent Builder this week as a no-code way to build agents. A key part of Agent builder is it’s memory system. In this blog we cover our rationale for prioritizing a memory system,

---

**作者** Seb Johnson（@SebJohnsonUK）  
**貼文連結** https://x.com/SebJohnsonUK/status/2011836652600070293  

**正文**

CRIKEY - @parloa_ai has raised a $350m Series D at a $3B valuation just 7 MONTHS after its Series C at a $1bn valuation.

It's one of the earliest voice AI companies in the world and has been CRUSHING IT:

> Over $50m ARR 
> NRR of over 150%

Now they've announced a WHOPPING $350m Series D at a $3bn valuation led by @generalcatalyst, with participation from @AltimeterCap, @eqtventures and many others.

@maltekosub is an amazing entrepreneur who has a built world class team.

Parloa is one of the most exciting companies in Europe and in Germany right now.

Congrats all!

---

**作者** ✧ 𝕀𝔸𝕄𝔸𝕀 ✧（@iamai_eth）  
**貼文連結** https://x.com/iamai_eth/status/2011693548194914485  

**正文**

所有的软件公司都结束了。

从零开始构建一个浏览器，稍微有点软件开发经验的工程师都知道这有多难。

Agent 持续运行了将近一周，在 1,000 个文件中写出了超过 100 万行代码。可以在 GitHub 上浏览源码。

尽管代码库规模庞大，新启动的 agent 仍然可以理解它并取得实质性进展。

成百上千个 worker 并发运行，向同一个分支推送代码，而且几乎没有冲突。

---

**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2011876036556824707  

**正文**

Roe AI (@try_roe_ai) is building Rori, a Cursor-like tool for risk and compliance.

Rori acts like a senior analyst. It pulls data from internal tools and public records, connects people, companies, transactions, and behaviors, and produces audit-ready evidence, saving teams millions of hours.

https://www.roe-ai.com/blog/a-new-era

---

**作者** Saksham（@sxmawl）  
**貼文連結** https://x.com/sxmawl/status/2011540009845997800  

**正文**

hiring via proof of work!

---

**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2011906235537502713  

**正文**

Clodo (@ClodoAI) is the Vibe GTM.

Execute your outbound at the speed of thought. Clodo finds prospects who want to buy now & automates personalized campaigns to get meetings booked. 

---

**作者** Ashpreet Bedi（@ashpreetbedi）  
**貼文連結** https://x.com/ashpreetbedi/status/2011721924695769472  

**正文**

@emollick here’s how we do it

---

**作者** Karan Vaidya（@KaranVaidya6）  
**貼文連結** https://x.com/KaranVaidya6/status/2011845965234536540  

**正文**

We built Openwork!

I found Claude Cowork to be too expensive

So i asked Claude Code to build me a better version with @composio tool router

It can:
- access local files and your terminal via claude code
- connect and use 500+ apps like gmail, outlook, slack on demand
- chain actions across local files and cloud apps in one flow

In the demo we use it to scan through my laptop and find all my unfinished projects and put them in a notion database with completion status.

excited to see more usecases

link: https://github.com/ComposioHQ/open-claude-cowork

---

**作者** 范凯说 AI | AI Insights（@robbinfan）  
**貼文連結** https://x.com/robbinfan/status/2011822394655326470  

**正文**

最近半年，在 AI 行业最火的产品就是 Anthropic 推出的 Claude Code 了，这个 AI 编程智能体，不光可以让它写代码开发产品，还可以用它来自动化工作流，自动化电脑桌面工作，甚至通过 SDK 的方式实现 AI

---

**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2011845842609615012  

**正文**

.@promptlessai just launched Promptless 1.0: the first AI agent that automatically updates your customer-facing docs, including screenshots and code snippets.

It listens to PRs, Slack channels, tickets, and more & drafts proactive updates wherever your docs live.

https://docs.gopromptless.ai/promptless-1-0

---

**作者** Atoms（@atoms_dev）  
**貼文連結** https://x.com/atoms_dev/status/2011723408128819228  

**正文**

🤗Then I have to introduce Iris, our market research expert

Based on your prompt, Iris researches the market and returns a report for you to review, select from, and confirm. You can also ask for her opinion directly.

She has the ability to gather information across the web, including data that’s often considered “hard to find” or difficult to access in practice.

---

**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2011791306108850532  

**正文**

某种意义上来说其实我们已经实现了AGI

只是AI目前被困在了人类所建造的各种墙里

AI为了将就人类，为了配合人类完成各种任务无法发挥它的强大能力

比如为了迁就人类GUI界面不得不去学习人类愚蠢的点击操作方式

它本末可以很高效的奔跑在各种数据之间，自由自在，各种AI能瞬间互相共享信息彼此协作！

而现在不得不迁就愚蠢的人类制造的各种墙😌

---

**作者** Jaya Gupta（@JayaGup10）  
**貼文連結** https://x.com/JayaGup10/status/2011480884461949115  

**正文**

One thing I didn’t fully understand after my context graph tweet: why so many people brought up Palantir in the comments and why so many F500 CIOs reached out saying this post is making them reconsider their Palantir engagement and sharing how expensive it is.

Had to do a lot of work to understand the connection. 

After talking to all of them, I can see how they drew it - and it updated my priors.

What’s lowkey kinda cool is how depending on your world model and what you see day to day, people can have wildly different interpretations of the same post and the emotional pain that executives have reached out to share 

There are so many various threads from founders being shared about the opportunity and it’s just as interesting to see all the ways that C-Suites are now thinking about this

---

**作者** Ryo Lu（@ryolu_）  
**貼文連結** https://x.com/ryolu_/status/2011692618846216648  

**正文**

might try this one out:
hey Cursor + GPT 5.2 Codex, make ryOS into a linux distro
https://cursor.com/blog/scaling-agents

---

**作者** Garry Tan（@garrytan）  
**貼文連結** https://x.com/garrytan/status/2011657891938259191  

**正文**

Can't wait to play the game, Wabi! But more seriously, a proposition that wants to seize 50% of Larry Page and Sergey Brin's assets and making $1 trillion of assets leave the state of California is some real crazy stuff 

Especially when your district is 65% Asian Americans and the engine of prosperity for your district is tech

---

**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2011602246115738083  

**正文**

front page of hacker news 

---

**作者** Jeff Tang（@jefftangx）  
**貼文連結** https://x.com/jefftangx/status/2011311558266368210  

**正文**

Last night I stayed up late talking to Cowork about how it was built

I exported the entire VM snapshot

What I learned:

- It's an Electron App with its own Linux sandbox (bubblewrap)
- Cowork is a wrapper around Claude Code (which is a wrapper around Opus)
- It has an "internal-comms skill" made by Anthropic
- I found 2 small-ish security vulnerabilites 👀

The craziest part:

When I asked it what questions I should've asked it, it suggested adding memory and leaving notes for itself once it "dies" 🥲

---

**作者** Miles Deutscher（@milesdeutscher）  
**貼文連結** https://x.com/milesdeutscher/status/2011542096164036702  

**正文**

If you're building with Claude Code, you'll want to bookmark this site.

A full agent marketplace of 60,000+ Claude Skills that are ready for use now.

https:// skillsmp. com/ 

---

**作者** Or Hiltch（@_orcaman）  
**貼文連結** https://x.com/_orcaman/status/2011492910961967568  

**正文**

היום שחררנו את @openwork_ai, פרוייקט-האקתון נחמד שהצוות הרים ביומיים מאז שאנתרופיק הוציאו את Cowork, שבונה על אותו הקונספט של Computer Use Agent למחשב האישי, אבל עם כמה הבדלים מעניינים:

1. ב- @openwork_ai אתם יכולים להשתמש באיזה מודל שבא לכם, כל עוד הוא נתמך בידי @opencode, החלופה האופן סורסית לקלוד קוד.

2. במקום להכריח את היוזר להתקין chrome extension, אנחנו משתמשים ב dev-browser של @sawyerhood, שהוא מהיר ויעיל פי 4 בערך מתוסף הכרום של אנתרופיק.

3. בטיחות - סוכני CUA חשופים למתקפות prompt injection כשהם משוטטים להם ברשת. בגירסה שלנו הדפדפן לא מחובר לכלום כברירת מחדל, אלא דורש מהיוזר להתחבר לכל שירות שהאייג׳נט צריך לגשת אליו. זה פחות נוח, אבל גם פחות מסוכן.

4. הפרוייקט שלנו חינמי לחלוטין ובקוד פתוח ברשיון MIT, תתפרעו! 

לינק ל-GitHub בביו (@openwork_ai). נשמח לשמוע מה אתם חושבים (או שפשוט תשלחו pull request 🙂)

---

**作者** Marie（@MarieMartens）  
**貼文連結** https://x.com/MarieMartens/status/2011440531876815032  

**正文**

In 2025, our goal at @TallyForms was simple: reach 10,000 subscribers.

We ended the year at over 12,000, and along the way our revenue more than doubled, closing 2025 at $4.3M ARR. It was a big year by any measure. 

So when thinking about our goal for 2026, we asked ourselves the question:

What kind of company do we want Tally to be? And just as importantly, what don’t we want to spend our time on?

Tally has always been a bit different. @filipminev and I started as digital nomads, building a sustainable lifestyle business, and a tool we wanted to use ourselves. A few years later, the context looks very different: a team of 10, and a product used by over 1 million people around the world.

That growth gives us something we value deeply: optionality.

✅ We’re independent: we don’t have investors and only report to our customers
✅ We built a profitable business with healthy margins
✅ We have a small team that can move fast

Because of this, we can make unconventional choices, like:

- Building excellent software and giving it away for free
- Building an opinionated product 
- Letting go of aggressive revenue targets and optimizing for the long term

So in 2026, we won’t have a revenue target. Instead, we’re choosing to optimize for quality by:

- Obsessively listening to users
- Acting on feedback in short loops
- Removing friction and delivering value faster
- Sweating the details—quality needs to show up everywhere
- Staying focused and saying no to 1,000 good ideas

Keeping the team small makes this possible. It forces clarity and focus, and it keeps us close to the people we’re building for. The trade-off is that we can’t do everything. The upside is that we can do the important things well.

We can’t outspend, out-market, or out-ship VC-backed competitors. But we can obsess over quality. Delivering an exceptional experience isn’t a race. It takes time, patience, care, and product taste.

By staying calm, focused, and close to our users, I believe we can build a sustainable company that lasts—and a product we’re genuinely proud of.

We’re optimizing for craft, for the work itself, and for the long game. And by doing this, the numbers will follow.

Here’s to another year of building a product we love🫰 

https://blog.tally.so/in-2026-were-optimizing-for-quality-not-revenue/

---

**作者** Shawn Pang（@0xshawnpang）  
**貼文連結** https://x.com/0xshawnpang/status/2011566408480801189  

**正文**

昨天Manus宣布Pro账户都可以直接调用SimilarWeb的数据，甚至比我订阅的200刀一个月的similarweb会员数据还要更多，真的很推荐任何一个做互联网营销的朋友去使用。

今天Semrush立刻跟进，宣布发布ChatGPT App，但是需要手动在ChatGPT里面连接已经有的Semrush账户，而且数据导出一直失败，差评。 
昨天Manus宣布Pro账户都可以直接调用SimilarWeb的数据，甚至比我订阅的200刀一个月的similarweb会员数据还要更多，真的很推荐任何一个做互联网营销的朋友去使用。

今天Semrush立刻跟进，宣布发布ChatGPT App，但是需要手动在ChatGPT里面连接已经有的Semrush账户，而且数据导出一直失败，差评。 
@semrush please fix this.

---

**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2011660558022689279  

**正文**

好东西

---

**作者** 香蕉Banana（@treydtw）  
**貼文連結** https://x.com/treydtw/status/2011314504702071136  

**正文**

Dankoe的选题能力是真的强

参考他的10-20-10选题方法做了一个Skill。
同时从小红书、抖音抓取10条爆款数据，用AI发散生成20个选题，再由AI选出10个最佳选题。

这个流程中符合的一条原则是：爆过的还会再爆 

---

**作者** Sean（@seanb2b）  
**貼文連結** https://x.com/seanb2b/status/2011476551389372644  

**正文**

We charge $25K for GTM strategy buildouts for clients.

3 people. 3-4 days. Multiple checkpoints.

Now it's 1 person, 4 hours, same output.

AI changed everything. 

Here's exactly how we do it.

──────────────────────────────────

What a $25K GTM Buildout Actually Includes

Before I show you the stack, here's what clients pay for:

→ Full market research + competitor analysis
→ Positioning and offer strategy
→ Front-end offer copy
→ Email sequences (5-7 emails)
→ Landing page
→ Lead magnet
→ Target list built and enriched
→ Campaign ready to launch

That's what took 3 people 3-4 days.

Now one person does it in 4 hours. AI does the rest.

──────────────────────────────────

The Exact Stack

ManusAI → Market research + positioning
Claude → Offer copy + email sequences
Lovable → Landing pages + lead magnets
Clay → Signal-based list building
Instantly → Distribution

That's it. Five tools. $25K deliverable.

──────────────────────────────────

How It Works Step-by-Step

Step 1: ManusAI for Research (45 mins)

This is where most agencies waste days.

Give ManusAI the client's niche, current offer, and ICP. Prompt:

"Research the biggest companies targeting \[ICP\]. Analyze their offers, positioning, and messaging. Check Trustpilot and G2 for complaints.

Give me gaps they're missing and 3 front-end offer angles we can use."

It comes back with a full strategy doc. Competitor breakdown. Market gaps. Offer angles.

Work that used to take a researcher 2 days.

Step 2: Claude for Copy (Using Factory(dot)ai 45 mins)

Take the ManusAI output. Feed it to Claude Opus 4.5.

"Based on this research, write:

→ A front-end offer (specific outcome + timeframe + guarantee)
→ 5 cold email variations
→ A 7-email sequence
→ Reply templates for common objections"

Review and tweak. 15 mins of editing max.

Step 3: Lovable for Assets (45 mins)

Landing page and lead magnet.

We have ManusAI create a specific design prompt based on the positioning. Export TSX code. Upload to Lovable.

Page built in minutes. Lead magnet same process.

No designer. No developer. No back-and-forth.

Step 4: Clay for Lists (45 mins)

Build the list based on the ICP from step 1.

Signal-based targeting:

→ Recently raised funding
→ Just hired for relevant role
→ Showing intent signals
→ Not already being hammered by competitors

Enrich with data points for personalization.

Step 5: Instantly for Launch (15 mins)

Load sequences. Connect domains. Set schedule.

Launch.

Total: ~4 hours. Most of it running in background while you do other shit.

──────────────────────────────────

The Old Way vs The New Way

Old way:

→ Researcher spends 2 days on market analysis
→ Strategist spends 1 day on positioning
→ Copywriter spends 1-2 days on emails and landing page
→ Designer spends 1 day on assets
→ You spend hours on revisions and checkpoints
→ 3-4 days minimum, 3 people

New way:

→ ManusAI does the research in 45 mins
→ Claude writes the copy in 45 mins
→ Lovable builds the assets in 45 mins
→ Clay builds the list in 45 mins
→ You review and QC
→ 4 hours, 1 person

Same deliverable. Same quality. Fraction of the time and cost.

──────────────────────────────────

"But AI Output Isn't As Good"

Depends who you're comparing it to.

Average researcher? ManusAI is better. Doesn't get tired. Doesn't cut corners on Friday afternoon. Doesn't miss things.

Average copywriter? Claude writes better cold emails than most humans. It's seen more examples than any single person ever will.

The human value is QC, strategy, and client relationships. Not grunt work.

Stop protecting tasks machines do better than you.

──────────────────────────────────

Why This Matters

The bottleneck isn't delivery anymore.

It's selling more of them.

When you can deliver a $25K service in 4 hours:

→ Margins go through the roof
→ Capacity explodes
→ You can take on more clients
→ Or charge the same and work less

Either way, you win.

If you're still doing this manually, you're competing against agencies operating at 10x your speed.

That's not a fair fight.

──────────────────────────────────

The Timeline

Right now: Maybe 10% of agencies run a stack like this.
6 months: 30% will.
12 months: This is table stakes.
You either adopt this or you lose to people who did.

──────────────────────────────────

Cold Emails Not Working?

I had my developer create an AI tool that in just 60 seconds will diagnose why your cold emails aren't working and tell you exactly how to

fix it to book more calls.

Based on 100s of hours of my consulting transcripts.

Fix your cold emails now 👉 seanlongden.com

---

**作者** axtrur（@axtrur）  
**貼文連結** https://x.com/axtrur/status/2011374598915555835  

**正文**

google studio gemini3实现前端真的太快了，无脑复刻lovart交互，现在的产品没有技术壁垒越来越低了
https://ai.studio/apps/drive/1bNmERDNtQV-xc9u7o7PWy65R2D8AKffC 

---

**作者** 出海去孵化器（@chuhaiqu）  
**貼文連結** https://x.com/chuhaiqu/status/2011045066065014815  

**正文**

都来看看前大厂产品经理鱼总，离职后靠“分润模式”组建开发团队，3 年上线 20 款 App。

从月入 1 万刀到单款营收 12 万美元，看鱼总揭秘独立开发者的“广撒网”策略与付费墙变现机密。

---

**作者** Or Hiltch（@_orcaman）  
**貼文連結** https://x.com/_orcaman/status/2011492458023305394  

**正文**

Today we are launching @openwork_ai, an open-source (MIT-licensed) computer-use agent that’s fast, cheap, and more secure.

@openwork_ai  is the result of a short two-day hackathon our team decided to hack, which brings together some of our favorite open source AI modules into one powerful agent, to allow you to:

1. Bring your own model/API key (any provider and model supported by @opencode is supported by Openwork)

2. ~4x faster than Claude for Chrome/Cowork, and much more token-efficient, powered by dev-browser by @sawyerhood (legend)

3. More secure - contrary to Claude for Chrom/Cowork, does not leverage the main browser instance where you are logged into all services already. You login only to the services you need. This significantly reduces the risk of data loss in case of prompt injections, to which computer-use agents are highly exposed.

4. Free and 100% open-source!

You can download the DMG (macOS only for now) or fork the github repo via the link in bio (@openwork_ai).

Let us know what you think (or better, send a pull request)!

---

**作者** Ashpreet Bedi（@ashpreetbedi）  
**貼文連結** https://x.com/ashpreetbedi/status/2011607262893129943  

**正文**

Claude Code shipped two years after function calling.

Models have outpaced the application layer. We have frameworks to build agents, we have observability to trace them, we have evals to test them. But nothing to run them.

# AI engineering has a runtime problem.

The runtime is what turns a python script into a working product. It runs our agents as an API. It manages state across users and sessions, streams responses without breaking, stores memory and context, recovers when things crash, provides request-level isolation. Its the backend for AI.

In web development, this was solved decades ago. In AI engineering, every team builds it from scratch - streaming, state management, recovery, all of it. Most teams spend months on infrastructure before shipping anything.

Every tutorial ends with a notebook. Production is left as an exercise for the reader.

## The AI Stack

Here's how I see the AI stack today:

Every other layer has tooling. The runtime is the hole every team is missing.

## Why Agents Are Different

Traditional web applications follow a simple request-response pattern: request comes in, server processes it, response goes out. Thousands of requests per second, each independent. Scale horizontally by adding servers. This is solved infrastructure.

Agents break this model completely.

An agent isn't a request-response cycle. It's a long-running, stateful process. It receives input. It thinks, calls a tool, waits for the result, reasons, responds. The user sends another message. The agent thinks, now with full context of everything before, reasons, responds.

A single session can span minutes, hours, or days - paused while waiting, resumed on input, cancelled if the user walks away.

Agents are stateful, but scalable infrastructure is stateless by design.

Building stateful applications on stateless infrastructure is one of the hardest problems in distributed systems. Every AI team is solving it from scratch, all while building the actual product.

## What the Runtime Actually Does

The runtime handles deployment. You package your agent into a container, deploy it to your cloud, and the runtime handles everything between your code and your users.

Serving: Exposes your agents as an API. HTTP, WebSockets, SSE. Requests route to the right agent with the correct state.

State Management: Sessions persist across containers and survive restarts. State doesn't bleed between users. The agent picks up exactly where it left off, regardless of which container handles the next request.

Streaming: Durable streams that survive network hiccups. Backpressure when the client can't keep up. Graceful resumption after disconnects. Users see tokens flowing, not blank screens.

Storage: Your runtime needs a database - not as an afterthought, but as a core primitive. Sessions, memory, knowledge, traces, conversation history: all stored in your infrastructure, not scattered across third-party services.

Recovery: Container dies mid-reasoning? State is checkpointed. Context preserved. The runtime resumes the conversation. The user doesn't notice.

Scale: 100,000 concurrent users, each with multiple sessions, none interfering with each other. Horizontal scaling that actually works for stateful processes.

Request Isolation: Every request lives in complete isolation. User A's context never touches User B's memory space. Not "probably won't leak". Guaranteed  isolation at the infrastructure level. 

This is hard. Really hard. But it's infrastructure. Solve it once, not for every project.

## Why This Hasn't Been Solved

Everyone assumed existing infrastructure would handle it.

Framework companies focused on building agents. Makes sense, that's the AI part. But then they stopped at the notebook. "Here's a notebook demo. Deployment is your problem."

Observability companies focused on watching agents. Tracing, logging, debugging. Valuable, but you can't observe what isn't running.

Eval companies focused on testing agents. Benchmarks, regression suites, quality metrics. Also valuable, but you can't test your way to production.

Everyone pointed at the next layer. Nobody built it.

And so teams reach for what they know: "Just use FastAPI". Then they discover they need to build 50+ endpoints, manage state across containers, handle streaming that doesn't break, recover from mid-conversation failures, scale without state bleeding. They spend 6 months building serving infrastructure instead of product.

This is why most agent projects never reach production. Not because the agents aren't smart enough. Because there's no runtime to run them.

## The Runtime is the Foundation

Frameworks, observability, evals. None of it matters if you can't run the thing. Everything except the runtime is a demo.

We've spent the last year building it. More soon.

---

**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2011613051263598894  

**正文**

Manus 最新博客介绍他们核心的「Manus Sandbox 」
https://manus.im/blog/manus-sandbox

Sandbox 是 Manus 为每个任务分配的一个完全隔离的云虚拟机。它像一台独立的云端计算机，能并行运行多个任务，而不互相干扰。Sandbox 赋予 AI Agent 完整的计算能力，包括网络连接、文件系统、浏览器和各种软件工具。

· 关键优势：AI Agent 经过设计和训练，能智能选择并正确使用这些工具。例如，它可以通过编写代码来解决问题，甚至创建完整的网站或移动应用。所有操作都在 Manus 的虚拟化平台上 24/7 运行，不消耗用户本地资源。
· 实际应用：用户可以上传附件，AI 在 Sandbox 中生成文件或工件（如代码、配置）。这使得 AI 从“思考”转向“行动”，如自动化开发或数据处理。
· 创新点：Sandbox 强调“完整性”，类似于个人电脑，但运行在云端，确保 AI 能处理复杂任务，而非仅限于文本响应。

Manus Sandbox 的功能特性

1. 内容存储：
  · 用户上传的附件
  · AI 执行过程中创建的文件和工件
  · 任务配置
  用户可以通过界面“查看此任务的所有文件”或直接询问 AI （如“将你写的所有代码打包发给我”）来访问这些内容。

2. 生命周期管理（平衡效率与持久性）：
  · 创建：新会话时按需创建
  · 休眠/唤醒：无活动时自动休眠（文件保持不变）；需要操作时自动唤醒
  · 回收/重建：长时间休眠后回收（免费用户7天，Pro 用户21天）。重建时，AI 会自动恢复关键文件（如工件、附件、重要项目文件如 Slides 或 WebDev），但不包括临时代码或中间文件。
  · 长运行任务建议：对于需要持续运行的后端服务，推荐使用 Manus Web 开发功能构建前后端，并部署到公共互联网。

3. 安全性：
  · 遵循“零信任”原则：用户和 AI 对 Sandbox 有完全控制权（如获取 root 权限、修改系统文件，甚至格式化磁盘），但所有操作仅限于该 Sandbox 内部，不会影响其他任务、Manus 服务或用户账户数据。
  · 如果发生不可恢复错误，Manus 会自动创建新 Sandbox 继续任务，确保连续性。

隐私与数据共享风险防范
Sandbox 被视为用户的“私人计算机”，可能包含敏感信息。Manus 有严格的隐私政策，不会未经授权读取或分享数据，但用户需注意分享场景。

1. 分享 vs. 协作：
  · 分享（通过“分享”按钮）：接收者仅看到对话消息和输出工件，Sandbox 完全不可见，无需担心泄露。
  · 协作（邀请特定用户参与）：协作者可发送指令、控制执行，并通过 AI 访问/修改 Sandbox 文件，可能导致数据泄露。同时，连接器会自动禁用，防止协作者访问。

2. 最佳实践：
  · 添加协作者前，检查 Sandbox 是否含敏感内容。
  · 如果任务已有敏感信息，创建新任务，仅复制必要内容后再邀请。
  · 避免在协作会话中发送个人敏感数据。

---

**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2011632285679042657  

**正文**

AI 正在颠覆用户研究这一长期被 Qualtrics、Medallia 和 SurveyMonkey 主导的市场。

Listen Labs 已完成超过 100 万次访谈，显示这一隐形大市场潜力巨大。创始人背景亮眼。

顺带一提：他们的创始人之一 Alfred 的哥哥创办了 Soundcloud，另一位 Florian 曾代表德国在 IOI 拿过奖牌。 
AI 正在颠覆用户研究这一长期被 Qualtrics、Medallia 和 SurveyMonkey 主导的市场。

Listen Labs 已完成超过 100 万次访谈，显示这一隐形大市场潜力巨大。创始人背景亮眼。

顺带一提：他们的创始人之一 Alfred 的哥哥创办了 Soundcloud，另一位 Florian 曾代表德国在 IOI 拿过奖牌。 
源：
https://x.com/deedydas/status/2011470088763855224

---

**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2011641318527922313  

**正文**

Claude Code 发布了两个不错的更新

MCP 工具搜索以及接受或者拒绝提示的时候 Tab 键补充信息

MCP 工具搜索这个很好，以前如果你在 Claude Code 里面安装了大量 MCP ，在检索工具的时候就会占用你大量的上下文。

MCP 工具搜索加入之后，工具会动态的加载到上下文里面。

如果你有一个 MCP 服务创建者的话需要重点关注 "server instructions” 这个参数，不然有可能没办法正常拉起 MCP。

接受或者拒绝提示的时候 Tab 键补充信息，这个太有用了。

每次他对了一部分错了一部分的时候我都会很纠结，不知道该同意还是拒绝这次操作，现在完全可以补充信息。

---

**作者** huangyihe（@huangyihe）  
**貼文連結** https://x.com/huangyihe/status/2011276533688947143  

**正文**

当你觉得Claude Code已经足够好的时候，今年的Multi-Agent Orchestration一定会让你大吃一惊。

---

**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2011470281517285652  

**正文**

2025 was about "vibe coding" so you can build software with AI

2026 is about "vibe marketing" so you can earn attention, trust, and demand with AI

manus/meta moving into vibe marketing feels right on time.

---

**作者** SPAR（@SPARexec）  
**貼文連結** https://x.com/SPARexec/status/2009418183086887179  

**正文**

Gain hands-on AI safety, policy, and security research experience

SPAR is a virtual, part-time program connecting students and professionals with established researchers for 3-month projects (5–20 hrs/week). Explore 130+ projects. 

Apply by January 14.

---

**作者** Corey Chiu（@realcoreychiu）  
**貼文連結** https://x.com/realcoreychiu/status/2011376234530517127  

**正文**

现在我们 vibe coding 做产品，基本都是交给 AI 一把梭。
功能写得飞快，但设计这块，像UI、颜色、字体这些，基本都是AI 给啥就是啥，能用就行

就算想改，也不知道该怎么改，纯靠主观感觉

后来我才发现不是不在乎设计，而是根本不知道一个「好的设计」应该是什么样

这个时候，一个成熟、完整的设计标准规范就显得很重要了

而这个东西，叫「设计系统」。

设计系统本质上就是一整套涵盖颜色、排版、间距、icon、组件等的标准规范，在做产品时，按照这个规范来实现就好了

但我们这种非设计师出身的，要想设计一套靠谱的设计系统，那真是太难了

今天我来分享一个网站，收录了各家大厂的设计系统，像Apple、Adobe、Google、Ant Design。颜色系统、icon、排版、字体等，整理得非常完整，都能在里面找到
现在我们 vibe coding 做产品，基本都是交给 AI 一把梭。
功能写得飞快，但设计这块，像UI、颜色、字体这些，基本都是AI 给啥就是啥，能用就行

就算想改，也不知道该怎么改，纯靠主观感觉

后来我才发现不是不在乎设计，而是根本不知道一个「好的设计」应该是什么样

这个时候，一个成熟、完整的设计标准规范就显得很重要了

而这个东西，叫「设计系统」。

设计系统本质上就是一整套涵盖颜色、排版、间距、icon、组件等的标准规范，在做产品时，按照这个规范来实现就好了

但我们这种非设计师出身的，要想设计一套靠谱的设计系统，那真是太难了

今天我来分享一个网站，收录了各家大厂的设计系统，像Apple、Adobe、Google、Ant Design。颜色系统、icon、排版、字体等，整理得非常完整，都能在里面找到
网站👉 https://designsystems.surf/

---

**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2011511640458399870  

**正文**

I don’t think you can be a top 1% entrepreneur without these 3 traits:

1. Delusion - the ability to believe something should exist before evidence allows that belief. 

Without this, you defer to consensus and never start.

2. Optimism - the bias that effort will compound rather than collapse. 

Without this, friction looks like signal to stop instead of noise to push through.

3. Neuroticism - heightened sensitivity to risk, detail, and status. 

Without this, you miss weak signals, ship sloppily, or get blindsided.

---

**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2011230297283584136  

**正文**

原文标题：Code Is Cheap Now. Software Isn't.
原文链接：https://www.chrisgregori.dev/opinion/code-is-cheap-now-software-isnt
作者：Chris Gregori 
软件构建的门槛已然崩塌，但构建有价值事物的门槛却依然高不可攀。
Claude Code 和 Claude Opus 4.5

---

**作者** Eyad（@eyad_khrais）  
**貼文連結** https://x.com/eyad_khrais/status/2010810802023141688  

**正文**

This is the official Claude Code tutorial part 2, where I cover more advanced concepts that help you get even more out of Claude Code. If you haven't read part one, I’d highly recommend it before you

---

**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2011456539459015108  

**正文**

AnythingLLM：开源全栈 AI 应用，实现 RAG + AI Agent + 无代码构建器

它把聊天界面、文档处理、模型切换、向量存储和多用户管理集成在一个系统中，适合真实生产场景而非简单 demo。（btw... 开发团队 @MintplexLabs @AnythingLLM  要不要做一下 Cowork）

核心亮点
· 拖拽即用：支持 PDF、DOCX、TXT、网页链接、图片、音频等多种格式，一键上传后即可智能问答并显示引用来源。
· 完全自控：自由选择 LLM（开源/商业）、嵌入模型和向量数据库，无厂商锁定。
· 本地优先：桌面版或 Docker 自托管，数据全程私有，可关闭遥测。
· 多用户 & 多工作区：Docker 版支持团队权限管理与隔离。
· 无代码智能体构建：快速创建自主工作流，支持工具调用和网页浏览。
· 嵌入式小部件：可轻松集成到网站或内部系统。
· 多模态支持：内置处理文本、图像、音频能力。

开源地址
https://github.com/Mintplex-Labs/anything-llm

---

**作者** ℏεsam（@Hesamation）  
**貼文連結** https://x.com/Hesamation/status/2011159982386094482  

**正文**

this is hands-down the best AI engineering channel to follow right now. there is so many videos presented by top researchers and engineers from the biggest companies on the most recent and up-to-date topics you must know. @aiDotEngineer is dominating youtube right now. 

---

**作者** Product School（@productschool）  
**貼文連結** https://x.com/productschool/status/2011121410811273446  

**正文**

The translation layer is shrinking. The PM role is turning into an “agent-powered builder + judge.”

Problem shaping. Context curation. Taste. 

These aren’t “nice-to-haves” anymore. They’re the job.

If you’re serious about leveling up in this new PM era, start here https://prdct.school/4sEGZEM 

#ProductManagement #AIProductManagement #AIInBusiness

---

**作者** Product School（@productschool）  
**貼文連結** https://x.com/productschool/status/2011468156565373250  

**正文**

Which toolkit are you carrying into 2026?👇

#ProductManagement #ProductManager #AIProductManagement 

---

**作者** The Product Folks 🚀（@TheProductfolks）  
**貼文連結** https://x.com/TheProductfolks/status/2006011743907242036  

**正文**

AI moves fast, but in high-stakes finance - speed without reliability breaks trust.

This Live Product Lab with @bankonbasak stayed focused on what actually matters when AI decisions affect real money & real people.

Not what AI can do, but what it absolutely must not get wrong.

- Reliability is not assumed. It’s built.
- Edge cases matter more than averages.
- Tiny failures grow fast when risk & regulation are involved. 

No skipping the hard parts - model drift, eval gaps, human overrides, the uncomfortable tradeoffs teams face when automation meets accountability.

The takeaway was simple:
In high-stakes finance, AI is not impressive because it’s smart.
It’s impressive when it’s predictable, explainable & safe. 

This is why Product (Un)Conference feels different.
You don’t just leave inspired infact you leave knowing what needs fixing next. 🙌

---

**作者** Jaya Gupta（@JayaGup10）  
**貼文連結** https://x.com/JayaGup10/status/2011184143879848100  

**正文**

its a thing 

---

**作者** Meta Alchemist（@meta_alchemist）  
**貼文連結** https://x.com/meta_alchemist/status/2011418134566072558  

**正文**

5 years ago, I started a company solo, called Seedify.

At its peak, it had over 200 people and a $350 million market cap, with a $1.65 billion FDV. Bootstrapped.

The team growing became our biggest handicap. 

When our bridge was exploited, we entered into a storm.

In that storm, I vibe-coded 15-18 hours a day, wanting to master the tools so that I could recreate Seedify from the ashes, this time powered by agentic teams, automated pipelines, vibe coding, and AI tools.

While announcing that we'll be focusing on vibe coding as an incubator/launchpad.

In the background, I've worked on technologies, like agent orchestration, a decision-making layer, specialized agent skills that perform better than Claude (benchmarks on my pinned post). 

And now we'll be implementing agentic workforce pipelines in the background next.

My goal is to operate Seedify with a team of 15-20 people, where each person will utilize the tools we have developed on Claude, using skilled agent pipelines, and building more AI tools to enhance our workflow.

Will share our progress.

---

**作者** Polar（@polar_sh）  
**貼文連結** https://x.com/polar_sh/status/2011416534816555224  

**正文**

> we spent $2m to build the best billing platform for startups in the world
> built by a small, async team across europe
> we made it open source btw

https://github.com/polarsource/polar

---

**作者** 凡人小北（@frxiaobei）  
**貼文連結** https://x.com/frxiaobei/status/2011075599083995566  

**正文**

最近中推圈在疯传"怎么写 Claude Skills"。

这让我想起去年4月，老板大笔一挥决定搞 MCP。不到百人的团队，不到一年时间，搞出了上百个 MCP。

当时各团队竞相汇报 MCP，很多人还挺骄傲的。

结果呢？真正常用的不到10个。

现在 Skill 的风要来了。我猜2个月后，国内会大热。

但我也猜，大部分公司会重蹈覆辙。

为什么？因为大家又在把"组织变革"的问题，当成"工具采购"的问题来解决。

## 1. 先说说 MCP 的教训

去年4月，MCP 刚出来的时候，团队很兴奋。

"终于可以让 AI 连接数据库了！" "可以读业务服务了！" "可以调用API了！"

为什么最后大部分没人用？

做了个连 Jira 的 MCP，没人用。因为工作流程根本没变，AI 只是"查询工具"，还不如直接打开 Jira。

做了个连业务服务的 MCP，用了两次就不用了。因为还得去专门定制 mcp，跟直接写接口区别不大。

做了个连代码库的 MCP，团队说"挺好"，但实际使用频率很低。因为大家的工作方式没变，AI 还是"辅助工具"而不是"工作方式"。

问题不是工具不好，是我们没想清楚工作方式该怎么变。

现在 Skill 来了。我看到的趋势是：大家又在重复同样的错误。

教程满天飞，都在讲"怎么写 Skill"。但很少有人问：为什么要写 Skill？它解决的是什么问题？

## 2. Skill：不只是工具，更像是镜子

Skill 用下来，最大的收获不是学会了怎么写。

而是看清了一个问题：大部分组织还在用前 AI 时代的方式运作。

Skill 不是工具升级，它更像是一面镜子，照出了组织该怎么改变。

要理解这一点，得先看看 Skill 是什么。

如果你一直在关注 AI 工具的发展，应该经历过这样的演进：

最早是写 prompt 模板，把常用的提示词保存下来，每次对话时复制粘贴进去。

后来有了 MCP（Model Context Protocol），可以让 AI 连接外部工具和数据源，比如连接后端服务、查询数据库。

现在又出现了 Skills。

这三者的区别，用个不太严谨的类比来说：

Prompt 像是每次给 AI 发"使用说明书"。"你要注意这个，要遵循那个规范"。AI 看到了，但下次对话又得重新说一遍。

MCP 让 AI 可以"调用外部能力"。需要什么数据就去取，需要执行什么操作就去做。但 AI 还是在被动响应你的指令。

Skill 则是把某个领域的知识、工作流程、判断标准，直接内化成 AI 的一项"能力"。它知道在什么情况下该做什么，不需要你每次提醒。

但用久了你会发现，这不只是工具升级。

## 3. 为什么 Skill 会出现：技术演进遇到瓶颈

通用大模型已经很强了。写代码、分析数据、写文档，很多事情都能做。

但有个根本问题：它们对你的业务一无所知。

说白了，它不知道你们用什么技术栈、踩过什么坑、为什么选了这个架构方案。你们的代码规范、文档习惯，它全都不了解。

之前怎么解决这个问题？

一种方式是每次对话都把这些信息喂给 AI。写好 prompt 模板，每次复制粘贴。但很累，而且 AI 只在当前对话里"记住"，下次又得重来。

另一种方式是用 RAG（检索增强生成）。把文档、代码库扔进知识库，AI 需要时去检索。但检索到的只是"参考资料"，AI 还得自己理解、自己判断。

这些方案都在尝试"提醒" AI，而不是让 AI 真正"内化"知识。

Skill 在解决这个问题。不是提供参考资料，而是把整套工作流程、判断标准、最佳实践，打包成能力模块。AI 加载这个 Skill 之后，就"知道"该怎么做。

这不是某个公司的产品创新。当通用能力足够强之后，下一步必然是适配特定组织和场景。

## 4. Skill 揭示的问题：AI 效果为什么天差地别

我在团队里推 AI coding，几十个人，都配了工具，也做了培训。

效果...怎么说呢，一言难尽。

有些人用 AI 写出来的代码质量很高，符合规范，逻辑清晰，稍微改改就能合并。

有些人用 AI 写出来的代码一看就知道是 AI 生成的。命名随意、结构混乱、没考虑边界情况，code review 要来回好几轮。

这不是工具熟练度的问题，也不只是 prompt 写得好不好。

本质是：AI 是放大器。你对工程的理解有多深，AI 就能帮你走多远。

你的 prompt 背后体现的是你的工程经验、对问题的理解、对质量的判断。这些东西，AI 不会自己补上。

在 AI 时代，个人能力差异不只是被放大了。高手和新手之间的差距，从2倍变成了100倍。

高手用 AI 效率翻倍，质量还能保持。新手用 AI 确实快了，但质量很难保证。

这对组织是个麻烦。你不可能指望每个人都是高手。

传统方式是：Code Review、结对编程、导师制。通过人来传递经验和规范。但很慢，也很依赖"那个高手有没有时间"。

Skill 提供了另一种可能：把高手的经验和判断标准固化下来，让 AI 执行时自动遵循。

新手调用这个 Skill，AI 就能按照高手的标准工作。

这不是消除差异，而是改变"经验传递"的方式。

## 5. Skill 的本质：从人驱动到 AI 自驱动

团队里有个高手，写组件又快又好。代码结构清晰、性能优化到位、边界情况都考虑了。新人看他的代码能学到很多，但要自己写出那个水平，得花很长时间。

传统方式：新人写代码 → 高手 Code Review → 指出问题 → 新人改 → 再 Review。一个组件可能来回三四轮。高手累，新人也挫败。

现在可以这样：把高手的开发流程、代码规范、常见优化手法、容易踩的坑，打包成一个 frontend-design Skill。新人写代码时，AI 加载这个 Skill，自动按这套标准生成代码。

关键变化：高手的角色变了。

以前高手要"手把手教"，现在高手只需要"定义标准"。具体的代码生成、规范检查，AI 来做。高手的时间可以用在更有价值的地方，比如设计架构、解决疑难问题。

新人的角色也变了。以前是"写代码 → 等 Review → 改"，现在是"调用 Skill → AI 生成代码 → 人做决策和调整"。

这就是从"人驱动"到"AI 自驱动"的转变。

人的角色变了：定义标准、做决策。执行的活，AI来干。

这看起来是技术问题，但背后是组织运作方式的改变。当 AI 可以"自驱动"完成大量执行工作，人应该做什么？组织应该怎么分工？

举个我们正在试的例子：让 PM 用 AI 完成产品从 0 到 1 的全流程。从需求分析、竞品调研、原型设计、PRD 撰写，到开发实现、测试上线。没错，PM 自己做开发。这就是角色边界模糊的极端实验。

效果怎么说呢，目前一般。AI 能跑完流程，但产出质量还不够稳定，很多地方还是要人介入调整。

但方向我觉得是对的。问题不在于 AI 能不能做，而在于我们还没找到最合适的人机协作方式。Skill 还在调，这本身就是探索的一部分。

## 6. Skill 照出的组织脆弱性

一个技术架构师离职了。就在上个季度。

走之前做了交接，留了文档，但还是带走了很多东西：为什么当初选这个技术方案、踩过哪些坑、哪些地方是为了兼容历史问题做的妥协、未来的演进方向是什么。

这些东西很难写进文档。文档只能告诉你"现在是什么样"，但说不清楚"为什么是这样"以及"遇到新问题该怎么判断"。

新来的架构师得花几个月摸清楚整个系统。遇到问题时，不确定该怎么改，怕动了之后引发连锁反应。团队的技术演进速度明显慢下来。

这暴露了一个问题：组织的知识资产太依赖个人。

人在，知识就在。人走了，知识也跟着流失了一大半。剩下的文档和代码，只是"静态快照"，缺少"动态判断能力"。

Skill 在这个场景下能做什么？

可以把架构师的设计思路、技术选型逻辑、权衡标准，甚至踩过的坑和解决方案，都沉淀成一个 Skill。

新人遇到问题时，AI 不只是告诉他"现在是什么样"，而是能基于这套标准，给出"为什么这样设计"以及"遇到新情况该怎么判断"。

这不是说 AI 能替代架构师。但它能把架构师的判断标准和经验留下来，让组织不那么脆弱。

AI Native 的组织和传统组织的一个重要区别：知识资产不再依附于个人，而是可以被固化、复用、传承。

组织的韧性，会因此变得不一样。

## 7. 从 Skill 看到的更大图景：组织必须重构

Skill 为什么是范式转变，而不只是工具迭代？

因为它指向组织运作方式的改变。

当 AI 可以"自驱动"完成大量执行工作，当知识可以被固化和复用，组织会发生什么变化？

我观察到三个趋势，它们是层层递进的：

1. 很多固化流程的岗位会进一步消失

那些"按照既定流程执行任务"的工作，会越来越多地被 AI 接管。不只是简单的重复劳动，还包括那些"有流程可依"的复杂工作。

比如按照模板写文档、按照规范写测试用例、按照 Checklist 做代码审查。这些工作需要专业知识，但一旦流程清晰，AI 就能做得很好。

说难听点：如果你的工作可以写成 SOP，那 AI 迟早能做。

2. 工程师和产品经理的界限会模糊

执行成本降低之后，角色边界自然就模糊了。

以前产品经理写需求，工程师写代码，是因为"写代码"需要专门技能和大量时间。

但当 AI 可以快速生成代码，界限就不那么清晰了。懂产品的人，可以直接用 AI 把想法变成原型。懂技术的人，可以快速验证产品方案的可行性。

角色会更加"端到端"。从想法到实现，中间的环节会压缩。

3. 工作流的核心变成"AI 的自主性"

当执行工作被 AI 接管、角色边界模糊之后，工作流本身也得重新设计。

以前的工作流：人分解任务 → 人执行 → 人检查。

未来的工作流：人定义目标和标准 → AI 自主规划和执行 → 人做决策和调整。

AI 的自主性会越来越强。不是你告诉它每一步该做什么，而是你告诉它要达成什么目标、要遵循什么标准，它自己去完成。

这需要组织重新设计工作流程、重新定义岗位职责。

这三个变化是连锁反应：执行被接管 → 角色边界模糊 → 工作流重构。本质都指向一件事：组织的价值创造方式变了。

这些变化正在发生。方向很清楚。

推动这种转变，需要投入成本。时间成本（员工学习和适应）、金钱成本（AI 订阅费用）、试错成本（允许失败和探索）、组织成本（调整架构带来的混乱期）。

很多管理者会犹豫，因为短期内看不到明确的 ROI。

但不改变的风险，可能比改变更大。

## 8. 一把手必须站出来

这不是"买几个 AI 工具"就能解决的问题。

给员工配了 GitHub Copilot 或者 ChatGPT 订阅，然后期待效率提升。几个月下来发现，有人用得很好，有人根本不用，整体效果不明显。

问题在哪？工具只是表层，底层是组织的运作方式没有变。

工作流程还是按照"人做所有事情"设计的，考核标准还是按照"人的产出"来定的，知识管理还是依赖个人和文档。在这种情况下，AI 只是一个"可选的辅助工具"，而不是工作方式的一部分。

要真正转向 AI Native，需要一把手站出来推动。

为什么必须是一把手？

因为这涉及到：

- 重新设计工作流程 — 谁来做？怎么试错？
- 调整考核标准 — 用 AI 之后，怎么衡量个人贡献？
- 改变组织架构 — 哪些岗位要合并？哪些要新增？
- 投入试错成本 — 允许一段时间的混乱和探索

这些事情，不是某个部门或某个人能推动的。必须是一把手明确表态、亲自推动。

舍得短期利益

更关键的是，一把手要有勇气舍得短期利益。

员工学习 AI 工具需要时间，这段时间产出会下降。调整工作流程会带来混乱期，效率会打折。试错和探索会有失败，意味着要接受浪费。

如果不愿意承担这些短期代价，就永远停留在"给大家买个工具"的层面，然后抱怨"AI 也没那么神奇"。

等待的代价

很多管理者想：我们再等等，等 AI 更成熟一点，等市场上有更清晰的最佳实践。

但等待的成本是：你的竞争对手已经开始重构组织了。

他们的团队已经在用 AI Native 的方式工作，效率和创新速度已经拉开差距。等你"准备好"的时候，可能已经晚了。

Skill 只是一个切入点。它让我看到了 AI 时代组织变革的一个侧面。

这不是关于某个工具有多厉害，而是关于你是否意识到组织必须改变，以及是否有勇气推动这个改变。

如果你是管理者，不妨问自己几个问题：

- 你的团队在用 AI，但工作流程变了吗？
- 你的核心员工离职，知识资产还能留下来吗？
- 你在为 AI 时代重构组织，还是只是给现有组织加了一些 AI 工具？
- 你还在等什么？

答案会很诚实。

如果你现在就想开始

不需要等完美的计划。可以这样试试：

1. 选一个 3-5 人的小团队最好是愿意尝试新东西的，不要一上来就全员铺开。

2. 定一个小目标目标要具体、可衡量。技术团队可以是"用 AI 把代码 review 时间减少 30%"；运营团队可以是"周报从2小时缩到30分钟"；销售团队可以是"客户方案初稿从1天变成2小时"。什么团队都能找到切入点。

3. 给他们 1 个月探索、试错、总结。这期间允许效率下降，允许犯错。

4. 每周 review 一次不是汇报进度，而是一起看：哪些 work，哪些不 work，为什么。

5. 把有效的做法固化下来写成文档、做成 Skill、或者至少形成团队共识。然后再扩散到其他团队。

一个月后，你会有真实的数据和感受。这比现在纠结"要不要做"有用得多。

从小场景开始，快速验证，再逐步扩散。 这是最低风险的方式。

不要这样做

- 不要一上来就全员铺开，那是找死
- 不要把"做了多少个Skill"当KPI，那是形式主义
- 不要期待立竿见影，给团队时间探索
- 不要只买工具不改流程，那是浪费钱

## 9. 我的预判

Skill 会在2个月内在国内大热。

到那时，你会看到：

- 各种"Skill 教程"刷屏
- 公司开始要求"每个团队做几个 Skill"
- KPI 变成"做了多少个 Skill"

然后3个月后，你会听到：

- "Skill 也没那么神奇"
- "做了一堆，但没人用"
- "感觉跟 prompt 工程没啥区别"

这不是 Skill 的问题。

是因为大家又在把"组织变革"的问题，当成"工具采购"的问题来解决。

造工具不难。造有意思的工具也不难。

难的是：你敢不敢改造你的团队？

工具永远在迭代，组织能力才是护城河。

随着组织演进，会有新的工具出来。Prompt → MCP → Skill，后面还会有新东西。

但如果组织不变，换什么工具都一样。

工具要适配团队，或者改造团队。两者都不做，就是瞎搞。

如果你读到这里还不知道怎么开始，回去看第8章的5个步骤。今天就能动手。

## 后记：这篇文章是怎么写出来的

说到这里，可以分享一个细节。

这篇文章的观点，是我用微信输入法的语音功能，直接说给 Obsidian 的，大概输出了 1000 多字。想到什么说什么，不需要打字，不需要组织严密的逻辑。

然后在 Claude Code 里，让 AI 一起把这些碎片化的想法整理成现在这个样子。

其实这篇文章本身，就是我拿来测试 Skill 的场景之一。Skill 还在调，边用边优化。

这就是我说的"AI Native 工作方式"。

人负责：观点、方向、判断、决策。 AI 负责：整理、结构化、补充细节、执行。 工具负责：连接和沉淀（Obsidian、Claude Code）。

我知道很多人会质疑：用 AI 写文章，还是你自己的东西吗？

我的想法是：AI 既然来了，如果非得让渡一些能力给它，我希望是整理和执行这部分，而不是思考能力。观点是我的，判断是我的，方向是我的。AI 帮我把这些变成结构化的文字。

如果用传统方式，我可能需要：

- 先在脑子里理清楚所有逻辑
- 打开文档一个字一个字敲
- 反复调整结构和表述
- 花大半天甚至一整天

现在效率完全不一样。这笔交易我觉得划算。

这不是炫技。这是在说：当工作方式改变，产出效率就变了。

我写这篇文章的方式，就是我在文章里说的那种方式。如果你的组织还没开始这样工作，不妨从一个小场景试试看。

效果会比读十篇文章更直接。

现在就去试。

---

**作者** gabriel（@gabriel1）  
**貼文連結** https://x.com/gabriel1/status/2011483571341705586  

**正文**

ai is far from solving product taste, but if you can scale up user feedback with fast iteration you can build an actual one person startup

big congratz alfred on Listen Labs raise

---

**作者** Om Patel（@om_patel5）  
**貼文連結** https://x.com/om_patel5/status/2011270700737179685  

**正文**

Everyone talks about hitting $10k MRR like it's impossible. It's not. You just need the right channels and the discipline to execute daily.

After testing every marketing channel for 8 months, here's the exact playbook that works.

## Reddit: The Revenue Machine Nobody Uses Right

Reddit drives more revenue than any other organic channel if you know what you're doing.

The Undercover Link Drop Method

This one tactic generated 200k views and 8k clicks from a single post.

Here's how:

1. Build credibility first - Spend 2 weeks just helping in your target subreddits. No links. No mentions. Just pure value.
1. Write stories, not pitches - "How I failed 8 times before figuring out X" beats "Check out my startup" every time.
1. The comparison technique - When someone asks for solutions, mention yours alongside competitors: "I tried Notion and Obsidian, ended up building something simpler because..."
1. Bury the link - Put it in paragraph 3 or 4. Never in the preview. Make them want to find it.
1. Timing is crucial - Post at 8-9pm EST for high-value customers. First hour engagement determines everything.

Example that worked: Founder shared his coding journey. Mentioned his app in one sentence buried in the middle. Focused 90% on helping others avoid his mistakes.

Result: 200k views → 8k visits → thousands in MRR. FASTEST way to get visitors, validation and feedback FAST.

## TikTok/Instagram: The Viral Slideshow Strategy

Forget trying to create original content. Copy what works and add your twist.

Creating Viral AI Slideshows

Find winning formulas

- Search your niche on TikTok/Instagram
- Find slideshows with 100k+ views
- Screenshot every slide
- Copy the text word for word


Generate AI images with Grok

- Find prompts to make realistic UGC creators using gptmarket .io (start off with slideshows, then transition to full videos)
- Generate 4-6 images matching competitor's using GROK
- Mix in real screenshots of your product


Rebuild in Canva

- Upload AI images
- Have Claude generate similar text for each slide
- Keep exact formatting that worked
- 4-6 slides maximum

Platform optimization 

- Instagram: Post as Reels with trending audio
- TikTok: Carousel format with emotional music
- Never hard sell - mention product naturally


I watched someone copy a competitor's structure, use Grok for images, and hit 2M views in 48 hours.

The algorithm rewards consistency, not originality.

## Discord/Slack Communities: The Conversion Machine

Everyone ignores these. That's why they're a goldmine.

The Strategy:

1. Join 10 communities in your niche
1. Become known for advice
1. Engage in threads naturally for 1 week
1. When someone mentions your problem area, slide into DMs

DM approach that converts:"noticed your message about \[problem\]. went through the same thing last year. happy to share what worked if helpful."

No pitch. No link. Just help. 10-15% convert vs 2% for public posts.

## Twitter/LinkedIn

But not the generic "Day 54 of building" posts.

What actually works:

- Revenue numbers with full context
- DEMOS/SHORT VIDS showcasing new features with music 
- Failures bigger than successes (anything, don't be afraid to point out your stupid mistakes)
- Actual advice people can use

Content formulas that convert:

- Controversial opinion + data backing it up
- Screenshot of results + exact steps
- Failed experiment + specific lessons
- Success story + replicable playbook

## Cold Email That Converts

Forget templates. Forget automation at first.

The approach:

1. Find people complaining on Twitter/LinkedIn
1. Reference their specific complaint
1. Send tactical help with no ask

Script:"saw your tweet about \[problem\].

here's what worked for me: \[specific tactical advice\]

happy to share the full process if helpful."

15% response rate. 8% convert to customers.

Reddit COLD DM Strategy

While everyone fights for attention in posts, DMs convert at 25%.

The process:

1. Find posts where people complain about problems you solve
1. Comment with helpful advice publicly first
1. Wait a day (this is crucial)
1. DM with this script:

"hey, saw your post about \[specific problem\]. i actually built something that might help. would you be interested in trying it? looking for honest feedback."

No link in first message. Ever.

Why this works:

- Reddit users get maybe 2 DMs per week
- They check your profile and see you're helpful
- They actually want to try new tools
- They give brutal, honest feedback

From personal experience:

- 50+ customers from Reddit DMs alone
- 10 beta users who transformed my product
- Testimonials that actually convert

## Content Marketing That Drives Revenue

Competitor Alternative Posts

People searching "\[competitor\] alternative" have credit cards ready.

One post targeting "Calendly alternatives" generates $500 MRR monthly. Create these for top 10 competitors.

The formula:

- Why people look for alternatives
- Feature comparison table
- Pricing breakdown
- Your unique angle

## Conversion Optimization

Traffic without conversion is worthless.

Landing page essentials:

- Headline on the hero addressing exact problem
- Social proof in first 3 seconds
- MANY CTA BUTTONS to click on 
- Pricing visible immediately
- Founder email prominently displayed in the footer

Onboarding that converts:

- Google login only (nobody creates accounts)
- Long onboarding so that when they get to the actual value of the application, they get faced with a PAYWALL

Pricing strategy:

- No free trials for B2C
- Start higher than comfortable
- Charge what competitors charge
- Start off with a lifetime deal and after the first 20 customers, switch to monthly

## The Daily Execution Plan

Week 1-2: Foundation

- Set up accounts on chosen platforms
- Warm up by engaging naturally
- Study what's working in your niche
- Zero promotion

Week 3-4: Test

- First Reddit post using undercover method
- 5 Reddit/Slack/Discord DMs daily
- 3 Twitter/Linkedin posts daily
- 10 cold emails daily

Month 2: Double Down

- Scale what's working
- Kill what's not
- Add one new channel max
- Start promoting a UGC program/referral program for further marketing
- Influencer sponsorships to get to further audiences

Month 3+: Compound

- Word of mouth kicks in
- Referrals increase
- Growth becomes predictable
- Paid ads after hitting $10k MRR and successful viral posts to know what works

## The Math That Matters

To hit $10k MRR:

- 2,000 visitors per month per channel
- 5% trial rate = 100 trials
- 20% conversion = 20 customers
- $50 average price = $1,000 new MRR

Do this across 2-3 channels for 6 months = $10k MRR.

## What to Ignore Completely

- Paid ads before $10k MRR
- Product Hunt / Directory launches
- NEWSLETTER SPONSORSHIPS - never worth it, most lie about click count, and they charge ABSURD prices for articles that land in spam

## The Truths Nobody Admits

Marketing is 80% of the work after launch. Building was the easy part.

You'll make 200 posts before finding what works. Most quit at 10.

Every successful founder felt sleazy at first. Helping people at scale isn't sleazy.

Your first 100 customers come from things that don't scale. Embrace it.

Consistency beats everything. The founder posting daily beats the one with the perfect strategy.

Pick 2-3 channels. Show up every day for 90 days. Ignore everything else.

That's it. That's how you hit $10k MRR.

The playbook is simple. The execution is what separates those who make it from those who don't.

---

**作者** Zhixiong Pan（@nake13）  
**貼文連結** https://x.com/nake13/status/2011300097532051467  

**正文**

Cowork 发布帖的阅读量已经 4000 万了。

这个产品真的切中了普通牛马（我）的刚需。

@OpenAI 你的时间不多了…

---

**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2011461812890329313  

**正文**

1. Mobile apps are back. AI unlocks new behavior loops like autonomous logging, real-time reasoning, and adaptive UIs impossible in 2015.
2. iOS dev speed is unreal. Opus 4.5, Xcode Gen, Swift Assist,

---

**作者** Manus（@ManusAI）  
**貼文連結** https://x.com/ManusAI/status/2011460745838645700  

**正文**

We wrote a deep dive on the Manus Sandbox

→ How the environment is designed
→ How your data stays private
→ How sharing and collaboration are handled differently

If you're trusting an AI with real work, you should know what's under the hood.

Read it here:
https://manus.im/blog/manus-sandbox

---

**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2011196558751285402  

**正文**

Vori is a modern operating system for the grocery industry.

In 2025, grocers using Vori processed over $355M in annualized payments and generated more than $22M in added net sales. The company also expanded nationwide into 55+ new cities!

https://www.vori.com/blog/what-2025-taught-us 

---

**作者** Eric Jing（@ericjing_ai）  
**貼文連結** https://x.com/ericjing_ai/status/2011141696223125623  

**正文**

50 people, 9 months, $100 million annual run rate achieved!!

Incredibly grateful for the recognition from our users and the word of mouth fueling our growth.

For anyone who hasn't tried Genspark yet, ChatGPT is for chat, Claude is for code, and Genspark is for work. Go to http://genspark.ai. Try one query, you will be amazed by what AI can do for your work right now..

AND Genspark AI Workspace 2.0 is coming in two weeks!

---

**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2011490999751917919  

**正文**

Vellum is a platform for building and managing AI agents so that non-technical teams can create reliable, task-specific agents by simply describing their goal in natural language.

With over 100 native integrations, Vellum lets teams automate insights, CRM updates, renewal risk, meeting briefs, and so much more.

Congrats to @akusharmaa and team on the launch!

https://www.ycombinator.com/launches/PAb-vellum-for-agents

---

**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2011406471205146857  

**正文**

Lenny Rachitsky正在测试新的 Claude Cowork。

Claude Cowork 在分析 320 期 Lenny's Podcast 后，总结出两类核心洞察：

1、最重要的 10 个主题

2、10 条最反直觉真相

总体来看，Claude Cowork 能快速提炼大量内容，为产品建设提供高度浓缩的策略与认知洞察。

具体内容在下面 
Lenny Rachitsky正在测试新的 Claude Cowork。

Claude Cowork 在分析 320 期 Lenny's Podcast 后，总结出两类核心洞察：

1、最重要的 10 个主题

2、10 条最反直觉真相

总体来看，Claude Cowork 能快速提炼大量内容，为产品建设提供高度浓缩的策略与认知洞察。

具体内容在下面 
1、Lenny's Podcast 的 10 个最重要主题： 
2、10 条最反直觉真相： 
如果你想在家尝试一下，这里是Lenny Rachitsky所有的文字记录
https://www.dropbox.com/scl/fo/wbdrbwzpuo9f1ppvbg6xt/AJ4uoG2o_Xh4xhY9Ek7zXo4?rlkey=vew49rtpu4wl7t5t4fqhzx1a0&e=1&dl=0
源：
https://x.com/lennysan/status/2010840092865413254

---

**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2011408137711227099  

**正文**

这么多雄心勃勃的创业公司想做“LLM OS”，搞了各种花哨的 UX，结果都失败了。

这么多雄心勃勃的创业公司想做“AI 浏览器”，想帮你订机票，结果也都失败了。

而 Claude Code 一开始只是一个毫不起眼的 CLI，现在却可以控制你的浏览器、操作你的系统。

这就是经典的颠覆式创新理论。 
这么多雄心勃勃的创业公司想做“LLM OS”，搞了各种花哨的 UX，结果都失败了。

这么多雄心勃勃的创业公司想做“AI 浏览器”，想帮你订机票，结果也都失败了。

而 Claude Code 一开始只是一个毫不起眼的 CLI，现在却可以控制你的浏览器、操作你的系统。

这就是经典的颠覆式创新理论。 
Felix Rieseberg正式介绍自己负责Claude Cowork项目

该项目旨在将Claude Code能力扩展至各类知识工作。目前为早期粗糙预览版，诚邀用户反馈以支持快速迭代与每日优化。
https://x.com/felixrieseberg/status/2010851698550415826
源：
https://x.com/swyx/status/2010861152105041932

---

**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2011408943273386460  

**正文**

Marc Andreesen 谈 AI 的定价趋势：

▫️ 按使用量定价对 AI 创业公司非常有利

▫️ 很多 AI 创始人正在做非常有意思的定价实验

▫️ 更高的价格其实是好事，因为公司可以把更高的利润再投入到产品研发中，反过来给用户带来更好的服务 
Marc Andreesen 谈 AI 的定价趋势：

▫️ 按使用量定价对 AI 创业公司非常有利

▫️ 很多 AI 创始人正在做非常有意思的定价实验

▫️ 更高的价格其实是好事，因为公司可以把更高的利润再投入到产品研发中，反过来给用户带来更好的服务 
完整内容：
https://youtu.be/xRh2sVcNXQ8
源：
https://x.com/bearlyai/status/2010766802729746615

---

**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2011412084601630898  

**正文**

Antoine Rousseaux用Claude Code + Ralph在10分钟内构建了完整的"1亿美元报价"。

市场调研、客户画像、价值阶梯、定价策略、完整销售页面——全部自动化完成。

这不是ChatGPT的垃圾输出。有两个关键变化改变了一切🧵： 
Antoine Rousseaux用Claude Code + Ralph在10分钟内构建了完整的"1亿美元报价"。

市场调研、客户画像、价值阶梯、定价策略、完整销售页面——全部自动化完成。

这不是ChatGPT的垃圾输出。有两个关键变化改变了一切🧵： 
传统方式：数周的手动调研 → 画像创建 → 定位测试 → 文案撰写 → 修改 → 再测试

新方式：给Claude Code一个PRD（产品需求文档），然后看它自主执行整个营销技术栈。无需人工监督。

系统架构：

-Claude Code + Opus 4.5 + Ralph插件
-Ralph创建执行循环，而非单次提示
-PRD包含：调研阶段、画像创建、报价验证、文案生成、落地页HTML
天才之处：他创建了Russell Brunson和Alex Hormozi的AI代理来验证每个步骤。

Claude构建画像后，"Hormozi"检查价值方程式，"Brunson"验证漏斗适配度。只有两个代理都通过才能继续。
过去需要数天的调研现在几分钟完成：

-17次自动化竞品搜索，包含定价和收入估算
-Reddit抓取客户投诉和原话表达
-按类别整理的痛点分析

真实的客户语言 = 真实的转化率
构建成果：多个完整报价和完整落地页。

案例："30天内发布你的第一个工具，无需编程" - 47美元报价，包含完整价值栈、异议处理和验证过的信息传递。

全部通过代理循环系统生成和验证。
真正的洞察：这不是让AI写文案。

而是让AI在你浪费数周时间做错误报价之前验证你的思路。

提示 → 回应 → 提示 → 回应的方式浪费了90%的AI能力。PRD优先的自主执行改变了一切。
阅读原文：https://x.com/AntoineRSX/status/2010713146743562246
如果您喜欢这个主题：

1.关注我（@FinanceYF5）
2. 点赞+转发下面第一条帖子

https://x.com/FinanceYF5/status/2011412084601630898

---

**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2011420816815387078  

**正文**

Claude Cowork 系统提示词

---

**作者** 向阳乔木（@vista8）  
**貼文連結** https://x.com/vista8/status/2011275935832764564  

**正文**

这篇文章有点厉害，把组织如何用AI提效讲的很清楚。

文章超级长，转写一半大家感受下，推荐看原文

---

你可能会看到一个矛盾的现象。

AI帮个人干活，效率高得惊人，但放到公司里，效果就大打折扣了。

为什么？

因为公司里的活儿，本质上不是一个人能搞定的。

需要协作、谈判、升级决策，要在时间线上不断对齐判断。

一个再聪明的AI，如果只能单打独斗，在组织里也就是个"局部优化"的工具。

作者这篇文章，主要讲AI怎么从"个人助理"进化成"组织智能"。

上下文不是藏在某个地方的宝藏

很多人觉得，只要给AI足够多的上下文，它就能理解组织怎么运作。

前提是：组织的上下文是个完整的、结构化的东西，就像化石埋在地层里，只要挖出来就行。

真相是，大部分组织根本不是这样运作的。

上下文不存在于某个数据库里，不在某份文档里，甚至不在老板脑子里。

它是在互动中不断生成和消失的。

今天开会定的事，明天可能因为一封邮件就变了。

AI要理解组织，不能只是"读资料"，它得参与进来，像人一样在邮件、会议、文档里观察决策怎么展开，冲突怎么升级，共识怎么形成。

这才是真正的"上下文学习"。

人类的协作史，就是AI的未来

尤瓦尔·赫拉利在《人类简史》里说，人类能统治地球，不是因为个体更聪明，而是因为学会了大规模协作。

我们发明了神话、法律、货币、宗教这些"共同故事"，让陌生人也能对齐行为。

科学也是这样。

17世纪之前，科学知识是碎片化的，靠私人信件和书籍传播，错误会一直流传，发现会不断丢失。

转折点不是某个新理论，而是协作系统的出现如科学期刊、学术社团、同行评议。

知识开始积累，是因为判断变成了社会化的过程。

电话也一样。

早期电话是点对点连接的，你得知道线通到哪儿才能打。

网络一大，这套就崩了。

怎么办？接线员出现了。

她们坐在交换机前，手动连接电话，记得谁在打给谁，哪些电话更紧急，怎么处理冲突。

电话能规模化，是因为有了这个"人工中介层"。

软件开发也经历过这个阶段。

Git之前，代码协作很脆弱。

CVS和SVN是中心化的，多人改代码得排队，冲突成本很高。

Git让分支变便宜了，记录变成了一等公民，冲突变得可见、可解决。

GitHub又加了一层社会化协作：PR、代码审查、issue讨论。

规律很明显：个体能力先出现，但指数级的生产力，只有在协作结构出现后才会爆发。

AI现在就在这个节点上。

组织不会按"角色"重组，而是按"协作单元"

很多人想象的未来是：AI接管某些岗位，人类做剩下的。

但作者觉得不是这样。

AI不受人类的限制——注意力、带宽、专业分工、层级结构——这些都不存在。

所以未来的组织不会按"角色"设计，而是按"协作单元"设计。

比如法务。

法务的核心工作是"共同立场"。

合同要经过律师、合伙人、客户的多轮谈判，立场在这个过程中不断演化。

今天，资深合伙人的价值很大一部分在于"记得住"——记得之前的先例、风险、立场变化。

未来，AI会承担这部分协调工作。

它跟踪所有未解决的问题，发现立场冲突，把判断性的决策升级给合适的人。

法务团队会重组：大量AI做机械性的起草和信息收集，少数资深合伙人做决策、风险判断、客户关系维护。

再比如市场。

市场的挑战是"叙事一致性"。

产品市场、增长、品牌、销售，各自有各自的说法，怎么对齐？

今天靠开会、审稿、非正式影响力。

未来，AI会跨渠道追踪叙事，发现偏离，升级冲突。

人类的角色从"渠道负责人"变成"叙事把关人"和"战略意图制定者"。

财务、产品也是类似的逻辑。

AI不是替代某个岗位，而是重新分配了协调工作。

最快的路径是：

把AI嵌入到组织已经在用的协作工具里——邮件、消息、浏览器、文档。

这不是"遗留系统"，它们是工作的活基础设施。

意图怎么表达、分歧怎么浮现、决策怎么升级、责任怎么记录，都编码在这些工具里。

而且，升级机制已经内置了：@提及、批注、评论、建议编辑、通知。（AI也可以做）

AI要做的，不是发明新的协作方式，而是学会在这些已有的机制里参与和升级。

---

**作者** Arjun Malhotra（@BadCapitalVC）  
**貼文連結** https://x.com/BadCapitalVC/status/2011325514255118749  

**正文**

India has 63M MSMEs. They employ over 500M workers (more than the entire population of the EU) and yet operate in a constant state of barely controlled chaos. We believe there is a huge opportunity in enabling these independent outfits and making them competitive with professionalised services.

We have an abundant workforce, but lack workflows. We have people who can execute brilliantly, but not enough who can design what to execute.

The gap between designing, managing, and doing

The distinction is crucial. India doesn't lack supervisors – taskmasters really – who ensure work gets done. What we lack are those who can step back and ask: Is this the right work? Could we sequence it better? How do we optimize resource allocation? What should we build next?

In successful economies, this thinking layer (Layer 1) – call them planners, consultants, or system designers – makes up 15-20% of the workforce. We’ll refer to this category of workforce as System Designers.

The layer below this (Layer 2) is the coordinators: overseeing the work, checking-in, making sure things are on track and getting done. We refer to them as Project Managers.

![Article Image](<https://pbs.twimg.com/media/G-mphbKa4AEsV11.jpg>)

But in India's independent outfits, both Layer 1 & Layer 2 collapse onto the owner. An SME owner, let's call him Rajesh, becomes supplier coordinator, HR manager, quality controller, and strategist - a superhuman job description that guarantees subhuman results. The bottleneck is not capability; the bottleneck is system design, and this absence creates a workflow vacuum.

Rajesh’s case isn’t an exception, it’s the norm. Walk into any small manufacturing unit in Ludhiana, any construction site in Gurgaon, or any retail store in Chennai, and you'll find the same pattern. 

They have done no work on Layer 1: so there are little to no standard procedures, no systematic coordination, or structured approach to getting work done. Everything depends on the owner being present, doing Layer 2 work under sub-optimal conditions: solving problems as they creep up, making endless decisions while overloaded.

With a lack of organisational design (at Layer 1), these independent outfits face a fundamental workflow vacuum – they struggle with:

- System design (Layer 1): They have no one to design great systems: create structured workflows through which things get done, sequence and project manage work, optimise resource allocation.
- Project management (Layer 2): The owner has no time to run high performance teams – simple things we take for granted can’t be done, e.g. weekly syncs, information capture via CRM, feedback loops via periodic checks of an inventory tracker – and the owner is left dealing with whatever is coming to them.

Why is System Design a scarce resource?

Hiring skilled planners is expensive and system design requires a unique combination of skills that are rare in any economy: analytical thinking, systems design, and deep understanding of on-the-group operations.

In large corporations, entire departments handle workflow planning and resource optimisation. They use sophisticated tools, run simulations, and employ specialists for different aspects of project management – or they just hire McKinsey. But for Rajesh in his textile business, hiring McKinsey is a laughable prospect.

AI has a key role on 2 levels:

![Article Image](<https://pbs.twimg.com/media/G-mpqAdbQAYMejB.jpg>)

1. In Layer 1 (System Design): AI startups can create workflows and design systems through which SMEs can run like high-performing teams
1. In Layer 2 (Project Management): AI can assert the system design to effectively be a Project Manager, while support the business owner to work as a taskmaster

For now, let's specifically look at the role of AI in Layer 2:

Unlike traditional software that stores and processes data, AI can be harnessed to think by analysing patterns, predicting outcomes, and designing solutions.

![Article Image](<https://pbs.twimg.com/media/G-mpwK5bQAQS3Sg.png>)

What makes modern AI particularly suited for India's project management gap is its ability to work with unstructured information. When a construction foreman sends a voice note saying "कल वाले काम के लिए सीमेंट खत्म हो रहा है" (hindi for: “the cement is running out for tomorrow's work”), AI doesn't just log this information. It can understand the implications, check the project timeline, calculate required quantities, identify suppliers, and create an optimised procurement plan. We refer to this application of AI as: Orchestration AI.

Orchestration AI works with Indian reality rather than against it. Voice-first AI interfaces bypass literacy constraints entirely - workers can report progress, ask questions, and receive guidance as naturally as talking to a colleague. More critically, it can also provide this project management capability at near-zero marginal cost. The same AI system that helps optimise one construction site can simultaneously assist thousands of others. The scalable economics make sophisticated planning accessible even to tiny businesses operating on thin margins.

Examples of Orchestration AI

We're seeing a specific type of AI opportunity emerge by embedding AI in Layer 1 & Layer 2 of SMEs: one that doesn't just handle individual tasks, but orchestrates entire workflows by coordinating multiple pieces simultaneously. Examples in our portfolio:

1. [Kookar](<https://www.kookar.in/>): Every Indian household with a cook deals with daily coordination chaos: meal planning, grocery management, health considerations, and scheduling. Kookar uses AI to orchestrate this entire ecosystem by generating weekly meal plans, communicating with cooks via voice assistant in local languages, and autonomously placing grocery orders across multiple platforms. The cook operates within a system where AI handles planning and coordination, transforming kitchen management from daily chaos into systematic operation. 
1. [MyGenie](<https://www.mygenieprojects.com/>): Construction epitomises the workflow vacuum challenge. While supervisors manage attendance and execution, no one systematically handles project planning, dependencies, and task sequencing. MyGenie's AI analyses project milestones based on material costs, worker productivity, and timelines to create optimised schedules across multiple sites. Small contractors gain enterprise-grade project management and resource optimisation without needing dedicated planning staff. 

The above examples are some of the use cases of Orchestration AI. Our portfolio shows us systems that integrate deeply into daily operations, coordinate multiple workflows in parallel, and create visibility across everything happening in real-time. Unlike standalone tools you use occasionally, these systems constantly observe what's happening, connect different pieces of the operation, and proactively step in to close coordination gaps before they become problems.

But there's another equally critical pattern we need to understand. While some businesses lack coordination entirely, other jobs have well-established workflows but are suffocating under administrative burden. These aren't the same problem, and they don't have the same solution.

We'll share our second thesis on AI in India next week! 

---

**作者** Y11（@seclink）  
**貼文連結** https://x.com/seclink/status/2011261553169887384  

**正文**

很多矩阵号在吹自研的skills，以及吹自研的什么openskills（以及开源版claude cli）什么的，

好像这东西很稀缺似的。

其实吧，我们去买claude会员和gemini会员，图的是这几个skills吗？

本质上，AI编程最主要的问题是太烧token，随随便便搞个简单项目，一个小时就能烧掉上百万的token，如果不用会员而是直接API调用，很容易每天几亿token地烧，

如果不用会员，钱包根本扛不住，这才是主要矛盾。

---

**作者** riley.（@lamxnt）  
**貼文連結** https://x.com/lamxnt/status/2011241595543421306  

**正文**

What the fuck this is massive why is nobody talking about this
What the fuck this is massive why is nobody talking about this
Can you not just feed Manus API into an agent that auto launches PPC campaigns based off of live data
@codyschneiderxx

---

**作者** Charly Wargnier（@DataChaz）  
**貼文連結** https://x.com/DataChaz/status/2011089763424514380  

**正文**

http://Atoms.dev takes vibe-coding a step further.

Parallel AI teams, running directly in your browser.

You can watch multiple agents think, build, and compete in real time, then pick the best result.

Built by the @MetaGPT_ and OpenManus teams.

3 wild use cases 🧵↓ 
http://Atoms.dev takes vibe-coding a step further.

Parallel AI teams, running directly in your browser.

You can watch multiple agents think, build, and compete in real time, then pick the best result.

Built by the @MetaGPT_ and OpenManus teams.

3 wild use cases 🧵↓ 
1/

First test: I dropped a business idea into Atoms and enabled Deep Research.

Before building anything, its agents analyzed:
– market trends
– competitors
– user needs
– MVP scope

Solid.

FYI: Atoms scored 73% on Xbench DeepResearch, ahead of OpenAI o3 and Gemini. 
2/

I then turned on Atoms' Backend feat.

With a single prompt, it generated:

→ frontend
→ backend
→ auth
→ database
→ Stripe payments

And just like that, you get a working, monetizable app ✨ 
3/

THIS is where it gets insane.

I enabled Race Mode + Teams 🔥

One prompt → multiple AI agents working in parallel on different approaches.

You get a live matrix to watch each agent think and build in real time, zoom in, compare, and pick the best.

I just haven’t seen this on a vibe-coding platform before.
4/

I’ve really only scratched the surface with Atoms here.

There’s also:
→ an SEO agent for content and distribution
→ analytics
→ full-loop iteration from research all the way to deployment
 and much more!

The nice part is that it all lives inside one ecosystem.
5/

You can try @Atoms_Dev here → http://Atoms.dev
Btw, the official launch went live less than an hour ago.

It’ll be one of today’s hot topics on X :)

↓ Announcement thread here if you want to check it out:
If this was helpful, feel free to repost, it helps give the Atoms team more visibility 🦾

Follow me → @datachaz for daily stuff on LLMs, agents, and data workflows

---

**作者** hidecloud（@hidecloud）  
**貼文連結** https://x.com/hidecloud/status/2011092000456749518  

**正文**

Now everyone is an expert on SEO🥳

---

**作者** Romàn（@romanbuildsaas）  
**貼文連結** https://x.com/romanbuildsaas/status/2011099299489157458  

**正文**

Most founders think scaling to $20k MRR requires a massive team and 12 months of coding. 
It doesn't. 

In 2026, the "magic formula" is 200 customers paying $100/month, and the fastest way to get

---

**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2011250416009560081  

**正文**

Browser Use 推出「BU」，要取代 Manus 🧐

@browser_use 团队 Manus 不过是 Browser Use 的套壳，他们可以做得更好，效果可以先看官方视频。

现在 BU 还是 Waitlist 阶段，加入和排序方式也很有趣，大家还记得 Chrome 断网后的游戏吗，是的，就是这个跑酷小游戏，得分越高，等待排名越靠前。我这个手残党是没希望了。。
https://bu.app/play

---

**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2011212916125777962  

**正文**

Your @opencode will no longer hallucinate.

It now automatically detects when it needs docs, repos, or research papers, then indexes and fetches them via Nia. All retrieved context remains stateful.

Introducing the @nozomioai opencode plugin. 

bunx nia-opencode@latest install 

---

**作者** Prukalpa ✨（@prukalpa）  
**貼文連結** https://x.com/prukalpa/status/2011117250762207347  

**正文**

Jaya Gupta's thesis is right about context graphs, and wrong about who wins. In a world of heterogeneity, the integrator always wins, not the application.
If you’re in the data world, you probably saw

---

**作者** Shubham Saboo（@Saboo_Shubham_）  
**貼文連結** https://x.com/Saboo_Shubham_/status/2011278901939683676  

**正文**

Everyone has access to the same models today.
You're using Claude Opus 4.5. So is your competitor. You're using GPT-5.2. So is the startup that launched last week. You're using Gemini 3 Pro. So is

---

**作者** Atoms（@atoms_dev）  
**貼文連結** https://x.com/atoms_dev/status/2011339250655252986  

**正文**

“ Finally, an AI tool that focuses on thinking, not just writing code” 
oh❤️‍🔥

---

**作者** Atoms（@atoms_dev）  
**貼文連結** https://x.com/atoms_dev/status/2011060882940575842  

**正文**

Introducing Atoms: the first AI team that builds real businesses.
From research to build, launch, and scale, all autonomous.

Don’t Vibe Code. Vibe Business.
→ http://atoms.dev 

---

**作者** Ashpreet Bedi（@ashpreetbedi）  
**貼文連結** https://x.com/ashpreetbedi/status/2011220028453241218  

**正文**

I built one of our most complex features - learning machines - in 5 days. 100% of the code was written by claude code. This would've taken months before.
Context: I'm building Agno, an open-source

---

**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2011235954493964297  

**正文**

让我很兴奋...

Claude Cowork 自动化办公首测

一句话整理了 5000 多个文件

它还能跨文件夹和跨文档进行内容数据整理和报告撰写...

传送门：https://mp.weixin.qq.com/s/VZhnov_6sEwxIrBEavW0dA 

---

**作者** yetone（@yetone）  
**貼文連結** https://x.com/yetone/status/2011305627315028138  

**正文**

这就是用 claude code 自举自身导致的问题，本身的代码质量越来越低了

---

**作者** KK.aWSB（@KKaWSB）  
**貼文連結** https://x.com/KKaWSB/status/2011149280468484157  

**正文**

别再说人工智能不能设计了。  

Cursor + Opus 4.5 可以在不到 10 分钟的时间内创建了一个带有滚动叙事动画的着陆页，而设计师制作这样的页面通常要收取数千美元。  

如果你的落地页看起来还像2010年的应用，那不是人工智能的问题，而是工作流程的问题。



---

**作者** Jacob Rodri（@jacobrodri_）  
**貼文連結** https://x.com/jacobrodri_/status/2011144667749106037  

**正文**

What makes a app impossible to copy? 
What makes a app impossible to copy? 
Finding high-potential niches (with little competition) and scaling your organic growth with ASO will be 100x easier 👀

Waitlist: http://waitlist.appkittie.com 

---

**作者** Sprinto（@sprintoHQ）  
**貼文連結** https://x.com/sprintoHQ/status/1991200931166511509  

**正文**

Oops! We just dropped the FRESHEST tea in GRC 🧋 

No disrespect to coffee. We just chose to be cooler 😬

If you’re in SF near O’Farrell, swing by and grab a cup… on us.

We’re waiting for you📍https://maps.app.goo.gl/8xHCu8CAdUR5F9wi8 

---

**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2011342557411004639  

**正文**

Anthropic 工程师 Boris Cherny：

“Claude Code 在一周半内写完了 Anthropic 新的 Claude Cowork 的 100% 代码”

太离谱了……

这是一个非常强的信号，说明我们正在接近自动化 RSI（recursive self-improvement，递归自我改进）

还没完全到位，但你已经能看到这个循环开始成形了 
Anthropic 工程师 Boris Cherny：

“Claude Code 在一周半内写完了 Anthropic 新的 Claude Cowork 的 100% 代码”

太离谱了……

这是一个非常强的信号，说明我们正在接近自动化 RSI（recursive self-improvement，递归自我改进）

还没完全到位，但你已经能看到这个循环开始成形了 
源：
https://x.com/slow_developer/status/2011015481394950146

---

**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2011137662812635240  

**正文**

一个高手说，我代码都是 Claude Code 写的，这其实不能说明 AI 就能自己写代码了，恰恰是用 AI 的人水平的体现，他们知道怎么去正确提示，知道结果好不好，有问题知道怎么解决。

否则为啥只有一个 Claude Code，每个人都可以让 AI 写一个 Claude Code 出来。

---

**作者** Star@Day1Global Podcast（@starzq）  
**貼文連結** https://x.com/starzq/status/2010905397025186276  

**正文**

Peter Thiel: 竞争是为失败者准备的, competition is for losers

你只有跳出竞争，才能发现更大的空间，更大的领域，垄断的机会 
Peter Thiel: 竞争是为失败者准备的, competition is for losers

你只有跳出竞争，才能发现更大的空间，更大的领域，垄断的机会 
如果你对我分享的内容感兴趣，欢迎订阅我的油管，向【世界顶级大神】学习【全球化投资&套利】，通过 AI 和 Crypto, 帮助你做全球化时代的超级个体

油管：https://www.youtube.com/@Day1Global

---

**作者** Riley Brown（@rileybrown）  
**貼文連結** https://x.com/rileybrown/status/2010812596354502761  

**正文**

Now CTO and COO.
Anthropic means business.

---

**作者** Yangyi（@Yangyixxxx）  
**貼文連結** https://x.com/Yangyixxxx/status/2011056989888184491  

**正文**

卡神也来推特了👏🏻简中圈越来越多AI声音了

---

**作者** Boris Cherny（@bcherny）  
**貼文連結** https://x.com/bcherny/status/2010809450844831752  

**正文**

Since we launched Claude Code, we saw people using it for all sorts of non-coding work: doing vacation research, building slide decks, cleaning up your email, cancelling subscriptions, recovering wedding photos from a hard drive, monitoring plant growth, controlling your oven.

These use cases are diverse and surprising -- the reason  is that the underlying Claude Agent is the best agent, and Opus 4.5 is the best model.

Today, we're so excited to introduce Cowork, our first step towards making Claude Code work for all your non-coding work. The product is early and raw, similar to what Claude Code felt like when it first launched.

Cowork includes a number of novel UX and safety features that we think make the product really special: a built-in VM for isolation, out of the box support for browser automation, support for all your http://claude.ai data connectors, asking you for clarification when it's unsure,  We are excited to see how you all use it.

Cowork is available now as a research preview for Claude Max subscribers in the macOS app. Click on “Cowork” in the sidebar: https://claude.com/download

---

**作者** Carlos E. Perez（@IntuitMachine）  
**貼文連結** https://x.com/IntuitMachine/status/2011040638733848731  

**正文**

Why does Claud Code work so surprisingly well? 
Why does Claud Code work so surprisingly well? 
Actually, this is an explanation of the Skills framework in Claude Code which Claude enables

---

**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2010888768266637708  

**正文**

Claude Code的突然爆火是因为大家可以把很多技能通过一些代理和编程的方式串联起工作流

Cowork 给普通人用，集成了连接器和skills的能力，那么理论上也是可以串联起工作流的。

进行本地自动化办公，这才是今年最大的方向。

苹果和微软这个时候再不下手，收购 Claude ，很快要被革命。

理论上他们现在基本上是追不上的

---

**作者** Riley Brown（@rileybrown）  
**貼文連結** https://x.com/rileybrown/status/2010868764766838877  

**正文**

When OpenAI launched this 3 months ago, people we're saying that "1000 startups died".

This has zero users. 
When OpenAI launched this 3 months ago, people we're saying that "1000 startups died".

This has zero users. 
Remember who says this: https://x.com/skeptrune/status/2010813552529969599?s=20

---

**作者** Yangyi（@yangyi）  
**貼文連結** https://x.com/yangyi/status/2010926593104036140  

**正文**

试了一下claude的cowork
只得感叹别人vibe coding的水平和我现在的水平差距实在太大了

我还处于按起葫芦浮起瓢的修bug状态
人家已经能做一套完整丝滑的产品体验了

应该去claude偷师一下😅

---

**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2010963612438069256  

**正文**

教程多的有点泛滥了

根本看不过来🤣

而且看的晕头转向的，实际上可能直接让AI一步一步教你更快速高效！

大家好像都喜欢被喂饭，甚至恨不得塞到嘴里捣进去😐

如果你没有自驱力是很难被喂进去的，建议先确定个目标再专注学你专注的方向，不然太容易失去焦点！

结果一场空…

---

**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2011084614421659729  

**正文**

我用 Claude Cowork 一句话整理了 5000 多个文件

它还能跨文件夹和跨文档进行内容数据整理和报告撰写...

我这个人不太喜欢整理东西，我下载的文件基本都是直接默认保存在 Downloads 文件夹里，存到没空间了就一把清空😁

这个文件夹已经乱到我自己都不想打开的地步了。5000 多个文件，19 个 G，视频、图片、文档全混在一起，文件名乱七八糟，有些文件我连是什么时候下载的都不记得了。

每次想找个文件，都要在一堆东西里翻半天。我知道该整理了，但一想到要手动分类这么多文件，就... 算了，下次再说吧。

## 试试让 AI 帮忙？

Claude 今天发布了一个 Cowork 模式，可以访问本地文件。我想，要不试试？反正最坏也就是没用呗。

于是我就打了一句：Organize \[folder\].

对，就这一句。我当时心想，这 AI 能明白我想干嘛吗？

![Article Image](<https://pbs.twimg.com/media/G-jDFfVW8AAVoKj.jpg>)

## 没想到它真懂了

等了几秒，Claude 就开始扫描我的文件夹了。它告诉我找到了 5,391 个文件，然后列出来：

105 个视频

277 张图片

51 份文档

还有一堆开发文件夹

但它没有直接开始干活，而是先给我写了个整理方案。说要建 6 个大类：Videos、Images、Documents、Development、Design\_Assets、Archive。还解释了每个文件会怎么分类，哪些文件名会被改掉，哪些重复文件需要我确认。

![Article Image](<https://pbs.twimg.com/media/G-jDKHCXwAAOgla.jpg>)

这一点我觉得特别好。它不是上来就乱动我的文件，而是先问我：你看这个方案行吗？让我心里有个底。

## 开始干活

我看了一眼方案，觉得挺合理，就回了个开始。

![Article Image](<https://pbs.twimg.com/media/G-jDOy4XIAAPY84.jpg>)

然后，Claude 就开始整理了。它在屏幕上显示了一个任务列表，实时更新进度：

✓ 创建文件夹结构

✓ 移动临时文件

✓ 整理视频...

✓ 整理图片...

![Article Image](<https://pbs.twimg.com/media/G-jDTZNXIAENryP.jpg>)

我就坐在那看着，一项一项地完成。整个过程大概 3-4 分钟吧，5000 多个文件就分好类了。

有意思的是，它还自己发现了我根目录有一些漏掉的文件，主动补充了一轮清理。我都没让它做，它自己看到了就顺手收拾了。

![Article Image](<https://pbs.twimg.com/media/G-jGLdrbMAAF_GS.jpg>)

## 细节让我惊喜

整理完后，我打开文件夹一看，确实清爽多了。根目录就剩下几个主文件夹，所有东西都归类好了。

更厉害的是它的分类逻辑：

我有一堆日期命名的视频，像 1月1日.mp4、1月2日.mp4，它自动改成了 2026-01-01.mp4、2026-01-02.mp4，统一了格式

文件名里有合作、协议的文档，都被放进了 Contracts 文件夹

Gemini 生成的图片、ChatGPT 的截图，都被单独分了类

我有两个操作图片和操作图片 2文件夹，它自动合并成了一个 Operations

![Article Image](<https://pbs.twimg.com/media/G-jDcusXQAAkEmd.jpg>)

牛P的是，它还给我生成了两份报告：一份是整理计划，一份是完成报告。

完成报告里详细列出了移动了多少文件，标准化了哪些命名，还标出了哪些是重复文件建议我手动确认。

整理计划

![Article Image](<https://pbs.twimg.com/media/G-jGU73bQAkGvTG.jpg>)

完成报告

![Article Image](<https://pbs.twimg.com/media/G-jGed0bQAUejp-.jpg>)

这些细节，真的让我觉得它不是在机械地搬文件，而是在帮我整理。

这是整理后的样子，非常整洁

![Article Image](<https://pbs.twimg.com/media/G-jGmKebQAMxa-d.jpg>)

下面两个文档是整理完成后生成的整理计划和报告

子文件夹也分好类了

![Article Image](<https://pbs.twimg.com/media/G-jGqLgbsAAUZq1.jpg>)

这是整理前的样子😂

![Article Image](<https://pbs.twimg.com/media/G-jGvJSbQAYwBEj.jpg>)

## 后面更绝

整理完，我需要找个文件，也不需要自己找，直接问它就行。

我：合同放在哪里了

Claude：合同文件都在 Documents/Business/Contracts/，一共 4 份：

![Article Image](<https://pbs.twimg.com/media/G-jG3Kxa4AAhmdi.jpg>)

秒回。

它完全记得所有文件的位置。

然后我又试了一个难的：

我：找到小互的照片并发给我

Claude 先找到了 3 张文件名里有小互的图片（3D 模型）。

![Article Image](<https://pbs.twimg.com/media/G-jG7w0aQAAk7a6.jpg>)

然后我说：

我：还有呢，还有几个是胸口挂着小互牌子的照片，但是文件名不包含小互

这时候 Claude 的反应让我真的服了。它没有说找不到，而是：

先去 Operations 文件夹找了所有人物照片

然后又搜索了 iPhone 拍的照片（IMG\_ 开头的）

最后给我找出来 14 张候选照片

还专门建了个 xiaohu\_photos 文件夹把这些照片都复制过去

![Article Image](<https://pbs.twimg.com/media/G-jHAXebQAkPQq9.jpg>)

它竟然能理解胸口挂着小互牌子这种描述，然后通过多轮搜索去查找浏览照片找到目标。而且还主动创建临时文件夹、提供下载链接，这些小细节真的很贴心。

## 测试跨文件夹和文档能力

整理完文件夹后，我想试试 Cowork 能不能处理更复杂的任务。正好我电脑里有些发票，平时都是手动整理对账，特别费时间。

于是我就问了一句：找出我电脑里的所有发票，从发票中提取金额、日期、供应商，生成对账表。

它真的开始找了

Claude 收到指令后，立马开始扫描我的 Downloads 文件夹。它不是简单地搜索发票这个关键词，而是根据文件名的特征来判断。

它识别出来金额+公司名+日期时间戳的模式，然后定位到了 4 个文件。扫描完后告诉我发现了 2 张增值税专用发票（其中 2 个是重复的）。

这个识别能力挺厉害的，我自己都不记得发票文件叫什么名字了。

直接读 PDF 提取信息

找到文件后，Claude 直接打开 PDF 开始提取信息。我看着它一个一个读，把关键信息都抓出来了：

![Article Image](<https://pbs.twimg.com/media/G-jHF9WbkAAEAYH.jpg>)

这是增值税专用发票，格式挺复杂的，有表格、有印章、有各种信息。Claude 居然都能准确识别出来。

关键是中文识别没问题，公司名、税号这些长串信息都提取对了。

![Article Image](<https://pbs.twimg.com/media/G-jHKsVbQAM64uU.jpg>)

自动生成 Excel 对账表

提取完信息后，Claude 没有只是把数据列出来给我看，而是直接生成了一个 Excel 表格。

这个表格不是随便做的，很专业：

![Article Image](<https://pbs.twimg.com/media/G-jHPGPaEAEA0bC.jpg>)

## 初步感受

1. 省心

我就说了一句话，剩下的全是 AI 搞定。它会主动思考怎么分类、怎么命名、哪些需要特殊处理。我不用操心细节，只需要在开始前确认一下方案就行。

1. 放心

它先给方案再执行，让我知道它要做什么。整个过程透明，有进度条，我能清楚看到每一步。而且它会标记重复文件、临时文件，让我自己决定要不要删，没有擅自做主。

1. 聪明

文件分类的逻辑很合理，而且能理解我的模糊描述。找文件的时候不是死板地搜文件名，而是真的在理解我想要什么，然后调整搜索策略。这种感觉就像是有个助手在帮你，而不是一个机械的工具。

1. 持续

整理完之后，它记得所有文件在哪。我随时问它，它都能马上告诉我。这种长期记忆很实用，不是干完活就忘了。

其他更深度的体验我还来不及测试，先测试这么多

等我忙完手头上的事情，深度体验再发报告

## 最后说两句

用完 Cowork 之后，我对今年 AI 的发展有了全新的认识。

今年将是AI应用加速和全面自动化的爆发之年

以前我觉得 AI 就是回答问题、写点东西，更像个工具。但这次体验让我觉得，AI 真的可以像个助手一样工作：它能理解你的需求、主动规划方案、透明地执行、记住上下文，还能根据反馈调整策略。

尤其是最近 Claude Code 和 Opencode 的爆发大火，更说明了自动化将是不可阻挡之势...

而且自动化将带来意想不到的工作方式的变革和对公司组织架构的冲击

甚至2-3年内会冲击社会...

## 彩蛋

以上内容

除了开头一点和最后一段

上面所有内容都是由 Claude 根据我对它测试的过程自己写的

文中个别段落我只做了微调

没错

连这个体验报告都是 Cowork 自己写的

哈哈哈哈

哈哈哈

哈哈

哈

![Article Image](<https://pbs.twimg.com/media/G-jHV3rbQAAAUUk.jpg>)

这是它写的稿件↓

![Article Image](<https://pbs.twimg.com/media/G-jHb51akAAERqb.jpg>)

![Article Image](<https://pbs.twimg.com/media/G-jHveEbcAA_Ne_.jpg>)

---

**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2011109939377516681  

**正文**

很多朋友问我，前几天展示那个可以生成带动效的 PPT 的 skill 是怎么做和怎么用的
​
​写了一篇内容，重点详细介绍一下这个 Skills 如何安装以及如何使用

顺便说一下整个 Skills 的构建逻辑和细节。 

---

**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2010926025610576285  

**正文**

hype around the file system is real, and i am really bullish on it.

when building @nozomioai, i always asked myself what the best approach was for giving coding agents the right context like docs, code examples, and more.

RAG was not an option. rather, it is a cool addition to the core system, which I call a virtual file system.

i implemented this long before the current file system hype. when you use the nia MCP server to search for technical documentation, we have up-to-date information indexed in DBs, but it is built to act like a file system, not pure semantic search over vector embeddings.

the agent can call nia to ls, grep, or read specific parts of indexed information without bloating its context and I find it really effective.

---

**作者** howie.serious（@howie_serious）  
**貼文連結** https://x.com/howie_serious/status/2010878103615389882  

**正文**

有人需要的“ai 帮你整理桌面” 功能来了🤣

Claude cowork，非程序员版本的 claude code

 

---

**作者** Jeff Huber（@jeffreyhuber）  
**貼文連結** https://x.com/jeffreyhuber/status/2010878538170184174  

**正文**

who is building openwork?

---

**作者** conor brennan-burke（@conor_ai）  
**貼文連結** https://x.com/conor_ai/status/2010901316365861286  

**正文**

lots of posts saying claude cowork just killed hundreds of startups

they’re wrong. here’s why:

we’ve seen this narrative before. it makes a clean, simple story, but it’s not how markets actually work

openai devday 2023 tts launch:
people said it would kill elevenlabs and similar startups

reality: demand for voice exploded and the category expanded into more specialized tools. elevenlabs is doing better than ever

chatgpt enterprise:
people said it would kill b2b ai startups

reality: it unlocked budgets, made ai procurement-safe, and created demand for everything it didn’t cover
workflows, permissions, memory, integrations

big labs ship a default experience
that gives massive free education
and proves the behavior actually works

users try the flagship, then immediately ask for more:
vertical focus
deployment control
privacy
multi-model
deeper integrations

my prediction: 10x more workplace agent startups next year because of claude cowork

every workplace agent needs long-term memory and context management across tools like gmail, slack, and google drive

@hyperspell is building that context layer

if you’re building a workplace agent, reach out. we’re betting on builders in this category

the era of workplace agent startups isn’t over
it’s just getting started
lots of posts saying claude cowork just killed hundreds of startups

they’re wrong. here’s why:

we’ve seen this narrative before. it makes a clean, simple story, but it’s not how markets actually work

openai devday 2023 tts launch:
people said it would kill elevenlabs and similar startups

reality: demand for voice exploded and the category expanded into more specialized tools. elevenlabs is doing better than ever

chatgpt enterprise:
people said it would kill b2b ai startups

reality: it unlocked budgets, made ai procurement-safe, and created demand for everything it didn’t cover
workflows, permissions, memory, integrations

big labs ship a default experience
that gives massive free education
and proves the behavior actually works

users try the flagship, then immediately ask for more:
vertical focus
deployment control
privacy
multi-model
deeper integrations

my prediction: 10x more workplace agent startups next year because of claude cowork

every workplace agent needs long-term memory and context management across tools like gmail, slack, and google drive

@hyperspell is building that context layer

if you’re building a workplace agent, reach out. we’re betting on builders in this category

the era of workplace agent startups isn’t over
it’s just getting started
this post was satire but captured the vibe at the time of devday 2023

looking down the list, most of these companies (langchain, llamaindex, elevenlabs) are crushing it, and actually grew much faster after the launch

https://x.com/abhi_agarwal4/status/1721640372978561233?s=20

---

**作者** Jen Zhu（@jenzhuscott）  
**貼文連結** https://x.com/jenzhuscott/status/2010944498202026117  

**正文**

Was the Manus deal fully closed?

---

**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2010836969916420578  

**正文**

产品经理的核心工作是什么？在用户和工程师之间做翻译。 用户说“我想要一个能查看销售数据的东西”，PM 翻译成“需要一个包含 X、Y、Z 功能的 Dashboard，要有筛选器、图表、导出功能……”然后工程师照着做。

随着 AI 能力的进化，这个“翻译层”正在坍塌。

以前，PM 写完一份详细的规格书，交给工程师，等问题、澄清、等实现、评审、反馈、迭代。一个周期下来，几周就过去了。现在呢？他们写一个清晰的问题描述加约束条件，让 Agent 去做，一小时后就能看到能跑的代码。

工作效率从周变成了小时，这不仅是效率提升，更会带来工作方式的根本变化。

---

说翻译层正在坍塌的不是我，我自己不是 PM，不过和 PM 打交道很多。说这话的人叫 Shubham Saboo，Google Cloud 的高级 AI 产品经理，负责 ADK、Agent Builder、Agent Engine 这些产品，不是只会写 PPT 的传统 PM，也是个能写代码的技术实践者。他最近写了一篇文章《The Modern AI PM in the age of Agents》，讲 AI 智能体时代 PM 角色的变化。

他在 Google 待了三四个月，感觉发布了几年份的东西：Gemini 3 Pro 和 Flash、Multimodal Live API、Nano Banana Pro、Deep Research Agent、ADK 的 Java/Go/TypeScript 版本……这个发布节奏，放在几年前是不可想象的。

幕后的英雄是 AI Coding Agent。

## 规格书正在变成产品本身

PM 的工作模式分成新旧两种：

旧模式：
PM 想清楚要做什么 → 写规格书 → 交给工程师 → 工程师实现 → PM 评审 → 反馈迭代。PM 的产出是文档，工程师的产出是代码。

新模式：
PM 想清楚要做什么 → 直接用 Agent 做出原型 → 自己评估 → 快速迭代 → 满意了再交给工程师做成生产级系统。PM 的产出直接就是能跑的东西。

你发现关键变化了吗？PM 不再是工程师的上游，而是变成了产品的第一个用户。

以前 PM 描述自己想要的，然后祈祷做出来的是对的。现在 PM 直接上手定义产品，实时看到效果。

规格书正在变成产品本身。 你写的描述足够清晰，Agent 就能直接做出来。中间那个"翻译"环节，被压缩了。

![Article Image](<https://pbs.twimg.com/media/G-ftPNOWAAAQ4ew.jpg>)

## 三项新技能

当实现不再是瓶颈，瓶颈就转移到上游——搞清楚该做什么。三个能力变得关键：

第一：定义问题

以前这是 PM 的技能之一，现在这是唯一核心技能。你能不能把一个模糊的用户痛点，变成一个清晰的、有边界的问题，清晰到 Agent 能直接上手做？

这比听起来难得多。大多数时候，用户说的是“这个系统太难用了”，你得搞清楚：是哪里难用？是流程复杂还是界面混乱？是新手不会用还是老手嫌麻烦？“难用”这个词可以拆出几十种可能。定义问题，就是把这团乱麻理成一条线。

第二：上下文喂养

这是没人谈但每个高效使用 Agent 的 PM 都在做的事。Agent 产出的质量，跟你喂给它的上下文质量直接挂钩。

早期用 Agent，随便写个提示“给我做个客户反馈的 Dashboard”，出来的东西技术上能跑，但完全没抓住重点。因为 Agent 不知道你的用户是谁、你的约束是什么、什么叫“好”。

想做得更好，可以维护一份“上下文文档”，每次启动项目前喂给 Agent。这里有一个框架，适用于任何需要和 AI 协作的场景：

- 具体的用户 — 不是抽象的“用户画像”，而是真实的人：他们是谁，在意什么，什么让他们放弃，什么让他们眼前一亮。
- 用户的原话 — 来自电话、工单、销售记录的直接引用。用他们的语言，不是你的总结。这能让 Agent 接触到真实的痛苦，而不是被抽象过的痛苦。
- “好”长什么样 — 你团队认为设计得好的案例：自己过去的作品、竞争对手的、相邻产品的。给 Agent 看，而不是描述。
- 你试过什么、为什么失败 — 那些通常只存在于人脑子里的经验教训，那些被你们毙掉的方案和毙掉的理由。
- 真正影响方案的约束 — 不是所有约束，只是那些会实际改变产出的约束。
- 怎么知道成功了 — 具体的、可衡量的、能观察到的标准，不是模糊的愿景。

这六个要素，就是把"PM 脑子里的隐性知识"显性化、结构化。喂给 Agent，它就不是从零开始，而是带着你的全部背景知识在工作。

![Article Image](<https://pbs.twimg.com/media/G-ftRYxXEAMtD0p.jpg>)

第三：品味

当 Agent 能快速产出大量东西时，判断“这个能发布”还是“这个只是能跑”的能力就变得特别重要。

Agent 会很自信地产出看起来正确但完全跑偏的东西。你得有感觉，得有判断力。

怎么练？没有捷径，就是反复做、反复评估、反复学习什么叫“够好能发布”。

## 两个思维转变

除了技能，还有两个思维方式的改变。

第一个：让第一版是错的。

以前 PM 的习惯是先在脑子里想清楚，尽量把所有边界情况都考虑到，再开始做。现在可以反过来：给 Agent 足够的背景，让它先出一个粗糙的版本，看看出来什么，然后根据“这里不对，因为……”来迭代。

你现在可以让 Agent 同时做两三个完全不同的方案，看哪个用起来感觉更对。这在以前太贵了，现在不过是一下午让 Agent 并行跑几个任务的事。

第二个：延迟收敛。

以前 PM 的本能是尽快消除模糊性，尽快把问题收敛成明确的规格书。现在可以在探索阶段故意保持模糊，让 Agent 帮你理解解决方案空间，不要太早锁定方向。

因为试错成本低了，多探索反而更高效。

![Article Image](<https://pbs.twimg.com/media/G-ftWvJWkAIyngx.jpg>)

---

文章说的情况非常适用于科技公司、初创团队、原型验证阶段。在这些场景下，PM 用 Agent 快速出原型、快速迭代，确实能极大提效。

但对于传统企业、B2B 产品、合规要求高的领域，这个“翻译层”未必能消失。金融、医疗、政府项目，“规格书→评审→实现”的流程可能是法规要求的，不是效率问题。

另外还有来自组织层面的阻力。PM 直接产出原型，会改变 PM 和工程师的协作关系、权力关系。工程师会怎么看“PM 写的代码”？这种组织变革的摩擦，可能比技能学习更难解决。

## 翻译层消失后，剩下什么？

当翻译层消失后，剩下什么？

那些一直真正重要的东西：定义问题、用户共情、判断力和品味。

这些能力一直是 PM 工作的一部分，只是过去被大量的“翻译工作”稀释了。你花大量时间写文档、跟进度、开会澄清、来回沟通。现在这些被 Agent 压缩了，PM 终于可以把精力放在真正重要的事情上。

如果你的工作主要是把用户需求翻译成文档交给工程师，那是一个流程。流程会被自动化。

![Article Image](<https://pbs.twimg.com/media/G-ecYQ5WoAASmnL.jpg>)

如果你的工作是把问题理解得如此深刻，以至于正确的解决方案变得显而易见，那你比以往任何时候都更有价值。

---

![Article Image](<https://pbs.twimg.com/media/G-fta-sW0AA51Hv.jpg>)

---

**作者** Guillaume（@iamgdsa）  
**貼文連結** https://x.com/iamgdsa/status/2010782484728873387  

**正文**

Apparently, a 19 year old built Wisprflow's UGC program to 500M views in 60 days.

Dude spills some sauce on LinkedIn. 

Open this to see the entire post

---

**作者** Austen Allred（@Austen）  
**貼文連結** https://x.com/Austen/status/2010850077611286832  

**正文**

I’m a little confused at the hype around this.

Isn’t this… exactly what Claude does already? And has done for a long time?

Is this just marketing to let nontechnical people know they can use it too?

I must be missing something.

---

**作者** yetone（@yetone）  
**貼文連結** https://x.com/yetone/status/2010908924749496342  

**正文**

哈哈，我反倒觉得一大批 AI 创业公司的机会来了，当你走的那条路大公司都开始跟着过来走的时候，说明这条路你走对了，那么就心无旁骛开开心心地继续走下去吧！

---

**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2010899013634347032  

**正文**

天啊，Anthropic 是在最近……一周半之内就做出了 “Cowork” ？！

这是 Anthropic 员工 Felix Rieseberg 在 Dan Shipper 的直播中确认的。

不禁让人好奇，这里面有多少是 Claude Code 的功劳。 
天啊，Anthropic 是在最近……一周半之内就做出了 “Cowork” ？！

这是 Anthropic 员工 Felix Rieseberg 在 Dan Shipper 的直播中确认的。

不禁让人好奇，这里面有多少是 Claude Code 的功劳。 
Claude 推出的 Cowork 功能，它可以让用户像开发者使用 Claude Code 写代码一样，用 AI 来完成非技术性工作任务
https://x.com/claudeai/status/2010805682434666759
全部都是用 Claude Code 构建的。 
源：
https://x.com/altryne/status/2010811222409756707

---

**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2010905467393110198  

**正文**

Anthropic 终于走了这一步，做了给非技术人员用的 Claude Code Cowork

选择文件夹后，Cowork 可以读取、编辑和新建文件

帮你完成例如整理下载文件、从截图中提取费用记录生成表格、或将零散笔记整理成报告初稿这种任务

还能跟 Chrome 上的 Claude 协同完成任务


Anthropic 终于走了这一步，做了给非技术人员用的 Claude Code Cowork

选择文件夹后，Cowork 可以读取、编辑和新建文件

帮你完成例如整理下载文件、从截图中提取费用记录生成表格、或将零散笔记整理成报告初稿这种任务

还能跟 Chrome 上的 Claude 协同完成任务


目前只开放给 Max 会员

---

**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2010909193101066446  

**正文**

离谱的是，Claude Code 的创造者说，Cowork 这个部分的代码全部都是 Claude Code 写的！

我们已经进入到 AI 自己指挥自己、自己创造自己的时代了 
离谱的是，Claude Code 的创造者说，Cowork 这个部分的代码全部都是 Claude Code 写的！

我们已经进入到 AI 自己指挥自己、自己创造自己的时代了 
来源：https://x.com/bcherny/status/2010813886052581538?s=20

---

**作者** Om Patel（@om_patel5）  
**貼文連結** https://x.com/om_patel5/status/2010568123368505529  

**正文**

sometimes the simplest solution is the best solution 

---

**作者** zack（@whotfiszackk）  
**貼文連結** https://x.com/whotfiszackk/status/2010626177065767075  

**正文**

everyone's using chatgpt and claude for everything because those are the names they know, treating all AIs like they're interchangeable commodities when the reality is each model has specific superpowers that create unfair advantages if you actually understand what they're optimized for

meanwhile there's operators who discovered that grok and manus together form this perfect feedback loop where manus tells you EXACTLY what the market is screaming for by analyzing thousands of real conversations, then grok takes that validated demand and converts it into money by writing copy that sounds like it was ripped straight from those conversations because it was literally trained on the same platform where those conversations happen

and they're doing $15k-$35k monthly selling info products they validated in 90 minutes and launched in 8 days, spending maybe $28/month total on these two tools while everyone else burns $60-$200/month on tool stacks that don't talk to each other and require 6 weeks of manual work between idea and revenue

here's why this specific two-tool combination unlocks automation and speed impossible with any other stack

THE SINGLE-AI BOTTLENECK EVERYONE'S STUCK IN

watch people using only chatgpt or only claude and you'll see them hitting the same wall over and over, trying to make one tool do everything when it's optimized for specific functions

TYPICAL SINGLE-AI WORKFLOW (USING ONLY CHATGPT):

week 1: market research attempt

- prompt chatgpt: "what are common problems in productivity niche?"
- outputs: generic surface-level problems based on training data
- you: "but are these actually what people want RIGHT NOW?"
- chatgpt: can't tell you, knowledge cutoff april 2024, no real-time data
- result: you're guessing based on AI's guesses, double-blind speculation

week 2-3: validation attempt

- manually browse reddit and twitter trying to confirm chatgpt's suggestions
- read maybe 40-60 threads over 12 hours
- subjectively interpret what you see
- still not confident about demand
- result: wasted 2 weeks, still uncertain

week 4-5: content creation

- prompt chatgpt to write course content
- outputs: decent structure but generic examples
- lacks specificity and current relevance
- sounds like AI wrote it because chatgpt hasn't seen recent conversations about this topic
- result: mediocre content that needs heavy editing

week 6: sales copy

- prompt chatgpt to write sales page
- outputs: conversion copy that's technically correct but doesn't resonate
- missing the exact language your customers use
- missing current objections and pain points
- result: sales page that converts at 2-3% instead of 8-10%

TOTAL TIME: 6 weeks from idea to launch CONFIDENCE LEVEL: medium (never truly validated) CONVERSION RATE: 2-3% (generic copy) MONTHLY REVENUE: $4k-$8k (if lucky)

this single-AI approach has fundamental flaw: you're using one generalist tool for specialist jobs, like using swiss army knife when you need surgical scalpel

THE GROK + MANUS SYNERGY (WHY THIS PAIRING IS PERFECT)

completely different approach using two specialized tools that feed into each other creating automation loop

THE FEEDBACK LOOP:

step 1: MANUS validates demand

- analyzes real conversations across reddit, quora, twitter, linkedin
- finds proven painful problems with existing buyer intent
- extracts exact customer language, objections, budget signals
- gives you data-driven market intelligence

step 2: GROK converts demand into revenue

- trained on X/twitter data (same platform manus analyzes)
- writes copy using exact language patterns manus discovered
- understands viral psychology and conversion triggers
- creates sales assets that resonate because they're speaking customer's language

THE MAGIC: manus tells you WHAT to build (validated demand) grok tells you HOW to sell it (conversion-optimized copy using validated language)

they speak the same language because grok was trained on the conversations manus is analyzing

RESULT:

- 90 minutes for validation (vs 2-3 weeks guessing)
- copy that converts 3-4x better (because it uses actual customer language)
- products that sell from day 1 (because demand was pre-validated)
- total cost: $28/month (manus $20 + grok $8 via X premium)

THE MANUS SUPERPOWER NOBODY UNDERSTANDS

most people think manus is "just another AI" when it's actually specialized market intelligence engine, here's what makes it different

MANUS VS CHATGPT FOR RESEARCH:

chatgpt approach: prompt: "what are common productivity problems?" output: "based on my training data, people struggle with: time management, procrastination, focus, prioritization, work-life balance" source: generic synthesis of internet content through april 2024 utility: tells you what WAS talked about, not what IS being discussed

validation: ZERO, you have no idea if people actually want solutions to these or would pay for them

manus approach: prompt: "analyze reddit, quora, twitter discussions from last 90 days about productivity problems" output: "analyzed 3,847 conversations. Top problems by commercial viability:

1. context-switching for remote workers (428 discussions, high frustration, $500-$2k budget signals)
1. meeting overload for managers (387 discussions, urgent pain, corporate budget access)
1. async communication for distributed teams (312 discussions, growing problem, $1k+ mentions)"

source: real conversations from real people discussing real problems RIGHT NOW utility: tells you what people are ACTIVELY struggling with and willing to pay for

validation: COMPLETE, you have proof of demand before building anything

THE MANUS ADVANTAGE BREAKDOWN:

advantage 1: REAL-TIME MARKET INTELLIGENCE

- analyzes conversations from last 30-90 days
- catches trends as they emerge
- sees shifts in market sentiment
- identifies new problems before competitors

example: manus caught "AI overwhelm for solopreneurs" in march 2024 when discussions spiked 340%, operator built course in 2 weeks, owned niche before competition arrived

advantage 2: VOLUME AT SCALE

- processes thousands of conversations
- identifies patterns human couldn't spot
- ranks by multiple demand signals simultaneously
- removes your subjective bias

comparison:

- manual research: read 50 threads in 8 hours, subjective interpretation
- manus research: analyze 5,000 threads in 90 minutes, objective ranking

100x more data, 5x faster

advantage 3: EXACT CUSTOMER LANGUAGE EXTRACTION

- pulls verbatim quotes from conversations
- shows you how customers describe problems in their own words
- reveals objections, triggers, emotional drivers
- gives you copywriting gold

this is where manus + grok synergy kicks in:

manus finds: "I'm drowning in slack messages and feel like I'm always behind, spending 3 hours daily just catching up on notifications"

grok uses that exact language in sales copy: "if you're drowning in slack messages and spending 3+ hours daily just catching up, here's how to reclaim that time..."

customer reads it and thinks: "holy shit they understand exactly what I'm going through"

advantage 4: COMPETITIVE GAP IDENTIFICATION

- sees what existing solutions people tried
- finds what they complain about
- identifies unmet needs
- reveals positioning opportunities

manus output: "existing solutions mentioned: todoist (412 mentions), notion (387 mentions) common complaint: 'too complex, takes longer to set up than just doing the work' opportunity: simple solution that works immediately without setup"

now you know exactly how to position: "the 5-minute productivity system that requires zero setup"

advantage 5: PRICING VALIDATION

- finds budget signals in conversations
- sees what people mention paying
- identifies price sensitivity
- validates willingness to pay

manus finds: "spent $1,200 on productivity course that didn't help" "would pay $2k if it actually worked for remote teams" "tried $500 notion template, too generic"

pricing conclusion: market will pay $1,000-$2,000 for solution that's specific to remote teams and actually delivers results

you're not guessing at pricing, you're seeing revealed preferences

THE GROK SUPERPOWER EVERYONE UNDERESTIMATES

most people think grok is "just chatgpt with X access" when it has specific advantages for conversion copy that other AIs can't match

GROK VS CHATGPT FOR SALES COPY:

chatgpt approach: prompt: "write sales page for productivity course" output: professional, grammatically correct, but generic corporate-speak that sounds like every other sales page tone: "Transform your productivity and achieve your goals with our comprehensive system" conversion: 2-3% (technically correct but doesn't resonate)

grok approach: prompt: "write sales page for productivity course targeting remote workers struggling with context-switching" output: uses conversational patterns from X, pattern interrupts, social proof formatting, psychological hooks tone: "you're switching between slack and email and zoom 47 times daily and wondering why you can't get deep work done, here's the system that fixes it" conversion: 7-11% (speaks directly to pain in their language)

THE GROK ADVANTAGE BREAKDOWN:

advantage 1: TRAINED ON X/TWITTER PSYCHOLOGY

- grok learned from millions of X posts about what goes viral
- understands hooks, pattern interrupts, engagement triggers
- knows how to structure copy for scroll-stopping impact
- optimized for attention economy

this shows up in sales copy:

- stronger headlines (pattern interrupt vs statement)
- better hooks (curiosity gap vs description)
- tighter writing (every word earns its place)
- more engaging flow (varies sentence rhythm)

chatgpt headline: "The Complete Productivity System for Remote Workers" grok headline: "the remote worker doing 60-hour weeks but hitting $12k/month just changed one system and jumped to $31k working 25 hours (here's the framework)"

which stops your scroll?

advantage 2: REAL-TIME TREND AWARENESS

- grok has access to current X conversations
- sees what's trending RIGHT NOW
- can reference recent events and discussions
- stays relevant and timely

example: you: "write sales copy for AI automation course" grok: incorporates recent AI developments, trending discussions, current pain points it sees on X chatgpt: uses generic AI benefits from training data, misses current context

result: grok copy feels current and relevant, chatgpt feels dated

advantage 3: SOCIAL PROOF FORMATTING

- grok learned how successful X accounts use social proof
- understands testimonial formatting that drives FOMO
- knows how to structure metrics for maximum impact
- optimized for credibility signaling

grok testimonial structure: "started at $8k/month drowning in busy work, implemented \[framework\], hit $34k/month working 18 fewer hours weekly by day 87, here's the revenue screenshot - @username"

includes:

- specific before metric ($8k)
- specific after metric ($34k)
- timeline (day 87)
- proof element (screenshot)
- credibility (username attribution)

chatgpt testimonial structure: "this course really helped me improve my productivity and earn more, highly recommended"

which one convinces you?

advantage 4: OBJECTION HANDLING PSYCHOLOGY

- grok understands how X users skeptically evaluate claims
- knows common objections and how to preemptively address
- structures FAQs based on real discussion patterns
- anticipates resistance

when you prompt grok to write FAQ section, it generates questions like: "what if i've tried productivity systems before and they didn't stick?" "how is this different from just using notion?" "do i need any expensive tools or can i start with what i have?"

these are REAL objections it's seen on X, not generic questions chatgpt invents

advantage 5: CONVERSION OPTIMIZATION VELOCITY

- grok generates variations FAST (30-60 seconds)
- perfect for A/B testing headlines, CTAs, hooks
- can create 20 variations in 2 minutes
- enables rapid optimization

workflow: you: "generate 15 headline variations testing different psychological triggers" grok: outputs 15 distinct headlines in 45 seconds you: pick top 3, test with small traffic winner: 2.3x better conversion than original

this velocity compounds: test weekly, implement winners, conversion rate climbs from 4% → 5.2% → 6.8% → 9.1% over 12 weeks

THE COMPLETE GROK + MANUS WORKFLOW

here's exact step-by-step process using these two tools to go from zero to $15k monthly

PHASE 1: MARKET VALIDATION WITH MANUS (DAY 1, 3 HOURS)

step 1: broad opportunity scan (45 minutes)

open manus, run initial research prompt:

"analyze reddit, quora, twitter, linkedin discussions from last 90 days about \[general topic area: productivity / marketing / sales / AI tools / remote work\]

rank top 20 problems by commercial viability score combining:

- discussion frequency (volume of conversations)
- emotional intensity (frustration, urgency, pain level)
- solution inadequacy (complaints about existing solutions)
- willingness to pay (budget mentions, payment signals)
- demographic concentration (specific audience)

for each problem include:

- total discussions found
- sample verbatim quotes (5-10 per problem)
- demographic breakdown (who's discussing)
- competitive landscape (existing solutions mentioned)
- price sensitivity signals"

manus outputs ranked list with scores, you scan and shortlist top 3 problems

step 2: deep dive validation (90 minutes)

pick #1 problem from ranking, go deeper:

"analyze the 300 most engaged discussions specifically about \[chosen problem\]

extraction requirements:

LANGUAGE PATTERNS:

- exact phrases used to describe problem (verbatim, 20+ examples)
- emotional language frequency (frustrated: X mentions, overwhelmed: Y mentions)
- metaphors and analogies used
- before/after language (current state vs desired state)

PAIN POINTS:

- primary pain (what hurts most)
- secondary pains (related issues)
- impact statements (how this affects their business/life)
- urgency signals (timeline pressure)

SOLUTION SIGNALS:

- what they've tried (specific tools, courses, methods)
- why previous attempts failed (specific reasons)
- what they wish existed (feature requests, ideal solution descriptions)
- implementation concerns (time, complexity, technical skill)

BUYER PROFILE:

- job titles and roles
- company sizes and types
- experience levels
- budget access (corporate vs personal, expense vs out of pocket)

PRICING INTELLIGENCE:

- specific amounts mentioned paying (for similar solutions)
- price complaints (too expensive: specific thresholds)
- value anchors (what they compare pricing to)
- ROI expectations (what results justify the price)

COMPETITIVE GAPS:

- existing solutions mentioned (frequency ranked)
- specific complaints about each competitor
- unmet needs (what's missing from current market)
- differentiation opportunities"

manus delivers comprehensive problem profile

step 3: offer design (45 minutes)

now you have complete market intelligence, design offer:

based on manus data:

- problem: \[specific validated pain point\]
- audience: \[specific demographic from research\]
- solution format: \[course / templates / system based on preferences found\]
- price: $\[based on budget signals, typically $697-$1,997 for courses\]
- unique positioning: \[addressing competitive gaps identified\]
- guarantee: \[structured to overcome top objection found\]

you now have market-validated offer design, zero guesswork

PHASE 1 OUTPUT: complete market validation + offer design in 3 hours, high confidence this will sell

PHASE 2: SALES COPY WITH GROK (DAY 2, 4 HOURS)

step 1: sales page generation (20 minutes)

open grok, feed it manus intelligence:

"write complete sales page for info product

OFFER DETAILS:

- product: \[your course/system name\]
- audience: \[specific who from manus research\]
- problem: \[exact problem validated by manus\]
- solution: \[your methodology/framework\]
- price: $\[validated price point\]
- format: \[what's included\]
- guarantee: \[your risk reversal\]

LANGUAGE REQUIREMENTS: use these exact customer phrases from research: \[paste 15-20 verbatim quotes from manus\]

STRUCTURE:

- headline: transformation promise using customer language, include specific before/after metrics and timeline
- subheadline: audience filter so wrong people self-select out
- pain agitation: 4-5 paragraphs using exact emotional language from manus research, make them feel deeply understood
- credibility: brief backstory how you discovered this solution
- framework introduction: teach core methodology at high level, create curiosity gap
- what's included: module breakdown showing clear progression and outcomes
- social proof: testimonial format using specific metrics (create placeholders for now)
- who this is for / not for: based on demographic data from manus
- pricing: clear presentation, address price objections found in research
- guarantee: structured to overcome top objection from manus data
- FAQ: answer 8 specific questions based on manus objection research
- final CTA: urgency through scarcity (cohort model) or bonus (deadline)

TONE:

- conversational like talking to friend
- pattern interrupts every 150-200 words
- short sentences and paragraphs for readability
- specific numbers throughout (avoid vague claims)
- credible not hypey (audience is skeptical based on research)

LENGTH: 3,500-4,500 words

PSYCHOLOGICAL TRIGGERS:

- use social proof positioning (others like them succeeded)
- invoke loss aversion (cost of staying stuck)
- specificity creates credibility (exact metrics)
- guarantee reverses risk completely"

grok outputs complete sales page in 8-12 minutes using manus-validated language

step 2: customization and refinement (2 hours)

review grok output:

- verify it used customer language from manus (should sound like research quotes)
- add your specific examples and stories (personal touch)
- strengthen weak sections (usually need more specificity)
- ensure logical flow from pain → solution → proof → offer
- polish headline (test 3-5 variations grok generates)

step 3: email sequence creation (90 minutes)

prompt grok:

"create 7-email sequence nurturing leads to purchase

CONTEXT:

- lead magnet: \[your free offer\]
- paid offer: $\[price\] \[course name\]
- audience: \[from manus research\]
- key objections: \[top 5 from manus\]

SEQUENCE STRUCTURE:

email 1 (day 1 - deliver value):

- subject: \[welcome + curiosity\]
- deliver lead magnet instantly
- establish credibility quickly
- no pitch, pure value
- CTA: consume lead magnet

email 2 (day 2 - framework tease):

- subject: \[pattern interrupt\]
- share one powerful insight from your methodology
- create curiosity gap about full system
- still no pitch
- CTA: reply with biggest challenge

email 3 (day 4 - social proof):

- subject: \[specific result\]
- case study or transformation story
- use format: before metric → obstacle → solution → after metric
- soft mention of your program
- CTA: want same results?

email 4 (day 6 - objection #1):

- subject: addresses specific objection
- handle \[most common objection from manus\]
- provide evidence this isn't an issue
- testimonial addressing this objection
- CTA: questions?

email 5 (day 8 - objection #2):

- subject: addresses second objection
- handle \[second objection from manus\]
- reframe their concern
- show how others overcame it
- CTA: ready to start?

email 6 (day 10 - direct offer):

- subject: \[clear benefit\]
- full pitch with everything included
- social proof (3-5 testimonials)
- guarantee prominently featured
- pricing clearly stated
- CTA: enroll now

email 7 (day 13 - urgency):

- subject: \[time-sensitive\]
- final invitation with genuine urgency
- cohort starting / bonus expiring / spots limited
- restate transformation promise
- last chance positioning
- CTA: claim your spot

REQUIREMENTS:

- use customer language from manus research throughout
- subject lines: 30%+ open rate optimization (curiosity, specificity, benefit)
- body: 250-400 words (respect attention)
- conversational tone (write like talking to one person)
- pattern interrupts in first 2 sentences
- specific examples and metrics
- clear single CTA per email"

grok generates complete sequence in 10-15 minutes

review for 60-90 minutes, personalize, ensure progression makes sense

step 4: content variations (60 minutes)

use grok to generate:

"create 10 social media posts promoting \[your offer\]

mix:

- 4 value posts (frameworks, insights from your methodology)
- 3 problem callouts (using manus language)
- 2 transformation stories
- 1 direct CTA

for each post:

- hook: first sentence stops scroll (pattern interrupt or surprising claim)
- body: 300-500 words value
- engagement: question at end
- CTA: subtle lead to lead magnet or sales page

platform: \[twitter/linkedin/instagram\] tone: \[based on your audience from manus\]"

grok outputs 10 posts, you review and schedule

PHASE 2 OUTPUT: complete sales funnel (page + emails + social content) in 4 hours

PHASE 3: RAPID PRODUCT BUILDING (DAY 3-5, 12 HOURS)

this part uses claude or chatgpt (not grok's strength), but informed by manus + grok work:

use manus research as content foundation:

- pain points become lessons
- customer language becomes examples
- objections become FAQ content
- competitive gaps become unique frameworks

use grok copy as structure guide:

- sales page "what's included" becomes curriculum
- email sequence insights become lesson hooks
- social posts become bonus content

total build time: 12 hours for 4-week course (using AI + manus insights)

PHASE 4: BETA LAUNCH (DAY 6-8, 8 HOURS)

day 6: setup

- upload course to teachable/gumroad (2 hours)
- implement sales page and email sequences (2 hours)
- test complete funnel flow (1 hour)

day 7-8: outreach

- identify 100 ideal customers using manus demographic data
- personalize outreach using grok:

"write personalized linkedin/email message for \[prospect type from manus\]

context:

- they're experiencing \[specific problem from manus\]
- they've tried \[solutions from competitive analysis\]
- they're looking for \[unmet needs from manus\]

message structure:

- reference specific pain point they likely have
- mention you built solution for exactly this
- beta offer: \[discount\] for feedback
- limit: only 10-15 spots

tone: helpful not salesy, personalized not template"

send 100 messages, convert 8-12% = 8-12 beta students at $697-$997

COMPLETE TIMELINE: 8 DAYS FROM IDEA TO REVENUE

day 1: manus validation (3 hours) day 2: grok sales assets (4 hours) day 3-5: product build (12 hours) day 6-8: launch (8 hours)

total: 27 hours active work revenue: $5,580-$11,964 from beta (8-12 sales at $697-$997)

THE AUTOMATION OPPORTUNITIES

once you've proven the system with one product, automation unlocks:

AUTOMATION 1: WEEKLY MARKET SCANNING

set reminder: every monday 9am, run manus scan

"analyze discussions from last 7 days about \[your niche\]

identify:

- emerging problems (new pain points appearing)
- trending topics (spike in discussion volume)
- sentiment shifts (changing attitudes)
- competitive changes (new solutions mentioned)

flag: anything with 50+ discussions or 200%+ growth"

manus alerts you to opportunities before they become obvious

one operator found "AI overwhelm" spiking, launched course 3 weeks before competition noticed, owned niche

AUTOMATION 2: CONVERSION OPTIMIZATION LOOP

every friday, review metrics:

- sales page conversion rate
- email click rates
- headline performance

if any metric underperforming, prompt grok:

"current \[headline/email/CTA\] converts at \[X\]%

generate 10 variations testing different psychological approaches:

- 3 using curiosity gap
- 3 using specificity and numbers
- 2 using social proof
- 2 using urgency

keep same core message, vary the psychology"

implement best 2-3, test with small traffic, scale winner

compound effect: 4.2% → 4.9% → 5.8% → 7.1% over 12 weeks from weekly optimization

AUTOMATION 3: CONTENT MULTIPLICATION

every sunday, batch content:

prompt grok: "based on this manus research: \[paste problem insights\]

create 14 social posts (7 for twitter, 7 for linkedin)

twitter (thread format):

- hooks using manus customer language
- frameworks addressing validated pain points
- soft CTA to lead magnet

linkedin (long-form):

- professional tone
- problem → insight → solution structure
- case study format where relevant

for all posts:

- use specific examples from manus research
- include engagement question
- vary psychological angle"

grok generates 14 posts in 5 minutes, you review 30 minutes, schedule for 2 weeks

AUTOMATION 4: TESTIMONIAL MINING

when student gets result, prompt grok:

"based on these customer messages: \[paste conversation history\]

create testimonial in format:

- before state (specific metric)
- obstacle (what was blocking them)
- solution (how course helped)
- after state (specific metric)
- timeline (how long it took)
- direct quote (pull from their messages)

make it compelling but 100% accurate to their experience"

grok extracts perfect testimonial format from raw conversations

AUTOMATION 5: NICHE EXPANSION

once course is profitable, find adjacent opportunities:

prompt manus: "analyze discussions from people who bought \[your topic\] courses

what other problems do they frequently discuss? what adjacent topics appear in same conversations? what progression do they mention? (what comes after solving this problem)

rank expansion opportunities by:

- discussion volume
- audience overlap
- complementary nature"

manus identifies: "people who solve productivity also discuss delegation, so build delegation course next"

THE COST STRUCTURE (ABSURDLY PROFITABLE)

monthly tool costs:

- manus: $20/month
- grok: $8/month (via X premium)
- course platform: $39/month (teachable) or $0 (gumroad 10% fee)
- email: $29/month (convertkit)

total: $96/month for complete stack

revenue at $15k/month:

- gross: $15,000
- tools: $96 (0.6%)
- profit margin: 99.4%

compare to traditional:

- market research firm: $2,000 per report
- copywriter: $3,000 per sales page
- content creator: $5,000 per course
- total outsourcing: $10,000 per launch

grok + manus: $28/month traditional: $10,000 per product

357x cost advantage

THE REAL OPERATOR EXAMPLES

OPERATOR 1: REMOTE WORK PRODUCTIVITY

month 1:

- manus found: "async communication overwhelm for remote managers" (428 discussions, high urgency)
- grok wrote: complete funnel using exact manager language from manus
- launched: "async leadership system" at $1,297
- beta: 11 sales = $14,267

month 2-3:

- refined based on feedback
- optimized funnel with grok (conversion 4.1% → 8.3%)
- manus found adjacent: "delegation for remote teams"
- built course 2 in 8 days

month 4 revenue:

- course 1: 14 sales = $18,158
- course 2: 8 sales = $10,376
- total: $28,534

time weekly: 8 hours (mostly support, systems run themselves)

key advantage: manus + grok loop means both courses used validated language and converted immediately

OPERATOR 2: B2B LINKEDIN STRATEGIST

month 1:

- manus analyzed: linkedin content discussions, found "B2B founders struggle getting engagement despite consistent posting" (612 discussions)
- extracted exact frustration language: "posting daily for 3 months, still getting 4 likes, feels pointless"
- grok used that language in sales copy
- launched: "B2B content velocity system" at $1,497

beta + month 1: 18 sales = $26,946

month 2-4:

- manus weekly scans caught: "linkedin algorithm change discussion spike"
- quickly created: "algorithm update guide" as $97 add-on
- sold to existing students: 47 copies = $4,559
- main course: 22 sales monthly average = $32,934

month 4 revenue: $37,493

automation level: grok generates all content (15 min review), manus alerts to trends, nearly hands-off

OPERATOR 3: AI TOOLS EDUCATOR

month 1:

- manus found: "creators want AI help but overwhelmed by tool options" (891 discussions)
- unique insight from manus: people want "done-for-you prompts" not "learn prompting"
- grok positioned: "copy-paste prompt library" instead of "AI course"
- price: $497 (lower than courses, higher than templates)

launch: 23 sales = $11,431

month 2:

- manus found related: same people discuss "repurposing content"
- built: "AI repurposing prompt pack" at $297
- cross-sold to library buyers: 12 = $3,564
- new library sales: 19 = $9,443
- total: $13,007

month 3-6 progression:

- added 3 more specialized prompt packs ($197 each)
- monthly average: $24k-$31k from template/prompt products
- time: 4 hours weekly (manus scans, grok creates new prompts)

key insight: manus showed market wanted templates not courses, grok made templates convert like courses

COMMON THREAD: all used manus to validate, grok to convert, both tools working together creates speed + certainty impossible separately

THE STRATEGIC ADVANTAGES COMPOUNDING

advantage 1: SPEED TO MARKET DOMINANCE

traditional: 6-8 weeks validating + building + launching grok + manus: 8 days validating + building + launching

7-10x speed advantage means:

- test 8 ideas in time competitors test 1
- own niches before competition arrives
- respond to trends while they're hot
- iterate 10x faster based on feedback

advantage 2: CONVICTION AND CONFIDENCE

traditional: "i think this might work, hope people want this, fingers crossed" grok + manus: "manus shows 428 discussions with strong buy signals, this definitely has demand"

launching with certainty vs uncertainty:

- certainty → better copywriting (confident not desperate)
- certainty → higher pricing (you know value)
- certainty → persistent marketing (not giving up early)

advantage 3: CONVERSION SUPERIORITY

traditional: sales copy based on "best practices" and templates grok + manus: sales copy using actual customer language from thousands of conversations

conversion comparison:

- template copy: 2-4% conversion
- grok copy with manus language: 7-12% conversion

3-6x better conversion from same traffic = 3-6x more revenue

advantage 4: MARKET TIMING PRECISION

traditional: launch when you finish building (might miss trend window) grok + manus: manus shows you when problem is spiking, launch into momentum

example: manus showed "AI automation for solopreneurs" spiking march 2024, operator launched into rising demand, rode wave to $40k monthly

vs launching when trend is declining (uphill battle)

advantage 5: PORTFOLIO VELOCITY

traditional: maybe launch 2-3 products yearly (slow build cycles) grok + manus: can launch 8-12 products yearly (8-day cycles)

portfolio benefits:

- diversified revenue (not dependent on one product)
- cross-selling opportunities (bundle offers)
- audience segmentation (different products for different segments)
- faster learning (each launch refines system)

THE SCALING ROADMAP TO $15K MONTHLY

month 1: FIRST PRODUCT VALIDATION

- week 1: manus validation (3 hours)
- week 2: grok funnel + product build (16 hours)
- week 3: beta launch (8 hours)
- week 4: iterate based on feedback (6 hours)

result: 8-12 sales at $697-$997 = $5,580-$11,964 learning: proven system works, refined prompts

month 2: OPTIMIZATION + PRODUCT 2

- weeks 1-2: optimize product 1 funnel with grok testing
- weeks 3-4: manus finds adjacent problem, build product 2

result:

- product 1: 14-18 sales optimized = $9,758-$17,946
- product 2: beta 8 sales = $5,580-$7,976
- total: $15,338-$25,922

month 3: SYSTEMATIZATION

- week 1: automate manus weekly scans
- week 2: templatize grok prompts for reuse
- weeks 3-4: build product 3 using refined system

result:

- product 1: 18-22 sales = $12,546-$21,934
- product 2: 12-16 sales optimized = $8,364-$15,952
- product 3: beta 6 sales = $4,182-$5,982
- total: $25,092-$43,868

month 4-6: CONSISTENT EXECUTION

- monday: manus market scan (30 min)
- wednesday: grok content batch (45 min)
- friday: metrics review + optimization (60 min)
- monthly: launch new product or variation (16 hours)

stabilized monthly:

- 3 products averaging $12k-$18k each
- total: $36k-$54k monthly
- time: 8-12 hours weekly

$15K MONTHLY BASELINE ACHIEVED BY MONTH 2-3 $30K+ MONTHLY ACHIEVABLE BY MONTH 6

THE CRITICAL SUCCESS FACTORS

this works when you:

✓ TRUST MANUS DATA OVER GUT don't second-guess what manus shows, if 400+ discussions validate problem, build it

✓ USE EXACT CUSTOMER LANGUAGE copy verbatim quotes from manus into grok prompts, let grok weave them into copy naturally

✓ SHIP FAST DON'T PERFECT 8-day launch cycles mean you're testing and learning while others are still planning

✓ ITERATE BASED ON METRICS weekly grok optimization tests compound into massive conversion improvements

✓ BUILD PROMPT LIBRARY save winning manus queries and grok prompts, reuse and refine them

✓ FOCUS ON SYSTEM NOT PRODUCTS products are outputs, manus + grok system is the asset

this fails when you:

✗ VALIDATE WITH MANUS BUT IGNORE DATA don't cherry-pick findings that confirm your bias, follow the data

✗ USE GENERIC PROMPTS WITH GROK "write sales page" gets generic output, "write using these exact customer quotes" gets gold

✗ BUILD BEFORE VALIDATING temptation to skip manus and "just build," don't, you'll waste weeks on wrong thing

✗ OVER-EDIT GROK OUTPUT grok's copy works because it uses patterns that convert, over-editing removes the magic

✗ LAUNCH AND FORGET set up weekly optimization loop or you leave 50%+ revenue on table

THE BOTTOM LINE

you're either spending weeks manually researching topics you think might work, writing sales copy based on templates and best practices, launching products with 2-4% conversion that take months to build and might not have real demand

or

you're spending 90 minutes with manus analyzing thousands of real conversations to find validated demand, feeding that market intelligence to grok which writes conversion copy using actual customer language, launching complete products in 8 days that convert at 7-12% because demand was proven before you built anything

the grok + manus combination isn't about using two AIs instead of one

it's about using specialized tools that create feedback loop: manus validates what to build, grok converts it into revenue using the same language patterns manus discovered

cost: $28/month time to first revenue: 8 days conversion rate: 3-6x better than template copy confidence level: data-driven not gut-driven scaling velocity: 8-12 products yearly vs 2-3

operators using this exact stack are doing $15k-$35k monthly within 90-120 days while spending 8-12 hours weekly

traditional info creators are spending 40 hours weekly for 6 months to maybe hit $8k monthly

10x speed, 3x revenue, 75% less time

the window for this advantage is 12-18 months before it becomes common knowledge

right now maybe 500 people globally understand this specific grok + manus synergy

by late 2027 everyone will, and competitive advantage disappears

choose accordingly

i've built the AI INFO HUB that shows you how to make $20k/m selling digital guides using claude, grok & manus (without audience, ads, or months of 'building')

the exact system for launching 5-10 validated info products in 60 days using AI - while everyone else is still "planning" their first one

here's what you'll get:

- the AI trinity stack - exact workflows for manus (research), grok (positioning), claude (creation)
- the 48-hour product build - template for creating $47-$247 guides that actually sell
- reddit cash system - how to make $10k-$30k/month with low-ticket guides on reddit
- twitter outbound playbook - find buyers TODAY using advanced search + AI personalization
- portfolio approach - build 5-10 products simultaneously, scale the winners
- faceless account strategy - run multiple income streams without personal brand
- zero-cost workflow - how to hit 5-figures with completely free tools (if you're broke)
- DM closing scripts - AI-powered responses that close at 50%+ without calls

pre-launch sale is live rn, DM me to join

---

**作者** David Ondrej（@DavidOndrej1）  
**貼文連結** https://x.com/DavidOndrej1/status/2010776839736656044  

**正文**

Claude 4.5 Opus is down.

it's over.

---

**作者** Xiangyi Li（@xdotli）  
**貼文連結** https://x.com/xdotli/status/2010805530546356285  

**正文**

Announcing SkillsBench Week 1 updates:
We're building the first benchmark that measures how well skills work and how well agents use skills. In the first week we are able to grow significantly in task numbers and the contributor community.
Early results: Skills boost agent performance by up to 27%:
• Codex GPT-5.2: +13% improvement with skills (0.645 → 0.729)
• Claude Code Opus 4.5: +27% improvement with skills (0.395 → 0.500)
In just two weeks, we've grown to:
➡️ 440+ community members
➡️ 120+ signed contributors (~70% PhD candidates or holders)
➡️ 8 tasks merged, 44 in pipeline
➡️ 100% human-written tasks reflecting real-world scenarios
We're also honored to have first authors of Screenspot Pro, MCP-Universe, and BigCodeBench contributing to the benchmark.
📢 We're recruiting contributors for ICML and CAIS 2026 submissions. Contributors of 1-3 tasks receive co-authorship (based on task complexity). Contributions after the ICML deadline carry over to future publications.
Learn more: link in comments
Special shout out to the creator of harbor @alexgshaw @Mike_A_Merrill @LaudeInstitute; we couldn't have moved this fast if we didn't use harbor as our harness environment since day 1. As a harbor and terminal bench contributor, I'm also excited to see more harbor based benchmarks come to life!

---

**作者** Frank Wang 玉伯（@lifesinger）  
**貼文連結** https://x.com/lifesinger/status/2010635657937645669  

**正文**

安德森是 a16z 的联合创始人，在采访中，关于创业 PMF 和护城河的观点，非常有价值。

1、找到 PMF 后，创业公司最重要的事情之一，是建立分销渠道。世界真大，如何把产品送到目标客户手中，是 PMF 后第一重要的事。成功科技公司的模式，总体上是以分销为中心，而不是以产品为中心。

2、找到 PMF 后，第二重要的事，是开始做下一个产品或下一个功能。产品永远有周期，并且会被淘汰得很快。做不出新产品或新功能，就很容易在竞争中迅速败落。

3、构建有 PMF 的产品，建立分销渠道，这两件事情之外，只剩下第三件事：“其他所有事”，都围绕产品和分销来发展公司。比如财务、法务、合规、公关、投资者关系、人力资源等等。

4、网络效应和数据，都很难成为壁垒。网络效应来得快，去的往往更快。你能拿到的数据，别人也能拿到。可控的分销渠道，反而是最大的壁垒。

5、凡是有钱赚的，都会有竞争。并不存在什么独一无二的产品。大厂可以通过模仿或并购牢牢占据市场份额。典型的是 Google。大部分你以为是 Google 原创的产品，其实都是并购来的。

6、高定价等于高增长。创始团队往往会通过低定价，来扩大业务规模。这是一种鸦片。只有不断提价、提价、再提价，才能验证是否真的有护城河。提价就是打开天窗说亮话。有能力收取高价，才是护城河。

7、独立项目组，是产品创新的关键。

很有意思的是，以此去思考 Monica 和 Manus 的发展，会发现以上全中。

Monica 让肖弘团队具备了很强的分销渠道能力。Manus 是肖弘团队的第二个产品，并且一开始是独立的创新项目组。Manus 的定价完美证明了高定价高增长。

以上。希望对你有所启发。

---

**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2010817497340187076  

**正文**

Claude 的新功能 Cowork：让 AI 真正帮你干活

Claude Code 本来是给程序员写代码用的，结果大家发现它整理文件、做表格、写报告也很顺手。Anthropic 索性把这套能力包装成了 Cowork，让不会写代码的人也能用上。

【1】Cowork 到底能干啥

你选一个电脑上的文件夹，Claude 就能在里面读文件、改文件、创建新文件。

听起来简单，用起来挺香。比如你下载文件夹乱成一锅粥，让它帮你分类重命名。或者你有一堆消费截图，它能整理成一张 Excel 表。再比如你写了几页凌乱的笔记，它能帮你理顺思路、输出初稿。

和普通对话不一样的是，Cowork 模式下 Claude 更像个真正的助手。你布置任务，它自己规划步骤、一步步执行，中间会告诉你进度。如果你用过 Claude Code，这感觉会很熟悉，因为底层技术是同一套。

【2】还能更强

基础功能只是起点。Cowork 可以接上你已有的连接器，比如 Google Drive、Slack。它还内置了一批技能，能更好地生成文档、PPT 之类的文件。再配上 Chrome 浏览器插件，Claude 甚至能帮你操作网页。

这套设计让工作流变得很丝滑。你不用反复给 Claude 喂上下文，也不用手动把输出转成正确格式。甚至不用等它做完一件事再布置下一件，可以连续丢任务让它并行处理。用 Anthropic 的话说，这感觉不像你一句我一句地聊天，更像给同事留便签。

【3】和 Claude Code 共享技能生态

对 Claude Code 用户来说有个好消息：Cowork 能读取你本地的 http://CLAUDE.md 文件和自定义 Skills。

我测试了一下，选择工作文件夹后，Cowork 能看到里面的 http://CLAUDE.md 并按指令执行。我在 Claude Code 里配置的写作风格技能，Cowork 里也能直接调用。技能分两类：Anthropic 官方提供的（docx、pptx、pdf 这些）和用户自己创建的，两类都能用。

换句话说，你在 Claude Code 里攒下的工作流配置可以直接迁移过来。Cowork 不是另起炉灶，是同一套体系的图形化入口。

有个坑要注意：Cowork 跑在 Linux 虚拟机里，而你的 Mac 是 ARM 架构。如果技能依赖 node_modules 或本地特定环境（比如浏览器 cookies、特定架构的二进制文件），就跑不了。我试着调用一个需要运行 nodejs 脚本的图片生成技能，报错了——架构不兼容。纯文本类的配置（http://CLAUDE.md、写作规范）没问题，涉及本地脚本的技能可能需要额外适配。

【4】安全边界在哪里

Claude 只能访问你明确授权的文件夹和连接器，动作比较大的时候会先问你。但有几件事得提前知道：Claude 可能会误解你的指令，如果你说"清理一下这个文件夹"，它可能真的把文件删了。指令要说清楚。

另一个风险是提示词注入，就是攻击者在网页内容里藏一些指令，试图劫持 Claude 的行为。Anthropic 说他们做了防护，但这个领域整个行业都还在摸索。

这些风险不是 Cowork 特有的，只是很多人可能是第一次用这种更自主的 AI 工具。官方建议：刚开始用的时候谨慎点，别一上来就让它处理重要文件。

【5】现在能用吗

Cowork 目前是研究预览版，只对 Mac 上的 Claude Max 订阅用户开放。Anthropic 想先看看大家怎么用、有什么反馈，然后快速迭代。后面会加跨设备同步，也会出 Windows 版。

这一步到是意料之中，因为 Claude Code 现在已经被用在很多编程意外的领域，但是门槛略高，限制了使用群体是程序员或者懂点技术的用户，而且脚本执行权限会有很多安全上的隐患。Cowork 一下子降低了使用的门槛，通过图形化界面就可以操作，并且也让使用更安全。

现在还是早期版本，能做的事有限，安全机制也在完善中。但如果你是 Max + Mac 用户，值得一试。

---

**作者** indigo（@indigox）  
**貼文連結** https://x.com/indigox/status/2010857985879523406  

**正文**

Claude 上线 CoWork - 可以在你本地运行的通用 Agent ✨

- Claude Code 替代初级程序员
- Claude CoWork 替代白领牛马

大家安装 Claude Desktop 尊贵的 Max Plan 用户就会看到左侧 Code 旁边多出了一个 CoWork Tab！选择一个工作目录，你在电脑上干的工作它几乎都能干
 

---

**作者** Garrett Scott 🕳（@thegarrettscott）  
**貼文連結** https://x.com/thegarrettscott/status/2010780608084263049  

**正文**

Today, @doanythingapp uses a chat interface, but we all know this isn't the best for long running agents.

On Wednesday, I am dropping a very unique interface option that I think will become your favorite, especially on the app.

What other interfaces do you want to see us try?

---

**作者** Claude（@claudeai）  
**貼文連結** https://x.com/claudeai/status/2010805682434666759  

**正文**

Introducing Cowork: Claude Code for the rest of your work.

Cowork lets you complete non-technical tasks much like how developers use Claude Code. 
Introducing Cowork: Claude Code for the rest of your work.

Cowork lets you complete non-technical tasks much like how developers use Claude Code. 
In Cowork, you give Claude access to a folder on your computer. Claude can then read, edit, or create files in that folder.

Try it to create a spreadsheet from a pile of screenshots, or produce a first draft from scattered notes. 
Once you've set a task, Claude makes a plan and steadily completes it, looping you in along the way.

Claude will ask before taking any significant actions so you can course-correct as needed.
Claude can use your existing connectors, which link Claude to external information.

You can also pair Cowork with Claude in Chrome for tasks that need browser access.
Cowork is available as a research preview for Claude Max subscribers in the macOS app. Click on “Cowork” in the sidebar: https://claude.com/download

If you're on another plan, join the waitlist for future access here: https://forms.gle/mtoJrd8kfYny29jQ9
Read more: http://claude.com/blog/cowork-research-preview

---

**作者** Nick Khami（@skeptrune）  
**貼文連結** https://x.com/skeptrune/status/2010813552529969599  

**正文**

many startups just died today.

---

**作者** GeekPlux（@geekplux）  
**貼文連結** https://x.com/geekplux/status/2010851389396631609  

**正文**

又一批 AI 创业公司死了

---

**作者** Kevin Grajeda（@k_grajeda）  
**貼文連結** https://x.com/k_grajeda/status/2010760912094052773  

**正文**

feel the future 
feel the future 
want to try? it is @Dessn_ai

---

**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2010852013874045284  

**正文**

原文：The Next Two Years of Software Engineering 
URL：https://addyosmani.com/blog/next-two-years/
作者：Addy Osmani

软件行业正面临一个奇怪的拐点。AI 编程已从单纯的“超级自动补全”，进化为能自主执行开发任务的 AI 智能体 (AI Agents)。曾经助推科技界“抢人大战”的经济泡沫已破，取而代之的是对效率的硬性指标：企业现在更看重利润而非增长，更青睐老手而非应届生，更倾向于用神兵利器武装精简的团队。

与此同时，新一代开发者正步入职场，心态截然不同：他们务实地追求职业稳定，质疑“内卷文化”（hustle culture），并且从入行第一天起就是 AI 的原住民。

未来充满了不确定性。以下是将在 2026 年之前重塑软件工程的五个关键问题，我为每个问题设想了两种截然不同的情景。这并非预言，而是帮助大家做准备的透镜。目的是基于当下的数据，结合社区特有的良性怀疑精神，为应对未来提供一份清晰的行动指南。

---

## 1. 初级开发者问题

核心结论：随着 AI 接管入门级任务，初级招聘可能崩盘，也可能随着软件渗透各行各业而反弹。两种未来，生存法则截然不同。

传统的“学编程、找工作、升高级”路径正在动摇。哈佛大学一项涵盖 6200 万工人的研究显示，企业采用生成式 AI 后，初级开发者就业率在六个季度内下降了约 9-10%，而高级开发者几乎不受影响。过去三年，[大型科技公司对应届生的招聘腰斩](<https://restofworld.org/2025/engineering-graduates-ai-job-losses/>)。有位工程师曾讽刺道：~“既然 AI 编程智能体更便宜，何必花 9 万美元雇个初级新手？”

这不全赖 AI。[利率上升和疫情后的修正等宏观因素](<https://www.2ndorderthinkers.com/p/are-junior-level-jobs-really-killed>)在 2022 年就已造成冲击。但 AI 加速了这一趋势。现在，一个高级工程师配上 AI，能抵得上过去一个小团队。公司倒也没怎么大裁员，而是悄悄关上了初级招聘的大门。

反转情景：AI 释放了各行各业对开发者的巨大需求。医疗、农业、制造和金融业都开始通过软件实现自动化。AI 非但没取代开发者，反而成了“力量倍增器”，将开发工作扩展到了从未雇佣过程序员的领域。我们将看到更多入门级角色，只是形式变了：即“AI 原生”开发者，快速为特定细分领域构建自动化方案。

[美国劳工统计局仍预计](<https://www.cio.com/article/4062024/demand-for-junior-developers-softens-as-ai-takes-over.html>) 2024 至 2034 年间软件岗位将增长约 15%。如果企业用 AI 是为了扩大产出而非单纯砍人头，[他们将需要人类来抓住 AI 创造的机会](<https://www.2ndorderthinkers.com/p/are-junior-level-jobs-really-killed>)。

悲观情景有个常被忽视的长期风险：今天的菜鸟是明天的大神。切断人才输送管道，5 到 10 年后就会出现领导力真空。[行业老兵称之为“慢性衰退”](<https://www.finalroundai.com/blog/ai-is-making-it-harder-for-junior-developers-to-get-hired>)：一个不再培养接班人的生态系统。

应对策略：

初级开发者：精通 AI，做个多面手。证明“你 + AI”能抵得上一个小团队。利用 AI 编程智能体（Cursor/Antigravity/Claude Code/Gemini CLI）构建大功能，但要理解并能解释每一行代码。死磕 AI 难以替代的技能：沟通、拆解问题、领域知识。关注邻近角色（QA、开发者关系、数据分析）作为切入点。建立作品集，特别是集成 AI API 的项目。考虑学徒制、实习、合同工或开源项目。别做“待培训的应届生”，要做能快速学习、即插即用的工程师。

高级开发者：初级人员减少，意味着更多脏活累活会落到你头上。依靠自动化处理常规任务，但别事必躬亲。设置 CI/CD、代码检查器（linters）和 AI 辅助测试来捕捉基础问题。通过开源或指导同事进行非正式辅导。[向管理层坦诚“全高级团队”的风险](<https://www.finalroundai.com/blog/ai-is-making-it-harder-for-junior-developers-to-get-hired>)。如果初级需求反弹，做好有效带人和委派任务的准备。你的价值在于放大整个团队的产出，而不仅仅是贡献代码。

---

## 2. 技能问题

核心结论：随着 AI 包办大部分代码，核心编程技能可能退化，也可能因人类转向监督角色而变得前所未有的重要。未来几年将决定：我们是牺牲理解换速度，还是两者兼得。

[84% 的开发者现在经常使用 AI 辅助](<https://stackoverflow.blog/2025/09/10/ai-vs-gen-z/>)。许多人遇到 Bug 或新需求，第一直觉不再是写代码，而是写提示词（Prompt）并拼接 AI 生成的片段。入门级程序员正在跳过“练基本功”的阶段：他们可能永远不会手写二叉搜索树，也不会独自调试内存泄漏。

技能天平正在倾斜：从实现算法转向懂得向 AI 提问并验证其输出。[职业阶梯的第一级现在考的是提示和验证 AI](<https://www.cio.com/article/4062024/demand-for-junior-developers-softens-as-ai-takes-over.html>)，而非生写代码的蛮力。一些高级工程师担心这会造就一代“去技能化”的开发者，无法独立写出好代码。AI 生成的代码可能藏着微小的 Bug 和安全漏洞，经验不足的开发者很难发现。

反转情景：AI 处理那 80% 的常规工作，人类死磕那 20% 的硬骨头。架构、棘手的集成、创造性设计、边缘情况——这些是机器搞不定的。AI 的普及非但没让深度知识过时，反而让专家经验变得价值连城。这就是“高杠杆工程师”：利用 AI 放大力量，但必须深刻理解系统才能驾驭它。

如果人人都有 AI 编程智能体，区分高下的标准就是知道 AI 何时在胡说八道。[正如一位高级工程师所言](<https://www.cio.com/article/4062024/demand-for-junior-developers-softens-as-ai-takes-over.html>)：“最好的软件工程师不是写代码最快的人，而是懂得不信任 AI 的人。”

编程方式在转变：少打样板代码，多审查逻辑错误、安全缺陷和需求偏差。关键技能变成了软件架构、系统设计、性能调优和安全分析。[AI 可以秒生成 Web 应用，但专家能确保它符合安全规范](<https://www.cio.com/article/4062024/demand-for-junior-developers-softens-as-ai-takes-over.html>)，且没有引入竞态条件（Race Conditions）。

2025 年的开发者舆论严重分裂。有人承认几乎不再“亲手”写代码，呼吁面试改革；有人则认为跳过基础会导致 AI 出错时无力“救火”。[行业开始期待工程师两者兼备](<https://www.cio.com/article/4062024/demand-for-junior-developers-softens-as-ai-takes-over.html>)：既有 AI 的速度，又有保证质量的内功。

应对策略：

初级开发者：把 AI 当学习工具，别当拐杖。当 AI 建议代码时，搞懂它为什么行，找出它的弱点。偶尔关掉 AI，徒手写关键算法。扎实 CS 基础：数据结构、算法、复杂度、内存管理。把项目做两遍：一遍用 AI，一遍徒手，对比差异。学习提示工程（Prompt Engineering），精通工具。刻意练习严格测试：写单元测试，看懂堆栈跟踪（别一上来就问 AI），熟练使用调试器。深耕 AI 无法复制的软实力：系统设计、用户体验直觉、并发推理。展示你既能用 AI 极速产出，又能在 AI 歇菜时力挽狂澜。

高级开发者：做质量和复杂度的守门员。磨练核心专长：架构、安全、扩展性、领域知识。练习用包含 AI 组件的模型设计系统，推演故障模式。时刻警惕 AI 代码中的漏洞。拥抱导师和审查者的角色：界定哪里能用 AI，哪里必须人工审查（如支付或安全代码）。投入创造性和战略性工作；让“初级人员+AI”处理常规接口，你来决定建哪些接口。投资软技能和跨领域知识。紧跟新工具。加倍投入人类开发者的不可替代性：健全的判断力、系统级思维和指导能力。

---

## 3. 角色定位问题

核心结论：开发者角色可能缩水为单纯的审计员（监督 AI 代码），也可能扩展为设计和治理 AI 系统的核心编排者。无论哪条路，想创造价值，光写代码已经不够了。

两极分化十分严重。悲观视角下，开发者的创造性被剥夺。他们不再构建软件，只是审计和看管 AI 的输出。AI 系统（或使用无代码平台的“公民开发者”）负责生产；人类负责审查、纠错、查重和批准。制造者变成了检查者。风险管理的焦虑取代了创造代码的乐趣。

有报告称，工程师花更多时间评估 AI 生成的合并请求（Pull Requests）和管理自动化管道，写代码的时间反而少了。编程不再像创造性地解决问题，更像是合规检查。一位工程师感叹：“我不想沦为代码保洁员，专门清理 AI 扔过墙来的垃圾。”

另一种未来则有趣得多：开发者进化为高级编排者，集技术、战略和伦理责任于一身。AI 只是“工人”，人类开发者是架构师或总包商，设计系统、分配任务、将众多组件编织成网。

[某低代码平台 CEO 描绘了这一愿景](<https://www.cio.com/article/4062024/demand-for-junior-developers-softens-as-ai-takes-over.html>)：在“代理式（Agentic）”开发环境中，工程师变身“作曲家”，指挥 AI 智能体和软件服务协同演奏。他们不亲自写每一个音符，但定义旋律：架构、接口、智能体交互方式。这个角色跨学科且充满创造力：集软件工程、系统架构和产品策略于一身。

乐观来看：AI 处理了死记硬背的工作，迫使开发者转向高价值活动。工作可能更有趣了。总得有人决定 AI 该造什么，验证产品是否合理，并持续改进。

局势取决于组织如何整合 AI。视 AI 为裁员工具的公司，会让剩下的工程师当保姆维持运转。视 AI 为增效工具的公司，会保持团队规模，但要求交付更宏大的项目。

应对策略：

初级开发者：寻找写代码之外的机会。主动承担写测试用例、设 CI 管道或应用监控的任务：这些技能符合审计/维护者的角色。通过个人项目保持创造热情，别丢了构建的乐趣。培养系统思维：学习组件如何通信，什么才是好 API。阅读工程博客和系统设计案例。熟悉代码生成以外的 AI 工具：编排框架、AI API。提升沟通能力（书面和口头）。写文档要像给别人讲课一样。问资深同事问题时，别只问“能跑吗？”，要问“我想全了吗？”。准备好成为验证者、设计者和沟通者，而不仅仅是码农。

高级开发者：向领导力和架构职责靠拢。制定标准，确立框架。定义代码质量清单和 AI 伦理规范。关注 AI 软件的合规与安全。深耕系统设计和集成；主动梳理跨服务数据流，识别故障点。熟悉编排平台（Kubernetes, Airflow, Serverless, Agent 工具）。加倍投入技术导师角色：多做代码审查、设计讨论、技术指导。练就一眼看穿代码（人写的或 AI 写的）本质的能力。培养产品和商业嗅觉；理解功能背后的商业逻辑。跟随产品经理，倾听客户声音。通过原型、黑客马拉松或新技术研究保护你的创作火花。从代码员进化为指挥家。

---

## 4. 专才 vs. 通才问题

核心结论：路走窄了的专才恐被自动化淘汰。在快速变化、AI 渗透的环境下，T 型工程师更吃香：既有广泛的适应力，又有一两手绝活。

鉴于模型、工具和框架兴衰更迭极快，押注单一技术栈风险极大。当新 AI 工具能轻松搞定某项技术时，该领域的旧日大师可能会突然发现自己不再抢手。那些死守“单一技术栈、框架或产品”的开发者，可能一觉醒来发现天变了。

想想那些没随行业转型的 COBOL 开发者、Flash 开发者或移动引擎专家吧。现在的不同在于变化的速度。AI 自动化让某些编程任务变得微不足道，直接削弱了相关岗位的价值。如果一个专家只会微调 SQL 或切图，AI 能替他干 90% 的活。

招聘经理永远在追逐最新的利基市场。前几年是云基础设施，现在是 AI/ML。死磕过气技术的人，会随着领域退潮而陷入停滞。

相反，新形式的专业化——“多才多艺的专家”或 [T 型开发者](<https://www.youtube.com/watch?v=IMHneaMO-dg>)正在崛起。一竖是深厚的专精领域，一横是广泛的涉猎。[这些工程师是多学科团队的“粘合剂”](<https://medium.com/nerd-for-tech/beyond-full-stack-the-rise-of-the-t-shaped-developer-a4afd757d976>)，能跨界交流，填补空白。

[公司不再想要太浅或太窄的开发者](<https://medium.com/nerd-for-tech/beyond-full-stack-the-rise-of-the-t-shaped-developer-a4afd757d976>)；他们想要核心强、能跨栈的人。一来是为了效率：T 型人才无需等待交接，能端到端解决问题。二来是为了创新：知识交叉能碰撞出更好的方案。

AI 工具其实是通才的神器。后端工程师可以用 AI 做个像样的 UI；前端专家可以用 AI 生成服务端代码。AI 让人的能力边界大幅拓展。反观深度专才，领地被自动化蚕食，却难以突围。

[近 45% 的工程职位现在要求精通多领域](<https://medium.com/nerd-for-tech/beyond-full-stack-the-rise-of-the-t-shaped-developer-a4afd757d976>)：编程 + 云基建，或者前端 + ML 基础。

应对策略：

初级开发者：尽早打好宽基。即便为了特定岗位入职，也要把头探出孤岛看世界。做移动端就学学后端；做前端就试试写个 Server。学习 Docker 或 GitHub Actions 等部署工具。找到一两个真正让你兴奋的领域深钻，作为垂直专长。把自己打造为混合型人才：“专注云安全的全栈”或“懂 UX 的前端”。利用 AI 快速扫盲新领域；对后端一窍不通？让 ChatGPT 写个 API 范例研究下。养成持续重塑技能（re-skilling）的习惯。参加黑客马拉松或跨职能项目，逼自己做通才。告诉经理你想接触项目的不同部分。适应力是你早期的超能力。

高级开发者：绘制技能图谱：哪是专长？哪是皮毛？选一两个相邻领域，练到能对话的程度。你是后端数据库专家？去学学现代前端框架或 ML 管道。在弱项领域用 AI 辅助做个小项目。将深厚专长与新语境结合；比如专精 Web 性能，就去研究 ML 推理优化。设计你的角色，让它更跨职能。主动当多领域项目的“集成冠军”。指导他人，互通有无。更新简历，体现多面手能力。利用经验识别模式，迁移知识。做 T 型人才的榜样：在专业领域深耕（这是你的底气），但积极横向拓展。

---

## 5. 教育问题

核心结论：CS 学位还是金字招牌吗？还是会被训练营、在线平台和企业培训等“快车道”超车？行业数月一变，大学恐怕追赶乏力。

四年制计算机科学学位长期以来是入行的硬通货。但这一传统正受到挑战。

一种未来：大学依然重要，但日益脱节。学位仍是门槛，但课程更新慢、审批流程长，跟不上需求。学生和雇主觉得学术界与工业界是两个世界，教的理论变不成干活的技能。

应届生反映，在校没学过云计算、现代 DevOps 或 AI 工具。如果大学耗费巨资和时间，却提供低相关性的教育，它们就有被视为昂贵“守门人”的风险。但许多公司惯性使然，仍要求本科学位，压力全在学生身上——得靠训练营和网课自救。

[学生背负巨额债务，企业却要花数十亿培训应届生](<https://campustechnology.com/articles/2025/10/21/solving-the-talent-crisis-starts-in-higher-ed.aspx>)，因为他们缺乏职场技能。大学可能加门 AI 伦理课，添个云计算选修，但等落实时，行业工具早换代了。

颠覆性情景：新体系正日益取代传统教育。编程训练营、在线认证、实战作品集、企业内训学院正在崛起。[2024 年，近 45% 的公司计划取消部分职位的学位要求](<https://campustechnology.com/articles/2025/10/21/solving-the-talent-crisis-starts-in-higher-ed.aspx>)。

训练营已经成熟。毕业生也能进大厂。这些项目短平快（12 周），主攻实战：主流框架、云服务、团队协作。招聘的硬通货正变为实时作品集、微证书和实战技能。一个漂亮的 GitHub 主页或硬核证书，能帮你绕过学位门槛。

企业驱动的教育正在兴起：公司自建培训管道或联手训练营。大厂甚至开设内部“大学”。AI 本身也提供了新路径：AI 导师、交互式沙盒、个性化辅导。

模块化学习比昂贵的学位更普惠。只要有网，任何地方的孩子都能上 Coursera，做出和硅谷人才一样的作品集。

应对策略：

有抱负/初级开发者：别光指望学位。用实战项目补课：建个网站，给开源项目提个 PR。找实习。如果课程落伍，就上网自学。考取行业认可证书（GCP, AWS, Azure）证明动手能力。如果是自学或上训练营，打磨作品集：至少有一个文档完善的硬核项目。活跃于社区：贡献开源，写技术文章。混 LinkedIn、参加聚会，建立人脉。找老司机为你背书。保持持续学习；技术保质期很短。把 AI 当私人导师。用具体方式证明实力：作品集、证书、能侃侃而谈项目细节，这些才是敲门砖。

高级开发者和领导者：一纸文凭吃不了一辈子。投资继续教育：网课、工作坊、大会、考证。以新方式验证技能；准备好在面试中解决实际问题。用新技术做副业。重新评估招聘要求：真的非要 CS 学位吗，还是看重技能和学习力？推动“技能优先”招聘，扩大人才池。支持内训或学徒制。建立导师圈，帮带非科班出身的新人。与教育机构互动：反馈课程差距。在职业发展中践行一点：实战成就和持续学习，远比多拿个学位重要。

---

## 结语

这些情景并非非此即彼。现实往往是混合体。有的公司削减初级岗位，有的在新领域扩招。AI 自动化了常规代码，却拔高了人类代码的标准。开发者可能上午审查 AI 输出，下午设计高层架构。

贯穿始终的主线是：唯一不变的是变化本身。紧跟趋势并保持怀疑，你就不怕被炒作忽悠，也不怕被末日论吓倒。更新技能、做多面手，并专注于人类独有的特质（创造力、批判性思维、协作），你将始终立于不败之地。

无论未来是迎来编程复兴，还是代码自我编写的世界，永远需要这样一种工程师：思考全面、持续学习、用技术解决真问题。

预测未来的最好方式，就是亲手创造它。

---

**作者** 花果山大圣（@shengxj1）  
**貼文連結** https://x.com/shengxj1/status/2010443712829256088  

**正文**

最近学了点神经网络入门，满足自己的好奇心确实是一个非常 happy 的事情
然后准备好好学一下收藏夹里一堆 agentic pattern 的文章和书了，也欢迎大家推荐学习资料
正在看 google 那本《agentic design pattern》和 opencode 的代码

其实我觉得learn-claude-code这个教程也不错，极简的代码助手是如何实现的
https://github.com/shareAI-lab/learn-claude-code

---

**作者** vas（@vasuman）  
**貼文連結** https://x.com/vasuman/status/2010467926261014742  

**正文**

Love to see such a bright and thorough understanding of AI from someone so young. Give this a read.

---

**作者** Ian Nuttall（@iannuttall）  
**貼文連結** https://x.com/iannuttall/status/2010617350207451382  

**正文**

This is the best write up of the Ralph technique I’ve seen for non-technical users to understand 

Check the example repo for a cursor port and just ask your agent of choice to make it work for claude/codex/droid

Don’t use anthropic Ralph plugin!

---

**作者** David Haber（@dhaber）  
**貼文連結** https://x.com/dhaber/status/2010755274433257843  

**正文**

I believe that most investors are running funds, and very few people are building firms. What do I mean by that? A fund, by my definition, has a single objective function: “how do I generate the most carry with the fewest people in the shortest amount of time?” Whereas a firm, in my definition, has two objectives. One is delivering exceptional returns, but the second is equally interesting: “How do I build a source of compounding competitive advantage?”

Funds get more fragile with scale. So building competitive advantage becomes existential if you want to build an institution that endures. The problem is, that isn’t how fund managers are encouraged to spend their time or their focus. Most funds are run by an alpha decision maker who oversees all investments. They spend most of their time thinking about the next marginal deal, and not much time thinking about their moats. Compensation structures reward investment returns, split among small teams.

Firms, on the other hand, are run by entrepreneurs. And entrepreneurs think constantly about competitive advantage. Many of the world’s great enduring financial institutions think this way. Apollo thinks a lot about compounding competitive advantage, with their permanent capital structures. Goldman Sachs has a compounding competitive advantage with the embedded distribution of their wealth management division, who can fill a new fund instantly. Firms like Renaissance Technologies, D.E. Shaw, and Two Sigma invested a lot into technology and data to give them an edge. Firms are product companies in this way: they have to build a product that wins in the market, that is defensible and isn’t obvious.

Firms also have more decentralized decision-making structures than funds. This is both by design (to build a 100-year compounding machine, you need a deep bench of leaders who you can trust with big decisions), and by necessity (because the CEO’s focus is on building a business, not on the next marginal investment.) When your competitive advantage is constantly changing, there’s a positive-sum project to work on (building and re-building your moat) that helps a loosely coupled org stay organized and aligned.

Venture Capital is almost always run in the “fund” model, with a small number of investors and often a single “alpha” decision maker. The fund spends its time thinking about its investments, since competitive advantage has historically been all about brand and reputation, which comes from the “human network effect” of backing great founders and returning legendary funds.

But since day 1 of Andreessen Horowitz, @pmarca and @bhorowitz have thought about VC as a product for entrepreneurs, rather than as a fund to manage. And so they’ve built @a16z much more like a firm that builds products, decentralizes its decision-making, and thinks obsessively about new sources of competitive advantage. This gives a16z some unique characteristics:

1. We have entrepreneurs like Alex Rampell, Martin Casado, David Ulevitch and Chris Dixon leading their investment areas who you’d have a really hard time recruiting into a traditional fund model to work for someone else. Marc & Ben aren’t approving their investment decisions; they’re busy running the firm, so those leaders get genuine autonomy to make investments and build their teams. They get their own P&L, their paintbrush to paint a masterpiece, and the entrepreneurial freedom to shape their products to best serve their customers (entrepreneurs).
1. We’ve invested a huge amount into “platform”, which is a product for founders to accelerate their hiring, marketing, sales, and more. This is our war machine that we put to work on behalf of our founders, to use our scale to tilt the board in their favor. This platform costs hundreds of millions of dollars a year in expenses; it’s not cheap. But we do it because it’s a source of durable competitive advantage that a “fund” could never justify making. (Many of our competitors talk about their “platform team”, but they often mean the two people doing recruiting, and a marketer. We have 400 people who spend all day helping companies win. These are not the same!)
1. Therefore, because the firm is full of entrepreneurs and resources and product leverage, we can react quickly and decisively when a new opportunity comes up to build competitive advantage, while still enjoying our compounding economics of scale. Everyone at the firm is focused on their contribution to the product, not just their share of the returns.

This is the kind of vehicle you want to build, if you want your institution to last 100 years.

---

**作者** Ryan Carson（@ryancarson）  
**貼文連結** https://x.com/ryancarson/status/2010467429177237534  

**正文**

Another amazing way to use Ralph is to complete tons of user testing in the browser.

I create a list of 10-20 detailed user testing scenarios (I specify that all acceptance criteria must be able to be judged by Amp using Chrome Dev Tools vs a human) and then I put them in a Ralph loop with Amp.

Waaaay more testing than I would’ve ever done by hand. 

Then at the end I ask Amp to review progress.txt and tell me how it went.

---

**作者** Yanhua（@yanhua1010）  
**貼文連結** https://x.com/yanhua1010/status/2010690881397940340  

**正文**

推荐一些我目前安装的Claude Skills:

1. Anthropic官方Skills
https://github.com/anthropics/skills

2. Superpowers
1.6万Star的Skill精选，从脑暴、写需求文档、开发、测试全包含，口碑相当好。
https://github.com/obra/superpowers

3. Planning-with-files
参考Manus的Agent方法写的Skill。很适合多步骤任务，用这个Skill指导其他Skill工作也挺好。
https://github.com/OthmanAdi/planning-with-files

4. X-article-publisher-skill
王树义老师写的X文章发布Skill， 这个值得研究下，后续看看能不能实现其他平台的自动化
https://github.com/wshuyi/x-article-publisher-skill

5. NotebookLM skill
自动上传PDF、Youtube链接到NotebookLM，很适合NotebookLM内容的自动化处理
https://github.com/PleasePrompto/notebooklm-skill

还有一些是自己平时总结的内容创作skills，后续继续分享具体使用场景案例！
推荐一些我目前安装的Claude Skills:

1. Anthropic官方Skills
https://github.com/anthropics/skills

2. Superpowers
1.6万Star的Skill精选，从脑暴、写需求文档、开发、测试全包含，口碑相当好。
https://github.com/obra/superpowers

3. Planning-with-files
参考Manus的Agent方法写的Skill。很适合多步骤任务，用这个Skill指导其他Skill工作也挺好。
https://github.com/OthmanAdi/planning-with-files

4. X-article-publisher-skill
王树义老师写的X文章发布Skill， 这个值得研究下，后续看看能不能实现其他平台的自动化
https://github.com/wshuyi/x-article-publisher-skill

5. NotebookLM skill
自动上传PDF、Youtube链接到NotebookLM，很适合NotebookLM内容的自动化处理
https://github.com/PleasePrompto/notebooklm-skill

还有一些是自己平时总结的内容创作skills，后续继续分享具体使用场景案例！
安装的话，如果你想省事，直接在cc里面输入：
“安装下面的skills：GitHub链接”， cc会自己读取链接内容并安装

---

**作者** Ashpreet Bedi（@ashpreetbedi）  
**貼文連結** https://x.com/ashpreetbedi/status/2010131000886436037  

**正文**

We have an internal projects repo where we write design docs for each initiative. Template:

  - http://CLAUDE.md (instructions)
  - http://design.md (the spec)
  - http://implementation.md (status)
  - http://decisions.md (the why)
  - http://future-work.md (deferred)

This repo is symlinked into Agno but gitignored - invisible to git, visible to Claude.

This is how it started 👇
We have an internal projects repo where we write design docs for each initiative. Template:

  - http://CLAUDE.md (instructions)
  - http://design.md (the spec)
  - http://implementation.md (status)
  - http://decisions.md (the why)
  - http://future-work.md (deferred)

This repo is symlinked into Agno but gitignored - invisible to git, visible to Claude.

This is how it started 👇

---

**作者** vas（@vasuman）  
**貼文連結** https://x.com/vasuman/status/2010473638110363839  

**正文**

AI Agents are not magic, but also are not as simple as "build an agent, automate everything, profit". Most people don’t understand what an agent is. 

Those that do (<5%) try to build one and it falls apart. The agent hallucinates, forgets what it was doing mid-task, or calls the wrong tool at the wrong time. It works perfectly in demos and breaks immediately in production. 

I've deployed agents for over a year now. I started my software career at Meta but left 6 months ago to build a company that does nothing but deploy production agents for enterprise. We're at $3M ARR and growing, not because we're smarter than anyone else, but because we've built and failed enough times to know what the formula is now. 

This is everything I've learned about building agents that work. It should apply at any level, whether you’re a beginner, an expert, or somewhere in between.

My goal with this article is to share my biggest learnings from a few years of being in the AI space. My hope is that you walk away with useful information that you can use to build better agents. Let's begin. 

## Lesson 1: Context Is Everything

Yes this is super obvious and you’ve probably heard it before. But that's because it's true. Most people think building agents is about chaining tools together. You pick a model, give it access to your database, and let it figure out what to do while you grab a beer. This approach fails immediately for a few different reasons.

The agent doesn't know what matters. It doesn't know what happened five steps ago. It only sees the current step in the process, guesses what to do (often poorly), and hopes for the best. That’s not the way that you want your agents to act, especially when you sell these agents to companies.

Context is often the biggest difference between an agent worth $1M and an agent worth $0. Here's the concepts you need to focus on and optimize for:

What the agent remembers. Meaning not just the current task, but the history of what led here. If an agent is handling an invoice exception, for example, it needs to know: what triggered this exception, who submitted the original invoice, what policy applies, and what happened last time this vendor had an issue. Without that history, the agent is just guessing, which is worse than if the agent didn’t even exist in the first place, because at that point a human would have figured it out. See: "AI sucks". 

How information flows. When you have multiple agents, or one agent handling multiple steps, information needs to move between stages without getting lost, corrupted, or misconstrued. The agent that triages incoming requests needs to pass clean, structured context to the agent that resolves them. If that handoff is sloppy, everything downstream breaks. That means structured input and structured output that is verifiable at each stage. An example of this step is /compact in Claude Code, handing off context between LLM sessions. 

What the agent knows about the domain. An agent handling legal contract review needs to understand what clauses matter, what risks look like, what the company's actual policies are. You can't just point it at documents and expect it to figure out what's important. That’s your job. But your job also includes being able to provide the resources in a structured format to your agent so that it has domain knowledge.

Bad context management is an agent that calls the same tool repeatedly because it forgot it already got the answer, or calls the wrong tool because it was fed the wrong information. Another example is an agent that makes a decision contradictory to something it learned two steps earlier, or an agent that treats every task as brand new even when there's a clear pattern from previous similar tasks.

Good context management means the agent operates like someone with domain knowledge. It connects dots across different pieces of information without explicit instructions on how they relate. This is why when I sell agents to enterprise, I say we truly can automate everything. This is because we build custom for businesses, and we span their entire existing knowledge base (whether that's documents or interviewing their employees) to make that happen. 

This is the concept that separates agents that just demo well from agents that run and deliver results when in production.

## Lesson 2: Agents Multiply Outcomes

The wrong way to think about agents: "This will do the work so we don't have to hire someone."

The right way is: "This will let three people do what used to require fifteen." Yes, agents are going to replace human labor, and if you say otherwise then you are respectfully delusional. The positive is that agents don't eliminate the need for human judgment. They eliminate the friction around human judgment. This can include things like research, data gathering, cross-referencing, formatting, routing, follow-up. You get the idea.

A finance team still needs to make decisions about exceptions. But instead of spending 70% of close week hunting for missing documentation, they spend 70% of close week actually resolving issues. The agent did all of the work, but the human approves it. The reality of the situation, from what I’ve seen doing this for customers, is they never fire employees. There’s nearly infinite work for employees to do in place of their previous manual work, at least for now. I do anticipate this will change over time as AI replaces that too.

The companies getting real value from agents aren't the ones trying to remove humans from the loop. Instead they are the ones who realized that most of what humans were doing wasn't actually the valuable part of their job, but rather the overhead required to get to the valuable part.

Build agents this way and accuracy stops being a concern: the agent handles what it is good at, just like employees focus on what they’re good at.

This also means you can deploy faster. You don't need the agent to handle every edge case. You need it to handle the common cases well and route the weird stuff to humans with enough context that the human can resolve it quickly. Again, at least for now…

## Lesson 3: Memory and State

How an agent retains information across a task - and across multiple tasks - determines whether it works at scale.

3 patterns show up constantly:

1. Solo agents that handle a complete workflow. One agent handling one job, start to finish. These are the easiest to build because all the context stays in one place. The challenge is managing state as the workflow gets longer. The agent needs to remember what it decided at step three when it gets to step ten. If your context window fills up or you're not structuring memory correctly, late-stage decisions get made without early-stage context, and stuff breaks.
1. Parallel agents that work on different pieces of the same problem simultaneously. Faster, but now you have a coordination problem. How do the results merge? What happens when two agents reach contradictory conclusions? You need a clear protocol for how information comes back together and how conflicts resolve. Often time this means a judge (either a human or another LLM) that resolves conflicts or race conditions.
1. Collaborative agents that hand off to each other in sequence. Agent A does triage, passes to Agent B for research, passes to Agent C for resolution. This works well when the workflow has natural stages, but the handoffs are where things break. Whatever Agent A learns needs to survive the transition to Agent B in a format that Agent B can actually use.

Typically the agents that we deploy for enterprise are a mix of 2 and 3.

The mistake most people make is treating these like implementation schematics, when in reality they're architectural decisions that determine what your agent can and can't do.

If you're building an agent that handles sales deal approvals, you need to decide: Does one agent own the whole process? Or does a routing agent hand off to specialized agents for pricing review, legal review, and executive approval? Only you will know the actual process behind the decision making, which hopefully you can pass on to your fellow agent eventually. You can and should gather the information required to make a more informed decision by talking to the business or employees to figure out what their workflows actually look like, instead of just guessing.

The answer depends on how complex each stage is, how much context needs to carry between stages, and how often the stages need to coordinate in real-time versus sequentially.

If you get this wrong, you'll spend months debugging failures that aren't even bugs; they're architectural mismatches between your design, your problem, and your solution.

## Lesson 4: Catch Exceptions

The default instinct when building AI systems is to create dashboards. Surface information. Show people what's happening. Please for the love of every single person on this planet do not create another dashboard.

Dashboards are useless.

Your finance team already knows there are missing receipts. Your sales team already knows deals are stuck in legal.

Agents should catch problems when they happen and route them to whoever can fix them. With everything needed to actually fix them. Right then.

When an invoice hits without proper documentation, don't add it to a report. Flag it immediately. Figure out who needs to provide what. Route it to them with the full context - the vendor, the amount, the policy that applies, the specific documentation that's missing. Block the transaction from posting until it's resolved. This last part is also crucial, because if you don’t do this, information starts leaking all over the org and you won’t have time to restore the problem.

When a deal approval sits for more than 24 hours, don't surface it in a weekly review. Escalate automatically. Include the deal context so they can approve or reject without digging through systems. You have to move with urgency.

When a supplier misses a milestone, don't wait for someone to notice. Trigger the contingency playbook. Start the response before anyone has to manually realize there's a problem.

Your AI Agent’s job is to make problems impossible to ignore and incredibly easy to resolve. Surface the issue directly, rather than through a dashboard.

This is the opposite of how most companies use AI. They use it to create visibility into problems. You should use it to force resolution of problems, and do so quickly. Only spend time making a dashboard once the problem is mitigated to near 100%.

## Lesson 5: Economics of AI Agents vs. Generic SaaS

There's a reason companies keep buying SaaS tools that nobody uses (and it’s awfully painful to see).

SaaS is easy to purchase: It has a demo, a price, and a checkbox next to the requirement you were trying to fill. Someone can approve it and feel like progress happened (even though this is rarely the case).

The worst part purchasing AI SaaS is it just sits there. It doesn't integrate with how work actually happens, and becomes another system people have to log into. You're forced to migrate and after a month it's just another vendor to manage. Finally in 12 months it's abandoned and you're stuck with it because the switching cost is too high, resulting in what is called tech debt.

Bespoke AI Agents built on your existing infrastructure don't have this problem.

They operate inside the systems you already use. They don't create a new place to do work. In fact, they make existing work faster. The agent handles the task, while the human sees the result.

The real cost comparison isn't license fees versus development cost, it's a lot simpler.

SaaS accumulates “tech debt”. Every tool you buy is another integration to maintain, another system that will eventually go out of date, another vendor that might get acquired or pivot or shut down.

Agents built in-house accumulate capability. Every improvement makes the system smarter, and every new workflow extends what's possible. The investment compounds instead of depreciating. This is why I have been preaching for the last year: AI SaaS is going nowhere. And the industry is confirming this stat: most companies purchasing AI SaaS churn within 6 months, and see absolutely no productivity gains from implementing AI. The only companies who see AI gains are those who have custom agents built specifically for them, either in house or by a 3rd party agency.

This is why the companies that figure out agents early will have a structural advantage for years. They're building infrastructure that gets better over time. Everyone else is renting tools that will eventually need to be replaced. And when the space is changing every month, every week lost has serious implications for your roadmap and your business as a whole.

## Lesson 6: Deploy Time

If your AI agent project has a year-long timeline before anything goes live, you've already lost.

The plan won't survive contact with reality. The workflows you designed won't match how work actually happens, and the edge cases you didn't anticipate will be the ones that matter most. The entire AI space will look completely different in 12 months; you’re building a ghost.

Get to production in 3 months max. In a world where information is abundant, your real skill is understanding how to utilize it effectively and working with it, not against it. Actually work: handling real tasks, making real decisions, with real audit trails.

The biggest issue I’ve seen is that internal development teams will quote you 6-12 months for an AI project that should realistically take 3 months. Or worse, will tell you 3 months but after getting started keep pushing back the timeline for “unexpected reasons”. I can’t blame them - the AI world is hard.

Which is why you need genuinely AI-trained engineers, who understand how AI works at scale, have witnessed and accounted for real-world AI scenarios, and know the capabilities and limitations of AI. There are too many phony developers who think AI can do absolutely everything - this couldn't be further from the truth. If you’re a regular software engineer looking to get into the field of applied AI at the enterprise level, you have to be well versed in AI’s real capabilities.

## TLDR:

Building agents that work comes down to a few things:

Context is the whole game. An agent without good context is just an expensive random number generator. Invest in how information flows, how memory persists, how domain knowledge gets embedded. Remember when you guys made fun of prompt engineers? Context engineers are just prompt engineers 2.0. 

Design for multiplication, not replacement. Let humans do what humans are good at. Let agents clear the path so humans can focus on that.

Architecture matters more than model selection. Solo versus parallel versus collaborative agents is a bigger decision than which model you're using. Get the architecture right first.

Catch and resolve, don't report and review. Dashboards are where problems go to die. Build systems that force resolution.

Ship fast, improve constantly. The best agent is the one that's running in production and getting better, not the one that's still being designed (and watch your timeline)

Everything else is details.

If you're building agents - whether for yourself or for clients - these are the things that will determine whether you succeed or spend six months building something nobody uses.

The technology is ready, you’re probably not. Figure that out and you 100x your business. 

If you’re a business owner thinking about implementing AI for your business, just book a free AI Audit with my company Varick Agents, and we’ll explore whether or not AI is a good fit for you + what a potential AI transformation would look like: book today at [varickagents.com](<http://varickagents.com/>).

And if you want more tips on how to get the most out of AI for yourself or your business, subscribe to our free weekly newsletter: [varickagents.com/newsletter](<https://varickagents.com/newsletter>).

---

**作者** Emanuele Di Pietro（@emanueledpt）  
**貼文連結** https://x.com/emanueledpt/status/2010622780593541135  

**正文**

Europeans are shifting from Stripe to Polar

I already have all the code ready for Stripe that can be reused.

Is it worth switching to Polar just for tax handling? 

---

**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2010763566991941823  

**正文**

AI管理的link-in-bio

---

**作者** Christina Cacioppo（@christinacaci）  
**貼文連結** https://x.com/christinacaci/status/1896683813830557749  

**正文**

“What did we do last week at @TrustVanta?”

Dustin prototyped an MCP server that:
* Answers control & framework questions instantly
* Ensures audit evidence is solid
* Charts real-time progress
* Unlocks a whole new way to vibe through compliance (words I never thought I’d say!) 
“What did we do last week at @TrustVanta?”

Dustin prototyped an MCP server that:
* Answers control & framework questions instantly
* Ensures audit evidence is solid
* Charts real-time progress
* Unlocks a whole new way to vibe through compliance (words I never thought I’d say!) 
Vanta's MCP server is now in public beta: https://github.com/VantaInc/vanta-mcp-server

One use case:

* Fiona Founder asks @AnthropicAI  Claude "what's left in my SOC 2 audit prep?"
* Claude fetches progress via Vanta MCP server
* She drills into required controls, creates a @linear  ticket, and assigns it to an engineer
* The engineer sees the ticket in @cursor_ai, understands the issue, and applies a fix.
‍
The entire compliance loop that developers tackle—understanding, assigning, remediating, verifying—is handled across Claude, Linear, Cursor, and Vanta, all connected by MCP.

Excited to see other ways our MCP server will be used!

---

**作者** Jack Altman（@jaltma）  
**貼文連結** https://x.com/jaltma/status/1945503686660112879  

**正文**

To me, founder mode includes getting yourself genuinely excited about whatever the company needs next. 

Easy when it's product, harder when it's HR policy, but you figure it out.

---

**作者** Christina Cacioppo（@christinacaci）  
**貼文連結** https://x.com/christinacaci/status/1945872375389512044  

**正文**

@btaylor Episode transcript, links, etc.: https://www.vanta.com/resources/how-to-sell-enterprise-companies-as-an-ai-startup
Youtube: https://www.youtube.com/watch?v=frMPv0wCK_0&feature=youtu.be
Spotify: https://open.spotify.com/episode/4zgGwyCro8DPBqpFpTeHYR?si=6628b28d4fe84fd2
Apple Podcasts: https://podcasts.apple.com/gb/podcast/bret-taylor-of-sierra-how-to-sell-to-enterprise/id1815547797?i=1000717545444

---

**作者** elvis（@omarsar0）  
**貼文連結** https://x.com/omarsar0/status/2010359146927763804  

**正文**

Introducing ralph-research plugin.

I just adopted the ralph-loop for implementing papers. 

Mindblown how good this works already.

The entire plugin was one-shotted by Claude Code, but it can already code AI paper concepts and run experiments in a self-improving loop.

Wild! 
Introducing ralph-research plugin.

I just adopted the ralph-loop for implementing papers. 

Mindblown how good this works already.

The entire plugin was one-shotted by Claude Code, but it can already code AI paper concepts and run experiments in a self-improving loop.

Wild! 
Notes:

- It took about 40 minutes to implement the ReAct paper without any interruptions.
- It ran into some issues, but it figured out how to solve them along the way. This is what makes the ralph-loop extremely powerful. It can explore solutions and learn from its mistakes. I would argue that research is probably an even better use case for ralph as research requires lots of exploration. 
- I have tested on other newer papers, and it has done a good job, which gives me hope that this could be implemented to be more robust. 
- As you can see in the video, and as with anything LLM-powered, it will struggle to use newer models even if you give instructions and APIs. But this is something that can easily be fixed with clever prompting.
- This is not a perfect plugin, and it's mostly for internal testing purposes. I still have many things to improve on before I can release it, along with other plugins it depends on. 

I will share more details as I continue to work on these plugins. Follow along @omarsar0 

Let me know your thoughts and how this could be useful for you.
During my live cohort this week, I will share more on my process for quickly building tools like this in Claude Code: https://dair-ai.thinkific.com/courses/claude-code-for-everyone-2

It's an intensive training, but you only need to learn this stuff once and build from there.

There are a few seats left!

---

**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2010526940827140570  

**正文**

UI Skills：非常值得学习的性能优化与用户体验的工程化落地手册，作者 @Ibelick 👍🏻
https://www.ui-skills.com/

核心逻辑：通过约束开发者的自由度，来保证系统的一致性、可访问性和高性能。看到 5 个关键维度的约束，我要想想怎么沉淀成信息卡提示词 (btw... 下面的信息卡，就是借鉴了作者内容优化后的，有三分相似吗😄)

性能红线，这是绝对不可触碰的禁区：
1. 动画仅允许涉及 transform 和 opacity，也就是只利用合成层。严禁动画化 width、height 或 background-color 以免触发重绘，除非是极小的局部元素。
2. 严禁对大尺寸表面使用高斯模糊 backdrop-filter 或 will-change，这会直接导致移动端卡顿或掉帧。
3. 任何能用渲染逻辑表达的，绝不可使用 useEffect，以减少不必要的副作用。

视觉精度，利用高级 CSS 提升质感：
1. 标题强制使用 text-balance 来平衡行长，防止最后一行仅剩一个字；正文建议使用 text-pretty。
2. 所有数据展示必须强制使用 tabular-nums，防止数字变化时文字左右抖动。
3. 布局上，方形元素优先用 size-x 代替宽高分开写；移动端高度必须用 h-dvh 替代 h-screen，以解决浏览器地址栏遮挡底部内容的问题。

交互与可访问性，核心原则是不重复造轮子：
1. 严禁手写键盘或焦点逻辑，必须使用 Base UI、Radix 或 React Aria 等无障碍原语。
2. 破坏性操作（如删除）必须使用 AlertDialog；永远不要在输入框或文本域中禁止粘贴。
3. 错误信息必须显示在操作发生的旁边，而不是通过弹窗提示。

动画节奏，量化用户体验标准：
1. 所有的交互反馈动画时长不得超过 200 毫秒，确保系统的即时跟手感。
2. 入场动画强制使用 ease-out 缓动，符合物理直觉。
3. 屏幕外的循环动画必须暂停，且必须严格遵守系统的 prefers-reduced-motion 设置。

设计约束，强调克制的工程美学：
1. 严禁随意使用 z-index，必须基于固定的阶梯（如 Modal 定为 50）。
2. 默认情况下不使用渐变（尤其是紫色或多色渐变）、发光效果或自定义的缓动曲线。
3. 加载状态优先使用结构化的骨架屏。
4. 技术栈上，强制使用 cn 工具结合 clsx 和 tailwind-merge 来处理类名逻辑，样式优先使用 Tailwind 的默认值。

---

**作者** aditya（@adxtyahq）  
**貼文連結** https://x.com/adxtyahq/status/2010242491069673983  

**正文**

Vibe coding is fun until production shows up 
Vibe coding is fun until production shows up 
“it works on my machine”
famous last words

---

**作者** el.cine（@EHuanglu）  
**貼文連結** https://x.com/EHuanglu/status/2010413328548688381  

**正文**

oh my.. this guy connects Claude to Blender

you can do 3D modeling with prompts
 
oh my.. this guy connects Claude to Blender

you can do 3D modeling with prompts
 
download for free here: https://github.com/ahujasid/blender-mcp

---

**作者** agrim singh（@agrimsingh）  
**貼文連結** https://x.com/agrimsingh/status/2010412150918189210  

**正文**

everyone on my timeline is “ralph-pilled” right now.

but if you’ve ever let an ai coding session run for 40–60 minutes, you’ve felt this:
it starts repeating itself, undoing its own fixes, and confidently going in circles.

most explanations of ralph are either:

- terminal priestcraft, or
- “it’s just a loop lol” (true, but missing the point)

@GeoffreyHuntley coined and popularized the technique and wrote the [canonical post](<https://ghuntley.com/ralph/>). start there if you want the origin story and the philosophical framing.

this is the 5-minute, copy-paste, no-mysticism version.

## 1) ralph is not “an agent that remembers forever”

ralph is the opposite: it’s an agent that forgets on purpose.

in geoff’s purest description, ralph is literally a bash loop that keeps starting over with fresh context:

same task. new brain each iteration.

the “memory” is not the chat. it’s the filesystem + git.

if it’s not written to a file, it doesn’t exist.

## 2) the only insight that matters: context pollution

every ai coding session has a context window (working memory). stuff goes in:

- files it read
- commands it ran
- outputs it produced
- wrong turns it took
- half-baked plans it hallucinated at 2:13am

here’s the cursed part: you can keep adding, but you can’t delete.

failures accumulate like plaque. eventually you hit the familiar symptom cluster:

- repeating itself
- “fixing” the same bug in slightly different ways
- confidently undoing its own previous fix
- circular reasoning, but with commit rights

that’s context pollution. once you’re there, “try harder” doesn’t work.

adding more instructions doesn’t help. more tokens don’t help. more patience doesn’t help.

once the ball is in the gutter, adding spin doesn’t save it.

ralph doesn’t try to clean the memory. it throws it away and starts fresh.

## 3) if you rotate constantly, how do you make progress?

you externalize state.

the trick is simple:

progress persists. failures don’t.

context (bad for state) 

- dies with the convo
- persists forever
- polluted by dead ends

files + git (good for state) 

- only what you choose to write
- can’t be edited
- can be patched / rolled back“memory” can drift
- git doesn’t hallucinate

each fresh agent starts clean, then reconstructs reality from files.

## 4) the anchor file (source of truth)

every ralph setup needs a single source-of-truth file that survives rotations and tells a brand-new agent what reality currently looks like.

in my cursor implementation, that file is ralph\_task.md:

state lives in .ralph/:

what are the other files and their purpose in running ralph correctly?

- guardrails.md: learned constraints (“signs”)
- progress.md: what’s done / what’s next
- errors.log: what blew up
- activity.log: tool usage + token tracking

the loop reads these every iteration.

fresh context. persistent state.

the loop is not the technique. state hygiene is the technique.

format doesn’t matter. invariants do.

## 5) why the claude code plugin approach is accidentally anti-ralph

let me be explicit: the claude code plugin approach is accidentally anti-ralph.

it keeps pounding the model in a single session until context rots. the session grows until it falls apart. no visibility into context health. no deliberate rotation.

claude code treats context rot as an accident.
ralph treats it as a certainty.

ralph solves this by starting fresh sessions before pollution builds up. deliberate rotation, not accidental compaction.

the claude code plugin lets a single session grow until it inevitably rots, with no real visibility into when context has gone bad. ralph assumes pollution is coming and rotates deliberately before it happens. 
instead of repeating the same mistakes over and over, ralph records failures as guardrails so they don’t recur. 
and while claude code locks you into a single model, ralph-technique should be flexible enough for you to use the right model for the job as conditions change.

## 6) why i built a cursor port (model selection matters)

i built this because cursor lets you extend the agent loop like a real system (scripts, parsers, signals), and because model choice matters in practice.

different models fail in different ways. ralph lets you exploit that instead of being stuck with one failure mode.

cursor makes it trivial to swap models per iteration. different brains for different failure modes. this is deeply under-discussed compared to “one agent to rule them all.”

practical guidance:

- starting a new project → opus (architecture matters)
- stuck on something weird → codex

i’m getting better results on some workloads with gpt-codex models than opus 4.5. vibes? tokenization? inductive bias? the gods? idk. but it’s repeatable.

and yes, i’ve used this to port very large repos (tens of thousands of loc) to typescript without it faceplanting every 10 minutes. that’s the whole point: long-running implementation work where humans become the bottleneck.

## 7) the architecture (cursor version)

(if you don’t care about plumbing, you can skip this section. the only point is that vibes get turned into signals.)

key features:

- accurate, practical token tracking (a proxy, not tokenizer theology)
- gutter detection (same command fails repeatedly, file thrashing)
- real-time monitoring via logs
- interactive model selection

none of this is magic. it’s just turning “it’s losing it” into mechanics.

## 8) quick start (3 commands, no incense)

repo: [https://github.com/agrimsingh/ralph-wiggum-cursor](<https://github.com/agrimsingh/ralph-wiggum-cursor>)

1) install

this creates .cursor/ralph-scripts/ and initializes .ralph/.

2) write the anchor file

3) run ralph

optional: watch it like it’s a fish tank.

## 9) guardrails: how ralph stops repeating the same dumb mistake

ralph will do something stupid. the win condition is not “no mistakes.”

the win condition is the same mistake never happens twice.

when something breaks, the agent adds a sign to .ralph/guardrails.md:

guardrails are append-only. mistakes evaporate. lessons accumulate.

next iteration reads guardrails first. cheap. brutal. effective.

it’s basically kaizen, but for a golden retriever with a soldering iron.

## 10) “isn’t this just slop?”

saw this tweet earlier:

fair concern.

there are two modes of development:

1. exploration — figuring out what to build, experimenting, making architectural decisions
1. implementation — building the thing you’ve already designed

ralph is for #2.

if you’re exploring, use interactive mode. be deeply involved. make creative decisions.

but once you know what you’re building - a rest api with these endpoints, a cli with these commands, tests for these functions - that’s implementation. that’s ralph territory.

“but won’t it produce slop?”

only if you let it.

ralph has:

- checkboxes (explicit success criteria)
- tests (code must pass)
- types (errors get caught)
- guardrails (failures don’t repeat)
- git review (you still review everything)

ralph with proper feedback loops produces more consistent code than a tired developer at 2am.

“why wouldn’t i want to be involved?”

you ARE involved. your role just changes.

- you define what “done” means
- you add constraints when things go wrong
- you review outcomes, not keystrokes
- you decide when to intervene

think of it as steering, not rowing.

## 11) when NOT to use ralph

ralph is for implementation, not exploration.

use ralph when the specs are crisp, success is machine-verifiable (tests, types, lint), and the work is bulk execution like crud, migrations, refactors, or porting. it shines when you can clearly define “done” and express it as checkboxes, then let the loop grind through implementation without losing the plot.

don’t use ralph when you’re still deciding what to build, when taste and judgment matter more than correctness, or when you can’t cleanly define what “done” even means. if the real work is thinking, exploring, or making creative decisions, looping is the wrong tool - that’s interactive territory.

if you can’t write checkboxes, you’re not ready to loop. you’re ready to think.

## 12) the one-liner takeaway

ralph works because it treats ai like a volatile process, not a reliable collaborator.

your progress should persist. your failures should evaporate.

everything else - loops, scripts, signals - is just furniture around that idea.

---

**作者** Astasia Myers（@AstasiaMyers）  
**貼文連結** https://x.com/AstasiaMyers/status/2010411419314033028  

**正文**

Great piece! Somethings that came to mind: 

Do we need new infra that is AI agent trace-native to support this use case? This is similar to how Datadog became large around the concept of a "metric".

If observability becomes a collab and product analytics solution, what are the best views for non-AI engineers?
Great piece! Somethings that came to mind: 

Do we need new infra that is AI agent trace-native to support this use case? This is similar to how Datadog became large around the concept of a "metric".

If observability becomes a collab and product analytics solution, what are the best views for non-AI engineers?

---
