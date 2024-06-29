# Import package
from tabulate import tabulate


class Transaction:

    """
    A class for system of self-service cashier.
    
    Attributes
    ----------
    nama_item (list):
        collect name of item, must be string
    
    jumlah_item (list):
        collect quantity of item, must be integer

    harga_per_item (list):
        collect price per item, can be integer/float
    
    dict_item (dictionary):
        summarize name of item, quantity of item, and price per item

    DISCOUNT_1 (float):
        If total shopping price greater than Rp 200000, get discount 5%

    DISCOUNT_2 (float):
        If total shopping price greater than Rp 300000, get discount 8%

    DISCOUNT_3 (float):
        If total shopping price greater than Rp 500000, get discount 10%

    
    Methods
    -------
    add_item(nama_item,jumlah_item,harga_per_item):
        Function to collect and summarize item

    update_item_name(nama_item,update_nama_item):
        Function to change name of item
    
    update_item_quantity(nama_item,update_jumlah_item):
        Function to update quantity of item

    update_item_price(nama_item,update_harga_item):
        Function to update price of item

    delete_item(nama_item):
        Function to delete one or more item

    reset_transaction():
        Function to delete all item

    check_order():
        Function to generate table of item

    total_price():
        Function to generate total shopping price
    
    """
    
    nama_item = []
    jumlah_item = []
    harga_per_item = []
    dict_item = {}
    DISCOUNT_1 = 0.05
    DISCOUNT_2 = 0.08
    DISCOUNT_3 = 0.1

    def add_item(self,nama_item: str,jumlah_item: int,harga_per_item: float|int):

        try:
            self.nama_item = str(nama_item)
            self.jumlah_item = int(jumlah_item)
            self.harga_per_item = int(float(harga_per_item))
            
            Transaction.nama_item += [self.nama_item]
            Transaction.jumlah_item += [self.jumlah_item]
            Transaction.harga_per_item += [self.harga_per_item]

            Transaction.dict_item.update({Transaction.nama_item.pop(): [Transaction.jumlah_item.pop(), Transaction.harga_per_item.pop()]})

        except:
            print("Cek input data anda (nama item/jumlah item/harga item)!")
        
        else:
            return f"Item yang dibeli adalah: {Transaction.dict_item}"
        

    def update_item_name(self,nama_item: str,update_nama_item: str):

        if type(nama_item) is str:

            self.nama_item = nama_item
            self.update_nama_item = update_nama_item

            if self.nama_item in list(Transaction.dict_item.keys()):
                Transaction.dict_item[self.update_nama_item] = Transaction.dict_item.pop(self.nama_item)
                print(Transaction.dict_item)

            elif self.nama_item not in list(Transaction.dict_item.keys()):
                print("Cek nama item yang anda input!")
                print("---------------------------------")
                print(Transaction.dict_item)

        else:
            print("Cek nama item yang anda input!")


    def update_item_quantity(self,nama_item: str,update_jumlah_item: int):

        self.nama_item = nama_item

        if type(update_jumlah_item) is int:
            self.update_jumlah_item = int(update_jumlah_item)

            if self.nama_item in list(Transaction.dict_item.keys()):
                Transaction.dict_item[self.nama_item][0] = self.update_jumlah_item
                print(Transaction.dict_item)

            elif self.nama_item not in list(Transaction.dict_item.keys()):
                print("Cek nama item yang anda input!")
                print("---------------------------------")
                print(Transaction.dict_item)
                
        else:
            print("Cek jumlah item yang anda input!")


    def update_item_price(self,nama_item: str,update_harga_item: float|int):

        self.nama_item = nama_item
        
        if type(update_harga_item) is int or type(update_harga_item) is float:
            self.update_harga_item = int(update_harga_item)
            
            if self.nama_item in list(Transaction.dict_item.keys()):
                Transaction.dict_item[self.nama_item][1] = self.update_harga_item
                print(Transaction.dict_item)

            elif self.nama_item not in list(Transaction.dict_item.keys()):
                print("Cek nama item yang anda input!")
                print("---------------------------------")
                print(Transaction.dict_item)
                
        else:
            print("Cek harga item yang anda input!")

    
    def delete_item(self,nama_item: str):

        self.nama_item = nama_item
        
        if type(self.nama_item) is str:

            try:
                if self.nama_item in list(Transaction.dict_item.keys()):
                    Transaction.dict_item.pop(self.nama_item)
                    print(Transaction.dict_item)
            
                elif self.nama_item not in list(Transaction.dict_item.keys()):
                    print("Item anda telah dihapus/belum dimasukkan/belum diupdate, coba lagi!")
                    print("---------------------------------")
                    print(Transaction.dict_item)

            except:
                print("Item anda telah dihapus/belum dimasukkan/belum diupdate, coba lagi!")

        else:
            print("Cek nama item yang anda input!")


    def reset_transaction(self):

        try:
            Transaction.dict_item.clear()
            print("Semua item berhasil di delete!")

        except:
            print("Semua item telah dihapus, silahkan diinput kembali!")


    def check_order(self):

        try:
            
            list_item = list(Transaction.dict_item.keys())
            list_jumlah_item = []
            list_harga_item = []
            
            for i in list(Transaction.dict_item.values()):
                list_jumlah_item.append(i[0]) 
                list_harga_item.append(i[1])

            if list_item.count('') == 0 and list_item.count('None') == 0 and [a for a in list_jumlah_item if a < 0] == []  and [b for b in list_harga_item if b < 0] == []:

                self.list_total_harga = [jumlah * harga for jumlah, harga in zip(list_jumlah_item, list_harga_item)]
                list_number = [i[0] + 1 for i in enumerate(list_item)]

                headers = ['No','Nama item','Jumlah item','Harga per item','Total harga']
                table_content = [[nomor,item,jumlah,harga,total] for nomor,item,jumlah,harga,total in \
                                 zip(list_number,list_item,list_jumlah_item,list_harga_item,self.list_total_harga)]

                print("Pemesanan sudah benar")
                print("-------------------------------------------------------------------------")
                print(tabulate(table_content,headers, tablefmt="github",colalign=('center','center','center','center','center'),numalign=('center')))
                print("-------------------------------------------------------------------------")

            elif list_item.count('') != 0 or list_item.count('None') != 0 or [a for a in list_jumlah_item if a < 0] != []  or [b for b in list_harga_item if b < 0] != [] :
                print("Terdapat kesalahan input data!")

        except:
            print("Silahkan diinput kembali!") 


    def total_price(self):
        
        try:
            list_item = list(Transaction.dict_item.keys())

            if list_item.count('') == 0 and list_item.count('None') == 0:
                
                total_belanja = sum(self.list_total_harga)
            
                if total_belanja >= 0 and total_belanja <= 200_000:
                    total_harga = total_belanja
                    print(f"Total belanjaan anda adalah: Rp {total_harga}")
                
                elif total_belanja > 200000 and total_belanja <= 300000:
                    total_harga = total_belanja - Transaction.DISCOUNT_1 * total_belanja
                    print(f"Anda mendapatkan diskon {int(Transaction.DISCOUNT_1*100)}%")
                    print(f"-> Total belanjaan anda adalah: Rp {int(total_harga)}")
                
                elif total_belanja > 300000 and total_belanja <= 500000:
                    total_harga = total_belanja - Transaction.DISCOUNT_2 * total_belanja
                    print(f"Anda mendapatkan diskon {int(Transaction.DISCOUNT_2*100)}%")
                    print(f"-> Total belanjaan anda adalah: Rp {int(total_harga)}")
                
                elif total_belanja > 500000:
                    total_harga = total_belanja - Transaction.DISCOUNT_3 * total_belanja
                    print(f"Anda mendapatkan diskon {int(Transaction.DISCOUNT_3*100)}%")
                    print(f"-> Total belanjaan anda adalah: Rp {int(total_harga)}")

            else:
                print('Terdapat kesalahan input data!')
            
        except:
            print("Silahkan diinput kembali!")

        finally:
            print("---------------------------------")
            print("Terima kasih!")