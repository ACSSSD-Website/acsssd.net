import csv
from html import escape

def generate_quicklinks_html(csv_file_path, output_html_path="ACSSSD-StudentApplications.html"):
    """
    Generates a single quick-links grid from a CSV file.

    Args:
        csv_file_path (str): The path to the CSV file.
        output_html_path (str): The path to save the generated HTML file.
    """

    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # Skip the header row

            html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ACSSSD Student Applications</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <style>
        .material-symbols-outlined {
            font-variation-settings:
            'FILL' 0,
            'wght' 400,
            'GRAD' 0,
            'opsz' 20
        }

        body {
            font-family: sans-serif;
            margin: 0;
            padding: 0;
            background-color: #ffffff;
        }

        .container {
            max-width: 960px;
            margin: 20px auto;
            padding: 0 20px;
        }

        h1 {
            text-align: left;
            margin-bottom: 20px;
            color: #333;
        }

        #search-container {
            display: flex;
            align-items: center;
            height: 100%;
        }

        #search-input {
            padding: 10px;
            width: 300px;
            border: 1px solid #ccc;
            border-radius: 5px;
            margin: 0;
        }

        .software-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
            gap: 10px;
        }

        .software-item {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            padding: 10px;
            text-align: center;
            cursor: pointer;
            transition: transform 0.2s ease-in-out;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .software-item:hover {
            transform: translateY(-5px);
        }

        .software-icon {
            font-size: 3em;
            margin-bottom: 5px;
            color: #555;
            line-height: 1;
        }

        .software-name {
            font-weight: bold;
            color: #333;
            margin-bottom: 8px;
            line-height: 1.2;
        }

        .software-help-container {
            display: flex;
            gap: 8px;
        }

        .software-help-link {
            text-decoration: none;
            color: #888;
            display: inline-block;
            line-height: 1;
            margin-top: 5px;
            transition: color 0.2s ease-in-out;
        }

        .software-help-link .material-symbols-outlined {
            font-size: 1.5em;
            vertical-align: middle;
        }

        .software-help-link:hover {
            color: #79282a;
        }

        .software-description {
            display: none;
        }

        #help-link {
            color: white;
            text-decoration: none;
            display: flex;
            align-items: center;
        }

        #help-link span {
            margin-right: 5px;
        }

    </style>
</head>
<body>
    <div class="container">
        <div class="software-grid" id="common-links-grid">
"""

            common_items = []

            for row in reader:
                if len(row) < 2:
                    continue
                name, link = (escape(value.strip()) for value in row[:2])
                if not name or not link:
                    continue
                icon_url = escape(row[2].strip()) if len(row) > 2 else ""
                icon_html = ""
                if icon_url:
                    icon_html = f'<div class="software-icon"><img width="40" height="40" src="{icon_url}" alt=""/></div>'

                common_items.append(f"""
        <div class="software-item" data-name="{name}">
            <a href="{link}" target="_blank" style="text-decoration: none; color: inherit;">
                {icon_html}
                <div class="software-name">{name}</div>
            </a>
            <div class="software-description">{name}</div>
        </div>
                """)
            html += "\n".join(common_items)
            html += """
        </div>
    </div>
</body>
</html>
"""

            with open(output_html_path, 'w', encoding='utf-8') as html_file:
                html_file.write(html)

            print(f"HTML file '{output_html_path}' created successfully.")

    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage (replace 'your_file.csv' with the actual path to your CSV file)
if __name__ == '__main__':
    generate_quicklinks_html('ACSSSD-StudentApplications.csv')

