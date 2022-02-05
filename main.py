import random


def give_cards(number_of_cards: int):
    """Retorna uma lista de cartas aleatórias do baralho, as removendo dele em seguida. O número de cartas retornadas
    é o mesmo especificado no paramêtro 'number of cards'."""
    hand = []
    for _ in range(number_of_cards):
        card = random.choice(deck)
        hand.append(card)
        deck.pop(deck.index(card))
    return hand


def score(hand: list):
    """Retorna a pontuação de uma mão de cartas."""
    score = 0
    for card in hand:
        if card == "Q" or card == "J" or card == "K":
            score += 10
        elif type(card) is int:
            score += card
        # No caso da carta ser um Ás:
        else:
            if score + 11 <= 21:
                score += 11
            # No caso da pontuação exceder 21 com a soma do Ás valendo 11:
            else:
                score += 1
    return score


def check_hand(total_score: int):
    """Retorna 'True' no caso de um blackjack, 'False' caso a pontuação tenha excedido 21,
    e 'None' em nenhum dos dois casos."""
    if total_score == 21:
        return True
    elif total_score > 21:
        return False
    return None


def display(final=True):
    """Mostra as cartas que estão na mesa e a pontuação atual."""
    show_user_hand = f"Suas cartas: {', '.join(str(card) for card in user_hand)}. Sua pontuação: {user_score}"
    show_comp_first_hand = f"Primeira carta da máquina: {comp_hand[0]}"
    show_comp_hand = f"Cartas da máquina: {', '.join(str(card) for card in comp_hand)}. Pontuação: {comp_score}"
    print(show_user_hand)
    # Caso final == True, todas as cartas da máquina são mostradas;
    # enquanto o jogo estiver em andamento, apenas a primeira carta da máquina é mostrada.
    if final:
        print(show_comp_hand)
    else:
        print(show_comp_first_hand)


def finish(final=False):
    """Executa a função display. Nos cenários de fim de jogo, além de executar a função display, retorna 'True'.
    Caso o jogador escolha não mais tirar cartas do baralho, o parâmetro 'final' deverá ser igual a 'True'."""

    # Checa se o jogador tem 21 pontos ou mais
    check_user_score = check_hand(user_score)

    # Caso a máquina e o jogador tenha feito 21 pontos
    if check_user_score and check_comp_score:
        display()
        print("Empate")
        return True

    # Caso apenas o jogador tenha feito 21 pontos
    elif check_user_score:
        display()
        print("Voce Ganhou! Blackjack!")
        return True

    # Caso a pontuação do jogador tenha excedido 21 pontos
    elif check_user_score is False:
        # Não é preciso mostrar mais do que a primeira carta da máquina
        display(final=False)
        print("Você perdeu. Passou de 21.")
        return True

    # Caso o jogador opte por não tirar mais cartas do baralho
    if final:
        # Caso a pontuação da máquina tenha excedido 21 pontos
        if check_comp_score is False:
            display()
            print("Você ganhou! A máquina passou de 21")
            return True

        # Caso a pontuação da máquina seja maior que a do jogador
        elif comp_score > user_score:
            display()
            print("Você perdeu.")
            return True

        # Caso a pontuação da máquina seja a mesma que a do jogador
        elif comp_score == user_score:
            display()
            print("Empate.")
            return True

        # Caso a pontuação do jogador seja maior que a da máquina
        elif user_score > comp_score:
            display()
            print("Você venceu!")
            return True

    # Caso nenhuma das condições acima tenham sido satisfeitas, significa que o jogo ainda está em andamento e que
    # não é preciso mostrar mais que a primeira carta da máquina
    display(final=False)


play = input("Bem vindo! Gostaria de jogar uma partida de Blackjack? Digite 'S' para Sim.\n").upper()
while play == "S":

    # Cria o baralho
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    deck *= 4
    random.shuffle(deck)

    # Define as cartas e a pontuação do jogador
    user_hand = give_cards(2)
    user_score = score(user_hand)

    # Define as cartas e a pontuação da máquina
    comp_hand = give_cards(1)
    comp_score = score(comp_hand)
    while comp_score <= 16:
        comp_hand += give_cards(1)
        comp_score = score(comp_hand)
    # Só é preciso checar uma vez se a máquina tem 21 pontos ou mais
    check_comp_score = check_hand(comp_score)

    # Caso o jogador tenha feito 21 pontos com a mão inicial
    if finish():
        play = input("Gostaria de jogar mais uma partida? Digite 'S' para Sim.\n").upper()
        continue

    while input("Gostaria de tirar mais uma carta? Digite 'S' para Sim.\n").upper() == "S":
        user_hand += give_cards(1)
        user_score = score(user_hand)
        check_user_score = check_hand(user_score)
        # Caso a pontuação do jogador seja igual a 21 pontos
        if check_user_score:
            break
        # Caso a pontuação do jogdor tenha excedido 21 pontos
        elif check_user_score is False:
            break
        finish()

    finish(final=True)
    play = input("Gostaria de jogar mais uma partida? Digite 'S' para Sim.\n").upper()
