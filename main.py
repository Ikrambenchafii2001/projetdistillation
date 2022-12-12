import math

Pf = 100
F3  = 100
F1 = F2 = F4 = F5 = 0
Z1 = 0.3
Z2 = 0.3
Z3 = 0.4
V1 = 0
U1 = 50
U2 = U3 = U4 = U5 = 0
V2 = float(input("estimer V2"))
V3 = float(input("estimer V3"))
V4 = float(input("estimer V4"))
V5 = float(input("estimer V5"))
T1 = float(input("estimer T1"))
T2 = float(input("estimer T2"))
T3 = float(input("estimer T3"))
T4 = float(input("estimer T4"))
T5 = float(input("estimer T5"))
#Element 1:
#Calculer A1:
A12 = V2 - U1
A13 = V3 - U1
A14 = V4 + F3 - U1
A15 = V5 + F3 - U1
print("A12= ", A12)
print("A13= ", A13)
print("A14= ", A14)
print("A15= ", A15)
#Donnés:
A1=6.8196
B1=785
C1=247
#Calculer P1:
P11 = float((10 ** (A1 - (B1 / (C1 + (T1 - 32) * (5 / 9))))) / 51.715)
print("P11=", P11)
P12 = float((10 ** (A1 - (B1 / (C1 + (T2 - 32) * (5 / 9))))) / 51.715)
print("P31=", P12)
P13 = float((10 ** (A1 - (B1 / (C1 + (T3 - 32) * (5 / 9))))) / 51.715)
print("P13=", P13)
P14 = float((10 ** (A1 - (B1 / (C1 + (T4 - 32) * (5 / 9))))) / 51.715)
print("P14=", P14)
P15 = float((10 ** (A1 - (B1 / (C1 + (T5 - 32) * (5 / 9))))) / 51.715)
print("P15=", P15)
#Calculer K1:
K11 = P11 / Pf
print("K11=", K11)
K12 = P12 / Pf
print("K12=", K12)
K13 = P13 / Pf
print("K13=", K13)
K14 = P14 / Pf
print("K14=", K14)
K15 = P15 / Pf
print("K15=", K15)
#calculer B1:
B11 = -V2
B12 = U1 - V3 - V2*K12
B13 = U1 - V4 - F3 - V3*K13
B14 = U1 - V4 - F3 - V4*K14
B15 = U1 - F3 - V5*K15
print("B11= ", B11)
print("B12= ", B12)
print("B13= ", B13)
print("B14= ", B14)
print("B15= ", B15)
#calculer C1:
C11 = V2 * K12
C12 = V3 * K13
C13 = V4 * K14
C14 = V5 * K15
print("C11= ", C11)
print("C12= ", C12)
print("C13= ", C13)
print("C14= ", C14)
#Calculer D1:
D11 = D12 = D14 = D15 = 0
D13 = -F3 * Z1
print("D11= ", D11)
print("D12= ", D12)
print("D13= ", D13)
print("D14= ", D14)
print("D15= ", D15)
#Matrice 1:
import numpy as np
Z1=np.array([[B11, C11, 0, 0, 0],
            [A12, B12, C12, 0, 0],
            [0, A13, B13, C13, 0],
            [0, 0, A14, B14, C14],
            [0, 0, 0, A15, B15]],dtype=float)
print ("Z1= ", Z1)
Y1=np.array([0, 0, D13, 0, 0],dtype=float)
print ("Y1= ", Y1)
x1=np.linalg.solve(Z1, Y1)
print ("x1= ", x1)
#Element 2:
#Calculer A2:
A22 = V2 - U1
A23 = V3 - U1
A24 = V4 + F3 - U1
A25 = V5 + F3 - U1
print("A22= ", A22)
print("A23= ", A23)
print("A24= ", A24)
print("A25= ", A25)
#Données:
A2=6.78866
B2=899.617
C2=241.942
#calculer P2:
P21 = float((10 ** (A2 - (B2 / (C2 + (T1 - 32) * (5 / 9))))) / 51.715)
print("P21=", P21)
P22 = float((10 ** (A2 - (B2 / (C2 + (T2 - 32) * (5 / 9))))) / 51.715)
print("P22=", P22)
P23 = float((10 ** (A2 - (B2 / (C2 + (T3 - 32) * (5 / 9))))) / 51.715)
print("P23=", P23)
P24 = float((10 ** (A2 - (B2 / (C2 + (T4 - 32) * (5 / 9))))) / 51.715)
print("P24=", P24)
P25 = float((10** (A2 - (B2 / (C2 + (T5 - 32) * (5 / 9))))) / 51.715)
print("P25=", P25)
#calculer K2:
K21 = P21 / Pf
print("K21=", K21)
K22 = P22 / Pf
print("K22=", K22)
K23 = P23 / Pf
print("K23=", K23)
K24 = P24 / Pf
print("K24=", K24)
K25 = P25 / Pf
print("K25=",K25)
#Calculer B2:
B21 = -V2
B22 = U1 - V3 - V2*K22
B23 = U1 - V4 - F3 - V3*K23
B24 = U1 - V4 - F3 - V4*K24
B25 = U1 - F3 - V5*K25
print("B21= ", B21)
print("B22= ", B22)
print("B23= ", B23)
print("B24= ", B24)
print("B25= ", B25)
#Calculer C2:
C21 = V2 * K22
C22 = V3 * K23
C23 = V4 * K24
C24 = V5 * K25
print("C21= ", C21)
print("C22= ", C22)
print("C23= ", C23)
print("C24= ", C24)
#Calculer D2:
D21 = D22 = D24 = D25 = 0
D23 = -F3 * Z2
print("D21= ", D21)
print("D22= ", D22)
print("D23= ", D23)
print("D24= ", D24)
print("D25= ", D25)
import numpy as np
Z2=np.array([[B21, C21, 0, 0, 0],
            [A22, B22, C22, 0, 0],
            [0, A23, B23, C23, 0],
            [0, 0, A24, B24, C24],
            [0, 0, 0, A25, B25]],dtype=float)
