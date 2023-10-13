# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:49:57 2023

@author: ASUS
"""
print('ARIF WARDANA/5009211030')
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghasilkan sinyal kotak periodik
def generate_square_wave(t, duration):
    signal = np.where((t >= -duration / 2) & (t <= duration / 2), 2, 0)
    return signal

# Parameter sinyal
t1 = np.linspace(-1, 1, 2000, endpoint=False)  # Rentang waktu: -1 hingga 1 detik
t2 = np.linspace(-0.5, 0.5, 1000, endpoint=False)  # Rentang waktu: -1/2 hingga 1/2 detik
t3 = np.linspace(-3, 3, 6000, endpoint=False)  # Rentang waktu: -3 hingga 3 detik

# Proses pembuatan sinyal kotak
signal1 = generate_square_wave(t1, 1)
signal2 = generate_square_wave(t2, 1)
signal3 = generate_square_wave(t3, 1)

# Transformasi Fourier menggunakan NumPy
F1 = np.fft.fftshift(np.fft.fft(signal1))
F2 = np.fft.fftshift(np.fft.fft(signal2))
F3 = np.fft.fftshift(np.fft.fft(signal3))

# Frekuensi
frequencies1 = np.fft.fftshift(np.fft.fftfreq(len(t1), 1 / 2000))
frequencies2 = np.fft.fftshift(np.fft.fftfreq(len(t2), 1 / 1000))
frequencies3 = np.fft.fftshift(np.fft.fftfreq(len(t3), 1 / 6000))

# Plot hasil
plt.figure(figsize=(12, 6))

plt.subplot(3, 2, 1)
plt.plot(t1, signal1)
plt.title('Sinyal Kotak: -1 s/d 1 Detik')

plt.subplot(3, 2, 2)
plt.plot(frequencies1, np.abs(F1))
plt.title('Transformasi Fourier: -1 s/d 1 Detik')
plt.xlim(-20, 20)  # Menampilkan frekuensi hingga 20 Hz

plt.subplot(3, 2, 3)
plt.plot(t2, signal2)
plt.title('Sinyal Kotak: -1/2 s/d 1/2 Detik')

plt.subplot(3, 2, 4)
plt.plot(frequencies2, np.abs(F2))
plt.title('Transformasi Fourier: -1/2 s/d 1/2 Detik')
plt.xlim(-40, 40)

plt.subplot(3, 2, 5)
plt.plot(t3, signal3)
plt.title('Sinyal Kotak: -3 s/d 3 Detik')

plt.subplot(3, 2, 6)
plt.plot(frequencies3, np.abs(F3))
plt.title('Transformasi Fourier: -3 s/d 3 Detik')
plt.xlim(-10, 10)

plt.tight_layout()
plt.show()
