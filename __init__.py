import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize
import matplotlib.cm as cm

plt.register_cmap(name = 'nanoanalysis_bright', cmap=nanoanalysis_bright)
plt.register_cmap(name = 'nanoanalysis_muted', cmap=nanoanalysis_bright)
plt.register_cmap(name = 'nanoanalysis_hazy', cmap=nanoanalysis_bright)
