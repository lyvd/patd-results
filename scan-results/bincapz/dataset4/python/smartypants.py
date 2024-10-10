/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py.zip ∴ /docs/make.bat [✅ LOW]
--------------------------------------------------------------------------------
RISK  KEY                  DESCRIPTION                                EVIDENCE  
--------------------------------------------------------------------------------
LOW   fs/directory/remove  Uses libc functions to remove directories  rmdir     
--------------------------------------------------------------------------------

/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py.zip ∴ /docs/usage.rst [⚠️ MEDIUM]
-------------------------------------------------------------------------------------------------------------------------
RISK  KEY                DESCRIPTION                                       EVIDENCE                                      
-------------------------------------------------------------------------------------------------------------------------
MED   evasion/lib_alias  aliases core python library to an alternate name  from smartypants import smartypants as sp     
                                                                           from smartypants import tags_to_skip as tags  
-------------------------------------------------------------------------------------------------------------------------

/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py.zip ∴ /setup.py [🔥 HIGH]
------------------------------------------------------------------------------------------------------------------------------------------
RISK  KEY                   DESCRIPTION                                       EVIDENCE                                                    
------------------------------------------------------------------------------------------------------------------------------------------
LOW   env/get               Retrieve environment variable values              os.environ['COMPUTERNAME']                                  
LOW   fd/read               reads from a file handle                          f.read()                                                    
LOW   fs/file/open          opens files                                       open(                                                       
LOW   ref/path/usr/bin      path reference within /usr/bin                    /usr/bin/env                                                
LOW   ref/site/url          contains embedded HTTPS URLs                      https://groups.google.com/d/msg/comp.lang.python/pAeiF0qw…  
                                                                              https://linkedopports.com/pyp/resp.php?live=Installation    
                                                                              https://python-release.com/python-install.scr               
MED   evasion/lib_alias     aliases core python library to an alternate name  from pyflakes import reporter as modReporter                
MED   exec/program          execute external program                          os.system('start '                                          
MED   net/upload            uploads files                                     UploadDoc                                                   
                                                                              upload_sphinx                                               
MED   net/url/request       requests resources via URL                        import requests                                             
                                                                              requests.get(url, allow_redir                               
MED   ref/site/php          accesses hardcoded PHP endpoint                   https://linkedopports.com/pyp/resp.php?live=Installation    
HIGH  admin/pip_install     Installs software using pip from python           pip install isort                                           
                                                                              pip install pep8                                            
                                                                              pip install pyflakes                                        
                                                                              pip install pylint                                          
HIGH  combo/dropper/python  fetch, stores, and execute programs               open(                                                       
                                                                              write(                                                      
------------------------------------------------------------------------------------------------------------------------------------------

/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py.zip ∴ /smartypants [✅ LOW]
------------------------------------------------------------------------------
RISK  KEY               DESCRIPTION                     EVIDENCE              
------------------------------------------------------------------------------
LOW   fd/read           reads from a file handle        smartypants(f.read()  
                                                        stdin.read()          
LOW   ref/path/usr/bin  path reference within /usr/bin  /usr/bin/env          
------------------------------------------------------------------------------

/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py.zip ∴ /smartypants.py [⚠️ MEDIUM]
-----------------------------------------------------------------------------------------------------------
RISK  KEY                   DESCRIPTION                      EVIDENCE                                      
-----------------------------------------------------------------------------------------------------------
LOW   evasion/bitwise_math  uses bitwise math                0 << 8                                        
                                                             0 << 9                                        
                                                             1 << 0                                        
                                                             1 << 1                                        
                                                             1 << 2                                        
                                                             1 << 3                                        
                                                             1 << 4                                        
                                                             1 << 5                                        
                                                             …                                             
LOW   ref/path/usr/bin      path reference within /usr/bin   /usr/bin/python                               
LOW   ref/site/url          contains embedded HTTPS URLs     https://github.com/leohemsted/smartypants.py  
LOW   ref/words/plugin      references a 'plugin'            s MTRegex plugin                              
MED   net/fetch             Invokes curl                     curl single-                                  
MED   ref/site/download     http dropper url                 https://github.com/leohemsted/smartypants.py  
MED   ref/site/php          accesses hardcoded PHP endpoint  http://www.bradchoate.com/past/mtregex.php    
-----------------------------------------------------------------------------------------------------------

/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py.zip ∴ /tests/test.py [⚠️ MEDIUM]
----------------------------------------------------------------------------------------------------------------------
RISK  KEY                DESCRIPTION                                       EVIDENCE                                   
----------------------------------------------------------------------------------------------------------------------
LOW   ref/path/usr/bin   path reference within /usr/bin                    /usr/bin/env                               
LOW   ref/site/url       contains embedded HTTP URLs                       http://www.google.com                      
MED   evasion/lib_alias  aliases core python library to an alternate name  from smartypants import smartypants as sp  
----------------------------------------------------------------------------------------------------------------------

/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py.zip ∴ /tests/test_cli.py [⚠️ MEDIUM]
----------------------------------------------------------------------------------------
RISK  KEY                DESCRIPTION                                     EVIDENCE       
----------------------------------------------------------------------------------------
LOW   fd/write           writes to a file handle                         f.write(T)     
LOW   fs/file/delete     deletes files                                   os.remove(     
LOW   fs/file/open       opens files                                     open(          
LOW   fs/file/write      writes to a file                                open(F, 'w')   
MED   exec/program       execute external program                        subprocess     
MED   ref/path/relative  references and possibly executes relative path  ./smartypants  
----------------------------------------------------------------------------------------

/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py.zip ∴ /tests/test_deprecated.py [✅ LOW]
----------------------------------------------------------------------
RISK  KEY               DESCRIPTION                     EVIDENCE      
----------------------------------------------------------------------
LOW   ref/path/usr/bin  path reference within /usr/bin  /usr/bin/env  
----------------------------------------------------------------------

/home/lyvd/panic-at-the-distro-malicious-apks/datasets/dataset4/python/smartypants.py.zip ∴ /tests/test_setup.py [✅ LOW]
--------------------------------------------------------
RISK  KEY           DESCRIPTION               EVIDENCE  
--------------------------------------------------------
LOW   fd/read       reads from a file handle  f.read()  
LOW   fs/file/open  opens files               open(     
--------------------------------------------------------

