import streamlit as st
import pandas as pd
import plotly.express as px
import base64


def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


@st.cache_data
def load_data():
    df = pd.read_csv("housing_info.csv", low_memory=False)
    df = df.dropna(subset=["Location"])
    return df


def main():

    img_file_path = "image/blue_house.jpg"
    img_base64 = get_img_as_base64(img_file_path)

    page_bg_img = f"""
    <style>

    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
        background-color: rgba(0, 0, 0, 0);
    }}

    [data-testid="stSidebar"] {{
        background: rgba(255, 255, 255, 0.7);
    }}

    [data-testid="stToolbar"] {{
        right: 2rem;
    }}

    .main-header {{
        font-size: 32px;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        margin-top: 20px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }}

    .dashboard-container {{
        margin-top: 20px;
        margin-bottom: 20px;
        background: rgba(255, 255, 255, 0.88);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
    }}

    /* ===== FIX METRICS TEXT COLOR ===== */
    div[data-testid="stMetric"] {{
        background: rgba(255, 255, 255, 0.98);
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.15);
    }}

    div[data-testid="stMetric"] * {{
        color: #000000 !important;
    }}

    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.markdown("""
        <div class="main-header">
            Dashboard: History of Kuala Lumpur Housing Prices
        </div>
    """, unsafe_allow_html=True)

    df = load_data()

    st.markdown('<div class="dashboard-container">', unsafe_allow_html=True)

    # Filter
    all_locations = sorted(df["Location"].unique().tolist())

    selected_locations = st.multiselect(
        "Filter by Location (leave empty to show all)",
        options=all_locations,
        default=[]
    )

    filtered = df[df["Location"].isin(selected_locations)] if selected_locations else df

    # KPI ROW
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Count of Location",
        f"{filtered['Location'].nunique():,}"
    )

    col2.metric(
        "Average of Price",
        f"RM {filtered['Price'].mean():,.0f}"
    )

    col3.metric(
        "Average of SizeValue",
        f"{filtered['SizeValue'].mean():,.0f} sq ft"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("#### Total Property Prices by Location")

        price_by_loc = (
            filtered.groupby("Location")["Price"]
            .sum()
            .sort_values(ascending=False)
            .head(15)
            .reset_index()
        )

        fig1 = px.bar(
            price_by_loc,
            x="Price",
            y="Location",
            orientation="h",
            labels={"Price": "Sum of Price", "Location": ""}
        )

        fig1.update_layout(
            yaxis={"categoryorder": "total ascending"},
            height=420,
            margin=dict(l=0, r=0, t=10, b=0)
        )

        st.plotly_chart(fig1, use_container_width=True)

    with col_b:
        st.markdown("#### Distribution of Rooms, Bathrooms and Car Parks by Furnishing")

        furn = (
            filtered.groupby("Furnishing")[["Rooms", "Bathrooms", "Car Parks"]]
            .sum()
            .reset_index()
            .melt(id_vars="Furnishing", var_name="Metric", value_name="Sum")
        )

        furn["Percent"] = furn.groupby("Furnishing")["Sum"].transform(
            lambda s: 100 * s / s.sum()
        )

        fig2 = px.bar(
            furn,
            x="Furnishing",
            y="Percent",
            color="Metric",
            labels={"Percent": "% of Total"}
        )

        fig2.update_layout(height=420, margin=dict(l=0, r=0, t=10, b=0))

        st.plotly_chart(fig2, use_container_width=True)

    col_c, col_d = st.columns(2)

    with col_c:
        st.markdown("#### Proportion of Property Size Types")

        size_type = filtered["SizeType"].value_counts().reset_index()
        size_type.columns = ["SizeType", "Count"]

        fig3 = px.pie(size_type, names="SizeType", values="Count", hole=0.5)

        fig3.update_layout(height=380, margin=dict(l=0, r=0, t=10, b=0))

        st.plotly_chart(fig3, use_container_width=True)

    with col_d:
        st.markdown("#### Total of Property Type")

        prop_type = (
            filtered.groupby("Property Type")["Price"]
            .sum()
            .sort_values(ascending=False)
            .head(12)
            .reset_index()
        )

        fig4 = px.treemap(
            prop_type,
            path=["Property Type"],
            values="Price"
        )

        fig4.update_layout(height=380, margin=dict(l=0, r=0, t=10, b=0))

        st.plotly_chart(fig4, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()