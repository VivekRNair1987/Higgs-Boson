import joblib
import matplotlib as plt
import pandas as pd
import numpy as np
import os
from sklearn.tree import DecisionTreeClassifier

# Captures the path of current folder
curr_path = os.path.dirname(os.path.realpath(__file__))


feat_cols = ['DER_mass_MMC', 'DER_mass_transverse_met_lep', 'DER_prodeta_jet_jet',
       'DER_deltar_tau_lep', 'DER_pt_tot', 'DER_met_phi_centrality',
       'DER_lep_eta_centrality', 'PRI_tau_pt', 'PRI_tau_eta', 'PRI_tau_phi',
       'PRI_lep_pt', 'PRI_lep_eta', 'PRI_lep_phi', 'PRI_met', 'PRI_met_phi',
       'PRI_jet_num', 'PRI_jet_leading_pt', 'PRI_jet_leading_eta',
       'PRI_jet_leading_phi', 'PRI_jet_subleading_pt',
       'PRI_jet_subleading_eta', 'PRI_jet_subleading_phi', 'Weight']

final = joblib.load(curr_path + r"\final_bestmodel11.joblib")
print(final)

print(final)
def predict_duration(attributes: np.ndarray):
    """ Returns Bike Trip Duration value"""

    pred = final.predict(attributes)
    print("Label predicted")
    print(pred)
    return int(pred[0])