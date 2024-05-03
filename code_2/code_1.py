import base64

text = str(input("введите текст для шифрования в base64: "))
encoded = base64.b64encode(text.encode())

base64_message = encoded
base64_bytes = base64_message.decode('ascii')
message_bytes = base64.b64decode(base64_bytes)
decode = message_bytes.decode('ascii')

print(encoded) 
print(decode) 