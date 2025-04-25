import requests
from typing import List, Dict, Any

def validate_product(product: Dict[str, Any]) -> List[str]:
    """Validate a single product and return list of defects."""
    defects = []
    
    # Check title
    if not isinstance(product.get('title'), str) or not product['title'].strip():
        defects.append("Empty title")
    
    # Check price
    price = product.get('price')
    if not isinstance(price, (int, float)) or price < 0:
        defects.append("Invalid price (negative or non-numeric)")
    
    # Check rating
    rating = product.get('rating', {}).get('rate')
    if not isinstance(rating, (int, float)) or rating > 5:
        defects.append("Rating exceeds 5")
    
    return defects

def test_api():
    """Test the Fake Store API and validate product data."""
    url = "https://fakestoreapi.com/products"
    
    try:
        # Make GET request
        response = requests.get(url)
        
        # Check HTTP status code
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return
        
        # Parse JSON response
        products = response.json()
        
        # Validate each product
        for product in products:
            defects = validate_product(product)
            if defects:
                print(f"\nProduct ID {product['id']} has the following defects:")
                for defect in defects:
                    print(f"- {defect}")
                print(f"Product details: {product}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
    except ValueError as e:
        print(f"Error parsing response: {e}")

if __name__ == "__main__":
    test_api() 