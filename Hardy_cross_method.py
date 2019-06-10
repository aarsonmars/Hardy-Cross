import matplotlib.pyplot as plt
import numpy as np

def draw_network(x,y,x1,y1,q):
    
    
    fig=plt.figure(figsize=(10,7))
    ax = fig.add_subplot()
    plt.plot(x,y,label='single pipe')
    plt.plot(x1,y1,label='common pipe')
    ax.text(-0.2,2,'A',fontsize=17)
    ax.text(2,-0.4,'C',fontsize=17)
    ax.text(4.2,2,'D',fontsize=17)
    ax.text(1.9,4.2,'B',fontsize=17)
    
    plt.text(0.5,2.7, '$Q_1=$'+str(q[0]), fontsize=16,rotation=30, rotation_mode='anchor')
    plt.text(2.5,3.7, '$Q_2=$'+str(q[1]), fontsize=16,rotation=330, rotation_mode='anchor')
    plt.text(2.7,0.2, '$Q_3=$'+str(q[2]), fontsize=16,rotation=33, rotation_mode='anchor')
    plt.text(0.5,1.1, '$Q_4=$'+str(q[3]), fontsize=16,rotation=325, rotation_mode='anchor')
    plt.text(1.9,1.2, '$Q_5=$'+str(q[4]), fontsize=16,rotation=90, rotation_mode='anchor')
    plt.legend(loc='best')
    plt.axis('off')
    plt.show()
    
np.r1=[1,3,2]
np.r2=[2,1,3]
value_of_r1=3
np.discharge_at_node= [100,-25,-75,0]
a= np.discharge_at_node[0]/2
c1=(a+np.discharge_at_node[1])/2
d=-a   
c2=-c1
b=c1
e=-(c1-d+np.discharge_at_node[3])
np.flow_rate_in_pipe2=[b,e,c2]

np.flow_rate_in_pipe1=[60,15,-40]
np.flow_rate_in_pipe2=[20,-55,-15]
for i in range(1,3):
    
    np.head_lossx=np.multiply(np.r1,np.flow_rate_in_pipe1)
    np.head_loss1=np.multiply(np.head_lossx,np.flow_rate_in_pipe1)
    
    np.ratio1= np.divide(np.head_loss1,np.flow_rate_in_pipe1)
    np.ratio1=np.absolute(np.ratio1)
    for ii in range(3):
        if np.flow_rate_in_pipe1[ii]<0:
            np.head_loss1[ii]=-np.head_loss1[ii]
     
    np.head_lossx=np.multiply(np.r2,np.flow_rate_in_pipe2)
    np.head_loss2=np.multiply(np.head_lossx,np.flow_rate_in_pipe2)
    np.ratio2= np.divide(np.head_loss2,np.flow_rate_in_pipe2)
    np.ratio2=np.absolute(np.ratio2)    
    for ii in range(3):
        if np.flow_rate_in_pipe2[ii]<0:
            np.head_loss2[ii]=-np.head_loss2[ii]
    dis1=np.sum(np.head_loss1)
    dis2=np.sum(np.head_loss2)
    
    
    correction_factor1=-(dis1/(2*np.sum(np.ratio1)))
    correction_factor2=-(dis2/(2*np.sum(np.ratio2)))
    np.flow_rate_in_pipe1=np.flow_rate_in_pipe1+correction_factor1
    np.flow_rate_in_pipe2=np.flow_rate_in_pipe2+correction_factor2

    np.flow_rate_in_pipe1[1]=np.flow_rate_in_pipe1[0]+np.discharge_at_node[1]-np.flow_rate_in_pipe2[0]
    np.flow_rate_in_pipe2[2]=-np.flow_rate_in_pipe1[1]
    
    np.q=[np.flow_rate_in_pipe1[0],np.flow_rate_in_pipe2[1],np.flow_rate_in_pipe2[0],np.flow_rate_in_pipe1[2],np.flow_rate_in_pipe1[1]]
    np.q=np.around(np.q,decimals=3)
    
    draw_network([0,2,4,2,0],[2,0,2,4,2],[2,2],[0,4],np.q)
    
     
print(np.flow_rate_in_pipe1)
print(np.flow_rate_in_pipe2)    

