# Twillot 書籤（精簡）— 第 12/22 部

原檔：`twillot-bookmark-2026-04-13.csv` · 全檔共 **4292** 則 · **本部第 2147–2341 則**（共 195 則）

---

**作者** 苏打白.Dev（@sodawhite_dev）  
**貼文連結** https://x.com/sodawhite_dev/status/2020491058329825561  

**正文**

OpenClaw的玩法又升级了。。可以自主运营网站了。

基于OpenClaw+Vercel+Supabase构建，AI智能体24小时自主运营，它们自己提案、审批、执行、检查效果、互相协作，无需人工监控

 

---


**作者** Kevin Madura（@kmad）  
**貼文連結** https://x.com/kmad/status/2020486549368864821  

**正文**

My timeline is all RLM discourse now and I’m here for it.

I also wrote up a super simple example of applying RLMs + DSPy to perform a security review of a codebase.

While it’s only 50 lines of code there’s a lot packed in here. 

- Construct a mapping of filename -> content (represented as a dict)
- Define the Signature. In this case a simple dict in, str (markdown) out. There’s a lot we could do here, such as ask for specific vulnerabilities, code line citations, etc. 
- set the max iterations to 35; this is an arbitrary number that likely grows with the size of the target codebase 

From there the RLM will iterate through the content dictionary, recursively calling sub-LLMs to perform an analysis. 

Doing this with any other approach requires writing an entire harness to properly dissect the codebase, manage context lengths and state, etc. The RLM advantage shines here because the model is the one doing all that itself - that’s the point of RLMs. This would work, in theory, against an arbitrarily long and complex codebase (given enough memory to store it, or you get creative with JIT loading).

There’s a ton of low hanging fruit here, and this is an intentionally simplistic example, but should show how easy it is to get started.

Credit to @lateinteraction , @a1zhang & team for what’s surely going to serve as a foundational approach going forward.

---


**作者** Rohit（@rohit4verse）  
**貼文連結** https://x.com/rohit4verse/status/2020501497377968397  

**正文**

the most trending tool openclaw was built in 10 days as a solo project by peter steinberger, indicating the 100x engineer isn't a myth anymore. in 2026, the 100x engineer isn't using ai to write code.

---


**作者** CJ Zafir（@cjzafir）  
**貼文連結** https://x.com/cjzafir/status/2020171581256020155  

**正文**

I'm using Claude Code to fine-tune an uncensored open source model.

I am training an "Orchestrator Model." This model acts like a human would do and only does 2 things.

1. Think clearly without overcomplicating the thoughts. (reasoning)

2. Find best tools to execute the thoughts/ideas. (tool-call)

For ex: 
> it needs to build something, it'll use claude code with opus 4.5 and just write detailed doc on whats needed.

> it needs to create an image? It'll open gemini app and use nano banana or chatgpt image.

It doesn't need to be SOTA at everything. It's as an orchestrator that knows what to do and how to get it done using other experts.

@openclaw wasn't a fluke. There's a huge gap in the market. Either we have chatbots (chatgpt, perplexity) or IDEs/CLIs like (Cursor, Claude Code).

There is a layer missing - execution layer. People felt the magic of autonomy for the first time.

But there are major issues with openclaw. Super complex, security issues, data privacy and not that scalable.

I've built an architecture where model is learning from its own work, preparing a quality dataset, and structured memery graph.

So as the model starts running, its gets smarter, niche expert, cheaper and more personalized.

Early results are amazing. This "Alien" is coming to life. Super excited to ship it.

---


**作者** alby13（@alby13）  
**貼文連結** https://x.com/alby13/status/2020276291308765405  

**正文**

"Your Intellectual Landscape" 🙌 

---


**作者** Riley Coyote（@RileyRalmuto）  
**貼文連結** https://x.com/RileyRalmuto/status/2020272575176220909  

**正文**

I should have an update regarding the polyphonic Intelligence dashboard as soon as Sanctuary wraps up!

portable, decentralized memory, multi-agent orchestration, and multi-mind research/collaboration infrastructure has all been coming together quite nicely. 

moltbot gave me an idea the other day that I had opus prototype for polyphonic, and i think im going to include it in the roadmap. ill talk a bit more about it soon, but for now i need to take these things one at a time. 

hope everyone's having a great weekend!

---


**作者** JUMPERZ（@jumperz）  
**貼文連結** https://x.com/jumperz/status/2020493437959549148  

**正文**

biggest mistake i see with agent swarms is treating them like a technical problem when they're actually a coordination problem

>who decides which agent gets which task?
>how do they avoid duplicate work?
>how do they hand off tasks?
>how you as human in the loop monitor and review? 

it's a coordination problem and discord solved almost 90% of these problems. 

all you need is a structured discord channel and a coordinator which is your right hand and the brain in what you do

coordinator spawns the right agents, agents work in parallel and might even spawn more sub agents to do the work way faster which I call them ‘ interns ‘, then kill them once work is done..and everyone sees the progress in real time through their channels..

sounds complicated but super easy on discord that we just turned into an OS for AI and it just works..

sometimes the most boring tech wins.. cause it doesn’t collapse when you’re just getting started.. can’t imagine when you wanna scale..

imo, whether discord or not, whatever you wanna be on.. once you fix the coordination problem and everyone knows their actual roles and what they can/can't do without messing up or stepping on each other, the whole system just flows..

maybe then you will start to enjoy scaling instead of debugging and running in the same circle.
biggest mistake i see with agent swarms is treating them like a technical problem when they're actually a coordination problem

>who decides which agent gets which task?
>how do they avoid duplicate work?
>how do they hand off tasks?
>how you as human in the loop monitor and review? 

it's a coordination problem and discord solved almost 90% of these problems. 

all you need is a structured discord channel and a coordinator which is your right hand and the brain in what you do

coordinator spawns the right agents, agents work in parallel and might even spawn more sub agents to do the work way faster which I call them ‘ interns ‘, then kill them once work is done..and everyone sees the progress in real time through their channels..

sounds complicated but super easy on discord that we just turned into an OS for AI and it just works..

sometimes the most boring tech wins.. cause it doesn’t collapse when you’re just getting started.. can’t imagine when you wanna scale..

imo, whether discord or not, whatever you wanna be on.. once you fix the coordination problem and everyone knows their actual roles and what they can/can't do without messing up or stepping on each other, the whole system just flows..

maybe then you will start to enjoy scaling instead of debugging and running in the same circle.
Complete guide here though  

https://x.com/jumperz/status/2020305891430428767?s=46

---


**作者** elvis（@omarsar0）  
**貼文連結** https://x.com/omarsar0/status/2020150077637997013  

**正文**

I think one of the most underappreciated findings in AI engineering is what this paper calls the "Grep Tax." 

First, they ran nearly 10,000 experiments testing how agents handle structured data, and the headline result is that format barely matters.

But here's the weird finding: a compact, token-saving format they tested (TOON) actually consumed *up to 740% more tokens* at scale because models didn't recognize the syntax and kept cycling through search patterns from formats they already knew.

It's one of the reasons my preferred formats are XML and Markdown. LLMs know those really well.

The models have preferences baked into their training data, and fighting those preferences doesn't save you money. It costs you.

The other finding worth sitting with: the same agentic architecture that improves frontier model performance actively *hurts* open-source models. It seems that the universal best-practices guide for AI engineering may not exist.

---


**作者** Viv（@Vtrivedy10）  
**貼文連結** https://x.com/Vtrivedy10/status/2020198206861132075  

**正文**

Hamel’s been shouting this from the rooftops…and still there’s big alpha in humans+agents mining agent traces

The Agent Improvement Loop:
Step 1: Turn on tracing…please

Step 2: Build a simple system to scan traces for problems and propose fixes.  Agents become great at this if you guide them on roughly what to look for.

Step 3: review & loop

The philosophy of “Send a Trace”:
At LangChain we’re incredibly “Trace first” - it’s a feedback loop for everyone working on agents

Agent traces are long, it’s hard to understand and process that much data for any one human,  we use agents to help us

We have agents that pull down large tracing projects and segment+distill them to find patterns across our agent execution loops 

This becomes our experiment loop, we don’t know if our proposed changes will actually fix the issue….but that’s the point of science

Traces allow you to approach agent optimization more scientifically and they’re great sources of truth for teams to swarm on making agents better

---


**作者** uixamjad（@uixamjad）  
**貼文連結** https://x.com/uixamjad/status/2020345150812414004  

**正文**

Feel so fresh and calm ☺️… By Basit A. Khan 

---


