import numpy as np
from skimage import img_as_float
from skimage.io import imshow
import matplotlib.pyplot as plt
import random as rand


class cube:
    
    def __init__(self, n=3, test=False):
        self.n = n
        
        if not test:
	        self.F = np.ones((n,n))
	        self.L = np.ones((n,n)) * 2
	        self.B = np.ones((n,n)) * 3
	        self.R = np.ones((n,n)) * 4
	        self.U = np.ones((n,n)) * 5
	        self.D = np.ones((n,n)) * 6

        else:
        	values_n = self.n**2*6
        	values = np.array(range(0, values_n))
        	values = values / values_n

        	self.F = np.array(values[0:self.n**2].reshape((self.n, self.n)))
        	self.L = np.array(values[self.n**2:self.n**2*2].reshape((self.n, self.n)))
        	self.B = np.array(values[self.n**2*2:self.n**2*3].reshape((self.n, self.n)))
        	self.R = np.array(values[self.n**2*3:self.n**2*4].reshape((self.n, self.n)))
        	self.U = np.array(values[self.n**2*4:self.n**2*5].reshape((self.n, self.n)))
        	self.D = np.array(values[self.n**2*5:self.n**2*6].reshape((self.n, self.n)))


        
    def move_U(self):
        # rotation of the upper layer clocklwise
        temp = [np.copy(arr) for arr in [self.F[0], self.L[0], self.B[0], self.R[0]]]
        self.F[0] = temp.pop()
        self.R[0] = temp.pop()
        self.B[0] = temp.pop()
        self.L[0] = temp.pop()
        self.U = np.rot90(self.U, k=3)
        
    def move_UU(self):
        # rotation of the upper layer anticlockwise
        temp = [np.copy(arr) for arr in [self.F[0], self.L[0], self.B[0], self.R[0]]]
#         temp = [np.copy(self.F[0]), np.copy(self.L[0]), np.copy(self.B[0]), np.copy(self.R[0])]
        self.B[0] = temp.pop()
        self.L[0] = temp.pop()
        self.F[0] = temp.pop()
        self.R[0] = temp.pop()
        self.U = np.rot90(self.U)
        
    def move_D(self):
        # rotation of the lower layer clockwise (looking from it's side)
        temp = [np.copy(arr) for arr in [self.F[-1], self.L[-1], self.B[-1], self.R[-1]]]
        self.B[-1] = temp.pop()
        self.L[-1] = temp.pop()
        self.F[-1] = temp.pop()
        self.R[-1] = temp.pop()
        self.D = np.rot90(self.D, k=3)
                
    def move_DD(self):
        # rotation of the lower layer anticlockwise
        temp = [np.copy(arr) for arr in [self.F[-1], self.L[-1], self.B[-1], self.R[-1]]]
