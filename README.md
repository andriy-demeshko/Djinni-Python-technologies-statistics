# Djinni-Python-technologies-statistics


## Install project

Python3 must be already installed

```shell
git clone https://github.com/andriy-demeshko/Djinni-Python-technologies-statistics.git
cd Djinni_Python_technologies_statistics
python -m venv venv
source venv/bin/activate # on MacOS
venv\Scripts\activate # on Windows
pip install -r requirements.txt
scrapy crawl vacancies -O technologies.csv
```
Then open file djinni_analysis/ technologies_analysis.ipynb with Jupyter Notebook and run all cells (Ctrl+Alt+Shift+Enter).

You`ll see all bar diagrams in the folder djinni_analysis/ diagrams.

## Example

![Website Interface](example.png)