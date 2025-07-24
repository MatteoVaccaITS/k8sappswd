# k8sappswd

A simple Flask application ready for Docker and Kubernetes deployment.

## Features

- Flask API with CORS enabled
- Dockerized for easy containerization
- Ready for deployment on Kubernetes

## Getting Started

### Requirements

- Python 3.11+
- Docker (optional, for containerization)

### Local Development

```bash
pip install -r requirements.txt
python app.py
```

### Docker

Build and run the container:

```bash
docker build -t k8sappswd .
docker run -p 5000:5000 k8sappswd
```

### Kubernetes

You can deploy this container to Kubernetes using your preferred method.

## License

MIT License
