import wordcloud

wc = wordcloud.WordCloud()

wc.generate("""
A Turing Machine (TM) is a mathematical model which consists of an infinite length tape divided 
into cells on which input is given. It consists of a head which reads the input tape. A state 
register stores the state of the Turing machine. After reading an input symbol, it is replaced 
with another symbol, its internal state is changed, and it moves from one cell to the right or 
left. If the TM reaches the final state, the input string is accepted, otherwise rejected.
- tutorialpoint.com
""")

wc.to_file("wc1.png")
