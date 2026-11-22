import matplotlib.pyplot as plt

names = []
values = []

with open(r"C:\Users\Nazar\OneDrive\Desktop\areas.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            name, area = line.split(":")
            names.append(name.strip())
            values.append(int(area.strip()))

plt.barh(names, values, color="lightblue")
plt.xlabel("Площа, км²")
plt.ylabel("Області")
plt.title("Площі областей України")

plt.tight_layout()
plt.show()