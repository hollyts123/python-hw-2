# Ініцілізовано функцію, напишіть в тілі функції логіку яка
# перетворить вхідну строчку за певною логікою.

# Функція приймає на вхід будь яку строчку і виводить в консоль 
# за допомогою функції print()
#  оновлену версію цієї строчки.
# Якщо довжина строчки більша ніж 5 символів 
#    -> Потрібно вивести лише перші 5 символів та в кінці додати три точки (...).
# Якщо перша літера строчки U або u (регістр не важливий) 
#    -> Вивести всю строчку в Upper Case (верхній регістр)
# Якщо перша літера строчки L або l (регістр не важливий) 
#    -> Вивести всю строчку в Lower Case (нижній регістр)
# Якщо жодна умова вище не підходить - вивести строку без змін.
# Декілька умов можуть пересікатись!
# Можна додавати свої тести за прикладом. 
# Потрібно врахувати обробку можливих помилок.

# Наприклад:
#   transformStr('Testing string') - > 'Testi...' (довжина більше 5 символів)
#   transformStr('Lux') - > 'lux' (Починается на L)
#   transformStr('up') - > 'UP' (Починается на U)
#   transformStr('Luxery') - > 'luxer...' (Починается на L + довжина більше 5 символів)

def transformStr(str):
    if(len(str) > 5):
        if(len(str) > 5 and str[0] == 'L' or str[0] == 'l'):
            print(str[0:5].lower() +"...")
        elif(len(str) > 5 and str[0] == 'u' or str[0] == 'U'):
            print(str[0:5].upper() +"...")    
        else:    
            print(str[0:5] + "...")    
    elif(str[0] == 'L' or str[0] == 'l'):
        print(str.lower())
    elif(str[0] == 'U' or str[0] == 'u'):
        print(str.upper())           
    else: 
        print(str) 

    


    
          

transformStr('Testing string') # 'Testi...' (довжина більше 5 символів)
transformStr('Lux') # 'lux' (Починается на L)
transformStr('up') # 'UP' (Починается на U)
transformStr('Luxery') # 'luxer...' (Починается на L + довжина більше 5 символів)
transformStr('underground')
transformStr('Mixer')
transformStr('lEXuS')
transformStr('UniCOde')
transformStr('Python')
transformStr('coding')
transformStr('Home')