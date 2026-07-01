import streamlit as st
import tempfile

from backend.audio_analysis import analyze_audio, plot_waveform
from backend.semantic import semantic_score
from backend.scorer import calculate_final_score
from backend.report_generator import generate_report

# Page config
st.set_page_config(page_title="VBCUA", page_icon="🎤")

# Title
st.title("🎤 Voice-Based Concept Understanding Analyser")
st.write("Upload an audio file to analyze conceptual understanding.")

# File uploader
uploaded_file = st.file_uploader(
    "Upload Audio File",
    type=["wav", "mp3", "m4a"]
)

if uploaded_file is not None:
    st.success("Audio uploaded successfully!")
    st.audio(uploaded_file)

    concept = st.text_input("Enter Concept Name")
    user_text = st.text_area("Enter User Explanation Text")
    reference_text = st.text_area("Enter Reference Concept Text")

    if st.button("Analyze"):
        # Save uploaded audio temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(uploaded_file.read())
            temp_audio_path = tmp.name

        # Audio analysis
        audio_metrics = analyze_audio(temp_audio_path)

        # Semantic score
        sem_score = semantic_score(user_text, reference_text)

        # Final score
        final_score = calculate_final_score(
            sem_score,
            audio_metrics
        )

        # Waveform graph
        waveform_fig, waveform_path = plot_waveform(
            audio_metrics["waveform"]
        )

        # Generate PDF report
        report = generate_report(
            concept,
            sem_score,
            final_score,
            audio_metrics,
            waveform_path
        )

        # Results
        st.subheader("Results")
        st.write("Semantic Score:", sem_score)
        st.write("Final Score:", final_score)

        # Clean metrics display
        st.subheader("Audio Metrics")
        display_metrics = {
            "duration": audio_metrics["duration"],
            "rms_energy": audio_metrics["rms_energy"],
            "zero_crossing_rate": audio_metrics["zero_crossing_rate"]
        }
        st.json(display_metrics)

        # Show waveform
        st.subheader("Waveform Visualization")
        st.pyplot(waveform_fig)

        # PDF download
        st.subheader("Generated PDF Report")
        with open(report, "rb") as pdf_file:
            st.download_button(
                label="Download PDF Report",
                data=pdf_file,
                file_name="VBCUA_Report.pdf",
                mime="application/pdf"
            )