def addnumbers(x, y):
    return x + y


class Leute:
    def __int__(self, name) -> None:
        super().__init__()
        self.name = name

    def __str__(self) -> str:
        return f"name:{self.name}"

def convert_gender(gender:str):
    gender = gender.upper()
    if gender == "M":
        return "Male"
    elif gender == "F":
        return "Female"
    else:
        return "Unknown_Gender"
