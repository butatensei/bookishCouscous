import numpy as np
import imageio
import matplotlib.pyplot as plt
from scipy import misc
img = np.array(imageio.imread("spritesheet.png"))
img = misc.toimage(img)
print(type(img))
img.show()
