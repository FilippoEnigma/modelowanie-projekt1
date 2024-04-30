from antlr4.error.ErrorListener import ErrorListener

class VerboseErrorListener(ErrorListener):
    def __init__(self):
        super(VerboseErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        suggestion = self.suggestFix(msg)
        self.errors.append(f"Syntax error at line {line}:{column} - {msg}{suggestion}")

    def hasErrors(self):
        return len(self.errors) > 0

    def printErrors(self):
        for error in self.errors:
            print(error)

    def suggestFix(self, msg):
        if "mismatched input" in msg:
            return " Check if a token is missing or if there's a typo."
        elif "no viable alternative at input" in msg:
            return " Check the syntax here. There might be a typo or a required element is missing."
        elif "extraneous input" in msg:
            return " Check for any additional, unnecessary tokens that might be causing an issue."
        else:
            return " Please check the syntax carefully."

