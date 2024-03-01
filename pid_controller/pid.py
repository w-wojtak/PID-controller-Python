# pid_controller/pid.py

class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0

    def update(self, setpoint, measured_value, dt):
        error = setpoint - measured_value
        P_out = self.Kp * error
        self.integral += error * dt
        I_out = self.Ki * self.integral
        derivative = (error - self.prev_error) / dt
        D_out = self.Kd * derivative
        self.prev_error = error
        total_output = P_out + I_out + D_out

        return total_output, P_out, I_out, D_out

    def reset(self):
        self.prev_error = 0
        self.integral = 0
