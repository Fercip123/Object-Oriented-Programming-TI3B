class BankAccount:
  def __init__(self, pemilik, saldo_awal=0):
    self.pemilik = pemilik
    self.__saldo = saldo_awal

  def get_saldo(self):
    return self.__saldo

  def deposit(self, jumlah):
    if jumlah > 0:
      self.__saldo += jumlah
      return f"Berhasil deposit {jumlah}. Saldo baru: {self.__saldo}"
    else:
      return "Jumlah deposit harus positif."

  def withdraw(self, jumlah):
    if jumlah > 0 and self.__saldo >= jumlah:
      self.__saldo -= jumlah
      return f"Berhasil tarik {jumlah}. Saldo baru: {self.__saldo}"
    elif jumlah <= 0:
      return "Jumlah penarikan harus positif."
    else:
      return "Saldo tidak cukup."

my_account = BankAccount("Alice", 1000)

print("Nama pemilik : ", my_account.pemilik)
print("Saldo awal : ", my_account.get_saldo())
print("Deposit sebesar 500")
print(my_account.deposit(500))
print("Saldo sekarang : ", my_account.get_saldo())
print("Tarik saldo : ", my_account.withdraw(2000))
