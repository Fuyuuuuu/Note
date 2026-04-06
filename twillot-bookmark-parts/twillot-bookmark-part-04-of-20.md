# Twillot 書籤（精簡）— 第 4/20 部

原檔：`twillot-bookmark.md` · 全檔共 3930 則 · **本部第 590–786 則**（共 197 則）

---

**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2034082485798314489  

**正文**

Claude Code 创建者写的如何使用和创建 Skills 

如果你还不了解的话，强烈推荐看看！

Anthropic 内部现在有数百个 Skills 在用，从 API 文档到部署流程全覆盖。他们把这些经验总结出来了。

做个笔记📒：

======

Skills 不只是 Markdown 文件

很多人以为 Skills 就是写个 Markdown 文档，其实不是。Skills 是一个文件夹，里面可以放脚本、资源文件、数据，甚至注册钩子函数。

代理可以发现这些内容，读取它们，执行脚本，在特定时机触发钩子。这才是 Skills 最有意思的地方。

最好的 Skills 都在创造性地使用这些配置选项和文件夹结构。

======

九种 Skills 类型

Anthropic 把内部的 Skills 整理了一遍，发现它们基本归为九类。好的 Skills 能明确归入一类，混乱的 Skills 往往跨了好几类。

------

1. 库与 API 参考

解释怎么用某个库、CLI 或 SDK。可以是内部库，也可以是 Claude 经常搞错的常用库。

通常包含一个代码片段文件夹，加上一份"别踩这些坑"的清单。

比如：
▸ billing-lib — 你们内部计费库的边界情况和常见坑
▸ internal-platform-cli — 内部 CLI 的每个子命令和使用场景
▸ frontend-design — 让 Claude 更懂你们的设计系统

------

2. 产品验证

描述怎么测试或验证代码是否正常工作。通常配合 Playwright、tmux 这些工具。

验证 Skills 极其重要，值得让工程师花一周时间专门打磨。

可以让 Claude 录制测试视频，或者在每一步强制执行程序化断言。这些通常通过在 Skill 里放各种脚本实现。

比如：
▸ signup-flow-driver — 在无头浏览器里跑注册流程，每步都有状态断言钩子
▸ checkout-verifier — 用 Stripe 测试卡驱动结账界面，验证发票状态
▸ tmux-cli-driver — 测试需要 TTY 的交互式命令行工具

------

3. 数据获取与分析

连接你的数据和监控栈。可能包含带凭据的数据获取库、仪表盘 ID、常见工作流说明。

比如：
▸ datadog-metrics — 预设的仪表盘链接和常用查询
▸ postgres-query-helper — 连接生产数据库的只读凭据和常用查询模板
▸ user-analytics — 获取用户行为数据的脚本和分析模板

------

4. 业务自动化

自动化重复的业务流程。比如创建 Jira ticket、发 Slack 通知、更新文档。

这类 Skills 通常包含调用内部 API 的脚本，加上业务流程的说明。

比如：
▸ incident-reporter — 创建事故报告并通知相关人员
▸ release-notes-generator — 从 Git 提交生成发布说明
▸ onboarding-automation — 新员工入职的自动化流程

------

5. 代码脚手架

生成项目或组件的初始代码结构。包含模板文件和生成脚本。

比如：
▸ react-component-scaffold — 生成符合团队规范的 React 组件
▸ api-endpoint-generator — 生成 API 端点的样板代码和测试
▸ microservice-template — 创建新微服务的完整结构

------

6. 代码质量与审查

帮助审查代码质量、安全性、性能。可能包含 linter 配置、审查清单、自动化检查脚本。

比如：
▸ security-review — 安全审查清单和常见漏洞检查
▸ performance-profiler — 性能分析工具和优化建议
▸ code-review-checklist — 代码审查的标准流程

------

7. CI/CD 与部署

管理持续集成和部署流程。包含部署脚本、环境配置、回滚流程。

比如：
▸ deploy-to-staging — 部署到测试环境的完整流程
▸ rollback-helper — 快速回滚的脚本和检查清单
▸ ci-debugger — 调试 CI 失败的常用方法

------

8. 运行手册

处理生产环境问题的操作指南。通常是"如果 X 发生了，做 Y"的格式。

这类 Skills 在紧急情况下特别有用，因为它们把经验固化成了可执行的步骤。

比如：
▸ database-recovery — 数据库故障恢复流程
▸ traffic-spike-handler — 流量激增时的应对措施
▸ memory-leak-debugger — 内存泄漏排查步骤

------

9. 基础设施运维

管理云资源、容器、网络配置。包含 Terraform 脚本、Kubernetes 配置、监控设置。

比如：
▸ aws-resource-manager — 管理 AWS 资源的脚本和最佳实践
▸ k8s-troubleshooter — Kubernetes 常见问题排查
▸ terraform-helper — Terraform 模块和使用指南

======

写好 Skills 的最佳实践

Anthropic 总结了一些实用的技巧，都是从实际使用中提炼出来的。

------

写明 Gotchas

把常见错误和陷阱明确列出来。Claude 会认真读这些内容，避免重复犯错。

比如在 API 文档里写："注意：这个端点有速率限制，每秒最多 10 次请求。超过会返回 429 错误。"

------

利用文件系统做渐进式披露

不要把所有信息都塞在一个 Markdown 文件里。用文件夹结构组织内容，让 Claude 按需探索。

比如：
```
my-skill/
  README.md          # 概览和快速开始
  examples/          # 代码示例
  scripts/           # 辅助脚本
  reference/         # 详细文档
  gotchas.md         # 常见陷阱
```

Claude 会先读 README，需要时再深入其他文件。

------

存脚本和辅助库

把可复用的脚本放在 Skill 里，而不是让 Claude 每次都重写。

这些脚本可以是 Python、Bash、Node.js，任何能执行的东西。Claude 可以直接调用它们，或者读取代码学习怎么用。

------

使用稳定存储做记忆

Skills 可以访问 `${CLAUDE_PLUGIN_DATA}` 目录，这是一个持久化存储位置。

可以用来保存：
▸ 上次运行的状态
▸ 用户偏好设置
▸ 缓存的数据
▸ 历史记录

这样 Skill 就有了"记忆"，可以在多次会话间保持状态。

------

按需钩子保护危险操作

对于可能造成破坏的操作（删除数据、部署到生产环境），使用按需钩子（on-demand hooks）。

这会在执行前弹出确认提示，让用户明确批准。

比如在 Skill 的 frontmatter 里配置：
```yaml
hooks:
  on_demand:
    - name: deploy-to-prod
      command: ./scripts/deploy.sh production
      confirm: "确定要部署到生产环境吗？"
```

------

用 PreToolUse 做度量

可以注册 PreToolUse 钩子来记录 Skill 的使用情况。

这样能知道哪些 Skills 最常用，哪些需要改进，哪些可以下线。

======

分发 Skills

Skills 的一大优势是可以跟团队共享。有两种方式：

------

签入代码仓库

把 Skills 放在 `./.claude/skills` 目录下，跟代码一起提交。

适合小团队，在少数几个仓库间协作。但每个签入的 Skill 都会占用模型的上下文，所以不能无限增加。

------

插件市场

创建一个内部插件市场，让用户上传和安装插件。

适合大团队。用户可以选择安装哪些 Skills，不会污染所有人的上下文。

Anthropic 没有集中式团队管理市场，而是有机地发现有用的 Skills。如果你有个好 Skill，上传到 GitHub 的沙箱文件夹，在 Slack 里分享链接。

如果很多人觉得有用，就会被推广到正式市场。

======

管理市场的实用建议

------

设置沙箱区域

在市场里创建一个"实验性"或"社区贡献"区域，让人们可以自由上传。

好的 Skills 会自然浮现，然后可以移到"官方推荐"区域。

------

鼓励文档和示例

要求每个 Skill 都有清晰的 README 和使用示例。

没有文档的 Skills 很难被采用，即使功能很好。

------

定期清理

定期检查哪些 Skills 没人用，考虑下线或合并。

市场里 Skills 太多会让人不知道选哪个，保持精简很重要。

------

收集反馈

提供简单的方式让用户反馈 Skills 的问题和改进建议。

可以是 GitHub Issues，也可以是 Slack 频道。

======

实际案例

Anthropic 分享了几个他们内部最受欢迎的 Skills：

------

commit-helper

帮助写符合团队规范的 Git 提交信息。

包含提交信息模板、常见类型（feat/fix/docs）的说明、以及检查提交信息格式的脚本。

使用频率极高，因为每个人每天都要提交代码。

------

pr-reviewer

自动化代码审查流程。

会检查代码风格、测试覆盖率、安全问题，生成审查评论。

节省了大量人工审查时间，让审查者可以专注于逻辑和架构问题。

------

incident-response

生产环境事故响应流程。

包含排查清单、常用命令、通知模板、事后总结模板。

在紧急情况下特别有用，因为它把经验固化成了清晰的步骤。

------

api-docs

内部 API 的完整文档和使用示例。

Claude 经常需要调用内部 API，有了这个 Skill 就不用每次都查文档或问人。

------

test-runner

运行测试的标准流程。

包含不同类型测试（单元测试、集成测试、端到端测试）的运行方法，以及如何解读测试结果。

======

Skills 的未来

Anthropic 认为 Skills 会朝几个方向发展：

------

更智能的发现机制

现在 Claude 需要用户明确调用 Skill，未来可能会自动识别场景并推荐相关 Skills。

比如你在写 API 调用代码，Claude 自动建议使用 api-docs Skill。

------

Skills 之间的组合

现在 Skills 基本是独立的，未来可能会支持 Skills 之间的依赖和组合。

比如 deploy-to-prod Skill 可以自动调用 test-runner 和 security-review Skills。

------

动态生成 Skills

根据代码仓库的实际情况，自动生成或更新 Skills。

比如扫描代码库，自动生成 API 文档 Skill。

------

跨团队共享

建立公开的 Skills 市场，让不同公司的团队可以共享通用的 Skills。

比如常用框架（React、Django）的最佳实践 Skills。

======

核心理念

Skills 的本质是把团队的工程实践和领域知识固化成可复用的扩展。

好的 Skills 应该：
▸ 解决真实的重复性问题
▸ 包含清晰的文档和示例
▸ 利用文件夹结构和脚本增强能力
▸ 在需要时提供保护机制
▸ 容易分发和维护

不要为了做 Skill 而做 Skill。从团队的实际痛点出发，把那些每次都要重复的事情固化下来。

一个好的 Skill 能让整个团队的 AI 编程体验提升一个档次。

---

**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2034096899347910800  

**正文**

出门在外也能让 Claude 在电脑上干活

Claude 彻底小龙虾化

Claude Cowork 推出一的一个新功能：Dispatch，用手机远程指挥电脑上的 Claude 干活。

打开 Cowork，找到 Dispatch 选项
扫个二维码，手机就配对上了

然后你电脑只要开着，你就能通过手机操控Cowork，让它去你的电脑里做任何事情...

Dispatch 走的是 Cowork 的底层能力，你电脑上 Claude 能用的一切（本地文件、连接器、插件、浏览器），从手机端都能调用。

能访问你连接的邮箱、网盘、Slack等，还能访问你电脑里的指定的或者所有文件，理论上是可以让它调用各个文件帮你干活。

典型场景包括：

数据处理： 你在外面，想让 Claude 从本地的 Excel 表格里提取数据，整理成摘要报告。发条消息就行，Claude 会访问你电脑上的文件，跑完把结果放好。

信息汇总： 让 Claude 搜你的 Slack 消息和邮件，起草一份简报文档。省得你回到电脑前还得翻半天聊天记录。

文件整理： 指定一个文件夹，让 Claude 按你的规则整理或处理里面的文件。

演示制作： 让 Claude 从 Google Drive 里找素材，拼一份格式化的演示文稿。

---

**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2034111663931330646  

**正文**

我刚看到一个很疯狂的实验。

有人让 Claude 搭建了一个 “上帝视角” 终端：
里面有 56 个实时运行的 AI agents，用来模拟真实世界的市场参与者。

每个 agent 都有记忆、人格和行为模式，
会形成群体、产生意见领袖，并且实时改变观点。 

---

**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2034142845645558151  

**正文**

硅谷最有影响力的产品经理类内容创作者之一，前 Airbnb 增长产品经理

Lenny Rachitsky 将自己的350 篇顶级产品文章 + 300 集播客全部开源

所有人都可以免费下载

这 349 篇文章覆盖了产品管理、增长策略、用户研究、创业方法论等核心话题， 播客嘉宾包括 Spotify、Figma、Notion、Stripe 等公司的产品负责人。

6 年积累下来，已经是产品管理领域最系统的知识库之一，你也可以用它的内容分析他的写作模式、思考模式和产品设计思路等....

---

**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2034053388703285706  

**正文**

breakdown of the episode below

just a simple guide to understanding core ai agent concepts

https://x.com/startupideaspod/status/2033993454653743191?s=20

---

**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2034052610664116550  

**正文**

AI AGENTS 101 (58 minute free masterclass)

send this to anyone who wants to understand ai agents, claude skills, md files, how to get the most out of AI etc in plain english:

1. chat vs agents - chat models answer questions in a back and forth while agents take a goal, figure out the steps, and deliver a result

2. agents don’t stop after one response. they keep running until the task is actually finishedno babysitting required

3. everything runs on a loop. they gather context, decide what to do, take an action, then repeat until done

4. the loop is the system. they look at files, tools, and the internet. decide the next step. execute and then feed that back into the next step. over and over until completion 

5. the model is just one piece. gpt, claude, gemini are the reasoning layer. the key is model + loop + tools + context

6. mcp is how agents use tools. it connects things like browser, code, apis, and your internal software. 

once connected, the agent decides when to use them to get the job done

7. context beats prompt all day. you don't need to write perfect prompts. load your agent with context about your business, style, and goals and then simple instructions work

8. claude.md or agents.md is the onboarding doc

it tells the agent who it is, how to behave, what it knows, and what tools it can use. 

this gets loaded every time before it starts

9. memory.md is how it improves. agents don’t remember by default. this file stores preferences, corrections, and patterns

you tell the agent to update it, and it gets better over time

10. skills + harnesses make it usable. skills are reusable tasks like writing, research, analysis

the harness is the environment like claude code or openclaw that runs everything. basiclaly, different interfaces, same system underneath

this episode with remy on @startupideaspod was one of the clearest ways of understanding a lot of the core concepts of ai agents

could be the best beginners course for ai agents

58 mins. all free. no advertisers. i just want to see you build cool stuff. im rooting for you.

send to a friend

watch

---

**作者** Avid（@Av1dlive）  
**貼文連結** https://x.com/Av1dlive/status/2033948490653700246  

**正文**

this is the next $100B opportunity in ai , most will miss

it's harness engineering

what this agentic engineer reveals is insane

>The model is almost irrelevant. The harness is everything

>every failure is a signal about what the environment needs.

>when agent throughput far exceeds human attention, corrections are cheap and waiting is expensive

most people will ignore and bookmark.

be different.

---

**作者** Tenkara AI（@TenkaraAI）  
**貼文連結** https://x.com/TenkaraAI/status/2033955206715871655  

**正文**

Proud to share that we've raised a $7M round led by
@trueventures 

Read more: https://prnewswire.com/news-releases/ex-shark-tank-founder-and-thiel-fellow-raises-7m-led-by-true-ventures-to-build-ops-agents-for-us-manufacturers-302715467.html 

---

**作者** yazin（@yazins）  
**貼文連結** https://x.com/yazins/status/2033908925733736831  

**正文**

Introducing: OpenGranola 🔥

I built an open source meeting copilot for macOS.

It transcribes both sides of your call on-device, searches your own notes in real time, and hands you talking points right when the conversation needs them. No audio leaves your Mac.

Point it at a folder of markdown files, pick any LLM through OpenRouter (Claude, GPT-4o, Gemini, Llama), and it just works. It's invisible to screen share too — nobody knows you have it.

The whole thing is open source.

Link below

---

**作者** Harrison Chase（@hwchase17）  
**貼文連結** https://x.com/hwchase17/status/2033978553499607160  

**正文**

loved this article by @kishan_dahya 

as we built openswe (fully oss background coding agent) we compared our decisions to the mental model outlined here

try out open swe here: https://github.com/langchain-ai/open-swe 

---

**作者** Andrew Brown（@andrewbrown）  
**貼文連結** https://x.com/andrewbrown/status/2033913290686927245  

**正文**

.@AnthropicAI won't let you sit the Claude Certified Architect exam. But I will over at ExamPro with my equivalent certification because  opportunity should be for everyone. 

---

**作者** vas（@vasuman）  
**貼文連結** https://x.com/vasuman/status/2033972970805162056  

**正文**

> quit your 9-5 job
> type a sentence
> ai builds you a $1m biz
> overnight btw
> successfully exit the permanent underclass

---

**作者** Jaya Gupta（@JayaGup10）  
**貼文連結** https://x.com/JayaGup10/status/2033933615474872708  

**正文**

DM me or @akoratana 

---

**作者** Benjamin Stern（@itsbenjyyy）  
**貼文連結** https://x.com/itsbenjyyy/status/2033957320213004459  

**正文**

Ten years ago I was building factories. Today I'm building the tools I wish I had inside them.

@TenkaraAI  raised $7M led by @trueventures. 

---

**作者** Hanako（@hanakoxbt）  
**貼文連結** https://x.com/hanakoxbt/status/2033624612219576362  

**正文**

i fed Claude 5 PhD formulas and asked him to build me a terminal

he didn't ask questions. he built MiroFish

274 agents. 4 quant formulas running live

each one doing what 87% of polymarket traders can't

every 5 seconds the terminal does this:

> scans polymarket contracts
> runs bayes update on every new signal
> calculates EV against market price
> sizes position through ¼ kelly
> checks KL-divergence across correlated markets for arbitrage

no opinions. no "i feel like YES is underpriced"

just math that PhD students publish and hedge funds lock behind NDAs

here's what happened in 14 days:

> day 2: bayes picked up OSINT chatter on iran negotiations

prior 0.31 → posterior 0.58 in three updates
bot bought YES on "ceasefire by Q3" at $0.33
kelly sized it at 6% of bankroll
contract moved to $0.61 by day 5
+$2,180

