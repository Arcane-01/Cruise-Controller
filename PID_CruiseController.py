
import numpy as np
import matplotlib.pyplot as plt


m = 1000                    #Mass of car
b = 25                      #drag coefficient
time = np.arange(50)        #time array
t = 0                       #current time
r = 60                      #reference velocity
v = 0                       #Current velocity
v_arr = []                  #velocity array

kp = 213                    #Parameters
kd = 0
ki = 5

r_arr = []                  #reference array
for i in range((len(time))):
    r_arr.append(r)
# print(r_arr)

old_e = 0                   #Error terms
E = 0
e_arr = []                  #error array


while t!= len(time):        #the cruise control
    e = r - v
    e_arr.append(e)
    e_dot = e - old_e
    E = E + e
    u = (kp*e) + (kd*e_dot) + (ki*E)
    old_e = e
    v = (m*v + u - b*v)/(m)
    v_arr.append(v)
    t += 1
# print(v_arr)              #54 in 10s desired and maximum overshoot of 3
# print(e_arr)

rise_time= 0
v_at_rise_t = r * ((90)/100)
rise_t_arr = []
for i in range(len(v_arr)):
    if v_arr[i] >= v_at_rise_t:
        rise_time = i
        break
print("Rise time =",rise_time,'secs')
for i in range((len(time))):
    rise_t_arr.append(v_at_rise_t)
# print(rise_t_arr)


max_overshoot = r * (5/100)  #allowed overshoot is 5% of steady state
overshoot = False
print("maximum overshoot =",max_overshoot)
for i in range(len(e_arr)):
    if e_arr[i] < -(max_overshoot):
        overshoot = True
        break
# print(e_arr)
print("overshoot = ", overshoot)

plt.plot(time,v_arr , label = 'velocity')
plt.plot(r_arr, label = "reference velocity")
plt.plot(time,rise_t_arr,'--', label = '90% of velocity at steady state')
plt.plot()
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.legend()
plt.show()







