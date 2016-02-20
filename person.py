class Person:
    def __init__(self, name_line, comments):
        """
        Construct a person.

        Args:
            self: the idiomatic python reference to self
            name_line: the first line in the grade file (utln and grade)
            comments: each line that follows the name_line until the next student
        Returns:
            Nothing (but creates a new Person)
        """
        name_lines = name_line.split()
        if len(name_lines) > 0:
            self.utln = name_lines[0]
        else:
            self.utln = "UNKNOWN"
        if len(name_lines) > 1:
            self.grade = name_lines[1]
        else:
            self.grade = "I"
        self.comments = map(str.strip, comments)

    def output(self):
        """
        Output a person in the grading format style.
        """
        print self.output_as_string()

    def output_as_string(self):
        """
        Generate a string in the format of a 105 grade.

        Returns:
            A string in precisely the format expected.
        """
        string = "{}    {}\n".format(self.utln, self.grade)
        for comment in self.comments:
            string = string + "  {}\n\n".format(comment)
        return string
        
