import streamlit as st

def double_until_100(start_value):
    values = [start_value]
    while values[-1] < 100:
        values.append(values[-1] * 2)
    return values

st.title("🔢 Number Doubler (Until 100)")

start_value = st.number_input("Enter a number:", min_value=1, step=1, value=1)

if st.button("Double the Number!"):
    result = double_until_100(start_value)
    
    st.write("### Output Sequence:")
    st.write(" → ".join(map(str, result)))

st.markdown("""
<div class="footer">
    <p>Secure Number double v1.0 | Stay Safe Online | <a href="https://github.com/SitesByKashan">Made By M Kashan Malik Awan</a> </p>
</div>
""", unsafe_allow_html=True)