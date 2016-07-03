'''
    Extract taglist for C/C++ file.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.
'''

# load modules/submodules
import re

import tag
import utils

#import objects

# CONSTANTS
# ---------


# REGEXES
# -------

COMMENT_STRING = r"(\".*?(?<!\\)\"|\'.*?(?<!\\)\')|(/\*.*?\*/|//[^\r\n]*$)"
COMMENTS = re.compile(COMMENT_STRING, re.MULTILINE | re.DOTALL)
LINE_COUNT = re.compile('[\r\n]')


CLASS_STRING = (
    r'(?:^|(?P<leading>\s+))'
    r'(?:typedef\s+)?'
    r'((?:struct)|(?:class))'
    r'\s*(?P<name>\w+)\s*\{'
)
CLASS_REGEX = re.compile(CLASS_STRING)

# FUNCTIONS
# ---------


def comment_replacer(match, line_count=LINE_COUNT):
    '''
    Remove comments, keep line totals intact. This is done via
    a custom comment replacer.
    '''

    comments = match.group(2)
    if comments is not None:
        return "\n" * len(line_count.findall(comments))

    # return group without comments
    return match.group(1)


def add_classes(c_source):
    '''Find class definitions from C source code.'''

    for match in CLASS_REGEX.finditer(c_source):
        leading = len(match.group('leading'))
        start = match.start() + leading
        code = c_source[start:]
        open, close = utils.match_brackets(code, utils.BRACKETS['braces'])
        tag.TAGS.append(tag.Class(c_source, code, start, open, close))


def build_tags(c_source):
    '''
    Extract active tags from a string containing C
    source code.
    '''

    del tag.TAGS[:]
    no_comments = COMMENTS.sub(comment_replacer, c_source)
    add_classes(no_comments)
    print(tag.TAGS)
    print(tag.TAGS[0].line)
    print(tag.TAGS[0].indent)
