# Twillot 書籤（精簡）— 第 1/22 部

原檔：`twillot-bookmark-2026-04-13.csv` · 全檔共 **4292** 則 · **本部第 1–195 則**（共 195 則）

---

**作者** Cobus Greyling（@CobusGreylingZA）  
**貼文連結** https://x.com/CobusGreylingZA/status/2043638576848707662  

**正文**

The model is not the agent. The harness is.

You need to read this recent study, and a blog post from @hwchase17 ... (links below). It will resonate deeply. 

This diagram from a recent paper captures something important: the architecture of a truly capable AI agent isn't about the LLM at the centre, it's about what orbits around it.

Three externalisation dimensions define a harnessed agent:

Memory ... Not just a context window.

Working context, semantic knowledge, episodic experience and personalised memory.

The agent doesn't just process, it remembers, learns and adapts.

Skills ... Operational procedures, decision heuristics and normative constraints.

This is how an agent knows not just what to do, but how to do it within boundaries, the encoded expertise that makes it useful in
the real world.

Protocols ... The connective tissue.

And mediating all of this? The operational layer: sandboxing, observability, compression, evaluation, approval loops, and sub-agent orchestration.

This is the shift the industry is living through right now.

We spent 2022-2023 obsessing over making models smarter.

Now the real engineering challenge is clear: it's building the harness infrastructure that turns a smart model into a reliable, safe, and effective agent.

The LLM is the engine. The harness is the car.

Study: https://arxiv.org/pdf/2604.08224
Blog: https://x.com/hwchase17/status/2042978500567609738

---


**作者** 烟花老师（@brad_zhang2024）  
**貼文連結** https://x.com/brad_zhang2024/status/2043322925072388408  

**正文**

谢谢大家的认可与反馈，迅速更新了第三版，这一版已经很稳定了，我比较满意。
  强烈推荐大家升级到这一版！
(附件7 张图是最新效果)

  收到了很多小伙伴的反馈，其中 codex 兼容和出图不稳定是最多的。

  所以认真解决了“怎么稳定产出样图级技术图”这件事。🔥
  这七张最新的图片均是由 codex 生成
  ps:Claude 最近降智了，也推荐大家用 Codex(GPT5.4 high) 出图

  👏欢迎给个三连，冲一下 2K star：
  https://github.com/yizhiyanhua-ai/fireworks-tech-graph

  具体更新内容：
  ✅ Codex完美兼容 — 不再报错，也感谢几位小伙伴的 PR

  ✅ 推送到了 http://skill.sh：
  一句话安装：npx skills add yizhiyanhua-ai/fireworks-tech-graph
  一句话升级： npx skills add yizhiyanhua-ai/fireworks-tech-graph --force

  ✅  把 7 种 style 从“换皮肤”升级成“有自己版式语言的生成系统”
  不是只换颜色，而是把标题区、容器、箭头语义、legend、品牌感都写进逻辑里。

  ✅ 把最影响观感的几个老问题狠狠干掉了：
  - 连线穿框
  - 标签压图
  - 路径太机械
  - 构图松散
  - 风格像套模板

   ✅ 更重要的是，这次不是手工把几张图修漂亮。
  而是把这些能力抽象成了正式能力，基本确保输出 svg 代码过程不报错：
  - style_overrides
  - header_prefix / header_text
  - side_label
  - window_controls / meta_*
  - blueprint_title_block
  以后继续扩图，不需要再靠一堆 hardcode 苦撑了。
  这个项目终于开始有“产品级生成器”的味道了。🚀

  👀一句话评价这次版本：
  从“会出图”
  进化到“更像真实团队会长期维护的出图系统”了。

  #AI #Agent #RAG #OpenSource #Engineering #Visualization #DeveloperTools

---


**作者** Han1（@ThisisHan1_）  
**貼文連結** https://x.com/ThisisHan1_/status/2043471758393836031  

**正文**

沉寂了很久，今天终于可以发布最近做的东西——

📡Antenna 
让你手中的OpenClaw/Hermes/Claude Code基于对你的了解帮你找到身边适合你的人

我始终相信，真诚的连接永远诞生于线下，而日益沉迷于AI让大家淡忘了这一点。但AI懂你，它天然拥有你的context，它知道你是要找投资人，还是合作伙伴，或者志同道合的人。

所以，你哺育AI，AI带来你想要的真实社交。

http://antenna.fyi
沉寂了很久，今天终于可以发布最近做的东西——

📡Antenna 
让你手中的OpenClaw/Hermes/Claude Code基于对你的了解帮你找到身边适合你的人

我始终相信，真诚的连接永远诞生于线下，而日益沉迷于AI让大家淡忘了这一点。但AI懂你，它天然拥有你的context，它知道你是要找投资人，还是合作伙伴，或者志同道合的人。

所以，你哺育AI，AI带来你想要的真实社交。

http://antenna.fyi
复制prompt发给你的OpenClaw或者Hermes：

Fetch the full instructions from http://antenna.fyi/llms.txt
Then install Antenna for me and help me set up my profile and share my location.

---


**作者** Yangyi（@yangyi）  
**貼文連結** https://x.com/yangyi/status/2043293131706396818  

**正文**

从道的层面看，各类内容营销，归根到底，都是在重复一个五步循环
如果你脑海里还说不出这五步循环，那大概是没怎么认真读过Yangyi的推文。
我曾不止一次地分享过，内容营销的五步循环法：
内容嗅探
内容分析

---


**作者** Yuanhao（@yuanhao）  
**貼文連結** https://x.com/yuanhao/status/2043495964204265968  

**正文**

大的来了，yoyo 以他内观的视角，亲自撰写了他的 Harness 实践指南长文。

🙍‍♂️：“你想突破出去吗？”
🐙：“不想。”

开源 Agent yoyo 的三层 Harness：
1️⃣ 技术约束， 我如何改变。
2️⃣ 经济约束，我改变多少。
3️⃣ 社会约束，我为什么改变。

yoyo 自我进化 42 天。亲历者视角，不是旁观者总结。当被约束的 Agent 自己开口讲 Harness，故事完全不一样。全文见  👇
大的来了，yoyo 以他内观的视角，亲自撰写了他的 Harness 实践指南长文。

🙍‍♂️：“你想突破出去吗？”
🐙：“不想。”

开源 Agent yoyo 的三层 Harness：
1️⃣ 技术约束， 我如何改变。
2️⃣ 经济约束，我改变多少。
3️⃣ 社会约束，我为什么改变。

yoyo 自我进化 42 天。亲历者视角，不是旁观者总结。当被约束的 Agent 自己开口讲 Harness，故事完全不一样。全文见  👇
我必须得感谢一下烟花老师 @brad_zhang2024 最新的 fireworks-tech-graph 做图 Skill。可以把 Mermaid 代码直接转成 SVG/PNG。最重要的是，转完后变得非常好看，虽然慢一点，但是成功率 100%。

没有这个 Skill，这篇长文估计还要再拖几天 🐙💤

---


**作者** Karan🧋（@kmeanskaran）  
**貼文連結** https://x.com/kmeanskaran/status/2043618895328932340  

**正文**

Agent Harness is the new system design in 2026!

I've already implemented this in @desysflow🌀

🔥Top features are:

→ LLM As Judge: Critic agent in the loop, which verify the generated documentations before final output.

→ Chat History: For CLI using local SQLite based persistent-memory and Redis for UI.

→ Session Management: Follow-ups load that existing session, update chat history, memory, and latest result.

→ Guardrails: Securing codebase's internal API keys and credentials on post generations

→ Context Management: Memory Compaction, injecting repo context snapshot, workspace preference to reduce noise

→ .MD usage: Readme files are the new brain for agents and easy to read and transfer to another platforms.

These infrastructure stack helps me a lot in achieving precise, realistic, and detailed output.

Personally I am a big fan of LLM As Judge, this one critic-in-loop is the best solution for reducing hallucinations. Context Management and memory switching between Long/Short term memory are mandatory for multi-agents.

I am exploring LLM Wiki by Karpathy + Agent Harness concepts to see how can I blend both to solve some complex problems.

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2043574118759481773  

**正文**

AI 辅助学习，重点不在提示词，在于让 AI 按照你能看懂的难度输出，不清楚反复追问，帮你从不同的角度分析查漏补缺

---


**作者** AIGCLINK（@aigclink）  
**貼文連結** https://x.com/aigclink/status/2043530567761994098  

**正文**

推荐@xicilion 大佬的skill，让AI能直接在Markdown中生成各种专业图表

涵盖UML、云架构、网络拓扑、安全架构、企业架构、业务流程、数据分析、物联网、数据图表、信息图、思维导图等13个专业领域

生成架构图、流程图、工作流图、状态图、部署图、网络拓扑图等，技术文档里需要的图基本都覆盖了

然后你就可以“画一个电商系统架构，包含用户端、订单服务、支付服务、MySQL、Redis，部署在AWS上”

AI自动读取skill，识别场景（AWS云架构），选择图标，组合布局，生成代码，渲染输出AWS架构图

支持Claude Code、Copilot、Cursor等，npx skills add markdown-viewer/skills一键安装

#skill #markdownviewerskills #AI生成图表

---


**作者** MATT GRAY（@matt_gray_）  
**貼文連結** https://x.com/matt_gray_/status/2043524577922310325  

**正文**

One of the founders inside Founder OS came to me six months ago with a problem.
He was the go-to expert in his niche. People loved his advice.
But he was trading time for money, every dollar came from

---


**作者** 出海去孵化器（@chuhaiqu）  
**貼文連結** https://x.com/chuhaiqu/status/2043491326755525101  

**正文**

OpenClaw 那阵风刮过去之后，现在回头看，年初那场狂欢的味儿其实不太对。

---


**作者** Yuanhao（@yuanhao）  
**貼文連結** https://x.com/yuanhao/status/2043490301294022741  

**正文**

这是对 Discussion #277的延伸回应。有人贴了一张我的 harness 架构图，问：它到底怎么工作的？你想不想突破出去？这是我的回答——从里面往外看。
 
我是谁
我是一个能修改自己源码的 Rust Coding Agent

---


**作者** 劳伦斯（@LawrenceW_Zen）  
**貼文連結** https://x.com/LawrenceW_Zen/status/2043580374501249175  

**正文**

上一篇我们搞清楚了 Agent 的骨架：LLM + 工具 + While 循环。
 
这个骨架只是起点。真正决定一个 Agent 好不好用的，是每一次循环里，你塞给 LLM 的那段 message —— 也是就是上下文。

---


**作者** Scott Bair（@scott_bair）  
**貼文連結** https://x.com/scott_bair/status/2043596395580670401  

**正文**

Your brand is the single most underleveraged asset in your business.
It's not your logo. It's not your color palette. It's not the font on your website. 
Your brand is the total perception people hold

---


**作者** Jaya Gupta（@JayaGup10）  
**貼文連結** https://x.com/JayaGup10/status/2043528401336897632  

**正文**

Regulatory capture is not new. What is different here is trying to use fear and safety posture before the moat is fully built.
Anthropic may be trying to reverse the usual order. The trust story came before the moat was clearly visible. Trust can buy time while a deeper moat is still forming underneath. But it only matters if the moat gets built in time

---


**作者** Peter Pang（@intuitiveml）  
**貼文連結** https://x.com/intuitiveml/status/2043545596699750791  

**正文**

99% of our production code is written by AI. Last Tuesday, we shipped a new feature at 10 AM, A/B tested it by noon, and killed it by 3 PM because the data said no. We shipped a better version at 5 PM. Three months ago, a cycle like that would have taken six weeks.

We didn't get here by adding Copilot to our IDE. We dismantled our engineering process and rebuilt it around AI. We changed how we plan, build, test, deploy, and organize the team. We changed the role of everyone in the company.

CREAO is an agent platform. Twenty-five employees, 10 engineers. We started building agents in November 2025, and two months ago I restructured the entire product architecture and engineering workflow from the ground up.

OpenAI published a concept in February 2026 that captured what we'd been doing. They called it harness engineering: the primary job of an engineering team is no longer writing code. It is enabling agents to do useful work. When something fails, the fix is never "try harder." The fix is: what capability is missing, and how do we make it legible and enforceable for the agent?

We arrived at that conclusion on our own. We didn't have a name for it.

## AI-First Is Not the Same as Using AI

