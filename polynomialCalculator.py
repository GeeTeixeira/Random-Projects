class polynomial:
    self.expression = None
    self.degree = 0
    def __init__(self, exp , deg):
        self.expression = exp
        self.degree = deg
    def toString(self):
        print(self.expression+"^"+self.degree)
class polynomialLinkedList:
    self.head = None
    self.next = None
    def __init__(self,exp):
        self.head = exp
    def setNext(self,nextNode):
        self.next = nextNode
    def toString(self):
        pointer = self.head
        while(pointer != None):
            print(pointer.toString())
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

def polyCalc(pTriangle, expression):
    degree = expression.degree
    exp = expression.expression
    triangle = generateTriangle(degree) # create pascal's triangle
    vals = splitExp(exp) #split the expression into 2 terms x-2 into x,2
    boolean = findX(vals) #find if X is the first term 
    xDegree = degree
    intDegree = 0
    intVal = 0
    while(xDegree >= 0 and intDegree >= degree):
        
    
