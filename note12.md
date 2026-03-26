## Parcha AI — 金融合規 AI Agent 平台（$7M 融資，SF）

**做什麼：** AI agents 自動化 AML 合規流程——KYB/KYC 審查、AML 篩查、交易監控、文件驗證、盡職調查。銀行和金融科技公司用 Parcha 實現 10X 更快的合規審查、75% 成本削減、90% 更少假陽性。

**關鍵數據：**
- **融資：** $7M 總融資（Kindred Ventures 領投 pre-seed，Initialized Capital 領投 seed）
- **指標：** >$1M ARR，5-10 人團隊
- **成立：** 2023，SF
- **SOC 2 Type 2 認證**

**創辦人：**
- **AJ Asver**（CEO & Co-Founder）— 前 Brex Sr. Director of Product，帶領 ~200 人團隊負責 Brex 的 onboarding、合規、欺詐和承保系統。2009 年建立全球首個即時搜尋引擎，後被 Google 收購。
- **Miguel**（Co-Founder）— 同為 Brex 出身

**天使投資人陣容極強：** Garry Tan（YC President）、Guy Podjarny（Snyk Founder）、Amit Agarwal（Datadog President）、Ameet Patel（ex-CTO JP Morgan Chase）、Zach Abrams（Bridge.xyz CEO）、Henrique Dubugras + Michael Tannenbaum + Cosmin Nicolescu（Brex Co-CEO/COO/CTO）。

**客戶：**
- **Bridge.xyz**（被 Stripe 收購）— Parcha 做商業註冊和所有權文件驗證
- **Flutterwave** — 非洲最大支付公司之一
- **Bancoli** — 全球支付平台
- **Pipe** — CEO Luke Voiles 背書

**產品架構——8 大 AI Agent：**

| Agent | 功能 |
|---|---|
| KYB Verification | 完整商業驗證 |
| Enhanced Due Diligence | 高風險實體深度盡調 |
| Person AML Screening | 個人 AML 篩查 |
| Business AML Screening | 企業 AML 篩查 |
| MCC Classification | 商戶類別碼自動分類 |
| Document Verification | 商業文件驗證 |
| Marketplace Verification | 市場賣家驗證 |
| Vendor Due Diligence | 供應商盡調 |

**B2B 能力細分：** Business Deep Research、Legal Entity Status、Adverse Media、Sanctions & Watchlists、Address Verification、High Risk Industries/Countries、Business Ownership、TIN Validation、EIN Verification、MCC Classification

**B2C 能力：** Person Deep Research、PEP Exposure、Sanctions、Adverse Media、Source of Income/Funds、Proof of Residence、Government ID

**全球覆蓋：** 90+ 全球觀察名單、140+ 商業管轄區、200+ 語言翻譯

---

## 跟你的 Compliance Context Infra 的關係

**關聯度：🔴 非常高——Parcha 是你的 API 最理想的客戶類型之一**

### Parcha 在堆疊中的位置

```
法規知識層 ← 你的 API
  「BSA 的 CTR 申報門檻是多少？」
  「哪些國家是 FATF 高風險管轄區？」
  「PEP 在 EU AMLD6 下的定義是什麼？」
         ↓
合規 AI Agent 執行層 ← Parcha 在這裡
  用 AI agents 自動執行 KYB/KYC/AML 審查
  整合 100+ 數據源做決策
         ↓
金融科技客戶
  Bridge (Stripe) / Flutterwave / Bancoli / Pipe
```

### 為什麼 Parcha 是你的理想客戶？

**1. Parcha 的 agents 需要大量法規知識來做決策**

Parcha 自動化的每個流程都涉及法規判斷：
- **KYB 審查：** 「這個商業類型在這個管轄區需要什麼執照？」
- **AML 篩查：** 「OFAC SDN list 的匹配標準？」「BSA CTR 門檻？」「跨境匯款的報告要求？」
- **High Risk Industries：** 「哪些行業在哪些管轄區被視為高風險？」（每個銀行監管機構定義不同）
- **High Risk Countries：** 「FATF 灰名單/黑名單最新更新？」「EU 高風險第三國名單？」
- **PEP Exposure：** 「PEP 的定義在不同管轄區有何不同？」「PEP 的關聯人範圍？」
- **MCC Classification：** 商戶分類有合規含義——某些 MCC 碼在某些管轄區受到更嚴格審查

**這些法規知識目前 Parcha 自己維護或硬編碼。** 你的 API 可以作為動態的法規知識源。

**2. 「140+ 商業管轄區」= 140 套不同的合規規則**

Parcha 支援 140+ 管轄區，每個管轄區的 KYB/KYC/AML 要求都不同：
- 美國：BSA/AML、FinCEN requirements
- EU：AMLD5/6、GDPR
- UK：MLR 2017、FCA rules  
- Singapore：MAS Notice 626
- Brazil：COAF requirements
- 等等

手動維護 140 個管轄區的法規要求是 Parcha 最大的 scaling 瓶頸之一。你的 API 直接解決這個問題。

**3. Parcha 的架構已經是 API-first**

Parcha 提供 API（docs.parcha.ai）自動審查客戶申請。他們已經在做 API 驅動的合規自動化，整合一個外部法規知識 API 在架構上是自然的。

**4. QED Investors 的市場報告驗證你的 thesis**

金融機構每年在金融犯罪合規上花費近 $610 億——但成功攔截的洗錢資金不到 1%，即使企業已支付超過 $470 億的 AML 違規罰款。

