import unidecode

# ------------ Primeira parte ------------

# Exercício 1

name = input("Insira o seu nome: ")

if name.isalpha():
    print("Nome em maiúsculas: ", name.upper())


# Exercício 2

def even_numbers(n):
    even_numbers = []

    for i in n:
        if i % 2 == 0:
            even_numbers.append(i)

    print("Números pares no array dado: ", even_numbers)


# Exercício 3

def invert_text(f):
    f = open(str(f), 'r')
    lines = f.readlines()
    lines.reverse()
    print("Linhas do ficheiro invertidas: ", lines)


# Exercício 4

def most_freq_words(f):
    f = open(str(f), 'r')
    
    words_freq = {}
    for line in f:
        for word in line.split():
            if word not in words_freq:
                words_freq[word] = 1
            else:
                words_freq[word]=words_freq[word]+1

    # ordenar o dicionário obtido de forma decrescente de value das keys
    freq_sorted = sorted(words_freq.items(), key=lambda x:x[1], reverse=True)
    
    # imprimir apenas os 10 elementos mais frequentes do dicionário
    for item in freq_sorted[:10]:
        print("\"", item[0],"\": ",item[1])


# Exercício 5

def clean_text(t):
    lower_text = t.lower()
    no_accents = unidecode.unidecode(lower_text)

    punctuation = [".", ":", "()", "!", "?", ",", ";", "-", '""']

    formated = ""
    for i in range(len(no_accents)):
        if no_accents[i] in punctuation:
            if i == len(no_accents)-1:
                formated = formated + no_accents[i]
            else:
                if no_accents[i-1] != " " and no_accents[i+1] != " ":
                    formated = formated + " " + no_accents[i]+ " "
                elif no_accents[i-1] != " " and no_accents[i+1] == " ":
                    formated = formated + " " + no_accents[i]
                else:
                    formated = formated + no_accents[i] + " "
        else:
            formated = formated + no_accents[i]

    print('Texto "limpo": ',formated)



# ------------ Segunda parte ------------

# Exercício 1 - Função para inverter string

def reverse(s):
    rev_string = s[::-1]
    print("Palavra dada: ", s)
    print("Palavra invervida: ", rev_string)


# Exercício 2 - Função para contar o número de "a" e "A" numa string

def count_a_A(s):
    counter_a = s.count("a")
    counter_A = s.count("A")
    print("A palavra dada (" + s + ") apresenta %s 'a' e %s 'A'." % (counter_a, counter_A))
    return counter_a, counter_A

# Exercício 3 - Função que retorna o número de vogais numa string

def count_vowels(s):
    counter = s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u") + s.count("A") + s.count("E") + s.count("I") + s.count("O") + s.count("U")
    print("A palavra dada (" + s + ") apresenta %s vogais." % counter)
    return counter


# Exercício 4 - Função que converte uma string para minúsculas

def lower_string(s):
    lower_s = s.lower()
    print("Palavra em minúsculas: ", lower_s)


# Exercício 5 - Função que converte uma string para maiúsculas

def upper_string(s):
    upper_s = s.upper()
    print("Palavra em maiúsculas: ", upper_s)