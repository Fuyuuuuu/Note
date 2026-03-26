好，這批量很大，我一個一個抓。讓我先把所有 URL 的內容拉回來。讓我一次把剩下的 speedrun 公司全部查完。好，資料夠了。這 24 家全部來自 **a16z Speedrun SR005**（2025 年批次）。讓我把它們整理成你需要的分析格式。

---

## a16z Speedrun SR005 — 24 家公司快速分析

我按照**跟你的 Compliance Context Infra 的相關性**分成四個等級：

---

### 🔴 高度相關（直接客戶 / 競爭者 / 架構驗證）

| 公司 | 做什麼 | 跟你的關係 |
|------|--------|-----------|
| **Artifact** | AI Agent 會計事務所，自動化對帳、分類帳過帳、稅務。$4M seed，a16z 領投，99% 對帳準確率，96% 總帳過帳準確率。SOC2/GDPR/ISO 認證。 | **跟 Cranston 同類型。** 需要即時更新的稅法/會計準則 Context。你的 Infra 可以讓它的 Agent 知道最新稅務法規而不用自建。 |
| **Loan Labs** | 為房貸公司建 agentic workers | **跟 Proximitty 類似。** 房貸涉及 TILA、RESPA、ECOA、HMDA 等大量聯邦+州級法規。需要你的 Compliance Context。 |
| **Logical Health** | 健康保險的透明度引擎 | **Healthcare compliance 垂直。** 保險法規+HIPAA+州級保險規定。你的 Context Infra 直接適用。 |
| **Moona Health** | AI 睡眠照護，由保險承保 | 需要理解保險報銷規則、FDA 設備合規、HIPAA。潛在客戶。 |
| **Fearn** | 合規 AI 用於起草智慧財產權 | **最直接相關。** 專門做 IP 起草的合規 AI，驗證了合規+AI+專業領域這個組合有市場。可能是競爭者也可能是合作者。 |
| **Avenir AI** | AI Agent 處理員工福利，$1.9T 市場 | 員工福利涉及 ERISA、ACA、COBRA、HIPAA 等複雜法規。需要你的 Compliance Context。 |
| **Nexxa.ai** | 重工業的 Agentic AI。9 個月從 0 到 $980K，每季 3x 增長，100% 專案啟動率。鐵路、金屬、汽車、建築。 | 重工業合規需求巨大（OSHA、EPA、行業標準）。你的 Context Infra 可以服務這類工業 AI。 |

---

### 🟡 中度相關（潛在客戶 / 間接驗證）

| 公司 | 做什麼 | 跟你的關係 |
|------|--------|-----------|
| **Ambiguous** | AI coworkers，像隊友一樣思考 | 通用 AI 員工平台。如果服務受監管行業客戶，就需要合規 Context。 |
| **Anchr** | 食品經銷商的 AI Agent 網路，自動化訂單接收、採購、庫存管理 | 食品行業有 FDA/FSMA 合規需求。間接客戶。 |
| **Sourcerer** | 建構未來的自主供應鏈 | 供應鏈涉及進出口合規、關稅、制裁篩查。你之前提過的「供應鏈」利基。 |
| **Margin** | 第一張 AI 信用卡 | 金融產品 = 金融合規（TILA、FCRA、ECOA）。跟 Pier 場景類似。 |
| **Presia** | 管理諮詢的 AI Agent，3 個月 $270K ARR | 如果服務受監管行業的諮詢專案，需要合規 Context。驗證了「AI 取代諮詢」模式。 |
| **Maniac** | 企業智能的 Pareto-optimal AI | 企業智能平台如果處理受監管數據，需要合規護欄。 |
| **EverCurrent** | 硬體開發的 AI 平台，把分散的知識轉化為共享清晰度。創辦人來自 Autodesk/Onshape，IOI 國際奧賽代表。 | **「把分散知識整合成可用 Context」的模式跟你完全平行**，只是她做硬體開發，你做合規。架構啟發很大。 |
| **Metal** | 募資超級智能 | 募資涉及證券法規。SEC 合規 Context 的潛在客戶。 |
| **Limy AI** | 讓品牌掌控 agentic interactions | 品牌合規、行銷合規（FTC 指南等）。你之前提過的行銷合規利基。 |

