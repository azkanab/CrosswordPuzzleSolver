import time
start_time = time.time()
#BUKA FILE
file_tts = open("uji4.txt", "r")

#BACA FILE

#Baca Ukuran Matriks
x = file_tts.readline()
nmatriks = int(x)

#Baca Matriks
matrikstts = []
for i in range (0,nmatriks):
	kolomtts = []
	for j in range (0,nmatriks):
		karakter = file_tts.read(1)
		kolomtts.append(karakter)
	file_tts.read(1) #untukenterfile
	matrikstts.append(kolomtts)
	
print()                                              
print("                 ooo.    o 8                ooooo ooooo .oPYo. ")
print("                 8  `8.    8                  8     8   8      ")
print("                 8   `8 o8 8 .oPYo. odYo.     8     8   `Yooo. ")
print("                 8    8  8 8 .oooo8 8' `8     8     8       `8 ")
print("                 8   .P  8 8 8    8 8   8     8     8        8 ")
print("                 8ooo'   8 8 `YooP8 8   8     8     8   `YooP' ")
print("                 .....:::....:.....:..::..::::..::::..:::.....:")
print("                 ::::::::::::::::::::::::::::::::::::::::::::::")
print("                 ::::::::::::::::::::::::::::::::::::::::::::::")                                                                                         
print()
print("======================= Menyelesaikan TTSmu dengan mudah! ==========================")
print()
print()
print(">>>>>>>>>>>>>>>>>>>>>>>> TTS KOSONG <<<<<<<<<<<<<<<<<<<<<<<<<<")
print()
for a in range (0,nmatriks):
	for b in range (0,nmatriks):
		print(matrikstts[a][b], end=' ')
	print()

#Baca List Jawaban
kata = file_tts.readline()
listkata = kata.split(";")
print()
print(" ==================== DAFTAR KATA =========================")
print()
print(listkata)

file_tts.close() #tutup file yang telah terbuka

#MENGHITUNG PANJANG HURUF PADA SEBUAH KATA
def panjanghurufmendatar(matriks,i,j):
	panjang = int(1)
	j = j + 1
	while (matriks[i][j] == "-"):
		panjang = panjang + 1
		j = j + 1
	return panjang

def panjanghurufmenurun(matriks,i,j):
	panjang = int(1)
	i = i + 1
	while (matriks[i][j] == "-"):
		panjang = panjang + 1
		i = i + 1
	return panjang

#JUMLAH KATA YANG TERSEDIA	
jmlkata = int(len(listkata))

#MEMBUAT LIST DARI PANJANG HURUF DI SETIAP KATA TTS YANG KOSONG
#Inisialisasi array jumlah huruf perkata dalam puzzle
listjmlkata = []
listtitikawal = []
listtitikakhir = []
jmlkatamendatar = int(0)
jmlkatamenurun = int(0)

#MENDATAR
for i in range (0, nmatriks):
	j = int(0)
	while j < nmatriks+1:
		pjghuruf = int(0)
		if j < nmatriks:
			if matrikstts[i][j] == "-":
				if matrikstts[i][j+1] == "-":
					kolom = []
					kolom.append(i)
					kolom.append(j)
					listtitikawal.append(kolom)
					pjghuruf = panjanghurufmendatar(matrikstts,i,j)
					listjmlkata.append(pjghuruf)
					jmlkatamendatar += 1
		if pjghuruf == 0:
			j = j + 1
		else:
			j = j + pjghuruf
			kolom = []
			kolom.append(i)
			kolom.append(j - 1)
			listtitikakhir.append(kolom)

