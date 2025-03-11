def obter_frase():
   
    while True:
        frase = input("Digite uma frase: ").strip()
        if frase:
            return frase
        print("Erro: A entrada não pode estar vazia. Tente novamente.")


def analisar_frase(frase):
    
    num_caracteres = len(frase)
    palavras = frase.split()
    num_palavras = len(palavras)
    palavra_mais_longa = max(palavras, key=len) if palavras else ""
    
    return num_caracteres, num_palavras, palavra_mais_longa, palavras


def manipular_frase(frase, palavras):
   
    frase_invertida_caracteres = frase[::-1]
    frase_invertida_palavras = " ".join(palavras[::-1])
    frase_maiusculas = frase.upper()
    frase_minusculas = frase.lower()
    tupla_palavras = tuple(palavras)
    
    return (
        frase_invertida_caracteres,
        frase_invertida_palavras,
        frase_maiusculas,
        frase_minusculas,
        tupla_palavras
    )


def exibir_resultados(num_caracteres, num_palavras, palavra_mais_longa,
                      frase_invertida_caracteres, frase_invertida_palavras,
                      frase_maiusculas, frase_minusculas, tupla_palavras):
    
    print("\n===== Análise da Frase =====")
    print(f"Número de caracteres: {num_caracteres}")
    print(f"Número de palavras: {num_palavras}")
    print(f"Palavra mais longa: {palavra_mais_longa}")
    print(f"Frase invertida (por caracteres): {frase_invertida_caracteres}")
    print(f"Frase invertida (por palavras): {frase_invertida_palavras}")
    print(f"Frase em maiúsculas: {frase_maiusculas}")
    print(f"Frase em minúsculas: {frase_minusculas}")
    print(f"Tupla de palavras: {tupla_palavras}")


def main():
   
    frase = obter_frase()
    num_caracteres, num_palavras, palavra_mais_longa, palavras = analisar_frase(frase)
    
    (
        frase_invertida_caracteres,
        frase_invertida_palavras,
        frase_maiusculas,
        frase_minusculas,
        tupla_palavras
    ) = manipular_frase(frase, palavras)
    
    exibir_resultados(
        num_caracteres, num_palavras, palavra_mais_longa,
        frase_invertida_caracteres, frase_invertida_palavras,
        frase_maiusculas, frase_minusculas, tupla_palavras
    )


if __name__ == "__main__":
    main()