print ("Z2= ", Z2)
Y2=np.array([0, 0, D23, 0, 0],dtype=float)
print ("Y2= ", Y2)
x2=np.linalg.solve(Z2, Y2)
print("x2= ", x2)
#Element 3:
#Calculer A3:
A32 = V2 - U1
A33 = V3 - U1
A34 = V4 + F3 - U1
A35 = V5 + F3 - U1
print("A32= ", A32)
print("A33= ", A33)
print("A34= ", A34)
print("A35= ", A35)
#Données:
A3=6.84471
B3=1060.733
C3=231.541
#calculer P3:
P31 = float((10 ** (A3 - (B3 / (C3 + (T1 - 32) * (5 / 9))))) / 51.715)
print("P31=", P31)
P32 = float((10 ** (A3 - (B3 / (C3 + (T2 - 32) * (5 / 9))))) / 51.715)
print("P32=", P32)
P33 = float((10 ** (A3 - (B3 / (C3 + (T3 - 32) * (5 / 9))))) / 51.715)
print("P33=", P33)
P34 = float((10 ** (A3 - (B3 / (C3 + (T4 - 32) * (5 / 9))))) / 51.715)
print("P34=", P34)
P35 = float((10 ** (A3 - (B3 / (C3 + (T5 - 32) * (5 / 9))))) / 51.715)
print("P25=", P35)
#calculer K3:
K31 = P31 / Pf
print("K31=", K31)
K32 = P32 / Pf
print("K32=", K32)
K33 = P33 / Pf
print("K33=", K33)
K34 = P34 / Pf
print("K34=", K34)
K35 = P35 / Pf
print("K35=",K35)
#Calculer B3:
B31 = -V2
B32 = U1 - V3 - V2*K32
B33 = U1 - V4 - F3 - V3*K33
B34 = U1 - V4 - F3 - V4*K34
B35 = U1 - F3 - V5*K35
print("B31= ", B31)
print("B32= ", B32)
print("B33= ", B33)
print("B34= ", B34)
print("B35= ", B35)
#Calculer C3:
C31 = V2 * K32
C32 = V3 * K33
C33 = V4 * K34
C34 = V5 * K35
print("C31= ", C31)
print("C32= ", C32)
print("C33= ", C33)
print("C34= ", C34)
#Calculer D3:
D31 = D32 = D34 = D35 = 0
D33 = -F3 * Z3
print("D31= ", D31)
print("D32= ", D32)
print("D33= ", D33)
print("D34= ", D34)
print("D35= ", D35)
import numpy as np
Z3=np.array([[B31, C31, 0, 0, 0],
            [A32, B32, C32, 0, 0],
            [0, A33, B33, C33, 0],
            [0, 0, A34, B34, C34],
            [0, 0, 0, A35, B35]],dtype=float)
print ("Z3= ", Z3)
Y3=np.array([0, 0, D33, 0, 0],dtype=float)
print ("Y3= ", Y3)
x3=np.linalg.solve(Z3, Y3)
print("x3= ", x3)
#Normalisation:
print("normalisation des x : ")
#élément 1:
som1 = x1[0] + x2[0] + x3[0]
print("somme1 = ", som1)
if som1 != 1 :
   X11 = x1[0] / (x1[0] + x2[0] + x3 [0])
   X21 = x2[0] / (x1[0] + x2[0] + x3 [0])
   X31 = x3[0] / (x1[0] + x2[0] + x3 [0])
   print("X11 = ", X11)
   print("X21 = ", X21)
   print("X31 = ", X31)
   S1 = X11 + X21 + X31
   print("la somme1 normalisé = ", S1)
