class Mahasiswa :
    def __init__(self, nama, nim) :
      self.nama = nama
      self.__nim = nim

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim_baru):
        if len(nim_baru) == 6:
          self.__nim = nim_baru
        else:
          print("Format NIM salah!")

ml = Mahasiswa("Radit", "220110")
print("NIM awal:", ml.get_nim())

ml.set_nim("123")
ml.set_nim("240201")
print("NIM baru:", ml.get_nim())
