# Whisper Speech Recognition on Akash Network

This project deploys OpenAI's Whisper speech recognition model on Akash Network with a user-friendly Gradio interface.

## Features

- Speech recognition for multiple languages
- GPU acceleration for faster inference
- Easy-to-use web interface
- Microphone input support
- File upload support
- Scalable deployment on Akash Network

## Deployment Instructions

1. Build and push the Docker image:
```bash
docker build -t your-dockerhub-username/whisper-akash:latest .
docker push your-dockerhub-username/whisper-akash:latest
```

2. Deploy on Akash Network:
- Visit [Akash Console](https://console.akash.network)
- Create a new deployment
- Upload the `deploy.yaml` file
- Follow the deployment wizard

## Usage

1. Access the web interface at the provided URL after deployment
2. Choose input method:
   - Record directly using your microphone
   - Upload an audio file
3. Select the language of the audio
4. Click "Submit" to get the transcription

## Requirements

- Akash Network account
- GPU provider for optimal performance
- Minimum 16GB RAM
- 20GB storage

## Performance Notes

The model runs on GPU when available, providing significantly faster transcription times. CPU mode is supported but will be slower.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT License 