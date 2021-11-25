#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Прочитать txt файл
# убрать из текста знаки препинания
# слова, соединенные дефисом, представить как два разных слова
# разбить на слова
# подсчитать максимальную длину слова (слов) и вывести их на экран
# записать в отдельный файл разделенные слова (по одному слову на строку)

punct = str.maketrans("", "", ",.?!*+—;:()\"'")
maxlen = 0
maxwords = []

with open("CrimeAndPunishment.txt", encoding="utf-8") as infile, open("outfile.txt", "w", encoding="utf-8") as outfile:
    for abc in infile:
        cleanwords = (abc.lower()).replace("-", " ")
        cleanwords = cleanwords.translate(punct)
        cleanwords = cleanwords.split()
        for word in cleanwords:
            if maxlen < len(word):
                maxlen = len(word)
                maxwords = [word]
            elif len(word) == maxlen:
                maxwords.append(word)

        cleanwords = "\n".join(cleanwords) +"\n"
        outfile.write(cleanwords)

print("Max length of word(s): {}".format(maxlen))
print("List of word(s) with max length: ", maxwords)
