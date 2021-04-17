#data id dan password
IdSeptha='1302170008'
passSeptha='12345'
IdImam='1302174033'                                        
passImam='12345'
IdCici='1302173968'
passCici='12345'
IdAdmin='Danang Triantoro'
passAdmin='12345'
#login
def pilihuser():
    print("Login as : \n","1. Admin\n",'2. User') 
    login=int(input('Pilih : '))
    if login==1:
        admin()
    elif login==2:
        user()
    else:
        print('Menu Tidak Tersedia')
        pilihuser()
#bagian admin
def admin():
    username=input('Username Admin : ')
    password=input('password Admin : ')
    if username==IdAdmin and password==passAdmin:
        menuadmin()
    else:
        print('Username atau Password yang anda masukan salah')
        admin()
def menuadmin():
    print('1. Lihat KRS Final Mahasiswa\n2. Reset Matakuliah Mahasiswa\n3. Accept KRS Mahasiswa\n4. Logout')
    n=int(input('Pilih: '))
    if n==1:
        lihatkrs()
    elif n==2:
        reset()
    elif n==3:
        acckrs()
    elif n==4:
        pilihuser()
    else:
        print('Menu tidak tersedia')
        menuadmin()
def lihatkrs():
    print('1. Septha Anggara\t1302170008\n2. Imam Nurul Ihsan\t1302174033\n3. Tasyalva Aulia\t1302173968\n4. Keluar')
    import json
    n=int(input('Nama Mahasiswa Yang Dilihat: '))
    if n==1:
        y=open('Septha Anggara 1302170008.txt','r')
        x=json.load(y)
        for i in range(len(x)):
            print(i+1,'\t',x[i])
    elif n==2:
        y=open('Imam Nurul Ihsan 1302174033.txt','r')
        x=json.load(y)
        for i in range(len(x)):
            print(i+1,'\t',x[i])
    elif n==3:
        y=open('Tasyalva Aulia 1302173968.txt','r')
        x=json.load(y)
        for i in range(len(x)):
            print(i+1,'\t',x[i])
    elif n==4:
        menuadmin()
    else:
        print('No yang anda input salah')
        lihatkrs()
    lihatkrs()
def reset():
    print('1. Septha Anggara\t1302170008\n2. Imam Nurul Ihsan\t1302174033\n3. Tasyalva Aulia\t1302173968\n4. Kembali')
    import json
    n=int(input('Nomor mahasiswa yang akan di reset: '))
    if n==1:
        y=open('Septha anggara 1302170008.txt','r')
        x=json.load(y)
        for i in range(len(x)):
            print(i+1,'\t',x[i])
        def hapus():
            print('Pilihan\n1. Ya\t2. Tidak')
            z=int(input('Apakah anda yakin akan mengubah mata kuliah mahasiswa ini: '))
            if z==1:
                y=open('Septha anggara 1302170008.txt','r')
                x=json.load(y)
                z=z+4
                x.pop(z)
                w=open('Septha anggara 1302170008.txt','w')
                json.dump(x,w)
                w.close()
                y=open('Septha anggara 1302170008.txt','r')
                q=json.load(y)
                for i in range(len(q)):
                    print(i+1, '\t', q[i])
                reset()
            elif z==2:
                reset()
            else:
                print('Nomor yang anda masukan tidak ada')
                hapus()
        hapus()
    elif n==3:
        y=open('Tasyalva Aulia 1302173968.txt','r')
        x=json.load(y)
        for i in range(len(x)):
            print(i+1,'\t',x[i])
        print('\n1. ya\t2. tidak')
        def hapus():
            print('Pilihan\n1. Ya\t2. Tidak')
            z=int(input('Apakah anda yakin akan mengubah mata kuliah mahasiswa ini: '))
            if z==1:
                y=open('Tasyalva Aulia 1302173968.txt','r')
                x=json.load(y)
                z=z+4
                x.pop(z)
                w=open('Tasyalva Aulia 1302173968.txt','w')
                json.dump(x,w)
                w.close()
                y=open('Tasyalva Aulia 1302173968.txt','r')
                q=json.load(y)
                for i in range(len(q)):
                    print(i+1, '\t', q[i])
                reset()
            elif z==2:
                reset()
            else:
                print('Nomor yang anda masukan tidak ada')
                hapus()
        hapus()
    elif n==2:
        print('Mahasiswa Ini tidak mengambil mata kuliah tingkat atas')
        reset()
    elif n==4:
        menuadmin()
    else:
        print('Nomor yang anda masukan tidak tersedia')
        nomor2()
