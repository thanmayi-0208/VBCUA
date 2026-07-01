def calculate_final_score(semantic_score, audio_metrics):
    # Audio score based on RMS energy
    rms = audio_metrics["rms_energy"]

    if rms > 0.1:
        audio_score = 90
    elif rms > 0.05:
        audio_score = 75
    else:
        audio_score = 50

    final_score = (semantic_score * 0.7) + (audio_score * 0.3)

    return round(final_score, 2)