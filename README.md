# WebScrap for UFCAT Data Collection

This project is a web scraping script developed to collect news, events, and notices data from the [Universidade Federal de Catalão (UFCAT)](https://ufcat.edu.br/) website. The collected data is stored in Firebase Realtime Database.

---

## 📋 Features

- Automated data collection from the following pages:
  - [News](https://ufcat.edu.br/noticias)
  - [Events](https://ufcat.edu.br/eventos)
  - [Notices](https://ufcat.edu.br/editais)
- Extraction of information such as title, link, image, alt text, and date.
- Automated navigation through listing pages using Selenium.
- Storage of collected data in Firebase Realtime Database.
- Retrieval of stored data from Firebase for validation.

---

## 🛠 Technologies Used

- **Python** (version 3.8 or higher)
- Libraries:
  - [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) for HTML parsing and data extraction.
  - [Selenium](https://pypi.org/project/selenium/) for automated browser navigation.
  - [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup) for Firebase integration.

---

## 📂 Project Structure

```plaintext
├── .github/
│   └── workflows/
│       └── main.yml        # GitHub Actions workflow for deployment automation
├── webscrap.py             # Main script
└── README.md               # Project documentation
```

---

## 🚀 How to Run

### 1. Prerequisites

Ensure the following are set up in your environment:

- Python 3.8 or higher.
- Google Chrome installed.
- [Chromedriver](https://chromedriver.chromium.org/downloads) compatible with your Google Chrome version.
- Firebase credentials JSON file (stored securely, e.g., as a GitHub secret for Actions).

Install the required Python dependencies:

```bash
pip install requests beautifulsoup4 selenium firebase-admin
```

### 2. Firebase Configuration

In the Firebase Console, set up a Realtime Database with a URL in the format:

```bash
https://<project-name>.firebaseio.com/
```

Ensure the Firebase credentials JSON is securely configured (e.g., as a GitHub secret for use in GitHub Actions).

### 3. Running Locally

To run the script locally, execute the main script:

```bash
python webscrap.py
```

The script will:
- Collect data from the specified URLs in the script's `self.urls` dictionary.
- Store the collected data in Firebase Realtime Database.
- Close the WebDriver after completing the scraping process.

### 4. Deployment with GitHub Actions

This project uses GitHub Actions for automated deployment. The workflow is defined in `.github/workflows/main.yml`. The script is executed automatically based on the configured triggers (e.g., push to the main branch or scheduled runs). The Firebase credentials are securely accessed via GitHub secrets.

To set up GitHub Actions:
- Store the Firebase credentials JSON as a GitHub secret (e.g., `FIREBASE_CREDENTIALS`).
- Configure the `main.yml` workflow file to install dependencies, set up Chromedriver, and run `webscrap.py`.

---

## 🗂 Data Structure

The data stored in Firebase follows this JSON format:

```json
{
  "type": "news",
  "link": "https://ufcat.edu.br/noticia/exemplo",
  "title": "News Title",
  "date": "DD/MM/YYYY",
  "image_url": "https://ufcat.edu.br/image.jpg",
  "alt_text": "Image description"
}
```

---

## ⚠️ Notes

- This script is tailored for the UFCAT website. Changes to the website's structure may require code adjustments.
- Selenium requires a compatible Chromedriver version for your browser.
- Ensure Firebase credentials are securely managed and not exposed in the repository.

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit suggestions, bug reports, or pull requests to improve the project.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

For questions or assistance, reach out to:

**Developer**: Marcos Paulo Rodrigues  
**Email**: dev.silva.marcos@gmail.com