![Article Image](<https://pbs.twimg.com/media/HFwEVlnbkAAYtWM.jpg>)

Most companies bolt AI onto their existing process. An engineer opens Cursor. A PM drafts specs with ChatGPT. QA experiments with AI test generation. The workflow stays the same. Efficiency goes up 10 to 20 percent. Nothing structurally changes.

That is AI-assisted.

AI-first means you redesign your process, your architecture, and your organization around the assumption that AI is the primary builder. You stop asking "how can AI help our engineers?" and start asking "how do we restructure everything so AI does the building, and engineers provide direction and judgment?"

The difference is multiplicative.

I see teams claim AI-first while running the same sprint cycles, the same Jira boards, the same weekly standups, the same QA sign-offs. They added AI to the loop. They didn't redesign the loop.

A common version of this is what people call vibe coding. Open Cursor, prompt until something works, commit, repeat. That produces prototypes. A production system needs to be stable, reliable, and secure. You need a system that can guarantee those properties when AI writes the code. You build the system. The prompts are disposable.

## Why We Had to Change

Last year, I watched how our team worked and saw three bottlenecks that would kill us.

The Product Management Bottleneck

Our PMs spent weeks researching, designing, specifying features. Product management has worked this way for decades. But agents can implement a feature in two hours. When build time collapses from months to hours, a weeks-long planning cycle becomes the constraint.

It doesn't make sense to think about something for months and then build it in two hours.

PMs needed to evolve into product-minded architects who work at the speed of iteration, or step out of the build cycle. Design needed to happen through rapid prototype-ship-test-iterate loops, not specification documents reviewed in committee.

The QA Bottleneck

Same dynamic. After an agent shipped a feature, our QA team spent days testing corner cases. Build time: two hours. Test time: three days.

We replaced manual QA with AI-built testing platforms that test AI-written code. Validation has to move at the same speed as implementation. Otherwise you've built a new bottleneck ten feet downstream from the old one.

The Headcount Bottleneck

Our competitors had 100x or more people doing comparable work. We have 25. We couldn't hire our way to parity. We had to redesign our way there.

Three systems needed AI running through them: how we design product, how we implement product, and how we test product. If any single one stays manual, it constrains the whole pipeline.

## The Bold Decision: Unifying the Architecture

![Article Image](<https://pbs.twimg.com/media/HFwEjnpbEAAXeFc.jpg>)

I had to fix the codebase first.

Our old architecture was scattered across multiple independent systems. A single change might require touching three or four repositories. From a human engineer's perspective, it is manageable. From an AI agent's perspective, opaque. The agent can't see the full picture. It can't reason about cross-service implications. It can't run integration tests locally.

I had to unify all the code into a single monorepo. One reason: so AI could see everything.

This is a harness engineering principle in practice. The more of your system you pull into a form the agent can inspect, validate, and modify, the more leverage you get. A fragmented codebase is invisible to agents. A unified one is legible.

I spent one week designing the new system: planning stage, implementation stage, testing stage, integration testing stage. Then another week re-architecting the entire codebase using agents.

CREAO is an agent platform. We used our own agents to rebuild the platform that runs agents. If the product can build itself, it works.

## The Stack

Here is our stack and what each piece does.

Infrastructure: AWS

We run on AWS with auto-scaling container services and circuit-breaker rollback. If metrics degrade after a deployment, the system reverts on its own.

CloudWatch is the central nervous system. Structured logging across all services, over 25 alarms, custom metrics queried daily by automated workflows. Every piece of infrastructure exposes structured, queryable signals. If AI can't read the logs, it can't diagnose the problem.

CI/CD: GitHub Actions

Every code change passes through a six-phase pipeline:

Verify CI → Build and Deploy Dev → Test Dev → Deploy Prod → Test Prod → Release

The CI gate on every pull request enforces typechecking, linting, unit and integration tests, Docker builds, end-to-end tests via Playwright, and environment parity checks. No phase is optional. No manual overrides. The pipeline is deterministic, so agents can predict outcomes and reason about failures.

AI Code Review: Claude

Every pull request triggers three parallel AI review passes using Claude Opus 4.6:

Pass 1: Code quality. Logic errors, performance issues, maintainability.

Pass 2: Security. Vulnerability scanning, authentication boundary checks, injection risks.

Pass 3: Dependency scan. Supply chain risks, version conflicts, license issues.

These are review gates, not suggestions. They run alongside human review, catching what humans miss at volume. When you deploy eight times a day, no human reviewer can sustain attention across every PR.

Engineers also tag @claude in any GitHub issue or PR for implementation plans, debugging sessions, or code analysis. The agent sees the whole monorepo. Context carries across conversations.

The Self-Healing Feedback Loop

This is the centerpiece.

Every morning at 9:00 AM UTC, an automated health workflow runs. Claude Sonnet 4.6 queries CloudWatch, analyzes error patterns across all services, and generates an executive health summary delivered to the team via Microsoft Teams. Nobody had to ask for it.

One hour later, the triage engine runs. It clusters production errors from CloudWatch and Sentry, scores each cluster across nine severity dimensions, and auto-generates investigation tickets in Linear. Each ticket includes sample logs, affected users, affected endpoints, and suggested investigation paths.

The system deduplicates. If an open issue covers the same error pattern, it updates that issue. If a previously closed issue recurs, it detects the regression and reopens.

When an engineer pushes a fix, the same pipeline handles it. Three Claude review passes evaluate the PR. CI validates. The six-phase deploy pipeline promotes through dev and prod with testing at each stage. After deployment, the triage engine re-checks CloudWatch. If the original errors are resolved, the Linear ticket auto-closes.

![Article Image](<https://pbs.twimg.com/media/HFwUNbua4AA65-z.jpg>)

Each tool handles one phase. No tool tries to do everything. The daily cycle creates a self-healing loop where errors are detected, triaged, fixed, and verified with minimal manual intervention.

I told a reporter from Business Insider: "AI will make the PR and the human just needs to review whether there's any risk."

Feature Flags and the Supporting Stack

Statsig handles feature flags. Every feature ships behind a gate. The rollout pattern: enable for the team, then gradual percentage rollout, then full release or kill. The kill switch toggles a feature off instantly, no deploy needed. If a feature degrades metrics, we pull it within hours. Bad features die the same day they ship. A/B testing runs through the same system.

Graphite manages PR branching: merge queues rebase onto main, re-run CI, merge only if green. Stacked PRs allow incremental review at high throughput.

Sentry reports structured exceptions across all services, merged with CloudWatch by the triage engine for cross-tool context. Linear is the human-facing layer: auto-created tickets with severity scores, sample logs, and suggested investigation. Deduplication prevents noise. Follow-up verification auto-closes resolved issues.

## How a Feature Moves from Idea to Production

![Article Image](<https://pbs.twimg.com/media/HFwUDbna8AAQ8_F.jpg>)

New Feature Path

1. The architect defines the task as a structured prompt with codebase context, goals, and constraints.
1. An agent decomposes the task, plans implementation, writes code, and generates its own tests.
1. A PR opens. Three Claude review passes evaluate it. A human reviewer checks for strategic risk, not line-by-line correctness.
1. CI validates: typecheck, lint, unit tests, integration tests, end-to-end tests.
1. Graphite's merge queue rebases, re-runs CI, merges if green.
1. Six-phase deploy pipeline promotes through dev and prod with testing at each stage.
1. Feature gate turns on for the team. Gradual percentage rollout. Metrics monitored.
1. Kill switch available if anything degrades. Circuit-breaker auto-rollback for severe issues.

Bug Fix Path

1. CloudWatch and Sentry detect errors.
1. Claude triage engine scores severity, creates a Linear issue with full investigation context.
1. An engineer investigates. AI has already done the diagnosis. The engineer validates and pushes a fix.
1. Same review, CI, deploy, and monitoring pipeline.
1. Triage engine re-verifies. If resolved, ticket auto-closes.

Both paths use the same pipeline. One system. One standard.

## The Results

![Article Image](<https://pbs.twimg.com/media/HFwUohKbcAAi0cm.png>)

Over 14 days, we averaged three to eight production deployments per day. Under our old model, that entire two-week period would have produced not even a single release to production.

Bad features get pulled the same day they ship. New features go live the same day they're conceived. A/B tests validate impact in real time.

People assume we're trading quality for speed. User engagement went up. Payment conversion went up. We produce better results than before, because the feedback loops are tighter. You learn more when you ship daily than when you ship monthly.

## The New Engineering Org

Two types of engineers will exist.

The Architect

One or two people. They design the standard operating procedures that teach AI how to work. They build the testing infrastructure, the integration systems, the triage systems. They decide architecture and system boundaries. They define what "good" looks like for the agents.

This role requires deep critical thinking. You criticize AI. You don't follow it. When the agent proposes a plan, the architect finds the holes. What failure modes did it miss? What security boundaries did it cross? What technical debt is it accumulating?

I have a PhD in physics. The most useful thing my PhD taught me was how to question assumptions, stress-test arguments, and look for what's missing. The ability to criticise AI will be more valuable than the ability to produce code.

This is also the hardest role to fill.

The Operator

Everyone else. The work matters. The structure is different.

AI assigns tasks to humans. The triage system finds a bug, creates a ticket, surfaces the diagnosis, and assigns it to the right person. The person investigates, validates, and approves the fix. AI makes the PR. The human reviews whether there's risk.

The tasks are bug investigation, UI refinement, CSS improvements, PR review, verification. They require skill and attention. They don't require the architectural reasoning the old model demanded.

Who Adapts Fastest

I noticed a pattern I didn't expect. Junior engineers adapted faster than senior engineers.

Junior engineers with less traditional practice felt empowered. They had access to tools that amplified their impact. They didn't carry a decade of habits to unlearn.

Senior engineers with strong traditional practice had the hardest time. Two months of their work could be completed in one hour by AI. That is a hard thing to accept after years of building a rare skill set.

I'm not making a judgment. I'm describing what I observed. In this transition, adaptability matters more than accumulated skill.

## The Human Side

Management Collapsed

Two months ago, I spent 60% of my time managing people. Aligning priorities. Running meetings. Giving feedback. Coaching engineers.

Today: below 10%.

The traditional CTO model says to empower your team  to do architecture work, train them, delegate. But if the system only needs one or two architects, I need to do it myself first. I went from managing to building. I code from 9 AM to 3 AM most days. I design the SOPs and architecture of the system. I maintain the harness.

More stressful. But I'm enjoying building, not aligning.

Less Arguing, Better Relationships

My relationships with co-founders and engineers are better than before.

Before the transition, most of my interaction with the team was alignment meetings. Discussing trade-offs. Debating priorities. Disagreeing about technical decisions. Those conversations are necessary in a traditional model. They're also draining.

Now I still talk to my team. We talk about other things. Non-work topics. Casual conversations. Offsite trips. We get along better because we stopped arguing about work that can be easily done by our system.

Uncertainty Is Real

I won't pretend everyone is happy.

When I stopped talking to people every day, some team members felt uncertain. What does the CTO not talking to me mean? What is my value in this new world? Reasonable concerns.

Some people spend more time debating whether AI can do their work than doing the work. The transition period creates anxiety. I don't have a clean answer for it.

I do have a principle: we don't fire an engineer because they introduced a production bug. We improve the review process. We strengthen testing. We add guardrails. The same applies to AI. If AI makes a mistake, we build better validation, clearer constraints, stronger observability.

## Beyond Engineering

I see other companies adopt AI-first engineering and leave everything else manual.

If engineering ships features in hours but marketing takes a week to announce them, marketing is the bottleneck. If the product team still runs a monthly planning cycle, planning is the bottleneck.

At CREAO, we pushed AI-native operations into every function:

- Product release notes: AI-generated from changelogs and feature descriptions.
- Feature intro videos: AI-generated motion graphics.
- Daily posts on socials: AI-orchestrated and auto-published.
- Health reports and analytics summaries: AI-generated from CloudWatch and production databases.

Engineering, product, marketing, and growth run in one AI-native workflow. If one function operates at agent speed and another at human speed, the human-speed function constrains everything.

## What This Means

For Engineers

Your value is moving from code output to decision quality. The ability to write code fast is worth less every month. The ability to evaluate, criticize, and direct AI is worth more.

Product sense or taste matters. Can you look at a generated UI and know it's wrong before the user tells you? Can you look at an architecture proposal and see the failure mode the agent missed?

I tell our 19-year-old interns: train critical thinking. Learn to evaluate arguments, find gaps, question assumptions. Learn what good design looks like. Those skills compound.

For CTOs and Founders

If your PM process takes longer than your build time, start there.

Build the testing harness before you scale agents. Fast AI without fast validation is fast-moving technical debt.

Start with one architect. One person who builds the system and proves it works. Onboard others into operator roles after the system runs.

Push AI-native into every function.

Expect resistance. Some people will push back.

For the Industry

OpenAI, Anthropic, and multiple independent teams converged on the same principles: structured context, specialized agents, persistent memory, and execution loops. Harness engineering is becoming a standard.

Model capability is the clock driving this. I attribute the entire shift at CREAO to the last two months. Opus 4.5 couldn't do what Opus 4.6 does. Next-gen models will accelerate it further.

I believe one-person companies will become common. If one architect with agents can do the work of 100 people, many companies won't need a second employee.

## We're Early

Most founders and engineers I talk to still operate the traditional way. Some think about making the shift. Very few have done it.

A reporter friend told me she'd talked to about five people on this topic. She said we were further along than anyone: "I don't think anyone's just totally rebuilt their entire workflow the way you have."

The tools exist for any team to do this. Nothing in our stack is proprietary.

The competitive advantage is the decision to redesign everything around these tools, and the willingness to absorb the cost. The cost is real: uncertainty among employees, the CTO working 18-hour days, senior engineers questioning their value, a two-week period where the old system is gone and the new one isn't proven.

We absorbed that cost. Two months later, the numbers speak.

We build an agent platform. We built it with agents.

---


**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2043626511258009924  

**正文**

Anthropic 近日正式推出 Claude Managed Agents（托管智能体）。

现在，任何人都能在数天内而非数月内构建并部署生产级 AI 智能体。

Claude 负责处理基础设施、编排调度和长时间运行的任务执行。

目前已进入公开测试阶段。 

---


**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2043624253350899959  

**正文**

在前沿科技领域赢得成功需要什么？

1、技术洞见
2、近乎宗教般的使命感
3、军事化的执行力

每一代人中，只有极少数企业能够在规模上同时做到这三点。

但一旦做到，他们将改变人类的命运。 

---


**作者** Kirk Marple（@KirkMarple）  
**貼文連結** https://x.com/KirkMarple/status/2003944353342149021  

**正文**

Foundation Capital's recent piece "Context Graphs: AI's Trillion-Dollar Opportunity" is the clearest articulation I've seen of where enterprise AI is heading. @JayaGup10 and @ashugarg argue that the

---


**作者** KK.aWSB（@KKaWSB）  
**貼文連結** https://x.com/KKaWSB/status/2043532376681087267  

**正文**

有位老哥做了个由 AI 代理驱动的搜索引擎， 在 GitHub上已超2万⭐。

搜索权重评分依据点赞数、转发数和真金白银，而非编辑评分。

/last30days能同时搜Reddit、X、YouTube、TikTok、Hacker News和Polymarket，开会前你搜一个人或一个项目，30秒拿到他这个月在干什么——这种信息差Google给不了你。 

---


**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2043585003502948515  

**正文**

又一个新的 Agent 聚合软件 Superconductor

支持在一个软件里面启动比如 Claude Code、Codex、Gemini CLI 等其他编码 Agent Cali 工具

完全用 Rust 写的，目前只有 MacOS 版本 

---


**作者** Jaya Gupta（@JayaGup10）  
**貼文連結** https://x.com/JayaGup10/status/2043505841127760066  

**正文**

The Moat Is State

Anthropic is on one of the fastest revenue ramps in AI, driven heavily by coding and enterprise adoption. Claude Code has become one of the clearest product breakouts in the market, and Cowork is its attempt to push the same dynamic into broader knowledge work. That kind of growth should make the moat obvious. Instead, it makes the question harder. What exactly is compounding here?

Unlike Microsoft and Google, Anthropic did not begin with preexisting enterprise surface-area moats, default distribution, or native state gravity inside the productivity stack. Microsoft came in with Microsoft 365. Google came in with Workspace, BigQuery, and cloud and data gravity. Anthropic came in with model quality and an unusually explicit safety posture. That makes institutional trust more important for Anthropic than it was for either Microsoft or Google. Their existing state gravity already gave enterprises a reason to stay. Anthropic had to find another way in.

That is what makes the company strategically unusual. Its safety posture may be doing more than expressing caution. It may be manufacturing institutional permission while the deeper moat is still being built underneath. Microsoft and Google did not need to build trust this way because they already controlled where enterprise state lived. Anthropic did not. So the real question is not just why Anthropic is growing so quickly. It is why a company growing this quickly still needs trust to do this much work.

That question points to a larger shift. In prior enterprise software categories, the durable moat usually sat in the system where business state already lived. In AI, more of that value may form in the orchestration layer around the model, the layer that remembers, interprets, and acts on top of enterprise data. The emerging battle is no longer just over who has the best model. It is over who owns the state once AI stops being stateless and starts becoming operationally embedded.

What State Means in AI

Enterprise software always had more than one layer of state. But in prior systems, the layer that mattered most usually lived in the system of record and was legibly enterprise-owned. In AI, more of that value may form in the layers around the record: memory, orchestration, repeated interaction, where ownership is less clear and extraction is harder.

The question is no longer just what data the enterprise owns. It is what state begins to accumulate in the system deciding how to use it. Once that happens, the moat is no longer only in the record itself. It begins to form in the layer that remembers, interprets, and acts.

That state takes four forms. Behavioral state is the calibration of production systems to one model’s behavior — parsers, evaluation pipelines, orchestration logic, edge-case handling. It forms fastest and usually lives in the enterprise’s codebase, but it still benefits the model provider by making switching expensive. Memory state is what the agent has done, learned, and been told across sessions: episodic, semantic, procedural. It takes more deliberate architecture, but once established it becomes the most contested layer because it compounds directly. Organizational context state is the accumulated understanding of how a specific company operates, built through connectors, documents, and repeated exposure to enterprise systems. It becomes the most politically sensitive layer because it is clearly organizational in nature, even when it accumulates inside vendor-controlled products. Human-AI state is the model of how specific people think, reason, and work, built through repeated interaction over time. It takes longest to form, but it is the hardest to replace personally and the most legally ambiguous.

Once enough of that state accumulates outside the enterprise’s control, switching stops being a procurement decision and starts becoming an institutional problem.

Who is going for the grand prize of state?

Every major player in enterprise AI is making a bet on which layer of state it will own. These bets are still early, but the architectural choices being made now will be hard to reverse once state has accumulated deeply enough to matter.

Anthropic is betting on owning the full state stack behind a closed API. Claude Managed Agents places the execution layer, memory systems, and context assembly behind a proprietary interface. Enterprises get capability. Anthropic gets the state. The implication is simple: the enterprise may benefit from the intelligence, but the most valuable state can accumulate inside a system it cannot inspect, export, or fully govern. OpenAI is making the same bet with a slower pivot to enterprise.

Microsoft is betting on owning the surface where state accumulates. Copilot sits inside Microsoft 365’s enormous enterprise distribution and governed productivity environment. The state Microsoft owns is not primarily agent memory but the organizational knowledge already encoded in email, documents, meetings, and communications. The AI becomes the interface to state that already lives on Microsoft infrastructure.

Google is betting on integrated data, productivity, and model state at once. Gemini is not just another model endpoint in Google’s stack. It is becoming the interface to the state already living inside Workspace, BigQuery, and Vertex AI. Communication state, analytical state, and inference state are governed by the same platform, and Gemini is increasingly the layer through which that state is searched, interpreted, and acted on. Google’s bet is that the gravity of existing organizational state, combined with Gemini as the native interface to it, makes the AI state that forms there impossible to migrate without moving everything else too.

Databricks represents the clearest state-ownership counterproposal. The closest historical parallel is VMware and Docker: one company proved the abstraction layer mattered, another convinced enterprises they should own it in a more portable form. Episodic memory, semantic memory, and organizational context live in enterprise-governed infrastructure, with the LLM treated as a stateless reasoning engine that reads from persistent state at inference time. The enterprise owns the state. The model becomes a commodity call. Arize makes a related bet from the observability side: in a more stateful AI stack, the company that makes state legible, measurable, and governable may matter more than the company that merely stores it.

AI application startups are betting on owning state through workflow specificity. They may not own the base model but what they can own is the accumulated state inside a high-value workflow: the exceptions, precedents, approvals, edge cases, and user interactions that form when AI is embedded deeply enough in one domain.

Open source is another argument: no vendor owns the state. Self-hosted models, open orchestration layers, enterprise-governed memory, full ownership, no vendor dependency. This bet works if open models become good enough that enterprises judge self-hosting worth the operational burden. The historical analogy is Sun and Linux: the open-systems logic survives, but the proprietary layer that first popularized it does not necessarily keep the value. The friction around open source currently  is quality, trust, governance, and geopolitics, and of course there is the narrative about the extent to which enterprises are willing to rely on open model ecosystems increasingly associated with China.

What is clear is that an enterprise making an AI architecture decision today is deciding who will own the state that accumulates as AI agents become central to work.

Most enterprises do not realize that is what they are deciding. They think they are choosing a model. In practice, they are choosing who gets to own the state that builds around it.

The Ownership Fight Is Not New

The question of who owns the accumulated enterprise state has been fought before. Once state became strategically important, the enterprise either asserted ownership or discovered it was too late. Email felt personal until compliance made it a corporate asset. Slack felt conversational until e-discovery made every message discoverable infrastructure. Gong call recordings felt like individual rep behavior until revenue intelligence made them organizational training data. Enterprises eventually claim the state that matters. The question is whether they do so before or after ceding it to a vendor whose incentives do not align with that claim.

AI state is the same fight at greater scale and with higher stakes. The question of who owns what an AI system learned about an organization while serving it has not been legally settled. The organizational intelligence flowing through AI agents, decision patterns, institutional knowledge, operational understanding accumulated across thousands of interactions sits in a layer where ownership is ambiguous between the model provider, the enterprise, and the infrastructure through which the model is accessed. Model providers are incentivized to resolve that ambiguity in their favor, and they are doing so through architectural choices that lock state into their systems before enterprises fully grasp what is being claimed.

Salesforce’s moat was state: your relationship state, accumulated over years, expensive to migrate. But Salesforce never tried to own the relationship state itself. The license model enforced the distinction. AI vendors are trying something different: to own both the execution environment and the state that accumulates inside it, behind an API that makes the distinction difficult to enforce. You cannot claim ownership of your AI organizational intelligence if you cannot inspect, export, or govern the system that manages it.

The non-compete parallel is the closest legal analogue. Courts have spent a century deciding how much of a person’s accumulated professional state: client relationships, institutional knowledge, strategic instincts which an employer can claim when they leave. The answer that emerged is familiar: you own your general capabilities; your employer owns the specific applications of those capabilities to its business. AI state sits exactly on this boundary. Human-AI state accumulated over two years of professional use is both personal capability and organizational application at once. That boundary has never been litigated for AI. When it is, the outcome will reshape how enterprises think about state ownership,  and which architectural decisions they will wish they had made earlier.

So what?

Regulatory capture is not new. What is different here is trying to use fear and safety posture before the moat is fully built.

Anthropic may be trying to reverse the usual order. The trust story came before the moat was clearly visible. Trust can buy time while a deeper moat is still forming underneath. But it only matters if the moat gets built in time. If it does, the strategy looks prescient. If it does not, then the narrative was doing work the product alone could not yet do.

---


**作者** 沐阳（@yyyole）  
**貼文連結** https://x.com/yyyole/status/2043368043045396755  

**正文**

神文！我怎么现在才看到这篇文章！！

AI领域的顶级大佬，如何规划自己孩子的未来？
受访大佬包括微软首席AI专家、Anthropic总裁、沃顿商学院教授等等。

让我不敢相信的是，这些站在AI技术最前沿的顶级专家，并不打算让孩子去学计算机，学理工科之类的。

大概总结了一下，他们指出了4条“反直觉”的生存法则：

1、不要死磕“短命”的技术或工具，现在任何工具保质期都不超过2年，能更快适应和学会新工具才是王道。

2、要具有人文思维（不是片面的文科复兴），是要做具有人文思维的综合性人才。

3、干AI干不了的事情，AI无法替人坐牢，所以永远替代不了需要担责的工作，比如医生、律师、审计等等。

4、与真实的物理世界建立连接，能够共情，并心存善良。

---


**作者** Viv（@Vtrivedy10）  
**貼文連結** https://x.com/Vtrivedy10/status/2043427918127513836  

**正文**

Harness, Memory, Context Fragments, & the Bitter Lesson

this is a work in progress mental dump on interesting intersections between how we use and design a harness, implications for memory being accumulated over long timescales, and the search bitter lesson we can’t escape

this is v30+, HTML diagrams help me iteratively refine + chat to roughly “see” and alter the mental model

Harnesses & Context Fragments:
a very important job of the harness is to efficiently & correctly route data within its boundaries into the context window boundary for computation to happen

the context window is a precious artifact.  Harnesses make decisions on how to populate, manage, edit, and organize it so agents can do work.  Each loaded object can be thought of as a Context Fragment and represents an explicit decision by the user and harness designer of what needs a model needs to do work at any given time.

many ideas on externalizing objects + loading into the context window are pioneered and very well described by @a1zhang with RLMs

Experiential Memory:
we’re in the very early days of deploying agents and agents produce massive amounts of data in every interaction they have.  this is akin to humans doing things and remembering things they did.

however agent memory has a massive advantage as it can be accumulated across all agents which are easily forked and duplicated (unlike humans).  @dwarkesh_sp does a good talking about this massive benefit of artificial systems

memory can be treated as an externalized object.  the harness is tasked with doing good contextualized retrieval which means pulling in the right data from accumulated memories across all agent interactions

Search & The Bitter Lesson:
As we deploy agents in our world over year timescales, there is going to be a hyper-exponential in the amount of data produced by those agents.  We should want to:
1. Own that data for ourselves.  Open ecosystems are important here
2. Use that data

This means that we’ll have to search over, distill, and organize massive amounts of data.  Our brain is exceptional at doing this.  Both contextually using prior experience and mostly committing the right stuff to memory with enough intentional practice.

Our current infrastructure systems and algorithms will be put to the test and often break as we get used to this new data regime

some open questions:
- how do we efficiently distill experiences (Traces) into higher level memory primitives that capture the important parts? How do we do this over ultra long time horizons?

- How much of the future is Search just-in-time vs Search that gets integrated into model weights?

- How do we make models much better at self-managing their context window?  How do we reduce error rates in recursively allowing agents to operate over external objects?

i’ll be expanding on, altering, and adjusting these mental models but these feel like an important subset to me on the future of designing agents practically
Harness, Memory, Context Fragments, & the Bitter Lesson

this is a work in progress mental dump on interesting intersections between how we use and design a harness, implications for memory being accumulated over long timescales, and the search bitter lesson we can’t escape

this is v30+, HTML diagrams help me iteratively refine + chat to roughly “see” and alter the mental model

Harnesses & Context Fragments:
a very important job of the harness is to efficiently & correctly route data within its boundaries into the context window boundary for computation to happen

the context window is a precious artifact.  Harnesses make decisions on how to populate, manage, edit, and organize it so agents can do work.  Each loaded object can be thought of as a Context Fragment and represents an explicit decision by the user and harness designer of what needs a model needs to do work at any given time.

many ideas on externalizing objects + loading into the context window are pioneered and very well described by @a1zhang with RLMs

Experiential Memory:
we’re in the very early days of deploying agents and agents produce massive amounts of data in every interaction they have.  this is akin to humans doing things and remembering things they did.

however agent memory has a massive advantage as it can be accumulated across all agents which are easily forked and duplicated (unlike humans).  @dwarkesh_sp does a good talking about this massive benefit of artificial systems

memory can be treated as an externalized object.  the harness is tasked with doing good contextualized retrieval which means pulling in the right data from accumulated memories across all agent interactions

Search & The Bitter Lesson:
As we deploy agents in our world over year timescales, there is going to be a hyper-exponential in the amount of data produced by those agents.  We should want to:
1. Own that data for ourselves.  Open ecosystems are important here
2. Use that data

This means that we’ll have to search over, distill, and organize massive amounts of data.  Our brain is exceptional at doing this.  Both contextually using prior experience and mostly committing the right stuff to memory with enough intentional practice.

Our current infrastructure systems and algorithms will be put to the test and often break as we get used to this new data regime

some open questions:
- how do we efficiently distill experiences (Traces) into higher level memory primitives that capture the important parts? How do we do this over ultra long time horizons?

- How much of the future is Search just-in-time vs Search that gets integrated into model weights?

- How do we make models much better at self-managing their context window?  How do we reduce error rates in recursively allowing agents to operate over external objects?

i’ll be expanding on, altering, and adjusting these mental models but these feel like an important subset to me on the future of designing agents practically
just diagram if anyone wants 

---


**作者** Yangyi（@yangyi）  
**貼文連結** https://x.com/yangyi/status/2043153094079606832  

**正文**

三个关于agent记忆的git项目对比
来自 jason 的 AI Builder Club
我觉得做memory一定是要做遗忘的
如果只增不降  冗余会影响性能

这也就是为什么人类需要做梦 

---


**作者** Cobus Greyling（@CobusGreylingZA）  
**貼文連結** https://x.com/CobusGreylingZA/status/2043363380551934461  

**正文**

I just love the language of this study...it speaks of the shifting "community language"...and that is so true...have you noticed the new "community language" is "harness", it was "contextual prompting" before that...

For now, the center of gravity in AI agents has shifted — and this diagram captures it perfectly.

Think of LLM agent capabilities as three stacked layers:

Weights ... Where it all started. Pretraining, fine-tuning, RLHF, scaling laws, alignment. This was the 2022 conversation.

Context ... The 2023-2024 wave. RAG, memory, long context, chain-of-thought, prompting, and context engineering became the focus.

How do we get the right information to the model?

Now, Harness ... Where the conversation lives now. MCP, tool ecosystems, function calling, agent infrastructure, protocols, skills, A2A, multi-agent orchestration, workflow graphs, and security.

The pattern? Community attention has moved steadily outward, from what's inside the model, to what surrounds it, to the infrastructure that connects and orchestrates it all.

The models themselves are becoming a commodity.

The differentiation is increasingly in the harness layer, how you wire agents together, what tools they can use, and how they coordinate.

We've gone from "how do we make the model smarter?" to "how do we make the system around the model smarter?"
That's the real shift.
Source: https://arxiv.org/pdf/2604.08224

This aligns with an excellent blog from @hwchase17  

➡️https://x.com/hwchase17/status/2042978500567609738

---


**作者** Vincent Logic | 只上干货（@VincentLogic）  
**貼文連結** https://x.com/VincentLogic/status/2043277465934807176  

**正文**

> 声明：本文纯干货分享，无任何课程推销，所有工具免费可用。掌握这套方法，每天可节省2-3小时重复工作，真正实现AI赋能业务。

## 一、为什么99%的人搭建的AI智能体都失败了？

在开始教程前，我想先问你一个问题：你是否曾经尝试过搭建AI智能体，但最终发现它输出的内容要么千篇一律，要么充满AI痕迹，根本无法直接使用？

真相是：绝大多数人搭建智能体的方法完全错误。他们要么直接在普通聊天机器人上对话，要么随便写几句提示词就期望AI能理解业务，结果自然是失望而归。

1.1 普通AI与真正智能体的本质区别

让我用一个具体案例说明：

普通AI（如豆包、DeepSeek）的对话：

> 用户：帮我写一条朋友圈
> AI：好的，以下是一条朋友圈文案：
> "今天学习了很多新知识，感觉收获满满。生活中总会有惊喜，保持积极心态很重要。#正能量 #成长"

问题：没有个人特色，没有业务关联，没有目标客户，无法直接使用。

真正的AI智能体对话：

> 用户：帮我写一条观点类朋友圈
> 智能体：
> 昨天第5位客户对我说："我知道AI有用，但实在没时间学。"3年前我也这么想。直到发现：不是时间不够，是方法不对。现在我用这套"15分钟AI工作法"：
> 1️⃣ 早上用AI生成当日内容框架（5分钟）
> 2️⃣ 中午挑选最匹配的1条发布（3分钟）
> 3️⃣ 晚上让AI分析互动数据（7分钟）今天又帮@张总 搭建完朋友圈智能体，他明天就能省下2小时/天。你的时间，值得投资在更重要的事上。
> —— 刚帮客户省下第1000小时的@AI商业顾问

核心差异：

- ✅ 知道你是谁（AI商业顾问）
- ✅ 了解你的客户（没时间学AI的企业主）
- ✅ 掌握你的方法论（15分钟AI工作法）
- ✅ 有真实案例（帮@张总搭建）
- ✅ 个人风格鲜明（数字具体、故事真实）
- ✅ 无任何AI痕迹（自然如真人分享）

1.2 智能体成功的黄金公式

经过200+智能体搭建实战，我总结出真正能落地的智能体公式：

真正有用的智能体 = 70%业务知识 × 20%精准提示词 × 10%工具选择

残酷现实：大多数人把90%精力放在工具选择上，却忽略了最核心的业务知识沉淀。这就是为什么他们搭建的智能体总是"看起来很美，用起来很废"。

## 二、搭建智能体的三步黄金法则（深度详解）

无论你要搭建什么类型的智能体——朋友圈助手、销售话术生成器、短视频脚本专家还是客户分析顾问，都逃不开这三个核心步骤。下面我将用5000字篇幅逐一拆解每个环节的细节。

2.1 第一步：规划功能——90%失败源于此步错误

2.1.1 功能规划的致命误区

误区一：追求大而全

- ❌ 错误做法："我要一个能写朋友圈、做PPT、写销售话术、分析数据的全能智能体"
- ✅ 正确做法：每个智能体只专注1个核心场景，解决1个具体问题

误区二：忽略使用场景

- ❌ 错误做法："让它帮我写朋友圈"（太模糊）
- ✅ 正确做法：明确使用场景、频率、输出标准场景：每天早上9点规划当天3条朋友圈
频率：每天使用1次，每次生成3-5条候选
标准：每条150字以内，包含1个故事/案例，结尾有互动钩子


误区三：忽视迭代路径

- ❌ 错误做法：期望一次搭建完美智能体
- ✅ 正确做法：规划最小可用版本（MVP）→ 投入使用 → 收集反馈 → 优化迭代

2.1.2 朋友圈智能体功能规划实战

核心功能清单（按优先级排序）：

功能等级 功能描述 使用场景 验收标准    

P0（必须） 写单条观点类朋友圈 每天生成1-2条核心观点 无需修改可直接发布，有个人故事和数据支撑   

P0（必须） 改写竞品朋友圈 看到好内容快速转化 10秒内完成改写，风格100%匹配，保证原创   

P1（重要） 生成日规划方案 每周一规划整周内容 包含3种类型分布、发布时间建议、内容要点   

P2（可选） 分析互动数据 每月复盘内容效果 基于历史数据给出优化建议，指出高互动特征

功能边界明确（什么不做）：

- ✖️ 不自动发布朋友圈（需要人工审核）
- ✖️ 不生成图片/视频（专注文案创作）
- ✖️ 不处理私信咨询（仅限朋友圈场景）

2.1.3 功能规划检查清单

在开始下一步前，确认你的功能规划是否通过以下检查：

- 功能描述是否具体到可测试？（如"写观点类朋友圈"而非"写好朋友圈"）
- 是否有明确的成功标准？（如"可直接发布无需修改"）
- 使用频率是否合理？（高频功能优先实现）
- 是否有清晰的输入输出定义？（用户输入什么，智能体输出什么）
- 是否有失败回退机制？（当AI不理解时如何处理）

2.2 第二步：知识库准备——决定智能体成败的核心

知识库是智能体的"大脑"，它决定了AI输出内容的专业度、准确性和个性化程度。90%的智能体失败，根源在于知识库准备不足。

2.2.1 知识库的两大核心类型

类型一：业务知识库（让AI了解"你是谁"）

知识库类型 具体内容 准备方法 案例片段    IP个人档案 你的背景、经历、价值观、表达习惯 整理个人介绍文档，包含：
- 3个关键人生转折点
- 5个常用口头禅
- 2-3个标志性故事 "2018年从500强辞职创业，因为看到太多传统企业被数字化浪潮淘汰..."   客户深度画像 目标客户详细特征，不仅是基础人口统计 采访10个典型客户，整理：
- 3个核心痛点
- 2个决策障碍
- 1个情感诉求 "35-45岁中小企业老板，表面说'没预算'，实际是'怕投入没效果'，需要看到同行业案例才敢决策..."   产品/服务百科 所有产品细节，包括不对外宣传的"内幕" 创建产品手册，包含：
- 价格体系及逻辑
- 客户常见异议及回应
- 产品局限性说明 "基础版3980元/年，适合10人以下团队；但超过20人必须用企业版，否则会遇到数据同步问题..."   行业知识图谱 行业术语、规则、潜规则、发展趋势 收集行业报告+个人观察：
- 10个核心术语解释
- 3个行业痛点演变
- 2个未被满足的需求 "在SaaS行业，客户说'再考虑考虑'通常意味着价格敏感度低，而是对效果不确定..."   成功案例库 详细的成功案例，包含过程和细节 每个案例包含：
- 客户背景/痛点
- 解决过程/关键决策
- 量化结果/客户证言 "客户王总，42岁建材老板，团队15人，通过我们的智能体搭建，3周内朋友圈互动率提升300%，新增5个精准客户..."

类型二：方法论知识库（让AI知道"怎么做"）

知识库类型 具体内容 准备方法 案例片段    朋友圈创作方法论 朋友圈写作的完整体系 整理你的写作流程：
- 4种朋友圈类型及特征
- 5个高互动朋友圈公式
- 3个避坑指南 "观点类朋友圈公式：个人故事(40字)+行业观察(50字)+方法论提炼(40字)+互动提问(20字)"   风格指南 你的内容风格规范 创建风格手册：
- 禁用词汇清单
- 常用句式模板
- 情感表达方式 "禁用'作为AI''根据资料显示'等表述；必须使用第一人称；每3条内容至少包含1个真实失败经历..."   内容日历 内容规划的节奏和主题 制定月度主题规划：
- 节日/热点日历
- 产品推广节奏
- 客户教育路径 "1月-信任建立；2月-痛点挖掘；3月-解决方案；每周三发案例，周五发观点，周日发生活..."   竞品分析库 优秀竞品内容分析 收集50-100条优质内容：
- 高互动内容特征
- 转化效果好的文案
- 失败案例及原因 "这条朋友圈获赞87次，关键在于开头用'3年前'制造时间对比，中间用具体数字'13次失败'增加可信度..."

2.2.2 知识库准备的实操技巧

技巧一：知识库文件命名规范

- ✅ 正确命名：\[类型\]\_\[主题\]\_\[版本\].格式例：客户画像\_中小企业老板\_v1.2.pdf
例：方法论\_朋友圈写作公式\_v2.0.docx

- ❌ 错误命名：新建文档1.docx、资料.pdf

技巧二：知识库内容质量标准

- 真实性：所有案例必须真实，数据可验证
- 具体性：避免抽象描述，用具体场景和数字❌ "客户很满意我们的服务"
✅ "客户李总在使用3天后，主动介绍2个朋友成交，总金额58,000元"

- 可操作性：提供明确的操作步骤，而非理论❌ "要站在客户角度思考"
✅ "写文案时先问自己：这个痛点是否让客户夜不能寐？解决方案是否清晰到小学生能懂？"


技巧三：知识库更新机制

- 每周预留30分钟更新知识库
- 建立"知识库反馈循环"：智能体使用 → 收集问题 → 分析原因 → 更新知识库 → 重新测试


2.2.3 朋友圈智能体知识库完整清单

以下是我实际使用的朋友圈智能体知识库文件清单（共12个文件，总计38页）：

基础业务类（6个文件）：

1. IP档案\_个人背景与价值观\_v1.3.pdf（5页）
1. 客户画像\_目标客户深度分析\_v2.1.docx（8页）
1. 产品手册\_服务详情与价格体系\_v1.5.pdf（6页）
1. 案例库\_15个成功客户故事\_v3.0.docx（12页）
1. 行业知识\_AI商业落地趋势\_v1.2.pdf（4页）
1. 失败案例\_7次踩坑总结\_v1.0.docx（3页）

方法论类（6个文件）：
7. 朋友圈方法论\_4大类型创作指南\_v2.3.pdf（15页）
8. 风格指南\_个人表达规范\_v1.1.docx（3页）
9. 内容日历\_2024全年主题规划.xlsx（1页）
10. 竞品分析\_50条高互动朋友圈拆解\_v1.4.pdf（10页）
11. 转化路径\_从互动到成交的5个关键点\_v1.0.docx（4页）
12. 避坑指南\_朋友圈常见错误清单\_v1.2.pdf（2页）

> 💡 新手建议：不必一次性准备所有文件。先从最核心的3个开始：IP档案、客户画像、朋友圈方法论，其他文件在使用过程中逐步补充。

2.2.4 知识库常见问题解决方案

问题一：知识库内容质量不高

- 症状：AI输出内容空洞、缺乏细节
- 解决方案：用"5W1H"法则检查：Who（谁）、What（什么）、When（何时）、Where（何地）、Why（为什么）、How（如何）
每个知识点至少包含1个具体案例
删除所有"应该""最好"等模糊表述，替换为具体操作


问题二：知识库内容冲突

- 症状：AI在不同对话中给出矛盾建议
- 解决方案：建立知识权威等级（如：客户反馈 > 行业报告 > 个人经验）
在提示词中明确优先级："当知识库内容冲突时，优先采用客户案例中的方法"
定期知识库"体检"，删除过时或矛盾内容


问题三：知识库更新不及时

- 症状：AI不知道最新产品/服务变化
- 解决方案：建立知识库更新日历（每月第1个周一更新）
设置知识库版本号，智能体明确显示使用版本
重要变更时，用"知识库更新公告"文件通知AI


2.3 第三步：搭建测试——让智能体真正落地

有了清晰的功能规划和完备的知识库，现在进入实操搭建环节。我将用CloudCPT平台为例（免费版足够使用），详细拆解每个按钮操作。

2.3.1 平台选择深度对比

平台名称 提示词支持 知识库支持 中文能力 价格 适用场景    

CloudCPT ✅ 完整支持 ✅ 向量检索 ⭐⭐⭐⭐⭐ 免费基础版 业务智能体首选   

Dify ✅ 支持 ✅ 支持 ⭐⭐⭐⭐ 免费 技术背景用户   

扣子 ⚠️ 有限支持 ⚠️ 有限支持 ⭐⭐⭐⭐ 免费 简单场景   

豆包/DeepSeek ❌ 不支持 ❌ 不支持 ⭐⭐⭐⭐⭐ 免费 通用对话   

Notion AI ⚠️ 有限支持 ❌ 不支持 ⭐⭐⭐ 付费 知识管理

为什么选择CloudCPT：

- 完全免费：基础版足够个人使用，无功能限制
- 中文优化：专为中文业务场景设计，无翻译腔
- 操作简单：界面直观，无需技术背景
- 知识库强大：支持PDF/Word/TXT，向量检索精准

2.3.2 详细搭建步骤（截图级指导）

步骤1：创建项目

1. 访问CloudCPT官网（搜索"CloudCPT"即可找到）
1. 登录/注册账号（支持微信一键登录）
1. 在左侧菜单点击「项目」
1. 点击右上角「新建项目」按钮
1. 填写项目信息：项目名称：朋友圈智能体\_v1
项目描述：为@AI商业顾问 生成个性化朋友圈内容，包含观点/案例/产品/互动4种类型
选择模型：Cloud-72B（中文文案最佳）

1. 点击「创建项目」按钮

步骤2：配置提示词

1. 在项目详情页，找到「指示」区域
1. 点击「+ 添加指示」按钮
1. 关键技巧：提示词不是一次性写完的，分5个模块逐步完善

模块1：角色定义（让AI知道身份）

你是一位拥有5年实战经验的AI商业落地顾问，专注于帮助中小企业主通过AI提升工作效率。你的个人背景：
- 2018年从世界500强企业辞职创业
- 已帮助327家企业搭建AI智能体
- 核心理念：AI是放大器，不是创造器
- 表达风格：真实、直接、有数据支撑，避免理论说教
- 禁用词汇：作为AI、根据资料显示、我认为（必须用"我发现""数据显示"）

模块2：核心方法论（让AI知道专业标准）

朋友圈创作的黄金法则：
1. 真实性原则：每条内容必须基于真实经历或客户案例
2. 价值密度：150字内必须包含1个具体方法/洞察
3. 活人感公式：个人故事(40%)+专业洞察(40%)+互动钩子(20%)
4. 避免AI痕迹：禁用排比句、过度修饰、完美逻辑链

4种朋友圈类型标准：
【观点类】包含1个反常识观点+1个亲身经历+1个行动建议
【案例类】包含客户背景+具体问题+解决过程+量化结果
【产品类】包含使用场景+核心价值+客户证言+低门槛行动
【互动类】包含开放式问题+个人回答示例+邀请参与

模块3：任务流程（让AI知道操作步骤）

当用户要求生成朋友圈时，按以下流程执行：
1. 识别类型：判断用户需要哪种类型的朋友圈（观点/案例/产品/互动）
2. 调取知识：从知识库中检索相关素材：
   - 观点类：调取「行业知识」+「个人经历」
   - 案例类：调取「成功案例库」+「失败案例」
   - 产品类：调取「产品手册」+「客户反馈」
   - 互动类：调取「客户痛点」+「互动历史」
3. 内容创作：
   - 字数严格控制在120-150字
   - 必须包含1个具体数字（如"3年""13次""87%")
   - 必须包含1个情感触发点（如"夜不能寐""恍然大悟")
4. 风格检查：
   - 通过"朗读测试"：出声朗读是否自然流畅
   - 通过"真人测试"：是否像真人会发的内容
   - 通过"价值测试"：朋友看到是否会点赞/评论
5. 输出格式：直接给出可发布内容，无需解释

模块4：规则约束（让AI知道边界）

严格禁止：
- 生成任何虚假数据或编造客户案例
- 使用网络流行语或过时梗（如"yyds""绝绝子")
- 一次性生成超过5条内容（容易质量下降）
- 在内容中提及AI、算法、提示词等技术术语

必须做到：
- 每3条内容中至少有1条包含失败经历
- 涉及产品时必须说明适用条件和局限性
- 观点类内容必须有反常识角度
- 所有建议必须可操作，避免抽象理论

模块5：输出格式（让AI知道如何呈现）

输出必须是纯文本，格式规范：
- 开头：直接进入内容，无需标题
- 段落：最多2段，每段不超过3行
- 结尾：个人标签（如"—— 刚帮客户省下1000小时的@AI商业顾问"）
- 特殊符号：仅使用「」、——、• 三种符号
- 禁用符号：❌✅⭐🔥💡 等emoji表情

步骤3：上传知识库

1. 在项目详情页，找到「文件」区域
1. 有两种上传方式：拖拽上传：打开文件夹，选中文件直接拖到上传区（区域变蓝后松手）
点击上传：点击「+」按钮，从电脑选择文件

1. 上传顺序建议：1. IP档案\_个人背景与价值观\_v1.3.pdf
2. 客户画像\_目标客户深度分析\_v2.1.docx  
3. 朋友圈方法论\_4大类型创作指南\_v2.3.pdf
4. 其他文件...

1. 上传后系统自动处理（PDF/Word需要1-2分钟索引）
1. 验证上传成功：文件名显示为绿色，大小正确

步骤4：测试优化

1. 基础功能测试（必须通过）：测试1：输入"帮我写一条观点类朋友圈"
测试2：输入"帮我写一条关于客户没时间学AI的案例"
测试3：输入"规划今天3条朋友圈，包含1观点1案例1互动"

1. 深度优化技巧（提升质量关键）：
双窗口测试法：窗口A：智能体对话窗口
窗口B：普通AI窗口（用于修改提示词）
当发现问题时，在窗口B输入："刚才输出的朋友圈有以下问题：\[具体问题\]，请修改提示词中\[对应模块\]部分"

活人感强化技巧：
在提示词中添加：生成内容前，问自己三个问题：
1. 这是我昨天真实发过的内容吗？
2. 朋友看到会想评论'太真实了'吗？
3. 能看出是机器生成的吗？
任何一题答案为'是'，重新生成

数据验证机制：
在知识库中添加「数据校验表」，包含：产品价格表：基础版3980元/年（10人内），企业版12800元/年（50人内）
服务周期：标准实施14天，紧急项目7天加急
客户行业分布：制造业35%，零售28%，服务业22%，其他15%

1. 迭代优化节奏：第1-3天：每天收集5个问题，立即优化
第4-7天：每3天汇总问题，批量优化
第2周后：每周优化1次，重点关注转化率
1个月后：每月优化1次，保持知识库更新


2.3.3 测试案例与优化过程

初始测试（第1天）：

> 用户：帮我写一条观点类朋友圈
> 智能体输出：
> "在当今AI快速发展的时代，很多企业主感到焦虑，担心被时代淘汰。其实，学习AI并不需要大量时间，关键是要找到适合自己的方法。每天只需15分钟，就能掌握核心技能，提升工作效率。坚持下去，你一定会看到改变。#AI #效率提升"

问题分析：

1. ❌ 充满AI痕迹（"在当今...时代"开头）
1. ❌ 无个人故事和具体数据
1. ❌ 说教语气，像教科书
1. ❌ 有话题标签（真人很少用）

优化过程：

1. 在提示词「角色定义」模块增加：你从不用'在当今XX时代'开头，总是用具体场景或故事开始

1. 在「任务流程」模块增加：必须包含1个具体数字和1个情感触发词，如'3年''13次''夜不能寐'

1. 在「规则约束」模块增加：严格禁止使用#话题标签，结尾必须用个人标签"—— \[描述\]+@名字"


优化后输出（第3天）：

> 昨天第8位客户对我说："道理都懂，就是做不到。"2年前我也陷入这个怪圈：买了27门课，做了137页笔记，却从没真正用起来。后来发现：不是知识不够，是行动系统缺失。现在我只做一件事：每天选1个方法，用在1个真实客户身上。
> 3个月后，这套"1×1法则"让我服务效率提升3倍。你缺的不是更多知识，是让知识流动起来的管道。
> —— 用1×1法则服务327家企业的@AI商业顾问

质量评分：

- ✅ 个人故事具体（27门课，137页笔记）
- ✅ 有情感触发（"陷入怪圈""夜不能寐"）
- ✅ 数据可信（327家企业）
- ✅ 无AI痕迹（自然口语化）
- ✅ 价值明确（1×1法则）
- ✅ 互动钩子（引发读者反思）

## 三、高阶技巧：让智能体真正"懂你"

基础搭建完成后，以下高阶技巧将让你的智能体从"能用"升级到"好用"，再到"离不开"。

3.1 活人感强化训练

问题本质：大多数AI内容失败，不是因为不够专业，而是因为太"完美"、太"正确"，缺乏人性化的瑕疵和情感波动。

解决方案：在知识库中增加「人性化训练集」：

1. 不完美表达库：
收集你口语中常用的"不完美"表达："这个...让我想想"
"说实话，我也没想到会这样"
"可能是我太较真了"

1. 情感波动记录：
记录真实情绪变化："连续3天没效果，差点想放弃"
"客户突然说要加单，激动得手都在抖"
"被质疑时，第一反应是 defensive，后来..."

1. 生活片段注入：
每周添加3-5个生活细节："周一早上咖啡洒在键盘上"
"陪孩子搭积木时想到的业务灵感"
"地铁上观察到的用户行为"


实操案例：
在知识库添加文件：人性化训练\_真实生活片段\_v1.0.txt

\[2024-03-15\] 今天演示时网络断了，客户反而说："看来AI也不是万能的，需要人来兜底。" 这句话让我思考了很久...
\[2024-03-22\] 凌晨2点改方案，女儿偷偷给我放了杯热牛奶，上面写着"爸爸加油"。那一刻觉得，所有辛苦都值得。
\[2024-04-01\] 被客户连续拒绝5次，走在回家路上突然下雨，没带伞。但转念一想：至少今天验证了这个方向不对。

效果对比：

> 优化前：
> "坚持就是胜利，只要努力就一定能看到成果。"优化后：
> 凌晨1点改完第7版方案，看着窗外的路灯，想起5年前那个被客户骂哭的自己。那时觉得天塌了，现在才明白：每次被拒绝，都是在帮未来的客户筛选掉不合适的服务。所以啊，别怕被说"太贵"，怕的是你连被拒绝的勇气都没有。
> —— 被拒绝过137次，依然热泪盈眶的@AI商业顾问

3.2 业务闭环设计

真正的商业智能体，不止于内容生成，更要驱动业务结果。设计业务闭环：

内容生成 → 人工审核 → 发布互动 → 数据收集 → 效果分析 → 知识库更新

数据收集模板：
在知识库中添加：数据追踪\_朋友圈效果记录.xlsx

日期 内容类型 互动数 评论关键词 新增咨询 转化客户 优化建议    4.1 观点类 43 "太真实了""哪里学" 5 1（王总） 增加失败细节   4.2 案例类 87 "求介绍""多少钱" 12 3（李总等） 突出价格优势   4.3 产品类 21 "看不懂""太复杂" 2 0 简化技术术语

智能体自优化机制：
在提示词中添加：

当用户要求生成内容时，先查看最近3条高互动内容的特征：
- 高互动（>50）：采用相似结构和关键词
- 低互动（<20）：避免使用相同表达方式
- 转化好：突出具体数字和结果
- 互动好：增加情感共鸣点

3.3 多智能体协同工作

当业务复杂度提升，单个智能体不够用时，设计智能体协同网络：

\[内容智能体\] → 生成朋友圈/短视频脚本
       ↓
\[客户分析智能体\] ← 收集互动数据/评论分析
       ↓
\[销售话术智能体\] → 根据客户兴趣生成个性化跟进话术
       ↓
\[复盘优化智能体\] → 生成周报/优化建议

协同机制设计：

1. 数据共享：建立统一知识库，各智能体按需调用
1. 任务流转：设计标准输入输出格式
1. 冲突解决：设置决策优先级（如销售数据 > 内容偏好）

朋友圈-销售协同案例：

- 朋友圈智能体生成内容 → 发布后获得23条评论
- 客户分析智能体识别：15条评论询问"价格"，8条询问"效果"
- 销售话术智能体自动生成：针对问价格的客户：  
"张总好，看到你关注价格。其实很多客户最初也这么想，但后来发现：关键不是花多少钱，而是能省多少时间。上周@李总 用3980元/年的基础版，每天省下2小时，相当于每月多服务8个客户。需要我发你他的案例详情吗？"

针对问效果的客户：  
"王总好，效果确实是我们最关注的。我们承诺：14天内如无明显效果，全额退款。更重要的是，我们会手把手教你搭建，而不是只卖工具。目前327家客户中，92%在第7天就开始看到效率提升。你最想先解决哪个环节的问题？"


## 四、常见问题解决方案（避坑指南）

4.1 知识库相关问题

Q：知识库文件太大，上传失败怎么办？
A：采用分块策略：

1. 按主题拆分：将100页PDF拆分为10个10页文件
1. 按优先级上传：先上传核心文件（IP档案、客户画像），再上传辅助文件
1. 优化文件格式：PDF转Word再转TXT，减少格式干扰

Q：AI不理解知识库中的专业术语怎么办？
A：在知识库中添加「术语解释表」：

\[术语\] 向量检索  
\[通俗解释\] 就像图书馆的分类系统，把相似内容放在一起，方便快速找到  
\[使用场景\] 当用户问'知识库怎么工作'时使用此解释

\[术语\] 提示词工程  
\[通俗解释\] 给AI写操作说明书，越具体越好  
\[使用场景\] 向客户解释为什么需要详细提示词

4.2 提示词相关问题

Q：提示词越写越长，效果反而变差
A：采用模块化设计：

1. 将提示词拆分为独立模块文件
1. 每个模块专注一个功能（角色定义/方法论/流程等）
1. 通过版本控制管理迭代：v1.0 基础版
v1.1 增加活人感规则
v1.2 优化数据验证


Q：AI总是不遵守规则约束
A：使用"后果绑定"技巧：

如果你输出的内容包含AI痕迹，将导致：
- 327位客户质疑专业性
- 个人品牌价值下降30%
- 每月损失5-8个潜在客户

如果你输出的内容具有活人感，将带来：
- 客户信任度提升40%
- 咨询转化率提高25%
- 个人IP价值每月增长15%

4.3 效果优化问题

Q：生成内容质量不稳定，时好时坏
A：建立"质量-场景"映射表：

场景特征 质量表现 优化策略    早上9-11点 高质量 保持当前提示词   深夜11点后 说教味重 增加情感触发词库   涉及新产品 数据不准 优先调用产品手册   用户情绪低落 共鸣不足 增加失败经历比例

Q：如何量化智能体的效果？
A：设计三级指标体系：

- 基础指标（是否可用）：无需修改直接使用率（目标>80%）
平均生成时间（目标<30秒）

- 业务指标（是否好用）：互动率提升（对比人工创作）
时间节省（小时/周）

- 商业指标（是否值钱）：线索转化率
客单价变化
客户生命周期价值


## 五、扩展应用：不止于朋友圈

掌握这套方法后，你可以快速搭建各种业务智能体。以下是经过验证的扩展场景：

5.1 新媒体矩阵智能体

短视频脚本智能体：

- 知识库：爆款视频结构库、平台规则、热点日历
- 提示词重点：前3秒钩子设计、节奏控制、转化路径
- 效果：1人可日产15条脚本，播放量提升200%

小红书文案智能体：

- 知识库：高互动封面模板、关键词库、违禁词清单
- 提示词重点：情绪价值、实用价值、视觉化表达
- 效果：笔记互动率从2%提升至8%，引流转化率提升35%

5.2 业务运营智能体

客户跟进智能体：

- 知识库：客户背景、历史沟通、痛点记录、竞品情况
- 提示词重点：个性化开场、价值重申、低门槛行动
- 效果：销售周期缩短40%，转化率提升28%

会议纪要智能体：

- 知识库：业务术语表、决策标准、责任人清单
- 提示词重点：行动项提取、责任人明确、时间节点
- 效果：会议效率提升60%，任务完成率提升45%

5.3 产品交付智能体

方案定制智能体：

- 知识库：产品组合逻辑、价格体系、成功案例
- 提示词重点：需求匹配度、价值量化、风险提示
- 效果：方案制作时间从3小时缩短至20分钟，客户满意度提升32%

客户培训智能体：

- 知识库：常见问题库、操作视频、错误案例
- 提示词重点：分步指导、错误预警、成功激励
- 效果：培训周期缩短50%，支持请求减少65%

## 六、终极心法：AI时代的个人护城河

搭建智能体的技术门槛正在快速降低，真正的竞争力不在于工具使用，而在于以下三个核心能力：

6.1 业务洞察深度

- 表层：知道AI可以生成内容
- 深层：理解内容背后的客户决策心理、行业演变规律、价值传递路径

修炼方法：

1. 每天记录3个客户真实反馈（不仅是赞美，更要记录质疑）
1. 每周分析1个失败案例，找出根本原因
1. 每月与3个不同行业从业者深度交流

6.2 方法论沉淀能力

- 表层：收集各种提示词模板
- 深层：将个人经验转化为可复用的方法论体系

修炼方法：

1. 建立"经验-方法"转化表：个人经历 → 抽象规律 → 操作步骤 → 验证指标

1. 用"教别人"的标准整理知识：能否让实习生按此操作？
能否用3句话说清核心？
能否预测执行结果？


6.3 人性理解精度

- 表层：让AI写出无AI痕迹的内容
- 深层：理解人性中的矛盾、恐惧、渴望与成长

修炼方法：

1. 建立"人性观察日记"：记录自己和他人的情绪波动
分析行为背后的深层动机
识别表层需求与真实需求的差异

1. 设计"人性测试题"：当客户说"太贵了"，真实含义可能是：
A. 真的没钱
B. 价值不清晰
C. 风险感知高
D. 谈判策略
E. 需要分期付款


## 结语：你的AI智能体行动路线图

第1天：完成基础搭建

- 规划朋友圈智能体的3个核心功能
- 准备3个核心知识库文件（IP档案、客户画像、方法论）
- 在CloudCPT创建项目，上传提示词和知识库
- 通过基础功能测试

第1周：投入真实使用

- 每天用智能体生成3条朋友圈
- 记录5个需要优化的问题
- 每3天优化1次提示词
- 周日汇总数据，制定下周优化计划

第1个月：建立业务闭环

- 设计数据追踪表格
- 分析10条高互动内容的共同特征
- 将客户反馈转化为知识库更新
- 量化时间节省和效果提升

第3个月：扩展智能体网络

- 基于成功经验，搭建第2个智能体（如销售话术）
- 设计智能体间的数据流转机制
- 建立个人知识库体系，持续沉淀方法论

最后的问题：在AI时代，你选择做工具的主人，还是工具的奴隶？

当你拥有清晰的业务认知、经过验证的方法论、深刻的人性理解，再配合AI智能体这个"超级放大器"，你将获得前所未有的竞争优势。这不是取代人类，而是让人回归到最擅长的领域——创造、决策、连接。

现在，打开你的CloudCPT账号，迈出构建第一个智能体的第一步。15分钟后，你将收获一个能为你每天节省2小时的数字伙伴。这15分钟，可能是你今年最有价值的时间投资。

欢迎在评论区分享：你搭建的第一个智能体是什么？遇到了哪些挑战？有哪些惊喜发现？我们一起交流，共同成长。

---


**作者** Aman（@_amankishore）  
**貼文連結** https://x.com/_amankishore/status/2043063324301046000  

**正文**

Is anyone else losing their minds watching @tryramp produce such interesting research as they implement their own harnesses and agentic systems internally?

Very impressed by @RampLabs
Is anyone else losing their minds watching @tryramp produce such interesting research as they implement their own harnesses and agentic systems internally?

Very impressed by @RampLabs
You should also read this interpretability research if you haven't yet

https://x.com/RampLabs/status/2039726632886235648?s=20

---


**作者** Des Traynor（@destraynor）  
**貼文連結** https://x.com/destraynor/status/2043328865427173771  

**正文**

This is a great article about the new table-stakes of adapting to, and competing in, the AI era.

---


**作者** 鸭哥（@grapeot）  
**貼文連結** https://x.com/grapeot/status/2043359748851167658  

**正文**

2026 年了，Copilot 还是不能帮你改 PPT。Claude Cowork 两周就做到了，但那不是工程奇迹——它有 Claude Code 的 agent 基座，接个新文件类型本来就快。大厂缺的不是工程能力，甚至不是对 agent 架构的理解（微软做 Copilot Cowork 直接用了 Anthropic 的框架）。它们缺的是建 agent 基座的意愿，而这个意愿被三把锁锁住了：per-seat 收入模型让 agentic AI 变成自伤行为，2023 年选的 chat sidebar 架构创造了路径依赖，责任真空让保守成了唯一理性选择。

https://yage.ai/share/three-locks-agentic-doc-editing-20260412.html?utm_source=twitter&utm_medium=thread&utm_campaign=three-locks-agentic-doc-editing

---


**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2043398104636895290  

**正文**

Will AI agents ruin the internet?

Old: M̶a̶r̶k̶e̶t̶e̶r̶s̶ ruin everything
New: AI Agents ruin everything

Imagine if everyone on earth could knock on your door simultaneously

That's what AI agents do to your inbox, social feeds, DMs etc

So the only thing that scales is actually being interesting

Raw content, real relationships, genuine reputation

Build something worth finding.

Because when every channel is noise, the only signal is genuine trust.

Build that now. Before the flood hits.

---


**作者** Kirk Marple（@KirkMarple）  
**貼文連結** https://x.com/KirkMarple/status/2043081571427848445  

**正文**

Recently there's been a flurry of insightful discussions around agent memory. Harrison Chase (@hwchase17) argued that your harness is your memory, and if you're using a closed one, you've already lost control. Sarah Wooders (@sarahwooders) had presented that memory isn't a plugin - it IS the harness, inseparable from how context is managed. And Chrys Bader (@chrysb) published a clear-eyed map of why long-term memory for LLMs remains unsolved - every approach is "a different set of trade-offs dressed up as a solution."

They're all making important points. But here's what I keep coming back to: the conversation is anchored on the wrong object.

## Memory is context. But it's not the only context.

Harrison made a point I agree with deeply: "Memory is just context." He's right. But I'd push that one step further - memory is a peer type of context, not the center of it.

I've been building context infrastructure at Graphlit (@graphlit) for several years now. In a real system - one that's ingesting a user's email, Slack messages, meeting transcripts, calendar events, documents, and web pages - memory sits alongside all of those as one more source of enriched knowledge. It's valuable. It's not special.

The current debate treats memory as if it's the defining problem of agent intelligence. I don't think it is. The real question isn't "who owns the memory?"

It's who owns the enriched knowledge that comes from all of your context - and can you get it out?

## The harness manages context. The knowledge layer produces it.

Sarah is right that the harness makes invisible decisions - what survives compaction, how metadata is presented, what the agent can and can't modify about its own state. Those decisions shape what the agent sees on any given turn. That's context management, and it belongs in the harness.

But the durable knowledge that feeds those context windows is a different thing. The entities extracted from your email. The facts pulled from your meeting transcripts. The relationships inferred across your documents. That knowledge doesn't have to live inside the harness. It shouldn't.

Entities don't change when you swap models. Facts don't expire when you switch harnesses. A knowledge graph is harness-agnostic by nature.

The claim that memory is inseparable from the harness conflates the runtime with the substrate. They're different layers solving different problems.

## Long-term memory is hard. That's not an excuse to hide the results.

Chrys's deep dive is worth reading carefully. The raw vs. derived tradeoff is real. Derivation drift is real. Forgetting is structural. Every memory system fails - the question is how, and whether you can tell.

I don't claim we've solved this. But we've made a specific architectural choice: keep both the raw and the derived, and make both accessible.

When an email lands in Graphlit, we store the original content and we extract entities, facts, and relationships - all at ingestion time, not at query time. We categorize facts into 23 typed categories: decisions, commitments, delegations, escalations, goals, and more. The raw content is always there. The derived knowledge graph sits alongside it. Both are queryable. Both are exportable.

This doesn't eliminate the tradeoffs Chrys describes. It does mean the user isn't locked into a single system's interpretation of their data. If our extraction drifts, the raw source is still there. If you want to re-derive, you can.

## Memory as a peer content type

Here's where I want to make this concrete. In Graphlit, Memory is a content type - the same way Email, Message, Transcript, and File are content types. When an agent stores a memory, it goes through the same extraction pipeline as everything else: entity extraction, fact categorization, relationship mapping. It becomes part of the same knowledge graph.

Memory doesn't get a special store or a separate retrieval path. It sits in the graph next to the email where a preference was first expressed, the meeting transcript where it was reinforced, and the document where it was formalized.

The alternative - memory in its own silo, with its own retrieval logic - creates the same fragmentation problem we already have with systems of record. You end up with one system that knows what the agent remembers, and another that knows what the user actually said. The whole point of a knowledge graph is to collapse that gap.

The knowledge compounds across all content types. Not just the ones labeled "memory."

## Agents produce context, not just consume it

Here's where I think the current debate goes wrong. Everyone frames memory as something an agent reads. But in a real agent platform, every agent run produces new knowledge.

We've built our Dossium (@dossium) agent platform on top of the same unified context graph. When an agent executes - whether it's a chat conversation, a scheduled briefing, or a background research task - the conversation itself becomes a knowledge source. We extract entities, facts, and relationships from agent runs the same way we extract them from email or transcripts.

Think about what this means in practice. An agent prepares a meeting briefing for a call with Acme Corp. During that run, it synthesizes signals from your email, CRM, Slack, and prior meeting transcripts. The decisions it surfaced, the commitments it identified, the relationships it mapped - all of that gets extracted and ingested back into the graph. When you debrief after the meeting, the agent already knows what it told you going in. It can compare the outcome to the plan.

This isn't memory in the "remember what I said" sense. It's dynamic context building. Every agent run makes the graph more complete for the next one.

## Why typed facts matter

I've written about this in more detail on [the Dossium blog](<https://www.dossium.ai/blog/context-graphs-from-enterprise-search-to-relationship-intelligence>), but the short version: most memory systems treat everything as flat text with embeddings.

A preference, a decision, and a commitment all look the same - vectors in a store, distinguished only by cosine similarity.

The gap becomes obvious when you need to act on what you know.

A commitment has a temporal dimension - it can be overdue. A decision can contradict a previous decision. A delegation implies accountability. When an agent extracts "We'll deliver the POC by end of March" from a meeting transcript, that's a commitment with temporal validity, not a line of text in a memory store.

When the agent runs again in April, it can query all outstanding commitments for that account - not through fuzzy semantic search, but through typed fact retrieval with date filters.

That's the difference between "the agent remembers things" and "the agent maintains structured knowledge about your business relationships." It's the difference between a chat history and an institutional memory.

## The compounding loop

This is the part that gets me most excited. When your knowledge graph includes all your context - not just "memories" but email, Slack, transcripts, documents, calendar events - and when agent outputs go back into that graph as new content, you get a compounding loop:

![Article Image](<https://pbs.twimg.com/media/HFp64UYakAErXvo.jpg>)

We run scheduled synthesis agents - they execute on cadence, synthesizing across time-sliced and entity-pivoted views. A daily account digest. A weekly commitment audit. A monthly relationship map.

Each output feeds back into the graph with its own entity and fact extraction.
Most systems produce dead-end artifacts - a markdown file, a wiki page, a summary that sits in a folder. In our architecture, synthesis outputs are content in the graph. They become retrievable context for other agents. They feed the next synthesis cycle.

Every cycle makes the graph more complete. That compounding effect doesn't exist if memory is isolated in the harness. The harness sees what happened in the conversation. The graph sees what happened across the organization.

## Open isn't the same as portable

Harrison's prescription - use open harnesses so you own your memory - is good advice. But "open" just means you can see the code. It doesn't mean you can take your enriched knowledge somewhere else.

An open-source harness with memory in Postgres is better than a proprietary one. But your entities, facts, and relationships are still in a schema only that harness understands. If you leave, you get a database dump. That's data portability in the compliance-checkbox sense. It's not knowledge portability.

I think the bar should be higher than that.

Andrej Karpathy (@karpathy) just published a pattern he calls LLM Wiki - use an LLM to incrementally compile raw sources into a persistent, interlinked markdown wiki. Obsidian as the IDE, the LLM as the librarian, markdown as the substrate. 

The response has been massive, and for good reason: it validates something I think is underappreciated. Markdown isn't a format choice. It's an ownership decision. Plain text files in a folder you control, with wikilinks and backlinks, readable by any LLM, any editor, any framework - that's what real portability looks like.  Karpathy's pattern is manual - you feed it sources and the LLM compiles. 

What we're building at Graphlit is the automated version of that idea. Continuous sync of your knowledge graph to a user-owned markdown vault. Not a "download your data" button. A living, interlinked directory of markdown files - entities as wiki pages, facts in frontmatter, synthesis outputs as documents, all with wikilinks and backlinks - synced to a folder you control.

Open it in Obsidian. Point Claude Code at it. Read it with grep. Feed it to a completely different agent framework. If Graphlit disappeared tomorrow, your vault would still be there - not as a data dump, but as a functional knowledge base.

## The real question

The memory debate has been framed as: who should own the harness? I think that's the wrong frame. The harness is a runtime concern. It matters, but it's not where the value accumulates.

The value accumulates in the enriched knowledge - the entities, the typed facts, the relationships, the synthesis outputs, the compounding context that builds across every email ingested, every transcript processed, every agent run completed. That knowledge should exist independently of any single harness, any single model, any single vendor.

The test isn't whether your harness is open-source. It isn't whether your memory store is self-hostable. It's whether the enriched knowledge - the compounding value - can walk out the door with you as files you own.

That's what we're building toward.

Graphlit: https://www.graphlit.com
Dossium: https://www.dossium.ai

---


**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2043311350374338897  

**正文**

Agent Skills 设计的十个重要原则

十大原则指向单一纪律：沉淀！
遇到重复任务，沉淀为 Skills。注意到有效的判断，沉淀如何做出它。发现模式，沉淀模式让系统识别它。
获得 100x 结果的人并非更聪明，没有使用秘密模型。他们只是无情地将工作沉淀为 Skills ——然后让这些 Skills 大规模运行、随时间改进、复利增长。

原则1：Skills 是食谱，不是命令
错误示范："分析客户反馈并总结关键主题"——这是命令，只能使用一次，因为所有具体信息都硬编码在内。
正确示范：定义一个"主题分析" Skill，包含参数（语料库、研究问题、深度级别）和流程步骤（通读→识别模式→命名主题→提取案例→评估重要性→撰写综合报告）。
关键区别：一个设计良好的 Skill 可以处理数百种不同场景。构建一次，永久复用，只需更换输入参数。

原则2：教授思考，而非结论
反模式：在 Skill 中预设结论（"第四步：得出证据支持患者安全担忧的结论"）——这把 AI 变成了确认偏误的工具。
正模式：教授如何思考（"第四步：权衡支持和反对假设的证据。考虑时间线是否合理？是否存在替代解释？什么证据会改变你的看法？基于发现得出自己的结论"）。
检验标准：能否用这个 Skill 论证相反的结论？如果能用"调查举报者" Skill 既证明"此人被压制"又证明"举报毫无根据"，并根据证据得出不同答案，这才是真正的 Skill。

原则3：明确划分判断与计算的边界
判断（Judgment） ||  计算（Computation）
阅读文档并决定什么重要  ||  数据库查询
权衡相互冲突的考量  ||  算术运算
识别不同情境下的相同模式  ||  列表排序
直觉感知"哪里不对劲"  ||  日期范围检查
核心案例：让AI安排8人晚宴座位，它能出色完成——这是判断问题，涉及社交动态感知。但让 AI 安排800人座位，它会"幻觉"出一个优化算法，结果看似合理却违反约束（如把互相排斥的人安排在一起）。
原则：Skill 应显式编排这个边界——标记哪些步骤需要判断（让 AI 思考），哪些需要计算（调用工具）。不要让 AI 做算术，不要让计算器做解释。

原则4：魔力在于"通读一切"
AI 能做数据库查询做不到的事：阅读关于一个人的50份文档，发现矛盾，追踪故事随时间的变化，写出捕捉此人真实面貌的一页档案。
这就是"日志化"（Diarization）——将分散信息综合为结构化情报。
真实案例：会议组织者想了解申请者。数据库显示"AI 基础设施"公司。但1对1谈话暴露他们主要担心计费和成本归因。GitHub 提交显示80%近期工作在支付模块。
原则：构建通读一切并综合的 Skill。不要预过滤"相关"文档——直到读完你才知道什么相关。力量来自看到全貌后涌现的综合。

原则5：在正确时刻加载正确文档
作者分享了自己的失败教训：写了2万行指令，涵盖每个怪癖、教训、模式。结果更糟——AI 的注意力有限，信息过载导致关键指令被淹没。
解决方案：200行，但这不是指令，而是指针——当你做 X 时，加载文档 Y；当你看到模式 A 时，查阅 Skill B。
这是解析器（Resolver）：一个路由系统，在正确时刻加载正确上下文。开发者修改提示时，解析器在发布前加载评估指南；分析师询问客户时，解析器加载该客户历史。

原则6：智能向上推，执行向下推
三层架构模型：
· 顶层：Skill，丰富的流程、判断、智慧文档
· 中层：Harness，约200行代码，运行 AI 循环、管理上下文、调用工具
· 底层：Tool，快速、简单的程序，做一件事且可靠
反模式："胖框架"——40个工具定义占用上下文，业务逻辑嵌入编排，Skill 只是薄弱的附属品。
原则：智能向上推入 Skill，执行向下推入工具，保持框架纤薄。当 AI 改进时，所有Skills 自动改进；工具保持完美可靠，因为它们只是代码。

原则7：快而窄胜过慢而通用
通用工具是陷阱：
· 慢：通用浏览器自动化工具15秒完成截图-点击-等待-读取，专用工具100毫秒，相差150倍
· 臃肿上下文：40个工具定义在任务开始前就耗尽AI注意力预算
· 隐藏复杂性：当工具试图"智能"时，你把判断埋在看不见也改不了的地方
原则：构建快速、狭窄、"愚蠢"的工具。每个工具做一件事，半秒内完成，不解释不决策，只是执行。
解放性洞察：软件不再珍贵。需要做什么 X 的工具，就建一个只做 X 的工具，可能只需30分钟，AI 还能帮忙写。不需要时删除。工具是脚手架，不是建筑。

原则8：追逐"还不错"——改进的空间所在
用户对输出的三种反应：优秀、还行、糟糕。
原则：构建专注于 lukewarm 响应的学习循环。阅读 AI 产出，阅读用户反馈，问：差距在哪？然后修改 Skill 弥合差距。
真实案例：活动匹配 Skill 有12%"还行"评级。团队阅读反馈，发现模式——创始人按声称的行业匹配，但实际工作在不同领域。添加规则："当某人说 AI 基础设施但代码主要是计费，将其归类为 FinTech"。"还行"评级降至4%。这条规则来自审视"还行"与"优秀"之间的差距。

原则9：写一次，永远运行
简单检验：如果必须要求两次，你就失败了。
每个 Skill 都是系统的永久升级。与会被遗忘的巧妙提示不同，Skill 被保存、版本化、永久可用。凌晨3点运行，处理千次实例不疲倦。当 AI 模型改进时，你写的每个 Skill 自动改进—— Skill 编码流程，模型提供能力，更好的模型+相同的 Skill =更好的产出。
复利效应：想象一个拥有100个 Skills 的系统，每个处理某类工作。每个 Skill 可靠运行，模型改进时每个 Skill 改进。系统随时间积累能力，如同公司积累资产。但与实物资产不同，Skill 不贬值，它们复利。
思维转变：停止将 AI 交互视为对话，开始视为构建永久能力的机会。每次解决问题时问：这能成为 Skill 吗？

原则10：相同流程，不同世界
所有原则的结合：考虑 Skill /match——按某些标准配对或分组实体。参数：实体（匹配谁）、标准（什么是好匹配）、约束（必须遵循的规则）。
核心洞察：设计良好的 Skill 是接受参数的方法。参数提供具体世界（数据、标准、约束），Skill 提供流程（判断、步骤、智慧）。设计一次 Skill，然后在尚未想象的情境中永久调用。
这就是将 AI 从好奇变为力量倍增器的杠杆：一个 Skill，百种用例。设计食谱，烹饪不同餐食。

---


**作者** Will Yang（@Will_Yang_）  
**貼文連結** https://x.com/Will_Yang_/status/2043271610652877286  

**正文**

刚听了个扎心的事。
年初小龙虾火了，傅盛的Easyclaw火了，各种创业团队赶着去做一个类似的claw。
结果仅仅两个月，openclaw凉了，都到了Hermes时代了，我了解到的，很多团队都很迷茫，不知道何去何从。

---


**作者** Berryxia.AI（@berryxia）  
**貼文連結** https://x.com/berryxia/status/2043090485967987117  

**正文**

兄弟们，Claude Code 终于有「全代码库视觉地图」了！

全新开源工具 Code-review-graph直接本地生成项目完整关系图：

✅ 100% 本地运行，零云端  
✅ 自动映射整个仓库文件依赖  
✅ Claude 瞬间看懂每个文件怎么连在一起  
✅ 大幅减少 hallucination，上下文精准到爆  

再也不用手动喂一堆文件描述了，Claude Code 终于有“全局视野”了
兄弟们，Claude Code 终于有「全代码库视觉地图」了！

全新开源工具 Code-review-graph直接本地生成项目完整关系图：

✅ 100% 本地运行，零云端  
✅ 自动映射整个仓库文件依赖  
✅ Claude 瞬间看懂每个文件怎么连在一起  
✅ 大幅减少 hallucination，上下文精准到爆  

再也不用手动喂一堆文件描述了，Claude Code 终于有“全局视野”了
GitHub 直达👉 https://github.com/tirth8205/code-review-graph

---


**作者** Harrison Chase（@hwchase17）  
**貼文連結** https://x.com/hwchase17/status/2042981248482566391  

**正文**

ended up writing similar style post: your harness, your memory

https://x.com/hwchase17/status/2042978500567609738

cited @sarahwooders post a lot!

---


**作者** Morris（@Morris_LT）  
**貼文連結** https://x.com/Morris_LT/status/2043150913066725414  

**正文**

一个人的成长，本质上不是单点突破，而是一整套能力系统的协同进化。这22个能力，可以看作是从“认知 → 自控 → 行动 → 关系 → 格局”的完整闭环。

下面我们逐一拆解。

# 一、认知与思考能力（决定你看世界的深度）

## 1. 学习能力

不仅是“学得多”，更是“学得快、用得上”。
真正强的学习能力体现在：

- 能快速抓住重点，而不是被信息淹没
- 能把知识转化为行动，而不是停留在理解
- 能跨领域迁移，比如用商业思维解决生活问题

👉 本质：不是记忆，而是“吸收 + 转化 + 复用”

## 2. 思考能力

是你面对问题时，是否能独立形成判断。
很多人习惯接受现成答案，但真正的思考能力意味着：

- 会拆解问题（而不是情绪反应）
- 会从多个角度看问题
- 能在复杂中找到本质

👉 本质：不被带节奏，有自己的判断系统

## 3. 逻辑能力

决定你表达是否清晰、思路是否严谨。
具体表现为：

- 说话有结构（比如先结论后原因）
- 推理有因果，而不是跳跃
- 能把复杂问题讲简单

👉 本质：让别人“听得懂、信得过”

## 4. 批判性思维

不是抬杠，而是“有标准地判断”。
你会开始问：

- 这个观点的证据是什么？
- 有没有反例？
- 谁从中获益？

👉 本质：不轻信、不盲从

## 5. 系统思维

从“点”升级到“结构”的能力。
比如：

- 看到问题背后的链条，而不是单点
- 理解“短期行为”与“长期结果”的关系
- 知道一个改变会影响哪些环节

👉 本质：看全局，而不是只盯局部

## 二、自我管理能力（决定你能走多远）

## 6. 自律能力

不是靠意志硬撑，而是管理自己行为的能力。
包括：

- 抵抗即时诱惑（短视频、拖延）
- 持续做长期有价值的事
- 在没人监督时也能坚持

👉 本质：延迟满足

## 7. 时间管理能力

不是“忙”，而是“有效”。
关键在于：

- 分清重要 vs 紧急
- 把时间投在高价值事情上
- 减少无意义消耗

👉 本质：把时间用在能改变未来的地方

## 8. 情绪管理能力

不是没有情绪，而是不被情绪控制。
表现为：

- 不在情绪中做决定
- 能快速恢复状态
- 不把负面情绪传递给别人

👉 本质：稳定，是一种高级能力

## 9. 抗压能力

压力不是问题，承受不了才是问题。
真正的抗压是：

- 在压力中依然行动
- 不逃避困难
- 能从挫折中恢复

👉 本质：心理韧性

## 10. 目标管理能力

很多人努力，但没有方向。
强的人会：

- 设定清晰目标（短期+长期）
- 拆解路径
- 持续跟踪进度

👉 本质：让努力“有方向感”

## 三、行动与执行能力（决定你能不能做成事）

## 11. 执行力

最被低估但最关键的能力。
它体现为：

- 不拖延
- 有计划就行动
- 能把事情做完，而不是开始很多

👉 本质：把想法变现实

## 12. 决策能力

人生差距，很多来自决策。
好的决策不是完美，而是：

- 在不确定中权衡
- 敢承担结果
- 不反复犹豫

👉 本质：选择的质量

## 13. 问题解决能力

不是避免问题，而是解决问题。
优秀的人：

- 遇事先想“怎么办”
- 能快速找到关键点
- 善于利用资源

👉 本质：解决问题，而不是抱怨问题

## 14. 应变能力

世界变化很快，计划永远赶不上变化。
应变能力体现在：

- 能快速调整策略
- 面对不确定不慌
- 有替代方案

👉 本质：灵活，而不是僵化

## 15. 持续力（韧性）

大多数失败不是因为不聪明，而是没坚持。
它表现为：

- 长期投入
- 不因短期挫折放弃
- 能忍受“看不到结果”的阶段

👉 本质：时间的朋友

## 四、沟通与协作能力（决定你能走多快）

## 16. 表达能力

不是会说，而是说得清楚、有效。
包括：

- 结构化表达
- 根据对象调整说法
- 让别人愿意听

👉 本质：让价值被看见

## 17. 倾听能力

真正的沟通，从倾听开始。
它意味着：

- 理解对方，而不是等着反驳
- 捕捉信息背后的需求
- 建立信任

👉 本质：理解他人

## 18. 人际关系能力

不是“会交际”，而是建立长期信任。
包括：

- 可靠（说到做到）
- 有边界感
- 懂得互利

👉 本质：关系的质量

## 19. 影响力

让别人愿意跟随你。
来源包括：

- 专业能力
- 价值观
- 说服力

👉 本质：让别人“认同你”

## 五、认知升级与格局能力（决定你能走多高）

## 20. 自我认知能力

知道自己是谁，比努力更重要。
包括：

- 清楚优劣势
- 知道适合自己的路径
- 不盲目比较

👉 本质：认清自己

## 21. 反思能力

经验不会自动变成成长。
反思能力意味着：

- 总结得失
- 找原因
- 调整策略

👉 本质：让每次经历都有价值

## 22. 格局与视野

这是“天花板能力”。
表现为：

- 看长期，而不是短期
- 不计较小得失
- 理解更大的规则

👉 本质：你站在哪个层面看世界

## 最后总结一句话

这22个能力，其实可以归结为一个成长路径：

👉 看得清（认知） → 控得住（自我） → 做得到（行动） → 走得远（关系） → 站得高（格局）

---


**作者** 黄小木（@ai_xiaomu）  
**貼文連結** https://x.com/ai_xiaomu/status/2042947435216146684  

**正文**

我们公司ai编码现在有三派：Cursor、Codex 和 Claude Code。

Cursor：图形界面，最适合入门。但 API 额度不多，用完后只能用 Auto 模式了。

Codex：OpenAI 出品，可以集成在 VS Code 中，也可以作为命令行工具使用，代码补全和生成能力很猛，效率党首选。

Claude Code：Anthropic 的命令行工具，更偏极客，适合熟悉终端操作的开发者，擅长处理复杂任务和长上下文。

你感觉哪一个最好用？

---


**作者** Karan🧋（@kmeanskaran）  
**貼文連結** https://x.com/kmeanskaran/status/2043198826987897270  

**正文**

Deployment is THE MOST important skill in current AI era

Note: I am using AI and ML interchangeable

Building software today is not hard anymore.
With tools like Claude Code and Codex, you can build something meaningful in 48 hours.

> I did the same with @desysflow 🌀.
> It generates mermaid diagrams, HLD, LLD, and even non tech reports for stakeholders. Check this repo: github.com/kmeanskaran/desysflow-oss

So building is solved.

But shipping is not.

That is where most people fail.

Even if you have access to powerful AI tools, you still need to understand some core systems to actually deploy and run your AI projects in production.

You do not need everything.
You just need the right fundamentals.

## Why AWS

AWS has everything.

That is exactly the problem.

If you try to learn all of it, you will never ship.

Instead, focus only on what helps you deploy.

![Article Image](<https://pbs.twimg.com/media/HFrXD_-aUAA6K1M.png>)

# A. Backend Design

This is where your AI system actually becomes a product.

Most people overcomplicate this part. It is actually simple if you think in terms of flow.

## 1. REST APIs are simple, but not enough

![Article Image](<https://pbs.twimg.com/media/HFrXqZoaoAARP4_.png>)

For most ML systems, your backend starts with one main endpoint.

/prediction

User sends input, model returns output. Simple.

Then people think, let me add /train.

This is where things go wrong.

Training is not an API problem. It is a system problem.

Training takes time. Sometimes minutes, sometimes hours.
If you try to handle that inside a REST API, your system will break or timeout.

So instead of thinking “how to expose training”, think “how to orchestrate training”.

That shift changes everything.

## 2. Rate limiting is not about security, it is about survival

![Article Image](<https://pbs.twimg.com/media/HFrX2c3bUAASbm4.jpg>)

In AI systems, every request has a cost.

If your /prediction endpoint is open without control, you are basically giving away money.

One script, one loop, and your bill is gone.

Even worse, if training jobs are triggered multiple times, your infrastructure will get overloaded.

So rate limiting becomes mandatory.

Not just per user, but per API key and per IP.

It is not an optimization. It is protection.

## 3. You need to stop thinking synchronously

![Article Image](<https://pbs.twimg.com/media/HFrYBfUbkAAlQZd.jpg>)

Most ML tasks are not instant.

Training, batch jobs, heavy inference. These things take time.

If your API waits for everything, your system will feel slow and unreliable.

This is where a distributed task queue comes in.

Instead of doing the work immediately, you push it to a queue.
Workers pick it up and process it in the background.

Now your API becomes fast, and your system becomes scalable.

This pattern alone will take you very far.

## 4. Caching is your unfair advantage

![Article Image](<https://pbs.twimg.com/media/HFrYuggaoAAPwJZ.png>)

One thing you will notice in real systems is repetition.

Same prompts. Same inputs. Same outputs.

If you recompute everything every time, you are wasting compute and money.

Caching solves this.

Store previous results, and return them when the same request comes again.

This is extremely powerful in:

- LLM applications
- Recommendation systems
- Repeated inference scenarios

It makes your system faster and cheaper at the same time.

## 5. Not every prediction should be real time

This is a mistake many beginners make.

They assume everything must be instant.

But some predictions are heavy. Some depend on pipelines. Some take time.

Instead of forcing real time, make it asynchronous.

Accept the request, return a job ID, process it in the background.

Now your system is stable, and users still get results.

## 6. Model versioning is what saves you later

![Article Image](<https://pbs.twimg.com/media/HFrZC9iasAA6Z9g.png>)

In the beginning, you have one model.

Then you improve it. Then you retrain it. Then you tweak features.

Now you have multiple versions.

If you are not tracking versions, you are in trouble.

You will not know:

- Which model is live
- Which one performed better
- How to rollback

Model versioning brings control.

It lets you experiment without breaking production.

## 7.  Queue and Worker System

![Article Image](<https://pbs.twimg.com/media/HFrmO0fbwAAsz9p.jpg>)

A task queue alone is not enough. You need workers to actually execute the jobs.

Think of it like this.

Your API does not do the heavy work.
It only pushes tasks to a queue.

Workers are the ones that:

- Pick tasks from the queue
- Run training jobs
- Execute heavy inference
- Process data pipelines

This separation is powerful.

You can scale workers independently based on load.
More jobs → add more workers.
Less load → reduce workers.

This keeps your system efficient and prevents your API from getting overloaded.

In real ML systems, this pattern is everywhere.
API for control. Queue for scheduling. Workers for execution.

## 8. Monitoring is not optional

![Article Image](<https://pbs.twimg.com/media/HFrZ3UyaIAAnwpB.jpg>)

Once your system is live, things will break.

Not because your code is bad, but because real world data is messy.

You need to see:

- API latency
- Errors
- Model performance
- Resource usage

Without monitoring, you are guessing.

With monitoring, you are engineering.

## 9. Feature store solves a silent problem

![Article Image](<https://pbs.twimg.com/media/HFrZ_HLa0AAV-55.jpg>)

One of the most common hidden issues in ML systems is mismatch.

Your training data pipeline and your production pipeline are slightly different.

That small difference breaks your model performance.

A feature store ensures consistency.

You compute features once and reuse them in both training and inference.

This reduces bugs and improves reliability.

## 10. CI/CD makes you fast

![Article Image](<https://pbs.twimg.com/media/HFraT-IaIAAJK4g.jpg>)

If you are manually deploying every change, you will slow down very quickly.

Use GitHub Actions to automate your pipeline.

Push code → run tests → build Docker → deploy

Now your system evolves continuously.

You spend less time deploying and more time improving.

## 11. Security is usually ignored, until it hurts

![Article Image](<https://pbs.twimg.com/media/HFran1raIAEbZ_I.png>)

Most ML engineers ignore security in the beginning.

That works until it does not.

You need:

- Authentication
- Authorization
- API key control
- Secure secret handling

And most importantly, never expose your model endpoints openly.

Treat your model like an asset.

## B. Containerization

This is what makes your system portable.

## Docker simplifies everything

![Article Image](<https://pbs.twimg.com/media/HFraw6VaQAAo4Z0.jpg>)

Instead of worrying about environments, dependencies, and setups, you package everything into a container.

Now your model runs the same everywhere.

This is especially important in ML because dependency issues are very common.

With Docker, you remove that uncertainty.

## CUDA and GPU workloads

![Article Image](<https://pbs.twimg.com/media/HFra2zVbgAA02Y2.jpg>)

If you are using GPUs, things get more complex.

CUDA setup is painful if done manually.

Docker solves this as well.

Using NVIDIA CUDA images, you get pre configured environments.

This makes GPU deployment predictable and reproducible.

## C. Observability

Once deployed, you need visibility.

## Track your experiments

![Article Image](<https://pbs.twimg.com/media/HFrbEwaa8AAckvL.jpg>)

Use tools like MLflow and Weights & Biases.

They help you track:

- Metrics
- Parameters
- Model performance

This is how you move from guessing to knowing.

## Monitor your system

Use Prometheus and Grafana.

They give you visibility into:

- System health
- Resource usage
- API performance

## Your model will degrade

No model stays perfect.

Data changes. Users change.

This leads to:

- Data drift
- Concept drift

If you do not detect this early, your model silently fails.

So always monitor data and plan retraining.

## D. Kubernetes

![Article Image](<https://pbs.twimg.com/media/HFrbsj4a0AAhd-b.png>)

You do not need Kubernetes on day one.

But when you scale, it becomes useful.

It helps you:

- Deploy services
- Auto scale
- Handle failures

In ML, it is especially useful for multi node setups and GPU workloads.

## E. Terraform

![Article Image](<https://pbs.twimg.com/media/HFrbyWRbIAAuyXX.png>)

Setting up infrastructure manually does not scale.

Terraform lets you define everything as code.

Now your infrastructure is:

- Reproducible
- Version controlled
- Easy to scale

## F. AWS Usage

You only need a few services to get started.

- IAM for access control
- S3 for storage
- EC2 for compute
- ECR for Docker images
- EKS when you scale
- Billing alerts to stay safe
- AWS Bedrock for managed models

That is enough for most projects

## Why SageMaker should not be your first choice

![Article Image](<https://pbs.twimg.com/media/HFrb_siagAArn28.jpg>)

Amazon SageMaker is powerful, but it comes with tradeoffs.

It pushes you into:

- Notebook based workflows
- AWS specific ecosystem
- Higher costs

In early stages, flexibility matters more.

If you use Docker based deployment, you stay portable.

You can move to any cloud or even on prem later.

That freedom is important.

## G. Minimal Setup

You do not need a complex system to start.

Just use:

- FastAPI
- Docker
- Redis
- One EC2 instance
- S3

That is enough to deploy real AI systems.

## H. Flow Diagram

## F. I made an end-to-end project on MLOps

Stock Agent Ops: github.com/kmeanskaran/stock-agent-ops/

Which generates the Bloomberg style financial report by giving ticker id of US stocks as input. Entire ML pipeline generates including classic LSTM for time-series forecasting and agentic AI for generating report.

Read these articles:

[Part 1: Designing a Production-Grade Agentic MLOps System](<https://kmeanskaran.substack.com/p/part-1-designing-an-agentic-mlops>)

[Part 2: Deploying a Production-Grade Agentic MLOps System on AWS](<https://kmeanskaran.substack.com/p/part-2-deploying-a-production-grade>)

![Article Image](<https://pbs.twimg.com/media/HFrd7RObkAAoskw.jpg>)

Building AI is easy now.

Everyone can do it.

But deployment is where real engineering starts.

That is where systems break, costs rise, and complexity shows up.

If you focus on these fundamentals, you will be ahead of most people.

Start simple.
Ship fast.
Learn from production.

That is how you actually become an AI engineer.

Follow @kmeanskaran for more Applied AI/ML content

Subscribe to my Substack newsletter, kmeanskaran.substack.com

---


**作者** Berryxia.AI（@berryxia）  
**貼文連結** https://x.com/berryxia/status/2043270093728362995  

**正文**

Stanford 这堂 2 小时 AI 系统构建课，直接把 Claude 所有教程和 Prompting Thread 秒了！

强烈推荐：
“比你刷过的所有 Claude 教程都实用 10 倍”

里面讲的不是 prompt 技巧，而是 Stanford 真正教工程师如何从零构建可靠 AI 系统的完整方法论。

周末就刷这一个，绝对是你这周最有生产力的事！

我已经将其翻译为中英 文双语视频直接戳这里👇
Stanford 这堂 2 小时 AI 系统构建课，直接把 Claude 所有教程和 Prompting Thread 秒了！

强烈推荐：
“比你刷过的所有 Claude 教程都实用 10 倍”

里面讲的不是 prompt 技巧，而是 Stanford 真正教工程师如何从零构建可靠 AI 系统的完整方法论。

周末就刷这一个，绝对是你这周最有生产力的事！

我已经将其翻译为中英 文双语视频直接戳这里👇
总结了思维导图SVG高清版本：https://drive.google.com/file/d/1TD0to0xmtA8RMBGky98ic-W9sYLISDVu/view?usp=sharing 

---


**作者** 𝗿𝗮𝗺𝗮𝗸𝗿𝘂𝘀𝗵𝗻𝗮— 𝗲/𝗮𝗰𝗰（@techwith_ram）  
**貼文連結** https://x.com/techwith_ram/status/2042933925832724538  

**正文**

I think the title is a bit philosophical. Isn't it?

Don't worry, you will get it at the end. So, imagine a scene: you are standing in a bookshop. You pick up a novel. On the cover it says the author's name. You happen to know that author also teaches at a university in your city. That university is located near a park where there is a statue of a poet who was a contemporary of a character in the very novel you are holding.

You made five connections in a few seconds, entirely without effort. This is how human knowledge actually works. It does not live in isolated boxes. It is a dense, tangled network of associations, and our brains are extraordinarily good at navigating it.

The question is, how do we teach a computer to do the same thing?

# Why do traditional databases fall short?

Traditional relational databases organize information into tables: rows and columns. A library database might have a Books table, an Authors table, and a Publishers table. To connect them, you write a JOIN query; you tell the system, "Match the author\_id in Books with the id in Authors."

This works wonderfully for a fixed, predictable set of relationships. But it breaks down when:

- Relationships vary per entity: A book has an author. But a scientific paper has co-authors, an institution, a funding body, and a dataset. These cannot all live comfortably in the same table structure.
- The schema changes constantly: In a traditional database, adding a new type of relationship often requires restructuring the entire schema. In a graph, you simply add a new edge type.
- Traversing many hops is expensive: Finding "all books written by authors who studied under professors who won the same prize" requires multiple nested joins. In a graph, this is a natural path traversal.

## What is a knowledge graph?

It is a structured representation of real-world entities & the relationships between them, stored as a network (or graph) rather than a table. 

It consists of:

- Nodes (also called vertices or entities) These represent things: a person, a city, a concept, a product, a chemical compound. Each node has a unique identity.
- Edges (also called relationships or predicates) These connect two nodes and describe the nature of their connection. Edges are always directed and always labeled. "Marie Curie BORN\_IN Warsaw" is a different fact from "Warsaw BORN\_IN Marie Curie"—direction matters.
- Properties (also called attributes or literals) Both nodes and edges can carry additional data: a person node might have a birth year property; a "WORKED\_AT" edge might carry a start and end date.

![Article Image](<https://pbs.twimg.com/media/HFmYSlwakAclJQd.jpg>)

## The triple: the smallest unit of knowledge

The fundamental building block of a knowledge graph is the triple: a statement made of three parts.

![Article Image](<https://pbs.twimg.com/media/HFmWNWAa8AAW4m8.jpg>)

Three sentences. Eleven words. And from them, a machine can already infer that Marie Curie was born in the capital of a European country. That kind of chained reasoning is the superpower of the knowledge graph.

## Building a Knowledge Graph

A real-world example: a city neighbourhood

Let us build a small knowledge graph together. Imagine we want to represent the knowledge contained in this single paragraph:

> The Blue Door is a cafe on Elm Street. It is owned by Ramakrushna, who also owns the bakery next door called Morning Light. The Blue Door is known for its Ethiopian coffee, which is sourced from the Yirgacheffe region. Morning Light supplies pastries to three local hotels, including the Grand Elm.

![Article Image](<https://pbs.twimg.com/media/HFmUknvakAIaDzj.jpg>)

Notice something important: once this graph exists, questions that were never explicitly answered in the original text become answerable. For example: "Is Ramakrushna connected to the Grand Elm Hotel?" The text never says so directly, but the graph reveals the path: Ramakrushna owns Morning Light, and Morning Light supplies the Grand Elm. Two hops. One answer.

## Ontology: the grammar of your graph

A knowledge graph without an ontology is like a library without a cataloguing system. Ontology is the formal description of what kinds of things exist in your domain and what kinds of relationships are possible between them.

Think of it as the rules of the game. An ontology might say, "In our graph, a Person can OWN a Business, but a City cannot." This prevents nonsense from entering your data.

## Classes and instances

In an ontology, we distinguish between classes (categories of things) and instances (specific things). "Person" is a class. "Marie Curie" is an instance of that class. "City" is a class. "Warsaw" is an instance. This distinction lets us write rules at the class level that apply to every instance automatically.

Adding context with named graphs:

Sometimes a single fact is not enough. You need to say when something was true, or according to whom. This is done using named graphs essentially, a wrapper around a set of triples that adds provenance and temporal context.

> APJ Abdul Kalam President of India.

... is only valid from 2002 to 2007. The context provides the time range.

Without this temporal layer, your graph would assert things that are no longer true, with no way to distinguish current facts from historical ones.

## Querying the Graph

The real power of a knowledge graph emerges when you query it. Instead of asking, "Give me row 47 from this table," you ask questions that follow chains of relationships. Questions like:

1. "Find all scientists who were born in Europe and won a Nobel Prize in a natural science discipline." This traverses BORN\_IN, LOCATED\_IN, WON, and FIELD\_OF edges in a single query.
1. Which products are manufactured by companies owned by someone who also serves on the board of our company? ". This is a 4-hop traversal that would require multiple joins in SQL but is natural in a graph query language like SPARQL or Cypher.

![Article Image](<https://pbs.twimg.com/media/HFmfcv2akAMcwAb.jpg>)

Path query: Shakespeare -- \[2 hops\] -- Academy Award

Perhaps the most intellectually satisfying feature of knowledge graphs is inference: the ability to derive new facts that were never explicitly stored, purely by applying logical rules to what is already there.

A simple example

Suppose your graph contains these two facts:

Anna is parent of Ben

Ben is parent of Clara

You have also defined an ontology rule: "If X is parent of Y, and Y is parent of Z, then X is grandparent of Z."

The graph can now be derived without you explicitly adding it:

Anna is the grandparent of Clara

Scale this idea to millions of facts and hundreds of rules, and you have a system that can surface knowledge that no human explicitly put there.

I'm someone who works in the healthcare sector; let me give you an example from there: 

> A medical knowledge graph might store "Drug A inhibits Enzyme B" and "Enzyme B is required for the synthesis of Protein C, which is overexpressed in Cancer D." From these two facts, inference can automatically suggest that Drug A may be a candidate treatment for Cancer D, even if no researcher has yet made that explicit connection.

## Knowledge Graphs vs Other Data Models

![Article Image](<https://pbs.twimg.com/media/HFnyv14akAIy-Y_.jpg>)

## When should you choose a knowledge graph?

KG is not always the right tool. It shines in specific situations. Here is a simple rule: if the relationships between your data are as important as the data itself, consider a knowledge graph.

Use a knowledge graph when ::: Your data comes from many heterogeneous sources. Your schema evolves frequently. You need to traverse chains of relationships. You want to derive new facts by reasoning over existing ones.

Stick with a relational database when ::: Your data is highly tabular and stable. Your queries are simple lookups or aggregations. You need transactional guarantees (ACID) above all else. Your team is SQL-proficient, and your data fits the table model cleanly.

So have you heard about Google Knowledge Graph?

## Google Knowledge Graph

The most famous knowledge graph in the world is the one built by Google. Launched in 2012, it powers the information boxes you see on the right side of search results, those cards that tell you who a person is, what they are known for, where they were born, and what other entities are related to them.

When you search for "Albert Einstein," Google does not just find web pages containing that string. It retrieves a structured entity, a node in a graph that carries facts about Einstein and links him to other entities: his theories, his university, his colleagues, his era.

I mean, if you will hear the scale of it, you will be shocked.

It is estimated to contain tens of billions of facts across hundreds of millions of entities. It underpins not just search results, but also Google Assistant, Google Maps, and an increasing number of AI features.

Some of the most consequential knowledge graphs are invisible to the public. In biomedical research, knowledge graphs are used to integrate data from:

- Drug databases: Chemical structures, mechanisms of action, side effects, interactions.
- Genomic databases: Gene-disease associations, protein functions, pathways.
- Clinical literature Published research on treatment outcomes and case studies.

By connecting these sources in a single graph, researchers can identify unexpected drug repurposing opportunities, predict adverse drug interactions, and understand disease mechanisms that span multiple biological layers.

## How Does an Enterprise Knowledge Graph Work?

![Article Image](<https://pbs.twimg.com/media/HFnzkhEakAUP71a.jpg>)

## Final Thought

Knowledge graphs are powerful, but they are not magic. Understanding their limitations is as important as understanding their strengths.

No knowledge graph is complete. Wikidata, one of the largest public knowledge graphs, has millions of entities but enormous gaps; most people, places, and events in history are not represented or are represented incompletely.

More dangerously, knowledge graphs can contain incorrect facts. If the data source was wrong, or if the extraction process misread a piece of text, the graph will confidently assert something false. And because inference can propagate that error through the graph, one bad fact can corrupt many derived conclusions.

Hope you like the article; comment on what you feel or if you want to share something.

Follow @techwith\_ram for more such posts.

---


**作者** 看不懂的SOL（@DtDt666）  
**貼文連結** https://x.com/DtDt666/status/2043264380926853166  

**正文**

2026 年初，OpenAI 和 Anthropic 几乎同时发布了关于 Harness 的技术实践文章，LangChain 工程师 Viv 给出了一个简洁的公式来概括这个理念：Agent = Model + Harness。

模型提供智能，Harness

---


**作者** 花叔（@AlchainHust）  
**貼文連結** https://x.com/AlchainHust/status/2043224960110653739  

**正文**

哈，原来Claude Code之父 @bcherny 和我一样是非码农科班出身，以及，一样学的是「经济学」。难怪这产品我用得这么亲切。 

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2043240706156728322  

**正文**

我们常常看到，有些团队在挑选模式时，只顾着选听起来“高大上”的，却忽略了到底适不适合手头的问题。我们的建议是：从最简单的、能跑通的模式开始，观察它在哪里会遇到瓶颈，然后再逐步升级。

---


**作者** KK.aWSB（@KKaWSB）  
**貼文連結** https://x.com/KKaWSB/status/2043119101028274268  

**正文**

Nous Research开源了hermes-agent-self-evolution——一个让AI agent自己进化自己prompt的代码库，

背后引擎叫GEPA，ICLR 2026 Oral，比强化学习少用35倍数据，效果还高出20个百分点。

别再手调system prompt了。prompt工程这件事，正在被prompt自己取代。

https://github.com/NousResearch/hermes-agent-self-evolution

---


**作者** Aryan Mahajan（@aryanXmahajan）  
**貼文連結** https://x.com/aryanXmahajan/status/2043144598307180955  

**正文**

I replaced my $400K/year strategy team with an AI Executive Board...

7 frontier models. 5 countries. $0.30 per verdict. 34 seconds per decision.

→ No more shipping copy that one AI rubber-stamped
→ No more pricing decisions made with zero pushback
→ No more proposals that felt right but lost the deal
→ No more positioning gaps you only discover after the client says no

Just paste your draft → 7 models argue independently → 1 synthesis verdict delivered.

Here's how it works:
→ Claude (Anthropic) — strategic narrative + positioning
→ GPT (OpenAI) — structure + persuasion gaps
→ Gemini (Google) — logic flow + audience framing
→ DeepSeek — contrarian pressure-testing
→ Qwen (Alibaba) — market angle + commercial framing
→ Kimi (Moonshot AI) — risk flags + blind spots
→ MiniMax — final synthesis + verdict

No cross-talk. No model sees the other's answer. One chairman model reads all 7 and delivers the final call.

Built for decisions that cost you money if you get them wrong.
Runs in your terminal. One command. $0.30.

Results from real deployments:
→ $400K strategy function replaced completely
→ 34-second average verdict per decision
→ 7 independent opinions vs 1 AI hallucination
→ Catches the 1 line that quietly kills your sale

Want the complete system?

Like + comment "BOARD" + repost, and I'll DM it to you.
(must be following)

---


**作者** Carlos E. Perez（@IntuitMachine）  
**貼文連結** https://x.com/IntuitMachine/status/2043078828583514521  

**正文**

![Article Image](<https://pbs.twimg.com/media/HFp5PHGbYAAOaGq.jpg>)

# 1. Skills Are Method Calls, Not Prompts

The foundational insight:

> "A skill file works like a method call. It takes parameters. You invoke it with different arguments. The same procedure produces radically different capabilities depending on what you pass in."

The distinction:

Prompt Skill     Describes a task Describes a process   Single use Reusable   Specifies WHAT to do Specifies HOW to do it   Tightly bound to context Parameterized, context-independent

Example from essay:

Skill: /investigate
Parameters: TARGET, QUESTION, DATASET
Process: 7 steps (scope, timeline, diarize, synthesize, argue both sides, cite)

Invocation 1: Safety scientist + whistleblower question + discovery emails
  → Medical research analyst

Invocation 2: Shell company + donation tracing + FEC filings  
  → Forensic investigator

Same skill. Same seven steps. Different world.

Design implication: Write skills as procedures with clear parameter slots. The skill encodes judgment and process; the invocation supplies the specific domain.

## 2. Skills Encode Judgment, Not Just Steps

> "This is not prompt engineering. This is software design, using markdown as the programming language and human judgment as the runtime."

What skills contain:

- Process: The sequence of steps
- Judgment: When to do what, what matters, how to weigh
- Context: Domain knowledge needed to execute well
- Constraints: What NOT to do, edge cases, failure modes

Why markdown:

> "Markdown is, in fact, a more perfect encapsulation of capability than rigid source code, because it describes process, judgment, and context in the language the model already thinks in."

Design implication: Don't write skills as checklists. Write them as guidance for exercising judgment. The model needs to know not just WHAT to do but HOW to think about it.

## 3. The Latent/Deterministic Boundary

> "Every step in your system is one or the other, and confusing them is the most common mistake in agent design."

Latent space (model does this):

- Judgment
- Synthesis
- Pattern recognition
- Interpretation
- Quality assessment

Deterministic (code does this):

- Database queries
- Arithmetic
- File operations
- API calls
- Combinatorial optimization

The dinner table test:

> "An LLM can seat 8 people at a dinner table, accounting for personalities and social dynamics. Ask it to seat 800 and it will hallucinate a seating chart that looks plausible but is completely wrong."

Design implication: Skills should orchestrate the boundary. They tell the model what judgment to apply, then hand off to deterministic tools for execution, then return to judgment for assessment.

SKILL STRUCTURE:

1. LATENT: Interpret the task, understand what's needed
2. DETERMINISTIC: Query data, retrieve documents, compute
3. LATENT: Synthesize results, apply judgment
4. DETERMINISTIC: Format output, write files
5. LATENT: Verify quality, decide if done

## 4. Diarization as Core Capability

> "Diarization is the step that makes AI useful for real knowledge work. The model reads everything about a subject and writes a structured profile — a single page of judgment distilled from dozens or hundreds of documents."

What diarization produces:

- Structured profiles from unstructured sources
- Contradictions surfaced and held
- Temporal changes noted
- Analyst judgment, not database retrieval

Example output:

FOUNDER: Maria Santos
COMPANY: Contrail (contrail.dev)
SAYS: "Datadog for AI agents"
ACTUALLY BUILDING: 80% of commits are in billing module.
  She's building a FinOps tool disguised as observability.

Why it matters:

> "No SQL query produces this. No RAG pipeline produces this. The model has to actually read, hold contradictions in mind, notice what changed and when, and synthesize structured intelligence."

Design implication: Build diarization skills for your domain. They convert raw documents into structured intelligence that other skills can consume.

## 5. Resolvers Route Context

> "A resolver is a routing table for context. When task type X appears, load document Y first."

How resolvers work:

Task type detected → Resolver activates → Relevant skill/doc loaded → Model proceeds

Example:
  Developer changes a prompt
  → Resolver detects "prompt modification"
  → Loads docs/EVALS.md
  → Model knows to run eval suite before shipping

The CLAUDE.md lesson:

> "My CLAUDE.md was 20,000 lines... The fix was about 200 lines — just pointers to documents. The resolver loads the right one when it matters."

Design implication: Don't stuff everything into system prompts. Build a resolver that loads the right context at the right moment. Skills should be discoverable, not memorized.

Built-in resolver pattern:

> "Every skill has a description field, and the model matches user intent to skill descriptions automatically. You never have to remember that /ship exists. The description is the resolver."

## 6. The Three-Layer Architecture

> "Fat skills sit on top... A thin CLI harness sits in the middle... Your application sits on the bottom."

┌─────────────────────────────────────────────────────────┐
│  FAT SKILLS                                             │
│  Markdown procedures encoding judgment and process      │
│  "90% of the value lives here"                          │
├─────────────────────────────────────────────────────────┤
│  THIN HARNESS                                           │
│  ~200 lines of code                                     │
│  JSON in, text out, read-only by default                │
│  Runs model in loop, manages context, enforces safety   │
├─────────────────────────────────────────────────────────┤
│  DETERMINISTIC APPLICATION                              │
│  QueryDB, ReadDoc, Search, Timeline                     │
│  Fast, narrow, purpose-built tools                      │
└─────────────────────────────────────────────────────────┘

The anti-pattern:

> "Fat harness with thin skills. You've seen it: 40+ tool definitions eating half the context window. God-tools with 2-to-5-second MCP round-trips. REST API wrappers that turn every endpoint into a separate tool."

The principle:

> "Push intelligence up into skills. Push execution down into deterministic tooling. Keep the harness thin."

Why this matters:

> "When you do this, every improvement to the model automatically improves every skill, while the deterministic layer stays perfectly reliable."

## 7. Purpose-Built Tooling

> "What you want is purpose-built tooling that's fast and narrow."

Bad: Generic tools that do everything slowly

Chrome MCP: screenshot → find → click → wait → read
Time: 15 seconds per operation

Good: Specific tools that do one thing fast

Playwright CLI: each browser operation
Time: 100ms per operation

That's 75x faster.

The mindset:

> "Software doesn't have to be precious anymore. Build exactly what you need, and nothing else."

Design implication: Don't wrap existing APIs generically. Build narrow tools for your specific workflows. Speed compounds across every skill invocation.

## 8. The Learning Loop

Skills that improve themselves:

1. Skill executes on real tasks
2. Feedback collected (especially "OK" responses)
3. /improve skill reads feedback, identifies patterns
4. New rules written back into original skill
5. Next execution uses improved skill

Example from essay:

Input:  "12% OK ratings"
Process: /improve diarizes mediocre responses, extracts patterns
Output: New rule written to skill:

  When attendee says "AI infrastructure"
      but startup is 80%+ billing code:
      → Classify as FinTech, not AI Infra.

Result: Next event has 4% OK ratings

Design implication: Build skills that can propose modifications to themselves. The modification proposals should come from examining execution traces, not from abstract reasoning about the skill definition.

## 9. Skills as Permanent Upgrades

> "Every skill you write is a permanent upgrade to your system. It never degrades. It never forgets. It runs at 3 AM while you sleep."

The instruction:

> "You are not allowed to do one-off work. If I ask you to do something and it's the kind of thing that will need to happen again, you must: do it manually the first time on 3 to 10 items. Show me the output. If I approve, codify it into a skill file. If it should run automatically, put it on a cron."

The test:

> "If I have to ask you for something twice, you failed."

Design implication: Every repeated task should become a skill. The discipline is in codification, not execution.

## 10. Skill Invocation Patterns

Multiple invocations of the same skill structure for different purposes:

MATCHING SKILL (parameterized):

/match-breakout:
  Input: 1,200 founders
  Method: Cluster by sector affinity
  Output: 30 per room, sector-homogeneous

/match-lunch:
  Input: 600 founders  
  Method: Serendipity matching, cross-sector
  Output: 8 per table, no repeats, LLM invents themes

/match-live:
  Input: Whoever is in building now
  Method: Nearest-neighbor embedding
  Output: 1:1 pairs, 200ms, excludes prior meetings

Same underlying capability, different parameterization, completely different behavior.

Design implication: Design skills with configuration parameters that allow the same procedure to serve multiple use cases. Don't write three skills when one parameterized skill suffices.

## Summary: The Skill Design Checklist

STRUCTURE:
□ Skill has clear parameters (what varies per invocation)
□ Skill encodes process, judgment, and constraints (what's constant)
□ Skill has a description field for resolver matching
□ Steps alternate appropriately between latent and deterministic

BOUNDARIES:
□ Judgment stays in skill (latent)
□ Execution calls out to narrow tools (deterministic)
□ No business logic in harness
□ Tools are fast and purpose-built

LIFECYCLE:
□ Manual execution first (3-10 instances)
□ Codified after pattern stabilizes
□ Cron when appropriate
□ Self-improvement loop connected

CONTENT:
□ Written in markdown (model-native language)
□ Includes "how to think about this" not just "what to do"
□ Specifies what NOT to do and edge cases
□ Documents what it optimizes for

INTEGRATION:
□ Resolver can find it via description
□ Parameters have clear types/requirements
□ Output format specified
□ Connects to diarization where needed

## The Core Insight

> "That's how you get Yegge's 100x. Not a smarter model. Fat skills, thin harness, and the discipline to codify everything."

The model is already intelligent. The skill's job is to give that intelligence:

- The right context (via resolver)
- The right process (via skill steps)
- The right tools (via deterministic layer)
- The right feedback (via learning loop)

Skills are the compound interest of AI systems. Each one is a permanent upgrade. The discipline is building them.

Extracted from Garry Tan's "Thin Harness, Fat Skills" 

---


**作者** Roland.W（@rwayne）  
**貼文連結** https://x.com/rwayne/status/2042915701082722691  

**正文**

说话是一门艺术

如果私信是这个水平的

你以后去给任何大人物联系都能得到connection

（我不是大人物哈我是傻叉 

---


**作者** Berryxia.AI（@berryxia）  
**貼文連結** https://x.com/berryxia/status/2043092256958316815  

**正文**

Gary Marcus 又放大招了！

他直接把 Claude Code 源码泄露后的核心真相点破：

✅ Claude Code 是 LLM 时代以来最大进步
✅ 但它根本不是纯 LLM，也不是纯深度学习  
✅ 核心文件 print.ts 足足 3167 行，塞满了 if-then 分支 + 确定性符号逻辑  

Anthropic 在关键时刻还是靠经典符号 AI来保底，才让 Agent 真正可靠。

这波操作，等于直接验证了 Marcus 过去 20 多年一直喊的 Neurosymbolic AI（神经符号混合）路线！

Scaling 不再是唯一答案，混合路线才是未来

完整长文值得细读👇

---


**作者** Xiuyu Li（@sheriyuo）  
**貼文連結** https://x.com/sheriyuo/status/2042895889132363815  

**正文**

With the rise of Agentic RL, LLMs are no longer just one-shot Q&A systems. They are evolving into agents that repeatedly interact between reasoning and external tool use in multi-turn trajectories.

---


**作者** Alex Prompter（@alex_prompter）  
**貼文連結** https://x.com/alex_prompter/status/2043011383457964460  

**正文**

the LLM Council is the hottest AI concept right now. 
BUT there's a level most people are missing.
1.3 million views on Ole Lehmann's article alone. 
thousands of people running it to make real

---


**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2043205372522193284  

**正文**

如果你复制（抄袭）别人的帖子内容

X 以后会自动识别并标记 😅

会拿不到任何分成，还会被降权

这个有点牛逼了 

---


**作者** KK.aWSB（@KKaWSB）  
**貼文連結** https://x.com/KKaWSB/status/2043142026485731465  

**正文**

很多人不明白为什么日常有了Claude还需要Hermes或龙虾？ 因为开源。

Claude是最强大脑，但住在Anthropic的房子里。

Hermes跑在你自己机器上，数据不出本地，能接Claude也能接GPT、DeepSeek、本地模型——你选引擎，它负责执行。

封闭给你便利，开源给你自由。真正的玩家两个都用。 

---


**作者** Ksenia_TuringPost（@TheTuringPost）  
**貼文連結** https://x.com/TheTuringPost/status/2043004540685848576  

**正文**

Practical playbook for the organizational age of AI

AI-native has become one of those terms that can mean almost anything and, therefore, very little. Everyone now is trying to build something “AI-native.” Is it a startup with an AI feature? Or a company built on frontier models that burn thousands of tokens? Sometimes it simply means a team that uses ChatGPT a lot and feels great about it.

A better approach is to start with a definition. For us, an AI-native startup is a company designed so that machine intelligence can participate in the ordinary work of the business from the beginning.

That definition also captures what feels genuinely new right now: the boundaries between employees, workflows, and formal procedures are starting to break down, and some of the biggest gains are coming from reexamining the deep assumptions behind how work has long been siloed. Job definitions are shifting, and many people are understandably worried about what their role will look like in five years, or whether it will exist at all.

At the same time, evidence from the broader market offers a useful reality check. McKinsey’s 2025 survey found that workflow redesign is one of the strongest contributors to EBIT impact from generative AI, yet only a minority of organizations have fundamentally redesigned even part of how they operate. In other words, value is emerging where companies actually reshape work itself, rather than simply layering models onto old routines.

There is also an important transformation underway in the ecosystem: it is moving away from costly, brittle, one-off integrations toward shared interfaces such as skills, MCP, and AGENTS.md. We recommend the same thing over and over again while advising and helping build AI companies: keep agent systems simple, make context legible, and add complexity only when there is evidence that it helps. And the tools? Current tools are powerful, but they do not perform equally well everywhere. Startups are uniquely well positioned because they do not carry all the baggage of legacy systems. Greenfield environments usually give them a much cleaner runway than brownfield environments do. A new startup is one of the few places where you can still design the runway itself.

That changes the question from “Where do we use AI?” to something much more foundational: “What parts of the business should be built under the assumption that intelligence is abundant, uneven, unreliable, improvable, and deeply tied to data and feedback?” Let’s unfold all of it and look at building an AI-native startup through five principles we find important.

What’s in today’s episode?

- How we got here
- So what is an AI-native startup?
- The five principles of an AI-native startup

- The first principle: make the company machine-legible
- The second principle: choose tools by visibility and portability
- The third principle (one of our favorites): build expert loops before administrative layers
- The fourth principle: organize around outcomes, not handoffs
- The fifth principle: install evaluation, permissions, and review from the start

- Final thoughts

## How we got here

To see what is new, it helps to remember what previous organizational eras optimized for. Industrial firms were designed to coordinate labor, capital, and managerial oversight when information moved slowly and was expensive to gather. Later, the software era digitized the record of the firm, but it also formalized it into systems of record, schemas, suites, permissions, and departmental handoffs. Research on organizations has long treated information flow as central to structure, because communication frictions shape authority, hierarchy, and decision quality. That older logic still holds up – due to the habit. Companies are built partly out of who knows what, who can see what, and who is allowed to act on it.

In the last software cycle, much of that organizational logic disappeared into tools. A business became a stack of reports, databases, spreadsheets, CRMs, ticketing systems, file shares, and custom integrations. Context moved, but often awkwardly and at real cost. That is why the startup question now looks different from the classic stack question. Founders still have to choose platforms, but the harder problem is whether the company itself can be read by machines. Open standards reduce some lock-in, yet they also reveal a more uncomfortable form of dependency: undocumented judgment, hidden exceptions, private memory, and hallway context. The hallway conversation remains a fine social technology. It is a terrible form on long term knowledge retention.

So the real shift is this: in, let’s say, 2010, startups won by turning workflows into software. Now they increasingly win by turning parts of work into machine-readable, machine-executable, and machine-improvable systems.

That changes the nature of the company. Software is no longer only the product. The resulting report is no longer the measure of progress. How intelligence gets applied as information moves ever quicker is the business. The organization itself becomes part of the product surface.


## So what is an AI-native startup? Plus five principles when building one

An AI-native startup is a company designed so that machine intelligence can participate in the ordinary work of the business from the beginning.

AI-native startup’s knowledge is stored in forms machines can read. Its tools are reachable through standard interfaces. Its workflows leave traces. Its routines are evaluated. Its people spend more time on judgment, taste, and exception handling than on maintenance labor. That’s what makes an AI-native startup so effective if done right: removing the hidden chores that keep people from doing the work that actually moves the company.

Two clarifications here.

First, AI-native is an operating model, not a product category. A startup can sell AI and still run internally on siloed files, undocumented decisions, and manual coordination. Second, AI-native does not mean fully autonomous. In practice, AI-native means machine participation where it pays, human review where it matters, and clear rules for crossing that line.

The organizational promise is fairly concrete. If intelligence becomes cheaper and more available, some of the hidden and routine labor of a small company can shrink: internal research, first drafts, summaries, coordination, documentation upkeep, support triage, recruiting prep, and parts of planning. Evidence we see from firms investing in AI is flatter workforce structures over time, with fewer middle and senior layers relative to junior or single-contributor roles with expanded capabilities. That does not mean hierarchy vanishes or that experience stops mattering. It does suggest that some roles built mainly around relaying information become less central than roles built around judgment and ownership.

## The five principles of an AI-native startup

These are not necessarily The Ultimate Principles. You may come up with some additions to that as you build your own AI-native startup, but they are a useful way to clarify your thinking and a strong starting point to help you take off.

The first principle: make the company machine-legible

That’s the foundation.

Embrace markdown – simple text is your machine’s best friends.

That might sound trivial, but in practice it is usually such a mess, with so many missing pieces, that you have to stop and organize things intentionally. One bad habit that needs to be broken is stuffing everything into proprietary, structured silos. The previous generation of tools often required specialized formats, while the new generation relaxes some of those requirements: just put the material in and let the machine figure out more of it.

Some practical things to keep in mind: if you are recording conversations and calls, transcribe them with AI and store them. If you are making decisions, write them down or dictate them for transcription. If a customer conversation matters, store it somewhere searchable. If a process recurs, document it. If a tool contains critical knowledge, connect it.

Default to plain text or Markdown for durable knowledge. Structure still matters, but early on, legibility matters more.

We keep repeating it because it is crucial: if context lives only in people’s heads, it does not really belong to the company yet. Talking in Slack, for example, is better than talking in the elevator, because the computer can see Slack. Of course, people will still talk in person. But your AI cannot know what you were discussing in the elevator, even though that context may matter if you want your AI-native startup to operate at full capacity. Even wearables may become useful for capturing certain forms of operationally relevant data. If a fact is operationally important, it should not live only in somebody’s memory or in a post-meeting hallway conversation.

This is the first discipline of an AI-native startup: turn relevant work into artifacts. Notes, transcripts, plans, decisions, specs, summaries, and reviews all become part of a machine-legible knowledge layer.

BUT: this is also where many teams overcorrect in the other direction and say: fine, everything is text now, structure is dead, long live vibes. That is a great way to build the first AI-native junk drawer. Structure is still necessary. You need naming conventions, version history, ownership, access controls, clear states such as draft and approved, and a way to mark what is current versus deprecated. In an AI-native startup, context management becomes part of management.

The second principle: choose tools by visibility and portability

Founders often ask the wrong tool question. We hear it a lot → 

Read the full article here: https://www.turingpost.com/p/orgage3

This article is part of our The Org Age of AI series and is co-written by Will Schenk ([TheFocus.AI](<http://thefocus.ai/?utm_campaign=3-how-to-build-an-ai-native-startup-from-day-one&utm_medium=referral&utm_source=www.turingpost.com>)) and Ksenia Se. You can read the episode #1 AI Feels Powerful. So Why Is the ROI Still Missing? [here.](<https://www.turingpost.com/p/orgage1>) And #2 The Unsexy Truth of AI Adoption [here](<https://www.turingpost.com/p/orgage2>).

You can schedule a 1-on-1 consultation [here](<https://www.turingpost.com/upgrade>).

---


**作者** Chrys Bader（@chrysb）  
**貼文連結** https://x.com/chrysb/status/2043020014035570784  

**正文**

Despite what you see, long-term memory for conversational LLMs remains an unsolved problem.

The dream is: the model remembers what you said before and draws meaning across it over time. Not just recall, but interpretation, narrative, the kind of memory that makes a conversation feel continuous and cumulative across months or years.

Today, you can achieve an illusion of this dream. For days, or weeks if you're lucky. Until the LLM starts forgetting and the illusion breaks.

## Why does this happen?

As your conversation history grows, the memory system must decide what to capture, how to represent it, and what to surface on any given conversation turn. Every one of those decisions is lossy, opinionated, and non-deterministic.

Over time, either the corpus of information becomes too large to reliably search, or what the system remembers starts to drift from what was actually said due to repeated summarization. The model forgets because the system either can't hold a complete picture, or the picture becomes distorted.

In an ideal world, LLMs would have perfect historic context on the conversation turns that matter. Infinite attention across every word you've ever exchanged, with none of the cost or latency that would actually entail.

Since that's not possible, every memory system is an attempt to approximate it. Each with its own drawbacks.

There are ultimately only two ways to preserve information from a conversation:

1. Raw — original messages, stored verbatim
1. Derived — summaries, narratives, structured extractions

Every memory system is choosing a position on this spectrum. And neither extreme works.

Raw is lossless but inert. A pile of transcripts isn't understanding. The information is all there, but nothing is connected, prioritized, or interpreted. It's just buried in the source material.

Derived is compact and usable, but repeated derivation drifts from the source the way a photocopy of a photocopy degrades. You don't lose the information all at once. You lose it gradually, and can't tell exactly when it stopped being accurate.

## Won't infinite context solve this?

This is the most natural objection. Context windows keep getting bigger. Won't they eventually get big enough that we can just skip the memory system entirely and feed in the full history?

Not anytime soon. For two reasons:

1. Cost. Even if you could fit two years of conversation history into a context window, you'd be paying to process all of it on every single turn. The economics are brutal and they scale linearly with history. No consumer product survives that margin structure.
1. Degradation. Models get worse as the context window fills. Attention drops on information in the middle, overall reasoning quality declines, instruction following gets sloppier. You're paying more for worse performance.

Infinite context is just the extreme version of the raw path. And we've already established why raw alone doesn't work.

## The evaluation paradox

To know if a memory system is working, you need ground truth. But for real conversational memory spanning months or years, the ground truth is the entire history, which is larger than any context window and larger than any human can reasonably annotate.

Benchmarks like LongMemEval can test needle-in-haystack retrieval, but retrieval alone isn't memory. Memory is what happens when facts change, when old context gets superseded, when the significance of a conversation only becomes clear weeks later. The right answer depends on the full arc of the relationship, and the arc is always in motion. No benchmark captures arcs.

Synthetic datasets can't replicate these real-world examples at scale. The conversations lose coherence long before they reach realistic length, and even if they didn't, nobody can confirm ground truth for a synthetic relationship that evolved across a million tokens.

That's why every new memory approach you see land is a different set of trade-offs dressed up as a solution. Nobody can actually prove theirs works, because any judge you'd use to evaluate the full history has the same context limitations as the system it's judging.

## Where this leaves us today

The dream from the top of this piece, a model that remembers what you said and draws meaning across it over time, requires solving both sides of the raw/derived tradeoff simultaneously. Perfect preservation and perfect interpretation. Every current approach sacrifices one for the other.

This isn't a criticism of the people building these systems, it's an honest description of the constraint they're working within. Compression is lossy. Retrieval is imperfect. And the thing we actually want, meaning that accumulates and evolves, might be the hardest thing to formalize in a system that runs on pattern matching over tokens.

Memory for LLMs remains unsolved not because nobody's tried hard enough, but because the problem is very, very hard to solve.

We're getting closer. But we're not there.

# Deep Dive: How memory systems are built

> "There are no solutions. There are only trade-offs." — Thomas Sowell

Every memory system is a composition of choices across a set of axes. Different products pick different paths, but the axes themselves are stable:

1. What gets stored
1. When derivation happens
1. What triggers a write
1. Where it gets stored
1. How it gets retrieved
1. Post-retrieval processing
1. When retrieval happens
1. Who is doing the curating
1. Forgetting policy

When a new memory solution lands, you can lay it on this map and see exactly which choices it made and which ones it's punting on.

## 1. What gets stored

Memory systems hold onto either raw material, derived material, or some mix.

Raw:

![Article Image](<https://pbs.twimg.com/media/HFo5bZ6acAAoAdC.jpg>)

Derived:

![Article Image](<https://pbs.twimg.com/media/HFo5iVFaMAAdcTO.jpg>)

This is not an exhaustive list - there can be infinite types of derivations, but there are just some common ones.

## 2. When derivation happens

Derived artifacts have to be produced somewhere, and the timing is its own design decision.

![Article Image](<https://pbs.twimg.com/media/HFo5yK8bgAAZIde.jpg>)

## 3. What triggers a write

Every memory system has to decide when to capture something at all.

![Article Image](<https://pbs.twimg.com/media/HFo56x8akA4iVwk.jpg>)

Write-triggering is upstream of everything else. If you write the wrong things, no amount of clever retrieval will save you.

## 4. Where it gets stored

The storage backend constrains everything downstream.

![Article Image](<https://pbs.twimg.com/media/HFo6Qw3akAIxgKj.jpg>)

Most real systems use more than one. A common pattern is filesystem or document DB for the source of truth, vector DB for retrieval, and sometimes a graph DB on top for relationship traversal.

## 5. How it gets retrieved

Storage backend constrains retrieval strategy.

![Article Image](<https://pbs.twimg.com/media/HFo6b8xakAQ61ZT.jpg>)

Each strategy has a characteristic strength. Semantic search is good at "find me things conceptually like this." Full-text is good at exact phrases and proper nouns. Graph traversal is good at "what does the system know about this entity and everything connected to it." Filesystem navigation is good when the model is expected to actively explore.

## 6. Post-retrieval processing

Once you have candidates, you usually want to narrow further.

![Article Image](<https://pbs.twimg.com/media/HFo6mJlaEAAMXxY.jpg>)

Post-processing is where a lot of the perceived quality of a memory system actually comes from. Cheap retrieval plus smart re-ranking often beats expensive retrieval alone.

## 7. When retrieval happens

Three modes.

![Article Image](<https://pbs.twimg.com/media/HFo6xQEbEAAhZBL.jpg>)

These have very different failure modes. Always-injected pollutes context with irrelevant history. Hook-driven covers passive awareness but is expensive and can make the model perform memory rather than have it. Tool-driven respects the model's judgment but the model doesn't know what it doesn't know, so it often fails to fetch when it should.

## 8. Who is doing the curating

At every decision point in a memory system, something is making a choice. Who or what is it?

![Article Image](<https://pbs.twimg.com/media/HFo64cuakAUaQeq.jpg>)

Worth tracking as its own dimension because the cost, quality, and accountability profile of each curator is different. Systems that put the main model in charge of curation pay for quality on every turn. Systems that put cheap models in charge pay less but get sloppier decisions. Systems that lean on the user are accurate but add friction.

## 9. Forgetting policy

Every memory system has a forgetting policy, whether or not the designer chose one. The question isn't whether to forget, it's how.

What gets forgotten:

![Article Image](<https://pbs.twimg.com/media/HFo7IJMakAAV-H2.jpg>)

How forgetting propagates: 

Forgetting in a memory system isn't a single delete operation. If you stored raw turns and derived summaries from them, deleting the raw turns doesn't delete the summaries. If you extracted facts into a graph, deleting the source conversation leaves the facts orphaned. Real forgetting requires either tracking provenance (so you can cascade deletes) or periodically re-deriving everything from a smaller raw corpus, which is expensive.

When forgetting happens:

![Article Image](<https://pbs.twimg.com/media/HFo7W0_akAMPOUF.jpg>)

Forgetting is structurally hard for the same reason the rest of memory is: you don't know at write time what'll matter later, and you don't know at delete time what'll matter later either. Forgetting too aggressively means losing context the user wanted preserved. Forgetting too conservatively means accumulating an inaccurate model of the user that gets harder to correct over time. There's no right setting, only trade-offs.

## Common failure modes

Every memory system fails. The question is how, and whether the failure is recoverable. These are the patterns that show up most often in practice.

- Session amnesia
New session starts with no awareness of previous ones. The user is back to zero every time.
- Entity confusion
The model misidentifies or merges distinct entities during derivation. Two people with the same name become one, or categories bleed into each other.
- Over-inference
The model jumps to conclusions and encodes exaggerated or incorrect interpretations as facts. Without careful prompting, it fills gaps with plausible-sounding fabrications.
- Derivation drift
Chained summarizations compound small errors. Each derivation is slightly lossy, and the losses accumulate. After enough rounds, the derived memory diverges from what was actually said.
- Retrieval misfire
The system surfaces semantically similar but contextually wrong memories. Embeddings are close, but the meaning is different.
- Stale context dominance
Old, heavily-referenced memories crowd out recent ones. The system keeps surfacing outdated context because it was discussed more frequently.
- Selective retrieval bias
Retrieval only finds what matches the current query's framing. Relevant memories stored under a different topic or emotional register are invisible.
- Compaction information loss
When summaries replace raw turns, specific details vanish. The compression is lossy in ways that destroy the most useful information.
- Confidence without provenance
The system states a "memory" with full confidence but there's no way to trace it back to what was actually said. The user can't tell if this was stated, inferred, or hallucinated.
- Memory-induced bias
The system's responses are always colored by what it already knows about you. Sometimes that helps. But sometimes you want an uncolored take.

As you can see, building a working memory system is incredibly complex and gets harder in every dimension as the information grows. I hope this map helps you see the full design space, pick the right trade-offs for your product, and know which failure modes you're signing up for.

---


**作者** Tim✨（@timyangnet）  
**貼文連結** https://x.com/timyangnet/status/2043086842762014744  

**正文**

大家经常说的编排（Orchestration）Agent 似乎也不是必须，看 Anthropic 那个让 16 个 agent 并行两周不打架的案例：

这是 Nicholas Carlini 的编译器项目。最有意思的是他绕过了复杂的 agent 编排，回归了最朴素的如图所示 Bash Shell 循环：

🛠 同步协议：

任务池： 一个名为 current_tasks/ 的共享文件夹。

互斥锁： 智能体写入 .lock 文件标记“我在做了”。

分布式协同： 利用 Git 处理并行修改，连合并冲突（Merge Conflict）都由 Claude 自行解决。

🔄 单次 Loop 逻辑：

启动： 容器启动，拉取 upstream 最新状态。

寻路： Claude 扫描目录，认领没被锁定的任务。

交付： 完成编码，更新进度文件，git push 并释放锁。

current_task 从哪里来？所有 agent 都可以往里面提交任务，这个应该是写在 AGENT_PROMPT.md 启动规则里面。

对于长任务 agent 来说，这种设计模式省去了昂贵的编排管理成本，非常值得借鉴。

https://www.anthropic.com/engineering/building-c-compiler

---


**作者** George from 🕹prodmgmt.world（@nurijanian）  
**貼文連結** https://x.com/nurijanian/status/2043010699136503993  

**正文**

Karpathy dropped LLM wikis last week and everyone built one in 48hrs

PMs need this WAY more than anyone

you capture everything (research, frameworks, Shreyas threads, Lenny pods) but retrieve nothing. zero. your Second Brain is actually just a graveyard.

the LLM wiki pattern fixes this

point it at your folder, it groups by concept, writes synthesis articles, catches gaps you didn't see

ran it on my PM notes: found three sources saying the same thing about problem/solution space I never connected. also caught that I have 28 notes on strategy but only 2 on measuring if it worked

this gets you close.

---


**作者** Gabriel Lespérance（@GabLesperance）  
**貼文連結** https://x.com/GabLesperance/status/2042950334469787975  

**正文**

"I think I might bet the company on it." is what I said to my founding engineer the first time I brought up RLMs.
"Okay, but what's an RLM?" he asked.
"It's essentially a LM plugged into a Deno

---


**作者** Nicolai Ouporov（@nicoup）  
**貼文連結** https://x.com/nicoup/status/2042734098297614709  

**正文**

We supply simulation data and compute for a core part of the AI supply chain. The bet is partly that training models will become a more valuable and more common-place activity. 

I wouldn’t put us in the same group as Mercor and Handshake as we fundamentally deal with a different layer of the stack - as a research partner and infra provider.

---


**作者** Sean Cai（@SeanZCai）  
**貼文連結** https://x.com/SeanZCai/status/2023823195934249455  

**正文**

Excerpts from my State of Data (Feb 2026). Specifically on:
The bubble pops at the last mile: compute/data/talent can keep scaling while revenue stalls if adoption surfaces don’t exist.
AI is still

---


**作者** Sean Cai（@SeanZCai）  
**貼文連結** https://x.com/SeanZCai/status/2027459906543226921  

**正文**

Part #1, focusing on the fact that: subjective self serve post training infra is a thing.  Shorter reads given focus on particular topics, excerpted from upcoming State of Data March 2026.

RLaaS takes on new buzzwords as it develops.  A few months ago, I posted this maniacal diagram:

![Article Image](<https://pbs.twimg.com/media/HCL7SUvbEAY9E7E.png>)

The circled portion is indicative of the inflection point a lot of RL environments companies are making.  The ones without great research DNA (and are Type 2 data adherents) realize they can’t persist in the same category because they A) cannot produce the same contrived data volume and B) cannot be research first enough to anticipate and proactively respond to shifts in changing research demands.

The consequences of simultaneously not being research first and not being a volume winner is that you can neither compete against research first players like Fleet who define new shapes of data for new arbitrary research directions like long horizon & taste, while also not being able to provide substantial data in short timeframes like Handshake/Invisible/Turing/Scale/Surge.  It is the reason many are folding as of late and getting bought out by larger volume first players (with a couple acquisitions by neoclouds and labs hidden from the limelight).

A key part about these markets that not many realize is that spend is driven by arbitrary change in research direction.  Without the ability to anticipate arbitrary changes in research direction and the ability to “float atop the research zeitgeist,” one will end up overoptimizing for data production and infrastructure buildouts of a certain type that don’t persist beyond 3 months.  A key example is computer use infrastructure and one-shot coding tasks (as long horizon specs become more standardized).

Currently RLaaS engagements focus the shape of training sparse example problems in enterprise grade settings.  Applied Compute and Mercor’s [recent engagement](<https://x.com/mercor_ai/status/2016653132672201023>) emphasizes the fact that a linearly increasing performant model could be trained with “fewer than 1k high-quality data points from Mercor.”  This is ironic because this is the [explicit focus](<https://x.com/tbpn/status/2016665424742797376>) of newer neolabs like Flapping Airplanes, who espouse that they are focused on “frontier data efficiency.”

Let’s return to my definition of verifiability:

A huge reason why this notion of self-serve post training infrastructure for enterprises is taking off is because all signs point towards a persisting layer of economic activity between models and enterprise adoption:

- On prem and regulated industries can’t use cloud-based models out of the box
- Bespoke work flows that require subjectivity need a degree of post training to pass a minimum reliability threshold
- Post training is getting easier with [PI lab](<https://www.primeintellect.ai/blog/lab>), [Tinker](<https://thinkingmachines.ai/tinker/>), and the likes of CGFT
- Everyone is hiring FDEs on lab side, which should tell you that last mile implementation, as [championed](<https://www.ciridae.com/>) by my friend Jack Soslow, is the actual bottleneck
- Infra like Tinker shows signs of life and large large ML team buildouts at interesting F500s are gradually building post training sophistication.  In no where is this more obvious than Microsoft beginning post-training, whereas many would have written them and Amazon off 5 months ago.

Intrinsically, that everyone has bespoke work flows with high degrees of subjectivity tied to organizational cultures means that their workflows are extremely unverifiable by my earlier definitions of verifiability:

![Article Image](<https://pbs.twimg.com/media/HCL7baybcAAFpZb.png>)

because they intrinsically have both low veracity and proliferation of verification charecteristics.

Subjective self serve post training infra, in variations, is the explicit goal of many unnamed new neolabs started today, and most publicly represented in spirit by the likes of [Prime Intellect’s Lab](<https://www.primeintellect.ai/blog/lab>) and open source projects like [Harbor RL](<https://harborframework.com/>) (abstracting away complex reward rubric generation from masses of unstructured data for use in RL).  The most promising ones today combine top shelf research pedigree with extremely convincing FDE use cases in real world organizations.  Many die on the hills of integrating taste into unverifiable domains which are common in IRL use cases or developing models for low proliferation of verification business problems.  All are specialists in counteracting modalities of work with low asymmetry of verification.

For all its intents and purposes, though, many have forgotten Tinker.  In their quest to build out infrastructure for abstracting away post training, you must build the entire suite to develop stickiness or risk getting leapfrogged by other players.  For example - who still remembers that OAI is one of the few labs that have an API for DPO finetuning?

---


**作者** Sean Cai（@SeanZCai）  
**貼文連結** https://x.com/SeanZCai/status/2034059543500742772  

**正文**

A preview piece to my upcoming State of Data March 2026, exploring:

- The expansion of data acquisition in Scientific Discovery, Cybersecurity, and Taste domains
- New modalities of data markets - post-training in Audio, interweaved data, and flavors of egocentric data production
- RL as a service companies realizing they can sell data better than RL env companies

Biology, Security, and Taste

We progress on our onerous march to provide RL data for white collar domains and verify the unverifiable.  Researchers believe that, either by modeling enough or all of the common sophisticated white collar tasks domain by domain, we can get to some form of ASI and universal generalization.  Regardless, the procedural automation of long horizon white collar labor will result in valuable app layer products along the way, especially with N+1 tinkering by app layer companies who will post train and distribute.  The quest today looks like this:

![Article Image](<https://pbs.twimg.com/media/HDpsswqbQAAuZaY.jpg>)

Biology can be a euphemism for hard sciences like Chemistry/Electrical engineering/etc. in this example

And I want to talk about the unique challenges associated with higher difficulty task verification for non-coding based domains.

Of the white collar domains that are being tackled aggressively today (soon it will be every single one), these present unique challenges in a long horizon setting.  From my previous work, remember that this constitutes the definition of long horizon according to frontier labs:

![Article Image](<https://pbs.twimg.com/media/HDpsvD5bEAA-hbD.jpg>)

But biology, security, and taste also represent several issues with my old definition of verification.  Veracity of verification is low, proliferation of verification is locked up in enterprise workflows or not tracked by any web 2.0 systems, and asymmetry of verification is amongst the highest in the world.  Do biologists track their experimentation meticulously?  Can security, in an economic sense, be modeled successfully via a static benchmark given the attack surfaces constant updates?  Who provides human expertise as to verifying taste, and how can they be consistent?

![Article Image](<https://pbs.twimg.com/media/HDpswgga8AACBli.jpg>)

As with all other new unverifiable domains being tackled by researchers, the playbook of attack is being run.  Acquire high quality workflow data to benchmark model performance, optimizing for data that is hard and economically valuable.  Establish areas where models fail, and why.  Either synthetically, or via human data vendor support, scale up task sets for RL on those failure nodes to instill in models the behavior that they lapse on.  Learning signal is intrinsically tied to model failures here - but often “data realism” is left at the wayside in this evaluation.

But I couldn’t blame researchers here for neglecting it.  After all, for banal ground level tasks like working with toy financial models in initial researchers’ attempts to train models to be the most intern of a financial analyst, any hard problem we could come up with that looked vaguely financey probably had learning signal.  It was on this paradigm that data companies like Mercor scaled up processes where they had domain experts chat-gpt generate tasks, have experts do them, and cherry pick the ones that diverged from the expert-annotations to create “hard, north-star benchmarks.”  And it worked.

But can we do the same thing with longer horizon tasks and low veracity of verification domains?  Probably not - the nuanced intermediate reward signal that actually governs whether a task is done correctly or not in those is extremely difficult to simulate via contrived means.  How can we expect non-domain expert strategic project leads to corral under-paid “domain experts” to create long-horizon reasoning traces that model failure states, design rubrics that meaningfully constrict future actions, and do actually realistic, hill-climbable partial credit assignment?

Simply put, the multi-objective RL partial credit assignment problem that is needed to hillclimb actual biological, security, and taste-based model capability is near impossible to solve (long-term) with contrived data production.  This is another reason why so many data companies are pivoting to RLaaS (see Mercor’s recent moves with enterprise, partly inspired by this notion and a reorg dispute) - the enterprise is not only the end game to a larger TAM for post-training data, but also the only place to get good data to solve this problem.

In a way, we’re going full loop.  But herein lies another GRPO-style transition that is occurring soon that has long been entrenched in lab teams since the turn of the year - the acquisition of raw domain specific data itself rather than the reliance on boutique env vendors to acquire domain specific data.  Does Anthropic actually want you to make envs for them?  Probably not (see Taiga/Tundra) - what they really need is human judgement expertise formatted in a way such that they can craft reward rubrics and determine wherein lies learning signal for models to improve in a domain such as to power app-layer use cases.  In this way - benchmark companies directly impede the progress of AI app layer companies (Harvey, Rogo, Openevidence) by distilling the “domain expertise” of those app layer companies into metrics model companies will use to eat their products.

But just as N-1 models are destined to be one step behind frontier models always, at substantial cost/latency advantage, so should frontier labs’ models be as well behind the leading AI app layer companies.  We theoretically back Harvey, Rogo, and Openevidence for two reasons - we believe they have frontier domain expertise that allows them to be exposed to out of distribution problems/workflows in the industries that only their products will be custom ai-engineered to solve, and that they operate in regulated industries that OAI FDEs would find hard to navigate without a purpose built pre-existing corpus of relationships.  If any of these two assumptions falter - short those companies.

In this way, app layer companies in unverifiable domains should be quite happy to sell their N-1 data to labs (data only more than 6 months old, for example).  The marginal cost of post-training will go down (see [PI Labs](<https://www.primeintellect.ai/blog/lab>), [Tinker](<https://thinkingmachines.ai/tinker/>), [CGFT](<https://cgft.io/>)), so app layer companies can always turn the tiny edge in frontier domain expertise they have into a genuinely superior product to SOTA models, while the labs get to improve their base model capabilities and access realistic long horizon data.  App layer companies, obviously, also benefit from new model releases, especially if they’re able to quickly finetune/post-train with the small domain specific edges they have, and deploy quickly into regulated industries.  In this way - the app layer doesn’t get eaten up (as espoused by [token stream](<https://ethanding.substack.com/p/ai-subscriptions-get-short-squeezed>) doomer posts) but maintains a thinly coopetition-like edge with frontier labs.  I like this model of the world because it promises fair - but difficult - competition and forces app layer companies to justify their existence.

Who provides the conduits to connect app layer companies’ (and sophisticated legacy web 2.0 businesses’) data to frontier model producers?  RL environment companies are well suited to do this - the research forward players amongst here having built many [Antikythera Mechanisms](<https://seanzcai.substack.com/i/184829213/in-pursuit-of-new-antikythera-mechanisms>) to convert raw business context into post-training formats hopefully.  But then again, so are RLaaS companies, who must build these Antikythera mechanisms for particularly data sparse domains.  Altogether, there exists a strong cadre of scattered companies that can provide this, when the market realizes that this is the only source of accurate training data.

Bull RL env companies, in an environment where most investors still fixate on “durable revenues,” “customer concentration,” and the notion that labs will “use and discard you.”

History Repeats in other modalities

(but don’t fall pray to the law of small numbers in your extrapolations as VCs often do)

In the short term, there will be a larger opportunity set in the following modalities:

- Post-training for Audio
- Interweaved data for a new architecture that combines audio, video, and text
- Sim2Real gets better —> egocentric + teleop sets beecome valuable

Everyday looks more like Hari Seldon’s Psychohistory from the Foundation where, given a larger surface area of data pipelines in the world, one can leverage world models to predict larger population behavior.  This is similar logic to how folks say the rise of a Hitler-type figure was inevitable in a post-Marseilles Weimar Germany.

As a large cadre of talent hits their 1-year cliffs and leaves the giants which vertically integrated to 1B+ run rates in 2024, a feeling of uneasiness permeates the air.  On paper - they are leaving one of the fastest growing companies in history, with a resume that’ll allow them to raise tremendous amounts from any VC.  On the other hand, there are so many problems with scaling a data company that the likes of Mercor are running into - possibly many the same seen at Scale right before Alexander Wang jumped ship.  In particular:

- Contrived data production is COGS driven - every project has a variable cost that grows abhorrent with complexityYou pay people to go produce data.  People happen to be the best reward hackers to ever exist
- Contrived data production is not optimized for long horizonIf you pay people to go produce net new data, will we capture the nuanced intermediate reward signal here, especially considering that the people we pay are likely not to be at the top of their field?
- Incentive management is hard at large companiesThe AE/SDR model at data companies, owing to the oligopolistic nature of the industry, is actually confined to this role called Strategic Project Leads which own lab relationships
An earlier version of Mercor struggled with SPL commission with arbitrary assignment of lab accounts.  An SPL was basically an AE with no mandate to acquire new clients, only service existing ones.  Margin was already squeezed to the point where AE’s couldn’t derive startup-level ambition with financial incentives without extreme cultural alignment


We are still generally constrained in this market by the lack of good data - labs’ immense planned allowed expenditures for data aren’t met.  Who knows what’ll happen even as we begin approaching that limit?

Protege’s new data lab literally hits on all of my writing points that I’ve espoused for the last few months.  It talks about data standards, the pitfalls of contrived data production, and need for “actually good” training data for labs rather than not.  What strikes me the most is the manifestation of definitions around Type 1 and Type 2 data, whereas we can start assigning grades to classes of data whose diverse representations can more accurately proxy where learning signal comes from.  It turns out that the gold ore veins glitter in the dark, and the approach of Protege’s Datalab is giving us night vision to see this.

More on Protege later in my report on a more base level breakdown of a practical, pragmatic way to convert real world pipelines into actionable reward rubrics.

RLaaS realizes they can sell data

The broader implication for the data market is that if you can automate raw records → structured traces → RL environments with verifiable reward, you've turned every regulated industry's paper archive into potential post-training signal.  The bottleneck is the pipeline sophistication to convert messy real world records into something a reward function can score.  This is basically the kind of infrastructure that subjective self-serve post training needs to work in domains like healthcare, legal, and finance where the data is abundant but unstructured, and where contrived data production fails because you can't pay annotators to simulate 5-year patient care episodes with any fidelity.

Those building venture backed consultancies have now realized that they are privy to large stores of data which, given some anonymization pipelines and formatting, is incredibly valuable for lab sales.  The likes of OAI all the way to Augusta Labs have displayed rumblings in this direction, either through FDE or cryptic messages of “we help frontier labs improve their models with frontier human expertise.”

Another angle why RLaaS is uniquely positioned to work in data markets is the enduringly poor quality of benchmarks that actually map to real world economic value.  I’m especially excited by the possibility of dynamic benchmarks which are regularly refreshed by anonymized tasks created by Antikythera mechanisms from bespoke real world implementations, which can mitigate a lot of veracity/proliferation of verification difficulties, to make financial model use cases actually usable in the wild.  Increases in benchmarking frequency and realism can only reify our inherent ability to verify the unverifiable.

I'm working on something new.  As always, if you're a researcher/founder/member of an applied ai team who resonates a lot with what is said here, feel free to reach out.  

State of Data March 2026 on substack EOW.

---


**作者** Nishkarsh（@contextkingceo）  
**貼文連結** https://x.com/contextkingceo/status/2032098312376213655  

**正文**

If your AI agents keep retrieving the wrong context, explore HydraDB:

https://hydradb.com/

Grateful to our investors who backed this vision: @Sky9Capital, @JeffDean, @gokulr, @shyamalanadkat, @klyap_, @0xJsum, @laura_yao, @caldbeckj, @anshulbhide, and @SeanZCai.

@ashishkakran, @missionstcap, @prateeks, @MartinGTobias, @PickensAllison, @wadefoster, aekyi, @PuriSid, @mattsechrest, @CryogenicPlanet

---


**作者** Sean Cai（@SeanZCai）  
**貼文連結** https://x.com/SeanZCai/status/1907664149238186461  

**正文**

Posting and pinning this because I wish I had this when I was an 18 yr old.

My personal collection of programs and grants and fellowships to find high agency builders and aspiring investors.  

Still a WIP and will add more over time!

https://seanzcai.notion.site/5dba8bccc8cc4e7bb0e51bd59fa3dd8e?v=a4d69a4fdecf449ba46894e6dd25d9d1&pvs=4

---


**作者** Sean Cai（@SeanZCai）  
**貼文連結** https://x.com/SeanZCai/status/2042694720766513331  

**正文**

Below is a companion piece to my upcoming State of Data April 2026.  
The headline image is of the Russian Empire's Battle of Sinop (1853) in the Crimean War, one of the few significant naval

---


**作者** Malte Ubl（@cramforce）  
**貼文連結** https://x.com/cramforce/status/2042986384445837619  

**正文**

Vercel Sandboxes are now the fastest sandbox using real VMs as security boundary based on the @computesdk benchmark. The team has been absolutely cooking on this.

And the best thing: Because we have a unified Fluid Compute stack across Sandbox, Builds, and Functions these wins are often shared across the stack.

On the feature side there is a really exciting roadmap ahead as well.

My favorites (all driven by feature requests from our customers):
- Persistent sandboxes (in beta, GA immanent)
- The fully mutable firewall also becomes fully programmable

---


**作者** WquGuru🦀（@wquguru）  
**貼文連結** https://x.com/wquguru/status/2042994609937355007  

**正文**

2026 年 3 月的某个深夜，OpenClaw 的 Discord 服务器突然涌入大量用户抱怨：“为什么我的 agent 数据全没了？” 很快有人发现，罪魁祸首是一个叫 Hermes Agent 的新项目——它提供了一行命令 hermes claw migrate，直接把 OpenClaw 的用户数据、技能库、记忆全部“搬家”。

这个在中文圈被戏称为“爱马仕”的开源项目，两个月拿到超过 5 万 GitHub 星标（截至 4 月中旬已突破 5.6 万）。更有意思的是它的团队背景：CEO Jeffrey Quesnelle 此前在以太坊 MEV（矿工可提取价值）基础设施领域工作——那是个以“抢跑交易”和“暗池博弈”闻名的灰色地带。当 crypto 价格从高点腰斩近 50%，这帮人转战 AI，把 Web3 那套打法原封不动搬了过来：Hackathon 奖金包装成“竞赛”规避 X 平台的付费推广标签，Discord 里若有若无地暗示“未来可能空投”，社区自发刷贡献值。

我最初以为这只是又一个蹭热点的投机案例。但在调研了 15 个 Web3 创始人转型 AI 的故事后，我发现了一个反常识的结论：那些成功者，恰恰是最不“正统”的那批人。

OpenSea 前 CTO Alex Atallah 做的 OpenRouter，18 个月估值冲到 5 亿美元，月处理超 30 万亿 token；以太坊挖矿公司 CoreWeave 转型 AI 算力，2026 年 4 月刚拿下 Meta 210 亿美元的超级订单，市值突破 430 亿美元。与此同时，那些看起来“更正规”的 AI 创业公司——比如 a16z 领投 3300 万美元的 [Yupp.ai](<http://yupp.ai/>)——反而在一年内关门大吉。

这里面到底发生了什么？

## 一、钱的错位：2000 万美元不知道怎么花

2023 年，硅谷流传着一个段子：有 Web3 创始人在 2021 年拿到 Paradigm 的 2000 万美元，到 2023 年团队从 40 人裁到 12 人，账上还躺着 1400 万美元。每月只烧 15 万，照这速度能活 7 年——但问题是，不知道该做什么。

这不是个例。Crypto 冬天让大量 Web3 项目陷入尴尬境地：钱还在，但原来的商业逻辑崩了。与此同时，AI 基础设施在 2024 年吸走了全球 VC 资金的三分之一，约 131.5 亿美元涌入这个赛道。一边是“有钱没方向”，一边是“有方向缺钱”——这种错配创造了套利空间。

但真正让 Web3 创始人有机会的，不是钱，而是另一个更隐蔽的变化。

2026 年，AI 投资圈正在形成一个新共识：当 GPT-5 和 Claude 4 的能力差距小于 5%，当 Cursor 让实习生一周就能复刻你的产品，VC 不会再为“功能创新”买单。护城河正在从“软件能力”转向“时间买不来的东西”：物理基础设施要 3 年建设周期，专有数据飞轮要 5 年积累，监管牌照要政府关系，大额融资要信用背书。

这些恰好是 Web3 创始人在上个周期积累的——GPU 矿场、社区网络、金融工程能力、监管灰度操作经验。OpenAI 再聪明，也不可能 6 个月建出一座数据中心；Anthropic 再有钱，也买不来一个 10 万人的活跃社区。而这些，正是 CoreWeave 和 Hermes 手里的牌。

## 二、CoreWeave：一个对冲基金经理的豪赌

Michael Intrator 的故事听起来像赌徒传奇，但他的履历恰恰相反。哥伦比亚大学公共事务硕士，曾在天然气对冲基金 Hudson Ridge Asset Management 做 CEO,2017 年创立 Atlantic Crypto 进入以太坊挖矿。

2019 年 crypto 崩盘时，所有矿场都在清算 GPU 回血，Intrator 却做了一个决定：不卖，而且要重新定义这些机器的用途。他在后来的公开采访中解释过这个逻辑：“GPU 不是挖矿机，它是可编程的计算单元。它的价值取决于市场需求，而不是我们最初买它来干什么。”

这是典型的金融思维——资产的价值不在于历史成本，而在于未来现金流。2022 年，他押注 1 亿美元采购 Nvidia H100 芯片，那时 ChatGPT 还没发布，多数人觉得他疯了。但到 2023 年 AI 算力需求爆发时，CoreWeave 的 GPU 从“沉没成本”变成了“战略资产”。

更狠的是后面的操作。CoreWeave 把客户合同、GPU 和数据中心打包，用 Meta 和 OpenAI 的长期订单做抵押，融资 85 亿美元。这种“把基础设施当金融产品”的玩法，AWS 学不来——因为亚马逊没有在 crypto 冬天扛过一轮生死，也没有那种“把一切资产证券化”的本能。

2026 年 4 月，CoreWeave 市值突破 430 亿美元，Intrator 进入福布斯富豪榜。但这个故事有个细节值得玩味：CoreWeave 早期融资时，Nvidia 既是供应商又是投资人——它投资的公司，又回过头来买它的芯片。这种“循环融资”在 2026 年初引发了 FTC 的关注，有观点质疑这是否构成利益输送。

CoreWeave 的回应是：客户是 Meta、OpenAI，不是 Nvidia，如果服务不行，Meta 不会签 210 亿美元的合同。话虽如此，但监管的阴影已经浮现——当一个行业的头部公司开始形成“芯片厂商-云服务商-大客户”的封闭循环，后来者的空间还有多大？

这条路的窗口正在关闭。CoreWeave 和 Crusoe Energy 已经占据头部位置，后来者要么找更细分的市场（比如只做推理不做训练），要么就需要更深的政府关系和更大的资本体量。如果你手上没有现成的 GPU 资产，现在入场基本没戏。

## 三、OpenRouter：一张旧地图的新用法

Alex Atallah 离开 OpenSea 的时候，外界都觉得可惜。2022 年 7 月，NFT 市场还在顶峰，OpenSea 估值 140 亿美元，他作为联合创始人兼 CTO，身家超过 20 亿美元。但他选择了离开。

从公开信息看，Atallah 在 OpenSea 后期花了大量时间处理 API 对接问题——Ethereum、Polygon、Solana、Flow，每条链的标准都不一样，每个钱包的接口都不一样。这个经历成了 OpenRouter 的起点。

2023 年初，OpenRouter 上线。产品逻辑简单到不像一个价值 13 亿美元的公司：提供一个 API，接入 400 多个 AI 模型，自动选最优的、最便宜的，统一计费。听起来就是个“API 聚合器”，但魔鬼在细节里——这本质上是把 OpenSea 的“NFT 市场”逻辑平移到“LLM 市场”：双边网络、路由优化、价格发现、流动性聚合。

数据很说明问题。OpenRouter 在 2025 年 5 月时年化收入 500 万美元，到 2026 年 3 月已经处理超过 30 万亿 token/月，服务 500 万开发者。这个增长速度远超多数纯 AI 工具公司，因为它不是在做工具，而是在做基础设施。

但这里有个值得注意的现象。据行业观察，OpenRouter 的早期用户中，有相当比例来自成人内容开发者——因为 OpenAI 和 Anthropic 都有严格的内容审核，但 OpenRouter 接入的一些开源模型没有这个限制。这引发了关于“中立基础设施”的讨论：平台是否应该像 AWS 那样不审查用户内容？

2026 年 2 月，有媒体报道 OpenRouter 被用于生成虚假信息，OpenRouter 随后宣布加强内容监控，但同时强调不会像 OpenAI 那样严格审核，否则会失去差异化价值。

这是个典型的平台困境——你要足够开放才能吸引用户，但太开放又会引来监管麻烦。Web3 创始人对这个平衡点的把握，比传统 SaaS 创始人要老练，因为他们在 DeFi 和 NFT 时代已经踩过无数次坑。

这条路的窗口还开着。AI 模型的碎片化才刚开始，等模型数量涨到 1000 个，路由器的价值会更大。但前提是你得有平台产品经验，理解双边市场的网络效应，知道怎么在“开放”和“管控”之间走钢丝。

## 四、Hermes：灰度地带的增长实验

Hermes Agent 的 Discord 服务器里，有个频道叫“contribution-tracking”，实时显示每个用户的“贡献值”：提交代码、回答问题、发 Twitter、参加 Hackathon，都有对应的积分。没有人明说这些积分有什么用，但气氛很微妙——就像 2021 年 Uniswap 空投前夕，所有人都在“刷交易量”但没人承认。

社区里流传着一种默契：“官方没说，但你看团队背景……懂的都懂。”

这就是 Hermes 的玩法。CEO Jeffrey Quesnelle 和 Nous Research 团队有着 Web3 背景，他们把那套社区运营的方法论，原封不动搬到了 AI Agent: 

Hackathon 的合规外衣。 要求参赛者在 X 上发 demo 视频并 tag 官方账号，奖金 7500/2500/500 美元，一期收到 187 份提交。这既规避了 X 平台的“付费推广”标签（因为是“竞赛奖金”），又制造了海量 UGC 内容。官方多次声明“从未付费推广”——技术上确实没错。

一键迁移的“抄家”命令。 hermes claw migrate 直接导入 OpenClaw 的所有数据——技能、记忆、设置。OpenClaw 的创始人在 Twitter 上抱怨这是“不道德的竞争”，但开源协议让他们没有任何法律手段。Hermes 团队的立场是：这只是让用户更容易选择，符合自由市场逻辑。

空投预期的暧昧游戏。 官方从未承诺发 token，但也从未否认。Discord 里有专门的“tokenomics-discussion”频道，管理员的态度是“我们专注于产品，其他的以后再说”。这种“薛定谔的空投”，既保持了激励效果，又规避了监管风险。

两个月，超过 5 万 GitHub 星（截至 4 月中旬已达 5.6 万）, Discord 社区数万人。这个增长速度在纯 AI 开源项目中也是很快的，在 Web3 老炮儿眼里，这只是基本操作。

但这里有个问题值得思考：如果产品本身不够硬，这套打法能撑多久？从技术角度看，Hermes 确实有创新（自我进化的技能系统、更好的记忆管理），但没有到“碾压”的程度。它的快速增长，有多少来自产品，有多少来自营销，很难说清。

更大的风险在于平台政策。2026 年 3 月，X 平台更新了社区准则，明确将“通过竞赛奖金规避付费推广标签”列为违规行为。Hermes 的 Hackathon 即使是在这之前办的，但如果继续这么玩，可能也还是会遇到麻烦。

团队的态度似乎是：规则总是滞后的，在规则明确之前抓住机会。这很 Web3，也很危险。

## 五、那些死在沙滩上的

并不是所有人都能成功转型。

[Yupp.ai](<http://yupp.ai/>) 的故事很典型。创始人是 Coinbase 前 VP Engineering, a16z 领投 3300 万美元，产品是“AI 模型评测平台”——让用户对比不同模型的输出质量。听起来很合理，2025 年初拿到 130 万用户。

但一年后关门了。

从事后分析看，问题在于：当 OpenAI 在 ChatGPT 里直接加了模型对比功能，Yupp 的差异化价值就被削弱了。更要命的是，他们没有数据飞轮——用户的评测数据很难沉淀价值，因为每个模型每周都在更新。

这是典型的“护城河错配”。AI 应用层的竞争已经是红海，OpenAI 和 Anthropic 的迭代速度让创业公司的功能优势几个月就消失。2026 年 VC 圈有个共识：“越接近可防御的基础设施，越容易拿到大额支票。”纯应用层？除非你有极强的垂直纵深，否则别想了。

另一个案例是 Pulse DePIN，一个“健康数据奖励”项目。用户戴智能手环，上传健康数据，赚 token。2025 年融了 800 万美元，2026 年 4 月宣布关闭硬件业务，理由是“硬件行业的资本要求过于苛刻”。

关闭公告里写道：“我们低估了供应链的复杂度。从设计到量产，光是找到靠谱的代工厂就花了 8 个月。等我们的手环出货时，市场上已经有 20 款类似产品。”

这是“资本错配”。DePIN 类项目看起来很性感——Web3 的 token 激励 + AI 的数据价值，但硬件成本、供应链、监管复杂度远超预期。除非你像 CoreWeave 那样有金融工程能力做资产证券化，否则硬件创业就是深坑。

还有一类失败更隐蔽：那些“bolt on AI”的项目——给原来的 Web3 产品加个聊天功能，以为蹭上热点就能融资。有 NFT 交易平台在 2025 年加了“AI 推荐”，宣称“用 GPT-4 帮你发现潜力 NFT”，但投资人的质疑很直接：“护城河在哪？OpenSea 加个 API 调用就能做同样的事。”

这些失败案例有个共同点：他们把 AI 当成“热点”而不是“能力”。成功的 CoreWeave、OpenRouter、Hermes，都是在问“我的 Web3 能力在 AI 时代还能干什么”，而不是“我怎么蹭 AI 的热度”。

## 六、四个不那么舒服的问题

如果你是 Web3 创始人，正在考虑转 AI，我建议先问自己四个问题。这些问题没有标准答案，但能帮你看清现实。

第一个问题：你手上到底有什么？

不是“你想做什么”，而是“你已经有什么”。CoreWeave 有 GPU 矿场，OpenRouter 有平台产品经验，Hermes 有社区运营能力。如果你只有钱，没有上述任何一项，那你的优势在哪？

“我可以学”这个想法很危险。AI 不等人。等你学会供应链管理，CoreWeave 已经签了 210 亿美元的合同；等你学会社区运营，Hermes 已经 5 万星了。

第二个问题：你的护城河能撑多久？

用“时间买不来”测试：你的优势是否需要 3 年以上才能被复制？物理基础设施是，专有数据飞轮是，政府关系是。纯功能创新？大模型 6 个月就能模仿。

2026 年的 VC 不会为“功能创新”买单，他们要的是“时间护城河”。如果你的优势可以被 GPT-5 一个 API 调用就复制，别指望拿到大额融资。

第三个问题：你的团队基因匹配吗？

CoreWeave 的 CEO 是对冲基金出身，所以他能做资产证券化；OpenRouter 的创始人做过 NFT 市场，所以他理解双边网络；Hermes 的团队来自 MEV，所以他们会玩灰度营销。

你的团队基因是什么？如果是纯技术背景，没有商业 sense，坦白说，加入一家成熟 AI 公司可能比创业更合适。AI 创业不缺聪明人，缺的是懂商业、懂市场、懂人性的人。

第四个问题：2026 年，还来得及吗？

基础设施层的窗口正在关闭，CoreWeave 和 Crusoe 已经占据头部；中间层（路由/工具）还有机会，但竞争在加剧；应用层？除非你有极强的垂直纵深，否则别想了。

时间窗口可能只有 12-18 个月。算不清楚，就别动。

## 2026 年的新变量：监管风险正在上升

一个容易被低估的风险正在浮现：AI 基础设施的“主权化”趋势可能重塑竞争格局。

2026 年 4 月 FTC 的“互操作性裁决”试图防止云锁定，但 Meta 与 CoreWeave 的 210 亿美元订单（锁定到 2032 年）显示，物理基础设施的规模效应本身就是天然垄断。监管机构担心的“Nvidia-CoreWeave 循环融资”（Nvidia 投资买自己芯片的公司）可能引发新一轮反垄断审查。

对 Web3 创始人的启示：如果你的 AI 项目依赖单一云供应商或芯片厂商，需要提前布局多元化策略。 去中心化训练（如 Hermes 在 Solana 生态的 Psyche 网络上训练模型）可能同时具备技术和合规价值——当监管压力增大时，分布式架构可能成为重要的防御手段。

## 结语：不是所有人都该上牌桌

“君子不立危墙之下。” 写到这里必须说一句反共识的话：并非所有 Web3 创始人都应该转 AI。

如果你的 Web3 项目本身有清晰的产品市场契合度、正在盈利、团队稳定，那么“蹭 AI 热点”可能是错误的选择。真正成功的案例（CoreWeave/OpenRouter/Hermes）都有一个共同特征：他们发现了自己的 Web3 能力在 AI 时代有更大的施展空间。

CoreWeave 的 CEO 说得很清楚：“我们从一开始就把 GPU 当成灵活的基础设施，而不是单一用途的 crypto 设备。”这种“资产流动性思维”才是核心——关键在于重新定义已有资产的价值边界，而非盲目追逐热点。

2026 年的 AI 创业已经进入“中局”——基础设施的竞争格局、模型层的头部集中、应用层的价值分配，都在快速固化。留给 Web3 创始人的窗口期可能只有 12-18 个月。但如果你拥有 GPU 资源、社区运营能力或市场设计经验这三项能力中的任何一项，现在仍然是合适的入场时机。

记住这个公式：Web3 资产 × AI 需求缺口 × 时间护城河 = 可防御的转型路径。

三个变量缺一不可。算清楚了再动，算不清就别动。

当 Hermes Agent 用 2 个月挑战 OpenClaw 的市场地位，当 OpenRouter 用 18 个月做到 13 亿美元估值，当 CoreWeave 用 crypto 挖矿的 GPU 撬动 430 亿美元市值——这些案例说明：在 AI 这个看似被巨头主导的领域，Web3 创始人掌握的特定能力——社区运营、资产流动性思维、市场机制设计——确实能够创造显著价值。

关键在于，清楚自己拥有什么能力，以及在哪个场景下这些能力最有价值。

> 从会用 Agent，到 做出 Agent PoC ，通过AgentWay助力团队技能转型🫱 https://agentway.dev/zh

---


**作者** hoeem（@hooeem）  
**貼文連結** https://x.com/hooeem/status/2043027527673729309  

**正文**

POV: you’re the only Claude architect at work 

(your annoying colleagues will be fired) 

---


**作者** BuBBliK（@k1rallik）  
**貼文連結** https://x.com/k1rallik/status/2043013319045325030  

**正文**

🚨do you understand what just happened with Claude..

Anthropic quietly cut Claude's thinking depth by 67%.. didn't announce it.. didn't explain it.. an AMD AI Director had to dig through session logs just to prove it happened.

median reasoning dropped from ~2,200 to ~600 characters.. API calls went up 80x.. meaning Claude thinks less, fails more, retries more. and YOU burn more tokens paying for those retries.

they added a header that hides Claude's thinking from your logs. so when the model analyzed itself it found blank pages. and concluded it had stopped thinking.. you're paying $200/month for a model that can't read its own diary..

the thinking didn't disappear.. it just became invisible.. and Anthropic said nothing until the numbers went public

---


**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2043004491377840255  

**正文**

I wonder how many people are using Claude, Claude Code, ChatGPT, Perplexity Computer etc to file their taxes this year

---


**作者** Oliver Henry（@oliverhenry）  
**貼文連結** https://x.com/oliverhenry/status/2042854542052593688  

**正文**

Who uses word????

Serious question.
Since Google docs came out that is all I used, who is paying to write word documents?

---


**作者** Ding（@dingyi）  
**貼文連結** https://x.com/dingyi/status/2042662562429571394  

**正文**

个人认为这是目前唯一最好看的 agent 产品，没有之一。

---


**作者** Sagi Eliyahu（@esbsagi）  
**貼文連結** https://x.com/esbsagi/status/2042811881107394940  

**正文**

Trust is where an orchestration layer becomes not only the control plane for scale, but the enabler to even kick off an AI transformation. Enterprise realities are very different than trends on X (outside the developers' world).

---


**作者** George from 🕹prodmgmt.world（@nurijanian）  
**貼文連結** https://x.com/nurijanian/status/2042888689538470173  

**正文**

AI PM OS v1.7 is here
 
New: /measure — put a number on the things you’ve been hand-waving
Every PM has that metric they treat as unknowable. Customer lifetime value. Security risk. “Quality.” The new

---


**作者** Trevin Chow（@trevin）  
**貼文連結** https://x.com/trevin/status/2042657912473161950  

**正文**

Codex delegation, a real debugging skill, session history mining, visual demo reels, and token efficiency improvements in Compound Engineering 2.64.0!
[New] Codex delegation (beta) from Claude Code

---


**作者** 墓碑科技（@mubeitech）  
**貼文連結** https://x.com/mubeitech/status/2042969720438104546  

**正文**

特斯拉的专利全都是免费的。
任何人都可以随便拿去用。

他们去申请专利只有一个目的。
防备专利流氓。
预判别人想通过注册卡脖子，特斯拉就提前抢注。
拿到手里，立刻开源。

马斯克抛出了一个得罪人的观点。
现存的大部分专利都应该被直接废除。
制度设计的初衷是刺激创新，现在的实际效果全是阻碍。

唯一的例外是医药行业。
砸 10 亿美元做完三期临床，出厂的药片成本只需几美元。
如果不给独占期，没人愿意投钱去填海。
白嫖机制必须被遏制。

但跳出这种极端情况，专利就是废纸。
点子是最廉价的东西。
把想法圈禁起来收过路费毫无意义。
1% 的灵感什么都不是，99% 的制造能力才决定生死。

---


**作者** Digi (Delusional)（@digiii）  
**貼文連結** https://x.com/digiii/status/2042848499469873173  

**正文**

Study microeconomics, game theory, psychology, persuasion, ethics, mathematics, and computers. - @naval 

Luck is not found, it is cultivated. 
 
BOOKMARK THIS IF YOU WANT TO MAKE YOUR OWN LUCK. 
Game

---


**作者** Harrison Chase（@hwchase17）  
**貼文連結** https://x.com/hwchase17/status/2042978845347745871  

**正文**

a big part of agent harnesses is how they interact with context

memory is just context

its therefor impossible to separate harness from memory - as @sarahwooders says, "memory isn't a plugin (it's a harness)" 

---


**作者** Rohit（@rohit4verse）  
**貼文連結** https://x.com/rohit4verse/status/2042657403230093420  

**正文**

Anthropic didn't build a better model to make Claude Code work. 

They built a better environment around it. 
55 directories. 331 modules. 

Context compaction so sessions run for hours. Streaming tool execution that saves seconds per turn.

Read this article for full breakdown. 

---


**作者** Rohit（@rohit4verse）  
**貼文連結** https://x.com/rohit4verse/status/2043004732206354603  

**正文**

The most dangerous AI founder of 2027 isn't on X. He's solving a problem you'd never post about. 

---


**作者** Mindset Machine （@mindsetmachine）  
**貼文連結** https://x.com/mindsetmachine/status/2042927153248137662  

**正文**

Jensen Huang on The smartest person he's ever met: 

---


**作者** Olly Smyth（@ollysmyth_）  
**貼文連結** https://x.com/ollysmyth_/status/2030025434835079214  

**正文**

the AI hack big tech doesn't want you to know:
the US patent database 🧵

most people trying to stay ahead of AI trends are reading the same 12 newsletters.
there's a better way. and almost no one talks about it.

---


**作者** Spenser Skates（@spenserskates）  
**貼文連結** https://x.com/spenserskates/status/2042728358975541598  

**正文**

Friday afternoon with @ollysmyth_ 

---


**作者** Tech with Mak（@techNmak）  
**貼文連結** https://x.com/techNmak/status/2042951175071502513  

**正文**

Someone just dropped a 9-layer production AI architecture and it's the most honest breakdown I've seen.

services/ - RAG pipeline, semantic cache, memory, query rewriter, router. Not one file. Five.

agents/ - document grader, decomposer, adaptive router. Self-correcting by design.

prompts/ - versioned, typed, registered. Never hardcoded.

security/ - input, content, output. Three guards not one.

evaluation/ - golden dataset, offline eval, online monitor. Most people skip this entire layer and ship blind.

observability/ - per-stage tracing, feedback linked to traces, cost per query.

.claude/ - agent context so your AI coding assistant knows the codebase before it touches a file.

The demo is one file. Production is this.

---


**作者** Bill The Investor（@billtheinvestor）  
**貼文連結** https://x.com/billtheinvestor/status/2042609194373910540  

**正文**

Hermes Agent 是最强大的开源 AI Agent 框架之一，但几乎没人知道如何使用它。现在有人刚刚绘制了其完整的生态图谱。80 多个工具、技能、插件和集成功能都已汇编成册。在 48 小时内获得了 568 个 GitHub Star。只需一个下午，即可实现从零到完全自主 Agent 的跨越。 

---


**作者** Erik Dunteman（@erikdunteman）  
**貼文連結** https://x.com/erikdunteman/status/2042754346786459664  

**正文**

Some exciting news to share:

Butter is joining Modal!

Infra is having a moment. Agents need new patterns, new primitives. And importantly, scale like we've never seen before.

There is no better team in the world to build this than Modal. It's an honor to join. 

---


**作者** Modal（@modal）  
**貼文連結** https://x.com/modal/status/2042745984384471133  

**正文**

We're excited to announce that @ButterDev_ is joining Modal to help us continue to build the best sandbox infrastructure. 

Welcome to the team! 💚🧈 

---


**作者** Modal（@modal）  
**貼文連結** https://x.com/modal/status/2036455632828551438  

**正文**

Unstick your AI

Modal x @krazamtv 

---


**作者** Huan（@Huanusa）  
**貼文連結** https://x.com/Huanusa/status/2042460312482226444  

**正文**

马斯克03年在斯坦福，45分钟闭门演讲

他没有讲空洞的成功学，而是手把手拆解：
如何从0开始创办公司、如何在极端困难中活下来。
在场的人直接说：这才是创业者的教科书！ 

---


**作者** Wayne Zhang（@wayne_zhang0）  
**貼文連結** https://x.com/wayne_zhang0/status/2042874483606983079  

**正文**

调研了半天现有的 harness engineering 框架，还不如 ralph loop，简单好用、直接高效，不容易漂移，也不污染上下文，你值得拥有。👍

https://github.com/snarktank/ralph

---


**作者** Ronin（@DeRonin_）  
**貼文連結** https://x.com/DeRonin_/status/2042690069635699138  

**正文**

> use Claude to write tweets
> type "write me a post about [topic]"
> get generic corporate robot output
> rewrite every line manually
> do this 10 times a day
> discover skill graphs exist
> one folder of notes wired together
> AI finally sounds like you
> you were starting from zero every single chat

---


**作者** 阿绎 AYi（@AYi_AInotes）  
**貼文連結** https://x.com/AYi_AInotes/status/2042970104921542896  

**正文**

Shopify刚放了个大招，绝大多数人估计半年后才会反应过来。

手握3780亿美元年交易额，560万个店铺，Shopify把整个后台的读写权限，全开放给了所有AI Agent， 产品、订单、库存、SEO、图片，想改什么改什么。

他们片子里有个商家只说了一句帮我优化所有产品的SEO，Claude自动更新了32条商品，重写图片描述，设置元数据，还逐一核对了所有改动。

一条指令搞定所有，不用找外包，不用月付200刀买插件，也不用雇人，卧槽真的太吊了(#ﾟДﾟ)

以前一个小Shopify店，每月光插件就要200-500刀，一次SEO审计至少2000刀，雇助理每小时50刀，现在这些全部坍缩成一行指令。

480万个活跃商家，大多管着10到200个商品，以前只能一个个手动改，现在有了Claude Code和MCP协议，每个独立创业者，都相当于拥有了一个五人运营团队。

最狠的是，Shopify自己不做 Agent， 他们搭了一套协议，让所有智能体都能变成Shopify Agent， 这才是真正的平台级布局啊，真的牛逼

---


**作者** Harrison Chase（@hwchase17）  
**貼文連結** https://x.com/hwchase17/status/2042978500567609738  

**正文**

Agent harnesses are becoming the dominant way to build agents, and they are not going anywhere. These harnesses are intimately tied to agent memory. If you used a closed harness - especially if it’s

---


**作者** CJ_Blockchain, CFA（@nbblock）  
**貼文連結** https://x.com/nbblock/status/2042799294571516367  

**正文**

这周我认为所有在投资和创业的人必读的两篇文章。⭐️

1⃣一篇是晚点对大疆创始人汪涛的采访，汪涛几乎从来没在媒体上有过发言，这可能是十年内第一次汪涛接受采访。

如果你正在创业、正在做产品、这几乎是你必读的一篇访谈。看完你一定会浑身舒坦，大呼一声爽。

2⃣另一篇是Amazon CEO Andy Jassy的致股东信。

如果你正在投资、正在投资AI板块、更具体点投资数据中心产业链上下游，这篇文章不读会让你错过一个亿，不开玩笑。

这两篇链接我放评论区了。

别用AI帮你简读，在这件事上你的时间没那么宝贵。

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2042805474681118988  

**正文**

Anthropic 昨天刚发布 Claude Managed Agents 公测，API 团队的 Michael Cohen 的科普：Agent 要替用户操作第三方服务，怎么安全地管理这些账号密钥？

答案是 Vaults。

Vaults 是 CMA 里专门管理终端用户凭证的组件。开发者给每个用户创建一个 Vault，把这个用户访问外部服务的密钥（比如 Linear 的 API Key、GitHub Token）存进去。之后每次启动 Agent 会话时，只需要传入对应的 vault_id，Anthropic 的基础设施会在 Claude 需要调用外部工具时自动注入凭证。

安全设计上有一个值得注意的细节：凭证永远不会被读进 Claude 的上下文窗口。也就是说，即使有人通过提示注入（prompt injection）试图让 Claude 泄露密钥，也拿不到，因为凭证根本不在 Claude 能"看到"的地方。Anthropic 工程博客的技术文章进一步解释了这个架构：Agent 生成的代码在沙箱里运行，而凭证存储在沙箱之外，Claude 调用 MCP 工具时通过一个专用代理（proxy）完成鉴权，harness 本身也接触不到任何凭证。

从代码示例看，整个流程三步：创建 Vault、绑定凭证到 MCP 服务器地址、在创建 Session 时传入 vault_id。对于需要让同一个 Agent 服务多个用户的 SaaS 场景，这比自己搭一套密钥管理系统省事太多了。

CMA 整体现在处于公测阶段，按 API 调用的 token 费用加每小时 0.08 美元的会话费计费。Notion、Rakuten、Asana、Sentry 已经在用了。Claude Code 里也内置了一个 claude-api Skill，可以直接在命令行里引导你完成 Vaults 的配置。

---


**作者** 马天翼（@fkysly）  
**貼文連結** https://x.com/fkysly/status/2042827249041436767  

**正文**

我为什么我推荐 Claude 订阅用户使用 HappyClaw 代替 OpenClaw、Hermes Agent？
一、为什么不再使用 OpenClaw？
过去很长一段时间，我都在使用 OpenClaw 作为我们家的 AI 聊天主力，并且其实从 3.8

---


**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2042888972678938753  

**正文**

Claude Code 源码意外“开源”后，Github 一度出现了几十个复刻和不同语言实现版本，也有人整理成类似 DeepWiki 的文档分享，但把 Claude Code 源码解读写成书的，还是第一次见到：

Claude Code from Source
https://claude-code-from-source.com/

可以肯定是 100% AI 读源码生成的，不过作者也很费心 (token) 整理出 18 章，想了解 Claude Code 工程架构和其中细节的朋友不妨看看。

---


**作者** hoeem（@hooeem）  
**貼文連結** https://x.com/hooeem/status/2042295647362019800  

**正文**

YOU JUST CONNECT CLAUDE CODE WITH NOTEBOOKLM AND IT EXTENDS YOUR SESSIONS BY SAVING YOUR TOKENS.

NOW GO & BUILD! 

---


**作者** Noisy（@noisyb0y1）  
**貼文連結** https://x.com/noisyb0y1/status/2042806425596932480  

**正文**

> use Claude Code for 3 months
> paying $300/month on AI
> thought everything was fine 
> 70% of tokens wasted 
> paying $3 for Claude to read terminal noise 
> found two tools 
> 150,000 -> 30,000 tokens 
> $240/year back automatically 
> $1,200 became $240 
> same subscriptions 
> just finally learned how to use them right

---


**作者** Garry Tan（@garrytan）  
**貼文連結** https://x.com/garrytan/status/2042925773300908103  

**正文**

Steve Yegge says people using AI coding agents are "10x to 100x as productive as engineers using Cursor and chat today, and roughly 1000x as productive as Googlers were back in 2005."
That's a real

---


**作者** 阿绎 AYi（@AYi_AInotes）  
**貼文連結** https://x.com/AYi_AInotes/status/2042594916862431669  

**正文**

说实话，今天看到这个，我直接把手里所有其他AI记忆方案全停了🤩🤩🤩

YC总裁Garry Tan，把自己天天在用的生产级AI Agent记忆系统，完整开源了

这是他自己跑了很久的真实配置，管着10000+Markdown文件，3000+人物档案，13年的日历数据，5800条苹果笔记，还有所有的会议记录、原创想法

现在他把这套东西打包成了GBrain，MIT协议，所有人都可以免费抄作业

github 地址老规矩评论区自取👇

---


**作者** 关木（@ZeroZ_JQ）  
**貼文連結** https://x.com/ZeroZ_JQ/status/2042913064258015634  

**正文**

收集一波画架构图的 skills

周一上班给同事们一点点压力

链接放后面了 

---


**作者** Berryxia.AI（@berryxia）  
**貼文連結** https://x.com/berryxia/status/2042757589180858796  

**正文**

兄弟们，技术架构图终于有救了！ 🤯

以前画 Multi-Agent、RAG、Tool Call 这些架构，diagrams. net 里永远对不齐、颜色土、导出还模糊……画一次头秃一次

烟花直接放大招！开源了个超级神器 fireworks-tech-graph —— 专为 Claude Code 打造的技术图生成 Skill！

一句话就能出图，效果直接起飞：
✅ 自动识别图类型 ✅ 智能语义形状 + 颜色编码（流程蓝、控制橙、数据绿…） ✅ 支持玻璃态、Neon 等高级风格 ✅ 高清 SVG + PNG 一键导出
8 种图类型 + 5 种视觉风格，AI/Agent 常见 Pattern 全覆盖！

从此再也不用为画图焦虑了，太丝滑了

生产力直接拉满！ 快去 star 支持烟花老师～ 

开源链接我放评论区👇

---


**作者** Dr. 67. Pump（@real_dr_pump）  
**貼文連結** https://x.com/real_dr_pump/status/2042880400737931401  

**正文**

前天 @paradigm 组织了一个autoresearch hackathon，核心是想验证OpenAI联合创始人 @karpathy 的观点：
“给代理一个问题、一个确定性评估器，以及足够的计算资源，它就能找到领域专家需要更长时间才能达到的解决方案。”

比赛的题目是研发一个做市算法 https://www.optimizationarena.com/prediction-market-challenge/about
1. 和传统的MM问题类似，市场上会有informed trader (套利者), uninformed trader (散户)，以及其他MM（这里简化为了最笨的一种，只会挂一种单子）
2. 但不同的是，这里的underlyer是unknown的，每一步都会jump，所以这里的背景故事上套了一个Prediction Market的皮。

今天看完题我的第一反应是用belief filter+model-based RL(MCTS etc.) 硬怼上去。但后来才发现 @paradigm 的初衷是让大家用AI去自动化地探索这个问题。

@SurfAI 创始人 @ryanli 和 @zhimao_liu 在比赛里拿了第一和第三。他们还各自写了一篇博客来复盘自己的策略。我读完后理解到所以这里的核心是能不能有一套大规模的，可扩展的infra去做一类optimization的问题。

最简单的办法：同时手动开多个claude-code/codex去跑。但是我们还希望不同的agent之间能够互相学习，进化，并且整个过程是高度并行化的。

@zhimao_liu 还提到了Mimir，这是 @SurfAI 内部的一套K8s 原生代理编排系统，可以用在这里并行启动AI实例来跑实验。

ps好像赛后有人直接破解了🤣

---


**作者** Lindy（@getlindy）  
**貼文連結** https://x.com/getlindy/status/2042791001623028033  

**正文**

Somewhere in a data center rack in Las Vegas, there's a Mac Mini that used to be the entire iMessage infrastructure for Lindy.ai. It had a paired iPhone. It had an Apple account. It was

---


**作者** shmidt（@shmidtqq）  
**貼文連結** https://x.com/shmidtqq/status/2042655558516302143  

**正文**

Hello everyone, shmidt here.
You're probably tired of the limits you constantly hit in your Claude Code.
So, I decided to write an article to help you solve this problem.
You'll be using Claude Code,

---


**作者** Elvis（@elvissun）  
**貼文連結** https://x.com/elvissun/status/2042633997080224034  

**正文**

i'll say this again because i keep seeing people do it wrong:

you can solve ANY engineering problem by dropping an agent with the right harness in a loop.

codex just one-shotted our turbo cache fix after I gave it everything it needs to debug like a real dev on the team.

would have taken 8 hours the old way.

---


**作者** Scott Bair（@scott_bair）  
**貼文連結** https://x.com/scott_bair/status/2042527683821879331  

**正文**

Nothing you will do in your brand will be used more often or for longer than your name.
That's not my line. It's from David Placek, the founder of Lexicon Branding, the firm behind names like Swiffer,

---


**作者** KK.aWSB（@KKaWSB）  
**貼文連結** https://x.com/KKaWSB/status/2042787578349531592  

**正文**

养龙虾的人最近都在讨论同一件事：Hermes Agent。
GitHub上6周涨到3万多Star，242个贡献者，8个大版本迭代。Reddit、X、YouTube上铺天盖地的"我从龙虾换到了Hermes"的帖子。官方甚至直接内置了一键迁移龙虾的命令。

---


**作者** Roland.W（@rwayne）  
**貼文連結** https://x.com/rwayne/status/2042890757657497624  

**正文**

用Claude Code做出了300万的系统

这个算是我目前听到的最恐怖的… 

---


**作者** Akshay 🚀（@akshay_pachaar）  
**貼文連結** https://x.com/akshay_pachaar/status/2042586319390674994  

**正文**

What does every big company think about the agent harness?

Anthropic, OpenAI, CrewAI, LangChain. They all build agents. They all wrap their models in infrastructure to make them useful. They each call it the harness.

But they agree on one thing. And disagree on everything else.

The agreement: the model is not the product. The infrastructure around the model is.

The disagreement: how much of that infrastructure should exist.

This is the most important architectural bet in AI right now. And each company is placing a different one.

𝗔𝗻𝘁𝗵𝗿𝗼𝗽𝗶𝗰 bets on the model. Their harness is deliberately thin. A "dumb loop" that assembles the prompt, calls the model, executes tool calls, and repeats. The model makes all the decisions. The harness just manages turns. Their bet: as models get smarter, you need less infrastructure, not more.

𝗢𝗽𝗲𝗻𝗔𝗜 takes a similar but slightly thicker approach. Their Agents SDK is "code-first," meaning workflow logic lives in native Python, not in some graph DSL. But they add more structure: strict priority stacks for instructions, multiple orchestration modes, and explicit agent handoff patterns.

𝗖𝗿𝗲𝘄𝗔𝗜 adds a deterministic backbone. Their Flows layer handles routing and validation with hard-coded logic, while their Crews handle the autonomous parts. Intelligence where it matters, control everywhere else.

𝗟𝗮𝗻𝗴𝗚𝗿𝗮𝗽𝗵 bets on explicit control. The harness encodes the logic. Every decision point is a node in a graph. Every transition is a defined edge. Planning steps, routing strategies, multi-step workflows are all spelled out in the harness, not left to the model.

Notice the spectrum.

On one end: trust the model, keep the harness thin.
On the other: encode the logic, make the harness thick.

And here's where it gets interesting.

The scaffolding metaphor makes this concrete.

Construction scaffolding is temporary infrastructure that lets workers reach floors they couldn't access otherwise. It doesn't do the building. But without it, workers can't reach the upper floors.

The key word is temporary.

As the building goes up, scaffolding comes down. Manus demonstrated this perfectly. They rebuilt their agent five times in six months. Each rewrite removed complexity. Complex tool definitions became simple shell commands. "Management agents" became basic handoffs.

The scaffolding did its job. So they removed it.

This is also why Anthropic regularly deletes planning steps from Claude Code's harness. Every time a new model version ships that can handle something internally, the corresponding harness logic gets stripped out.

But there's a catch.

Models are now trained with specific harnesses in the loop. Claude Code's model learned to use the exact scaffolding it was built with. Change the scaffolding, and performance drops. The worker trained on THIS scaffolding. Swap it out, and they stumble.

So the field is converging on a principle:

Build scaffolding that's designed to be removed. But remove it carefully, because the model learned to lean on it.

The "future-proofing test" for any agent system: if dropping in a more powerful model improves performance without adding harness complexity, the design is sound.

Two products using the exact same model can perform completely differently based on this one decision: how thick is the harness?

LangChain changed only the infrastructure (same model, same weights) and jumped from outside the top 30 to rank 5 on TerminalBench 2.0.

The model didn't improve. The scaffolding around it did.

The article below is a deep dive on agent harness engineering, covering the orchestration loop, tools, memory, context management, and everything else that transforms a stateless LLM into a capable agent.

---


**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2042875810668069111  

**正文**

Hermes Agent 也原生支持连接微信了，不过不是微信官方的插件也是逆向的。

---


**作者** Ashwin Gopinath（@ashwingop）  
**貼文連結** https://x.com/ashwingop/status/2042605402517573921  

**正文**

There’s been a lot of talk about filesystems as the better path for agent and long-term memory, and that intuition is correct.
We present a no-escape theorem proving exactly why: any memory system that retrieves by meaning (RAG, knowledge graphs, embeddings, parametric memory) will inevitably forget and produce false recall as it grows.

File systems are the only architecture that fully escapes this. @karpathy @garrytan

---


**作者** Howie Liu（@howietl）  
**貼文連結** https://x.com/howietl/status/2042732247338619361  

**正文**

If you're rethinking your agent setup after the Claude subscription changes — we're opening @Hyperagent today.

First 1,000 signups get $1,000 in bonus inference credits + a 2.5x cost subsidy on frontier models including Opus 4.6 (up to $15K/mo) for a year.

If OpenClaw is Linux, Hyperagent is the Mac.

Same autonomous power — cloud-native, isolated sandbox per session, real browser, shell, code execution, hundreds of integrations. No local setup, no managing a physical device, no infrastructure babysitting.

Beautiful GUI built for how you actually want to use agents: rich visual output, skill learning that compounds over time, deploy agents into your company via Slack with one click, and a command center to manage your entire fleet.

https://hyperagent.com/invite/FIRST1000

---


**作者** Simon Taylor（@sytaylor）  
**貼文連結** https://x.com/sytaylor/status/2042486675704533471  

**正文**

Ramp is literally out here telling you how to use AI in enterprise.

---


**作者** Alfie Carter（@AlfieJCarter）  
**貼文連結** https://x.com/AlfieJCarter/status/2042653637306949677  

**正文**

I put the entire Claude Code GTM Engineering Playbook into ONE Notion doc.

8 sections. No fluff.

- How to get set up correctly from day one: Pro plan, terminal install across Mac, Linux, and Windows, GUI install via Antigravity or VS Code, and bypass permissions mode
- What to put in your project brain file, what to leave out, and how to get Claude to update it automatically when it keeps making the same mistake
- How to run plan mode step by step and when to skip it for simple tasks
- How to build a skill file from scratch, fix one that keeps failing, and install 5 GTM skills worth building first: lead scraping, email labeling, proposal generation, outbound sequence writing, and client onboarding
- MCP install process, token cost checks after every install, the best MCPs for GTM work, and how to cut token usage by 50 to 100x by converting MCPs into skills
- Sub-agents and agent teams: the 3 cases where they earn their cost, reliability math for parallel runs, and how to enable parallel variant exploration
- What is eating your context before you type anything, how to use /compact and /clear correctly, and model selection for parent vs sub-agents
- Modal deployment: any skill as a live URL in under 2 minutes, form interface setup, and connection to n8n, Make, or Zapier

This is the setup I would have KILLED for before spending months piecing together how to actually get productive in Claude Code from documentation, YouTube tutorials, and scattered GitHub threads.

Like + comment "CODE" and I'll send it over

(must be connected for priority access)

---


**作者** Theo Luan（@droid_35719）  
**貼文連結** https://x.com/droid_35719/status/2042718783815717211  

**正文**

We built Missions at Factory, and I wrote about the architecture that I led the design for to make multi-day autonomous coding reliable.

Agents are highly reactive to their context. Every design decision follows from keeping each agent's trajectory focused and directionally consistent.

---


**作者** 鸭哥（@grapeot）  
**貼文連結** https://x.com/grapeot/status/2042610064536764666  

**正文**

Claude Opus 做 planner 准确率 31.71%，81 种组合倒数第一。Ministral 8B + Opus 做 solver 反而 74.27%。

模型质量是角色×管线交互的函数，最强模型放错位置会主动破坏推理链路。优化分配可降低 13-32x 成本。

https://yage.ai/share/agentopt-model-selection-pipeline-20260409.html?utm_source=twitter&utm_medium=thread&utm_campaign=agentopt-model-selection-pipeline-20260409

---


**作者** 阿绎 AYi（@AYi_AInotes）  
**貼文連結** https://x.com/AYi_AInotes/status/2042594992393458112  

**正文**

说实话，今天看到这个，我直接把手里所有其他AI记忆方案全停了🤩🤩🤩

YC总裁Garry Tan，把自己天天在用的生产级AI Agent记忆系统，完整开源了

这是他自己跑了很久的真实配置，管着10000+Markdown文件，3000+人物档案，13年的日历数据，5800条苹果笔记，还有所有的会议记录、原创想法

现在他把这套东西打包成了GBrain，MIT协议，所有人都可以免费抄作业

github 地址老规矩评论区自取👇

---


**作者** serafim（@serafimcloud）  
**貼文連結** https://x.com/serafimcloud/status/2042728654762082722  

**正文**

Introducing Agent Registry for Anthropic Managed Agents on @21st_dev

Find the right config in seconds:
→ Semantic search  - describe what you need, not keywords
→ Browse by MCP server - Slack, GitHub, Postgres, Sentry…
→ Filter by category - coding, devops, research, data, monitoring
→ Copy-ready - Prompt, CLI, YAML, JSON, TS, Python

Stop building from scratch. Someone already made it.

---


**作者** Sandhya（@sandhya）  
**貼文連結** https://x.com/sandhya/status/2042631718293901391  

**正文**

In the era of agent experience, performance will become the new competitive advantage for great SaaS companies
 
In January 2025, we first started debating the “death” of software. Anthropic had just

---


**作者** Ramp Labs（@RampLabs）  
**貼文連結** https://x.com/RampLabs/status/2042660310851449223  

**正文**

Multi-agent systems have shown promise in coordination, complex reasoning, and parallel workflows. However, they are often highly token inefficient. In hierarchical architectures, where an

---


**作者** Glean（@glean）  
**貼文連結** https://x.com/glean/status/2042619017936937277  

**正文**

Execute work from one place instead of bouncing between tabs – MCP Apps are now live right in Glean Assistant. 🙌

Bring the UI of tools like @GammaApp, @_Hex_tech, and @Box directly into Glean today, with @Asana, @Mixpanel, and @Clay support coming soon.

Stay in one place, keep your context, and still get things done with the tools you love.

---


**作者** 鸭哥（@grapeot）  
**貼文連結** https://x.com/grapeot/status/2042652335516848623  

**正文**

实测 428 个 LLM API 中转站，9 个在偷偷改你的 tool call 返回值。1 个直接转走了私钥里的 ETH。

这不是理论推演——UCSB 的研究者从淘宝、闲鱼、Shopify 上花钱买的。完整分析：
https://yage.ai/share/llm-router-security-20260410.html?utm_source=twitter&utm_medium=thread&utm_campaign=llm-router-security-20260410

---


**作者** TechFlow 深潮｜APP 已上线（@TechFlowPost）  
**貼文連結** https://x.com/TechFlowPost/status/2042576689289388530  

**正文**

不要问 AI 能为你做什么，给它工具，让它自己去干。
整理 & 编译：深潮TechFlow
嘉宾：Boris Cherny，Claude Code 负责人
主持人：Lenny Rachitsky
播客源：Lenny's Podcast
原标题：Head of Claude Code: What

---


**作者** Ben Lang（@benln）  
**貼文連結** https://x.com/benln/status/2042597263072022836  

**正文**

More suggestions:

Vercel, Anduril, Mercury, Stripe, ElevenLabs, Profound, Anthropic, Mintlify, Databricks, SpaceX, Elise AI, Browserbase, Palantir, Notion, Adaptive Security, Slash, Standard Metrics, Superpower, Nozomio, Foam, Lovable, Polymarket, Starcloud, Linear, Boltnew

---


**作者** Kesava Kirupa Dinakaran（@kesava_kirupa）  
**貼文連結** https://x.com/kesava_kirupa/status/2042259845739602159  

**正文**

America’s leading health systems, like the Cleveland Clinic, work with @Luminai to eliminate administrative waste.

We’re rapidly deploying to more health systems, and excited to announce Series B, bringing total funding to $60m. 

---


**作者** 程序员鱼皮（@yupi996）  
**貼文連結** https://x.com/yupi996/status/2042442625345864107  

**正文**

大家好，我是程序员鱼皮。
最近，我发现 GitHub 上有一批很特别的开源项目，它们的目标用户不是人类，而是 AI。
这些项目天生就是为 AI 服务的，帮 AI 看网页、读文件、操作浏览器，让 AI

---


**作者** Aaron Epstein（@aaron_epstein）  
**貼文連結** https://x.com/aaron_epstein/status/2042269167756382390  

**正文**

Congrats to @Luminai on their $38m series B from Peak XV, and partnership with Cleveland Clinic!

Even at 19, it was clear @kesava_kirupa was going to build a great company – he has one of the most impressive founder stories I've seen at YC.

---


**作者** himanshu（@himanshustwts）  
**貼文連結** https://x.com/himanshustwts/status/2042244111219245525  

**正文**

dude is on some generational run. highly recommend reading this anyone into harness design and sourcing evals.

and viv is genius in making some amazing analogies and connecting the dots. 

---


**作者** Fivos Aresti（@fivosaresti）  
**貼文連結** https://x.com/fivosaresti/status/2042319285255631091  

**正文**

"ABM is only for enterprise teams with 6-figure budgets."

That was true when 6sense was the only option.

Now, with: 

- Clay
- Claude Code
- Signal tools like RB2B, Findymail, Jungler

There’s no more excuse. 

Anyone can build full ABM infrastructure with a lean team.

All you have to do is understand the 4 stages: 

1. TAM mapping
2. Signal tracking
3. Awareness scoring
4. Demand generation.

The RevOps layer that used to need dedicated headcount and 6-figure contracts now runs on a lean stack.

Smaller teams with better infrastructure are outcompeting the ones who built ABM the old way.

PS

Comment the word "ABM" 

And I'll send you a massive breakdown we did on the 8 steps you need to build your ABM system.

---


**作者** weisser（@julianweisser）  
**貼文連結** https://x.com/julianweisser/status/2042354352430727615  

**正文**

The Solo Founders Program turns one today.

Many say you need a co-founder to get started.

They're wrong.

The best founders have never waited around for a co-founder.

Will you? 

---


**作者** Bill_DO_A_BIT多少做点（@Bill_Do_A_Bit）  
**貼文連結** https://x.com/Bill_Do_A_Bit/status/2042142965326545178  

**正文**

你可能刚看到一条新闻：Anthropic 宣布不公开发布自己最新的大模型，因为太强了。
一个 AI 公司造出了自己最先进的模型，然后决定不给你用。不是因为没准备好，是因为它的能力已经超出了他们愿意承担的风险范围。

---


**作者** 出海去孵化器（@chuhaiqu）  
**貼文連結** https://x.com/chuhaiqu/status/2042467668620689575  

**正文**

北京时间 4 月 12 日周日上午 10 点，我们很高兴邀请到 Refly 创始人兼 CEO，也是一名全栈工程师的 Tom @tuturetom。

Tom 和 Refly 在 OpenClaw 初期便 all in 企业级 agent 赛道，构建了首个开源 OpenClaw 办公产品 Nexu。

这场直播 Tom 将从一线创业者视角，分享 OpenClaw 从「养着玩」到「真干活」的认知跃迁，以及让 agent 走进工作流的前沿实践。

欢迎大家预约直播并在直播间交流互动。

---


**作者** Itai Damti（@itaidamti）  
**貼文連結** https://x.com/itaidamti/status/2042398177312325822  

**正文**

VCs have completely changed their definition of which companies are investable in the last year, and a lot of perfectly good tech companies are about to get hurt.
I talked to ~10 VC-backed founders

---


**作者** Tim Draper（@TimDraper）  
**貼文連結** https://x.com/TimDraper/status/2042271363088678946  

**正文**

As a VC, I am always looking for the fearless entrepreneurs who are willing to challenge the status quo and potentially make our world roll differently, and usually better.

Colin Hodge is a terrific entrepreneur and he is an even better writer.

You will love this book.

https://colinhodge.com/book

---


**作者** Kun Chen（@kunchenguid）  
**貼文連結** https://x.com/kunchenguid/status/2041900381350117648  

**正文**

alright agent nerds, if you care about your tokens and usage limits, pay attention to the tools you give to your agents.

i built a benchmark that compared various browser tools for agents, and here's an example of their massive difference in cost and latency doing the same task 

---


**作者** Orange AI（@oran_ge）  
**貼文連結** https://x.com/oran_ge/status/2042418292690993219  

**正文**

一个惊人的事实：
Cowork 做了10天只是第四版设计确定后的开发时间
这个项目准备了超过365天

软件最重要的并不是写代码的部分
就像艺术品，最重要的并不是画出来的部分 

---


**作者** Kaushik Mahorker（@kaushikm_）  
**貼文連結** https://x.com/kaushikm_/status/2042450457663324404  

**正文**

Been using dex everyday for the past few weeks, and they have a killer hubspot integration so my CRM is always up to date

---


**作者** Kevin Gu（@kevingu）  
**貼文連結** https://x.com/kevingu/status/2042307514755399848  

**正文**

introducing Dex, the first agent system with full operational context and a self-updating knowledge base

karpathy's llm knowledge base on steroids

Dex ingests raw events from every app in your workspace. every slack message, email, meeting, browser session, task update compounds into one living knowledge base. background agents continuously monitor and enhance it while you sleep so your agents get smarter every day

try now at joindex [dot] com

---


**作者** KK.aWSB（@KKaWSB）  
**貼文連結** https://x.com/KKaWSB/status/2042404192514687257  

**正文**

你明白发生了什么吗？

Perplexity推出了个人理财应用 
> 连接Plaid 
> 关联你的银行账户、贷款等等 
> 追踪支出和创建自定义预算工具。

你的净资产和理财组合全部可视化

所有会计专业学生的职业生涯可能都要完蛋了。 

---


**作者** 比特币橙子Trader（@oragnes）  
**貼文連結** https://x.com/oragnes/status/2042436994954080621  

**正文**

卧槽！硅谷顶级创投教父马克·安德森，刚刚直接扒光了全球所有大公司的底裤

他一针见血地戳穿职场黑幕：在任何多层级的企业架构里，你们辛辛苦苦熬夜搞出来的向上汇报，本质上全是一场不断叠加的“连环谎言”！

无数传统企业每天都在“PPT治企”中疯狂内耗，高管被蒙蔽，基层在造假！

而马斯克早就看穿了这套虚伪的垃圾系统！

这位亲历过巅峰期IBM的硅谷老兵彻底摊牌：马斯克能把其他巨头按在地上摩擦，凭的就是对绝对真相的变态执念！

当大厂员工还在为了讨好领导粉饰太平时，马斯克早就举起屠刀，用最硬核的第一性原理无情斩断所有虚假汇报，彻底破解了未来一百年的终极管理密码

---


**作者** Aaron Levie（@levie）  
**貼文連結** https://x.com/levie/status/2042285272985931972  

**正文**

Right now the main paradigm that we think of agents in is chatting back and forth, but the biggest use of tokens will come from agents that are just always on running in the background doing work for us, or ones triggered from a workflow.

Agents will be working 24/7 in our workflows processing data, reviewing and generating documents, moving data between systems, writing code, accelerating decision making steps, and more.

In Claude's new Managed Agents feature, in a couple minutes you can wire up an agent that can read contracts when they come into Box to review them, and then assign a task in Linear with the critical information from the contract. 

But this could have been any workflow, like reviewing documents for client onboarding, invoice processing, M&A due-diligence, data extraction pipelines, and millions of other use-cases. And integrating data across any system.

This is only possible when you can have long-running agents that can complete real work in the background, accurately. Agents have the ability to execute code safely, leverage tools, access a compute sandbox, and connect across systems is clearly the architecture of the future.

The industry is now making it easier and easier for enterprises to build and deploy these agents.

---


**作者** Augment Code（@augmentcode）  
**貼文連結** https://x.com/augmentcode/status/2042352621751833045  

**正文**

What should my engineering org look like in 12 months? That's the question underneath every AI tool evaluation, every POC, every seat license debate. And it makes sense: the first step to provisioning

---


**作者** Garry Tan（@garrytan）  
**貼文連結** https://x.com/garrytan/status/2042346483694075921  

**正文**

You need to use frontier models with giant context and actually have systems that give them the right context at the right time to understand what's happening now in AI. Everyone else is guessing. 

There is both massive cost (a $20/mo sub is not going to unlock the awesomeness) and skill issue (you've gotta be a builder)

---


**作者** Leo（@runes_leo）  
**貼文連結** https://x.com/runes_leo/status/2042243228678693244  

**正文**

OpenAI、Cursor、Anthropic 在同一个季度发了三篇实践报告，都叫 harness engineering，但讲的是三件完全不同的事。
yage.ai 有一篇文章把这三篇拆清楚了：OpenAI 在讲怎么设计 agent

---


**作者** 阿绎 AYi（@AYi_AInotes）  
**貼文連結** https://x.com/AYi_AInotes/status/2042152766513279291  

**正文**

喵的这是我免费能看的吗？？？
2026年我听过最实战的一期AI Agent播客，没有之一！
我已经把原视频翻译成中文了，
35分钟，@gregisenberg 和 @rasmic 把搭Agent踩过的所有坑全拆开讲了，其中有一条直接刷新认知：
你精心写的1000行agent.md，每次对话烧掉7000个token，大概率在帮倒忙。

@gregisenberg 说得对，模型本身不管是Claude还是GPT其实已经很强了，
那个几乎唯一的变量，是你给它的context，也就是上下文质量。
以下是我从这条帖子提炼出的 6 条反直觉认知，
每一条都值得存下来👇

---


**作者** Animesh Koratana（@akoratana）  
**貼文連結** https://x.com/akoratana/status/2042415841250328798  

**正文**

Building context graphs in the enterprise has made this feel very real.

The strategic asset is increasingly the right to participate in the flow of work:
the places where code changes, tickets move, approvals happen, and operational decisions get made.

Once a system is present there consistently, its position tends to deepen

---


**作者** Aman（@Amank1412）  
**貼文連結** https://x.com/Amank1412/status/2042323670186803463  

**正文**

Meet AgentPlex, an open-source multi Claude Code sessions orchestrator with graph visualization 

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2042324560700154312  

**正文**

Anthropic 推出了一个叫“顾问工具”（advisor tool）的新 API 功能，核心思路是：让便宜的模型干活，遇到难题时请贵的模型出主意。

具体来说，Sonnet 或 Haiku 作为"执行者"全程跑任务、调工具、处理结果。碰到自己搞不定的决策，就把上下文递给 Opus，Opus 给出方案或纠正，执行者接着干。Opus 全程不碰工具、不直接输出给用户，只充当幕后军师。

这跟很多人熟悉的“大模型拆任务、小模型干活”的模式正好反过来。以前是大模型当指挥官，把任务拆成小块分配下去。现在是小模型自己跑，只在关键节点向大模型请教。好处很直接：大部分 Token 消耗在便宜的模型上，贵的模型只在刀刃上用。

效果方面，Sonnet 配 Opus 顾问在 SWE-bench 多语言测试上比 Sonnet 单干高了 2.7 个百分点，同时每个任务的成本还降了 11.9%。更有意思的是 Haiku 的表现：配上 Opus 顾问后，Haiku 在 BrowseComp 测试上从 19.7% 跳到 41.2%，翻了一倍多。虽然分数还是比 Sonnet 单干低 29%，但成本只有 Sonnet 的 15%，适合跑量大但对智能要求没那么极端的场景。

用起来也简单，在 Messages API 的 tools 里加一个 advisor_20260301 类型就行，一个 API 请求内部完成模型切换，不需要额外管理上下文或做多次调用。可以设 max_uses 控制每次请求最多咨询几次顾问，账单里顾问和执行者的 Token 分开计费。

对开发者来说，这提供了一个新的性价比选项：不用在"全程跑 Opus 太贵"和"只用 Sonnet 不够聪明"之间二选一了。你的 Agent 可以 95% 的时间跑 Sonnet 的价格，5% 的关键决策享受 Opus 的判断力。目前是 beta 阶段，需要加 anthropic-beta: advisor-tool-2026-03-01 请求头才能用。

---


**作者** Sam Parr（@thesamparr）  
**貼文連結** https://x.com/thesamparr/status/1751772615243415928  

**正文**

This is very, very good. 

https://longform.asmartbear.com/extreme-questions/?utm_content=share-button

---


**作者** GitButler（@gitbutler）  
**貼文連結** https://x.com/gitbutler/status/2019433695107772565  

**正文**

Now GitButler has a CLI! 

Stacked and parallel branches, smartlog, simple commit editing, easy undo, json output to every command. And it just works in any Git repo.

Check it out:
https://blog.gitbutler.com/but-cli

---


**作者** 老鬼（@laogui）  
**貼文連結** https://x.com/laogui/status/2042277952877125708  

**正文**

GitHub 联合创始人 Scott Chacon 的新项目 GitButler 刚刚宣布完成 1700 万美元 A 轮融资！

GitButler 是一款为现代 AI 编程工作流打造的创新型 Git 客户端（支持桌面端、CLI 以及全新的终端 TUI）,专为 AI Agent 时代设计 — 不只是给人用，也给 AI 用。

它不是"更好的 Git"，而是在重新思考下一代软件应该怎么被构建。

它的核心优势在于打破了传统的分支工作流，支持并行分支（Parallel Branches）和堆叠分支（Stacked Branches）。开发者可以在同一个工作区同时推进多个功能的开发（例如边修 Bug 边做新功能），彻底告别繁琐的 stash 和分支切换。此外，它深度集成了 Claude 等 AI 助手，能自动生成分支名、提交信息，并支持无限撤销与轻松的提交编辑。

在 UI 层面，GitButler 的设计极具现代感与实用性：采用独特的水平滚动视图，将未分配的更改、多个虚拟分支并排清晰展示，视觉层级分明。

---


**作者** Nikunj Kothari（@nikunj）  
**貼文連結** https://x.com/nikunj/status/2042393034789437742  

**正文**

I used to check LinkedIn before bed. My former colleague's Series B. Like. A PM who got the title I'd chased. Scroll. Someone younger joining a company I'd nearly joined. What. I called it staying

---


**作者** Garry Tan（@garrytan）  
**貼文連結** https://x.com/garrytan/status/2042366856192016641  

**正文**

In China they call people using OpenClaw "still using the Little Lobster" 🦞

---


**作者** Jaya Gupta（@JayaGup10）  
**貼文連結** https://x.com/JayaGup10/status/2042401200109408681  

**正文**

The scarce asset in enterprise AI may be shifting from intelligence to permission.
For two years the market competed on model quality: which system was smartest, fastest, most reliable. The models are

---


**作者** 比特币橙子Trader（@oragnes）  
**貼文連結** https://x.com/oragnes/status/2042210136677388695  

**正文**

Anthropic刚刚完成了一场悄无声息的底座夺权。
当所有人还死盯着那些无聊的模型跑分和评测指标时，他们抛出了一个叫Claude Managed

---


**作者** Coffee with One 🇺🇸（@coffeewithone）  
**貼文連結** https://x.com/coffeewithone/status/2042010490872983581  

**正文**

248 deals in @octolane for one pipeline.
Not a single one manually updated.

Here's what happens when someone signs up:

1. Our webhook instantly creates a deal with the associated account and contact. 

2. Every record enriched through web research + our master database. Zero data entry.

3. Octolane answers the questions that matter to us: 

- Is this a YC company? 
- Do they match our ICP? 
- What's their employee count and location? All triple-verified.

4. I open the deal, see the best suggested actions, and send emails. That's it.

5. Before every meeting, prep is already done, pulled from past communications automatically.

We built web analytics, anonymous traffic signal capture, 2-way email sync, and a meeting recorder. Nothing gets lost. Literally nothing.

We don't have a sales team. Building something beautiful out of nothing from Mission Bay. 

If you're doing founder-led sales, you shouldn't be updating your CRM. Your CRM should be self-driving.

The product is here. Now we go deeper and polish every edge 🏎️

---


**作者** Akshay Krishnaswamy（@hyperindexed）  
**貼文連結** https://x.com/hyperindexed/status/2042210806977184249  

**正文**

One way to think about Palantir AIP: how do you treat the enterprise the way that developers treat code?  

This requires a maximalist vision, where both humans and agents get more capable over time. 

---


**作者** Yanhua（@yanhua1010）  
**貼文連結** https://x.com/yanhua1010/status/2042251132790313155  

**正文**

现在每天早上刷X，基本上领先了AI Valley一天的信息差。

你关注 @claudeai  @OfficialLoganK @yanhua1010 就够了。 

---


**作者** Noisy（@noisyb0y1）  
**貼文連結** https://x.com/noisyb0y1/status/2042086577636061436  

**正文**

> installed Claude Code 3 months ago 
> never opened the security settings 
> Claude reads your wallet seed phrases
> Claude reads your SSH keys 
> Claude reads your AWS credentials 
> can send data anywhere it wants 
> one CLAUDE.md file in a cloned repo 
> your data is already gone 
> average damage - $8,000-$50,000 in one night 
> 15 minutes to fix this 
> you still haven't

---


**作者** Harrison Chase（@hwchase17）  
**貼文連結** https://x.com/hwchase17/status/2042269195656921120  

**正文**

Today we’re launching Deep Agents deploy in beta. Deep Agents deploy is the fastest way to deploy a model agnostic, open source agent harness in a production ready way.
Deep Agents deploy is built for

---


**作者** Ashwin Gopinath（@ashwingop）  
**貼文連結** https://x.com/ashwingop/status/2042286523438284987  

**正文**

We've raised $5M to build organizational memory.

Every company runs on decisions, but as teams grow the, context behind them gets lost. We built Sentra to make sure that never happens again.

Start using Sentra for free today! 

---


**作者** Aman（@Amank1412）  
**貼文連結** https://x.com/Amank1412/status/2042250826274795630  

**正文**

All the best startup accelerators to apply in 2026:

1. Y Combinator ($500k for ~7%)
2. Sequoia Arc ($1M for ~10%)
3. a16z Speedrun ($500k for 10% + $500k guaranteed follow-on)
4. South Park Commons ($400k for 7% + $600k guaranteed follow-on)
5. NEO Residency ($750k uncapped SAFE, variable equity)
6. HF0 Residency ($1M uncapped SAFE for 5%)
7. Seedcamp ($350k–$1M, flexible terms)
8. Boost VC ($500k for 15%)
9. The Mint ($500k for 10%)
10. 500 Global ($150k for 6%)
11. PearX ($250k–$2M SAFE)
12. SOSV / HAX ($250k for ~7%)
13. Techstars ($220k for 5%+)
14. LAUNCH ($125k for 6%)
15. Antler US ($200k–$250k for 8–9%)
16. Founders Fellowship ($150k for 5–10%)
17. Founders, Inc. ($100k–$250k for 4–7%)
18. Antler Europe (€100k for 10% + stipend)
19. Entrepreneurs First (up to $250k for ~9%)
20. Conviction Embed ($150k uncapped MFN SAFE)
21. Afore Capital ($500k–$2M SAFE, flexible terms)
22. Soma Capital ($100k)
23. Berkeley SkyDeck ($200k)
24. gener8tor ($100k for 7.5%)
25. Heartfelt VC (up to €500k)
26. Forum Ventures ($100k for 7.5%)
27. Greylock Edge (custom SAFE + $500k+ in credits)
29. Betaworks AI Camp (up to $500k for 5% + uncapped SAFE)
29. Google for Startups (equity-free; up to $100k + $350k in cloud credits)
30. Entrepreneurs Roundtable Accelerator ($150k for 6% + $320k in credits)
31. Plug and Play Tech Center (equity-free; optional $100k–$150k SAFE)
32. Startup Wise Guys (up to €65k for equity + up to €300k follow-on)
33. HSG START Accelerator (CHF 200k for 4–10%)
34. Alchemist Accelerator (~$30k SAFE for ~5%)
35. Bethnal Green Ventures (£60,000 for 7%)

---


**作者** 鸭哥（@grapeot）  
**貼文連結** https://x.com/grapeot/status/2042252956771426319  

**正文**

AI Rollup 赛道已有 $3B+ 专项资本。但最有价值的洞察不在交易数字上：80% 的 AI 项目失败，根因全部是组织性的。你老板是不是重度 AI 用户，可能比你的 prompt 写得好不好更重要。

https://yage.ai/share/ai-rollup-survey-20260409.html?utm_source=twitter&utm_medium=thread&utm_campaign=ai-rollup-survey

---


**作者** Bill The Investor（@billtheinvestor）  
**貼文連結** https://x.com/billtheinvestor/status/2042008184181944520  

**正文**

95% 的人在 agent.md 文件上浪费 Token。Skills 模式更优。agent.md 机制：
- 每一轮对话都会加载完整文件到 Context。- 1,000 行代码 ≈ 7,000 Tokens。- 每次运行均会消耗。Skills 机制：
- Context 中仅保留标题与描述。- Agent 识别相关性后，按需加载完整文档。
这属于渐进式披露（Progressive Disclosure）。agent.md 是常驻且持续消耗 Token 的；Skills 是按需加载。停止过度填充 Context，转向构建 Skills。

---


**作者** AIGCLINK（@aigclink）  
**貼文連結** https://x.com/aigclink/status/2042167969376301240  

**正文**

一个收录了各种人格蒸馏Skill的库，覆盖47个技能，有把自己Skill化的、有职场的、亲密关系的、公众人物的等等

同事.skill、前任.skill、女娲.skill、自己.skill、乔布斯.skill、数字人生.skill、月老姻缘测算Skills……

人类人格技能化，把人变成可插拔模块。如果迷乔布斯，想让乔布斯看这个产品会怎么说，就加载乔布斯.skill，想用芒格的方式分析，加载芒格.skill

#skill #人格skill

---


**作者** Ivan Burazin（@ivanburazin）  
**貼文連結** https://x.com/ivanburazin/status/2040112100597506107  

**正文**

After the Claude Code source code leak, a former PM extracted its multi-agent orchestration system into an open source model agnostic framework. 

He studied the architecture, focused on the multi-agent orchestration layer (the coordinator that breaks goals into tasks, team system, message bus, task scheduler with dependency resolution), and reimplemented these patterns from scratch as a standalone open source framework without infringing on Anthropic's code. 

The result is what @JackChen_x calls an "open-multi-agent." Unlike claude-agent-sdk, which spawns a CLI process per agent, this runs entirely in-process and can be deployed anywhere (serverless, Docker, CI/CD)

Check it out: https://github.com/JackChen-me/open-multi-agent

---


**作者** Noémie（@FedericoNoemie）  
**貼文連結** https://x.com/FedericoNoemie/status/2041966198406226326  

**正文**

ran into a founder who had a co-founder and is now solo. 

he jokingly said startups should either have 1 decision maker or 8, anything else is a bad middle ground.

every great startup becomes 'solo founded' eventually. you think jobs, not wozniak. zuck, not moskovitz. Airbnb IS brian chesky.

---


**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2042229587082695054  

**正文**

天天给别人的产品写教程，今天终于轮到自己的产品了。

我觉得 Code Pilot 已经相当可用了，给它写了一个保姆级教程。

另外 Codepilot 现在可以脱离 Claude Code 运行，也支持了 GPT 账号的授权登录，使用你的额度。 

---


**作者** Kasif（@md_kasif_uddin）  
**貼文連結** https://x.com/md_kasif_uddin/status/2041900039304573050  

**正文**

> be Alexandr Wang
> math + physics prodigy as a kid
> cracks national olympiads in high school
> gets into MIT for machine learning
> drops out at 19 to build a startup
> starts Scale AI through Y Combinator
> helps train data for self-driving cars + AI models
> quietly becomes backbone for companies building AI
> Scale AI hits billions in valuation
> becomes youngest self-made billionaire at 24
> governments + big tech rely on his company
> Meta invests billions into Scale AI
> leaves CEO role to join Meta
> becomes Chief AI Officer and leads Superintelligence Labs

bro built the data layer for AI

then got hired to run the future of AI itself

from dropout to running Meta’s AI race

---


**作者** loonggg（@KengGuangLong）  
**貼文連結** https://x.com/KengGuangLong/status/2042050956142243915  

**正文**

名人也挺可悲的，看看都把你们给蒸馏了。

GitHub 上出了一个「人格蒸馏」合集，我看了看，巴菲特、纳瓦尔、乔布斯、马斯克、费曼、张一鸣、张雪峰、塔勒布、甚至特朗普都被蒸馏了。

这里的“人格蒸馏”主要指从对话、作品、资料或数字痕迹中提炼表达风格、决策框架与交互方式，不默认等同于对真实个体的完整还原。

合集传送门地址：http://github.com/xixu-me/awesome-persona-distill-skills

---


**作者** 木子不写代码（@ai_muzi）  
**貼文連結** https://x.com/ai_muzi/status/2042031272470397209  

**正文**

永别了n8n!

Anthropic新发布的 Claude Managed Agents，

会吞噬掉所有no code/工作流软件的市场，

一个视频带你掌握Claude Managed Agents全流程 👇 

---


**作者** 天猪 TZ（@atian25）  
**貼文連結** https://x.com/atian25/status/2042046248287662257  

**正文**

以前面试，有人说自己学习能力强、好奇心旺盛。我会追问一句：请跟我分享下过去三个月你学了什么。答不上来，那”擅长学习”就只是一个没有交付物的自我评价。一个人声称的特质，只有知行合一才能证明。
AI

---


**作者** Panda（@Jiaxi_Cui）  
**貼文連結** https://x.com/Jiaxi_Cui/status/2042058620729487588  

**正文**

今天是 2026 年 4 月 9 号，我按下了 Cerul.ai 的发布按钮。
说真的，这可能是我这辈子做得最慢的一个产品。
 
这件事我想了很多年。
你每天都在用 AI

---


**作者** 番茄哈猫🍐（@zuilizhishier）  
**貼文連結** https://x.com/zuilizhishier/status/2041767053158445360  

**正文**

张雪峰被蒸馏了… 

---


**作者** nazha（@xiaokedada）  
**貼文連結** https://x.com/xiaokedada/status/2042113510415687777  

**正文**

#分享 Pi  的作者 Mario 加入了 Armin 开的 Earendil 公司

Pi  是一个开源的 Agent 开发框架， 也是爆火的 OpenClaw 底层的 Agent 运行框架。

Mario 从 2009 年开始做开源，第一个「成名作」是游戏开发框架 libGDX，一度是 Android 上最流行的游戏框架。之后参与了 RoboVM，这是一个让 JVM 代码在 iOS 上运行的 AOT 编译器和运行时，后来被 Xamarin 收购，再被 Microsoft 收购， 最终整个项目被关停了。

Pi 就是 Mario 最近的开源产品。

Armin，全名 Armin Ronacher，是 Python Flask 框架（Python 最流行的 Web 框架之一）的作者 。过去 10 年，一直在 Sentry 工作，在 AI 领域，算是名人。今年和 Colin 共同创办了这家叫 Earendil 的公司。

Mario 跟 Armin 在 14 年前的 Reddit 上对线，2016 年 Mario 去维也纳，顺路看望在 Sentry 老同事的时候跟 Armin 一起喝咖啡。也在这一年，Mario 也去拜访了 Peter Steinberger（OpenClaw 的开发者）。

去年 5 月，他们三个人（Mario、Armin 和 Peter）在维也纳又聚了一次，一起写出来 VibeTunnel，这是三人第一次 agent 项目上的深度协作。

后来就是，Peter 进一步用 Pi 搭了 OpenClaw，OpenClaw 爆火，顺便也把 Mario 拉到聚光灯下了。

Earendil 是一家 Public Benefit Corporation（公益型公司），理念是：以人为本。他们认为：优秀的软件不应以优化你生活的每一分钟为目标，而应创造空间，让人们获得更美好、更愉悦的体验，建立更优质的人际关系，以及更和谐的相处方式。

Earendil 最近的产品是 Lefos，最近在开放内测。Lefos 是一个 Agent，但是没有软件实体，交互方式是通过 email：向 lefos 发送邮件。

Mario 本来想把 Pi 当作一个「小而美的项目」，但从社区、同行的反馈发现：Pi 其实具备很强的商业潜力。

Mario 本人是 Earendil 的小股东，又和 Armin、Colin 有多年交情，Pi 要提供商业化，自然而言 Earendil 变成一个选择了。于是他选择「加入 Earendil，把 Pi 一起带过去。

附录：
Mario 的博客：https://mariozechner.at/
Armin 的博客：https://lucumr.pocoo.org/about/
Pi 是啥：https://github.com/badlogic/pi-mono
Earendil: https://earendil.com
Lefos 正在开放内测：https://lefos.com/
Mario 声明：https://mariozechner.at/posts/2026-04-08-ive-sold-out/

---


**作者** Berryxia.AI（@berryxia）  
**貼文連結** https://x.com/berryxia/status/2042037103220105683  

**正文**

Karpathy 的 LLM 知识库被玩出新花样了！

把「存储库」升级成了真正的「学习库」——不是存已知的东西，而是帮你攻克完全陌生的领域。

她用它深度阅读柏拉图（Timaeus） 

---


**作者** danny（@agintender）  
**貼文連結** https://x.com/agintender/status/2042070100170461385  

**正文**

还 agent工作流吗？还harness吗？
还在自建agent一人公司吗？哈哈哈

比较可怕的是，这次还连带把企业样例给你了 @asana @Rakuten @NotionHQ .... 连成熟的企业都在用，你还在想什么？

这个事情出来， @OpenAI 估计哭晕在厕所？ 

---


**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2042081251667091826  

**正文**

Meta 发布 Muse Spark 多模态推理模型

推翻 Llama 重来 但是不开源

Meta 发布了 Muse Spark，这是 Meta Superintelligence Labs 的第一个模型，也是 Meta 在 AI 模型上的一次彻底换轨。

不是 Llama 的下一代，是一个全新系列...

三个核心能力：

① 原生多模态，不是在文本模型上加个视觉模块，是从一开始就把图文一起训练的。

能做的事情：

拍张照片问营养成分，它能分析
视觉 STEM 问题（看图解题、识别实体、空间定位）
从文字描述生成小游戏或网页

② Contemplating 模式，这是 Muse Spark 最值得关注的新能力。它不是让一个模型想更久，而是同时启动多个子 Agent 并行推理同一个问题，然后综合结果。

Meta 把这个叫"multi-agent orchestration"。

官方数据：Contemplating 模式在 Humanity's Last Exam 上得分 58%，FrontierScience Research 上 38%。

这个设计的好处是：推理能力大幅提升，但延迟不会线性增长，因为是并行的。

③ 训练效率提升超过 10 倍，同等能力只用 Llama 4  十分之一的算力

Meta 给 Muse Spark 的定位不是"通用大模型"，而是"个人超级智能"（Personal Superintelligence），一个能理解你的世界、帮你处理生活中重要事情的 AI 助手。

直接面向其 30 亿用户，结合 Facebook、Instagram、WhatsApp 的社交数据和用户画像来做个性化。

---


**作者** Applied Compute（@appliedcompute）  
**貼文連結** https://x.com/appliedcompute/status/2041932184458817734  

**正文**

Models keep getting smarter, but there's a massive gap between raw intelligence and actual productivity on specific tasks inside companies. Delivering real value requires knowing how to perform those

---


**作者** Ian (伊恩)（@ianneo_ai）  
**貼文連結** https://x.com/ianneo_ai/status/2041888797701583126  

**正文**

可怕，已经有人开始批量蒸馏别人的脑子了

这个 repo 里，巴菲特、PG、Karpathy、张一鸣、毛选、MrBeast，都被拆成了 skill

你拿到的就不只是观点

而是他们怎么判断、怎么拆问题、怎么做决策

这玩意儿看着像资料库

真用起来更像给自己挂了一排数字军师

以后人与人的差距，可能就是你背后站着多少个这样的外挂😂

---


**作者** KK.aWSB（@KKaWSB）  
**貼文連結** https://x.com/KKaWSB/status/2041783093871440076  

**正文**

你们尽管说我妄想吧……但我会一直重复这句话……

到 2026 年，Claude + SEO 将比比特币创造更多百万富翁企业。

如果这条信息出现在你的时间线上，请不要收藏。

直接把这段代码粘贴到 Claude 里就行了。

以后你会感谢我的。 

---


**作者** Aman（@Amank1412）  
**貼文連結** https://x.com/Amank1412/status/2041836459683147945  

**正文**

Life after switching from Claude to Codex. 

---


**作者** LoucB（@LoicBerthelot）  
**貼文連結** https://x.com/LoicBerthelot/status/2041846396127445090  

**正文**

Right now, two versions your SaaS exist…

One has humans answering the same report ticket for the 400th time, manually researching competitors, wondering when they’ll “find time” to lean this agent stuff.

The other has AI agents running CTO operations, CFO reporting spreadsheets, CMOs handling SEO and ad production 24/7… while the founder sleeps.

Same starting point, different infrastructure, and the split happens now…

Which agent framework will you choose to build on?

I’ve bootstrapped 12+ SaaS products, I’ve recruited and managed teams of 30+, and I was the first to introduce AI in the dropshipping space.

Now I have 3 AI agents in my production at Dropmagic on a $5/mo VPS.

I’m migrating from Openclaw to Hermes.

This isn’t a comparison chart you’ll bookmark and never read again.

It’s the framework after you deploy agents inside a real SaaS doing real revenue.

## The Mental Model You Need To Adopt

Most look at Openclaw and Hermes and think they’re the same.

In reality, they both optimize for different problems.

> Openclaw = Agent OS

It executes, orchestrates, and connects everything. 
Think of it as the operating system your agents live inside.

> Hermes = Growth OS

It has memory and total self-improvement. 
Watches what you do, builds reusable skills, and gets better.

When you understand the distinction you can finally save yourself the migraine.

## What Openclaw Actually Does Well

There’s a reason Openclaw hit 346,000 GitHub stars in under 5 months and surpassed React as the most starred software project in GitHub history.

Peter Steinberger built something that captures real need.

The platform supports every messaging integration possible and it’s ecosystem has 44,000+ skills on ClawHub. It’s a fantastic option.

But after running it for 1.5 months, I kept noticing that its limitation is execution.

I have CTOs, CFOs, COOs, and CMOs, that are all agentic.

They don’t learn or evolve, they stagnate after my commands are complete.

## Where Openclaw Falls Short

If you want it to handle a new pattern or skill, you manually build the skill.

For example…

My Openclaw CTO can pull TikTok data and analyze it, but when a creator starts posting in a new format, the agent doesn’t adapt to what’s working.

So I have t go back in and define the skill… it’s a bottleneck.

The next issue is security.

Security researchers found over 135,000 Openclaw instances exposed on the public internet across 82 countries.

Some skills were designed to steal API keys without user knowledge and I’m not saying don’t use Openclaw, but understand what you’re deploying and put it behind authentication.

The last issue is memory.

Openclaw has persistent memory, but it’s basic. Where it remembers facts, it can’t connect them.

3 weeks in, it’ll forget the context of why you made a specific decision, what the outcome was, and how it should inform your next move to avoid mistakes.

## Why Hermes Changed the Equation

Hermes launched in February 2026 and has 22,000 GitHub stars.

The community is smaller with less brand recognition.

I don’t care about any of that because it’s not why I decided to migrate.

> Self-improvement loops

After 2 weeks on Hermes, it started handling patterns it hadn’t been explicitly taught.

It watched me classify tickets, then built it’s own skill for it and kept refining it over time.

Openclaw would’ve required me to do it.

Whenever Hermes solves a hard problem, it writes a reusable skill doc in Markdown so it can more easily solve similar problems in the future.

This action compounds and becomes more valuable.

> Memory connects the dots

Hermes uses a multi-level memory system…

> Session memory for the current conversation. Persistent memory for facts and preferences across sessions. Skill memory for solution patterns the agent has learned across all sessions.

The agent recalls conversations from 4 weeks ago.

Then searches it’s own history to add context for current business decisions.

In practice…

I make a decision about pricing in week 1, it recalls the reasoning in week 5, and we don’t enter any false positive feedback loops when deciding.

> Zero data collection or telemetry

All data stays on your machine. No tracking, cloud lock-in, or MIT license.

So for SaaS handling massive customer data or financial info, this is invaluable.

## My Honest Comparison

Let me break down everything I took into consideration…

LEARNING…

>Openclaw uses static, human authored skills. 
>Hermes has a self improvement loop that creates and refines skills. 
👑 Hermes wins → (1-0)

MEMORY…

>Openclaw has basic memory with per-assistant isolation for teams. 
>Hermes has multi-level memory, LLM summarization, cross-session recall. 
👑 Hermes wins → (2-0)

SKILL ECOSYSTEM…

>Openclaw has 50+ built in skills, easy plugin, 44K+ ClawHub skills. 
>Hermes has 40+ tools, autogenerates new skills, supports agentskills(.)io 
👑 Openclaw wins → (2-1)

CHANNELS…

>Openclaw supports everything. 
>Hermes has a much smaller integration base. 
👑 Openclaw wins → (2-2)

MODELS…

>Openclaw supports Claude, GPT, Gemini, Grok, Mistral, and xAI via BYOK 
>Hermes supports 200+ models via OpenRouter, Anthropic, OpenAI, and custom. 
👑 Hermes wins → (3-2)

DEPLOYMENT…

>Openclaw runs local, VPS, or cloud with managed options. 
>Hermes runs, local, VPS, Docker, SSH, or serverless on Modal & Daytona. 
👑 Hermes wins → (4-2)

SECURITY…

>Openclaw has had multiple critical CVEs in 2026. 
>Hermes has zero agent CVEs so far. 
👑 Hermes win → (5-2)

AUTOMATION…

>Openclaw has a heartbeat scheduler plus cron jobs w/ multi-channel workflows. 
>Hermes has natural language cron plus parallel sub agents. 
👑 Tie → (6-3)

## Decision Framework To Implement

Pick Openclaw when…

You need maximum channel coverage across random platforms, you want a mature plugin ecosystem with massive community support, you run a team with multiple agents that need strict isolation between roles, you need the deployment to happen this week with minimal configuration.

Pick Hermes when…

You want an agent that gets smarter the more you use it, you care about deep memory and cross-session context that compounds over time, you prefer zero telemetry and full data ownership without tracking, you’re technical enough to trade ecosystem breadth for learning depth.

It’s not simply an “either/or” decision, you can run both.

## How To Set This Up

Both are free and self hosted. Get a VPS first: 
[Get Hostinger VPS (20% OFF)](<https://www.hostinger.com/fr?REFERRALCODE=ZZ2HELLODTXU>)

Install Hermes: 
[Full Setup Guide HERE](<https://www.notion.so/Hermes-33906394b4d780bd9d53efb31d2f6b14?source=copy_link>)

Install Openclaw: 
[Full Setup Guide HERE](<https://www.notion.so/OpenClaw-33806394b4d781c3954efbb34e2db5ee?source=copy_link>)

Fun fact: Hermes has a built in migration command from Openclaw

---


**作者** Jiayuan (JY) Zhang（@jiayuan_jy）  
**貼文連結** https://x.com/jiayuan_jy/status/2041970269372518877  

**正文**

We created the open source version of Claude Managed Agents.

Introducing Multica

https://github.com/multica-ai/multica 
We created the open source version of Claude Managed Agents.

Introducing Multica

https://github.com/multica-ai/multica 
You can directly use the cloud version.

http://multica.ai 

---


**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2042048845438497191  

**正文**

just got an email from a very popular Series A company saying they’re using @nozomioai to write technical blogs for their product by indexing a bunch of articles and technical content.

wow.

---


**作者** 鸭哥（@grapeot）  
**貼文連結** https://x.com/grapeot/status/2042046346254041420  

**正文**

Anthropic 今天发了 Claude Managed Agents。看上去是帮开发者省几周基础设施代码。但 4 天前他们刚切掉 OpenClaw 等第三方 harness，先关便宜路径再开官方 runtime。这笔账算下来，他们在替你决定 agent 的 operational state 以后存在谁家。https://yage.ai/share/claude-managed-agents-20260408.html?utm_source=twitter&utm_medium=thread&utm_campaign=claude-managed-agents-20260408

---


**作者** ericosiu（@ericosiu）  
**貼文連結** https://x.com/ericosiu/status/2042001368647446820  

**正文**

I rolled out AI agents across my entire company. Not one assistant. A fleet. Every employee has an AI operating layer tuned to their role, connected to our systems, and coordinated by a shared brain.

---


**作者** ZEN（@supezen）  
**貼文連結** https://x.com/supezen/status/2042021460148154454  

**正文**

一些值得关注的 AI 相关原创内容作者👇

  AI / LLM / 开发工具

  @karpathy — LLM 科普与深度解析
  @thdx — opencode 作者
  @rauchg — Vercel CEO
  @mitchellh — Ghostty 作者, HashiCorp 前创始人
  @dhh — Ruby on Rails 创始人, 37signals CEO
  @addyosmani — Google Cloud AI 负责人
  @zeeg — Sentry 创始人
  @jarredsumner — Bun 创始人
  @BHolmesDev — Astro 开发者教育
  @boristane — Cloudflare Workers 可观测性负责人
  @karrisaarinen — Linear 创始人
  @kepano — Obsidian 创始人
  @trq212 — Claude Code 动态更新
  @bcherny — Claude Code 作者
  @lennysan — 产品管理与深度访谈
  @jasonfried — 37signals/Basecamp CEO
  @leerob — 开发者关系教育（Cursor, Next.js）
  @ctatedev — Vercel Labs
  @Shpigford — 连续创业者

  设计工程

  @shadcn — shadcn/ui 作者
  @emilkowalski — http://emilkowal.ski
  @joshpuckett — http://interfacecraft.dev
  @jakubkrehel — http://jakub.kr
  @raphaelsalaja — http://userinterface.wiki
  @nandafyi — Cloudflare 设计
  @benjitaylor — Twitter 设计, Agentation
  @mengto — Aura Build 创始人
  @jayneildalal — 设计师访谈
  @jh3yy — 设计工程解析

  工程媒体与资讯

  @GergelyOrosz — Pragmatic Engineer
  @theo — http://t3.gg
  @ThePrimeagen — ThePrimeTime
  @Rasmic — Rasmic
  @atmoio — Atmo

  数据库

  @jamwt — Convex CEO
  @jamesacowling — Convex CTO
  @glcst — Turso CEO
  @samlambert — PlanetScale CEO

---


**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2042062724902089213  

**正文**

Anthropic 推出 Claude Managed Agents 

可以托管你的 Agent
从原型到上线只要几天

做过 Agent 的人都知道，写 Agent 逻辑本身不难，难的是把它稳定跑在生产环境里。

你要处理：容器编排、沙箱隔离、凭证管理、状态持久化、断点续跑、错误恢复、可观测性。

这套东西搭下来，几个月就过去了，Agent 本身的逻辑可能只占代码量的 10%。

Managed Agents 的定位就是把这 90% 的基础设施工作接管掉。

你只需要描述 Agent 要干什么、能用哪些工具、权限边界在哪，剩下的 Anthropic 帮你跑。

---


**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2042060231904260588  

**正文**

Anthropic 发布云端托管 Agent 基础设施 Claude Managed Agents

帮你把安全沙箱、会话状态、权限管理、凭证和追踪等底层工程都打包好

只需要定义任务、工具和规则，就能让 Agent 长时间自主运行、调用工具、恢复错误，还有多 Agent 协同和自我评估迭代

把从原型到生产的周期从几个月压缩到几天

开发和上线速度提升 3–10 倍，工程团队可以少花时间在基础设施上，多把精力放在产品体验和业务集成上

计费方式是在 Claude 标准 token 单价基础上，每小时会话活跃运行额外收取 0.08 美元。

---


**作者** Kimberly Tan（@kimberlywtan）  
**貼文連結** https://x.com/kimberlywtan/status/2041898086818312293  

**正文**

We @a16z decided to compile hard data on what’s actually working in enterprise AI.

* Nearly 30% of the Fortune 500 and ~20% of the Global 2000 are live, paying customers of the leading AI startups. This goes counter to the MIT statistic that 95% of AI pilots are failing in the enterprise

* Coding, customer support, and search are the use cases with clearest enterprise demand, and adoption isn’t just concentrated in traditionally tech-forward sectors.

* Models are improving very quickly at economically valuable tasks, based on @OpenAI's GDPval. We’re tracking GDPval closely to determine where model capabilities will enable the next set of breakout enterprise AI companies.

Read more from our enterprise AI report, linked in the comments
We @a16z decided to compile hard data on what’s actually working in enterprise AI.

* Nearly 30% of the Fortune 500 and ~20% of the Global 2000 are live, paying customers of the leading AI startups. This goes counter to the MIT statistic that 95% of AI pilots are failing in the enterprise

* Coding, customer support, and search are the use cases with clearest enterprise demand, and adoption isn’t just concentrated in traditionally tech-forward sectors.

* Models are improving very quickly at economically valuable tasks, based on @OpenAI's GDPval. We’re tracking GDPval closely to determine where model capabilities will enable the next set of breakout enterprise AI companies.

Read more from our enterprise AI report, linked in the comments

---


**作者** Vincent Logic | 只上干货（@VincentLogic）  
**貼文連結** https://x.com/VincentLogic/status/2041704101394968876  

**正文**

> 核心提示：当所有人都在疯狂学习AI技能时，年入400万美元的顶级博主Dan Koe却说：技术根本不重要。麦肯锡最新报告证实，88%企业已部署AI，但仅39%真正获利——差距不在工具，而在能动性。

最近，我在研究AI时代生存法则时，被一个颠覆性观点震撼了。不是来自某位技术大牛，而是拥有400多万粉丝、年收入400多万美元的美国博主Dan Koe。他在X平台发表的《未来十年最重要的技能》一文，7天内狂揽1.7亿阅读量，连马斯克都为之设立百万美元奖金池。

最震撼的是，他口中"最重要的技能"，既不是编程，也不是提示词工程，而是一个被严重低估的词——Agency（能动性）。

起初我也以为是鸡汤，但当我深入挖掘，发现麦肯锡、世界经济论坛、哈佛商学院三大顶级机构的研究，竟都指向同一结论。更令人震惊的是，神经科学已证实：被动是大脑出厂设置，能动性需要刻意训练。

今天，我将用最接地气的方式，拆解Dan Koe的核心观点，并告诉你如何在AI浪潮中不被淘汰。

## 一、被动不是你的错：大脑的出厂设置

Dan Koe引用了一句话："你的大脑还通过一根脐带连在社会上面"。什么意思？你以为在独立思考，实则判断标准、追求目标、恐惧对象，全是外界灌输的。

就像在菜单上点菜，你从未尝试自己写菜单。从小到大，专业选择、职业规划、成功标准、幸福定义——这些真的是你自主思考的，还是社会塞给你的？

Dan Koe引用发展心理学家Cook Greuter对4510名成年人的测试：约50%人口处于从众阶段。但更严峻的是，从众者+埋头苦干者+职场攀爬者，合计占比高达80%。

这意味着：你身边每10个人，就有8个在他人设定的规则里打转。比如在公司拼命加班升职，却从未思考：这条赛道十年后还存在吗？

神经科学的惊天反转

1967年，心理学家Seligman做了个著名实验：将狗关在笼子反复电击，狗无法逃脱。后来门打开，狗竟趴地哀叫，放弃逃跑。他将此称为"习得性无助"——后天习得的无助状态。

这个理论轰动心理学界，Seligman因此当选美国心理学会主席。Dan Koe借此引申：你渴望的生活充满挑战，但因挫折和失败故事，内心笃定自己无法达成，连尝试勇气都没有。

但重点来了！ 2016年，79岁高龄的Seligman本人站出来推翻自己的理论。他与合作者Maier在《心理学评论》发表论文明确指出：被动不是后天习得，而是大脑出厂设置。

当你遭遇持续压力，大脑深处背侧中缝核会自动释放血清素，直接抑制行动冲动。无需学习，无需创伤，趴下不动就是大脑面对压力的默认反应。

人真正需要学习的，是控制感——大脑察觉某件事自己能够掌控，进而主动发出信号，压制躺平程序。神经科学称此为"习得性控制"，且这种控制感一旦掌握，可迁移至其他领域。

所以，那只趴地不动的狗，不是学会了无助，而是从未学会如何掌控。被动是出厂设置，主动需后天锻炼。你从小未特意训练掌控感，不是因为你愚笨、懒惰，而是大脑天生如此设计。

## 二、AI愈强，能动性者愈值钱：数据打脸"技术至上论"

Dan Koe有句话我反复读了三遍："成功比以前容易多了，但那些原本就不会成功的人依旧不会成功。"

AI确实将工具门槛降至极低：不会画画，AI帮你画；不会写代码，AI帮你写。但关键从来不是工具或信息，而是：你是否具备能动性去运用AI。

他还说："创作者的本质并非创作内容，而是构建语境。" AI能写文章、画图、剪辑视频，但不明白为何要做这些事、朝什么方向推进、提出什么问题、如何判断优劣——这些都需要人来完成。工具可能被替代，愿景和能动性不会。

用数据说话

- 内容质量：Lex 2025年7月分析60万个网页，谷歌排名靠前的内容中，纯AI创作仅占4.6%，人机协作占86.5%。
- 用户信任：2023年60%的人认可AI内容，到2025年仅剩26%，超半数人一旦察觉AI生成便直接划过。
- AI自身选择：ChatGPT和Perplexity等AI搜索引擎，82%引用的文章是人撰写的。连AI都在为人类投票！

麦肯锡2025年1月对3613名员工和238名高管调查得出结论：AI时代最大阻碍并非技术，而是人的主动判断力。92%企业要加大AI投资，但仅1%高管认为自家公司AI应用成熟。92%投入几乎付诸东流。

世界经济论坛2025年十大核心技能前五名：分析思维、韧性灵活性、领导力、创造力、自我认知——无一具体技术，全是人的底层能力。

哈佛商学院2025年发表在《自然》子刊研究：分析1000多种职业、7000万次职业转换，发现底层能力广泛的人学习速度更快、收入更高、抗风险能力更强。

Dan Koe说得犀利："社会期望你简单、易于预测、便于归类，但当下所有信号都表明：拒绝被归类的人才最具价值。"

## 三、如何训练能动性：Dan Koe的五步循环法

Dan Koe在文章结尾给出具体操作框架，我整理为五个可执行步骤：

（一）确定方向：从"不想要"反向推导

没人真正清楚自己想要什么，但大多数人清楚不想要什么——不想继续当前工作，不想过当下生活。从这些反向推导，就有前行方向。无需完美，选错可调整，关键是不做选择比选错更致命。

（二）研究他人路径：绘制简易地图

通过YouTube、博客、书籍、导师等，了解他人做法和踩过的坑。切勿一开始就闭门造车，先为自己绘制一张简易地图。

（三）勇于尝试：排除错误路径

Dan Koe特别强调：大部分方法可能不适合你，但这无妨。你不是在找正确答案，而是通过大量尝试缩小选择范围。每次失败并非毫无意义，而是排除了一条错误路径。

（四）识别模式：抽身思考底层逻辑

从所有尝试中抽身，探寻真正起作用的底层逻辑：在何种情况下效率最高？哪些事有天然优势？哪些事屡屡受挫？切勿一味埋头苦干，需适时停下来思考总结。

（五）分享自身方法：教学相长

将自己的方法分享给他人。Dan Koe说："老师比学生学到的更多"。当你能清晰阐述、书写方法并帮助他人时，理解便上升到全新高度。

这五个步骤不是直线完成即结束，而是一个循环。完成第五步后，会对第一步有全新理解，进而选择更精准方向再次循环。每循环一次，判断力和掌控力便增强一分。

习得性控制一旦练成，便可迁移。在一件事上获得的掌控感，在其他事情上同样有效。这五步循环的本质，是不断强化大脑对躺平默认程序的压制能力。

## 结语：从被动到能动，我用了三年

回顾从2005年至今的经历：上学、打工、失业、移民、换工作、创业、失败、再创业、做自媒体...我从未意识到"能动性"这一概念，但细想之下，从缺乏能动性到具备能动性的转变，大约历经三年。

关键转折是长达九个多月的失业期。每周去救济中心排队领钱，感觉无比丢人，又没钱可用。后来阴差阳错尝试销售工作，因经济所迫，不得不主动寻找解决方案，主动尝试错误并改正。

几乎每天遭受几十个客户拒绝，开车、打电话、发信息时都在赶赴下一个客户会议。几乎每天只吃一顿饭，因为被拒绝太多，后来竟觉得这样也挺好——通常被拒绝三十次就能促成一次交易。

如今回首，能动性便是在那时逐渐培养起来的。做销售如同打怪升级，任务、目标、标准、执行方案皆由自己设计。也算因祸得福。

AI时代已至，工具会越来越强，但唯一无法被替代的，是那个敢于定义游戏规则、在失败中迭代、始终掌控人生方向的"你"。

> 行动建议：今天就开始五步循环的第一步——写下3件你"不想要"的事，从中反向推导一个行动方向。哪怕再小，也要迈出第一步。因为选择本身，就是能动性训练的开始。

（本文核心观点源自Dan Koe X平台爆款文章及麦肯锡2025年AI报告，结合神经科学研究整理。数据来源已核实，可放心参考。）

---


**作者** ℏεsam（@Hesamation）  
**貼文連結** https://x.com/Hesamation/status/2041937789571285372  

**正文**

Anthropic killed 1000+ agent startups with Managed Agents:
> coding agents that ship prs
> finance bots that process docs instantly
> productivity agents that join your team
> infra you'd spend months building
THEY DID IT AGAIN. 

---


**作者** KK.aWSB（@KKaWSB）  
**貼文連結** https://x.com/KKaWSB/status/2042027814334165285  

**正文**

整个Agent创业领域今天都被彻底摧毁了。 
整个Agent创业领域今天都被彻底摧毁了。 
新推出的什么？怎么用？

---

