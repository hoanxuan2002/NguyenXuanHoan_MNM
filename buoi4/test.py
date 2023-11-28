import cv2
import numpy as np
from tkinter import filedialog
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

def smooth_image(image):
    # Lọc làm mịn ảnh bằng GaussianBlur
    blur = cv2.GaussianBlur(image, (5,5), 0)
    return blur

def edge_detection(image):
    # Tách biên ảnh bằng Canny
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return edges

def enhance_image(image):
    # Tăng cường độ sáng
    enhanced_img = cv2.convertScaleAbs(image, alpha=1.2, beta=50)
    return enhanced_img

def show_image(image, root):
    # Chuyển đổi ảnh OpenCV thành ảnh Tkinter
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)

    # Lưu trữ tham chiếu đến đối tượng ImageTk.PhotoImage
    root.image = image

    # Hiển thị ảnh
    img_label = Label(root, image=image)
    img_label.pack()

def main():
    # Tạo cửa sổ Tkinter
    root = Tk()
    root.image = None  # Khởi tạo thuộc tính image

    # Mở hộp thoại chọn tệp
    file_path = filedialog.askopenfilename()

    # Đọc ảnh
    img = cv2.imread(file_path)
    current_img = img  # Khởi tạo hình ảnh hiện tại

    # Tạo các nút cho các chức năng
    blur_button = Button(root, text="Smooth Image", command=lambda: show_image(smooth_image(current_img), root))
    edge_button = Button(root, text="Edge Detection", command=lambda: show_image(edge_detection(current_img), root))
    enhance_button = Button(root, text="Enhance Image", command=lambda: show_image(enhance_image(current_img), root))

    # Hiển thị các nút
    blur_button.pack()
    edge_button.pack()
    enhance_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
