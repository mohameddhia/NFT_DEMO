from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from scripts.deploy_and_create import deploy_and_create
from brownie import network
import pytest


def test_can_create_simple_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    simpleCollectible = deploy_and_create()
    assert simpleCollectible.ownerOf(0) == get_account()
    
