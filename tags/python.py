'''
    Extract taglist for Python file.

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
#import re
import shlex

#import objects

# REGEXES
# -------

#COMMENT_STRING = r"(\".*?(?<!\\)\"|\'.*?(?<!\\)\')|(/\*.*?\*/|//[^\r\n]*$)"
#COMMENTS = re.compile(COMMENT_STRING)


# TODO: need to find classes



# FUNCTIONS
# ---------


#def remove_comments(line):
#    '''Remove comments from the target line'''
#
#
#def remove_docstring(line):
#    '''Remove docstring from the target line'''


#def parse_python(python_lines):
#    '''
#    Parse Python file source code to remove comments and extract
#    significant features.
#    '''


def build_tags(python_source):
    '''
    Extract active tags from a string containing Python
    source code.
    '''

    no_comments = shlex.split(python_source)
    print(type(shlex))
    #python_lines = python_source.splitlines()
    #print(python_lines)

    # Need to remove all comments

