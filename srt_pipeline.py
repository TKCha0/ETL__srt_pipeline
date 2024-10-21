from extractor.srt_extractor import SrtExtractor
from transformer.srt_transformer import SrtTransformer
from loader.srt_loader import SrtLoader

class SrtPipeline:
    def __init__(self, file_path):
        self.extractor = SrtExtractor(file_path)
        self.transformer = SrtTransformer()
        self.loader = SrtLoader()

    def run(self):
        wav_path, file_name = self.extractor.extract()
        srt_file = self.transformer.transform(wav_path)
        srt_file_path = self.loader.load(srt_file, file_name)    

        print(f"SRT 檔案位置: {srt_file_path}")

        self.extractor.clean_tempfolder()

if __name__ == "__main__":
    mp4_file = r"xxxx\xxxxx\xxxx"
    pipeline = SrtPipeline(mp4_file)
    pipeline.run()
    

