import os
import xml.etree.ElementTree as ET

def convert_VOC_to_yolo(voc_dir, yolo_dir, classes):
    if not os.path.exists(yolo_dir):
        os.makedirs(yolo_dir)

    for file_name in os.listdir(voc_dir):
        if not file_name.endswith('.xml'):
            continue

        # pascal VOC_xml file 읽기(read)
        voc_file = os.path.join(voc_dir,file_name)
        tree = ET.parse(voc_file)
        root = tree.getroot()

        # image size 추출
        size = root.find('size')
        width = int(size.find('width').text)
        height = int(size.find('height').text)

        # YOLO annotation
        yolo_annotation = []

        for obj in root.findall('object'):
            class_name = obj.find('name').text
            if class_name not in classes:
                 continue
            class_id = classes.index(class_name)

            bndbox = obj. find('bndbox')

            xmin = int(bndbox.find('xmin').text)
            ymin = int(bndbox.find('ymin').text)
            xmax = int(bndbox.find('xmax').text)
            ymax = int(bndbox.find('ymax').text)

            # yolo format으로 변환
            x_center = (xmin + xmax) / 2.0 / width
            y_center = (ymax + ymin) / 2.0 / height

            bbox_width = (xmax - xmin) / width
            bbox_height = (ymax - ymin) / height

            yolo_annotation.append(f"{class_id} {x_center} {y_center} {bbox_width} {bbox_height}")

        # yolo_anntation file 쓰기
        yolo_file = os.path.join(yolo_dir, file_name.replace('.xml', '.txt'))
        with open(yolo_file, 'w') as f:
            f.write("\n".join(yolo_annotation))


classes = ["balloon"]
voc_dir = 'C:/Users/kimjiho/Documents/labeldata'
yolo_dir = 'C:/Users/kimjiho/Documents/labeldata'

convert_VOC_to_yolo(voc_dir, yolo_dir, classes)