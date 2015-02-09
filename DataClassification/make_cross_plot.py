# coding=windows-1250
from matplotlib.pyplot import bar, show, ylabel, xlabel, xticks, yticks, annotate, grid, ylim, title

__author__ = 'Agnieszka'
import numpy as np

a=open('workfile')

text=a.read()
list_with_lines= text.split('\n')
all_res=[]
for i in range(7,len(list_with_lines),9):
    print list_with_lines[i]
    all_res.append(float(list_with_lines[i].split('semi_vesicle ')[1]))
width = 0.8
x=np.arange(1,len(all_res)+1)
all_res=np.array(all_res)
all_res=all_res[all_res!=0]
x=x[all_res!=0]
print(all_res.mean(),all_res.std())
bar(x,all_res*100,width=width, color='0.50',)
ylim([0,100])
ylabel('Skutecznosć klasyfikatora [%]'.decode('windows-1250'))
xlabel('Numer Pacjenta')
#title('pęchrz'.decode('windows-1250'))

xticks(x+width/2,x)



grid(True)
show()