from .base_loader import BaseLoader
import os

class SrtLoader(BaseLoader):
    def load(self, subs, file_name):
        if not os.path.exists("srt_folder"):
            os.makedirs("srt_folder")
            print(f" 已建立 srt_folder。")
        else:
            print(f"srt_folder 已存在。")

        srt_path = os.path.join("srt_folder", file_name) + ".srt"

        subs.save(srt_path, encoding='utf-8')
        
        print(f"SRT 檔案已儲存至: {srt_path}")
        return srt_path