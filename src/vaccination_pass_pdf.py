import PyPDF2

class VaccinationPassPdf:
  """ Digital Vaccination Pass PDF """

  person_field_mappings = {
    'Nombres / First and Middle Name:': 'first_name',
    'Apellidos / Last Name:': 'last_name',
    'N° de Documento / Document ID:': 'national_identifier',
    'Fecha de Nacimiento / Date of Birth:': 'date_of_birth',
  }

  vaccine_field_mappings = {
    'Fecha de vacunación / Vaccination date:': 'vaccination_date',
    'Vacuna administrada / Vaccine product:': 'vaccine_product',
    'Vacunatorio / Vaccination center:': 'vaccination_center',
    'Lote o serie / Lot or series:': 'vaccine_series',
    'Laboratorio fabricante / Manufacturer:': 'vaccine_manufacturer'
  }

  vaccine_section_title = {
    '1° dosis': 1,
    '2° dosis': 2,
  }

  def __init__(self, path):
    self.path = path
    self.file_contents = ''
    self.has_opened_file = False
    self.fields = None

  def __open(self):
    """
      Opens the provided path and attempts to read the PDF file.

      If the provided path belongs to a PDF file, then it opens the
      file and retrieve its contents. Otherwise throws an error.
    """

    pdf_file = open(self.path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_page = pdf_reader.getPage(0)
    text = pdf_page.extractText()

    self.file_contents = text
    self.has_opened_file = True

    pdf_file.close()

  def __read(self):
    """
      Parse PDF file lines into a dictionary with the relevant fields
    """

    if self.has_opened_file == False:
      raise Exception('You must first execute "DigitalVaccinationPassPdf.open"')

    lines = self.file_contents.split('\n')
    vaccine_section_flag = None
    details = dict()
    details['vaccines'] = list()

    # Get rid of empty strings/lines
    lines = filter(lambda line: line != '', lines)
    lines = list(lines)

    # Retrieve tuples
    lines_iter = iter(lines)

    for line in lines_iter:
      if line in self.vaccine_section_title:
        vaccine_section_flag = self.vaccine_section_title[line]

      if line in self.person_field_mappings:
        details[self.person_field_mappings[line]] = next(lines_iter)

      if line in self.vaccine_field_mappings and vaccine_section_flag != None:
        if 'vaccines' in details:
          try:
            details['vaccines'][vaccine_section_flag - 1]
            details['vaccines'][vaccine_section_flag - 1][self.vaccine_field_mappings[line]] = next(lines_iter)
          except IndexError:
            vaccine = dict()
            vaccine[self.vaccine_field_mappings[line]] = next(lines_iter)
            details['vaccines'].append(vaccine)

    return details

  def details(self):
    self.__open()

    return self.__read()

if __name__ == '__main__':
  dvp_pdf = VaccinationPass('input.pdf')
  details = dvp_pdf.details()