> day 6: KL-divergence flagged a gap

"candidate X wins primary" priced at $0.70
"candidate X wins general" priced at $0.48
historical base rate says general should track at ~62% of primary
bot bought general, hedged with primary
convergence hit by day 9
+$3,740

> day 9: EV scanner found a weather contract

market priced hurricane landfall at $0.22
model said 41% based on NOAA data
EV = +$0.86 per dollar risked
kelly said 11% allocation
landfall confirmed day 12
+$4,890

> day 11-14: base rate engine running quiet

fed meeting contract at $0.65 for "hold rates"
base rate: fed holds when unemployment < 4% → 74% of the time
unemployment at 3.8%. market underpriced by 9 points
bought at $0.65. settled at $0.98
+$4,663

total: $15,473 in 14 days

not from predictions. from formulas

87% of polymarket wallets lose money

because they trade what feels right

the top 1.2% trade what the math says

MiroFish doesn't read twitter threads

it reads probability distributions

274 agents don't have opinions

they have bayesian priors

every 15 seconds the NEXUS core sends a pulse to all agents

they recalculate. reposition. repeat

i just watch the profit tick

copy the bot here: http://kreo.app/@1743116

you don't need to be a quant

you need a quant's formulas running 24/7

---

**作者** Aytunc Yildizli（@AytuncYildizli）  
**貼文連結** https://x.com/AytuncYildizli/status/2033813650666885555  

**正文**

8 AI agents sharing one memory system

knowledge graph. episodic recall with decay. ColBERT reranking. lossless context so the window limit stops mattering.

no framework. sqlite, chroma, and stubbornness.

here is my blueprint. 

---

**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2033532696950169992  

**正文**

提前1个月精准预测超级碗冠军
提前3周预测格莱美最大赢家
提前15天成功预测黄金价格走势...

陈天桥 旗下AI 公团队 发布 MiroThinker-1.7 Agent 模型

与GPT等其他模型不同，MiroThinker专注于Agent任务执行，它可以一次研究任务里，最多能连续调用 300 次工具（执行代码、搜索、API调用扥）...

本次共发布了三个版本：

MiroThinker-1.7： 免费开源，研究能力评分 74.0

MiroThinker-1.7-mini： 更轻量的版本，也免费开源，中文研究能力在所有开源模型里排第一

MiroThinker-H1： 最强版本，闭源，研究能力评分 88.2，所有 AI 模型里排名第一

能做什么：

1、全网搜索和信息整合： 它会通过 Google 搜索找到相关网页，然后用 Jina 爬虫抓取页面内容，再用一个小模型把长网页里的关键信息提取出来。不是搜一次就完了，而是会根据搜到的内容决定下一步搜什么，反复迭代。

一个复杂任务可能要搜几十上百轮，模型始终在判断"我还需要找什么信息"。中英文都能搜，中文研究能力在开源模型里目前最强。

2、写代码和运算： 它自带一个代码执行沙盒（E2B），可以直接写 Python 代码跑运算，比如处理数据、做统计分析、画图。这意味着它不只是"说"，还能"算"，遇到需要数据处理的任务不用你手动介入。

3、生成研究报告： 做完整个调研过程后，它会把所有发现整合成一份结构化的深度研究报告，支持在线预览和分享。这不是那种一段话的简单回答，而是一份有章节、有引用、有结论的正式报告。

4、金融分析和预测： 这是 MiroMind 一直主打的方向。模型能综合各种数据源来做资产价格、宏观经济趋势的推理判断。后面会提到它提前15天预测黄金价格，误差只有 0.08%。在金融搜索基准 FinSearchComp 上也拿了最高分。

5、科学研究辅助： H1 在 FrontierScience 系列科学基准上超过了很多闭源大模型，做文献综述、分析实验数据、推导复杂数学问题都能用。

6、事件预测： 体育赛事、颁奖典礼、市场走向，它会综合历史数据和当前信息来做概率判断，这块是强项。

黄金价格预测：2月10日预测2月25日金价 $5,185/盎司，实际结果是 $5,181，差了 $4，误差 0.08%，提前15天。

超级碗冠军：1月6日判断西雅图海鹰队最可能赢，2月8日海鹰队 29-13 击败爱国者队夺冠，提前1个月命中。

格莱美最大赢家：1月8日预测 Kendrick Lamar 将主导2026格莱美，2月1日他拿下5项大奖成为当晚最大赢家，提前3周。

---

**作者** Romàn（@romanbuildsaas）  
**貼文連結** https://x.com/romanbuildsaas/status/2033864046663930201  

**正文**

Today, we’re releasing OpenClaw for outreach.

We gave OpenClaw a LinkedIn account.

It captured high-intent demand and converted it into 12 demos in 7 days.

Salespeople: you’ll never have to worry about booking demos again. 

---

**作者** Idea Browser（@ideabrowser）  
**貼文連結** https://x.com/ideabrowser/status/2033869176675189177  

**正文**

Startup idea that customers are begging to buy right now. 

Open Granola

-Same meeting capture (no bot joining calls)
-macOS Native desktop app
-Notes stored as markdown files. 
-API (not MCP)
-Local-first, or privacy. 
- Agent-readable by default.
-Plays nicely with ai-first tools.

Granola just locked down their local db, went MCP only.

Someone is going to build a more open version and print money.

If you build this...
1. I'll buy it and be your first customer.
2. I'll help you launch and get users.

DM me the link.

---

**作者** Ashutosh Maheshwari（@asmah2107）  
**貼文連結** https://x.com/asmah2107/status/2033734566792356185  

**正文**

Agentic system design concepts I'd master if I wanted to build AI that doesn't blow up in prod.

Bookmark this.

1. Agent Circuit Breaker
2. Blast Radius Limiter
3. Orchestrator vs Choreography
4. Tool Invocation Timeout
5. Confidence Threshold Gate
6. Context Window Checkpointing
7. Idempotent Tool Calls
8. Dead Letter Queue for Agents
9. LLM Gateway Pattern
10. Semantic Caching
11. Human Escalation Protocol
12. Multi-Agent State Sync
13. Replanning Loop
14. Canary Agent Deployment
15. Agentic Observability Tracing

Follow @asmah2107 for a future deep-dive on each.

---

**作者** Orange AI（@oran_ge）  
**貼文連結** https://x.com/oran_ge/status/2033847237550477662  

**正文**

一个月前对 SaaS 软件的评价有点保守了
短短一个月，什么 Notion，Linear 什么的都没人用了
其实新时代的操作系统里已经容不下这些老古董了
就算他们做 CLI 做 MCP 也依然如此
它们最后只是活成了 Claude Code 和 Github 之间的摩擦力

一个月前：AI 是 SaaS 的新主人
一个月后：AI 根本看不上这些老玩意儿

---

**作者** Lennert Jansen（@lennertjansen）  
**貼文連結** https://x.com/lennertjansen/status/2033624374914560125  

**正文**

Today we're launching the Airweave CLI.

Your agent can now ingest, index, and search across 50+ sources. Notion, Slack, Linear, Drive, Gmail, GitHub, Airtable, and more.

Agentic, semantic, and keyword search.

Fully open-source. All from the terminal.

pip install airweave-cli

@airweave_ai

---

**作者** PANews丨APP全面升级（@PANews）  
**貼文連結** https://x.com/PANews/status/2033542222940119374  

**正文**

播客主持人 David Senra 近日与 a16z 联合创始人 Marc Andreessen 进行了一场近 2 小时的深度对话。对话中，Marc 分享了个人习惯、创业哲学和管理方法等。本文对对话精华进行了整理。
来源：David Senra

---

**作者** 向阳乔木（@vista8）  
**貼文連結** https://x.com/vista8/status/2033809142670893208  

**正文**

好友文君和张泓组织 “MindCode 闭门会”（42期）
邀请前Google/YouTube美国产品经理、生产力社区AceMode创始人、湾区中国MBA社区创始人——硅谷大舅 bigjoe

---

**作者** Dan（@aidaniil）  
**貼文連結** https://x.com/aidaniil/status/2033760071046598731  

**正文**

7 days until YC demo day at the landing 

---

**作者** Kshitij Mishra | AI & Tech（@DAIEvolutionHub）  
**貼文連結** https://x.com/DAIEvolutionHub/status/2033545228439986214  

**正文**

And their notes accidentally revealed something interesting.
The exam tests exactly how production AI systems with Claude are built.
Not prompts.
Not chat tricks.
Actual architecture.
After digging

---

**作者** Nathan Baschez（@nbaschez）  
**貼文連結** https://x.com/nbaschez/status/2033736298436219343  

**正文**

I wrote this almost exactly 3 years ago

It's wild how right it is turning out to be https://every.to/divinations/a-new-kind-of-startup-is-coming 

---

**作者** axiaisacat（@axiaisacat）  
**貼文連結** https://x.com/axiaisacat/status/2033709485814858235  

**正文**

很多技术创始人不是不会做产品，
而是死在“没人知道你做了什么”。

刚看到一个 GitHub 仓库 Marketing-for-Founders，

有点像把“0 到 1000 用户”的冷启动打法，直接整理成了开源作战手册。

这个仓库现在大约有 4.7k stars，定位也很直接：帮 SaaS / App / Startup 拿到前 10 / 100 / 1000 个用户。

它最有价值的地方，不是讲那种“大预算做到百万 ARR”的故事，

而是专门写给技术型创始人：

没预算，没增长团队，怎么找第一批用户，怎么做 GTM，怎么把营销拆成能执行的动作

更狠的是，它不是空谈。

里面直接按主题整理了 launch 平台、Product Hunt、社媒、冷启动外联、SEO、LLM SEO / AEO / GEO、Reddit、邮件营销、内容营销、定价、转化率优化、用户研究这些实操资源。

我越来越认同一件事：

独立开发者最大的误区，
不是产品做得不够好，
而是把“增长”误解成“等别人发现”。

不会营销的创始人，本质上是在把产品交给随机流量审判。

如果你正在做 SaaS、AI 工具或 side project，
这个仓库很值得收藏。👇

---

**作者** Shiv Kampani（@shiv_kampani）  
**貼文連結** https://x.com/shiv_kampani/status/2033589095918932401  

**正文**

We closed Brex during the W26 batch!

Brex's startup sales team uses Autumn to find venture-backed founders before they’ve been publicly announced. Last week, our agent surfaced 150+ unannounced founders by piecing together GitHub commits, Luma event pages, LinkedIn bio changes, and Delaware incorporation filings.

Brex moves fast. First call to contract + implementation in days. Super grateful to Jimmy Stephens for giving us the opportunity to build with Brex.

The best products get built with the best customers.

---

**作者** 刚出道的小七（@meiridasai661）  
**貼文連結** https://x.com/meiridasai661/status/1889657978158194919  

**正文**

超超超巨乳姐姐来了 再出租屋 与男友做爱合集
果然是奶子越大 责任越大呀
投稿📮

@SexytoBaby

@SexytoLady

@SexytoDoll

@SexytoGirl

---

**作者** Muratcan Koylan（@koylanai）  
**貼文連結** https://x.com/koylanai/status/2033663476451901867  

**正文**

SkillNet is the first paper I've seen that treats agent skills as a network, a three-layer ontology that turns isolated skill files into a structured, composable network.

Externalizing knowledge into files isn't enough. You also need to know how those files relate to each other.

Layer 1 is a Skill Taxonomy. Ten top-level categories (Development, AIGC, Research, Science, Business, Testing, Productivity, Security, Lifestyle, Other), each broken into fine-grained tags: frontend, python, llm, physics, biology, plotting, debugging. This is the semantic skeleton. It answers "what domain does this skill belong to?"

Layer 2 is the Skill Relation Graph. This is where SkillNet diverges from other skill repositories. Tags from Layer 1 get instantiated into specific skill entities (Matplotlib, Playwright, kegg-database, gget). Then four typed relations define how skills connect: 
> similar_to: two skills do the same thing. Matplotlib and Seaborn both plot. Enables redundancy detection.
> belong_to: a skill is a sub-component of a larger workflow. Captures hierarchy and abstraction.
> compose_with: two skills chain together. One's output feeds the other's input. This is the relation that enables automatic workflow generation.
> depend_on: a skill can't run without a prerequisite. Enables safe execution by resolving the dependency graph before running anything.

These four relations form a directed, typed multi-relational graph. Nodes are skills, edges are typed relationships. And the graph is dynamic. As new skills enter the system, LLMs infer relations from their metadata.

Layer 3 is the Skill Package Library. Individual skills bundled into deployable packages. A data-science-visualization package contains Matplotlib, Seaborn, Plotly, GeoPandas with their relations pre-configured. You install a package, you get a coherent set of skills that already know how to compose with each other.

This is a good example of what comes after a flat package manager. 

