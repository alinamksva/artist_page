import os
from PIL import Image

# Настройки
input_folder = "/Users/alinamaksimova/Desktop/images"         # Папка с оригинальными изображениями
output_folder = "/Users/alinamaksimova/Documents/test_gitpages/images"      # Куда сохранять результат
base_width = 500                     # Новая ширина (высота подгонится пропорционально)

# Создаём выходную папку, если нет
os.makedirs(output_folder, exist_ok=True)

# Перебираем файлы в папке
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Вычисляем новую высоту, сохраняя пропорции
        w_percent = base_width / float(img.size[0])
        h_size = int((float(img.size[1]) * float(w_percent)))
        resized_img = img.resize((base_width, h_size), Image.Resampling.LANCZOS)

        # Сохраняем в output_folder
        output_path = os.path.join(output_folder, filename)
        if resized_img.mode == "RGBA":
            resized_img = resized_img.convert("RGB")
        resized_img.save(output_path)

        print(f"✔ {filename} resized to {base_width}x{h_size}")