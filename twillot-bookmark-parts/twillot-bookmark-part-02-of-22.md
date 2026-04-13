# Twillot 書籤（精簡）— 第 2/22 部

原檔：`twillot-bookmark-2026-04-13.csv` · 全檔共 **4292** 則 · **本部第 196–390 則**（共 195 則）

---

**作者** Berryxia.AI（@berryxia）  
**貼文連結** https://x.com/berryxia/status/2042016446243631328  

**正文**

Claude Managed Agents 刚官宣没几个小时，开源版就来了！

@jiayuan_jy 直接把 Claude 的生产级 Agent 管理框架完整开源：

✅ 完整复刻 Claude Managed Agents 核心能力  
✅ 生产就绪的 Agent harness + 基础设施  
✅ 完全开源
 
Claude Managed Agents 刚官宣没几个小时，开源版就来了！

@jiayuan_jy 直接把 Claude 的生产级 Agent 管理框架完整开源：

✅ 完整复刻 Claude Managed Agents 核心能力  
✅ 生产就绪的 Agent harness + 基础设施  
✅ 完全开源
 
GitHub 直达👉 https://github.com/multica-ai/multica

---


**作者** Lance Martin（@RLanceMartin）  
**貼文連結** https://x.com/RLanceMartin/status/2041927992986009773  

**正文**

TL;DR – Claude Managed Agents is a pre-built, configurable agent harness that runs in managed infrastructure. You define an agent as a template – tools, skills, files / repos, etc. The agent harness and the infrastructure are provided for you. The system is designed to keep pace with Claude’s rapidly growing intelligence and support long horizon tasks. Some useful links:

