'''
Запросить фразу состоящую минимум из трех слов. 
Сформировать фразу из этих слов в которой каждая буква слова, 
продублирована то количество раз, которое соответствует номеру позиции 
данной буквы в слове этой буквы. 
Например: Привет как дела => Прриииввввееееетттттт кааккк деелллаааа

'''

fraz = input('Введите фразу минимум из трёх слов: ').split()

fraz_len = len(fraz)


if fraz_len < 0:
    print("Меньше 3 слов")
else:
    new_word = []
    # Берём слово из фразы
    for word in fraz:
        # Трансформируем слово
        tran_word = ""
        for idx, char in enumerate(word, start=1):
            tran_word += char * idx 
        new_word.append(tran_word)
   
    
    new_fraz = " ".join(new_word)
    print(new_fraz)


