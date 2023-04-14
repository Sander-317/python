
class Homeowner:
    def __init__(self, name, address, needs):
        
        if isinstance(name, str):
            if len(name) > 0:
                self.name = name
            else:
                raise ValueError("enter valid name please")
        else:
            raise ValueError("enter valid name please")
        
        if isinstance(address, str):
            if len(address) > 0:
                self.address = address
            else:
                raise ValueError("enter valid address please")
        else:
            raise ValueError("enter valid address please")
        
        if isinstance(needs, list):
            self.needs = needs
        else:
            raise ValueError("please enter a list")
        
    def find_specialist(self, specialists_list):
        new_list = []
        for need in self.needs:
            print("need in find specialist  ", need)
            for specialist in specialists_list:
                print("specialist and need in find specialist  ", specialist.specialty, need)
                # breakpoint()
                if need == specialist.specialty:
                    new_list.append((need, specialist.name, specialist.price))
                    break
                break        
              
            continue
          
        return new_list


class Specialist:
    def __init__(self, name, price):
        if isinstance(name, str):
            if len(name) > 0:
                self.name = name
            else:
                raise ValueError("enter valid name please")
        else:
            raise ValueError("enter valid name please")
        
        if isinstance(price, (int, float)):
            if price > 0:
                self.price = price
            else:
                raise ValueError("enter valid price please")
        else:
            raise ValueError("enter valid price please")

class Electrician(Specialist):
    Specialist.specialty = 'electrician'
        
class Painter(Specialist):
    Specialist.specialty = 'painter'

class Plumber(Specialist):
    Specialist.specialty = 'plumber'

# Homeowners
alfred = Homeowner("Alfred Alfredson","Alfredslane 123", ["painter", "plumber"] )
bert = Homeowner("Bert Bertson","Bertslane 231",["plumber"])
candice = Homeowner("Candice Candicedottir",  "Candicelane 312",["electrician", "painter"])


# Specialists
alice = Electrician("alice", 50)
bob = Painter("bob", 50)
craig = Plumber("craig", 50)
specialists_list = [alice,bob,craig]

bert.find_specialist(specialists_list)
test1 = alfred.find_specialist(specialists_list)
print(test1)

# test = Electrician("dude", 30)
# print(test.name,test.specialty)
# print(specialists_list)
# print(Homeowner("test dude", "test street", ["plumber"]))
# print(alfred.name)