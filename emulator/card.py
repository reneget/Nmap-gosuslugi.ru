import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from crypto import generate_key, generate_entropy

class Card ():
    id_: int = 1
    secret: str = str(open('crypto/secret.txt', 'r').read())
    entropy: str = generate_entropy(16)
    pwd: str = generate_key(secret, entropy)[0]
    def get_card_info(self):
        return self.id_, self.entropy, self.pwd

def main():
    card = Card()
    print(card.get_card_info())

if __name__ == "__main__":
    main()
