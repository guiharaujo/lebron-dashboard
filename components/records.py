import streamlit as st
from data.constants import RECORDS


def render() -> None:
    st.subheader("Historical Records")

    for record in RECORDS:
        if record["highlight"]:
            st.markdown(
                f"""
                <div style="
                    border: 2px solid #FDB927;
                    border-radius: 10px;
                    padding: 16px 20px;
                    background: linear-gradient(135deg, #1a1205, #2a1f00);
                    margin-bottom: 12px;
                ">
                    <span style="font-size:1.5rem">{record['icon']}</span>
                    <span style="
                        color: #FDB927;
                        font-size: 1.15rem;
                        font-weight: 700;
                        margin-left: 8px;
                    ">{record['title']}</span>
                    <br>
                    <span style="
                        color: white;
                        font-size: 1.4rem;
                        font-weight: 700;
                    ">{record['value']}</span>
                    <p style="color:#bbb; margin: 6px 0 0; font-size:0.9rem">
                        {record['detail']}
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            with st.expander(f"{record['icon']}  {record['title']} — **{record['value']}**"):
                st.write(record["detail"])
