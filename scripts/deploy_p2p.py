# Import.
from brownie import P2PPlatform, accounts
from scripts.helpers import (
    publish_source,
    get_increased_gas_price,
    get_account_admin_p2p,
    get_account_control_p2p,
    ADMIN_P2P
)


# Deploy.
def deploy_p2p():
    account = get_account_admin_p2p();
    incresed_gas_price = get_increased_gas_price();
    p2p = P2PPlatform.deploy(
        ADMIN_P2P,
        ADMIN_P2P,
        {"from": account, "gas_price": incresed_gas_price},
        publish_source=publish_source(),
    );
    return p2p;


# Main.
def main():
    p2p = deploy_p2p();
    print(p2p);
    return p2p;
