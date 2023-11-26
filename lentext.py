def dov (text):
    sybvol = [".",',','-',"'","\""]
    for sybvols in sybvol:
        text= text.replace(sybvols,'')

    vciclova = text.split() 
    clovacount=[]
    
    for clova  in vciclova:
        clova = {
           "clova": clova,
         " dovjuna": len(clova)   

        }
        clovacount.append(clova)

    clova_sort_dovjuna = []   
    # bubble сортування 
    for i in range (len(clovacount)):
        for j in range (len(clovacount)- i - 1):
            if clovacount[j]["dovjuna"]> clovacount[j+1]["dovjuna"]:
                temp = clovacount[j]
                clovacount[j] = clovacount[j+1]
                clovacount[j+1]= temp
    
    clovacount.reverse()

    if   len(clovacount)>5:
        for i in range(0,5):
            print ( f'Top {i +1} - {clovacount[i][clova]} - {clovacount[i]["dovjuna"]} symbvol')
    else:
        for i in range(0,len(clovacount)):
            print ( f'Top {i +1} - {clovacount[i][clova]} - {clovacount[i]["dovjuna"]} symbol') 

def paxunokclova(text):
     dla_symvoliv = [".", ",", "-", "'", "\""]
     for symvols in dla_symvoliv :
        text = text.replace(symvols, '') 

     vciclova = text.split() 
     clovacount=[]
    
     for clova  in vciclova:
        clova = {
           "clova": clova,
         " dovjuna": len(clova)   

        }
        clovacount.append(clova) 
        clova_sort_dovjuna = []   
    # bubble сортування 
        for i in range (len(clovacount)):
            for j in range (len(clovacount)- i - 1):
             if clovacount[j]["dovjuna"]> clovacount[j+1]["dovjuna"]:
                temp = clovacount[j]
                clovacount[j] = clovacount[j+1]
                clovacount[j+1]= temp      
     clovacount.reverse()

     if   len(clovacount)>5:
        for i in range(0,5):
            print ( f'Top {i +1} - {clovacount[i][clova]} - {clovacount[i]["dovjuna"]} times')
     else:
        for i in range(0,len(clovacount)):
            print ( f'Top  {i +1} - {clovacount[i][clova]} - {clovacount[i]["dovjuna"]} times') 

def pokazatu(text):
    vciclova = text.split()
    print(f"\n{len(vciclova)} слів")

text = input("Введіть текст: ")

choice = input("Виберіть варіант:"
      "\n1 - Топ 5 по довжині"
      "\n2 - Топ 5 по кількості повторювань"
      "\n3 - Показати кількість слів у тексті\n")
if choice == "1":
    dov(text)
elif choice == "2":
    paxunokclova(text)
elif choice == "3":
    pokazatu(text)

 
