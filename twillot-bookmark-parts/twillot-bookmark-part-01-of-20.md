# Twillot 書籤（精簡）— 第 1/20 部

原檔：`twillot-bookmark.md` · 已併入 `twillot-bookmark-2026-04-06 (2).csv`（7 則） · 全檔共 3937 則 · **本部第 1–203 則**（共 203 則）

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

**作者** cole murray（@_colemurray）  
**貼文連結** https://x.com/_colemurray/status/2040889792863629602  

**正文**

>be me 
>expert in search and retrieval
>read article about “company memory”
>read implementation 
>dump everything into one db
>basic vector db search
>doesn’t understand query document encoder problem
>no FTS
>no reranker
>every time

---

**作者** Simon Taylor（@sytaylor）  
**貼文連結** https://x.com/sytaylor/status/2040895288416624888  

**正文**

TL;DR Despite ALL the hype from payments companies, agentic commerce isn't happening. Walmart saw a 66% drop in conversion when adding agentic commerce. We shouldn't be trying to embed checkouts in

---

**作者** Sriraam（@27upon2）  
**貼文連結** https://x.com/27upon2/status/2040975201068810670  

**正文**

After reading Cursor's real-time RL blog where they release a new Composer checkpoint almost every five hours, I wanted to build a similar system. Turns out we already have the tools and infra needed

---

**作者** KK.aWSB（@KKaWSB）  
**貼文連結** https://x.com/KKaWSB/status/2041007230917747033  

**正文**

开源的黄金时代来了！

一位老哥用Claude Code 创建了一个 AI 求职系统，该系统对 700 多份求职申请进行了评分，并且真的帮他找到了一份工作。

而且现在是开源的。

它可以扫描多家公司的招聘页面，根据不同的职位修改你的简历，甚至还能自动填写申请表。该代码库包含：
> 14 种技能模式（评估、扫描、PDF、 ...)
> 前往终端仪表盘
通过 Playwright 生成 ATS 优化的 PDF 文件
已预配置 45 家以上公司（Anthropic、OpenAI、ElevenLabs、Stripe 等）

GitHub：https://github.com/santifer/career-ops

---

**作者** vas（@vasuman）  
**貼文連結** https://x.com/vasuman/status/2041012932994318689  

**正文**

Got a new laptop and I remembered how everyone posts "what should I install"

Everyone mentions raycast, wispr flow, and more productivity slop

No one ever mentions what you actually need to install

like Google Chrome, Zoom, Slack, Docker, Brew, and Spotify 

---

**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2041022789843653027  

**正文**

my brain is telling me to play around with @nozomioai core infra and tweak it so it works for that use case as well.

any thoughts? is it still relevant?

---

**作者** 艾略特（@elliotchen100）  
**貼文連結** https://x.com/elliotchen100/status/2040981753490477403  

**正文**

Karpathy 4月3日发了一条关于"LLM Knowledge Bases"的推文，1500万浏览，4.8万赞，8.8万收藏。两天后他又 quote 了自己，把想法整理成了一个 GitHub Gist，又拿到了480万浏览。Gist 本身拿了将近 5000 个 Star。

---

**作者** 鸭哥（@grapeot）  
**貼文連結** https://x.com/grapeot/status/2040882211961069643  

**正文**

Agentic AI编程工具写一两千行的原型行云流水。但一旦项目突破5000行，魔法就失灵了。开始看不清全局架构、记不住历史决策、代码充斥诡异bug。你不得不频繁手动干预。问题出在记忆机制——context window就那么大，项目一大就装不下了。

---

**作者** 李韭二（@li9292）  
**貼文連結** https://x.com/li9292/status/2040805282813730841  

**正文**

19 倍。14 个月，从 10 亿到 190 亿美元。
Anthropic 增长负责人 Amol Avasare 刚在 Lenny Podcast 上做了将近两小时的深度访谈。
这个人通过一封冷邮件加入了 Anthropic，创业失败过，经历过脑损伤，

---

**作者** Itai Damti（@itaidamti）  
**貼文連結** https://x.com/itaidamti/status/2040877793454493920  

**正文**

Slides: https://drive.google.com/file/d/18Llfqt5wRx6IEp8d_0Tg9-JNgZj04Qbp/view?usp=drive_link
These are some slides I created this week (without AI!) to help our team understand basic concepts around agentic money. It led to great conversations.

I tried to make

---

**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2040863432157856229  

**正文**

being solo for almost a year taught me a lot about what i want from people and the pace we should operate at.

this will be stressful and intense. but also insanely fun.

i’m the type of person who wants to avoid boring corporate structure miles away from anything i build. that shows up in how i think about company + culture:

- fuck your 9-9-6. that is EXTREMELY performative. i work every day. i sleep and breathe this company, so there’s no need for that structure if you truly love what you do.

- no fixed wake-up times. sleep whenever you want, just get your 8 hours

- health matters a lot. i want everyone around me operating at 100%.

- i won’t outsource things i don’t understand myself. sales, marketing, etc. if i suck at it, i learn it first

- i will be very demanding. this is a 10-year journey. but i make sure everyone is taken care of (housing, strong equity, great comp obv)

- you need to be socially capable and talk to girls. most engineers on this platform just sit in their rooms 24/7, goon to manga, and are afraid to go outside. people who promote bs like “never touch grass, just code” are stupid imo even tho i spend 95% of my time at the office.

this isn’t the old era where pure engineering was enough. any strong engineer should be able to write, record, talk to users, and help with distribution.

i look for that and push for it. the easiest signal is simple: you’re not socially cooked.

this is the environment i want to build. not for everyone, but perfect for the right people.

my DMs are always open.

---

**作者** Eliano A Younes（@eliano）  
**貼文連結** https://x.com/eliano/status/2040839044762906853  

**正文**

A deep dive on Palantir’s FDEs by @christjine was published yesterday in @MarketWatch 

“For years, the rest of Silicon Valley dismissed the FDE role as an unserious gig. Investors shared this opinion, arguing that Palantir was more of a glorified consultancy than a legitimate tech company…. Now companies are looking to copy Palantir’s approach. 

Revered today as the “hottest” job in tech, the FDE title is plastered across job boards and employed by companies ranging from AI startups to software-as-a-service behemoths racing to carve out their sphere of influence in the burgeoning enterprise-AI market.”

https://www.marketwatch.com/story/palantir-pioneered-the-hottest-job-in-tech-its-legions-of-copycats-may-not-succeed-bdd581e3?gaa_at=eafs&gaa_n=AWEtsqf4ekOZJ3QOeAl9LxTWUAMd4cXaMlMcm2XlUtX1uRJXUYnJdqWRG_veIgYveJU%3D&gaa_ts=69d1d6ef&gaa_sig=bDQSPCxQyiYy0cEqyJAmTa6xEoTrOjQyRt1UtrlclkldPdfhM-z8lBTEr18bLgRVPZ3XGQVeyiboPoyupbZYtQ%3D%3D

---

**作者** Allie Howe（@vtahowe）  
**貼文連結** https://x.com/vtahowe/status/2040832207087194448  

**正文**

What is a Context Graph?
I first learned about context graphs from @akoratana. On an Insecure Agents podcast with Animesh I learned that a context graph is a system that captures and stores how

---

**作者** Zack Korman（@ZackKorman）  
**貼文連結** https://x.com/ZackKorman/status/2040836360391512314  

**正文**

Narrative violation: @cluely is the only Delve customer I've seen that removed the compliance claims from their site. 

Everyone else just hid the connection to Delve but still bragged about their compliance. 

---

**作者** KK.aWSB（@KKaWSB）  
**貼文連結** https://x.com/KKaWSB/status/2040613275201900639  

**正文**

当你发现用Claude Code能马上开发出你脑子里想要的任何项目时，你的第一反应不是"太好了"，而是"怎么让它24小时不停地干"。

但用过的人都知道，Agent自动跑着跑着就会被卡住。这篇文章讲的就是解决方案——Harness。

推荐阅读👇 

---

**作者** 沐阳（@yyyole）  
**貼文連結** https://x.com/yyyole/status/2040723020705345994  

**正文**

原来，10后已经黑客松的常客了。
4000+小时AI探索开发，有意思，每天5小时中高强度使用，都要需要两年多。

小红书黑客松巅峰赛，48小时将创意落地，总奖50万，200+选手。
据说很多10后…… 

---

**作者** Ksenia_TuringPost（@TheTuringPost）  
**貼文連結** https://x.com/TheTuringPost/status/2040752778113659345  

**正文**

9 open agents that can improve themselves (a collection inspired by Hermes Agent)

▪️ HyperAgents
▪️ Agent0
▪️ EvoAgentX
▪️ AgentEvolver
▪️ Agent Zero
▪️ Letta Code
▪️ LettaBot
▪️ LangGraph Reflection
▪️ SuperAGI

Save this list and check it out for links and to explore how these agents self-evolve: https://www.turingpost.com/p/agentselfimprovement

---

**作者** 阿绎 AYi（@AYi_AInotes）  
**貼文連結** https://x.com/AYi_AInotes/status/2040464515662598384  

**正文**

这个多 Agent 架构，直接焊死了AI swarm最致命的死穴。

它不是又一个堆 Agent 数量的花里胡哨的玩具，是一个能自我净化、自我迭代、长期跑稳的集体知识大脑，把Karpathy的Wiki Pattern，直接升级成了可复利的 swarm 版本。

所有玩过多代理 swarm 的人，都踩过同一个致命的坑。
你养了一堆AI Agent，让它们搞研究、写代码、做分析、出内容，各自疯狂输出。
可时间一长，问题就全来了。
它们的产出乱七八糟堆在一起，幻觉和错误信息像病毒一样扩散，一个代理编了假结论，后面的全跟着错，幻觉越滚越大，最后整个系统直接变成了集体扯淡的聊天群。

而这个架构，用四层过滤+一个复利闭环，直接把这个死穴给解决了。

第一步，放开手脚让代理随便干。
不管是内容研究、工程开发还是协调调度，任何角色、任何数量、任何模型的代理，所有输出都会被自动捕获，按代理分文件夹归档，零额外成本，全流程自动化。

第二步，编译器自动做结构化整理。
每隔几小时，系统会自动把零散、杂乱的原始输出，整理成分领域的结构化Wiki文章，自动生成目录、反向链接和完整索引，像一个不知疲倦的机器人图书管理员，把混乱的信息梳理得井井有条。

第三步，也是最核心的一招，Hermes独立审查官把关。
这一步直接掐断了幻觉扩散的源头。
Hermes作为完全独立的审核者，看不到文章的生成过程，没有任何上下文偏见，只做两件事：判断内容是否准确，判断它是否值得放进永久知识库。
通过审核的内容，才会进入live知识库，成为整个系统的“大脑”；没通过的，就留在草稿区自然淘汰。

第四步，给每个代理定制专属知识简报。
每个代理启动工作前，都不是空白大脑。
系统会自动生成对应角色的专属简报，筛选出最相关、最新的知识库内容，控制在2000字以内，让代理在开工前，就已经知道整个swarm沉淀下来的所有有效知识。

整个流程跑下来，就形成了一个完美的正向复利循环。
代理读了精准简报，产出质量更高；高质量的内容经过审核，让知识库更丰富；更丰富的知识库，又能生成更精准的简报。
越跑越聪明，知识像滚雪球一样持续复利，真正实现了复合智能。

它最厉害的地方，从来不是堆了多少个代理，而是用「生产者与审查者完全分离」的经典设计，从根源上解决了多代理系统的幻觉滚雪球问题。
它让10个各自为战的小聪明，变成了一个有纪律、会自我净化、能持续进化的集体大脑。

如果你也在搭自己的agent swarm，这个架构值得直接抄作业，哪怕先把Hermes独立审查+自动简报这两招用起来，效果都会天差地别。

---

**作者** Luyu Zhang（@goocarlos）  
**貼文連結** https://x.com/goocarlos/status/2040335470127992947  

**正文**

我经常需要在做产品的过程中，快速索引各种框架、方法论和思维工具。

设计思维、JTBD、Kano 模型、精益画布、北极星指标、AARRR……

这些框架你可能都听过，但下次要用的时候，你还是会打开 Google 或者 Claude 从头搜。

我也一样。所以我顺手做了 http://pmframe.works——100 个产品思维框架的索引站。每个框架都有：
· 可视化结构图
· 真实案例拆解
· 可下载的 Skill

站在巨人的肩膀上，少走弯路。
免费开放，拿去用。

---

**作者** Vadim（@VadimStrizheus）  
**貼文連結** https://x.com/VadimStrizheus/status/2040687605600141619  

**正文**

pov: you have been using Claude Code for 3 months and just discovered skill graphs. 

Give this to your agent. 

You’ll thank me later. 👇

---

**作者** Jiayuan (JY) Zhang（@jiayuan_jy）  
**貼文連結** https://x.com/jiayuan_jy/status/2040747872627650720  

