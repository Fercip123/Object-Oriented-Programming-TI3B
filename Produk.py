class Produk :
    def __init__(self, nama, harga, pakaian, elektronik, makanan, stok) :
      self.nama = nama
      self.harga = harga
      self.pakaian = pakaian
      self.elektronik = elektronik
      self.makanan = makanan
      self.stok = stok

class Harga (Produk):
  def __init__(self, harga) :
    self.pakaian = 500
    self.elektronik = 2000
    self.makanan = 300

  def tampilkan_harga(self) :
    print(f"Pakaian dengan harga = {self.pakaian}")
    print(f"eletronik dengan harga = {self.elektronik}")
    print(f"makanan dengan harga = {self.makanan}")

class pakaian (Produk) :
  def __init__(self, baju, celana) :
    self.baju = "baju"
    self.celana = "celana"

  def tampilkan_pakaian(self) :
    print(f"Baju = {self.baju}")
    print(f"Celana = {self.celana}")

class elektronik : # This class does not inherit from Produk, unlike 'Harga' and 'pakaian'
  def __init__(self, handphone, komputer) :
    self.handphone = "handphone"
    self.komputer = "komputer"

  def tampilkan_elektronik(self) :
    print(f"Handphone = {self.handphone}")


# The call to 'Harga' constructor with (0) is a bit odd given its __init__ signature.
# Assuming it's for demonstration and the 'harga' parameter isn't strictly used internally.
harga_obj = Harga(0)
harga_obj.tampilkan_harga()
