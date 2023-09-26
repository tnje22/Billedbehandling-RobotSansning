import math

kernel = [1, 1, 1]

kernel_size = len(kernel)
kernel_radius = math.floor(kernel_size/2)

input_signal = [1, 4, 7, 1, 1, 1, 4, 4, 1, 1]
output_signal = [0] * (len(input_signal) - 2*kernel_radius)

for x in range(len(output_signal)):
    total = 0
    for kernel_x, weight in enumerate(kernel):
        total += input_signal[x + kernel_x] * weight
    output_signal[x] = total/sum(kernel)

print(f"Input signal: {input_signal}")
print(f"Output signal: {output_signal}")
