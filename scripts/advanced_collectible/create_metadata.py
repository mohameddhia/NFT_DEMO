from brownie import AdvancedCollectible
from scripts.helpful_scripts import BREED_MAPPING, get_breed


def main():
    advance_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advance_collectible.tokenCounter()
    print(f"you have created {number_of_advanced_collectibles} collectibles!")
    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advance_collectible.tokenIdToBreed(token_id))
