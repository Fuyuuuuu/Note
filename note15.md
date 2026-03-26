好問題。讓我從 59 家公司裡直接提煉出來。

## 產品型態

**① Copilot（人問 AI 答）**
人類提問，AI 回答合規問題。需要人類判斷和執行。
→ CannabisRegulations.ai、Norm AI（早期）、Regology

**② Autopilot（AI 直接做）**
AI 直接完成合規任務，人類審核結果。Bek/Sequoia 框架裡的核心模式。
→ Payna（幫你申請 50 州執照）、Brico（同上）、Medallion（醫療執照）、Eloquent AI（金融服務客服自動化）、Copperlane（抵押貸款流程）、Zolvo（商業貸款服務）、Parcha（KYC/AML 審核）

**③ API / Infrastructure（給其他軟體用）**
不面向終端用戶，而是給其他 AI 公司或軟體調用。
→ Checkr（背景調查 API）、Plaid 模式（你的目標方向）、Norm AI API（policy-as-code）

**④ Platform / OS（工作流平台）**
提供完整工作台，讓合規團隊在上面操作。
→ Complyance（$28M）、Abstract Security、Vulcan

**⑤ Translation Layer（翻譯層）**
坐在現有系統之間，不替換任何東西，只是讓它們互通。
→ Eos AI 模式、Cardamon（法規→義務→要求的結構化翻譯）

**⑥ Agent（端到端執行者）**
結合 Autopilot + 自主決策，可以跨系統操作。
→ Noetic（硬體合規：研究→文件→找實驗室，全自動）、Oddysee AI（大麻執照申請）

**⑦ Knowledge Hub / Context Layer（知識庫）**
結構化合規知識，供人或機器查詢。
→ Andrew Ng 的 Context Hub 概念、CyberContext AI、你的 Compliance Context Infrastructure 方向

7/5 

1/2/6

4

3

## 商業模式

**① 按任務收費（pay-per-task / credit-based）**
每完成一個具體任務收費。最接近「賣工作」。
→ Eloquent AI（按成功自動化的任務收 credit）、Checkr（按每次背景調查收費）、Parcha（按 KYC 審核量）

**② SaaS 訂閱（monthly/annual seat）**
按人頭或按公司收月費/年費。傳統模式。
→ Complyance、Regology、Abstract、Norm AI、CannabisRegulations.ai

**③ 項目制 ACV（Annual Contract Value）**
一次簽約，按年收大額合同。通常 6 位數起。
→ Payna（六位數 ACV，幾週內簽下）、Brico（企業合同）

**④ API 用量計費（usage-based）**
按 API call 數量或處理量收費。Infrastructure 公司的標準模式。
→ Checkr（按調查次數）、Reducto（按頁數）、Plaid（按連接數）

**⑤ 成功抽成（success-based / outcome-based）**
只有成功才收費。風險最低的定價方式。
→ Bek 框架裡的理想模式：不收「用軟體的費用」，收「完成工作的費用」

**⑥ 替代定價（vendor swap）**
直接替換客戶原本付給律師/顧問的費用。不是新增預算，是轉移預算。
→ Payna（替代法律事務所的 billable hours）、Brico（替代合規顧問）

## 產品型態 × 商業模式的組合

最值得注意的組合：



**Autopilot + 替代定價 = 最快變現。** Payna 的模式：客戶本來每年付律師事務所 $200K 做 50 州執照，Payna 收 $100K 用 AI 做同樣的事。客戶省錢，Payna 的 margin 比律師事務所高很多。不需要創造新預算。

**API + 用量計費 = 最大規模。** Checkr 做到 $800M revenue 就是這個模式。但需要先有大量客戶。冷啟動難。

**Agent + 按任務收費 = 最對齊的激勵。** Eloquent AI 4 週做到 $500K ARR，因為客戶只在 AI 成功完成任務時才付費。風險全在 Eloquent 這邊，所以客戶容易說 yes。



你在想哪個組合最適合你的起步？

---

---

---

可以。而且從你研究的公司裡看，**最成功的公司全部都在融合**。

## 已經在融合的公司



**Checkr** 就是最好的例子。它從單一 API（背景調查）起步，但實際上它同時是：API（給 Uber、Lyft 調用）+ Autopilot（自動完成調查流程）+ Platform（客戶有 dashboard 可以管理）。一開始只是 API，規模大了之後自然長出其他型態。

**Brico** 也是。對客戶來說是 Autopilot（幫你申請執照），對客戶的工程團隊來說是 API（接 NMLS），對合規主管來說是 Platform（追蹤所有州的執照狀態）。同一個產品，三個介面。

**Noetic** 更極端：Knowledge Hub（研究法規要求）+ Agent（自動產生文件）+ Platform（匹配實驗室）。三層融合成一個端到端流程。

**Eloquent AI** 表面是 Autopilot（自動處理客服任務），但底層是 Translation Layer（觀察 SOP 學習流程，坐在現有系統之間），商業模式是 credit-based 按任務收費。



## 融合的邏輯

不是隨便混在一起。有一個自然的演化順序：

**起點 → 擴張方向永遠是同一條路：**

從服務一個人的一個任務開始，然後沿著價值鏈往兩個方向擴張——往上游做知識層，往下游做執行層。

用你的情境來想：

**階段 1：Autopilot（進入市場最快）** → 幫客戶做一件具體的合規任務。比如「幫你搞定台灣某個特定執照申請」。 → 商業模式：替代定價（原本付顧問的錢）

**階段 2：+ Knowledge Hub** → 做著做著，你會累積大量結構化的合規知識。這些知識本身就是產品。 → 可以開放給客戶自助查詢，或打包成 API 給其他公司用。

**階段 3：+ API / Infrastructure** → 當你的合規知識夠結構化、夠標準化，其他 AI 公司可以直接調用。 → 商業模式加上用量計費。

**階段 4：+ Agent** → 當 API 夠穩定、知識夠完整，AI agent 可以端到端自主完成任務。 → 商業模式變成按成果收費。

## 關鍵洞察

**融合不是一開始的設計，是自然演化的結果。**

Checkr 不是一開始就想做「背景調查平台 + API + 自動化引擎」。它就是做背景調查 API，然後客戶需要 dashboard 所以加了 Platform，客戶量大了所以加了 Autopilot。

**但反過來——如果你一開始就嘗試同時做所有型態，你什麼都做不好。**

