from SublimeLinter.lint import RubyLinter, LintMatch

"""This module exports the Flay plugin class."""

class Flay(RubyLinter):
    cmd = 'flay'
    regex = r'\s*(?P<filename>.+):(?P<line>\d+)'
    multiline = False

    defaults = {
        'executable': 'flay',
        'selector': 'source.ruby',
        'args': ['-#']
    }
    # , '${file_on_disk}'
    cmd = ('${executable}', '${args}' , '${tempfile}')
    tempfile_suffix = '-'
    default_type = WARNING

    def split_match(self, match):
        """Add near detail to error dict."""

        error = super().split_match(match)
        error['error_type'] = 'error' if float(error['message']) > self.settings.get('threshold') else 'warning'

        return error
