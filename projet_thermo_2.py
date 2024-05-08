import matplotlib.pyplot as plt

def cp(T):
    
    return -0.00000018628*(T)**3 + 0.00045653*(T)**2 - 0.1361*(T) +1009


R= 1.03*(10**(-6))
A= 3.14*(3500)**2
def hr(T):
    return 4*0.05*5.67*10**(-8) * ((298+T)/2)**3

qm = 8*10**(5)
phi=600
a=0.05
t=0.85
Text= 298
hes=19
hec=40
hcv=11
hcs=10
hcc=12
As=3.14*(3500)**2
Ae=3.14*(101)**2
dr=50
ds=3500

Tas=[298]
Tps=[298+t*phi/hcs]
Tpv=[(a*phi+(hes+hr(299))*Text+hcv*Tas[0])/(hes+hcv+hr(299))]
print(Tpv)
r=3500
i=0
while r>20:

    k=2*r*3.14*dr/(qm*cp(Tas[i]))
    
    b=-Tas[i]*hcv + hes*t*phi/hcs +hcv*(a*phi+(hes+hr(Tpv[i]))*Text+hcv*Tas[i]) /(hes+hcv+hr(Tpv[i]))
    Tas.append(Tas[i]+k*b) 
    Tps.append(Tas[i+1]+t*phi/hcs)
    Tpv.append((a*phi+(hes+hr(Tpv[i]))*Text+hcv*Tas[i+1])/(hes+hcv+hr(Tpv[i])))
    r=r-dr
    i=i+1 




Tas= [i-273 for i in Tas]
Tps= [i-273 for i in Tps]
Tpv= [i-273 for i in Tpv]

I=[3500-i*dr for i in range(0,71)]
#peux tu adapter le code pour qu'il fasse l'affichage des 3 températures en fonction de la distance au centre de la serre

fig, ax = plt.subplots()
ax.plot(I, Tps)

ax.set_xlim(3500, 0)  
ax.set_xlabel('Distance au centre (m)')
ax.set_ylabel('Temperature (°C)')
ax.set_title("Température du sol en fonction de la distance au centre")

ax.grid(True)

plt.show()
