class Vaccine:
  """ Digital Vaccination Pass representation """
  def __init__(self, vaccine_manufacturer, vaccination_date, product, center, lot_or_series):
    self.vaccine_manufacturer = vaccine_manufacturer
    self.vaccination_date = vaccination_date
    self.product = product
    self.center = center
    self.lot_or_series = lot_or_series

  def __str__(self) -> str:
      return f'''
      Manufacturer: {self.vaccine_manufacturer}
      Vaccination date: {self.vaccination_date}
      Name: {self.product}
      Center: {self.center}
      Lot or series: {self.lot_or_series}
      '''
