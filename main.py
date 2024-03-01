# main.py

import matplotlib.pyplot as plt
from pid_controller.pid import PIDController

from system_simulation.simulation import SystemSimulator


def main():
    # PID parameters
    Kp, Ki, Kd = 0.25, 0.1, 0.15

    # Create a PID controller instance
    pid = PIDController(Kp, Ki, Kd)

    # Setpoint and initial measured value
    setpoint = 10
    measured_value = 0

    # Time-related variables
    dt = 0.1  # Time step
    current_time = 0
    end_time = 80  # Run for 80 seconds

    # Data for plotting
    times = []
    setpoints = []
    measured_values = []
    control_signals = []
    P_outputs = []
    I_outputs = []
    D_outputs = []

    system_simulator = SystemSimulator()

    while current_time <= end_time:
        control_signal, P_out, I_out, D_out = pid.update(setpoint, measured_value, dt)
        measured_value = system_simulator.simulate_system(control_signal)

        # Collect data for plotting
        times.append(current_time)
        setpoints.append(setpoint)
        measured_values.append(measured_value)
        control_signals.append(control_signal)
        # Collect data for PID components
        P_outputs.append(P_out)
        I_outputs.append(I_out)
        D_outputs.append(D_out)

        current_time += dt

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(times, setpoints, label='Setpoint', linestyle='--')
    plt.plot(times, measured_values, label='Measured Value')
    plt.plot(times, control_signals, label='Control Signal', alpha=0.7)
    plt.plot(times, P_outputs, label='P Output')
    plt.plot(times, I_outputs, label='I Output')
    plt.plot(times, D_outputs, label='D Output')
    # plt.ylim([0, 100])
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('PID Controller Performance')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
