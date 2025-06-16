class listOperations:
    def __init__(self, userList:list):
        print("list instance created")
        self.myNucList = userList
    
    def doSorting(self):
        print("do sorting")
        print("before:- ", self.myNucList)
        self.myNucList.sort()
        print("after:- ", self.myNucList)

    def doRemove(self, s:str):
        print("do remove:-" , s)
        self.myNucList.remove(s)        
        print("after:- ", self.myNucList)
    
    def doDelete(self):
        print("do delete")
        self.myNucList.clear
        print("after:- ", self.myNucList)

    def doPop(self):
        print("do pop")
        self.myNucList.pop(1) # delete  element at position 1 (which is second from left)
        print("after:- ", self.myNucList)
    

# main is not required. Python can find the entry point with intendentation level.
l1 = listOperations(['D', 'B', 'F', 'A', 'I', 'C', 'E', 'H', 'G'])
l1.doSorting()
l1.doRemove('E')
l1.doDelete()
l1.doPop()






    