這就是你之前陷入的迴圈：想要同時建 Infrastructure + API + Agent + Platform，結果什麼都沒開始。

## 所以答案是

**融合是目標，但不是起點。**

起點是一個型態、一個任務、一個客戶。

你研究了 59 家公司，看到了所有可能的產品型態和商業模式。現在的問題只剩一個：**你的第一個型態 × 第一個任務 × 第一個客戶是什麼？**

---

---

---

資料量很大。讓我根據已有的 compacted summary 和這次搜尋結果，整理出完整的利基地圖。

根據我們所有對話中分析的 59+ 家公司和 Miro 資料，這是完整的利基和細分地圖：

---

## 一、已有玩家的利基（已驗證）

### 1. 金融服務合規

**最大、最擁擠的利基。**

細分：

- **KYC/AML/反洗錢** — Parcha、Fenrock AI (YC W26)、WorkFusion ($251M)、Fenergo、Lucinity、Sigma360、Oracle FCC、NameScan、ComplyAdvantage、NICE Actimize
- **金融執照（50 州）** — Brico ($21.6M)、Payna (YC W26)
- **消費貸款合規** — Shiboleth (YC)
- **商業貸款服務** — Zolvo (YC S26)
- **抵押貸款合規** — Copperlane (YC)
- **保險經紀合規** — Newfront (YC)
- **私募/PE 合規** — Zarna (YC F25)

### 2. 資安/GRC 合規

細分：

- **SOC2/ISO/HIPAA 自動化** — Complyance ($28M, GV)、Oneleet (YC)、Delve (YC)、Probo (YC)、Vanta
- **網站隱私合規** — Feroot Security ($14M) — PCI DSS 4.0.1、HIPAA、GDPR、CCPA、50+ 法律
- **AI 治理/合規** — LogosGuard (YC)
- **平台安全合規** — SafetyKit (YC)

### 3. 法規智能基礎設施（水平）

細分：

- **法規→AI 可消費格式** — Norm AI ($147M) — 決策樹 + LEAP 平台
- **全球法規數據庫** — Regology ($8.15M) — Smart Law Library™、跨行業
- **法規→知識圖譜** — Vulcan ($10.9M) — 美國法律本體
- **法規監測情報** — Abstract ($9M+) — 7M+ 法規記錄、145K+ 政府機構
- **合規自動化平台** — CyberContext AI — 跨行業 GRC

### 4. 醫療合規

細分：

- **醫療執照/認證** — Medallion ($85M+)
- **醫療合規自動化** — Readily (YC) — 減少 90% 法規分析時間
- **藥品法規寫作** — Ritivel (YC W26) — CTD、CSR、IND、BLA 自動生成

### 5. 硬體認證合規

細分：

- **安全認證** — Saphira (YC) — ISO 26262、ISO 10218、UL 508A
- **端到端硬體合規** — Noetic (YC) — FCC、FDA、CE、UL、ISO、FAA
- **自駕安全驗證** — Valgorithmic (YC)

### 6. 大麻合規

細分：

