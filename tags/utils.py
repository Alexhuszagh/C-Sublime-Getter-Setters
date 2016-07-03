'''
    Utilities for extracting tags.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.
'''

# CONSTANTS
# ---------

BRACKETS = {
    'parentheses': ('(', ')'),
    'braces': ('{', '}'),
    'square': ('[', ']'),
    'angle': ('<', '>'),
}

# FUNCTIONS
# ---------


def match_brackets(string, brackets=BRACKETS['parentheses']):
    '''Find opening and closing bracket position from a target string'''

    start = string.find(brackets[0])
    if start == -1:
        # no match
        return None

    counter = 1
    for end, character in enumerate(string[start+1:]):
        if character == brackets[0]:
            counter += 1
        elif character == brackets[1]:
            counter -= 1
        if not counter:
            return start, end+1
