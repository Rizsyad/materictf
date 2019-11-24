import base64
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def de_base64(data):
    return base64.b64decode(data)

def en_base64(data):
    return base64.b64encode(data)

def encrypt():
    texts = raw_input("Enter the text to encode: ")
    encoded = ''

    print("\n")

    for i in range(0, 10):
        base64_encode = en_base64(texts)
        texts = base64_encode
        print("Encode ke {} [ {} ] \n\n".format(i+1, base64_encode))

def dencode():
    txtbase64 = raw_input("Enter the text to decode: ")  
    base64_decode = ''
    # txtbase64 = "VmtaV1MxTldSWHBrUlRGT1VsVXdkMVpGV1RWU01ERldaRE53V1UxSGVGQlZWRUkwVm1zMVZtSkdRbFZpYWtFNQ=="

    print("\n")

    for i in range(0, 999): #0 sampai 999
        try:
            #mencoba mendecode enkripsi menjadi string
            base64_decode = de_base64(txtbase64)
            txtbase64 = base64_decode
            print("[?] Percobaan ke {} [ {} ] \n\n".format(i+1, base64_decode))
        except:
            #melakukan break jika tidak bisa lagi didecode
            break

def main():
    choice = int(input("1. Encrypt\n2. Decrypt\nchoice (1 or 2): "))

    if choice == 1:
        encrypt()
    elif choice == 2:
        dencode()
    else:
        print("Invalid Choice")


if __name__ == '__main__':
    cls()
    main()


# Vm0wd2QyVkZOVWhTYmtwT1ZtMW9WMVl3Wkc5V1JsbDNXa2M1V0ZadGVIbFhhMXBQWVVaS2MxTnNXbFpOYm1oUVdWVmFTMk14VG5OWGJHUlRUVEZLVVZadGNFZFpWMUpYVW01T2FWSnVRazlVVkVKTFUxWmFjMVZyWkd0TlJGWjVWRlpXVjJGSFZuRlJWR3M5
