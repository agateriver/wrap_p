import sublime
import sublime_plugin


class WrappCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        """wrap every lines in selected text in a <p> tag"""
        for region in self.view.sel():
            if not region.empty():
                # expand the selected text to whole lines
                _region = self.view.line(region)
                s = self.view.substr(_region)
                # Split the text in lines
                lines = s.splitlines()
                # Wrap every line in a <p> tag
                lines = ["<p>%s</p>" % l for l in lines]
                # Join the lines and replace the text
                self.view.replace(edit, _region, "\n".join(lines))

class Wrappindent2emCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                # expand the selected text to whole lines
                _region = self.view.line(region)
                s = self.view.substr(_region)
                # Split the text in lines
                lines = s.splitlines()
                # Wrap every line in a <p> tag
                lines = ['<p style="text-indent:2em">%s</p>' % l for l in lines]
                # Join the lines and replace whole lines
                self.view.replace(edit, _region, "\n".join(lines))

class WrappselCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        """wrap selected text in a <p> tag"""
        for region in self.view.sel():
            if not region.empty():
                s = self.view.substr(region)
                content ="<p>%s</p>" % s
                self.view.replace(edit, region, content)

			

class Wrappselindent2emCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                s = self.view.substr(region)
                content ='<p style="text-indent:2em">%s</p>' % s
                self.view.replace(edit, region, content)

