from vaccine import Vaccine
from vaccination_pass_pdf import VaccinationPassPdf

class VaccinationPass:
  """ Digital Vaccination Pass representation """
  def __init__(self):
    self.first_name = None
    self.last_name = None
    self.national_identifier = None
    self.date_of_birth = None
    self.vaccines = []

  def from_pdf(self, path):
    pdf = VaccinationPassPdf(path)
    pdf = pdf.details()

    self.first_name = pdf['first_name']
    self.last_name = pdf['last_name']
    self.national_identifier = pdf['national_identifier']
    self.date_of_birth = pdf['date_of_birth']
    self.vaccines = pdf['vaccines']

  def __parse_vaccine(self, vaccine_dict) -> Vaccine:
    """ Creates a `Vaccine` instance from PDF `vaccines` dictionaries """
    vac = Vaccine(
      vaccine_dict['vaccine_manufacturer'],
      vaccine_dict['vaccination_date'],
      vaccine_dict['vaccine_product'],
      vaccine_dict['vaccination_center'],
      vaccine_dict['vaccine_series'],
    )

    return vac

  def __vaccines_list_str(self, vaccines_dictionaries) -> str:
    result = ''
    vaccines = map(self.__parse_vaccine, vaccines_dictionaries)

    for vacc in vaccines:
      result += str(vacc)

    return result

  def __str__(self) -> str:
    return f'''
      First Name: {self.first_name}
      Last Name: {self.last_name}
      National Identifier: {self.national_identifier}
      Date of Birth: {self.date_of_birth}

      Vaccines:
      {self.__vaccines_list_str(self.vaccines)}
    '''
