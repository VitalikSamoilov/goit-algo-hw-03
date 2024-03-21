import re
phone_number = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
normalize_phone = []
pettern = r"[^0-9]"
def cleaned_number(phone):
    return re.sub(pettern, "", phone)   
for phone in phone_number:
    normalized = cleaned_number(phone)
    if not normalized.startswith("+"):
        if normalized.startswith("38"):
            normalized = "+" + normalized
        else:
            normalized = "+38" + normalized
    normalize_phone.append(normalized)
print(normalize_phone)