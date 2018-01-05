
# 正则表达式
import re
# >>> re.match('^Josh', 'Joshua Yss')
# <_sre.SRE_Match object; span=(0, 4), match='Josh'>
# >>>

# 1、match方法
# re.match(pattern, string, flags=0)
# pattern：表达式
# string：目标字符串
# flags：静态字段，例如re.DOTALL 取自re.RegexFlag.A

# . 匹配一个字符
# re.match('^...\d', 'joshua123')
# re.match('^......\d', 'joshua123')
# <_sre.SRE_Match object; span=(0, 7), match='joshua1'>

# flags=re.DOTALL # make dot match newline '.' 能匹配到'\n'
# re.match('.', '\n')
# re.match('.', '\n', flags=re.RegexFlag.DOTALL)
# <_sre.SRE_Match object; span=(0, 1), match='\n'>

# 2、re.search(pattern, string, flags=0)
# 找到第一个匹配结果并返回 注意以下结果中的匹配范围span=(2, 3)
# re.search('ab*', 'dfasabcde')
# <_sre.SRE_Match object; span=(2, 3), match='a'>
# re.search('ab*', 'asabcde')
# <_sre.SRE_Match object; span=(0, 1), match='a'>
# re.search('ab*', 'absabcde')
# <_sre.SRE_Match object; span=(0, 2), match='ab'>
# re.search('ab*', 'abbbbsabcde')
# <_sre.SRE_Match object; span=(0, 5), match='abbbb'>

# match 和 search
# match('a', 'abcde') <==> search('^a', 'abcde')
# re.match('c', 'abcde')
# re.search('c', 'abcde')
# <_sre.SRE_Match object; span=(2, 3), match='c'>
# re.search('^c', 'abcde')

# re.match('^a', '123\n34\nabc', re.M)
# re.search('^a', '123\n34\nabc')
# re.search('^a', '123\n34\nabc', re.M)
# <_sre.SRE_Match object; span=(7, 8), match='a'>

# 3、compile先将表达式编译,然后将编译结果用来匹配字符串,用于多次匹配 等价于match
# re.compile(pattern, flags=0)
# prog = re.compile('ab*')
# prog.match('abcde')
# <_sre.SRE_Match object; span=(0, 2), match='ab'>
# 等价于以下
# re.match('ab*', 'abcde')
# <_sre.SRE_Match object; span=(0, 2), match='ab'>


# 4、re.fullmatch() 全匹配
# re.fullmatch('ab*','abbbb')
# <_sre.SRE_Match object; span=(0, 5), match='abbbb'>
# re.fullmatch('ab*','abbbbc')

# 5、re.split()通过正则表达式分割字符串
# re.split('[a-z]', 'a123w78f9')
# ['', '123', '78', '9']

# 6、re.findall()
# re.findall('ab*', '2abcabbb34acc')
# ['ab', 'abbb', 'a']
# re.findall('[a-z]*', '2abcabbbacc')
# ['', 'abcabbbacc', '']

# 7、re.finditer()
# 以迭代器形式返回所有匹配对象
# iter = re.finditer('[a-z]', 'a123w78f9')
# next(iter)
# <_sre.SRE_Match object; span=(0, 1), match='a'>
# next(iter)
# <_sre.SRE_Match object; span=(4, 5), match='w'>
# next(iter)
# <_sre.SRE_Match object; span=(7, 8), match='f'>

# 8、re.sub(pattern, repl, string, count=0, flags=0)
# 通过repl替换目标string中匹配到的字符串
# repl可以是字符串,也可以是方法(必须包含一个参数)
# re.sub('-', ' ', 'I-Am-You-Everything',count = 2)
# 'I Am You-Everything'
# 当repl是一个方法时,方法必须包含一个参数,参数为匹配到的Match Object,否则报错TypeError: rpl() takes 0 positional arguments but 1 was given
# >>> re.sub('-', rpl, 'I-Am-You-Everything')
# 'I Am You Everything'
# >>> def rpl(mo):
# ...     print('called')
# ...     return ' '
# ...
# >>> re.sub('-', rpl, 'I-Am-You-Everything')
# called
# called
# called
# 'I Am You Everything'
# >>>

# >>> def rpl(mo):
# ...     if mo.group(0) == '-':
# ...         return ' '
# ...     elif mo.group(0) == '\\':
# ...         return '-'
# ...
# >>> re.sub(r'-|\\', rpl, 'I-Am-You 2017\\12\\07')
# 'I Am You 2017-12-07'

# 9、re.subn()和 re.sub()一样，返回值为元组

# 10、re.escape()


re.error

re.purge()
re.template()



# 返回的匹配类型对象 Match Objects


