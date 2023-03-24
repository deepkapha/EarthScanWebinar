import os
import io

import cv2
import matplotlib.pyplot as plt
import numpy as np
import requests
import streamlit as st
from PIL import Image

st.set_option('deprecation.showPyplotGlobalUse', False)


# Define the JUA class and the plot_histograms function (omitted for brevity)
class JUA():
    def __init__(self, image1, url='https://1ei5j2kto9.execute-api.us-east-1.amazonaws.com/prod/predict',
                 headers={'accept': 'application/json'}):
        self.url = url
        self.image1 = image1
        self.headers = headers

    def predict(self):
        with open(self.image1, 'rb') as image:
            response = requests.post(self.url, headers=self.headers,
                                     files={'file': (self.image1, image, 'image/png')})

        if response.status_code == 200:
            try:
                result = response.json()['prediction']
                return result
            except JSONDecodeError as e:
                print("Error decoding JSON:", e)
                print("Response content:", response.content)
        else:
            print('Failed to call the API, status code:', response.status_code)
            print('Response content:', response.content)


# Define a function to plot histograms of the anomaly values
def plot_histograms(anomalies, img):
    # Sort the anomaly types by frequency in descending order
    anomalies_sorted = dict(sorted(anomalies.items(), key=lambda item: item[1], reverse=True))

    # Plot the histogram
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 8), facecolor='#f5f5f5')
    fig.subplots_adjust(wspace=0.3, hspace=0.1)
    fig.patch.set_facecolor('#FFDDE1')

    # Load the image and display it in the left subplot
    img = cv2.imread(img)
    ax1.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    ax1.set_title('Image', fontsize=16, fontweight='bold')
    ax1.set_xticks([])
    ax1.set_yticks([])

    # Create a bar chart in the right subplot
    x_pos = np.arange(len(anomalies_sorted))
    ax2.bar(x_pos, anomalies_sorted.values(), color=['#FA8072', '#87CEFA', '#90EE90', '#FFDAB9', '#C6E2FF'])
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(anomalies_sorted.keys(), fontsize=14, fontweight='bold', rotation=45, ha='right')
    ax2.set_xlabel('Anomaly Types', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Percentage', fontsize=14, fontweight='bold')
    ax2.set_title(' Anomaly Types of PV type', fontsize=16, fontweight='bold')

    # Create a pie chart in the right subplot
    total_anomalies = sum(anomalies.values())
    anomaly_percentages = [(anomaly_freq / total_anomalies) * 100 for anomaly_freq in anomalies_sorted.values()]
    ax3.pie(anomaly_percentages, labels=anomalies_sorted.keys(), autopct='%1.1f%%', startangle=90,
            colors=['#FA8072', '#87CEFA', '#90EE90', '#FFDAB9', '#C6E2FF'])
    ax3.set_title('Anomaly Type Percentage', fontsize=16, fontweight='bold')

    plt.tight_layout(pad=3)
    plt.draw()
    plt.pause(0.001)

    # Clear the output
    from IPython.display import clear_output
    clear_output(wait=True)


import geocoder


def get_user_location():
    # Use the IP Geolocation API to get the user's location
    url = "https://api.ipgeolocation.io/ipgeo?apiKey=f294fd340228428baca4d61b7660d49a"
    response = requests.get(url).json()
    # Extract the location information from the API response
    print(response)
    city = response['city']
    state = response['state_prov']
    country = response['country_name']
    location = f"{state}, {country}"
    return location

def main():
    # Set the title and page layout
    st.set_page_config(page_title="JUA Image Anomaly Detection", page_icon=":camera_with_flash:", layout="wide")




    # Get the user's location
    location = get_user_location()
    st.markdown(
        f"<div class='icon'></div><p style='color: white; font-weight: bold;font-family: Times New Roman, sans-serif: display: inline;'>{location}</p>",
        unsafe_allow_html=True)



    import base64
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
            f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .icon {{
            background-image: url('https://cdn-icons-png.flaticon.com/512/7976/7976202.png');
            background-size: contain;
            background-repeat: no-repeat;
            width: 48px;
            height: 48px;
            display: inline-block;
            margin-right: 10px;
        }}
        </style>
        """,
            unsafe_allow_html=True
        )





    add_bg_from_local('field.png')
    # Create a sidebar for the interactive buttons
    st.sidebar.title('GS Solar')
    st.sidebar.header("Module Anomaly Detection")
    st.sidebar.text(" Upload your module's image \n or select from the preloaded images \n to view it and detect the possible \n anomalies that your module might \n be facing")

    option = st.sidebar.selectbox("Select an option:", ["Upload an image", "Choose from preloaded images"])

    # Add a file uploader and a dropdown for preloaded images
    if option == "Upload an image":
        uploaded_file = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            # Open the uploaded image file
            img = Image.open(uploaded_file)
            img = img.resize((512, 512))


            st.markdown("<p style='color: white; font-weight : 'bold'; text-align: center;'>Selected Image</p>",
                        unsafe_allow_html=True)
            st.image(img, use_column_width=False)
            st.markdown("<p style='color: white; font-weight : 'bold'; text-align: center;'>As you can see the green border in the image shows the part of the full image where the analysis is being done and the error is being detected</p>", unsafe_allow_html=True)

            # Save the uploaded image to a temporary file
            tmp_file_path = f"/tmp/{uploaded_file.name}"
            with open(tmp_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Run the anomaly detection algorithm on the uploaded image
            juaAPI = JUA(tmp_file_path)
            out = juaAPI.predict()
            plot_histograms(out, tmp_file_path)

            # Display the anomaly histogram
            st.pyplot()
            table_style = """
                                    <style>
                                        table {
                                            border: 2px solid #FFFFFF;
                                            border-collapse: collapse;
                                            background-color: #000000;
                                        }

                                    </style>
                                """

            # Display the dictionary as a table with the custom style applied

            st.write(table_style, unsafe_allow_html=True)

            st.table(out)


    else:
        # Get the list of preloaded images
        image_dir = "/Users/shuvamdas/PycharmProjects/pythonProject1/datasets2"
        image_files = sorted([os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith(".png")])

        # Display a dropdown to select a preloaded image
        selected_image_file = st.sidebar.selectbox("Select an image:", image_files)

        # Display the selected image
        img = Image.open(selected_image_file)
        img = img.resize((512, 512))
        st.image(img, use_column_width=False)
        st.markdown("<p style='color: white; font-weight : 'bold'; text-align: center;'>Selected Image</p>",
                    unsafe_allow_html=True)
        st.markdown(
            "<p style='color: white; font-weight : 'bold'; text-align: center;'>As you can see the green border in the image shows the part of the full image where the analysis is being done and the error is being detected</p>",
            unsafe_allow_html=True)

        # Run the anomaly detection algorithm on the selected image
        juaAPI = JUA(selected_image_file)
        out = juaAPI.predict()
        plot_histograms(out, selected_image_file)

        # Display the anomaly histogram
        st.pyplot()
        table_style = """
                        <style>
                            table {
                                border: 2px solid #FFFFFF;
                                border-collapse: collapse;
                                background-color: #000000;
                            }

                        </style>
                    """

        # Display the dictionary as a table with the custom style applied
        st.write(table_style, unsafe_allow_html=True)
        st.table(out)




if __name__ == "__main__":
    main()
