# 🚀 MLOps on AWS — End-to-End ML Infrastructure Setup

A complete MLOps workflow deployed on AWS using EC2, EBS, S3, IAM Roles, and an automated Machine Learning training pipeline. This project demonstrates cloud-based ML infrastructure provisioning, dataset management, environment automation, model training, logging, and persistence handling.

---

# 📌 Project Overview

This project covers:

- AWS EC2 setup for ML workloads
- Persistent storage using EBS
- Dataset versioning using S3
- Automated environment provisioning
- ML pipeline automation
- Model selection & logging
- Scheduled EC2 auto-shutdown
- Data persistence validation

---

# 🖥️ EC2 Configuration

## Instance Details

| Configuration | Value |
|---|---|
| Instance Type | `t3.micro` |
| Operating System | `Ubuntu 22.04` |
| AWS Region | `ap-south-1` |
| IAM Role | `mlops-ec2-s3-role` |

---

# 💾 EBS Storage Configuration

| Configuration | Value |
|---|---|
| Root Volume | Default |
| Additional Volume | `10GB` |
| AWS Device Name | `/dev/xvdf` |
| OS Device Name | `/dev/nvme1n1` |
| Mount Point | `/mnt/ml-data` |

## Directory Structure

```bash
/mnt/ml-data/
├── datasets/
├── features/
├── models/
└── logs/
```

---

# ☁️ Amazon S3 Configuration

| Configuration | Value |
|---|---|
| Bucket Name | `nooran-mlops-data-2026` |
| Versioning | Enabled |
| Access | Private |
| Region | Same as EC2 |

## Uploaded Datasets

- `raw.csv`
- `processed.csv`

---

# ⚙️ Infrastructure Setup Commands

## 🔹 Mount EBS Volume

```bash
lsblk
sudo mkfs.ext4 /dev/nvme1n1
sudo mkdir -p /mnt/ml-data
sudo mount /dev/nvme1n1 /mnt/ml-data
df -h
```

---

## 🔹 Configure Auto-Mount

```bash
sudo blkid
sudo nano /etc/fstab
sudo mount -a
```

---

## 🔹 Verify AWS CLI & IAM Access

```bash
aws --version
aws s3 ls
```

---

## 🔹 Sync Dataset from S3 → EC2

```bash
aws s3 sync s3://nooran-mlops-data-2026 /mnt/ml-data/datasets
```

---

## 🔹 Sync Dataset from EC2 → S3

```bash
aws s3 sync /mnt/ml-data/datasets s3://nooran-mlops-data-2026
```

---

# 🧪 Environment Setup

## Bootstrap Script

File: `setup_ml_env.sh`

### Run Setup

```bash
chmod +x setup_ml_env.sh
./setup_ml_env.sh
source ~/ml-venv/bin/activate
```

## Features

- Installs Python & pip
- Creates virtual environment
- Installs ML dependencies
- Idempotent execution
- Compatible with fresh EC2 launches

---

# 🤖 Machine Learning Pipeline

## Training Script

File: `train_pipeline.py`

### Execute Pipeline

```bash
python train_pipeline.py
```

## Pipeline Workflow

The pipeline performs:

- Dataset loading from mounted EBS storage
- Feature scaling
- Training of multiple ML models
- Automatic best model selection
- Metrics logging
- Persistent model saving

## Output Locations

| Artifact | Location |
|---|---|
| Models | `/mnt/ml-data/models/` |
| Logs | `/mnt/ml-data/logs/` |

---

# ⏱️ Automated EC2 Shutdown

To optimize cloud costs, scheduled instance shutdown was configured using cron jobs.

## Cron Commands

```bash
sudo crontab -e
sudo crontab -l
```

---

# ✅ Validation Checklist

- [x] EBS auto-mounts after reboot
- [x] Training outputs stored on EBS
- [x] S3 versioning enabled and verified
- [x] AWS S3 sync operational
- [x] Bootstrap script is idempotent
- [x] Automatic EC2 shutdown configured
- [x] Data persists after instance restart

---

# 📂 Project Structure

```bash
mlops-project/
├── setup_ml_env.sh
├── train_pipeline.py
├── README.md
└── screenshots/
```

---

# 🛠️ Technologies Used

- Amazon Web Services (AWS)
- Ubuntu
- Python
- Scikit-learn
- AWS EC2
- AWS EBS
- AWS S3
- IAM Roles
- Linux Cron Jobs

---

# 📈 Key Learning Outcomes

- Cloud infrastructure provisioning for ML workloads
- Persistent storage management using EBS
- Secure AWS authentication using IAM roles
- Data synchronization between EC2 and S3
- Building reproducible ML environments
- Automating ML training pipelines
- Managing cloud cost optimization strategies

---

# 📸 Screenshots

The `screenshots/` directory contains:

- Mounted EBS verification
- `/etc/fstab` configuration
- AWS S3 sync success
- S3 version history
- Virtual environment setup
- Pipeline execution logs
- Cron configuration
- EC2 stopped state validation

---

# 📄 License

This project is intended for educational and learning purposes.
