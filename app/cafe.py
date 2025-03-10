import datetime
from app.errors import (OutdatedVaccineError,
                        NotVaccinatedError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name : str) -> None:
        self.name = name

    def visit_cafe(self, visitor : dict) -> str | None:
        fail = 0
        if "vaccine" not in visitor:
            fail = 1
            raise NotVaccinatedError
        else:
            if "expiration_date" in visitor["vaccine"]:
                cond = (datetime.date.today()
                        > visitor["vaccine"]["expiration_date"])
                if cond:
                    fail = 1
                    raise OutdatedVaccineError

        if "wearing_a_mask" in visitor:
            if visitor["wearing_a_mask"] is False:
                fail = 1
                raise NotWearingMaskError
        else:
            raise NotWearingMaskError
        if fail == 0:
            return f"Welcome to {self.name}"
        else:
            return None
