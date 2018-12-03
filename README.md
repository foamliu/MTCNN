# MTCNN

下述论文预测部分的PyTorch实现：
[Joint Face Detection and Alignment using Multi-task Cascaded Convolutional Networks.](https://arxiv.org/abs/1604.02878)

## 模型

### 管道

级联框架管道包括三阶段多任务深度卷积网络：首先，短平快的Proposal Network (P-Net)生成候选窗口；然后在下一阶段通过 Refinement Network (R-Net) 完善这些窗口；在最后阶段，Output Network (O-Net)生成边界框和脸部标记点。

![image](https://github.com/foamliu/MTCNN/raw/master/images/pipeline.png)

###架构

![image](https://github.com/foamliu/MTCNN/raw/master/images/architecture.png)

## 效果

![image](https://github.com/foamliu/MTCNN/raw/master/images/example.png)

## 用法

```bash
$ python demo.py
```

## 鸣谢

基于项目：
 - [TropComplique/mtcnn-pytorch](https://github.com/TropComplique/mtcnn-pytorch)