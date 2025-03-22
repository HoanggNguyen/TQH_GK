import pandas as pd
import altair as alt
import seaborn as sns
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from streamlit_option_menu import option_menu

color_palette = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#96EFFF', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
 
st.set_page_config(
    page_title="US Population Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded")

# Custom CSS for better styling
st.markdown("""
    <style>
    .reportview-container {
        background: #0e1117;
    }
    .sidebar .sidebar-content {
        background: #262730;
    }
    .Widget>label {
        color: #fafafa;
        font-family: 'Roboto', sans-serif;
    }
    .stTextInput>div>div>input {
        color: #fafafa;
    }
    .stSelectbox>div>div>select {
        color: #fafafa;
    }
    .stTitle {
        font-weight: bold;
        color: #ff4b4b;
    }
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap');
    body {
        font-family: 'Roboto', sans-serif;
    }
    .stApp {
        background-color: #41644A; 
    }
    .page-title {
        font-family: 'Arial', sans-serif;  
        font-size: 36px;                   
        font-weight: bold;                
        color: #fdf5e6;                    
        text-align: center;               
        margin-top: 20px;                  
        margin-bottom: 20px;              
        border-bottom: 2px solid #3498db;  
        padding-bottom: 10px;             
    }
    .home-page-desc {
        font-family: 'Arial', sans-serif;  
        font-size: 18px;                   
        color: white;     
        text-wrap: balance;               
        text-align: left;               
        margin-top: 20px;                  
        margin-bottom: 20px;  
        font-weight: bold;           
    }

    .custom1 {
            background-color: #528B8B;
            padding: 20px;
    }
    .custom2 {
            background-color: #4682B4;
            padding: 20px;
    }
    .custom3 {
            background-color: #CD5C5C;
            padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Enable dark theme for Altair charts
alt.themes.enable("dark")

DATAPATH = "./country_comparison_large_dataset_vn.csv"
df = pd.read_csv(DATAPATH)

with st.sidebar:
    selected_option = option_menu(
        menu_title="Tác vụ",  # Required
        options=["Trang chính", "Kinh tế và dân số", "Xã hội và sức khỏe", "Năng lượng, môi trường và cơ sở hạ tầng", "Quản trị"],  # Required
        icons=["house-door-fill", "bar-chart-line-fill", "person-heart", "lightning-fill", "buildings-fill"],  # Optional
        menu_icon="cast",  # Optional
        default_index=0,  # Optional
        styles={
            "container": {"padding": "5!important", "background-color": "#0e1117"},
            "icon": {"font-size": "25px", "color": "#ff4b4b"},
            "nav-link": {
                "font-size": "17px", 
                "font-family": "Open Sans, sans-serif", 
                "text-align": "left", 
                "margin": "0px",
            },
            "nav-link-selected": {
                "background-color": "#ffc757", 
                "font-family": "Open Sans, sans-serif",
                "font-size": "18px",
                "font-weight": "bold",
                "color": "#0e1117",
            },
        },
    )

# Updated chart layout configuration with better contrast
def get_chart_layout():
    return {
        'plot_bgcolor': 'rgba(253, 245, 230, 0.7)',  # Custom plot background color (light)
        'paper_bgcolor': 'rgba(253, 245, 230, 1)',   # Custom chart background color
        'title': "", 
        'xaxis_title_font': dict(color="#0d0d0d", weight="bold"),
        'yaxis_title_font': dict(color="#0d0d0d", weight="bold"),
        'xaxis': dict(
            showgrid=True, 
            gridcolor='rgba(0, 0, 0, 0.5)',  # Light grid lines
            tickfont=dict(color='#696969'),  # Tick font color
            title_font=dict(color='#696969')  # Axis title font color
        ),
        'yaxis': dict(
            showgrid=True, 
            gridcolor='rgba(0, 0, 0, 0.5)',  # Light grid lines
            tickfont=dict(color='#696969'),  # Tick font color
            title_font=dict(color='#696969')  # Axis title font color
        ),
        'legend': dict(
            title=dict(
                text='Quốc gia',  # Legend title
                font=dict(color='#696969', weight="bold")  # Legend title styling
            ),
            font=dict(color='#696969'),  # Legend text color
            bgcolor="rgba(253, 245, 230, 0.7)"  # Legend background color
        ),
        
        'font': dict(
            color='black'  # General text color
        )
    }

if selected_option == "Trang chính":
    # CSS styles for the main page
    st.markdown(
        """
        <style>
        .main {
            padding: 2rem;
            background-color: ##f0f2f6;
        }
        .title {
            font-size: 3rem;
            font-weight: bold;
            color: #FFBD73;
            text-align: center;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .subtitle {
            font-size: 1.5rem;
            color: #FFBD73;
            text-align: center;
            font-weight: bold;
            margin-bottom: 2rem;
        }
        .section-title {
            font-size: 2rem;
            font-weight: bold;
            color: #96EFFF;
            margin-top: 2rem;
            margin-bottom: 1rem;
            text-align: center;
        }
        .metric-card {
            border: 2px solid #1f77b4;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            margin: 10px;
            background-color: #fdf5e6;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
        }
        .metric-value {
            font-size: 28px;
            font-weight: bold;
            color: #15B392;
        }
        .metric-label {
            font-size: 16px;
            color: #555;
            margin-top: 5px;
        }
        .info-box {
            background-color: #fdf5e6;
            border-radius: 10px;
            padding: 20px;
            margin: 10px 0;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100px;
        }
        .info-box h3 {
            color: #1f77b4;
            margin-bottom: 10px;
        }
        .info-box p {
            font-size: 20px;
            color: #333;
            line-height: 1.6;
            font-weight: bold;
            text-wrap: balance;
            text-align: center;
            margin: 0;
        }
        .info-item {
            font-size: 18px;
            height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #333;
            border-radius: 10px;
            background-color: #fdf5e6;
            font-weight: bold;
            margin-bottom: 10px;
            text-align: center;
        }
        .tab-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            margin-top: 20px;
        }
        .tab-description {
            flex-basis: calc(50% - 10px);
            background-color: #fdf5e6;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        .tab-description:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
        }
        .tab-title {
            font-weight: bold;
            color: #15B392;
            font-size: 1.5rem;
            text-align: center;
            margin-bottom: 10px;
        }
        .tab-description p {
            font-size: 16px;
            color: #333;
            text-align: center;
            text-wrap: balance;
            justify-content: center;
            align-items: center;
            line-height: 1.6;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 class='title'>Bảng Điều Khiển Phân Tích Dữ Liệu Toàn Cầu</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Khám phá xu hướng kinh tế, xã hội và môi trường trên toàn cầu</p>", unsafe_allow_html=True)

    # Dataset purpose
    st.markdown("<h2 class='section-title'>Mục Đích của Bộ Dữ Liệu</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="info-box">
            <p>Bộ dữ liệu này cung cấp một cái nhìn toàn diện về các chỉ số phát triển của các quốc gia trên toàn cầu. 
            Nó bao gồm nhiều lĩnh vực như kinh tế, dân số, y tế, giáo dục, công nghệ, môi trường, và quản trị. 
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col_purpose1, col_purpose2 = st.columns(2)
    with col_purpose1:
        st.markdown("<div class='info-item'>Hiểu rõ hơn về xu hướng phát triển toàn cầu</div>", unsafe_allow_html=True)
        st.markdown("<div class='info-item'>So sánh các nước Trung Quốc, Ấn Độ, Canada, Úc, Mỹ, Nga</div>", unsafe_allow_html=True)
    with col_purpose2:
        st.markdown("<div class='info-item'>Phân tích mối quan hệ giữa các chỉ số khác nhau</div>", unsafe_allow_html=True)
        st.markdown("<div class='info-item'>Cung cấp cơ sở dữ liệu cho việc hoạch định chính sách và nghiên cứu</div>", unsafe_allow_html=True)
    
    # Dataset overview
    st.markdown("<h2 class='section-title'>Tổng Quan Bộ Dữ Liệu</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-value">{len(df['Quốc gia'].unique())}</div>
                <div class="metric-label" style="font-weight: bold">Quốc gia</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-value">{df['Năm'].min()} - {df['Năm'].max()}</div>
                <div class="metric-label" style="font-weight: bold">Phạm vi Năm</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-value">{df.size:,}</div>
                <div class="metric-label" style="font-weight: bold">Điểm Dữ liệu</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Explore Topics
    st.markdown("<h2 class='section-title'>Khám Phá Các Chủ Đề</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="tab-container">
            <div class="tab-description"">
                <h3 class="tab-title">Kinh tế và dân số</h3>
                <p>Phân tích chi tiết về GDP, GDP bình quân đầu người, lạm phát, dân số, và các chỉ số liên quan. Hiểu rõ về tăng trưởng kinh tế và biến động dân số của các quốc gia.</p>
            </div>
            <div class="tab-description">
                <h3 class="tab-title">Xã hội và sức khỏe</h3>
                <p>Khám phá các chỉ số về tuổi thọ, chi tiêu y tế, tỷ lệ bác sĩ-bệnh nhân, tỷ lệ biết chữ, và chỉ số phát triển con người. Đánh giá chất lượng cuộc sống và phúc lợi xã hội.</p>
            </div>
            <div class="tab-description" >
                <h3 class="tab-title">Năng lượng, môi trường và cơ sở hạ tầng</h3>
                <p>Phân tích tiêu thụ năng lượng, tỷ lệ năng lượng tái tạo, phát thải CO2, và cơ sở hạ tầng. Hiểu rõ về sự phát triển bền vững và thách thức môi trường.</p>
            </div>
            <div class="tab-description">
                <h3 class="tab-title">Quản trị</h3>
                <p>Đánh giá hiệu quả quản trị thông qua chỉ số cảm nhận tham nhũng, chỉ số tự do báo chí, và tỷ lệ tham gia bầu cử. Hiểu rõ về tình hình dân chủ và minh bạch trong quản lý nhà nước.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

elif selected_option == "Kinh tế và dân số":
    st.markdown('''<div class="page-title">Kinh tế & Dân số</div>''', unsafe_allow_html=True)
    
    # Improved filters layout
    slt1, slt2 = st.columns((1,1))
    min_year, max_year = int(df['Năm'].min()), int(df['Năm'].max())

    with slt1:
        selected_countries = st.multiselect("Chọn các quốc gia để so sánh", options=df['Quốc gia'].unique(), default=df['Quốc gia'].unique()[:], key="Quốc gia_selection")
    with slt2:
        selected_year = st.selectbox("Chọn năm cụ thể", options=range(min_year, max_year + 1), index=max_year - min_year, key="Năm_selection")

    selected_year_range = st.slider("Chọn khoảng năm", min_value=min_year, max_value=max_year, value=(min_year, max_year), key="Năm_range")
    # Filter the dataset based on selections
    # Filter the dataset based on selections
    filtered_df = df[(df['Năm'] >= selected_year_range[0]) & 
                     (df['Năm'] <= selected_year_range[1])]
    # Filter specific countries
    filtered_df_countries =  df[(df['Quốc gia'].isin(selected_countries)) & 
                     (df['Năm'] >= selected_year_range[0]) & 
                     (df['Năm'] <= selected_year_range[1])]
    # Filter specific Năm
    filtered_df_Năm = df[df['Năm'] == selected_year]

    filtered_df_countries_Năm = filtered_df_Năm[(filtered_df_Năm['Quốc gia'].isin(selected_countries))]

    
    col1, col2, col3 = st.columns([1, 2, 2])
    
    with col1:
        st.markdown('''<div class="custom3" style="height: 525px;">
                        <h6><center>GDP VÀ DÂN SỐ</center></h6>
                        <p>GDP và dân số là hai chỉ số thiết yếu, cung cấp cái nhìn toàn diện về tiềm lực kinh tế và quy mô dân số, phát triển của một quốc gia.</p>
                    </div>
                    ''', unsafe_allow_html=True)
    with col2:
        title = f"GDP CỦA CÁC QUỐC GIA TỪ NĂM {selected_year_range[0]} ĐẾN {selected_year_range[1]}"
        st.markdown(f'''<div class="custom3", style="height: 75px;">
                            <center><strong>{title}</strong></center>
                        </div>
                    ''', unsafe_allow_html=True)
        if selected_countries:
            gdp_data = filtered_df_countries
            
            fig = px.line(gdp_data, 
                        x='Năm', 
                        y='GDP (nghìn tỷ USD)', 
                        color='Quốc gia',
                        markers=True,
                        color_discrete_sequence=color_palette)

            # Configure the logarithmic y-axis with better settings
            fig.update_yaxes(
                type="log",
                title='GDP (Nghìn tỷ USD)',
                ticktext=['1', '2', '3', '4', '5', '10', '20', '30'],
                tickvals=[1, 2, 3, 4, 5, 10, 20, 30],
                range=[0, 1.5],  # log10 range for better visualization
                showgrid=True,
                gridwidth=1,
                gridcolor='rgba(128, 128, 128, 0.15)',
                showline=True,
                linewidth=1,
                linecolor='rgba(128, 128, 128, 0.4)'
            )

            # Improve the x-axis
            fig.update_xaxes(
                title='Năm',
                dtick=5,  # Show Năm marks every 5 Năms
                gridcolor='rgba(128, 128, 128, 0.15)',
                gridwidth=1,
                showline=True,
                linewidth=1,
                linecolor='rgba(128, 128, 128, 0.4)'
            )

            # Get the base layout and update it with additional settings
            layout = get_chart_layout()
            layout.update(
                height=450,
                margin=dict(l=60, r=30, t=30, b=50),
                hovermode='x unified',
            )

            # Update layout with merged settings
            fig.update_layout(**layout)

            # Improve marker and line styling
            fig.update_traces(
                marker=dict(
                    size=6,  # Slightly smaller markers
                    line=dict(width=1, color='DarkSlateGrey')
                ),
                line=dict(width=1),  # Slightly thinner lines
                hovertemplate='%{y:.1f} Nghìn Tỷ USD<extra></extra>'  # Simpler hover template
            )
            fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
            # Display the chart
            st.plotly_chart(fig, use_container_width=True)
    with col3:
        title = f'DÂN SỐ CỦA CÁC QUỐC GIA TỪ NĂM {selected_year_range[0]} ĐẾN {selected_year_range[1]}'
        st.markdown(f'''<div class="custom3", style="height: 75px;">
                    <center><strong>{title}</strong></center>
                    </div>
                    ''', unsafe_allow_html=True)

        if selected_countries:
            pop_data = filtered_df_countries
            
            fig = px.line(pop_data,
                        x='Năm',
                        y='Dân số (triệu người)',
                        color='Quốc gia', 
                        markers=True,
                        color_discrete_sequence=color_palette)

            # Configure the logarithmic y-axis with better settings
            fig.update_yaxes(
                type="log",
                title='Dân số (triệu người)',
                ticktext=['10', '20', '50', '100', '200', '500', '1000', '2000'],
                tickvals=[10, 20, 50, 100, 200, 500, 1000, 2000],
                range=[1, 3.3],  # log10 of 10 to 2000
                showgrid=True,
                gridwidth=1,
                gridcolor='rgba(128, 128, 128, 0.2)',
            )

            # Improve the x-axis
            fig.update_xaxes(
                title='Năm',
                dtick=5,  # Show Năm marks every 5 Năms
                gridcolor='rgba(128, 128, 128, 0.2)',
                gridwidth=1,
            )

            # Get the base layout and update it with additional settings
            layout = get_chart_layout()
            layout.update(
                margin=dict(l=60, r=30, t=50, b=50),
                hovermode='x unified'
            )

            # Update layout with merged settings
            fig.update_layout(**layout)

            # Improve marker and line styling
            fig.update_traces(
                marker=dict(
                    size=6,
                    line=dict(width=1, color='DarkSlateGrey')
                ),
                line=dict(width=1),
                hovertemplate='%{y:.0f} Triệu Người<extra></extra>'
            )
            fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
            # Display the chart
            st.plotly_chart(fig, use_container_width=True)
    
    # Second row - Population metrics
    col4, col5, col6 = st.columns([1, 2, 2])
    
    with col4:
        st.markdown('''<div class="custom2", style="height: 525px;">
                        <h6><center>CÁC MỐI TƯƠNG QUAN KINH TẾ VÀ DÂN SỐ</center></h6>
                        <p>GDP bình quân đầu người và tỷ lệ tham gia lao động là hai yếu tố then chốt, không chỉ phản ánh mức độ phát triển kinh tế mà còn thể hiện sức khỏe và quy mô của thị trường lao động trong một quốc gia.</p>
                    ''', unsafe_allow_html=True)
    with col5:
        title = f'DÂN SỐ VÀ GDP BÌNH QUÂN ĐẦU NGƯỜI THEO QUY MÔ GDP VÀO NĂM {selected_year}'
        st.markdown(f'''<div class="custom2", style="height: 75px;">
                    <center><strong>{title}</strong></center>
                     </div>
                    ''', unsafe_allow_html=True)
        if selected_countries:
            pop_gdp_data = filtered_df_countries_Năm
            
            fig = px.scatter(pop_gdp_data,
                           x='Dân số (triệu người)',
                           y='GDP bình quân đầu người (USD)',
                           size='GDP (nghìn tỷ USD)', 
                           color='Quốc gia',
                           hover_name='Quốc gia',
                           size_max=30,
                           color_discrete_sequence=color_palette)
                # Configure the logarithmic y-axis with better settings

            fig.update_layout(
            **get_chart_layout(),
            annotations=[
                dict(
                    xref='paper', yref='paper',
                    x=0.5, y=1.15,  # Position at the top center of the chart
                    showarrow=False,
                    text="Kích thước bong bóng biểu thị quy mô GDP của các quốc gia",
                    font=dict(size=16, color="DarkSlateGrey")
                )
            ]
            )
            fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
            st.plotly_chart(fig)
    with col6:
        title=f'DÂN SỐ VÀ TỶ LỆ THAM GIA LAO ĐỘNG THEO QUY MÔ GDP VÀO NĂM {selected_year}'
        st.markdown(f'''<div class="custom2", style="height: 75px;">
                    <center><strong>{title}</strong></center>
                     </div>
                    ''', unsafe_allow_html=True)
        pop_gdp_data = filtered_df_countries_Năm
        
        fig = px.scatter(pop_gdp_data,
                           x='Dân số (triệu người)',
                           y='Tỷ lệ tham gia lực lượng lao động (%)',
                           size='GDP (nghìn tỷ USD)', 
                           color='Quốc gia',
                           labels={'Dân số (triệu người)': 'Dân số (triệu người)',
                                'Tỷ lệ tham gia lực lượng lao động (%)': 'Tỷ lệ tham gia lao động (%)'},
                           hover_name='Quốc gia',
                           size_max=30,
                           color_discrete_sequence=color_palette)
        
        fig.update_layout(
            **get_chart_layout(),
            annotations=[
                dict(
                    xref='paper', yref='paper',
                    x=0.5, y=1.15,  # Position at the top center of the chart
                    showarrow=False,
                    text="Kích thước bong bóng biểu thị quy mô GDP của các quốc gia",
                    font=dict(size=16, color="DarkSlateGrey")
                )
            ]
        )
        fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
        st.plotly_chart(fig)

elif selected_option == "Xã hội và sức khỏe":
    st.markdown('''<div class="page-title">Xã hội & Sức khoẻ</div>''', unsafe_allow_html=True)

        # Improved filters layout
    col1, col2 = st.columns((1,1))
    min_year, max_year = int(df['Năm'].min()), int(df['Năm'].max())

    with col1:
        selected_countries = st.multiselect("Chọn các quốc gia để so sánh", options=df['Quốc gia'].unique(), default=df['Quốc gia'].unique()[:], key="Quốc gia_selection")
    with col2:
        selected_year = st.selectbox("Chọn năm cụ thể", options=range(min_year, max_year + 1), index=max_year - min_year, key="Năm_selection")

    # Main tab
    col1, col2, col3 = st.columns([1, 2, 2])
    with col1:
        st.markdown('''<div class="custom2", style="height: 525px;">
                        <h6><center>TUỔI THỌ</center></h6>
                        <p>Tuổi thọ qua các năm có xu hướng dao động xung quanh mốc ban đầu năm 2000. 
                           Và đang có xu hướng giảm dần ở năm 2023.</p>
                        <p>Các nước có tỉ lệ bác sĩ trên bệnh nhân và chi tiêu y tế bình quân đầu người cao 
                            thường có tuổi thọ cao hơn các nước còn lại. </p></div>
                    ''', unsafe_allow_html=True)  # Start of the
    with col2:
        title = f'TUỔI THỌ CỦA CÁC QUỐC GIA TỪ NĂM {min_year} ĐẾN {max_year}'
        st.markdown(f'''<div class="custom2", style="height: 75px;">
                    <center><strong>{title}</strong></center>
                    </div>
                    ''', unsafe_allow_html=True) 
        if selected_countries:
            hdi_data = df[
                (df['Quốc gia'].isin(selected_countries)) & (df['Năm'])
            ][['Quốc gia', 'Năm', 'Tuổi thọ (năm)']].dropna()
            # Create a line chart for HDI using Plotly
            fig = px.line(hdi_data, x='Năm', y='Tuổi thọ (năm)', color='Quốc gia', 
                        title="Tuổi thọ (năm) Over Năms by Quốc gia",
                        labels={'Tuổi thọ (năm)': 'Tuổi thọ (Năm)', 'Năm': 'Năm'},
                        color_discrete_sequence=color_palette,
                        markers=True)

                    # Get the base layout and update it with additional settings
            layout = get_chart_layout()
            layout.update(
                margin=dict(l=60, r=30, t=30, b=50),
                hovermode='x unified',
            )

            # Update layout with merged settings
            fig.update_layout(**layout)

            # Improve marker and line styling
            fig.update_traces(
                marker=dict(
                    size=6,  # Slightly smaller markers
                    line=dict(width=1, color='DarkSlateGrey')
                ),
                line=dict(width=1),  # Slightly thinner lines
                
            )
            fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
            st.plotly_chart(fig)
    with col3: 
        title = f'TỈ LỆ BÁC SĨ-BỆNH NHÂN VÀ TUỔI THỌ THEO CHI TIÊU CHĂM SÓC SỨC KHOẺ BÌNH QUÂN ĐẦU NGƯỜI NĂM {selected_year}'
        st.markdown(f'''<div class="custom2", style="height: 75px;">
                    <center><strong>{title}</strong></center>
                     </div>
                    ''', unsafe_allow_html=True)
        
        if selected_countries:
            #Create a bubble chart using Plotly
            fig = px.scatter(df[df["Quốc gia"].isin(selected_countries) & (df['Năm'] == selected_year)], 
                    x='Tỷ lệ bác sĩ-bệnh nhân', 
                    y='Tuổi thọ (năm)', 
                    size='Chi tiêu y tế bình quân đầu người (USD)',  # Bubble size
                    color='Quốc gia',  # Bubble color
                    title='Life Expectancy vs Tỷ lệ bác sĩ-bệnh nhân (Bubble Chart)',
                    labels={'Tỷ lệ bác sĩ-bệnh nhân': 'Tỉ lệ bác sĩ-bệnh nhân',
                            'Tuổi thọ (năm)': 'Tuổi thọ (năm)'},
                    size_max=40,
                    hover_name="Quốc gia",
                    hover_data=["Năm"],
                    animation_group="Quốc gia",
                    color_discrete_sequence=color_palette
            )
            layout = get_chart_layout()
            layout.update(
                annotations=[
                dict(
                    xref='paper', yref='paper',
                    x=0.5, y=1.15,  # Position at the top center of the chart
                    showarrow=False,
                    text="Kích thước bong bóng biểu thị chi tiêu y tế bình quân đầu người của các quốc gia",
                    font=dict(size=16, color="DarkSlateGrey")
                )
            ]
            )
            fig.update_layout(**layout)
            fig.update_traces(
                marker=dict(# Slightly smaller markers
                    line=dict(width=1, color='DarkSlateGrey')
                ),
                line=dict(width=1), 
            )
            fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
            # Show the scatter plot
            st.plotly_chart(fig)
    
    col4, col5, col6 = st.columns([1, 2, 2])
    with col4:
        st.markdown('''<div class="custom3", style="height: 525px;">
                        <h6><center>TỈ LỆ HỘ NGHÈO</center></h6>
                        <p>Tỉ lệ hộ nghèo, tỉ lệ thất nghiệp cho mức độ sống của người dân, và những thách thức mà nhà nước đang phải đối mặt.</p>
                        <p>Các nước có GDP bình quân đầu người cao chưa chắc đã có tỉ lệ hộ nghèo thấp như: USA, Canada, Australia. 
                        Cho thấy sự chênh lệch giai cấp trong các xã hội này là vô cùng lớn.</p></div>
                    ''', unsafe_allow_html=True)
    with col5:
        title = f'TỈ LỆ HỘ NGHÈO VÀ DÂN SỐ CỦA CÁC QUỐC GIA NĂM {selected_year}'
        st.markdown(f'''<div class="custom3", style="height: 75px;">
                    <center><strong>{title}</strong></center>
                    </div>
                    ''', unsafe_allow_html=True)
        if selected_countries:
            poverty_data = df[
                (df['Quốc gia'].isin(selected_countries)) & 
                (df['Năm'] == selected_year) 
                ][['Quốc gia', 'Tỷ lệ nghèo (%)', 'Tỷ lệ thất nghiệp (%)']].dropna()
            poverty_data = poverty_data.sort_values(by='Tỷ lệ nghèo (%)', ascending=True)

            poverty_data = poverty_data.rename(columns={
            'Tỷ lệ nghèo (%)': 'Hộ nghèo', 
            'Tỷ lệ thất nghiệp (%)': 'Thất nghiệp'
            })

            melted_data = pd.melt(poverty_data, 
                      id_vars=['Quốc gia'], 
                      value_vars=['Thất nghiệp', 'Hộ nghèo'],
                      var_name='Metric', 
                      value_name='Value (%)')

            # Create the grouped bar chart
            fig = px.bar(melted_data, 
                        x='Quốc gia', 
                        y='Value (%)', 
                        color='Metric',  # Color by 'Metric'
                        barmode='group',  # Grouped bars
                        labels={
                            'Metric': 'Chỉ số',
                            'Value (%)': 'Tỉ lệ (%)',
                            'Quốc gia': 'Quốc gia',
                        },
                        color_discrete_map={
                            'Thất nghiệp': color_palette[1],
                            'Hộ nghèo': color_palette[0],  
                        },
                        hover_name = 'Metric',
                        )
            chart_layout = get_chart_layout()
            chart_layout['legend']['title']['text'] = 'Chỉ số'  
            fig.update_layout(**chart_layout)

            # Show the chart
            st.plotly_chart(fig)
    with col6:
        title = f'TỈ LỆ HỘ NGHÈO VÀ GDP BÌNH QUÂN ĐẦU NGƯỜI CỦA CÁC QUỐC GIA NĂM {selected_year}'
        st.markdown(f'''<div class="custom3", style="height: 75px;">
                    <center><strong>{title}</strong></center>
                     </div>
                    ''', unsafe_allow_html=True) 
        
    # Scatter plot for Poverty-Rate vs GDP per Capita
        if selected_countries:
            health_data = df[
                (df['Quốc gia'].isin(selected_countries)) & 
                (df['Tỷ lệ nghèo (%)'].notna()) & 
                (df['GDP bình quân đầu người (USD)'].notna()) &
                (df['Năm'] == selected_year)
            ][['Quốc gia', 'Tỷ lệ nghèo (%)', 'GDP bình quân đầu người (USD)']]
            # Create a scatter plot using Plotly
            fig = px.scatter(health_data, x='Tỷ lệ nghèo (%)', y='GDP bình quân đầu người (USD)', 
                        color='Quốc gia', 
                        title=' Tỷ lệ nghèo (%) vs GDP bình quân đầu người (USD)',
                        labels={'Tỷ lệ nghèo (%)': 'Tỉ lệ hộ nghèo (%)',
                                'GDP bình quân đầu người (USD)': 'GDP bình quân (in USD)'},
                        color_discrete_sequence=color_palette,
                        size_max = 40)
            
            # Vietnamese translation for the legend title
            fig.update_layout(**get_chart_layout())

            fig.update_traces(
                marker=dict(# Slightly smaller markers
                    size=10,
                    line=dict(width=1, color='DarkSlateGrey')
                ),
                line=dict(width=1), 
            )
            fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
            # Show the scatter plot
            st.plotly_chart(fig) 

elif selected_option == "Năng lượng, môi trường và cơ sở hạ tầng":
    st.markdown('''<div class="page-title">Năng lượng, Môi trường & Cơ sở hạ tầng</div>''', unsafe_allow_html=True)

    # Custom CSS to style column
    st.markdown("""       
        <style>
        .summary1{
            background-color: #528B8B;
            padding: 20px;
        }
        .summary2 {
            background-color: #4682B4;
            padding: 20px;
        }       
        .summary3{
            background-color: #cd5c5c;
            padding: 20px;
        }
        .custom1, .custom2, .custom3 {
            padding: 20px;
            height: 75px; /* Set the fixed height here */
            overflow: hidden; /* Ensures text doesn't overflow */
            text-align: center; /* Center-align the text */
            display: flex;
            justify-content: center;
            align-items: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar for Quốc gia selection
    col1, col2 = st.columns((1,1))
    min_year, max_year = int(df['Năm'].min()), int(df['Năm'].max())

    with col1:
        selected_countries = st.multiselect("Chọn các quốc gia để so sánh", options=df['Quốc gia'].unique(), default=df['Quốc gia'].unique()[:], key="Quốc gia_selection")
    with col2:
        selected_year = st.selectbox("Chọn năm cụ thể", options=range(min_year, max_year + 1), index=max_year - min_year, key="Năm_selection")

    selected_year_range = st.slider("Chọn khoảng năm", min_value=min_year, max_value=max_year, value=(min_year, max_year), key="Năm_range")
    selected_years = selected_year_range
    selected_year = selected_year
    # Main tab
    col1, col2, col3 = st.columns([1, 2, 2])
    with col1:
        st.markdown('''<div class="summary1", style="height: 525px;">
                        <h6><center>NĂNG LƯỢNG</center></h6>
                        <p>Mặc dù tổng lượng tiêu thụ năng lượng của các quốc gia tương đối ổn định qua các năm, nhưng sự phụ thuộc vào năng lượng không tái tạo vẫn chiếm ưu thế, đặc biệt là ở các nước lớn như Mỹ, Nga và Ấn Độ. Việc thúc đẩy chuyển đổi sang năng lượng tái tạo vẫn còn là một thách thức lớn</p></div>
                    ''', unsafe_allow_html=True)
    with col2:
        title =f'LƯỢNG TIÊU THỤ NĂNG LƯỢNG CỦA CÁC QUỐC GIA TỪ NĂM {selected_years[0]} ĐẾN {selected_years[1]}'
        st.markdown(f'''<div class="custom1">
                    <center><strong>{title}</strong></center>
                    </div>
                    ''', unsafe_allow_html=True)

        if selected_countries:
            energy_data = df[(df['Quốc gia'].isin(selected_countries)) & (df['Năm'] >= selected_years[0]) & (df['Năm'] <= selected_years[1])]
            fig = px.area(energy_data, 
                x='Năm', y='Tiêu thụ năng lượng (TWh)', 
                color='Quốc gia',
                color_discrete_sequence=color_palette,
                markers=True
            )

            fig.update_layout(
                xaxis_title="Năm",
                yaxis_title="Lượng tiêu thụ năng lượng (TWh)",
                **get_chart_layout(),
            )

            fig.update_traces(
                marker=dict(
                    size=6,
                    line=dict(
                        color='black',
                        width=1
                    )
                )
            )
            fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
            st.plotly_chart(fig)
    with col3:
        title=f'TỈ LỆ NĂNG LƯỢNG TÁI TẠO CỦA CÁC QUỐC GIA NĂM {selected_year}'
        st.markdown(f'''<div class="custom1">
                    <center><strong>{title}</strong></center>
                    </div>
                    ''', unsafe_allow_html=True)

        if selected_countries:
            filtered_df = df[(df["Quốc gia"].isin(selected_countries)) & (df['Năm'] == selected_year)]
            filtered_df = filtered_df[['Quốc gia', 'Năm', 'Tiêu thụ năng lượng (TWh)','Tỷ lệ năng lượng tái tạo (%)']]
            filtered_df['Tỉ lệ năng lượng không tái tạo (%)'] = 100 - df['Tỷ lệ năng lượng tái tạo (%)']

            stacked_df = pd.melt(filtered_df, 
                     id_vars=['Quốc gia', 'Năm'], 
                     value_vars=['Tỷ lệ năng lượng tái tạo (%)', 'Tỉ lệ năng lượng không tái tạo (%)'], 
                     var_name='Loại năng lượng', 
                     value_name='Phần trăm')

            # Create a stacked bar chart
            fig_renewable = px.bar(
                stacked_df, 
                x='Quốc gia', 
                y='Phần trăm', 
                color='Loại năng lượng',  # Stack by 'Energy Type' to show renewable and non-renewable
                color_discrete_map={
                    'Tỷ lệ năng lượng tái tạo (%)': '#7daed7',  # LimeGreen for renewable
                    'Non-Renewable Energy Share (%)': '#478dff'  # OrangeRed for non-renewable
                }
            )

            chart_layout = get_chart_layout()
            chart_layout['legend']['title']['text'] = 'Loại năng lượng'  

            fig_renewable.update_layout(
                yaxis_title="Tỉ lệ (%)",
                xaxis_title="Quốc gia",
                **chart_layout,
            )

            st.plotly_chart(fig_renewable)

    # Main tab
    col4, col5, col6 = st.columns([1, 2, 2])
    with col4:
        st.markdown('''<div class="summary2", style="height: 525px;">
                        <h6><center>MÔI TRƯỜNG</center></h6>
                        <p>Độ che phủ rừng của các nước có xu hướng giữ nguyên qua các năm, nhưng tại các quốc gia có dân số lớn và tiêu thụ năng lượng cao như Trung Quốc và Ấn Độ, lượng phát thải CO2 vẫn ở mức rất cao, cho thấy mối tương quan rõ rệt giữa tăng trưởng năng lượng và tác động đến môi trường. Đặc biệt là Trung Quốc, nước đang phát triển lớn nhất thế giới, với tỉ lệ bao che phủ rừng thấp nhưng lượng phát thải khí CO2 rất lớn </p></div>
                    ''', unsafe_allow_html=True)
    with col5:
        title = f'ĐỘ CHE PHỦ RỪNG CỦA CÁC QUỐC GIA TỪ NĂM {selected_years[0]} ĐẾN {selected_years[1]}'
        st.markdown(f'''<div class="custom2">
                    <center><strong>{title}</strong></center>
                    </div>
                    ''', unsafe_allow_html=True)

        if selected_countries:
            df_forest = df[df["Quốc gia"].isin(selected_countries) & (df["Năm"] >= selected_year_range[0]) & (df["Năm"] <= selected_year_range[1])]

            fig_forest = px.line(
                df_forest,
                x="Năm", 
                y="Diện tích rừng che phủ (%)",
                color="Quốc gia",
                color_discrete_sequence=color_palette,
                markers=True
            )

            fig_forest.update_layout(
                xaxis_title="Năm",
                yaxis_title="Độ che phủ rừng (%)",
                **get_chart_layout(),
            )
            fig_forest.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
            st.plotly_chart(fig_forest)
    with col6:
        title = f'BIỂU ĐỒ THỂ HIỆN LƯỢNG PHÁT THẢI CO2 VÀ LƯỢNG TIÊU THỤ NĂNG LƯỢNG THEO DÂN SỐ NĂM {selected_year}'
        st.markdown(f'''<div class="custom2">
                    <center><strong>{title}</strong></center>
                    </div>
                    ''', unsafe_allow_html=True)

        if selected_countries:
            fig_co2_ptr = px.scatter(
                df[(df["Quốc gia"].isin(selected_countries)) & (df["Năm"] == selected_year)],
                x="Tiêu thụ năng lượng (TWh)", y="Lượng phát thải CO2 (triệu tấn)",
                size="Dân số (triệu người)", color="Quốc gia", hover_name="Quốc gia", color_discrete_sequence=color_palette,
                size_max=20  # Control the max size of the bubbles
        )

        fig_co2_ptr.update_layout(
            xaxis_title="Lượng tiêu thụ năng lượng (TWh)",
            yaxis_title="Lượng phát thải CO2 (triệu tấn)",
            **get_chart_layout(),
        )
        layout = get_chart_layout()
        layout.update(
            annotations=[
                dict(
                    xref='paper', yref='paper',
                    x=0.5, y=1.15,  # Position at the top center of the chart
                    showarrow=False,
                    text="Kích thước bong bóng biểu thị quy mô dân số của các quốc gia",
                    font=dict(size=16, color="DarkSlateGrey")
                )
            ]
        )

        fig_co2_ptr.update_layout(
            xaxis_title="Lượng tiêu thụ năng lượng (TWh)",
            yaxis_title="Lượng phát thải CO2 (triệu tấn)",
            **layout,  # Remove the parentheses here
        )
        fig_co2_ptr.update_traces(
            marker=dict(
                line=dict(width=1, color='DarkSlateGrey')
            )
        )
        fig_co2_ptr.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
        st.plotly_chart(fig_co2_ptr)

    #Main tab
    col7, col8 = st.columns([1, 4])
    with col7:
        st.markdown('''<div class="summary3", style="height: 525px;">
                        <h6><center>CƠ SỞ HẠ TẦNG</center></h6>
                        <p>Việc đầu tư vào cơ sở hạ tầng được chú trọng đặc biệt là ở các nước lớn nhưng tỉ lệ sử dụng phương tiện công cộng lại ở mức thấp dẫn đến sự phát thải CO2 cao. Việc đầu tư vào cơ sở hạ tầng qua việc xây dựng các sân bay thu hút lượng lớn du khách nước ngoài mang lại doanh thu khá lớn cho hoạt động du lịch<p></div>
                    ''', unsafe_allow_html=True)
    with col8:
        title = f'CHIỀU DÀI MẠNG LƯỚI ĐƯỜNG BỘ VÀ TỈ LỆ SỬ DỤNG PHƯƠNG TIỆN CÔNG CỘNG THEO LƯỢNG PHÁT THẢI CO2 NĂM {selected_year}'
        st.markdown(f'''<div class="custom3">
                    <center><strong>{title}</strong></center>
                    </div>
                    ''', unsafe_allow_html=True)
        if selected_countries:
            df_filtered = df[(df["Quốc gia"].isin(selected_countries)) & (df['Năm'] == selected_year)]
            
            # Plot the merged infrastructure chart
            fig_infra = px.scatter(df_filtered, 
                                    x="Chiều dài mạng lưới đường bộ (km)",  # Road network length
                                    y="Sử dụng phương tiện công cộng (%)",  # Number of airports
                                    size="Lượng phát thải CO2 (triệu tấn)",  # CO2 emissions
                                    color="Quốc gia",  # Countries
                                    hover_name="Quốc gia",  # Hover data
                                    title="Mạng lưới đường bộ và Số lượng sân bay với lượng phát thải CO2",
                                    color_discrete_sequence=color_palette
                                )

            layout = get_chart_layout()
            layout.update(
                annotations=[
                    dict(
                        xref='paper', yref='paper',
                        x=0.5, y=1.15,  # Position at the top center of the chart
                        showarrow=False,
                        text="Kích thước bong bóng biểu thị lượng phát thải CO2 của các quốc gia",
                        font=dict(size=16, color="DarkSlateGrey")
                    )
                ]
            )

            fig_co2_ptr.update_layout(
                xaxis_title="Lượng tiêu thụ năng lượng (TWh)",
                yaxis_title="Lượng phát thải CO2 (triệu tấn)",
                **layout,  # Remove the parentheses here
            )
            # Customize chart layout
            fig_infra.update_layout(
                xaxis_title="Chiều dài mạng lưới đường bộ",  
                yaxis_title="Tỉ lệ sử dụng phương tiện công cộng (%)",
                **layout,
            )

            fig_infra.update_traces(
                marker=dict(
                    line=dict(width=1, color='DarkSlateGrey')
                )
            )
            fig_infra.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
            st.plotly_chart(fig_infra)        

elif selected_option == "Quản trị":
    st.markdown('''<div class="page-title">Quản trị</div>''', unsafe_allow_html=True)
    
    # Custom CSS to style columns
    st.markdown("""
        <style>
        .custom-box {
            padding: 20px;
        }
        .custom1 { background-color: #4B0082; }
        .custom2 { background-color: #8B4513; }
        .custom3 { background-color: #2F4F4F; }
        .custom4 { background-color: #483D8B; }
        .chart-title {
            color: white;
            text-align: center;
            font-weight: bold;
            margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
    # Improved filters layout
    col1, col2 = st.columns((1,1))
    min_year, max_year = int(df['Năm'].min()), int(df['Năm'].max())

    with col1:
        selected_countries = st.multiselect("Chọn các quốc gia để so sánh", options=df['Quốc gia'].unique(), default=df['Quốc gia'].unique()[:], key="Quốc gia_selection")
    with col2:
        selected_year = st.selectbox("Chọn năm cụ thể", options=range(min_year, max_year + 1), index=max_year - min_year, key="Năm_selection")

    selected_year_range = st.slider("Chọn khoảng năm", min_value=min_year, max_value=max_year, value=(min_year, max_year), key="Năm_range")

    # Filter data based on selected Năm range
    filtered_data = df[(df['Năm'] >= selected_year_range[0]) & (df['Năm'] <= selected_year_range[1])]

    # Function to create line chart
    def create_line_chart(data, x_col, y_col, title, y_label):
        fig = px.line(data, x=x_col, y=y_col, color='Quốc gia', 
                      title=title,
                      labels={y_col: y_label, x_col: 'Năm'},
                      markers=True, 
                        color_discrete_sequence=color_palette)
        fig.update_layout(**get_chart_layout())

        fig.update_yaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128, 128, 128, 0.15)',
            showline=True,
            linewidth=1,
            linecolor='rgba(128, 128, 128, 0.4)'
        )

        # Improve the x-axis
        fig.update_xaxes(
            gridcolor='rgba(128, 128, 128, 0.15)',
            gridwidth=1,
            showline=True,
            linewidth=1,
            linecolor='rgba(128, 128, 128, 0.4)'
        )

        return fig

    # Function to create bar chart
    def create_bar_chart(data, x_col, y_col, title, y_label):
        fig = px.bar(data, x=x_col, y=y_col, color='Quốc gia', 
                     title=title,
                     labels={y_col: y_label, x_col: 'Năm'},
                     color_discrete_sequence=color_palette,
                     barmode='group')
        fig.update_yaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128, 128, 128, 0.15)',
            showline=True,
            linewidth=1,
            linecolor='rgba(128, 128, 128, 0.4)'
        )

        # Improve the x-axis
        fig.update_xaxes(
            gridcolor='rgba(128, 128, 128, 0.15)',
            gridwidth=1,
            showline=True,
            linewidth=1,
            linecolor='rgba(128, 128, 128, 0.4)'
        )

        fig.update_layout(**get_chart_layout())
        fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
        return fig

    # Function to create scatter plot
    def create_scatter_plot(data, x_col, y_col, title, y_label):
        fig = px.scatter(data, x=x_col, y=y_col, color='Quốc gia', 
                         title=title,
                         color_discrete_sequence=color_palette,
                         labels={y_col: y_label, x_col: 'Năm'},
                         size_max=15)
        fig.update_layout(**get_chart_layout())
        return fig

    # Function to create box plot
    def create_box_plot(data, x_col, y_col, title, y_label):
        fig = px.box(data, x=x_col, y=y_col, color='Quốc gia', 
                     title=title,
                     color_discrete_sequence=color_palette,
                     hover_name='Quốc gia',
                     labels={y_col: y_label, x_col: 'Quốc gia'})

        fig.update_yaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128, 128, 128, 0.15)',
            showline=True,
            linewidth=1,
            linecolor='rgba(128, 128, 128, 0.4)'
        )

        # Improve the x-axis
        fig.update_xaxes(
            gridcolor='rgba(128, 128, 128, 0.15)',
            gridwidth=1,
            showline=True,
            linewidth=1,
            linecolor='rgba(128, 128, 128, 0.4)'
        )
        fig.update_layout(**get_chart_layout())
        fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
        return fig

    # Function to create bubble chart
    def create_bubble_chart(data, x_col, y_col, title, x_label, y_label):
        fig = px.scatter(data, x=x_col, y=y_col, size='Dân số (triệu người)', color='Quốc gia',
                         hover_name='Quốc gia', title=title,
                         labels={x_col: x_label, y_col: y_label},
                         color_discrete_sequence=color_palette,
                         size_max=40)

        
        fig.update_yaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128, 128, 128, 0.15)',
            showline=True,
            linewidth=1,
            linecolor='rgba(128, 128, 128, 0.4)'
        )

        # Improve the x-axis
        fig.update_xaxes(
            gridcolor='rgba(128, 128, 128, 0.15)',
            gridwidth=1,
            showline=True,
            linewidth=1,
            linecolor='rgba(128, 128, 128, 0.4)'
        )
        layout = get_chart_layout()
        layout.update(
                        annotations=[
                        dict(
                            xref='paper', yref='paper',
                            x=0.5, y=1.15,  # Position at the top center of the chart
                            showarrow=False,
                            text="Kích thước bong bóng biểu thị quy mô dân số của các quốc gia",
                            font=dict(size=16, color="DarkSlateGrey")
                        )
                    ]
        )
        fig.update_layout(**layout)
        fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
        return fig

    # Function to create section
    def create_section(title, description, chart_title, data, y_col, y_label, custom_class, chart_type):
        col1, col2, col3 = st.columns([1, 2, 2])
        with col1:
            st.markdown(f'''
                <div class="custom-box {custom_class}", style="height: 525px;">
                    <h6><center><strong>{title}</center></strong></h6>
                    <p>{description}</p>
                </div>
            ''', unsafe_allow_html=True)
        with col2:
            chart_title = f'{chart_title.upper()} TỪ NĂM {selected_year_range[0]} ĐẾN {selected_year_range[1]}'
            st.markdown(f'<div class="custom-box {custom_class}", style="height: 75px;"><center><strong>{chart_title}</center></strong></div>', unsafe_allow_html=True)
            if selected_countries:
                chart_data = data[
                    (data['Quốc gia'].isin(selected_countries)) & 
                    (data['Năm'].notna())
                ][['Quốc gia', 'Năm', y_col]].dropna()
                if chart_type == 'line':
                    fig = create_line_chart(chart_data, 'Năm', y_col, title, y_label)
                elif chart_type == 'bar':
                    fig = create_bar_chart(chart_data, 'Năm', y_col, title, y_label)
                elif chart_type == 'scatter':
                    fig = create_scatter_plot(chart_data, 'Năm', y_col, title, y_label)
                elif chart_type == 'box':
                    fig = create_box_plot(chart_data, 'Quốc gia', y_col, title, y_label)
                st.plotly_chart(fig)
        with col3:
            if selected_countries:
                bubble_data = data[
                    (data['Quốc gia'].isin(selected_countries)) & 
                    (data['Năm'].notna()) & 
                    (data[y_col].notna()) & 
                    (data['Dân số (triệu người)'].notna()) &
                    (data['GDP (nghìn tỷ USD)'].notna())
                ][['Quốc gia', 'Năm', y_col, 'Dân số (triệu người)', 'GDP (nghìn tỷ USD)', 'Chỉ số tự do báo chí', 'Chỉ số cảm nhận tham nhũng']].dropna()
                latest_data = bubble_data[bubble_data['Năm'] == selected_year]
                # Lấy năm gần đây nhất có dữ liệu
                if title == "TỈ LỆ TỘI PHẠM":
                    
                    chart_title = f'{y_label.upper()} VÀ GDP THEO QUY MÔ DÂN SỐ NĂM {selected_year}'
                    st.markdown(f'<div class="custom-box {custom_class}", style="height: 75px;"><center><strong> {chart_title} </center></strong></div>', unsafe_allow_html=True)
                    
                    fig_bubble = create_bubble_chart(latest_data, y_col, 'GDP (nghìn tỷ USD)', 
                                                    f"So sánh {y_label} và GDP (Năm {selected_year})", 
                                                    y_label, "GDP (Nghìn tỷ USD)")
                    st.plotly_chart(fig_bubble)
                else:
                    chart_title = f'{y_label.upper()} VÀ CHỈ SỐ TỰ DO BÁO CHÍ THEO QUY MÔ DÂN SỐ NĂM {selected_year}'
                    st.markdown(f'<div class="custom-box {custom_class}", style="height: 75px;"><center><strong> {chart_title}</center></strong></div>', unsafe_allow_html=True)
                    fig = px.scatter(latest_data, x='Chỉ số tự do báo chí', y=y_col, size='Dân số (triệu người)', color='Quốc gia',
                         hover_name='Quốc gia', title=title,
                         color_discrete_sequence=color_palette,
                         size_max=40)

                    
                    fig.update_yaxes(
                        showgrid=True,
                        gridwidth=1,
                        gridcolor='rgba(128, 128, 128, 0.15)',
                        showline=True,
                        linewidth=1,
                        dtick=10,
                        linecolor='rgba(128, 128, 128, 0.4)'
                    )

                    # Improve the x-axis
                    fig.update_xaxes(
                        gridcolor='rgba(128, 128, 128, 0.15)',
                        gridwidth=1,
                        showline=True,
                        linewidth=1,
                        dtick=20,
                        linecolor='rgba(128, 128, 128, 0.4)'
                    )
                    layout = get_chart_layout()
                    layout.update(
                        annotations=[
                        dict(
                            xref='paper', yref='paper',
                            x=0.5, y=1.15,  # Position at the top center of the chart
                            showarrow=False,
                            text="Kích thước bong bóng biểu thị quy mô dân số của các quốc gia",
                            font=dict(size=16, color="DarkSlateGrey")
                        )
                    ]
                    )
                    fig.update_layout(**layout)
                    fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
                    st.plotly_chart(fig)

    # Crime Rate Section
    create_section(
        "TỈ LỆ TỘI PHẠM",
        "Tỉ lệ tội phạm qua các năm có xu hướng biến động khác nhau ở mỗi quốc gia. Một số nước có xu hướng giảm, trong khi các nước khác lại tăng. Tỉ lệ tội phạm có thể bị ảnh hưởng bởi nhiều yếu tố như kinh tế, xã hội, và hiệu quả của hệ thống pháp luật.",
        "TỈ LỆ TỘI PHẠM QUA CÁC NĂM",
        filtered_data,
        'Tỷ lệ tội phạm (trên 100,000 người)',
        'Tỉ lệ tội phạm (trên 100,000 dân)',
        "custom1",
        "line"
    )
    # Voting Participation Rate Section
    create_section(
        "TỈ LỆ THAM GIA BẦU CỬ",
        "Tỉ lệ tham gia bầu cử phản ánh mức độ tham gia của công dân trong quá trình dân chủ của một quốc gia. Tỉ lệ cao hơn thường được coi là dấu hiệu của sự tham gia tích cực của công dân trong quá trình chính trị.",
        "TỈ LỆ THAM GIA BẦU CỬ THEO QUỐC GIA",
        filtered_data,
        'Tỷ lệ tham gia bầu cử (%)',
        'Tỉ lệ tham gia bầu cử (%)',
        "custom2",
        "box"
    )