#deskripsi
#spesifikasi: program untuk presensi

#kamus
#matriksSudahAbsen adalah matriks yang berisi data yang memiliki kapasitas 200 mahasiswa untuk absensi selama 1 bulan(November)
#matriksJadwal adalah matriks yang berisi jadwal sesuai jadwal mata kuliah TPB STEI
#indeksTandaiHadir adalah fungsi yang berguna untuk mencari sekarang adalah absen keberapa
#presentaseKehadiran adalah fungsi untuk mencari presentase kehadiran pada matkul yang diinginkan
#mengambilData adalah prosedur untuk mengambil data dari file data.txt dan memasukkannya ke dalam matriksSudahAbsen
#menyimpanData adalah prosedur untuk menyimpan data dari matriksSudahAbsen ke dalam file data.txt
#maiMenu adalah prosedur untuk menampilkan main menu

#fitur
#presensi sesuai tanggal dan jam saat ini
#presentase kehadiran seperti SIX
#data presensi tidak akan hilang setelah program ditutup


from datetime import datetime                  #import library terkait tanggal
import os                                      #inport library untuk command prompt                                                       

#fungsi untuk mendapat indeks absen saat ini, fungsi ini akan mencari dari tanggal 1 sampai saat ini dan memberi nomor untuk setiap mata kuliah yang ditemui    
def indeksTandaiHadir():                                                                        
    absenKe = 0                                                     #absenKe adalah variabel untuk mencari urutan absen ke berapa untuk tanggal dan waktu saat ini
    for i in range(tanggal):                                        #i adalah variabel perulangan tanggal dari awal bulan sampai sekarang

        if(i==(tanggal-1)):                                                                     #i=tanggal-1 adalah tanggal saat ini (ini karena pada matriks jadwal yang kami buat tanggal 1 adalah indeks 0)                                                           
            j=0                                                     #j adalah variabel perulangan jam dari pagi hingga jam saat ini 
            jamDicari = jam-7                                                                   #pada matriks jam 0 adalah jam 7 sehingga jam saat ini harus dikurangi 7 sehingga sesuai dengan matriks 
            if(matriksJadwal[i%7][jamDicari]!="" and jamDicari!=0):                               #ketika jam saat ini terdapat mata kuliah, perlu dikurangi 1 supaya mata kuliah tersebut tidak ikut terhitung karena user akan menandai hadir pada jam saat ini 
                    jamDicari -= 1
            while(j<jamDicari):                                     #perulangan dari pagi hingga jam saat ini
                if(matriksJadwal[i%7][j]!=""):                                                  #ketika menemukan mata kuliah, tambahkan absenKe dengan 1
                    absenKe += 1
                    j += 1                                                                      #j+1 ketika menemukan mata kuliah untuk menghindari suatu mata kuliah dihitung 2 kali, (misal fisdas ada pada jam 7 dan 8, saat kita menemukan fisdas di jam 7, maka jam langsung ditambah 1 menjadi 8 dan ditambah 1 lagi ketika keluar if menjadi jam 9)
                j += 1
        else:                                                                                   #ketika i<tanggal saat ini
            j=0 
            while(j<11):                                           #perulangan dari pagi hingga sore, kita memiliki waktu kuliah dari pukul 7-18 wib dimana itu adalah 11 jam                                                
                if(matriksJadwal[i%7][j]!=""):
                    absenKe += 1
                    j += 1
                j += 1
    return absenKe                                                 #kembalikan nilai berupa saat ini user harus tandai hadir pada urutan ke berapa

