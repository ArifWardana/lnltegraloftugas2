# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 17:10:52 2023

@author: ASUS
"""
print('Arif Wardana/ 5009211030')

def convolution_1d(signal, kernel):
    # Menghitung panjang sinyal masukan dan kernel
    signal_len = len(signal)
    kernel_len = len(kernel)
    
    # Panjang hasil konvolusi adalah panjang sinyal + panjang kernel - 1
    result_len = signal_len + kernel_len - 1
    
    # Inisialisasi array hasil dengan nilai nol
    result = [0] * result_len

    # Iterasi melalui semua indeks hasil
    for i in range(result_len):
        # Iterasi melalui semua indeks kernel
        for j in range(kernel_len):
            # Pastikan indeks saat ini dalam rentang sinyal masukan
            if i - j >= 0 and i - j < signal_len:
                # Lakukan perkalian antara elemen sinyal dan kernel yang sesuai
                result[i] += signal[i - j] * kernel[j]

    return result

# Contoh penggunaan:
signal = [1, 2, 3, 4, 5]
kernel = [0.5, 1, 0.5]
result = convolution_1d(signal, kernel)

# Menggunakan NumPy untuk validasi
import numpy as np
numpy_result = np.convolve(signal, kernel, mode='full')

# Membandingkan hasil
print("Hasil Konvolusi Kustom:", result)
print("Hasil Konvolusi NumPy:", numpy_result)