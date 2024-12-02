import gradio as gr
import whisper
import torch

# Load model on startup
print("Loading Whisper model...")
device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("medium").to(device)
print(f"Model loaded on {device}")

def transcribe_audio(audio_file, language="English"):
    """
    Transcribe audio using Whisper model
    """
    try:
        # Transcribe audio
        result = model.transcribe(
            audio_file, 
            fp16=False,
            language=language
        )
        return result["text"]
    except Exception as e:
        return f"Error processing audio: {str(e)}"

# Create Gradio interface
demo = gr.Interface(
    fn=transcribe_audio,
    inputs=[
        gr.Audio(source="microphone", type="filepath", label="Audio Input"),
        gr.Dropdown(
            choices=["English", "Spanish", "French", "German", "Italian", "Portuguese", "Dutch"],
            value="English",
            label="Language"
        )
    ],
    outputs=gr.Textbox(label="Transcription"),
    title="Whisper Speech Recognition",
    description="Record or upload audio to transcribe it using OpenAI's Whisper model",
    examples=[
        ["example1.mp3", "English"],
        ["example2.mp3", "Spanish"]
    ]
)

demo.launch(server_name="0.0.0.0", share=True) 