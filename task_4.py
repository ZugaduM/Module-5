class Building:
  total = 0
  def __init__(self):
    Building.total += 1

i = 0
while i != 40:
  my_class = Building()
  i += 1
  

print(f'Total class instances: {Building.total}')
