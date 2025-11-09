import json

def extract_lsb_hex_message(json_file):
    """
    Extract 16-character hex message from image using LSB steganography.
    
    Process:
    1. Load JSON with RGB pixel values (10x10 = 100 pixels)
    2. Extract LSB from R, G, B channels (row by row, left to right)
    3. Concatenate all bits
    4. Convert every 8 bits to ASCII character
    5. Return first 16 characters as hex string
    """
    # Load JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Extract pixels - handle nested structure: rows of pixels
    pixels = data.get('pixels', [])
    
    # Extract LSB bits from each pixel (row by row, left to right)
    # Order: R -> G -> B for each pixel
    bits = []
    
    # Process each row
    for row in pixels:
        # Process each pixel in the row (left to right)
        for pixel in row:
            # Pixel format: [R, G, B]
            r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
            
            # Extract LSB (rightmost bit) from each channel
            bits.append(r & 1)  # LSB of Red
            bits.append(g & 1)  # LSB of Green
            bits.append(b & 1)  # LSB of Blue
    
    # Convert bits to binary string
    binary_string = ''.join(str(bit) for bit in bits)
    
    print(f"Total bits extracted: {len(binary_string)}")
    print(f"First 64 bits: {binary_string[:64]}")
    
    # Convert every 8 bits to ASCII character
    message_chars = []
    for i in range(0, len(binary_string), 8):
        if i + 8 <= len(binary_string):
            byte_str = binary_string[i:i+8]
            char_code = int(byte_str, 2)
            message_chars.append(chr(char_code))
    
    # Join characters to form message
    message = ''.join(message_chars)
    
    print(f"ASCII message (first 16 chars): {message[:16]}")
    print(f"ASCII message (first 8 chars): {message[:8]}")
    
    # Convert first 8 characters to 16-character hex string
    # Each ASCII character becomes 2 hex digits
    hex_message = ''.join(format(ord(c), '02x') for c in message[:8])
    
    # Ensure exactly 16 characters
    hex_message = hex_message[:16].lower()
    
    return hex_message, message, binary_string

# Main execution
if __name__ == "__main__":
    json_file = 'stego_image.json'
    
    print("LSB Steganography Extraction Tool")
    print("=" * 60)
    print(f"Processing: {json_file}\n")
    
    try:
        hex_msg, ascii_msg, binary = extract_lsb_hex_message(json_file)
        
        print(f"\n{'='*60}")
        print(f"EXTRACTED 16-CHARACTER HEX MESSAGE: {hex_msg}")
        print(f"{'='*60}")
        print(f"\nDetails:")
        print(f"  ASCII message: {ascii_msg[:16]}")
        print(f"  Total bits: {len(binary)}")
        print(f"  Total bytes: {len(binary) // 8}")
        
    except FileNotFoundError:
        print(f"File not found: {json_file}")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
