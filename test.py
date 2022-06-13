#To convert to hex
# 'halo'.encode().hex()

# To convert to string 
decrypted_message = bytes.fromhex('6FB078DA550B2650832661E14F4F8D2CFAEF475A0DF3A75CACDC5DE5CFC5FADC').decode('utf-8')
print(decrypted_message)