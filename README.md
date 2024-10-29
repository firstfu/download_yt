# YouTube 影片下載工具

這是一個使用 Python 開發的 YouTube 影片下載工具，可以下載一般影片和短影片(Shorts)。使用 yt-dlp 作為核心下載引擎。

## 功能特點

- 支援下載 YouTube 一般影片
- 支援下載 YouTube Shorts
- 自動選擇最佳畫質
- 輸出格式為 MP4
- 支援自訂檔名

## 安裝需求

- Python 3.6+
- pnpm (用於管理相依套件)

## 安裝步驟

1. 複製專案到本地：

   ```bash
   git clone https://github.com/你的用戶名/專案名稱.git
   cd 專案名稱
   ```

2. 建立虛擬環境：

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或
   .\venv\Scripts\activate  # Windows
   ```

3. 安裝相依套件：
   ```bash
   pnpm install
   pip install -r requirements.txt
   ```

## 使用方法

1. 執行程式：

   ```bash
   python download_yt_shorts.py
   ```

2. 在程式碼中修改要下載的影片網址和檔名：
   ```python
   download_shorts("YouTube影片網址", "自訂檔名")
   ```

## 注意事項

- 下載的影片會儲存在 `downloads` 資料夾中
- 請確保有足夠的硬碟空間
- 請遵守 YouTube 的服務條款和版權規定

## 授權條款

MIT License
