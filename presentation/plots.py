import numpy as np
import matplotlib
import matplotlib.pyplot as plt

font = {'family' : 'DejaVu Sans',
        # 'weight' : 'normal',
        'size'   : 22}

matplotlib.rc('font', **font)

save = True

def show_or_save(filename):
    plt.savefig(filename) if save else plt.show()
    plt.close()

def despine(ax):
    for spine in ('top', 'right'):
        ax.spines[spine].set_visible(False)
    
## Beta(2,2)
fig, ax = plt.subplots(figsize=(5, 4))
xspace = np.linspace(0, 1, 100)
ax.plot(xspace, xspace * (1 - xspace) / 6.0)
ax.set_xlim((0, 1))
ax.set_ylim((0,0.05))
ax.set_xlabel('$b$')
ax.set_ylabel('$p(b)$')
fig.tight_layout()
despine(ax)
show_or_save('images/coin_flip_prior.pdf')

## l(b)=p(k=1|b)
fig, ax = plt.subplots(figsize=(5, 4))
xspace = np.linspace(0, 1, 100)
ax.plot(xspace, xspace)
ax.set_xlim((0, 1))
ax.set_ylim((0, 1))
ax.set_xlabel('$b$')
ax.set_ylabel('$p(k=1|b)$')
fig.tight_layout()
despine(ax)
show_or_save('images/coin_flip_likelihood.pdf')

## p(b|k=1) a.k.a. Beta(3,2)
fig, ax = plt.subplots(figsize=(5, 4))
xspace = np.linspace(0, 1, 100)
ax.plot(xspace, xspace ** 2 * (1 - xspace))
ax.set_xlim((0, 1))
ax.set_ylim((0, 0.2))
ax.set_xlabel('$b$')
ax.set_ylabel('$p(b|k=1)$')
fig.tight_layout()
despine(ax)
show_or_save('images/coin_flip_posterior.pdf')

## normal
fig, ax = plt.subplots(figsize=(5, 4))
xspace = np.linspace(-3, 3, 100)
ax.plot(xspace, np.exp(-0.5 * xspace ** 2) / np.sqrt(2 * np.pi), color='black')
ax.set_xlim((-3, 3))
ax.set_ylim((0, 0.5))
ax.set_xlabel('$x$')
ax.set_ylabel('$p(x)$')
fig.tight_layout()
despine(ax)
show_or_save('images/normalized_normal.pdf')

## normal and unnormalized normal
fig, ax = plt.subplots(figsize=(5, 4))
xspace = np.linspace(-3, 3, 100)
ax.plot(xspace, np.exp(-0.5 * xspace ** 2) / np.sqrt(2 * np.pi), color='black')
ax.plot(xspace, np.exp(-0.5 * xspace ** 2), color='black', ls='--')
ax.set_xlim((-3, 3))
ax.set_ylim((0, 1.1))
ax.set_xlabel('$x$')
ax.set_ylabel('$p(x)$')
fig.tight_layout()
despine(ax)
show_or_save('images/normalized_unnormalized_normal.pdf')

## Bernoulli(0.2)
fig, ax = plt.subplots(figsize=(5, 4))
ax.scatter((2, 4), (0.8, 0.2), marker='o')
ax.axvline(2, ymax=0.8, color='black', ls='--')
ax.axvline(4, ymax=0.2, color='black', ls='--')
ax.set_xticks((2, 4))
ax.set_xticklabels(('0 (tail)', '1 (head)'))
ax.set_xlim((1, 5))
ax.set_ylim((0, 1))
ax.set_xlabel('$k$')
ax.set_ylabel('$p(k)$')
fig.tight_layout()
despine(ax)
show_or_save('images/bernoulli.pdf')
