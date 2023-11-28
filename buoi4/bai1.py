import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageSmoothingApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Tạo khung hiển thị ảnh
        self.image_frame = tk.Frame(window)
        self.image_frame.pack(fill=tk.BOTH, expand=True)

        # Tạo nút chọn ảnh
        self.btn_select_image = tk.Button(window, text="Select Image", command=self.load_image)
        self.btn_select_image.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.window.mainloop()

    def load_image(self):
        # Mở cửa sổ chọn tệp
        filename = filedialog.askopenfilename(title ='open')
        if filename:
            # Đọc ảnh
            self.img = cv2.imread(filename)
            self.display_image(self.img, 'Original Image')

            # Áp dụng bộ lọc làm mịn
            smooth_img = cv2.GaussianBlur(self.img, (5, 5), 0)
            self.display_image(smooth_img, 'Smooth Image')

    def display_image(self, img, title):
        # Chuyển đổi ảnh từ BGR sang RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Chuyển đổi ảnh OpenCV thành ảnh PIL
        img = Image.fromarray(img)

        # Chuyển đổi ảnh PIL thành ảnh Tkinter
        imgtk = ImageTk.PhotoImage(image=img)

        # Tạo một khung mới và hiển thị ảnh
        frame = tk.Frame(self.image_frame)
        frame.pack(side=tk.LEFT, padx=10, pady=10)

        label = tk.Label(frame, text=title)
        label.pack()

        canvas = tk.Canvas(frame, width=img.width, height=img.height)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)

        # Lưu lại ảnh Tkinter để tránh bị garbage collector xóa
        canvas.image = imgtk

if __name__ == "__main__":
    ImageSmoothingApp(tk.Tk(), "Image Smoothing App")