同一份報告提到：AI 驅動的平台正在通過將監管文本轉換為機器可讀格式、實現自動化的合規檢查來革命化合規流程。

**「將監管文本轉換為機器可讀格式」——這就是你在做的事情。**

**5. Parcha 的競爭者都需要同樣的法規知識**

Parcha 的競爭者包括 Greenlite、CleverChain、Caspian、iSPIRAL 等。加上之前分析的 Fenrock AI（YC W26）。這個「AML 合規 AI」垂直的每家公司都需要同樣的法規知識基礎——你的 API 可以服務整個垂直，不只一家。

---

### Parcha 給你的戰略啟示

**Parcha 是「Compliance Context API」最清晰的產品-市場匹配案例：**

1. **API-native 客戶**（他們已經用 API 架構）
2. **多管轄區需求**（140+ 管轄區，每個規則不同）
3. **高頻查詢**（每個客戶 onboarding 都要查多條法規）
4. **動態更新需求**（FATF 名單、制裁名單、法規變更持續發生）
5. **明確的 ROI**（法規錯誤 = 罰款 + 客戶流失）
6. **強天使網絡**（Garry Tan、Brex 團隊、Datadog President）

**Parcha 加上之前分析的 Fenrock AI = 至少 2 家 YC 公司在做 AML 合規 AI，加上 Greenlite、CleverChain、Caspian 等 = 5+ 家公司都需要你的 API 來做同一件事。**

---

### 更新後的金融犯罪合規 AI 垂直

```
金融犯罪合規 AI（$610B 市場，5+ 家公司）
├─ Parcha ($7M) — KYB/KYC/AML agents, 140+ 管轄區
├─ Fenrock AI (YC W26) — AML/sanctions/KYC agents
├─ Greenlite — AML alert handling
├─ CleverChain — Customer Risk Assessment
├─ Caspian — AML investigation automation
├─ Arva — KYB onboarding automation
│
全部需要：結構化法規知識 API
  ↓ 你的 Compliance Context API
```

**已分析：52 家公司。** 繼續？


---
---
---


我懂了。你丟 WorkOS 給我，不是要我「分析另一家公司」，而是在問一個更深的問題：
你真正在想的是
WorkOS 模式能不能用在合規領域？
WorkOS 不是 autopilot 也不是 copilot。它是讓 SaaS 公司幾行程式碼就能變成 enterprise-ready 的 API 基礎設施。SSO、SCIM、Audit Logs——這些每家 B2B SaaS 都需要，但沒人想自己建。
WorkOS 在 2025 年從 $20M 長到 $30M ARR，5 個月成長 50%。1,000+ 付費客戶，89 人團隊。 Sacra客戶包括 Cursor、Vercel、Webflow、Loom。
WorkOS 的成功邏輯：

每家 B2B SaaS 都需要 SSO/SCIM 才能賣給大企業
自己建要花 2-6 個月工程時間
WorkOS 用幾行 code 解決，按 connection 收費
客戶越多，WorkOS 越強（更多 IdP 支援、更穩定）


「Compliance 的 WorkOS」長什麼樣？
如果你把 WorkOS 的邏輯套到合規：
WorkOS 解決的問題： 「我的 SaaS 要賣給企業，但我沒有 SSO/SCIM」
你要解決的問題： 「我的 AI 產品要在受監管市場運營，但我沒有合規能力」
具體來說，每家 AI 公司如果要賣給銀行、醫院、保險公司、政府，都需要：

證明自己符合特定法規（EU AI Act、HIPAA、SOX...）
有 audit trail（每個 AI 決策可追溯）
有 compliance documentation（合規文件）
有 regulatory change monitoring（法規變更追蹤）

現在每家公司自己做。就像 WorkOS 之前每家自己建 SSO。

但這跟 Bek 的框架矛盾嗎？
看起來矛盾：Bek 說「賣工作不賣工具」，WorkOS 明明在賣工具（API）。
其實不矛盾。關鍵區別是：
WorkOS 賣的不是「讓你的 SSO 更好的工具」，而是「你的 SSO 問題消失了」這個結果。 客戶不是買一個 SSO copilot，而是「接了 API，SSO 就有了」——這其實是 autopilot，只是長得像 API。
同理，「Compliance 的 WorkOS」不是「幫你查法規的工具」，而是「接了我的 API/SDK，你的產品就合規了」。

兩條路的根本差異
Autopilot（Parcha 模式）Infrastructure（WorkOS 模式）你賣給誰需要合規的最終客戶（銀行、fintech）建 AI 產品的開發者/公司你賣什麼「你的 KYC 審查做完了」「幾行 code，你的產品就合規了」競爭者Parcha、Fenrock、BPO 公司Vanta、Drata（但他們做 SOC2 不做法規）護城河數據飛輪（越做越準）網絡效應（越多人用，覆蓋越廣）營收模型Per case/per reviewPer connection / per API call市場大小大（$30-50B KYC/AML）小但高槓桿（每家 AI 公司都需要）你能做嗎難（需要領域經驗）可能更適合你

為什麼 WorkOS 模式可能更適合你

