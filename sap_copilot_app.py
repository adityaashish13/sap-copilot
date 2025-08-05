import streamlit as st

st.set_page_config(page_title="SAP Copilot", layout="wide")
st.title("🤖 SAP Basis AI Copilot")

# -------------------- Static Inputs --------------------
sap_version = "ECC 6.0"
db = "Oracle 19c"
os = "Windows 2019"
env = "PROD"
client = "800"

with st.expander("📌 System Info", expanded=True):
    st.markdown(f"**SAP Version:** {sap_version}")
    st.markdown(f"**Database:** {db}")
    st.markdown(f"**OS:** {os}")
    st.markdown(f"**Environment:** {env}")
    st.markdown(f"**Client:** {client}")

# -------------------- Use Case 1: Error Resolver --------------------
st.subheader("1️⃣ Error Resolver")
logs_input = st.text_area("Paste log snippet", value="ORA-00001: Unique constraint violated")
if logs_input:
    st.success("✔️ Root cause identified: ORA-00001 - Unique constraint violated.")
    st.info("Recommended Action: Check primary key constraints on table ZFI_JOBS.")
    st.warning("Related SAP Notes: 1234567, 3344556")

# -------------------- Use Case 2: Knowledge Search --------------------
st.subheader("2️⃣ Knowledge Search")
query = st.text_input("Enter your SAP query", value="How to configure transport routes")
if query:
    st.write("Result:")
    st.markdown("""
    **Use transaction STMS for transport configuration.**

    **Steps:**
    1. Login to domain controller  
    2. Go to STMS > Overview  
    3. Configure transport routes
    """)

# -------------------- Use Case 3: Internal Ticket Generator --------------------
st.subheader("3️⃣ Internal Ticket Generator")
issue_summary = st.text_input("Issue Summary", value="SAP job failure")
steps_taken = st.text_area("Steps Taken", value="Job re-triggered, logs analyzed")
impact = st.text_area("Impact", value="Delay in month-end closing")

if issue_summary and steps_taken and impact:
    st.markdown("""
    **Generated Ticket:**

    ---
    **Subject:** SAP job failure  

    **Description:**  
    SAP job failure  

    **Steps Taken:**  
    Job re-triggered, logs analyzed  

    **Impact:**  
    Delay in month-end closing  

    **Priority:** High
    """)

# -------------------- Use Case 4: RCA Email Draft --------------------
st.subheader("4️⃣ RCA Email Draft")
rca_incident = st.text_input("Root Cause", value="Job failed due to missing variant, recreated")
steps_taken_rca = st.text_area("Action Taken", value="Recreated variant and rescheduled job")
issue_summary_rca = st.text_input("Issue Summary for RCA", value="Background job failure")

if rca_incident and steps_taken_rca and issue_summary_rca:
    st.markdown(f"""
    **Email Draft:**

    **Subject:** RCA for SAP Error on {env} - {issue_summary_rca}

    Dear Management,

    The issue on {env} system related to "{issue_summary_rca}" has been resolved.

    **Root Cause:** {rca_incident}  
    **Action Taken:** {steps_taken_rca}  

    Please let us know if you need further details.

    Regards,  
    SAP Basis Team
    """)

# -------------------- Use Case 5: SAP/Oracle Support Ticket Draft --------------------
st.subheader("5️⃣ SAP/Oracle Support Ticket Draft")
support_logs = st.text_area("Paste Error Logs", value="ORA-12541: TNS:no listener")
issue_summary_sup = st.text_input("Issue Summary", value="Database connectivity error")
steps_taken_sup = st.text_area("Steps Taken", value="Restarted listener and verified TNS settings")
impact_sup = st.text_area("Impact", value="Users unable to log in to SAP")

if support_logs and issue_summary_sup and steps_taken_sup and impact_sup:
    st.markdown(f"""
    **Support Ticket Draft:**

    **Subject:** {issue_summary_sup} on {env}

    **Description:**  
    {support_logs}  

    **System Info:**  
    SAP Version: {sap_version}  
    DB: {db}  
    OS: {os}  
    Client: {client}  

    **Steps Taken:**  
    {steps_taken_sup}  

    **Impact:**  
    {impact_sup}  

    **Component:** BC-OP-DB-ORA (example)
    """)
