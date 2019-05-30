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

def polyCalc(pTriangle):
