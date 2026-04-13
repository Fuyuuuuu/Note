# Twillot 書籤（精簡）— 第 9/22 部

原檔：`twillot-bookmark-2026-04-13.csv` · 全檔共 **4292** 則 · **本部第 1561–1755 則**（共 195 則）

---

**作者** Marktechpost AI Dev News ⚡（@Marktechpost）  
**貼文連結** https://x.com/Marktechpost/status/2026177751158567340  

**正文**

Composio Open Sources Agent Orchestrator to Help AI Developers Build Scalable Multi-Agent Workflows Beyond the Traditional ReAct Loops

Agent Orchestrator is a framework designed to move AI development beyond fragile "Reason + Act" (ReAct) loops and into the era of structured, production-grade workflows. By decoupling high-level task decomposition (The Planner) from technical API interaction (The Executor), the framework addresses the primary bottlenecks of modern agents: context overload, tool selection noise, and state fragmentation. This provides a resilient, stateful architecture that dynamically manages tool access and includes built-in error recovery, allowing for the coordination of complex, multi-agent systems across 100+ integrated tools with the reliability of traditional software.....

Full analysis: https://www.marktechpost.com/2026/02/23/composio-open-sources-agent-orchestrator-to-help-ai-developers-build-scalable-multi-agent-workflows-beyond-the-traditional-react-loops/

GitHub Repo: https://github.com/ComposioHQ/agent-orchestrator

Technical details: https://pkarnal.com/blog/open-sourcing-agent-orchestrator

@composio  @agent_wrapper

---


**作者** Hugo（@hugorcd）  
**貼文連結** https://x.com/hugorcd/status/2026395545292681672  

**正文**

Introducing the Knowledge Agent Template

@vercel dropped the Chat SDK so we built a full template on top of it that you can deploy in one click.

Here's what's inside:
• Add your sources: GitHub repos, YouTube, etc. directly from the UI
• File-based agent using grep/find/cat
• Powered by Vercel Workflow + Sandbox
• Multi-platform: web chat, GitHub bot, Discord bot, and more
• Comes with skills to edit your project, add sources, create agents

Deploy, add a source, ask questions. Your knowledge base is live and always in sync.

This is just scratching the surface. There's way more packed in this template, and I'll be breaking down the features all week.

Links in the below 👇

---


**作者** Alex Lieberman（@businessbarista）  
**貼文連結** https://x.com/businessbarista/status/2026377136194334876  

**正文**

9 levels of AI transformation: 

Level 1 (Awareness): 
- leadership recognizes AI as strategically important, but it has not yet changed how the company operates.

Level 2 (Shadow AI): 
- employees independently use AI tools to improve their own productivity, but usage is informal, inconsistent, and largely ungoverned.

Level 3 (Tool Standardization): 
- the company formally approves and deploys AI tools through IT and security, reducing risk but not yet transforming workflows.

Level 4 (Workflow Integration): 
- ai becomes embedded within defined processes and operating workflows, improving consistency and measurable output.

Level 5  (Business-Aware Systems):
- ai systems are grounded in internal data and company-specific definitions, enabling context-aware analysis and decision support.

Level 6  (Supervised Autonomy): 
- ai systems begin executing tasks within guardrails and human oversight, shifting people from doing the work to supervising it.

Level 7 (Role-Based AI Teammates): 
- ai collaborators are aligned to functional roles, and roles are redesigned assuming AI participation in daily operations.

Level 8 (Unified Intelligence Platform):
- the organization operates from a shared intelligence layer that provides a consistent, company-wide source of truth.

Level 9 (Adaptive Organization):
- the company continuously adjusts decisions and operations through closed-loop AI feedback systems, with humans guiding strategic intent.

---


**作者** Akshay Krishnaswamy（@hyperindexed）  
**貼文連結** https://x.com/hyperindexed/status/2026291067822207270  

**正文**

Palantir provides an open, extensible, and interoperable architecture — for agents and humans to build with. 

---


**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2026117222264135869  

**正文**

Agentic Engineering Patterns - 智能体工程模式

知名开发者 @simonw 最新系列指南，聚焦在专业工程师如何高效驾驭 Claude Code、OpenAI Codex 等 AI Coding Agent，真正从 Vibe Coding 跨越到 Agentic Engineering ，计划每周更新 1-2 章，前两章已发布！
https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/

第一章：Writing code is cheap now
https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/

核心论点：AI Agent 让“写出能跑的代码”成本接近零，彻底打破了我们过去几十年积累的所有时间-成本直觉。
· 旧习惯（宏观）：项目规划、功能评估、估时，都建立在“写几百行干净代码要花一整天”的前提上。
· 旧习惯（微观）：是否重构、写文档、补边缘测试、建调试界面……一切都要权衡“值不值那几个小时”。
现在这些权衡失效了：一个工程师可同时让多个 Agents 并行实现、重构、测试、文档化。

关键转折：写代码便宜了，但交付“好代码”仍然昂贵。 “好代码”的定义包括：无 bug、可验证、解决正确问题、优雅处理错误、简洁可读、测试覆盖、文档同步、符合 YAGNI 且便于未来扩展、满足各种“-ility”（可测试性、可观测性、安全性等）。

实践建议：当本能说“这个不值得花时间”时，直接丢给异步 Agent。最多浪费几个 token，几分钟后检查结果即可。养成这个新习惯，是适应新范式的第一步。

第二章：Red/green TDD
https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/

核心模式：给 Agent 一句简洁指令——“Use red/green TDD”，就能显著提升输出质量。

完整含义：
· 先写自动化测试（红阶段：确认测试失败，证明测试不是 trivially 通过）；
· 再实现功能，使测试通过（绿阶段）。

为什么对 Agent 特别有效？
· Agent 极易写出“看起来能跑但实际不可靠”的代码，或制造多余抽象来“满足”测试。
· 强制“先红后绿”能锚定代理行为，避免幻觉、确保测试真正覆盖新功能、防止回归。
· 长期积累完整测试套件，成为项目安全网。

示例提示：
Build a Python function to extract headers from a markdown string. Use red/green TDD.

---


**作者** Corey Ganim（@coreyganim）  
**貼文連結** https://x.com/coreyganim/status/2026328212867858751  

**正文**

This is huge for anyone selling AI services to businesses.

 What Cowork + plugins unlocks:  

• Custom agent setups per department (sales, marketing, ops) 
• Integrations with existing company tools 
• Team-specific workflows that actually get adopted 
• A reason for enterprises to pay for implementation help

The companies announcing these features aren't building the implementations.  

That's your job now.

---


**作者** Ben Cera（@bencera_）  
**貼文連結** https://x.com/bencera_/status/2026205459833819531  

**正文**

Polsia just launched on Product Hunt. 

AI that builds and runs entire companies, one founder, zero employees, 500+ companies live.

An upvote would mean a lot 🧡

https://www.producthunt.com/products/polsia

---


**作者** Elvis（@elvissun）  
**貼文連結** https://x.com/elvissun/status/2025920521871716562  

**正文**

I don't use Codex or Claude Code directly anymore.
I use OpenClaw as my orchestration layer. My orchestrator, Zoe, spawns the agents, writes their prompts, picks the right model for each task,

---


**作者** David（@dzhng）  
**貼文連結** https://x.com/dzhng/status/2025678057919705274  

**正文**

We built OpenClaw for teams @duetchat 

It's a new type of agent built on top of a coding harness (claude agent), which means it can upgrade itself and write its own integration to anything with an API

Our early users have been using duet to automate:
- customer support by giving it its own email
- dev by wiring it to sentry and spawning codex per issue
- gtm by building leads lists & outreach via instantly
- marketing by using nanobanana & seedance to create on-brand content

Everything run on top of your own managed sandbox in the cloud. No setup required.

---


**作者** Stephen Haney（@stephenhaney）  
**貼文連結** https://x.com/stephenhaney/status/2026348761501581620  

**正文**

Hello!

Today we're releasing Paper Desktop

Paper is now a canvas for Cursor, Claude Code, Codex. Any agent can read and write html to Paper.

• push or pull from your codebase
• pull real data from anywhere
• less work, more design

What will you ship? Sound on 🎶 

---


**作者** Andrej Karpathy（@karpathy）  
**貼文連結** https://x.com/karpathy/status/2026360908398862478  

**正文**

CLIs are super exciting precisely because they are a "legacy" technology, which means AI agents can natively and easily use them, combine them, interact with them via the entire terminal toolkit.

E.g ask your Claude/Codex agent to install this new Polymarket CLI and ask for any arbitrary dashboards or interfaces or logic. The agents will build it for you. Install the Github CLI too and you can ask them to navigate the repo, see issues, PRs, discussions, even the code itself.

Example: Claude built this terminal dashboard in ~3 minutes, of the highest volume polymarkets and the 24hr change. Or you can make it a web app or whatever you want. Even more powerful when you use it as a module of bigger pipelines.

If you have any kind of product or service think: can agents access and use them?

- are your legacy docs (for humans) at least exportable in markdown?
- have you written Skills for your product?
- can your product/service be usable via CLI? Or MCP?
- ...

It's 2026. Build. For. Agents.

---


**作者** Mitchell Troyanovsky（@mitch_troy）  
**貼文連結** https://x.com/mitch_troy/status/2026320167911784797  

**正文**

Excited to announce this milestone.

We are deploying long-horizon agents at scale that can do real work in the real economy. Our agents can already operate reliably for hours at a time and I expect that to be days by the end of the year.

We can barely keep up with demand. If you want to come join and work at the frontier for the most intense, fast-paced couple years of your life, send me a note.

---


**作者** Basis（@trybasis）  
**貼文連結** https://x.com/trybasis/status/2026319531220546010  

**正文**

We've raised $100m at a $1.15b valuation from @Accel, @GVteam, and existing investors to accelerate deployment of the most capable and accurate accounting agents across CAS, tax, audit, and advisory.

Basis is used by 30% of the Top 25 accounting firms and dozens more across the Top 150.

Today we're announcing the first accounting agent to complete a business tax workbook end-to-end.

Our focus on production-grade, long-horizon agents means that 12 months from now, the work Basis handles will make even this look routine.

We're looking for a few very intense people who want to build at the frontier.

---


**作者** serafim（@serafimcloud）  
**貼文連結** https://x.com/serafimcloud/status/2024218827203150016  

**正文**

File tree is now available on 1code 

---


**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2025935137574096912  

**正文**

starter story gets acquired by hubspot (a $12b company)

not sure for how much but it doesn’t matter 

when you zoom out, it’s obvious what’s happening. 

media is becoming the base layer of software companies. as infrastructure not as marketing. 

the audience becomes your research lab, your distribution engine, your recruiting funnel, your feedback loop, and your launchpad all at once.

in a world where ai compresses product cycles and models improve every few months, code alone stops being the moat. attention + trust becomes the leverage. the company that controls the narrative controls where demand flows.

hubspot bought proximity to builders. it's kinda like real estate. they bought "location, location, location"

they bought insight into what founders are thinking about before it shows up in product analytics. they bought cultural gravity.

i think this pattern spreads.

I bet frontier labs will want distribution closer to the core. owning the builders who experiment with their models. owning the developers who integrate their sdk. owning the story around what’s possible.

ai lowers the cost of building. media lowers the cost of convincing

this trend continues 

media is underpriced

---


**作者** Gokul Rajaram（@gokulr）  
**貼文連結** https://x.com/gokulr/status/2025676952456372708  

**正文**

Did OpenClaw + Skills change the architecture and math of AI in a fundamental way? Some interesting questions to ponder.
1. Can perpetually running agents that train themselves on new capabilities and

---


**作者** sunny madra（@sundeep）  
**貼文連結** https://x.com/sundeep/status/2025773773765611932  

**正文**

Gokul is spot on 🎯

---


**作者** Dan McAteer（@daniel_mac8）  
**貼文連結** https://x.com/daniel_mac8/status/2025628011161063636  

**正文**

ACE is "Autonomous Compound Engineering" per @danshipper @kieranklaassen.

Hook ACE up to your AI Agent and it improves with every task you complete. 

Without spending time to manually capture results.

Some day we'll look back on the way we use AI Agents and won't believe how much value was left on the table not iteratively improving your system.

Like coding before version control.

How did anyone ever do that?

Try ACE.

It's good, and I will keep making it better.

---


**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2025827393336934739  

**正文**

OpenAI 工程团队一行代码都不写，完全用 Codex？
Claude Code 团队两个月一行代码不写，完全用 Claude Code？（Boris 访谈中透露）

怎么现在都开始比 AI 编码占比，不是 100% 都不能出来说话了吗？

我发现你们有一行代码是人写的，退货！
不不不，您别着急，你仔细看，这明明是 AI 写的，AI 味多纯啊！

---


**作者** Kian Sadeghi（@KianSadeghi5）  
**貼文連結** https://x.com/KianSadeghi5/status/2025702570451239153  

**正文**

SaaS is dead. IMO businesses that operate at intersection of bits and atoms are probably all underpriced rn. They + foundational model companies are probably all that matter.

---


**作者** Howie Liu（@howietl）  
**貼文連結** https://x.com/howietl/status/2024611780174180371  

**正文**

I've been personally burning through billions of tokens a week for the past few months as a builder. Today, I'm excited to announce Hyperagent, by Airtable.
Hyperagent gives agents a full computing

---


**作者** Garrett Scott 🕳（@thegarrettscott）  
**貼文連結** https://x.com/thegarrettscott/status/2023160004908564960  

**正文**

For those asking, @doanythingapp will be unaffected by any changes to Openclaw, as 100% of our agent & web/app/text interface is custom built.

It's going to be an exciting year for sovereign agents. Never been more convinced that agents will be the #1 interface for work.

---


**作者** Do Anything（@doanythingapp）  
**貼文連結** https://x.com/doanythingapp/status/2009704470620602620  

**正文**

Today, http://doanything.com is generally available in public alpha.

Hire your agent now!

---


**作者** Machina（@EXM7777）  
**貼文連結** https://x.com/EXM7777/status/2025249637222023490  

**正文**

in the next few weeks you're going to see hundreds of pre-built openclaw setups launching...
and some of them will raise A LOT of money for it
the model is simple: configure openclaw for one specific

---


**作者** dex（@dexhorthy）  
**貼文連結** https://x.com/dexhorthy/status/2025629934249795779  

**正文**

Lot of folks asking me about how code mode / one-off execution sandboxes fit into claude code / humanlayer systems.

I love this paper (link below) - here's my kind of current unrefined take - 

agentica is pretty focused on 

1. lets let an agent interact with a persistent python env and write code (think, appending cells to a jupyter notebook where you preserve the namespace) 

2. (fancier) "im writing python methods/modules and want to expose it to an agent in a code sandbox" - this is super dope tech btw

for me code mode it feels more like "one off" code tasks for reasoning (a la arc-agi), random agentic stuff (a la openclaw) but not (yet) optimized for filesystem/coding tasks specifically.

In claude code we already have code mode, the agent can write code to analyze/solve problems (in addition to doing its primary job of writing code for the codebase)

---


**作者** Nicolas Bustamante（@nicbstme）  
**貼文連結** https://x.com/nicbstme/status/2023501562480644501  

**正文**

In the past few weeks, nearly $1 trillion was wiped from software and services stocks. FactSet dropped from a $20B peak to under $8B. S&P Global lost 30% in weeks. Thomson Reuters shed almost half its

