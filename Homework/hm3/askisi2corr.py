#!/usr/bin/python3

'''
 Lusi tou provlimatos tou armonikou talantwti
 me tin methodo Euler. 
 
 Xreiazomaste ti thesi kai taxutita tou sustimatos
 kai epomenws exoume na lusoume 2 diaforikes eksiswseis
  a = du/dt 
  u = dx/dt 
 Kseroume oti i epitaxunsi tou sustimatos einai a = -w^2*x
 Epomenws ta vimata Euler einai:
 (1)    a = -w^2 * x         H epitaxunsi me basi ti thesi ti stigmi t_i
 (2)    x = x + u * dt       H thesi ti stigmi t_i+1 xrisimopoiontas tin u sti 
                             xroniki stigmi t_i
 (3)    u = u + a * dt       H taxytita ti stigmi t_i+1 xrisimopoiontas tin a
                             sti xroniki stimi t_i
 Simeiwste oti tha prepei na upologistei prwta i thesi kai 
 meta i taxutita giati diaforetika i nea taxytita tha xrisimopoieithei
 ston upologismo tis 
 Gia tin methodo tou Euler-Cromer exoume:
     a = g - u*b/m    H paragwgos ti stigmi t_i
     unew = u + a*dt  H taxitita ti stigmi t_(i+1)
     a = g - unew*b/m H epitaxunsi ti stigmi t_(i+1)
     u = u + a*dt     H taxytita ti stimi t_(i+1) meta apo vima Euler-Cromer 
                      opou xrisimopoioume tin paragwgo ti stigmi t_(i+1) gia 
                      na upologisoume tin xroniki ekseliksi tis taxytitas 

  To programma trexei gia:
  Arxiki thesi    : 1m
  Arxiki taxutita : 0m/s
  Mass            : 1 kg  (10gr)
  K               : 1  N/m
  tfin            : 2*T  opou T = 2pi/omega = 2pi
  ntsteps         : 1000 kai 10000 xronika vimata dt=T/ntsteps
 
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# H synartisis TheorSol douleuei toso me sugkekrimeni timi
# gia ti metavliti times oso kai me ti xrisi pinaka
def VTheorSol(time, omega, Ampl, phi):
    angle = omega*time + phi
    return -Ampl * omega * np.sin(angle)

def XTheorSol(time, omega, Ampl, phi): 
    angle = omega*time + phi
    return Ampl * np.cos(angle)

def D1x(omega,t,ux):  # H 1-i paragwgos tou x: dx/dt = ux
    return ux

def D2x(omega,t,x):  # H 2-i paragwgos tou x: d2x/t2 = ax = dux/dt
    return -(omega**2 * x)

def Euler(Der1x, Der2x, omega, Tinit, Vinit, Xinit, Tfinal, dt):
    time     = Tinit         # arxikos xronos
    v        = Vinit         # arxiki taxytita
    x        = Xinit         # arxiki thesi
    Xpos     = []            # Pinakas thesewn
    Vel      = []            # Pinakas taxytitwn 
    Time     = []            # Pinakas xronwn

    while time <= Tfinal:    # Loop ews otou o xronos ginei isos me 
                             # ton apaitoumeno xrono ekseliksis
        Vel.append(v)        # apothikeusi ti pliroforias se pinaka
        Time.append(time)
        Xpos.append(x)
#... Xrisimopoiontas tis sunartiseis twn paragwgwn apofeugoume to provlima
#... tis seiras efarmogis twn vimatwn Euler opws grafike sta eisagwgika sxolia
        dudt = Der2x(omega,time,x)    # i epitaxinsi ti stigmi t_i
        dxdt = Der1x(omega,time,v)    # i taxutitia  ti stigmi t_i
        v    = v + dudt * dt           # Vima Euler gia tin taxutita
        x    = x + dxdt * dt           # Vima Euler gia tin thesi 
        time = time + dt
    return Time, Xpos, Vel

#... Kurio programma
'''
K      = float(input("Specify the spring constant: "))
Mass   = float(input("Specify the mass of the object: "))
t0     = float(input("Specify the initial time [t0]: "))
v0     = float(input("Specify the initial velocity [v0]: "))
x0     = float(input("Specify the initial position [x0]: "))
nT     = int(input("Specify the final time [Number of Periods]: "))
nsteps = int(input("Specify the number of cases for the time step: "))
  Arxiki thesi    : 1m
  Arxiki taxutita : 0m/s
  Mass            : 1 kg  (10gr)
  K               : 1  N/m
  tfin            : 2*T  opou T = 2pi/omega = 2pi
  ntsteps         : 1000 kai 10000 xronika vimata dt=T/ntsteps
