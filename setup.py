from setuptools import find_packages, setup

setup(
    name="sales",
    version="1.0.0",
    py_modules=["sales"],
    packages=find_packages(),
    install_requires=["Click>=7.0"],
    entry_points="""
        [console_scripts]
        sales=sales:cli
    """,
)