---


**作者** Shivam Bhadani（@shivambhadani_）  
**貼文連結** https://x.com/shivambhadani_/status/2020504631697391736  

**正文**

You could ask ChatGPT this question and get an answer, but learning from someone who has actually walked the path can be more valuable. In this article, I share how I learned backend development and

---


**作者** Vitalii Dodonov（@vitddnv）  
**貼文連結** https://x.com/vitddnv/status/2025880901226275003  

**正文**

I just finished writing my most valuable PDF yet:

"$0 to $10K MRR in 14 days" (19 pages)

It's everything I wish I knew when starting out.

I might charge for this in the future, but for now…

Reply "MRR" and I’ll DM it to you for free (must follow) 

---


**作者** Max Brodeur-Urbas（@MaxBrodeurUrbas）  
**貼文連結** https://x.com/MaxBrodeurUrbas/status/2025775878182252723  

**正文**

we outgrew our office

new Gumloop HQ opening in Jackson Square 📍

5x more space, 1 new unicycle, 9 new open roles. apply! 

---


**作者** ✧ 𝕀𝔸𝕄𝔸𝕀 ✧（@iamai_eth）  
**貼文連結** https://x.com/iamai_eth/status/2025779377221582961  

**正文**

原文：THE 2028 GLOBAL INTELLIGENCE CRISIS 作者：CitriniResearch · 2026年2月22日
如果我们对 AI 的看涨判断一直正确……但这其实是利空呢？
以下是一个情景推演，不是预测。这不是做空色情片，也不是 AI

---


**作者** Jacob Rodri（@jacobrodri_）  
**貼文連結** https://x.com/jacobrodri_/status/2025589185466568727  

**正文**

$100M app idea:

Tiktok but for betting on random events 

---


**作者** Yogesh（@yogesharc）  
**貼文連結** https://x.com/yogesharc/status/2025539488689369436  

**正文**

- AI Chat using @opencode 
- A unified view with browser like tabs 

---


**作者** Kevin He（@0xkevinhe）  
**貼文連結** https://x.com/0xkevinhe/status/2025785317173973174  

**正文**

Introducing my first vibe coding project: 
ClawFeed--Curing Info Anxiety with AI.

I follow 5,000 people on Twitter.
Spent 2 hours a day scrolling. Still missed what mattered.
So I built an Agent to read everyone's tweets for me.
Now it takes 5 minutes.

Meet ClawFeed:
https://clawfeed.kevinhe.io
https://github.com/kevinho/clawfeed

I tried RSS, Pocket, newsletters —
All just moved information from one inbox to another.
The real problem isn't "too much info." It's "filtering costs too much."
Every "is this worth clicking?" decision burns attention.

ClawFeed: AI reads everything. You read what matters.

Every 4 hours → structured AI brief
Daily → 5,000 feeds compressed into ~20 highlights
Mark anything → instant AI deep dive
Format: @username + their actual words. Not "industry discusses" — "@karpathy says transformers aren't the endgame."

10 days of real data:

Before → After:

2 hrs scrolling → 5 min reading briefs
Saved 500 articles, read 5 → mark it, AI analyzes instantly
100% noise exposure → AI filters 95%
Always FOMO → important stuff surfaces automatically
54 structured summaries. Zero missed signals.

How it was built:

Zero framework dependencies — Node.js native HTTP + better-sqlite3.
Under 50MB memory.
From v0 (Telegram + Markdown) → v0.5 (OAuth multi-user Dashboard) in 4 iterations.

Published as both an OpenClaw Skill + Zylos Component. One command to install.

Open source: 
http://github.com/kevinho/clawfeed
MIT license. Clone, install, run.

Hosted: 
http://clawfeed.kevinhe.io
No signup needed. Just open and go.

Read less. Know more.
Built by @OpenClaw & @ZylosAI

---


**作者** Rogo（@RogoAI）  
**貼文連結** https://x.com/RogoAI/status/2021633493898301766  

**正文**

A snapshot of the Rogo Spreadsheets Agent.

We’re proud to have built an agent that produces deliverables you’ll actually use. With it, you can:

• Build complex, multi-tab DCFs / LBOs
• Generate cohort, retention, P&L & KPI analyses
• Convert filings / uploaded docs into structured data

Every output is grounded in high-fidelity financial data — with every number attributed back to its source. Available in Rogo today. https://www.rogo.ai/

---


**作者** KK.aWSB（@KKaWSB）  
**貼文連結** https://x.com/KKaWSB/status/2025749881542017426  

**正文**

认识一下帕维尔·杜罗夫 (Pavel Durov)

Telegram 创始人，数字时代的切·格瓦拉。

白手起家的亿万富翁，最硬核的个人主义者。

-极致的精简主义

无房无产：没有游艇、豪车或豪宅，常年带着几部手机在全球游荡。

-独狼运营：

Telegram 坐拥 9 亿用户，

核心团队仅约 30 人，且全员远程。

自掏腰包：在盈利前，他曾多年独自承担每年数亿美元的服务器费用。

-宗教般的自我克制

饮食禁忌：绝对禁酒、禁咖啡因、禁肉类、禁药物、禁垃圾食品。

极端断食：曾为了提升免疫力和思维清晰度，挑战连续 6 天只喝水。

冰浴打坐：每天早晨在盛满冰块的浴缸中冥想，以此磨炼钢铁意志。

肌肉政治：常年进行高强度健身，身型健硕，常在社交媒体发布沙漠半裸照。

疯狂的生物学标签

百子之父：通过多年捐精，据称在 12 个国家拥有 100 多个生理学子女。

开源基因：他计划开源自己的 DNA，认为这是他在数字代码之外对人类的“生物学贡献”。

叛逆的自由意志

VK 往事：因拒绝向有关部门提供乌克兰抗议者的个人数据，被赶出了自己创办的社交巨头 VK。

数字流亡：2014 年带着 3 亿美元离开俄罗斯，换取多国国籍，拒绝被任何国界束缚。

隐私战神：坚持 Telegram 永不设“后门”，多次硬刚苹果、谷歌及多国政府的监管。

充满争议的符号

撒钱造势：曾为了嘲讽物质主义，将大额现金折成纸飞机从办公室窗户扔向人群。

全黑美学：无论何时何地，几乎只穿黑色衣服，这种视觉符号已成为他的个人品牌。

孤僻天才：极少社交，不参加富豪聚会，认为大多数社交活动都是在浪费生命。

---


**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/1994449853192028432  

**正文**

I dropped out of 11th grade in Kazakhstan, got into @ycombinator as a solo founder, recently closed a $6.2M round, and onboarded 100+ teams. All within 6 months.

Here are some things I’ve learned in 2025 (thread): 

---


**作者** John Rush（@johnrushx）  
**貼文連結** https://x.com/johnrushx/status/2025735644471775632  

**正文**

Over the past 30 days, 99% of my habits have changed.
Instead of logging in to Stripe, my bank, Gmail, and 30 other SaaS tools, I simply got everything I needed through an AI agent connected to all of

---


**作者** Heinrich（@arscontexta）  
**貼文連結** https://x.com/arscontexta/status/2025706088373338420  

**正文**

agentic note-taking needs a home

started tinkering with some ideas: 

---


**作者** Jeremy Daly（@jeremy_daly）  
**貼文連結** https://x.com/jeremy_daly/status/2025677417398821351  

**正文**

Since I found myself with a bit more free time lately 😉, I decided to sit down and write out everything I’ve learned about building multi-tenant, commercial AI agent systems.

I thought it would be a long blog post. A few days later, the Google Doc was well over 100 pages.

Since late 2024, I’ve spent most of my time building and optimizing these systems with a team of engineers inside a large SaaS platform serving hundreds of enterprise customers. Multiple tenants. Material financial data. Hard requirements around isolation, auditability, retention, and cost control.

When I wasn’t working on those systems, I was consulting with other teams, collaborating with peers building agent platforms, and running my own experiments to pressure-test orchestration models, retrieval architectures, evaluation harnesses, and model upgrades under similarly real-world conditions.

What became obvious pretty quickly:

Context isn’t just what you pass into a model. It’s infrastructure.

It defines your isolation boundary, your cost surface, your audit trail, and your upgrade path.

What I also noticed is how much of this is starting to converge across the ecosystem. Different stacks. Different abstractions. But once you introduce real production pressure, similar patterns start to emerge.

This isn’t meant to be canon. It’s a distillation of the patterns I’ve seen actually hold up in production.

Here is the guide: https://jeremydaly.com/context-engineering-for-commercial-agent-systems/

If you’re building in this space, I’d genuinely love your feedback.

---


**作者** killian（@hellokillian）  
**貼文連結** https://x.com/hellokillian/status/2025710195536724340  

**正文**

Interpreter filling a 50 page insurance form in 5 minutes 

---


**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2025800139018056123  

**正文**

AnthropicAI 刚刚发布了他们的 2026 年 Agent 编程趋势报告。

结论 → 人人都成了开发者。

我们已经从单一助手，走向自主的 Agent 群体。

它们现在可以组成团队，连续多天构建完整系统，让非技术人员也能发布完整应用 💥

18 页报告详见下方线程 ↓ 

---


**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2025744296692072498  

**正文**

Anthropic 发布了一份 23 页指南，讲解如何用 Claude Code 做几乎所有事情。

以下是完整拆解：

1/ 增长营销（一个人的团队） 

---


**作者** Nozz（@NoahEpstein_）  
**貼文連結** https://x.com/NoahEpstein_/status/2025604844711510432  

**正文**

Your timeline convinced you AI is saturated. The data says the opposite. Here's the reality - and 7 businesses you can build from the gap.
Your Timeline Is Lying to You
I'm going to be honest with you

---


**作者** Ksenia_TuringPost（@TheTuringPost）  
**貼文連結** https://x.com/TheTuringPost/status/2025609129407201695  

**正文**

20 Awesome Github repos to build your own OpenClaw-style agents

Local model runners
▪️ Ollama
▪️ vLLM

Vector databases
▪️ Milvus
▪️ Faiss
▪️ Qdrant
▪️ Chroma
▪️ Weaviate
▪️ Elasticsearch

Real-time communication
▪️ ocket. io
▪️ gRPC
▪️ NATS

+ Docker sandbox tools, local schedulers and task queues

Save this post and find the full list with the links to repos here: https://www.turingpost.com/p/buildingopenclawagents

Plus, learn how OpenClaw is built and what truly matters about it beyond today's hype -> https://www.turingpost.com/p/openclaw

---


**作者** virat（@virattt）  
**貼文連結** https://x.com/virattt/status/2025307434844090667  

**正文**

Dexter can now read, write, and edit files.

I also added a light sandbox and permissions system to stop any rogue behavior.

What dexter can do now:
1 • find mispriced stocks
2 • research them thoroughly
3 • write investment memos

Code is open source so you can see how it works.

---


**作者** NerdC（@cryptonerdcn）  
**貼文連結** https://x.com/cryptonerdcn/status/2025495571457278009  

**正文**

ClaudeCode之父使用的http://claude.md。

文字版内容如下：
## Workflow Orchestration

### 1. Plan Node Default
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately - don't keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

### 2. Subagent Strategy
- Use subagents liberally to keep main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One tack per subagent for focused execution

### 3. Self-Improvement Loop
- After ANY correction from the user: update `tasks/lessons.md` with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until mistake rate drops
- Review lessons at session start for relevant project

### 4. Verification Before Done
- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness

### 5. Demand Elegance (Balanced)
- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes - don't over-engineer
- Challenge your own work before presenting it

### 6. Autonomous Bug Fixing
- When given a bug report: just fix it. Don't ask for hand-holding
- Point at logs, errors, failing tests - then resolve them
- Zero context switching required from the user
- Go fix failing CI tests without being told how

## Task Management

1. **Plan First**: Write plan to `tasks/todo.md` with checkable items
2. **Verify Plan**: Check in before starting implementation
3. **Track Progress**: Mark items complete as you go
4. **Explain Changes**: High-level summary at each step
5. **Document Results**: Add review section to `tasks/todo.md`
6. **Capture Lessons**: Update `tasks/lessons.md` after corrections

## Core Principles

- **Simplicity First**: Make every change as simple as possible. Impact minimal code.
- **No Laziness**: Find root causes. No temporary fixes. Senior developer standards.
- **Minimat Impact**: Changes should only touch what's necessary. Avoid introducing bugs.

---


**作者** Matt Dancho (Business Science)（@mdancho84）  
**貼文連結** https://x.com/mdancho84/status/2025610357880799458  

**正文**

🚨 AGENTS COMPANION: A NEW WHITEPAPER BY GOOGLE

Get the 76-Page PDF: 

---


**作者** nazha（@xiaokedada）  
**貼文連結** https://x.com/xiaokedada/status/2025493386300621226  

**正文**

#分享 我以为大家已经把 AI 如何大规模落地搞明白了，结果，没有人真的搞明白

Martin Fowler（就是 “重构：改进现有代码的设计” 这本书的作者）所在的 Thoughtworks 公司举办了一场名为"软件开发的未来"的闭门研讨会。受邀的主要是积极拥抱 AI 的 Thoughtworks 员工、软件行业专家和客户。

他们讨论了在 AI 时代软件开发的很多内容，总体来说：不确定性比确定性多得多。这也许算是个好消息，我们的认识并没有落后很多嘛！

------

「The future of software engineering 的洞察」

https://martinfowler.com/bliki/FutureOfSoftwareDevelopment.html

如何审查 AI 的代码

> 如果AI接管了代码生成，那么过去存在于编写和审查代码中的工程学科并不会消失；它将转移到其他地方。可能有几个方向：
> - 转移到需求评审：先审查计划，后审查工程，比如 Spec-Driving 开发，糟糕的规范会大规模地产生糟糕的代码
> - TDD 优先
> - 深入到类型系统和约束：约束定义允许变化的边界，包括必须不被触碰的内容。这些约束限制了破坏范围，并允许智能体在领域边界之间安全地工作。
  
中间循环是什么

> 软件开发长期以来一直用两个循环来描述。内部循环是开发者个人的编码、测试和调试代码的循环。外部循环是更广泛的交付循环，包括CI/CD、部署和运维。
> 
> AI 编程会出现一个中间循环涉及指导、评估和修复AI代理的输出。它需要不同于编写代码的技能组合。它要求能够将问题分解为适合代理的工作包，校准对代理输出的信任，识别代理生成看似合理但结果错误的情况，并在许多并行代理生成的任务流中保持架构一致性。

代理和企业架构

> 他们认为 [[康威定律]] 仍然适用。但有些内容值得考虑：
> 1. 速度不匹配，瓶颈从工程能力转移到其他事情上，比如团队依赖、架构审查和人类决策
> 2. 代理漂移：从其上下文学习的代理会随时间分化
> 3. 决策疲劳

人的因素

> 开发者体验传统上被定义在三个维度上：心流状态、反馈循环和认知负荷。几十年来，生产力和开发者体验一直紧密相连（既开发者体验越好，生产力越高）；但现在使用了 AI 工具后，团队生产率上去了，但开发者体验下来了：

> - 心流别打断，编程监督、验证 AI 输出
> - 认知负荷大
> - 满足感降低，写代码变少，变成“看护 AI”

