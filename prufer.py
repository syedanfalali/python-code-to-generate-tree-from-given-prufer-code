import numpy as npy


n=int(input("Enter length of prufer code:"))
graph=npy.zeros((n+2,n+2))
prufer_list=[]
vertex_list=[]
for i in range(n):
    prufer_list.append(int(input("Enter value  ")))
i=1
for i in range(1,n+3):
    vertex_list.append(i)
print(vertex_list)
print(prufer_list);
while(len(prufer_list)!=0):
    for i in range(1,len(vertex_list)+1):
        if(i in prufer_list):
            print("i=",i)
            print(prufer_list)
            print(vertex_list)
            if(len(prufer_list)==0):
                break;
        else:
            graph[i-1,prufer_list[0]-1]=1;
            graph[prufer_list[0]-1,i-1]=1;
            print("i=",i)
            prufer_list.pop(0);
            vertex_list.remove(i);
            print(prufer_list)
            print(vertex_list)
            if(len(prufer_list)==0):
                break;
if(len(vertex_list)!=1):
    print("reamaining vertices",vertex_list[0],vertex_list[1])
    graph[vertex_list[0]-1,vertex_list[1]-1]=1;
    graph[vertex_list[1]-1,vertex_list[0]-1]=1;
    vertex_list.pop(0);
print(vertex_list)
print(prufer_list);
print(graph);
    
