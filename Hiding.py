def hide_credit_card(card_number):
    if not isinstance(card_number, str):
        raise ValueError("Credit card number should be a string.")

    # Ensure the card number has at least four digits
    if len(card_number) < 4:
        raise ValueError("Credit card number should have at least four digits.")

    hidden_part = '*' * (len(card_number) - 4)
    visible_part = card_number[-4:]

    return hidden_part + visible_part


credit_card_number = "546512654126541265161"
hidden_card = hide_credit_card(credit_card_number)

print("Original Credit Card Number:", credit_card_number)
print("Hidden Credit Card Number:", hidden_card)
