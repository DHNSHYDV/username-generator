from setuptools import setup, find_packages

setup(
    name="username-generator",
    version="0.1.0",
    description="A versatile tool for generating creative and unique usernames",
    author="Zed",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask>=2.0.1",
    ],
    entry_points={
        "console_scripts": [
            "generate-username=generate_username:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)