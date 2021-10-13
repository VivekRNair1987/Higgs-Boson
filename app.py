##pip install streamlit
import streamlit as st
from model import predict_duration
import numpy as np

st.set_page_config(page_title="HIGGS BOSON App",
                   page_icon="🛴", layout="wide")


with st.form("prediction_form"):

    st.header("Enter the Deciding Factors:")

    DER_mass_MMC = st.number_input("DER_mass_MMC: ", value=0, format="%d")
    DER_mass_transverse_met_lep = st.number_input("DER_mass_transverse_met_lep: ")
    DER_mass_vis = st.number_input("DER_mass_vis: ")
    DER_deltar_tau_lep = st.number_input("DER_deltar_tau_lep: ")
    DER_pt_tot = st.number_input("DER_pt_tot: ")
    DER_met_phi_centrality = st.number_input("DER_met_phi_centrality: ")
    PRI_tau_pt = st.number_input("PRI_tau_pt: ")
    PRI_tau_eta = st.number_input("PRI_tau_eta: ")
    PRI_tau_phi = st.number_input("PRI_tau_phi: ")
    PRI_lep_pt = st.number_input("PRI_lep_pt: ")
    PRI_lep_eta = st.number_input("PRI_lep_eta: ")
    PRI_lep_phi = st.number_input("PRI_lep_phi: ")
    PRI_met = st.number_input(" PRI_met: ")
    PRI_met_phi = st.number_input("PRI_met_phi: ")
    PRI_met_sumet = st.number_input("PRI_met_sumet: ")
    PRI_jet_leading_pt = st.number_input("PRI_jet_leading_pt: ")
    PRI_jet_leading_eta = st.number_input("PRI_jet_leading_eta: ")
    PRI_jet_leading_phi = st.number_input("PRI_jet_leading_phi: ")
    PRI_jet_all_pt = st.number_input("PRI_jet_all_pt: ")
    Weight = st.number_input("Weight: ")

    submit_val = st.form_submit_button("Predict Label")

if submit_val:
    # If submit is pressed == True
    attribute = np.array([DER_mass_MMC,DER_mass_transverse_met_lep, DER_mass_vis,
       DER_deltar_tau_lep, DER_pt_tot, DER_met_phi_centrality,
       PRI_tau_pt, PRI_tau_eta, PRI_tau_phi, PRI_lep_pt, PRI_lep_eta,
       PRI_lep_phi, PRI_met, PRI_met_phi, PRI_met_sumet,
       PRI_jet_leading_pt, PRI_jet_leading_eta, PRI_jet_leading_phi,
       PRI_jet_all_pt, Weight]).reshape(1,-1)

    print (attribute)
    print(attribute.shape)
    if attribute.shape == (1,20):
        print("attributes valid")
        

        value = predict_duration(attributes= attribute)


        st.header("Here are the results:")
        st.success(f"The label predicted is {value}")