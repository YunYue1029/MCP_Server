# Speech Analysis MCP Server

本專案是一個語音分析伺服器，使用MCP（Model Context Protocol）架構，用於自動分析英文口說內容。支援語音轉文字、文法錯誤分析、詞彙建議、邏輯建議及原句比對等功能。

## 專案結構
```
.
├── models/                   # 工具呼叫封裝邏輯（如 tool_call.py）
├── myenv/                   # Python 虛擬環境（不建議提交）
├── speech_audio/            # 參考或教學音檔
├── tools/                   # MCP 工具集合
│   ├── compareSentence.py   # 比對原文與口說差異
│   ├── grammar.py           # 文法分析工具
│   ├── logic.py             # 內容邏輯建議工具
│   ├── vocab.py             # 詞彙建議工具
│   └── whisper.py           # 語音轉文字處理
├── user_audio/              # 使用者上傳的語音檔
├── main.py                  # MCP server 主程式
├── MCPtest.json             # MCP 測試請求樣板
├── requirements.txt         # Python 套件安裝清單
└── README.md                # 專案說明文件
```
## 功能說明

- **語音轉文字**：使用 OpenAI Whisper 模型處理語音檔
- **文法檢查**：分析文法錯誤
- **詞彙建議**：提供更佳詞彙選擇
- **邏輯建議**：回饋語句內容結構與邏輯
- **句子比對**：標示與原文不一致之處
- **GPT Agent**：自動選擇並調用 MCP 工具

## 📦 安裝步驟

1. 下載專案：
    ```bash
    git clone https://github.com/your_username/your_repo.git
    cd your_repo
    ```

2. 建立虛擬環境並安裝依賴：
    ```bash
    python -m venv myenv
    source myenv/bin/activate      # Windows: myenv\Scripts\activate
    pip install -r requirements.txt
    ```

3. 啟動 MCP server：
    ```bash
    python main.py
    ```

## 🔌 API & 測試方式

可使用 `main.py` 搭配 POST 請求來觸發工具分析，範例請參考 `MCPtest.json`。

## 🎵 音檔支援格式

- `.mp3`, `.wav`
- 測試音檔可放置於 `user_audio/` 目錄

## 📄 License

本專案僅供研究與學術用途。

---

如需協助或有建議，歡迎提交 Issue 或聯絡作者 🙌