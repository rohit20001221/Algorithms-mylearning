from Crypto.Cipher import DES


def pad(text):
    while len(text) % 8 != 0:
        text += b" "

    return text


key = b"12345678"
iv = b"34278561"
text = b"this is a sample test message"

des = DES.new(key, DES.MODE_CBC, iv)

padded_text = pad(text)

print(des.encrypt(padded_text))