#fungsi presentase kehadiran suatu matkul, hampir sama dengan fungsi di atas, hanya ditambahi 2 variabel lain
def presentaseKehadiran(matkul):                                   #terdapat parameter matkul(mata kuliah yang dicari) berupa string
    absenKe = 0                                                    #absenKe berfungsi sama seperti di atas 
    indeksTotal = 0                                                #indeksTotal adalah banyaknya presensi dari tanggal 1 sampai tanggal ini dari matkul yang dicari
    yangHadir = 0                                                  #yangHadir adalah banyaknya keempatan presensi yang ditandai hadir oleh user
    
    for i in range(tanggal):                                                                            
        if(i==(tanggal-1)):                                                                        #ketika tanggal saat ini                                                           
            if(jam>=7 and jam<=18):
                j=0
                jamDicari = jam-7
                if(matriksJadwal[i%7][jamDicari]!="" and jamDicari!= 17):
                        jamDicari += 1
                while(j<jamDicari):
                    if(matriksJadwal[i%7][j]!=""):                                                     #ketemu suatu mata kuliah(bisa saja bukan yang dicari)
                        if(matriksJadwal[i%7][j]==matkul):                                             #jika mata kuliah sama dengan yang dicari, indeksTotal ditambah 1 
                            indeksTotal += 1
                            if(matriksSudahAbsen[nim-1][absenKe]):                                     #cek apakah sudah ditandai hadir? jika sudah, yangHadir ditambah 1
                                yangHadir += 1 
                        absenKe += 1                                                                   #absenKe ditambah terus ketika menemui mata kuliah baik yang dicari maupun yang bukan dicari
                        j += 1
                    j += 1
            if(jam>=18):
                j=0
                while(j<10):                                                
                    if(matriksJadwal[i%7][j]!=""):
                        if(matriksJadwal[i%7][j]==matkul):                                             #mata kuliah yang sama dengan yang dicari
                            indeksTotal += 1
                            if(matriksSudahAbsen[nim-1][absenKe]):                                     #cek apakah sudah ditandai hadir?
                                yangHadir += 1
                        absenKe += 1
                        j += 1    
                    j += 1
        else:                                                                                      #ketika tanggal bukan saat ini
            j=0
            while(j<10):                                                
                if(matriksJadwal[i%7][j]!=""):
                    if(matriksJadwal[i%7][j]==matkul):                                             #mata kuliah yang sama dengan yang dicari
                        indeksTotal += 1
                        if(matriksSudahAbsen[nim-1][absenKe]):                                     #cek apakah sudah ditandai hadir?
                            yangHadir += 1
                    absenKe += 1
                    j += 1    
                j += 1
    presentase = 0.0                                                                               
    if(yangHadir!=0):                                                                              #ketika yangHadir tidak sama dengan 0, maka presentasenya pasti lebih dari 0 dan didapat dengan rumus tersebut 
        presentase = yangHadir/indeksTotal*100
    return presentase

#prosedur untuk mengambil data dari file data.txt dan memasukkannya ke dalam matriks sudahAbsen
def mengambilData():
    file = open("data.txt",'r')                                                                 
    for i in range(200):
        file.seek(i*102)
        tmp = file.readline()
        for j in range(100):
            matriksSudahAbsen[i][j]=bool(int(tmp[j]))
    file.close()

#prosedur untuk menyimpan matriksSudahAbsen ke dalam file data.txt
def menyimpanData():
    file = open("data.txt",'w')
    for i in range(200):
        for j in range(100):
            tmp = int(matriksSudahAbsen[i][j])
            file.write(str(tmp))
        if(i!=199):
            file.write("\n")
    file.close() 

#fungsi menghasilkan nim
def generateNim():
    if(nim/10<1):
        return "1652100"+str(nim)
    elif(nim/10<10):
        return "165210"+str(nim)
    else:
        return "16521"+str(nim)

#prosedur untuk menampilkan main menu
def mainMenu():
    os.system("cls")
    print("**************************************")
    print("*                                    *")
    print("*  Selamat datang NIM "+generateNim()+"       *")
    print("* ",tanggal,"November pukul",str(date[11:16]),"           *")   
    print("*  1. Presensi                       *")
    print("*  2. Presentase kehadiran           *")
    print("*  3. Keluar                         *")
    print("*                                    *")
    print("**************************************")
    pilihan = int(input("Masukkan pilihanmu "))
    return pilihan

#prosedur untuk kembali ke main menu
def kembali():
    pilih = str(input("Ketik apapun untuk kembali"))
    return pilih

#prosedur tampilan awal saat input nim
def login():
    print("**************************************")
    print("*      ssss     iii  xxx     xxx     *")
    print("*    sss  sss   iii   xxx   xxx      *")
    print("*     sss       iii    xxx xxx       *")   
    print("*      sss      iii      xxx         *")
    print("*        sss    iii    xxx xxx       *")
    print("*    sss  sss   iii   xxx   xxx      *")
    print("*      ssss     iii  xxx     xxx     *")
    print("**************************************")


