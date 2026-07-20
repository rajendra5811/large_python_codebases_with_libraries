class Person:
    def __init__(self, person_id, name, age):
        self.__person_id = person_id
        self.__name = name
        self.__age = age

    # display method to print the details of the person
    def display(self):
     print(f"{self.__person_id}\t{self.__name}\t{self.__age}\n")
    
    # read-only method.
    def get_name(self):
     return self.__name

    # write-only name method.
    def set_name(self, new_name):
      new_name = str(input("Enter new name: ")) 
      if len(new_name) < 3:
        print("Invalid Name")
        return False
      self.__name = new_name
      return True
 
   # read-only age method.
    def get_age(self):
      return self.__age
    
    # write-only age method.
    def set_age(self, new_age):
      new_age = int(input("Enter new age: "))
      if new_age < 0 or new_age > 120:
        print("Invalid Age")
        return False
      self.__age = new_age
      return True

class Employee(Person):
    def __init__(self, person_id, name, age, department, employee_id, is_active):
        super().__init__(person_id, name, age)
        self.department = department
        self.employee_id = employee_id  
        self.is_active = True  # default value for is_active

    # display method to print the details of the employee
    def display(self):
        super().display()
        print(f"{self.department}\t{self.employee_id}\t{self.is_active}\n")
    
    def get_employee_id(self):
        return self.employee_id
    
    def is_active(self):
        return self.is_active
    

    
    #activate method to activate the employee
    def activate(self):
        self.is_active = True
        print(f"Employee {self.employee_id} is activated.")
    
   #deactivate method to deactivate the employee
    def deactivate(self):
        self.is_active = False
        print(f"Employee {self.employee_id} is deactivated.")

class Security_Guard(Person):
    def __init__(self, person_id, name, age, guard_id, shift):
        super().__init__(person_id, name, age)
        self.guard_id = guard_id
        self.shift = shift

    def display(self): 
       super().display()
       print(f"{self.guard_id}\t{self.shift}\n")

class FingerPrint:
    def __init__(self, fingerprint_id, is_registered):
        self.fingerprint_id = fingerprint_id
        self.is_registered = is_registered

    def register(self):
        self.is_registered = True
        print(f"Fingerprint {self.fingerprint_id} is registered.")
    
    def verify(self):
        if self.is_registered:
            print(f"Fingerprint {self.fingerprint_id} is verified.")
        else:
            print(f"Fingerprint {self.fingerprint_id} is not registered.")

class Attendence:
    def __init__(self, employee, date, time, status):
        self.employee = employee
        self.status = status
        self.date = date
        self.time = time


    def display(self):
        print(f"{self.employee.get_name()}\t{self.date}\t{self.time}\t{self.status}\n")
        
class Biometric_system:
    def __init__(self):
        self.employees = []
        self.security_guards = []
        self.fingerprints = []
        self.attendances = []

    def add_employee(self, employee):
        self.employees.append(employee)
    
    def add_security_guard(self, security_guard):
        self.security_guards.append(security_guard)
    
    def add_fingerprint(self, fingerprint):
        self.fingerprints.append(fingerprint)
    
    def add_attendance(self, attendance):
        self.attendances.append(attendance)

    def activate_employee(self, employee):  
        employee.activate()

    def deactivate_employee(self, employee):    
        employee.deactivate()

    def register_fingerprint(self, fingerprint):
        fingerprint.register()

    def find_employee(self, employee_id):
        for employee in self.employees: #employee_id 
            if employee.get_employee_id() == employee_id:
                return employee
        return None

    def find_guard(self, guard_id):
        for guard in self.security_guards:
            if guard.guard_id == guard_id:
                return guard
        return None

    def find_attendance(self, attendance_id):
        for attendance in self.attendances:
            if attendance.attendance_id == attendance_id:
                return attendance
        return None

    def add_employee(self, employee):
        self.employees.append(employee)
    
    def add_guard(self, guard):
        self.security_guards.append(guard)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def active_employees(self):
        for employee in self.employees:
            if employee.is_active:
                print(f"{employee.get_name()} is active.")
        return employee 
    
    def registered_fingerprints(self):
        for fingerprint in self.fingerprints:
            if fingerprint.is_registered:
                print(f"Fingerprint {fingerprint.fingerprint_id} is registered.")
        return fingerprint
    
    def display_employees(self):
        for employee in self.employees:
            employee.display()

    def display_attendance(self):
        for attendance in self.attendances:
            attendance.display()

    def validate_age(self, age):
        if age < 18 or age > 65:
            print("Invalid Age")
            return False
        return True

    def validate_fingerprint(self, fingerprint):
        if not fingerprint.is_registered:
            print("Fingerprint is not registered.")
            return False
        return True
    
    def allow_access(self, employee, fingerprint):
        if employee.is_active and fingerprint.is_registered:
            print(f"Access granted to {employee.get_name()}.")
            return True
        else:
            print(f"Access denied to {employee.get_name()}.")
            return False

    def mark_attendance(self, employee, date, time, status):
        attendance = Attendence(employee, date, time, status)
        self.attendances.append(attendance)
        print(f"Attendance marked for {employee.get_name()} on {date} at {time} with status {status}.")


