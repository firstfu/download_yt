import yt_dlp


def download_shorts(url, custom_filename=None):
    # 設定下載選項
    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",  # 優先下載最高畫質 MP4
        "outtmpl": "downloads/%(title)s.%(ext)s" if not custom_filename else f"downloads/{custom_filename}.%(ext)s",
        "merge_output_format": "mp4",  # 確保輸出為 MP4 格式
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],  # 強制轉換為 MP4
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 先獲取影片資訊
            info = ydl.extract_info(url, download=False)
            print(f"準備下載: {info.get('title')}")

            # 開始下載
            ydl.download([url])
        print("下載完成！")
    except Exception as e:
        print(f"下載錯誤: {str(e)}")


# ##########################
# 颱風
# download_shorts("https://www.youtube.com/watch?v=8gjYK86v9I0", "typhoon")

# 龍捲風
# download_shorts("https://www.youtube.com/shorts/sz90P7sA2vg", "tornado")

# 土石流
# download_shorts("https://www.youtube.com/watch?v=-UEPdqHKTbQ&t=2s", "landslide")


# 暴風雪
download_shorts("https://www.youtube.com/watch?v=CQSfI_tXZLY", "blizzard")

# 洪水
download_shorts("https://www.youtube.com/watch?v=oU53X6ZTVQM", "flood")
