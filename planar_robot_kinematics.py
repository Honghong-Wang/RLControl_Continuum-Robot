import numpy as np
import matplotlib.pyplot as plt

# Planar Robot Kinematics Functions

# Homogeneous transformation matrix
def trans_mat_cc(kappa, s):
#Mapping from configuration parameters to task space
# tip frame is aligned so that the x-axis points toward the center of the
# circle
#
# INPUT:
# kappa: curvature
# l: trunk length
#
# OUTPUT:
# T: Transformation matrices containing orientation and position
    
    c_ks=np.cos(kappa*s);
    s_ks=np.sin(kappa*s);
    T = np.zeros((1,16));
    if kappa==0:
        T = np.array([c_ks,s_ks,0,0,-s_ks,c_ks,0,0,0,0,1,0,0,s,0,1]);  
    else:
        T = np.array([c_ks,s_ks,0,0,-s_ks,c_ks,0,0,0,0,1,0,(c_ks-1)/kappa,s_ks/kappa,0,1]);
        
    T = np.reshape(T,(4,4),order='F');
    return T


# The forward kinematics for an n section manipulator can then be generated by the product of 
# n matrices. The forward kinematics for our elephant trunk robot 
# with its n sections can be calculated as
def coupletransformations(T,T_tip):
    
#Find orientation and position of distal section
#(Multiply T of current section with T at tip of previous section)
#INPUT:
#T: Transformation matrices of current section
#T_tip: Transformation at tip of previous section
#OUTPUT:
#Tc: coupled Transformation matrix

    Tc = np.matmul(T_tip, T)
    
    return Tc


def trans_mat_cc_der(kappa, s):
# Derivative of the homogeneous transformation matrix to map
# from velocity of each joint to velocity of the tip of the continuum robot
#
# INPUT:
# kappa: curvature
# l: trunk length
#
# OUTPUT:
# T: Transformation matrices containing velocity of the tip of the robot
    
    c_ks=np.cos(kappa*s);
    s_ks=np.sin(kappa*s);
    T = np.zeros((1,16));
    T = np.array([c_ks,s_ks,0,0,
                  -s_ks,c_ks,0,0,
                   0,0,1,0,
                   ((1/(kappa**2))*(1-c_ks))-((s/kappa)*s_ks),
                   ((1/(kappa**2))*(-1*s_ks))+((s/kappa)*c_ks),0,0]);
        
    T = np.reshape(T,(4,4),order='F');
    return T

def jacobian_matrix(delta_kappa, kappa1, kappa2, kappa3, l1, l2, l3):
# Jacobian Matrix for J11 and J21 -> also add for J12, J13, J22, J23   
    T1_cc_1 = trans_mat_cc(kappa1+delta_kappa,l1);
    T2_1 = trans_mat_cc(kappa2, l2);
    T2_cc_1 = coupletransformations(T2_1,T1_cc_1);
    T3_1 = trans_mat_cc(kappa3, l3);
    T3_cc_1 = coupletransformations(T3_1,T2_cc_1);
    x1 = T3_cc_1[0,3]
    y1 = T3_cc_1[1,3]
    
    T1_cc_2 = trans_mat_cc(kappa1-delta_kappa,l1);
    T2_2 = trans_mat_cc(kappa2, l2);
    T2_cc_2 = coupletransformations(T2_2,T1_cc_2);
    T3_2 = trans_mat_cc(kappa3, l3);
    T3_cc_2 = coupletransformations(T3_2,T2_cc_2);
    x2 = T3_cc_2[0,3]
    y2 = T3_cc_2[1,3]
    
    
    J11 =  (x1 - x2) / (2*delta_kappa);
    J21 =  (y1 - y2)/ (2*delta_kappa);
    
    J = np.array([J11,J21]);
    J = np.reshape(J,(2,1))
    
    return J


# from configuration space (kappa, length) to task space (x,y)

# parameters
delta_kappa = 0.1;
kappa1 = 1.7035; # 1/m
l1 = 0.1000; # metre
kappa2 = 1.0000; # 1/m
l2 = 0.1000; # metre
kappa3 = 2.0000; # 1/m
l3 = 0.1000; # metre

    
# section 1
T1_cc = trans_mat_cc(kappa1,l1);

# section 2
T2 = trans_mat_cc(kappa2, l2);
T2_cc = coupletransformations(T2,T1_cc);

# section 3
T3 = trans_mat_cc(kappa3, l3);
T3_cc = coupletransformations(T3,T2_cc);

J = jacobian_matrix(delta_kappa, kappa1, kappa2, kappa3, l1, l2, l3)
print(J)

# Plot the trunk with three sections and point the section seperation
plt.scatter(0.000001,0,linewidths=5,color = 'black',label="Tip of each Section")
plt.scatter(T1_cc[0,3],T1_cc[1,3],linewidths=5,color = 'black')
plt.scatter(T2_cc[0,3],T2_cc[1,3],linewidths=5,color = 'black')
plt.scatter(T3_cc[0,3],T3_cc[1,3],linewidths=5,color = 'black')
plt.legend(loc="best")
plt.title("2D Continuum Robot")
plt.xlabel("X - Position")
plt.ylabel("Y - Position")
plt.show()