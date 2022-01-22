message = "Hello World"
A_public = 125
A_private = 195
B_public = 130
B_private = 230

class keys():
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.partkey = None
        self.fullkey = None

    def generate_partkey(self):
        self.partkey = self.public_key1 ** self.private_key
        self.partkey = self.partkey % self.public_key2

    def generate_fullkey(self, partkey):
        self.fullkey = partkey ** self.private_key
        self.fullkey = self.fullkey % self.public_key2

    def encrypt_message(self, message):
        encrypted = ''
        for i in message:
            encrypted += chr(ord(i) + self.fullkey)
        return encrypted

    def decrypt_message(self, message):
        decrypted = ''
        for i in message:
            decrypted += chr(ord(i) - self.fullkey)
        return decrypted

Aperson = keys(A_public, B_public, A_private)
Bperson = keys(A_public, B_public, B_private)

Aperson.generate_partkey()
Bperson.generate_partkey()

Aperson.generate_fullkey(Bperson.partkey)
Bperson.generate_fullkey(Aperson.partkey)

print (f'''Aperson   Bperson
Публичные ключи
{Aperson.public_key1}     {Bperson.public_key1}
{Aperson.public_key2}     {Bperson.public_key2}
Части ключей
{Aperson.partkey}     {Bperson.partkey}
Полные ключи
{Aperson.fullkey}     {Bperson.fullkey}''')

encrypted = Aperson.encrypt_message(message)
print('Зашифрованное сообщение:', encrypted)

decrypted = Bperson.decrypt_message(encrypted)
print('Расшифрованное сообщение:',decrypted)