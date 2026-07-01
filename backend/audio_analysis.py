import librosa
import matplotlib.pyplot as plt


def analyze_audio(audio_path):
    y, sr = librosa.load(audio_path)

    duration = librosa.get_duration(y=y, sr=sr)
    rms = librosa.feature.rms(y=y).mean()
    zcr = librosa.feature.zero_crossing_rate(y).mean()

    return {
        "duration": round(duration, 2),
        "rms_energy": round(float(rms), 4),
        "zero_crossing_rate": round(float(zcr), 4),
        "waveform": y
    }


def plot_waveform(waveform):
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.plot(waveform)
    ax.set_title("Audio Waveform")
    ax.set_xlabel("Samples")
    ax.set_ylabel("Amplitude")

    image_path = "waveform.png"
    fig.savefig(image_path)

    return fig, image_path