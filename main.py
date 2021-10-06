from matplotlib import pyplot as plt

fig, ax = plt.subplots()
ax.set_title("Gravity Simulation")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Distance (m)")

a = -10 # Rounded gravity from -9.8 m/s2
vi = float(input("Enter vi: ")) # Initial gravity
t = abs((0 - vi) / a) # Calcualte time it takes to get v = 0

if vi >= 0:
  # Distance when v = 0
  d = (vi*t) + (a/2 * t**2)
  print(f"At {t:.2f}s, v = 0.00, d = {d}")

  # Velocity when d = 0
  v = vi + (a*(t*2))
  print(f"At {t*2:.2f}s, v = {v}, d = 0.00")
t = float(input("Enter ending time: "))

dist = []
vel = []
acc = []

# Steps of tenths
g = round(t*10)
x = [i/10 for i in range(g+1)]
for t in x:
  # Calculate distance and velocity
  d = (vi*t) + (a/2 * t**2)
  vf = vi + (a*t)

  dist.append(d)
  vel.append(vf)
  acc.append(a)

# Print the end distance if you don't already know
if dist[-1] != 0:
  print(f"At {t:.2f}s, d = {dist[-1]}")

# Save and exit
ax.plot(x, dist, label=f"vi = {vi}m/s")
ax.legend()
fig.savefig("gravity.png")
print("Saved!")
