import numpy as np
from math import sin, cos
import math
import pandas as pd

np.set_printoptions(precision=3, suppress=True)
matrix = np.zeros((6, 6))
cubuk_sayisi = int(input("çubuk sayısı giriniz: "))

for i in range(cubuk_sayisi):
    

    E = int(input(""+str(i+1)+" nolu çubuğun elastisite modülünü giriniz: "))
    A = int(input(""+str(i+1)+" nolu çubuğun kesit alanını giriniz: "))
    L = int(input(""+str(i+1)+" nolu çubuk boyunu giriniz: "))
    degree = int(input(""+str(i+1)+" nolu çubuğun düzlem ile yaptığı açıyı giriniz: "))
    a = math.radians(degree)
    I = int(input(""+str(i+1)+" nolu çubuğun atalet momentini giriniz: "))

    matrix[0,0] = int((E*A/L)*(cos(a)**2)+ (12*E*I/(L**3))*(sin(a)**2))
    matrix[0,1] = int((E*A/L - 12*E*I/L**3)*cos(a)*sin(a))
    matrix[0,2] = int(-(6*E*I/(L**2))*(sin(a)))
    matrix[0,3] = -matrix[0,0]
    matrix[0,4] = -matrix[0,1]
    matrix[0,5] = matrix[0,2]
    matrix[1,0] = matrix[0,1]
    matrix[1,1] = int((E*A/L)*(sin(a)**2)+ (12*E*I/(L**3))*(cos(a)**2))
    matrix[1,2] = int((6*E*I/(L**2))*(cos(a)))
    matrix[1,3] = -matrix[1,0]
    matrix[1,4] = -matrix[1,1]
    matrix[1,5] = matrix[1,2]
    matrix[2,0] = matrix[0,2]
    matrix[2,1] = matrix[1,2]
    matrix[2,2] =int(4*E*I/L)
    matrix[2,3] = -matrix[2,0]
    matrix[2,4] = -matrix[2,1]
    matrix[2,5] = matrix[2,2]/2
    matrix[3,0] = -matrix[0,0]
    matrix[3,1] = -matrix[0,1]
    matrix[3,2] = -matrix[0,2]
    matrix[3,3] = matrix[0,0]
    matrix[3,4] = matrix[0,1]
    matrix[3,5] = -matrix[0,2]
    matrix[4,0] = -matrix[1,0]
    matrix[4,1] = -matrix[1,1]
    matrix[4,2] = -matrix[1,2]
    matrix[4,3] = matrix[1,0]
    matrix[4,4] = matrix[1,1]
    matrix[4,5] = -matrix[1,2]
    matrix[5,0] = matrix[2,0]
    matrix[5,1] = matrix[2,1]
    matrix[5,2] = matrix[2,2]/2
    matrix[5,3] = -matrix[2,0]
    matrix[5,4] = -matrix[2,1]
    matrix[5,5] = matrix[2,2]
    
    
    

    user_input = input(""+str(i+1)+" nolu çubuğun serbestlik numaralarını sırası ile giriniz: ")
    
    c = [int(i) for i in user_input.split(' ')]
    
    df = pd.DataFrame(matrix, columns=c, index=c)
    
    
 
    print(df)


serbest = int(input("serbestlik sayısını giriniz giriniz: "))


serbestlik_sayisi = list(range(1, serbest+1))

print(serbestlik_sayisi)

buyukS = np.zeros((serbest,serbest))
buyukS_matrisi = pd.DataFrame(buyukS, columns=serbestlik_sayisi, index=serbestlik_sayisi)

print(buyukS_matrisi)


"""m00 = (E*A/L)*(cos(a)**2)+ (12*E*I/(L**3))*(sin(a)**2)
m01 = (E*A/L - 12*E*I/L)*cos(a)*sin(a)
m02 = -(6*E*I/(L**2))*(sin(a))
m10 = m01
m11 = (E*A/L)*(sin(a)**2)+ (12*E*I/(L**3))*(cos(a)**2)
m12 = -(6*E*I/(L**2))*(cos(a))
m20 = m02
m21 = m12
m22 = matrix[0,2]"""





