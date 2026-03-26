這個問題問得太好了。你想同時做 Infra **又**做垂直工作流，這聽起來矛盾，但 Claude Code 的發展路徑其實完美示範了怎麼做到。

讓我先把 Claude Code 的策略邏輯拆開：

## Claude Code 的啟發：Infra 偽裝成產品

Claude Code 表面上是一個「給開發者用的終端工具」——這是一個垂直的、深入工作流的產品。但本質上它做了幾件事：

**第一，它是 Anthropic 的 Context Infra 的最佳展示。** Claude Code 的厲害不只是 LLM 能力，而是它能讀懂你的整個 codebase、理解你的 coding style、知道你的 project 結構。這就是 context。它把「理解你的工作環境」這件事做到極致，然後讓 AI 在這個 context 裡面幹活。

**第二，它用「開發者工具」這個切入點建立了生態。** 開發者是最好的早期用戶——他們願意嘗試新東西、能給高品質反饋、而且他們自己就是未來會在你的 Infra 上構建產品的人。Claude Code 的用戶同時也是 Anthropic API 的潛在客戶。

**第三，它從單一 Agent 擴展到 Multi-Agent。** Claude Code 從一個 terminal agent 開始，現在發展出 swarm mode、parallel task execution。先讓一個 agent 做到極好，再讓多個 agent 協作。

**第四，Cowork 是從 Code 自然延伸出來的。** 證明了程式碼工作流之後，再擴展到非技術工作流（文件、瀏覽器、Excel），用的是同一套 context 引擎。

## 套用到你的合規事業

你可以用完全一樣的邏輯：

```
Claude Code 的路徑：
Terminal Agent (Code) → Swarm Mode → Cowork (非技術工作流) → Frontier (企業平台)

你的路徑：
Compliance Agent (一個利基的工作流) → Agent Team → 跨利基擴展 → Context Infra 開放給生態
```

具體來說，你不需要在「做 Infra」和「做垂直產品」之間二選一。策略是：

**先做一個像 Claude Code 一樣的「垂直產品」**——但你內部的架構從第一天就是按 Context Infra 來設計的。對外，用戶看到的是一個解決具體合規工作流的產品（像 Scoop 做 IND、像 Lexi 做法律文件）。對內，你的技術架構是模組化的 Context Layer + Agent Layer，這樣當你進入第二個垂直領域時，你只需要加新的 Context 模組，Agent 的執行框架可以重用。

這就是 Peter Thiel 說的「從壟斷一個小市場開始」——但你壟斷的方式不只是做最好的垂直產品，而是**同時在暗處構建可擴展的 Infra**。

打個比方：

Stripe 一開始就只是「讓開發者 7 行 code 接入支付」。但它底層的 Infra（風控、合規、跨境清算）從第一天就是模組化設計的。所以後來才能長出 Stripe Atlas（公司設立）、Stripe Connect（平台支付）、Stripe Treasury（銀行即服務）。用戶一開始只看到一個支付 API，但 Stripe 內部看到的是一整套金融基礎設施。

你要做的也是一樣：**用戶看到的是一個合規工作流產品，你看到的是 Context Infra 在長大。**

## 那到底先做哪個垂直工作流？

這才是最關鍵的決定。基於 Claude Code 的啟發，你的第一個垂直應該滿足這些條件：你的回答會幫我們一起鎖定最適合的第一個垂直切入點。同時如果你有想法，也可以直接跟我說——比如你之前列的 20 個利基裡面，有沒有哪個讓你特別興奮或者覺得特別有機會的？