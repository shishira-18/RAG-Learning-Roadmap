import os 
import re
# Function to load and parse markdown content
def load_chapter_content(file_path):
    try:
        with open(os.path.join("docs", file_path), "r", encoding="utf-8") as f:
            content = f.read()
        def parse_content(content):
            segments = []
            lines = content.split("\n")
            current_text = []
            image_pattern = r"!\[(.*?)\]\((.*?)\)"
            
            for line in lines:
                image_match = re.match(image_pattern, line.strip())
                if image_match:
                    if current_text:
                        segments.append({"type": "text", "content": "\n".join(current_text)})
                        current_text = []
                    segments.append({"type": "image", "alt_text": image_match.group(1), "url": "docs/"+image_match.group(2)})
                else:
                    current_text.append(line)
            if current_text:
                segments.append({"type": "text", "content": "\n".join(current_text)})
            return segments
        parsed_segments = parse_content(content)
        return parsed_segments
    except FileNotFoundError:
        return "chapter needs to be added."
    except Exception as e:
        print(f"Error loading chapter content from {file_path}: {e}")