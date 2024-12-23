import mysql.connector
from mysql.connector import Error
from rich.console import Console
from rich.panel import Panel
import database.pelanggan as pell
import database.jenis_roti as rott
import database.pesanan as pess

def start_menu(): 
    try:
        # Buat koneksi
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="",  
            database="cloud_bread" 
        )

        curr = connection.cursor()
        console = Console()

        text = """\n\n[#ffa45e]====== SELAMAT DATANG DI TOKO ROTI ======[/#ffa45e]\n\n"""
        menu = generate_menu(["Data Pelanggan", "Data Roti",
                     "Pesanan Roti", "Riwayat Transaksi", "Keluar"])

        console.print(text)
        while True:
            console.print(Panel.fit(menu,
                                title="Menu Utama", title_align="left", border_style="bright_blue", padding=(1, 4, 0, 4)))
            user_input = int(input("> masukkan pilihan : "))
            print("")

            match user_input:
                case 1:
                    data_pelanggan(connection, curr, console)
                case 2:
                    data_roti(connection, curr, console)
                case 3:
                    pesanan_roti(connection, curr, console)
                case 4:
                    riwayat_transaksi(connection, curr, console)
                case 5:
                    exit()
                case _:
                    print("pilihan yang anda masukkan salah")

    except Error as err:
        print("Error : ", err)

def generate_menu(menu_list):
    menu = ""
    for index, item in enumerate(menu_list, start=1):
        menu += f"[[bold cyan]{index}[/bold cyan]] [green]{item}[/green]\n"
    return menu    

def data_pelanggan(conn, curr, console):
    menu = generate_menu(["Tambah Pelanggan", "Lihat Daftar Pelanggan", "Ubah Data Pelanggan", "Hapus Data Pelanggan", "Kembali", "Keluar"])
    ulang = True
    while ulang:
        console.print(Panel.fit(menu,
                                title="Data Pelanggan", title_align="left", border_style="bright_blue", padding=(1, 4, 0, 4)))
        user_input = int(input("> masukkan pilihan : "))
        print("")

        match user_input:
            case 1:
                pell.tambah_pelanggan(conn, curr)
            case 2:
                pell.lihat_daftar_pelanggan(curr)
            case 3:
                pell.ubah_data_pelanggan(conn,curr)
            case 4:
                pell.hapus_pelanggan(conn,curr)
            case 5:
                ulang = False
            case 6:
                exit()
            case _:
                print("pilihan yang anda masukkan salah")

def data_roti(conn, curr, console):
    menu = generate_menu(["Tambah Jenis Roti", "Lihat Daftar Roti", "Ubah Data Jenis Roti", "Hapus Jenis Roti", "Kembali", "Keluar"])
    ulang = True
    while ulang:
        console.print(Panel.fit(menu,
                                title="Data Roti", title_align="left", border_style="bright_blue", padding=(1, 4, 0, 4)))
        user_input = int(input("> masukkan pilihan : "))
        print("")

        match user_input:
            case 1:
                rott.tambah_jenis_roti(conn, curr)
            case 2:
                rott.lihat_daftar_jenis_roti(curr)
            case 3:
                rott.ubah_data_jenis_roti(conn,curr)
            case 4:
                rott.hapus_jenis_roti(conn,curr)
            case 5:
                ulang = False
            case 6:
                exit()
            case _:
                print("pilihan yang anda masukkan salah")

def pesanan_roti(conn, curr, console):
    menu = generate_menu(["Buat Pesanan Baru", "Lihat Daftar Pesanan", "Ubah Status Pesanan", "Hapus Pesanan", "Kembali", "Keluar"])
    ulang = True
    while ulang:
        console.print(Panel.fit(menu,
                                title="Pesanan Roti", title_align="left", border_style="bright_blue", padding=(1, 4, 0, 4)))
        user_input = int(input("> masukkan pilihan : "))
        print("")

        match user_input:
            case 1:
                pess.tambah_jenis_roti(conn, curr)
            case 2:
                pess.lihat_daftar_jenis_roti(curr)
            case 3:
                pess.ubah_data_jenis_roti(conn, curr)
            case 4:
                pess.hapus_jenis_roti(conn, curr)
            case 5:
                ulang = False
            case 6:
                exit()
            case _:
                print("pilihan yang anda masukkan salah")

def riwayat_transaksi(conn, curr, console):
    menu = generate_menu(["Lihat Riwayat Transaksi", "Cari Transaksi Berdasarkan ID/ Nama Pelanggan", "Cetak Struk Transaksi", "Kembali", "Keluar"])
    ulang = True
    while ulang:
        console.print(Panel.fit(menu,
                                title="Riwayat Transaksi", title_align="left", border_style="bright_blue", padding=(1, 4, 0, 4)))
        user_input = int(input("> masukkan pilihan : "))
        print("")

        match user_input:
            case 1:
                pess.lihat_riwayat_transaksi(curr)
            case 2:
                pess.cari_riwayat_berdasarkan_nama_dan_id(curr)
            case 3:
                pess.cetak_struk_transaksi(curr)
            case 4:
                ulang = False
            case 5:
                exit()
            case _:
                print("pilihan yang anda masukkan salah")

if __name__ == "__main__":
    start_menu()