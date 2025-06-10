import cv2

def pencil_sketch(image_path, output_path=None):
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to load image at {image_path}")
        return
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Invert the grayscale image
    inverted_gray = 255 - gray
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(inverted_gray, (21, 21), 0)
    
    # Invert the blurred image
    inverted_blur = 255 - blurred
    
    # Create the pencil sketch by blending grayscale and inverted blurred images
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)
    
    # Show the original and sketch images
    cv2.imshow('Original Image', img)
    cv2.imshow('Pencil Sketch', sketch)
    
    # Save the sketch image if output path is provided
    if output_path:
        cv2.imwrite(output_path, sketch)
        print(f"Pencil sketch saved to {output_path}")
    
    # Wait until a key is pressed then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Replace 'input_image.jpg' with your image filename or full path
    input_image = 'input_image.png'  
    output_image = 'output_sketch.png'  # Optional: output file name
    
    pencil_sketch(input_image, output_image)
