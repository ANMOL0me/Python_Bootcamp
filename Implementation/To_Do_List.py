
def show(task,priority,due,status): 
 if (priority=="+")
 print("Task\tPriority\tDue\tstatus") 
 print(f"{task}\t{priority}\t{due}\t{status}")
 
def add(task,priority,due,status):
 task = input("Enter the task")
 priority = input("enter priority with +")
 due = input("Enter the due date")
 Status = input("Status(y/n)")
 show(task,priority,due,status)



task = []
priority = []
due = []
status = []


print("Task\tPriority\tDue\tstatus")
while True:
 print("Select an option")
 print("1: Add\n2: Remove \n3: customize\n4: show\nsh5: Exit")
 usip = int(input("Enter a operation"))
 match usip:
  case 1:
   add(task,priority,due,status)
  case 2:
   remove()
  case 3:
   customize() 
  case 4:
   show()
  case 5:
   exit
  case _:
   print("Check input")
