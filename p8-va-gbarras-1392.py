import matplotlib.pyplot as plt
import numpy as np

diasX=["Lun","Mar","Mie","Jue","Vie"]
califa_va_y=[5,6,3,8,10]
plt.bar(diasX,califa_va_y)
plt.title("Califa en VA de Daniel Gallegos NC 1392")
plt.xlabel("Dias de semana habil")
plt.ylabel("Calificacion en VA")
plt.grid()
plt.show()