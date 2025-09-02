import streamlit as st

st.set_page_config(page_title='VaxTrackAI', layout='wide')

st.logo("images/ovl-logo.png", size="large")
with st.sidebar:
    st.image("images/ovl-logo.png", width=150)

st.title("💉 VaxTrackAI :robot:")
# st.image("images/hero.png")
# st.subheader("Africa Vaccine Dropout Classifier")
st.markdown("""
Welcome to VaxTrackAI, the Africa Vaccine Dropout Prediction App. 

**Dropout** in immunization programs is typically defined as a coverage rate greater than or equal to 10%. This means that if the percentage of children who start the vaccination series but do not complete it is 10% or more, it's considered a dropout issue. A dropout rate above **10%** often indicates a problem with program utilization or service delivery.

This tool predicts the likelihood that a child will **drop out between DTP1 and DTP3** vaccinations based on:
- Antigen coverage (DTP1, DTP3, PCV1, PCV3, MCV1, MCV3, OPV1, OPV3, BCG)
- Country
- Region
- Population data (population under 1 year old)

Navigate between **Predict** and **Insights** pages to explore the model.
""")
# st.markdown("---")
st.write("")

st.subheader("💉 Antigen Overview")

antigen_tabs = st.tabs([
    "DTP1", "DTP3", "PCV1", "PCV3", 
    "MCV1", "MCV3", "OPV1", "OPV3", "BCG"
])

# Define the descriptions
descriptions = {
    "DTP1": "**DTP1** is the first dose of the DTP vaccine, which protects against Diphtheria, Tetanus, and Pertussis (Whooping cough). Given at 6 weeks of age.",
    
    "DTP3": "**DTP3** is the third and final dose in the DTP series. Completion of this dose is critical for full protection against these deadly diseases.",
    
    "PCV1": "**PCV1** is the first dose of the Pneumococcal Conjugate Vaccine. It protects infants against pneumonia, meningitis, and sepsis. Typically given at 6 weeks.",
    
    "PCV3": "**PCV3** is the third dose in the PCV vaccine series, ensuring long-term immunity against pneumococcal diseases in young children.",
    
    "MCV1": "**MCV1** is the first dose of the Measles-Containing Vaccine, usually administered at 9 months of age to protect against measles.",
    
    "MCV3": "**MCV3** (or second measles dose in some countries) boosts immunity and increases protection against measles in older children.",
    
    "OPV1": "**OPV1** is the first dose of the Oral Polio Vaccine, which protects against poliovirus. Typically given at birth or 6 weeks.",
    
    "OPV3": "**OPV3** is the final dose in the OPV series, crucial for building strong immunity against polio, especially in high-risk areas.",
    
    "BCG": "**BCG** is a single-dose vaccine given at birth to protect against severe forms of tuberculosis, especially TB meningitis in children."
}

# Render content inside each tab
for tab, antigen in zip(antigen_tabs, descriptions):
    with tab:
        st.markdown(descriptions[antigen])

st.write("")
st.write("")

st.subheader("🔢 Model Evaluation Metrics")
st.markdown("""
        - VaxTrackAI was built by training a Extreme Gradient Boost (XGBoost) model on [population](https://idataportal.afro.who.int/dataset/population/resource/28a1db7b-2c8f-4433-bef2-e902d5a9cf09?view_id=5e08af5b-41c2-478b-b9b6-54d9525d7b94) and [vaccination coverage](https://idataportal.afro.who.int/dataset/ri_coverage_all_antigens/resource/7c5b7d34-b285-4bb8-ad66-ac23c8b23689?view_id=a28630bf-7e25-4da5-b424-eaa377128718) data from WHO African Region Data Portal.
        - The model achieved accuracy of **95%** and an AUC score of **98%**.
        - Features such as MCV3 and BCG are the most influential features for the model's predictions. PCV1 is the next most important, followed by MCV1, and Population.
""")