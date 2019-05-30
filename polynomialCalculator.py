import math
class polynomial():
    def __init__(self, exp , deg):
        self.expression = exp
        self.degree = deg
        self.next = None
    def toString(self):
        print("("+self.expression+")^"+str(self.degree))
        
class polynomialLinkedList():
    def __init__(self):
        self.head = None
    def setNext(self,nextNode):
        if(self.head != None):
            holder = self.head
            while(holder.next != None):
                holder = holder.next
            holder.next = nextNode
        else:
            self.head = nextNode
    def toString(self):
        pointer = self.head
        while(pointer != None):
            print(pointer.expression+"^"+str(pointer.degree),end=" ")
            pointer = pointer.next

def generateTriangle(level):
  x = 0
  triangle = []
  while(x<=level+1):
    if(x==0):
      triangle.append([1])
      x+=1
    else:
      newTri = [1,1]
      triTemp = triangle[len(triangle)-1]
      y = len(triTemp)
      cnt = 0
      while(cnt<y-1):
        newVal = triTemp[cnt]+triTemp[cnt+1]
        newTri.insert(cnt+1,newVal)
        cnt+=1
      triangle.append(newTri)
    x+=1
  return triangle

def splitExp(exp):
    if("-" in exp):
        vals = exp.split("-")
    if("+" in exp):
        vals = exp.split("+")
    vals[0] = vals[0].lstrip()
    vals[0] = vals[0].rstrip()
    vals[1] = vals[1].lstrip()
    vals[1] = vals[1].rstrip()
    return vals

def findX(vals):
    if(vals[0] == "x"):
        return True
    return False

def polyCalc(poly):
    degree = poly.degree
    exp = poly.expression
    print(degree,exp)
    triangle = generateTriangle(degree) # create pascal's triangle
    vals = splitExp(exp) #split the expression into 2 terms x-2 into x,2
    
    boolean = findX(vals) #find if X is the first term
    print(boolean)
    
    leftDegree = degree
    rightDegree = 0
    intVal = 0

    listPol = polynomialLinkedList()
    while(leftDegree >= 0 and rightDegree <= degree):
        if(boolean):
            intVal = int(vals[1])**rightDegree
            print(vals[1],intVal)
            x = str(intVal)+vals[0]
            newPol = polynomial(x,leftDegree)
            listPol.setNext(newPol)
        else:
            intVal =int(vals[0])**leftDegree
            x = str(intVal)+"*"+vals[1]
            listPol.setNext(polynomial(x,rightDegree))
        leftDegree-=1
        rightDegree+=1
    return listPol
    
