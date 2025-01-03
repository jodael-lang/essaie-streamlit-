import streamlit as st

st.title("Prédiction de la tranche d'âge des individus")

st.write("ceci est un exemple d'une application qui prédit la tranche d'âge des individus en foncions des informations recceuillies")

nom = st.text_input("Entrer votre nom")
if nom:
    st.write("Bonjour ",nom)
    
age = st.number_input("Entrer votre age", min_value = 0, max_value = 100, step = 1)

sexe = st.selectbox("Choisissez votre sexe",["F","M","Autres"])

def predire_m(age, sexe):
    if age < 18:
        #st.write("mineur")
        if age <= 12:
            st.write("mineur et enfant")
        elif age <= 15:
            st.write("mineur et puber")
        else:
            st.write("mineur et adolescent")
    else:
        st.write("majeur")

if st.button("Prédire"):
    pred = predire_m(age,sexe)
    st.write(f"Vous êtes probablement **{pred}**")
     
