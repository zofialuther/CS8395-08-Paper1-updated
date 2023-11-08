import Text.Printf as printf

input_data = [ ("", ' ')
          , ("The better the 4-wheel drive, the further you'll be from help when ya get stuck!", 'e')
          , ("headmistressship", 's')
          , ("\"If I were two-faced, would I be wearing this one?\" --- Abraham Lincoln ", '-')
          , ("..1111111111111111111111111111111111111111111111111111111111111117777888", '7')
          , ("I never give 'em hell, I just tell the truth, and they think it's hell. ", '.')
          , ("                                                    --- Harry S Truman  ", 'r')
          , ("aardvark", 'a')
          , ("😍😀🙌💃😍😍😍🙌", '😍')
          ]
          
def collapse(s, c):
  def go(s):
    if not s:
      return []
    elif len(s) > 1 and s[0] == s[1] and s[0] == c:
      return go(s[1:])
    else:
      return [s[0]] + go(s[1:])
  return go(s)

def main():
  for a, c in input_data:
    b = collapse(a, c)
    printf("squeeze: '%c'\nold: %3d «««%s»»»\nnew: %3d «««%s»»»\n\n" % (c, len(a), a, len(b), b))

main()