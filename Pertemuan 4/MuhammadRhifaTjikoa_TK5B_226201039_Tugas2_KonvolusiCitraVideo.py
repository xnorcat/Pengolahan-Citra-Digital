import numpy as np
import cv2

# Mengambil video dari direktori
# camera = cv2.VideoCapture("MuhammadRhifaTjikoa_TK5B_226201039_Tugas2_KonvolusiCitra.mp4")
camera = cv2.VideoCapture("C:\\Users\mrhitj\\Documents\\Python Code\\Pengolahan Citra Digital\\Screen Recording 2024-09-11 193252.mp4")

#konvolusi manual
# Definisi fungsi konvolusi manual dengan parameter citra dan kernel
def konvolusi(image, kernel):
    # Mengambil nilai lebar dan tinggi dari citra
    row,col= image.shape
    # Mengambil nilai lebar dan tinggi dari kernel
    mrow,mcol=kernel.shape
    h = int(mrow/2) # Mengambil setengah tinggi dari kqernel

    # Membuat citra kosong atau citra penuh dengan piksel hitam yang setiap pikselnya berukuran 8bit
    canvas = np.zeros((row,col),np.uint8)

    for i in range(0,row): # Perulangan untuk membaca setiap baris dari citra
        for j in range(0,col): # Perulangan untuk membaca setiap kolom dari citra
            if i==0 or i==row-1 or j==col-1: # Memeriksa apakah piksel saat ini berada di tepi gambar
                canvas.itemset((i,j),0) # Ubah piksel tersebut menjadi hitam
            else: # Memeriksa apakah piksel saat ini bukan berada di tepi citra
                imgsum=0 # Deklarasi variable untuk penempatan hasil penjumlahan dari hasil perkalian citra dengan kernel
                for k in range (-h, mrow-h): # Perulangan untuk membacca setiap baris dari kernel
                    for l in range (-h, mcol-h): # Perulangan untuk membaca setipa kolom dari kernel
                        res=image[i+k,j+l] * kernel[h+k,h+l] # Perkalian piksel citra dengan piksel kernel
                        imgsum+=res  # Tambahkan hasil perkalian ke variable imgsum
                    canvas.itemset((i,j), imgsum) # Ubah piksel tersebut menjadi hasil konvolusi
    return canvas # Mengembalikan hasil konvolusi

# Definisi fungsi kernel High Pass Filter dengan parameter citra
def kernel1(image):
    # Kernel High Pass Filter  dengan setiap pikselnya merupakan nilai float 32-bit
    kernel = np.array([[-1/9, -1/9, -1/9],[-1/9, 8/9, -1/9],[-1/9, -1/9, -1/9]],np.float32)
    canvas = konvolusi(image, kernel) # Lakukan proses konvolusi lalu simpan ke variable canvas
    print("Hasil konvolusi kernel1 = ", canvas) # Cetak piksel hasil konvolusi
    return canvas # Mengembalikan hasil konvolusi

# Definisi fungsi kernel Low Pass Filter dengan parameter citra
def kernel2(image):
    # Kernel Low Pass Filter dengan setiap pikselnya merupakan nilai float 32-bit
    kernel = np.array([[0, 1/8, 0],[1/8, 1/2, 1/8],[0, 1/8, 0]],np.float32)
    canvas2 = konvolusi(image, kernel) # Lakukan proses konvolusi lalu simpan ke variable canvas2
    print("Hasil konvolusi kernel2 = ", canvas2) # Cetak piksel hasil konvolusi
    return canvas2 # Mengembalikan hasil konvolusi

while True:
    ret, frame = camera.read() # Membaca setiap frame dari video
    image1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Mengubah frame video menjadi warna abu abu

    test1 = kernel1(image1) # Lakukan proses High Pass Filter
    print("gambar1 ordo = ", image1.shape) # Cetak ukuran citra frame
    print("gambar1 ori = ", image1) # Cetak piksel citra frame
    print("gambar1 HPF ordo = ", test1.shape) # Cetak ukuran citra setelah di filter dengan High Pass Filter
    print("gambar1 HPF = ", test1) # Cetak piksel citra setelah di filter dengan High Pass Filter
    cv2.imshow("gambar1",image1) # Tampilkan citra frame di jendela
    cv2.imshow("High pass",test1) # Tampilkan citra frame High Pass Filter di jendela

    test2=kernel2(image1) # Lakukan proses Low Pass Filter pada frame
    print("gambar2 ori ordo = ", image1.shape) # Cetak ukuran frame
    print("gambar2 ori = ", image1) # Cetak piksel frame
    print("gambar1 LPF ordo = ", test2.shape) # Cetak ukuran frame Low Pass Filter
    print("gambar2 LPF = ", test2) # Cetak piksel frame Low Pass Filter
    cv2.imshow("gambar2",image1) # Tampilkan frame di jendela
    cv2.imshow("low pass",test2) # Tampilkan frame Low Pass Filter di jendela

    # Menunda selama 1 detik dan menunggu interupsi dari keyboard jika pengguna menekan 'q'
    if cv2.waitKey(1) == ord('q'):
        break # Hentikan program

camera.release() #Menutup kamera
cv2.destroyAllWindows() #Menutup semua jendela frame

# Spesikasi laptop yang digunakan
# Prosesor : Intel(R) Core(TM) i3-100G51 CPU @ 1.20GHz (4 CPUS,) ~1.20GHz
# Memory   : 8 GB
# GPU      : Intel UHD Graphics G1
# Kesimpulan
# Setelah menjalankan program ini, video yang dijalankan memiliki framerate yang rendah.
# Hal ini karena proses konvolusi dilakukan dua kali di dalam while loop. Di dalam proses konvolusi, konvolusi memiliki nested for loops sebanyak 2 hingga 4 kali.
# Selain itu, waktu proses konvolusi tergantung dengan ukuran frame video. Ukuran video yang digunakan sebesar 182 x 330.
# Adapun selain proses konvolusi yang menyebabkan rendahnya framerate, yaitu mencetak suatu nilai atau fungsi print() dan menampilkan setiap frame dari video.
# Untuk mendapatkan framerate stabil, ada beberapa hal yang dapat dilakukan seperti menggunakan ukuran video yang lebih rendah, menggunakan algoritma konvolusi dengan
# perulangan yang sedikit atau menggunakan algoritma konvolusi yang berbeda, dan menampilkan satu filter untuk satu program.
