# -*- coding: utf-8 -*-
"""HIV.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gNdPtk96Sxt2vtDsUjaqKhSaODDxMlKR
"""

import numpy as np
import matplotlib.pyplot as plt

# Prameter model
N = 1000          # Total populasi
beta = 0.002      # Tigkat penularan
gamma = 0.1       # Laju perkembangan ke AIDS
mu = 0.01         # Tingkat kematian alami
delta = 0.2       # Tingkat kematian akibat AIDS

# Kondisi awal
H0 = 900
I0 = 80
V0 = 20

# Waktu simulasi
T = 100       # Durasi dalam hari
dt = 1        # Langkah waktu

# Vektor waktu
time = np.arange(0, T + dt, dt)

# Array untuk menyimpan hasil simulasi
H = np.zeros(len(time))
I = np.zeros(len(time))
V = np.zeros(len(time))

# Kondisi awal
H[0] = H0
I[0] = I0
V[0] = V0

# Simulasi dengan metode euler
for t in range(1, len(time)):
  dH = mu * N - beta * H[t-1] * I[t-1] - mu * H[t-1]
  dI = beta * H[t-1] * I[t-1] - (gamma + mu) * I[t-1]
  dV = gamma * I[t-1] - (delta + mu) * V[t-1]

  # Update populasi
  H[t] = H[t-1] + dH * dt
  I[t] = I[t-1] + dI * dt
  V[t] = V[t-1] + dV * dt

# Plot hasil simulasi
plt.figure(figsize=(10, 6))
plt.plot(time, H, label='Rentan (H)', color = 'magenta')
plt.plot(time, I, label='Terinfeksi HIV (I)', color = 'green')
plt.plot(time, V, label='AIDS (V)', color = 'red')
plt.xlabel('Hari')
plt.ylabel('Populasi')
plt.title('Simulasi Penyebaran HIV/AIDS selama 100 hari')
plt.legend()
plt.grid(True)
plt.show()