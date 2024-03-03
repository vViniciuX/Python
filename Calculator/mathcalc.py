from dataclasses import dataclass, field


class Units:
  length_units = {
    'Ym': 1/10**24,
    'Zm': 1/10**19,
    'Em': 1/10**18,
    'Pm': 1/10**15,
    'Tm': 1/10**12,
    'Gm': 1/10**9,
    'Mm': 1/10**6,
    'km': 1/10**3,
    'hm': 1/10**2,
    'dam': 1/10,
    'm': 1,
    'dm': 10,
    'cm': 10**2,
    'mm': 10**3,
    'µm': 10**6,
    'nm': 10**9,
    'pm': 10**12,
    'fm': 10**15,
    'am': 10**18,
    'zm': 10**21,
    'ym': 10**24,
  }
  
  area_units = {
    'Ym^2': 1/1000**24,
    'Zm^2': 1/1000**19,
    'Em^2': 1/1000**18,
    'Pm^2': 1/1000**15,
    'Tm^2': 1/1000**12,
    'Gm^2': 1/1000**9,
    'Mm^2': 1/1000**6,
    'km^2': 1/1000**3,
    'hm^2': 1/1000**2,
    'dam^2': 1/1000,
    'm^2': 1,
    'dm^2': 1000,
    'cm^2': 1000**2,
    'mm^2': 1000**3,
    'um^2': 1000**6,
    'nm^2': 1000**9,
    'pm^2': 1000**12,
    'fm^2': 1000**15,
    'am^2': 1000**18,
    'zm^2': 1000**21,
    'ym^2': 1000**24,
  }
  
  volume_units = {
    'Ym^3': 1/1000**24,
    'Zm^3': 1/1000**19,
    'Em^3': 1/1000**18,
    'Pm^3': 1/1000**15,
    'Tm^3': 1/1000**12,
    'Gm^3': 1/1000**9,
    'Mm^3': 1/1000**6,
    'km^3': 1/1000**3,
    'hm^3': 1/1000**2,
    'dam^3': 1/1000,
    'L': 1/1000,
    'm^3': 1,
    'dm^3': 1000,
    'cm^3': 1000**2,
    'mm^3': 1000**3,
    'um^3': 1000**6,
    'nm^3': 1000**9,
    'pm^3': 1000**12,
    'fm^3': 1000**15,
    'am^3': 1000**18,
    'zm^3': 1000**21,
    'ym^3': 1000**24,
  }

@dataclass
class Squad(Units):
  height: int = 0
  width: int = 0
  area: int = 0
  height_unit: str = field(default='m')
  width_unit: str = field(default='m')
  area_unit: str = field(default='m')
  length_units = Units.length_units
  area_units = Units.area_units
  
  
  def __str__(self):
    if self.height and self.width:
      return f"Area: {(self.height*self.length_units.get(self.height_unit) * self.width*self.length_units.get(self.width_unit)) / self.area_units.get(self.area_unit)} {self.area_unit}^2"
    elif self.area and self.height:
      return f"Width: {(self.area*self.area_units.get(self.area_unit)*self.length_units.get(self.height_unit)) / self.height*self.length_units.get(self.height_unit) / self.area_units.get(self.area_unit)} {self.width_unit}"
    elif self.area and self.width:
      return f"Height: {((self.area*self.area_units.get(self.area_unit)*self.length_units.get(self.height_unit)) / self.width*self.length_units.get(self.width_unit)) / self.area_units.get(self.area_unit)} {self.height_unit}"

@dataclass
class Cube(Units):
  height: int = 0
  width: int = 0
  length: int = 0
  volume: int = 0
  height_unit: str = field(default='m')
  width_unit: str = field(default='m')
  length_unit: str = field(default='m')
  volume_unit: str = field(default='m')
  length_units = Units.length_units
  volume_units = Units.volume_units
  
  def __str__(self):
    if self.height and self.width and self.length:
      return f"Volume: {(self.height*self.length_units.get(self.height_unit) * self.width*self.length_units.get(self.width_unit) * self.length*self.length_units.get(self.length_unit)) / self.volume_units.get(self.volume_unit) } {self.volume_unit}"
    elif self.volume and self.height and self.length:
      return f"Width: {(self.volume / self.height*self.length_units.get(self.height_unit) / self.length*self.length_units.get(self.length_unit))/self.volume_units.get(self.volume_unit) } {self.width_unit}"
    elif self.volume and self.width and self.length:
      return f"Height: {(self.volume / self.width*self.length_units.get(self.width_unit) / self.length*self.length_units.get(self.length_unit))/self.volume_units.get(self.volume_unit) } {self.height_unit}"
    elif self.volume and self.height and self.width:
      return f"Length: {(self.volume / self.width*self.length_units.get(self.width_unit) / self.height*self.length_units.get(self.height_unit))/self.volume_units.get(self.volume_unit) } {self.length_unit}"

def main() -> None:
  print(Squad(area=2, width=2, height_unit='m', area_unit='m^2', width_unit='m'))
  print(Cube(volume=8, width=2, length=2))
  
if __name__=="__main__":
  main()