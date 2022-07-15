vowels = ['a', 'e', 'i', 'o', 'u']

num_cases = int(input())

def null_cipher():
  output = ""
  for i in range(num_cases):
    decrypted_msg = ""
    encrypted_msg = input()
    for i in range(len(encrypted_msg)):
      if encrypted_msg[i:i+1] in vowels:
        if encrypted_msg[i+1:i+2] in vowels:
          decrypted_msg += encrypted_msg[i+1:i+2]
          encrypted_msg = encrypted_msg.replace(encrypted_msg[i:i+1],'', 1)
        else:  
          decrypted_msg += encrypted_msg[i+1:i+2]
    output += decrypted_msg + "\n"
  return output

print(null_cipher())
