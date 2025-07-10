# 🗃️ Internal Wiki DevOps Project V2

This project demonstrates an end-to-end DevOps pipeline for deploying an internal Flask-based wiki app.

## 🚀 Tech Stack

- **Flask** – lightweight Python web app
- **Docker** – containerised app for consistent deployments
- **Kubernetes** – orchestration using manifests/Helm
- **Terraform** – infrastructure as code (optional)
- **Ansible** – automation and config management (optional)
- **Prometheus** – metrics collection for monitoring
- **GitHub Actions** – CI/CD pipeline to build and push Docker images

## ⚙️ CI/CD Workflow

- Build Docker image on every push to `main`
- Push image to Docker Hub securely using GitHub Secrets
- Deploy image using `kubectl apply` (manual or automated)

## 📊 Monitoring

- Prometheus scrapes app metrics exposed at `/metrics`
- Example dashboard: `wiki-app-dashboard.json`

## ✅ How to Run

1. Clone repo & `cd` into project
2. Build image: `docker build -t yourname/wiki-app .`
3. Deploy with `kubectl apply -f K8s/`
4. Access app via service NodePort/LoadBalancer

## 🔒 Secrets Management

All credentials (Docker Hub username/password, keys) stored in GitHub Secrets.
