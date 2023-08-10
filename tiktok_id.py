from datetime import datetime

def find_time_and_date(tiktok_id):
    # Convert the ID to a 64-bit integer
    tiktok_id_int = int(tiktok_id)
    
    # Perform a right bitwise shift of 32 bits
    shifted_bits = tiktok_id_int >> 32
    
    # Convert to decimal
    shifted_bits_decimal = int(shifted_bits)
    
    # Check if it's 10 digits long and starts with 1
    if len(str(shifted_bits_decimal)) == 10 and str(shifted_bits_decimal)[0] == '1':
        # Interpret as a Unix timestamp
        timestamp = datetime.fromtimestamp(shifted_bits_decimal)
        print(f'The timestamp for the TikTok ID {tiktok_id} is {timestamp}.')
    else:
        print(f'The TikTok ID {tiktok_id} does not seem to be valid.')

if __name__ == "__main__":
    while True:
        tiktok_id = input("Please enter the TikTok video ID (or type 'quit' to exit): ")
        
        if tiktok_id.lower() == 'quit':
            print("Exiting the app. Goodbye!")
            break
        
        find_time_and_date(tiktok_id)