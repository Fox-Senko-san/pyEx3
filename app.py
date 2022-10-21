import multiprocessing
import os
import random
from RandomWordGenerator import RandomWord
from collections import OrderedDict

def anltk_file(file_name : str) -> None:
    sym : int = 0
    max_len : int = 0
    min_len : int = 999999
    gl : int = 0
    sgl : int = 0
    len_list : dict = {}
    with open(file_name, "r", encoding="UTF-8") as f:
        for word in f:
            word = word.strip()
            sym += len(word.replace(" ", ""))

            if len(word) > max_len:
                max_len = len(word)
            if len(word) < min_len:
                min_len = len(word)
            try:
                len_list[len(word)] += 1
            except:
                len_list[len(word)] = 1
            for char in word.lower():
                if char in "aeiouy": gl += 1
                else: sgl += 1


    output : str = f"""
********************************************************************
  Аналитика для файла {file_name}
********************************************************************

  1. Всего символов --> {sym}
  2. Максимальная длинна слова --> {max_len}
  3. Минимальная длинна слова --> {min_len}
  4. Средняя длинна слова --> {round((max_len+min_len)/2)}
  5. Количество гласных --> {gl}
  6. Количество согласных --> {sgl}
  7. Количество повторений слов с одинаковой длинной:

"""
    
    for key, i in OrderedDict(sorted(len_list.items())).items():
        output += f"    *{key} сим. >> {i} повтор.\n"

    print(output)

def create_file(x : list) -> None:
    file_name : str = f"file_rand{random.randint(0, 347598765)}_{os.getpid()}.txt"
    with open(file_name, "w", encoding="UTF-8") as f:
        generator = RandomWord(max_word_size=10, constant_word_size=False)
        for _ in range(random.randint(100000, 5000000)):
            f.write(generator.generate() + "\n")
    anltk_file(file_name)

def main() -> None:
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        pool.map(create_file, range(multiprocessing.cpu_count()))

if __name__ == "__main__":
    main()