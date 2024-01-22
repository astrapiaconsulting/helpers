import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='helpers',
    version='0.0.1',
    author='Bhavya Kumawat',
    author_email='bhavyakumawat99@gmail.com',
    description='Utility Methods',
    long_description_content_type="text/markdown",
    url='https://github.com/astrapiaconsulting/helpers',
    license='MIT',
    packages=['helpers'],
    install_requires=['requests'],
)
