from pathlib import Path
from setuptools import find_packages, setup
dependencies = ['beard-portscan','Pillow']
# read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name='rtspscanner',
    packages=find_packages(),
    version='0.1.4',
    description="RTSP Camera Scanner",
    author="The Bearded Tek",
    author_email="kenny@beardedtek.com",
    url="https://github.com/beardedtek-com/RTSPScanner",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='AGPLv3',
    project_urls={
        "Bug Tracker": "https://github.com/beardedtek-com/RTSPScanner/issues",
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
        "cctv",
        "security"
    ],
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
        "Topic :: Multimedia :: Video",
        "Topic :: Multimedia :: Video :: Capture",
    ],
    install_requires=dependencies,
    py_modules=['rtspscanner'],
    entry_points={
        'console_scripts': [
            "rtspscanner=rtspscanner:main"
        ],
    },
)
