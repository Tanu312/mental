from PIL import Image
import pytesseract

# Load the image
image_path = '/mnt/data/IMG-20240715-WA0019.jpg'
image = Image.open(image_path)

# Perform OCR on the image
ocr_result = pytesseract.image_to_string(image)

# Split the OCR result into lines
lines = ocr_result.split('\n')

# Initialize dictionaries to hold the labels and results
labels = []
results = []

# Process each line to extract labels and results
for line in lines:
    if ' ' in line:
        parts = line.split(' ')
        labels.append(parts[0].strip())
        results.append(' '.join(parts[1:]).strip())

# Combine the labels and results into a dictionary
data = {label: result for label, result in zip(labels, results)}

# Print the extracted labels and results
print("Labels and Results:")
for label, result in data.items():
    print(f"{label}: {result}")
