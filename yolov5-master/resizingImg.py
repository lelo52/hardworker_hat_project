import os
from PIL import Image


def convert_and_resize_images(folder_path, output_folder_path, size):
    # 출력 폴더가 존재하지 않으면 생성합니다.
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # 지원하는 파일 확장자 리스트
    supported_extensions = [".jpg", ".jpeg", ".jfif"]

    # 순차적으로 번호를 붙이기 위한 카운터
    count = 1

    for filename in os.listdir(folder_path):
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext in supported_extensions:
            image_path = os.path.join(folder_path, filename)
            try:
                with Image.open(image_path) as img:
                    # 이미지 리사이즈
                    img = img.resize(size, Image.ANTIALIAS)
                    # 새 파일명 생성
                    new_filename = f"image{count}.jpg"
                    new_image_path = os.path.join(output_folder_path, new_filename)
                    # 이미지를 jpg 형식으로 저장
                    img.save(new_image_path, 'JPEG')
                    print(f"Converted and resized {filename} to {new_filename}")
                    count += 1
            except Exception as e:
                print(f"Error processing {filename}: {e}")


# 사용 예제
folder_path = 'C:/Users/kimjiho/Documents/dataset_filth_balloon'
output_folder_path = 'C:/Users/kimjiho/Documents/resized_data_balloon'
size = (416, 416)  # 리사이즈할 크기

convert_and_resize_images(folder_path, output_folder_path, size)

