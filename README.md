kdn-pal
=======

### Description

Kdnuggets (http://www.kdnuggets.com/) pure console reader. Designed to run from console (hence the setup.py) and to dig out most interesting news (yet this feature currently under development). Uses RSS parser and / or HTML scrapping to display news from KDNuggets portal.

#### To do list

* publish on pypi
* implement html scrapping
* sort and shuffle articles intelligently

### Licence

The MIT License (MIT)

Copyright (c) 2014 Oskar Jarczyk

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

### Usage

```
(kdn-pal) C:\data\kdn-pal>python kdn.py
 KDNuggets - command line tool for data hackers
Usage: kdn.py [OPTIONS] COMMAND [ARGS]...

  What's new on KDNuggets

Options:
  --rss / --no-rss
  --verbose
  --save-directory PATH
  --help                 Show this message and exit.

Commands:
  academic  List academic topics
  jobs      List jobs
  podcasts  List podcasts
  stories   List stories
  view      Go to the particular story on KDNuggets

(kdn-pal) C:\data\kdn-pal>
```
