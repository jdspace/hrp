# %% imports
import matplotlib
matplotlib.use("TkAgg")    # <-- Add this line
import numpy as np
import matplotlib.pyplot as plt

# %% quick test
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("VS Code + Python is working!")
plt.show()

# %% imports
import sys
import numpy as np
import matplotlib.pyplot as plt

print("Python executable:", sys.executable)

# %% quick test
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Local HRP venv is working!")
plt.show()

# %%
