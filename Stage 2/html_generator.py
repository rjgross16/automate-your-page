def generate_concept_HTML(concept_question, concept_answer):
    html_text_1 = '''
<div class="concept">
    <div class="concept-question">
        ''' + concept_question
    html_text_2 = '''
    </div>
    <div class="concept-answer">
        ''' + concept_answer
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_question(concept):
    start_location = concept.find('QUESTION:')
    end_location = concept.find('ANSWER:')
    question = concept[start_location+10 : end_location-1]
    return question

def get_answer(concept):
    start_location = concept.find('ANSWER:')
    answer = concept[start_location+8 :]
    return answer

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('QUESTION:')
        next_concept_end   = text.find('QUESTION:', next_concept_start + 1)
        concept = text[next_concept_start:next_concept_end]
        text = text[next_concept_end:]
    return concept
        

SITE_TEXT = """QUESTION: Why am I seeing this?
ANSWER: You are on a browser (hopefully, or else then 
I have no answer for you). You told your browser to go to 
this page, and so your computer, since it's dumb and has 
no mind of its own (yet), went ahead and texted its friend 
Web and said "Hey buddy, can you send me the files that my 
owner requested?" 
Web said, "no problem, just give me a few nanoseconds," then 
retreived the files from a server via something called 
HTTP and sent them to your computer. Then your browser, since it's 
also dumb and has no mind of its own, interpeted the files that 
came through and displayed them on your screen.
QUESTION: Ok, but how did you make it?
ANSWER: I used a language called HTML, which stands for Hypertext 
Markup Language. HTML is made up of: Text content - which is what 
you are seeing now, Markup - which is what this page looks like, 
References to other documents - like the logo at the top of the screen, 
Links to other pages - like this link to a puppy video.
QUESTION: How did you make it look like this?
ANSWER: Everything you see on the screen is part of an HTML element. 
You add these elements to your page using things called tags, and you 
can apply attributes, or <strong>styles</strong>, to those elements. 
So, for example, I added a link to the puppy video using a link tag 
(which looks like this: &lt;a&gt;), and I wrote in my code that all 
link elements should be my favorite shade of red and have bold font.
QUESTION: Sounds pretty easy
ANSWER: Well, it would be really easy if computers weren't so dumb. 
I know what you're thinking, <Computers aren't dumb, didn't a computer 
beat Ken Jennings in Jeopardy?</em> That is true, but that computer 
was super dumb before programmers wrote a LOT of code to make it smart. 
And programmers must be careful when writing code. One small mistake, 
and the computer's <strong>stupidity</strong> would cause it to misinterpret 
the language and break everything.
QUESTION: Oh, so how do you write HTML?
ANSWER: To start, you can learn one easy thing, which is that every HTML 
document has the same basic structure: HTML &lt;html&gt; - which tells 
the computer that you are writing a document using HTML, Head &lt;head&gt; 
- where you usually put the styling of your page, Body &lt;body&gt; - 
where pretty much everything else goes."""


def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        question = get_question(concept)
        answer = get_answer(concept)
        concept_html = generate_concept_HTML(question, answer)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


print generate_all_html(SITE_TEXT)