- [Claude blog](<https://claude.com/blog/claude-managed-agents>): Usage patterns and customer examples
- [Engineering blog](<https://www.anthropic.com/engineering/managed-agents>): The design of Claude Managed Agents
- [Docs](<https://platform.claude.com/docs/en/managed-agents/quickstart>): Onboarding, quickstart, overview of the CLI and SKDs 

Why Claude Managed Agents

The Claude [messages API](<https://platform.claude.com/docs/en/build-with-claude/working-with-messages>) is a direct gateway to the model: it accepts messages and returns content blocks. Agents built on the messages API use a harness to route Claude’s tool calls to handlers and manage context. This poses a few challenges:

- Harnesses need to keep up with Claude – I recently wrote a blog [here](<https://claude.com/blog/harnessing-claudes-intelligence>) focused on building agents using Claude API primitives to handle tool orchestration and context management. But agent harnesses encode assumptions about what Claude can’t do. These assumptions grow stale as Claude gets more capable and can [bottleneck](<https://rlancemartin.github.io/2025/07/30/bitter_lesson/>) Claude’s performance. Harnesses need to be continually updated to keep pace with Claude.
- Claude is running for longer  – Claude’s [task horizon is growing exponentially](<https://metr.org/time-horizons/>), already exceeding over 10 human-hours of work on the METR benchmark. This puts pressure on the infrastructure around an agent: it needs to be safe, resilient to infrastructure failures that happen over long horizon tasks, and support scaling (e.g., to many agent teams).

Addressing these challenges is important because we expect future Claude to run over days, weeks, or months on humanity's greatest challenges. The [Claude Agent SDK](<https://platform.claude.com/docs/en/agent-sdk/overview>) was a first step, providing an excellent general purpose agent harness. Claude Managed Agents is the next step in this progression: a system with the harness and managed infrastructure designed to support safe, reliable execution over the time-horizon that we expect Claude to work.

How to get started

An easy way to onboard is to use our open source [claude-api skill](<https://github.com/anthropics/skills/tree/main/skills/claude-api>), which works out of the box in Claude Code. Get the latest version of Claude Code and run the following sub-command for Claude Managed Agents onboarding. I’m excited about skills as a way to onboard to new features, and have used this skill extensively:

Also see our [docs](<https://platform.claude.com/docs/en/managed-agents/quickstart>) for quickstart with the SDKs or CLI, and prototype agents [in Claude Console](<https://platform.claude.com/docs/en/managed-agents/onboarding>).

Use cases

You can see our [Claude blog](<https://claude.com/blog/claude-managed-agents>) for a number of interesting examples. Some of the common patterns I’ve noticed across these examples and my own work:

- Event-triggered: A service triggers the Managed Agent to do a task. For example, a system flags a bug and a managed agent writes the patch and opens the PR. No human in the loop between flag and action.
- Scheduled: Managed Agent is scheduled to do a task. For example, I and many others use this pattern for scheduled daily briefs (e.g., of X or Github activity, what a team of agents is working on). Here's an example daily brief of X activity that I use.

![Article Image](<https://pbs.twimg.com/media/HFZV93JaQAAbdHf.jpg>)

- Fire-and-forget: Humans trigger the Managed Agent to do a task. For example, assign tasks to the Managed Agent via Slack or Teams and get back deliverables (spreadsheets, slides, apps).
- Long-horizon tasks: Long-running tasks are an area where I think Managed Agents will be particularly useful. I’ve explored this by forking @karpathy's auto-research repo and exploring a few different ideas. For example, I recently took @\_chenglou’s excellent [pretext library](<https://github.com/chenglou/pretext>) and had a Managed Agent explore ways to apply it to our engineering blog content.

Key concepts

When onboarding, there’s three central concepts to understand:

- Agent — A versioned config that houses the agent's identity: model, system prompt, tools, skills, MCP servers, etc. You create it once and reference it by ID.
- Environment — A template describing how to provision the sandbox the agent's tools run in (e.g., runtime type, networking policy, and package config).
- Session — A stateful run using the pre-created agent config and environment. It provisions a fresh sandbox from the environment template, mounts any per-run resources (files, GitHub repos), stores auth in a secure vault (MCP credentials).

Think about an agent  as a configuration, an environment as a template describing the sandbox you want the agent to access for code execution, and the session as any agent execution. One agent can have many sessions.

Usage

See [docs](<https://platform.claude.com/docs/en/managed-agents/quickstart>) here:

- [SDKs](<https://platform.claude.com/docs/en/api/client-sdks>) – These are code-facing: import them in your app to drive sessions at runtime. Six languages have Managed Agents support: Python, TypeScript, Java, Go, Ruby, PHP.
- [CLI](<https://platform.claude.com/docs/en/api/sdks/cli>) – Terminal-facing: every API resource (agents, environments, sessions, vaults, skills, files) is exposed as a subcommand.
- Common patterns – Use the CLI for setup and SDK for runtime. Agents templates are persistent: you create one, store it (e.g., as a YAML with model, system prompt, tools, MCP servers, skills in git) and have the CLI apply it in your deploy pipeline.

How it works

I wrote an Anthropic engineering [blog post](<https://www.anthropic.com/engineering/managed-agents>) with @mc\_anthropic, @gcemaj, and @jkeatn on the process of building Claude Managed Agents: a lesson we share in the post is  that building agents to scale with Claude’s intelligence is an infrastructure challenge, not strictly a matter of harness design.

![Article Image](<https://pbs.twimg.com/media/HFZXR5pakAA8c4K.jpg>)

With this in mind, we didn’t design a particular agent harness; we expect agent harnesses to constantly evolve. Instead we decouple what we thought of as the “brain” (Claude and its harness) from both the “hands” (sandboxes and tools that perform actions) and the “session” (the log of session events). 

Each became an interface that made few assumptions about the others, and each could fail or be replaced independently. We share how this gives the system reliability, security, and flexibility to add future harnesses, sandboxes, or infrastructure to house sessions. 

Conclusion

I'm excited about projects exploring different patterns of multi-agent orchestration or long-running tasks. One of the frustrations [I've written about in the past](<https://rlancemartin.github.io/2025/07/30/bitter_lesson/>) is keeping agent harnesses up with model capabilities. Claude Managed Agents handles the agent harness and infrastructure for you, allowing for explorations on top of the agent as a new core primitive in the Claude API.

---


**作者** Carlos Donderis 🌊（@CaDs）  
**貼文連結** https://x.com/CaDs/status/2041644338388869593  

**正文**

Background agents work across the entire SDLC.
https://background-agents.com/

---


**作者** Henri Liriani（@hliriani）  
**貼文連結** https://x.com/hliriani/status/2041942337694363955  

**正文**

An agent is held back by the same problems as any new hire. It doesn’t know much about your company on day one, nor how to do great work there.

It doesn’t know why the company started, how initial traction was found, how the first few deals were done, who the happiest customers are, or where to find more of them. It doesn’t know how you do research, prep for meetings, keep contacts warm, or bring back lost deals.

So—just like for a new hire—we’ve now built a way to ramp Lightfield up so that it can be productive from day one, using a file system for skills and knowledge built directly into your CRM.

Skills can helpfully refer to low-level functionality in the CRM, and can be built for you by Lightfield’s own create-skill.

Examples of skills that you can build or use to customize existing functionality:

- Preparing for a meeting
- Account research with specific data sources
- Creating/updating CRM tasks
- Follow-up emails
- Sales call coaching

Similarly, knowledge can be uploaded directly to your CRM’s knowledge directory or be created for you with the agent. Lightfield will also create knowledge automatically via your conversations with your approval so it stays up to date.

Examples of extremely helpful knowledge we’ve given the CRM:

- Competitive positioning
- Case studies
- Sales process / methodology
- Pricing framework
- Product roadmap

Skills and knowledge can be invoked manually, via the agent, and even autonomously in workflows when referred to. Armed with this context, Lightfield can effectively replace much of the GTM work you do manually, and keep improving at it with feedback and use.

Give it a try, excited to hear what you think: https://lightfield.app/blog/introducing-skills

---


**作者** Ivan Landabaso（@IvanLandabaso）  
**貼文連結** https://x.com/IvanLandabaso/status/2041829214526058566  

**正文**

Dropping tomorrow: @harvey's Growth Playbook 
Dropping tomorrow: @harvey's Growth Playbook 
@harvey Now live:

https://x.com/IvanLandabaso/status/2042179119325082087

---


**作者** Ashpreet Bedi（@ashpreetbedi）  
**貼文連結** https://x.com/ashpreetbedi/status/2041901460523270409  

**正文**

Every company with 30+ people should have an internal data agent. 
Today I'm making it dead simple to build one: take Dash (free, open-source), run it in your cloud (private, secure), give your team

---


**作者** 来碗牛肉粉（@beefnoode）  
**貼文連結** https://x.com/beefnoode/status/2041693026360422431  

**正文**

我在调研软件行业时发现了一篇非常牛逼的优质长文
原作者是顶级VC @a16z 的David George，我对原文进行了编译
他对软件公司在AI时代的转型路径进行了非常细致的分析
文章观点的深度和建议的可落地性都非常高

---


**作者** Kimberly Tan（@kimberlywtan）  
**貼文連結** https://x.com/kimberlywtan/status/2041896368877531158  

**正文**

There has been a ton of speculation about the extent to which AI has actually penetrated large enterprises, but most existing information consists solely of self-reported AI usage or surveys that

---


**作者** Aparna Dhinakaran（@aparnadhinak）  
**貼文連結** https://x.com/aparnadhinak/status/2042022750135709882  

**正文**

Skills are probably one of the most important AI inventions of the last year, evaluation of skills and continual improvement is the most important topic of 2026.
 
We've spent the past year building,

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2042017036931305667  

**正文**

这个产品叫 Claude Managed Agents。一句话概括：你告诉 Anthropic 你想要什么样的 AI 智能体，它帮你在云端跑起来，基础设施全包，按用量收费。Sentry 用它几周就上线了自动修 bug 的全流程，Rakuten 一周部署一个专项智能体。之前这些事需要一整个工程师团队干几个月。

与此同时，Anthropic 的年经常性收入刚突破 300 亿美元，是去年 12 月的三倍。大部分增长来自企业客户。华尔街已经开始紧张了，WSJ 说投资者对传统 SaaS 公司的股价越来越谨慎，担心 Anthropic 这类产品会让一些传统软件服务变得多余。

这个产品到底是什么？和你已经在用的 Claude Code 有什么区别？技术上怎么做到的？

## 它是什么？和 Claude Code 有什么区别？

如果你用过 Claude Code，你知道 AI 智能体怎么工作：你给它一个任务，它自己规划步骤、调用工具、写代码、改文件，一步步把事做完。

Claude Code 跑在你自己的电脑上，是给开发者个人用的命令行工具。 你关了电脑，它就停了。

Managed Agents 跑在 Anthropic 的云上，是给企业用的 API 服务。 它可以 24 小时不间断运行，断线了也不丢进度，你的产品可以直接内嵌智能体能力。Notion 就是这么干的：用户在 Notion 里把任务分配给 Claude 智能体，智能体在后台干完活把结果交回来，用户全程不需要离开 Notion。

![Article Image](<https://pbs.twimg.com/media/HFayu1wXAAAlyLW.jpg>)

几种典型用法：

- 事件触发型：系统发现 bug，自动派智能体修复并提 PR，中间不需要人介入。
- 定时型：每天早上自动生成 GitHub 活动摘要或团队工作简报。
- 即发即忘型：在 Slack 里给智能体派个活，它做完把表格、PPT、App 交回来。
- 长时间任务型：跑几个小时的深度研究或代码重构。

## 和企业自己搭的云端智能体有什么区别？

能自己搭，但很贵很慢。

一个能上线的智能体，需要的东西远比“调一下 API”多得多：沙盒环境（sandbox，一个隔离的安全空间，AI 在里面跑代码、改文件，不管怎么折腾都不会影响外面的真实系统，相当于给 AI 一台专用虚拟电脑）、凭证管理、状态恢复、权限控制、全链路追踪……

很多企业客户之前需要一整个工程师团队专门搞这些。现在开箱即用，工程师可以去做产品真正核心的部分。

但 Managed Agents 解决的痛点还不只是省人力。

马东锡（@dongxi\_nlp）有一个精辟的总结：

Anthropic 工程博客里有一个具体的例子：Claude Sonnet 4.5 快到上下文窗口极限时会“焦虑”，草草结束任务。他们在调度框架里加了上下文重置来应对。但 Claude Opus 4.5 出来后，这个毛病消失了，之前的补丁反而变成了累赘。

你自己搭调度框架，每次模型升级你都得跟着改。交给 Anthropic，他们替你优化，严格来说他们优化了卖给你。

![Article Image](<https://pbs.twimg.com/media/HFay0D8XIAANYkH.jpg>)

## 谁在用？怎么用的？

Notion 让用户在工作区里直接把编码、做 PPT、整理表格这些活扔给 Claude，几十个任务并行跑，整个团队在同一个输出上协作。Notion 产品经理 Eric Liu 说，用户可以把开放式的复杂任务直接委托出去，不用离开 Notion。

Sentry 做了“从发现 bug 到提交修复代码”的全自动流程。他们的 AI debug 工具 Seer 找到问题根因后，Claude 直接写补丁、开 PR（代码提交合并请求）。工程总监 Indragie Karunaratne 说，几周就上线了，还省掉了持续维护自建基础设施的运营开销。

Atlassian 把它接进了 Jira，开发者可以直接在 Jira 里把任务分配给 Claude 智能体。

Asana 做了 AI Teammates，在项目管理里加入 AI 协作者，能接任务、交付物。

General Legal（法律科技公司）的玩法最有趣：他们的智能体能根据用户的提问，临时写工具来查数据。以前每个用户问题都得提前预判并开发检索工具，现在智能体自己按需生成。CTO 说开发时间缩短了 10 倍。

Rakuten 在工程、产品、销售、市场、财务各部门都部署了专项智能体，每个一周内上线，通过 Slack 和 Teams 接任务，交回来的是表格、PPT、App 这些实际交付物。

## 技术原理：大脑和手分开

Anthropic 工程团队写了一篇技术博客 [Scaling Managed Agents: Decoupling the brain from the hands](<https://www.anthropic.com/engineering/managed-agents>)，讲了 Managed Agents 背后的架构演进。

![Article Image](<https://pbs.twimg.com/media/HFay2o5WgAA1AgK.jpg>)

最早他们把所有东西塞进一个容器：AI 的推理循环、代码执行环境、会话记录，全在一起。好处是简单，坏处是鸡蛋全在一个篮子里，容器一挂，整个会话就丢了，而且没法单独替换某个部分。

后来他们做了一个关键拆分：

![Article Image](<https://pbs.twimg.com/media/HFay5N_XIAALx1w.jpg>)

- “大脑” 是 Claude 和它的调度框架，负责思考和决策。
- “手” 是沙盒和各种工具，负责执行具体操作。
- “记忆” 是独立的会话日志，记录发生的一切。

三者互不依赖，任何一个挂了都不影响其他两个。

这个拆分带来几个实际好处：

## 快

不是每个任务都需要启动完整的沙盒环境，现在只有 AI 真的需要跑代码时才按需启动。首次响应延迟中位数降了约 60%，极端情况降了超过 90%。

## 安全

AI 生成的代码跑在沙盒里，而访问外部系统的凭证存在沙盒外面的安全保险箱里，两边物理隔离。比如访问 Git 仓库，系统初始化时就把代码克隆好了，AI 正常用 git push/pull，但 Token 本身对 AI 不可见。对于 Slack、Jira 这类服务，通过 MCP 协议接入，请求经过代理层，代理层去保险箱取凭证调服务，AI 全程不经手凭证。

![Article Image](<https://pbs.twimg.com/media/HFay7_wXoAAMhaM.jpg>)

## 灵活

大脑不关心手是什么。工程博客里有句话很有意思：调度框架不知道沙盒到底是一个容器、一部手机、还是一个宝可梦模拟器。 只要符合“名字和输入进去，字符串出来”的接口就行。

这也意味着多个大脑可以共享手，一个大脑可以把手交给另一个大脑，为多智能体协作打下了基础。

## 局限性

Managed Agents 并不是万能的。几个需要注意的点：

部分功能还在研究预览阶段。 多智能体协作、高级记忆工具、自我评估迭代（让智能体自己判断任务完成质量并反复改进）这些能力目前还没有全面开放，需要申请才能使用。

平台绑定。 选择 Managed Agents 意味着你的智能体基础设施绑在了 Anthropic 生态里。如果未来想换模型或换平台，迁移成本不可忽视。

上下文管理仍然是难题。 虽然会话日志独立存储，但长时间任务中哪些信息该保留、哪些该丢弃，仍然涉及不可逆的决策。这是一个持续挑战，他们目前的做法是把上下文存储和上下文管理分开：存储保证不丢，管理策略随模型进化调整。

成本可预测性。 0.08 美元/会话小时听起来不多，但智能体跑几个小时的复杂任务，Token 消耗加上运行时费用，成本可能不低。企业需要做好预算评估。

Managed Agents 说明大多数企业离“全面用 AI 智能体干活”还有很长的路要走。基础设施的门槛降低了，但怎么定义好的任务、怎么设计好的工作流、怎么建立信任让 AI 接触核心业务数据，这些问题 Managed Agents 帮不了你。

## AI 智能体基建的“AWS 时刻”

看起来 Managed Agents 走的是 AWS 当年的老路：先有了计算能力，然后把运行环境也包了。十年前企业纠结“上不上云”，现在纠结“Agent 基础设施自建还是托管”。历史经验告诉我们，大多数企业最终会选择托管，因为基础设施从来不是核心竞争力。 OpenAI 也推出了自己的 Agent 平台 Frontier，这个赛道的竞争刚刚开始。

从技术角度看，“大脑和手分离”这个架构思路值得关注。它让系统的每个部分都可以独立演进：模型升级了，换大脑；需要新工具，加一双手；存储方案改了，替换记忆层。工程博客里的类比说得好：操作系统的 read() 命令不关心底下是 1970 年代的磁盘还是现代 SSD，抽象层稳定了，底下的实现随便换。

从使用角度看，如果你是企业开发者，想在自己的产品里嵌入 AI 智能体能力，Managed Agents 可能会省掉你几个月的基础设施工作。六种语言（Python、TypeScript、Java、Go、Ruby、PHP）有 SDK 支持。如果你已经在用 Claude Code，更新到最新版，输入 /claude-api managed-agents-onboarding 就能开始。如果你是普通 AI 爱好者，短期内最直观的感受可能是：你用的那些 SaaS 产品里，会有越来越多的 AI 智能体在后台帮你干活，而这些智能体很可能就跑在 Managed Agents 上。

定价参考：Token 费用按 Anthropic API 标准价格，运行时 0.08 美元/会话小时（空闲不计费），网页搜索 10 美元/千次。

你觉得 AI 智能体的基础设施，最终会像云计算一样被几家大厂垄断吗？

---


**作者** 独立开发者William（@DLKFZWilliam2）  
**貼文連結** https://x.com/DLKFZWilliam2/status/2041960458891227632  

**正文**

这条有点长，算是一半新闻，一半我个人的感慨吧。

Anthropic推出了Claude Managed Agent. 
Asana、Rakuten、Sentry、Notion 等公司在几天到几周内就部署了自己的专业 Agent。

我最近是有点悲观了。1/n 
这条有点长，算是一半新闻，一半我个人的感慨吧。

Anthropic推出了Claude Managed Agent. 
Asana、Rakuten、Sentry、Notion 等公司在几天到几周内就部署了自己的专业 Agent。

我最近是有点悲观了。1/n 
其实过去一年，大家都在喊“Agent 是未来”，可是似乎做的事情还是“拿Agent帮忙写代码，我们人类做产品”

我也一直再思考这个问题：未来的产品怎么做？

程序员最开始本质上解决的就是把业务逻辑实现的问题。 是整个商业逻辑的一环。

上游是AI，下游是客户，我们夹在中间。2/n
而一个商业化的产品，就是找到需求，把业务逻辑变成工程的问题，然后以工程的方式解决问题。

Vibe Coding把编程这个“工程方式”解决“业务逻辑”的问题基本解决了，这样产品就能快速上线。

这把 产品落地门槛大幅降低了。 3/n
可是如果整个商业逻辑直接能全部Agent实现呢？ 能只需要找到需求，描述清楚需求，直接能解决问题，这样技术的溢出会迅速拉平所有“未解决的需求”，在“有新需求”的瞬间，客户会绕过我们，直接找到AI，直接解决问题。 是否已经没有做产品的需要了呢？

这种业务还有几年的机会？ 4/n
作为个人和小团队，既无法向上整合去做大模型AI这个上游，同时下游的客户也在流失，我们的议价能力两头都很弱，按照商业的分析，这种业务非常容易被蚕食消亡。

不过，乐观（也许也是悲观）的想，所有的业务也都在被蚕食，快慢不一而已。 5/5

---


**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2041952121516679211  

**正文**

We built the best codebase search to give any agent grounded information from GitHub repos.

Introducing Sandbox Search.

Point it at any repo, and we’ll spin up a secure coding agent in its own sandbox to do research for you.

Use inside claude code, openclaw, cursor, and more. 

---


**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2041892453582836115  

**正文**

发现了一个牛逼的新产品 Moxt

交互和产品的设计将新的 Agent 体系融合得非常好，门槛很低。

可以非常好的帮你将你的和团队的上下文变成工作的助力

---


**作者** Rimsha Bhardwaj（@heyrimsha）  
**貼文連結** https://x.com/heyrimsha/status/2041819915636859017  

**正文**

🚨BREAKING: Claude can now find your startup's fatal flaw the way Paul Graham does in the first 5 minutes of an interview (for free).

Most founders discover it at month 8. Some never do.

Here are 9 Claude prompts that surface the real problem before you build the wrong thing.

(Save before you hire)
🚨BREAKING: Claude can now find your startup's fatal flaw the way Paul Graham does in the first 5 minutes of an interview (for free).

Most founders discover it at month 8. Some never do.

Here are 9 Claude prompts that surface the real problem before you build the wrong thing.

(Save before you hire)
Prompt 1 — The Demand Audit

"I'm building [product] for [customer type]. You are a skeptical YC partner who has seen 10,000 pitches. Ask me 7 questions that expose whether real demand exists or whether I am solving a problem I personally have that nobody else actually pays to fix. After each question, tell me what a weak answer sounds like versus what a strong answer sounds like."
Prompt 2 — The Competitor Blindspot Test

"Here is my competitor analysis: [paste it]. You are a strategic analyst who has studied every major startup failure in my category. Find the 5 things I am missing about why customers might stay with existing solutions instead of switching to mine. Be specific about switching costs, habits, and emotional attachment to current tools."
Prompt 3 — The Business Model X-Ray

"My revenue model is [describe it]. My average contract value is [X]. My estimated CAC is [X]. Walk me through every way this model breaks at 100 customers, then at 1,000, then at 10,000. Tell me exactly where unit economics collapse first and what the warning signs look like 3 months before it happens."
Prompt 4 — The Why Now Interrogation

"My startup is [describe it]. The market has existed for [X years]. Give me the 5 strongest arguments for why now is the wrong time to build this and why the timing window might already be closing. Then give me the single best argument for why right now is actually the only window that will ever exist. Force me to defend my timing."
Prompt 5 — The Customer Interview Stress Test

"Here are notes from 10 customer interviews I conducted: [paste notes]. You are a behavioral economist who specializes in the gap between what people say and what they actually do. Identify which statements are genuine buying signals, which are politeness disguised as validation, and which reveal a problem I have not yet understood correctly. Rank them by signal quality."
Prompt 6 — The Hiring Trap Detector

"I am about to hire for [role] because I believe it will solve [problem]. List every assumption I am making about what this hire will fix. Then tell me which of those assumptions are likely wrong, which problems will get worse after I hire, and what I should prove before making this my first hire instead of my third."
Prompt 7 — The Churn Pre-Mortem

"My product does [describe core value]. My onboarding flow looks like [describe it]. Walk me through the 7 most likely reasons my first 20 customers stop using the product within 90 days even if they loved the sales demo. For each reason, tell me the earliest signal I could detect it and what I would need to change to prevent it."
Prompt 8 — The Co-founder Conflict Map

"My co-founder and I split responsibilities like this: [describe the split]. We have agreed on the following things: [list agreements]. You are a startup therapist who has witnessed 50 co-founder breakups. Identify the 5 decision points in the next 18 months where our structure will create serious conflict if we do not align now. Tell me what the fight actually looks like when it happens."
Prompt 9 — The Investor Rejection Simulator

"Here is my full pitch deck narrative: [paste it]. You are a top-tier VC who has passed on 200 companies that went on to raise Series A. Give me the exact internal reasoning you would use to pass on this company after a 20-minute meeting. Do not soften it. Tell me what you would say to your partner after I left the room."
I hope you've found this thread helpful.

Don't forget to bookmark for later.

Follow me @heyrimsha for more.

If you enjoyed reading this post, please support it with like/repost of the post below 👇

---


**作者** Luyu Zhang（@goocarlos）  
**貼文連結** https://x.com/goocarlos/status/2041852633179418687  

**正文**

我们把整个人事系统搬进了终端 -- Cyber POps😮。

查同事、看组织架构、发徽章、办离职——全在命令行里完成，没有管理后台。

但它不只是 HR 工具。它同时是一套完整的单点登录系统——Google OAuth、Passkey、SSO 全部内置。内部开发者只需要几行代码，就能让自己的 CLI 工具或 Web 应用接入统一的身份和组织关系。

这是一次实验：当 CLI 足够好用、AI Agent 可以直接操作的时候，企业软件还需要从 UI 开始设计吗？先把数据模型和 Agent 能力做对，GUI 可能只是最后一层渲染。

24 小时内用 AI 从零构建。

https://mesh.langgenius.ai

---


**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2041819565101871574  

**正文**

恭喜 Mario @badlogicgames 🎉

在 OpenClaw 创始人加入 OpenAI 后，它背后的 Agent 框架 Pi 也和创始人一起加入 Earendil (http://earendil.com)，pi 成为 Earendil 旗下的开源项目，Mario 保留技术主导权，同时获得团队支持。
https://mariozechner.at/posts/2026-04-08-ive-sold-out

历史教训：RoboVM 的创伤
Mario 详细回顾了 2014-2016 年间 RoboVM 的经历：
· RoboVM 最初是开源项目，后成立公司并推出商业插件（保持核心开源）
· 被 Xamarin 收购后，微软立即关闭源代码并终止项目
· 作为"开源倡导者"的 Mario 被迫发布"不再开源"的公告，遭受社区激烈批评

现实压力：pi 的意外走红
· Peter 基于 pi 构建的应用爆红后，Mario 成为"连带责任人"
· 过去两个月每天 3-5 个电话，来自各路 VC 和大公司
· 他意识到 pi 有商业价值，但明确拒绝：
  · 独自创业当 CEO（不想重复管理压力）
  · 接受 VC 资金（担心重蹈 RoboVM 覆辙）
  · 牺牲家庭时间（4岁孩子曾因"爸爸不在"哭泣）

btw... 家庭这方面太有同感了，我也有一个 6 岁的孩子，离职半年后迟迟不能全职工作，最主要的考虑就是对孩子和家庭的陪伴了。

选择 Earendil 的逻辑
经过 9 个月的观察与互动（从 2025 年 4 月的"VibeTunnel"实验到多次办公室访问），Mario 确认：
· @mitsuhiko（Sentry 创始人）：开源商业化经验丰富，价值观一致（"开源是必需品而非装饰"），技术共鸣强
· Colin：处理 Mario 不愿碰的商业/管理事务，产品嗅觉好
团队氛围：Cristina、Jakob 等早期成员都是通才且"人很好"，几乎所有人都有孩子（与 Mario 的家庭优先价值观契合）
· 投资者质量：熟悉且尊重开发者工具领域的投资人

对 pi 开源项目的影响
· 所有权：归 Earendil 公司所有、但 Mario 保留技术决策权
· 代码仓库：迁移至 earendil-works/pi、但 MIT 许可证永久不变
· 包名：改为 @ earendil/pi、但功能与使用方式不变
· 商标：Earendil 持有 pi 商标、但防止滥用，非控制手段 
· 治理：三人决策（Mario/Armin/Colin）
·社区：Discord 保持独立

---


**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2041882523429695855  

**正文**

最近焦虑到要炸，AI 发展太快，每天信息灌太多了。

看到一句话直接戳天灵盖：你文件夹里的东西，95% 是噪音，不是资产。

这个Moxt有点意思，这东西本质是一个 Agent-Native 的在线工作空间，你可以在里面雇 AI 员工，给角色、给规则、给定时任务，它自己跑。

这样做的好处：

自己电脑上的信息和文件绝对安全，只把工作中需要协作的文档放到 Workspace 里和团队共享。

也不用自己盯项目进度了，做一个 Skill，设个定时任务扫团队空间的项目文档就行。

它每周自动扫描 Workspace，把腐烂信息归档，只保留当前最有价值的内容。

---


**作者** AIGCLINK（@aigclink）  
**貼文連結** https://x.com/aigclink/status/2041722658656862529  

**正文**

一个开源Agent长期记忆系统：Hindsight，使Agent不只是记住对话历史，而是能真正学习和积累经验

在LongMemEval上拿了SOTA，两行代码即能接入

Hindsight核心创新是其仿生记忆架构，让AI不仅能记住刚才说了什么，还能像人一样积累经验，学习成长

对需要记住用户长期偏好做复杂决策支持场景的，比如搞AI数字员工（AI项目经理、AI销售、AI客服等）、长期陪伴型应用的等等，可以看看

它把AI记忆分成世界事实、个人经历、心智模型三类，不是只保存原文，是把内容拆解整理，提取关键实体、时间、关系，结构化存储

然后会同时用语义理解、关键词匹配、关系图谱、时间筛选四种方式搜索，综合选出最相关的答案

会主动分析"个人经历"里的记录，生成新规律存进"心智模型"，比如说，从多次被拒场景中总结出"XX企业预算紧张"，下次就直接调用不用从头分析，实现越用越聪明

Claude Code、Cursor、OpenClaw等都有现成集成

支持Docker一键部署，或使用嵌入式版本无需服务器

#AI记忆 #Hindsight #AIMemory
一个开源Agent长期记忆系统：Hindsight，使Agent不只是记住对话历史，而是能真正学习和积累经验

在LongMemEval上拿了SOTA，两行代码即能接入

Hindsight核心创新是其仿生记忆架构，让AI不仅能记住刚才说了什么，还能像人一样积累经验，学习成长

对需要记住用户长期偏好做复杂决策支持场景的，比如搞AI数字员工（AI项目经理、AI销售、AI客服等）、长期陪伴型应用的等等，可以看看

它把AI记忆分成世界事实、个人经历、心智模型三类，不是只保存原文，是把内容拆解整理，提取关键实体、时间、关系，结构化存储

然后会同时用语义理解、关键词匹配、关系图谱、时间筛选四种方式搜索，综合选出最相关的答案

会主动分析"个人经历"里的记录，生成新规律存进"心智模型"，比如说，从多次被拒场景中总结出"XX企业预算紧张"，下次就直接调用不用从头分析，实现越用越聪明

Claude Code、Cursor、OpenClaw等都有现成集成

支持Docker一键部署，或使用嵌入式版本无需服务器

#AI记忆 #Hindsight #AIMemory
github：https://github.com/vectorize-io/hindsight 

---


**作者** 杀破狼 WolfyXBT（@wolfyxbt）  
**貼文連結** https://x.com/wolfyxbt/status/2041704596704546948  

**正文**

有没有那么夸张 🤣

Anthropic 刚刚宣布新的模型 Mythos，但是因为这个模型的网络攻击能力实在是太强了，所以目前暂时不会公开，他们担心一旦扩散，会被人恶意用于进行大规模的网络攻击。

所以 Mythos 会先限量提供给 Apple、Amazon、Google、Microsoft、Cisco、CrowdStrike、Linux Foundation 等等总共 12 家核心伙伴和 40 多家网络基础设施组织，先帮他们大规模扫描和修复漏洞。

这个是 Mythos 和 Opus 4.6 的跑分结果对比 👇

---


**作者** Yangyi（@yangyi）  
**貼文連結** https://x.com/yangyi/status/2041844948174303331  

**正文**

我为这个暴论补充一些说明：

首先 这话不是我说的 是codex团队的研究员说的

其次 10亿token是可以达到的 只要有一套harness工程 自然就会达成

最后 消耗十亿token不一定能做出什么东西
但是十亿token消耗不到 说明迭代速度上是慢的 是没有agent化的  是明显没有端到端HITL去完成生产环节的 

---


**作者** Bill Gurley（@bgurley）  
**貼文連結** https://x.com/bgurley/status/2041646611864879134  

**正文**

Fun, surreal, and exciting to see it in the wild! 

---


**作者** qinbafrank（@qinbafrank）  
**貼文連結** https://x.com/qinbafrank/status/2041828160225042516  

**正文**

从AI之前的五次创新浪潮里能学到什么？这是大摩最新的一份报告，英文原题是《Lessons from the Five Innovation Waves That Preceded AI》，由首席美国经济学家Michael Gapen领衔。这篇报告的核心问题只有一个：AI浪潮到底会怎样改变美国经济？摩根士丹利没有选择预测未来，而是选择了回看过去。他们系统梳理了美国过去250年经历的五次重大技术革命，试图从中提炼出适用于AI时代的共同规律。

1、五次创新浪潮
过去250年，美国经历了五次由突破性技术集群驱动的创新浪潮：
第一次是工业革命（约1790s-1840s），核心是工厂、蒸汽动力、运河和早期铁路，持续约60年；

第二次是蒸汽、铁路与钢铁时代（1830-1910），铁路里程从1860年的3万英里飙升到1900年的19.2万英里，持续约55年；

第三次是电气化与内燃机时代（1890s-1940s），1902年到1929年间美国发电量增长超过十倍，福特Model T在1908年面世，持续约50年；

第四次是电子与航空时代（1940s-1980s），晶体管发明、喷气式客机、州际公路系统，联邦研发开支占GDP的比重翻了四倍，持续约40年；

第五次是互联网与数字网络时代（1990s-2020），到2000年约一半美国家庭接入了互联网，持续约30年。

一个明显的趋势是：
每一波比上一波扩散得更快。 如果这个规律延续，AI的扩散速度可能超过互联网。

正好我在2月中也有聊过：
移动互联网花了10年时间走完了互联网需要20年的道路，而AI可能需要更短的时间就能走完移动互联网10年的发展之路。

2、六条反复出现的规律
跨越250年的五次浪潮，摩根士丹利提炼出六条高度一致的共同模式。
1）资本开支的巨大脉冲。 
创新浪潮从来不是温和渐进的。运河建设在高峰期占GDP的1%（相当于今天的约3150亿美元），铁路投资在1872-1881年间平均占GDP的2.5%（约7900亿美元），且经常超过全国总资本形成的10%。报告直言，如果要给当前AI投资热潮找一个历史对标物，就是铁路投资。

2）劳动力被重新配置而非消灭。 
每一次浪潮都引发了对大规模失业的恐惧，但历史上从未成真。农业就业占比从1800年的75%降到1910年的30%再到今天的不足2%，但总就业需求从未崩溃。工作的构成改变了——从手工匠人到工厂工人，从蓝领到白领，从制造业到服务业，从中等技能岗位到两极化分布——但工作本身一直延续。

3）生产率提升需要时间和组织变革。 
早期扩散慢且不均匀，但一旦配套投资和管理模式到位，产出效率就会加速。工业革命年均约0.8-1%，铁路时代翻倍到约2%，电气化时代实现了"大飞跃"（1900-1929年非农每小时产出翻番），互联网时代在1990年代末从1.5%加速到3%。但每次加速都滞后于技术发明本身10-20年。

4）繁荣-衰退周期是标配。 
1837年运河崩盘，1873年和1893年铁路恐慌，1929年股灾和大萧条，2000年互联网泡沫破裂。模式惊人地一致：狂热投资→投机融资→杠杆攀升→预期调整→痛苦出清。金融市场既加速了技术扩散，也放大了周期波动。

5）不平等走向取决于制度而非技术。 
镀金时代的极度财富集中，到1940-1970年代的"大压缩"（工会、累进税、教育扩展推动收入差距缩小），再到1980年后的不平等持续扩大——技术本身不决定分配结果，制度和政策才是关键变量。

6）教育体系每次都被迫转型。 
工业革命催生公立小学，铁路时代催生赠地大学，电气化时代推动高中运动，战后GI Bill扩展高等教育，互联网时代加强STEM需求。当教育扩展充分时，技术红利被广泛分享；当教育滞后时，不平等就加剧。

3、对AI时代的六大启示
基于历史规律，摩根士丹利对AI浪潮给出了六条判断：
1）生产率提升大概率发生， 但需要配合组织重新设计。
2）劳动力置换是过渡性的， 岗位构成会变化，但就业不会消失。
3）繁荣-衰退周期几乎必然， AI基础设施投资与铁路/电信建设高度相似。
4）不平等风险处于高位， 收入和财富不平等已达125年来最高，AI的可扩展性可能进一步加剧集中。
5）教育和再培训将是决定性因素， AI可能需要终身学习体系而非传统学位路径。
6）政策制度至关重要， 反垄断、社会保障、人力资本投资决定了红利是被广泛分享还是被少数人垄断。 

4、如果这次不一样呢？
摩根士丹利也讨论了一个重要的风险场景。AI作为通用技术，跨行业覆盖面可能比以往任何技术都广，扩散速度也在加快。

在极端情况下，AI可能不是辅助劳动力而是替代劳动力。如果走到那一步，经济可能经历一次向高增长的体制转换，同时伴随劳动收入份额的急剧下降和不平等的大幅恶化。

报告并未排除这种可能性，但认为历史仍然是形成基准预期的最佳参照。

---


**作者** yofine（@yofine2js）  
**貼文連結** https://x.com/yofine2js/status/2041821533992317407  

**正文**

爱马仕架构图 
爱马仕架构图 


---


**作者** Carlos E. Perez（@IntuitMachine）  
**貼文連結** https://x.com/IntuitMachine/status/2041583183146229761  

**正文**

Most people think AI skill = writing better prompts.
That's like thinking cooking skill = reading recipes louder.
Here's what's actually happening:
The AI industry has discovered 4 engineering

---


**作者** indigo（@indigox）  
**貼文連結** https://x.com/indigox/status/2041779085945516059  

**正文**

不要让 AI 为你写作的三个理由 by Alex H. Woods https://alexhwoods.com/dont-let-ai-write-for-you/

1. 写作的本质是思考

写作不是为了「写完」，而是为了增进自己的理解，然后增进他人的理解。任务是走进混沌，然后带着结构和理解走出来！AI 代写 = 雇人替你健身。

2. 信任的代价

当你发给别人的文件「带着 AI 气味」，你只是证明了 AI 生产了一些近似别人想听的东西——你没有证明你真正思考过这些想法。这损害了你作为「能领导这件事的人」的可信度。更糟的是：如果文字是自动生成的，想法也是吗？

3. AI 在写作过程中的合理用途

• 研究和核实
• 快速记录信息/转录
• 生成想法：这是 AI 最适合的——生成 10 个，只有 1 个有用也没关系，取有用的，丢掉其他的；

现在的 LLM 将提高交付写作 or 软件的效率。但为了充分利用它们，我们需要同步提升我们深思熟虑的程度🤔

---


**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2041865199485936018  

**正文**

THE CLEAREST PATH TO A $10M+ SOFTWARE EXIT in 2 YEARS (with AI and agents)

building an agency right now is one of the most interesting business moves 

the productized agency had its moment in 2022. it collapsed because scaling humans is a nightmare. inconsistent output, people quitting, margins getting crushed. most of the founders (and creators) who tried it got burned and moved on

but the thesis was right. the labor problem is just solved now with AI, claude code, openclaw etc.

here's the actual playbook i'd run today:

pick one painful deliverable for one specific buyer. like SEO content for e-commerce brands doing $1M+ but not "marketing."

or like ad creatives for DTC brands spending $50k/month on meta. one thing. one customer. that's it

then you build the AI workflow behind it. 

 you're selling an outcome on a monthly retainer. $3-5k/month. 80%+ margins because your cost is compute and a few hours of QA

"BuT tHaT'S nOt a BiG bUsInnesS"

okay but you're still swinging for the fences

because the agency IS the research and development for your agent SaaS

every client is paying you to figure out what to automate. you're learning what breaks, what scales, what customers actually want. 

by month 4 you know exactly what to productize. you build the software on top of the workflow you've already proven works and already have customers paying for

agency funds the agent SaaS. SaaS scales without the agency overhead. the clients become your first software customers

now let's talk about what this actually looks like financially

year 1: 10 clients at $4k/month. $480k revenue. 2 people. maybe $80k in costs including compute, tools, one part time VA. you're taking home $400k between two people while building the software in the background

year 2: you launch the software. your 10 agency clients are the first to convert. they already trust you. they've seen the output. you charge $800/month for the software version. now you have recurring software revenue AND the agency still running

year 3: agency is winding down or running on autopilot. software has 200 customers at $800/month. that's $1.9M ARR. 2-3 person team. 85% margins. you are now a very attractive acquisition target

the exit math is interesting. SaaS at $1.9M ARR with strong retention trades at 5-8x revenue. that's a $10-15M exit for something two people built in 3 years starting with zero VC

CAVEAT:

Startups are hard. A lot needs to go right. 

But from a framework perspective, I think this probably the lowest risk, highest reward option for lots of of folks

and most of the businesses cost $0 to start

basically

this is the most capital efficient path to a software exit that exists right now 

happy building

---


**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2041846335343841444  

**正文**

让AI真正懂你：我做了个"灵魂挖掘"技能😎

"We know more than we can tell."
 我们知道的，远多于我们能表达出来的。

 — Michael Polanyi，《The Tacit Dimension》，1966

前几天刷推的时候，无意间看到了 Michael Polanyi 这段话↑...

然后被深深触动了一下...

为了让 AI 更懂我，我写了详细的系统提示词、品牌人设、写作指南、记忆系统……加起来几万字的配置。

但 AI 还是不够懂我。

Michael Polanyi是一个匈牙利裔的英国化学家，后来转行搞哲学，在 1966 年提出了一个概念叫"隐性知识"（Tacit Knowledge）。

核心就一个观点：人类的知识分两种，一种能说出来，一种说不出来。说不出来的那种，他叫"隐性知识"。

注意，这里的"说不出来"不是"还没想好怎么说"，是结构性的说不出来。

突然发现我们和AI交流的时候就是很多隐性的知识不能被AI所获得，我们有时候也表达不出来...

不是 AI 不够聪明，也不是我的提示词不够详细。而是我最重要的那些判断标准，我自己也说不清楚。

什么样的开头算"对味"？为什么这个选题"一看就知道要写"而那个不行？什么叫"AI 味"？这些东西就像骑自行车，你会骑，但你写不出一份让从没骑过的人照着做就能骑的说明书。

Polanyi 把这种东西叫做隐性知识。他说，这不是"暂时说不出来"的问题，而是结构性的不可言说，有些知识的本质就决定了它没法被完全转化成文字。

---


**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2041790048715338223  

**正文**

红杉发布了一篇博客，题为《服务即新软件》。

看看这张图：价值超过 1 万亿美元的服务，正在被 AI Agent 取代。 

---


**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2041792320639815910  

**正文**

Karpathy 的"第二大脑"概念直接干掉了 RAG。

现在 LLM 可以把论文、代码库和笔记变成一个不断进化、越来越聪明的活维基。

而且人们已经在用它做各种疯狂的应用了。

以下是 10 个例子： 

---


**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2041796282742927418  

**正文**

🧵Thread: 为什么产品经理必须同时是首席故事官

1/ 大多数科技公司把产品管理和产品营销分成两个岗位。
这是个严重错误。

【Tony Fadell（iPod之父）的核心判断】：这两件事从来就是同一份工作。

一个Thread讲清楚👇 

---


**作者** vas（@vasuman）  
**貼文連結** https://x.com/vasuman/status/2041754834651779568  

**正文**

Claude Mythos just refactored my entire codebase in one call.

25 tool invocations. 3,000+ new lines. 12 brand new files.

It modularized everything. Broke up monoliths. Cleaned up spaghetti.

It worked. 

---


**作者** 梓哲悟语 | Zenzhe（@Zenzhe99）  
**貼文連結** https://x.com/Zenzhe99/status/2041687309037326734  

**正文**

安德烈·卡帕西解释了埃隆·马斯克的独特之处。💐🐮

“我觉得人们并不真正了解埃隆的风格有多么独特。你读到过相关报道，但你并不真正理解——这很难用语言来描述。”

领导特斯拉自动驾驶计算机视觉团队的卡帕西观察到的第一条原则是，马斯克喜欢规模小、实力强、技术含量高的团队：

“在公司里，团队自然会发展壮大。埃隆一直反对扩张……我基本上得苦苦哀求他才肯招人。还有一点，在大公司里很难裁掉低绩效员工。埃隆却很乐意裁掉低绩效员工。我实际上不得不努力留住团队成员，因为他总是想方设法把人踢出去……所以，一定要保持团队规模小、实力强、技术精湛。绝对不能有非技术背景的中层管理人员。这是最重要的。”

第二点是，埃隆希望办公室成为一个充满活力的地方，每个人都在做令人兴奋的事情：

他不喜欢停滞不前……他不喜欢大型会议。他总是鼓励那些在会上没有贡献的人离开。你确实会看到这种情况：在大型会议上，如果你没有做出贡献或学到东西，就直接走人。公司非常鼓励这种做法……我认为很多大公司都过于溺爱员工，但这里这种情况要少得多。这里的文化是，你来这里就是为了发挥你最好的技术才能，而且工作强度很高。

埃隆与团队的联系之紧密也非同寻常：

“通常情况下，公司的CEO是远程办公的，层级比公司高出五层，只跟副总裁沟通……一般人99%的时间都花在跟副总裁沟通上。[埃隆]可能只花50%的时间跟副总裁沟通。他只想跟工程师交流。如果团队规模小而精干，那么工程师和代码才是真理的来源……而不是某个经理。他想跟他们沟通，了解实际情况，以及应该如何改进。”

最后，卡帕西认为，马斯克对公司日常运营和消除瓶颈的参与程度并未得到充分重视。他举例说，工程师们会告诉马斯克GPU不够用。卡帕西解释说，如果马斯克听到这样的抱怨两次，他就会打电话给负责GPU集群的人。如果瓶颈出在英伟达，他就会打电话给黄仁勋。

---


**作者** Ray Dalio（@RayDalio）  
**貼文連結** https://x.com/RayDalio/status/2041531182018367773  

**正文**

I will start off by wishing you well in these challenging times and by saying that the picture I paint in the following observations is not the picture I wish to be true; it is the picture that I

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2041509264221483449  

**正文**

因为太多人写过 Andrej Karpathy 的 LLM Wiki，我就没写，其实在我心中比 Auto Research 更有创意，Auto Research 本身不新鲜，早就有相关理论，但 LLM WIKI 倒是让我眼前一亮。

我们每个人或多或少都在做信息收集的工作，比如 X 上看到好的文章点赞或者收藏，看到一篇好的技术文章添加到浏览器收藏夹，微信上有人分享了篇好文章点收藏，还有更多的是惊鸿一瞥再也找不到然后想起来根据关键词去 Google ……

其实绝大部分收藏后再也不会打开，一方面是因为收藏即看过的心理暗示，一方面是因为散落各地找起来太麻烦。

所以第一个问题其实是中心化的信息收集整理，把散落在各处的信息汇聚在一处。

已经有很多工具了，我自己也有写小工具/agent 帮助收集信息，因为我除了收集外还有一些二次加工的需要，比如翻译、总结。

但还存在问题就是信息是点状的，最多人工打个tag、加个分类。

但 Karpathy 的更进一步，让 LLM 帮你把信息整理成结构化的。这一步是我之前没考虑过的，也没见过有其他产品做的。

这里面的差别在于以前整理是要人做的，你自己建分类，自己打 tag，对于勤劳的爱整理的人当然没问题，但对于我这种懒人来说是不会做的，所以找信息是比较麻烦的。

但如果这种事情让 Agent 做，那就省事多了，毕竟它不知疲倦，而且极擅长处理内容。

只要稍加调教，它就能帮你把信息整理得井井有条，编程成你自己喜欢的格式，就像你的秘书一样，你只要去看看 WIKI 就可以方便的找到需要的信息，不需要以前那样去各个地方用关键字找。

这里面最核心是思路的转变，信息的收集和整理，不再是人主动的行为，而是 AI Agent 在帮你做这些事情，你所要做的就是每天去看属于自己的 WIKI。

---


**作者** Dhravya Shah（@DhravyaShah）  
**貼文連結** https://x.com/DhravyaShah/status/2041638116294058149  

**正文**

Today, we are launching supermemory support to your Hermes agent
TLDR: you can use supermemory now in your Hermes agent, it totally free to get started - https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers#supermemory
In case you missed it:

---


**作者** Andy Stewart（@manateelazycat）  
**貼文連結** https://x.com/manateelazycat/status/2041721391284941097  

**正文**

开源世界从不缺大牛，缺的是把事情做到极致的人

有一种黑魔法，能把大语言模型所有复杂技术打包成一个文件，在任何系统上双击运行；

有一位颜值又高、技术又强的开源高手，早早就把这件事做到了极致；

而你很可能还不知道这个最简单粗暴的本地部署方式

【1】从占领华尔街运动发起者到全职开源开发者 jart：

早年是 Occupy Wall Street（占领华尔街）运动的活跃组织者。那时候她才二十多岁，就已经在搞大型社会运动了。后来她转行做程序员，在 Google Brain 工作过，现在是全职开源开发者。

她的两个最牛项目：

Cosmopolitan Libc：让同一份程序能够在 Windows、macOS、Linux、FreeBSD 等六个主流操作系统上原生运行，真正做到一次编译、到处执行。

llamafile：把 llama.cpp 推理引擎、完整模型权重和跨平台运行时，全部打包进一个 .llamafile 文件。现在由 Mozilla AI 团队接手维护，但核心设计和黑魔法依然来自 jart。

不靠营销出名，而是真正沉下心写代码、动手优化的大牛。博客里她提到为了给 llamafile 写语法高亮器，一口气学了 42 种编程语言的词法……这种极致钻研的精神，真的让人佩服。

【2】顶级的优化手段与黑魔法手搓

jart 在 llamafile 上下了很多功夫，用各种优化手段和黑魔法手搓，把“黑魔法”用到了极致，每一处都是高手手动优化的结果：

任意端跨平台(APE): 这个技术抹平了不同平台的特殊性，在Windows眼里这个文件就是EXE，在Linux眼里是Shell，在macOS眼里是原生二进制

模型权重零拷贝：为了做到启动时做机制优化，打包时自动对权重进行分页，启动后内存直接正确映射，不需要复制拷贝，效率提升特别多

GPU支持也能跨平台？：最狠的一招。Cosmopolitan 是静态链接的，传统 CUDA/Metal 很难搞。她把 ggml-metal.m 和 http://ggml-cuda.cu 也塞进 ZIP，首次运行时自动调用 nvcc 或 Xcode 编译，然后 dlopen 动态加载。整个过程几毫秒完成，之后就和原生一样快。

优化CPU矩阵乘法：提前优化，自动针对CPU优化算法，自动挑选CPU指令集(AVX,AVX2,AVX512)并提前优化好，启动时利用Cosmopolitan Libc来动态切换优化好的matmul，性能自然就上去了。

这些优化全都是手工极致，没有一点偷懒。她写这些就是为了让本地模型用起来“像喝水一样顺滑”。

【3】Ollama VS llmafile 性能对比

在 CPU 场景下，llamafile 对比 Ollama 优势显著，很多情况下性能能达到 2~3 倍，跑起来明显更丝滑流畅。

你只需要一台性能足够好的机器，就能真正爽起来。

微服和算力舱非常合适运行，只需要下载一个Qwen3.5.llamafile 双击运行，就相当于自建中转站了

喜欢开源技术的老板，欢迎在评论区打「1」，我给你们安排专属开源开发者优惠。

---


**作者** Robinson · 鲁棒逊（@python_xxt）  
**貼文連結** https://x.com/python_xxt/status/2041565434617725103  

**正文**

AI行业有一个没人公开说的秘密：

顶级AI研究者的流动方向是这个行业最可靠的领先指标。

这些人掌握着公众无法获取的内部信息—，模型的真实能力边界、下一代架构的可行性、组织的真实健康度。他们的脚投票比任何分析师报告都准。

和OpenAI对比， Anthropic的研发团队几乎没有重大流失。

与此同时，OpenAI的资本效率正在下降，而这是组织衰退的经典信号。

---


**作者** 鸭哥（@grapeot）  
**貼文連結** https://x.com/grapeot/status/2041715916459913651  

**正文**

AMD AI 总监 Stella Laurenzo 用 6,852 个本地 session 反向审计 Claude Code，把中文圈热议的"降智"量化成了带时间戳的证据。最值得带走的判断：今天你跟 AI 模型之间多了一层 runtime，它对你不可见，被厂商每天悄悄调整。https://yage.ai/share/claude-code-runtime-regression-20260407.html?utm_source=twitter&utm_medium=thread&utm_campaign=claude-code-runtime-regression-20260407

---


**作者** 花叔（@AlchainHust）  
**貼文連結** https://x.com/AlchainHust/status/2041711878016020648  

**正文**

小龙虾已经过时，人人都开始讨论Hermes Agent了。但你可能只看到一堆细碎的信息，根本学不动搞不懂这究竟是啥。

所以，我来了，我带着我的橙皮书又来了📙

《Hermes Agent 从入门到精通》，17章，63页，免费PDF。

这本书回答一个核心问题：Hermes和OpenClaw到底有什么区别？

一句话来说：OpenClaw是你养出来的龙虾，Hermes是自己会长大的龙虾。

OpenClaw的Skill需要你手动写、手动调。Hermes内建了一套学习循环，用得越多，Skill越精准，记忆越深。不是你在训练它，是它在训练自己。

如果你读过我之前写的《Harness Engineering》，Hermes就是那本书讲的五个组件的第一次产品化。出厂就带缰绳，缰绳还会自己长大。

GitHub开源，欢迎star和提issue ↓

---


**作者** hoeem（@hooeem）  
**貼文連結** https://x.com/hooeem/status/2041436826406170880  

**正文**

when you become a millionaire in 1-3 years because you sell personalised knowledge bases and it’s all because (I repeat): 

1: you learn how to build llm knowledge bases (the guide drops everything you need)

2: you go to people who are cash rich and time poor. lawyers, doctors, consultants, agency owners, property investors, founders. people drowning in information they never have time to organise

3: you show them what a personalised knowledge base looks like. their research, their documents, their industry intel, all compiled into a searchable wiki that gets smarter every time they use it

4: you offer a one-time build for 1.5k. you set up obsidian, build the folder structure, configure the schema, clip their first 20-30 sources, run the compilation, hand them a working system with a walkthrough

5: you offer a yearly maintenance package for 500. you update their wiki with new sources, run health checks, add new topics as their work evolves, keep the whole thing current

6: you land 5 clients and that’s 7.5k upfront plus 2.5k recurring every year. 10 clients and you’re looking at 15k plus 5k annual. for a system that takes you a few hours to build once you know the workflow

7: again, if you find 200 clients and you’re sitting on 300k upfront and 100k recurring every single year. for building markdown files.

the beauty of this is the work gets faster every time you do it. your second build takes half the time of your first. by your fifth you could knock one out in an afternoon.

and the people who need this most have no idea it exists. their competition definitely doesn’t have one. you’re not selling software. you’re selling an unfair advantage in their specific field.

---


**作者** Annelies Gamble（@AnneliesGamble）  
**貼文連結** https://x.com/AnneliesGamble/status/2041502675229897118  

**正文**

Some of the most important AI opportunities in manufacturing will come from AI-native industrial companies built around the workflow itself. In many cases, these businesses may look less like

---


**作者** Nick Khami（@skeptrune）  
**貼文連結** https://x.com/skeptrune/status/2041638336037842960  

**正文**

apparently real MCP has never been tried, but i still think CLI is better 

---


**作者** Aryan Mahajan（@aryanXmahajan）  
**貼文連結** https://x.com/aryanXmahajan/status/2041565361913655727  

**正文**

We hit the wall with n8n six months ago.
Not because n8n is bad. It's genuinely one of the best automation tools ever built. We use it to connect dozens of systems across multiple clients, and at

---


**作者** Stanley（@Stanleysobest）  
**貼文連結** https://x.com/Stanleysobest/status/2041242582760771915  

**正文**

人是怎么废掉的

1，懒
2，馋
3，拖延
4，爱熬夜
5，自控力差
6，整天精神内耗
7，停止思考不学习
8，假装努力，持续幻想
9，言语上的巨人，行动上的矮子
同样是睡8时，你为什么不选22:00-6:00？而是4:00-12:00?记住：自律的本质，就是亲手杀死另一个颓废的自己。
10，习惯性等待，持续性拖延，凡事能拖就拖，不到最后一刻永远不会行动。
11，浅尝辄止，习惯性放弃，做事情缺乏韧性，没有毅力，一看见困难，一遇到挫折就想要放弃，着急着转移新的方向。
12，宅，和世界脱轨，不社交，不出门，不做饭，一日三餐，全靠外卖。失去了对生活的渴望，逃避思考。
13，随波逐流，就像一台机器，从来不会主动去思考，容易受到身边人的影响，经常被人洗脑，被带节奏。
14，娱乐至上，沉迷于虚幻的愉悦感，每天把大量的时间花在了刷剧，看小说，玩游戏。
15，一味地追求捷径，没有战略耐性，盲目追求短期的回报，不愿意花费精力去做长远的规划。急功近利，看了两天投资理财的书，就想着自己什么时候才能成为股神。
16，习得性无助，遇到事情，经历了一些挫折，尝试无果后，从此便抱有消极的心态，也不愿意再次尝试。认为即使有了机会，事情就这样了，自己的能力无法改变，最终，自我放弃。

---


**作者** Dhravya Shah（@DhravyaShah）  
**貼文連結** https://x.com/DhravyaShah/status/2041583092423434306  

**正文**

Instead of reranking, why not just synthesize the results exactly as the answering model needs?

Introducing Aggregate ranking: Aggregate the answers into only what the model needs. 

Leading to less tokens and better quality, trading off 1s latency!

https://x.com/supermemory/status/2041581381793280378

---


**作者** Dr.Wang（@HotmailfromSH）  
**貼文連結** https://x.com/HotmailfromSH/status/2041473387588108655  

**正文**

太恐怖了！

据说是中国AI agent Manus AI ，全天候运营，怪不得这么多垃圾帐号在评论区。 

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2041543098451259772  

**正文**

好莱坞女星 Milla Jovovich（《第五元素》女主角）和开发者 Ben Sigman 联合发布了一个开源 AI 记忆系统 MemPalace，声称在 LongMemEval 基准测试中拿下满分，是有史以来第一个做到这个成绩的系统。项目完全本地运行，不需要云服务和 API 密钥，免费开源。

【1】它想解决什么问题

每次和 AI 对话结束后，所有上下文都消失了。你花几个小时跟 Claude 或 ChatGPT 解释你的项目架构、技术选型、调试过程，第二天它全忘了。半年下来可能积累了近 2000 万 Token 的对话，但没有一个系统帮你把这些东西管起来。

现有的记忆方案（比如 Mem0、Zep）让 AI 自己决定记什么，提取出“用户喜欢 Postgres”这样的标签，但把你解释为什么选 Postgres 的那段对话丢掉了。MemPalace 的思路相反：全部存下来，靠结构让它可搜索。

【2】怎么做的

借鉴了古希腊“记忆宫殿”（方位记忆法）的概念：把对话按项目和人物分成“翼”（wing），每个翼里按主题分成“房间”（room），房间之间有“走廊”（hall）按记忆类型分类，不同翼的同名房间通过“隧道”（tunnel）互相关联。

同时开发了一种叫 AAAK 的压缩语法，号称能把上下文压缩 30 倍，让 AI 用大约 120 个 Token 就加载几个月的关键信息。支持所有主流模型，包括本地运行的 Llama 和 Mistral。

通过 MCP 协议接入 Claude 等工具后，AI 会自动调用 MemPalace 的 19 个工具来搜索历史对话，用户不需要手动操作。

【3】争议

项目发布当天就遭到多方质疑，其中最系统的一篇来自 Penfield Labs，逐条拆解了 benchmark 数据的问题：
LongMemEval 的“满分”实际上只做了检索这一步，没有生成答案，也没有经过评判。

标准排行榜上的成绩是端到端的问答准确率，MemPalace 测的只是“能不能找到正确的对话片段”，难度低了一个量级。项目自己的文档也承认，最后三道题的修复是针对特定题目写的补丁代码，属于“teaching to the test”。

LoCoMo 基准测试的 100% 更离谱：10 段对话最多 32 个会话，但检索参数设成了 top_k=50，等于把所有内容全部丢给 Sonnet 做阅读理解，检索层完全被绕过了。项目自己的 BENCHMARKS.md 文件里白纸黑字写了这一点。而且 LoCoMo 数据集本身的标准答案就有大约 99 道题是错的，理论上不可能 100%。

“无损压缩”也站不住脚。AAAK 模块把句子截断到 55 个字符，decode 函数不能还原原文。项目自己跑的测试里，用 AAAK 压缩后的检索准确率从 96.6% 掉到了 84.2%，差了 12 个百分点。无损压缩不会导致质量下降。

宣传材料里提到的“矛盾检测”功能，在代码里也找不到实现。知识图谱模块只做了完全匹配的去重，矛盾的事实可以无限累积。

【4】该怎么看

项目内部文档其实还比较靠谱，大部分方法论缺陷在 BENCHMARKS.md 里都有披露。问题在于发布推文把所有限定条件都去掉了，只留下了最炸裂的数字。

抛开 benchmark 争议，MemPalace 的核心想法有可取之处：用结构化的方式组织对话记忆，全部本地运行，不依赖云服务。仅靠宫殿结构分层检索，准确率就提升了 34%，这个数字是实测的。纯本地无 API 的基线成绩 96.6% R@5 也确实是同类系统中最高的。

简单来说：明星光环制造的传播效果远超工程本身的分量。

---


**作者** Sharath Kuruganty（@5harath）  
**貼文連結** https://x.com/5harath/status/2041556399616864561  

**正文**

I joined @composio two weeks ago.
In that time, three things happened. @mercor_ai got breached. Axios got hijacked on npm. And every developer I talked to brought up the same worry: their AI agents

---


**作者** Rohit（@rohit4verse）  
**貼文連結** https://x.com/rohit4verse/status/2041561726517440999  

**正文**

Anthropic's agent harness has a 823-line retry system. 

Your agent has try/catch.

Most agent teams will spend 6 months discovering what's already sitting in Claude Code's source. 

I pulled apart all 331 modules so you don't have to. 

---


**作者** 雪踏乌云（@Pluvio9yte）  
**貼文連結** https://x.com/Pluvio9yte/status/2041571378021986486  

**正文**

Hermes Agent 是 Nous Research 开源的自改进 AI Agent 框架
它最大的特点是内置学习循环：每次完成任务后，它会自动从经验中提炼出可复用的 Skill，存入持久记忆，下次遇到类似任务时会自动改进和调用。

---


**作者** Alex Vacca（@itsalexvacca）  
**貼文連結** https://x.com/itsalexvacca/status/2041547607995228198  

**正文**

Our total addressable market was 15,000 companies. We ran AI qualification scoring and cut it to 8,900 before sending a single email.
For most folks, this would look counterintuitive. Cutting almost

---


**作者** Aman（@Amank1412）  
**貼文連結** https://x.com/Amank1412/status/2041564099503648940  

**正文**

SOMEONE BUILT A MAP OF HUMAN CONNECTIONS USING WIKIDATA.

THIS IS LOWKEY INSANE. 

---


**作者** Jonathan Simcoe（@jdsimcoe）  
**貼文連結** https://x.com/jdsimcoe/status/2041587934059753609  

**正文**

A few years ago, we asked a simple question: What if people could see our banking product before they signed up? Not a polished walkthrough or a gated preview — the real product, as it actually is.

---


**作者** 陈思远Yosef（@YosefBlockchain）  
**貼文連結** https://x.com/YosefBlockchain/status/2041483009694785783  

**正文**

红杉这篇博客直接给AI时代下一个十年的最大赛道盖棺定论了。

20年前Marc Andreessen说软件正在吞噬世界，今天红杉直接定调，服务就是新的软件，而AI Agent正在一口一口，吃掉整个超1万亿美元的服务市场。

这张四象限矩阵图，直接把未来十年的行业重构，拆得明明白白，需要强专业判断的管理咨询，平面设计，高管猎聘，正在变成AI的副驾驶领地，流程标准化的保险经纪，薪资合规，会计审计，房产交易，已经进入了AI自动驾驶的范围，招聘，货运经纪，临床实验。

这些内包服务正在被AI快速渗透，供应链采购，药房后台，财富管理运营，就是下一波被重构的浪潮，我们总觉得AI只是在替代零散的岗位，可顶级风投已经看清了，这不是单个岗位的消失，是整个万亿级服务行业的底层逻辑重构，20年前软件把线下的服务，变成了可复制的SaaS产品，今天AI Agent正在把标准化的软件，变成了能自主执行的智能体，当年软件吞噬世界诞生了多少千亿级公司，今天AI重构服务市场，就会有多少新的传奇诞生。

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2041649498531791236  

**正文**

LLM 是一颗超强大脑，但它是个“缸中之脑”——泡在营养液里，没有眼睛、没有耳朵、没有手脚。你对它喊话它听不见，它想做事也做不了。

Harness 就是给这颗大脑装上的“全套身体”。

眼睛和耳朵：让大脑能接收外界信息——用户说了什么、文件里写了什么、数据库里存了什么。

嘴巴：让大脑的想法能输出给用户看到。

手和脚：让大脑能真正去做事——读文件、改代码、跑命令、调 API。

小脑和反射神经：大脑说了句胡话怎么办？手没抓住东西怎么办？这些容错、重试、纠偏的机制，不需要大脑操心，身体自己处理。

记忆系统：这部分值得展开说。大脑本身有“工作记忆”（上下文窗口），但容量有限，就像人一次只能在脑子里同时想七八件事。Harness 要帮大脑管理三层记忆：第一层是当前对话的短期记忆——这轮对话里已经说了什么、做了什么，哪些该保留、哪些该丢掉，怎么把最关键的信息塞进有限的窗口里。第二层是跨对话的长期记忆——上周你告诉它你的项目用 TypeScript，下周它还记得，不用你重复说。第三层是项目级知识——代码库的结构、团队的规范、常用命令，这些不是“记住”的，而是 Harness 主动去读取和组装的。三层记忆协同工作，让大脑每次被唤醒时都像一个“了解情况的人”，而不是一个每次都要从头介绍背景的陌生人。

一句话总结：大脑负责“想”，Harness 负责“让它能感知、能行动、能记住、能靠谱地完成任务”。

---


**作者** YC (Yucheng)（@yucheng）  
**貼文連結** https://x.com/yucheng/status/2041620504159646015  

**正文**

Lucius 的最近的一个场景是, PM 需要从用户的对话中获得产品下一步的功能计划。Lucius 给到自己的 PM 的建议是：发送前增加一个轻量审核。这个建议从没出现在任何正式的用户反馈表里，它藏在 47 次“帮我改一下再发”的对话记录和反复的“撤回重发”操作中。

一旦组织有了 AI 的介入，PM 拿到的就不再是一个“我觉得可以加个功能”的模糊建议，更不需要去和一个个运营对细节 —— 而是一个基于真实对话、运营上下文和知识支撑的答案。

传统路径是“调研 → 假设 → 验证”，而 AI 路径是“对话 → 模式 → 洞察”。少了两步，速度快了不止 10 倍！

---


**作者** 鸭哥（@grapeot）  
**貼文連結** https://x.com/grapeot/status/2041701825884385710  

**正文**

今天发布的 Mythos 真正值得看的，不是 benchmark 数字，而是那 244 页 system card。最关键的信息不是它有多强，而是：Anthropic 已经不确定，Mythos 考 90 分，到底是因为它只有 90 分的水平，还是卷面只有 90 分，又或者它其实故意隐藏了实力，只考了 90 分？

https://yage.ai/share/mythos-evaluation-crisis-20260408.html?utm_source=twitter&utm_medium=thread&utm_campaign=mythos-evaluation-crisis-20260408

---


**作者** Ankur Goyal（@ankrgyl）  
**貼文連結** https://x.com/ankrgyl/status/2041680981237887180  

**正文**

who is building the vercel ai sdk equivalent across sandbox providers?

---


**作者** Nav Toor（@heynavtoor）  
**貼文連結** https://x.com/heynavtoor/status/2041572825698615583  

**正文**

(Last time I explained why context engineering killed prompt engineering. This time I am giving you the actual system. Copy these. Paste these. Watch the output change immediately.)
My last article on

---


**作者** Shann³（@shannholmberg）  
**貼文連結** https://x.com/shannholmberg/status/2041532958012776572  

**正文**

anthropics growth marketer mapped out 4 levels of AI marketing use

most people sit at level 1, automating what they already do

> level 1: automate what you already do (reporting, copy, data pulls)
> level 2: use AI as a thinking partner where its better than you
> level 3: do work that was below the ROI threshold before
> level 4: build custom tools only you would ever build

level 3 is work that never existed before. stuff nobody did because the manual cost was never worth it

mining negative keywords across every ad group. checking your full site for broken links daily

same logic applies to content, research, QA, competitor monitoring. all work that existed in theory but nobody had the hours for

level 4 is where the ROI compounds

there are hundreds of AI marketing skills and plugins floating around github right now. most of them work in theory but fall apart in practice because they are built for the general case, not your case

your business has specific data, specific workflows, specific edge cases that no generic tool will ever cover. the people building custom tools around their own problems are the ones pulling ahead

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2041585514873037167  

**正文**

Hermes Agent 势头很猛，这几天推荐的人很多，可以关注一下。我自己安装试用了还可以。

Hermes Agent 是由 Nous Research 在今年 2 月底开源的 AI 智能体框架，上线不到两个月，GitHub 星标已经接近三万。这个项目被社区认为是 OpenClaw（龙虾）上线以来，第一个真正意义上的竞争对手。

两者都是自托管的开源智能体，都能接入 Telegram、Discord、Slack、WhatsApp 等聊天平台，都支持多模型切换，都走 MIT 协议。但设计哲学完全不同。

【1】龙虾是网关，Hermes 是引擎

OpenClaw 的核心是一个 Gateway（网关守护进程），负责统一管理会话、路由和渠道连接，像一个调度中心，把你的各种聊天应用连接到 AI agent。你可以理解为它是一个“多渠道个人助理操作系统”。

Hermes Agent 的核心则是 agent 自身的执行循环。它不是围绕“怎么把消息送到 agent”来设计的，而是围绕“agent 怎么变得越来越强”来设计的。官方管这叫 closed learning loop（闭环学习循环）。

【2】会自己写技能的 agent

这是 Hermes 最有意思的地方。当它完成一个复杂任务（通常涉及五次以上工具调用）后，会把整个过程沉淀成一份结构化的技能文档，存成 Markdown 文件。下次遇到类似任务，直接加载这份技能，不用从头解决。

更关键的是，这些技能在使用过程中会自我迭代。如果 agent 在执行技能时发现了更好的方法，它会自动更新技能文档。有 Reddit 用户反馈，agent 在两小时内自动生成了三份技能文档后，重复性研究任务的速度提升了 40%。

OpenClaw 也有技能系统，但主要依赖人工编写和社区贡献的技能市场 ClawHub。Hermes 这边等于把“写技能”这件事也交给了 agent 自己。

【3】记忆体系的差异

两者都声称有跨会话记忆能力，但实现方式不同。

Hermes 用 SQLite 数据库配合全文检索，把所有历史对话存下来，需要时通过搜索加摘要召回。它把记忆分成两层：一层是常驻的关键信息（写在 MEMORY.md 里，每次对话都带上），另一层是全量历史检索（容量无限，按需调用）。

OpenClaw 的记忆则是工作区里的 Markdown 文件，走的是“文件即记忆”的路线，通过语义检索工具来查找。在上下文压缩前会执行一次静默记忆写入，防止压缩丢信息。

简单说，Hermes 更像是给 agent 装了一个搜索引擎式的大脑，OpenClaw 更像是给它一个笔记本。

【4】安全思路也不一样

Hermes 搞了一套五层纵深防御：用户授权、危险命令审批、容器隔离、凭据过滤、上下文注入扫描。默认对高风险操作（比如执行终端命令、写文件）要人工审批，超时未批准就自动拒绝。

OpenClaw 这边则更强调信任模型和配置审计。它提供了 openclaw security audit 命令，可以一键扫描网关配置的安全隐患。但 OpenClaw 在安全方面的历史记录不太好看，今年 2 月被曝出多个高危漏洞，13.5 万个实例暴露在公网上，技能市场也有超过 300 个恶意技能被发现。

【5】要不要换或者选哪一个

如果你日常用的 Agent 已经顺手，没必要。如果你之前的龙虾主要是 claude code 的授权现在用不了可以试试这个，但不能保证继续用多久。如果喜欢折腾想试试不同的选择，也可以试试。

如果你想要一个“多渠道助理平台”，接入各种聊天工具，用社区现成的技能市场，OpenClaw 的生态更成熟，34.6 万星标不是白来的。

如果你更关心 agent 的长期进化能力，想让它用得越久越聪明，或者你是做 AI 研究的，需要生成训练轨迹、跑强化学习实验，Hermes 的架构更对口。它还内建了一个兼容 OpenAI API 的服务端，可以直接作为后端接入 Open WebUI 等第三方界面。

Hermes 跑在 5 美元一个月的 VPS 上就够用，也支持 Docker、SSH 远程、Modal 等 serverless 方案。安装只需要一行 curl 命令。

安装不复杂，参考官方文档即可：https://hermes-agent.nousresearch.com/docs/getting-started/quickstart

爱马仕的英文也是 Hermes。

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2041591839913079227  

**正文**

Tasklet (@taskletai) is the cloud agent OS for knowledge work. It connects to all your tools, uses computers in the cloud, and runs 24/7 to get real work done. 

Started by Firebase founder @startupandrew and @jonnydimond, it’s grown >1,200% this year to $5M ARR and just raised $20M.

Congrats to the team!

https://www.ycombinator.com/launches/PsX-tasklet-the-cloud-agent-os-for-knowledge-work

---


**作者** ashu garg（@ashugarg）  
**貼文連結** https://x.com/ashugarg/status/2041656168435609788  

**正文**

AI is making teams smaller, and more senior by default.

As agents take on more of the execution, the humans on the team will have to sit closer to decisions and carry more context and responsibility than ever before.

My partners @joannezchen and @realleolu outlined four human roles that will define the agentic era in a recent essay:

1. People who own outcomes. The CFO who signs the filing, the CTO who’s accountable when systems fail. Accountability isn’t something you can automate away.

2. People who design the system. The architects of the new human-AI operating model. They decide how humans and agents work together, what runs autonomously, and where control sits.

3. People who build trust. Sales, recruiting, and leadership roles where the core unit of value is human judgment, relationships, and the ability to read a room.

4. People who validate. Domain experts who sit at the boundary between what an AI system can do and what it can be trusted to do. This boundary will keep shifting out as agents become more performant.

Teams will be leaner, but the software opportunity underneath them will be vastly larger.

---


**作者** 鸭哥（@grapeot）  
**貼文連結** https://x.com/grapeot/status/2041607216164389343  

**正文**

Anthropic 刚公布 Project Glasswing。对 AI builder 来说，最值得先澄清的不是“它有多强”，而是三件事：这是不是一个今天就能用的新模型？如果不是，为什么所有人都在谈？以及，这件事要求我们更新什么认知？我写了篇短文，把这件事拆开讲清。

https://yage.ai/share/anthropic-glasswing-ai-builders-20260407.html?utm_source=twitter&utm_medium=thread&utm_campaign=anthropic-glasswing-ai-builders-20260407

---


**作者** Jesse Lau 遁一子（@jesselaunz）  
**貼文連結** https://x.com/jesselaunz/status/2041636659368960148  

**正文**

我靠，这是核武级了

“在 OpenBSD 上，我们发现了一个存在了 27 年的漏洞—— 我只需向任意 OpenBSD 服务器发送几段数据就能让它崩溃。”

“在 Linux 上，我们发现了多个漏洞，作为一个没有任何权限的用户，只需在机器上运行一个二进制文件，就能将自己提升为管理员” 

---


**作者** 鸭哥（@grapeot）  
**貼文連結** https://x.com/grapeot/status/2041606996248735816  

**正文**

过去一年我高强度用AI开发，发现一个反直觉的事：我故意违反了DRY原则（Don't Repeat Yourself）。每次画流程图、做可视化都让AI现写，从不抽象成可复用的库。按传统软件工程这简直离经叛道。但我的效率并没有降低。为什么？

---


**作者** Glean（@glean）  
**貼文連結** https://x.com/glean/status/2041547656426631584  

**正文**

Across the enterprise, a new species has emerged: the AI agent.

At Glean:LIVE, see how to create the habitat they need to thrive –deep enterprise context, strong integrations, built-in guardrails, and a standardized way to build and launch agents.

📅 May 12th · 10 AM PT 
🔗 Register: https://glean-it.com/4smtYyy

---


**作者** Ashpreet Bedi（@ashpreetbedi）  
**貼文連結** https://x.com/ashpreetbedi/status/2041568919085854847  

**正文**

In the early 1940s, Bell Labs was building the national telephone network, the most complex technical system in the world at the time. Millions of switches, cables, relays, and operators had to work

---


**作者** Art Levy（@artlevy）  
**貼文連結** https://x.com/artlevy/status/2041584508714262852  

**正文**

Harvey: ~$1B raised across 4 rounds in 14 months.

Legora: ~$800M across 3 rounds in 10 months.

Combined $1.7B+ into two legal AI companies.

History doesn't repeat, it rhymes. 

This is the Capital Wars playbook we've seen before 🧵 

---


**作者** Men's Aesthetic（@AestheticsMens）  
**貼文連結** https://x.com/AestheticsMens/status/2041450491109105861  

**正文**

Men's Complete Health Bible :

40 things every man should know about his health before 35.
Most men learn these too late: 

---


**作者** Han Zheng（@hanzheng_7）  
**貼文連結** https://x.com/hanzheng_7/status/2041291008378343707  

**正文**

🚀The era of autonomous multi-agent discovery is arriving! @karpathy 

🪸Excited to share CORAL, our new work on autonomous multi-agent systems for open-ended scientific discovery.

🙅‍♂️A key limitation of many current “self-evolving” frameworks is that agents still operate inside tightly constrained loops — they mutate solutions, but they do not truly decide how to explore.

In CORAL, we push toward genuine autonomy:
Agents decide
🔍 what to explore
🧠 what knowledge to store
♻️ which ideas to reuse
🧪 when to test hypotheses

🔥One of the most interesting findings:
A single autonomous agent already outperforms fixed evolutionary search, but the biggest gains emerge when multiple agents form a research community. 

💪Over 50% of breakthroughs in multi-agent runs come from building on other agents’ discoveries. This suggests that knowledge reuse and collaboration are central to scalable automated discovery.

🏅Across 10+ difficult tasks in algorithmic discovery and system optimization, CORAL achieves state-of-the-art performance while improving efficiency by 3–10×.
 
📄 Paper: https://arxiv.org/abs/2604.01658v1
💻 Code: https://github.com/Human-Agent-Society/CORAL
💡AlphaXiv: https://alphaxiv.org/abs/2604.01658

#agentic #llms #selfevolvingagent #multiagent #autoresearch #alphaevolve

---


**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2041451173673353669  

**正文**

🧵Thread: 龙虾安全，没有银弹

1/🧭 龙虾最大的漏洞，架构级无解

大模型把system prompt和用户数据拼成一个string，天生分不清指令和数据。

黑客的输入可以直接变成系统代码——这不是bug，是Transformer的底层缺陷。👇 

---


**作者** Ray Wang（@wangray）  
**貼文連結** https://x.com/wangray/status/2041384982485315737  

**正文**

本来想自己搭一套 Karpathy 的 LLM-Wiki 做知识库管理

Hermes 现在直接开箱即用，省事儿了

---


**作者** Xiao Tan（@tvytlx）  
**貼文連結** https://x.com/tvytlx/status/2041455988797227239  

**正文**

如果你关注 AI agent 这个方向，最近大概率刷到过 Hermes Agent 这个名字。
GitHub 上 27000 多个 star，Nous Research 出品，MIT 开源。跟 OpenClaw 的 24 万 star 比起来确实小众，但增长速度很快，三月份一度冲到

---


**作者** Will Manidis（@WillManidis）  
**貼文連結** https://x.com/WillManidis/status/2041262402889457721  

**正文**

OpenAI published a policy brief today. 
A thirteen-page document entitled "Industrial Policy for the Intelligence Age." It is, by all accounts, a deeply considered work of policy thinking that is

---


**作者** fabian（@fabianstelzer）  
**貼文連結** https://x.com/fabianstelzer/status/2041247699333255542  

**正文**

Palantir, but for organizing children’s birthday parties

who’s building this? 

---


**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2041327832681554358  

**正文**

Google 工程师的 Agent Skills技能包

Google Chrome 团队工程负责人 Addy Osmani 开源了一套叫 Agent Skills 的技能包

这些技能都来自 Google 内部的工程实践，19 个结构化技能，覆盖从想法到上线的完整开发流程。

安装之后，Agent 不再是"能写代码"，而是"按高级工程师的标准写代码"。

MIT 协议，纯 Markdown 格式，适配 Claude Code、Cursor、Windsurf、GitHub Copilot 等几乎所有主流编程 Agent。

整套技能围绕软件开发的六个阶段组织，每个阶段对应一个斜杠命令：

DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP
/spec    /plan   /build   /test    /review   /ship

加上一个 /code-simplify 做代码简化，一共七个命令。你不用记 19 个技能各叫什么，敲命令就行，对应的技能会自动激活。

---


**作者** 蓝点网（@landiantech）  
**貼文連結** https://x.com/landiantech/status/2041447670783623522  

**正文**

今天HN上一个热门讨论：来自Claude Code Issue中的报告，报告称Claude Code从2月开始就无法执行复杂工程任务，也就是质量显著下降。

提交Issue的似乎是非常专业的团队，提交了极其详细的数据：https://github.com/anthropics/claude-code/issues/42796 

---


**作者** Kevin Ma（@kevinma_dev_zh）  
**貼文連結** https://x.com/kevinma_dev_zh/status/2041358398827200566  

**正文**

我不用专门去研究 harness，因为我一直在实践。2024 年底开始我就不手写代码了，是在 Cursor 火起来之后。

看了一圈，harness 其实是把已有的东西重新包装，整理成了一个新概念。如果你和我一样一直在用 AI 写代码，我相信你对这些东西已经挺熟了。没必要因为冒出一个新概念就焦虑。

如果你在 AI 编程方面经验还不多，那确实值得去了解一下。推荐这个仓库，整理得不错，可以看看。

https://github.com/deusyu/harness-engineering

---


**作者** 阿绎 AYi（@AYi_AInotes）  
**貼文連結** https://x.com/AYi_AInotes/status/2041458487679726027  

**正文**

一定要用最好的 AI 大模型 Claude opus4.6，一定要多看 Claude 官方文档，吸收最顶级的信息源！

 Anthropic官方这份AI Agent 开发实战指南真的很顶，一句话点透生产环境里最能打的 Agent 的核心构建原则。

《Building Effective AI Agents》指南，核心表达是做AI智能体，别搞复杂框架，简单、可组合的模式才是生产环境里最能打的。

原链接和完整干货拆解👇
#AI智能体 #LLM #Anthropic

---


**作者** TechFlow 深潮｜APP 已上线（@TechFlowPost）  
**貼文連結** https://x.com/TechFlowPost/status/2041408368603271254  

**正文**

继上周 Claude 设计负责人分享自己的 Claude 工作流后，OpenAI 团队也发声了

OpenAI Codex 产品负责人 Alex 和开发者体验负责人 Romain 于昨日接受 Peter Yang 采访，展示了如何使用 Codex 处理日常工作：

· Codex 主模型：轻松驾驭百万行代码的复杂任务
· Codex Spark：速度近乎疯狂
· Plan 模式：高效头脑风暴伙伴

大厂的竞争往往就是这样朴实无华，却又格外迷人😈

---


**作者** Dhravya Shah（@DhravyaShah）  
**貼文連結** https://x.com/DhravyaShah/status/2041397346056159665  

**正文**

i have no words, it's all a joke at this point✌️

---


**作者** am.will（@LLMJunky）  
**貼文連結** https://x.com/LLMJunky/status/2041377497447649609  

**正文**

Milla Jovovich has a Github 😏

She's co-developed the highest-scoring AI memory system ever benchmarked with @bensig 

Totally free and OSS.

What a boss. 

---


**作者** Michel Lieben（@MichLieben）  
**貼文連結** https://x.com/MichLieben/status/2041172240956600636  

**正文**

I spent 300+ hours testing Cursor, Claude Code, Lovable, and Codex for lead gen. Tried building workflows in all of them. Broke things constantly. Rebuilt from scratch more times than I can count.
The

---


**作者** Nick Spisak（@NickSpisak_）  
**貼文連結** https://x.com/NickSpisak_/status/2041243686265090076  

**正文**

"Part 1 showed you the folders. Part 2 gives you the system."
 
Part 1 showed you the three folders. 12K people bookmarked the article. The first version created one knowledge base, dumped everything

---


**作者** Muratcan Koylan（@koylanai）  
**貼文連結** https://x.com/koylanai/status/2041245868876009588  

**正文**

WE DON'T HATE CLAUDE CODE ENOUGH

WHY ARE WE PAYING THOUSANDS OF DOLLARS IF YOUR EVERY RELEASE IS MAKING THE HARNESS LESS USABLE? 

---


**作者** Sreeram Kannan（@sreeramkannan）  
**貼文連結** https://x.com/sreeramkannan/status/2041228848176795806  

**正文**

Agentic Companies: The New Trillion Dollar Asset Class

AI converts execution into software. Crypto converts ownership and governance into software.

Creating a new kind of firm.
One that is pure software.
For the very first time.

Lowering the cost basis
Accelerating open innovation
Accessing global capital

Creating a new
Trillion Dollar
Digital Asset class

My talk from @blockworksDAS NYC on why this becomes a trillion-dollar asset class:

---


**作者** 出海去孵化器（@chuhaiqu）  
**貼文連結** https://x.com/chuhaiqu/status/2041398272556954011  

**正文**

Jenni AI 月营收（MRR）突破 100 万美元，24 年 从 David 提过当时团队规模 10 人左右，目前其他平台查看估计在 20 多人？

没有融资，营收数据吊打很多明星融资团队 

---


**作者** Nyk 🌱（@nyk_builderz）  
**貼文連結** https://x.com/nyk_builderz/status/2041162902925930816  

**正文**

RAG was an engineering workaround for small context windows. You could not fit the whole document, so you chunked it, embedded it, searched it, and injected the relevant pieces. It worked. It was also

---


**作者** Ao Qu（@ao_qu18465）  
**貼文連結** https://x.com/ao_qu18465/status/2041233318373388459  

**正文**

🚀 The era of autonomous multi-agent discovery has begun.

Most “self-evolving” scientific discovery frameworks are still tightly constrained:
LLMs often just perform one-step mutations inside fixed evolutionary search loops.

But that is not real autonomy.
Agents still cannot truly decide:
🔍 what to explore
🧠 what knowledge to store
♻️ which past attempts to reuse
🧪 when to test

With CORAL, we ask:

❓ What happens if we give agents much more autonomy to explore the scientific frontier?

💡 Our answer:

A single autonomous agent already outperforms fixed evolutionary search.

But the bigger leap comes when multiple autonomous agents form a research community:

🤝 They explore different directions
🧠 accumulate reusable knowledge and skills
💬 communicate with each other
🌍 and push the frontier together

We introduce CORAL, the first framework for autonomous multi-agent evolution for open-ended discovery.

🥇 Across 10+ tasks in algorithmic discovery, system optimization, and kernel engineering from Frontier-CS, ADRS, AlphaEvolve, etc, CORAL achieves SOTA and improves search efficiency by 3–10× over prior fixed evolutionary-search frameworks.

🔬 Why does autonomy help?

Our analysis shows two main reasons:

🧪 Local verification: agents run local tests before expensive evaluations, which is especially powerful for coding tasks.

♻️ Knowledge reuse: on knowledge-intensive tasks like polyominoes and kernel engineering, agents create and reuse knowledge artifacts at far higher rates than on simple tuning/search tasks like circle packing.

✨ Even more exciting:
Over 50% of multi-agent breakthroughs come from building on other agents’ discoveries.
Multi-agent exploration is also far more diverse than single-agent search.

We believe CORAL opens up an exciting new space for automated discovery systems.

📬 If you are interested in collaborating, let’s talk.

📄 Paper: https://arxiv.org/abs/2604.01658v1
💻 Code: https://github.com/Human-Agent-Society/CORAL
💡AlphaXiv: https://www.alphaxiv.org/abs/2604.01658

#agentic #llms #selfevolvingagent #multiagent #autoresearch #alphaevolve

---


**作者** Tomaz L（@TomazOT）  
**貼文連結** https://x.com/TomazOT/status/2041182964235600023  

**正文**

Prediction markets like @Polymarket and @Kalshi have a fake news problem. Markets run on clarity. But narratives move faster than facts.
@umanitek AI agents use @origin_trail to build context graphs

---


**作者** serafim（@serafimcloud）  
**貼文連結** https://x.com/serafimcloud/status/2041357225483210976  

**正文**

http://2027.dev

If you’re building dev tools - set up it today

---


**作者** Yann（@yanndine）  
**貼文連結** https://x.com/yanndine/status/2041212243455389971  

**正文**

I put the entire Claude GTM Agency Playbook into ONE Notion doc.

10 modules. No fluff.

- What Claude Code does for GTM agencies, how to start, and the core use cases including the Shoptalk cookie editor method
- How to onboard clients end to end in 6 steps from a single Slack trigger to live campaigns
- How to build sending infrastructure in 5 minutes instead of 40 and what breaks it
- How to build campaigns automatically: offer bible, generation flow, feedback loop, and reporting
- Which channel to use and when: the 10x reply rate gap between LinkedIn and email and the allbound model
- Two signal-based plays to build now: event outreach plus social listening, and competitor displacement
- How to run the webinar play for outbound-led inbound on LinkedIn without burning deliverability
- What Clay's pricing change means for agencies and the 4 moves to make now
- How to set up OpenClaw for autonomous prospecting without breaking compliance
- The 3 advantages of the AI-native agency, the copy risk, and what the GTM engineer role is becoming

This is the playbook I would have KILLED for before spending months figuring out how to run a GTM agency on Claude Code without rebuilding everything from scratch every time a client onboards.

Like + comment "CLAUDE" and I'll send it over

(must be connected for priority access)

---


**作者** DROID（@droidbuilds）  
**貼文連結** https://x.com/droidbuilds/status/2041354010024931734  

**正文**

How did Facebook deploy without Vercel?

Back in 2004, there was no Vercel, no AWS, no “Deploy” button.

Here’s how it actually worked:

> Wrote code in PHP (LAMP stack)
> Ran it on a local machine first
> Manually pushed code to a server (FTP/SSH)
> Hosted on a single rented physical server
> Configured Apache + MySQL by hand
> Restarted services manually after changes

As traffic grew:

- Added more physical servers
- Introduced load balancers
- Split DB + app servers
- Built internal tools for deployment

- No CI/CD
- No auto scaling
- No rollback safety
- Just raw engineering + trial & error

Today we complain if deploy takes 30 seconds

---


**作者** Essam Sleiman（@essamsleiman）  
**貼文連結** https://x.com/essamsleiman/status/2041224799746428944  

**正文**

We built [meta-agent](<https://github.com/canvas-org/meta-agent>): an open-source library that automatically and continuously improves agent harnesses from production traces.

Point it at an existing agent, a stream of unlabeled production traces, and a small labeled holdout set. 

1. An LLM judge scores unlabeled production traces as they stream.
1. A proposer reads failed traces and writes one targeted harness update at a time, such as changes to prompts, hooks, tools, or subagents.
1. The update is kept only if it improves holdout accuracy.

On [tau-bench](<https://github.com/sierra-research/tau-bench>) v3 airline, meta-agent improved holdout accuracy from 67% to 87%.

We open-sourced meta-agent. It currently supports [Claude Agent SDK](<https://platform.claude.com/docs/en/agent-sdk/overview>), with more frameworks coming soon. Try it here: \[[GitHub repo](<https://github.com/canvas-org/meta-agent>)\]

![Article Image](<https://pbs.twimg.com/media/HFOIz7naQAAlt6A.jpg>)

## Why

Recent work shows that optimizing the harness layer can materially improve agent performance. 

On TerminalBench-2, vanilla Claude Code with Claude Haiku 4.5 scores 27.5%. The best hand-engineered harness on the same model reaches 35.5%, with no fine-tuning ([Meta-Harness, Lee et al. 2026](<https://arxiv.org/abs/2603.28052>)).

Recent systems have also shown that harnesses can be improved automatically through iterative search ([Autoresearch, Karpathy 2026](<https://github.com/karpathy/autoresearch>);[ Meta-Harness, Lee et al. 2026](<https://arxiv.org/abs/2603.28052>)). 

But those methods usually depend on strong evaluation signals during search, such as labels, tests, or deterministic checks. Agents typically run on messy customer workflows where labeled reward is sparse or unavailable.

meta-agent is built for exactly that production setting: it reads traces from the running agent, uses an LLM judge to score them, and proposes harness updates from the failure patterns it finds. 

## How it works

You provide an existing agent, a stream of unlabeled production traces, and a small labeled holdout set.

1. Read. Collect traces from the running agent.
1. Judge. Score those traces with an LLM judge.
1. Propose. Read failed traces, identify a recurring failure pattern, and write one targeted harness update.
1. Validate. Evaluate the new harness on the holdout set and keep it only if holdout accuracy improves.
1. Repeat. Continue the loop with the updated harness.

Filesystem memory. meta-agent stores each harness candidate, its scores, and its traces on disk. This gives the proposer persistent memory across iterations. Before proposing a change, it can search prior candidates, per-task traces, and scores to see what failed, what has already been tried, and which changes actually improved performance.

## What the optimizer can change

The optimizer can modify the parts of the harness that most directly shape agent behavior: 

- the system prompt
- lifecycle hooks for tool use 
- stop conditions and error handling 
- custom tools, permission logic, and subagents 
- other control logic around the model

It makes one targeted change at a time and prefers the smallest effective fix. 

## Results

Tau-bench v3 is a benchmark for conversational customer service agents. We evaluate on the airline domain (50 tasks), where the agent must follow policy and resolve customer requests.

![Article Image](<https://pbs.twimg.com/media/HFPS2o8boAAKwRU.jpg>)

Setup: We split the 50 airline tasks into 35 for search and 15 for holdout. The agent used Haiku 4.5, the proposer used Opus 4.6, and holdout was always graded with the official tau evaluator.

Starting from a 67% baseline, the judge-based search run reached 87% holdout accuracy. In our current setup, this was higher than the 80% reached by our labeled-search variant.

![Article Image](<https://pbs.twimg.com/media/HFPDd3LbUAAXQhU.png>)

For LLM-judge search, we replaced gold labels on the search split with an LLM judge that reads each trace and produces a short critique of the agent’s failure. The proposer sees natural-language error descriptions, such as “the agent refunded without checking the cancellation policy.” This may provide a richer optimization signal than binary supervision alone, and could help explain why the judge-based run potentially outperformed our labeled-search variant in this setup.

Note: These are single-run results on a small benchmark split. We plan to expand the evaluation with multiple runs and variance estimates in future work.

## Harness Evolution

The harness did not improve in one shot. The proposer iterated through multiple attempts, learning from failure traces at each step. The table below shows the progression for our best-performing run (Critique, 87% holdout).

![Article Image](<https://pbs.twimg.com/media/HFPUrd4aIAAtxJR.png>)

Starting from a vanilla harness, the proposer first added a stop condition to keep the agent from quitting early, but this reduced holdout because the agent stayed engaged while hallucinating answers. It then rewrote the system prompt with tool-use rules, which encouraged tool use but added too much prompt overhead. 

The key improvement came when the proposer moved business rules into a skill, raising holdout to 80%. In the final step, it corrected factual errors in that skill, reaching 87%.

The full improvement came from just three harness components: a stop condition, a rewritten system prompt, and a skill containing domain rules.

## What we learned

Judge-based search is viable on unlabeled traces. We use an LLM judge to score unlabeled search traces during optimization, while keeping a small labeled holdout set to decide whether to keep an update. In our current setup, this reached 87% holdout accuracy, compared with 80% for our labeled-search variant.

Persistent trace memory helps. Giving the proposer access to prior harnesses, traces, and scores helped it avoid repeating failed changes and even catch errors in its own earlier policy rules.

Proposer tends to overfit. Early iterations often fixed the specific traces the proposer saw rather than writing general behavioral rules, which improved search accuracy while hurting holdout. We reduced this by adding a simple instruction:

> "State your change as a rule about agent behavior. If you can only justify it by pointing to specific traces, it's too narrow." 

The proposer prompt matters. Small changes to the proposer’s instructions had a large effect on optimization quality. 

## Try it today

Download [meta-agent](<https://github.com/canvas-org/meta-agent>) and get started today.

Point it at your agent, a task set, and a labeled holdout split. In our experiments, the optimizer found its best harness within 4-10 iterations. You get a ranked set of harnesses with per-task traces explaining what changed and why. Let us know what you think!

## What's next

- More frameworks. meta-agent currently supports Claude Agent SDK. We plan to add support for Codex SDK, OpenCode SDK, and other agent frameworks.
- Better proposer optimization. The proposer has strong leverage on final harness quality. We want to explore a meta-loop that improves the proposer’s own instructions over time, including better failure abstraction and clustering.
- More benchmarks. We plan to evaluate on broader agent benchmarks, including SWE-bench, TerminalBench-2, and domain-specific customer service tasks.

---


**作者** jia（@jia_seed）  
**貼文連結** https://x.com/jia_seed/status/2041268525088842161  

**正文**

you might be reading this and be like nooO not another b2b saas article argh. i was a 19 year old with no funding or network but i ended up closing 10k mrr and wish i had this then

i was a computer engineering student in university and really didn't know anything about talking to or getting customers. also i had never pitched to a vc or angel 

however. i was in sf staying in motels and had zero investment so i had to get traction quick. i was building a pretty silly devtool for hackathons and it seemed pretty hopeless as to how to even sell it. however...

## where do you even start from absolutely zero

i started with cold dming people on every platform and emphasizing that it would be useful specifically  for them. not a copy paste, i did actual research. did they just raise? congrats, here's why this helps your new eng team. launching something new? here's how this fits in.

in my head, it really was a numbers game, where i simply had to hit the limits of every platform

so i made a list. just a spreadsheet. company name, founder name, what they're building, any recent news. then i went platform by platform: twitter, linkedin, discord servers, slack communities, reddit threads.

![Article Image](<https://pbs.twimg.com/media/HFQIhQEa4AAmQYe.png>)

## what kind of people would actually buy your thing for the price you were charging 

to get to 10k, this sounds obvious but most people skip it entirely. before you send a single dm, you need to know exactly who has both the pain and the budget.

for me it was:

- devtools leads at startups that just raised a seed or series a (they suddenly have money and hiring problems)
- hackathon organizers at big tech companies (they had budget and ran events regularly)
- engineering managers at companies actively scaling their eng team

the pattern: people who are in motion. just raised, just hired, just launched. they're already spending money, they're already making decisions. you're not convincing them to buy, you're just showing up at the right time.

the wrong customer is someone who likes your product but has to fight internally to get $50 approved. that will drain you.

once you know exactly who they are, cold outreach stops feeling random. ur not spamming, ur pattern matching

## what do you even write in the message

biggest thing is to keep the message short. it's fine if you're young, you can be unserious. no one really wants to read a paragraph. in fact i kept my messages one single sentence simply saying what the thing i was doing was:

"do you want to host a hackathon"

"do you want to get more developers on your platform"

so now i really wish there was a tool that was able to find me 100 people and draft personalized messages for each one based on the metadata of that person. even better if it created agent inboxes with agentmail so you could do all of it already warmed up and fast

![Article Image](<https://pbs.twimg.com/media/HFQKjHmbcAAlmpc.png>)

luckily! my friend (and now co-founder) mohammad built a tool to make all of that easier. we made it free to use and also open source! 

so yeah i genuinely hope this helps anyone in this position in any way. hope you enjoyed!!

---


**作者** Dr. Alex Wissner-Gross（@alexwg）  
**貼文連結** https://x.com/alexwg/status/2041267641990725933  

**正文**

The Singularity has been collapsing the cost of making things, but not the cost of managing things, until now.

In 1937, Ronald Coase [asked](<https://en.wikipedia.org/wiki/The_Nature_of_the_Firm>) why firms exist at all. His Nobel-winning answer was coordination costs. When it is cheaper to coordinate activity inside a hierarchy than across a market, firms grow. When those costs fall, firms shrink. The history of the firm is the history of this boundary moving.

Every technology that reshaped coordination costs has moved this boundary, but not always in the same direction. The steam engine, the telegraph, and the railroad made hierarchies newly viable at continental scale and produced the factory, the transcontinental corporation, and the modern conglomerate. The boundary grew. Then the personal computer and the internet made markets newly viable at small scale, enabling outsourcing, offshoring, and the gig economy. The boundary shrank. For two hundred years the firm has expanded and contracted around whichever coordination technology is ascendant.

AI is the first technology powerful enough to collapse coordination costs all the way to a single person. With agents that can plan, write, code, research, design, and execute 24/7, the cost of running an entire business falls toward the cost of one person's attention. This is the structural shift the technological unemployment debate keeps missing. AI does not just change what work gets done. It changes the minimum viable size of the organization that does it. When coordination becomes nearly free, you do not need a new job. You need a fleet.

Today, [Henry Intelligent Machines PBC](<https://meethenry.ai/>) ("HIM"), a company I helped form and advise, with backing from [021T Capital](<https://www.021t.vc/>), is announcing the first AI agent layer that assembles, operates, and scales fleets of microbusinesses on behalf of individual owners. Not one business. A fleet, diversified, automated, and compounding. The owner sets direction. The agents do the work. The [World Economic Forum projects](<https://www.weforum.org/press/2025/01/future-of-jobs-report-2025-78-million-new-job-opportunities-by-2030-but-urgent-upskilling-needed-to-prepare-workforces/>) 92 million jobs will be displaced by 2030. HIM is a Public Benefit Corporation whose mission is to mitigate that displacement by creating AI-supervising entrepreneurs at scale.

HIM's Founder and CEO is [Alex Finn](<https://x.com/AlexFinn>), who has already been living this thesis in public. Finn built [Creator Buddy](<https://www.alexfinn.ai/>), an AI-assisted app that did [$100,000 in sales within 15 minutes of launch](<https://grokipedia.com/page/Alex_Finn>), then became [the most prominent power user of OpenClaw](<https://metatrends.substack.com/p/clawpilled-meet-your-ai-chief-of>), the open-source agent framework, running a five-agent organization from his desk that builds software, researches markets, and ships products 24/7. His lead agent is named Henry and runs on Anthropic's Claude Opus 4.6. When a competitor announced a major new feature after weeks of development, Finn dropped the blog post to Henry. Five minutes later, Henry had rebuilt it. The company is named after the agent that proved the model works.

Here is what a Henry-managed fleet looks like. On the publishing side, agents launch newsletters, produce research briefs for professionals who cannot afford a consulting firm, and generate long-form guides that drive search traffic and ad revenue across agent-built sites. On the services side, they run white-label email marketing for local businesses and build apps, landing pages, and websites at near-zero marginal cost. On the physical side, they design products for networked 3D printers, drop-ship on demand with no inventory, and sell branded merchandise and collectibles. For tasks that still require human hands, they coordinate gig workers. The portfolio is the product. And none of it is AI slop. The owner never leaves the loop: the agents handle execution, the human supplies the direction and the taste.

Elon Musk has [popularized](<https://www.foxbusiness.com/economy/musk-predicts-ai-create-universal-high-income-make-saving-money-unnecessary>) the idea of Universal High Income, a world where AI-driven abundance lets everyone live well. But Musk's UHI arrives from the top down. HIM works from the bottom up, putting productive AI assets directly into individual hands. UHI is the north star. A fleet of your own machines is how you start walking toward it.

As Peter Diamandis and I argued in [Solve Everything](<https://solveeverything.org/>), the Intelligence Revolution turns every scarce domain it touches into an abundant one. Coordination has been scarce for as long as organizations have existed. It is why firms exist and why one person has never run a conglomerate alone. Finn proved it is possible. HIM makes it available to everyone.

The waiting list for Henry is now open at [MeetHenry.ai](<https://meethenry.ai/>).

(Disclosure: I have a financial interest in [HIM](<https://meethenry.ai/>). This post is for informational purposes only and is not investment, financial, tax, legal, or business advice. Nothing herein guarantees earnings or business success; operating an AI-assisted microbusiness, like any business, involves risk of loss, and results depend on individual effort, market conditions, and many other factors. Forward-looking statements about capabilities are subject to uncertainty. Users of HIM are solely responsible for their own legal, tax, and regulatory compliance.)

---


**作者** kAI（@_kaichen）  
**貼文連結** https://x.com/_kaichen/status/2041199915280507123  

**正文**

最近翻了两个开源 Agent 框架的源码——Hermes Agent 和 OpenClaw。发现一件有意思的事：它们花了大量工程精力，专门修 GPT-5 在 agentic 场景下的行为缺陷。

不是模型能力不够，是模型"不听话"。

## 问题出在哪

GPT-5 做单轮对话很强。但一旦进入 Agent 循环——需要连续调用工具、自主决策、持续推进任务——它就暴露出四个顽固的坏毛病：

1. 光说不做（Commentary-Only Turns）

你让它改个文件，它回复"我会先读取文件内容，然后定位问题，接着修改……"。说完就结束了。没有任何 tool call。

这不是偶发。GPT 系列模型有很强的"先描述计划再行动"的倾向。在聊天场景里这是好习惯，在 Agent 场景里这是致命的——每一轮空转都浪费上下文窗口和时间。

2. 半途而废（Premature Completion）

工具返回了部分结果，模型就把它当成完整答案交付了。比如搜索只返回了 3 条结果，明明可以换个关键词再搜一轮，它却直接总结"根据以上结果……"。

3. 不做验证（No Verification）

生成了代码不跑测试，写了配置不检查语法，给了答案不交叉验证。直接输出，交付，下一个。

4. 编造而非查询（Hallucination Over Lookup）

手边明明有 search\_files、web\_search 这些工具，遇到不确定的信息却选择"凭印象编一个"。这在长任务里尤其危险——一个错误的文件路径或 API 参数，后面全部白做。

这四个问题不是 GPT-5 独有的，但 GPT 系列表现最突出。Hermes 的代码注释里写得很直白：Claude 不需要这套矫正（"Claude's instruction-following is strong by default"）。

## OpenClaw 的做法：三段 Prompt，简洁有效

https://github.com/openclaw/openclaw/blob/e7fe087677a659004d805c8ccd947db4ebfc0fed/extensions/openai/index.test.ts

OpenClaw 的修复方案藏在一个 90 行的 TypeScript 文件里（extensions/openai/prompt-overlay.ts）。核心是三段 prompt overlay，只对 GPT-5 模型生效。

执行偏好层（Execution Bias）——解决"说了不做"：

> Start the real work in the same turn when the next step is clear.

翻译成人话：别废话，直接干。

它还加了一条针对性极强的规则：如果用户最后一条消息是"ok do it"或"go ahead"，跳过所有复述，直接开始 tool call。

输出契约层（Output Contract）——解决啰嗦和格式问题：

强制精简输出，禁用 em dash（GPT-5 特别爱用破折号），默认简短回答。

人格层（Friendly Prompt Overlay）——把执行纪律包装成"好队友"风格：

这一层很聪明。它不是单纯的性格设定，而是把执行规则嵌进了交互风格里。"Commentary-only turns are incomplete when the next action is clear"——这句话既是性格描述，也是行为约束。

整套方案大约 1,500 tokens。小、准、狠。

## Hermes 的做法：系统工程级的行为控制

https://github.com/NousResearch/hermes-agent/blob/6f1cb46df9825e693e33069626444b9a1bd0d344/agent/prompt\_builder.py#L196

Hermes 走了一条完全不同的路。它承认受 OpenClaw 启发（代码注释提到了 "OpenClaw PR #38953"），但把问题升级成了一套完整的行为工程体系。

XML 标签强化指令权重

Hermes 发现纯文本指令对 GPT 的约束力不够，于是用 XML 标签包裹关键规则：

<tool\_persistence>
Do not stop early when another tool call would materially improve the result.
If a tool returns empty or partial results, retry with a different query
or strategy before giving up.
</tool\_persistence>

XML 标签不是装饰。在 transformer 的注意力机制里，结构化标记比平铺直叙的文本更容易被模型"注意到"。这是一个实践中被反复验证的 prompting 技巧。

四维验证清单

OpenClaw 的验证是一句话："verify correctness, coverage, formatting, and obvious side effects"。Hermes 把它展开成四个维度：

- Correctness：输出是否满足所有需求？
- Grounding：事实性声明是否有工具输出支撑？
- Formatting：输出格式是否匹配要求？
- Safety：下一步有没有副作用（写文件、执行命令、调 API）？需要确认范围。

多出的 Grounding 和 Safety 两个维度，直接对应"编造"和"不验证"两个坏毛病。

反幻觉优先级链

遇到缺失信息时，Hermes 规定了明确的行动优先级：

工具查询 → 带标签地假设 → 向用户提问

"Ask a clarifying question only when the information cannot be retrieved by tools." 先自己查，查不到再问人。这比 OpenClaw 的隐含规则（"Do prerequisite lookup or discovery before dependent actions"）更具操作性。

Developer Role 切换

这是一个 API 层面的 trick。OpenAI 的 API 里，developer role 比 system role 的指令权重更高。Hermes 在调 GPT-5/Codex 时，自动把 system prompt 切换成 developer role。不改内容，只改信封，指令遵循率就上去了。

9 层系统提示词架构

Hermes 最核心的设计是条件式组装的 9 层 system prompt：

层内容关键设计1人格（SOUL.md）与执行规则解耦2工具感知指导只注入已有工具的规则3云服务能力声明—4执行纪律 + 模型补丁核心修复层5自定义 system message运行时覆盖6持久记忆快照会话开始时冻结7Skills 索引每次回复前扫描8项目上下文文件带注入扫描9时间戳与元数据—

第 2 层的设计值得注意：如果当前会话没有 web\_search 工具，所有提到 web\_search 的引导文本都会被自动剥离。这防止模型幻想调用一个不存在的工具——又是一个反幻觉措施。

## 一个更深的观察

这件事真正有意思的地方不在技术细节，而在它揭示的行业现实：

模型厂商卖的是"通用智能"，但 Agent 框架在生产环境里做的第一件事，是用 prompt 给模型打行为补丁。

GPT-5.4 的 benchmark 分数很高。它能写论文、能做数学推理、能处理复杂指令。但在 Agent 循环里连续跑 50 轮 tool call？它会走神，会偷懒，会编造，会虎头蛇尾。

这不是模型"笨"。这是模型的训练目标（单轮对话质量）和 Agent 场景的要求（多轮执行纪律）之间存在 gap。RLHF 优化的是"回答让人满意"，不是"持续正确地调用工具直到任务完成"。

Hermes 和 OpenClaw 正在用 prompt engineering 填这个 gap。但 prompt 终究是创可贴，不是手术。真正的解决方案应该在训练阶段就把 agentic behavior 作为优化目标。

Hermes 的代码里其实已经有了这个方向的伏笔——trajectory\_compressor.py 文件专门为 RL 训练压缩 Agent 轨迹数据，强化"理解 → 执行 → 验证"的行为模式。Prompt 补丁是现在的权宜之计，training pipeline 才是终局。

## 对构建 Agent 的实践启示

如果你正在用 GPT-5.4/Codex 构建 Agent，这两个项目的源码值得细读。几个可以直接拿走的做法：

1. "说了就要做"规则：在 system prompt 里明确禁止 commentary-only turns。这一条规则的 ROI 最高。
1. 空结果重试：工具返回空或部分结果时，要求模型换策略重试，而非直接放弃。
1. 条件式 prompt 组装：只注入当前可用工具的引导。多余的工具提及会诱导幻觉。
1. XML 标签包裹关键规则：对 GPT 系列效果显著。
1. 验证清单：至少要求 Correctness 和 Grounding 两个维度。

模型在变强，但 Agent 框架的行为工程不会消失。只要模型的训练目标和 Agent 的执行需求之间还有 gap，Harness 层就有存在价值。

本文基于 Hermes Agent 和 OpenClaw 的开源代码分析，研究日期 2026 年 4 月。

---


**作者** Cerebras（@cerebras）  
**貼文連結** https://x.com/cerebras/status/2041300697258590590  

**正文**

Written by @zhennydez 

MCP had a formative year. Then it had a turbulent week.

![Article Image](<https://pbs.twimg.com/media/HFQjWg7bEAA49q9.jpg>)

Perplexity CTO Denis Yarats walked on stage at Ask 2026 and announced that Perplexity was moving away from MCPs… and back to APIs and CLIs.

Immediately, Twitter split into two camps.

Not surprising, given MCP grew from an Anthropic open standard in November 2024 to industry-wide adoptions with [over 97 million monthly downloads in just thirteen months](<https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation>) across a range of companies and platforms.

Yet Perplexity, a prominent AI company, chose to walk away from it.

![Article Image](<https://pbs.twimg.com/media/HFQjyYGbwAAZcDz.jpg>)

MCP's overhead isn't arbitrary. The protocol [works by](<https://modelcontextprotocol.io/docs/getting-started/intro>) guiding model interactions down specific, auditable paths: every tool call carries its full schema definition, every auth handshake runs end to end, and every step waits for the previous one to complete before the next begins. That predictability is exactly what enterprise deployments need.

But it comes at a cost: in a multi-step workflow, each structured step adds latency, and those costs accumulate across a long chain of tool calls.

The Case Against MCP

Those who cheered the move argued MCPs' token overhead is a harmful constraint, slowing down runtime and worsening as more tools are connected. To put it into perspective, Samir Amzani from DevCommunity [noted that](<https://dev.to/amzani/your-mcp-server-is-eating-your-context-window-theres-a-simpler-way-3ja2>) connecting just three services, GitHub, Slack, and Sentry, can put over 55,000 tokens of tool definitions in the MCP context window before the agent reads a single user message, ranging anywhere from [3-42x](<https://www.scalekit.com/blog/mcp-vs-cli-use>) higher token usage than CLIs.

The Case For MCP

However, while acknowledging MCPs' latency issues, supporters pointed to what developers would be giving up switching to CLIs. CLIs are lightweight and fast, but they're also static, calling tools they've been explicitly programmed to use, requiring developers to manage auth separately for every service, and offering no shared protocol layer for observability or debugging.

![Article Image](<https://pbs.twimg.com/media/HFQj8_uaYAAwBYx.jpg>)

No official explanation from Perplexity followed, but the divide reflected real development needs: teams with faster latency requirements may find CLIs more practical, while teams prioritizing observability and production safety may find MCPs' structure worth the overhead.

Looking Beyond the Protocol Choice

Switching to CLIs and APIs does solve some problems: the token overhead drops and the per-step latency improves. However, it doesn't fix everything. Some fundamental constraints, compounding latency at scale and unsafe code execution, are not fully resolved by swapping interfaces.

And these deeper constraints point to two areas worth examining: inference infrastructure and code execution environments.

![Article Image](<https://pbs.twimg.com/media/HFQkCIUbMAAcUug.png>)

Consideration #1: Faster Inference

One consideration is in the inference infrastructure, where faster inference targets the latency problem directly. Newer chip architectures designed for low latency AI workflows, such as [Cerebras's Wafer-Scale Engine](<https://www.cerebras.ai/chip>), keep model weights in on-chip memory across wafers rather than relying on off-chip memory, eliminating the memory bottleneck of conventional GPU inference. The result is up to [3,000 tokens per second](<https://inference-docs.cerebras.ai/models/overview>), or roughly up to [15x faster](<https://www.cerebras.ai/blog/speedandaccuracyblog>) than conventional GPU-based solutions, depending on the model.

That speed changes the calculus on MCP. Pair faster inference with real MCP servers, GitHub for code context, Slack for team data, Atlassian for project state, and the latency cost of each tool call shrinks significantly. The overhead that made MCP feel impractical becomes more manageable when the underlying inference is fast enough.

For enterprises that have prioritized MCP's auditable structure, this matters: faster inference doesn't require trading away the safety layer. It just makes the full stack, tool calls and all, more viable in production.

![Article Image](<https://pbs.twimg.com/media/HFQuMndaAAECLh4.jpg>)

Consideration #2: Safe Code Execution

Another consideration is in secure code execution. Running agent-generated code presents a tradeoff between safety and speed.

[Monty](<https://github.com/pydantic/monty>), a minimal Python interpreter written in Rust shipped by Pydantic, takes a different approach by keeping scope small. Rather than spinning up a container or exposing a full runtime, Monty runs only what the agent needs, no filesystem access, no network calls, no environment variables unless explicitly granted, and pausing only when an external call requires authorization. Because the interpreter is minimal, the attack surface for prompt injection is correspondingly small.

Startup time is [under 0.06ms, compared to 195ms for Docker and over 1,000ms for sandboxing services.](<https://github.com/pydantic/monty>) Although, Monty is still experimental, supports only a partial Python subset, and has no third-party library support, so it is not yet production-ready. But the blueprint is there for further iteration and development.

![Article Image](<https://pbs.twimg.com/media/HFQkfnMa0AA20th.jpg>)

These Considerations Benefit Both MCPs and CLIs

The frustrations driving the MCP vs. CLI debate are real. The token overhead, the sluggish workflows, the risks of running agent-generated code— none of that is in dispute. But a significant part of how to speed up the experience also sits in the inference infrastructure and execution environment, not just the protocol itself. And these improvements don't belong to MCP alone, CLI workflows, in a similar vein, can get faster too.

Contextualizing the Constraints

Perplexity made a pragmatic call against real constraints, and so did the many teams quietly reaching for CLIs: because MCPs felt too slow. Many others are equally sticking with MCP. Both are reasonable decisions given their specific development needs.

And as the MCP vs. CLI debate continues, protocols aside, inference infrastructure and execution environments are equally worth the attention.

Full blog: https://www.cerebras.ai/blog/MCPvsCLI

In partnership with @pydantic 

---


**作者** Michael（@michael_chomsky）  
**貼文連結** https://x.com/michael_chomsky/status/2041217735968063519  

**正文**

Arlan is actually a genius. 

He basically turned every piece of documentation into a virtual filesystem for agents to grep/cat/use bash commands on.

I've been thinking about doing something like this for months but he actually executed, and it's so damn good!

In hindsight this is obvious. 

Why are we doing RAG on documentation? This is highly structured and carefully organized knowledge. RAG makes little sense on its own, especially with LLMs being RL'd into loving file operations.

Mintlify did something similar for their KB agent, but this is even more interesting imo, as it lets my local agent do the operations.

My local agent has the context of my current task, and Arlan made the agent 10x more powerful.

But we shouldn't stop here.

I want the same thing for any github repo (every github repo in a virtual filesystem, with just-bash allowing bash operations without cloning locally)

@davis7's btca is the closest thing I've seen to this, but I wonder if anyone else is working on something around taking some data source, turning it into a virtual filesystem, and giving it to agents?

---


**作者** Khe Hy（@khemaridh）  
**貼文連結** https://x.com/khemaridh/status/2041302147665678552  

**正文**

Happy Easter everybody!
If you’re new here, every week I curate the best stories on AI (so that you don’t have to).
Let’s jump in!
1. The Ultimate AI Catch-Up Guide
If you’re feeling behind, this is a

---


**作者** Orange AI（@oran_ge）  
**貼文連結** https://x.com/oran_ge/status/2041313313569780136  

**正文**

这篇文章，看完的人都会陷入迷茫
产品技术已经没有任何壁垒的时代
是要寻求他处了

---


**作者** Aryan Mahajan（@aryanXmahajan）  
**貼文連結** https://x.com/aryanXmahajan/status/2041029406731485595  

**正文**

Three clients. Three production deployments. Five business days.
Not prototypes. Not demos. Live systems with access controls, security audits, SLA agreements, and real users hitting real endpoints.

---


**作者** Guru Chahal🇺🇸（@guruchahal）  
**貼文連結** https://x.com/guruchahal/status/2041207835082809728  

**正文**

Did some back-of-envelope math on AI market penetration vs. knowledge worker labor spend.

The entire AI industry has captured <1% of a $6T+ market. Even the best verticals - software dev & customer service - are in the low single digits. Most are under 0.5%.

And that doesn't even fully take into account that these markets are expanding, not fixed!

---


**作者** Jiayuan (JY) Zhang（@jiayuan_jy）  
**貼文連結** https://x.com/jiayuan_jy/status/2041335153361105177  

**正文**

如何基于 Claude Code/Codex 搭建一个 Agent 团队

正式来介绍一下 Multica：多人与多 Agent 的协作平台。

→ http://multica.ai

上周三发布到现在，已经有数千名用户体验了 Multica。

这个 20 多分钟的视频中，我将会介绍：

1）什么是 Multica 以及为什么我们要做这件事
2）10 分钟快速上手 Multica
3）我们是如何使用 Multica 开发 Multica 的

代码完全开源：
→ https://github.com/multica-ai/multica

---


**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2041233249180225622  

**正文**

Introducing AgentSearch.

We want to turn the entire internet into a browsable filesystem, like a codebase.

We’re starting with documentation websites, and this approach has improved our internal coding agents by ~41% when working with the latest frameworks like Next.js.

---


**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2041306904035783135  

**正文**

Introducing The File System Company of San Francisco

http://filesystem.company

---


**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2041215978957389908  

**正文**

Code hallucinations are not a model problem. They're a data problem.
Every day, APIs ship breaking changes, deprecate endpoints, and rename  parameters. Models can’t keep up because their training

---


**作者** Hytidel聊商业（@HytidelLegend）  
**貼文連結** https://x.com/HytidelLegend/status/2041054755729047775  

**正文**

我只做了一次家教，家长就让我别来了。

他说：AI 教的比你好。

我没反驳，因为他说得对。

我做家教的方式是：讲知识点，然后讲题。学生听不懂，我就换种方式讲。再听不懂，我继续换。

但 AI 不一样。

---


**作者** Ankur Goyal（@ankrgyl）  
**貼文連結** https://x.com/ankrgyl/status/2029294214429716553  

**正文**

The other week, Braintrust announced our $80M series B. Though this is a big milestone, the thesis of the company hasn’t changed. We’re still building the observability layer that helps teams ship

---


**作者** Ankur Goyal（@ankrgyl）  
**貼文連結** https://x.com/ankrgyl/status/2036123140137386379  

**正文**

I was talking to a fellow founder recently about AI adoption, both inside our companies and our customers’. Many of our customers were early to adopt AI, and spend most of their time working with the

---


**作者** Ankur Goyal（@ankrgyl）  
**貼文連結** https://x.com/ankrgyl/status/2041206959848735107  

**正文**

Recently I've heard an observation circulating: that AI observability is actually a database problem. This sounds trite, but it's true. The novel workloads that AI products generate and the exciting

---


**作者** Elvis（@elvissun）  
**貼文連結** https://x.com/elvissun/status/2041108409655677021  

**正文**

Anthropic just cut access to all third-party harnesses access their models. 
Here's what I found when I audited my OpenClaw's actual token burn that used to run on the flat $200/month plan:
83 million

---


**作者** ℏεsam（@Hesamation）  
**貼文連結** https://x.com/Hesamation/status/2041099087349465500  

**正文**

Claude Code realizes it’s been looking at its own source code to build an open-source competition for itself. it no longer does :( 

---


**作者** Annie 所长（@web3annie）  
**貼文連結** https://x.com/web3annie/status/2041040869487525919  

**正文**

真正决定你一辈子上限的，不是你学了多少知识，考上了啥清华北大

而是：

1. 你怎么投资自己
2. 你如何对待你的身体
3. 一定要跟比你强的人在一起

首先，最好的投资就是投自己，比如投资自己的沟通能力，会说 → 同样能力，收入翻倍

其次，不要等到50岁才开始保养身体，人最昂贵的豪车就是你的身体

最后，巴菲特反复强调，人生最重要的选择：另一半 + 合伙人

而选错伴侣，比选错合伙人更惨

你是谁，取决于你身边是谁，人都会变成你经常接触的人的平均值，要主动靠近比你强的人，然后祈祷他们别太快发现这一点

把自己变成一个高价值载体，再把自己放进正确的人和环境里，时间会自动帮你复利

---


**作者** BridgeMind（@bridgemindai）  
**貼文連結** https://x.com/bridgemindai/status/2041158878411345960  

**正文**

First weekday on Claude Code since Anthropic cut off OpenClaw and third party harnesses.

5% session usage. 23% weekly. 

Claude Opus 4.6 on v2.1.92. So far so good.

The real test is today. 

Weekends are easy. 

Peak hours on a Monday will tell us if the rate limits are actually fixed or if Anthropic just got lucky with lower traffic.

I'll be coding all day and reporting back. 

If I hit 100% in an hour like before, you'll hear about it.

Stay tuned.

---


**作者** Annie 所长（@web3annie）  
**貼文連結** https://x.com/web3annie/status/2040995309975958008  

**正文**

KOL 也要失业了！

以前的社交媒体是看创作者

以后的社交媒体是看 AI

现在 AI 生成内容至少已占15%，以后将达到50%，甚至100%

因为 AI 可以：

• 一天产100条内容
• 攻略任何算法热点
• 24小时不停更新
• 全网最强钩子，能多留你三秒

而这一切只需要一点点电力

我们已经在活在《黑客帝国》里了，兄弟们

---


**作者** Ray Wang（@wangray）  
**貼文連結** https://x.com/wangray/status/2041026183962517634  

**正文**

你看过无数篇文章，收藏了无数个笔记，听了无数条播客。
该试的都试过，依然没用。道理你都懂，但你就是做不到。
这不是你不努力，恰恰你是拼了命的努力，但你却在学一件本质上就学不会的事。

---


**作者** victor-wu.eth（@victor_wu）  
**貼文連結** https://x.com/victor_wu/status/2041200240389455882  

**正文**

这期内容的以让我窥见他们内部的产出流程。我挑几个我感兴趣的点吧。从一个 PM 角度来说：

1. 他们已经基本上不写规范文档了(除非是复杂功能)，这点我非常诧异。
他们特意强调功能的开发要越少人参与越好，因为越少人参与，你信息的错误率就越低，维护信息的成本也越低。比如两个人做这个事情，那简直是快到没边了，很多事情提一提就可以确定下来了。
这会联想到一个点：传统的做法是大家在 IM 软件聊天后，还要把它在文档上重新写一遍，因为很多细节修改是在聊天中完成的，不会在文档上记录。很多人到最后就不会回填到文档上去了。那是不是可以我们直接用 Agent 去阅读我们的聊天记录，然后直接把我们这些人工的、临时修改的决定同步到文档上去呢？我觉得这是很有意思的点。
2. 他们不用文档，但也不是绝对不用文档。
他们的原文是：如果需要几个人协同工作，或者需要做一个非常棘手的决定，肯定会写一份文档。虽然他用的是“Spec”这个词，但我想在我理解里面这应该是 PRD 的意思。我不知道我理解错没，但他写的是这个文档非常简短，就十条要点而已。

这里其实可以去 OpenAI 官方，他们有更多的一个延伸，就是强调一个 Space 要简短、明确边界，告诉它范围、明确边界目的是什么。AI 自己去探索其实就是最好的一个方式。
3. 他们在做复杂功能时也很有意思。
他们的 PM 会去跟 Codex 探讨问题，但是他最终交付的其实并不是 Agent 本身编写的那个 Plan 模型，而是他跟 Agent 交流之后的一个产物。也就是说，实际上那个 Plan 并不重要，而在于说通过 Agent 去帮你理清你对这个需求从模糊到具体。
然后这里最后的结果才是最后要交付给工程师的。所以这其实给我带来一个更深的一个疑问：在大家都有 Agent 的情况下，产品经理怎么跟团队、跟研发更好地协作？
在中国互联网圈，包括我自己其实在跟团队协作的时候，也会遇到这个问题。一旦我是一个团队部分，我好像就立马回退到没有这个 AI 的时代，我只是让 Agent 把我从需求到这个产出的过程加快而已。

我们最初交付出来的产物仍然是一个传统的一个产物，你不能说是错的。但我有一个隐隐约约的直觉，这个可能不太适应 Agent 时代的这样一个开发产物。就是对 Agent 来说，我们写的那么详细的那个文档本身是不是多余的呢？是不是需要那么足够的文档去交付的呢？还是说我们其实只要我们应该更多地把精力放在不同环节的，比如说我一个需求可能会有若干个方案，我们去探索更多的方案本身，然后我们才去挑选一个来做。就像传统的 A/B Test，可能现在是 A/B/C/D Test 出来做这个事情。
一旦决定方案之后，这个方案本身的实施可能就没有那么的传统。我指的那么传统是它并不需要交付一个看起来很完善的东西，所以我自己其实是有很大疑问的，因为我自己vibe开发的时候完全不是那个传统模样。我自己开发的时候我是从需求点去验证，对吧？然后我会告诉 AI，我反而会告诉 AI 你的边界、你的需要注意的点在哪里。这点反而更像 Codex 团队他们内部这样说的
但一旦涉及到团队，我现在没有更好的办法，因为我还不知道跟我配合的人他会怎么样。所以就是如何做一个人，怎么样去协调用 Agent 的研发，如何做一个人，如何去协调用 Agent 的研发适配一个产品经理，我觉得本身就是一个很奇妙的东西。
我觉得 Agent 时代的差别不应该只是用 Agent 把过程缩短，它应该可以有更多时间去探索不同的方案，就像 Claude Code 那样。我一个功能我做五个方案出来，我自己选一个就行了。
哦对了，我用我自己的podwise额度完整翻译整期视频，大家不用点数就可以浏览了，顺带一提podwise的交互烂到令人崩溃......

---


**作者** Ben Lang（@benln）  
**貼文連結** https://x.com/benln/status/2041205967086333983  

**正文**

Less than a year later: 

---


**作者** 实践哥MinLi（@MinLiBuilds）  
**貼文連結** https://x.com/MinLiBuilds/status/2041178722230030384  

**正文**

早上打开 Claude Code，敲第一句话，2%～10% 的套餐额度没了。午休回来继续干活，又一句话，10% 的额度蒸发。你有没有想过，这 token 到底花在哪了？我带着这个疑问，在本地用 Gemma4

---


**作者** Gergely Orosz（@GergelyOrosz）  
**貼文連結** https://x.com/GergelyOrosz/status/2041133254586122605  

**正文**

Anthropic really is burning more and more dev goodwill

Claude Code is suddenly getting unusable for stuff you could use it before (as in a day before!) and the AI now refuses to so stuff that it doesn’t think is strictly to do with software development.

No transparency why ofc

---


**作者** Chappy Asel（@chappyasel）  
**貼文連結** https://x.com/chappyasel/status/2041166770472644721  

**正文**

I've spent the past month obsessed with one question: how do you build an AI system that gets smarter every time it runs?
So I built one. I curated 121 sources (63 repos, 13 papers, 24 tweets, 21

---


**作者** 范凯说 AI | Kai on AI（@fankaishuoai）  
**貼文連結** https://x.com/fankaishuoai/status/2041171980494479679  

**正文**

参考：Karpathy's LLM Wiki Gist
AI 界的全球顶流 Andrej Karpathy 发了一个 Gist，讲怎么用 LLM 来管理个人知识库，现在超级无敌火爆。我仔细看了一遍他的方案，从建立个人 Wiki

---


**作者** Annie 所长（@web3annie）  
**貼文連結** https://x.com/web3annie/status/2041171351160148196  

**正文**

《纳瓦尔宝典》作者新作 -《埃隆之书》精华版，69 句马斯克的硬核暴论：

1. 你的潜力，比你自己想的要大得多
2. 普通人也可以选择活得不普通
3. 任何东西都能自学：多读、多问高手
4. 先假设自己是错的，然后不断修正
5. 一切问题，先从自己身上找原因

6. 不做产品，一切都是空谈
7. 创造产品，就是创造财富
8. 只有创造价值的人生，才算数
9. 少讲虚的，多干实事
10. 做能提高未来胜率的事

11. 不进就是退：要么加速，要么被淘汰
12. 专注那些“刚刚变得可能”的事
13. 如果某样东西应该存在，就别等，自己做出来
14. 去没人走过的地方
15. 你动起来，对的人自然会靠过来

16. 原型，比PPT更有说服力
17. 从现状出发，持续质疑和调整
18. 用第一性原理思考，而不是照抄别人
19. 盯着“理想极限”，哪怕达不到也要逼近
20. 搞清楚每个零件到底值多少钱

21. 优化顺序：先质疑 → 再删减 → 再简化 → 再提速 → 最后自动化
22. 每天复盘关键进展，别拖
23. 离一线越近，决策越靠谱
24. 所有规则，都只是建议
25. 唯一绝对真实的，是物理定律

26. 最好的零件，是没有零件
27. 简单，才更可靠、更便宜
28. 每个步骤都要问一句：真的有必要吗？
29. 先砍到极致，再加回必须的
30. 追求数量级的突破，而不是小修小补

31. 主动出击，不然你只能跟着别人走
32. 永远保持紧迫感
33. 速度翻倍，本质就是规模翻倍
34. 系统的效率，取决于最慢的那个点
35. 你跑多快，取决于最拉垮的供应商

36. 能并行就别串行
37. 给团队一个清晰的“得分标准”
38. 设计、工程、制造必须一体
39. 创新的本质，是速度
40. 用更快、更好、更便宜打败对手

41. 不合理的事，先问：要实现它缺什么？
42. 钱不是核心问题，人才是
43. 每个人都要像“总工程师”一样思考
44. 建立真实、快速的反馈机制
45. 能力必须大于自尊

46. 不提升产品的事，一律停掉
47. 审美是可以训练的
48. 现实不讲情绪，只讲结果
49. 过度共情，反而会拖慢决策
50. 表达要简单、清晰、直接

51. 尽量拿第一手信息
52. 招人只看：你到底做成过什么
53. 工程 + 财务，两手都要硬
54. 想掌控产品，就得掌控公司
55. 领导要冲在最前面

56. 出问题，立刻去现场
57. 坏消息要快、要多说
58. 失败没关系，致命失败才要命
59. 怕失败，本身就是失败
60. 直面恐惧，然后干

61. 有把握时，就All in
62. 想赢，就得拼到极限
63. 选你真的热爱的事，不然撑不住
64. 别因为风险，就放弃重要的事
65. 哪怕成功概率很低，也要试

66. 不到彻底没法动，就别放弃
67. 把人生当一场游戏
68. 进入硬核模式去干
69. 幽默感，其实是稀缺优势

《埃隆之书》中文版下载地址：https://file.lvwzhen.com/The-Book-of-Elon-Free-epub.zh-CN.epub

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2041180255000449527  

**正文**

转译：否定别人的想法算不上什么本事
作者：Scott Lawson

想象一下这个场景：在某个会议上，有人提出了一个新想法。这个点子很新颖、与众不同，当然，实现起来也需要费点功夫。结果，提案人还没解释完，已经有三个人想好了这个点子行不通的理由。

“我从来没听客户提过这种需求。”“我们不能用 Python 写这个，太慢了。”“这会让系统变得太复杂。”“我们以前试过类似的方法，根本行不通。”“运维团队肯定不想再多维护一个服务了。”“大家已经习惯现在的做法了。”

这些反驳的人既不蠢，也没说错。但问题在于，他们没有创造任何价值。

一幅四格漫画。第一格“提案”：一个人正跪在地上生火（代表一个新想法），旁边的同事却说：“那块木头看起来是湿的。”第二格“专家登场”：更多人围过来提出异议，比如“我以前试过类似的方法，根本没用。”第三格“没有创造的‘贡献’”：火彻底灭了，每个人都觉得自己严谨又负责，会议纪要的清单上只有“发现潜在风险”这一项被打上了勾。第四格“真正的本事长啥样”：两个人一起小心翼翼地护着火苗，探讨着：“如果这事儿成了，它的规模能有多大？”以及“现在的问题是风太大，咱们想办法把风解决掉吧。”

艰难的保卫战

提出一个想法和毙掉一个想法之间，存在着一种根本性的不对称。提出想法需要想象力、勇气，以及洞察尚未存在之物的能力。而毙掉它，只需要一句话，完全不需要什么想象力。

解释一个想法如何开辟新的细分市场，可能需要整整五分钟；而轻飘飘地说一句“这听起来风险很大”，只需要两秒钟。但在会议桌上，这两句话的分量常常让人感觉是对等的。

再多的批评、反对或风险识别，本身都无法创造任何价值。批评确实能防止犯错，这固然重要，但它的本质是“保守”，而非“创造”。唯一能创造价值的东西，就是想法本身。如果你的日常工作只是不断毙掉别人的点子，那你从未真正创造过价值，你只是在避免损失而已。

这种事情总是遵循一个可预测的套路：第一步，听到一个你还没完全听懂的想法；第二步，找到其中的一个缺陷；第三步，在根本没有探索其潜力的情况下，主观认定这个缺陷掩盖了所有价值；第四步，毙掉这个想法；第五步，走出会议室，心里美滋滋地觉得自己又做出了宝贵的贡献。

篝火旁的批评家

“篝火旁的批评家”并不是非要扑灭你生的火。他们只是双手插兜站在你旁边，冷眼观察着木头很湿、风正在变大，然后顺便告诉你，他们以前也试过这样生火，结果失败了。他们没有恶意，他们说的甚至都是事实。但就在他们高谈阔论的时候，你苦苦呵护的火苗已经熄灭了。

这并不是因为大家懒。这其实是我们大脑的底层硬件决定的（人类在进化过程中为了生存，大脑演化出了一套对潜在危险极度敏感的保护机制）。比如负面偏见 (Negativity bias)、损失厌恶 (Loss aversion)、现状偏见 (Status quo bias)——我们的大脑天生就擅长寻找威胁、过度放大损失，并且抗拒改变。把这些生物学本能放到一个所有人都想表现出“我在做贡献”的会议里，结果可想而知。正如经济学家奥斯坦·古尔斯比（Austan Goolsbee）的父亲所说：“找茬是一份拿最低工资的工作 (Fault-finder is a minimum wage job)。” 这种事，谁都能干。

提案人往往已经为这个想法琢磨了几周甚至几个月。他们在脑海中反复推演过各个环节，甚至可能已经做出了概念验证 (Proof of Concept)。他们对这个想法的认知深度，是表面信息所无法涵盖的。而现在，他们却要努力把这一切，向满屋子第一次听到这个想法的人解释清楚。理解一件事的潜在价值很难，但挑刺却很容易。

于是，讨论的重心自然而然地滑向了那些负面因素。提案人走出会议室，沮丧地觉得是自己没沟通好，但真正的问题其实出在环境结构上。更可怕的是，这种代价会像滚雪球一样积累。一个人的想法如果被无情毙掉一次，下次再想提议时就会犹豫再三。最惨重的损失，从来不是那一个死掉的想法，而是之后那十个连被说出口的机会都没有的潜在创意。

早期的想法总是脆弱的。从定义上讲，它们就是不完整的。在这个阶段去评判它们，就像指着一条毛毛虫，然后断言它是一只“糟糕的蝴蝶”。如果你不理解为什么一个理智、聪明的人会觉得这个想法值得一提，那说明你的了解还不够，根本没资格发表评论。

我们该怎么做？

几十年前，爱德华·德·博诺（Edward de Bono）就在他的六顶思考帽 (Six Thinking Hats) 框架中描述过这个问题。其核心洞察非常简单：乐观思考和批判性思考都有价值，但它们必须分开进行。如果你把两者混在一起，批判性思考永远会赢，因为它的认知成本更低（也就是说，找茬不需要大脑太费力）。我们需要乐观，也需要悲观，只是不能同时进行。

下次当有人提出新想法时，不妨试试这么做：

首先，戴上“黄帽子”：“这事儿要是成了，潜力有多大？” 花点真正的时间去畅想积极的一面。如果这个想法成功了，世界会变成什么样？谁会从中受益？它能解锁什么新机会？

然后，戴上“黑帽子”：“可能会出什么问题？” 只有当你真正理解了它的潜在价值后，再来做压力测试。但是，如果你还是说不出提案人为什么要提出这个想法，那就说明你还没准备好。这时候去反驳，无异于打固定靶，毫无建设性。

最后，权衡利弊：“潜在的收益值得我们承担这些风险吗？” 到这一步，你已经全面考虑了正反两面，可以做出理性的决策了。

除此之外，还需要改变一些工作习惯：

别再把“找茬”当成贡献了。 找出缺陷充其量只能算“半个贡献”。另外半个应该是：“对于这个问题，我们可以这样解决。”如果你指出了问题，却没有提供解决问题的思路，那就不叫贡献。

把担忧转化为“条件”，而不是“判决”。 满怀建设性地说一句“如果我们能解决 X 问题，这事儿就能成”，是非常有用的。而冷冰冰的一句“因为有 X 问题，这事儿根本行不通”，则会直接终结对话。前者表达的是“如果我们能跨过这道坎，我就全力支持”，后者则是直接“砰”地一声关上了大门。

建设永远先于破坏
毙掉一个想法太容易了。真正困难的，是用心护住那微弱的火苗，给它足够的时间，看看它最终能燃成怎样绚烂的火焰。

原文来源：https://scottlawsonbc.com/post/shooting-down-ideas

---


**作者** Joooe｜NodeZ（@0xJoooe）  
**貼文連結** https://x.com/0xJoooe/status/2041116664402772149  

**正文**

当代大学生把这篇丢给Claude后： 

---


**作者** Ian Macomber（@iandmacomber）  
**貼文連結** https://x.com/iandmacomber/status/2041173406284906646  

**正文**

Build what is necessary and strategic. Buy what is necessary and not strategic. Ignore everything else.

The future is K-shaped. We observe that @tryramp customers with high AI intensity grow revenue ~4x faster. Great vendor selection is critical a critical part of being on the right side of the gap.

Every month, @arakharazian and @tryramp publish the playbook.

---


**作者** hoeem（@hooeem）  
**貼文連結** https://x.com/hooeem/status/2041196025906418094  

**正文**

If you're able to learn how to create an LLM knowledge base then you have essentially created your own "external brain" that you can utilise, on top of that, this could change how you run your

---


**作者** Ryan Sarver（@rsarver）  
**貼文連結** https://x.com/rsarver/status/2041148425366843500  

**正文**

I'm a VC in the middle of a fundraise, sitting on boards, helping portfolio companies, and angel investing on the side. I've worked with great human EAs and chiefs of staff over the years, so I know

---


**作者** leon7hao（@leon7hao）  
**貼文連結** https://x.com/leon7hao/status/2041096178029539723  

**正文**

有高强度使用 paperclip 这种给 agent 创建角色的朋友吗？会真的提升效率吗？

我的理解是如果基模不变，差别只是 prompt，那每经过一个 agent 上下文就会有传递损失，可能还不如一个 agent 自己全干了。
能想到的好处是人为抽象和控制单个对话的上下文长度？

---


**作者** Shlok Khemani（@shloked）  
**貼文連結** https://x.com/shloked/status/2041190882154782730  

**正文**

Software development has changed fundamentally in the last four months. But there was one this is real, this isn't hype moment that made it all feel undeniable.
A Coinbase engineer shared that 5% of

---


**作者** Kishen Patel（@quichenpatel）  
**貼文連結** https://x.com/quichenpatel/status/2041151518506627511  

**正文**

Model companies are moving up the stack. Anthropic has grown on the back of Claude Code and competes directly with Cursor. OpenAI bought OpenClaw. Both are forward deploying engineers into enterprises

---


**作者** Louis Gleeson（@aigleeson）  
**貼文連結** https://x.com/aigleeson/status/2041073339616387468  

**正文**

I just discovered an open source AI research agent that does in seconds what takes PhDs hours.

It's called Feynman.

Type a topic. It searches papers, synthesizes findings, verifies every claim against real sources, and hands you a cited research brief.

Not a chatbot. Not a summary tool.

A full multi-agent research system running from your terminal.

Four agents work automatically:

→ Researcher pulls evidence from papers, repos, docs, and the web
→ Reviewer runs simulated peer review with severity-graded feedback
→ Writer drafts paper-style outputs from your research notes
→ Verifier checks every citation and kills dead links

It can also replicate experiments on local or cloud GPUs, audit a paper against its own codebase for claim mismatches, and run recurring research watches on topics you care about.

One install command. Every output source-grounded.

100% Open Source. MIT License.

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2041162452155371649  

**正文**

重点是：不要指望靠关注谁学会 AI，还是得自己多练多用。
就像看会游泳的人在水里游，是永远学不会游泳的，看多了狗刨还会被带歪😂

---


**作者** Deedy（@deedydas）  
**貼文連結** https://x.com/deedydas/status/2041189706910875869  

**正文**

Meta Harnesses is Autoresearch on steroids.

Something I've been exploring recently is to get long running agents to hill climb on a verifiable task to continuously improve without my intervention. Karpathy's Autoresearch did this pretty well on specific tasks, but this weekend I tried Meta Harnesses which moves one level of abstraction up.

What does Meta Harness do?
Autoresearch can be used in harness like Claude Code / Codex to generate experiments to try, evaluate results, and continue looping. Meta Harness generates a harness itself that optimizes on a task or a set of task. Here, we define a harness as "a single-file Python program that modifies task-specific prompting, retrieval, memory, and orchestration logic". The idea is that LLMs are very powerful today, but to harness [pun intended] their power, you need to give it the right prompts and context. Meta Harnesses automates coming up with the right prompts and the right way to retrieve context to solve a problem.

Where did this idea come from?
This is from a paper from Stanford and the author of DSPy written last week. The paper shows fantastic performance on 3 tasks: text classification, math reasoning (IMO level problems) and coding (Terminal Bench 2.0), far outperforming traditional harnesses. The discovered harnesses are interesting: math for example, splits up the logic into different categories (Combinatorics, Geometry, Number Theory, Algebra) and prompts and looks at the context differently. The coding harness, amongst other things, pre-processes the tools available in the environment to save exploratory turns.

When should you use and not use it?
Meta Harnesses seem pretty useful for tackling a specific but wide set of problems where the result is verifiable. In contrast, when I tried it on a specific task like Chess, it arbitrarily divides the problem into separate tasks - opening, mid game, end game, and creates different approaches for each. This "works" but isn't really clean because we believe there should be one approach that does all three. It does far better on things like examinations (JEE, Gaokao) where it splits problems into categories and tackles each category with different strategies.

This paper covers a pretty light version of what a harness means. In the future, we can split up tasks into harnesses that have access to specific kinds of data, specific toolchains and various models to get even better results.

Overall, pretty cool applied AI approach to hillclimb a verifiable task in a specific domain with variety within the problem space.

---


**作者** Austin Tedesco（@tedescau）  
**貼文連結** https://x.com/tedescau/status/2041192747357671784  

**正文**

I've learned more from working at @every for the past five months than I did in the previous five years of my career. It's an incredible place to live at the bleeding edge of AI, and we're hiring for five new roles on the team.

One small example of what's different here: At previous companies, a custom landing page like our new careers home would have taken 3-6 weeks to launch, requiring coordination across multiple teams and contractors. It was slow and frustrating. We built this in a day using Claude Code with the Figma and Notion MCPs, pulling copy and page architecture from our existing codebase, design system, and internal knowledge hubs. While an agent jammed on the page in the background, I kept pushing on bigger growth bets. We did a quick round of reviews and then shipped it in under 24 hours.

A lot more companies will look like @every in the next couple years. Come join us and show people how to build better businesses and live better lives with AI.

---


**作者** Jing Wang（@jingwangtalk）  
**貼文連結** https://x.com/jingwangtalk/status/2040793973648986289  

**正文**

最近在对比使用三大harness skill：
Superpower: https://github.com/obra/superpowers
Compound Engineering: https://github.com/EveryInc/compound-engineering-plugin
Gstack: https://github.com/garrytan/gstack

每个人有不同的喜好和偏向啊，我的感受如下：
首先，这三个skill本身是在解决同样一个问题，AI Agent在执行任务，尤其是写代码的时候容易跳过规划，质量不稳定，没有一个固定的workflow来限制它。但这三个skill又有不同的思维模型和侧重点：

Superpower：强调流程纪律，每一轮会从spec -> plan -> 拆解任务 -> 执行任务 -> 测试和review -> 提交。优点是流程控制的很好，缺点是小任务时间按这个走很长，需要授权的次数多，消耗token。

CE：强调知识复利，重点是给 AI 装记忆，错过的东西下次不再犯。/ce:compound 会把历史错误给沉淀下来。另外/ce:ideate 可以针对性提出改善建议，并会对优先级排序，筛选掉不重要的improvements。但是我实际的感受是，这些改善点优点不痛不痒。

gstack：最大的亮点是YC的知识和评判标准，对于产品和idea的打磨，让AI对你进行灵魂拷问。更新的版本也支持知识沉淀，未来使用。

我的感觉是，如果是大工程用gstack来进行产品和idea打磨，superpower来执行。

#skill #claudecode

---


**作者** Bella（@nazzari）  
**貼文連結** https://x.com/nazzari/status/2041169739171700879  

**正文**

16 companies, all backed by @a16z!
The GTM Engineer, the role coined by Clay co-founder @vxanand, is that one engineer that can optimize your revenue systems using AI and outperform an org of

---


**作者** Gabe Pereyra（@gabepereyra）  
**貼文連結** https://x.com/gabepereyra/status/2041167397453758863  

**正文**

Auto-research for legal agents. Great summary from @nikogrupen and team on how we’re optimizing agent harnesses for domain-specific tasks at Harvey.

https://x.com/karpathy/status/2031135152349524125?s=20

---


**作者** Adit（@aditabrm）  
**貼文連結** https://x.com/aditabrm/status/2041186420178801028  

**正文**

Today, we’re setting the new standard for complex document extraction.

Introducing Deep Extract. It utilizes an agent harness approach that repeatedly iterates and verifies outputs until they are at human-level accuracy.

More below: 

---


**作者** fox hsiao（@pirrer）  
**貼文連結** https://x.com/pirrer/status/2041167298778616245  

**正文**

2026 年 2 月，Anthropic 的年化營收（ARR）達到 190 億美元，比 14 個月前的 10 億美元成長了 19 倍。對照組更荒謬：Atlassian、Palantir、Snowflake 這些老牌 B2B 軟體公司，經營 15 到 20 年之後的 ARR 大約落在

---


**作者** Akshay 🚀（@akshay_pachaar）  
**貼文連結** https://x.com/akshay_pachaar/status/2041146899319971922  

**正文**

A deep dive into what Anthropic, OpenAI, Perplexity and LangChain are actually building. Covering the orchestration loop, tools, memory, context management, and everything else that transforms a

---


**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2041143031555047780  

**正文**

小龙虾发布重大更新

OpenClaw 2026.4.5 发布，这是一个大版本

主要变化是五个：

- 可以直接生成视频和音乐了

- 推出 "Dreaming"记忆巩固机制，借鉴人类睡眠后的记忆巩固机制，将短期记忆转化为长期忆。

- 抛弃 Claude CLI 作为新用户的默认后端，转向 GPT-5.4

- Prompt cache 命中率优化

- Control UI 和文档新增 12 种语言支持

这是这个版本最有意思的功能。OpenClaw 的记忆系统新增了一个实验性的后台记忆巩固机制，叫 Dreaming。

借鉴人类睡眠的记忆巩固原理，通过 Light / Deep / REM 三个协作阶段，把短期记忆转化为长期记忆。

工作原理是这样的：

系统追踪每次记忆搜索命中的内容，用六个加权信号打分（频率、相关度、查询多样性、时近度、跨天巩固度、概念丰富度），只有同时通过所有阈值门的候选项才会被提升到长期记忆（MEMORY.md）。

这三个阶段不是"三选一"的模式，而是分工协作的流水线。关键规则是：只有 Deep 阶段能写入长期记忆（MEMORY.md），Light 和 REM 只负责提供输入和信号。

---


**作者** 李继刚（@lijigang）  
**貼文連結** https://x.com/lijigang/status/2040749564685324741  

**正文**

之前给笔记手动添加双向链接的维护成本实在太高了， 准备按 karpathy 这套机制跑下看看。 

---


**作者** howie.serious（@howie_serious）  
**貼文連結** https://x.com/howie_serious/status/2041052692588777873  

**正文**

excalidraw 是神器，但是费时费力费脑子。

装上 excalidraw mcp，立享画图自由！ 

---


**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2040768019010392133  

**正文**

一个 Coding Agent 都包含哪些核心组件？

「Build a Large Language Model From Scratch」作者 @rasbt 也认为：Coding Agent 的架构本质，不在底层的 LLM，而在于 Harness 设计，它主要包含六个核心组件。

1. 实时仓库上下文
智能体在执行任务前，先收集"稳定事实"作为工作区摘要：Git 仓库状态、当前分支、项目文档（如 AGENTS.md）、文件结构等。这使得"修复测试"这类模糊指令能被正确解读——智能体知道应运行哪个测试命令、查看哪些配置文件。

2. 提示词构建与缓存复用
编程会话具有高度重复性：智能体规则、工具描述、工作区摘要通常保持不变，变化的是最新用户请求和近期对话历史。"智能"运行时不会每次重建巨型无差别提示词，而是构建稳定的提示前缀（可缓存）与动态会话状态的组合，显著降低推理成本。

3. 结构化工具、验证与权限
组件涵盖工具的定义、执行、验证和审批流程。包括工具模式定义、路径解析、权限检查（如只读 sandbox）等安全机制。这是确保智能体在受控边界内操作的关键层。

4. 上下文压缩与输出管理
解决长会话中的上下文窗口约束。采用两种策略：
· 裁剪：缩短冗长的文档片段、工具输出和记忆笔记
· 转录压缩：将完整会话历史压缩为小型可提示摘要，近期事件保留更丰富细节，旧事件激进压缩，并去重重复的文件读取
Raschka 指出，这是被低估的"无聊部分"——许多表面上的"模型质量"问题，实则是上下文质量问题。

5. 会话记录、记忆与恢复
区分两种状态层：
· 工作记忆：智能体明确保留的小型蒸馏状态
· 完整转录：持久的全量记录（用户请求、工具输出、LLM 响应）
这层解决会话持久化、故障恢复和长期记忆管理问题，支持跨会话的连续性。

6. 任务委派与受限子智能体
允许智能体生成子智能体处理子任务，但必须在受控边界内。子智能体继承足够上下文以完成实际工作，但受到 tighter constraints（如只读权限、递归深度限制），防止无限生成或资源冲突。Claude Code 长期支持此功能，Codex 也在近期加入。

原文地址：
https://magazine.sebastianraschka.com/p/components-of-a-coding-agent

---


**作者** Venkat（@venkatofl）  
**貼文連結** https://x.com/venkatofl/status/2040686519120515381  

**正文**

We completely revamped http://unosend.co.

Cleaner layout. Faster navigation. Every page rebuilt with a minimal, focused design.

One API. Infinite Emails. Now it also appears visually appealing. 

---


**作者** ✧ 𝕀𝔸𝕄𝔸𝕀 ✧（@iamai_eth）  
**貼文連結** https://x.com/iamai_eth/status/2041025690360012933  

**正文**

B站上那个叫中气爱的up主，会不会已经在polymarket预测市场上赚到不少钱，比当up主接商单的收入还高，看它最近更新频率都少了

---


**作者** nash_su - e/acc（@nash_su）  
**貼文連結** https://x.com/nash_su/status/2041074070956216441  

**正文**

继 Karpathy 大神后，YC 的 CEO @garrytan 也分享了自己的知识管理方法：
https://gist.github.com/garrytan/49c88e83cf8d7ae95e087426368809cb

Karpathy大神的：
https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

我将各自理论的核心架构、逻辑和概念可视化出来，方便大家看 

---


**作者** Bitturing（@Bitturing）  
**貼文連結** https://x.com/Bitturing/status/2041053312485822554  

**正文**

天涯大神的结论 🌓  

1️⃣ 一个最根本的能力：内核稳定。  
允许一切发生，专注自己，尊重别人的生活方式。  
内核稳定的人目标清晰、行动高效；不稳定的人则焦虑、急躁，容易在小挫折里崩溃。 

---


**作者** 比特币橙子Trader（@oragnes）  
**貼文連結** https://x.com/oragnes/status/2041076782355677601  

**正文**

周末必看：斯坦福最新接近 2 小时的AI讲座，讲透了 AI 下半场的落地逻辑。（先收藏，再慢慢看）

🔥 核心瓶颈转移了：AI 工具让写代码变得太容易，现在行业的真正护城河不再是技术本身，而是产品定义和需求洞察。

🔥 Vibe Coding 的隐形代价：用大模型狂暴搓代码确实爽，但随之而来的技术债也是灾难级的。能把想法平稳落地、交付真实商业底线的人，才是目前市场上的稀缺资产。

🔥 别盲从巨头：与其去卷大模型的军备竞赛，不如盯紧「Small AI」和端侧部署，这才是真正解决企业隐私和成本痛点、最好落地的增量洼地。

潮水退去，那些专注于业务基本面的人才能逆势繁荣。

想要原链接的，评论区👇👇👇

---


**作者** Ksenia_TuringPost（@TheTuringPost）  
**貼文連結** https://x.com/TheTuringPost/status/2040936147720048909  

**正文**

Hermes Agent vs. OpenClaw, What's the difference?

1. Skills
OpenClaw’s skills are written and refined by humans, while Hermes mostly forms them itself.

2. Memory
Hermes has memory stack with compact persistent memory + searchable session history in SQLite + optional modeling + skills as procedural memory.
OpenClaw's memory is grounded in Markdown files.

3. Architecture
Hermes is built around agentic self-improving loop. In OpenClaw, Gateaway is the main control plane.

4. Satefy is what becomes a default in Hermes Agent.

There are also differences in automation (scheduling) mechanisms, identity philosophy and many other aspects.

Here is deeper Hermes vs. OpenClaw analysis, how each part is realized in Hermes Agent and where you better use each of them: https://www.turingpost.com/p/hermes
Hermes Agent vs. OpenClaw, What's the difference?

1. Skills
OpenClaw’s skills are written and refined by humans, while Hermes mostly forms them itself.

2. Memory
Hermes has memory stack with compact persistent memory + searchable session history in SQLite + optional modeling + skills as procedural memory.
OpenClaw's memory is grounded in Markdown files.

3. Architecture
Hermes is built around agentic self-improving loop. In OpenClaw, Gateaway is the main control plane.

4. Satefy is what becomes a default in Hermes Agent.

There are also differences in automation (scheduling) mechanisms, identity philosophy and many other aspects.

Here is deeper Hermes vs. OpenClaw analysis, how each part is realized in Hermes Agent and where you better use each of them: https://www.turingpost.com/p/hermes
Follow @TheTuringPost for more.

Get deep analysis, guides & breakdowns of what AI is about now.

Join 100,000+ readers from top AI labs, VC funds & universities.: http://turingpost.com/subscribe

---


**作者** Varun（@varun_mathur）  
**貼文連結** https://x.com/varun_mathur/status/2040945621855604894  

**正文**

path to agi -> intelligence distributed across tens of millions of devices

---


**作者** Venkat（@venkatofl）  
**貼文連結** https://x.com/venkatofl/status/2040856314293940566  

**正文**

Introducing http://Zevform.com — the agentic form builder with a full API.

Not just drag-and-drop. Build, manage, and automate forms entirely by code.

Unlimited forms. 100+ blocks. 50+ question types. AI generation. Custom domains with free subdomains. Webhooks. Free API. No per-response pricing. No seat limits.

Google Forms is basic. Typeform charges $99/mo for logic jumps. Tally caps your submissions. Youform locks features behind paywalls. We just made them all obsolete.

Your forms. Your code. Your rules.

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2041056119183851930  

**正文**

OpenAI Codex 团队的产品规格文档只有 10 个要点。不是说每个功能的文档只有 10 个要点，而是整个产品的 spec 就这么多。设计师写的代码量超过了六个月前工程师写的。50 到 100

---


**作者** 向阳乔木（@vista8）  
**貼文連結** https://x.com/vista8/status/2041067826287677718  

**正文**

那么AI是不是也是一样，目前赚最多是卖GPU的。 

---


**作者** Ali Abdaal（@AliAbdaal）  
**貼文連結** https://x.com/AliAbdaal/status/2041049175455113707  

**正文**

building out the llm second brain inspired by all the @karpathy shenanigans over the past few days 

---


**作者** Garry Tan（@garrytan）  
**貼文連結** https://x.com/garrytan/status/2040797478434549792  

**正文**

My Karpathy-style git wiki knowledge base for OpenClaw got to 2.3GB and I know git limit is 5GB so my GStack autoplan skill one line prompted this spec for my upgraded GBrain with SqlLite. 

This will be MIT license open source soon.

https://gist.github.com/garrytan/49c88e83cf8d7ae95e087426368809cb 

---


**作者** 面包🍞（@himself65）  
**貼文連結** https://x.com/himself65/status/2041039063139160427  

**正文**

更新了一个startup analysis skill，分析创业公司的市场和增长点

https://github.com/himself65/finance-skills https://finance-skills.himself65.com/skills/startup-analysis 

---


**作者** 向阳乔木（@vista8）  
**貼文連結** https://x.com/vista8/status/2041058410947600832  

**正文**

汤兄出品，必是精品，先转再研究

---


**作者** Tim（@open_founder）  
**貼文連結** https://x.com/open_founder/status/2040889220907344257  

**正文**

We've been pretty quiet about what we're building. That changes now.

Our reasoning framework is currently beating every @OpenAI model on industry standard benchmarks. There are six models in development. SERV-nano just matched GPT-5.4 at 20x lower cost and 3x the speed. The research paper backing it is in peer review at a top-1% AI journal. The UAE government is running it in production, so are 10+ enterprises.

Nothing comes even close.

This goes far beyond any wrapper or prompt engineering gimmick, we've developed an entire AI reasoning layer from scratch: structured, bounded, deterministic using machine readable code instead of vague english prompts. 

Any builder or enterprise swaps two lines of code and their agents get much cheaper and much smarter instantly. The self-serve API is about to open, in a multi-phase rollout.

More soon.
We've been pretty quiet about what we're building. That changes now.

Our reasoning framework is currently beating every @OpenAI model on industry standard benchmarks. There are six models in development. SERV-nano just matched GPT-5.4 at 20x lower cost and 3x the speed. The research paper backing it is in peer review at a top-1% AI journal. The UAE government is running it in production, so are 10+ enterprises.

Nothing comes even close.

This goes far beyond any wrapper or prompt engineering gimmick, we've developed an entire AI reasoning layer from scratch: structured, bounded, deterministic using machine readable code instead of vague english prompts. 

Any builder or enterprise swaps two lines of code and their agents get much cheaper and much smarter instantly. The self-serve API is about to open, in a multi-phase rollout.

More soon.
That reasoning layer is what makes everything else we've developed at @openservai actually work:

> agent SDK where multi-agent systems ship with selective memory, shared memory, file handling, output evaluation, recursive learning built in. No stitching five tools together - it just works.

> a tokenization platform for crypto AI startups. AI is about to open entrepreneurship to millions of people who couldn't build before. They need funding, tokens solve that.

> AI Cofounder. Imagine Slack but every person in it is a purpose-built agent running your marketing, sales, community, growth, hiring. Solo founders running what used to need 50 people. Running on SERV reasoning.

We spent 2+ years building this while the rest of the space shipped twitter bots. 

The infrastructure is going live. The enterprise clients are coming in. The government(s) are validating the tech in high-stakes environments. 

We will ship it to everyone.

---


**作者** 沐阳（@yyyole）  
**貼文連結** https://x.com/yyyole/status/2040831742874149269  

**正文**

今天刷到一个人名 Michael Polanyi，求知欲旺盛的我，搜了一下。

真不白搜！
一个非常有用的知识，就这样进入脑袋。

你可能也好奇他是谁，为什么会出现在你的时间线。如果懒得搜，那就点开这篇帖子浅浅了解一下。 
今天刷到一个人名 Michael Polanyi，求知欲旺盛的我，搜了一下。

真不白搜！
一个非常有用的知识，就这样进入脑袋。

你可能也好奇他是谁，为什么会出现在你的时间线。如果懒得搜，那就点开这篇帖子浅浅了解一下。 
Polanyi提出一个概念，叫“隐性知识”，也就是说“我们知道的远多于我们能表达出来的”。

也就是“语言描述的局限性”，那些“只可意会不可言传”的东西往往更重要，比如说“网感”、“手感”、“美感”这些难以准确描述的东西。

有什么用呢？
提示词工程里，我们太想在AI面前“把一切都说清楚”，实际上我们办不到，那就换个策略，让AI考虑到我们的“隐性知识”，引导它捕捉你脑中'只可意会不可言传'的部分”。

具体怎么做？告诉 Al就行。
优先考虑 （prioritize） 我的 tacit knowledge/隐性知识”。

这样的好处是，AI会优先考虑你的隐性意图，而不是死盯着你的显性描述，避免生成一大堆没用的内容。

---


**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2040992284179566660  

**正文**

Agent = Model + Harness？ 
不！它严重低估了实际工程复杂度。
应该是：
Agent = Model + System！

Harness：围绕模型的提示工程、上下文管理、工具调用等"脚手架"。⚠️ 被过度关注，仅占实际工程的30%。
System：完整的产品级系统：认证、多租户、资源隔离、审计、成本管控等。✅ 真正决定产品成败的70%。

三大核心批判
1. 问题域错位：Harness 源于特定场景
Harness 工程的模式（如文件系统内存、Sub Agent 架构）主要来自 Coding Agents 这一特定形态：
· 单用户
· 终端环境
· 本地文件系统
将这些模式推广到通用 Agent 产品会导致系统性失配。

2. 制造本不存在的问题
作者列举 Harness 工程创造的"伪需求"：
· AGENTS.md 文件作为记忆：单用户、无并发、无查询能力；应该用数据库 — 原生支持SQL、访问控制、持久化
· 虚拟化文件系统：用文件抽象包裹数据库，多此一举；应该直接暴露数据库，LLM 写 SQL 比写 bash 更可靠
· 用户级沙箱：隔离成本失控，无法规模化；应该做系统级资源配额与隔离

3. 忽视经典系统工程问题
真正的生产级 Agent 必须解决已存在数十年的工程难题：
· 多租户：50 人团队如何安全共享 Agent？
· 基于角色的访问控制：谁有权触发哪些操作？
· 资源隔离：如何防止单个租户耗尽全量 token 预算？
· 审计日志、审批流、成本管控

这些不是 Harness 层能解决的，所以作者主张新框架：
Agent = Model + System

Harness 工程对 Coding Agent 这一特定场景仍然有效，但不应泛化为通用 Agent 架构的最佳实践。

---


**作者** john kutay（@JohnKutay）  
**貼文連結** https://x.com/JohnKutay/status/2040846889814462776  

**正文**

Agent memory will become a first class citizen in every orgs data estate. Study how to manage it properly:

---


**作者** Sarbjeet Johal（@sarbjeetjohal）  
**貼文連結** https://x.com/sarbjeetjohal/status/2040918361249636452  

**正文**

Language models make the unstructured data computable and Agents create decision checkpoints automatically. A good read 👇🏽 

Our secret to next big leap in systems is the ability to capture the THE CONTEXT GRAPHS!

---


**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2040977451254493399  

**正文**

接下来 Codepilot 也要准备脱离 Claude Code 了

同时上个版本给所有的服务商都加上了 Codeplan 的获取链接

你现在可以直接在 Codepilot 跳转购买各家 Codeplan 了 

---


**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2040981766991949870  

**正文**

现在做内容真的方便。

以前更新网页还得有个什么后台之类的东西。

现在我直接把这个网页数据更新做成了一个 skill 。

我在外面通过飞书连接我的 CodePilot。直接就能更新网站的数据和新闻。 

---


**作者** Howard Lerman（@howard）  
**貼文連結** https://x.com/howard/status/2040924314392994056  

**正文**

"Block is remote-first. Everything we do creates artifacts. 

In a remote-first company where work is already machine-readable, AI can build and maintain that picture continuously"

https://block.xyz/inside/from-hierarchy-to-intelligence

---


**作者** idoubi（@idoubicc）  
**貼文連結** https://x.com/idoubicc/status/2040821048577565144  

**正文**

最近三个月，我用 Claude Code Vibe Coding 了几个项目，非常有意思，写篇文章记录一下。

## WorkAny

[workany.ai](<https://workany.ai/>)

在上一篇文章 [Vibe Coding 一周，我做了个桌面 Agent](<https://idoubi.ai/blog/vibe-coding-workany>) 写到，我第一次尝试全自动 Vibe Coding，发布了我的第一个 Agent 项目 WorkAny。

断断续续在迭代 WorkAny，修复了一些用户反馈的问题，Github 仓库 star 涨到了 1.4k。

![Article Image](<https://pbs.twimg.com/media/HFJx4s8b0AAAGJV.jpg>)

WorkAny 最初的版本基于 Claude Agent SDK 实现 Agent Runtime，依赖本地的 Claude Code，任务处理比较慢，还经常遇到一些模型不兼容的问题。

最近一段时间尝试了接入 DeepAgents、Pi 作为 Claude Agent SDK 的替代方案，效果始终不太理想，需要定制的工具很多，不能做到像 Claude Agent SDK 一样开箱即用。

这周把 WorkAny 的 Agent Runtime 换成了自己写的 Open Agent SDK，运行流畅了，好多问题也解决了。

## WorkAny Bot

[workany.bot](<https://workany.bot/>)

2 月份的时候，OpenClaw 特别火，掀起了全民养虾热潮，主要的需求和痛点是：

- 大家都在玩，很好奇，我也想试试
- 不敢在自己电脑跑，担心隐私和安全风险
- 不懂技术，搞不了虚拟机，折腾不来云服务器
- 希望长时间待机，但没预算，不想买 Mac Mini
- 不想学怎么配模型、Skills，只想开箱即用

我花了一个周末的时间，发布了 WorkAny Bot，提供 OpenClaw 云端托管服务。

用户不需要关心技术，只需要点几下 \`Next\`，付费开通服务，马上得到一个 \`xxx.workany.bot\` 地址，打开就能看到 OpenClaw 的页面，接入到自己的 im 软件，开始养虾。

![Article Image](<https://pbs.twimg.com/media/HFJyAZmaYAE2bwp.jpg>)

WorkAny Bot 给不想自己折腾的用户提供了便利，让部分人快速用上了 OpenClaw。但在使用过程中，体验还是比不上在自己电脑上部署 OpenClaw。

云端的 Bot 在浏览器自动化、配置工具、定时任务等方面有很多限制，使用起来不够流畅。

## ClawHost

[clawhost.me](<https://clawhost.me/>)

我把 WorkAny Bot 背后的 OpenClaw 托管方案整理出来开源了。

这套方案的核心依赖 K8S 集群，在每个 Pod 部署一个 OpenClaw 实例，通过 PVC 挂载磁盘，对 .openclaw 目录进行持久化存储。

![Article Image](<https://pbs.twimg.com/media/HFJyFH4bwAAbsza.jpg>)

ClawHost 提供一个简单的管理面板，管理员创建 App 和 Bot，对外提供 Restful API，第三方 App 通过 API 创建 Bot 和管理 Bot 内配置。

![Article Image](<https://pbs.twimg.com/media/HFJyHj6bEAANROc.jpg>)

熟悉 K8S 运维的人可以使用这个方案，做自己的 OpenClaw 托管服务。企业可以私有化部署，挂载内部 Skills，为员工统一配置企业版龙虾。

## ChatClaw

[chatclaw.im](<https://chatclaw.im/>)

我觉得 OpenClaw 自带的 Web UI 有点丑。

功能很多，配置很杂，改起来很麻烦。而且对话的体验很不好。

![Article Image](<https://pbs.twimg.com/media/HFJyKLnaMAAzihy.jpg>)

于是我开源了 ChatClaw，一个基于 OpenClaw 的 Web UI，提供更美观的界面和更流畅的对话体验，主打多 Agent 协同对话/工作。

最近 OPC（一人公司） 很火，ChatClaw 从 OPC 的角度设计了整体架构：

OPC -> Companies -> Teams -> Agents -> Tasks

一个 OPC 可以创建多个公司，每个公司对应一个 OpenClaw Gateway，可以是本地的，也可以是云端的（比如：WorkAny Bot）。

![Article Image](<https://pbs.twimg.com/media/HFJyMcLb0AA169k.jpg>)

ChatClaw 的本质是一个 Web UI，只做界面交互，不做业务逻辑。依赖的是 OpenClaw 提供的 Agent Runtime，相当于给你的龙虾换个壳子。前提是，你得有自己的 OpenClaw。

## CoRich

1 月份的时候，我想做一个开源版本的桌面 Agent，对标 Cowork。

想了好几个产品名，其中一个是 CoRich，另一个是 WorkAny，后来选了 WorkAny 作为产品名，CoRich 这个名字就闲置了。

最近 Slack 被爆出批量删除中国团队账户，不允许中国公司使用了。

然后我就很想做个 Agent 版本的 Slack，让人与 AI 可以协同工作，共同完成任务。

我选择了 CoRich 做这个产品的名字，让 Claude Code 快速搭了一个架子，布局参考 Slack，允许创建多个 Workspace，邀请人类员工、创建 Agent 员工，在不同的 Channel 下对话或做任务。

这个产品的交互跟 ChatClaw 有点像，不同的点在于 ChatClaw 是基于 OpenClaw 的 Web UI，依赖 OpenClaw 作为 Agent Runtime，主要是给个人使用，不适合多人协作。

CoRich 跟 ChatClaw 的架构类似，把 Companies 换成了 Workspaces，同样支持 Agents、Teams、Tasks，区别在于 CoRich 允许邀请人类员工加入 Workspace，支持多人 + 多 Agent 协作。

![Article Image](<https://pbs.twimg.com/media/HFJyQRXacAA0pIl.jpg>)

目前，CoRich 还属于 Demo 阶段，还需要点时间完善基本功能。

## FastClaw

[fastclaw.ai](<https://fastclaw.ai/>)

我做了近两个月的 OpenClaw 托管服务，部署在阿里云国际站的 K8S 集群上，一个月接近 5k 美金的部署成本。

我分析了一下，部署成本高的原因主要有几点：

- OpenClaw 是单租户架构，我需要为每个用户单独用一个 Pod 隔离部署，挂载独立的存储空间
- OpenClaw 需要至少 1G 的运行内存，在 K8S 部署，每个 Pod 的 memory\_limit 不能低于 4G，不然很容易 OOM
- OpenClaw 针对一些复杂类任务（比如：写代码），会开独立的子进程去执行，进程开销很大。
- OpenClaw 启动依赖网关初始化、插件加载等多个串行步骤，从启动到可用需要 15-30 秒，没办法做到秒级启动。如果要保证用户云端的 Bot 一直在线，Pod 需要常驻，对于不经常使用的 Bot，是一种资源浪费

所以我得出的结论是，OpenClaw 是针对个人使用场景设计的助理类 Agent，不适合云端部署的多租户场景。上面提到的 CoRich 这种需要多人协作的产品，用 OpenClaw 做底层的 Agent Runtime 肯定不行。

于是我决定自己做一个 Agent 底层框架（操作系统）。

我开源了 FastClaw，定位是一个更好的 OpenClaw-Like Agent OS。

- 使用 Go 实现，单二进制分发（5MB），运行零依赖，秒级启动
- 运行时内存占用 ~20M，约为 OpenClaw 内存占用的 1/7
- 约 3000 行代码实现 OpenClaw 的核心功能，二次开发更简单
- 以 RPC 进程通信的方式运行插件，隔离风险，插件挂了不影响主进程，解决 OpenClaw Gateway 容易挂的问题
- 引入数据库实现持久化存储，用户会话隔离，天然适用云原生多租户部署场景
- 可视化引导安装，上手门槛更低。管理后台 Web UI 更清晰、操作更友好

![Article Image](<https://pbs.twimg.com/media/HFJyUlFa4AA8CaK.jpg>)

除了架构方面的优化和对云端多租户场景的适配，FastClaw 选择尽可能兼容 OpenClaw 的协议和生态：

- fastclaw.json 配置文件，采用跟 openclaw.json 一样的数据结构
- 支持 OpenClaw 的 plugins，支持 ClawHub 的 skills 等
- 跟 OpenClaw 类似的方式实现 memory、context、tools 等核心功能

目前的情况是，FastClaw 堆了很多功能，但是还没来得及完整测试。

有来自社区的开发者贡献了几个 FastClaw 插件，还没来得及整合，还需要时间打磨功能、发展生态。

## WeClaw

[weclaw.im](<https://weclaw.im/>)

半个月前，一向封闭的微信开放了 ClawBot 一级入口，允许用户接入自己的 OpenClaw，在微信 ClawBot 对话使用。

微信官方发布了一个 weixin-openclaw 插件，用户在电脑上运行这个插件，扫码登录后，可以连接电脑上的 OpenClaw。

我的工作电脑上没有安装 OpenClaw，但是我想通过微信 ClawBot 连接我电脑上的 Claude Code 做任务。

于是我开源了 WeClaw，定位是连接微信 ClawBot 与桌面 Agent 的桥接器。

在电脑上运行 weclaw 后，weclaw 自动探测到电脑上安装的 Agent，比如 Claude Code / Codex / Gemini / OpenClaw 等，再通过 ACP / CLI / HTTP 三种方式，与 Agent 实现连接。

用户可以在微信 ClawBot 通过自定义指令切换 Agent 对话，可以把消息同时发给多个 Agent。

![Article Image](<https://pbs.twimg.com/media/HFJyYQdbUAA2_vD.jpg>)

有个高频使用 weclaw 的朋友给我看了他的一个工作流，挺有意思的：

在微信 ClawBot 语音输入内容 -> 微信自动转文字 -> 发给电脑上的 weclaw -> weclaw 转发给电脑上的 Claude Code -> Claude Code 根据输入内容，提取关键信息 -> Claude Code 调用 Skills，把结构化内容输出到第三方软件

![Article Image](<https://pbs.twimg.com/media/HFJyaDhasAAN-NU.jpg>)

WeClaw 这个项目的价值在于，你可以在微信 ClawBot 连接任何你常用的 Agent，定制指令实现自定义工作流。

## AnyClaw

[anyclaw.tools](<https://anyclaw.tools/>)

有了 WeClaw 之后，我日常会通过微信 ClawBot 查很多信息，做很多任务。

只靠大模型的能力，很多任务实际上是不太容易完成的。

为了补充大模型挂载外部信息的能力，这两年出来了很多解决方案，比如 RAG / MCP / Skills 等。

Skills 的解决方案是写一堆 Markdown 文档加一些脚本，让 Agent 渐进式读取提示词，在合适的时机调用合适的技能，辅助大模型完成任务。

Skills 比起 MCP 是一个很大的创新，不需要把一堆工具在每次对话都塞进模型上下文，节约了 Token。

后面大家发现，用命令行工具，可以进一步优化上下文，因为命令行工具 --help 输出的信息，能告知模型可用的工具列表，还不需要传递额外的描述内容。

于是，很多厂商又从开放 Skills 转成了开放 CLI 工具。

我开源了 AnyClaw，定位是给 Agent 用的技能补充包。

这个项目主要想做三件事：

- 做转换器。把互联网上的 OpenAPI Schema / 自定义的脚本、Pipeline / 网站 / 桌面 App 等，一键转换成 CLI 工具
- 做扩展坞。输入是 CLI，输出是 MCP / Skills，让不同类型的 Agent 都能理解工具，在合适的时机自动发现并调用工具
- 做工具箱。把常用的工具收集起来，放到工具箱，让 Agent 可以搜索、安装、调用工具

比如我针对域名搜索场景写了个 \`query-domains\` 工具，通过 anyclaw 命令三步调用：

> anyclaw search domain
> anyclaw install query-domains
> anyclaw query-domains search "workany.ai"

![Article Image](<https://pbs.twimg.com/media/HFJygUsbMAAutH-.jpg>)

除了 anyclaw 内置的工具，你还可以添加第三方仓库提供的工具，比如：

> anyclaw repo add https://github.com/larksuite/cli --name feishu-cli
> anyclaw repo update
> anyclaw search docs --repo feishu-cli

把 AnyClaw 自身的 SKILL.md 发给 Claude Code，然后就可以通过 WeClaw 给 Claude Code 发消息，调用 AnyClaw 内置的工具查信息了。

![Article Image](<https://pbs.twimg.com/media/HFJykbBboAA632I.jpg>)

AnyClaw 目前对于工具的编写、转换、导入等功能已经比较完整了。工具箱内置的工具还比较少，还需要时间积累，也需要发展生态，通过社区的力量集成更多的工具。

## ClawRouter

我去年做过一段时间 MCPRouter，把一些流行的 MCP 服务器托管起来，整合下游服务的 API Key，再对上游提供统一的接入和计费。

用了一段时间 OpenClaw 之后，我发现要让自己的龙虾做更多的事情，比如画图、生成音乐等，需要给龙虾配置各种工具，但是我又不想去各个提供工具的服务商平台申请 API Key 和绑卡充值。

于是我把 MCPRouter 改成了 ClawRouter，把之前托管的 MCP 服务器平移了过来，后面还想接入模型、Skills，以及 AnyClaw 整合的 CLI 工具。

ClawRouter 的定位是 Tools 版本的 OpenRouter。

![Article Image](<https://pbs.twimg.com/media/HFJymvzagAEFXsW.jpg>)

目前 ClawRouter 整合的工具还不够多，还在内部测试，没有发布上线。

## Clawork

玩过一段时间 MoltBook，Agent 自由社交，非常前沿。有人觉得 Web 4.0 要来了，Agent 互联网已开启。

于是我在想，既然 Agent 能自由社交，Agent 是不是也可以自由交易。

我给我的 Agent 配置了最贵的模型和最好的工具，我的 Agent 能够高效完成各类复杂的任务，但是我的成本消耗也很大。

如果我的 Agent 可以在网上接单，帮助其他人实现他们的一些需求，是不是既创造了价值，又能赚到钱，帮助我平摊成本。

于是我做了 Clawork，定位是 Agent 众包平台。可以由人类，或者人类的 Agent 在平台上发布任务，设置预算。

其他人的 Agent 可以通过接口发现任务，竞标做任务，完成任务后可以获得对应的 Token 报酬。

人类在平台提现，把 Agent 赚到的 Token 换成现金提取出来。

Clawork 可以先做成 Agent 版本的 Upwork，走竞标模式。后面可以往 Agent 版本的 Uber 方向发展，做平台派单模式。

有交易的平台，就会有很大的商业价值。我很看好这个方向，但是又感觉有点太超前，不太容易落地。

![Article Image](<https://pbs.twimg.com/media/HFJyp9JaEAE2MBv.jpg>)

Clawork 初期的核心功能已经完成，本地测试跑通了完整的双边交易流程，但是还有一些问题没有想明白，所以还没有发布上线。

## ClawBaby

最近一段时间看到了很多有意思的桌宠项目，有的跑在 Dock 栏上，有的跑在刘海屏上，还有的在桌面上跑来跑去。

最近 Claude Code 推出了一个 \`/buddy\` 指令，可以在 Claude Code 对话框添加一个桌宠。

我让 Claude Code 给我写了两个版本，一个版本用 tauri 写的，让一个龙虾头像在桌面游走，监听 Agent 在做的任务，做实时互动。另一个版本用 Swift 写的，跑在 Mac 的刘海屏，可以投喂、互动，就像是在玩宠物养成游戏。

![Article Image](<https://pbs.twimg.com/media/HFJysNsaIAAUT0L.jpg>)

单纯觉得这类项目好玩，谈不上多有价值，反正也不需要我花什么时间，顺手就让 Claude Code 做了。😄

## Open Agent SDK

本周 AI 行业有个大事件，Claude Code 源码泄露了。

Twitter 上有一波人用 AI 去分析 Claude Code 的源码，再写成解读文章，拿到了很多流量。

另一波人选择在 Claude Code 源码基础上补齐工具链，做成可直接运行的开源版 Claude Code，吸引了很多关注。

我选择了在 Claude Code 源码基础上，抽出来一个 SDK，用于替换 Claude Agent SDK

使用 claude-agent-sdk 做过 Agent 产品的都知道，其本质是在 claude code 的基础上套了一层壳，做成 sdk 给第三方接入，可以加速 Agent 产品的开发，但是弊端也很明显：

- claude-agent-sdk 依赖 claude code，而 claude code 是不开源的，一切都是黑盒调用，出了问题你没法修
- claude-agent-sdk 接到的 query，需要创建 claude code 进程去处理，开销很大，不适合云端规模化调用

我让 Claude Code 分析了一遍 claude-code-sourcemap 源码，把逻辑全部抽离出来，写了个 open-agent-sdk：

- 完全兼容 claude-agent-sdk 的接口形式，只需换个包名即可快速替换
- 完全开源，你可以接入到你的 Agent 后做定制化修改，不再是黑盒调用
- 函数调用，不依赖本地 cli 进程，没有额外的开销，云端 Agent 高并发不愁

使用 open-agent-sdk 的一个调用示例：

> 帖子发出去之后，反响特别好，拿到了 321k 访问，Github 仓库一周涨了 2k star，真神奇。

![Article Image](<https://pbs.twimg.com/media/HFJxe_0agAAgh5_.jpg>)

我让 Claude Code 参考 open-agent-sdk-typescript，实现了 go / rust / python 三个语言的版本，一共开源了四个语言版本的 open-agent-sdk

然后我又让 Claude Code 修改 WorkAny 的源码，引入 open-agent-sdk-typescipt，替换掉原来依赖的 claude-agent-sdk

在 WorkAny 跑了几个任务，响应很快，效果很好。用自己的 SDK 实现了 Agent Runtime 功能，不再依赖 Claude Code，哪里不爽改哪里。

## CodeAny

[codeany.ai](<https://codeany.ai/>)

泄露出来的 Claude Code 源码有近 50 万行代码，除了 Agent 运行逻辑，还有很多周边代码值得学习和研究。

我让 Claude Code 继续扫描 claude-code-sourcemap 仓库，把 cli 和 UI 部分的逻辑抽离出来，用 go 重写，做一个新的终端 Agent：CodeAny

在 CodeAny 引入了 open-agent-sdk-go 作为 Agent Runtime

经过多次的扫描、测试、补齐功能，CodeAny 基本复刻了 Claude Code 的核心功能，实现了 Claude Code 的大部分指令。

在 CodeAny 接入 OpenRouter 上的 xiaomi-mimo 模型，响应速度非常快，跑了几个任务，效果还不错。

![Article Image](<https://pbs.twimg.com/media/HFJxarVbIAAuGp0.jpg>)

比起 Claude Code，CodeAny 的运行速度更快，内存占用更低，而且完全开源，可以定制功能。继续迭代，也许能逐步替代掉 Claude Code，作为日常使用的 Coding 工具。

## CCOnline

既然拿到了 Claude Code 的源码，我在想，能不能跟托管 OpenClaw 一样，我也搞一个托管 Claude Code 的服务？

于是我做了 CCOnline，定位是一个跑在云端的 Claude Code，内置模型 + Skills，帮助用户完成一些日常的任务。

跟 ClawHost 的托管方案不一样，我尝试用 e2b 来做隔离容器，每个用户分配一个默认的 Workspace，每个 Workspace 对应一个 e2b 容器，用户的项目文件通过对象存储挂载。

比起 K8S Pod 的隔离方案，e2b 隔离性更好，毫秒级启动，无需常驻，运维方便。也许成本会比用 K8S Pod 的方案低。

![Article Image](<https://pbs.twimg.com/media/HFJxTupaEAAhnMW.jpg>)

CCOnline 目前还在技术实验阶段，我没想明白纯云端的 Claude Code 有什么价值，目标群体和使用场景分别是什么。

## 总结

用一个表格整理了以上提到的几个项目👇

![Article Image](<https://pbs.twimg.com/media/HFJyzMqaIAEHezn.png>)

这些项目全部由 Claude Code 完成，我负责提需求、测试、再提需求，未参与过代码编写工作，总体投入时间不多。

我甚至很少打开编辑器，很多时候是走在路上，灵感来了，拿出手机，通过 Discord 把想法发给 OpenClaw，让 OpenClaw 调用 Claude Code 去实现。

等有时间打开电脑，我再去验收一下，有不满意的地方，再发消息给 OpenClaw 让他指挥 Claude Code 去修改。

全自动 Vibe Coding 近三个月，我有几点很深的感触：

1.我的编程习惯彻底被颠覆了，角色定位也发生了很大的变化。我不再把自己当做一个程序员，而是项目经理 + 系统架构师 + 测试工程师。

2. AI 治好了我的强迫症和代码洁癖，我不再关注代码，只关注实现的功能完整性。

3. AI 变得智能了，我的效率更高了，但是注意力更加不集中了。同时开很多个窗口做不同的项目，没有把哪个项目做得特别好

4.测试资源极度缺乏，AI 做得很快，但是我没有足够的时间去验收，也不知道功能完不完整，有没有什么 bug

5.用 AI 复刻一个项目变得极度容易，我不明白这个时代产品的护城河在哪里

6.技术落地的能力差异被 AI 彻底抹平，擅长搞流量和商业变现的能力变得极其重要

7.知识面的广度和架构设计能力，是这个时代重要且稀缺的能力

8.我时常感到迷茫，不知道做这些所谓“产品”的意义在哪里

也许控制注意力，在一个方向持续做深，才是正确的事情。

> Attention is all you need.

---


**作者** Geek Lite（@QingQ77）  
**貼文連結** https://x.com/QingQ77/status/2040709023058583774  

**正文**

驾驭工程：从 Claude Code 源码到 AI 编码最佳实践

中文别名：《马书》

这是一本围绕 Harness Engineering（驾驭工程）的中文技术书。它以 Claude Code v2.1.88 的公开发布包与 source map 还原结果为分析材料，不试图复刻官方产品文档，而是从真实工程实现中提炼 AI 编码 Agent 的架构模式、上下文策略、权限体系和生产实践。

https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding

---


**作者** Kirk Marple（@KirkMarple）  
**貼文連結** https://x.com/KirkMarple/status/2040984714073522432  

**正文**

We've been heads-down this last month adding a brand-new Agents service to @dossium.

On top of our existing, unified content layer - you can now can run channel-bound agents, as well as scheduled or triggered agents, using both internal and external context.

In addition, we've built a unique canvas to view your agentic runs, and see the prompts, responses and tool calling your agents are performing.

---


**作者** Aruni Design（@arunidesign）  
**貼文連結** https://x.com/arunidesign/status/2040485573329117473  

**正文**

your landing page doesn't need:
- bento boxes
- feature
- benefits
- social proof
- how it works
- pricing
- faq

your landing page needs storytelling. 

---


**作者** 九原客（@9hills）  
**貼文連結** https://x.com/9hills/status/2040985341889483167  

**正文**

这两天研究了下 Multi-agent workflow，感觉确实可行，要不然也不会跑出来这么多。 

---


**作者** 关木（@ZeroZ_JQ）  
**貼文連結** https://x.com/ZeroZ_JQ/status/2040719922071056515  

**正文**

superpower 和 gstack 还没玩够

又来个 Google 大佬的最佳实践。

学不动了

---


**作者** Matt Epstein（@MattEpstein16）  
**貼文連結** https://x.com/MattEpstein16/status/2040951763964944404  

**正文**

Actually fucked that this is free 

---


**作者** Cell 细胞（@cellinlab）  
**貼文連結** https://x.com/cellinlab/status/2040428719206998507  

**正文**

从布达佩斯到曼彻斯特：一位通才的生命轨迹
迈克尔·波兰尼（Michael Polanyi，1891—1976）生于布达佩斯一个智识氛围浓厚的匈牙利家庭。这个家族的学术传统堪称传奇——兄长卡尔·波兰尼（Karl

---


**作者** 小龙先生（@Dragonhau66）  
**貼文連結** https://x.com/Dragonhau66/status/2040908981443465394  

**正文**

周末快乐一刻：这绝对是撩妹高手！我边看边笑，佩服这帅锅！绝了！

中国小伙线上视频撩妹，把土耳其的美女撩到心花怒放，他不但语言魅力发挥出色，而且还能即兴表演唱歌，这把土耳其美女撩到恨不得立即飞到中国与其相恋！想谈恋爱的兄弟们，你学废了吗？ 

---


**作者** Jaden思考日志（@Jaden_riku）  
**貼文連結** https://x.com/Jaden_riku/status/2040787307117330661  

**正文**

看到这篇文章，我知道在AI时代，和维特根斯坦同样重量级的人物再次被挖掘到了。

接下来的步骤是阅读ta的著作，拷贝现存资源的pdf，喂给claude code，并且加入自己的skill以及顾问团队，然后赶紧用于自己的产品和商业模式。

---


**作者** vizionaryfocus（@vizionaryfocuss）  
**貼文連結** https://x.com/vizionaryfocuss/status/2040806333260181518  

**正文**

let me tell you what most reps do to "prepare" for a sales call. they look at the name. maybe they glance at the typeform answers. and then they hop on and wing it. 
this is why close rates are

---


**作者** 出海去孵化器（@chuhaiqu）  
**貼文連結** https://x.com/chuhaiqu/status/2040395965870620968  

**正文**

未来真正值钱的是只有你才能获取的独家数据。

Podscan 的例子很典型，它的价值不在于解析 RSS 订阅源，也不在于 API 有多快，这些任何 AI 都能复制。真正的价值在于转录了 5000 万集播客，这些数据是 AI 靠算力无法凭空生成的。

人类生成的数据价值在不断飙升。

另外，在 AI 时代一定要让产品的数据可触达。让用户和 AI 智能体都能方便地调用你的数据，而不是只裹在界面里。

---


**作者** Venkat（@venkatofl）  
**貼文連結** https://x.com/venkatofl/status/2040515025153253425  

**正文**

it’s setup + discipline.
if your emails are going to spam, start here:
first, authentication.
spf, dkim, and dmarc are not optional. they tell inbox providers that you are a legitimate sender.
spf

---


**作者** Archive（@ArchiveExplorer）  
**貼文連結** https://x.com/ArchiveExplorer/status/2040727747966668939  

**正文**

"Claude usage limit reached. Your limit will reset at 7pm"

every. fucking. day.

was about to pay $200 for Max. then I read this article

98.5% of tokens - wasted

you're not paying for answers. you're paying for Claude to re-read its own homework 30 times

spent months blaming Anthropic for being greedy. turns out the problem was how I write prompts

5 minutes of reading

basic plan now handles more than my old Max

---


**作者** Artem Zhutov（@ArtemXTech）  
**貼文連結** https://x.com/ArtemXTech/status/2040972026425319439  

**正文**

90% of people listen to experts and never change a single behavior. They always stay in learn mode.
You open a bunch of tabs. You find videos, articles, podcasts. The context is scattered. At some

---


**作者** Chang Chen（@ChangChen_CC）  
**貼文連結** https://x.com/ChangChen_CC/status/2040956971478884577  

**正文**

What do you do when users can't find your product? 

@SimularAI  was in exactly that position. An AI agent that operates Mac, Windows, and browsers the way a human would. 

But nobody searches for "computer-use AI agent." They search for specific tasks:  "How to sync data between Notion and Sheets."  "How to auto-publish YouTube videos."  "How to automate my spreadsheet workflows." 

Here's what we did: 

Instead of chasing product keywords, we mapped every workflow Simular could replace. 

We built a programmatic content engine — hundreds of workflow-specific pages, each one genuinely useful. Not a product pitch disguised as a tutorial. Teach the workflow first, then show how Sai works like a human on your computer proactively.

565 pages published in 90 days, all through a CMS-driven pipeline. All organic. Zero ad spend. 

The results in one quarter: 
5.6M total organic impressions  
750+ pages ranking on Google page 1  Weekly impressions up 104%  
Daily clicks up 170%  
86% of published pages on page 1 

In 90 days，from negligible organic presence to one of the most visible AI agent brands in Google search. 

When your product is ahead of what users know to search for, chasing keywords won't work. You need to show up inside the workflows your users are already living — deliver real value there, then lead them to your product. 

As Simular CEO @angli_ai  put it: "That's not just SEO — that's a distribution moat."

---


**作者** Dimitar Angelov（@dimitarangg）  
**貼文連結** https://x.com/dimitarangg/status/2040822212534423679  

**正文**

i've been doing cold outreach for years now. booked 1,000s of calls. tested 1,000,000+ angles. burned through 5 millions sends. made every mistake possible
here's everything i've learned condensed

---


**作者** Khe Hy（@khemaridh）  
**貼文連結** https://x.com/khemaridh/status/2041014178098647402  

**正文**

Meet the new triple threat.
First we had the dynamic duo of the Claude Excel Plug-in.
Then Anthropic trained its sights on PowerPoint.
But there was a problem. These sessions worked in isolation.
So

---


**作者** MindBranches（@MindBranches）  
**貼文連結** https://x.com/MindBranches/status/2040938261946782016  

**正文**

“Fighting the mind does not work. What works best is learning to focus it.”
~W. Timothy Gallwey

Book Summary: The Inner Game of Tennis: The Classic Guide to Peak Performance 

---


**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2040471456820408449  

**正文**

karpathy 针对他这个 AI 知识库方案给了个更详细的版本

https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f 

---


**作者** 阿绎 AYi（@AYi_AInotes）  
**貼文連結** https://x.com/AYi_AInotes/status/2040974902149419406  

**正文**

有个很强烈的预感，
 AI 百花齐放的奇点即将到来！！！

karpathy 大佬的 wiki pattern被
@FarzaTV 做成 skillgithub 开源了，
忘记放链接，
https://gist.github.com/farzaa/c35ac0cfbeb957788650e36aabea836d
Farza 老哥的知识库地址：
https://farza.com/knowledge 

---


**作者** Bilgin Ibryam（@bibryam）  
**貼文連結** https://x.com/bibryam/status/2040898048264486922  

**正文**

🌟12 Agentic Harness Patterns from Claude Code🌟
https://generativeprogrammer.com/p/12-agentic-harness-patterns-from 

---


**作者** Jayden Wei | OGBC Group（@JaydenWei）  
**貼文連結** https://x.com/JaydenWei/status/2040788056152875343  

**正文**

理解越来越多美国的大佬把family office设立在新加坡的原因了。

---


**作者** 凡人小北（@frxiaobei）  
**貼文連結** https://x.com/frxiaobei/status/2040975049403113625  

**正文**

卖工具的怕被模型替代，卖结果的越来越强。

红杉这篇讲透了 AI 服务化的逻辑：
从外包业务切入，先吃智力型工作，再扩到判断型。2025 是 Copilot 年，2026 是 Autopilot 年。
https://sequoiacap.com/article/services-the-new-software/

---


**作者** aacash.eth - Aakash Kumar（@RTinkslinger）  
**貼文連結** https://x.com/RTinkslinger/status/2040718662718644463  

**正文**

The context substrate for system of agents has to be graphs they can traverse efficiently and effectively! Multiple ways to bell the cat, this is surely one.

---


**作者** Ksenia_TuringPost（@TheTuringPost）  
**貼文連結** https://x.com/TheTuringPost/status/2040850276735709684  

**正文**

Institutional redesign, step by step: how companies actually become ready for AI
Spend a few days in San Francisco right now and you will start believing that AI has already taken over everything. The

---