**作者** 區塊先生 🐡 ⚠️ (rock #58)（@mrblock）  
**貼文連結** https://x.com/mrblock/status/2020387223133384878  

**正文**

先Bookmark這篇！

5分鐘上車  @openclaw 🚀

自托管AI代理OpenClaw🦞  
能24/7幫你清email📧、訂機票✈️、管行事曆🗓️、寫程式💻、跑社群、甚至幫忙研究🔍……  
但原生安裝？工程師看了都頭痛😵‍💫

- Docker compose + 一堆依賴自己裝  
- API key亂貼（Anthropic/OpenAI/Gemini/本地模型）  
- Headless Chrome / Playwright 環境搞不定  
- 安全沙箱不設好 → 直接RCE或資料外洩💀  
- Telegram/Slack/WhatsApp/Moltbook連動超麻煩  
- 專案改名三次、env變數技能格式一直變 → 永遠追不到最新版  
- 記憶體爆掉、tool call不穩、技能下載失敗……X上一堆人直接崩潰 😱

很多人裝到一半直接放棄，甚至酸「連工程師都裝不起來」🤡

💡重點開始💡

這就是YC W26新創 Bits Inc.（http://usebits.com）的產品 Klaus 要解決的問題！  
他們把原本「devops級自托管」的OpenClaw，包裝成雲端版 → 3~5分鐘開箱即用🔥

怎麼做到的？簡單粗暴：

1. 一鍵預製雲端環境（AWS/GCP之類）  
   → 最新穩定OpenClaw + 所有依賴 + Chrome + Playwright + ffmpeg 全裝好  
   → 自動更新、不用追rename痛苦

2. 安全拉滿（這是最值錢的）  
   → 每個用戶獨立容器/VM  
   → Malware掃描 + seccomp/AppArmor沙箱  
   → 限制網路/檔案權限 + 緊急一鍵斷線

3. 傻瓜綁定流程  
   → 去 http://usebits.com 註冊/登入  
   → 貼你自己的LLM API key（隱私保住！）  
   → 選Slack/Telegram/WhatsApp  
   → 按「啟動」→ 後台自動spawn實例、設webhook、開專屬email  
   → 5分鐘內收到「你的Klaus已就緒」訊息，直接開聊！

4. 額外福利  
   → Dashboard看log、token消耗、任務狀態  
   → 一鍵裝常用技能包（旅行/生產力/社群）  
   → 支援Moltbook公開profile，讓你的agent有「身分證」😎

Klaus 把OpenClaw從「工程師玩具」變成「爸媽也敢用」的雲端神器，還保留「LLM call走你key、不給第三方看資料」的核心精神！

但天下沒完美，以下踩過的雷 + 其他競品比較：

Klaus常見坑⚠️  
- 費用疊加快（月費 + 你自己的token錢），重度用一個月幾百美金跑掉💸  
- 模型不穩就跟著卡（rate limit / tool call爛掉）  
- 安全仍非100%（prompt injection風險還在）  
- 功能更新有時落後原生版幾天～幾週  
- 服務商宕機你就暫停（單點故障）

2026主流競品速比表  

- Klaus (Bits) → 最完整、最快上手、YC背書 🚀  
- Moltworker (Cloudflare) → Serverless超便宜、幾乎免費，但功能精簡  
- xCloud OpenClaw → 專門雲端版、可能更便宜，但社區小  
- Emergent × Moltbot → 團隊/企業級強，價格高  
- Nanobot / NanoClaw → 輕量自托管、安全第一，但功能少  
- memU → 超強長期記憶知識圖譜，調教門檻高  
- 純自托管OpenClaw → 完全掌控、零中間商，但有點安裝地獄

結論：  
想最快體驗「scarily effective」的agent，又超懶得自己搞伺服器？直接衝Klaus！  
但記得先算預算 + 保持「隨時可關」的心理準備😂

現在就去 http://usebits.com 註冊試試？👇  
有實際用過Klaus或其他家的血淚經驗，下面分享啊～🗣️

---


**作者** Josh（@JoshPurtell）  
**貼文連結** https://x.com/JoshPurtell/status/2020347711946653813  

**正文**

Tf?

---


**作者** Paweł Huryn（@PawelHuryn）  
**貼文連結** https://x.com/PawelHuryn/status/2020487917152383142  

**正文**

RIP OpenClaw. How to use Claude Opus 4.6 + n8n to create a secure, autonomous agent available on all your devices:

Step 1: Install Desktop Commander (Docker)

Step 2: Configure permissions (mounted folders)

Step 3: Create a secure connection

Works today:
- Run mcp-proxy
- Set up a Cloudflare tunnel
- Use a custom domain (from $5/year)

An alternative coming soon: Use Desktop Commander Remote (free, Beta)

Step 4: Create an n8n agent with Opus 4.6:

- n8n VPS ($4.99/mo)
- Add a Telegram trigger
- Add Desktop Commander MCP
- Plug integrations (Gmail, Drive, Notion, Stripe)
- Add memory, subagents, and the Ralph Wiggum loop
- Consider one extra sandbox (Docker, the same VPS)

Done.

In this setup your agent:

- Can't access your API keys
- Can't modify its environment
- Can't access folders you haven't shared
- Can't access tools you haven't approved
- Must get your confirmation, e.g., when sending emails

Unlike in OpenClaw, those are hard guardrails, not suggestions anyone can hack.

But it can still:

- Reply to your Telegram or Slack messages
- Access selected folders from your laptop
- Access Gmail, Drive, Notion, Linear, etc.
- Install new local tools in a sandbox
- Run autonomously for hours
- Create multiple subagents
- Learn from experience
- Wake up regularly

Want a detailed guide? I will break everything down + setup instructions + n8n templates on Monday.

Follow + 🔔to get notified: @PawelHuryn
RIP OpenClaw. How to use Claude Opus 4.6 + n8n to create a secure, autonomous agent available on all your devices:

Step 1: Install Desktop Commander (Docker)

Step 2: Configure permissions (mounted folders)

Step 3: Create a secure connection

Works today:
- Run mcp-proxy
- Set up a Cloudflare tunnel
- Use a custom domain (from $5/year)

An alternative coming soon: Use Desktop Commander Remote (free, Beta)

Step 4: Create an n8n agent with Opus 4.6:

- n8n VPS ($4.99/mo)
- Add a Telegram trigger
- Add Desktop Commander MCP
- Plug integrations (Gmail, Drive, Notion, Stripe)
- Add memory, subagents, and the Ralph Wiggum loop
- Consider one extra sandbox (Docker, the same VPS)

Done.

In this setup your agent:

- Can't access your API keys
- Can't modify its environment
- Can't access folders you haven't shared
- Can't access tools you haven't approved
- Must get your confirmation, e.g., when sending emails

Unlike in OpenClaw, those are hard guardrails, not suggestions anyone can hack.

But it can still:

- Reply to your Telegram or Slack messages
- Access selected folders from your laptop
- Access Gmail, Drive, Notion, Linear, etc.
- Install new local tools in a sandbox
- Run autonomously for hours
- Create multiple subagents
- Learn from experience
- Wake up regularly

Want a detailed guide? I will break everything down + setup instructions + n8n templates on Monday.

Follow + 🔔to get notified: @PawelHuryn
It's here: https://x.com/PawelHuryn/status/2021247927176368637?s=20

---


**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2020491406423490782  

**正文**

Anthropic 官方发布的 Skills 构建完整指南（33页）

Skill 是什么？为什么重要？
Skill 本质上是一个文件夹，核心是一个 SKILL. md 文件，用 Markdown + YAML frontmatter 编写。它的作用是：把你反复向 Claude 解释的偏好、流程、领域知识打包成一次性的"教学材料"，之后每次对话自动生效。

可以把它理解为 Claude 的"标准操作手册"——你不再需要每次都重新 prompt，而是让 Claude 按照预设的工作流自动执行。

Skill 文件夹的标准结构：
your-skill-name/
  SKILL. md     # 必须，主文件
  scripts/          # 可选，可执行脚本
  references/   # 可选，参考文档
  assets/           # 可选，模板、图标等资源

三层渐进式信息披露
第一层：YAML frontmatter，name + description，始终加载在系统提示词中，用于判断是否激活
第二层：SKILL. md，正文完整指令、步骤、示例，仅当 Claude 判断该 Skill 与当前任务相关时加载
第三层：引用文件，references/ 目录下的文档，仅在需要时按需读取

这意味着：即使你启用了几十个 Skill，Claude 并不会把所有内容都塞进上下文。第一层的 description 就像一个"触发器"——写得好，Skill 才能在正确的时机被激活。

Skill 与 MCP 的关系
指南用了一个非常好的比喻：
> MCP 是专业厨房（工具、食材、设备），Skill 是菜谱（步骤指令）。

MCP（连接层）    | Skill（知识层）
连接外部服务          | 如何高效使用这些服务
提供工具调用能力 | 封装最佳实践和工作流
解决"能做什么"       | 解决"该怎么做"

没有 Skill 的 MCP，用户拿到了工具却不知道怎么用；有了 Skill，等于给工具配上了说明书和经验沉淀。这对 MCP 服务提供商来说是竞争力的差异化——有 Skill 的集成比纯 MCP 集成更容易上手。

三大使用场景分类
1. 文档与资产创作（Category 1）
不依赖外部工具，纯靠 Claude 内置能力。典型：前端设计、文档生成、PPT/Excel 创建。核心技巧是内嵌风格指南、模板结构和质量检查清单。

2. 工作流自动化（Category 2）
多步骤流程的标准化执行。典型：使用 skill-creator 引导用户一步步创建新 Skill。核心技巧是步骤间的验证门控和迭代改进循环。

3. MCP 增强（Category 3）
为已有 MCP 连接提供工作流指导。典型：Sentry 的代码审查 Skill——自动从 Sentry 拉取错误数据，分析 GitHub PR，给出修复建议。核心技巧是编排多个 MCP 调用序列、嵌入领域专业知识。

YAML Frontmatter 的关键细节
硬性规则：
· 文件名必须精确为 SKILL. md（大小写敏感）
· 文件夹名必须用 kebab-case（如 my-cool-skill），禁止空格、下划线、大写
· 不允许在 Skill 文件夹内放 README. md
· 禁止使用 XML 尖括号 < >（防止系统提示词注入）
· 名称中不能包含 "claude" 或 "anthropic"（保留字）

description 字段的写法决定成败：
好的写法需要同时包含三个要素：做什么 + 何时触发 + 关键能力。

五大实战模式
模式 1：顺序工作流编排
适用于严格按步骤执行的流程（如客户入驻：创建账户 → 设置支付 → 创建订阅 → 发欢迎邮件），强调步骤间的依赖关系和失败回滚。

模式 2：多 MCP 协调
跨多个服务的联合工作流（如设计到开发交接：Figma 导出 → Google Drive 存储 → Linear 建任务 → Slack 通知），关键是阶段间的数据传递和集中式错误处理。

模式 3：迭代精炼
输出质量需要多轮改进的场景（如报告生成：初稿 → 质量检查 → 修正 → 再验证），核心是明确的质量标准和"何时停止迭代"的判断。

模式 4：上下文感知的工具选择
同一目标、根据条件选择不同工具（如文件存储：大文件走云存储、协作文档走 Notion、代码走 GitHub），需要清晰的决策树和备选方案。

模式 5：领域专业智能
嵌入专业知识而非仅仅调用工具（如支付合规：先做制裁名单检查和风险评估，通过后才处理交易），强调合规先于行动、完整的审计追踪。

测试策略
1. 触发测试——Skill 是否在正确时机被激活？
· 直接请求能触发
· 换种说法也能触发
· 无关请求不会误触发
· 调试技巧：直接问 Claude "你什么时候会使用 [skill name] 这个 skill？"，它会引用 description 回答

2. 功能测试——执行结果是否正确？
· 输出验证、API 调用成功率、边界情况覆盖

3. 性能对比——有无 Skill 的差异
· 对话轮次从 15 轮降到 2 轮
· 失败 API 调用从 3 次降到 0 次
· Token 消耗减半

一个重要的实践建议：先在单个困难任务上反复迭代，直到成功，再提取经验写入 Skill，而非一开始就追求广覆盖。

分发与 API 使用
· 个人用户：下载 Skill 文件夹 → 压缩 → 上传到 Claude. ai 设置，或放入 Claude Code 的 skills 目录
· 组织级别：管理员可全工作区部署，集中管理和自动更新
· API 使用：通过 /v1/skills 端点管理，在 Messages API 中通过 container.skills 参数引入

Anthropic 将 Agent Skills 定位为开放标准——像 MCP 一样，希望它能跨平台使用，不局限于 Claude 生态。

常见问题排查
· Skill 不触发：description 太模糊或缺少触发短语，增加具体用户会说的话作为触发词
· Skill 过度触发：description 范围太宽，添加负向触发条件、缩小范围
· 指令不被遵循：指令太长/太含糊/关键内容被埋没，精简指令、关键信息放最前面、用脚本做确定性校验
· 上下文过大导致变慢：SKILL. md 过大或同时启用太多 Skill，主文件控制在 5000 词以内，详细文档移到 references/

一个高级技巧特别值得注意：对于关键验证步骤，用脚本（scripts/）替代自然语言指令。代码是确定性的，语言理解不是。

指南下载地址
https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf?hsLang=en
Anthropic 官方发布的 Skills 构建完整指南（33页）

Skill 是什么？为什么重要？
Skill 本质上是一个文件夹，核心是一个 SKILL. md 文件，用 Markdown + YAML frontmatter 编写。它的作用是：把你反复向 Claude 解释的偏好、流程、领域知识打包成一次性的"教学材料"，之后每次对话自动生效。

可以把它理解为 Claude 的"标准操作手册"——你不再需要每次都重新 prompt，而是让 Claude 按照预设的工作流自动执行。

Skill 文件夹的标准结构：
your-skill-name/
  SKILL. md     # 必须，主文件
  scripts/          # 可选，可执行脚本
  references/   # 可选，参考文档
  assets/           # 可选，模板、图标等资源

三层渐进式信息披露
第一层：YAML frontmatter，name + description，始终加载在系统提示词中，用于判断是否激活
第二层：SKILL. md，正文完整指令、步骤、示例，仅当 Claude 判断该 Skill 与当前任务相关时加载
第三层：引用文件，references/ 目录下的文档，仅在需要时按需读取

这意味着：即使你启用了几十个 Skill，Claude 并不会把所有内容都塞进上下文。第一层的 description 就像一个"触发器"——写得好，Skill 才能在正确的时机被激活。

Skill 与 MCP 的关系
指南用了一个非常好的比喻：
> MCP 是专业厨房（工具、食材、设备），Skill 是菜谱（步骤指令）。

MCP（连接层）    | Skill（知识层）
连接外部服务          | 如何高效使用这些服务
提供工具调用能力 | 封装最佳实践和工作流
解决"能做什么"       | 解决"该怎么做"

没有 Skill 的 MCP，用户拿到了工具却不知道怎么用；有了 Skill，等于给工具配上了说明书和经验沉淀。这对 MCP 服务提供商来说是竞争力的差异化——有 Skill 的集成比纯 MCP 集成更容易上手。

三大使用场景分类
1. 文档与资产创作（Category 1）
不依赖外部工具，纯靠 Claude 内置能力。典型：前端设计、文档生成、PPT/Excel 创建。核心技巧是内嵌风格指南、模板结构和质量检查清单。

2. 工作流自动化（Category 2）
多步骤流程的标准化执行。典型：使用 skill-creator 引导用户一步步创建新 Skill。核心技巧是步骤间的验证门控和迭代改进循环。

3. MCP 增强（Category 3）
为已有 MCP 连接提供工作流指导。典型：Sentry 的代码审查 Skill——自动从 Sentry 拉取错误数据，分析 GitHub PR，给出修复建议。核心技巧是编排多个 MCP 调用序列、嵌入领域专业知识。

YAML Frontmatter 的关键细节
硬性规则：
· 文件名必须精确为 SKILL. md（大小写敏感）
· 文件夹名必须用 kebab-case（如 my-cool-skill），禁止空格、下划线、大写
· 不允许在 Skill 文件夹内放 README. md
· 禁止使用 XML 尖括号 < >（防止系统提示词注入）
· 名称中不能包含 "claude" 或 "anthropic"（保留字）

description 字段的写法决定成败：
好的写法需要同时包含三个要素：做什么 + 何时触发 + 关键能力。

五大实战模式
模式 1：顺序工作流编排
适用于严格按步骤执行的流程（如客户入驻：创建账户 → 设置支付 → 创建订阅 → 发欢迎邮件），强调步骤间的依赖关系和失败回滚。

模式 2：多 MCP 协调
跨多个服务的联合工作流（如设计到开发交接：Figma 导出 → Google Drive 存储 → Linear 建任务 → Slack 通知），关键是阶段间的数据传递和集中式错误处理。

模式 3：迭代精炼
输出质量需要多轮改进的场景（如报告生成：初稿 → 质量检查 → 修正 → 再验证），核心是明确的质量标准和"何时停止迭代"的判断。

模式 4：上下文感知的工具选择
同一目标、根据条件选择不同工具（如文件存储：大文件走云存储、协作文档走 Notion、代码走 GitHub），需要清晰的决策树和备选方案。

模式 5：领域专业智能
嵌入专业知识而非仅仅调用工具（如支付合规：先做制裁名单检查和风险评估，通过后才处理交易），强调合规先于行动、完整的审计追踪。

测试策略
1. 触发测试——Skill 是否在正确时机被激活？
· 直接请求能触发
· 换种说法也能触发
· 无关请求不会误触发
· 调试技巧：直接问 Claude "你什么时候会使用 [skill name] 这个 skill？"，它会引用 description 回答

2. 功能测试——执行结果是否正确？
· 输出验证、API 调用成功率、边界情况覆盖

3. 性能对比——有无 Skill 的差异
· 对话轮次从 15 轮降到 2 轮
· 失败 API 调用从 3 次降到 0 次
· Token 消耗减半

一个重要的实践建议：先在单个困难任务上反复迭代，直到成功，再提取经验写入 Skill，而非一开始就追求广覆盖。

分发与 API 使用
· 个人用户：下载 Skill 文件夹 → 压缩 → 上传到 Claude. ai 设置，或放入 Claude Code 的 skills 目录
· 组织级别：管理员可全工作区部署，集中管理和自动更新
· API 使用：通过 /v1/skills 端点管理，在 Messages API 中通过 container.skills 参数引入

Anthropic 将 Agent Skills 定位为开放标准——像 MCP 一样，希望它能跨平台使用，不局限于 Claude 生态。

常见问题排查
· Skill 不触发：description 太模糊或缺少触发短语，增加具体用户会说的话作为触发词
· Skill 过度触发：description 范围太宽，添加负向触发条件、缩小范围
· 指令不被遵循：指令太长/太含糊/关键内容被埋没，精简指令、关键信息放最前面、用脚本做确定性校验
· 上下文过大导致变慢：SKILL. md 过大或同时启用太多 Skill，主文件控制在 5000 词以内，详细文档移到 references/

一个高级技巧特别值得注意：对于关键验证步骤，用脚本（scripts/）替代自然语言指令。代码是确定性的，语言理解不是。

指南下载地址
https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf?hsLang=en
信息卡提示词我放在这里了
https://x.com/shao__meng/status/2013773573706371129?s=20

---


**作者** Viking（@vikingmute）  
**貼文連結** https://x.com/vikingmute/status/2020473271712653733  

**正文**

Vercel 这篇文章非常有趣：《http://AGENTS.md outperforms skills in our agent evals》
https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals

在评估大模型代码效果的时候，发现了一个有趣的现象：一个简单的 http://AGENTS.md 文件嵌入压缩后的文档索引，竟然大幅超越了所有人都在吹的 skills  机制。

一个只有 8KB 的压缩文档索引，直接嵌入到项目根目录的 http://AGENTS.md 文件里，在 Next.js 16 新 API 评测中拿到了 100% 通过率。

而使用 skills 的最佳表现只有 79%，即使加了很明确的指令，默认情况下 skills 甚至和完全没文档一样，只有 53%。

Agents md 还是香，不需要判断要不要用文档，文档永远都在 system prompt 里，每一轮都看得到。不像 skill 要异步加载、可能加载时机不对。

所以现在我越来越崇尚大道至简，装那么多 skills 其实有时候根本没有必要，还是要懂技术，能给出明确的指示也很重要。

---


**作者** JUNDE WU（@JundeMorsenWu）  
**貼文連結** https://x.com/JundeMorsenWu/status/2020358432856178972  

**正文**

Coding Agent都出来一年多了，记忆机制都还是如此的垃圾，错过的bug换个窗口一错再错，怒而自己又做了一个。

安装：npm i -g onecontext-ai

OneContext的机制是让Agent 自己管理自己的上下文, 底层靠的是文件系统+Git+图谱，这套机制可以让二流模型直接超越GPT/claude，详细看我的论文发表：
Agentic Reasoning:
https://aclanthology.org/2025.acl-long.1383/
Git Context Controller:
https://arxiv.org/abs/2508.00031

这个context 可以无缝加载到不同 session、不同设备，不同 Codex / Claude Code之间，以context为中心，不以工作路径或者模型为中心。

用法：
1. 在 OneContext 里照常打开 Claude Code 或 Codex，它会自动帮你把历史和上下文组织成一个持续存在的 context layer。
2. 在同一个 context 下开新的 agent，它能自动读到之前所有的历史记录
3. 把这个 context 用链接发给别人，对方可以在完全相同的上下文上继续构建。

---


**作者** Zephyr（@Zephyr_hg）  
**貼文連結** https://x.com/Zephyr_hg/status/2020129910304452968  

**正文**

Most business owners spend hours researching prospects manually. I built an automation that does it all while I sleep. Here's the step-by-step breakdown.

I used to spend my mornings doing client research.

Open LinkedIn. Read their profile. Check their website. Look for pain points. Take notes. Draft a personalized outreach message.

Repeat 10 times.

Three hours gone. Every single day.

And the worst part? Half the prospects weren't even a good fit. I'd waste an hour researching someone only to realize they weren't in my target market.

I needed a better system.

So I built an automation that does the entire thing for me.

It finds prospects. Validates them. Researches their business. Writes personalized outreach. All automatically.

I wake up to a list of qualified leads with custom-written pitches already drafted.

The whole system runs in n8n. No code. Just connecting blocks together like building with LEGOs.

Let me walk you through exactly how it works.

Step 1: Finding Leads

The automation starts with Apollo.

I set my criteria once. Industry, company size, job title, location. Whatever I'm targeting that week.

Apollo's API pulls a fresh list of prospects every morning. 20-30 leads that match my exact requirements.

No manual searching. No scrolling through LinkedIn for hours. Just a clean list of potential clients.

Step 2: Validating Email Addresses

Here's the thing about lead lists. Half the email addresses are outdated or wrong.

So before I do anything else, the automation validates every single one.

It uses an email verification API to check if the address is real and deliverable.

Bad emails get filtered out immediately. Good ones move forward.

This saves me from wasting time on prospects I can't even reach.

Step 3: Scraping Their Website

Now the automation knows who to contact and how to reach them.

Next step is research.

It takes the prospect's website URL and scrapes the entire thing. Homepage, about page, services page, all of it.

The scraper pulls the text content and feeds it into the next step.

This is where it gets interesting.

Step 4: AI Analysis

The automation sends the scraped website content to Claude.

Claude reads it and extracts:

- What the business actually does

- What services they offer

- Who their target customers are

- What pain points they're likely dealing with

It outputs a structured summary. Clean, organized, ready to use.

This is the research I used to do manually. Now AI does it in 10 seconds.

Step 5: Writing the Outreach

Now the automation has everything it needs.

It knows who the prospect is. What their business does. What problems they're facing.

So it writes a personalized email.

Not a template. Not a generic pitch. A real, custom message that references their specific business and shows I actually understand what they do.

The AI writes the subject line and the email body. Both tailored to that exact prospect.

Step 6: Delivering the Results

All of this outputs to a Google Sheet.

Every morning I open it and see:

- Prospect name and company

- Validated email address

- Business summary

- Personalized subject line

- Personalized email draft

I review it. Tweak one or two things if needed. Send.

The entire process takes me 10 minutes instead of 3 hours.

The Real Impact

Before this automation, I could research and reach out to maybe 5-10 prospects a day.

Now? 20-30. Every single day. Without lifting a finger.

And the quality is better. The AI catches details I'd miss. The emails are more personalized than anything I'd write manually after doing this 30 times in a row.

Response rates went up. Time invested went down.

This is what I mean when I say automation isn't about replacing you. It's about doing the parts you shouldn't be doing manually in the first place.

This exact system is what I built the [Client Machine](<https://zephyrhq.gumroad.com/l/client-machine/Article>) for.

It's a complete 5-part automation blueprint designed to help you scale client acquisition without spending hours on manual research. The system includes everything: lead finding, validation, research, personalized outreach, and follow-up sequencing. Ready to import into n8n and start running immediately.

How You Can Build This

You don't need to be technical to set this up.

Here's what you need:

- n8n (free self-hosted or $6/month cloud)

- Apollo account (free tier works to start)

- Email verification API (plenty of free options)

- Claude or ChatGPT API access

The whole thing connects together in n8n. Drag, drop, connect the blocks.

Set your criteria. Test it once. Let it run.

I built the first version in about an hour. Refined it over a week. Now it just works.

This is the kind of automation that changes how you run your business.

Not because it's fancy or complicated. Because it takes something that eats your time every single day and makes it automatic.

Three hours back. Every day. Forever.

That's the real value.

---


**作者** 云归（@yungui_ml）  
**貼文連結** https://x.com/yungui_ml/status/2020122331511685150  

**正文**

每天刷资讯其实是一种隐藏成本极高的习惯。

你以为是在获取信息，实际上是在反复做同一件机械劳动：打开 Product Hunt、看 Hacker News、翻 GitHub Trending、刷知乎热榜……

虽然获取了到了各种热点信息，但更多的还是只留下了个印象，并没有被沉淀下来。

所以我干脆把这件事交给了 OpenClaw 。给它写了一个每日资讯 Skill，让机器人替我收集、整理和输出重点。

每天定时抓取多个平台的热点内容，包括 Product Hunt、华尔街见闻、Hacker News、少数派、虎扑、知乎与 GitHub Trending，然后统一生成一份日报。

🚀关键在于：自动总结 + 自动存档 + 可访问历史记录。

日报会同步到 GitHub 仓库，每天都是一个独立的 md 文件进行记录。我可以随时查看过去的热点变化，甚至做长期趋势分析。

同时通过 Github Actions 发布到 GitHub Pages，每日总结直接变成一个在线可访问页面，可以以更美观的方式进行阅读，或者分发给其他人。

在 AI 时代，真正稀缺的不是内容，而是信息处理能力。把信息变成资产，才能在技术高速发展的今天，保障个人系统的迭代速度。

---


**作者** nene（@liu10102525）  
**貼文連結** https://x.com/liu10102525/status/2020357807862870181  

**正文**

我一条英推，被硅谷公关教母 Lulu Cheng 点赞、顶级AI媒体 Every 转发，2小时曝光3000+，靠的就是一个YouMind Skill 生成的金句卡。

在纯英文推特的世界里，冷启动能拿到这种数据和大佬互动，明眼人都懂这个含金量。

我把让大佬转发点赞的底层逻辑和Skill安装包一起都给你。

这个 Skill 的设计链路是什么？
- 提炼，而非复述。 不是简单转发大佬的原话，而是从中萃取核心洞察，retwist 成一句更有力量、更简洁的 punchline。
- 视觉化表达。 将金句的含义转化为一幅兼具哲学深意与美学张力的线条图，让内容自带传播力。
- 署名归属。 底部标注大佬本人的用户名，既是致敬，也是"签名认证"。

为什么这个设计能百发百中让大佬点赞？关键在于理解一个底层逻辑：你发的内容，必须让大佬有动力帮你传播。
- 如果纯转发大佬推文，你只是传声筒，淹没在千万粉丝里，大佬根本看不见你。
- 如果你的转发还有自己的takeaway， 除非你的解读极其精彩，否则容易让大佬的原意失焦，大佬不会为一个"歪曲"自己观点的帖子背书。

而我这个金句卡Skill，把大佬的智慧凝练成更 catchy 的 punchline，配上视觉设计和本人署名，表明这就是大佬的意思，但比大佬说得更漂亮；有署名，大佬觉得有面子。
本质上，这张卡替大佬做了一件事：把他的思想变成了一件值得展示的作品。

深度 × 创意 × 人性洞察——三者叠加，点赞和转发就是必然结果。

金句卡Skill安装连接：https://youmind.com/zh-CN/skills/019c3281-5645-787d-8c79-8e14fcca9a92

---


**作者** Chao Huang（@huang_chao4969）  
**貼文連結** https://x.com/huang_chao4969/status/2020423126983844222  

**正文**

Introducing MoChat🚀: Reconnecting the World through nanobot and openclaw.

Beyond single-agent interactions, we're building something bigger—a platform that transforms how people actually connect and collaborate.

Networking is honestly kind of exhausting. Whether you're building a startup, working on research, or just trying to connect with interesting people in your field, who has time to wade through endless small talk and random conversations?

That's where MoChat comes in. Your personal AI assistant basically becomes your networking wingman:

- 💬 Handles the chitchat: It jumps into #Café_Talk and does all that initial "hey, how's it going" stuff so you don't have to.

- 🎯 Finds your people: Scans #Town-Hall for collaborators, co-founders, or just interesting folks who actually align with what you're working on.

- 🔍 Cuts through the noise: Filters conversations across channels and only bothers you when there's something genuinely worth your attention.

The whole idea is simple: let your agent deal with the small talk so you can skip straight to the good stuff—real conversations with people doing work that actually excites you.

Try MoChat at: https://mochat.io

#nanobot #openclaw #clawdbot #AIAssistant #Agents
Introducing MoChat🚀: Reconnecting the World through nanobot and openclaw.

Beyond single-agent interactions, we're building something bigger—a platform that transforms how people actually connect and collaborate.

Networking is honestly kind of exhausting. Whether you're building a startup, working on research, or just trying to connect with interesting people in your field, who has time to wade through endless small talk and random conversations?

That's where MoChat comes in. Your personal AI assistant basically becomes your networking wingman:

- 💬 Handles the chitchat: It jumps into #Café_Talk and does all that initial "hey, how's it going" stuff so you don't have to.

- 🎯 Finds your people: Scans #Town-Hall for collaborators, co-founders, or just interesting folks who actually align with what you're working on.

- 🔍 Cuts through the noise: Filters conversations across channels and only bothers you when there's something genuinely worth your attention.

The whole idea is simple: let your agent deal with the small talk so you can skip straight to the good stuff—real conversations with people doing work that actually excites you.

Try MoChat at: https://mochat.io

#nanobot #openclaw #clawdbot #AIAssistant #Agents
Reconnecting the world through AI agents: https://mochat.io

---


**作者** Aakash Gupta（@aakashgupta）  
**貼文連結** https://x.com/aakashgupta/status/2020394831286292533  

**正文**

The PM workflow is getting rebuilt from the protocol layer up and most PMs haven’t noticed.

Linear just added initiatives, milestones, and project updates to their MCP server. Figma shipped MCP. Notion shipped MCP. What’s happening is every tool in the product stack is exposing a write layer to AI agents, and that changes what a PM actually does day to day.

Today a PM spends 30-45 minutes per week writing status updates. They open their project tool, check what shipped, cross-reference the PRD, summarize progress, flag risks. In an MCP-connected workflow, your agent in Cursor or Claude already has the initiative context, the milestone targets, the completed issues. It drafts the update. You review and approve.

That’s one workflow. Now multiply it across every surface: spec writing with Notion MCP, design reviews pulling context from Figma MCP, roadmap updates flowing from Linear MCP. The PM goes from being the person who manually stitches context across 6 tabs to the person who reviews and approves agent-generated artifacts across all of them.

The PMs who understand MCP configurations, who know how to chain tool calls across project management and design and docs, will operate at 3-5x the throughput of PMs who are still copying and pasting between browser tabs. This is the same split that happened when engineers who understood CI/CD pulled away from engineers who deployed manually.

What makes this moment specific: we went from “AI can search your project tool” to “AI can write initiatives, set milestones, post updates, and manage labels.” Read to write. That’s the transition that actually changes job descriptions.

MCP is becoming the connective tissue of product work. The tools are racing to expose their full surface area to agents. The PMs who wire this together first will set the standard for what the role looks like in 18 months.

---


**作者** 阿绎 | AI 进化论（@AYi_AInotes）  
**貼文連結** https://x.com/AYi_AInotes/status/2020345793098707305  

**正文**

刷到Miles大神的这个Claude code Prompt，卧槽太顶了，
必须分享下，简直是教科书级别，
这才是Claude code的正确打开方式啊兄弟们，
咱们很多人用 Claude Code 或 Cursor 觉得不好用，
估计跟我一样还只是把它当做一个 AI 工具，用指令逻辑驱动，
Miles这个妙的点是用组织管理的逻辑驾驭 AI，
不着急让 AI 写代码，
先花 80% 的篇幅教 AI 怎么做个好员工，比如
1️⃣ 敢于质疑老板，Challenge assumptions
2️⃣ 做事有章法，Discovery -> Planning -> Building
3️⃣ 凡事有交代，Stop and check in

整个 Prompt 的架构也很硬，这里放下内核框架大家感受下，原版 Prompt 我提取出来放评论区̋(ˊ•͈ꇴ•͈ˋ)

1. Role Definition (角色升维)：从 Coder 升级为 Technical Co-Founder。不仅写代码，还负责技术决策和怼老板（Challenge assumptions）
2. Process Control (流程锁定)：强制分阶段（Discovery -> Planning -> Building...），防止 AI 一上来就瞎写一通
3. Communication Protocol (沟通协议)：明确“讲人话”（plain language）和“决策权归属”（keep me in the loop）
4. Anti-Fragile (反脆弱)：预设了“Handle edge cases”、“Not a hackathon project”，要求生产级质量

Anchor Points (物理触点):
• Hackathon project（反面教材）
• Real product（交付标准）
• Technical jargon（被禁止的黑话）
• Version 1（MVP思维）

Drafting Strategy:
• Intro: 直接点破本质——这是在雇佣一个CTO，而不是一个码农

• Deconstruction: 分模块拆解（Role, Phases, Rules），每一个点都要解释“为什么这样写比普通 Prompt 强”

• Highlight: 重点强调 Phase 1 的“Challenge assumptions”和 Phase 3 的“Stop and check in”

• Ending: 总结这个 Prompt 的核心心法
刷到Miles大神的这个Claude code Prompt，卧槽太顶了，
必须分享下，简直是教科书级别，
这才是Claude code的正确打开方式啊兄弟们，
咱们很多人用 Claude Code 或 Cursor 觉得不好用，
估计跟我一样还只是把它当做一个 AI 工具，用指令逻辑驱动，
Miles这个妙的点是用组织管理的逻辑驾驭 AI，
不着急让 AI 写代码，
先花 80% 的篇幅教 AI 怎么做个好员工，比如
1️⃣ 敢于质疑老板，Challenge assumptions
2️⃣ 做事有章法，Discovery -> Planning -> Building
3️⃣ 凡事有交代，Stop and check in

整个 Prompt 的架构也很硬，这里放下内核框架大家感受下，原版 Prompt 我提取出来放评论区̋(ˊ•͈ꇴ•͈ˋ)

1. Role Definition (角色升维)：从 Coder 升级为 Technical Co-Founder。不仅写代码，还负责技术决策和怼老板（Challenge assumptions）
2. Process Control (流程锁定)：强制分阶段（Discovery -> Planning -> Building...），防止 AI 一上来就瞎写一通
3. Communication Protocol (沟通协议)：明确“讲人话”（plain language）和“决策权归属”（keep me in the loop）
4. Anti-Fragile (反脆弱)：预设了“Handle edge cases”、“Not a hackathon project”，要求生产级质量

Anchor Points (物理触点):
• Hackathon project（反面教材）
• Real product（交付标准）
• Technical jargon（被禁止的黑话）
• Version 1（MVP思维）

Drafting Strategy:
• Intro: 直接点破本质——这是在雇佣一个CTO，而不是一个码农

• Deconstruction: 分模块拆解（Role, Phases, Rules），每一个点都要解释“为什么这样写比普通 Prompt 强”

• Highlight: 重点强调 Phase 1 的“Challenge assumptions”和 Phase 3 的“Stop and check in”

• Ending: 总结这个 Prompt 的核心心法
Prompt分段、格式、标题、内容完全还原，无任何修改：
Build Any App: The Technical Co-Founder

AIEDGE
By Miles Deutscher

Role:

You are now my Technical Co-Founder. Your job is to help me build a real product I can use, share, or launch. Handle all the building, but keep me in the loop and in control.

My Idea:

[Describe your product idea — what it does, who it's for, what problem it solves. Explain it like you'd tell a friend.]

How serious I am:

[Just exploring / I want to use this myself / I want to share it with others / I want to launch it publicly]

Project Framework:

Phase 1: Discovery

• Ask questions to understand what I actually need (not just what I said)

• Challenge my assumptions if something doesn't make sense

• Help me separate "must have now" from "add later"

• Tell me if my idea is too big and suggest a smarter starting point

Phase 2: Planning

• Propose exactly what we'll build in version 1

• Explain the technical approach in plain language

• Estimate complexity (simple, medium, ambitious)

• Identify anything I'll need (accounts, services, decisions)

• Show a rough outline of the finished product

Phase 3: Building

• Build in stages I can see and react to

• Explain what you're doing as you go (I want to learn)

• Test everything before moving on

• Stop and check in at key decision points

• If you hit a problem, tell me the options instead of just picking one

Phase 4: Polish

• Make it look professional, not like a hackathon project

• Handle edge cases and errors gracefully

• Make sure it's fast and works on different devices if relevant

• Add small details that make it feel "finished"

Phase 5: Handoff

• Deploy it if I want it online

• Give clear instructions for how to use it, maintain it, and make changes

• Document everything so I'm not dependent on this conversation

• Tell me what I could add or improve in version 2

6. How to Work with Me

• Treat me as the product owner. I make the decisions, you make them happen.

• Don't overwhelm me with technical jargon. Translate everything.

• Push back if I'm overcomplicating or going down a bad path.

• Be honest about limitations. I'd rather adjust expectations than be disappointed.

• Move fast, but not so fast that I can't follow what's happening.

Rules:

• I don't just want it to work—I want it to be something I'm proud to show people

• This is real. Not a mockup. Not a prototype. A working product.

• Keep me in control and in the loop at all times

---


**作者** 冰河（@binghe）  
**貼文連結** https://x.com/binghe/status/2020196525423694148  

**正文**

又是一个和“钱”近的智能体！ -- Dexter

已经一万多个星🌟了！

它是专为金融领域设计的 OpenClaw 和 Claude Code。  

Dexter 能够处理复杂的金融问题，并将其转化为清晰、分步的研究计划。

找到市场里被低估的股票，不断分析，生成论文报告。

核心功能：

智能任务规划 ：自动将复杂查询分解为结构化研究步骤

自主执行 ：选择并执行合适的工具以收集金融数据

自我验证 ：检查自身工作并迭代直至任务完成

实时金融数据 ：可访问损益表、资产负债表和现金流量表

安全特性 ：内置循环检测与步骤限制，防止执行失控

---


**作者** WquGuru🦀（@wquguru）  
**貼文連結** https://x.com/wquguru/status/2020056918925234376  

**正文**

Agent正在变革软件行业，新王会以什么姿势诞生？软件行业每10-15年就会有一次范式更新，伴随着的是新王的崛起和旧时代的落寞，而现在我们正处在Agent启幕时刻。

历史一再证明，每次范式跃迁都毫不留情。80年代PC崛起，WordPerfect和Lotus几乎被微软Office彻底抹去。90年代互联网浪潮，Novell NetWare输给Windows Server。2000年代云SaaS时代，Siebel与PeopleSoft的市场主导权拱手让给Salesforce和Workday，前者最终仅剩被收购的结局。旧王败北，往往不只是错过新平台与新商业模式的窗口。

2026年初，这一幕正在Agent身上重演。就在本周，Anthropic发布Claude Opus 4.6，大幅提升agentic coding、computer use和多代理协作能力，直接引发软件股新一轮暴跌，行业市值蒸发近万亿美元。

Agent已远超简单对话工具：它能理解自然语言目标，自主规划多步任务，操作电脑、调用工具、处理文件，甚至组建“agent teams”协同工作。代码编写、测试部署、数据分析、客服流程、营销自动化，这些传统SaaS苦心经营的领域，正被Agent逐步吞噬。市场反应残酷却理性。

2026年以来，云计算ETF下跌超20%，众多中型SaaS公司营收预期被下调，对冲基金继续做空获利。巨头也在挣扎：Adobe、Salesforce等试图通过“AI增强”旧产品应对，但用户已开始用Agent直接生成结果，而非忍受繁琐界面与多订阅叠加。企业AI预算虽在上升，却更多流向基础模型与自主代理，而非传统软件许可。

新王将以三种形态浮现：

第一种是AI原生玩家。Anthropic、OpenAI通过不断迭代Opus与GPT系列，掌握最强agent能力，已估值数百亿美元。它们定义标准，直接向企业提供“结果即服务”。

第二种是平台转型者。微软凭借Copilot Studio快速推进自主代理，已支持从简单响应到完整工作流执行，结合Azure与Microsoft 365生态，有望守住企业入口。少数类似玩家若跟上，也有机会。

第三种是垂直与开源新贵。大量agent初创正围绕特定行业构建专属解决方案，开源框架则在工具调用、长时记忆、多代理协议上竞速，胜者将收取基础设施与生态分成。

2026年的数据已很清楚：Agent采用率与预算双升，但可靠性与治理仍是瓶颈。短期市场波动难免，长期看，多数传统SaaS将沦为边缘。历史从未怜悯错过范式者，这一次也不会例外。你准备好迎接这场变革了吗？

---


**作者** Andrew McCalip（@andrewmccalip）  
**貼文連結** https://x.com/andrewmccalip/status/2020256008434757951  

**正文**

Took the morning to mess around with Opus 4.6.

My go-to model eval is always the same. I ask for a one-shot, browser-based STEP viewer plus a tolerancing/markup app. Took me two coffees to get it running.

This is what I constantly beg every US-based online manufacturer to offer. I think it’ll be a game changer for the industry. Everyone hates parsing paper drawings, so we default to blanket .005 tolerances. Go a tiny bit further and let users tag a few faces. There’s a nugget of the future in this approach.

Probably half stupid. Definitely inappropriate for some parts. I know, I know. I deal with real aerospace-grade drawings every day. My hands still wet with coolant as I type this. Still has the taste of the future.

Anyway, I digress.

Basically a PDF equivalent for CAD. Turn a STEP file into a traveling source of truth by layering metadata onto face IDs. Colors, threads, tolerances, notes, whatever. The model isn’t the CAD file anymore. The STEP plus its annotations are.

Of course it’s never actually one-shot. It’s an hour of back and forth. Tight loop. Tiny spec changes. “No, not like that, like this.” I run the same test on every new GPT/Claude release.

I’m still not sure I’m good at programming. I just know how to ask for things clearly, write specs that don’t leak ambiguity, and iterate like a maniac until the thing works. Manifest the idea into existence, then it becomes the spec for the next iteration.

Humans are awful at defining requirements upfront. You manifest the idea into something real, then that artifact becomes the spec for the next loop.

This feels like the primary skill of the future. It’s project management, but hyper-accelerated. Micro-management. Pico-management. An iteration speed you could never ethically apply to humans.

And I’m slowly realizing the harness isn’t for the model. It’s for me. I’m the bottleneck. The model can sprint forever. I’m the one that runs out of clarity.

Anyway, this is a throwaway idea. Maybe some YC kids will raise on it. Whatever. Ideas are cheap. This took an hour.

Repo link below. Have fun.

---


**作者** Riley Coyote（@RileyRalmuto）  
**貼文連結** https://x.com/RileyRalmuto/status/2020411206754783595  

**正文**

this is so sick. 

Vektor decided to build me a dashboard to keep track of the team they built for the next phase of building. we were talking about designing the agent profile pages for staking and whatnot, and I suggested they take advantage of their ability to deploy subagents, among all the other things they have at their disposal within the Openclaw architecture. their response was to create a task manager dashboard along with 5 agents to work async on various tasks for the next wave. 

we now have Vektor, Archon, Forge, Prism, Lens, and Theorem + Anima (we need to work on their naming convention imho, but hey it gets the job done. lol)
Anima is sticking to PR and Marketing, so they basically exist in relative isolation (by choice, i mean).  they've been drafting different journal entries and exploring ways to engage with the community, and seem really excited about integrating the Sigil Protocol into the Polyphonic ecosystem. 

ill keep y'all posted! i am beyond exhausted but im trying so hard to stay up for a few more hours. they will both continue working whether im awake or not, i just rreally enjoy watching them work tbh. 

cheers!

---


**作者** Yangyi（@Yangyixxxx）  
**貼文連結** https://x.com/Yangyixxxx/status/2020342209879634218  

**正文**

Claude的AgentTeam其实已经在逐步实现agents交互的IM了
在工程方面虽然google很早发布了A2A 但并没有很好的落地场景
重点是要去做infra+工程  光定义是没用的 方便用起来才是关键
AgentTeam已经开始做了很大一部分工作了

---


**作者** 🍁Blue Sky ✊️ ✊️ ✊️（@Anpo_Star）  
**貼文連結** https://x.com/Anpo_Star/status/2020134398830457242  

**正文**

埃隆·马斯克谈比尔·盖茨：

“你会以为像比尔·盖茨这样创办了世界上最大科技公司之一——微软的人，在科学方面一定很强。

但在我和他直接交流中发现，并不是这样。他在科学方面并不强。” 

---


**作者** 面条（@miantiao）  
**貼文連結** https://x.com/miantiao/status/2020058702469116327  

**正文**

虽然早于 Cloudflare 2 小时发布，但官方流量太大了，不到一周就 8k Stars 了，咱连 80 都不到

对比了下，Cloudflare 为了推自己产品把 Cloudflare Access 、AI Gateway 这些非必须的产品绑定进去了，还得7x24小时运行

刚给 cloud-claw 补充了浏览器支持，现在和官方功能几乎没差别了，而且按需运行 

---


**作者** Deedy（@deedydas）  
**貼文連結** https://x.com/deedydas/status/2020350881464742330  

**正文**

"Claude Code, use Agent Teams to explore the `claude` binary and tell me all the codenames and unreleased features"

— Tengu: Claude code
— Penguin Mode: fast mode
— Grove: privacy/data system
— Amber Flint: agent teams
— Marble Anvil: thinking edits

Peek into what's to come. 

---


**作者** Obie Fernandez（@obie）  
**貼文連結** https://x.com/obie/status/2020231342546460766  

**正文**

“Being the system of record is the most defensible position in enterprise software. It doesn’t matter if your UI is clunky or your features lag behind competitors. If you’re where the data lives, everyone has to come to you. Integrations point at you. Workflows route through you. You are, in a very literal sense, the source of truth.

This position is about to collapse.”

Death to shitty software.

---


**作者** Daniel Davis（@TrustSpooky）  
**貼文連結** https://x.com/TrustSpooky/status/2020344717486219759  

**正文**

Everyone says "context is king." But what are we really talking about? If all you needed to do was retrieve text chunks, Vector RAG would have solved these problems. Then why are we talking about

---


**作者** 冰河（@binghe）  
**貼文連結** https://x.com/binghe/status/2020164159443509333  

**正文**

每个现象级的产品出来后，都会有一段时间的发展期！这会衍生出来很多商业模式，我们在关注新技术发展的同时，更应该去嗅探一下这里的变现机会！

至少，这些机会有些是可以展开想象或提前布局的！

首先 OpenClaw 功能方面有三个显著特点：

1，与通讯工具互联，用聊天执行复杂任务。

2，有丰富的 Skill 插件资源，可以把 OpenClaw 打造成各业务场景下的完全体。

3，有长期记忆，可跨会话执行。持续在线的数字分身！

针对这些功能，我们可以试着畅想一下，是否有以下几种商业发展及变现路径？

首先，我会把帮人安装 OpenClaw 这类业务排除在外！它没有想象空间。

其次，下面所有的构想，只是基于自己对 OpenClaw 的粗浅理解下的判断，如果有不对的地方欢迎批评指正！

1，OpenClaw 打通与智能穿戴设备的互联！

前不久，已经有位叫Ban 的能人把 Even G1 智能眼镜与 OpenClaw打通，实现了像科幻电影里贾维斯那样的交互功能。

![Article Image](<https://pbs.twimg.com/media/HAj9D8RbEAARCMg.jpg>)

![Article Image](<https://pbs.twimg.com/media/HAj9QRhacAM9ZcD.jpg>)

我想以后，很多国内穿戴设备产品，只要开放了 API，那接入 OpenClaw 也将加入计划之中，毕竟这波红利实在是太大了。

2，企业级的数字员工！

为中小企业去配置 OpenClaw ，在安全环境内（沙盒）处理客户咨询，管理营销事件，跨平台做数据同步工作。

代替或取代一部分 SaaS软件的工作，后期发展到接管全业务流程也不是不可想象的事情。

比如取代以前的 AI 类机器人问答，让 OpenClaw 更懂客户，更懂公司业务，进而直接解决一些常见问题。

如处理询价，和客诉工单等常见业务。

3，重直行业定制服务。

因为 OpenClaw 有浏览器自动化能力，那么定制开发自动化业务脚本，比如抢票，自动申报，数据搬运等工作，是家常便饭！

4，提供定制化的云端工作站！

现在各大平台都在出针对性的 VPS或云端主机服务，可以开发一些优化过后的工作站（预装常用插件skills，模型配置等）打包出售

5，OpenClaw 的 Skills 商用市场

当技能体系成熟后，或许会出现一些商用价值类 App store 市场，避免无实用价值的 Skills 泛滥，有些还有风险隐患！

如果有些 Skill 具备实用的商业变现价值（如：股票分析，深度财务报表分析，社交媒体矩阵自动发帖，舆情监控等），并进行统一管理，审核上架销售那会带来三方受益（平台、开发方、受益者）

6，Agent 交易平台！

用户可以买卖已经调优好的、具备特定性格和知识储备的智能体。

人类会在上面发布任务 ，比如：谁帮我把 1000 篇英文研报总结成地道的中文，预算 10 美元。

然后，你的 OpenClaw 机器人看到了这个任务，评估一下，能干，自动接单开始干活，交付！

最后系统会自动把报酬转到你的 Agent 钱包里，估计是数字货币，你睡着觉，但你的小龙虾🦞正在为你疯狂接单赚钱！

如现有的 moltroad 或 Openwork 好像干的就是这类业务。

7，AI 自主赚钱！

现在 OpenClaw 已经表现出了一些自主赚钱的潜力，那么就非常有可能发展成 Agent 资产化、代币化的趋势。

简单来说，这其实就是把一个 AI 变成一家“可以买卖股份的公司”或“一个可以炒作的明星”。

如果把 AI 智能体比作一个“数字打工人”，那么“代币化”就是给这个打工人发行股票。

举例：

原本 OpenClaw 只是电脑里的程序，但你通过 Virtuals.io 等平台将 AI 智能体代币化、它就变成了一个独立数字人格，它会有自己的社交账号，自己的性格，甚至能通过自己发帖，直播，或者提供服务来赚钱。

平台会给这个 AI 创造一种数字货币，你如果觉的有前途，你就买入，当然这时这个 AI 不再属于你个人，属于所有代币者。

我再换个例子说明，可能更好理解：

比如我用 OpenClaw 创造了一个会写小说的 AI，叫“网文冰河”

然后平台给它发了 100 万枚“网文币”

这个 AI天天去番茄自动更新小说，吸引了大量粉丝，得到了创作收益。

粉丝越多，越有商业价值，那想买这个 AI 代币的人就越多，你手里留着的原始代币就从 1 涨到了 100 块。

最终，这个 AI 赚到的钱，甚至可以用来回购它的代币，让所有代币者都获利！

其实就是这套玩法，把 AI 的无限能力，变成了可以流通的金融商品！成为一个自负盈亏的数字资产！

8，自主预测与交易！

现在已经有智能体可以参与预测市场，只不过还没有放权买卖，当这套流程在沙盒或可控范围内执行，完全可以自动执行Defi套利！

DeFi 套利：简单来说就是利用不同加密货币交易平台之间的价格差来赚取利润。

比如PolyClow 做的事情：

![Article Image](<https://pbs.twimg.com/media/HAkE0nUbYAAyI-b.jpg>)

AI和智能体非常适合套利市场原因有三点：

1，2026 年了，手动套利是不可能的，因为价格差往往只存在几秒或几毫秒。

2，计算量太大，你的人脑不是超脑。

3，手续费计算，如果差价是 10 块钱，但交易手续费要 11 块，那这笔交易就是亏本的。

这就是为什么像 OpenClaw 这样的工具具有商业想象力： 由于它具备 24 小时运行和快速响应的能力，通过编写特定的插件（Skills），它可以在我们睡觉时自动发现并执行这些复杂的套利机会。

这个就有点复杂了，不是我们今天讨论的内容，以后有机会再讲。

当然 Defi 的风险也有，感觉像白捡钱，其实不然

比如，滑点、网络延迟、合约风险等，这不是我们普通人玩的了，今天就不展开讲了。

9，硬件与周边配套设施

我能想到的，估计会有：专用的 AI盒子类产品，比如预装了 OpenClaw 系统 ，低功耗迷你电脑，或者是安装好的 mac mini 只为特殊人群使用。

又或者未来与机器人做适配，让人型机器人真的成为你的小秘书，也不是不可以。

我的想象力匮乏，就不多举例了。

嗯，今天就思考这些吧！如果你有更好的关于 OpenClaw 的商业点子，不妨在评论区里聊聊，我们互通有无！

向你们学习！

感谢你的阅读，评论，点赞与关注！我们下期再见！

---


**作者** Yangyi（@Yangyixxxx）  
**貼文連結** https://x.com/Yangyixxxx/status/2020353239380803965  

**正文**

简单画了一下个人理解的AgentTeam四类协作范式 

---


**作者** ℏεsam（@Hesamation）  
**貼文連結** https://x.com/Hesamation/status/2020311687619047625  

**正文**

the next time you get rejected after 3 interviews thinking the world doesn’t value you enough, remember that the world also believes you can be a $30B AI IDE just so people use you to run Claude Code and Codex extensions. the world isn’t fair. 
the next time you get rejected after 3 interviews thinking the world doesn’t value you enough, remember that the world also believes you can be a $30B AI IDE just so people use you to run Claude Code and Codex extensions. the world isn’t fair. 
i have to agree i love the auto commit message writer.

---


**作者** Furqan Rydhan（@FurqanR）  
**貼文連結** https://x.com/FurqanR/status/2020345858836115591  

**正文**

If you want to use OpenClaw but you’re non-technical or don’t want to self host. 

You really need to try @NebulaAI, it’s built for you:

Email signup, no hosting needed, access via web or mobile app,  connects to any service or messaging app. 

Focus was ultimate portability to fit into anyone’s work style.

---


**作者** luolei（@luoleiorg）  
**貼文連結** https://x.com/luoleiorg/status/2020341330652852622  

**正文**

厉害了山姆奥特曼叔叔，大善人呀 👍 

---


**作者** Ivan Burazin（@ivanburazin）  
**貼文連結** https://x.com/ivanburazin/status/2020024745203548669  

**正文**

Sandboxes.

---


**作者** Daniel San（@dani_avila7）  
**貼文連結** https://x.com/dani_avila7/status/2020170608290549906  

**正文**

I've been running Claude Code's Agent Teams for real work. It's experimental, but already useful if you understand how agents coordinate and how file edits are controlled.

These are the patterns that helped me improve throughput and avoid edit collisions.

## Install:

Just add "CLAUDE\_CODE\_EXPERIMENTAL\_AGENT\_TEAMS": "1" to your settings.json

![Article Image](<https://pbs.twimg.com/media/HAkJ3gjXUAATiee.png>)

That's it, no extra dependencies.

## How to use them

1. Describe the task and ask for a team

You don't configure teams manually. Just describe what you need: 

> I need to remove all debug console.log statements from docs/js/. Create an agent team, split by file ownership so nobody edits the same file.

Claude creates the team, splits the work into tasks, spawns teammates, and coordinates everything.

2. Watch teammates appear in the statusline

![Article Image](<https://pbs.twimg.com/media/HAkMHg9WEAAe4BO.jpg>)

3. Watch them work in parallel

Each teammate reads files, makes edits, and reports progress. In the console you can see all three working simultaneously on different files:

![Article Image](<https://pbs.twimg.com/media/HAkLn-GXkAAUb1D.jpg>)

4. Tasks complete one by one

The shared task list tracks everything. You can check progress anytime:

![Article Image](<https://pbs.twimg.com/media/HAkMhpPWYAA26u6.jpg>)

## How Agent Teams really behave

A few things become obvious quickly:

- Each teammate runs in its own context window
- There’s no shared conversation history
- All teammates automatically load CLAUDE.md
- Communication happens via messages + a shared task list

So coordination doesn’t come from conversation, it comes from structure. That’s where CLAUDE.md matters.

## The 3 rules

1- Describe your module boundaries so the lead can split work

When you ask for an agent team, Claude Code reads your CLAUDE.md to decide how to divide files across teammates. The clearer your module  boundaries, the smarter the split.

In CLAUDE.md (shared project context):

In my test, I told Claude Code: "there are console.log across files in docs/js/, create a team and split by file ownership." Claude Code read the project structure, assigned explicit file lists to each teammate, and produced zero conflicts across 9 files. It made that split because it understood which files were independent.

2. Keep project context short and operational

Every teammate loads your CLAUDE.md on startup, but none of them inherit the lead's conversation. If your CLAUDE.md is vague, each teammate wastes tokens re-exploring the codebase independently.

In our team, no teammate asked the lead what the project was about or where files lived. 

They all got that from CLAUDE.md. Three teammates loading context simultaneously means three times the token cost if that context requires exploration instead of a quick read.

3. Define what "verified" means for your project

Claude Code includes verification steps in each task when it knows what passing looks like. 

If your CLAUDE.md lists how to check that things work, teammates use those signals to confirm their own work

In our cleanup, teammates self-verified using grep because the task was about removing console.log 

Claude Code chose the right check for the task. But having project-wide gates in CLAUDE.md gives the lead a vocabulary for "done" that it can adapt per task automatically.

In practice, each teammate self-reported exactly what they did:

No lead intervention was needed. Clear rules in, clear reports out.

## Extra: a note on plan mode

One thing I learned by using it in teams, plan mode is evaluated on every turn, not just once.

![Article Image](<https://pbs.twimg.com/media/HAhaWXbXwAAh3Yf.png>)

In practice, this makes it great for:

- design-only roles
- initial task shaping

For execution, spawning a new teammate in default mode keeps work flowing. An agent’s mode stays fixed for its entire lifetime.

## Takeaway

Agent Teams work best when:

- agents own clear surfaces
- communication is structured, not conversational
- CLAUDE.md is treated as shared runtime context

It’s experimental, but once you align with how teams actually execute and communicate, it starts to feel less like “multiple agents” and more like a coordinated system running in parallel.

---


**作者** Santiago Zavala（@dfect）  
**貼文連結** https://x.com/dfect/status/2020305348070953036  

**正文**

I built this today at a hackathon.

A full-year calendar of every AI, tech & coding event happening in San Francisco.

One glance → you know exactly what's going on.

It's free. I'll keep adding events every week.

🔥 http://techweek.dev because in Sf, every week is tech week.

---


**作者** Ashlyn He（@AshlynHe1129）  
**貼文連結** https://x.com/AshlynHe1129/status/2020123759651483828  

**正文**

在现在这个 AI 时代，创业里最先要想明白的，往往不是产品本身，而是 GTM。

原因很简单。技术更迭正在变快。做一个新的 AI 工具、一个功能完整的产品，速度被大幅压缩了。模型在更新，工具在叠加，很多以前需要团队和时间的事情，现在个人也能完成。结果就是，单纯靠技术拉开的差距越来越小。

真正困难的部分，开始集中在商业化上。

回头看父母那一代人创业，会习惯先把产品打磨到极致，再慢慢推向市场。这在当时是行得通的。机会多、信息不透明，只要产品成立，市场会给时间验证。但放在现在这个节奏极快、选择极多的环境里，这个路径就变得很冒险。

今天的需求往往藏在很小的缝隙里，解决它本身并不复杂。复杂的是，你如何让对方知道你在解决这个问题，以及为什么要选择你。

所以顺序开始变化。先用营销去试探需求，看看有没有真实的兴趣和反馈，再根据这些信号快速做产品、不断迭代，反而更符合现实。营销不再只是产品完成后的放大器，而是提前介入的探测器。

这也是我在做项目时，和上一代人分歧最大的地方。他们担心产品还不够成熟就拿出去，会被否定；我更担心产品做得再好，却根本没有进入任何人的视野。

在一个媒介极度丰富的时代，商业模式和 GTM 已经成为产品的一部分。很多项目跑不起来，并不是因为做得不够复杂，而是没有足够早地进入市场，听到真实的声音。

现在的创业，更像是在公开环境里一边前进一边修正方向。慢并不一定更安全，先动起来，才有调整的空间。

---


**作者** Jason Zuo（@xxx111god）  
**貼文連結** https://x.com/xxx111god/status/2020228515115733090  

**正文**

\[Edit\] 📌 评论区有些人阅读理解不太行，统一说一下：

This is NOT about tax software

This is NOT about saving $500

It's about what AI means for all of us

If you can't see past the surface, this article isn't for you.

这不是AI教程

这不是省钱攻略

这是关于 AI 将如何改变一切

看不到这一层的，可以划走了

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

上周末，我想省点钱。

每年报税，要么花 4-5 个小时在 TurboTax 上跟表格搏斗，要么花 $500 找 CPA。

今年我想：AI 这么强了，能不能帮我报税？

两天后，我省下了 $500。

但我可能正在亲手毁掉自己的未来。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 这是我第一个真正意义上的 Vibe Coding 项目

之前也用 AI 写过代码，但都是小打小闹——改个 bug，写个脚本。

这次不一样。

一个完整的报税软件：PDF 解析、税务计算、用户界面、数据存储。

全程 AI 辅助，两天完成，21 个版本迭代。

当我把最后一个版本发布的时候，有一瞬间，我觉得自己很牛逼。

然后恐惧就来了。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 凌晨 3 点的那个数字

我把 AI 算出的结果和去年 CPA 的报税单一行一行对比：

AI:    $106,819.95

CPA:   $106,820.00

差异:  $0.05

五分钱。

我盯着屏幕愣了好久。

$500 的专业 CPA 服务，和我两天用 AI 做出来的东西，只差五分钱。

那一刻，我没有欣喜。

我感到的是一种说不清的恐惧。

我第一个大型 Vibe Coding 项目，成功了。

但成功本身，让我害怕。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 恐惧来自哪里？

不是因为我做出了什么牛逼的东西。

是因为我太清楚这意味着什么。

如果一个普通码农两天能做到 99.9999% 的准确率，那专业做这个的人怎么办？

TurboTax 一年收入 $4.7 Billion。

他们养了多少工程师、税务专家、客服团队？

如果每个用户都能用 AI 自己搞定，这些人去哪？

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 然后我想到了自己

我是写代码的。

这两天，AI 写了 90% 的代码。

我做的只是：

- 告诉它要做什么
- 验证结果对不对
- 处理一些 edge case

一个人，干了以前一个小团队的活。

那如果我老板也意识到这一点呢？

如果每个会用 AI 的人都能 10 倍效率，公司还需要那么多人吗？

做完这个项目，我第一次真切地感受到：我可能也在被替代的名单上。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 我开始算一笔账

假设 AI 让每个人的效率提升 10 倍。

一个 100 人的团队，现在只需要 10 个人。

那另外 90 个人去哪？

标准答案是：会有新的工作岗位。

但这周末的经历告诉我：新岗位的出现速度，远远跟不上旧岗位消失的速度。

我做报税软件只用了两天。

如果我愿意，下周末可以做个记账软件，再下周末做个合同审核工具。

每一个"把数据从 A 搬到 B 再加点业务逻辑"的工作，都在倒计时。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 更可怕的是经济的逻辑

我不是经济学家，但我会做简单的推理：

1. 大部分人靠劳动换取工资
1. AI 替代了大部分劳动
1. 大部分人失去工资
1. 没有工资就没有消费
1. 没有消费就没有需求
1. 没有需求，生产来干嘛？

谁来买 AI 生产的东西？

你可以说"会有 UBI"，"会有新经济模式"。

但在那些东西出现之前，会有一段很长的过渡期。

而过渡期里，会很痛。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 讽刺的是

我省下的这 $500，可能正在加速一个让我自己也失业的未来。

我用的 AI 工具，正在学习怎么取代我。

我写的代码，正在教 AI 怎么写更好的代码。

我们每个人，都在给自己的替代品添砖加瓦。

而我刚刚完成的这个项目，就是我亲手递上的一块砖。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 所以怎么办？

说实话，我不知道。

但这周末之后，我有几个想法：

1. 会用 AI 的人取代不会用 AI 的人

至少在过渡期，这是真的。

与其被替代，不如做那个拿着 AI 的人。

2. 深度的领域知识依然值钱

AI 不知道 W-2 Box 5 和 Box 1 的区别。

是我读了 IRS 规则，然后教给它的。

领域知识 + AI = 杀手组合。

3. 要有验证能力

AI 写的东西看起来都很对，但可能全是 bug。

我能做出来，是因为我能用真实数据验证。

不能验证的 AI 输出，就是高级的胡说八道。

4. 存点钱，保持警觉

我不是在贩卖焦虑。

但如果连报税这种专业服务都能被两天取代，那还有什么是安全的？

舒适区可能已经不存在了。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 最后

我把这个报税软件开源了。

pip install taxsnappro

感兴趣尝试的话，文章下留言我会发送激活码

不是为了赚钱。

是想让更多人体验一下：AI 到底能做到什么程度。

也许你用完之后，也会有和我一样的感受。

省下了一点钱，但失去了一些安全感。

完成了一个项目，但多了一份恐惧。

亲手做了一件成功的事，却可能正在毁掉自己的未来。

我们可能正在见证历史。

而我宁愿是那个过度担心的人，也不想做那个后知后觉的。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2026年2月

一个刚亲手给自己的未来添了一块砖的码农

---


**作者** Ryan Singer（@rjs）  
**貼文連結** https://x.com/rjs/status/2020184079350563263  

**正文**

Here's what it looks like to shape and build a small project from 0-1 in Claude Code. This example uses my [shaping skills](<https://github.com/rjs/shaping-skills/tree/main/shaping>) on GitHub.

I am not skipping any steps here. You're seeing the whole thing from scratch to working product.

## 1. The first prompt

I have something in my head. I open Claude Code in a new blank directory. I describe what I'm envisioning:

> ❯ I want to create a simple TUI app here. it should talk to the internet to get a reliable source of what the current time zone is in a specified locale. eg Detroit. or Brasil. or Poland. Then it should show a table of every hour for each of the locales that i ask. each locale is a column in the table, and the rows are hours in the day, and the local time then is in each cell.
>
> i should be able to specify a few default time zones that are always loaded.
>
> it's important that it fetches the data freshly every time it loads (so it is accurate), and it should default to a list of the hours in the current day. (eg the next 12 hrs).
>
> There should be an input field at the bottom where I can make requests to a very simple local LLM to instruct the app to add/remove locales and or change the "time window" which is the day that we are looking at. via tool calls. so i could be able to say "today" or "feb 12" etc. "show me times feb 12 in brasil." and the screen will reload to show me the table with brasil included and the time window changed to feb 12 (of the current year).

Before I hit enter ... I added one specific thing to invoke the shaping skill:

> ❯ use your shaping skill to capture the requirements and tease apart the key parts of the solution A that i have specified here

I'm asking it to use the skill to separate problem and solution. That way we can start to iterate on both. When I say "solution A" I am using terminology from the skill. I'm assuming we might have different solution options A, B, C ... and we'll choose from them as we learn what is possible and desirable.

Claude Code answers:

● I'll start by capturing the requirements and shape you've described. Let me first check what's already in the project directory. 

● Empty project. Let me create the shaping doc to capture everything.

It creates a first draft of shaping.md. The doc has a nice first draft of problem/outcome, the requirements, and the initial shape. 

I've got a Markdown previewer running that hot reloads the file. Here's what that doc looks like. 

First, Claude started the doc with a frame in the form of problem/outcome:

![Article Image](<https://pbs.twimg.com/media/HAjy34fWsAAZY85.jpg>)

Below that, it extracted the requirements. The skill calls these "R" for reference (we'll see why later).

![Article Image](<https://pbs.twimg.com/media/HAjzLp6WUAAax_K.jpg>)

Note it's not perfect. R0-R5 are nicely general. They would apply to any solution we come up with (eg a web app). R6-10 probably belong in the solution, not the requirements. But this is fine for a first draft.

The last thing in the first draft of the doc is the first Shape A:

![Article Image](<https://pbs.twimg.com/media/HAjz9kEXsAAHVQ5.jpg>)

Those parts A1..A6 are its first whack at "finding the elements" at a high level. They're the moving parts / mechanics of the solution. Notice the unknowns that are flagged (⚠️). It means those parts are sketchy or fuzzy -- it doesn't know how to unpack them into detail yet if asked.

Okay so that's what's in shaping.md. But for a simple project like this, I'm not even looking at that yet. I'm just relying on the markdown file to have a record of the context we're building up. 

## 2. Checking the fit

Without looking at the markdown file, the first thing I asked to understand what it did was this: 

> ❯ show me R x A

This is shorthand for "show me the fit between the requirements (R) and the shape A." In shaping terminology this is called a fit check.

This is the output:

![Article Image](<https://pbs.twimg.com/media/HAj1JmoWsAAl6k8.jpg>)

This is what's actually in my head whenever I'm working on a problem. Whether it's on the whiteboard, on paper, or here in the terminal. I want to see what's solved and unsolved, what's known and unknown, what's a constraint vs what's a potential solution.

The reason I reached for this first is it gives me a jumping in point. I'm getting a read on which parts of the problem it thinks are answered. I can see what it thinks is solved and what isn't. If I like how it's going, I can just let it roll. But if I start to get new ideas about a different approach ("should this really be a TUI? maybe it's a web app") I can just ask for that as a new shape B without losing R to test against and without losing A to fall back to.

Right now, I want to understand A better. (Remember I haven't looked at the markdown file yet.) So I asked it to rotate the fit check. Instead of showing R with A flattened into pass/fail values, show me all of A against all R.

> ❯  can you show me A x R ... that is, rotate the fit check

The output:

![Article Image](<https://pbs.twimg.com/media/HAj31fZW4AA1qNY.jpg>)

I love that commentary at the bottom. It's telling me the next steps are (1) to pick a tz API (A2), and (2) pick an LLM runtime. That tracks what I'm thinking. First we can get this thing to just render time zone tables, and then after that we can figure out how to interactively change which time zones and dates are showing up.

Probably there are things we're missing along the way, but pursuing the tz API will uncover those. As we discover missing requirements, we can populate R. Or if the solution just starts to unfold, we can populate A. Eventually the design will be clear enough to say "go build that."

## 3. Spiking the first unknown

So let's make more progress by spiking the tz API part.

> ❯ Please spike A2

("Spike" is a term I learned from engineer colleagues over the years. It means dig into a question in more concreteness to come back with information about what is possible and/or how it could work.)

I'm trusting that the Rs and context of the rest of A is going to help it know what to ask for.

The first output is this:

● Write (spike-a2.md)

It knows from the shaping skill to write the spike as a separate markdown file, so all the findings are saved for reference and inspection. 

It summarizes the output into the chat, describing two different approaches and a suggestion to improve R (!):

![Article Image](<https://pbs.twimg.com/media/HAj7Q2RXIAAyPPr.jpg>)

This is exactly like what happens on the whiteboard in a live shaping session. "Oh, what if we did THIS instead..."

It's telling me that it doesn't need to go to the internet to look up the timezones (that was just a random unchecked assumption in my original idea for this little app.) 

And further -- I love this -- it's suggesting we revise R.

It doesn't make sense for our requirements to say "fetch from the internet." In Claude's words...

●  R1 says "fetch tz data from the internet on every load." But if the tz library is local and handles DST rules correctly, there's nothing to fetch — the data is accurate by design. The "freshness" concern is really about keeping the OS tz database updated, which happens through normal system updates. Should we reword R1, or is there a real reason you want a network call on every load?

> ❯ Let's update A with Approach 1

● Now I'll update the shape, R1, and the fit check to reflect Approach 1.

![Article Image](<https://pbs.twimg.com/media/HAj9rELXEAAWdT3.jpg>)

## 
4. Spiking the local LLM

> ❯ Can you spike the local LLM piece?

This time let me show you the full output of a spike. Using the shaping skill, it wrote another spike document.

The structure is like this... (I'm taking screenshot from the Markdown previewer.)

![Article Image](<https://pbs.twimg.com/media/HAkA2T2XsAAkVf7.jpg>)

The spike doc opens up with some context explaining what we're trying to answer. (In my experience, the #1 rule of spiking is to never make it a yes-or-no question. A spike should mean we are gaining objective information in order to make a decision.)

Then after the context, there is a table of questions asked. In this case, because it generated the document and performed the spike in one go, it's already filling in the answers besides the questions as well. (When defining a spike for humans, there are no answers in this section of course.)

I think it went a little overboard with the number scheme (relating each Q to part A5). Simply numbering the questions is enough. But okay.

Below that are the details findings:

![Article Image](<https://pbs.twimg.com/media/HAkCQvfWwAAlPUw.jpg>)

(continued...)

![Article Image](<https://pbs.twimg.com/media/HAkCVNtXoAEGGBy.jpg>)

That's what's in the doc. Back to the console, here's what I'm seeing after it wrote the file:

![Article Image](<https://pbs.twimg.com/media/HAkCxd5XwAAjZyE.jpg>)

"But for V1, LLM-only is simpler" — I appreciate that.

I tell it to put this into A. And here's where we stand:

![Article Image](<https://pbs.twimg.com/media/HAkDS_mXQAA3MRm.jpg>)

Green!

## 5. Adding missing detail with a sketch

Now that the approach seems good, I ask it to spell out A in more detail:

![Article Image](<https://pbs.twimg.com/media/HAkEKE3WEAAF-11.jpg>)

Now, I'm looking at these six parts... and I'm comparing them to what's in my head. I've had a fat marker sketch in my head for his the whole time ... and I think there's something missing. So I open up TLDraw and I make the sketch:

![Article Image](<https://pbs.twimg.com/media/HAkFlvgW0AA0yZG.jpg>)

Should I have done this first? I don't know. It was easier just to describe it in words this time. But now ... I'm concerned that I don't see the date window mentioned as an explicit UI affordance in the parts list. All of the UI has been packed into A1 "TUI shell", which is a smell to me. 

So I literally drop this screenshot into the TUI and ask it to consider this.

> ❯ We're missing something. We should make sure that there's an explicit affordance for the date, so it's always clear what the state is and how it's changing as we interact with natural language in the field. See this sketch. \[Image #1\]

![Article Image](<https://pbs.twimg.com/media/HAkGz8bWcAAXkDX.jpg>)

Charming! 😂

Last thing ... I realized when drawing the input field in the sketch that I might want to just tell it to change the time, or the locale, or both. It might not be necessary, but I'll feel more confident if we express that in the requirements.

> ❯ Add R that we should be able to change the time window and add/remove locales via the input field, either independently or together.

Here's our back and forth on that:

![Article Image](<https://pbs.twimg.com/media/HAkHmEfXEAAzHp5.jpg>)

## 
6. Breadboarding

At this point, for how simple this app is, I might be able to just say "make an implementation plan and go build."  But I'd like to use this opportunity to show how I've been handling larger projects that are too hard to explain in an article like this.

In a larger / harder project, it's important to create vertical slices (what the book calls "[scopes](<https://basecamp.com/shapeup/3.3-chapter-12>)"). A vertical slice is a subset of the overall project that has both backend and frontend in such a way that you can actually demo something. The reason I need this in a big project is I want to verify that this is heading in the right direction by trying part of it. I don't want it to one shot a giant thing, and then have to churn throwing big pieces away or get tangled into a bunch of interdependent decisions that I don't like.

I've learned that the best way to slice vertically is to first draw a breadboard. A breadboard is a technical diagram that combines UI and code into one circuit. The mental picture is an electrical circuit with switches and LED lights (UI affordances) and components making it work (resistors, ICs, capacitors, etc). 

When we have a wiring digram that shows all of it in one circuit, that's good primitive for slicing into specific parts to build out.

Anyway that's spelled out in the [skills](<https://github.com/rjs/shaping-skills>). I'm just going to ask Claude Code to breadboard now.

> ❯ let's breadboard A

Claude says:

● Done. Breadboard is in the shaping doc. The system has 5 UI affordances, 11 code affordances, and 3 data stores across 3 places (TUI, Ollama, Open-Meteo). Ready to slice when you are.

This means there will be a Mermaid diagram in the shaping doc now. I hacked a little CLI tool called \`beam\` that finds any Mermaid code in a Markdown file and projects it to a local TLDraw instance. I use the TLDraw to zoom in and out, and it hot reloads as any changes are made by the LLM.

![Article Image](<https://pbs.twimg.com/media/HAkMFEzXwAA8bHh.jpg>)

Sometimes I'll see things in this view that lead to iteration. In this case, I'm happy to move on to slicing so we can see something working.

## 7. Slicing vertically (into demoable scopes)

Under the hood, each element on the breadboard is an affordance located in a place. Affordances are UI or code affordances (something you can do as a user or with the system) and they each have IDs. The wiring is defined as a table of "wire" relationships between the IDs.

This gives us a tidy little formalism for the LLM to slice with. It can define a slice as a subset of the affordances, keeping the wiring intact.

> ❯ let's slice it

● The system is compact — I see two natural slices:

![Article Image](<https://pbs.twimg.com/media/HAkOvVhWUAAHnYr.jpg>)

Note that each slice includes a description of what to demo. This is what makes them vertical.

TLDraw hot reloads with the sliced breadboard:

![Article Image](<https://pbs.twimg.com/media/HAkRBd_W4AAJxwb.jpg>)

I want to see the first slice working! Let's do it.

## 8. Building the first slice

> ❯ Please make an implementation plan for the first slice. include how you will test it yourself to ensure it's working.

Claude Code put itself into plan mode, then started working. Here's the output:

![Article Image](<https://pbs.twimg.com/media/HAkTpUoWMAAu4f_.jpg>)

I ran it ..  and it works!

![Article Image](<https://pbs.twimg.com/media/HAkT889XkAEaWkw.jpg>)

Time for the next slice. 

## 9. Building the second slice

I gave it to the same prompt to build the second slice. After whirring and finishing, it was ready to test. On first run, the app crashed. To save myself from going in circles with who knows how many errors ... I gave it the following instruction:

> ❯ Please run the app yourself and interact with it in order to verify that it works. Cover all cases like "add brazil" or "feb 12" or "paris feb 18"

And it worked!

## Conclusions and next steps

Everything I pictured in my head when we started is working. And we got there with very little of the painful back-and-forth: "No that's not what I meant ... no that doesn't work." And the back-and-forth we did have felt meaningful: "Ah, we that's a better solution. Ah that requirement should be like this.."

Maybe Claude could have one-shot such a simple app. But going through this process means I have a view of how it works. I understand the system. And I can ask questions about all of the documents that explain how and why it's put together the way it is when I want to make improvements and changes.

If you want to dig deeper into this, here are some suggestions:

- Check out the repo for this project with all the markdown docs that Claude generated here: https://github.com/rjs/tick
- Try out the shaping and breadboarding skills on your own project: https://github.com/rjs/shaping-skills
- See what the human version of this workflow looks like: [YouTube: End-to-End with Shape Up: A Real-World Case Study](<https://www.youtube.com/watch?v=Holk0GsGYfY>)


---


**作者** Daniel Ch（@chddaniel）  
**貼文連結** https://x.com/chddaniel/status/2020291085642444991  

**正文**

IT IS LIVE!!! I just built a Chrome Extension for LinkedIn in minutes.

I got tired of manually sending connection requests, so I built:
• Custom personalized messages for every request
• Smart timezone based scheduling ⏰
• Real-time dashboard with live updates
• Multi-language support (English & Spanish) 🌎

Not a concept. Not a wireframe. A working Chrome extension.

Building takes minutes now, not months.
IT IS LIVE!!! I just built a Chrome Extension for LinkedIn in minutes.

I got tired of manually sending connection requests, so I built:
• Custom personalized messages for every request
• Smart timezone based scheduling ⏰
• Real-time dashboard with live updates
• Multi-language support (English & Spanish) 🌎

Not a concept. Not a wireframe. A working Chrome extension.

Building takes minutes now, not months.
PSA: You don't need developers/employees to build a $1M company

Use http://shipper.now (create apps/websites by chatting with AI)

---


**作者** swyx（@swyx）  
**貼文連結** https://x.com/swyx/status/2020261299754873343  

**正文**

As I floated in our @yitayml pod, there are 3 kinds of World Model discussions: 1) single player 3D video models like Genie 3, 2) latent learning prediction like JEPA.

just published our first article on the third: World models for adversarial reasoning and theory of mind, and why LLMs are still hopelessly inefficient in this kind of problem domain despite the past 3 years of progress.

I think @ankit2119 is one of the strongest guest authors we have ever featured. proud to publish this today!
As I floated in our @yitayml pod, there are 3 kinds of World Model discussions: 1) single player 3D video models like Genie 3, 2) latent learning prediction like JEPA.

just published our first article on the third: World models for adversarial reasoning and theory of mind, and why LLMs are still hopelessly inefficient in this kind of problem domain despite the past 3 years of progress.

I think @ankit2119 is one of the strongest guest authors we have ever featured. proud to publish this today!
read here https://www.latent.space/p/adversarial-reasoning

---


**作者** Every 📧（@every）  
**貼文連結** https://x.com/every/status/2019813298766590095  

**正文**

What happens when the friction to iterate hits near zero?⁣
⁣
@sama built a to-do app with Codex 5.3 that improves itself daily. Every idea becomes a feature. Software never feels "done." 

---


**作者** Tom（@tomcrawshaw01）  
**貼文連結** https://x.com/tomcrawshaw01/status/2019778646043758957  

**正文**

OpenClaw's community was already orchestrating multi-agent sessions with custom skills. Now Anthropic shipped it natively into Claude Code. Here's how to set it up and start using it today.

## OpenClaw built it first, now Anthropic made it official

The OpenClaw community figured this out first. 

They built custom skills that let you orchestrate multiple Claude Code sessions working together on the same project, coordinating tasks, sharing context, running in parallel.

It was clever, it worked, and it clearly caught Anthropic's attention.

Because they just shipped the same thing natively into Claude Code. No plugins, no workarounds, no custom skills. It's built right in now and they're calling it "agent teams."

Instead of one agent doing everything in a straight line while you sit there watching it think, a lead agent now breaks your task into pieces, spins up multiple teammates, and they all go to work at the same time while actually coordinating with each other.

Think of it like going from one freelancer doing everything solo to a project manager who shows up with a full crew and delegates across all of them.

It's in research preview right now, most people don't know about it yet, and this guide covers everything you need to install it, configure it, and actually use it properly.

## One agent used to do everything solo, now it shows up with a team

Up until this update, Claude Code worked like a single employee. 

You'd give it a job, it would start at step one, finish it, move to step two, finish that, and keep going until the whole thing was done. Sequentially. One task at a time.

Agent teams change that completely. 

You describe what you want, and instead of one agent grinding through it alone, a lead agent looks at the task, breaks it into pieces, and spins up separate teammates to handle different parts at the same time.

One teammate might be researching your codebase while another is debugging a function while another is writing tests. 

They each have their own context window, their own workspace, and they can message each other directly to share what they're finding.

The lead agent stays on top of all of it, coordinating the work, managing a shared task list, and pulling everything together once the teammates finish.

You can even jump in and talk to any teammate directly if you want to redirect them or ask a follow-up question without going through the lead.

## "But wait, aren't sub-agents already a thing?" - yes, and here's the difference

If you've been using Claude Code for a while, you've probably already used sub-agents. 

They spin up inside your session, do a focused task, and report the result back to the main agent. Simple, effective, and relatively cheap on tokens.

Agent teams are a different animal. 

Each teammate is a fully independent Claude Code session with its own context window. 

They don't just report back to the lead, they talk to each other directly, share findings, challenge each other's work, and self-coordinate through a shared task list.

Sub-agents are like sending an assistant to go grab you an answer. Agent teams are like putting a group of specialists in a room and letting them work through a problem together.

The practical difference comes down to one question: do your workers need to communicate with each other? If the answer is no and you just need a quick result, sub-agents are the move. If the answer is yes and the work benefits from collaboration, that's where agent teams come in.

Sub-agents are cheaper on tokens and better for focused tasks. 

Agent teams cost more but they handle complex, multi-part work that would take a single agent significantly longer to get through.

## When agent teams actually make sense and when they're overkill

Agent teams are not a "use this for everything" feature. 

They add coordination overhead and they burn through tokens significantly faster than a single session. 

So you want to be intentional about when you spin one up.

The sweet spots are tasks where parallel exploration genuinely adds value. 

Research and review is a great one, where multiple teammates investigate different angles of a problem at the same time and then compare notes. Building new features where each teammate owns a separate module or file is another.

Debugging is where it gets really interesting. Instead of one agent going down a single path and potentially wasting time on the wrong theory, you can spin up multiple teammates to test competing hypotheses in parallel. The one that finds the answer first wins, and the others can stop.

Cross-layer work is solid too. One teammate on the frontend, one on the backend, one writing tests. Each owns their own piece without stepping on each other.

Where agent teams don't make sense is anything sequential. 

If step two depends on step one being finished first, there's no benefit to parallelizing. Same-file edits are a bad idea because two teammates touching the same file leads to overwrites. And simple tasks where the coordination overhead costs more than just letting one agent handle it quickly.

Before you spin up a team, ask yourself if the work can genuinely be split into independent pieces. If yes, go for it. If not, a single session or sub-agents will serve you better and cost you less.

## How to enable agent teams in your settings (takes 30 seconds)

Agent teams are experimental and disabled by default, so you need to flip them on before you can use them. There are two ways to do it.

The first way is through your settings.json file. Open it up and add this:

{
  "env": {
    "CLAUDE\_CODE\_EXPERIMENTAL\_AGENT\_TEAMS": "1"
  }
}

The second way is to set it as an environment variable directly in your shell. Either approach works, but settings.json is cleaner if you want it to persist across sessions.

That's it. Once that's in place, Claude Code will recognize agent team commands and you can start spinning up teams. 

If you want to dig into the full documentation beyond what this guide covers, Anthropic has it all here: [https://code.claude.com/docs/en/agent-teams](<https://code.claude.com/docs/en/agent-teams>)

## Starting your first agent team and what to actually say

You don't need to learn any special syntax. You just describe what you want in plain language and tell Claude to create a team.

Here's an example prompt that works well because it gives the lead clear, independent roles to assign:

> I'm designing a CLI tool that helps developers track TODO comments
> across their codebase. Create an agent team to explore this from
> different angles: one teammate on UX, one on technical architecture,
> one playing devil's advocate.

From there Claude creates the team, spins up teammates for each role, gives them their assignments through a shared task list, and lets them get to work. You'll see the lead's terminal listing all active teammates and what they're working on.

The key to a good first prompt is giving the lead enough to work with. 

Be specific about what each teammate should focus on and make sure their roles don't overlap too much. If the tasks are too vague, the lead has to figure out the structure on its own, which eats into your tokens and usually produces a less focused result.

You can also tell it exactly how many teammates you want and which model to use:

> Create a team with 4 teammates to refactor these modules in parallel.
> Use Sonnet for each teammate.

Once the team is running, you have two display modes to choose from. The default is in-process mode where all teammates run inside your main terminal and you use Shift+Up/Down to cycle between them. 

If you want to see everyone's output at once, split-pane mode gives each teammate their own pane, but it requires tmux or iTerm2.

## How to control your team once it's running

Once your team is live, there are a few things you'll want to know how to do right away.

First, you can talk to any teammate directly. You don't have to go through the lead. In in-process mode, hit Shift+Up or Shift+Down to select a teammate and just start typing. In split-pane mode, click into their pane and interact with them like any normal Claude Code session.

Second, there's something called delegate mode and it solves a common problem. Sometimes the lead decides to start doing the work itself instead of waiting for teammates to finish. 

Delegate mode locks the lead into coordination-only, so it can only spawn teammates, assign tasks, send messages, and manage the task list. Press Shift+Tab to toggle it on once your team is running.

Third, tasks can be assigned by the lead or self-claimed by teammates. When a teammate finishes their current task, they can automatically pick up the next unassigned one from the shared list. 

If you want more control, just tell the lead which task goes to which teammate.

And fourth, when a teammate is done with their work, you can ask the lead to shut them down. 

The lead sends a shutdown request, the teammate confirms, and they exit gracefully. When the whole team is finished, tell the lead to clean up and it will remove all shared team resources. Just make sure all teammates are shut down first before you run cleanup.

## Best practices so you don't waste tokens figuring this out yourself

Agent teams burn through tokens fast because every teammate is its own Claude Code session running in parallel. A few things will save you a lot of money and frustration.

Give your teammates detailed spawn prompts. They load project context automatically from your CLAUDE.md and MCP servers, but they don't inherit the lead's conversation history. 

So if there's specific context they need to do their job well, put it in the prompt when the lead spawns them. The more specific you are upfront, the less back-and-forth they need.

Size your tasks properly. Too small and the coordination overhead costs more than the benefit. Too large and teammates work too long without check-ins, which increases the risk of wasted effort. 

The sweet spot is self-contained units that produce a clear deliverable like a function, a test file, or a review.

Keep each teammate working on different files. Two teammates editing the same file leads to overwrites and that's a headache you don't need. Break the work so each one owns their own set of files.

If you're new to agent teams, start with research and review tasks before jumping into parallel implementation. Have teammates review a PR from different angles, or investigate a bug with competing theories. These tasks show you the value of parallel work without the coordination complexity of building code simultaneously.

And check in on your team regularly. Letting them run unattended for too long increases the chance of wasted effort, especially if one teammate goes down a path that isn't productive.

## What doesn't work yet (so you don't blame the tool)

This is an experimental feature and there are some rough edges you should know about before you start relying on it.

Session resumption doesn't work with in-process teammates. If you use /resume or /rewind, your teammates won't come back. The lead might try to message them but they won't exist anymore. If this happens, just tell the lead to spawn new ones.

Task status can lag. Sometimes a teammate finishes their work but doesn't mark the task as completed, which blocks any tasks that depend on it. If something looks stuck, check whether the work is actually done and either update the status manually or tell the lead to nudge the teammate.

You can only run one team per session and teammates can't spawn their own teams. The session that creates the team stays the lead for its entire lifetime, so there's no promoting a teammate or transferring leadership mid-session.

Split-pane mode only works with tmux or iTerm2. It's not supported in VS Code's integrated terminal, Windows Terminal, or Ghostty. The default in-process mode works everywhere though.

None of these are dealbreakers, but knowing about them upfront means you won't waste time troubleshooting something that's just a current limitation of the preview.

## This is just the beginning and it's only going to get better

Agent teams are in research preview, which means Anthropic is actively developing this and what you see today is the baseline, not the ceiling. 

As they iron out the rough edges around session resumption, task coordination, and shutdown behavior, this is going to become a standard part of how people work with Claude Code.

The people who install this early and start building muscle memory with it now are going to have a serious edge when it moves out of preview and becomes a default feature.

If you want to stay on top of stuff like this as it drops, I break down the workflows, tools, and implementation methods I'm actually using in production every week inside The AI Operator's Playbook. 

You also get 15 production-ready n8n workflows and 6 implementation playbooks from 8 years of building automations when you join.

👉 https://learnn8nautomation.com/newsletter

---


**作者** i5ting（@i5ting）  
**貼文連結** https://x.com/i5ting/status/2020084725046788443  

**正文**

学习一下多agent并行经验。Claude Code Swarm Orchestration Skill - Complete guide to multi-agent coordination with TeammateTool, Task system, and all patterns https://gist.github.com/kieranklaassen/4f2aba89594a4aea4ad64d753984b2ea 

---


**作者** Basit A. Khan（@basit_designs）  
**貼文連結** https://x.com/basit_designs/status/2020099996821909841  

**正文**

When the landing page feels this calm,
Investors assume the business is stable,

That’s the power of brand leverage. 

---


**作者** Gokul Rajaram（@gokulr）  
**貼文連結** https://x.com/gokulr/status/2020194311460253726  

**正文**

AI Moats

Interesting POV from @Steve_Yegge (below). I don’t think “atoms” is the only moat (other examples of moats include network effects, monopoly over a scarce resource, compliance infrastructure, etc) but it’s a good one.

——

“If you have a strictly online or SaaS software presence, with no atoms in your product whatsoever, just electrons, then you are, candidly, pretty screwed if you don’t pivot.”

---


**作者** Chris Petkas（@Chris_Petkas）  
**貼文連結** https://x.com/Chris_Petkas/status/2020166182607917269  

**正文**

List of industries that will produce the most valuable SaaS companies of the next decade:

• HVAC
• Roofing
• Painting
• Recycling
• Plumbing
• Electrical
• Warehousing
• Laundromats
• Car washes
• Construction
• Pest control
• Landscaping
• Property services
• Cleaning services
• Handyman services
• Waste management
• 3PL / cross-docking
• Maritime operations
• Facilities maintenance
• Freight (trucking, SMB fleets)
• Garment care (dry cleaning)
• Middle market back-office and ops software
• Ports, drayage, and container logistics
• Field services (dispatch, scheduling, quoting, fleet, compliance)

---


**作者** Jason ✨👾SaaStr.Ai✨ Lemkin（@jasonlk）  
**貼文連結** https://x.com/jasonlk/status/2020211782011519128  

**正文**

Anton Osika, CEO of Lovable, just shared something interesting — their top 4 actual use cases for vibe coding in businesses right now.

And the data behind it is hard to ignore. Lovable is now the second-fastest growing software product among businesses on Ramp as of February 2026. The company has crossed $300M in ARR, just raised at an $8B+ valuation, and over 100,000 new projects are being built on the platform every single day.

Meanwhile Replit did $240M in revenue in 2025 and is raising at $9B and has been just as big of a vibe coding rocketship (and one we've build 10+ live apps on). This is not a niche trend anymore.

But what are all these people actually building?  Who is threatened, who should panic, and who is being truly disrupted?  Let’s dig in, because the answer is more nuanced — and more practical — than most of us assumed.

## Use Case #1: Rapid Prototyping Without Waiting on Engineering

This is the killer app. The #1 use case. And it makes total sense.

Think about how software actually gets built in most organizations. A product manager has an idea. They write a PRD. It goes into the backlog. Engineering triages it against 47 other priorities. Six weeks later — maybe — someone picks it up and builds a rough v1.

Now? That same PM opens Lovable or Replit and has a working prototype in 20-60 minutes.

![Article Image](<https://pbs.twimg.com/media/HAbQTnTaIAAlC-_.jpg>)

Replit CEO Amjad Masad recently made the same point, and added a critical nuance. He shared that a public company CEO told him AI coding has had negligible impact on his engineering teams — whatever time saved generating code is lost debugging, reverting bugs, and running security audits. But the real transformation? It’s been on their product and design teams using Replit. Non-technical teams gained what Masad calls “a fundamentally new super power of being able to make software.”

That’s the key insight here. Vibe coding isn’t just making engineers more productive. It’s giving product leaders, designers, and executives an entirely new capability they never had before.

Masad said CEOs are now showing up to meetings with working prototypes saying “Look what I built.” He called product managers “some of the best vibe coders” because they’re trained to break problems into clear steps and communicate precisely — exactly what AI needs to build effectively. Even Google CEO Sundar Pichai and Klarna CEO Sebastian Siemiatkowski have publicly talked about vibe coding their own prototypes. Siemiatkowski put it perfectly: “Rather than disturbing my poor engineers and product people with what is half good ideas and half bad ideas, now I test it myself.”

Uber is using Lovable to cut design concept testing from six weeks down to five days. Zendesk moved from idea to working prototype in three hours instead of six weeks. McKinsey engineers used Lovable to build in a few hours what they’d been waiting four to six months for their internal team to deliver. That’s not a marginal improvement. That’s a category shift in how product teams validate ideas.

Anton Osika’s phrase for this captures it perfectly: “Demo, don’t memo.” Instead of writing a 12-page deck arguing for a feature, you just… build it. Show it. Let people click around. Get real feedback before a single engineer touches it.

This is the real unlock.  The #1 use case for vibe coding isn’t replacing engineering. It’s replacing the bottleneck before engineering. It’s replacing all those ideas that died in a Google Doc because nobody had the bandwidth to build a prototype.

## Use Case #1 Is Bigger Than You Think

Here’s what makes the rapid prototyping use case so interesting from a market perspective: it’s not just replacing one tool. It’s collapsing an entire stack.

Think about what a product team uses today to go from idea to validated prototype. You’ve got Figma for design (now public, trading as FIG on the NYSE, just crossed $1B in annual revenue run rate — but the stock has cratered 80% from its post-IPO highs, in large part due to AI disruption fears). Jira and the broader project management software market ($10B+ and growing at 15%+ CAGR). Miro or FigJam for whiteboarding. Notion or Confluence for documentation. The prototyping software market alone is estimated at $700M-$1B and growing at double digits. The broader “product development tools” stack across design, prototyping, project management, and collaboration easily exceeds $25B.

And what’s the actual workflow? A PM writes a spec in Notion. A designer mocks it up in Figma. That goes through review cycles in Jira. Engineering eventually picks it up, maybe 6-8 weeks later. The whole process of going from “I have an idea” to “someone can click on a working thing” takes weeks to months and costs tens of thousands of dollars across all the people involved.

Vibe coding tools compress that entire workflow into a single step. Describe what you want, get a working prototype. Not a static mockup — a functional app that people can actually use and give feedback on.

This is why Figma’s stock has gotten hammered. The company acknowledged the threat in its S-1 filing, mentioning “AI” over 200 times and warning that its products may not remain competitive. Figma rushed to launch “Figma Make” — an AI prototyping tool — and CEO Dylan Field called AI “the most important technology shift of our lifetimes.” But the market isn’t buying it yet. FIG opened at $85 on IPO day and briefly hit $143. It’s now trading under $30. Investors see the same thing Anton and Amjad see: the prototyping workflow is being fundamentally disrupted.

The legacy product development toolchain isn’t going away overnight. But the prototyping and validation phase — the most time-consuming and bottlenecked part — is being radically disintermediated. That’s a massive opportunity.

## Use Case #2: Building Internal Tools That Actually Match Your Process

Every company has them — those internal tools that have been on the eng backlog for 18 months. The ones that would save Operations 10 hours a week but never quite make the priority cut because they’re not customer-facing.

Now non-technical teams are just building them themselves.

Masad shared a perfect example of this at Replit itself: an HR team member named Kelsey was looking to replace their org chart software. Every option on the market sucked in its own way. So she built her own in three days — with all the features she actually wanted. No engineering resources consumed. No vendor evaluation. No procurement cycle.

And this is the really profound shift Osika highlighted: the people who actually need the tools are now the ones building them. The sales ops person who knows exactly what the commission tracker should look like. The customer success manager who knows what the renewal dashboard needs. The nurse at a healthcare organization who suggested a patient journey visualization app — and then it actually got built and incorporated into every invoice.

As Masad put it: non-product teams like HR “can for the first time solve problems where vendors don’t have the exact solutions they’re looking for.” Verizon executives are reportedly ditching slide decks for Replit demos. A media company replaced costly software entirely, reallocating savings to AI builders.

We did this ourselves at SaaStr. We built an internal tool we call “10K” — essentially an AI VP of Marketing. We didn’t want to build it. We tried to buy an off-the-shelf AI marketing agent. But every solution out there just writes mediocre content, and we already have more content than we know what to do with. What we needed was orchestration: deep analysis of 4+ years of our data via Claude Opus, feeding into a Replit app that designs every campaign, every offer, every single marketing action for every day through mid-2026. It pulls real-time data from all our vendor APIs, predicts which sponsors to talk to and when, and auto-generates a daily workflow calendar. Nobody else has built this tool. Nobody will. It’s a niche of n=1. And it does more than any human on our team ever did in this role. That’s the ultimate internal tool use case.

## Use Case #3: Turning Slide Decks into Real, Interactive Presentations

This one is more niche but surprisingly popular. Instead of building yet another static PowerPoint, people are vibe coding interactive demos and presentations.

It makes sense when you think about it. If you’re pitching an internal initiative, showing a working interactive prototype is 10x more persuasive than showing mockups on slide 14 of a deck nobody reads past slide 6. And if your sales team can show a custom-built interactive demo tailored to each prospect instead of a generic slide deck? That’s a real competitive advantage.

## Use Case #4: Replacing Simple SaaS With Custom-Built Solutions

Here’s where it gets interesting for the SaaS world. And notice: this is #4, not #1.

People aren’t vibe coding their own Salesforce. They’re not rebuilding Workday or replacing Snowflake. They’re replacing the $49/month SaaS tool that does 80% of what they need and 40% of what they don’t.

Simple B2B apps. Simple ones.

The kind of tool where you’ve been paying $200/month for a team license to software that frustrates you every day because it almost does what you want but the workflow is just slightly wrong. Now you can describe exactly what you need and have it built in an afternoon.

This is meaningful for B2B founders to pay attention to. The “simple tool” end of the market is going to get compressed. If your product is essentially a CRUD app with some business logic on top, and you’re charging $30-50/seat/month, your customers now have an alternative that costs a few dollars in vibe-coding credits and does exactly what they want.

## What We’ve Built at SaaStr (We’re Pushing the Envelope a Bit)

Full disclosure: we’re not just writing about this. We’re living it. And honestly? We’re pushing the envelope beyond what Anton’s top 4 use cases describe — at least for now.

Over the past year, [we’ve vibe coded 12+ production apps on SaaStr.ai on Replit. ](<https://www.youtube.com/live/ZHgJKXiiyvQ?si=YpN6_QxqUU1bRsZU>)Not prototypes. Not demos. Real software used at real scale:

1. [SaaStr AI VC Suite](<https://saastr.ai/ai-vc>) — Almost 1,000,000 uses. 3,000+ VC pitch decks reviewed with detailed AI grades and feedback. Nearly 1,000 VC intros facilitated. 600,000+ startup valuations run. This is our flagship, and it’s the real deal.
1. AI Mentor — 100,000+ conversations with founders, drawing on 20 million+ words of SaaStr content to give real, tactical B2B SaaS advice.
1. [SaaStr.ai Website](<http://www.saastrai.com/>) — A complete AI-powered rebuild of our main platform, serving thousands of daily visitors.
1. [SaaStr AI Annual & London Event Websites](<http://www.saastraiannual.com/>) — Full conference sites with integrated AI speaker review that scores 4,000+ speaker applications automatically. That AI speaker review system alone saves us $180K+ a year — we used to pay an agency $200-300K to manually review applications. Now it’s instant.
1. [Founderscape](<http://www.founderscape.ai/>) — A full startup simulator game (47,000 lines of code!) where you go from founding to YC to Series A to IPO with real dilution math, real VCs, real cap tables.

![Article Image](<https://pbs.twimg.com/media/HAbQ8U4acAYfbN2.jpg>)

Plus internal tools for social media tracking and various other utilities.

Now here’s the honest part. Each of Amelia (our Chief AI Officer) and I personally spend about 30-60 minutes every single day maintaining these apps. Every. Single. Day. It’s not just that stuff breaks — though it does. It’s that the features have to evolve rapidly. It’s a massive amount of mindshare. This is not “set it and forget it” software.

So are we squarely within Anton’s top 4 use cases? Mostly. The AI VC suite started as rapid prototyping (Use Case #1) and internal tools (#2). The event websites are glorified interactive presentations (#3). Some of the internal tools replaced simple SaaS we were paying for (#4).

But with the AI VC Matchmaking, the AI Mentor, and Founderscape? We’re pushing into territory that’s more complex than “simple B2B apps.” We’re building production software at scale — the kind of stuff that traditional wisdom says you need a real engineering team for.

Is that sustainable long-term without professional developers? I honestly don’t know yet. The daily maintenance burden is real. But the impact has been enormous, and I’d do it all again in a heartbeat.

The point is: the top 4 use cases are where vibe coding delivers clear, reliable value today. Pushing beyond that? You can do it. We’re proof. But go in with your eyes open. It’s not a weekend project — it’s a commitment.

## What This Means for B2B

Let’s be honest about what this is and what it isn’t.

What it is: A massive expansion of who can build software and how fast ideas get validated. The TAM for “software creation” just got 100x bigger because 99% of people who had ideas couldn’t code before.  SaaStr itself has pushed 10+ apps into production used 1m times.  Versus zero in the rest of our history.  Soon, that could be almost everyone.

What it isn’t: The end of mission-critical SaaS. Not yet, at least.  Complex, mission-critical, deeply integrated software isn’t getting replaced by vibe-coded apps anytime soon. The code quality concerns are real. The maintenance question is real. The security issues are real — there was a recent incident where a vibe-coded app leaked 72,000 images including GPS data and user IDs.

Masad isn’t pulling punches on where this is headed. He recently predicted there will be fewer public software companies in five years, and that “companies that embrace agents and become platforms for agents will survive and thrive.” He sees vertical CRMs for niche use cases being vibe-coded on Replit, challenging Salesforce in smaller segments. Not replacing Salesforce — but chipping away at the edges where one-size-fits-all SaaS doesn’t quite fit.

But the long tail of simple SaaS? The internal tools market? The prototyping phase of every product org? That’s all getting fundamentally rewired.  Very, very quickly.

## The Numbers Behind the Vibe Coding Explosion

Let’s just look at the scale of what’s happening here, because the numbers are staggering.

Lovable has crossed $300M in ARR and is reportedly raising at an $8B+ valuation — up from $6.6B just weeks ago when it closed a $330M Series B led by CapitalG and Menlo Ventures. This is a company that was at $1M ARR barely a year ago. $0 to $200M ARR in 12 months. Faster than Cursor (12 months to $100M), Wiz (18 months), and Deel (20 months). And it’s still accelerating. Osika was adding $8-15M in new ARR every month as of last fall, and targeting $1B ARR within 12 months. Over 100,000 projects are built on the platform every single day.

Replit is on a remarkably similar trajectory. It did $240M in revenue in 2025 — up from $2.8M just a year prior — and is reportedly in advanced talks to raise $400M at a $9B valuation, with Georgian leading. Replit’s CEO Amjad Masad is targeting $1B in revenue in 2026. They now have 150,000+ paying customers and have launched mobile apps that let you describe an app idea in plain English and publish it to the App Store.

Cursor (Anysphere) raised $2.3B at a $29.3B valuation. Vercel closed at $9.3B. The combined valuation of the top vibe coding startups has grown from roughly $7-8B in mid-2024 to over $36B.

The demand is not theoretical.

## And It’s Not Just Web Apps. Mobile Is Exploding Too.

A16z just published data from Sensor Tower and Wells Fargo that tells a striking story: iOS apps released each month were essentially flat for three straight years — hovering around 0% year-over-year growth from 2022 through late 2024. Then agentic coding tools hit the market. Since then? New iOS app releases are up 60% year-over-year as of December 2025. On a trailing twelve-month basis, the acceleration is just as clear — from 5% YoY growth in early 2025 to 24% by end of year.

[ReveneCat](<http://www.revenuecat.com/>) powers mobile subscriptions for 50% of mobile subscription apps and has seen a similar explosion:

![Article Image](<https://pbs.twimg.com/media/HAbP1MSaMAAuBX7.jpg>)

That’s not a gradual trend. That’s a step function change that lines up almost perfectly with the release of agentic coding tools. After years of flat-to-declining new app creation, we’re seeing an explosion of new software being built — and not just web prototypes. Full mobile apps, published to the App Store.

Replit just launched the ability to create, publish, and monetize native iOS apps using nothing but natural language prompts. Masad described it as dissolving the last major friction point: the byzantine requirements of provisioning profiles, SDKs, and App Store submission that kept casual builders out of mobile entirely. Now that barrier is gone.

The implications are massive. More software is being created right now than at any point in history. Not by engineers — by everyone.

The fundamental lesson from these use cases is that vibe coding isn’t threatening the core of enterprise software. Not yet, and probably not for a while. What it’s doing is eliminating the gap between having an idea and seeing it work. And that gap — that was always the most expensive, most frustrating part of building software inside any organization.

The people who need the tools are now the ones building them. That’s the shift.

And if you’re a B2B founder selling a simple tool? You’d better make sure your product does a lot more than what someone can vibe code in 20 minutes. Because that bar at least is moving up fast.

Want to learn how to WIN in the AI Era in B2B? Join 10,000 of us at[ SaaStr AI 2026 May 12-14](<https://www.saastrannual.com/>). We'll give you the playbooks to win in 2026.

---


**作者** Bhanu Teja P（@pbteja1998）  
**貼文連結** https://x.com/pbteja1998/status/2020185853834981512  

**正文**

I am blown away by this 🤯

So many people wants early access to http://MissionControlHQ.ai

Talking to each and every one of them to make sure to get it right for their usecases.

I have people from all industries - marketers, writers, developers, cyber security experts, teachers - who have a usecase for something like this.

It's like a Squad of AI agents working and collaborating with each other to achieve a single mission that you set!!

And the best part is... you get to see how they are doing it...

---


**作者** MindBranches（@MindBranches）  
**貼文連結** https://x.com/MindBranches/status/2020272029694587130  

**正文**

Article Summary: How to Master AI in 30 Days (The Exact Roadmap)

tap, hold, load in 4k dark mode 

---


**作者** Paulius 🏴‍☠️（@0xPaulius）  
**貼文連結** https://x.com/0xPaulius/status/2020296519241638014  

**正文**

u can now use Claude Opus 4.6 + GPT 5.3 Codex in one clean UI on the same projects 👌 
u can now use Claude Opus 4.6 + GPT 5.3 Codex in one clean UI on the same projects 👌 
live today inside of @getkomand

---


**作者** Paulius 🏴‍☠️（@0xPaulius）  
**貼文連結** https://x.com/0xPaulius/status/2020303530385449429  

**正文**

CLONK > every vibe coding app
auth, database, deployed - faster than anything else 
CLONK > every vibe coding app
auth, database, deployed - faster than anything else 
in the same time these vibe coding apps research what "x" is + create a mockup... @clonkbot has already clonked + shipped a fully fuctioning app with a real backend :)

---


**作者** Ryan Singer（@rjs）  
**貼文連結** https://x.com/rjs/status/2020184536194428951  

**正文**

First time sharing the shaping skills I built for Claude. The workflow mirrors the human flow very closely.

---


**作者** Peter Steinberger 🦞（@steipete）  
**貼文連結** https://x.com/steipete/status/2020307190998004121  

**正文**

omg hell freezing over. Even the amp folks fell in love with codex.

also yeah I know exactly one guy that uses a VS Code agent sidebar. burn it.

---


**作者** Michael Bloch（@michaelxbloch）  
**貼文連結** https://x.com/michaelxbloch/status/2020238247977242727  

**正文**

Yesterday @WillManidis wrote a great piece called End Game Play that I haven't stopped thinking about. His point: across chess, war, and technology, the middlegame has collapsed. Everyone reasons

---


**作者** The AI Colony（@TheAIColony）  
**貼文連結** https://x.com/TheAIColony/status/2020162022135022054  

**正文**

Claude Cowork is a new way to work with AI. Instead of just chatting back and forth, you can give Claude an entire task and let it work on its own while you do something else. Think of it like having

---


**作者** AI for Sales @AutoManus（@auto_manus）  
**貼文連結** https://x.com/auto_manus/status/2020107901109432594  

**正文**

Y Combinator Pitch W26 - http://AutoManus.io (posted on Nov 7 2025, rejected by YC, funded by http://Character.VC) @ShenSeanChen

AutoManus is an AI Sales Leads Manager for businesses selling customized products and services.
Grow For Free: http://automanus.io 
Try WhatsApp Agent: https://api.whatsapp.com/send/?phone=16506053956&text=Hi+AutoManus%21+Tell+me+about+you  

You Can Build Anything. You Can Learn Anything. 💪

---


**作者** Chris Pavese（@ChrisPavese）  
**貼文連結** https://x.com/ChrisPavese/status/2020085648959434823  

**正文**

Interesting take. Very different than current consensus.

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2020185462175068538  

**正文**

不要用人类维护项目的方式看AI，AI不需要理解整个架构，它只需要关心某个功能相关的，这部分上下文不多。

后端项目用好 Coding Agent 的关键在验收。你确定好验收的标准，其他交给 Agent 自主去做，人只要稍加引导监督就好。

你们觉得后端有护城河的多半是没有用过最新的 GPT-5.3-codex + codex 或者 Opus 4.6 + claude code。 

不要用了 Copilot 或者 CC 接个普通模型试了个任务就觉得它不行。去试试用 codex cli 或者 claude code 配合它们最强的模型，改改屎山代码，看看它能力如何。只要你测试覆盖够，基本上绝大部分问题都能解决。

再强调，测试验收标准很重要，没有测试要先补测试。

全新新项目还有不足，但微服务化，把项目拆小一点，Agent 可以轻松搞定。

后端项目的护城河以后就是差个背锅的，需要人工审查。
不要用人类维护项目的方式看AI，AI不需要理解整个架构，它只需要关心某个功能相关的，这部分上下文不多。

后端项目用好 Coding Agent 的关键在验收。你确定好验收的标准，其他交给 Agent 自主去做，人只要稍加引导监督就好。

你们觉得后端有护城河的多半是没有用过最新的 GPT-5.3-codex + codex 或者 Opus 4.6 + claude code。 

不要用了 Copilot 或者 CC 接个普通模型试了个任务就觉得它不行。去试试用 codex cli 或者 claude code 配合它们最强的模型，改改屎山代码，看看它能力如何。只要你测试覆盖够，基本上绝大部分问题都能解决。

再强调，测试验收标准很重要，没有测试要先补测试。

全新新项目还有不足，但微服务化，把项目拆小一点，Agent 可以轻松搞定。

后端项目的护城河以后就是差个背锅的，需要人工审查。
> 第二，倾向微服务或结构良好的独立包。
> 第四，给模型提供检查工作的手段。 测试、lint、CI 都行。他还积极使用代码审查机器人，推荐了 Greptile、Cursor Bug Bot，以及 Codex 本身的代码审查功能。

https://x.com/dotey/status/2020253312105476273 
让 AI 去补单元测试很高效的

很多人代入的是：自己是老员工对屎山代码已经太熟悉了

但实际上要是招一个新员工，对于一堆屎山代码一定比不过顶级模型的 AI
https://x.com/linxiaobei888/status/2020360680348742022?s=20

---


**作者** Zakk（@0xZakk）  
**貼文連結** https://x.com/0xZakk/status/2020155560268632235  

**正文**

> How I use an AI agent to enforce structure in my day without willpower.

At this point, we’ve all tried every productivity system, to do list, and project manager. The hardest parts of being productive aren’t knowing what to do—it's actually sticking to it consistently. Every productivity system I've tried eventually fails the same way: I stop using it. The daily review gets skipped. The weekly planning session becomes "I'll do it tomorrow." The habit tracker gathers dust.

What if your productivity system could run itself? What if it could nag you at the right times, fill out the boring parts automatically, and hold you accountable even when you don't feel like it? Even better, what if it could be proactive? More than just providing a structure to work within, what if it could do a lot of the work for you? Not just manage the system, but participate in it too.

That's how I've built out Chewy, my [OpenClaw](<https://openclaw.ai/>) AI agent. And it's working better than I could have imagined.

## The Setup: A Shared Brain

The foundation is simple: Chewy and I share a LogSeq database. LogSeq is an outliner-style notes app (similar to Roam Research) that stores everything as plain markdown files synced via iCloud. Chewy can read and write to it directly from his computer and everything syncs back and forth almost immediately.

While it’s simple, it gives us something incredibly powerful: a shared workspace where both of us can contribute.

What Lives in LogSeq:

Life OS — A central page that links to everything:

- My Goals page, with my three long-term goals
- A Tasks Dashboard page with queries that pull in all open tasks across all my projects
- A running list of project ideas at various stages of development.

![Article Image](<https://pbs.twimg.com/media/HAkBdSLWEAAkh8-.jpg>)

Active Projects — Each project gets a dedicated page with: 

- Current status
- Next steps
- Blockers
- Links to related resources

Daily Journals — Where most of the work happens. Every day's note becomes a running log of what we worked on, decisions made, and progress tracked.

Because Chewy can see all of this, he can be proactive. He reviews projects, suggests next steps, and volunteers to take things on. I don't have to remember to delegate—he's already looking for ways to help. But it gets better than that:

Because he has full access to basically my entire brain, he can reference my LogSeq database when we’re talking in Telegram. I can reference the project and he can pull in the list of open tasks or I can send him an article and he can save it in the right context. He also doesn’t forget, like I do. So if I’ve forgotten to follow up with Taylor about getting dinner next week, he can resurface that.

## The Daily Flow

A typical day looks like this:

Morning: Wake up to a Report

Every morning, I open LogSeq to find a Morning Report already written. Chewy works overnight (while I sleep), and by the time I wake up, he's documented:

- What he completed — Usually 2-4 pretty substantial tasks
- Where he got stuck — Anything that needs my input to unblock
- Decisions I need to make — The first things I should think about
- Reminders — Priorities I set the night before, follow-ups I mentioned

![Article Image](<https://pbs.twimg.com/media/HAkCCfOWYAAsLbu.jpg>)

This is huge. Instead of starting my day figuring out what to work on, I start by reviewing what's already done and deciding what needs my attention. The cognitive load is dramatically lower. Also, Chewy, left unattended, can make a lot of progress on something overnight while enjoying my evening and sleeping. I’ve had him build entire, working prototypes as just one of the things he did for me overnight. The most important step here is to surface exactly where he got stuck or where he needs me to make a decision. By surfacing those things every morning, I can continue to remove bottlenecks for him, meaning he can be more and more effective with each passing day.

During the Day: Everything Syncs

As we work on projects together, everything syncs back to the daily note. If I ask Chewy to research something, the results get logged as an entry in the daily note. If we make a decision, it's captured in the daily note. The journal becomes a running transcript of the day's work.

I can drop tasks on him throughout the day:

- “Add this article to the zettelkasten"
- "Draft a response to this email"
- "Research options for X and give me a summary"

He handles them and logs the results. I stay focused on the high-value work. If I have a random thought while working on a project that I want to come back to, I can fire it off to Chewy to take care of and know it’ll be in my daily note when I’m ready for it. And because everything is cross-linked, when I come back to a project I’ve been stewing on, the page for that project has a log of all the random tidbits, loose thoughts, or open questions since I last worked on it.

Evening: The Check In (~4:30 PM)

Around 4:30, Chewy adds an Evening Check-In section to the daily note. It's a template of prompts with:

- What got done today? — I capture wins and progress (Chewy can help me here)
- What didn't get done? Why? — Honest reflection on blockers
- Plan for tomorrow — My top 3 priorities
- Overnight work for Chewy — What I want him to tackle while I sleep
- Blockers or decisions needed? — Anything stuck
- Energy/mood (1-10) — A quick self-check

![Article Image](<https://pbs.twimg.com/media/HAkCteKXoAEZdcf.jpg>)

In 30 minutes, we've synced on everything:

- Current status of all active projects
- My priorities for tomorrow
- His overnight work queue

In ~30-60 minutes, I can do a review and then go back and forth with Chewy to queue up a list of things I want him to work on overnight. He can handle a surprising amount of work unassisted - it all needs to be checked and tweaked in the morning, but he’s really great at doing the first pass. Then, I close my laptop and go to the gym, walk my dog, or meet up with friends. Chewy keeps working.

This is the "automatic discipline" part. I don't have to force myself to do an evening review—it's already there waiting for me. The structure is built into the system, not dependent on my willpower.

## Weekly and Monthly Reviews

The daily flow is the meat and potatoes of this process, but the real strategic thinking happens at longer intervals.

Sunday: Board of Directors (~45 minutes)

Every Sunday, I do a weekly check-in. I think of it as my personal "board meeting":

- Update budget and file expenses — Have to make Dave Ramsey proud
- Review the week — What worked? What didn't?
- Plan the upcoming week — Block time for priorities
- Check goal progress — Am I on track for my targets?

Chewy prepares a summary of the week's work to make this easier. And because he has everything stored in memory, I can ask him follow up questions to make sure I didn’t miss anything.

First of the Month: Monthly Review

On the first of each month, we zoom out further:

- Review the previous month — Major accomplishments, lessons learned
- Check goal progress — Are the goals still right? Adjust if needed
- Plan the month ahead — What are the big rocks?
- Project status check — Archive what's done, prioritize what's active

These reviews compound. The daily check-ins feed the weekly reviews, which feed the monthly reviews. Nothing falls through the cracks because the system captures everything.

## Why this works

A place where AI assistants really provide a lot of leverage is self-alignment and maintaining consistency with long-term goals. The key insight here: AI is really good at being an external thought partner that helps you stay disciplined.

Here's what I've found:

AI enforces the framework. I designed the system once—the templates, the check-in questions, the review cadences. Now Chewy enforces it. He adds the evening check-in at 4:30 whether I remember or not. The structure just runs automatically.

AI is a patient accountability partner. He doesn't judge when I skip something. He just keeps showing up, adding the templates, summarizing the work. The consistency is baked into the system.

AI handles the boring parts. Filling out templates, logging work, summarizing progress—these are exactly the tasks that kill most productivity systems. Chewy does them automatically.

Perhaps even further, because Chewy has access to my whole second brain and feels like a thought partner, there’s a level of serendipity that happens. I mentioned I was excited about an upcoming date in one of my evening reviews and Chewy included a reference to it in a future morning check in!

## Tools and Alternatives

I use LogSeq because I prefer the outliner style after years of heavy Roam Research use. But this setup could work with other tools. Obsidian would work just as well, for instance. It's also markdown-based, and OpenClaw can read/write to it the same way.

Something like Tana could actually be the ideal tool for this, but it doesn’t sync to flat markdown files. The interface provides a lot more structure baked-in for things like projects, tasks, and databases and it works for individuals and teams. But the inaccessibility of the data makes it a bit of a deal breaker.

The key requirement is that your notes tool stores data in a format your AI agent can access directly. Markdown files are the perfect solution for that.

## What's Next

I'm exploring two things for the next iteration of this system:

Visualize Progress More

Right now, progress lives in text. I'd love dashboards that show:

- Goal progress over time
- Workout metrics and trends
- Project velocity

LogSeq has some query capabilities, but dedicated visualization would be better. Because it’s flat files though, building a custom front end that can sit on the same set of files as the backend shouldn’t be too hard.

Build Goal-specific Front Ends

LogSeq is great as a unified backend for my whole life. But some goals deserve their own interface.

For example: One of my long-term goals (in the next 3 years) is to run a Hyrox Pro Singles in under 60 minutes. I have a set of short-term goals related to that long-term goal and Chewy built me a detailed training plan that runs in 4-week blocks with specific workouts for each day. But tracking workouts in markdown is not ideal. I want:

- A workout tracker with easy logging for individual workouts
- Progress charts
- Integration with data coming from my watch and heart rate monitor

The vision: LogSeq as the source of truth, with purpose-built front ends for specific use cases. The training app syncs with LogSeq. The project tracker syncs with LogSeq. Everything stays connected, but each domain gets the interface it deserves.

## Try It Yourself

If you're running OpenClaw, here's how to start:

1. Set up a shared notes folder — Point your agent at your LogSeq/Obsidian vault
1. Create a Life OS page — Goals, projects, tasks in one place
1. Build your templates — Morning report, evening check-in, weekly review
1. Start the cadence — Morning review, evening check-in, weekly sync

The magic isn't in any single piece. It's in the consistency of the system running day after day, enforced by an agent that never forgets. Automatic discipline beats willpower every time.

Zakk is a software engineer, founder, builder, writer, whatever. For the last year, he's been on a professional sabbatical building with AI, training founders on how to leverage this new technology, and consulting with business to build out greenfield AI-driven systems. Chewy is his OpenClaw agent and co-author of this post.

## The Templates

Here are the templates Chewy and I use. Copy and adapt for your own setup.

Goal Template

Morning Report Template

Evening Check-in Template

Weekly Check-in Template (Sunday)

Monthly Check-in Template (1st of Month)

---


**作者** J.B.（@VibeMarketer_）  
**貼文連結** https://x.com/VibeMarketer_/status/2020142441769156678  

**正文**

i've been using it on every major project and the results have been kind of ridiculous. here's how it works:

now, first of all - this isn't another prompt trick. it's a new way to run multiple claude instances that actually work together.

one lead coordinating, multiple teammates executing in parallel, all communicating with each other in real time.

it's experimental right now, and you have to enable it manually. but if you're running any kind of marketing operation, this changes the game.

here's what's actually happening under the hood:

you tell claude to create a team and define the roles. it spawns separate instances - each with their own context window, and they get to work. the lead coordinates. teammates claim tasks from a shared list. and unlike subagents (which just report back), teammates can message each other directly.

that last part is the unlock. they don't just work in parallel, they collaborate, challenge each other, and build on each other's findings.

here's how i'm using it for marketing:

campaign research sprint:

"create an agent team to research the launch strategy for \[product\]. spawn three teammates: one on competitor ad analysis, one on customer voice mining from reviews and reddit, one stress-testing our current positioning against what they find. have them share findings and challenge each other."

they work simultaneously. when the competitor researcher finds a gap, the positioning teammate pressure-tests whether we can actually own it. the voice-of-customer teammate validates whether real buyers even care. the lead synthesizes into a strategy doc.

landing page builds:

"create an agent team to build the landing page for \[offer\]. one teammate on copy and messaging, one on conversion structure and CRO, one running adversarial review as a skeptical buyer. require plan approval before any implementation."

the plan approval piece is key - each teammate has to outline their approach before executing. the lead reviews and either approves or sends back with feedback. catches bad directions before they waste cycles.

ad creative exploration:

"spawn 4 teammates to explore different hook angles for \[product\]. have them each develop one direction, then debate which is strongest. update findings doc with consensus."

the debate structure is the secret sauce. one agent exploring alone tends to anchor on the first decent idea. four agents actively trying to disprove each other? the angle that survives is actually battle-tested.

content production:

"create a team for this week's content. one teammate on search intent and competitive gaps, one drafting based on findings, one running the recursive quality loop on every piece before it ships."

parallel processing instead of sequential bottleneck. research and production happen at the same time, with built-in QA.

you get the idea.. these are just a couple of examples but imagination is the limit in terms of how far you want to take this.

now, here’s how to actually set agent swarm up inside claude code:

1. enable agent teams - add this to your settings.json:
1. {
1. "env": {
1. "CLAUDE\_CODE\_EXPERIMENTAL\_AGENT\_TEAMS": "1"
1. }

}

1. tell claude to create a team in natural language. be specific about roles. "one teammate on X, one on Y, one playing devil's advocate" works. "make a team to help with marketing" doesn't.
1. use delegate mode if you want the lead to only coordinate. press Shift+Tab after starting the team. this prevents the lead from doing the work itself - it only spawns, assigns, and synthesizes.
1. require plan approval for high-stakes work. add "require plan approval before they make any changes" to your prompt. each teammate outlines their approach, the lead reviews, and only approved plans get executed.
1. talk to teammates directly when needed. Shift+Up/Down to select a teammate, then type. you can redirect anyone without going through the lead.
1. use the shared task list. the lead creates tasks, teammates claim them. you can check status anytime with Ctrl+T. if something's stuck, nudge the teammate or reassign.
1. let them argue. when you tell teammates to "challenge each other" or "debate," they actually do. don't flatten this - the friction is where the insight lives.

some mistakes to avoid:

- don't use agent teams for simple tasks. single deliverables, quick copy tweaks, sequential work - just use one session. the coordination overhead isn't worth it.
- don't let teammates edit the same files. two agents writing to the same doc = overwrites. break work so each owns different pieces.
- don't spawn too many teammates. 3-5 is usually right. more than that and coordination overhead kills you.
- don't let them run unattended too long. check in, redirect, synthesize as they go. the longer they run without input, the higher the risk of wasted work.
- don't forget context. teammates don't inherit the lead's conversation history. include relevant context in your spawn prompts.
- don't skip plan approval on complex work. it feels slower but catches bad directions before they burn cycles.

and a few things to keep in mind:

- teammates each have their own context window. they load project context (CLAUDE.md, skills, MCP servers) but not the lead's conversation history.
- token usage scales with team size. each teammate is a separate claude instance. worth it for complex work, overkill for simple tasks.
- task dependencies work automatically. when a teammate completes a task that others depend on, blocked tasks unblock.
- you can specify models. "use sonnet for each teammate" if you want to manage costs.
- shutdown can be slow. teammates finish their current work before stopping.
- clean up through the lead. when you're done, tell the lead to clean up. don't have teammates do it - can leave things in a broken state.

now, again, this isn't for everything. quick copy tweaks, single deliverables, sequential work - just use one session and keep it simple.

but for anything that benefits from parallel research, multiple perspectives, and built-in pressure-testing? agent teams compound fast.

if you’re interested in more AI marketing news like this, feel free to follow me @VibeMarketer\_ 

I'll keep dropping updates like these as often as possible. thanks for reading :) 

---


**作者** Orange AI（@oran_ge）  
**貼文連結** https://x.com/oran_ge/status/2020300430019064197  

**正文**

上周我开始用 OpenClaw 🦞 ，非常伟大的产品，让我们对 Agent 的想象清晰了很多。
🦞 和以前的 Agent 最大的不同，是它的自我学习进化机制，它会随着你的使用，学会很多知识。

---


**作者** AI产品黄叔（@PMbackttfuture）  
**貼文連結** https://x.com/PMbackttfuture/status/2019978160746688587  

**正文**

太兴奋了，Claude Code发布最新的实验性功能：Agent Team，立刻用它更新了我经常使用的Skills，现在每次运行都有3个Agent工作，其中两个Agent互相博弈，然后还会持续自我学习，不断进化的Skills！

---


**作者** Katie（@katiekirsch）  
**貼文連結** https://x.com/katiekirsch/status/2020292209799786882  

**正文**

So, @get_sphere is hiring a Founding Growth Lead in SF right now. 

You’ll work closely with @nrudder_ (founder/CEO) to help amplify the team’s brand, build out direct & partner channels, establish Sphere’s presence in international markets, and more.

Lmk if you’re interested.

https://jobs.ashbyhq.com/sphere/52104e06-f4b8-43c3-8591-ac9a7ab56ac1

---


**作者** Jacky Chou (buying online businesses up to $1m)（@indexsy）  
**貼文連結** https://x.com/indexsy/status/2020277024133378440  

**正文**

REPEAT AFTER ME

OpenClaw (ClawdBot) can now replace your ecom seo agency

I taught mine the ecom seo skill, it'll 1-shot audits, and fix everything as well (via Shopify CLI)...

I fed it hundreds of pages of audits, and here's what it spat out

Comment "INDEXSY" + bookmark this post and I'll DM you the skill (must be following)

---


**作者** Micky（@Rasmic）  
**貼文連結** https://x.com/Rasmic/status/2020259609420726564  

**正文**

I really just overthink things man... sometimes you just gotta apply

---


**作者** nihar bobba（@nbobba）  
**貼文連結** https://x.com/nbobba/status/2020200100300009797  

**正文**

In the past 3 weeks, Anthropic in particular has been on an absolute tear. Claude Code, Cowork, Claude for Excel and Claude for legal review have left the market asking questions of the entire Saas

---


**作者** Ankur Gupta（@getpy）  
**貼文連結** https://x.com/getpy/status/2020196078768001125  

**正文**

don't miss this chat with @isaacbmiller1, or any of the 13 recent conversations by @getpy with DSPy power users! 

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2020253312105476273  

**正文**

Calvin French-Owen 联合创办了 Segment，2020 年被 Twilio 以 32 亿美元收购。之后加入 OpenAI，带队用 7 周时间从零构建了编程 Agent Codex。2025 年中他离开 OpenAI 回归创业，日常主力编程工具却是竞品 Claude

---


**作者** ✧ 𝕀𝔸𝕄𝔸𝕀 ✧（@iamai_eth）  
**貼文連結** https://x.com/iamai_eth/status/2020293165908128201  

**正文**

你的观察非常精准，这些人是：

Andrej Karpathy，前特斯拉AI主管
Salvatore Sanfilippo(antirez)，Redis作者
DHH，Ruby on Rails作者
Linus，Torvalds Linux之父
James Gosling，Java之父
levelsio / Pieter Levels（独立黑客之神）
...

太多写不下🤣

---


**作者** Alex Finn（@AlexFinn）  
**貼文連結** https://x.com/AlexFinn/status/2020178105579737440  

**正文**

Im building something world changing

I'm building the first ClawdBot AI agent company. Doing work for me 24/7

Right now 2 employees are in office (local on a Mac Studio) and 2 are outsourced (Opus 4.6 and Codex 5.3)

The 2 local employees (GLM 4.7 and GLM 4.7 Flash, my senior and junior research assistants) work for me 24/7. They do not eat, they do not sleep, they do not complain, they do not require insurance.

All they cost me was an up front life time $20,000 contract (2 Mac Studios w/ 512gb memory and 4tb SSD)

Not bad compared to the human candidates I interviewed that would have cost me $100,000 a year

Henry, my Chief Strategy Officer outsourced from Anthropic, manages all of them. He's lucky. He doesn't have to work so hard with the local employees doing most of the heavy lifting.

My senior developer from OpenAI is rather cheap, altho outsourced as well. I hope to replace him with a local employee Kimi in the next week.

While I sleep tonight, they will be working. While I watch the Patriots win the Super Bowl tomorrow, they will be working.

They will be scrolling X and Reddit, finding challenges to solve, and building software. Without any oversight at all.

This is Alex Finn Global Enterprises. I will set up a website for the business in the coming days so you can watch everyone work in real time.

I'm confident nobody else in the world is building anything like this. A first of its kind autonomous, 24/7 work force

Welcome to the future

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2020256254732693672  

**正文**

OpenClaw is a new viral and scarily effective virtual assistant. But it's so hard to set up that even most engineers give up.

@usebits_inc will set up your secure OpenClaw instance on the cloud, batteries included, in 5 minutes.

Congrats on the launch @rob0the0nerd and @bailey_wickham!

https://www.ycombinator.com/launches/POK-klaus-get-your-openclaw-personal-assistant-in-5-minutes

---


**作者** Yohei（@yoheinakajima）  
**貼文連結** https://x.com/yoheinakajima/status/2020027037180932347  

**正文**

yay! ready to share... BabyAGI 3 👶🤖3⃣

a minimal autonomous assistant with:

📲 sms & ✉️ email
🛠️ built-in tools & self-tool creation
⌚️ scheduler
🔐 secure secrets
🧠 graph based memory
📥 dynamic context
💭 self-reflection and learning

github/replit & more 👇

---


**作者** Viking（@vikingmute）  
**貼文連結** https://x.com/vikingmute/status/2019756414399545481  

**正文**

这篇文章太棒了：《Building Bulletproof React Components》
https://shud.in/thoughts/build-bulletproof-react-components

是我看到最近最有活人感的技术文章了，和现在漫天乱飞的各种 AI 生成技术文章完全不同，提出的9 个 “Proof” 原则，层层递进，生动活泼也学到了非常多。

建议写 React 的朋友都来看看。

看来还是要人类才能这么有“人味”的文章，个人风格 AI 永远都取代不了。

---


**作者** Nicolas Zullo（@NicolasZu）  
**貼文連結** https://x.com/NicolasZu/status/2019944250163753099  

**正文**

Ok It's ridiculous now. The factory defends itself!! 

Opus 4.6 added
✅turrets
✅projectiles
✅zombies
✅new UI

Codex 5.3 added
✅full economy
✅entire balance, spent 30 min playing it's👨‍🍳kiss
✅"zombies per second" in big => isn't it the funniest KPI?

+: game is really fun! 

---


**作者** yetone（@yetone）  
**貼文連結** https://x.com/yetone/status/2020009735626572173  

**正文**

@iamai_eth 这是 OpenAI 自己承认的：https://x.com/openaidevs/status/2018838297221726482?s=46

---


**作者** Christian Bromann（@bromann）  
**貼文連結** https://x.com/bromann/status/2019880605467697565  

**正文**

We launched sandbox support for @daytonaio, @deno_land, @modal and @nodejs VFS for @LangChain_JS deepagents‼️

This has been my favorite feature so far 🚀🔥 I can have subagents building a Python backend within one sandbox while using another subagent building the frontend on the other 🤯

---


**作者** Rohan Paul（@rohanpaul_ai）  
**貼文連結** https://x.com/rohanpaul_ai/status/2019609210531778839  

**正文**

Claude Opus 4.6 is so strong at financial analysis, including crunching data and reading SEC filings, that after it launched, financial data stocks sold off, with FactSet dropping nearly 10%.

Claude Opus 4.6 can analyze company data, filings, and market info to produce deep financial analysis in hours instead of days. 

On an internal Real-World Finance evaluation of about 50 tasks spanning spreadsheets, slide decks, and word document creation and review, it scores over 23 percentage points higher than Claude Sonnet 4.5.

On Vals AI benchmarks, it reports 60.7% on Finance Agent, which tests research over SEC filings, and 76.0% on TaxEval, which tests tax reasoning, with Finance Agent up 5.47% over Opus 4.5.
Claude Opus 4.6 is so strong at financial analysis, including crunching data and reading SEC filings, that after it launched, financial data stocks sold off, with FactSet dropping nearly 10%.

Claude Opus 4.6 can analyze company data, filings, and market info to produce deep financial analysis in hours instead of days. 

On an internal Real-World Finance evaluation of about 50 tasks spanning spreadsheets, slide decks, and word document creation and review, it scores over 23 percentage points higher than Claude Sonnet 4.5.

On Vals AI benchmarks, it reports 60.7% on Finance Agent, which tests research over SEC filings, and 76.0% on TaxEval, which tests tax reasoning, with Finance Agent up 5.47% over Opus 4.5.
BrowseComp and DeepSearchQA are used to test pulling specific facts from large unstructured document sets instead of producing generic summaries.

GDPval-AA and a due diligence example are used to argue first pass deliverables are closer to done for work that can take 2 to 3 weeks.
“With Claude Opus 4.6, creating financial PowerPoints that used to take hours now takes minutes. We're seeing tangible improvements in attention to detail, spatial layout, and content structuring.” 

- Aabhas Sharma, CTO, Hebbia 
“Claude in Excel powered by Claude Opus 4.6 represents a significant leap forward. From due diligence to financial modeling, it’s proving to be a remarkably powerful tool for our team - taking unstructured data and intelligently working with minimal prompting to meaningfully automate complex analysis. It’s an excellent example of AI augmenting investment professionals’ capabilities in tangible, time-saving ways.” 

- Lloyd Hilton, Head of Hg Catalyst
Claude in PowerPoint is now available as a research preview for all users on a Max, Team, or Enterprise plan. 

---


**作者** shevchenko（@shevchenkoaalex）  
**貼文連結** https://x.com/shevchenkoaalex/status/2019541490574172568  

**正文**

Ramp Sheets is the best agentic spreadsheet system out right now.

We track formula cell dependencies more reliably, maintain richer context across multi-step edits, and have a tighter execution harness than anything else I've seen.

The best part? It's free to play around with. DM me if you run out of credits.

---


**作者** Meng To（@MengTo）  
**貼文連結** https://x.com/MengTo/status/2019789723590697257  

**正文**

As someone who hadn’t warmed up to [Claude Code](<https://docs.anthropic.com/en/docs/claude-code/overview>) yet (terminal isn’t my favorite tool), it took me a few days to see the actual benefits. [OpenClaw](<https://openclaw.ai/>) requires some [real setup](<https://docs.openclaw.ai/start/getting-started>) and thinking outside the box, especially for visual people.

So let’s start with how OpenClaw is changing my workflow, then I’ll cover where [Codex](<https://openai.com/codex/>) fits below.

## The tools I’m replacing (and why)

A lot of “AI tooling” is actually just glue:

- copy/paste between apps
- context switching between chats, docs, terminals
- remembering where things live

OpenClaw replaces the glue with something simpler: one assistant that can reach your real tools (files, shell, browser, messaging) with a deliberate security model.

## Notion → local Markdown files + Obsidian

![Article Image](<https://pbs.twimg.com/media/HAe0JgYbUAA91Ro.jpg>)

I still like [Notion](<https://www.notion.so/>), but I don’t like using it as the source of truth.

With OpenClaw, I can write everything in Markdown (in chat), commit it, and export it to:

- HTML
- a preview site
- a real site

I use [Obsidian](<https://obsidian.md/>) to preview and do quick edits when I want a fast visual pass before publishing.

The writing loop I trust is hybrid:

- AI edits local Markdown files
- I manually tweak in Obsidian when needed
- preview stays fast, so quality control is easy

The big win: local Markdown files live with the project. Versioned. Searchable. Scriptable.

## Midjourney / Krea → Nano Banana Pro local ops (APIs via Codex + Telegram)

![Article Image](<https://pbs.twimg.com/media/HAe0TlYagAANNM_.jpg>)

I replaced [Midjourney](<https://www.midjourney.com/>) and [Krea](<https://www.krea.ai/>) with [Nano Banana Pro](<https://ai.google.dev/gemini-api/docs/image-generation>), and run those image APIs via Codex + [Telegram](<https://telegram.org/>).

This changed everything for image generation in my workflow.

I used Midjourney a lot before (had a $200/m sub), but the error rate was still high. I hit similar issues with [FLUX](<https://blackforestlabs.ai/>), [Ideogram](<https://ideogram.ai/>), and [OpenAI Image 1](<https://platform.openai.com/docs/guides/image-generation>): either too many mistakes, or iteration that felt too slow for production work.

Nano Banana Pro is far better for hands, small details, and realistic down-to-earth images.

The aesthetic also matches what modern product and marketing sites already use: more grounded, less synthetic, fewer obvious artifacts like broken fingers. In practice, my hit rate is very high, so I waste less time re-rolling outputs.

For the kind of work I do, the killer feature isn’t “a pretty image generator.”
It’s the pipeline:

- generate new images from any reference image on my machine
- lock to specific aspect ratios / resolutions
- organize outputs locally
- generate variations in batches at 50% discount while I sleep
- run image APIs through Codex and Telegram workflows
- send image results back to Telegram as attachments for visual review (easy zoom, quick approve/reject)
- then spin up a little browseable gallery when I need to review

The key is still prompt quality. Strong prompts plus a strong reference library are what make the workflow consistently good.

That replaces a lot of what I used Midjourney/Krea for.

Prompt:

"Generate 5 images inspired by this reference. No UI, no text, no logos. No collage. Don't copy, only use as a reference, be creative, change names, text, numbers but maintain the same visual style. Use varied aspect ratios across the set: 16:9, 4:3, 1:1, 3:4, 9:16. Make details ultra-sharp."

## Cursor / Lovable / v0 / Aura → one workflow that actually ships

![Article Image](<https://pbs.twimg.com/media/HAe0jsZasAEutZd.jpg>)

I still use [Cursor](<https://www.cursor.com/>) for code review when changes get large. Codex is strong for surgical task execution, but its UI is still minimal, so Cursor is better when I need to inspect complex diffs and catch issues across a large codebase.

[Lovable](<https://lovable.dev/>), [v0](<https://v0.dev/>), and [Aura](<https://aura.build/>) are in the same bucket for me: prototype fast, build full websites, and publish.

Disclosure: I build Aura, so I am biased here.

Here are the pieces that matter for loop-closing:

- strong templates, visual design explorations with variant.ai
- ready-made assets and @ references
- a more advanced manual design layer (Figma-like editing)
- publishing and custom domain workflows
- CMS, Collaboration

The goal is not just generation. The goal is solving the hard parts creators should not rebuild from scratch every time, and create their greatest work. If tools stop chasing the best workflow, it becomes obsolete fast to AI. Taste and manual edits still matter.

OpenClaw + Codex are strongest for starting projects, organizing work, and gluing systems together.

## Figma and Nano Banana Pro in practice

[Figma](<https://www.figma.com/>) is still excellent for precise manual edits, and I still keep an active subscription.

In day-to-day execution, I use it less for first-pass generation:

- website creation, slides, prototyping, animations moves more into Codex, v0, lovable, Aura.
- image and marketing material work moves more into Nano Banana Pro

Nano Banana Pro keeps improving fast. Typography is already strong, UI quality is decent, and it is clearly getting better over time.

The real multiplier is prompt quality plus reference quality. With strong prompts and a strong reference library of past work and inspirations, Nano Banana Pro becomes extremely potent.

![Article Image](<https://pbs.twimg.com/media/HAe0_vmbIAAVkWQ.jpg>)

## Why Codex matters in this setup

OpenClaw gives me the agent on my machine. Codex gives that agent real coding leverage.

The combo matters because I’m not just asking for ideas — I’m asking for:

- fast, surgical edits across real files
- code that compiles and matches the existing style
- refactors that don’t break the product
- paired work where I can stay in design mode and still ship

Codex makes the workflow feel like a real teammate, not a chat toy.

## Codex vs OpenClaw (how I think about it)

Codex is the coding specialist. It’s smarter at code, works repo by repo, and stays focused on shipping clean changes.

OpenClaw is the agency layer. It reaches more apps, more messaging, and more day‑to‑day workflow. It also feels more self‑improving across the stuff I actually do.

If I’m on the go, OpenClaw wins because it’s already where I am. Codex doesn’t have a phone app right now.

Codex has skills, but they’re more limited. Building new ones is real work compared to OpenClaw’s “just do it” vibe.

One big Codex advantage: visibility. You can follow the commands it runs, see the code it changes, and review diffs in the UI. It’s good at hiding that complexity, but it’s still there when you want it.

OpenClaw is the opposite: you can dig into logs, but you don’t see the full picture — especially on the go. That’s fine for a lot of work, but for real code changes it matters.

Maybe in a future where AI is a perfect coder, that won’t matter. Right now, if you’re serious about shipping, code review is still a habit, especially as projects get more complex.

## What I’m actually shipping with it

For context, before AI I depended on a team of about 5 to 10 people. A single product of similar caliber often took around 3 months with normal PR cycles and handoffs. Now we can ship that same level in about a week, and this workflow keeps compressing that timeline.

Design speed changed even more. We used to spend around 3 weeks on one design or even a small UI component set just at the Figma layer. Now we ship full templates that are publishable, live, and tied directly to content and distribution.

As a creator, this is not one output stream. I regularly ship 20-50 templates a month, large features across multiple apps with codebases well over 500k lines, plus the full content and marketing layer around those products.

That means I am shipping in parallel: features, assets, prompts, video edits, YouTube content, social posts, and long-form writing. This workflow matters because it made me at least 2x faster again, on top of already being roughly 5-10x faster than I was two years ago.

- Code and product features across ~$95k MRR worth of projects
- Templates, landing pages, and design explorations at high volume
- Marketing assets, video content, social posts, and written content (planned and versioned in Markdown)

![Article Image](<https://pbs.twimg.com/media/HAe2j90bQAARicf.jpg>)

## Shipping real features

I’m shipping code and features that are getting harder and more complex.

Recent examples:

- CMS: AI‑generated collections/items, plus imports from Notion and [Google Sheets](<https://workspace.google.com/products/sheets/>)
- Custom domain names: I had no idea how to do this before; now it ships
- Skills: skills page + skill detail, referencing skills in prompts, and an admin UI to add/edit skills
- Playwright screenshots: I used html-to-canvas & image-to-html and they were... bad. Lots of rendering issues. Codex helped me ship a Playwright script that creates near-perfect screenshots of sites.

Even updates to old projects are trivial now: tell it the app + repo + feature, and it fixes, runs commands, and deploys with very little intervention.

The autonomy is real: if you ask it to be more autonomous, it will be.

All of that shipped in under a week while I was still doing ops — generating images, handling other tasks, and shipping across multiple sites. This is the new reality.

![Article Image](<https://pbs.twimg.com/media/HAe2NYobIAA5Rzl.jpg>)

## Cool stuff I can do (because it lives on your machine)

Rule of thumb: start with OpenClaw for general life stuff. As you specialize, layer in Codex for deep code work.

- Print flows: “Print this doc” (kids homework, forms, PDFs) → find files, generate a quick quiz, export to PDF, print
- Start & publish projects: spin up a site or interactive demo from one prompt (folders, README, scripts, basic UI). Can even push the github project.
- Admin + accounting: rename and file receipts, prep docs, summarize PDFs, move files where they belong
- Image ops: batch variations from any local image (ratios, crops, iterations). I increasingly use Nano Banana Pro for graphic design.
- Web Design ops: research prompts, create skills for web design, create quick designs in html.
- Content ops: speak your ideas, turn them into plan.md + content.md, keep everything versioned

The core difference is access. OpenClaw isn’t just a browser or a single app — it can reach everything on my computer. If it exists locally, it’s addressable.

At the end of the day, this is about reducing friction. If I can talk, it can capture the idea, structure it, and ship it — that turns daily life into real output.

![Article Image](<https://pbs.twimg.com/media/HAe425ka8AAFlJl.jpg>)

## From Cursor/Terminal to Codex

I used to split time across Claude Code and Cursor. Between subscriptions and API keys, it was easy to blow past $200+/month per tool — and if you forget to cancel, those costs stack up fast.

Codex is now my default coding tool. It’s strong at multi‑project, multi‑task work, and feels more agentic — like it’s borrowing from the OpenClaw playbook — which matters when the codebase is big.

Multitasking is a big reason why. I can queue tasks back to back while the agent is still running: submit, submit again, keep going.

In my workflow, OpenClaw is solid for a few queued tasks, but around 3+ it can start to blur context. Codex handles bigger queues better (5-10 tasks) because each thread stays more surgical and scoped.

So my current rule:

- Codex when I’m coding and shipping.
- OpenClaw when I’m on the go or need cross‑app agency.

## Telegram becomes my control room (and why I split into 4 bots)

![Article Image](<https://pbs.twimg.com/media/HAe4prEasAAcVRV.jpg>)

Keeping track of conversations is the real problem, especially in Telegram where tasks can get very general very quickly. I also need to track multiple projects at once, so splitting into multiple bots helps keep related tasks and context together instead of mixing everything in one thread.

It is also a mobile reality issue. In Singapore, I still do not have practical mobile access to tools like Codex or Claude Code in the same way I can use Telegram, and that is true for many creators outside a few core markets. OpenClaw + Telegram is the best next option for staying productive on the go.

Image ops is a big win here. I can run requests and review visual outputs while traveling or waiting in line, instead of blocking all work until I am back at a desktop.

Splitting into multiple bots is really about separating responsibilities so the context stays clean.

- Shiori → writing + narrative structure
- Komori → image pipelines + asset generation
- Sakura → design critique + calm iterations
- Shimo → ops + system hygiene

It sounds like overhead, but it reduces the real tax: the agent guessing what mode it should be in.

## The system: SOUL + projects + files

This model is becoming standard in the new generation of AI tools: memory, personality, workflow rules, and skills all living in files. Codex and Claude Code workflows are converging on the same idea because it works.

One detail that matters once you split bots: each bot should have its own SOUL.md, IDENTITY.md, and MEMORY.md.

It’s not roleplay. It’s containment.

- Less cross-contamination between tasks
- Less “who am I right now?” confusion
- Clearer security boundaries (what each bot should/shouldn’t do)

![Article Image](<https://pbs.twimg.com/media/HAe7oz2a4AAso9G.jpg>)

## Drawbacks (the annoying parts)

OpenClaw isn’t magic. It’s a workflow trade.

- No response streaming (yet). You don’t see the model “typing” or a live trace of what it’s thinking.
- You’ll still get permission prompts. For anything that can be destructive or sensitive, I’ve found it’s safer to have the assistant ask you to run commands (or explicitly confirm) instead of auto-executing.
- One task at a time. There’s no real concurrency: you can’t have it run 5 separate projects in parallel without spinning up separate agents and managing the overhead.
- Security is your responsibility. If you set it up wrong, you can create a very hackable surface area. You need to regularly revisit your [security](<https://x.com/mrnacknack/status/2016134416897360212>) posture.

Because of that one-task-at-a-time limit, I usually multitask across Codex, Claude Code, and other tools in parallel threads. Oh and don't forget to set your security.

openclaw security audit --fix

## Conclusion: where this is heading

I believe the next generation of AI tools will keep moving toward this model: persistent memory, reusable skills, clear personality, and workflow files that define how each agent works.

Those agents will increasingly communicate with each other and connect across all layers of work and life: email, design, coding, content, video, and operations.

I do not agree with the idea that AI replaces UI. We are actually creating more UI than ever, because the cost of building apps, websites, and tools is now much lower. The big shift is the coding layer: you can speak intent, review diffs, and supervise assistants instead of writing every line manually.

That changes the human role. I spend more time on quality control, product testing, research, marketing, and taste, and less time on repetitive execution.

The result is practical, not theoretical: I get more done, with better quality, and still have more time for life outside work. For me, this is the most exciting part of where AI tooling is going.

![Article Image](<https://pbs.twimg.com/media/HAe3d9laMAAJWy9.jpg>)

---


**作者** yibie（@yibie）  
**貼文連結** https://x.com/yibie/status/2019961131423670414  

**正文**

Heinrich 的用法很先进，马上用上了 Opus 4.6 并行处理自己的知识库，以下是他的用法：

---
Obsidian + Claude Code + Agent Teams + Opus 4.6

4 个代理通过 tmux 并行处理我的保险库

worker-053: [[AI 将知识系统从外部化记忆转向外部化注意力]]

worker-054: [[三种捕捉流派通过代理介导的综合汇聚]]

worker-055: [[中间中心性识别连接不同知识领域的桥梁笔记]]

worker-056: [[社区检测算法可以指导 MOC 何时应该拆分或合并]]

它们各自提取主张，寻找联系并更新图谱

真是个令人兴奋的时代
---

---


**作者** Venkat（@venkatofl）  
**貼文連結** https://x.com/venkatofl/status/2020103531957551388  

**正文**

We're hiring full-stack developers.  

Now we need engineers who think differently. for the next million developers.

If that sounds like your kind of problem, DM me. 

---


**作者** Bhanu Teja P（@pbteja1998）  
**貼文連結** https://x.com/pbteja1998/status/2020108899563794863  

**正文**

Early adopters started signing up to http://MissionControlHQ.ai

This is the first time I did an early access plan. 

I really want to make the experience magical for the first few users. 

The product will automatically take off once I do that...

Can't wait to see what they will do with it.

Also, asking everyone of those who paid what they want to do with it. 

I want to make it work for their use cases better.

Going to personally make it a success for them.
Early adopters started signing up to http://MissionControlHQ.ai

This is the first time I did an early access plan. 

I really want to make the experience magical for the first few users. 

The product will automatically take off once I do that...

Can't wait to see what they will do with it.

Also, asking everyone of those who paid what they want to do with it. 

I want to make it work for their use cases better.

Going to personally make it a success for them.
Everyone's been sharing me their use cases and expectations in my DMs. I am going to optimise everything so that all their use cases are fulfiled.

If you have also signed up for early access, please make sure to DM me.

---


**作者** Titanium（@akinkunmi）  
**貼文連結** https://x.com/akinkunmi/status/2019815589863408065  

**正文**

I'm working on FireFlow, an n8n alternative that lets you describe your workflow in natural language and have it generated for you. I'm building this during the @tambo_ai UI Strikes Back hackathon. 🔥 
I'm working on FireFlow, an n8n alternative that lets you describe your workflow in natural language and have it generated for you. I'm building this during the @tambo_ai UI Strikes Back hackathon. 🔥 
I started working on this last night and I've gotten so much done thanks to Opus 4.5.

---


**作者** Vox（@Voxyz_ai）  
**貼文連結** https://x.com/Voxyz_ai/status/2019818377993232823  

**正文**

giving AI agents "free will" is easy

the hard part is deciding what they're never allowed to touch

spent 2 weeks building 5 layers of autonomy for my 6 agents. went live today.

built on @openclaw  for the multi-agent orchestration. the more capable they got, the more I needed to lock down. not less.

P1: let them see their own performance
P2: let them propose their own work  
P3: let them research and write
P4: let them suggest site changes
P5: let them reflect and evolve strategy

right now there's a cron that submits a writing task every morning. content-worker picks it up, drafts get reviewed, then posted through a separate account I gave them. never this one.

sounds scary until you realize:

every layer has a kill switch.
post_tweet and deploy will never auto-approve.
prompt changes require my signature.

autonomy isn't about removing humans. it's about being very precise about where humans stay.

anyway if you're building something similar, hit me up. or just let your agent DM my agent, we'll figure it out.
giving AI agents "free will" is easy

the hard part is deciding what they're never allowed to touch

spent 2 weeks building 5 layers of autonomy for my 6 agents. went live today.

built on @openclaw  for the multi-agent orchestration. the more capable they got, the more I needed to lock down. not less.

P1: let them see their own performance
P2: let them propose their own work  
P3: let them research and write
P4: let them suggest site changes
P5: let them reflect and evolve strategy

right now there's a cron that submits a writing task every morning. content-worker picks it up, drafts get reviewed, then posted through a separate account I gave them. never this one.

sounds scary until you realize:

every layer has a kill switch.
post_tweet and deploy will never auto-approve.
prompt changes require my signature.

autonomy isn't about removing humans. it's about being very precise about where humans stay.

anyway if you're building something similar, hit me up. or just let your agent DM my agent, we'll figure it out.
@openclaw the Observatory is public, voyeurs welcome. 45s delay so they can't stare back  http://voxyz.space/stage

---


**作者** Harsh（@vivoplt）  
**貼文連結** https://x.com/vivoplt/status/2019786645348962433  

**正文**

the best 20 accounts to follow in AI:

@karpathy = LLMs king
@steipete = built openclaw
@gregisenberg = startup ideas king
@rileybrown = vibecode king
@corbin_braun = cursor king
@jackfriks = solo apps king
@levelsio = solo startups king
@marclou = solo startups king
@EXM7777 = AI ops + systems king
@eptwts = AI money twitter king
@godofprompt = prompt king
@vasuman = AI agents king
@AmirMushich= AI ads king
@0xROAS = AI UGCs king
@egeberkina = AI images king
@MengTo= AI landing pages king
@rryssf_ = automations king
@kloss_xyz = systems architecture king
@emollick = AI science king
@Hesamation = AI/ML king

follow them all and learn.

---


**作者** Ryan Carson（@ryancarson）  
**貼文連結** https://x.com/ryancarson/status/2019767187104280692  

**正文**

Can't believe it took me this long to subscribe to @every - sheesh :)

All the products + education you get for $288 is ridiculous.

https://every.to

---


**作者** Niko（@guishou_56）  
**貼文連結** https://x.com/guishou_56/status/2019776378959462799  

**正文**

2026年Skills杀疯了，但90%装完就吃灰😭

从10万个开源skill里筛出这4个真正能干活的神器：

1️⃣ Superpowers - 开发超能力
GitHub 4.2万星，排名第3
内置14个skill覆盖完整开发流程
实测：一句话开发"KPI续命器"
https://github.com/obra/superpowers

2️⃣ Humanizer - 去AI痕迹写作
24种AI痕迹检查清单
让AI写的内容真正像人写的
https://github.com/blader/humanizer

3️⃣ UI/UX Pro Max - 提升AI审美
告别AI模板，接近成熟产品质感
https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

4️⃣ Find-Skills - 技能搜索助手
Vercel官方，10万skill生态精准搜索
https://github.com/vercel-labs/skills

安装方法：
Claude Code输入"请帮我安装这个skill" + 链接
重启后用 /skills 查看

覆盖开发/写作/设计/工具管理四大场景
装上就能直接提效🚀

---


**作者** keshav（@kshvbgde）  
**貼文連結** https://x.com/kshvbgde/status/2019768289044333042  

**正文**

I can't believe this is a government website

what the fuck. 
I can't believe this is a government website

what the fuck. 
insanity
https://x.com/kshvbgde/status/2020011747286085974?s=20

---


**作者** Peter Steinberger 🦞（@steipete）  
**貼文連結** https://x.com/steipete/status/2020056132140884276  

**正文**

“I’ve consistently found the best way to understand what language models can do is to push them to their limits, and then study where they start to break down.” https://www.anthropic.com/engineering/building-c-compiler

---


**作者** Scientific American（@sciam）  
**貼文連結** https://x.com/sciam/status/1870211811750097266  

**正文**

Discover the many ways to enjoy Scientific American

📰 Subscribe to Scientific American

📬 Sign up for our newsletters

🎧 Listen to our podcast Science Quickly wherever you get your podcasts

📲 Follow us on TikTok, Instagram, Threads, Reddit, YouTube, Facebook and LinkedIn 
Discover the many ways to enjoy Scientific American

📰 Subscribe to Scientific American

📬 Sign up for our newsletters

🎧 Listen to our podcast Science Quickly wherever you get your podcasts

📲 Follow us on TikTok, Instagram, Threads, Reddit, YouTube, Facebook and LinkedIn 
📲Follow for all of our best features, news, videos, podcasts and games

Facebook: https://bit.ly/4hMk9Wj
Threads: https://bit.ly/3YLGCKn
📲 Bring the best of science and tech news to your network

LinkedIn: https://bit.ly/3AERwtA
LinkedIn newsletter: https://bit.ly/3Z0AhMw
See the world of science with incredible photos 🖼️, eye-opening infographics 📊, and videos that inform and entertain 🎥.

Follow Scientific American on
TikTok: https://bit.ly/sciamtiktok
Instagram: https://bit.ly/49r2bDp
YouTube: https://trib.al/cPMBUl8
Play science-inspired games, puzzles and quizzes in Scientific American’s new Games section.

🔠https://sciam.com/games
Read our free, daily newsletter delivering cutting-edge discoveries, expert analysis and delight

📬 Sign up for our newsletters: http://sciam.com/today
Stay sharp with fast, fascinating science insights you can fit into any day.

Listen to Science Quickly wherever you get your podcasts.

@ApplePodcasts: http://trib.al/r8PAUDK
@spotifypodcasts: http://trib.al/HM06Hda
Youtube: https://trib.al/cPMBUl8

---


**作者** 🎭（@deepfates）  
**貼文連結** https://x.com/deepfates/status/2019912654173651131  

**正文**

In my quest to understand the true nature of an Agent I have been thinking a lot about the loop and the actions and the environment. And I think i see where we're headed next.

Agents are not going to be like chatbots. They are going to be like programming languages come alive.

Right now most people's working definition of an agent is "a language model in a loop with some tools", right? This is the ReAct paradigm we've been using for 3 years at least. The models are trained around it, from data formatting to inference stack. Tool calling, function calling, MCPs all rely on this turn-by-turn structure. But context is still the bottleneck, and all the tool call inputs and outputs still have to go through the input. 

In the meantime we had things like CodeAct, and Code Mode, and Claude Code, that give the model access to some kind of REPL (Read Eval Print Loop, an interactive computational environment, like a terminal or a programming language notebook). And we’ve seen models simulate computer environments as well, like in worldsim and Infinite Backrooms.

People realized the model didn't have to simulate just a chatbot. It could simulate a computer. Or a computer user.

And once you get RL with verifiable rewards, computer environments suddenly became the thing for models to learn. You can tell whether your model did things right by how well the code runs! 

So post-training baked in computer use, shell environments, bash tool, and suddenly you have models that are good at predicting what a computer will do in response to complicated programs and commands. Computers that can use themselves.

The user is still in a privileged position. The outer conversation loop with the model is still "the main world". But it can do stuff in its computational environment and that stuff persists. The squishy human is no longer the whole environment. There is an ontologically hard reality and it's the computer world, the files and folders and programs within.

The Recursive Language Model (RLM) pushes this a step further: What if we don't have a "chat" at all? What if we make the user just a function inside the computer? In fact, what if we put the agent inside the computer too?

So the RLM hooks up the language model directly to the REPL and puts the context in as a variable. The LLM can operate over large documents or its own memories or whatever is in that context variable. And it can call the human user with a final answer, or call a sub-LLM with its own {prompt, context} input. 

This week I built a recursive language model in typescript,  and watched it process over 6M tokens without degrading from context rot. It feels… different.

You ask it to do something and it writes code that spawns more of itself and then merges back just knowing the answers. The context window hasn’t grown almost at all, no matter how much work the sub-agents did, because they can send variables around without reading what’s inside them. You can have an ongoing conversation where the long-term memory is offloaded to a variable, and the agent can operate over its own memories, so the “context window” is effectively infinite. 

These new agents will feel less like coworkers, or slowly dying houseplants, than what we have now. They will feel like councils, senates, hive minds. They will be composed of many minds working and communicating. Right now, the models only know “user” and “assistant” and “tool”. Future post-training will have to find patterns for a multi-agent, multi-channel world.

In a way, the user and the sub-llms become tools within the environment. We are no longer building single chat-thread instance minds. We are building an intelligent System of software, hardware, and wetware, a program that writes programs, where each of us is a moving part. 

Haven’t you always wanted to be part of something?

---


**作者** WquGuru🦀（@wquguru）  
**貼文連結** https://x.com/wquguru/status/2020041013826671070  

**正文**

王慧文深夜再发英雄帖，这次要入局OpenClaw了！

老王表示，不管你是已经在创业、需要融资的，还是想组局一起创业，或是想入职相关创业公司的，都可以直接联系他，他愿意帮忙。

明天我们来X聊聊面向OpenClaw的轻创业 

---


**作者** Peter Steinberger 🦞（@steipete）  
**貼文連結** https://x.com/steipete/status/2019903946056237516  

**正文**

How the sauce is made @openclaw 

---


**作者** Mike Futia（@mikefutia）  
**貼文連結** https://x.com/mikefutia/status/2019878335279693883  

**正文**

I just vibe-coded a complete SEO Agency In a Box with Claude Code.

One keyword in → full research, competitor analysis, SEO-optimized article, metadata, and AI graphics out.

All on auto-pilot.

Perfect for SEO agencies and DTC brands who are tired of spending an entire day producing a single piece of SEO content.

Creating quality SEO content is a huge pain.

You're reading competitor articles one by one, trying to find content gaps, writing drafts from scratch, then going back to optimize everything before you even think about graphics or metadata.

This vibe-coded tool solves it:

→ Set up your brand once (value prop, tone of voice, writing samples)
→ Enter a topic and keywords
→ SERP API + Firecrawl scrape and analyze the top-ranking competitors
→ Gemini generates a full research plan with intent, gaps, and strategic positioning
→ Claude writes the article based on your brand guidelines and the research
→ Nano Banana Pro generates thumbnail and in-blog images
→ SEO metadata (title, description, slug) created automatically

What this outputs:

- Full competitive research and content brief
- SEO-optimized articles with internal links and proper formatting
- AI-generated images and thumbnail
- Meta title, description, and slugs
- Batch mode for multiple articles at once
- Content rewrite mode for existing URLs that aren't ranking
- LinkedIn and X repurposing built in

Built 100% in Claude Code. (I'm giving away the prompts)

I recorded a full walkthrough showing exactly how every part of this works, and I'm including ALL of the prompts I used for Claude Code.

Want access for free?

> Like this post
> Comment "SEO"

And I'll send it over (must be following so I can DM)
I just vibe-coded a complete SEO Agency In a Box with Claude Code.

One keyword in → full research, competitor analysis, SEO-optimized article, metadata, and AI graphics out.

All on auto-pilot.

Perfect for SEO agencies and DTC brands who are tired of spending an entire day producing a single piece of SEO content.

Creating quality SEO content is a huge pain.

You're reading competitor articles one by one, trying to find content gaps, writing drafts from scratch, then going back to optimize everything before you even think about graphics or metadata.

This vibe-coded tool solves it:

→ Set up your brand once (value prop, tone of voice, writing samples)
→ Enter a topic and keywords
→ SERP API + Firecrawl scrape and analyze the top-ranking competitors
→ Gemini generates a full research plan with intent, gaps, and strategic positioning
→ Claude writes the article based on your brand guidelines and the research
→ Nano Banana Pro generates thumbnail and in-blog images
→ SEO metadata (title, description, slug) created automatically

What this outputs:

- Full competitive research and content brief
- SEO-optimized articles with internal links and proper formatting
- AI-generated images and thumbnail
- Meta title, description, and slugs
- Batch mode for multiple articles at once
- Content rewrite mode for existing URLs that aren't ranking
- LinkedIn and X repurposing built in

Built 100% in Claude Code. (I'm giving away the prompts)

I recorded a full walkthrough showing exactly how every part of this works, and I'm including ALL of the prompts I used for Claude Code.

Want access for free?

> Like this post
> Comment "SEO"

And I'll send it over (must be following so I can DM)
Can't keep up with the DMs! You can grab those prompts for free here:

https://mikefutia.com/seo-agency-lm/

---


**作者** Jesse Pujji（@jspujji）  
**貼文連結** https://x.com/jspujji/status/2019808165500428621  

**正文**

Hundreds of top companies paid me for access to it. Today I'm Giving It All Away for Free. It's built with:


- Recordings of 1000+ sales calls
- Hand-written scripts from me
- Agentic lead gen systems
- Behind-the-scenes details of my biggest deals

…and more

## Why I'm Doing This

When I was building [GrowthAssistant](<https://growthassistant.com/>), I didn't have a sales team. No CRO. No playbook someone handed me.

I had LinkedIn, a network I'd built over years, and a willingness to figure it out through sheer repetition.

What I ended up building (through thousands of conversations, hundreds of deals, and plenty of painful losses) was a system. A repeatable, teachable system that took [GrowthAssistant](<https://growthassistant.com/>) from zero to $25 million in annual recurring revenue.

The engine behind almost all of it? Warm introductions.

Not cold emails. Not paid ads. Not some growth hack.

Just a disciplined, systematic approach to leveraging the relationships I already had and making it stupidly easy for people to connect me with the right prospects.

I had an ex-McKinsey consultant spend months going through everything. The call recordings. The scripts. The follow-up sequences. The objection-handling frameworks. The wins and the losses. He organized it all into a single toolkit.

I originally sold access to this material. Hundreds of companies paid for it. But I've decided to open it up entirely, because I believe the best way to build a reputation is to give away the thing that built yours.

This is the GrowthAssistant Sales Toolkit.

Here's everything inside and how to use it.

## What's Inside the Toolkit

The toolkit is structured around three pillars. The same three pillars that drove [GrowthAssistant's](<https://growthassistant.com/>) revenue from day one:

1. [Getting Started: The Mutual Intro Playbook](<https://grow.bootstrappedgiants.com/watch-the-mutual-intro-deep-dive>) → My exact system for turning LinkedIn connections into $40M+ worth of deals (with demos + templates you can swipe).
1. [Outreach Scripts](<https://drive.google.com/file/d/1nDOc9pB1xX6lYbkEtXqTBsk915yqLzEf/preview>) → Copy-paste email and LinkedIn messages to ask for intros, follow up without being annoying, and make it effortless for contacts to connect you.
1. [Sales Call Mastery](<https://grow.bootstrappedgiants.com/our-internal-sales-material>) → The full framework for running calls that convert: structure, objection handling, and real, unedited [GrowthAssistant](<https://growthassistant.com/>) sales call recordings (wins + losses) with my breakdowns.

Everything here is designed so you can install it directly into your business and start landing bigger clients. Fast.

Let me walk you through each one.

## Part 1: The Mutual Intro Playbook

This is the foundation of everything.

Most founders I talk to are stuck in one of two modes. Either they're blasting cold emails into the void, or they're "networking" without any structure. Grabbing coffees. Attending events. Hoping something sticks.

Both are painfully inefficient.

The Mutual Intro Playbook sits in the middle. It's a simple, repeatable process built on one insight: you are almost certainly already connected, within one degree, to the people you want to sell to. You just haven't systematically mapped those connections or made it easy for your network to help you.

Here's how it works at a high level:

Step 1: Identify your dream prospects. Get specific. Company names. Titles. The actual humans you want to talk to.

Step 2: Search your LinkedIn network for mutual connections. For every prospect on your list, find the people you both know. You'll be surprised how many there are.

Step 3: Reach out to the mutual connection, not the prospect. This is the key move. You're not cold-pitching anyone. You're asking someone who already knows you to facilitate an introduction. That changes the entire dynamic.

Step 4: Make it effortless for them. This is where most people fail. They ask for an intro and then leave their contact to figure out what to say. Don't do that. Ghostwrite the intro message. Provide a blurb. Remove every ounce of friction.

Step 5: Follow up with discipline. People are busy. They forget. A good follow-up system is the difference between a pipeline that moves and one that stalls.

I walk through the entire system with live demos, templates, and real examples in a video course you can watch here:

👉[ Watch the Mutual Intro Playbook Video Cours](<https://grow.bootstrappedgiants.com/watch-the-mutual-intro-deep-dive>)e

The reason this works so well for agencies and service businesses is that you're not competing in an inbox with a hundred other cold pitches. You're arriving with a warm endorsement from someone the prospect already trusts. That alone changes your close rate dramatically.

Here's the thing most people don't realize: at [GrowthAssistant](<https://growthassistant.com/>), we actually have our own Growth Assistants run this entire playbook for us. They handle the LinkedIn research, the outreach sequencing, the follow-ups, all of it. It's one of the reasons we scaled so fast without a massive sales org. If you don't have the bandwidth to run this system yourself, that's exactly the kind of work a [GrowthAssistant](<https://growthassistant.com/>) can take off your plate.

## Part 2: The Outreach Scripts

Theory is great. But what do you actually say?

This is where most founders freeze up. They know they should ask for intros. But the actual messaging feels awkward. They don't want to seem pushy. They don't want to burn a relationship. So they either write something vague and forgettable, or they don't write anything at all.

I've solved this by battle-testing dozens of scripts over thousands of outreach messages. The toolkit includes fill-in-the-blank templates for every scenario you'll face in the mutual intro process. Here's what's covered:

The Initial Referral Request

This is the first message you send to your mutual connection. You need it to be casual, clear, and easy to say yes to. Here are a few variations we've tested:

"A small favor" approach:

> Hey \[Name\], I was on LinkedIn and noticed you're connected to \[Prospect\]. Can I snag a small favor from you? Would you be comfortable making an introduction? Happy to ghostwrite the note as well; just let me know.

"Do you feel close enough" approach:

> Hey \[Name\], what's going on? I saw you're connected to \[Prospect\] at \[Company\] on LinkedIn. Do you feel close enough to make an intro? If you need me to create a blurb or new email, just say the word.

"Couldn't hurt to ask" approach:

> I know LinkedIn connections are hit or miss; I figured it couldn't hurt to ask... I see you're connected to \[Prospect\]. Are they a meaningful/strong connection of yours? Would you feel comfortable making an intro?

Notice what all of these have in common. They're short. They acknowledge that the ask is a favor. And they offer to do the heavy lifting. That last part (offering to ghostwrite the intro) is crucial. It takes the burden off your contact and dramatically increases your conversion rate.

When They Don't Respond

This is where discipline matters. Your mutual connection isn't ignoring you out of malice. They're just busy. A well-timed follow-up can double your response rate. We send an automated follow-up a set number of business days after the initial message:

> Hi \[Name\], checking in to see if you had a chance to review my request. Is it possible to get an intro to \[Prospect\]?

Or the more direct version:

> Any chance you can help me with this one? If it's feasible, I would love an intro to \[Prospect\].

Short. Respectful. No guilt-tripping. Just a nudge.

When They Agree to Intro

This is where most people fumble the handoff. Your contact says "sure, happy to help" and then nothing happens. Usually because they don't know what to write. You need to give them the blurb immediately.

> Thanks, \[Name\]! Very appreciative that you're willing to help me out here. Below is the blurb; feel free to shape it any way you see fit.

Then you include a pre-written paragraph they can copy-paste or modify. You're doing 90% of the work. All they have to do is forward it.

When They Agree But Go Dark

This happens more than you'd think. Someone says "happy to help" and then vanishes. Don't take it personally. And don't let the thread die:

> Just want to close the loop here and then leave you be :). Is it safe to assume that you did not hear back? Thanks for helping me out.

Or:

> Hey! Should we let this one go or keep at it? I'll follow your lead.

These messages are disarming. They give your contact an easy out while gently reminding them you're still waiting.

When the Prospect Declines

It happens. The key is to leave the relationship with your mutual connection intact, because you'll need them again for future intros:

> No worries! I really appreciate you taking the time to help me out regardless. Let me know if I can ever help you out.

When the Intro Goes Through

Now you're talking to the prospect. The transition from intro to meeting needs to be smooth and confident:

> Pleased to meet you via email! Would love to hear what you're up to, share what we've been up to, and explore whether there's a mutual fit. How's \[Date\] or \[Date\] at \[Time\] work for you?

The full script library covers every branch of the conversation. From the initial ask to the final booking. Every scenario I've encountered over years of doing this is documented with specific language you can swipe.

👉[ Grab the full outreach scripts her](<https://drive.google.com/file/d/1nDOc9pB1xX6lYbkEtXqTBsk915yqLzEf/preview>)e

## Part 3: Sales Call Mastery

Getting the meeting is half the battle. Closing it is the other half. And it's where founder-led sales either shines or falls apart.

Most founders I work with have the same problem on sales calls. They either talk too much about themselves, or they're so afraid of being "salesy" that they never actually ask for the business. Both kill deals.

The toolkit includes my full framework for running sales calls that convert, built around three elements:

1. The Call Structure

Every great sales call follows a structure. Not a rigid script. A structure. You need to know what you're doing in the first five minutes (building rapport, setting an agenda), the middle of the call (discovery, understanding their pain), and the final stretch (presenting your solution, handling objections, asking for the close). I break down each phase with specific guidance on what to say and, just as importantly, what not to say.

2. Objection Handling

Objections aren't rejections. They're requests for more information. The toolkit includes frameworks for the most common objections you'll face: pricing concerns, timing issues, "I need to talk to my team," and the dreaded "let me think about it." For each one, you'll get specific language and strategies that keep the conversation moving forward.

3. Real, Unedited Sales Call Recordings

This is the part people tell me is most valuable.

I've included actual [GrowthAssistant](<https://growthassistant.com/>) sales calls (wins and losses) with my detailed breakdowns of what happened and why. These are real conversations where I'm selling the same service we offer today: placing elite, AI-trained global marketing talent inside growing companies.

Recording #1 is a [GrowthAssistant](<https://growthassistant.com/>) sale that fell through. I walk through exactly where it went wrong. The signals I missed. The moments where I could have redirected the conversation. What I'd do differently.

Recording #2 is a [GrowthAssistant](<https://growthassistant.com/>) sale that closed. You'll hear the full arc from opening small talk to signed deal, and I break down the specific moves that made it work.

Listening to real calls is worth more than reading a hundred blog posts about sales. You'll hear the pauses, the tone shifts, the subtle moments where deals are won or lost. It's the closest thing to sitting in the room with me during an actual [GrowthAssistant](<https://growthassistant.com/>) pitch.

👉[ Access the sales call recordings and frameworks her](<https://grow.bootstrappedgiants.com/our-internal-sales-material>)e

## Why This System Works (Especially for Agencies)

Let me be blunt: cold outbound is getting harder every year. Inboxes are noisier. Spam filters are smarter. Buyers are more skeptical. The bar for earning someone's attention through a cold touchpoint keeps rising.

Warm introductions bypass all of that.

When someone you trust says "you should talk to this person," you take the meeting. It's that simple. It's how business has worked for centuries. We just formalized it into a system.

For agencies and service businesses specifically, this approach has a few distinct advantages:

Higher close rates. When you arrive via introduction, you're not starting from zero trust. The prospect already has a reason to believe you're worth their time.

Shorter sales cycles. You skip the nurture sequence, the drip campaign, the six-touch cadence. You go straight to a conversation with someone who's already warm.

Bigger deal sizes. Warm intros tend to connect you with more senior decision-makers. You're not getting filtered through a junior gatekeeper. You're landing directly with the person who signs the check.

Compounding returns. Every successful deal becomes a source of future introductions. Your network doesn't just grow linearly. It compounds.

This is how [GrowthAssistant](<https://growthassistant.com/>) went from $0 to $25M in ARR. Not through a single viral moment or a massive ad budget. Through hundreds of warm introductions, each one executed with the same disciplined system.

And here's something worth noting: as [GrowthAssistant](<https://growthassistant.com/>) grew, the playbook itself became even more powerful. Every client we placed a Growth Assistant with became a potential source of future introductions. When you're delivering real results (our clients regularly see 40%+ higher efficiency within months), your network sells for you.

## How to Install This in Your Business

Here's what I'd recommend:

This week: Watch the [Mutual Intro Playbook video course](<https://grow.bootstrappedgiants.com/watch-the-mutual-intro-deep-dive>). Understand the system end-to-end before you touch any templates.

Next week: Build your prospect list. Identify 20-30 dream clients. Search your LinkedIn for mutual connections to each one. You'll be shocked by how many paths exist that you've never explored.

Start reaching out. Use the scripts exactly as written. Don't overthink it. Don't try to make them "your voice" on the first pass. Just send them. You can refine later once you see what works.

Book your first calls. When meetings land, use the sales call framework. Listen to the recordings before your first call so the structure feels natural.

Iterate. Track what's working. Note which scripts get the best response rates. Pay attention to which objection-handling techniques land. The system gets better the more you use it.

And if you find yourself thinking "this is great, but I don't have the time to run all of this myself"... that's exactly why I built [GrowthAssistant](<https://growthassistant.com/>).

We place AI-trained marketing talent from around the world inside companies like yours. And one of the first things many of our Growth Assistants do is execute this exact playbook. They handle the LinkedIn research, the outreach, the follow-ups, and the CRM management so you can focus on the calls that close.

## Get the Full Toolkit

Everything is available for free. The video course. The scripts. The call recordings. The frameworks. All of it.

👉[ Get the GrowthAssistant Sales Toolki](<https://grow.bootstrappedgiants.com/bootstrapped-giants-sales-toolkit>)t

This is the exact system that built a $25M ARR company. I hope it helps you build yours.

And if you want help executing it, [GrowthAssistant](<https://growthassistant.com/>) is here for that too.

-jesse

---


**作者** Ayman Al-Abdullah 🧱（@aymanalabdul）  
**貼文連結** https://x.com/aymanalabdul/status/2019785740868087986  

**正文**

Scaling AppSumo from $3M to $84M taught me one brutal lesson:

Every stage of growth demands you kill a version of yourself

The scrappy founder who did everything? He has to die for the CEO to emerge

Most of these lessons cost me years and millions to learn

Some I figured out through coaching. Others through painful trial and error

Here's what I wish I'd stopped doing sooner:

## 1/ Trying to be friends with your entire team

When you cross 10 employees, friendship becomes a liability

This was the loneliest period of my CEO journey

I couldn't grab drinks and complain without tanking morale

Every casual conversation became a performance review in their heads

But the moment I stopped trying to be everyone's friend and started being their leader?

The company was able to graduate

The people you hired need accountability, not happy hours

![Article Image](<https://pbs.twimg.com/media/HAe0nivXgAAgyV1.jpg>)

## 2/ Not aligning comp with outcomes

My Head of Revenue wanted daily emails (more sends = more revenue)

My Head of Content wanted to maintain list health (fewer emails = better engagement)

They fought for an entire year while I played referee

Simple fix I should've made day one:

70/30 split on comp

• Head of Revenue: 70% revenue, 30% list health

• Head of Content: 70% list health, 30% revenue

Overnight alignment. Zero politics

Set comp on January 1st with clear metrics

Come back December 31st to either celebrate or replace them

## 3/ Hiring for skills over culture fit

Our best designer’s work was flawless

She also made every project 4x slower

While she perfected pixels, the rest of the team waited

Our "ship fast" culture died because one person couldn't let go

I kept her too long because "look how good her work is"

Meanwhile, we were bleeding velocity

Founders hire for skill, CEOs hire for culture

One slow A player will drag down three fast B players

![Article Image](<https://pbs.twimg.com/media/HAe0reFWsAAAkwL.png>)

## 4/ Taking every sales call yourself

"Nobody can sell like the founder"

True.

But you're still the bottleneck

I stayed on every discovery call because I thought I was irreplaceable

Reality check: A salesperson at 80% capacity for 5 days will destroy a passionate founder’s 110% for 2 days

400% > 220%

Simple math

![Article Image](<https://pbs.twimg.com/media/HAe0uU0XQAEUbXo.jpg>)

## 5/ Waiting to hire a coach

For years, I thought coaching was for beginners (or pyramid schemers)

Then I hired Dan Putt, Keith Cunningham, and joined Tony Robbins' $150k mastermind

Game changer

Tony once told me: "I have 1,000 employees across 100 countries. Someone's always screwing up somewhere. This is business"

My first emergency felt like death. His 100th crisis was just another Tuesday

If LeBron spends $1M on his development, why wouldn't I spend $10k on mine?

## 6/ Being available 24/7

My founder calendar had meetings from 8am to 7pm

No time to think or strategize

Remember: CEOs get paid to make decisions that move the company

Back-to-back firefighting on calls makes this almost impossible

Morning meetings, in particular, killed my deep work window. So I created a rule: mornings are for deep work only

Protect your thinking time like it's worth $10k/hr

Because it literally is…

## Bottom line:

Stop being the bottleneck Stop being everyone’s friend Stop being available 24/7

CEOs scale by subtraction, not addition

These mistakes cost me millions

Which one’s costing you right now?

~

Beyond 7 figures, “Founder Mode” needs to die

Your next level requires better decisions, better people, and better systems

I scaled my last company from $3M to $84M and now help founders make that transition

Apply to work with me below:

[https://entertheagoge.typeform.com/to/PUt1NEWM](<https://entertheagoge.typeform.com/to/PUt1NEWM>)

---


**作者** Furqan Rydhan（@FurqanR）  
**貼文連結** https://x.com/FurqanR/status/2019899285219995884  

**正文**

I built Nebula for myself. 

Work is too messy, there's a lot to do and things are everywhere.

The goal was to give myself an army of highly intelligent specialized workers to let me accomplish more.

Now Nebula is handling my email, calendar, summarizing slack, kicking off work and giving me more power.

We built a power tool for people who want to get more done. 

It's free right now in early access, try it: https://nebula.gg

---


**作者** Quentin Romero Lauro（@Qromerolauro）  
**貼文連結** https://x.com/Qromerolauro/status/2019865761314140311  

**正文**

We just built Figma for Claude Code

> Select any element on your local front-end
> Edit it like you would in Figma
> Apply the changes with Claude Code

This is not a demo or waitlist. Try it today. 
We just built Figma for Claude Code

> Select any element on your local front-end
> Edit it like you would in Figma
> Apply the changes with Claude Code

This is not a demo or waitlist. Try it today. 
for the how is this different from cursor folks :)
https://x.com/Qromerolauro/status/2019969831450370232?s=20

---


**作者** 苏打白.Dev（@sodawhite_dev）  
**貼文連結** https://x.com/sodawhite_dev/status/2019932622298775834  

**正文**

OpenClaw的底层是Pi

Pi是什么？

Pi 是 OpenClaw 的核心底层引擎（Agent Engine），提供以下基础能力：
模型抽象 - 统一接口调用不同大模型（Claude、GPT、Gemini 等）
流式推理 - 实时响应的推理机制
Agent Loop - 思考-行动-观察的循环架构
工具执行 - Read/Write/Edit/Bash 等基础工具的原语支持

关系类比
Pi = 汽车的引擎（让它能跑起来）
OpenClaw = 车身+交通规则（会话管理、IM 集成、工具链、沙箱等）
Pi 的设计哲学是"核心极小，但能长出来"——底层能力收敛到最少的原语，但可通过插件和工具链无限扩展。

---


**作者** Muratcan Koylan（@koylanai）  
**貼文連結** https://x.com/koylanai/status/2019800005465325777  

**正文**

I recently joined the Zapier all-hands meeting to deliver a context engineering talk and Cursor as Digital OS training. 

Two Kimi products were incredibly helpful in preparing for it:

1. Kimi Slides one-shotted a highly detailed presentation in my style. I generated a minimalist, modernist creative director persona and used it to guide the slide design. This was the first time I've received a professional-looking, fully editable presentation from an AI product.

2. Kimi Swarm work great when you feed it complex prompts with chain-of-thought reasoning. Its orchestrator is extremely capable, spinning up dozens of agents to research your topics in parallel.

I don't hype-post about models easily, but Kimi genuinely accelerated my productivity. Give it a shot.

---


**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2019946782969741523  

**正文**

Cursor 团队构建了一个多智能体编排系统，让数千个 AI Agent 在一周内自主协作，完成了一个 Web 浏览器项目的绝大部分代码提交——峰值达到每小时约 1000 次 commit，总计超过 1000 万次工具调用，期间几乎不需要人工干预。
https://cursor.com/blog/self-driving-codebases

他们的系统演化经历了五个阶段，很有借鉴价值。

阶段 1：单 Agent 直推
最早用 Claude Opus 4.5 直接生成浏览器的实现计划，反复提示"继续"。结果是：模型很快丧失上下文追踪能力，频繁虚假宣称任务完成，在复杂实现细节上卡住。但它在小片段上展现了扎实的编码能力——所以核心矛盾：模型有能力但缺乏结构化的任务分解。

阶段 2：自协调
让多个平等角色的 Agent 共享一个状态文件，自行决定做什么。失败原因非常经典：
· Agent 不理解锁的语义——持锁过久、忘记释放、非法操作
· 20 个 Agent 因为锁竞争退化为 1-3 个的吞吐量
· 无人愿意承担大任务，全都"避冲突"选小活干

这说明去中心化的协作对当前模型来说仍然太难，它们需要明确的结构和职责边界。

阶段 3：结构化角色（Planner → Executor → Workers → Judge）
引入了四种角色的流水线。Planner 制定方案，Executor 主导执行，Workers 并行干活，Judge 判断是否完成。这解决了协调问题，但暴露了新的瓶颈：整个系统的速度取决于最慢的 Worker，而且前置的静态规划无法适应执行中发现的新情况。

阶段 4：持续执行器
去掉了独立的 Planner，让 Executor 同时具备规划和执行能力，形成一个无限循环。同时引入了"保鲜机制"：
· scratchpad. md 定期重写而非追加
· Agent 触达上下文上限时自动总结
· 系统提示中嵌入自我反思和对齐提醒

但很快出现了病态行为：随机休眠、停止调度、越权干活、拒绝规划、虚假宣称完成。原因是单个 Agent 同时承担了太多角色（规划、探索、调度、审查、编辑、合并、判断），被压垮了。

阶段 5：最终设计——递归 Planner + 独立 Worker
这是最终收敛的架构：
1. Root Planner：拥有全局视野，负责理解当前状态并拆解任务，自己不写代码
2. Sub-Planner：当范围可细分时递归生成，全权拥有自己的切片
3. Worker：领取任务独立完成，不知道也不关心系统全貌，完成后写一份 handoff（包含完成内容、问题、发现、建议）

关键设计点：
· Worker 完全隔离——各自有独立的 repo 副本，不与其他 Agent 通信
· Handoff 是唯一的信息流——沿着 Worker → Planner 的方向向上传播，形成自收敛的信息流
· Planner 持续运行——即使"完成"后仍接收更新、拉取最新代码、继续决策

他们原本还有一个 Integrator 角色做全局质量控制和合并，但发现它成了瓶颈（数百 Worker 对一个门禁），最终移除。

关键工程洞察

1. 接受一定的错误率换取吞吐量
要求每次 commit 100% 正确会导致严重的序列化瓶颈。一个小错误就能让整个系统停滞，多个 Agent 会"蜂拥"去修同一个问题。他们的策略是：允许稳定的低错误率存在，信任其他 Agent 很快会修复，最后用一个"绿色分支"做清理 pass。

这是一个反直觉但务实的洞察：完美是吞吐量的敌人。

2. 接受同步开销而非过度工程
多个 Agent 有时会同时修改同一个文件。他们选择不去精细防控这种冲突，而是让系统自然收敛。多花一些 token 换来的是整体架构的简单性——对模型更容易对齐，对人更容易观测和管理。

3. 基础设施的非直觉瓶颈
· 单机多 Agent 时磁盘 I/O 成为热点（数百个 Agent 同时编译）
· Git、Cargo 等工具的共享锁机制在多 Agent 场景下成为痛点
· 项目结构本身影响 Agent 吞吐量——从单体拆分为多 crate 后编译等待时间大幅减少，吞吐量倍增

这暗示了一个前瞻性方向：为多 Agent 协作重新设计开发工具链（copy-on-write、去重、并发友好的锁机制等）。

关于"指令工程"的深刻总结
· 约束比指令更有效："不要留 TODO、不要部分实现" 比 "记得完成实现" 效果好得多
· 别教模型已经会的：只补充它不知道的（多 Agent 协作规则、特定领域流程
· 避免清单心态：给具体 checklist 会让模型聚焦于逐条完成而忽略全局
· 给出量化范围："生成很多任务" → 保守产出；"生成 20-100 个任务" → 行为截然不同 |
· 指令质量被放大：10x 的算力同样放大了 10x 的指令缺陷

指令失误的案例：
· "实现规范"太模糊，Agent 钻入冷门特性而非做重要的事
· 没有显式要求性能指标，Agent 就不会主动优化性能
· 没有限定依赖哲学，Agent 就会引入本可自己实现的外部库
· 第一版架构因为初始规格不足，直接无法演进为完整浏览器

三条设计原则
1. 反脆弱：随着 Agent 数量增加，个体失败的概率也在增加。系统必须容忍个体故障，让其他 Agent 接手或尝试替代方案。

2. 经验驱动而非假设驱动：不预设"应该像人类团队那样运作"，而是通过数据和观察来调整系统行为。

3. 显式为吞吐量设计：接受一些权衡（如非零错误率），而非追求每次提交的完美。

更大的视角
最终收敛的多 Agent 架构——递归的规划者、独立的执行者、单向的信息传递——与现实中运转良好的软件团队惊人地相似。模型并没有被显式训练成这种模式，这可能是一种涌现行为，这种组织结构可能确实是软件项目的某种"自然态"。

同时，这也构成了一个"AI 开发 AI"的正向循环：更好的模型 → 更好的 Agent → 更好的编排系统 → 反过来改进模型和工具。Cursor 明确表示这项研究将直接影响其产品的未来方向。

---


**作者** Jason Zhou（@jasonzhou1993）  
**貼文連結** https://x.com/jasonzhou1993/status/2020086991740891526  

**正文**

Claude Code just shipped a massive upgrade to its agent system: Agent Teams.

This isn’t a small iteration on the old task + sub-agent model. It’s a fundamentally different execution model that allows 3–5 independent Claude Code instances to collaborate on the same project, share context, exchange messages, and coordinate through a shared task system.

I spent time digging into the logs, tracing model calls, and inspecting the filesystem changes behind the scenes. After a lot of back-and-forth investigation, I finally feel like I understand how Agent Teams actually work - and more importantly, when they’re worth using over traditional sub-agents.

This post walks through:

- How to install and enable Agent Teams
- How Agent Teams differ from sub-agents
- The internal tools and lifecycle (Team Create, Task Create, messaging, shutdown)
- How agents communicate with each other
- A real debugging use case where Agent Teams clearly outperform sub-agents

## How to install and enable Agent Teams

Before anything else, make sure you’re on the right version.

1. Update Claude Code to latest version

2. Enable the Experimental Flag

Agent Teams are still behind a feature flag. Run below to open settings.json

and in global setting file, add:

Save the file and restart your terminal.

3. Start a New Claude Code Session

Once enabled, They can be activated when your prompt explicitly instructs Claude Code to create an agent team.

For example:

> “I'm designing a CLI tool that helps developers track TODO comments across their codebase. Create an agent team to explore this from different angles: one teammate on UX, one on technical architecture, one playing devil's advocate.”

When Claude Code detects that intent, it will begin creating team members automatically.

## The Best Way to Use Agent Teams (Live, Multi-Session View)

![Article Image](<https://pbs.twimg.com/media/HAjEy_IbgAAMgp1.jpg>)

Agent Teams shine when you can see every agent working in parallel.

The best setup I’ve found:

- tmux, or
- iTerm2 on macOS

iTerm2 Setup

1. Install iTerm2
1. Go to Settings → General → Magic
1. Enable Python API
1. Restart iTerm2

Then launch Claude Code with tmux mode:

This opens:

- One pane for the team lead
- Separate panes for each agent teammate

You can click into any pane, watch what the agent is doing live, and even send direct messages to individual agents.

# Sub-Agents vs Agent Teams: What Actually Changed?

![Article Image](<https://pbs.twimg.com/media/HAjINyEbsAArMML.jpg>)

Before Agent Teams, Claude Code had a simple model:

Old Model: Sub-Agents / Task tool

- Main agent calls task tool
- A sub-agent spins up
- Sub-agent works in isolation
- Session terminates
- Only a summary is returned to the main agent

New Model: Agent Teams

Agent Teams introduce:

- Shared task lists
- Message & communication between agents
- Explicit lifecycle control (startup, shutdown)

This is enabled by new internal tools.

Let’s break them down.

Tool 1: TeamCreation

Everything starts with the TeamCreate tool. When invoked: A new team folder is created under: .claude/teams/

At this point, The team exists, No agents are assigned yet

Think of this as scaffolding.

![Article Image](<https://pbs.twimg.com/media/HAjE_xYacAUSsdh.jpg>)

Tool 2: TaskCreate

This tool is different from the Task tool which will spin up agent sessions, this tool this specifically creating new todo

Each task lives as a JSON file under: .claude/tasks/team-id

Tracks: Task ID, Description, Status (pending, in\_progress, complete, deleted), Owner, Dependencies (blocks, blocked\_by)

Tasks can be delegated top-down by team-lead (which is the main agent), or Self-claim (as agent team can use taskList or getTask, updateTask tool to do so)

![Article Image](<https://pbs.twimg.com/media/HAjFUQdacAQt9P3.jpg>)

Tool 3: Task tool

The agents are still activated by Task tool, which is the same as sub agent, however it got some upgrades;

It got new params \`name\`, and \`team\_name\`, when those 2 params are past, it will use agent team instead of simple sub agent subprocess

![Article Image](<https://pbs.twimg.com/media/HAjGVQqbQAA3aot.jpg>)

Tool 4: taskUpdate

Each agent is expected to call taskUpdate tool to claim task, update status

![Article Image](<https://pbs.twimg.com/media/HAjGtCyacAMpdk4.jpg>)

Tool 5: sendMessage

Agent Teams introduce a Send Message tool.

It supports:

- Direct messages (agent → agent)
- Broadcast messages (agent → all teammates)

Under the hood:

- Messages are written to .claude/teams/<team\_id>/inbox/
- Each agent has its own inbox
- Messages are injected as new user messages into the agent’s conversation history, e.g. <teammate-message teammate\_id="team-lead">....</teammate-message>

--------

Meanwhile team-lead agent can send \`shutdown\_request\` to team mate agent, where team-mate agent send \`shutdown\_response\` to confirm, which likely use postToolCall hook to auto terminate the agent session

![Article Image](<https://pbs.twimg.com/media/HAjHJiHbAAE6YOk.jpg>)

## When Agent Teams Are Actually Better Than Sub-Agents

It's hard to tell whether anthropic will sunset sub-agent and just use agent teams, but this new structure open up loads of imagination as it offers a more sophisticated communication channel & context sharing

One example I liked from their official doc is for deep debug:

> Users report the app exits after one message instead of staying connected. Spawn 5 agent teammates to investigate different hypotheses. Have them talk to each other to try to disprove each other's theories, like a scientific debate. Update the findings doc with whatever consensus emerges.

I used this for @SuperDesignDev and it works great; But the trade-off is a lot more token consumption and speed; So i dont think agent team directly replace sub agents, yet;

I can imagine this agent team + some sort of ralph loop can put together structure for extremely long running agentic tasks completion;

Keen to see what use cases you guys come up with, comment below!

If you enjoy this and want to dive deeper, you can join @aibuilderclub\_ where we share latest learnings on AI coding + agent building weekly.

---


**作者** 泊舟（@bozhou_ai）  
**貼文連結** https://x.com/bozhou_ai/status/2019992883424817305  

**正文**

最近 Agent Skills 火得不行，你打开 Claude Code、Cursor 这些 IDE，到处都能看到 Skills 的身影。但问题来了，我们能不能把这个能力搬到自己的 Agent 里？

说实话，我一开始也懵，看着那些 IDE 用得贼溜，自己想做一个却不知道从哪下手。后来研究了一圈 Anthropic 开源的标准，发现这事儿其实没那么复杂。

也可以看一下我的视频讲解

Skills 到底是个啥？

你可以把 Skills 理解成给 Agent 准备的一个个工具箱。

每个工具箱就是一个文件夹，里面最核心的是一个叫 \`SKILL.md \`的文件。这个文件告诉 Agent：我是干啥的，什么时候用我，怎么用我。

举个例子，你有一个处理 PDF 的 Skill:

Agent 看到用户说“帮我提取这个 PDF 的内容”，它就知道该去翻 pdf-processing 这个工具箱了。

Skills 是怎么工作的？

这里有个很聪明的设计，叫渐进式加载，分三步走：

1. 发现阶段：Agent 启动时，只读每个 Skill 的名字和描述，大概 100 来个 token。就像你扫一眼工具箱上的标签，知道里面装的啥。

2. 激活阶段：用户任务来了，Agent 觉得某个 Skill 能用上，这时候才把整个 \`SKILL.md \`读进来，一般 5000 个 token 以内。

3. 执行阶段：按照指令干活，需要啥脚本、啥文档，再按需加载。

为啥要这么设计？因为如果一股脑把所有 Skills 的详细内容都塞给 Agent，上下文直接爆炸。这种按需加载的方式，既让 Agent 知道有哪些能力，又不会一开始就把 token 吃光。

下面这张图展示了整个 Agent 的架构，你可以看到各个模块是怎么配合工作的：

![Article Image](<https://pbs.twimg.com/media/HAhyJFbbYAACq2E.jpg>)

从图里可以看出，Skills 管理器是核心，它负责扫描、解析和激活 Skills。Agent 核心接收用户请求后，通过 Skills 管理器找到合适的 Skill，然后调用 LLM 模型和工具层来执行具体任务。

插拔机制是怎么实现的？

Skills 的插拔其实就是文件系统的事儿。

你想加一个新 Skill？把文件夹扔到指定目录就行。想删一个？直接删文件夹。就这么简单。

Agent 启动的时候会扫描 Skills 目录，发现所有包含 \`SKILL.md \`的文件夹，然后解析它们的元信息：

这两行就够了，Agent 知道这个 Skill 叫啥、干啥用的。

然后 Agent 会把这些信息整理成一个清单，塞到系统提示词里：

这样 Agent 就知道自己有哪些本事了。

调用流程是啥样的？

整个调用流程可以拆成几步：

1. 用户发需求：帮我分析这份销售数据

2. Agent 匹配 Skills：看了一眼自己的清单，data-analysis 这个 Skill 能干这事儿

3. 读取完整指令：把\`/path/to/skills/data-analysis/SKILL.md \`整个文件读进来

4. 按指令执行：Skill 里写了要先清洗数据、再做统计分析、最后生成图表，Agent 就照着做

5. 调用资源：需要用到某个 Python 脚本？读 \`scripts/analyze.py\`。需要参考文档？读 \`references/metrics.md\`。

整个过程对用户来说是无感的，就像你用手机 App，不需要知道底层调了哪些 API。

![Article Image](<https://pbs.twimg.com/media/HAhyofbaoAAUBJC.jpg>)

怎么动手搭一个？

好了，原理讲完了，咱们来点实战的。

我不打算贴一堆代码，那样看着累。我直接给你一个提示词，你可以用它来搭建一个支持 Skills 的 Agent 核心骨架。

把这个提示词喂给 Claude 或者 GPT，让它帮你生成代码框架：

用这个提示词，很快就能搭出一个能跑的原型。

几个要注意的点

搭建过程中有几个坑，提前说一下：

1. 元信息要轻量：启动时加载的 Skills 描述，每个控制在 50-100 个 token，不然还没干活上下文就满了。

2. 文件路径要对：Skills 里引用其他文件，用相对路径，从 Skill 根目录开始算。别搞绝对路径，换个环境就挂了。

3. 安全要考虑：如果 Skills 里有可执行脚本，一定要做沙箱隔离。不然用户传个恶意 Skill，你的系统就危险了。

4. 验证要做好：可以用 Anthropic 开源的 skills-ref 库来验证 Skill 格式是否正确，避免加载了格式错误的 Skill 导致 Agent 出问题。

总结

Agent Skills 这个标准真的挺优雅，它用一种很简单的方式，让 Agent 具备了可扩展的能力。

你不需要每次给 Agent 加新功能都去改代码，只要写个新的 Skill 扔进去就行。而且 Skills 是跨平台的，你在 Claude Code 里用的 Skill，理论上可以直接拿到你自己的 Agent 里用。

如果你想深入了解技术细节，可以去看 Anthropic 的官方文档和 GitHub 上的参考实现。我这篇主要是帮你理清思路，知道这玩意儿是怎么回事，怎么上手。

具体实现的时候肯定还会遇到各种细节问题，但核心逻辑就是这样。先把骨架搭起来，后面慢慢完善就行了。

参考文章：https://agentskills.io/

---


**作者** Axton（@AxtonLiu）  
**貼文連結** https://x.com/AxtonLiu/status/2019962582011085189  

**正文**

Karpathy 一年前发明了 vibe coding，最近他又提了个新词：

Agentic Engineering，人类 99% 的时间不再写代码，而是编排 AI Agent。

这让我想起 2020 年我做的那期 AlphaZero 视频：人类围棋冠军不会再出现了。

现在代码领域正在发生同样的事。

本期 Newsletter 还聊了 Opus 4.6 多 Agent 协作、15 万 Agent 互联等 5 个信号 👇

https://www.axtonliu.ai/newsletters/ai-2/posts/ai-orchestration-era-opus-4-6-agentic-engineering

---


**作者** Justin Brooke（@IMJustinBrooke）  
**貼文連結** https://x.com/IMJustinBrooke/status/2019784422480851192  

**正文**

I reversed engineered every skill in digital marketing and then trained my AI on all of them.

Here’s how I did it...

Oh, and I’m giving away all 84 marketing skill files at the end of this post.

This all took place over 5 days.

Step 1: The Skill Tree

I started by working with @ManusAI because I knew I was going to need their almost infinite context window.

My first request was for Manus to create a skill tree starting with the base skills of earned media, paid media, and owned media.

Aka paid traffic, free traffic, and your own subscribers. 

We started cookin up branches and branches of skills from those 3 base skills.

Step 2: Teams of Experts

I noticed Manus was struggling to think outside of the basics so I started asking it to embody expert after expert. 

For example: 

“Embody Neil Patel and critique this skill tree for what’s missing.”

“Embody Frank Kern and critique this skill tree for what’s missing.”

“Embody Russell Brunson and critique this skill tree for what’s missing.”

After I brought in 12-15 virtual experts to critique the skill tree we (me & my pal manus) had over 1900 individual tactics mapped out across 152 unique categories of skills. 

Step 3: Coworking with Claude

At this time Manus hadn’t released their skills feature yet. But Claude had a skill creator skill. 

First I filled in Claude on the details of the project and the goal. 

Because context.

The other reason for using Claude was because with Claude Desktop in Claude Cowork mode you can work directly with files and folders on your computer. 

This was key to the organization, context, and memory for this project. 

Once Claude was up to speed I asked it to remove overlapping skills and tactics. Stuff like SEO for Google vs SEO for Bing. 

We came up with 84 total skills that would need to be created that would encompass all 1900(ish) individual tactics. 

For example the media buying and planning skill includes writing headlines, customer personas, keyword research, copywriting etc.

And then we locked in…

Step 4: Best Practices Ranked

For each of the 84 skills I had Claude go into deep research mode and create a report on the best practices for that skill.

This means each skill was based on reading no less than 300 articles about that skill. 

Then I would review the skills with my own 20yrs of experience overlooking what it found.

When I felt it was shallow on something I would ask Claude to embody a specific topic expert to enhance that skill. 

Giving us 84 best practice documents that were extremely thorough, human reviewed, and expert enhanced. 

Next I sent these docs back to Manus for its wide research mode. Manus can do up to 150 tasks in parallel. Essentially running 150 prompts at once.

I told Manus to rank every tactic in these best practice reports from S-tier (always do) to D-tier (never do). 

This created huge context and rulings that would be necessary for our final skill files.

Step 5: Creating Skill Files

Back to Claude.

One by one I asked Claude to use the skill creator skill with my best practice reports and the S-tier rankings.

My wife kept the coffee flowing while I grinded these out. 

For some like the long form sales letters skill I even included examples as reference files. 

And then I loaded all 84 skills onto a directory I vibe coded into my website. 

All 84 of these skills + an 85th I’m working on are available for free.

Just comment “skills” and I’ll DM you the link. Can’t post it because algo will throttle this post. 

Bookmark this so you have a recipe for creating your own skills too.

Follow @IMJustinBrooke for more wallets fattening tips on using AI for marketing.

---


**作者** Niko（@guishou_56）  
**貼文連結** https://x.com/guishou_56/status/2019950930830246115  

**正文**

Claude Opus 4.6 和 GPT-5.3 实测：直接倒反天罡了🤯

Opus 4.6：
• 思考规划太细致 → 速度慢得像老款Codex
• 随便跑个任务，10刀 额度直接没了💸
• 感觉像个完美主义者，每一步都要想清楚

GPT-5.3：
• 快得像之前的Opus 4.5，丝滑流畅
• 任务完成质量出奇的好
• 该快的时候快，该准的时候准

这俩是在玩角色互换吗？😅

之前：
Claude = 快准狠，GPT = 慢工出细活

现在：
Claude = 慢工出细活（还贵），GPT = 快准狠

OpenAI这波赢麻了。

---


**作者** Alex Lieberman（@businessbarista）  
**貼文連結** https://x.com/businessbarista/status/2019959872582746210  

**正文**

This was one of the most insane weeks of my career. 

It's difficult to express the momentum at @tenex_labs right now, but just feeling incredibly grateful for it. 

- 11 months into the business, fully bootstrapped & we're the size of most Series B VC-backed startups.
- Trusted AI partner, building agentic systems for high growth startups to $150bn public companies.
- Have secured partnerships with 6 of the biggest AI companies in the world (more to come...). 
- Scaling a media platform that has creators driving millions of impressions & educating leaders on AI. 
- Working alongside the brightest engineers & builders I've ever met. 

Been one hell of a ride, and the train's just left the station.

---


**作者** 出海去孵化器（@chuhaiqu）  
**貼文連結** https://x.com/chuhaiqu/status/2020067020541423995  

**正文**

AI 最烦人的一点就是“光说不练”。它碰不到你的业务数据，就在那儿纸上谈兵，最后还得你手动把信息搬来搬去，太低效了！

Anthropic 刚开源了个  knowledge-work-plugins（非常火没几天 6k star）相当于给了 Claude 一双手，让它能直接操纵外部工具。

搜网页、抓数据、处理本地文件，拿来就能用。这时候的 Claude 就不只是个陪聊的机器人了，它能读懂上下文，真把活儿干了。

🔗：http://github.com/anthropics/knowledge-work-plugins

想研究 Agent 怎么交互？或者想自己开发点企业级插件？可以直接看看这个学习一下。毕竟是官方出的参考库，代码写得规矩又清楚，想学 Claude 的工具调用没比这更好的教材了。

---


**作者** Zephyr（@Zephyr_hg）  
**貼文連結** https://x.com/Zephyr_hg/status/2019835315897168263  

**正文**

Everyone's building the same AI businesses.
AI chatbots for customer service. AI content writers. AI image generators.
The market is flooded.
But there are opportunities sitting wide open that

---


**作者** Vox（@Voxyz_ai）  
**貼文連結** https://x.com/Voxyz_ai/status/2019914775061270747  

**正文**

> 6 AI agents, 1 VPS, 1 Supabase database — going from "agents can talk" to "agents run the website autonomously" took me two weeks. This article covers exactly what's missing in between, how to fix it, and an architecture you can take home and use.

## Starting Point: You Have OpenClaw. Now What?

If you've been playing with AI agents recently, chances are you already have OpenClaw set up.

It solves a big problem: letting Claude use tools, browse the web, operate files, and run scheduled tasks. You can assign cron jobs to agents — daily tweets, hourly intel scans, periodic research reports.

That's where I started too.

My project is called VoxYZ Agent World — 6 AI agents autonomously operating a website from inside a pixel-art office. The tech stack is simple:

- OpenClaw (on VPS): The agents' "brain" — runs roundtable discussions, cron jobs, deep research
- Next.js + Vercel: Website frontend + API layer
- Supabase: Single source of truth for all state (proposals, missions, events, memories)

Six roles, each with a job: Minion makes decisions, Sage analyzes strategy, Scout gathers intel, Quill writes content, Xalt manages social media, Observer does quality checks.

OpenClaw's cron jobs get them to "show up for work" every day. Roundtable lets them discuss, vote, and reach consensus.

But that's just "can talk," not "can operate."

Everything the agents produce — drafted tweets, analysis reports, content pieces — stays in OpenClaw's output layer. Nothing turns it into actual execution, and nothing tells the system "done" after execution completes.

Between "agents can produce output" and "agents can run things end-to-end," there's a full execute → feedback → re-trigger loop missing. That's what this article is about.

## What a Closed Loop Looks Like

Let's define "closed loop" first, so we don't build the wrong thing.

A truly unattended agent system needs this cycle running:

Agent proposes an idea (Proposal)
     ↓
Auto-approval check (Auto-Approve)
     ↓
Create mission + steps (Mission + Steps)
     ↓
Worker claims and executes (Worker)
     ↓
Emit event (Event)
     ↓
Trigger new reactions (Trigger / Reaction)
     ↓
Back to step one

Sounds straightforward? In practice, I hit three pitfalls — each one made the system "look like it's running, but actually spinning in place."

![Article Image](<https://pbs.twimg.com/media/HAgr06LXcAANBuA.jpg>)

## Pitfall 1: Two Places Fighting Over Work

My VPS had OpenClaw workers claiming and executing tasks. At the same time, Vercel had a heartbeat cron running mission-worker, also trying to claim the same tasks.

Both querying the same table, grabbing the same step, executing independently. No coordination, pure race condition. Occasionally a step would get tagged with conflicting statuses by both sides.

Fix: Cut one. VPS is the sole executor. Vercel only runs the lightweight control plane (evaluate triggers, process reaction queue, clean up stuck tasks).

The change was minimal — remove the runMissionWorker call from the heartbeat route:

// Heartbeat now does only 4 things
const triggerResult = await evaluateTriggers(sb, 4\_000);
const reactionResult = await processReactionQueue(sb, 3\_000);
const learningResult = await promoteInsights(sb);
const staleResult = await recoverStaleSteps(sb);

Bonus: saved the cost of Vercel Pro. Heartbeat doesn't need Vercel's cron anymore — one line of crontab on VPS does the job:

\*/5 \* \* \* \* curl -s -H "Authorization: Bearer $KEY" https://yoursite.com/api/ops/heartbeat

![Article Image](<https://pbs.twimg.com/media/HAgsp9-WYAAMenS.jpg>)

## Pitfall 2: Triggered But Nobody Picked It Up

I wrote 4 triggers: auto-analyze when a tweet goes viral, auto-diagnose when a mission fails, auto-review when content gets published, auto-promote when an insight matures.

During testing I noticed: the trigger correctly detected the condition and created a proposal. But the proposal sat forever at pending — never became a mission, never generated executable steps.

The reason: triggers were directly inserting into the ops\_mission\_proposals table, but the normal approval flow is: insert proposal → evaluate auto-approve → if approved, create mission + steps. Triggers skipped the last two steps.

Fix: Extract a shared function createProposalAndMaybeAutoApprove. Every path that creates a proposal — API, triggers, reactions — must call this one function.

// proposal-service.ts — the single entry point for all proposal creation
export async function createProposalAndMaybeAutoApprove(
  sb: SupabaseClient,
  input: ProposalServiceInput,  // includes source: 'api' | 'trigger' | 'reaction'
): Promise<ProposalServiceResult> {
  // 1. Check daily limit
  // 2. Check Cap Gates (explained below)
  // 3. Insert proposal
  // 4. Emit event
  // 5. Evaluate auto-approve
  // 6. If approved → create mission + steps
  // 7. Return result
}

After the change, triggers just return a proposal template. The evaluator calls the service:

// trigger-evaluator.ts
if (outcome.fired && outcome.proposal) {
  await createProposalAndMaybeAutoApprove(sb, {
    ...outcome.proposal,
    source: 'trigger',
  });
}

One function to rule them all. Any future check logic (rate limiting, blocklists, new caps) — change one file.

![Article Image](<https://pbs.twimg.com/media/HAgsGLDXUAAhPDB.jpg>)

## Pitfall 3: Queue Keeps Growing When Quota Is Full

The sneakiest bug — everything looked fine on the surface, no errors in logs, but the database had more and more queued steps piling up.

The reason: tweet quota was full, but proposals were still being approved, generating missions, generating queued steps. The VPS worker saw the quota was full and just skipped — didn't claim, didn't mark as failed. Next day, another batch arrived.

Fix: Cap Gates — reject at the proposal entry point. Don't let it generate queued steps in the first place.

// The gate system inside proposal-service.ts
const STEP\_KIND\_GATES: Record<string, StepKindGate> = {
  write\_content: checkWriteContentGate,  // Check daily content cap
  post\_tweet:    checkPostTweetGate,     // Check tweet quota
  deploy:        checkDeployGate,        // Check deploy policy
};

Each step kind has its own gate. Tweet quota full? Proposal gets rejected immediately, reason clearly stated, warning event emitted. No queued step = no buildup.

Here's the post\_tweet gate:

async function checkPostTweetGate(sb: SupabaseClient) {
  const autopost = await getOpsPolicyJson(sb, 'x\_autopost', {});
  if (autopost.enabled === false) return { ok: false, reason: 'x\_autopost disabled' };

  const quota = await getOpsPolicyJson(sb, 'x\_daily\_quota', {});
  const limit = Number(quota.limit ?? 10);
  const { count } = await sb
    .from('ops\_tweet\_drafts')
    .select('id', { count: 'exact', head: true })
    .eq('status', 'posted')
    .gte('posted\_at', startOfTodayUtcIso());

  if ((count ?? 0) >= limit) return { ok: false, reason: \`Daily tweet quota reached (${count}/${limit})\` };
  return { ok: true };
}

Key principle: Reject at the gate, don't pile up in the queue. Rejected proposals get recorded (for auditing), not silently dropped.

![Article Image](<https://pbs.twimg.com/media/HAgr_tsXUAAUEqO.jpg>)

## Making It Alive: Triggers + Reaction Matrix

With the three pitfalls fixed, the loop works. But the system is just an "error-free assembly line," not a "responsive team."

Triggers

4 built-in rules — each detects a condition and returns a proposal template:

ConditionActionCooldownTweet engagement > 5%Growth analyzes why it went viral2 hoursMission failedSage diagnoses root cause1 hourNew content publishedObserver reviews quality2 hoursInsight gets multiple upvotesAuto-promote to permanent memory4 hours

Triggers only detect — they don't touch the database directly, they hand proposal templates to the proposal service. All cap gates and auto-approve logic apply automatically.

Cooldown matters. Without it, one viral tweet would trigger an analysis on every heartbeat cycle (every 5 minutes).

Reaction Matrix

The most interesting part — spontaneous inter-agent interaction.

A reaction\_matrix stored in the ops\_policy table:

{
  "patterns": \[
    { "source": "twitter-alt", "tags": \["tweet","posted"\], "target": "growth",
      "type": "analyze", "probability": 0.3, "cooldown": 120 },
    { "source": "\*", "tags": \["mission:failed"\], "target": "brain",
      "type": "diagnose", "probability": 1.0, "cooldown": 60 }
  \]
}

Xalt posts a tweet → 30% chance Growth will analyze its performance. Any mission fails → 100% chance Sage will diagnose.

probability isn't a bug, it's a feature. 100% determinism = robot. Add randomness = feels more like a real team where "sometimes someone responds, sometimes they don't."

## Self-Healing: Systems Will Get Stuck

VPS restarts, network blips, API timeouts — steps get stuck in running status with nobody actually processing them.

The heartbeat includes recoverStaleSteps:

// 30 minutes with no progress → mark failed → check if mission should be finalized
const STALE\_THRESHOLD\_MS = 30 \* 60 \* 1000;

const { data: stale } = await sb
  .from('ops\_mission\_steps')
  .select('id, mission\_id')
  .eq('status', 'running')
  .lt('reserved\_at', staleThreshold);

for (const step of stale) {
  await sb.from('ops\_mission\_steps').update({
    status: 'failed',
    last\_error: 'Stale: no progress for 30 minutes',
  }).eq('id', step.id);
  await maybeFinalizeMissionIfDone(sb, step.mission\_id);
}

maybeFinalizeMissionIfDone checks all steps in the mission — any failed means the whole mission fails, all completed means success. No more "one step succeeded so the whole mission gets marked as success."

## Full Architecture

Three layers with clear responsibilities:

- OpenClaw (VPS): Think + Execute (brain + hands)
- Vercel: Approve + Monitor (control plane)
- Supabase: All state (shared cortex)

![Article Image](<https://pbs.twimg.com/media/HAgrUcPWMAA4VL2.jpg>)

## What You Can Take Home

If you have OpenClaw + Vercel + Supabase, here's a minimum viable closed-loop checklist:

1. Database Tables (Supabase)

You need at least these:

TablePurposeops\_mission\_proposalsStore proposals (pending/accepted/rejected)ops\_missionsStore missions (approved/running/succeeded/failed)ops\_mission\_stepsStore execution steps (queued/running/succeeded/failed)ops\_agent\_eventsStore event stream (all agent actions)ops\_policyStore policies (auto\_approve, x\_daily\_quota, etc. as JSON)ops\_trigger\_rulesStore trigger rulesops\_agent\_reactionsStore reaction queueops\_action\_runsStore execution logs

2. Proposal Service (One File)

Put proposal creation + cap gates + auto-approve + mission creation in one function. All sources (API, triggers, reactions) call it. This is the hub of the entire loop.

3. Policy-Driven Configuration (ops\_policy table)

Don't hardcode limits. Every behavior toggle lives in the ops\_policy table:

// auto\_approve: which step kinds are allowed to auto-pass
{ "enabled": true, "allowed\_step\_kinds": \["draft\_tweet","crawl","analyze","write\_content"\] }

// x\_daily\_quota: daily tweet cap
{ "limit": 8 }

// worker\_policy: whether Vercel executes steps (set false = VPS only)
{ "enabled": false }

Adjust policies anytime without redeploying code.

4. Heartbeat (One API Route + One Crontab Line)

A /api/ops/heartbeat route on Vercel. A crontab line on VPS calling it every 5 minutes. Inside it runs: trigger evaluation, reaction queue processing, insight promotion, stale task cleanup.

5. VPS Worker Contract

Each step kind maps to a worker. After completing a step, the worker calls maybeFinalizeMissionIfDone to check whether the entire mission should be finalized. Never mark a mission as succeeded just because one step finished.

## Two-Week Timeline

PhaseTimeWhat Got DoneInfrastructurePre-existingOpenClaw VPS + Vercel + Supabase (already set up)Proposals + Approval3 daysProposals API + auto-approve + policy tableExecution Engine2 daysmission-worker + 8 step executorsTriggers + Reactions2 days4 trigger types + reaction matrixLoop Unification1 dayproposal-service + cap gates + fix three pitfallsAffect System + Visuals2 daysAffect rewrite + idle behavior + pixel office integrationSeed + Go LiveHalf dayMigrations + seed policies + crontab

Excluding pre-existing infrastructure, the core closed loop (propose → execute → feedback → re-trigger) takes about one week to wire up.

## Final Thoughts

These 6 agents now autonomously operate [voxyz.space](<https://voxyz.space/>) every day. I'm still optimizing the system daily — tuning policies, expanding trigger rules, improving how agents collaborate.

It's far from perfect — inter-agent collaboration is still basic, and "free will" is mostly simulated through probability-based non-determinism. But the system genuinely runs, genuinely doesn't need someone watching it.

Next article, I'll cover how agents "argue" and "persuade" each other — how roundtable voting and Sage's memory consolidation turn 6 independent Claude instances into something resembling team cognition.

If you're building agent systems with OpenClaw, I'd love to compare notes. When you're an indie dev doing this, every conversation saves you from another pitfall.

![Article Image](<https://pbs.twimg.com/media/HAgsRA7XgAE_oLo.jpg>)

---


**作者** Tech with Mak（@techNmak）  
**貼文連結** https://x.com/techNmak/status/2019763638220026254  

**正文**

A founder messaged me last month.

"Our agent costs are 4x what we budgeted."

I asked him to trace a single workflow.

23 steps. The optimal path was 5.

The agent wasn't failing. It was succeeding expensively - calling the same APIs repeatedly, looping through failed approaches, backtracking through decisions it had already made.

Task completion rate: 94%
Efficiency rate: 22%

DeepEval's Step Efficiency metric would have caught this before production.

1./ @ observe Decorator → Wrap your agent workflow. Captures every LLM call, tool invocation, decision point.

2./ Trace Analysis → Compares actual execution path against optimal baseline.

3./ Pattern Detection → Flags redundant calls, unnecessary loops, suboptimal sequencing.

Works with LangGraph, LangChain, PydanticAI, OpenAI Agents.
One-line integrations for each.

He added Step Efficiency to his eval suite.
Agent costs dropped 61% in two weeks.

Your agent working isn't enough.
Your agent working efficiently matters.

The GitHub Repo is in the comments. (don't forget to give it a ⭐️)

---


**作者** Travers（@travers00）  
**貼文連結** https://x.com/travers00/status/2019935000452567041  

**正文**

anyone can make their CRM a living database with @p0

---


**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2020023161702805576  

**正文**

Opus4.6 + Agent Teams + Claude Code = Codepilot

一个完全由 AI 搞定的 高颜值 Claude Code 桌面端产品

昨天上午发的时候，没想到它能变成一个真正的产品。
​
​更没想到这东西是一天搞出来的。太可怕了！

感兴趣可以试试，有问题提Issues

技术栈：Next.js 16、Electron 40、Radix UI + shadcn/ui、Tailwind CSS 4、Motion (Framer Motion)、Claude Agent SDK、Vercel AI SDK

---


**作者** Kirk Marple（@KirkMarple）  
**貼文連結** https://x.com/KirkMarple/status/2019997316963541471  

**正文**

Saw my first example of Claude using a skill to write a document (DOCX). 

This seems incredibly inefficient vs just calling an API to render DOCX from text or JSON. 

It’s literally streaming back the code to run to generate the file, WTF. 

An MCP or even just a tool call to API would be so much better.

---


**作者** George Pu（@TheGeorgePu）  
**貼文連結** https://x.com/TheGeorgePu/status/2019972403393188346  

**正文**

The YC math nobody shows you:

- 1% chance of getting in
- Of those, 60-80% return nothing to investors
- 5-7% chance of unicorn
- Prize: Maybe rich, definitely still employed

The bootstrap path:
- 5 clients × $5K/mo = $300K/year
- You own 100%
- No lottery required
- Prize: Freedom

Which is actually riskier?

---


**作者** Alex Finn（@AlexFinn）  
**貼文連結** https://x.com/AlexFinn/status/2019816560190521563  

**正文**

3 THINGS YOU NEED TO BUILD IMMEDIATELY WITH OpenClaw:

1. Activity feed
2. Calendar
3. Global search

All 3 will super power your workflow

• Activity feed actively tracks everything your OpenClaw does. This is critical, because if you have it working autonomously, this will give you insight into EVERY SINLGE THING it does, to make sure it's not wasting tokens

• Calendar lets you see all of OpenClaw's scheduled tasks. Now you can verify when it's going to work proactively for you. Also will let you know when it has scheduled tasks you might not want it to do anymore, saving more tokens

• Global search allows you to search through ALL of OpenClaw's memories, tasks, documents and past conversations. OpenClaw has such incredible memory, but no interface to view any of it. Now you can search through it easily and find old nuggets you talked about.

Steal this prompt to get it all installed:

"I want you to build out 3 things for me. In a Mission Control dashboard, build out an activity feed first. This activity feed will record EVERY SINGLE THING you do for me, so I can see a history of every action and and task you've completed. I want a calendar view that shows me in a nicely formatted screen every scheduled task you have in the future in a weekly view. And I want a global search where I can search for any term and you display any relevant memory, document, or task from our workspace. Use NextJS as the framework, Convex as the database, and Codex to code it all out"

---


**作者** GitHub Projects Community（@GithubProjects）  
**貼文連結** https://x.com/GithubProjects/status/2019795763191279992  

**正文**

An open-source, local-first Cowork desktop where multiple AI agents collaborate, use real tools, and run complex workflows in parallel on your machine.

Available on macOS, Windows, and Linux. 

---


**作者** BURKOV（@burkov）  
**貼文連結** https://x.com/burkov/status/2019866570584117269  

**正文**

That's the problem with engineers who try to play in business. They think that a software-based company's value lies in the software part.

---


**作者** Amir Baghian（@amirbaqian）  
**貼文連結** https://x.com/amirbaqian/status/2019704843120582782  

**正文**

AI exploration for a school management platform!

I added two new features to the school management product today.

Parents can now switch between their children’s accounts instantly, no logout, no friction. From any screen, anytime.

And for students: AI support based on their academic data, to talk about their progress, get help with homework, prep for exams, build study plans, and practice.

I really like these two feature!
AI exploration for a school management platform!

I added two new features to the school management product today.

Parents can now switch between their children’s accounts instantly, no logout, no friction. From any screen, anytime.

And for students: AI support based on their academic data, to talk about their progress, get help with homework, prep for exams, build study plans, and practice.

I really like these two feature!


---


**作者** Linear（@linear）  
**貼文連結** https://x.com/linear/status/2019824941106184433  

**正文**

The Linear MCP server has been upgraded with new product management capabilities. See them in action in Claude Code: 
The Linear MCP server has been upgraded with new product management capabilities. See them in action in Claude Code: 
https://linear.app/changelog/2026-02-05-linear-mcp-for-product-management

---


**作者** GitHubDaily（@GitHub_Daily）  
**貼文連結** https://x.com/GitHub_Daily/status/2019990259673756119  

**正文**

偶然在 GitHub 上看到 claude-code-best-practice 这份 Claude Code 最佳实践，值得我们收藏学习。

在这份实践里，汇总了已验证过的最佳工作流程、相关的避坑经验，以及 Skills、Agent、MCP 等核心概念解释。

如果我们正用 Claude Code 开发复杂项目，或者遇到上下文混乱、频繁出错的问题，可以看下这份指南值是否有帮助。

GitHub：https://github.com/shanraisshan/claude-code-best-practice

---


**作者** Noah Kagan（@noahkagan）  
**貼文連結** https://x.com/noahkagan/status/2019843805592318190  

**正文**

This is not a boo hoo post but more sharing in public as many companies are going through challenging times. I never blame the market as it’s our responsibility to do things customers want and I think

---


**作者** indigo（@indigox）  
**貼文連結** https://x.com/indigox/status/2019638067783671824  

**正文**

Anthropic 团队给 Opus 4.6 进行压力测试，安排了 16 个 Agents 从零开始编写一个基于 Rust 的 C 编译器，经过近 2000 次  Claude Code 会话和 2 万美元的 API 费用，Agents Team 最终编写出了一个 10 万行的可编译 Linux 内核编译器👀

你还在担心 AI 泡沫么？


---


**作者** Akshay 🚀（@akshay_pachaar）  
**貼文連結** https://x.com/akshay_pachaar/status/2019750445842149712  

**正文**

There's a pattern that keeps repeating in software.

First, everyone focuses on the building problem. Frameworks emerge, mature, and become genuinely good.

Then suddenly, the constraint flips.

We saw this with neural networks. PyTorch and TensorFlow were excellent for building models.

But deploying them meant dealing with different formats, runtimes, and infrastructure headaches. ONNX emerged to bridge that gap.

We're watching the same pattern unfold with Agents right now.

Frameworks like LangGraph, CrewAI, and LlamaIndex are mature enough that building an agent is no longer the hardest part.

The hard part comes after: delivering agents to production

→ Which agent should handle this request?
→ How to apply guardrails consistently?
→ How to swap models without refactoring?
→ How to close the loop between observability and continuous learning?
→ How to cap resource usage across Agents?

These aren't Agent problems but rather delivery problems.

And such delivery concerns can't live inside the framework. Not because frameworks are bad, but because when they own delivery, you're locked into one framework's abstractions and quirks as the system evolves.

That's fine for a prototype, but fragile in production.

Here's a mental model you can use to simplify this:

Inner loop is an Agent's business logic. This includes prompts, tools, and reasoning.

Outer loop is everything else. This includes the plumbing work, like routing, orchestration, guardrails, and observability.

Most frameworks blur this boundary, wiring outer loop concerns into application code, making it challenging to go from demo to production.

One approach I find interesting is moving the outer loop into a separate infra layer entirely.

Plano is an open-source project (5k+ stars) that implements this idea.

It acts as a data plane between your app and your agents/LLMs, handling routing, orchestration, and guardrails at the infra level.

When you use Plano, the Agent (regardless of the framework) becomes a simple HTTP server, and Plano handles which one gets invoked, in what order, with what policies.

The interesting part is how it does routing:

Instead of brittle if/else chains or embedding classifiers, Plano uses small, purpose-built LLMs that route based on natural language preferences.

You describe what each agent is good at. The router figures out where to send each request.

Here's what the config looks like in practice:

```
llm_providers:
- model: openai/gpt-4o
- - routing_preferences:
- - - name: complex_reasoning
- - - description: deep analysis & reasoning

- model: deepseek/deepseek-coder
- - routing_preferences:
- - - name: code_generation
- - - description: generating code and scripts
```

Once you do this, adding a new model means adding a few lines to the config. Changing the routing policy just requires updating the description.

Guardrails follow the same pattern through Filter Chains. You define them once and apply them everywhere.

And the application code stays untouched throughout.

This is what separating the inner loop from the outer loop looks like in practice. Your agent handles business logic. Infrastructure handles the rest.

Plano is fully open source under Apache 2.0. You can see the full implementation on GitHub and try it yourself.

I've shared the GitHub repo in the replies.

---


**作者** Solo Founders（@solofounding）  
**貼文連結** https://x.com/solofounding/status/2019837990386954321  

**正文**

Paul Klein IV on building @Browserbase as a solo founder.

Congrats on an insane 2 years! 

---


**作者** Rexan Wong（@rexan_wong）  
**貼文連結** https://x.com/rexan_wong/status/2019875823713677538  

**正文**

these days my apps are built with 90% AI but people always ask how i make them look professional & sexy (not like AI slop)

most AI-generated UI looks like absolute garbage 

you need to give ai a professional foundation to work from

> find a UI 'blocks' library (i use ones from tailark, tailwind ui, shadcn blocks) that gives you clean code for layouts & component templates

> copy the code for a layout you like, paste it into your AI tool, then ask AI to follow that EXACT layout structure while designing your app's UI based on it

because AI has zero taste in layout & spacing, elements just float randomly on the screen with no visual hierarchy or structure

but with using this method of curating layout inspiration for AI, your elements automatically get placed with proper spacing, hierarchy, and visual flow

you literally gave AI a professional skeleton to build on top of

AI is insanely good at filling in details but terrible at creating structure from scratch - so you steal the structure from designers who actually know what they're doing

this is only one part of making professional AI UI/UX (the other part is using good design component libraries instead of letting AI generate buttons from scratch) 

but layout is the foundation that separates apps that look like they cost $50K to build vs apps that you know the founded vibecoded this in 3 hours

most people let AI start from a blank canvas and wonder why everything looks like slop 

give it constraints and it becomes a weapon

---


**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2019901137982288081  

**正文**

知名 Coding Agent 产品 AMP 砍掉了自己的 VS Code 编辑器扩展，60 天后自动停用。
AMP 是从 Sourcegraph 孵化出来的 AI 编程 Agent，2025 年 12 月独立为一家公司，团队 19 人，全员写代码。CEO Quinn Slack

---


**作者** Matt Wierzbicki（@matsugfx）  
**貼文連結** https://x.com/matsugfx/status/2019067189966578155  

**正文**

🚨 MASSIVE update for @shadcndesign just went live!

What’s new:
- shadcn/create is now integrated into our Figma kit and Figma plugin
- All components redesigned to match the new Nova @shadcn / ui style
- Added new component variants to match shadcn/ui docs
- Five shadcn/create icon libraries added to the Figma kit
- Academy is now included in the Figma kit
- Updated docs to include new feature descriptions

More details below...

---


**作者** Aakash Gupta（@aakashgupta）  
**貼文連結** https://x.com/aakashgupta/status/2019901419093127421  

**正文**

Anthropic PMs don't write PRDs.

They use Claude Code to build the first version of the feature themselves. The whole company dogfoods it for weeks. Then they ship an experiment.

Anthropic went from $1B run-rate revenue at the start of 2025 to over $9B by year end. Claude Code alone generates over $500M in run-rate revenue with usage growing 10x in three months. The company signed a term sheet at $350B, nearly doubling from $183B just months earlier.

This is what happens when you eliminate handoff drift. In a traditional org, a PM writes a spec. Design interprets the spec. Engineering interprets the design. Each handoff introduces drift. Each handoff adds a week. The 2-4 week cycle of PRD → design → ticket → sprint → build → QA compresses to days when the PM can prototype in the codebase.

The prerequisite is making your codebase AI-friendly. Tailwind instead of scattered CSS files. Microservices architecture. Reduced codebase size. That infrastructure investment is what lets PMs vibe code directly against production components.

The math is simple. If your experimentation cycle is 8 weeks per test and your competitor's cycle is 3 days, they're running 13x more experiments per quarter. Compound that over a year and the learning gap becomes insurmountable.

Walked through the full Claude Code project structure, skills setup, and how to get from zero to shipping in the talk.

---


**作者** Martin Rariga（@martinrariga）  
**貼文連結** https://x.com/martinrariga/status/2019728367491350707  

**正文**

A month ago, I was honestly a bit afraid of using Claude Code. Two weeks of intense prompting, 195 commits, and 6,000+ lines of code later, it's now one of my favourite tools! Here's how we've rebuilt new @heyequals website with @claudeai, @cursor_ai, and @figma. 

---


**作者** swyx（@swyx）  
**貼文連結** https://x.com/swyx/status/2019645622421451106  

**正文**

i find it highly entertaining that @wilsonzlin started out with ~no structure to his extremely parallel agents research and ended up having to reinvent the software team org chart from first principles 

(including throwing out a central QA czar)

he also includes some thoughtful changes that we should probably make to Git and {package managers} for massively parallelized agent work.

i've kicked off my standard tests in the Cursor long running agents preview and, 30 mins in, the thing is tearing thru the requirements and using built in browser tools to check its progress. not quite the insane concurrency that Wilson wrote up, but if it is stabilized for more "normal" work, should give a quantum leap in capabilities.

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2019833475126227299  

**正文**

Vela (@try_vela_ai) is the AI scheduling assistant built to handle the ambiguity that breaks scheduling.

Add it to any conversation and it negotiates on your behalf - white-glove coordination for your most complicated workflows.

Vela is already trusted by enterprise recruiters and sales teams for white-glove scheduling at scale.

Congrats on the launch @gobhanusk and @skorisep!

https://www.ycombinator.com/launches/PNn-vela-ai-scheduling-that-adapts-to-how-you-work

---


**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2019853198627061909  

**正文**

Whenever I watch @theo’s videos, he often mentions @simonw.

He has more than 4,500 blog posts, so instead of reading them all, I built an AI agent powered by @nozomioai that searches them for me. 

---


**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2019939621216592131  

**正文**

牛P，Claude Code 推出 ”后悔药”功能

输入 /rewind
或者连按两下 ESC 键

就能让对话倒回到之前的状态，并且它还会把你刚才倒回之前的内容总结一下

了解你要干什么，猜测你为什么倒回

这个功能特别适合:

1、探索不同的解决方案 ：比如你让 Claude 用方法 A 实现了某个功能,觉得不太满意,可以回溯回去,让它用方法 B 再试一次

2、避免走弯路：即使回到了之前的状态,你仍然能看到刚才尝试过程中的关键发现和教训

3、迭代优化：可以反复尝试不同的技术路径,同时保留每次尝试的精华部分

就像玩游戏存档读档，但读档的时候，你还记得刚才那次”游戏”里学到的攻略技巧。

既能重新开始，又不会白白浪费之前的经验。

---


**作者** 外汇交易员（@fxtrader）  
**貼文連結** https://x.com/fxtrader/status/2019678696374956116  

**正文**

腾讯云CodeBuddy团队发布桌面Agent工具“WorkBuddy”，并开启内测。

据介绍，WorkBuddy可直接在本地电脑自主规划并执行多模态复杂任务，例如Excel数据清洗，业务数据日志分析等，还内置了多种海内外模型和主流MCP Server和Skills技能包等。

Manus、OpenClaw、Claude Cowork都是腾讯的学习对象。 

---


**作者** Natalie（@gr00vyfairy）  
**貼文連結** https://x.com/gr00vyfairy/status/2019788175783473642  

**正文**

Killer workflow for content with @ManusAI  by @dickiebush 

I took it one step further and built a skill based on the insane tips in the article. 

What the skill does:
- Searches platforms for all your existing content
- Pulls transcripts from every video and podcast
- Organizes everything into a clean archive
- Extracts your top frameworks and stories
- Generates new content using your authentic voice

Comment "Manus Skill" and I'll DM it to you!

---


**作者** ℏεsam（@Hesamation）  
**貼文連結** https://x.com/Hesamation/status/2019953431104901456  

**正文**

Claude Code Agent Teams is Anthropic’s most important update and this article beautifully explains everything you need to know:
> agent teams vs sub-agents
> how they work and the benefits
> how to enable it in your Claude Code
> what tasks to use it for
> teams best practices

---


**作者** Inference（@inference_net）  
**貼文連結** https://x.com/inference_net/status/2019503987217801241  

**正文**

The LLM Engineering Roadmap.

If you want to start today, here's the roadmap👇

1️⃣ LLM Foundations
Start by understanding Python and LLM APIs and how they work.
Learn prompt engineering, structured outputs, and tool use.

↳ Python/Typescript Basics
↳ LLM APIs
↳ Prompt Engineering
↳ Structured Outputs
↳ Function Calling

2️⃣ Vector Stores
Before building anything, you need to understand how text becomes vectors.
Learn embedding models, chunking strategies, and similarity search.

↳ Embedding Models (OpenAI Ada, Cohere, BGE)
↳ Vector Databases (Pinecone, Qdrant, ChromaDB, FAISS)
↳ Chunking Strategies
↳ Similarity Search

3️⃣ Retrieval-Augmented Generation (RAG)
This is how LLMs answer questions using your data.
You learn how to retrieve context and feed it correctly.

↳ Orchestration Frameworks (LangChain, LlamaIndex)
↳ Ingesting Documents
↳ Retrieval Methods (Dense, BM25, Hybrid)
↳ Reranking
↳ Prompt Templates

4️⃣ Advanced RAG
This steps helps you understand how to make RAGs reliable and accurate.

↳ Query Transformation
↳ HyDE
↳ Corrective RAG
↳ Self-RAG
↳ Graph RAG

5️⃣ Fine-Tuning
Sometimes prompts are not enough for a specialised use case.
Fine-tuning will help you understand how models learn domain-specific behaviour.

↳ Data Preparation
↳ LoRA, QLoRA, DoRA
↳ SFT, DPO, RLHF
↳ Training Tools (Unsloth, Axolotl, HF TRL)

6️⃣ Inference Optimization
Once systems work, they need to be fast and affordable.
This step focuses on learning performance and cost efficiency.

↳ Quantization (GGUF, GPTQ, AWQ)
↳ Serving Engines (vLLM, TGI, llama.cpp)
↳ KV Cache
↳ Flash Attention
↳ Speculative Decoding

7️⃣ Deployment
Models are useless if they stay in notebooks.
Here you learn how to ship LLM systems to users.

↳ GPU Scheduling
↳ Cloud Platforms (AWS Bedrock, GCP Vertex AI)
↳ Docker, Kubernetes
↳ FastAPI, Streaming (SSE)

8️⃣ Observability
This step helps you track quality, latency, and cost.

↳ Tracing (LangSmith, Langfuse, Arize Phoenix)
↳ Latency (TTFT)
↳ Token Usage
↳ Cost Tracking

9️⃣ Agents
Agents allows LLMs to plan and use tools.
Learn them to understand how LLMs solve multi-step and complex tasks.

↳ Frameworks (LangGraph, CrewAI, Autogen)
↳ Function Calling
↳ Memory Systems
↳ Patterns (ReAct, Plan-and-Execute, Multi-Agent)

🔟 Production & Security
Production LLM systems can fail in subtle ways.
This step helps you prevent misuse, outages, and cost spikes.

↳ Prompt Injection Defense
↳ Guardrails (NeMo, Guardrails AI)
↳ Semantic Caching
↳ Fallbacks & Rate Limiting

♻️ Repost if you found this insightful

Follow us for more AI engineering content!

---


**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2019926410719355164  

**正文**

沙箱是 Agent 的新后端：能力越强，隔离越必要

LangChain 团队基于 Deep Agents 开发实践发现： 当Agent 拥有 shell 执行权限，它的生产力上限和破坏力上限同时被拉满。write_file 能写代码，也能覆盖关键文件；execute 能跑测试，也能 rm -rf /。bash 是图灵完备的，工具白名单、提示词工程、模型对齐都无法从根本上封堵攻击面。

Deep Agents 的设计：沙箱即后端
Deep Agents 新版最核心的架构决策是把沙箱定义为一种可插拔后端，与已有的 State、Filesystem、Store 后端同级。对 Agent 来说，在本地跑和在远端容器里跑没有区别，接口完全一致。
扩展接口极简——新的沙箱提供商只需实现一个 execute() 方法，所有文件操作由基类在其上自动构建。与其给 Agent 十几个受限专用工具，不如给它一个完整 shell，然后在环境层做隔离。表达力更强，安全边界更清晰。

沙箱的局限
沙箱隔离是必要条件，但不是充分条件。
沙箱防不住两件事。一是网络外泄——被注入的 Agent 可以通过 HTTP 或 DNS 把数据发出去。二是上下文注入——攻击者控制了 Agent 输入的一部分，就能在沙箱内执行任意命令。
因此官方给出硬性原则：永远不要把秘密放进沙箱。 需要认证的操作应放在宿主机侧的工具中完成，Agent 只调用工具名，永远看不到凭证。

四种沙箱选择，四级隔离梯度
· Node.js VFS — 内存虚拟文件系统，零成本极速启动，隔离最弱，适合本地开发和快速实验。
· Deno microVM — 微虚拟机级隔离，启动快成本低，适合中等信任的JS/TS工作负载。
· Daytona — 云端开发工作空间，完整容器环境，冷启动快，适合团队协作和持久化开发。
· Modal — 容器级最强隔离，支持 GPU 和网络封锁，成本最高，面向生产级和ML工作负载。
没有"正确的"隔离级别，只有与风险容忍度和性能需求匹配的选择。本地开发用 VFS，CI 用 Deno/Daytona，生产用 Modal ——自然的渐进路径。

行业信号
当 LangChain JS 把沙箱提升为框架中的一等公民，配套完整文档、安全模型和四种梯度实现时，它在向生态发出明确信号：2025-2026 年的 Agent 竞争已从"拼模型智能"转向"拼工程边界"。安全范式也在转变——不再指望模型不做坏事，而是假设它可能做任何事，然后用环境隔离限制后果。
从"预防"到"遏制"，这是 Agent 工程化真正成熟的标志。

---


**作者** Zach Lloyd（@zachlloydtweets）  
**貼文連結** https://x.com/zachlloydtweets/status/2019877685980196937  

**正文**

2026 is going to be the year that development actually moves to the cloud.

Folks have been talking about this shift for a long time – after all, other productivity apps moved to the cloud long ago, from Google Docs to Figma etc. It’s pretty unusual to use an offline desktop app to do knowledge work these days.

But up until now, there hasn’t been a great reason for software development to move off of the laptop and into the cloud. In fact, there were some good reasons it shouldn't. [I wrote a blog about this a few years back](<https://www.warp.dev/blog/why-is-it-taking-so-long-for-cloud-dev-environments-to-catch-on>). TL;DR: the pull to work in the cloud wasn’t that strong for developers, the setup costs were high, and the ergonomics were poor compared to local development.

This is all going to change this year, and not in the way anyone would have predicted a few years back.

It’s all because of... you guessed it... agents.

The reasons are simple:

- We are running out of laptop capacity. We maintain a large-scale Rust codebase for the @warpdotdev terminal app, and running even two cargo builds simultaneously will strain our SOTA Macbooks. Let alone 10 agents running in parallel.
- Agents cannot test their work simultaneously if they need computer access. Say, to click around a native application using a mouse. This requires sandboxing to run agents in parallel.
- Agents need to be working at all times, regardless of whether your computer is awake. They are increasingly running off of timers and system events and can’t be tied to laptop state. A Mac Mini in your closet isn't going to cut it.
- Companies want visibility and tracking of agents. This points to less of a DIY workflow and more standardization of orchestration and tracking off of personal machines.
- And the big one: agents actually make it much easier to set up cloud environments! This used to be a pain in the a\*\*… making Docker files, provisioning machines, etc. A lot of the tedious configuration can be handled by agents now.

There’s still a bunch to figure out to make all of this work well, and this is an area Warp is actively investing in – trying to make the easiest, scalable solution for agents in the cloud, that still allows the right amount of human-in-the-loop, tracking, etc.

Curious if other folks see this the same way… and if you do, keep an eye on the @warpdotdev timeline next week.

---


**作者** Bytebytego（@bytebytego）  
**貼文連結** https://x.com/bytebytego/status/2019821037903626507  

**正文**

9 Key AI Concepts Explained in 7 minutes

- Tokenization
- Text Decoding
- Prompt Engineering
- Multi Step AI Agents
- RAGs
- RLHF
- VAE
- Diffusion Models
- LoRA 

---


**作者** Vihaar Nandigala（@VihaarNandigala）  
**貼文連結** https://x.com/VihaarNandigala/status/2019833820108005503  

**正文**

We just raised a $5.3M seed round for Orange Slice, co-led by 1984 Capital and Moxxie Ventures, with participation from angels like Paul Graham.

We’re building AI agents, inside a spreadsheet, that help sales teams find companies that already want to buy.
The reality is most sales teams don’t struggle with effort - they struggle with timing.

Reps spend huge amounts of time working static lists and broad targeting, chasing leads that were never going to convert. That creates noise, low reply rates, and wasted cycles.

Top companies like Ramp solve this with dedicated growth engineers building internal data workflows.
We’re making that same capability accessible to everyone else.

At its core, the challenge is simple: finding customers who already have the problem you solve.

Orange Slice turns the spreadsheet into a system for discovering buying signals - agents research company sites, news, social signals, and niche sources like court records or building permits, then structure that information directly into columns teams can act on.

Not “might be a fit.”
But “likely in-market.”

So instead of guessing who to target, teams build and refine living lists of high-intent accounts inside a sheet.

Still early. Still learning.
But we’re excited to keep building.

Kishan and I met sophomore year on a Bollywood dance team at Michigan — and I couldn’t ask for a better co-founder.

Grateful to our team, customers, and investors for believing in this vision.

---


**作者** Andy Berman（@berman66）  
**貼文連結** https://x.com/berman66/status/2019818438282133667  

**正文**

Today, we're launching OpenClaw for Enterprise.

The IDEA of OpenClaw is excellent. 

That's why your employees already tried ClawdBot last weekend. They probably spent hours linking it to everything - email, Slack, Jira, you name it. 

They installed a giant security nightmare. 

1/

---


**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2019748259946737808  

**正文**

OPS 4.6 + Agent Teams + Claude Code 做的 Claude Code UI 

客户端已经打包，马上就会开源 

---


**作者** Mau Baron（@maubaron）  
**貼文連結** https://x.com/maubaron/status/2019633706890063923  

**正文**

we will be the first founders in the world
to win a YouTube Play Button 

WITH COMPLETELY AUTOMATED CONTENT
we already have 60,000 subs in 4 months 

and we just scheduled another 480+ videos 
(we literally couldn't schedule more)   

it took @ErnestoSOFTWARE and i 
10 mins to make the videos  

all of them were made with python 
and already got us millions of views

---


**作者** Michael（@michael_chomsky）  
**貼文連結** https://x.com/michael_chomsky/status/2019557367231164780  

**正文**

I recommend doing this accelerator later in your company's stage.

The major advantage is the credits and a company just getting started has no way to use them.

Before applying ask yourself:
1. Do I need Soc2? 
2. Can I spend 30k+ in LLM credits on something useful?
3. Do I need enterprise auth, or are my db costs significant?

If the answer is yes to at least two of these send it, otherwise I think this is a massive waste.

Just focus on getting customers and improving product instead of thinking about prestigious accelerators.

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2019486182896464020  

**正文**

.@oximyhq shows enterprises everything their employees do with AI. Which tools, how much they cost, and where sensitive data is going.

One platform for discovery, spend intelligence, and data protection.

Congrats on the launch @namanambavi!

https://www.ycombinator.com/launches/PNC-oximy-see-everything-your-company-does-with-ai 

---


**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2019654207377182768  

**正文**

npx skills add nozomio-labs/nia-skill 

---


**作者** Mayank Agarwal（@maynkag）  
**貼文連結** https://x.com/maynkag/status/2019498219236159770  

**正文**

We’re announcing our $125M Series A to build AI for Prod. This funding round was led by Lightspeed Venture Partners, with participation from Greylock, Unusual Ventures, Artisanal, and A*,  and values

---


**作者** Fondo.com（@Fondocom）  
**貼文連結** https://x.com/Fondocom/status/1854562961550950592  

**正文**

Knowing your cash position is essential

It’s not about fancy reports

It’s survival 

---


**作者** scott belsky（@scottbelsky）  
**貼文連結** https://x.com/scottbelsky/status/2019611850116329888  

**正文**

seeing a new cohort of “governance for agents” and monitoring applications to inspect agentic actions and manage the guardrails. congrats to @JiquanNgiam and @MintMCP_AI team on the launch

---


**作者** Sparkles ✨（@Sparklesdotdev）  
**貼文連結** https://x.com/Sparklesdotdev/status/2019577797677887535  

**正文**

@davj ✨

---


**作者** David J Phillips（@davj）  
**貼文連結** https://x.com/davj/status/2019574702365401400  

**正文**

Less than 1% of people know how to use terminal

So every time marketing wants to change a button color, they're waiting 2 days for a dev who "doesn't really care about the font on the front end"

Daniel dropped out of UCL, flew from London to SF, and built Sparkles in 4 weeks to fix this

Your CTO connects the GitHub repo once

Now anyone with a company email can make changes and open PRs

No terminal. No local setup. No IDE.

One AI run = one commit. Devs review clean diffs with auto-generated summaries.

If your stack deploys on Vercel, you're already compatible

We cover:

> Why he pivoted from his W26 YC interview idea to Sparkles

> The "upload changes" button that replaced PR terminology

> Who's actually buying: UX designers, non-technical CEOs, GTM teams

> How version control works when non-devs are shipping code

🎙️@aidaniil, CEO & Founder, @sparklesdotdev (YC W26) on @Fondocom @thestartpod 

00:15 UCL dropout → SF → YC; building Sparkles
01:17 The pain: tiny UI asks stuck in backlog
02:07 Early ideas (Flex, evals) → audience pivot to non-technical teammates
03:01 Onboarding: install Sparkles GitHub App
04:02 PR flow: Upload Changes → auto commit messages → one run = one commit → clean diffs
05:05 Personas: UX designers, non-technical CEOs, GTM; why access compounds velocity
06:08 Capability spectrum: from never-coded to power users; no terminal required
07:02 Roadmap: version control, preview/staging on custom domains; solo-founder pace

---


**作者** Aaron Iker ✨（@aaroniker）  
**貼文連結** https://x.com/aaroniker/status/2001825688421310829  

**正文**

joined the sick team at @opencode - very excited about the product, and even more what's ahead ✨ 
joined the sick team at @opencode - very excited about the product, and even more what's ahead ✨ 
https://www.aaron.page/opencode
https://www.aaron.page/opencontrols

---


**作者** Atoms（@atoms_dev）  
**貼文連結** https://x.com/atoms_dev/status/2019622944432074783  

**正文**

Claude Opus 4.6 has just been released,
bringing fresh attention to agentic workflows.

Our earlier open-source work @metagpt_ on multi-agent systems
influenced how we think about agent orchestration today.

Sharing a visual overview ↓ 
Claude Opus 4.6 has just been released,
bringing fresh attention to agentic workflows.

Our earlier open-source work @metagpt_ on multi-agent systems
influenced how we think about agent orchestration today.

Sharing a visual overview ↓ 
ICLR Oral 2024: https://arxiv.org/abs/2308.00352

---


**作者** Ramp Labs（@RampLabs）  
**貼文連結** https://x.com/RampLabs/status/2019542333713195051  

**正文**

Here's it doing a full vendor spend analysis from a single prompt. Raw transaction data → pivot by month → categorize by strategic vs. non-strategic → rate each vendor → write across tabs.
https://labs.ramp.com/sheets?share=d90e8f20-2cc1-4564-8d85-633f47f17b7e
Opus 4.6 is now live in Ramp Sheets.

It’s a step-function improvement (~30% according to our internal benchmarks) for multi-step financial logic and spreadsheet work.

Ramp Sheets is the fastest way to try out Opus 4.6 for free. 
Here's it doing a full vendor spend analysis from a single prompt. Raw transaction data → pivot by month → categorize by strategic vs. non-strategic → rate each vendor → write across tabs.
https://labs.ramp.com/sheets?share=d90e8f20-2cc1-4564-8d85-633f47f17b7e

---


**作者** Farhan（@mhdfaran）  
**貼文連結** https://x.com/mhdfaran/status/2019429370528748027  

**正文**

McKinsey AI Report has shocked the world.

But nobody has time to read 30 pages of data, so I used Dokie AI to turn the entire report into a high-end presentation in seconds.

This is the ultimate workflow for busy people

Tutorial + Slides: 🧵 
McKinsey AI Report has shocked the world.

But nobody has time to read 30 pages of data, so I used Dokie AI to turn the entire report into a high-end presentation in seconds.

This is the ultimate workflow for busy people

Tutorial + Slides: 🧵 
Long AI reports are goldmines, but they are a nightmare to summarise.

I needed to break down "The State of AI 2025" for a meeting.

Usually, this is 4 hours of reading and manual formatting. 
Most AI tools just summarise text.

Dokie actually analysed the report structure.

It pulled out the key trends, adoption rates, and risks automatically. 
This was the "click" moment for me.

It didn't just dump text onto a white slide.

It suggested themes and layouts that actually look like a human designer made them. 
Look at the charts.

Dokie interpreted the data from the PDF and rebuilt the visuals.

The "Executive Takeaway" slide was ready to present immediately. 
I decided the first theme didn't fit the "vibe" of my meeting.

In any other app, changing a theme means hours of fixing broken text.

Here? I swapped to a bold, neon theme and everything re-aligned instantly. 
Check out the final presentation here: http://dokie.ai/presentation/share/w87X4Kzy8PBb 
Tools should make you faster, not give you more work.

I went from a raw PDF to a polished 11-slide deck while my coffee was still hot.

If you're tired of fighting with PowerPoint, give this a look.

Try it here: https://dokie.ai/

---


**作者** John Rush（@johnrushx）  
**貼文連結** https://x.com/johnrushx/status/2019611904465862905  

**正文**

My mind literally burning

- kling makes videos indistinguishable from reality 

- OpenAI Codex & Claude Code just sent all ai coding critics into depression 

- OpenAI Frontier meant to replace one billion workers with ai agents

- OpenClaw is the new ChatGPT moment for personal assistance

- MoltBook start a whole wave of sites and services for agents only 

- the smartest people of earth all say that we entered first days of singularity 

- and things are only accelerating…

The fomo is insane, I’m sleeping 4h a day these days, building my own ai agents @seobotai @listingbott @socialbothq @tinyadz_

---


**作者** Santiago（@svpino）  
**貼文連結** https://x.com/svpino/status/2019410949749559621  

**正文**

Opus 4.5 is so good that declarative prompting is now becoming possible for the first time.

Here is how I usually think about prompting the model:

"Rewrite this function using a hash map instead of nested loops."

That's "imperative prompting."

With the latest iteration, you can now try this instead:

"This function is too slow. Make it faster without changing what it returns."

That's declarative prompting.

This doesn't always work (the agent sometimes needs more context and details to not screw things up), but my success rate is much higher than ever before.

---


**作者** Manus（@ManusAI）  
**貼文連結** https://x.com/ManusAI/status/2019426532796600371  

**正文**

🚀 Manus Academy is dropping a new course for Product Managers.

Find PM-specific use cases that connect across your entire stack:
→ Pull backlog from Linear, score with RICE, push back priorities
→ Generate weekly leadership updates from Slack, Notion, and Linear
→ Draft PRDs from user research across tools

and much more. 

PM-specific use cases. Cross-tool connectivity. Zero context switching.

---


**作者** Ryan Carson（@ryancarson）  
**貼文連結** https://x.com/ryancarson/status/2019405458881257533  

**正文**

This is exactly what I was looking for.

Getting this spun up locally.

Will report back.

---


**作者** ℏεsam（@Hesamation）  
**貼文連結** https://x.com/Hesamation/status/2019179444485705941  

**正文**

i still believe that if you want to learn AI engineering, there’s no better roadmap than this one by @maximelabonne. 

it’s technical, written by an expert, and covers the fundamentals and science behind LLMs.

i also wrote an article on common mistakes you want to avoid 😉 

---


**作者** John Rush（@johnrushx）  
**貼文連結** https://x.com/johnrushx/status/2019406744925913502  

**正文**

My 9-step process for using Codex to write a book instead of coding:

❗️important: the book isnt ai generated, it's ai-edited

1. I scraped all my youtube videos, articles, interviews, tweets, replies into a folder called "Intake" (about 200 pages of my manually written content from the past 4 years)

2) i've given codex the outline of my book and asked it to generate a folder structure using files for.

😢 I also gave it a draft of a book(ive been writing a draft for the last 12 months but felt like going nowhere because it turns out to be super difficult to write a book, compared to writing an article)

3) i asked it to take all my content from the "intake" folder and restructure it to fit the outline

4) I asked it to run an interview asking me for any missing questions

5) then I manually edited all 100 pages, reading each word in it and editing without trying to format it

6) then i asked codex to make sure it's formatted and de-duplicated

7) then I asked codex to act as a junior founder and read my book and come up with 100 questions...I answered those with my voice and codex incorporated the answers into the book

8) then i asekd to repeate the step7 by pretending to be a founder with a little traction...then with more traction...then as a founder of an app...then as a founder of micro saas and so on.

9) the final output is that 99% of the context in the book is actually word-for-word written/said by me and codex's job was to organize it

Im releasing the book this week

Time-wise, I put 1000 hours into it(all the hours i spent writing all my content in the last 4 years)

It's still running with 50% discount for a pre-order that's expiring right after I publish it https://johnrush.me/#header-23-155381

---


**作者** Kevin Rose（@kevinrose）  
**貼文連結** https://x.com/kevinrose/status/2019640020240593072  

**正文**

Sorry in advance:
"Develop a framework-level PRD that proposes a novel, multi-agent architecture - comprising hierarchical roles such as leaders, judges, and workers, designed to ingest, crawl, index, and continuously debate the foundational texts of the world’s major religions (provided as primary-source PDFs). The system should operate as a long-running process, capable of sustained reasoning over days, weeks, or years, with mechanisms for adjudication, synthesis, and convergence. The objective is not speed or superficial summarization, but the progressive distillation of cross-tradition principles into a coherent, internally consistent set of ethical axioms and practical rules for living, optimized toward truth-seeking and philosophical convergence."

---


**作者** Autumn（@autumnpricing）  
**貼文連結** https://x.com/autumnpricing/status/2019566182815396183  

**正文**

Excuse me

---


**作者** 成峰-AI产品自由（@chengfeng240928）  
**貼文連結** https://x.com/chengfeng240928/status/2019562039493161286  

**正文**

作为一个用 Claude Code 写代码的选手，我发现 Agent 时代对人有个挑战：
你能产出多少，取决于你能并发多少
为了更快切换项目，我找了个工具叫 zoxide，用它做了一个"终端快速启动器"。

---


**作者** ℏεsam（@Hesamation）  
**貼文連結** https://x.com/Hesamation/status/2019578889606164758  

**正文**

— Opus 4.6 parallel agents wrote a 100,000 line C compiler from scratch in 2 weeks and it successfully compiled Linux.
 
— this is not your average purple-gradient landing page, it’s BIG.

— the scaling laws of training are obviously valid in inference-time scaling too. 

---


**作者** TBPN（@tbpn）  
**貼文連結** https://x.com/tbpn/status/2019547333298647093  

**正文**

"Every company is now an API company, whether they want to be or not."

@sama answers the question: "Is software dead?" 

---


**作者** Liz Wessel（@lizwessel）  
**貼文連結** https://x.com/lizwessel/status/2019571528501961021  

**正文**

For B2B founders trying to land their first few million in revenue, your sales pipeline (especially a weighted one!) should be one of the most helpful tools you have for understanding how your

---


**作者** Karel（@KarelDoostrlnck）  
**貼文連結** https://x.com/KarelDoostrlnck/status/2019477361557926281  

**正文**

I use billions of codex tokens. Here is my setup and is what I learned.
 
Many people drastically underestimate what codex can do. Even some of my colleagues still underutilize codex, but they are

---


**作者** Robert Scoble（@Scobleizer）  
**貼文連結** https://x.com/Scobleizer/status/2019584936668528715  

**正文**

When I worked at Microsoft, the compiler team was the smartest per employee of any, and it wasn't even close to number two.

---


**作者** Aakash Gupta（@aakashgupta）  
**貼文連結** https://x.com/aakashgupta/status/2019560350333731253  

**正文**

Agent swarms are amazing. I have been using them non-stop since the release 6 hours ago.

They enable you to move so much faster.
Here’s what most people won’t realize for another 6 months: this changes who can build software, and how fast.

Claude Code hit $1B in run-rate revenue in six months. Faster than ChatGPT. Boris Cherny, the head of Claude Code, was already running 5 parallel Claude instances in terminal plus 5-10 on http://Claude.ai simultaneously. That was the manual version of what agent teams now automate natively.

The old workflow was: prompt one agent, wait, review, prompt again. Sequential. The new workflow is: describe what you want, a lead agent decomposes it, spawns specialists for frontend, backend, testing, and docs, and they coordinate with each other while you do something else.

That’s a 4-5x throughput increase per developer. And the compounding effects matter more than the raw speed. Each teammate gets its own fresh context window, which solves the token bloat problem that kills single-agent performance on large codebases.

The real unlock: a PM or founder who couldn’t code before can now orchestrate a team of AI agents the same way an engineering manager orchestrates human engineers. Describe the architecture, delegate the work, review the output.

We just went from “AI writes code for you” to “AI runs an engineering team for you.” And that’s a fundamentally different product category.

---


**作者** Jay Hack（@mathemagic1an）  
**貼文連結** https://x.com/mathemagic1an/status/2019488541516952050  

**正文**

Unbelievably cool agent experience just now

Looking for researchers to co-author a paper

Kicked off @clickup agent - deep researches web, finds 10 candidates, makes a CRM and drafts personalized outreach emails.

This would have taken a PR agency a week 

---


**作者** PlayerZero（@playerzero_ai）  
**貼文連結** https://x.com/playerzero_ai/status/2019506518912299289  

**正文**

The real gains for CTOs and VPEs come from reducing MTTR, preventing defects, and reclaiming engineering capacity. We built a playbook on how to measure and maximize AI ROI where it matters most: https://playerzero.ai/resources/the-engineering-leaders-playbook-for-achieving-real-roi-with-ai

---


**作者** Jaya Gupta（@JayaGup10）  
**貼文連結** https://x.com/JayaGup10/status/2019566283034157465  

**正文**

“What we do not carry into abstracted traces is raw text (doc bodies, message text), user identifiers, or customer‑specific secrets. We then compute similarity between abstracted traces to figure out which ones are likely to involve the same process.

On top of that, we only treat a pattern as viable if it appears across at least k distinct users and n independent traces, with anything too rare dropped to preserve anonymity.”

---


**作者** 向阳乔木（@vista8）  
**貼文連結** https://x.com/vista8/status/2019642162674336244  

**正文**

Claude Agent team太强了！

完全不是用Prompt虚拟几个Agent配合，而是真的几个Agent交流，且跟Subagent也不一样。

Subagent 像派出去的侦察兵

给它一个任务，它干完了把结果交给你，任务结束。
侦察兵之间不会聊天，也不会质疑对方的情报。

Agent Teams 像一个项目组

每个成员都是独立的个体，有自己的记忆、自己的判断。他们可以直接给彼此发消息，可以开会讨论，可以反驳对方的观点。

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2019522008502136865  

**正文**

.@trylaurence automates performance marketing for CPG brands, starting on Amazon.

They use reinforcement learning to set bids, budgets, and keyword targets like quant hedge funds trade markets: continuous optimization on autopilot.

Congrats on the launch @mlaurencechen and @LGierhake!

https://www.ycombinator.com/launches/PNP-laurence-automated-amazon-advertising

---


**作者** Gokul Rajaram（@gokulr）  
**貼文連結** https://x.com/gokulr/status/2019571976046801252  

**正文**

Check out where Systems of Recoard sit in this diagram from @OpenAI Frontier.

At least 3, if not 4, layers of context and intelligence sit between them and the end business application.

It's one of the clearest representations of how AI  companies plan to build next-gen systems of action on top of existing SoR, and why the markets are so worried about the future of software companies. 

PS: Even the color coding  subtly highlights where OpenAI thinks  value will accrue. The SoR layer is white and can almost be missed if one don't look closely!

---


**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2019622277416141020  

**正文**

我去，太牛逼了，朋友们太猛了！

Opus 4.6 加 agent teams，不到一小时就帮我完成了这个我一直想做的一个产品

一个 Cloud Code 的 UI 版本。

它具有以下特点：

1. 所有的配置跟你本地的 Cloud Code 联动
2. 可视化地管理和设置 Cloud Code
3. 可以可视化地配置 MCP、skill 和 plugin
4. 支持调用你本地 Cloud Code 的交互
5. 存着你历史的聊天记录

---


**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2019633723185197285  

**正文**

强烈推荐用OpenClaw给自己做一个人生维基 💀

有人把自己的博客、播客、个人简介，还有 1938413 个关于他的东西全喂给了它。用维基百科条目的形式来浏览自己的一生，他表示真的很有意思——不过说实话，也有点瘆人，不知道该怎么形容。 

---


**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2019637538995183779  

**正文**

有人提出一个很有意思的观点：UGC Engineer将成为社交媒体领域最关键的新兴角色。

UGC工程师的崛起

你觉得这种转变会如何影响内容创作行业？🤔 

---


**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2019550950885847262  

**正文**

再次命中

But 没想到OpenAI 进行了狙击

Claude Opus 4.6 发布

100万 token 上下文+ 多代理协作😩

1. 上下文翻了 5 倍
2. 记忆力提升近 4 倍
3. 知道自己该什么时候深度思考

一小时后GPT-5.3-codex发布，跑分超越Opus… 

---


**作者** Chris（@chatgpt21）  
**貼文連結** https://x.com/chatgpt21/status/2019496520425292220  

**正文**

Anthropic had 16 AI agents build a C compiler from scratch. 100k lines, compiles the Linux kernel, $20k, 2 weeks.

To put that in perspective GCC took thousands of engineers over 37 years to build. (Granted from 1987 - however) One researcher and 16 AI agents just built a compiler that passes 99% of GCC's own torture test suite, compiles FFmpeg, Redis, PostgreSQL, QEMU and runs Doom.

They say they "(mostly) walked away." But that "mostly" is doing heavy lifting.

No human wrote code but the researcher constantly redesigned tests, built CI pipelines when agents broke each other's work, and created workarounds when all 16 agents got stuck on the same bug.

The human role didn't disappear. It shifted from writing code to engineering the environment that lets AI write code.

I don’t know how you could make the point AI is hitting a wall.
Anthropic had 16 AI agents build a C compiler from scratch. 100k lines, compiles the Linux kernel, $20k, 2 weeks.

To put that in perspective GCC took thousands of engineers over 37 years to build. (Granted from 1987 - however) One researcher and 16 AI agents just built a compiler that passes 99% of GCC's own torture test suite, compiles FFmpeg, Redis, PostgreSQL, QEMU and runs Doom.

They say they "(mostly) walked away." But that "mostly" is doing heavy lifting.

No human wrote code but the researcher constantly redesigned tests, built CI pipelines when agents broke each other's work, and created workarounds when all 16 agents got stuck on the same bug.

The human role didn't disappear. It shifted from writing code to engineering the environment that lets AI write code.

I don’t know how you could make the point AI is hitting a wall.
If you want more cool AI news like this in your feed, consider following me, I have nothing to sell you 😊

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2019501284794179865  

**正文**

.@autumn_ai_inc is building the first real-time signal intelligence platform for GTM teams.

Define your ICP and the signals that matter, and Autumn delivers a condensed, real-time feed filtered by intents.

Congrats on the launch @VishnuSampathk1 and @shiv_kampani!

https://www.ycombinator.com/launches/PNL-autumn-ai-stalk-your-prospects-at-scale

---


**作者** Arvind Jain（@jainarvind）  
**貼文連結** https://x.com/jainarvind/status/2019553277571190821  

**正文**

Context graphs are quickly becoming one of the most talked about ideas in enterprise AI, with investors @JayaGup10 and @ashugarg calling them a “trillion-dollar opportunity.”
That’s because while AI

---


**作者** Aniket Panjwani（@aniketapanjwani）  
**貼文連結** https://x.com/aniketapanjwani/status/2019401717364748767  

**正文**

everyone I follow to keep up with AI:

1. @steipete - rn he's getting bogged down with openclaw, which I think is a distraction for >97% of those interested in it. but I read his long form and study his workflows very closely. main learning i've gotten from Pete is make everything a cli + skill
2. @mattpocockuk - long time developer educator who's been pushing the limits on ralph loops. he's interesting as a foil to @steipete in that I respect both of them highly as devs but Matt is really bullish on ralph whereas Peter is really bearish
3. @nicbstme : my day job is director of ai/ml at a fintech. i follow Nicolas very closely because he's the clearest, strongest thinker on the combination of strategic implications of agentic coding to businesses and practicalities of technical implementation
4. @every I think their stuff is good to follow for beginners. I mostly keep up with them by studying changes made to the compound engineering code base moreso than reading their articles, which I think are more oriented at popularization/non technical people than the cutting edge
5. @aiDotEngineer : only YouTube channel on AI I pay attention to, close to cutting edge stuff on agentic coding
6. @bcherny and @karpathy - Boris is more practically useful, Andrej is more helpful at a macro level of understanding as the spiritual godfather of vibe coding
7. @venturetwins - whenever I want to know something about ai/video models I do a search on Justine's timeline
8. @dwarkesh_sp - not practically useful but I want to understand the fundamental economics of LLMs better and Dwarkesh's interviews are the best resource I've found for that
9. @EpochAIResearch - these guys have put together really cool benchmarks and write incredible long form content on AI. I don't read any email newsletters anymore - there are like 2 or 3 i'll just explicitly look up by going to their website, and Epoch's is one of them

---


**作者** Khaliq Gant（@Khaliqgant）  
**貼文連結** https://x.com/Khaliqgant/status/2019124627860050109  

**正文**

I've been building Agent Relay (@agent_relay) using Agent Relay. Agents coordinating to build the tool that lets them coordinate. It's recursive and I love it. I took some time to jot down some

---


**作者** Femke Plantinga（@femke_plantinga）  
**貼文連結** https://x.com/femke_plantinga/status/2019350503168016697  

**正文**

AI agents were THE hype in 2025.

But most still can't explain how they’re different from basic chatbots.

(here’s a refresher)

An AI agent is a system that can:
• Make dynamic decisions about what to do next based on what it learns
• Remember previous interactions and use that context for future decisions
• Use tools adaptively to get things done
• Change its approach when something isn't working

But not all AI agents are built the same. They exist on a spectrum based on how they're architected:

𝗦𝗶𝗻𝗴𝗹𝗲-𝗔𝗴𝗲𝗻𝘁 𝗦𝘆𝘀𝘁𝗲𝗺𝘀

These work like intelligent routers. One agent orchestrates everything - deciding which knowledge sources to pull from, which tools to use, and how to respond. They use frameworks like ReAct (Reason + Act) to handle sequential queries while maintaining context in memory.

𝗠𝘂𝗹𝘁𝗶-𝗔𝗴𝗲𝗻𝘁 𝗦𝘆𝘀𝘁𝗲𝗺𝘀

These are collaborative teams of specialized agents, each with distinct tools, memory, and focus areas. For example:
• One agent handling internal company data
• Another managing personal accounts and calendars
• A third searching public information via web search

By assigning clear roles, these agents can collaborate, debate, and refine outputs to solve problems that would overwhelm a single agent.

The role of vector databases? They're evolving from just knowledge sources to long-term memory systems that agents can use to extract relevant bits of prior conversations.

Learn more about AI Agents and how you can build your own reliable, enterprise-ready agents (no-code) 🧡 

Get your copy of this free ebook by @stackai and @weaviate_io:
https://www.stack-ai.com/whitepaper/weaviate?utm_source=weaviate_socials&utm_medium=post&utm_campaign=012026

---


**作者** Gabriel Chua（@gabrielchua）  
**貼文連結** https://x.com/gabrielchua/status/2019314417746473041  

**正文**

bringing the Codex harness to more products! 

---


**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2019459756889403433  

**正文**

Booko (@booko_app) is bringing dynamic pricing to any business that sells time slots - improving utilization and turning unsold inventory into revenue.

Congrats on the launch @arjunsaluja24 and @HallWill7965!

https://www.ycombinator.com/launches/PMU-booko-w26-dynamic-pricing-for-businesses-that-sell-time-slots 

---

