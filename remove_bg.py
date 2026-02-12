import sys
import os

try:
    from rembg import remove
    from PIL import Image
    import io
except ImportError:
    print("Error: rembg not installed")
    sys.exit(1)

input_path = r'e:\WEB\CV WEB\profile.png'
output_path = r'e:\WEB\CV WEB\profile-nobg.png'

if not os.path.exists(input_path):
    print(f"Error: Input file {input_path} not found")
    sys.exit(1)

print(f"Processing {input_path}...")

try:
    with open(input_path, 'rb') as i:
        input_data = i.read()
        output_data = remove(input_data)
        
    with open(output_path, 'wb') as o:
        o.write(output_data)
        
    print(f"Success! Saved to {output_path}")

except Exception as e:
    print(f"Error processing image: {e}")
    sys.exit(1)
