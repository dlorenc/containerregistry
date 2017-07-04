# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools


DEPENDENCIES = (
    'httplib2 >= 0.9.1',
    'six >= 1.9.0',
    'oauth2client >= 4.1.2',
    'futures >= 3.1.1',
)


long_description = 'A set of Python libraries and tools for interacting with a Docker Registry.'


setuptools.setup(
    name='containerregistry',
    version='0.0.12',
    author='Google',
    author_email='mattmoor@google.com',
    description='A set of Python libraries and tools for interacting with a Docker Registry.',
    long_description=long_description,
    url='https://github.com/Google/containerregistry',
    packages=setuptools.find_packages(),
    install_requires=DEPENDENCIES,
    license='Apache 2.0',
    keywords='google container registry',
    classifiers=(
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
    ),
)
