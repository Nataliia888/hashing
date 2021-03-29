
'''hashlib is a hashing function that takes variable length
of bytes and converts it into a fixed-length sequence'''
import hashlib

#The function returns a hash of the file passed into it
def get_file_sha(file):
    # Initializing the sha256() method
    m = hashlib.sha256()
    # loop till the end of the file
    chunk = 0
    while chunk != b'':
        # we can read only 1024 bytes at a time
        chunk = file.read(1024)
        m.update(chunk)
        # return the hex representation of SHA-256 digest
        return m.hexdigest()

# open file for reading in binary mode
with open('decrypted_PII.csv', 'rb') as f1, open('PII.csv', 'rb') as f2:
    file1 = get_file_sha(f1)
    file2 = get_file_sha(f2)
    print('original:', file1)
    print('decrypted:', file2)
    if file1 != file2:
        print('file is changed')
    else:
        print('file is not changed')


