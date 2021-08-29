

class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class ListNode:
    def __init__(self):
        self.head = None
        self.count = 0

    def addTail(self,data): # append new node
        cur = self.head
        global selector
        if cur == None:
            self.head = Node(data)
            selector = self.head
        
        else:
            while cur.next != None:
                cur= cur.next
            cur.next = Node(data)
            selector = cur.next

      
    def get_item(self, index): # get node by index
        cnt = 0
        cur = self.head
        while cnt < index:
            cnt += 1
            cur = cur.next
        return cur

    def add(self,N,data): # insert new node
        
        if N > 0:
            cur = self.get_item(N-1)
            temp = cur.next
            for i in range(len(data)): # link to forward nodes
                cur.next = Node(data[i])
                cur = cur.next 
        else: # insert first(change self.head)
            temp = self.head
            self.head = Node(data[0])
            cur = self.head
            for i in range(1,len(data)):
                cur.next = Node(data[i])
                cur = cur.next

        cur.next = temp # link to rest behind   
        
        global selector
        selector = cur

    def printAll(self):
        cur = self.head
        while cur != None:
            if cur == selector:  
                print('\033[1m'+cur.val+'\033[0m'+'\u0332' ,end=" ")
            else:
                print(cur.val,end=" ")
            cur = cur.next
    
    def get_data(self):
        print(selector.val)
        # print(selector.val+" (",end=" ")
        # self.printAll()
        # print(")")

    def traverse_front(self,count):
        global selector
        temp = selector
        selector = self.head
        for i in range(count):
            if selector.next != None:
                selector = selector.next
            else:
                selector = temp
                print("Error : element doesn't exist")


    def traverse_rear(self,count):
        self.data_count()
        if self.head == None:
            print("It's empty list. Add tail")
        else:
            Idx = self.count -1 -count
            global selector
            selector = self.get_item(Idx)

            # cur = self.head
            # for i in range(self.count -1 -count):
            #     cur = cur.next
            # global selector
            # selector = cur

    def delete(self): 
        global selector
        cur = self.head
        if cur == selector:
            self.head = cur.next
            selector = cur.next
            return

        while cur.next != selector:
            cur = cur.next
        cur.next = selector.next
        if selector.next != None:
            selector = selector.next
        else: # delete last one
            selector = self.head

    def data_count(self):
        cur = self.head
        self.count = 0 
        while cur != None:
            self.count +=1
            cur = cur.next

    def is_empty(self):
        if self.head == None:
            return "True"
        else:
            return "False"

    def get_index(self,data):
        cur = self.head
        self.count = 0 
        
        while cur.val != data:
            self.count +=1
            cur = cur.next
        global selector
        selector = cur
        return self.count

    def replace(self,new_data):
        global selector
        selector.val = new_data
        
    def clear(self):
        self.head = None



def create(list):
    list = ListNode()
    return list


def main(): 
    cmd = input("\n").split() # 명령 분할
    cmdType = cmd[0][0] 
    num = len(cmd)
    

    if cmdType =="+":
        if my_list.is_empty() == "True":
            for i in range(num):
                my_list.addTail(cmd[i][1])
        else:
            new_nodes = []
            for i in range(num):
                new_nodes.append(cmd[i][1])
            my_list.add(my_list.get_index(selector.val)+1,new_nodes)
        my_list.printAll()
            

    elif cmdType =="L":
        my_list.printAll()

    elif cmdType =="G":
        my_list.get_data()

    elif cmdType == "<":  
        my_list.traverse_front(cmd.count("N"))
        
        if (num> 1) and (cmd[1][0] == "+"):
            new_nodes = []
            for i in range(1,num):
                new_nodes.append(cmd[i][1])
            my_list.add(0,new_nodes)

        my_list.printAll()

    elif cmdType == ">":
        my_list.traverse_rear(cmd.count("A"))
        if cmd[-1] == "-":
            my_list.delete()
            my_list.printAll()

    elif cmdType == "-":
        my_list.delete()
        my_list.printAll()

    elif cmdType == "#":
        my_list.data_count()
        print(my_list.count)
    
    elif cmdType == "E":
        print(my_list.is_empty())

    elif cmdType == "?":
        Idx = my_list.get_index(cmd[0][1])+1
        print(Idx,end="")
        print(":",end=" ")
        my_list.printAll()

    elif cmdType == "=":
        my_list.replace(cmd[0][1])
        my_list.printAll()
        
    elif cmdType == "C":
        my_list.clear()
    
    elif cmdType.isnumeric():
        print(cmd[0][0])
        my_list.traverse_front(int(cmdType)-1)
        if cmd[0][1] == "G":
            my_list.get_data()
        
        elif cmd[0][1] == "=":
            my_list.replace(cmd[0][2])


list_name = "my_list"
my_list = create(list_name)
selector = "None"

while __name__ == "__main__":
    main()