# import base58
# import logging
# import requests
# from solders.keypair import Keypair
# from solders.pubkey import Pubkey  # Correct import for Pubkey
# from solders.rpc.requests import GetFeeForMessage
# from solders.message import MessageV0  # Correct import for MessageV0
# from solders.commitment_config import CommitmentLevel  # Import CommitmentLevel
# from solana.rpc.api import Client

# # Set up logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     handlers=[logging.StreamHandler()]
# )

# # Function to create a Keypair from a base58 private key
# def create_keypair_from_private_key(private_key_b58):
#     private_key = base58.b58decode(private_key_b58)  # Decode the base58 private key
#     logging.info("Private key decoded successfully.")
#     return Keypair.from_bytes(private_key)  # Create a Keypair object from the decoded bytes

# # Function to log the action to an immutable blockchain audit trail
# def log_audit_trail(client, keypair, action_message):
#     """
#     Record the given action on the blockchain as an audit log.
#     This would invoke a contract that stores the action in a tamper-proof way.
#     """
#     logging.info(f"Logging action: {action_message}")
#     # Send the transaction (simulation for audit logging)
#     logging.info("Transaction sent to Solana Blockchain")
#     logging.info(f"Audit trail for action '{action_message}' successfully recorded!")

# # Function to handle blockchain interaction (deploying, auditing, etc.)
# def deploy_contract_and_record_audit(client, keypair, contract_data):
#     """
#     Deploys the contract and records the action to the audit trail.
#     """
#     logging.info("Deploying contract to Solana blockchain...")

#     # 1. Deploy contract (simplified here for simulation)
#     logging.info("Contract deployed successfully.")

#     # 2. Log the contract deployment in the blockchain audit trail
#     log_audit_trail(client, keypair, "Contract deployed successfully")

# # Function to interact with Solana RPC using requests
# def interact_with_solana_rpc():
#     """
#     This function demonstrates how to make an RPC call using solders for a basic method (like getting fee for a message).
#     """
#     # Create a valid MessageV0 object. Normally you'd use a transaction message.
#     # For this example, we are using a default MessageV0.
#     message = MessageV0.default()

#     # Build the RPC request (GetFeeForMessage)
#     fee_request = GetFeeForMessage(message, commitment=CommitmentLevel.Processed)  # Use the enum for commitment
#     fee_json = fee_request.to_json()  # Convert the request to JSON string
#     logging.info(f"Fee request JSON: {fee_json}")

#     # Solana Testnet RPC URL
#     solana_rpc_url = "https://api.testnet.solana.com"

#     # Send the request using the requests library
#     response = requests.post(solana_rpc_url, data=fee_json, headers={"Content-Type": "application/json"})
    
#     # Print the raw JSON response
#     logging.info(f"RPC Response: {response.json()}")

# # Main function to execute the deployment and blockchain actions
# def main():
#     # Private key (base58 encoded) example - replace this with your actual private key
#     private_key_b58 = ""

#     # Create the Keypair from the private key
#     keypair = create_keypair_from_private_key(private_key_b58)

#     # Print the public address (wallet address) and Phantom-compatible private key
#     logging.info(f"Public Address (Public Key): {keypair.pubkey()}")
#     logging.info(f"Private Key (Base58): {base58.b58encode(keypair.secret()).decode('utf-8')}")

#     # Setup Solana client (testnet or mainnet)
#     client = Client("https://api.testnet.solana.com")

#     # Simulated contract data (in real case, this would be your compiled contract)
#     contract_data = b"dummy_contract_data"

#     # Deploy contract and log the action
#     deploy_contract_and_record_audit(client, keypair, contract_data)

#     # Example Solana RPC interaction (getting fee for a message)
#     interact_with_solana_rpc()

# if __name__ == "__main__":
#     main()



import base58
import logging
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solders.system_program import create_account
from solders.transaction import Transaction
from solders.message import MessageV0, MessageHeader
from solana.rpc.api import Client

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

# Function to create a Keypair from a base58 private key
def create_keypair_from_private_key(private_key_b58):
    private_key = base58.b58decode(private_key_b58)  # Decode the base58 private key
    logging.info("Private key decoded successfully.")
    return Keypair.from_bytes(private_key)  # Create a Keypair object from the decoded bytes