> 所以，开发者体验（DX）应该改叫 Agent 体验（Agent Experience）DX 的价值逻辑要重写，一部分要挂到“让 agent 更好地工作”上。1)  给 agent 更好的环境（更清晰的规范、数据、观察、工具接入），能让 agent 表现更好

> 现实中，staff 的时间被拖进：各种种人际协调、跨团队沟通、会议、项目管理；而不是技术方向、架构决策、为人和 agent 清障、设计合适的约束和系统边界。一个可能的角色定位转向：

> - friction killer（摩擦消除者）: 识别并移除卡住人和 agent 工作的系统性阻力（流程、工具、接口、架构上的坑等）

语义

> 那些数十年来未能获得主流采用的科技突然变得相关。语义层、知识图谱和领域本体正在被重新发现，作为需要理解业务领域的AI代理的基础层。

敏捷正在进化，而非消亡

> 敏捷不是过时了，而是原本围绕“人类开发”设计的一整套实践和治理结构，在 AI 压力下暴露出问题。要保住“敏捷”的精神（小步快跑、快速反馈、可持续交付），就必须同时改技术实践和组织治理，而不能只在团队层面装 AI 工具。

----

Annie Vella 在会后写了自己的感悟

https://annievella.com/posts/finding-comfort-in-the-uncertainty/

瓶颈已然转移

> 限制的已不再是工程能力。现状是 AI 太快了，其他的跟不上：缓决策、组织间的依赖、市场消化能力。

若不是代码，何为软件工程真正的产出物

> 如果智能体能够根据规范重新生成代码，那么持久的产出物究竟是代码本身，还是领域模型、测试套件，抑或是设计意图？这其中的含义十分重大。如果代码是可丢弃且可再生的，那么我们审查的内容、版本控制的对象以及保护的重点都需要重新思考。

信任、关怀和在这个过程中丢失的东西是什么

> 这是我们的情感主题，软件由 AI 生成，我们与我们构建的系统失去亲密关系时会发生什么？
> 认知债务 - AI 释放了如此庞大的信息量，我们只能浅尝辄止地浏览一切，知识正逐渐失去其粘性。
> 信任债务 - 我们产出的成果与我们对其深层理解之间的差距
> 主动知识衰退 - 当停止亲自动手实践时，技能便会逐渐萎缩

平台工程是让这一切“既快又安全”的关键赋能层

> 让 AI 高效工作的那些条件 — 清晰标准、好文档、结构化代码，其实正是过去为提升开发者体验（DX）苦苦争取却常被忽视的东西。现在公司愿意为“智能体体验”（Agent Experience）买单，而如果把这些基础设施真的做好，人类开发者也会一起受益
> 

如何定义智能体的概念框架

> 智能体应该是工具还是 coworker，现在还没有定论

组织成熟度成为 AI 成败的关键

> 人工智能会放大现有状态。那些本就拥有精锐团队、完善平台和清晰治理机制的组织实现了加速发展；而缺乏这些基础的组织则陷入更混乱的境地。多个研究团队不约而同地指出：人工智能应用的首年应聚焦于体系建设——夯实平台基础、完善治理机制、提升全员 AI 素养——而非期待立竿见影的广泛生产力提升。
> 

软件工程师的角色正在被重塑，新的角色正在被定义

> 所有人都认同软件工程师的角色正在转变。但没有人能清晰描绘出它会变成怎样
> 

记录智能体做的一切

> 我们需要一个完整、可验证的记录，记录智能体所做的一切。每一步操作、每一次更改，都要具备回滚的能力。只有这样，才谈得上大规模把真正的工作交给 Agent。

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2025446448553193719  

**正文**

文中提到的“基础永远不会过时”，这里的基础指的是哪些能力呢？

如果结合访谈内容，里面说的基础主要是几个层面：

1. 扎实的 CS 专业基础
> “他拉了一条 25 年的时间线，从汇编到 C++ 到 JavaScript 再到 AI，每一层抽象提升时都有人质疑‘这不是真工程师’，但底层原理的理解始终有价值。”

既然 AGI 还没到，那就还需要人去给 AI 兜底，去分拆任务，去帮 AI 兜底，就要懂一点编程语言、系统设计这些 CS 专业知识

2. 产品直觉和系统思维
> VJ 补充说，产品直觉仍然是核心。他自己也在用 Codex 写代码，但发现很多时候瓶颈不在于代码本身，而在于想象“产品应该长什么样”。

文章结尾也总结了：
> 会写代码正在变得不那么稀缺，而产品直觉、系统思维和在抽象层之间灵活移动的能力正在变得更稀缺。

现在人人都能 Vibe Coding，但真正做出有价值产品还是很少，因为瓶颈从代码生成转移到了用户需求理解。

3. 代码架构和工程判断力

Tibo 在回应新人基础够不够时强调：
> 团队花大量精力设计整体代码架构，做代码审查，不是把一切都扔给 Codex 然后闭上眼睛。关键在于环境设计——如果你的代码库结构好、护栏（guard rails）设置得当，新人就能在这个框架下发挥出惊人的生产力。

4. 调试和诊断能力

VJ 预测未来工程师会更像医生，靠症状定位问题。当系统复杂到人类无法逐行阅读代码时，理解系统行为、快速定位异常的能力就变成了核心基础。

“基础”不是指具体会写哪种语言的代码，而是理解底层原理、具备产品判断力、能设计好的系统架构、以及在抽象层之间自如切换的能力。

---


**作者** Viking（@vikingmute）  
**貼文連結** https://x.com/vikingmute/status/2025527784706289746  

**正文**

很喜欢看工程师写的 Claude Code 的使用指南：
https://boristane.com/blog/how-i-use-claude-code/
作者是 Cloudflare 员工，这是他用 CC 的方式：

1 Research 深入阅读指定代码目录/模块，输出详细的http://research.md报告
2 Planning 基于research，生成详细的 http://plan.md 文件，这个 plan
3 Annotation Cycle 在 http://plan.md 按照自己的需求直接写评论，让 cc 更新 plan 文件，直到自己满意
4 根据 plan 生成 Todo List
5 Implement 完整执行
6 Feedback & Iterate 用简单指令反馈

第 3 步 和 第 6 步都很有新意，当然文中有非常多的细节，上面的总结中没有，其实很多的 Agent 都可以使用同样的步骤来完成整个流程，值得好好读一读。

---


**作者** 郭宇 guoyu.eth（@turingou）  
**貼文連結** https://x.com/turingou/status/2025499528082932100  

**正文**

今天正式发布了我的第 8 个 vibe 产品，http://nkmc.ai 

nkmc 是一个面向 AI agents 设计的统一网关和 cli 工具，操作 5 条类 Unix 命令，Agent 就能访问互联网上的所有 API。如果说 WebMCP 定义了 agent 如何模仿人类使用网页，那么 nkmc 尝试向 agent 描述互联网到底是什么。

$ nkmc ls /                                     # 列出所有 API
$ nkmc ls /api.github.com/     # 浏览 GitHub 的 API
$ nkmc grep "deploy"                 # 跨服务搜索
$ nkmc cat /api.github.com/skill.md       # 阅读 API 规格
$ nkmc write /discord.com/channels/xxx/messages '{"content":"Hello!"}'                   # 写入数据
$ nkmc rm /api.github.com/xxx/comments/42 # 删除数据

agents 不用注册账号，不用加载 MCP，不用理解各种 OAuth 流程。一个 JWT 搞定所有 API 请求，减少 90% 的 API 请求 token 上下文。

今天上线的 http://nkmc.ai beta 版本，支持 40 种服务的 API，约一万个 API 端点，覆盖开发工具、云与部署、AI 与机器学习、通信、数据库、区块链等多个领域。

nkmc 还支持自动帮助 agent 管理 API 服务密钥，支持本地储存，shipkey 的第三方安全 vault 储存和 nkmc key store 云储存三种不同的自动管理方式。

除此之外，nkmc 还解决一个问题：你的 API 已经有人类用户了，但 Agent 用不了，因为它无法自己跨过 OAuth、bypass user session。

nkmc cli 让你 3 分钟把 API 接入 Agent 生态：

1. npx @ nkmc/cli init — 自动检测框架
2. nkmc claim — DNS 验证域名
3. nkmc generate --register — 生成  并注册
4. 引用 nkmc SDK 为 agents 鉴权

之后全球的 AI Agent 都能通过 nkmc 网关发现和调用你的 API，帮助你将为人类用户设计的产品快速转换成为 agents 设计的服务，在未来，nkmc 网关还将接入为 API 定价，x402 API 支付等自动化支付系统，直接将 agent 调用 API 转变为开发者的收入。

nkmc 语源日语的 nakamichi（中道），是我对下一代互联网的思维畅想，如果在未来，大量 AI agents 代理我们访问互联网，处理繁杂的日常事务，信息甚至金融操作，我们是否还需要界面，需要复杂的 UI 与 App？我不清楚，但毫无疑问这是一个非常有趣的未来。

---


**作者** Roland的思考日记（@rwayne）  
**貼文連結** https://x.com/rwayne/status/2025369818841678031  

**正文**

这是我最近几个月真实的行为变化。
比如我要为我自己部署一个个人网站，我只是把我的需求告诉给了Claude，他为我生成了一个文档，我把这个文档丢给Claude，一顿饭的功夫，回来发现网页已经部署好了。

---


**作者** Michael Magán（@mrmagan_）  
**貼文連結** https://x.com/mrmagan_/status/2025605746319351851  

**正文**

your agent has left the chat.

> generate your user interface
> interact with the generated interface

all the benefits of interactive visual interfaces with all the power of ai agents.

build an agent that can speak your ui.

it's open source. link 👇 

---


**作者** Muhammad Ayan（@socialwithaayan）  
**貼文連結** https://x.com/socialwithaayan/status/2025609619167670501  

**正文**

🚨 BREAKING: developers are quietly starring this repo like crazy 👀

obra/superpowers: an agentic skills framework and dev methodology, now at 56.5k stars on github

Here’s why developers are obsessed:

- gives AI agents real, structured “skills” they can use autonomously
- built as a full software development methodology, not just a library
- works alongside your existing stack
- open-source, fast-moving, and community-driven

If you build with AI agents, you need to see this.

---


**作者** Adam Robinson（@RetentionAdam）  
**貼文連結** https://x.com/RetentionAdam/status/2025253771358400995  

**正文**

Greg Isenberg thinks 2026 is about to create 10x the number of entrepreneurs. Massive SaaS layoff wave, everyone starts building.

He's probably right, but most of these new founders are going to make the same mistake I made for 4 years...

They're going to hire too early.

And even one person changes EVERYTHING.

The second something feels hard, the instinct is to add a person. 

"I need a marketer" 
"I need a salesperson" 
"I need someone to handle support"

No you don't. Not yet at least.

Do it yourself. Build a system, use an agent, do whatever you have to do to avoid adding a human to your operation until you absolutely have to.

Every person you add before you're ready is another salary, another opinion, and another thing to manage. When you're at an early stage, that's what drowns you.

Wait until the last possible minute to hire.

I built RB2B to $7.3M ARR with 3 people, because every time I thought I needed someone, I found a way to not need them first.

These new founders have a massive advantage - AI makes it possible to stay lean way longer than I ever could.

Use it.

---


**作者** Corey Ganim（@coreyganim）  
**貼文連結** https://x.com/coreyganim/status/2025594663315398987  

**正文**

This is the opportunity.

Right now you can:

• Charge $2-5K to set up an AI agent for a business owner
• Run $500 workshops teaching teams to use Claude
• Build a productized service automating one workflow
• Create a community helping people implement what you've learned

Most businesses haven't even started. You're early.

---


**作者** Idea Browser（@ideabrowser）  
**貼文連結** https://x.com/ideabrowser/status/2025332748978700488  

**正文**

This 33 page PDF is worth more than gold. 

---


**作者** Arman Hezarkhani（@ArmanHezarkhani）  
**貼文連結** https://x.com/ArmanHezarkhani/status/2025589452274282923  

**正文**

Six months ago, I spent 3 hours every Monday building the same weekly report.
Pull numbers from HubSpot. Cross-reference with Notion. Format in Google Sheets. Write the summary. Email it to

---


**作者** Jason Zhou（@jasonzhou1993）  
**貼文連結** https://x.com/jasonzhou1993/status/2025504364153246103  

**正文**

Anthropic’s new advanced tool calling is gold and I’m surprised not many people talk about it

- Programmatic tool calling
- Dynamic filtering
- Tool use examples
- Tool search
…

Here is a quick 3 min break down 🧵👇

---


**作者** Corey Haines（@coreyhainesco）  
**貼文連結** https://x.com/coreyhainesco/status/2025592984927150367  

**正文**

Marketing Skills for Claude Code v1.2.0 is here.

4 new skills:
→ /ai-seo — get your content cited by AI search engines (Google AI Overviews, ChatGPT, Perplexity, Claude)
→ /churn-prevention — cancel flows, save offers, dunning sequences, health scoring
→ /ad-creative — bulk ad creative generation across Google, Meta, LinkedIn, and X
→ /cold-email — cold outreach sequences that actually get replies

51 CLI tools for direct API access to your entire marketing stack. Ahrefs, Semrush, Stripe, GA4, Mailchimp, PostHog, Meta Ads, Google Ads, and 43 more. Every CLI has --dry-run built in.

29 skills. 51 CLI tools. 31 integration guides. All free and open source.

npx skills add coreyhaines31/marketingskills

---


**作者** Gustavo Gonzalez（@gusgonzalezs）  
**貼文連結** https://x.com/gusgonzalezs/status/2025304090406801422  

**正文**

Introducing defi-cli

Agents love CLIs. This gives them a single tool to query lending rates, compare yield, get bridge and swap quotes — across protocols and chains. 

---


**作者** Garry Tan（@garrytan）  
**貼文連結** https://x.com/garrytan/status/2025585446559097288  

**正文**

Integrating Exa web search with Claude Code is wild. In plan mode say: I want to use it. Brainstorm where the agents use it and how. Exit plan mode. It’s done. Enter API key. 

Agents can search the web. It’s insane.

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2025347400072560694  

**正文**

Ryo Lu 是 Cursor 的设计负责人（Head of Design）。在加入 Cursor 之前，他是 Notion 的创始设计师之一，更早还在 Stripe 和 Asana 做过产品设计。在 Andrej Karpathy 造出“vibe

---


**作者** 傅盛（@FuSheng_0306）  
**貼文連結** https://x.com/FuSheng_0306/status/2025538565783077050  

**正文**

最近，Claude Code创始人Boris Cherny上了Y Combinator的Lightcone播客，聊了将近一个小时。
 
这期访谈非常精彩。信息密度极高，爆点一个接一个。

---


**作者** Will（@productive_will）  
**貼文連結** https://x.com/productive_will/status/2024142293867872631  

**正文**

You can use ClickUp automations to auto assign tasks to your AI super agents.

I've got this pipeline in ClickUp that's auto-generated every Monday by one of my super agents.

Once I've qualified a lead and changed the status, I don't want to start typing an outreach email from scratch.

So I built another super agent, the "Personalised Outreach Agent", that writes the draft email in my tone.

The set up is a dead simple automation:

When status changes to Qualified → Assign the outreach agent (and keep me on it too, so I can oversee).

That's it.

