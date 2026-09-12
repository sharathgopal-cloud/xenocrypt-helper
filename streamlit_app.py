import streamlit as st
import collections
import string

# Set up mobile page configuration
st.set_page_config(page_title="Xenocrypt Solver", page_icon="📝", layout="centered")

st.title("📝 Xenocrypt Analyzer")
st.write("Paste your Spanish text below to extract key Codebusters data.")

# Large, mobile-friendly text input area
user_input = st.text_area("Spanish Text Input:", placeholder="Paste text here...", height=150)

if user_input:
    # Standardize to uppercase and include Spanish Ñ
    text = user_input.upper()
    valid_letters = string.ascii_uppercase + "Ñ"
    
    words = text.split()
    two_letter_words = set()
    three_letter_words = set()
    clean_letter_list = []
    
    for word in words:
        cleaned_word = "".join([c for c in word if c in valid_letters])
        if len(cleaned_word) == 2:
            two_letter_words.add(cleaned_word)
        elif len(cleaned_word) == 3:
            three_letter_words.add(cleaned_word)
        for letter in cleaned_word:
            clean_letter_list.append(letter)

    total_letters = len(clean_letter_list)
    letter_counts = collections.Counter(clean_letter_list)
    
    # Display Results in clean, mobile-friendly blocks
    st.subheader("📊 Letter Frequencies")
    st.caption("Standard Spanish Expected Top Letters: E, A, O, S, N")
    
    # Create a clean string layout for mobile scrolling
    freq_output = ""
    for letter, count in letter_counts.most_common():
        percentage = (count / total_letters) * 100
        freq_output += f"**Letter {letter}:** {count} times ({percentage:.1f}%)\n\n"
    st.markdown(freq_output)
        
    st.subheader("📌 2-Letter Words")
    st.caption("Look for: EL, LA, DE, EN, UN")
    st.write(", ".join(sorted(two_letter_words)) if two_letter_words else "_None found_")
    
    st.subheader("📌 3-Letter Words")
    st.caption("Look for: QUE, LOS, LAS, CON, POR")
    st.write(", ".join(sorted(three_letter_words)) if three_letter_words else "_None found_")
