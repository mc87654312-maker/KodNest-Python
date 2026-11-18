# Shallow copy it can access inner value by shared reference
import copy


original = [[1,2],[3,4]]

s_copy = copy.copy(original)

original[1][0] = 300

print(original)
print(s_copy)

# Deep copy

original = [[1,2],[3,4]]

s_copy = copy.deepcopy(original)

original[0][0] = 100

print(original)
print(s_copy)