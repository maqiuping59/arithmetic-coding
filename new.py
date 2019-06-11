from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,100)
y = np.sin(x)
plt.plot(x,y)
plt.title('马秋平')
plt.show()