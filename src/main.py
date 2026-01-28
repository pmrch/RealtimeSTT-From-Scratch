import nemo.collections.asr as nemo_asr

asr_model = nemo_asr.models.ASRModel.from_pretrained("nvidia/parakeet-ctc-0.6b")
transcript = asr_model.transcribe(["path/to/audio_file.wav"])[0].text