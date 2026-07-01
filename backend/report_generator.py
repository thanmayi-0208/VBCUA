from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_report(
    concept,
    semantic_score,
    final_score,
    audio_metrics,
    waveform_path
):
    filename = "VBCUA_Report.pdf"

    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 780, "VBCUA REPORT")

    c.setFont("Helvetica", 12)
    y = 740

    c.drawString(50, y, f"Concept: {concept}")
    y -= 30

    c.drawString(50, y, f"Semantic Score: {semantic_score}")
    y -= 25

    c.drawString(50, y, f"Final Score: {final_score}")
    y -= 35

    c.drawString(50, y, "Audio Metrics:")
    y -= 25

    c.drawString(70, y, f"Duration: {audio_metrics['duration']} sec")
    y -= 25

    c.drawString(70, y, f"RMS Energy: {audio_metrics['rms_energy']}")
    y -= 25

    c.drawString(
        70,
        y,
        f"Zero Crossing Rate: {audio_metrics['zero_crossing_rate']}"
    )
    y -= 40

    c.drawString(50, y, "Waveform:")
    y -= 210

    c.drawImage(waveform_path, 80, y, width=450, height=180)

    y -= 40

    if final_score >= 80:
        assessment = "Strong Understanding"
    elif final_score >= 60:
        assessment = "Moderate Understanding"
    else:
        assessment = "Poor Understanding"

    c.drawString(50, y, f"Assessment: {assessment}")

    c.save()

    return filename