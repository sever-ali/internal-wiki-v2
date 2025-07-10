# 🗂️ Internal Wiki v2 — README

## 🚀 Project Overview

This project is a refined MVP for an **internal wiki** that store or company staff can use to access knowledge easily.  
It demonstrates end-to-end modern DevOps practices:  
- **Infrastructure provisioning** with Terraform  
- **Configuration management** with Ansible  
- **Containerisation** with Docker  
- **Kubernetes deployment** with raw manifests  
- **Monitoring** using Prometheus scrape endpoints

It’s designed to show how you can automate cloud infrastructure, configure servers, deploy a simple Flask app, and monitor it — all in a repeatable way.

---

## ⚙️ What This Project Uses

- **Terraform** — to provision the underlying AWS network (VPC, subnet, IGW, security groups) and EC2 instance.
- **Ansible** — to install Docker & K3s on the EC2 and copy K8s manifests.
- **Docker** — to build & containerise the Flask wiki app.
- **Kubernetes (k8s)** — raw manifests to deploy the wiki, expose it, and monitor with Prometheus.
- **GitHub Actions CI/CD** — to automate Docker build & push.

---

## 🗂️ Project Structure

```
.github/workflows/
 └── deploy.yml           # CI/CD pipeline for Docker image

ansible/
 ├── inventory.ini        # Target server inventory for Ansible
 └── playbook.yml         # Installs Docker, K3s, copies manifests

terraform/
 ├── main.tf              # Main Terraform config for VPC, subnet, SG, EC2
 └── variables.tf         # Terraform variables

k8s/
 ├── deployment.yaml      # K8s Deployment for Flask app
 ├── service.yaml         # K8s Service to expose app
 └── service-monitor.yaml # Prometheus ServiceMonitor for metrics

Dockerfile                # Container definition for Flask wiki
requirements.txt          # Python requirements
run.py                    # Simple Flask app with Prometheus metrics

.gitignore                # Ignore venv, .pem, .tfstate, etc.

```
--- 

## 🚀 How To Deploy & Test

### ✅ 1️⃣Provision Infrastructure

1. Install Terraform and configure your AWS credentials.
2. Initialise & apply:

```
terraform init
terraform apply

```

3. Take note of the output — your EC2 public IP.


### ✅ 2️⃣ Configure & Deploy with Ansible

1. Install Ansible.
2. Update ansible/inventory.ini with your EC2 IP and SSH key path.
3.Run the playbook:

```
ansible-playbook -i ansible/inventory.ini ansible/playbook.yml

```

This provisions Docker, K3s, and copies your K8s manifests.

### ✅ 3️⃣ Build & Push Docker Image (CI/CD)

1. The .github/workflows/deploy.yml includes:
 - Checkout, build & push Docker image to Docker Hub.
2. Pushing changes to main triggers this workflow automatically.


### ✅ 4️⃣ Deploy to K8s & Monitor

1. Your Ansible playbook already places the manifests in the correct path on your EC2.
2. SSH into the EC2 and apply them:

```
kubectl apply -f /home/ubuntu/k8s/
```

3. Prometheus will scrape metrics via /metrics endpoint.


### ✅ 5️⃣ Verify

- Visit http://<your-load-balancer-or-node-ip>:<nodePort> to confirm the wiki app is running.
- Access /metrics to see Prometheus scrape data.
- Connect Grafana dashboards if you extend monitoring later.

### ⚡ Notes

- Never commit secrets like SSH keys or .pem files to your repo.
- Adjust security groups to limit open ports in production.
- Connect Grafana dashboards if you extend monitoring later.

This project shows you can combine Terraform, Ansible, Docker, Kubernetes, and Prometheus to deliver a repeatable cloud deployment with observability.