import cv2
import os

def detect_microplastics(image_path, output_folder="static"):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Simple thresholding to detect particles (example)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    count = len(contours)

    # Annotate image
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Save annotated image
    annotated_filename = os.path.join(output_folder, f"annotated_{os.path.basename(image_path)}")
    cv2.imwrite(annotated_filename, img)

    return count, annotated_filename

