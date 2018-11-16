#1.Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах 
#в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее 
#эффективным использованием памяти.
#Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода 
#для одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду. 
#Также укажите в комментариях версию Python и разрядность вашей ОС.

def few_values(n1,n2) :
    bitAnd = n1 & n2
    bitOr = n1 | n2
    bitLeft2Difits = n1 << 2
    bitRight2Difits = n1 >> 2 
    string_output = 'Bit AND between 5 and 6 is '+str(bitAnd)
    string_output+= '. Bit OR between 5 and 6 is '+str(bitOr)
    string_output+= '. Bit shift left for 2 digits for 5 is '+str(bitLeft2Difits)
    string_output+= '. Bit shift right for 2 digits for 5 is '+str(bitRight2Difits) 
    return string_output

s=few_values(5, 6) 
print(s)

#Python version 3.7, OS 64 bit
#In method few_values was used 4*24bits = 96 bits of memory