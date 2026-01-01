class Produk:
    def __init__(self, nama, harga, stok):

        self.nama = nama
        self.harga = harga
        self.stok = stok

    def info(self):
        print("--- Detail Produk ---")
        print(f"Nama: {self.nama}")
        print(f"Harga: Rp{self.harga:,.2f}")
        print(f"Stok Tersedia: {self.stok}")
        print("---------------------")

    def jual(self, jumlah: int):
        if jumlah <= 0:
            print("❌ Jumlah penjualan harus lebih dari nol.")
            return

        if self.stok >= jumlah:
            self.stok -= jumlah
            print(f"✅ Penjualan {jumlah} unit {self.nama} berhasil.")
            print(f"   Sisa stok: {self.stok}")
        else:
            print(f"⚠️ Gagal menjual {jumlah} unit {self.nama}.")
            print(f"   Stok tidak mencukupi. Stok saat ini: {self.stok}")

    def restok(self, jumlah: int):
        if jumlah <= 0:
            print("❌ Jumlah restok harus lebih dari nol.")
            return

        self.stok += jumlah
        print(f"✅ Restok {jumlah} unit {self.nama} berhasil.")
        print(f"   Stok saat ini: {self.stok}")


print("## Membuat Produk ##")
buku_tulis = Produk("Buku Tulis Sinar Dunia", 5500.00, 100)
laptop_lenovo = Produk("Laptop Lenovo Ideapad", 7999000.00, 15)

buku_tulis.info()
laptop_lenovo.info()

print("\n## Melakukan Penjualan (Jual) ##")
buku_tulis.jual(20) 
laptop_lenovo.jual(5) 
laptop_lenovo.jual(20) 

print("\n## Melakukan Restok ##")
buku_tulis.restok(50)
laptop_lenovo.restok(10)

print("\n## Informasi Terbaru ##")
buku_tulis.info()
laptop_lenovo.info()