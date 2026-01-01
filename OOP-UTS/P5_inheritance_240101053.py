class Akun:
    def __init__(self, pemilik, saldo=0):
        self._pemilik = pemilik
        self._saldo = saldo
        self._biaya_bulanan = 5000

    def get_saldo(self):
        return f"Saldo saat ini untuk {self._pemilik}: Rp{self._saldo:,.2f}"

    def tarik_biaya_bulanan(self):
        if self._saldo >= self._biaya_bulanan:
            self._saldo -= self._biaya_bulanan
            print(f"(-) Biaya Bulanan Dasar Rp{self._biaya_bulanan:,.2f} ditarik.")
        else:
            print("Gagal menarik biaya bulanan: Saldo tidak cukup.")
            
class AkunPelajar(Akun):
    def __init__(self, pemilik, saldo=0, sekolah="Tidak Disebutkan"):
        super().__init__(pemilik, saldo) 
        
        self._sekolah = sekolah 
        
        self._biaya_bulanan = 1000

    def get_info_pelajar(self):
        return f"Pemilik: {self._pemilik}, Sekolah: {self._sekolah}, Saldo: Rp{self._saldo:,.2f}"

class AkunPremium(Akun):
    def __init__(self, pemilik, saldo=0, limit_overdraft=1000000):
        super().__init__(pemilik, saldo)
        
        self._limit_overdraft = limit_overdraft
        self._biaya_bulanan = 25000

    def tarik_biaya_bulanan(self):
        biaya = self._biaya_bulanan
        self._saldo -= biaya
        print(f"(-) Biaya Bulanan Premium Rp{biaya:,.2f} ditarik. Saldo baru: Rp{self._saldo:,.2f}")

    def tarik_dana(self, jumlah):
        if self._saldo + self._limit_overdraft >= jumlah:
            self._saldo -= jumlah
            print(f"Berhasil tarik Rp{jumlah:,.2f}. Saldo baru: Rp{self._saldo:,.2f}")
        else:
            print("Gagal tarik dana: Saldo + Overdraft Limit tidak cukup.")

print("## Akun Dasar ##")
akun_dasar = Akun("Budi", 50000)
print(akun_dasar.get_saldo())
akun_dasar.tarik_biaya_bulanan()
print(akun_dasar.get_saldo())

print("\n## Akun Pelajar ##")
akun_pelajar = AkunPelajar("Rina", 20000, "SMAN 1 Jakarta")
print(akun_pelajar.get_info_pelajar())
akun_pelajar.tarik_biaya_bulanan()
print(akun_pelajar.get_saldo())

print("\n## Akun Premium ##")
akun_premium = AkunPremium("Dewi", 500000)
print(akun_premium.get_saldo())
akun_premium.tarik_biaya_bulanan()
akun_premium.tarik_dana(600000)
print(akun_premium.get_saldo())