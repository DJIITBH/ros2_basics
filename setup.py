from setuptools import find_packages, setup

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dhananjay',
    maintainer_email='dhananjaya@iitbhilai.ac.in',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = mypkg.my_node:main", #make executable here "executable_name = pkg.node_name:main"
            "draw_circle = mypkg.draw_circle:main",
            "pose_subscriber = mypkg.pose_subscriber:main"
        ],
    },
)