---

### 🟢 低度相關（模式參考 / 市場訊號）

| 公司 | 做什麼 | 值得注意的 |
|------|--------|-----------|
| **Labyrinth** | 未找到詳細資訊（可能 stealth） | — |
| **Layerpath** | AI Demo Agent 把潛在客戶轉化為營收 | GTM 工具，不直接相關但模式可參考 |
| **Valor** | 未找到詳細資訊 | — |
| **BotBot** | AI 產品的 UX 層 | 你的產品層如果做得好也需要好的 UX |
| **Brief** | AI 首席產品官 | 產品管理 AI，無直接合規關係 |
| **Sans Strings Studio** | 科技增強的內容工作室 | 娛樂/內容，無直接關係 |
| **Jooba** | 全球首家自主招聘公司 | 招聘有 EEOC/勞動法合規，但距離你的核心較遠 |

---

## 關鍵洞察

**1. a16z 跟 YC 在同一個方向下注。** Artifact（a16z）跟 Cranston（YC）幾乎做一樣的事——AI 會計事務所。Loan Labs（a16z）跟 Proximitty（YC）都做貸款/催收 AI。這不是巧合，是市場共識。

**2. 這批 24 家裡至少 7 家是你的直接潛在客戶。** Artifact、Loan Labs、Logical Health、Moona Health、Avenir AI、Nexxa.ai、Margin——每一家都在受監管行業用 AI Agent，每一家都需要合規 Context。

**3. Fearn 是你在 IP 合規領域的直接 signal。** 它證明「合規 + AI + 專業領域」的組合被 a16z 認可。但它只做 IP 起草這個小垂直，你的 Infra 可以更通用。

**4. EverCurrent 的架構跟你的高度同構。** 她做的是「把硬體開發的分散知識整合成共享 Context」，你做的是「把合規的分散知識整合成共享 Context」。她的產品演進路徑值得密切追蹤。

**5. 每批加速器都在冒出更多「垂直 AI Agent 需要合規但自己不做」的公司。** 這持續強化你的 thesis：做底層 Compliance Context Infra，讓這些公司都來接你的 API。

繼續丟下一批？



---
---
---


Rillet — AI-native ERP（Sequoia + a16z）
做什麼： AI 會計帳務軟體，自動化記帳、對帳、結帳，讓財務團隊在幾小時內完成原本需要幾週的結帳流程。 Tech Startups整合 Salesforce、Stripe、Brex 等工具，即時拉入資料並自動處理。
關鍵數據：

$70M Series B，a16z + ICONIQ 聯合領投，估值約 $500M Tech Startups
總融資超過 $100M，在不到一年內完成 Tech Startups
200+ 客戶，包括 Windsurf 和 Postscript Tech Startups
自動化 93%+ 的手動會計功能
自動合規 ASC 606（營收認列）、遞延收入、合約資產等 GAAP 要求 Kruze Consulting
創辦人 Nicolas Kopp 是數位銀行 N26 的美國前 CEO

商業模式： SaaS 平台，取代 Oracle NetSuite 這類傳統 ERP。不是做「事務所」服務，而是賣軟體工具給企業財務團隊。
跟你的架構的關係：
Rillet 是 Cranston / Artifact 的上游。Cranston 和 Artifact 做的是「AI 會計事務所」（取代人），Rillet 做的是「AI ERP 平台」（取代系統）。三者的差異：
RilletCranston / Artifact賣什麼軟體平台會計服務客戶企業內部財務團隊需要外包會計的公司取代誰Oracle / NetSuite傳統會計事務所合規處理方式內建 GAAP/ASC 606 邏輯自建稅務合規知識規模$500M 估值，$100M+ 融資早期，<$5M
對你的啟發：

Rillet 證明了「合規內建」的價值。 它的一大賣點就是自動 ASC 606 合規、audit-ready workpapers。這說明合規不是附加功能，而是 核心差異化。你的 Context Infra 可以讓更多 SaaS 產品做到 Rillet 在會計領域做到的事——把合規變成自動且內建的。
Rillet 的 $500M 估值 = 會計 AI 市場被驗證。 這意味著 Cranston、Artifact、Denki、Oxus 都在追一個被市場確認的大機會。而你的 Context Infra 是這些公司的共同需求。
Rillet 也可能是你的客戶。 它現在自己處理 GAAP/ASC 606 邏輯，但隨著擴展到更多法規領域（跨國稅務、多國合規），一個外部 Compliance Context API 會更有效率。


