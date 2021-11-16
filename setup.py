from setuptools import setup


setup(
      name='watson_sklearn_transforms',
      version='1.0',
      description='''
            This is a sample python package for encapsulating custom
            tranforms from scikit-learn into Watson Machine Learning
      ''',
      url='https://github.com/GabrielGBernardes/btc2021-sklearn-transforms/',
      author='Gabriel Gutierrez',
      author_email='gabrielgber2@gmail.com',
      license='BSD',
      packages=[
            'watson_sklearn_transforms'
      ],
      zip_safe=False
)
