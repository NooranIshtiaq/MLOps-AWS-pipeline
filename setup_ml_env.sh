#!/bin/bash
set -e

echo "Updating system..."
sudo apt update -y

echo "Installing Python & tools..."
sudo apt install -y python3 python3-pip python3-venv

VENV_DIR=$HOME/ml-venv

if [ ! -d "$VENV_DIR" ]; then
  echo "Creating virtual environment..."
  python3 -m venv $VENV_DIR
else
  echo "Virtual environment already exists"
fi

source $VENV_DIR/bin/activate

echo "Installing ML libraries..."
pip install --upgrade pip
pip install numpy pandas scikit-learn joblib

echo "Environment setup completed successfully"