Rima AI — 會計師的文件 + 試算表自動化（YC S22）
做什麼： 幫會計師自動化文件和試算表工作。會計師用簡單語言描述他們的工作流程，Rima 的 Agent 就會代替執行，並保留他們的 know-how。 Y Combinator
具體功能： 上傳 PDF（1 份或 100 份），Rima 以人類級別準確度讀取每一行項目，自動填入你的 Excel 工作簿，並跨檔案比對和對帳。每個資料點都可追溯到原始來源。 Getrima
關鍵數據：

YC S22（原名 Garage，從非洲汽車零件 marketplace pivot 成會計 AI）
5 人團隊，Austin
創辦人：Georgia Tech + Harvard MBA，前 Bain、Draper Associates
與 AI 供應商有零資料保留協議 Getrima

商業模式： SaaS 工具，賣給會計師和財務團隊。是比 Rillet 更小、更聚焦的產品——不取代整個 ERP，而是自動化 Excel 和 PDF 的手動工作。
跟你的架構的關係：
Rima 是這個生態裡最底層的工具型角色——做的是 Document → Structured Data 的轉換，類似 Reducto。它不處理合規邏輯，只處理數據提取和填表。
把所有會計 AI 公司堆疊起來看：
┌─────────────────────────────────────────────┐
│  Cranston / Artifact                         │ ← AI 事務所（做服務）
│  "我幫你做會計"                               │
├─────────────────────────────────────────────┤
│  Rillet                                      │ ← AI ERP 平台（取代系統）
│  "我是你的會計系統"                            │
├─────────────────────────────────────────────┤
│  Denki / Oxus                                │ ← AI 稽核（確保正確）
│  "我檢查你的帳對不對"                          │
├─────────────────────────────────────────────┤
│  Rima AI                                     │ ← 文件自動化（數據提取）
│  "我幫你把 PDF 變成 Excel"                    │
├─────────────────────────────────────────────┤
│  ❓ 你的 Compliance Context Infra ❓          │ ← 合規知識層
│  "我告訴所有人法規是什麼、怎麼遵守"            │
└─────────────────────────────────────────────┘
每一層都需要知道「法規要求什麼」，但沒有人在做這個統一的知識層。 Rima 知道怎麼提取數據但不知道數據是否合規；Rillet 內建了 ASC 606 但其他法規要自己加；Cranston 的 Agent 自己學稅法；Denki/Oxus 自己處理 SOX 規則。
你的 Compliance Context Infra 就是這張圖最下面那層——所有人的公用基礎設施。


---
---
---

Let me review the transcript to understand the context and ongoing analysis framework.Now let me search for Stack AI and Ema AI.Now I have enough data. Let me provide the analysis.

---

## Stack AI — 企業 AI Agent 建構平台（YC W23）

**做什麼：** No-code 拖拉式平台，讓企業非技術人員也能建構和部署 AI agents，自動化各種後台作業流程。

**關鍵數據：**
- YC W23 batch，創辦人 Antoni Rosinol 和 Bernardo Aceituno 都是 MIT PhD
- $16M Series A，由 Lobby VC 領投，LifeX Ventures、Vercel CEO Guillermo Rauch、Weaviate CEO Bob Van Luijt 等參投
- 團隊 13 人，成員來自 MIT、Meta AI、NASA、BCG Gamma、IBM
- 服務數百家組織，包括 Fortune 500 公司、銀行、醫院和大學
- 支援 30+ LLM 供應商和 100+ 資料連接器，符合 SOC 2 Type 2、HIPAA、GDPR
- 客戶包括 Nubank、LifeMD、MIT Sloan、SmartAsset，以及 Top 5 國防機構

**產品架構：**
- 視覺化 drag-and-drop canvas builder，將預建元件組成 agentic workflows
- Auto Agents 功能：用自然語言描述需求，平台自動生成完整的多步驟 AI agent
- 整合 SharePoint、Snowflake、Salesforce、Confluence 等企業數據源
- 支援 on-premise 部署和 VPC 部署

