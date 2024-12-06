class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"Сотрудник: {self.name}, id: {self.id}"

class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def get_info(self):
        return f'Менеджер: {self.name}, id: {self.id}, Отдел: {self.department}'

    def manage_project(self):
        return f'Менеджер {self.name}, id: {self.id}, управляет отделом {self.department}'

class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def get_info(self):
        return f'Техник: {self.name}, id: {self.id}, Специализация: {self.specialization}'

    def perform_maintenance(self):
        return f'Техник {self.name}, id: {self.id}, со специализацией {self.specialization}, выполнил обслуживание'

employee_list = []

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)

    def get_info(self):
        return f"Техменеджер: {self.name}, id: {self.id}, Отдел: {self.department}, специализация: {self.specialization}"

    def manage_project(self):
        return f'Техменеджер {self.name}, id: {self.id}, со специализацией {self.specialization} управляет отделом {self.department}'

    def perform_maintenance(self):
        return f'Техменеджер {self.name}, id: {self.id}, со специализацией {self.specialization}, выполнил обслуживание'

    def add_employee(self, employee):
            employee_list.append(employee)
            return 'сотрудник добавлен'

    def get_team_info(self):
        team = 'Команда:\n'
        for i in employee_list:
            team += i.get_info() + '\n'
        return team

emp1 = Employee('e1','001')
emp2 = Manager('e2','002','netw')
emp3 = Technician('e3','003','ai')
emp4 = TechManager('e4','004','it','engineering')

print(emp1.get_info()) # класс Employee

print(emp2.get_info()) # класс Manager
print(emp2.manage_project())

print(emp3.get_info()) # класс Technician
print(emp3.perform_maintenance())

print(emp4.get_info()) # класс TechManager
print(emp4.manage_project())
print(emp4.perform_maintenance())

print(emp4.add_employee(emp1)) # добавление сотрудников и вывод инф о команде
print(emp4.add_employee(emp2))
print(emp4.add_employee(emp3))
print(emp4.add_employee(emp4))
print(emp4.get_team_info())