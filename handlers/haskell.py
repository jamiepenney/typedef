from .implicit_type import ImplicitTypeHandler

class HaskellHandler(ImplicitTypeHandler):

    def booleanRepr(self, bool_val):
        if bool_val:
            return "True"
        return "False"

    def numberRepr(self, number_string):
        return number_string

    def stringRepr(self, string_without_quotes):
        return "\"" + string_without_quotes + "\""

    def createFullOutputString(self, variable_name, value):
        return variable_name + " = " + value

    def arrayStartString(self):
        return "["

    def arrayEndString(self):
        return "]"

    def setStartString(self):
        # NOTE: Requires import
        return "Set.fromList ["

    def setEndString(self):
        return "]"

    def mapStartString(self):
        return "Map.fromList ["

    def mapEndString(self):
        return "]"

    def keyValueStartString(self):
        return "("

    def keyValueEndString(self):
        return ")"

    def multiValueSeparator(self):
        return ","

    def keyValueSeparator(self):
        return " , "