**核心使用場景：** RFP 回應生成、投資備忘錄撰寫、保險理賠處理、合規稽核自動化。在金融領域包含 KYC 自動化、CapEx/OpEx 分類、對帳自動化。

**商業模式：** SaaS 平台，兩層定價（Free + Enterprise custom pricing），瞄準大企業客戶。

---

## Ema AI — Universal AI Employee（企業通用 AI 員工）

**做什麼：** 建構「萬用 AI 員工」，可以變形為組織內任何角色——客服、HR、銷售、法務合規、資料分析等。

**關鍵數據：**
- 成立 2023 年，總部 Mountain View，總融資 $61M，跨 3 輪
- Series A $36M，由 Accel 和 Section 32 領投，加上 Prosus、Hitachi Ventures、Wipro Ventures、KPMG 等策略投資者
- 創辦人 Surojit Chatterjee：前 Coinbase CPO（帶領 2021 年 IPO）、前 Google VP（將 Mobile Ads 和 Shopping 做到數十億美元規模）
- 共同創辦人 Souvik Sen：前 Okta VP of Engineering，Google 反廣告詐騙 ML 系統 TrustGraph 負責人
- 2025 年 7 月營收達 $15.2M
- 出 stealth 後客戶數三倍增長，加入 Microsoft Pegasus Partnership Program
- 員工 51-200 人

**核心技術：**
- **EmaFusion™**：專利模型，結合 100+ 公開和私有 LLM，為每個任務選擇最高精度、最低成本和延遲的組合
- **Generative Workflow Engine™**：自動生成工作流程和編排程式碼，選擇合適的 agents 和設計模式
- 200+ 預建 connectors 整合企業內部數據源
- 支援 on-premise 部署和 air-gapped 環境
- 符合 SOC2、ISO 27001、ISO 42001、EU AI Act、GDPR、HIPAA、NIST

**使用場景：** 客服、HR、法務合規、銷售、資料工程、醫療前授權、保險理賠等。藥劑師使用 Ema 加速藥物審批流程，合規分析師用來確保法規遵循。

---

## 兩者比較

| | **Stack AI** | **Ema AI** |
|---|---|---|
| **定位** | AI Agent 建構平台（工具） | Universal AI Employee（產品化員工） |
| **核心差異** | 給你工具自己建 agent | 直接給你「AI 員工」來用 |
| **技術路線** | 連接各家 LLM + 拖拉式 canvas | 自有 EmaFusion™ 融合 100+ 模型 |
| **融資** | $16.6M | $61M |
| **營收** | 未公開 | $15.2M（2025 年 7 月） |
| **團隊規模** | ~13 人 | 51-200 人 |
| **創辦人背景** | MIT PhD（機器人/AI 學術） | Google VP + Coinbase CPO（大企業產品） |
| **目標客戶** | 中大型企業技術團隊 | 大型企業非技術用戶 |
| **合規認證** | SOC 2, HIPAA, GDPR | SOC 2, ISO 27001, ISO 42001, EU AI Act, HIPAA, GDPR, NIST |
| **策略投資者** | Vercel CEO, Weaviate CEO | KPMG, Wipro, Hitachi, Microsoft Pegasus |

---

## 跟你的 Compliance Context Infra 的關係

這兩家跟之前分析的垂直 AI 公司（Cranston、Rillet、Denki）不同——它們是**水平的 AI Agent 平台**，跨越多個行業和功能。但這反而讓它們跟你的定位更有意思：

**1. Stack AI = 你最直接的潛在客戶類型之一**

Stack AI 讓企業用 no-code 方式建 AI agent。但當這些 agent 被用在合規場景（KYC、監管申報、稽核報告），agent 需要知道「法規要求什麼」。Stack AI 平台本身**不提供合規知識**——它提供的是建構和編排能力。你的 Compliance Context API 正好可以成為 Stack AI agent 調用的**外部知識源**。

**2. Ema AI = 你更難賣進、但價值更高的目標**

