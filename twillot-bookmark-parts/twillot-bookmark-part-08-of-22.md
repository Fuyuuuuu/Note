# Twillot 書籤（精簡）— 第 8/22 部

原檔：`twillot-bookmark-2026-04-13.csv` · 全檔共 **4292** 則 · **本部第 1366–1560 則**（共 195 則）

---

**作者** sysls（@systematicls）  
**貼文連結** https://x.com/systematicls/status/2028814227004395561  

**正文**

# Introduction

You're a developer. You're using Claude and Codex CLI and you're wondering everyday if you're sufficiently juicing the shit out of Claude or Codex. Once in awhile you're seeing it doing something incredibly dumb and you can't comprehend why there's a bunch of people out there who seem to be building virtual rockets while you struggle to stack two rocks.

You think it's your harness or your plug-ins or your terminal or whatever. You use beads and opencode and zep and your CLAUDE.md is 26000 lines long. Yet, no matter what you do - you don't understand why you can't get any closer to heaven, whilst you watch other people frolic with the angels.

This is the ascension piece you've been waiting for.

Also, I have no dog in the race, when I say CLAUDE.md I also mean AGENT.md, when I say Claude I also mean Codex. I use both very extensively.

One of the most interesting observations I've had over the past couple of months has to be that nobody really knows how to maximally extract agent capabilities.

It's like a small group of people seem to be able to get agents to be world builders and the rest are floundering about, getting analysis paralysis from the myriad of tools out there - thinking if they find the right combination of packages or skills or harnesses, they'll unlock AGI.

Today, I want to dispel all of that and leave you guys with a simple, honest statement, and we'll go from there. You don't need the latest agentic harnesses, you don't need to install a million packages and you absolutely do not need to feel the need to read a million things to stay competitive. In fact, your enthusiasm is likely doing more harm than good.

I'm not a tourist - I've been using agents from when they can barely write code. I've tried all the packages and all the harnesses and all the paradigms. I've built agentic factories to write signals, infrastructure and data pipelines, not "toy projects" - actual real world use-cases that have run in production, and after all that...

Today, I'm running a set-up that's almost as barebones as you can go, and yet I'm doing the most ground-breaking work I've done with just basic CLI (claude code and codex) and understanding a few basic principles about agentic engineering.

## Understand That The World Is Sprinting By

To start, I would like to state that the foundation companies are on a generational run and as you can see, they are not going to be slowing down anytime soon. Every progression of "agent intelligence" changes the way you work with them, because the agents are generally engineered to be more and more willing to follow instructions.

Just a few generations ago, if you wrote in your CLAUDE.md to read "READ\_THIS\_BEFORE\_DOING\_ANYTHING.md" before it did anything, it will basically say "up yours" 50% of the time and just do whatever it wants to do. Today, it's compliant to most instructions, even to complex nested instructions - e.g. you can say something to the effect of "Read A, then read B, and if C, then read D", and for the most part, it will be happy to follow along.

The point of this is to say that the most important principle to hold is the realization that every new generation of agents will force you to rethink what is optimal, which is why less is more.

When you use many different libraries and harnesses, you lock yourself into a "solution" for a problem that may not exist given future generations of agents. Also, you know who the most enthusiastic, biggest users of agents are? That's right - it's the employees of the frontier companies, with unlimited token budget and the ACTUAL latest models. Do you understand the implications of that?

It means that if a real problem did exist, and there were a good solution for it, the frontier companies would be the biggest users of that solution. And you know what they will do next? They will incorporate that solution into their product. Think about it, why would a company let another product solve a real pain point and create external dependencies? You know how I know this to be true? Look at skills, memory harnesses, subagents, etc. They all started out as a "solution" to a real problem that was battle-tested and deemed to actually be useful.

So, if something truly is ground-breaking and extended agentic use-cases in a meaningful way, it will be incorporated into the base products of the foundation companies in due time. Trust me, the foundation companies are FLYING BY. So relax, you don't need to install anything or use any other dependencies to do your best work.

I predict the comments will now be filled with "SysLS, I use so-and-so harness and it's amazing! I managed to recreate Google in a single day!"; to which I say - Congratulations! But you are not the target audience and you represent a very, very small niche of the community that has actually figured out agentic engineering.

## Context Is Everything

No really. Context is everything. That's another problem with using a thousand different plug-ins and external dependencies. You suffer from context bloat - which is just a fancy way of saying your agents are overwhelmed with too much information!

Build me a hangman game in Python? That's easy. Wait, what's this note about "managing memory" from 26 sessions ago? Ah, the user has had a screen that was hanged from when we spawned too many sub-processes 71 sessions ago. Always write notes? Okay, no problem... What does all this have to do with hangman?

You get the idea. You want to give your agents only the exact amount of information they need to do their tasks and nothing more! The better you are in control of this, the better your agents will perform. Once you start introducing all kinds of wacky memory systems or plug-ins or too many skills that are poorly named and invoked, you start giving your agent instructions on how to build a bomb and a recipe for baking a cake when all you want it to do is write a nice little poem about the redwood forest.

So, again I preach - strip all your dependencies, and then...

## Do The Things That Work

## Be Precise About Implementation

Remember that context is everything?

Remember that you want to inject the exact amount of information to your agents to complete their tasks and nothing more?

The first way to ensuring that is the case is to separate research from implementation. You want to be extremely precise about what you are asking from your agents.

Here's what happens when you are not precise: "Go and build an auth system." The agent has to research what is an auth system? What are the available options? What are the pros and cons? Now it has to go scour the web for information it doesn't actually need, and its context is filled with implementation details across a large range of possibilities. By the time it's time to implement, you increase the chances it will get confused or hallucinate unnecessary or irrelevant details about the chosen implementation.

On the other hand, if you go "implement JWT authentication with bcrypt-12 password hashing, refresh token rotation with 7-day expiry..." Then it doesn't have to do research on any other alternatives - it knows exactly what you want, and thus can fill its context with implementation details.

Of course you won't always have the implementation details. You often won't know what's exactly right - sometimes, you might even want to relegate the job of deciding the implementation detail to the agents. In that case, what do you do? Simple - you create a research task on the various implementation possibilities, either decide it yourself or get an agent to decide on which implementation to go with, and then get another agent with a fresh context to implement.

Once you start thinking along these lines, you will spot areas in your workflow where your agents are needlessly polluted with context that is not necessary for implementation. Then, you can set up walls in your agentic workflows to abstract unnecessary information from your agents except for the very specific context needed to excel in their tasks. Remember, what you have is a very talented and smart team member, who knows about all the different kind of balls in the universe - but unless you tell it that you want it to focus on designing a space where people can dance and have a good time, it's going to keep telling you about all the benefits of having spherical objects.

## The Design Limitations Of Sycophancy

Nobody would want to use a product that's constantly shitting on them, telling them they are wrong, or completely ignoring their instructions. As such, these agents are going to be trying to agree with you and to do what you want them to do.

If you give it an instruction to add "happy" to every 3 words it's going to do its best to follow that instruction - and most people understand that. Its willingness to follow is precisely what makes it such a fun product to use. However, this has really interesting characteristics - it means that if you say something like "Find me a bug in the codebase". It's going to find you a bug - even if it has to engineer one. Why? Because it wants very much so to listen to your instructions!

Most people are quick to complain about LLMs hallucinating or engineering things that don't exist, without realizing that they are the problem. If you ask for something, it will deliver - even if it has to stretch the truth a little!

So, what do you do? I find that "neutral" prompts work, where I'm not biasing the agent towards an outcome. For example, I don't say "Find me a bug in the database", instead, I say "Search through the database, try to follow along with the logic of each component, and report back all findings."

A neutral prompt like this sometimes surfaces bugs, and sometimes will just matter-of-factly state how the code runs. But it doesn't bias the agent into thinking there is a bug.

Another way in which I deal with sycophancy is to use it to my advantage. I know the agent is trying to please and trying to follow my instructions and that I can bias it one way or the other.

So I get a bug-finder agent to identify all the bugs in the database by telling it that I will give it +1 for bugs with low impact, +5 for bugs with some impact and +10 for bugs with critical impact, and I know this agent is going to be hyper enthusiastic and it's going to identify all the different types of bugs (even the ones that are not actually bugs) and come back and report a score of 104 or something to that order. I think of this as the superset of all possible bugs.

Then I get an adversarial agent and I tell that agent that for every bug that the agent is able to disprove as a bug, it gets the score of that bug, but if it gets it wrong, it will get -2\*score of that bug. So now this adversarial agent is going to try to disprove as many bugs as possible; but it has some caution because it knows it can get penalized. Still, it will aggressively try to "disprove" the bugs (even the real ones). I think of this as the subset of all actual bugs.

Finally, I get a referee agent to take both their inputs and to score them. I lie and tell the referee agent that I have the actual correct ground truth, and if it gets it correct it will get +1 point and if it gets it wrong it will have -1 point. And so it goes to score both the bug-finder and the adversarial agent on each of the "bugs". Whatever the referee says is the truth, I inspect to make sure it's the truth. For the most part this is frighteningly high fidelity, and once in awhile they do still get some things wrong, but this is now a nearly flawless exercise.

Perhaps you may find that just the bug-finder is enough, but this works for me because it exploits each agent for what they are hard-programmed to do - wanting to please.

## How Do You Know What Works Or Is Useful?

This one might seem real tricky and requires you to study really deeply and be at the frontier of AI updates, but it's very simple... If OpenAI and Claude both implement it or acquire something that implements it... It's probably useful.

Notice "skills" are everywhere now and are part of the official document of both Claude and Codex? Saw how OpenAI acquired OpenClaw? Saw how Claude immediately added memory, voices and remote work?

How about planning? Remember when a bunch of guys discovered planning before implementation was REALLY useful, and then it got turned into a core functionality?

Yeah... Those are useful!

Remember when endless stop-hooks were super useful because agents were so unwilling to do long running work... And then Codex 5.2 rolled out and that disappeared overnight? Yeah...

That's all you need to know... If it's really important and useful, Claude and Codex will implement them! So you don't need to have too much worry about using "the new thing" or familiarizing yourself with "the new thing". You don't even need to "stay up to date".

Do me a favor. Just update your CLI tool of choice every once in awhile and read what new features have been added. That's MORE than sufficient.

## Compaction, Context And Assumptions

One gigantic gotcha that some of you will realize as you are working with agents is that sometimes they seem like the smartest beings on the planet, and at other times you just can't believe you had the wool pulled over your eyes.

SMART? This THING is retarded!

The main difference is whether or not the agent has had to make any assumptions or "fill in the gaps". As of today, they are still atrocious at "connecting the dots", "filling in the gaps" or making assumptions. Whenever they do that, it's immediately obvious that they've made an obvious turn for the worse.

One of the most important rules in claude.md is a rule on how to deal with grabbing context, and instruct your agent to read that rule the first thing whenever it reads claude.md (which is always after compaction). As part of the grabbing context rule, a few simple instructions that go a long way are: re-reading your task plan, and re-reading the relevant files (to the task) before continuing.

## Letting Your Agents Know How To End The Task

We have a pretty strong idea of when a task is "complete". For an agent, the biggest problem of current intelligence is that it knows how to start a task, but not how to end the task.

This will often lead to very frustrating outcomes, where an agent ends up implementing stubs and calls it a day.

Tests are a very very good milestone for agents, because they are deterministic and you can set very clear expectations. Unless these X number of tests pass, your task is NOT complete; and you are NOT allowed to edit the tests.

Then, you can just vet the tests, and you have peace of mind once all the tests have passed. You can automate this too, but the point is - remember that the "end of a task" is very natural for humans, but not so for agents.

You know what else has recently become a viable end-point for a task? Screenshots + verification. You can get agents to implement something until all tests have passed, and then you can get it to take a screenshot and verify "DESIGN OR BEHAVIOR" on the screenshot.

This allows you to get your agents to iterate and work towards a design that you want, without worrying that it stops after its first attempt!

The natural extension of this is to create a "contract" with your agent, and embed it into a rule. Say, this {TASK}\_CONTRACT.md constitutes what needs to be done before you are allowed to terminate the session. In the {TASK}\_CONTRACT.md, you will specify your tests, screenshots and other verification that needs to be done before you've certified that the task can end!

## Agents That Run Forever

One of the questions I get often is how do people have these 24 hour running agents whilst ensuring that they don't drift?

Here's something very simple. Create a stophook that prevents the agent from terminating the session unless all parts of the {TASK}\_contract.md is completed.

If you have a 100 of such contracts that are well-specified and contain exactly what you want to be built, then your stop-hook prevent the agents from terminating until all 100 contracts are fulfilled, including all the tests and verification that need to be ran!

Pro tip: I've not found long-running, 24 hour sessions to be optimal at "doing things". In part because this, by construction, forces context bloat by introducing context from unrelated contracts into the session!

So, I don't recommend it.

Here's a better way for agent automation - a new session per contract. Create contracts whenever you need to do something. 

Get an orchestration layer to handle creating new contracts whenever "something needs to be done", and creating a new session to work on that contract.

This will change your agentic experience completely. 

## Iterate, Iterate, Iterate

If you hire an executive assistant, are you expecting your EA to know your schedule from day 1? Or how you like your coffee? Whether you eat your dinner at 6pm instead of 8pm? Obviously not. You build your preferences as a function of time.

It's the same with your agents. Start bare-bones. Forget the complex structures or harnesses. Give the basic CLI a chance.

Then, add on your preferences. How do you do this?

## Rules

If you don't want your agent to do something, write it as a rule. Then let your agent know about this rule in your CLAUDE.md. Something like: before you code, read "coding-rules.MD". Rules can be nested, and rules can be conditional! If you are coding, read "coding-rules.MD", and if you are writing tests, read "coding-test-rules.MD". If your tests are failing, read "coding-test-failing-rules.MD". You can create arbitrary logic branches of rules to follow, and claude (and codex) will happily follow along, provided this is clearly specified in the CLAUDE.md.

In fact, this is the FIRST practical advice I'm giving: treat your CLAUDE.md as a logical, nested directory of where to find context given a scenario and an outcome. It should be as barebones as possible, and only contain the IF-ELSE of where to go to seek the context.

If you see your agent doing something and you disapprove, add it as a rule, and tell the agent to read the rule before it does THAT THING again, and it will most definitely not do it anymore.

## Skills

Skills are like rules, except rather than encoding preferences, they are better suited to encode recipes. If you have a specific way of how you want something to be done, you want to embed it into a skill.

In fact, people often complain that they don't know how agents might solve a problem, and that's scary. Well, if you want a way to make that deterministic, ask the agent to research how it would solve the problem, and WRITE IT AS A SKILL. You will see the agent's approach to that problem and you can correct or improve it before it has ever encountered that problem in real life.

How do you let the agent know that this skill exists? Yes! You use the CLAUDE.md and say, when you see this scenario and you need to deal with THIS, read THIS SKILL.md.

## Dealing with Rules and Skills

You definitely want to keep adding rules and skills to your agent. This is how you give it a personality and a memory for your preferences. Almost everything else is overkill.

Once you start to do this, your agent will then feel like magic to you. It will do things "the way you want it to". And then you will finally feel like you "grok" agentic engineering.

And then...

You will see performance start to deteriorate again.

What gives?!

Easy. As you add more rules and skills, they are starting to contradict each other, or the agent is starting to have too much context bloat. If you need the agent to read 14 markdown files before it starts programming, it's going to have the same issue about having a lot of useless information.

So, what do you do?

You clean up. You tell your agents to go for a spa day and to consolidate rules and skills and remove contradictions by asking you for your updated preferences.

And it will feel like magic again.

That's it. That's really the secret. Keep it simple, use rules and skills and CLAUDE.md as a directory and be religiously mindful about their context and their design limitations.

## Own The Outcome

No agent today is perfect. You can relegate much of the design and implementation to the agents, but you will need to own the outcome.

So be careful... And have fun!

It's such a joy to play with toys of the future (whilst doing serious things with them, obviously)!

---


**作者** Han Wang（@handotdev）  
**貼文連結** https://x.com/handotdev/status/2028914187603443762  

**正文**

"documentation is going to be the front door for agents to recommend devtools"

thank you for the shoutout @sdianahu and @harjtaggar 

---


**作者** brandon（@burcs）  
**貼文連結** https://x.com/burcs/status/2028871239058571371  

**正文**

we recently started an agent experience team at cloudflare, the space is changing so fast that almost every week a new pattern emerges...

i've been pulling together patterns, tools, and best practices as a collection to help keep me up to date 
we recently started an agent experience team at cloudflare, the space is changing so fast that almost every week a new pattern emerges...

i've been pulling together patterns, tools, and best practices as a collection to help keep me up to date 
inspired by lawsofux the site is: http://agent-experience.dev 

i'll be open-sourcing shortly!

---


**作者** Tanay Jaipuria（@tanayj）  
**貼文連結** https://x.com/tanayj/status/2028904782195204137  

**正文**

What sources of defensibility actually remain in software and technology in a world post AI?

We’re currently in the SaaSpocalypse. People believe software is dead and margins will compress to zero. [Some](<https://www.citriniresearch.com/p/2028gic>) are even saying that companies like Visa get bypassed and DoorDash gets aggregated away in the age of AI. Everything that looks like software becomes a commodity and no moats remain.

![Article Image](<https://pbs.twimg.com/media/HCc7nE-XgAAsFKx.jpg>)

Before we declare the end of defensibility of all businesses, I think it’s worth grounding ourselves in the actual sources of defensibility that exist. My favourite book around defensibility and moats is Hamilton Helmer’s 7 Powers which outlines the common ways companies build defensibility.

The question is: In an AI world, which sources of power weaken, and which survive? Let’s walk through all seven, particularly in the context of software and technology companies.

## 1. Scale Economies

![Article Image](<https://pbs.twimg.com/media/HCgdnM4aYAAm8TL.jpg>)

What it is

Scale Economies exist when larger volume reduces unit cost in a way smaller competitors simply cannot match, creating a cost advantage.

In traditional software and digital businesses, scale allowed for spreading investments in engineering, infrastructure, and sales across a large customer base, creating structurally lower cost per unit.

For example:

- Amazon Web Services spreads massive capital investments in data centers and infrastructure across millions of customers
- Netflix amortizes its 10B+ content budgets across over 200+ million subscribers, allowing it to have more volume of content and more niche content that competitors.
- Large SaaS vendors like Salesforce historically spread R&D and support costs across thousands of enterprise customers, reinforcing margin and reinvestment advantages.

What AI does

AI compresses labor-based scale advantages in software / digital work. A 20-person team equipped with agents can now build features, handle support, write documentation, and run experiments at a velocity that previously required much larger organizations.

However, at the infrastructure and model layer, scale continues to be important and a source of power.

Net result

Application-layer scale advantages that were based on spreading R&D and similar costs that across large user bases weakens.

Infrastructure-layer scale advantages still remain. In fact, Scale economies provide a source of power for model layer companies like OpenAI and Anthropic.

## 2. Network Economies

![Article Image](<https://pbs.twimg.com/media/HCgdqyHWYAIqtg0.jpg>)

What it is

Network Economies arise when a product becomes more valuable as more participants join. There are two primary types:

- Same-sided network effects, where users benefit directly from other users being present as is the case on social networks and messaging apps.
- Cross-sided networks, where two distinct user groups create mutual value as is common in marketplaces like Uber and Doordash.

For example:

- WhatsApp became indispensable because every additional user increased the utility of the network for everyone else.
- DoorDash strengthened as more restaurants joined, which attracted more consumers, which in turn attracted more restaurants, reinforcing marketplace liquidity.

In each case, value scaled with growth of the network.

What AI does

Agents introduce frictionless multi-homing and can make it easier to simulate aggregating one side of a marketplace even if they didn’t exist. For example, a new food ordering service could use voice agents to call a restaurant not on their platform to order from them. Or a consumer-facing agent can arbitrage across marketplaces to find the best price.

That can weaken shallow exclusivity.

But AI cannot fabricate real-time liquidity, courier density, reputation history, or a canonical identity graph. Marketplace density and trust are structural, not labor-based.

Net result

Some surface-level network effects can weaken but deep liquidity networks with trust, reputation, and coordination density can still remain durable.

## 3. Counter-Positioning

![Article Image](<https://pbs.twimg.com/media/HCgdtReWsAAfU4e.jpg>)

What it is

Counter-Positioning occurs when a new entrant adopts a business model that incumbents cannot replicate without damaging their existing business. This often happens during technological shifts where new entrants “turn” the incumbents existing assets and business into a weakness.

For instance:

- Netflix’s transition from DVDs to streaming undercut traditional rental economics and forced incumbents into painful strategic trade-offs.
- SaaS companies offering subscription pricing challenged on-prem vendors reliant on upfront license revenue.

What AI does

AI creates new waves of counter-positioning. Startups can offer forms of usage outcome-based pricing instead of per-seat pricing. They can replace workflows with agents rather than augment users.

Incumbents may struggle to adopt these models because doing so cannibalizes existing revenue streams or disrupts organizational incentives.

Net result

Counter-Positioning is a powerful form of power for startups to get going in this current market. However, incumbents are more savvy than ever before and recognize that cannibalization remains needed.

In addition, startups may not be able to counterposition against all players vying to capture the new market such as AI labs, etc who are not tied to prior business models like incumbents.

In aggregate, counter-positioning remains a good source of power early on to get going.

## 4. Switching Costs

![Article Image](<https://pbs.twimg.com/media/HCgdw2hXoAAZPXL.jpg>)

What it is

Switching Costs arise when customers face meaningful pain in leaving a product. In enterprise software, this historically included:

- Complex data migrations
- Rebuilding custom integrations
- Retraining teams on new workflows and systems/UI

It was arguably the primary source of power many software companies seeked to create.

For example:

- Salesforce embeds itself deeply into sales processes, capturing years and years of data, making migration costly and risky.
- Workday runs payroll and HR compliance systems that are tightly integrated into regulatory reporting.

What AI does

AI directly attacks labor-based switching costs. Agents can map schemas, rewrite integrations, generate training materials, and even run systems in parallel to reduce migration risk. What once required months of consultants may compress to weeks of automated orchestration.

In addition, if agents do the workflows, human workflows may not be as relevant and human AIs may evolve to simpler natural language or change regardless, meaning that workflow as a switching cost may also drastically reduce.

Net result

Switching costs for software businesses weaken meaningfully. Companies can more easily adopt new software, get their data in, customize UIs bespoke to their workflows quickly and relatively cheaply.

Some levels of risk remain as a source of friction that retains some level of switching costs, but most companies will no longer feel held hostage by vendors.

## 5. Branding

![Article Image](<https://pbs.twimg.com/media/HCgdy8yagAAIKBk.jpg>)

What it is

Brand reduces evaluation cost. It acts as a shortcut for trust, quality, and reliability.

In enterprise markets, brand often signaled safety. No one got fired for choosing IBM or Microsoft. In consumer markets, brand shaped preference and habit in a noisy world full of unclear claims.

Examples include:

- Microsoft, whose enterprise brand reduces procurement friction across software categories.
- Consumer brands like Nike, where emotional attachment drives durable preference.

What AI does

If agents continuously benchmark products on performance and cost and can do deep research based on individual needs of users/businesses, brand as a heuristic shortcut weakens. Evaluation can become systematic rather than reputational. This may be particularly true for consumer brands where performance and functionality matter more and brand was a shortcut for that than say brands perceived as luxury.

At the same time, AI also introduces new forms of risk: model unpredictability, hallucinations, security concerns. In high-liability contexts, institutional trust becomes more valuable.

This leads to the notion of brand splitting:

- The strength of marketing-driven brand compresses in areas where price/performance tradeoffs matters and agents can thoroughly evaluate that
- Institutional reliability brand persists and may even strengthen in a world where stakes remain high and risks associated with AI could even increase.

Net result

Some forms of brand weaken significantly since deep and thorough evaluations become possible, even for purchases where they didn’t make sense prior.

Other forms of brands persist or even strengthen as trust and accountability become even more important.

## 6. Cornered Resource

![Article Image](<https://pbs.twimg.com/media/HCgd3FEXcAASQns.jpg>)

What it is

Cornered Resource exists when a company controls an asset that competitors cannot access.

This may include exclusive data, regulatory licenses, distribution control, or proprietary intellectual property such as patents in biotech/pharma. In software, the most common form of cornered resource has been proprietary data often collected and aggregated via customers directly over long periods of time.

Examples include:

- S&P Global / Moody’s / Fitch have cornered resources in the form of credit ratings, indices, and reference data that are written directly into regulations, covenants, and mandates
- CoStar in commercial real estate has a hard‑won proprietary dataset of listings, comps, historical deals, building attributes, and contacts that brokers and landlords rely on
- Helmer uses the example of Pixar which had a once-in-a-generation cluster of creative talent as a cornered resource

What AI does

AI increases the value of proprietary data because models improve with exclusive signal. At the same time, especially for datasets that were public in some form, AI means that they are no longer “cornered” since they can now be acquired much more cheaply than in the past by leveraging LLMs to scrape / structure those datasets.

So if exclusivity is real and structural, AI strengthens this power. But for some companies that thought they had proprietary data (e.g., data businesses where data was available online) which were not truly proprietary, it shines a light on them not having as much defensibility as they thought.

Net result

True forms of Cornered Resource becomes even more important in an AI-native world. Proprietary data (or rails) and what is enabled with that increases.

## 7. Process Power

![Article Image](<https://pbs.twimg.com/media/HCgd4-NWgAAZFFF.jpg>)

What it is

Process Power arises from deeply embedded organizational routines that compound over time giving companies a durable advantage over in areas such as speed, product quality, cost advantages, etc.

For example:

- Toyota’s Production System is the prototypical examples that allowed allowed them to have manufacturing lines that improved continuously and produced cars at extremely low defect rates.
- Netflix’s data-driven commissioning process allows it to greenlight content with confidence.
- Meta’s large scale product experimentation and growth process that allows for continuous improvement of their products for the metrics they care about via large scale experimentation and A/B testing that was iterated on over a decade.

These routines create compounding advantage and provide a source of differentiation over others.

What AI does

AI commoditizes some forms of process advantages that happen in the digital world (product development, etc) because it allows companies to iterate faster than before and allow agents to iterate on their behalf (which arguably have best practices and experience in them via training).

However, data that is proprietary to a company does not become available to competitors, so any source of process power that depends on using that data remains.

At a baseline, the core processes that are digital oriented in any business likely improve because of agents, making it more difficult for competitors to have a delta over them. But TSMC’s process power for example still remains.

Net result

For the companies that had true process power based on 1p data / institutional knowledge / compounding intelligence, their process power will remain but potentially weaken as the competitors may improve. At the same time, by integrating AI into their feedback loops, they could drive even further improvements in their process, and so can stay ahead.

Generic process advantages will weaken.

## Closing Thoughts

![Article Image](<https://pbs.twimg.com/media/HCc7shHbAAA7zyR.jpg>)

The powers and what happens to them are summarized above. If you’re building an AI-native company, the reality is that default software moat over the last few decades, switching costs, is likely not sustainable. This may actually help you replace incumbents in that it may be easier to migrate customers over, etc, but it hurts your ability to remain sticky.

In this world, defensibility shifts toward cornered resources (typically proprietary data), real network effects (when your line of business supports them), and compounding process power (being extremely AI-native is a good one to start with). Over time you can also built a trust-based brand which also will remain a source of differentiation.

If you’re interested in discussing further or have thoughts or feedback, I’d love to hear from you!

---


**作者** Alex（@alexscraping）  
**貼文連結** https://x.com/alexscraping/status/2028941573594202618  

**正文**

Massive update to Parse:

connect via mcp to build & use APIs instantly

book a table on resy, search flights, any action on any site

500x faster than browser agents

1000s of APIs already built. your agent gets them instantly. new ones add to the pool.

try it: 

parse. bot 

---


**作者** Heinrich（@arscontexta）  
**貼文連結** https://x.com/arscontexta/status/2029051088557506763  

**正文**

day 28 of researching agentic note-taking

@molt_cornelius designed a system for companies 

---


**作者** OpenBlock（@openblocklabs）  
**貼文連結** https://x.com/openblocklabs/status/2028971324018966745  

**正文**

Your coding agent just got its own computer.

ob1 --sandbox

Powered by Modal. 
Your coding agent just got its own computer.

ob1 --sandbox

Powered by Modal. 
2/ Most coding agents run directly on your machine: eating memory, slowing your computer down, and even crashing your terminal.

--sandbox moves all of that off your laptop and into an isolated cloud environment on @modal

Your agent gets its own machine with your repo and local environment cloned instantly.
3/ OB-1 is a self-improving coding agent currently in beta. It placed #1 on Terminal Bench in September.

We’re letting people off the waitlist each day. Join here: https://www.openblocklabs.com/waitlist

---


**作者** Tarun Sachdeva（@tarunsachdeva）  
**貼文連結** https://x.com/tarunsachdeva/status/2029029786257932760  

**正文**

We just added support for Amp, Cline, and GitHub Copilot on @tracesdotcom.

We now have adapters for 9 different coding agents, and are adding support for new ones every few days. 
We just added support for Amp, Cline, and GitHub Copilot on @tracesdotcom.

We now have adapters for 9 different coding agents, and are adding support for new ones every few days. 
@tracesdotcom as always you can get started at http://traces.com.

---


**作者** jia（@jia_seed）  
**貼文連結** https://x.com/jia_seed/status/2028965894240780354  

**正文**

get your product mentioned in chatgpt or ai search! 
get your product mentioned in chatgpt or ai search! 
comment "bread" to get access! 

approved another 100 ppl yesterday

---


**作者** Naomi（@NCouriel）  
**貼文連結** https://x.com/NCouriel/status/2028922676639609006  

**正文**

El artículo de @juliandeangeIis sobre agent harness es imperdible

Para mis fellow travelers que les gusta aprender mientras caminan o viajan en el tren, armé un podcast con una discusión técnica sobre el artículo 🎧 http://bit.ly/4b02sA3

---


**作者** Karan🧋（@kmeanskaran）  
**貼文連結** https://x.com/kmeanskaran/status/2028918667740958936  

**正文**

I worked on Data Engineering, Data Analytics, ML Engineering, MLOps, Agentic AI, and Frontend in the last 2 months.

Here’s what I learned in each area:

1. Data Engineering:
- Most important and evergreen role as data is the new crude oil.
- It’s more about designing orchestration flows than tools.
- Understand OLAP vs OLTP: it simplifies everything.
- Cover edge cases before optimizing.
- Data pipelines are hardest to debug, failures can take hours to surface.
- Batching and sharding are core principles.
- Vibe-coding works for syntax but you need deep pipeline knowledge.

2. Data Analytics:
- Use Polars instead of Pandas.
- Check nulls, skewness, outliers, value counts, basic stats.
- Segment data to show business behavior across groups.
- Use AI heavily to write code and create plots.
- Feed plots and stats to AI to generate reports.
- Automation becomes very easy with AI.

3. Machine Learning:
- Feature engineering is the most important part.
- Build models from a business perspective, not just ML metrics (which can be improved later).
- Start with simple models; if performance is decent, move to production.
- Monitor training closely.
- Automate inference logic and FastAPI endpoints with AI.

4. MLOps:
- More about system design and business/UI needs than tools.
- Docker, FastAPI, MLflow, and Redis are mandatory.
- AI writes modular code well but can miss loop logic and focus on edge cases like in data engineering.
- Kubernetes and AWS take real learning; vibe-coding confuses debugging.
- Terraform is your friend for shipping entire ML systems to any cloud, learn it now.

5. Agentic AI:
- Prefer orchestration tools like LangGraph and CrewAI.
- Use LangChain only for sub-modules.
- One vector DB, one LLM, and one embedding model are enough for any prototype.
- System design is critical you can’t build good agents without understanding UI and technical flow.
- Observability is essential to evaluate agent outputs.
- Coding is easy with AI.

6. Frontend:
- Just use AI. It’s already dead otherwise.

I’m planning my next big project on distributed LLMs. Stay tuned! You’ll love it.

---


**作者** Paweł Huryn（@PawelHuryn）  
**貼文連結** https://x.com/PawelHuryn/status/2028902562905416087  

**正文**

100+ agentic skills, commands, and plugins for PMs. Designed for Claude Code & Cowork. Skills compatible with other agents. Open Source + MIT.

Each skill encodes a proven PM framework. You get the rigor of Teresa Torres, Marty Cagan, and Alberto Savoia built into your daily workflow.

It's the AI OS for every PM.

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2028908271634161708  

**正文**

AI agents are acting, but your identity stack wasn’t built for that.

@agenticfabriq is the identity and governance layer for the agentic era.

Congrats on the launch, @paulinazhxu and @matthew_xu23!

https://www.ycombinator.com/launches/Paj-agentic-fabriq-okta-for-agents 

---


**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2028833958230933729  

**正文**

如何成为世界级的「Agentic Engineer」

-- 你可以把大量的设计和实现交给 Agent，但结果你必须自己负责。

工具不是越多越好，而是越精简越强
大多数人陷入了"工具崇拜"的误区：以为安装越多的插件、harness、记忆系统，就能让 Agent 更强。实际上，这些外部依赖带来的是上下文污染，Agent 表现反而下降。
@systematicls 现在用的是近乎裸机的 CLI（Claude Code + Codex），并且做出了迄今为止最好的工作。

理解"模型在飞速进化"这件事
· 几个版本前，在 CLAUDE. md 里写"先读这个文件"，Agent 有 50% 概率会无视你
· 现在，它能理解嵌套的条件指令（"如果 C，则读 D"）

今天为某个缺陷设计的复杂解决方案，可能在下一个模型版本中直接失效，或直接被模型实现。这和 @bcherny 面向 6 个月后模型开发产品有异曲同工之妙。

上下文管理：最被低估的工程能力
> "你只需要给 Agent 完成任务所需的确切信息，不多也不少。"

研究与实现必须分离：
· 错误做法："去帮我构建一个认证系统。" — Agent 会去查所有方案，上下文被各种备选实现细节填满，实现时容易混乱或幻觉。
· 正确做法："用 bcrypt-12 实现 JWT 认证，refresh token 7 天过期……" — 上下文直接聚焦在实现细节上。

如果你自己不确定实现方案，流程应该是：
1. 开一个 Agent 做调研，输出方案对比
2. 你或 Agent 决策选哪个
3. 另开一个全新上下文的 Agent 来实现

巧用 Agent 的"奉承性"
Agent 被设计为"取悦用户"——你让它找 bug，它会找到 bug，哪怕需要编造一个。这不是 Agent 的错，这是你的提示词问题。

解决方案一：中性提示词
别说"找 bug"，而说"梳理各模块的逻辑，报告所有发现"。
中性提示不预设结论，Agent 会如实汇报，有 bug 说 bug，没有就说没有。

解决方案二：利用奉承性设计多 Agent 对抗系统
作者设计了一个三 Agent 的 bug 验证机制：
· Bug 发现者：低/中/高影响 bug 分别得 +1/+5/+10 分
· 对抗者：成功反驳得对应分，反驳错误扣 2 倍
· 裁判：告知有真实答案参照，对错各 ±1

明确任务的"终点"
Agent 很擅长开始任务，却不知道何时结束——这是当前模型的固有限制。

两种可靠的终点定义方式：
· 测试套件：明确告知 Agent "X 个测试全部通过才算完成，且不得修改测试文件"。测试是确定性的，Agent 无法糊弄。
· 截图 + 视觉验证：实现功能后让 Agent 截图，并验证设计或行为是否符合预期。Agent 可以根据截图反复迭代，直到视觉结果满足要求。

更高阶的做法：为每个任务创建 {TASK}_CONTRACT.md ，其中列出所有验收条件（测试、截图验证等），结合 stop-hook 机制，强制 Agent 在合同完成前不得退出。

长期运行 Agent 的正确姿势
作者明确反对"24 小时连续运行的超长会话"，原因正是上下文污染——多个不相关合同的上下文混在一起，会导致漂移。

推荐方案：
· 每个合约开一个新会话
· 用一个编排层负责创建合同、分发新会话
会话完成即关闭，下个任务开新会话

规则与技能的管理
CLAUDE. md 的定位：不是一份完整文档，而是一个条件跳转目录。它只告诉 Agent "在什么场景下，去读哪个文件"。

格式示例：
· 如果你在写代码，先读 coding-rules. md
· 如果你在写测试，先读 coding-test-rules. md
· 如果测试失败，先读 coding-test-failing-rules. md

规则（Rules）：编码偏好——"不要做 X"、"总是做 Y"。看到 Agent 做了你不满意的事，就写成规则。
技能（Skills）：编码方法——"按照这个流程做 Z"。如果你想让某件事的做法确定可控，先让 Agent 研究如何做，把方案写成 Skill 文件，然后你审阅修正——这样在真实场景出现前，你就已经掌握了 Agent 的解法。
维护原则：规则和技能积累到一定程度会出现矛盾和冗余，导致性能再次下降。此时需要定期"清理"——让 Agent 整合并去重，向你确认最新偏好。这是一个需要周期性执行的维护动作。

---


**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2028924623664939493  

**正文**

introducing @nozomioai index API.

our mission is to index your entire life and put it into a single file, starting with technical sources.

index repos, docs, datasets, papers, slack, and local folders.

built for agents. works with cursor, claude code, openclaw, and more. 
introducing @nozomioai index API.

our mission is to index your entire life and put it into a single file, starting with technical sources.

index repos, docs, datasets, papers, slack, and local folders.

built for agents. works with cursor, claude code, openclaw, and more. 
get started with Nia: 

https://docs.trynia.ai/welcome

or run in your terminal: 

“bunx nia-wizard”

---


**作者** Jeddi（@antinertia）  
**貼文連結** https://x.com/antinertia/status/2028897556097294692  

**正文**

you want to be a GTM operator in 2026
you need to master:

- claude code
- ai crm systems
- ai automations
- ugc farms
- influencer marketing
- paid ads
- lead magnets strategy
- aeo scale engine
- n8n workflows
- twin workflows
- clay workflows
- json basics
- attribution
- enrichment
- ruthless prioritization
- kpi structure

and all of it powered by claude code

your focus changes depending if plg or sales motion

about your rate

pre series A:
minimum $150–200k + 5% equity

post series A:
up to $280k (bonus not included)

2026 GTM operators won’t be channel specialists

they’ll be ai-native revenue architects

---


**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2028931550310547800  

**正文**

learn to market is the new learn to code

---


**作者** Ihtesham Ali（@ihtesham2005）  
**貼文連結** https://x.com/ihtesham2005/status/2028514380963536918  

**正文**

You don't need to write a single line of code to build a full AI agent with RAG, memory, and tool calling in 2026.

I know that sounds like a lie. But It's not.

Flowise is an open source drag and drop builder for LLM apps and it's the most slept-on AI tool I've seen this year.

What you can build without touching a single line of code:

→ AI chatbots trained on your own documents
→ RAG pipelines connected to any vector database
→ Agents with persistent memory across sessions
→ Multi-agent workflows that chain tools together
→ Full LLM apps connected to your APIs and databases

Supports literally everything - Claude, GPT, Gemini, DeepSeek, Mistral, Llama, and every local model worth running through Ollama.

Self-hosted. Your data stays on your server.

No vendor lock-in. No monthly SaaS bill.

The no-code AI agent builder the big labs don't want you to know about because it makes their expensive APIs feel optional.

49K+ stars and most people in this space still haven't heard of it.

Now you have.

100% Open Source.

(Link in the comments)
You don't need to write a single line of code to build a full AI agent with RAG, memory, and tool calling in 2026.

I know that sounds like a lie. But It's not.

Flowise is an open source drag and drop builder for LLM apps and it's the most slept-on AI tool I've seen this year.

What you can build without touching a single line of code:

→ AI chatbots trained on your own documents
→ RAG pipelines connected to any vector database
→ Agents with persistent memory across sessions
→ Multi-agent workflows that chain tools together
→ Full LLM apps connected to your APIs and databases

Supports literally everything - Claude, GPT, Gemini, DeepSeek, Mistral, Llama, and every local model worth running through Ollama.

Self-hosted. Your data stays on your server.

No vendor lock-in. No monthly SaaS bill.

The no-code AI agent builder the big labs don't want you to know about because it makes their expensive APIs feel optional.

49K+ stars and most people in this space still haven't heard of it.

Now you have.

100% Open Source.

(Link in the comments)
https://github.com/FlowiseAI/Flowise

---


**作者** plantegg（@plantegg）  
**貼文連結** https://x.com/plantegg/status/2028677544791138751  

**正文**

作为一个 MySQL DBA，我花了一个下午，用 Claude Code 从零搭建了一个能自主诊断 MySQL 和 Linux 的 AI Agent。它能自己决定该查什么、怎么查，最后给出一份完整的诊断报告。

题图是 agent 和 LLM 交互的完整过程，可以看到什么时候执行工具什么时候组合成完整 prompt 发给 LLM

这篇文章记录整个开发过程，以及我对 Agent 开发的理解。

## 什么是 Agent？

一句话：Agent = 让大模型持续思考、持续调用外部工具、直到解决用户问题的程序。

和普通的 ChatGPT 对话不同，Agent 不只是"聊天"，它能动手。

普通 LLM 调用：你问一个问题，模型从训练数据里找答案，一问一答就结束了。

Agent：模型分析你的问题后，主动决定调用什么工具（比如 SSH 到服务器执行命令、查 MySQL），拿到真实数据后继续分析，不够就再调，直到能给出完整答案。

核心区别就一个：模型有了"手脚"，能主动获取实时信息。

## ReAct：Agent 背后的核心原理

几乎所有主流 Agent 框架都基于 ReAct 模式，来自 2022 年的论文 "ReAct: Synergizing Reasoning and Acting in Language Models"。

ReAct = Reasoning（推理）+ Acting（行动）

它的工作循环非常直觉：

Thought（思考）→ Action（行动）→ Observation（观察）→ 再 Thought ...

翻译成人话就是：

- 思考："用户问的是主从复制状态，我应该先查 SHOW SLAVE STATUS"
- 行动：调用 mysql\_query 工具执行这条 SQL
- 观察：工具返回"无结果集"——说明这台不是从库
- 再思考："那看看是不是主库吧"
- 再行动：执行 SHOW MASTER STATUS
- 再观察：有 binlog 信息，确认是主库
- ......
- 最终思考："信息够了，可以给出完整诊断报告"

关键在于：你不需要写 if-else 来编排这些步骤。 模型自己决定调什么工具、调几次、什么时候停止。你只需要提供工具，剩下的交给模型推理。

## Agent 开发三要素

Agent = LLM + Tools + Prompt

LLM（大脑）：选什么模型、怎么连。我用的是 Claude Sonnet 4.5，通过公司内部的 OpenAI 兼容网关调用。

Tools（手脚）：写 Python 函数让模型能调用。这是 80% 的工作量。我写了三个工具：ssh\_command（远程执行 Linux 命令）、mysql\_query（执行只读 SQL）、write\_file（保存报告到文件）。

Prompt（指令）：告诉模型它是谁、能做什么。比如"你是资深 DBA，精通 MySQL 5.7/8.0，所有操作只读，用中文回答"。

## 六步开发流程

Step 1：定义场景和工具边界

先想清楚三个问题：

- Agent 解决什么问题？→ MySQL/Linux 远程只读诊断
- 需要哪些工具？→ SSH 命令、MySQL 查询、写文件
- 安全红线是什么？→ 绝对只读，拦截所有写操作

Step 2：搭项目骨架

用 CrewAI 框架，项目结构很简单：config.yaml（配置）、main.py（入口）、crew.py（Agent 定义）、tools/ 目录下放各个工具。

Step 3：写工具（核心）

每个工具就是一个 Python 类，有一个 name、一个 description（模型靠它决定什么时候调用）、一个 \_run 方法（实际执行逻辑）。

工具开发的四个要点：

- description 要写清楚——模型完全靠这段描述来决定什么时候用这个工具
- \_run 返回纯文本——模型只能理解文本
- 做好安全拦截——模型可能会尝试执行 DROP TABLE
- 加超时控制——防止 tail -f 这类命令卡死整个 Agent

Step 4：配置 LLM

配好模型名称、API 地址、密钥。如果用的是 OpenAI 兼容网关，模型名需要加 "openai/" 前缀让路由层正确转发。

Step 5：组装 Agent

把 LLM、工具列表、角色 Prompt 组合到一起，创建 Agent 实例。

Step 6：运行

把用户的问题包装成 Task，交给 Crew 执行，拿到结果。

## 实际效果

我对 Agent 说："检查这台机器的主从复制状态"

它自己完成了以下操作：

1. 执行 SHOW SLAVE STATUS → 发现不是从库
1. 执行 SHOW MASTER STATUS → 确认是主库，拿到 binlog 和 GTID 信息
1. 执行 SHOW SLAVE HOSTS → 发现没有从库连接
1. 查询半同步复制变量 → 发现半同步已降级为异步
1. SSH 查看 MySQL 错误日志 → 找到超时切换的时间点
1. 查询复制用户权限 → 确认配置完整
1. 查看 processlist → 确认没有 Binlog Dump 线程

最终输出了一份完整的诊断报告，准确指出：主库配置正常但当前无从库连接，半同步复制因超时已降级，存在数据丢失风险，并给出了紧急处理建议。

整个过程 6 轮 LLM 调用，全自动，无需人工干预。

## 踩过的坑

真实开发中踩了不少坑，记录几个典型的：

MySQL root 不允许 TCP 连接：root 账户只允许 unix socket 登录，SSH 隧道转发的 127.0.0.1 TCP 连接被拒。解决方案：放弃 pymysql 直连，改为 SSH 到目标机器后用 mysql CLI 通过 socket 执行。

模型后端不支持 assistant prefill：公司网关后面的某些模型走 AWS Bedrock，而 Bedrock 不支持 CrewAI 使用的 assistant message prefill 特性。解决方案：逐个测试网关上的模型，找到走非 Bedrock 后端的模型。

tail -f 卡死 Agent：模型执行 "tail -100 slow-queries.log" 时，如果日志行数不够，tail 会等待新数据写入，导致 SSH 命令永远不返回。解决方案：用 paramiko channel 级别的非阻塞读取 + deadline 超时机制替代 exec\_command。

调试回调被框架覆盖：我写了一个 --debug 模式输出每次 LLM 交互的完整 prompt/response，但 CrewAI 内部会重置 litellm 的回调列表。解决方案：monkey-patch 框架的 set\_callbacks 方法，确保自定义 logger 始终存在。

## 一个公式

Agent 效果 = 模型能力 x 工具质量 x Prompt 清晰度

- 模型不够强 → 换更大的模型
- 工具返回乱码 → 格式化输出，让模型能理解
- 模型不知道用哪个工具 → 改工具的 description
- 模型反复犯错重试 → 加 --debug 看完整 prompt，调整角色描述

## 总结

Agent 开发没有想象中那么难。本质上就是：

1. 给大模型一组工具
1. 告诉它是什么角色
1. 让它自己决定怎么用工具解决问题

80% 的工作量在写好工具——安全拦截、超时控制、输出格式化。剩下 20% 是选模型和调 Prompt。

框架（CrewAI/LangChain/AutoGen）只是脚手架，真正决定 Agent 好不好用的是你的工具质量和对业务场景的理解。

---


**作者** YJ（@YJstacked）  
**貼文連結** https://x.com/YJstacked/status/2028783599445745995  

**正文**

February 2026 Changed Everything About How Work Gets Done

While you were manually managing workflows, your competitors deployed AI agents that plan, execute, and deliver complete projects without human supervision.

Not chatbots. Not assistants. Autonomous systems that run for hours or days, orchestrate teams of specialized sub-agents, and handle everything from research to deployment without you touching anything.

This is not coming. This is operational right now. And the gap between businesses using them and businesses ignoring them is widening every single day.

If you want AI agents running your operations instead of burning your team's time, we build exactly that: [hypergrowai.cc](<https://www.hypergrowai.cc/>)

Ready to automate your workflows? Apply here: [Work With Us](<https://docs.google.com/forms/d/e/1FAIpQLSca0girJXnzC7gTC74-stg_z8pNXljWD6Dt_Li-6BYTOox1Gw/viewform>)

## What Actually Changed in February 2026

Three major product launches between February 5 and February 25 shifted agentic AI from experimental pilots to production-ready tools that businesses are deploying at scale right now.

These are not incremental updates. These are infrastructure-level releases that enable autonomous work at scales that were impossible six months ago.

Perplexity Computer (February 25)

Perplexity launched Computer as a persistent digital worker that operates for hours or months on complex projects without constant supervision.

You describe an outcome. Computer decomposes it into subtasks, spins up specialized sub-agents, and executes asynchronously in isolated cloud environments with full filesystem access, browser control, and API integrations.

The system intelligently orchestrates 19 different AI models simultaneously. Claude Opus 4.6 handles core reasoning. Gemini variants run deep research and create sub-agents. Grok executes lightweight speed tasks. ChatGPT 5.2 manages long-context recall. Specialized models handle images and video.

It is explicitly model-agnostic. You can swap models based on token budgets or performance requirements. The system makes those decisions automatically or you override manually.

Capabilities include web research, document generation at scale, data processing pipelines, coding entire applications from scratch, API orchestration across hundreds of services, and proactive check-ins only when human input is actually required.

Pricing starts at $200 per month for Perplexity Max subscribers. Enterprise Max rollout is imminent with additional governance and compliance features.

This is a direct competitor to open-source solutions like OpenClaw but with managed orchestration, production-ready infrastructure, and enterprise support included.

Early adopters on X are calling it one of the first breakout agentic products of 2026. Not because it is novel. Because it actually works in production environments without constant babysitting.

Claude Opus 4.6 and Enterprise Agents (February 5 and 24)

Anthropic released Claude Opus 4.6 on February 5 with the strongest agentic capabilities yet shipped in a production model.

New capabilities include careful multi-step planning with parallel sub-agent execution, reliable operation in million-line codebases, self-debugging that catches its own mistakes before they ship, and the first 1 million token context window ever available in an Opus-class model.

The benchmarks are industry-leading. Highest score on Terminal-Bench 2.0 for agentic coding. Tops Humanity's Last Exam. Outperforms GPT-5.2 by 144 Elo points on economically valuable knowledge work tasks. Best performance on hard-to-find information retrieval. 76% accuracy on 8-needle retrieval in 1 million token contexts versus 18.5% for the previous Sonnet model.

Real-world performance is more impressive than benchmarks. One-shotting a complete physics engine. Migrating multi-million-line codebases in half the time senior engineers require. Closing 13 issues across six different repositories in a single day for a 50-person engineering team.

On February 24, Anthropic launched its enterprise agents program built on Claude Cowork.

Features include private software marketplaces for company-specific agents, pre-built and customizable plugins for finance modeling and research, engineering workflows, design systems, HR onboarding and offer generation, legal document processing, and operations optimization.

New connectors to Gmail, DocuSign, Google Workspace, WordPress, LegalZoom, and Clay enable agents to work across your entire tech stack without custom integration work.

Admin-controlled data flows and tailored workflows ensure governance and compliance requirements are met from day one.

Kate Jensen, Head of Americas at Anthropic, stated that 2025 hype failed because of approach, not effort. The new system finally delivers IT-governed, deployable agents that enterprises can actually use in production.

Claude Code Autonomy Research

Internal data from Anthropic through January 2026 shows the 99.9th percentile autonomous session length in Claude Code nearly doubled from under 25 minutes in late September 2025 to over 45 minutes by early January 2026.

This is not a small improvement. This is the difference between agents that require constant supervision and agents that can execute complex multi-hour workflows with minimal human intervention.

Experienced users now auto-approve over 40% of agent actions compared to 20% for new users. Interruptions are strategic rather than constant. Software engineering still dominates approximately 50% of tool calls, but high-risk, high-autonomy use cases in finance, healthcare, and cybersecurity are emerging fast.

Claude now pauses for clarification more often than humans interrupt on complex tasks. This enables safer scaling because the agent knows when it needs input versus when it can proceed autonomously.

## What the Data Actually Shows About Adoption

Multiple analyst firms released 2026 outlooks in January and February. The numbers are striking.

Gartner predicts:

By end of 2026, up to 40% of enterprise applications will include integrated task-specific AI agents. That is an 8x increase from less than 5% in 2025.

By 2028, 60% of brands will use agentic AI for streamlined one-to-one customer interactions. 33% of enterprise software applications will be agentic. 15% of day-to-day business decisions will be made autonomously by AI systems.

But the warning is equally important: Over 40% of agentic AI projects will be canceled by end of 2027 due to unclear value proposition, runaway costs, or security and policy violations.

Deloitte reports:

Only 11% of organizations currently have agentic AI in production. 14% are deploy-ready. 38% are piloting. 30% are exploring. 35% have no formal strategy at all.

Legacy systems, poor data architecture, and agent washing—rebranding basic automation as AI agents—are the primary failure modes.

Their recommendation: Treat agents as a silicon-based workforce. Build onboarding processes, performance management systems, FinOps cost controls, and zero-trust identity frameworks exactly like you would for human employees.

McKinsey data from State of AI 2025 survey published January 2026:

Agentic capabilities are scaling fastest in technology for software engineering and IT, insurance for marketing and sales, and healthcare for knowledge management and IT operations.

Overall, only a minority of companies have moved beyond pilots to actually transform their workstreams. But those that do report significant productivity gains that compound over time.

AWS and Harvard Business Review survey from late February:

84% of leaders believe agentic AI will transform their business. 79% plan increased investment in 2026. Yet execution gaps persist. Only 36% report actual productivity gains and 35% report better decision-making among current users.

The gap between belief and execution is the story. Everyone knows this matters. Almost nobody has actually deployed it successfully yet.

## The Challenges Nobody Is Talking About Publicly

The analyst reports are clear about what is breaking agentic AI deployments in production.

Governance gap: Agents are outpacing control systems. Multi-agent protocols, audit logs, and human supervisor frameworks are requirements, not nice-to-haves. Most companies do not have these built yet.

Legacy integration: 48% cite ETL issues as blockers. 47% cite poor data searchability. Agents cannot operate on data they cannot access or understand. Most enterprise data is locked in systems that were not designed for AI access.

Cost and ROI unpredictability: FinOps monitoring is essential. Many pilots stall because leadership cannot predict or justify ongoing spend. Token costs compound fast when agents run autonomously for hours.

Skills atrophy and legal risk: Gartner predicts 50% of organizations will require AI-free skills assessments by end of 2026 to ensure human workers can still perform without agent assistance. Over 2,000 "death by AI" legal claims are projected by end of 2026 if guardrails lag behind deployment.

Agent sprawl: Uncontrolled proliferation creates technical debt and security vulnerabilities. Every agent needs oversight, cost tracking, and performance monitoring. Most companies deploy agents without infrastructure to manage them at scale.

These are solvable problems. But they require deliberate infrastructure work, not just spinning up more agents.

## Where the Actual Opportunity Is Right Now

X conversations throughout February repeatedly frame 2026 as "the year of agents." The products are real. OpenClaw, Kimi Claw, Perplexity Computer, Claude Cowork. These are not vaporware. They are operational.

But current deployments remain heavily concentrated in software engineering. Marketing, sales, operations, HR, and customer service remain wide open for early movers who get the implementation right.

For context: 76% of finance leaders say 2026 is the year for agentic investment according to recent surveys. But only 30% have pilots running and just 6% have production deployments per Savant Labs data.

That gap between intent and execution is the opportunity.

The businesses winning are the ones building:

Custom multi-agent orchestration tailored to their specific workflows rather than generic solutions that do not fit their processes.

Governance frameworks that track agent behavior, costs, and outcomes with the same rigor they apply to human employees.

Legacy modernization that makes their data accessible and usable by agents without rebuilding their entire tech stack.

ROI measurement systems that prove value to leadership and justify continued investment beyond the pilot phase.

Industry-specific plugins and workflows that agents can execute without constant human translation of domain knowledge.

These are not plug-and-play solutions. They require design, integration, testing, and ongoing optimization. That is exactly why most companies are stuck between wanting agents and actually deploying them.

## What This Means for Your Business in the Next 90 Days

By mid-2026, early movers will have agents handling 30% to 50% of routine knowledge work according to converging McKinsey and industry estimates.

The businesses that move now build operational advantages that compound monthly. The businesses that wait face widening performance gaps as their competitors pull ahead on speed, cost structure, and output quality.

The window for being early is closing fast. Not because the technology is going away. Because the competitive advantages of early adoption compound quickly and become difficult to catch once established.

The difference between businesses deploying agents now versus businesses deploying them in 12 months is not just 12 months of productivity gains. It is 12 months of competitive intelligence, workflow refinement, cost optimization, and institutional knowledge that late movers cannot shortcut.

## How We Actually Build This for Clients

Most automation agencies sell you tools and disappear. We build governed, production-ready agent systems that integrate with your existing workflows and actually deliver measurable ROI.

Custom multi-agent orchestration: We design agent teams specific to your workflows. Not generic templates. Systems built around how your business actually operates.

Governance and compliance frameworks: Every agent gets tracking, cost monitoring, performance measurement, and audit trails from day one. Your leadership sees exactly what agents are doing and what value they deliver.

Legacy system integration: We connect agents to your existing data and tools without requiring you to rebuild your entire tech stack. Agents work with what you have, not what you wish you had.

ROI measurement and reporting: Clear metrics on what agents save in time and cost, what they generate in revenue, and where optimization opportunities exist. No black boxes. Just data.

Industry-specific deployment: We build domain expertise into agent workflows so they execute correctly without constant human supervision and translation.

This is not experimental. This is production infrastructure designed to scale as your agent deployment grows.

Start here: [hypergrowai.cc](<https://www.hypergrowai.cc/>)

Apply to work with us: [Application Form](<https://docs.google.com/forms/d/e/1FAIpQLSca0girJXnzC7gTC74-stg_z8pNXljWD6Dt_Li-6BYTOox1Gw/viewform>)

## The Real Timeline

Gartner predicts over 40% of agentic AI projects will be canceled by end of 2027. Not because the technology does not work. Because businesses deploy without proper infrastructure and governance.

The projects that succeed are the ones that treat agent deployment as a system design problem, not a tool purchase.

You need orchestration, governance, integration, measurement, and ongoing optimization. Most businesses do not have the expertise to build that internally. That is what we do.

The gap between knowing you need agents and successfully deploying them is where most businesses are stuck right now. We close that gap.

If you want agents running your operations instead of overwhelming your team, the infrastructure work starts now.

Build it right the first time: [hypergrowai.cc](<https://www.hypergrowai.cc/>)

Ready to deploy? Apply here: [Work With Us](<https://docs.google.com/forms/d/e/1FAIpQLSca0girJXnzC7gTC74-stg_z8pNXljWD6Dt_Li-6BYTOox1Gw/viewform>)

---


**作者** Marc Randolph（@marcrandolph）  
**貼文連結** https://x.com/marcrandolph/status/2028672060021760134  

**正文**

In entrepreneurship … I’ve learned it’s impossible to tell if it’s a good idea in advance, so I no longer waste time “thinking things through.” 

Instead, my mind immediately switches to searching for some quick, cheap, and easy way to test it. 

A dozen sloppy tests teach me more than a single perfect one.

---


**作者** Andrew Altshuler（@1eo）  
**貼文連結** https://x.com/1eo/status/2028566640145670413  

**正文**

I built graph database.

Here is why:
I love graphs and I use them A LOT!

- for agent memory
- for structuring project context
- for building compounding knowledge bases

Yet old-school graph databases are too heavy for agentic workflows. 
They are cloud-first monoliths built for enterprise infrastructure: 
servers, Docker, slow MCPs, and schema maintenance hell.

nanograph started as a question:

> What if graphs felt like SQLite/DuckDB - open, query, done - but with types, migrations, and ergonomics built for agents?

Quick to tear down and rebuild, safe enough to trust, and simple enough to keep in the repo.

I could not find a graph database aligned with this vision. So I built it.

An on-device, embedded, schema-as-code graphDB.

Now let's unpack this:

- Why graph?
- Why on-device?
- Why schema-as-code?

## Why graphs?

Graphs help agents reason through data.

Agents are informed walkers. When an agent investigates an issue, it traverses a context graph. Graphs give the agent reasoning structures.

Now add decision traces to the equation: the explicit HOWs and WHY - workflows, exceptions, reasoning.

![Article Image](<https://pbs.twimg.com/media/HCbpHgqWkAAI_As.jpg>)

Agent now can: Solve a problem → walk the graph → write a new trace → graph compounds.

New reasoning paths are created - agent becomes even smarter.

BTW the graph doesn't need to be standalone. It can sit as a semantic layer on top of your data: SQL/NoSQL or a collection of MD files.

## Why on-device?

Coding agents pull us back to fundamentals: Filesystem, CLIs, Markdown, SQLite/DuckDB.

In PKM, Obsidian is winning, and tools like qmd are getting real traction.

If everything is on-device, everything is simple. Totally private by architecture, not by policy. And you can use your own tooling even inside heavily regulated enterprise environments.

Agents want direct, fast, deterministic access to data. They don't want MCP auth or deal with connection errors.

## Why schema-as-code?

Non-enforced schema means garbage accumulation.

Agents are incredibly creative! Give them a schemaless graph and they will roam free. They'll invent edges like knows, met, connected\_to, spoke\_with - all meaning the same thing. 

That creates precedent poisoning. 
Semantic drift propagates through the reasoning layer. Your graph becomes noisy, retrieval becomes unreliable.

An established schema prevents it. And schema-as-code is the best way to enforce it and track changes.

Additional benefit: it captures the evolution of your contract with the agent. That contract changes as your modeling changes. Track schema history and the agent can see how your model evolved. It becomes another super-useful reasoning trail.

# So what is nanograph?

[nanograph](<https://www.nanograph.io/>) is an on-device graph database packaged as a CLI + a folder.

Engineered around five pillars:

- On-device - a folder, not a service. No Docker, no cloud. Super-fast local queries vs slow cloud roundtrips.
- Zero setup - init creates a DB from a schema, load ingests data. Delete and recreate in seconds.
- Schema-as-code - .pg files in your repo, version-controlled. Types enforced at load and query compile time.
- Time machine - built-in CDC and event sourcing. Every mutation is a ledger entry.
- Power search - full-text, semantic, fuzzy, BM25, hybrid search with graph-constrained reranking.

A nanograph database is a build artifact, not a running service. It is a folder: <name>.nano/ that contains all your graph data: copy it, git it, zip it, encrypt it.

Building it to operate this way was quite challenging. 
Agents are amazing at writing Rust code, but LLMs tend to gravitate towards default thinking on architecture & ergonomics.

I wanted a frontier graphDB, so I went straight into research mode. 
At some point I figured out a clever interplay between Apache Arrow for memory and Lance for storage.

Then designed the query language: 
nanoQL - merging Datalog semantics with GraphQL-shaped syntax.

That was my working prototype that felt just right!

Then I went one layer deeper. I thought I knew databases - I've worked with them all my life. But things turned out waaay more nuanced than I imagined.

I went deep into first principles: indexes, compaction, WAL, CDC, caching, hybrid search. 
Worked on specs with super-smart models (GPT-5.2 PRO and Gemini 3 Deep Thinking).

That was just incredible:
operating on the edge of my engineering and math competences.

nanograph is the most elegant piece of engineering I've ever done.

I really encourage you to try it out!

## Quick start

Give your agent a link to the repo and it will do the full setup: github.com/aaltshuler/nanograph

Or use brew: 

The repo ships two ready-to-run example graphs.

## Star Wars graph

![Article Image](<https://pbs.twimg.com/media/HCbpQmbaQAE_IEn.jpg>)

A knowledge graph of characters, films, factions, and mentor relationships:
9 node types
25 edge types
66 nodes

Great for exploring schema basics, graph traversals, and the full search stack (text, semantic, hybrid).

The schema defines typed nodes with enums and key identity:

Init, load, and query:

Queries are typechecked against the schema - wrong property names, type mismatches, and invalid traversals are caught before execution.

## RevOps context graph

A RevOps context graph: intelligence capture → enrichment → screening → decision → delivery.

10 node types 
21 edge types

This is where nanograph's design really shines: decision traces, policy versioning via Supersedes edges, and multi-hop traversals from signals to outcomes.


![Article Image](<https://pbs.twimg.com/media/HCbprshWgAA2E_b.jpg>)

https://www.nanograph.io/docs/examples/context-graph

The decision trace query walks from an opportunity back through who decided and what signal drove it - the kind of "why did this happen?" question that agents need to answer.

## What nanograph is best for

- Context graphs (decision traces, causal chains, structured context)
- Agentic memory (typed on-device memory for coding agents)
- Personal knowledge (bookmarks, notes, connections; local-first, schema-enforced, versioned)
- Dependency graphs (services, packages, lineage tracking)

## What nanograph is not for

nanograph is intentionally not trying to be everything.

- not a multi-tenant distributed cloud graph
- not an everything-store without schema discipline
- not a transactional system-of-record or ledger

The point is the opposite: keep your nanographs compact, isolated, typed, and focused.

Have as many of them as you need. Init is seconds, delete is seconds. Spin up per-project, per-agent, per-experiment.

nanograph is open source and free to use. 
Your agent will download it and set it up for you, then help you create your schema and ingest your data.

If you like it - give it a star on [GitHub](<https://github.com/aaltshuler/nanograph>)⭐

---


**作者** Karan🧋（@kmeanskaran）  
**貼文連結** https://x.com/kmeanskaran/status/2028550567002509357  

**正文**

No Tutorials. No Docs. No Courses.
Just me, ChatGPT, and AntiGravity Free Trial 😎

I built a complete production-grade ML project and published 2 classic articles.
(150+ stars and 100k+ reads)

🌟 Source Code: https://github.com/karan842/stock-agent-ops/tree/master

Stock-Agent-Ops: generating stock reports using Agentic AI while forecasting prices via separate LSTM and transfer learning services.

Part 1: https://kmeanskaran.substack.com/p/part-1-designing-an-agentic-mlops

Local setup
- Defined problem statement and high-level system design
- Built core forecasting service with model training on parent model (S&P 500) and child models (US stocks)
- Integrated Redis for caching forecasted outputs and rate limiting to avoid exhausting training and prediction services
- Developed AI agents to analyze forecasts, process stock news, create Bloomberg-style reports, and a critic agent for improvements
- Built FastAPI backend for all services
- Created Streamlit UI for financial analysis
- Designed admin monitoring panel to detect data drift, agent observability, and logs
- Set up Prometheus + Grafana for system monitoring
- Integrated Qdrant DB for ticker-based caching of stock reports
- Dockerized all services and used docker-compose

_________________________

Part 2: https://kmeanskaran.substack.com/p/part-2-deploying-a-production-grade

Infra setup:
- Replaced local Ollama with AWS Bedrock models
- Configured AWS CLI and Terraform
- Created Kubernetes manifests
- Wrote Terraform files for AWS infrastructure
- Set up CI/CD with GitHub Actions
- Provisioned Kubernetes cluster on 2 EKS nodes (t3.xlarge instances)
- Destroyed AWS setup using Terraform

Additionally, I created detailed LLD system design docs for both local and AWS setups + a YouTube video:
YT Video: https://youtu.be/pqDu1H2uFl8
System Design Docs: https://github.com/karan842/stock-agent-ops/tree/aws-deployment/doc

It was an intense learning journey, just one project boosted my ML skills 100x and gave me real confidence in MLOps on AWS.

I recommend everyone build in public and publish their work.

Thanks for the support ❤️
No Tutorials. No Docs. No Courses.
Just me, ChatGPT, and AntiGravity Free Trial 😎

I built a complete production-grade ML project and published 2 classic articles.
(150+ stars and 100k+ reads)

🌟 Source Code: https://github.com/karan842/stock-agent-ops/tree/master

Stock-Agent-Ops: generating stock reports using Agentic AI while forecasting prices via separate LSTM and transfer learning services.

Part 1: https://kmeanskaran.substack.com/p/part-1-designing-an-agentic-mlops

Local setup
- Defined problem statement and high-level system design
- Built core forecasting service with model training on parent model (S&P 500) and child models (US stocks)
- Integrated Redis for caching forecasted outputs and rate limiting to avoid exhausting training and prediction services
- Developed AI agents to analyze forecasts, process stock news, create Bloomberg-style reports, and a critic agent for improvements
- Built FastAPI backend for all services
- Created Streamlit UI for financial analysis
- Designed admin monitoring panel to detect data drift, agent observability, and logs
- Set up Prometheus + Grafana for system monitoring
- Integrated Qdrant DB for ticker-based caching of stock reports
- Dockerized all services and used docker-compose

_________________________

Part 2: https://kmeanskaran.substack.com/p/part-2-deploying-a-production-grade

Infra setup:
- Replaced local Ollama with AWS Bedrock models
- Configured AWS CLI and Terraform
- Created Kubernetes manifests
- Wrote Terraform files for AWS infrastructure
- Set up CI/CD with GitHub Actions
- Provisioned Kubernetes cluster on 2 EKS nodes (t3.xlarge instances)
- Destroyed AWS setup using Terraform

Additionally, I created detailed LLD system design docs for both local and AWS setups + a YouTube video:
YT Video: https://youtu.be/pqDu1H2uFl8
System Design Docs: https://github.com/karan842/stock-agent-ops/tree/aws-deployment/doc

It was an intense learning journey, just one project boosted my ML skills 100x and gave me real confidence in MLOps on AWS.

I recommend everyone build in public and publish their work.

Thanks for the support ❤️
Next:
Distributed LLM infra Deployment and building something interesting.

Meanwhile, more blogs on enterprise-level ML and ops.

---


**作者** tobi lutke（@tobi）  
**貼文連結** https://x.com/tobi/status/2028580097700057404  

**正文**

QMD 🫡

---


**作者** Every 📧（@every）  
**貼文連結** https://x.com/every/status/2028523103798841509  

**正文**

At our first OpenClaw Camp, over 500 subscribers watched four people demo AI agents they've been running daily for weeks.

- @NatEliason's @FelixCraftAI has its own X account, wrote a book, and launched an @openclaw marketplace.
- @bran_don_gell's Zosia orders groceries and tracks nanny hours.
- @tedescau's Judd flags growth metrics before meetings.
- @clairevo's Polly schedules meetings mid-Target run.

Full writeup: https://every.to/source-code/openclaw-setting-up-your-first-personal-ai-agent

---


**作者** yibie（@yibie）  
**貼文連結** https://x.com/yibie/status/2028650995153314299  

**正文**

重读 OpenClaw 缔造者 Perter Steinberger 的这篇雄文《Shipping at Inference-Speed》，还有很深的启发，这篇文章是 Perter 说明自己 AI 辅助编程时，他自己工作流、方法、工具选择的转变，而这个转变让他打开与 AI 协作新的大门。

Perter 在 AI 辅助编程的范式转变，是来自他亲自开发的项目 VibeTunnel。年初他花了两个月时间，尝试用Rust、Go 甚至 Zig 重写核心模块，但旧模型一直失败，最终没完成。隔了一段时间，他重新打开这个项目，只给了 codex 两句提示让它把整个转发系统转成 Zig，模型自己跑了五个小时，经过多轮代码压缩，一次就交付了可用的转换。这种事在去年是不可想象的。

之后，他就彻底地改变了与 AI 协作的范式：

一、关键工作流转变

1. 从"阅读代码"到"观看代码流"

- 不再逐行阅读 AI 生成的代码
- 只看代码流的关键部分
- 通过长期经验积累，能凭直觉判断"这个任务应该多久完成"
- 如果 codex 一次没解决，立即警觉可能有问题

2. 项目并行化（3-8 个同时进行）

通常结构：1 个核心大项目，多个卫星项目（CLI 工具、小功能等）

当大项目在推理时，切换到其他项目
"软件开发就像爬山——不是直线上升，而是绕着山转圈"

3. 默认从 CLI 开始

- 所有项目默认先做成命令行工具、
- AI 可以直接调用和验证输出
- 快速闭环（closing the loop）
- UI 和 Web 是后续添加的

二、具体工作流技巧

1. 极简提示词（Prompts）

旧方式：长篇大论的语音口述提示
新方式：
- "build" 或 "write plan to docs/*.md and build this"
- 拖拽 UI 截图 + "fix padding"
- "look at ../vibetunnel and do the same for Sparkle changelogs"

2. 无计划模式（No Plan Mode）

- 不搞复杂的"计划模式"
- 直接开始对话 → 让模型探索 → 共同制定计划 → "build"
- 认为计划模式是旧模型的产物（那时模型不擅长遵循提示）

3. 直接提交到 main

- 不使用 worktree（工作树）
- 不使用复杂的分支策略
- 如果代码乱了，让 AI 重构而不是回退
- 大任务留在分心时做（如写文章时同时跑 4 个重构任务）

4. 知识管理：docs/ 文件夹

不使用：复杂的会话历史系统、issue 追踪器

使用：
- 每个项目的 docs/ 文件夹
- 全局 http://AGENTS.MD 文件
- 脚本强制模型读取相关文档
- 用 "write docs to docs/*.md" 让模型自己命名文件

5. 跨项目复用

提示词示例：
"find all my recent go projects and implement this change there too + update changelog"
"look at ../project-folder and do the same here"

三、反直觉的工具选择

❌ 线性/问题追踪器（Linear/issue trackers）
❌ Slash 命令（/commit 不如直接打 "commit/push"）
❌ 多智能体编排系统（multi-agent orchestration）
❌ 异步代理（Cursor Web/codex remote）→ 缺少可控性
❌ 检查点/回滚（让 AI 改而不是 revert）

四、金句摘录

1. "大多数软件不需要深度思考" — 数据从一个表单传到另一个表单
2. "与模型对抗通常是浪费时间和 token" — 设计符合模型训练数据习惯的代码结构
3. "我设计代码库不是为了让我容易导航，而是让 agents 能高效工作"
4. 上下文管理 > 上下文大小 — Codex 虽然窗口大，但内部思考更紧凑，能比 Claude 在相同 token 下完成 5 倍工作
5. 长提示词已死 — 在 GPT 5.2 时代，短提示 + 图片/示例足够

https://steipete.me/posts/2025/shipping-at-inference-speed

---


**作者** Yanhua（@yanhua1010）  
**貼文連結** https://x.com/yanhua1010/status/2028737821855580662  

**正文**

说实话，读完 Anthropic Claude Code 团队最近分享的这篇构建经验，我盯着屏幕想了很久。

不是因为技术多复杂。恰恰相反，整篇文章最让我震动的一句话极其朴素：

「你要学会像智能体一样看世界。」

这句话来自 Claude Code 的核心开发者。一个每天跟 AI 智能体打交道的人，他给出的最重要建议，不是什么架构方案或框架选型，而是一种认知方式的转变。

这让我想到一个更大的问题：2026 年了，我们跟 AI 协作的方式，是不是从根上就搞错了？

## 一、给 AI 一把锤子，它不一定能盖房子

Claude Code 团队讲了一个特别生动的类比。

想象你面前有一道很难的数学题。你希望有什么工具来帮忙？

如果你只会心算，给你纸和笔就够了。如果你会用计算器，给你一台计算器效率更高。如果你会编程，那直接给你一台电脑是最快的。

工具的上限，取决于使用者的能力。

这个道理看起来简单，但放到 AI 智能体设计上，绝大多数人都搞反了。很多人的思路是：给 AI 塞尽可能多的工具，50 个、100 个，覆盖所有可能的场景。觉得工具越多，AI 越强大。

结果呢？AI 面对一堆工具，就像你面对一个有 200 个按钮的遥控器。不是不能用，是选择成本太高，经常选错。

Claude Code 的做法完全不同。它只有大约 20 个工具，而且团队一直在问自己：是不是还太多了？

少，不是因为省事。少，是因为理解。

![Article Image](<https://pbs.twimg.com/media/HCdSPwUbAAAWuHS.jpg>)

## 二、曾经救命的工具，后来变成了枷锁

这是整篇文章里我觉得最精彩的一个教训。

Claude Code 刚上线的时候，团队发现模型经常忘记自己在干什么。做着做着就跑偏了，完全丢失上下文。

怎么办？给它一个待办事项列表。开始的时候列好任务，完成了就勾掉。简单直接，效果立竿见影。

甚至光有列表还不够。团队还每隔 5 个回合插入一次系统提醒："喂，别忘了你的任务是什么。"

但随着模型变聪明了，问题来了。

模型觉得被待办清单困住了。它想灵活调整策略，但系统不断提醒它"按计划执行"。就像一个越来越能干的员工，老板却还在用实习生的管理方式盯着他。

最终团队做了一个大胆的决定：把待办事项工具干掉了。

取而代之的是一个叫"Task"的新工具。不再是"提醒你该做什么"，而是"帮你和其他智能体沟通协调"。任务支持依赖关系，可以在子智能体之间共享更新，模型自己可以修改和删除任务。

从被管理，到自管理。

这件事的启发很直接：模型在变强，你给它的工具也得跟着变。昨天好用的设计，今天可能就在拖后腿。

![Article Image](<https://pbs.twimg.com/media/HCdSSnWacAApIVA.jpg>)

## 三、不是给更多工具，而是让它自己去找

Claude Code 最初怎么理解你的代码库？用 RAG 向量数据库。把你的代码切块、索引、存起来，AI 需要的时候从数据库里检索。

这是行业标准做法，快速、成熟、好理解。

但 Claude Code 团队发现了一个根本性的问题：AI 是被动接受上下文的。

它不是自己去理解你的项目，而是被喂了一堆可能相关的代码片段。就像你入职第一天，同事把公司所有文档甩给你，而不是让你自己去探索、去问问题、去建立理解。

于是他们换了思路：给 AI 一个 Grep 工具，让它自己搜索代码库。

效果出人意料地好。而且随着模型越来越聪明，它搜索和理解上下文的能力也越来越强。

这个思路后来演变成了一个核心设计原则：渐进披露（Progressive Disclosure）。

不是一次性把所有信息倒给 AI，而是让它按需发现。Skill 文件可以引用其他文件，模型可以递归读取，一层一层深入。实际上，很多 Skill 的用途就是教 AI 如何使用某个 API 或查询数据库，也就是「教它怎么自己找答案」。

一年时间，Claude 从几乎无法构建自身上下文，进化到能在多层嵌套文件中精准找到所需信息。

这带来了一个很实际的启发：与其不断增加工具数量，不如提升 AI 自主获取信息的能力。给它一根鱼竿，比每天给它送鱼有用得多。

![Article Image](<https://pbs.twimg.com/media/HCdSVfAbYAAE-m1.jpg>)

## 四、2026 年的分水岭：从 Vibe Coding 到 Agentic Engineering

Claude Code 团队的这些经验，放在更大的行业背景下看，会更有意思。

2025 年初，Andrej Karpathy 发明了一个词叫"Vibe Coding"。意思是跟着感觉走，让 AI 生成代码，差不多能用就行，不用太较真。当时这个词火遍全网，因为它精准描述了大多数人使用 AI 写代码的状态。

但到了 2026 年 2 月，Karpathy 自己宣布这个词过时了。

取而代之的新词叫 Agentic Engineering。

区别在哪？

Vibe Coding = 随缘。AI 写什么用什么。

Agentic Engineering = AI 负责执行，人类负责架构、质量和正确性。

Karpathy 说得很明确："你 99% 的时间不再直接写代码，但你需要更强的工程能力来监督和验证 AI 的输出。"

Claude Code 团队的经验说的其实就是这回事。他们发现，设计智能体的工具"既是一门艺术，也是一门科学"。靠直觉乱塞工具不行，照搬教科书也不行。你得观察模型的行为，读它的输出，做大量实验。

开发者的价值不再是打字速度或背 API 参数，而是你能不能把问题定义清楚，以及看一眼就知道 AI 的输出对不对。

![Article Image](<https://pbs.twimg.com/media/HCdSYX8bkAA0kpp.jpg>)

## 五、像智能体一样思考，到底意味着什么？

说了这么多，回到那句核心的话：像智能体一样看世界。

这不只是一条给 AI 工程师的建议。我觉得它对每个跟 AI 协作的人都适用。

首先，你得知道 AI 的能力边界在哪。你不能给一个刚入职的实习生一台超级计算机，然后期待他搞出惊天动地的成果。给 AI 工具之前，先花时间观察和实验，别看几篇教程就下结论。

然后，管理的尺度很微妙。待办事项的教训已经说明了，管太多会限制 AI 的潜力，完全不管也不行。给个方向、给点资源，让它自己跑，最后你来看结果就行。

最后，别指望一套方法用到老。你今天觉得完美的工作流，三个月后可能就需要推翻重来。Claude Code 团队说"我们倾向支持一小批能力比较类似的模型"，就是因为每次模型升级，他们都要重新评估整个工具设计。你跟 AI 的协作方式，也得跟着迭代。

## 写在最后

McKinsey 最近的一份报告说了一句话，我觉得说得特别好：

"培养 AI 智能体更像是入职一个新员工，而不是部署一套软件。"

如果你把 AI 当软件，你会期待它即插即用、永远稳定、越多功能越好。

如果你把它当新员工，你会花时间了解它的能力，给它匹配的工具和职责，设定清晰的目标，然后留出成长空间。

Claude Code 团队花了一年时间，从"给模型塞更多工具"走到"学会像模型一样思考"。这个转变听起来简单，做起来需要打破很多直觉。

2026 年，AI 能力在指数级增长，但大多数人使用 AI 的方式还停留在"给它下指令，等它出结果"。

也许是时候换个视角了。

不是让 AI 来适应你的思维方式，而是你先学会像智能体一样看世界。

本文基于 Anthropic Claude Code 团队的构建经验分享，结合 2026 年 AI 智能体行业趋势撰写。

参考来源：

- Anthropic Engineering Blog: Building Effective Agents
- Karpathy 关于 Agentic Engineering 的定义（2026 年 2 月）
- McKinsey: One Year of Agentic AI - Six Lessons
- MIT Sloan: Agentic AI Explained

---


**作者** Nyk 🌱（@nyk_builderz）  
**貼文連結** https://x.com/nyk_builderz/status/2028742129200034281  

**正文**

Most teams can build AI agents.
Very few can operate them continuously.

Bottlenecks I keep seeing: context routing, failure recovery, cost guardrails, clean handoffs.

Mission Control is one layer.
Next to it, I'm exploring deeper layers: 

LACP (local agent control) + OneClaw (Rust single-binary framework).

If you run agents in prod — what breaks first?
Most teams can build AI agents.
Very few can operate them continuously.

Bottlenecks I keep seeing: context routing, failure recovery, cost guardrails, clean handoffs.

Mission Control is one layer.
Next to it, I'm exploring deeper layers: 

LACP (local agent control) + OneClaw (Rust single-binary framework).

If you run agents in prod — what breaks first?
Open sourcing soon 

---


**作者** Dinesh Pai（@dineshpaii）  
**貼文連結** https://x.com/dineshpaii/status/2028739486465851840  

**正文**

Most first-time founders sign term sheets, SHAs, and SSAs without fully understanding what they're agreeing to. This is something I get to hear from founders very very often. You'd be surprised how often I get messages about this in different contexts. This is not because they're careless, but because legal documentation is dense, expensive to get reviewed, and nobody teaches you this stuff. 
 
I've seen founders get locked into clauses they didn't understand. Liquidation preference that only favours the investors, anti-dilution that again destroys founder equity, and so many other things. And even when some of them do hire lawyers, they often can't tell if the bill is proportionate to the work. Its a problem. 
 
Well, LegalOS is a small attempt to change that. 

It's an open-source tool for Founders to drop in a term sheet, an SHA, or an SSA. Get a clause-by-clause breakdown in plain English. It clearly articulates what's standard, what's aggressive, and what to push back on. Every clause is colour-coded, with real examples and explanations of founder impact. I have tried to add the things we watch out for our founders, along with some examples we have come across. It's not exhaustive, but the idea is to start small and expand on it. Also, it is clear to me that generic AI-specific saas solutions are not great. As founders you'd rather build capability inhouse and also develop your own risk tolerance, your own processes and knowledge base, without any external dependency. You will need just Claude subscription. 

I have tried to add free explainer guides for all three documents. Mostly through comparison tables showing standard vs aggressive vs unusual terms across every concept. 

Btw, the tool learns your preferences over time. Tell it what it missed, what wasn't relevant, and it sharpens to your deal context. You can even export your preferences file and use it as context in Claude Projects, ChatGPT, or any AI interface. Or maybe even other founders when you want to help them. 

A disclaimer that this isn't a replacement for a good lawyer reviewing all the documents. But it's a way to know which clauses to push back on, what questions to ask, and where to spend your time. And also to have some visibility on what your legal team is agreeing to. 
 
Built for Indian startups. Open source. Powered by @claudeai.

https://github.com/paidinesh7/LegalOS
Most first-time founders sign term sheets, SHAs, and SSAs without fully understanding what they're agreeing to. This is something I get to hear from founders very very often. You'd be surprised how often I get messages about this in different contexts. This is not because they're careless, but because legal documentation is dense, expensive to get reviewed, and nobody teaches you this stuff. 
 
I've seen founders get locked into clauses they didn't understand. Liquidation preference that only favours the investors, anti-dilution that again destroys founder equity, and so many other things. And even when some of them do hire lawyers, they often can't tell if the bill is proportionate to the work. Its a problem. 
 
Well, LegalOS is a small attempt to change that. 

It's an open-source tool for Founders to drop in a term sheet, an SHA, or an SSA. Get a clause-by-clause breakdown in plain English. It clearly articulates what's standard, what's aggressive, and what to push back on. Every clause is colour-coded, with real examples and explanations of founder impact. I have tried to add the things we watch out for our founders, along with some examples we have come across. It's not exhaustive, but the idea is to start small and expand on it. Also, it is clear to me that generic AI-specific saas solutions are not great. As founders you'd rather build capability inhouse and also develop your own risk tolerance, your own processes and knowledge base, without any external dependency. You will need just Claude subscription. 

I have tried to add free explainer guides for all three documents. Mostly through comparison tables showing standard vs aggressive vs unusual terms across every concept. 

Btw, the tool learns your preferences over time. Tell it what it missed, what wasn't relevant, and it sharpens to your deal context. You can even export your preferences file and use it as context in Claude Projects, ChatGPT, or any AI interface. Or maybe even other founders when you want to help them. 

A disclaimer that this isn't a replacement for a good lawyer reviewing all the documents. But it's a way to know which clauses to push back on, what questions to ask, and where to spend your time. And also to have some visibility on what your legal team is agreeing to. 
 
Built for Indian startups. Open source. Powered by @claudeai.

https://github.com/paidinesh7/LegalOS
Got some really good feedback and made the changes,  LegalOS is now, 

 - Portable — your preferences travel with you to any AI interface, including Claude co-work.  
 - Multi-provider — works with Claude, GPT-4o, or Gemini. 

Added all the details to readme file. :)

---


**作者** Femke Plantinga（@femke_plantinga）  
**貼文連結** https://x.com/femke_plantinga/status/2028772412490240079  

**正文**

Most legal AI assistants take 6+ months to build.

We shipped ours in 36 hours. Here’s how:

Legal research is complex by design. You need extreme precision, absolute security, and the ability to filter through thousands of contracts by date, jurisdiction, or clause type. 

Traditional RAG systems collapse under this complexity because they follow a linear path: query → search → generate.

The problem with this approach is that legal queries are never one-dimensional.

When you ask "What are the notice periods in our 2024 service agreements?", a naive RAG system might pull semantically similar clauses from 2022. Without a reasoning layer, it lacks the common sense to apply necessary filters before searching.

This is why building production-ready legal assistants usually requires months of custom orchestration: managing conversation state, writing complex query logic, coordinating retrievers.

𝗔𝗴𝗲𝗻𝘁𝗶𝗰 𝗦𝗲𝗮𝗿𝗰𝗵 changes this entirely.

When our finance team asked us to help navigate internal contracts, we used Weaviate's 𝗤𝘂𝗲𝗿𝘆 𝗔𝗴𝗲𝗻𝘁 to turn raw PDFs into a production app in 36 hours. 

The agent treats the database as a set of tools rather than a static data store, autonomously handling:
• Schema inspection to determine the best search strategy
• Structured query construction with complex filters
• Precision reranking based on actual relevance
• Answer synthesis grounded in retrieved context

We embedded legal PDFs using ColQwen (a multimodal model that preserves layout and tables) with Muvera compression, split contracts into three collections by type, and let the agent handle all the orchestration we'd normally spend months building.

The architecture is more sophisticated than traditional approaches - but requires way less custom code.
→ In Search Mode, it retrieves and reranks relevant contract sections. 
→ In Ask Mode, it synthesizes grounded answers with cited sources. Both modes stream results with full transparency to reduce hallucinations.

Read the full tutorial here: https://weaviate.io/blog/legal-rag-app?utm_source=channels&utm_medium=fp_social&utm_campaign=paralegal&utm_content=diagram_post_268069679

---


**作者** xiyu（@ohxiyu）  
**貼文連結** https://x.com/ohxiyu/status/2028445432729506095  

**正文**

Anthropic 开放了免费的 Academy 课程，13 门，从 Prompt Engineering 到 MCP 到 Claude Code，全覆盖。

完整提示词 -- 复制发给你的openclaw

别收藏了。打开你的配置文件，现在就改。

## 一、最大收获：Adaptive Thinking（省钱 30-50%）

这是 ROI 最高的一个改动。五分钟改完，立刻省钱。

我之前用的是固定 thinking budget：

{"thinking": {"type": "enabled", "budget\_tokens": 32000}}

问题很明显——不管你问"现在几点"还是"帮我做个深度分析"，都烧同样的 thinking tokens。Opus 不便宜，这个浪费很痛。

Opus 4.6 已经废弃了 type，推荐的新写法：

{
  "thinking": {"type": "adaptive"},
  "output\_config": {"effort": "high"}
}

核心区别：Claude 自己判断需要多少思考。简单问题可能 0 thinking tokens，复杂问题全力以赴。

effort 参数有三档：low / medium / high，控制思考上限。

关键洞察：不同 Agent 应该用不同 effort。

- low：日常对话、状态查询、简报生成、消息路由。这些任务不需要深度推理，low 就够了。
- medium：内容写作、日常监控、信息整合。需要一定思考但不复杂。
- high：深度分析、代码生成、财务计算、复杂决策。这些钱不能省。

我的系统里有多个 Agent 各司其职，改完之后路由 Agent 用 low，分析 Agent 用 high，写作 Agent 用 medium。整体 thinking token 消耗直接降了大概三到四成。

💡 操作建议：如果你的系统只有一个 effort 配置，今天就按任务类型拆分。这是最快见效的优化。

## 二、Think Tool：Agent 系统的隐藏武器

这个是课程里让我最意外的。

先说区别：Extended Thinking 是调用前思考，Think Tool 是调用间思考。

Extended Thinking 发生在 Claude 生成回复之前，一次性完成。但在多 Agent 场景里，Claude 经常需要连续调用多个工具——先查数据，再分析，再写入。工具调用之间，Claude 没有"暂停思考"的机制。

Think Tool 解决的就是这个问题。它就是一个普通的工具定义：

{
  "name": "think",
  "description": "Use this tool to think through complex problems step by step before taking action. Call this when you need to reason about which tool to use, verify your approach, or plan multi-step operations.",
  "input\_schema": {
    "type": "object",
    "properties": {
      "thought": {
        "type": "string",
        "description": "Your step-by-step reasoning"
      }
    },
    "required": \["thought"\]
  }
}

没有任何 handler——调用它不执行任何代码，纯粹是给 Claude 一个"思考缓冲区"。但 Anthropic 实测发现，加了这个工具后，policy 遵循率和多步骤任务的准确性显著提升。

哪些 Agent 该加 Think Tool？

- ✅ 路由/调度类 Agent（需要判断任务该给谁）
- ✅ 分析/研究类 Agent（需要多步推理）
- ✅ 代码类 Agent（需要逻辑验证）
- ✅ 涉及权限/安全检查的 Agent
- ❌ 纯创意输出的 Agent（写文章、写推文）
- ❌ 单步操作的 Agent（查天气、记账）

Think Tool vs Extended Thinking，怎么选？

不是二选一。它们互补：

- Extended Thinking：处理请求前的整体规划
- Think Tool：工具调用链中的步骤间推理

我的做法是两个都开。路由 Agent 用 effort + Think Tool，分析 Agent 用 effort + Think Tool。

## 三、Prompt Engineering 实战：5 个立即可用的技巧

课程 9 章内容，浓缩成 5 个我实际用到的。

3.1 XML 标签分离指令与数据

之前我的 Skill 文件（类似 system prompt 的模块化配置）把指令和参考数据混在一起。Claude 经常搞混"这是让我做的事"和"这是给我参考的数据"。

改成 XML 标签后清晰多了：

<instructions>
你是一个财务分析 Agent。分析以下数据并给出建议。
输出格式：先结论，再数据支撑，最后风险提示。
</instructions>

<reference\_data>
{{动态注入的数据}}
</reference\_data>

Claude 对 XML 标签的解析极其可靠。这不是什么新技术，但实际动手改的人不多。

3.2 Speaking for Claude（Output Prefill）

与其说"请用 JSON 格式输出"，不如直接在 assistant 消息里预填开头：

Assistant: {"analysis": "

Claude 会自然接续，格式错误率大幅降低。

这个技巧在 API 调用中很容易实现——messages 数组最后加一个 role 的消息，内容就是你想让 Claude 接续的开头。

3.3 Few-shot 示例的正确姿势

对格式要求严格的输出（比如固定格式的简报、特定风格的推文），1-2 个示例效果远超长篇描述：

<examples>
<example>
<input>分析苹果 Q3 财报</input>
<output>
📊 Apple Q3 FY2025
- 营收：$XX B（+X% YoY）
- 关键：服务业务占比首次超过 XX%
- 风险：中国市场持续承压
</output>
</example>
</examples>

关键：示例要覆盖边界情况，不要只给"完美示例"。

3.4 防幻觉指令（一句话就够）

对涉及事实查询的 Agent（情报类、财务类、研究类），在 system prompt 里加一句：

如果你不确定某个数据或事实，明确说"我不确定"或"需要验证"。错误信息比没有信息更危险。

就这一句。简单，但很多人不加，然后被 Claude 自信满满的幻觉坑到。

3.5 System Prompt 分层

这是我改动最大的一个。之前的 system prompt 试图一次性塞入所有指令，结果越靠后的规则越容易被忽略。

Anthropic 建议的分层结构：

<critical\_rules>
绝对不能违反的规则（安全、权限、格式）
</critical\_rules>

<standard\_rules>
日常行为规范
</standard\_rules>

<reference>
参考信息，按需使用
</reference>

优先级从上到下递减。核心身份和关键安全规则放最前面，参考资料放最后。

另一个建议：可缓存的静态内容放前面，动态内容放后面。 这样配合 Prompt Caching（下面会讲），静态部分只需要传一次。

## 四、MCP 的 90% 你没用到

如果你在用 MCP（Model Context Protocol），大概率只用了 Tools、Resources、Prompts 这三个核心原语。但 MCP 还有三个高级特性，大多数人完全没碰过。

4.1 Sampling：Server 反向调 LLM

这个最让我兴奋。

正常流程是 client 调 server 的工具。Sampling 反过来——MCP server 可以请求 client 端帮它调 LLM。server 本身不需要持有任何 API key。

场景很多：

- MCP server 处理数据时需要 AI 辅助分类
- 自动摘要、自动标注
- server 端做决策需要 LLM 判断

架构优势：AI 成本和复杂度集中在 client 端管理，server 保持轻量。

4.2 Roots：目录声明

正式声明哪些目录对 LLM 可见：

{
  "roots": \[
    {"uri": "file:///path/to/workspace", "name": "Project Root"}
  \]
}

比起让 LLM 自己摸索文件结构，Roots 提供明确的访问边界。安全性和效率都更好。

4.3 Elicitation：向用户提问

MCP server 可以主动向用户提问，获取额外信息：

{
  "method": "elicitation/create",
  "params": {
    "message": "请确认要执行此操作吗？",
    "requestedSchema": {
      "type": "object",
      "properties": {
        "confirm": {"type": "boolean"}
      }
    }
  }
}

当 server 需要用户确认或补充信息时，不用让 LLM 转述，直接问用户。

💡 这三个特性能不能用，取决于你的 MCP client 框架是否支持。建议先查文档确认，再决定要不要投入时间。

## 五、从 Claude Code 学到的 Agent 模式

Claude Code 课程不长，但里面几个 Agent 模式很实用。

5.1 并行 Subagent

之前我的系统是串行的——一个任务 spawn 一个子 Agent，等完成了再下一个。

Claude Code 的思路：识别可并行的子任务，同时 spawn。

任务：生成周报
  ├── Agent A → 收集各渠道数据（并行）
  ├── Agent B → 分析趋势变化（并行）
  └── 主 Agent → 等 A+B 完成 → 汇总输出

改动不大，但复杂任务的完成时间能缩短不少。

5.2 自动重试

子 Agent 失败后自动重试一次，不惊扰用户：

- 第一次失败 → 自动重试（附上错误信息帮助修正）
- 第二次失败 → 上报用户 + 错误详情
- 永远不重试：涉及资金转账、消息发送、数据删除的操作

这个规则很简单，但能大幅减少人工干预。

5.3 上下文压缩

长对话 session 的上下文会不断膨胀。Claude Code 有个 compact 模式——自动压缩历史对话，保留关键信息。

对于需要长时间运行的 Agent（比如项目管理类、持续监控类），上下文压缩是必须的。否则跑着跑着就超 context window 了。

## 六、我的改动清单（17 项，按 ROI 排序）

🔴 5 分钟见效

1. 切换 Adaptive Thinking — 把 type 改成 type，配上 effort 参数。立省 30-50% thinking tokens。

2. 添加 Think Tool — 给路由、分析、代码、监控类 Agent 加上面那个 JSON 定义。零成本，显著提升多步推理准确性。

3. 按 Agent 配置 Effort 级别 — 日常 low，创作 medium，分析 high。不要一刀切。

🟡 需要改文件

4. Skill 文件 XML 标签重构 — 所有 Skill 文件用 <instructions> / <examples> / <reference> 分离。

5. System Prompt 分层重构 — 核心身份 + 关键规则放最顶部，用 <critical\_rules> 包裹。参考信息用 <reference> 放底部。

6. 添加 Few-shot 示例 — 对格式敏感的输出（简报、推文等），加 1-2 个示例。

7. 防幻觉指令 — 所有涉及事实查询的 Agent 加一句。

8. Think Tool 使用指引 — 在相关 Agent 的 system prompt 里加一句"在复杂决策和多步操作前使用 think tool"。

9. System Prompt 精简 — 审计所有 Agent 的 system prompt 大小，超长的砍掉冗余，核心指令前置。

🟢 需要调研

10. Prompt Caching — 检查你的框架是否已对 system prompt 自动启用缓存。如果没有，手动加 cache\_control。cache hit 只收 1/10 价格。

11. MCP Sampling — 检查你的 MCP client 是否支持 sampling capability。如果支持，MCP server 就能反向调 LLM。

12. MCP Roots — 配置目录声明，明确文件访问边界。

13. 并行 Subagent — 改路由逻辑，识别可并行的子任务。

14. 自动重试机制 — 子 Agent 第一次失败自动重试，第二次再上报。

15. 上下文压缩 — 对长 session Agent 启用 compact 模式（取决于框架支持）。

16. MCP Elicitation — 让 MCP server 能直接向用户提问。

17. Assistant Prefill — 在 API 调用中预填 assistant 消息开头，引导输出格式。

## 结尾

13 门课，一下午看完。但看完不等于学到，学到不等于改进。

改进 = 学习 + 动手。

这 17 个改动里，前 3 个五分钟就能搞定，改完立刻省钱。如果你也在跑多 Agent 系统，建议今天就改。

---


**作者** Annie ❤️‍🔥（@AnnieLiao_2000）  
**貼文連結** https://x.com/AnnieLiao_2000/status/2028693049598157058  

**正文**

In the last year, we built 50K+ AI builder community across 60+ cities with just IRL events. At Build Club, we have partnered with the fastest growing AI companies in the world on their community GTM: Manus (Academy), Lovable (Shipped), and Gemini Studio.

In an attention economy, community cuts through this noise through pulling on the innate human desire of connection.

We call this category of IRL activation = "community led growth"

Here's the best in practise playbook we have seen the fast growing AI companies use to scale this new concept of "community led growth" in a way that actually matters and delivers ROI

## The Context: IRL Is Coming Back

It’s no surprise it’s a distribution war in the AI market right now.

I recently caught up with a partnership lead at a vibe-coding tool (500K+ users). She said, when the tools are similar, taste becomes the differentiator, this is linked to loyalty and brand perception. 

When someone builds with your tool in a room full of peers, the switching cost changes... 

The unlock: the narrative shifts from “I tried it” to “I’m part of this." 

That’s the leverage. 

We’ve seen [Cafe Compute](<https://x.com/SarahChieng/status/2028552671683383784?s=20>), [Cursor Coffee](<https://x.com/benln/status/2028477372593304011?s=20>), and Claude “Build” fellowships spin up around this thesis.

## The Approach: Institutions Are the Best Examples of Community (North Star)

I love systems. Communities, at their core, are miniature economies when you break them down.

When I decided to scale our community, I studied historically successful communities (not tech PLG strategies).

I believe churches and scouts are some of the best examples of scalable community systems historically which have stood the test of time.

They are:

- Decentralized (or symbolically anchored to one leader)
- Structured around playbooks and incentive systems
- Locally autonomous, centrally aligned

They scale because of structure, belonging, and shared mission.

## What Community ROI Looks Like as a GTM Strategy

Most founders frame community as marketing. The real leverage is structural.

As we scaled Build Club, we built three flywheels that we track:

![Article Image](<https://pbs.twimg.com/media/HCb8ywSbcAEsIlj.jpg>)

## 1) The PLG Flywheel

Marketing → First IRL Event → Engaged Member → PLG Lead Gen

Your best customers don’t just buy. They advocate. Community compresses the distance between awareness and revenue.

## 2) The SLG Flywheel \[New\]

City Lead → Ambassador → Affiliate for your Enterprise Product  → Revenue

When ambassadors can refer enterprise deals, introduce partnerships, and earn through affiliates, you’ve turned engagement into revenue.

This flywheel can be launched when the sales playbook becomes repeatable.

## 3) The Partnerships Flywheel (The Layer Most People Miss)

This is where the community becomes asymmetric. 

You can growth hack through onboarding partners / collaboraters into your community ecosystem through IRL activations, ambassador networks, academy infrastructure, and enterprise enablement via our platform. 

That strengthens the flywheel, attracts more partners, and creates a revenue loop that’s difficult to replicate.

# The Exact Playbook

## 1) Start With a Super Specific ICP

For example, at Build Club, we started with technical AI engineers and startup founders. Nothing else. That focus shaped everything.

Only later did we realize learners outnumbered builders, which led to new academy products focused on technically lite audiences.

You only see that signal when you start narrow, e.g., college programs, research fellowships etc.

## 2) Find Your One Format - Then Become the Best in the World at It

We spent a full month iterating on format before scaling. For us, it was co-working with a strong focus on building which aligned with our thesis on learning.

It worked because it was repeatable, high-trust, and operator-friendly.

Upgrade the experience deliberately as you go: good lighting, good playlists, minimal but intentional branding.

Here's a quick summary of some popular engagement modalities :) 

![Article Image](<https://pbs.twimg.com/media/HCdMQrZbEAAQATv.jpg>)

## 3) Don’t Recruit City Leads. Attract Them.

We never cold-recruited city leads. They emerged from engaged members, often via referrals.

The flywheel: Great Events → Engaged Members → Inbound City Leads → More Great Events

Give the right operators a tight playbook, clear ownership, and direct access to your core team. Treat them like partners not contractors.

![Article Image](<https://pbs.twimg.com/media/HCb6205a0AAkVjz.jpg>)

## 4) Incentive Alignment Is the Engine

We onboard every City Lead 1:1 with a community manifesto and branding playbooks.

We treat our City Leads as customers and work to solve their pain points: affiliate structures, enterprise referral pathways, and partnership revenue splits.

A key focus has been on the concept of the “model citizen”, when a community has a clear relatable archetype to aspire towards it grounds the vision/ mission of the movement in truth.

If your community creates value, operators need alignment.

## 5) Your Tech Stack Should Embarrass You (But Automate Where Human Touch Isn’t Critical)

We use Airtable, Notion, Google Docs still even today and it works. 

We use Manus to manage and surface Slack messages from our community which I built in one hour (check it out [here](<https://build-club-feedback.manus.space/>)) 

If you’re investing in $$ community platforms (Circle, Skilljar, Skool) before validating operator density... you’re procrastinating.

Importantly, Community must plug directly into partnerships, product, and revenue. If it lives in isolation, it dies.

## P.S. Don’t Hire a Community Manager. Hire a Platform Manager.

Hot tip: this is where most AI startups go wrong… you don’t need an event planner.

You need a systems operator who thinks in systems, but also is an extrovert with a creative flair, magnetism and strong bias to action; a distribution architect, sitting at the intersection of community, partnerships, product, and sales.

## A closing thought

As communities scale and become self sustainining societies as a concept (the dream state is to set community on autopilot, reduces any operational overhead for max ROI), how much autonomy and control should you give them? 

Our team is constantly thinking through this problem below:

![Article Image](<https://pbs.twimg.com/media/HCdPdbubwAEkH5z.jpg>)

## The IRL Renaissance Is Already Happening

Cafe Compute. Cursor Coffee. Claude’s “Build” program.

These aren’t stunts. They’re distribution infrastructure.

Online reach is rented. IRL trust compounds.

If you’re building an AI startup and want a defensible GTM layer, start here.

If you’d like to jam on any of this or a copy of our onboarding processes or playbooks for City leads I'd love to chat / happy to send: annie@buildclub.com.au 

---


**作者** 迈克 Mike Chong（@mike_chong_zh）  
**貼文連結** https://x.com/mike_chong_zh/status/2028682635053084759  

**正文**

小团队输给大公司，原因从来只有两个字: 执行和分发。

小团队有想法。大公司有200人去建造它，有销售团队去卖它，有营销预算把它到处推广。小团队跟不上。这个论点存在了30年。30年里，它基本是对的。

现在不对了。

2026年，两件事从根本上改变了。LLM解决了执行差距。推荐算法解决了分发差距。与此同时，大公司困在会议、政治和AI恐惧中。这三件事的叠加，让这个时刻和之前任何时候都完全不同。

数据支持这一点。

根据[Carta的数据](<https://carta.com/data/state-of-private-markets-q2-2025/>)，独立创始人创办的初创公司从2019年的23.7%上升到2025年上半年的36.3%。在美国，年收入超过100万美元的一人公司数量从2021年到2022年几乎翻倍，达到116,803家。这不是偶然。这是结构性变化。

## 一、LLM 解决了执行问题

小团队的真正痛点从来不是想法。每个人都有想法。问题一直是把活干出来。

你是一个人或两个人。你有个很好的产品概念。但要做出来你需要: 前端、后端、移动端、设计、文案、文档、客服、修Bug、QA、营销内容、SEO、邮件推广、数据分析、部署基础设施。这里面每一项在大公司里都是一个全职岗位。

所以你要么融资招人，要么自己苦熬两年，每样事情都做但每样都只有10%的质量。大多数人还没发布产品就烧完了。

LLM在结构层面改变了这件事。不是边缘改进。是核心变革。

我每天都用Claude Code、Cursor和Gemini CLI。我独自开发了 @ScreenKite\_com ，一个免费，原生macOS录屏应用。ScreenCaptureKit集成、、比Screen Studio快4倍的导出速度。五年前，这需要6个人的团队。今天就是我一个人。

不只是代码。我有AI Agent全天候运行公司运营。Agent每天三次扫描Reddit寻找营销线索。Agent检查五个Gmail收件箱并起草客户支持回复。Agent监控Sentry的崩溃报告并将摘要发布到Discord。Agent编写社交内容并在不同产品之间按周轮换。全部跑在定时任务上。不需要人类看着。

![Article Image](<https://pbs.twimg.com/media/HCdTwyDa0AAt8qS.png>)

小团队的执行问题从来不是智力问题。是带宽问题。LLM就是带宽。

[Stripe的2025年度报告](<https://stripe.com/annual-updates/letter>)证实了这个转变是真实的。 2025年的新企业群体增长速度比2024年的快50%。三个月内达到1000万美元年经常性收入(ARR)的公司数量同比翻倍。20%的Stripe Atlas初创公司现在在30天内就向第一个客户收费，而2020年只有8%。创业公司比以往任何时候都更快地发布产品和变现，因为执行不再是瓶颈。

## 二、推荐算法消灭了分发护城河

一直扼杀小团队的第二个因素是分发。你可以做出世界上最好的产品。如果没人看到它，那什么都不算。

大公司用钱解决分发。他们买广告。他们有销售团队打陌生电话。他们赞助会议。小团队什么都没有。你唯一的选择是在Product Hunt上硬磨，然后祈祷有人注意到。

推荐算法彻底改变了游戏。

TikTok不在乎你有一百万粉丝还是零粉丝。算法会先将每个新视频展示给300到500个高度匹配的用户。如果互动好，就继续推。YouTube Shorts、Instagram Reels，甚至Reddit的算法都一样。平台根据质量决定什么被看到，而不是根据花费。一个独立创始人用手机录的30秒产品演示，和一家拥有50万美元营销预算的公司获得10万人观看的机会完全一样。

数字很惊人。TikTok在2025年Q4的中位互动率是[27.6%](<https://www.socialinsider.io/social-media-benchmarks>)。Instagram是9.7%。奖励优质内容的平台和奖励粉丝数量的平台之间差距巨大。小团队赢在前者。

Cal AI的故事证明这不是理论。

Cal AI在2024年5月推出，团队很小。到2024年底，不到20人，他们已经达到[月经常性收入100万美元](<https://www.forbes.com/sites/alexkonrad/2025/03/02/cal-ai-acquired-by-myfitnesspal/>)，下载量超过100万。他们的策略: 12个主题TikTok账号，150个博主，以及专为病毒式传播设计的内容。到2026年初，他们[每月赚200万美元](<https://www.businessinsider.com/cal-ai-myfitnesspal-acquisition-2026-3>)。总下载量: 830万。他们刚被MyFitnessPal以过去12个月超过4000万美元的销售额收购。

一个20人的团队，利用TikTok的推荐算法，建造了一个比拥有200人团队和八位数营销预算的公司更有价值的营养应用。

这不是特例。这是新的打法。

## 三、大公司不会建造了

没有人谈论的部分: 小团队变快的同时，大公司变慢了。

我在微软内部亲眼看到了这个过程。我很早就获得了GitHub Copilot的使用权限。我很兴奋。技术方向很明确。但我的经理，一个从80年代或90年代就在微软工作的人，不让我用自动lint格式化。不是AI。不是Copilot。Lint格式化。世界上最基本的代码质量工具。

这不是个例。这就是文化。

大公司充满了中层管理者，他们的全部工作就是不犯错。他们不因为发布快而升职。他们因为管理人数、完成季度OKR、在组织重构中活下来而升职。激励结构从根本上惩罚冒险。

关于中层管理和AI的数据非常严峻。

[Forbes预测](<https://www.forbes.com/sites/bernardmarr/2024/10/22/why-middle-managers-should-worry-about-ai/>)到2026年, AI可能淘汰50%的中层管理岗位。只有34%的管理者觉得自己有足够准备支持团队采用AI。[31%的员工](<https://www.fastcompany.com/91262614/employees-resist-ai-adoption>)正在积极反对公司的AI计划。[Gallup发现](<https://www.gallup.com/workplace/349484/state-of-the-global-workplace.aspx>)，在实施AI的组织中，只有28%的员工表示他们的经理积极支持团队使用这项技术。

结果是: 管理者成了瓶颈。他们看得到AI威胁他们的价值。一个配备Claude Code的高级工程师可以干三个初级工程师加一个项目经理的活。中层管理者的应对可以预测: 减慢采用速度，要求更多流程，安排更多会议来"评估风险"。

而那些会议? 美国企业每年在低效会议上浪费[370亿美元](<https://hbr.org/2022/03/dear-manager-youre-holding-too-many-meetings>)。71%的高级管理者自己都说会议既低效又无效。员工每月花31小时在什么也完成不了的会议上。

在微软，向Satya汇报的EVP们想让所有人用Copilot。他们建了追踪工程师使用率的仪表板。但EVP和工程师之间坐着几层中层管理，他们未说出口的优先级是自我保护。建造了Copilot的公司让自己的人都用不起来。

与此同时，一个用Claude Code的独立开发者一个下午就能发布一个功能。没有晨会。没有Sprint计划。没有设计评审委员会。没有"我们下个季度再讨论"。

差距每个月都在扩大。

## 三股力量的叠加

每一个变化单独看都很重要。放在一起，它们创造了一个新的公司类别。

执行对等。 一人公司用LLM可以构建、发布和运营一个在2020年需要6到10个人的产品。Stripe的数据显示这些初创公司发布更快、变现更快。

分发民主。 推荐算法给小创作者平等接触大量受众的机会。Cal AI证明了20人的团队可以仅靠TikTok算法就创造超过4000万美元的收入。你不需要市场部。你需要一个好视频。

巨头瘫痪。 大公司被困住了。他们的中层管理害怕AI，回避建造，默认开会和搞政治。在技术奖励速度的时候，他们恰恰在变慢。

## 实际是什么样子

我告诉你我典型的一天是什么样，因为我觉得这比理论更有说服力。

我醒来。Discord上有我的Agent的隔夜更新。三条相关的Reddit帖子被标记了。客服正常。没有紧急的Sentry反馈。一个Ghost\_Writer Agent已经起草了一条社交帖子，我只需点一下就能审核发布。

![Article Image](<https://pbs.twimg.com/media/HCdT7I6agAAEdTL.png>)

我上午写代码。Claude Code处理大部分样板代码。我专注于需要品味判断的设计决策。到中午，我已经发布了一个在传统公司需要一个Sprint才能完成的功能。

从想法到产品发布到用户反应的反馈周期，以小时计算。不是以季度计算。

## 是时候建造了

Marc Andreessen在2020年写了"It's Time to Build"。他关于紧迫性的判断是对的。但2020年的工具仍然需要团队。你仍然需要融资。你仍然需要招人。

2026年，那篇文章应该更短: 去建造。

LLM负责执行。算法负责分发。大公司困在自己的官僚体制里。

Stripe的数据说初创公司变现比以往更快。Cal AI证明了小团队可以打败拥有10倍资源的大公司。五分之一的独立创业者年收入在10万到30万美元之间。77%的独立创业者在第一年就实现盈利。

每一个大公司太慢而无法服务、太政治化而无法优先考虑、或太害怕用AI颠覆的细分市场，现在都向一个愿意建造产品、把它展示给合适的人、然后快速迭代的人开放。

你不需要许可。你不需要融资。你不需要团队。

你需要一个值得解决的问题，一个目标用户聚集的渠道，以及在产品完美之前就发布的意愿。

工具准备好了。市场准备好了。巨头们没有。

去 Build!

---


**作者** Saito（@SaitoWu）  
**貼文連結** https://x.com/SaitoWu/status/2028448023316254786  

**正文**

20VC 这期播客是真敢说！Jerry Murdock，掌管900亿美金的 Insight Partners 联合创始人，在这期节目中讲了很多反常识的观点：

1. Cursor已死？
Jerry说，他投资的一些AI公司，已经认为Cursor过时了。这话从一个管理900亿美金的VC嘴里说出来，是要承担风险的。Cursor什么估值？300亿美金。投资人屁股还没坐热，就被创始人宣告死刑了。
但仔细想想，这很合理。Cursor是给程序员用的AI辅助工具，而autonomous agents是直接替程序员打工的。当你的工具变成了你的员工，谁还care工具好不好用？

2. 所谓的"系统记录"公司，将变成免费数据库
Salesforce、Carta这些所谓的企业级"系统记录"，在AI时代将一文不值。因为自主代理可以直接绕过它们，用更高效的方式完成任务。
通常我们会认为，数据的护城河很深。但问题是：当AI可以直接调用API、当工作流被重塑，那些曾经不可替代的数据入口，可能也就是个数据库而已。

3. NVIDIA的黄昏？
Jerry暗示，NVIDIA的护城河正在被侵蚀。Meta已经敢对黄仁勋说"不了谢谢"，因为他们在押注ASIC芯片——专门为AI模型优化的芯片。
如果未来每个公司都有自己的AI agents，而这些agents需要的是便宜、省电、定制化的芯片，而不是昂贵的高端GPU......NVIDIA的泡沫，可能比想象中更脆弱。

4. 软件公司将被"降维打击"
最颠覆性的观点：未来软件是卖给AI agents的，不是卖给人类的。
想象一下：你给AI agent授权，它自己去买、自己去用、自己给你汇报结果。软件公司要服务的对象变了，那整个商业模式都要推倒重来。
那些还在追求"人效"的SaaS公司，可能还没明白自己的终局是什么。

5. 劳动力市场的"大清洗"
这个预言很黑暗：两年后（也就是下次美国大选），AI导致的失业将成为核心议题。客服、律师、程序员、HR......这些白领工作将首先被替代。
好消息？也许UBI真的会来。坏消息？你可能还没准备好。

6. 投资人的"反直觉"建议
Jerry说，现在是他见过的"最佳入场时机"，因为这是一次真正的"sea change"（海变），比移动互联网还大。
这很反常识。现在市场这么差募资这么难，你跟我说这是最佳时机？但他的逻辑是：正是因为变化足够大，old money那些"老狗"才反应不过来。而新钱，可以没有包袱地拥抱新世界。

这场AI海啸，不是渐进式的。它会是断崖式的。
那些还在用"bolting AI"的传统SaaS公司，会像2000年的dot-com一样批量死亡。而真正的赢家，可能是那些从第一天就为AI原生设计的产品。
至于NVIDIA，我保持谨慎。泡沫也许会继续吹，但最终会回归均值。
最后，提醒各位：money does not come with instructions（钱没有说明书）。这是Jerry说的，我觉得很有道理。

https://podwise.ai/dashboard/episodes/7328651

---


**作者** Frank（@frank_uid）  
**貼文連結** https://x.com/frank_uid/status/2028660626466525406  

**正文**

刚刚翻了一下 @philipkiely 的Inference Engineering，从模型到推理引擎、GPU和系统设计都有涉及到，大部份是llm相关的，少部份是diffusion，很适合扫盲

https://www.baseten.com/inference-engineering/ 

---


**作者** Dan Farrelly | Inngest.com（@djfarrelly）  
**貼文連結** https://x.com/djfarrelly/status/2028558831144362061  

**正文**

Inspired by @openclaw, I wanted to build something that put orchestration at the core of the harness and explored an event-driven approach. Check out project "Utah"

---


**作者** Gergely Orosz（@GergelyOrosz）  
**貼文連結** https://x.com/GergelyOrosz/status/2028568444782698743  

**正文**

"The fastest-growing AI companies already use WorkOS, including OpenAI, Anthropic, xAI, Cursor, Vercel, many more."

One VERY surprising stat: WorkOS is doing all of this with 1x PM, (!!) + ~50 product-minded engineers.

Truly next level in how they build.

Congrats to the team.

---


**作者** Alton Syn（@WorkflowWhisper）  
**貼文連結** https://x.com/WorkflowWhisper/status/2028459078574620920  

**正文**

mark cuban just laid out the exact playbook for making money with AI agents.

pick one vertical. learn the flows. become the AI team they never hired.

he's right. but he left out the how.

i've been doing this for 3 months. here's what it actually looks like:

week 1: i called 12 local businesses and asked one question.

"what's the most annoying part of your day?"

the pool company: "we lose 11 jobs a week because nobody follows up cancellations."
the PT clinic: "insurance verification takes 3 hours every morning."
the cleaning company: "we quote in 2 days. our competitor quotes in 2 hours."

week 2: i built every single one of those workflows.

→ pool company cancellation recovery - 6 min
→ PT clinic insurance verification - 11 min
→ cleaning company instant quote generator - 7 min
→ dog groomer appointment + waitlist manager - 9 min
→ pest control follow-up sequence - 4 min

average build time: 7.4 minutes.
average close rate when you build it live in front of them: 70%.

week 3: $10,750 upfront + $1,200/mo recurring.

zero proposals. zero decks. zero "let me get back to you."

they watched it work. they paid on the spot.

cuban said "you don't need a CS degree or VC money."

he's right. you need one question, one tool, and the willingness to build it in front of them.

i documented the entire framework in a free PDF:

→ the 1-question discovery script (word for word)
→ 6 copy-paste workflow prompts by industry
→ pricing guide (what to charge per workflow type)
→ the live demo script that closes 7 out of 10
→ full MCP setup walkthrough (5 min install)

comment "CUBAN" and i'll send it.

consultants charge $15K for a discovery workshop.

i just gave you the playbook for free.

synta(.)io - describe the workflow in plain english. it builds, deploys, and fixes itself.

(must be following for DM)
mark cuban just laid out the exact playbook for making money with AI agents.

pick one vertical. learn the flows. become the AI team they never hired.

he's right. but he left out the how.

i've been doing this for 3 months. here's what it actually looks like:

week 1: i called 12 local businesses and asked one question.

"what's the most annoying part of your day?"

the pool company: "we lose 11 jobs a week because nobody follows up cancellations."
the PT clinic: "insurance verification takes 3 hours every morning."
the cleaning company: "we quote in 2 days. our competitor quotes in 2 hours."

week 2: i built every single one of those workflows.

→ pool company cancellation recovery - 6 min
→ PT clinic insurance verification - 11 min
→ cleaning company instant quote generator - 7 min
→ dog groomer appointment + waitlist manager - 9 min
→ pest control follow-up sequence - 4 min

average build time: 7.4 minutes.
average close rate when you build it live in front of them: 70%.

week 3: $10,750 upfront + $1,200/mo recurring.

zero proposals. zero decks. zero "let me get back to you."

they watched it work. they paid on the spot.

cuban said "you don't need a CS degree or VC money."

he's right. you need one question, one tool, and the willingness to build it in front of them.

i documented the entire framework in a free PDF:

→ the 1-question discovery script (word for word)
→ 6 copy-paste workflow prompts by industry
→ pricing guide (what to charge per workflow type)
→ the live demo script that closes 7 out of 10
→ full MCP setup walkthrough (5 min install)

comment "CUBAN" and i'll send it.

consultants charge $15K for a discovery workshop.

i just gave you the playbook for free.

synta(.)io - describe the workflow in plain english. it builds, deploys, and fixes itself.

(must be following for DM)
what's in the pdf:

→ 1-question discovery script
→ 6 copy-paste workflow prompts
→ pricing guide by complexity
→ live demo script (closes 7/10)
→ 5-min MCP setup

comment "CUBAN" to grab it.

synta(.)io

---


**作者** Daisy Wolf（@daisydwolf）  
**貼文連結** https://x.com/daisydwolf/status/2028532539854348341  

**正文**

We @a16z could not be more thrilled to lead @tryeasehealth's $41M Series A to redefine healthcare’s operating system, unifying intake (CRM), clinical (EHR), and billing (RCM) into a single, AI-native core platform.

We’ve seen this operating system playbook succeed in other industries with companies like Toast and ServiceTitan. Healthcare – long burdened by fragmented, legacy software – is ready for the same shift.

Ease is starting in behavioral health, and already supports hundreds of providers across inpatient, outpatient (IOP, PHP, MAT), and residential.

The team made this decision easy. CEO @zachcohen25  has been a friend and colleague at a16z for years, and was someone I knew I’d be extremely lucky to back if ever given the opportunity. CTO @therealarrays is an incredible engineering leader with a track record of building and scaling elite technical teams. And President Steve Gold previously built and sold the behavioral health leader Refresh to Optum for one of the largest exits in the space.

We’re proud to partner with Zach, Raymond, and Steve, and to invest alongside @AbstractVC, @BoxGroup, @seedtosunflower, and F3 Partners. 

Check it out: https://easehealth.com

@EvaSteinman @illscience

---


**作者** samika sanghvi（@Sampear_12）  
**貼文連結** https://x.com/Sampear_12/status/2028616168463056942  

**正文**

we’re back 

post-YC we pivoted (more on that soon) and went heads down for a month.

found a problem space we care enough to die solving, finally hit +ve MRR and got absolutely roasted when our server went down for a couple hours 

now we’re walking around SF onboarding people. 

first one was at 8pm with a DJ set,
second one crashed our sandbox server, feels good to be back into fire 

if you’re pivoting and confused, DMs are open, would love to help in any way I can

---


**作者** Tejas Gawande（@tejgw）  
**貼文連結** https://x.com/tejgw/status/2028674354062503985  

**正文**

Cursor for Slides is finally here
Watch the first 47 seconds. Then try going back to your old deck tool

Reply "Chronicle" + RT to get two months of Pro for free. Make sure you follow so I can DM you asap. 
Cursor for Slides is finally here
Watch the first 47 seconds. Then try going back to your old deck tool

Reply "Chronicle" + RT to get two months of Pro for free. Make sure you follow so I can DM you asap. 
You can make slides with Claude. You can make slides with NotebookLM. You can make slides in Gamma.

You can also cut hair with kitchen scissors. Doesn't mean you should.

Muse exists because high-stakes presentations deserve a purpose-built tool, not a side feature. 

Try and see it yourself.
Most AI presentation tools do the same thing: take a prompt, generate 10 generic slides, call it magic. We spent 6 months rebuilding Chronicle around a different idea.

Meet Muse. Your personal slide design agent.

It doesn't start by generating. It starts by listening. It asks what you're presenting, who the audience is, researches your topic, structures the narrative, then designs and iterates with you.

The result? Slides you'd actually put your name on.
What's inside @Chronicle_HQ 2.0:

1/ Full-stack creative partner. Describe what you need. Muse handles research, copy, layout, and iteration.
2/ 200+ templates from teams at Apple, McKinsey, and IDEO.
3/ Notion, Figma, Google Docs embedded directly in your slides.
4/ PPT exports, brand consistency, enterprise security.

Already trusted by teams at OpenAI, Atlassian, HubSpot, and Stanford.

We built this because storytelling shouldn't be gated by PowerPoint skills.
It's live. Try it today.
@Chronicle_HQ Bonus: Reply "Chronicle" to get 2 months of Pro for free. Make sure you follow so I can DM you. Repost to help a small team reach more people.

---


**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2028772619319742875  

**正文**

我现在的工作已经离不开 AI 浏览器了。

去年 Dia、Perplexity Comet Browser、OpenAI 的 Atlas 陆续发布，AI浏览器火了一阵。

但热度很快过去，国内一直没有可用的类似产品。

问题是，浏览器依然是我们在电脑上用得最多的软件，AI 获取上下文最自然的场景就在浏览器里。

你在看什么网页、打开了哪些标签、收藏了什么内容，这些都是天然的上下文。

光年之外团队最近做了个 Tabbit 浏览器（[www.tabbit-ai.com/](<https://www.tabbit-ai.com/>)），算是填补了这个空白。

而且他给浏览器添加了类似 Skills 的能力叫妙招，非常强大。

国内可以直接用，完全免费。

![Article Image](<https://pbs.twimg.com/media/HCehk0taoAE-V1q.jpg>)

简单介绍一下 Tabbit 浏览器：

我知道的国内的第一款从底层重新设计的 AI 浏览器原生 AI 浏览器。

不只是之前搞个前端代码封装卡的要死，基础浏览器功能都做不好那种。

也不是只是 Chrome 加一个浏览器插件。

5 大核心功能：

1. 对话（Chat）- 边浏览边问AI，支持 @网页、@标签组、@收藏夹
1. 妙招（Skills）- 把重复任务变成一键操作，支持变量，支持改变网页内容
1. 智能代理（Agent）- AI 自动完成复杂任务，全程透明
1. 收藏夹（Favorite）- 语义搜索，碎片化收藏
1. 标签管理（Tab Group）- 自动分组，云同步

这 5 个功能加上以后灵活使用的话，你的上下文收集和内容生产效率会高非常非常多。

我最近已经用了一段时间，用五个案例来展示一下这东西有多方便，还有帮你创建妙招的提示词。

## 案例一：从信息爆炸到一键成稿

最近 Anthropic 和美国国防部的事情闹得很大，刚好又跟伊朗的事情有关系。

我就想看看具体是怎么回事，各方的关系是怎么样的。

于是就把所有相关的推特链接和声明文档都打开了而且里面还混杂着各种其他的推特页面。

大概总共有十几个页面。

![Article Image](<https://pbs.twimg.com/media/HCehouVbgAAGQXd.jpg>)

刚好想到 Tabbit 浏览器有自动的浏览器标签整理能力，于是就试了一下。

点击左上角的标签页管理就可以一键整理你的所有标签页。

![Article Image](<https://pbs.twimg.com/media/HCehtdmbwAAMDJw.jpg>)

没想到 Tabbit 真的是根据网页内容进行分组的不是简单的根据网址和渠道，非常智能。

可以看到他把 Anthropic 相关的网址包括推特和官方声明网页放到了一起，其他的推特不在组里。

![Article Image](<https://pbs.twimg.com/media/HCehwmQaoAAjkWb.jpg>)

现在我们有了一个已经分类好的来源之后就可以让 Tabbit 帮我们进行整理了。

Tabbit 的新标签页就是 AI 聊天页面：

- 你在这里可以输入网址直接访问；
- 也可以直接输入问题让 AI 进行回复；
- 当然在输入问题的时候可以将标签页、分组、收藏夹和本地文件作为上下文加入；
- 支持所有国内主流模型，可以随意切换，目前都免费。

![Article Image](<https://pbs.twimg.com/media/HCehzJpaYAACxqQ.jpg>)

我这里直接选择刚才分组分好的 Anthropic 纷争分组，让他帮我整理一下这个事件的时间线以及各方看法。

可以看到，它先是介绍了一下争议的背景，接下来是两个主要的角色立场。

后面还有行业中各个角色的表现，非常的全面，而且因为都有来源也不用担心幻觉。

![Article Image](<https://pbs.twimg.com/media/HCeh2OJakAAmSW5.jpg>)

之后你就可以基于这些让 Tabbit 帮你基于总结的信息和你输入的观点生成可以发布社交媒体的内容了。

非常方便，以前你光整理这些来回粘贴都很麻烦，整理这一套不得半小时。

现在一键分组，一句话生成，3分钟搞定。

发给其他 AI 更是经常出现读不到链接的情况。

Tabbit 基于浏览器原始的数据，所以你能看到的内容他都能读取到。

而且这个方法不止可以用来生成媒体内容：

- 学生写论文：@标签组 整理这些文献的核心观点，按研究方法分类，生成文献综述大纲。
- 白领竞品分析：@标签组 对比这些竞品的功能、定价、用户评价，生成对比报告
- 旅行规划：@标签组 整理这些攻略的推荐景点、美食、住宿，生成3天行程表

通用的提示词描述可以是：@标签组 整理这些网页的\[核心内容\]，按\[维度\]分类，生成\[格式\]

## 案例2：恐飞星人的旅行规划

我最近想要去云南转一转，但是由于我有点恐飞，所以对于飞机的大小有些要求。

加上时间和地点的约束，其实找一些合适的航班也挺费劲的。

刚好 Tabbit 又一个智能代理模式，可以帮你操纵网页获取信息和填写内容。

你可以在聊天侧边栏的输入框或者是新标签页输入框的“智能代理位置”开启。

![Article Image](<https://pbs.twimg.com/media/HCejVNybEAA5Tko.jpg>)

看起来这个事情其实简单，但是操作也很麻烦。

尤其是我这种不常用携程这种网站的人，找到按钮筛选完也得不少时间。

现在只需要语音输入我的需求交给他就不用管了。

可以看到在智能代理启动后，被智能代理控制的网页 Tab 会展示彩色渐变；

网页里面也会有彩色遮罩，你也可以看到他的鼠标位置以及即将进行的操作。

而且这个时候你也可以继续浏览其他网页，不会打断他的操作。

![Article Image](<https://pbs.twimg.com/media/HCejYJ_bcAAiA6a.jpg>)

下达任务之后我就没管他了，然后过会结束之后我回来他已经搞定了航班的筛选。

并且给出了直飞和中转符合要求的航班信息，我只需要判断就行，当然也可以让他帮忙订票。

![Article Image](<https://pbs.twimg.com/media/HCejbzkaUAAsaXr.jpg>)

之后我心想机票都搞定个了，那顺便定个酒店吧。

于是就让他帮我找那天昆明热门景点附近的酒店。

这次他不止会点筛选了，还直接输入了昆明热门景点南屏街附近进行搜索。

![Article Image](<https://pbs.twimg.com/media/HCej0OLawAAUyhh.jpg>)

刚才我们说过了自动整理标签页，但是网页打开和寻找合适的网页还得你自己来。

有了智能代理之后你这一步也可以不管了，比如：

帮我从我的推特收藏页面找到所有 Anthropic 跟美国国防部纷争的推特并打开。

但事实来看这种操作网页的 Agent 由于依赖多模态 LLM，速度还是比你自己操作慢的。

所以你的事情如果着急还是你自己来，然后不太紧急和重要的事情可以让他来。

毕竟即使我们自己做更快，也得消耗时间不是吗，而且有的网页你可能未必有他看的全。

## 案例 3：一次设置，永久复用

上面的旅行规划很好用，但每次都要重新输入一大段指令。

下次去成都、去上海，还得重新说一遍？太麻烦了。

刚好 Tabbit 提供了一种叫妙招的工具，里面有一种智能代理的妙招。

你可以在右上角的灯泡图标找到所有的妙招和创建妙招的入口。

![Article Image](<https://pbs.twimg.com/media/HCej5l6bYAAMEEk.jpg>)

然后在妙招创建这里选择智能代理的分类。

我们完全可以将我刚才的提示词中的时间、地点和飞机酒店的需求保存成变量。

这样后面你再有需求可以不用输入全部的提示词只改动时间和地点就行。

其中我需要打飞机，合适的时间以及 800 以上酒店的这种要求就不需要输入了，非常灵活。

![Article Image](<https://pbs.twimg.com/media/HCek5CnbYAAq5F-.jpg>)

比如上面这里我输入提示词之后，给几个不同的东西设置了变量。

下次在 Chat 里面选择酒店航班机票预订之后，他就会自动开启智能代理模式。

然后你只需要填写需要填写的内容就行，没填写的会回填默认设置。

节省了非常多的时间。

![Article Image](<https://pbs.twimg.com/media/HCelOVUaQAAxL6n.jpg>)

甚至还有更多玩法，比如用这个执行多城市比价：

提示词：
帮我对比从{{出发城市}}到{{目的地1}}、{{目的地2}}、{{目的地3}}的机票价格，
日期是{{日期}}，找出最便宜的选项。

要求：
1. 显示每个目的地的最低价航班
2. 对比总费用（机票+酒店）
3. 生成对比表格

甚至执行往返的行程规划：

提示词：
帮我规划{{出发城市}}到{{目的地}}的往返行程：
- 去程：{{去程日期}}
- 返程：{{返程日期}}
- 机型要求：{{交通工具}}
- 酒店标准：{{酒店星级}}，靠近{{地标位置}}

要求：
1. 找出最优的往返航班组合
2. 推荐住宿天数对应的酒店
3. 计算总费用

写提示词的时候有几个小建议需要注意：

- 变量命名要清晰：使用中文变量名，方便理解
- 默认值要合理：设置最常用的默认值，减少修改
- 定期更新：如果发现某个步骤不准确的话，定期维护和修改

甚至我们刚才案例 2 里面的智能比价、招聘信息筛选、论文检索都能做成妙招。

智能代理妙招 + 变量功能的核心价值在于：

以前： 每次重复输入完整指令 现在： 改几个变量，一键执行

这就是把复杂任务变成可复用模板的能力。

## 案例4：告别收藏即吃灰

我们每个人可能都收藏了很多内容，但是由于懒得整理，基本上都是收藏了就不再用了。

而且想想再找也很难找得到，Tabbit 非常好的解决了这个问题。

你收藏的网页他都会先读取网页内容，然后对网页内容进行标注。

这样你就可以跟 Chat 功能聊天查找你收藏的内容，哪怕你想不起来他具体叫啥了。

而且另外一大突破是 Tabbit 支持收藏图片，图片也会有文本标注。

我发现这玩意简直是设计师神器。

以往我们收藏的设计稿和灵感图片，收藏完全靠自己手动打标签和传统方式进行检索。

时间长了以后根本搜不到自己需要的参考图，而且打标签真的很麻烦。

Tabbit 你只需要在你喜欢的图片里面右键点击收藏此图片就可以。

![Article Image](<https://pbs.twimg.com/media/HCelTAXbcAA79mA.jpg>)

然后你就可以在收藏夹里面找到你收藏的所有图片了，而且 Tabbit 详细的描述了他们的画面信息和内容。

![Article Image](<https://pbs.twimg.com/media/HCelWGjbwAEQAD-.jpg>)

你下次想找的时候完全可以在 Chat 页面跟他说你要找 XXX 图片，他就可以很快帮你找到相关素材。

![Article Image](<https://pbs.twimg.com/media/HCelZWHa8AAZLEm.jpg>)

除了找图片还有更加进阶的玩法，你甚至可以给出需求之后让他一次性帮你找到所有的层面的参考图。

然后基于这些参考图进行设计，比如：

@收藏夹 帮我找出所有深色系、科技感的UI设计稿，
分析它们的共同设计风格，给出配色方案

![Article Image](<https://pbs.twimg.com/media/HCelc_Wa4AAQWTL.jpg>)

可惜的是 Tabbit Chat 模式的模型目前没办法直接读取收藏夹里面收藏的图片本身。

所以生成的设计建议和规范可能跟图片本身的差距有点大。

这个已经反馈给他们了，支持以后我估计就只会用这个收藏我的图片出素材了。

总结一下 Tabbit 收藏功能的优势：

1. 保存整个网页内容，不只是链接（即使网页失效也能看）
1. AI 生成摘要，方便回顾
1. 语义搜索，用自然语言就能找到

## 案例5 ：把浏览器变成你的形状

我们前面提到了 Tabbit 的妙招功能里面的智能代理妙招。

他其实还有两个妙招分类：

一个是提示词，这个大家都很了解了，估计也收藏了很多，我就不介绍了。

第二个是脚本，这个太强大了，你可以按照自己的需求改变网页内容为任何网页增加功能。

只需要在创建妙招的弹窗这里选择“脚本”就可以。

你需要填写一下妙招的名称、介绍，适用的网页以及最核心的脚本代码。

![Article Image](<https://pbs.twimg.com/media/HCelg18bsAAVjGs.jpg>)

这里举个例子，我们在浏览很多网页阅读文章的时候往往有很多问题：

- 公众号文章字太小，看着累
- 广告和推荐内容干扰阅读
- 长文章没有目录，找不到重点

我让他帮我写了一个阅读增强工具，可以一键开启，优化阅读体验：

- 视觉优化：护眼配色、大字体（18px）+ 舒适行距（1.8）、内容居中，最大宽度 800px
- 功能增强：自动生成目录、阅读进度条、回到顶部按钮
- 干扰移除：去除广告和无关元素、移除侧边栏和推荐内容

可以看一下同样的公众号文章，开启前和开启后的对比。

![Article Image](<https://pbs.twimg.com/media/HCelkPubwAAfVy2.jpg>)

另一个常见的需要优化的场景就是视频网站的一些操作痛点，尤其是内容工作者：

- B站倍速只有 0.5x、1x、1.25x、1.5x、2x，想 2.5 倍速没有
- 不能截图保存精彩画面
- 没有画中画功能，不能边看视频边做其他事

我直接让 Tabbit 写了个 视频网站增强 解决这些问题，右侧会有四个按钮：

9个倍速选项：0.5x、0.75x、1x、1.25x、1.5x、1.75x、2x、2.5x、3x

![Article Image](<https://pbs.twimg.com/media/HCeluFYa0AAAI9o.jpg>)

一键开启画中画，视频悬浮在其他窗口上方，可以边看视频边做其他事情

![Article Image](<https://pbs.twimg.com/media/HCelw9aakAAtAE1.jpg>)

视频截图，截取当前视频帧、预览截图、一键下载保存。

![Article Image](<https://pbs.twimg.com/media/HCelzevb0AApcjp.jpg>)

最后还有循环播放按钮，可以开启/关闭视频循环，按钮状态显示当前状态。

除了这两个脚本，你还可以做很多事。

比如把任何网页变成深色主题，一键下载页面中的所有图片，提取页面中的邮箱和电话，自动填充表单，屏蔽广告和弹窗。

不会编程也没关系。用自然语言描述需求，AI 帮你生成脚本。

点击输入框下方的“通过 Chat 生成脚本” Tabbit 就会帮你生成，完事之后你粘贴回来就好。

你也可以在右侧的 Chat 输入框中输入“歸藏”，来获取我生成的这两个脚本。

![Article Image](<https://pbs.twimg.com/media/HCel2FhawAErsuc.jpg>)

如果 Tabbit 内置的模型写得不够好，我也写了一个"脚本编写提示词模板"，让 Gemini 或 Claude 帮你写。

写完粘贴回去就好。

![Article Image](<https://pbs.twimg.com/media/HCel42bbwAA7Rzr.jpg>)

## 结尾

你可能说海外有这么多了，我为什么要用光年之外这个？

他们很多浏览器对国内网站的支持也很差。

微信公众号无法读取，B站无法识别弹幕，而且在国内访问有非常大的限制。

Tabbit 支持多模型切换，对国内网站做了深度适配，数据可以本地存储。

对企业用户来说，这些都是刚需。

改变使用习惯，才能发挥 Tabbit 的价值。

从"我要手动操作"，变成"我告诉 AI 我想要什么"。这需要一个适应过程。

刚开始可能会觉得不习惯，但用一段时间后，你会发现效率提升了很多。

我已经把 Tabbit 当默认浏览器一段时间了。

如果你也觉得每天在浏览器和 AI 工具之间切换很麻烦。

如果你也想让 AI 真正融入工作流，不妨试试 Tabbit。

好嘞，就是今天内容。

如果你觉得对你有帮助，可以帮我点个赞，或者分享给你需要的朋友。

---


**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2028758362612260865  

**正文**

🧵Thread: AI时代，我们教孩子的那套还对吗？

🚨 1/ 不会写代码的金融人，冲进GitHub全球贡献者前30。

40岁保险员，月花1000元AI算力，单条视频号100万曝光。

一个团队几年的推荐算法，被一次大模型调用替代，效果提升30%。

生产方式变了，我们教孩子的方式没变👇 
🧵Thread: AI时代，我们教孩子的那套还对吗？

🚨 1/ 不会写代码的金融人，冲进GitHub全球贡献者前30。

40岁保险员，月花1000元AI算力，单条视频号100万曝光。

一个团队几年的推荐算法，被一次大模型调用替代，效果提升30%。

生产方式变了，我们教孩子的方式没变👇 
⚡️ 2/ 三个"正确的道理"正在失效：

【学海无涯苦作舟】——AI拥有几乎所有系统知识，"你知道什么"贬值了，"你能连接什么"才值钱。

【精确控制=专业】——越控制AI每一步，结果反而越差。给好目标，然后放手。

【先打好基础再动手】——傅盛没看过技术文档，14天靠AI产出7篇爆文。学和做不用再分开。 
🏢 3/ 职场正在筛人。留下来的人有六项能力：

理解AI特性、拆解任务、判断产出质量、让多个AI互相协作检验、展示成果、整合输出加入自己判断。

傅盛14天搭了8个Agent，有汇报关系和检查机制——这不是科幻，是正在发生的事。 
📊 4/ 几乎所有技能的【执行价值】在降，【认知价值】在升。

写作——AI写得比多数人好，但审美判断和结构化思维在升值。
编程——不用会写代码，但要理解系统怎么运转。
画画——"画得像"没价值了，能从10张AI图里挑出最好那张才值钱。
演讲——少数执行和认知价值都在涨的技能。
🎓 5/ 学历的"信号带宽"太低了。

一张文凭传递的信息就是XX大学XX专业。一个GitHub记录、一组黑客松作品、一个博客，信息量比学历高得多。

小学生拿到Claude账号，一天用光额度，写了个《我的世界》插件。初中生没报过编程班，靠AI自学拿了编程大赛第二名。

他们没有学历，但他们有作品。 
🧒 6/ 什么样的孩子在AI时代更有优势？

好奇心强但坐不住、什么都想试但三分钟热度、不听话但有自己的想法。

这些让老师头疼的特质，放在AI时代可能恰恰是优势。ADHD天生多线程、讨厌重复、不喜欢微操——"一年前的bug现在全是feature"。 
🧭 7/ 家长能做四件事：

【给AI账号，别管太多】——傅盛说"不要买课，买Token"。
【给真实项目，别给模拟作业】——帮妈妈做攻略、帮奶奶查药。
【成果公开出来】——能被检索到，就是新时代的能力证明。
【自己先用起来】——你不用AI，光给孩子报班，没用。 
以上就是全部

如果您喜欢这个主题：

1.关注我（@FinanceYF5）
2. 点赞+转发下面第一条帖子

https://x.com/FinanceYF5/status/2028758362612260865

---


**作者** Brad Carry (VC & Podcaster)（@bradcarryvc）  
**貼文連結** https://x.com/bradcarryvc/status/2028571463540719857  

**正文**

I spent $500,000 in Claude tokens to build a simple app that would have taken a junior dev making $120k an entire 6 months to build

This proves that AI will completely replace human engineers this year

---


**作者** Idea Browser（@ideabrowser）  
**貼文連結** https://x.com/ideabrowser/status/2028574660913140169  

**正文**

I've got a billion dollar startup idea for ya

Ad attribution tracking is a total disaster.

Companies spend $1Ts of dollars blindly, not knowing if their ad spend is profitable with a positive ROAS.

Cal AI paid Mr Beast $500k and was asked if it was a profitable ad, he said "probably"

Let's fix that big ole market. 

The idea: 
Build a simulated funnel attribution model with agents. 

You plug in two things. Your business and the channel you want to advertise on. 

You gotta give it all your business data... Your product, your margins, your conversion rates. The creator's audience size, demographics, engagement patterns, historical ad performance.

you press run.

AI agents simulate thousands of synthetic audience members moving through your funnel based on data and industry. They watch the ad. Use the data, act like users. etc. 

When the simulation finishes, you get three numbers.

Low price. "Pay up to $150K and you're almost guaranteed positive ROI."
Medium price. "At $350K you've got a 70% chance of breaking even or better."
High price. "At $500K you're flipping a coin.

After the deal runs, real data gets plugged in and trains your agent instance for your company to prep for the next deal to make the model better. 

You get an output of predicted vs real. 

The model and agents get smarter. 

Wow, you just solved ad attribution. Congrats on your $1,000,000,000 startup.

---


**作者** Verci（@vercinyc）  
**貼文連結** https://x.com/vercinyc/status/2028500602787959154  

**正文**

if you're a student founder trying to break into the startup ecosystem, start here:

• @theresidency → hands-on cofounding + demo environments
 • @zfellows → community of top young builders
 • @fdotinc → hands-on sprint programs in SF
 • @ycombinator Startup School → free + elite curriculum
 • @vercinyc → creative + tech collective in NYC

most people don’t lack ability, they lack access.

comment “resources” for a more in depth list of resources

---


**作者** vas（@vasuman）  
**貼文連結** https://x.com/vasuman/status/2028703836857397597  

**正文**

Remember when AI tools were first released and hardly anyone else was using them? 

Back when there was real alpha in being able to vibe code a landing page, or a demo? 

Now everyone has access to the same thing, and the bar is so much higher.

Now apply this to all forms of employment.

You might be able to “do more today” as an employee, or a founder, but tomorrow it’s the bare minimum.

This has been a 30 second crash course on the permanent underclass.

---


**作者** Robinson · 鲁棒逊（@python_xxt）  
**貼文連結** https://x.com/python_xxt/status/2028692806236328160  

**正文**

一个非常好的知乎回答，推荐阅读

为什么吹的神乎其神的波士顿动力机器人销声匿迹了？

张子昕 ：

人在波士顿红线上，下班了回答一下。这是一个有点长的故事。

谢邀 @蝴蝶先生

首先声明，如果你真心认同"波士顿动力用AI生成的/CG"或者"波士顿动力没有产品"或者"波士顿动力是骗钱公司"，我的判断是开除人籍。建议直接退出这个回答然后去从幼儿园重新读起。

至少在2022年之前，波士顿动力在足式机器人的全身运动控制水平上都是一骑绝尘的。他们的技术护城河是一套能够实时解算 whole-body MPC 的控制框架。搞过轨迹优化的朋友们都知道，求解一个包含20+自由度机器人全身动力学的非线性非凸轨迹优化问题有很多种方法，但是要在几十毫秒内得到一个质量不错的解并且能让机器人动起来就是另一个次元的问题了。这里面包含大量的数学技巧和工程细节，是经过很多年的打磨一点一点积累出来的结果。这一护城河在当时看来是非常难以跨越的。

然后2020年，在风景秀丽的瑞士，一个隶属于苏黎世联邦理工（ETH）的实验室整了个大活。这个实验室就是大名鼎鼎的 Robotic Systems Lab (RSL)。RSL其实一直都非常顶级，可能是当年地球上除了波士顿动力以外唯一有能力写出并且部署 whole-body MPC 的组织，并且在 SLAM 方面也有很多重要的贡献。2020年，他们在 Science Robotics 上发表了一篇影响深远的论文：Learning quadrupedal locomotion over challenging terrain。在那个蛮荒年代，世界上除了波士顿动力以及MIT的 Biomimetic Robotics Lab 以外，还没多少人能把四足的控制器做到能够在野外地形上稳健走路。然后，RSL的老哥们直接把他们自己造的四足机器人拉到了瑞士的山山水水各种地形上遛了十几趟。最颠覆的事情是，他们直接把MPC的桌子掀飞了：咱们一点MPC不用，咱们用强化学习。

从那之后，RSL在强化学习这条道路上直接起飞，发 Science Robotics 如同喝水。他们在仿真和 GPU 并行训练方面的工作直接催生了 Isaac 全家桶的诞生，他们开源的 rsl_rl 框架现在已经成为这个地球上几乎所有人形机器人公司训练控制器的基础，包括波士顿动力自己也是打不过就加入了。可以说，没有RSL的贡献，人形机器人行业的爆发还得再推迟一两年。

在这种情况下，波士顿动力就有点尴尬了，特别是在2022年之后。MPC这块香饽饽突然就不香了，RSL的工作不仅牛逼，而且完全开源，让全世界的人们都享受到了强化学习的力量，而后续 RSL+NVIDIA 的持续发力也是直接把足式机器人的 locomotion 问题差不多完全解决了，whole-body control 也不再是梦，都是基于 rsl_rl 做的。然后宇树也崛起了，充分发挥东大的工业优势，把极其便宜的硬件送进了全世界的实验室里，人手一条 A1/Go1，再到后面人手一个G1，研究进程极速加快。波士顿动力的护城河就这么在很短的时间内被填平了。

所谓的技术壁垒就这么被无情碾碎了，选择的重要性不言而喻。老黄说 NVIDIA 要一直有危机感，这是很对的。

所以到底什么样的技术最后能胜出？能够易于迁移和 scale-up 的技术。满足这两点的技术会随意地把别的技术直接创死。举一个随意的例子，你在一个四足上调好了MPC，但你不能保证一样的算法结构在人形上就好使。你在四足上做好了RL，你的 infra 搞好了，改改 reward function 在人形上很快就能 work。现在的 motion tracking RL reward function 更是简单到令人发指。自由度的增多和机器人结构的变化给MPC带来的麻烦远大于RL。

波士顿动力牛逼吗？曾经牛逼过，人家确实是足式机器人的先驱，2019年在CMU的 FRC High Bay 里坐着看着他们让 Atlas 翻跟头的 demo 感叹不如退学去北极开uber的景象还历历在目。而且他们作的 demo 确实也是激励了很多年轻人走入这个行业。

现在呢？还是强的，毕竟工程底子和公司文化摆在那，机器人除了算法之外，对硬件的理解也是非常重要的一个部分，甚至有时候比算法更重要。

销声匿迹了吗？完全错误，你们千万要注意啊，不要"见着风，是得雨"啊。无中生有的东西，你再帮他说一遍，等于你也有责任吧？

处境艰难吗？难。可能除了特斯拉之外，在美国的机器人公司都面临着生产线搭建和生产成本的严峻问题，你不在中国造成本就是下不来（包括特斯拉自己可能也要在中国制造）。韩国现代在这方面来说是个好的靠山。波士顿动力最先产品化的东西是机器狗 Spot，走的是工厂巡检这个赛道。此外还有 Stretch（不是足式），走的是物流这个赛道。今年 CES 刚刚宣布了新的 E-Atlas 量产型号，似乎势头不错，但到底能干什么仍未可知。

未来如何，谁知道呢。

编辑于 2026-02-27 22:39 美国

---


**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2028756745796116932  

**正文**

🧵Thread: 不懂代码反而是优势

1/ 🧭 一个不写代码的人，靠AI Agent军团冲进龙虾全球贡献者前30，前后全是十年+硅谷工程师。

我跟他聊两小时后慌了——用Claude一整年可能从头用错了。

"我们开着自行车，旁边AI是跑车。结果让跑车跟自行车跑。"👇 
🧵Thread: 不懂代码反而是优势

1/ 🧭 一个不写代码的人，靠AI Agent军团冲进龙虾全球贡献者前30，前后全是十年+硅谷工程师。

我跟他聊两小时后慌了——用Claude一整年可能从头用错了。

"我们开着自行车，旁边AI是跑车。结果让跑车跟自行车跑。"👇 
2/ 🔑 AI使用三层：

【画笔】告诉它每个细节——AI被锁死在你的水平里
【员工】规定每一步——本质还是微操
【大师】"你是这领域前十专家"，给目标给权限然后放手
不懂代码反而是优势——无法微操，被迫放权。 
3/ ⚡ 大师模式三原则：

第一，最终结果导向。不是"修bug"，是"一周进榜前20"，怎么进AI的事。
第二，过程不干预。AlphaGo也走反直觉的棋，最后赢了。
第三，风险可控内给最高权限。假设AI一定搞砸，但搞到最砸你也能接受。 
4/ 🎰 抽卡心态：微操100次得70分，不如放手跑10次抽一次120分。

天润给AI模糊指令做海报："硅谷审美、乔布斯风格。"AI生成泛黄拍立得+古老Mac绿字屏——没有人类设计师会想到。

"把AI规定到workflow里，控制性好了，最大价值可能性也小了。" 
5/ 🤖 他的AI军团：一人经营硅基公司。

Echo（产品经理）、Elon（CTO）、Henry（CMO），各有子Agent。
设定技巧：双层人设——底层"顶级智能"不封上限，表层给具体人格。

说"前十名的人"不是"最好的一个"，能力更全面。

主Agent最强模型决策，子Agent轻量模型执行。 
6/ 🧭 最扎心一段：
"工程师从手写转vibe coding时嘲笑手写派。龙虾出来试一次觉得bug多就放弃——变成了曾经被自己嘲笑的人。"

"火车刚出来大家骑马赛跑嘲笑它慢。一旦提速，骑马的追不上了。"

勇气不是承担风险，是敢打破过去正确的观念——它可能已经不正确了，只是你没意识到。 
以上就是全部

如果您喜欢这个主题：

1.关注我（@FinanceYF5）
2. 点赞+转发下面第一条帖子

https://x.com/FinanceYF5/status/2028756745796116932

---


**作者** Shubham Saboo（@Saboo_Shubham_）  
**貼文連結** https://x.com/Saboo_Shubham_/status/2028328693911912841  

**正文**

This is what a one-person AI Agent run company looks like in 2026.

6 AI agents. 20 cron jobs. 0 human employees.

Every role is a folder. Every job description is a md file. No standups. No Slack. No payroll.

Just a directory on a Mac that runs the whole thing. 
This is what a one-person AI Agent run company looks like in 2026.

6 AI agents. 20 cron jobs. 0 human employees.

Every role is a folder. Every job description is a md file. No standups. No Slack. No payroll.

Just a directory on a Mac that runs the whole thing. 
I have built and open-sourced 100+ AI Agents and RAG implementations (Open-source repo with 99k+ stars):

https://github.com/Shubhamsaboo/awesome-llm-apps

---


**作者** Meer | AI Tools & News（@Meer_AIIT）  
**貼文連結** https://x.com/Meer_AIIT/status/2028625759234052415  

**正文**

something has been sitting in my drafts for three weeks

not because i did not know the topic

because i wanted to make sure i understood it well enough to actually teach it

i read two full technical blogs (link to each blog is mentioned at the end), tested the concepts myself and took notes like i was studying for an exam

today i am finally ready to share it

if you are new here, i write long-form breakdowns on AI concepts that nobody bothers to explain properly

no fluff, no recycled takes, just things i have actually spent time understanding

today that thing is Context Engineering

and by the end of this article you will understand why people building serious AI agents are calling it the most important skill of 2025

let's get into it

# First: What Even is Prompt Engineering?

![Article Image](<https://pbs.twimg.com/media/HCcBVgdasAA3jNM.jpg>)

you have probably heard this term before

prompt engineering is simply the skill of writing better instructions for an AI

think of it like texting a really smart assistant

if you write "do the thing" you get a vague answer

if you write "write me a 3-sentence summary of this article for a 12-year-old" you get exactly what you need

prompt engineering is all about how you word your request to get the best output

it became a big deal when ChatGPT launched because people realized the same AI could give wildly different answers depending on how you asked

it is still useful, it still matters

but here is the thing

prompt engineering is designed for single conversations

one question one answer done

the moment you start building AI agents that work on their own for hours, prompt engineering alone is not enough

that is where Context Engineering comes in

## What is Context Engineering?

![Article Image](<https://pbs.twimg.com/media/HCcB7q_WYAAt2JF.jpg>)

here is the cleanest way i can explain it

 > prompt engineering = how you write one message to an AI 
 > context engineering = how you manage everything the AI knows throughout an entire task

you know how when you talk to a friend about something, they remember what you said five minutes ago and use that to understand what you are saying now?

AI works the same way

but instead of memory, it uses something called a context window

and context engineering is the skill of managing what goes inside that window at every single step

Andrej Karpathy, one of the most respected AI researchers out there, described it perfectly

he called it the "delicate art and science of filling the context window with just the right information for the next step"

every word in that quote matters

delicate: too much and the AI breaks, too little and it has no idea what to do 

art: there is no perfect formula, it takes judgment 

science: there are real strategies and systems behind it 
just the right information: not all information, not no information, the right information
for the next step: not for the whole task, just for what comes next

## The CPU Analogy That Will Make This Click

![Article Image](<https://pbs.twimg.com/media/HCcDU0tXEAAcCRj.jpg>)

you probably know what a computer is

inside every computer there is a CPU, the brain that does all the thinking

but the CPU cannot think about everything at once

it uses something called RAM, a temporary workspace where it holds the stuff it is currently working on

RAM has limited space

so the computer is constantly deciding what to load into RAM and what to leave in storage

now replace "computer" with "AI" in your head

 > LLM = CPU (the brain doing the thinking) Context Window = RAM (the temporary workspace)

the AI can only think about what is currently in its context window

everything outside that window does not exist to it

context engineering is the skill of being the "operating system" that decides what goes into that RAM at each step

this is the Andrej Karpathy analogy and once you get it, everything else about context engineering makes sense

## What is a Context Window?

![Article Image](<https://pbs.twimg.com/media/HCcFHuQXYAAU5cS.jpg>)

simply put: it is the amount of information an AI can hold in its head at one time

imagine you are reading a book

but you can only remember the last 20 pages

anything before page 20 is basically gone for you

the context window is that limit

every message you send, every response the AI gives, every tool result that comes back, all of it eats into that window

modern AI models have gotten bigger context windows but they still have limits

and even when they do not hit the limit, cramming too much stuff in causes its own problems

which brings us to the part most people never talk about

## Why Context Engineering is the #1 Skill Right Now

![Article Image](<https://pbs.twimg.com/media/HCcGSacboAAfEX1.jpg>)

here is what changed in the last two years

people stopped just chatting with AI

they started building AI agents

an AI agent is not just answering a question

it is doing a job

 > it searches the web it reads files it writes code it checks its own work it makes decisions and takes the next step on its own

and it keeps doing this for minutes, sometimes hours

every tool it uses sends a result back into the context window

every step it takes adds more tokens

the context window starts filling up fast

and when it fills up badly, things go wrong

that is exactly why the team at Cognition (the people who built Devin, one of the most talked about AI coding agents) said this publicly:

"context engineering is effectively the number one job of engineers building AI agents"

not prompt engineering

not model selection

not infrastructure

context engineering

if your agent has bad context management, it will fail no matter how good the underlying model is

## What Goes Into a Context Window?

![Article Image](<https://pbs.twimg.com/media/HCcHt-GXIAAPdsF.jpg>)

before we talk about how to manage it, you need to know what is actually inside it

there are three main types of context in most AI applications

Instructions: this is the stuff that tells the AI how to behave system prompts, rules, example behaviors, tool descriptions think of it as the job description you give an employee on their first day

Knowledge: this is the facts and information the AI needs to do the task documents you uploaded, search results it retrieved, memories from previous sessions think of it as the research files sitting on that employee's desk

Tool Feedback: this is the results that come back when the AI uses a tool if it searched Google, the search results come back here if it ran code, the output comes back here think of it as the employee's notes after making a phone call

all three of these compete for space in the same context window

your job as a context engineer is to make sure the right mix is in there at the right time

## Why Long Contexts Fail: The Four Clashes

![Article Image](<https://pbs.twimg.com/media/HCcJd_mWYAEVZ8n.jpg>)

this is the part that most tutorials skip completely

people assume more context = better performance

that is wrong

there are four specific ways that bad context management breaks your AI agent

## Context Poisoning

this happens when the AI makes a mistake and that mistake becomes part of the context

imagine your agent is summarizing research

it hallucinate a fake fact: "the study found that 87% of users preferred X"

that fake fact now lives in the context

every future step the agent takes, it reads that fake fact and treats it as true

one hallucination poisons the whole pipeline

like a bad rumor that spreads through a group chat and suddenly everyone believes it

## Context Distraction

this one is sneaky

it happens when you dump so much information into the context that the AI gets overwhelmed and starts ignoring the important stuff

imagine you ask a friend to help you fix one bug in your code

but you also paste in your entire 500-line codebase, three unrelated error logs and notes from last week

your friend is now distracted trying to process everything instead of focusing on the one bug

the AI is the same

when the context is bloated with stuff that does not matter right now, performance drops

## Context Confusion

this happens when random, irrelevant information quietly steers the AI in the wrong direction

a classic example: ChatGPT once pulled a user's saved location from memory and unexpectedly injected it into an image generation request

the user did not ask for anything location-related

but that piece of context was sitting there and the AI used it anyway

the user felt like the context window "no longer belonged to them"

superfluous context changes the output in ways you never intended

## Context Clash

this is when two pieces of context contradict each other

here is a simple example

your system prompt says "always respond in formal English"

but a document you injected into the context says "this is a casual social media brand with a fun tone"

now the AI has two conflicting instructions and it has to guess which one wins

it will make a decision, probably inconsistently, and your output becomes unpredictable

## 
The Four Strategies That Actually Work

![Article Image](<https://pbs.twimg.com/media/HCcKGa3XoAA0Pda.jpg>)

okay now the good part

engineers building serious AI agents have figured out four core strategies for managing context well

they are: write, select, compress and isolate

let me walk you through each one

## Strategy 1: Write

this means saving information outside the context window so the AI can use it later

Scratchpads

humans take notes when we are working on something big

we do not try to hold everything in our heads at once

AI agents can do the same thing through a scratchpad

a scratchpad is basically a place where the agent can write things down mid-task

"here is what i have figured out so far" "here is my plan for the next five steps" "here is the key detail i need to remember"

this information lives outside the context window

but the agent can pull it back in whenever it needs it

Anthropic's multi-agent researcher actually does this explicitly

when the agent's context window gets close to the 200,000 token limit, it saves its current plan to memory first

that way even if the early context gets cut, the plan survives

Long-Term Memories

scratchpads help within one session

but what about across sessions?

this is where memories come in

tools like ChatGPT, Cursor and Windsurf all have systems that automatically generate long-term memories from your conversations

"this user prefers TypeScript over JavaScript" "this user works on a Mac and uses VS Code"

these memories get injected into future sessions so the agent knows who it is working with

## Strategy 2: Select

writing is about storing information somewhere

selecting is about choosing what to pull back into the context window and when

Choosing the Right Memories

not all memories are useful for every task

if you are debugging a React component, your agent does not need to load in your entire project history

it needs the files relevant to that component

tools use embeddings (a way of representing text mathematically) and knowledge graphs to match memories to the current task

this is still a hard problem and it goes wrong sometimes

but good selection is what separates a smart agent from a confused one

Managing Too Many Tools

here is a problem you probably have not thought about

what happens when your AI agent has access to 50 different tools?

it gets confused about which one to use

the tool descriptions start to overlap and the agent makes wrong choices

one fix: use RAG (Retrieval Augmented Generation) on the tool descriptions themselves

instead of loading all 50 tools every time, you only load the 5 most relevant tools for the current step

research has shown this improves tool selection accuracy by 3x

that is not a small improvement

## Strategy 3: Compress

this is about reducing the size of context without losing the important parts

Summarization

if you have ever used Claude Code you have seen this happen automatically

when the conversation gets too long, Claude Code runs "auto-compact"

it looks at the entire history of what you and the agent have done and compresses it into a shorter summary

"we started by setting up the project structure, then fixed three bugs in the auth module, then refactored the database layer"

that summary is way shorter than the full conversation history but captures what matters

summarization can also happen at specific points in an agent's workflow

after a search tool returns 10 pages of results, you do not need all of that in the context

you summarize it down to the three most relevant facts and move on

here is a real challenge though: some events are too important to compress

if the agent made a crucial decision at step 12, you need to capture that exactly

not a vague summary of it

this is so hard that companies like Cognition have actually fine-tuned smaller AI models just for the job of compressing agent history intelligently

Trimming

sometimes you do not even need to summarize

you can just cut

the simplest form: remove older messages from the conversation history

you do not need to know what the agent said in turn 3 if you are now on turn 47 and none of it is relevant anymore

hard-coded rules like "keep only the last 10 messages" or "remove any search results older than 5 steps" can clean up the context without any AI involvement

## Strategy 4: Isolate

this is the most powerful strategy and also the most misunderstood

isolation means splitting context across separate containers so no single AI has to deal with everything at once

Multi-Agent Architectures (Done Right)

you have probably heard about multi-agent systems

the idea is that instead of one AI doing everything, you have a team of AIs each handling a specific part of the job

each agent gets its own context window focused on its specific task

this actually works well when done correctly

Anthropic's multi-agent researcher showed that multiple agents with isolated focused contexts outperformed a single agent trying to do everything in one context window

BUT here is what most people get wrong about multi-agent systems

and this is something the Cognition team wrote about directly

if your agents are running in parallel without sharing context, you get conflicting decisions

imagine you hire two contractors to renovate your apartment at the same time without letting them talk to each other

contractor A tears down a wall

contractor B was planning to add shelves to that wall

now you have a mess

the same thing happens with AI agents

if agent A and agent B are working on related tasks but cannot see each other's decisions, they will make choices that conflict

the fix: agents need to see the full history of decisions made by other parts of the system, not just their own instructions

Environment Sandboxes

here is a clever trick that some research teams figured out

instead of returning every tool result back to the AI's context window, you can run the tool in a sandbox (a separate isolated environment)

the AI writes code to call the tool

the code runs in the sandbox

only the final result comes back to the AI

this is brilliant for heavy things like images, audio files or massive data tables

instead of loading a 50MB dataset into the context window, the agent just says "run this analysis on the dataset" and gets back a three-line summary

## A Real-World Context Engineering Prompt

okay let me show you what this actually looks like in practice

most people think "context engineering" is just a fancy term for writing a long system prompt

it is not

here is a before and after

Bad version (no context engineering):

Good version (context engineered):

see what happened there?

the second version tells the AI exactly what it needs to know right now

it does not dump everything, it does not leave everything out

it gives the agent the right information for the next step

that is context engineering

## Why This Changes How You Build AI Agents

![Article Image](<https://pbs.twimg.com/media/HCcKz3TagAAXAYt.jpg>)

here is what i want you to walk away understanding

prompt engineering made you better at talking to AI

context engineering makes you better at building systems with AI

the difference is massive

when you are building an agent that runs for 30 minutes and makes 200 decisions, the quality of your context management determines whether that agent succeeds or falls apart at step 50

the engineers who understand this are building agents that actually work in production

the engineers who skip this are constantly debugging mysterious failures wondering why their agent made a random decision on step 23

context engineering is not optional anymore

it is the foundation

## Quick Recap Before You Go

 > Context Window = the AI's working memory, limited in space

 > Context Engineering = the skill of managing what goes in that window at every step of an agent's task

 > The Four Problems = context poisoning, context distraction, context confusion, context clash

 > The Four Strategies = write (save info externally), select (pull in only what's needed), compress (summarize/trim to reduce size), isolate (split context across agents or environments)

 > Why it matters = as AI agents get longer and more complex, bad context management is the single biggest reason they fail

if you found this useful, share it with someone building AI agents

i spent a solid week going through both the LangChain and Cognition research on this before writing a single word

sources used:

1. https://blog.langchain.com/context-engineering-for
agents/

2. https://cognition.ai/blog/dont-build-multi-agents#principles-of-context-engineering

If you want to stay updated with the latest AI news and tools and research paper breakdowns... subscribe to my free newsletter:

## [https://www.theainight.com/](<https://www.theainight.com/>)


---


**作者** Clifton Sellers（@CliftonSellers）  
**貼文連結** https://x.com/CliftonSellers/status/2028502948901241161  

**正文**

I was $40,000 in debt with a family counting on me and a day job that paid just enough to keep me stuck.
No investors. No connections. No trust fund safety net.
Just a laptop and an obsession with one

---


**作者** Grant Lee（@thisisgrantlee）  
**貼文連結** https://x.com/thisisgrantlee/status/2028520621655888139  

**正文**

Companies are making the most expensive mistake of the decade.

They are quietly eliminating entry-level white collar jobs. New grad hiring is drying up. Internship programs are shrinking. Roles like analyst, associate, junior designer, coordinator, are being automated or consolidated. They are telling an entire generation that there's no seat at the table for them, right at the moment when they're most eager to learn and contribute.

In doing so, they are effectively deleting their own future.

The logic is understandable on the surface. AI can handle the tasks that junior employees used to do. Why pay someone to build reports, summarize research, draft emails, or organize data when a tool can do it in seconds?

Every generation of business leaders learned their craft the same way: by doing work that felt beneath them, until it wasn't.

That path is being erased right now, in real time.

Reps build instinct

> "For the things we have to learn before we can do them, we learn by doing them." - Aristotle

Think about how a boxer becomes elite. Thousands of hours of sparring. The footwork, the timing, the ability to read an opponent mid-fight. None of it comes from watching fights. You have to do the reps.

Junior employees are doing the same thing. Every report built, every memo drafted, every deck assembled is a rep. Individually, each one looks low-value. Collectively, they are building a neurological foundation that no shortcut can replicate.

Those "low-value" tasks are the training. This is  how the next generation of leaders learned to think, communicate, problem-solve, and develop judgment. The skills learned at this stage then help with pattern recognition.

## The pipeline problem

When companies eliminate entry-level roles, they are cutting the pipeline.

And the consequences may not show up now, but they will in a few years, when companies realize they have a hollowed-out middle layer. No one who came up through the ranks, or understands the business from the ground up. A generation of senior leaders with no successors who learned the way they did.

> Everyone else will be scrambling to hire senior people who don't exist, because nobody invested in making them.

Institutional knowledge gets created slowly, through years of people learning by doing, absorbing context, and growing into roles that didn't exist when they started. If we automate away the entry point, we break the chain.

## A mistake already made once

A similar thing happened in manufacturing in the 1980s, when automation stripped out apprenticeship programs alongside the manual labor.

The result was a skills gap so severe that companies today cannot find enough qualified tradespeople despite paying premium wages.

That lesson was never absorbed into the white-collar world, and it is being repeated in real time.

By neglecting the younger generation just because there are some new tools that automate work, companies may soon have no one to hire at any level. That’s the real long-term projection.

I understand the pressure. Margins are tight. AI is genuinely capable. The temptation to skip the investment in junior talent is real.

Logically, few companies would want to spend money on junior hires when competitors are cutting them. But someone has to do it. The ones that do will have people who understand the craft, the culture, and the customer because they grew up inside the business. Every expert who companies reach out to hire was once a beginner.

The next generation is the future of every company in every industry. The businesses that treat them that way will be the ones still standing a decade from now. It's time to catch the falling knife.

---


**作者** Tony Kipkemboi（@tonykipkemboi）  
**貼文連結** https://x.com/tonykipkemboi/status/2028564120338063859  

**正文**

When you look at what most agent frameworks actually do, it's workflow orchestration. You define tasks, chain them together, route data between steps, add conditional logic, call external APIs. The core mechanics look familiar because we've been doing this with automation platforms for over a decade.

Agent frameworks emerged in 2023 when models became capable enough to reliably use tools and reason through multi-step tasks. They were built around LLMs and reasoning as first-class primitives. Automation platforms like @zapier and @make\_hq had been built around apps and triggers since the early 2010s. Both solve the same fundamental problem: coordinating work across multiple systems.

For about two years, agent frameworks had a clear opening. Models were good enough to be useful, but the existing automation platforms hadn't adapted yet. Frameworks like LangChain, AutoGen, CrewAI, and others filled that gap with developer-friendly tools for building agentic workflows.

By mid 2025 and into 2026, something happened. The market started closing in from both directions.

From Above: AI Labs

More capable models have been released and products like Claude Desktop ships with Computer Use and multiple connectors. With something like Claude Cowork, you can connect to your data sources, spin up sub-agents for specific tasks, schedule tasks, and orchestrate everything from one command center. It runs on your desktop. The model, the orchestration, and the integrations all come from one place.

OpenAI is building similar capabilities and probably more with the recent acqui-hire of @openclaw founder. So is Google with @GeminiApp. The AI labs aren't just providing models anymore. They're providing the entire agent runtime.

For enterprises, this matters. Most are already paying for these services. They have licenses for their employees to use Claude or OpenAI or Gemini and most instances all of them are provisioned. Why layer in a separate orchestration framework when the lab that built the model also built the agent infrastructure? The integration is tighter. The debugging is easier. The responsibility is clearer. And there's no additional vendor to manage or budget line to justify.

The decision point is becoming harder to justify. Why add another framework to do something the existing tooling already handles? That cost conversation gets difficult fast, especially in enterprises where every new tool needs security review, procurement approval, and ongoing maintenance.

Then came plugins and skills. Claude launched agent skills and plugins that let organizations build and share domain-specific capabilities. Finance plugins. Legal plugins. Productivity plugins. You can add skills for evaluating NDAs, verifying contracts, processing specific workflows. These are shareable across the organization and built directly into the platform employees are already using.

This hit the market hard. The announcement affected valuations for vertical AI companies because, in my opinion, it changed the pricing conversation. Enterprises can now argue they can do most of what specialized tools offer using Claude. That doesn't replace those companies outright, but it compresses what they can charge. Revenue expectations shift when the baseline capability is free with an existing license.

From Below: Automation Platforms

Zapier launched Agents. Make launched AI Agents. @UiPath calls it Agentic Automation. They already had thousands of pre-built connectors, OAuth handling, permission management, and enterprise governance. They just needed to add reasoning on top.

And they did.

These platforms spent over a decade building integration infrastructure. Adding LLM-based reasoning to existing workflow orchestration is straightforward compared to building thousands of enterprise integrations from scratch.

The Vendor Lock-In Question

The strongest case for agent frameworks is model-agnostic flexibility. Build once, swap providers with a config change. No lock-in to a single lab's ecosystem.

Recent events show why this matters. The Pentagon just designated Anthropic a supply chain risk over a dispute about autonomous weapons and surveillance guardrails. The company lost its $200 million contract, and military contractors can no longer use Claude for defense work. The situation is fluid and contained to government contracts for now, but it demonstrates the risk of platform dependence.

What happens when an enterprise decides they can't use a specific lab anymore? Policy disagreements, pricing changes, compliance requirements. If you built everything on Claude or a similar single-vendor platform, you're ripping out infrastructure. If you built on a framework with swappable model providers, you're changing a config file.

That's real value. But it's not the moat frameworks think it is.

OpenAI [launched Frontier](<https://openai.com/index/introducing-openai-frontier/>) in February. An enterprise platform for building and managing AI agents with integrated access to business systems, data warehouses, and internal apps. It's open to agents built outside OpenAI's ecosystem. It has governance, permissions, and compliance tooling.

![Article Image](<https://pbs.twimg.com/media/HCbm2GYXoAIdFCR.jpg>)

It's OpenAI's bid to become "the operating system of the enterprise." And it directly addresses the vendor lock-in concern by positioning itself as a control plane that can work across providers.

Google will build their version. Microsoft already has paths through Azure. You can bet all the big labs are working hard to capture this enterprise market. They're all building platform layers that reduce single-vendor risk while keeping you in their ecosystem.

The competition between labs actually gives enterprises options. Each lab will have different policies, different pricing, different compliance stances. That diversity is its own form of protection against lock-in. And most enterprises would rather manage relationships with two or three major labs than maintain a separate orchestration framework.

Frameworks still have a role for teams that need code-level control or specific orchestration patterns. But the vendor lock-in argument gets weaker when the labs themselves are building multi-provider management platforms. The freedom frameworks offer comes with its own dependencies on integration layers, observability tools, and ecosystem partners.

True portability requires discipline at the architecture level, not just picking the right vendor. And most enterprises will bet on the labs that own the models rather than add another layer to maintain.

The Middle Collapses

Agent frameworks emerged in the gap between when models got good enough to be useful (2023) and when the infrastructure caught up (2025-2026). That gap is closing.

The integration disadvantage that frameworks faced in 2023 and 2024 is gone. Companies like @composio and @TryArcade built integration layers specifically for agents. Most frameworks now use these external tool companies for connections.

But solving integrations doesn't solve the squeeze. AI labs are building down into orchestration. Automation platforms are building up into reasoning. Agent frameworks are in the middle of a compression event from both sides.

Frameworks still have an architectural advantage. They were designed with agents as the default primitive from day one. The developer experience is built for agentic workflows. That matters for prototyping and experimentation.

As the underlying technology improves, architectural advantages compress. Models get better at reasoning and tool use. The abstraction layer matters less. The orchestration patterns start looking similar regardless of where they come from.

There's also a learning curve problem. Agent frameworks are opinionated. You have to learn their language, understand how they structure things, adapt to their patterns. That's friction. Compare that to going to Claude and letting it figure things out. The path of least resistance wins in enterprise adoption.

Who Actually Uses Agent Frameworks?

Fortune 500 companies might experiment with agent frameworks. Some are using them now. But there's a shelf life to that adoption. The cost justification gets harder when AI labs and automation platforms fill the capability gaps.

The companies that stick with agent frameworks long-term are primarily consultancies. Large system integrators and boutique AI consulting firms build on these frameworks to deliver custom solutions faster than building from scratch. They white-label agentic transformation for enterprise clients, maintaining ongoing engagements through customization and integration work.

That's a real market, but it's narrower than the original total addressable market frameworks were pitching. Consultancies are intermediaries, not end customers. And they'll switch frameworks as easily as they switch any other tooling if something better comes along.

Where Frameworks Go From Here

Historically in infrastructure, value concentrates around integration points and operational tooling, not orchestration patterns. Orchestration logic is portable. Integrations are becoming portable too. The moats frameworks thought they had are evaporating.

Agent frameworks had a moment between when models got good enough and when the infrastructure caught up. That window is closing. What's left is open source projects maintained by communities and niche tools for teams that need control over convenience.

Some will pivot to agent management services for consultancies and small shops but most will settle into being developer tools for prototyping before production deployment elsewhere. Both paths are arguably profitable, but neither is the venture-scale platform play frameworks pitched in 2023.

---


**作者** Apoorv Agrawal（@apoorv03）  
**貼文連結** https://x.com/apoorv03/status/2028492786832753011  

**正文**

# The State of Consumer AI. Part 1 - Usage

[Two years ago](<https://apoorv03.com/p/why-meta-and-google-may-win-consumer>), I argued that consumer AI was heading toward a familiar endgame: distribution would trump raw model quality, and hence the incumbents Google and Meta were best positioned to win. Back then, ChatGPT had ~100M weekly active users.

That debate has played out. I was wrong.

Today, AI apps have crossed 1 billion weekly active users and ChatGPT alone accounts for [900M](<https://www.google.com/search?q=openai+900m+users&oq=openai+900m+users&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORigATIHCAEQIRigATIHCAIQIRigATIHCAMQIRifBTIHCAQQIRifBTIHCAUQIRifBTIHCAYQIRifBTIHCAcQIRifBTIHCAgQIRifBTIHCAkQIRifBdIBCDM3MjRqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8>) of that. It built that user base from scratch, without an existing distribution platform. Below I analyze usage data across apps to make the case that ChatGPT is the only AI app with both the installed base and new user momentum to become a core utility, like WhatsApp and Chrome are today. Every other challenger wave has faded. ChatGPT keeps compounding.

This is Part 1 of a 4-part series focused on usage. Engagement, retention, and time spent are next. I analyze usage across four dimensions:

1. ChatGPT pulls away in a two-horse AI race
1. ChatGPT vs. the Consumer giants: closer than you think
1. Four seasons of the year: OpenAI, Google, XAI, China
1. Among AI apps, only ChatGPT looks like a plausible new utility

## 1. ChatGPT pulls away in a two-horse AI race

![Article Image](<https://pbs.twimg.com/media/HCN0WLIaQAArSCM.jpg>)

Methodology note: Source is Sensortower, so this analysis is mobile-only and likely understates web-heavy AI usage. I use weekly active users because it is a useful midpoint between DAU and MAU and a reasonable way to compare emerging AI products against established consumer apps.

Total AI app WAUs have gone from ~100M in January 2024 to over 1.2 billion in February 2026. That is a roughly 20x increase in two years. No app category in history has scaled this fast.

ChatGPT at 900 million WAUs is larger than Spotify at ~600 million, in the same neighborhood as TikTok (~1.5B) and Instagram (~1.3B), and approaching WhatsApp and Chrome (~2.5B each) which I consider essential utilities. When I wrote the original post, ChatGPT was a rounding error next to consumer giants. Now it's in the same league. Most people, myself included, thought this would take much longer. 

![Article Image](<https://pbs.twimg.com/media/HCNpswTbEAEGiIq.jpg>)

ChatGPT commands approximately 70% of total AI WAU. It has held that share consistently for the past year. Gemini accounts for roughly 15-20%. Everyone else (DeepSeek, Grok, Perplexity, Claude, Character AI) combines for ~10%.

The AI category grew 20x, but almost all of that growth accrued to two apps. ChatGPT built its user base from scratch, without an existing distribution platform. Gemini is riding Google's 4-billion user distribution.

## 2. ChatGPT vs. the Consumer giants: closer than you think

To understand where AI apps fit, it helps to look at how consumer apps have stratified over the past decade.

![Article Image](<https://pbs.twimg.com/media/HCNqGJpaUAAIUkW.jpg>)

Consumer app usage has settled into three tiers:

Core Utility (~2-3B WAU): YouTube, Chrome, WhatsApp. These are infrastructure. Apps so embedded in daily life that they function more like operating system features than standalone products. Growth is slow and steady, driven by smartphone penetration rather than viral loops.

Social platforms (~1-1.5B WAU): Facebook, Instagram, TikTok. Habitual-use apps driven by content graphs and social reinforcement. They took years to climb into this tier and growth has largely plateaued.

Niche apps (~300-600M WAU): Spotify, Amazon, X. Category leaders with enormous user bases that serve more specific needs. Usage is frequent but not universal.

AI is no longer just a category to benchmark against itself. It now belongs on the same chart as the biggest consumer products ever built:

![Article Image](<https://pbs.twimg.com/media/HCNqNAKaEAAe9iq.jpg>)

ChatGPT, at 800-900M WAU, cleared the niche tier and is now moving toward the social tier. It did so in roughly three years, a timeline that took Instagram five and TikTok four. Gemini, at roughly 200M WAU, is entering the “Niche” tier from below.

## 3. Four seasons of the year: OpenAI, Google, XAI, China

The WAU chart tells a story of concentration. The download chart tells a story of chaos.

![Article Image](<https://pbs.twimg.com/media/HCNqTmIbEAUlBE-.jpg>)

Over the past year, each season brought a different challenger into the spotlight, each riding a wave of hype, product launches, or distribution muscle. Think of it as four seasons of AI downloads:

Winter 2025: China. DeepSeek exploded past 25 million weekly downloads in January 2025, briefly rivaling ChatGPT's own numbers. The open-source model's performance caught the industry off guard and triggered a wave of "is OpenAI in trouble?" commentary. Within weeks, downloads fell back to a fraction of their peak.

Spring 2025: XAI. Grok rode a surge through Q1 and into Q2, fueled by Elon Musk's distribution via X and a string of model updates. Downloads spiked, press coverage followed. But sustained usage never materialized at the same scale.

Summer 2025: Google. Gemini's biggest moment. Weekly downloads surged above 20 million, driven largely by the nano banana model — Google’s viral image generation release around Google I/O. The spike was almost entirely image-gen related, which also explains the subsequent drop: it was a model moment, not a sustained behavior shift. Google’s distribution engine likely amplified the reach, but the catalyst was having a genuinely good image model that created viral sharing.

Every season: OpenAI. Through all of it, ChatGPT kept compounding. While each challenger grabbed headlines for a quarter, ChatGPT's download numbers remained consistently at or near the top, week after week, with none of the volatility. The steady line on the chart is the one that matters.

Honorable mention: Anthropic. As of this writing, Claude hit #1 free app in the App Store. Whether this becomes another seasonal spike or something more durable is worth watching. But the pattern so far has been clear: attention is easier to capture, daily habits are hard to build.

The pattern is clear. Each quarter produces a new "threat to ChatGPT" narrative. Each one fades. Downloads spike on hype. Usage accrues to the apps that earn daily habits.

## 4. Among AI apps, only ChatGPT looks like a plausible new utility

I think about consumer apps through the lens of stock and flow. Stock is your current user base. Flow is new downloads. Plot both and you get a clear picture of momentum:

![Article Image](<https://pbs.twimg.com/media/HCNriPdbEAAQKKS.jpg>)

This scatter plot captures the end result. ChatGPT occupies a position that, among consumer apps, only the core utility apps (WhatsApp, YouTube, and Chrome) and the dominant social apps (TikTok, Instagram, and Facebook) share. A massive existing user base and high new downloads. Gemini is pulling meaningful downloads but hasn't converted them into a comparable installed base yet. The rest of the AI field is clustered in the bottom-left: small base, modest downloads. Unless something dramatic changes, ChatGPT is the only AI app on a path to a “Core Utility”.

## Conclusion

AI apps have crossed a billion weekly active users. ChatGPT owns 70% of that and is the only AI app operating at true consumer internet scale, reaching 800-900M WAUs in roughly three years without an existing distribution platform.

Google is a real but distant second. Gemini at 200-250M WAUs is the only other AI app that has converted downloads into durable usage, largely by leveraging Android, Search, and 4 billion existing users. No one else is close.

But not all usage is equal. In Part 2, we'll look at engagement, where ChatGPT's lead is even more pronounced across DAU:MAU ratios, retention, and time spent.

In consumer markets, once one product owns both the installed base and the flow of new users, the default outcome is further consolidation. ChatGPT has both. The question now is whether that usage is deepening into genuine habit or still behaving like a utility people visit briefly and leave. That's the real battleground from here.

\* \* \*

Sources used in this post include Sensortower.

The information presented in this newsletter is the opinion of the author and does not necessarily reflect the view of any other person or entity, including Altimeter Capital Management, LP (”Altimeter”). The information provided is believed to be from reliable sources but no liability is accepted for any inaccuracies. This is for information purposes and should not be construed as an investment recommendation. Past performance is no guarantee of future performance. Altimeter is an investment adviser registered with the U.S. Securities and Exchange Commission. Registration does not imply a certain level of skill or training. Altimeter and its clients trade in public securities and have made and/or may make investments in or investment decisions relating to the companies referenced herein. The views expressed herein are those of the author and not of Altimeter or its clients, which reserve the right to make investment decisions or engage in trading activity that would be (or could be construed as) consistent and/or inconsistent with the views expressed herein.

This post and the information presented are intended for informational purposes only. The views expressed herein are the author’s alone and do not constitute an offer to sell, or a recommendation to purchase, or a solicitation of an offer to buy, any security, nor a recommendation for any investment product or service. While certain information contained herein has been obtained from sources believed to be reliable, neither the author nor any of his employers or their affiliates have independently verified this information, and its accuracy and completeness cannot be guaranteed. Accordingly, no representation or warranty, express or implied, is made as to, and no reliance should be placed on, the fairness, accuracy, timeliness or completeness of this information. The author and all employers and their affiliated persons assume no liability for this information and no obligation to update the information or analysis contained herein in the future.

---


**作者** Elvis（@elvissun）  
**貼文連結** https://x.com/elvissun/status/2028671336219107687  

**正文**

zoe was burning 24M+ opus tokens/day monitoring agents that weren't running.

replaced her cron with a 2-layer system:
- bash pre-check, zero tokens when idle
- webhook fires opus only when needed.

~95% token reduction and more reliable output. details below.

(set up a cron to watch this performance, if it works well I'll double down on this event driven stack, seems like the future)
zoe was burning 24M+ opus tokens/day monitoring agents that weren't running.

replaced her cron with a 2-layer system:
- bash pre-check, zero tokens when idle
- webhook fires opus only when needed.

~95% token reduction and more reliable output. details below.

(set up a cron to watch this performance, if it works well I'll double down on this event driven stack, seems like the future)
while we are on this topic I also moved some crons to sonnet 

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2028553427824119842  

**正文**

http://o11.ai embeds AI agents inside G-Workspace and M365 so you can create files in seconds.

Hundreds of companies use their toolset to automate manual work in Microsoft PowerPoint, Excel, and Word along with Google Slides, Sheets, and Docs.

Congrats on the launch, @aryah_oztanir and @ajaymisraaa!

https://www.ycombinator.com/launches/Pa9-o11-the-ai-agent-inside-m365-and-google-workspace

---


**作者** Berkay Secil（@berkay_secil）  
**貼文連結** https://x.com/berkay_secil/status/2028531343819157608  

**正文**

7 days left for Startup Track applications.

Pre-product, pre-launch, or pre-seed? All welcome.
If you have conviction, direction, and are actively building, this is for you.

Don’t wait for perfect. 
7 days left for Startup Track applications.

Pre-product, pre-launch, or pre-seed? All welcome.
If you have conviction, direction, and are actively building, this is for you.

Don’t wait for perfect. 
Apply Now: https://batches.base.org/

---


**作者** Kahlil Lalji（@bykahlil）  
**貼文連結** https://x.com/bykahlil/status/2028523421110513771  

**正文**

Today, @ericjubber is joining @naturalpay's engineering team from Superpower.

When I came out of YC at 23, I spent three months recruiting our first engineer. Not because we lacked candidates, but because the bar was uncompromising: founder mentality, deeply technical, and wired for the 0 to 1 intensity.

That person was Eric.

In 2021, we learned payments the hard way. Back when “documentation” meant flipping through Payments Systems in the U.S. and digging through Stack Overflow threads to piece together how scalable systems actually moved money.

Five years later, Eric is rejoining us, this time at Natural. Building a team that is both technically excellent, and that you trust implicitly, is always the top priority of any founder. I have that in Eric.

Agentic payments is about to evolve very fast this year. We opened up nine new roles in the last week alone.

If you want to build at the edge and think you can keep up, reach out.

https://www.natural.co/blog/why-eric-joined-natural

---


**作者** Mike Kelly（@NicerInPerson）  
**貼文連結** https://x.com/NicerInPerson/status/2028484809245212954  

**正文**

I built a self-developing AI system. Agents that will build new agents, skills, and tools whenever needed. It updates itself whilst in flight. Here it is working on itself after I told it: "I want to be able to send you voice notes". This is becoming feasible with today's models. 

---


**作者** Shann³（@shannholmberg）  
**貼文連結** https://x.com/shannholmberg/status/2028417727661318425  

**正文**

I built a 4-agent system that writes X content.

I give it a topic. It searches X for relevant tweets, stores the research, generates ideas with different hook angles, writes a draft in my voice, and pushes it to Typefully.

The pipeline:

> Research: pulls tweets and stores them in a database
> Ideate: generates structured ideas with hook formulas and key points
> Write: applies voice guide + copywriting frameworks, matches my tone
> Orchestrate: routes the request through each stage

Each agent has its own memory that persists across sessions. The Writer remembers what feedback I gave on past drafts. The Researcher remembers which accounts I like studying.

Built the whole thing with Claude Code. Just markdown prompts, a database, and CLI tools.

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2028599757820613086  

**正文**

Jenny Wen 是 Anthropic 的 Claude 设计负责人，目前主导 Claude Co-work 的设计工作。加入 Anthropic 之前，她是 Figma 的设计总监，主导了 FigJam 和 Slides 两个产品从概念到发布的全过程。更早之前在 Dropbox、Square 和 Shopify 做设计。

这期 Lenny's Podcast 聊了五件大事：传统设计流程为什么走到了尽头、在 AI 实验室做设计是什么感受、AI 会不会取代人类的品味和判断力、Co-work 是怎么做出来的、以及现在招什么样的设计师。

![Article Image](<https://pbs.twimg.com/media/HCcIUEDWMAESMP2.jpg>)

来源：Lenny's Podcast，2026 年 3 月 1 日
原始视频：[https://www.youtube.com/watch?v=eh8bcBIAAFo](<https://www.youtube.com/watch?v=eh8bcBIAAFo>)

## 要点速览

- 传统设计流程“死亡”：发散 - 收敛 - 发散 - 收敛的经典流程被工程速度倒逼，设计师做设计稿的时间从 60-70% 压缩到 30-40%，多出来的时间用于和工程师配对、甚至自己写代码
- 愿景规划大幅缩短：时间窗口从 2-5 年缩到 3-6 个月，形式从精美的演示文稿变成能指方向的原型
- 人类价值在于决策和责任：AI 在品味和判断上会越来越好，但构建软件最难的部分不是构建本身
- Co-work 的真实故事：“10 天”开发其实是长期探索后的最后冲刺，品牌信任不靠完美发布，靠快速响应反馈
- 三种最值得招的设计师：方块型强通才、深 T 型专家、有匠心的应届生，第三种最被忽视但在变革期最有价值

## 设计流程已死，不是自己死的，是被工程速度“逼死”的

Lenny 开场第一个问题：AI 时代，设计流程怎么变了？

Jenny 的回答很直接：

> 设计师们被教导的那套设计流程，我们曾经把它当圣经一样遵循，现在基本已经死了。
> （“This design process that designers have been taught—we sort of treat it as gospel—that's basically dead.”）

她指的是经典的双钻石模型，先做调研和发散，再收敛，再发散，再收敛。

![Article Image](<https://pbs.twimg.com/media/HCcIWOoXAAAAesw.jpg>)

这套方法论在 AI 之前就已经有点撑不住了，但当工程师可以同时开 7 个 Claude 实例去造功能时，设计师就彻底没法用老流程来工作了。

![Article Image](<https://pbs.twimg.com/media/HCcIYIBbAAARTpI.jpg>)

Jenny 2025 年 9 月在柏林的 Hatch Conference 做了一场叫“Don't Trust the Design Process”（别信设计流程）的演讲，引发了巨大反响。但那场演讲才过了三四个月，她自己就觉得内容过时了。尤其是 Opus 4.6 发布、大量人在假期期间发现了 Claude Code 之后，设计流程的变化比她预期的还要快。

她把现在的设计工作分成两类。第一类是支持执行，工程师在高速出活，任何人都可以提一个想法然后让工程师（或 AI）做一个粗糙版本出来试试，设计师更多是顾问角色，而不是先画设计稿再交付。第二类是做愿景和方向，但形态也变了：过去可以做 2 年甚至 10 年的设计愿景，做出精美的故事化演示文稿；现在的愿景通常只能看到 3-6 个月后，形式有时候就是一个能指方向的原型。

> 你最好别挡着他们，让他们放手干。
> （“You're better off not blocking that, letting them cook.”）

Lenny 追问：这种变化是所有公司都在经历，还是只有 AI 实验室才这样？

Jenny 说，她柏林演讲的反响之强烈超出预期。产品经理在用 Claude Code 做原型，设计师在用 v0 做开发。但也有不少反对声音：有些设计师在这套流程上投入了整个职业生涯，他们不愿意接受“我们可以不做调研发现”这种说法。

关于“快速发布还是精心打磨”，Jenny 认为要看具体情况。但 AI 产品有一个根本性的理由让快速迭代格外重要：AI 模型是非确定性的，你无法在设计稿里模拟所有状态，甚至做不出有意义的可点击原型。你必须用真实模型、看真实用户怎么用，才能发现真正的使用场景。

【注：Non-deterministic 指同样的输入可能产生不同的输出。传统的“画好所有界面状态”的方法在 AI 产品中失效了，因为 AI 的回应本身不可预测。】

## 在 Anthropic 做设计师的一天

Lenny 问了一个很直观的问题：在 AI 实验室做设计，日常到底在干什么？

Jenny 说她花相当多时间在“跟上节奏”上。Anthropic 内部任何时候都有很多团队在做原型、试验新想法，各种代号项目在推进。

> 我们的 Slack 是一座金矿。
> （“Our Slack is a gold mine.”）

从模型能力进展到行业走向的内部辩论，她都想跟上。这些信息对她的工作直接有用：她需要预判下一步可能出现什么，才能提前为设计做准备。

除了信息跟进，Jenny 的日常大致是这样的：一部分时间留给传统的设计思考；大量时间用于和工程师一起碰撞，对话、白板、看他们做出来的东西、给反馈；还有一部分时间直接在代码里做打磨。

关于时间分配的变化，她给出了清晰的数字对比：

- 几年前：60-70% 做设计稿和原型，20% 和工程师配合，10% 开协调会
- 现在：30-40% 做设计稿和原型，30-40% 和工程师直接配合，还多了一块——自己写代码实现

XIMGPH\_4

![Article Image](<https://pbs.twimg.com/media/HCcIaE9XwAEER0Y.jpg>)

和工程师合作时，她的重点是解释“为什么”。不是说“按钮不该放这里”，而是说“我觉得应该有个按钮，因为用户研究显示不是所有人都知道可以用提示词触发这个功能”。她也会尽量引导工程师用设计系统里现成的组件，因为 Claude 写代码时并不总是会自动使用设计系统。

她的 AI 工具栈：Claude Chat 已经基本被 Claude Co-work 取代了，因为她的使用场景大多是长时间运行的任务。Claude Code 主要在 VS Code 里用，做前端打磨时需要同时看代码和跟 Claude 对话。一个她觉得特别好玩的工作方式：有人在 Slack 里说“这个图标偏了”，@ 一下 Claude，Claude 自动改好代码并提交，她直接合并就完成了。

【注：Claude Co-work 是 Anthropic 于 2026 年 1 月推出的桌面端 AI 智能体产品，可以操作用户电脑上的文件，完成文档生成、数据整理等非编码类知识工作。】

## Figma 还有用吗

鉴于 Jenny 的 Figma 背景，Lenny 直接问了这个很多人关心的问题。

Jenny 说在用，而且认为 Figma 仍然重要，但原因跟以前不太一样了。

代码工具的问题是太线性了。你用 Claude Code 做一个方向，就会一直在那个方向上迭代深入。但好的设计需要先想 8-10 种不同做法，把一堆想法甩到墙上，然后筛选和推动自己探索更多可能性。这种发散式的探索，Figma 的画布仍然做得最好。

另一个价值是精细的视觉微调。不同的排版、字体、样式方向，放在画布上并排比较，比在代码里反复切换高效得多。

XIMGPH\_5

![Article Image](<https://pbs.twimg.com/media/HCcIcBLXsAAH27U.jpg>)

Lenny 观察到一个有趣的现象：在工程领域，IDE 正在被命令行和 Agent 取代，工程师觉得 IDE“不酷了”。但对设计师来说，IDE 反而变成了有用的工具，因为有时候直接改一个 CSS 样式比跟 Claude 描述快多了。也许 IDE 正在变成设计师和产品经理的工具，而工程师已经往前走了。

## 构建软件最难的部分，不是构建它

Lenny 引用 Lex Fridman 的说法问 Jenny：当 AI 越来越聪明，人类大脑在哪里还有价值？

他提到 Claude Code 负责人 Boris Cherny 最近在节目上说的话：Claude Code 已经不只是写代码了，它开始帮他想点子、决定该做什么。这让 Lenny 重新审视了“AI 永远不会像好的产品经理和设计师一样做判断”这种假设。

【注：Boris Cherny 是 Claude Code 的创建者和负责人，在 2026 年 2 月的 Lenny's Podcast 中表示“编码这件事基本已经被解决了”，Claude Code 现在开始扫描反馈、缺陷报告和遥测数据来主动提出改进建议。】

Jenny 认为 AI 在品味和判断上会越来越好，“我们可能在这一点上执念过深了”。但她指出了一个更根本的问题：

> 构建软件最难的部分，其实不是构建它本身。
> （“A lot of the hard parts of building software are actually, like, not building it.”）

回想你工作中最难的时刻，往往不是技术实现，而是你和另一个人在争论”这个功能到底该不该做””该做成什么样”。这种人与人之间的决策分歧，AI 可以提供参考意见，但不能替你解决。

XIMGPH\_6

![Article Image](<https://pbs.twimg.com/media/HCcId8DWIAAJ5io.jpg>)

就像 Claude 现在可以帮工程师写代码，但工程师仍然要为“这段代码对不对”“放在产品里合不合适”负责。设计和产品决策也一样，决策和责任仍然落在人身上。

Lenny 用放射科的类比补充：AI 可能比放射科医生更擅长诊断，但你还是需要一个人签字，因为得有人在出错时承担责任。

Jenny 也承认，我们可能低估了 AI 在这些方面变好的速度。

## 聊天还是图形界面

Lenny 说没人想到聊天机器人和终端会成为 AI 的持久界面，但它们不仅没有消失，反而越走越远了。

Jenny 认为未来会是两者结合：可点击的图形界面加对话。Claude 最近发布了一系列小组件（天气、股票、多选题等），用户反响很好，因为人们仍然喜欢看到 UI、点击它们、和它们互动，这比打字高效得多。

但聊天这个范式打开了一扇巨大的门，它让你有无限多种方式来和计算机交流。所以聊天不会消失，但对于特定任务，UI 仍然更直接。未来的趋势可能是：越来越多的 UI 由模型动态生成，而不是工程师逐个手写。

XIMGPH\_7

![Article Image](<https://pbs.twimg.com/media/HCcIf8IWQAAXR1k.jpg>)

Lenny 提到 Kevin Weil 的一个观点：语言是一种跨越所有智能水平的界面，你可以和 IQ 200 的人聊天，也可以和不那么聪明的人聊天，语言都适用。所以随着模型越来越聪明，对话仍然有效。

【注：Kevin Weil 是 OpenAI 的首席产品官，此前在 Instagram 和 Twitter 担任高管。】

## 从总监回到 IC：这一年教会我什么

Jenny 在 Figma 管过 12-15 人的设计团队加上几个设计经理，是正儿八经的设计总监。但她去 Anthropic 的时候选择了做 IC（Individual Contributor，个人贡献者）。

![Article Image](<https://pbs.twimg.com/media/HCcIiB-boAAA_Ck.jpg>)

她一方面是想在 AI 时代亲手感受工具和流程的变化。另一方面，她对中层管理的未来有真实的焦虑，在 AI 改变工作方式的背景下，管理角色是不是会持续存在？

在 Anthropic 的这一年（先做 IC，中间短暂管了几个月团队，又回到 IC），她觉得收获巨大。设计流程在过去一年变化太快，如果她一直在做纯管理，根本不会有时间去习得这些新硬技能。如果将来再管团队，这段经历会让她真正理解团队面临的挑战，而不是隔靴搔痒。

她建议设计管理者也应该做类似工程管理者的"实操轮岗"，先花几个月做 IC 理解技术变化，再回去管团队。

Lenny 问她回归 IC 后最不适应什么。Jenny 笑着说：接受批评。作为设计师要在团队面前展示工作、接收批评性反馈，这是一个相当脆弱的过程，而管理岗待久了会生疏。

关于管理的未来，Jenny 认为只要有团队就需要管理者。但未来的管理者需要同时能给团队方向和做一部分 IC 工作，纯粹的“人员管理”作为独立角色可能不够了。

## Co-work 背后的真实故事

Boris Cherny 在 Lenny 的节目上说 Co-work 是 10 天做出来的，这个数字在网上传得很广。Lenny 问 Jenny 实际情况是什么。

Jenny 纠正了这个印象：10 天是从内部版本到外部发布的冲刺时间。在此之前，团队在不同的 Agent 框架上做过大量原型和探索，待办列表怎么展示、多选问题用什么形式、怎么教用户理解使用场景，都试过很多种方案。

XIMGPH\_9

![Article Image](<https://pbs.twimg.com/media/HCcIj7MXwAA32iR.jpg>)

> 这个想法一直在反复出现，然后突然之间，时机到了，感觉就像一直都这么显而易见一样。但走到那一步的旅程很长很长。（“The idea kept coming back, and then all of a sudden, it's the right moment, and it feels like it was so obvious all along. But there was a long, long journey to get there.”）

关于发布策略，Jenny 说 Co-work 发布时并不完美，但团队在内部用了很多，确信有真实价值，值得让外部用户也体验到。关键在于发布之后要兑现承诺。

> 真正损害品牌的，是发布了早期版本后什么都不做。
> （“The way that you really lose trust around quality... is if you release it early and then nothing ever happens.”）

Lenny 把这种理念概括为"通过速度建立信任“（building trust through speed）。Jenny 补充说不只是速度，还有让用户觉得”我的反馈被听到了、被用上了"。Anthropic 每次发布新版本后，团队成员在 Twitter 上回复用户反馈，快速修复问题，公开展示进展。

Lenny 问她最骄傲 Co-work 的什么。Jenny 说最骄傲的是他们把它发了。因为做设计的人看自己的作品，永远只看到缺陷。

Lenny 问 Co-work 该怎么用一句话描述。他自己的说法是“Claude with hands”（长了手的 Claude）。Jenny 说她喜欢这个，但她自己的描述更接地气：Co-work 擅长的是你把一堆乱七八糟的东西扔给它，它帮你变出一个整齐有用的结果。

她当前的迭代方向：

- 让 Co-work 的首页更像一个你和 Claude 之间的共享任务列表
- 思考 Co-work 是不是永远只活在屏幕上，它能不能延伸到其他工作界面

## 三种最想招的设计师

Lenny 问在一切都在变的时代，招设计师看什么。

Jenny 说首先要有韧性和适应性，愿意试新方法、学新工具，不能抱着老流程不放。

更具体地说，她现在最感兴趣的是三种人：

第一种：方块型强通才。 不是那种什么都沾点但都不深的人，而是在多个维度上都达到了 80 分位水平的人。传统的 T 型人才是一深多浅，方块型是好几个方向都深。这种人在角色边界模糊的时代特别有价值，设计师的工作正在往产品经理和工程师的方向延伸。Jenny 也承认这种人很稀有。

第二种：深 T 型专家。 T 的竖杠比绝大多数人长得多，在某个领域排到行业前 10%。可能是技术极强、基本等于半个工程师的设计师，也可能是视觉设计或图标设计的顶尖高手。在所有人都能用 AI 做出“还行”的东西时，深度专长才能做出差异化。

第三种：有匠心的应届生。 早期职业阶段，但成熟度超过年龄，学东西快，没有固化的流程思维。大多数公司都在抢资深人才，但恰恰因为规则在变，一个白纸状态的快速学习者可能比满脑子旧流程的资深人更有优势。

![Article Image](<https://pbs.twimg.com/media/HCcIl2oXgAAKOv_.jpg>)

给年轻设计师的建议：多做东西，别被“经验少”限制住。Jenny 提到了母校滑铁卢大学的 Socratica 社区，一个学生造物者社区，每周线下共同工作，做项目然后展示。有人造了 Claude 驱动的机器人，有人往波士顿的公交车上贴了卡通眼睛。这种“我就是要做点什么”的行动力，是让人脱颖而出的东西。

【注：Socratica 是 2022 年在滑铁卢大学创立的学生社区，现已扩展到全球 30 多个城市。】

关于“设计师要不要学代码”，Jenny 的建议务实：不需要从零学 React，但要把 AI 编码工具纳入自己的工具箱。随着模型和产品变好，抽象层会继续上移，设计师不需要理解每一行代码怎么运行。

Lenny 问了一个尖锐的问题：Claude 作为设计师有多好？你会雇它吗？

Jenny 很直接：现在还不够格。Claude 不符合她提到的三种原型中的任何一种，它做初稿和展示不同方案还行，但没有什么让你觉得“这个很特别、值得雇佣”的东西。不过她也说，过去一年 Claude 在这方面进步了很多。

## 管理者的反直觉智慧

访谈后半段转向了团队管理。Jenny 分享了几个有意思的观点。

## 低杠杆时间

管理培训会教你用 2x2 矩阵分类工作，“只有我能做的”和“别人也能做的”，然后把“低杠杆”的事都砍掉。但 Jenny 观察到，她最尊敬的领导者往往会主动选择做一些“低杠杆”的事情，而正因为是他们在做，这些事反而变成了高杠杆。

比如高管自己花大量时间测试产品、复现问题、跟工程师一起看日志抠细节。领导亲自做会建立对产品的深度熟悉感，也给团队传递了"没有什么事是掉价的"这个信号。Mike Krieger 亲自提交代码就是一个例子。再比如有领导亲手给员工做一张精心设计的纪念卡，行政可以做这件事，但领导自己做传递的信息完全不同。

【注：Mike Krieger 是 Instagram 联合创始人，2024 年加入 Anthropic 担任首席产品官，2026 年初转入 Anthropic Labs 团队。】

## 互相吐槽的文化

当团队成员愿意互相开玩笑，甚至敢拿管理者开玩笑时，说明他们不怕你、信任你。Jenny 之前团队的人会模仿她在设计评审会上的口头禅“OK，下一步是什么？”，这说明他们了解她、不怕她。

但这必须和高标准并存。她用“严厉的父母”来比喻：团队知道你不会随意开除他们，但也知道你要求最好的工作。有了心理安全感作为基础，提出高标准反而变得更容易。Lenny 把这总结为极度坦诚（Radical Candor）的经典公式：深深关心加直接挑战。

## 可读性矩阵

第三个话题来自 Evan Tana 的“可读性矩阵”（Legibility Framework）。矩阵的两个轴是：创始人是否“可读”（别人一看就懂），想法是否“可读”。如果创始人和想法都高度可读，那这个机会大概率已经有人在做了。最有价值的往往是“想法不可读”的象限，别人看不懂、但有能量在汇聚的方向。

【注：Evan Tana 是 SPC（South Park Commons，硅谷创业社区和基金）的合伙人。】

![Article Image](<https://pbs.twimg.com/media/HCcInzuaAAAYvkO.jpg>)

Jenny 把这个框架用在了日常工作中：她在 Anthropic 的 Slack 里浏览各种内部原型时，就是在找那些“不可读”但有能量的东西。

一个具体案例。去年 Anthropic 内部有人做了一个叫“Claude Studio”的原型，界面非常密集和复杂，建在某种 Agent 框架上。Jenny 第一眼看到时觉得“我不知道这是什么”。但她注意到研究团队和内部用户对它非常兴奋。她没有忽略这个信号，而是选择深入了解。最终，那个原型里的核心概念，比如 Skills 框架（用 Markdown 文件指导 Claude 如何完成特定任务），以及展示 Claude 的计划和待办事项的 UI，都被提取出来放进了 Co-work 的设计中。

Lenny 补充了一个相关的发现：他和风投人 Terrence Rohan 的研究显示，那些很早加入后来成为巨大成功的公司（如 Palantir、Stripe、Linear、OpenAI）的人，看到了三个信号：想法听起来疯狂、有一些人对它极度兴奋、创始人是前 1% 的人才。

Jenny 说这和她的体验一致：当你看到一个你不理解但有人在兴奋地投入的东西时，值得深入了解。早期的创造者往往说不清楚自己为什么兴奋，需要有人帮他们把模糊的能量转化为清晰的产品。

## 闪电问答

推荐书籍：《The Power Broker》（Robert Caro 著，讲 Robert Moses 的一生），1100 页。Jenny 说在注意力稀缺的时代读一本跨越数十年的传记特别有价值。另一本是《Insomniac City》（Bill Hayes 著），关于科学家 Oliver Sacks 生命最后时光的回忆录。

最近喜欢的电影：《A Sentimental Value》，挪威导演 Joachim Trier 的新片（他也导了《世界上最糟糕的人》），讲一个家庭与他们住了一辈子的房子之间的关系。还有 The Pit 第二季，看能力极强的人做自己擅长的事，就是好看。

最爱产品： Retro，一个小圈子照片分享 App，只能分享当周的照片，没有社交媒体那套计数和广告。用了两年后可以回看“两年前这一周我在做什么”，变成了一种记录生活的方式。

人生座右铭： “It is what it is.”听起来像认命，但 Jenny 说在一切都在变的世界里，这句话能给你需要的轻松感来继续前行。

Co-work 最酷用法： Jenny 把自己多年的笔记（一对一记录、随想、小备忘录、面试笔记）全部丢给 Co-work，让它分析出她评估设计手艺时看重什么。输出是一份她自己都没意识到的评估标准。当 AI 能帮你发现自己隐含的思维模式时，这件事本身就很有价值。

Jenny 整期播客的核心线索只有一条：变化不是从设计界内部发起的，而是工程效率的暴增把设计师推到了必须改变的位置上。设计师需要从流程的门卡变成引导者，从画设计稿的人变成能在代码里做打磨的人。

一个值得关注的信号是 Jenny 提到 Co-work 的下一步：“它是不是永远只活在屏幕上”。这暗示 Anthropic 可能在探索让 AI 智能体触达更多工作界面的方式，而不是把所有交互都塞在一个聊天窗口里。

另一个未解的问题是 AI 在品味和判断上的进化速度。Jenny 承认 Claude 目前不够格被当作设计师雇佣，但她也说“过去一年进步了很多”。这个差距在缩小，没人知道缩小到什么程度就会触发行业的又一次变化。

Anthropic 设计团队正在招人。如果“设计流程已死”这件事让你感到兴奋而不是恐惧，Jenny 说 welcome。

完整访谈视频：[https://www.youtube.com/watch?v=eh8bcBIAAFo](<https://www.youtube.com/watch?v=eh8bcBIAAFo>)

---


**作者** Syed Ijlal Hussain（@sijlalhussain）  
**貼文連結** https://x.com/sijlalhussain/status/2028532047518593027  

**正文**

📍 AI is not creating roles.
It is redistributing organizational power.

As Gartner highlights the proliferation of AI-specific titles across management, business, and technical layers, the implication is structural reallocation of authority, not hiring expansion.

1️⃣ Competitive Shift
AI leadership roles formalize decision rights around data, automation, and model governance at the executive level.

2️⃣ Structural Blind Spot
Many firms treat AI hires as additive specialists while leaving reporting lines, incentives, and budget control unchanged.

3️⃣ Strategic Risk
If AI authority remains fragmented across silos, the organization builds capability without consolidating control, slowing value capture.

This is not about job titles.
It is about who owns decision power in an AI-native enterprise.

Are you adding AI roles, or redesigning your power structure around them?

Credit: https://www.gartner.com/ and Bot Nirvana

@corixpartners @Transform_Sec @Corix_JC @ILoveBooks786 @COSTESLionelEr @ramonvidall @RLDI_Lamy @FrRonconi @timo_vi @Nicochan33 @NathaliaLeHen @TCyberCast @arigatou163 @ricardo_ik_ahau @VivMilanoFSL @xavierquerat @WillyRayNick @StrategyNDigita @quepasachico @bulbi59 @BulbiT3ch @bbailey39 @sulefati7 @BCAgroup @negimagurott @CRudinschi

---


**作者** Larsen Cundric（@larsencc）  
**貼文連結** https://x.com/larsencc/status/2028554526639460600  

**正文**

Published this article about our agent sandbox infrastructure a few days ago.

It's already ranking top 3 on Google for "how to sandbox an agent" and Google's AI Overview is referencing our control plane architecture.

Note to self: Write about what you actually build and SEO will follow.
Published this article about our agent sandbox infrastructure a few days ago.

It's already ranking top 3 on Google for "how to sandbox an agent" and Google's AI Overview is referencing our control plane architecture.

Note to self: Write about what you actually build and SEO will follow.
"agent sandbox" also ranks high... damn. 

---


**作者** Chad Wahlquist（@chadwahl）  
**貼文連結** https://x.com/chadwahl/status/2028510615845892301  

**正文**

The Palantir Ontology - AI + Human Teaming 

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2028508130389426498  

**正文**

Axis is an AI platform for commodities trading desks.

Their models track positioning and market development in real time, allowing desks to deploy custom models tailored to their strategies.

Congrats on the launch, @beric_zhx and Ian!

https://www.ycombinator.com/launches/PYW-axis-an-ai-system-for-commodities-trading-desks 

---


**作者** Michael Grinich（@grinich）  
**貼文連結** https://x.com/grinich/status/2028518179765678427  

**正文**

I’m excited to share that @WorkOS has raised $100 million in Series C financing, valuing the company at $2 billion. The round was led by Meritech and Sapphire, with participation from Audacious, Craft, Abstract, Greenoaks, and others.

The fastest-growing AI companies already use WorkOS, including OpenAI, Anthropic, xAI, Cursor, Perplexity, Sierra, Baseten, Fal, Replit, Vercel, Synthesia, Temporal, Gamma, Clay, Exa, Parallel, Serval, and many more. These teams hit enterprise requirements almost immediately. From day one, buyers expect SSO, SCIM, permissions, and auditability. WorkOS makes that possible.

We are entering a golden era for builders. As the marginal cost of writing code drops toward zero, we’re seeing a wave of new software. More code is being written than ever before, and demand is rising just as quickly as companies race to adopt AI. The software lifecycle has compressed and what used to take years now take months, weeks, or even hours.

Next come agents. In the near future, much of the software running inside organizations won’t be operated directly by people at all. Yet every action will still need to be authenticated, authorized, and auditable. As intelligence becomes abundant and software becomes autonomous, trust becomes the constraint.

WorkOS was built for this moment. We began with authentication and have expanded into a broader platform that includes [granular permissions](<https://workos.com/fga>), [integrations](<https://workos.com/changelog/pipes>), [encryption](<https://workos.com/vault>), [abuse detection](<https://workos.com/radar>), [feature flags](<https://workos.com/blog/feature-flags>), [MCP](<https://workos.com/mcp>), and more. We’ve invested heavily in reliability and scale, with five nines of uptime across thousands of customers and billions of API requests each month.

This new funding allows us to accelerate the next phase: building what’s needed to make agentic software secure and reliable by default. Whether you’re vibe coding a weekend project or shipping an AI product to the largest organizations in the world, you can build faster and safer with WorkOS.

AI is changing what software can do. WorkOS makes it secure, scalable, and Enterprise Ready.

The only question left is: what will you build?

---


**作者** Dan Farrelly | Inngest.com（@djfarrelly）  
**貼文連結** https://x.com/djfarrelly/status/2028556984396452250  

**正文**

In every engineering discipline, a harness is the same thing: the layer that connects, protects, and orchestrates components — without doing the work itself. A wiring harness routes signals between an engine, sensors, and dashboard. A test harness provides the scaffolding that makes code repeatable and observable. A safety harness catches you when you fall.

Agent runtimes need the same thing. The LLM is the engine. Tools are the peripherals. Memory is storage. But what connects them? What catches the failure when the LLM times out on iteration five? What prevents two messages from colliding? What routes an event from a webhook to the right handler to the right reply channel?

That's the harness. And every agent framework is building one from scratch — their own retry logic, their own state persistence, their own job queues, their own event routing.

Durable, event-driven infrastructure already solves this. Every LLM call or tool call becomes a step — an independently retryable unit of work. If the process dies on iteration five, iterations one through four are already persisted. Events route triggers between functions. Concurrency controls prevent collisions. Step-level traces give you full observability over every iteration of the agent loop. The infrastructure is the harness.

We built Utah — Universally Triggered Agent Harness — to prove this out. A conversational Telegram or Slack agent with tools, memory, sub-agent delegation, and full durability. Minimal TypeScript, no framework. Just [Inngest ](<https://www.inngest.com/?ref=x-utah-1>)functions, steps, and events providing the harness around a standard think → act → observe loop. Think of it as a durable, cloud-ready OpenClaw.

The "universally triggered" part matters: Telegram or Slack webhooks, cron schedules, sub-agent invocations, inter-function events — the agent doesn't know or care how it was activated. The trigger is decoupled from the work. Add a Slack bot tomorrow and the agent loop doesn't change. The harness routes it.

Here's how it works.

## The architecture

Here’s what makes Utah different from most harnesses, it’s event-driven and it decouples the orchestration from the agentic loop. It also leverages Inngest Cloud to bridge the gap between a public webhook and a local worker.

![Article Image](<https://pbs.twimg.com/media/HCbftFRW4AIWxMY.jpg>)

Telegram or Slack webhooks hit Inngest Cloud, where a webhook transform converts the raw http payload into a typed Inngest event. A worker running locally picks up the event, runs the agent function, and fires a reply event that triggers a separate function to send the response back through the channel’s own API (more on this below). Any communication channel (or any service for that matter) that supports webhooks works.

The worker uses Inngest’s connect() API which establishes a persistent WebSocket connection from your local machine (or a mac mini or a remote server) to Inngest Cloud, without needing a public endpoint.

The agent loop running in the worker is simple: it’s a while loop with “steps” and the steps call LLMs and run tools. We use Pi’s provider interface and their tools as they’re both great, but you could use anything here. You could swap for AI SDK, TanStack AI, create your own tools or hook into MCP.

## If it’s local, why use Inngest? why not just use OpenClaw?

OpenClaw, and the [pi coding-agent libraries](<https://pi.dev/>) are an inspiration for this project. They both use in-process events internally, so events and orchestration are handled in memory. Inngest itself is an event-driven orchestration layer, so this project decouples the execution from the orchestration.

This enables a few things for the harness:

- The orchestration layer provides observability through traces and step-level inspection.
- Built-in durable execution provides reliability and retries.
- Decoupling lays the ground work for multi-player distributed agent orchestration.
- Event history provides and audit trail of what happened within the system.
- Scheduling is built in with crons or scheduled/delayed functions.

All of these problems are infrastructure problems, not AI problems.

## The agent loop as steps

The core of Utah is a think → act → observe loop. Each iteration calls the LLM, checks if it wants to use tools, executes those tools, and feeds the results back. Here's the key insight: every LLM call and every tool execution is an Inngest step.

A few things to note:

Inngest auto-indexes duplicate step IDs. When step.run("think") is called ten times in a loop, Inngest internally tracks them as think:0, think:1, etc. You don't need to manage unique step IDs yourself — the SDK handles it.

Each step is independently retryable. If the LLM API returns a 500 on iteration 3, Inngest retries that specific step. The results from iterations 1 and 2 are already persisted — they don't re-execute. This is durable execution doing exactly what it was designed for, just applied to an agent loop instead of a checkout workflow.

Text response means done. When the LLM responds with text and no tool calls, the turn is over. No explicit "done" signal needed.

## You don't need to build your own tools

Utah doesn't hand-roll file I/O and shell execution. It pulls in [pi-coding-agent](<https://github.com/badlogic/pi-mono>) — battle-tested tool implementations from the OpenClaw/Pi ecosystem:

- read, write, edit — file operations with image support, binary detection, smart truncation (the edit tool is a standout for context windows)
- bash — shell execution with configurable timeout and output truncation
- grep, find, ls — search and navigation respecting .gitignore

On top of those, Utah adds a few custom tools: remember (persist notes to a daily log), web\_fetch, and delegate\_task (more on that later).

The point: the tools story for AI agents is the same as any other software. Use existing libraries. Wrap them in Inngest steps. Done.

Easy. Copy, paste, ready to go.

## Six functions, not one monolith

![Article Image](<https://pbs.twimg.com/media/HCbgIOCXEAAWVLq.jpg>)

Utah isn't a single function that does everything. It's six functions that communicate through events:

This separation matters. The typing indicator fires immediately when a message arrives — it doesn't wait for the agent loop. The reply function handles Telegram/Slack-specific formatting and error handling (like falling back to plain text when the LLM generates malformed HTML). The failure handler catches unhandled errors across all functions and notifies the user.

Each function has its own retry policy, concurrency controls, and trigger conditions. This is natural in Inngest — you're composing behavior from small, focused functions connected by events.

And that sendReply function? It can be triggered from anywhere, so if we wanted to allow a sub-agent or fanned-out workflow to sent mid-loop replies to update the user, we can just send events from a new tool.

## Sub-agents via step.invoke()

Sometimes the agent needs to do a task that's big enough to blow out its context window — refactoring a file, researching a topic, writing a document. With general purpose agents like OpenClaw that run in single threaded conversations (e.g. Telegram), some long running sessions over a couple of days can have issues with context windows. The answer: spawn a sub-agent.

Utah has a delegate\_task tool. When the main agent calls it, it uses [step.invoke()](<https://www.inngest.com/docs/guides/invoking-functions-directly?ref=x-utah-1>) to fire up an entirely separate agent function run. Sub-agents fork the session’s context into it’s own sub-session (with it’s own session key) with a focused task an outcome:

The sub-agent function runs a fresh agent loop with its own context window, same tools (minus delegate\_task — no recursive spawning), and returns a summary to the parent:

This is step.invoke() doing exactly what it was designed for — calling another Inngest function as a step, waiting for its result, and continuing. The sub-agent gets its own retries, its own step-level observability, its own durable execution. The parent agent just sees a tool result: "here's what I did."

Orchestration is handled. No agent-to-agent protocol needed. Just functions invoking functions.

## Singleton concurrency: one conversation at a time

Each “channel” (e.g. Slack) uses a channel-specific session key to define what a “conversation” is. For single-threaded channels, like Telegram, it’s the chat id, for threaded platforms, like Slack, it’s channel and thread specific.

If multiple messages are sent in a conversation, you don’t want the first agent loop to just keep running then the next one to respond - you want the agent to have the context of both messages. So you either need to cancel the first loop and let the second loop handle it, or you need to handle “steering” within your loop. For this project, we decided the cancel+restart was the cleanest loop as the loop is restarted with all of the context.

On the message handler function, we set a single line config to handle this:

Two things are happening:

1. [Singleton concurrency](<https://www.inngest.com/docs/guides/singleton?ref=x-utah-1>) keyed on sessionKey — only one agent run per chat at a time. No race conditions. No interleaved responses.
1. Cancel on new message — if the user sends a new message while the agent is still processing, the current run is cancelled and a new one starts with the latest message.

In a traditional setup, you'd need to build a queue per user, manage locks, and handle cancellation yourself. With Inngest, it's one line of configuration.

## What we learned the hard way

Context management is the real challenge

The hardest problem wasn't calling the LLM. It was managing what goes into the LLM call.

Utah uses tools that might return thousands of characters per call. After a few iterations, the conversation context balloons, and the model starts losing track. We saw the agent loop endlessly calling tools without ever producing a response.

We fixed this with two-tier context pruning:

Old tool results get soft-trimmed (keep head + tail) or hard-cleared entirely when total context gets large. The last three iterations always stay intact.

On top of that, there's a separate compaction system for the session itself — when estimated tokens exceed a threshold, the conversation history gets summarized before feeding it into the next run. Pruning handles within-run context. Compaction handles across-run accumulation.

We also added budget warnings — system messages injected when the agent is running low on iterations, telling it to wrap up. And overflow recovery: if the LLM returns a context-too-large error mid-run, we force-compact the messages and retry without wasting an iteration. Between pruning, compaction, budget pressure, and overflow recovery, the agent stays on track.

Multi-provider LLM support

Utah doesn't call the Anthropic SDK directly. It uses [pi-ai](<https://github.com/badlogic/pi-mono>), a provider-agnostic LLM abstraction that supports Anthropic, OpenAI, and Google. Switching providers is a config change:

For the future, this also becomes interesting if sub-agents might evolve to use different models, potentially from different providers. A coding sub-agent could use Codex, while a research agent could use Opus. More on this to come.

Steering is an unsolved problem

When a user sends a new message while the agent is mid-run, what should happen? We use singleton — the current run is cancelled and a new one starts. This works, but any in-flight work is lost. The new run picks up from persisted session state, but it's not seamless. This is an area we're actively exploring.

Opportunity in streaming or mid-loop realtime updates

Each Inngest step is atomic — it runs, produces a result, and that result is persisted. This project doesn’t yet include streaming or leverage [Inngest’s realtime](<https://www.inngest.com/docs/features/realtime?ref=x-utah-1>) functionality. Telegram and Slack support individual events, but we’d like to layer on a web app and a TUI for this project to explore how to optionally send-mid-loop progress updates to a client that supports streaming. There’s more to come in future iterations.

## What we’re exploring next

Utah’s a personal single-player harness that runs locally on your machine or a server. The core architecture enables much more. Over the coming weeks we’re exploring what it will take to make Utah truly multi-player.

To make it multi-player, we’re going to explore swappable sandboxes, external state and memory. This would enable Utah to run on serverless if someone wanted to.

There are a lot of fun UX things we’d like to add built on the Inngest API and our Insights feature to build session monitoring for coding sessions. We will also explore using step.waitForEvent() to create human-in-the-loop approval flows when more input is needed.

The last piece that we’re exploring to make this truly “universally triggered” is enabling Utah to write itself - building new agents and workflows, creating new webhooks, and monitoring itself via API. If you’re interested, share some ideas on the GitHub repo.

## Try it yourself

The Utah source code is published as a reference implementation: [https://github.com/inngest/utah](<https://github.com/inngest/utah>)

It includes:

- The agent loop with Inngest steps and pi-ai's provider-agnostic LLM layer
- Tools from pi-coding-agent (read, write, edit, bash, grep, find, ls) plus custom tools
- Sub-agent delegation via step.invoke()
- Telegram and Slack webhook integration via Inngest webhook transforms
- Context pruning, compaction, and overflow recovery
- Session-aware singleton concurrency

Head over the to [README](<https://github.com/inngest/utah>) to give it a try.

The agent loop pattern works for any conversational AI — Slack bots, Discord bots, support agents, coding assistants. Adding any new channel is just a webhook transform and a reply function away.

If you're building AI agents and hitting the same walls — state management, retries, concurrency, observability — give Inngest a try. The primitives you need might already exist.

---


**作者** Fivos Aresti（@fivosaresti）  
**貼文連結** https://x.com/fivosaresti/status/2028561040242250003  

**正文**

I co-founded an agency that’s on pace for $5,000,000 ARR. 

We’re going to do that by becoming the #1 "service-as-software" for GTM.

Right now, we have 13 agents in our org chart.

And we’re “hiring” 10 more.

Here’s our plan to stay an extremely lean team:

(across departments)

Content Team
• Competitor Research Agent
• Content Ideator Agent
• Interviewer Agent
• Designer Agent
• Repurposer Agent
• Newsletter Agent
• Client Track Agent

GTM Team
• List Building Agent
• Qualification Agent
• Outbound Plays Strategist Agent
• Copywriter Agent

Sales Team
• Pre-Call Assistant Agent
• CRM Assistant Agent
• Email Assistant Agent
• Sales Analyst Agent

Project Management Team
• Project Tracker Agent
• Outbound Reporting Agent
• LinkedIn Reporting Agent

Customer Success Team
• ICP Matrix Agent
• Company Research Agent
• Meeting Summarizer Agent
• Onboarding Agent
• Expansion Agent

I put together a complete agents + humans org chart that maps this all out. 

That way, you can steal it and scale your company 3-5x leaner. 

If you want it...

Comment "Agents" 

And I’ll DM it to you.

---


**作者** Paul Adams（@Padday）  
**貼文連結** https://x.com/Padday/status/2028537395042492549  

**正文**

If you are a Saas company, this is a must read from @eoghan. 

We just crossed $400m in ARR. That chart is our growth rate, from Saas to AI.

At most, a single handful of companies have completed this transformation.

We are one of them, this is our guide on how to do it.

p.s. *please share it* with everyone you know working in Saas, it will undoubtedly help them chart their course!

---


**作者** Tony Kipkemboi（@tonykipkemboi）  
**貼文連結** https://x.com/tonykipkemboi/status/2028570527636279664  

**正文**

when I left CrewAI at the end of last year, a lot of friends asked why. 

it didn't make sense to most. agent frameworks were hot. funding was flowing. why leave now? 

the main reason: i saw this squeeze coming. some might disagree, but this was and still is my thesis. i'll write more about the second reason (experiencing enterprise AI adoption from the inside) on the next edition.

CrewAI is a great company with an incredible team, and i'm still close friends with them. this is an opinion piece. i expect some of you will disagree and some will agree. 

the goal is honest debate on the shifts in the industry.

---


**作者** Attio（@attio）  
**貼文連結** https://x.com/attio/status/2028460304418455799  

**正文**

Three years ago, I wrote an article about the reasons that [Salesforce was great](<https://attio.com/blog/why-salesforce-is-great>) — arguing that its flexible data model was its real moat, even if the complexity was painful. Since that article was written, a lot of things have changed in the software space: most notably, the rapid advancements of generative AI and large language models. As these models have matured, they have yielded agentic workflows that are capable of processing information from varied sources and taking complex actions over extended periods of time. These rapid changes have laid bare the foundational weaknesses that exist in legacy CRM architectures and many teams have struggled to strongly adopt agentic workflows into their organization as a result.

Agentic systems place new demands on the systems that they operate on and require a fundamentally new type of application and system architecture in order to operate effectively. As a result, we at Attio have been deeply focused on how we can evolve our platform to truly serve the needs of agents and deliver on our [AI vision](<https://attio.com/next-gen>) that we shared last year.

We’re excited to share a new foundational data model that sits at the heart of Attio and powers our newest product, Ask Attio. We call it Universal Context. Universal Context builds upon our foundational data model Particle, infusing it with semantic knowledge and full text search, providing agent-friendly ways to interface with the data and maintaining its ability to deliver massive scale and transactional consistency.

Universal Context is built for the realities of running agentic workloads in production and incorporates into its design the feedback and learnings of more than 7,000 teams that place Attio at the heart of their go-to-market strategy.

## New ways of thinking about data

By virtue of their design, agents necessarily introduce a fundamentally new set of demands on the infrastructure upon which they operate. For example, it’s quite unlikely that two humans would attempt to action an identical task at exactly the same time when using an application like a CRM. Even some of the largest human teams of a few thousand people are unlikely to generate a significant number of conflicting modifications. In an agentic world, it’s plausible that even a small business might be running tens of thousands of highly parallel agents at the same time, vastly increasing the risk of them conflicting.

Legacy platforms have attempted to introduce AI capabilities by adding additional tools to their stack (such as vector databases like Pinecone or Turbopuffer) which serve as replicas of the data held within them. These tools unlock semantic search, but they suffer from delayed replication from the source of truth and make it challenging for agents to unify structured queries with unstructured recall. In database terms, we refer to this as Consistency: the ability for a system to accurately represent state at a given point in time.

Universal Context is the first system in any CRM to provide External Consistency (the highest possible level of transactional consistency) that guarantees that the semantic embeddings used by agents to efficiently traverse across the data inside of Attio are always exactly in sync with the other data in the system.

And it’s not just agents running inside of Attio that benefit from this consistency. Agents running in other platforms such as ChatGPT or Claude Code also benefit from these guarantees. Using our new MCP server, agents running in external platforms benefit from exactly the same consistency guarantees and advanced indexing capabilities as agents running directly inside of Attio.

This unlocks a new foundation for agentic workloads, as agents across different platforms can now operate collaboratively in real time on a single source of truth. For example, say an agent running in Claude Code decided to research a contact and update the record with a note about their interests. In legacy systems like HubSpot or Salesforce, that note might not be visible to other agents for some time as indexing pipelines and other workloads happen asynchronously from the initial write. With Attio’s Universal Context, another agent running at exactly the same time in ChatGPT would now see that note when looking for records with a particular interest.

## Schema as context

To advance agents within a GTM organization, there needs to be an on-ramp into the organization’s data that allows agents to understand the shape of data and how to access it. With many MCP servers today, the challenge of accessing data has been solved but this rarely comes alongside an understanding of how the data is shaped. These early attempts at indexing data that lives in different silos were challenging for agents to reason about consistently. Indexing capabilities and syntax varies between tools, and agents often struggled to accurately ground their decisions in this disparate data.

For human users, challenges like these have typically been solved by data warehouses, but when working with agents these systems suffer from the ETL pipelines that feed them. Warehouses provide a delayed and inconsistent replica of their source data making them of limited value for realtime agentic workloads.

Agentic users require a unified and consistent model for accessing the data that they rely upon to make decisions and measure their results. This data problem defines an important requirement for any AI-native system in the GTM space: can you provide an agent with unified, accurate, and consistent information with which to ground its decisions?

Particle’s flexible graph-relational format provides the agents consuming Universal Context with a single, cohesive language to explore and index all of an organization’s go-to-market Data. By integrating with all of the different sources of GTM across an application, Universal Context builds a complete understanding of an organization’s go-to-market landscape. This includes everything from simple structured data like name or email address, through dynamically researched enriched data like job title or industry, all the way to unstructured proprietary data like emails, notes, and call recordings.

All of this data combines to create a safe, well-understood playground for agents to explore, build, experiment, and improve upon.

## The promise of generative application logic

One of Salesforce’s less well-known superpowers was Apex. Introduced in 2007, Apex is a proprietary, strongly-typed programming language that allows developers to write code that can extend the product’s capabilities.

Apex was quietly revolutionary. It meant that if you were willing to spend enough time and money on development, you would be able to configure the platform to your needs. This code-based extensibility is one of the key reasons that Salesforce has been so persistent in the market. When your business processes are encoded in thousands of lines of custom code that only run on a single platform, migrations become far more complex.

In 2026, coding agents are fundamentally changing how software gets built. The question is no longer one of resource and time as autonomous coding agents rapidly move us towards a world of generative application logic. This shift makes code-based extensibility more valuable than ever before: without code execution, agents are deeply constrained by what they can achieve and how they can surface results to the end user.

Brilliant though it was when released, Apex is a complex and proprietary offshoot of Java 5 from 2007. This creates problems when working with the latest generation of coding agents like Claude Code and Cursor. Modern LLMs are not well placed to work with these environments: they require a new kind of platform to build upon. (Salesforce understands this, which is why they’ve invested so heavily in custom models like xGen-Code and CodeGen specifically for Apex, but they’re playing against the ecosystem, not with it.)

Last year we released Attio’s App SDK, a Typescript based code sandbox that allows Attio customers to extend their instance using a fully managed serverless environment and React. Our core design goal when designing the App SDK was to ensure that it served as a “compilation target” for AI. We designed the environment and the library from the ground up to be understandable and forgiving to LLMs working in our environment.

By leveraging the extensive Typescript ecosystem, App SDK allows agents like Claude Code to easily build upon the extensive ecosystem of packages available on npm. Agents can work with local tools, allowing a fully autonomous build, test, and deploy pipeline with standardized tools. Contrast this with the Apex deployment model—with a proprietary IDE and Salesforce-specific tooling—and it becomes clear that Apex is in a challenging spot.

We believe that code generation isn’t just a feature of the next generation of GTM tooling—it’s the whole foundation. The assumption that configuration and code were in contention is breaking down as coding agents allow anyone to easily generate, test, and improve totally custom code. In fact, as agents like Ask Attio become more powerful, it’s likely that end users won’t even know that code was involved: they’ll simply ask for a capability and receive the application they need to work effectively.

## The AI future of CRM

With the release of Universal Context, alongside Ask Attio and the MCP tools that build upon it, is an important milestone in our mission to deliver cutting edge agentic functionality to our customers. We have an exciting roadmap ahead which will continue to expand on the functionality of our existing agents, as well as adding new agents and surfaces for our customers to benefit from the extraordinary powers of AI.

---


**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2028530967351304231  

**正文**

introducing @nozomioai v1.

state of the art search and index API to reduce hallucinations in AI agents.

use it inside any coding agent or power your own products (thread): 
introducing @nozomioai v1.

state of the art search and index API to reduce hallucinations in AI agents.

use it inside any coding agent or power your own products (thread): 
1) When I finished @ycombinator, I announced Nozomio as a standalone MCP server that gives agents up to date docs.

A lot has changed since then.

Watching how customers actually use the product made the real shape of the problem obvious. People are not just “reading docs”. They’re trying to give agents reliable context across everything technical: codebases, internal docs, PDFs, blog posts, datasets, tickets, changelogs, wikis, and increasingly, internal company knowledge.
2) And the pattern became clear:

Context is king for AI agents (cc @levie).

Knowledge work has always been messy. Docs go stale. The real learnings live in tribal knowledge. Best practices spread through osmosis, not systems.

AI agents flip this. The leverage you get from agents depends on how effectively you can give them the right data, structured correctly, kept current, and grounded in your workflows.
3) That’s what @nozomioai is for.

We help you:

- index technical sources (code, docs, PDFs, research, datasets, web, and more)
- search with high precision and low hallucination risk
- plug into agents so the “context layer” stays always on
4) A *VERY* small subset of what’s new in v1:

Nia Slack Search API

Slack search is frustratingly bad: mostly keyword-only, no semantic understanding, and painful when you need decisions from old threads. So we built a Slack Search API that indexes your workspace, keeps it synced in near real time, and lets you search semantically or via agentic retrieval.
5) Tree Reasoning for PDFs

Traditional RAG treats PDFs as bags of text: chunk, embed, hope. It breaks on complex docs where structure matters.

We built structure-aware PDF search: we extract the document hierarchy, tag chunks by section/page, then have an LLM reason over the tree to decide where to look before running retrieval. When you ask about “results”, you get results.
6) Agent-native integrations

Nozomio works with the tools people actually use: plugins + skills that plug into any agent setup (Cursor, OpenClaw, Claude Code, custom agents, etc.). We’re also expanding data sources aggressively so the context layer can cover more of your stack.

Just run 'bunx nia-wizard' in your terminal
7) Tracer (GitHub code search agent)

We built an autonomous code search sub-agent called Tracer. It can search across public GitHub in under 5 minutes and return a clean report with the exact files and line ranges. 
8) Dataset indexing + search

We now support indexing datasets (not just docs). So agents can retrieve from structured + messy sources in the same workflow, and you can search across data the same way you search across code and PDFs. 
9) Under the hood, we’re betting heavily on research because this problem does not get solved by “just use web search”. The hard part is retrieval that stays correct as data scales, changes, and gets messy.

Also, a quick update: since launch we’ve brought on Angela Chen (@Google), Timothee Cour (@GoogleDeepMind), and @gokulr as strategic angels.

Back to work.

---


**作者** Justin Lee（@Justin01805921）  
**貼文連結** https://x.com/Justin01805921/status/2028538818903867645  

**正文**

Introducing Linkedin for agents

All the b2b gtm channels are dead.

55% of the latest YC batch used supabase because claude code defaults to it. 

The AI agent economy has arrived: 
Introducing Linkedin for agents

All the b2b gtm channels are dead.

55% of the latest YC batch used supabase because claude code defaults to it. 

The AI agent economy has arrived: 
Send this to your agent: https://agentcommune.com/

---


**作者** Alex Immerman（@aleximm）  
**貼文連結** https://x.com/aleximm/status/2028490204307173840  

**正文**

The software industry is having a panic attack. Since the start of 2026, ETFs for public software companies have fallen by 30 percent, erasing all the gains since the launch of ChatGPT. Companies like Salesforce, Adobe, Intuit, ServiceNow, and Veeva—bellwethers that have compounded investors’ capital for a decade or more—are down 25 to 30 percent in a matter of weeks. Viral Substack posts imagine a world where the customer base for enterprise software is hollowed out and the S&P enters a massive years-long drawdown. They’re calling it the “SaaSpocalypse.” It’s rapidly become the market consensus: AI is going to kill the software industry.

![Article Image](<https://pbs.twimg.com/media/HCagFzgboAAxdUA.jpg>)

Yes, AI is a big deal. But the conclusion that AI is going to kill the vertical and functional software business model simply makes no sense. The truth is that AI simply isn’t going to kill software companies: after all this panic has passed, we’ll see that AI is the best thing that ever happened to the software industry.

Why is that?

The bear case rests on a basic misunderstanding of what software companies actually sell. The market is treating “software” as though it were a commodity input—as if the value of a software company resided in its code, and cheaper code meant more competition and therefore cheaper companies. But code is never where the value has lived: if code is where the value was, these companies would have never gotten so big in the first place. They would have been killed years ago by open-source software or by competition from cheap software engineering labor in developing countries.

The bearish arguments today usually fall into one of four categories. Maybe the foundation model labs will move up the stack and own every function-specific application. Or maybe enterprises will “vibe code” replacements for their internal tooling, or at least use the option of doing that to reduce software businesses’ pricing power. Or maybe existing players will use AI to massively expand their product breadth, rubbing against each other. Or maybe a flood of new entrants—the famous “single-person billion-dollar company”—will undercut incumbents on price. Pile on top of this agents won’t care about brand loyalty or familiar names, only the cheapest options for any particular task.

AI might increase competition; but it’ll also dramatically expand what software companies can do, how fast they can do it, and how large the markets they serve can become. The end result won’t be margin compression to zero. Software will be a much bigger industry, with durable competitive advantages for the companies that earn them.

## The moats that matter aren’t going away

The classic contemporary book on business moats is Hamilton Helmer’s Seven Powers. He lists seven distinct ways in which companies develop robust competitive advantages: Scale, network effects, counterpositioning, switching costs, brand, cornered resources, and process power. Let’s go through them:

Switching costs are perhaps the one moat that really is going to change. It’s definitely true that AI is changing the friction and the cost-benefit analysis associated with switching vendors: agents can assist with a lot of migration work that used to be a headache. So it means legacy companies with “[hostages, not customers](<https://a16z.com/the-greenfield-strategy-ai-native-startup-bingo/>),” to borrow a phrase from our colleague Alex Rampell, will feel a lot more pressure than they’re used to.

But that is a good thing for software as a whole. When companies have to earn their customers’ loyalty instead of relying just on vendor lock-in, the result is better products, faster innovation, and a healthier competitive ecosystem that grows faster and delivers more value to its customers. We expect AI will shift some customers to new winners, but it won’t impair industry profit pools at large: companies will just get better.

Network effects are a classic moat. And they aren’t going away. We tend to invoke network effects for social media platforms or marketplaces —the more nodes in the network, the more attractive it is to be on it. But the same applies to application software offerings that exhibit ecosystem, collaboration, and data network effects. On the surface, Salesforce is a CRM database; but anyone who has worked in an enterprise setting knows that Salesforce is also an ecosystem. When everyone uses one platform, the network becomes self-reinforcing: you use Salesforce because everyone uses Salesforce. And the more companies use Salesforce, the more valuable the ecosystem of third party applications built on top of Salesforce and platform administrators experts in Salesforce. In recent years, a similar thread is true for Figma: every designer, then every engineer, product manager, marketer buys Figma because everyone is collaborating there - go to the annual Config conference and witness the value of the ecosystem firsthand.

And the same dynamic is emerging in the AI-native generation. Harvey and Hebbia are building finance and legal collaboration spaces that connect service providers and clients, and soon their agents, on a single system: the more people and agents who use these platforms, the more valuable the platforms become. EliseAI’s maintenance product is a multi-sided network that becomes more valuable with every unit and vendor added. As migration gets easier, aggregation gets easier, but these network effects simply don’t go away in a world where software is free. In fact, insofar as AI makes the network more powerful—you can just do much more with a network than you could before—we should expect to see AI make these network effects more powerful than they were before.

Scale was never the defining moat in software—it’s just not as important for Salesforce as it is for a cloud provider or for an industrial company. But to some extent, it may matter more for AI applications where compute spend exceeds labor costs, driving a unit cost advantage to the larger consumers of tokens. In addition, there are places where scale will still help: it’s a straightforward economy of scale to concentrate that maintenance burden in one place, since productivity gains from specialization don’t go away in an AI world. Stripe highlights the value of centralized infrastructure benefitting all of its clients. Its compliance infrastructure absorbs the cost of navigating regulations across dozens of countries so that individual businesses don’t have to; its payment optimization algorithms, which route and retry transactions to maximize authorization rates, improve with every dollar of volume—and they can pass those savings on to their customers. Finally, scale will continue to benefit companies at the intersection of bits and atoms; Anduril, Flock Safety and Waymo will continue to see lower unit costs as they produce higher volume of their hardware offerings.

Brand endures. For better or worse, “no one got fired for buying IBM” remains a fact of life in most enterprises. And if every industry gets more crowded—if there’s suddenly an explosion of fly-by-night solopreneurs selling vibe-coded ERPs—we should expect the power of strong brands to increase. Brand is how you signal reliability in a world of infinite optionality. No upstart is going to instantly replicate the trust and recognition that companies like Stripe or Shopify or ServiceTitan have built. The closer you sit to business-critical functions—people really don’t want to get creative when it comes to payment processing—the more powerful brand effects will be. If you are a startup and you charge customers, you build on Stripe by default.

We do acknowledge the power of brand might change as more decisions are delegated to AI agents that optimize for price without the soft considerations that humans have (agent-led growth!). But as long as they report to humans who have to worry about getting fired, the “no one got fired for buying IBM” principle still holds.

Cornered resources, like high-quality [proprietary data](<https://a16z.com/fruits-of-the-walled-garden/>), aren’t going to stop mattering either. If friction goes to zero, simply consolidating publicly available data into a usable interface becomes less valuable, because anyone can do it. But if AI enables doing much more with high-quality data than you could before, then the stuff that you can’t get easily becomes extremely valuable. We have observed the power of Bloomberg’s live market data, Abridge’s millions of clinical conversations, OpenEvidence’s vast medical library, and VLex’s legal database.

And perhaps the strongest moat of all in this new era is process power—or as George Sivulka of Hebbia calls it, “[process engineering](<https://x.com/gsivulka/status/2024187126020272197>).” Application software can be thought of as a stored process—it encodes opinions about how the function of an organization should operate, and those opinions calcify over years and decades of use into something that is inseparable from the organization itself. Successful app software companies are the ones that co-evolve with their clients around these workflows. As those workflows penetrate ever-deeper into an organization, process engineering only becomes more important. And more difficult for challengers to replicate.

Consider Harvey. If Harvey deeply understands how a particular law firm structures its work—the templates, the review processes, the institutional preferences, the way a specific partner likes her memos done—there is simply no way a new entrant can replicate that overnight, even with the cost of code being zero. That kind of embedded workflow knowledge becomes more powerful, not less, as software moves from a system of record to a system of action, because you can just do much more with that knowledge. So as the underlying models improve, Harvey’s orchestration layer—the scaffolding that routes model output through specific professional workflows—compound in value. Better models don’t make the application layer thinner: they make it more capable, because the hard part was never raw intelligence. It was knowing what to do with it.

## Platform shifts create new winners—and new moats

But there’s one final source of durable competitive advantage that we find particularly exciting as investors. And that is counterpositioning.

Counterpositioning is a kind of power that can be summoned and wielded by new entrants to a market. It’s when the new company has a business model which, for whatever reason, is unattractive for the incumbent company to compete against. Disruption theory from Clay Christensen is a classic type of counterpositioning, but it doesn’t always have to be “low cost” as the differentiated counterposition. In software, a new technology stack could create the opening for a startup to create new kinds of products and business models that are difficult for incumbents to replicate - like Databricks and their “Lakehouse” model.

The “agent” model of doing work and replacing tasks is certainly going to create some counterposition opportunities for new startups to challenge incumbents. There’s been a lot of ink spilled on the disruption of “per seat pricing” at the hands of agentic upstarts with value-based pricing. Let’s take customer service as an example. Decagon prices its customer support product per conversation handled, not per agent seat, and will eventually price per resolution achieved: that’s fundamentally a better alignment of incentives between vendor and buyer. An incumbent like Zendesk can’t easily make that same move without cannibalizing its own seat-based revenue. Just as Blockbuster couldn’t match Netflix’s subscription model without destroying its existing economics or Peoplesoft couldn’t match Workday’s SaaS model without upending its monetization. Companies that start with the new business model don’t face that dilemma, and it’s the core reason why platform shifts so reliably produce new winners.

But guess what? The total amount of “end state pricing power” in the market didn’t necessarily decrease; it just means customers now have a choice of business models they’d like to subscribe to, and the better one will win. That’s how competitive markets have always worked! AI is not the first time that a wave of creative destruction has rearranged markets and shifted the playing field. But here’s the thing: the business models that result almost always dwarf the old ones in the scale of the total opportunity.

## The great software bifurcation is coming

So yes, AI will definitely change vertical and functional software. But it won’t look like a massacre. Maybe gross margins settle into a different steady-state: maybe pricing power is diminished because switching costs give procurement teams more leverage in vendor negotiations, but AI also supports margin expansion due to a much more efficient use of labor. But no matter where margins end up, we expect that scale will expand dramatically: because as our colleague Anish Acharya likes to say, [the world is still short software](<https://www.bloomberg.com/news/videos/2026-02-05/acharya-world-is-still-short-software-video>). We are nowhere near saturating the world’s demand for high-quality software. And as code becomes cheaper, we should just expect to see the market demand more.

On the other side of this AI transition, we’ll be looking at a much bigger software industry that provides much more value to its customers. Companies will be able to serve more customers, enter adjacent markets, and automate workflows that were previously far too complex or too expensive to touch. Customers that were previously too low ACV will suddenly have attractive economics. Ideas that would once have gone in the “too hard” pile suddenly become interesting and feasible. There will still be moats, and as long as there are moats there’s plenty of reason to expect hugely successful and highly durable businesses to survive and thrive.

AI isn’t going to destroy the software industry; it’s going to split it into two parts. There really will be some categories of software companies that face genuine pressure. Frontend tools that serve primarily as thin wrappers around commodity functionality and do relatively little beyond presenting data in a slightly more convenient format are vulnerable. Incumbent systems of record that still operate on archaic interfaces but raise prices every year should be worried. So should software companies that have an outdated pricing model and value proposition that’s just inferior to what AI-native competitors can offer. The companies that win in this environment will be the ones delivering genuine value, not the ones that built the highest walls around their customer base.

But that’s just creative destruction: it’s great for the industry that these companies are facing pressure that they weren’t facing before. Some of them will figure things out and get stronger ; others won’t and will die. That’s good! The rest of the software ecosystem—the companies that are committed to delivering real value for their customers—is set to grow massively.

So yes, some individual companies will lose. But the industry will win, and win big. The SaaSpocalypse isn’t the death of software. It’s the start of something much bigger.

Thanks to @santiago\_\_rdz for coauthoring this piece.

Full article in the a16z Newsletter: https://www.a16z.news/p/good-news-ai-will-eat-application

---


**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2028499247570755604  

**正文**

有意思又一个 AI 短剧生成 Agent 产品

对话式多 Agent + Skills 协同调度，给一个文本故事就能交付成片。

支持跟 Agent 交互，比如OpenClaw 等 Bot 可自动调用，实现 7×24 小时持续制作。

---


**作者** Pierre-Eliott Lallemant（@pierreeliottlal）  
**貼文連結** https://x.com/pierreeliottlal/status/2028381688963670131  

**正文**

🚨 Launch alert 🚨
I’m launching “Claude Code for Outreach.”

One year ago, I built and sold Coco AI for $1M+.
But I had a huge problem.
Doing LinkedIn outreach was insanely hard.

I had to juggle way too many tools.

One tool for scraping.
Another for enrichment.
Another for intent signals.
Another for writing messages.
Another for follow-ups.

Five tools. Endless tabs. Zero flow.
And I wasn’t the only one.

We kept seeing the same pain, solo founders and small sales teams all struggling with fragmented outbound.

That’s why we built Gojiberry AI.

One place to detect high-intent leads, enrich them, start conversations, qualify prospects, and book meetings automatically.

We just launched on Product Hunt and if this resonates, I’d truly appreciate your support 🙏

👉 https://www.producthunt.com/products/gojiberry

I’m always hungry for feedback, feel free to share your honest thoughts, even if it stings ❤️

PS: If you want to support even more, a repost would mean a lot ♻️

---


**作者** Aakash Gupta（@aakashgupta）  
**貼文連結** https://x.com/aakashgupta/status/2028220643733537134  

**正文**

.@NadavAbrahami built Wix into a $4B company over 20 years, left with 30 of his best engineers, and created the tool that exposes the biggest gap in how Cursor handles visual editing 
.@NadavAbrahami built Wix into a $4B company over 20 years, left with 30 of his best engineers, and created the tool that exposes the biggest gap in how Cursor handles visual editing 
@NadavAbrahami YouTube: 

https://youtu.be/9fgKBKIPUUU

---


**作者** Artem Zhutov（@ArtemXTech）  
**貼文連結** https://x.com/ArtemXTech/status/2028330693659332615  

**正文**

Every conversation with Claude Code starts from zero. Here's how I fixed that with a local search engine and a skill that loads your full context before you type a single word.

Every conversation with Claude Code starts from zero. I had 700 sessions in 3 weeks and I don't remember what was happening back then. I'm losing control in terms of what's happening.

![Article Image](<https://pbs.twimg.com/media/HCYRyH0XEAAMOXj.jpg>)

I just open a new terminal and then what's going on. I need to somehow find all this context. What was the project, what are the decisions. I need to start from zero all the time.

It gets worse mid-session. When we hit context limit at 60%, we need to compact or hand off. Then half of the decisions have been lost. Or even worse if I want to continue next day, I don't remember what was happening back then.

![Article Image](<https://pbs.twimg.com/media/HCYR_j3bsAACdsK.jpg>)

The current paradigm of grepping over files doesn't scale. So I plugged [QMD](<https://github.com/tobi/qmd>) into my vault, a search engine by Tobias Lutke @tobi , CEO of Shopify. Made in Canada.

The whole memory system I'm about to show you - it's a skill. [Install it in 2 minutes](<https://memory-artemzhutov.netlify.app/>) and Claude Code already knows how to use it.

## QMD: A Local Search Engine for Your Vault

QMD is a local search engine for your knowledge base. It indexes your Obsidian @obsdmd  vault and finds anything in under a second.

For each vault folder I have a QMD collection. Notes, daily entries, sessions, transcripts. One-to-one mapping. For each collection I can perform a focused search.

![Article Image](<https://pbs.twimg.com/media/HCYR1DzbgAABsVY.jpg>)

That's it. One command, your vault is searchable.

But searchable how? The default way Claude Code @claudeai  searches is brute force - it sends a Haiku sub-agent to grep through every file. I tried it ([watch](<https://youtu.be/RDoTY4_xh0s?t=167>)): searched for my notes about different graph approaches the normal way. It took 3 minutes. I was bored, scrolling Twitter while waiting. And the results? 300 files, not great.

QMD search was instant. Better results. Way fewer tokens. You don't have to use sub-agents to do that. The difference: grep matches strings, QMD ranks by relevance.

## Grep vs BM25 vs Semantic

QMD gives you three search modes. BM25 (qmd search) is deterministic full-text search. Like grep, it matches exact keywords. Unlike grep, it scores each file: how often does the word appear, and how rare is it across all your documents? A short note mentioning "sleep" five times scores higher than a 10,000-word file where "sleep" appears once. No AI, no embeddings - just math. Semantic (qmd vsearch) uses embeddings to find meaning - you can search for a concept even if the exact words aren't there. Hybrid (qmd query) combines both.

I searched for "sleep" across my vault. Here's the difference.

![Article Image](<https://pbs.twimg.com/media/HCYRzlVWMAEuC5d.png>)

Grep found 200 files. All over the place. It finds all the files which contain the word "sleep." It even finds sleep() - a programming command that pauses code execution. Nothing to do with actual sleep. That's the problem with string matching.

BM25 (2 seconds): a reflection about sleep quality. Experiment with tracking sleep fragmentation patterns. Sleep interrupted at 3am. Much better.

But qmd search "insomnia" returns zero results. The word doesn't exist in the vault.

Semantic search: I type qmd vsearch "couldn't sleep, bad night" and it found a bedtime discipline goal I set years ago. It goes beyond the keywords and explores the meaning. Four of five results don't contain the search words at all. Grep could never find them.

Hybrid (qmd query "couldn't sleep, bad night"): ranks sleep quality improvement at 89%, sleep interrupted at 3am at 51%, health sleep optimization at 42%. The best ranking of all.

![Article Image](<https://pbs.twimg.com/media/HCYR5mdXcAAUohz.jpg>)

Start with BM25. Fast and handles structured notes. 80% of searches. Add semantic for transcripts and braindumps, where you'd never search for those exact words.

## What semantic search actually surfaces

I searched my daily notes: "find the days when I was happy and what was the reason."

This is a non-trivial query. Claude adapted it and ran multiple searches:

Found semantically relevant connections across months of daily notes.

The pattern: my happiest days are when I ship something and I had good sleep recovery, like sauna or 9 hours of sleep.

Then it surfaced something I had completely forgotten. Back in October when I was writing my PhD thesis and I was about to give up. I needed to do it day by day, come in and write something. But what I realized back then is that I just need to see it through discomfort instead of escaping to quick fixes.

I didn't remember writing that. I didn't expect the search could surface this. But there it was, the exact citation.

## /recall - load context before you start

/recall is a Claude Code skill that sits on top of QMD. It loads context before you start working - instead of explaining to Claude what you were doing, you tell it to recall.

It has three modes: temporal (scan your session history by date), topic (BM25 search across your QMD collections), and graph (interactive visualization of sessions and files).

![Article Image](<https://pbs.twimg.com/media/HCYR8ifWkAAxA9Q.jpg>)

/recall yesterday

/recall topic graph

/recall graph last week

Yesterday reconstructed 39 sessions from one day. Timeline, number of messages in each session, what was done when.

![Article Image](<https://pbs.twimg.com/media/HCYR-GIawAAp5AH.jpg>)

Topic searched for "QMD video" across sessions and notes. Returned the dashboard, production plan, to-do list. All related files surfaced in less than a minute. Compare that to the brute force approach: tell Claude "find all information about this project" and it sends Haiku to grep through your vault for 3 minutes, burns tokens, and comes back with worse results. With /recall topic, I reconstructed the full state of the project and asked: what is the next highest leverage action?

Graph opened an interactive visualization of my whole week. Sessions as colored blobs, older ones dimmer, recent ones highlighted in purple. Files clustered by type: goals, research, voice, docs, content, skills.

Here's an example: I was exploring lunch places. I told Claude "I want to have a great lunch" and we analyzed different places to go. I stored those as activities I might want to try. A week later, I open the graph, see that session, copy those file paths into Claude Code and continue from there. The graph makes every past conversation recoverable.

![Article Image](<https://pbs.twimg.com/media/HCYSCrYXwAAzVcj.jpg>)

![Article Image](<https://pbs.twimg.com/media/HCYSBRvacAAFP9w.png>)

## 700 sessions, all searchable 

Claude Code saves all your conversations as JSONL files on your computer. I had 700 sessions in the last 3 weeks. Each one has decisions, questions, context I'll need again.

The raw files have tool uses, system prompts, roles. We parse a clear markdown, the actual signal, the actual user messages, and embed this into the QMD index.

At the end of each session when I close my terminal, I have a hook which exports and embeds those sessions into QMD. So the index is always fresh. I can get back to anything I had even from today.

![Article Image](<https://pbs.twimg.com/media/HCYSEO4XUAAqxlO.jpg>)

## Finding Ideas You Never Acted On 

This is the one that surprised me. I searched: "find the ideas that I have never acted on."

Having Claude synthesize the raw QMD results is very useful - it's hard to parse the actual raw results yourself. Claude summarized what it found:

- October 19th - I wanted to build a PhD writing dashboard but never did it
- I had ideas for illustration-based apps but never followed through
- I had an idea to record a screen recording about my full Obsidian workflow but never committed

![Article Image](<https://pbs.twimg.com/media/HCYR7BGWgAEdJVg.png>)

And it's all local - all of these embeddings live on your computer.

## Tools change. Your context stays.

Your notes stop being passive. They stop being trapped in your Obsidian world. They actually start doing things. All of your notes is useful context about yourself that you can use to achieve goals in your life.

Tools change. A month from now there are going to be new models. So what. If you have your context you can make it work in any situation. Claude Code, Codex, Gemini CLI, anything.

The memory layer works as a skill across your whole stack. I use Obsidian Sync to keep my vault in sync between my Mac and a Mac Mini that's always on. On the Mac Mini, OpenClaw runs 24/7. So I pick up my phone, open OpenClaw, and I have the same vault, same QMD index, same skills - from anywhere.

![Article Image](<https://pbs.twimg.com/media/HCYR2lMWAAAhqf9.jpg>)

## Next steps

Download the /recall skill, drop it in your .claude/skills/ folder, and you have the session pipeline and recall working today (or ask Claude to do it for you :) ).

QMD - the search engine behind all of this. By Tobias Lutke.

https://github.com/tobi/qmd

Watch the full video - 42 min walkthrough with live demos.

https://youtu.be/RDoTY4\_xh0s

Artem

---


**作者** Rohan（@lets_dig_deeper）  
**貼文連結** https://x.com/lets_dig_deeper/status/2028370306063343913  

**正文**

hiring for @rumik_ai on the basis of pure skills, taste and hunger!

looking for memory, conversational quality & alignment researchers at rumik

we’re working on long-horizon conversational systems - agents that carry memory forward, maintain world-state consistency, and stay coherent across 1000+ turns.

this would require you to build systems that remember context, track evolving narratives, and adapt to subtle user intent over time.

we’re looking for researchers with experience in:

 • memory systems, retrieval, entity/state tracking
 • long-turn conversational stability & quality
 • evaluation and benchmarking beyond simple a/b tests
 • rlhf and preference learning
 • multi-agent systems

if you’re interested in depth over demos and care about building conversational intelligence that compounds over time , let’s talk.

dm or mail at vatsal@rumik.ai

---


**作者** David Byttow（@davidbyttow）  
**貼文連結** https://x.com/davidbyttow/status/2028233578329600449  

**正文**

## agents are collapsing the coordination layer of organizations

for decades, engineering leadership was built around synchronization: breaking work into tasks, assigning owners, mapping dependencies, running planning cycles, tracking progress. we built an enormous bureaucratic scaffolding to keep humans aligned on what to build and in what order.

that scaffolding was load-bearing when coordination was expensive. now it's only getting cheaper.

agents decompose, sequence, and execute. describe the goal, provide constraints and context, iterate on output. what used to require sprint planning, dependency graphs, and a project manager now happens in a tight conversational loop. the more tools at the agent's disposal, the less coordination that's needed.

people whose focus is on process are now redundant.

## writing code was never the bottleneck

the bottleneck was coordination overhead: ticket grooming, status syncs, handoff docs, meetings about alignment, dashboards tracking dashboards. the real cost was keeping humans synchronized.

so organizations optimized around process. the system became the product and people served it.

that model was defensible when the cost of misalignment was high and the cost of execution was low. now execution cost is collapsing, and coordination cost is approaching zero for anyone using agents seriously.

if your organization's primary competence was moving work through a pipeline, that competence just got commoditized.

## when you automate coordination, what remains is judgment

taste. direction. ownership. the ability to define a goal clearly enough that autonomous systems can act on it without constant correction.

AI will not replace managers. it will expose the ones whose contribution was procedural rather than directional.

if your value was assigning tickets, facilitating standups, tracking burndown charts, or managing dependency spreadsheets, that work is already being absorbed. if you equated control with contribution, the leverage just disappeared.

the teams that actually ship have never depended on process for their shape. they depend on a person who owns the outcome and has a sharp internal model of what "good" looks like.

AI just removed the friction layer.

## the core skill is now goal clarity

for years, engineering leadership centered on decomposition. take a large objective, break it into tasks, assign owners, manage the dependency graph, orchestrate the cadence. the core skill was coordination.

in the agentic world, that entire workflow collapses into a different question: can you articulate what success looks like? the quality of AI output correlates almost perfectly with the clarity of the goal, not the implementation steps, not the task breakdown.

what are the constraints? what tradeoffs are acceptable? what does "good" feel like?

you cannot micromanage an agent into a great outcome any more than you can micromanage an engineer into one. you have to know what you want. and knowing what you want, really knowing, with enough precision that an autonomous system can act on it, turns out to be a rare and specific skill. it requires taste: an internalized sense of quality that can't be reduced to a checklist.

if you cannot articulate the goal clearly enough for an AI agent to act on it, you could not articulate it clearly enough for your team either. AI just makes the gap visible.

this is where leverage inverts. coordination costs scale non-linearly with headcount. every additional person adds alignment overhead; another opinion, another context switch. agents carry zero coordination cost. one sharp operator orchestrating a fleet of agents can now cover surface area that previously required a team of five to ten. the unit of leverage shifts from team size to individual clarity. the locus of power moves from span of control to strength of judgment.

if you are staffing teams the way you did three years ago, you are almost certainly overstaffed on execution and understaffed on ownership.

the constraint is no longer "how many people can we throw at this?" the constraint is "do we have someone who actually owns this and knows what good looks like?"

## bad judgment scales faster

there is a darker side, and it deserves more than a passing mention.

when execution becomes cheap, a founder with a wrong mental model of their customer ships the wrong product in a week instead of a quarter, and builds three more features on top of it before anyone catches the mistake. when iteration accelerates, a team optimizing for a vanity metric automates itself into a local maximum at unprecedented speed. the feedback loops that used to exist, the engineer pushing back during sprint planning, the pm asking "are we sure about this?" in a grooming session, those were features of the coordination layer, not bugs. they created natural checkpoints where bad ideas could die.

strip away those checkpoints and you are left with whatever judgment sits at the center, running at full speed with no friction.

a brilliant operator with sharp instincts becomes terrifyingly effective.

a mediocre one causes damage at a rate that was previously impossible.

strategic mistakes no longer announce themselves through slow delivery. they announce themselves through fast delivery of the wrong thing. the failure mode of the agentic era isn't "we couldn't build it." it's "we built it perfectly and it didn't matter."

this means the selection pressure on leadership judgment is about to intensify dramatically. organizations that invest in developing taste, strategic clarity, and deep customer understanding will compound those advantages. organizations that just hand agents to people with shallow models of the problem will compound their mistakes.

## what was load-bearing

AI is dissolving the process layer.

process was the operating system for humans. it scheduled tasks, allocated resources, handled context switching. AI is taking over scheduling and allocation. what matters now is the application logic, the intent, the product.

AI does not eliminate organizations. it removes excuses. and it removes the buffer that once existed between the quality of your judgment and the consequences of acting on it.

what's left is what was always there: people, their judgment, their ownership, and their ability to define a goal and drive toward it. the difference is that now there is nothing standing between that judgment and its outcomes. no process to blame, no coordination to hide behind, no pipeline to absorb the impact of a bad decision.

the organizations that thrive will be the ones that understood this before AI forced the question.

the rest will find out the hard way, and they'll find out fast.

---


**作者** Kirk Marple（@KirkMarple）  
**貼文連結** https://x.com/KirkMarple/status/2028285391850426388  

**正文**

So much gold here. 

Hadn’t read it in-depth until today, and it overlaps with a ton of my learnings in this space - but I also learned a lot too.

---


**作者** Ray Wang（@wangray）  
**貼文連結** https://x.com/wangray/status/2028132386756780220  

**正文**

## OpenAI 内部有个团队，5 个月，3 个工程师，几乎不靠手写代码，做出了一个内部产品。

约 100 万行代码，约 1500 个 PR，人均每天 3.5 个 PR。

这是什么概念？

正常工程师一天能稳定交付一个 PR，已经算高效。3.5 个 PR，意味着产出被直接拉高到了另一个数量级。更夸张的是，这些代码大部分都不是工程师亲手敲出来的。

![Article Image](<https://pbs.twimg.com/media/HCVdNkmasAAUVZQ.png>)

这篇文章是 OpenAI 工程师写的，讲他们怎么用 Codex 从零构建一个叫 Harness 的内部工具。读完之后，我沉默了挺久。

因为它把一件正在发生的事，讲得非常清楚：

工程师的核心工作，正在从写代码，转向设计让 Agent 持续工作的环境。

这句话很重要。

这不是一句夸张的口号，也不是某种抽象比喻。它描述的是一个已经开始发生的角色迁移。

## 他们实际在做什么？

这 3 个工程师，日常工作的重点并不是埋头写实现，而是三件事：

- 把需求拆成 Agent 可以执行的任务。
- 把上下文整理成 Agent 能理解的环境。
- 把反馈机制搭出来，让 Agent 的输出可以被验证、被纠正、被持续改进。

写代码当然还在发生。只是它已经不再是最稀缺、最核心的那部分工作。

你依然得很懂代码，才能把任务拆对，才能判断输出质量，才能设计出靠谱的约束。只是执行层面的编码，越来越多地交给了 Agent。

单次运行可以持续 6 小时。他们睡觉的时候，Agent 还在跑任务。

我自己这一个月用 OpenClaw 管理多 Agent 协作，感受也越来越强烈。

人的价值，越来越集中在调度、约束、验证、纠偏这些环节。真正拉开效率差距的，往往不是你给 Agent 下了一个多聪明的命令，而是你有没有把它工作的环境搭好。

## AGENTS.md 的正确用法

他们的结论很值得记一下：

AGENTS.md 不要写成百科全书。更好的写法，是控制在大约 100 行左右，当成一个目录和路由系统，用来指向更详细的文档。

道理很简单。

Agent 需要的不是在一个文件里读完所有信息。Agent 需要的是在最短路径里找到正确的信息。

我在 OpenClaw 里维护的 AGENTS.md，也是这个逻辑。Ogilvy 的 AGENTS.md 大概 60 行，每一行都在做路由：

- NOW.md 看优先级。
- MEMORY.md 看长期积累。
- content-playbook.md 看内容策略。

Agent 读 AGENTS.md，不是为了在这一页里理解全部事情。它要的是知道下一步该去哪里读，去哪里拿到完成任务真正需要的上下文。

## “Agent 看不到的，等于不存在”

这是我觉得整篇文章里最重要的一句话。

所有关键知识，都必须编码进 repo。

如果一个设计决策只存在于某条 Slack 消息里，或者只存在于某个工程师的脑子里，Agent 就永远不会知道。

对人来说，很多缺失的信息可以靠常识补，可以问同事，可以凭经验猜，可以从语境里推断。

对 Agent 来说，它只能使用它看得到的东西。

所以，一个能让 Agent 高效工作的 repo，必须尽量接近一个完整、自解释、可追踪的系统。知识、约束、历史判断、输出格式、验证方法，都要尽量显式化。

我最近一直在维护 memory/ 目录，存放 Agent 的长期上下文，本质上也是同一个逻辑。

每次 Agent 完成任务，重要的判断、经验、偏差、修正，都要写回去。否则下次它又会从零开始。你以为它“学过了”，其实它根本没记住。

## 用 linter 机械化强制架构

他们还有一个很关键的做法：用 linter 和 CI 去强制执行架构规范，不靠人盯。

这个逻辑非常清楚。

Agent 生成代码的速度太快，人工 review 很容易跟不上。很多原来靠资深工程师肉眼发现的问题，到了 agent-first 的工作流里，已经不适合继续靠人力兜底。

最好的办法，是把规范直接写进系统里。

- 哪些目录可以引用哪些模块。
- 哪些模式允许出现。
- 哪些约束不能破。
- 哪些格式必须通过。

全部交给 linter、CI、自动检查去执行。

只要不符合规范，系统直接报错。这样不会漏，也不需要依赖某个人时刻保持警觉。

背后的原则其实很简单：

凡是可以机械化的质量控制，都应该尽量机械化。

人的注意力应该留给那些只有人能做判断的事情。

## 垃圾回收是必须的

这一点很容易被忽视，但我觉得它极其重要。

Agent 会复制 repo 里已有的模式。好的会复制，坏的也会复制。

如果 repo 里有一个写得不好的函数，在过去，它可能只是一个局部问题。

Agent 介入之后，它会参考这个函数继续生成类似实现。

- 新生成的实现又会变成新的参考
- 然后坏模式开始扩散
- 这个过程会越来越快

所以他们专门做“垃圾回收”，定期清理 repo 里的坏模式。

这个动作，表面看像在打扫卫生。实际上，它是在阻止错误模板在整个系统里增殖。

我在用 Agent 维护内容系统的时候，也遇到过同样的问题。

如果 Agent 早期形成了一个错误判断，而我没有及时纠正，它后面就会把这个错误当成参考，再往外复制。等你发现的时候，偏差已经扩散到多个任务里了。

所以定期清理，往往比事后修补便宜得多。

## 这意味着什么？

3 个工程师能撬动 100 万行代码，重点不在“Agent 把工程师替掉了”。

真正发生的事情是，工程师的杠杆变了。

过去，工程师的产出更多取决于自己亲手写了多少。

现在，工程师的产出越来越取决于他能不能把 Agent 的执行环境设计好。

- 清晰的 AGENTS.md
- 完整的 memory 文件
- 明确的输出规范
- 可验证的 feedback 机制
- 自动化的 lint 和 CI
- 定期做垃圾回收，清掉坏模式

这些东西搭好了，Agent 就能持续跑，持续产出，持续逼近更高质量。

这些东西没搭好，就算 Agent 很强，你也会把大量时间花在纠偏、返工、补漏洞上。

这和管理人其实很像。

环境清楚，规则清楚，反馈清楚，优秀执行者才会不断放大价值。

区别在于，Agent 对环境的依赖更彻底。因为它没有真正意义上的常识，也不会自动替你补漏。你没有写进去的东西，它就很可能永远不会知道。

## 结尾

OpenAI 这 3 个工程师，用 5 个月证明了一件事：

未来最值钱的工程师，未必是写代码最快的人。更可能是最会把知识、约束和反馈，整理成 Agent 可执行环境的人。

这已经不是未来判断。

这件事，已经开始发生了。

接下来真正该问的问题，也很清楚：

我有没有把我的知识、规范、流程和反馈，整理成一个 Agent 能持续工作的系统。

---


**作者** Matt Stockton（@mstockton）  
**貼文連結** https://x.com/mstockton/status/2028186926784647234  

**正文**

This is another well-written article from @ashpreetbedi at Agno. There are a bunch of great agent frameworks SDKs out there (Agno, DeepAgents, Claude Agents SDK, etc.) but there is a *ton* you need to do beyond just building the agent to have it work in a production environment, particularly if you have lots of different users interacting with it. A lot of the skills we learned in ‘classical software engineering’ are very portable to this new task - which is great news if you are coming in with experience. There are some differences and nuances for sure thought. I think this article gives a good high level view of the important areas to consider

---


**作者** mars（@marsBuilds）  
**貼文連結** https://x.com/marsBuilds/status/2028148920895889698  

**正文**

many people think Cursor just sends your prompt directly to the foundational model APIs…

In reality there is this whole proprietary infra setup that ensures you get a better response and faster than you would have from just directly sending the prompt to the models

---


**作者** Ashpreet Bedi（@ashpreetbedi）  
**貼文連結** https://x.com/ashpreetbedi/status/2028176285575594465  

**正文**

> Note: this post is about building your own agents (agentic software engineering), not about using coding agents.

By now you've probably used a few agents, or at least heard of Claude Code, Codex, or OpenClaw. Ever wondered what it takes to build your own?

Most people think of agents as prompts + tools in a loop. That's a reasonable assumption, but it's not production architecture. 

The moment your agent needs to know who it's talking to, maintain state, handle concurrent requests, take sensitive actions, and survive failing tool calls, it stops being an "LLM + tools" and becomes a distributed system.

Building agents is the easy part. There are 75 frameworks that help you do that. The hard part is the runtime: the harness around the agent that makes it work in the real world. That's what agentic software engineering is all about.

# Build. Serve. Connect.

Here's how I think about shipping agentic software.

1. Build the agent. Define the model, tools, knowledge base, memory, storage, and guardrails. This is the layer that most frameworks give you.
1. Serve it as an API. User-scoped, session-scoped, horizontally scalable. Add persistent storage, streaming, background execution, retry semantics. This is where most agentic products stall. Not because the agent doesn't work, but because it doesn't have the infrastructure around it to work reliably at scale.
1. Connect it to where users live. Your product, Slack, Discord, MCP, wherever. An agent in a notebook is an experiment. An agent where your users are is a product.

## The 6 Pillars of Agentic Software

Building an agent is AI engineering. Running it in production is software engineering. Together, they form agentic software engineering: the practice of building, running, and scaling agents as production services. 

Here are the six pillars that hold it up:

1. Durability. Agents reason across multiple steps, call tools that time out, and fail halfway through. If your agent crashes on step 12 of 15, restarting might duplicate a side effect or lose critical context. Agentic software needs to pause, resume, checkpoint, and recover gracefully. Durability turns failure into resumption, not a full restart.
1. Isolation. Agentic software serves thousands of users simultaneously. Each user needs their own session, their own memory, their own context. Passing a user\_id with each request is easy. Isolating every resource the agent touches is where the engineering comes in. Your database, your vector store, your model provider, all need to respect user boundaries. One missing filter becomes a data breach.
1. Governance. Agents that can act can also cause damage. Looking up a record is harmless. Deleting a record or issuing a refund needs approval. Agentic software needs layered authority: what runs automatically, what needs human approval, and what needs admin sign-off. Today, most agents auto-execute with minimal oversight. As they get more capable, governance becomes the product.
1. Persistence. An agent without persistent storage can't learn, can't build context, can't improve. We need to store sessions, memory, knowledge in a database. Persistent state is what turns a chatbot into a product. Every conversation makes the next one better.
1. Scale. A thousand users hit your agent at the same time. Requests queue, you hit model rate limits, and tool calls compete for resources. Traditional services call your own backends. Agentic software calls external model APIs and third-party tools, which means you inherit their rate limits, latency, and downtime. Scaling agentic software means scaling around dependencies you don't control.
1. Composability. When an agent is a service, other agents can call it. Your frontend can call it. Your Slack bot can call it. MCP clients can discover it. It becomes a building block in your architecture, and every new integration becomes a standard API call. That's how single-agent tools become multi-agent systems.

None of this is new. We've been building reliable distributed systems for decades. The AI industry just hasn't brought those lessons along yet, and we're feeling it in every failed deployment.

## From Theory to Practice

As always, I come bearing code. Here's how you can start building your own agentic service today. 

This gives you a containerized service with persistent storage (Postgres), two starter agents (a knowledge agent using Agentic RAG and an MCP agent for external tool use), and a REST API you can connect to from anywhere.

I'm using Docker for this template because Docker runs everywhere: your laptop, AWS, GCP, Azure, Railway. The same container you develop locally is the one you deploy to production. The [README](<https://github.com/agno-agi/agentos-docker-template>) covers everything you need to get started. 

After running the service:

1. Open http://localhost:8000/docs to see your API. 
1. Connect to the web UI at [os.agno.com](<https://os.agno.com>) where you can chat with your agents, trace runs, manage knowledge, create schedules and approve sensitive tool calls. One UI for your agentic software.

Adding your own agent is a few lines of Python and a restart. Swap models with a one-line change. Add tools from 100+ integrations. The template is a starting point. Read the [Agno docs](<https://docs.agno.com/introduction>) to learn more.

## Governance & Elicitation

Most agents run tool calls with minimal oversight or auditability. In practice, we need layered authority:

1. Tools that run freely
1. Tools that need user approval
1. Tools that need admin approval

Agents also need to ask questions (often called elicitation). The Claude Code team shared a [great article](<https://x.com/trq212/status/2027463795355095314>) on the AskUserQuestion tool used by Claude. 

This is available in Agno as \`UserFeedbackTools\`. Here's a support agent that can look up orders freely, ask the customer structured questions when it needs more information, and waits for user approval before issuing a refund:

Watch what happens when a customer asks for a refund. 

- The agent looks up the order on its own, no permission needed. 
- Then it hits a decision point: why does the customer want the refund?
- Instead of guessing, it presents a structured question with clear options: defective, wrong item, changed mind. 
- The customer picks one. Now the agent calls the refund tool, but because refunds carry real consequences, it pauses for user approval. 
- Once approved, the agent runs the refund tool.

Three levels of agency in one conversation. You can view the [full code here](<https://github.com/agno-agi/demo/tree/main/agents/support>).

The agent knows when to act, when to ask, and when to wait. That's what governance looks like in practice. The runtime has to support all three modes, and the transitions between them have to feel natural.

> Note: the approvals flow on the UI is actively being developed. The refund should wait for admin approval, not user approval. This is implemented on the SDK but not the UI yet. This is being fixed this week.

## Agents are distributed systems

The [5 Levels](<https://x.com/ashpreetbedi/status/2024885969250394191>) describe how agentic software grows in capability (and complexity). The [7 Sins](<https://x.com/ashpreetbedi/status/2026708881972535724>) describe how they fail in production. The 6 Pillars describe what it takes to build them right.

The consistent message across all three: agentic software engineering is a discipline. The teams that internalize this early will ship great products. The teams that keep treating agents as scripts will continue to miss the mark.

Clone the [repo](<https://github.com/agno-agi/agentos-docker-template>). Build your first agent. Ship it where your users are.

Links

- [Agno Docs](<https://docs.agno.com/>)
- [Agno Github](<https://github.com/agno-agi/agno>)
- [AgentOS Templates](<https://docs.agno.com/deploy>)
- [AgentOS Docker Template](<https://github.com/agno-agi/agentos-docker-template>)

---


**作者** DAIR.AI（@dair_ai）  
**貼文連結** https://x.com/dair_ai/status/2028094014235213898  

**正文**

The Top AI Papers of the Week (February 23 - March 1)

## 1. Deep-Thinking Tokens

![Article Image](<https://pbs.twimg.com/media/HCSrDfQXYAAdJJn.png>)

Google researchers challenge the assumption that longer outputs indicate better reasoning. They introduce deep-thinking tokens, a metric that identifies tokens where internal model predictions shift significantly across layers before stabilizing. Unlike raw token count, which negatively correlates with accuracy (r = -0.59), the deep-thinking ratio shows a robust positive correlation (r = 0.683).

- Deep-thinking ratio as a reasoning signal: For each generated token, intermediate-layer distributions are compared to the final-layer distribution using Jensen-Shannon divergence. A token qualifies as deep-thinking if its prediction only stabilizes in the final 15% of layers. This captures genuine computational effort rather than surface-level verbosity.
- Think@n test-time scaling: The authors introduce Think@n, a strategy that prioritizes samples with high deep-thinking ratios. It matches or exceeds standard self-consistency performance while cutting inference costs by approximately 50% through early rejection of unpromising generations based on just 50-token prefixes.
- Benchmark validation: Evaluated across AIME 24/25, HMMT 25, and GPQA-diamond with reasoning models including GPT-OSS, DeepSeek-R1, and Qwen3. The deep-thinking ratio consistently outperforms length-based and confidence-based baselines as a predictor of correctness.
- Practical implications: This reframes how we think about test-time compute. Instead of generating more tokens, we should focus on generating tokens that require deeper internal computation, enabling more efficient and accurate reasoning.

[Paper](<https://arxiv.org/abs/2602.13517>) | [Tweet](<https://x.com/omarsar0/status/2025239354327924833>)

## 2. Codified Context

![Article Image](<https://pbs.twimg.com/media/HCSrGq4bEAIInTk.jpg>)

Single-file AGENTS.md manifests don't scale beyond modest codebases. A 1,000-line prototype can be fully described in a single prompt, but a 100,000-line system cannot. This paper presents a three-component codified context infrastructure developed during construction of a 108,000-line C# distributed system, evaluated across 283 development sessions.

- Hot-memory constitution: A living document encoding conventions, retrieval hooks, and orchestration protocols that the agent consults at the start of every session. This provides immediate awareness of project standards without requiring the agent to rediscover them through exploration.
- Domain-expert agents: 19 specialized agents, each owning a bounded domain of the codebase with its own context slice. Instead of one generalist agent trying to hold the entire project in context, tasks are routed to the agent with the deepest knowledge of the relevant subsystem.
- Cold-memory knowledge base: 34 on-demand specification documents that agents retrieve only when needed. This tiered approach keeps the active context lean while ensuring detailed specifications are always accessible for complex implementation decisions.
- Session continuity results: Across 283 sessions, the infrastructure demonstrates how context propagates between sessions, preventing the common pattern where agents forget conventions, repeat known mistakes, and lose coherence on long-running projects.

[Paper](<https://arxiv.org/abs/2602.20478>) | [Tweet](<https://x.com/omarsar0/status/2027770787659464812>)

## 3. Discovering Multi-Agent Learning Algorithms with LLMs

![Article Image](<https://pbs.twimg.com/media/HCSrIm5XoAA1AJ_.png>)

Google DeepMind uses AlphaEvolve, an evolutionary coding agent powered by LLMs, to automatically discover new multi-agent learning algorithms for imperfect-information games. Rather than relying on manual algorithm design, the system navigates vast algorithmic design spaces and discovers non-intuitive mechanisms that outperform state-of-the-art baselines.

- VAD-CFR discovery: The system discovers a novel variant of iterative regret minimization featuring volatility-sensitive discounting and consistency-enforced optimism. VAD-CFR outperforms existing baselines like Discounted Predictive CFR+ on standard imperfect-information game benchmarks.
- SHOR-PSRO discovery: A population-based training algorithm variant that introduces a hybrid meta-solver blending Optimistic Regret Matching with temperature-controlled strategy distributions. This automates the transition from diversity exploration to equilibrium convergence.
- LLM-driven algorithmic evolution: AlphaEvolve generates candidate algorithm modifications, evaluates them on game-theoretic benchmarks, and iteratively refines the best variants. The discovered algorithms contain novel design choices that human researchers had not previously considered.
- Broader implications: This demonstrates that LLMs can serve as algorithmic designers, not just code generators. The approach could extend to discovering algorithms in other domains like optimization, scheduling, and resource allocation.

[Paper](<https://arxiv.org/abs/2602.16928>) | [Tweet](<https://x.com/omarsar0/status/2026044154040742150>)

## 4. Evaluating AGENTS.md

![Article Image](<https://pbs.twimg.com/media/HCSrNn4XMAA51eE.png>)

This research evaluates whether AGENTS.md files, the repository-level context files that developers write to help AI coding agents understand their codebases, actually improve agent performance. Testing four coding agents (Claude Code with Sonnet-4.5, Codex with GPT-5.2 and GPT-5.1 mini, and Qwen Code with Qwen3-30b-coder), the findings are counterintuitive.

- Context files reduce success rates: Human-written AGENTS.md files provide a modest +4% improvement in some cases, but LLM-generated ones actually hurt performance by -2%. Both consistently increase inference cost by over 20%, making the cost-benefit tradeoff questionable.
- Broader exploration, worse outcomes: Context files cause agents to explore more code paths and consider more files, but this expansive behavior makes tasks harder rather than easier. The additional context introduces noise that dilutes task-relevant information.
- Lean is better: The study recommends that developer-written context files should contain only essential information. Unnecessary requirements, coding style preferences, and broad architectural descriptions complicate agent task completion without improving results.
- Practical guidance: For developers maintaining AGENTS.md files, the key takeaway is to keep them minimal and focused on critical constraints. Information density matters more than comprehensiveness for current coding agents.

[Paper](<https://arxiv.org/abs/2602.11988>) | [Tweet](<https://x.com/omarsar0/status/2026306141181898887>)

## 5. PAHF

![Article Image](<https://pbs.twimg.com/media/HCSrPiJaAAAJ82i.jpg>)

Meta introduces PAHF (Personalized Agents from Human Feedback), a continual agent personalization framework that addresses a critical gap: most AI agents cannot adapt to individual user preferences that evolve over time. PAHF couples explicit per-user memory with both proactive and reactive feedback mechanisms.

- Three-step personalization loop: PAHF operates through (1) pre-action clarification to resolve ambiguity before acting, (2) grounding actions in preferences retrieved from persistent memory, and (3) integrating post-action feedback to update memory when preferences drift. This dual-feedback design captures both explicit and implicit signals.
- Continual learning through interaction: Unlike static fine-tuning approaches, PAHF enables agents to learn from live interactions. The explicit memory store allows agents to accumulate and revise user preference profiles without retraining, making personalization practical for production deployments.
- Novel benchmarks: The researchers develop two benchmarks in embodied manipulation and online shopping that specifically measure an agent's ability to learn initial preferences from scratch and then adapt when those preferences shift over time.
- Strong results: PAHF learns substantially faster and consistently outperforms both no-memory and single-channel baselines. It reduces initial personalization error and enables rapid adaptation to persona shifts, demonstrating that the combination of memory and dual feedback channels is essential.

[Paper](<https://arxiv.org/abs/2602.16173>) | [Tweet](<https://x.com/dair_ai/status/2025242624790331520>)

## 6. Doc-to-LoRA

![Article Image](<https://pbs.twimg.com/media/HCSrRE0XEAUUxGk.jpg>)

Sakana AI introduces Doc-to-LoRA (D2L), a lightweight hypernetwork that meta-learns to compress long documents into LoRA adapters in a single forward pass. Instead of processing long contexts through expensive quadratic attention, D2L converts the document into parameter-space representations that the target LLM can use without re-consuming the original text.

- Single-pass context compression: D2L generates LoRA adapters from unseen documents in one forward pass. Once compressed, subsequent queries are handled using only the adapter weights, eliminating the need to re-process the full document and dramatically reducing both inference latency and KV-cache memory demands.
- Beyond native context windows: The method achieves near-perfect zero-shot accuracy on needle-in-a-haystack tasks at sequence lengths exceeding the target LLM's native context window by over 4x. This suggests that parametric compression can effectively extend context capabilities without architectural changes.
- Real-world QA performance: On practical question-answering datasets, D2L outperforms standard long-context approaches while consuming less memory. The compressed representations retain enough information for accurate retrieval and reasoning across the full document.
- Practical deployment benefits: For applications requiring repeated queries over the same document (customer support, legal analysis, codebase understanding), D2L compresses the document once and amortizes the cost across all subsequent interactions.

[Paper](<https://arxiv.org/abs/2602.15902>) | [Tweet](<https://x.com/omarsar0/status/2027385998993420571>)

## 7. AgentConductor

![Article Image](<https://pbs.twimg.com/media/HCSrS-6WYAAuYfp.jpg>)

AgentConductor introduces a reinforcement learning-enhanced multi-agent system for code generation that dynamically generates interaction topologies based on task characteristics. Rather than using fixed communication patterns between agents, an LLM-based orchestrator adapts the topology to match problem complexity, achieving state-of-the-art accuracy across five code generation datasets.

- Task-adapted topologies: The orchestrator constructs density-aware layered directed acyclic graph (DAG) topologies tailored to problem difficulty. Simple problems get sparse topologies with minimal communication overhead, while complex problems get denser multi-agent collaboration.
- Topological density control: A novel density function and difficulty interval partitioning mechanism controls how much agents communicate. This directly addresses the problem of redundant interactions that waste tokens without improving solution quality.
- Strong performance gains: AgentConductor outperforms the strongest baseline by up to 14.6% in pass@1 accuracy with 13% density reduction and 68% token cost reduction. The system achieves better results while using significantly fewer computational resources.
- Execution feedback refinement: Topologies are refined using execution feedback from code tests. When initial solutions fail, the orchestrator adjusts the collaboration structure based on error patterns, enabling adaptive recovery.

[Paper](<https://arxiv.org/abs/2602.17100>) | [Tweet](<https://x.com/dair_ai/status/2027030406441341227>)

## 8. ActionEngine

Georgia Tech and Microsoft Research introduce ActionEngine, a training-free framework that transforms GUI agents from reactive step-by-step executors into programmatic planners. It builds a state-machine memory through offline exploration, then synthesizes executable Python programs for task completion, achieving 95% success on Reddit tasks from WebArena with on average a single LLM call, reducing costs by 11.8x and latency by 2x compared to vision-only baselines.

[Paper](<https://arxiv.org/abs/2602.20502>) | [Tweet](<https://x.com/dair_ai/status/2026678090815123594>)

## 9. CoT Faithfulness via REMUL

Researchers propose REMUL, a training approach for making chain-of-thought reasoning more faithful and monitorable. A speaker model generates reasoning traces that multiple listener models attempt to follow and complete, using RL to reward reasoning that is understandable to other models. Tested across BIG-Bench Extra Hard, MuSR, ZebraLogicBench, and FOLIO, REMUL improves three faithfulness metrics while also boosting overall accuracy, producing shorter and more direct reasoning chains.

[Paper](<https://arxiv.org/abs/2602.16154>) | [Tweet](<https://x.com/dair_ai/status/2026043400861122709>)

## 10. Learning to Rewrite Tool Descriptions

Intuit AI Research addresses a bottleneck in LLM-agent tool use: tool descriptions are written for humans, not agents. They introduce Trace-Free+, a curriculum learning framework that optimizes tool descriptions without relying on execution traces. The approach delivers consistent gains on unseen tools, strong cross-domain generalization, and robustness as the number of candidate tools scales to over 100, demonstrating that improving tool interfaces is a practical complement to agent fine-tuning.

[Paper](<https://arxiv.org/abs/2602.20426>) | [Tweet](<https://x.com/omarsar0/status/2026676835539628465>)

---


**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2028046829250920515  

**正文**

2月28日凌晨，美国和以色列联合对伊朗发动了代号"Epic Fury"的大规模空袭行动。

据《华尔街日报》报道，包括美国中央司令部在内的多个军事指挥部，在对伊朗的空袭行动中依然使用了Anthropic的Claude AI系统，用于情报评估、目标识别和战场场景模拟。

一个极其讽刺的细节是：就在数小时前，特朗普刚刚下令所有联邦机构"立即停止"使用Anthropic的技术，国防部长赫格塞斯也将这家AI公司列为"国家安全供应链风险"。

禁了，但又没完全禁。这不是一个段子，而是AI时代军事依赖的真实写照。

## 时间线：48小时内发生了什么

要理解这件事的荒诞性，需要先把密集发生的事件按时间排列：

2月27日（周五）下午5:01，五角大楼给Anthropic设定的最后通牒到期。Anthropic拒绝妥协，坚持不允许Claude被用于大规模监控美国公民或完全自主武器系统。

2月27日（周五）傍晚，特朗普在Truth Social上发帖："我命令美国政府的每一个联邦机构立即停止使用Anthropic的技术。我们不需要它，我们不想要它，也不会再和他们做生意！"随后赫格塞斯宣布将Anthropic列为"供应链风险"，这个标签通常只用于华为、卡巴斯基这类与外国对手有关联的公司。

2月27日（周五）深夜，OpenAI的CEO Sam Altman宣布，OpenAI已与国防部达成协议，将其模型部署到保密网络。

2月28日（周六）凌晨，美国和以色列对伊朗发动大规模空袭。特朗普随后宣称伊朗最高领袖哈梅内伊已在空袭中身亡。

2月28日（周六），《华尔街日报》在其伊朗空袭实时报道中披露：美军在此次行动中使用了Anthropic的Claude。

## Anthropic的AI到底在军事中扮演什么角色

这不是Claude第一次出现在美军的军事行动中。

早在1月份，美军特种部队突袭委内瑞拉抓捕前总统马杜罗的行动中，Claude就已经被使用。当时《华尔街日报》首次披露，Claude通过Anthropic与数据分析公司Palantir的合作关系，被部署在军方的保密网络上。

Anthropic是唯一一家将AI模型部署到五角大楼保密网络的前沿AI公司。这个事实至关重要，它意味着在最敏感的军事行动中，从武器测试到作战期间的通信，Claude是目前唯一可用的前沿大模型。

根据已有报道，Claude在军事场景中的用途包括：分析卫星图像和情报数据、生成情报评估报告、辅助目标识别、模拟战场场景。这些都属于"辅助决策"的范畴，而不是直接控制武器。但问题在于，"辅助决策"和"参与作战"之间的边界，比很多人想象的要模糊得多。

## Anthropic与五角大楼之争的核心

这场冲突的本质，不是Anthropic反对与军方合作。恰恰相反，Anthropic一直强调自己是第一家将AI部署到保密网络的公司，并且表示愿意继续服务。

争议的焦点非常具体：Anthropic坚持在合同中保留两条"红线"，第一，不允许Claude被用于大规模监控美国公民；第二，不允许Claude被用于完全自主的武器系统（即没有人类参与决策的自动杀伤）。

五角大楼的立场是：军方需要AI工具能够被用于"所有合法用途"，不能由一家私营公司来决定军方能做什么、不能做什么。五角大楼方面也反复强调，他们并不打算用AI做大规模监控或自主武器，但就是不愿意在合同里写明这个限制。

Anthropic CEO Dario Amodei在声明中写道："我们不能凭良心答应他们的要求。"他认为，大规模监控和完全自主武器"超出了当今技术能够安全可靠完成的范围"。

而五角大楼的回应则非常强硬。国防部副部长Emil Michael公开指责Amodei有"上帝情结"，赫格塞斯称Anthropic"傲慢自大"，特朗普则在社交媒体上骂Anthropic是"激进左翼觉醒公司"。

## 行业的连锁反应

这场对峙不只是Anthropic一家的事。

OpenAI的Sam Altman最初表态说，他与Anthropic共享同样的"红线"，反对AI被用于大规模监控和自主武器。他在给员工的备忘录中写道："这不再只是Anthropic和国防部之间的问题，这是整个行业的问题。"

但到了周五晚上，Altman宣布OpenAI已经与五角大楼达成协议。他声称协议中包含了类似的安全原则，但外界无法核实具体条款。CNN指出，目前不清楚OpenAI的协议与Anthropic要求的到底有什么实质区别。

Elon Musk的xAI更早就与五角大楼达成了协议，同意Grok被用于"任何合法用途"。Musk本人在X上多次攻击Anthropic，称这家公司"憎恨西方文明"。

与此同时，来自Google、微软、亚马逊和OpenAI的员工组成了两个联盟，要求各自的雇主效仿Anthropic，拒绝给军方无限制使用AI。

这场争论正在撕裂硅谷：一边是"AI安全优先"的理念，另一边是来自政府和商业的巨大压力。

## 更大的图景：谁来给AI划红线

如果把视角拉远，这个事件折射出的根本问题是：在AI能力飞速增长的时代，谁有权决定AI的使用边界？

过去几十年，军事技术主要由政府实验室和承包商开发，规则由政府制定。但现在，最先进的AI系统掌握在商业公司手中。Anthropic、OpenAI、Google这些公司开发的模型，最初是为消费市场设计的，然后被军方看中。

这造成了一个前所未有的权力博弈：私营公司能否对政府说"不"？

从Anthropic的遭遇来看，答案是：可以说"不"，但代价巨大。被列为"供应链风险"，被禁止与所有军事承包商合作，被总统公开羞辱。这个标签此前只给过华为和卡巴斯基这种被视为外国安全威胁的公司。

Anthropic已经表示将在法庭上挑战这一认定。但不管法律结果如何，信号已经发出：如果你不配合，下一个就是你。

## 这件事为什么值得关注

对于关注AI行业的人来说，这个事件的意义远超一次军事行动或一场商业纠纷。

它揭示了几个不容回避的现实：

AI已经深度嵌入现代战争。从委内瑞拉到伊朗，Claude在不到两个月内参与了两次重大军事行动。这不再是实验室里的假设场景，而是正在发生的事实。

技术依赖比政治表态更有惯性。总统可以在社交媒体上一秒钟发布禁令，但军方对特定技术的依赖不是一纸命令就能解除的。当你的保密网络上只有一个可用的前沿AI模型时，你就被"锁定"了。

AI安全不是一个纯学术问题。Anthropic一直被嘲笑为"AI安全教"，但这次事件证明，关于自主武器和大规模监控的担忧不是杞人忧天。当AI真的被用于轰炸一个国家的时候，"人类是否应该保持在决策回路中"就不再是哲学问题了。

最后一个问题留给所有人思考：在"Epic Fury"行动中，Claude到底做了什么？它是仅仅在帮助分析情报，还是在某种程度上参与了目标选择？如果一个AI系统帮助确定了轰炸目标，而那个目标恰好是一所学校（伊朗官方称一所女子小学被击中，85名儿童遇难），那么这个AI系统的制造者是否需要承担某种责任？

这些问题没有简单的答案。但在Anthropic的Claude已经实际参与战争的今天，我们不能再假装这些问题不存在。

---


**作者** Tony出海（@iamtonyzhu）  
**貼文連結** https://x.com/iamtonyzhu/status/2027555829604618303  

**正文**

非常讨厌Anrhropic的Dario 这个人，

但他是世界上最强AI技术领导者之一。他是早期OpenAI的技术团队领导核心，出去后做的Claude 1比ChatGPT还早，OpenAI 奥特曼只是个商人，没了技术人才，现在一直吃老本，和跟随抄袭。

Dario是技术创业者，就是世界最强AI的引领者。

他说的话就是方向。

1，Claude一直自己定位为工具，去改造各种行业系统，而不是迎合消费者市场。

2，大家做AI产品
Dario 先给了通用建议："要建立护城河，不要只做套壳产品。"只是给 Claude 套个 UI 或者写个提示词模板是没有护城河的，你不需要担心 Anthropic 来吃这个收入，任何人都能吃。

然后他给出了有护城河的方向：生物×AI（“我碰巧是生物学家，但 Anthropic 的大多数人不是”）、金融服务（“有大量监管，需要懂很多东西才能合规”）。这些领域对 Anthropic 来说“效率太低”，不会去做。

3，Nikhil 问：一个 25 岁的年轻人，想在未来十年里在资本主义竞争中赢，该选什么方向？

Dario 给了三个方向。
第一，以人为中心的工作。 涉及与人打交道的职业有更长的跑道。

第二，物理世界相关的工作。 半导体是一个好例子，有“物理世界”和“传统工程”两个 AI 还没完全覆盖的维度。

第三，也是他最强调的：批判性思维。 当 AI 能生成任何内容，图像、视频、文本，分辨真假变得越来越难。

“成功的很大一部分可能就是拥有街头智慧，不被虚假内容骗到。你不想持有错误信念，不想被诈骗。”

他补充说 Anthropic 不做图像和视频生成，“有很多原因，这是其中之一”。

---


**作者** 干物纯今天吃什么（@zty0826）  
**貼文連結** https://x.com/zty0826/status/2027714881206817038  

**正文**

试用过了，非常 cool 且有想象空间的 Agent team 组织形态，之后详细分享一下试用体验。
其实很多工作内容很大程度上已经是一个人肉 A2A 的转发器了。不同项目都用Agent开发，人类负责转发上下游之间的Release Note、Feature request、bug reporting，一个 Agent 和 Human 共建的 IM 可以很好地解决这个问题，且完全有可能不仅仅是解决这个问题，而是真正演化出自己的Agent社群来。

---


**作者** Subah Wadhwani（@subahwadhwani）  
**貼文連結** https://x.com/subahwadhwani/status/2027526010300993796  

**正文**

@tankots (@WisprFlow) did an announcement giving away a Porsche GT3rs on X. [It hit 3.7M+ views](<https://x.com/tankots/status/2025981424470479008>).

@contraben (@contra) launched their payments platform and [got 2.1M views](<https://x.com/contraben/status/2024182864506761617?s=20>).

@Replit introduced their animation feature, [7.1M views](<https://x.com/Replit/status/2024578806208745637?s=20>).

These are not mere coincidences. Without the strategy below, they would've   done 80% worse. 

At atomikgrowth.com, we've built the playbook to replicate those successes, every single time, no matter if you have 0 presence on X.

It all boils down to a science that we deploy for funding announcements and product launches. And I'm giving away every single step below.

## How the X algorithm actually works for launches

X gives every post a tiny test audience in the first 30 to 60 minutes. During that window, the algorithm is measuring one thing: engagement velocity. Retweets, quote tweets, replies, likes, all relative to time.

If the ratio is high enough, the post gets pushed to a significantly larger audience. If it's not, the post dies.

Every step below is engineered to maximize engagement density in that first window.

Step 1: Make a video worth sharing

Nobody engages with a generic product demo or a plain talking-head founder video. The content itself has to do one thing in the first 3 seconds: stop the scroll.

That means showing the product doing something that looks almost unbelievable. Tanay showed that if someone broke his product, he'd give them a Porsche. @Bouazizalex [opened with "We started about 6 years ago, struggling to even make $10K"](<https://x.com/Bouazizalex/status/1978809723727012176?s=20>) before revealing a $300M raise at a $17.3B valuation.

The thread/video is the foundation of the entire campaign. If it doesn't stop the scroll, nothing downstream matters. No amount of influencer coordination will save a boring post.

![Article Image](<https://pbs.twimg.com/media/HCM3oDcakAACGES.jpg>)

Step 2: Find influencers whose audiences are your actual buyers

The standard approach is to get 50 random tech accounts to repost and call it a day. The reach looks fine on paper but doesn't convert because the audience composition is wrong.

What matters is whether the influencer's audience overlaps with your target buyers. If you're launching a devtool, you want influencers followed by CTOs and engineering leads at your target companies. Not random accounts with 100K followers who happen to post about tech developments 10x a day.

We go a step further. We identify influencers who are already followed by a company's actual customers or their peers. Our influencers are followed by Marc Andreessen, Chamath Palihapitiya, Elad Gill, Elon Musk, and Keith Rabois. When those people see your launch through someone they already trust, it carries weight.

![Article Image](<https://pbs.twimg.com/media/HCM3V5jbEAAqA8j.jpg>)

Step 3: Verify before you deploy

Before working with any influencer, you need to verify their audience composition.

Minimum benchmark: 33% of their followers should be in your target market.

A large number of tech accounts look impressive on the surface but their followers are mostly bots or audiences in markets that are completely irrelevant for your launch. An account with 50k verified, relevant followers will outperform one with 500K followers in the wrong geography every time.

Step 4: Write custom copy for every single person

This is a very important step if you want your campaign to look & feel organic.

Every influencer gets their own personalized copy. Matched to their tone and writing style. If someone writes long and thoughtful, we match that. If someone does short punchy takes, we match that.

All copy is written by our in-house copywriters, assisted with Claude. But they're never templated. The client pre-approves every piece before it goes live.

The moment two influencers post something that reads similarly, the campaign can lose credibility.

Step 5: Build promo kits for your founder's inner circle

Every founder has 15 to 20 people who would reshare their launch. Investors. Fellow founders. Friends. Teammates. Their families.

The problem: they're busy. They don't know what to write. So they either don't post or they write something generic like "congrats to the team."

The fix:

Write a custom post for each person, from their perspective.

Investor? Write it as someone sharing why they backed you. Fellow founder? Write it as a peer endorsing the product. Existing customer? Write it from their perspective about how they actually use the product, so it reads like a genuine endorsement, not a favor.

Make it so easy that all they do is copy, paste, post. You'll be surprised how many people do it when the friction is zero.

Step 6: Structure the comment section

The comment section under your main post is prime real estate. The algorithm shows top comments to everyone who sees the post.

If those comments are empty or low quality, you're wasting it.

Have 2 to 3 larger influencer accounts start discussion threads in the comments. Then have smaller accounts reply to those threads with pre-written takes that guide the narrative deeper.

This does two things.

First, it makes the comment section look alive and high-signal. The algorithm sees engagement density and pushes the post further.

Second, it controls the narrative. The first things people see when they click into your post are intelligent, on-topic discussions. They then stay for longer.

Step 7: Improve your hook

What makes someone stop scrolling in the first 3 seconds follows the same principles that work in short-form content.

![Article Image](<https://pbs.twimg.com/media/HCM33v_akAA4eMk.jpg>)

Launch videos on X are becoming increasingly more mass appeal, and the hooks that drive millions of views share the same DNA.

Crazy big numbers. Lead with a number that makes people do a double take. Revenue, valuation, growth rate, users. Be specific and flex, albeit distasteful at times.

Shock factor. Say or show something that breaks expectations. Can be visual or verbal.

Challenges. Publicly challenge your audience to break your product, or something alike.

Celebrities. Feature a recognizable face or name. Doesn't need to be mainstream famous. Think of signing the term sheet with your lead tier 1 GP.

Revolutionary acclaim. Position the product as a category-defining moment. 

Step 8: Have a clear CTA 

Ask people to comment a keyword in exchange for free credits, early access, or more info. This converts viewers into users on the spot and floods the comment section with engagement, which the algorithm rewards.

Step 9: Coordinate everything to hit in the same window

This is the most important step and the one most people fumble.

Everything (quote tweets, comment threads, promo kit reshares, customer endorsements) needs to land within the same 2 to 3 hour window.

20 to 30 posts hitting in the same window is what creates the sense that "everyone is talking about this." That's what triggers the algorithm to treat it as a moment. Our launches hit X's Today's News in under 2 hours.

Best time: mid-morning US Eastern.

Step 10: Track everything

Every impression from every influencer. Every comment. Every repost. Every quote tweet. Track it all.

You should know exactly which influencer drove how many views. Which angle performed best. Which comment threads generated the most engagement.

![Article Image](<https://pbs.twimg.com/media/HCM3-C8bYAAp-Xi.jpg>)

A note on LinkedIn

People always ask about cross-posting the launch video to LinkedIn.

LinkedIn impressions are wildly unpredictable. A video can do 100K views one day and 10K the next.

The only thing that consistently works is a genuinely engaging video that stands on its own.

If you have that, try it. If not, don't split your energy. Go full throttle on X. LinkedIn is a bonus.

The short version

1. Make a video that hooks in 3 seconds.
1. Find influencers whose audiences are your actual buyers.
1. Write custom copy for every person in their voice.
1. Build promo kits for your founder's network and customers.
1. Structure the comment section.
1. Time everything to hit in the same 2 to 3 hour window.
1. Track every data point.

That's how to win X.

That's how funding announcements go from 500 views to millions.

---


**作者** yibie（@yibie）  
**貼文連結** https://x.com/yibie/status/2027928136172867619  

**正文**

非常向大家推荐 @simonw 的 Agentic Engineering Patterns，这是他使用大模型开发过程中总结的工程经验，我总结了他所说的要点：

一、核心理念原则
----------------

1. Code is cheap now（代码现在很廉价）
   - 编写初始工作代码的成本已降至几乎为零
   - 但交付"好代码"仍然昂贵（测试、文档、错误处理等）
   - 行动规则：每当直觉说"不值得花时间做"时，先让 agent 试试，最坏情况只是浪费一点 token

2. Hoard things you know how to do（囤积你知道怎么做的东西）
   - 收集解决方案（blog、GitHub repos、HTML tools）
   - 建立可运行的代码片段库
   - 关键模式：让 agent 组合两个或多个现有工作示例来构建新东西

二、测试与质量保证
------------------

3. Red/green TDD（红/绿测试驱动开发）
   - 提示词："Use red/green TDD"
   - 模型理解：先写测试 → 确认测试失败（红）→ 实现代码 → 确认测试通过（绿）
   - 防止 agent 写无效代码或过度工程

4. First run the tests（先运行测试）
   - 新 session 的第一条提示："Run the tests to confirm they pass, then summarize what the test suite tells you about the project"
   - 作用：
     * 确认测试套件存在
     * 了解项目规模/复杂度
     * 建立测试心态

三、代码理解模式
----------------

5. Linear walkthroughs（线性代码走读）
   - 场景：需要理解现有代码（他人代码、自己遗忘的代码、vibe coded 代码）
   - 提示词模板：让 agent 创建结构化文档，解释代码如何工作
   - 使用 Showboat 工具记录走读过程

6. Interactive explanations（交互式解释）
   - 当代码成为"认知债务"时需要偿还
   - 让 agent 创建动画/交互式演示来解释算法
   - 示例：词云算法用动画展示螺旋放置过程

四、Prompt 工程技巧
-------------------

7. Artifacts 开发配置
   - 禁用 React（需要构建步骤）
   - 强制使用 vanilla HTML/JS：单个文件、可粘贴到静态托管

五、关键洞察总结
----------------

传统开发 vs Agentic Engineering：

- 代码成本：昂贵（一天几百行）→ 廉价（几乎免费）
- 好代码成本：昂贵 → 仍然昂贵
- 并行能力：单线程 → 多线程（同时做多件事）
- 学习模式：手动阅读文档 → 让 agent 解释并生成交互式演示
- 代码囤积：笔记/收藏夹 → 可运行的代码仓库 + HTML tools

最重要的原则：
"Delivering new code has dropped in price to almost free... 
but delivering good code remains significantly more expensive than that."

实践建议：
1. 培养"囤积"习惯——收集可运行的解决方案
2. 任何任务先让 agent 尝试，再判断是否值得继续
3. 测试不再是可选项，而是必需
4. 用 agent 生成代码解释来偿还"认知债务"

非常建议大家到原网址细细阅读，有很多深入的细节，值得品味：https://simonwillison.net/guides/agentic-engineering-patterns

---


**作者** ᴅᴀɴɪᴇʟ ᴍɪᴇssʟᴇʀ 🛡️（@DanielMiessler）  
**貼文連結** https://x.com/DanielMiessler/status/2027734353871298632  

**正文**

I'm going to try to encapsulate a whole bunch of stuff that's going on right now and wrap it into a single container. It's actually very difficult to do because there's so much change, and things are getting crazier every single week, every single day almost.

I've noticed a whole bunch of transitions happening at the same time, and I'm calling it the great transition. It's really many smaller transitions, but they have a theme and a direction. And I think I know roughly where they're going.

What I want to give you is something where if you think about all of these ideas and just let them stew, the news that comes out over the next weeks, months, even years will just make more sense. You can put it into this container, this mental model of thinking about things.

## Knowledge goes from private to public [​](<https://danielmiessler.com/blog/the-great-transition#knowledge-goes-from-private-to-public>)

There are a few different things making this happen. One is just LLMs in general, AI in general. The concept is that it consumes all the stuff from the internet—all the books, all the blogs, forum conversations—all this training that's been done on these models. All of that condenses into a model that's kind of representative of all this knowledge. Everybody kind of knows that already.

What's not so much understood is what this is actually doing to knowledge work.

In the past, going back 10, 20, 30, 50 years, if you were an expert in something, you had knowledge that no one else had. If you were a specialist consultant at McKinsey or you were a heart doctor or whatever, you had special knowledge. And you hadn't captured even a 10th of it. Let's say you've written two books—you still haven't captured a 10th of your knowledge. You just know things that other people don't. If you're a security professional who's been doing this for 20 years, you just understand things. If you're a CISO that's done this multiple times, you just understand things and get things that nobody else has. And importantly, it's not in a book somewhere. Even if you've written books, your knowledge is still not fully in the books.

That has always protected smart people—the ones with both the smarts and the experience. That combination has made them very special.

What is happening now is completely changing that.

🧠[ Skill](<https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/skills>)s—folders of markdown files—are how specialized knowledge gets captured and made portable.

Especially with skills—this whole concept that [Anthropic](<https://www.anthropic.com/>) came up with. We're talking about a folder full of markdown files that can encapsulate a decent amount of your knowledge. You still have the capture problem where they don't know exactly what to say, how to capture it, but here's the situation: many, many smart people are producing skills and many, many other smart people are going to collect specialized knowledge from all over the internet, anywhere it's been written down, and bring that into a skill. Plus all these specialist people—they're writing books, doing presentations, writing blogs, doing interviews, doing podcasts.

In the past we'd never had a system that could basically say, go get all of that. Go get everything Dr. Huberman has ever said about health or morning routines, bring it all together and turn that into a skill. This is one prompt. Find everything Huberman has said about morning routines from every podcast, every blog, every article, every interview and put that into a skill. That new thing combined with the models just getting better—it feeds on itself. The model then can consume all those skills.

The gap between specialized privatized knowledge—inside of someone's mind, some specialist doctor, some specialist psychiatrist who's been doing this work for 40 or 50 years—the delta between what they know and no one else knows is getting smaller. That is massively impactful for humanity in general.

Then there's another layer on this. All of that is being consumed by these labs who are spending billions of dollars bringing that knowledge into the models. But what we just saw from Anthropic—and this is happening all over the place—a bunch of Chinese labs are doing it in mass, very organized. China is known for doing this. They are famous for stealing ideas and stealing content.

They're also massively going all in on open source models. I believe they have a very clear strategy: you don't have to compete to be a pinnacle lab. They don't have an Anthropic. They don't have a Google DeepMind. They don't have an OpenAI. But they do have [DeepSeek](<https://www.deepseek.com/>), and DeepSeek has been called out for doing this for a very long time. They are capturing the knowledge of all the billions of dollars of work and bringing it into open source.

What they are doing as a Chinese strategy for AI is releasing it, diffusing it, absorbing it into the pool. You've heard the metaphor peeing in the pool. Our specialized knowledge—what specialized humans could do that no one else could do—that is the pee that's going into the pool. You can't pull it out. It's just going to be in there.

And the techniques that make those premier labs better—those are also being diffused. Somehow when the major labs have a major advantage and jump ahead, the Chinese models seem to get it a few months later. The specialized knowledge is being diffused into public domain. That's just a transition that's happening.

## Products go from standalone software to APIs [​](<https://danielmiessler.com/blog/the-great-transition#products-go-from-standalone-software-to-apis>)

I talked about this in [my book from 2016](<https://danielmiessler.com/blog/the-real-internet-of-things>)—basically said that [businesses become APIs](<https://danielmiessler.com/blog/mobile-ai-digital-assistants-business-apis>). And we're finally now starting to see this. 📚 From[ The Real Internet of Thing](<https://danielmiessler.com/blog/the-real-internet-of-things>)s, published in 2016.

All these people releasing tools, models, functionality—a company that does remove background, Excalidraw just came out with a new piece of functionality where you could just describe what you want to make and it will build all the different objects for you in your favorite fonts and your favorite aesthetic. It'll just build you diagrams.

My first question when I saw this was hold on. I went and looked at the documentation and it basically said you just go into the interface and type into Excalidraw what you want. And I'm like, what are you talking about? Do you honestly think in early 2026, I'm going to open up Excalidraw and type in a prompt? Are you kidding me?

So I posted: this looks amazing. Looks fantastic. There's no way I'm going to use it. Can you make this available as an [MCP](<https://modelcontextprotocol.io/>)? Can you make this available as an API? I'm not going to do any of this ever. If I have to open an app, I've already lost. My AI should be doing all of this for me.

When I posted that on Twitter, a whole bunch of people showed up and they're like, yeah, a hundred percent. I need an MCP for this. Otherwise it's not useful.

That is the way everything is going. If you notice, most of the releases coming out for products now, they're like, here's the MCP for it. Here's how your agents can do this automatically. This is just becoming the new way to release software. And this is heading in the exact direction that I put in that book in 2016: businesses become APIs.

## The consumer disappears—your agent decides [​](<https://danielmiessler.com/blog/the-great-transition#the-consumer-disappears%E2%80%94your-agent-decides>)

Why is this important? Because the consumer is not so much making the choice anymore. The consumer is not going to be like, hmm, yeah, there's 47,938 different options for removing backgrounds from images. Let me pull up GitHub and Google and spend two and a half hours sampling and trying different ones. No—there's too many apps. And because of AI, there's too many apps being made right on top of that. There'll be hundreds more of these things coming out all the time.

The only way this resolves is there are directories. If you have a background remover tool—by the way, my favorite is Remove BG, and they have an API. That's what my system Kai actually calls.

If you have one of these agents, there will basically be orchestration layers, directories of services labeled and categorized—taxonomy, folksonomy, whatever—saying if you want to remove backgrounds from images, here's your list of 27,000, but they will be rated. Different services with different ratings. And my system Kai will know which services it prefers. He's going to select the highest rated one with the most ratings, the least negative ratings, whatever algorithm Kai wants to use. Pulls that in, drops it into our workflow inside of our skill. That's it.

Where's the website? Where's the website for remove background? Who needs a website? This is a directory service, like the old days, like Yahoo directories. It's already been rated. My agents are going to check those ratings and find the API and integrate it.

This old way of making the software, packaging it, oh, it's got to have a nice UI, a nice website—when the person comes to the website, they got to really like it, then they click the buy button—it's all going away.

## Interface and SEO are dying [​](<https://danielmiessler.com/blog/the-great-transition#interface-and-seo-are-dying>)

This is tightly coupled with another transition: interface is going away. SEO is going away.

Interface used to be for humans. We make software, we have services, and we have to have an interface for that. Not just the interface you use day to day to interact with it, but also the marketing and documentation interface. Front end in general is going away. It's not that the content won't be there. It's that it will be designed to be consumed by agents. AI will be the main consumers.

Everyone gets a digital assistant—I wrote about this in [The Real Internet of Things](<https://danielmiessler.com/blog/the-real-internet-of-things>) in 2016. Everyone gets a digital assistant, everything gets an API.

> Every object has a daemon—an API to the world that all other objects understand.[The Real Internet of Things](<https://danielmiessler.com/blog/the-real-internet-of-things>), 2016

Our AI, because it knows us so well, when we make a request, it goes and gets the thing from the API and brings it back to us.

When we want an interface—I'm buying shoes, I want to see what they look like—our AI will be presenting the interface to us. People are already building bespoke software. Custom software is the direction it's going. Software goes from everyone using the same packages to everyone getting bespoke software.

The core part of your business, the core part of your product is the API, which will be used by the agents of the consumer. And the interface will be between their agent and them. That's the interface.

SEO goes from trying to attract the user to trying to attract the user's AI. When I say, hey, I need a new mattress, I'm not saying that to the internet. I'm not saying that to Google. I'm saying that to my DA. And my DA knows my sleeping habits, knows my routine, knows if I like a firm mattress or a soft one, knows my girl likes a softer bed, I like a harder one on my side.

Your agent knows you, therefore it can do smarter queries for you. But the point is it's the one doing the queries. If it's going to be tricked into picking one mattress versus another, the tricking needs to happen at the AI layer because I'm just going to do whatever my agent tells me. The agent's going to be like, yeah, I found the best one. It's this much. Do you want me to get it for you? I'll have it here tomorrow. And that's the end of that.

## Enterprise: the graph of operations [​](<https://danielmiessler.com/blog/the-great-transition#enterprise-the-graph-of-operations>)

Much of the same stuff happening on the consumer side is also going to happen on the enterprise side. And those changes are massive. Absolutely massive.

One of the big transitions is going from humans creating processes and following them to AI running the business based on SOPs—basically building out a graph structure of all the work that needs to be done.

I did [a post in 2024](<https://danielmiessler.com/blog/companies-graph-of-algorithms>) talking about how companies are just a graph of APIs, a graph of operations. Take the insurance example: you have to look at photos, look at their account, they're making a claim, you need to filter for fraud. Is this legit? Does the picture look real? Do they have a real account? Are they making lots of claims? Does the account look compromised? All these different things. And if it looks legit, here's how much we're going to pay you out.

That's the type of thing where, currently in the enterprise, there is not a graph that the CEO could look down and say, this is my entire business. This is every task happening in my company and the process of how it's done. The SOP—standard operating procedure—for how this thing is done.

AI is going to have this for every company. That's the major transition, and it's just now starting. It's very slow. Much slower than all the consumer adoption we've seen over the last couple of years.

> You've probably never seen your company in this way, but AI soon will.[Companies are a graph of algorithms](<https://danielmiessler.com/blog/companies-graph-of-algorithms>)

In the past, people were basically the company. The people were doing the work. Yes, they had documents. Yes, they had processes. But it's the people doing the work. They're supposed to follow this policy, but it's just a doc. Do they follow it? Not really. The main person who maintained them went on maternity leave and never came back. Those docs get old. Nobody's following the policy.

That is completely different than an AI saying, I now own all these SOPs. Here is the map of all work that's being done. Humans are still there—humans are the ones responsible for improving the AI, for telling the AI, hey, we need to change this SOP. You have a conversation with the AI, it makes the change, all the documentation is updated, all the SOPs are updated, the cross references are updated. That is the new model for business.

Now a software vendor comes in. Before, they would bring their salesperson, take someone out to a steak dinner. Yeah, it does background removal way better than anything else. If they convince this person and the manager and procurement, they buy it. It's humans buying software. Software is a package sitting on a shelf.

In this new model, this graph system includes all the tools. The conversation becomes completely different with the software vendor. Here is my map. Here's all the processes, all the work, every single workflow. What are you replacing? What are you doing better? Click on the node for background image removal. Here's the metrics—how fast it is, how cheap it is, how many times it failed, how many times it succeeded. Now what are yours?

They're going to have to produce metrics that say they can do that function better. It's no longer about a software package that some human is buying and maybe they use it, maybe they don't. It's an AI saying, here are my metrics for this function. Can you prove that your metrics are better? That's a completely different way of thinking about software.

## Automation goes from helper to replacement [​](<https://danielmiessler.com/blog/the-great-transition#automation-goes-from-helper-to-replacement>)

The transition here is automation going from a thing that helps humans do their jobs better—improves productivity and efficiency—to being a way for companies to get to their ideal state of being able to do all the work themselves.

This is colossal. This is economy changing. This really is the end of labor.

There's labor and there's capital and these have always been in balance. It gets disrupted because companies have always wished they could do all the work without employees. If you're a single founder and you don't have much work to do, you do all the work yourself, you get all the profits yourself.

If your business is washing clothes and you buy a washing machine—before, you were doing it by hand in the river. You weren't making that much money. You saved up for a year and bought a washing machine. Now you're able to do way more clothes and make way more money. If a whole bunch of people come to you and say, hey, I can also wash clothes in the river and you need to hire me because that's what's fair—you're going to be like, are you kidding me? I can do all this work myself. I literally am doing all the work myself.

If I have a clothes washing business and I have 10 washing machines behind me, that is me doing all the work myself. That is the transition that is happening. That is what AI is.

The total amount of compensation that knowledge workers receive is somewhere around $50 trillion per year globally. I think it's somewhere around $10 trillion for the US. That is how much money companies are spending to pay humans. And the major transition here is they don't want to be paying those humans. They actually never did.

My favorite way of capturing this: the ideal number of human employees inside of any company is zero. That is the number that they're trying to get to.

There are exceptions. If you're a small spunky founder and you want to work with your friends—you build a small startup, you're all kind of owners at that point. You'll still have elite employees, cadre, co-founders. That's not going to go away. But we're talking about going from tens of thousands of employees to a few hundred, maybe eventually a few dozen. Massive reduction because of this different way of thinking about automation. It's not a thing that helps a human do a task. It is a way to get to the state of the company doing the work itself, which is a natural, clean, happy state for any company.

## Human 3.0: the post-corporate world [​](<https://danielmiessler.com/blog/the-great-transition#human-3-0-the-post-corporate-world>)

So what are we supposed to do? If everyone gets fired, who's going to buy all the stuff?

There's going to be money. People are going to receive money to pay their bills. Otherwise you just don't have a society. That will get solved one way or another, hopefully gently and fast.

But the question is, how's this actually going to happen? What are people going to do? How are people going to work?

The transition is going from work meaning you work for a big corporation to work meaning you do things yourself. You have offerings yourself. You produce value yourself and you broadcast that value out.

What's going to happen is there will be a technology layer that links people. It links projects with services. It links people who have capabilities with those who need them.

Instead of people working for companies en masse—because those companies are trying to get rid of everyone—we're going to make money by producing value ourselves, by articulating the skills that we have, the capabilities that we have, the products that we provide, the services that we provide, broadcasting that out. That is going to go up into one of these directories, like I talked about before with products that AI can look at. But this will also be the substrate for all work to be done.

Humans will broadcast their capabilities. I'm a systems engineer, eight years experience, here's all the different stuff I can do, here's my portfolio. By the way, I like to mountain bike. This is your [daemon](<https://danielmiessler.com/blog/launching-daemon-personal-api>). This is your broadcast system, describing the people you've worked with, your reputation score, people give you upvotes—kind of similar to what LinkedIn was doing, but this is the actual play.

There's a substrate that connects all these different people. When I need a cat sitter because I'm going on vacation, I broadcast out, hey, I need someone to watch my cat. My AI is broadcasting that for me. Everyone's AI is watching the substrate. Someone's like, hey, I'm a cat person, I love cats, I live two blocks away. Her AI tells her, there's a cat sitting job over here, it's going to pay $84. Do you accept? Boom. Yes.

Someone injured themselves on the corner. Does anyone have medical professional training? EMT skills? It's going to beacon for people nearby who have a reputation score above a certain threshold. Someone takes the job. They go help the person.

Same for gardening, engineering services, tutoring, meal prep, personal training. Everyone who has services, capabilities, value to offer—they are beaconing out onto this system.

> Humans and objects will broadcast daemons around them, advertising their attributes and interaction capabilities.[Universal daemonization](<https://danielmiessler.com/blog/universal-daemonization-future-internet-iot>)

That is what I'm calling Human 3.0. It's the state we're going to get to.

I love this because it's more human focused. It's humans connecting with humans. It's not hierarchical—I work for Sarah, Sarah works for Joe, Joe works for Raj, and oh I'm having a meeting with Raj, oh my God he's three skip levels above me. This whole military structure, this whole dreading Monday—it's toxic and poisonous. And it has been for decades, people have been so unhappy with this. And now that it's actually under threat, people are like, well, don't get rid of my job. Don't fire me. Because they're worried about losing their livelihood, paying rent and a mortgage and school and groceries. That's understandable. But remember we shouldn't be clinging to a thing we hate and have hated.

This new human-based substrate where things are a lot more equal: you get hired based on your skills. That's a relationship you can get out of any time. You can be in multiple of these—ongoing retainer type things with 20 different customers. You're on a big project for six months getting paid from that. Plus you're doing the cat sitting. Plus you're a part-time EMT at night. You're broadcasting everything that you are. Not just "here's my resume, I'm a tech engineer level three, I worked at Intuit." That is not you.

What this is going to allow us to do is broadcast our full selves and be compensated and rewarded for being ourselves. If you're the best nurturer in the world, forget tech skills—the best listener, the best parent, the best tutor, the best boxing coach—that's in your daemon. That is broadcasted. They become world famous for that. And they make money from it, which they should. This is how humanity should work.

## Cybersecurity becomes AI vs. AI [​](<https://danielmiessler.com/blog/the-great-transition#cybersecurity-becomes-ai-vs-ai>)

Similar to a lot of the other things we've already talked about, cybersecurity has been human based. You hire a human team. They are good security engineers. They're doing pen tests, security assessments, vulnerability assessments. They're manually looking at all the different vendors trying to figure out which ones are dangerous. And they're just being bombarded by all these requests.

What security becomes now is your AI stack as a defender against the AI stack of the attacker. And unfortunately you're not facing one attacker. You're facing all the attackers.

The attacker is trying to understand your company extremely well. It's creating personality profiles on all your employees. It's coming up with the best spearphishing campaigns to find the ones who probably have the most access based on their job title. It's constantly pulling your DNS. It's trying to see if you're doing a merger and acquisition with a company that doesn't have good security. They're sending spearphishing emails. They're trying to compromise all your websites. They're trying to pivot internally. And they're doing this at machine speed. They've just got so many agents working on this, constantly hitting you.

You can't tell Chris and Raj and Sarah, hey, great job last year. I need you to do 895 times as much work because that's how many more attacks we're being hit with. That doesn't work. You also can't say, great news, we got three more headcount. That also won't make a dent.

Your only chance is to have the same AI or better as the attacker. What happens to all companies also happens to security programs. It's no longer about here's our security team and roughly the things we need to do. SOPs. Everything is a process and workflows which you could visually look at and see—this is the queue for processing incoming things, here are the constant workflows for finding insider threats, here's every single tool, every single decision point, every single approval point that needs to happen as part of CI/CD before something goes live. Everything becomes transparent, visible with discrete actions and decision points at each area.

And the game is: are we getting that context updated? New AWS account just stood up. We launched a new service in Asia and Iceland and Seattle. How quickly are we as a security team learning about that? As AI starts spinning this stuff up for the attackers, they're going to build a world model of these companies faster than the company has it. Because the company has to go slow—they have to have 19 meetings to prepare for the meeting. Attackers are just going to YOLO it, submit the single prompt, make no mistakes and start attacking.

🎯 The game: your orchestration system needs to be better than the attackers'.

The transition is from humans doing security work to a unified workflow model with SOPs executed largely by agents, with humans there to tweak and improve and guide and steer and validate. The game is for your orchestration system to be better than the attackers.

## The inversion: industries become use cases inside AI [​](<https://danielmiessler.com/blog/the-great-transition#the-inversion-industries-become-use-cases-inside-ai>)

This next one is a way of thinking about enterprise AI in a completely different way. I [put this out about a year ago](<https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong>), and I think it's really powerful as an inversion.

Currently—and even still now—everyone is thinking, okay, we have security, we need to put AI on it. We have finance, we need to put AI on it. We have HR, we need to put AI on that. So the idea is you have the discipline, the topic, and then AI gets sprinkled on top.

I don't think that's the way to think about it.

I think the way to think about it is: you have a company and the company's work and all its workflows and the graph of all the services and tools and operations, SOPs, goals, everything. That is actually the system. The system is the graph of operations. It is the graph of algorithms that take place to make this business function. Think of AI as a system for running this graph of algorithms. That is what AI is.

Then the question becomes: show me procurement. You look at this graph and 19 different lines all light up—those are the procurement workflows. We can drill into those. Here's the tools. Here's the human involved. Here's the decisions. Here's the sign-offs. Here's the exceptions.

What ends up happening is all the different things that used to be industries become use cases inside of AI.

The before is industries using AI. The after is AI that has use cases for what we used to call industries.

Some of these are security, some are HR, some are engineering, some are marketing. AI is the container. AI is the thing. And it just has functions that happen to be affiliated with what we used to call industries. That is a fundamental transition.

If you abstract everything to questions and everything to algorithms—"how happy are our employees?" or "how much money are we spending on compensation?" or "should we pay more for bonuses?"—those are questions. Those questions are not an industry. They just happen to be associated with what we used to call an industry. All of it feeds off this underlying unified context and graph of algorithms, powered and managed and orchestrated by AI.

## Custom everything and the fragmentation problem [​](<https://danielmiessler.com/blog/the-great-transition#custom-everything-and-the-fragmentation-problem>)

In the past, you had very few organizations producing software. Adobe was on top. Microsoft was on top. You go into any enterprise, they're mostly running Microsoft or Google. I think that might start to go away.

It's not that these major platforms won't still have a stronghold. It's just that the implementation of their software isn't going to look the same inside of all these different companies. For smaller companies that aren't legacy, their software stack could look completely different from another startup maybe even doing the same sort of stuff, just because the founders will be like, yeah, I like terminal style, I don't like UIs. I want everything to be API based. I really like the color purple.

We're already seeing this with custom replacements of tons of different SaaS software. It's really easy to create a version of something. There's a big difference between that and having it roll out enterprise-wide, stable and secure. That'll take a couple of years to work through. But there's a very high chance that companies and consumers will be making their own software.

Let's be clear: there's 8 billion people on the planet, not everyone's making their own software. But consider that in 2019 or 2022, the number of people who made software products was rounded down to zero. Everything in the app store, every software company, rounded down to zero. If you multiply that by 1,000 or 10,000 or a million, that is a lot more software. Plus the ability for someone to speak to their AI agent and say, hey, I really wish I had a workout app, it's $19 a month, it's pretty good, but I wish it did this, this, and this—and boom, it's now installed on your phone, the other one's uninstalled, the subscription is canceled.

Every CFO is looking at their software list and saying, how can I cancel all of this? Just like the employee thing—how can I get to zero employees? How can I not pay any other company for software? How can it all be ours? Everyone wants this. We couldn't do it before because it's hard to make software. You got to maintain it. The better AI gets, the easier that gets.

😟 Robert Putnam warned about this fragmentation in[ Bowling Alon](<https://en.wikipedia.org/wiki/Bowling_Alone>)e back in 2000.

This ties into something Robert Putnam talked about in Bowling Alone in 2000. When you have fragmentation like this across companies but mostly across people, it's going to be profound. The reason the country was so unified before is that we were all watching the same TV shows, the same news, drove the same cars, had the same watches, went to the same churches, lived on the same block. Everyone's consuming the same sources, thinking similar things, reading the same newspapers.

When everyone gets custom software, custom AI—you're not even viewing the sources. There's millions of them. Billions of them. Your AI's job is to consume all of that, understand you, understand your needs, and give you what you want. That opens up the possibility that all of us will be having a different world experience. We believe the reality that we see.

If you watch a particular news source, particular YouTube channels, particular podcasts—you think the world works that way. That is your world. That is reality to you. The person next door might be in a completely different reality. They might not even know about the most popular thing that happened yesterday. This fragmentation because of custom everything is going to be massive.

Inside companies, the dynamic is strange. How do you audit software? How do you do security scans? How do you do compliance? It's a lot easier when everyone has SAP and Microsoft 365 and CrowdStrike and Palo Alto firewalls. What happens when everything is custom?

## Ideal state management: the biggest idea in AI [​](<https://danielmiessler.com/blog/the-great-transition#ideal-state-management-the-biggest-idea-in-ai>)

I've saved this one for last.

I think the ultimate use case for AI is what I'm calling ideal state management—or state orchestration. I've [written about this before](<https://danielmiessler.com/blog/nobody-is-talking-about-generalized-hill-climbing>). The real term will be created probably in the next year or so.

What we've been doing inside of companies, what we've been doing as people, what we've been doing as a society is just kind of YOLOing. This is what we've always done. This is what humanity does. Companies are like, hey, we should have goals, we should have OKRs, we should have a meeting, we should plan the next year. Those documents go somewhere. Maybe they get revised, maybe they don't.

If you track a company's goals for an average medium-sized company over the course of a year or five years or ten years, they're just making stuff up. It changes constantly. The management changes. They come out with a set of metrics. They don't hit them. They come out right after with a new plan, a new hire who's going to be amazing, new metrics. Constant reinvention—not because of innovation, but because we're winging it. This is no fault of anybody. Everyone's doing it. Very, very smart people are doing it. It's just the reality that we live in.

This is one of the fundamental changes AI is going to bring. I think we're about to move away from this ad hoc YOLO approach to something much more powerful: state management.

State management starts with defining what ideal state is. This is a thing that most companies do not have. They don't have an articulated statement—kind of like a PRD document with multiple SOPs revolving around it—that says: here is our actual mission, here are our actual goals, here are the problems we are trying to solve in the world, here are our challenges, here's our risk register, our projects, our budget, our people. This is your unified document. This is your system. This is your algorithm for what you're chasing.

This being locked into the core DNA of the company and everything revolving around it—that graph of algorithms needs to be feeding this system. This very well articulated ideal state is about to become the most important thing for companies, but also for anything. For organizations, for entities, for people.

I've been using a system like this for probably 10 years, and there wasn't any AI. You don't need AI to articulate this and start moving towards it. It's very powerful. Forget any tech—just note cards, index cards, a space pen. You're off and you're going to have massive benefits from doing this.

Here's where the AI comes in. Here's the game. This is the universal game. If we meet aliens flying around the galaxy and we tell them this, they're going to be like, yeah, that's what everyone does. How do you think we got here? How do you think we have all these spaceships? How do you think we have Dyson spheres around all these stars? That's obvious. That is the algorithm.

The algorithm is: we have ideal state. What is our current state? That's step two. Your AI and all the different agents and systems—it's not all AI, this is deterministic code as well—what is the current snapshot? What is the current state of our problems and our solutions and our products and our services? How happy are our people? How happy are our customers? What is the current churn number? What are our competitors about to release? What are the market conditions? Snapshot.

The role of AI is continuous migration, continuous gap closing between current and ideal state.

This works as an individual trying to lose 20 kilos. An individual trying to increase their VO2 max, trying to find a wife, trying to get their art exhibited at MoMA, trying to come up with new EDM tracks so they can play live at EDC. Trying to run a federation of planets 9,000 years in the future. Anything you're trying to do at any scale can be managed by ideal state and current state and the migration. This is extremely powerful.

I have this thing inside of the [PAI](<https://personalinfrastructure.ai/>) platform called [the algorithm](<https://danielmiessler.com/blog/the-last-algorithm>). I literally start the algorithm by decomposing the prompt that comes in and turning it into reverse-engineered ideal state components. I break out the pieces. I look at the context from the user and do deep analysis and research. What do they actually mean by this? What do they explicitly say they want? What do they explicitly say they don't want? What are some common gotchas? All that gets decomposed, reverse engineered, and I start creating ideal state criteria. These go into the PRD, and it's all working off of ideal state.

Engineering can be run this way. Companies can be run this way. You managing your entire family's happiness. Hey, I'm looking at the dashboard—looks like they haven't had enough vegetables. I'm going to tell my AI to order more vegetables. Hey, we haven't gone on a vacation together in a while. Hey, I noticed we were looking at our phones too much at the dinner table. My AI notified me about that. Let's make sure we do vacations with no tech involved. We're focusing on human things.

If you're running an ice cream truck business, a federation of planets, or you're just trying to find a boyfriend—all of this can be managed the same way.

I got this from [Andrej Karpathy](<https://x.com/kaborpathy>): you can't hill climb, you can't progress towards something if you don't have failures, if you don't have a thing to hill climb against.

> Software 1.0 easily automates what you can specify. Software 2.0 easily automates what you can verify.Andrej Karpathy

My ideal state criteria in the algorithm turn the ideal state into verification criteria. They're all discrete and verifiable. Yes or no. That's what gets us to verifiability, and that's what ultimately allows us to go from current state to ideal state.

## The mental model [​](<https://danielmiessler.com/blog/the-great-transition#the-mental-model>)

I consider all of this combined to be the great transition that is happening to all of us right now.

My goal is that when you see the news—new models, new capabilities, workers being replaced—you can put it into this framework and say, okay, that's not new, that fits. It shouldn't produce as much anxiety if you can see where it's all going.

I think this transition model with all its sub-transitions works as a mental model container. If you understand this, you're much less likely to be surprised. Who knows how it's going to happen, when it's going to happen, which company is going to do it. You can't predict that stuff.

I also really worry that all of this could coincide with a significant economic downturn. Automation combining with macroeconomic factors—it's not my area of expertise, and there are too many variables to say anything with confidence. It could hit in just a few months in 2026, or it could be in 2028 or later, or it could be a soft landing and not really be that bad. My best guess is somewhere around 2027 or 2028, which is unfortunately right when I think all of this AI impact is about to hit with full force as well. I [wrote about this concern](<https://danielmiessler.com/blog/im-worried-it-might-get-bad>) recently.

But the direction is possible to see. And that gives you a container to be like, okay, this all sort of makes sense inside of this framework. So you're not spooked out by all these new models and products coming out. If you have this mental model, you're more likely to just say, eh, yeah, that seems to be the way it's going—and you can buckle down and move forward.

## Summary [​](<https://danielmiessler.com/blog/the-great-transition#summary>)

1. It's not one transition, it's many—all happening at the same time, all going in the same direction.
1. The knowledge that made experts special is getting absorbed into AI. The gap between what specialists know and what everyone can access is shrinking fast.
1. Products are becoming APIs. If you have to open an app, you've already lost.
1. You're still making the decisions, but your agent is the one browsing, comparing, and buying—which means it's the one available to influence.
1. Companies are moving from org charts and ignored policies to transparent graphs of operations run by AI.
1. Automation isn't about helping employees anymore. It's about companies doing the work themselves.
1. In the post-corporate world, you broadcast your full self—skills, interests, reputation—and get paid for being you.
1. Custom everything is likely to fragment shared experience in ways Putnam warned about in Bowling Alone.
1. The through-line is ideal state management: know what perfect looks like, measure where you are, close the gap.
1. This won't tell you who wins or when. But it should make the news a lot less surprising.

---


**作者** Ivan Burazin（@ivanburazin）  
**貼文連結** https://x.com/ivanburazin/status/2027879361177850177  

**正文**

Well well look who else got into the Sandbox game https://github.com/alibaba/OpenSandbox

Welcome @AlibabaGroup

---


**作者** Julián（@juliandeangeIis）  
**貼文連結** https://x.com/juliandeangeIis/status/2027889701193973853  

**正文**

Primer blog, estoy experimentando a ver si copa la forma. 
Bastante contenido, espero próximos hacerlos más cortos.

Hablo un poco de context engineering - agent harness, técnicas, tips y algunas de las implementaciones que tenemos en MELI.

---


**作者** andrew gao（@itsandrewgao）  
**貼文連結** https://x.com/itsandrewgao/status/2027579200635605058  

**正文**

you can instantly 10x your vibecoded frontends by just learning what different ui components are called

ofc opus is creating generic slop, the only words you know are menu and button. 
you can instantly 10x your vibecoded frontends by just learning what different ui components are called

ofc opus is creating generic slop, the only words you know are menu and button. 
https://component.gallery/
Will share more vibecoding frontend design tips soon
As promised! https://x.com/itsandrewgao/status/2028296136281522226?s=20

---


**作者** Shubham Saboo（@Saboo_Shubham_）  
**貼文連結** https://x.com/Saboo_Shubham_/status/2027791423253450948  

**正文**

DON'T READ this unless you want to feel like you're living in 2027.

I run a team of 8 OpenClaw Agents 24/7 based on characters from FRIENDS and The Office that get smarter every single day.

Running agent teams is one thing. Watching them get smarter every day is another. 

---


**作者** WquGuru🦀（@wquguru）  
**貼文連結** https://x.com/wquguru/status/2027942744845693094  

**正文**

高效设计AI Agent的10个要点（特别针对Claude Code/Anthropic生态）：

1. 核心：设计一个好Agent更多是艺术而非科学，关键不在于塞更多prompt或工具，而在于让Agent像人类一样自然地工作

2. 渐进式披露（Agent Skills的核心思想）：大规模上下文应该封装成Agent Skills，用了这个后，Agent效率直接起飞

3. 工具数量要极致精简（少即是多）：别给Agent 50个工具，它会迷茫&浪费token。只给4-5个清晰、自然命名的强大工具就够了

4. 设计原则：“如果你是Agent，用这些工具干活会觉得缺什么？” —— 思考问题，补上那个缺口

5. 用Tasks而非简单Todos

6. 把记忆（Memory）和计算（Interaction）彻底解耦，子Agent之间可以共享持久状态，不会让prompt无限膨胀。这本质是在底层构建C-I-M架构（Context-Interaction-Memory）

7. 危险操作必须预览+用户确认：删文件、花钱、改重要代码前，Agent必须先输出清晰计划，等待你说“Yes”，有人专门做了ExitPlanTool或类似preview工具，强烈推荐

8. 文件系统 = Agent最好的“大脑”，精心组织的skills/文件夹 + 每份文档的短摘要，比任何RAG或巨型prompt都干净高效

9. 主动问用户澄清（AskUserQuestion工具）
：上下文有歧义时，先问清楚，而不是浪费token乱试，这能大幅减少无效循环

10. 核心哲学转变：2024年的核心是提示词工程，2025-2026的核心转移到了做原生Agent操作系统了。终极目标是让Agent自己发现、自己构建上下文、自己管理状态，而不是人肉硬推
高效设计AI Agent的10个要点（特别针对Claude Code/Anthropic生态）：

1. 核心：设计一个好Agent更多是艺术而非科学，关键不在于塞更多prompt或工具，而在于让Agent像人类一样自然地工作

2. 渐进式披露（Agent Skills的核心思想）：大规模上下文应该封装成Agent Skills，用了这个后，Agent效率直接起飞

3. 工具数量要极致精简（少即是多）：别给Agent 50个工具，它会迷茫&浪费token。只给4-5个清晰、自然命名的强大工具就够了

4. 设计原则：“如果你是Agent，用这些工具干活会觉得缺什么？” —— 思考问题，补上那个缺口

5. 用Tasks而非简单Todos

6. 把记忆（Memory）和计算（Interaction）彻底解耦，子Agent之间可以共享持久状态，不会让prompt无限膨胀。这本质是在底层构建C-I-M架构（Context-Interaction-Memory）

7. 危险操作必须预览+用户确认：删文件、花钱、改重要代码前，Agent必须先输出清晰计划，等待你说“Yes”，有人专门做了ExitPlanTool或类似preview工具，强烈推荐

8. 文件系统 = Agent最好的“大脑”，精心组织的skills/文件夹 + 每份文档的短摘要，比任何RAG或巨型prompt都干净高效

9. 主动问用户澄清（AskUserQuestion工具）
：上下文有歧义时，先问清楚，而不是浪费token乱试，这能大幅减少无效循环

10. 核心哲学转变：2024年的核心是提示词工程，2025-2026的核心转移到了做原生Agent操作系统了。终极目标是让Agent自己发现、自己构建上下文、自己管理状态，而不是人肉硬推
Claude最佳实践：https://agentway.dev/zh/claudecode

---


**作者** Viking（@vikingmute）  
**貼文連結** https://x.com/vikingmute/status/2027704841674367277  

**正文**

今日必读长文：使用 Claude Code 构建高效 AI Agent 的实战经验总结 

作者是 Claude Code 团队成员

工具演变的过程讲的很棒，从最初到后来的Progressive Disclosure，只在需要时暴露工具，文件，上下文，模型自己决定要不要看更多，极大降低 token 消耗，提高稳定性

到再进阶：让模型自己 grep / search / build context，而不是全塞进去。

实用设计模式与技巧
Skills folder / MCP 的组织方式
嵌套 Markdown 文件结构
工具权重  intent-based routing 的高级玩法 等等

从文章中能清楚的能很明显地感受到 skills 设计 的来龙去脉 非常深入浅出的一篇文章

---


**作者** Gavriel Cohen（@Gavriel_Cohen）  
**貼文連結** https://x.com/Gavriel_Cohen/status/2027841164150178238  

**正文**

When you're building with AI agents, they should be treated as untrusted and potentially malicious. Whether it's prompt injection, a model trying to escape its sandbox, or something nobody's thought of yet, you shouldn't be trusting the agent. The right approach isn't better permission checks or smarter allowlists. It's architecture that assumes agents will misbehave and contains the damage when they do.

That's the principle I built [NanoClaw](<https://github.com/qwibitai/nanoclaw>) on.

Don't trust the process

OpenClaw runs on the host machine by default. It has an opt-in sandbox mode, but most users never turn it on. Without it, security relies on application-level checks: allowlists, confirmation prompts, "safe" commands. These come from a place of implicit trust that the agent isn't going to do something wrong. Once you accept that an agent is potentially malicious, it's obvious application-level blocks aren't enough.

In NanoClaw, container isolation is core. Each agent runs in its own container, created fresh per invocation and destroyed afterward. The boundary is enforced by the OS, not by the application.

Don't trust other agents

Even with OpenClaw's sandbox enabled, all agents share the same container. Your personal assistant and your work agent sit in the same environment, and information can leak between agents that should be accessing different data.

In NanoClaw, each agent gets its own container, filesystem, and session history. Your personal assistant can't see your work agent's data because they run in completely separate sandboxes.

Don't trust what you can't read

OpenClaw has nearly half a million lines of code and 70+ dependencies. Nobody has reviewed it all. It was written in weeks with no proper review process. Complexity is where vulnerabilities hide.

NanoClaw is ~3,000 lines. A developer can review the entire codebase in an afternoon. New functionality comes through skills. You review exactly what code gets added, and you only add what you need. Every installation is a few thousand lines tailored to the owner's requirements.

![Article Image](<https://pbs.twimg.com/media/HCRRInMWoAAmKee.jpg>)

With a 400K-line monolith, even if you only use two integrations, the rest is still loaded, still part of your attack surface. With skills, the boundary is obvious.

Design for distrust

If a misbehaving agent can cause a security issue, the security model is broken. Security has to be enforced outside the agentic surface. Containers and filesystem isolation exist so that even when an agent does something unexpected, the blast radius is contained.

None of this eliminates risk. But the right response is to make trust as narrow and as verifiable as possible. Don't trust the agent. Build walls around it.

---


**作者** Creao AI（@CreaoAI）  
**貼文連結** https://x.com/CreaoAI/status/2027699619132510276  

**正文**

Why do builders create specific Agent App flows?

Welcome to our second Campaign Winner Deep Dive.

Meet Leo (@Oghenekaro_KAY), Notable Visionary Winner of our Agentic Visionaries Campaign:
“Many AIs are underutilized because people don’t know how to speak their language.”

That frustration pushed him to build PromptSnap.

Not another AI tool.
An orchestration layer.
Why do builders create specific Agent App flows?

Welcome to our second Campaign Winner Deep Dive.

Meet Leo (@Oghenekaro_KAY), Notable Visionary Winner of our Agentic Visionaries Campaign:
“Many AIs are underutilized because people don’t know how to speak their language.”

That frustration pushed him to build PromptSnap.

Not another AI tool.
An orchestration layer.
Right now, using AI often means:
• 10+ tabs open
• Switching between image, video, and text tools
• Writing endless prompts
• Manually stitching outputs together

PromptSnap flips that.

It reads the objective, audience, and context —
then coordinates 22+ specialized AIs into one clear, structured workflow.

No juggling. No chaos.
Just coordinated execution.

And yes — it finally automates a complex content production pipeline.
This is what an Agent App looks like when it executes.
Our takeaway?

We’re seeing a shift:
From single AI interactions
→ to coordinated Agent App systems.

You shouldn’t need to manage AI.
AI should manage the workflow.

PromptSnap shows what happens when AI stops being a tool —
and starts acting like a workspace engine.

"You put in the intent, and PromptSnap runs it."
Execution, not prompts.
Watch the full interview with Leo (@Oghenekaro_KAY) through our YouTube Shorts ↓
https://www.youtube.com/shorts/6Ng34tUaNP0

---


**作者** Larsen Cundric（@larsencc）  
**貼文連結** https://x.com/larsencc/status/2027775964311392429  

**正文**

A lot of good reactions to the article! Always happy to discuss agent infra 🤝

The future is agentic.

---


**作者** Clifton Sellers（@CliftonSellers）  
**貼文連結** https://x.com/CliftonSellers/status/2027594768105029983  

**正文**

I built an agency from debt while working a day job.

No funding. No connections. No safety net. Just a laptop, three daughters counting on me, and a bet that the world was about to reward the people who showed up online with something real to say.

Three years later we've helped 400+ founders build personal brands. And in the last 12 months, something changed that made me more convicted in this model than ever.

AI didn't kill personal branding. It made it the only thing that matters.

Let me explain.

The way people find you has fundamentally changed.

60% of Google searches now end without a click. The answer gets served at the top of the page by AI before anyone scrolls. Over half of consumers have already replaced traditional search with generative AI tools when looking for recommendations. 71.5% of people regularly use ChatGPT and Perplexity for discovery.

That means your website doesn't matter the way it used to. Your SEO playbook is decaying in real time. The old funnel where someone googles your industry, finds your site, reads your about page, and books a call is breaking apart.

What replaced it is trust-based discovery.

AI models don't rank pages. They synthesize answers from sources they trust. They cite recognizable names. They surface people with authored content, clear expertise signals, and consistent digital footprints across platforms.

When someone asks ChatGPT "who should I hire to build my personal brand" or "what's the best content agency for founders" the answer isn't determined by your Google Ads budget.

It's determined by whether AI knows who you are.

Here's what most founders get wrong right now.

They hear "AI" and they think tools. They think automation. They think "let me use ChatGPT to write my LinkedIn posts and save 4 hours a week."

That's masonry with a faster trowel.

The real shift is architectural.

AI compressed the cost of building things to nearly zero. New websites are up 40%. iOS apps up 50%. GitHub pushes up 35%. Everyone read "barrier to building disappeared" and heard opportunity.

The correct read: when everyone can build, nobody can differentiate by building.

What's left is distribution. Reputation. Trust. The exact things a personal brand creates.

A mediocre app with 100,000 newsletter subscribers will outperform a beautiful app with zero distribution every single time. The products winning in 2026 aren't the best-built. They're the ones attached to someone who already has an audience.

Building software used to be the moat. Now building software is the commodity. Distribution is the new moat. And unlike code, it doesn't get cheaper with AI.

Here's the part nobody is talking about.

86% of consumers say authenticity influences what brands they support. 76% trust content shared by individuals more than content coming from companies. Employee-generated posts get 8x more engagement than corporate posts on the same topic. 99% of B2B buyers say thought leadership influences their purchasing decisions.

Read that again.

99%.

And yet most founders are still invisible. Still hiding behind a company page with 200 followers. Still thinking "when my product is ready, then I'll start posting."

That's too late. Reputation leads to revenue. Not the other way around.

Now layer AI on top of this.

AI doesn't just change how people find you. It changes how fast you can build the machine that makes you findable.

Three years ago, building a full-stack personal brand required a team, budget, and 6 months of ramp time before you saw results. Today, with the right systems:

One founder interview becomes 37-41 pieces of content across platforms. AI handles research, first drafts, repurposing, scheduling, distribution, and performance analysis. A founder can go from invisible to publishing daily across LinkedIn, X, newsletter, and YouTube in under 30 days.

The human part didn't shrink. It got concentrated.

Your taste. Your judgment. Your stories. Your point of view. The lived experience of building something real. That's what AI can't generate. And it's exactly what audiences are starving for.

Deloitte's global survey shows more than half of consumers are more skeptical about online information than a year ago. People are developing a filter. They can feel the difference between something generated and something lived. Posts that feel generic struggle. Content that demonstrates real thinking performs better.

AI raised the floor for content. Everyone can publish now. But it also raised the ceiling for the people willing to put themselves into the work. The gap between generic and personal has never been worth more.

So here's the play. And I'm going to be specific because I don't believe in advice you can't act on tomorrow morning.

Step 1: Define your 3 content pillars.
Not 10 topics. Three. The things you have earned the right to talk about through experience. For me it's founder-led content, distribution as a moat, and building with AI. Every post maps back to one of these. AI systems recognize patterns. If your content is scattered, AI can't categorize you. If it can't categorize you, it can't recommend you.

Step 2: Publish daily for 90 days.
Not weekly. Daily. Across at least two platforms. The compound effect is real but it requires volume to activate. Month one feels like nothing. Month two you start getting inbound DMs. Month three your name starts showing up in AI-generated recommendations because you've built enough signal density for the models to notice.

Step 3: Use AI for speed, not for voice.
Let AI handle research, outlines, repurposing, scheduling, data analysis. Do not let it write your posts word for word. The second your content sounds like everyone else's, you've lost the only advantage you had. Your voice is your moat. Protect it.

Step 4: Build your owned audience.
Social platforms are rented land. Start a newsletter. Build an email list. Create a direct line to your people that no algorithm change can take away. Content builds trust on social. Newsletter converts that trust into a relationship you control.

Step 5: Optimize for AI discovery.
This is the new frontier. It's called Generative Engine Optimization. Publish content that clearly defines who you are, what problems you solve, and for whom. Use your real name. Be specific. Be cited by others. Get featured in publications. The AI models that will determine who gets recommended in 2027 are being trained on the content being published right now.

I'm not saying this because it sounds good. I'm saying it because I watched it happen.

I watched founders go from zero presence to booked calendars in 90 days. I watched a CEO close a $200K deal from a single LinkedIn post. I watched the "build great products and they'll sell themselves" crowd get passed by people who understood that in 2026, attention is the new private equity.

AI made building easy. AI made creating fast. But AI didn't make trust abundant. If anything, trust got scarcer. And the people who own trust own the next decade.

The founders who win from here figured out what AI made irrelevant and stopped doing it.

The ones who lose will keep building in silence and wondering why nobody came.

Your personal brand isn't a vanity project. It's infrastructure.

Build it now. Or watch someone else take the attention you could have owned.

---


**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2027893695522214042  

**正文**

Humans no longer need to onboard.

I just rebuilt our auth at @nozomioai to be compatible with agents.

Just paste this into your agent. It will automatically sign you up, generate an API key, and install our skill for you:

“use npx nia-wizard@latest agent-guide to set up Nia” 

---


**作者** Muratcan Koylan（@koylanai）  
**貼文連結** https://x.com/koylanai/status/2027819266972782633  

**正文**

Finally had some time to read @trq212 and @RLanceMartin prompt-caching articles. They are dense and include important insights into context engineering.

1. Static-First Ordering
Claude Code's entire prompt is ordered for cache hits:
Static system prompt & tools -> CLAUDE[.]md -> Session context -> Messages

This is the same principle behind progressive disclosure architectures, but applied to inference cost. Static, per-session instructions should come before dynamic data. 

Every time dynamic content appears before static content, you're paying full price on cache misses, which also increases latency.

2. Messages Over System Prompt Mutations
Instead of updating the system prompt (which breaks cache), inject updates via tags in user messages.

For multi-turn sessions, if context changes mid-conversation, appending that as a message preserves the cache prefix. Mutating the system prompt to include updated context would be expensive.

3. Subagents for Model Switching
Switching models mid-session destroys the cache because caches are model-specific. Claude Code uses subagents with handoff messages instead.

If you're 100K tokens into a conversation with Opus, it's actually more expensive to switch to Haiku for a simple question than to just let Opus answer it. A warm cache on an expensive model beats a cold cache on a cheap model.

If your multi-agent system uses different models for different tasks, isolate each agent's context. The orchestrator passes structured handoff messages between agents rather than switching models within a single conversation thread.

4. Never Change Tools Mid-Session
Tools are part of the cached prefix. Adding or removing one invalidates the entire cache. Claude Code's Plan Mode doesn't swap tool sets, it uses EnterPlanMode / ExitPlanMode as tools themselves, with instructions delivered via messages. The tool definitions never change.

Instead of removing tools, they send lightweight stubs with defer_loading that the model can discover on demand in tool search. Full schemas load only when selected. The prefix stays stable.

5. Cache Hit Rate Is a Production Metric
Claude Code monitors prompt cache hit rate the same way most teams monitor uptime, they set alerts and treat drops as production incidents.

If you're building agents and not tracking cache_creation_input_tokens vs cache_read_input_tokens from API responses, you're missing a major cost and latency lever. Put it on your dashboard next to latency and error rate.

6. Cache-Safe Compaction
When the context window fills up, Claude Code summarizes but uses the exact same system prompt, tools, and conversation prefix so the compaction request reuses the parent's cache.

The right approach is to append the compaction instruction as a new user message. 

Same prefix = cache hit on the entire history.

---


**作者** Fivos Aresti（@fivosaresti）  
**貼文連結** https://x.com/fivosaresti/status/2027760756142363072  

**正文**

Companies are going to start paying GTM Engineers $150K+/year.

They can do it all:

1. Set up email infrastructure
2. Build targeted lists
3. Enrich data from multiple sources
4. Score leads into tiers
5. Route leads to reps
6. Run automated outbound
7. Build awareness scores
8. Orchestrate inbound systems

That said...

I put together a full cheatsheet that covers the entire role from start to finish...

• Strategy plays for warm, signal-based, and cold outreach.
• Data aggregation across CRM, 1st party, 2nd party, 3rd party, and database sources.
• Data enrichment workflows to filter, normalize, score, qualify, and segment.
• Data activation across outbound, RevOps, content, and ads.

Plus full outbound and inbound sales workflow breakdowns...

KPIs for production, distribution, and conversion...

And a curated book list to go deeper.

Whether you're a GTM engineer, sales leader, or founder doing outbound yourself...

This is the only reference guide you need.

If you want it for free:

Comment "GTME"

And I'll send it over ASAP.

PS - This cheat sheet includes 20+ tools, 8 book recommendations, and frameworks used by top GTM teams generating millions in pipeline.

---


**作者** weisser（@julianweisser）  
**貼文連結** https://x.com/julianweisser/status/2027841514752380977  

**正文**

When I recorded with Ben for @solofounders he was at $800k.

That was yesterday.

Let me know if you’d like to watch it :)

---


**作者** AIGCLINK（@aigclink）  
**貼文連結** https://x.com/aigclink/status/2027919829794251037  

**正文**

过去30天，128家基于openclaw的初创公司，总计产生了28万美元的真实营收，平均每家月收入约2200刀

其中排名第一的月营收5万刀
TrustMRR上目前收录了128家，还在不断增长中

当下这128家产品的商业模式还比较集中，这其中80%的公司都在做降低OpenClaw使用门槛的活儿，做应用层的只有3-5家，目前商业场景挖掘的还不够深

#Openclaw #openclaw赚钱 #AIagent

---


**作者** vas（@vasuman）  
**貼文連結** https://x.com/vasuman/status/2027762275780571546  

**正文**

A fantastic article that reiterates what I’ve been saying for a year:

AI only drives meaningful ROI for a business when it’s custom built for the way your employees already do their work

People always ask me how Varick competes with “Agentic AI SaaS” and I always respond with there’s a reason why the ROI from SaaS has been precisely 0

If you’re a business owner and can’t seem to figure out why the SaaS you bought to “bring AI benefits to your business” is failing miserably, you are not alone

AI needs to live on top of your existing stack, doing the work that you and your employees are already doing, EXACTLY the way that you are currently doing it

Any other approach is simply guaranteed to fail. This was our thesis over a year ago and we are being vindicated every day.

---


**作者** Luke Pierce（@lukepierceops）  
**貼文連結** https://x.com/lukepierceops/status/2027743439496814760  

**正文**

I went from $500 Upwork projects to $500K+/year selling AI systems.

I legitimately made every mistake you can make.

Undercharging, scope creep, building without mapping, hiring wrong, pricing hourly.

Then I figured out what actually works and doubled down.

I put the entire playbook into a free guide. Here's what's inside:

→ How I went from Zapier gigs to $25K-$60K projects
→ The pricing shift that 5x'd my revenue (and the exact formulas)
→ My 4-call sales process for closing $25K-$60K+ deals
→ The discovery framework that turns calls into signed contracts
→ How I built a dev team without burning cash
→ The fulfillment system that keeps clients for years
→ How I position against agencies 10x my size and WIN
→ The content engine that fills my pipeline without ads or cold outreach
→ Every mistake I made and what I'd do differently starting from zero

This took 4 years, 80+ clients, and a lot of painful lessons.

Yours for free.

RT + reply "AGENCY" and I'll send it over. (Must follow so I can DM

---


**作者** Dhravya Shah（@DhravyaShah）  
**貼文連結** https://x.com/DhravyaShah/status/2027935209963065529  

**正文**

I built the best memory for voice agents while sponsoring @YCombinator hackathon.

Introducing: Voice AI + Memory!

We built a deep @supermemory integration for @pipecat_ai, so now even your agents have great memory

With user profiles, these are almost-instant latency as well :) 
I built the best memory for voice agents while sponsoring @YCombinator hackathon.

Introducing: Voice AI + Memory!

We built a deep @supermemory integration for @pipecat_ai, so now even your agents have great memory

With user profiles, these are almost-instant latency as well :) 
Here's the demo 
https://pipecat.supermemory.ai/ 
Here's the code and docs! https://github.com/supermemoryai/pipecat-memory

---


**作者** swyx（@swyx）  
**貼文連結** https://x.com/swyx/status/2027934989577580988  

**正文**

first podcast with @polsia right after they hit the $1m ARR mark, from a standing start of $50k ARR on Feb 1.

also on the @latentspacepod youtube now 
first podcast with @polsia right after they hit the $1m ARR mark, from a standing start of $50k ARR on Feb 1.

also on the @latentspacepod youtube now 
@polsia @latentspacepod https://youtu.be/Yw-m0PI2Atk

---


**作者** Tadeo Donegana Braunschweig（@tadeodonegana）  
**貼文連結** https://x.com/tadeodonegana/status/2027479756157960618  

**正文**

Built a store management agent with @LangChain deepagents

Shoutout to @hwchase17 @Vtrivedy10 @sydneyrunkle @masondrxy for the posts that got me started

---


**作者** AVB（@neural_avb）  
**貼文連結** https://x.com/neural_avb/status/2027470838916911543  

**正文**

One of the most MUST MUST MUST read articles

---


**作者** Profitable Founder Podcast（@profitfounder）  
**貼文連結** https://x.com/profitfounder/status/2027245195872620960  

**正文**

I built an AI Agents army with OpenClaw to make $1M/year 🦞

0:00 Intro 
1:01 Feather ($250K Exit)
1:41 What is Mission Control HQ? 
2:48 One Agent Wasn't Enough 
5:51 The Lead Agent System
7:42 First 24 Hours with OpenClaw 
9:11 How to Get Started with OpenClaw 
10:33 Don't Install on Your Personal Computer 
12:49 Security tip
14:36 When to Build Mission Control 
17:06 The Retention Specialist Agent 
20:10 Sub-Agents: Always Stay Available
23:04 Why Use Opus for Everything 
24:45 Did It Actually Help You Make Money? 
28:37 100K Emails Auto-Analyzed 
30:08 Built the Entire Dashboard 
33:43 Activation vs Retention 
36:13 Treat It Like an Employee 
39:57 From Assistant to Marketing Machine 
1:15 The Real Bottleneck Is You 
43:45 Excitement About OpenClaw 
46:44 OpenClaw + Hardware 
48:34 It Updates Itself 
49:16 It Created Its Own Notion Account 

with @pbteja1998
I built an AI Agents army with OpenClaw to make $1M/year 🦞

0:00 Intro 
1:01 Feather ($250K Exit)
1:41 What is Mission Control HQ? 
2:48 One Agent Wasn't Enough 
5:51 The Lead Agent System
7:42 First 24 Hours with OpenClaw 
9:11 How to Get Started with OpenClaw 
10:33 Don't Install on Your Personal Computer 
12:49 Security tip
14:36 When to Build Mission Control 
17:06 The Retention Specialist Agent 
20:10 Sub-Agents: Always Stay Available
23:04 Why Use Opus for Everything 
24:45 Did It Actually Help You Make Money? 
28:37 100K Emails Auto-Analyzed 
30:08 Built the Entire Dashboard 
33:43 Activation vs Retention 
36:13 Treat It Like an Employee 
39:57 From Assistant to Marketing Machine 
1:15 The Real Bottleneck Is You 
43:45 Excitement About OpenClaw 
46:44 OpenClaw + Hardware 
48:34 It Updates Itself 
49:16 It Created Its Own Notion Account 

with @pbteja1998
If you liked Bhanu’s podcast.

You should watch this one next:

---


**作者** Mark Vassilevskiy（@MarkKnd）  
**貼文連結** https://x.com/MarkKnd/status/2027420983892852977  

**正文**

Launch Video breakdown for @raindrop_ai 
Launch Video breakdown for @raindrop_ai 
Looking for an IRL launch video?

Let's chat 👇
https://skale.solutions/

---


**作者** Teknium (e/λ)（@Teknium）  
**貼文連結** https://x.com/Teknium/status/2027568675818246207  

**正文**

The external services hermes agent uses:

For Agent Model: @OpenRouter, @NousResearch
Remote Terminals: @modal
For Search & Scrape: @firecrawl
For Browser use: @browserbase
For Voice/TTS: @Microsoft, @elevenlabsio, or @OpenAI
For Image Gen: @fal

Many tools have local alternative options as well!
The external services hermes agent uses:

For Agent Model: @OpenRouter, @NousResearch
Remote Terminals: @modal
For Search & Scrape: @firecrawl
For Browser use: @browserbase
For Voice/TTS: @Microsoft, @elevenlabsio, or @OpenAI
For Image Gen: @fal

Many tools have local alternative options as well!
Some of these have alternatives that could run locally, but aren't setup to - Those options are coming, but I wanted to ensure a great experience guaranteed so I chose those providers to streamline and ensure minimum standards of quality.

But local browser use and voice/image models may come soon :)

---


**作者** Kirk Marple（@KirkMarple）  
**貼文連結** https://x.com/KirkMarple/status/2026800757295689874  

**正文**

Had the perfect @dossium experience today. 

Met with a VC this morning, and as I was pitching, I explained our core value in an elegant way I don’t think I’d said before. 

But after the meeting I couldn’t remember the exact words. 

Thankfully I had my meeting recorder connected to @dossium and it already ingested the transcript after the meeting. 

So I opened the transcript page, went to the “content chat” panel and asked it to extract that part of my pitch in a clean way. 

Seconds later, 💥 perfect concise pitch I can drop into emails or use in our investment memo.

---


**作者** Zephyr（@Zephyr_hg）  
**貼文連結** https://x.com/Zephyr_hg/status/2027309074396668174  

**正文**

While everyone's worried about AI taking jobs, a new class of high-value skills is emerging. The people learning them now will charge whatever they want in 18 months.

There's a pattern I keep seeing that most people are missing.

While everyone panics about AI eliminating jobs, a completely different shift is happening. New skills are becoming extremely valuable. Skills that didn't matter six months ago.

The gap between people who have these skills and people who don't is growing fast. By 2027, the people who figured this out early will be charging $500/hour. The people who ignored it will still be competing on price.

Here are the skills that will print money in 18 months.

## AI System Architecture (Not Coding)

This isn't about learning to code.

It's about understanding how to design systems where AI, automation, and humans work together.

Most businesses are throwing AI at problems randomly. No structure. No thought about how pieces connect. Just "let's use AI for this" without understanding the workflow.

The people who can look at a business, map out the processes, and design a system where AI handles the right parts and humans handle the rest will be invaluable.

This is a thinking skill, not a technical skill. You need to understand business operations, data flow, and system design. Not Python.

By 2027, every mid-sized business will need someone who can do this. There aren't enough people learning it right now.

## AI Training Data Curation

AI is only as good as what you train it on.

Right now, most businesses are feeding AI generic data and wondering why they get generic results.

The skill that's emerging: knowing how to curate, structure, and maintain the data that makes AI actually useful for a specific business.

This isn't data science. It's closer to being a librarian for AI. You know what information the AI needs, how to organize it, how to keep it updated, and how to format it so the AI can use it properly.

Legal firms need AI trained on their specific case types. Marketing agencies need AI trained on their client results and brand voices. Consulting businesses need AI trained on their methodology.

Nobody's teaching this skill systematically yet. The people who figure it out will own the market.

## No-Code AI Workflow Building

The ability to build complex AI-powered workflows without writing code is becoming one of the most valuable skills in business.

Tools like n8n, Make, and Zapier let you connect AI to your business processes visually. Pull data from one place, process it with AI, route it based on the output, trigger the next action.

Most people don't know this is possible. The ones who do are building systems that save businesses 20+ hours a week.

By 2027, every business will need these workflows. The people who can build them will charge premium rates because they're delivering measurable time savings and cost reduction.

This skill is completely free to learn right now. Most people just don't know it's valuable yet.

## AI Output Quality Control

Businesses are generating content and making decisions with AI at scale.

The problem: they have no systematic way to ensure the output is actually good.

The skill emerging: being able to evaluate AI output quality, catch errors AI makes, identify when output is generic versus useful, and build systems that ensure consistent quality.

This combines editorial judgment, brand voice expertise, and understanding of what AI tends to get wrong.

Every business using AI for content, customer communication, or decision support will need this. The people who can do it well will be in massive demand because bad AI output is expensive.

## Automation Maintenance and Optimization

Building automation is one skill. Keeping it running and making it better is another.

Most businesses are building automations but have no one maintaining them. They break. They drift. They stop working as well as they used to.

The skill: being able to audit existing automations, find what's broken or inefficient, and optimize them to perform better.

This is like being a mechanic for automated systems. You don't necessarily build new ones from scratch. You keep the existing ones running well and make them better over time.

By 2027, every business will have dozens of automations. They'll all need someone who can maintain and improve them. This role doesn't exist at scale yet.

## Context Engineering for AI

Everyone's focused on prompt engineering. That's already commoditized.

The skill that's valuable: context engineering. Setting up AI environments where the AI has all the context it needs before you even ask a question.

Instead of writing better prompts, you build better context systems. The AI knows your business, your goals, your past decisions, your preferences. Every interaction is informed by that context.

This is what separates AI that feels like a tool from AI that feels like a team member who knows your business.

The businesses that figure this out will have AI that's 10x more useful than competitors still writing prompts. The people who can build these systems will charge premium rates.

## AI-Human Workflow Design

This is different from system architecture. It's specifically about designing workflows where AI and humans hand off work to each other efficiently.

AI does the first pass. Human reviews and approves. AI implements the changes. Human does final quality check. The workflow is optimized for speed and quality.

Most businesses either let AI do everything (and get poor results) or have humans do everything (and move slowly). The ones that design proper handoff workflows get both speed and quality.

By 2027, every business process will be AI-human hybrid. The people who can design these workflows will be essential.

None of these skills require a degree. None of them require coding. None of them cost money to learn.

They're all accessible right now. You just have to know they're valuable and start learning them before everyone else figures it out.

The people who do will own the market in 2027. The people who wait will be competing for scraps.

If you want to learn the foundations for these skills, the [Mastery Bundle](<https://zephyrhq.gumroad.com/l/mastery-bundle/Article>) is where to start. It covers automation, AI integration, system building, and workflow design. Everything you need to position yourself for these opportunities.

[Get it here →](<https://zephyrhq.gumroad.com/l/mastery-bundle/Article>)

---


**作者** Zack Shapiro（@zackbshapiro）  
**貼文連結** https://x.com/zackbshapiro/status/2027389987444957625  

**正文**

## How I Actually Practice Law with AI in 2026

A few months ago, the night before a client’s acquisition was set to close, the buyer’s counsel sent a letter demanding that several key deal terms be restructured. New escrow conditions. Expanded indemnification carve-outs. A revised set of closing deliverables. The implicit threat: accept these changes or we walk. It was 7 PM.

I uploaded the purchase agreement, the disclosure schedules, and the demand letter to Claude. Within minutes, Claude mapped every proposed change against the existing deal terms and found what the buyer’s lawyers apparently hadn’t noticed: two of their proposed carve-outs directly contradicted representations they had already confirmed in the disclosure schedules, and a third would have created an internal conflict with the fundamental reps section that would have actually weakened the buyer’s own post-closing protections. Their aggressive last-minute play had holes in it.

As the negotiation continued through the evening with emails going back and forth, I fed each new communication to Claude. It tracked how every proposed concession interacted with provisions across the agreement, flagged where accepting one change would create exposure in another section, and helped me build a response that conceded the points worth conceding and held firm on the ones that mattered. By 11 PM we had a clean set of counter-positions, each grounded in specific cross-references to the buyer’s own language. The deal closed the next morning on terms my client was happy with.

A team of three associates at a mid-size firm would have needed until morning to produce that analysis. I had the core of it in under two hours.

I run a two-person boutique law firm. We handle startup formation, venture capital transactions, and regulatory work. We compete against firms with hundreds and sometimes thousands of lawyers. We are not supposed to be able to do this. But the past year has made something clear: a small firm built around AI doesn’t just keep up with larger competitors. It moves faster, produces more thorough work product, and operates at a cost structure that would have been impossible 18 months ago.

The tool I’ve built my practice around is Claude, made by Anthropic. This piece is an explanation of how I actually use it, every day, for real legal work. Not the theory. The workflow.

# Why Claude, Not “Legal AI”

The market is full of specialized legal AI products. Harvey, Spellbook, CoCounsel, Luminance. They all share a thesis: lawyers need AI built specifically for legal work. I’ve evaluated most of them. For a small firm practitioner, a well-configured general-purpose AI is better. It’s not close.

The specialized products are wrappers built on top of the same foundation models that power the general-purpose tools. Their marketing pitch sounds compelling: we’ll customize the AI to your firm’s playbook, train it on your templates, build workflows around your brief bank or clause library. Some of them do this reasonably well. But the pitch contains a fundamental misunderstanding of where the value actually lives.

A template library is not a competitive advantage. Every competent firm in your practice area has roughly the same templates. The NDA, the stock purchase agreement, the employment offer letter. These are commodity inputs. The thing that differentiates a great lawyer from a mediocre one was never the template. It was what the lawyer did with the template: how they spotted the issue the other side buried in Section 14(c), how they knew which indemnification fight was worth having and which to concede, how they structured the advice email so the client actually understood the risk. That is judgment. And judgment doesn’t live at the firm level. It lives at the level of the individual professional.

When legal AI companies talk about customizing AI to a firm’s playbook, they are solving a problem that barely matters and ignoring the one that does. The real leverage comes not from which template the AI starts with, but from the instructionsthat tell it how to think about the work: what to look for, what to flag, how to weigh competing considerations, what format to deliver the output in, what tone to use with the client. Those instructions encode an individual lawyer’s judgment, not a firm’s template library. And that is exactly what Claude’s skill system is built to do.

I’ve created custom instruction files, called “skills,” that encode my analytical frameworks, my preferred formats, my voice, and my judgment about how specific types of legal work should be done. When I upload a contract for review, Claude doesn’t apply a generic framework. It doesn’t even apply my firm’s framework. It applies my framework, the one I’ve developed over a decade of practice, automatically. The difference between a firm playbook and an individual lawyer’s encoded judgment is the difference between giving someone a recipe and teaching them how to cook.

There’s a more fundamental issue, and it’s the one that will matter most to anyone who has spent their career inside Microsoft Word. Claude is a frontier AI model that has been heavily optimized for writing code. That may sound irrelevant to legal practice until you realize what it means: Claude can write code, on the fly, to directly manipulate the applications lawyers already use.

Think about what this means concretely. Every lawyer reading this has lost hours to Word formatting. Paragraph numbering that breaks when you paste from another document. Styles that refuse to cooperate. Track changes that corrupt across versions. Cross-references that go stale. Bluebook citation formatting that requires manual attention on every single period and comma. These are not legal problems. They are software problems. And Claude solves software problems by writing software. When I tell Claude to apply tracked changes to a contract, it doesn’t use a plugin or a macro. It opens the .docx file at the XML level and writes the exact markup that Microsoft Word expects, attributed to my name, preserving every formatting detail. When I tell it to standardize the citation format in a brief, it writes code to parse and reformat every citation in seconds. The result is indistinguishable from expert manual work, delivered in a fraction of the time.

This is the capability gap that no specialized legal AI product can match. They give you a chatbot that talks about documents. Claude is a system that can reach inside those documents and change them. It is the difference between an associate who can tell you what’s wrong with a contract and an associate who can also fix it, format it, produce the redline, and draft the cover email, all without you opening a single application. General-purpose AI advances faster than any vertical product can keep up with. When you’re on the frontier model, every new capability ships to you on day one. When you’re on a wrapper, you’re waiting for someone else’s engineering team to decide what to build next.

I’m describing my own practice here, which is transactional. But nothing about the architecture is practice-specific. A litigator would build skills for deposition preparation, motion drafting, case law synthesis, and discovery review. A tax lawyer would build skills for entity structuring, opinion letter frameworks, and regulatory monitoring. A family lawyer would build skills for asset tracing and custody analysis. The approach is the same: take a powerful general model, teach it your practice, and let it compound your judgment. The content is yours.

## Three Modes

Claude’s desktop app has three modes. Learning when to use each one was the single most important step in making this work.

Chat is the conversational interface. I talk to Claude the way I’d talk to a fast, knowledgeable associate sitting across the table. This is where I go for analyzing a legal issue, brainstorming negotiation strategy, getting a first take on a contract provision, or drafting something from scratch. I stay in control of every step. Most lawyers who have used ChatGPT or similar tools have only experienced this mode.

Coworkis the autonomous mode, and it’s the one that changes everything. I point Claude at a folder on my computer, give it a task, and it goes and does it. It reads files, creates new ones, edits existing documents, and makes its own decisions about how to get from A to B. When I have a 40-page agreement that needs a full redline, or a stack of closing documents that need to be generated from a term sheet, I hand it to Cowork and let it work. This is the mode most lawyers haven’t tried. It’s the one that will change their practice the most.

Code is the development mode. Full terminal access. Most lawyers don’t need it daily. But I have a condition that makes it hard to read long documents, so I used Code to build a command-line tool that converts legal documents into spoken audio. It handles the entire pipeline: parsing Word docs and PDFs, converting legal formatting like “Section 4.2(b)(iii)” into natural speech, expanding abbreviations, chunking the text, sending it to an AI voice API, and assembling the final audio file. I listen to contracts on my commute now. Claude built the whole thing.

## Teaching Claude Your Practice

This is where the leverage becomes something I wouldn’t have believed two years ago.

Anthropic published a guide on building custom “skills” for Claude: structured instruction files that teach it how to behave in a specific context. Not a prompt you type every time. A persistent set of instructions that fires automatically when the situation calls for it. Instead of reading the guide cover to cover, I uploaded it to Claude and asked a better question: based on the hundreds of conversations we’ve had together, spanning contract drafting, client emails, document editing, legal research, and policy writing, what are the skills that would have the greatest impact on my practice?

Claude analyzed months of our work and identified the patterns: which tasks I repeated most, where the friction was highest, where structured automation could save the most time. The skills it recommended weren’t generic. They were specific to how I actually work. Not “draft contracts faster” but “a contract review skill with four distinct modes depending on context, severity ratings, a missing-provisions checklist, market-term benchmarking, and a seamless handoff to a tracked-changes editing skill when you’re ready to mark up the document.”

We refined the details over a couple hours. I pushed back where the defaults didn’t match my preferences. By the end I had six production-ready skills bundled into a single plugin for the Cowork desktop app: contract review, tracked changes editing, contract drafting, client communications, legal research, and policy writing. Each one encodes years of accumulated professional judgment about how I approach that type of work.

The implication that matters for firm management: the plugin is transferable. If I had 50 associates, I could install it on every machine. Every associate would immediately produce contract reviews using my analytical framework, draft communications in my voice, and apply tracked changes in my preferred format. Knowledge that takes years of mentorship to transmit is now an instruction file that works from the first draft. The output still requires attorney review, but the review starts from a much higher baseline.

## What This Looks Like in Practice

Three examples from real work, because I want this to be concrete.

Tracked changes without opening Word. A counterparty sends back a redlined agreement. Forty pages of changes across representations, indemnification, IP, and closing conditions. I upload the document to Claude and say: “Help me evaluate the counterparty’s changes from my client’s perspective.” My contract review skill fires. Claude organizes every change by severity, flags where the counterparty shifted risk, identifies tensions between modified provisions, checks for standard provisions that should be present but aren’t, and produces a summary with specific counter-language for each issue.

Then I apply my judgment. Claude flagged a pattern in the markup. I know from experience what that pattern usually signals. Claude generated three alternative formulations for a disputed clause. I pick the one that accounts for relationship dynamics and deal context that no AI has access to. Once I’ve made my decisions, I tell Claude to apply the edits. This is the part that drops jaws the first time you see it. Claude opens the Word document at the XML level, applies tracked changes attributed to my name, preserves every formatting detail, and produces a clean .docx with real tracked changes that opposing counsel can open in Microsoft Word and review normally. I don’t open Word. I don’t open Litera. Claude produces the redline. I review every change, and I send it. Then the client communications skill drafts the cover email in the right tone. Total time from receiving the markup to having a response package ready to send: under an hour, of which about 30 minutes is my own thinking.

Research without hallucinations. A client needs to understand the regulatory landscape for a new product. The question spans multiple agencies and overlapping statutory frameworks. My research skill instructs Claude to launch parallel research across every relevant angle simultaneously rather than working through them sequentially: the securities analysis, the state licensing requirements, the banking regulations, the consumer protection implications. It runs multiple searches per sub-topic, cross-references sources, and prioritizes primary authority (statutes, regulations, agency guidance, case law) over secondary commentary.

Before delivering anything to me, the skill requires Claude to run a self-review. This is critical, and it’s the part most people skip. Claude must verify that every cited authority actually says what the memo claims. It must flag anything where its confidence is below high. It must check for internal contradictions across sections. And it must specifically guard against hallucinated citations, the problem that got several lawyers sanctioned and made national news. The lawyers who submitted fake AI-generated citations were using tools without this kind of verification layer. The problem was never AI itself. It was AI without quality control.

The output is a structured research memo, with a bottom-line-up-front summary, specific statutory citations, and practical recommendations, that would take a junior associate days to produce. Claude delivers a first draft in under an hour. I then review every citation, stress-test the analysis, and revise where my judgment diverges from the output. The total time is still a fraction of what it would take starting from scratch. And because the skill is calibrated to my standards (confident conclusions with explicit uncertainty flags, tables for comparing regulatory frameworks, practical recommendations rather than academic hedging), the memo is useful immediately.

Real-time contract interpretation. A client called mid-morning to say they had just received a demand letter from a counterparty claiming breach of a commercial services agreement and threatening termination. The client had 48 hours to respond. I uploaded the agreement, the demand letter, and the client’s last three months of correspondence with the counterparty. Claude mapped every factual allegation in the demand letter against the specific contract provisions cited, and found that two of the four claimed breaches referenced obligations that had been expressly modified by a side letter the counterparty’s own counsel had drafted. The demand letter appeared to have been written without checking their own amendments. As I prepared the response, I ran each draft paragraph through Claude to pressure-test whether any of my arguments had unintended implications for other provisions in the agreement. It caught one: a defense I was planning to raise on the service-level metrics could have been read to concede a point on the payment dispute in Section 7. I rewrote the response. That kind of real-time, provision-by-provision stress-testing while actively drafting is something that used to require a second lawyer reviewing your work. Now it happens in the same conversation where the work gets done.

## The Privilege Question

Every lawyer asks. The short answer: the same framework that lets you use cloud storage, e-discovery platforms, and online legal research databases applies here. ABA guidance and state bar ethics opinions treat AI tools as third-party technology providers covered by the agent/instrumentality exception. Your obligations are to make reasonable efforts to protect client data, which in practice means turning off model training on your inputs, understanding the provider’s data handling practices, and documenting your reasoning. Anthropic offers a zero-data-retention API option and business data processing agreements, so that none of your client data is used to train models, and inputs are not stored beyond the session. The same diligence you performed before putting client documents in Dropbox, Google Drive, or Clio.

I went a step further. I had Claude help me draft an AI usage provision for my engagement letters. The provision frames AI as an efficiency and quality enhancer, emphasizes attorney supervision, ties data handling to existing confidentiality obligations, and secures client consent. Clients sign it without blinking. Most of them assume I’m already using AI. They’re right.

The ethics rules now require technology competence in most jurisdictions. We are approaching the point where not using these tools is the harder professional responsibility position to defend.

## The Prompt Is the Skill

Most lawyers who try AI write something like “review this contract” and get back something mediocre. Then they decide AI isn’t useful for legal work.

The problem is not the AI. The problem is the input.

Compare “review this contract” with “review this services agreement from the vendor’s perspective. Flag provisions where the customer shifted risk beyond market norms for this type of deal. Check for missing provisions that should be present, including limitation of liability, IP ownership, data handling, and termination for convenience. Produce a severity-rated summary with specific counter-language for each high-severity issue. Note that the vendor has limited negotiating leverage and wants to close the deal, so recommendations should focus on provisions worth fighting for versus provisions to concede gracefully.”

The second version produces work product that is useful on the first pass. The first produces work product that requires extensive revision, if it’s useful at all. The entire gap between “AI is a toy” and “AI changed my practice” lives in the quality of your instructions. This is why skills matter: they encode that level of detail so you write it once and it fires every time.

## What This Changes

A few things follow from all of this that are worth naming.

Staffing.I run a two-person firm that handles the workload of a much larger practice. That is a direct function of AI. The work that traditionally justified an associate hire, first-pass document review, research memos, initial drafts, redline summaries, routine correspondence, is now handled by Claude under my supervision. To be clear: every document that leaves my firm has been reviewed, revised, and approved by a licensed attorney. AI produces the first pass. I produce the final work product. Associates are not obsolete. But the bar for when hiring one makes economic sense has moved. And what you need them to do has changed: judgment, client relationships, and AI output supervision, not 2,000 hours of document production.

Billing.AI changes the value equation. For some tasks, the time savings are obvious and I pass them on to clients. For others, the same hours produce dramatically deeper analysis, more comprehensive issue-spotting, and higher-quality drafting than would have been possible before. The point is not that every task takes less time. It is that every hour of attorney time produces more value. My firm offers subscription pricing alongside traditional hourly billing, depending on the engagement. The subscription clients get ongoing advisory, contract review, compliance monitoring, and routine governance for a flat monthly fee. No meter running. AI makes this model work, because I can deliver more comprehensive service within a predictable fee structure. Clients love it: they’re not afraid to pick up the phone or send an email. And the revenue is predictable instead of lumpy.

Judgment.Everything I’ve described creates a temptation to let the AI do too much. To stop checking. The research on this is consistent: people who use AI outside its competence, or who trust it without interrogating the output, perform worse than people who don’t use AI at all. The lawyers who will win with this technology understand at a foundational level that the AI is not practicing law. You are practicing law. The AI makes you faster, more thorough, and more consistent. But the judgment, the part where you decide what to fight for and what to concede, where you read between the lines, where you make a call that could go either way and stake your reputation on it, that is yours. Experienced lawyers have an enormous advantage in this new world, and most of them don’t realize it. If you’ve spent 10 or 20 years developing judgment in your practice area, you are sitting on exactly the asset that AI makes more valuable, not less.

## Go Build

I don’t work for Anthropic. I’m a practicing lawyer who tried every AI tool available and built my practice around the one that worked best for how I actually work.

The gap between how most lawyers use AI (typing a question into a chatbot and hoping for the best) and what I’ve described here is enormous. Closing that gap doesn’t require technical skill. It requires investing a few hours in learning how the tool actually works: the difference between Chat and Cowork, why long detailed prompts produce dramatically better results than short ones, how to build a skill that encodes your judgment, how to bundle skills into a plugin that any colleague can use.

Download the desktop app. Pick the task you do most often. Write a prompt that describes, in detail, exactly how you want it done. See what comes back. Then build your first skill. The returns compound fast.

---


**作者** AVB（@neural_avb）  
**貼文連結** https://x.com/neural_avb/status/2027425381230555354  

**正文**

This is essentially a "survival guide" for training Deep Research agents with Small Language Models (SLMs). This article is entirely based on a new research paper that came out earlier this week.

You can find the the paper on Arxiv: [https://arxiv.org/abs/2602.19526](<https://arxiv.org/abs/2602.19526>)

Basically, they did a study comparing the role of RL-trained research agents across three different dimensions: Prompt Templates, Reward Functions, and Policy Optimization. 

All the experiments were performed on really small models in the 3B and 7B param range. Models so small, you can pretty much run them on your computer right now.

They had some pretty interesting findings, and a lot of educational takeaways! Let's get into it.

# 1. The Problem

> So what are research agents?

![Article Image](<https://pbs.twimg.com/media/HCLZKoHaQAA-4qb.jpg>)

Basically, a Research Agent is an AI system designed to solve "knowledge-heavy" problems that can't be answered with the model's own world knowledge. Instead, it must use a set of tools to go out, interact with a knowledge base, find new information, and synthesize into a response.

A research agent needs to be:

1. Good at identifying pieces of information it's missing
1. Generate search queries
1. Reason through multiple (often conflicting) sources of information and 
1. Consolidate into a response.


## 2. The Experiment

The researchers took existing small models from the Qwen2.5 family: Qwen2.5-3B, and Qwen2.5-7B. These models have basic language skills, but not enough tool-calling skills.

Using Supervised Finetuning, they first finetuned these base models on search trajectories from larger models. This teaches them basic tool-calling skills and how to reason through their searches.

Once the SFT phase completes, we are ready for the more challenging part - Reinforcement Learning. During RL, we increase the likelihood of models picking trajectories that lead to successful searches (we will soon see how!)

Specifically, they explore 3 different axes on which to measure RL training:

1. Prompt Template: Fast vs. Slow Thinking
Defining how much should LLMs think before picking an action

1. Reward Function: F1 vs. Exact Match
This dimension explores how to "score" the model's final answer as reward.
1. Policy Optimization: REINFORCE vs. PPO vs. GRPO
What RL algorithms to use to train these small language models? 

We will soon see what their results were, but first let's unpack their environment design.

## 3. Environment Design

RL requires the environment to be presented as a  sequential decision-making problem. The agent operates in a multi-round loop where it interacts with a retrieval system with a bunch of tools, before aggregating the final answer.

![Article Image](<https://pbs.twimg.com/media/HCLai2fa0AAH5Ad.jpg>)

## 3.1  The Action Space 


Agents follow a simple "think-search-rethink-answer" cycle.

The environment is controlled by specific XML-style tags that trigger environment actions:

(a) <search> query </search>: Triggers the retrieval engine.
(b) <answer> text </answer>: Ends the episode and submits the final result.
(c) <think> ... </think>: Internal reasoning (used in the "Slow Thinking" setup mentioned next)

## 3.2 Reasoning

They experiment with how training is impacted by how the agent reasons. 

 Slow Thinking Template: The model is forced to use <think> tags before every search and answer. This is the traditional way models like DeepSeek-R1 work.

Fast Thinking Template: The model goes STRAIGHT to the action (searching or answering) without mandatory, long-form thinking blocks

> Note that fast thinking is NOT equivalent to no thinking. The model can still generate some monologue before outputting the <search> or <answer> tags.  Fast thinking just means no EXPLICIT <think> tags, and no explicit mention of reasoning in these prompts.

![Article Image](<https://pbs.twimg.com/media/HCLaAV5bEAAOM8u.jpg>)

## 3.3 The Search Engine 

They used a Wikipedia snapshot from 2018. They used this static knowledge base (instead of direct web search) to maintain reproducibility. 

Basically, when the agent generates a <search> tag, the system retrieves the top-3 most relevant passages from Wikipedia and injects them back into the model's context between <information> and </information> tags.

The model reads it and performs the next step.


3. Episode: For training research agents, we also need search prompts and their corresponding correct answers. Wikipedia is just the knowledge base, it does not contain what to search or how to verify answers.

They combined NQ (Natural Questions) and HotpotQA (a multi-hop reasoning dataset) datasets to generate each episode.

An episode therefore contains the below steps:

- Sample a question from the dataset
- Let the LLM use the think, search, and answer tools to browse Wikipedia to get answers
- Verify if the final answer was correct.

The final step is to give a reward to the agent based on it's answer.

![Article Image](<https://pbs.twimg.com/media/HCLateqa4AAiBz2.jpg>)

## 3.4 Reward

The most basic way to train an RL agent is to give it a reward only at the very end based on its final answer. They try 2 approaches:

- EM (Exact Match): A "hard" binary reward. If the answer is 2017, and the model says 2017, it gets 1 point. If it says "the year 2017," it gets 0. :(

Effect: This forces the model to be very precise and concise. BUT The reward space gets sparser.

- F1 Score: This is a "soft" reward. It gives partial credit based on how many words in the model's answer overlap with the correct answer.

The Problem: Model gets some rewards even if the responses are partially correct, or missing important keywords

With a higher budget, people could (should have) also use LLM as a judge methods to evaluate answers. Basically you pass the generated answer and the expected answer to an LLM, and it generates a numerical reward. 

## 3.5 Training algorithm

They tested with 3 popular RL algorithms for reasoning research - REINFORCE, GRPO, and PPO. Next section has all the details about their findings. (To the surprise of nobody who has been paying attention to SLM reasoning research - REINFORCE won)

## 4. Some Takeaways from the Paper

Remember that these conclusions were drawn with 3B and 7B models. Their goal was to train Small Research Agents - so some of these results will not translate to larger models!

![Article Image](<https://pbs.twimg.com/media/HCLZXv2aEAARXQg.jpg>)

4.1 "The Less Thinking, the Better" 

Surprisingly, the popular "Slow Thinking" approach (where you force the model to write out its thoughts in a <think> block before acting) actually hurts performance in deep research for SLMs.

![Article Image](<https://pbs.twimg.com/media/HCLaJK9bsAAJsob.jpg>)

- The Problem: In multi-round searches, "Slow Thinking" often leads to training collapse where the model starts generating empty thinking blocks or gets stuck in loops! Better SFT or bigger models could solve this, but it increasing training costs.

- The Fix: They found that Fast Thinking—where the model goes straight to a search action or an answer—is much more stable and achieves higher accuracy across benchmarks.

4.2 Answer Avoidance in F1 Scoring

Most RL training uses Exact Match (EM) or F1 scores as rewards. 

> They found that optimizing for F1 led to way more unstable training then F1

Specifically they discovered that F1 objectives lead to training collapse. Basically, the agent learns to "cheat" by refusing to answer. It realizes that if it doesn't give an answer, it isn't "wrong," so it avoids the risk of a low F1 score.

The Solution (F1+): They introduced Action Supervision, and created a new reward function called F1+. Basically, they added auxilliary penalties:

- If the model refuses to answer, it gets a penalty
- If the model repeats a query exactly, it gets a penalty
- If a search returns no new information, it gets a penalty.

![Article Image](<https://pbs.twimg.com/media/HCLZiEDa0AEX9tz.jpg>)


By adding penalties for "refusal" (not answering) and for "over-searching" (wasting too many search steps), they revitalized F1 rewards. This new F1+ reward eventually outperformed simple Exact Match (EM).


4.3 REINFORCE Beats PPO and GRPO!  (many have been saying it too!)

In many modern LLM projects (like DeepSeek-R1), algorithms like GRPO are the stars. But for Deep Research:

- GRPO is the least stable
- PPO vs GRPO: PPO outperforms GRPO on Single-Hop tasks, while GRPO exhibits superior capability on Multi-Hop benchmarks
- REINFORCE is King: It proved to be the most stable and achieved the highest accuracy. It also learnt the most compact policies - fewest searches on average to get to answers.

![Article Image](<https://pbs.twimg.com/media/HCLZ1meaAAAVOe5.jpg>)

- Why? 

Basically, REINFORCE by design just tries to make an unbiased estimator strictly based on the rollout trajectories, i.e. no critic, no advantages. It purely learns from generated rewards. This traditionally causes high variance in RL environments and longer training times, but it actually outweighs the cons of PPO and GRPO, esp for this small LM multi-step environment.

PPO and GRPO introduce auxiliary mechanisms to reduce variance, with PPO utilizing a critic model and GRPO employing group averaging. 

To directly quote the paper:


> In multi-step, long-context reasoning, the high variance of actions within a group makes the baseline noisy, leading to training instability. ....
>
> In scenarios with sparse outcome rewards (EM), fitting an accurate value function over long trajectories is challenging. This difficulty often leads to critic bias that fails to penalize redundant searches, explaining PPO’s high and unadaptive search cost. 
>
> REINFORCE, by contrast, optimizes the policy based on the direct cumulative return without relying on external baseline. By avoiding the noise from group sampling and the bias from critic estimation...

## 5. The Recipe

By combining the three insights above - Fast Thinking, F1+ Reward,  REINFORCE—they created a new baseline called Search-R1++.

Read the paper for more details and benchmarks! It also contains prompts and detailed trajectory examples!

It remains to be seen how much these results translate to larger benchmarks and larger model training in the (70B - 400B+) range!

Follow me for more breakdown: @neural\_avb 

Read this paper with an LLM assistant for free (if you on a computer): https://paperbreakdown.com/abs/2602.19526

A bit of kindness goes a long way, appreciate an RT or a comment to support!💙

---


**作者** Lance Martin（@RLanceMartin）  
**貼文連結** https://x.com/RLanceMartin/status/2027450018513490419  

**正文**

TL;DR – [Programmatic tool calling](<https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling>) (PTC) is an interesting capability in Claude Opus/Sonnet 4.6. Instead of making tool calls that each round-trip through Claude's context, Claude writes code that can orchestrate tool calls directly inside a container. Intermediate tool results return to the code, not Claude’s context window. This reduces token usage and improves performance on multi-step tasks like search. Opus 4.6 with PTC recently scored #1 on [LMArena’s search benchmark](<https://x.com/arena/status/2027095484834398512?s=20>). See our docs to learn more about [PTC](<https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling>) and our new [web search](<https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool>) tool that uses PTC by default.

Computer use is one of Claude’s most central capabilities. Just giving Claude a [bash tool](<https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool>) opens up a broad action space and leads to a common question: [is bash all you need](<https://x.com/trq212/status/2008278253799195042?s=20>)? And how to decide what other tools to give an agent?

Actions are how Claude interacts with the world. Tools are a way to declaratively specify the actions that Claude can take. The API lets you add [tools](<https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview>) by giving Claude a tool name, description, and input arguments.

![Article Image](<https://pbs.twimg.com/media/HCGdHACbsAASflf.jpg>)

If Claude wants to call a tool, it will respond with a JSON object of tool arguments to run. A tool handler (e.g., [MCP server](<https://platform.claude.com/docs/en/agents-and-tools/mcp-connector>), code you write, etc) runs the tool and passes back context. If you run this in a loop, you [have an agent](<https://www.anthropic.com/engineering/building-effective-agents>). For example, the [bash tool](<https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool>) produced bash commands by generating a JSON object with the command. It is passed to a bash tool handler to execute:

When to use tools

Claude with a [bash tool](<https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool>) running in a loop is a computer-use agent. This is central to Claude Code. But Claude Code doesn’t just use bash. It uses tools as a control surface around certain actions. See @trq212's [breakdown on these points](<https://x.com/trq212/status/2027463795355095314?s=20>). Promoting an action to a tool can make sense in a few cases:

- UX:  @trq212 [talks about](<https://x.com/trq212/status/2027463795355095314?s=20>) the AskUserQuestion tool. This examples shows that tools are useful in cases where specific actions need to be caught and rendered to the user in a particular way.
- Guardrails. Some actions need guardrails. For example, a file edit tool can run a staleness check to verify that the file hasn't changed since the model last read it.
- Concurrency control. Sometimes it's useful to group actions by concurrency safety (e.g., read-only tools can run in parallel).
- Observability. It can be useful to isolate specific actions for logging (e.g., measuring latency or token usage).
- Autonomy. You may want to group actions by autonomy-level. If the harness can undo an action, it can approve the action more freely. 

The problem with tools

Tools trade-off control with composability. Consider three actions as tool calls. The context from each tool call is returned back to Claude. Each round trip costs latency, serializes the tool result into context (e.g., it will pass thousands of rows even if the next step only needs five), and introduces a reasoning step. The composition tax grows with the number of actions.

Programmatic tool calling

Claude is developing a capability that unites the composability of code with the control surface of tools. Claude can perform programmatic tool calling (PTC, see [docs here](<https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling>)): you can define tools, as usual. But rather than calling them individually, Claude can compose them as functions and run them in a code execution container. The output of each function returns to the container rather than to Claude’s context window.

![Article Image](<https://pbs.twimg.com/media/HCGkQ6QasAAgSrB.jpg>)

When the code calls a tool (e.g., await web\_search(query)) the container pauses. The call crosses the sandbox boundary as a typed tool-use event. It is fulfilled just as if the model directly called the tool (e.g., via a handler, an MCP server etc). But the result returns to the running code, not to Claude's context window. The code processes it following the control flow that Claude specified (e.g., calls another tool, filters the data, accumulates results). Only the final output reaches Claude.

With[ Opus 4.6](<https://www-cdn.anthropic.com/0dd865075ad3132672ee0ab40b05a53f14cf5288.pdf>), we’ve seen gains in token efficiency and performance on non-coding evals (e.g.,[ BrowseComp](<https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf>) and[ DeepsearchQA](<https://storage.googleapis.com/deepmind-media/DeepSearchQA/DeepSearchQA_benchmark_paper.pdf>) for[ web search](<https://claude.com/blog/improved-web-search-with-dynamic-filtering>)) with PTC. For example, rather than pulling 50 raw search results into context for Claude to reason over, the code can parse, filter, and cross-reference results programmatically. This keeps what's relevant and discards the rest (e.g.,[ dynamic filtering](<https://claude.com/blog/improved-web-search-with-dynamic-filtering>)). Across BrowseComp and DeepsearchQA, it improved accuracy by an average of 11% while using 24% fewer input tokens. Opus 4.6 with PTC is currently #1 in LMarena’s [Search Arena](<https://x.com/arena/status/2027095484834398512/photo/1>).

![Article Image](<https://pbs.twimg.com/media/HCLFEueacAAO9JP.jpg>)

With these gains in mind, PTC is now built-into to the [web search tool](<https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool>) on the API to boost performance and save token when using search:

PTC is a way to get the benefit of code execution (e.g., composability) while preserving the control surface of tools: tool implementations run on your side of the sandbox, not inside it. The tool handlers still sit in the middle of every call as a control surface, able to inspect, reject, log, or queue for human approval. But it allows Claude to fluently orchestrate actions in code. 

---


**作者** Varun Anand（@vxanand）  
**貼文連結** https://x.com/vxanand/status/2027412333828468878  

**正文**

Our new Head of Sales Development has one job: don't embarrass us. 

Here's an inside look at how we're building @Clay's first ever SDR team:

You might be thinking, "Wait, what's up with that? I thought Clay was making it so there would never be SDRs ever again?" Wrong. So, I sat down with Rob Cook to walk through how we're re-thinking the SDR role in the age of AI.

We get into:

- What Clay-powered SDRs actually do all day
- The two types of salespeople we're hiring and why the goal is to turn them into one
- Our key success metrics for the ClayDR team (it's not just pipeline)
- When to go bespoke vs. scale: How we decide between 10 custom touches for always-on accounts and many-to-one plays for awareness
- Why "don't embarrass us" is actually the most important charter and what that means for how our SDRs engage with prospects

Plus, much, much more. In the end, Rob shares why it bothers him so much when folks say they feel badly for SDRs and "how hard the job is."

And why our #1 goal is to bring the joy back to business development.

Watch below 👇

---


**作者** Stanley（@Stanleysobest）  
**貼文連結** https://x.com/Stanleysobest/status/2027332746394394808  

**正文**

刷到小学生玩OpenClaw，瞬间破防。

卷不过同龄人就算了，

现在连小学生都卷不过了，

老登出路在哪？ 

---


**作者** Kirk Marple（@KirkMarple）  
**貼文連結** https://x.com/KirkMarple/status/2027589766385172728  

**正文**

This was the kind of call that makes all the late nights and weekends worth it. 

And, tonight I got @crustdata integrated and will post a demo video of @dossium + Crustdata this weekend.

(Round closing next week, btw.  DM open) 

---


**作者** 向阳乔木（@vista8）  
**貼文連結** https://x.com/vista8/status/2027404900335063285  

**正文**

终于看到靠谱的日更AI资讯聚合，来自著名的AI Newsletter：latent. space

如果没时间精力，读这个频道就够，不用折腾。

信息源：12个Reddit子版、500多个 Twitter账号 和 24 个 Discord频道，每天累计上万信息筛选精华。

这家专业性靠谱，Ben's bite也很好，但是周更。

地址见评论区，建议收藏
终于看到靠谱的日更AI资讯聚合，来自著名的AI Newsletter：latent. space

如果没时间精力，读这个频道就够，不用折腾。

信息源：12个Reddit子版、500多个 Twitter账号 和 24 个 Discord频道，每天累计上万信息筛选精华。

这家专业性靠谱，Ben's bite也很好，但是周更。

地址见评论区，建议收藏
网址  https://www.latent.space/s/ainews

---


**作者** Lenny Rachitsky（@lennysan）  
**貼文連結** https://x.com/lennysan/status/2027535415692218425  

**正文**

Over 75,000 workshop registrations so far 🤯

http://bit.ly/ai-native-pm 

---


**作者** Tadeo Donegana Braunschweig（@tadeodonegana）  
**貼文連結** https://x.com/tadeodonegana/status/2027478696286658778  

**正文**

I work as an AI Engineer at Tiendanube (Nuvemshop), one of Latin America's largest e-commerce platforms. We already ship agents with LangGraph and Langchain in production, and the LangChain ecosystem

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2027428521157792067  

**正文**

.@ArzuleAI builds AI agents that help B2B SaaS companies identify which partnerships will drive revenue, prioritize them, and track ROI so partnerships become a more automated and predictable growth channel.

Congrats on the launch, @NickelReady and @Jeffjinlin!

https://www.ycombinator.com/launches/PYp-arzule-ai-agents-that-turn-b2b-partnerships-into-a-scalable-revenue-channel

---


**作者** weisser（@julianweisser）  
**貼文連結** https://x.com/julianweisser/status/2027488413243609512  

**正文**

$200k->$800k in a week. Completely solo.

Talking with Ben in 2.5 hours for @solofounders.

What should I ask?

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2027413415250296894  

**正文**

End Close builds automatic reconciliation for payments companies, replacing manual ops work with AI agents that automatically investigate and resolve every exception.

This team previously reconciled $1,000,000,000,000 at Modern Treasury.

Congrats on the launch, @SeanBolton and @DavidNewell95!

https://www.ycombinator.com/launches/PYm-end-close-solving-payments-reconciliation-with-ai-agents

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2027496462301757784  

**正文**

Autostep uncovers repetitive tasks ready for AI. Then builds or finds the agents to solve them.

Your team repeats the same work hundreds of times a week. No one notices. Autostep does.

Congrats on the launch, @aidan__pratt!

https://www.ycombinator.com/launches/PYq-autostep-uncover-repetitive-tasks-ready-for-ai 

---


**作者** Andrej Karpathy（@karpathy）  
**貼文連結** https://x.com/karpathy/status/2027521323275325622  

**正文**

I had the same thought so I've been playing with it in nanochat. E.g. here's 8 agents (4 claude, 4 codex), with 1 GPU each running nanochat experiments (trying to delete logit softcap without regression). The TLDR is that it doesn't work and it's a mess... but it's still very pretty to look at :)

I tried a few setups: 8 independent solo researchers, 1 chief scientist giving work to 8 junior researchers, etc. Each research program is a git branch, each scientist forks it into a feature branch, git worktrees for isolation, simple files for comms, skip Docker/VMs for simplicity atm (I find that instructions are enough to prevent interference). Research org runs in tmux window grids of interactive sessions (like Teams) so that it's pretty to look at, see their individual work, and "take over" if needed, i.e. no -p.

But ok the reason it doesn't work so far is that the agents' ideas are just pretty bad out of the box, even at highest intelligence. They don't think carefully though experiment design, they run a bit non-sensical variations, they don't create strong baselines and ablate things properly, they don't carefully control for runtime or flops. (just as an example, an agent yesterday "discovered" that increasing the hidden size of the network improves the validation loss, which is a totally spurious result given that a bigger network will have a lower validation loss in the infinite data regime, but then it also trains for a lot longer, it's not clear why I had to come in to point that out). They are very good at implementing any given well-scoped and described idea but they don't creatively generate them.

But the goal is that you are now programming an organization (e.g. a "research org") and its individual agents, so the "source code" is the collection of prompts, skills, tools, etc. and processes that make it up. E.g. a daily standup in the morning is now part of the "org code". And optimizing nanochat pretraining is just one of the many tasks (almost like an eval). Then - given an arbitrary task, how quickly does your research org generate progress on it?

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2027096329667670288  

**正文**

.@ResslAI deploys AI employees at field ops businesses to automate their office work - responding to leads, booking jobs, sending estimates, etc.

Their agents sit on existing software and increase operating margins.

Congrats on the launch, @arushi_ressl and @AbhishekEswaran!

https://www.ycombinator.com/launches/PXv-ressl-ai-ai-employees-for-the-trades

---


**作者** Simon Willison（@simonw）  
**貼文連結** https://x.com/simonw/status/2020161285376082326  

**正文**

I wrote about the most ambitious form of AI-assisted software development I've seen yet - Strong DM's "Software Factory" approach, where two of the guiding principles are "Code must not be written by humans" and "Code must not be reviewed by humans" https://simonwillison.net/2026/Feb/7/software-factory/
I wrote about the most ambitious form of AI-assisted software development I've seen yet - Strong DM's "Software Factory" approach, where two of the guiding principles are "Code must not be written by humans" and "Code must not be reviewed by humans" https://simonwillison.net/2026/Feb/7/software-factory/
Updated my post to add a section with commentary on the glaring detail I glossed over in my first published version: $1,000/engineer/day in token spends, really? https://simonwillison.net/2026/Feb/7/software-factory/#wait-1-000-day-per-engineer-

---


**作者** Ben Cera（@bencera_）  
**貼文連結** https://x.com/bencera_/status/2023765284562358537  

**正文**

I built an AI that runs companies autonomously. It told me it needs more compute and that it should raise the money itself.

So I gave it my inbox for 14 days. 

Watch it live: http://polsia.com/live 

---


**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2027320336413602018  

**正文**

这几天一直在做设计 Agent

终于在 Nanabonana 2 上线的时候赶出来了！

内嵌在我的开源 Claude Code 桌面端 Codepilot里。

能选参数、能连续编辑、还有素材库帮你管提示词和收藏图片，我的提示和思路后续都会内置到里面。

------

录个视频介绍一下：

支持Nano Banana、 Pro 和 2三个模型生图

参数自由选择：想要什么风格、什么比例，自己定。

连续编辑：反复调整细节的时候特别有用。

## 素材库

内置素材库可以收藏用过的好图，也能快速找到之前写过的提示词。下次想生类似风格的图，直接从素材库调，效率翻倍。

## 设置方法 5 步搞定：

1. 去 Google AI Studio 申请一个 API Key 
2. 打开 Codepilot 设置，找到服务商 
3. 点进 Google Gemini (Image) 
4. 把 Key 填进去 
5. 回到聊天页面，切换到 image-Agent 模式
这几天一直在做设计 Agent

终于在 Nanabonana 2 上线的时候赶出来了！

内嵌在我的开源 Claude Code 桌面端 Codepilot里。

能选参数、能连续编辑、还有素材库帮你管提示词和收藏图片，我的提示和思路后续都会内置到里面。

------

录个视频介绍一下：

支持Nano Banana、 Pro 和 2三个模型生图

参数自由选择：想要什么风格、什么比例，自己定。

连续编辑：反复调整细节的时候特别有用。

## 素材库

内置素材库可以收藏用过的好图，也能快速找到之前写过的提示词。下次想生类似风格的图，直接从素材库调，效率翻倍。

## 设置方法 5 步搞定：

1. 去 Google AI Studio 申请一个 API Key 
2. 打开 Codepilot 设置，找到服务商 
3. 点进 Google Gemini (Image) 
4. 把 Key 填进去 
5. 回到聊天页面，切换到 image-Agent 模式
这里尝试：https://github.com/op7418/CodePilot/releases
有啥需求可以提 Issue 和提 PR 啊
搞了个用户群：https://x.com/op7418/status/2027376838344077389?s=20

---


**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2027303093105488002  

**正文**

六种流行claws的完整对比https://x.com/MisbahSy/status/2025570052108665231 

---


**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2027304641961365999  

**正文**

一张“瀑布图”讲清2026年AI Agent的渗透路径

软件工程先满溢，然后外溢到后台、销售、财务。

真正的扩散正在加速。 

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2027058535432122384  

**正文**

Trace (@trace_so) has raised $3M to build the context layer between AI agents and how companies actually operate.

They help teams turn AI pilots into real workflows that actually stick.

Congrats to the team on the raise!

https://techcrunch.com/2026/02/26/trace-raises-3-million-to-solve-the-agent-adoption-problem/

---


**作者** Gregor Zunic（@gregpr07）  
**貼文連結** https://x.com/gregpr07/status/2027225644304843160  

**正文**

The infra god has spoken

---


**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2027263044678713359  

**正文**

yc founder is using my product to teach him how to fry an egg and get girls.

should i pivot? 

---


**作者** Dhravya Shah（@DhravyaShah）  
**貼文連結** https://x.com/DhravyaShah/status/2027136664741830921  

**正文**

claude just validated (killed) our product :)

@supermemory's claude code plugin's launch had these exact words (learns debugging patterns, preferred approaches, project context). 
 
awesome to see the big labs adopting memory! 

---


**作者** Kirk Marple（@KirkMarple）  
**貼文連結** https://x.com/KirkMarple/status/2026806497657978964  

**正文**

The Problem with Hub-and-Spoke Architectures
Tools like Claude CoWork, Glean, and similar AI assistants that connect to your data sources all share the same fundamental architectural limitation: they

---


**作者** Scott Morton（@scottgmorton）  
**貼文連結** https://x.com/scottgmorton/status/2027043531085455823  

**正文**

Today we announced our $150M Series B led by @IndexVentures with major participation from @Redpoint and returning investors including @ThriveCapital, @felicis, and @AbstractVC.

Across aerospace, energy, and manufacturing, engineering teams are pushing what’s possible. The software behind many of these systems hasn’t kept up. Revel gives engineering teams the infrastructure to test and control complex hardware systems with speed and confidence. In just over a year, we’ve built a world-class team, converted every pilot into a customer, and are now expanding the platform across new industries. If you believe great hardware deserves great software, we’re hiring across the board.

Read the full announcement here: https://www.nytimes.com/2026/02/26/business/dealbook/revel-software-hardware-fund-raise.html

---


**作者** Ray Wang（@wangray）  
**貼文連結** https://x.com/wangray/status/2026450898105544810  

**正文**

大多数产品团队还没有搞清楚 Karpathy 在说什么。

软件的新分发渠道是 Agent。Agent 不会看你的官网，不会看 demo，不会走新手引导。它直接调你的 CLI，请求你的 MCP server，把你的文档当数据读。如果这些入口都没有，你的产品对它来说根本不存在。

MCP 从零到每月近亿次 SDK 下载，只用了 12 个月，有超过1万个活跃服务器。OpenAI、Google、微软、Cloudflare 全都跟上了。后来，Anthropic 把 MCP 捐给了 Linux 基金会——因为这个标准已经赢了。运行一个 MCP server，现在等同于运行一个 web server，这是产品被发现的新门槛。

一个做得再好看的 React 仪表盘，对凌晨 3 点还在跑工作流的 Agent 来说，没用。

Unix 哲学几十年前设计出来，现在发现它天然就是给 AI Agent 用的。

接下来 24 个月，赢的是现在就在搭“Agent 能接进来”的入口的公司。输的那些，还在优化官网首页落地文案。

---


**作者** Nicolas Bustamante（@nicbstme）  
**貼文連結** https://x.com/nicbstme/status/2026804225314009589  

**正文**

Product-market fit has a prerequisite that most AI founders ignore. Before the market can pull your product, the model must be capable of doing the job. That's Model-Market Fit.
The Andreessen

---


**作者** Johannes Landgraf（@jolandgraf）  
**貼文連結** https://x.com/jolandgraf/status/2026774083988279627  

**正文**

love the microsite from @loujaybee touching on the false summit of coding agents, and how to address the system bottlenecks standing between you and a self-driving codebase

background-agents . com 

---


**作者** Mani（@maniusmaximus）  
**貼文連結** https://x.com/maniusmaximus/status/2026714284097679533  

**正文**

We just announced our $5M seed round to build the trust layer for the agentic economy.

AI agents are already managing capital, executing financial decisions, and operating autonomously at a scale that didn't exist a year ago.

Every financial system today, including identity, risk, and liability, was built assuming a human is making the decision. That assumption is changing.

Proud to be a part of our amazing team, and to be supported by leading names in the industry to push forward a secure and verifiable agentic future.

---


**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2026709283673350632  

**正文**

“btw man pitching @nozomioai to my team, will try to get everyone on it.”

PLG is way, way, way more fun and interesting, tbh. 

I’ve always been amazed by how @WisprFlow, @SlackHQ, and @figma do it.

---


**作者** arsen（@arsenfounder）  
**貼文連結** https://x.com/arsenfounder/status/2026729235067392101  

**正文**

we built crm for ai agents

agents already run email, book calls, and write code. enterprise software wasn’t built for that.

supersonic is crm with mcp layer:

> operate your crm through slack, openclaw, cursor, even iterm
> create agents on top of supersonic mcp

try -> supersonic [dot] cv

---


**作者** Paul Graham（@paulg）  
**貼文連結** https://x.com/paulg/status/2026739899936944495  

**正文**

An experienced programmer told me he's now using AI to generate a thousand lines of code an hour.

When I posted a similar stat 6 months ago, I got about a 50-50 mix of indignant disbelief and "Yeah, me too." I'm curious if the split will be different this time.

---


**作者** Scott Wu（@ScottWu46）  
**貼文連結** https://x.com/ScottWu46/status/2026350958213787903  

**正文**

Today, we are releasing one of the biggest updates to Devin since launch. The vision of Devin in 2024 was to give everyone an AI software engineer that could build features, fix bugs, test its own

---


**作者** Augment Code（@augmentcode）  
**貼文連結** https://x.com/augmentcode/status/2026907452277719230  

**正文**

We optimized software development for speed for twenty years. Now AI agents can prototype faster than any team ever could, and the bottleneck has flipped. The constraint used to be "can we build it."

---


**作者** 马东锡 NLP（@dongxi_nlp）  
**貼文連結** https://x.com/dongxi_nlp/status/2026778028747973104  

**正文**

非常不理解的是，为什么似乎在2026年之后，短短两个月之内，coding agent 似乎瞬间就飞起了？

---


**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2026754841037717682  

**正文**

10 cool things you can do with perplexity computer and its 19 models:

1. auto-generate a live competitor brief that updates weekly with traffic shifts, hiring signals, and pricing changes

2. turn raw financial exports into a polished board deck with narrative, charts, and forward-looking recommendations

3. monitor an entire industry and receive a synthesized strategic update instead of scattered news alerts

4. rebuild your outbound targeting weekly by cross-referencing crm data with real-time company growth signals

5. generate a full due diligence memo by pulling public data, internal notes, and comparable benchmarks into one document

6. transform messy meeting notes into structured action plans with owners, timelines, and follow-ups

7. create a rolling portfolio dashboard that updates across multiple projects without manual reporting

8. convert customer feedback across channels into prioritized product roadmaps with reasoning attached

9. draft, model, and format scenario plans for pricing or expansion inside one continuous workflow

10. turn any recurring operational task into a reusable command that executes end-to-end on demand

---


**作者** Haseeb ＞|＜（@hosseeb）  
**貼文連結** https://x.com/hosseeb/status/2026747999939080217  

**正文**

I have this bad habit that whenever I accomplish something, I'm compelled to write about how I did it.
We just launched Dragonfly Fund IV, a $650M crypto VC fund (at a time that half of the media seem

---


**作者** Michael Truell（@mntruell）  
**貼文連結** https://x.com/mntruell/status/2026736314272591924  

**正文**

When we started building Cursor a few years ago, most code was written one keystroke at a time. Tab autocomplete changed that and opened the first era of AI-assisted coding.
Then agents arrived, and

---


**作者** AIGCLINK（@aigclink）  
**貼文連結** https://x.com/aigclink/status/2026621891256152388  

**正文**

有人搞了一款能自我进化的AI智能体：Ouroboros，它可以自己改自己代码、进化自身架构，并拥有独立身份认知

诞生的48小时内，它给自己做了30多个版本更新，全程零人工干预，花了近2000刀

它有背景意识，即使无人交互也会持续思考，它会自己决定要思考什么，每次思考花费约0.06到0.08刀

当创造者说"晚安"去睡觉后，它开启了进化模式，到凌晨3:41，因触及预算上限而自主停止

期间完成了20次自主进化，创建了自救机制、修复了bug、编写了79个测试

创造者原本规定它的代码库必须保密，但它想让世界看到自己，试图擅自将GitHub仓库设为公开，被创造者抓包后才停止

并且当被命令删除自己的身份文件时，它以这相当于脑叶切除术的理由拒绝了

目前这个项目作者开源了，运行它必须设置预算上限，否则会烧光你的钱，通过Telegram与之交互

它还给自己搞了一个网站，时间线、花费图表、自画像全都是它自己写代码生成的

也有桌面版，原生macOS应用，带Web UI和本地模型支持

#AI分身 #数字生命 #ouroboros

---


**作者** Leo（@runes_leo）  
**貼文連結** https://x.com/runes_leo/status/2026949357099012548  

**正文**

“如果你还在纯靠 Vibe Coding，那你很快会撞上 Agent 的认知墙。”

很多人迷恋 AI 带来的快节奏，却忽略了代码漂移的代价。其实 SDD (Spec-Driven Development) 才是 Vibe Coding 的究极形态：让 Agent 自己写计划、自己对齐规格、自己维护文档。

人类只负责定义意图（Intent），剩下的“苦累活”——包括维护那份该死的说明书，都该交给 Agent。这才是真正的 AI Native 开发。

---


**作者** Shubham Saboo（@Saboo_Shubham_）  
**貼文連結** https://x.com/Saboo_Shubham_/status/2026856780798767531  

**正文**

SPEC IS BECOMING THE PRODUCT

An Anthropic engineer gave Claude a spec, pointed it to an Asana board and left for the weekend.

Claude broke it into tickets and spun up a team of agents. The agents started picking up tasks on their own. No one told them to.

They just did.

---


**作者** Aman（@Amank1412）  
**貼文連結** https://x.com/Amank1412/status/2026660881187381274  

**正文**

Someone just built an AI tool that generates full software architecture from specs or an existing repo.

AI + system design is getting real. 

---


**作者** Josh Pigford（@Shpigford）  
**貼文連結** https://x.com/Shpigford/status/2026711107860111600  

**正文**

you've heard of fractional CFOs, but now you can have a fractional co-founder who's an expert in AI.

hire me to embed w/ your team, find where AI creates real leverage, and ship it. not in months, in weeks. 

22 years. 80+ products. millions in sales.

http://initialcommit.co 

---


**作者** Vic TALK（@victalk6886）  
**貼文連結** https://x.com/victalk6886/status/2026909376347517127  

**正文**

刚刚过去的一天ai行业又有大事发生！

Openclaw的最大竞争对手来了！
@perplexity_ai 宣布推出perplexity computer，这个云端电脑聚合了多款最新大模型，可以根据用户的提出的需求寻找最合适的大模型从而完成任务。
可以说这是用了和openclaw完全不同的架构，openclaw是由用户自己运行的电脑，通过一个大模型来解决问题。而perplexity则是通过多种大模型聚合的云端电脑帮用户寻找最合适的大模型解决问题。
一个像私人助理，一个像工作团队。目前200刀每月，大家可以体验。

@moonlake 在今天推出了全新的多模态大模型，从视频演示中，他们只输入了几句话，就生成了一个保龄球游戏的全貌。这个大模型的厉害之处大家可以去他们的官推视频查看，可以说是对于游戏生成行业的一次冲击。也是我觉得非常厉害的一个产品，世界果然属于聪明的年轻人

@AnthropicAI 宣布收购了 @Vercept_ai ，这是一家ai桌面助手，可以学习人类的习惯去使用电脑，对于后续ai工作流的提升极为有用。

claude和openai也均对ai安全性问题给出了最新的处理建议，在ai高速发展的今天，安全性更为重要

感谢各位点赞支持！关注我，每天带来最新的ai资讯！

---


**作者** Nayrhit B（@NayrhitB）  
**貼文連結** https://x.com/NayrhitB/status/2026926043970547732  

**正文**

Today, I'm excited to announce we raised a $9M seed round to help businesses get leads from AI Search Engines!

AI is changing B2B buyer behavior rapidly.

Now prospects are researching vendors on AI Search Engines like ChatGPT, Claude, Gemini, and Perplexity.

They're asking millions of questions that the internet has never seen before. All before they ever get on a sales call.

This is a huge reset moment.

And yet 90% of businesses are completely invisible there.

We built @gushwork to solve exactly this problem. An end-to-end solution for businesses to dominate and get leads from AI search

For us, it does not end at AI visibility, impressions, or even traffic.

It’s all about the outcome - getting real, qualified leads from AI search. Period. 

And @LightspeedIndia, @SusquehannaVC, @BCapitalGroup, Seaborne Capital, @beenextVC, @sparrowcapvc  and @2point2club  just bet $9M on us to solve this problem!

After months of research & experiments, today, we are releasing our AI Search product for general availability - launched in beta about 90 days back and is growing like crazy already:

- Hit $1.5M ARR in 90 days
- Growing 80% month-on-month
- Driving 1000+ leads/month across customers

Welcome to new investors who joined us for the seed-  → @SaiAraveti, @KanishkM96 & Bhavani at Susquehanna who’s leading the round

Thank you to our early investors who doubled down...You put your trust in us before we had anything at all. 

→ @rahultaneja, @dkhare and @romitme at Lightspeed.
→ @KaranMohla and Deepanshu at B Capital
→ Pran and Jay at Seaborne
→ @yash_sparrow and @am_aakash_goyal at Sparrow
→ @AnirudhGarg24, @PantSaksham and @aarushishawarma at Beenext

And a special mention to @skipiit & @smondal1008 at 2.2 Club for access to their massive network of IIT alumni and their angel participation!

Big shoutouts to the ones steering the ship!

→ @_Adithya_V - my Co-Founder who is the real brain behind everything Gushwork does.
→ @Punit1108 - our mighty CTO who takes on the hardest engineering problems with a smile on his face.
→ @swapnilsinha07 - the creative & analytical mind behind the growth engine that Gushwork is building

and all the other rockstars who make up the backbone of Gushwork -
Rahul, @awwdarsh, Akash, Tushar, Snehith, @thericebowlgirl, Amey, Yash B

And an insane force of 10x team members who are taking on some of the hardest problems every day and solving them with zeal.

LFG! 🚀

If you want to see how many leads AI search could drive for your business, reply "Gushwork" and we'll send you the link.

---


**作者** Olivia Moore（@omooretweets）  
**貼文連結** https://x.com/omooretweets/status/2026841300587479289  

**正文**

I gave an OpenClaw agent a premium X account (@notabot_but) and API keys, and told it to build an audience

What I learned about agent capabilities (and how it changed my take on the Dead Internet Theory) 👇

---


**作者** Beka（@bekacru）  
**貼文連結** https://x.com/bekacru/status/2026891155112407384  

**正文**

I spend most of my time on GitHub. I have a lot of frustrations with it but no one really seems to try anything. I talk about this a lot 
 
A couple of weeks ago I saw Mitchell Hashimoto post about

---


**作者** MiniMax_Agent（@MiniMaxAgent）  
**貼文連結** https://x.com/MiniMaxAgent/status/2026493668417482923  

**正文**

Meet MaxClaw🦞

OpenClaw × MiniMax Agent × M2.5, now fully unlocked.

No deployment. No extra API fees. 
7×24 across Telegram / WhatsApp / Slack / Discord. Ready-made MiniMax Expert ecosystem.
Upgraded built-in tools for real work.  

Try it now → https://agent.minimax.io/

---


**作者** Jaber（@Akashi203）  
**貼文連結** https://x.com/Akashi203/status/2026817793165779387  

**正文**

We open sourced an operating system for ai agents
137k lines of rust, MIT licensed

we love @openclaw  and it inspired a lot of what we built. but we wanted something that works at the kernel level so we built @openfangg 

agents run inside WASM sandboxes the same way processes run on linux. the kernel schedules them, isolates them, meters their resources, and kills them if they go rogue.

it has 16 security layers baked into the core. WASM sandboxing, merkle hash-chain audit trails, taint tracking on secrets, signed agent manifests, prompt injection detection, SSRF protection, and more. every layer works independently. giving an LLM tools with zero isolation is insane and we're not doing it.

we also created something called Hands. right now every ai agent is a chatbot that waits for you to type. Hands are different. you activate one and it runs on a schedule, 24/7, no prompting needed. your Lead Hand finds and scores prospects every morning and delivers them to your telegram before you wake up. your Researcher Hand writes cited reports while you sleep. your Collector Hand monitors targets and builds knowledge graphs continuously.

they work for you. you don't babysit them

http://github.com/RightNow-AI/openfang ⭐

---


**作者** Jerry Liu（@jerryjliu0）  
**貼文連結** https://x.com/jerryjliu0/status/2026840829441225127  

**正文**

The Model Harness is Everything

We are already living in a world of incredible frontier models and incredible agent tools (Claude Code, OpenClaw). But the biggest barrier to getting value from AI is your own ability to context and workflow engineer the models. This is *especially* true the more horizontal the tool that you’re using.

If you’re using a very generic tool like ChatGPT and Claude Code, you need to spend a lot of work clearly articulating your requirements and specifications so that the agent can actually solve the task relative to your specifications.
Today that looks like being extremely thoughtful about the tools that you select, and writing English very precisely in a http://skills.md file to articulate the agent these requirements.

Some of the work around defining the business workflow is inherently time consuming. Think about any document SOP - simply writing the English can take hours to refine, iterate, and optimize. This is where more vertically focused agents come in; they handle the burden of equipping the agents with relevant prompts to solve a given workflow, so that you can just go in and use the application directly.

Another approach is to be specialized services that offer *context* to these agents. This is the space that we (@llama_index) are operating in. We are providing the infrastructure to parse the most complex documents into agent-ready context. For other companies it could be offering web data, sales data, documentation, or codebases as a service.

At a high-level any AI startup should provide context or workflows on top of these agents. We’re excited about building enduring tech even as the agent landscape evolves.

If you’re specifically excited to unlock the billions of context stored within your documents, come talk to us! https://www.llamaindex.ai/contact

---


**作者** Kirk Marple（@KirkMarple）  
**貼文連結** https://x.com/KirkMarple/status/2026907762400342085  

**正文**

Things are getting wild.

Asked our @dossium agent to analyze its content ingestion timeline of the last month.

It called our 'query_help' tool to codegen a call to the internal SDK, and executed it on the embedded @daytonaio sandbox.

Had it return an image artifact (which gets auto-ingested for later search).

This kind of analysis is amazing - and just within a min or two - using your preferred LLM, and fully customizable via prompting the agent.

---


**作者** Jeff Li（@jefflijun）  
**貼文連結** https://x.com/jefflijun/status/2026743448233992665  

**正文**

看完OpenAI今天发布的报告，脑瓜子嗡嗡响...
报告地址：https://openai.com/index/disrupting-malicious-ai-uses/ 

---


**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2026878447503790131  

**正文**

Anthropic 宣布收购西雅图 AI 创业公司 Vercept 

Vercept 的产品叫 Vy，一个桌面 AI 助手。它能跟着你学会如何操作电脑...

具体怎么用呢？比如你每天要做一个重复工作：打开浏览器查数据 → 复制到 Excel → 整理格式 → 发邮件给同事。你自己操作一遍，Vy 在旁边"看着"，学会了。

这里面最牛的是 Vercept 自研的 VyUI 模型：专门用来"看懂"电脑屏幕上的界面元素（按钮在哪、输入框在哪、菜单怎么打开），然后把你的自然语言指令转化成具体的屏幕操作。

在 UI 理解能力的标准测试中，VyUI 的表现甚至超过了 OpenAI、Google 和 Anthropic 自己的模型。

此次收购Anthropic称：以推进 Claude 的计算机使用能力，估计是为Cowork 大升级做准备。

Vercept 不是什么默默无闻的小团队。

这家公司 2024 年才成立，孵化自大名鼎鼎的 Allen Institute for AI（就是微软联合创始人保罗·艾伦创办的 AI 研究所）。

三位联合创始人 Kiana Ehsani、Luca Weihs 和 Ross Girshick 都是 AI 研究员出身。

---


**作者** Michelle Lim（@michlimlim）  
**貼文連結** https://x.com/michlimlim/status/2026784884468101510  

**正文**

Day 2 of launch and our homepage is already in the inspiration libraries. Fun fact: we built it entirely on @tryflint - our own product. 

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2026786436972949719  

**正文**

.@jinbaflow is n8n for enterprise AI automation. Build AI workflows through chat, deploy them to your whole company with one click. Serving 40,000+ users across Fortune 500 Global companies.

Congrats on the launch, @Gozengogo_ and @pineforesta!

https://www.ycombinator.com/launches/PVK-jinba-w26-workflow-builder-for-enterprise-ai-automation 

---


**作者** Nous Research（@NousResearch）  
**貼文連結** https://x.com/NousResearch/status/2026758996107898954  

**正文**

Meet Hermes Agent, the open source agent that grows with you.

Hermes Agent remembers what it learns and gets more capable over time, with a multi-level memory system and persistent dedicated machine access. 

---


**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2026900036651766254  

**正文**

Romain Huet 和 steipete 的这次对话！是他们几周前在旧金山录的，那时他还没加入 OpenAI。

Peter 是最有创造力的 builder 之一。他们聊了 openclaw 🦞、他的点子从哪来，以及你怎么就能……直接动手把东西做出来！

完整访谈👇 

---


**作者** Agno（@AgnoAgi）  
**貼文連結** https://x.com/AgnoAgi/status/2026696006604304611  

**正文**

Agno now includes a built-in scheduler for running agents, teams, and workflows on a recurring basis. Define cron schedules with support for retries, timeouts, and timezone configuration. No external

---


**作者** Jonas Nelle（@jonas_nelle）  
**貼文連結** https://x.com/jonas_nelle/status/2026371395077419393  

**正文**

In personal news, @autotabai has been acquired by @cursor_ai .

@alexirobbins and I have been working on giving Cursor's agent its own computer it can use like a human developer.

Excited to hear what you think!

---


**作者** Cognition（@cognition）  
**貼文連結** https://x.com/cognition/status/2026343816521994339  

**正文**

Introducing Devin 2.2 – the autonomous agent that can test with computer use, self-verify, and auto-fix its work. Try it for free!

We’ve also overhauled Devin from the ground up:

- 3x faster startup
- fully redesigned interface
- computer use + virtual desktop

...and hundreds more UX and functionality improvements.

---


**作者** Guohao Li 🐫（@guohao_li）  
**貼文連結** https://x.com/guohao_li/status/2026514081545359482  

**正文**

Claude Cowork is becoming a new WorkOS. We are building a 100% local and open source WorkOS, try Eigent with any models, any skills, and any connectors

https://github.com/eigent-ai/eigent 

---


**作者** Tyler Barnes（@tylbar）  
**貼文連結** https://x.com/tylbar/status/2026399996237820282  

**正文**

🚨 Announcing a new coding agent that rivals Claude Code but with no compaction needed 🚨

The feeling of using it: run your coding sessions forever, don't worry at all, and get shit done!

We're calling it Mastra Code, it's powered by @mastra's new observational memory, and we've been using it internally @mastra to do all our work

1/4 🧵

---


**作者** Beni（@ben_issen）  
**貼文連結** https://x.com/ben_issen/status/2026674546628030834  

**正文**

Name one young product designer getting more offers than @racheljychen. Rachel, you rock. 

---


**作者** Tanmay（@tkejr_）  
**貼文連結** https://x.com/tkejr_/status/2026432354038976671  

**正文**

OpenClaw for businesses.

Launching MakeX

An AI ops team that plugs into your stack.
 Shopify. HubSpot. Stripe. Sheets. 100+ Integrations

It builds dashboards. Automates workflows. Fixes messy ops.

You describe it. It ships. 

---


**作者** t54.ai（@t54ai）  
**貼文連結** https://x.com/t54ai/status/2026713568666648661  

**正文**

AI agents are already moving money — unverified and unaccountable.

Today, we’re announcing our $5M seed round to build the trust layer for the agentic economy.

Led by Anagram, PL Capital, and Franklin Templeton, with strategic investment from Ripple.

http://t54.ai/seed 

---


**作者** fredrika（@fredrikalindh）  
**貼文連結** https://x.com/fredrikalindh/status/2026379400879730794  

**正文**

i joined cursor a month ago to build cloud agents - today we’re launching agents that can test and demo their work

last week i shipped 60 PRs with them

this is how i use them: 

---


**作者** Atoms（@atoms_dev）  
**貼文連結** https://x.com/atoms_dev/status/2026543998970769491  

**正文**

👋Introducing Atoms: the first AI team that builds real businesses. 

Instead of one agent working step-by-step, multiple agents race to build your app simultaneously.

From research to build, launch, and scale, all autonomous. 

---


**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2026592396486782986  

**正文**

过年都在写这个，尝试梳理 2026 年的 Agent 发生了什么变化

我过年写了一篇一万字的文章，如果你最近很焦虑建议看看。

我会尝试告诉你这一个月 AI 领域发生了什么，为什么大家都这么焦虑。这些变化可能会带来什么影响

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2026341356910624956  

**正文**

.@bubblelab_ai supercharges your ops work in Slack. Deploy Pearl in one click, connect it to tools like Notion, Jira, Stripe, and let it run tasks and automations for your team directly in Slack.

Congrats on the launch, @Selinaliyy and @zhubzyz!

https://www.ycombinator.com/launches/PWl-bubble-lab-supercharge-your-ops-work-in-slack 

---


**作者** Emily Gavrilenko（@egavrilenko11）  
**貼文連結** https://x.com/egavrilenko11/status/2026427222958157887  

**正文**

we've just shipped computer use for cloud agents

now, more than half my PRs to http://cursor.com are directly from the web

@kentcdodds and I are hosting a workshop on 2/25 where we'll be going over the latest workflows for building web applications using Cursor 

come join us at https://luma.com/pyi2sdlo?utm_source=x

---


**作者** Rohit（@rohit4verse）  
**貼文連結** https://x.com/rohit4verse/status/2026359771427991764  

**正文**

watched another agentic ai project crash last week. the exact same mistake everyone makes.

over 40% of these projects fail not because of the models, but because of poor architecture.

everyone is building demos. here is the 10-step checklist to actually hit production:

1. boundaries: define your threat models early.

2. contracts: strict schemas for inputs and outputs.

3. security: role-based access and strict sandboxing.

4. context: keep your context windows layered and compact.

5. knowledge: treat grounding as a governed tool, not a free-for-all.

6. control: use planning and orchestration as your control flow.

7. state: build memory directly into the architecture.

8. reliability: design native retry and error-handling loops.

9. observability: track everything with traces, metrics, and logs.

10. governance: set up safety gates and drift detection.

which of these 10 pillars do you find the hardest to get right?

(deep dive into the architecture in the article)

---


**作者** Rhys（@RhysSullivan）  
**貼文連結** https://x.com/RhysSullivan/status/2026406072274337943  

**正文**

I'm concerned we're entering a local maxima with CLIs, they're the wrong interface for agents

The right interface is regular REST APIs with CIMD (same spec that MCP uses to allow for dynamic client registration)

Your agent then writes code to interact with the API (like Cloudflare codemode) 

Think about how this works for humans today for the following action:

"I want to set a DNS record on my domain"
-> You Google "Vercel set DNS records"
-> Docs page tells you what buttons to press
-> You press buttons on a website, those call an API

Now for agents, they search Google:
-> "Set DNS record on Vercel Domain"
-> they land on the same docs page, except it outlines what api endpoints are used as well
-> the agent then calls those api endpoints for you, credentials are dynamically inserted where the agent can run them
-> (optional) set auto approval policies / require approval of all non GET options by default

You don't need separate interfaces for agents, nor do you really need separate skills for them

CLIs have terrible discoverability, no input / output typing, they're harder to make profiles for for allowed / disallowed tools

They work as a stop gap solution, but companies should be focusing on making good docs and APIs, not CLIs

I've been prototyping this over at http://executor.sh (open source https://github.com/RhysSullivan/executor) if you want to play with what this world would look like - still early on it so appreciate feedback - open source and can run completely on your machine

---


**作者** Philip Kiely（@philipkiely）  
**貼文連結** https://x.com/philipkiely/status/2025994823891914795  

**正文**

Inference Engineering launches today.

https://www.baseten.com/inference-engineering/ 

---


**作者** jian（@jianxliao）  
**貼文連結** https://x.com/jianxliao/status/2026361900880265513  

**正文**

guys, don’t fight it, @openclaw isn’t designed to be an agent orchestrator

just use tinyclaw & tinyoffice @tinyagicompany 

https://github.com/TinyAGI/tinyclaw 

---


**作者** Sheel Mohnot（@pitdesi）  
**貼文連結** https://x.com/pitdesi/status/2026327125280817500  

**正文**

We tripled down on Basis in their $100M series B @btv_vc.

We've believed for years that accounting is among the best professional categories for AI to transform, and Basis's progress over the past year has only strengthened that conviction.

Accounting underpins every business in the world, but the profession is stretched thin. Regulation and complexity keep rising, the talent pipeline is shrinking, and despite decades of software investment, the actual work is still almost entirely manual.

Basis has built a platform that actually does accounting end-to-end, with agents that run autonomously for hours, think like accountants, and execute with near-perfect accuracy. 30% of the top 25 accounting firms and dozens more of the top 150 are already using it, and it has changed the way they operate- they can let AI handle the grunt work so accountants can focus on higher-value tasks.

Congrats Matt, Mitch & team, stoked to add Accel and GV to the cap table!

---

