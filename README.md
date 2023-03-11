# YOLO_for_Pedestrian_Detection  

## **就这样吧，哈哈哈**	:relaxed:  

![](https://img.shields.io/badge/author-Picaun-orange)

## 目录  
 - [前言](#前言)
 - [论文研究思路及工作方法](#论文研究思路及工作方法)
    - [总体目标和方法](#总体目标和方法)
    - [研究设计类型](#研究设计类型)
    - [总体群体和抽样方法](#总体群体和抽样方法)
    - [数据收集方法](#数据收集方法)
    - [数据收集程序](#数据收集程序)
    - [数据分析策略](#数据分析策略)
    - [结论和建议](#结论和建议)
    
## 前言  
>目标检测是计算机视觉中的一个重要研究方向，它的目的是在图像或视频中定位和识别出感兴趣的物体。目标检测在许多领域有着广泛的应用，如安防监控、自动驾驶、医学影像分析等。目标检测算法可以分为两类：一类是基于区域提议的方法，如R-CNN系列；另一类是基于回归的方法，如YOLO系列。基于区域提议的方法通常需要两个阶段：首先生成候选区域，然后对每个区域进行分类和回归。这种方法虽然可以达到较高的精度，但是速度较慢，不适合实时应用。基于回归的方法则只需要一个阶段：直接从图像中预测出物体的类别和位置。这种方法具有速度快、简单易实现等优点，但是精度相对较低。  
YOLO v4是一种基于回归的目标检测算法，它在2020年由Bochkovskiy等人提出，是YOLO v3算法的改进版。YOLO v4主要使用了一种新的CNN架构CSPNet来提高特征提取能力，并且引入了一种基于k-means聚类的方法来生成锚框。YOLO v4在COCO2017数据集上达到了45.5% mAP和65 FPS（mAP表示平均精度，FPS表示每秒处理帧数），表现出了优异的速度和精度。  
YOLO v4算法是当前最先进的实时对象检测模型之一，在COCO数据集上取得了很高的平均精度 (AP) 和帧率精度 (FPS)。然而，YOLO v4算法也存在一些不足之处或可以改进之处。例如，在卷积计算量和模型参数量方面还有较大优化空间；在损失函数方面还可以考虑更多因素来提高检测精度；在多目标跟踪方面还需要结合其他算法来实现。  
本毕业设计以YOLO v4算法为基础，在COCO2017行人数据集上进行测试，并对其进行改进优化。具体地说，在卷积层上使用深度分离卷积替换原始YOLO算法中使用到普通卷积层来降低计算量与参数量；在损失函数上通过对比使用GIoU、DIoU、CIoU作为损失函数对检测精度影响并选择合适损失函数；最后利用SORT算法实现行人跟踪功能。本毕业设计旨在提高YOLO v4算法在行人检测与跟踪任务上表现，并探索其在实际场景中应用潜力。

## 论文研究思路及工作方法  
### 总体目标和方法  
>本研究旨在利用YOLO v4算法，测试COCO2017行人数据集性能表现，并根据测试结果，对YOLO算法的检测速度和精度两个方面进行改进。本研究采用定量的研究范式，使用计算机视觉和深度学习的相关技术。  

### 研究设计类型  
>本研究选择实验设计作为研究设计类型，通过对比不同版本的YOLO算法在同一数据集上的检测效果，评估其优劣，并提出改进方案。  

### 总体群体和抽样方法  
>本研究使用COCO2017行人数据集作为总体群体，该数据集包含118287张训练图像和5000张验证图像，共有117266个行人实例。本研究使用全样本法，即将所有图像都用于训练或验证。  

### 数据收集方法  
>本研究使用YOLO v4算法作为数据收集方法，分别在COCO2017行人数据集上进行训练和验证，并记录其检测速度（FPS）和精度（mAP）等指标。  

### 数据收集程序  
本研究遵循以下步骤进行数据收集：  
>1、下载并安装YOLO v4算法的源代码及依赖库；  
2、下载并解压COCO2017行人数据集，并将其转换为适合YOLO算法输入的格式；  
3、修改配置文件中的相关参数，如类别数、锚框尺寸、学习率、批量大小等；  
4、使用GPU加速运行训练脚本，并保存模型权重文件；  
5、使用GPU加速运行验证脚本，并输出检测结果及评估指标；  
6、根据测试结果，对YOLO算法进行改进:  
>>1、 使用深度分离卷积替换原始YOLO算法的普通卷积来降低卷积计算量和模型参数量；  
2、 对比使用GIoU、DIoU、CIoU作为损失函数对检测精度的影响，并设计出合适的损失函数；  
3、 利用SORT算法，在检测结果基础上实现行人跟踪。  
4、 对改进后的YOLO算法重复上述训练和验证过程，并与原始版本进行对比分析。  

### 数据分析策略  
>本研究使用统计分析软件（如Excel或SPSS）对收集到的数据进行处理和分析，主要包括以下内容：  
>>1、描述性统计分析：计算不同版本的YOLO算法在COCO2017行人数据集上的平均检测速度（FPS）和平均精度（mAP），并绘制相应的柱状图或折线图；  
2、推断性统计分析：使用t检验或ANOVA等方法比较不同版本的YOLO算法在COCO2017行人数据集上的检测速度和精度是否存在显著差异，并计算相应的p值；  
3、结果解释和讨论：根据数据分析结果，解释并讨论YOLO算法的优缺点，以及改进方案的有效性和局限性，同时结合相关文献进行对比和支持；  

### 结论和建议  
>总结本研究的主要发现和贡献，指出本研究的局限性和不足，以及提出未来研究的方向和建议。  

## 参考文献
[1][Redmon J, Divvala S, Girshick R, et al. You only look once: Unified, real-time object detection[C]. Proceedings of the IEEE conference on computer vision and pattern recognition, 2016: 779-788](https://arxiv.org/pdf/1506.02640.pdf "You only look once: Unified, real-time object detection")  
[2][ZJiang P, Ergu D, Liu F, et al. A Review of Yolo algorithm developments[J]. Procedia Computer Science, 2022, 199: 1066-1073](https://pdf.sciencedirectassets.com/280203/1-s2.0-S1877050922X00021/1-s2.0-S1877050922001363/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDb5remvZVhCZc5XSYxKtjRzEf0XjWztUpobNypmO3oAwIgD%2BVubCdQRyMyjbZpfRfa5%2ByPmVWYcT4fsTYPqn5YEigqvAUIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAFGgwwNTkwMDM1NDY4NjUiDGd%2BtUPcT7sJuNBAlSqQBV0RBxWdeH%2BNiwxWXo8VcLflNW7halzr2PHgG6Epmi%2BKkncm9aN1yhcs%2FjW%2FvXT%2FtGRUvox6CCHfTmHfHL7QXoa9aUSQQh6rY%2BFy3nJs1UETs57vNlkEQr%2Bk%2FrQ67tppNoQO8IlEtCPjJrIx0UCZqsISblnXUVGW5aeVZy4RPAOHFNShSrGuChSRtj1rJFa8pQwVUI%2FdACxye2rN04gXwmZDxTsL7d3%2Bdb7pQHRZjsDkH7QMkePzCeHndVXMXN5E1Is7uCTWfRUGGVwC1HZPZBCmM6AIn1%2B4X0UXSGTk8WTmurJ3oqxEJfs1lTOCYcTNqmMeavxUi1QDvgfMNKKWIU2K7sGlSVhQZkmAZ5o8%2B23Wlr6xgnsOiRai8LvZdBuaNbRze%2Fg3VOL%2FU6qyDBoxoTmAGOJ0iGJuCLAdx1hVfwoKGg3QbTm18yfZ9MmR7hecPHDlFHjz2JdoJsYKgV4LZQybBsrWFVGMf08uw0KW3%2BQUhOhXYU2UeCLz%2FWyunaRiGg28lWxqkrEyDvmxEzO8iJH0egebMfKt5Eaulma1gDnLdU1Nc%2Fj%2BXLJIV9I1mKOtXSnb3nVwWUmz1W1CNSIWTZaFBCkEW8mnYEKsVThvHKtMRn7YKyDUSW9a0128jnH82Np25FXNO5VVYwMyEBmC4qVRY5vCgFgd1ruwEk0EXFX%2BVWQVkVnTtgoAj3UCnGvt0FU13Qbdv6z6LQ8%2Fv24MVoT6yc0jC6KhaJz0FvhyyrREY1hVX42xW8YuRYi5Jd7leN%2FF9u8q9D6rIX42ADiluMorTgh%2FVesTCMhcdwOE5CwQCPNp74R4sGIiLyUOojfJUobBi92huzog%2BTfP1GVPqZbLpxwaHB2yujlcGaLAGcO2MJGfsqAGOrEB3ijHFB0YTmvlfxYfBPyCVm%2F%2F9d4ZKltJfObOiuGxI0Dx3HWVXCfGulkKS3S%2FFy3%2BPtSP3XNyXQ2rMRu1AjbwQ28i8gxu%2BNI3lsvwgORd3K6v2yvabc%2Buuhvyufv50%2BzhObGxvAwA9Myb4owLaJU7NlrhTyXAqh6gbVRe%2FiaDyt6UVlCZCKpueLPysCiiiX5ZINzWLCJfmpOo7YerLadrJgajykehkuzNmLvTBR3UdVr6&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230311T152442Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYSVHIXWWH%2F20230311%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=6bf0de080caf585677d943ef22725c7c8b558108ab307c68e61d455bc984b48b&hash=945591910a8141c899f1b5c3ef5e86f1c43b153f6987426fc368e4ad60529360&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S1877050922001363&tid=spdf-d58c47a6-6ae4-43c3-99a9-53baf1f63ebc&sid=24a04356791ad14c3a1b3c445ba161d7573agxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=0f115705535a060b5407&rr=7a64ce4f1cc62efd&cc=us "A Review of Yolo algorithm developments[J]. Procedia Computer Science")  
[回到顶部](#readme)