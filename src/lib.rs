use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    pubkey::Pubkey,
    msg,
    system_instruction,
    system_program,
    rent::Rent,
    program_error::ProgramError,
};

entrypoint!(process_instruction);

/// This structure represents an audit trail entry
#[derive(Debug)]
pub struct AuditTrailEntry {
    pub action: String,      // Description of the action/event (e.g., "user login", "document signed")
    pub timestamp: u64,      // Timestamp of the action
    pub user: Pubkey,        // The user responsible for the action
    pub program_id: Pubkey,  // The program under which the action was performed
}

fn record_audit_trail(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    action: String,
    user: Pubkey,
) -> ProgramResult {
    let timestamp = Clock::get()?.unix_timestamp as u64;

    // Create an audit trail entry
    let audit_entry = AuditTrailEntry {
        action,
        timestamp,
        user,
        program_id: *program_id,
    };

    // Serialize the audit trail entry into bytes
    let serialized_data = bincode::serialize(&audit_entry).map_err(|_| ProgramError::InvalidInstructionData)?;

    // Store the audit trail in the first account data (for simplicity in this example)
    let account_info_iter = &mut accounts.iter();
    let account = next_account_info(account_info_iter)?;

    // Ensure the account has enough space to store the data
    let rent = Rent::get()?;
    if account.data_len() < serialized_data.len() {
        return Err(ProgramError::AccountDataTooSmall);
    }

    // Copy the serialized audit entry data to the account's data
    account.try_borrow_mut_data()?[..serialized_data.len()].copy_from_slice(&serialized_data);

    msg!("Audit trail recorded: {:?}", audit_entry);

    Ok(())
}

fn process_instruction(
    program_id: &Pubkey,  // Public key of the program
    accounts: &[AccountInfo],  // List of accounts involved in the transaction
    instruction_data: &[u8],  // Data passed with the instruction
) -> ProgramResult {
    msg!("Solana Smart Contract - Audit Trail!");

    // Extract the action and user public key from the instruction data
    if instruction_data.len() < 32 {
        return Err(ProgramError::InvalidInstructionData);
    }

    let user_pubkey = Pubkey::new(&instruction_data[0..32]);

    // Let's assume the rest of the instruction data is the action string (could be encoded as UTF-8)
    let action = String::from_utf8(instruction_data[32..].to_vec()).map_err(|_| ProgramError::InvalidInstructionData)?;

    // Record the audit trail entry
    record_audit_trail(program_id, accounts, action, user_pubkey)?;

    Ok(())
}