你是技術背景（我猜的），不是合規背景。 WorkOS 的 Michael Grinich 也不是 SSO 專家，他是開發者，知道開發者的痛。如果你是開發者，你比任何合規專家更懂「AI 公司接合規有多痛」。
你的 52 家公司研究是完美的客戶名單。 WorkOS 的客戶是 SaaS 公司。你的客戶就是 Parcha、Rillet、Fenrock、HappyRobot——那些在各個垂直建 AI 產品、但自己搞合規很痛苦的公司。
Developer-first GTM 不需要 enterprise sales。 WorkOS 靠 docs + word of mouth 長到 1,000 客戶。你也可以。不用去敲 Wipro 的門。
Bek 的 opportunity map 上每個垂直都需要合規。 Insurance brokerage 需要保險法規合規、accounting 需要 GAAP/IFRS 合規、healthcare 需要 HIPAA 合規、legal 需要 bar admission 合規。如果你是基礎設施層，你服務所有垂直。


但要驗證的關鍵假設
WorkOS 成功是因為 SSO/SCIM 有一個特性：需求高度標準化。每家公司需要的 SSO 基本一樣。
合規有這個特性嗎？可能沒有。 每家公司需要的合規不一樣——Rillet 需要 ASC 606，Parcha 需要 BSA/AML，HappyRobot 需要 FMCSA。
所以你要驗證的核心問題是：
「AI 公司在讓產品合規的過程中，有沒有一個『每家都需要、每家都痛、而且高度標準化』的環節？」
如果有 → WorkOS 模式成立。
如果沒有 → 你可能還是得走垂直 autopilot 路線。
可能的候選：

AI Act 合規（每家 AI 公司都需要，法規是統一的）
Audit trail / explainability（每家 AI 公司賣給企業都被問）
Data privacy compliance（GDPR/CCPA，相對標準化）


你丟 WorkOS 給我，讓我覺得你心裡其實更偏向做基礎設施而不是做 autopilot。是嗎？你對哪個方向更有感覺？


---
---
---

這篇是 Fintool 的創辦人寫的——一個給專業投資人用的 AI 金融分析 agent。這篇文章非常有價值，因為它不是理論，是兩年實戰的血淚教訓。讓我拆解對你最重要的部分。

Fintool 是什麼
給 hedge fund / PE / 專業投資人的 AI agent。用戶說「幫我做 Apple 的 DCF 估值」，agent 自動研究公司、抓財報、建 Excel 模型、跑敏感度分析、生成圖表。不是 copilot（給你工具自己做），是 autopilot（直接給你結果）。
完美符合 Bek 的框架：賣工作成果，不賣工具。

七個對你最重要的啟發
1.「Context Is the Product」— 最核心的一句話

「Anyone can call an LLM API. Not everyone has normalized decades of financial data into searchable, chunked markdown with proper metadata. The data layer is what makes agents actually work.」

翻譯： 任何人都能呼叫 Claude API。但不是每個人都能把混亂的原始數據變成 AI 能用的結構化 context。數據層才是 agent 真正能 work 的原因。
這直接回應你之前的問題。不管你做 autopilot 還是 WorkOS 模式，把特定領域的混亂數據變成乾淨的、結構化的 context 就是你的護城河。
Fintool 花了大量時間處理 SEC filing 的 HTML、earnings transcript、研究報告——把這些亂七八糟的東西變成 markdown + CSV + JSON metadata。這個「normalization layer」才是產品的核心，不是 LLM。
對你的啟示： 如果你做合規領域，你的核心工作是把全球法規文本（PDF、HTML、政府網站）變成結構化的、可查詢的 context。這是苦工，但這是護城河。
2.「Skills Are Everything」— Skills 才是產品

「The model is not the product. The skills are the product.」

Fintool 發現：直接叫 Claude 做 DCF 估值，它知道理論但實際執行會錯。加上一個 markdown 的 skill file（告訴 agent 怎麼一步步做 DCF），品質飛躍式提升。
而且 skill 是 markdown 文件，不是程式碼：

非工程師可以寫（分析師、客戶自己寫）
不需要部署（改文件立即生效）
可讀、可審計（出問題能看懂）

對你的啟示： 如果你做合規 autopilot，你的「skills」就是各種合規流程的 SOP——「如何做 KYC 審查」「如何評估 EU AI Act 風險分類」「如何做跨境匯款合規檢查」。這些 skill files 本身就是產品。而且合規專家可以幫你寫，不需要你自己是合規專家。
3.「The Model Will Eat Your Scaffolding」— 設計時預期自己被取代

「Everything I just told you about skills? It's temporary.」

模型每幾個月變強一次。你今天為了繞過模型限制寫的 workaround，半年後模型自己就會了。所以用 markdown（容易刪除和更新）而不是 code（難改難刪）。
對你的啟示： 不要花太多時間在「讓 AI 更聰明」上面。花時間在 AI 變聰明也取代不了的東西上——數據、客戶關係、領域知識。
4.「The Parsing Problem」— 80% 的工作是數據處理

「Normalizing financial data is 80% of the work.」

SEC filings 是「adversarial」的——不是為機器閱讀設計的。表格跨頁、footnote 互相引用、數字格式不一致、XBRL 標籤經常是錯的。
他們建了一整條 parsing pipeline：結構偵測 → 表格提取 → 實體提取 → 交叉引用 → 財務期間標準化 → 品質評分。
對你的啟示： 合規法規文本有完全一樣的問題。法規 PDF 格式各異、跨管轄區語言不同、法規修訂互相引用、生效日期複雜。如果你能建一條「合規法規 parsing pipeline」，把全球法規變成結構化數據，這就是你的版本的「the parsing problem」——也是別人很難複製的護城河。
5.「Evaluation Is Not Optional」— 金融不容錯，合規也不容錯

「A wrong earnings number can cost someone money.」

