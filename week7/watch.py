import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    if source := re.search(r'^(.*?)? (src="(.*?)")(.*?)?$', s):
        shorter=re.sub("embed/", "", source.group(3))
        if "youtube" in shorter:
            shorter=re.sub("youtube", "youtu.be", shorter)
            return shorter
    else:
        return None


if __name__ == "__main__":
    main()

"""Run your program with python watch.py. Ensure your program prompts you for HTML, then copy/paste the below:
<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
Press enter and your program should output https://youtu.be/xvFZjo5PgG0. Notice how, though the src attribute is prefixed with http://www.youtube.com/embed/, the resulting link is prefixed with https://youtu.be/.

Run your program with python watch.py. Ensure your program prompts you for HTML, then copy/paste the below:
<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" 
frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
Press enter and your program should still output https://youtu.be/xvFZjo5PgG0.

Run your program with python watch.py. Ensure your program prompts you for HTML, then copy/paste the below:
<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>
Press enter and your program should output None. Notice how the src attribute doesn’t point to a YouTube link!"""