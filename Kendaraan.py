class Kendaraan :
  def __init__(self, merek, tahun, no_polisi, jenis):
    self.merek = merek
    self.tahun = tahun
    self.no_polisi = no_polisi
    self.jenis = jenis


class Mobil(Kendaraan):
  def tampilkan_info(self):
    print(f"Merek Mobil: {self.merek}")
    print(f"Tahun: {self.tahun}")
    print(f"No Polisi: {self.no_polisi}")
    print(f"Jenis: {self.jenis}")

class motor(Kendaraan):
  def tampilkan_info(self):
    print(f"Merek Motor: {self.merek}")
    print(f"Tahun: {self.tahun}")
    print(f"No Polisi: {self.no_polisi}")
    print(f"Jenis: {self.jenis}")


my_mobil = Mobil("Toyota", 2022, "D 4567 EF", "Sedan")
print("\n--- Info Mobil ---")
my_mobil.tampilkan_info()

my_motor = motor("Yamaha", 2023, "A 9876 GHI", "Sport")
print("\n--- Info Motor ---")
my_motor.tampilkan_info()