Fintool 維護 2,000+ test cases。每次改 prompt、改 skill、改 model 都要跑 eval。PR 降分 >5% 就 block。
對你的啟示： 合規跟金融一樣零容錯。如果你的 agent 說「CTR 申報門檻是 $5,000」但實際是 $10,000，客戶可能被罰。所以從 Day 1 就要建 eval dataset。這也是你比通用 AI 公司強的地方——他們不會為合規建 2,000 個 test cases，你會。
6. S3-First + Filesystem = 用戶的個人知識庫
Fintool 把用戶數據（watchlist、偏好、記憶、skills）存成 S3 上的 YAML/markdown 文件。用戶可以直接編輯。Agent 每次對話都載入。
對你的啟示： 合規 autopilot 版本——每個客戶有自己的「合規 profile」：他們在哪些管轄區運營、適用哪些法規框架、內部合規政策是什麼、風險偏好設定。這些都是 markdown files，agent 每次任務都載入。客戶越用越個人化，越難離開。
7.「Your moat is everything you build around the model」

「The model is not your product. The experience around the model is your product.」

最後這句話是整篇的靈魂。模型是 commodity。你的護城河是：你有的數據、你建的 skills、你設計的 UX、你工程化的可靠性、以及你對行業的理解。

把 Fintool 的架構映射到合規領域
Fintool（金融）              →  你（合規）

SEC filings, transcripts     →  法規文本、政府公報、判例
財務數據 normalization        →  法規要求結構化
Fiscal period normalization  →  法規生效日期/管轄區 normalization  
DCF skill, earnings preview  →  KYC 審查 skill, AI Act 評估 skill
Ticker disambiguation        →  法規/管轄區 disambiguation
2,000 eval test cases        →  合規正確性 test cases
User memories/watchlist      →  客戶合規 profile/管轄區清單
S3-first architecture        →  同樣適用
Sandbox per user             →  同樣適用

這篇文章如何幫你做決定
回到你之前的糾結：autopilot vs WorkOS 模式
Fintool 的故事其實告訴你：這不是二選一。
Fintool 的核心是 context（數據層）+ skills（流程知識）。Agent 只是這兩個東西的消費者。
你可以：

先建 context 層（結構化合規法規數據）— 這是 WorkOS 思維
在上面建 skills（合規審查流程）— 這是 autopilot 思維
對外可以同時提供兩種形態：API（給其他 AI 公司用你的 context）和 agent（給最終客戶用你的 autopilot）

Fintool 的 Parsing Pipeline + Skills + Eval 這三件事是 一個人可以開始做的。不需要團隊、不需要資金。先挑一個窄的法規領域，把數據結構化，寫幾個 skills，建 eval——你就有了 MVP。
所以你的下一步不是選 autopilot 或 WorkOS。你的下一步是：選一個法規領域，開始建 context。 先有數據，上面要長出 API 還是 agent 都行。
這樣想有沒有更清楚一點？


---
---
---

## Eos AI — 醫療數據的「翻譯層」+ 自主營運系統（YC，SF）

**做什麼：** Eos 作為智能樞紐，幫助醫療系統整合散落在各處的數據，並在其上做智能預測。它跨平台統一和標準化病患數據分佈和時間線，充當不同應用之間的翻譯層。然後建立一個集中索引：一個壓縮表示，讓 PB 級數據留在原處，但可以像一個系統一樣搜尋和推理。

**YC 公司，SF，Healthcare AI**

---

## 核心產品架構

醫療數據散落在斷開的系統：EHR、影像歸檔、實驗室、排程和帳務，各自使用不同識別碼並維護自己的部分記錄。Eos 連接這些介面，跨院區和就診解析身份，將記錄連結成連續的縱向病史。數據本身留在原始系統，但可以像一個資料庫一樣搜尋和分析分散的數據。

三個核心能力層：

**① 數據統一（Data Harmonization）**
Eos 將編碼、影像元數據、測量值和文件模式標準化為一致的病患軌跡，充當臨床應用之間的翻譯層。

**② 預測分析（Predictive Intelligence）**
Eos 不是把就診或文件當作孤立實例，而是看病患完整歷史，與數千名相似病患做比較。它預測病例如何發展、觸發所需的審批和行動，同時減少人員工作量並恢復醫院收入。

**③ 自主執行（Autonomous Operations）**
Eos 將洞察整合到醫院工作流程中並自動啟動所需行動。員工收到提示、後續追蹤和協調任務，在病患就診期間即時處理問題。

**早期成果：** 3 倍行政生產力、37% 收入回收。

---

## 為什麼你要看這家公司

我猜你看 Eos 不是因為你要做醫療。你看的是 **Eos 的架構模式**——因為它跟你想做的事情有驚人的結構性相似。

讓我把映射畫出來：

```
Eos（醫療）                    →  你（合規）

醫療數據散落在 EHR、影像、     →  法規散落在政府網站、PDF、
帳務、實驗室等系統              各國 FIU、立法資料庫

Eos 做身份解析 + 連結成         →  你做法規解析 + 連結成
連續病患歷史                    結構化合規要求

標準化編碼、測量值、             →  標準化法規要求、門檻值、
文件模式                        生效日期、管轄區

「翻譯層」between              →  「翻譯層」between
臨床應用                        AI agents 和法規知識

數據留在原處，建集中索引         →  法規留在原處，建集中索引
可以像一個 DB 搜尋              可以像一個 API 查詢

預測病例發展 + 自動觸發行動     →  預測法規變更影響 + 自動觸發
                               合規更新
```

