import streamlit as st
import pandas as pd
from xgboost import XGBClassifier
from utils import load_model_and_features, preprocess_input


st.set_page_config(page_title='Prediction', layout='wide')
st.title("🧪 Make a Prediction")
st.logo("images/ovl-logo.png", size="large")
with st.sidebar:
    st.image("images/ovl-logo.png", width=150)

model_path = "assets/xgb_model.joblib"
features_path = "assets/feature_columns.joblib"
scaler_path = "assets/scaler.joblib"
model, feature_cols, scaler = load_model_and_features(model_path, features_path, scaler_path)
numerical_features = ['Population', 'BCG', 'MCV1', 'MCV3', 'OPV1', 'OPV3', 'PCV1', 'PCV3', 'Year']

country_name_to_code_region = {
    "Angola": ["AGO", "Central Africa"],
    "Benin": ["BEN", "Western Africa"],
    "Botswana": ["BWA", "Eastern and Southern Africa"],
    "Burkina Faso": ["BFA", "Western Africa"],
    "Burundi": ["BDI", "Central Africa"],
    "Cameroon": ["CMR", "Central Africa"],
    "Central African Republic": ["CAF", "Central Africa"],
    "Cote d'Ivoire": ["CIV", "Western Africa"],
    "Democratic Republic of the Congo": ["COD", "Central Africa"],
    "Eritrea": ["ERI", "Eastern and Southern Africa"],
    "Eswatini": ["SWZ", "Eastern and Southern Africa"],
    "Ethiopia": ["ETH", "Eastern and Southern Africa"],
    "Gambia": ["GMB", "Western Africa"],
    "Ghana": ["GHA", "Western Africa"],
    "Guinea-Bissau": ["GNB", "Western Africa"],
    "Kenya": ["KEN", "Eastern and Southern Africa"],
    "Lesotho": ["LSO", "Eastern and Southern Africa"],
    "Liberia": ["LBR", "Western Africa"],
    "Madagascar": ["MDG", "Eastern and Southern Africa"],
    "Malawi": ["MWI", "Eastern and Southern Africa"],
    "Mali": ["MLI", "Western Africa"],
    "Mauritania": ["MRT", "Western Africa"],
    "Mauritius": ["MUS", "Eastern and Southern Africa"],
    "Mozambique": ["MOZ", "Eastern and Southern Africa"],
    "Namibia": ["NAM", "Eastern and Southern Africa"],
    "Niger": ["NER", "Western Africa"],
    "Nigeria": ["NGA", "Western Africa"],
    "Republic of Congo": ["COG", "Central Africa"],
    "Rwanda": ["RWA", "Eastern and Southern Africa"],
    "Sao Tome and Principe": ["STP", "Central Africa"],
    "Senegal": ["SEN", "Western Africa"],
    "Seychelles": ["SYC", "Eastern and Southern Africa"],
    "Sierra Leone": ["SLE", "Western Africa"],
    "South Africa": ["ZAF", "Eastern and Southern Africa"],
    "Togo": ["TGO", "Western Africa"],
    "Uganda": ["UGA", "Eastern and Southern Africa"],
    "United Republic of Tanzania": ["TZA", "Eastern and Southern Africa"],
    "Zambia": ["ZMB", "Eastern and Southern Africa"],
    "Zimbabwe": ["ZWE", "Eastern and Southern Africa"]
}

st.subheader("Enter Values:")

col1, col2, col3 = st.columns(3, gap="large", vertical_alignment="top")
with col1:
    pcv1 = st.slider("PCV1 Coverage", 0, 100, 50)
    pcv3 = st.slider("PCV3 Coverage", 0, 100, 60)
    mcv1 = st.slider("MCV1 Coverage", 0, 100, 60)
    mcv3 = st.slider("MCV3 Coverage", 0, 100, 70)


with col2:
    opv1 = st.slider("OPV1 Coverage", 0, 100, 50)
    opv3 = st.slider("OPV3 Coverage", 0, 100, 60)
    bcg = st.slider("BCG Coverage", 0, 100, 80)
    population = st.number_input("Population under 1", value=500000)


with col3:
    year = st.selectbox("Year", list(range(2015, 2030)))
    st.write("")
    selected_country = st.selectbox("Country", list(country_name_to_code_region.keys()))
    st.write("")
    region = country_name_to_code_region[selected_country][1]
    st.text_input("Region", value=region, disabled=True)
    st.write("")
    
    css = """
    <style>
        button {
            height: auto;
            padding-top: 9px !important;
            padding-bottom: 9px !important;
        }
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)

    if st.button("Predict Dropout Likelihood", icon="🪄", type="primary", use_container_width=True):
        country_code = country_name_to_code_region[selected_country][0]

        input_df = pd.DataFrame.from_dict({
            "PCV1": [pcv1],
            "PCV3": [pcv3],
            "MCV1": [mcv1],
            "MCV3": [mcv3],
            "BCG": [bcg],
            "OPV1": [opv1],
            "OPV3": [opv3],
            "Population": [population],
            "Year": [year],
            "CountryCode": [country_code],
            "Region": [region]
        })
        X_processed = preprocess_input(input_df, feature_cols, scaler, numerical_features)
        pred = model.predict(X_processed)[0]
        proba = model.predict_proba(X_processed)[0][1]

        # st.success(f"**Predicted Dropout Class:** {'Dropout' if pred==1 else 'No Dropout'}")
        # st.info(f"**Dropout Probability:** {proba:.2f}")

        # Store prediction results in session state
        st.session_state.pred_class = 'Dropout' if pred == 1 else 'No Dropout'
        st.session_state.pred_proba = proba
        st.session_state.show_result = True  # Trigger result display

# Show the result outside the if-block
if st.session_state.get("show_result", False):
    st.success(f"**Predicted Dropout Class:** {st.session_state.pred_class}")
    st.info(f"**Dropout Probability:** {st.session_state.pred_proba:.2f}")