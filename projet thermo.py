
def cp(T):
    
    return -0.00000018628*(T)**3 + 0.00045653*(T)**2 - 0.1361*(T) +1009


R= 1.03*(10**(-6))
A= 3.14*(3500)**2
def hr(T):
    return 4*0.05*5.67*10**(-8) * ((298+T)/2)**3

qm = 2*10**(5)
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

T=[298,298,298,298]

for i in range(0,10):

    Tasm= Text + (As-Ae)/(qm*cp(T[0])) * ((a+t)*phi+(hr(T[3])+hes)*(Text-(a*phi+(hes+hr(T[3]))*Text)/(hr(T[3])+hes+hcv)))

    Tasm = Tasm/ (1+ ((As-Ae)/(qm*cp(T[0])))*(hr(T[3])+hes)*hcv/(hr(T[3])+hes+hcv))

    Tpsm = Tasm + (As-Ae)/(As*hcs) * t*phi
    Tacm= (Text+Tasm*R*qm*cp(T[2]))/(1+R*qm*cp(T[2]))
    Tpvm= (a*phi+(hes+hr(T[3]))*Text+hcv*Tasm)/(hes+hr(T[3])+hcv)

    T =[Tasm,Tpsm,Tacm,Tpvm]

print("Tasm",Tasm-273,"°C")
print("Tpsm",Tpsm-273,"°C")
print("Tacm",Tacm-273,"°C")
print("Tpvm",Tpvm-273,"°C")



