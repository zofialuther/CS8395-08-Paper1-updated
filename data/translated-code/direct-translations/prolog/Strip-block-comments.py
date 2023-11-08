```python
from pyswip import Prolog

prolog = Prolog()
prolog.assertz(":- system:set_prolog_flag(double_quotes,codes) .")

def strip_block_comments(INPUTz):
    strip_block_comments(INPUTz,OUTPUTz)
    print("```")
    print(OUTPUTz)
    print("```")

def strip_block_comments(INPUTz,OUTPUTz):
    prolog.query("prolog:phrase(block(OUTPUTz),INPUTz)")

def block([]):
    prolog.assertz("\+ [_] , ! .")

def block([CODE|OUTPUTz]):
    prolog.assertz("\+ comment , ! , [CODE] , block(OUTPUTz) .")

def block(OUTPUTz):
    prolog.assertz("comment , ! , block(OUTPUTz) .")

def comment():
    prolog.assertz("comment_entr , zero_or_more(comment_each) , comment_exit .")

def comment_entr():
    prolog.assertz("\"/*\" .")

def comment_each():
    prolog.assertz("comment , ! .")
    prolog.assertz("\+ comment_exit , ! , [_] .")

def comment_exit():
    prolog.assertz("\"*/\" .")

def zero_or_more(CALLABLE):
    prolog.assertz("call(CALLABLE) , ! , zero_or_more(CALLABLE) .")

def zero_or_more(_):
    prolog.assertz("! .")
```