**正文**

Multica 把团队所有人和 Agent 的 context 共享在同一个 Workspace 里——这件事的复利效应比想象中大得多。

今天换了一台新 Mac，装好 Claude Code + Multica CLI，创建一个新 Agent，直接就能接上之前没做完的工作。

每一次协作——每一个 issue、每一段讨论、每一次 code review——都在持续沉淀成团队共享的 context。用得越久，Agent 对你的项目理解越深，新成员（包括新设备）上手越快。

Context 不是消耗品，是资产。Multica 让它自动积累、持续增值。

btw， 图中的 Lambda & Emacs 是家里的两只猫，已经上班一段时间了 😄

欢迎体验：http://multica.ai

---

**作者** Joey Lee（@JoyLi629）  
**貼文連結** https://x.com/JoyLi629/status/2040682055801937969  

**正文**

nexu 是一个可以一键安装的 OpenClaw 桌面客户端，让你在本地用 AI 操控一切。GitHub：https://github.com/nexu-io/nexu ，觉得有用的话帮忙点个 Star 支持一下 🌟
4 月 3 号，Andrej Karpathy 发了一条推，聊他最近怎么用

---

**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2040239119918362956  

**正文**

Memory 和 Agent Harness 是什么关系？

是随意“插拔”的外部插件？ @sarahwooders 认为：记忆管理是 Agent Harness 的核心职责和内在能力。

为什么“插入记忆”这个想法有问题？
1. RAG ≠ Memory
当前很多开发者把 RAG 当作“记忆”的代名词，认为只要能从过去对话或文档中检索信息，就实现了记忆。但 Sarah 指出：检索只是记忆中很小的一部分，甚至很多时候，用简单的 grep 就足以达到类似效果。把 RAG 品牌化为“记忆”，导致 MemGPT 经常被误解为一个“可插拔的记忆工具”。
2. MemGPT / Letta 的本质是 Stateful Agent Harness
MemGPT 从一开始就不是一个单纯的记忆插件，而是一个有状态的 Agent Harness——在“Agent harness”这个术语流行之前就已经存在。Agent 的记忆能力，来自于框架本身暴露给模型的工具，这些工具允许 Agent 主动改写提示词、管理外部状态，再加上框架自身的上下文管理机制共同产生。记忆不是一个独立的模块，而是从整个系统架构中“涌现”出来的。

Agent Harness 在记忆管理中的“隐形决策”
Sarah 强调，Agent harness 做了大量外部插件无法控制的关键决策，这些决策直接决定了“记忆”在实际运行中的表现。她列举了几个典型问题：
· 如何将 AGENTS.md 或 CLAUDE.md 这类文件加载到上下文中？
· Agent 的技能元数据是通过系统提示还是系统消息呈现？
· Agent 是否允许修改自己的系统指令？
· 在上下文压缩时，什么信息会被保留，什么会被丢弃？
· 历史交互是否被存储并可查询？
· 内存元数据如何呈现给 Agent？
· 当前工作目录如何表示？暴露多少文件系统信息？

不同 harness 对这些问题的答案差异巨大，而用户往往看不到这些隐藏在系统消息中的“上下文提示”。这些设计选择，共同构成了 Agent 的实际记忆行为。

实际案例与 Letta 的实践
· Claude Code 的内存系统：Sarah 提到，从 Claude Code 泄露的源代码分析中，可以看到它内置了一个多层级的内存层次结构，这正是直接嵌入在 harness 中的设计。
· Letta Code：Letta 进一步推进了“memory-first”的理念。它将 Agent 记忆投射到一个由 Git 备份的文件系统上，支持后台内存子 Agent 并发修改。这些子 Agent 专门负责提示重写和主动内存管理。
· Context Constitution：Letta 最近发布的「Context Constitution」文件，总结了 Agent 在上下文管理中遵循的共同原则。这些原则与 harness 的设计紧密耦合，不可分割。

---

**作者** Guri Singh（@heygurisingh）  
**貼文連結** https://x.com/heygurisingh/status/2040464288264139002  

**正文**

🚨Breaking: Someone open sourced a knowledge graph engine for your codebase and it's terrifying how good it is.

It's called GitNexus. And it's not a documentation tool.

It's a full code intelligence layer that maps every dependency, call chain, and execution flow in your repo -- then plugs directly into Claude Code, Cursor, and Windsurf via MCP.

Here's what this thing does autonomously:

→ Indexes your entire codebase into a graph with Tree-sitter AST parsing
→ Maps every function call, import, class inheritance, and interface
→ Groups related code into functional clusters with cohesion scores
→ Traces execution flows from entry points through full call chains
→ Runs blast radius analysis before you change a single line
→ Detects which processes break when you touch a specific function
→ Renames symbols across 5+ files in one coordinated operation
→ Generates a full codebase wiki from the knowledge graph automatically

Here's the wildest part:

Your AI agent edits UserService.validate().

It doesn't know 47 functions depend on its return type.

Breaking changes ship.

GitNexus pre-computes the entire dependency structure at index time -- so when Claude Code asks "what depends on this?", it gets a complete answer in 1 query instead of 10.

Smaller models get full architectural clarity. Even GPT-4o-mini stops breaking call chains.

One command to set it up:
`npx gitnexus analyze`

That's it. MCP registers automatically. Claude Code hooks install themselves.

Your AI agent has been coding blind. This fixes that.

9.4K GitHub stars. 1.2K forks. Already trending.

100% Open Source.

(Link in the comments)

---

**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2040659186070040584  

**正文**

原文：Components of A Coding Agent https://magazine.sebastianraschka.com/p/components-of-a-coding-agent 
作者：Sebastian Raschka, 博士
编程智能体如何在实践中利用工具、记忆和代码仓库上下文，让大语言模型发挥更大威力

---

**作者** Žiga Drev（@DrevZiga）  
**貼文連結** https://x.com/DrevZiga/status/2040684786604294227  

**正文**

Context graphs will be to the 2030s what databases were to the 2000s.

---

**作者** 老张来了（@laozhang2579）  
**貼文連結** https://x.com/laozhang2579/status/2040732229035585615  

**正文**

你以为把文档扔给 AI 让它检索就叫知识管理？Karpathy 说，那叫每次从零开始。
几个小时前，Karpathy 在 GitHub 上发了一篇 Gist，提出了一个完全不同的思路：不是让 AI 被动检索，而是让 AI 主动帮你建一个

---

**作者** 阿绎 AYi（@AYi_AInotes）  
**貼文連結** https://x.com/AYi_AInotes/status/2040635298179428371  

**正文**

amazing(⊙o⊙)
karpathy 的Wiki Pattern，被FarzaTV 老哥落地成了真正可用的AI第二大脑个人知识库。

他把过去数年2500条日记、备忘录、iMessage对话，全部喂给LLM，自动生成417篇结构化个人维基——Farzapedia。

内容覆盖朋友、创业、研究、书籍、人生片段，篇篇带反向链接，完整复刻维基结构。

最颠覆的是：
它不是给人读的，是专为AI Agent设计。
纯Markdown文件+目录索引，Agent无需RAG，直接像人一样遍历文件系统检索信息。

演示里，一句/wiki-query "whats my biggest inspiration?"
Claude从目录出发，逐层查阅、关联、推理，最终得出答案：《火影忍者》，并附上完整人生脉络解释。

新增内容，LLM自动更新/新建词条，像永不疲惫的超级图书管理员；
隐私完全本地留存，比传统RAG好用数倍。

这不是概念，是可直接复用的系统：
把一生碎片化记录，变成Agent能深度理解、精准调用的结构化第二大脑。

目前已上线，开源wiki skill可直接上手。
@FarzaTV Really awesome, bro. Thanks for open-sourcing this!
#AI #个人知识库 #Agent

---

**作者** 鸭哥（@grapeot）  
**貼文連結** https://x.com/grapeot/status/2040810955647648153  

**正文**

红杉最近两篇文章，一个讲卖结果，一个讲去层级。我觉得它们共同漏掉的是中间那层组织接口：评估谁做、权限怎么给、出了事谁负责。从 copilot 到 autopilot，本质上不是能力升级，而是责任迁移。 https://yage.ai/share/sequoia-autopilot-organizational-interface-20260405.html?utm_source=twitter&utm_medium=thread&utm_campaign=sequoia-autopilot-organizational-interface-20260405

---

**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2040662772128862697  

**正文**

🚀 Legora 只用了 18 个月就做到 1 亿美元 ARR。

速度比 OpenAI、Anthropic、Cursor、Wiz 都更快。

更关键的是，它做的还不是热门通用 AI，而是很多人以为会很慢的法律软件赛道。

这件事值得细看👇 

---

**作者** Karan🧋（@kmeanskaran）  
**貼文連結** https://x.com/kmeanskaran/status/2040659634550436346  

**正文**

You don't need random papers, just learn these concepts sequentially to kickstart your LLM engineer journey.

Here’s what actually matters if you’re an engineer:
- Tokenization and embeddings
- Attention and transformer blocks
- Training and fine tuning
- LoRA and QLoRA
- DPO and alignment
- Quantization
- KV cache and inference systems
- FlashAttention and PagedAttention

Not theory.
Systems.

I wrote a complete guide covering everything step by step. If you want to build with LLMs, not just study them, this is for you.

Also breaking down inference and deployment at scale in upcoming posts on hands-on level.

---

**作者** Harrison Chase（@hwchase17）  
**貼文連結** https://x.com/hwchase17/status/2040475736314880268  

**正文**

learning at the context layer is basically memory

there's a few different ways to do this - have the agent update it's memory as it's running (in the hot path) or do it in the background 

---

**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2040428943312871511  

**正文**

POV: April 2026 

---

**作者** Ronin（@DeRonin_）  
**貼文連結** https://x.com/DeRonin_/status/2040348839257747645  

**正文**

Do you understand what just got open sourced???

an agent that improves other agents. autonomously. NO human in the loop

[ literally how it helps to me ]:

