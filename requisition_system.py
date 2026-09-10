## IT5016_ assessment 3
#programming principles and concepts
#Requisition system
#author:Belay Gebressilassie
#IT5016-Assessment 3,(Student ID:20267238)
#Class:software Development
#SRP (Single Responsibility Principle):
#The Requisition class is responsible for storing and managing
#information about a single requisition.
#YAGNI(you Arent't Gonna Need It):
#The program includes only the features required for the
#requisition extra functionality.
requisition_counter = 10000
class Requisitionsystem:
    def __init__(self):
        self.date=""
        self.staff_id=""
        self.staff_name=""
        self.requisition_id=0
        self.total=0
        self.status="Pending"
        self.approval_reference="Not available"
        self.items=[]
#KISS (Keep It Simple,Stupid):
#This function uses a simple calculation to creat
#a new requisition ID,making the code easy to understand.
    def staff_info(self,date,staff_id,staff_name):
        global requisition_counter
        self.date=date
        self.staff_id=staff_id
        self.staff_name=staff_name

        requisition_counter+=1
        self.requisition_id=requisition_counter

    def requisitions_details(self,items):
        self.items=items
        self.total=0

        for item in items:
            self.total+=item[1]

        return self.total
    
    def requisition_approval(self):
        if self.total<500:
            self.status="Approved"
            self.approval_reference=self.staff_id + str(self.requisition_id)[-3:]
        else:
            self.status="Pending"
#OCP(Open/Closed principle):
# The approval process is organised in a separate method,
# so the system can be extended with new approval rules
# without changing the rest of the requisition system.         
    def respond_requisition(self,response):
        if response=="Approved":
            self.status="Approved"
            self.approval_reference=self.staff_id+str(self.requisition_id)[-3:]
        elif response=="Not approved":
                self.status="Not approved"
                self.approval_reference="Not available"
#Separation of concerns (SoC):
#This method focuses on displaying requisition information.
#Keeping display tasks separate makes the program easier to maintain.
    def display_requisitions(self):
        print("Date:",self.date)
        print("Requisition ID:",self.requisition_id)
        print("Staff ID:",self.staff_id)
        print("Staff Name:",self.staff_name)
        print("Total:$",self.total)
        print("Status:",self.status)
        print("Approval Reference Number:",self.approval_reference)
        print()

#DRY(Don't Repeat Yourself):
#This method uses one reusable function to calculate
#requisition statistics instead of repoeating the same code.
    @staticmethod
    def requisition_statistic(requisitions):
        total_submitted=len(requisitions) 
        total_approved=0
        total_pending=0
        total_not_approved=0

        for requisition in requisitions:
            if requisition.status=="Approved":
                total_approved+=1
            elif requisition.status=="Pending":
                total_pending+=1
            elif requisition.status=="Not approved":
                total_not_approved+=1
        return total_submitted,total_approved,total_pending,total_not_approved
        
    

requisitions=[]       

requisition1=Requisitionsystem()
requisition1.staff_info("03/04/2024","FN19","John Paul")
requisition1.requisitions_details([("Computer equipment",450)])
requisition1.requisition_approval()
requisitions.append(requisition1)

requisition2=Requisitionsystem()
requisition2.staff_info("05/04/2024","FN20","Tracy Brown")
requisition2.requisitions_details([("Computer equipment",1000)])
requisition2.requisition_approval()
requisitions.append(requisition2)

requisition3=Requisitionsystem()
requisition3.staff_info("07/05/2024","FN15","Emma Wellington")
requisition3.requisitions_details([("Computer equipment",3500)])
requisition3.requisition_approval()
requisitions.append(requisition3)

requisition4=Requisitionsystem()
requisition4.staff_info("03/05/2024","FN02","Catlin white")
requisition4.requisitions_details([("Computer equipment",490)])
requisition4.requisition_approval()
requisitions.append(requisition4)

requisition5=Requisitionsystem()
requisition5.staff_info("10/05/2024","FN10","David Smith")
requisition5.requisitions_details([("Computer equipment",750)])
requisition5.requisition_approval()
requisitions.append(requisition5)

print("BEFORE MANAGER RESPONSE")
print()
            
for requisition in requisitions:
    requisition.display_requisitions()


statistics=Requisitionsystem.requisition_statistic(requisitions)

requisition2.respond_requisition(" Approved")
requisition3.respond_requisition("Not approved")
requisition5.respond_requisition("Approved")
print()
print("AFTER MANAGER RESPONSE")
print()

for requisition in requisitions:
    requisition.display_requisitions()

statistics=Requisitionsystem.requisition_statistic(requisitions)
print(" Displaying the Requisition Statistics")
print("The total number of requisitions submitted :",statistics[0])
print(" The total number of  approved requisitions :",statistics[1])
print("The total number of pending requisitions:",statistics[2])
print(" The total number of  not approved requisitions:",statistics[3]) 