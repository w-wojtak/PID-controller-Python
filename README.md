# PID controller in Python
Implementation of a simple PID controller in Python


A PID (Proportional-Integral-Derivative) controller is a control loop mechanism widely used in industrial control systems. It calculates an error value as the difference between a desired setpoint (SP) and a measured process variable (PV) and applies a correction based on proportional, integral, and derivative terms. 

- The **Proportional** component computes an output proportional to the error $P_{\text{out}} = K_p \times \text{Error}$, where  $K_p$ is the proportional gain and Error is $\text{SP} - \text{PV}$. 
- The **Integral** component sums the error over time and multiplies it by the integral gain $I_{\text{out}} = K_i \times \int \text{Error} \, dt$, with $K_i$ being the integral gain. This addresses any cumulative offset that the proportional component alone cannot eliminate.
- The **Derivative** component calculates the rate of change of the error, multiplying it by the derivative gain $D_{\text{out}} = K_d \times \frac{d(\text{Error})}{dt}$, where $K_d$ is the derivative gain. This anticipates future error and applies a corrective action beforehand, enhancing system stability and response time. 

The total output of the PID controller is the sum of these three components: $\text{Output} = P_{\text{out}} + I_{\text{out}} + D_{\text{out}} $.


![Figure_1](https://github.com/w-wojtak/PID-controller-Python/assets/19287772/b61c92b7-938f-4d89-a439-661c823f3b01)
