"""
at652.chapter_1
===============

This module provides helper functions for the first chapter of the Machine Learning for Remote Sensing
short course of AT652.
"""
from typing import List, Optional, Tuple

import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize, LogNorm
from matplotlib.gridspec import GridSpec
import numpy as np


def plot_loss_landscape(
        theta_grid: np.ndarray,
        loss_grid: np.ndarray,
        theta_true: Optional[float] = None,
        split_cb: bool = False
) -> Tuple[plt.Figure, plt.Axes, plt.Axes]:
    fig = plt.figure(figsize=(6, 4))
    gs = GridSpec(2, 2, width_ratios=[1.0, 0.075])

    ax = fig.add_subplot(gs[:, 0])
    m = ax.contourf(theta_grid[0], theta_grid[1], loss_grid, cmap="Greys")

    if theta_true is not None:
        ax.scatter(theta_true[0], theta_true[1], marker="x", color="k", label="Explicit solution")
        ax.legend()

    ax.set_xlabel(r"$\theta_1$")
    ax.set_ylabel(r"$\theta_2$");

    if split_cb:
        cax_1 = fig.add_subplot(gs[0, 1])
        cax_2 = fig.add_subplot(gs[1, 1])
    else:
        cax_1 = fig.add_subplot(gs[:, 1])
        cax_2 = None
    plt.colorbar(m, label=rf"$L(\theta)$", cax=cax_1)

    return fig, ax, cax_2

def plot_optimization_steps(
        ax: plt.Axes,
        steps: List[np.ndarray],
        cmap="plasma",
        cax: Optional[plt.Axes] = None,
        label_end_points: bool = False,
        label: Optional[str] = None
):

    n_steps = len(steps)
    cmap = ScalarMappable(LogNorm(1, n_steps - 1), cmap=cmap)

    for step_ind in range(len(steps) - 1):
        curr_step = steps[step_ind]
        next_step = steps[step_ind + 1]
        x = [curr_step[0], next_step[0]]
        y = [curr_step[1], next_step[1]]
        ax.plot(x, y, c=cmap.to_rgba(step_ind + 1))

    if label_end_points:
        ax.scatter(*steps[0], color=cmap.to_rgba(1), label="Initial guess", marker="x")
        ax.scatter(*steps[-1], color=cmap.to_rgba(n_steps), label=f"Step {n_steps}", marker="x")
        ax.legend()

    if label is not None:
        cntr = steps[0]
        ax.text(cntr[0], cntr[1], s=label)

    if cax is not None:
        plt.colorbar(cmap, label="Optimization step", cax=cax)
