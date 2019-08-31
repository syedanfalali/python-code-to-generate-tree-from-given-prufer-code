import numpy as npy

#take prufer code length as input
n=int(input("Enter length of prufer code:"))
#initialize graph to zeroes
graph=npy.zeros((n+2,n+2))
#initialize lists
prufer_list=[]
vertex_list=[]
#read prufer code elements
for i in range(n):
    prufer_list.append(int(input("Enter value  ")))
i=1
#create n+2 verices for n number of prufer code
for i in range(1,n+3):
    vertex_list.append(i)
#according to algorithm mapping elements
while(len(prufer_list)!=0):
    for i in range(1,len(vertex_list)+1):
        #if element present in prufer code ignore it
        if(i in prufer_list):
            print("i=",i)
            print(prufer_list)
            print(vertex_list)
            if(len(prufer_list)==0):
                break;
         #if element doesn't present in prufer code map it wth first element in prufer code
        else:
            graph[i-1,prufer_list[0]-1]=1;
            graph[prufer_list[0]-1,i-1]=1;
            print("i=",i)
            #remove mapped elements in both prufer code and vertices list
            prufer_list.pop(0);
            vertex_list.remove(i);
            print(prufer_list)
            print(vertex_list)
            if(len(prufer_list)==0):
                break;
 #map the remaining vertices in vertex list
if(len(vertex_list)!=1):
    print("reamaining vertices",vertex_list[0],vertex_list[1])
    graph[vertex_list[0]-1,vertex_list[1]-1]=1;
    graph[vertex_list[1]-1,vertex_list[0]-1]=1;
    vertex_list.pop(0);
print(vertex_list)
print(prufer_list);
print(graph);
    
