from utils.utils import remove_accents

def get_user_inputs():
    while True:
        city = input("Digite a cidade: ").strip().upper()
        city = city.replace("Ç", "C")
        city = remove_accents(city)
        state = input("Digite a sigla do estado(ex: 'SP'): ").strip().upper()

        if not city or len(state) != 2:
            print("Entrada inválida, tente novamente.")
            continue
        return city, state