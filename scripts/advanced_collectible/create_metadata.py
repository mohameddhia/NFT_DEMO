import json
from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import BREED_MAPPING, get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests


def main():
    advance_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advance_collectible.tokenCounter()
    print(f"you have created {number_of_advanced_collectibles} collectibles!")
    for token_id in range(number_of_advanced_collectibles):
        # breed = get_breed(advance_collectible.tokenIdToBreed(token_id))
        breed = get_breed(1)
        metadata_filename = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        print(metadata_filename)
        collectible_metadata = metadata_template
        if Path(metadata_filename).exists():
            print(f"{metadata_filename} already exists Deletes to override")
        else:
            print(f"creating metadata file :{metadata_filename}")
            collectible_metadata["name"] = breed
            collectible_metadata["description"] = f"An adorable {breed} pup!"
            image_path = "./img/" + breed.lower().replace("_", "-") + ".png"
            image_uri = upload_to_ipfs(image_path)
            collectible_metadata["image"] = image_uri
            with open(metadata_filename, 'w') as file:
                json.dump(collectible_metadata,file)
            upload_to_ipfs(metadata_filename)


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:

        image_binary = fp.read()
        # Upload to IPFS
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