#         temp = [np.copy(self.F[-1]), np.copy(self.L[-1]), np.copy(self.B[-1]), np.copy(self.R[-1])]
        self.F[-1] = temp.pop()
        self.R[-1] = temp.pop()
        self.B[-1] = temp.pop()
        self.L[-1] = temp.pop()
        self.D = np.rot90(self.D)

    def move_L(self):
        # rotation of the left layer clockwise
        temp = [np.copy(arr) for arr in [self.F[:,0], self.D[:,0], self.B[:,-1][::-1], self.U[:,0]]]
        self.F[:,0] = temp.pop()
        self.U[:,0] = temp.pop()
        self.B[:,-1] = temp.pop()[::-1]
        self.D[:,0] = temp.pop()
        self.L = np.rot90(self.L)
        
    def move_LL(self):
        # rotation of the left layer anticlockwise
        temp = [np.copy(arr) for arr in [self.F[:,0], self.D[:,0], self.B[:,-1][::-1], self.U[:,0]]]
        self.B[:,-1] = temp.pop()[::-1]
        self.D[:,0] = temp.pop()
        self.F[:,0] = temp.pop()
        self.U[:,0] = temp.pop()
        self.L = np.rot90(self.L, k=3)
        
    def move_R(self):
        # rotation of the right layer clockwise
        temp = [np.copy(arr) for arr in [self.F[:,-1], self.D[:,-1], self.B[:,0][::-1], self.U[:,-1]]]
        self.B[:,0] = temp.pop()[::-1]
        self.D[:,-1] = temp.pop()
        self.F[:,-1] = temp.pop()
        self.U[:,-1] = temp.pop()
        self.L = np.rot90(self.L, k=3)
        
    def move_RR(self):
        # rotation of the right layer anticlockwise
        temp = [np.copy(arr) for arr in [self.F[:,-1], self.D[:,-1], self.B[:,-0][::-1], self.U[:,-1]]]
        self.F[:,-1] = temp.pop()
        self.U[:,-1] = temp.pop()
        self.B[:,0] = temp.pop()[::-1]
        self.D[:,-1] = temp.pop()
        self.L = np.rot90(self.L)
        
    def move_F(self):
        # rotation of the front layer clockwise
        temp = [np.copy(arr) for arr in [self.U[-1,:], self.R[0,:], self.D[0,:], self.L[:,-1]]]
        self.U[-1,:] = temp.pop()
        self.L[:,-1] = temp.pop()
        self.D[0,:] = temp.pop()
        self.R[:,0] = temp.pop()
        self.F = np.rot90(self.F)
        
    def move_FF(self):
        # rotation of the front layer anticlockwise
        temp = [np.copy(arr) for arr in [self.U[-1,:], self.R[0,:], self.D[0,:], self.L[:,-1]]]
        self.D[0,:] = temp.pop()
        self.R[:,0] = temp.pop()
        self.U[-1,:] = temp.pop()
        self.L[:,-1] = temp.pop()
        self.F = np.rot90(self.F, k=3)

    def move_B(self):
        #rotation of the back layer clockwise
        temp = [np.copy(arr) for arr in [self.U[0,:], self.R[-1,:], self.D[-1,:], self.L[:,0]]]	
        self.D[-1,:] = temp.pop()
        self.R[:,-1] = temp.pop()
        self.U[0,:] = temp.pop()
        self.L[:,0] = temp.pop()
        self.B = np.rot90(self.B, k=3)

    def move_BB(self):
        #rotation of the back layer anticlockwise
        temp = [np.copy(arr) for arr in [self.U[0,:], self.R[-1,:], self.D[-1,:], self.L[:,0]]]	
        self.U[0,:] = temp.pop()
        self.L[:,0] = temp.pop()
        self.D[-1,:] = temp.pop()
        self.R[:,-1] = temp.pop()
        self.B = np.rot90(self.B, k=3)
        
    def plot_horiz(self):
        
        img = np.zeros((self.n * 3, self.n * 4))
        img[self.n: self.n*2, 0:self.n] = self.L
        img[self.n: self.n*2, self.n: self.n*2] = self.F
        img[0:self.n, self.n: self.n*2] = self.U
        img[self.n: self.n*2, self.n*2:self.n*3] = self.R
        img[self.n*2: self.n*3, self.n: self.n*2] = self.D
        img[self.n: self.n*2, self.n*3: self.n*4] = self.B
        
        imshow(img)
        return img

    def plot_vert(self):
        
        img = np.zeros((self.n * 4, self.n * 3))
        img[self.n: self.n*2, 0:self.n] = self.L
        img[self.n: self.n*2, self.n: self.n*2] = self.F
        img[0:self.n, self.n: self.n*2] = self.U
        img[self.n: self.n*2, self.n*2:self.n*3] = self.R
        img[self.n*2: self.n*3, self.n: self.n*2] = self.D
        img[self.n*3: self.n*4, self.n: self.n*2] = np.rot90(self.B)
        
        imshow(img)
        return img

    def shuffle(self, k=100):
    	# shuffling the cube
	    moves = [self.move_D, self.move_DD, self.move_F, self.move_FF, self.move_U, self.move_UU,
	             self.move_L, self.move_LL, self.move_R, self.move_RR]
	    while  k > 0:
	    	rand.choice(moves)()
	    	k -= 1
	        
              
        