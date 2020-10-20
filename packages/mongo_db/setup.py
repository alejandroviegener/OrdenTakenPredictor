from setuptools import setup

setup(name='mongo_db',
      version='0.1.0',
      description='Package that implements a mongo database client',
      url='https://github.com/alejandroviegener/OrdenTakenPredictor/',
      author='Alejandro Viegener',
      author_email='alejandro.viegener@gmail.com',
      license='MIT',
      packages=['mongo_db'],
      install_requires=['pymongo'],
      zip_safe=False)
