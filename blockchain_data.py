from solana.rpc.api import Client
from solders.pubkey import Pubkey  # Import Pubkey from solders

# Connect to Solana Testnet or Mainnet
client = Client("https://api.testnet.solana.com")

# Replace with your actual Program ID
program_id = Pubkey.from_string("GLnMY2xvTm9ioRRakSCPMExqvK995JETaFivpEtWuzpa")

# Get all accounts associated with your program
response = client.get_program_accounts(program_id)

# Extract the result from the response object
accounts = response.value  # `response.value` contains the actual result

# Print the program accounts
print("Program accounts:", accounts)