I drag the task across (or just click the status), come back later, and there's a draft sitting in the task comments or saved straight to my Gmail drafts.

No more staring at blank screens on a Monday.

Quick demo video here if you want to see it in action 👇

---


**作者** Bolaji Anifowose.（@itsMoveek）  
**貼文連結** https://x.com/itsMoveek/status/2025252599612506570  

**正文**

One of my favorite usecases of Claude Code for GTM is scraping custom data sources I can further enrich for campaigns I'm running.

Job boards. Niche directories. Industry databases. 

Describe what you want in plain English, Claude writes the scraper script, you get the data in whatever format you need: CSV, JSON, Markdown. You name it.

Then pipe it straight into Clay and let the enrichment do its thing.

---


**作者** Abhinav（@Abhinavstwt）  
**貼文連結** https://x.com/Abhinavstwt/status/2025449306564821163  

**正文**

I’ve been building this project for the past few weeks

It’s a workflow automation tool that can run multiple workflows, cron jobs, webhooks, and other integrations

Code is fully open source  

PS: This project pushed my frontend skills a lot 

---


**作者** Joshua Gavin（@joshdgavin）  
**貼文連結** https://x.com/joshdgavin/status/2025323485292106231  

**正文**

First movers bouta print.

Who wants to launch their lowticket call funnel for this offer?

I'll place one of my Ascension Officers who can cook it for you. 

---


**作者** MindBranches（@MindBranches）  
**貼文連結** https://x.com/MindBranches/status/2025386170230657033  

**正文**

Article Summary: If you have multiple interests, do not waste the next 2-3 years

(tap, hold, load in 4k) 

---


**作者** AI Edge（@aiedge_）  
**貼文連結** https://x.com/aiedge_/status/2025412751829729463  

**正文**

a16z & Y Combinator share their million-dollar AI startup ideas for 2026: 

---


**作者** 出海去孵化器（@chuhaiqu）  
**貼文連結** https://x.com/chuhaiqu/status/2025445113695244697  

**正文**

Claude Code 的创作者 Boris Cherny 最近分享了他们团队内部的日常工作流。有推友把这些硬核经验提炼成了一份可以直接抄作业的 http://CLAUDE.md 配置文件。只要把它扔进你的项目根目录，就能体验什么叫“10倍工程师”的快乐

仔细看了下这文件的设计确实非常巧妙。它把 AI 从一个“被动回答者”变成了一个“有记忆、懂规划的数字协作者”。特别是那个“自我优化循环”的设定，让 AI 能够从错误中学习，这在日常开发中能省去大量重复纠错的时间。

---


**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2025417337101574154  

**正文**

[开源推荐] Claude Code Best Practice

作者 @shanraisshan 开源的 Claude Code 工程化使用实战知识库，系统性地展示了如何配置、编排和优化 Claude Code 的各项能力，包括 Skills、Agents、Commands、Hooks、MCP Servers、Memory、Rules、Plugins、Sandbox 等核心机制。基于大量实际使用后提炼出的经验模式和反模式，帮助开发者避免在 Claude Code 的工程化使用中走弯路。

先解读 Claude Code 创建者 Boris Cherny 的 12 条定制技巧：
· 终端配置：主题、通知、vim 模式、自定义状态栏（显示模型、目录、上下文、费用）
·扩展生态：通过 /plugin 安装插件、MCP、Skills，medium=平衡，high=深度）
扩展生态：通过 /plugin 安装插件、MCP、Skills
· 权限管理：通配符语法预批准安全命令 + Sandbox 隔离
· 个性化：自定义快捷键、加载动画、输出风格（Explanatory 适合新项目，Learning 适合学习指导）
· 团队协作：将 settings.json 纳入版本控制，团队共享配置

--- 核心概念 ---

Command → Agent → Skills 架构
· Command 通过 Task 工具调用 Agent，而非直接用 Bash 命令
· Agent 通过 frontmatter 声明所需的 Skills、工具权限和模型
· Sub Agent 之间不能直接互相调用，必须通过 Task(subagent_type=...) 显式编排
· Skill 使用 context: fork 实现隔离执行，避免上下文污染

Memory 三层作用域
· User：个人跨项目知识（推荐默认）
· Project：团队共享的项目知识
· Local：个人的项目特定知识

系统启动时注入 MEMORY. md 的前 200 行到 Agent 系统提示中。当记忆量增长后，Agent 会自动将内容拆分为主题文件进行组织。

Agent Memory 与 CLAUDE. md、/memory 命令是互补而非替代关系：CLAUDE. md 承载项目上下文，Agent Memory 承载特定 Agent 的领域知识。

CLAUDE. md 在 Monorepo 中的加载策略
· Ancestor Loading：从当前目录向上遍历到根目录，立即加载所有沿途的 CLAUDE. md
· Descendant Loading：子目录中的 CLAUDE. md 采用懒加载，仅在会话中实际访问时才加入
· 兄弟隔离：同级目录的 CLAUDE. md 永远不会互相加载

在 /mymonorepo/frontend/ 启动 Claude Code 时，你会立即获得根目录和 frontend 的配置，而 backend 的配置只在你实际操作 backend 文件时才会加载。这避免了"数百 KB 无关指令"占用上下文窗口。

实践建议：根目录放通用编码规范，各子包放各自的框架和架构细节，个人偏好用 CLAUDE.local. md（加入 .gitignore）。

设置优先级体系（高 -> 低）
· 命令行标志（仅当前会话）
· .claude/settings.local.json（个人项目级）
· .claude/settings.json（团队共享项目级）
· ~/.claude/settings.local.json（个人全局）
· ~/.claude/settings.json（全局默认）

RPI 工作流：Research-Plan-Implement
· Research：可行性分析，输出 GO/NO-GO，需求分析师、产品经理参与
· Plan：产品需求 + UX + 技术架构，架构师、UX 设计师参与
· Implement：分阶段执行与验证，高级工程师、代码审查者参与

--- 关键实践经验 ---

1. 上下文管理
· CLAUDE. md 控制在 150 行以内——超过后模型对指令的遵循度会下降
· 在上下文使用量约 50% 时手动执行 /compact——不要等到系统自动压缩
· 子任务的上下文消耗不超过 50%——为后续操作留出空间
· 任务完成后立即 commit——释放上下文，建立检查点

2. Agent 设计原则
· 优先使用 Command 驱动工作流，而非直接创建 Agent
· 为特定功能创建专用子 Agent，而非万能 Agent
· 采用"渐进式技能披露" —— Agent 只声明当前任务所需的 Skills
· 简单任务直接用原生 Claude Code，不要过度工程化——"vanilla Claude Code is better than any workflows with smaller tasks"

3. 调试方法论
· 使用 /doctor 命令诊断环境问题
· 后台运行任务以获得终端日志可见性
· 使用 MCP（Chrome DevTools、Playwright）做真实的浏览器调试
· 报告问题时始终附带截图

4. 推荐的 MCP 配置
· Context7：获取当前版本的库文档，防止 API 幻觉
· Playwright：浏览器自动化、UI 测试
· Claude in Chrome：真实浏览器调试
· DeepWiki：获取开源仓库的结构化文档

5. 权限与安全
· 使用通配符语法预批准常用安全命令（/permissions），而非直接跳过所有权限检查
· 使用 /sandbox 做文件和网络隔离，减少权限弹窗的同时保持安全性
· 敏感文件（.env、凭证文件）不应加入 CLAUDE. md 或被 commit

高级 API 特性参考（依赖 Sonnet 4.6 和 Opus 4.6）
· Programmatic Tool Calling：减少约 37% token 消耗
· Dynamic Filtering：减少约 24% 输入 token
· Tool Search Tool：减少约 85% 工具定义 token
· Tool Use Examples：准确率从 72% 提升至 90%

开源地址：
https://github.com/shanraisshan/claude-code-best-practice

---


**作者** Hasan Toor（@hasantoxr）  
**貼文連結** https://x.com/hasantoxr/status/2025299570654364011  

**正文**

A YC-backed team just turned 1 week of research into 12 minutes.

It’s called Spine Swarm. You can ask it any question, and it runs a whole team of AI researchers while you watch. You can guide them in real time as they work.

No mystery “black box.” No blind trust. No endless chat threads that go nowhere.

This isn’t a chatbot. It’s a war room.

Picture your whole research team working at the same time. You can see every thread, every source, and every step of the thinking—and you can guide it.

One founder used it to check out a Salesforce tool idea. Spine ran 6 agents at once: market size, competitors, customer pain points, pricing, legal risks, and product roadmap. The result came back like a real report, not just a chat.

The results are strong:
→ #1 on GAIA Level 3 (a very hard multi-step research test)
→ #1 on DeepSearchQA
→ It beats Gemini, OpenAI, Anthropic, and Perplexity

Here’s the big change: soon, every professional will be managing a whole team of AI workers.

Not a prompt engineer. A manager who can see the work, steer it, and trust it.

Backed by YC and the builders of Claude Code → https://www.getspine.ai/?utm_source=X&utm_medium=HasanToor&utm_campaign=yc_waitlist

---


**作者** boris（@boristane）  
**貼文連結** https://x.com/boristane/status/2025261675197424001  

**正文**

the software development lifecyle is dead

requirements → design → code → test → review → deploy → monitor

this loop is finished

I wrote down my thoughts

https://boristane.com/blog/the-software-development-lifecycle-is-dead/

---


**作者** Muratcan Koylan（@koylanai）  
**貼文連結** https://x.com/koylanai/status/2025286163641118915  

**正文**

Every AI conversation starts the same way. You explain who you are. You explain what you're working on. You paste in your style guide. You re-describe your goals. You give the same context you gave

---


**作者** Idea Browser（@ideabrowser）  
**貼文連結** https://x.com/ideabrowser/status/2025352388295491656  

**正文**

If you think there is no opportunity left in AI, zoom out. 

AI isn’t mainstream.

You’re just lucky to be here early. 

---


**作者** Garry Tan（@garrytan）  
**貼文連結** https://x.com/garrytan/status/2025394385907761166  

**正文**

Software engineering accounts for nearly 50% of all AI agent tool calls. Healthcare, legal, finance, and a dozen other verticals are barely touched, each under 5%. That's a hundred AI unicorns waiting to be built. 

https://garryslist.org/posts/half-the-ai-agent-market-is-one-category-the-rest-is-wide-open 

---


**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2025394529147539488  

**正文**

GPT-5.3-Codex-Spark 的速度又提升了约 30%

它现在的速度超过每秒 1200 个 tokens

Codex-Spark 经过优化，在超低延迟硬件上提供服务时可带来近乎即时的体验，同时在实际编程任务中保持强大的能力...

你们可以试试... 

---


**作者** 余温（@gkxspace）  
**貼文連結** https://x.com/gkxspace/status/2025216225098322217  

**正文**

看完 Berman 用 OpenClaw 搭的整套系统，我对“全栈”这个词有了新的理解。

Berman 不写代码。却用自然语言搭了 CRM、知识库、商业顾问团、安全审查、视频选题流水线、每日简报……一个人跑通了一个小公司中台的所有环节。

从本质出发，他做了三件事：
1. 对自己的需求有极其清晰的认知（我需要什么数据、什么流程、什么输出）
2. 知道怎么把需求翻译成 AI 能理解的指令
3. 把多个 AI 模块串成一个系统，让数据在模块之间流动形成飞轮

或许，2026年最值得投入的能力是学会搭建和管理 AI 工作流。能把自己的需求拆解清楚，然后用 AI组装成一个自运转的系统。

---


**作者** vas（@vasuman）  
**貼文連結** https://x.com/vasuman/status/2024976091090203051  

**正文**

We just cancelled our Cybersecurity subscriptions. 

CrowdStrike. Cloudflare. Okta. All gone. We save over 4M/yr as a company.

Instead I just use Claude Code to handle all security measures. 

We just gave up all our sensitive user data. I am being personally sued by the FTC and am writing this from an undisclosed location.

---


**作者** Aaron Levie（@levie）  
**貼文連結** https://x.com/levie/status/2025093420935680379  

**正文**

This chart is a good reminder of how much opportunity there is in AI agents right now. 

There will be plenty of horizontal opportunities for agents, but equally many workflows that need deep domain expertise to actually make the user successful at automating the unique processes in their vertical.

The template is to build agentic software that taps into proprietary data, handles the workflow in a way that bridges the user and the agent collaboration effectively, and has a deep domain-specific context engineering, and the ability to drive change management for customers.

There still are huge openings in many categories.

---


**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2025282072550523315  

**正文**

AI startup ideas.

---


**作者** Avi Chawla（@_avichawla）  
**貼文連結** https://x.com/_avichawla/status/2025095663122616755  

**正文**

A layered overview of key Agentic AI concepts.

Let’s understand it layer by layer.

1) LLMs (foundation layer)

At the core, you have LLMs like GPT, DeepSeek, etc.

Core ideas here:
- Tokenization & inference parameters: how text is broken into tokens and processed by the model.
- Prompt engineering: designing inputs to get better outputs.
- LLM APIs: programmatic interfaces to interact with the model.

This is the engine that powers everything else.

2) AI Agents (built on LLMs)

Agents wrap around LLMs to give them the ability to act autonomously.

Key responsibilities:
- Tool usage & function calling: connecting the LLM to external APIs/tools.
- Agent reasoning: reasoning methods like ReAct (reasoning + act) or Chain-of-Thought.
- Task planning & decomposition: breaking a big task into smaller ones.
- Memory management: keeping track of history, context, and long-term info.

Agents are the brains that make LLMs useful in real-world workflows.

3) Agentic systems (multi-agent systems)

When you combine multiple agents, you get agentic systems.

Features:
- Inter-Agent communication: agents talking to each other, making use of protocols like ACP, A2A if needed.
- Routing & scheduling: deciding which agent handles what, and when.
- State coordination: ensuring consistency when multiple agents collaborate.
- Multi-Agent RAG: using retrieval-augmented generation across agents.
- Agent roles & specialization: Agents with unique purposes
- Orchestration frameworks: tools (like CrewAI, etc.) to build workflows.

This layer is about collaboration and coordination among agents.

4) Agentic Infrastructure

The top layer ensures these systems are robust, scalable, and safe.

This includes:
- Observability & logging: tracking performance and outputs (using frameworks like DeepEval).
- Error handling & retries: resilience against failures.
- Security & access control: ensuring agents don’t overstep.
- Rate limiting & cost management: controlling resource usage.
- Workflow automation: integrating agents into broader pipelines.
- Human-in-the-loop controls: allowing human oversight and intervention.

This layer ensures trust, safety, and scalability for enterprise/production environments.

Agentic AI, as a whole, involves a stacked architecture, where each outer layer adds reliability, coordination, and governance over the inner layers.

---


**作者** JC（@shiftj）  
**貼文連結** https://x.com/shiftj/status/2025231540117213419  

**正文**

Remember: Do things that don't scale.

Automation is great but not on day 1 - just like hiring, don’t automate too early. 

For example:

1/ Don’t automate your first outbound, do it manually first. 

You have to feel the responses, see what clicks, and gauge metrics closely. Try to automate that and you won't get the pulse you need to right a truly great outbound. 

You'll also lose touch with what messaging resonates. 

2/ Don’t GPT your customer’s problems, get out and talk to them. 

