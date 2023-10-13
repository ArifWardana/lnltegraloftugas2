# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 19:01:02 2023

@author: ASUS
"""
print('ARIF WARDANA/5009211030')
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghasilkan sinyal kotak periodik 2D
def generate_2d_square_wave(t, duration_x, duration_y):
    signal = np.zeros((len(t), len(t)), dtype=float)
    for i in range(len(t)):
        for j in range(len(t)):
            if (-duration_x / 2 < t[i] < duration_x / 2) and (-duration_y / 2 < t[j] < duration_y / 2):
                signal[i][j] = 2
    return signal

# Parameter sinyal
t = np.linspace(-3, 3, 6000, endpoint=False)  # Rentang waktu: -3 hingga 3 detik

# Proses pembuatan sinyal kotak 2D
signal1 = generate_2d_square_wave(t, 1, 1)
signal2 = generate_2d_square_wave(t, 1, 1)
signal3 = generate_2d_square_wave(t, 3, 3)

# Transformasi Fourier 2D menggunakan NumPy
F1 = np.fft.fftshift(np.fft.fft2(signal1))
F2 = np.fft.fftshift(np.fft.fft2(signal2))
F3 = np.fft.fftshift(np.fft.fft2(signal3))

# Frekuensi
frequencies = np.fft.fftshift(np.fft.fftfreq(len(t), 1 / 6000))

# Plot hasil
plt.figure(figsize=(12, 6))

plt.subplot(3, 2, 1)
plt.imshow(signal1, extent=[-3, 3, -3, 3], cmap='gray')
plt.title('Sinyal Kotak 2D: -1 s/d 1 Detik')

plt.subplot(3, 2, 2)
plt.imshow(np.abs(F1), extent=[-3, 3, -3, 3], cmap='inferno', origin='lower')
plt.title('Transformasi Fourier 2D: -1 s/d 1 Detik')

plt.subplot(3, 2, 3)
plt.imshow(signal2, extent=[-3, 3, -3, 3], cmap='gray')
plt.title('Sinyal Kotak 2D: -1/2 s/d 1/2 Detik')

plt.subplot(3, 2, 4)
plt.imshow(np.abs(F2), extent=[-3, 3, -3, 3], cmap='inferno', origin='lower')
plt.title('Transformasi Fourier 2D: -1/2 s/d 1/2 Detik')

plt.subplot(3, 2, 5)
plt.imshow(signal3, extent=[-3, 3, -3, 3], cmap='gray')
plt.title('Sinyal Kotak 2D: -3 s/d 3 Detik')

plt.subplot(3, 2, 6)
plt.imshow(np.abs(F3), extent=[-3, 3, -3, 3], cmap='inferno', origin='lower')
plt.title('Transformasi Fourier 2D: -3 s/d 3 Detik')

plt.tight_layout()
plt.show()
