from data import *
class NewUser:
    def __init__(self, username):
        self.username = username
    
    def check_benefit(self):
        print(tabulate(table, header, tablefmt="pretty"))
    
    def pick_plan(self, new_plan, referral_code):
        try:
            user_info = user_data.get(self.username)
            if user_info:
                plan_index = header.index(new_plan)
                plan_price = table[-1][plan_index]

                if referral_code == user_info[-1]:
                    discount = 0.04
                    print("Referral code exists")
                else:
                    raise Exception("Referral code not found")

                final_price = plan_price * (1 - discount)
                print(f"Harga yang harus dibayar {self.username} adalah {final_price:.3f}")

            else:
                raise Exception("Username tidak valid")

        except Exception as e:
            print(f"Error: {e}")
            # Handle the exception or re-raise it if needed
            raise