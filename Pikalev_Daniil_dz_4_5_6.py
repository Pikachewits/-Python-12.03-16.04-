class Storage:
    def __init__(self, title):
        self.title = title
        self.lists = {}
        self.give_lists = {}

    def take_to_storage(self, equipment):
        self.lists.update({equipment.serial_number:[equipment.title]})
        print('На склад '+self.title+' получено оборудование: '+equipment.title+', серийный номер - '+ str(equipment.serial_number))


    def give_to_storage(self, equipment, other):
        self.give_lists.update({equipment.serial_number: [equipment.title, other]})
        print('Передано оборудование: ' + equipment.title + ' ,серийный номер - ' + str(equipment.serial_number))
        other.take_to_storage(equipment)


    def list_equipments(self):
        print('На склад '+self.title + ' получено оборудование: ')
        print(self.lists)
        print('Общее количество: ', len(self.lists))
        print('Со склада '+self.title + ' выдано оборудование: ')
        print(self.give_lists)
        print('Общее количество: ', len(self.give_lists))




class Office_equipment:
    def __init__(self, title, serial_number):
        self.title = title
        self.serial_number = serial_number

    def __str__(self):
        return str(self.title)

class Printer(Office_equipment):
    def __init__(self,title,serial_number, print_velocity):
        Office_equipment.__init__(self,title, serial_number)
        self.print_velocity = print_velocity

    def __str__(self):
        return  'Название модели: '+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.print_velocity)


class Scanner(Office_equipment):
    def __init__(self, title,serial_number,resolution):
        Office_equipment.__init__(self,title, serial_number)
        self.resolution = resolution

    def __str__(self):
        return  'Название модели: '+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.resolution)

class Copier(Office_equipment):
    def __init__(self, title,serial_number, addit):
        Office_equipment.__init__(self, title, serial_number)
        self.addit = addit

    def __str__(self):
        return  'Название модели: '+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.addit)



store1 = Storage(' "Главный склад" ')
store2 = Storage(' "Маленький склад" ')
a = Printer('HP', 98625, 100)
b = Scanner('Epson', 16548, 4000)
c = Copier('Samsung', 165486, 50)
d = Printer('Sony', 68892, 200)

print(a)
print(b)
print(c)
print(d)

store1.take_to_storage(a)
store1.take_to_storage(b)
store1.take_to_storage(c)
store1.take_to_storage(d)

store1.give_to_storage(a, store2)

store1.list_equipments()
store2.list_equipments()
