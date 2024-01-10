import random
import os

#============================== ============================#
#                                                                                                                                                               #
# The default mesorah is Modern Israeli. If you'd like to change it, just change the              #
# latin letter that comes before the "#" and the name of the letter.                                          #
#                                                                                                                                                               # 
# EXAMPLE:                                                                                                                                          #
# 1511: 'ch', # Qof                                                                                                                               #
#              ↓                                                                                                                                              #
# 1511: 'kh', # Qof                                                                                                                               #
#                                                                                                                                                               #
# You'll also have to change the final version of the letter                                                         #
#                                                                                                                                                               #
#1498: 'ch',# Final Chaf                                                                                                                      #
#1499: 'ch',# Chaf                                                                                                                               #
#              ↓                                                                                                                                              #
#1498: 'kh',# Final Chaf                                                                                                                      #
#1499: 'kh',# Chaf                                                                                                                               #
#                                                                                                                                                               #
#==========================================================#


#==============#
# FORMAT FOR replace ={} FUNCTION       
# ASCII Decimal Code : "latin letter",              
#==============#

replace = {
           1488: '\'', #Aleph
           64305: 'b', #Bet - No idea why this ascii code
                               #          works but other ascii codes don't for other letters?
                               #          worth reading into
           1489: 'v', # Vet
           1490: 'g', #Gimel
           1491: 'd', #Dalet
           1492: 'h', #He
           1493: 'v',  #Vav
           1494: 'z', #Zayin
           1495: 'ch',# Het
           1496: 't', # Tet
           1497: 'y', # Yod
           1498: 'ch',# Final Chaf
           1499: 'ch',# Chaf
           'KAF': 'k', # Kaf
           1500: 'l', #Lamed
           1501: 'm', #Final Mem
           1502: 'm', #Mem
           1503: 'n', # Final Nun
           1504: 'n', #Nun
           1505: 's', # Samekh
           1506: '\'', # Ayin
           1507: 'f', # Final Fe
           'PE': 'p', # Pe
           1508: 'f', # Fe
           1509: 'tz', # Final Tsadi
           1510: 'tz', # Tsadi
           1511: 'k', # Qof
           1512: 'r', # Resh
           '  SHIN  ': 'sh', # Shin
           ' SIN ': 's', # Sin
           1514: 't' , # Tav
            # VOWELS
            1458: 'a', 1463: 'a', 1464: 'a', 1459: 'a', #A
            1457: 'e', 1462: 'e', # E
            1461: 'e',  ###########This is Tsere/Tseire
            1460: 'i', # I
            1465: 'o', # O
            1467: 'u' # U
            }
#------------------------------------------------------------------------------------------------------------------------------
#Don't touch this
os.system('cls' if os.name == 'nt' else 'clear')
clist = ['א', 'בּ', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'KAF', 'כ', 'ל', 'מ', 'נ','ס', 'ע', 'PE', 'פ', 'צ', 'ק', 'ר', ' SHIN ', ' SIN ', 'ת']
vlist = [ u'\u05b2', u'\u05b3', u'\u05b4', u'\u05b5', u'\u05b6', u'\u05b7', u'\u05b8', u'\u05b8',  u'\u05b9']
flist = ['ך', 'ם', 'ץ', 'ן' , 'ף']
streak = 0
loop = 0
print("=======\n\nHebrew Transliteration Pracitce\ntype \"stop\" to exit the program\nConsider using the font Varela round for easier reading\n")

while loop < 1: 
    hebrewout = random.choice(clist) + random.choice(vlist) +  random.choice(clist) + random.choice(vlist) + random.choice(flist)
    hebrewin = (hebrewout.translate(replace).replace('KAF', 'k').replace('PE', 'p' ).replace(' SHIN ', 'sh').replace(' SIN ', 's')) # transliterates the hebrew while also fixing the KAF, PE, SIN & SHIN problem
    print("=======\n" + hebrewout.replace('KAF', 'כּ').replace('PE','פּ').replace(' SHIN ', 'שׁ').replace(' SIN ', 'שׂ')) # KAF, PE, SHIN, SIN fix 

    answer = input()
    if answer == "stop":
        loop = 2 
        print("Goodbye!")
    elif answer == hebrewin: 
        print("Correct")    
        streak = streak + 1
        if (streak % 5) == 0:
            print("-----\nYour streak is now " + str(streak) + "\n-----\n")
        elif streak == 1:
            print("-----\nAnd so the journey starts again\n-----")
    else:
        print("No, the correct answer is " + hebrewin + "\n----\nYou broke your streak of " + str(streak) + "\n-----")
        streak = 0