'''
K=1
Mass=1
t0=0
v0=0
x0=1
nT=2
nsteps=2




phi    = 0                      # Arxiki fasi
omega  = np.sqrt(Mass/K)
Period = 2*np.pi/omega          # Periodos
Tmax   = nT * Period            # Arithmos periodwn ws tmax
Ampl   = np.sqrt(v0**2/omega**2 + x0**2)   # Apo Emix = 0.5kA^2 =0.5mu^2+0.5kx^2


TheTime, TheVelocity, ThePosition = [],[],[]
labels,legends = [],[]

#... Gia tin askisi tha treksoume gia oliko xrono 2 periodwn
#... gia 1000 kai 10000 vimata kai tha eksetasoume tin periptwsi 
#... tis mias periodou pou zita sto (a) erwtima i askisi sta grafimata

for icase in range(nsteps):
    strng = 'Enter the Number of time stepa for %.d case ' % icase
    leg = input(strng)
    dt  = Period/int(leg)
    
    lbl = 'Euler - No. of steps ='+leg
    labels.append(lbl)              # Dimiourgia labels and legends
    legends.append(leg)              # for the plotting

#... Euler    
    Time, Velocity, Xposition = [],[],[]        # Orismos listas 
    Time, XPosition, Velocity= Euler(D1x,D2x,omega,t0,v0,x0,Tmax,dt)
    TheTime.append(Time)                        # Apothikeusi tis listas
    TheVelocity.append(Velocity)                # se lista me stoixeia listes
    ThePosition.append(XPosition)
    del Xposition
    del Time
    del Velocity

#... Plotting 

comm=['g:', 'r-.', 'b--', 'C1-','mv']
fig1 = plt.figure(figsize=(16,8))

#... Position
plt.subplot(2,2,1)
for ic in range(nsteps):
    tsteps = int(legends[ic])*nT   #Pol/smos me nT wste na diatireite o arithmos
                                   #twn vimatwn aneksartita tis periodou
    ncol = int(tsteps/2)
    t  = np.array(TheTime[ic])
    xp = np.array(ThePosition[ic])
    plt.plot(t[:ncol], xp[:ncol], comm[ic], label=labels[ic])
    if ic == 0:
        xth = XTheorSol(t, omega, Ampl, phi)
        plt.plot(t[:ncol],xth[:ncol],'k-',label=r'$Acos( \omega t + \phi)$')
        del xth
    del t
    del xp
#...
plt.title('Position')
plt.xlabel('Time (sec)')
plt.ylabel('Position, x($m$)')
plt.legend(loc='lower right')
plt.grid(True)
        
#... Velocity
plt.subplot(2,2,2)
for ic in range(nsteps):
    tsteps = int(legends[ic])*nT  
    ncol = int(tsteps/2)
    t  = np.array(TheTime[ic])
    v  = np.array(TheVelocity[ic])
    plt.plot(t[:ncol], v[:ncol], comm[ic], label = labels[ic])
    if ic == 0:
        vth = VTheorSol(t, omega, Ampl, phi)
        plt.plot(t[:ncol],vth[:ncol],'k-',
                 label=r'$ - \omega A sin( \omega t+ \phi)$')
        del vth
    del t
    del v
#...
plt.title('Velocity')
plt.xlabel('Time (sec)')
plt.ylabel('Velocity, v($m/s$)')
plt.legend(loc='upper left')
plt.grid(True)

#... Energy
encom=['r--','b--','k--','r-.','b-.','k-.']

plt.subplot(2,2,3)
EneDif=[]
for ic in range(nsteps):
    tsteps = int(legends[ic])*nT
    t  = np.array(TheTime[ic])
    v  = np.array(TheVelocity[ic])
    xp = np.array(ThePosition[ic])
    Uel  = 0.5*K*xp**2
    Ekin = 0.5*Mass*v**2
    Emix = Uel + Ekin
    label0 = r'$U_{{el}}$ - %d nsteps'%int(legends[ic])
    label1 = r'$E_{{kin}}$ -%d nsteps'%int(legends[ic])
    label2 = r'$E_{{mech}}$ - %d nsteps'%int(legends[ic])
    ncol = int(tsteps/2)  # Gia 1 periodo
    plt.plot(t[:ncol], Uel[:ncol], encom[ic+0],label=label0)
    plt.plot(t[:ncol], Ekin[:ncol],encom[ic+1],label=label1)
    plt.plot(t[:ncol], Emix[:ncol],encom[ic+2],label=label2)

    vth = VTheorSol(t, omega, Ampl, phi)
    xth = XTheorSol(t, omega, Ampl, phi)
    ThUel  = 0.5*K*xth**2
    ThEkin = 0.5*Mass*vth**2
    ThEmix = ThUel + ThEkin

    EneDif.append(np.abs(Emix - ThEmix))
    if ic == 0:
        plt.plot(t[:ncol], ThUel[:ncol],'r-',label=r'$U_{{el}^{th}}$')
        plt.plot(t[:ncol], ThEkin[:ncol],'b-',label='$E_{{kin}^{th}}$')
        plt.plot(t[:ncol], ThEmix[:ncol],'k-',label='$E_{{mech}^{th}}$')

    del vth
    del xth
    del t
    del v
    del xp
    del ThUel
    del ThEkin
    del ThEmix
    del Uel
    del Ekin
    del Emix
plt.title('Energy')
plt.xlabel('Time (sec)')
plt.ylabel('Energy, E($Joule$)')
plt.legend(loc='upper left')
plt.grid(True)
plt.title('Energy')
plt.xlabel('Time (sec)')
plt.ylabel('Energy, E($Joule$)')
plt.legend(loc='upper left')
plt.grid(True)

plt.subplot(2,2,4)
for ic in range(nsteps):
    tsteps = int(legends[ic])
    ncol = int(tsteps/2)
    t = np.array(TheTime[ic])
    plt.plot(t,EneDif[ic], comm[ic], label=labels[ic])
    del t
plt.title('$|E_{Euler} - E_{Theory}|$')
plt.xlabel('Time (sec)')
plt.ylabel('Difference, E(Joule)')
plt.legend(loc='upper left')
plt.grid(True)
#
plt.tight_layout()
#

fig2 = plt.figure(figsize=(6,6))
for ic in range(nsteps):
    t = np.array(TheTime[ic])
    v = np.array(TheVelocity[ic])
    x = np.array(ThePosition[ic])
    plt.plot(x,v,comm[ic],label=labels[ic])
    if ic == 1:
        vth = VTheorSol(t, omega, Ampl, phi)
        xth = XTheorSol(t, omega, Ampl, phi)
        plt.plot(xth,vth,'k-', label='Theory')
        del vth
        del xth
    del t
    del v
    del x
plt.title('Phase Diagram')
plt.xlabel('Position, x(m)')
plt.ylabel('Velocity, $v(m/s)$')
plt.legend(loc='upper left')
plt.text(-0.85,0.3,r'$E = \frac{1}{2} x^2+ \frac{1}{2}mv^2 \Rightarrow \frac{x^2}{2\frac{E}{k}} + \frac{v^2}{2\frac{E}{m}} = 1$')
plt.text(-0.85,0.15,r'When $k=m$, $R^2 = 2\frac{E}{k} = 2\frac{E}{m} \Rightarrow \frac{x^2}{R^2} + \frac{v^2}{R^2} = 1$ - circle')
plt.text(-0.85,0.0,r'When $k \neq m$, $a^2 = 2\frac{E}{k}$ and $b^2 = 2\frac{E}{m} \Rightarrow \frac{x^2}{a^2} + \frac{v^2}{b^2} = 1$ - ellipse')
plt.grid(True)

    
pp=PdfPages('hm03_prob02.pdf')
pp.savefig(fig1)
pp.savefig(fig2)
pp.close()
#
plt.show()
    