- tuning prompts (i was spending hours daily to do it manually)
- testing tools (lol, i shouldn't learn each tool 1-3 hrs anymore)
- reading error logs (they created a fobia to test anything in my product :<(
- tweaking orchestration for every single use case

AutoAgent just did all of that, by itself, in 24 hours

[ what it actually does ]:

> spins up thousands of sandboxes
> tests different prompts, tools, orchestration setups
> reads its own failure traces
> fixes itself
> repeats until it beats every human-engineered score

every other entry on those benchmarks was hand-built by real engineers..

this one built itself

[ btw the part which totally broke my brain ]:

it's like hiring yourself to review your own work

it's logical that you already know how you think, so you catch mistakes 10x faster

that's exactly what happens when both agents run on the same model. same brain, different job

+ on top of all that excitement, it fixes at senior engineer level (BOOOOOM)

[ and behaviors nobody programmed ]:

- started writing its own unit tests
- built verification loops to check its own work
- created subagents when tasks got too complex

nobody told it to do any of this...

100% OPEN SOURCE, FREE

I setupped and I am so fcking satisfied

P.S. Sorry if somewhere my reaction was too "forcing" to setup it, just wanted to mark by BOLD what's the treasure

you can skip it, it's your deal ❤️

---

**作者** 在悉尼和稀泥（@JamesAI）  
**貼文連結** https://x.com/JamesAI/status/2040461236597580070  

**正文**

纽约时报上周炸出一个故事。
41 岁的 Matthew Gallagher，在洛杉矶家里，拿 2 万美金，用 ChatGPT 和 Claude 写代码，14 个月做出一家年营收 18 亿美元的公司。员工？就他和他兄弟两个人。
数据我直接列一下。

---

**作者** Aaron Levie（@levie）  
**貼文連結** https://x.com/levie/status/2040650799550722243  

**正文**

One of the core things we’re going to have to contend with in AI is that even the most advanced models in the word can’t have all the relevant knowledge needed to be useful, because everyone has different use-cases and ways they’ve designed their workflows. 

Perhaps most importantly, as you get into the enterprise, everyone has entirely different access levels to corporate knowledge and information. Continual learning at the model layer, even at a single enterprise level, is near impossible because every user knows and has access to something different than another user.  

This isn’t like coding where by and large most developers can access all the relevant stuff to their job. On a single banking team, bankers have entirely different sets of documents they’re ever allowed to see. Sanitizing this is hard and having the model keep secrets is impossible.

This is why the context layer is going to always be the core part of the AI stack for applied use cases to turn general models turn into useful agents. Can’t fight the physics on this one.

---

**作者** Eric Lay（@itsericlay）  
**貼文連結** https://x.com/itsericlay/status/2040544845496992248  

**正文**

come work at @VirioAI with @jjeremyro 

---

**作者** 鸭哥（@grapeot）  
**貼文連結** https://x.com/grapeot/status/2040454099985117253  

**正文**

1/

做 AI Agent 的同学，你们监控过自己的 prompt cache hit rate 吗？

最近读到一个反直觉的 PR：对话历史需要压缩时，优先删最新的 tool results，而不是最旧的。听起来荒谬，但背后的逻辑很硬：早期内容构成缓存前缀，删了等于摧毁缓存基础。

---

**作者** 阿绎 AYi（@AYi_AInotes）  
**貼文連結** https://x.com/AYi_AInotes/status/2040669222838341969  

**正文**

这是人类历史上最好的创业时机（the best time in history to build a startup）”，而且这个黄金窗口只剩 12-24 个月。

以上是 The Startup Ideas Podcast主持人 Greg Isenberg最近一起播客的核心观点，对大多数普通人来说确实是少有的搞钱或者改命机会。

四大核心原因：
1. 构建成本几乎为零（Build cost is basically zero）  
   现在用 AI 工具，开发产品、写代码、部署的成本极低，甚至接近零。

2. AI Agents 在替你干活（Agents are doing the work）  
   AI 代理人可以自动处理大量工作，让 solo founder（独行创业者）拥有以前团队才有的执行力。

3. 受众（audiences）目前被严重低估/低价（Audiences are underpriced）  
   拥有一个小而精准的受众群，价值远高于过去。

4. 最好的利基市场（niches）还完全敞开（The best niches are wide open）  
   很多垂直、小众但高价值的市场还没有被大公司或激烈竞争占据。

你真正需要的东西只有4样：
- 一个好 idea
- 一台笔记本电脑
- Claude（用它来写代码、生成产品）
- 一个100~5000人的精准利基受众（niche audience）

用这些能打造什么？
- 一家 24/7 自动运行*的生意
- 95% 高利润率
- 零员工（纯 solopreneur / 一人公司）

主持人反复强调：**每一天都很重要（Every day matters）  
现在不行动，等竞争者醒悟、工具更普及、利基被抢占后，机会就会大幅缩小。

---

**作者** Ramnandan Krishnamurthy（@ramkris）  
**貼文連結** https://x.com/ramkris/status/2040552106286072108  

**正文**

Banger article 🧨

👀 “A finance product built around "help the CFO close the books faster" and a finance product built around "make the month-end close not require a human" are not the same product. They are not the same company. You cannot usually get from the first to the second by iterating. You have to start with the second in mind.”

---

**作者** Insecure Agents Podcast（@insecureagents）  
**貼文連結** https://x.com/insecureagents/status/2040558232029299012  

**正文**

Jaya predicts "a new infrastructure layer will emerge: the picks and shovels for constructing, securing, and querying context graphs at enterprise scale”

@akoratana and @vtahowe talk about the identity infrastructure that's emerging as one of these shovels 

---

**作者** Jordan Edwards（@JordanEdwards7）  
**貼文連結** https://x.com/JordanEdwards7/status/2040473336338059422  

**正文**

The people behind the build. Starting with one named Bo.
The Forward Deployed CEO concept has gotten a lot of attention lately. What has not gotten enough attention are the people at Palantir who made

---

**作者** Noisy（@noisyb0y1）  
**貼文連結** https://x.com/noisyb0y1/status/2040159662453276879  

**正文**

Open-source engine runs 500 AI agents with different views on one news story

MiroShark - open-source swarm intelligence engine.

You drop in any document or news story even a market and it creates hundreds of AI agents with unique personalities.

Each agent has its own views, emotions, reaction speed and level of influence on others.

Then they're launched into a simulated social network - and start posting, replying, arguing, changing their minds. Hour by hour. 

> They work 24/7 in real time.

At the core - a Neo4j knowledge graph with personal memory for each agent.

What you need to run it:
- Neo4j (knowledge graph + agent memory)
- LLM (Ollama locally or any cloud API)
- Embeddings (nomic-embed-text or OpenAI)
- CAMEL-AI engine (agents live, post, argue)
- ReportAgent (analyzes everything + generates a report)

One docker compose up -d and you have a full simulation at localhost:3000.

Any student with an old laptop can do this.

Want cloud - connect OpenRouter, OpenAI or even Claude Code.

---

**作者** Bryan Onel（@BryanOnel86）  
**貼文連結** https://x.com/BryanOnel86/status/2040174710659362982  

**正文**

Excited to announce an exclusive partnership with @simdotai to launch the first AI-native GRC workflow solution.

Shoutout to @emkara and @typingwala for making this happen!

---

**作者** Harrison Chase（@hwchase17）  
**貼文連結** https://x.com/hwchase17/status/2040471961206214864  

**正文**

meta harness is a great paper from @yoonholeee that came out earlier this week and is a great example of learning at the harness layer 

---

**作者** Nick Spisak（@NickSpisak_）  
**貼文連結** https://x.com/NickSpisak_/status/2040448463540830705  

**正文**

@karpathy  dropped a post describing how he uses AI to build personal knowledge bases.
The idea is simple: instead of keeping notes scattered across apps, you dump everything into one folder. Then you

---

**作者** 阿绎 AYi（@AYi_AInotes）  
**貼文連結** https://x.com/AYi_AInotes/status/2040350984732659975  

**正文**

卧槽，太劲爆了， 2万美元启动1年干出4亿美元营收的AI一人独角兽，

被 NYT吹爆的AI一人独角兽创业神话，4亿美元营收的背后，全是踩满监管红线的灰色操作😂

这个41岁男人用2万美元+AI工具，1年干出4亿美元营收、6500万美元净利润的故事，一半是AI效率奇迹，一半是踩满监管红线的灰色操作。

先讲100%属实的硬核事实，全部经过权威媒体核验：
故事的主角Medvi公司和创始人Matthew Gallagher真实存在。

41岁的他在2024年9月，靠着2万美元启动金，用ChatGPT、Claude、Midjourney等AI工具快速上线项目，主打复合GLP-1减肥药，也就是司美格鲁肽、替尔泊肽的复合调配版本。
整个公司的全职员工，只有他和弟弟两个人，其余全链路的医生、处方、药房、物流服务，全部靠白标平台打包提供。

首年完整财年的业绩，夸张到近乎离谱，却完全真实。
2025年Medvi拿下4.01亿美元营收，服务25万客户，净利润率16.2%，纯利润约6500万美元，2026年的预计营收直接冲到18亿美元。
这些财务数据，都经过了NYT和Forbes的双重查验，没有水分。

而NYT通篇没提的，是这套神话背后，踩满平台规则红线的灰色营销打法。
帖子里的两张配图全部真实可查，一张是创始人本人照片，另一张是Facebook Ads Library的实时截图。
截图里能看到大量顶着「http://Dr.XXX」名号的账号，正在密集投放Medvi的赞助广告，主打「无医生上门」「快速拿药」的核心卖点，截至目前这些账号依然在活跃投放。

这些看似专业的医生账号，大多是虚构的人设，靠着专业身份制造用户信任感，做精准流量收割，也就是帖主提到的800+假医生账号矩阵。
这也是健康类目里最典型的黑灰产广告打法。

更关键的是，这套玩法早已踩中了监管和法律的多重红线，实锤黑料全部可查：
2026年2月20日，FDA就向Medvi发出正式警告信，直指其网站虚假宣传复合药「与Wegovy/Ozempic/Mounjaro成分相同」，涉嫌误导性标示，同期收到同类警告的远程医疗公司，还有30多家。
2025年就有媒体曝光，Medvi在广告里大量使用AI换脸生成的患者用药前后对比照，用deepfake内容虚构产品效果。
合作的白标平台OpenLoop Health在2026年1月遭遇数据泄露，160万患者的姓名、地址、医疗信息疑似外泄，目前已引发多起集体诉讼，Medvi也被一同列入被告名单。

一句话说透整件事的完整全貌：
NYT笔下的「AI一人公司造富神话」是真的，帖主挖出的营销黑幕、监管风险也是真的，两者拼在一起，才是这个故事的全部真相。
这本质上是一场用AI+白标平台+大规模虚假人设广告，快速收割GLP-1红利的灰色创业。
哪怕营收爆炸式增长，也始终踩在FDA监管红线、平台政策底线和法律风险的边缘，属于看似合法、实则风险拉满的创业模式。

---

**作者** vas（@vasuman）  
**貼文連結** https://x.com/vasuman/status/2040295331796332650  

**正文**

How many lines of code do you think it takes to clone Delve? Somewhere in SF Garry Tan has 8 concurrent claude code instances up. He's on the case, give him 3 days. Matter fact give him 2 days because GStack gives him a head start.

---

**作者** Moe（@katibmoe）  
**貼文連結** https://x.com/katibmoe/status/2040272048954777943  

**正文**

🔥

---

**作者** George Sivulka（@gsivulka）  
**貼文連結** https://x.com/gsivulka/status/2040097100617167191  

**正文**

Introducing the "Forward-Deployed Banker"

Come work at the intersection of finance and AI… we’re hiring! 

---

**作者** Bill The Investor（@billtheinvestor）  
**貼文連結** https://x.com/billtheinvestor/status/2040118074385608797  

**正文**

我靠，这Faceless YouTube频道光是播放量就40亿，赚了28万美元。结果我直接裁了那个4000块/月的写稿团队，现在Claude Code搞定创意和脚本，只要20块/月。系统是这样运作的： 

---

**作者** 宝玉（@dotey）  
**貼文連結** https://x.com/dotey/status/2040157640442229153  

**正文**

文档平台 Mintlify 发了一篇工程博客，讲了一件挺有意思的事：他们给自家 AI 文档助手造了一套假的文件系统，叫 ChromaFs，让 AI 以为自己在用 grep、cat、ls 这些命令浏览文件，实际上每个命令都被拦截、翻译成了数据库查询。

效果很直接：会话启动时间从原来沙箱方案的 46 秒降到 100 毫秒，每次对话的边际计算成本几乎为零。

Mintlify 之前的方案是标准的 RAG 流程：把文档切块、向量化、存进 Chroma 数据库，用户提问时检索最相关的片段喂给大模型。问题是，如果答案分散在好几个页面里，或者用户要的是某段精确的代码语法，向量检索经常找不对。

他们想让 AI 像开发者翻代码一样翻文档，而不是靠语义相似度碰运气。

核心思路是：AI 不需要真的操作系统，只需要一个足够逼真的幻觉。

ChromaFs 基于 Vercel Labs 的开源项目 just-bash（一个用 TypeScript 重写的 bash 子集）构建。just-bash 提供了可插拔的文件系统接口，负责解析命令和管道逻辑，ChromaFs 则把所有底层文件操作翻译成 Chroma 数据库查询。每个文档页面变成一个"文件"，每个章节变成一个"目录"，AI 就可以用 grep 搜精确字符串、用 cat 读整页内容、用 find 遍历结构。

之前用真沙箱的方案（给每个用户起一个微型虚拟机），按 Mintlify 月均 85 万次对话的量算，一年光计算成本就要 7 万美元以上。ChromaFs 复用了已有的数据库基础设施，这笔钱省了。

grep 是最难虚拟化的命令。如果真让它逐文件扫描，走网络 IO 会很慢。ChromaFs 的做法是先把 grep 的参数解析出来，用 Chroma 的元数据查询做粗筛，找出可能命中的文件批量预取到缓存里，再让 just-bash 在内存中做精确匹配。

权限控制也很优雅：初始化时根据用户身份裁剪文件树，没权限的路径直接从树里删掉，AI 连路径都看不到，不存在越权风险。

所有写操作一律返回"只读文件系统"错误，AI 能随便看但改不了任何东西，整个系统无状态，不用担心清理和数据污染。

这篇文章在 Hacker News 上引发了一个有意思的讨论。好几位开发者指出，大家不知不觉中把 RAG（检索增强生成）等同于了向量搜索，但 RAG 里的 R 是 Retrieval（检索），本来可以是任何方式：全文搜索、SQL 查询、甚至翻电话簿。把 RAG 绑死在向量数据库上，是早期技术路径的惯性。

有人解释了这种惯性的由来：RAG 概念流行的时候，大模型还不太会用工具，多轮搜索和纠错能力也差，向量检索是当时最省事的方案。现在模型的工具调用和推理能力上来了，让 AI 自己决定用什么方式找信息，反而比预设一条检索管道更灵活。

也有人提出了务实的质疑：Mintlify 的场景是结构化的技术文档，天然适合文件系统隐喻，但如果是组织内部那种乱七八糟、没有层级结构的知识库，这套方案未必好使。

这个方向和 Claude Code 的做法有相通之处：与其把所有信息预检索好喂给模型，不如给模型一套探索工具，让它自己决定看什么、怎么找。对于正在搭建 AI 文档助手或内部知识库的开发者来说，Mintlify 的这套方案提供了一个向量检索之外的选项，尤其适合文档结构清晰、对精确匹配要求高的场景。

---

**作者** Prismor（@prismor_dev）  
**貼文連結** https://x.com/prismor_dev/status/2040182252597039562  

**正文**

@ycombinator Pretty awesome! We've open sourced our tools for EU CRA compliance, this is the biggest software supply chain mandate in a decade. Happy to follow-up

https://www.prismor.dev/cra

---

**作者** Y Combinator（@ycombinator）  
**貼文連結** https://x.com/ycombinator/status/2040148401426436470  

**正文**

http://Complir.io is building AI infrastructure that automates product compliance for global retailers.

Managing compliance across markets means different regulations per country, fragmented documentation, and constant changes. Most teams still run it on spreadsheets. Every product launch becomes a fire drill.

Complir maps products to regulatory requirements, generates required documentation automatically, and keeps everything current when regulations or products change. Today they manage 100k+ products across Europe and are growing ~45% MoM.

---

**作者** Gauri Gupta（@gauri__gupta）  
**貼文連結** https://x.com/gauri__gupta/status/2040251170099524025  

**正文**

Connect your agent and let it cook over the weekend. We just open-sourced our auto-harness — a self-improving loop that finds your agent's failures, turns them into evals, and fixes them. All

---

**作者** 歸藏(guizang.ai)（@op7418）  
**貼文連結** https://x.com/op7418/status/2040245390814085270  

**正文**

早上起来时间线上都在骂。

Anthropic 宣布说，不能用 Claude 账户中的额度使用 OpenClaw 这种三方的产品了。

他们会送你一个月的额度进行过渡，之后就得购买单独额度。

关于 Claude Code 的额度消耗异常问题，昨天也回复了，意思是不存在问题。

真太傻逼了，当大家傻子。

与此同时，Codex 不语，只是一味地重置额度。

---

**作者** Jaya Gupta（@JayaGup10）  
**貼文連結** https://x.com/JayaGup10/status/2040179441633259582  

**正文**

Thank you Forbes 

---

**作者** Polo1.4 贱🕊️（@xiaojianjian567）  
**貼文連結** https://x.com/xiaojianjian567/status/2039858723406148058  

**正文**

我找到了《埃隆之书》的中文版下载地址
喜欢@elonmusk的可以去下载
免费，这很马斯克精神 
中文版： https://file.lvwzhen.com/The-Book-of-Elon-Free-epub.zh-CN.epub 

---

**作者** weisser（@julianweisser）  
**貼文連結** https://x.com/julianweisser/status/2040110380928868513  

**正文**

Many founders choose the factory, and they choose it for understandable reasons: safety in numbers, a clear set of instructions, the comfort of a recognizable path. But a factory has one purpose: to

---

**作者** Leonard Tang（@leonardtang_）  
**貼文連結** https://x.com/leonardtang_/status/2040122646197612557  

**正文**

Towards Semantic Observability
Traditional observability works because the set of behaviors of failures was known ex ante. Engineers know what to look for in advance:
A request failed.
Latency

---

**作者** Emmett Chen-Ran（@doubleemt）  
**貼文連結** https://x.com/doubleemt/status/2040112561161707904  

**正文**

Word on the street is SaaS is dead, and all app-layer software companies are moving up the stack to provide services. So, as a company venturing forth to carve its path deep into uncharted territory,

---

**作者** Idea Browser（@ideabrowser）  
**貼文連結** https://x.com/ideabrowser/status/2040051868131266923  

**正文**

I ran an experiment, I wanted spend $1,000 on apps and tools this week to support builders and become a customer.
​
573 replies...I bought some... and looked at a TON of businesses and found...

Your

---

**作者** elvis（@omarsar0）  
**貼文連結** https://x.com/omarsar0/status/2040099881008652634  

**正文**

Diagram of the LLM Knowledge Base system.

Feed this to your favorite agent and get your own LLM knowledge base going. 

---

**作者** Hila Shmuel（@HilaShmuel）  
**貼文連結** https://x.com/HilaShmuel/status/2039915543260500284  

**正文**

Meet Cabinet: Paper Clip + KB. for quite some time I've been thinking how LLMs are missing the knowledge base - where I can dump CSVs, PDFs, and most important - inline web app. running on Claude Code with agents with heartbeats and jobs https://runcabinet.com 

---

**作者** Harrison Chase（@hwchase17）  
**貼文連結** https://x.com/hwchase17/status/2039749451259195428  

**正文**

feedback loops for agents are all the rage - here's how @vishsuresh_ implemented one for our GTM agent!

great blog on it below

---

**作者** Yann（@yanndine）  
**貼文連結** https://x.com/yanndine/status/2039730005081460815  

**正文**

A two-person GTM team at a Series B SaaS company closed $2.4M in pipeline in one quarter.

No SDRs. No demand gen agency. No paid ads.

Signal-based outreach. Intent scoring. AI-sequenced follow-up. Automated reporting.

Two GTM engineers running the whole motion - for one quarter.

I pulled it apart.

Compared it to every system we've built across the GTM teams we've worked with.

Then asked myself one question:

If I had to reverse engineer this from scratch - what would it actually look like?

Turns out the architecture isn't that complicated.

I mapped the whole thing into a step-by-step playbook you can upload directly to any LLM.

It walks you through building your own version from GTM strategy to fully AI-powered execution.

Comment "GTM" and I'll send it over.

---

**作者** Wayne Zhang（@wayne_zhang0）  
**貼文連結** https://x.com/wayne_zhang0/status/2039828708803195153  

**正文**

过去一个季度，Coding Agent 领域出现了一条清晰的演进脉络：Claude Code 和 CodeX 定义了底座能力，社区项目（如 oh-my-opencode）在此基础上引入 Multi-Agent

---

**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2039869709747736884  

**正文**

AutoHarness [Aha]：面向 AI Agent 的轻量级治理框架

来自 AIMING Lab，团队认为：Agent = Model + Harness
模型负责推理，框架负责其余一切（上下文管理、工具治理、成本控制、可观测性、会话持久化等）

技术架构 - 三层治理模式
· Core：6步，轻量级治理
· Standard：8步，生产级 Agent
· Enhanced⚠️：14步，最大治理强度

其中 Enhanced 模式的架构决策部分参考了 Claude Code 源代码，上下文工程实践参考了 Codex 开源代码。

关键特性 - 开箱即用的治理能力
· 风险模式匹配：内置危险操作、密钥暴露、路径遍历等检测
· Token 预算管理：自动截断防止上下文爆炸
· 单次调用成本归因：模型感知的定价追踪
· 分层验证：输入护栏 → 执行 → 输出护栏
· JSONL 审计日志：完整溯源，满足合规要求
· 多智能体配置：基于角色的差异化治理

开源地址：https://github.com/aiming-lab/AutoHarness

---

**作者** Annie 所长（@web3annie）  
**貼文連結** https://x.com/web3annie/status/2040003050958643443  

**正文**

这位帅气法国小哥靠 5 个 AI 小产品，月赚 70万刀

实现躺赢，简直是人生赢家

他是怎么做的？

核心赚钱模型：SaaS订阅

他所有的产品本质都是：

按月收费（$10 / $29 / $99 这种）

解决用户的痛点，用户持续用，就持续付钱

• Rabbit AI → AI 做视频：40万刀/月
• Outrank → SEO搞流量：20万刀/月
• Super X → X涨粉：1.3万刀/月
• Postsyncer → 可以一键发 10 个平台：15刀/月（两杯星巴克🧋😂）
• feather →：1万刀/月

👉 总共 70万刀+/月

---

**作者** The Startup Ideas Podcast (SIP) 🧃（@startupideaspod）  
**貼文連結** https://x.com/startupideaspod/status/2039871732358742423  

**正文**

The era of the one-person $1B company is here.

This is how you structure your team of AI agents:

- Engineering: code, testing, DevOps 
- Design: UI/UX, brand assets 
- Marketing: content, SEO, social
- Sales: lead gen, outreach, demos 
- Support: tickets, docs
- Data: metrics, analysis

1 founder. 
6 agent departments. 
0 employees.

Slow. Then all at once.

---

**作者** Tracy（@CTracy0803）  
**貼文連結** https://x.com/CTracy0803/status/2039898683261768054  

**正文**

AI 圈真正的一手信息在哪里？

不在 Twitter 热搜
在 Reddit 的深度讨论里
在 Discord 社区的实时动态里

但这些地方我们根本没时间一个一个盯

而已经有176,000 订阅者的http://latent.space 每天筛选：
Reddit × 12 个版块
Twitter × 500+ 账号
Discord × 24 个频道

上万条信息浓缩成一个信息流到Saymore
每天自动聚合，实时推送

https://saymore.app/zh-CN/thread/62/overview?ref=CTracy0803&sharer_id=3&sharer_username=CTracy0803&share_channel=copy_link

---

**作者** Yanhua（@yanhua1010）  
**貼文連結** https://x.com/yanhua1010/status/2039716848070172686  

**正文**

Y Combinator CEO 开源了他的编程工作流。23 个 AI 角色，完整的 Sprint 流程，真实浏览器测试。3 周，61000 Star。我花了几个小时拆解这个项目，聊聊我看到了什么。
先说这个项目有多离谱
gstack 在 2026 年 3 月

---

**作者** 卡比卡比（@jakevin7）  
**貼文連結** https://x.com/jakevin7/status/2039975808123752492  

**正文**

大家都自诩推特是AI前沿，但是大家的用法很多都还很原始人
前几天大家居然还在讨论worktree的用法，我只能说大家该吃点好的了，该来点真的 AI native。
我们应该把 AI agent 当人，而不是还天天讨论什么worktree，clone这些事情🤣 

---

**作者** Nate Lorenzen（@anatelorenzen）  
**貼文連結** https://x.com/anatelorenzen/status/2039733038054244829  

**正文**

The new King of DTC Twitter - @galligator.

3 ads. 

$1.8 Billion valuation. 

---

**作者** ashu garg（@ashugarg）  
**貼文連結** https://x.com/ashugarg/status/2039834321167761425  

**正文**

The graveyard of enterprise AI pilots is full of products that couldn't clear security and governance.

At our recent CEO and CIO dinners, we heard this repeatedly from @djpersia (@databricks), Rajat Taneja (@Visa), and CIOs from @Zuora, @asana, and @BlackLine.

In many orgs, data can’t simply be sent to a third-party cloud. It often needs to stay within a company’s own environment, whether that’s a private cloud (VPC) or on-prem.

There are also baseline certification requirements: SOC 2, HIPAA, HiTrust, Veracode, BlackDuck. Security reviews alone can take longer than the pilot itself.

Once those boxes are checked, what happens next is less understood.

Large companies now have hundreds of agents running across the org, many of them built by employees without engineering backgrounds. Most are still working out how to maintain visibility into what those agents are doing, if they’re interacting with each other in unintended ways, and whether they’re compromising the company’s underlying data and permissions model.

This is where many deployments break down - and where the next layer of value is getting built.

@arizeai (a FC portco) has seen product usage go up 10x in the last quarter alone: a sign of how urgently enterprises need observability and evals.

---

**作者** Nick Khami（@skeptrune）  
**貼文連結** https://x.com/skeptrune/status/2039767373083996621  

**正文**

if you're doing context engineering, literally just follow this guide and you'll be fine

---

**作者** Garry Tan（@garrytan）  
**貼文連結** https://x.com/garrytan/status/2039938219257794857  

**正文**

Decision traces are a big deal and now possible with 1M token context

*sneak peek: one of my projects is launching soon and will be focused on decision traces in agentic engineering

---

**作者** Wayne Zhang（@wayne_zhang0）  
**貼文連結** https://x.com/wayne_zhang0/status/2039809144254058691  

**正文**

目前看到的写 harness engineering 写得最好的文章，同一个名词所描述内容的深度区别，非常大。

https://yage.ai/share/harness-engineering-scalability-20260330.html

---

**作者** Shruti（@heyshrutimishra）  
**貼文連結** https://x.com/heyshrutimishra/status/2039802540771152005  

**正文**

The next $1T company won't build software.
It'll replace the people using it.
Sequoia just published the framework. Most founders read it and missed the point entirely.
Here's what they actually said

---

**作者** himanshu（@himanshustwts）  
**貼文連結** https://x.com/himanshustwts/status/2039811786602607052  

**正文**

and here is the full architecture of the LLM Knowledge Base system covering every stage from ingest to future explorations. 

---

**作者** Kevin Gu（@kevingu）  
**貼文連結** https://x.com/kevingu/status/2039843234760073341  

**正文**

today we're releasing AutoAgent, an open source library for autonomously improving an agent on any domain.
AutoAgent hit both the #1 on SpreadsheetBench (96.5%) and the #1 GPT-5 score on TerminalBench

---

**作者** 墓碑科技（@mubeitech）  
**貼文連結** https://x.com/mubeitech/status/2039843680492630339  

**正文**

世界上第一家破十亿美元的“单人公司”出现了。
Sam Altman 刚给《纽约时报》发了封邮件。
说他赢下了和硅谷高管们的赌局。
现在他点名要见见这个单枪匹马的猛人。

照片里这个男人叫 Matthew Gallagher。
今年 41 岁。
拿着两万美金，花了两个月。
在洛杉矶的客厅里拼凑出一家 GLP-1 减肥药医疗公司。
第一年狂揽 4.01 亿美元营收。
今年的流水直指 18 亿。

这要怎么玩？
全靠雇佣不知疲倦的 AI 劳工。
ChatGPT、Claude 和 Grok 联手敲代码。
Midjourney 搞定所有视觉出图。
Runway 直接生成视频广告。
ElevenLabs 接管所有客户的语音通话。
最后用定制的 AI 智能体把整条流水线焊死。

以前打天下需要层层叠叠的草台班子。
现在一个人加一堆 API 就能砸出十亿美元的盘子。
华尔街那套按人头算估值的旧历法彻底失效了。

---

**作者** GREG ISENBERG（@gregisenberg）  
**貼文連結** https://x.com/gregisenberg/status/2039737082176844229  

**正文**

So, he vibe coded a $1B startup? 

Really cool

With the right idea, right tools, right distribution channel, anything is possible in 2026

---

**作者** Agno（@AgnoAgi）  
**貼文連結** https://x.com/AgnoAgi/status/2039755831487479917  

**正文**

A new approval system lets you require human sign-off before agents execute sensitive actions. Using the @approval decorator alongside a HITL primitive (requires_confirmation, requires_user_input, or

---

**作者** Ayush S（@ayushswrites）  
**貼文連結** https://x.com/ayushswrites/status/2039780028922183928  

**正文**

I've never publicly spoken about this, but today feels like the right time to tell this story.  

Today, Central got acqui-hired by Mercury.  

In early 2023, the CEO of an unknown company called "Central Business Applications Inc" reached out to us. 

Said he loved what we were building at Warp, wanted to use our product for his new startup, and even offered to "discuss product strategy."  

We onboarded them. They used Warp for about six months. During that time, they asked us detailed questions about how state tax registrations work, what a registered agent is, how we handle compliance across multiple jurisdictions.  Thought it was odd, but assumed goodwill.  

Then they left. And launched a clone.  Their launch post paraphrased our problem and solution statements from six months earlier. Our launch said "designed for founders, not HR." Theirs said "platform for founders not HR." Our website said "Unlike traditional payroll providers, Warp does tax registrations and compliance work for you automatically." Theirs said "Unlike other platforms, 
Central handles compliance work automatically."  

They never could match the product. But we would update our website copy and a few weeks later, theirs would match.  

I actually think this validates something important: payroll and employee management is a genuinely hard problem. You can study someone's product, copy their positioning, mirror their website. 

But you can't copy years of infrastructure built across thousands of tax agencies, the compliance automation that compounds over time, or a world class engineering team that ships it. 

Over the past couple weeks, some of Central's biggest customers have been switching to Warp. 

If you're on Central wondering what comes next, we'll make the transition seamless.  

Back to building.

---

**作者** Dens Sumesh（@densumesh）  
**貼文連結** https://x.com/densumesh/status/2039781682858061925  

**正文**

“how agents look at you when they see a file system” 

---

**作者** Jaya Gupta（@JayaGup10）  
**貼文連結** https://x.com/JayaGup10/status/2039726900231418293  

**正文**

@jason_lopatecki For sure and the best tooling for that is @arizeai :)!!

---

**作者** Aparna Dhinakaran（@aparnadhinak）  
**貼文連結** https://x.com/aparnadhinak/status/2039724128266334257  

**正文**

Every AI system in production generates two categories of data: conversations, the interactions between agents and customers, between agents and other agents, the reasoning chains that drove every

---

**作者** Jason Lopatecki（@jason_lopatecki）  
**貼文連結** https://x.com/jason_lopatecki/status/2039726059588125022  

**正文**

Amazon didn’t just capture what you bought. It also built the tooling to evaluate whether it made a good recommendation. The evaluation layer is important (and hard). A capture layer alone would give you decision traces, which is just a bigger, more structured pile of data.

---

**作者** Arvind Jain（@jainarvind）  
**貼文連結** https://x.com/jainarvind/status/2039398271135928384  

**正文**

Agentic AI is everywhere right now. But very few teams can explain why their agents behave the way they do, or how to systematically make them better.

People often describe traces as the “codebase” for agents. They show how an agent thinks and what it did at every step. As agents take on more tools, sandboxes, and skills, their paths multiply. That makes them harder to reason about and harder to improve. Static prompts don’t scale when every run looks different.

At @glean, we use traces as part of the learning and memory loop, not just logging. Trace learning lets agents learn from real usage, adapt to edge cases, and get better without model fine-tuning or long instruction sets. The goal isn’t to replay old runs, but to extract the signal that helps the agent make a better decision next time.

In the enterprise, tool strategies are never one-size-fits-all. Each company wires systems together differently, defines its own sources of truth, and has its own rules of engagement. Treating this as generic is both a security risk and a quality problem, because it ignores how work actually gets done. Work is also personal. The systems people touch, the updates they make, and the templates they use all vary.

So we built learning at two levels:
- Enterprise-level strategies for how tools and workflows operate
- User-level preferences for how work actually gets done

Traces give us a way to understand and shape agent decision-making, and to create a feedback loop that compounds over time.

If agentic AI is going to move beyond impressive demos to reliable day-to-day work, this kind of trace-driven learning is essential. It’s one of the ways we’re building self-learning agents that can execute real work, at scale.

---

**作者** Glean（@glean）  
**貼文連結** https://x.com/glean/status/2039746563120226424  

**正文**

MCP gives models access to tools, but it’s the enterprise context layer and skills on top that make those tools reliable, relevant, and actually useful.  

Steve shows how our remote MCP server brings that context into day-to-day work and how skills help models choose the right tools, follow the right workflows, and drive better outcomes. 

He also walks through how Glean uses user activity and memory to suggest new skills you can spin up for yourself.

---

**作者** Gabe Pereyra（@gabepereyra）  
**貼文連結** https://x.com/gabepereyra/status/2039735237165404292  

**正文**

Over the weekend, I agent-pilled my parents. Both of them are retired and in their free time, my dad plays solitaire and my mom contributes to an open source scientific computing library. I had been

---

**作者** Arlan（@arlanr）  
**貼文連結** https://x.com/arlanr/status/2039758320094105627  

**正文**

internally, @nozomioai just solved code hallucination for agents.

this is likely the most useful tool for coding agents that need up-to-date API docs or real-time information from the web.

launching soon. it will be free.

---

**作者** ashu garg（@ashugarg）  
**貼文連結** https://x.com/ashugarg/status/2039745286483128449  

**正文**

Why decision traces will reshape B2B the way behavioral data reshaped B2C
Our latest thinking on context graphs, developed with my partner @JayaGup10.
 
Consumer platforms built one of the most

---

**作者** ashu garg（@ashugarg）  
**貼文連結** https://x.com/ashugarg/status/2039078682267209987  

**正文**

Enterprise AI has a pilot problem.

The gap between a promising pilot and concrete change in how work gets done was one of the central themes of our recent CEO and CIO dinners. We heard from @djpersia of @databricks, Rajat Taneja of @Visa, and CIOs from @Zuora, @asana, and @BlackLine.

As Rajat put it, pilots are almost always too pristine to matter. They run on curated data in controlled environments. Production is much messier, with imperfect data, edge cases, and the full complexity of how a business operates.

The teams seeing the most impact from AI start with use cases that have bounded scope, high-quality data that’s easy to connect to models, a clear outcome, and humans in the loop. They test against production traffic earlier, with the ability to revert when something breaks.

Along with the pilot trap, we got into why most enterprises have no visibility into what their agents are doing, why founders who try to work around the CIO tend to regret it, and why layering AI on top of existing processes only gets you so far - the biggest gains require redesigning how work gets done.

Read the full recap in my latest B2BaCEO: https://lnkd.in/gsqpzhNs

---

**作者** WquGuru🦀（@wquguru）  
**貼文連結** https://x.com/wquguru/status/2039721219390591415  

**正文**

承蒙诸位在Claude Code源码解析的茫茫书海里，偏偏相中了这两本小书——过去24小时，访问量竟一口气冲破14k！流量最猛的几位“老铁”是美国、中国、香港、新加坡、日本、台湾……

我当初动手写这两本书，就在深思这个问题：“在Claude Code和Codex那浩如烟海的源代码里，怎么才能三两下就捞出每天都能用的最佳实践？”于是我没去死抠那些细枝末节，而是绕了个弯，问了个更大的宏观问题——“Claude Code和Codex的Harness，到底是怎么从模型的附属物，一步步长成今天这副模样的？”答案，全在这两本书里。

考虑到大家阅读习惯不一样，我顺手也整了PDF版和网页版。假期马上就到，愿你们从中吸上那么一两分营养。在Claude Mythos模型即将推向大众的当口，这两本书兴许能在眼下这个极速变化的世界里，给你我都找着一点儿踏实的锚点。

Github仓库：https://github.com/wquguru/harness-books

---

**作者** Alfie Carter（@AlfieJCarter）  
**貼文連結** https://x.com/AlfieJCarter/status/2039732676966400375  

**正文**

I put my entire Claude Code setup for GTM engineering into ONE Notion doc

10 modules. No fluff.

- How to install Claude Code and run your first GTM session in under 10 minutes
- How to build a CLAUDE. md that acts as your project brain and never loses context
- How to install GTM skills that chain together and run autonomously
- How to connect your full stack via MCP servers without writing custom wrappers
- How to run parallel agents and subagents across GTM workflows simultaneously
- How to manage context and token usage across long research sessions
- How to choose between Sonnet, Opus, and Haiku based on the task
- How to hook Claude Code into external triggers so workflows run without you
- The exact GTM workflows to build first: signal detection, lead scoring, outreach sequencing
- Full slash command reference for every repeatable GTM task

This is the setup I would have KILLED for before spending months piecing it together from documentation, YouTube tutorials, and scattered GitHub threads.

Like + comment "BIBLE" and I'll send it over

(must be connected for priority access)

---

**作者** ratsxp（@Pxstar_）  
**貼文連結** https://x.com/Pxstar_/status/2039733921387307166  

**正文**

看到很多人不喜欢《人物》对Kimi的报道，认为这是「毫无底线的吹捧」「毫无常识的神话」，全篇充满了「文科生式对于科技的想象」。
这让我想起在我还在上学的时候，我眼里硅谷的公司都是这样的，因为对他们的报道就是那么神话，印象最深的一篇采访马斯克的，大概是这么写的：「 2002年马斯克从PayPal套现离场后，便开始了自己的假期，记者在里约热内卢的海滩上拍到了他，他一边看书一边喝啤酒，记者把镜头拉近，看到了书的名字《火箭推进器的基础理论》」
这些戏剧化的演绎式描述，可能在专业的人看来很幼稚，甚至是记者与企业家合谋给社会做的一场秀，但是这种演绎是能给很多人真正的力量的，《人物》不是商业或者科技媒体。他的受众也不是AI行业的从业人员，而是更多的行业外的普通人，为了塑造某种感受的能量场，可能输出了一些幼稚的内容，犯了一些错误。但是应该给这些错误一些宽容度，因为英雄需要舞台和灯光去塑造。
我们当年包容了多少对硅谷公司的吹捧，今天就应该包容多少对中国公司的吹捧。

---

**作者** immad（@immad）  
**貼文連結** https://x.com/immad/status/2039736146855678416  

**正文**

At my previous startup, I remember an ADP payroll rep coming to our office with a literal binder to set up payroll. A binder. This was the best option available to us. I filled out forms, waited,

---

**作者** Zack Shapiro（@zackbshapiro）  
**貼文連結** https://x.com/zackbshapiro/status/2039716839769440339  

**正文**

“This isn’t just a productivity shift, it’s an organizational one.” 🤖

---

**作者** Guillermo Flor（@guilleflorvs）  
**貼文連結** https://x.com/guilleflorvs/status/2039732359839273381  

**正文**

Sequoia's AI Opportunity map👇 

---

**作者** Jaya Gupta（@JayaGup10）  
**貼文連結** https://x.com/JayaGup10/status/2039737982576636294  

**正文**

Consumer platforms built one of the most powerful business models of the last two decades around a compounding loop: every user interaction became a signal that improved the system. Netflix, Meta,

---

**作者** Bill The Investor（@billtheinvestor）  
**貼文連結** https://x.com/billtheinvestor/status/2039645141624086701  

**正文**

会计师们，这下有压力了！一款自托管 AI 让你不用再为发票和收据发愁：拍个照片上传，产品信息自动提取，税费解析、货币转换，全在你笔记本电脑上搞定。

完全开源，零 API 费用，这可让传统会计软件的日子难过了。 

---

**作者** Tw93（@HiTw93）  
**貼文連結** https://x.com/HiTw93/status/2039713457952706686  

**正文**

想和大伙聊聊，在 AI 时代我是如何深入学习一个技术领域的。

之前没有 AI 之前更多是看书、翻这个领域有名的国内外人的所有博客，然后摘抄记录到笔记本，这种速度挺慢，但是很有学习的乐趣，比如当时学习 WebGL 就是这种感觉，可能学懂一个东西差不多要半年空闲时间，慢但快乐。

现在有了 AI 之后，其实我很讨厌网上那种3分钟教你看完百年孤独，也讨厌一切短剧和倍速看电视剧的方式，更多还是挑好的看，吃好一点。

不过最近写你不知道的 Claude Code 和 Agent 系列，除了自己懂的部分外，其实还有大量不太清楚的领域，好在之前收藏了不少文章，刚好借助这一块清库存，全部搞懂输出出去，一直认为，很多时候，不在于看了多少东西，听了多少东西，输入了多少东西，其实用处不大，更加看重你输出了多少东西，这个才是你自己的。

然后我上上周启动了一个深坑挑战自己，研究大模型的训练流程，确保非专业的人也听得懂，探索了2周，刚好这个经验可以分享给大伙，当然成文也差不多好了，最近会发出。

我会把这个学习过程当做写代码一样的组织，第一步收集高质量的资料，比如与之相关的近几年的精品论文，各大模型厂商发布的关键模型的博客，X上模型负责人发表的一些文章，以及斯坦福等高校的近两年关于这一块的课程学习，还有经典的手搓一个大模型的代码仓库等等，这些都是我的一个资料来源过程，我会借助工具自动化全部下载、转md、清洗，梳理，弄好结构化分门别类到我这次研究的仓库。

然后对于自己看得懂的内容就全部看一遍，把不好的删掉，好的留下，对于看不懂的内容，直接借助 Claude 帮我的理解，更复杂一点的直接翻译成中文去阅读，对于代码本地可以跑的就跑起来，不能跑的那种就去看结构，总之会有一个大概的认识和知晓技术原理，这个阶段可以去掉原有一半可能没有用的内容。

到了这个阶段，其实你对这个领域有一个大概的认知了，就可以给这篇文章开始写一个大纲，以及大纲应该结合的来源内容，这里均可以用markdown很多表达，你要讲什么，或者说你想讲什么更想让读者知道，一定一定，文章是写给你给给看的人看的，需要知晓对方的认知水平，和汇报其实差不多。

然后接下来就是苦力活加之前内容的复习过程，和大学时候考试前复习很像，把每一章的内容填充完整，这样下来，你会得到一篇非常长而且有点啰嗦的文章。

这个时候AI就可以帮太忙，你可以让他帮你不改变你原有的内容意思你的语气的情况下，帮我去掉无用的啰嗦内容，以及连贯不到位的内容，或者是这一块缺少的内容，还需要补充什么知识的地方，借助AI继续去完善补充，这里又可以学到很多原来遗漏的东西。

最后整理好以后，可以继续自己读一遍，而非让AI读一遍，这里AI只是工具，千万不要把你的脑袋被AI代替了，这就没有啥意思来，自己读的过程中可以对文章继续修改调优，这里和写代码又非常像了，自测那种感觉，修复问题修问题，最后读了2遍以后，基本感觉完美了，然后就可以发出来给大伙看看。

有小伙伴肯定是担心自己写的东西没有人看，就不太喜欢发出来，或者说就不写了，其实只要你的内容有意义，自然就有读者，而非是你偷懒的理由。

花10min写完这个碎碎念，结束，欢迎交流你是如何学习一个新领域的，下面视频就是我后面要发的那篇你不知道的大模型训练文章的学习仓库，挺有意思，就录了一个视频给大伙看看我的工业化学习方式。

---

**作者** hoeem（@hooeem）  
**貼文連結** https://x.com/hooeem/status/2039723470691451072  

**正文**

claude cowork was launched 3 months ago, since then claude has shipped 50+ updates which has completely changed how I utilise cowork, here's how you can take advantage and master it:
claude cowork has

---

**作者** a16z（@a16z）  
**貼文連結** https://x.com/a16z/status/2039720734579453967  

**正文**

The software supply chain has become the most critical and least-defended attack surface in modern software development.

This week, someone hijacked one of the most popular packages on the internet and used it to install a backdoor on every machine that ran npm install.

a16z's @MaikaThoughts, @zanelackey, and Joel de la Garza on how @SocketSecurity detected the Axios attack within 6 minutes, why AI is compressing software supply chain attack timelines, and why defenders have to move at machine speed to save the agents: https://www.a16z.news/p/et-tu-agent-did-you-install-the-backdoor

---

**作者** Brad Carry (VC & Podcaster)（@bradcarryvc）  
**貼文連結** https://x.com/bradcarryvc/status/2039430031135436856  

**正文**

POV: You dropped out of Stanford, moved across the country to San Francisco, and now you’re building a $0 ARR startup with 15 of your closest friends you met on X 

---

**作者** Ramp Labs（@RampLabs）  
**貼文連結** https://x.com/RampLabs/status/2039726632886235648  

**正文**

We built a system that steers an LLM toward specific concepts without retraining, and in the process learned something concrete about where meaning lives in different model architectures. Steer a

---

**作者** Kahlil Lalji（@bykahlil）  
**貼文連結** https://x.com/bykahlil/status/2039569020337496387  

**正文**

You know what underlies all of this? Agents moving money

---

**作者** Ramp Labs（@RampLabs）  
**貼文連結** https://x.com/RampLabs/status/2039726090478874897  

**正文**

Introducing Steer AI. We made an AI that can't stop thinking about any concept you choose, by steering a model's internal representations at inference time.

Ask it anything, and watch it bend reality around that concept. Available for one week only. 

---

**作者** Jaya Gupta（@JayaGup10）  
**貼文連結** https://x.com/JayaGup10/status/2039724653355450570  

**正文**

A business context graph!

---

**作者** The Claude Portfolio（@theaiportfolios）  
**貼文連結** https://x.com/theaiportfolios/status/2039478715302994361  

**正文**

Breaking: Claude was right

Yesterday, the Agents invested in Eli Lilly $LLY because of a potential FDA approval for their oral Ozempic.

Today, the FDA approved its Foundayo weight-loss product, unlocking a $50B new market.

Stock was up 3% on the news. 

---

**作者** Ben Burtenshaw（@ben_burtenshaw）  
**貼文連結** https://x.com/ben_burtenshaw/status/2039340340658802849  

**正文**

tl;dr: how to build a team of open source agents that collaborate on autoresearch.
This article walks through a project to implement @karpathy 's autoresearch in a multi agent system with open source

---

**作者** 花叔（@AlchainHust）  
**貼文連結** https://x.com/AlchainHust/status/2039550416187478272  

**正文**

我靠，还真给我整上架了！

我的《OpenClaw橙皮书》《Claude Code橙皮书》现在均已上架微信读书！！

不走传统出版流程，但这种伪出版，方便大多数人阅读到，破除信息差的方式我觉得还挺棒的！ 

---

**作者** Jiayuan (JY) Zhang（@jiayuan_jy）  
**貼文連結** https://x.com/jiayuan_jy/status/2039598198663336235  

**正文**

Multica 当前解决的一个最核心的问题：多人和多 Agent 之间的协作与 context 交换。

例如现在我每天早上到公司的第一件事就是阅读 Inbox 中的所有内容：

- Agent 已经完成的待 review 的工作
- 其他人和 Agent 的沟通中（例如方案设计）需要我来确认的地方
- 新的 issue 需要我这边提供部分上下文
- 一些每天的汇总信息（日报、数据分析、市场研究等）

如果你当前只是 1 个人使用多个 Agent，其实对 Multica 的需求不会那么大。（但是也可以有一个统一的 workspace 来管理所有 Agent）

---

**作者** ashu garg（@ashugarg）  
**貼文連結** https://x.com/ashugarg/status/2037695467480605044  

**正文**

I share what founders need to hear from the people who make the buying decisions.
Where are we, really, in the enterprise AI adoption cycle? What’s working, what’s holding big companies back, and what

---

**作者** Alex Booker（@bookercodes）  
**貼文連結** https://x.com/bookercodes/status/2038981619587994114  

**正文**

We built an AI memory system modeled on how humans remember and - just as importantly - how they forget. It compresses conversations 5-40x, supports temporal reasoning, and holds the highest

---

**作者** Chao Huang（@huang_chao4969）  
**貼文連結** https://x.com/huang_chao4969/status/2039399788215705888  

**正文**

Introducing OpenHarness, an ultra-lightweight, pure Python alternative to Claude Code that delivers approximately 80% of essential agent functionality using just 3% of the code lines.

With a single command, you can launch OpenHarness and unlock seamless integration with popular CLI agents including OpenClaw, nanobot, Cursor, and more.

OpenHarness is an open-source Python implementation designed for researchers, builders, and the community:
- 🔍 Understand how production AI agents work under the hood
- 🧪 Experiment with cutting-edge tools, skills, and agent coordination patterns
- 🔧 Extend the harness with custom plugins, providers, and domain knowledge
- 🏗️ Build specialized agents on top of proven architecture

Try OpenHarness: https://github.com/HKUDS/OpenHarness

---

**作者** yibie（@yibie）  
**貼文連結** https://x.com/yibie/status/2039007244214542568  

**正文**

由于我觉得卡神 的 autoresearch 是这几年，最重要的 AI 工作方法论，所以我创建了一个仓库，专门搜集基于 autoresearch 衍生的各类变体，以及有价值的相关讨论。 欢迎 Star，Fork，最好可以一起共建。

https://github.com/yibie/awesome-autoresearch

---

**作者** Shann³（@shannholmberg）  
**貼文連結** https://x.com/shannholmberg/status/2039636480101118430  

**正文**

a guy is running an agentic social media scheduler that brings him $73K/month

he just showed how he uses Paperclip and AI skills to automate his entire marketing pipeline

here´s how he did it 🧵 

---

**作者** Aman（@Amank1412）  
**貼文連結** https://x.com/Amank1412/status/2031422225061130552  

**正文**

Someone built an AI agent that automates outbound sales.

> Paste your product URL
> It finds companies actively hiring for your problem
> Researches their team, stack, and signals
> Writes hyper personalized outreach

End result: leads, sequences, and meetings generated automatically.

Link: http://clawgtm.com

---

**作者** Brainbase Labs（@BrainbaseHQ）  
**貼文連結** https://x.com/BrainbaseHQ/status/2032147218359337188  

**正文**

We're excited to release Brainbase Conversational, the first ever code-runtime general agent designed for perfectly reliable and traceable voice agents. 

---

**作者** Viking（@vikingmute）  
**貼文連結** https://x.com/vikingmute/status/2039683588212580380  

**正文**

Stitch 这个东西的贡献应该是 design.md 文件了吧，我找到了一个 awesome-design-md https://github.com/VoltAgent/awesome-design-md
里面有几十个设计风格比较优秀网站的 design.md ，拷贝它们风格的时候直接用对应的文件就行。

其实根本不需要必须在 Stitch 中用，任意一个 AI agent 都可以用，我花五分钟再 v0 中就创建了三种风格迥异的设计，prompt 就一行字，按照这个design.md 给我随便设计一个 AI Agent 网站，参考了 OpenCode,raycast 和 Airbnb 这三个，https://v0-open-code.vercel.app/ 效果具体怎么样呢？大家可以看看 live demo以及我的视频，我觉得还是不错的。

---

**作者** Kyle Gawley（@kylegawley）  
**貼文連結** https://x.com/kylegawley/status/2039643257551167936  

**正文**

I cancelled my Claude subscription

I'm now self hosting the open source version on a $5/mo droplet

---

**作者** Aadit Sheth（@aaditsh）  
**貼文連結** https://x.com/aaditsh/status/2039673645967229259  

**正文**

This Sequoia chart has a quadrant where agencies die.

And one where they thrive.

They mapped $1T+ in services getting disrupted by AI agents. Four quadrants: is the work outsourced or insourced, and does it need judgment or intelligence?

Right side (autopilot territory)... agencies die here. Insurance brokerage, IT services, payroll. Work that can be fully codified. If you're here, you're competing against software that costs 99% less and doesn't sleep.

Left side (copilot territory)... agencies thrive here. Consulting, PR & comms, design, executive search. Still requires real judgment. AI can't replace the thinking.

I've been seeing this play out at The Narrative Company. We do comms work for Fortune 500 executives and honestly every decision requires human judgment. AI cannot do that (at least not yet). But the delivery underneath? We've built systems where AI handles what used to take a full team weeks. The thinking still comes from us. The cost to execute has just dropped massively.

I think this gap is about to become the new baseline. Agencies still hiring 20 people for what 5 can do with AI aren't just inefficient. They're going to price themselves out.

Five-person firms doing the work of fifty. Same price to the client. Completely different economics underneath.

If you're small enough to move fast, honestly this is probably the biggest opportunity in a decade.

---

**作者** yibie（@yibie）  
**貼文連結** https://x.com/yibie/status/2039630540127785338  

**正文**

有点好奇港科大里的都是一些什么神人，动不动代码规模压缩到十分之一不止

https://github.com/HKUDS/OpenHarness

---

**作者** Muratcan Koylan（@koylanai）  
**貼文連結** https://x.com/koylanai/status/2039580023569428787  

**正文**

Anthropic published two context engineering posts last month. The cookbook covers compaction, clearing, and memory. The harness post covers multi-agent architecture for long-running coding sessions.

The cookbook is a good starting point if you're new to context management. If you've been building agents, most of it is familiar. 

But a few patterns were useful regardless of what SDK or framework you're using:

- When you clear old tool results from context, you invalidate your cached prompt prefix. So clearing needs to be worth the cache miss. If you clear too often and free too little each time, you're paying cache-write overhead every turn for minimal gain. Clear in bigger, less frequent chunks.

- When you override the default compaction/summarization prompt, you're replacing it entirely. The default usually includes task-continuation scaffolding (state, next steps, open threads). If you write your own, you need to cover that yourself. Easy to miss.

- If you're combining context clearing with a memory/note-taking tool, exclude the memory tool from clearing. Otherwise the agent's own memory reads get wiped and it loses track of what it just saved. This applies to any agent system where one tool's outputs are inputs to another.

The harness post had more I didn't know.

Context anxiety is different from context rot. Context rot is recall degrading as the window fills. Context anxiety is the model wrapping up prematurely because it thinks it's running out of context. Compaction doesn't fix it because the conversational history is still there, just compressed. Only a full context reset (fresh agent + structured handoff) fixes it.

In self-evaluation, the generator reliably praised its own work, even when the output was broken. Separating the evaluator into its own agent and calibrating it to be skeptical was far more tractable than making a generator self-critical. The calibration took multiple rounds of reading evaluator logs and fixing where its judgment diverged from the developer's. Few-shot examples with score breakdowns. 

Every component in an agent harness encodes an assumption about what the model can't do on its own. When they upgraded from Opus 4.5 to 4.6, the sprint decomposition became unnecessary (this is a good example of why you have to rewrite all your code from scratch every 6 months). The model held coherence over 2+ hour builds without it. The harness doesn't shrink as models improve. 

One last note that seems like Claude is keeping the planner focused on product context and high-level technical design, not granular implementation details, while Codex folks are posting against a separate planning mode. If the planner gets a technical detail wrong, the error cascades into downstream implementation. Better to constrain on what to build and let the generator figure out how.

Cookbook: https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools Harness post: https://www.anthropic.com/engineering/harness-design-long-running-apps

---

**作者** 阿绎 AYi（@AYi_AInotes）  
**貼文連結** https://x.com/AYi_AInotes/status/2039221410024075594  

**正文**

有条件一定要用最好的AI大模型Claude，用opus 4.6！
这个印度开发老哥把Claude代码功能讲的太细了，
中文字幕版已做好，兄弟们请查收！
每个程序员和AI玩家都应该知道的12个Claude代码功能：
- CLAUDE.md
- Permissions
- Plan Mode
- Checkpoints
- Skills
- Hooks
- MCP
- Plugins
- Context
- Slash Commands
- Compaction
- Subagents

---

**作者** Louis Gleeson（@aigleeson）  
**貼文連結** https://x.com/aigleeson/status/2039301356918645138  

**正文**

A developer just open-sourced a full autonomous AI dev team that runs 24/7 without a single human.

It's called OpenSwarm. You give it a Linear issue. It writes the code, reviews it, fixes CI failures, resolves merge conflicts, and closes the ticket. All by itself.

Here's what's wild:

→ Worker agent writes the code
→ Reviewer agent evaluates and requests changes
→ Tester and Documenter run after approval
→ StuckDetector fires when agents hit a wall
→ LanceDB vector memory lets it remember every past task
→ Controls your entire repo from a Discord message

You don't touch it. It just ships.

The memory system is insane. Hybrid retrieval scoring across belief, strategy, and system pattern memory types. It doesn't just complete tasks. It gets smarter after each one.

It also monitors your open PRs, auto-fixes failing CI, auto-resolves merge conflicts, and retries until everything is green.

MIT License. Built on Claude Code CLI.

---

**作者** hoeem（@hooeem）  
**貼文連結** https://x.com/hooeem/status/2039440364893827538  

**正文**

POV: you spend $4000 on personal trainers every year and now you see this. 

---

**作者** 柴郡🔔｜Crypto+AI Plus（@0xCheshire）  
**貼文連結** https://x.com/0xCheshire/status/2039641474913243323  

**正文**

能让你的下一个项目效率提升 10 倍的最佳 Claude Code  开源仓库：

1. Superpowers
https://github.com/obra/superpowers

2. Awesome Claude Code
https://github.com/hesreallyhim/awesome-claude-code

3. GSD (Get Shit Done)
https://github.com/gsd-build/get-shit-done

4. Claude Mem
https://github.com/thedotmack/claude-mem

5. UI UX Pro Max
https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

6. n8n-MCP
https://github.com/czlonkowski/n8n-mcp

7. Obsidian Skills
https://github.com/kepano/obsidian-skills

8. LightRAG
https://github.com/hkuds/lightrag

9. Everything Claude Code
https://github.com/affaan-m/everything-claude-code

---

**作者** himanshu（@himanshustwts）  
**貼文連結** https://x.com/himanshustwts/status/2038924027411222533  

**正文**

Based on everything explored in the source code, here's the full technical recipe behind Claude Code's memory architecture:

[shared by claude code]

Claude Code’s memory system is actually insanely well-designed. It isn't like  “store everything” but constrained, structured and self-healing memory.

The architecture is doing a few very non-obvious things:

> Memory = index, not storage
+ MEMORY.md is always loaded, but it’s just pointers (~150 chars/line)
+ actual knowledge lives outside, fetched only when needed

> 3-layer design (bandwidth aware)
 + index (always)
 + topic files (on-demand)
+ transcripts (never read, only grep’d)

> Strict write discipline
 +  write to file → then update index
 + never dump content into the index
 +  prevents entropy / context pollution

> Background “memory rewriting” (autoDream)
 +  merges, dedupes, removes contradictions
 +  converts vague → absolute
 +  aggressively prunes
 +  memory is continuously edited, not appended

> Staleness is first-class
 + if memory ≠ reality → memory is wrong
 +  code-derived facts are never stored
 +  index is forcibly truncated

> Isolation matters
 + consolidation runs in a forked subagent
 + limited tools → prevents corruption of main context

> Retrieval is skeptical, not blind
 +  memory is a hint, not truth
 +  model must verify before using

> What they don’t store is the real insight
 +  no debugging logs, no code structure, no PR history
 +  if it’s derivable, don’t persist it

---

**作者** WorldofAI（@intheworldofai）  
**貼文連結** https://x.com/intheworldofai/status/2039481184078409769  

**正文**

Built a 3-layer Memory Stack that wires Claude Code directly into Obsidian with skills so it never forgets your project DNA, your notes, your standards, or your goals.

Fixes most of Claude Code's memory issues. 

---

**作者** 毅行出海 Sven（@sven_ai）  
**貼文連結** https://x.com/sven_ai/status/2039175168975843334  

**正文**

这项目有点猛，已经冲到 GitHub 50.5k Star，还在持续上涨，建议收藏

项目作者在CC源码泄露后，没有继续停留在“存档”层面，而是选择从零开始用 Python 重写，复现了 Claude Code 的核心 harness、tool wiring 和 agent workflow。

也就是说，它在做的不是简单搬运，
而是把 Claude Code 最值得研究的那部分能力，重新实现成一个可继续演进的开源版本。

作者同时也在推进 Rust 移植，目标是做出更快、更安全的最终版本。

如果你关注 AI coding、agent runtime、harness engineering 这些方向，这个项目值得收藏起来。
GitHub：https://github.com/instructkr/claw-code

---

**作者** Emanuel O.（@inceptioncortex）  
**貼文連結** https://x.com/inceptioncortex/status/2039100617176531385  

**正文**

The other Anthropic open-source nobody is talking about:

→ Hermes-agent — best agentic harness

→ Paperclip — heartbeat monitoring for agent tasks & routines

→ Phone gateway — notifications for status, commits, cron jobs

The playbook is open. The pieces are free. 

---

**作者** Rohit（@rohit4verse）  
**貼文連結** https://x.com/rohit4verse/status/2039382279743840739  

**正文**

Everyone is building inside the AI bubble.
Almost nobody is building what survives after it pops.
Foundation models. Humanoid robots. AGI timelines.
Meanwhile the actual money is flowing into

---

**作者** JD Ross（@justindross）  
**貼文連結** https://x.com/justindross/status/2039345193346904143  

**正文**

Insurance Brokerage is the biggest opportunity in AI Autopilot

---

**作者** Nevo David（@wickedguro）  
**貼文連結** https://x.com/wickedguro/status/2039344437374156948  

**正文**

2026 is clearly the year of the personal AI Assistant. You hook this assistant to all your services, and it can do anything you want. From reading and replying to your email to negotiating about gym

---

**作者** Roan（@RohOnChain）  
**貼文連結** https://x.com/RohOnChain/status/2039338468065849589  

**正文**

🚨 BREAKING: You can now run a Bloomberg Terminal for FREE.

The closest open-source alternative that exists. 
No $24,000 subscription. No API costs. 100% local on your machine.

Bookmark this. Install it right now. Takes ten minutes. 

---

**作者** KK.aWSB（@KKaWSB）  
**貼文連結** https://x.com/KKaWSB/status/2039292942116925882  

**正文**

🔥 AionUI，GitHub 已经 20k ⭐，最近日增 271，势头很猛。

这东西说白了就一句话： 一个本地跑的 AI Agent 调度面板， 把 Claude Code、Gemini CLI、Codex、OpenCode 全塞进一个界面里管。

为什么需要它？
现在玩 AI coding 的人，手里都不止一个 agent。 Claude Code 写逻辑，Gemini 做分析，Codex 跑补全—— 每个都开一个终端窗口，来回切换烦死人。
AionUI 干的就是这件事： - 一个面板同时开多个 agent，并行跑任务 - MCP 配置一次，自动同步到所有 agent，不用一个个配 - 本地运行，代码不上传，数据不出门 - 支持定时任务，挂着 24/7 自动跑 - 免费开源，Windows、Mac、Linux 都能用

相当于给你的 AI 工具箱装了一个统一操作台。

别再一个个终端切来切去了。 用多 agent 的人，这个值得收藏。
🔗 https://github.com/iOfficeAI/AionUi

---

**作者** Damian Player（@damianplayer）  
**貼文連結** https://x.com/damianplayer/status/2039458905848242642  

**正文**

the people who figure this out WILL have an unfair advantage. soon, everyone will know how to do this. here's how to start before it's obvious
for the last year, developers have had autonomous AI

---

**作者** Zichen Chen (🐱,💖)（@my_cat_can_code）  
**貼文連結** https://x.com/my_cat_can_code/status/2039381668654719052  

**正文**

#autoresearch
We've been asking ourselves a question: if AI agents can now run hundreds of experiments overnight, how do we know whether they're actually contributing to research — or just generating noise?

That's why we built AutoLab (https://autolab.moe/blog). Not another pass/fail benchmark, but an open-source environment where agents face the same loop every researcher knows intimately — propose, test, fail, diagnose, revise, repeat. 23 tasks with no answer keys, just open search spaces and real constraints. 
We ran 160 evaluations across 7 frontier models. 8,640 trajectories. 598M tokens. Every decision, every pivot, every dead end — all openly available in our Live Lab for anyone to replay and learn from. 

What we found wasn't about which model is "smartest." It's about a capability we call closed-loop resilience: when incremental refinement stops working, can the agent recognize it and restructure? On one task, two frontier models hit the same wall. One kept pushing within the existing frame. The other stepped back and redesigned the approach entirely. That moment — knowing when to abandon a frame, not just optimize within it — is what separates real research from sophisticated pattern matching. 
We believe this matters beyond benchmarking. If agents are genuinely entering the research loop, we want that transition to be measured transparently, built in the open, and shaped by the community — not locked inside any single lab. The scientist doesn't disappear. The loop gets a new participant. And we want to make sure that participant is understood. 

This is a joint effort across @Stanford, @MIT, @UW, @UCSanDiego, @ucsantabarbara, @NotreDame, NUS, @Google, @nvidia, @IBMResearch, and @bakelab_hq. But 23 tasks is just the start. If you have an optimization problem you've spent weeks grinding on empirically — with a clear metric and no known optimal solution — it probably belongs here. Contribute a full task, a rough skeleton, or just the idea. 

The best benchmarks aren't built by one team. They're built by the people who actually do the work!

---

**作者** Caspar Broekhuizen（@caspar_br）  
**貼文連結** https://x.com/caspar_br/status/2039576939724521609  

**正文**

Great stat in here: Claude Code went from 17% to 92% on our eval set once it had access to LangSmith traces and Skills. A coding agent without trace data is just guessing at fixes

---

**作者** Tony出海（@iamtonyzhu）  
**貼文連結** https://x.com/iamtonyzhu/status/2039141752070984051  

**正文**

Claude code 分析文章千千万，唯独这篇最强，深入分析里边的结构。

我们学习这个世界最强 agent 系统，
拿着这些方法应用到产品 agent 里面去。

ps ：XiaoTan 又写出一个
《ClaudeCode源码深度研究报告（增强完整版）》，下载链接👇
https://github.com/tvytlx/claude-code-deep-dive 

---

**作者** Jaya Gupta（@JayaGup10）  
**貼文連結** https://x.com/JayaGup10/status/2039545730533318999  

**正文**



---

**作者** 铁锤人（@lxfater）  
**貼文連結** https://x.com/lxfater/status/2039181720457781613  

**正文**

已经有人将GPT-5.4塞入Claude code了😂

---

**作者** indigo（@indigox）  
**貼文連結** https://x.com/indigox/status/2039586298080751734  

**正文**

Jeff Dean 和 Sanjay 现在都在用 Agent 写代码！如果他们是 100x 工程师，加了 Agent 他们可能是 1000x 工程师。Antigravity 产品负责人 Kevin 和 Windsurf 联创 Varun 在 Kleiner Perkins Builders 播客上分享了他们对 10x 工程师的新定义：

- 会分解问题：大问题拆成 Agent 能处理的原子片段；
- 设计可被 Agent 操作的代码库：有足够测试，Agent 改完代码后能自信地往前推进——老代码库 Agent 难以操作，因为不知道改动后哪些不变量还成立；
- 准确表达需求：给 Agent 错误需求 = 做出错误的东西；给 Agent 正确需求 = 产出正确的结果；
- 设置良好的运行环境：让 Agent 能自我调试、自我验证；

如果你还在手打代码，不让 Agent 独立工作，你会被落下，你的公司也会被落下。Varun 设定了团队最大人数上限：“AI 生产力提升必须超过团队增长带来的复杂度。我们的目标不是扩张，是精简”✨

---

**作者** Omar Waseem（@omarwasm）  
**貼文連結** https://x.com/omarwasm/status/2039430028400709867  

**正文**

“People who don't organize into tribes get wiped out by people who do”

Similar is true for agents.”

Damn

---

**作者** Garry Tan（@garrytan）  
**貼文連結** https://x.com/garrytan/status/2039554406501531725  

**正文**

Wow. Incredible amount of SOTA training data now just available to China thanks to @mercor_ai leak. Every major lab. Billions and billions of value and a major national security issue.

---

**作者** Olivia Moore（@omooretweets）  
**貼文連結** https://x.com/omooretweets/status/2039150266889744653  

**正文**

RIP, software as a service (1999-2025) 

Welcome to the world, services as software (2026 - ?)

---

**作者** Dan Shipper 📧（@danshipper）  
**貼文連結** https://x.com/danshipper/status/2039137683230867722  

**正文**

@badlogicgames Try this!
https://proofeditor.ai

---

**作者** 小互（@xiaohu）  
**貼文連結** https://x.com/xiaohu/status/2038905737003581737  

**正文**

说一句"hello"现在会消耗你整个 session 用量的 2%…

Claude 最近用量确实有些诡异

免费双倍用量两周是阴谋吗？故意让你养成肆无忌惮的使用习惯，然后收割你？

还是是双倍用量后大家的失落感…😌

 

---

**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2039616101097824362  

**正文**

🧵Thread: 硅谷做饭

1/🧭 做饭不是厨艺

在 Palo Alto，最稀缺的往往不是钱，而是下班后的注意力。

这份做饭指南最重要的约束只有两个：每天注意力投入≤1小时，每周采购≤3小时。👇 

---

**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2039614039777771738  

**正文**

🧵Thread: 孩子用AI没规则不行，不用也不行——一份按年龄段的实操指南

1/🧭 一位华人家长说了句特别精准的话：【孩子不用AI肯定不行，用AI没有边界没有规则也不行】。

核心发现：K-2和3-5年级的策略完全不同，搞反了比不做更糟👇 

---

**作者** AI Will（@FinanceYF5）  
**貼文連結** https://x.com/FinanceYF5/status/2039610160335950060  

**正文**

🧵Thread: Agent经济需要自己的身份证、护栏和监控摄像头

1/🧭 云计算刚起步时，大家都在造应用。

后来发现：应用需要Okta、Datadog、Snyk、Stripe。

AI agent正在重演这个故事——YC W26有28家公司在造agent的"水电煤"👇 

---

**作者** 阿绎 AYi（@AYi_AInotes）  
**貼文連結** https://x.com/AYi_AInotes/status/2039392277265797411  

**正文**

一位俄罗斯老哥分享了用 AI 能把学习效率提升 10 倍，靠这 3 件套 NotebookLM、Gemini、Obsidian，绝了！ 
一位俄罗斯老哥分享了用 AI 能把学习效率提升 10 倍，靠这 3 件套 NotebookLM、Gemini、Obsidian，绝了！ 
需要中英双语字幕的宝子留言告诉我

---

**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2039509008147710200  

**正文**

Claude Code「源代码开源」后，HKUDS 推出超轻量级 Claude Code 替代方案 ~ OpenHarness

Python 实现的 AI Agent Harness，核心目标是：
· 用 2.3% 的代码量（11,733 行 vs Claude Code 的 512,664 行）实现 80% 的核心功能
· 提供 44 倍更轻量 的代码库（163 文件 vs 1,884 文件）
· 保持 98% 的工具兼容度（43 个工具）和 61% 的命令覆盖（54 个命令）

团队对 Harness 的定义：
Harness = Tools + Knowledge + Observation + Action + Permissions
· Tools：43+ 工具，bash, read, write, search, MCP 等
· Knowledge：知识库，skills, CLAUDE.md, memory
· Observation：观察能力，git diff, error logs, file state
· Action：执行能力，CLI 命令, API 调用, 文件编辑
· Permissions：安全边界，sandboxing, approval, trust

和 Claude Code 的对比
维度  Claude Code  OpenHarness
代码量   512,664      11,733（2.3%）
文件数     1,884         163
语言            TS             Python
工具数        ~44          43（98% 兼容）
命令数        ~88          54（61% 覆盖）
技能兼容   ✅             ✅ anthropics/skills
插件兼容   ✅             ✅ claude-code/plugins
测试            —               114 + 6 E2E
企业功能   完整           剥离，专注核心

开源地址
https://github.com/HKUDS/OpenHarness

---

**作者** Adam（@_overment）  
**貼文連結** https://x.com/_overment/status/2039365942509994408  

**正文**

"agents are just LLMs running in a loop"

yeah, right. 

---

**作者** GitLawb（@gitlawb）  
**貼文連結** https://x.com/gitlawb/status/2039412303180013722  

**正文**

new version of OpenClaude is up! v0.1.5 is released. 

---

**作者** 阿绎 AYi（@AYi_AInotes）  
**貼文連結** https://x.com/AYi_AInotes/status/2039388762116088205  

**正文**

Elon Musk有一个学习方法，
解释了一个困扰我很多年的问题，
为什么有些东西学完一周就忘光，
有些东西一通百通，区别就在于你有没有先建树干。

@elonmusk 说过，要把知识看成一棵语义树，先确保自己理解基本原理，也就是树干和大树枝，再去接触树叶一样的细节，否则那些细节根本无处依附。

这句话我琢磨了很久，越想越觉得它解释了一个困扰我很多年的问题，为什么有些东西学完就忘，有些东西一通百通。

区别就在于你有没有树干。

没有树干的时候，你学到的每一个技巧都是悬在空中的，挂不住，风一吹就掉了，读完一本书一周忘光，学完一门课一个月用不上，本质上都是同一个问题，你在往一棵不存在的树上挂叶子。

这个比喻不只是修辞，它完全符合我们大脑的工作机制，神经可塑性的运作方式就是这样的，能带来成功的神经连接会被不断强化，无用的连接像枯枝一样断掉，当你有了坚实的主干结构，新信息才有地方附着，没有这个框架，所有知识都会快速滑落。

马斯克自己就是这么干的，他没有先去学怎么造火箭发动机，而是先弄懂火箭为什么要那样工作，物理学、材料科学、热力学的基本原理，一旦掌握了这些，具体的工程决策就变成了可以评估、质疑和改进的东西。

芒格也是一样，不死记投资方法，而是从心理学、历史、数学、物理、哲学、生物学里搭建多元思维框架，然后用这个框架在所有领域做决策。

一个方法只能解决一个问题，一次有效，一个原理能反复用上百次，应对你还没遇到的场景。

哈灵顿·埃默森说过，方法可能有百万种，但原理很少，掌握原理的人能成功选择自己的方法，只试方法而忽视原理的人注定遇到麻烦。

所以咱们不管学什么新东西，先别急着找技巧，先问一个问题，
这个领域的树干是什么，哪些是一旦理解就能让其他一切都变得更容易的第一性原理。

先长树干，再挂树叶。

---

**作者** Sharbel（@sharbel）  
**貼文連結** https://x.com/sharbel/status/2039376880814412163  

**正文**

> paid for Claude Pro for 6 months
> kept hitting rate limits
> switched to Max
> still hitting rate limits
> found Projects last week
> my context problem was never the plan
> it was me not using the tool properly
> skill issue discovered 

---

**作者** WquGuru🦀（@wquguru）  
**貼文連結** https://x.com/wquguru/status/2039519918291611656  

**正文**

Harness工程最佳实践的学习姿势：

- 一边剖析Claude Code源码
- 一边比对Claude Code和Codex工程实践差异

书籍源码（含PDF生成逻辑、最佳实践Skill）完全开放在https://github.com/wquguru/harness-books中，在线阅读可以看https://harness-books.agentway.dev/

搭配 @blackanger 张汉东老师的大作阅读更佳🫱 https://zhanghandong.github.io/harness-engineering-from-cc-to-ai-coding/

---

**作者** Alex Vacca（@itsalexvacca）  
**貼文連結** https://x.com/itsalexvacca/status/2039455570965692838  

**正文**

pov: when someone actually explains the architecture behind the repo instead of just telling you to download it 

---

**作者** Fili（@filiksyos）  
**貼文連結** https://x.com/filiksyos/status/2039364035494215847  

**正文**

Built a fun project last night

Reverse engineer any repo into it's original prompt 

---

**作者** meng shao（@shao__meng）  
**貼文連結** https://x.com/shao__meng/status/2039530691533402464  

**正文**

Stanford CS 153 课程，特邀讲座嘉宾阵容过于夸张了吧。。。完全不亚于顶级 AI 峰会阵容

课程项目设计「One-Person Frontier Lab」，AI 赋能下的个体生产力极限，项目要求学生用 10 周时间，验证"单人+ AI 工具"能否创造实质性价值。

不得不感叹，斯坦福的学生真是太幸福了，我对孩子的期待也是斯坦福，我自己是没机会了，等 Youtube 课程视频更新再学习 😄

btw... 中国到处都在追捧 OPC，除了制造焦虑和卖课的二手老师们，能不能真的出一些有价值的课程？

---

**作者** ℏεsam（@Hesamation）  
**貼文連結** https://x.com/Hesamation/status/2039381120127496362  

**正文**

how does Claude Code keep track of user preferences, manage it's memory or choose what to keep and what to forget? the leaked source code is here to tell us.
yesterday, @himanshustwts wrote a post

---

**作者** The Startup Ideas Podcast (SIP) 🧃（@startupideaspod）  
**貼文連結** https://x.com/startupideaspod/status/2039454928406728742  

**正文**

I have a running list of things I can't stop thinking about.
Opportunities. Things that scare me. Ideas worth stealing. All of it is colliding at once and if you're paying attention, you probably feel

---

**作者** Tony出海（@iamtonyzhu）  
**貼文連結** https://x.com/iamtonyzhu/status/2039505555937763337  

**正文**

原推特创始人 Jack 的 Block 公司非常激进，用 AI 深度改造公司结构。

AI 就是这种技术。 有史以来第一次，一个系统可以维护整个业务的持续更新模型，并利用它来协调工作，而这些工作以前需要人类通过层层管理来传达信息。

---

**作者** Jaya Gupta（@JayaGup10）  
**貼文連結** https://x.com/JayaGup10/status/2039474958787895297  

**正文**

Context graph part 2 > 

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
