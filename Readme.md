# AI Webpage Summariser
Author: Jesse-Paul Miracle Osemeke

### About
This project is a Streamlit application that takes in the url of any webpage, scrapes the content, and summarises it. It uses the Google Gemini API to perform the summarisation, and the BeautifulSoup library to scrape the webpage. The application is deployed on Streamlit Community Cloud.

### Tools Used
- Python
- Streamlit
- BeautifulSoup
- Google Gemini API
- Langchain
- Selenium

### Testing / Running
To run this project locally, you will need to have Python installed on your machine. You can then clone this repository and install the required dependencies using the following command:
```shell
pipenv install
```
Once the dependencies are installed, you can run the application using the following command:
```shell
streamlit run main.py
```
__PS__: Don't forget to add your Google Gemini API key in a `.env` file, using the format specified in `.env.example`

### Deployment
This application is deployed on Streamlit Community Cloud. You can access it [here](https://web-content-summariser.streamlit.app/).

### Future Work
- Add more features to the application, such as the ability to summarise multiple webpages at once, and the ability to save summaries for later reference.
- Improve the user interface and user experience of the application.
- Explore other summarisation techniques and models to improve the accuracy and efficiency of the summarisation process.
- Add support for other languages beyond English.

### Contributing
Contributions to this project are welcome. If you would like to contribute, please fork the repository and submit a pull request with your changes. Please ensure that your code is well-documented and follows the existing code style.