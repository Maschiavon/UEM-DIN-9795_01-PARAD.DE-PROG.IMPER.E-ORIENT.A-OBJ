from os import error # Para as estruturas try except
import random # Para criação do vetor aleatório
import sys # Para ter acesso aos argumentos digitados na linha de comando
import selectionsort # Para ter acesso ao algoritmo do Selection Sort, outros algoritmos podem ser construídos e importados
import time # Para o cálculo de tempo de execução dos algoritmos de ordenação

count = 0 #Contador global (para o Merge Sort apenas)

def main():
    x = 13 # Definição do tamanho do vetor
    VetorAleatorioOriginal = random.sample(range(x), x) # Versão aleatória do vetor de entrada para os algoritmos de ordenação

    VetorInvertido = VetorAleatorioOriginal.copy()
    VetorInvertido.reverse() # Versão invertida do vetor de entrada para os algoritmos de ordenação

    VetorCrescente = VetorAleatorioOriginal.copy()
    VetorCrescente.sort() # Versão crescente do vetor de entrada para os algoritmos de ordenação

    VetorDecresente = VetorCrescente.copy()
    VetorDecresente.reverse() # Versão decrescente do vetor de entrada para os algoritmos de ordenação
    
    VetorEscolhido = [] # Vetor que representa a versão do vetor escolhida pelo usuário
    
    ordenacao = "" # argumento da linha de comando que representa como a entrada estará ordenada inicialmente
    algortimo = "" # argumento da linha de comando que representa o algoritmo de ordenação que será utilizado
    
    #Teste da validade dos argumentos digitados na linha de comando
    try:
        ordenacao = sys.argv[1]
        algortimo = sys.argv[2]
    except:
        raise ValueError("Comando inválido!")
    
    #Verificação do argumento de ordenação inicial do vetor de entrada
    if ordenacao == 'aleatorio':
        VetorEscolhido = VetorAleatorioOriginal
    elif ordenacao == 'invertido':
        VetorEscolhido = VetorInvertido
    elif ordenacao == 'crescente':
        VetorEscolhido = VetorCrescente
    elif ordenacao == 'decrescente':  
        VetorEscolhido = VetorDecresente
    else: 
        raise ValueError("Comando de ordenação inválido!")
    
    #Verificação e pesquisa de algoritmo com o nome digitado na linha de comando
    #Os algoritmos do Merge Sort e Bubble Sort já estão no arquivo main.py
    #Enquanto que outros algoritmos de ordenação deverão ser adicionados com uma importação de arquivo de extensão .py
    if algortimo == 'mergesort':
        print("Algoritmo Escolhido: Merge Sort")
        start = time.time()
        getattr(Sorter, algortimo)(Sorter, VetorEscolhido)
        end = time.time()
        print("\ntempo consumido = " + str(end - start) + " segundos\n")
    elif algortimo == 'bubblesort':
        print("Algoritmo Escolhido: Bubble Sort\n")
        start = time.time()
        resultado = getattr(Sorter, algortimo)(VetorEscolhido)
        end = time.time()
        print("\ntempo consumido = " + str(end - start) + " segundos")
    else:
        #Verificação do nome do algoritmo que foi digitado na linha de comando caso não seja Merge Sort ou Bubble Sort
        try:
            print("Algoritmo Escolhido: " + algortimo + "\n")
            classePorString = getattr(sys.modules[__name__], algortimo)
            start = time.time()
            resultado = getattr(classePorString, algortimo)(VetorEscolhido)
            end = time.time()
            print("tempo consumido = " + str(end - start) + " segundos\n")
        except:
            raise ValueError("O algoritmo especificado não existe!")

#Classe que armazena os algoritmos originais de main.py
class Sorter:
    def mergesort(self, Vetor: list):
        global count
        if len(Vetor) > 1:
            print("\nVetor à dividir: " + str(Vetor))
            meio = len(Vetor)//2
            VetE = Vetor[:meio]
            
            print("\nMetade Esquerda: " + str(VetE))
            VetD = Vetor[meio:]
            print("Metade Direita: " + str(VetD))
            self.mergesort(self, VetE)
            self.mergesort(self, VetD)
            i = j = k = 0
            while i < len(VetE) and j < len(VetD):
                if VetE[i] < VetD[j]:
                    Vetor[k] = VetE[i]
                    i += 1
                else:
                    Vetor[k] = VetD[j]
                    j += 1
                    count += 1
                k += 1
            while i < len(VetE):
                Vetor[k] = VetE[i]
                i += 1
                k += 1
            while j < len(VetD):
                Vetor[k] = VetD[j]
                j += 1
                k += 1
            print("\nPartição Resultante: " + str(Vetor))
            print("Número de trocas até o momento: " + str(count))

    def bubblesort(Vetor: list):
        print("Vetor Original: " + str(Vetor))
        contador = 0
        elementos = len(Vetor) - 1
        ordenado = False
        while not ordenado:
            ordenado = True
            for i in range(elementos):
                if Vetor[i] > Vetor[i + 1]:
                    Vetor[i], Vetor[i + 1] = Vetor[i + 1], Vetor[i]
                    ordenado = False
                    print("\n" + str(Vetor))
                    contador += 1
                    print("Número de trocas até o momento: " + str(contador))
        if contador == 0:
            print("\nNúmero de trocas até o momento: " + str(contador))
        return Vetor

if __name__ == '__main__':
    main()