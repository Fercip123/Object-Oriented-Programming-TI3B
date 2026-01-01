class kucing:
  def __init__(self, nama, warna, jenis_kelamin, suasana_hati_kucing):
    self.nama = nama
    self.warna = warna
    self.jenis_kelamin = jenis_kelamin
    self.suasana_hati_kucing = suasana_hati_kucing

  def tampilkan_info_kucing(self):
    print(f"Nama: {self.nama}")
    print(f"Warna: {self.warna}")
    print(f"Jenis Kelamin: {self.jenis_kelamin}")
    print(f"Suasana Hati: {self.suasana_hati_kucing}")

  def tampilkan_suasana_hati_level(self):
    mood_levels = {
        "baik": 100,
        "kurang baik": 60,
        "buruk": 30
    }
    level = mood_levels.get(self.suasana_hati_kucing.lower(), "Tidak Diketahui")
    print(f"Suasana hati kucing ({self.suasana_hati_kucing}): Level {level}")


class pemilik:
  def __init__(self, nama, jumlah_kucing):
    self.nama = nama
    self.jumlah_kucing = jumlah_kucing
    self.cara_meningkatkan_suasana_hati = {
        "memberi makan": 100,
        "memberi susu": 60,
        "memberi makanan kucing": 30
    }

  def tampilkan_info_pemilik(self):
    print(f"\nNama: {self.nama}")
    print(f"Jumlah kucing: {self.jumlah_kucing}")
    print(f"Cara meningkatkan suasana hati: {self.cara_meningkatkan_suasana_hati}")

  def berinteraksi(self, kucing_obj, interaksi):
    print(f"\n{self.nama} berinteraksi dengan {kucing_obj.nama} dengan method '{interaksi}'")
    interaksi_poin = self.cara_meningkatkan_suasana_hati.get(interaksi.lower())

    if interaksi_poin is not None:
        print(f"Interaksi '{interaksi}' memberikan {interaksi_poin} points.")
    elif {self.cara_meningkatkan_suasana_hati} == "memberi makan":
        {self.cara_meningkatkan_suasana_hati} + interaksi_poin
        print(f"Interaksi '{interaksi}' increases mood.")
    else:
        print(f"Interaksi '{interaksi}' not known or does not increase mood.")

# Example Usage:
my_cat = kucing("Kitty", "orange", "betina", "baik")
my_owner = pemilik("Adi", 1)

my_cat.tampilkan_info_kucing()
my_cat.tampilkan_suasana_hati_level()

my_owner.tampilkan_info_pemilik()
my_owner.berinteraksi(my_cat, "Memberi makan")

# Another example
sad_cat = kucing("Milo", "black", "jantan", "buruk")
sad_cat.tampilkan_info_kucing()
sad_cat.tampilkan_suasana_hati_level()
my_owner.berinteraksi(sad_cat, "Memberi susu")