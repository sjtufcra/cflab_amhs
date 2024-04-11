from setuptools import setup, find_packages

setup(
    name='amhs_sjtu',
    version='1.0.0',
    author='cf_lab',
    url="https://github.com/sjtufcra/cflab_amhs.git",
    packages=find_packages(),
    description="用于规划一个寻优路径",  
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6", 
    install_requires=[  
        'fastapi',
        'uvicorn',
        'pandas',
        'networkx',
        'oracledb',
        "redis",  
        "redis-py-cluster",
        "pyyaml"
    ]
)