# Create the biometric system instance  
biometricsystem = Biometric_system()

# Create employees
employee1 = Employee(1, "John Doe", 30, "IT", 101, True)
employee2 = Employee(2, "Jane Smith", 25, "HR", 102, True)
employee3 = Employee(3, "Mike Johnson", 40, "Finance", 103, False)

# Add employees to the system
biometricsystem.add_employee(employee1)
biometricsystem.add_employee(employee2)
biometricsystem.add_employee(employee3)

# Create fingerprints
fingerprint1 = FingerPrint(1, True)
fingerprint2 = FingerPrint(2, False)
fingerprint3 = FingerPrint(3, True)

# Add fingerprints to the system
biometricsystem.add_fingerprint(fingerprint1)
biometricsystem.add_fingerprint(fingerprint2)
biometricsystem.add_fingerprint(fingerprint3)

# Create attendance records
attendance1 = Attendence(employee1, "2023-10-01", "09:00", "Present")
attendance2 = Attendence(employee2, "2023-10-01", "09:15", "Present")
attendance3 = Attendence(employee3, "2023-10-01", "09:30", "Absent")

# Add attendance to the system
biometricsystem.add_attendance(attendance1)
biometricsystem.add_attendance(attendance2)
biometricsystem.add_attendance(attendance3)

# Create security guards
security_guard1 = Security_Guard(1, "Guard 1", 35, "G001", "Day")
security_guard2 = Security_Guard(2, "Guard 2", 40, "G002", "Night")

# Add security guards to the system
biometricsystem.add_security_guard(security_guard1)
biometricsystem.add_security_guard(security_guard2)


# --- Demonstrate / call methods on the system ---

# Display all employees
print("=== All Employees ===")
biometricsystem.display_employees()

# Display all attendance records
print("=== Attendance Records ===")
biometricsystem.display_attendance()

# Find an employee by employee_id
emp = biometricsystem.find_employee(102)
if emp:
    print("=== Found Employee ===")
    emp.display()
else:
    print("Employee not found.")

# Activate an inactive employee (employee3 is inactive)
print("=== Activate Employee ===")
biometricsystem.activate_employee(employee3)

# Deactivate an active employee (employee1)
print("=== Deactivate Employee ===")
biometricsystem.deactivate_employee(employee1)

# Register a fingerprint that is not registered
print("=== Register Fingerprint ===")
biometricsystem.register_fingerprint(fingerprint2)

# Show registered fingerprints
print("=== Registered Fingerprints ===")
biometricsystem.registered_fingerprints()

# Validate age using system validator
print("=== Age Validation ===")
print("Age 25 valid?", biometricsystem.validate_age(25))
print("Age 70 valid?", biometricsystem.validate_age(70))

# Validate a fingerprint
print("=== Fingerprint Validation ===")
print("Fingerprint1 valid?", biometricsystem.validate_fingerprint(fingerprint1))
print("Fingerprint2 valid?", biometricsystem.validate_fingerprint(fingerprint2))

# Allow access based on employee status and fingerprint
print("=== Access Control ===")
biometricsystem.allow_access(employee1, fingerprint1)
biometricsystem.allow_access(employee3, fingerprint2)

# Mark new attendance
print("=== Mark Attendance ===")
biometricsystem.mark_attendance(employee1, "2023-10-02", "08:55", "Present")

# Show active employees
print("=== Active Employees ===")
biometricsystem.active_employees()

# Show updated attendance
print("=== Updated Attendance ===")
biometricsystem.display_attendance()