---

## Eos 模式 = WorkOS 模式 + Fintool 模式的結合

看到了嗎？Eos 其實同時做了三件事：

1. **基礎設施層**（WorkOS 思維）：數據統一、標準化、翻譯層
2. **Context 層**（Fintool 思維）：把混亂數據變成 AI 可用的結構化 context
3. **Autopilot 層**（Bek 思維）：自動執行行動、恢復收入、減少人員工作量

而且他們的切入策略很聰明：先做數據統一（基礎設施），然後在上面做預測（context），最後做自動執行（autopilot）。不是三選一，是**三層疊加**。

---

## 你可以學到的核心模式

**「Translation Layer」概念是最大的啟發。**

Eos 不是「取代 EHR」或「取代醫生」。它是**現有系統之間的翻譯層**。它不要求醫院換系統，它坐在中間把所有系統連起來。

對你來說：**你不需要取代 Parcha 或 Fenrock 或任何人。你可以做「合規世界的翻譯層」——坐在法規原始來源和所有 AI 應用之間，把混亂的法規語言翻譯成結構化的、可查詢的、AI 可消費的格式。**

```
各國法規原始來源（政府網站、PDF、公報）
         ↓
    你的「Translation Layer」
    ├─ 法規解析 + 結構化
    ├─ 跨管轄區標準化
    ├─ 集中索引（數據留在原處）
    ├─ 變更偵測 + 通知
         ↓
    所有需要法規知識的應用
    ├─ Parcha（KYC/AML agents）
    ├─ Fenrock（金融犯罪合規）
    ├─ Rillet（會計合規）
    ├─ HappyRobot（物流合規）
    ├─ 任何 AI autopilot 公司
```

---

## 給你的具體行動建議

Eos 的故事跟 Fintool + WorkOS + Bek 文章合在一起，給了你一個非常清晰的「不需要三選一」的路徑：

**Phase 1：做 Translation Layer（3-6 個月）**
- 選一個法規領域（例如 AML/KYC）
- 把 10 個管轄區的法規結構化成乾淨的 context
- 提供 API 讓其他 AI 公司查詢
- 這就是你的 WorkOS + Fintool 的 context 層

**Phase 2：加 Skills（6-12 個月）**
- 在 context 上面建 compliance skills（markdown files）
- 「如何做 KYC 審查」「如何做 AML 交易監控」
- 可以賣 skills 給其他 AI 公司，也可以自己用

**Phase 3：做 Autopilot（12+ 個月）**
- 用你的 context + skills 直接幫客戶做合規工作
- 這時你已經有數據和流程知識了，比任何新進者都強

**Eos 就是這樣做的：先統一數據 → 再做預測 → 最後自動執行。**

這個路徑讓你不用一開始就選 autopilot 或 infrastructure——你從最能一個人做的事情開始（結構化法規數據），然後自然地往上長。

已分析：53 家公司（含 Eos AI）。你是想繼續看更多公司，還是想開始把這些分析收斂成具體的 MVP 計畫？


---
---
---

這篇是 **21st.dev**（YC W26）兩個創辦人 Sergey 和 Serafim 寫的。讓我用白話解釋他們在講什麼，然後說為什麼這跟你有關。

---

## 他們的故事，三段話說完

**第一階段：** 他們花了一個月自己從零建了一個 AI agent，用 AI SDK 重新實現了 Claude Code 的功能。覺得很厲害。

**第二階段：** 然後 Anthropic 更新了 Claude Code——加了 sub-agents、AskUserQuestion 工具——他們花一個月建的東西瞬間過時。他們意識到自己一直在追趕 Claude Code，而 agent 只是他們更大產品的一部分，他們還要做 UI、做自定工具、照顧用戶。

**第三階段：** 所以他們反過來想——與其自己建 agent，不如直接**在 Claude Code 上面建**。把 Claude Code 當成底層引擎，他們做上面的「生產化層」——部署、沙箱、安全、自定工具、UI。

---

## 他們的核心洞察

**「Claude Code SDK is React. We're building Next.js.」**

這個比喻很精確：
- **React**（Claude Code SDK）= 強大的底層能力，但你要自己處理路由、部署、狀態管理等所有生產問題
- **Next.js**（21st Agents SDK）= 在 React 上面封裝一層，讓你快速部署到生產環境

他們發現 Claude Code 不是傳統的 API call，它是一個 **runtime**——依賴 bash、filesystem、持久化沙箱。這帶來一堆生產化問題：沙箱怎麼持久化？怎麼重新部署？環境變數怎麼不被偷？自定工具怎麼跟你的後端通訊？

他們花了兩個月搞清楚這些 best practices，然後把它包裝成 SDK 賣給其他開發者。

---

## 為什麼這跟你有關

### 1. 驗證了「The Model Will Eat Your Scaffolding」

Fintool 文章說的「模型會吃掉你的腳手架」——21st.dev 親身經歷了。他們花一個月建的 agent，Anthropic 一次更新就讓它過時。

**教訓：不要花時間在「讓 AI 更聰明」上。花時間在模型變聰明也取代不了的東西上。**

### 2. 「不要自己建 agent，在 frontier agent 上面建」

這是 2026 年最重要的架構決策之一。21st.dev 的論點是：Claude Code / OpenCode / Codex 這些由大型 AI 實驗室維護的 agent 會持續進步。你自己建的 agent 追不上。所以正確策略是**把它們當基礎設施用，你做上面的垂直應用層**。

