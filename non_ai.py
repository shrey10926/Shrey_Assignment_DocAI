import cv2, os

def count_cell(img_name):

    image = cv2.imread(img_name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 40))

    horizontal_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    vertical_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=2)

    table_structure = cv2.add(horizontal_lines, vertical_lines)

    contours, hierarchy = cv2.findContours(table_structure, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    image_copy = image.copy()
    cv2.drawContours(image_copy, contours, -1, (0, 255, 0), 2)
    cv2.imshow('All Contours', image_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cell_count = 0
    min_area = 500
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > min_area:
            cell_count += 1

    print(f"Number of cells detected: {cell_count}")

result = count_cell(os.path.join("Images", "Table.JPG"))