def acckrs():
    print('1. Septha Anggara\t1302170008\n2. Imam Nurul Ihsan\t1302174033\n3. Tasyalva Aulia\t1302173968\n4. Kembali')
    x=int(input('Input no. mahasiswa yang akan di accept: '))
    if x==1:
        pertama()
    elif x==2:
        kedua()
    elif x==3:
        ketiga()
    elif x==4:
        menuadmin()
    else:
        print('Nomor Mahasiswa yang anda input tidak ada di urutan')
        acckrs
    acckrs()
def pertama():
    import json
    y=open('Septha anggara 1302170008.txt','r')
    d=json.load(y)
    for i in range(len(d)):
        print(i+1,'\t',d[i])
    print('Pilihan\n1. Ya\t2. Tidak')
    r=int(input('Accept KRS ini: '))
    if r==1:
        print('KRS mahasiswa sudah di accept')
    elif r==2:
        acckrs()
def kedua():
    import json
    y=open('komputasi2.txt','r')
    d=json.load(y)
    for i in range(len(d)):
        print(i+1,'\t',d[i])
    print('Pilihan\n1. Ya\t2. Tidak')
    r=int(input('Accept KRS ini: '))
    if r==1:
        print('KRS mahasiswa sudah di accept')
    elif r==2:
        acckrs()
def ketiga():
    import json
    y=open('Tasyalva Aulia 1302173968.txt','r')
    d=json.load(y)
    for i in range(len(d)):
        print(i+1,'\t',d[i])
    print('Pilihan\n1. Ya\t2. Tidak')
    r=int(input('Accept KRS ini: '))
    if r==1:
        print('KRS mahasiswa sudah di accept')
    elif r==2:
        acckrs()
#user
def user():
    username=input('Username User: ')
    password=input('password User: ')
    if username==IdSeptha and password==passSeptha:
        semesterseptha()
    elif username==IdImam and password==passImam:
        semesterimam()
    elif username==IdCici and password==passCici:
        semestercici()
    else:
        print('User name atau password salah')
        user()
def semesterseptha():
    L=[3.76,2.77,3.21]
    print('\t\t\tMenu Utama\nNama: Septha Anggara\tFakultas: Informatika\tIPK:3.76\nJurusan:Ilmu Komputasi\tKelas CS-41-04')
    print('1. Ajukan KRS\t2. Lihat KRS\n3. Logout')
    import json
    x=int(input('pilih menu: '))
    if x==1:                                        
        if L[0]>3.00:
            y=open('komputasi2.txt','r')
            x=json.load(y)
            for i in range(len(x)):
                print(i+1,'\t',x[i])
            print('Karena ipk anda diatas 3.00 maka anda wajib mengambil mata kuliah tambahan\n1. WGTIK\t2. Sistem Operasi')
            z=int(input('Matkul Yang ingin ditambahkan: '))
            if z==1:
                y=open('komputasi2.txt','r')
                x=json.load(y)
                L=['WGTIK','Sistem Operasi']
                x.append(L[0])
                w=open('Septha anggara 1302170008.txt','w')
                json.dump(x,w)
                w.close()
                for i in range(len(x)):
                    print(i+1, '\t', x[i])
                print('Pilihan\n1. Ya\t2. Tidak')
                e=int(input('Apakah anda yakin akan mengajukan KRS ini: '))
                if e==1:
                    print('Silahkan hubungin dosen wali anda untuk menyetujui KRS ini')
                elif e==2:
                    semesterseptha()
                print('Ketik "ya" untuk kembali ke menu')
                def salah():
                    q=str(input('Kembali ke menu: '))
                    if q=='ya':
                        semesterseptha()
                    else:
                        print('perintah yang anda masukan salah')
                        salah()
                salah()
            elif z==2:
                y=open('komputasi2.txt','r')
                x=json.load(y)
                L=['WGTIK','Sistem Operasi']
                x.append(L[1])
                w=open('Septha anggara 1302170008.txt','w')
                json.dump(x,w)
                w.close()
                for i in range(len(x)):
                    print(i+1, '\t', x[i])
                print('Pilihan\n1. Ya\t2. Tidak')
                e=int(input('Apakah anda yakin akan mengajukan KRS ini: '))
                if e==1:
                    print('Silahkan hubungin dosen wali anda untuk menyetujui KRS ini')
                elif e==2:
                    semesterseptha()
                print('Ketik "ya" untuk kembali ke menu')
                def salah():
                    q=str(input('Kembali ke menu: '))
                    if q=='ya':
                        semesterseptha()
                    else:
                        print('perintah yang anda masukan salah')
                        salah()
                salah()
        elif L[0]<=3.00:
            print('Mohon maaf IPK anda tidak memenuhi syarat')
    elif x==2:
        def akhir():
            print('1.Semester 1\n2.Semester 2')
            w=int(input('Melihat KRS pada semester: '))
            if w==1:
                y=open('komputasi1.txt','r')
                x=json.load(y)
                for i in range(len(x)):
                  print(i+1,'\t',x[i])
                def perintahakhir():
                    print('Pilihan\n1. Kembali ke menu utama\t2. Kembali ke pemilihan semester')
                    e=int(input('Pilihan: '))
                    if e==1:
                        semesterseptha()
                    elif e==2:
                        akhir()
                    else:
                        print('Pilihan yang anda input tidak tersedia')
                        perintahakhir()
                perintahakhir()
            elif w==2:
                y=open('Septha anggara 1302170008.txt','r')
                x=json.load(y)
                for i in range(len(x)):
                    print(i+1, '\t', x[i])
                def perintahakhir():
                    print('Pilihan\n1. Kembali ke menu utama\t2. Kembali ke pemilihan semester')
                    e=int(input('Pilihan: '))
                    if e==1:
                        semesterseptha()
                    elif e==2:
                        akhir()
                    else:
                        print('Pilihan yang anda input tidak tersedia')
                        perintahakhir()
                perintahakhir()
        akhir()
    elif x==3:
        pilihuser()
    else:
        print('Nomor menu yang anda input tidak tersedia')
        semesterseptha()
