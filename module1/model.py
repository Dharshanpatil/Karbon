
import json
from rules import latest_financial_index

def analyze_data(data):
    result = {}
    result['latest_financial_index'] = latest_financial_index(data)

    return result

if __name__ == "__main__":
    with open('data.json', 'r') as f:
        data = json.load(f)
    
    result = analyze_data(data)
    print(json.dumps(result, indent=4))
