from setuptools import setup, find_packages

setup(
    name='your-package-name',
    version='0.1.0',
    description='A brief description of your project',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/your-package-name',
    packages=find_packages(), 
    install_requires=[
        'azure-cognitiveservices-speech',
        'python-dotenv',
        'argparse'
    ],  
)
