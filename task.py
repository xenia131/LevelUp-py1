def get_hidden_card(card_number, n = 4):
    card_number = str(card_number)
    return(f'{"*" * n}{card_number[12:]}')

print(get_hidden_card('1234123412344321', 6))
