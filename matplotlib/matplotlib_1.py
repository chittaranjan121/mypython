'''import pandas
import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,3,5,7])
ypoints=np.array([2,4,5,7])
plt.plot(xpoints,ypoints,marker='o',ms=20,mec='r',mfc='yellow')
plt.show()
###linestyle , linecolor,line width
import pandas
import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([3,8,1,10])
plt.plot(xpoints,linestyle='dashed',color='green',linewidth=10.5)
plt.show()

###title
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
xpoints=np.array([1,3,4,6])
plt.title("My Plot")
plt.plot(xpoints,color='g',marker='o',ms='10',mfc='r')
plt.xlabel("zero points")
plt.ylabel("Value points")
plt.show()

####Font property
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
xpoint=np.array([1,3,4,6])
ypoint=np.array([3,5,7,9])

font1={'family':'serif','color':'r','size':10}
font2={'family':'serif','color':'y','size':10}
plt.title("My Plot",fontdict=font1)
plt.plot(xpoint,ypoint,marker='o',mfc='r',ms=10,mec='b')
plt.xlabel("my x label",fontdict=font1)
plt.ylabel("My Y Label",fontdict=font2)
plt.grid()
plt.show()

#####subplot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.plot(x,y,color='g')
plt.subplot(1,2,1)
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.plot(x,y,color='g')
plt.subplot(1,2,2)
plt.show()

###supertitle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=np.array([1,3,4,6])
plt.plot(x)
plt.title('My Plot')
plt.suptitle("My Super title")
plt.show()

###scatter Plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x,y,color='r')
plt.show()
###
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4])
y=np.array([10,20,30,40])
sizes=np.array([20,50,100,200])
plt.scatter(x,y,s=sizes,alpha=0.5)
plt.colorbar()
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x=np.random.randint(100,size=(100))
y=np.random.randint(100,size=(100))
colors=np.random.randint(100,size=(100))
sizes=10*np.random.randint(100,size=(100))
plt.scatter(x,y,c=colors,s=sizes,alpha=0.5,cmap='nipy-spectral')
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x=np.random.randint(100,size=(100))
y=np.random.randint(100,size=(100))
colors=np.random.randint(100,size=(100))
sizes=10*np.random.randint(100,size=(100))
plt.scatter(x,y,c=colors,s=sizes,alpha=0.5,cmap='nipy-spectral')
plt.show()

##Bars
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x=np.array(["a","b","c","d"])
y=np.array([3,8,1,10])
plt.title("my barchart")
#plt.bar(x,y)
plt.barh(x,y,color='cyan',height=0.5)
plt.show()

####histogram
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x=np.random.randint([80,10,250])
plt.hist(x,width=0.4)
plt.show()
'''
###pie chart
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x=np.array([35,25,25,15])
myexplode=[0.2,0,0,0]
label=(["apple","orange","banana","cocunut"])
plt.pie(x,labels=label,startangle=90,explode=myexplode,shadow=True)
plt.legend()
plt.show()