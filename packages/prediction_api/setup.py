from setuptools import setup

setup(name='prediction_api',
      version='0.1.0',
      description='Package that implements an api for the prediction model',
      url='https://github.com/alejandroviegener/OrdenTakenPredictor/',
      author='Alejandro Viegener',
      author_email='alejandro.viegener@gmail.com',
      license='MIT',
      packages=['prediction_api'],
      install_requires=['sklearn', 'pandas', 'numpy', 'fastapi'],
      zip_safe=False)
