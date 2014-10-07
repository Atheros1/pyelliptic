# Copyright (C) 2014 Yann GUIBET <yannguibet@gmail.com>
# This program is free software; you can redistribute it
# and/or modify it under the terms of version 3 of the
# GNU General Public License as published by the Free
# Software Foundation
#
# In addition, as a special exception, the author of this
# program gives permission to link the code of its
# release with the OpenSSL project's "OpenSSL" library (or
# with modified versions of it that use the same license as
# the "OpenSSL" library), and distribute the linked
# executables. You must obey the GNU General Public
# License in all respects for all of the code used other
# than "OpenSSL".  If you modify this file, you may extend
# this exception to your version of the file, but you are
# not obligated to do so.  If you do not wish to do so,
# delete this exception statement from your version.
#
# This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public
# License along with this package; if not, write to the Free
# Software Foundation, Inc., 51 Franklin St, Fifth Floor,
# Boston, MA  02110-1301 USA

from setuptools import setup, find_packages

setup(
    name="pyelliptic",
    version='1.5.4',
    url='https://github.com/yann2192/pyelliptic',
    license='GPL',
    description=
    "Python OpenSSL wrapper for modern cryptography with " +
    "ECC, AES, HMAC, Blowfish, ...",
    author='Yann GUIBET',
    author_email='yannguibet@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Environment :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Security :: Cryptography',
    ],
    install_requires=[
        'streql==3.0.2',
    ],
)