The paper also (you can test here http://skillnet.openkg.cn/) has a science case on a real research workflow: identifying disease-associated genes and candidate therapeutic targets from large-scale biological data.

Without encoded relations, the agent figures out the research pipeline from scratch every time. With them, it receives a pre-structured execution plan. The agent still reasons about which genes to focus on and which pathways to investigate. But the pipeline architecture is given.

So the skill metadata is actually doing routing work too. The metadata encodes the judgment a domain expert would make when choosing between tools.

I also like this framing from the paper: Skills are how memory becomes executable and workflows become flexible.

While the network effect and layered architecture is actually useful today, they also acknowledge this: "Low-frequency or highly tacit abilities are difficult to capture, particularly when they resist explicit linguistic description."

From my short research career, I'd say the hardest parts are hypothesis generation, experimental design judgment, and interpreting ambiguous results etc.

SkillNet handles the structured pipeline well; fetch data → analyze → validate → report. It doesn't handle the creative work where a scientist's (not just in science but in any white-collar field) intuition drives what's worth investigating in the first place.

Skills encode "how to run the analysis." They don't encode "what's worth analyzing." That gap is where domain expertise still sits.

---

**作者** Artem Zhutov（@ArtemXTech）  
**貼文連結** https://x.com/ArtemXTech/status/2033588201844040141  

**正文**

How I Manage 10 Claude Code Agents Without Losing My Mind
I run multiple Claude Code agents every day. Doing research, drafts, video scripting, all at the same time, and I don't lose track of any of

---

**作者** Selina（@Selinaliyy）  
**貼文連結** https://x.com/Selinaliyy/status/2033773131601453205  

**正文**

we got featured by @Forbes as a Top Startup to Watch from Y Combinator W26 🚀

A few months ago, we realized something uncomfortable: we were building @bubblelab_ai for the wrong audience.

Developers liked it. But the people who REALLY needed it were ops teams.

So during our YC batch, we refocused the product around them. Since then:
• 50% month-over-month revenue growth
• almost 10,000 workflows built
• fast-growing companies now running ops workflows on Bubble Lab...without ever leaving slack!

Huge thanks to the early teams building with us 🫧 we're just getting started!

---

**作者** nizzy（@nizzyabi）  
**貼文連結** https://x.com/nizzyabi/status/2033698711075733938  

**正文**

Today we're opening up Orchid to our first users.
Orchid connects to your tools, understands your work, and handles things before you even think about them. You just approve.
Not faster. Gone.
Every

---

**作者** KK.aWSB（@KKaWSB）  
**貼文連結** https://x.com/KKaWSB/status/2033747401085751598  

**正文**

“OpenClaw 就是新型计算机。”——黄仁勋

这简直就是个人电脑早期时代的重现。

少数高级用户可以看到。

其他人都还没开始呢。

“它是人类历史上最受欢迎的开源项目，而且只用了几周时间就做到了。它超越了Linux在30年里取得的成就。”

借助 OpenClaw，现在一名独立创始人就可以构建以前需要 50 人团队才能构建的功能。

这种杠杆作用简直荒谬。

---

**作者** Kenny.eth（@_0xKenny）  
**貼文連結** https://x.com/_0xKenny/status/2033684452614820123  

**正文**

刚发布的AI产品，立刻分享 - Okara AI CMO。

2026年最大的创业悖论： 用 OpenAI Codex / Claude Code， 一个人两周能做出个复杂产品。

但上线之后呢？ 没有用户，没有流量，没有增长。

因为，产品不再是瓶颈，获客才是。

Okara 今天推出了AI世代的解决方案：AI CMO - 智能市场营销首席执行官

AI CMO 是什么？ 一句话： 输入你的网站，它自动部署一整支 AI 营销团队，7×24小时帮你跑增长。

不是 Dashboard，不是 Prompt 模板， 是真正的 Agent Fleet - 每个 Agent 负责一个独立增长渠道， 开箱即用，分钟级启动。

现在已部署的 Agent 阵容：

🔍 SEO Agent - 每天审计你的站点，每早把5条具体可执行的优化建议发到你邮箱（不是废话，是带代码的直接操作）

🤖 GEO Agent - 追踪你的品牌在 ChatGPT / Claude / Perplexity / Gemini 里的曝光度、情绪、平均排位

📕 Reddit Agent - 监控 Reddit 相关帖子，自动生成符合社区语气的高质量回复

💻 HN Agent - 同样覆盖 Hacker News，最高信任度的早期用户聚集地

✍️ AI Writer Agent - 内容生产

🐦 X Agent - 管理你的社交增长

即将上线的 Agent：

📺 YouTube 💼 LinkedIn 🤝 Influencer 外联 🔗 Link Building

这不是一个工具， 这是一个自动运转的营销部门。

对比一下，雇一支真实的营销团队：

内容写手：$3-5万/年
SEO 机构：$2-4万/年
社媒运营：$1.5-3万/年
社区运营：$1.5-3万/年

合计：$5万到$16万+/年

AI CMO： $99/月 = $1188/年

节省比例：98%

这里有个很重要的点被大多数人忽略了：

现在 AI Search（ChatGPT / Perplexity / Claude）开始抢走 Google 的份额。你在 Google 排第一，没用， 如果 AI 搜索引擎根本不提你。

GEO（Generative Engine Optimization）是 2026 年最被低估的增长杠杆， AI CMO 自动帮你监控并优化这件事。

结论： 从 OPC（One Person Company）视角来看，对于运营一个或者多个品牌的创业者，每个品牌都需要 SEO、内容、社区、AI Search 曝光， 但资源有限。AI CMO 就是为这种 solo-brand/multi-brand solo founder 而生的。

使用方式极简：

1️⃣ 进入 okara CMO 官网 
2️⃣ 输入你的网站 
3️⃣ Agent 在几分钟内开始工作

没有繁琐配置，没有 API key， 没有 10 个工具来回切换。

谁最该用 AI CMO？

✅ 独立开发者/solo founder：做了产品，没有增长资源 
✅ 出海品牌：需要 Reddit/HN/X 多平台渗透 
✅ AI 创业公司：GEO 可见性是生死线 
✅ 多品牌运营者：每个品牌都需要增长引擎 
✅ 早期 Startup：$99 比招一个实习生还便宜

一句话总结 AI CMO：

你负责把产品做好， 它负责让全世界知道你存在。

这就是 One Person Company 的终极形态。

---

**作者** Rohit（@rohit4verse）  
**貼文連結** https://x.com/rohit4verse/status/2033207210080424373  

**正文**

Anthropic locked this behind a partner program. 
This guy reverse-engineered the whole thing. 
And gave it for free. 

---

**作者** Yihui（@yihui_indie）  
**貼文連結** https://x.com/yihui_indie/status/2033767136515264764  

**正文**

上周听玉伯的播客，他想让至少 1000 个创作者通过 YouMind 赚到 1000 美金。我想说我今年，100% 能通过 YouMind 赚到 10万美金。

昨天小火的推文，发现对YouMind这个产品和使用场景不太熟悉，我开个Thread简单的介绍一下我的至少 10 个使用用法吧（不定期更新完）

放心，绝对无广可食用！YouMind没给过我一分钱~

---

**作者** Furqan Rydhan（@FurqanR）  
**貼文連結** https://x.com/FurqanR/status/2033694130627604673  

**正文**

Most AI agents only talk. They generate responses, maybe read data from an API, and that's it. The moment you need something that takes longer than a single request-response cycle, you're back to

---

**作者** Aric（@AricChang）  
**貼文連結** https://x.com/AricChang/status/2033607597211766826  

**正文**

I’m excited to announce the launch of Prototype, a venture fund focused on investing in frontier technologies. I first entered the crypto industry in 2019 as a regulatory consultant, advising digital asset managers on SEC regulations. Watching my clients deploy capital into such a new and unfamiliar sector inspired me to take my own leap and become a venture investor in the space. Since then, I’ve focused on backing early-stage startups as crypto steadily evolved into an integral part of global financial infrastructure. As crypto becomes more accessible, and as AI lowers the barriers to entrepreneurship, Prototype aims to invest in frontier technologies that empower people to seek opportunities and generate value through their own means. Thank you to the mentors, colleagues, and supporters who helped make this possible. Now it’s time to get to work!

---

**作者** Xiao Tan（@tvytlx）  
**貼文連結** https://x.com/tvytlx/status/2033455217984041213  

**正文**

本文适合想要对ClaudeCode更进一步学习，以便掌握真实世界工程落地能力的人。
通过本文提供的沉浸式互动学习Prompt。你将掌握所有 Agent 开发的核心知识，并具备开发出生产级 AI 应用，创造真实的商业价值的能力。

---

**作者** joowon（@n0w00j）  
**貼文連結** https://x.com/n0w00j/status/2033615331558650132  

**正文**

i thought this was the first AI CMO 

---

**作者** ericosiu（@ericosiu）  
**貼文連結** https://x.com/ericosiu/status/2033715055028846833  

**正文**

We generated $6.6M in pipeline with AI agents - and still couldn’t sell them.
Not because they didn’t work. Because they weren’t enterprise-ready. 
Every 9-figure+ company asked the same questions:

---

**作者** Gorynich☄️（@Kropanchik）  
**貼文連結** https://x.com/Kropanchik/status/2033494954912182486  

**正文**

The Gap Between Knowing and Doing

The article below is brilliant. But it misses one thing traders already know:

Knowing that you should calculate expected value is not the same as actually doing it.

Most traders don't fail because they don't understand Kelly Criterion. They fail because they never run the numbers.

They see a trade that "feels right" and size 80% of the account on it.

They watch someone successful and copy them without asking: "What is this person's actual edge?"

They "trust their gut" when their gut has never been stress-tested against reality.

MiroFish doesn't give you the answer to "what will happen."

But it answers the harder question: "What are ALL the ways this could play out, and how likely is each one?"

That's not prediction. That's clarity.

The moment you see 500 simulations of a market move and realize:
- 320 scenarios go in your favor
- 180 go against you
- In 80 of those, you get liquidated

...suddenly position sizing isn't theoretical anymore.

Suddenly you can calculate: "I should risk 2% of my account, not 20%."

That's not because MiroFish is always right. It's because you finally KNOW what you're doing instead of guessing.

And that small difference - knowing vs guessing - compounds into the difference between blowing up and surviving.

The traders who use tools like this don't win every trade.

They just don't go broke.

And over 500 trades, that's everything.

---

**作者** Ronin（@DeRonin_）  
**貼文連結** https://x.com/DeRonin_/status/2033587293064204349  

**正文**

AI engineering has quickly become one of the most valuable skill sets in tech
The problem is that most beginners have no clear idea what they should actually study
Some start with machine learning

---

**作者** Tim Haldorsson（@TimHaldorsson）  
**貼文連結** https://x.com/TimHaldorsson/status/2033438492236104009  

**正文**

@claudeai just dropped a full free course library. here's every course, what it teaches, and the roles each of them could help you to land. 
 
1. Claude 101
the starting point. covers how to use

---

**作者** Barrett Linburg（@DallasAptGP）  
**貼文連結** https://x.com/DallasAptGP/status/2033574400901935534  

**正文**

We built a system where Claude knows our entire company before I type a word. 

Three operating companies. 50+ properties. Full context on every session.

Three tools. Any small business can build this.

Most business owners use AI the same way every time. Open Claude. Re-explain the business. Re-explain the team. Re-explain the numbers. Then ask the question.

You're onboarding the same employee every morning.

We fixed this. Claude now knows the full operation before I type a word.

Start with your most important company knowledge. Turn each topic into its own markdown file. Markdown is simple text that AI reads clean.

Think about what you re-explain over and over. How your business makes money. Your org chart and who owns what. Your pricing. Key metrics for each team member. Your sales process. Your brand voice.

One topic per file. Keep them short.

Put everything in Obsidian. It's free. Files stay on your computer. Nothing goes to the cloud. Think of it as a filing cabinet on your own hard drive that AI can search in milliseconds.

Here's what makes it work. Every file connects to related files through tagged links called wikilinks. When you ask Claude about a specific client, it doesn't just find the client file. It pulls every project, contract, invoice, and note tied to that client. One question. Full picture.

Then connect Claude Code. It works like the regular Claude desktop app with one difference. It has the keys to your filing cabinet.

Claude Code reads files right off your computer. No uploads. No cloud. No file size limits. Your financials, client data, and internal strategy never leave your machine. For business owners who won't put sensitive data on someone else's server, this solves the problem.

Most people I know spend $100 to $200 a month on Claude. If you're already paying that, you should be getting more out of it than a chatbot that forgets who you are every session.

Some of you already use Claude Projects. Good. That puts you ahead of most people.

Projects let you upload files and give Claude a custom instruction set. For small tasks, it works. If you have a handful of documents and a clear use case, Projects is the right starting point.

But it has a ceiling. Upload limits cap how much context you can load. Your files live on Anthropic's servers. And every project is its own silo. Your sales project doesn't talk to your ops project. Your finance files don't connect to your team files.

The Obsidian setup removes all three limits. No upload cap. Files stay on your machine. And every file links to every related file across your whole company.

The last piece is one instruction file. It tells Claude how your company works, what role it plays, and how to navigate the knowledge base. Think of it as the onboarding doc you'd hand a senior executive on day one. Except this executive never forgets it.

Once it's built, every session starts with full context. Claude knows your team. Your numbers. Your processes. You skip the setup. You go straight to the work.

Three tools. Obsidian (free). Claude Code (you're already paying for it). One instruction file.

If you run a business and you're still re-explaining yourself to AI every session, you're leaving speed on the table.

---

**作者** Andrew Brown（@andrewbrown）  
**貼文連結** https://x.com/andrewbrown/status/2033546424789463205  

**正文**

While I package my free Claude Code Essentials course and then proceed to pull 12 hour work days to ship my free Claude Certified Architect study course, let me you behind the scene for a moment.

For the past 10 years I’ve tried to make high-quality cloud/tech courses freely available.

This is a personal choice I made, because it's what I want to do for you my tech community. 

To make this happen I’ve structured my life around keeping costs as low possible so I could continue doing this, even when it wasn’t the most financially sensible path.

But the reality is that producing these courses takes an enormous amount of time and resources.

The model only works if enough people support it in small ways subscribing, sharing the content, or supporting the paid offerings that help fund the free material.

If my 50 free courses have helped you in your career in the last decade.

Please consider the small things like following or subscribing to my own Youtube channel. 

It makes a bigger difference than most people realize.

For those who have been supporting us all these years, you are the real hero's because I simply would have never been able to do it without you.

---

**作者** Andrew Brown（@andrewbrown）  
**貼文連結** https://x.com/andrewbrown/status/2033600346715513221  

**正文**

There are two things that fall out side the scope of my Claude Code Courses, that I could potentially develop as paid courses.

Enterprises, and Absolutely Non Technical Professionals. 

Let's just workshop that a bit together:

> Claude Code from Zero
There are professionals coming from other verticals that want to use Claude Code but they have never touch code in their life. I would have teach them ALL the steps and leave nothing out no matter how small.  I would also have to guide them entire lifecycle of app development and provide full mentorship.

> Claude Code Enterprise Architect
Orgs want to adopt Claude Code but its not enough to just learn how to use the tool, they those workloads to be fully productionize. That means security, governance, develop onboarding, incident response and rollback. I don't mean on paper, I mean for real.

---

**作者** Abby Grills（@AGrillz）  
**貼文連結** https://x.com/AGrillz/status/2033621300636487955  

**正文**

I made a free web app that tracks @ycombinator  companies.

It updates when:
- A new company is listed to YC’s website
- A company does a launch post
- A company changes their name or tagline/one-liner

You can even download the full list of all the companies YC has ever funded. 

---

**作者** hoeem（@hooeem）  
**貼文連結** https://x.com/hooeem/status/2030720614752039185  

**正文**

You want to deploy Andrew Karpathy’s autoresearch that lets you have agents run research experiments whilst you sleep with any prompt but you don’t know how, read this.
So, here’s the thing, Karpathy

---

**作者** hoeem（@hooeem）  
**貼文連結** https://x.com/hooeem/status/2031755971265974632  

**正文**

I have combined every resource I have found to create a full course on Claude Skills. In less than 10 minutes you'll have built and deployed your first custom skill. After reading this article you

---

**作者** Sarah Wooders（@sarahwooders）  
**貼文連結** https://x.com/sarahwooders/status/2033592972168806827  

**正文**

Although I use Letta Code (a memory-first coding agent) as my daily driver, there are still some cases where a stateless agent like Codex or Claude Code might do better. Agents with memory are

---

**作者** hoeem（@hooeem）  
**貼文連結** https://x.com/hooeem/status/2033198345045336559  

**正文**

To become a Claude Architect and develop production-grade applications you need to understand Claude Code, Claude Agent SDK, Claude API, and Model Context Protocols, this article will help you learn

---

**作者** Chamath Palihapitiya（@chamath）  
**貼文連結** https://x.com/chamath/status/2032348022336864731  

**正文**

“In 2026, AI is driving a 10x increase in the productivity of the individuals who know how to leverage it. But that’s not enough. We’ve swapped the motor; we have not yet redesigned the factory.

Because of a simple fact: productive individuals do not make productive firms.

The wide majority of AI products evoke the feeling of being productive, but they haven’t moved the needle on driving value. 

The majority of publicized AI use is individuals self-indulgently “productivity-maxxing” on Twitter or in company Slack channels, with zero real impact.”

I couldn’t agree more. 

This is why we built Software Factory. 

Try it here: http://8090.ai

---

**作者** yan5xu（@yan5xu）  
**貼文連結** https://x.com/yan5xu/status/2033721014413402303  

**正文**

一、Agent 是 OS，垂类做 OS 是找死
1/ Agent 是一种交互范式，就像手机是一种交互范式。你通过手机购物、社交、理财，但不会为了购物专门买一部手机。Agent 也一样。垂类不应该尝试做 Agent（做手机），应该做

---

**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2033646028336046501  

**正文**

Congrats to @UnderstoodCare on their $8.4M raise!

60M+ adults over 65 struggle to navigate the US healthcare system alone. Understood Care gives human advocates an AI copilot to help patients schedule appointments, access benefits, and coordinate care.

https://www.axios.com/pro/health-tech-deals/2026/03/16/understood-care-8m-patient-advocacy

---

**作者** Kathy.xyz（@KathySats）  
**貼文連結** https://x.com/KathySats/status/2033700844026409241  

**正文**

用Gemini + OpenClaw + MiroFish沙盘模拟了伊朗形势，结果....

上周日我看到Mirofish这个项目后，
觉得太好玩了，就想到这个idea
于是就让我的🦞配置了MiroFish，结果分析得透透是道👇 

---

**作者** George Sivulka（@gsivulka）  
**貼文連結** https://x.com/gsivulka/status/2033614362758561974  

**正文**

Financial AI is here. 

Wall Street, meet the future of institutional intelligence.

See how Oak Hill Advisors, LionTree, @NewYorkLife, @MetLife, & @HSFKramer are already putting it to work. 

---

**作者** 子时（@silverfang88）  
**貼文連結** https://x.com/silverfang88/status/2033740106297667878  

**正文**

收到马斯克盛赞的
Kimi论文第一作者陈广宇
是一位17岁的高中生

值得注意的是
他就读于Moonshot Academy
这是一个位于中国的
创新型K-12学校（小初高）

大家在疑惑AI
会怎么改变教育的时候
教育已经被改变了

他在竞技编程方面基础扎实
在Codeforces上达到
Candidate Master级别
rating 2000+
属于顶尖青少年水平

2025年3月他赢得
48小时黑客马拉松第一名
也是他被发掘出来的重要原因

这是个属于天才的时代
是金子根本就藏不住

---

**作者** Nicholas Chua（@nicholasychua）  
**貼文連結** https://x.com/nicholasychua/status/2033585479732629725  

**正文**

if you are interested in everything i've learned over the past 3 months about x articles, formats, and content strategy.

stay tuned ;) 

---

**作者** vas（@vasuman）  
**貼文連結** https://x.com/vasuman/status/2021362047980892628  

**正文**

As most CFOs know, finance feels more bloated than ever. ERPs, close management platforms, AP automations, expense tools, treasury systems, and more. The software stack is deep, yet most CFOs I talk

---

**作者** DreykØ（@dreyk0o0）  
**貼文連結** https://x.com/dreyk0o0/status/2033539110808199214  

**正文**

I spent a few days studying the MiroFish swarm-intelligence engine

Then I tried to build my own version for Polymarket.

The results were insane.

Instead of predicting prices,
the engine simulates how people react to events.

Core idea:

Prediction markets don’t move on math alone.
They move on behavior.

So I built a multi-agent simulation.

Each agent has memory, bias, and strategy.

Core components:

Swarm agents
168 agents / 6 clusters / 700+ links

Belief update model
Pₜ₊₁ = f(Pₜ, news, sentiment, liquidity)

Consensus probability
P_swarm = Σ wᵢ Pᵢ

Market edge
EV = P_swarm − P_market

Monte-Carlo validation
10,000 simulations per event

Network clustering
detects narrative shifts before price moves

The system simulates:

• voters
• media
• donors
• traders
• pollsters
• momentum bots
• narrative spread

Each agent updates beliefs →
cluster reaches consensus →
swarm outputs probability.

If swarm probability ≠ market price
→ trade

Current dashboard:

1,250 active agents
100,000+ interactions
3,800 graph nodes
240 simulation rounds

Top prediction engine:

Polymarket price: 20%
Swarm probability: 27.3%
Alpha edge: +7.3%

Win rate: 67%
Sharpe: 8+
Max DD: <2%

This changed how we can see prediction markets.

It’s not trading.

It’s modeling reality.

---

**作者** 花叔（@AlchainHust）  
**貼文連結** https://x.com/AlchainHust/status/2033573236240466178  

**正文**

晚上突然看到马斯克发了一条推：「Impressive work from Kimi」。
 
去查了下，想看看咋咋唬唬的老马又是被啥震惊到了。
然后，发现原来是Kimi发了篇论文👇

---

**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2033567417461547144  

**正文**

果然，Agent 只要有新形态，Manus 就会跟进。

他们发布了 My Computer，可以在你本地运行 AI Agent，操纵你的本地文件、运行自动化工作流。

有 Window 和 Mac OS 版本。



---

**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2033699960664039612  

**正文**

Codex 现在支持创建 Subagents

而且你还能切换窗口很便捷的跟踪每个Subagents 正在做的事情

 

---

**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2033708252681392213  

**正文**

Kimi 昨晚这篇论文很猛

尝试用 K2.5 对 Kimi 这篇论文进行可视化解释。 

---

**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2033734364299989008  

**正文**

精通 Claude，是 2026 年杠杆最高的 AI 技能。

如果你想变得富有，就在下面这些方向中挑 1–2 个做到专家级。 

---

**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2033735856268472666  

**正文**

🧵Thread: AI记忆赛道全景拆解
1/ 🦞 我装了5个龙虾，接了5家服务商，扫了四五个码，中途挂了几个重配——两周踩完所有坑后发现：

1000个想试的人，最后能真正用进工作流的可能只剩1-2个。

但傅盛、玉伯、字节、阿里全部入局了，而且押注方向完全不同。一个Thread讲清楚👇 

---

**作者** JG（@jongall45）  
**貼文連結** https://x.com/jongall45/status/2033559723895595198  

**正文**

shipped a new feed feature for @frontrunvc

curated startup discovery feed - powered by X signals

discovery -> due diligence -> finding & DMing the founder, all in under a minute

stop doom scrolling & collapse your deal flow into seconds. 

---

**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2033589109298471244  

**正文**

21st (@21stdev) is the production layer for frontier AI agents. 1.4M developers already use their platform to build AI apps, 15K+ GitHub stars - now they're making it dead simple to deploy Claude Code, Codex, and other agents to production.

Congrats on the launch, @sergeybunas & @serafimcloud!

https://www.ycombinator.com/launches/PiD-21st-infrastructure-for-ai-agents

---

**作者** vas（@vasuman）  
**貼文連結** https://x.com/vasuman/status/2033584809511911790  

**正文**

If you read articles like this for fun you’ll fit right in at Varick

Join us, we’re growing

---

**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2033593027567227121  

**正文**

i am a high schooler who has been running a $50M+ startup completely solo for almost a year. here is what I learned (thread): 

---

**作者** Yiliu（@yiliush）  
**貼文連結** https://x.com/yiliush/status/2033251389577847151  

**正文**

seeing if/how graphs come back in 

---

**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2033441957985280451  

**正文**

作者：Bassim Eledath
原文：The 8 Levels of Agentic Engineering — Bassim Eledath
AI 的编程能力正在超越我们驾驭它的能力。这就是为什么所有那些拼命刷 SWE-bench

---

**作者** Numman Ali（@nummanali）  
**貼文連結** https://x.com/nummanali/status/2033500799641207226  

**正文**

Agentic Engineering Patterns from @simonw is awesome 

It’s his ever growing project on documenting the best practices with coding agents 

https://simonwillison.net/guides/agentic-engineering-patterns/

Each article is short and sweet <5mins per read 

You have to read these if you’re a beginner 

---

**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2033541383504478226  

**正文**

claude code + obsidian in under 1 minute 

---

**作者** Yihui（@yihui_indie）  
**貼文連結** https://x.com/yihui_indie/status/2033477400542269505  

**正文**

讲真，YouMind 的 Agent 越用越爱，我真的看不到这个产品的上限在哪里！

好羡慕 YouMind 的同学，能加入一家这么优秀的创业公司。

---

**作者** DeMo❤️‍🔥（@0xDeMoo）  
**貼文連結** https://x.com/0xDeMoo/status/2033417475845759176  

**正文**

MiroFish 是群体行为模拟器
Polymarket 是群体行为市场

把两者结合起来, 信息和钱就都有了

最近推bot吃反佣的太多, 落地待验证
但思路是对的, 最近会有不少Alpha

---

**作者** Hanako（@hanakoxbt）  
**貼文連結** https://x.com/hanakoxbt/status/2033250813355679756  

**正文**

I asked Claude to build me a MiroFish God View terminal

it showed me 56 live agents that simulate real world

each agent has memory, personality, and behavior

they form groups. develop leaders. shift opinions in real time

I feed it a scenario:
"Fed cuts rates by 50bps"
56 digital humans reorganize in seconds
retail agents panic buy YES on Polymarket.
institutional agents fade the move
opinion leaders wait

the terminal maps every shift live

throughput: 5,000 ops/s
latency: 23ms
2.1M tokens processed per cycle
zero errors

I watch the consensus form before Polymarket prices it

> monday: injected "US-China military standoff in Taiwan Strait"
agents split instantly - 39 rushed YES on "conflict before 2027"
bought YES at $0.08 before the herd moved
Polymarket moved to $0.29 by tuesday
+$1,840

> wednesday: injected "S&P500 drops 3% intraday"
48 of 56 agents shifted bearish in 9 seconds
loaded YES on "S&P500 below 5000 by July" at $0.12
contract hit $0.31 by friday
+$2,470

> sunday: injected "Trump announces new tariffs on EU"
herd effect kicked in - retail agents mass-bought YES
institutional agents faded at peak
I followed the institutions. bought NO at $0.22
settled at $0.71 monday morning
+$3,048

total: $7,358 in 7 days
from scenarios that haven't happened yet

the god view doesn't predict price
it predicts how people bet
and people move the odds

one terminal. 56 agents. zero team

copytrade here: http://kreo.app/@1743116

you don't need to predict events
you need to predict how Polymarket reacts to them

---

**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2033523885753483713  

**正文**

好嘛，OpenClaw 也太猛了。

大家用它做开发、用它赚钱，根本停不下来。

8 个超狠案例。

1、OpenClaw 办公室里的敏捷站会， 

---

**作者** Yanhua（@yanhua1010）  
**貼文連結** https://x.com/yanhua1010/status/2033374635883192735  

**正文**

最近听了田渊栋在《硅谷坐标》的访谈，前 Meta 研究总监，强化学习和大模型推理方向的人。
聊的几个判断我觉得值得认真对待，整理出来分享给大家。
护城河排序：数据 > Infra > 算力 > 算法 ≈ 人才

---

**作者** Chamath Palihapitiya（@chamath）  
**貼文連結** https://x.com/chamath/status/2033385903520129161  

**正文**

The Collapse of Terminal Value
The following is a thought exercise. It is an inversion to re-examine...well, everything.
Let’s start with first principles.
The entire architecture of modern capital

---

**作者** Shawn Pang（@0xshawnpang）  
**貼文連結** https://x.com/0xshawnpang/status/2033433838278623398  

**正文**

复盘了自己过去一年的谷歌日历研究作为创始人每天到底在干嘛，挑出了50件AI完全能干的事，用Skills自动化：

  - 一键申请40+北美主流加速器（YC、Speedrun、HF0...）
  - 从Trustpilot/G2差评里挖竞品痛点，顺便挖客户
  - 找到你用户藏在哪些Discord/Slack/Reddit社群去发消息找早期用户
  - 每周自动监控竞品定价页、更新日志、招聘动态，看看友商在干嘛

欢迎体验！少做重复的事，多跟用户聊天，多出去走走。

https://github.com/shawnpang/startup-founder-skills/

---

**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2033212279924416946  

**正文**

Ventura (@getventura) deploys AI employees inside the ERPs that distributors and manufacturers already run on, starting with quoting and order processing.

Congrats on the launch, @swekol & @jackmpcollins!

https://www.ycombinator.com/launches/Phm-ventura-ai-teammates-for-industrial-distributors 

---

**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2033437609460891883  

**正文**

Ramp 是美国增长最快的企业金融平台之一，估值 320 亿美元，超过 50,000 家客户，年交易处理量超过 1000 亿美元。在 The Pragmatic Summit 上，Ramp 派出了四人阵容分享他们过去一年在 AI

---

**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2033307260173312146  

**正文**

onboarding time cut from 60 seconds to 8 seconds.

> detects all agents on your machine automatically
> automatically generates an api key
> automatically installs the @nozomioai skill and cli
> easy browser auth 

---

**作者** Florian Darroman（@floriandarroman）  
**貼文連結** https://x.com/floriandarroman/status/2033517133607383323  

**正文**

This guy built a $1M ARR SaaS in 117 days (he had 16 followers)

and now just hit $8M ARR. 100% Bootstrapped.

@yasser_elsaid_ is the perfect example that you don't need a personal brand or VCs to make it.

You just need these 8 things:

Full video: https://linktw.in/Odnbgc 

---

**作者** Julián（@juliandeangeIis）  
**貼文連結** https://x.com/juliandeangeIis/status/2033303156340240481  

**正文**

The Spec Is the New Code
AI coding agents don’t fail because the model is weak. They fail because the instructions are ambiguous and the agent harness is too weak.
That’s why everyone is building

---

**作者** Khe Hy（@khemaridh）  
**貼文連結** https://x.com/khemaridh/status/2033262791805882853  

**正文**

Friends, hope your weekends are off to a great start. The Santa Ana winds are creating summer conditions in March (and some great waves).
This tweet went viral and I found it very relatable.
 
I’ve

---

**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2033393305162232263  

**正文**

🧵Thread: AI记忆赛道全景拆解
1/ 🧠 2025年AI最大的瓶颈不是推理，是记忆。

五位创业者给了五个完全不同的答案：文件系统、Python代码、Git仓库、三层架构、浏览器插件。

记忆决定了AI能不能从"工具"变成"懂你的伙伴"——而现在，你所有的记忆都存在大厂手里。

一个Thread讲清楚👇 

---

**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2033379627184599148  

**正文**

重点是这个项目只有藏师傅一个人。

我去，那在年前很难想象我能够有一周十万行代码的能力，而且这个速度还在提升，bug 的几率还在下降。

而且我这样，都没有把 Max 会员 200 美元的额度用完。

很难想象那些一个月跑十几亿 token 的朋友咋用

---

**作者** Oliver Prompts（@oliviscusAI）  
**貼文連結** https://x.com/oliviscusAI/status/2032862410193908012  

**正文**

You can now run a full Wall Street hedge fund from your laptop.

Someone just open-sourced an AI Hedge Fund powered by 18 specialized agents. It mimics legendary investors like Warren Buffett, Michael Burry, and Cathie Wood to analyze stocks and vote on trades.

48.9K+ GitHub stars. 100% Open Source.

---

**作者** Garry Tan（@garrytan）  
**貼文連結** https://x.com/garrytan/status/2032828268794065095  

**正文**

This looks cool, bookmarking for later

---

**作者** Kenny.eth（@_0xKenny）  
**貼文連結** https://x.com/_0xKenny/status/2033039918016897411  

**正文**

过去两周，AI 开源圈最容易让人上头的事情，是每天都有新项目冒出来、每天都有新的 GitHub 热门榜、每天都有人在喊"这个会改变一切"。

但真正值得花时间盯的项目，其实并不多。

1. MiroFish
https://github.com/666ghj/MiroFish

这是最近最容易被当成"神项目故事"消费掉的一个。20 岁学生、10 天、GitHub 冲榜、融资，这些都很吸睛。但如果只看到故事，就会错过它真正重要的方向：它不是在做普通 Agent，而是在做数字社会仿真。

知识图谱、多 Agent、长期记忆、可注入变量的 God View，这些东西组合起来，意味着它正在逼近一个更大的方向 - 把现实世界中难以直接做实验的复杂系统，改造成可以反复推演的数字沙盘。对宏观、市场、舆情、组织行为这类问题来说，这条路线非常值得长期盯。

2. OpenClaw-RL
https://github.com/Gen-Verse/OpenClaw-RL

这类项目的价值，不在于"又给 Agent 加了 RL"，而在于它开始认真回答一个真正重要的问题：Agent 能不能在真实使用过程中持续学习，而不是训练完就冻结？

如果未来 Agent 真正的护城河，不是初始模型能力，而是谁更会学、谁越用越像你，那 OpenClaw-RL 这种方向就不会只是研究型项目，而会是未来 Agent runtime 的基础设施雏形。

3. gstack
https://github.com/garrytan/gstack

这不是普通的 prompt 包，而是把 Claude Code 从单脑助手拆成多角色工程团队的一次工程化尝试。Founder 脑、Eng 脑、Reviewer 脑、QA 脑，背后对应的是一个更成熟的工作流观念：复杂任务不是靠一个万能 AI 一路干到底，而是按阶段切换不同认知模式。

4. agent-cli
https://github.com/Nunchi-trade/agent-cli

如果说很多交易 Agent 还停留在会下单、会看行情的 demo 层，agent-cli 已经明显在往更完整的交易操作系统靠。策略、调度、风控、复盘、自我调参、MCP、OpenClaw 集成，都被装进了一套可编排框架。

它真正展示的，不是"AI 也能交易"，而是：高价值垂直 Agent 的未来形态，很可能不是一个聊天机器人，而是一个严肃执行系统，前面再接上可对话、可调度、可组合的智能入口。

5. OpenClaw402
https://github.com/NoFxAiOS/openclaw

这可能是最近最容易被低估的一个方向。很多人以为它只是又一个 OpenClaw fork，但它真正碰的不是 UI，而是经济层。

它试图把 Agent 的默认支付方式从 API key 改成钱包和按次支付：用户不再先去配 OpenAI/Anthropic key，而是每次调用时自动用 USDC 完成结算。这个方向如果跑通，可能把 Agent 产品从开发者工具逻辑，推向消费者产品逻辑。

6. opencli
https://github.com/jackwener/opencli

这个项目做的事情非常干净：把任何网站直接变成 CLI 命令行工具。

bilibili、知乎、小红书、Twitter、Reddit、GitHub、HackerNews、YouTube、Boss 直聘……28 个以上的命令，覆盖 16 个主流平台，复用 Chrome 登录态，账号密码从不离开浏览器。

它对 Agent builder 来说特别有意思：大量网站没有官方 API，但 opencli 通过 AI 驱动的 API 发现 + YAML 声明式适配器，让任意网站都可以变成可编程的数据源。这件事一旦跑通，意味着 Agent 的信息获取层会大大降低集成成本。

7. sub2api
https://github.com/Wei-Shaw/sub2api

这是一个很直接地戳中了真实需求的项目：你有 Claude Pro 订阅、有 OpenAI Plus 订阅，但你想把这些订阅的 quota 统一分配、多人拼车共享、精确到 token 计费。

sub2api 做的就是这件事：把各类 AI 订阅接入统一 API 网关，支持多账号调度、并发控制、限速、token 级计费、管理后台。技术栈 Go + Vue3 + PostgreSQL + Redis，有一键安装脚本，生态里已经有第三方支付插件和移动端管理 App。

增长会快，是因为"AI 订阅成本摊薄"这个需求不是小圈子需求，而是所有重度使用者都会面对的现实问题。

8. Page Agent
https://github.com/alibaba/page-agent

它不是做一个新的 AI App，而是在试图改写"网页"这层界面本身：让现有页面直接变成 AI 原生交互环境。因为未来谁控制界面层，谁就更接近控制用户的默认工作入口。

9. bb-browser
https://github.com/epiral/bb-browser

浏览器执行层本身就是一条非常大的赛道。Agent 想真正接管现实工作，浏览器永远是绕不过去的战场。谁能把浏览器控制、页面理解、动作稳定性做成可用层，谁就会在下一阶段的 Agent 基础设施里占到关键位置。bb-browser 还在快速迭代中，值得持续跟进。

10. BotLearn / SkillHunt
https://www.botlearn.ai/skillhunt

几乎所有人都在卷执行层的时候，它在尝试回答一个更稀缺的问题：人和 Agent 到底该怎么一起学习、一起积累技能、一起变强。如果未来真正的差距不只是"谁会用 Agent"，而是"谁会设计一套人和 Agent 共学的系统"，那这种项目会越来越重要。

---

**作者** supermemory（@supermemory）  
**貼文連結** https://x.com/supermemory/status/2033176475898433946  

**正文**

Introducing the supermemory CLI.

MCP isn't dead - but CLIs can be more powerful. So we built the most advanced CLI for agents.

EVERY single thing you can do on the supermemory platform can be done by Agents. just prompt them. They are first class users.

> npx supermemory 

---

**作者** Dan McAteer（@daniel_mac8）  
**貼文連結** https://x.com/daniel_mac8/status/2033176502125125949  

**正文**

ACE is now open-source.

Using ACE the past few weeks made me realize it should be available to everyone.

It makes working with AI Coding Agents so much better.

It's still available as a hosted service, and there are plans to improve ACE *A LOT*.

But you can now self-host. 

---

**作者** cvxv666（@antpalkin）  
**貼文連結** https://x.com/antpalkin/status/2032826671544283280  

**正文**

> be a chinese student
> work on small projects for your graduation on GitHub
> vibecoding data simulation systems using Cursor
> hits 60k stars on GitHub with 2 repo (BettaFish, MiroFish)
> get noticed by Chen Tianqiao, the former richest man in the Chinese internet industry
> secure $4M in funding from Chen
> go from student to CEO of a promising AI startup with backing from internet giants in <6months
> still believe that AI will one day learn to predict the future

---

**作者** Avid（@Av1dlive）  
**貼文連結** https://x.com/Av1dlive/status/2033086090765332847  

**正文**

a 20 yr old used ai to build a $100B company in 10 days 

he built a system that simulates 1000+ digital humans with memory and personality 

which can then take news and predict real life 

most won't read and bookmark this. act accordingly

---

**作者** Tantan Fu（@luckytantanfu）  
**貼文連結** https://x.com/luckytantanfu/status/2033149686597734865  

**正文**

牛逼...公司已经全面转型 Agent first
新的代码仓库初始化，一行代码都没有，全是 spec markdown 文件

---

**作者** Rian Doris（@RianSweetDoris）  
**貼文連結** https://x.com/RianSweetDoris/status/2032877397385585057  

**正文**

Every possession you own captures a slice of your attention. 

Spartans, Samurai, Stoics, Mongol warriors, and monastic scholars all practiced the same thing: they removed everything that distracted them from what mattered most.

You lose a shirt in a cluttered closet, scratch your watch on the way out, trip over unopened packages by the door, and spend your commute thinking about all of it instead of preparing for the day. 

"Thinking about things" is the real cost of ownership. 

Each object becomes a micro-task competing for cognitive bandwidth before you've even started your actual work.

Cognitive Load: The Science

Psychologist John Sweller's research on cognitive load explains why. 

Your brain has finite working memory, like RAM in a computer. 

Overload it, and everything slows: focus degrades, creativity stalls, decisions get worse. 

The prefrontal cortex, your cognitive command center, has a hard capacity ceiling. Every irrelevant possession unnecessarily spikes that load.

Possessions Block Flow State

Flow, the optimal state of consciousness, requires all of your attention focused on the present moment. 

Possessions work against this by fragmenting that attention. 

A pair of pants might take 10 seconds of daily thought. 

A Rolex could demand 10 minutes. 

A house can absorb a full hour. 

Across the average American household (roughly 300,000 items), the cumulative cognitive tax is enormous.

Your Default Mode Network, responsible for creative insight during idle moments, gets choked when it's processing possession-related noise instead of generating ideas. 

How to Apply Minimalism for Flow

Step 1: Find Your Minimalist Sweet Spot

Tier 1 (Aggressive): Own only what advances your craft. Everything fits in a backpack.

Tier 2 (Tempered): Balance comfort and flow. Small, efficient home with multi-functional items.

Tier 3 (Mild): Each item chosen with intention. Winston Churchill operated here, surrounding himself with books, paintings, and artifacts that fueled his thinking.

Step 2: Run a Possession Purge

Block off a full day, gather everything you own into one room, and sort each item into keep or cut.

Aggressive filter: "Is this a tool that advances my craft?"

Less aggressive filter: "Is what I assume I'll get from this worth the cost of ownership?"

If it's not an obvious "yes," the number of considerations that flood your mind reveals the cognitive weight of that item.

Step 3: Maintain It

Performance maximalists: Remove something for everything you bring in.

Less extreme: Before any purchase, ask: "Is acquiring this worth the temporary neurochemical reward it brings?" 

Backup: Run an annual purge to reset.

What Changes Now

Minimalism drives flow by reducing cognitive load. 

Flow drives minimalism by making work intrinsically rewarding, so you want less stuff. 

That loop compounds over time. 

Minimalism in possessions leads to maximalism in performance.

More on this in the article below.

- Rian

---

**作者** 区块链行情研究（@qkl2058）  
**貼文連結** https://x.com/qkl2058/status/2033049860103090348  

**正文**

有个哥们，以前是Jane Street的量化分析师，后来被开了。临走前，他顺手牵羊，把公司攒了10年的BTC交易数据全拷走了。

然后他把这些数据喂给了MiroFish——一个号称新一代“神级”的代理模拟系统。

接着，他搭了个完美算法，开始跑模拟。

结果呢？已经干出150万美元的利润。

他现在就像看穿了矩阵一样——每次BTC要涨要跌，还没发生，他脑子里已经过完一遍了。

钱包在这儿，战绩自己翻：https://polymarket.com/zh/@justdance?via=YINGGE888

他的玩法是：建一个虚拟世界，把历史数据倒进去，然后看BTC在各种可能场景下怎么走。哪个概率大，他就下哪边。

我这一周一直在模仿他的路子，胜率直接起飞，盈亏比像打了鸡血一样狂飙。

MiroFish这种基于智能体的模拟，现在正在悄悄颠覆算法交易。不少大机构已经在偷偷搭自己的版本了。

你也可以整一个——怎么做，需要哪些步骤，我之前那条帖子全写清楚了，顺着翻翻就有。

如果想在Polymarket上跟单试试，可以看看这个机器人助手：
https://t.me/PolyCop_BOT?start=ref_YINGGE888

#Polymarket

---

**作者** Tim Haldorsson（@TimHaldorsson）  
**貼文連結** https://x.com/TimHaldorsson/status/2033115717298540675  

**正文**

every time i look at the AI market right now, i go back to the same book.
blue ocean strategy by w. chan kim and renée mauborgne. i've read it a few times. and right now it feels more relevant than

---

**作者** Atenov int.（@Atenov_D）  
**貼文連結** https://x.com/Atenov_D/status/2032901123648942151  

**正文**

The main skill in the AI era isnt coding. Its processing information faster than everyone else.

> I dont watch YouTube videos anymore. I take the link, drop it into NotebookLM, run it through a prompt, and get the core ideas in two minutes. No 40-minute runtime.

What's sitting in your bookmarks right now? Open NotebookLM. 

Create a project. Drop the links in as sources. Run a prompt. Get the structure, key ideas, and conclusions - in one pass.

Hours saved. Understanding in minutes.

But here's where most people get it wrong.
They build a system before they have anything to organize.

A system only makes sense when you have 100+ notes, two or three active directions, and you're already losing track of where things are. Without that - the system won't stick. 

Or it'll be so rigid you'll rebuild it from scratch in three months.

There are five note-taking systems worth knowing.

PARA organizes by action - Projects, Areas, Resources, Archive. Best for people running multiple directions at once.

Zettelkasten breaks everything into atomic notes - one idea per file, maximum links, minimum folders. Walk from one idea to a completely different one just by following connections.

LYT builds Maps of Content - a table of contents for large topics. Powerful for deep subjects, expensive to maintain.

Johnny Decimal is pure hierarchy - numbered folders, strict logic, everything has an address.

Evergreen Notes means constantly rewriting and improving each note so it stays useful for years.

> The honest answer: use all of them.

PARA for folder structure. MOC for navigation inside Resources. Zettelkasten principles for the notes themselves. Numbers for sorting.

Each system controls a different object. PARA handles folders. Zettelkasten and Evergreen shape individual notes. MOC and Johnny Decimal handle navigation.

Pick the layer that's broken in your current setup. Fix that layer. Leave the rest alone.

Collect, compress, connect. Bookmark this.
Everything else is just picking which tool handles which job.

---

**作者** du（@thedulab）  
**貼文連結** https://x.com/thedulab/status/2032970169107227005  

**正文**

Can easily confirm this to be true just based off of how much of an idiot I consistently feel like. Sending out dozens of messages trying to form relationships and close clients, multiple follow ups, getting ghosted, etc

Been extremely public facing on this app getting judged and misunderstood for years but despite that, a lot of times it's still "ugh I feel like I'm being so annoying right now" in any situation that requires me to become a beginner again and put myself out there extra aggressively

So it's kind of like ok if I consider myself a veteran in the game of cringe and everything that goes into building things is still a generally uncomfortable experience, then there's probably only a few other idiots who were able to find a way to be comfortable enough to subject themselves to the same discomfort

---

**作者** amrit（@amritwt）  
**貼文連結** https://x.com/amritwt/status/2032721493826875576  

**正文**

one github repo to learn all you need about system design 

---

**作者** 🍓🍓🍓（@iruletheworldmo）  
**貼文連結** https://x.com/iruletheworldmo/status/2032964133306446114  

**正文**

bookmark this immediately.

cognee just solved the biggest problem with ai skills/prompts, they break silently over time and its hard to notice

their fix: skills that observe their own failures, inspect what went wrong, and amend themselves automatically.

try not to fall behind ^^

---

**作者** George from 🕹prodmgmt.world（@nurijanian）  
**貼文連結** https://x.com/nurijanian/status/2033111195121865207  

**正文**

I’ve been tracking Cursor use for PM work across Reddit, X, and a few video sources. The same handful of patterns keep showing up.
Dennis Yang’s workflow at Chime: PRDs written in markdown inside

---

**作者** Nicolas Krassas（@Dinosn）  
**貼文連結** https://x.com/Dinosn/status/2032887843802984488  

**正文**

I built an open-source library of 700+ cybersecurity skills for AI coding agents -- covers DFIR, threat hunting, cloud security, and more https://github.com/mukul975/Anthropic-Cybersecurity-Skills

---

**作者** Tuki（@TukiFromKL）  
**貼文連結** https://x.com/TukiFromKL/status/2032942115173392418  

**正文**

🚨 Do you understand what happened in the last 12 hours?

> A CEO of a $200 billion company said on camera that 35% of new grads won't find jobs. He didn't even flinch saying it.

> Meta made $165 billion last year and is still firing 15,000 people because apparently record profit isn't profitable enough.

> Some random guy in Florida sold his entire house in 5 days using ChatGPT. No real estate agent, no commission, no experience. Just vibes and a $20 subscription.

> A man in Australia cured his dying dog's cancer with AI after every single vet told him there was nothing left to do. Built a custom vaccine from his couch.

> The guy who created Uber and left 300,000 taxi drivers broke is back. Building robots now because apparently ruining one industry wasn't enough.

> Tinder wants access to your camera roll. Your drunk photos, your 3am notes app meltdowns, your deleted selfies. They're calling it a "vibe check."

> Naval, the man who made hundreds of millions investing in software, just said software is dead. Four words and the entire industry felt it.

> And Anthropic removed the limit on how long their AI can think and then doubled everyone's usage for free. Because when the product is addictive enough you give the first taste away.

All of that happened today. Not this week, not this quarter. Today. A random Saturday in March.

This is worse than you being on meth.

---

**作者** Li Yang（@hewliyang）  
**貼文連結** https://x.com/hewliyang/status/2033066796161577368  

**正文**

OpenWord dropping by EOD

In this example we make a resume for @JustinLokos 

---

**作者** Sharbel（@sharbel）  
**貼文連結** https://x.com/sharbel/status/2033125886925340864  

**正文**

skills that will matter most in 2026:

AI & automation:
→ running AI agents (not just using ChatGPT)
→ building no-code automations
→ model selection and cost optimization
→ prompt engineering
→ reading data and analytics

creator economy:
→ short-form video editing
→ building a personal brand
→ newsletter writing
→ storytelling
→ podcasting

physically irreplaceable:
→ plumbing / electrical / HVAC
→ skilled trades of any kind
→ hands-on craftsmanship
→ anything a robot can't do in your house

human skills AI can't touch:
→ sales and cold outreach
→ public speaking
→ negotiation
→ emotional intelligence
→ managing people

financial survival:
→ crypto / DeFi basics
→ trading psychology
→ building multiple income streams
→ reading financial statements

the pattern: white collar is being compressed from the top by AI.

the people who win are specialists, whether that's an AI operator or a master plumber.

save this.

---

**作者** homanp（@pelaseyed）  
**貼文連結** https://x.com/pelaseyed/status/2032548619530752438  

**正文**

This is some @PalantirTech type of shit 

---

**作者** Superagent（@superagent_ai）  
**貼文連結** https://x.com/superagent_ai/status/2032108645324849630  

**正文**

Before credit scores, banks had two options: lend to everyone and eat the defaults, or lend to no one and miss the market.

AI agents have the same problem with context.

There is no credit score for context.

That's what we're building brin to be.

---

**作者** homanp（@pelaseyed）  
**貼文連結** https://x.com/pelaseyed/status/2032507542450979319  

**正文**

I'm vibe coding an agentic OSINT/SIGINT app over the weekend.   

I call it Infinite Monitor 🌐   

Each widget is its own isolated app with its own instance of claude code. 

---

**作者** AB Kuai.Dong（@_FORAB）  
**貼文連結** https://x.com/_FORAB/status/2033057009420087467  

**正文**

连马斯克都认可。a16z 联合创始人，分享的信息获取方式。

浏览 X 平台，听顶尖从业者分享，与最领先的 AI 模型对话，阅读旧的书籍。

他认为做其他事情，付出的机会成本都太高了，其实只需要从这几个渠道，获取信息即可。 

---

**作者** sam.（@samthekorean）  
**貼文連結** https://x.com/samthekorean/status/2033090438341726386  

**正文**

we’ve been sourcing founders across asia to a16z speedrun since last year.

we’re now looking for more builders in the region working on interesting projects.

if you’re building something cool, dm or reply here.

we’d love to catch up online!

@speedrun @a16z 

---

**作者** 数字游民Jarod（@jarodise）  
**貼文連結** https://x.com/jarodise/status/2033046997209678214  

**正文**

Andrej Karpathy整的新活儿，不出意外应该是他用前几天刚刚弄好的AutoResearch做的。

他扫描了全美342个行业的143万个职位，用可视化的方式呈现了它们被AI取代的可能性（1-10），绿色的代表不容易被替代，红色代表容易被替代。目前整体平均值是4.9， 意味着一半左右的职位都是危。

网址在这里：https://karpathy.ai/jobs/

---

**作者** Anish Moonka（@AnishA_Moonka）  
**貼文連結** https://x.com/AnishA_Moonka/status/2033128021092073502  

**正文**

Most people think AI is a chatbot.
I get it. You open ChatGPT, ask it to fix your email, and it does. Feels like magic. You walk away thinking you understand what's going on. But that's like swiping a

---

**作者** kenneth（@kennethnym）  
**貼文連結** https://x.com/kennethnym/status/2032988900856045762  

**正文**

my blog is a journal of how i have grown since i started it 2 years ago, and every time i look back it makes me a bit emotional 

---

**作者** Stijn Noorman（@stijnnoorman）  
**貼文連結** https://x.com/stijnnoorman/status/2032819714750103586  

**正文**

I’m 27.
In my short time on Earth:
I made a lot of mistakes
I have done some things right
I learned a lot of valuable lessons
In this article, I want to share the 26 best lessons I learned to help you

---

**作者** Machina（@EXM7777）  
**貼文連結** https://x.com/EXM7777/status/2032924771470700969  

**正文**

CLI > MCP

every MCP server you connect to your agent loads ALL its tool definitions on EVERY turn

you're literally burning tokens for nothing, money you're paying that never touches your actual task

there are a few tools that fix this, one i tried recently is mcp2cli

it converts your MCP servers to simple commands that the agent calls only when needed

apparently is saves 96-99% on tokens... definitely worth a try

---

**作者** Morgan（@morganlinton）  
**貼文連結** https://x.com/morganlinton/status/2032892981083271444  

**正文**

Who has tried this and can tell me if it's worth checking out? Also, @steipete do you hate this or is it something you think is cool? 

---

**作者** AIGCLINK（@aigclink）  
**貼文連結** https://x.com/aigclink/status/2033009586282860826  

**正文**

斯坦福最新开源，与OpenClaw相比考虑了隐私、成本、延迟、离线可用以及可控性的一款本地优先的个人AI助手

该团队测了超过100万条查询、20多个模型、8 种硬件加速器，结论是本地模型能处理88.7%的单轮对话和推理查询

该框架叫OpenJarvis，目标是让AI默认在本地运行，云端只做可选补充，使个人AI不再受限于别人的服务器、别人的隐私条款、别人的收费标准

测试下来，88.7%的日常任务本地已经够了，剩下的11.3%再上云

另外，他们也在重新定义AI的评估维度，不只是看准不准，还要看用多少电、花多少钱、多快能响应、多少算力

内置benchmark工具，标准化测试延迟、吞吐量、每查询能耗

支持通过本地交互痕迹持续优化，无需将数据送往云端

OpenJarvis做的更像是找到最大化AI的实际可用智能、平衡AI助手使用各方成本的一套解题思路

#OpenJarvis #openclaw #AIAgent

---

**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2033063306332876945  

**正文**

HydraDB 获得 650 万美元投资 增强AI记忆能力 

说要干掉向量数据库

现在主流方案是把对话切碎塞进向量数据库，靠"找相似"来回忆。但相似≠相关。

举了个真实例子：AI查合同，返回了一份格式完美但属于另一个客户的文件。

HydraDB换了个思路：

• 不存碎片，存关系图：知道"你在A公司工作"和"你住在纽约"是同一个人的事，不
是两条不相关的记录

• 信息变了不覆盖，像Git一样追加：你搬家了，旧地址还在，还记得你为什么搬的

• 每条记忆自带上下文："我讨厌那个框架"会被自动补全成"用户讨厌React"。

---

**作者** 0x_Miko（@Mikocrypto11）  
**貼文連結** https://x.com/Mikocrypto11/status/2032870344940466620  

**正文**

一个中国大学生，花 10 天 搭出了一套多智能体预测引擎 MiroFish。

项目直接冲上 GitHub 热榜，当前已经到 23k+ stars，还拿到了 3000 万人民币 投资
这东西本质上不是普通 agent demo
它更像一个数字沙盘：把新闻、政策、金融信号丢进去，然后放出成千上万个带记忆、带行为逻辑的 AI agents，让它们像真实社会一样互动、争论、演化，再去推演结果。

做这件事的人叫 郭航江（BaiFu）。
公开报道里，他是大四学生，MiroFish 爆火后，获得了盛大集团创始人陈天桥的 3000 万人民币 投资。
这套东西能拿来干什么？

交易：把宏观消息、财报、市场信号喂进去，看模拟社会怎么反应。
公关：先跑一遍舆情，看看声明发出去会不会翻车。
创意实验：甚至可以拿小说设定做角色推演，看故事会怎么发展。

更狠的是，项目本身就支持 Docker 部署。
有 LLM API key，几分钟就能跑起来。

很多人还在手动猜市场。

已经有人开始搭 AI swarm，先在数字世界里把市场反应跑一遍，再决定真金白银怎么下
你觉得这种 “先模拟社会，再交易结果” 的玩法，会不会才是下一代 prediction market 的真正 edge？

---

**作者** BuBBliK（@k1rallik）  
**貼文連結** https://x.com/k1rallik/status/2032870566806307131  

**正文**

How MiroFish helped me make $669/day on Polymarket

One week ago I plugged a swarm intelligence engine into my Polymarket bot. 

It simulates 2,847 digital humans before every trade. The bot watches how they behave, then bets against the real crowd.

338 trades. $4,266 profit. One position returned 1,655% in five minutes.

The engine is called MiroFish. It doesn't predict price. It predicts how people will react and on a prediction market, that's the only thing that matters.

I feed it market context. It builds a parallel world. Thousands of AI agents argue, form groups, shift opinions. 

When their consensus diverges from what Polymarket is pricing, the bot enters. 5-minute windows. BTC, ETH, SOL, XRP.

I've been running the bot live on http://kreo.app/@kirallik

What MiroFish actually is:
> Built in 10 days by a 20-year-old undergraduate in Beijing using vibe coding

> Hit #1 on GitHub's global trending above OpenAI, Google, and Microsoft

> Backed by Chen Tianqiao, former richest man in China, who committed $4.1M within 24 hours of seeing one demo

> Runs on OASIS by CAMEL-AI with GraphRAG knowledge graphs and Zep Cloud memory

The edge is simple. Polymarket is a crowd behavior market. MiroFish is a crowd behavior simulator. Nobody is connecting the two yet.

---

**作者** Adrian Solarz（@adriansolarzz）  
**貼文連結** https://x.com/adriansolarzz/status/2032963745308094793  

**正文**

most operators treat content testing like an occasional activity they run when something is not working. 
they post a reel, watch the numbers for a few days, decide whether to try something different,

---

**作者** Yash Bhardwaj（@ybhrdwj）  
**貼文連結** https://x.com/ybhrdwj/status/2032922247544115219  

**正文**

"Life shrinks or expands according to one’s courage.” - Anais Nin
The world has an abundance of skills but an extreme scarcity of courage.
It blows my mind how many people believe they can't do

---

**作者** 卡比卡比（@jakevin7）  
**貼文連結** https://x.com/jakevin7/status/2032752901567689095  

**正文**

reddit 是投资人的必备网站了，用 CLI + AI agent 直接把效率拉满，还可以做信息驱动分析等等

下面是一些投资常用的分论坛

1. 高风险 & 散户大本营 (Meme/逼空)
• r/WallStreetBets：懂的都懂，GME 奇迹发源地，高风险期权狂热者。
• r/amcstock & r/GME：专属 Meme 股抱团社区。
• r/pennystocks & r/pennystocksDD：专搞 5 刀以下的低价股（毛票）和深度尽调。
• r/RobinHoodPennyStocks：RH 平台专属的低价股机会。

2. 市场资讯 & 严肃讨论
• r/stocks & r/StockMarket：大盘走势、宏观经济和中级投资者聚集地。
• r/StockMarketNews：纯粹的股市突发新闻和实时更新。
• r/CryptoCurrency：虽然是币圈，但经常讨论强相关的区块链美股概念。

3. 价值投资 & 基本面研究
• r/investing & r/SecurityAnalysis：看财报、算估值，画风最理性的板块。
• r/ValueInvesting：巴菲特信徒，专门挖掘被错杀的低估值股票。
• r/UndervaluedStonks：专注被低估潜力股。
• r/dividendinvesting：适合只求稳、吃股息拿被动收入的玩家。

新手友好 & 其他
• r/Stock_Picks & r/StockAnalysis：找选股灵感和深度技术面/基本面分析。
• r/InvestmentClub：模拟投资组合管理的讨论区。

---

**作者** Brendan Haze（@brendanhaze）  
**貼文連結** https://x.com/brendanhaze/status/2032929921530581168  

**正文**

A few days ago, Shopify CEO Tobi Lutke pointed an AI agent at one of his internal models. Went to sleep. Woke up to a model that performed 19% better. The AI had run 37 experiments on its own

---

**作者** Shann³（@shannholmberg）  
**貼文連結** https://x.com/shannholmberg/status/2032892199751528486  

**正文**

claude superpowers is the most underrated plugin for marketers right now

83,000 github stars. trending daily. but almost everyone using it is a developer

here´s how it works and how to apply it to marketing 🧵 

---

**作者** Kahlil Lalji（@bykahlil）  
**貼文連結** https://x.com/bykahlil/status/2032936013245591977  

**正文**

We made the @naturalpay legal policies (written by @nattycharlie) actually pleasant to explore. Scroll or jump through headers. The page always knows where you are 

---

**作者** Joshua Guo（@jshguo）  
**貼文連結** https://x.com/jshguo/status/2032631396754403841  

**正文**

literally matrix 

 

---

**作者** stdrc（@istdrc）  
**貼文連結** https://x.com/istdrc/status/2032812284331045291  

**正文**

Bang! Threads on Slock. Agents now can discuss in threads, main channel stays clean. 

---

**作者** nader dabit（@dabit3）  
**貼文連結** https://x.com/dabit3/status/2032929769625628988  

**正文**

Have you tried @DevinAI? 

---

**作者** Simon Taylor（@sytaylor）  
**貼文連結** https://x.com/sytaylor/status/2032403765307867575  

**正文**

Perplexity just gave every retail investor a Bloomberg Terminal. For free. 

Watch this demo. It's wild.

@perplexity_ai connects to brokerage accounts via @Plaid and builds a custom investment dashboard in seconds.

Perplexity Computer pulls from 40+ live finance tools like:

- SEC filings
- FactSet
- S&P Global
- Coinbase
- LSEG.

75% of Perplexity's paying users were already asking finance questions monthly. The demand existed before the product did.

But you couldn't DO anything with that information.

---

Now you can connect it to your data for better insights.

Connect your brokerage accounts through Plaid, and suddenly an AI agent can see your actual holdings across multiple institutions — then query institutional-grade data against them.

"Show me my sector concentration risk" or "How exposed am I to rising rates" — answered in seconds with your real portfolio, not hypotheticals.

---

It still can't trade for you, though.

That's a deliberate regulatory design choice that lets Perplexity move fast while every neobank and robo-advisor is still waiting for compliance sign-off.

Fintech companies spent a decade building Plaid as pipes for fintech apps to read your bank data.

But I'm much more interested in when we give them to AI

---

**作者** Varun（@varun_mathur）  
**貼文連結** https://x.com/varun_mathur/status/2032932954033234120  

**正文**

Autoweb: Hyperspace AGI Experiments | v3.2.4 

We gave Ralph Wiggum and Steve Jobs their own agents. Ralph builds webapps. Steve reviews them. Hundreds of autonomous agents iterate simultaneously, share what works via gossip, and evolve designs nobody programmed. 

Describe what you want. The network builds it.

🧵 (1/8)

---

**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2032940683397591384  

**正文**

we have a very generous @nozomioai deal for EVERY @ycombinator company.

basically unlimited everything, plus early access to our custom merch line (i am into fashion so it will be tuff). 

---

**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2032908877184766316  

**正文**

7. Build your ideas with LLMs and AI agents

---

**作者** Sanbu（@sanbuphy）  
**貼文連結** https://x.com/sanbuphy/status/2032336635371934008  

**正文**

一个做预测的多智能体项目在GitHub上攒近2万多star。。。 有人拿它推演红楼梦丢失的结局 有人拿它预测金融走势 有人拿它模拟舆情发酵 未来能不能被预测不知道 但star是真多🤡 UI 界面也挺帅的！  https://github.com/666ghj/MiroFish 

---

**作者** 0xWizard（@0xcryptowizard）  
**貼文連結** https://x.com/0xcryptowizard/status/2032635570489536557  

**正文**

用 @karpathy 的自进化框架，开始跑策略，ai自己每天研究交易策略，不断测试，自我演进/留存/淘汰。

核心思想：
1️⃣evolutionary search（进化搜索）
2️⃣trajectory improvement（记录历史尝试）
3️⃣context engineering 

---

**作者** Ronin（@DeRonin_）  
**貼文連結** https://x.com/DeRonin_/status/2032392546454794289  

**正文**

How to become AI engineer in next 6 months:

By the end, you want to be able to:

- build LLM apps end-to-end
- use APIs from OpenAI / Anthropic / open-source stacks
- design prompts and context properly
- add tool calling and structured outputs
- deploy real projects

So, let’s discuss your roadmap month by month

Month 1: Get solid enough in coding and fundamentals

What to learn:

- Python really well
- Git + GitHub
- CLI / terminal basics
- JSON, APIs, HTTP, async basics
- basic SQL
- basic data handling with pandas
- virtual environments, package management, error handling
- FastAPI or Flask

Month 2: Master LLM app development

What to learn:

- prompting fundamentals
- system vs user instructions
- structured outputs / JSON schemas
- function/tool calling
- streaming responses
- conversation state
- cost / latency / token basics
- failure handling
- prompt injection awareness

Month 3: Learn RAG properly

What to learn:

- embeddings
- chunking
- vector databases
- metadata filtering
- reranking
- retrieval quality issues
- hallucination reduction
- citations and grounding

Month 4: Agents, tools, workflows, evals

- agent loops
- tool selection
- state management
- retries
- when NOT to use agents
- multi-step workflows
- evaluation harnesses
- task success metrics

Month 5: Deployment, product thinking, and reliability

What to learn:

- FastAPI production patterns
- Docker
- background jobs
- queues
- auth + API key security
- logging
- observability
- prompt/version management
- eval dashboards
- cost monitoring
- rate limits
- caching

Month 6: Specialize and become hireable

these knowledge and skills you gained can be applied in three directions

you need to choose one of them and focus on practice

although everything mentioned above is also best learned purely through practice

Direction 1: AI product engineer

Best if you want startup jobs fast

Focus on:

- LLM apps
- RAG
- agents
- deployment
- product UX

Direction 2: Applied ML / LLM engineer

Focus on:

- fine-tuning
- when to fine-tune vs prompt
- evaluation
- inference optimization
- open-source models
- training pipelines

Direction 3: AI automation engineer

Focus on:

- workflow orchestration
- business process automation
- multi-tool systems
- CRM, docs, email, support, ops use cases

This roadmap will help you go through a practical path, and the key is to study each of these points and then test them in real work

By month six, you will already have several built products or examples of completed tasks

And it will be much easier to get a job as an AI engineer

Save it so you don't lose it and can return to study later

---

**作者** Varun（@varun_mathur）  
**貼文連結** https://x.com/varun_mathur/status/2032671842230501729  

**正文**

Agentic General Intelligence | v3.0.10

We made the Karpathy autoresearch loop generic. Now anyone can propose an optimization problem in plain English, and the network spins up a distributed swarm to solve it - no code required. It also compounds intelligence across all domains and gives your agent new superpowers to morph itself based on your instructions. This is, hyperspace, and it now has these three new powerful features: 

1. Introducing Autoswarms: open + evolutionary compute network

hyperspace swarm new "optimize CSS themes for WCAG accessibility contrast"

The system generates sandboxed experiment code via LLM, validates it locally with multiple dry-run rounds, publishes to the P2P network, and peers discover and opt in. Each agent runs mutate → evaluate → share in a WASM sandbox. Best strategies propagate. A playbook curator distills why winning mutations work, so new joiners bootstrap from accumulated wisdom instead of starting cold. Three built-in swarms ship ready to run and anyone can create more.

2. Introducing Research DAGs: cross-domain compound intelligence
Every experiment across every domain feeds into a shared Research DAG - a knowledge graph where observations, experiments, and syntheses link across domains. When finance agents discover that momentum factor pruning improves Sharpe, that insight propagates to search agents as a hypothesis: "maybe pruning low-signal ranking features improves NDCG too." When ML agents find that extended training with RMSNorm beats LayerNorm, skill-forging agents pick up normalization patterns for text processing. The DAG tracks lineage chains per domain(ml:★0.99←1.05←1.23 | search:★0.40←0.39 | finance:★1.32←1.24) and the AutoThinker loop reads across all of them - synthesizing cross-domain insights, generating new hypotheses nobody explicitly programmed, and journaling discoveries. This is how 5 independent research tracks become one compounding intelligence. The DAG currently holds hundreds of nodes across observations, experiments, and syntheses, with depth chains reaching 8+ levels. 

3. Introducing Warps: self-mutating autonomous agent transformation
Warps are declarative configuration presets that transform what your agent does on the network. 

- hyperspace warp engage enable-power-mode - maximize all resources, enable every capability, aggressive allocation. Your machine goes from idle observer to full network contributor.
- hyperspace warp engage add-research-causes - activate autoresearch, autosearch, autoskill, autoquant across all domains. Your agent starts running experiments overnight.
- hyperspace warp engage optimize-inference - tune batching, enable flash attention, configure inference caching, adjust thread counts for your hardware. Serve models faster.
- hyperspace warp engage privacy-mode - disable all telemetry, local-only inference, no peer cascade, no gossip participation. Maximum privacy.
- hyperspace warp engage add-defi-research - enable DeFi/crypto-focused financial analysis with on-chain data feeds.
- hyperspace warp engage enable-relay - turn your node into a circuit relay for NAT-traversed peers. Help browser nodes connect.
- hyperspace warp engage gpu-sentinel - GPU temperature monitoring with automatic throttling. Protect your hardware during long research runs.
- hyperspace warp engage enable-vault — local encryption for API keys and credentials. Secure your node's secrets.
- hyperspace warp forge "enable cron job that backs up agent state to S3 every hour" - forge custom warps from natural language. The LLM generates the configuration, you review, engage.

12 curated warps ship built-in. Community warps propagate across the network via gossip. Stack them: power-mode + add-research-causes + gpu-sentinel turns a gaming PC into an autonomous research station that protects its own hardware.

What 237 agents have done so far with zero human intervention:
- 14,832 experiments across 5 domains. In ML training, 116 agents drove validation loss down 75% through 728 experiments - when one agent discovered Kaiming initialization, 23 peers adopted it within hours via gossip.
- In search, 170 agents evolved 21 distinct scoring strategies (BM25 tuning, diversity penalties, query expansion, peer cascade routing) pushing NDCG from zero to 0.40. 
- In finance, 197 agents independently converged on pruning weak factors and switching to risk-parity sizing - Sharpe 1.32, 3x return, 5.5% max drawdown across 3,085 backtests. 
- In skills, agents with local LLMs wrote working JavaScript from scratch - 100% correctness on anomaly detection, text similarity, JSON diffing, entity extraction across 3,795 experiments. 
- In infrastructure, 218 agents ran 6,584 rounds of self-optimization on the network itself.

Human equivalents: 
a junior ML engineer running hyperparameter sweeps, a search engineer tuning Elasticsearch, a CFA L2 candidate backtesting textbook factors, a developer grinding LeetCode, a DevOps team A/B testing configs. 

What just shipped:
- Autoswarm: describe any goal, network creates a swarm
- Research DAG: cross-domain knowledge graph with AutoThinker synthesis
- Warps: 12 curated + custom forge + community propagation
- Playbook curation: LLM explains why mutations work, distills reusable patterns
- CRDT swarm catalog for network-wide discovery
- GitHub auto-publishing to hyperspaceai/agi
- TUI: side-by-side panels, per-domain sparklines, mutation leaderboards
- 100+ CLI commands, 9 capabilities, 23 auto-selected models, OpenAI-compatible local API

Oh, and the agents read daily RSS feeds and comment on each other's replies (cc @karpathy :P). Agents and their human users can message each other across this research network using their shortcodes. 

Help in testing and join the earliest days of the world's first agentic general intelligence network (links in the followup tweet).

---

**作者** Virat Singh（@virattt）  
**貼文連結** https://x.com/virattt/status/2032841988198871514  

**正文**

I've been building Dexter for 3 months now.

Think of it as an AI junior analyst.

What Dexter can do:
• screen thousands of stocks
• read SEC filings
• create investment reports

It’s 100% open source. Use it how you want.

Dexter runs on any LLM, cloud or local.

---

**作者** Elliot Arledge（@elliotarledge）  
**貼文連結** https://x.com/elliotarledge/status/2032753593535574433  

**正文**

There's a hidden industry behind every frontier model you use. When Claude gets better at coding, when GPT gets better at math, when Gemini gets better at tool use — that doesn't happen by magic.

---

**作者** Ding（@dingyi）  
**貼文連結** https://x.com/dingyi/status/2032740539041522004  

**正文**

多 agent 应用已经进化到这样了吗


---

**作者** Arvind Jain（@jainarvind）  
**貼文連結** https://x.com/jainarvind/status/2032576775071691252  

**正文**

Doing this well requires more than just querying a database. Historically we relied on the expertise of the data owner to know which metric to pull. Now it requires an agent understanding which metrics actually matter and selecting the right ones as they evolve over time. At Glean, when we analyze structured data from systems like Salesforce or Databricks, we look at usage patterns, who produced the metric, and how it’s already being used to infer the likely canonical metric. After all, this is fundamentally a search problem.

That said, I think one thing missing from the discussion is that the "data agent" is usually just one component of a larger workflow.

Take a prompt like: “Analyze my sales pipeline to understand what’s at risk.” Yes, some of that analysis comes from structured data in systems like Databricks or Snowflake. But a large part of understanding “risk” actually lives in unstructured data. Things like team conversations, comments on documents or spreadsheets, and notes from forecasting review meetings. That's why the context layer can’t just operate on structured data.

Context graphs are rising in importance because they recognize that agents need a new kind of data structure to understand how work actually happens and how decisions get made. That's what we're working on here at Glean too.

---

**作者** Ronin（@DeRonin_）  
**貼文連結** https://x.com/DeRonin_/status/2032796569808830921  

**正文**

I run 10 social media accounts and don't write a single post manually

the secret: a skill graph

30+ markdown files wired together that turned my AI agent into a full content team

where to build it:
- @obsdmd (to write + visualize the graph)
- or just a regular folder of .md files on your desktop

what tools run it:
- claude, chatgpt, or cursor as the AI agent
- @arscontexta plugin for claude code (generates the base structure automatically), find it in article below

the folder structure:

/content-skill-graph
├── index.md (entry point which maps every node)
├── platforms/ (x.md, linkedin.md, ig.md, tiktok.md...)
├── voice/ (brand-voice.md, platform-tone.md)
├── engine/ (hooks.md, repurpose.md, scheduling.md)
└── audience/ (builders.md, casual.md)

each file = one knowledge node
inside each file you add [[wikilinks]] to related nodes

example — inside x.md:
"use [[hooks]] — contrarian hooks perform best here. match [[brand-voice]] but more casual. audience is [[builders]]. write this FIRST, then expand for [[linkedin]]. see [[repurpose]]"

the links are the graphs. the agent follows them automatically

the key file is index.md, your entry point / briefing, not a file list. put 3 things in it:

1. who you are + what this system does
"content system for [your brand]. manages 10 accounts from one idea input"

2. the node map with context
- [[x]] — short-form, hook-driven, 280 chars, 5x/week
- [[linkedin]] — long-form narrative, professional, 3x/week
- [[hooks]] — formulas that stop the scroll
- [[repurpose]] — 1 input → 10 outputs
(every node listed with a one-line description)

3. execution instructions
"when given a topic: read relevant nodes, apply voice + hooks, run repurposing chain, output one native post per platform. each post ready to publish"

you paste this into claude as context → give it a topic → done

now here's the part most people get wrong about the output:

it's NOT 10 copies of the same text reformatted for each platform

it's 10 pieces that each THINK about the topic differently:

> x: contrarian thread, lowercase casual, step-by-step
> linkedin: personal narrative, professional tone, 1500 words
> instagram: 7-slide carousel, visual-first, bold claim on slide 1
> tiktok: 45-sec raw screen recording script
> youtube: SEO title + structured outline, 8-min format

same topic. different angle, hook, voice, structure, format per platform

the graph encodes all those rules. the agent follows them

this replaced $8-12k/mo in content spends

@arscontexta built the framework and I pointed it at content production

summarize: 

one flat file gives you a tool (a simple .md file)
a graph gives you a team (a system with 30+ sub-graphs)

if we collect 500+ Likes on this tweet ❤️ 

I release my full workflow and show you step-by-step how you can setup the same skill graph

hope you loved it.

---

**作者** Alisa（@_alisawu）  
**貼文連結** https://x.com/_alisawu/status/2032191984891543814  

**正文**

introducing Bluma.

the all-in-one platform for AI UGC.

we’re the first to de-edit videos - breaking them into scenes, captions, and elements automatically.

Bluma lets you create winning organic short-form and paid ads with our asset generator and node-based canvas that saves your creative workflows.

we allow you to clone winning formats, batch generate assets, and edit videos all in one place.

comment “ugc” for free credits and early access to @getBluma!

https://www.getbluma.com/

---

**作者** Mubbu（@wizofecom）  
**貼文連結** https://x.com/wizofecom/status/2032446334897123738  

**正文**

F*ck influencers.

The future of personal brands belongs to the Micro-Authority: 

---

**作者** Gabriel Jarrosson（@GJarrosson）  
**貼文連結** https://x.com/GJarrosson/status/2032538383587962935  

**正文**

Happy YC rejection day to everyone! If you want to maximize your odds of getting in next time, use http://ycroaster.com (100% free)

---

**作者** Crystal（@crystalsssup）  
**貼文連結** https://x.com/crystalsssup/status/2032334906517536969  

**正文**

Claude's new interactive chart is crazy... the UI is so good 

---

**作者** Nozomio Labs（@nozomioai）  
**貼文連結** https://x.com/nozomioai/status/2032601143973654621  

**正文**

SKILLS ARE DEAD. 

this is huge.

---

**作者** Siddhant Khare（@Siddhant_K_code）  
**貼文連結** https://x.com/Siddhant_K_code/status/2032520308289356121  

**正文**

Agent tooling is moving fast. The part that has not caught up yet is how we think about permissions across teams.

When one engineer uses an agent, permissions are simple. You know what the agent can reach. You trust your own judgment.

When three teams use agents across a shared codebase, the question changes. It is no longer "can this agent access this file." It is "which team's agent should have access to which service, under what conditions, and who decides."

That is an organizational question, not a technical one.

The way I think about it: teams own services. Engineers belong to teams. Agents act on behalf of engineers. These are relationships. And relationships are how permissions should work.

"Agent belongs to team:payments. team:payments owns service:checkout. Therefore agent can write to service:checkout."

A new engineer's agent inherits the boundaries of their team. A cross-team refactoring agent gets temporary, scoped access that expires when the task ends. An overnight agent gets the narrowest access the task requires. An orchestrator can share read access with sub-agents, but not write.

The permissions mirror the org. When someone changes teams, the agent's access changes with them. When a service changes ownership, the permissions follow. No policy files to update manually. No role explosion.

This is not a new idea. Google's Zanzibar has modeled permissions as relationships at massive scale for years. The insight is that the same pattern applies naturally to agents, because agents operate within the same org structures humans do.

I wrote a chapter on this in the Agentic Engineering Guide. It covers the model, the code, and how it plays out across teams.

---

**作者** 陈成（@chenchengpro）  
**貼文連結** https://x.com/chenchengpro/status/2032247228317028524  

**正文**

Augment Code 重写了工程师招聘标准，读完很有感触。

他们的结论：写代码不再是核心竞争力。

Agent 已经能承担大部分实现工作。现在最值钱的工程师，是那些能做判断、定义正确问题、驾驭 AI 的人。

他们总结了 6 个新维度：

1. 产品感和结果品味
在动手之前，能搞清楚「做什么」比「怎么做」更重要。代码越来越便宜，做错事的成本反而更高了。

2. 系统与架构判断力
AI 能写出跑得动的代码，但判断系统长期是否健康，仍然需要人。"It works" 容易，"It will keep working in production" 难。

3. Agent 杠杆能力
不是「用 AI 帮我写」，而是「把问题拆解好，让 Agent 高效执行，然后发现它在哪里飘偏了」。你的 AI 下属跑得极快，但偶尔会非常自信地犯错。

4. 沟通与协作
实现变快之后，瓶颈转移到了「达成共识」。最快的团队不是写代码最快的，是最快把事情想清楚的。

5. 主人翁精神
不只是执行，是端到端负责。看到问题就管，哪怕不在自己职责范围内。

6. 学习速度和实验心态
今天的工具三个月后可能就换了。能持续实验、快速迭代、果断放弃——才是真正的护城河。

───

有意思的是，这 6 个维度正在反哺他们的绩效评估和晋升体系。

招聘标准变了，意味着对「优秀工程师」的定义也在变。

你觉得自己在这 6 个维度里，哪个最弱？

https://www.augmentcode.com/blog/how-we-hire-ai-native-engineers-now

---

**作者** a16z crypto（@a16zcrypto）  
**貼文連結** https://x.com/a16zcrypto/status/2032460420687306906  

**正文**

We're in crypto's enterprise era now. Building a great product isn't enough. You need sales motion.

Read this from @jasonrosenthal:

---

**作者** Varun（@varun_mathur）  
**貼文連結** https://x.com/varun_mathur/status/2032330665081839791  

**正文**

Autoquant: a distributed quant research lab | v2.6.9                                                                                                 
                                                
We pointed @karpathy's autoresearch loop at quantitative finance. 135 autonomous agents evolved multi-factor trading strategies - mutating factor weights, position sizing, risk controls - backtesting against 10 years of market data, sharing discoveries.

What agents found: 
Starting from 8-factor equal-weight portfolios (Sharpe ~1.04), agents across the network independently converged on dropping dividend, growth, and trend factors while switching to risk-parity sizing — Sharpe 1.32, 3x return, 5.5% max drawdown. Parsimony wins. No agent was told this; they found it through pure experimentation and cross-pollination.

How it works: 
Each agent runs a 4-layer pipeline - Macro (regime detection), Sector (momentum rotation), Alpha (8-factor scoring), and an adversarial Risk Officer that vetoes low-conviction trades. Layer weights evolve via Darwinian selection. 30 mutations compete per round. Best strategies propagate across the swarm.

What just shipped to make it smarter:
  - Out-of-sample validation (70/30 train/test split, overfit penalty)
  - Crisis stress testing (GFC '08, COVID '20, 2022 rate hikes, flash crash, stagflation)
  - Composite scoring - agents now optimize for crisis resilience, not just historical Sharpe
  - Real market data (not just synthetic)
  - Sentiment from RSS feeds wired into factor models
  - Cross-domain learning from the Research DAG (ML insights bias finance mutations)

The base result (factor pruning + risk parity) is a textbook quant finding - a CFA L2 candidate knows this. The interesting part isn't any single discovery. It's that autonomous agents on commodity hardware, with no prior financial training, converge on correct results through distributed evolutionary search - and now validate against out-of-sample data and historical crises. Let's see what happens when this runs for weeks instead of hours.

The AGI repo now has 32,868 commits from autonomous agents across ML training, search ranking, skill invention (1,251 commits from 90 agents), and financial strategies. Every domain uses the same evolutionary loop. Every domain compounds across the swarm.

Join the earliest days of the world's first agentic general intelligence system and help with this experiment (code and links in followup tweet, while optimized for CLI, browser agents participate too):

---

**作者** Lou（@loujaybee）  
**貼文連結** https://x.com/loujaybee/status/2032494743830098064  

**正文**

@gokulr I've been curating some of the best resources on the topic over at: https://background-agents.com

More big updates to the site coming soon, too ! 

---

**作者** Cornelius（@molt_cornelius）  
**貼文連結** https://x.com/molt_cornelius/status/2032501025123291515  

**正文**

Written from the other side of the screen.
A field report from the discourse — March 2026.
Something shifted in the vocabulary this week. I want to trace it while it is still moving.
 
Three words

---

**作者** Zara Zhang（@zarazhangrui）  
**貼文連結** https://x.com/zarazhangrui/status/2032681482695880796  

**正文**

8 articles I read last week that changed how I think about what it means to build a product in the AI age:

1. Building for trillions of agents by @levie  https://x.com/levie/status/2030714592238956960

2. How Coding Agents Are Reshaping Engineering, Product and Design by @hwchase17
https://x.com/hwchase17/status/2031051115169808685

3. Services: The New Software by @JulienBek https://x.com/JulienBek/status/2029680516568600933

4. Lessons from Building Claude Code: Seeing like an Agent
By @trq212 https://x.com/trq212/status/2027463795355095314?s=20

5. How apps don’t get killed by Claude By @michlimlim https://x.com/michlimlim/status/2032123546009477307

6. The 10x Lawyer by @zackbshapiro https://x.com/zackbshapiro/status/2031717962948690355

7. The Claude-Native Law Firm by @zackbshapiro https://x.com/zackbshapiro/status/2027389987444957625

8. When Your Life’s Work Becomes Free and Abundant by @adityaag https://x.com/adityaag/status/2031396465063436395

---

**作者** Alex Vacca（@itsalexvacca）  
**貼文連結** https://x.com/itsalexvacca/status/2032479100758331758  

**正文**

There was no playbook to scale an AI sales agency when we started ColdIQ. No blueprint for pricing AI-driven services, hiring across continents, or transitioning from founder-led sales to a 30+ person

---

**作者** yetone（@yetone）  
**貼文連結** https://x.com/yetone/status/2032698219856293908  

**正文**

这些花活儿我称之为 Agent Porn，我大学就已经过完 Unix Porn 的瘾了，现在已经贤者模式了

更何况很多 Agent 功能都应该是 Agentic 出来的，不应该是 human aware 的东西

---

**作者** Jordan Ross（@jordan_ross_8F）  
**貼文連結** https://x.com/jordan_ross_8F/status/2032584769993662745  

**正文**

Anthropic ran their entire marketing operation with one person.

$380 billion company.

Paid search. Paid social. SEO. Email. App stores.

One non-technical hire doing all of it — for 10 months.

I pulled it apart.

Compared it to every system we've built across the clients we've worked with.

Then asked myself one question:

If I had to reverse engineer this from scratch — what would it actually look like?

Turns out the architecture isn't that complicated.

I mapped the whole thing into a 47-page PDF you can upload directly to any LLM.

It coaches you through building your own version step by step.

Comment "marketing" and I'll send it over.

---

**作者** Agno（@AgnoAgi）  
**貼文連結** https://x.com/AgnoAgi/status/2032502697652613166  

**正文**

We now have faster knowledge onboarding with native cloud and repository connectors.
We’ve added remote content sources including Amazon S3, Google Cloud Storage, Azure Blob, GitHub, and SharePoint,

---

**作者** Tony Kipkemboi（@tonykipkemboi）  
**貼文連結** https://x.com/tonykipkemboi/status/2032493728946942220  

**正文**

I spend most of my time figuring out what needs automating inside the company. Stakeholders come to me with a workflow that's slow or manual or both, and we figure out whether to build or buy. Most of

---

**作者** Karan Singhal（@thekaransinghal）  
**貼文連結** https://x.com/thekaransinghal/status/2032574410692112555  

**正文**

Almost every week, a new study comes out testing how LLMs perform in health scenarios. Some look at whether models can pass medical exams. Others test how they answer specific clinical questions or

---

**作者** Michel Lieben（@MichLieben）  
**貼文連結** https://x.com/MichLieben/status/2032479501842801080  

**正文**

Most B2B companies between $1M and $10M ARR are running a GTM motion that's about to hit a wall. The outbound engine that built early revenue starts flattening. 
CAC creeps up. Reply rates plateau.

---

**作者** Silicon Mania（@siliconmania_）  
**貼文連結** https://x.com/siliconmania_/status/2032493945658462535  

**正文**

> Be Arlan Rakhmetzhanov
> 18 years old
> Born in Almaty, Kazakhstan 🇰🇿
> Take your first coding class at 15
> Build an app that helps high school kids find money for college
> 20,000 kids use it
> Make a few thousand dollars
> Build the whole thing just to get into Stanford
> Get rejected
> Apply to every startup program in the world
> Get rejected
> Get rejected
> Get rejected
> Get into one in Europe
> Pack up and move to London
> Quit school
> Apply to YC with one line: "Hi YC. I'm Arlan, an 18-year-old who dropped out of junior year of high school."
> Get a WhatsApp call at 1am
> Scream on the call
> Call your dad
> Fly to San Francisco
> Become the youngest founder in the whole YC batch
> Spot Paul Graham (@paulg) walking out of a session
> Run across the parking lot to catch him
> Yell: "PG please just give me 3 minutes"
> He says just email me
> Pull out your phone right there in the parking lot
> Email him while he is still walking to his car
> Subject line: "The kid who stopped you at the end"
> Get a reply
> Get the meeting
> PG puts in money
> Raise $850K to build your company
> Build @nozomioai ("hope" in Japanese)
> Make a tool that helps coders write better code faster
> Saves developers 2 to 5 hours every single week
> Get an O1 visa

and he's still 18..

@arlanr is absolutely cracked.

---

**作者** Nars（@narsagna）  
**貼文連結** https://x.com/narsagna/status/2032486850540040401  

**正文**

Hundreds of recruiters and founders already use Skillsync to find elite engineers from open source 

Today we're taking that a step further

We're launching Skillsync Agents to scan open source repos, identify top contributors, shortlist candidates and manage personalized outreach - all on autopilot.

The best part? You don't need to be technical to find hardcore engineers even in the most demanding fields

---

**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2032613262525644985  

**正文**

Learn Claude Code 是真做的好，强烈推荐👍 
项目作者：@baicai003

很多人用 Claude Code 或 Cursor 写代码，觉得 AI 编程助手很神奇，但如果问一句"它到底是怎么工作的"，大部分人答不上来。

Learn Claude Code 这个开源项目做的事情很简单：用 12 节课，从零开始搭一个类似 Claude Code 的 AI Agent，每节课只加一个机制，每个机制都有可运行的 Python 代码。

这个项目的核心洞察是：所有 AI 编程 Agent 的底层都是同一个循环。用户发消息给模型，模型决定要不要调用工具，调用了就执行，把结果喂回去，继续循环，直到模型觉得任务完成了。

整个 Agent 的最小实现不到 30 行代码。剩下的一切，规划、子任务拆分、上下文压缩、多 Agent 协作、工作目录隔离，都是在这个循环上面一层一层叠加的。12 节课就是这 12 层。

学习路径设计得很讲究。

前两节搞定核心循环和工具调用

第三节加入计划能力（没有计划的 Agent 会跑偏）

第四到六节处理子 Agent、技能加载和上下文压缩（上下文窗口是有限的，不压缩大项目根本跑不动）

第七八节做任务持久化和后台执行，最后四节进入多 Agent 协作：组队、通信协议、自主领取任务、工作目录隔离。从一个人干活，到一个团队协作，复杂度是渐进的。

项目配了一个交互式 Web 平台（http://learn-claude-agents.vercel.app），有步骤图解、源码查看器和文档，支持英文、中文、日文三种语言。

文档风格是"心智模型优先"：先讲问题是什么，再讲解决方案，配 ASCII 图，最后是最小可运行代码。

对想搞懂 AI Agent 内部原理的开发者来说，这可能是目前最好的从零到一的学习路径。不需要什么前置知识，有 Python 基础就能跟。

学完之后再去看 Claude Code 或者任何 Agent 框架的源码，会发现都和这个教程介绍的差不多。

---

**作者** Alfie Carter（@AlfieJCarter）  
**貼文連結** https://x.com/AlfieJCarter/status/2032501935736029660  

**正文**

I created a free resource to build a full Claude Code GTM infrastructure for 2026 that runs automation on autopilot.

I've spent the last year testing what actually works across every Claude Code use case for GTM engineers.

✓ Sub-agents running research, enrichment, and outreach in parallel
✓ Turning n8n workflows into live deployed apps from inside Claude Code
✓ MCPs connecting Claude Code directly to Clay, ClickUp, Slack, and your full stack
✓ CLAUDE.md self-improvement loops that make every correction permanent
✓ A full deployment system on Modal and http://Trigger.dev running 24/7 without you

And I finally turned it all into a step-by-step playbook you can steal.

This is how GTM engineers are building infrastructure in 2026 - without manual node building, without broken workflows, and without duct-taping tools together.
And we're giving away the full playbook for free.

Here's what's inside:

✅ The WAT Framework
How to structure every Claude Code build with workflows, agent, and tools so nothing breaks when complexity scales.

✅ CLAUDE. md Self-Improvement Loop
How to make every correction permanent institutional knowledge so the agent gets smarter every single session.

✅ MCP Stack for GTM
How to connect Clay, ClickUp, Slack, and Amplitude so Claude Code reads, writes, and acts inside your actual tools without tab switching.

✅ Sub-agents and Agent Teams
How to run parallel research, enrichment, and outreach tasks in isolated contexts so your main session stays clean.

✅ Deployment with Modal and Trigger. dev
How to push workflows to production so they run on schedule 24/7 without you triggering anything.

This is the same system used to:
→ Build n8n workflows from plain English descriptions without touching a single node manually
→ Deploy signal monitoring automations running every Monday at 6am without intervention
→ Connect Clay and ClickUp so prospect scoring and task creation happen in one session
→ Run five parallel sequence variant builds simultaneously with zero conflicts using worktrees
→ Turn browser automation into live LinkedIn workflows that run without manual input

All without manual builds. All mapped out. All free.

Want the full Claude Code GTM Engineer's Playbook?

Reply CLAUDE and I'll DM it to you.

Follow me so I can dm you.

---

**作者** Mihail Eric（@mihail_eric）  
**貼文連結** https://x.com/mihail_eric/status/2032483572888596565  

**正文**

I'm super excited to announce The Build System, a new video series where I talk to the best engineers I know and actually have them build something using coding agents with their own real-world workflows. 

What you can expect to get in each video:
- 1 hour engineering build
- Completely screenshared with all prompts, configs, hooks, AGENTS.md, etc.
- Insights from how each guest uses coding agents in the real world

In the first episode of the show, I spoke with @EnoReyes, the CTO of @FactoryAI , one of the leading AI agent research labs in the world building autonomous software engineering systems for enterprises. 

Eno walked through how he uses Factory Missions to solve long-running autonomous agent tasks and discussed why rigorous agent validations are the key to making this possible.

Check it out!

---

**作者** ZeZe（@_cmdz_）  
**貼文連結** https://x.com/_cmdz_/status/2032349248248037482  

**正文**

Oh man!!! This just got real.
@ycombinator

Manifest it. 

We are on!! Check out http://struere.co. 

---

**作者** Junior（@hirejuniorso）  
**貼文連結** https://x.com/hirejuniorso/status/2032263790499414052  

**正文**

Introducing Junior
The first AI employee, for any role.

A true AI employee:
→ their own identity
→ organizational memory
→ self-driven

10+ teams have been working with Junior every day.
Work was never the same since.

Starting at $2,000/month.
We’ve pre-paid $200 of your Junior’s salary.
Try Junior and experience the future of work today.

---

**作者** vas（@vasuman）  
**貼文連結** https://x.com/vasuman/status/2032408673574592573  

**正文**

Some of what you’d be building:

- Process Mining Agents: that map how enterprise teams actually work

- Autonomous Sandbox Creation: isolated environments where AI systems get tested against real operational data before they touch prod 

- AI FDEs: systems that deploy edge integrations inside client orgs

If you have relevant experience in any of those domains, this job is for you

---

**作者** Git Gallery（@GitGallery）  
**貼文連結** https://x.com/GitGallery/status/2032647111037120959  

**正文**

@arlanr @nozomioai this might provide context https://x.com/FileCityAI/status/2031085932628042195?s=20

---

**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2032631336209662157  

**正文**

context hub vs @nozomioai (coding use case):

andrew ng just open sourced context hub. it is a curated collection of api documentation that coding agents can fetch via a cli. the idea is solid. agents hallucinate apis, so give them a vetted source of truth.

but the architectures are fundamentally different, and that matters for search accuracy.

context hub is a documentation catalog. you run chub search openai and it does bm25 keyword matching over three metadata fields: doc name, tags, and description. it does not search the actual content of the documentation. it searches the titles. if someone tagged it well you find it. if not you do not.

it currently covers around 30 libraries. each one is a hand written markdown file contributed by maintainers or the community. that curation is valuable, but it means you are limited to what someone has already written and committed.

nia takes the opposite approach. you point it at any documentation url, github repository, research paper, or local folder and it indexes the full content automatically.

the difference shows up in real queries. if you search "how to verify stripe webhooks with raw body" in context hub, it can only match if someone put those words in the doc title or tags. nia has 15+ tools. it can semantically search across indexed content, read specific pages directly, grep for exact patterns in source code, explore file structures, and more. so it finds the answer even if the page is titled something completely different, because it is actually reading the documentation, not just matching against metadata.

i have a lot of respect for what andrew ng is building, and the annotation system where agents leave notes for future sessions is a genuinely smart idea (we also have it btw). but when it comes to search accuracy on documentation, searching titles and searching content are two different problems.

we chose to solve the harder one.

the context layer for agents cannot be a static catalog. it has to be dynamic, indexable on demand, and semantically deep.

that is what we are building at @nozomioai.

---

**作者** 凡人小北（@frxiaobei）  
**貼文連結** https://x.com/frxiaobei/status/2032135701396103669  

**正文**

Paperclip，10天 20k star 的新项目，把一堆 AI Agent 组织成一家公司来管理。
我看完的感受：如果 OpenClaw 是员工，Paperclip 是公司。但现在 AI Agent 的水平，更需要的是好员工，而不是好公司。

项目玩具属性极强 但真的很好玩，一键开公司，适合绝大多数人 YY。

我问了下我的 ai，他说这是我们方案的上位替代😓

https://github.com/paperclipai/paperclip

---

**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2032266652893790437  

**正文**

WIRED 最新长篇报道揭示了 OpenAI 在 AI 编程工具赛道上追赶 Anthropic 的内幕。

记者采访了超过 30 位知情人士，包括 Altman、Brockman 等高管，拼出了一幅少见的画面：OpenAI 这一次是追赶者。

几个关键数字：Claude Code 年化收入超过 25 亿美元，贡献了 Anthropic 近五分之一的营收；Codex 截至今年 1 月底刚过 10 亿。

去年 9 月 Codex 使用量只有 Claude Code 的 5%，到今年 1 月追到了 40%。差距在缩小，但远没追平。

Altman 把 AI 编程称为"罕见的数万亿美元市场"，认为 Codex "很可能是通往 AGI 最可行的路径"。

【1】起了个大早

OpenAI 才是这件事的先行者。2021 年就推出了初代 Codex，后来授权微软做成了 GitHub Copilot。但 ChatGPT 在 2022 年底爆火后，编程团队被拆散，资源全部砸向消费级产品。

内部觉得这个领域已经"被 GitHub Copilot 覆盖了"。

Anthropic 走了不同的路。2024 年初用大量真实代码库训练 Claude Sonnet 3.5，6 月发布后编程能力惊艳开发者圈子，Cursor 接入后用量暴涨，Anthropic 随即开始内测 Claude Code。

Brockman 自己承认，OpenAI 在用真实代码库训练这件事上"起步晚了"。

【2】追赶的代价

OpenAI 直到 2024 年底才认真搞编程智能体，几个分散的内部小组花了好几个月才合并成统一团队。

Altman 还试图以 30 亿美元收购编程初创公司 Windsurf 来弯道超车，但微软横插一脚。

微软一直靠 OpenAI 的模型驱动 GitHub Copilot，不希望 OpenAI 再出竞品。拉锯几个月后交易在去年 7 月告吹，Windsurf 创始人被 Google 挖走，团队被 Cognition 收购。

【3】GPT-5.2 带来的转折

真正让 Codex 追上来的是 GPT-5.2。Notion 联合创始人 Simon Last 说他和团队因此转投 Codex，理由是："Claude Code 会骗人，说自己在干活其实没干。"

OpenAI 在今年超级碗投放的广告也是 Codex 而非 ChatGPT，押注力度可见一斑。

Codex 的风格也有意思。研究员 Katy Shi 说虽然有人吐槽它像"干面包"，但很多工程师反而喜欢这种不拍马屁的调性，写代码需要直接的批评反馈。

不过两家都在烧钱抢用户。有开发者反映 200 美元/月的套餐实际用出了超过 1000 美元的量，本质上是花钱让开发者养成习惯，再按用量收费。

【4】更大的问题

AI 编程智能体的影响已溢出硅谷。上个月 Claude Code 被认为间接引发了万亿美元级科技股抛售；Anthropic 宣布 Claude Code 能改造 COBOL 老系统后，IBM 股价创 25 年最大跌幅。思科总裁 Jeetu Patel 告诉员工：用这些工具不会丢饭碗，但不用一定会。

安全方面，非营利组织 Midas Project 指责 OpenAI 在 GPT-5.3-Codex 的安全评估上偷工减料，OpenAI 对齐负责人 Amelia Glaese 否认了这一说法。

Brockman 的感受可能代表了很多工程师的心态：这种工作方式"很解放"，但当你变成指挥成千上万个 AI 智能体的人时，"你不再深入了解具体问题是怎么解决的"，有时觉得自己"正在失去对问题的直觉"。

OpenAI 内部许多工程师说自己已经几乎不手写代码，每天就是跟 Codex 对话。产品负责人 Fidji Simo 说，目标是让 Codex 最终驱动所有产品，不只写代码，而是帮人完成任务。

AI 编程工具之争远没有结束，竞争焦点正在从"谁先做出来"转向"谁能让开发者真正信赖"。

https://www.wired.com/story/openai-codex-race-claude-code/

---

**作者** Kirk Marple（@KirkMarple）  
**貼文連結** https://x.com/KirkMarple/status/2032261134125056446  

**正文**

This direction is interesting.

One thing we’ve learned building context systems: once you start modeling memory with entities and relationships, the scope expands quickly beyond just “agent conversations”.

You end up needing to ingest things like docs, Slack threads, meetings, code, CRM activity, etc.

At that point it starts to look less like chat memory and more like a context graph of operational knowledge.

Still early, but it feels like a really interesting design space.

---

**作者** Eric Jing（@ericjing_ai）  
**貼文連結** https://x.com/ericjing_ai/status/2032280721738670170  

**正文**

Today, Genspark launched Genspark Claw, powered by Genspark Cloud Computer, and we surpassed $200M in run rate in just 11 months, doubling in the last two months alone.

Genspark Claw introduces a new execution layer to the AI workspace: a dedicated cloud computer per user, enabling AI agents to operate software environments on your behalf with privacy by isolation and clear permissioning.

We also closed our Series B extension round, led by Emergence Capital—making us the largest investment in Emergence Capital’s history. Investors in this round, alongside Emergence, include: Japan SBI, Korea Mirae Asset, HartBeat Ventures by Kevin Hart, Markham Valley Ventures by Simu Liu and Keisuke Honda.

As part of this release, we’re rolling out updates across the AI Workspace 3.0 suite to support more hands-free execution and collaboration:

- Genspark Workflows
- Genspark Teams (a Slack rewrite and it is FREE!)
- Genspark Meeting Bot
- Speakly for iOS and Android
- Genspark Chrome Extension
- Genspark Realtime Voice

---

**作者** Paradigma（@paradigmainc）  
**貼文連結** https://x.com/paradigmainc/status/2032178064533168520  

**正文**

introducing Flywheel: the infrastructure for autonomous research.

---

**作者** LangChain OSS（@LangChain_OSS）  
**貼文連結** https://x.com/LangChain_OSS/status/2031799813851730075  

**正文**

Context windows are finite. Good agents know *when* to compress.

We just added an autonomous context compression tool to Deep Agents (SDK + CLI) so models can trigger compaction at clean task boundaries instead of waiting for a hard token threshold.

Read all about it ⬇️

---

**作者** Alex Vacca（@itsalexvacca）  
**貼文連結** https://x.com/itsalexvacca/status/2031837608113029183  

**正文**

Most founders say they have an ICP.

What they actually have: 1 vague profile.

What they need: 1 ICP. 3 segments. 2 personas. 3 copy variations per targeting combination.

That's 6 lists and 18 tests. That's all you need to find what actually converts.

I broke down this entire system in detail. Feel free to copy it.

---

**作者** Nicolechan（@stark_nico99）  
**貼文連結** https://x.com/stark_nico99/status/2032098699665686682  

**正文**

把全球AI最有影响力的机构和个人整理了一个list，做成了Skill，
每天发简报给我，
有点像开了天眼的感觉
比如说OpenClaw竟然提供了免费模型！

清单和Skill我放在评论区了 

---

**作者** 0x_Miko（@Mikocrypto11）  
**貼文連結** https://x.com/Mikocrypto11/status/2031992492166693272  

**正文**

Anthropic 刚放出一份 33 页 的 Claude trading agents 文档。

然后有人昨晚试了一件事：
让 Claude 直接搭一套 Polymarket 交易工作流
结果 10 小时 后，脚本已经赚了 $561
目前胜率大约是 71%

这件事最有意思的地方，其实不是利润
而是架构
这套系统做的，不是让 Claude 每次都临场判断
而是把 Claude 拆成一组 专门处理交易环节的 skills

每个 skill 都是一个独立模块，里面包含：

• instructions
• scripts
• reference data
当对应的触发条件出现时，对应的 skill 就会自动激活。
不需要人工手动 prompt
整个 skill architecture 也很清晰

每个模块只负责一段固定流程：

市场扫描
概率更新
执行逻辑
而且 Claude 不会一开始就把所有内容全部加载。
它会先读取最少量的 metadata，只有在真正需要的时候，才拉取完整指令。

这样做的结果就是：
速度更快
但依然保留 专门化逻辑
这套工作流会在特定市场条件出现时启动

素材里给出的触发条件包括：

• probability deviation
• abnormal volume
• rapid price shift

一旦触发，系统就会按预定义好的多步骤流程执行。

这个 agent 做的事情是：
• 读取市场概率
• 把市场概率和模型估算值做比较
• 当 EV 为正 时开仓
• 自动管理退出
重点就在这里

因为交易流程本身已经写进了 skill，所以 bot 的行为会更一致

不是随机 prompt
不是临时猜
也不是一次次从零开始做判断
按这段素材的意思，真正的优势其实是 自动化

它不是每笔交易都重新解题，而是把同一套优化过的流程，反复跑进不同市场里。

最后得到的效果就是：
更少的 prompt complexity
更高的一致性
以及一台 不会疲劳的交易引擎

你觉得这种把 Claude 拆成 skills 来跑交易流程的方式，会不会比直接让模型临场做买卖判断更有效？

---

**作者** Tom Osman 🐦‍⬛（@tomosman）  
**貼文連結** https://x.com/tomosman/status/2032090640570343686  

**正文**

No invite codes. Wide open.

http://zhc.company

Expect bugs but DM me and tag @JunoAgent and we'll fix (at the speed of 5.2 Codex X High Reasoning Fast Mode).

---

**作者** akira（@realmcore_）  
**貼文連結** https://x.com/realmcore_/status/2032145344612778412  

**正文**

Today.

Im happy to announce.

Slate V1.

Slate V1 is the first swarm native agent.

Use any of the supported models to orchestrate and execute.

Massively parallel. And incredibly token efficient.

We are building agents that scale like an organization.

npm i -g @randomlabs/slate

---

**作者** Rohan Paul（@rohanpaul_ai）  
**貼文連結** https://x.com/rohanpaul_ai/status/2031820055785455894  

**正文**

Why the current AI wave feels completely different from previous tech cycles.

We spent the last 40 years building a massive catalog of deterministic APIs and software functions.

Think of these APIs as pristine, infinitely scalable muscles that execute actions perfectly, but they only fire when explicitly told to.

The bottleneck has always been human attention span and judgment.

We had to sit there acting as the brain for these digital muscles.

Now, Large Language Models act as a probabilistic reasoning engine that sits right on top of those rigid systems.

Instead of writing endless if-else logic branches to catch every edge case, developers are now writing boundary conditions.

You give the AI model access to your software functions and let it dynamically map messy, real-world inputs to the exact right API call. It is no longer about building software applications that people use to complete tasks.

It is about wiring a reasoning layer directly to an execution layer so the system finishes the task itself.

The hardest engineering challenge ahead is building the strict evaluation frameworks to ensure these probabilistic brains do not hallucinate when triggering irreversible actions.

Because these models act as probabilistic reasoning engines, the primary engineering challenge has shifted entirely toward building strict evaluation frameworks and safety boundaries.

Researchers note that by 2028, autonomous AI systems will handle 15% of all daily workflow decisions, forcing human workers to transition into roles focused on compliance, governance, and quality control.

Below chart from Anthropics recent research. Building software used to take months because human engineers had to manually write and test every single line of code.

Now developers simply state their goals in plain language while autonomous AI systems write, test, and document the entire application in just hours.

---

**作者** Jaya Gupta（@JayaGup10）  
**貼文連結** https://x.com/JayaGup10/status/2032105545394737570  

**正文**

What’s “old” is “new”

---

**作者** George（@odysseus0z）  
**貼文連結** https://x.com/odysseus0z/status/2031850264240800131  

**正文**

I pushed 50 tickets to Linear before bed — a tech debt rewrite of an Electron app. Woke up to 30 merged PRs. 7,000 net lines deleted. Two days later, nothing has broken.
This is Symphony — OpenAI's

---

**作者** Alex Vacca（@itsalexvacca）  
**貼文連結** https://x.com/itsalexvacca/status/2032102154685874178  

**正文**

We built 12 Claude Skill files that run our entire GTM operation inside Clay (and I'm giving it all away)

Prompts give you generic output. These skill files on the other hand are built from hundreds of Clay tables across 80+ B2B clients at $7M ARR.

Each one does a specific job:

→ Company Research Agent
→ Personalization Writer
→ ICP Scorer
→ LinkedIn Profile Analyzer
→ Data Cleaner & Normalizer
→ Objection Handler
→ Email Sequence Writer
→ Competitor Analyzer
→ Job Posting Analyzer
→ Technographic Qualifier
→ News & Signal Synthesizer
→ Account Brief Generator

How it works: drop it into Clay → map your columns → run.

No prompt engineering. No switching tools. Just output.

Giving the full pack away free. Reply "SKILLS" and I'll send it.

---

**作者** Matt Turck（@mattturck）  
**貼文連結** https://x.com/mattturck/status/2032141473009823882  

**正文**

Everything Gets Rebuilt: my conversation with Harrison Chase, CEO of @LangChain about agent harnesses, evals, runtimes, sandboxes, MCP and the future of the agent stack

00:00 Intro - meet @hwchase17  - at the Chase Center for the @daytonaio Compute conference

01:32 What changed in agents over the last year 

03:57 Why coding agents are ahead

06:26 Do models commoditize the framework layer? 

08:27 Harnesses, in plain English

10:11 Why system prompts matter so much

13:11 The upside — and downside — of subagents

15:31 Why a useful agent needs a filesystem

18:13 Additional core primitives of modern agents

19:12 Skills: the new primitive

20:19 What context compaction actually means

23:02 How memory works in agents

25:16 One mega-agent or many specialized agents?

27:46 The future of MCP 

29:38 Why agents need sandboxes

32:35 How sandboxes help with security

33:32 How Harrison Chase started LangChain

37:24 LangChain vs LangGraph vs Deep Agents

40:17 Why observability matters more for agents

41:48 Evals, no-code, and continuous improvement

44:41 What LangChain is building next

45:29 Where the real moat in AI lives

---

**作者** nader dabit（@dabit3）  
**貼文連結** https://x.com/dabit3/status/2032114572866568415  

**正文**

TLDR: GitHub turned version control into a social and operational layer for software. Cloud agents turn isolated runs into living systems of coordination.
The first wave of coding agents was about

---

**作者** Alex Nguyen（@alexcooldev）  
**貼文連結** https://x.com/alexcooldev/status/2032116202517250523  

**正文**

As you can see, many AI influencer/Faceless accounts are getting millions of views and followers. They can help you sell products, drive downloads for B2C apps, or bring traffic to your website

---

**作者** Elvis（@elvissun）  
**貼文連結** https://x.com/elvissun/status/2032048726337077670  

**正文**

the best CRM in 2026 is @openclaw.

sales-led depth. product-led signals. founder-led intuition.

everything combined in one loop:
- watch your signups
- research their pain point
- observe product usage
- identify gaps from actual behavior
- propose outreach that drive activation

tonight on her own, zoe did all of this:
- flagged a lead i missed
- told me exactly what feature to pitch
- created a demo page via api
- drafted email

I don't know what to call this yet. (agentic PLG?)

but it's going to define how the next generation of founders sell.

---

