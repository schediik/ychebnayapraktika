import tkinter as tk
def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            start = ord('А') if char.isupper() else ord('а')
            offset = ((ord(char) - start + shift) % 26)
            new_char = chr(start + offset)
        else:
            new_char = char
        result.append(new_char)
    return ''.join(result)
def encrypt_decrypt():
    input_text = entry.get()
    try:
        shift_value = int(shift_entry.get())
    except ValueError:
        output_label.config(text="Ошибка: введите целое число")
        return

    encrypted_text = caesar_cipher(input_text, shift_value)
    output_label.config(text=encrypted_text)
root = tk.Tk()
root.title("Шифрование методом Цезаря")

tk.Label(root, text="Введите текст:").pack(pady=10)
entry = tk.Entry(root, width=50, bg="pink")
entry.pack(padx=10, pady=5)

tk.Label(root, text="Введите величину сдвига:").pack(pady=5)
shift_entry = tk.Entry(root, width=10, bg="pink")
shift_entry.pack(padx=10, pady=5)

encrypt_button = tk.Button(root, text="Зашифровать / Расшифровать", command=encrypt_decrypt, bg="aquamarine")
encrypt_button.pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 12), bg="lavender")
output_label.pack(pady=10)

root.mainloop()