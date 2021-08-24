Line Delimited JSON Reader
==================

This Python generator function reads from a ld-json data stream and outputs a dictionary object per JSON object.
The module uses the core 'json' module to parse the input.

Quick Start
-----------

To install, use pip:

::

    $ pip install kipy-ldjson-reader

Example Usage
-------------

**Example 1:** Basic usage

.. code-block:: python

    from ldjson import ldjson

    with open("test.json", "r", encoding="utf-8") as input_stream:
        for json_object in ldjson(input_stream):
            print(json_object)


Contributors
------------

This package is authored and maintained by:

-  `Gary Ranson`


Copyright and License
---------------------

	The `MIT license <https://opensource.org/licenses/MIT>`_

	Copyright (c) 2021 Gary Ranson

	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in all
	copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
	SOFTWARE.