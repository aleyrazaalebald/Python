# import libraries

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

########################
# Page title
########################
image = Image.open('Penguins.jpg')
st.image(image, caption="Penguins", use_container_width=True)
st.write("""

         # DNA Nucleotide Count Web App
This ap counts the nucleotide composition of query DNA!

""")

########################
# Input Text Box
########################

#st.sidebar.header('Enter DNA Sequence')
st.header('Enter DNA sequence')
sequence_input = ">DNA Query 2\n nGAACACGTGGAGGCAAACAGGAAGGT\nGAAGAAAGAAAGGGGTCDFGGAATTCGT\nGGGAGAGAGAGTAAAATG"
sequence = st.text_area("Sequence Input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)
st.write("""
         ***
""")
#print the input DNA Sequence
st.header('INPUT (NA Query)')
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

### 1. Print dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_cont(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C',seq.count('C'))
    ])
    return d

X = DNA_nucleotide_cont(sequence)

X

### 2. Print Text
st.subheader('2. Print text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')

### 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index': 'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(10) # controls width of bar.
)

st.write(p)