#Mulai baris ini adalah program utama

#matriks yang berisi jadwal mata kuliah TPB ITB
matriksJadwal = [["Fisika Dasar","Fisika Dasar","","","Matematika","Matematika","","Pengkom","Pengkom","",""],
                ["","Pengkom","","Matematika","Matematika","","","Fisika Dasar","Fisika Dasar","Olahraga","Olahraga"],
                ["","","","","","","","","","",""],
                ["Fisika Dasar","Fisika Dasar","","","Matematika","Matematika","","Bahasa Inggris","Bahasa Inggris","",""],
                ["TTKI","TTKI","","","","","","","","",""],
                ["","","","","","","","","","",""],
                ["","","","","","","","","","",""]]

#matriks yang berisi data dari 200 mahasiswa selama bulan November
matriksSudahAbsen = [[False for i in range(100)] for j in range(200)]   

#copy paste disini

login()                                                                           #menampilkan halaman pertama yang ada tulisan SIX
nim = int(input("Masukkan NIM akhir: "))                                          #input nim mahasiswa
ulang = True
while(ulang):                                                                     #perulangan yang akan berulang terus sampai user ingin keluar dengan mengetik angka 3
    mengambilData()                                                               #pengambilan data dari data.txt   
    date = str(datetime.now())                                                    #mengambil waktu saat ini berupa string
    jam = int(date[11:13])                                                        #mengambil informasi jam dari variabel date
    tanggal = int(date[8:10])                                                     #mengambil informasi tanggal dari variabel date
    pilihan = mainMenu()                                                          #menmapilkan main menu
    # 1. Absen sesuai waktu sekarang
    if(pilihan==1):                                                                                                                   #menampilkan pilihan pertama yaitu presensi
        if(jam<18 and jam>=7 and matriksJadwal[(tanggal-1)%7][jam-7]!=""):                                                                   #mengecek jika saat ini terdapat jam matkul, maka harus presensi
            print("Sekarang waktunya presensi mata kuliah",matriksJadwal[(tanggal-1)%7][jam-7])
            tandai = str(input("ketik Y untuk tandai hadir "))
            if(tandai=='Y'):                                                                                                                  #menandai hadir dengan mengetik Y
                urutanAbsen = indeksTandaiHadir()                                                                                             #mencari indeks yang harus ditandai hadir
                matriksSudahAbsen[nim-1][urutanAbsen] = True                                                                                  #menandai hadir pada matriksSudahAbsen dengan mengisi true
                menyimpanData()                                                                                                               #menyimpan hasil perubahan matriksSudahAbsen
        else:
            print("Sekarang belum waktunya presensi")
        ulang = bool(input("Ketik apapun untuk kembali "))
    #2. Cek Presentase kehadiran
    elif(pilihan==2):                                                                                                                 #menampilakan pilihan kedua yaitu presentase kehadiran
        print("Presentase kehadiran anda dalam mata kuliah Fisika Dasar adalah",presentaseKehadiran("Fisika Dasar"),"%")              #menampilkan setiap presentase kehadiran 
        print("Presentase kehadiran anda dalam mata kuliah Matematika adalah",presentaseKehadiran("Matematika"),"%")
        print("Presentase kehadiran anda dalam mata kuliah Pengkom adalah",presentaseKehadiran("Pengkom"),"%")
        print("Presentase kehadiran anda dalam mata kuliah Olahraga adalah",presentaseKehadiran("Olahraga"),"%")
        print("Presentase kehadiran anda dalam mata kuliah Bahasa Inggris adalah",presentaseKehadiran("Bahasa Inggris"),"%")
        print("Presentase kehadiran anda dalam mata kuliah TTKI adalah",presentaseKehadiran("TTKI"),"%")
        ulang = bool(input("Ketik apapun untuk kembali "))
    elif(pilihan==3):
        ulang = False                                                                                                                 #ketika user memilih 3 maka akan keluar dari perulangan dan program selesai
                                                                                     
                                            
