import matplotlib.pyplot as plt
from .colormaps import nanoanalysis_bright, nanoanalysis_muted, nanoanalysis_hazy

plt.register_cmap(name = 'nanoanalysis_bright', cmap=nanoanalysis_bright)
plt.register_cmap(name = 'nanoanalysis_muted', cmap=nanoanalysis_bright)
plt.register_cmap(name = 'nanoanalysis_hazy', cmap=nanoanalysis_bright)
