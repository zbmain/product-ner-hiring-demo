# 商品信息提取-测试题

请根据下述数据集，实现商品标题NER识别模型，从商品标题中提取实体。

## 数据集：

商品NER数据集: https://modelscope.cn/datasets/winwin_inc/product-ner-hiring-demo

* 商品标题
* 实体标签：
    * group_name: 集团
    * brand_name: 品牌
    * spec: 规格
    * package: 包装

## 说明

1. 请根据实现方案，若需BIO数据集，请自行转换。
2. ⚠️这是一个嵌套NER任务

* 元气森林外星人维B水柑橘味500ml
    * 集团: 元气森林
    * 品牌: 外星人
    * 规格: 500ml
    * 包装：
* 元气森林饮用纯净水云峰白520ml
    * 集团: 元气森林
    * 品牌: 元气森林
    * 规格: 500ml
    * 包装：

## 代码描述：

1. 请自行安装环境管理工具`uv`: https://github.com/astral-sh/uv
2. 执行代码测试：`uv run pytest` 将下载数据集预览。
3. 如需Jupyter Notebook：`uv run notebook`
4. 请继续实现你的代码。

## 结果要求：

* 编程语言：Python优先、Typescript/Go均可。
* 实现框架：不限（机器学习、深度学习、Agent方案）。
* 思路：给出你的分析因素、框架选择原因、流程优化分析与深度优化建议。
* 输出
    * 指标：根据测试集自行计算指标。
    * 如果使用Python语言请通过Py、Notebook+Py完成，并保留过程记录。
    * 其他语言请提供一个HTTP API的在线Service，或者可以被方便调用的Lib。
    * 【加分项】对实现方案的思路描述、完整迭代记录。

## 提交方式

* 克隆仓库，打包完整项目Zip，发给HR。
* 或者Fork项目（不要提PR），提交你的仓库链接，发给HR。