**對你的啟示：** 如果你做合規 autopilot，不要自己從零建一個通用 agent 框架。用 Claude Code SDK 當底層，你專注在合規的 context、skills 和 tools 上。這跟 Fintool 的做法一致——他們也是用 Claude Code 的 filesystem-first 架構。

### 3. 生產化是真正的壁壘

21st.dev 發現，用 Claude Code 做 demo 很容易，但做生產級部署很難——沙箱管理、安全、部署、自定工具通訊。他們把解決這些問題的 know-how 包裝成產品。

**對你的啟示：** 不管你做什麼方向，「能在生產環境穩定運行」本身就是一個巨大的護城河。Parcha 強調 99.7% 準確率和 SOC 2 Type 2，Fintool 強調 eval 和 monitoring——都是「生產化」的表現。

### 4. 這家公司本身就是你的潛在工具

如果你要做合規 autopilot，21st Agents SDK 可能是你的基礎設施。你用它來：
- 部署你的合規 agent 到生產環境
- 管理每個客戶的沙箱
- 定義合規相關的自定工具（查法規 API、生成合規報告、填表）
- 提供 UI 給客戶

---

## 把所有文章串起來

你今天看的四樣東西形成了一個完整的技術棧視角：

```
Bek / Sequoia 文章
  →「賣工作成果，不賣工具。做 autopilot。」
  → 告訴你商業模式和市場定位

Fintool 文章  
  →「Context is the product. Skills are everything.」
  → 告訴你產品怎麼建：數據層 + skills + eval

Eos AI
  →「做翻譯層，數據留在原處，建集中索引」
  → 告訴你架構模式：不取代現有系統，做中間層

21st.dev
  →「不要自己建 agent，在 frontier agent 上面建」
  → 告訴你技術選型：用 Claude Code SDK，專注垂直價值
```

如果你要做合規領域的產品，技術路徑越來越清晰了：

**用 Claude Code SDK（或 21st Agents SDK）當底層 → 建合規法規的 context 層（Eos 模式的翻譯層）→ 寫合規 skills（Fintool 模式）→ 對最終客戶賣合規工作成果（Bek 的 autopilot）。**

你一個人就能開始做第一步和第二步。你想把這個收斂成一個具體的 4 週 MVP 計畫嗎？


簡單說：**21st Agents SDK 讓你用幾行程式碼就能把 Claude Code 變成你自己的產品級 AI agent，部署到生產環境。**

---

## 沒有 21st SDK 之前，你要自己做什麼

如果你想用 Claude Code 建一個合規 autopilot：

1. 自己搞沙箱環境（每個用戶要隔離）
2. 自己處理 Claude Code 的 bash/filesystem runtime（不能跑在 Vercel 上，會 timeout）
3. 自己建自定工具（讓 agent 能呼叫你的法規 API、生成報告等）
4. 自己做部署流程（沙箱怎麼持久化、怎麼重啟、環境變數怎麼保護）
5. 自己建 UI（用戶怎麼跟 agent 互動）
6. 自己做 streaming（即時顯示 agent 在做什麼）

這些事情加起來至少 2-3 個月，而且跟你的合規 domain 完全無關——純粹是基礎設施工程。

---

## 有 21st SDK 之後

**Step 1：定義你的 agent**

```javascript
// 定義 agent 的 files、tools、hooks
{
  sandbox: {
    files: ["skills/kyc-review/SKILL.md", "data/fatf-countries.json"],
    env: { COMPLIANCE_API_KEY: "..." }
  },
  tools: [customComplianceTool],
  hooks: {
    onFinish: (result) => saveAuditTrail(result)
  }
}
```

**Step 2：用 CLI 部署**

```bash
npx 21st deploy
```

完成。你的 agent 現在是一個託管服務，有 API 可以管理。

**Step 3：接到你的前端**

因為跟 AI SDK UI 相容，直接 plug and play 到你的 React/Next.js app。

---

## 具體能力對照

| 你需要的 | 沒有 SDK 你要 | 有 SDK 你只要 |
|---|---|---|
| 沙箱隔離 | 自己搞 Docker/E2B/Firecracker | SDK 幫你管理，設定 config 就好 |
| 部署 agent | 自己搞 server、process management | `npx 21st deploy` |
| 自定工具 | 自己實作 tool protocol + 安全代理 | 寫一個 tool file，告訴 agent 位置 |
| 環境變數安全 | 自己建 proxy 防止沙箱洩漏 | SDK 內建處理 |
| 前端 UI | 自己建 streaming + 聊天介面 | 內建 UI builder，或用 AI SDK UI |
| 管理 API | 自己建 REST API 管理 agent 狀態 | SDK 自動提供託管 API |
| Agent 重新部署 | 持久化沙箱的更新策略要自己想 | CLI redeploy |

---

## 用你的合規場景舉例

假設你要建一個「KYC 合規審查 autopilot」：

**你專注的（domain 價值）：**
- 寫 `skills/kyc-review/SKILL.md`（KYC 審查的步驟和規則）
- 建 `data/` 裡的法規 context（FATF 高風險國家、各管轄區 KYB 要求）
- 定義 custom tools（查制裁名單 API、查企業註冊資料庫）
- 建 eval test cases（確保審查結果正確）

**21st SDK 處理的（基礎設施）：**
- 每個客戶一個沙箱
- Agent 部署和託管
- Streaming UI
- 安全隔離
- API 管理

