class Mahasiswa:
    def __init__(self, nama, nim):
      self.nama = nama # Public
      self.__nim = nim # Private

m1 = Mahasiswa("Riko", "220110")

print(m1.nama) # Berhasil
print(m1.__nim) # Error!
