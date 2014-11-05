# Mini-project #6 - Blackjack

import simpleguitk as simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = "Hit or Stand?"
player_score = 0
dealer_score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)


# define hand class
class Hand:
    def __init__(self):
        self.cards = []  # create Hand object

    def __str__(self):
        result = ""
        for card in self.cards:
            result += " " + card.__str__()

        return "Hand contains" + result  # return a string representation of a hand

    def add_card(self, card):
        self.cards.append(card)  # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        has_ace = False

        for card in self.cards:
            rank = card.get_rank()
            value += VALUES[rank]

            if rank == 'A':
                has_ace = True  
         
        if value < 11 and has_ace:
            value += 10

        return value  # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        for card in self.cards:
            card.draw(canvas, pos)
            pos[0] += 40  # draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []

        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank)) # create a Deck object

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.cards)  # use random.shuffle()

    def deal_card(self):
        return self.cards.pop(0) # deal a card object from the deck
    
    def __str__(self):
        result = ""
        for card in self.cards:
            result += " " + card.__str__()

        return "Deck contains" + result  # return a string representing the deck


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, dealer_score

    # your code goes here
    if in_play:
        outcome = "You lost because of re-deal! New deal?"
        dealer_score += 1
        in_play = False
    else:
        deck = Deck()
        outcome = "Hit or Stand?"
        
        deck.shuffle()

        player_hand = Hand()
        dealer_hand = Hand()

        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())

        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
            
        in_play = True


def hit():
    global outcome, in_play, dealer_score
    # if the hand is in play, hit the player
    if in_play:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())

    # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            outcome = "You have been busted. New deal?"
            dealer_score += 1
            in_play = False


def stand(): 
    global outcome, in_play, dealer_score, player_score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())
    
    if in_play:
        if dealer_hand.get_value() > 21:
            outcome = "Dealer busted. Congratulations!"
            player_score += 1
            in_play = False
        else:
            if dealer_hand.get_value() >= player_hand.get_value() or player_hand.get_value() > 21:
                outcome = "Dealer wins. New deal?"
                dealer_score += 1
                in_play = False
            else:
                outcome = "You won. New deal?"
                player_score += 1
                in_play = False


# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below        
    canvas.draw_text("Blackjack", [220, 50], 50 ,"Navy")
    canvas.draw_text(outcome, [10, 100], 30 ,"White")

    player_hand.draw(canvas, [100, 300])
    dealer_hand.draw(canvas, [100, 150])
    
    canvas.draw_text("Dealer: %s" % dealer_score, [10, 150], 20, "Black")
    canvas.draw_text("Player: %s" % player_score, [10, 300], 20, "Black")
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (136,198), CARD_BACK_SIZE)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 400)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 100)
frame.add_button("Hit",  hit, 100)
frame.add_button("Stand", stand, 100)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()

# remember to review the grade rubric