from dateutil import parser


def exctractor(*, input_dict) -> dict:
    date = parser.parse(input_dict["dob"]["date"])
    new_dict = {"GENDER": input_dict["gender"],
                "FIRST_NAME": input_dict["name"]["first"],
                "LAST_NAME": input_dict["name"]["last"],
                "EMAIL": input_dict["email"],
                "AGE": input_dict["dob"]["age"],
                "BIRTHDAY": f"{date.day}-{date.month}-{date.year}",
                "NATIONALITY": input_dict["nat"],
                "LOGIN": input_dict["login"]["username"],
                "PASSWORD": input_dict["login"]["password"],
                "CITY": input_dict["location"]["city"],
                "STREET": input_dict["location"]["street"]["name"],
                "NUMBER": input_dict["location"]["street"]["number"],
                "COUNTRY": input_dict["location"]["country"]

                }
    return new_dict