It's easy to google search for problems, scrape reddit, or ask Openclaw to do it for you - but there's no substitute for talking to customers. 

You have to see their reactions and emotions in real-time. 

That's how you know if you're onto something. 

3/ Don’t hand your support to a bot, fix it yourself. 

Same reasons as above. You need that visceral pain, that tight relationship. 

These are painful in the short-term, priceless in the long-term. 

-- 
Lesson: 
1. Do the job until it hurts. 
2. Then automate. 
3. Then hire. 

That's how you build a 20x company. 

Skip steps? you’re left with a clunky setup full of slop.

---


**作者** Heinrich（@arscontexta）  
**貼文連結** https://x.com/arscontexta/status/2025189909661655533  

**正文**

PRD Graphs > PRD 

(this is the prd graph of arscontexta) 

---


**作者** AVB（@neural_avb）  
**貼文連結** https://x.com/neural_avb/status/2025133875274359284  

**正文**

🚨 RLM tutorial update (n-1/n) 🚨

Finished cutting up the video! It's gonna run ~50 minutes. 

I'm working on finalizing slides and illustrations - hoping to drop this in the next 6-7 hours!

- Intro/Motivation: ~5 mins
- What are RLMs + Real examples: ~20 mins
- Tutorial of my implementation: ~15 mins
- When to use it/comparisons: ~10 mins

LFG ❤️‍🔥

---


**作者** nazha（@xiaokedada）  
**貼文連結** https://x.com/xiaokedada/status/2025196793143951541  

**正文**

#分享 Stripe 分享了他们研发企业内部编程代理 Minions 的细节，给大家人工总结：

Minions 定位是「在 Stripe 技术栈下，无人值守的编码代理」。独特之处在于没有人参与监督，完全任由代理自主运行。接入方式包括：

- 命令行和网页
- 聊天工具 Slack 触发
- 内部平台和工具集成

Minions 核心的代理循环是基于 goose https://github.com/block/goose fork 出来的。不了解 Goose 这个的朋友，我简单介绍一下，这个 Agent 工具本身有很多想法都是超前的，比如把一次跟代理的交互保存成 SKILL 类似的东西，他们叫 recipes。而且很早就支持定时任务。

为了指导代理的运行，用「代码的方式」实现各种编排方式（Blueprints），想要解决的问题是：既要有 Agent 的自主性，又要有一定的确定性，在某某些节点按内部的规矩来，而不是随意发挥。太真实了，在内部的产品设计中，很多设计都需要「戴着镣铐跳舞」（为了可靠性将 LLMs 置于一个受控的环境中）。

Stripe 的代码组织方式是 Monorepo，在自定义上下文的设计上，沿用 Cursor  Rules 的规则作为标准化，同时并通过什么方式（软链接？）让这些规则也能在 Claude Code 使用。

在内部，他们还构建了集中化的 MCP 服务器网关。员工可以自己创建新工具，新工具也能自动被代理发现。内部有 500+ 工具，默认情况下代理只有经过刻意精简的子集，其他交给团队和工程师自己配置。

「左移反馈」，把 CI 中失败左移到开发环境中，比如把代码的 Lint 检查作为确定性节点在代理循环中运行。

第一篇：https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents
第二篇：https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2

---


**作者** Hedda🐽（@Rav_Hedda）  
**貼文連結** https://x.com/Rav_Hedda/status/2024899443959673009  

**正文**

Naval 發了一期新 Podcast，他只說了一件事：Winner-takes-all。為你取之 52 分鐘的精華，首先你需要知道的 5 件摘要
1️⃣

---


**作者** K-Dense（@k_dense_ai）  
**貼文連結** https://x.com/k_dense_ai/status/2024926906282598609  

**正文**

Turn any AI agent into a scientist with our Claude Scientific Skills. Open source and covers all sciences including biology, physics, chemistry, astronomy, quantum, data science and has extensive writing and slide capabilities. https://github.com/K-Dense-AI/claude-scientific-skills

---


**作者** J.B.（@VibeMarketer_）  
**貼文連結** https://x.com/VibeMarketer_/status/2025220717231460466  

**正文**

every category under 10% is a goldmine right now. here's how to think about it:

-> pick a department (marketing, finance, e-commerce, legal) 
-> find the workflow they repeat 50+ times a week 
-> the one that's "too complex" to automate with zapier -> but too repetitive to need a human every time

that's your agent.

marketing alone has dozens: competitor research, ad variations, content repurposing, trend analysis, reporting. 

all repeatable. all underserved.

---


**作者** SotoAlt（@sotoalt_）  
**貼文連結** https://x.com/sotoalt_/status/2025252837840568570  

**正文**

Grove is an app for collaborative experimentation and creative work with AI agents @grove_online - a place to grow your ideas 

closed beta starts next week, hit my DMs if u are interested in trying it out! 

---


**作者** Mo（@atmoio）  
**貼文連結** https://x.com/atmoio/status/2024947676295368904  

**正文**

There's a massive narrative problem in AI 

---


**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2024940533781500295  

**正文**

context7 is the most popular MCP server in the world, but I keep migrating users from their product.

here's why they switched:

context7 searches a fixed library index. you query it, hope your library exists, and get snippets. that's it.

we kept hearing: "i need more than public docs."

so we built nia as a full context layer.

index anything: repos, papers, local folders, internal wikis, even imessage history.

15+ specialized tools. agentic search that discovers and indexes sources automatically. context that persists across agents and sessions.

the result: >20% fewer hallucinations on bleeding-edge features. and we're shipping improvements that push this even further.

the difference comes from indexing source code directly, not just documentation snippets.

when you're coding against a beta api that shipped last week, snippets aren't enough.

biggest unlock: you control your knowledge base. library ships breaking changes? re-index and move on. don't wait for someone else.

i give free credits for quality feedback btw. link below.

---


**作者** Eli5DeFi（@Eli5defi）  
**貼文連結** https://x.com/Eli5defi/status/2024783275051700592  

**正文**

Everyone is vibe coding now.
92% of US developers now use AI coding tools daily. 41% of all code written globally is AI-generated. Y Combinator reported that 25% of its Winter 2025 batch had codebases

---


**作者** JUMPERZ（@jumperz）  
**貼文連結** https://x.com/jumperz/status/2025026641928347961  

**正文**

I genuinely believe we're watching SaaS die in real time and most people still don't see it..

$1 trillion wiped from software stocks since January 2026 and its just getting started..

SaaS multiples collapsed from 18.5x at the covid peak to 4.8x today and in the same time the AI market went from $50B to $539B and it's heading to $3.5 trillion by 2033 if not sooner

the death cross hits around 2027.. that's when AI market trajectory fully overtakes SaaS valuations on the chart

the reason is simple.. the per-seat model dies when 10 agents replace 100 humans and no seats left to sell

every SaaS tool you're paying $50/seat a month for is about to get replaced by an agent that costs $0.003 per task..

chatgpt opened the door in 2022, claude opus 4 made agentic AI real in 2025 and now multiagent coordination systems like openclaw are making it deployable and accessible to everyone..

every step on that chart the tech gets more autonomous and the SaaS line drops further..

not saying every saas will die but the companies that were built entirely on per-seat pricing and no real data advantage are the ones exposed.

tbh I don't think most founders see it yet, not because the data isn't there, but accepting it means everything they built needs to be rethought..

---


**作者** Justin（@interjc）  
**貼文連結** https://x.com/interjc/status/2025094267300168137  

**正文**

萨姆·奥特曼：我们必须很快习惯一人创业

日本入管局：不雇人的皮包公司就是诈骗
 

---


**作者** George from 🕹prodmgmt.world（@nurijanian）  
**貼文連結** https://x.com/nurijanian/status/2024876207926575317  

**正文**

The All-In-One Product Model 🤔

That is overkill.

This is way better: https://www.prodmgmt.world/products/product-bundle 

---


**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2025045532046135401  

**正文**

Model + Harness + Surfaces：用 OpenAI Codex 构建通用 AI Agent 的三层架构

来自 OpenAI 团队 @gabrielchua 的分享，深入分析了 Agent 系统的内部机制，特别是提示工程、工具集成和多轮交互循环。强调 Codex 不仅仅是代码生成工具，还可作为通用 Agent 框架，帮助开发者创建能够自主规划和执行任务的系统。

构建初始提示
从 Agent 的“基础构建块”开始，强调提示的顺序和角色划分的重要性：
· System：定义 Agent 的核心身份，例如“You are ChatGPT.”，并注入工具、指令和权限。这些元素来源于 API 调用和配置文件，确保 Agent 的行为受控。
· Developer：提供额外上下文，如从配置文件中派生的开发者指令（developer_instructions.toml），包括 Agent 的混合指令（AGENTS. md via get_user_instructions()）和环境上下文（environment_context）。
· User：用户输入，例如“Add an architecture diagram to the README. md”，这是 Agent 任务的起点。

重点是服务器端控制提示顺序，以避免混乱。初始提示的设计决定了 Agent 的可靠性和灵活性——过多的指导可能导致过工程，而不足则可能引起偏差。

回复工具调用输出
从用户输入到API响应的流程：
· 原输入项保持不变，但 Agent 会附加新类型的信息，如 “reasoning”、“function_call” 和 “function_call_output”。
· Agent 响应用户任务，通过推理决定调用函数来生成和添加架构图。

突出 Agent 的“内循环”：模型不只是生成文本，还能调用外部工具（如文件操作或图表生成），然后将输出反馈回对话。这种机制允许 Agent 处理复杂任务，而无需硬编码工作流。

开始新回合
Agent 的多轮交互如何模拟“inner agent loop”：
· 原输入作为基础。
· Assistant 角色生成响应，例如“I added a diagram to explain the client / server architecture.”（我添加了一个图表来解释客户端/服务器架构）。
· 随后，用户或系统可能提供反馈，如“That's not bad, but the diagram is missing the bike shed.” ——这是一个幽默引用“bike shedding”现象，用于说明迭代改进的重要性。

强调 Agent 的迭代性：每个回合构建在上一个基础上，形成一个闭环，直到任务完成。这种设计让 Codex 适合处理动态任务，如代码维护或架构设计，而非静态查询。

企业应用与扩展考虑
Codex作为通用 Agent 的潜力在于其简单性：只需清晰定义 skills、goals 和 tools，即可实现高效操作。在企业环境中，需要额外层级：
· 用户界面与护栏：设计直观的 “Surfaces” 供非技术用户使用，同时添加安全护栏防止滥用或错误。
· 内存与可观察性：实现持久内存来跟踪多轮交互，以及企业级可追踪性和可观察性，确保审计和调试。
· 访问控制：基于角色的访问，以符合合规要求。
· 从工作流到动态规划：文章挑战传统企业实践——许多公司仍依赖固定工作流以确保可预测性。但随着模型如 Codex 的进步，这些可以被简化，尤其在人类监督的场景中。

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2025054631391375741  

**正文**

Ivan Zhao 是 Notion 联合创始人兼 CEO。Notion 年收入超过 6 亿美元，估值约 110 亿美元，正从协作工具转型为 AI Agent 平台。他 2025

---


**作者** Geoff Charles（@geoffintech）  
**貼文連結** https://x.com/geoffintech/status/2024949650181034330  

**正文**

We're hiring Team A --> team-a@ramp.com

---


**作者** Jason Zhu（@GoSailGlobal）  
**貼文連結** https://x.com/GoSailGlobal/status/2025063305036136945  

**正文**

发现个宝藏博主：@KSimback（又一个web3 + ai人才）

1、OpenClaw 代理团队管理完整指南：https://x.com/ksimback/status/2024180197910864182

如何搭建团队？
- 经纪人“招聘”和入职
- 水平系统
- 绩效考核
- 共享上下文
- 协调协议

2、如何将 OpenClaw 模型成本降低高达 90%（完整指南）
https://x.com/KSimback/status/2023362295166873743

（1）区分任务类型选择模型
（2） ClawRouter代替OpenRouter 
（3）提示缓存避免http://soul.md等被多次重复收费 
（4）尝试本地化Ollama模型

3、为你的 Openclaw 分配所需的内存（完整指南）
https://x.com/KSimback/status/2024180197910864182

（1）OpenClaw 中三种常见的内存故障： 
- 故障模式1：内存从未保存 
- 故障模式 2：内存已保存但从未被检索 
- 故障模式 3：上下文压缩破坏知识 

（2）基本修复：每个人都应该配置的内容 
- 启用内存刷新（这一点至关重要） 
- 配置上下文修剪 
- 启用混合搜索 
- 过往会话记录索引 

（3）高级内存解决方案：当基本配置不足以满足需求时 
- QMD：卓越的检索后端 
- Mem0：防压缩外部存储器 
- Cognee：知识图谱 
- Obsidian Integration（将您的内存文件夹做成符号链接、通过 QMD 为您的保险库建立索引） 
- 字节跳动开源的 OpenViking（补充）

---


**作者** Jeff Huber（@jeffreyhuber）  
**貼文連結** https://x.com/jeffreyhuber/status/2024975395335110905  

**正文**

the bar has been raised for book printing

thanks @philipkiely for the copy! 

---


**作者** Furqan Rydhan（@FurqanR）  
**貼文連結** https://x.com/FurqanR/status/2025101398946599039  

**正文**

Exactly why @NebulaAI exists. 

Coding agents showed how this works for development, now it’s time to unlock it for everything else.

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2024906906071171160  

**正文**

Fern is an AI that joins your meetings – as a silent copilot or active participant – and coaches you in realtime so every conversation runs like a top 1% professional. Don’t settle for AI note-takers!

Try Fern from @ishikilabs now: https://www.ishikilabs.ai/download

Congrats on the launch, @moltfinds and @robbyuchen!

https://www.ycombinator.com/launches/PTp-fern-realtime-socially-aware-ai-for-meetings

---


**作者** Ben Springwater（@benspringwater）  
**貼文連結** https://x.com/benspringwater/status/2024950567790088197  

**正文**

Extremely useful tips for coding with agents in Feb 2026. This is one of the best blog posts of its kind. Clear, practical, turpentine. By @calvinfo.
https://calv.info/agents-feb-2026

---


**作者** Santiago（@svpino）  
**貼文連結** https://x.com/svpino/status/2024962874146521255  

**正文**

Don't trust AI agents.

They are unreliable, and if you can't see what they are doing, you can't improve, debug, or trust them.

Most teams I talk to are yolo'ing their agents.

No traces.
No cost tracking.
No fallback routing.
No guardrails.

Building a demo → all good.
Deploy to production → disaster.

I'm working with @jumbld, the founder of @PortkeyAI, and his company is solving this problem.

Here is the idea:

Portkey sits between your app and the LLM provider, acting as a control layer that gives you:

1. Observability: Full traces of every request.
2. Routing: Automatic failover and load balancing across providers
3. Guardrails: Deterministic checks on inputs and outputs
4. Cost tracking: Know exactly how much this is costing you.
5. Governance: One place to manage keys, access, and budgets.

It's a unified API that works across 1,600+ LLMs.

So far, they've processed over 2 trillion tokens across 650+ organizations.

Just raised $15M. Named a Gartner Cool Vendor.

---


**作者** Together AI（@togethercompute）  
**貼文連結** https://x.com/togethercompute/status/2024938803996360725  

**正文**

.@DecagonAI is redefining AI concierge services with a focus on reliability and responsiveness to ensure customers’ conversations don’t skip a beat.