def semesterimam():
    L=[3.76,2.77,3.21]
    print('\t\t\tMenu Utama\nNama: Imam Nurul Ihsan\tFakultas: Informatika\tIPK:2.77\nJurusan:Ilmu Komputasi\tKelas CS-41-04')
    print('1. Ajukan KRS\t2. Lihat KRS\n3. Logout')
    import json
    x=int(input('pilih menu: '))
    if x==1:
        if L[1]<=3.00:
            y=open('komputasi2.txt','r')
            x=json.load(y)
            w=open('Imam Nurul Ihsan 1302174033.txt','w')
            json.dump(x,w)
            w.close()
            for i in range(len(x)):
                print(i+1, '\t', x[i])
            print('Mohon maaf karena IPK anda tidak memenuhi syarat maka tidak dapat mengambil mata kuliah tambahan')
            print('Ketik "ya" untuk kembali ke menu')
            def salah():
                q=str(input('Kembali ke menu: '))
                if q=='ya':
                    semesterimam()
                else:
                    print('perintah yang anda masukan salah')
                    salah()
            salah()
        elif L[1]>3.00:
            print('Karena ipk anda diatas 3.00 maka anda wajib mengambil mata kuliah tambahan\n1. WGTIK\t2. Sistem Operasi')
            z=int(input('Matkul Yang ingin ditambahkan: '))
            if z==1:
                y=open('komputasi2.txt','r')
                x=json.load(y)
                L=['WGTIK','Sistem Operasi']
                x.append(L[0])
                w=open('Imam Nurul Ihsan 1302170008.txt','w')
                json.dump(x,w)
                w.close()
                for i in range(len(x)):
                    print(i+1, '\t', x[i])
                print('Ketik "ya" untuk kembali ke menu')
                def salah():
                    q=str(input('Kembali ke menu: '))
                    if q=='ya':
                        semesterimam()
                    else:
                        print('perintah yang anda masukan salah')
                        salah()
                salah()
            elif z==2:
                y=open('komputasi2.txt','r')
                x=json.load(y)
                L=['WGTIK','Sistem Operasi']
                x.append(L[1])
                w=open('Imam Nurul Ihsan 1302170008.txt','w')
                json.dump(x,w)
                w.close()
                y=open('Imam Nurul Ihsan 1302170008.txt','r')
                x=json.load(y)
                for i in range(len(x)):
                    print(i+1, '\t', x[i])
                print('Ketik "ya" untuk kembali ke menu')
                def salah():
                    q=str(input('Kembali ke menu: '))
                    if q=='ya':
                        semesterimam()
                    else:
                        print('perintah yang anda masukan salah')
                        salah()
                salah()
    elif x==2:
        def akhir():
            print('1.Semester 1\n2.Semester 2')
            w=int(input('Melihat KRS pada semester: '))
            if w==1:
                y=open('komputasi1.txt','r')
                x=json.load(y)
                for i in range(len(x)):
                  print(i+1,'\t',x[i])
                def perintahakhir():
                    print('Pilihan\n1. Kembali ke menu utama\t2. Kembali ke pemilihan semester')
                    e=int(input('Pilihan: '))
                    if e==1:
                        semesterimam()
                    elif e==2:
                        akhir()
                    else:
                        print('Pilihan yang anda input tidak tersedia')
                        perintahakhir()
                perintahakhir()
            elif w==2:
                y=open('Imam Nurul Ihsan 1302174033.txt','r')
                x=json.load(y)
                for i in range(len(x)):
                    print(i+1, '\t', x[i])
                def perintahakhir():
                    print('Pilihan\n1. Kembali ke menu utama\t2. Kembali ke pemilihan semester')
                    e=int(input('Pilihan: '))
                    if e==1:
                        semesterimam()
                    elif e==2:
                        akhir()
                    else:
                        print('Pilihan yang anda input tidak tersedia')
                        perintahakhir()
                perintahakhir()
        akhir()
    elif x==3:
        pilihuser()
    else:
        print('Nomor menu yang anda input tidak ada')
        semesterimam()
