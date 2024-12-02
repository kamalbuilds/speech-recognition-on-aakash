FROM nvidia/cuda:12.2.0-base-ubuntu22.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    git \
    wget \
    tar \
    xz-utils \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
RUN pip3 install --no-cache-dir setuptools-rust
RUN pip3 install --no-cache-dir git+https://github.com/openai/whisper.git 
RUN pip3 install --no-cache-dir gradio>=4.0.0 torch torchaudio numpy

# Download the medium model
RUN python3 -c "import whisper; whisper.load_model('medium')"

# Copy application code
COPY app.py .

# Expose port for Gradio interface
EXPOSE 7860

# Run the application
CMD ["python3", "app.py"] 