from setuptools import setup, find_packages

with open("Readme.md", "r") as file:
    long_description = file.read()

setup(
    name="mentions_pipeline_notebook",
    version="0.0.1",
    author="Patrice Lopez",
    author_email="patrice.lopez@science-miner.com",
    description="Python notebooks illustrating software mention extraction pipelines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/softcite/mentions_pipeline_notebook",
    packages=find_packages(exclude=['test', '*.test', '*.test.*']),  
    include_package_data=True,
    python_requires='>=3.8',
    install_requires=[
        'article_dataset_builder==0.2.3',
        'software_mentions_client==0.1.0',
        'tqdm==4.21',
        'requests',
        'jupyter',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
