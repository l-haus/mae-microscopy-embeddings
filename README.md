# MAE Microscopy Embeddings

This repository explores the use of pretrained Masked Autoencoders (MAEs) to generate vector embeddings from microscopy images. It serves as a minimal, research-driven sandbox for evaluating embedding structure and preparing for future robustness and semantic validation benchmarks.

## Overview

Modern self-supervised models like MAEs offer powerful representations without requiring labeled data. This project investigates how these embeddings behave when applied to microscopy images, with a focus on similarity, normalization, and eventual retrieval robustness.

The goal is to inform downstream tasks such as semantic search, model explainability, and drift detection in high-dimensional scientific datasets.

## Contents

- [`notebooks/01_embedding_exploration.ipynb`](notebooks/01_embedding_exploration.ipynb): Loads sample images, extracts embeddings using a pretrained vision model, applies interquartile mean normalization, and visualizes similarities.
- `src/`: Placeholder for embedding utilities and vector search code (optional modular components).
- `examples/`: Public or synthetic example images used for demo purposes.
- `requirements.txt`: Reproducible Python environment setup.

## Goals

- Use pretrained MAE-like vision models for inference on microscopy images
- Analyze embedding structure and distance consistency
- Visualize pairwise similarity and t-SNE projections
- Lay the groundwork for robustness testing and model validation

## Future Directions

- Benchmark across multiple pretrained models and augmentations
- Explore distribution shift and retrieval consistency
- Integrate FAISS or Redis for scalable similarity search
- Evaluate explainability tools and failure mode diagnostics

## Notes

This project is based on independent research using public models and synthetic or non-sensitive images. No proprietary data or institutional code is included.

This repository explores the use of pretrained Masked Autoencoders (MAEs) to extract feature embeddings from real microscopy images. It serves as a minimal research sandbox for investigating embedding structure, robustness, and semantic similarity under biologically noisy conditions.

The project is aligned with goals in model validation, representation stability, and semantic retrieval in high-dimensional scientific imaging.

## Project Overview

Masked Autoencoders (MAEs) generate patch-level embeddings that can be pooled into compact image representations. In this project, we:

- Apply facebook/vit-mae-base to microscopy images from the BBBC006 dataset
- Visualize embeddings using cosine similarity and t-SNE
- Analyze embedding drift under Gaussian noise perturbations
- Compare clean vs noisy embeddings to understand model robustness

## Repository Structure

```
mae-microscopy-embeddings/
├── notebooks/
│ ├── 01_exploration.ipynb # Core embedding + robustness notebook
│ └── 99_summary.md # Project summary and next steps
├── examples/
│ ├── bbbc_subset/ # ~20 sample images (see README inside)
│ └── README.md # Download + setup instructions
├── requirements.txt # Project dependencies
├── README.md # You are here
```
## Getting Started

1. Clone this repository

2. Download the BBBC006 image dataset from:
    https://data.broadinstitute.org/bbbc/BBBC006/BBBC006_v1_z16_images.zip
3. Place approximately 20 .tif files in examples/bbbc_subset/
4. Create a virtual environment and install dependencies:
```
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
```
5. Open notebooks/01_exploration.ipynb and run through the analysis

## Features Demonstrated

- Embedding extraction via Hugging Face ViTMAEModel
- Patch pooling (mean over tokens) for full-image representation
- Pairwise cosine similarity matrices
- t-SNE projections of clean vs noisy inputs
- L2 drift metrics under Gaussian perturbation

## Dataset Notes

The example images are from the BBBC006 dataset, part of the Broad Bioimage Benchmark Collection. They were acquired from a single 384-well microplate containing U2OS cells stained with Hoechst 33342 (to label nuclei).

Images were captured under the following conditions:
- Exposure time: 15 ms for Hoechst, 1000 ms for phalloidin
- Magnification: 20x with 2x binning
- Acquisition: 2 sites per well
- Focusing: Laser auto-focusing at the well bottom, followed by a z-stack of 32 images per site
    - 16 slices at the optimal focal plane
    - 15 slices above and 16 below the focal plane
    - Z-step interval: 2 μm
- Image dimensions: 696 x 520 pixels
- Format: 16-bit TIFF, LZW compressed
- Markers: Filenames containing 'w1' indicate Hoechst images; 'w2' indicates phalloidin
- Camera pixel size: 6.45 μm
- Objective numerical aperture (NA): 0.45

These conditions introduce realistic variability in focus, brightness, and morphology, making the dataset well-suited for evaluating embedding robustness and semantic consistency in microscopy image models.

Source: Broad Bioimage Benchmark Collection (https://bbbc.broadinstitute.org/BBBC006)

See examples/README.md for setup details.

## Summary and Future Work

A full summary is included in:

- The final notebook cell in 01_exploration.ipynb
- notebooks/99_summary.md

Planned extensions include:

- Benchmarking across pretrained transformer-based vision models (e.g., ViT, MAE variants)
- Evaluating robustness to input perturbations (blur, brightness shifts, cropping)
- Analyzing embedding drift under biological and technical variability
- Integrating similarity search with FAISS for prototype semantic retrieval
- Exploring t-SNE and clustering behavior across deeper z-stacks and other imaging modalities
- Investigating patch-wise attribution or interpretability tools for embedding diagnostics

## Disclaimer

This project uses public models and data. No proprietary code or sensitive information is included.