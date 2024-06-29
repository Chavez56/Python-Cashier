# Import module
from module_transaction import Transaction

# Assign module to variable
trnsct_123 = Transaction()

print("TEST CASE 1")
print("----------------")

trnsct_123.add_item(nama_item = 'Ayam Goreng',jumlah_item = 2, harga_per_item = 20_000)
print(trnsct_123.add_item(nama_item = 'Pasta Gigi',jumlah_item = 3, harga_per_item = 15_000))

print()

print("TEST CASE 2")
print("----------------")

trnsct_123.delete_item(nama_item='Pasta Gigi')

print()

print("TEST CASE 3")
print("----------------")

trnsct_123.reset_transaction()

print()

print("TEST CASE 4")
print("----------------")

trnsct_123.add_item(nama_item = 'Ayam Goreng',jumlah_item = 2, harga_per_item = 20_000)
trnsct_123.add_item(nama_item = 'Pasta Gigi',jumlah_item = 3, harga_per_item = 15_000)
trnsct_123.add_item(nama_item = 'Mainan Mobil',jumlah_item = 1, harga_per_item = 200_000)
print(trnsct_123.add_item(nama_item = 'Mi Instan',jumlah_item = 5, harga_per_item = 3_000))

trnsct_123.check_order()

trnsct_123.total_price()

print()

print("TEST CASE 5")
print("----------------")

trnsct_123.reset_transaction()

trnsct_123.add_item(nama_item = 'Ayam Goreng',jumlah_item = 2, harga_per_item = 20_000)
trnsct_123.add_item(nama_item = 'Pasta Gigi',jumlah_item = 3, harga_per_item = 15_000)
trnsct_123.add_item(nama_item = 'Mainan Mobil',jumlah_item = 1, harga_per_item = 200_000)
print(trnsct_123.add_item(nama_item = 'Mi Instan',jumlah_item = 5, harga_per_item = 3_000))

print()
trnsct_123.update_item_name(nama_item='Ayam Goreng', update_nama_item='Ayam Bakar')
trnsct_123.update_item_quantity(nama_item='Mi Instan',update_jumlah_item=10)
trnsct_123.update_item_price(nama_item='Pasta Gigi',update_harga_item=25_000)
trnsct_123.update_item_quantity(nama_item='Ayam Bakar',update_jumlah_item=4)

trnsct_123.check_order()

trnsct_123.total_price()

print()

print("SPECIAL TEST CASE")
print("----------------")

trnsct_123.reset_transaction()

trnsct_123.add_item(nama_item = 'Ayam Goreng',jumlah_item = 2, harga_per_item = 20_000)
trnsct_123.add_item(nama_item = '',jumlah_item = 3, harga_per_item = 15_000)
trnsct_123.add_item(nama_item = None,jumlah_item = 1, harga_per_item = 200_000)
print(trnsct_123.add_item(nama_item = 'Mi Instan',jumlah_item = 5, harga_per_item = '3_000'))

trnsct_123.check_order()

trnsct_123.total_price()