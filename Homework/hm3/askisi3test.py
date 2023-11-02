
import matplotlib.pyplot as plt
g=9.8
def TDeriv(b,u,m):
    return (-b*u/m+g)

def Euler(V0, t0, t, dt, b, m):
    time     = t0        
    v        = V0            
    Velocity = []            
    Time     = []           
    while time < t:        
        Velocity.append(v)    
        Time.append(time)
        dudt = TDeriv(b,v,m)                   
        v = v + dudt * dt                  
        time = time + dt
    return Time, Velocity


x,y=Euler(0,0,0.1,0.001,0.1,0.01)
plt.plot(x,y)
plt.grid(True)
plt.show()