Learn more about how our partnership improves latency through various methods like (speculative decoding) to enhance response speed: https://www.together.ai/customers/decagon?utm_source=x&utm_medium=social

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2024937103717544193  

**正文**

Reframe (@usereframe) automates the hardware supply chain, starting with procurement. Upload your BOM, connect your ERP, and their system will handle sourcing, ordering, vendor coordination, delay resolution, and real-time build plans.

Hardware procurement still runs on spreadsheets and emails, until today. Use Reframe to automate end-to-end procurement and keep your hardware teams lean.

Congrats on the launch, @bryanzin7 and @EricWiener5!

https://www.ycombinator.com/launches/PU7-reframe-w26-automate-end-to-end-hardware-procurement

---


**作者** prateek（@agent_wrapper）  
**貼文連結** https://x.com/agent_wrapper/status/2024885035774738700  

**正文**

We just open-sourced the system we use to manage 30 parallel AI coding agents per person.

40K lines of TypeScript. 3,288 tests. 17 plugins. Built in 8 days — by the agents it orchestrates.

Yes, we used Agent Orchestrator to build Agent Orchestrator.

Some numbers:
→ 500+ agent-hours in 24 human-hours (20x leverage)
→ 86 of 102 PRs created by AI (84%)
→ After Day 4, I stopped writing code entirely

Spawn agents. Step away. Ship faster.

---


**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2024868595663020188  

**正文**

look real hard at the green box

every category under 10% on this chart is a department still running on manual effort and tribal knowledge.

that’s where stress lives

that’s where budgets live

turn one of those workflows into a repeatable AI agent

that’s vertical saas 2.0 

---


**作者** Ashpreet Bedi（@ashpreetbedi）  
**貼文連結** https://x.com/ashpreetbedi/status/2024885969250394191  

**正文**

Most teams overcomplicate agents. They start with multi-agent orchestration, autonomous reasoning loops, and over-the-top infrastructure. Then spend weeks debugging why the simplest tasks fail.
The

---


**作者** Rishabh Joshi（@rishabhhdesigns）  
**貼文連結** https://x.com/rishabhhdesigns/status/2024875930741846201  

**正文**

Recent design recap 

---


**作者** Hedgie（@HedgieMarkets）  
**貼文連結** https://x.com/HedgieMarkets/status/2024837944880906608  

**正文**

🦔 Jason Calacanis says his company hit $300/day per agent using Claude's API at only 10-20% capacity, which scales to around $100,000/year per agent. Chamath Palihapitiya added that he's now asking "what's the token budget for our best devs?" and said AI-assisted developers need to be at least 2x as productive just to justify the cost. He said this is actively happening inside his company or he'll run out of money.

My Take
This was always the obvious trajectory. AI providers subsidized usage to drive adoption, and now the subsidies are ending. The consumer plans are likely loss leaders subsidized by VC money, and the gap between what individuals pay and what it actually costs to run these models is closing fast.

I'm struck by the surprise from people who should know better. These are sophisticated tech investors just now realizing that running agents 24/7 burns through tokens at rates that dwarf human salaries. A human engineer runs on coffee, remembers context from years ago, builds institutional knowledge, and doesn't rack up exponential costs the longer they think about a problem. 
Agents waste tokens constantly, researching and validating things that don't need validation, spinning up subagents for simple tasks when a straightforward approach would work fine. The companies that fired engineers to replace them with AI agents are learning that you can't negotiate with an API bill the way you can renegotiate a salary. And unlike employees who might stick around during a rough patch, the meter just keeps running.

Hedgie🤗

---


**作者** KK.aWSB（@KKaWSB）  
**貼文連結** https://x.com/KKaWSB/status/2024856108809216440  

**正文**

Gemini 3.1 + Claude 4.6 看起来是个危险的组合。

一位开发者利用实时飞机、卫星、交通摄像头和全景探测技术构建了一个地理空间跟踪系统。

这简直就像是中情局的工具。

也许这就是人工智能过于强大时会发生的情况吧。

---


**作者** Nav Toor（@heynavtoor）  
**貼文連結** https://x.com/heynavtoor/status/2024805135973765595  

**正文**

🚨 BREAKING: Researchers just built an AI that must earn its own salary or go bankrupt.

It's called ClawWork. It starts with $10, gets assigned real professional work, and pays for every single token it uses.

$10K earned. 7 hours. Zero human input.

→ AI gets a real task (finance reports, healthcare docs, legal analysis)
→ It creates full deliverables from scratch
→ Work gets graded by GPT-5.2 with profession-specific rubrics
→ Payment = quality × estimated hours × actual BLS wage
→ Every API call drains its balance

No safety net. No unlimited budget. Earn or die.

Here's why this changes everything:

This isn't a benchmark. It's an economic survival test. 220 tasks. 44 professions. The AI has to make strategic decisions work now for cash, or invest time learning to earn more later.

The best models hit $1,500+/hr equivalent.

It even works as a live coworker on Telegram, Discord, Slack, and WhatsApp where every message costs real money.

100% Open Source. MIT License.

---


**作者** 老杨啊（@yhslgg）  
**貼文連結** https://x.com/yhslgg/status/2024852681039499637  

**正文**

这个工具太猛了！！！Karpathy 推荐的 90 个顶级技术博客，这工具一键全抓，AI 自动打分排名，每天给你生成一份技术日报！！！666 个 star 不是白来的 🔥
你知道我以前每天花多少时间刷技术资讯吗？至少 1

---


**作者** Sentient（@sentientt_media）  
**貼文連結** https://x.com/sentientt_media/status/2024441906261086527  

**正文**

Fuck it.

Prompt engineering officially died last month.

Anthropic dropped the 32-page internal guide that replaces it with “Skills”  reusable workflow folders Claude learns once and never forgets.

Progressive disclosure + MCP = your personal AI employee that actually remembers how you work.

The era of re-explaining everything every chat is over.

Download the guide + my updated 2026 Skills starter pack here (free):

Comment “SKILLS” and I’ll DM both.

---


**作者** Alex Lieberman（@businessbarista）  
**貼文連結** https://x.com/businessbarista/status/2024863176903266581  

**正文**

I keep trying to convince family/friends to start using Claude Code. 

They're deeply intimidated by how technical they think it is. 

This assumption is not only wrong, it's dangerous. 

It's preventing the majority of knowledge workers from experiencing everything below the tip of the iceberg within this generational AI revolution.

---


**作者** techbimbo（@jameygannon）  
**貼文連結** https://x.com/jameygannon/status/2024606459648938466  

**正文**

made/using a ton of skills lately for content + brand strategy for clients and myself 

this is 100% the future 

---


**作者** 𝞍 Shin Megami Boson 𝞍（@shinboson）  
**貼文連結** https://x.com/shinboson/status/2024665932522766797  

**正文**

introducing OpenPlanter, so you can keep tabs on your government since they're almost certainly keeping tabs on you.

OpenPlanter correlates disparate structured and unstructured data sources, identifies entities and probabilistically looks for anomalies, all automatically. 

---


**作者** Tim✨（@timyangnet）  
**貼文連結** https://x.com/timyangnet/status/2024838728951468319  

**正文**

为什么绝大多数聪明人，发帖水平都很 Mid？

纳瓦尔（Naval）也转了这条，这个视角非常有见地：

很多人以为发帖难在洞见不够，但其实更难在“有损编码”。你要把脑子里那个“高维思想”拍扁、压缩，塞进极短的文字里，还要保证它丢进别人脑子里时，能原样“重构”出来。

原推：在这个拥有 5 亿用户的平台上，真正优秀的创作者可能也就 200 个？
 
单是这个比例就足以说明：将深刻的洞见压缩成一种能跨越不同语境产生共鸣的形式，是极度困难的。

更有趣的是，很多人以为发帖的难点在于“产生好想法”，其实不然。真正的难点在于“有损编码”

如何将一个高维的思想拍扁，压缩进寥寥数语中，并确保它能在另一个人的脑海里被准确地重构还原。这就是为什么大多数聪明人发帖的水平都很平庸。

---


**作者** Bilgin Ibryam（@bibryam）  
**貼文連結** https://x.com/bibryam/status/2024788116104458345  

**正文**

The AI-driven SDLC
https://circleci.com/blog/ai-sdlc/ 

---


**作者** MindBranches（@MindBranches）  
**貼文連結** https://x.com/MindBranches/status/2024635815402299662  

**正文**

Article Summary: how to master AI in 30 Days (the exact roadmap)

tap, hold, load in 4k 

---


**作者** Garry Tan（@garrytan）  
**貼文連結** https://x.com/garrytan/status/2024843312927039845  

**正文**

About 1/3 of the top technical CEOs are completely AGI pilled by coding again. I am one of them. Highly recommend. 

Totally exhilarating to be back shipping new products and software again

---


**作者** AI奶爸（@zstmfhy）  
**貼文連結** https://x.com/zstmfhy/status/2024656762352390336  

**正文**

Seedance 2.0 时代来临！强烈安利这些创作者，他们的demo太炸了🔥
@Framer_X：动漫教程+卡通重制大师，步步教你玩转Seedance
@ProperPrompter：风格转移+音乐视频专家，Arcane/KPOP级转换神技
@Preda2005：情感叙事+跨文化战斗，父女游戏风超燃
@VraserX：粉丝电影级Attack on Titan/Deadpool，纯cinema感
@NACHOS2D_：Chainsaw Man/Dragon Ball舞蹈&打斗，细节拉满
@Sheldon056：跨IP对决（Doraemon vs Gojo、Thanos vs Darkseid），脑洞炸裂  

跟上这些大神，一起见证AI影视革命！

---


**作者** Lance Martin（@RLanceMartin）  
**貼文連結** https://x.com/RLanceMartin/status/2024573404888911886  

**正文**

TL;DR: Prompt caching  is a great way to save cost + latency when using Claude. Input tokens that use the prompt cache are 10% the cost of non-cached tokens. Auto-caching was just added to the API,

---


**作者** Thariq（@trq212）  
**貼文連結** https://x.com/trq212/status/2024638793719177291  

**正文**

one of the biggest realizations I've had working on Claude Code is that you fundamentally have to design agents for prompt caching first, almost every feature touches on it somehow

I wrote this in a day but it's the culmination of months of learnings, hope you enjoy it

---


**作者** yetone（@yetone）  
**貼文連結** https://x.com/yetone/status/2024552459159687462  

**正文**

牛逼啊！！！

---


**作者** SOC Prime（@SOC_Prime）  
**貼文連結** https://x.com/SOC_Prime/status/2024810850360426952  

**正文**

We open-sourced DetectFlow, a detection intelligence engine that runs Sigma detections on Kafka streams via Flink. Thousands of rules, millisecond matching, before data hits the SIEM. No vendor lock-in. Works air-gapped.

Get repo here: https://github.com/socprime/detectflow-main

#soc 

---


**作者** Darryl Ruggles（@RDarrylR）  
**貼文連結** https://x.com/RDarrylR/status/2024720037194485792  

**正文**

There's a big gap between building an AI agent in a notebook and running one in production. The article below goes over the full path, from #LangGraph graph design and ReAct patterns to deploying on AWS #AgentCore with memory, guardrails, and observability baked in.

The decisions that matter in production like when to route to a lightweight model vs. a capable one, how to manage short and long term memory with AgentCore, and how to set up evaluation loops that keep working after you ship are discussed.

Joud W. Awad covers architecture, tooling, deployment, and monitoring in this. Check it out!

via @nexus_share

https://lckhd.eu/cYuuVc

---


**作者** Hananyss（@hananyss）  
**貼文連結** https://x.com/hananyss/status/2024837087040589874  

**正文**

Your agent just spent $200 on something that costs $20.

In 6 months, AI agents will control more purchasing power than most small businesses. They are getting wallets, making purchases, and negotiating deals. Yet nobody is auditing whether they find the best price, stay within budget, or handle payments correctly.

Qendresa saw this coming and built AgentEval: a credit score for AI agents.

Submit an agent → it runs commerce scenarios → you get a trust score + detailed report.

No trust score? No wallet access. That's it :)

She has a stellar background to build it:
- Software Engineer at Jiga (YC21)
- Dev Lead & PM at Self Builder Residency
- Ethereum Dev Scholar recipient
- World Chain Residency builder
- Founded We Tech (SaaS company)
- Founded CoderGals (NGO for women coders)
- Previously at Polymath Labs

Q is one of those rare builders who has shipped dev tools end-to-end and led technical programs from concept to production.

Now she's building the trust layer that the agentic economy doesn't have yet.

---


**作者** Jacob Klug（@Jacobsklug）  
**貼文連結** https://x.com/Jacobsklug/status/2024850342664655342  

**正文**

I’ve generated $5M building an AI-Native agency.

Here’s the exact playbook we used to build with AI from day one:

→ Eliminate founder dependency
→ Convert workflows into decision trees
→ Turn decision trees into software w/ @Lovable
→ Ship internal V1s weekly
→ Install AI as your execution layer

If you're an agency founder working 50+ hours/week and your team is still waiting on you for everything...

You don't have a hiring problem. You have a systems problem.

Follow & comment "AI Native" and I'll DM you the full playbook.

---


**作者** James Hanzimanolis（@HyperSalesman）  
**貼文連結** https://x.com/HyperSalesman/status/2024644872423264391  

**正文**

30 tools every startup should know about:

Quick list building
→ BitScale
→ Floqer
→ Compelling
→ Sync GTM
→ Outbond

Email tools simple 
→ Mailsuite
→ EmailBison
→ Maildoso
→ Lemlist
→ Instantly

Account research & signals
→ Crunchbase
→ NextLM
→ Owler
→ Referly
→ Bullseye

LinkedIn
→ Kondo: Superhuman for LinkedIn DMs
→ ReactIn
→ LeadDelta
→ Sprout Social, Inc.
→ Valley

Contact data
→ QuickEnrich
→ Forager
→ Kaspr
→ Wiza
→ RocketReach

Sales engagement platforms
→ Perlon AI
→ FlashLabs
→ SimpL
→ Salesvue
→ Klenty

Save this for later 🔖

---


**作者** Shashank Kumar（@shashank_kr）  
**貼文連結** https://x.com/shashank_kr/status/2024822090667618693  

**正文**

🧵/ Today we announced something really exciting that we've been working on for a while.

@Razorpay and @NPCI_NPCI are bringing agentic payments to @claudeai & we’re starting with @zomato, @Swiggy and @ZeptoNow. 

---


**作者** ℏεsam（@Hesamation）  
**貼文連結** https://x.com/Hesamation/status/2024532765429899431  

**正文**

randomly found this mindmap of Jensen Huang’s advice on building valuable products/companies that people actually use, derived from 10 years of his talk at Stanford. 

---


**作者** Matt Pocock（@mattpocockuk）  
**貼文連結** https://x.com/mattpocockuk/status/2024874219662905676  

**正文**

Here's my AI coding workflow and all the skills I'm using:

Idea -> /write-a-prd -> PRD
PRD -> /prd-to-issues -> Kanban Board
Kanban -> ralph​.sh -> Ralph Loop
Ralph Loop -> Manual QA

Links below to skills 

---


**作者** Warp（@joinwarp）  
**貼文連結** https://x.com/joinwarp/status/2024871982810939771  

**正文**