#élément 2
som2 = x1 [1] + x2 [1] + x3 [1]
print("somme2 = ", som2)
if som2 != 1 :
   X12 = x1 [1] / (x1 [1] + x2 [1] + x3 [1])
   X22 = x2 [1] / (x1 [1] + x2 [1] + x3 [1])
   X32 = x3 [1] / (x1 [1] + x2 [1] + x3 [1])
   print("X12 = ", X12)
   print("X22 = ", X22)
   print("X32 = ", X32)
   S2 = X12 + X22 + X32
   print("la somme2 normalisé = ", S2)
   # élément 3
   som3 = x1[2] + x2[2] + x3[2]
   print("somme3 = ", som3)
   if som3 != 1:
       X13 = x1 [2] / (x1 [2] + x2 [2] + x3 [2])
       X23 = x2 [2] / (x1 [2] + x2 [2] + x3 [2])
       X33 = x3 [2] / (x1 [2] + x2 [2] + x3 [2])
       print("X13 = ", X13)
       print("X23 = ", X23)
       print("X33 = ", X33)
       S3 = X13 + X23 + X33
       print("la somme3 normalisé = ", S3)
   som4 = x1 [3] + x2 [3] + x3 [3]
   print("somme4 = ", som4)
   if som4 != 1:
       X14 = x1 [3] / (x1 [3] + x2 [3] + x3 [3])
       X24 = x2 [3] / (x1 [3] + x2 [3] + x3 [3])
       X34 = x3 [3] / (x1 [3] + x2 [3] + x3 [3])
       print("X14 = ", X14)
       print("X24 = ", X24)
       print("X34 = ", X34)
       S4 = X14 + X24 + X34
       print("la somme4 normalisé = ", S4)
   som5 = x1[4] + x2[4] + x3[4]
   print("somme5 = ", som5)
   if som5 != 1:
       X15 = x1 [4] / (x1 [4] + x2 [4] + x3 [4])
       X25 = x2 [4] / (x1 [4] + x2 [4] + x3 [4])
       X35 = x3 [4] / (x1 [4] + x2 [4] + x3 [4])
       print("X15 = ", X15)
       print("X25 = ", X25)
       print("X35 = ", X35)
       S5 = X15 + X25 + X35
       print("la somme5 normalisé = ", S5)

   from scipy.optimize import fsolve
   def func1(T):
       a = (X11 * ((10 ** (A1 - B1 / (C1 + (T - 32) * 5 / 9))) / 5171.5) + X21 * ((10 ** (A2 - B2 / (C2 + (T - 32) * 5 / 9))) / 5171.5) + X31 * ((10 ** (A3 - B3 / (C3 + (T - 32) * 5 / 9))) / 5171.5) -1)
       return a
   root = fsolve(func1, [1])
   print(root)
   from scipy.optimize import fsolve
   def func2(T):
       b = (X12 * ((10 ** (A2 - B2 / (C2 + (T - 32) * 5 / 9))) / 5171.5) + X22 * ((10 ** (A2 - B2 / (C2 + (T - 32) * 5 / 9))) / 5171.5) + X32 * ((10 ** (A3 - B3 / (C3 + (T - 32) * 5 / 9))) / 5171.5) - 1)
       return b
   root = fsolve(func2, [1])
   print(root)
   from scipy.optimize import fsolve
   def func3(T):
       c = (X13 * ((10 ** (A3 - B3 / (C3 + (T - 32) * 5 / 9))) / 5171.5) + X23 * ((10 ** (A2 - B2 / (C2 + (T - 32) * 5 / 9))) / 5171.5) + X33 * ((10 ** (A3 - B3 / (C3 + (T - 32) * 5 / 9))) / 5171.5) - 1)
       return c
   root = fsolve(func3, [1])
   print(root)
   from scipy.optimize import fsolve
   def func4(T):
       d = (X14 * ((10 ** (A3 - B3 / (C3 + (T - 32) * 5 / 9))) / 5171.5) + X24 * ((10 ** (A2 - B2 / (C2 + (T - 32) * 5 / 9))) / 5171.5) + X34 * ((10 ** (A3 - B3 / (C3 + (T - 32) * 5 / 9))) / 5171.5) - 1)
       return d
   root = fsolve(func4, [1])
   print(root)
   from scipy.optimize import fsolve
   def func5(T):
       e = (X15 * ((10 ** (A3 - B3 / (C3 + (T - 32) * 5 / 9))) / 5171.5) + X25 * ((10 ** (A2 - B2 / (C2 + (T - 32) * 5 / 9))) / 5171.5) + X35 * ((10 ** (A3 - B3 / (C3 + (T - 32) * 5 / 9))) / 5171.5) - 1)
       return e
   root = fsolve(func5, [1])
   print(root)
