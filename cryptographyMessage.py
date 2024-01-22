from cryptography.fernet import Fernet

message = input("whats your Message? ")
key = Fernet.generate_key()
fernet = Fernet(key)
message = fernet.encrypt(message.encode())
print("Encrypted Message: ", message)
message = fernet.decrypt(message).decode()
print("your original Message: ", message)