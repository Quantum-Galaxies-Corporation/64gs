from h5py import File
import numpy as np

def read_h5( iter, type , ham : int, ovFlag = False, level = 0):
    if type == 'c':
        x =  list(File(str(iter)+'/c.'+str(ham)+'.riz.'+str(2-ovFlag)+'.0_mac')['  0-0'])[0]
        l = int(np.sqrt(len(x)))
        return np.reshape(x,(l,l))
    else:
        def space(level):
            if level < 10:
                return '  '
            elif level < 100:
                return ' '
            else:
                return ''
                
        x =  list(File(str(iter)+'/e.kry.'+str(ham)+'.'+str(1)+'.0_mac')[space(level)+str(level)+'-0'])
        return np.array(x)

def get(v, indices):
    u = []
    for i in indices:
        u += [v[i]]
    return u
    
def get2(m,indices):
    u = []
    for i in indices:
        for j in indices:
                u += [m[i][j]]
    return np.reshape(u,(len(indices),len(indices)))

def retr(ham,v,indices):
    u = np.zeros(len(ham))
    for ii,i in enumerate(indices):
        u[i] = v[ii]
    return u
