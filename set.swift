set1 = {10, 20, 30}
set2 = {20, 30, 40}

print("Set 1:", set1)
print("Set 2:", set2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

set1.add(50)
print("After adding element:", set1)

set1.remove(10)
print("After removing element:", set1)