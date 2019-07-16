import numpy as np



 np.set_printoptions(suppress=True)
 path = "https://raw.githubusercontent.com/selva86/datasets/master/Auto.csv"
 data = np.genfromtxt(path,delimiter="," ,skip_header=1,dtype=object)
 data[:3]



a = np.zeros([4,4])

b = np.ones([4,4])


c = np.concatenate([a,b],axis = 0)
d = np.concatenate([a,b],axis = 1)


f =np.subtract(a,b)
def addition(a,b):
     print(np.add(a,b))

def subtration(a,b):
    print(np.add(a,b))

def Rconcat():
    np.concatenate([a,b],axis = 0)


 print arry by randon no..


arry = np.random.randint(1,4,size = [4,3])

w = np.sort(arry,axis =0)
q= np.sort(arry,axis =1)













