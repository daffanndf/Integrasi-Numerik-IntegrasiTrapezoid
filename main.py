import time
import numpy as np

def f(x):
    return 4 / (1 + x**2)

def trapezoidal_integration(f, a, b, N):
    h = (b - a) / N
    x = np.linspace(a, b, N+1)
    integral = (f(a) + f(b))/2
    integral += np.sum(f(x[1:-1]))
    integral *= h
    return integral

def calculate_pi(N_values):
    pi_reference = 3.14159265358979323846
    pi_estimates = []
    rms_errors = []
    execution_times = []

    for N in N_values:
        start_time = time.time()
        integral = trapezoidal_integration(f, 0, 1, N)
        pi_estimate = integral
        pi_estimates.append(pi_estimate)
        rms_error = np.sqrt(np.mean((pi_reference - pi_estimate)**2))
        rms_errors.append(rms_error)
        execution_time = time.time() - start_time
        execution_times.append(execution_time)

    return pi_estimates, rms_errors, execution_times

N_values = [10, 100, 1000, 10000]
pi_estimates, rms_errors, execution_times = calculate_pi(N_values)

print("N\tPi Estimate\t\tRMS Error\t\tExecution Time (s)")
print("-" * 60)
for i in range(len(N_values)):
    print(f"{N_values[i]}\t{pi_estimates[i]}\t{rms_errors[i]}\t{execution_times[i]}")
