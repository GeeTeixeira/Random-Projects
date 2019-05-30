def generateTriangle(level):
  x = 0
  triangle = []
  while(x<=+1):
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

def printTriangle(triangle):
  temp = len(triangle)-1
  cnt = 0
  while(temp>=0 and cnt<len(triangle)):
    temp2 = temp
    while(temp2>=0):
      print("\t",end="")
      temp2-=1
    for x in triangle[cnt]:
      print(x,end="\t\t")
    print()
    temp-=1
    cnt+=1
 
level = int(input("Enter the level of the triangle:\n"))
triangle = generateTriangle(level)
printTriangle(triangle)
