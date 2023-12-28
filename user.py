from data import *
from tabulate import tabulate
class User:
    def __init__(self, username):
        self.username = username
        
    def check_benefit(self):
        print(tabulate(table, 
                       header, 
                       tablefmt = "pretty"))
        
    def check_plan(self, username):
        for key, value in user_data.items():
            try:
                if key == username:
                    print(f"Username : {username}")
                    print(f"Plan : {value[0]}")
                    print(f"Durasi Plan : {value[1]}")
                    print("Plan Benefits :")
                    
                    new_header = []
                    new_table = []
                    row = []
                                
                    if value[0] == 'Basic Plan':
                        for baris in range(len(table)):
                            row.append(table[baris][0])
                            row.append(table[baris][-1])
                            new_table.append(row)
                            row = []
                        
                        new_header.append(header[0])
                        new_header.append(header[-1])
                        
                        print(tabulate(new_table, 
                                       new_header, 
                                       tablefmt = "pretty"))
                
                    elif value[0] == 'Standard Plan':
                        for baris in range(len(table)):
                            row.append(table[baris][1])
                            row.append(table[baris][-1])
                            new_table.append(row)
                            row = []
                        
                        new_header.append(header[1])
                        new_header.append(header[-1])
                        
                        print(tabulate(new_table, 
                                       new_header, 
                                       tablefmt = "pretty"))
                        
                    elif value[0] == 'Premium Plan':
                        for baris in range(len(table)):
                            row.append(table[baris][2])
                            row.append(table[baris][-1])
                            new_table.append(row)
                            row = []
                        
                        new_header.append(header[2])
                        new_header.append(header[-1])
                        
                        print(tabulate(new_table, 
                                       new_header, 
                                       tablefmt = "pretty"))
                        
                    else:
                        raise Exception("Invalid plan")
                 
            except:
                raise Exception("Username tidak ada")
        
    def upgrade_plan(self, username, new_plan):
        for name, info in user_data.items():
            if name == username:
                # new_plan = info[0]
                duration_plan = info[1]
                
                if duration_plan > 12:
                    discount = 0.05 
                    if new_plan == 'Basic Plan':
                        harga_potongan = 120_000 * discount
                        total_bayar = 120_000 - harga_potongan
                        print(f"Total yang harus dibayar oleh {name} = {total_bayar}")
                        
                    elif new_plan == 'Standard Plan':
                        harga_potongan = 160_000 * discount
                        total_bayar = 160_000 - harga_potongan
                        print(f"Total yang harus dibayar oleh {name} = {total_bayar}")
                        
                    elif new_plan == 'Premium Plan':
                        harga_potongan = 200_000 * discount
                        total_bayar = 200_000 - harga_potongan
                        print(f"Total yang harus dibayar oleh {name} = {total_bayar}")
                        
                    else:
                        raise Exception("Plan tidak ditemukan")
                    
                else:
                    discount = 0.00 
                    
                    if new_plan == 'Basic Plan':
                        harga_potongan = 120_000 * discount
                        total_bayar = 120_000 - harga_potongan
                        print(f"Total yang harus dibayar oleh {name} = {total_bayar}")
                        
                    elif new_plan == 'Standard Plan':
                        harga_potongan = 160_000 * discount
                        total_bayar = 160_000 - harga_potongan
                        print(f"Total yang harus dibayar oleh {name} = {total_bayar}")
                        
                    elif new_plan == 'Premium Plan':
                        harga_potongan = 200_000 * discount
                        total_bayar = 200_000 - harga_potongan
                        print(f"Total yang harus dibayar oleh {name} = {total_bayar}")
                        
                    else:
                        raise Exception("Plan tidak ditemukan")                
        