import os

folder_path = '/coco/person_only/images/val2017' # 指定文件夹路径
output_file = '/coco/val2017.txt' # 输出文件名

#folder_path = '/coco/person_only/images/train2017'
#output_file = '/coco/train2017.txt'

with open(output_file, 'w') as f:
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'): # 检查文件扩展名
                f.write(os.path.join(root, file) + '\n')
