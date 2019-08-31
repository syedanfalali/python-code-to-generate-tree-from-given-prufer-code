# prufercode-to-tree
    From this code we can convert a prufer sequence into tree in form of matrix.
initially give input as length of required prufer sequence then after enter 
each vertex elements in the prufer sequence in order.
    It will generate prufer list and vertex list at every iterarion clearly step
by step.Finally desired tree is generated in matrix form.

Let us understand algorithm to construct tree with an example:

Input : (4, 1, 3, 4)

Step 1: First we create an empty graph of 6 vertices and get 4 from the sequence. 

Step 2: Out of 1 to 6, the least vertex not in Prufer sequence is 2. 

Step 3: We form an edge between 2 and 4. 

             2----4    1    3    5      6
Step 4: Next in the sequence is 1 and corresponding 
        vertex with least degree is 5 (as 2 has been 
        considered). 
        
             2----4    1----5    3    6
             
Step 5: Next in the sequence is 3 and corresponding 
        vertex with least degree is 1 
        (as 1 is now not part of remaining Prufer sequence) 
        
             2----4    3----1----5    6
             
Step 6: Next in the sequence is 4 and corresponding vertex
        with least degree is 3 (as 3 has not been considered 
        as is not present further in sequence)
        
             2----4----3----1----5    6
             
Step 7: Finally two vertices are left out from 1 to 6 (4
         and 6) so we join them.
         
             2----4----3----1----5
                  |
                  6
                  
This is the required tree on 6 vertices.
