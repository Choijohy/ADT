
def create(array):
    array= []
    return array

def insert(array,data):
    
    for i in range(len(data)):
        global selector
        if selector=="init":
            array.append(data[i][1])
        else:
            selIndex = array.index(selector)
            array.insert(selIndex+i+1,data[i][1])
        
        lastAddIndex = array.index(data[i][1])

    for i in range(len(array)):
        if i== lastAddIndex:
            selector=array[i]
            print('\033[1m'+selector+'\033[0m'+'\u0332' ,end=" ")
        else:
            print(array[i], end=" ")

def traverse_front(array,count):
    global commandType2
    global selector

    if commandType2 =="M":
        selector = array[count]
        move(int(command[1][1]))
    else:
        for i in range(len(array)):
            if i == count: 
                selector = array[i]
                print('\033[1m'+selector+'\033[0m'+'\u0332' ,end=" ")
            else:
                print(array[i],end=" ")

def traverse_rear(array,count):
    for i in range(len(array)):
        if i == len(array)-count-1:
            global selector 
            selector = array[i]
            print('\033[1m'+selector+'\033[0m'+'\u0332' ,end=" ")
        else:
            print(array[i],end=" ") 

def delete(array):
    global lastDel
    global selector
    if lastDel:
        del array[-1]
        selector = array[0]
        selIndex = 0
        lastDel = 0
    else:
        selIndex = array.index(selector)
        array.remove(selector)
    
    

    for i in range(len(array)):
        if selIndex == len(array):
            newIndex = selIndex-1
            if i == newIndex:
                selector = array[i]
                print('\033[1m'+selector+'\033[0m'+'\u0332' ,end=" ")
            else:
                print(array[i],end=" ")
        else:
            if i == selIndex:
                selector = array[i]
                print('\033[1m'+selector+'\033[0m'+'\u0332' ,end=" ")
            else:
                print(array[i],end=" ")

def get_data(array):
    global selector
    print("Return",selector)

def replace(array,new_data):
    global selector
    selIndex = array.index(selector)
    array[selIndex] = new_data
    for i in range(len(array)):
        if i== selIndex:
            selector=array[i]
            print('\033[1m'+selector+'\033[0m'+'\u0332' ,end=" ")
        else:
            print(array[i], end=" ")

def empty(array):
    global selector
    array =[]
    selector="init"
    return array

def move(new_position):
    # Revise array
    global selector
    selIndex = my_array.index(selector)
    if selIndex < new_position:
        moveItems = my_array[selIndex+1:new_position+1]
        my_array[selIndex:new_position]=moveItems
        my_array[new_position]=selector
        selIndex = my_array.index(selector)
    else:
        moveItems = my_array[new_position:selIndex]
        my_array[new_position+1:selIndex+1] = moveItems
        my_array[new_position]=selector
        selIndex = my_array.index(selector)

    # # Show array
    for i in range(len(my_array)):
        if i ==selIndex:
            print('\033[1m'+selector+'\033[0m'+'\u0332' ,end=" ")
        else:
            print(my_array[i],end=" ")
   
def data_count(array):
    global selector
    global temp
    selIndex = array.index(selector)
    if temp== str(len(my_array)-1):
        moveItems = array[selIndex+1:]
        array[selIndex:-1]=moveItems
        array[-1]=selector
        selIndex = array.index(selector)    
    elif temp =="P":
        if selIndex == 0:
            print("Nothing to change")
        else:
            array[selIndex] = array[selIndex-1]
            array[selIndex-1] = selector
            selIndex = array.index(selector)
    elif temp =="N":
        if selIndex == len(array)-1:
            print("Nothing to change")
        else:
            array[selIndex] = array[selIndex+1]
            array[selIndex+1] = selector
            selIndex = array.index(selector)

    for i in range(len(array)):
        if i == selIndex:
            print('\033[1m'+selector+'\033[0m'+'\u0332' ,end=" ")
        else:
            print(my_array[i],end=" ")

def show(array):
    global selector
    if selector=="init":
        print("none")
    else:
        selIndex = array.index(selector)
        for i in range(len(array)):
            if i == selIndex:
                print('\033[1m'+selector+'\033[0m'+'\u0332' ,end=" ")
            else:
                print(array[i],end=" ")


my_array = create("my_array")
selector = "init"
lastDel = 0

while 1:
    command = input("\n").split()
    print(command)
    commandType = command[0][0]
    if len(command)>=2:
        commandType2 = command[1][0]

    if commandType =="+":
        insert(my_array,command)
    if commandType =="-":
        delete(my_array)
    if commandType =="<":
        num = command.count("N")
        traverse_front(my_array,num)
            
    if commandType ==">":
        if commandType2 =="P":
            traverse_rear(my_array,(len(command)-1))
        if commandType2 =="-":
            lastDel= 1
            delete(my_array)

    if commandType == "@":
        get_data(my_array)

    if commandType =="=":
        replace(my_array,command[0][1])

    if commandType =="E":
        my_array=empty(my_array)

    if commandType =="M":
        temp = command[0][1]
        if temp== str(len(my_array)-1) or (temp == "P") or (temp == "N"):
            data_count(my_array)
        else:
            move(int(command[0][1]))
        
    if commandType =="L":
        show(my_array)