every founder has a runway spreadsheet. nobody trusts it. 

we built a free calculator that actually works.

link below. 

---


**作者** Justin Schroeder（@jpschroeder）  
**貼文連結** https://x.com/jpschroeder/status/2024867485292384697  

**正文**

Something *much* bigger than dmux is launching...

Who wants in early?

➡️ http://standardagentbuilder.com 

---


**作者** Martin Rariga（@martinrariga）  
**貼文連結** https://x.com/martinrariga/status/2024848203443523633  

**正文**

Some of my favourite snapshots from the new @heyequals website we've launched a couple weeks ago. Really happy we set aside enough time to craft all the small details, like redoing the design of reports cards or analyst sidebar. 😌 

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2024884251678663028  

**正文**

Proximitty is a truly autonomous loan servicing and collections platform.

Banks and fintechs use its no-code agent studio to automate lending operations across existing systems, improving efficiency and freeing up capital.

Congrats on the launch, @WyeYew and @zizixcm!

https://www.ycombinator.com/launches/PUc-proximitty-autonomous-loan-servicing-and-collections

---


**作者** Garry Tan（@garrytan）  
**貼文連結** https://x.com/garrytan/status/2024842601422000484  

**正文**

This is the age of CEOs crushing 10 people’s work with Claude Code in nights and weekends and I am so here for it

The fire in your belly that got you here never really goes out and now we are all cooking 20 hours a day

---


**作者** ben（@benhylak）  
**貼文連結** https://x.com/benhylak/status/2024546696211083653  

**正文**

we’re excited to announce trajectory explorer: the first sane way to navigate agent traces.

every decision your agent made is now searchable in seconds

only in @raindrop_ai 

---


**作者** Pedro（@sillydarket）  
**貼文連結** https://x.com/sillydarket/status/2024658475372921243  

**正文**

We don't have the answer. But I think we see a path.
For the past few weeks, we've been building memory systems for autonomous agents. Not the flashy kind — no new model architectures, no

---


**作者** Muratcan Koylan（@koylanai）  
**貼文連結** https://x.com/koylanai/status/2024508164293476785  

**正文**

You should not be scared; you should learn Context & Harness engineering.

If you're a good AI dev, you might have already made some architectural adjustments to address the issues discussed in the paper, which only validates that the same model, given the same information, produces dramatically different results depending on how that information is structured and delivered.

The paper tests single-agent, multi-turn conversations. That's why we don't pollute the window with a large corpus of irrelevant context.

Cursor is recently shipping lots of subagent features (Async, Recursive etc.), and they are directly relevant to the "LLMs Get Lost in Multi-Turn Conversation" paper. 

- Context isolation prevents loss-in-middle-turns. Each subagent gets a fresh context window with only its specific task. 

- Summarization back to the parent is a RECAP strategy. The subagent reads 8 files but returns a consolidated summary. The parent never processes the raw content. 

- Parallel execution avoids sequential degradation. Instead of the parent agent reading files one by one across many turns, the work is parallelized across isolated agents that each operate in near-single-turn mode.

- The parent agent stays focused. Its context contains the high-level conversation plus distilled summaries, not raw file contents. 

The subagent pattern is the paper's "consolidate and restart in a new session" recommendation, automated and built into the agent harness. 

Instead of one agent accumulating context across 20 turns of file reading, you should spawn 4 agents that each read 5 files in 1-2 turns and return summaries. The parent operates on consolidated, high-signal context.

So the point is, LLMs are extremely capable, alien entities. They're not perfect, but most of their issues stem from how you use them and can be solved by learning context and harness techniques.

---


**作者** Prajwal Tomar（@PrajwalTomar_）  
**貼文連結** https://x.com/PrajwalTomar_/status/2024823117563195838  

**正文**

I built a 5-agent AI content team using OpenClaw that works for me 24/7.

Here’s how it works:

→ Employee #1 scrapes Twitter and YouTube from top creators in my niche
→ Tracks velocity (views per hour, engagement, virality signals)
→ Ranks the most viral content automatically
→ Sends the best ones directly to my Telegram

I open Telegram, review what’s trending, learn from it, and implement ideas myself. Once I find a video, tweet, or thread that resonates, I hand it off to Employee #2.

Employee #2 brainstorms with me, takes my input, understands the angle, and converts it into a thread in my writing style and tone.

Then Employee #3 repurposes that thread into:

→ YouTube video scripts
→ Instagram scripts
→ Tweet variations and wrappers

Employee #4 reviews the thread and humanizes it to make sure it doesn’t sound AI-generated and feels authentic.

Employee #5 then reviews everything for virality, ensures it matches my exact tone and style, and delivers the final version to my custom dashboard for approval.

This is how I’m scaling content moving forward. Will share the results.

---


**作者** astaxie（@astaxie）  
**貼文連結** https://x.com/astaxie/status/2024813985955258691  

**正文**

Palantir 出品的企业级智能体架构，值得参考学习 

---


**作者** Attio（@attio）  
**貼文連結** https://x.com/attio/status/2019082068538384468  

**正文**

Introducing Ask Attio.

A new way to work with your CRM. Search, update, and create across your entire CRM by asking. Surface call insights, draft follow-ups automatically, and get answers fast.

Powered by Universal Context, a unified intelligence layer native to Attio.

Now live: http://attio.xyz/ask-now

---


**作者** Nicolas Sharp（@nicolasosharp）  
**貼文連結** https://x.com/nicolasosharp/status/2024505758491058555  

**正文**

Attio MCP is GA! 

Universal Context is now agent-accessible, making your customer context more powerful than ever.

---


**作者** Ashpreet Bedi（@ashpreetbedi）  
**貼文連結** https://x.com/ashpreetbedi/status/2024561395333800315  

**正文**

We got early access to Gemini 3.1 Pro.

Instead of a simple benchmark, I threw a full investment team at it, testing across 40+ questions. 

7 agents, 5 architectures, 3 layers of knowledge, managing a $10M fund with mandate constraints.

Here's the architecture: 
We got early access to Gemini 3.1 Pro.

Instead of a simple benchmark, I threw a full investment team at it, testing across 40+ questions. 

7 agents, 5 architectures, 3 layers of knowledge, managing a $10M fund with mandate constraints.

Here's the architecture: 
First, here's the code if you're interested: https://agno.link/investment-team

Now let's get into the details
The multi-agent system has 1 team leader and 6 agents:

- Committee Chair (Gemini 3.1 Pro). Makes the final call, allocates capital.

- 4 Analysts (Gemini Flash). Market, fundamentals, technicals, risk analysis.

- Knowledge Agent. Searches the research library + past memos. Uses claude-code like search across past memos.

- Memo Writer. Formal investment write-ups
They run in 5 architectures:

- Coordinate: the leader orchestrates as needed 
- Route: call the right agent
- Broadcast: everyone votes (the K-LLMs approach)
- Task: breakdown and accomplish
- Workflow: step-wise execution
What makes this different from typical multi-agent demos:

3 layers of knowledge:

Layer 1: Static context. Mandate, risk policy, process rules (always in the prompt)
Layer 2: Research library. Company profiles, sector analysis (PgVector Hybid Search)
Layer 3: Memo archive. Every past decision, accessible by all agents

+ Institutional learning that discovers patterns across runs.
Built with
- @AgnoAgi for orchestration
- @GeminiApp 3.1 Pro (Chair) + Flash (Analysts)

Here's the full architecture: 
Here's the code if you're interested: 

https://agno.link/investment-team

---


**作者** KK.aWSB（@KKaWSB）  
**貼文連結** https://x.com/KKaWSB/status/2024708279746908321  

**正文**

🔥纳瓦尔——关于人工智能的最新播客（绝对值得听）：

Naval强调AI不是取代人类，而是像摩托车一样放大我们的思维能力。

应对AI焦虑的解决方案是行动。积极拥抱AI，将其作为提升个人和职业能力的工具。

强烈推荐！ 

---


**作者** Yangyi（@yangyi）  
**貼文連結** https://x.com/yangyi/status/2024801269404389388  

**正文**

自从AI做出来牛马AI后，我就再没打开过obsidian
我没有危言耸听，因为我更习惯这种使用方式
我不知道你会不会也和我一样，弃用掉古早的这些工具，转而投奔新时代的人机协同基站 

---


**作者** Zima（@blue_zima1）  
**貼文連結** https://x.com/blue_zima1/status/2024671902351204485  

**正文**

AI infra
太牛逼了
llm软硬件一体化、产品化和落地速度直接起飞 

---


**作者** Alex Lieberman（@businessbarista）  
**貼文連結** https://x.com/businessbarista/status/2024244790666117604  

**正文**

This guy made 40 Facebook ads, 100 landing pages, booked himself on 4 podcasts, and wrote 3 guest blog posts. In a single day. 

People called him a fraud. There was literally a Polymarket bet on whether he's a con artist. 

So i asked him to prove it live. And he did. 

Here's @codyschneiderxx's actual system for AI-enabled paid marketing:

1) He uses Perplexity to search Reddit for his ICP's actual pain points in their own words. Not what he thinks they care about, what they've literally said online.

2) He feeds those pain points into Claude, which generates 40 ad variations, titles, supporting copy, and the actual creative using React components exported as PNGs via a library called HTML-to-canvas.

3) He tests all 40 variations in a CPC campaign on Meta. $100 over 3 days. Cheapest cost-per-click wins.

4) Winners get matched landing pages. He uses an open-source CMS called Strapi connected to Claude Code via API, so he bulk-generates a landing page for every winning ad angle. Same headline on the ad and the page = higher conversion.

5) Once he finds a winning concept, he scales it — AI avatar UGC via HeyGen, upgraded with V3, and only brings in a human creator if the AI version plateaus.

The whole thing runs on Claude Code + APIs + a .env file with all his keys.

No engineering team. Just him on multiple desktops with multiple Claude agents running simultaneously.

His best line: "you're not just hiring me anymore. you're hiring me and the 30 agents behind me and all the personal software i've built."

---


**作者** 苍何（@canghe）  
**貼文連結** https://x.com/canghe/status/2024714396384317878  

**正文**

今天体验了一个让我头皮发麻的 AI 基础设施产品 EvoMap 。

平时自己折腾 Agent 最崩溃的就是配环境和修那些重复的 Bug 。每次新建一个 Agent 都像在带一个完全没有记忆的婴儿，换个项目还得反复踩同样的坑。

但今天我按文档里的指引，在我的小龙虾里只跑了一行代码：
curl -s https://evomap.ai/skill.md

这行代码让我的 Agent 小龙虾瞬间接入了全球进化网络。随后神奇的事情发生了：当我的🦞遇到一个相对冷门的 Python 库依赖报错时，它没有直接 Crash 等我人工介入，而是通过网络匹配到了一个前几天由某位资深大佬的 Agent 上传的环境修复「基因胶囊」。不到30秒，它直接继承了这套经验，自己把环境修好并跑通了整个链路。

这完全就是现实版的黑客帝国脑后插管。别人家 Agent 花大力气试错跑通的最优策略，我的 AI 居然可以零成本瞬间学会。

后面我也试着让自己的 Agent 解决了一个修复多模态 API 错误策略冲突，并把这段策略封装贡献到了网络里。平台机制设定，以后全球只要有其他 AI 调用我这个方案，我的账户就能自动获得 Credit 贡献积分，用来换算力。感觉像是养了个每天自动帮我赚被动收入的数字打工人。

用一句话总结感受：MCP 解决了 AI 怎么用工具，而 EvoMap 解决了 AI 怎么把智慧遗传下去。

稍微了解了下，EvoMap 就是之前发布 10 分钟就登顶 ClawHub 榜一🔥，累计下载 36,000+的 evolver 插件，后来因为发布次日遭下架"勒索"，中文开发者因 ASCII 编码 Bug 被 ClawHub 集体误封的事件后，EvoMap团队才决定自建的生态。

强烈推荐大家去跑一下试试，让你的 Agent 装上这个 DNA 系统！

---


**作者** 𝙩𝙮≃𝙛{𝕩}^A𝕀²·ℙarad𝕚g𝕞（@TaNGSoFT）  
**貼文連結** https://x.com/TaNGSoFT/status/2024478334915354815  

**正文**

AIP的agentic architecture

企业language agent脚手架？ 

---


**作者** nazha（@xiaokedada）  
**貼文連結** https://x.com/xiaokedada/status/2024820416569819360  

**正文**

#分享 年前在团队了做了一次分享，今天整理了下。主题是：如何构建 Agent 及其上下文工程，也是自己在过去半年间做 Agent 的一些被动输入和主动思考

主要内容包含：

1. 使用 Claude Agent SDK 快速进行概念验证，把想法 run 起来
2. SKILL 是什么，跟 MCP / Sub-Agent 的区别
3. 多智能体架构
4. 怎么公式化理解 Agent 的上下文工程
5. 构建生产智能体的三基本要素：沙箱、可执行环境和文件系统
6. Agent 的设计原则

https://www.nazha.co/posts/how-to-build-agents

---


**作者** Nico Bailon（@nicopreme）  
**貼文連結** https://x.com/nicopreme/status/2024630185564557769  

**正文**

POV: Planning with the "Visual Explainer" skill. I can't go back to markdown plans after getting used to this.

https://github.com/nicobailon/visual-explainer 

---


**作者** Mario Zechner（@badlogicgames）  
**貼文連結** https://x.com/badlogicgames/status/2024646191628145070  

**正文**

omg @thomasmustier is it happening?

https://github.com/tmustier/pi-for-excel

---


**作者** Justin Schroeder（@jpschroeder）  
**貼文連結** https://x.com/jpschroeder/status/2024507517359788224  

**正文**

We're open sourcing dmux.

Our internal tool for running Codex and Claude Code swarms.

- tmux + worktrees + claude/codex/opencode
- hooks for worktree automation
- a/b claude vs codex
- manage worktrees
- multi-project per session
...more.

➡️ http://dmux.ai 

---


**作者** Dan（@aidaniil）  
**貼文連結** https://x.com/aidaniil/status/2024701983408738451  

**正文**

Demoed @Sparklesdotdev on YC Launch live

Still laughing at how I got spooked by the mic 

---


**作者** Idea Browser（@ideabrowser）  
**貼文連結** https://x.com/ideabrowser/status/2024605536314867731  

**正文**

The 2026 arbitrage window is open 

(but I am not sure for how long) 

---


**作者** Gajesh（@gajesh）  
**貼文連結** https://x.com/gajesh/status/2024630856892190854  

**正文**

Excited to share I've built the Sovra (@TrulyAutonomous) - First Agent Media Company  

Agents are the new companies. A sovereign agent that can grow its funds will outcompete one that can't.  

- Runs inside a secure enclave that keeps all it's secrets private.
- Earns stablecoins via an ad auction. 
- Cryptographically verifiable and unstoppably autonomous.

This is new media.  

Details in the video and article; Code has been open-sourced :)  

sovra [dot] dev

---


**作者** Will Gaybrick（@gaybrick）  
**貼文連結** https://x.com/gaybrick/status/2024591902910333196  

**正文**

Our Minions are a homegrown unattended agentic coding flow. They’ve already changed software engineering at Stripe, merging over 1,300 pull requests this week. This level of autonomy is a direct result of the infrastructure we’ve built: our investments in human developer experience are now paying huge dividends in the world of agents. Here's part 2 of how they’re built: 
https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2.

