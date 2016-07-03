'''
    C++ style getters and setters for C/C++ and Python.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.
'''

#import re
import os
import sys

HOME = os.path.dirname(os.path.realpath(__file__))
sys.path.append(HOME)
sys.path.append(os.path.join(HOME, "tags"))

import sublime                                          # NOQA
import sublime_plugin

import c
#import python


# HELPERS
# -------


#def build_tags(source):
#    '''
#    Extract active tags from a string containing Python
#    source code.
#    '''
#
#    print(repr(remove_comments(source)))
#    #print(remove_comments(python_source))


# COMMANDS
# --------


class BuildTags(sublime_plugin.TextCommand):
    '''Build tag list for the sublime text getter/setter command'''

    def run(self, edit):
        '''Build the entire tag list'''

        syntax = self.view.settings().get('syntax')
        contents = self.view.substr(sublime.Region(0, self.view.size()))
        if syntax.startswith("Packages/Python"):
            pass
            #python.build_tags(contents)
            #build_tags(contents)
        elif syntax.startswith("Packages/C++"):
            c.build_tags(contents)


class CreateSetter(sublime_plugin.TextCommand):
    '''Create a setter for a C++ member variable'''

    def run(self, edit):
        '''Find the getter and setter and insert at the active point'''

        position = self.view.sel()[0].begin()
        self.view.insert(edit, position, "Hello, World!")


class GetterCommand(sublime_plugin.TextCommand):
    '''Create a getter for a C++ member variable'''


class GetSetCommand(sublime_plugin.TextCommand):
    '''Combines both the get/set commands'''
