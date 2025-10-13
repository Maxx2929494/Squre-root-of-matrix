import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib import gridspec

"""

Visualization: 
Plot square root of eigenvalues (\mu_j) in complex plane
Draw circles with radius 2|\mu_j| centred at mu_j 
Satsifying property is equivalent to all eignvalues laying in **all** circles

Mark eigenvalues that violate this condition with red

Shows heatmap on right-hand side matrix form to show which pairs violate.

"""
def plot_stability_circles(eigvals,figsize=(11,6),dpi=300,save_path=None,show_indices=True,cmap='viridis'):

    # Convert to numpy array and compute principal square roots
    lam = np.array(eigvals, dtype=complex).flatten()

    mu = np.sqrt(lam)  # principal complex square root

    # Build pairwise matrix S[i,j] = 0.5 * |1 - mu_i/mu_j| with careful division
    # assuming mu = np.sqrt(lam)
    n = mu.size
    ratio = mu[:, None] / mu[None, :]
    S = 0.5 * np.abs(1 - ratio)
    np.fill_diagonal(S, 0.0)
    max_S = np.max(S)


    # remove diagonal (i==j) from consideration
    np.fill_diagonal(S, 0.0)

    # maximum 
    max_S = np.nanmax(S)  
    stable = (max_S < 1.0)

    # find violating pairs
    violating = list(zip(*np.where(S >= 1.0)))
    # find eigenvalues 
    participating = np.zeros(n, dtype=bool)
    for (i, j) in violating:
        participating[i] = True
        participating[j] = True

    # Prepare figure with a main axes and a side heatmap
    plt.rcParams.update({
        "font.size": 11,
        "axes.titlesize": 12,
        "axes.labelsize": 11,
        "legend.fontsize": 10,
        "figure.dpi": dpi
    })

    fig = plt.figure(figsize=figsize, dpi=dpi)
    gs = gridspec.GridSpec(1, 3, width_ratios=[2.2, 0.05, 1.2], wspace=0.35)

    ax_main = fig.add_subplot(gs[0,0])
    ax_heat = fig.add_subplot(gs[0,2])



    # MAIN PLOT: complex plane scatter + circles
    x = mu.real
    y = mu.imag
    radii = 2.0 * np.abs(mu)

    # plot circles
    for j in range(n):
        circ = Circle((x[j], y[j]), radii[j],
                      fill=False, linewidth=1.1, linestyle='--', alpha=0.45)
        ax_main.add_patch(circ)

    # scatter points: red if participating in any violation, else blue
    colors = np.array(['tab:blue']*n)
    colors[participating] = 'tab:red'
    sizes = np.full(n, 70)
    sizes[participating] = 120

    ax_main.scatter(x, y, s=sizes, c=colors, edgecolor='k', zorder=5)
    if show_indices:
        for k, (xx, yy) in enumerate(zip(x, y)):
            ax_main.text(xx, yy, f'  {k}', fontsize=9, verticalalignment='center', horizontalalignment='left')

    # axis formatting
    ax_main.axhline(0, color='lightgray', linestyle='-', linewidth=0.8)
    ax_main.axvline(0, color='lightgray', linestyle='-', linewidth=0.8)
    ax_main.set_aspect('equal', adjustable='datalim')
    ax_main.set_xlabel(r'$\Re(\sqrt{\lambda})$')
    ax_main.set_ylabel(r'$\Im(\sqrt{\lambda})$')
    ax_main.grid(True, linestyle=':', linewidth=0.6)

    # Legend
    from matplotlib.lines import Line2D
    legend_elems = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor='tab:blue', markeredgecolor='k', markersize=8, label='satisfying'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='tab:red', markeredgecolor='k', markersize=8, label='violating'),
        Line2D([0], [0], linestyle='--', color='gray', label=r'Circle: $B(\mu_j,2|\mu_j|)$')
    ]
    ax_main.legend(handles=legend_elems, loc='upper left')

    
    ax_main.set_title("Stability condition for eigenvalues commutating method")

    # HEATMAP: show S matrix
    im = ax_heat.imshow(S, interpolation='nearest', cmap=cmap, origin='lower')
    ax_heat.set_title(r"Pairwise $\frac{1}{2}\left|1-\frac{\mu_i}{\mu_j}\right|$")
    ax_heat.set_xlabel(r"$j$")
    ax_heat.set_ylabel(r"$i$")
    # annotate values up to reasonable length
    for (i, j), val in np.ndenumerate(S):
        if i == j:
            continue
        if np.isinf(val):
            txt = "inf"
        else:
            txt = f"{val:.2f}"
        ax_heat.text(j, i, txt, ha='center', va='center', fontsize=8, color='w' if val > (np.nanmax(S)/2 + 1e-12) else 'k')


    # annotate violating pairs in the heatmap 
    if violating:
        for (i, j) in violating:
            ax_heat.plot(j, i, marker='s', markerfacecolor='none', markeredgecolor='red', markersize=10, markeredgewidth=1.4)

    # tight layout
    plt.tight_layout()

    # save if requested
    if save_path is not None:
        try:
            plt.savefig(save_path, bbox_inches='tight', dpi=dpi)
            print(f"Saved figure to {save_path}")
        except Exception as e:
            warnings.warn(f"Could not save figure to {save_path}: {e}")

    return fig, ax_main, {'S': S, 'max_S': max_S, 'violating_pairs': violating}, stable


if __name__ == "__main__":
    example_eigs = np.array([4.0, 1.0+0.5j, 0.25, 0.9-0.2j])
    fig, ax, H, stable_flag = plot_stability_circles(example_eigs, save_path=None)
    plt.show()

