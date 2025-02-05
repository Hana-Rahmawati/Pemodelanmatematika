# -*- coding: utf-8 -*-
"""kesetimbangan .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10hl0LStV0DHIWacWxmlVR5YSPObjEnbo
"""

import numpy as np
import matplotlib.pyplot as plt

# Rentang nilai x dan waktu untuk medan vektor
x = np.arange(0, 3, 0.1)
t = np.arange(0, 4, 0.1)
T, X = np.meshgrid(t, x)

# Definisikan sistem
dX = -X**2 + 3 * X - 2
dT = np.ones(dX.shape)

# Plot stream plot
plt.figure(figsize=(8, 6))
plt.streamplot(T, X, dT, dX, color=dX, cmap='coolwarm', linewidth=1)

plt.title("Stream Plot of the System")
plt.xlabel("Time(t)")
plt.ylabel("x")
plt.axhline(0, color='gray', linestyle= '--')
plt.colorbar(label='dx/dt')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Parameter konstanta
k = 0.1 # konstanta pendinginan
Ta = 25 # suhu lingkungan

# DEFINISI SISTEM PERSAMAAN DIFERENSIAL
def system(T):
    return k * (Ta - T)

# Membuat grid untuk visualisasi
t_vals = np.linspace(0, 50, 20)  #Rentang waktu
T_vals = np.linspace(0, 50, 20)  # Rentang suhu
t, T = np.meshgrid(t_vals, T_vals)  #Perbaikan urutan meshgrid

# Menghitung vektor arah
U = np.ones_like(T) #Arah horisontal tetap untuk menunjukkan perubahan dalam waktu
V = system(T)     # Arah vertikal mengikuti sistem persaman diferensial

# Plot medan vektor menggunakan streamplot
plt.figure(figsize=(7, 5))
plt.streamplot(t, T, U, V, color='blue')
plt.axhline(Ta, color='red', linestyle='--', label='solusi setimbang (T = Ta)')
plt.xlabel('waktu (t)')
plt.ylabel('suhu (t)')
plt.title('Medan vektor pendinginan')
plt.legend()
plt.grid()
plt.show()