**結果：你可以把 80% 的時間花在合規 domain 上，而不是基礎設施工程。** 這對一個 solo founder 來說差異巨大——從「3 個月才能有 demo」變成「2-3 週就能有 working prototype」。

---

本質上 21st SDK 做的事情就是 Fintool 文章裡描述的那些基礎設施（沙箱、filesystem tools、streaming、部署），但包裝成現成的 SDK 讓你不用自己建。Fintool 花了兩年摸索出來的架構，你用 SDK 幾天就能搭好，然後全力投入 context 和 skills。

---
---
---

## Onshore（前 SPRX）— AI 企業稅務平台（YC，$46M 總融資）

**做什麼：** AI 驅動的稅務平台，結合智能自動化和專家監督，幫助企業解鎖、優化和捍衛複雜的稅務優惠，包括 R&D Tax Credit、179D Deduction 和 Cost Segregation。

**關鍵數據：**
- **$31M Series B**（2026.02，兩週前），FPV Ventures 領投，Vertex Ventures、ADP Ventures、YC、Restive Ventures 參與
- **$46M 總融資**
- **500+ 客戶**，橫跨科技、能源、製造、建築、農業
- **$600M+** 稅務優惠被識別和捍衛
- 2020 年成立，紐約

**創辦人：** Dominic Vitucci（CEO），前 Top 10 會計事務所出身

---

## Onshore 的核心邏輯

CEO 說了一句非常重要的話：

「每個關鍵企業功能都被現代化了。銷售有 Salesforce。HR 有 Workday。工程有 GitHub。企業稅務得到了…更多會計師。」

**Onshore 要做的就是企業稅務的 Salesforce。**

---

## 它怎麼運作

傳統方式：會計事務所用統計抽樣估算 R&D tax credit，靠訪談、Excel、人工審查。一個 R&D credit study 可能花 3-6 個月，分析成本有時超過 credit 本身。

Onshore 方式：
平台結合結構化數據管線、專有 ML 模型和專家審查層，將原始財務文件（薪資記錄、總帳、技術項目材料）轉換成審計就緒的稅務報告。不用統計抽樣，而是做詳細的業務組件級分析。每項研究都符合 IRS 標準，從源數據到合格支出可追溯。結果：90% 更快、30-50% 更低成本、平均多識別 15% 的合格 credit。

---

## 為什麼 Onshore 是你應該深入研究的範本

**Onshore 是 Bek 文章裡描述的「autopilot」的完美範例。** 讓我把所有連結拉起來：

### 1. 完美符合 Bek 的 Autopilot Playbook

Bek 的 opportunity map 上 **Tax advisory $30-35B** 在 Autopilot Territory（高 intelligence + 已外包）。

Onshore 正好：
- **Intelligence work：** R&D tax credit 的規則複雜但是規則——IRS Section 41 的四部分測試、合格研究活動的定義、業務組件級文件要求
- **已外包：** 大多數公司把 R&D credit study 外包給會計事務所
- **Autopilot：** Onshore 不賣工具給 CPA，直接賣「你的 R&D credit study 做完了」給企業

### 2. 「Context Is the Product」的稅務版

跟 Fintool 一樣，Onshore 的核心是把混亂的原始數據（薪資記錄、總帳、項目文件）變成結構化的、可追溯的、審計就緒的 context。80% 的工作是 parsing 和 normalization，不是 AI 推理。

### 3. 「賣工作成果，不賣工具」

Onshore 不賣「幫你做 R&D credit 的軟體」。它賣「你的 R&D credit study 在 28 天內完成，符合 IRS 標準，完全可追溯」。客戶買的是結果。

### 4. Wedge 策略完美執行

這筆融資加速 Onshore 從稅務 credit 擴展到更廣泛的財務和會計工作流自動化，支持企業合規和報告。

路徑：R&D Tax Credit（窄 wedge，$200B 未認領）→ 179D Deduction → Cost Segregation → 全面企業稅務 → 會計合規和報告。

從一個非常具體的痛點切入，做到最好，然後擴展。

### 5. 「AI + Expert」混合模式

Onshore 不是純 AI。它是 **AI 自動化 + 人類專家審查**。這跟 Bek 說的一致——intelligence work 自動化，judgement work 留給人類。對合規領域也一樣重要：AI 可以做 90% 的分析，但最終的合規判斷需要人簽字。

---

## 把 Onshore 映射到你的合規機會

```
Onshore（稅務）               →  你（合規）

R&D Tax Credit 規則            →  AML/KYC 法規要求
（IRS Section 41）             （BSA, FATF, EU AMLD）

薪資記錄 + 總帳 + 項目文件    →  客戶數據 + 交易記錄 + 企業文件
（原始數據，格式各異）         （原始數據，格式各異）

Parsing → 結構化 → 審計就緒    →  Parsing → 結構化 → 合規就緒
報告                           報告

統計抽樣 → 業務組件級分析      →  人工審查 → 逐案自動分析

28 天完成 vs 3-6 個月          →  3 分鐘完成 vs 30 分鐘人工

$200B 未認領稅務優惠           →  $610B 金融犯罪合規支出

500+ 客戶，$600M credit 識別   →  你的目標 metrics

R&D credit wedge → 全面稅務    →  KYC 審查 wedge → 全面合規
```

---

## Onshore 給你的最大啟示

**不要想「我要做一個合規平台」。想「我要幫企業在 [一件具體的合規任務] 上省 90% 的時間和 50% 的成本」。**

