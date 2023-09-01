import matplotlib.pyplot as plt
import numpy as np

def nsphere_volume(n, R):
    if n == 0:
        return 1
    numerator = ((np.pi)**2) * (R**n)
    gamma_function = 1
    for i in range (1, n):
        gamma_function *= i
    denominator = gamma_function * ((n/2)+1)
    return numerator/denominator

my_stuff = []
#highest = 0
count = 0

for i in range(0, 51):
    for j in range(100, 205, 5):
        a = (int(nsphere_volume(i, j/100) * 100))/100
        my_stuff.append([i, j/100, a])

    #count += 1
    #print(count)


print("hello1")
ax = plt.figure().add_subplot(projection='3d')

print("hello2")
plt.title("N Sphere Volume Plot")


for a in my_stuff:
    ax.scatter(a[0], a[1], a[2])

ax.set_xlim(0, 50)
ax.set_ylim(1, 2)
ax.set_zlim(0, 20)
ax.set_xlabel('n')
ax.set_ylabel('R')
ax.set_zlabel('Volume')

print("hello")

plt.savefig("test.png")


