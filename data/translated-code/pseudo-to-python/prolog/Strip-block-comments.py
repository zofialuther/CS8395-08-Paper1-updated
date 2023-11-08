def strip_block_comments(INPUTz):
    OUTPUTz = strip_block_comments_helper(INPUTz)
    print("```")
    print(OUTPUTz)
    print("```")

def strip_block_comments_helper(INPUTz):
    return block(INPUTz)

def block(INPUTz):
    if not INPUTz:
        return []
    else:
        if not comment(INPUTz):
            return [INPUTz[0]] + block(INPUTz[1:])
        else:
            return block(INPUTz)

def comment(INPUTz):
    if len(INPUTz) < 2:
        return False
    else:
        if INPUTz[0:2] == "/*":
            return True
        else:
            return False