#MENURUN	
for j in range (0, nmatriks):
	i = int(0)
	while i < nmatriks+1:
		pjghuruf = int(0)
		if i < nmatriks:
			if matrikstts[i][j] == "-":
				if matrikstts[i+1][j] == "-":
					kolom = []
					kolom.append(i)
					kolom.append(j)
					listtitikawal.append(kolom)
					pjghuruf = panjanghurufmenurun(matrikstts,i,j)
					listjmlkata.append(pjghuruf)
					jmlkatamenurun += 1
		if pjghuruf == 0:
			i = i + 1
		else:
			i = i + pjghuruf
			kolom = []
			kolom.append(i - 1)
			kolom.append(j)
			listtitikakhir.append(kolom)
	
#MENCARI KEMUNGKINAN JAWABAN DENGAN PERMUTASI DAN LANGSUNG MENGISI PADA TTSNYA
#Inisialisasi matriks permutasi

def terisi (matrikstts,i,j):
	if matrikstts[i][j] != "-":
		return True
	else:
		return False
		
import itertools
listpermutasi = []

print()
print("==================== LANGKAH - LANGKAH =====================")
print()
for listpermutasi in itertools.permutations(listkata,jmlkata):
	found = True
	for i in range (0,jmlkata):
		if len(listpermutasi[i]) != listjmlkata[i]:
			found = False
	if found:
		for inisialisasi in range (jmlkatamendatar, jmlkatamendatar + jmlkatamenurun): #Inisialisasi isi menurun
			x1 = listtitikawal[inisialisasi][0]
			x2 = listtitikakhir[inisialisasi][0]
			y = listtitikawal[inisialisasi][1]
			for baris in range (x1, x2+1):
				matrikstts[baris][y] = "-"
		#MENDATAR
		for j in range (0, jmlkatamendatar): #Mengakses list kata
			x = listtitikawal[j][0]
			y1 = listtitikawal[j][1]
			y2 = listtitikakhir[j][1]
			kata = list(listpermutasi[j])
			huruf = int(-1)
			for kolom in range (y1, y2+1):
				huruf += 1
				print('Titik (',x,',',kolom,') diisi dengan ', kata[huruf])
				matrikstts[x][kolom] = kata[huruf]
		#MENURUN
		k = jmlkatamendatar
		susunanpermutasimenurun = True
		while k < jmlkatamendatar + jmlkatamenurun and susunanpermutasimenurun : #Mengakses list kata
			x1 = listtitikawal[k][0]
			x2 = listtitikakhir[k][0]
			y = listtitikawal[k][1]
			kata = list(listpermutasi[k])
			huruf = int(-1)
			for baris in range (x1, x2+1):
				huruf += 1
				if not terisi(matrikstts,baris,y):
					print('Titik (',baris,',',y,') diisi dengan ', kata[huruf])
					matrikstts[baris][y] = kata[huruf]
				else: #jika cell matriks sudah terisi dibandingkan apakah hurufnya sama atau tidak dengan yang akan diisi
					if matrikstts[baris][y] != kata[huruf]:
						susunanpermutasimenurun = False #tidak lanjut ke kata berikutnya, namun masih lanjut ke huruf selanjutnya pada kata tersebut
						print("Huruf ",kata[huruf]," tidak sama dengan ",matrikstts[baris][y]," di titik ",'(',baris,',',y,')')
					else:
						print('Titik (',baris,',',y,') diisi dengan ', kata[huruf])
						matrikstts[baris][y] = kata[huruf]
			k += 1
		if baris == listtitikakhir[jmlkata-1][0] and y == listtitikakhir[jmlkata-1][1] : #jika pengisian sudah sampai terakhir maka pengisian tts telah berhasil
			break
		i += 1


print()
print(">>>>>>>>>>>>>>>>>>>>>>>> HASIL TTS <<<<<<<<<<<<<<<<<<<<<<<<<<")
print()
for a in range (0,nmatriks):
	for b in range (0,nmatriks):
		print(matrikstts[a][b], end=' ')
	print()

#MENGHITUNG WAKTU EKSEKUSI
end_time = time.time()
ex_time = end_time - start_time
print()
print("Executed in",ex_time,"seconds")
print()