Ema 自己建了很重的合規層（ISO 42001、EU AI Act、NIST 全都拿了）。它的 EmaFusion 模型也有能力自己處理合規邏輯。但隨著 Ema 擴展到更多產業和國家，每個新法規領域（稅務、勞動法、金融監管、醫療合規）都需要重建知識。Ema 的策略投資者包括 KPMG——這代表四大會計事務所已經在押注 AI agent 用於合規。

**3. 平台 vs 垂直 = 你的兩種 GTM**

```
垂直 AI 公司（Cranston, Rillet, Denki）  →  深度整合，成為他們的合規引擎
水平 AI 平台（Stack AI, Ema）             →  成為他們 marketplace 裡的合規模組
```

Stack AI 這類平台的 agent 每次處理合規任務，都需要即時查詢「這個行業、這個地區、這個交易類型的法規是什麼」。你的 API 可以成為他們 **100+ connectors 裡的第 101 個**——但這一個特別有價值，因為合規知識是高黏性、高頻更新的。

**4. 關鍵洞察：KPMG 同時投資 Ema 也是合規 AI 的推手**

KPMG 投資 Ema 是其在 AI agent 領域的整體策略一部分。這意味著四大正在把合規服務從「人力密集」轉向「AI agent 密集」。但 KPMG 自己建合規平台、又投 Ema 做通用 agent——中間缺的就是**結構化的合規知識 API**。

---

**更新後的生態系分層：**

```
┌─────────────────────────────────────────────┐
│  Ema AI / Stack AI                           │ ← 水平 AI Agent 平台
│  "我能做任何工作，但我不懂法規"                │
├─────────────────────────────────────────────┤
│  Cranston / Artifact                         │ ← AI 事務所（做服務）
├─────────────────────────────────────────────┤
│  Rillet                                      │ ← AI ERP 平台（取代系統）
├─────────────────────────────────────────────┤
│  Denki / Oxus                                │ ← AI 稽核（確保正確）
├─────────────────────────────────────────────┤
│  Rima AI                                     │ ← 文件自動化（數據提取）
├─────────────────────────────────────────────┤
│  ❓ 你的 Compliance Context Infra ❓          │ ← 合規知識層
│  "告訴所有人法規是什麼、怎麼遵守"              │
└─────────────────────────────────────────────┘
```

**水平平台加入後，你的 TAM 大幅擴大。** 不只是垂直 AI 公司需要合規知識——每一個在合規場景中運行的通用 AI agent 都需要。Stack AI 和 Ema 的客戶覆蓋金融、保險、醫療、法律、國防……每個產業的 agent 都需要各自的合規上下文。

繼續分析下一批？

---
---
---

這家非常有意思。

---

## Cumbuca — 巴西 Open Finance 監管代理（YC W25）

**做什麼：** 巴西 Open Finance 和 Pix 生態系統的第一個「監管代理」（regulatory proxy）。提供直連巴西央行的 bare-metal 基礎設施，讓國際金融科技公司在 Cumbuca 的支付牌照下建構自己的產品，不需自己花數年申請牌照。

**核心概念：** 你想進入巴西市場做支付，原本只有兩條路：等數年拿自己的牌照、或把控制權交給第三方 BaaS/PSP 中間商。Cumbuca 提供第三條路——客戶在 Cumbuca 的支付發起牌照（PISP）下建構自己的基礎設施，保留完整操作自主權，由 Cumbuca 處理合規。

**關鍵數據：**
- 成立 2021 年，São Paulo，5 人團隊
- CEO Daniel Ruhman 申請了 8 次 YC 才被錄取
- 總融資 $4.12M，投資者包括 Lightspeed Venture Partners 和 Supera Capital
- Lightspeed 在巴西唯一的投資
- 三位創辦人在 2022 年取得牌照時，是巴西金融業最年輕的法定董事之一
- 前 B2C 產品（共享帳戶 app）曾成長到超過 100 萬帳戶，後關閉轉向 B2B

**創辦人背景：**
- Daniel Ruhman（CEO）：14 歲發布第一個 iPhone app，在 UC Berkeley 短暫就讀認知科學後輟學創業。經歷過打工經濟平台、Pix 原生新銀行（Comadre）、共享帳目 app 多次 pivot
- Bruno Cury & Pedro Castilho：共同創辦人，金融監管領域深度經驗
- 核心團隊包括 Gustavo Lino（前巴西支付交易發起者協會 INIT 主席）和 Nic Marcondes（巴西 Open Finance 框架的關鍵架構師）

