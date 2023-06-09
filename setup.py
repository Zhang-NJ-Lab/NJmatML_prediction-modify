import setuptools

setuptools.setup(
    name="NJmatML",
    version="0.0.11",
    author="Lei_Zhang",
    author_email="ervin42772@gmail.com",
    description="Automates data-driven machine learning for materials science via NJmatML (材料数据可视化、机器学习建模与预测)",
    long_description="User Mannual（说明书参见）: https://nbviewer.org/github/Zhang-NJ-Lab/NJmatML/blob/main/2022-11-21/NJmatML-2022-11-21.ipynb                    \n  \n"
                     "csv模板请参见：https://github.com/Zhang-NJ-Lab/NJmatML/tree/main/2022-11-17      \n  \n"
                     "起始训练测试数据集csv（最右一列需要为输出数据，每列需要有列名）：https://github.com/Zhang-NJ-Lab/NJmatML/blob/main/2022-11-17/2DEformationCleaned.csv     \n"
                     "待预测csv：https://github.com/Zhang-NJ-Lab/NJmatML/blob/main/2022-11-17/x_New.csv     \n"
                     "特征生成中的无机材料化学式csv：https://github.com/Zhang-NJ-Lab/NJmatML/blob/main/2022-11-17/Inorganic_formula.csv     \n"
                     "特征生成中的有机材料化学式csv：Featurize_formula_exps.csv     \n  \n"
                     "模块：数据读取，可视化，热图，特征选择，特征生成，重要性排名，机器学习建模，准确率计算，交叉验证，符号回归等等。封装了简便函数用于机器学习建模。         \n  \n",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)