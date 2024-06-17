tasks = []

def addTask():
  task = input("ENTER A TASK: ")
  tasks.append(task)
  print(f"Task'{task}'added to the list")

def listTasks():
  if not tasks:
    print("NO TASKS CURRENTLY")
  else:
    print("Current Task")
    for index,task in enumerate(tasks):
      print(f"Task #{index}.{task}")

def deleteTask():
  listTasks()
  try:
    taskToDelete = int(input("ENTER THE #to delete:"))
    if taskToDelete >=0 and taskToDelete < len(tasks):
      tasks.pop(taskToDelete)
      print(f"Task {taskToDelete} deleted")
    else:
      print(f"task #{taskToDelete} not found")
  except:
    print("invalid input")

if __name__ == "__main__":
  print("WELCOME TO THE TO DO LIST)")
  while True:
    print("\n")
    print("SELECT AN OPTION")
    print("......")
    print("1.ADD TASK")
    print("2.DELETE TASK")
    print("3.LIST TASKS")
    print("4.QUIT")


    choice = input("ENTER YOUR CHOICE:")

    if(choice =="1"):
      addTask()
    elif(choice =="2"):
      deleteTask()
    elif(choice =="3"):
      listTasks()
    elif( choice =="4"):
      break
    else:
      print("Invalid input, Try again")
  print("BYE-BYEEe")   