def semestercici():
    L=[3.76,2.77,3.21]
    print('\t\t\tMenu Utama\nNama: Tasyalva Aulia\tFakultas: Informatika\tIPK:3.21\nJurusan:Ilmu Komputasi\tKelas CS-41-04')
    print('1. Ajukan KRS\t2. Lihat KRS\n3. Logout')
    import json
    x=int(input('pilih menu: '))
    if x==1:                                        
        if L[2]>3.00:
            y=open('komputasi2.txt','r')
            x=json.load(y)
            for i in range(len(x)):
                print(i+1,'\t',x[i])
            print('Karena ipk anda diatas 3.00 maka anda wajib mengambil mata kuliah tambahan\n1. WGTIK\t2. Sistem Operasi')
            z=int(input('Matkul Yang ingin ditambahkan: '))
            if z==1:
                y=open('komputasi2.txt','r')
                x=json.load(y)
                L=['WGTIK','Sistem Operasi']
                x.append(L[0])
                w=open('Tasyalva Aulia 1302173968.txt','w')
                json.dump(x,w)
                w.close()
                w=open('Tasyalva Aulia 1302173968.txt','r')
                x=json.load(w)
                for i in range(len(x)):
                    print(i+1, '\t', x[i])
                print('Pilihan\n1. Ya\t2. Tidak')
                e=int(input('Apakah anda yakin akan mengajukan KRS ini: '))
                if e==1:
                    print('Silahkan hubungin dosen wali anda untuk menyetujui KRS ini')
                elif e==2:
                    semestercici()
                print('Ketik "ya" untuk kembali ke menu')
                def salah():
                    q=str(input('Kembali ke menu: '))
                    if q=='ya':
                        semestercici()
                    else:
                        print('perintah yang anda masukan salah')
                        salah()
                salah()
            elif z==2:
                y=open('komputasi2.txt','r')
                x=json.load(y)
                L=['WGTIK','Sistem Operasi']
                x.append(L[1])
                w=open('Tasyalva Aulia 1302173968.txt','w')
                json.dump(x,w)
                w.close()
                for i in range(len(x)):
                    print(i+1, '\t', x[i])
                print('Pilihan\n1. Ya\t2. Tidak')
                e=int(input('Apakah anda yakin akan mengajukan KRS ini: '))
                if e==1:
                    print('Silahkan hubungin dosen wali anda untuk menyetujui KRS ini')
                elif e==2:
                    semesterseptha()
                print('Ketik "ya" untuk kembali ke menu')
                def salah():
                    q=str(input('Kembali ke menu: '))
                    if q=='ya':
                        semesterseptha()
                    else:
                        print('perintah yang anda masukan salah')
                        salah()
                salah()
        elif L[2]<=3.00:
            print('Mohon maaf IPK anda tidak memenuhi syarat')
    elif x==2:
        def akhir():
            print('1.Semester 1\n2.Semester 2')
            w=int(input('Melihat KRS pada semester: '))
            if w==1:
                y=open('komputasi1.txt','r')
                x=json.load(y)
                for i in range(len(x)):
                  print(i+1,'\t',x[i])
                def perintahakhir():
                    print('Pilihan\n1. Kembali ke menu utama\t2. Kembali ke pemilihan semester')
                    e=int(input('Pilihan: '))
                    if e==1:
                        semestercici()
                    elif e==2:
                        akhir()
                    else:
                        print('Pilihan yang anda input tidak tersedia')
                        perintahakhir()
                perintahakhir()
            elif w==2:
                y=open('Tasyalva Aulia 1302173968.txt','r')
                x=json.load(y)
                for i in range(len(x)):
                    print(i+1, '\t', x[i])
                def perintahakhir():
                    print('Pilihan\n1. Kembali ke menu utama\t2. Kembali ke pemilihan semester')
                    e=int(input('Pilihan: '))
                    if e==1:
                        semestercici()
                    elif e==2:
                        akhir()
                    else:
                        print('Pilihan yang anda input tidak tersedia')
                        perintahakhir()
                perintahakhir()
        akhir()
    elif x==3:
        pilihuser()
    else:
        print('Nomor menu yang anda input tidak tersedia')
        semestercici()
pilihuser()
