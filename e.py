import tkinter as tk

def шифрування():
     word = input("") 
     key = 2 
 
     word = str(word).replace(" ", "") 
     si= dict() 
     result = "" 
 
     for i in range(key): 
      si[i] = list() 
 
 
     for num in range(0, len(word), key): 
        for i in range(key): 
            if len(word) > num + i: 
                si[i] += word[num + i] 
 
        shiphred_list = list(si.values()) 
        shiphred_list.reverse() 
 
        for i in shiphred_list: 
         result += "".join(i) 
 
        print(result)

вікно = tk.Tk()
вікно.title("Шифр Чистоколу")

вхід = tk.StringVar()
tk.Label(вікно, text="Введіть текст:").pack()
Ввід = tk.Entry(вікно, textvariable=вхід)
Ввід.pack()

вихід = tk.StringVar()
tk.Label(вікно, text="Зашифрований текст:").pack()
Вивід = tk.Entry(вікно, textvariable=вихід, state='readonly')  # Змінив ім'я змінної, щоб уникнути конфлікту
Вивід.pack()

кнопка_шифрування = tk.Button(вікно, text="Зашифрувати", command=шифрування)  # Змінив ім'я змінної
кнопка_шифрування.pack()

вікно.mainloop()