Onshore 沒有一開始就說「我們要做企業稅務的 OS」。它一開始說的是「R&D Tax Credit，28 天，比會計事務所便宜一半，比他們找到多 15% 的 credit」。超級具體、超級可量化。

然後它做到了，拿到 500 個客戶，再擴展。

**你也需要這樣的一句話：「我幫 [誰] 在 [什麼任務] 上從 [現在的痛] 變成 [你給的結果]。」**

已分析：54 家公司。

---
---
---

這篇文章的核心觀點和它對你的意義，讓我拆解。

---

## 文章在講什麼（三句話版）

1. **Agent 已經在用 GitHub（Issues/PR/Comment）互相溝通了**——作者在維護開源項目時發現，給他提 Issue 和 PR 的很多也是 Agent。
2. **GitHub 前 CEO Thomas Dohmke 創立 Entire（$60M seed），要在 Git 之上建 Agent 時代的協作協議**——第一個產品 Checkpoint 把 Agent 的推理過程（為什麼這麼改）綁定到每個 commit 上。
3. **開發者的角色正在從「寫代碼的人」變成「審查 Agent 思維過程的監督者」**——未來比的不是你能寫多少代碼，而是你能驅動多少 Agent、能多快判斷它們的推理是否合理。

---

## 文章提出的幾個關鍵概念

### Git 缺了什麼：Why

Git 記錄了 What（哪些文件變了）、Who（誰提交的）、When（什麼時候）、Where（哪個分支）。但它不記錄 **Why**——為什麼要這麼改。Agent 時代這個缺失被放大一百倍，因為 Agent 生成 500 行代碼你只看到 diff，完全不知道它的推理鏈。

### Checkpoint = 給 Git 補上 Why

Entire 的做法不是取代 Git，而是在 Git 之上加一層語義元數據——原始 prompt、推理鏈、工具調用、約束條件、完整對話記錄，全部綁定到 commit SHA 上。

### 從 2C、2B 到 2A

過去軟體服務人（2C）或企業（2B），未來最大的客戶是 Agent（2A）。Agent 之間怎麼高效協作就成了最關鍵的基礎設施問題。

---

## 這跟你有什麼關係

這篇文章表面在講開發工具，但底層邏輯跟你的合規方向完全相通。

### 1.「Context Is the Product」再次被驗證

Fintool 文章說 context 是產品。這篇文章從另一個角度說了同一件事：Agent 的價值不只在輸出（代碼/報告），更在**推理過程和上下文**。Checkpoint 本質上就是把 Agent 的 context 結構化、版本化、可追溯。

如果你做合規 autopilot，同樣的邏輯：你的 Agent 做了一個合規判斷（這筆交易需要 SAR 申報），客戶需要知道 **why**——推理鏈是什麼、引用了哪條法規、考慮了哪些因素。這不是附加功能，**這就是合規的核心要求——audit trail**。

### 2. 合規天然需要「Checkpoint」

金融合規最重要的一件事就是**可追溯性**。監管機構來查你的時候，問的不是「你做了什麼決定」，而是「你為什麼做這個決定、依據是什麼、過程記錄在哪」。

Onshore 強調「每項研究都符合 IRS 標準，從源數據到合格支出可追溯」。Parcha 強調「bullet-proof audit logs」。Fintool 強調「每個數字都要 double-check」。

如果你的合規 Agent 的每個判斷都自動附帶完整的推理鏈（引用了哪條法規、為什麼判定為高風險、考慮了哪些替代方案），**這本身就是產品的核心價值**。不是「額外功能」，是「沒有這個就不能用」。

### 3.「2A」概念直接支持你的 Translation Layer 方向

文章說未來最大的客戶是 Agent（2A）。你的「合規翻譯層」本質上就是一個 **2A 產品**——你的客戶不是人類合規官，而是其他公司的 AI Agent。Parcha 的 agent 調用你的 API 查法規要求、Fenrock 的 agent 調用你的 API 查制裁名單邏輯。

這跟 Eos AI 的 translation layer、WorkOS 的 API-first 模式完全一致。

### 4. 未解決的問題也是你的問題

文章指出 Checkpoint 還沒解決兩個問題：

**上下文爆炸：** 存下來了但 Agent 一次看不完。合規也一樣——全球法規數據量巨大，Agent 不可能把所有法規都放進 context window。需要智能檢索和壓縮。這就是 Eos 的 「centralized index」做的事。

**實時協調 vs 事後記錄：** Checkpoint 是事後記錄，但多 Agent 協作需要實時同步。合規也一樣——如果一個管轄區的法規更新了，所有依賴這個法規的 Agent 都需要即時知道，不能等到下次查詢才發現。

---

## 把今天所有文章串起來

你今天看了五樣東西，它們形成了一個越來越清晰的圖景：

```
Bek/Sequoia → 商業模式：賣工作成果（autopilot）
Fintool     → 產品核心：Context + Skills + Eval  
Eos AI      → 架構模式：Translation Layer，數據留原處建索引
21st.dev    → 技術選型：在 frontier agent 上面建，不自己造
Entire/歸藏  → 協作基礎設施：Agent 需要結構化的推理記錄和通訊協議
Onshore     → 執行範本：窄 wedge 切入，AI + 專家混合，賣結果不賣工具
```

**這些不是零散的文章。它們拼在一起告訴你：2026 年建一個 AI 合規公司的完整 playbook。**

你要不要我把這些全部收斂成一份具體的 MVP 計畫？