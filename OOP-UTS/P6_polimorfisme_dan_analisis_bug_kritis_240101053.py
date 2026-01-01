class Karyawan:
    def __init__(self, nama, gaji_pokok):
        # Menggunakan _ (protected) agar mudah diakses/dicetak di kelas anak
        self._nama = nama 
        self._gaji_pokok = gaji_pokok

    def get_gaji_pokok(self):
        # Mengembalikan nilai numerik, bukan string berformat
        return self._gaji_pokok
    
    def get_nama(self):
        return self._nama
    
    def hitung_bonus(self):
        # Metode dasar (akan ditimpa)
        return 0 # Mengembalikan 0 agar hitungan total gaji tetap berjalan
    
    def hitung_total_gaji(self):
        # Memanggil hitung_bonus()
        total_gaji = self._gaji_pokok + self.hitung_bonus()
        # Mengembalikan nilai numerik
        return total_gaji
    
# ----------------------------------------------------------------------
    
class KaryawanTetap (Karyawan):
    def __init__(self, nama, gaji_pokok, lama_kerja_tahun):
        # Panggil konstruktor induk
        super().__init__(nama, gaji_pokok)
        self._lama_kerja_tahun = lama_kerja_tahun

    def hitung_bonus(self):
        # Mengakses atribut protected induk (_gaji_pokok)
        bonus = 0.1 * self._gaji_pokok * self._lama_kerja_tahun
        return bonus

# ----------------------------------------------------------------------

class KaryawanKontrak (Karyawan):
    def __init__(self, nama, gaji_pokok, proyek_selesai):
        # Panggil konstruktor induk
        super().__init__(nama, gaji_pokok)
        self._proyek_selesai = proyek_selesai

    def hitung_bonus(self):
        # Mengakses atribut protected
        bonus = 500000 * self._proyek_selesai
        return bonus
    
# ----------------------------------------------------------------------
    
def cetak_slip_gaji(daftar_karyawan):
    """Fungsi Polimorfik untuk mencetak detail gaji."""
    for karyawan in daftar_karyawan:
        # Panggilan polimorfik hitung_bonus() dan hitung_total_gaji()
        nama = karyawan.get_nama()
        gaji_pokok = karyawan.get_gaji_pokok()
        bonus = karyawan.hitung_bonus()
        total_gaji = karyawan.hitung_total_gaji()

        print(f"Nama: {nama}")
        print(f"Gaji Pokok: Rp{gaji_pokok:,.2f}")
        print(f"Bonus: Rp{bonus:,.2f}")
        print(f"Total Gaji: Rp{total_gaji:,.2f}")
        print("-" * 30)

# --- Pengujian ---

tetap_1 = KaryawanTetap("Andi", 5000000, 5) # Bonus: 5M * 0.1 * 5 = 2.5 Juta
kontrak_1 = KaryawanKontrak("Bunga", 3000000, 4) # Bonus: 500rb * 4 = 2 Juta
tetap_2 = KaryawanTetap("Citra", 6500000, 2) # Bonus: 6.5M * 0.1 * 2 = 1.3 Juta

daftar_karyawan = [tetap_1, kontrak_1, tetap_2]

cetak_slip_gaji(daftar_karyawan)