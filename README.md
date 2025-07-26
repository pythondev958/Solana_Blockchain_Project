# **Solana Blockchain Project - Audit Trail and Smart Contract Deployment**

This project integrates **Solana Blockchain** with a Python script for creating a **Phantom-compatible keypair**, deploying smart contracts, and recording **immutable audit trails** on the blockchain. The project is designed to meet legal compliance needs, including tamper-proof logging of actions and system events for enterprise-grade security and data privacy.

---

## **Project Overview**

This project enables blockchain-based audit trails, ensuring that all actions in the system are recorded in a tamper-proof manner. It uses the Solana blockchain to store these records, ensuring that the logs cannot be altered after they are committed. These logs play a critical role in **legal compliance auditing**, **trust-building**, and **forensic analysis** of actions within the system.

### **Key Features**

- **Immutable Blockchain Audit Trails**: The system logs user and system actions onto the Solana blockchain to ensure data integrity.
- **Compliance with Legal Requirements**: Designed to handle tamper-proof record-keeping and create an auditable trail for compliance verification.
- **Phantom-Compatible Keypair**: Generates Solana-compatible public and private keys in a Phantom wallet-compatible format.
- **Smart Contract Deployment**: Automates smart contract deployment using Python, enabling the blockchain actions to be recorded.

---

## **Installation Guide**

To set up this project on your local machine, follow these steps:

### **1. Clone the Repository**

```bash
git clone https://github.com/pythondev958/Solana_Blockchain_Project.git
cd Solana_Blockchain_Project
2. Set Up Python Virtual Environment
Make sure you have Python 3.8+ installed. Then, create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
3. Install Project Dependencies
Once inside the virtual environment, install the necessary dependencies:

bash
Copy
Edit
pip install -r requirements.txt
The requirements.txt file should include the necessary libraries, such as solders for Solana interaction and other dependencies. If it doesn’t exist, you can manually install:

bash
Copy
Edit
pip install solders base58
4. Setup Solana CLI
Make sure you have Solana CLI installed on your machine. If not, follow the official installation guide.

After installation, verify that Solana CLI is working:

bash
Copy
Edit
solana --version
Usage
1. Create Phantom-Compatible Keypair
The project uses Solana's Python SDK to create a Phantom-compatible keypair. The script generates a wallet that can be used in Phantom, which can be accessed using the generated public and private keys.

bash
Copy
Edit
python deploy_contract.py
This will print:

vbnet
Copy
Edit
Wallet Address (Public Key): <Generated Public Key>
Phantom-Compatible Private Key: <Generated Private Key>
2. Deploy Smart Contract
To deploy a smart contract, first ensure that your Rust contract is compiled and ready. Then, use the Python script to deploy the contract to the Solana blockchain:

Compile the Smart Contract: Use cargo build to build your Rust program.

Deploy the Contract: Run the Python deployment script to deploy your contract:

bash
Copy
Edit
python deploy_contract.py
Smart Contract Code
The smart contract is written in Rust and deployed to Solana using the Solana Program Library (SPL). Below is a simple contract that logs information:

rust
Copy
Edit
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    pubkey::Pubkey,
    msg,
};

entrypoint!(process_instruction);

fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    _instruction_data: &[u8],
) -> ProgramResult {
    msg!("Solana Smart Contract!");

    let accounts_iter = &mut accounts.iter();
    let _account = next_account_info(accounts_iter)?; 

    msg!("Program ID: {}", program_id);
    msg!("Account: {}", _account.key);

    Ok(())
}
Legal Compliance & Blockchain Audit Trail
Why Blockchain for Audit Trails?
Tamper-Proof Logs: Once actions are logged on the blockchain, they cannot be altered, providing a secure record of actions for legal auditing purposes.

Legal Compliance: The blockchain-based audit trail ensures that all data is compliant with legal standards and can be used in court for forensic analysis.

Enterprise-Grade Security: Leveraging Solana’s high throughput and low transaction costs, we can ensure secure, fast, and cost-effective record-keeping.

Contributing
We welcome contributions! If you would like to contribute to the project, please fork the repository and create a pull request with your changes.
