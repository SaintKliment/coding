codecs = ["cp1252", "cp437", "utf-8"]

for codec in codecs:
    with open("simple_text.txt", "r", encoding=codec) as file:
        text = file.read()
    print(codec.rjust(12), "|", text)

# import unicodedata

# letter1 = "µ"
# letter2 = "μ"
# print(unicodedata.name(letter1))
# print(unicodedata.name(letter2))
