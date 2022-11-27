""""
Suppose we wanted to create a new type to represent hands in blackjack. One thing we might want to do with this type is overload the comparison operators like > and <= so that we could use them to check whether one hand beats another. e.g. it'd be cool if we could do this:

>>> hand1 = BlackjackHand(['K', 'A'])
>>> hand2 = BlackjackHand(['7', '10', 'A'])
>>> hand1 > hand2
True
Well, we're not going to do all that in this question (defining custom classes is a bit beyond the scope of these lessons), but the code we're asking you to write in the function below is very similar to what we'd have to write if we were defining our own BlackjackHand class. (We'd put it in the __gt__ magic method to define our custom behaviour for >.)

Fill in the body of the blackjack_hand_greater_than function according to the docstring.
"""
def blackjack_hand_greater_than(hand_1, hand_2):
    def value(arr):
        total = 0
        ace = 0
        for card in arr:
            if card == 'A':
                ace += 1
            elif card == "J" or card == "K" or card == "Q":
                total += 10
            else:
                total += int(card)
        total += ace
        while ace > 0 and (total + 10) <= 21:
            total += 10
            ace -= 1
        return total

    max_limit = 21
    hand1 = value(hand_1)
    hand2 = value(hand_2)
    return False if hand1 > max_limit else (hand1 > hand2 or hand2 > max_limit)


hand_1 = ['J', 'A']
hand_2 = ["6"]
print(blackjack_hand_greater_than(hand_1, hand_2))
