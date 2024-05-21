class House:
  def __init__(self):
    self.numberOfFloors = 0
    print(f'Начальный этаж - {self.numberOfFloors}')

  def setNewNumberOfFloors(self, floors):
    self.numberOfFloors = floors
    print(f'Текущий этаж - {self.numberOfFloors}')


def main():
  my_house = House()
  my_house.setNewNumberOfFloors(10)


main()