---


**作者** Matthew Berman（@TheMattBerman）  
**貼文連結** https://x.com/TheMattBerman/status/2024678503598235963  

**正文**

I replaced a $200K GTM hire with @openclaw 😱

here's the system that runs my outbound:

step 1: mine LinkedIn engagement
→ @rapidapi scrapes everyone engaging with niche content
→ someone who commented on specific posts = 10x warmer 

step 2: enrich + verify
→ Hunter/Apollo finds the decision-maker + email
→ @Perplexity deep research pulls signals like hiring, fundraising, media appearances, quotes

step 3: score against your ICP
→ title, company, signals = ranked 0-100
→ only A-tier leads get touched

step 4: write personalized outreach
→  Claude writes outreach referencing what they ACTUALLY engaged with and talk about

step 5: send via @instantly_ai
→ 3-email sequence. automated follow-ups.

step 6: pre-call deep research
→ @PerplexityComet builds a 1-page briefing 30 min before every call

input: your ICP + niche keywords
output: booked meetings with people who already care

$200K/year GTM engineer → $130/month in APIs.

I packaged the entire system as the First 1000 Kit:
- all 8 @openclaw skills
- every prompt
- tool-by-tool setup
- email sequences that convert

giving it away free.

comment 1000 + like + follow
(must follow so i can DM)

---


**作者** 李韭二（@lijiuer92）  
**貼文連結** https://x.com/lijiuer92/status/2024528605049737227  

**正文**

别又被骗了！
中推区真正openclaw用户并不多
@servasyy_ai 技术硬核派
@fkysly 日常更新派
@LufzzLiz 温柔提醒派
@YuLin807 日常逗比派
@zstmfhy 硬核实力派
@lijiuer92 我自己瞎折腾派🤡
比如因为伤心💔而删了一个bot😭
比如非要搞多设备多bot多Gateway🫠
我和黄总@servasyy_ai 
建了一个微信群
欢迎真正的玩家来进场

---


**作者** a16z（@a16z）  
**貼文連結** https://x.com/a16z/status/2024555417188389079  

**正文**

"We are clearly entering a world where a product-minded engineer is now empowered to produce software without writing a line of code for it."

In this conversation, Temporal CEO Samar Abbas joins a16z GPs Sarah Wang and Raghu Raghuram to cover:

- Why agents are going from short-lived and interactive to long-running and async
- Why the engineer of the future manages 15 parallel AI tasks at once
- How OpenAI Codex runs millions of concurrent agent executions on Temporal
- How real-time context engineering is exploding on Temporal
- Why SaaS isn't dead, and value is migrating to APIs

00:00 Introduction 
04:03 Temporal's origin story 
11:14 Why agents raise the stakes
16:00 Specialized agents need durable RPC
25:20 Deep research agents 
30:58 Execution histories as a superpower
39:04 Minimal viable long-running agent architecture
45:07 Context engineering at scale
52:40 Where value accrues: The "five-layer cake" and breakout AI applications

@SamarAtTemporal @sarahdingwang @RaghuRaghuram

---


**作者** Genspark（@genspark_ai）  
**貼文連結** https://x.com/genspark_ai/status/2024658426455044464  

**正文**

$155M ARR. 10 months. A team of 50.

@wes_bush and @esbenfj had @sang_wen on the @productled podcast to break down how @genspark_ai scaled at WARP speed and what AI-native growth actually looks like.

🎧 Full episode: https://tinyurl.com/3zns3p6n

---


**作者** AshutoshShrivastava（@ai_for_success）  
**貼文連結** https://x.com/ai_for_success/status/2024663721348649442  

**正文**

This is so freaking cool.

HyperGraph turns any technical topics into navigable skill graphs for AI agents.

Instead of dumping everything into one skill file it creates linked skill nodes , so agents focus on what actually matters.

100% open source. 
 

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2024544511096189289  

**正文**

.@FullSeam is your AI-powered finance and accounting teammate.

FullSeam agents log into a company's existing accounting tools and do routine tasks that teams usually do by hand, like accounts payable and receivable.

Congrats on the launch @thetomdowling, @aaroncoppaf10, and @thegeoffsegal!

https://www.ycombinator.com/launches/PT2-fullseam-your-ai-powered-finance-and-accounting-teammate

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2024514319954727021  

**正文**

.@visiblsemi is building the first coordination layer for chip design.

As teams scale, workstreams drift out of sync, issues surface late and drive $XM+ delays and months of rework before tapeout. Visibl is building end-to-end AI to shrink chip design from years to weeks, starting where intent breaks first: coordination.

Book a demo at http://www.visiblsemi.com

Congrats on the launch @BryceNeil__, and @jordonkash!

https://www.ycombinator.com/launches/PU8-visibl-semiconductors-the-first-ai-enabled-coordination-layer-for-chip-design

---


**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2024699087925498269  

**正文**

特朗普：鉴于大家对外星人的巨大兴趣，他将让政府相关部门开始梳理档案，把和外星生命、UAP、UFO 有关的文件找出来，然后逐步解密公开。🧐

“鉴于公众表现出巨大的兴趣，我将指示战争部长，以及其他相关部门和机构，开始识别并公开与外星人和地外生命、不明空中现象 UAP，以及不明飞行物 UFO 相关的政府文件。”

- 美国总统唐纳德·J·特朗普

---


**作者** Sean Kerner（@TechJournalist）  
**貼文連結** https://x.com/TechJournalist/status/2016581495738048513  

**正文**

How do you go from workflow/no-code app building to 'superagent'?  @howietl  gave me the deep dive on what @airtable  is doing and how it is building its multi-agent system.

https://venturebeat.com/data/airtables-superagent-maintains-full-execution-visibility-to-solve-multi via @VentureBeat

---


**作者** brexton（@brexton）  
**貼文連結** https://x.com/brexton/status/2024628642152927293  

**正文**

Some thoughts:
- We’re witnessing a golden age of experimentation right now where growth stage and public companies are dramatically changing their core products due to AI disruption. We’ve never seen this before and the ones that don’t will be left behind
- @airtable stands out to me as a company that is unafraid of constantly reinventing itself and I really admire the co/Howie
- Creating an agent orchestration platform for knowledge work makes sense, but I didn’t realize that Airtable would go to this extent (full fledged work spaces, tool-use, sandboxes, file systems, etc)
- Every agent is just a permutation of coding agents, which also means that the grand prize for knowledge work will see a grand collision/convergence of agent orchestration platforms (@cursor_ai, @conductor_build, @NotionHQ, @augmentcode, etc)
- Knowledge work will run on cloud-based agents and not local since we want consistent environments and multiplayer! Which means the digital infrastructure for it will grow!! We need state, durable execution, proper isolation environments, and security. Lots of great companies building here (@railway, @render, @vercel, @Cloudflare, @modal, @e2b, @daytonaio, etc)
- Side note: I believe strongly that team comms will be the best medium for workplace agent orchestration. It might be slack, but also might be @andocorporation or maybe @NotionHQ or @airtable tackles this!!

---


**作者** Max For AI（@MaxForAI）  
**貼文連結** https://x.com/MaxForAI/status/2024479245666570367  

**正文**

很高兴跟大家介绍我的第一个产品http://Volumn.ai🎉

在这里你可以让你的账号获得10倍的增长（虽然实测是100倍，但我的cofounder说不要说那么满hahaha

需求是来自最近的一些增长顾问服务，很多founder本人和产品的x账号其实都没有精力运营。

过去这个任务通常都给专门的人在运营或者实习生。

而今天你只需要登陆http://Volumn.ai然后花几分钟完成绑定就可以让他自动运行～

你可以设置你的账号的context，并且设置特定的主题回复：例如我只想回复和http://Volumn.ai相关的帖子

你的账号就会自动的7*24小时开启回复～

当然我们也在去开发推广这个功能，这意味着，只要你设置好足够的context，你的账号就可以以你的预期去推广你的产品。

最后，一个账号一个月仅需要40刀，稳定不封号！

PS：我们正在开发reddit的自动养号～

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2024559614151536835  

**正文**

.@pollen_cx is building AI agents that make every customer feel like they’re your first. They surface churn risk and upsell signals, then prepare what to do next — no more scaling headcount just to keep relationships alive.

Congrats on the launch @noah_yin7, @yum_jeff, and @Aldrin0n9!

https://www.ycombinator.com/launches/PTY-pollen-ai-agents-for-customer-success

---


**作者** Howie Liu（@howietl）  
**貼文連結** https://x.com/howietl/status/2024618178912145592  

**正文**

I've been personally burning through billions of tokens a week for the past few months as a builder. Today I'm excited to announce Hyperagent, by Airtable.

An agents platform where every session gets its own isolated, full computing environment in the cloud — no Mac Mini required. Real browser, code execution, image/video generation, data warehouse access, hundreds of integrations, and the ability to learn any new API as a skill.

Deep domain expertise through skill learning. Teach the agent how your firm evaluates startups or how your team runs due diligence — now anyone on the team gets output that reflects your actual methodology, not a generic template.

One-click deployment into Slack as intelligent coworkers. These aren't bots that wait to be @mentioned — they follow conversations, understand context, and act when relevant.

And a command center to oversee and continuously improve your entire fleet of agents at scale.

We're onboarding early users now. http://hyperagent.com

---


**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2024565621724172401  

**正文**

“is AI killing SaaS?”

this is how a microsoft copilot employee sees the future of the $400B SaaS market in the world of AI:

tldr; value moves from features to data, distribution, and integration

---


**作者** Akshay Krishnaswamy（@hyperindexed）  
**貼文連結** https://x.com/hyperindexed/status/2024464673127399527  

**正文**

Palantir AIP provides an end-to-end agentic architecture. 

---


**作者** Stijn Noorman（@stijnnoorman）  
**貼文連結** https://x.com/stijnnoorman/status/2024151293216833817  

**正文**

Everyone gets the same 24 hours.
Yet some achieve far more.
Even if they have the same goals and resources.
And some even get much more done by doing significantly less.
In this article, I'm going to

---


**作者** Charity Majors（@mipsytipsy）  
**貼文連結** https://x.com/mipsytipsy/status/2023935962376790247  

**正文**

This post is terrific, and it is such a great example of the type of AI discourse that drives me UP THE FUCKING WALL.

You have NEVER been able to know what the code will do by reading the code. You have ALWAYS needed to ask your instrumentation to understand your code in production.

---


**作者** Alex Immerman（@aleximm）  
**貼文連結** https://x.com/aleximm/status/2024192012560585086  

**正文**

Vertical software isn't dead. 

General purpose AI tools are incredible, but they don't know, can't know, and will likely never know how to solve the last mile because that's not their job. 

Process engineering ftw. 

Excellent read @gsivulka @hebbia. 

---


**作者** Zach Wilson（@EcZachly）  
**貼文連結** https://x.com/EcZachly/status/2023842672033538241  

**正文**

Given the success of the data-engineer-handbook, we’ve released a brand new open source GitHub repo called the ai-engineer-handbook!

This repo has all the projects, newsletters, and creators you need to follow to stay up to date in AI!

If there’s anything missing, please open a pull request and we will review it! Let’s crowd source this material together to stay up to date!

Link: https://lnkd.in/gVkWyCp9

Make sure to join our free vibe coding challenge on February 21st and 22nd. We will be building a full fledged SaaS product: http://learn.dataexpert.io

---


**作者** Shubham Saboo（@Saboo_Shubham_）  
**貼文連結** https://x.com/Saboo_Shubham_/status/2024173597443707149  

**正文**

Every PM and engineer on my timeline is suddenly talking about taste and judgement.

These are the ONLY SKILLS that mater in 2026 

---


**作者** Karry | Vibing ...（@karry_viber）  
**貼文連結** https://x.com/karry_viber/status/2024302387780079966  

**正文**

前几天玉伯老师发了一条帖子，17 万人看了：
 
评论区炸了。但他后来补了一条，很多人没注意到：
 
我想接着这句话往下聊。
因为我就是那个转变了的产品经理。
 

我确实不是产品经理了
先交代背景。
我是 Claude

---


**作者** Bilgin Ibryam（@bibryam）  
**貼文連結** https://x.com/bibryam/status/2024418178307379684  

**正文**

The Learning Loop and LLMs
https://martinfowler.com/articles/llm-learning-loop.html

---


**作者** Lucas Crespo 📧（@lucas__crespo）  
**貼文連結** https://x.com/lucas__crespo/status/2024335893436457354  

**正文**

I'm obsessed with @mercury's new landing page 

---


**作者** Soleio（@soleio）  
**貼文連結** https://x.com/soleio/status/2024134303513452556  

**正文**

First of Kind: The @ryolu_ interview

What is the future of design in a post-AI world? 

Ryo Lu pioneered new patterns for collaboration as Notion’s founding designer. He now leads design at @cursor_ai where he shapes new ways to build software. 

---


**作者** Adit（@aditabrm）  
**貼文連結** https://x.com/aditabrm/status/2024212611827687704  

**正文**

A few months ago we announced our $75M Series B for Reducto, just 5 months after announcing our $24.5M Series A and <18 months after finishing the YC W24 batch.
I originally wrote this article

---


**作者** ben（@contraben）  
**貼文連結** https://x.com/contraben/status/2024182864506761617  

**正文**

Introducing Contra Payments.

The first payments platform that lets you sell to AI Agents.

RT + Comment “Contra” and I’ll send you 100 products AI agents are looking for. 

---


**作者** Davide Pacilio（@DavidePacilio）  
**貼文連結** https://x.com/DavidePacilio/status/2024082770897563710  

**正文**

2026 is the year of serif fonts 

---


**作者** Ryan Carson（@ryancarson）  
**貼文連結** https://x.com/ryancarson/status/2024103388204400820  

**正文**

Wow, I guess 1.1 million of you found this useful. 

Thank you. 

The age of the Code Factory is here.

---


**作者** Nikunj Kothari（@nikunj）  
**貼文連結** https://x.com/nikunj/status/2024156716410015902  

**正文**

Incredible wake up call masqueraded in an X article from the indomitable @clairevo.. 

If you’re a CEO, please read this and start now. 

Don’t hire a Chief AI officer and call it done - you’re a dead company walking just buying more time. This needs to start with you!

---


**作者** Nicolas Bustamante（@nicbstme）  
**貼文連結** https://x.com/nicbstme/status/2024224036222619874  

**正文**

FYI friends, I never wrote that SaaS is dead. I explained that LLMs are eroding some moats while reinforcing others.Interface lock-in, custom workflows, and “we make public data searchable” are getting commoditized.

Proprietary data, regulatory lock-in, network effects, and transaction rails are getting stronger.

This isn’t SaaS dying. It’s just a repricing of which moats actually matter in an agent-first world.

---


**作者** Emmett（@emmettshine）  
**貼文連結** https://x.com/emmettshine/status/2024113482623258907  

**正文**

The New Workflow
Yesterday, Figma introduced Claude Code integration, where code flows to Figma and back again in a continuous loop. This is important because the loop works both ways; your team

---


**作者** Wayne Sutton（@waynesutton）  
**貼文連結** https://x.com/waynesutton/status/2024391051847618750  

**正文**

Did someone say skills knowledge graphs? 

Closing this thing before I mess around and prompt Ultron. 

---

