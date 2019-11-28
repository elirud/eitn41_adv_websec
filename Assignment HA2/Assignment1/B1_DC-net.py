sa_val = input("Please enter shared 16-bit secret from Alice (SA): ")
da_val = input("Please enter Alice's data to be broadcasted (DA): ")
sb_val = input("Please enter shared 16-bit secret from Bob (SB):")
db_val = input("Please enter Bob's data to be broadcasted (DB): ")
opt_m_val = input("Please enter optional 16-bit message to send anonymously (M): ")
send_opt_val = input("Please enter bit value for sending optional message (0 or 1): ")

xor_val = bin(bin(int(sa_val, 16)^bin(int(sb_val, 16)))

for i in range (16):
