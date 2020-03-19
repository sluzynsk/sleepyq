from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='sleepyq',
      version='0.8',
      description='SleepIQ API for Python',
      long_description=readme(),
      url='http://github.com/sluzynsk/sleepyq',
      author='Steve Luzynski',
      author_email='steve@luzynski.net',
      license='MIT',
      packages=['sleepyq'],
      install_requires=[
          'requests',
          'inflection'
      ],
      include_package_data=True,
      zip_safe=False)
