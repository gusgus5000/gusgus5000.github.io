from tkinter import messagebox, simpledialog, Tk


def get_task():
    Task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
    return Task


def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message:')
    return message


def is_even(number):
    return number % 2 == 0


def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters


def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters


def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message


root = Tk()

while True:
    task = get_task()
    if task == 'e':
        message = get_message()
        encrypt = swap_letters(message)
        messagebox.showinfo("ciphertext of the secret message is:", encrypt)
    elif task == '4321':
        message = get_message()
        decrypt = swap_letters(message)
        if decrypt[-1].lower() == "x":
            decrypt = decrypt[:-1]
        messagebox.showinfo("plaintext of the secret message is :", decrypt)
    else:
        break
        root.mainloop()
