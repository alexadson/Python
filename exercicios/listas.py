# if e else para definir, suspeita, cúmplice, assassino e inocente.
def classificar_participacao(respostas):
    respostas_positivas = sum(respostas)  # sum =soma de respostas

    if respostas_positivas == 2:
        return "Suspeita"
    elif 3 <= respostas_positivas <= 4:
        return "Cúmplice"
    elif respostas_positivas == 5:
        return "Assassino"
    else:
        return "Inocente"


def fazer_perguntas():
    perguntas = [
        "Você telefonou para a vítima?",
        "Você esteve no local do crime?",
        "Você mora perto da vítima?",
        "Você tinha dívidas com a vítima?",
        "Você já trabalhou com a vítima?"
    ]

    respostas = []

    print("Responda as seguintes perguntas com 'sim' ou 'não':")
    for pergunta in perguntas:  # estutura de repetição para respostas
        resposta = input(pergunta + " ").strip().lower()  # ?
        while resposta not in ['sim', 'não']:
            print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")
            resposta = input(pergunta + " ").strip().lower()  # ?
        # append foi usado para adicionar o sim a final.
        respostas.append(resposta == 'sim')

    return respostas


def main():  # definição principal
    respostas = fazer_perguntas()
    classificacao = classificar_participacao(respostas)
    print(f"A classificação da participação no crime é: {classificacao}")


if __name__ == "__main__":
    main()

# ---------------------------------------------------------


def ler_respostas():
    opcoes = ["Windows Server 2022", "Unix",
              "Red Hat Enterprise Linux (RHEL)", "Solaris", "Unbutu Server OS", "Outro"]
    votos = [0] * 6  # Lista para armazenar os votos de cada opção

    print("Digite o número correspondente ao seu sistema operacional favorito:")
    print("1. Windows Server 2022")
    print("2. Unix")
    print("3. Red Hat Enterprise Linux (RHEL)")
    print("4. Solaris")
    print("5. Unbutu Server OS")
    print("6. Outro")
    print("Digite 0 para encerrar a entrada de dados.")

    while True:
        try:
            resposta = int(input("Resposta: "))
            if resposta == 0:
                break
            elif 1 <= resposta <= 6:
                votos[resposta - 1] += 1
            else:
                print("Valor inválido! Por favor, digite um número entre 0 e 6.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")

    return votos, opcoes


def calcular_percentuais(votos):
    total_votos = sum(votos)
    percentuais = [(voto / total_votos) * 100 if total_votos >
                   0 else 0 for voto in votos]
    return percentuais, total_votos


def exibir_resultados(votos, percentuais, opcoes, total_votos):
    print("\nSistemas Operacionais - Votos %")
    for i, opcao in enumerate(opcoes):
        print(f"{opcao} - {votos[i]} {percentuais[i]:.0f}%")

    vencedor_index = votos.index(max(votos))
    vencedor = opcoes[vencedor_index]
    votos_vencedor = votos[vencedor_index]
    percentual_vencedor = percentuais[vencedor_index]

    print(f"\nTotal de {total_votos} votos")
    print(f"O Sistema Operacional mais votado foi o {vencedor}, com {
          votos_vencedor} votos, correspondendo a {percentual_vencedor:.0f}% dos votos.")


def main():  # DEFINIÇÃO PRINC
    votos, opcoes = ler_respostas()
    percentuais, total_votos = calcular_percentuais(votos)
    exibir_resultados(votos, percentuais, opcoes, total_votos)


if __name__ == "__main__":
    main()
