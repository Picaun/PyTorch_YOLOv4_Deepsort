代码执行顺序应当为：（如果要将带person标签的图片分离出来）
	origin_coco_to_yolo.py-->select_person.py-->person_coco_to_yolo.py-->generate_path.py
说明：
	origin_coco_to_yolo.py与person_coco_to_yolo.py文件都是用于将coco数据集的json文件转换为yolo所需要的格式

	person_coco_to_yolo.py实际上就是origin_coco_to_yolo.py文件里面改了一下地址，自行改改还能生成其他类别的，select_person.py文件同理

	select_person.py文件是从官方的coco2017数据集分离出person标签的图片并生成对应的json文件

	generate_path.py文件是生成本项目所需的train2017.txt val2017.txt

注意：
	应当自行设定脚本文件中的目标路径，当前脚本中的设定都是以前运行时的设定
	如果想要训练所有类型，只需要origin_coco_to_yolo.py-->generate_path.py