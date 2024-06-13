import time

print("Progress: ", end="")
for i in range(10):
    print("\rProgress: {}%".format((i + 1) * 10), end="")
    time.sleep(1)

print("\nDone!")
