import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)
    
cursor = connection.cursor()

try:
    # Buat database jika belum ada
    cursor.execute('CREATE DATABASE IF NOT EXISTS cloud_bread')
    print("Database Berhasil Dibuat atau Sudah Ada")

    # Pilih database
    cursor.execute("USE cloud_bread")

    # Buat tabel pelanggan jika belum ada
    cursor.execute("""
    CREATE TABLE pelanggan (
        id_pelanggan INT AUTO_INCREMENT PRIMARY KEY,
        nama VARCHAR(100) NOT NULL,
        alamat VARCHAR(255),
        no_telepon VARCHAR(15),
        tanggal_bergabung DATE DEFAULT CURRENT_DATE
    );
    """)
    print("Tabel pelanggan Berhasil Dibuat!!")

    # Buat tabel jenis_pelanggan jika belum ada
    cursor.execute("""
    CREATE TABLE jenis_roti (
        id_jenis INT AUTO_INCREMENT PRIMARY KEY,
        jenis_roti VARCHAR(50) NOT NULL,
        harga INT NOT NULL
    );
    """)
    print("Tabel jenis_pelanggan Berhasil Dibuat!!")

    # Buat tabel pesanan jika belum ada
    cursor.execute("""
    CREATE TABLE pesanan (
        id_pesanan INT AUTO_INCREMENT PRIMARY KEY,
        id_pelanggan INT NOT NULL,
        tanggal_pesanan DATE DEFAULT CURRENT_DATE,
        total_harga INT NOT NULL,
        status ENUM('Diproses', 'Selesai', 'Diambil') DEFAULT 'Diproses',
        FOREIGN KEY (id_pelanggan) REFERENCES pelanggan (id_pelanggan) ON UPDATE CASCADE
    );
    """)
    print("Tabel pesanan Berhasil Dibuat!!")

    # Buat tabel detail_pesanan jika belum ada
    cursor.execute("""
    CREATE TABLE detail_pesanan (
        id_detail INT AUTO_INCREMENT PRIMARY KEY,
        id_pesanan INT NOT NULL,
        id_jenis INT NOT NULL,
        jumlah INT NOT NULL,
        sub_total INT NOT NULL,
        FOREIGN KEY (id_pesanan) REFERENCES pesanan (id_pesanan) ON UPDATE CASCADE,
        FOREIGN KEY (id_jenis) REFERENCES jenis_roti (id_jenis) ON UPDATE CASCADE
    );
    """)
    print("Tabel detail_pesanan Berhasil Dibuat!!")

    # manambahkan data kedalam tabel jenis roti
    cursor.execute("""
    INSERT INTO jenis_roti (jenis_roti, harga) VALUES
    ('roti coklat', 10000),
    ('roti matcha', 12000),
    ('cromboloni', 8000),
    ('croisant', 7000),
    ('pancake durian', 15000),
    ('mochi', 14000),
    ('sandwich', 25000),
    ('roti srikaya', 15000),
    ('roti keju', 8000);
    """)
    print("Data berhasil dimasukkan ke tabel jenis_roti!!")
    
    connection.commit()
except Error as err:
    print("Error:", err)

finally:
    cursor.close()
    connection.close()
    print("Koneksi ditutup")
