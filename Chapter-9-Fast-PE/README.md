# Chapter 9 – Accelerating Parameter Estimation

Companion code for Chapter 9 of *The Gravitational-Wave Revolution: Methods, Workflows,
and the Future of Discovery*.

Everything is organized in Jupyter notebooks. Each notebook explains what it does and can
be run from top to bottom. The notebooks are saved with their output, so they can also
simply be read on GitHub.

## Contents

### `tutorial/` – a Dingo toy model that runs on a laptop

A small neural network is trained to measure the chirp mass and the luminosity distance of
a binary black hole observed by the LIGO and Virgo detectors. All other parameters are fixed.
No GPU is needed.

| Notebook | What it does | Run time (2 CPU cores) |
|---|---|---|
| `1_training.ipynb` | Generates the waveforms, prepares the noise curves, trains the network, plots the learning curve | about 10 minutes |
| `2_inference.ipynb` | Analyses one simulated signal and compares with the exact posterior | about 1 minute |
| `3_validation.ipynb` | Analyses 100 simulated signals: sample efficiency and P-P plot | about 4 minutes |

Run them in this order. The two settings files, `waveform_dataset_settings.yaml` and
`train_settings.yaml`, are read by the notebooks and are commented line by line.
The file `training_data/asd_dataset.hdf5` contains the detector noise curves; it is created
by the first notebook and is included here for convenience.

The notebooks save the results of their slow steps on your computer: the trained network in
`training/`, and the results of notebooks 2 and 3 in `results/`. When these files exist they
are reused, so running a notebook again (for example to change a plot) takes a few seconds.
Delete a folder to compute its content again. These files are not part of the repository.

### `figures/` – the illustrative figures of the chapter

| Notebook | Figure |
|---|---|
| `fig_signal_duration.ipynb` | Time to merger versus frequency, and a sketch of pre-merger localization (Fig. 9.1) |
| `fig_data_stream.ipynb` | Simulated data stream of a next-generation detector (Fig. 9.2) |
| `fig_likelihood_methods.ipynb` | Relative binning, multibanding and reduced-order quadrature (Fig. 9.4) |
| `fig_normalizing_flow.ipynb` | A normalizing flow in one dimension (Fig. 9.5) |

The file `gwr_style.py` contains the plotting style shared by all notebooks.

## Where are the figures?

Each notebook saves its figures as PDF files in a folder called `output` next to it:
`figures/output/` and `tutorial/output/`.

## Installation

```bash
pip install -r requirements.txt
```

The tutorial was written for Dingo version 0.10.

## A note on the figures

Some figures are illustrations, not results of analyses: the sketch of pre-merger
localization, the simulated data stream, and the panels on relative binning, multibanding and
reduced-order quadrature. Each notebook says so at the top. The figures of the tutorial
are real results of the toy model.
