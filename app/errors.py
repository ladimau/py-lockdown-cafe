class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Should be vaccinated!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Vaccine outdated!"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "No mask!"
