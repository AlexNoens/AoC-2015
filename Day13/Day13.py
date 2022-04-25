class Guest:
    name = ""
    neighbour_l = ""
    neighbour_r = ""
    happiness = {}
    def __init__(self,name):
        self.name = name

    def add_happiness_case(self,name,score):
        self.happiness[name] = score



def load_input():
    f = open("Day13/smol.txt", "r")
    return f.readlines()

def calc_score(mod,mag):
    if mod == "lose":
        return -int(mag)
    return int(mag)

def process_input(file):
    guest_list = {}
    split_list = []
    for each in file:
        split_list = each.split(" ")
        print(split_list)
        try:
            guest_list[split_list[0]] = Guest(split_list[0])
            guest_list[split_list[0]].add_happiness_case(split_list[10],calc_score(split_list[2],split_list[3]))
        except:
            guest_list[split_list[0]].add_happiness_case(split_list[10],calc_score(split_list[2],split_list[3]))
            pass

    print(guest_list["Alice"].name)
    print(guest_list["Alice"].happiness)

if __name__ == "__main__":
    process_input(load_input())
