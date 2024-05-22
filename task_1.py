class House:
  def __init__(self):
    self.numberOfFloors = 10


def main():
  my_house = House()
  for i in range(1, my_house.numberOfFloors + 1):
    print(f'Текущий этаж равен {i}')


main()
