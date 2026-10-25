# MNIST Dimensionality Reduction and Reconstruction with Autoencoders

A TensorFlow/Keras notebook that uses the built-in MNIST dataset to explore an autoencoder for image reconstruction and a denoising workflow.

## Data and limitations

No external dataset files are required; TensorFlow downloads MNIST when needed. The notebook is an exploratory demonstration and does not report a reproducible benchmark.

No datasets, checkpoints, or model weights are included. Notebook outputs were cleared to remove stale runtime logs and generated figures. The training and evaluation cells remain part of the notebook but were not rerun during repository preparation; this README makes no performance or real-world accuracy claim.

## Requirements

- Python 3.10 or newer
- Dependencies listed in `requirements.txt`
- TensorFlow uses the Keras 2 API; TensorFlow 2.12–2.15 is the intended compatibility range. Install a build appropriate for your platform and hardware.

```bash
python -m venv .venv
# Activate the environment, then:
python -m pip install -r requirements.txt
```

## Run

Open `notebook.ipynb` in Jupyter or Google Colab. Review the data paths and labels before running. Several source notebooks contain exploratory or dataset-specific assumptions that may need adjustment for a different dataset.

## Tests

The tests validate notebook structure and confirm that generated execution outputs are absent. They do not execute model training or verify predictive performance.

```bash
python -m pip install pytest
python -m pytest
```
