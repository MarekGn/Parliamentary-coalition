import matplotlib

# fig_width 80mm (here size in inches)
fig_width = 3.34*1.25
fig_height = 2.2*1.25
linewidths=0.75
tickwidths=0.8*linewidths
tickminor=1.5
tickmajor=2*tickminor
params = {
			'font.size':12/1.0,
			'axes.labelsize': 12/1.0,
			'axes.titlesize': 12/1.0,
			'legend.fontsize': 8/1.0,
			'xtick.labelsize': 8.5/1.0,
			'ytick.labelsize': 8.5/1.0,
			
			'font.family': 'serif',
			'xtick.direction': 'in',
			'ytick.direction': 'in',
			'ytick.major.width': tickwidths,
			'xtick.major.width': tickwidths,
			'ytick.minor.width': tickwidths,
			'xtick.minor.width': tickwidths,
			'ytick.minor.size': tickminor,
			'xtick.minor.size': tickminor,
			'ytick.major.size': tickmajor,
			'xtick.major.size': tickmajor,
			'ytick.right': True,
			'xtick.top': True,
			'text.usetex': True,
			'figure.figsize': [fig_width, fig_height],

			'axes.linewidth': linewidths,
			'lines.linewidth': linewidths,
			'lines.markeredgewidth': linewidths,
			'lines.markersize': 4,
			'legend.frameon': True,
			'legend.handlelength': 1,
			'ps.usedistiller': 'xpdf',
}
matplotlib.rcParams.update(params)