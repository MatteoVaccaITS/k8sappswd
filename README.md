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

---

## Kubernetes: Check and Expose the App on Localhost

### Dry-run and validate your manifests

You can validate your YAML files before applying them using `--dry-run=client` and `kubectl apply --validate=true`:

```bash
kubectl apply -f pod.yaml --dry-run=client --validate=true
kubectl apply -f deployment.yaml --dry-run=client --validate=true   # if you have a deployment
kubectl apply -f service.yaml --dry-run=client --validate=true
```

### Apply your pod, deployment, and service YAML files

```bash
kubectl apply -f pod.yaml
kubectl apply -f deployment.yaml   # if you have a deployment
kubectl apply -f service.yaml
```

Check the status of pods and services:

```bash
kubectl get pods
kubectl get services
```

Expose the service on your localhost (for example, if your service is named `k8sappswd-service`):

```bash
kubectl port-forward service/k8sappswd-service 5000:5000
```

Now you can access the app at [http://localhost:5000](http://localhost:5000).

---

## License

MIT License
