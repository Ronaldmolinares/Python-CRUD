from setuptools import setup

setup(
    name="sales",
    version="1.0.0",
    py_modules=["sales"],
    install_requires=["Click>=7.0"],
    entry_points="""
        [console_scripts]
        sales=sales:cli
    """,
)
