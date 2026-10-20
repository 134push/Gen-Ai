alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

your_message = input("enter your message : ").lower()

def encrpt():
    new_message = []
    shift = int(input("enter the code on where you start the encrupted : "))
    for letter in your_message:
        if letter in alphabet:
            old_index = alphabet.index(letter)
            new_index = (old_index + shift) % len(alphabet)
            new_message.append(alphabet[new_index])
        else:
            new_message.append(letter)
    
    encrypted_text = "".join(new_message)
    print(f"your encrpted message = {encrypted_text}") 
        
encrpt()
