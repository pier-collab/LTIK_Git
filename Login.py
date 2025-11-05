print("Hello, welcome to the login module!")

def proseslog():
    pwbenar = "Latihan"
    maksimalcoba = 3

    for percobaan in range(1, maksimalcoba + 1):
        password = input("Masukkan Password: ")

        if password == pwbenar:
            print("Login berhasil! Selamat datang di sistem RPL UPI Cibiru.")
            return True
        else:
            if percobaan < maksimalcoba:
                print(f"Password salah. Percobaan ke-{percobaan} dari {maksimalcoba}. Silakan coba lagi.\n")
            else:
                print("Akses ditolak. Hubungi administrator.")
                return False

proseslog()
