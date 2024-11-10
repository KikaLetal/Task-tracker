#importing packages 
import time
import json

#made class for tasks 
class task:
  def __init__(self, id, description):
    self.id = id
    self.description = description
    self.status = "To do"
    self.createdAt = time.strftime("%m-%d %H:%M", time.localtime())
    self.updateAt = time.strftime("%m-%d %H:%M", time.localtime())

#this is for debuging vvv
  def __str__(self):
    return f"id {self.id} description {self.description} status {self.status} created at {self.createdAt} last update at {self.updateAt}"
  
#--------------------------------------------------------------------------------------------------------------------------------  
#adding new tasks
def add(comma):
    
    with open('data.json', "r+") as file:
      data = json.load(file)
      #lambda just for id, it will one more than the previous one if JSON file is not empty and it will be 1 is there's no tasks in file
      #all below is a similar
      data.append((task((lambda x: x + 1)(data[-1]["id"]), comma).__dict__)) if data != [] else data.append((task((lambda x: x + 1)(0), comma).__dict__))
      if data[0]["id"] == 0: data.pop(0) 
    with open('data.json', "w") as file:
      json.dump(data, file)
      print(f"the task was successful add (Id: {data[-1]['id']})" + "\n")

    main()

#--------------------------------------------------------------------------------------------------------------------------------
#updating existing tasks
def update(value):
  id, UpdateTask = value.split(maxsplit=1)
  try:

    with open('data.json', "r+") as file:
      data = json.load(file)
      if data[0]["id"] == 0:
        print("todo list is empty")
        main()  
      data[int(id) - 1]["description"] = UpdateTask
      data[int(id) - 1]["updateAt"] = time.strftime("%m-%d %H:%M", time.localtime())

    with open('data.json', "w") as file:
      json.dump(data, file)    
      print(f"the task was successful update (Id: {data[-1]['id']})" + "\n")

    main()
  #exceptions if user write wrong id and the same for below functions
  except (IndexError, ValueError):
    print("invalid index")
    main()

#--------------------------------------------------------------------------------------------------------------------------------
#deleting tasks
def delete(id):
  try:

    if int(id) > 0:
      with open('data.json', "r+") as file:
        data = json.load(file)
        if data == [] or data[0]["id"] == 0:
          print("todo list is empty")
          main()  

        data.pop(int(id) - 1) 

        for i in range(int(id)-1, len(data)):
          data[i]["id"] = data[i]["id"] - 1

      with open('data.json', "w") as file:
        json.dump(data, file)
        print("the task was successful delete \n")


    main()
  except (IndexError, ValueError):
    print("invalid index")
    main()
    
#--------------------------------------------------------------------------------------------------------------------------------
#marking status in progress
def markinprogress(id):
  try:

    if int(id) > 0:
      with open('data.json', "r+") as file:
        data = json.load(file)
        if data == [] or data[0]["id"] == 0:
          print("todo list is empty")
          main()  

        data[int(id) - 1]["status"] = "In progress"
        data[int(id) - 1]["updateAt"] = time.strftime("%m-%d %H:%M", time.localtime())

      with open('data.json', "w") as file:
        json.dump(data, file)
        print("the mark was successful changed \n")

    main()
  except (IndexError, ValueError):
    print("invalid index")
    main()
  
#--------------------------------------------------------------------------------------------------------------------------------
#marking status done
def markdone(id):
  try:

    if int(id) > 0:
      with open('data.json', "r+") as file:
        data = json.load(file)
        if data == [] or data[0]["id"] == 0:
          print("todo list is empty")
          main()  

        data[int(id) - 1]["status"] = "Done"
        data[int(id) - 1]["updateAt"] = time.strftime("%m-%d %H:%M", time.localtime())

      with open('data.json', "w") as file:
        json.dump(data, file)
        print("the mark was successful changed \n")

    main()
  except (IndexError, ValueError):
    print("invalid index")
    main()
  
#--------------------------------------------------------------------------------------------------------------------------------
#marking status to do again if user missclicked before 
def marktodo(id):
  try:

    if int(id) > 0:
      with open('data.json', "r+") as file:
        data = json.load(file)
        if data == [] or data[0]["id"] == 0:
          print("todo list is empty")
          main()  

        data[int(id) - 1]["status"] = "To do"
        data[int(id) - 1]["updateAt"] = time.strftime("%m-%d %H:%M", time.localtime())

      with open('data.json', "w") as file:
        json.dump(data, file)
        print("the mark was successful changed \n")

    main()
  except (IndexError, ValueError):
    print("invalid index")
    main()
  
#--------------------------------------------------------------------------------------------------------------------------------
#just display tasks, mark is filter by status
def list(mark=0):
  #it's a kludge :), but for more beatiful and simple input!!! so you don't need to write "list To do"(with the capital letter in "To do") just "to do"
  #it's more quickly and comfortable
  if mark != None: mark = mark[0].upper() + mark[1:]
  with open('data.json', "r+") as file:
        data = json.load(file)
        for i in range(len(data)):
          #if mark is empty(user did'n write anything), we show every task 
          if mark == None: print(f'id: {data[i]["id"]} | description: {data[i]["description"]} | status: {data[i]["status"]} | created at: {data[i]["createdAt"]} | last update: {data[i]["updateAt"]}', '\n')
          else: 
            #else we check mark with task's status
            if data[i]["status"] == mark :
              print(f'id: {data[i]["id"]} | description: {data[i]["description"]} | status: {data[i]["status"]} | created at: {data[i]["createdAt"]} | last update: {data[i]["updateAt"]}', '\n')
  main()
#--------------------------------------------------------------------------------------------------------------------------------
#the programm manager
def main():
  try:
    #beauty input like in example, that's splition on finction part and value part
    command = input("write comma: ").split(maxsplit=1)
    #actually it's for the list function, because it could be called like just "list" without any parameters
    #so we checking how many parameters gives user and giving None, if no parameters was given
    if len(command) == 1:
      func = command[0]
      value = None
    else:
      func,value = command
    #searching the function that called by user
    globals()[func](value)
  except KeyError:
    print("invalid comma")
    main()

#--------------------------------------------------------------------------------------------------------------------------------
#initialization function, it needs for found JSON file and creating if it doesn't exist
def WakeUp():
  try:
    print("Trying to load file... \n")
    with open('data.json', "r") as file:
      file.close()
    print("successful.. \n")
    main()
  except FileNotFoundError:
    print("failed connection... \n")
    print("Creating file... \n")
    with open('data.json', "x") as file:
      json.dump([{"description": 'дел пока нет', "id": 0}], file)
      file.close()
    main()

WakeUp()
