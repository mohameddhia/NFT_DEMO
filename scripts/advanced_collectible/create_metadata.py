from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import BREED_MAPPING, get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path


def main():
    advance_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advance_collectible.tokenCounter()
    print(f"you have created {number_of_advanced_collectibles} collectibles!")
    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advance_collectible.tokenIdToBreed(token_id))
        metadata_filename = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        print(metadata_filename)
        collectible_metadata = metadata_template
        if Path(metadata_filename).exists:
            print(f"{metadata_filename} already exists Deletes to override")
        else:
            print(f"creating metadata file :{metadata_filename}")
            collectible_metadata["name"] = breed
            collectible_metadata["description"] = f"An adorable {breed} pup!"
            # image_uri = upload_to_ipfs()
            # collectible_metadata["image"] = image_uri


def upload_to_ipfs(filepath):
    pass
