import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as rect
import sys

class cell:
    def __init__(self,bleft,sides,angle):
        self.bleft=bleft #bottomleft
        self.sides=sides
        self.angle=angle

class ptree:
    def __init__(self,boundary,branch=None,gen=None):
        if branch is None:
            self.branch=[]
        else:
            self.branch=branch
        self.boundary=boundary
        if gen is None:
            self.gen=None
        else:
            self.gen=gen
    
    def grow(self,theta):
        if len(self.branch)>0:
            for i in range(2):
                self.branch[i].grow(theta)
        else:
        # definir cosas del cell
            lena=[ i*np.cos(theta) for i in self.boundary.sides ]
            lenb=[ i*np.sin(theta) for i in self.boundary.sides ]
            pax=self.boundary.bleft[0]-self.boundary.sides[1]*np.sin(self.boundary.angle)
            pay=self.boundary.bleft[1]+self.boundary.sides[1]*np.cos(self.boundary.angle)
            pbx=pax+lena[0]*np.cos(theta+self.boundary.angle)
            pby=pay+lena[0]*np.sin(theta+self.boundary.angle)
            anglea=self.boundary.angle + theta
            angleb=self.boundary.angle - (np.pi/2 - theta)
        # agregar los cell
            self.branch.append(ptree(cell([pax,pay],lena,anglea)))
            self.branch.append(ptree(cell([pbx,pby],lenb,angleb)))
            for i in range(2):
                self.branch[i].gen=self.gen+.15
        
    def plotree(self,ax):
        angler=np.rad2deg(self.boundary.angle)
        ax.add_patch(rect((self.boundary.bleft[0],self.boundary.bleft[1])
            ,self.boundary.sides[0],self.boundary.sides[1],angler,
            color=(1-1./self.gen**2,1-1./(self.gen+1)**2,1./(self.gen+1)**2,1./np.log(self.gen*np.e))))
        if len(self.branch)>0:
            for i in range(2):
                self.branch[i].plotree(ax)
            


n=int(sys.argv[1])
plt.figure()
plt.axis('off')
ax = plt.gca()
ax.set_xlim(-2.5,3.5)
ax.set_ylim(0,6)
#root=cell([0,0],[.08,.1],0)
root2=cell([.35,.27],[.07,.11],0)
root3=cell([-.35,.27],[.08,.12],0)
#tree=ptree(root,gen=1)
tree2=ptree(root2,gen=1)
tree3=ptree(root3,gen=1)
for i in range(n):
#    tree.grow(np.pi/4)
    tree2.grow(np.pi/(4-.8))
    #tree3.grow(np.pi/(4+1.1))
#tree.plotree(ax)
tree2.plotree(ax)
#tree3.plotree(ax)
plt.show()
#plt.savefig("tree.png", bbox_inches='tight')

