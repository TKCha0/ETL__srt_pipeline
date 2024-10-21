from .base_transformer import BaseTransformer
import os 
import whisper
from whisper.audio import load_audio
import pysrt
from io import StringIO

class SrtTransformer(BaseTransformer):  
    def transform(self, wav_path):
        global srt_content

        model = whisper.load_model("medium")
        print(f"Whisper 模型已加載。")

        audio = load_audio(wav_path)
        print("正在轉錄音訊...")
        
        result = model.transcribe(audio)
        print("音訊轉錄完成。")

        subs = pysrt.SubRipFile()

        for i, segment in enumerate(result["segments"]):
            start_time = segment["start"]
            end_time = segment["end"]
            text = segment["text"].strip()
            
            start_hours, remainder = divmod(start_time, 3600)
            start_minutes, start_seconds = divmod(remainder, 60)
            start_milliseconds = int((start_seconds - int(start_seconds)) * 1000)

            end_hours, remainder = divmod(end_time, 3600)
            end_minutes, end_seconds = divmod(remainder, 60)
            end_milliseconds = int((end_seconds - int(end_seconds)) * 1000)
            
            start_time_srt = pysrt.SubRipTime(start_hours, start_minutes, int(start_seconds), start_milliseconds)
            end_time_srt = pysrt.SubRipTime(end_hours, end_minutes, int(end_seconds), end_milliseconds)
            
            sub = pysrt.SubRipItem(index=i + 1, start=start_time_srt, end=end_time_srt, text=text)
            subs.append(sub)

        return subs
           


