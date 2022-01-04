from brownie import network, AdvancedCollectible
from brownie.network import account
import pytest
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_contract,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
import time


def test_can_create_advanced_collectible_integration():
    # deploy contract
    # create an NFT
    # get a random breed back
    # arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("test only for integration testing")
    # ACT
    advanced_collectible, creation_transaction = deploy_and_create()
    time.sleep(120)

    # Assert
    assert advanced_collectible.tokenCounter() > 0
