from setuptools import setup

setup(name='prediction_model',
      version='0.1.0',
      description='Package for order-taken prediction',
      url='https://github.com/alejandroviegener/OrdenTakenPredictor/',
      author='Alejandro Viegener',
      author_email='alejandro.viegener@gmail.com',
      license='MIT',
      packages=['prediction_model'],
      install_requires=['sklearn', 'pandas'],
      zip_safe=False)