**產品架構——極度聰明的設計：**

關鍵洞察：Cumbuca 不建「Cumbuca API」（那會強加自己的抽象層），而是建一個最小化監管層。客戶直接對 Open Finance 和 Pix 的官方規格開發。當客戶準備好申請自己的牌照時，只需把 Cumbuca 的憑證換成自己的。

這意味著：
- 零 vendor lock-in
- 客戶永遠不會被 Cumbuca 中斷服務
- 客戶是在建自己的基礎設施，不是租用 Cumbuca 的

**商業模式：** 監管代理 / Compliance-as-Infrastructure。收費模式是讓客戶在 Cumbuca 牌照下運營的授權費用。首年 B2B 運營目標是簽下 10 個大客戶。

---

## 🔥 這是你見過最接近你的架構概念的公司

Cumbuca 對你的 Compliance Context Infrastructure 論文有**極高的戰略意義**，原因如下：

**1. Cumbuca = 「合規代理」在支付領域的具體實現**

你的想法是：建一個合規知識層，讓所有 AI 公司可以調用「法規要求什麼」。Cumbuca 做了一個非常類似但更窄的事——在巴西支付領域，它建了一個**監管代理層**，讓所有金融科技公司可以直接操作而不用自己處理合規。

| | **Cumbuca** | **你的 Compliance Context Infra** |
|---|---|---|
| **核心功能** | 監管牌照代理 | 監管知識 API |
| **客戶得到什麼** | 在別人牌照下合法運營 | 即時獲知法規要求 |
| **解決什麼痛點** | 「拿牌照要等好幾年」 | 「建合規邏輯要花幾個月」 |
| **客戶類型** | 想進入巴西的國際金融公司 | 需要合規知識的 AI 公司 |
| **Lock-in 策略** | 零 lock-in（可帶走） | 低 lock-in（知識層非綁定） |
| **地域範圍** | 巴西限定 | 跨國跨領域 |

**2. Cumbuca 證明了「合規作為基礎設施」這個商業模式可行**

Lightspeed 投了它，而且是 Lightspeed 在整個巴西的唯一投資。這代表頂級 VC 認為**把合規包裝成基礎設施賣給其他公司**是一個值得押注的商業模式。

**3. Cumbuca 的「最小化監管層」哲學 = 你應該學的設計原則**

Cumbuca 刻意不建「Cumbuca API」，而是讓客戶對官方規格開發。這避免了 vendor lock-in，也讓客戶更願意採用。你的 Compliance Context API 可以借鏡：

- 不要建「你的合規標準」→ 而是結構化呈現官方法規
- 不要鎖住客戶 → 而是讓客戶能隨時切換到自建
- 提供價值在「即時性」和「正確性」→ 不在「獨佔性」

**4. Cumbuca 也可能是你的合作夥伴或客戶**

Cumbuca 處理的是巴西支付的監管牌照代理，但它的客戶還需要知道：具體合規要求是什麼？多國金融法規怎麼對接？反洗錢規則在不同司法管轄區有什麼差異？這些**合規內容知識**正是你能提供的。

---

**更新生態系分層——加入 Cumbuca 的新維度：**

```
┌─────────────────────────────────────────────┐
│  Ema AI / Stack AI                           │ ← 水平 AI Agent 平台
│  "我能做任何工作，需要合規知識"                │
├─────────────────────────────────────────────┤
│  Cranston / Artifact / Rillet                │ ← 垂直 AI 公司（會計/ERP）
│  "我自動化特定領域，內建合規"                  │
├─────────────────────────────────────────────┤
│  Cumbuca                                     │ ← 監管代理（Regulatory Proxy）
│  "我讓你合法運營，處理牌照合規"                │
├─────────────────────────────────────────────┤
│  ❓ 你的 Compliance Context Infra ❓          │ ← 合規知識 API
│  "我告訴所有人法規是什麼、怎麼遵守"            │
└─────────────────────────────────────────────┘
```

