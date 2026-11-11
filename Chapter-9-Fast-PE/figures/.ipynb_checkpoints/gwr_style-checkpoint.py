"""Common plotting style for the figures of Chapter 9, "Accelerating Parameter Estimation".

Every notebook imports this small module, so that all figures share the same fonts,
sizes and colours.

    from gwr_style import COLORS, TEXTWIDTH, save_figure, use_book_style
"""
import os

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.projections import register_projection

# Width of the text block of the book (111.5 mm), converted to inches.
# A figure created with this width is printed at its natural size.
TEXTWIDTH = 111.5 / 25.4

# The colour palette used in all figures and flowcharts.
COLORS = {
    "blue": "#2B4C7E",
    "lightblue": "#8FB8DE",
    "orange": "#E0861A",
    "teal": "#2A9D8F",
    "magenta": "#A8326B",
    "grey": "#6B6B6B",
    "lightgrey": "#D9D9D9",
}

def use_book_style():
    """Apply the plotting style of the book.

    The style is applied when this module is imported. Some packages change the
    plotting settings when they are used; call this function again before making a
    figure to restore the style of the book.
    """
    mpl.rcdefaults()
    # Some packages replace the standard matplotlib axes with their own version,
    # which draws thick lines in legends. Go back to the standard axes.
    register_projection(Axes)
    mpl.rcParams.update(
        {
            # A Times-like font, to match the text of the book.
            "font.family": "serif",
            "font.serif": ["TeX Gyre Termes", "Times New Roman", "Times", "DejaVu Serif"],
            "mathtext.fontset": "stix",
            # Font sizes, in points.
            "font.size": 8,
            "axes.labelsize": 8,
            "axes.titlesize": 8,
            "legend.fontsize": 7,
            "xtick.labelsize": 7,
            "ytick.labelsize": 7,
            # Thin lines for axes and ticks; ticks point inwards.
            "axes.linewidth": 0.6,
            "xtick.major.width": 0.6,
            "ytick.major.width": 0.6,
            "xtick.minor.width": 0.4,
            "ytick.minor.width": 0.4,
            "xtick.direction": "in",
            "ytick.direction": "in",
            "lines.linewidth": 1.2,
            # Legends are drawn inside a thin box.
            "legend.frameon": True,
            "legend.fancybox": False,
            "legend.edgecolor": "#6B6B6B",
            "legend.framealpha": 1.0,
            "patch.linewidth": 0.5,
            "figure.dpi": 150,
            "savefig.dpi": 300,
        }
    )


use_book_style()


def save_figure(fig, name, folder="output"):
    """Save a figure as a PDF file in the folder `output`, next to the notebook."""
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, name)
    fig.savefig(path, bbox_inches="tight", pad_inches=0.02)
    print("Figure saved to", path)
