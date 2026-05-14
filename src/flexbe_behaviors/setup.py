from setuptools import setup, find_packages
from glob import glob

package_name = 'flexbe_behaviors'

setup(
    name=package_name,
    version='0.0.0',

    packages=find_packages(),

    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),

        ('share/' + package_name,
            ['package.xml']),

        ('share/' + package_name + '/behaviors',
            glob('behaviors/*.xml')),
    ],

    install_requires=['setuptools'],
    zip_safe=True,

    maintainer='karan',
    maintainer_email='kamitrathod01@gmail.com',

    description='FlexBE behaviors and custom states',
    license='Apache-2.0',

    tests_require=['pytest'],

    entry_points={
        'console_scripts': [],
    },
)