Cumbuca 處理的是**「你能不能合法做這件事」（牌照/授權）**，你處理的是**「你該怎麼做才合規」（知識/規則）**。兩者互補，不衝突。

**目前已分析：35 家公司。** Cumbuca 是到目前為止跟你的商業模式最具結構性相似度的一家。繼續？


---
---
---


資料齊了。三家都是物流 AI，非常有趣的集群。

---

## Prox — 3PL 後勤 AI 數位同事（YC S25）

**做什麼：** 為 3PL（第三方物流）和 fulfillment center 建構「數位同事」，自動化後台作業層——理賠處理、發票對帳、追蹤承運商等燒掉數十億勞動小時的工作。

**關鍵數據：**
- YC S25 batch，2 人團隊，2025 年成立
- 創辦人 Gregory Makodzeba 和 Dima Yanovsky，童年朋友，都在家族倉庫長大
- Gregory 之前在 Pulley（YC W20）建構內部和客戶面向的 AI agents
- Dima 創辦了 Rektoff（保護超過 $1000 億資產的安全系統，客戶包括 Solana），曾在 Runtime Verification 領導 DevRel（客戶含 NASA、Boeing）

**產品定位：** 非常早期，專注 3PL 倉儲的後台自動化。深度理解物流作業的本體論（ontology），因此能在數天內而非數月內建好整合。

---

## Pallet — 物流 AI 作業系統（YC + Bain + General Catalyst）

**做什麼：** AI 物流軟體，旗艦產品 CoPallet 自動化物流後台作業（接單、報價、入口網站更新），比傳統人力快 10 倍、成本降一半。

**關鍵數據：**
- 總融資 $50M
- $27M Series B，General Catalyst 領投，Bain Capital Ventures、Activant Capital、Bessemer 跟投
- 天使投資人包括 Dan Lewis（Microsoft CPO、Convoy 共同創辦人）、Amit Agarwal（前 Datadog 總裁）、Girish Rishi（前 BlueYonder CEO）
- CEO Sushanth Raman 是 Retool 早期工程師，共同創辦人 Andrew Spencer 也是 Retool 工程師，兩人家族都在物流業
- Series A 時已有約 60 個客戶，$3M ARR

**產品：**
- CoPallet 自動化任何重複性物流工作流程——接單、入口更新、報價、貨物追蹤、文件解析
- 讀取進來的運輸指令，跨模式分配貨物（海運、鐵路、最後一哩），管理承運商、拖車、倉庫之間的交接
- 一家中型承運商重新分配了 25 名做重複資料輸入的員工，省下數百萬美元

---

## HappyRobot — 物流 AI 語音作業系統（YC S23 + a16z）

**做什麼：** 為「實體經濟」建構 AI 原生作業系統，結合即時數據、專業 AI 工作者和編排智能，自主管理複雜的關鍵任務。從供應鏈和工業規模運營開始。

**關鍵數據：**
- $44M Series B，Base10 Partners 領投，a16z、Array Ventures、Samsara Ventures、Tokio Marine 等參投。總融資 $62M。
- Series A 才剛完成 10 個月就關了 Series B
- 營收超過 $10M
- 70+ 企業客戶，包括 DHL、Ryder、Schneider、Werner
- YC S23，創辦人是三個西班牙人：Pablo 和 Javi Palafox 兄弟 + Luis Paarup。Pablo 在 TU Munich 做電腦視覺 PhD，Meta Reality Labs 實習。Javi 曾任 $3 億消費品牌 CFO

**產品——獨特的語音 AI 切入點：**
- 建構 AI agents 來自動化物流行業的電話通話——從與卡車司機的簡單確認通話到企業間的合約價格談判
- 預約排程從一週縮短到 30 分鐘以內；催收帶來超過 100 倍回報；外呼銷售 ROI 超過 19 倍；承運商銷售帶來 5 倍回報
- AI 同時流利西班牙語，在跨境物流中有巨大優勢
- Bridge 平台：集中化的載貨管理和工作流程執行控制面板

---

## 三家比較

