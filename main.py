import streamlit as st
st.title('Login Form')

dict = {'divyashelke@gmail.com':123,'shamikakadam@gmail.com':456,'ishamathkar@gmail.com':789}
username = st.text_input('Enter your email: ')
password = st.number_input('Enter your password: ')
btn = st.button('Login here!')

if btn:
    if username in dict:
        if password == dict[username]:
            st.snow()
            st.success('SUCCESSFULLY LOGGED IN!', icon="✅")

        else:
            st.error('Login Error, Wrong Password')
            st.success('FAILED',icon = "❌")
    else:
        st.error('Login Error, Wrong Username')
        st.success('FAILED', icon="❌")