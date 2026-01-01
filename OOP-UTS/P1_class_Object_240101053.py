class Mobil:
  def __init__(self, merk, tahun, warna, start_engine):
    self.merk = merk
    self.tahun = tahun
    self.warna = warna
    self.start_engine = start_engine

  def start(self):
    if self.start_engine:
      print("Mesin telah dinyalakan")
    else:
      print("Mesin belum dinyalakan")

  def tampilkan_info(self):
    print(f"Merk: {self.merk}, Tahun: {self.tahun}, Warna: {self.warna}, {self.start_engine}")

mobil1 = Mobil("Toyota", 2020, "Merah", True)
mobil2 = Mobil("Honda", 2022, "Biru", False)

mobil1.tampilkan_info()
mobil1.start()
mobil2.tampilkan_info()
mobil2.start() 