import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Convergence plots for a given method
# Applied to multiple matrices
def plot_convergence(it_lists, err_lists, labels=None, logy=True, figsize=(7,4.5), linewidth=1.5, markersize=2, filename=None, title=None):


    plt.rcParams.update({'figure.dpi':300,'font.size':10,'axes.labelsize':11,'axes.titlesize':11,'legend.fontsize':9,'xtick.labelsize':9,'ytick.labelsize':9})
    fig, ax = plt.subplots(figsize=figsize)
    markers = ['o','s','^','D','v','P']

    for i, (it,err) in enumerate(zip(it_lists, err_lists)):
        ax.plot(it, err, marker=markers[i%len(markers)], markersize=markersize, linewidth=linewidth, label=(labels[i] if labels and i<len(labels) else f'run {i+1}'))

    # Change axis if logy is enabled.
    if logy:
        ax.set_yscale('log')
        ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: ('{:.0e}'.format(y) if y<1 else '{:.0e}'.format(y))))

    # Layout of figure
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Relative error')
    ax.grid(which='both', linestyle='--', linewidth=0.5, alpha=0.7)
    ax.legend(frameon=False, ncol=2, loc='upper right')

    # Set title
    if title:
        ax.set_title(title)

    fig.tight_layout()
    if filename:
        fig.savefig(filename, bbox_inches='tight', dpi=600)
    return fig, ax