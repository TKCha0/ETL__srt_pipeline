from .base_extractor import BaseExtractor
import ffmpeg
import os
import tempfile
import shutil

class SrtExtractor(BaseExtractor):
    def __init__(self, file_path):
        self.file_path = file_path
        self.temp_folder = None

    def extract(self):
        self.temp_folder = tempfile.mkdtemp()
        print(f"臨時資料夾已建立：{self.temp_folder}")

        file_name = os.path.splitext(os.path.basename(self.file_path))[0]
        wav_path = os.path.join(self.temp_folder, file_name) + ".wav"
            
        ffmpeg.input(self.file_path).output(wav_path, acodec = "pcm_s16le", ar = "16000", ac = "1").run()

        print(f"WAV 檔案已生成：{wav_path}")
            
        return wav_path, file_name
    
    def clean_tempfolder(self):
        if self.temp_folder and os.path.exists(self.temp_folder):
            shutil.rmtree(self.temp_folder)
            print(f"臨時資料夾已刪除：{self.temp_folder}")