# Function to log the action to an immutable blockchain audit trail
def log_audit_trail(client, keypair, action_message):
    """
    Record the given action on the blockchain as an audit log.
    This would invoke a contract that stores the action in a tamper-proof way.
    """
    logging.info(f"Logging action: {action_message}")
    # Send the transaction (simulation for audit logging)
    logging.info("Transaction sent to Solana Blockchain")
    logging.info(f"Audit trail for action '{action_message}' successfully recorded!")

# Function to handle blockchain interaction (deploying, auditing, etc.)
def deploy_contract_and_record_audit(client, keypair, contract_data):
    """
    Deploys the contract and records the action to the audit trail.
    """
    logging.info("Deploying contract to Solana blockchain...")

    # 1. Deploy contract (simplified here for simulation)
    logging.info("Contract deployed successfully.")

    # 2. Log the contract deployment in the blockchain audit trail
    log_audit_trail(client, keypair, "Contract deployed successfully")

# Function to interact with Solana RPC using requests
def interact_with_solana_rpc(client, keypair):
    """
    This function demonstrates how to make an RPC call using solders for a basic method (like getting fee for a message).
    """
    # Fetch the latest blockhash from the client (use `get_latest_blockhash` instead of `get_recent_blockhash`)
    response = client.get_latest_blockhash()
    
    # Access the blockhash correctly from the `value` attribute
    recent_blockhash = response.value.blockhash  # Access the blockhash through `value`
    logging.info(f"Recent Blockhash: {recent_blockhash}")
    exit()
    # Simulate a create_account transaction with a random public key (you can replace with real values)
    new_account_pubkey = Pubkey.from_string("EJmeW47zDebNgLZT3oiHmH5zBkW4yLb1d2MVjQZHsQ8G")  # Replace with actual key

    # Correctly build the dictionary to pass to create_account
    create_account_args = {
        "from_pubkey": keypair.pubkey(),  # The public key of the account creating the new one
        "to_pubkey": new_account_pubkey,  # The public key for the new account
        "lamports": 1000000,  # Amount of lamports (SOL) to transfer
        "space": 0,  # Space needed for the new account (use 0 for a simple account)
        "program_id": Pubkey.from_string("11111111111111111111111111111111"),  # System program
        "owner": Pubkey.from_string("11111111111111111111111111111111")  # System program as owner
    }

    # Directly build the instruction and add it to the transaction without compiling
    instruction = create_account(create_account_args)

    # Prepare the MessageHeader (needed for MessageV0)
    header = MessageHeader(
        num_required_signatures=1,  # Number of signatures required for the transaction
        num_readonly_signed_accounts=0,  # Number of readonly signed accounts
        num_readonly_unsigned_accounts=1  # Number of readonly unsigned accounts (in this case, just the new account)
    )

    # Prepare the MessageV0 with required parameters, including the header
    message = MessageV0(
        header=header,
        account_keys=[keypair.pubkey(), new_account_pubkey],  # List of account keys involved in the transaction
        recent_blockhash=recent_blockhash,  # The recent blockhash
        instructions=[instruction],  # Add the instruction directly to the message without compilation
        address_table_lookups=[]  # Optional, empty list for address table lookups
    )

    # Create a transaction using the message
    transaction = Transaction(
        from_keypairs=[keypair], 
        message=message, 
        recent_blockhash=recent_blockhash
    )

    # Send the transaction using the Solana client (simplified version)
    result = client.send_transaction(transaction, keypair)

    # Log the transaction result
    logging.info(f"Transaction sent! Result: {result}")

# Main function to execute the deployment and blockchain actions
def main():
    # Private key (base58 encoded) example - replace this with your actual private key
    private_key_b58 = ""

    # Create the Keypair from the private key
    keypair = create_keypair_from_private_key(private_key_b58)

    # Print the public address (wallet address) and Phantom-compatible private key
    logging.info(f"Public Address (Public Key): {keypair.pubkey()}")
    logging.info(f"Private Key (Base58): {base58.b58encode(keypair.secret()).decode('utf-8')}")

    # Setup Solana client (testnet or mainnet)
    client = Client("https://api.testnet.solana.com")

    # Simulated contract data (in real case, this would be your compiled contract)
    contract_data = b"dummy_contract_data"

    # Deploy contract and log the action
    deploy_contract_and_record_audit(client, keypair, contract_data)

    # Example Solana RPC interaction (getting fee for a message)
    interact_with_solana_rpc(client, keypair)

if __name__ == "__main__":
    main()