- **法規 AI chatbot** — [CannabisRegulations.ai](http://CannabisRegulations.ai) — 按州別
- **執照申請** — Oddysee AI — 100+ 大麻企業

### 7. 勞動/建設合規

細分：

- **勞動合規自動化** — Dili (YC S23) — 工資、學徒、聯邦資金合規，$1B+
- **全球薪資合規** — Deel、Craze (印度)

### 8. 房地產合規

細分：

- **房產稅+租賃法規+銀行合規** — Goldbridge (YC W26) — 房地產財務 OS

### 9. 會計/審計合規

細分：

- **AI 記帳合規** — Balance (YC W26)、FullSeam (YC W26)
- **內部審計自動化** — Oxus (YC)、Agentive (YC)

### 10. 供應鏈/物流合規

細分：

- **車隊合規** — Carma (YC) — $5.5M seed
- **商戶風險合規** — Ballerine (YC)、Coris (YC)

### 11. IP/專利合規

細分：

- **專利侵權監測** — Patent Watch（在 Miro 中出現）、Stilta (YC W26)

---

## 二、我們討論過但尚無 AI 原生玩家的空白利基

這些在之前的對話中被明確標記為「空白市場」：

- **保險代理人執照（50 州）** — Payna 模式但在保險
- **食品/飲料許可證** — 餐廳、食品卡車、酒牌
- **環境許可證** — 排放、水質、廢棄物
- **交通/物流許可證** — 貨運、危險物品
- **教育/培訓認證** — 學校、職業認證
- **跨境電商產品合規** — CE 標誌、FDA 產品註冊
- **APAC 金融執照** — 台灣、新加坡、日本、香港金融牌照

---

## 三、整理成矩陣

按「市場成熟度」×「競爭密度」排列：


|             | 低競爭                     | 高競爭                   |
| ----------- | ----------------------- | --------------------- |
| **大市場**     | 保險代理執照、APAC 金融執照、跨境電商合規 | KYC/AML、SOC2/ISO、金融執照 |
| **中市場**     | 房地產合規、藥品法規寫作、勞動合規       | 醫療執照、法規智能平台           |
| **小市場（長尾）** | 食品許可、環境許可、教育認證、交通許可     | 大麻合規、硬體認證             |


---

**左上角（大市場 + 低競爭）是你最甜蜜的切入點。** 特別是 APAC 金融執照——你在台灣，這是你的地理優勢，而且目前零 AI 原生玩家。

你想深入哪個象限？

---

---

---

## Panta — AI 原生商業保險經紀（YC W26）

**一句話：** OpenClaw 風格的 AI operators 跑在一排 Mac Mini 上，做幾千個保險經紀人的工作。

**這家公司極度重要。讓我解釋為什麼。**

### 做什麼

Panta 是一家持牌商業保險經紀公司，專門做 **Excess & Surplus (E&S) 市場**——也就是標準保險公司不願承保的高風險業務：武裝保全、爆裂物製造商、危險氣體設施、屋頂工、鋼鐵廠、危險貨物運輸。這個市場每年 $1250 億保費。

他們的 AI agents 不是賣軟體給經紀人，而是**自己成為經紀人**——在真實的文件系統、保險公司門戶、email、電話、PDF 裡操作，做人類經紀人做的每一件事。

### 為什麼這家公司驗證了你之前的框架

**Panta 完美體現了 Bek/Sequoia 的「Autopilot Territory」模式：**

Bek 的框架說保險經紀是 $140-200B 的 Autopilot 機會。Panta 就是在執行這個。他們的核心洞察跟 Bek 一模一樣：不要賣工具給經紀人讓他們快 10%，而是直接取代整個人類協調層。

**他們從「賣軟體」到「成為服務」的轉折：**

他們自己說：「我們花了好幾個月把 AI 工具賣給經紀人，然後才意識到行不通。所以我們不再賣軟體，直接成為經紀人。」這跟 Bek 說的「sell the work, not the tool」一模一樣。

### 核心數據

- 50 步驟的流程中，經紀人的判斷只佔 5%，其他 95% 是純粹的協調工作
- 一個人類經紀人的天花板是約 400 個客戶
- Panta 的目標是一個 AI operator 處理 4,000 個客戶——10 倍
- 12 月成立，已經在生產環境中綁定多張保單
- 案例：一家武裝保全公司被 6 個經紀人拒絕，Panta 的 agents 3 天內拿到可綁定報價，發了 60 封 email
- 3 人團隊，San Francisco
- YC Partner: Gustaf Alstromer

### 創辦人

**Vincent Chen（CEO）**— 前 Google ML 工程師，領導 Vertex AI 推薦模型、NotebookLM Enterprise、Google I/O 的 Ask Photos。

**Frank Wang（CTO）**— 前 Apple 資深工程師，建構 Gen-AI chatbot 和 Rust 基礎設施。Rust 和 Gleam 生態系 Top-10 開源貢獻者。

兩人高中就認識，都是持牌商業保險經紀人。自己親手做過爆裂物製造商、危險氣體設施等高難度保單。

### 技術架構——為什麼叫「OpenClaw」

他們在 OpenClaw 爆紅之前就建了類似架構：AI agents 操作在跟人類經紀人完全相同的系統裡——文件系統、保險公司入口網站、email、電話、PDF。不是 API 整合，是直接用 computer-use 操作現有系統。

### 跟你的 Compliance Context Infra 的關係

**關聯度：🔴 非常高——這是 Bek 框架裡最大的 Autopilot Territory**

Panta 的 AI agents 在做保險經紀工作時，需要大量合規知識：

**① 州級保險法規**

- E&S 市場在每個州的法規不同（surplus lines 稅率、filing 要求、eligible/non-eligible carrier 規則）
- 50 州 × 多種保險類型 = 巨大的法規碎片化
- 你的 API：`「加州 surplus lines 的申報要求和稅率是什麼？」`

**② 保險牌照合規**

- 經紀人必須在每個運營州持有牌照
- 跟 Payna/Brico 做的金融執照是同一個結構的問題
- 你的 API：`「在德州做 surplus lines broker 需要哪些牌照和 E&O 保險要求？」`

**③ 保單合規要求**

- 不同類別的風險（爆裂物、危險貨物）有不同的監管要求
- 聯邦 OSHA + 州級安全法規 + 行業特定法規
- 你的 API：`「武裝保全公司在紐約州需要的最低責任險額度是多少？」`

**④ 這直接連回你的空白利基**

之前我列的空白市場裡有「保險代理人執照（50 州）」。Panta 的存在證明了這個市場不只是需要執照自動化，更需要整個保險合規知識基礎設施。

### 更新後的生態系地圖

```
保險合規 AI（新類別，Bek 最大的 Autopilot Territory）
├── Panta (YC W26) — AI 原生 E&S 經紀，full-stack autopilot
├── Newfront (YC) — 現代保險經紀平台
└── 空白：保險代理執照自動化（Payna 模式在保險）

你的 API 在這裡的價值：
→ 為 Panta 的 agents 提供 50 州 surplus lines 法規
→ 為 Panta 的 agents 提供行業特定風險要求
→ 為 Panta 的 agents 提供保險牌照合規知識
```

**已分析：60 家公司。** Panta 是繼 Fenrock 之後第二個最直接的潛在客戶——一家做保險合規 autopilot 的 AI 公司，其 agents 每天需要查詢 50 州的保險法規。

---

---

---

好問題。「Consumer 合規」是一個被你找到的重要缺口。讓我整理我們討論過和搜尋到的所有消費者面向合規場景。

## Consumer 領域的合規——確實存在，但幾乎沒有 AI 原生玩家

### 已存在的（但主要是 B2B2C）

**消費者數據隱私合規**

- OneTrust ($2.1B 融資) — 但這是幫企業合規，不是直接面向消費者
- Feroot Security — 網站隱私合規（PCI DSS、CCPA、GDPR），保護的是消費者，但客戶是企業
- Ethena (YC) — 合規培訓（防騷擾、行為準則），但也是 B2B

**消費者金融保護合規**

- Shiboleth (YC) — 消費貸款合規自動化，幫金融機構遵守消費者保護法
- Greenboard (YC) — 金融公司合規計劃管理
- QED 投資人提到的：Azimuth 幫 Truist 銀行自動化消費者業務線的合規測試

**消費者廣告/行銷合規**

- Veriad (YC) — AI 合規官員，審查廣告是否合規和合法。這是最接近「consumer-facing 合規」的
- Norm AI — 也做行銷內容合規審查

### 真正的消費者合規空白地帶

目前**幾乎沒有人在做直接面向消費者的合規 AI**。但消費者面臨的合規痛點是巨大的：

**① 消費者權益/退款/索賠合規**

- 消費者想退貨，但不知道自己在不同州/國家的法律權利是什麼
- 航班延誤賠償（EU261 法規）、消費者保護法
- 目前有 AirHelp 類公司但不是 AI 原生

**② 租戶權利合規**

- 租客被房東欺負，不知道自己的權利
- 租金管制、驅逐保護、安全押金規則——每州不同
- Goldbridge 從房東端在做，但**沒有人從租客端做**

**③ 勞動者權利合規**

- 員工被解僱、被欠薪、被歧視——不知道自己的法律選項
- FMLA、ADA、Fair Labor Standards Act、各州勞動法
- 目前只有律師事務所在做（昂貴、慢）

**④ 移民/簽證合規**

- 簽證申請人需要知道自己的資格和流程
- H1B、O1、EB5 各有不同要求和時間線
- 目前 Boundless Immigration 等在做但不是 AI 原生

**⑤ 小企業主合規**

- 餐廳、電商、小店——需要知道自己需要哪些許可證、執照、稅務義務
- 每個城市/州/國家都不同
- 2025 年各州立法機關提出了超過 1,100 項 AI 相關法案，約 100 項州法律。對全國營運的企業來說，這造成了重疊且經常衝突的義務
- 單是加州的隱私和網路安全要求就可能對小企業施加每年近 $16,000 的合規成本

**⑥ AI 使用合規（新興）**

- 各州對「AI」、「高風險」和「重大決定」的定義不同，要求企業在多個框架下分析同一系統
- 消費者有「被 AI 做決策」時的知情權和反對權
- 幾乎沒人幫消費者理解和行使這些權利

**⑦ 電商跨境合規（消費者端）**

- 消費者從海外購物的關稅、進口限制、退貨權利
- 跨境電商賣家需要的產品合規（CE 標誌、FDA）

### 為什麼 Consumer 合規是空白

**因為付費模式難。** B2B 合規很明確——企業不合規會被罰款，所以願意付錢。消費者不合規不會被罰，只是「不知道自己的權利」，付費意願低。

成功的 consumer 合規模式通常是：

- **成功抽成**：AirHelp 幫你拿到航班賠償，抽 25%
- **訂閱制**：Boundless Immigration 收會員費幫你追蹤簽證狀態
- **嵌入 B2B2C**：幫企業做合規，間接保護消費者（OneTrust 模式）

### 對你的意義

Consumer 合規跟你的 API 基礎設施方向有一個有趣的連接：

**如果有人做「消費者合規助手」——比如一個 AI 幫租客知道自己在每個州的權利——那個 AI 需要從哪裡獲取法規知識？**

答案就是你的 API。

所以 consumer 合規不是你直接做的利基，但它是你 API 的另一類潛在客戶——consumer-facing 的 AI 應用。

你問這個問題是在想什麼方向？

---

---

---

HVAC 合規確實存在，而且是一個被嚴重低估的領域。但目前 AI 公司主要在做 HVAC 的**營運效率**，幾乎沒有人專門做 HVAC **合規**。

## HVAC 領域的 AI 公司（已有）

**Rebar** — 剛拿到 $14M Series A，為商業 HVAC 供應商用 AI 生成報價，速度快 60-70%。2026 年前六週 ARR 翻倍，40 個客戶，估值 $450M。但這是報價工具，不是合規。

**Netic** — $23M Series B，估值 $450M，收入不到一年增長 2,100%。做 HVAC、水電、屋頂等家庭服務公司的 AI 營收引擎。也不是合規。

**BrainBox AI** — 商業建築 HVAC 系統 AI 優化，減少能耗 25%。有合規元素但主要是能源效率。

**ServiceTitan / Housecall Pro / FieldEdge** — HVAC 業務管理軟體平台。有一些合規功能但不是核心。

## HVAC 合規的具體痛點（沒有 AI 原生玩家）

**① 技師執照和認證合規**

- HVAC 技師需要 EPA Section 608 認證（制冷劑處理）
- 各州有不同的承包商執照要求
- AI 可以追蹤員工認證、保險續期和必要的安全表格，在到期前自動發送提醒，標記缺失文件
- 但目前沒有專門做這個的 AI 公司

**② 制冷劑法規合規**

- EPA 法規持續收緊（AIM Act、HFC phase-down）
- 不同制冷劑有不同的處理、回收、記錄要求
- 2025-2030 年 HFC 配額持續削減，每年規則都在變
- 碎片化程度高：聯邦 EPA + 各州環保局 + CARB（加州）

**③ 建築法規合規**

- HVAC 安裝必須符合當地建築法規
- International Mechanical Code (IMC) 是基礎，但各州/市有修改
- 能源法規：IECC、ASHRAE 90.1、Title 24（加州）
- 每隔幾年更新一次，各地更新節奏不同

**④ 環境合規**

- 在生物醫學設施中，HVAC 系統必須維持嚴格標準以支持研究、病患護理和法規合規
- 室內空氣品質法規（OSHA、EPA）
- 排放標準和報告要求

**⑤ 安全合規**

- OSHA 工作場所安全要求
- 密閉空間進入、電氣安全、高空作業
- 各州額外的安全法規

**⑥ 許可證和檢查合規**

- 每個 HVAC 安裝/維修項目可能需要建築許可
- 不同城市/縣有不同的許可要求和費用
- 檢查排程和通過標準

**⑦ 合規工具也正在轉向無紙化流程，使滿足環境法規更容易，而不需要實體表格**

## 為什麼這很有趣

HVAC 合規是你之前利基矩陣裡「小市場 + 低競爭」象限的典型代表——但它其實不小：

- 美國 HVAC 分銷行業每年處理超過 $1500 億
- HVAC 承包商約 12 萬家（美國）
- 每家都面對多層合規：聯邦 EPA + 州執照 + 當地建築法規 + OSHA

而且它完美符合**長尾服務**的定義：每個城市的建築法規不同，每個州的承包商執照要求不同，制冷劑法規每年都在變。太碎片化讓大公司不願進入，但對承包商來說是真實的痛。

## 跟你的方向的關係

HVAC 合規是你之前提到的「空白利基」中**食品/飲料許可證、環境許可證**的同一類問題——本地化、碎片化的trades/建築合規。

如果你做的是 Compliance Context API，HVAC 合規知識會是其中一個垂直數據集。但如果你想直接做 Autopilot 服務，HVAC 承包商執照自動化會是一個具體的切入點——類似 Payna 對金融執照做的事，但在 trades 領域。

你是在考慮 HVAC 作為你的第一個服務利基嗎？

---

---

---

## **一、依產業／領域（你筆記裡有提到的）**

### **金融／BFSI**

- **KYC / AML / 反洗錢**（note2, note15）
- **金融執照（美國 50 州）**（note13, note14, note15）
- **消費貸款合規**（note2, note15）
- **抵押貸款 / 房貸**（note14, note15）
- **保險經紀 / 保險合規**（note2, note13, note15）
- **私募 / PE 合規**（note15）
- **SOX / 金融合規**（note2, note8）
- **靈活 FinTech / Capital Market**（note2, Miro）

### **資安／GRC**

- **SOC2 / ISO / HIPAA 自動化**（note2, note15）
- **網站隱私合規（PCI DSS、GDPR、CCPA 等）**（note11, note15）
- **AI 治理 / 合規**（note15）
- **Vanta 市場**（note2）

### **法規智能（水平／基礎設施）**

- **法規→AI 可消費格式**（Norm AI 等）（note15）
- **全球法規數據庫**（Regology 等）（note11, note15）
- **法規知識圖譜**（Vulcan 等）（note9, note11, note15）
- **法規監測 / 政策情報**（Abstract 等）（note11, note15）

### **醫療**

- **FDA 製藥**（note2）
- **醫療執照 / Credentialing（跨州）**（note13, note14, note15）
- **醫療機構 AI 合規**（Wedge AI 等）（note2）
- **遠距醫療執照**（note13）
- **藥品法規寫作（CTD、IND、BLA 等）**（note15）

### **硬體／製造**

- **硬體安全認證（CE、FCC、UL、ISO、FAA 等）**（note13, note14, note15）
- **Manufacture / F4 / VLA / CAD**（note2）
- **自駕 / 機器人安全驗證**（note15）

### **大麻**

- **大麻法規 / 執照申請**（note2, note13, note14, note15）

### **建築／營造**

- **建築 / Construction 合規與專案 Agent**（Armeta 等）（note2, note4, Miro 區塊分類）
- **建築許可 / 審圖**（Miro）

### **政府／公共**

- **Gov / FedRAMP / 政府採購審核**（note2）
- **監管機構 / 市政審查**（note2, note4, Miro）

### **供應鏈／物流**

- **供應鏈 AI 代理**（note2, note9）
- **Global Trade / 跨境電子商務合規**（note2, note5）
- **物流 / 車隊合規**（note14, note15）
- **關稅 / 進出口合規**（note8, note9）

### **行銷／內容**

- **Marketing / AI Content Compliance**（note2, note4, note9）

### **法律**

- **Law**（note2, note4, note8）
- **IP / 專利合規**（note11, note15）

### **ESG / 永續**

- **ESG**（note2）
- **CSRD / SFDR**（note13）

### **會計／稽核**

- **Accounting**（note2, note8）
- **內部稽核 / SOX 稽核**（note8, note15）

### **房地產**

- **房地產合規（房產稅、租賃法規、銀行合規）**（note2, note11, note15）

### **勞動／薪資**

- **勞動合規 / 薪資合規**（note13, note15）

### **其他產業或場景**

- **線上博弈 / 運動博彩**（note13）
- **無人機 / 自駕車許可**（note13）
- **食品 / CPG / 飲料許可證**（note13, note15）
- **環境許可證**（排放、水質、廢棄物）（note15）
- **教育 / 培訓認證**（note15）
- **交通 / 物流許可證**（貨運、危險品）（note15）
- **保險代理人執照（50 州）**（note15）
- **Excess & Surplus (E&S) 保險市場**（note15）
- **HVAC 合規 / 承包商執照**（note14, note15）
- **個人報稅 / 帳單檢查**（note2）
- **Fact Checking**（note2）
- **Agent 自身合規市場**（note2）
- **Coding Niche / Build Compliance Prototype**（note5）
- **IPO Niche**（Miro 完整清單）

---

## **二、依「管轄區／地理」提到的利基**

- **美國 50 州**（金融執照、保險執照、醫療執照、大麻等）
- **APAC / 東南亞 ASEAN**（新加坡 MAS、印尼 OJK、泰國 SEC、菲律賓 BSP 等）（note13, note15）
- **歐盟 27 國**（GDPR、AI Act、DORA、轉法差異）（note13）
- **中東 GCC**（DIFC、ADGM、SAMA 等）（note13）
- **拉丁美洲 / 巴西**（note8, note13）
- **台灣**（你設定的主場／APAC 切入點）

---

## **三、note15 的「利基矩陣」簡表（大/中/小市場 × 競爭度）**


|             | **低競爭**                 | **高競爭**               |
| ----------- | ----------------------- | --------------------- |
| **大市場**     | 保險代理執照、APAC 金融執照、跨境電商合規 | KYC/AML、SOC2/ISO、金融執照 |
| **中市場**     | 房地產合規、藥品法規寫作、勞動合規       | 醫療執照、法規智能平台           |
| **小市場（長尾）** | 食品許可、環境許可、教育認證、交通許可     | 大麻合規、硬體認證             |


---

## **四、Miro 區塊分類裡與利基相關的標籤**

- 合規/監管/GRC、建築審圖、政府
- 醫療/健康、生命科學、稅務
- 建築/營建、製造、供應鏈
- 大麻/藥局、公用事業、國防
- 碳/硬體/安全合規、環境/法規

---

**總結**：所有 md 裡出現的 niche 涵蓋 **金融、資安/GRC、法規基礎設施、醫療、硬體認證、大麻、建築、政府、供應鏈/物流、行銷、法律/IP、ESG、會計/稽核、房地產、勞動、博弈、食品、環境、教育、交通、保險、HVAC、個人稅務、Agent 合規、coding、IPO** 等，並搭配 **美國 50 州、APAC、歐盟、中東、拉美** 等管轄區維度。  
若要針對「某一個 niche」做下一步（例如只列「有對應公司的」或「你標記為空白的」），可以指定類別或檔案，我可以再幫你篩一版清單。

---

---

---

根據你所有 md 筆記，出現過的**產品型態**與**商業模式**整理如下。

---

## **一、產品型態（Product Types）**

### **note15 的七類（最完整）**


| **型態**                              | **說明**                   | **筆記中的代表**                                                                  |
| ----------------------------------- | ------------------------ | --------------------------------------------------------------------------- |
| **① Copilot（人問 AI 答）**              | 人提問，AI 回答合規問題，人判斷與執行     | [CannabisRegulations.ai](http://CannabisRegulations.ai)、Norm AI 早期、Regology |
| **② Autopilot（AI 直接做）**             | AI 完成合規任務，人審核結果；Bek 框架核心 | Payna、Brico、Medallion、Eloquent AI、Copperlane、Zolvo、Parcha                   |
| **③ API / Infrastructure**          | 給其他 AI／軟體調用，不直接對終端用戶     | Checkr、Plaid、Norm AI API（policy-as-code）                                    |
| **④ Platform / OS**                 | 合規團隊用的完整工作台              | Complyance、Abstract Security、Vulcan                                         |
| **⑤ Translation Layer（翻譯層）**        | 坐在現有系統之間，讓系統互通、不取代       | Eos AI、Cardamon（法規→義務→要求）                                                   |
| **⑥ Agent（端到端執行者）**                 | Autopilot + 自主決策，可跨系統操作  | Noetic、Oddysee AI                                                           |
| **⑦ Knowledge Hub / Context Layer** | 結構化合規知識，供人／機器查詢          | Context Hub、CyberContext AI、Compliance Context Infra                        |


### **其他筆記補充的型態**

- **Library as a Service (LaaS)**：交付物是「服務／API」，不是代碼或文檔；Agent 透過 MCP 調用（note2, note7, note8）
- **Compliance Library as a Service**：合規知識庫 + MCP，給 Agent 調用（note7）
- **Regulatory Proxy（監管代理）**：用我的牌照／合規能力讓你營運，例如 Cumbuca（note13）
- **B2B2C / 嵌入 B2B2C**：幫企業做合規，間接保護消費者，如 OneTrust（note15）

---

## **二、商業模式（Business Models）**

### **note15 的六種**


| **模式**                                   | **說明**               | **代表**                               |
| ---------------------------------------- | -------------------- | ------------------------------------ |
| **① 按任務收費（pay-per-task / credit-based）** | 每完成一個具體任務收費，最接近「賣工作」 | Eloquent AI、Checkr、Parcha            |
| **② SaaS 訂閱（月/年、seat）**                  | 按人頭或公司收月費/年費         | Complyance、Regology、Abstract、Norm AI |
| **③ 項目制 ACV（年約）**                        | 一次簽約、按年收大額合同，常六位數起   | Payna、Brico                          |
| **④ API 用量計費（usage-based）**              | 按 API 調用數或處理量計費      | Checkr、Reducto、Plaid                 |
| **⑤ 成功抽成（outcome-based）**                | 只有成功才收費；Bek 理想型      | 「收完成工作的費用」                           |
| **⑥ 替代定價（vendor swap）**                  | 取代客戶原本付給律師/顧問的預算     | Payna、Brico                          |


### **note8 的十種命名模式（含策略層）**


| **模式**                                                   | **要點**                                                              |
| -------------------------------------------------------- | ------------------------------------------------------------------- |
| **1. Plaid 模式**                                          | 合規 Context 做成標準化 API，按調用量收費；做底下基礎設施                                 |
| **2. Stripe 模式**                                         | Infra → 生態擴張：Context Infra → Agent → Agent Team → Agentic Economics |
| **3. Library as a Service（[21st.dev](http://21st.dev)）** | 合規知識透過 MCP 被 Agent 調用；交付可執行的合規智能                                    |
| **4. 諮詢 + FDE**                                          | 前期諮詢/駐場導入，知識回饋到 Context Infra（Varick、Fed10）                         |
| **5. Doola 模式**                                          | 一條龍代辦：「Doola for Compliance」、done-for-you                           |
| **6. Firm 轉型賦能**                                         | 幫 Firm 轉型 Full Stack AI；客戶是服務商（Clio、Wayco）                          |
| **7. 監管端工具（Vulcan）**                                     | 賣給政府/監管機構：制定法規、審查、公眾評論                                              |
| **8. Marketplace / 模板**                                  | 合規模板、Playbook 市集（Vybe）                                              |
| **9. AI Employee 訂閱**                                    | Multi-Agent 合規團隊訂閱（Proximitty）                                      |
| **10. Pier 模式**                                          | 合規嵌入產品 API；幾行 code 就合規（如放貸）                                         |


### **其他筆記提到的模式**

- **Cumbuca 模式**：Regulatory proxy——用我的牌照讓你營運，收「授權／代理」費（note13）
- **Cranston / AI 事務所**：不賣軟體，收會計/合規服務費；AI 做、人品管（note8）
- **按 connection 收費**：WorkOS 式，例如「每個合規連接」計費（note12）

---

## **三、產品型態 × 商業模式的組合（筆記中的結論）**

- **Autopilot + 替代定價** → 最快變現（Payna：取代律所 billable hours）
- **API + 用量計費** → 規模最大（Checkr $800M），但冷啟動難
- **Agent + 按任務收費** → 激勵最對齊（Eloquent AI 4 週 $500K ARR）
- **階段 1→4 演化**：Autopilot（替代定價）→ + Knowledge Hub → + API（用量計費）→ + Agent（按成果收費）

---

## **四、核心區分（Bek / 筆記反覆出現）**

- **賣工具（tool）**：Copilot、純 API、純 Infra → 容易被下一版模型吃掉
- **賣工作成果（work）**：Autopilot、按任務/成果收費、替代律所/顧問 → 筆記中較推薦

---

## **五、一句話對照表**


| **維度**   | **選項摘要**                                                                                                                    |
| -------- | --------------------------------------------------------------------------------------------------------------------------- |
| **產品型態** | Copilot、Autopilot、API/Infra、Platform/OS、Translation Layer、Agent、Knowledge Hub/Context、LaaS、Regulatory Proxy                 |
| **商業模式** | 按任務、SaaS 訂閱、項目 ACV、API 用量、成功抽成、替代定價；Plaid/Stripe/WorkOS/Doola/Payna/Pier/Cumbuca/FDE/Firm 轉型/監管端/Marketplace/AI Employee 訂閱 |


以上都是你 md 裡出現過的產品型態與商業模式；若要針對「只做第一階段」或「solo 起步」再篩一版，可以指定條件。

---

---

---

## **一、筆記裡已出現的「混合型態」實例**

### **1. 三型態融合（同一產品、多介面）**


| **公司**     | **混合內容**                                                                       | **出處** |
| ---------- | ------------------------------------------------------------------------------ | ------ |
| **Checkr** | **API**（給 Uber/Lyft 調用）+ **Autopilot**（自動完成調查）+ **Platform**（客戶 dashboard）     | note15 |
| **Brico**  | 對客戶 = **Autopilot**（幫你申請執照）；對工程 = **API**（接 NMLS）；對合規主管 = **Platform**（追蹤各州狀態） | note15 |
| **Noetic** | **Knowledge Hub**（研究法規）+ **Agent**（自動產文件）+ **Platform**（匹配實驗室）                 | note15 |


### **2. 兩型態融合**


| **公司**          | **混合內容**                                                           | **出處** |
| --------------- | ------------------------------------------------------------------ | ------ |
| **Eloquent AI** | 表面 **Autopilot**（客服自動化）+ 底層 **Translation Layer**（觀察 SOP、坐在現有系統之間） | note15 |
| **Fintool 思路**  | 對外可同時：**API**（給其他 AI 用你的 context）+ **Agent**（給終端客戶用 autopilot）     | note12 |


### **3. 三層同時做（Eos 式）**


| **模式**  | **混合內容**                                                                       | **出處** |
| ------- | ------------------------------------------------------------------------------ | ------ |
| **Eos** | **Infra 層**（數據統一、翻譯層）+ **Context 層**（Fintool 式結構化）+ **Autopilot 層**（自動執行、恢復收入） | note12 |


### **4. 技術棧式混合（你的方向）**

- **Claude Code SDK 當底層** → **Context 層**（Eos 式翻譯層）→ **Skills**（Fintool）→ 對客戶賣 **Autopilot**（Bek）
- 即：**Infra/引擎 + Context + Autopilot** 混在一起對外呈現為一個產品（note12）

---

## **二、依「價值鏈」的混合邏輯（note15）**

筆記的建議是：**從一個起點，往上下游長**，而不是一次做全部。

- **上游**：知識／查詢 → Knowledge Hub、Context Layer、API、Copilot
- **下游**：執行／交付 → Autopilot、Agent、Platform

因此「混合」通常是** 2～3 個相鄰型態**的組合，例如：


| **上游 ←**          | **混合組合（例）**                       | **→ 下游**         |
| ----------------- | --------------------------------- | ---------------- |
| Knowledge Hub     | **Knowledge Hub + API**           | 只開知識/查詢          |
| Knowledge Hub     | **Knowledge Hub + Agent**         | 查完還能自動做          |
| Knowledge Hub     | **Knowledge Hub + Platform**      | 查詢 + 在平台上操作      |
| Translation Layer | **Translation Layer + Autopilot** | 坐在系統間 + 直接做完     |
| API               | **API + Autopilot**               | 被調用 + 自動執行       |
| API               | **API + Platform**                | 被調用 + 人有操作台      |
| Autopilot         | **Autopilot + Platform**          | 自動做 + 人監控/審核     |
| Copilot           | **Copilot + Autopilot**           | 人問 AI 答 + AI 直接做 |


---

## **三、可以有哪些「混合產品型態」清單（依筆記）**

在**先從單一型態起步、再自然演化**的前提下，筆記裡合理出現的混合有：

1. **API + Platform**（例如 Checkr、Brico：調用 + 管理台）
2. **API + Autopilot**（API 觸發，後端自動完成整件工作）
3. **Autopilot + Platform**（自動做 + 人在平台上審核/追蹤）
4. **Knowledge Hub + API**（結構化知識對外當 API）
5. **Knowledge Hub + Agent**（知識驅動的端到端 Agent）
6. **Knowledge Hub + Platform**（知識庫 + 合規工作台）
7. **Translation Layer + Autopilot**（Eos / Eloquent 式：坐系統間 + 自動執行）
8. **Translation Layer + API**（翻譯層對外當 API）
9. **Agent + Platform**（Agent 執行 + 人在 Platform 上看/控）
10. **Copilot + Autopilot**（先回答再執行，或依情境切換）
11. **LaaS + API**（合規 Library 以服務/API 形式被調用）
12. **API + Autopilot + Platform**（Checkr/Brico 的完整三件套）
13. **Knowledge Hub + Agent + Platform**（Noetic 式：研究→執行→匹配/追蹤）
14. **Infra/Context + Autopilot**（底層 context/infra，上層對客戶是 autopilot）

---

## **四、筆記的提醒**

- **融合是結果，不是 Day 1 設計**：先單一型態、單一任務、單一客戶，再長出第二、第三型態。
- **避免一次做滿**：一開始就 Infrastructure + API + Agent + Platform 容易什麼都沒真的做出來。
- **演化順序的範例**：Autopilot → + Knowledge Hub → + API → + Agent（note15 階段 1→4）。

所以：**混合產品型態可以有上面這些**，但筆記建議是**先選一個主型態，再按價值鏈選「要加哪一種混合」**，而不是一開始就設計一個大雜燴。

---

---

---

MiroFish 很火，但跟你的方向關聯性需要拆開來看。

## MiroFish 是什麼

一個開源 AI 預測引擎，它提取真實世界的數據（新聞、報告、甚至小說），產生成千上萬個有獨特人格和記憶的 AI agents，讓他們在模擬世界中互動，然後根據湧現的結果產生預測報告。

簡單說：「SimCity 遇上 AI 預測」。

## 核心數據

- GitHub 27.8K stars
- 盛大集團創辦人陳天橋 24 小時內敲定 3000 萬人民幣投資
- 開發者郭航江是北郵大四學生，10 天內用 Vibe Coding 完成開發
- 前一個項目 BettaFish（輿情分析）一週內獲得 20,000 stars

## 技術架構

MiroFish 用 GraphRAG 解析輸入，提取實體和關係，建構結構化知識圖譜——誰是關鍵玩家、他們如何連接、存在什麼壓力、涉及什麼機構。然後基於這個圖譜自動生成 agent 人格，在兩個平台（類 Twitter 和類 Reddit 環境）同時運行模擬，數十到數百個 agents 開始互動——發帖、評論、辯論、形成觀點、互相影響。

## 我的看法——三個層面

**① 作為技術項目：印象深刻但需要冷靜看**

10 天開發、大四學生、GitHub 登頂——這個故事本身比技術更火。Multi-agent 模擬預測並不新，Stanford 的 Generative Agents 論文在 2023 年就做了類似的事。MiroFish 的價值在於把它做成了開箱即用的開源工具，降低了門檻。

但「預測萬物」是一個極大的 claim。Multi-agent 模擬的準確性高度依賴於初始設定的品質——agent 人格設計得不好，模擬結果就是垃圾。目前還沒有看到嚴謹的預測準確率驗證。

**② 跟你的合規 AI 方向的關聯：有，但不直接**

MiroFish 的應用場景包括：金融決策支持、政策和輿情預測、公關危機模擬、行銷策略測試

其中「政策預測」跟你有交集。想像一下：

- 一個新的 AML 法規草案出來 → 用 MiroFish 模擬金融機構和犯罪者的行為 → 預測法規的實際影響
- 一個州要改變保險法規 → 模擬經紀人、承保人、消費者的反應 → 預測市場變化

但這是「法規影響預測」，不是「法規合規執行」。跟你做的 Compliance Context API 是不同的問題。

**③ 對你的內容策略和建構策略的啟示：這才是最值得注意的**

MiroFish 對你最大的啟示不是技術，而是**路徑**：

一個大四學生，10 天 Vibe Coding，開源到 GitHub，登頂 trending，24 小時拿到投資。

這驗證了幾件事：

**開源 + 病毒式傳播可以替代傳統的客戶開發。** 他沒有做客戶訪談、沒有找 PMF、沒有 cold email。他做了一個有趣的東西，放上去，讓人自己來。

**一個人可以做出有影響力的東西。** 你不需要團隊、不需要融資才能開始。

**但——他的問題跟你的問題不同。** MiroFish 是一個通用引擎，「預測萬物」聽起來很酷但商業化路徑模糊。你的方向是具體的：合規知識給 AI agents 用。你的商業化路徑更清晰（API 按次收費），但你的傳播性不如他。

## 對你的具體建議

如果你受到 MiroFish 啟發，想用類似路徑，最高 ROI 的做法是：

**做一個開源的、具體的、有用的東西，放到 GitHub 上。**

不是「合規預測引擎」（太模糊），而是比如：

**「50-State Regulatory API」** — 一個開源的、結構化的美國 50 州某個特定法規領域的 JSON 數據庫 + 查詢 API。

比如「50 州 surplus lines 保險法規」或「50 州 HVAC 承包商執照要求」。具體到 Panta 或任何 HVAC 公司的 AI agent 可以直接調用。

這比 MiroFish 更無聊，但更有商業價值。而且如果有人的 AI agent 真的開始用你的 API，那就是真正的 PMF——不是 GitHub stars。

你是在想走 MiroFish 的開源傳播路線嗎？

---

---

---

這個問題問得非常好。讓我把 MiroFish 的架構和 Vulcan 的方向疊在一起看。

## MiroFish 的核心能力

**輸入真實世界種子 → 建構知識圖譜 → 產生有人格的 agents → 模擬互動 → 預測結果**

## Vulcan 的核心能力

**爬取全美法律全文 → 建構法律知識圖譜（節點+關係：判例推翻聯邦法、聯邦法優先於州法）→ 衝突檢測 → 合規規劃 → 法規文本生成**

## 疊在一起的啟發

當你把 MiroFish 的「模擬引擎」和 Vulcan 的「法律知識圖譜」結合，出現了一個目前沒有人在做的東西：

**法規影響模擬器——在法規生效之前，預測它對受監管企業的具體影響。**

目前的合規 AI 公司全部在做「法規已經生效了，幫你遵守」。沒有人在做「法規還在草案階段，幫你預測影響」。

想像這個場景：

EPA 發布新的 HFC 制冷劑限制草案。目前 HVAC 公司的反應是：等法規生效 → 請律師解讀 → 花幾個月調整。如果有一個工具可以做：

**草案文本 → Vulcan 式知識圖譜（這條法規影響哪些現有法規、哪些行業、哪些州）→ MiroFish 式模擬（HVAC 承包商、製造商、供應商、消費者的行為會怎麼改變）→ 輸出：「你的業務在 6 個月內需要做這三件事，否則面臨 X 風險」**

這就從「被動合規」變成了「主動法規策略」。

## 三個具體的產品概念

**概念 A：法規沙盒（Regulatory Sandbox）**

輸入：一條新法規草案 處理：Vulcan 式圖譜找出所有受影響的法律節點 + MiroFish 式模擬跑出利害關係人的行為變化 輸出：影響評估報告——誰受益、誰受損、哪些合規流程要改

客戶：政府機關（在立法前測試影響）、大型企業（在法規生效前準備）、遊說公司（用數據支持論點）

Vulcan 已經在賣給維吉尼亞州政府和美國教育部了。他們少的就是模擬層。

**概念 B：合規壓力測試（Compliance Stress Test）**

輸入：一家公司的現有合規狀態 + 多個可能的法規變化情境 處理：模擬不同法規情境下公司的合規缺口、成本變化、風險暴露 輸出：類似金融壓力測試——「如果 X 法規通過，你的合規成本增加 Y%，需要 Z 個月調整」

客戶：CFO、合規長、董事會

這跟金融業的 CCAR/DFAST 壓力測試是同一個邏輯，但用在法規合規上。

**概念 C：Agent 行為合規預測**

這個最前沿。隨著 AI agent 越來越多參與經濟活動：

輸入：一個 AI agent 的行為規則 + 相關法規 處理：模擬這個 agent 在各種邊緣情境下的行為 → 檢測哪些行為可能違規 輸出：「你的 agent 在這 5 個情境下會違反 X 法規」

客戶：所有部署 AI agent 的公司（Panta、Eloquent、Fenrock）

Norm AI 說他們在做「agent-to-agent 合規監控」，但那是事後監控。這個概念是**事前模擬**——在 agent 上線前就跑完合規壓力測試。

## 但——這些都太大了

這三個概念都是 Series A 以後的產品。你現在需要的是第一步。

回到你的現實：你一個人，在台灣，沒有融資。MiroFish + Vulcan 的啟發告訴你的不是「去建一個法規模擬引擎」，而是：

**知識圖譜是合規 AI 的核心資產。**

MiroFish 的價值在圖譜。Vulcan 的價值在圖譜。Norm AI 的 LEAP 本質上也是一種圖譜（決策樹）。Regology 的 Smart Law Library 也是圖譜。

**每一家成功的合規 AI 公司，底層都在建某種形式的法規知識圖譜。**

而且每一家都在從零開始建自己的。

## 所以對你的啟發是

你的第一步不需要模擬引擎。你需要的是：

**一個特定領域的法規知識圖譜，結構化到 AI agent 可以直接查詢。**

比如：台灣金融法規的知識圖譜。不只是「法規文本」，而是「法規 A 要求 X → 如果違反 → 罰則 Y → 相關法規 B, C → 最近修改日期 → 影響的業務類型」。

做出來之後，它可以被 Vulcan 式的公司用（法規分析）、被 MiroFish 式的工具用（模擬輸入）、被 Panta/Fenrock 式的 agent 用（即時查詢）、被 Norm AI 式的平台用（決策樹的數據源）。

**一個圖譜，多個消費者。這就是基礎設施。**

你之前在 X 上的內容策略 + 開源知識圖譜 = 你的第一步。你覺得呢？