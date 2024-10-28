import docx
import csv
import re
import traceback

def read_word_file(file_path):
    """Read content from a Word document."""
    try:
        doc = docx.Document(file_path)
        return '\n'.join(paragraph.text for paragraph in doc.paragraphs)
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        print("Full error:")
        print(traceback.format_exc())
        raise

def parse_questions(content):
    """Parse the content into structured question data."""
    try:
        # Split content into individual questions
        questions = re.split(r'\d+\.\s+', content)[1:]  # Skip empty first split
        parsed_data = []
        
        for question_text in questions:
            if not question_text.strip():
                continue
                
            question_dict = {
                'Question': '',
                'Option_A': '',
                'Option_B': '',
                'Option_C': '',
                'Option_D': '',
                'Correct_Answer': '',
                'Explanation': ''
            }
            
            # Split into lines and clean them
            lines = [line.strip() for line in question_text.split('\n') if line.strip()]
            
            # Get question text (everything until first option)
            for i, line in enumerate(lines):
                if re.match(r'^A[\\\)|\)]', line):  # Match both A) and A\)
                    question_dict['Question'] = ' '.join(lines[:i]).strip()
                    break
            
            # Get options
            for line in lines:
                if re.match(r'^A[\\\)|\)]', line):  # Match both A) and A\)
                    question_dict['Option_A'] = re.sub(r'^A[\\\)|\)]\s*', '', line).strip()
                elif re.match(r'^B[\\\)|\)]', line):
                    question_dict['Option_B'] = re.sub(r'^B[\\\)|\)]\s*', '', line).strip()
                elif re.match(r'^C[\\\)|\)]', line):
                    question_dict['Option_C'] = re.sub(r'^C[\\\)|\)]\s*', '', line).strip()
                elif re.match(r'^D[\\\)|\)]', line):
                    question_dict['Option_D'] = re.sub(r'^D[\\\)|\)]\s*', '', line).strip()
                elif line.startswith('Correct answer:'):
                    question_dict['Correct_Answer'] = line.replace('Correct answer:', '').strip()
                elif line.startswith('Explanation:'):
                    question_dict['Explanation'] = line.replace('Explanation:', '').strip()
            
            parsed_data.append(question_dict)
        
        return parsed_data
    except Exception as e:
        print(f"Error parsing questions: {str(e)}")
        print("Full error:")
        print(traceback.format_exc())
        raise

def write_to_csv(data, output_file):
    """Write parsed data to CSV file."""
    try:
        fieldnames = ['Question', 'Option_A', 'Option_B', 'Option_C', 'Option_D', 'Correct_Answer', 'Explanation']
        
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Error writing CSV: {str(e)}")
        print("Full error:")
        print(traceback.format_exc())
        raise

def convert_word_to_csv(input_file, output_file):
    """Main function to convert Word file to CSV."""
    try:
        # Read Word document
        content = read_word_file(input_file)
        
        # Parse questions
        parsed_data = parse_questions(content)
        
        # Write to CSV
        write_to_csv(parsed_data, output_file)
        
        return f"Successfully converted {len(parsed_data)} questions to {output_file}"
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        print("Full error:")
        print(traceback.format_exc())
        return f"Error during conversion: {str(e)}"

if __name__ == "__main__":
    try:
        input_file = "SS3_Econs.docx"
        output_file = "questions.csv"
        result = convert_word_to_csv(input_file, output_file)
        print(result)
    except Exception as e:
        print(f"Main error: {str(e)}")
        print("Full error:")
        print(traceback.format_exc())