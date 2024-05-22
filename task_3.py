class Building:
  def __init__(self, number = 10, type = ''):
    self.numberOfFloors = number
    self.buildingType = type

  def __eq__(self, other):
    return (self.numberOfFloors == other.numberOfFloors) and (self.buildingType == other.buildingType)
      


my_building = Building(10, 'house')
othrer_building = Building(2, 'apartment')

if Building.__eq__(self=my_building, other=othrer_building):
    print( 'You are my neighbor!')
else:
    print('You leave in another place.')
  
