sa_val = int(input("Please enter shared 16-bit secret from Alice (SA): "), 16)
da_val = int(input("Please enter Alice's data to be broadcasted (DA): "), 16)
sb_val = int(input("Please enter shared 16-bit secret from Bob (SB): "), 16)
db_val = int(input("Please enter Bob's data to be broadcasted (DB): "), 16)
opt_m_val = int(input("Please enter optional 16-bit message to send anonymously (M): "), 16)
send_opt_val = int(input("Please enter bit value for sending optional message (0 or 1): "), 16)

xor_val = sa_val ^ sb_val

message_received = hex((xor_val ^ da_val) ^ db_val).lstrip('0x').upper().zfill(4)

data_sent = xor_val if send_opt_val == 0 else xor_val ^ opt_m_val
data_sent = hex(data_sent).lstrip('0x').upper().zfill(4)
print(data_sent) if send_opt_val == 1 else print(data_sent + message_received)

