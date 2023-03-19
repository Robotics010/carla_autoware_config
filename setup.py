from setuptools import setup

package_name = 'carla_autoware_config'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/config',
             ['config/objects.json']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Robotics010',
    maintainer_email='kirill.mitkovskii@gmail.com',
    description='Configuration files for carla_autoware_bridge',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
