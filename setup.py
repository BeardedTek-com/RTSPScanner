from pathlib import Path
from setuptools import find_packages, setup
dependencies = ['beard-portscan']
# read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name='rtspscanner',
    packages=find_packages(),
    version='0.1.1',
    description="RTSP Camera Scanner",
    author="The Bearded Tek",
    author_email="kenny@beardedtek.com",
    url="https://github.com/beardedtek/PortScan",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    project_urls={
        "Bug Tracker": "https://github.com/beardedtek/rtsp/issues",
    },
    keywords=[
        "port",
        "scanner",
        "multithreading",
        "queue",
        "terminal",
        "utility",
        "rtsp",
        "camera",
        "frigate",
        "fevr",
        "beardedtek",
        "python3",
    ],
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Affero GNU General Public License v3 (AGPLv3)",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    install_requires=dependencies,
    py_modules=['rtspscanner'],
    entry_points={
        'console_scripts': [
            "rtspscanner=rtspscanner:main"
        ],
    },
)
