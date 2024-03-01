# system_simulation/simulation.py
import random

class SystemSimulator:
    def __init__(self):
        self.current_speed = 0  # Current speed of the system
        self.inertia = 0.8  # Inertia factor (0-1, where 1 is high inertia)
        self.delay = 2  # Delay in time steps
        self.delay_buffer = []  # Buffer to simulate delay

    def simulate_system(self, input_value):
        """
        Simulate the response of the system to the input value.
        Includes inertia, delay, non-linearity, and noise.
        """
        # Simulate inertia
        self.current_speed = self.current_speed * self.inertia + input_value * (1 - self.inertia)

        # Simulate delay
        self.delay_buffer.append(self.current_speed)
        if len(self.delay_buffer) > self.delay:
            delayed_speed = self.delay_buffer.pop(0)
        else:
            delayed_speed = 0

        # Simulate non-linearity and noise
        non_linear_speed = delayed_speed ** 1.05
        noisy_speed = non_linear_speed + 0.1 * random.uniform(-1, 1)

        return noisy_speed
