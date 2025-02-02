from setuptools import setup, find_packages

setup(
    name="baby-monitor",
    version="v1.0.0", 
    packages=find_packages(),
    install_requires=[
        "opencv-python==4.7.0.72",
        "flask==2.2.3",
        "flask-socketio==5.2.1",
        "pyserial==3.5",
        "numpy==1.23.4",
        "paho-mqtt==1.6.1",
        "requests==2.28.1",
        "gpiozero==1.6.2",
    ],
    extras_require={
        'dev': [
            'pytest',  # For testing
        ]
    },
    description="A Raspberry Pi-based baby monitor with video streaming and more.",
    author="Bradley Edelman",
    author_email="bjedelma@gmail.com",
    url="https://github.com/BradleyEdelman/Raspberry-Pi-Baby-Monitor.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)
