from PIL import Image

from detector import detect_faces
from visualization_utils import show_bboxes

if __name__ == '__main__':
    img = Image.open('images/office1.jpg')
    bounding_boxes, landmarks = detect_faces(img)
    show_bboxes(img, bounding_boxes, landmarks)