| | **Prox** | **Pallet** | **HappyRobot** |
|---|---|---|---|
| **YC Batch** | S25（極早期） | 非 YC，但 YC 級投資人 | S23 |
| **融資** | YC seed | $50M | $62M |
| **切入點** | 3PL 後台（理賠、發票） | 全物流後台（接單、報價） | 語音通話（銷售、追蹤） |
| **AI 模式** | 數位同事 | AI 作業系統（CoPallet） | AI 工作者 + 語音 |
| **客戶規模** | 極早期 | 60+ 客戶 | 70+ 企業（DHL、Ryder） |
| **投資人** | YC | General Catalyst、Bain、Bessemer | Base10、**a16z**、Samsara |
| **團隊** | 2 人 | ~中型 | 快速成長 |
| **獨特優勢** | 倉庫原住民 DNA | Retool 背景，數據整合強 | 語音 AI + 西語能力 |

---

## 跟你的 Compliance Context Infra 的關係

這三家全在物流 AI 領域，物流是一個**合規密集度極高但數位化極低**的產業。

**1. 物流合規的複雜度被嚴重低估**

物流涉及的合規領域包括：
- **海關合規**：進出口申報、HS 編碼分類、原產地規則
- **運輸法規**：FMCSA（美國聯邦汽車運輸安全管理局）、DOT 規定、駕駛時間限制
- **關稅法規**：現在因為 Trump 關稅政策劇烈變動
- **危險品法規**：HAZMAT 運輸規則
- **跨境貿易合規**：制裁篩查、出口管制
- **保險合規**：承運商保險要求、貨物保險

每一筆貨運都可能觸及多個合規要求，而且**法規在頻繁變動**（尤其關稅政策）。

**2. 三家公司的合規處理方式：都是內建、碎片化的**

- **Pallet**：CoPallet 自動化接單和報價，但當法規要求改變（例如新關稅讓報價邏輯改變），需要人工更新規則
- **HappyRobot**：AI 語音 agent 跟承運商談判價格，但不知道最新的承運商資格合規要求（FMCSA 狀態、保險有效性）
- **Prox**：自動化理賠處理，但理賠是否合規需要對照運輸法規

**3. 你的 API 在物流場景的具體用途：**

```
物流 AI Agent 問你的 API：
→ "這批貨從深圳到洛杉磯，HS 編碼 8471.30，目前適用什麼關稅稅率？"
→ "這個承運商的 FMCSA 授權狀態是什麼？保險是否有效？"
→ "HAZMAT Class 3 液體的跨州運輸需要什麼文件？"
→ "新關稅政策下，這個品類的進口稅率有沒有變化？"
```

**4. 關稅是殺手級使用場景**

Pallet 的 CEO 說：「隨著關稅推高各方面成本，ROI 非常明顯，我們最大的挑戰變成了跟上需求。」

這意味著關稅變動正在加速物流 AI 的採用。但**關稅法規極度不穩定**——你的 Compliance Context API 如果能即時反映關稅政策變動，對每一家物流 AI 公司都是關鍵基礎設施。

---

**更新生態系分層——加入物流 AI 集群：**

```
┌──────────────────────────────────────────────────┐
│  水平 AI Agent 平台                                │
│  Ema AI / Stack AI                                │
├──────────────────────────────────────────────────┤
│  垂直 AI：會計/ERP                                 │
│  Cranston / Artifact / Rillet / Denki / Oxus      │
├──────────────────────────────────────────────────┤
│  垂直 AI：物流                          ← 新增！   │
│  Pallet ($50M) / HappyRobot ($62M) / Prox        │
├──────────────────────────────────────────────────┤
│  垂直 AI：保險                                     │
│  Xpanceo / 其他保險 AI                             │
├──────────────────────────────────────────────────┤
│  監管代理                                          │
│  Cumbuca（巴西支付牌照代理）                        │
├──────────────────────────────────────────────────┤
│  ❓ 你的 Compliance Context Infra ❓                │
│  會計合規 + 物流合規 + 保險合規 + 支付合規 = 統一 API │
└──────────────────────────────────────────────────┘
```

**物流 AI 是你的第二大垂直市場機會**（僅次於會計/金融）。三家公司加起來 $112M+ 融資，證明市場已被驗證。而且物流合規因為關稅戰正在變得更複雜、更需要即時更新——完美符合你的 API 價值主張。

**目前已分析：38 家公司。** 繼續？