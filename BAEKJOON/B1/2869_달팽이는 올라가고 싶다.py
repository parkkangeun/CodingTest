# 2024.10.02
# Python

import math
afternoon, night, height = map(int, input().split())
print(math.ceil((height - night) / (afternoon - night)))