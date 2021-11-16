import vaccination_pass

if __name__ == '__main__':
  vp = vaccination_pass.VaccinationPass()
  vp.from_pdf('input.pdf')

  print(vp)
