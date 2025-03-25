import sys
import pyaudio
import wave


class Recorder:
    def __init__(self, file_path="recorded_audio.wav"):
        self.file_path = file_path
        self.audio = None
        self.stream = None
        self.recording = False
        self.rec_data = []

    def audiostart(self):
        """音声録音を開始"""
        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=pyaudio.paInt16,
            rate=44100,
            channels=1,
            input_device_index=1,
            input=True,
            frames_per_buffer=1024,
        )
        self.recording = True
        return audio, stream

    def audiostop(self):
        """音声録音を終了"""
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

    def read_plot_data(self):
        data = self.stream.read(1024)
        return data

    def rec_exec(self):
        wave_f = wave.open(self.file_path, "wb")
        wave_f.setnchannels(1)
        wave_f.setsampwidth(2)
        wave_f.setframerate(44100)
        wave_f.writeframes(b"".join(self.rec_data))
        wave_f.close()

    def record_audio(self, file_path="recorded_audio.wav"):
        self.audio, self.stream = self.audiostart()

        print("録音開始")
        while self.recording:
            data = self.read_plot_data()
            self.rec_data.append(data)
        print("録音終了")

        # self.audiostop(audio, stream)
        # self.rec_exec(file_path, rec_data)
        # print(f"録音データを {file_path} に保存しました。")

    if __name__ == "__main__":
        record_audio()
