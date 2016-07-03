'''
    Tag object definitions for different syntaxes.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.
'''

from collections import namedtuple

# GLOBALS
# -------

TAGS = []

# OBJECTS
# -------


class Node(namedtuple("Node", [
    "module",
    "code",
    "start",
    "open",
    "close"
])):
    '''Object definition for a node.'''

    #   PROPERTIES

    @property
    def line(self):
        '''Get the line the node occurs on'''

        return self.module[:self.start].count('\n') + 1

    @property
    def indent(self):
        '''
        Get the indentation of the node (indentation type can
        be found via the Sublime API).
        '''

        indent_newline = self.code.find('\n', self.open+1)
        if indent_newline == -1:
            return           # class not recognized, no indentation

        previous = self.module[:self.start]
        newline = previous.rfind('\n')
        indent = self.start - newline - 1

        return indent


class Class(Node):
    '''Object definition for a class node'''


class Function(Node):
    '''Object definition for a function node'''


class TagList(object):
    '''Holder for the active tags for the file'''

    tags = TAGS

    def sort(self):
        '''Sort tag list'''
