import platform
import tempfile
import dominate

from weasyprint import HTML

class Printer:
    data: str
    filename: str

    def print_win(self):
        import win32api
        import win32print

        # os.startfile("C:/Users/TestFile.txt", "print")

        with open("results.txt", "w+") as f:
            f.write("RESULT")
            # f.

    def print_linux(self):
        import subprocess
        subprocess.Popen(["/usr/bin/lp", self.filename])


    def print_mac(self):
        pass


    def construct_file(self):
        # make a temporary file
        # this is where we will write our output
        self.filename = tempfile.mktemp(".pdf")

        # make a new html doc
        doc = dominate.document(title = "FBLA Quiz Results")

        htmlc = """\
<html>

    <body>
        <h1> FBLA Quiz Results </h1>

        <h2> ------------------------------------ </h2>

        <h3> 
            <u> Question 1 </u>
            <br>
            <h4> 
                Question: Is FBLA cool

                <br>
                Correct Answer: Yes
                <br>
                Your Answer: No

                <br><br>

                Result: Incorrect
            </h4>
            
            
        </h3>
    </body>


</html>"""
        # (temporary) load in raw html string
        doc.add_raw_string(htmlc)

        # load html code into HTML object as a string
        # then convert it to a pdf and write it to the temp file created
        HTML(string=doc.render()).write_pdf(self.filename)

    def print(self, data: str):
        self.data = data
        self.construct_file()

        self.print_linux()
        return

        if platform.system() == "WIndows":
            print_win()
        
        elif platform.system() == "Linux":
            print_linux()

        elif platform.system() == "Darwin":
            print_mac()