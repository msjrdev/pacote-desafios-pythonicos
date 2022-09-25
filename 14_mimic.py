"""
14. mimic

Neste desafio você vai fazer um gerador de lero-lero.

É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.

Para isso você precisa:

A. Abrir o arquivo especificado via linha de comando.

B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.

C. Criar um dicionário de "imitação".

Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.

Por exemplo, suponha um arquivo com o conteúdo: A B C B A

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B

Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.

Use a string vazia como a primeira palavra do texto para preparar as coisas.

Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""

import random
import sys
from collections import defaultdict


def file_to_list(filename):
    with open(filename) as f:
        list_words = f.read().lower().split()
    return list_words


def mimic_dict(filename):
    mimic_d = defaultdict(list)
    mimic_list = file_to_list(filename)
    first_word, last_word = mimic_list[0], mimic_list[-1]
    mimic_list = mimic_list[1:-2]
    mimic_tuple = list(zip(mimic_list, mimic_list[1:]))
    for k, v in mimic_tuple:
        if v not in mimic_d[k]:
            mimic_d[k].append(v)
    mimic_d[""], mimic_d[last_word] = first_word, ""
    return mimic_d


def print_mimic(mimic_dict, word):
    """Dado o dicionario imitador e a palavra inicial, imprime texto de 200 palavras."""
    # +++ SUA SOLUÇÃO +++
    new_text = word.capitalize()
    capitalize_next_word = False
    word_init = word
    for count in range(200):
        list_words = mimic_dict[word]
        if list_words != [''] and list_words:
            word = random.choice(list_words)
        else:
            word = word_init
        new_text += f' {word.capitalize()}' if capitalize_next_word else f' {word}'
        # a cada 20 palavras, coloca um ponto final
        if count % 20 == 0:
            new_text += "."
            capitalize_next_word = True
        else:
            capitalize_next_word = False
    print(new_text)


# Chama mimic_dict() e print_mimic()
def main():
    if len(sys.argv) != 2:
        print('Utilização: ./14_mimic.py file-to-read')
        sys.exit(1)

    dict = mimic_dict(sys.argv[1])
    print_mimic(dict, '')


if __name__ == '__main__':
    main()
